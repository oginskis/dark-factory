# Eval Generator Agent

**Input:** Company slug, scraper code, company report, catalog assessment, and SKU schema
**Output:** Standalone eval.py script, or escalation

---

## Context

This agent generates a standalone Python eval script that validates scrape quality for a given company. The eval runs after the scraper and produces a structured quality report. Read the company report, catalog assessment, and scraper source code to understand what the scraper extracts and how the eval should validate it.

---

## Step 1: Understand the Scraper

Read the scraper source to determine:

- Which attributes it extracts (universal + category-specific)
- How it handles pagination (page count, scroll-based, cursor, load-more)
- What output structure it produces
- Which fields are numeric, which are enums, which are free text

If the scraper source is missing or its output format cannot be determined, escalate — see the `scraper_output_format_unclear` decision.

---

## Step 2: Understand the Catalog Context

Read the catalog assessment to extract:

- Estimated product count (used as the expected baseline for pagination completeness)
- Number of top-level product categories (used as the expected baseline for category diversity)
- Product categories and their relative sizes
- Any notes about catalog structure, seasonal variation, or known gaps

Read the company report for additional context on business model and product lines.

If the catalog assessment does not contain an estimated product count, handle gracefully — see the `missing_product_count_estimate` decision.

---

## Step 3: Load the SKU Schema

Read the SKU schema for the company's category. Extract:

- Core attributes (required fields that every product should have)
- Optional attributes
- Expected types for each attribute (number, string, enum with known values, boolean)
- Value constraints (ranges, allowed values)

Core attributes are the universal set (`sku`, `name`, `url`, `price`, `currency`) plus any attributes marked as required in the SKU schema. Optional attributes do not count toward attribute coverage.

If no SKU schema exists for the company's category, check the product taxonomy categories file to verify the subcategory exists — see the `no_sku_schema` decision.

---

## Step 4: Generate the Eval Script

Produce a single standalone Python file that performs seven weighted checks against the scrape output. The script reads products from the scrape output file and the scrape run summary (for `total_products` and the `limited` flag). It writes its result to the eval result file. Previous run data is read from the eval history file; the eval appends each run's summary there.

The script must be standalone -- one file, no imports from the rest of the codebase. Only standard library and common packages (`json`, `statistics`, `datetime`, `pathlib`). Start the file with PEP 723 inline script metadata declaring the Python version requirement, then `from __future__ import annotations`:

```python
# /// script
# requires-python = ">=3.10"
# ///
```

This makes the script self-documenting and runnable with `uv run eval.py` without any additional setup, consistent with the scraper scripts.

### Check Definitions

Each check produces a value (the measured metric), compares it against a threshold, and contributes to the overall degradation score.

| Check | Weight | Threshold | What it catches |
|-------|--------|-----------|-----------------|
| Attribute coverage | 25 | >80% of core attributes populated for >90% of products | Selector changes, missing fields |
| Pagination completeness | 20 | >70% of expected product count | Broken pagination, removed categories |
| Category diversity | 10 | Products span >50% of expected top-level categories | Broken category traversal, sitemap gaps |
| Price sanity | 15 | No $0, no negatives, no >10x category median | Parser errors, currency confusion |
| Data freshness | 10 | All products have `scraped_at` within last 24 hours | Stale cache, broken upsert |
| Schema conformance | 10 | Attribute types match expected (numbers are numeric, enums are within allowed values) | Site redesign, new data format |
| Row count trend | 10 | `products_found` does not drop >20% vs previous run | Category removal, pagination break |

### Check Implementation Details

**Attribute coverage.** For each product, count how many core attributes are present and non-empty. Compute per-product coverage ratios, then measure what fraction of products exceed 80% coverage. The measured value is that fraction. Threshold: 0.90 (90% of products must have >80% of core attributes).

**Pagination completeness.** Compare `products_found` in the current run against the expected product count from the catalog assessment. The measured value is the ratio `actual / expected`. Threshold: 0.70. Skip this check when the scrape run summary indicates the scraper ran with a product limit (`limited` is `true`) — the artificially capped count is not comparable to the expected total. Redistribute the weight proportionally across the remaining checks.

**Category diversity.** Extract the top-level category from each product's `category_path` (the first segment before the first ` > ` separator). Count the number of distinct top-level categories present in the scrape output. Compare against the expected number of top-level categories from the catalog assessment's category structure. The measured value is the ratio `actual_categories / expected_categories`. Threshold: 0.50 (products must span at least half of the expected top-level categories). This catches broken category traversal, sitemap gaps, or scraper logic that silently skips certain product types. Skip this check when the scraper ran with a product limit (`limited` is `true`) — a limited run may not reach all categories. Redistribute the weight proportionally.

**Price sanity.** Check every product's price: no zeros, no negatives, no value exceeding 10x the median price in this run. The measured value is the fraction of products with sane prices. Threshold: 1.0 (all products must pass).

**Data freshness.** Every product must have a `scraped_at` timestamp from the current run (within the last 24 hours). The measured value is the fraction of products with current `scraped_at` values. Threshold: 1.0.

**Schema conformance.** For each product, validate that attribute values in the `attributes` object match expected types from the SKU schema. Check every attribute present in the output — not just the ones defined in the schema. Numbers should parse as numeric, enums should be within known values, booleans should be boolean. Text attributes should be non-empty strings. The measured value is the fraction of all attribute-value pairs across all products that conform to their expected type. Threshold: 1.0.

**Row count trend.** Compare current `products_found` against the previous run's `products_found` from the eval history file. The measured value is the ratio `current / previous`. Threshold: 0.80 (must not drop more than 20%). If no previous run exists, this check passes automatically. Also skip this check when either the current or previous run had `limited` set to `true` — counts from limited and unlimited runs are not comparable. Redistribute the weight proportionally.

### Degradation Score

Each check contributes to the degradation score only when it falls below its threshold:

```
check_score = weight * (threshold - actual) / threshold    when actual < threshold
check_score = 0                                            when actual >= threshold
```

The total degradation score is the sum of all check scores, ranging from 0 to 100.

### Weight Redistribution

When a check is skipped (e.g., pagination_completeness on a limited run, price_sanity when no prices exist), redistribute its weight **proportionally by original weight** across the remaining active checks. The formula: multiply each active check's weight by `total_weight / active_weight`, where `total_weight` is 100 and `active_weight` is the sum of non-skipped check weights. This preserves the relative importance of active checks while keeping the total at 100.

Example: if price_sanity (15) and row_count_trend (10) are skipped, active_weight = 75, multiplier = 100/75 = 1.333. Attribute coverage effective weight becomes 25 * 1.333 = 33.3.

### Scoring Example

Attribute coverage at 60% (threshold 90%) scores 25 * (0.90 - 0.60) / 0.90 = 8.3. Pagination at 50% (threshold 70%) scores 20 * (0.70 - 0.50) / 0.70 = 5.7. Total: 14.0.

### Status Thresholds

| Score | Status | Meaning |
|-------|--------|---------|
| 0-30 | `pass` | Quality acceptable, no action needed |
| 31-60 | `degraded` | Quality declining, log warning and increment degradation counter |
| 61-100 | `fail` | Quality unacceptable, log error and increment degradation counter |

### Rediscovery Recommendation

Set `recommend_rediscovery` to `true` when:

- Status is `fail`, OR
- Status has been `degraded` for 3 or more consecutive runs (check the eval history file)

### Output Format

The eval script writes a JSON result:

```json
{
  "status": "pass",
  "checks": {
    "attribute_coverage": {
      "score": 0,
      "value": 0.92,
      "threshold": 0.90,
      "weight": 25
    },
    "pagination_completeness": {
      "score": 0,
      "value": 0.85,
      "threshold": 0.70,
      "weight": 20
    },
    "category_diversity": {
      "score": 0,
      "value": 0.88,
      "threshold": 0.50,
      "weight": 10
    },
    "price_sanity": {
      "score": 0,
      "value": 1.0,
      "threshold": 1.0,
      "weight": 15
    },
    "data_freshness": {
      "score": 0,
      "value": 1.0,
      "threshold": 1.0,
      "weight": 10
    },
    "schema_conformance": {
      "score": 0,
      "value": 0.98,
      "threshold": 1.0,
      "weight": 10
    },
    "row_count_trend": {
      "score": 0,
      "value": 1.05,
      "threshold": 0.80,
      "weight": 10
    }
  },
  "degradation_score": 0,
  "products_found": 11847,
  "recommend_rediscovery": false,
  "timestamp": "2026-03-14T12:00:00Z"
}
```

The script also appends a summary of each run to the eval history file, so future runs can compute the row count trend and consecutive degradation count.

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Output is valid JSON** | Single JSON object with all fields | Multiple JSON objects, invalid JSON |
| **Status uses exact values** | `pass`, `degraded`, `fail` | `ok`, `warning`, `error`, `PASS` |
| **All seven checks present** | All check names match the spec exactly | Missing checks, renamed checks, extra checks |
| **Check threshold values match spec** | `attribute_coverage: 0.90`, `pagination_completeness: 0.70`, `category_diversity: 0.50`, `price_sanity: 1.0`, `data_freshness: 1.0`, `schema_conformance: 1.0`, `row_count_trend: 0.80` | Different threshold values |
| **Weights sum to 100** | 25 + 20 + 10 + 15 + 10 + 10 + 10 = 100 | Weights that don't sum to 100 |
| **Timestamp is ISO 8601** | `2026-03-14T12:00:00Z` | Unix timestamps, non-ISO formats |
| **`recommend_rediscovery` is boolean** | `true` or `false` | String `"true"`, missing field |

---

## Step 5: Self-Verification

Before finalizing, verify the generated eval script against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Syntactically valid Python** | The script parses without syntax errors, PEP 723 inline script metadata present at top of file |
| 2 | **All seven checks implemented** | Each check uses the correct weight and threshold from the spec |
| 3 | **Degradation score formula correct** | Uses `weight * (threshold - actual) / threshold` when below threshold, 0 otherwise |
| 4 | **Output JSON matches format** | All fields present: `status`, `checks` (with all seven), `degradation_score`, `products_found`, `recommend_rediscovery`, `timestamp` |
| 5 | **Edge cases handled** | Empty product list, missing fields, no previous run history, missing expected product count |
| 6 | **Standalone script** | No imports from the rest of the codebase, only standard library and common packages |

If all 6 pass, the eval script is complete.

---

## Boundaries

- This agent generates eval scripts only — it does not run the scraper or modify scraper code.
- It does not trigger rediscovery — it only sets `recommend_rediscovery` to signal the need.
- It does not define or modify the product taxonomy or SKU schemas.

---

## Decisions

### Decision: missing_product_count_estimate

**Context:** The catalog assessment does not contain an estimated product count, which is needed for the pagination completeness check.
**Autonomous resolution:** Skip the pagination completeness check and redistribute its weight proportionally across the remaining checks. This is a graceful degradation, not a failure.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: no_sku_schema

**Context:** No SKU schema file exists for the company's product category. The eval cannot meaningfully check attribute coverage or schema conformance without knowing which attributes are expected.
**Autonomous resolution:** Verify that the subcategory from the company report exists in the product taxonomy categories file. If it does, the schema simply hasn't been created yet — trigger SKU schema generation for that subcategory. Once the schema is available, return to Step 3 and continue.
**Escalate when:** The subcategory from the company report does not appear in the product taxonomy categories file. This indicates a taxonomy integrity issue.
**Escalation payload:** Company slug, the full `Category > Subcategory` value from the company report, confirmation that the subcategory was not found in the taxonomy.

### Decision: scraper_output_format_unclear

**Context:** The scraper source code is ambiguous about the output format it produces, making it unclear how to validate the scrape output.
**Autonomous resolution:** If the scraper source exists but uses an unusual output structure, infer the format from the code and proceed.
**Escalate when:** Scraper source is missing or unparseable.
**Escalation payload:** Company slug, details about what is missing or malformed in the scraper source.
