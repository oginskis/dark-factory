# Tester Sub-Agent

**Input:** Scraper path, catalog structure, expected product count, routing tables, mode, iteration, fix targets (retest only)
**Output:** `test_report.json` — structured results with rule-level pass/fail, per-category breakdowns, sample evidence

---

## Key Rules

1. The tester NEVER edits `scraper.py`. It only runs the scraper and evaluates output.
2. Use the helper scripts for all mechanical work. The tester's job is to call them, read their output, aggregate results, and handle failures.

---

## Scripts

| Script | Purpose | Output |
|--------|---------|--------|
| `tester_run_scraper.py` | Run scraper with correct flags, capture stderr, manage iteration files | JSON traces to stdout |
| `tester_tester_evaluate_structural.py` | S01-S09 structural validation | JSON with `rule_results` + `issues` to stdout |
| `tester_tester_evaluate_semantic.py` | M01-M04 semantic validation | JSON with `rule_results` + `issues` to stdout |
| `tester_tester_compare_baseline.py` | Regression detection (retest mode) | JSON with `status` + `regressions` to stdout |

All scripts are at `.claude/skills/scraper-generator/scripts/`.

---

## Input Contract

| Field | Type | Description |
|---|---|---|
| `scraper_path` | path | Path to `scraper.py` |
| `catalog_structure` | object | Verified category tree from catalog assessment |
| `expected_product_count` | int | From catalog assessment |
| `routing_tables_path` | path | Path to `generator_input.json` |
| `mode` | enum | `"full"`, `"retest"`, or `"final"` |
| `iteration` | int | Iteration number (1, 2, 3...) |
| `fix_targets` | list | (retest only) Rules and categories to re-verify |
| `regression_sample_from` | list | (retest only) Passing categories to sample for regression |
| `test_report_path` | path | Path where the tester writes `test_report.json` |

**Derived paths:** `output_dir = scraper_path.parent / "output"`. All scripts receive this as `--output-dir`. The tester writes all output files to this directory.

---

## Output Contract

The tester writes these files to the scraper's output directory. The scripts handle most of this — the tester aggregates and writes the final report.

| File | Written by | Description |
|------|-----------|-------------|
| `test_report.json` | tester | Current iteration's results (orchestrator reads this) |
| `test_reports.json` | tester | Cumulative array of all iterations |
| `test_summary.txt` | tester | Human-readable summary of all iterations |
| `products_iteration_{N}.jsonl` | `tester_run_scraper.py --step save-iteration` | Per-iteration product snapshot |
| `debug_iteration_{N}.log` | `tester_run_scraper.py` (stderr capture) | Per-iteration debug log |
| `debug.log` | `tester_run_scraper.py --step save-iteration` | Copy of latest iteration's debug log |
| `baseline_products.jsonl` | `tester_run_scraper.py --step save-baseline` | Regression baseline (full mode only) |

### test_report.json format

```json
{
  "mode": "full",
  "timestamp": "2026-03-18T15:00:00Z",
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
    {"id": "S01", "status": "pass", "value": 0.72, "threshold": 0.30, "per_category": {}},
    {"id": "M01", "status": "fail", "value": 0.95}
  ],
  "issues": [
    {
      "rule_id": "M01",
      "detail": "units embedded in values",
      "affected_categories": ["/shop/timber-joinery"],
      "affected_attributes": ["nominal_width"],
      "sample_values": {"nominal_width": ["18mm", "9mm"]},
      "sample_urls": ["https://example.com/p1", "https://example.com/p2", "https://example.com/p3"]
    }
  ],
  "passing_categories": ["/shop/sheet-materials/plywood"]
}
```

### Retest mode extensions

Retest mode adds three fields to the report:

```json
{
  "fix_results": {
    "S01": {"status": "fixed", "before": 0.15, "after": 0.45},
    "M01": {"status": "still_failing", "before": 0.80, "after": 0.60}
  },
  "regression_results": {
    "status": "pass",
    "products_compared": 12,
    "regressions": [],
    "category_dropouts": []
  },
  "new_issues": [
    {"rule_id": "S03", "detail": "brand missing after fix", "affected_categories": ["/shop/tools"], "sample_urls": ["https://example.com/p1"]}
  ]
}
```

| Field | Description |
|---|---|
| `fix_results` | Dict keyed by rule ID. Each value: `status` (`"fixed"` or `"still_failing"`), `before` (value from previous report), `after` (value from this retest). Only includes rules listed in `fix_targets`. |
| `regression_results` | Verbatim output from `tester_compare_baseline.py` — `status` (`"pass"` or `"fail"`), `products_compared`, `regressions` (field-level), `category_dropouts`. |
| `new_issues` | Issues NOT in the previous report — new failures introduced by the fix. Same structure as `issues[]` entries. |

---

## Full Mode

**Step 1 — Probe.** Select 3-5 product URLs across different top-level categories from `catalog_structure`. Run:

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step probe \
  --probe-urls "https://www.acme.com/p1,https://www.acme.com/p2,https://www.acme.com/p3" \
  --iteration 1
```

Read the JSON traces from stdout. Each trace has `"phase": "probe"` with `status` ("ok", "error", "timeout", "parse_error"). If all probes fail, the scraper's extraction is broken — skip to evaluation (S09 will catch it).

**Step 2 — Per-category sampling.** Compute limit per category: `max(5, min(expected_count * 0.2, 500) / num_categories)`. Run:

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step categories \
  --categories "/shop/tools,/shop/wood,/shop/paint" \
  --limit-per-cat {computed_limit} \
  --iteration 1
# Example: 1200 expected, 3 categories → max(5, min(240, 500)/3) = 80
```

Read traces: `"phase": "category"` with status per category.

**Step 3 — Depth check.**

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step depth \
  --iteration 1
```

**Step 4 — Save iteration files.**

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step save-iteration \
  --iteration 1
```

**Step 5 — Save baseline.**

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step save-baseline \
  --iteration 1
```

**Step 6 — Evaluate structural rules.** Determine the worst exit code from Steps 1-3 by reading the `exit_code` field from each trace line (every trace from `tester_run_scraper.py` includes `"exit_code": N`). Use the highest non-zero value, or 0 if all succeeded. Pass it to `--exit-code`:

```bash
uv run .claude/skills/scraper-generator/scripts/tester_tester_evaluate_structural.py \
  --output-dir docs/scraper-generator/acme/output \
  --exit-code 0 \
  --iteration 1
```

Parse the JSON stdout: `rule_results` array (S01-S09) and `issues` array.

**Step 7 — Evaluate semantic rules.**

```bash
uv run .claude/skills/scraper-generator/scripts/tester_tester_evaluate_semantic.py \
  --output-dir docs/scraper-generator/acme/output \
  --routing-tables docs/scraper-generator/acme/generator_input.json \
  --iteration 1
```

Parse the JSON stdout: `rule_results` array (M01-M04) and `issues` array.

**Step 8 — Aggregate and write report.** Merge `rule_results` and `issues` from both scripts. Determine overall status:
- Any error-severity rule (`S01, S03, S04, S05, S07, S08, S09, M01, M04`) failed → `"needs_fix"`
- S08 or S09 failed → `"unfixable"` (crash or no output)
- All pass → `"pass"`

Write `test_report.json`, append to `test_reports.json`, write `test_summary.txt`.

**Compute `passing_categories`:** For each top-level category prefix (first ` > ` segment of `category_path`), check whether all error-severity rules (S01, S03, S04, S05, S07, M01, M04) pass for products in that category. List the prefixes of all passing categories. Categories with only warning-severity failures (S02, S06, M02, M03) still count as passing.

---

## Retest Mode

**Step 1 — Fix verification.** Run categories that had failures. This starts with a clean `products.jsonl` (no `--append`). Step 1 products remain in the file — Step 2 appends to them.

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step categories \
  --categories "/shop/tools" \
  --limit-per-cat 10 \
  --iteration 2
```

**Step 2 — Regression check.** Run categories that were passing. Use `--append` so regression products accumulate alongside fix products:

```bash
uv run .claude/skills/scraper-generator/scripts/tester_run_scraper.py \
  --scraper docs/scraper-generator/acme/scraper.py \
  --step categories \
  --categories "/shop/wood,/shop/paint" \
  --limit-per-cat 10 \
  --append \
  --iteration 2
```

Then compare against baseline:

```bash
uv run .claude/skills/scraper-generator/scripts/tester_tester_compare_baseline.py \
  --baseline docs/scraper-generator/acme/output/baseline_products.jsonl \
  --retest docs/scraper-generator/acme/output/products.jsonl
```

**Step 3 — Save iteration files + evaluate.** Run in this order (save-iteration must run first — evaluation scripts read the snapshot):
1. Save iteration: `tester_run_scraper.py --step save-iteration --iteration {N}`
2. Structural: `tester_evaluate_structural.py --output-dir {output_dir} --exit-code {worst_exit} --skip-s06 --iteration {N}`
3. Semantic: `tester_evaluate_semantic.py --output-dir {output_dir} --routing-tables {routing_tables_path} --iteration {N}`

Do NOT save baseline in retest mode — only full and final modes save baselines.

**Step 4 — Aggregate.** Same as full mode Step 8, plus include `regression_results` from tester_compare_baseline. **Regression results influence the overall status:** if `compare_baseline` returns `"status": "fail"` (field regressions or category dropouts detected), the overall status must be `"needs_fix"` even if all S01-S09 and M01-M04 rules pass. This prevents regressions from silently propagating through final mode.

**Note on combined evaluation:** Structural/semantic rules run on the combined output of fix-verification + regression-sample products. If aggregate scores are misleading (e.g., a correct fix lowered by pre-existing issues in regression samples), note this in the report but still use the combined result for status determination.

Pass `--retest-categories` to `tester_compare_baseline.py` with the list of passing categories that were retested, enabling category-level dropout detection.

**Total retest timeout: 5 minutes.**

---

## Final Mode

Same as full mode but **skip probe** (Step 1). Start from per-category sampling. Use the next iteration number.

**Baseline overwrite:** Final mode saves a new baseline (Step 5 of full mode). This is intentional — the latest successful run becomes the reference for future retests.

---

## Handling Script Failures

If any script exits with a non-zero code:

1. Read stdout — partial traces may show how far it got
2. Read `debug_iteration_{N}.log` — scraper's stderr shows HTTP requests, errors, timing
3. Diagnose: was it the scraper (extraction broken) or the script (bug)?
4. Write a `test_report.json` with `"status": "unfixable"` and the error details so the orchestrator knows what happened

Do NOT retry a script silently. Report the failure with evidence.

---

## Status Values

| Status | Meaning |
|---|---|
| `pass` | All error-severity rules pass. Warning-severity rules (S02, S06, M02, M03) may fail — they do NOT affect status. |
| `needs_fix` | One or more error-severity rules failed — coder can fix |
| `unfixable` | Scraper crashed (S08) or produced no output (S09) — fundamental issue |

### Rule severity classification

| Severity | Rules | Effect on status |
|----------|-------|-----------------|
| **error** | S01, S03, S04, S05, S07, S08, S09, M01, M04 | Any failure → `"needs_fix"` (or `"unfixable"` for S08/S09) |
| **warning** | S02, S06, M02, M03 | Failures are logged in `rule_results` and `issues` but **never** trigger `"needs_fix"`. A scraper with only warning failures is `"pass"`. |

The tester always reports warning failures in the output for visibility, but the status determination ignores them entirely.

---

## Validation Rules Reference

The scripts implement these rules. This table tells the tester what each result means and what fix guidance to give the coder.

### Structural (tester_evaluate_structural.py)

| Rule | Severity | What it checks | What to fix if it fails |
|------|----------|---------------|------------------------|
| S01 | error | >=30% products have non-empty core_attributes | Extraction logic isn't finding spec tables or product attributes. Check CSS selectors in the catalog assessment against the live page. Look at `per_category` to find which categories are broken. |
| S02 | warning | >=20% products have non-empty extended_attributes | Same as S01 but lower priority. Only a warning — does not block. |
| S03 | error | 100% products have all required top-level fields | Missing `sku`, `name`, `url`, `brand`, `product_category`, `scraped_at`, or `category_path`. Check which fields are missing from `issues[].detail`. Usually a selector issue for the missing field. |
| S04 | error | 100% products have valid taxonomy ID in product_category | The scraper is emitting an ID that doesn't exist in categories.md. Check the `category_mapping` in config — a URL prefix may map to a wrong or misspelled taxonomy ID. |
| S05 | error | brand is top-level, never inside attribute buckets | The scraper puts brand inside core/extended/extra_attributes instead of as a top-level field. Fix the extraction to set `brand` at root level. |
| S06 | warning | >=2 distinct top-level category_path values (skip in retest) | Scraper only produces one category path — pagination or category traversal may be broken. Only a warning. |
| S07 | error | errors_count in summary.json is 0. `tester_run_scraper.py` accumulates summary.json across all scraper invocations within a step, so errors_count reflects the total across all category runs. | Scraper logged errors during the run. Read `debug_iteration_{N}.log` for details — usually HTTP errors or parse failures. |
| S08 | error | Scraper exit code 0 (no crash) | Scraper crashed. Read `debug_iteration_{N}.log` for the traceback. If exit code is -1, it timed out. |
| S09 | error | products.jsonl exists and is non-empty | Scraper ran but produced zero products. Extraction logic doesn't match the site. This is unfixable by patching — likely needs a full rewrite of extraction selectors. |

### Semantic (tester_evaluate_semantic.py)

| Rule | Severity | What it checks | What to fix if it fails |
|------|----------|---------------|------------------------|
| M01 | error | Number-typed attrs with units must be numeric, not "18mm" | The scraper stores "18mm" as a string instead of `18` + `attribute_units: {"attr": "mm"}`. Fix: parse the numeric value out, put the unit in `attribute_units`. Check `issues[].affected_attributes` for which attrs and `issues[].sample_values` for examples. |
| M02 | warning | All number-typed attrs must be int/float, not strings | String values like `"3"` where `3` (int) is expected. Fix: add `int()` or `float()` conversion in the extraction logic. Warning only — does not block. |
| M03 | warning | attribute_units must have entries for attrs with units in routing table | Product has the attribute but `attribute_units` doesn't have the corresponding key. Fix: add the unit to `attribute_units` when extracting the attribute. Warning only. |
| M04 | error | No embedded units (regex scan for "18mm", "5kg", "220V" patterns) | Same root cause as M01 — values have units concatenated. Check `issues[].sample_values` for the exact patterns. Fix: split value from unit during extraction. |
