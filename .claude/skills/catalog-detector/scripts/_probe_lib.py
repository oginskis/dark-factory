"""Shared HTTP, logging, and utility infrastructure for catalog-detector probe scripts."""
from __future__ import annotations

import json
import re
import sys
import time
from datetime import datetime, timezone

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
    """Tracks HTTP request outcomes across a probe run."""

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

    def summary(self) -> str:
        """Return transport health as a plain string: 'healthy', 'degraded', or 'blocked'."""
        if self.status_403 + self.status_429 + self.challenge_pages > self.total / 2:
            return "blocked"
        total_non_ok = self.total - self.status_200
        if total_non_ok > 0 or self.timeouts > 0:
            return "degraded"
        return "healthy"


def fetch(client: httpx.Client, url: str, *, timeout: float, delay: float,
          max_size: int, tracker: TransportTracker) -> tuple[str | None, int | None, bool, dict, str | None]:
    """Fetch URL. Returns (text, status, truncated, headers, final_url). Handles 429 retry."""
    time.sleep(delay)
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
    if resp.encoding is None:
        text = resp.content[:max_size].decode("utf-8", errors="replace")
    else:
        text = resp.text
    truncated = len(resp.content) > max_size
    if truncated:
        text = text[:max_size]
        log("warning", "Response truncated", url=url,
            original_size=len(resp.content), truncated_to=max_size)

    # Only flag as challenge page if the response is small — a real challenge/interstitial
    # page (Cloudflare, CAPTCHA gate) is typically < 10KB. A 200 response with substantial
    # content that happens to contain "captcha" (e.g., a reCAPTCHA widget on a contact form)
    # is NOT a challenge page.
    is_challenge = (
        status == 200
        and len(text) < 10_000
        and detect_challenge_page(text)
    )
    tracker.record(status, is_challenge)
    resp_headers = dict(resp.headers)
    final_url = str(resp.url)
    return text, status, truncated, resp_headers, final_url


def get_body_text_length(html: str) -> int:
    tree = HTMLParser(html)
    for tag in tree.css("script, style"):
        tag.decompose()
    body = tree.css_first("body")
    return len(body.text(strip=True)) if body else 0


def make_client() -> httpx.Client:
    """Return a configured httpx.Client with browser-like headers."""
    return httpx.Client(
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        },
        follow_redirects=True,
        max_redirects=10,
    )
