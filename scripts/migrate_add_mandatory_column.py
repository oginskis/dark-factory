# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Migration: Add 'Mandatory' column to all SKU schema tables.

Inserts a 'Mandatory' column after 'Unit' in both Core Attributes and
Extended Attributes tables. Mandatory core keys (sku, product_name, url, price,
currency) get 'yes'; all others get '—'.

Usage:
    uv run scripts/migrate_add_mandatory_column.py              # dry-run
    uv run scripts/migrate_add_mandatory_column.py --apply      # write changes

Exit codes: 0 = success, 1 = errors encountered
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "docs" / "product-taxonomy" / "sku-schemas"

MANDATORY_CORE_KEYS = {"sku", "product_name", "url", "price", "currency"}


def _process_table(lines: list[str], i: int, new_lines: list[str], col_count: int) -> tuple[int, bool]:
    """Process a single attribute table, adding Unit (if missing) and Mandatory columns.

    col_count is 5 (old format, no Unit) or 6 (current format with Unit).
    Returns (new_i, modified).
    """
    # Rewrite header
    new_lines.append("| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |")

    # Separator line
    i += 1
    if i < len(lines) and lines[i].strip().startswith("|"):
        new_lines.append("|--------|--------|--------|--------|-----------|--------|--------|")
    else:
        new_lines.append(lines[i] if i < len(lines) else "")

    # Data rows
    i += 1
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].split("|")]
        # split gives ['', cell1, ..., celln, '']
        min_cells = col_count + 2  # data cells + 2 empty edges
        if len(cells) >= min_cells:
            key = cells[2]  # Key column (index 1=Attribute, 2=Key)
            mandatory = "yes" if key in MANDATORY_CORE_KEYS else "\u2014"
            if col_count == 5:
                # Old 5-col: insert Unit=— after Data Type (index 3), then Mandatory
                cells.insert(4, "\u2014")  # Unit
                cells.insert(5, mandatory)  # Mandatory
            else:
                # 6-col: insert Mandatory after Unit (index 4)
                cells.insert(5, mandatory)
            new_lines.append("| " + " | ".join(cells[1:-1]) + " |")
        else:
            new_lines.append(lines[i])
        i += 1

    return i, True


def add_mandatory_column(content: str) -> tuple[str, int]:
    """Add Mandatory column to attribute tables in a schema file.

    Handles both 6-column (with Unit) and 5-column (without Unit) tables.
    Returns (new_content, tables_modified).
    """
    lines = content.split("\n")
    new_lines = []
    tables_modified = 0
    i = 0

    # Pattern for 6-column header (current format with Unit)
    pat6 = re.compile(r"^\|\s*Attribute\s*\|\s*Key\s*\|\s*Data Type\s*\|\s*Unit\s*\|\s*Description\s*\|\s*Example Values\s*\|")
    # Pattern for 5-column header (old format without Unit)
    pat5 = re.compile(r"^\|\s*Attribute\s*\|\s*Key\s*\|\s*Data Type\s*\|\s*Description\s*\|\s*Example Values\s*\|")

    while i < len(lines):
        line = lines[i]

        if "Mandatory" in line and line.strip().startswith("|"):
            new_lines.append(line)
            i += 1
            continue

        if pat6.match(line):
            i, _ = _process_table(lines, i, new_lines, 6)
            tables_modified += 1
            continue

        if pat5.match(line):
            i, _ = _process_table(lines, i, new_lines, 5)
            tables_modified += 1
            continue

        new_lines.append(line)
        i += 1

    return "\n".join(new_lines), tables_modified


def main():
    parser = argparse.ArgumentParser(description="Add Mandatory column to SKU schemas")
    parser.add_argument("--apply", action="store_true", help="Write changes (default: dry-run)")
    args = parser.parse_args()

    schema_files = sorted(SCHEMAS_DIR.glob("*.md"))
    if not schema_files:
        print(f"No schema files found in {SCHEMAS_DIR}", file=sys.stderr)
        sys.exit(1)

    total = 0
    modified = 0
    skipped = 0
    errors = 0

    for path in schema_files:
        total += 1
        content = path.read_text(encoding="utf-8")

        if "| Mandatory |" in content:
            skipped += 1
            continue

        try:
            new_content, tables_count = add_mandatory_column(content)
        except Exception as e:
            print(f"ERROR: {path.name}: {e}", file=sys.stderr)
            errors += 1
            continue

        if tables_count == 0:
            print(f"SKIP: {path.name}: no attribute tables found")
            skipped += 1
            continue

        if args.apply:
            path.write_text(new_content, encoding="utf-8")
            print(f"OK: {path.name} ({tables_count} tables)")
        else:
            print(f"DRY-RUN: {path.name} ({tables_count} tables would be modified)")

        modified += 1

    print(f"\nTotal: {total}, Modified: {modified}, Skipped: {skipped}, Errors: {errors}")
    if not args.apply and modified > 0:
        print("Re-run with --apply to write changes.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
