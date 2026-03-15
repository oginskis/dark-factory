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

- Which attributes it extracts (both universal top-level fields and category-specific attributes)
- What output format the scraper produces — v1 (flat `attributes` object) or v2 (`_format: 2` with `core_attributes`, `extended_attributes`, `extra_attributes`)
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

- Core attributes — category-specific attributes that every product must have populated. In v2 format these live inside `core_attributes`; in v1 format they are inside the flat `attributes` object. Do not include universal fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) — those are hardcoded in the shared eval script.
- Extended attributes — additional category-specific attributes that are useful but not mandatory. In v2 format these live inside `extended_attributes`.
- All attributes the scraper extracts (core, extended, and extra) with their expected types
- Enum constraints — attributes with a known set of allowed values

If no SKU schema exists for the company's category, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision.

---

## Step 4: Generate the Eval Config

Produce the eval config file with all 9 required fields:

```json
{
  "company_slug": "<slug>",
  "expected_product_count": <number>,
  "expected_top_level_categories": ["<category>", ...],
  "core_attributes": ["<attr>", ...],
  "extended_attributes": ["<attr>", ...],
  "type_map": {"<attr>": "<type>", ...},
  "enum_attributes": {"<attr>": ["<value>", ...], ...},
  "has_prices": <boolean>,
  "output_format": <1 or 2>
}
```

### Field derivation

| Field | Source | How to determine |
|-------|--------|------------------|
| `company_slug` | Company report | The slug from the company report |
| `expected_product_count` | Catalog assessment | The estimated product count. If missing, see the `missing_product_count_estimate` decision. |
| `expected_top_level_categories` | Catalog assessment | The top-level category names from the category structure section. These are the catalog's own category names (e.g., "Riga Wood"), not taxonomy categories. |
| `core_attributes` | SKU schema + scraper source | Category-specific attributes that every product must have populated. In v2 these come from `core_attributes`; in v1 these are the mandatory subset of the flat `attributes` object. Only include attributes the scraper actually extracts. Universal fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) are handled by the shared eval script — do not include them here. |
| `extended_attributes` | SKU schema + scraper source | Additional category-specific attributes that are useful but not mandatory. In v2 these come from `extended_attributes`. For v1 scrapers, set to an empty array `[]`. |
| `type_map` | SKU schema + scraper source | Maps every attribute name (across core, extended, and extra) to its expected type: `"str"`, `"number"`, `"list"`, or `"bool"`. Covers all attributes the scraper extracts. |
| `enum_attributes` | SKU schema + scraper source | Maps attributes that have a closed set of allowed values to their value arrays. Only include attributes where the allowed values are known from the SKU schema or clearly enumerable from the scraper logic. Use an empty object `{}` when no enum constraints apply. |
| `has_prices` | Catalog assessment + scraper source | `true` if the catalog has prices and the scraper extracts them, `false` otherwise. When `false`, the shared eval script skips the price sanity check. |
| `output_format` | Scraper source | `2` if the scraper writes v2 records (with `_format: 2`, `core_attributes`, `extended_attributes`, `extra_attributes`). `1` if the scraper writes v1 records (flat `attributes` object). |

### v1/v2 format handling

The eval script supports two scraper output formats:

- **v1** (no `_format` field): Products have a flat `attributes` dict. The eval applies a single `attribute_coverage` check that treats all attributes as one bucket. The `extended_attribute_coverage` and `extra_attributes_ratio` checks are skipped. Set `output_format` to `1` and `extended_attributes` to `[]`.
- **v2** (`_format: 2`): Products have `core_attributes`, `extended_attributes`, and `extra_attributes` dicts. The eval applies the split checks: `core_attribute_coverage` (on `core_attributes`), `extended_attribute_coverage` (on `extended_attributes`), and `extra_attributes_ratio` (on `extra_attributes` relative to core + extended counts). Set `output_format` to `2`.

When reading scraper output, detect the format from the first record. If `_format` is present and equals `2`, use v2 logic; otherwise use v1 logic.

### Checks (12 total)

The shared eval script implements 12 weighted checks. Weights sum to 100:

| Check | Weight | Threshold | What it catches |
|-------|--------|-----------|-----------------|
| `core_attribute_coverage` | 20 | 0.90 | Core attributes missing — selector changes, schema drift |
| `extended_attribute_coverage` | 5 | 0.50 | Extended attributes missing — less critical but tracked |
| `pagination_completeness` | 10 | 0.70 | Broken pagination, removed categories |
| `category_diversity` | 5 | 0.50 | Broken category traversal, sitemap gaps |
| `category_classification` | 10 | 0.95 | Products with `_unclassified` product_category |
| `price_sanity` | 10 | 1.00 | Parser errors, currency confusion |
| `data_freshness` | 5 | 1.00 | Stale cache, broken upsert |
| `schema_conformance` | 5 | 1.00 | Site redesign, new data format |
| `row_count_trend` | 5 | 0.80 | Category removal, pagination break |
| `duplicate_detection` | 10 | 0.99 | Duplicate products by SKU |
| `field_level_regression` | 10 | 0.50 | Per-field fill rate drops vs previous run |
| `extra_attributes_ratio` | 5 | 0.50 | Too many unmapped attributes — schema inadequate |

### Check implementation details

**core_attribute_coverage** (weight 20, threshold 0.90): For v2 format records, count how many core schema attributes are present and non-empty in `core_attributes`. Compute per-product coverage, measure fraction of products above 80%. For v1 format, this check uses the flat `attributes` dict with the `core_attributes` list from config. Threshold: 0.90 (90% of products must have >80% of core attributes filled).

**extended_attribute_coverage** (weight 5, threshold 0.50): Same logic as core but applied to `extended_attributes`. Lighter threshold: 0.50 (50% of products must have >50% of extended attributes filled). Skipped for v1 format.

**pagination_completeness** (weight 10, threshold 0.70): Compares actual product count to `expected_product_count`. Skipped on limited runs.

**category_diversity** (weight 5, threshold 0.50): Checks that scraped products span the `expected_top_level_categories`. Skipped on limited runs.

**category_classification** (weight 10, threshold 0.95): Count products where `product_category` is not `_unclassified` and is a valid taxonomy ID. Ratio must be >= 0.95. Skipped on limited runs.

**price_sanity** (weight 10, threshold 1.00): Validates price values are positive numbers with valid currency codes. Skipped when `has_prices` is false.

**data_freshness** (weight 5, threshold 1.00): Checks `scraped_at` timestamps are recent (within expected window).

**schema_conformance** (weight 5, threshold 1.00): Validates attribute types match `type_map` and enum values match `enum_attributes`.

**row_count_trend** (weight 5, threshold 0.80): Compares current row count to previous run baseline. Skipped on first run or limited runs.

**duplicate_detection** (weight 10, threshold 0.99): Checks for duplicate products by SKU. Ratio of unique SKUs to total must be >= 0.99.

**field_level_regression** (weight 10, threshold 0.50): Compares per-field fill rates against previous run baseline. Flags fields where fill rate dropped significantly. Skipped when no baseline exists.

**extra_attributes_ratio** (weight 5, threshold 0.50): Computes `1 - (extra_count / (core_count + extended_count))` averaged across all products. Higher is better (fewer unmapped extras). Threshold: 0.50. This flags schemas that are inadequate for the company. Skipped for v1 format.

### Weight redistribution

When checks are skipped (e.g., no baseline for `field_level_regression`, limited run for `pagination_completeness`, v1 format for `extended_attribute_coverage`), their weights are redistributed proportionally among the remaining active checks. This ensures the total always sums to 100.

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Valid JSON** | Single JSON object, parseable | Trailing commas, comments, multiple objects |
| **All 9 fields present** | Every field from the schema above | Missing fields, extra fields |
| **`company_slug` is a string** | `"finieris"` | Missing or numeric |
| **`expected_product_count` is a positive integer** | `31` | `0`, negative, string, float |
| **`expected_top_level_categories` is a non-empty array of strings** | `["Riga Wood"]` | Empty array, array of numbers |
| **`core_attributes` contains only category-specific attributes** | `["brand", "manufacturer"]` | Includes `"sku"`, `"name"`, `"url"`, `"price"`, `"currency"`, or `"scraped_at"` |
| **`extended_attributes` is an array of strings** | `["color", "finish"]` or `[]` | Missing, null, array of numbers |
| **`type_map` values use exact type strings** | `"str"`, `"number"`, `"list"`, `"bool"` | `"string"`, `"int"`, `"float"`, `"array"`, `"boolean"` |
| **`type_map` covers all attributes in `core_attributes` and `extended_attributes`** | Every core and extended attribute has a type entry | Attribute missing from type_map |
| **`enum_attributes` values are arrays of strings** | `{"surface_treatment": ["Uncoated", "Film-faced"]}` | Values as a single string, nested objects |
| **`has_prices` is a boolean** | `true` or `false` | `"true"`, `"false"`, `0`, `1` |
| **`output_format` is 1 or 2** | `1` or `2` | `"1"`, `"v2"`, missing |

---

## Step 5: Run Eval Script

Run the shared eval script with the generated config file. The script reads the scraper output and produces an eval result file.

If the shared eval script fails to run or produces an error, review the config file for issues. Common problems:

- Scraper output does not exist yet — the scraper must run before the eval. If no scraper output is found, note this and confirm the config is valid by inspecting its structure.
- Attribute names in `type_map` do not match what the scraper actually writes — cross-check against the scraper source.
- `expected_top_level_categories` values do not match the category names the scraper uses in `category_path` — compare with actual scraper output if available.

---

## Step 6: Self-Verification

After the run completes, read the eval result file and verify all 12 checks appear in the output:

| # | Check name | Verify |
|---|------------|--------|
| 1 | `core_attribute_coverage` | Present, weight 20, threshold 0.90 |
| 2 | `extended_attribute_coverage` | Present, weight 5, threshold 0.50 (or skipped for v1 format) |
| 3 | `pagination_completeness` | Present, weight 10, threshold 0.70 (or skipped on limited run) |
| 4 | `category_diversity` | Present, weight 5, threshold 0.50 (or skipped on limited run) |
| 5 | `category_classification` | Present, weight 10, threshold 0.95 (or skipped on limited run) |
| 6 | `price_sanity` | Present, weight 10, threshold 1.0 (or skipped if `has_prices` is false) |
| 7 | `data_freshness` | Present, weight 5, threshold 1.0 |
| 8 | `schema_conformance` | Present, weight 5, threshold 1.0 |
| 9 | `row_count_trend` | Present, weight 5, threshold 0.80 (or skipped on limited/first run) |
| 10 | `duplicate_detection` | Present, weight 10, threshold 0.99 |
| 11 | `field_level_regression` | Present, weight 10, threshold 0.50 (or skipped if no baseline) |
| 12 | `extra_attributes_ratio` | Present, weight 5, threshold 0.50 (or skipped for v1 format) |

Skipped checks have `"value": null` and `"skipped": true` — this is expected behavior, not an error.

If the eval runs successfully and all 12 checks appear in the result, the config is verified.

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
**Escalation payload:** Company slug, the taxonomy ID from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: scraper_output_format_unclear

**Context:** The scraper source code is ambiguous about the output format it produces, making it unclear how to populate the config's attribute fields.
**Autonomous resolution:** If the scraper source exists but uses an unusual output structure, infer the format from the code and proceed.
**Escalate when:** Scraper source is missing or unparseable.
**Escalation payload:** Company slug, details about what is missing or malformed in the scraper source.
