# /// script
# requires-python = ">=3.10"
# ///
"""Verify that every SKU schema file conforms to the two-table format.

Checks:
1. Has ## Core Attributes and ## Extended Attributes (not old ## Attributes)
2. Has **Taxonomy ID:** with a backtick-enclosed ID matching categories.md
3. Core attribute count: 5-10
4. Extended attribute count: 10-15
5. Total attributes: 15-30
6. No backticks in table data cells
7. No duplicate attribute names across core and extended tables
8. Each table has exactly 4 columns: Attribute, Data Type, Description, Example Values
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "docs" / "product-taxonomy" / "sku-schemas"
CATEGORIES_FILE = REPO_ROOT / "docs" / "product-taxonomy" / "categories.md"

EXPECTED_COLUMNS = ["Attribute", "Data Type", "Description", "Example Values"]


def load_taxonomy_ids() -> set[str]:
    """Load valid taxonomy IDs from categories.md."""
    if not CATEGORIES_FILE.exists():
        print(f"WARNING: categories file not found: {CATEGORIES_FILE}")
        return set()

    ids: set[str] = set()
    for line in CATEGORIES_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- "):
            continue
        for tid in re.findall(r"`([a-z][a-z0-9_.]+)`", line):
            ids.add(tid)
    return ids


def parse_table_rows(lines: list[str], start: int) -> tuple[list[str], list[list[str]], int]:
    """Parse a markdown table starting at `start`. Returns (header_cols, data_rows, end_index)."""
    header_cols: list[str] = []
    data_rows: list[list[str]] = []
    i = start

    # Find the header row (first line starting with |)
    while i < len(lines) and not lines[i].strip().startswith("|"):
        i += 1

    if i >= len(lines):
        return header_cols, data_rows, i

    # Header row
    header_cols = [c.strip() for c in lines[i].strip().strip("|").split("|")]
    i += 1

    # Separator row (|---|---|...)
    if i < len(lines) and re.match(r"\s*\|[-| ]+\|\s*$", lines[i]):
        i += 1

    # Data rows
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        data_rows.append(cells)
        i += 1

    return header_cols, data_rows, i


def verify_schema(filepath: Path, valid_ids: set[str]) -> list[str]:
    """Verify a single schema file. Returns a list of error messages (empty = pass)."""
    errors: list[str] = []
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- Check 1: Section headers ---
    has_core = any(line.strip() == "## Core Attributes" for line in lines)
    has_extended = any(line.strip() == "## Extended Attributes" for line in lines)
    has_old = any(line.strip() == "## Attributes" for line in lines)

    if has_old:
        errors.append("has old '## Attributes' section (should be Core + Extended)")
    if not has_core:
        errors.append("missing '## Core Attributes' section")
    if not has_extended:
        errors.append("missing '## Extended Attributes' section")

    # --- Check 2: Taxonomy ID ---
    taxonomy_id: str | None = None
    for line in lines:
        if line.startswith("**Taxonomy ID:**"):
            match = re.search(r"`([^`]+)`", line)
            if match:
                taxonomy_id = match.group(1)
            else:
                errors.append("**Taxonomy ID:** line present but no backtick-enclosed ID found")
            break
    else:
        errors.append("missing **Taxonomy ID:** header line")

    if taxonomy_id is not None and valid_ids and taxonomy_id not in valid_ids:
        errors.append(f"taxonomy ID `{taxonomy_id}` not found in categories.md")

    # If we don't have the required sections, skip table-level checks
    if not has_core or not has_extended:
        return errors

    # Locate section start lines
    core_start = next(i for i, l in enumerate(lines) if l.strip() == "## Core Attributes")
    ext_start = next(i for i, l in enumerate(lines) if l.strip() == "## Extended Attributes")

    # --- Parse tables ---
    core_header, core_rows, _ = parse_table_rows(lines, core_start + 1)
    ext_header, ext_rows, _ = parse_table_rows(lines, ext_start + 1)

    # --- Check 8: Column structure ---
    if core_header != EXPECTED_COLUMNS:
        errors.append(
            f"Core Attributes table columns {core_header} != expected {EXPECTED_COLUMNS}"
        )
    if ext_header != EXPECTED_COLUMNS:
        errors.append(
            f"Extended Attributes table columns {ext_header} != expected {EXPECTED_COLUMNS}"
        )

    # --- Check 3/4/5: Attribute counts ---
    core_count = len(core_rows)
    ext_count = len(ext_rows)
    total = core_count + ext_count

    if core_count < 5 or core_count > 10:
        errors.append(f"core attribute count {core_count} not in range 5-10")
    if ext_count < 10 or ext_count > 15:
        errors.append(f"extended attribute count {ext_count} not in range 10-15")
    if total < 15 or total > 30:
        errors.append(f"total attribute count {total} not in range 15-30")

    # --- Check 6: No backticks in data cells ---
    for row_idx, row in enumerate(core_rows, start=1):
        for cell in row:
            if "`" in cell:
                errors.append(
                    f"backtick in Core Attributes data row {row_idx}: {cell[:60]}"
                )
                break
    for row_idx, row in enumerate(ext_rows, start=1):
        for cell in row:
            if "`" in cell:
                errors.append(
                    f"backtick in Extended Attributes data row {row_idx}: {cell[:60]}"
                )
                break

    # --- Check 7: No duplicate attribute names ---
    core_names = [row[0] for row in core_rows if row]
    ext_names = [row[0] for row in ext_rows if row]
    all_names = core_names + ext_names
    seen: set[str] = set()
    for name in all_names:
        if name in seen:
            errors.append(f"duplicate attribute name: '{name}'")
        seen.add(name)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verify SKU schema files conform to the two-table format."
    )
    parser.add_argument(
        "--file",
        type=Path,
        default=None,
        help="Verify a single schema file instead of all schemas.",
    )
    args = parser.parse_args()

    valid_ids = load_taxonomy_ids()

    if args.file:
        files = [args.file]
    else:
        if not SCHEMAS_DIR.exists():
            print(f"FAIL: schemas directory not found: {SCHEMAS_DIR}")
            return 1
        files = sorted(SCHEMAS_DIR.glob("*.md"))

    if not files:
        print("No schema files found.")
        return 1

    passed = 0
    failed = 0

    for filepath in files:
        errs = verify_schema(filepath, valid_ids)
        if errs:
            failed += 1
            print(f"FAIL: {filepath.name}")
            for e in errs:
                print(f"  - {e}")
        else:
            passed += 1
            print(f"PASS: {filepath.name}")

    total = passed + failed
    print(f"\n{passed}/{total} schemas passed")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
