#!/usr/bin/env python3
"""
Pre-process SKU schemas into attribute routing tables for the scraper-generator.

Reads SKU schema markdown files and extracts attribute keys, data types, and
enum values. Outputs a compact JSON file that the LLM orchestrator reads instead
of parsing raw schema files.

Usage:
    python prepare_generator_input.py \
        --schemas wood.softwood_hardwood_lumber wood.flooring_decking \
        --output docs/scraper-generator/{slug}/generator_input.json
"""

import argparse
import json
import re
import sys
from pathlib import Path


def find_repo_root() -> Path:
    """Walk up from script location to find repo root."""
    path = Path(__file__).resolve().parent
    for _ in range(10):
        if (path / ".claude" / "skills").is_dir():
            return path
        path = path.parent
    raise RuntimeError("Cannot find repo root")


REPO_ROOT = find_repo_root()
TAXONOMY_FILE = REPO_ROOT / "docs" / "product-taxonomy" / "categories.md"
SCHEMAS_DIR = REPO_ROOT / "docs" / "product-taxonomy" / "sku-schemas"

# Universal fields handled by the eval script — exclude from routing tables
UNIVERSAL_KEYS = {
    "sku", "product_name", "name", "url", "price", "currency",
    "brand", "product_category", "scraped_at", "category_path",
}

# SKU schema Data Type → eval type mapping
TYPE_MAP = {
    "text": "str",
    "enum": "str",
    "number": "number",
    "text (list)": "list",
    "boolean": "bool",
}


def slugify_display_name(display_name: str) -> str:
    """Convert taxonomy display name to schema filename slug."""
    slug = display_name.lower()
    for char in "&/(),":
        slug = slug.replace(char, "")
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug


def find_schema_file(taxonomy_id: str) -> Path | None:
    """Find the schema file for a taxonomy ID by looking up the display name."""
    # Read categories.md to find the display name
    categories_text = TAXONOMY_FILE.read_text(encoding="utf-8")
    pattern = rf"^- (.+?) `{re.escape(taxonomy_id)}`$"
    match = re.search(pattern, categories_text, re.MULTILINE)
    if not match:
        return None
    display_name = match.group(1).strip()
    slug = slugify_display_name(display_name)
    schema_path = SCHEMAS_DIR / f"{slug}.md"
    if schema_path.exists():
        return schema_path
    # Fallback: search directory for partial match
    for f in SCHEMAS_DIR.glob("*.md"):
        if slug in f.stem or f.stem in slug:
            return f
    return None


def parse_schema_table(content: str, section_name: str) -> list[dict]:
    """Parse a markdown table under a ## section into a list of dicts."""
    # Find the section
    pattern = rf"^## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, content, re.MULTILINE | re.DOTALL)
    if not match:
        return []

    section = match.group(1)
    lines = [l.strip() for l in section.split("\n") if l.strip().startswith("|")]
    if len(lines) < 3:
        return []

    # Parse header
    headers = [h.strip() for h in lines[0].split("|")[1:-1]]
    # Skip separator line (lines[1])
    # Parse data rows
    rows = []
    for line in lines[2:]:
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) >= len(headers):
            row = dict(zip(headers, cells))
            rows.append(row)
    return rows


def extract_routing_table(schema_path: Path) -> dict:
    """Extract core/extended attribute keys, types, and units from a schema file."""
    content = schema_path.read_text(encoding="utf-8")

    core_rows = parse_schema_table(content, "Core Attributes")
    extended_rows = parse_schema_table(content, "Extended Attributes")

    core_keys = []
    extended_keys = []
    types = {}
    units = {}

    for row in core_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        unit = row.get("Unit", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            core_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")
            if unit and unit not in ("—", "-"):
                units[key] = unit

    for row in extended_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        unit = row.get("Unit", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            extended_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")
            if unit and unit not in ("—", "-"):
                units[key] = unit

    return {
        "core": core_keys,
        "extended": extended_keys,
        "types": types,
        "units": units,
    }


def main():
    parser = argparse.ArgumentParser(description="Pre-process SKU schemas for scraper generation")
    parser.add_argument("--schemas", nargs="+", required=True, help="Taxonomy IDs to process")
    parser.add_argument("--output", required=True, help="Output JSON path")
    args = parser.parse_args()

    routing_tables = {}
    errors = []

    for taxonomy_id in args.schemas:
        schema_path = find_schema_file(taxonomy_id)
        if schema_path is None:
            errors.append(f"No schema file found for {taxonomy_id}")
            continue
        routing_tables[taxonomy_id] = extract_routing_table(schema_path)

    if errors:
        for error in errors:
            print(f"WARNING: {error}", file=sys.stderr)

    output = {"routing_tables": routing_tables}
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2))
    print(f"Wrote routing tables for {len(routing_tables)} schemas to {args.output}")


if __name__ == "__main__":
    main()
