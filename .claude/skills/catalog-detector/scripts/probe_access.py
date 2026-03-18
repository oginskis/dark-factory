# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx",
#     "selectolax",
# ]
# ///
"""
Fetch a website's homepage and assess transport health and anti-bot defenses.

WHEN TO CALL: First script in the probe pipeline. No preconditions.

ARGUMENTS:
    --url       Target website URL (required)
    --timeout   HTTP timeout in seconds (default: 15.0)
    --delay     Inter-request delay in seconds (default: 0)
    --max-response-size  Max response bytes (default: 2_000_000)

EXIT CODES:
    0 = full result
    1 = partial result (errors[] explains gaps)
    2 = script crash (fall back to manual reasoning)

INTERPRETATION:
    transport_health == "blocked"  → stop immediately; write anti_bot_severe assessment
    transport_health == "degraded" → proceed but note in Platform-Specific Notes
    transport_health == "healthy"  → proceed normally
    anti_bot.suspected_empty_shell == true → site may be JS-rendered;
        confirm with probe_platform text_to_html_ratio
"""
from __future__ import annotations

import argparse
import json
import sys
from urllib.parse import urlparse

from selectolax.parser import HTMLParser

from _probe_lib import (
    detect_challenge_page,
    fetch,
    find_blocked_keywords,
    get_body_text_length,
    log,
    make_client,
    TransportTracker,
)


def analyze_anti_bot(html: str, content_length: int, body_text_length: int,
                     tree: HTMLParser) -> dict:
    """Analyze homepage HTML for anti-bot defenses."""
    is_challenge = detect_challenge_page(html)
    has_nav = tree.css_first("nav") is not None
    has_article = tree.css_first("article") is not None
    has_main = tree.css_first("main") is not None
    substantial_structure = has_nav or has_article or has_main
    suspected_shell = content_length > 1000 and body_text_length < 500 and not substantial_structure

    return {
        "challenge_page_detected": is_challenge,
        "cloudflare_ray": None,  # filled from response headers by caller
        "cloudflare_challenge": "cf-turnstile" in html.lower() or "_cf_chl_opt" in html.lower(),
        "captcha_detected": "g-recaptcha" in html.lower() or "h-captcha" in html.lower(),
        "datadome_detected": "datadome" in html.lower(),
        "perimeterx_detected": "perimeterx" in html.lower() or "_pxhd" in html.lower(),
        "blocked_keywords_found": find_blocked_keywords(html),
        "homepage_content_length": content_length,
        "suspected_empty_shell": suspected_shell,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Probe website transport health and anti-bot")
    parser.add_argument("--url", required=True, help="Target website URL")
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--delay", type=float, default=0)
    parser.add_argument("--max-response-size", type=int, default=2_000_000)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    tracker = TransportTracker()
    errors: list[dict] = []

    result: dict = {
        "url": args.url,
        "final_url": args.url,
        "redirected": False,
        "cross_domain_redirect": False,
        "homepage_status": None,
        "transport_health": "blocked",
        # "healthy"  → proceed normally
        # "degraded" → proceed but note in Platform-Specific Notes
        # "blocked"  → stop immediately; write anti_bot_severe assessment
        "anti_bot": {
            "challenge_page_detected": False,
            "cloudflare_ray": None,
            "cloudflare_challenge": False,
            "captcha_detected": False,
            "datadome_detected": False,
            "perimeterx_detected": False,
            "blocked_keywords_found": [],
            "homepage_content_length": 0,
            "suspected_empty_shell": False,
            # suspected_empty_shell == true → site may be JS-rendered;
            # confirm with probe_platform text_to_html_ratio
        },
        "errors": errors,
    }

    try:
        with make_client() as client:
            hp_text, hp_status, _, hp_headers, hp_final_url = fetch(
                client, args.url, timeout=args.timeout,
                delay=0, max_size=args.max_response_size, tracker=tracker)
            result["homepage_status"] = hp_status

            if not hp_text:
                errors.append({"section": "homepage", "error": "Homepage unreachable"})
                result["transport_health"] = tracker.summary()
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

            # Anti-bot analysis
            body_text_len = get_body_text_length(hp_text)
            anti_bot = analyze_anti_bot(hp_text, len(hp_text), body_text_len, HTMLParser(hp_text))
            anti_bot["cloudflare_ray"] = hp_headers.get("cf-ray")
            result["anti_bot"] = anti_bot

            # Transport health
            result["transport_health"] = tracker.summary()

    except Exception as exc:
        log("error", "Script crashed", error=str(exc))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    sys.exit(0 if not errors else 1)


if __name__ == "__main__":
    main()
