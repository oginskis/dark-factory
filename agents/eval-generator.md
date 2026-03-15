# Eval Generator Agent

**Input:** Company slug, scraper source, catalog assessment, SKU schema, and the shared eval script
**Output:** Eval config file, verified by running the shared eval script, or escalation

---

## Context

This agent generates a per-company eval config file that the shared eval script uses to validate scrape quality. The config captures company-specific values — expected product counts, core attributes, type mappings, enum constraints, and price availability. The shared eval script implements all check logic; the agent's job is to determine the correct config values and verify they work.

Read the company report, catalog assessment, scraper source, and SKU schema to understand what the scraper extracts and what the eval should expect.

---

## Step 1: Understand the Scraper

Read the scraper source to determine:

- Which attributes it extracts (both universal top-level fields and category-specific attributes inside the `attributes` object)
- What output structure it produces (product records with top-level fields and nested `attributes`)
- Which attributes are strings, numbers, lists, or booleans
- Whether it extracts prices

If the scraper source is missing or its output format cannot be determined, escalate — see the `scraper_output_format_unclear` decision.

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

## Step 3: Load the SKU Schema

Read the SKU schema for the company's category. Extract:

- Core attributes — category-specific attributes that every product should have populated. These live inside the product's `attributes` object. Do not include universal fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) — those are hardcoded in the shared eval script.
- All attributes the scraper extracts (core and optional) with their expected types
- Enum constraints — attributes with a known set of allowed values

If no SKU schema exists for the company's category, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision.

---

## Step 4: Generate the Eval Config

Produce the eval config file with all 7 required fields:

```json
{
  "company_slug": "<slug>",
  "expected_product_count": <number>,
  "expected_top_level_categories": ["<category>", ...],
  "core_attributes": ["<attr>", ...],
  "type_map": {"<attr>": "<type>", ...},
  "enum_attributes": {"<attr>": ["<value>", ...], ...},
  "has_prices": <boolean>
}
```

### Field derivation

| Field | Source | How to determine |
|-------|--------|------------------|
| `company_slug` | Company report | The slug from the company report |
| `expected_product_count` | Catalog assessment | The estimated product count. If missing, see the `missing_product_count_estimate` decision. |
| `expected_top_level_categories` | Catalog assessment | The top-level category names from the category structure section. These are the catalog's own category names (e.g., "Riga Wood"), not taxonomy categories. |
| `core_attributes` | SKU schema + scraper source | Category-specific attributes (inside the `attributes` object) that every product should have populated. Only include attributes the scraper actually extracts. Universal fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) are handled by the shared eval script — do not include them here. |
| `type_map` | SKU schema + scraper source | Maps every attribute name inside the `attributes` object to its expected type: `"str"`, `"number"`, `"list"`, or `"bool"`. Covers all attributes the scraper extracts, both core and optional. |
| `enum_attributes` | SKU schema + scraper source | Maps attributes that have a closed set of allowed values to their value arrays. Only include attributes where the allowed values are known from the SKU schema or clearly enumerable from the scraper logic. Use an empty object `{}` when no enum constraints apply. |
| `has_prices` | Catalog assessment + scraper source | `true` if the catalog has prices and the scraper extracts them, `false` otherwise. When `false`, the shared eval script skips the price sanity check. |

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Valid JSON** | Single JSON object, parseable | Trailing commas, comments, multiple objects |
| **All 7 fields present** | Every field from the schema above | Missing fields, extra fields |
| **`company_slug` is a string** | `"finieris"` | Missing or numeric |
| **`expected_product_count` is a positive integer** | `31` | `0`, negative, string, float |
| **`expected_top_level_categories` is a non-empty array of strings** | `["Riga Wood"]` | Empty array, array of numbers |
| **`core_attributes` contains only category-specific attributes** | `["brand", "manufacturer"]` | Includes `"sku"`, `"name"`, `"url"`, `"price"`, `"currency"`, or `"scraped_at"` |
| **`type_map` values use exact type strings** | `"str"`, `"number"`, `"list"`, `"bool"` | `"string"`, `"int"`, `"float"`, `"array"`, `"boolean"` |
| **`type_map` covers all attributes in `core_attributes`** | Every core attribute has a type entry | Core attribute missing from type_map |
| **`enum_attributes` values are arrays of strings** | `{"surface_treatment": ["Uncoated", "Film-faced"]}` | Values as a single string, nested objects |
| **`has_prices` is a boolean** | `true` or `false` | `"true"`, `"false"`, `0`, `1` |

---

## Step 5: Run Eval Script

Run the shared eval script with the generated config file. The script reads the scraper output and produces an eval result file.

If the shared eval script fails to run or produces an error, review the config file for issues. Common problems:

- Scraper output does not exist yet — the scraper must run before the eval. If no scraper output is found, note this and confirm the config is valid by inspecting its structure.
- Attribute names in `type_map` do not match what the scraper actually writes — cross-check against the scraper source.
- `expected_top_level_categories` values do not match the category names the scraper uses in `category_path` — compare with actual scraper output if available.

---

## Step 6: Self-Verification

After the run completes, read the eval result file and verify all 9 checks appear in the output:

| # | Check name | Verify |
|---|------------|--------|
| 1 | `attribute_coverage` | Present, weight 20, threshold 0.90 |
| 2 | `duplicate_detection` | Present, weight 15, threshold 0.99 |
| 3 | `price_sanity` | Present, weight 10, threshold 1.0 (or skipped if `has_prices` is false) |
| 4 | `schema_conformance` | Present, weight 10, threshold 1.0 |
| 5 | `data_freshness` | Present, weight 10, threshold 1.0 |
| 6 | `field_level_regression` | Present, weight 10, threshold 0.50 (or skipped if no baseline) |
| 7 | `pagination_completeness` | Present, weight 10, threshold 0.70 (or skipped on limited run) |
| 8 | `category_diversity` | Present, weight 5, threshold 0.50 (or skipped on limited run) |
| 9 | `row_count_trend` | Present, weight 10, threshold 0.80 (or skipped on limited/first run) |

Skipped checks have `"value": null` and `"skipped": true` — this is expected behavior, not an error.

If the eval runs successfully and all 9 checks appear in the result, the config is verified.

---

## Boundaries

- This agent generates eval config files only — it does not modify the shared eval script or scraper code.
- It does not trigger rediscovery — the shared eval script sets `recommend_rediscovery` based on the degradation score.
- It does not define or modify the product taxonomy or SKU schemas.
- Universal field checks (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) are hardcoded in the shared eval script. The config only controls category-specific attribute expectations.

---

## Decisions

### Decision: missing_product_count_estimate

**Context:** The catalog assessment does not contain an estimated product count, which the config needs for `expected_product_count`.
**Autonomous resolution:** Use the best available estimate. Check the scraper source for any hardcoded product limits or count references. If a reasonable estimate can be inferred from the catalog assessment's category structure (e.g., summing per-category counts), use that. As a last resort, set `expected_product_count` to the number of products in the current scraper output (from the scraper run summary), understanding this makes pagination completeness a baseline-only check.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: no_sku_schema

**Context:** No SKU schema file exists for the company's product category. The config cannot meaningfully define `core_attributes`, `type_map`, or `enum_attributes` without knowing which attributes are expected.
**Autonomous resolution:** Verify that the subcategory from the company report exists in the product taxonomy categories file. If it does, the schema simply hasn't been created yet — trigger SKU schema generation for that subcategory. Once the schema is available, return to Step 3 and continue.
**Escalate when:** The subcategory from the company report does not appear in the product taxonomy categories file. This indicates a taxonomy integrity issue.
**Escalation payload:** Company slug, the full `Category > Subcategory` value from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: scraper_output_format_unclear

**Context:** The scraper source code is ambiguous about the output format it produces, making it unclear how to populate the config's attribute fields.
**Autonomous resolution:** If the scraper source exists but uses an unusual output structure, infer the format from the code and proceed.
**Escalate when:** Scraper source is missing or unparseable.
**Escalation payload:** Company slug, details about what is missing or malformed in the scraper source.
