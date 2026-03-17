# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
"""
Detect CMS/platform from HTML signals and response headers.

WHEN TO CALL: After probe_access confirms the site is reachable
    (transport_health != "blocked"). Requires no other preconditions.

ARGUMENTS:
    --url       Target website URL (required)
    --timeout   HTTP timeout in seconds (default: 15.0)
    --delay     Inter-request delay in seconds (default: 0.5)
    --max-response-size  Max response bytes (default: 2_000_000)

EXIT CODES:
    0 = full result
    1 = partial result (errors[] explains gaps)
    2 = script crash (fall back to manual reasoning)

INTERPRETATION:
    platform_guess == "unknown" → deep investigation path; no knowledgebase to load
    platform_confidence == "definitive" → signal from meta tag or powered-by header; trust it
    platform_confidence == "weak" or "none" → use LLM judgment; probe may be wrong
    platform_conflict == true → 2+ platforms detected; orchestrator will run probe_recipe
        for each candidate and pick best result by recipe_match rank
    text_to_html_ratio < 0.05 → likely SPA; check for js_only stop condition
    framework_detected != null → JS framework present; verify if structured data
        fallback is available
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from urllib.parse import urlparse

from selectolax.parser import HTMLParser

from _probe_lib import fetch, log, make_client, TransportTracker


PLATFORM_SIGNALS = {
    "meta_generator": None,
    "powered_by_header": None,
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

SIGNAL_TO_PLATFORM = {
    "shopify_cdn": "shopify",
    "wp_content_path": "woocommerce",
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

    meta = tree.css_first('meta[name="generator"]')
    if meta:
        signals["meta_generator"] = meta.attributes.get("content")

    signals["powered_by_header"] = headers.get("x-powered-by")

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
    platform_hits: dict[str, int] = {}
    for key, platform in SIGNAL_TO_PLATFORM.items():
        if signals.get(key):
            platform_hits[platform] = platform_hits.get(platform, 0) + 1

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


def analyze_js_rendering(html: str, content_length: int) -> dict:
    tree = HTMLParser(html)
    for tag in tree.css("script, style"):
        tag.decompose()
    body = tree.css_first("body")
    body_text = body.text(strip=True) if body else ""
    body_text_length = len(body_text)

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
        # body_text_length — raw character count of visible text after removing scripts/styles
        "noscript_tag_found": "<noscript" in html.lower(),
        "framework_detected": framework,
        # framework_detected — null means no JS framework found; non-null means SPA likely
        "empty_product_container": empty_container,
        "text_to_html_ratio": round(ratio, 3),
        # text_to_html_ratio < 0.05 → likely SPA; check for js_only stop condition
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


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Detect CMS/platform from HTML signals")
    parser.add_argument("--url", required=True, help="Target website URL")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--delay", type=float, default=0.5)
    parser.add_argument("--max-response-size", type=int, default=2_000_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracker = TransportTracker()
    errors: list[dict] = []

    result: dict = {
        "platform_guess": "unknown",
        # "unknown"   → deep investigation path; no knowledgebase to load
        # known name  → load platform knowledgebase for recipe verification
        "platform_confidence": "none",
        # "definitive" → from meta tag or powered-by header; trust it
        # "likely"     → 2+ signals for same platform
        # "weak"       → single signal; use LLM judgment
        # "none"       → no signals found
        "platform_signal_count": 0,
        "platform_conflict": False,
        # true → 2+ different platforms detected; run probe_recipe for each
        "platform_version": None,
        "js_rendering_signals": {},
        "geo_hints": {},
        "errors": errors,
    }

    try:
        with make_client() as client:
            hp_text, hp_status, _, hp_headers, hp_final_url = fetch(
                client, args.url, timeout=args.timeout,
                delay=0, max_size=args.max_response_size, tracker=tracker)

            if not hp_text:
                errors.append({"section": "homepage", "error": "Homepage unreachable"})
                print(json.dumps(result, indent=2))
                sys.exit(1)

            signals = detect_platform_signals(hp_text, hp_headers)
            guess, confidence, sig_count, conflict, version = guess_platform(signals)
            result["platform_guess"] = guess
            result["platform_confidence"] = confidence
            result["platform_signal_count"] = sig_count
            result["platform_conflict"] = conflict
            result["platform_version"] = version

            result["js_rendering_signals"] = analyze_js_rendering(hp_text, len(hp_text))
            result["geo_hints"] = extract_geo_hints(hp_text, hp_headers, hp_final_url or args.url)

    except Exception as exc:
        log("error", "Script crashed", error=str(exc))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
