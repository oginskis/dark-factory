# Eval Checks

**Input:** Products (JSONL), eval config, run summary, eval history, baseline
**Output:** Eval result with 13 weighted check scores (weights sum to 100), degradation score, pass/degraded/fail status

---

## Summary

| Check | Weight | Threshold | What it catches |
|-------|--------|-----------|-----------------|
| `core_attribute_coverage` | 20 | 0.90 | Core attributes missing — selector changes, schema drift |
| `extended_attribute_coverage` | 5 | 0.90 | Extended attributes missing — tracked with high overall threshold |
| `pagination_completeness` | 10 | 0.70 | Broken pagination, removed categories |
| `category_diversity` | 5 | 0.50 | Broken category traversal, sitemap gaps |
| `category_classification` | 10 | 0.95 | Products with invalid `product_category` — note: `product_category` is validated by this dedicated check, not by `core_attribute_coverage` |
| `price_sanity` | 10 | 1.00 | Parser errors, currency confusion |
| `data_freshness` | 5 | 1.00 | Stale cache, broken upsert |
| `schema_conformance` | 5 | 1.00 | Site redesign, new data format |
| `row_count_trend` | 5 | 0.80 | Category removal, pagination break |
| `duplicate_detection` | 5 | 0.99 | Duplicate products by SKU |
| `field_level_regression` | 10 | 0.50 | Per-field fill rate drops vs previous run |
| `extra_attributes_ratio` | 5 | 0.50 | Too many unmapped attributes — schema inadequate |
| `semantic_validation` | 5 | 0.95 | Composite: value cleanliness, non-product detection, numeric format, embedded units |

## Check implementation details

**core_attribute_coverage** (weight 20, threshold 0.90): Count how many core schema attributes are present and non-empty in `core_attributes`. Compute per-product coverage, measure fraction of products at or above 75%. Threshold: 0.90 (90% of products must have >=75% of core attributes filled). Core attributes receive the highest weight because scrapers are expected to put high effort into extracting them — they define what makes a product identifiable and comparable.

**extended_attribute_coverage** (weight 5, threshold 0.90): Same logic as core but applied to `extended_attributes`. Threshold: 0.90 (90% of products must have >50% of extended attributes filled). Lower weight reflects secondary importance, but the high overall threshold ensures consistent extraction. Skipped when `extended_attributes` list is empty.

**pagination_completeness** (weight 10, threshold 0.70): Compares actual product count to `expected_product_count`. Skipped on limited runs.

**category_diversity** (weight 5, threshold 0.50): Checks that scraped products span the `expected_top_level_categories`. Skipped on limited runs.

**category_classification** (weight 10, threshold 0.95): Count products where `product_category` is not `_unclassified` and is a valid taxonomy ID. Ratio must be >= 0.95. Skipped on limited runs.

**price_sanity** (weight 10, threshold 1.00): Validates price values are positive numbers with valid currency codes. Skipped when `has_prices` is false.

**data_freshness** (weight 5, threshold 1.00): Checks `scraped_at` timestamps are recent (within expected window).

**schema_conformance** (weight 5, threshold 1.00): Validates attribute types match `type_map` and enum values match `enum_attributes`. Attributes not in `type_map` get basic sanity checks (must be primitive, non-empty, no HTML).

**row_count_trend** (weight 5, threshold 0.80): Compares current row count to previous run baseline. Skipped on first run or limited runs.

**duplicate_detection** (weight 5, threshold 0.99): Checks for duplicate products by SKU. Ratio of unique SKUs to total must be >= 0.99.

**field_level_regression** (weight 10, threshold 0.50): Compares per-field fill rates against previous run baseline. Flags fields where fill rate dropped significantly. Skipped when no baseline exists.

**extra_attributes_ratio** (weight 5, threshold 0.50): Computes `1 - (extra_count / (core_count + extended_count))` averaged across all products. Higher is better (fewer unmapped extras). Threshold: 0.50. This flags schemas that are inadequate for the company.

**semantic_validation** (weight 5, threshold 0.95): Composite check (4 sub-checks, score = min of all sub-check scores). Always runs — never skipped. Sub-checks: (1) value cleanliness — detects HTML, control chars, overlong values; (2) non-product detection — flags navigation pages and empty records; (3) numeric field format — validates fields listed in `semantic_validation.numeric_fields` (conditional on config); (4) embedded-units detection — scans all attribute buckets for values with embedded units (e.g., "18mm", "5kg") that should be in `attribute_units` instead.

## Weight redistribution

When checks are skipped (e.g., no baseline for `field_level_regression`, limited run for `pagination_completeness`, empty `extended_attributes` for `extended_attribute_coverage`), their weights are redistributed proportionally among the remaining active checks. This ensures the total always sums to 100.

## Self-verification checklist

After a run completes, verify all 13 checks appear in the eval result:

| # | Check name | Verify |
|---|------------|--------|
| 1 | `core_attribute_coverage` | Present, weight 20, threshold 0.90 |
| 2 | `extended_attribute_coverage` | Present, weight 5, threshold 0.90 (or skipped when extended_attributes is empty) |
| 3 | `pagination_completeness` | Present, weight 10, threshold 0.70 (or skipped on limited run) |
| 4 | `category_diversity` | Present, weight 5, threshold 0.50 (or skipped on limited run) |
| 5 | `category_classification` | Present, weight 10, threshold 0.95 (or skipped on limited run) |
| 6 | `price_sanity` | Present, weight 10, threshold 1.0 (or skipped if `has_prices` is false) |
| 7 | `data_freshness` | Present, weight 5, threshold 1.0 |
| 8 | `schema_conformance` | Present, weight 5, threshold 1.0 |
| 9 | `row_count_trend` | Present, weight 5, threshold 0.80 (or skipped on limited/first run) |
| 10 | `duplicate_detection` | Present, weight 5, threshold 0.99 |
| 11 | `field_level_regression` | Present, weight 10, threshold 0.50 (or skipped if no baseline) |
| 12 | `extra_attributes_ratio` | Present, weight 5, threshold 0.50 |
| 13 | `semantic_validation` | Present, weight 5, threshold 0.95 (always runs — 4 sub-checks: cleanliness, non-product, numeric format, embedded units) |

Skipped checks have `"value": null` and `"skipped": true` — this is expected behavior, not an error.
