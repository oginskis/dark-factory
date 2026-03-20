# Eval Conditions

## Config format rules

The `eval_config.json` must conform to these rules:

| Rule | Correct | Wrong |
|------|---------|-------|
| **Valid JSON** | Single JSON object, parseable | Trailing commas, comments, multiple objects |
| **All required fields present** | Every field from the schema in workflow.md Step 4 | Missing fields, extra fields |
| **`company_slug` is a string** | `"finieris"` | Missing or numeric |
| **`expected_product_count` is a positive integer** | `31` | `0`, negative, string, float |
| **`expected_top_level_categories` is a non-empty array of strings** | `["Riga Wood"]` | Empty array, array of numbers |
| **`subcategories` keys are taxonomy IDs (contain dot)** | `{"wood.softwood_hardwood_lumber": {...}}` | Array, flat attributes, keys without dots |
| **Each subcategory has `core_attributes`, `extended_attributes`, `expected_count`** | `{"core_attributes": ["material"], "extended_attributes": ["color"], "expected_count": 200}` | Missing fields, wrong types |
| **`semantic_validation` is optional; when present, must have `numeric_fields` array** | `{"numeric_fields": ["width", "thickness"]}` | String, array, missing numeric_fields key |
| **`type_map` values use exact type strings** | `"str"`, `"number"`, `"list"`, `"bool"` | `"string"`, `"int"`, `"float"`, `"array"`, `"boolean"` |
| **`type_map` covers all attributes across all subcategories** | Every core and extended attribute has a type entry | Attribute missing from type_map |
| **`enum_attributes` values are arrays of strings** | `{"surface_treatment": ["Uncoated", "Film-faced"]}` | Values as a single string, nested objects |
| **`has_prices` is a boolean** | `true` or `false` | `"true"`, `"false"`, `0`, `1` |

## Collection strategy

How many products to scrape for eval verification:

- **Per subcategory:** 20% of `expected_count`, minimum 10, maximum 100
- **All subcategories must be covered** — every subcategory in the eval config gets its own sample
- **Total:** sum of per-subcategory samples (no separate total cap)
- **Single-subcategory fallback:** 20% of `expected_product_count`, minimum 10, maximum 100

### Single-subcategory companies

One invocation with the total sample size:

```
uv run docs/scraper-generator/{slug}/scraper.py --limit <total> --output-file docs/eval-generator/{slug}/output/products.jsonl --summary-file docs/eval-generator/{slug}/output/summary.json --log-file docs/eval-generator/{slug}/output/debug.log
```

### Multi-subcategory companies

One invocation per subcategory. Get category keys by inverting the scraper's `docs/scraper-generator/{slug}/config.json` `category_mapping` (URL prefix → taxonomy ID) to (taxonomy ID → URL prefixes). Then run for each subcategory using `--categories` and `--append`:

```
uv run docs/scraper-generator/{slug}/scraper.py --categories <keys> --limit <per_sub_limit> --output-file docs/eval-generator/{slug}/output/products.jsonl --summary-file docs/eval-generator/{slug}/output/summary.json --log-file docs/eval-generator/{slug}/output/debug.log --append
```

`--append` adds products to the existing file instead of overwriting. Run this for each subcategory so all are covered in one `products.jsonl`.

## Quality checks

Thirteen weighted checks (weights sum to 100):

| Check | Weight | Threshold | What it catches |
|-------|--------|-----------|-----------------|
| `core_attribute_coverage` | 20 | 0.90 | Core attributes missing — selector changes, schema drift |
| `extended_attribute_coverage` | 5 | 0.90 | Extended attributes missing — tracked with high overall threshold |
| `pagination_completeness` | 10 | 0.70 | Broken pagination, removed categories |
| `category_diversity` | 5 | 0.50 | Broken category traversal, sitemap gaps |
| `category_classification` | 10 | 0.95 | Products with invalid `product_category` |
| `price_sanity` | 10 | 1.00 | Parser errors, currency confusion |
| `data_freshness` | 5 | 1.00 | Stale cache, broken upsert |
| `schema_conformance` | 5 | 1.00 | Site redesign, new data format |
| `row_count_trend` | 5 | 0.80 | Category removal, pagination break |
| `duplicate_detection` | 5 | 0.99 | Duplicate products by SKU |
| `field_level_regression` | 10 | 0.50 | Per-field fill rate drops vs previous run |
| `extra_attributes_ratio` | 5 | 0.50 | Too many unmapped attributes — schema inadequate |
| `semantic_validation` | 5 | 0.95 | Dirty values, embedded units, non-products |

## Check details

**core_attribute_coverage** (weight 20, threshold 0.90): Per-product coverage of mandatory core fields + subcategory core attributes. A product passes if >=75% are populated. Overall score: fraction of products passing. Highest weight — core attributes define what makes a product identifiable.

**extended_attribute_coverage** (weight 5, threshold 0.90): Same logic applied to `extended_attributes`, per-product threshold >50%. Skipped when `extended_attributes` list is empty.

**pagination_completeness** (weight 10, threshold 0.70): Ratio of actual to expected product count. Skipped on limited/sampled runs.

**category_diversity** (weight 5, threshold 0.50): Set intersection of actual vs expected top-level categories. Skipped on limited runs.

**category_classification** (weight 10, threshold 0.95): Fraction of products with a valid taxonomy ID in `product_category`. Skipped on limited runs.

**price_sanity** (weight 10, threshold 1.00): Fraction of priced products with sane values (positive, within 10x median). Skipped when `has_prices` is false.

**data_freshness** (weight 5, threshold 1.00): Fraction of products with `scraped_at` within last 24 hours.

**schema_conformance** (weight 5, threshold 1.00): Fraction of attribute values matching `type_map` types and `enum_attributes` constraints. Attributes not in `type_map` get basic sanity checks (primitive, non-empty, no HTML).

**row_count_trend** (weight 5, threshold 0.80): Ratio of current to previous product count. Skipped on first run or limited runs.

**duplicate_detection** (weight 5, threshold 0.99): Ratio of unique SKUs to total.

**field_level_regression** (weight 10, threshold 0.50): Fraction of core attributes whose fill rate hasn't dropped >50% vs baseline. Skipped when no baseline exists.

**extra_attributes_ratio** (weight 5, threshold 0.50): Average of `1 - (extra_count / mapped_count)` across products. Flags schemas that are inadequate for the company.

**semantic_validation** (weight 5, threshold 0.95): Composite of 4 sub-checks (score = min). Always runs. (1) Value cleanliness — HTML, control chars, overlong values. (2) Non-product detection — navigation pages, empty records. (3) Numeric field format — validates `semantic_validation.numeric_fields` (conditional on config). (4) Embedded-units detection — flags values like "18mm", "5kg" that should be in `attribute_units`.

## Scoring

Checks that can't run (no baseline, limited sample, no prices, empty extended_attributes) are skipped. Their weights redistribute proportionally among active checks so the total always sums to 100.

| Degradation score | Status | Action |
|-------------------|--------|--------|
| 0–30 | `pass` | No action |
| 31–60 | `degraded` | Review scraper output |
| 61–100 | `fail` | Re-run pipeline |

Three consecutive `degraded` runs or any `fail` sets `recommend_rediscovery: true`.

If fewer than 3 checks can run, status is `insufficient_data`.

## Self-verification checklist

After a run completes, verify all 13 checks appear in `eval_result.json`:

| # | Check name | Verify |
|---|------------|--------|
| 1 | `core_attribute_coverage` | Present, weight 20, threshold 0.90 |
| 2 | `extended_attribute_coverage` | Present, weight 5, threshold 0.90 (or skipped) |
| 3 | `pagination_completeness` | Present, weight 10, threshold 0.70 (or skipped) |
| 4 | `category_diversity` | Present, weight 5, threshold 0.50 (or skipped) |
| 5 | `category_classification` | Present, weight 10, threshold 0.95 (or skipped) |
| 6 | `price_sanity` | Present, weight 10, threshold 1.0 (or skipped) |
| 7 | `data_freshness` | Present, weight 5, threshold 1.0 |
| 8 | `schema_conformance` | Present, weight 5, threshold 1.0 |
| 9 | `row_count_trend` | Present, weight 5, threshold 0.80 (or skipped) |
| 10 | `duplicate_detection` | Present, weight 5, threshold 0.99 |
| 11 | `field_level_regression` | Present, weight 10, threshold 0.50 (or skipped) |
| 12 | `extra_attributes_ratio` | Present, weight 5, threshold 0.50 |
| 13 | `semantic_validation` | Present, weight 5, threshold 0.95 (always runs) |

Skipped checks have `"value": null` and `"skipped": true` — expected behavior, not an error.
