# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
"""
Probe a website for platform detection, anti-bot assessment, and recipe verification.

Reports evidence as JSON to stdout. The LLM decides how to route based on findings.
Exit codes: 0 = full result, 1 = partial (errors array explains gaps), 2 = script crash.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin, urlparse

import httpx
from selectolax.parser import HTMLParser


def log(level: str, message: str, **extra: object) -> None:
    entry = {"level": level, "message": message,
             "timestamp": datetime.now(timezone.utc).isoformat(), **extra}
    print(json.dumps(entry), file=sys.stderr)


CHALLENGE_PATTERNS = [
    "you have been blocked",
    "access denied",
    "challenge-platform",
    "cf-browser-verification",
    "just a moment",
    "cf-turnstile",
    "_cf_chl_opt",
    "checking if the site connection is secure",
    "challenges.cloudflare.com",
    "g-recaptcha",
    "h-captcha",
    "captcha",
]


def detect_challenge_page(html: str) -> bool:
    html_lower = html.lower()
    return any(p in html_lower for p in CHALLENGE_PATTERNS)


def find_blocked_keywords(html: str) -> list[str]:
    html_lower = html.lower()
    return list({p for p in CHALLENGE_PATTERNS if p in html_lower})


class TransportTracker:
    """Tracks HTTP request outcomes across the entire probe run."""

    def __init__(self) -> None:
        self.total = 0
        self.status_200 = 0
        self.status_429 = 0
        self.status_403 = 0
        self.status_other = 0
        self.timeouts = 0
        self.challenge_pages = 0
        self.rate_limited = False

    def record(self, status: int | None, is_challenge: bool = False) -> None:
        self.total += 1
        if status is None:
            self.timeouts += 1
        elif status == 200:
            self.status_200 += 1
        elif status == 429:
            self.status_429 += 1
            self.rate_limited = True
        elif status == 403:
            self.status_403 += 1
        else:
            self.status_other += 1
        if is_challenge:
            self.challenge_pages += 1

    def summary(self, delay: float) -> dict:
        total_non_ok = self.total - self.status_200
        if self.status_403 + self.status_429 + self.challenge_pages > self.total / 2:
            overall = "blocked"
        elif total_non_ok > 0 or self.timeouts > 0:
            overall = "degraded"
        else:
            overall = "healthy"
        return {
            "total_requests": self.total,
            "status_200_count": self.status_200,
            "status_429_count": self.status_429,
            "status_403_count": self.status_403,
            "status_other_count": self.status_other,
            "timeouts": self.timeouts,
            "suspected_challenge_pages": self.challenge_pages,
            "inter_request_delay_used": delay,
            "overall": overall,
        }


def fetch(client: httpx.Client, url: str, *, timeout: float, delay: float,
          max_size: int, tracker: TransportTracker) -> tuple[str | None, int | None, bool, dict, str | None]:
    """Fetch URL. Returns (text, status, truncated, headers, final_url). Handles 429 retry."""
    time.sleep(delay)
    log("info", "Fetching", url=url)
    try:
        resp = client.get(url, timeout=timeout)
    except httpx.TimeoutException:
        log("warning", "Timeout", url=url)
        tracker.record(None)
        return None, None, False, {}, None
    except httpx.RequestError as exc:
        log("warning", "Request error", url=url, error=str(exc))
        tracker.record(None)
        return None, None, False, {}, None

    # Handle 429 with one retry
    if resp.status_code == 429:
        retry_after = int(resp.headers.get("Retry-After", "5"))
        log("warning", "Rate limited", url=url, status=429, retry_after=retry_after)
        time.sleep(min(retry_after, 30))
        try:
            resp = client.get(url, timeout=timeout)
        except (httpx.TimeoutException, httpx.RequestError):
            tracker.record(429)
            return None, 429, False, {}, None
        if resp.status_code == 429:
            tracker.record(429)
            return None, 429, False, {}, None

    status = resp.status_code
    # Get text with encoding handling
    if resp.encoding is None:
        text = resp.content[:max_size].decode("utf-8", errors="replace")
    else:
        text = resp.text
    truncated = len(resp.content) > max_size
    if truncated:
        text = text[:max_size]
        log("warning", "Response truncated", url=url,
            original_size=len(resp.content), truncated_to=max_size)

    is_challenge = detect_challenge_page(text) if status == 200 else False
    tracker.record(status, is_challenge)
    resp_headers = dict(resp.headers)
    final_url = str(resp.url)
    return text, status, truncated, resp_headers, final_url


PLATFORM_SIGNALS = {
    "meta_generator": None,  # extracted from <meta name="generator">
    "powered_by_header": None,  # X-Powered-By header
    "shopify_cdn": False,
    "wp_content_path": False,
    "prestashop_modules_path": False,
    "magento_static_version": False,
    "woocommerce_body_class": False,
    "bigcommerce_cdn": False,
    "squarespace_static": False,
    "wix_static": False,
    "drupal_settings": False,
}

# Map signal keys to platform names
SIGNAL_TO_PLATFORM = {
    "shopify_cdn": "shopify",
    "wp_content_path": "woocommerce",  # WordPress, but WooCommerce is the e-commerce layer
    "prestashop_modules_path": "prestashop",
    "magento_static_version": "magento",
    "woocommerce_body_class": "woocommerce",
    "bigcommerce_cdn": "bigcommerce",
    "squarespace_static": "squarespace",
    "wix_static": "wix",
    "drupal_settings": "drupal",
}


def detect_platform_signals(html: str, headers: dict) -> dict:
    signals = dict(PLATFORM_SIGNALS)
    tree = HTMLParser(html)

    # Meta generator
    meta = tree.css_first('meta[name="generator"]')
    if meta:
        signals["meta_generator"] = meta.attributes.get("content")

    # Response headers
    signals["powered_by_header"] = headers.get("x-powered-by")

    # Path/content patterns
    html_lower = html.lower()
    signals["shopify_cdn"] = "cdn.shopify.com" in html_lower
    signals["wp_content_path"] = "/wp-content/" in html_lower
    signals["prestashop_modules_path"] = "/modules/" in html_lower and "prestashop" in html_lower
    signals["magento_static_version"] = bool(re.search(r"/static/version\d+/", html))
    signals["woocommerce_body_class"] = "woocommerce" in html_lower
    signals["bigcommerce_cdn"] = "bigcommerce.com" in html_lower
    signals["squarespace_static"] = "squarespace.com/static" in html_lower or "squarespace-cdn.com" in html_lower
    signals["wix_static"] = "static.wixstatic.com" in html_lower
    signals["drupal_settings"] = "drupalSettings" in html or "drupal.js" in html_lower

    return signals


def guess_platform(signals: dict) -> tuple[str, str, int, bool, str | None]:
    """Returns (guess, confidence, signal_count, conflict, version)."""
    # Count positive signals per platform
    platform_hits: dict[str, int] = {}
    for key, platform in SIGNAL_TO_PLATFORM.items():
        if signals.get(key):
            platform_hits[platform] = platform_hits.get(platform, 0) + 1

    # Check meta_generator for definitive match
    meta = signals.get("meta_generator") or ""
    meta_lower = meta.lower()
    meta_platform = None
    for name in ["prestashop", "shopify", "magento", "woocommerce", "drupal",
                 "bigcommerce", "squarespace", "wix", "opencart"]:
        if name in meta_lower:
            meta_platform = name
            break

    signal_count = sum(1 for k, v in signals.items() if v and k in SIGNAL_TO_PLATFORM)
    conflict = len(platform_hits) > 1

    if meta_platform:
        return meta_platform, "definitive", signal_count, conflict, meta.strip()

    if platform_hits:
        best = max(platform_hits, key=platform_hits.get)
        confidence = "likely" if platform_hits[best] >= 2 else "weak"
        return best, confidence, signal_count, conflict, None

    return "unknown", "none", 0, False, None


def analyze_anti_bot(html: str, content_length: int, body_text_length: int,
                     tree: HTMLParser) -> dict:
    is_challenge = detect_challenge_page(html)
    # Check for empty shell: big HTML but tiny text, no structural elements
    has_nav = tree.css_first("nav") is not None
    has_article = tree.css_first("article") is not None
    has_main = tree.css_first("main") is not None
    substantial_structure = has_nav or has_article or has_main
    suspected_shell = content_length > 1000 and body_text_length < 500 and not substantial_structure

    return {
        "homepage_content_length": content_length,
        "challenge_page_detected": is_challenge,
        "suspected_empty_shell": suspected_shell,
        "cloudflare_ray": None,  # filled from headers
        "cloudflare_challenge": "cf-turnstile" in html.lower() or "_cf_chl_opt" in html.lower(),
        "captcha_detected": "g-recaptcha" in html.lower() or "h-captcha" in html.lower(),
        "datadome_detected": "datadome" in html.lower(),
        "perimeterx_detected": "perimeterx" in html.lower() or "_pxhd" in html.lower(),
        "blocked_keywords_found": find_blocked_keywords(html),
        "product_page_status": None,  # filled later
        "product_page_accessible": None,  # filled later
    }


def analyze_js_rendering(html: str, content_length: int) -> dict:
    tree = HTMLParser(html)
    # Strip scripts and styles for body text length
    for tag in tree.css("script, style"):
        tag.decompose()
    body = tree.css_first("body")
    body_text = body.text(strip=True) if body else ""
    body_text_length = len(body_text)

    # Framework detection
    framework = None
    if "__NEXT_DATA__" in html:
        framework = "nextjs"
    elif "window.__NUXT__" in html or "__nuxt" in html:
        framework = "nuxt"
    elif "ng-app" in html or "ng-version" in html:
        framework = "angular"
    elif "data-reactroot" in html:
        framework = "react"
    elif re.search(r'data-v-[a-f0-9]', html):
        framework = "vue"

    # Reparse for container check (previous decompose modified tree)
    tree2 = HTMLParser(html)
    empty_container = False
    for sel in [".products", "#product-list", "[data-products]"]:
        el = tree2.css_first(sel)
        if el and not el.text(strip=True):
            empty_container = True
            break

    ratio = body_text_length / content_length if content_length > 0 else 0
    return {
        "body_text_length": body_text_length,
        "noscript_tag_found": "<noscript" in html.lower(),
        "framework_detected": framework,
        "empty_product_container": empty_container,
        "text_to_html_ratio": round(ratio, 3),
    }


def extract_geo_hints(html: str, headers: dict, final_url: str) -> dict:
    tree = HTMLParser(html)
    html_tag = tree.css_first("html")
    html_lang = html_tag.attributes.get("lang") if html_tag else None
    vary = headers.get("vary", "")
    parsed = urlparse(final_url)
    path_segments = [s for s in parsed.path.split("/") if s]
    country_seg = None
    geo_patterns = re.compile(r"^(en-gb|en-us|de|fr|nl|es|it|pt|pl|sv|da|no|fi|cs|ru|ja|zh|ko|lv|et|lt)$", re.I)
    for seg in path_segments[:2]:
        if geo_patterns.match(seg):
            country_seg = seg.lower()
            break

    return {
        "vary_accept_language": "accept-language" in vary.lower(),
        "html_lang": html_lang,
        "geo_redirect_detected": country_seg is not None,
        "country_path_segment": country_seg,
    }


def get_body_text_length(html: str) -> int:
    tree = HTMLParser(html)
    for tag in tree.css("script, style"):
        tag.decompose()
    body = tree.css_first("body")
    return len(body.text(strip=True)) if body else 0


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


def parse_sitemap(client: httpx.Client, url: str, *, timeout: float, delay: float,
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
        # Strip namespace for easier parsing
        clean = re.sub(r'\sxmlns="[^"]+"', '', text, count=1)
        root = ET.fromstring(clean)
    except ET.ParseError:
        log("warning", "Failed to parse sitemap XML", url=url)
        return []

    # Check if sitemap index
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
        # Catalog link detection
        if any(kw in href_lower for kw in catalog_keywords):
            if href.startswith("/"):
                catalog_links.append(href)
            elif href.startswith(base_url):
                catalog_links.append(href.replace(base_url, ""))

    # Nav categories from main navigation
    for nav in tree.css("nav, .nav, .menu, .main-menu"):
        for link in nav.css("a"):
            text = link.text(strip=True)
            if text and len(text) > 2 and len(text) < 50:
                nav_categories.append(text)

    return {
        "catalog_links": list(set(catalog_links))[:10],
        "nav_categories": list(dict.fromkeys(nav_categories))[:20],
    }


def extract_md_section(content: str, heading: str) -> str | None:
    """Extract content under a ## heading."""
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def parse_knowledgebase(kb_path: Path) -> dict:
    """Parse CSS selectors, JSON-LD patterns, pagination, and API endpoints from a knowledgebase file."""
    content = kb_path.read_text(encoding="utf-8")
    result = {
        "css_selectors": [],
        "json_ld_types": [],
        "pagination_url_pattern": None,
        "products_per_page": None,
        "api_endpoints": [],
    }

    # Parse CSS Selectors table
    css_section = extract_md_section(content, "CSS Selectors")
    if css_section:
        for line in css_section.split("\n"):
            if not line.strip().startswith("|") or "---" in line:
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2 and cells[0].lower() != "element":
                # Extract selector from backticks
                selector_match = re.search(r"`([^`]+)`", cells[1])
                if selector_match:
                    result["css_selectors"].append({
                        "element": cells[0],
                        "selector": selector_match.group(1),
                        "notes": cells[2] if len(cells) > 2 else "",
                    })

    # Parse JSON-LD Patterns
    jsonld_section = extract_md_section(content, "JSON-LD Patterns")
    if jsonld_section:
        for schema_type in ["Product", "BreadcrumbList", "AggregateOffer", "Offer"]:
            if schema_type.lower() in jsonld_section.lower():
                result["json_ld_types"].append(schema_type)

    # Parse Pagination
    pagination_section = extract_md_section(content, "Pagination")
    if pagination_section:
        url_match = re.search(r"URL pattern:\s*`?([^`\n]+)`?", pagination_section)
        if url_match:
            result["pagination_url_pattern"] = url_match.group(1).strip()
        pp_match = re.search(r"Products per page:\s*(\d+)", pagination_section)
        if pp_match:
            result["products_per_page"] = int(pp_match.group(1))

    # Parse API endpoints (Shopify JSON API or similar named sections)
    for section_name in ["Shopify JSON API", "API Endpoints", "JSON API"]:
        api_section = extract_md_section(content, section_name)
        if api_section:
            for match in re.finditer(r"`(/[^`]+\.json[^`]*)`", api_section):
                result["api_endpoints"].append(match.group(1))
            break

    return result


def verify_recipe(client: httpx.Client, product_urls: list[str],
                  kb: dict, *, timeout: float, delay: float,
                  max_size: int, tracker: TransportTracker) -> list[dict]:
    checks = []
    for url in product_urls:
        text, status, truncated, _, _ = fetch(client, url, timeout=timeout, delay=delay,
                                               max_size=max_size, tracker=tracker)
        if not text or (status and status != 200):
            checks.append({"url": url, "status": status, "page_truncated": truncated,
                           "body_text_length": 0, "json_ld_product_found": False,
                           "json_ld_extracted": None, "css_checks": [], "api_checks": [],
                           "attribute_selectors_tested": []})
            continue

        body_text_len = get_body_text_length(text)
        tree = HTMLParser(text)

        # JSON-LD extraction
        json_ld_product = None
        for script in tree.css('script[type="application/ld+json"]'):
            try:
                data = json.loads(script.text(strip=True))
                if isinstance(data, dict):
                    if data.get("@type") == "Product":
                        json_ld_product = data
                        break
                    # Handle @graph-wrapped JSON-LD (WooCommerce pattern)
                    for item in data.get("@graph", []):
                        if isinstance(item, dict) and item.get("@type") == "Product":
                            json_ld_product = item
                            break
                    if json_ld_product:
                        break
            except (json.JSONDecodeError, AttributeError):
                pass

        json_ld_extracted = None
        if json_ld_product:
            offers = json_ld_product.get("offers", {})
            if isinstance(offers, list):
                offers = offers[0] if offers else {}
            brand = json_ld_product.get("brand", {})
            brand_name = brand.get("name") if isinstance(brand, dict) else str(brand)
            json_ld_extracted = {
                "name": str(json_ld_product.get("name", ""))[:200],
                "sku": str(json_ld_product.get("sku", ""))[:200],
                "price": str(offers.get("price", offers.get("lowPrice", "")))[:50],
                "currency": str(offers.get("priceCurrency", ""))[:10],
                "brand": str(brand_name or "")[:200],
            }

        # CSS selector checks (cap at 10)
        css_checks = []
        for sel_info in kb["css_selectors"][:10]:
            selector = sel_info["selector"]
            el = tree.css_first(selector)
            extracted = el.text(strip=True)[:200] if el else ""
            css_checks.append({
                "selector": selector,
                "extracted": extracted,
                "non_empty": bool(extracted),
            })

        # API checks
        api_checks = []
        for endpoint in kb["api_endpoints"]:
            api_url = urljoin(url, endpoint)
            api_text, api_status, _, _, _ = fetch(client, api_url, timeout=timeout,
                                                   delay=delay, max_size=max_size, tracker=tracker)
            has_data = False
            if api_text and api_status == 200:
                try:
                    api_data = json.loads(api_text)
                    has_data = bool(api_data)
                except json.JSONDecodeError:
                    pass
            api_checks.append({"endpoint": endpoint, "status": api_status, "has_data": has_data})

        # Attribute selectors (check for spec tables or variant containers)
        attr_selectors = []
        for sel in [".product-variants .form-group", "table.data.table tr",
                    "#product-attribute-specs-table tr", "dl.product-attributes dt"]:
            els = tree.css(sel)
            if els:
                attr_selectors.append({"selector": sel, "count": len(els)})

        checks.append({
            "url": url,
            "status": status,
            "page_truncated": truncated,
            "body_text_length": body_text_len,
            "json_ld_product_found": json_ld_product is not None,
            "json_ld_extracted": json_ld_extracted,
            "css_checks": css_checks,
            "api_checks": api_checks,
            "attribute_selectors_tested": attr_selectors,
        })

    return checks


def check_pagination(client: httpx.Client, product_urls: list[str],
                     kb: dict, *, timeout: float, delay: float,
                     max_size: int, tracker: TransportTracker) -> dict:
    """Try to find a category page and verify pagination works."""
    # Try to derive a category URL from a product URL
    pagination_pattern = kb.get("pagination_url_pattern")
    if not pagination_pattern or not product_urls:
        return {"tested": False, "reason": "no pagination pattern or product URLs available"}

    # Attempt: strip product slug from a product URL to get category
    sample_url = product_urls[0]
    parsed = urlparse(sample_url)
    path_parts = [p for p in parsed.path.split("/") if p]
    if len(path_parts) >= 2:
        category_path = "/" + "/".join(path_parts[:-1])
        category_url = f"{parsed.scheme}://{parsed.netloc}{category_path}"
    else:
        return {"tested": False, "reason": "cannot derive category URL from product URL"}

    # Fetch page 1
    text1, status1, _, _, _ = fetch(client, category_url, timeout=timeout, delay=delay,
                                     max_size=max_size, tracker=tracker)
    if not text1 or status1 != 200:
        return {"tested": False, "reason": f"category page returned {status1}"}

    tree1 = HTMLParser(text1)
    parsed_base = urlparse(category_url)

    def collect_links(tree: HTMLParser) -> set[str]:
        links = set()
        for a in tree.css("a[href]"):
            href = a.attributes.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            # Normalize relative to absolute
            if href.startswith("/"):
                full = f"{parsed_base.scheme}://{parsed_base.netloc}{href}"
            elif href.startswith("http"):
                full = href
            else:
                continue
            # Include any path with 2+ segments and no query string that looks product-like
            ph = urlparse(full)
            if ph.netloc == parsed_base.netloc and len([s for s in ph.path.split("/") if s]) >= 2:
                links.add(ph.path)
        return links

    p1_links = collect_links(tree1)

    # Build page 2 URL
    if "?page=" in pagination_pattern or "?p=" in pagination_pattern:
        page2_url = category_url + "?page=2"
    elif "/page/" in pagination_pattern:
        page2_url = category_url.rstrip("/") + "/page/2/"
    else:
        page2_url = category_url + "?page=2"

    text2, status2, _, _, _ = fetch(client, page2_url, timeout=timeout, delay=delay,
                                     max_size=max_size, tracker=tracker)
    if not text2 or status2 != 200:
        return {"tested": True, "category_url": category_url,
                "page1_product_count": len(p1_links),
                "page2_url": page2_url, "page2_status": status2,
                "page2_product_count": 0, "products_differ": False}

    tree2 = HTMLParser(text2)
    p2_links = collect_links(tree2)

    return {
        "tested": True,
        "category_url": category_url,
        "page1_product_count": len(p1_links),
        "page2_url": page2_url,
        "page2_status": status2,
        "page2_product_count": len(p2_links),
        "products_differ": bool(p2_links - p1_links),
    }


def compute_recipe_match(checks: list[dict], pagination: dict) -> str:
    if not checks:
        return "untested"
    total_checks = 0
    passed_checks = 0
    for check in checks:
        if check["status"] != 200:
            continue
        # JSON-LD check
        total_checks += 1
        if check["json_ld_product_found"]:
            passed_checks += 1
        # CSS checks
        for css in check["css_checks"]:
            total_checks += 1
            if css["non_empty"]:
                passed_checks += 1

    if total_checks == 0:
        return "untested"

    ratio = passed_checks / total_checks
    pagination_tested = pagination.get("tested", False)

    if ratio == 1.0 and pagination_tested and pagination.get("products_differ", False):
        return "full"
    if ratio > 0.5:
        return "partial"
    return "poor"


def guess_url_pattern(urls: list[str]) -> str | None:
    """Guess a URL template from a sample of URLs."""
    if not urls:
        return None
    paths = [urlparse(u).path for u in urls[:20]]
    # Find common suffixes
    if all(p.endswith(".html") for p in paths):
        return "/{path}.html"
    if all("/product/" in p for p in paths):
        return "/product/{slug}"
    if all("/p/" in p for p in paths):
        return "/p/{id}-{slug}"
    if all("/products/" in p for p in paths):
        return "/products/{handle}"
    return None


RECIPE_RANK = {"full": 3, "partial": 2, "poor": 1, "untested": 0}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe website for catalog detection")
    parser.add_argument("--url", required=True, help="Company website URL")
    parser.add_argument("--knowledgebase-dir", required=True, type=Path,
                        help="Path to platform knowledgebase directory")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--max-product-samples", type=int, default=5)
    parser.add_argument("--max-response-size", type=int, default=2_000_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracker = TransportTracker()
    errors: list[dict] = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    result: dict = {
        "url": args.url,
        "final_url": args.url,
        "redirected": False,
        "cross_domain_redirect": False,
        "homepage_status": None,
        "errors": errors,
        "rate_limited": False,
    }

    try:
        with httpx.Client(headers=headers, follow_redirects=True, max_redirects=10) as client:
            # 1. Fetch homepage
            hp_text, hp_status, _, hp_headers, hp_final_url = fetch(
                client, args.url, timeout=args.timeout,
                delay=0, max_size=args.max_response_size, tracker=tracker)
            result["homepage_status"] = hp_status

            if not hp_text:
                errors.append({"section": "homepage", "error": "Homepage unreachable"})
                result["transport_health"] = tracker.summary(args.delay)
                print(json.dumps(result, indent=2))
                sys.exit(1)

            # Redirect detection
            if hp_final_url and hp_final_url != args.url:
                result["final_url"] = hp_final_url
                result["redirected"] = True
                input_domain = urlparse(args.url).netloc.replace("www.", "")
                final_domain = urlparse(hp_final_url).netloc.replace("www.", "")
                result["cross_domain_redirect"] = input_domain != final_domain
            else:
                result["final_url"] = hp_final_url or args.url

            # 2. Platform detection
            resp_headers = hp_headers
            signals = detect_platform_signals(hp_text, resp_headers)
            guess, confidence, sig_count, conflict, version = guess_platform(signals)
            result["platform_signals"] = signals
            result["platform_guess"] = guess
            result["platform_confidence"] = confidence
            result["platform_signal_count"] = sig_count
            result["platform_conflict"] = conflict
            result["platform_version"] = version

            # 3. Anti-bot
            body_text_len = get_body_text_length(hp_text)
            result["anti_bot"] = analyze_anti_bot(hp_text, len(hp_text), body_text_len, HTMLParser(hp_text))
            result["anti_bot"]["cloudflare_ray"] = resp_headers.get("cf-ray")
            result["js_rendering_signals"] = analyze_js_rendering(hp_text, len(hp_text))
            result["geo_hints"] = extract_geo_hints(hp_text, resp_headers, result["final_url"])

            # 4. JSON-LD on homepage
            tree = HTMLParser(hp_text)
            json_ld_types = []
            for script in tree.css('script[type="application/ld+json"]'):
                try:
                    data = json.loads(script.text(strip=True))
                    if isinstance(data, dict):
                        if "@type" in data:
                            json_ld_types.append(data["@type"])
                        # Handle @graph wrapper
                        for item in data.get("@graph", []):
                            if isinstance(item, dict) and "@type" in item:
                                json_ld_types.append(item["@type"])
                except (json.JSONDecodeError, AttributeError):
                    pass
            result["json_ld_on_homepage"] = json_ld_types

            # 5. Robots.txt
            robots_url = urljoin(result["final_url"], "/robots.txt")
            robots_text, robots_status, _, _, _ = fetch(client, robots_url, timeout=args.timeout,
                                                      delay=args.delay, max_size=100_000,
                                                      tracker=tracker)
            if robots_text and robots_status == 200:
                robots = parse_robots_txt(robots_text)
                result["robots_txt"] = {"found": True, "status": 200, **robots}
            else:
                result["robots_txt"] = {"found": False, "status": robots_status,
                                        "sitemaps": [], "disallowed_paths": [], "crawl_delay": None}

            # 6. Sitemap
            sitemap_urls_to_check = result["robots_txt"]["sitemaps"] or [
                urljoin(result["final_url"], "/sitemap.xml")
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

            # 7. Homepage links
            result["homepage_links"] = extract_homepage_links(hp_text, result["final_url"])

            # 8. Recipe verification (supports multi-platform on conflict)
            platforms_to_test = [guess]
            if conflict:
                # Also test other detected platforms
                for sig_key, plat in SIGNAL_TO_PLATFORM.items():
                    if signals.get(sig_key) and plat != guess and plat not in platforms_to_test:
                        platforms_to_test.append(plat)

            best_recipe = None
            for test_platform in platforms_to_test:
                kb_file = args.knowledgebase_dir / f"{test_platform}.md"
                if not kb_file.exists():
                    continue
                kb = parse_knowledgebase(kb_file)
                recipe_samples = samples[:args.max_product_samples] if samples else []
                checks = verify_recipe(client, recipe_samples, kb, timeout=args.timeout,
                                       delay=args.delay, max_size=args.max_response_size,
                                       tracker=tracker)
                pagination = check_pagination(client, all_product_urls[:10], kb,
                                              timeout=args.timeout, delay=args.delay,
                                              max_size=args.max_response_size, tracker=tracker)
                recipe_match = compute_recipe_match(checks, pagination)
                candidate = {
                    "knowledgebase_file": kb_file.name,
                    "knowledgebase_found": True,
                    "knowledgebase_selectors_parsed": len(kb["css_selectors"]),
                    "knowledgebase_api_endpoints_parsed": len(kb["api_endpoints"]),
                    "recipe_match": recipe_match,
                    "product_pages_tested": len(checks),
                    "checks": checks,
                    "pagination_check": pagination,
                }
                # Keep the best-matching platform result
                if best_recipe is None or RECIPE_RANK.get(recipe_match, 0) > RECIPE_RANK.get(best_recipe["recipe_match"], 0):
                    best_recipe = candidate

                # Check product page for anti-bot (from first platform tested only)
                if result["anti_bot"]["product_page_status"] is None:
                    if checks and checks[0]["status"] == 200:
                        result["anti_bot"]["product_page_status"] = 200
                        result["anti_bot"]["product_page_accessible"] = True
                    elif checks:
                        result["anti_bot"]["product_page_status"] = checks[0]["status"]
                        result["anti_bot"]["product_page_accessible"] = False

            if best_recipe:
                result["recipe_verification"] = best_recipe
            else:
                result["recipe_verification"] = {
                    "knowledgebase_file": None,
                    "knowledgebase_found": False,
                    "knowledgebase_selectors_parsed": 0,
                    "knowledgebase_api_endpoints_parsed": 0,
                    "recipe_match": "untested",
                    "product_pages_tested": 0,
                    "checks": [],
                    "pagination_check": {"tested": False, "reason": "no knowledgebase found"},
                }

            # 9. Transport health
            result["rate_limited"] = tracker.rate_limited
            result["transport_health"] = tracker.summary(args.delay)

    except Exception as exc:
        log("error", "Script crashed", error=str(exc))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
