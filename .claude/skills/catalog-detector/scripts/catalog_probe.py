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
    log("info", "catalog_probe.py skeleton — full implementation coming in Task 7", url=args.url)
    print(json.dumps({"url": args.url, "status": "skeleton"}))
    sys.exit(0)


if __name__ == "__main__":
    main()
