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
