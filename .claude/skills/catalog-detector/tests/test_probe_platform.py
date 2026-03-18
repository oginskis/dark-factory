# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest", "selectolax"]
# ///
"""Tests for probe_platform.py — platform detection, JS rendering, geo hints."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from probe_platform import (
    analyze_js_rendering,
    detect_platform_signals,
    extract_geo_hints,
    guess_platform,
)


# ---------------------------------------------------------------------------
# detect_platform_signals
# ---------------------------------------------------------------------------


class TestDetectPlatformSignals:
    def test_shopify_signals(self, shopify_html):
        signals = detect_platform_signals(shopify_html, {})
        assert signals["shopify_cdn"] is True
        assert signals["meta_generator"] == "Shopify"

    def test_woocommerce_signals(self, woocommerce_html):
        signals = detect_platform_signals(woocommerce_html, {})
        assert signals["wp_content_path"] is True
        assert signals["woocommerce_body_class"] is True

    def test_powered_by_header(self, minimal_html):
        signals = detect_platform_signals(minimal_html, {"x-powered-by": "Express"})
        assert signals["powered_by_header"] == "Express"

    def test_no_powered_by_header(self, minimal_html):
        signals = detect_platform_signals(minimal_html, {})
        assert signals["powered_by_header"] is None

    def test_magento_static_version(self):
        html = '<html><body><link href="/static/version1234567890/styles.css"></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["magento_static_version"] is True

    def test_prestashop_signals(self):
        html = '<html><body><link href="/modules/ps_checkout/views/style.css">PrestaShop</body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["prestashop_modules_path"] is True

    def test_prestashop_modules_without_prestashop_keyword(self):
        """/modules/ alone is not enough; prestashop keyword must also be present."""
        html = '<html><body><link href="/modules/some_module/style.css"></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["prestashop_modules_path"] is False

    def test_bigcommerce_cdn(self):
        html = '<html><body><script src="https://cdn.bigcommerce.com/assets/app.js"></script></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["bigcommerce_cdn"] is True

    def test_squarespace_static(self):
        html = '<html><body><link href="https://static1.squarespace.com/static/css/theme.css"></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["squarespace_static"] is True

    def test_squarespace_cdn(self):
        html = '<html><body><link href="https://assets.squarespace-cdn.com/style.css"></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["squarespace_static"] is True

    def test_wix_static(self):
        html = '<html><body><img src="https://static.wixstatic.com/media/photo.jpg"></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["wix_static"] is True

    def test_drupal_settings(self):
        html = '<html><body><script>drupalSettings = {};</script></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["drupal_settings"] is True

    def test_drupal_js(self):
        html = '<html><body><script src="/core/drupal.js"></script></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["drupal_settings"] is True

    def test_no_signals(self, minimal_html):
        signals = detect_platform_signals(minimal_html, {})
        assert signals["shopify_cdn"] is False
        assert signals["wp_content_path"] is False
        assert signals["meta_generator"] is None

    def test_meta_generator_extraction(self):
        html = '<html><head><meta name="generator" content="WordPress 6.4"></head><body></body></html>'
        signals = detect_platform_signals(html, {})
        assert signals["meta_generator"] == "WordPress 6.4"


# ---------------------------------------------------------------------------
# guess_platform
# ---------------------------------------------------------------------------


class TestGuessPlatform:
    def test_definitive_from_meta_generator(self):
        signals = {"meta_generator": "Shopify", "shopify_cdn": True}
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "shopify"
        assert confidence == "definitive"
        assert version == "Shopify"

    def test_meta_generator_prestashop(self):
        signals = {"meta_generator": "PrestaShop 1.7", "prestashop_modules_path": True}
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "prestashop"
        assert confidence == "definitive"
        assert version == "PrestaShop 1.7"

    def test_meta_generator_opencart(self):
        signals = {"meta_generator": "OpenCart 3.0"}
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "opencart"
        assert confidence == "definitive"

    def test_likely_from_multiple_signals(self):
        signals = {
            "meta_generator": None,
            "wp_content_path": True,
            "woocommerce_body_class": True,
        }
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "woocommerce"
        assert confidence == "likely"
        assert count == 2

    def test_weak_from_single_signal(self):
        signals = {
            "meta_generator": None,
            "shopify_cdn": True,
        }
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "shopify"
        assert confidence == "weak"
        assert count == 1

    def test_unknown_no_signals(self):
        signals = {"meta_generator": None}
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "unknown"
        assert confidence == "none"
        assert count == 0
        assert conflict is False

    def test_conflict_detected(self):
        signals = {
            "meta_generator": None,
            "shopify_cdn": True,
            "wp_content_path": True,
        }
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert conflict is True
        assert count == 2

    def test_meta_generator_overrides_conflicting_signals(self):
        """Meta generator is definitive even with conflicting CDN signals."""
        signals = {
            "meta_generator": "Shopify",
            "wp_content_path": True,
            "woocommerce_body_class": True,
        }
        guess, confidence, count, conflict, version = guess_platform(signals)
        assert guess == "shopify"
        assert confidence == "definitive"


# ---------------------------------------------------------------------------
# analyze_js_rendering
# ---------------------------------------------------------------------------


class TestAnalyzeJsRendering:
    def test_normal_page(self, minimal_html):
        result = analyze_js_rendering(minimal_html, len(minimal_html))
        assert result["framework_detected"] is None
        assert result["empty_product_container"] is False
        assert result["text_to_html_ratio"] > 0
        assert result["body_text_length"] > 0

    def test_nextjs_detected(self, spa_html):
        result = analyze_js_rendering(spa_html, len(spa_html))
        assert result["framework_detected"] == "nextjs"
        assert result["noscript_tag_found"] is True

    def test_nuxt_detected(self):
        html = '<html><body><div id="__nuxt"></div><script>window.__NUXT__={}</script></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["framework_detected"] == "nuxt"

    def test_angular_detected(self):
        html = '<html><body ng-app="myApp"><div ng-version="15"></div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["framework_detected"] == "angular"

    def test_react_detected(self):
        html = '<html><body><div data-reactroot>Content</div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["framework_detected"] == "react"

    def test_vue_detected(self):
        html = '<html><body><div data-v-1a2b3c>Content</div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["framework_detected"] == "vue"

    def test_empty_product_container(self):
        html = '<html><body><div class="products"></div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["empty_product_container"] is True

    def test_non_empty_product_container(self):
        html = '<html><body><div class="products"><div>Product A</div></div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["empty_product_container"] is False

    def test_text_to_html_ratio_zero_content(self):
        result = analyze_js_rendering("", 0)
        assert result["text_to_html_ratio"] == 0

    def test_noscript_found(self):
        html = '<html><body><noscript>Enable JS</noscript><div>Content</div></body></html>'
        result = analyze_js_rendering(html, len(html))
        assert result["noscript_tag_found"] is True

    def test_noscript_not_found(self, minimal_html):
        result = analyze_js_rendering(minimal_html, len(minimal_html))
        assert result["noscript_tag_found"] is False


# ---------------------------------------------------------------------------
# extract_geo_hints
# ---------------------------------------------------------------------------


class TestExtractGeoHints:
    def test_html_lang(self, minimal_html):
        result = extract_geo_hints(minimal_html, {}, "https://example.com/")
        assert result["html_lang"] == "en"

    def test_vary_accept_language(self):
        html = "<html><body></body></html>"
        headers = {"vary": "Accept-Language, Cookie"}
        result = extract_geo_hints(html, headers, "https://example.com/")
        assert result["vary_accept_language"] is True

    def test_no_vary_header(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/")
        assert result["vary_accept_language"] is False

    def test_geo_redirect_en_gb(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/en-gb/products")
        assert result["geo_redirect_detected"] is True
        assert result["country_path_segment"] == "en-gb"

    def test_geo_redirect_de(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/de/shop")
        assert result["geo_redirect_detected"] is True
        assert result["country_path_segment"] == "de"

    def test_geo_redirect_lv(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/lv/products")
        assert result["geo_redirect_detected"] is True
        assert result["country_path_segment"] == "lv"

    def test_no_geo_redirect(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/products/widget")
        assert result["geo_redirect_detected"] is False
        assert result["country_path_segment"] is None

    def test_no_html_lang(self):
        html = "<html><body></body></html>"
        result = extract_geo_hints(html, {}, "https://example.com/")
        assert result["html_lang"] is None


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
