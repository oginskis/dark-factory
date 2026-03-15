# Taxonomy Enforcement & Schema Tiering Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enforce consistent attribute naming across scrapers by tiering SKU schemas into core/extended, adding taxonomy IDs, and restructuring the product record format for cross-company search.

**Architecture:** Four sequential phases: (1) taxonomy IDs + verification tooling, (2) schema format migration, (3) agent/skill updates for new format, (4) eval updates. Each phase produces a working commit. Phases 1-2 are data/format changes with no behavior change. Phases 3-4 change pipeline behavior.

**Tech Stack:** Python 3.10+, markdown files (agent specs, skill wrappers, schemas), `uv run` for script execution. No new dependencies.

**Spec:** `docs/superpowers/specs/2026-03-15-taxonomy-enforcement-design.md`

---

## Phase 1: Taxonomy IDs & Verification

Add dot-notation IDs to `categories.md` and build the verification script.

### Task 1: Create taxonomy ID verification script

**Files:**
- Create: `scripts/verify_taxonomy.py`

- [ ] **Step 1: Write the verification script**

The script reads `categories.md`, extracts all subcategory lines, and validates:
- Every subcategory line has exactly one backtick-enclosed ID
- No duplicate IDs across all subcategories
- IDs match the `[a-z][a-z0-9_.]+` pattern
- Each ID has the format `{category_short}.{subcategory_short}`

```python
# /// script
# requires-python = ">=3.10"
# ///
"""Verify taxonomy IDs in categories.md are valid and unique."""
from __future__ import annotations

import re
import sys
from pathlib import Path

CATEGORIES_PATH = Path(__file__).resolve().parent.parent / "docs" / "product-taxonomy" / "categories.md"
ID_PATTERN = re.compile(r"^- (.+?) `([a-z][a-z0-9_.]+)`$")
ID_FORMAT = re.compile(r"^[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*$")


def verify() -> list[str]:
    errors: list[str] = []
    text = CATEGORIES_PATH.read_text()
    ids_seen: dict[str, int] = {}
    current_category = ""
    line_num = 0

    for line in text.splitlines():
        line_num += 1
        stripped = line.strip()

        if stripped.startswith("## "):
            current_category = stripped[3:].strip()
            continue

        if not stripped.startswith("- "):
            continue

        # This is a subcategory line
        match = ID_PATTERN.match(stripped)
        if not match:
            errors.append(f"Line {line_num}: Missing taxonomy ID: {stripped}")
            continue

        display_name = match.group(1)
        taxonomy_id = match.group(2)

        if not ID_FORMAT.match(taxonomy_id):
            errors.append(f"Line {line_num}: ID '{taxonomy_id}' does not match category.subcategory format")

        if taxonomy_id in ids_seen:
            errors.append(f"Line {line_num}: Duplicate ID '{taxonomy_id}' (first seen at line {ids_seen[taxonomy_id]})")
        else:
            ids_seen[taxonomy_id] = line_num

    return errors


def main() -> None:
    errors = verify()
    if errors:
        print(f"FAIL: {len(errors)} error(s) found:\n")
        for e in errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print(f"PASS: All taxonomy IDs valid and unique.")
        sys.exit(0)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Run the script — expect FAIL (no IDs exist yet)**

Run: `uv run scripts/verify_taxonomy.py`
Expected: FAIL with 237 "Missing taxonomy ID" errors (one per subcategory)

- [ ] **Step 3: Commit**

```bash
git add scripts/verify_taxonomy.py
git commit -m "feat: add taxonomy ID verification script"
```

### Task 2: Assign taxonomy IDs to all subcategories

**Files:**
- Modify: `docs/product-taxonomy/categories.md`

- [ ] **Step 1: Write a script to auto-assign IDs**

Create a one-time migration script that reads `categories.md`, generates IDs from category and subcategory names, and writes the updated file. The ID generation logic:

```python
def generate_id(category: str, subcategory: str) -> str:
    """Generate dot-notation ID from category and subcategory names."""
    def slugify(name: str) -> str:
        s = name.lower()
        # Remove parenthesized content
        s = re.sub(r'\([^)]*\)', '', s)
        # Remove special chars
        for ch in '&/,':
            s = s.replace(ch, '')
        s = re.sub(r'\s+', '_', s.strip())
        s = re.sub(r'_+', '_', s)
        return s.strip('_')

    cat_short = slugify(category)
    # Abbreviate long category names
    CATEGORY_ABBREVS = {
        "food_beverage_products": "food",
        "agricultural_products_livestock_equipment": "agriculture",
        "apparel_footwear_accessories": "apparel",
        "textiles_fabrics_leather": "textiles",
        "electronics_electrical_equipment": "electronics",
        "household_appliances": "appliances",
        "machinery_industrial_equipment": "machinery",
        "energy_equipment_storage": "energy",
        "automotive_vehicles": "automotive",
        "chemicals_chemical_products": "chemicals",
        "pharmaceuticals_medical_devices": "pharma",
        "metals_metal_products": "metals",
        "minerals_ores_raw_materials": "minerals",
        "plastics_rubber_products": "plastics",
        "construction_materials_glass_ceramics": "construction",
        "wood_products_lumber": "wood",
        "paper_pulp_printed_products": "paper",
        "packaging_materials": "packaging",
        "furniture_home_furnishings": "furniture",
        "kitchenware_tableware_housewares": "kitchen",
        "consumer_goods_personal_care_household": "consumer",
        "petroleum_coal_products": "petroleum",
        "jewelry_watches_accessories": "jewelry",
        "sporting_goods_toys_recreation": "sports",
        "firearms_ammunition": "firearms",
        "safety_personal_protective_equipment": "safety",
    }
    cat_key = cat_short
    cat_id = CATEGORY_ABBREVS.get(cat_key, cat_short[:12])

    sub_short = slugify(subcategory)
    # Truncate very long subcategory slugs
    if len(sub_short) > 30:
        sub_short = sub_short[:30].rstrip('_')

    return f"{cat_id}.{sub_short}"
```

The script reads the current `categories.md`, adds IDs to each subcategory line, and writes back.

- [ ] **Step 2: Run the migration script**

Run: `uv run scripts/assign_taxonomy_ids.py`
Expected: `categories.md` updated with 237 IDs

- [ ] **Step 3: Run the verification script — expect PASS**

Run: `uv run scripts/verify_taxonomy.py`
Expected: PASS

- [ ] **Step 4: Review the generated IDs manually**

Spot-check a sample of IDs to ensure they're readable and logical:
- `machinery.power_tools` for "Power Tools (Drills, Saws, Sanders)"
- `energy.ev_charging` for "Electric Vehicle Charging Equipment"
- `safety.head_protection` for "Head Protection (Hard Hats, Helmets)"

Fix any that don't read well. Re-run verification.

- [ ] **Step 5: Commit**

```bash
git add docs/product-taxonomy/categories.md scripts/assign_taxonomy_ids.py
git commit -m "feat: assign taxonomy IDs to all 237 subcategories"
```

---

## Phase 2: Schema Format Migration

Migrate all 237 SKU schemas from the flat single-table format to the new Core/Extended two-table format.

### Task 3: Create schema format verification script

**Files:**
- Create: `scripts/verify_schemas.py`

- [ ] **Step 1: Write the schema verification script**

Validates each schema file against the new format rules:
- Has `## Core Attributes` and `## Extended Attributes` sections
- Has `**Taxonomy ID:**` header matching an ID in `categories.md`
- Core count: 5-10 attributes
- Extended count: 10-15 attributes
- Total: 15-30 attributes
- No backticks in table cells
- No duplicate attribute names across core and extended
- Table has exactly 4 columns

The script takes an optional `--file` argument to verify a single schema, or verifies all schemas when run without arguments.

- [ ] **Step 2: Run — expect FAIL (schemas still in old format)**

Run: `uv run scripts/verify_schemas.py`
Expected: FAIL for all 237 schemas

- [ ] **Step 3: Commit**

```bash
git add scripts/verify_schemas.py
git commit -m "feat: add schema format verification script"
```

### Task 4: Update product-taxonomy skill for new format

**Files:**
- Modify: `.claude/skills/product-taxonomy/SKILL.md`

Note: There is no `agents/product-taxonomy.md` — the product-taxonomy skill is self-contained in its SKILL.md. All changes go there.

- [ ] **Step 1: Update the skill wrapper**

Key changes to the SKILL.md:

**Output format (Phase 4):**
- Replace single `## Attributes` table with `## Core Attributes` and `## Extended Attributes` tables
- Add `**Taxonomy ID:**` to the file header template (looked up from `categories.md`)
- Update the canonical file structure example to show both tables
- Add core selection criteria: identity, material/composition, primary dimension, identification/provenance

**Self-verification checks (Phase 5) — specific changes:**
- Check 2: Change "Attribute count in range: 20-40" → "Core: 5-10, Extended: 10-15, Total: 15-30"
- Check 3: Change "Single flat table" → "Two table sections: `## Core Attributes` and `## Extended Attributes`"
- Add Check: "Taxonomy ID present and matches an ID in `categories.md`"
- Keep all other checks unchanged (mandatory attrs first in core, currency separate, descriptions company-neutral, compliance international, no sub-subcategory drilling, changelog present, pricelist test, format compliance)

**Evolution mode rules (add to Phase 2):**
- Evolution runs can only add attributes to Extended
- Promotion from extended → core requires frequency evidence (3+ companies)
- Never delete or rename existing attributes (append-only)
- When invoked by scraper-generator feedback loop, the skill evaluates whether proposed attributes are genuinely significant for the subcategory (researches other companies, not just the triggering company)

- [ ] **Step 2: Verify the skill file is syntactically correct**

Read through the updated SKILL.md and confirm the markdown renders correctly, the template is consistent, and the verification checks match the spec.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/product-taxonomy/SKILL.md
git commit -m "feat: update product-taxonomy skill for core/extended schema format"
```

### Task 5: Migrate all 237 schemas (big bang)

**Files:**
- Modify: All 237 files in `docs/product-taxonomy/sku-schemas/*.md`

- [ ] **Step 1: Create the migration agent prompt**

Write a prompt that an agent can execute for each schema. The prompt:
1. Reads the existing flat schema
2. Reads `categories.md` to find the taxonomy ID for this subcategory
3. Applies core selection heuristics (identity, material, dimension, identification/provenance → core; everything else → extended; deep spec sheet only → drop)
4. Writes the updated schema in the new two-table format
5. Self-verifies against the new rules

This migration is explicitly exempted from the append-only rule — it may restructure, trim, and drop attributes.

- [ ] **Step 2: Run the migration across all schemas**

Execute the migration using parallel agents (batches of ~20 to avoid overwhelming the system). Each agent handles one schema file.

- [ ] **Step 3: Run the schema verification script — expect PASS for all**

Run: `uv run scripts/verify_schemas.py`
Expected: PASS for all 237 schemas

- [ ] **Step 4: Spot-check a sample of migrated schemas**

Review 5-6 schemas from different categories to verify the core/extended split makes sense:
- `power-tools-drills-saws-sanders.md`
- `fasteners-bolts-nuts-screws-rivets.md`
- `nutritional-supplements-vitamins.md`
- `drinkware-glassware-wine-glasses-tumblers-decanters.md`
- `head-protection-hard-hats-helmets.md`
- `major-appliances-refrigerators-ovens-washers.md`

- [ ] **Step 5: Commit as a single commit (enables `git revert` rollback)**

```bash
git add docs/product-taxonomy/sku-schemas/
git commit -m "feat: migrate all 237 SKU schemas to core/extended format"
```

---

## Phase 3: Agent & Skill Updates

Update the pipeline agents and skill wrappers to use taxonomy IDs, the new schema format, and the three-bucket product record.

### Task 6: Update product-classifier agent (Stage 1)

**Files:**
- Modify: `agents/product-classifier.md`
- Modify: `.claude/skills/product-classifier/SKILL.md`

- [ ] **Step 1: Update the agent file**

Key changes to `agents/product-classifier.md`:
- Step 3 (Classify into Taxonomy): Replace "one primary, at most one secondary" with "unlimited subcategories, one primary". The agent reads taxonomy IDs from `categories.md` using the regex parsing logic.
- Step 5 (Report format): Update the Business Classification table to use `Subcategories` (all taxonomy IDs) and `Primary` (single taxonomy ID) fields instead of `Primary` and `Secondary` display names. Display names kept in parentheses.
- Step 6 (Self-verification): Update checks to validate taxonomy IDs exist in `categories.md`.

- [ ] **Step 2: Update the skill wrapper**

Key changes to `.claude/skills/product-classifier/SKILL.md`:
- Update file location references if needed
- Note that the agent now outputs taxonomy IDs, not display names

- [ ] **Step 3: Commit**

```bash
git add agents/product-classifier.md .claude/skills/product-classifier/SKILL.md
git commit -m "feat: product-classifier uses taxonomy IDs and unlimited subcategories"
```

### Task 7: Update catalog-detector agent (Stage 2)

**Files:**
- Modify: `agents/catalog-detector.md`

- [ ] **Step 1: Update the agent file**

Minimal change — add instruction to note URL path patterns observed per product category in the catalog assessment. This provides useful input for the scraper-generator's URL mapping in Stage 3.

Add to the assessment template a section like:
```
### URL Patterns by Category
- `/Head-Protection/` → head protection products
- `/Respiratory-Protection/` → respiratory protection products
```

- [ ] **Step 2: Commit**

```bash
git add agents/catalog-detector.md
git commit -m "feat: catalog-detector notes URL patterns per category"
```

### Task 8a: Update scraper-generator — product record format & attribute mapping

**Files:**
- Modify: `agents/scraper-generator.md`
- Modify: `.claude/skills/scraper-generator/SKILL.md`

- [ ] **Step 1: Update product record format in the agent**

Replace the current single `attributes` object with the three-bucket format:
- `core_attributes`: mapped to schema core names
- `extended_attributes`: mapped to schema extended names
- `extra_attributes`: unmapped site-specific data
- Add `_format: 2`, `brand` (top-level), `product_category` (taxonomy ID)

Update the data contract section, the product record schema, and all examples.

- [ ] **Step 2: Add attribute mapping enforcement**

The scraper-generator must:
1. Read core and extended attribute names from the schema
2. Map site-specific field names to schema attribute names
3. Enforce: core/extended attributes use exact schema names (snake_case)
4. Unmapped attributes go to `extra_attributes`
5. `extra_attributes` governance: keys must be `snake_case`, values must be primitives or arrays of primitives. Add this to self-verification checks.

- [ ] **Step 3: Add backward compatibility for company reports**

The scraper-generator must handle both old and new company report formats:
- Old format: reads `Primary` and `Secondary` fields with `Category > Subcategory` display names
- New format: reads `Subcategories` and `Primary` fields with taxonomy IDs

Detection: if the report has a `Subcategories` row, use new format. Otherwise, fall back to old format by matching display names against `categories.md` to resolve taxonomy IDs.

Note: When a company re-enters the pipeline, Stage 1 runs first and produces a new-format report. This backward compat is only needed during the transition period for manual scraper regeneration of existing companies.

- [ ] **Step 4: Update self-verification checks**

Add new checks:
- Product records have `_format: 2`
- `product_category` is a valid taxonomy ID from `categories.md`
- `core_attributes` keys match schema core names
- `extended_attributes` keys match schema extended names
- `extra_attributes` keys are `snake_case`, values are primitives or arrays of primitives

- [ ] **Step 5: Update the skill wrapper**

Update `.claude/skills/scraper-generator/SKILL.md`:
- Reference the new product record format
- Add `config.json` fields: `category_mapping`, `default_category`

- [ ] **Step 6: Commit**

```bash
git add agents/scraper-generator.md .claude/skills/scraper-generator/SKILL.md
git commit -m "feat: scraper-generator outputs three-bucket format with attribute mapping"
```

### Task 8b: Update scraper-generator — URL mapping & multi-subcategory support

**Files:**
- Modify: `agents/scraper-generator.md`

- [ ] **Step 1: Add URL-prefix → taxonomy ID mapping logic**

Add a new step between catalog assessment reading and scraper code generation:
1. Read the company report to get all `Subcategories` taxonomy IDs
2. Discover all unique URL path prefixes from sitemap
3. Map each prefix to a taxonomy ID (exhaustive — every prefix must be mapped)
4. If a prefix cannot be mapped, escalate (not silently skip)
5. Store mapping in `config.json` as `category_mapping` and `default_category`
6. The generated scraper uses this mapping to set `product_category` per product via substring match on URL — no LLM at runtime

- [ ] **Step 2: Add multi-subcategory schema loading**

When a company spans multiple subcategories:
1. Load SKU schemas for ALL subcategories in the company's `Subcategories` list
2. For each product, determine its subcategory from URL mapping
3. Map the product's attributes against the correct subcategory's schema for core/extended classification
4. Products that don't match any URL prefix get `product_category: "_unclassified"` and use the primary subcategory's schema as fallback

- [ ] **Step 3: Commit**

```bash
git add agents/scraper-generator.md
git commit -m "feat: scraper-generator builds URL→taxonomy mapping for multi-subcategory companies"
```

### Task 8c: Update scraper-generator — taxonomy feedback loop

**Files:**
- Modify: `agents/scraper-generator.md`

- [ ] **Step 1: Add taxonomy feedback loop (post-test step)**

After the `--limit 20` test passes, as a post-generation step that does NOT affect the current scraper:
1. Collect all unique attribute keys from `extra_attributes` across test output
2. Check if any appear on >80% of products
3. If yes, invoke `/product-taxonomy` in evolution mode to evaluate adding them as extended attributes
4. The taxonomy skill researches whether the attribute is genuinely significant (not just company-specific)
5. Log what was proposed — the scraper-generator reports which attributes were submitted

The feedback does NOT re-map the current scraper's output. Newly added attributes take effect on future scraper generations.

- [ ] **Step 2: Add file lock for concurrency**

The feedback step must acquire a file lock before modifying any schema:
- Lock file: `{schema-file}.lock` (e.g., `power-tools-drills-saws-sanders.md.lock`)
- Location: next to the schema file in `docs/product-taxonomy/sku-schemas/`
- If locked: skip the feedback step, log a warning ("Another agent is updating this schema")
- Staleness: locks older than 10 minutes are considered stale and can be broken
- The lock logic is implemented as instructions in the scraper-generator agent file (the LLM agent creates/checks/removes the lock file during execution)

- [ ] **Step 3: Commit**

```bash
git add agents/scraper-generator.md
git commit -m "feat: scraper-generator taxonomy feedback loop with file locking"
```

### Task 9: Update eval-generator agent (Stage 4)

**Files:**
- Modify: `agents/eval-generator.md`
- Modify: `.claude/skills/eval-generator/SKILL.md`

- [ ] **Step 1: Update the check definitions**

Replace the current 9-check table with the new 12-check table from the spec:

| Check | Weight | Threshold |
|-------|--------|-----------|
| `core_attribute_coverage` | 20 | 0.90 |
| `extended_attribute_coverage` | 5 | 0.50 |
| `pagination_completeness` | 10 | 0.70 |
| `category_diversity` | 5 | 0.50 |
| `category_classification` | 10 | 0.95 |
| `price_sanity` | 10 | 1.00 |
| `data_freshness` | 5 | 1.00 |
| `schema_conformance` | 5 | 1.00 |
| `row_count_trend` | 5 | 0.80 |
| `duplicate_detection` | 10 | 0.99 |
| `field_level_regression` | 10 | 0.50 |
| `extra_attributes_ratio` | 5 | 0.50 |

- [ ] **Step 2: Add v1/v2 format handling**

The eval must detect `_format` field:
- v1 (absent): read `attributes` as flat dict, apply old-style checks
- v2 (`_format: 2`): read `core_attributes`, `extended_attributes`, `extra_attributes` separately

- [ ] **Step 3: Define new check implementations**

- `core_attribute_coverage`: same as old `attribute_coverage` but only counts core schema attributes
- `extended_attribute_coverage`: same logic but for extended attributes, lighter threshold (0.50)
- `category_classification`: count products where `product_category` is not `_unclassified`, ratio must be >= 0.95
- `extra_attributes_ratio`: compute `1 - (extra_count / (core_count + extended_count))`, must be >= 0.50

- [ ] **Step 4: Update the skill wrapper**

Update `.claude/skills/eval-generator/SKILL.md`:
- Reference new check table
- Note v1/v2 format handling

- [ ] **Step 5: Commit**

```bash
git add agents/eval-generator.md .claude/skills/eval-generator/SKILL.md
git commit -m "feat: eval-generator supports 12 checks with core/extended split"
```

### Task 10: Update product-discovery orchestrator

**Files:**
- Modify: `.claude/skills/product-discovery/SKILL.md`

- [ ] **Step 1: Update the orchestrator**

- Update the pipeline summary template: add `product_category` to the output
- Update the Stage 1 description to reflect unlimited subcategories
- Update the Stage 3 description to reflect three-bucket output format
- Update the Stage 4 description to reflect 12 checks

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/product-discovery/SKILL.md
git commit -m "feat: product-discovery orchestrator updated for taxonomy enforcement"
```

---

### Task 11: Create attribute promotion verification script

**Files:**
- Create: `scripts/check_attribute_promotion.py`

- [ ] **Step 1: Write the promotion script**

This script scans all scraper configs (`docs/scraper-generator/*/config.json`) for a given subcategory and counts how many companies extract each attribute. Attributes appearing in 3+ company scrapers are candidates for promotion from extended → core.

The script:
1. Takes a taxonomy ID as argument (e.g., `machinery.power_tools`)
2. Finds all scraper configs where `category` matches that ID
3. Reads their test output (`output/products.jsonl`) if available
4. Counts attribute frequency across companies
5. Reports which extended attributes appear in 3+ companies → candidates for core promotion

This is an advisory tool, not automated — the output informs a manual `/product-taxonomy` evolution run.

- [ ] **Step 2: Commit**

```bash
git add scripts/check_attribute_promotion.py
git commit -m "feat: add attribute promotion verification script"
```

---

## Phase 4: Validation

End-to-end validation that the updated pipeline works correctly.

### Task 12: Verify skill conventions

- [ ] **Step 1: Run the skill convention verifier**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all`
Expected: All skills pass convention checks. Fix any issues introduced by the agent/skill modifications.

- [ ] **Step 2: Run taxonomy and schema verification**

Run: `uv run scripts/verify_taxonomy.py && uv run scripts/verify_schemas.py`
Expected: Both PASS

- [ ] **Step 3: Commit any fixes**

```bash
git add -A
git commit -m "fix: address convention violations from skill updates"
```

### Task 13: Run a test company through the updated pipeline

- [ ] **Step 1: Pick a test company**

Choose a company that spans a single subcategory for simplicity (e.g., Festool for power tools, or a new company not yet in the system).

- [ ] **Step 2: Run the full pipeline**

Execute `/product-discovery` for the test company. Verify:
- Stage 1: Company report uses taxonomy IDs in `Subcategories` and `Primary` fields
- Stage 2: Catalog assessment notes URL patterns
- Stage 3: Scraper outputs `_format: 2` with `core_attributes`, `extended_attributes`, `extra_attributes`, `product_category`
- Stage 4: Eval uses 12 checks, handles v2 format

- [ ] **Step 3: Verify cross-company searchability**

Check that the test company's products have the same `core_attributes` field names as another company in the same subcategory (if one exists). For example, if testing a power tools company, compare its output against Milwaukee Tool's schema-aligned output.

- [ ] **Step 4: Commit any fixes**

```bash
git add -A
git commit -m "fix: address issues found during single-subcategory validation"
```

### Task 14: Run a multi-subcategory company

- [ ] **Step 1: Pick a multi-subcategory company**

Test with a company that spans multiple subcategories (e.g., MSA Safety — respiratory protection, head protection, fall protection, sensors).

- [ ] **Step 2: Run the full pipeline**

Execute `/product-discovery` for the test company. Verify:
- Stage 1: Company report lists multiple taxonomy IDs in `Subcategories`
- Stage 3: URL mapping correctly assigns different `product_category` values per product
- Each product's `core_attributes` and `extended_attributes` match the correct subcategory's schema
- Products that don't match any URL prefix get `_unclassified`

- [ ] **Step 3: Commit any fixes**

```bash
git add -A
git commit -m "fix: address issues found during multi-subcategory validation"
```

---

## Summary

| Phase | Tasks | What it produces |
|-------|-------|-----------------|
| 1: Taxonomy IDs | Tasks 1-2 | `categories.md` with 237 IDs, verification script |
| 2: Schema Migration | Tasks 3-5 | 237 schemas in core/extended format, verification script |
| 3: Agent Updates | Tasks 6-11 | Updated agents and skills, promotion script |
| 4: Validation | Tasks 12-14 | Convention checks, end-to-end proof (single + multi-subcategory) |

Each phase is independently committable and produces verifiable results. Phases 1-2 are pure data/format changes with no behavior change. Phases 3-4 change pipeline behavior.
