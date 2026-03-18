# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest", "selectolax"]
# ///
"""Tests for probe_access.py — anti-bot analysis."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest
from selectolax.parser import HTMLParser

from probe_access import analyze_anti_bot


# ---------------------------------------------------------------------------
# analyze_anti_bot
# ---------------------------------------------------------------------------


class TestAnalyzeAntiBot:
    def test_clean_page_no_detections(self, minimal_html):
        tree = HTMLParser(minimal_html)
        result = analyze_anti_bot(minimal_html, len(minimal_html), 100, tree)

        assert result["challenge_page_detected"] is False
        assert result["cloudflare_challenge"] is False
        assert result["captcha_detected"] is False
        assert result["datadome_detected"] is False
        assert result["perimeterx_detected"] is False
        assert result["blocked_keywords_found"] == []
        assert result["suspected_empty_shell"] is False

    def test_challenge_page_detected(self, challenge_page_html):
        tree = HTMLParser(challenge_page_html)
        result = analyze_anti_bot(challenge_page_html, len(challenge_page_html), 10, tree)

        assert result["challenge_page_detected"] is True
        assert result["cloudflare_challenge"] is True
        assert len(result["blocked_keywords_found"]) > 0

    def test_cloudflare_ray_is_none_by_default(self, minimal_html):
        """cloudflare_ray is always None from analyze_anti_bot; caller fills it."""
        tree = HTMLParser(minimal_html)
        result = analyze_anti_bot(minimal_html, len(minimal_html), 100, tree)
        assert result["cloudflare_ray"] is None

    def test_captcha_detected(self):
        html = '<html><body><div class="g-recaptcha" data-sitekey="key123"></div></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 10, tree)
        assert result["captcha_detected"] is True

    def test_hcaptcha_detected(self):
        html = '<html><body><div class="h-captcha"></div></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 10, tree)
        assert result["captcha_detected"] is True

    def test_datadome_detected(self):
        html = '<html><body><script src="https://js.datadome.co/tags.js"></script></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 10, tree)
        assert result["datadome_detected"] is True

    def test_perimeterx_detected_pxhd(self):
        html = '<html><body><script>window._pxhd = "abc";</script></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 10, tree)
        assert result["perimeterx_detected"] is True

    def test_perimeterx_detected_name(self):
        html = '<html><body><script src="//client.perimeterx.net/main.js"></script></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 10, tree)
        assert result["perimeterx_detected"] is True

    def test_suspected_empty_shell_true(self):
        """Large HTML with almost no visible text and no structural tags -> suspected shell."""
        html = '<html><head></head><body><div id="app"></div>' + ('<script>x=1;</script>' * 100) + '</body></html>'
        tree = HTMLParser(html)
        # content_length > 1000, body_text_length < 500, no nav/article/main
        result = analyze_anti_bot(html, len(html), 0, tree)
        assert result["suspected_empty_shell"] is True

    def test_suspected_empty_shell_false_with_nav(self):
        """Large HTML with nav tag should NOT be suspected as empty shell."""
        html = '<html><body><nav>Menu</nav><div id="app"></div>' + ('<script>x=1;</script>' * 100) + '</body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 0, tree)
        assert result["suspected_empty_shell"] is False

    def test_suspected_empty_shell_false_small_content(self):
        """Small HTML is not suspected as shell (content_length <= 1000)."""
        html = '<html><body><div id="app"></div></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 0, tree)
        assert result["suspected_empty_shell"] is False

    def test_suspected_empty_shell_false_with_body_text(self):
        """Large HTML with sufficient body text -> not shell."""
        html = '<html><body><div>' + ('Real content text. ' * 100) + '</div></body></html>'
        tree = HTMLParser(html)
        result = analyze_anti_bot(html, len(html), 600, tree)
        assert result["suspected_empty_shell"] is False

    def test_homepage_content_length_populated(self, minimal_html):
        tree = HTMLParser(minimal_html)
        result = analyze_anti_bot(minimal_html, 42, 100, tree)
        assert result["homepage_content_length"] == 42


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
