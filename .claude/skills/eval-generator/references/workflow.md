# Eval Generator Workflow

**Input:** Company slug, scraper source, catalog assessment, generator input (routing tables), eval script
**Output:** Eval config file, verified by running the eval script, or escalation

---

## Context

This workflow generates a per-company eval config file that the shared eval script uses to validate scrape quality. The config captures company-specific values — expected product counts, core attributes, type mappings, enum constraints, and price availability. The shared eval script implements all check logic; the workflow's job is to determine the correct config values and verify they work.

Read the company report, catalog assessment, scraper source, and generator input file to understand what the scraper extracts and what the eval should expect.

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

- Estimated product count (becomes `expected_product_count`)
- Top-level product category names (becomes `expected_top_level_categories`)
- Whether the catalog has prices (becomes `has_prices`)
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
| `company_slug` | Company report | The slug from the company report |
| `expected_product_count` | Catalog assessment | The estimated product count. If missing, see the `missing_product_count_estimate` decision. |
| `expected_top_level_categories` | Catalog assessment | The top-level category names from the category structure section. These are the catalog's own category names (e.g., "Riga Wood"), not taxonomy categories. |
| `subcategories` | Generator input + catalog assessment | Per-subcategory map. Each entry has `core_attributes` (from `core_attribute_keys`), `extended_attributes` (from `extended_attribute_keys`), and `expected_count` (from catalog assessment category tree). Only attributes the scraper actually extracts. |
| `type_map` | Generator input + scraper source | Merge `attribute_types` from all subcategories in `generator_input.json` into a flat map. Values are already in eval format: `"str"`, `"number"`, `"list"`, `"bool"`. For extra attributes not in the generator input, inspect the scraper source. |
| `enum_attributes` | Scraper source | Maps attributes that have a closed set of allowed values to their value arrays. Only include attributes where the allowed values are clearly enumerable from the scraper logic. Use an empty object `{}` when no enum constraints apply. |
| `has_prices` | Catalog assessment + scraper source | `true` if the catalog has prices and the scraper extracts them, `false` otherwise. When `false`, the shared eval script skips the price sanity check. |
| `semantic_validation` | Generator input | Object with `numeric_fields` array. Derived from `attribute_types` — include all attributes where the type is `"number"`. Also include attributes that have entries in `units` (these are measurement fields). |

### Checks (13 total)

See `references/checks.md` for the full check reference — summary table, implementation details, weight redistribution, and self-verification checklist.

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Valid JSON** | Single JSON object, parseable | Trailing commas, comments, multiple objects |
| **All required fields present** | Every field from the schema above | Missing fields, extra fields |
| **`company_slug` is a string** | `"finieris"` | Missing or numeric |
| **`expected_product_count` is a positive integer** | `31` | `0`, negative, string, float |
| **`expected_top_level_categories` is a non-empty array of strings** | `["Riga Wood"]` | Empty array, array of numbers |
| **`subcategories` must be an object where each key is a taxonomy ID (contains dot)** | `{"wood.softwood_hardwood_lumber": {...}}` | Array, flat attributes, keys without dots |
| **Each subcategory value must have `core_attributes` (array), `extended_attributes` (array), and `expected_count` (number)** | `{"core_attributes": ["material"], "extended_attributes": ["color"], "expected_count": 200}` | Missing fields, wrong types |
| **`semantic_validation` is optional, when present it must be an object with `numeric_fields` array** | `{"numeric_fields": ["width", "thickness"]}` | String, array, missing numeric_fields key |
| **`type_map` values use exact type strings** | `"str"`, `"number"`, `"list"`, `"bool"` | `"string"`, `"int"`, `"float"`, `"array"`, `"boolean"` |
| **`type_map` covers all attributes across all subcategories** | Every core and extended attribute from all subcategories has a type entry | Attribute missing from type_map |
| **`enum_attributes` values are arrays of strings** | `{"surface_treatment": ["Uncoated", "Film-faced"]}` | Values as a single string, nested objects |
| **`has_prices` is a boolean** | `true` or `false` | `"true"`, `"false"`, `0`, `1` |

---

## Step 5: Run Eval Script

Run the eval script with `--collect` to validate the config end-to-end:

```
uv run .claude/skills/eval-generator/scripts/eval_run.py docs/eval-generator/{slug}/eval_config.json --collect
```

`--collect` runs the scraper to collect a per-subcategory sample (20% of capacity, max 100 per subcategory), then scores the output against the config. Products are written to `docs/eval-generator/{slug}/output/products.jsonl`. This is the only way to verify the config actually works — a dry run without products proves nothing.

If the eval fails or produces unexpected results, review the config for these common problems:

- Attribute names in `type_map` do not match what the scraper actually writes — cross-check against the scraper source.
- `expected_top_level_categories` values do not match the category names the scraper uses in `category_path` — compare with actual scraper output.

---

## Step 6: Self-Verification

After the run completes, read the eval result file and verify all 13 checks appear in the output. Use the self-verification checklist in `references/checks.md`.

If the eval runs successfully and all 13 checks appear in the result, the config is verified.

---

## Boundaries

- This workflow generates eval config files only — it does not modify the shared eval script or scraper code.
- It does not trigger rediscovery — the shared eval script sets `recommend_rediscovery` based on the degradation score.
- It does not define or modify the product taxonomy or SKU schemas.
- Mandatory core attribute checks (`sku`, `name`, `url`, `price`, `currency`, `brand`, `scraped_at`) are hardcoded in the shared eval script. The config only controls category-specific attribute expectations.

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
