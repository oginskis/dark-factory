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
3. **Remediation log (new)** — `docs/eval-generator/{slug}/output/remediation_log.json` traces the full ping-pong history.

### Cycle Flow

```
/scraper-remediation {slug}
  → Reads eval_result.json
  → If not degraded/failed: exit, nothing to fix
  → Builds fix request from check_details
  → Invokes scraper-generator in fix mode (existing scraper.py + fix request)
  → Scraper-generator patches scraper, re-runs validation
  → Re-runs eval against new output
  → If passing: done
  → If still failing AND cycle < 3: loop
  → If cycle == 3: escalate to human
```

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
  "passing_checks": ["price_sanity", "duplicate_detection", "data_freshness", "extra_attributes_ratio", "semantic_validation"],
  "scraper_path": "docs/scraper-generator/harlowbros/scraper.py",
  "eval_config_path": "docs/eval-generator/harlowbros/eval_config.json"
}
```

Scraper-generator reads this and makes targeted patches — adding enrichment patterns, fixing type conversions, adding selectors — instead of regenerating from scratch.

### Remediation Log

Written by the remediation skill to `docs/eval-generator/{slug}/output/remediation_log.json`:

```json
{
  "slug": "harlowbros",
  "started_at": "2026-03-18T14:00:00Z",
  "trigger_eval_score": 44.55,
  "trigger_eval_status": "degraded",
  "cycles": [
    {
      "cycle": 1,
      "fix_request": { "failing_checks": ["core_attribute_coverage", "schema_conformance"] },
      "scraper_changes": "Added name-enrichment patterns for wood_type, appearance_grade. Fixed type conversion for numeric spec table values.",
      "eval_after": { "score": 32.0, "status": "degraded" }
    },
    {
      "cycle": 2,
      "fix_request": { "failing_checks": ["core_attribute_coverage"] },
      "scraper_changes": "Added description parsing for use_class from product description text.",
      "eval_after": { "score": 18.0, "status": "pass" }
    }
  ],
  "outcome": "resolved",
  "resolved_at": "2026-03-18T14:25:00Z",
  "total_cycles": 2
}
```

`outcome` values: `"resolved"` (eval passes), `"escalated"` (3 cycles exhausted → human notified), `"no_action"` (eval was already passing).

`scraper_changes` is read from scraper-generator's validation.json `fix_summary` field — the remediation skill does not write to scraper-generator's files.

### Scraper-Generator Fix Mode

When scraper-generator receives a fix request (`mode: "fix"`):

**What changes:**
- Reads the existing scraper.py instead of generating from scratch
- Reads the fix request to understand what's broken
- Makes targeted patches (add enrichment patterns, fix type conversions, add selectors)
- Adds a `fix_summary` field to validation.json describing what it changed

**What stays the same:**
- Same validation phases (probe, smoke test, final verification)
- Same fix cycle limits within validation
- Same escalation rules
- Same output paths

**Boundary:** Scraper-generator doesn't know about eval or remediation cycles. It sees "here's a scraper, here's what's wrong, fix it." The remediation skill owns the loop logic.

### Cross-Skill Read/Write Boundaries

| Skill | Writes to | Reads from |
|-------|-----------|------------|
| scraper-generator | `docs/scraper-generator/{slug}/` (scraper.py, config.json, output/, validation.json) | catalog assessment, company report, SKU schemas |
| eval-generator | `docs/eval-generator/{slug}/` (eval_config.json, output/) | scraper source, scraper output, catalog assessment, SKU schemas |
| eval script (eval.py) | `docs/eval-generator/{slug}/output/` (eval_result.json, eval_history.json, baseline.json) | eval_config.json, scraper output |
| scraper-remediation | `docs/eval-generator/{slug}/output/remediation_log.json` | eval_result.json, validation.json |

**Rule:** A skill may read from another skill's output but never write to it. Scraper-remediation invokes the other skills — it doesn't do their work.

### Escalation

After 3 failed cycles, the remediation skill:
1. Writes `"outcome": "escalated"` to remediation_log.json
2. Presents to the human: the 3-cycle history, what was tried, what's still failing
3. Recommends full re-discovery (`/product-discovery`) but the human decides
