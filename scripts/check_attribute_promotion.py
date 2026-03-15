# /// script
# requires-python = ">=3.10"
# ///
"""Check which extended attributes are candidates for promotion to core.

Scans scraper output across all companies in a subcategory and reports:
- Extended attributes appearing in 3+ companies -> candidates for core promotion
- Extra attributes appearing in 3+ companies -> candidates for addition to extended
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CATEGORIES_FILE = REPO_ROOT / "docs" / "product-taxonomy" / "categories.md"
SCHEMAS_DIR = REPO_ROOT / "docs" / "product-taxonomy" / "sku-schemas"
SCRAPER_DIR = REPO_ROOT / "docs" / "scraper-generator"

PROMOTION_THRESHOLD = 3


def load_taxonomy_map() -> dict[str, str]:
    """Build a mapping from taxonomy ID to the display name (subcategory part).

    E.g. ``machinery.power_tools`` -> ``Power Tools (Drills, Saws, Sanders)``.
    """
    if not CATEGORIES_FILE.exists():
        return {}

    tid_to_name: dict[str, str] = {}
    for line in CATEGORIES_FILE.read_text(encoding="utf-8").splitlines():
        if not line.startswith("- "):
            continue
        match = re.match(r"^- (.+?) `([a-z][a-z0-9_.]+)`$", line)
        if match:
            tid_to_name[match.group(2)] = match.group(1)
    return tid_to_name


def taxonomy_id_for_category(category: str, tid_to_name: dict[str, str]) -> str | None:
    """Given a config category string, return the matching taxonomy ID.

    Config ``category`` is formatted as ``"Parent > Subcategory Name"`` — we
    match the subcategory portion against the display names from categories.md.
    """
    # Extract the subcategory part (after ">")
    parts = category.split(">")
    subcat_name = parts[-1].strip() if parts else category.strip()

    for tid, name in tid_to_name.items():
        if name == subcat_name:
            return tid
    return None


def schema_slug_for_taxonomy_id(taxonomy_id: str, tid_to_name: dict[str, str]) -> str | None:
    """Derive the SKU schema slug from a taxonomy ID.

    The slug is the kebab-case version of the subcategory display name.  For
    example ``Power Tools (Drills, Saws, Sanders)`` becomes
    ``power-tools-drills-saws-sanders``.
    """
    name = tid_to_name.get(taxonomy_id)
    if name is None:
        return None

    # Remove parenthetical qualifiers' parens/commas, lowercase, replace
    # spaces and special chars with hyphens, collapse multiple hyphens.
    slug = name.lower()
    slug = slug.replace("(", "").replace(")", "").replace(",", "")
    slug = slug.replace("&", "").replace("/", " ")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    # Collapse runs of hyphens
    slug = re.sub(r"-+", "-", slug)
    return slug


def parse_schema_attributes(schema_path: Path) -> tuple[set[str], set[str]]:
    """Parse core and extended attribute names from a SKU schema markdown file.

    Returns ``(core_attrs, extended_attrs)`` where each element is a set of
    snake_case attribute names derived from the Attribute column.
    """
    if not schema_path.exists():
        return set(), set()

    text = schema_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    def to_snake(name: str) -> str:
        s = name.strip().lower()
        s = s.replace("(", "").replace(")", "").replace(",", "")
        s = s.replace("/", " ").replace("&", " ")
        s = re.sub(r"[^a-z0-9]+", "_", s)
        s = s.strip("_")
        s = re.sub(r"_+", "_", s)
        return s

    def extract_table_attrs(start_idx: int) -> set[str]:
        """Extract attribute names from the markdown table following start_idx."""
        attrs: set[str] = set()
        i = start_idx
        # Find the header row (first line starting with |)
        while i < len(lines) and not lines[i].strip().startswith("|"):
            i += 1
        if i >= len(lines):
            return attrs
        # Skip header row
        i += 1
        # Skip separator row
        if i < len(lines) and re.match(r"\s*\|[-| ]+\|\s*$", lines[i]):
            i += 1
        # Data rows
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if cells:
                attrs.add(to_snake(cells[0]))
            i += 1
        return attrs

    core_attrs: set[str] = set()
    extended_attrs: set[str] = set()

    for i, line in enumerate(lines):
        if line.strip() == "## Core Attributes":
            core_attrs = extract_table_attrs(i + 1)
        elif line.strip() == "## Extended Attributes":
            extended_attrs = extract_table_attrs(i + 1)

    return core_attrs, extended_attrs


def find_matching_companies(
    taxonomy_id: str, tid_to_name: dict[str, str]
) -> list[tuple[str, Path]]:
    """Find all companies whose config.json matches the given taxonomy ID.

    Returns a list of ``(company_slug, config_path)`` tuples.
    """
    if not SCRAPER_DIR.exists():
        return []

    matches: list[tuple[str, Path]] = []
    for config_path in sorted(SCRAPER_DIR.glob("*/config.json")):
        try:
            config = json.loads(config_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue

        # Check the category field
        category = config.get("category", "")
        config_tid = taxonomy_id_for_category(category, tid_to_name)
        if config_tid == taxonomy_id:
            slug = config.get("company_slug", config_path.parent.name)
            matches.append((slug, config_path))
            continue

        # Check a subcategories list if present
        subcategories = config.get("subcategories", [])
        if isinstance(subcategories, list):
            for subcat in subcategories:
                subcat_tid = taxonomy_id_for_category(str(subcat), tid_to_name)
                if subcat_tid == taxonomy_id:
                    slug = config.get("company_slug", config_path.parent.name)
                    matches.append((slug, config_path))
                    break

    return matches


def collect_attributes(
    products_path: Path,
    core_schema_attrs: set[str],
    extended_schema_attrs: set[str],
) -> tuple[set[str], set[str], set[str]]:
    """Read a products.jsonl file and return the sets of attribute keys found.

    Returns ``(core_found, extended_found, extra_found)`` where each is the
    set of attribute names that appear at least once in the output.

    Handles both v1 (flat ``attributes``) and v2 (three-bucket) formats.
    """
    core_found: set[str] = set()
    extended_found: set[str] = set()
    extra_found: set[str] = set()

    all_schema_attrs = core_schema_attrs | extended_schema_attrs

    if not products_path.exists():
        return core_found, extended_found, extra_found

    for line in products_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            continue

        fmt = record.get("_format")
        if fmt == 2:
            # v2 three-bucket format
            for key in record.get("core_attributes", {}):
                core_found.add(key)
            for key in record.get("extended_attributes", {}):
                extended_found.add(key)
            for key in record.get("extra_attributes", {}):
                extra_found.add(key)
        else:
            # v1 flat attributes — classify by schema membership
            attrs = record.get("attributes", {})
            if not isinstance(attrs, dict):
                continue
            for key in attrs:
                if key in core_schema_attrs:
                    core_found.add(key)
                elif key in extended_schema_attrs:
                    extended_found.add(key)
                else:
                    extra_found.add(key)

    return core_found, extended_found, extra_found


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check which extended attributes are candidates for promotion "
            "to core across all companies in a subcategory."
        ),
    )
    parser.add_argument(
        "taxonomy_id",
        help="Taxonomy ID (e.g. machinery.power_tools)",
    )
    args = parser.parse_args()

    taxonomy_id: str = args.taxonomy_id

    # ------------------------------------------------------------------
    # 1. Load taxonomy mappings
    # ------------------------------------------------------------------
    tid_to_name = load_taxonomy_map()
    if not tid_to_name:
        print(f"WARNING: could not load taxonomy from {CATEGORIES_FILE}")

    if taxonomy_id not in tid_to_name:
        print(f"ERROR: taxonomy ID '{taxonomy_id}' not found in categories.md")
        return 0  # advisory — always exit 0

    # ------------------------------------------------------------------
    # 2. Load SKU schema (core vs extended attribute names)
    # ------------------------------------------------------------------
    schema_slug = schema_slug_for_taxonomy_id(taxonomy_id, tid_to_name)
    schema_path: Path | None = None
    core_schema_attrs: set[str] = set()
    extended_schema_attrs: set[str] = set()

    if schema_slug:
        schema_path = SCHEMAS_DIR / f"{schema_slug}.md"
        core_schema_attrs, extended_schema_attrs = parse_schema_attributes(schema_path)

    if not core_schema_attrs and not extended_schema_attrs:
        # Try to find the schema via the sku_schema field in any matching config
        companies = find_matching_companies(taxonomy_id, tid_to_name)
        for _, config_path in companies:
            try:
                config = json.loads(config_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, OSError):
                continue
            alt_slug = config.get("sku_schema")
            if alt_slug:
                alt_path = SCHEMAS_DIR / f"{alt_slug}.md"
                core_schema_attrs, extended_schema_attrs = parse_schema_attributes(alt_path)
                if core_schema_attrs or extended_schema_attrs:
                    schema_path = alt_path
                    break

    if not core_schema_attrs and not extended_schema_attrs:
        print(f"WARNING: no SKU schema found for {taxonomy_id}")
        print("Cannot determine core vs extended attributes without a schema.")
        return 0

    # ------------------------------------------------------------------
    # 3. Find matching companies
    # ------------------------------------------------------------------
    companies = find_matching_companies(taxonomy_id, tid_to_name)

    # ------------------------------------------------------------------
    # 4. Collect per-company attribute sets
    # ------------------------------------------------------------------
    # Maps: attribute_name -> set of company slugs that have it
    extended_by_company: dict[str, set[str]] = defaultdict(set)
    extra_by_company: dict[str, set[str]] = defaultdict(set)

    companies_with_output: list[str] = []

    for slug, config_path in companies:
        products_path = config_path.parent / "output" / "products.jsonl"
        if not products_path.exists():
            continue

        core_found, extended_found, extra_found = collect_attributes(
            products_path, core_schema_attrs, extended_schema_attrs
        )

        if not core_found and not extended_found and not extra_found:
            continue

        companies_with_output.append(slug)

        for attr in extended_found:
            extended_by_company[attr].add(slug)
        for attr in extra_found:
            extra_by_company[attr].add(slug)

    # ------------------------------------------------------------------
    # 5. Report
    # ------------------------------------------------------------------
    subcat_name = tid_to_name.get(taxonomy_id, taxonomy_id)
    total_companies = len(companies)
    total_with_output = len(companies_with_output)
    all_slugs = [slug for slug, _ in companies]

    print(f"Subcategory: {taxonomy_id}")
    print(f"Companies found: {total_companies} ({', '.join(all_slugs) if all_slugs else 'none'})")
    if total_with_output < total_companies:
        missing = [
            slug for slug, cp in companies
            if not (cp.parent / "output" / "products.jsonl").exists()
        ]
        if missing:
            print(f"Companies without output: {', '.join(missing)}")
    print()

    # Extended -> Core candidates
    ext_candidates = {
        attr: slugs
        for attr, slugs in sorted(extended_by_company.items())
        if len(slugs) >= PROMOTION_THRESHOLD
    }
    ext_below = {
        attr: slugs
        for attr, slugs in sorted(extended_by_company.items())
        if len(slugs) < PROMOTION_THRESHOLD and len(slugs) > 0
    }

    print(f"=== Extended -> Core promotion candidates ({PROMOTION_THRESHOLD}+ companies) ===")
    if ext_candidates:
        for attr, slugs in sorted(ext_candidates.items(), key=lambda x: -len(x[1])):
            print(f"  {attr}: {len(slugs)}/{total_with_output} companies (currently extended)")
    else:
        print("  No candidates found.")
    print()

    # Extra -> Extended candidates
    extra_candidates = {
        attr: slugs
        for attr, slugs in sorted(extra_by_company.items())
        if len(slugs) >= PROMOTION_THRESHOLD
    }
    extra_below = {
        attr: slugs
        for attr, slugs in sorted(extra_by_company.items())
        if len(slugs) < PROMOTION_THRESHOLD and len(slugs) > 0
    }

    print(f"=== Extra -> Extended addition candidates ({PROMOTION_THRESHOLD}+ companies) ===")
    if extra_candidates:
        for attr, slugs in sorted(extra_candidates.items(), key=lambda x: -len(x[1])):
            print(f"  {attr}: {len(slugs)}/{total_with_output} companies (not in schema)")
    if extra_below:
        for attr, slugs in sorted(extra_below.items(), key=lambda x: -len(x[1])):
            print(
                f"  {attr}: {len(slugs)}/{total_with_output} companies "
                f"(not in schema) -- below threshold"
            )
    if not extra_candidates and not extra_below:
        print("  No candidates found.")
    print()

    if not ext_candidates and not extra_candidates:
        print("No candidates found for promotion.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
