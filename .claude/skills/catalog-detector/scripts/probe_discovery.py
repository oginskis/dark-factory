# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
"""
Parse robots.txt, sitemaps, and homepage links to discover product URLs.

WHEN TO CALL: After probe_access confirms the site is reachable. Independent of
    probe_platform — can run in parallel.

ARGUMENTS:
    --url                Target website URL (required)
    --timeout            HTTP timeout in seconds (default: 15.0)
    --delay              Inter-request delay in seconds (default: 0)
    --max-response-size  Max response bytes (default: 2_000_000)
    --max-product-samples  Number of product URLs to sample (default: 5)

EXIT CODES:
    0 = full result
    1 = partial result (errors[] explains gaps)
    2 = script crash (fall back to manual reasoning)

INTERPRETATION:
    sitemap.found == false → use category traversal for product discovery; note in assessment
    sitemap.sample_success_rate below 80% → URLs may be stale or behind auth; verify manually
    robots_txt.crawl_delay → record in assessment for reference; scrapers use adaptive backoff instead
    sitemap.product_url_count == 0 AND homepage_links.catalog_links == [] →
        likely no_public_catalog stop
    sample_product_urls → pass directly to probe_recipe via --product-urls
    json_ld_on_homepage contains "Product" → structured data likely available on product pages;
        prioritise structured_data strategy
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse

from selectolax.parser import HTMLParser

from _probe_lib import fetch, log, make_client, TransportTracker


def parse_robots_txt(text: str) -> dict:
    sitemaps = []
    disallowed = []
    crawl_delay = None
    for line in text.split("\n"):
        line = line.strip()
        if line.lower().startswith("sitemap:"):
            sitemaps.append(line.split(":", 1)[1].strip())
        elif line.lower().startswith("disallow:"):
            path = line.split(":", 1)[1].strip()
            if path:
                disallowed.append(path)
        elif line.lower().startswith("crawl-delay:"):
            try:
                crawl_delay = int(line.split(":", 1)[1].strip())
            except ValueError:
                pass
    return {"sitemaps": sitemaps, "disallowed_paths": disallowed, "crawl_delay": crawl_delay}


PRODUCT_URL_PATTERNS = re.compile(r"/product/|/p/|\.html|/shop/|/collections/|/toode/")
MAX_SITEMAP_DEPTH = 3
MAX_PRODUCT_URLS = 10_000


def parse_sitemap(client, url: str, *, timeout: float, delay: float,
                  max_size: int, tracker: TransportTracker,
                  depth: int = 0) -> list[str]:
    """Parse a sitemap (or sitemap index) and return product-like URLs."""
    if depth > MAX_SITEMAP_DEPTH:
        log("warning", "Sitemap recursion depth exceeded", url=url, depth=depth)
        return []

    text, status, _, _, _ = fetch(client, url, timeout=timeout, delay=delay,
                                   max_size=max_size, tracker=tracker)
    if not text or status != 200:
        return []

    urls = []
    try:
        clean = re.sub(r'\sxmlns="[^"]+"', '', text, count=1)
        root = ET.fromstring(clean)
    except ET.ParseError:
        log("warning", "Failed to parse sitemap XML", url=url)
        return []

    if root.tag == "sitemapindex" or root.findall("sitemap"):
        for sitemap_el in root.findall(".//sitemap/loc"):
            if sitemap_el.text and len(urls) < MAX_PRODUCT_URLS:
                child_urls = parse_sitemap(client, sitemap_el.text.strip(),
                                           timeout=timeout, delay=delay,
                                           max_size=max_size, tracker=tracker,
                                           depth=depth + 1)
                urls.extend(child_urls)
    else:
        for loc in root.findall(".//url/loc"):
            if loc.text:
                u = loc.text.strip()
                if PRODUCT_URL_PATTERNS.search(u):
                    urls.append(u)
                    if len(urls) >= MAX_PRODUCT_URLS:
                        break

    return urls


def sample_diverse(urls: list[str], n: int) -> list[str]:
    """Sample n URLs from diverse positions (beginning, middle, end)."""
    if len(urls) <= n:
        return list(urls)
    step = len(urls) // n
    return [urls[i * step] for i in range(n)]


def extract_homepage_links(html: str, base_url: str) -> dict:
    tree = HTMLParser(html)
    catalog_keywords = {"product", "shop", "catalog", "collection", "price", "buy", "store"}
    catalog_links = []
    nav_categories = []

    for link in tree.css("a[href]"):
        href = link.attributes.get("href", "")
        text = link.text(strip=True)
        if not href or href.startswith("#") or href.startswith("javascript:"):
            continue
        href_lower = href.lower()
        if any(kw in href_lower for kw in catalog_keywords):
            if href.startswith("/"):
                catalog_links.append(href)
            elif href.startswith(base_url):
                catalog_links.append(href.replace(base_url, ""))

    for nav in tree.css("nav, .nav, .menu, .main-menu"):
        for link in nav.css("a"):
            text = link.text(strip=True)
            if text and len(text) > 2 and len(text) < 50:
                nav_categories.append(text)

    return {
        "catalog_links": list(set(catalog_links))[:10],
        "nav_categories": list(dict.fromkeys(nav_categories))[:20],
    }


def guess_url_pattern(urls: list[str]) -> str | None:
    """Guess a URL template from a sample of URLs."""
    if not urls:
        return None
    paths = [urlparse(u).path for u in urls[:20]]
    if all(p.endswith(".html") for p in paths):
        return "/{path}.html"
    if all("/product/" in p for p in paths):
        return "/product/{slug}"
    if all("/p/" in p for p in paths):
        return "/p/{id}-{slug}"
    if all("/products/" in p for p in paths):
        return "/products/{handle}"
    return None


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Discover product URLs via robots/sitemap/links")
    parser.add_argument("--url", required=True, help="Target website URL")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--delay", type=float, default=0)
    parser.add_argument("--max-response-size", type=int, default=2_000_000)
    parser.add_argument("--max-product-samples", type=int, default=5)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracker = TransportTracker()
    errors: list[dict] = []

    result: dict = {
        "robots_txt": {
            "found": False,
            "status": None,
            "sitemaps": [],
            "disallowed_paths": [],
            "crawl_delay": None,
            # crawl_delay → copy value into scraper config; respect between requests
        },
        "sitemap": {
            "found": False,
            # false → use category traversal for product discovery
            "urls_checked": [],
            "product_url_count": 0,
            "product_url_count_truncated": False,
            "product_url_pattern_guess": None,
            "sample_product_urls": [],
            "sample_success_rate": "0/0",
            # below 80% → URLs may be stale or behind auth; verify manually
        },
        "homepage_links": {
            "catalog_links": [],
            "nav_categories": [],
        },
        "json_ld_on_homepage": [],
        # contains "Product" → structured data likely available on product pages
        "errors": errors,
    }

    try:
        with make_client() as client:
            # Fetch homepage for links and JSON-LD
            hp_text, hp_status, _, hp_headers, hp_final_url = fetch(
                client, args.url, timeout=args.timeout,
                delay=0, max_size=args.max_response_size, tracker=tracker)

            base_url = hp_final_url or args.url

            if not hp_text:
                errors.append({"section": "homepage", "error": "Homepage unreachable"})
            else:
                # Homepage links
                result["homepage_links"] = extract_homepage_links(hp_text, base_url)

                # JSON-LD on homepage
                tree = HTMLParser(hp_text)
                json_ld_types = []
                for script in tree.css('script[type="application/ld+json"]'):
                    try:
                        data = json.loads(script.text(strip=True))
                        if isinstance(data, dict):
                            if "@type" in data:
                                json_ld_types.append(data["@type"])
                            for item in data.get("@graph", []):
                                if isinstance(item, dict) and "@type" in item:
                                    json_ld_types.append(item["@type"])
                    except (json.JSONDecodeError, AttributeError):
                        pass
                result["json_ld_on_homepage"] = json_ld_types

            # Robots.txt
            robots_url = urljoin(base_url, "/robots.txt")
            robots_text, robots_status, _, _, _ = fetch(client, robots_url, timeout=args.timeout,
                                                        delay=args.delay, max_size=100_000,
                                                        tracker=tracker)
            if robots_text and robots_status == 200:
                robots = parse_robots_txt(robots_text)
                result["robots_txt"] = {"found": True, "status": 200, **robots}
            else:
                result["robots_txt"]["status"] = robots_status

            # Sitemaps
            sitemap_urls_to_check = result["robots_txt"].get("sitemaps") or [
                urljoin(base_url, "/sitemap.xml")
            ]
            all_product_urls: list[str] = []
            for sm_url in sitemap_urls_to_check:
                product_urls = parse_sitemap(client, sm_url, timeout=args.timeout,
                                             delay=args.delay, max_size=args.max_response_size,
                                             tracker=tracker)
                all_product_urls.extend(product_urls)

            truncated = len(all_product_urls) >= MAX_PRODUCT_URLS
            samples = sample_diverse(all_product_urls, args.max_product_samples)

            # Check sample accessibility
            ok_count = 0
            for s_url in samples:
                _, s_status, _, _, _ = fetch(client, s_url, timeout=args.timeout,
                                             delay=args.delay, max_size=args.max_response_size,
                                             tracker=tracker)
                if s_status == 200:
                    ok_count += 1

            result["sitemap"] = {
                "found": bool(all_product_urls),
                "urls_checked": sitemap_urls_to_check,
                "product_url_count": min(len(all_product_urls), MAX_PRODUCT_URLS),
                "product_url_count_truncated": truncated,
                "product_url_pattern_guess": guess_url_pattern(all_product_urls[:100]),
                "sample_product_urls": samples,
                "sample_success_rate": f"{ok_count}/{len(samples)}" if samples else "0/0",
            }

    except Exception as exc:
        log("error", "Script crashed", error=str(exc))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
