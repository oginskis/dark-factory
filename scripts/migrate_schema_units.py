# /// script
# requires-python = ">=3.10"
# ///
"""Migrate SKU schema files: extract units from Data Type into a new Unit column.

For each schema file:
1. Parse Core Attributes and Extended Attributes tables
2. Extract unit from Data Type parentheses (e.g., 'number (mm)' → Data Type: 'number', Unit: 'mm')
3. Preserve 'text (list)' as a type qualifier, not a unit
4. Add Unit column after Data Type
5. Rewrite the file
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent.parent / "docs" / "product-taxonomy" / "sku-schemas"

# Regex to extract unit from Data Type like "number (mm)" or "text (deg C)"
# Must NOT match "text (list)" — that's a type qualifier
UNIT_RE = re.compile(r"^(text|number)\s+\((?!list\b)(.+?)\)$")


def extract_unit(data_type: str) -> tuple[str, str]:
    """Extract unit from data type string. Returns (clean_type, unit)."""
    data_type = data_type.strip()
    match = UNIT_RE.match(data_type)
    if match:
        return match.group(1), match.group(2)
    # No unit — return as-is with em dash
    return data_type, "\u2014"


def parse_table_row(line: str) -> list[str]:
    """Parse a markdown table row into cells."""
    cells = line.strip().strip("|").split("|")
    return [c.strip() for c in cells]


def format_table_row(cells: list[str]) -> str:
    """Format cells back into a markdown table row."""
    return "| " + " | ".join(cells) + " |"


def make_separator(col_count: int) -> str:
    """Create a markdown table separator row."""
    return "|" + "|".join(["--------"] * col_count) + "|"


def migrate_table(lines: list[str], start_idx: int) -> tuple[list[str], int]:
    """Migrate a single attributes table starting at start_idx.

    Returns (new_lines, end_idx) where end_idx is the line after the table.
    """
    # Find header row (first row with pipes)
    header_idx = start_idx
    while header_idx < len(lines) and "|" not in lines[header_idx]:
        header_idx += 1

    if header_idx >= len(lines):
        return lines[start_idx:], len(lines)

    header_cells = parse_table_row(lines[header_idx])

    # Verify this is an attributes table with Data Type column
    if "Data Type" not in header_cells:
        # Not an attributes table, skip
        end = header_idx + 1
        while end < len(lines) and "|" in lines[end]:
            end += 1
        return lines[start_idx:end], end

    dt_idx = header_cells.index("Data Type")

    # Insert Unit column after Data Type
    new_header = header_cells[:dt_idx + 1] + ["Unit"] + header_cells[dt_idx + 1:]

    # Skip separator row
    sep_idx = header_idx + 1

    # Process data rows
    new_lines = []
    new_lines.append(format_table_row(new_header))
    new_lines.append(make_separator(len(new_header)))

    row_idx = sep_idx + 1
    while row_idx < len(lines) and "|" in lines[row_idx]:
        cells = parse_table_row(lines[row_idx])
        if len(cells) >= len(header_cells):
            clean_type, unit = extract_unit(cells[dt_idx])
            cells[dt_idx] = clean_type
            new_cells = cells[:dt_idx + 1] + [unit] + cells[dt_idx + 1:]
            new_lines.append(format_table_row(new_cells))
        row_idx += 1

    # Include any pre-table lines (like the ## heading)
    prefix = lines[start_idx:header_idx]
    return prefix + new_lines, row_idx


def migrate_file(filepath: Path) -> bool:
    """Migrate a single schema file. Returns True if changed."""
    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    new_lines: list[str] = []
    i = 0
    changed = False

    while i < len(lines):
        line = lines[i]

        # Detect attributes table sections
        if line.strip().startswith("## Core Attributes") or line.strip().startswith("## Extended Attributes"):
            table_lines, end_i = migrate_table(lines, i)

            # Check if we actually added a Unit column
            for tl in table_lines:
                if "| Unit |" in tl:
                    changed = True
                    break

            new_lines.extend(table_lines)
            i = end_i
        else:
            new_lines.append(line)
            i += 1

    if changed:
        filepath.write_text("\n".join(new_lines), encoding="utf-8")

    return changed


def main() -> None:
    schema_files = sorted(SCHEMAS_DIR.glob("*.md"))
    print(f"Found {len(schema_files)} schema files")

    migrated = 0
    skipped = 0
    errors = 0

    for filepath in schema_files:
        try:
            if migrate_file(filepath):
                migrated += 1
                print(f"  \u2713 {filepath.name}")
            else:
                skipped += 1
        except Exception as e:
            errors += 1
            print(f"  \u2717 {filepath.name}: {e}", file=sys.stderr)

    print(f"\nDone: {migrated} migrated, {skipped} unchanged, {errors} errors")


if __name__ == "__main__":
    main()
