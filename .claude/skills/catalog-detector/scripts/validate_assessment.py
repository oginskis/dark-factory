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


VALID_STRATEGIES = {"html_css", "json_api", "pdf", "none"}
VALID_PLATFORMS = {
    "woocommerce", "shopify", "magento", "prestashop", "opencart",
    "bigcommerce", "squarespace", "wix", "drupal", "custom", "unknown",
}
VALID_STOP_REASONS = {
    "no_public_catalog", "auth_required", "anti_bot_severe",
    "js_only", "attributes_not_extractable",
}


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
    pattern = rf"^(#{{2,4}})\s+{re.escape(heading)}\s*\n(.*?)(?=\n#{{2,4}}\s|\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    return match.group(2) if match else None


# ---------------------------------------------------------------------------
# Success gate checks (12 gates)
# ---------------------------------------------------------------------------

def check_correct_template(template: str) -> dict:
    """
    WHAT IT CHECKS: Whether the document matches a known template (success or stop).
    FAILURE MEANS: The document is missing key structural markers (## Extraction Blueprint
        or **Stop reason:**). It may be incomplete or use a non-standard format.
    HOW TO FIX: Ensure the document has either an '## Extraction Blueprint' section (success)
        or both '**Scraping strategy:** none' and '**Stop reason:**' fields (stop).
    """
    if template == "success":
        return {"pass": True, "details": "Success template detected: has Extraction Blueprint section"}
    if template == "stop":
        return {"pass": True, "details": "Stop template detected: has Stop reason field"}
    return {"pass": False, "details": "Neither success nor stop template detected"}


def check_heading_and_slug(content: str) -> dict:
    """
    WHAT IT CHECKS: H1 heading matches '# Catalog Assessment: {name}' and **Slug:** field exists.
    FAILURE MEANS: The document header is malformed or the slug identifier is missing.
    HOW TO FIX: Ensure line 1 is '# Catalog Assessment: Company Name' and add '**Slug:** company-slug'.
    """
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
    """
    WHAT IT CHECKS: **Scraping strategy:** is one of {html_css, json_api, pdf, none}.
    FAILURE MEANS: The strategy field is missing or uses a non-standard value.
    HOW TO FIX: Set **Scraping strategy:** to one of the valid values.
    """
    strategy = extract_field(content, "Scraping strategy")
    if strategy and strategy.split()[0] in VALID_STRATEGIES:
        return {"pass": True, "details": f"Strategy: {strategy}"}
    return {"pass": False, "details": f"Invalid strategy: {strategy}"}


def check_platform_valid(content: str) -> dict:
    """
    WHAT IT CHECKS: **Platform:** is a recognized platform name.
    FAILURE MEANS: Platform field is missing or uses an unrecognized name.
    HOW TO FIX: Set **Platform:** to one of: woocommerce, shopify, magento, prestashop,
        opencart, bigcommerce, squarespace, wix, drupal, custom, unknown.
    """
    platform = extract_field(content, "Platform")
    if platform and platform.split()[0] in VALID_PLATFORMS:
        return {"pass": True, "details": f"Platform: {platform}"}
    return {"pass": False, "details": f"Invalid platform: {platform}"}


def check_data_source_concrete(content: str) -> dict:
    """
    WHAT IT CHECKS: ### Data Source section has **Primary method:** and **Endpoint/URL pattern:**.
    FAILURE MEANS: The extraction method or URL pattern is not documented.
    HOW TO FIX: Add both fields to the Data Source section with concrete values.
    """
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
    """
    WHAT IT CHECKS: Product Discovery section has all 4 required fields: Discovery method,
        Pagination mechanism, Products per page, Pagination URL pattern.
    FAILURE MEANS: Discovery information is incomplete — scraper-generator won't know how to crawl.
    HOW TO FIX: Add all 4 fields to the Product Discovery section.
    """
    section = extract_section(content, "Product Discovery")
    if not section:
        return {"pass": False, "details": "### Product Discovery section missing"}
    fields = ["Discovery method", "Pagination mechanism", "Products per page", "Pagination URL pattern"]
    found = [f for f in fields if f"**{f}:**" in section]
    if len(found) == len(fields):
        method = extract_field(section, "Discovery method")
        return {"pass": True, "details": f"Discovery method: {method}, all fields present"}
    missing = [f for f in fields if f not in found]
    return {"pass": False, "details": f"Missing: {', '.join(missing)}"}


def check_category_tree_complete(content: str) -> dict:
    """
    WHAT IT CHECKS: All leaf categories in the Verified Category Tree table have product counts.
    FAILURE MEANS: Some categories were listed without verifying how many products they contain.
    HOW TO FIX: Visit each leaf category URL and record the product count. Use '*' if count
        is acknowledged but unknown.
    """
    section = extract_section(content, "Verified Category Tree")
    if not section:
        return {"pass": False, "details": "#### Verified Category Tree section missing"}
    # Parse table rows
    rows = [line for line in section.split("\n") if line.strip().startswith("|") and "---" not in line]
    if len(rows) < 2:
        return {"pass": False, "details": "Category tree table has no data rows"}
    # Parse column index from header
    col_index = 2  # default fallback
    if rows:
        header_cells = [c.strip().lower() for c in rows[0].split("|")[1:-1]]
        for i, h in enumerate(header_cells):
            if "count" in h or "product count" in h:
                col_index = i
                break
    data_rows = rows[1:]  # skip header
    leaf_missing = 0
    total_leaves = 0
    for row in data_rows:
        cells = [c.strip() for c in row.split("|")[1:-1]]
        if len(cells) < col_index + 1:
            continue
        count_cell = cells[col_index]
        if "(landing)" in count_cell.lower():
            continue
        total_leaves += 1
        if count_cell.strip() in ("*", "—", "–", "-", ""):
            pass  # accepted as acknowledged-incomplete placeholder
        elif not re.search(r"\d+", count_cell):
            leaf_missing += 1
    if total_leaves == 0:
        return {"pass": False, "details": "Category tree table has no leaf categories (all rows skipped or landing pages)"}
    if leaf_missing == 0:
        return {"pass": True, "details": f"All {total_leaves} leaf categories have product counts"}
    return {"pass": False, "details": f"{leaf_missing} of {total_leaves} leaf categories missing product count"}


def check_price_verified(content: str) -> dict:
    """
    WHAT IT CHECKS: Price section contains >=2 URLs with observed price values.
    FAILURE MEANS: Price selector was written without being tested on real pages.
    HOW TO FIX: Navigate to 2+ product pages, observe the actual price rendered,
        and record each URL with its observed price in the Verified on: block.
    """
    section = extract_section(content, "Price")
    if not section:
        return {"pass": False, "details": "#### Price section missing"}
    verified = len(re.findall(r"[-–]\s+(?:https?://|/)[\S]+", section))
    if verified >= 2:
        return {"pass": True, "details": f"{verified} product URLs found with price values in Verified on section"}
    return {"pass": False, "details": f"Only {verified} verified URLs (need >= 2)"}


def check_spec_table_verified(content: str) -> dict:
    """
    WHAT IT CHECKS: Spec Table / Attributes section has >=2 URLs with attribute counts.
    FAILURE MEANS: Attribute selectors were written without being tested on real pages.
    HOW TO FIX: Navigate to 2+ product pages, verify attributes are extractable,
        and record each URL with observed attributes in the Verified on: block.
    """
    # Look for "Spec Table" or "Attributes" section
    section = None
    for heading in ["Spec Table / Attributes", "Spec Table", "Attributes"]:
        section = extract_section(content, heading)
        if section:
            break
    if not section:
        return {"pass": False, "details": "#### Spec Table / Attributes section missing"}
    verified = len(re.findall(r"[-–]\s+(?:https?://|/)[\S]+", section))
    if verified >= 2:
        return {"pass": True, "details": f"{verified} product URLs found with attribute counts"}
    return {"pass": False, "details": f"Only {verified} verified URLs (need >= 2)"}


def check_product_count(content: str) -> dict:
    """
    WHAT IT CHECKS: **Estimated product count:** contains a numeric value.
    FAILURE MEANS: No product count estimate was provided.
    HOW TO FIX: Add **Estimated product count:** with a number (e.g., '~500' or '1200').
    """
    count_str = extract_field(content, "Estimated product count")
    if count_str and re.search(r"\d+", count_str):
        return {"pass": True, "details": count_str}
    return {"pass": False, "details": f"Product count missing or non-numeric: {count_str}"}


def check_knowledgebase_updated(content: str, kb_dir: Path) -> dict:
    """
    WHAT IT CHECKS: The company slug appears in the platform knowledgebase file's Sites table.
    FAILURE MEANS: The knowledgebase was not updated with this company's findings.
    HOW TO FIX: Add a row for this company in the platform knowledgebase's Sites Using This Platform table.
    """
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
    """
    WHAT IT CHECKS: **Anti-bot:** is one of {none, light, moderate}.
    FAILURE MEANS: Anti-bot severity is missing or uses an invalid value. 'severe' is a stop
        condition (use stop template instead).
    HOW TO FIX: Set **Anti-bot:** to none, light, or moderate with a parenthetical explanation.
    """
    value = extract_field(content, "Anti-bot")
    if value and value.split()[0] in ("none", "light", "moderate"):
        return {"pass": True, "details": f"Anti-bot: {value.split()[0]}"}
    return {"pass": False, "details": f"Invalid anti-bot value: {value}"}


# ---------------------------------------------------------------------------
# Stop gate checks (3 gates)
# ---------------------------------------------------------------------------

def check_stop_template(content: str) -> dict:
    """
    WHAT IT CHECKS: Document has both '**Scraping strategy:** none' and '**Stop reason:**'.
    FAILURE MEANS: Stop template is incomplete.
    HOW TO FIX: Add both fields to the document header.
    """
    has_strategy_none = "**Scraping strategy:** none" in content
    has_stop_reason = "**Stop reason:**" in content
    if has_strategy_none and has_stop_reason:
        return {"pass": True, "details": "Stop template: strategy=none, stop reason present"}
    return {"pass": False, "details": f"Missing: {'strategy none' if not has_strategy_none else ''} {'stop reason' if not has_stop_reason else ''}"}


def check_valid_stop_reason(content: str) -> dict:
    """
    WHAT IT CHECKS: **Stop reason:** is a recognized value.
    FAILURE MEANS: Stop reason is missing or non-standard.
    HOW TO FIX: Set to one of: no_public_catalog, auth_required, anti_bot_severe, js_only,
        attributes_not_extractable.
    """
    reason = extract_field(content, "Stop reason")
    if reason and reason.strip() in VALID_STOP_REASONS:
        return {"pass": True, "details": f"Stop reason: {reason}"}
    return {"pass": False, "details": f"Invalid stop reason: {reason}"}


def check_findings_explain(content: str) -> dict:
    """
    WHAT IT CHECKS: ## Findings section exists and has at least one bullet point.
    FAILURE MEANS: No explanation of why scraping was stopped.
    HOW TO FIX: Add a ## Findings section with bullet points explaining what was found
        and why scraping is not viable.
    """
    section = extract_section(content, "Findings")
    if bool(section and section.count("\n-") > 0):
        bullet_count = section.count("\n-")
        return {"pass": True, "details": f"Findings section has {bullet_count} bullet(s)"}
    return {"pass": False, "details": "## Findings section missing or has no bullets"}


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

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
            "correct_template": lambda: check_correct_template(template),
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
        gates["correct_template"] = check_correct_template(template)
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate catalog assessment report")
    parser.add_argument("file", type=Path, help="Path to catalog assessment markdown")
    parser.add_argument("--knowledgebase-dir", type=Path,
                        default=Path("docs/platform-knowledgebase"))
    parser.add_argument("--output-json", type=Path, default=None,
                        help="Write gate results to this JSON file in addition to stdout")
    args = parser.parse_args()

    if not args.file.exists():
        log("error", "File not found", path=str(args.file))
        sys.exit(2)

    content = args.file.read_text(encoding="utf-8")
    if not content.strip():
        log("error", "File is empty", path=str(args.file))
        sys.exit(2)

    result = run_gates(content, args.knowledgebase_dir)
    result["file"] = str(args.file)

    output = json.dumps(result, indent=2)
    print(output)

    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(output)

    sys.exit(0 if all(g.get("pass") is not None for g in result["gates"].values()) else 1)


if __name__ == "__main__":
    main()
