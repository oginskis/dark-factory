# Catalog Detector Scripts Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add two Python scripts to catalog-detector that reduce LLM token cost by ~25-30% per run — `catalog_probe.py` (platform detection + recipe verification + anti-bot) and `validate_assessment.py` (report validation gates).

**Architecture:** Both scripts follow the repo convention: PEP 723 inline metadata, JSON stdout / JSON-lines stderr, exit codes 0/1/2. The probe script uses httpx + selectolax for HTTP + HTML parsing. The validator uses only stdlib for markdown regex matching. Both are standalone — no shared library between them. All paths are passed via CLI args (no `find_repo_root()` needed).

**Tech Stack:** Python 3.10+, httpx, selectolax, stdlib (json, re, argparse, xml.etree.ElementTree, pathlib, time, datetime, sys)

**Spec:** `docs/superpowers/specs/2026-03-17-catalog-detector-scripts-design.md`

---

## Chunk 1: Knowledgebase Normalization + validate_assessment.py

### Task 1: Normalize WooCommerce knowledgebase CSS Selectors

**Files:**
- Modify: `docs/platform-knowledgebase/woocommerce.md:12-22`

- [ ] **Step 1: Convert CSS Selectors from bullets to table**

Replace the `## CSS Selectors` section (lines 12-22) with a markdown table. Preserve all selectors and notes. The breadcrumb entry should list the primary selector with theme variants in Notes:

```markdown
## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on category pages | `ul.products li.product a` | Filter for `href` containing `/product/`. Multilingual: `/toode/` in Estonian |
| Pagination next page | `a.next.page-numbers` | Absent when on last page (no disabled state) |
| Breadcrumb | `nav.woocommerce-breadcrumb` | Varies: Kadence `.kadence-breadcrumbs`, Yoast `.yoast-breadcrumb`, generic `nav[aria-label='breadcrumb']`. Try all, fallback in order |
| Product short description | `.woocommerce-product-details__short-description` | — |
| Product full description | `.woocommerce-Tabs-panel--description` | — |
```

- [ ] **Step 2: Verify table parses correctly**

Run a quick check: the table has 5 data rows, pipe-delimited, with `Element | Selector | Notes` header. Confirm with:
```bash
grep -c "^|" docs/platform-knowledgebase/woocommerce.md
```
Expected: 7 lines (header + separator + 5 data rows).

- [ ] **Step 3: Commit**

```bash
git add docs/platform-knowledgebase/woocommerce.md
git commit -m "Normalize woocommerce.md CSS Selectors to table format

Prerequisite for catalog_probe.py knowledgebase parser which expects
pipe-delimited markdown tables."
```

### Task 2: Normalize Shopify knowledgebase CSS Selectors + Pagination

**Files:**
- Modify: `docs/platform-knowledgebase/shopify.md:17-24`

- [ ] **Step 1: Convert CSS Selectors from bullets to table**

Replace lines 17-19 with:

```markdown
## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on collection pages | `.product-card a` | Varies by theme: also try `.product-item a`, `.grid-product a` |
| Pagination next | `.pagination a[rel="next"]` | Also try `a.next` |
| Breadcrumb | `.breadcrumb` | Varies: also `.breadcrumbs`, `nav[aria-label="Breadcrumb"]` |
```

- [ ] **Step 2: Normalize Pagination section**

Replace lines 22-24 with bullet items matching the format other files use:

```markdown
## Pagination
- URL pattern: `/collections/{name}?page={N}` (HTML) or `/products.json?limit=250&page={N}` (JSON API)
- Products per page: 16-24 (HTML collections), 250 (JSON API)
- Next page detection: `.pagination a[rel="next"]` (HTML) or empty `products` array (JSON API)
- Product sitemap: `sitemap_products_1.xml` — lists all product URLs
```

- [ ] **Step 3: Commit**

```bash
git add docs/platform-knowledgebase/shopify.md
git commit -m "Normalize shopify.md CSS Selectors and Pagination format

CSS Selectors migrated from bullets to table. Pagination normalized
to use URL pattern / Products per page bullet format."
```

### Task 3: Build validate_assessment.py

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/validate_assessment.py`

This is the simpler script — pure markdown parsing, no HTTP. Build it first.

- [ ] **Step 1: Create script skeleton with PEP 723 metadata and CLI**

```python
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Validate a catalog assessment report against the self-verification gates.

Checks the markdown structure against success (12 gates) or stop (3 gates)
templates. Reports evidence; the LLM fixes issues.

Exit codes: 0 = all gates checked, 1 = some gates couldn't run, 2 = file error.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


def log(level: str, message: str, **extra: object) -> None:
    entry = {"level": level, "message": message,
             "timestamp": datetime.now(timezone.utc).isoformat(), **extra}
    print(json.dumps(entry), file=sys.stderr)


VALID_STRATEGIES = {"static_html", "structured_data", "pdf_pricelist", "none"}
VALID_PLATFORMS = {
    "woocommerce", "shopify", "magento", "prestashop", "opencart",
    "bigcommerce", "squarespace", "wix", "drupal", "custom", "unknown",
}
VALID_STOP_REASONS = {
    "no_public_catalog", "auth_required", "anti_bot_severe",
    "js_only", "attributes_not_extractable",
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate catalog assessment report")
    parser.add_argument("file", type=Path, help="Path to catalog assessment markdown")
    parser.add_argument("--knowledgebase-dir", type=Path,
                        default=Path("docs/platform-knowledgebase"))
    args = parser.parse_args()

    if not args.file.exists():
        log("error", "File not found", path=str(args.file))
        sys.exit(2)

    content = args.file.read_text(encoding="utf-8")
    if not content.strip():
        log("error", "File is empty", path=str(args.file))
        sys.exit(2)

    # ... gate checks ...
    result = run_gates(content, args.knowledgebase_dir)
    print(json.dumps(result, indent=2))
    sys.exit(0 if all(g.get("pass") is not None for g in result["gates"].values()) else 1)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Implement template detection and metadata extraction helpers**

```python
def detect_template(content: str) -> str:
    """Return 'success', 'stop', or 'unknown'."""
    has_blueprint = "## Extraction Blueprint" in content
    has_stop = "**Stop reason:**" in content and "**Scraping strategy:** none" in content
    if has_stop:
        return "stop"
    if has_blueprint:
        return "success"
    return "unknown"


def extract_field(content: str, field_name: str) -> str | None:
    """Extract value from **Field:** value pattern."""
    pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+)"
    match = re.search(pattern, content)
    return match.group(1).strip() if match else None


def extract_slug(content: str) -> str | None:
    return extract_field(content, "Slug")


def extract_section(content: str, heading: str) -> str | None:
    """Extract content under a markdown heading (## or ###)."""
    pattern = rf"^(#{2,4})\s+{re.escape(heading)}\s*\n(.*?)(?=\n#{2,4}\s|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return match.group(2) if match else None
```

- [ ] **Step 3: Implement all 12 success gate checks**

Each gate is a function returning `{"pass": bool, "details": str}`:

```python
def check_correct_template(content: str, template: str) -> dict:
    if template == "success":
        return {"pass": True, "details": "Success template detected: has Extraction Blueprint section"}
    if template == "stop":
        return {"pass": True, "details": "Stop template detected: has Stop reason field"}
    return {"pass": False, "details": "Neither success nor stop template detected"}


def check_heading_and_slug(content: str) -> dict:
    h1_match = re.search(r"^# Catalog Assessment: .+", content, re.MULTILINE)
    slug = extract_slug(content)
    if h1_match and slug:
        return {"pass": True, "details": f"H1: '{h1_match.group(0)}', Slug: '{slug}'"}
    issues = []
    if not h1_match:
        issues.append("H1 missing or wrong format")
    if not slug:
        issues.append("Slug field missing")
    return {"pass": False, "details": "; ".join(issues)}


def check_strategy_valid(content: str) -> dict:
    strategy = extract_field(content, "Scraping strategy")
    if strategy and strategy.split()[0] in VALID_STRATEGIES:
        return {"pass": True, "details": f"Strategy: {strategy}"}
    return {"pass": False, "details": f"Invalid strategy: {strategy}"}


def check_platform_valid(content: str) -> dict:
    platform = extract_field(content, "Platform")
    if platform and platform.split()[0] in VALID_PLATFORMS:
        return {"pass": True, "details": f"Platform: {platform}"}
    return {"pass": False, "details": f"Invalid platform: {platform}"}


def check_data_source_concrete(content: str) -> dict:
    section = extract_section(content, "Data Source")
    if not section:
        return {"pass": False, "details": "### Data Source section missing"}
    has_method = "**Primary method:**" in section
    has_endpoint = "**Endpoint/URL pattern:**" in section
    if has_method and has_endpoint:
        method = extract_field(section, "Primary method")
        return {"pass": True, "details": f"Primary method: {method}, has endpoint/URL pattern"}
    return {"pass": False, "details": f"Missing: {'method' if not has_method else ''} {'endpoint' if not has_endpoint else ''}".strip()}


def check_discovery_actionable(content: str) -> dict:
    section = extract_section(content, "Product Discovery")
    if not section:
        return {"pass": False, "details": "### Product Discovery section missing"}
    fields = ["Discovery method", "Pagination mechanism", "Products per page"]
    found = [f for f in fields if f"**{f}:**" in section]
    if len(found) == len(fields):
        method = extract_field(section, "Discovery method")
        return {"pass": True, "details": f"Discovery method: {method}, all fields present"}
    missing = [f for f in fields if f not in found]
    return {"pass": False, "details": f"Missing: {', '.join(missing)}"}


def check_category_tree_complete(content: str) -> dict:
    section = extract_section(content, "Verified Category Tree")
    if not section:
        return {"pass": False, "details": "#### Verified Category Tree section missing"}
    # Parse table rows
    rows = [l for l in section.split("\n") if l.strip().startswith("|") and "---" not in l]
    if len(rows) < 2:
        return {"pass": False, "details": "Category tree table has no data rows"}
    data_rows = rows[1:]  # skip header
    leaf_missing = 0
    total_leaves = 0
    for row in data_rows:
        cells = [c.strip() for c in row.split("|")[1:-1]]
        if len(cells) < 4:
            continue
        count_cell = cells[2]  # Product Count column
        if "(landing)" in count_cell.lower():
            continue
        total_leaves += 1
        if not re.search(r"\d+", count_cell):
            leaf_missing += 1
    if leaf_missing == 0:
        return {"pass": True, "details": f"All {total_leaves} leaf categories have product counts"}
    return {"pass": False, "details": f"{leaf_missing} of {total_leaves} leaf categories missing product count"}


def check_price_verified(content: str) -> dict:
    section = extract_section(content, "Price")
    if not section:
        return {"pass": False, "details": "#### Price section missing"}
    verified = section.count("http")
    if verified >= 2:
        return {"pass": True, "details": f"{verified} product URLs found with price values in Verified on section"}
    return {"pass": False, "details": f"Only {verified} verified URLs (need >= 2)"}


def check_spec_table_verified(content: str) -> dict:
    # Look for "Spec Table" or "Attributes" section
    for heading in ["Spec Table / Attributes", "Spec Table", "Attributes"]:
        section = extract_section(content, heading)
        if section:
            break
    if not section:
        return {"pass": False, "details": "#### Spec Table / Attributes section missing"}
    verified = section.count("http")
    if verified >= 2:
        return {"pass": True, "details": f"{verified} product URLs found with attribute counts"}
    return {"pass": False, "details": f"Only {verified} verified URLs (need >= 2)"}


def check_product_count(content: str) -> dict:
    count_str = extract_field(content, "Estimated product count")
    if count_str and re.search(r"\d+", count_str):
        return {"pass": True, "details": count_str}
    return {"pass": False, "details": f"Product count missing or non-numeric: {count_str}"}


def check_knowledgebase_updated(content: str, kb_dir: Path) -> dict:
    slug = extract_slug(content)
    platform = extract_field(content, "Platform")
    if not slug or not platform:
        return {"pass": False, "details": "Cannot check: slug or platform missing from report"}
    platform_key = platform.split()[0].lower()
    kb_file = kb_dir / f"{platform_key}.md"
    if not kb_file.exists():
        if platform_key in ("unknown", "custom"):
            return {"pass": True, "details": f"Platform is {platform_key}, no knowledgebase expected"}
        return {"pass": False, "details": f"Knowledgebase file {kb_file} does not exist"}
    kb_content = kb_file.read_text(encoding="utf-8")
    if slug in kb_content:
        return {"pass": True, "details": f"Found '{slug}' in {kb_file.name} Sites table"}
    return {"pass": False, "details": f"Slug '{slug}' not found in {kb_file.name}"}


def check_anti_bot_value(content: str) -> dict:
    value = extract_field(content, "Anti-bot")
    if value and value.split()[0] in ("none", "light", "moderate"):
        return {"pass": True, "details": f"Anti-bot: {value.split()[0]}"}
    return {"pass": False, "details": f"Invalid anti-bot value: {value}"}
```

- [ ] **Step 4: Implement 3 stop gate checks**

```python
def check_stop_template(content: str) -> dict:
    has_strategy_none = "**Scraping strategy:** none" in content
    has_stop_reason = "**Stop reason:**" in content
    if has_strategy_none and has_stop_reason:
        return {"pass": True, "details": "Stop template: strategy=none, stop reason present"}
    return {"pass": False, "details": f"Missing: {'strategy none' if not has_strategy_none else ''} {'stop reason' if not has_stop_reason else ''}"}


def check_valid_stop_reason(content: str) -> dict:
    reason = extract_field(content, "Stop reason")
    if reason and reason.strip() in VALID_STOP_REASONS:
        return {"pass": True, "details": f"Stop reason: {reason}"}
    return {"pass": False, "details": f"Invalid stop reason: {reason}"}


def check_findings_explain(content: str) -> dict:
    section = extract_section(content, "Findings")
    if section and "-" in section:
        bullet_count = section.count("\n-")
        return {"pass": True, "details": f"Findings section has {bullet_count} bullet(s)"}
    return {"pass": False, "details": "## Findings section missing or has no bullets"}
```

- [ ] **Step 5: Wire gates into run_gates orchestrator**

```python
def run_gates(content: str, kb_dir: Path) -> dict:
    template = detect_template(content)
    gates = {}
    issues = []

    if template == "stop":
        gate_fns = {
            "stop_template": lambda: check_stop_template(content),
            "valid_stop_reason": lambda: check_valid_stop_reason(content),
            "findings_explain": lambda: check_findings_explain(content),
        }
    elif template == "success":
        gate_fns = {
            "correct_template": lambda: check_correct_template(content, template),
            "heading_and_slug": lambda: check_heading_and_slug(content),
            "strategy_valid": lambda: check_strategy_valid(content),
            "platform_valid": lambda: check_platform_valid(content),
            "data_source_concrete": lambda: check_data_source_concrete(content),
            "discovery_actionable": lambda: check_discovery_actionable(content),
            "category_tree_complete": lambda: check_category_tree_complete(content),
            "price_verified": lambda: check_price_verified(content),
            "spec_table_verified": lambda: check_spec_table_verified(content),
            "product_count": lambda: check_product_count(content),
            "knowledgebase_updated": lambda: check_knowledgebase_updated(content, kb_dir),
            "anti_bot_value": lambda: check_anti_bot_value(content),
        }
    else:
        gates["correct_template"] = check_correct_template(content, template)
        issues.append("Gate 1 (correct_template): neither success nor stop template")
        return {"file": "", "detected_template": "unknown", "gates": gates,
                "passed": 0, "failed": 1, "issues": issues}

    for name, fn in gate_fns.items():
        try:
            result = fn()
            gates[name] = result
            log("info", f"Gate {name}: {'PASS' if result['pass'] else 'FAIL'}", details=result["details"])
            if not result["pass"]:
                issues.append(f"Gate ({name}): {result['details']}")
        except Exception as exc:
            gates[name] = {"pass": None, "details": f"Error: {exc}"}
            issues.append(f"Gate ({name}): error — {exc}")
            log("error", f"Gate {name} crashed", error=str(exc))

    passed = sum(1 for g in gates.values() if g.get("pass") is True)
    failed = sum(1 for g in gates.values() if g.get("pass") is False)

    return {
        "file": "",  # filled by caller
        "detected_template": template,
        "gates": gates,
        "passed": passed,
        "failed": failed,
        "issues": issues,
    }
```

- [ ] **Step 6: Test against existing catalog assessments**

Run against the 6 existing assessments:
```bash
for f in docs/catalog-detector/*.md; do
  echo "=== $(basename $f) ==="
  uv run python .claude/skills/catalog-detector/scripts/validate_assessment.py "$f" \
    --knowledgebase-dir docs/platform-knowledgebase 2>/dev/null | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(f\"  Template: {r['detected_template']}, Passed: {r['passed']}, Failed: {r['failed']}\")
for i in r['issues']: print(f'  - {i}')
"
done
```

Expected: uk-timber.md and harlowbros.md pass most gates (success template). timbersource.md and thetimbermerchants.md pass stop gates. Some failures are expected (e.g., knowledgebase not updated for all).

- [ ] **Step 7: Commit**

```bash
git add .claude/skills/catalog-detector/scripts/validate_assessment.py
git commit -m "Add validate_assessment.py for catalog-detector report validation

Checks 12 success gates or 3 stop gates against the catalog assessment
markdown. Pure regex/string matching, no HTTP. Exit codes: 0/1/2."
```

---

## Chunk 2: catalog_probe.py — Core Infrastructure

### Task 4: Script skeleton + logging + HTTP helpers

**Files:**
- Create: `.claude/skills/catalog-detector/scripts/catalog_probe.py`

- [ ] **Step 1: Create script with PEP 723 metadata, CLI, and logging**

```python
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
```

- [ ] **Step 2: Implement HTTP helper with delay, retry, truncation, transport tracking**

```python
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
```

- [ ] **Step 3: Implement challenge page detection**

```python
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
```

- [ ] **Step 4: Implement CLI argument parsing**

```python
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
```

- [ ] **Step 5: Commit skeleton**

```bash
git add .claude/skills/catalog-detector/scripts/catalog_probe.py
git commit -m "Add catalog_probe.py skeleton with HTTP helpers and transport tracking"
```

### Task 5: Platform detection + anti-bot + JS signals + geo hints

**Files:**
- Modify: `.claude/skills/catalog-detector/scripts/catalog_probe.py`

- [ ] **Step 1: Implement platform signal detection**

```python
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
```

- [ ] **Step 2: Implement anti-bot, JS rendering, and geo hint extraction**

```python
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
```

- [ ] **Step 3: Implement body text length extraction helper (reused across sections)**

```python
def get_body_text_length(html: str) -> int:
    tree = HTMLParser(html)
    for tag in tree.css("script, style"):
        tag.decompose()
    body = tree.css_first("body")
    return len(body.text(strip=True)) if body else 0
```

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/catalog-detector/scripts/catalog_probe.py
git commit -m "Add platform detection, anti-bot, JS signals, geo hints to catalog_probe.py"
```

---

## Chunk 3: catalog_probe.py — Sitemap, Recipe Verification, Assembly

### Task 6: Robots.txt + sitemap parsing + homepage links

**Files:**
- Modify: `.claude/skills/catalog-detector/scripts/catalog_probe.py`

- [ ] **Step 1: Implement robots.txt parsing**

```python
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
```

- [ ] **Step 2: Implement sitemap parsing with index recursion and diverse sampling**

```python
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
```

- [ ] **Step 3: Implement homepage link extraction**

```python
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
```

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/catalog-detector/scripts/catalog_probe.py
git commit -m "Add robots.txt, sitemap parsing, homepage link extraction to catalog_probe.py"
```

### Task 7: Knowledgebase parsing + recipe verification + main assembly

**Files:**
- Modify: `.claude/skills/catalog-detector/scripts/catalog_probe.py`

- [ ] **Step 1: Implement knowledgebase parser**

```python
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


def extract_md_section(content: str, heading: str) -> str | None:
    """Extract content under a ## heading."""
    pattern = rf"^## {re.escape(heading)}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None
```

- [ ] **Step 2: Implement recipe verification (CSS + JSON-LD + API checks)**

```python
def verify_recipe(client: httpx.Client, product_urls: list[str],
                  kb: dict, *, timeout: float, delay: float,
                  max_size: int, tracker: TransportTracker) -> dict:
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
                if data.get("@type") == "Product":
                    json_ld_product = data
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
```

- [ ] **Step 3: Implement pagination check**

```python
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
    p1_links = {a.attributes.get("href", "") for a in tree1.css("a[href]")
                if a.attributes.get("href", "").endswith(".html")}

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
    p2_links = {a.attributes.get("href", "") for a in tree2.css("a[href]")
                if a.attributes.get("href", "").endswith(".html")}

    return {
        "tested": True,
        "category_url": category_url,
        "page1_product_count": len(p1_links),
        "page2_url": page2_url,
        "page2_status": status2,
        "page2_product_count": len(p2_links),
        "products_differ": bool(p2_links - p1_links),
    }
```

- [ ] **Step 4: Implement recipe_match confidence calculation**

```python
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
```

- [ ] **Step 5: Add URL pattern guessing helper**

```python
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
```

- [ ] **Step 6: Implement main() assembly — wire everything together**

```python
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
                    if "@type" in data:
                        json_ld_types.append(data["@type"])
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
                if best_recipe is None or recipe_match == "full":
                    best_recipe = candidate

                # Check product page for anti-bot (from first platform tested)
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
```

- [ ] **Step 7: Test against real sites**

```bash
# Test against uk-timber (known PrestaShop)
uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url https://www.uk-timber.co.uk \
  --knowledgebase-dir docs/platform-knowledgebase \
  2>/tmp/probe_stderr.log | python3 -m json.tool | head -30

# Check stderr logs
cat /tmp/probe_stderr.log | head -20

# Test against a Cloudflare-blocked site
uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py \
  --url https://www.timbersource.co.uk \
  --knowledgebase-dir docs/platform-knowledgebase \
  2>/tmp/probe_stderr2.log | python3 -m json.tool | head -30
```

Expected for uk-timber: `platform_guess: "prestashop"`, `platform_confidence: "definitive"`, `recipe_match: "full"` or `"partial"`, `transport_health.overall: "healthy"`.

Expected for timbersource: `challenge_page_detected: true` or `transport_health.overall: "blocked"`.

- [ ] **Step 8: Commit**

```bash
git add .claude/skills/catalog-detector/scripts/catalog_probe.py
git commit -m "Complete catalog_probe.py with recipe verification, sitemap, and assembly

Full probe script: platform detection, anti-bot/JS/geo signals, robots.txt,
sitemap parsing, knowledgebase recipe verification, transport health tracking."
```

---

## Chunk 4: Workflow Integration + End-to-End Validation

### Task 8: Update catalog-detector SKILL.md with script invocation

**Files:**
- Modify: `.claude/skills/catalog-detector/SKILL.md`

- [ ] **Step 1: Add script invocation bullets to Workflow section**

Add these bullets to the `## Workflow` section, after "Read and follow `references/workflow.md`." and before the existing bullets:

```markdown
- Before starting the workflow, run the catalog probe script:
  `uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py --url {site_url} --knowledgebase-dir docs/platform-knowledgebase 2>docs/catalog-detector/{slug}_probe_stderr.log`
  Parse stdout as JSON. Read the stderr log file for diagnostics if needed.
  - Exit code 0 or 1: use the probe results to inform Steps 1-3. Routing logic:
    - If recipe_match is "full" AND transport_health.overall is "healthy" AND anti_bot shows no blocking AND js_rendering_signals show no SPA framework:
      → Skip Steps 1-3, proceed to Step 4 using the probe data.
    - If recipe_match is "full" BUT anti_bot shows issues OR js_rendering_signals.text_to_html_ratio < 0.05:
      → Skip Steps 1-2, proceed to Step 3 for deeper investigation of the flagged concern.
    - If recipe_match is "partial" or "poor":
      → Use probe data as a starting point, proceed to Step 3 (starting at 3b, the probe already covers 3a).
    - If recipe_match is "untested" (no knowledgebase or all URLs failed):
      → Proceed to Step 3 from 3a, using probe's anti_bot and platform signals as context.
    - If platform_guess is "unknown" but signals suggest a recognizable CMS, classify as "custom" — the script never returns "custom" because that requires LLM judgment.
    - Check the errors array: any entry means the corresponding section's data is incomplete. Supplement with manual investigation for those sections.
  - Exit code 2: ignore the script output, fall back to manual Steps 1-3 entirely.
  - DO NOT modify the probe script. If it produces unexpected results, use manual reasoning to verify or override — the script output is evidence, not a verdict.
- After writing the catalog assessment, run the validation script:
  `uv run python .claude/skills/catalog-detector/scripts/validate_assessment.py docs/catalog-detector/{slug}.md --knowledgebase-dir docs/platform-knowledgebase 2>docs/catalog-detector/{slug}_validate_stderr.log`
  Fix any failing gates. DO NOT modify the validation script.
- **These scripts are infrastructure, not generated code. Never edit, patch, or fix them during a pipeline run — even if you can identify the bug. If a script fails (exit code 2) or produces unexpected results, fall back to manual reasoning for those steps. Record the issue in the catalog assessment's Platform-Specific Notes so it can be fixed in a dedicated maintenance pass. Editing scripts mid-pipeline risks introducing regressions that affect other companies.**
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/catalog-detector/SKILL.md
git commit -m "Add probe and validation script invocation to catalog-detector workflow

Scripts are called before and after the LLM workflow. Immutability rule
ensures scripts are never modified during pipeline execution."
```

### Task 9: End-to-end validation

- [ ] **Step 1: Run probe against all known sites and verify output structure**

```bash
for url in "https://www.uk-timber.co.uk" "https://www.iwood.co.uk" "https://www.harlowbros.co.uk"; do
  slug=$(echo "$url" | sed 's|.*://||;s|www\.||;s|\..*||')
  echo "=== $slug ==="
  uv run python .claude/skills/catalog-detector/scripts/catalog_probe.py \
    --url "$url" --knowledgebase-dir docs/platform-knowledgebase \
    2>/dev/null | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(f\"  Platform: {r['platform_guess']} ({r['platform_confidence']})\")
print(f\"  Recipe: {r['recipe_verification']['recipe_match']}\")
print(f\"  Transport: {r['transport_health']['overall']}\")
print(f\"  Errors: {len(r['errors'])}\")
"
done
```

- [ ] **Step 2: Run validator against all existing assessments**

```bash
for f in docs/catalog-detector/*.md; do
  echo "=== $(basename $f) ==="
  uv run python .claude/skills/catalog-detector/scripts/validate_assessment.py "$f" \
    --knowledgebase-dir docs/platform-knowledgebase 2>/dev/null | python3 -c "
import sys, json
r = json.load(sys.stdin)
print(f\"  Template: {r['detected_template']}, Passed: {r['passed']}, Failed: {r['failed']}\")
for i in r['issues'][:3]: print(f'  - {i}')
"
done
```

- [ ] **Step 3: Run skill-creator-local verification**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py catalog-detector
```

Expected: PASS with 0 issues.

- [ ] **Step 4: Final commit**

```bash
git add -A
git commit -m "End-to-end validation of catalog-detector scripts

Probe tested against uk-timber, iwood, harlowbros. Validator tested
against all 6 existing catalog assessments. Skill verification passes."
```
