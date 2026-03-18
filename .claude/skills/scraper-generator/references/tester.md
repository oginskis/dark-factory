# Tester Sub-Agent

**Input:** Scraper path, catalog structure, expected product count, routing tables, mode, fix targets (retest only)
**Output:** `test_report.json` — structured results with rule-level pass/fail, per-category breakdowns, sample evidence

---

## Key Rule

The tester NEVER edits `scraper.py`. It only runs the scraper and evaluates output.

---

## Input Contract

| Field | Type | Description |
|---|---|---|
| `scraper_path` | path | Path to `scraper.py` |
| `catalog_structure` | object | Verified category tree from catalog assessment |
| `expected_product_count` | int | From catalog assessment |
| `routing_tables_path` | path | Path to `generator_input.json` (for semantic rules — contains `types` and `units` dicts) |
| `mode` | enum | `"full"`, `"retest"`, or `"final"` |
| `fix_targets` | list | (retest only) Rules and categories to re-verify |
| `regression_sample_from` | list | (retest only) Passing categories to sample for regression |

---

## Output Contract

Write two output files to the scraper's output directory after each dispatch:

1. **`test_reports.json`** — JSON array of all iterations. Read the existing file, append the new entry, write back. If the file doesn't exist, create it with a single-element array. This preserves the full history of every full/retest/final run.

2. **`test_summary.txt`** — Human-readable summary of all iterations. Overwrite on each dispatch. Use this format:

```
=== ITERATION 1: FULL mode — NEEDS_FIX === (2026-03-18T15:00:00Z)

  FAILED:
    M04: 43 products have value/unit concatenation in nominal_width, nominal_thickness
  PASSED: S01, S02, S03, S04, S05, S06, S07, S08, S09, M01, M02
  WARNINGS:
    M03: 12 attributes missing from attribute_units

  ISSUES:
    [M04] Regex found "18mm" pattern in number-typed attributes
      Attributes: nominal_width, nominal_thickness
      nominal_width: ["18mm", "9mm", "12mm"]

---
=== ITERATION 2: RETEST mode — PASS === (2026-03-18T15:05:00Z)

  FIX RESULTS:
    M04: PASS — 0 violations after fix
  REGRESSIONS: PASS (49 compared)
  PASSED: S01, S02, S03, S04, S05, S07, S08, S09, M01, M02, M04

---
=== ITERATION 3: FINAL mode — PASS === (2026-03-18T15:20:00Z)
  ...
```

The user can `cat output/test_summary.txt` at any time to see the full story of what was tested, what failed, what was fixed, and where things stand.

```json
{
  "mode": "full | retest | final",
  "timestamp": "ISO 8601",
  "status": "pass | needs_fix | unfixable",
  "smoke_summary": {
    "scraper_crashed": false,
    "persist_hook_verified": true,
    "duration_seconds": 45.2
  },
  "final_summary": {
    "total_products": 150,
    "errors_count": 0,
    "duration_seconds": 320.5,
    "scraper_crashed": false,
    "persist_hook_verified": true
  },
  "rule_results": [
    {
      "id": "S01",
      "status": "pass | fail | warn | skip",
      "value": 0.72,
      "threshold": 0.30,
      "per_category": {
        "/shop/timber-joinery": 0.65,
        "/shop/fencing": 0.12
      }
    },
    {
      "id": "M01",
      "status": "fail",
      "value": 0.95,
      "detail": "95% of products have units embedded in nominal_width, nominal_thickness"
    }
  ],
  "issues": [
    {
      "rule_id": "M01",
      "detail": "units embedded in values",
      "affected_categories": ["/shop/timber-joinery/joinery-timber/decorative-mouldings"],
      "affected_attributes": ["nominal_width", "nominal_thickness"],
      "sample_values": {"nominal_width": ["18mm", "9mm", "12mm"]},
      "sample_urls": ["https://example.com/p1", "https://example.com/p2", "https://example.com/p3"]
    }
  ],
  "passing_categories": ["/shop/sheet-materials/plywood/marine-plywood"]
}
```

`issues[].sample_values` and `issues[].sample_urls` must contain at least 3 entries, up to 10. This gives the coder enough evidence to diagnose and fix without re-running.

**Retest additions:** When `mode` is `"retest"`, the report also includes:

| Field | Description |
|---|---|
| `fix_results` | Per-rule pass/fail for each `fix_target` |
| `regression_results` | Output of `compare_baseline.py` — pass/fail + regression details |
| `new_issues` | Any issues found outside the fix targets |

---

## Three Modes

### Full Mode

Run after the coder writes the initial scraper. Validates everything from extraction to pagination.

**Step 1 — Probe.** Select 3-5 product URLs across different top-level categories from `catalog_structure`. Run for each:

```bash
uv run {scraper_path} --probe {url}
```

Evaluate all rules on probe output. This is a fast sanity check before committing to a full run. Timeout: **30 seconds per URL**.

**Step 2 — Per-category sampling.** For each top-level category in `catalog_structure`, run:

```bash
uv run {scraper_path} --categories "{cat}" --limit {N}
```

Where `N` is proportional to estimated category size. Total sample = 20% of expected products, max 500, min 5 per category. Use `--append` after the first category run so outputs accumulate into one `products.jsonl`.

Timeout per invocation: **`max(60, limit * 6)` seconds**.

**Step 3 — Depth check.** Run with no `--categories` to verify pagination and deduplication:

```bash
uv run {scraper_path} --limit 100
```

Timeout: **600 seconds**.

**Step 4 — Evaluate.** Run all rules (S01-S09, M01-M04) on the combined `products.jsonl` output.

**Step 5 — Save baseline.** Copy `products.jsonl` to `baseline_products.jsonl` in the same output directory.

**Step 6 — Write `test_report.json`.**

---

### Retest Mode

Run after the coder patches a fix. Only tests affected areas plus a regression sample.

**Step 1 — Fix verification.** For each fix target, run:

```bash
uv run {scraper_path} --categories "{affected_categories}" --limit 10
```

Re-evaluate the specific failing rule on the output.

**Step 2 — Regression check.** Run:

```bash
uv run {scraper_path} --categories "{regression_sample_from}" --limit 10 --append
```

Then run the regression comparison:

```bash
uv run .claude/skills/scraper-generator/scripts/compare_baseline.py --baseline {output_dir}/baseline_products.jsonl --retest {output_dir}/products.jsonl
```

If `compare_baseline.py` returns status `"fail"`, include the regressions list in `test_report.json` under `regression_results`.

**Step 3 — Rule evaluation.** Run all structural and semantic rules on the combined output.

**Step 4 — Write `test_report.json`** with `fix_results`, `regression_results`, and `new_issues`.

**Total retest timeout: 5 minutes.**

---

### Final Mode

Run after all retests pass. Same as full mode's per-category sampling + depth check, but **skip probe**. Fresh run to confirm at scale.

Write `test_report.json`.

---

## Validation Rules

### Structural Rules (S01-S09)

#### S01 — Core attribute fill rate

| | |
|---|---|
| **Severity** | error |
| **Threshold** | >= 30% of products must have non-empty `core_attributes` |
| **Check** | For each product, test whether `core_attributes` is non-empty (at least one key with a non-null value). Compute the percentage across all products. |
| **Metric** | `value` = count of products with non-empty core_attributes / total products |
| **Per-category** | Report `per_category` breakdown: for each top-level category path, compute the fill rate separately. This catches categories where extraction is broken while others are fine. |
| **On failure** | Include in `issues[]`: affected categories (those below threshold), sample URLs from failing products, sample values showing what core_attributes look like for failing products. |

#### S02 — Extended attribute fill rate

| | |
|---|---|
| **Severity** | warning |
| **Threshold** | >= 20% of products must have non-empty `extended_attributes` |
| **Check** | Same as S01 but for `extended_attributes`. |
| **Metric** | `value` = count of products with non-empty extended_attributes / total products |
| **On failure** | Include in `issues[]` with affected categories and sample URLs. Status is `warn`, not `fail` — does not block. |

#### S03 — Required top-level fields present

| | |
|---|---|
| **Severity** | error |
| **Threshold** | 100% of products |
| **Check** | Every product record must have all of: `sku`, `name`, `url`, `price`, `brand`, `product_category`, `scraped_at`. Each must be non-null (except `price` which may be null if the catalog does not display prices). |
| **Metric** | `value` = count of fully compliant products / total products |
| **On failure** | Include in `issues[]`: which fields are missing, sample URLs of non-compliant products, sample values showing the missing field pattern. |

#### S04 — product_category is valid taxonomy ID

| | |
|---|---|
| **Severity** | error |
| **Threshold** | 100% of products |
| **Check** | Read `docs/product-taxonomy/categories.md` and extract all valid taxonomy IDs. For each product, verify `product_category` appears in the valid set. |
| **Metric** | `value` = count of products with valid taxonomy ID / total products |
| **On failure** | Include in `issues[]`: invalid taxonomy IDs found, sample URLs, the invalid values. |

#### S05 — brand is top-level, not inside attributes

| | |
|---|---|
| **Severity** | error |
| **Threshold** | 100% of products |
| **Check** | Verify `brand` exists as a top-level field. Check that `core_attributes`, `extended_attributes`, and `extra_attributes` do not contain a `brand` key. |
| **Metric** | `value` = count of compliant products / total products |
| **On failure** | Include in `issues[]`: sample URLs, sample values showing where brand appears incorrectly. |

#### S06 — Category diversity

| | |
|---|---|
| **Severity** | warning |
| **Threshold** | >= 2 distinct top-level `category_path` values |
| **Check** | Collect all unique top-level category path prefixes from products. Count distinct values. If the catalog has only one category, auto-pass. |
| **Metric** | `value` = count of distinct top-level category paths |
| **Skip** | Skip in retest mode. |
| **On failure** | Include in `issues[]`: the single category path found, expected categories from catalog_structure. |

#### S07 — Zero errors

| | |
|---|---|
| **Severity** | error |
| **Threshold** | `errors_count == 0` in `summary.json` |
| **Check** | Read `summary.json` from the scraper's output directory. Verify `errors_count` is 0. |
| **Metric** | `value` = errors_count from summary.json |
| **On failure** | Include in `issues[]`: the error count and any error details from the summary. |

#### S08 — Scraper completed without crash

| | |
|---|---|
| **Severity** | error |
| **Threshold** | Process exit code 0 |
| **Check** | After each scraper invocation, check the process exit code. |
| **Metric** | `value` = exit code (0 = pass) |
| **On failure** | Include in `issues[]`: exit code, stderr output, last few log lines. |

#### S09 — Persist hooks functional

| | |
|---|---|
| **Severity** | error |
| **Threshold** | `products.jsonl` exists and is non-empty after run |
| **Check** | Verify the output file exists and contains at least one line. |
| **Metric** | `value` = line count of products.jsonl |
| **On failure** | Include in `issues[]`: whether file is missing or empty, any persist hook errors from logs. |

---

### Semantic Rules (M01-M04)

The tester reads `generator_input.json` (at `routing_tables_path`) to get:
- `types` — dict of attribute name to type string (`"str"`, `"number"`, `"list"`, `"bool"`) per subcategory
- `units` — dict of attribute name to unit string (e.g., `"mm"`, `"kg"`) per subcategory

These dicts are the source of truth for what type and unit each attribute should have.

#### M01 — Units separated from values

| | |
|---|---|
| **Severity** | error |
| **Check** | For each product: find attributes where the routing table type is `"number"` AND the `units` dict has an entry for that attribute. The attribute value must be numeric (`int` or `float`), and `attribute_units` must contain the key with the correct unit. Fails when the value is something like `"18mm"` where `18` + `{"attr": "mm"}` is expected. |
| **On failure** | Include in `issues[]`: affected attributes, sample values showing the concatenated value (e.g., `"18mm"`), sample URLs, affected categories. Minimum 3 samples, up to 10. |

#### M02 — Type conformance

| | |
|---|---|
| **Severity** | warning |
| **Check** | For each product: all attributes typed `"number"` in the routing tables should be `int` or `float`, not strings. Catches `"18mm"` (string with unit) and `"3"` (string that should be numeric). Overlaps with M01 for unit-bearing attributes. |
| **On failure** | Include in `issues[]`: affected attributes, sample values with their actual types, sample URLs. |

#### M03 — attribute_units populated

| | |
|---|---|
| **Severity** | warning |
| **Check** | For each product: when the routing table `units` dict has an entry for an attribute AND the product has that attribute in any bucket (`core_attributes`, `extended_attributes`, `extra_attributes`), `attribute_units` should contain the key. |
| **On failure** | Include in `issues[]`: affected attributes (those missing from attribute_units), sample URLs, the expected unit from the routing table. |

#### M04 — Value/unit concatenation scan

| | |
|---|---|
| **Severity** | error |
| **Check** | Apply regex `\d+\s*(mm|cm|m|kg|g|lb|oz|ml|l|V|W|A|Hz|kW|MPa)$` to attribute values — but ONLY on attributes where the routing table type is `"number"` OR the `units` dict has an entry. Do NOT flag string-typed attributes that happen to contain unit-like suffixes. |
| **On failure** | Include in `issues[]`: affected attributes, the matching values, sample URLs, affected categories. |

---

### Rule Evaluation per Mode

| Rule | Full | Retest (fix verification) | Retest (regression) | Final |
|---|---|---|---|---|
| S01-S05 | All products | Affected categories only | Compare baseline | All products |
| S06 | All products | Skip | Skip | All products |
| S07-S09 | All runs | All runs | All runs | All runs |
| M01-M04 | All products | Affected categories only | Compare baseline | All products |

---

## Regression Detection

During retest mode, after running the regression sample, invoke:

```bash
uv run .claude/skills/scraper-generator/scripts/compare_baseline.py --baseline {output_dir}/baseline_products.jsonl --retest {output_dir}/products.jsonl
```

If the script returns status `"fail"`, include the `regressions` list in `test_report.json` under `regression_results`. The orchestrator will dispatch the coder with both the original fix targets and the regression details.

---

## Timeouts

| Mode | Timeout |
|---|---|
| Probe | 30 seconds per URL |
| Full per-category run | `max(60, limit * 6)` seconds per invocation |
| Full depth check | 600 seconds |
| Retest total | 5 minutes |
| Final per-category run | `max(60, limit * 6)` seconds per invocation |

If a timeout is exceeded, kill the process immediately. Record the timeout in `test_report.json` under the relevant rule (S08 for crash, or as a top-level note). A timeout counts as a failure for the affected run.

---

## Status Values

| Status | Meaning |
|---|---|
| `pass` | All rules pass |
| `needs_fix` | One or more error-severity rules failed — coder needs to fix |
| `unfixable` | Fundamental issue (site down, complete extraction failure, all probes return empty) |
