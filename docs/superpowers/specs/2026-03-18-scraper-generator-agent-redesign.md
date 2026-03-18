# Scraper Generator Redesign

**Date:** 2026-03-18
**Status:** Approved

## Problems

1. **Validator re-runs everything after every fix.** 500-product run (50 min) repeats on every code change.
2. **No visibility into what the validator is doing.** Runs for 1+ hour with no structured reporting.
3. **Units embedded in values.** `"nominal_width": "18mm"` instead of `18` + `attribute_units`.
4. **Category misclassification.** Mouldings classified as lumber instead of millwork.
5. **Empty core_attributes.** Pine products missing `wood_type` parseable from product name.
6. **No semantic validation.** Fill rate percentages don't catch issues 3-5.
7. **Confusing who writes code and who tests.** Validator edits `scraper.py` during probe fix loop.

## Solution

Three agents with strict roles. Targeted re-testing. Semantic validation rules. No backwards compatibility.

## Agent Roles

| Agent | Does | Writes code? | Runs scraper? |
|---|---|---|---|
| **Orchestrator** | Coordinates flow, dispatches coder and tester, handles escalations. Runs inline. | No | No |
| **Coder** | Writes and patches `scraper.py`. Sub-agent dispatch. | Yes | No |
| **Tester** | Runs scraper, evaluates output, reports results. Sub-agent dispatch. | No | Yes |

No agent both writes code and evaluates it.

## Reference Files

```
.claude/skills/scraper-generator/
  SKILL.md
  references/
    orchestrator.md    ← rewrite: pure coordination
    coder.md           ← new: replaces code-generator.md + persist-hooks.md
    tester.md          ← new: replaces validator.md
```

Delete: `code-generator.md`, `validator.md`, `persist-hooks.md`.

## Scraper CLI Flags

Generated scrapers must support:

| Flag | What it does | New? |
|---|---|---|
| `--limit N` | Stop after N products | Existing |
| `--probe URL` | Extract one product to stdout | Existing |
| `--categories LIST` | Only traverse matching category prefixes | New |
| `--append` | Skip setup() truncation, append to products.jsonl | New |

`--categories` + `--limit` can combine. `--probe` exclusive with everything else.

These requirements live in `coder.md`.

## Tester Modes

| Mode | When | What it runs | Time |
|---|---|---|---|
| `full` | After coder writes initial scraper | Per-category sampling: `--categories X --limit N` per top-level category (proportional to size), then `--limit 100` depth check | ~15 min |
| `retest` | After coder patches a fix | `--categories {broken} --limit 10` + `--categories {passing} --limit 10` for regression | ~3 min |
| `final` | All retests pass | Same per-category sampling as full, fresh run | ~15 min |

Every mode uses `--categories` + `--limit`. No mode runs unscoped `--limit 500`. Every category gets tested.

Uses `--append` so multiple category runs accumulate into one `products.jsonl`.

### Baseline & Regression

After `full` mode, tester copies `products.jsonl` to `baseline_products.jsonl`. During `retest`, helper script `compare_baseline.py` diffs regression sample against baseline.

## Structured Test Report

Tester writes `test_report.json` — overwritten each dispatch.

```json
{
  "mode": "full",
  "timestamp": "2026-03-18T15:00:00Z",
  "status": "pass | needs_fix | unfixable",
  "smoke_summary": {
    "total_products": 20,
    "errors_count": 0,
    "duration_seconds": 45.2,
    "scraper_crashed": false,
    "persist_hook_verified": true
  },
  "final_summary": { "...": "same fields" },
  "rule_results": [
    {"id": "S01", "status": "pass", "value": 0.72, "threshold": 0.30, "per_category": {"/shop/timber-joinery": 0.65, "/shop/fencing": 0.12}},
    {"id": "M01", "status": "fail", "value": 0.95, "detail": "95% of products have units embedded in nominal_width, nominal_thickness"}
  ],
  "issues": [
    {
      "rule_id": "M01",
      "detail": "units embedded in values",
      "affected_categories": ["/shop/timber-joinery/joinery-timber/decorative-mouldings"],
      "affected_attributes": ["nominal_width", "nominal_thickness"],
      "sample_urls": ["https://example.com/p1", "https://example.com/p2", "https://example.com/p3"],
      "sample_values": {"nominal_width": ["18mm", "9mm", "12mm"]}
    }
  ],
  "passing_categories": ["/shop/sheet-materials/plywood/marine-plywood"]
}
```

Retest adds: `fix_results`, `regression_results`, `new_issues`.

## Validation Rules

### Structural (existing checks, now with IDs)

| ID | Rule | Severity | Threshold |
|---|---|---|---|
| S01 | Core attribute fill rate | error | >= 30% |
| S02 | Extended attribute fill rate | warning | >= 20% |
| S03 | Required top-level fields present | error | 100% |
| S04 | `product_category` is valid taxonomy ID | error | 100% |
| S05 | `brand` is top-level | error | 100% |
| S06 | Category diversity | warning | >= 2 top-level paths |
| S07 | Zero errors in run | error | 0 |
| S08 | No crash | error | exit 0 |
| S09 | Persist hooks work | error | products.jsonl non-empty |

### Semantic (new — catches problems 3-5)

| ID | Rule | Problem | What it checks |
|---|---|---|---|
| M01 | Units separated from values | #3 | `number`-typed attributes with schema Unit != `--` must be numeric, unit in `attribute_units`. Fails on `"18mm"`. |
| M02 | Type conformance | #3 | All `number`-typed attributes must be int/float, not strings. |
| M03 | `attribute_units` populated | #3 | Schema declares unit + product has attribute → `attribute_units` must have the key. |
| M04 | Value/unit concatenation scan | #3 | Regex on `number`-typed or unit-bearing attributes only. |

S01 per-category breakdown + sample_values catches #4 (misclassification) and #5 (missing name-extractable attributes) by showing exactly which categories and attributes are failing.

**Routing table extension:** `prepare_generator_input.py` adds a `units` dict (attribute key → schema unit string) so tester can evaluate M01/M03/M04.

## Coder Contract

Lives in `coder.md`. Absorbs everything from current `code-generator.md` + `persist-hooks.md`:
- Product record format
- Library selection
- 10 required behavior rules
- Product discovery strategy
- Python code quality rules
- Persist hooks
- CLI flags (`--limit`, `--probe`, `--categories`, `--append`)

**Two modes:**

**`generate`** — receives: catalog assessment, routing tables, category mapping, platform knowledgebase, label map (non-English). Writes `scraper.py`.

**`fix`** — receives: everything from generate + latest `test_report.json` + existing `scraper.py`. Patches targeted fixes based on the issue details and sample values.

Full context on every dispatch — coder always has the complete picture.

## Orchestrator Flow

Pure coordination. No code, no testing.

```
Step 1: Load context, build category mapping, load SKU schemas
  +-- Missing assessment? -> ESCALATE
  +-- Unmapped URL prefix? -> ESCALATE
  +-- Missing schema, subcategory exists? -> Auto-generate via /product-taxonomy
  +-- Missing schema, not in taxonomy? -> ESCALATE

Step 1b: Build label map (non-English only, skip for English)
  +-- Coverage < 30%? -> ESCALATE

Step 2: Dispatch Coder (mode: "generate")
  <- scraper.py written

Step 3: Dispatch Tester (mode: "full")
  <- test_report.json
  +-- "pass" -> Step 6
  +-- "needs_fix" -> Step 4
  +-- "unfixable" -> ESCALATE

Step 4: Dispatch Coder (mode: "fix")
  Pass: test_report.json + full context
  <- scraper.py patched

Step 5: Dispatch Tester (mode: "retest")
  Pass: fix_targets, regression_sample_from
  <- test_report.json overwritten
  +-- "pass" -> Step 5b
  +-- "needs_fix" -> Step 4 (max 3 cycles, then ESCALATE)
  +-- regressions -> Step 4 with regression info

Step 5b: Dispatch Tester (mode: "final")
  +-- "pass" -> Step 6
  +-- "fail" -> ESCALATE

Step 6: Platform knowledgebase + config.json + validation.json + self-verification
```

## Circuit Breakers

| Breaker | Limit |
|---|---|
| Fix -> retest cycles | Max 3 |
| Same rule failing after fix | Max 2 attempts, then unfixable |
| Label extension attempts (non-English) | Max 3 |
| Retest timeout | 5 minutes |
| Full/final timeout | max(120, sample_size * 6) seconds |

## Compatibility

`validation.json` still written in Step 6 — derived from `test_report.json`, same format as today. `/scraper-remediation` reads `validation.json` unchanged. When remediation invokes fix mode, orchestrator maps eval check names to rule IDs.

## Files Changed

| File | Change |
|---|---|
| `references/orchestrator.md` | Rewrite — pure coordination, coder/tester dispatches |
| `references/coder.md` | New — replaces code-generator.md + persist-hooks.md |
| `references/tester.md` | New — replaces validator.md, three modes, structural + semantic rules |
| `references/code-generator.md` | Delete |
| `references/validator.md` | Delete |
| `references/persist-hooks.md` | Delete |
| `scripts/prepare_generator_input.py` | Update — add units dict |
| `scripts/compare_baseline.py` | New — JSONL regression diff |
| `tests/test_compare_baseline.py` | New |
| `tests/test_prepare_generator_input.py` | Update — test units |
| `SKILL.md` | Update — file locations, dispatch instructions |

## Expected Result

| Scenario | Before | After |
|---|---|---|
| First validation | 25-50 min | ~15 min (per-category sampling) |
| Each fix cycle | 25-50 min | ~3 min (retest) |
| 3 fix cycles + final | 100-200 min | ~25 min |
