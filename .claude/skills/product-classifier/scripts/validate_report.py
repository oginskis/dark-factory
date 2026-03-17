# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Validate a product-classifier company report against self-verification gates.

WHEN TO CALL: After writing the company report (Step 5), before presenting results.
ARGUMENTS:
    file                  Path to company report markdown
    --categories-file     Path to product taxonomy categories.md
EXIT CODES:
    0 = all gates checked (pass/fail in output)
    1 = some gates couldn't run
    2 = file error

Gates checked:
    1. All canonical sections present
    2. Primary is a valid taxonomy ID
    3. Subcategories contain valid taxonomy IDs
    4. All taxonomy IDs exist in categories.md
    5. Slug is present
    6. Product lines described (### subsections under ## Products)
    7. References populated (at least 2 markdown links)
    8. Primary appears in Subcategories
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


def extract_field(content: str, field_name: str) -> str | None:
    """Extract value from **Field:** value pattern."""
    pattern = rf"\*\*{re.escape(field_name)}:\*\*\s*(.+)"
    match = re.search(pattern, content)
    return match.group(1).strip() if match else None


def parse_taxonomy_ids(categories_path: Path) -> dict[str, str]:
    """Parse categories.md and return {id: display_name} dict."""
    content = categories_path.read_text(encoding="utf-8")
    ids = {}
    for line in content.split("\n"):
        m = re.match(r'^- (.+?) `([a-z][a-z0-9_.]+)`$', line.strip())
        if m:
            ids[m.group(2)] = m.group(1).strip()
    return ids


def extract_subcategory_ids(content: str) -> list[str]:
    """Extract taxonomy IDs from the Subcategories row in the Business Classification table."""
    m = re.search(r'\|\s*Subcategories\s*\|\s*(.+?)\s*\|', content)
    if not m:
        return []
    return re.findall(r'`([a-z][a-z0-9_.]+)`', m.group(1))


def extract_primary_id(content: str) -> str | None:
    """Extract the Primary taxonomy ID from the Business Classification table."""
    # Match table row: | Primary | `id` (Display Name) |
    m = re.search(r'\|\s*Primary\s*\|\s*`([a-z][a-z0-9_.]+)`', content)
    return m.group(1) if m else None


# --- Gates ---

def check_sections_present(content: str) -> dict:
    """
    WHAT IT CHECKS: All 6 canonical sections exist in the report.
    FAILURE MEANS: Report is structurally incomplete.
    HOW TO FIX: Add the missing ## section(s).
    """
    required = ["Overview", "Business Classification", "Products",
                 "Product Catalog Analysis (Preliminary)", "Findings", "References"]
    missing = [s for s in required if f"## {s}" not in content]
    if not missing:
        return {"pass": True, "details": "All 6 canonical sections present"}
    return {"pass": False, "details": f"Missing sections: {', '.join(missing)}"}


def check_primary_valid(content: str, taxonomy: dict[str, str]) -> dict:
    """
    WHAT IT CHECKS: Primary taxonomy ID exists in categories.md.
    FAILURE MEANS: The Primary ID is invented, misspelled, or not from the taxonomy file.
    HOW TO FIX: Look up the correct ID in docs/product-taxonomy/categories.md.
    """
    primary = extract_primary_id(content)
    if not primary:
        return {"pass": False, "details": "No Primary taxonomy ID found"}
    if primary in taxonomy:
        return {"pass": True, "details": f"Primary `{primary}` found in taxonomy"}
    return {"pass": False, "details": f"Primary `{primary}` NOT in categories.md"}


def check_subcategories_valid(content: str, taxonomy: dict[str, str]) -> dict:
    """
    WHAT IT CHECKS: All Subcategories taxonomy IDs exist in categories.md.
    FAILURE MEANS: One or more IDs are invented or misspelled.
    HOW TO FIX: Look up each ID in docs/product-taxonomy/categories.md.
    """
    ids = extract_subcategory_ids(content)
    if not ids:
        return {"pass": False, "details": "No taxonomy IDs found in report"}
    invalid = [i for i in ids if i not in taxonomy]
    if not invalid:
        return {"pass": True, "details": f"All {len(ids)} taxonomy IDs valid"}
    return {"pass": False, "details": f"Invalid IDs: {', '.join(invalid)}"}


def check_all_ids_in_taxonomy(content: str, taxonomy: dict[str, str]) -> dict:
    """
    WHAT IT CHECKS: Every backtick-delimited taxonomy ID in the report exists in categories.md.
    FAILURE MEANS: The report contains taxonomy IDs that don't exist.
    HOW TO FIX: Replace invented IDs with real ones from categories.md.
    """
    ids = extract_subcategory_ids(content)
    invalid = [i for i in ids if i not in taxonomy]
    if not invalid:
        return {"pass": True, "details": f"All {len(ids)} IDs exist in taxonomy"}
    return {"pass": False, "details": f"IDs not in categories.md: {', '.join(invalid)}"}


def check_slug_present(content: str) -> dict:
    """
    WHAT IT CHECKS: **Slug:** field exists and is non-empty.
    FAILURE MEANS: Slug is missing from the report header.
    HOW TO FIX: Add **Slug:** {slug} derived from the company domain.
    """
    slug = extract_field(content, "Slug")
    if slug:
        return {"pass": True, "details": f"Slug: {slug}"}
    return {"pass": False, "details": "Slug field missing"}


def check_product_lines(content: str) -> dict:
    """
    WHAT IT CHECKS: At least one ### subsection exists under ## Products.
    FAILURE MEANS: Product lines are not described with proper headings.
    HOW TO FIX: Add ### subsections for each major product line under ## Products.
    """
    products_match = re.search(r'^## Products\s*\n(.*?)(?=\n## |\Z)', content,
                                re.MULTILINE | re.DOTALL)
    if not products_match:
        return {"pass": False, "details": "## Products section not found"}
    section = products_match.group(1)
    headings = re.findall(r'^### .+', section, re.MULTILINE)
    if headings:
        return {"pass": True, "details": f"{len(headings)} product line subsections"}
    return {"pass": False, "details": "No ### subsections under ## Products"}


def check_references(content: str) -> dict:
    """
    WHAT IT CHECKS: References section has at least 2 markdown links.
    FAILURE MEANS: Investigation was too shallow or references weren't recorded.
    HOW TO FIX: Add markdown links for key pages visited during investigation.
    """
    refs_match = re.search(r'^## References\s*\n(.*?)(?=\n## |\Z)', content,
                            re.MULTILINE | re.DOTALL)
    if not refs_match:
        return {"pass": False, "details": "## References section not found"}
    links = re.findall(r'\[.+?\]\(https?://.+?\)', refs_match.group(1))
    if len(links) >= 2:
        return {"pass": True, "details": f"{len(links)} reference links"}
    return {"pass": False, "details": f"Only {len(links)} reference links (need >= 2)"}


def check_primary_in_subcategories(content: str) -> dict:
    """
    WHAT IT CHECKS: The Primary taxonomy ID also appears in the Subcategories row.
    FAILURE MEANS: Primary was set but not included in the Subcategories list.
    HOW TO FIX: Add the Primary ID to the Subcategories row.
    """
    primary = extract_primary_id(content)
    if not primary:
        return {"pass": False, "details": "Cannot check: no Primary ID found"}
    sub_ids = extract_subcategory_ids(content)
    if primary in sub_ids:
        return {"pass": True, "details": f"Primary `{primary}` appears in Subcategories"}
    return {"pass": False, "details": f"Primary `{primary}` not found in Subcategories row"}


def run_gates(content: str, taxonomy: dict[str, str]) -> dict:
    gate_fns = {
        "sections_present": lambda: check_sections_present(content),
        "primary_valid": lambda: check_primary_valid(content, taxonomy),
        "subcategories_valid": lambda: check_subcategories_valid(content, taxonomy),
        "all_ids_in_taxonomy": lambda: check_all_ids_in_taxonomy(content, taxonomy),
        "slug_present": lambda: check_slug_present(content),
        "product_lines": lambda: check_product_lines(content),
        "references": lambda: check_references(content),
        "primary_in_subcategories": lambda: check_primary_in_subcategories(content),
    }

    gates = {}
    issues = []
    for name, fn in gate_fns.items():
        try:
            result = fn()
            gates[name] = result
            if not result["pass"]:
                issues.append(f"Gate ({name}): {result['details']}")
        except Exception as exc:
            gates[name] = {"pass": None, "details": f"Error: {exc}"}
            issues.append(f"Gate ({name}): error — {exc}")

    passed = sum(1 for g in gates.values() if g.get("pass") is True)
    failed = sum(1 for g in gates.values() if g.get("pass") is False)

    return {
        "file": "",
        "gates": gates,
        "passed": passed,
        "failed": failed,
        "issues": issues,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate product-classifier company report")
    parser.add_argument("file", type=Path, help="Path to company report markdown")
    parser.add_argument("--categories-file", type=Path,
                        default=Path("docs/product-taxonomy/categories.md"))
    parser.add_argument("--output-json", type=Path, default=None,
                        help="Write gate results to this JSON file")
    args = parser.parse_args()

    if not args.file.exists():
        log("error", "File not found", path=str(args.file))
        sys.exit(2)

    if not args.categories_file.exists():
        log("error", "Categories file not found", path=str(args.categories_file))
        sys.exit(2)

    content = args.file.read_text(encoding="utf-8")
    if not content.strip():
        log("error", "File is empty", path=str(args.file))
        sys.exit(2)

    taxonomy = parse_taxonomy_ids(args.categories_file)
    result = run_gates(content, taxonomy)
    result["file"] = str(args.file)

    output = json.dumps(result, indent=2)
    print(output)

    if args.output_json:
        args.output_json.parent.mkdir(parents=True, exist_ok=True)
        args.output_json.write_text(output)

    sys.exit(0 if all(g.get("pass") is not None for g in result["gates"].values()) else 1)


if __name__ == "__main__":
    main()
