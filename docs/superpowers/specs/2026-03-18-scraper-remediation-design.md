# Design: Scraper Remediation Feedback Loop

**Date:** 2026-03-18
**Status:** Approved

## Problem

The eval system detects scraper degradation and sets `recommend_rediscovery` in eval_result.json, but nothing reads that flag. When a site changes and the scraper starts producing bad data, a human must manually notice and re-run scraper-generator. There is no automated feedback loop between eval results and scraper fixes.

## Solution

A new `/scraper-remediation` skill that orchestrates an autonomous eval↔scraper-generator feedback loop. Max 3 fix cycles. If still failing after 3 cycles, escalate to a human for full re-discovery decision.

## Architecture

### Components

1. **`/scraper-remediation` skill (new)** — thin orchestrator that owns the feedback loop. Reads eval diagnostics, invokes scraper-generator in fix mode, re-runs eval, tracks cycles.
2. **Scraper-generator fix mode (new)** — scraper-generator receives a fix request instead of generating from scratch. Makes targeted patches to the existing scraper based on specific eval failures.
3. **Remediation log (new)** — `docs/scraper-remediation/{slug}/remediation_log.json` traces the full ping-pong history.

### Entry Conditions

Before entering the cycle flow, the remediation skill checks:

1. **eval_result.json missing:** Exit with `outcome: "no_action"` and message "Run eval first."
2. **Status is `pass`:** Exit with `outcome: "no_action"`.
3. **Status is `insufficient_data`:** Exit with `outcome: "escalated"` — eval cannot score meaningfully, remediation cannot help. Escalate to human immediately.
4. **Concurrent run guard:** If `remediation_log.json` exists with `started_at` but no `resolved_at`, check the age. If `started_at` is older than 4 hours, treat as a stale lock (previous run crashed) — overwrite and proceed. Otherwise exit.
5. **Status is `degraded` or `fail`:** Enter the triage phase.

### Triage Phase

Before entering fix cycles, distinguish between a scraper problem and a config drift problem:

1. Read eval_result.json `check_details`.
2. **Config drift indicators** — failures that suggest the eval config is stale, not the scraper:
   - `pagination_completeness` failing while `core_attribute_coverage` passes → product count changed, not extraction.
   - `category_diversity` failing while other checks pass → site reorganized categories.
   - `row_count_trend` failing in isolation → product count shifted.
3. **If config drift is detected:** Re-run `/eval-generator` to regenerate eval_config.json with fresh data from the catalog assessment. Then re-run eval. If it passes now, exit with `outcome: "resolved"` (the scraper was fine, the config was stale). If it still fails, continue to fix cycles.
4. **If scraper regression is detected** (attribute coverage, schema conformance, price sanity failures): proceed to fix cycles.

### Scraper Backup

Before the first fix cycle, copy the current scraper to a backup:

```
docs/scraper-generator/{slug}/scraper.py.pre-remediation
```

If all 3 cycles fail and the scraper is worse than before, the human can restore from this backup. The backup is overwritten on each new remediation invocation (not per cycle — we want the pre-remediation state, not the inter-cycle state).

### Cycle Flow

```
/scraper-remediation {slug}
  → Check entry conditions
  → Triage: config drift or scraper regression?
  → If config drift: re-run eval-generator, re-eval, maybe exit early
  → Backup scraper.py → scraper.py.pre-remediation
  → Build fix request from check_details
  → Invoke scraper-generator in fix mode (existing scraper.py + fix request)
  → Scraper-generator patches scraper, runs validation (probe → smoke → final verification)
  → Validator's final verification produces fresh output in docs/scraper-generator/{slug}/output/
  → Re-run eval script against fresh output (no --collect flag, --no-history flag to avoid polluting eval_history.json)
  → If passing: delete baseline.json so next eval creates a fresh baseline, done
  → If scraper-generator returns fix_outcome: "unfixable": escalate immediately, don't waste remaining cycles
  → If still failing AND cycle < 3: loop
  → If cycle == 3: escalate to human
```

### Eval Re-Run Isolation

Remediation eval re-runs must not pollute the production eval history. The eval script is invoked with a `--no-history` flag (new) that:
- Writes eval_result.json as normal (remediation needs to read the result)
- Does NOT append to eval_history.json
- Does NOT update baseline.json

After a successful remediation (`outcome: "resolved"`), the remediation skill deletes `baseline.json` so the next regular eval run creates a fresh baseline from the fixed scraper's output.

### Fix Request Format

The remediation skill reads eval_result.json and builds a fix request for scraper-generator:

```json
{
  "mode": "fix",
  "cycle": 1,
  "slug": "harlowbros",
  "failing_checks": [
    {
      "check": "core_attribute_coverage",
      "value": 0.0,
      "threshold": 0.9,
      "subcategory_details": {
        "wood.softwood_hardwood_lumber": {
          "coverage": 0.0,
          "products": 90,
          "top_missing": [["appearance_grade", 90], ["use_class", 90], ["wood_type", 86]]
        }
      }
    },
    {
      "check": "schema_conformance",
      "value": 0.65,
      "threshold": 1.0
    }
  ],
  "passing_checks": [
    { "check": "price_sanity", "value": 1.0, "threshold": 1.0 },
    { "check": "duplicate_detection", "value": 1.0, "threshold": 0.99 },
    { "check": "data_freshness", "value": 1.0, "threshold": 1.0 },
    { "check": "extra_attributes_ratio", "value": 0.89, "threshold": 0.5 },
    { "check": "semantic_validation", "value": 1.0, "threshold": 0.95 }
  ],
  "scraper_path": "docs/scraper-generator/harlowbros/scraper.py",
  "eval_config_path": "docs/eval-generator/harlowbros/eval_config.json"
}
```

`passing_checks` includes values and thresholds so scraper-generator can avoid regressions (e.g., `duplicate_detection` at 0.995 is barely passing — don't introduce duplicates).

### Remediation Log

Written by the remediation skill to `docs/scraper-remediation/{slug}/remediation_log.json`:

```json
{
  "slug": "harlowbros",
  "started_at": "2026-03-18T14:00:00Z",
  "trigger_eval_score": 44.55,
  "trigger_eval_status": "degraded",
  "triage": "scraper_regression",
  "cycles": [
    {
      "cycle": 1,
      "fix_request": {
        "failing_checks": [
          { "check": "core_attribute_coverage", "value": 0.0, "threshold": 0.9 },
          { "check": "schema_conformance", "value": 0.65, "threshold": 1.0 }
        ]
      },
      "scraper_changes": {
        "summary": "Added name-enrichment patterns for wood_type, appearance_grade. Fixed type conversion for numeric spec table values.",
        "fix_targets": ["core_attribute_coverage", "schema_conformance"],
        "changes": [
          { "type": "enrichment_pattern", "attribute": "wood_type" },
          { "type": "type_conversion", "scope": "spec_table_numeric" }
        ]
      },
      "eval_after": { "score": 32.0, "status": "degraded" }
    },
    {
      "cycle": 2,
      "fix_request": {
        "failing_checks": [
          { "check": "core_attribute_coverage", "value": 0.33, "threshold": 0.9 }
        ]
      },
      "scraper_changes": {
        "summary": "Added description parsing for use_class from product description text.",
        "fix_targets": ["core_attribute_coverage"],
        "changes": [
          { "type": "description_parsing", "attribute": "use_class" }
        ]
      },
      "eval_after": { "score": 18.0, "status": "pass" }
    }
  ],
  "outcome": "resolved",
  "resolved_at": "2026-03-18T14:25:00Z",
  "total_cycles": 2
}
```

`outcome` values: `"resolved"`, `"escalated"`, `"no_action"`.

`triage` values: `"scraper_regression"`, `"config_drift"` (resolved by re-running eval-generator), `"config_drift_then_scraper"` (config was stale AND scraper needed fixes).

`scraper_changes` is read from scraper-generator's validation.json `fix_summary` field (see below) — the remediation skill does not write to scraper-generator's files.

### Scraper-Generator Fix Mode

When scraper-generator receives a fix request (`mode: "fix"`):

**What changes:**
- **Skips the archive step** — patches the scraper in place, does not archive and regenerate
- Reads the existing scraper.py instead of generating from scratch
- Reads the fix request to understand what's broken
- Makes targeted patches (add enrichment patterns, fix type conversions, add selectors, update label maps for non-English sites)
- Adds a `fix_summary` field to validation.json (see format below)
- **Can return `fix_outcome: "unfixable"`** if the problem requires a fundamental approach change (e.g., site switched from HTML to SPA, added bot protection, completely restructured URLs). This short-circuits the remediation loop — no point burning cycles 2-3 on patches that can't work.

**Fix mode orchestrator step flow:**
1. **Step 1 (load context):** Same as normal — reads catalog assessment, company report, SKU schemas, config.json for expected_product_count and category mappings.
2. **Step 2a-2c (code generation):** REPLACED — instead of generating from scratch, reads existing scraper.py and applies targeted patches based on the fix request's failing_checks. If the fix requires changes beyond patching (fundamental site change), set `fix_outcome: "unfixable"` and return.
3. **Step 3 (validation dispatch):** Same as normal — probe, smoke test, final verification. Validator internal retry counters reset fresh each remediation cycle.
4. **Step 4 (diagnostic persistence):** Same, plus writes `fix_summary` to validation.json.

**What stays the same:**
- Same validation phases (probe, smoke test, final verification)
- Same fix cycle limits within validation
- Same escalation rules
- Same output paths

**Boundary:** Scraper-generator doesn't know about eval or remediation cycles. It sees "here's a scraper, here's what's wrong, fix it." The remediation skill owns the loop logic.

**`fix_summary` format in validation.json:**

```json
{
  "fix_summary": {
    "summary": "Added name-enrichment patterns for wood_type, appearance_grade.",
    "fix_outcome": "fixed",
    "fix_targets": ["core_attribute_coverage", "schema_conformance"],
    "changes": [
      { "type": "enrichment_pattern", "attribute": "wood_type" },
      { "type": "type_conversion", "scope": "spec_table_numeric" }
    ]
  }
}
```

`fix_outcome` values: `"fixed"` (patches applied, validation passed), `"partial"` (some fixes applied but validation has issues), `"unfixable"` (fundamental change needed — short-circuits remediation loop).

`changes[].type` is free-form text describing the kind of change. Not a closed enum — scraper-generator describes what it did.

This field is only present when scraper-generator runs in fix mode. The remediation skill reads it to populate the remediation log's `scraper_changes`.

### Cross-Skill Read/Write Boundaries

| Skill | Writes to | Reads from |
|-------|-----------|------------|
| scraper-generator | `docs/scraper-generator/{slug}/` (scraper.py, config.json, output/, validation.json) | catalog assessment, company report, SKU schemas, fix request |
| eval-generator | `docs/eval-generator/{slug}/` (eval_config.json, output/) | scraper source, scraper output, catalog assessment, SKU schemas |
| eval script (eval.py) | `docs/eval-generator/{slug}/output/` (eval_result.json, eval_history.json, baseline.json) | eval_config.json, scraper output |
| scraper-remediation | `docs/scraper-remediation/{slug}/remediation_log.json` | eval_result.json, validation.json |

**Rule:** A skill may read from another skill's output but never write to it. Scraper-remediation invokes the other skills — it doesn't do their work.

**Note:** The remediation skill creates `scraper.py.pre-remediation` in the scraper-generator directory as a backup. This is the one exception to the write rule — it's a safety mechanism, not a skill output.

### Escalation

After 3 failed cycles (or `fix_outcome: "unfixable"` on any cycle), the remediation skill:
1. Writes `"outcome": "escalated"` to remediation_log.json
2. Presents to the human: the cycle history, what was tried, what's still failing
3. Recommends full re-discovery (`/product-discovery`) but the human decides

### Changes to eval.py

The eval script needs a new `--no-history` flag:
- When set: writes eval_result.json but skips appending to eval_history.json and skips baseline creation/updates
- Purpose: remediation eval re-runs should not pollute the production eval history
