# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
"""
Load a platform knowledgebase and verify its extraction recipe on sampled product pages.

WHEN TO CALL: After probe_discovery has found sample_product_urls and probe_platform
    has identified the platform. Requires a knowledgebase file to exist for the platform.

ARGUMENTS:
    --url                Base website URL (required)
    --platform           Platform slug, e.g. "magento" (required)
    --knowledgebase-dir  Path to platform knowledgebase directory (required)
    --product-urls       Comma-separated product URLs to test (optional)
    --timeout            HTTP timeout in seconds (default: 15.0)
    --delay              Inter-request delay in seconds (default: 0.5)
    --max-response-size  Max response bytes (default: 2_000_000)

EXIT CODES:
    0 = full result
    1 = partial result (errors[] explains gaps)
    2 = script crash (fall back to manual reasoning)

INTERPRETATION:
    recipe_match == "full"     → recipe verified on real product pages; use fast path
    recipe_match == "partial"  → some checks passed; verify failing ones manually
    recipe_match == "poor"     → does NOT mean the site is broken. The probe may have
        received category page URLs from the sitemap instead of product pages. Always
        inspect checks[].url — if URLs contain /shop/, /category/, or /collection/
        path segments, the match result is invalid. Treat as "untested" and proceed
        to manual investigation.
    recipe_match == "untested" → no product URLs supplied or available; proceed to Step 3a
    knowledgebase_found == false → no recipe to verify; proceed to deep investigation
    checks[].status non-200 → possible access restriction on product pages
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

from selectolax.parser import HTMLParser

from _probe_lib import fetch, get_body_text_length, log, make_client, TransportTracker


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

    css_section = extract_md_section(content, "CSS Selectors")
    if css_section:
        for line in css_section.split("\n"):
            if not line.strip().startswith("|") or "---" in line:
                continue
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 2 and cells[0].lower() != "element":
                selector_match = re.search(r"`([^`]+)`", cells[1])
                if selector_match:
                    result["css_selectors"].append({
                        "element": cells[0],
                        "selector": selector_match.group(1),
                        "notes": cells[2] if len(cells) > 2 else "",
                    })

    jsonld_section = extract_md_section(content, "JSON-LD Patterns")
    if jsonld_section:
        for schema_type in ["Product", "BreadcrumbList", "AggregateOffer", "Offer"]:
            if schema_type.lower() in jsonld_section.lower():
                result["json_ld_types"].append(schema_type)

    pagination_section = extract_md_section(content, "Pagination")
    if pagination_section:
        url_match = re.search(r"URL pattern:\s*`?([^`\n]+)`?", pagination_section)
        if url_match:
            result["pagination_url_pattern"] = url_match.group(1).strip()
        pp_match = re.search(r"Products per page:\s*(\d+)", pagination_section)
        if pp_match:
            result["products_per_page"] = int(pp_match.group(1))

    for section_name in ["Shopify JSON API", "API Endpoints", "JSON API"]:
        api_section = extract_md_section(content, section_name)
        if api_section:
            for match in re.finditer(r"`(/[^`]+\.json[^`]*)`", api_section):
                endpoint = re.sub(r'\{[^}]+\}', '', match.group(1))
                endpoint = endpoint.rstrip('?&')
                result["api_endpoints"].append(endpoint)
            break

    return result


def verify_recipe(client, product_urls: list[str],
                  kb: dict, *, timeout: float, delay: float,
                  max_size: int, tracker: TransportTracker) -> list[dict]:
    """Test product URLs against knowledgebase recipe. Returns per-URL check results."""
    checks = []
    for url in product_urls:
        text, status, truncated, _, _ = fetch(client, url, timeout=timeout, delay=delay,
                                               max_size=max_size, tracker=tracker)
        if not text or (status and status != 200):
            checks.append({
                "url": url,
                "status": status,
                "json_ld_found": False,
                "json_ld_type": None,
                "css_checks": [],
                "api_checks": [],
            })
            continue

        tree = HTMLParser(text)

        # JSON-LD extraction
        json_ld_product = None
        json_ld_type = None
        for script in tree.css('script[type="application/ld+json"]'):
            try:
                data = json.loads(script.text(strip=True))
                if isinstance(data, dict):
                    if data.get("@type") == "Product":
                        json_ld_product = data
                        json_ld_type = "Product"
                        break
                    for item in data.get("@graph", []):
                        if isinstance(item, dict) and item.get("@type") == "Product":
                            json_ld_product = item
                            json_ld_type = "Product"
                            break
                    if json_ld_product:
                        break
            except (json.JSONDecodeError, AttributeError):
                pass

        # CSS selector checks (cap at 10)
        css_checks = []
        for sel_info in kb["css_selectors"][:10]:
            selector = sel_info["selector"]
            el = tree.css_first(selector)
            sample_text = el.text(strip=True)[:200] if el else ""
            css_checks.append({
                "selector": selector,
                "found": bool(sample_text),
                # true → selector matched and returned non-empty text
                "sample_text": sample_text,
                # preview of extracted text (first 200 chars)
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

        checks.append({
            "url": url,
            "status": status,
            "json_ld_found": json_ld_product is not None,
            # true → JSON-LD with @type Product found on page
            "json_ld_type": json_ld_type,
            # records the actual @type value found (e.g. "Product"), null if none
            "css_checks": css_checks,
            "api_checks": api_checks,
        })

    return checks


def check_pagination(client, product_urls: list[str],
                     kb: dict, *, timeout: float, delay: float,
                     max_size: int, tracker: TransportTracker) -> dict:
    """Try to find a category page and verify pagination works."""
    pagination_pattern = kb.get("pagination_url_pattern")
    if not pagination_pattern or not product_urls:
        return {"tested": False, "pattern_confirmed": None, "next_page_found": False}

    sample_url = product_urls[0]
    parsed = urlparse(sample_url)
    path_parts = [p for p in parsed.path.split("/") if p]
    if len(path_parts) >= 2:
        category_path = "/" + "/".join(path_parts[:-1])
        category_url = f"{parsed.scheme}://{parsed.netloc}{category_path}"
    else:
        return {"tested": False, "pattern_confirmed": None, "next_page_found": False}

    text1, status1, _, _, _ = fetch(client, category_url, timeout=timeout, delay=delay,
                                     max_size=max_size, tracker=tracker)
    if not text1 or status1 != 200:
        return {"tested": False, "pattern_confirmed": None, "next_page_found": False}

    tree1 = HTMLParser(text1)
    parsed_base = urlparse(category_url)

    def collect_links(tree: HTMLParser) -> set[str]:
        links = set()
        for a in tree.css("a[href]"):
            href = a.attributes.get("href", "")
            if not href or href.startswith("#") or href.startswith("javascript:"):
                continue
            if href.startswith("/"):
                full = f"{parsed_base.scheme}://{parsed_base.netloc}{href}"
            elif href.startswith("http"):
                full = href
            else:
                continue
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
        return {
            "tested": True,
            "pattern_confirmed": None,
            "next_page_found": False,
        }

    tree2 = HTMLParser(text2)
    p2_links = collect_links(tree2)
    products_differ = bool(p2_links - p1_links)

    return {
        "tested": True,
        "pattern_confirmed": pagination_pattern if products_differ else None,
        # the pagination URL pattern that was confirmed working, null if not confirmed
        "next_page_found": products_differ,
        # true → page 2 returned different product links than page 1
    }


def compute_recipe_match(checks: list[dict], pagination: dict) -> str:
    """Compute recipe match quality from check results."""
    if not checks:
        return "untested"
    total_checks = 0
    passed_checks = 0
    for check in checks:
        if check["status"] != 200:
            continue
        total_checks += 1
        if check["json_ld_found"]:
            passed_checks += 1
        for css in check["css_checks"]:
            total_checks += 1
            if css["found"]:
                passed_checks += 1

    if total_checks == 0:
        return "untested"

    ratio = passed_checks / total_checks
    pagination_tested = pagination.get("tested", False)

    if ratio == 1.0 and pagination_tested and pagination.get("next_page_found", False):
        return "full"
    if ratio > 0.5:
        return "partial"
    return "poor"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify extraction recipe on product pages")
    parser.add_argument("--url", required=True, help="Base website URL")
    parser.add_argument("--platform", required=True, help="Platform slug (e.g. magento)")
    parser.add_argument("--knowledgebase-dir", required=True, type=Path,
                        help="Path to platform knowledgebase directory")
    parser.add_argument("--product-urls", default=None,
                        help="Comma-separated product URLs to test (optional)")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--max-response-size", type=int, default=2_000_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracker = TransportTracker()
    errors: list[dict] = []

    # Check knowledgebase
    kb_file = args.knowledgebase_dir / f"{args.platform}.md"

    result: dict = {
        "knowledgebase_file": kb_file.name if kb_file.exists() else None,
        "knowledgebase_found": kb_file.exists(),
        "knowledgebase_selectors_parsed": 0,
        "knowledgebase_api_endpoints_parsed": 0,
        "recipe_match": "untested",
        # "full"     → recipe verified on product pages; use fast path
        # "partial"  → some checks passed; verify the failing ones manually
        # "poor"     → most checks failed; VERIFY checks[].url before concluding —
        #              category page URLs produce false "poor" results
        # "untested" → no product URLs supplied or available; proceed to Step 3a
        "product_pages_tested": 0,
        "checks": [],
        "pagination_check": {"tested": False, "pattern_confirmed": None, "next_page_found": False},
        "errors": errors,
    }

    # If no product URLs, return untested immediately
    if not args.product_urls:
        errors.append({"section": "recipe", "error": "No product URLs supplied (--product-urls omitted)"})
        print(json.dumps(result, indent=2))
        sys.exit(1)

    if not kb_file.exists():
        errors.append({"section": "knowledgebase", "error": f"Knowledgebase not found: {kb_file}"})
        print(json.dumps(result, indent=2))
        sys.exit(1)

    try:
        kb = parse_knowledgebase(kb_file)
        result["knowledgebase_selectors_parsed"] = len(kb["css_selectors"])
        result["knowledgebase_api_endpoints_parsed"] = len(kb["api_endpoints"])

        product_urls = [u.strip() for u in args.product_urls.split(",") if u.strip()]

        with make_client() as client:
            checks = verify_recipe(client, product_urls, kb, timeout=args.timeout,
                                   delay=args.delay, max_size=args.max_response_size,
                                   tracker=tracker)
            pagination = check_pagination(client, product_urls, kb, timeout=args.timeout,
                                          delay=args.delay, max_size=args.max_response_size,
                                          tracker=tracker)

        recipe_match = compute_recipe_match(checks, pagination)
        result["recipe_match"] = recipe_match
        result["product_pages_tested"] = len(checks)
        result["checks"] = checks
        result["pagination_check"] = pagination

    except Exception as exc:
        log("error", "Script crashed", error=str(exc))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
