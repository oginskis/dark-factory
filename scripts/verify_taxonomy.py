# /// script
# requires-python = ">=3.10"
# ///
"""Verify that every subcategory in categories.md has a valid taxonomy ID."""
from __future__ import annotations

import re
import sys
from pathlib import Path

CATEGORIES_FILE = (
    Path(__file__).resolve().parent.parent
    / "docs"
    / "product-taxonomy"
    / "categories.md"
)

# Full line pattern: subcategory name followed by a backtick-enclosed ID
LINE_PATTERN = re.compile(r"^- (.+?) `([a-z][a-z0-9_.]+)`$")

# The ID itself must be exactly category.subcategory (one dot, two segments)
ID_PATTERN = re.compile(r"^[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$")


def main() -> int:
    if not CATEGORIES_FILE.exists():
        print(f"FAIL: categories file not found: {CATEGORIES_FILE}")
        return 1

    text = CATEGORIES_FILE.read_text(encoding="utf-8")
    lines = text.splitlines()

    errors: list[str] = []
    seen_ids: dict[str, int] = {}  # id -> first line number

    for lineno, line in enumerate(lines, start=1):
        if not line.startswith("- "):
            continue

        match = LINE_PATTERN.match(line)
        if not match:
            errors.append(
                f"  line {lineno}: missing or malformed taxonomy ID: {line}"
            )
            continue

        tid = match.group(2)

        if not ID_PATTERN.match(tid):
            errors.append(
                f"  line {lineno}: ID does not match category.subcategory "
                f"dot-notation: `{tid}`"
            )

        if tid in seen_ids:
            errors.append(
                f"  line {lineno}: duplicate ID `{tid}` "
                f"(first seen on line {seen_ids[tid]})"
            )
        else:
            seen_ids[tid] = lineno

    if errors:
        print(f"FAIL: {len(errors)} error(s) in {CATEGORIES_FILE.name}:\n")
        for err in errors:
            print(err)
        return 1

    print(f"PASS: all subcategories have valid taxonomy IDs ({len(seen_ids)} checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
