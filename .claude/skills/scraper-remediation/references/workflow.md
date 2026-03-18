# Scraper Remediation Workflow

**Input:** Company slug, eval result with check_details, existing scraper source
**Output:** Remediation log with outcome (`resolved`, `escalated`, `no_action`), or escalation

---

## Context

This workflow orchestrates an autonomous feedback loop between eval results and scraper-generator. When eval detects scraper degradation, this workflow triages the cause (config drift vs scraper regression), applies up to 3 targeted fix cycles, and tracks the full ping-pong history in a remediation log. The workflow is a thin orchestrator — it invokes scraper-generator in fix mode and re-runs the eval script, but never modifies scrapers or eval configs directly.

---

## Step 1: Check Entry Conditions

Read `eval_result.json` and check the following in order:

1. **File missing:** If `eval_result.json` does not exist, exit with `outcome: "no_action"` and message "Run eval first."
2. **Already passing:** If `status` is `"pass"`, exit with `outcome: "no_action"`.
3. **Insufficient data:** If `status` is `"insufficient_data"`, exit with `outcome: "escalated"` — eval cannot score meaningfully, remediation cannot help. Escalate immediately — see `insufficient_data_escalation` decision.
4. **Concurrent run guard:** If `remediation_log.json` exists with `started_at` but no `resolved_at`, check the timestamp. If `started_at` is older than 4 hours, treat as a stale lock from a crashed run — overwrite and proceed. Otherwise exit with a message that remediation is already in progress.
5. **Degraded or failed:** If `status` is `"degraded"` or `"fail"`, proceed to Step 2.

Write `remediation_log.json` with `started_at` set to the current timestamp and `outcome` omitted (signals in-progress).

---

## Step 2: Triage

Before entering fix cycles, determine whether the problem is a stale eval config or a broken scraper.

Read `eval_result.json` `checks` and `check_details`. Look for config drift indicators:

- `pagination_completeness` failing while `core_attribute_coverage` passes → product count changed on the site, not an extraction problem.
- `category_diversity` failing while other checks pass → site reorganized its category tree.
- `row_count_trend` failing in isolation → product count shifted.

**If config drift detected:**
1. Set `triage: "config_drift"` in the remediation log.
2. Re-run `/eval-generator` for the slug to regenerate `eval_config.json` with fresh data.
3. Re-run the eval script: `uv run eval/eval.py {eval_config_path} --no-history`.
4. If eval now passes: set `outcome: "resolved"`, write the remediation log, exit.
5. If eval still fails: set `triage: "config_drift_then_scraper"`, proceed to Step 3.

**If scraper regression detected** (attribute coverage, schema conformance, price sanity failures): set `triage: "scraper_regression"`, proceed to Step 3.

---

## Step 3: Backup Scraper

Before the first fix cycle, copy the current scraper to a backup:

```bash
cp docs/scraper-generator/{slug}/scraper.py docs/scraper-generator/{slug}/scraper.py.pre-remediation
```

This preserves the pre-remediation scraper. The backup is overwritten on each new remediation invocation, not per cycle.

---

## Step 4: Build Fix Request

Construct a fix request JSON from the eval result. Include all failing and passing checks with their values and thresholds:

```json
{
  "mode": "fix",
  "cycle": 1,
  "slug": "{slug}",
  "failing_checks": [
    {
      "check": "core_attribute_coverage",
      "value": 0.0,
      "threshold": 0.9,
      "subcategory_details": {
        "wood.softwood_hardwood_lumber": {
          "coverage": 0.0,
          "products": 90,
          "top_missing": [["appearance_grade", 90], ["use_class", 90]]
        }
      }
    }
  ],
  "passing_checks": [
    { "check": "price_sanity", "value": 1.0, "threshold": 1.0 }
  ],
  "scraper_path": "docs/scraper-generator/{slug}/scraper.py",
  "eval_config_path": "docs/eval-generator/{slug}/eval_config.json"
}
```

For checks that have `check_details` entries in the eval result (e.g., `core_attribute_coverage`, `extended_attribute_coverage`, `semantic_validation`), include the full detail in `subcategory_details`. For checks without detail, include only `check`, `value`, and `threshold`.

Increment `cycle` on each iteration (1, 2, 3).

---

## Step 5: Invoke Scraper-Generator Fix Mode

Invoke `/scraper-generator` with the fix request as input. Scraper-generator in fix mode:

1. Reads the existing scraper.py (does not archive or regenerate from scratch).
2. Analyzes the failing checks to determine what to patch.
3. Applies targeted fixes (enrichment patterns, type conversions, selectors, label maps).
4. Runs validation (probe → smoke test → final verification).
5. Writes `fix_summary` to `validation.json` with `fix_outcome` (`"fixed"`, `"partial"`, or `"unfixable"`).

If `fix_outcome` is `"unfixable"`, skip remaining cycles — proceed directly to Step 8 (escalation).

---

## Step 6: Re-Run Eval

After scraper-generator completes, re-run the eval script against the fresh output:

```bash
uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json --no-history
```

The `--no-history` flag ensures the remediation re-run does not pollute `eval_history.json` or create/update `baseline.json`.

---

## Step 7: Assess Result and Loop

Read the updated `eval_result.json`:

- **Passing (`status: "pass"`):** Delete `baseline.json` so the next regular eval creates a fresh baseline. Set `outcome: "resolved"`. Proceed to Step 9.
- **Still failing AND `cycle < 3`:** Record this cycle in the remediation log, increment cycle counter, return to Step 4.
- **Still failing AND `cycle == 3`:** Record this cycle. Set `outcome: "escalated"`. Proceed to Step 8.

---

## Step 8: Escalate

When escalation is needed (3 cycles exhausted, `fix_outcome: "unfixable"`, or `insufficient_data`):

1. Set `outcome: "escalated"` in the remediation log.
2. Write the remediation log with all cycle history.
3. Escalate to the user — see the appropriate decision (`cycles_exhausted`, `unfixable_scraper`, or `insufficient_data_escalation`).

---

## Step 9: Self-Verification

After the workflow completes (any outcome), verify:

1. `remediation_log.json` exists at `docs/scraper-remediation/{slug}/remediation_log.json`.
2. It contains valid JSON with all required fields: `slug`, `started_at`, `resolved_at`, `trigger_eval_score`, `trigger_eval_status`, `triage`, `cycles` (array), `outcome`, `total_cycles`.
3. `outcome` is one of `"resolved"`, `"escalated"`, `"no_action"`.
4. If `outcome` is `"resolved"`, verify `baseline.json` was deleted.
5. Each cycle entry has `cycle`, `fix_request`, `scraper_changes`, `eval_after`.

---

## Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Valid JSON** | Single JSON object, parseable | Trailing commas, comments |
| **`slug` is a string** | `"harlowbros"` | Missing or numeric |
| **`started_at` and `resolved_at` are ISO 8601** | `"2026-03-18T14:00:00Z"` | Unix timestamp, missing |
| **`triage` is a known value** | `"scraper_regression"`, `"config_drift"`, `"config_drift_then_scraper"` | Other values |
| **`outcome` is a known value** | `"resolved"`, `"escalated"`, `"no_action"` | Other values |
| **`cycles` is an array** | `[{...}, {...}]` | Object, string |
| **Each cycle has required fields** | `cycle`, `fix_request`, `scraper_changes`, `eval_after` | Missing fields |
| **`total_cycles` matches array length** | `"total_cycles": 2` with 2 entries | Mismatch |

---

## Boundaries

- Does not modify scraper.py directly — scraper-generator does that via fix mode.
- Does not modify eval_config.json directly — eval-generator does that during triage.
- Does not append to eval_history.json or create/update baseline.json — uses `--no-history` flag.
- Writes only to `docs/scraper-remediation/{slug}/`.
- One exception: creates `scraper.py.pre-remediation` backup in the scraper-generator directory before the first fix cycle.
- Does not define the product taxonomy, SKU schemas, or eval check logic.

---

## Decisions

### Decision: unfixable_scraper

**Context:** Scraper-generator returned `fix_outcome: "unfixable"` — the problem requires a fundamental approach change (e.g., site switched from HTML to SPA, added bot protection, completely restructured URLs) that cannot be addressed with targeted patches.
**Autonomous resolution:** None.
**Escalate when:** Always — this is not recoverable within the remediation loop.
**Escalation payload:** Company slug, cycle number where unfixable was detected, fix_summary from scraper-generator, current eval score and failing checks.

### Decision: cycles_exhausted

**Context:** Three fix cycles completed and the eval still reports degradation or failure. The scraper has been patched three times but the eval score has not recovered to a passing state.
**Autonomous resolution:** None.
**Escalate when:** Always — the remediation budget is spent.
**Escalation payload:** Company slug, all 3 cycle entries (fix requests, scraper changes, eval results), current eval score, trend across cycles (improving/stable/worsening).

### Decision: insufficient_data_escalation

**Context:** The eval returned `status: "insufficient_data"` meaning fewer than 3 checks could be scored. This typically means the scraper output is missing, empty, or severely malformed. Remediation cannot help — there is nothing to diagnose.
**Autonomous resolution:** None.
**Escalate when:** Always.
**Escalation payload:** Company slug, eval status, products_found count from eval result.
