# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Migration: Add 'Price Includes VAT' row to Core Attributes in all SKU schemas.

Inserts the row after Currency (row 5) as a non-mandatory core attribute.

Usage:
    uv run scripts/migrate_add_price_includes_vat.py              # dry-run
    uv run scripts/migrate_add_price_includes_vat.py --apply      # write changes

Exit codes: 0 = success, 1 = errors encountered
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "docs" / "product-taxonomy" / "sku-schemas"

VAT_ROW = "| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |"


def add_vat_row(content: str) -> tuple[str, bool]:
    """Insert price_includes_vat row after the currency row in Core Attributes.

    Returns (new_content, modified).
    """
    if "price_includes_vat" in content:
        return content, False

    lines = content.split("\n")
    new_lines = []
    inserted = False

    for line in lines:
        new_lines.append(line)
        # Insert after the Currency row (key = currency)
        if not inserted and "| currency |" in line.lower() and line.strip().startswith("|"):
            new_lines.append(VAT_ROW)
            inserted = True

    return "\n".join(new_lines), inserted


def main():
    parser = argparse.ArgumentParser(description="Add price_includes_vat row to SKU schemas")
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

        if "price_includes_vat" in content:
            skipped += 1
            continue

        try:
            new_content, changed = add_vat_row(content)
        except Exception as e:
            print(f"ERROR: {path.name}: {e}", file=sys.stderr)
            errors += 1
            continue

        if not changed:
            print(f"SKIP: {path.name}: no currency row found")
            skipped += 1
            continue

        if args.apply:
            path.write_text(new_content, encoding="utf-8")
            print(f"OK: {path.name}")
        else:
            print(f"DRY-RUN: {path.name}")

        modified += 1

    print(f"\nTotal: {total}, Modified: {modified}, Skipped: {skipped}, Errors: {errors}")
    if not args.apply and modified > 0:
        print("Re-run with --apply to write changes.")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
