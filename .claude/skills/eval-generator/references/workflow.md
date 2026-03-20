# Eval Generator Workflow

**Input:** Company slug, scraper source, catalog assessment, generator input, eval script
**Output:** eval_config.json, verified by running the scraper and eval script, or escalation

---

## Context

This workflow generates a per-company eval config file that the eval script uses to validate scrape quality. The config captures company-specific values — expected product counts, core attributes, type mappings, enum constraints, and price availability. The eval script implements all check logic; the workflow's job is to determine the correct config values and verify they work.

Read the company report, catalog assessment, scraper source, and generator input file to understand what the scraper extracts and what the eval should expect.

### Inputs

These files must exist before the workflow starts. SKILL.md is responsible for providing them.

| File | Path | Used in | What the workflow reads from it |
|------|------|---------|-------------------------------|
| Company report | `docs/product-classifier/{slug}.md` | Step 2 | Business model, product lines |
| Catalog assessment | `docs/catalog-detector/{slug}/assessment.md` | Step 2 | Estimated product count, top-level categories, has_prices |
| Scraper source | `docs/scraper-generator/{slug}/scraper.py` | Step 1 | Which attributes it extracts, output structure, price extraction |
| Generator input | `docs/scraper-generator/{slug}/generator_input.json` | Step 3 | Core/extended attribute keys, types, units per subcategory |
| Eval script | `.claude/skills/eval-generator/scripts/eval_run.py` | Step 5 | Runs checks against collected products |

### Outputs

All outputs are written to `docs/eval-generator/{slug}/`.

| File | Written by | Description |
|------|-----------|-------------|
| `docs/eval-generator/{slug}/eval_config.json` | Workflow (Step 4) | Per-company eval config with subcategory attribute maps, type_map, semantic_validation |
| `docs/eval-generator/{slug}/output/products.jsonl` | Scraper (Step 5a) | Products scraped per sampling rules in `references/conditions.md` |
| `docs/eval-generator/{slug}/output/summary.json` | Scraper (Step 5a) | Run metadata (total_products, duration, errors) |
| `docs/eval-generator/{slug}/output/debug.log` | Scraper (Step 5a) | Structured log of HTTP requests and parse events |
| `docs/eval-generator/{slug}/output/eval_result.json` | Eval script (Step 5b) | Thirteen weighted check scores, degradation score, pass/degraded/fail status |
| `docs/eval-generator/{slug}/output/eval_history.json` | Eval script (Step 5b) | Append-only log of all eval runs |
| `docs/eval-generator/{slug}/output/baseline.json` | Eval script (Step 5b) | First-run attribute fill rates for regression detection |

---

## Step 1: Understand the Scraper

Read the scraper source to determine:

- Which attributes it extracts (both mandatory core attributes and category-specific attributes)
- Which attributes go into `core_attributes`, `extended_attributes`, and `extra_attributes`
- Which attributes are strings, numbers, lists, or booleans
- Whether it extracts prices

If the scraper source is missing or its output structure cannot be determined, escalate — see the `scraper_output_format_unclear` decision.

---

## Step 2: Understand the Catalog Context

Read the catalog assessment to extract:

- Estimated product count → use for `expected_product_count` in eval config
- Top-level product category names → use for `expected_top_level_categories` in eval config
- Whether the catalog has prices → use for `has_prices` in eval config
- Any notes about catalog structure or known gaps

Read the company report for additional context on business model and product lines.

If the catalog assessment does not contain an estimated product count, handle gracefully — see the `missing_product_count_estimate` decision.

---

## Step 3: Load the Generator Input

Read the generator input file (`generator_input.json`) produced by scraper-generator. This file contains pre-processed SKU schemas with core/extended attribute keys, data types, and units per subcategory — the same routing tables the scraper uses.

If the file does not exist, see the `missing_generator_input` decision.

The file has this structure:

```json
{
  "subcategory_schemas": {
    "taxonomy_id": {
      "core_attribute_keys": ["key1", "key2"],
      "extended_attribute_keys": ["key3", "key4"],
      "mandatory_keys": ["key1"],
      "attribute_types": {"key1": "number", "key2": "str", "key3": "str", "key4": "number"},
      "units": {"key1": "mm", "key4": "kW"}
    }
  }
}
```

For each subcategory in `subcategory_schemas`, extract:

- **`core_attribute_keys`** → becomes `subcategories.{id}.core_attributes` in the eval config
- **`extended_attribute_keys`** → becomes `subcategories.{id}.extended_attributes` in the eval config
- **`attribute_types`** → merged across all subcategories to build the flat `type_map` in the eval config
- **`units`** → attributes with units are numeric; use to build `semantic_validation.numeric_fields`

Derive `expected_count` per subcategory from the catalog assessment's category tree — sum leaf category product counts that map to each subcategory. If not derivable, divide `expected_product_count` equally among subcategories. Each subcategory gets its own `core_attributes`, `extended_attributes`, and `expected_count`. Do NOT union them.

For `enum_attributes`: inspect the scraper source to identify attributes with a closed set of allowed values. Use an empty object `{}` when no enum constraints are clearly identifiable.

---

## Step 4: Generate the Eval Config

Produce the eval config file with all required fields:

```json
{
  "company_slug": "<slug>",
  "expected_product_count": 500,
  "expected_top_level_categories": ["Category A", "Category B"],
  "subcategories": {
    "wood.softwood_hardwood_lumber": {
      "core_attributes": ["wood_type", "structural_grade"],
      "extended_attributes": ["species", "nominal_thickness"],
      "expected_count": 300
    },
    "wood.millwork": {
      "core_attributes": ["material", "joint_type"],
      "extended_attributes": ["species", "profile_pattern"],
      "expected_count": 200
    }
  },
  "type_map": {"wood_type": "str", "structural_grade": "str"},
  "enum_attributes": {},
  "has_prices": true,
  "semantic_validation": {
    "numeric_fields": ["nominal_width", "nominal_thickness", "width", "thickness"]
  }
}
```

### Field derivation

| Field | Source | How to determine |
|-------|--------|------------------|
| `company_slug` | Skill input | The company slug (e.g., `festool`) — same `{slug}` used in all file paths |
| `expected_product_count` | Catalog assessment | The estimated product count. If missing, see the `missing_product_count_estimate` decision. |
| `expected_top_level_categories` | Catalog assessment | The top-level category names from the category structure section. These are the catalog's own category names (e.g., "Riga Wood"), not taxonomy categories. |
| `subcategories` | Generator input + catalog assessment | Per-subcategory map. Each entry has `core_attributes` (from `core_attribute_keys`), `extended_attributes` (from `extended_attribute_keys`), and `expected_count` (from catalog assessment category tree). Only attributes the scraper actually extracts. |
| `type_map` | Generator input + scraper source | Merge `attribute_types` from all subcategories in `generator_input.json` into a flat map. Values are already in eval format: `"str"`, `"number"`, `"list"`, `"bool"`. For extra attributes not in the generator input, inspect the scraper source. |
| `enum_attributes` | Scraper source | Maps attributes that have a closed set of allowed values to their value arrays. Only include attributes where the allowed values are clearly enumerable from the scraper logic. Use an empty object `{}` when no enum constraints apply. |
| `has_prices` | Catalog assessment + scraper source | `true` if the catalog has prices and the scraper extracts them, `false` otherwise. When `false`, the eval script skips the price sanity check. |
| `semantic_validation` | Generator input | Object with `numeric_fields` array. Derived from `attribute_types` — include all attributes where the type is `"number"`. Also include attributes that have entries in `units` (these are measurement fields). |

### Config format rules

Validate the generated config against the format rules in `references/conditions.md` § Config format rules.

---

## Step 5: Verify End-to-End

Two commands: run the scraper to collect products, then run the eval to score them.

### Step 5a: Collect products

Follow the collection strategy in `references/conditions.md` to determine sample sizes and invocation pattern (single vs per-subcategory). Output all files to `docs/eval-generator/{slug}/output/`.

### Step 5b: Score with eval

Run the eval script pointing to the collected products:

```
uv run .claude/skills/eval-generator/scripts/eval_run.py docs/eval-generator/{slug}/eval_config.json
```

If the eval fails or produces unexpected results, review the config for these common problems:

- Attribute names in `type_map` do not match what the scraper actually writes — cross-check against the scraper source.
- `expected_top_level_categories` values do not match the category names the scraper uses in `category_path` — compare with actual scraper output.

---

## Step 6: Self-Verification

After the run completes, read the eval result file (`docs/eval-generator/{slug}/output/eval_result.json`) and verify all 13 checks appear in the output. Use the self-verification checklist in `references/conditions.md`.

If the eval runs successfully and all 13 checks appear in the result, the config is verified.

---

## Boundaries

- This workflow generates eval config files only — it does not modify the eval script or scraper code.
- It does not trigger rediscovery — the eval script sets `recommend_rediscovery` based on the degradation score.
- It does not define or modify the product taxonomy or SKU schemas.
- Mandatory core attribute checks (`sku`, `name`, `url`, `price`, `currency`, `brand`, `scraped_at`) are hardcoded in the eval script. The config only controls category-specific attribute expectations.

---

## Decisions

### Decision: missing_product_count_estimate

**Context:** The catalog assessment does not contain an estimated product count, which the config needs for `expected_product_count`.
**Autonomous resolution:** Use the best available estimate. Check the scraper source for any hardcoded product limits or count references. If a reasonable estimate can be inferred from the catalog assessment's category structure (e.g., summing per-category counts), use that. As a last resort, set `expected_product_count` to the number of products in the current scraper output (from the scraper run summary), understanding this makes pagination completeness a baseline-only check.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: missing_generator_input

**Context:** The generator input file (`generator_input.json`) does not exist in the scraper-generator output directory. This file is produced by scraper-generator and contains the pre-processed SKU schemas needed to build the eval config.
**Autonomous resolution:** Re-run the prepare script to generate it: `uv run .claude/skills/scraper-generator/scripts/orchestrator_prepare_generator_input.py --schemas {taxonomy_ids} --output docs/scraper-generator/{slug}/generator_input.json` — where `{taxonomy_ids}` are the space-separated subcategory IDs from the company report. If the script exits 0 or 1 (partial), continue with available data.
**Escalate when:** The scraper-generator stage has never been run for this company (no `docs/scraper-generator/{slug}/` directory exists at all). The eval requires a working scraper to validate.
**Escalation payload:** Company slug, confirmation that the scraper-generator output directory does not exist.

### Decision: scraper_output_format_unclear

**Context:** The scraper source code is ambiguous about the output format it produces, making it unclear how to populate the config's attribute fields.
**Autonomous resolution:** If the scraper source exists but uses an unusual output structure, infer the format from the code and proceed.
**Escalate when:** Scraper source is missing or unparseable.
**Escalation payload:** Company slug, details about what is missing or malformed in the scraper source.
