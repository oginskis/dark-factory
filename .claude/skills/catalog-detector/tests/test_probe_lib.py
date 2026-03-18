# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest", "httpx"]
# ///
"""Tests for _probe_lib.py — shared HTTP, logging, and utility infrastructure."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from _probe_lib import (
    detect_challenge_page,
    fetch,
    find_blocked_keywords,
    get_body_text_length,
    log,
    TransportTracker,
)


# ---------------------------------------------------------------------------
# detect_challenge_page
# ---------------------------------------------------------------------------


class TestDetectChallengePage:
    def test_cloudflare_turnstile(self):
        html = '<div class="cf-turnstile">Challenge</div>'
        assert detect_challenge_page(html) is True

    def test_cloudflare_browser_verification(self):
        html = '<div class="cf-browser-verification">Verifying...</div>'
        assert detect_challenge_page(html) is True

    def test_access_denied(self):
        html = "<h1>Access Denied</h1><p>You have been blocked</p>"
        assert detect_challenge_page(html) is True

    def test_captcha(self):
        html = '<div class="g-recaptcha" data-sitekey="abc123"></div>'
        assert detect_challenge_page(html) is True

    def test_hcaptcha(self):
        html = '<div class="h-captcha"></div>'
        assert detect_challenge_page(html) is True

    def test_just_a_moment(self):
        html = "<title>Just a moment...</title>"
        assert detect_challenge_page(html) is True

    def test_cf_chl_opt(self):
        html = "<script>var _cf_chl_opt = {};</script>"
        assert detect_challenge_page(html) is True

    def test_normal_page_no_challenge(self, minimal_html):
        assert detect_challenge_page(minimal_html) is False

    def test_case_insensitive(self):
        html = "<p>YOU HAVE BEEN BLOCKED</p>"
        assert detect_challenge_page(html) is True

    def test_empty_html(self):
        assert detect_challenge_page("") is False


# ---------------------------------------------------------------------------
# find_blocked_keywords
# ---------------------------------------------------------------------------


class TestFindBlockedKeywords:
    def test_multiple_keywords(self):
        html = '<div class="cf-turnstile">Just a moment</div>'
        keywords = find_blocked_keywords(html)
        assert "cf-turnstile" in keywords
        assert "just a moment" in keywords

    def test_no_keywords(self, minimal_html):
        assert find_blocked_keywords(minimal_html) == []

    def test_deduplicates(self):
        html = "captcha captcha captcha"
        keywords = find_blocked_keywords(html)
        assert keywords == ["captcha"]

    def test_challenge_platform_and_challenges_cloudflare(self):
        html = '<div id="challenge-platform">challenges.cloudflare.com</div>'
        keywords = find_blocked_keywords(html)
        assert "challenge-platform" in keywords
        assert "challenges.cloudflare.com" in keywords


# ---------------------------------------------------------------------------
# TransportTracker
# ---------------------------------------------------------------------------


class TestTransportTracker:
    def test_initial_state(self):
        t = TransportTracker()
        assert t.total == 0
        assert t.status_200 == 0
        assert t.rate_limited is False

    def test_record_200(self):
        t = TransportTracker()
        t.record(200)
        assert t.total == 1
        assert t.status_200 == 1

    def test_record_429_sets_rate_limited(self):
        t = TransportTracker()
        t.record(429)
        assert t.status_429 == 1
        assert t.rate_limited is True

    def test_record_403(self):
        t = TransportTracker()
        t.record(403)
        assert t.status_403 == 1

    def test_record_none_counts_timeout(self):
        t = TransportTracker()
        t.record(None)
        assert t.timeouts == 1

    def test_record_other_status(self):
        t = TransportTracker()
        t.record(500)
        assert t.status_other == 1

    def test_record_challenge_page(self):
        t = TransportTracker()
        t.record(200, is_challenge=True)
        assert t.challenge_pages == 1

    def test_summary_healthy(self):
        t = TransportTracker()
        t.record(200)
        t.record(200)
        t.record(200)
        assert t.summary() == "healthy"

    def test_summary_degraded_with_timeout(self):
        t = TransportTracker()
        t.record(200)
        t.record(None)
        assert t.summary() == "degraded"

    def test_summary_degraded_with_non_200(self):
        t = TransportTracker()
        t.record(200)
        t.record(200)
        t.record(301)
        assert t.summary() == "degraded"

    def test_summary_blocked(self):
        t = TransportTracker()
        t.record(403)
        t.record(403)
        t.record(200)
        # 2 out of 3 are 403, which is > total/2
        assert t.summary() == "blocked"

    def test_summary_blocked_by_challenge_pages(self):
        t = TransportTracker()
        t.record(200, is_challenge=True)
        t.record(200, is_challenge=True)
        t.record(200)
        # 2 challenge pages > total/2
        assert t.summary() == "blocked"

    def test_summary_blocked_mixed_403_429(self):
        t = TransportTracker()
        t.record(403)
        t.record(429)
        t.record(200)
        # 403+429 = 2 > 3/2
        assert t.summary() == "blocked"


# ---------------------------------------------------------------------------
# get_body_text_length
# ---------------------------------------------------------------------------


class TestGetBodyTextLength:
    def test_simple_body(self):
        html = "<html><body><p>Hello World</p></body></html>"
        # strip=True strips leading/trailing whitespace but preserves internal spaces
        assert get_body_text_length(html) == len("Hello World")

    def test_strips_scripts_and_styles(self):
        html = """
        <html><body>
            <p>Visible</p>
            <script>var x = 1;</script>
            <style>.foo { color: red; }</style>
        </body></html>
        """
        length = get_body_text_length(html)
        assert length == len("Visible")

    def test_no_body_returns_zero(self):
        html = "<html><head><title>Test</title></head></html>"
        assert get_body_text_length(html) == 0

    def test_empty_body(self):
        html = "<html><body></body></html>"
        assert get_body_text_length(html) == 0

    def test_complex_content(self, minimal_html):
        length = get_body_text_length(minimal_html)
        assert length > 0


# ---------------------------------------------------------------------------
# fetch
# ---------------------------------------------------------------------------


class TestFetch:
    def _make_mock_response(self, status_code=200, text="<html>OK</html>",
                             content=None, headers=None, url="https://example.com"):
        resp = MagicMock()
        resp.status_code = status_code
        resp.text = text
        resp.content = (content or text.encode("utf-8"))
        resp.encoding = "utf-8"
        resp.headers = headers or {}
        resp.url = url
        return resp

    def test_successful_fetch(self):
        import httpx
        client = MagicMock()
        resp = self._make_mock_response()
        client.get.return_value = resp
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert text == "<html>OK</html>"
        assert status == 200
        assert truncated is False
        assert final_url == "https://example.com"
        assert tracker.status_200 == 1

    def test_timeout_returns_none(self):
        import httpx
        client = MagicMock()
        client.get.side_effect = httpx.TimeoutException("timeout")
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert text is None
        assert status is None
        assert tracker.timeouts == 1

    def test_request_error_returns_none(self):
        import httpx
        client = MagicMock()
        client.get.side_effect = httpx.RequestError("connection failed")
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert text is None
        assert status is None
        assert tracker.timeouts == 1

    @patch("_probe_lib.time.sleep")
    def test_429_retries_once(self, mock_sleep):
        import httpx
        client = MagicMock()
        resp_429 = self._make_mock_response(status_code=429, headers={"Retry-After": "2"})
        resp_200 = self._make_mock_response(status_code=200)
        client.get.side_effect = [resp_429, resp_200]
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert status == 200
        assert text == "<html>OK</html>"
        mock_sleep.assert_called_once_with(2)

    @patch("_probe_lib.time.sleep")
    def test_429_retry_still_429(self, mock_sleep):
        import httpx
        client = MagicMock()
        resp_429 = self._make_mock_response(status_code=429, headers={"Retry-After": "3"})
        client.get.return_value = resp_429
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert status == 429
        assert text is None
        assert tracker.status_429 == 1

    def test_truncation(self):
        big_content = b"x" * 1000
        client = MagicMock()
        resp = self._make_mock_response(text="x" * 1000, content=big_content)
        client.get.return_value = resp
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=500, tracker=tracker)

        assert truncated is True
        assert len(text) == 500

    def test_challenge_page_detected_small_response(self, challenge_page_html):
        client = MagicMock()
        resp = self._make_mock_response(text=challenge_page_html,
                                         content=challenge_page_html.encode())
        client.get.return_value = resp
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert tracker.challenge_pages == 1

    def test_challenge_keywords_in_large_page_not_flagged(self):
        """A large page with a captcha widget is NOT a challenge page."""
        html = "<html><body>" + ("x" * 15_000) + '<div class="g-recaptcha"></div></body></html>'
        client = MagicMock()
        resp = self._make_mock_response(text=html, content=html.encode())
        client.get.return_value = resp
        tracker = TransportTracker()

        fetch(client, "https://example.com", timeout=10, delay=0,
              max_size=2_000_000, tracker=tracker)

        assert tracker.challenge_pages == 0

    @patch("_probe_lib.time.sleep")
    def test_delay_is_respected(self, mock_sleep):
        client = MagicMock()
        resp = self._make_mock_response()
        client.get.return_value = resp
        tracker = TransportTracker()

        fetch(client, "https://example.com", timeout=10, delay=1.5,
              max_size=2_000_000, tracker=tracker)

        mock_sleep.assert_called_once_with(1.5)

    def test_no_encoding_uses_content_decode(self):
        """When resp.encoding is None, fallback to content decode."""
        client = MagicMock()
        resp = self._make_mock_response()
        resp.encoding = None
        resp.content = b"<html>decoded</html>"
        client.get.return_value = resp
        tracker = TransportTracker()

        text, status, truncated, headers, final_url = fetch(
            client, "https://example.com", timeout=10, delay=0,
            max_size=2_000_000, tracker=tracker)

        assert text == "<html>decoded</html>"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
