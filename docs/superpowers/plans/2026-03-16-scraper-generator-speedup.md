# Scraper Generator Speedup Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce scraper-generator stage from ~37 minutes to ~8 minutes by adding an extraction blueprint to the catalog-detector, eliminating 2 of 3 sub-agents, adding a pre-processing script for schema loading, and reducing smoke test size.

**Architecture:** The catalog-detector produces a verified extraction blueprint (category URLs, price method, CSS selectors, sample labels). A Python script pre-processes SKU schemas into routing tables. The scraper-generator orchestrator handles label mapping and code generation inline (no sub-agents), dispatching only the validator. Language-level label seeds are shared across sites.

**Tech Stack:** Markdown (skill workflows), Python (pre-processing script, verify_skill.py), JSON (generator input, language seeds)

**Spec:** `docs/superpowers/specs/2026-03-16-scraper-generator-speedup-design.md`

---

## Chunk 1: Catalog-detector extraction blueprint

### Task 1: Enhance Step 5 and add Step 5a to catalog-detector workflow

**Files:**
- Modify: `.claude/skills/catalog-detector/references/workflow.md`

- [ ] **Step 1: Read the current workflow**

Read `.claude/skills/catalog-detector/references/workflow.md` (351 lines). Locate Step 5 (Product Attribute Extractability Check, ~line 133) and Step 6 (Determine Scraping Strategy, ~line 154).

- [ ] **Step 2: Enhance Step 5 with extraction metadata collection**

After the existing Step 5 content (which checks whether attributes are present as structured text), add instructions to record extraction metadata from the 3-5 product pages already being inspected:

```markdown
### Extraction metadata (collected from the same 3-5 product pages)

While inspecting product pages for extractability, also record these details for the extraction blueprint:

**Price extraction method** — check in this order:
1. Look for `<script type="application/ld+json">` blocks containing Product schema with a price field in the raw HTML (before JS runs)
2. Check whether any element with price-related CSS classes (`.price`, `.product-price`, `.current-price`) contains actual numeric price text in the raw HTML
3. Search the raw HTML source for `dataLayer.push(` containing a `"price"` field
4. If using Playwright for investigation, check network requests for API calls returning price data

Record which method succeeded and the specific extraction pattern.

**Spec table selectors** — identify the CSS selector path to the product attribute table:
- What HTML element contains the spec table (e.g., `table`, `dl`, `div.specifications`)
- How to iterate over attribute rows (e.g., `table tr`)
- How to extract the label from each row (e.g., `td:first-child`)
- How to extract the value from each row (e.g., `td:nth-child(2)`)

**Product name selector** — the CSS selector for the main product heading (e.g., `h1`).

**SKU/reference location** — where the product identifier appears (e.g., spec table label "Norāde", JSON-LD field, or dedicated element).

**Breadcrumb selector** — the CSS selector for the category breadcrumb navigation.

**Sample attribute labels** — collect every unique attribute label from the spec tables across all inspected product pages. Record: the exact label text, how many of the inspected pages include it, and one example value.
```

- [ ] **Step 3: Add Step 5a (Verified Category Tree)**

Insert a new `## Step 5a: Verified Category Tree` between the enhanced Step 5 and Step 6:

```markdown
## Step 5a: Verified Category Tree

After Step 5 confirms that product attributes are extractable, crawl the full category tree to produce a verified URL inventory. This eliminates the most common source of downstream bugs — wrong or assumed category URL paths.

Starting from each top-level category discovered in Step 3:
1. Fetch the category page
2. Identify child category links (URLs that extend the current path with `/{id}-{slug}`)
3. If children exist: recurse into each child (this is a branch node)
4. If no children exist: this is a leaf node — count the product links on the page
5. Record every node: category path (human-readable breadcrumb), exact URL, product count (0 for branch nodes), and depth level

Output the tree as a table. Include only nodes that are part of the scraper-relevant categories (skip categories that don't map to any taxonomy subcategory, e.g., fuel wood, promotions).

**Circuit breaker:** If the tree exceeds 100 nodes or depth 5, stop recursion and log a warning. Most e-commerce sites have fewer than 50 leaf categories.
```

- [ ] **Step 4: Verify the steps are in the right order**

Read the file and confirm: Step 5 (enhanced) → Step 5a (new) → Step 6 (unchanged). Step 5a must come after Step 5 passes the extractability check (no point crawling the tree if the site isn't scrapable).

### Task 2: Add extraction blueprint to report template and self-verification

**Files:**
- Modify: `.claude/skills/catalog-detector/references/workflow.md`

- [ ] **Step 1: Add the extraction blueprint section to the success template**

In Step 8 (Write Catalog Assessment), inside the success template (the markdown code block starting with `# Catalog Assessment: {Company Name}`), add the `## Extraction Blueprint` section after `## Notes`:

```markdown
## Extraction Blueprint

### Verified Category Tree

| Category Path | URL | Product Count | Depth |
|---|---|---|---|
| {Level 1} > {Level 2} > {Leaf} | {exact URL path} | {count} | {depth} |

### Price Extraction Method
- **Primary method:** {static_html_css | json_ld | dataLayer | api_endpoint}
- **Static HTML price:** {yes: selector | no: reason}
- **dataLayer price:** {yes: event name and JSON path | no}
- **JSON-LD price:** {yes | no}
- **Verified on:** {2-3 product URLs with actual extracted prices}
- **Currency:** {ISO 4217}
- **Price variants:** {description if applicable, e.g., per-unit vs per-area}

### Spec Table Selectors
- **Row selector:** {CSS selector for attribute rows}
- **Label cell:** {CSS selector or position for the label}
- **Value cell:** {CSS selector or position for the value}
- **Verified on:** {2-3 product URLs with attribute counts}

### Product Name Selector
- **Selector:** {CSS selector}

### SKU/Reference Location
- **Source:** {spec table label | JSON-LD field | dedicated element}
- **Label/field name:** {exact text or key}

### Breadcrumb Selector
- **Selector:** {CSS selector}

### Sample Attribute Labels

| Site Label | Frequency | Example Value |
|---|---|---|
| {exact label text} | {N/M pages} | {example} |
```

- [ ] **Step 2: Add two new self-verification gates**

In Step 9 (Self-Verification), add to the success report gates table:

```markdown
| 9 | **Verified category tree is complete** | Every leaf category from Step 3 that maps to a taxonomy subcategory has a row in the Extraction Blueprint table with a verified URL and product count > 0 |
| 10 | **Price method is verified** | Extraction Blueprint lists at least 2 product URLs with actual extracted price values |
```

- [ ] **Step 3: Verify the template is valid**

Read the full success template and confirm: all existing sections are intact, `## Extraction Blueprint` comes after `## Notes`, and the template would produce valid markdown.

---

## Chunk 2: Pre-processing script and language seeds

### Task 3: Create prepare_generator_input.py

**Files:**
- Create: `.claude/skills/scraper-generator/scripts/prepare_generator_input.py`

- [ ] **Step 1: Write the script**

```python
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
    """Extract core/extended attribute keys and types from a schema file."""
    content = schema_path.read_text(encoding="utf-8")

    core_rows = parse_schema_table(content, "Core Attributes")
    extended_rows = parse_schema_table(content, "Extended Attributes")

    core_keys = []
    extended_keys = []
    types = {}

    for row in core_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            core_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")

    for row in extended_rows:
        key = row.get("Key", "").strip()
        data_type = row.get("Data Type", "").strip()
        if key and key not in UNIVERSAL_KEYS:
            extended_keys.append(key)
            types[key] = TYPE_MAP.get(data_type, "str")

    return {
        "core": core_keys,
        "extended": extended_keys,
        "types": types,
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
```

- [ ] **Step 2: Test the script with PATA's schemas**

```bash
uv run python .claude/skills/scraper-generator/scripts/prepare_generator_input.py \
  --schemas wood.softwood_hardwood_lumber wood.flooring_decking wood.millwork \
    wood.plywood_engineered_panels chemicals.paints_coatings_inks metals.fasteners \
  --output /tmp/test_generator_input.json
```

Expected: JSON file with 6 routing tables, each containing `core`, `extended`, and `types` arrays. No errors.

```bash
uv run python -c "
import json
data = json.load(open('/tmp/test_generator_input.json'))
for tid, table in data['routing_tables'].items():
    print(f'{tid}: {len(table[\"core\"])} core, {len(table[\"extended\"])} extended')
"
```

Expected output like:
```
wood.softwood_hardwood_lumber: 5 core, 15 extended
wood.flooring_decking: 5 core, 15 extended
...
```

- [ ] **Step 3: Clean up test output**

```bash
rm /tmp/test_generator_input.json
```

### Task 4: Create language seed infrastructure

**Files:**
- Create: `docs/platform-knowledgebase/labels-lv.json`

- [ ] **Step 1: Create the Latvian label seed from the pata.lv run**

Extract the LABEL_MAP from the pata.lv scraper and save as the Latvian seed:

```json
{
  "_language": "lv",
  "_description": "Latvian attribute label translations for building materials sites",
  "_updated": "2026-03-16",
  "labels": {
    "Platums": "width",
    "Biezums": "thickness",
    "Garums": "length",
    "Suga": "species",
    "Mitrums": "moisture_content",
    "Kvalitāte": "grade",
    "Kvalitātes grupa": "grade",
    "Zāģējuma veids": "profile_pattern",
    "Virsmas apstrāde": "finish",
    "Krāsa/Tonis": "color",
    "Krāsa": "color",
    "Platība": "coverage_per_box",
    "Iepakojuma izmērs": "pack_quantity",
    "Iepakojums": "pack_quantity",
    "Iepakojumā": "pack_quantity",
    "Pielietojums": "application",
    "Diametrs": "diameter",
    "Galvas forma": "head_type",
    "Korozijas izturības klase": "finishcoating",
    "Vide": "interiorexterior",
    "Lietošanas vide": "interiorexterior",
    "Apstiprinājumi": "certification",
    "Bitu tips": "drive_type",
    "Savienotāja tips": "connector_type",
    "Galvas diametrs": "head_diameter"
  },
  "category_aliases": {
    "wood.softwood_hardwood_lumber": {
      "width": "nominal_width",
      "thickness": "nominal_thickness",
      "grade": "appearance_grade"
    },
    "wood.flooring_decking": {
      "width": "width",
      "thickness": "thickness",
      "grade": "grade"
    },
    "wood.millwork": {
      "width": "width",
      "thickness": "thickness"
    },
    "wood.plywood_engineered_panels": {
      "width": "width",
      "thickness": "thickness"
    }
  },
  "value_translations": {
    "species": {
      "Egle": "Spruce",
      "Priede": "Pine",
      "Bērzs": "Birch",
      "Melnalksnis": "Black Alder",
      "Apse": "Aspen",
      "Osis": "Ash",
      "Akācija": "Acacia",
      "Ozols": "Oak",
      "Gumijkoks": "Rubber Wood"
    }
  }
}
```

- [ ] **Step 2: Verify the file is valid JSON**

```bash
uv run python -c "import json; data = json.load(open('docs/platform-knowledgebase/labels-lv.json')); print(f'Labels: {len(data[\"labels\"])}, Aliases: {len(data[\"category_aliases\"])}, Value translations: {len(data[\"value_translations\"])}')"
```

Expected: `Labels: 24, Aliases: 4, Value translations: 1`

---

## Chunk 3: Scraper-generator rewrite

### Task 5: Rewrite scraper-generator orchestrator

**Files:**
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md`

This is the largest content change. The orchestrator loses 2 dispatch sections and gains inline label mapping + code generation steps.

- [ ] **Step 1: Read the current orchestrator**

Read `.claude/skills/scraper-generator/references/orchestrator.md` (411 lines). Map the sections:
- Steps 1, 1b, 2, 2a — context loading (KEEP, mostly unchanged)
- Dispatch: Label Discovery — REMOVE
- Dispatch: Code Generation — REMOVE
- Dispatch: Validation — KEEP
- Steps 3, 4, 5 — post-validation (KEEP)
- Decisions — KEEP

- [ ] **Step 2: Replace Dispatch: Label Discovery with inline Step 2b**

Replace the `## Dispatch: Label Discovery (non-English only)` section (with its input/output contracts and dispatch conditions) with a new inline step:

```markdown
## Step 2b: Build Label Map (non-English only)

Skip for English-language sites.

Build the `LABEL_MAP` and `CATEGORY_ALIASES` dicts that the scraper will use to translate source-language attribute labels to English schema keys.

**Sources (in priority order):**
1. **Language seed file** — check the platform knowledgebase for a language seed (e.g., `labels-lv.json` for Latvian). If it exists, load it as the starting point. It contains common attribute label translations from previous scraper runs in the same language.
2. **Extraction blueprint sample labels** — the catalog assessment's extraction blueprint contains sample attribute labels from 3-5 product pages. Map each label to a schema key using the attribute routing tables from Step 2a.
3. **Unmapped labels** — labels that appear in the blueprint but don't match any schema key go to `extra_attributes` with `snake_case` keys derived from the source-language text.

**Build CATEGORY_ALIASES** for labels that map to different schema keys per subcategory (e.g., "Biezums" → `nominal_thickness` for lumber, `thickness` for flooring). The language seed may already contain aliases from previous sites — use those as a starting point, add any new aliases discovered from the blueprint labels.

**Compute label coverage:** Count how many blueprint labels map to schema keys (via LABEL_MAP + CATEGORY_ALIASES) vs total labels. If coverage is below 70%, log a warning but proceed — the blueprint's sample may be small (3-5 pages). If coverage is below 30%, escalate — see the `label_coverage_insufficient` decision.

**After scraper generation succeeds:** Save the merged LABEL_MAP back to the language seed file so future sites in the same language start with a richer seed. This is a write-back at the end of the pipeline, not during label mapping.
```

- [ ] **Step 3: Replace Dispatch: Code Generation with inline Step 2c**

Replace the `## Dispatch: Code Generation` section with:

```markdown
## Step 2c: Generate Scraper Code

Write a single standalone Python scraper file following the product record format defined in `references/code-generator.md`. Use the pre-processed routing tables from `generator_input.json`, the LABEL_MAP from Step 2b, and the extraction blueprint from the catalog assessment.

**The extraction blueprint provides verified selectors — use them directly:**
- Price extraction: use the method specified in the blueprint (dataLayer regex, CSS selector, JSON-LD parsing, etc.)
- Spec table: use the row/label/value selectors from the blueprint
- Product name: use the selector from the blueprint
- Breadcrumb: use the selector from the blueprint
- Category URLs: use the verified category tree from the blueprint for `CATEGORY_MAPPING`

**Include in the generated scraper:**
- PEP 723 inline script metadata with dependencies
- The LABEL_MAP and CATEGORY_ALIASES from Step 2b as static dicts
- Value translation dicts (e.g., SPECIES_MAP) from the language seed
- Attribute routing tables from generator_input.json
- Persist hook implementations from the persist hooks reference file
- `--limit N` and `--probe URL` arguments via argparse

Read `references/code-generator.md` for the complete product record format, library selection rules, required behavior (items 1-10), product discovery strategy, and Python code quality requirements.
```

- [ ] **Step 4: Update the step flow diagram**

Update the ASCII step flow diagram in the `## Context` section to reflect the new flow:

```
Step 1 → Step 1b → Step 2 → Step 2a → Step 2b (label map, non-English) → Step 2c (generate scraper)
→ DISPATCH: Validator → Step 3 → Step 4 → Step 5 → DONE
```

Remove the three DISPATCH nodes for label discoverer, code generator, and validator. Replace with Step 2b, Step 2c, and one DISPATCH node for validator only.

- [ ] **Step 5: Update the retry state machine**

The retry state machine in the Dispatch: Validation section currently references re-dispatching the label discoverer and code generator. Update:
- `label_coverage_dropped` → return to Step 2b (inline), then Step 2c (inline), then re-dispatch validator
- `core_fill_rate_low` → fix routing tables at Step 2a, re-run Step 2c, re-dispatch validator
- `probe_failed` → ESCALATE (unchanged)
- `test_failed/timeout` → fix Step 2c, re-dispatch validator

- [ ] **Step 6: Update Step 1 to load the pre-processed generator_input.json**

In Step 1 (Load Context), add:

```markdown
Read the pre-processed generator input file for the company. This JSON contains attribute routing tables (core/extended key lists and types per subcategory), pre-built from the SKU schemas by a script. Use these tables directly — do not re-read the raw SKU schema files.
```

- [ ] **Step 7: Verify word count**

```bash
wc -w .claude/skills/scraper-generator/references/orchestrator.md
```

Target: ≤3,000 words. The orchestrator gained Steps 2b and 2c but lost two dispatch sections with their contracts. Net should be similar or shorter.

### Task 6: Update SKILL.md and delete label-discoverer.md

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md`
- Delete: `.claude/skills/scraper-generator/references/label-discoverer.md`

- [ ] **Step 1: Update SKILL.md sub-agent list**

In the `## Workflow` section, replace:

```markdown
- Dispatch sub-agents using the Agent tool as directed by the orchestrator. Sub-agent files in `.claude/skills/scraper-generator/references/`:
  - `label-discoverer.md` — non-English label discovery
  - `code-generator.md` — scraper.py generation
  - `validator.md` — probe testing and smoke tests
  The orchestrator specifies what data to pass to each sub-agent and when to dispatch them.
```

With:

```markdown
- Dispatch the validator sub-agent using the Agent tool as directed by the orchestrator. Sub-agent file: `.claude/skills/scraper-generator/references/validator.md` — probe testing and smoke tests.
  The orchestrator specifies what data to pass and when to dispatch.
- The orchestrator handles label mapping and code generation inline (no sub-agent dispatch for these).
- Reference file `.claude/skills/scraper-generator/references/code-generator.md` defines the canonical product record format — the orchestrator reads it during code generation but does not dispatch it as a sub-agent.
```

- [ ] **Step 2: Add pre-processing script invocation**

In the `## Workflow` section, add before the smoke test commands:

```markdown
- Before starting the orchestrator, run the pre-processing script to build routing tables:
  `uv run python .claude/skills/scraper-generator/scripts/prepare_generator_input.py --schemas {taxonomy_ids} --output docs/scraper-generator/{slug}/generator_input.json`
  where `{taxonomy_ids}` are the space-separated subcategory taxonomy IDs from the company report.
```

- [ ] **Step 3: Add language seed loading instruction**

In the `## Workflow` section, add:

```markdown
- For non-English sites, check for a language seed file at `docs/platform-knowledgebase/labels-{lang}.json` where `{lang}` is the ISO 639-1 language code from the catalog assessment. If it exists, provide it to the orchestrator. After successful scraper generation, save the updated label map back to the seed file.
```

- [ ] **Step 4: Update smoke test limit**

Change `--limit 20` to `--limit 10` in the smoke test command:

```markdown
- Smoke test: `uv run docs/scraper-generator/{slug}/scraper.py --limit 10 2>docs/scraper-generator/{slug}/output/debug.log` with a 2-minute timeout (Bash tool timeout: 120000ms).
```

- [ ] **Step 5: Delete label-discoverer.md**

```bash
git rm .claude/skills/scraper-generator/references/label-discoverer.md
```

- [ ] **Step 6: Verify no broken references**

```bash
grep -rn "label-discoverer" .claude/skills/ | grep -v "docs/superpowers/"
```

Expected: 0 matches (the file was only referenced in SKILL.md and orchestrator.md, both now updated).

### Task 7: Update verify_skill.py for the changes

**Files:**
- Modify: `.claude/skills/skill-creator-local/scripts/verify_skill.py`

- [ ] **Step 1: Update the sub-agent detection in check_subagent_pattern()**

The function currently identifies sub-agent files as `.md` files in `references/` excluding `workflow.md`, `orchestrator.md`, and `persist-hooks.md`. After deleting `label-discoverer.md`, only `code-generator.md` and `validator.md` remain as non-excluded files.

`code-generator.md` is now a reference file (not a sub-agent) but is NOT dispatched. However, it still has `## Input Contract`, `## Output Contract`, and `# Code Generator Sub-Agent` heading — these would trigger the sub-agent checks.

Update the excluded set to also exclude `code-generator.md` since it's a reference, not a dispatched sub-agent:

```python
excluded = {"workflow.md", "orchestrator.md", "persist-hooks.md", "code-generator.md"}
```

- [ ] **Step 2: Run verify_skill.py --all**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
```

Expected: 0 critical, 0 moderate. All skills pass.

---

## Chunk 4: Verification

### Task 8: Full verification

- [ ] **Step 1: Run verify_skill.py --all**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
```

Expected: all 7 skills PASS, 0 issues.

- [ ] **Step 2: Verify no broken references to label-discoverer or agents/**

```bash
grep -rn "label-discoverer\|agents/" .claude/skills/ CLAUDE.md --include="*.md" --include="*.py" | grep -v "docs/superpowers/"
```

Expected: 0 matches.

- [ ] **Step 3: Verify the pre-processing script runs cleanly**

```bash
uv run python .claude/skills/scraper-generator/scripts/prepare_generator_input.py \
  --schemas wood.softwood_hardwood_lumber wood.flooring_decking wood.millwork \
  --output /tmp/verify_routing.json && \
  uv run python -c "import json; d=json.load(open('/tmp/verify_routing.json')); print(f'{len(d[\"routing_tables\"])} schemas processed')" && \
  rm /tmp/verify_routing.json
```

Expected: `3 schemas processed`

- [ ] **Step 4: Verify file structure matches the spec**

```bash
# Sub-agent files: only validator.md should be detected as sub-agent
ls .claude/skills/scraper-generator/references/
# Should show: code-generator.md, orchestrator.md, persist-hooks.md, validator.md
# (label-discoverer.md is gone)

# Language seed exists
ls docs/platform-knowledgebase/labels-lv.json

# Pre-processing script exists
ls .claude/skills/scraper-generator/scripts/prepare_generator_input.py
```

- [ ] **Step 5: Present diff for review**

Show `git diff --stat` for user review before any commit.
