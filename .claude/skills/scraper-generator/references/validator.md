# Validator Sub-Agent

**Input:** Generated scraper, catalog structure, expected product count, label coverage data (non-English only)
**Output:** Structured result with status code (`pass`, `label_coverage_dropped`, `core_fill_rate_low`, `probe_failed`, `test_failed`, `timeout`), test products, fill rate metrics, diagnostics

---

## Input Contract

| Field | Type | Description |
|---|---|---|
| `scraper` | artifact | The generated scraper to validate |
| `catalog_structure` | object | Verified Category Tree and Product Discovery section from the catalog assessment's Extraction Blueprint |
| `expected_product_count` | int | Estimated total products in the catalog (from catalog assessment) |
| `label_coverage` | float | Label coverage computed during label discovery (non-English sites only; omit for English sites) |
| `extension_attempts_used` | int | Number of label-discovery extension attempts already consumed (non-English sites only) |

---

## Output Contract

| Field | Type | Description |
|---|---|---|
| `status` | enum | One of: `pass`, `label_coverage_dropped`, `core_fill_rate_low`, `probe_failed`, `test_failed`, `timeout` |
| `probe_results` | list | Per-URL probe outcomes (URL, pass/fail, issues found) |
| `smoke_test_summary` | object | Summary dict from the smoke test teardown hook, or `null` if not reached |
| `final_verification_summary` | object | Summary dict from the final verification run, or `null` if skipped or not reached |
| `taxonomy_feedback` | object | Extra attributes proposed for schema addition, or `null` if skipped |
| `label_coverage_at_probe` | float | Recomputed label coverage after probing (non-English sites only) |
| `fix_cycles_used` | object | Map of gate name → number of fix-reprobe cycles consumed |

---

## Phase 1: Probe Extraction

Before running the full scraper, validate that the extraction logic works against the live site. This is a fast feedback loop — seconds per iteration, not minutes.

### Probe page selection

The probe must cover the breadth of the catalog. Different product categories on the same site often have different page layouts, spec tables, or data availability — a selector that works for one category may fail on another.

Select probe pages from **at least 3 different top-level categories** as identified in the catalog structure. Within each category, pick a product that looks representative — not the simplest or most populated one. If the catalog has fewer than 3 top-level categories, probe at least one product from every category.

### Probe execution

For each selected probe page, run the scraper's probe mode with that URL. Examine the output to verify all of the following:

- Universal top-level fields (`sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`) are populated. `price` and `currency` may be `null` when the catalog does not display prices.
- `core_attributes` and `extended_attributes` contain schema-matched keys.
- `extra_attributes` keys are `snake_case` with primitive values.
- No extraction errors are reported.

This executes the real extraction code path — do not manually simulate selectors or JSON parsing.

### Probe fix loop

If extraction fails for a given page:

1. Identify the specific issue (wrong selector, unexpected JSON-LD structure, missing field).
2. Fix the scraper code.
3. Re-probe the same page to verify the fix.
4. Repeat until the probe passes for all sampled products.

**Circuit breaker:** If the same extraction issue persists after 5 probe-fix cycles across all probe pages, return `status: probe_failed`.

### Label coverage gate (non-English sites only)

After probing all sampled products, recompute **label coverage** against the probe results. The probe may reveal new attribute labels not seen during initial sampling. If label coverage has dropped below 70%, return `status: label_coverage_dropped`. The caller will re-dispatch label discovery, then code generation, then re-run validation.

The label discovery circuit breaker (maximum 3 extension attempts total across the entire generation process) applies — do not bypass it. Check `extension_attempts_used` from the input before returning this status; if the limit is already reached, return `status: probe_failed` instead.

### Attribute fill rate gate

After probing, verify that probed products actually have non-empty `core_attributes`. For each probed product, at least one core attribute key must be populated. If every probed product has empty `core_attributes`, the label mapping or attribute routing is broken.

**Circuit breaker:** Allow at most 2 fix-regenerate-reprobe cycles. If core attributes remain empty after 2 cycles, return `status: probe_failed`.

Otherwise, return `status: core_fill_rate_low` so the caller can trigger a fix-regenerate cycle.

Once the probe passes for all sampled pages and both coverage gates are met, proceed to Phase 2.

---

## Phase 2: Smoke Test

Run the scraper with a limit of 20 products and verify it works end-to-end. This is a fast structural check — the probe already validated extraction logic, so failures here indicate problems with pagination, batching, rate limiting, or the persist hook.

### Timeout rule

The test run has a **hard time limit of 2 minutes**. A limit-20 scraper that takes longer than 2 minutes is broken.

If the test exceeds 2 minutes:

1. Kill the process immediately.
2. Read the scraper's stderr output (JSON log lines) to diagnose the failure. Common patterns:

   | Symptom | Likely cause | Fix |
   |---------|-------------|-----|
   | Repeated "Failed to parse" warnings with 0 products | Extraction logic broken | Fix selectors or JSON-LD parsing |
   | Repeated HTTP errors or retries | Rate limiting or network issue | Increase delay, add random jitter |
   | Processing many categories with 0 products | Category traversal broken | Fix navigation logic |
   | HTTP 429 responses | Rate limiting | Increase delay, add random jitter |
   | 200 responses but empty HTML | Geo-blocking or bot detection | Add realistic headers, rotate User-Agent |
   | Redirect chains to different domain | Localized redirect | Pin URL, set Accept-Language, handle redirects |
   | Garbled names or JSON failures | Encoding mismatch | Detect encoding, decode explicitly |

3. Fix the root cause and re-run.

**Circuit breaker:** Maximum 2 timeout retries. If the scraper times out a third time, return `status: timeout`.

Do not assume the scraper is "just slow." A correctly working limit-20 run should complete in under 90 seconds.

### Smoke test verification

The test must satisfy all of the following:

1. **Scraper completes without crashing.**
2. **Summary is valid** — `total_products` between 1 and 20; `errors_count` is 0.
3. **Product records are correct** — `brand` is a top-level field; `product_category` is a valid taxonomy ID; `sku`, `name`, `url`, and `scraped_at` are populated.
4. **Attribute fill rate gate** — at least 30% of products must have non-empty `core_attributes`. If fewer than 30%, return `status: core_fill_rate_low`.
5. **Extended attributes advisory** — at least 20% of products should have non-empty `extended_attributes`. If fewer than 20%, log a warning but do not stop.
6. **Persist hook worked** — the output destination has product data.
7. **Category diversity** — extracted products span at least 2 distinct top-level `category_path` values. If the catalog has only one category, auto-pass this check.

If the test fails for any hard criterion, return `status: test_failed`.

Once the smoke test passes, proceed to Phase 3. The scraper code is final at this point.

---

## Phase 3: Taxonomy Feedback

After the smoke test, analyze the test output for potential schema improvements. This phase does not modify the scraper or affect the validation result.

**When to skip:** Skip entirely when there are no `extra_attributes` in any test product, no extra attribute appears in more than 80% of test products, or the smoke test did not pass.

### Procedure

1. Collect all unique attribute keys from `extra_attributes` across all test products.
2. For each extra attribute, count how many products include it. If more than 80% of test products have the key, it is a candidate for schema addition.
3. Verify the candidate is not already in the schema under a different name.
4. For significant candidates, record the candidate attribute names and example values in the output as a taxonomy feedback signal. Do not re-map the current scraper's output — the scraper is final.

Record which attributes were proposed in `taxonomy_feedback`.

---

## Phase 4: Final Verification Run

After the smoke test and taxonomy feedback, run the scraper with a larger sample. This output is what the eval-generator validates against. The scraper code does not change in this phase.

### Sample size

```
sample_size = min(ceil(expected_product_count * 0.2), 100)
```

Examples: 50 products → sample 10, 123 → sample 25, 500+ → sample 100.

**When to skip:** If `sample_size <= 20`, skip this phase — the smoke test output is sufficient.

### Timeout

Maximum seconds allowed: `max(120, sample_size * 6)`.

### Verification criteria

1. Scraper completes without crashing.
2. `errors_count` is 0.
3. `total_products` is between 1 and `sample_size`.

If the verification fails, allow one retry, then return `status: test_failed`.

---

## Status Reference

| Status | Meaning | Returned from |
|--------|---------|---------------|
| `pass` | All phases completed successfully | Phase 4 (or Phase 2 when Phase 4 is skipped) |
| `label_coverage_dropped` | Label coverage fell below 70% at probe time | Phase 1 label coverage gate |
| `core_fill_rate_low` | Core attributes empty in probe or fewer than 30% fill rate in smoke test | Phase 1 fill rate gate or Phase 2 verification |
| `probe_failed` | Probe fix circuit breaker exhausted, or fill rate fix circuit breaker exhausted | Phase 1 |
| `test_failed` | Smoke test or final verification failed | Phase 2 or Phase 4 |
| `timeout` | Timeout circuit breaker exhausted (3 attempts) | Phase 2 |
