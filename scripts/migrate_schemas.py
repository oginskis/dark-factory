# /// script
# requires-python = ">=3.10"
# ///
"""Migrate all SKU schema files from flat format to core/extended format.

For each schema file:
1. Add **Taxonomy ID:** header line
2. Split single ## Attributes table into ## Core Attributes and ## Extended Attributes
3. Remove Brand and deep-spec attributes
4. Add changelog entry for the migration
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = REPO_ROOT / "docs" / "product-taxonomy" / "sku-schemas"
CATEGORIES_FILE = REPO_ROOT / "docs" / "product-taxonomy" / "categories.md"

TODAY = date.today().isoformat()

# ── Classification constants ──

MANDATORY_CORE = ["SKU", "Product Name", "URL", "Price", "Currency"]

ALWAYS_CORE_NAMES = {
    "SKU", "Product Name", "URL", "Price", "Currency",
    "Model Number", "Country of Origin",
}

DROP_NAMES = {
    "Brand", "Brand/Manufacturer",
    "Sound Power Level", "Vibration Level",
    "Product Dimensions", "Package Dimensions",
    "Expiration Date Format", "Best Before Date Format",
    "Container Material", "Capsule Material",
}

IDENTITY_KEYWORDS = ["type", "form", "kind", "class", "category", "grade"]
MATERIAL_KEYWORDS = ["material", "ingredient", "composition"]
DIMENSION_KEYWORDS = [
    "voltage", "size", "capacity", "weight", "count",
    "serving", "length", "diameter", "thread",
]


def slugify(name: str) -> str:
    """Slugify a taxonomy display name to match schema filenames."""
    s = name.lower()
    # Remove apostrophes before slugifying so "Men's" -> "mens" not "men-s"
    s = s.replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s


def build_taxonomy_map() -> dict[str, str]:
    """Build mapping from schema filename slug to taxonomy ID."""
    text = CATEGORIES_FILE.read_text(encoding="utf-8")
    slug_to_id: dict[str, str] = {}
    for line in text.splitlines():
        if not line.startswith("- "):
            continue
        match = re.match(r"- (.+?) `([a-z][a-z0-9_.]+)`", line)
        if match:
            display_name = match.group(1).strip()
            tax_id = match.group(2)
            slug = slugify(display_name)
            slug_to_id[slug] = tax_id
    return slug_to_id


def parse_table_rows(lines: list[str], start: int) -> tuple[list[list[str]], int]:
    """Parse a markdown table starting at `start`.

    Returns (data_rows_as_raw_lines, end_index).
    Each data_row is the list of cell values.
    """
    i = start
    # Skip to header row
    while i < len(lines) and not lines[i].strip().startswith("|"):
        i += 1
    if i >= len(lines):
        return [], i

    # Skip header row
    i += 1
    # Skip separator row
    if i < len(lines) and re.match(r"\s*\|[-| ]+\|\s*$", lines[i]):
        i += 1

    data_rows: list[list[str]] = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        data_rows.append(cells)
        i += 1

    return data_rows, i


def classify_attribute(name: str) -> str:
    """Classify an attribute as 'core', 'extended', or 'drop'."""
    if name in DROP_NAMES:
        return "drop"
    if name in ALWAYS_CORE_NAMES:
        return "core"

    name_lower = name.lower()

    for kw in IDENTITY_KEYWORDS:
        if kw in name_lower:
            return "core"
    for kw in MATERIAL_KEYWORDS:
        if kw in name_lower:
            return "core"
    for kw in DIMENSION_KEYWORDS:
        if kw in name_lower:
            return "dimension_candidate"

    return "extended"


def split_attributes(
    rows: list[list[str]],
) -> tuple[list[list[str]], list[list[str]]]:
    """Split attribute rows into core and extended lists.

    Returns (core_rows, extended_rows).
    """
    core: list[list[str]] = []
    extended: list[list[str]] = []
    dimension_candidates: list[list[str]] = []

    for row in rows:
        if not row:
            continue
        attr_name = row[0]
        classification = classify_attribute(attr_name)

        if classification == "drop":
            continue
        elif classification == "core":
            core.append(row)
        elif classification == "dimension_candidate":
            dimension_candidates.append(row)
        else:
            extended.append(row)

    # For dimension candidates: pick the most important one for core, rest to extended
    # The most important is the first one (they appear in priority order in the schema)
    if dimension_candidates:
        # Count how many non-mandatory core we already have
        non_mandatory_core = len([r for r in core if r[0] not in MANDATORY_CORE])
        if non_mandatory_core < 5:
            # We have room — add the first dimension candidate to core
            core.append(dimension_candidates[0])
            extended.extend(dimension_candidates[1:])
        else:
            # Already enough core, all dimension candidates go to extended
            extended.extend(dimension_candidates)

    # Enforce core ordering: mandatory 5 first, then others
    mandatory_rows = []
    other_core_rows = []
    for row in core:
        if row[0] in MANDATORY_CORE:
            mandatory_rows.append(row)
        else:
            other_core_rows.append(row)

    # Sort mandatory in the canonical order
    mandatory_order = {name: i for i, name in enumerate(MANDATORY_CORE)}
    mandatory_rows.sort(key=lambda r: mandatory_order.get(r[0], 99))

    core = mandatory_rows + other_core_rows

    # If core has more than 10, demote least important to extended
    while len(core) > 10:
        # Demote the last non-mandatory core attribute
        demoted = core.pop()
        extended.insert(0, demoted)

    # If extended has more than 15, drop the least important (from the end)
    while len(extended) > 15:
        extended.pop()

    # If total < 15, that's OK — we don't add artificial attributes
    # But if dropping brought total below 15, we should have kept more extended
    # We already handle this by only dropping when > 15

    return core, extended


def format_table(header: str, rows: list[list[str]]) -> str:
    """Format a markdown table section."""
    lines = [
        f"## {header}",
        "",
        "| Attribute | Data Type | Description | Example Values |",
        "|-----------|-----------|-------------|----------------|",
    ]
    for row in rows:
        # Ensure exactly 4 cells
        while len(row) < 4:
            row.append("")
        cells = " | ".join(row[:4])
        lines.append(f"| {cells} |")
    return "\n".join(lines)


def migrate_file(filepath: Path, taxonomy_id: str) -> tuple[bool, str]:
    """Migrate a single schema file. Returns (success, message)."""
    text = filepath.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Check if already migrated
    if any(line.strip() == "## Core Attributes" for line in lines):
        return True, "already migrated"

    # Find the ## Attributes section
    attr_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Attributes":
            attr_idx = i
            break

    if attr_idx is None:
        return False, "no ## Attributes section found"

    # Find the ## Changelog section
    changelog_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## Changelog":
            changelog_idx = i
            break

    if changelog_idx is None:
        return False, "no ## Changelog section found"

    # Parse the attributes table
    attr_rows, _ = parse_table_rows(lines, attr_idx + 1)
    if not attr_rows:
        return False, "no attribute rows found"

    # Split into core and extended
    core_rows, extended_rows = split_attributes(attr_rows)

    # Build the new header: add Taxonomy ID after Parent category
    new_header_lines = []
    inserted_taxonomy = False
    for i, line in enumerate(lines):
        if line.strip() == "## Attributes":
            break
        if line.startswith("**Parent category:**") and not inserted_taxonomy:
            new_header_lines.append(line)
            new_header_lines.append(f"**Taxonomy ID:** `{taxonomy_id}`")
            inserted_taxonomy = True
        else:
            new_header_lines.append(line)

    if not inserted_taxonomy:
        # Fallback: add taxonomy ID before ## Attributes
        new_header_lines.append(f"**Taxonomy ID:** `{taxonomy_id}`")

    # Build the core and extended tables
    core_table = format_table("Core Attributes", core_rows)
    extended_table = format_table("Extended Attributes", extended_rows)

    # Build the changelog section with new entry
    changelog_lines = []
    changelog_table_started = False
    changelog_header_seen = False
    changelog_data_rows: list[str] = []
    for i in range(changelog_idx, len(lines)):
        line = lines[i]
        if line.strip() == "## Changelog":
            changelog_lines.append(line)
            changelog_lines.append("")  # blank line after heading
            continue
        # Check separator BEFORE header — both start with "|"
        if (
            re.match(r"\s*\|[-| ]+\|\s*$", line)
            and not changelog_table_started
            and changelog_header_seen
        ):
            changelog_lines.append(line)
            changelog_table_started = True
            # Add migration entry as first data row
            changelog_lines.append(
                f"| {TODAY} | Migrated to core/extended format | Migration script |"
            )
            continue
        if line.strip().startswith("|") and not changelog_table_started:
            # Header row
            changelog_lines.append(line)
            changelog_header_seen = True
            continue
        if changelog_table_started:
            changelog_lines.append(line)

    # Assemble the final file
    parts = [
        "\n".join(new_header_lines),
        "",
        core_table,
        "",
        extended_table,
        "",
        "\n".join(changelog_lines),
        "",  # trailing newline
    ]

    new_text = "\n".join(parts)

    filepath.write_text(new_text, encoding="utf-8")

    return True, f"core={len(core_rows)}, extended={len(extended_rows)}"


def main() -> int:
    slug_to_id = build_taxonomy_map()
    print(f"Loaded {len(slug_to_id)} taxonomy entries")

    schema_files = sorted(SCHEMAS_DIR.glob("*.md"))
    print(f"Found {len(schema_files)} schema files")

    success_count = 0
    fail_count = 0
    skip_count = 0

    for filepath in schema_files:
        slug = filepath.stem
        taxonomy_id = slug_to_id.get(slug)

        if taxonomy_id is None:
            print(f"FAIL: {filepath.name} — no taxonomy ID found for slug '{slug}'")
            fail_count += 1
            continue

        ok, msg = migrate_file(filepath, taxonomy_id)
        if ok:
            if "already migrated" in msg:
                skip_count += 1
                print(f"SKIP: {filepath.name} — {msg}")
            else:
                success_count += 1
                print(f"OK:   {filepath.name} — {msg}")
        else:
            fail_count += 1
            print(f"FAIL: {filepath.name} — {msg}")

    print(f"\nResults: {success_count} migrated, {skip_count} skipped, {fail_count} failed")
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
