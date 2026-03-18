---
name: scraper-remediation
description: >
  Autonomous feedback loop between eval results and scraper-generator that detects degradation, triages config drift vs scraper regression, and applies up to 3 targeted fix cycles.
  Produces a remediation_log.json tracing every cycle (eval diagnosis, scraper fix, re-eval result) and the final outcome.
  Use this skill when eval detects scraper degradation —
  "fix scraper for X", "remediate X scraper", "scraper for X is degraded", "run remediation for X".
  Requires both eval results from /eval-generator and a scraper from /scraper-generator to exist first.
  If the user wants the full pipeline from scratch, use /product-discovery instead.
user-invocable: true
---

# Scraper Remediation

Autonomous eval↔scraper-generator feedback loop. Detects degradation, triages the cause, applies up to 3 targeted fix cycles, escalates to human if unresolved.

## Input

`$ARGUMENTS` is the company slug (e.g., `harlowbros`).

## File locations

| Resource | Path |
|----------|------|
| Eval result (read) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval config (read) | `docs/eval-generator/{slug}/eval_config.json` |
| Eval baseline (read/delete) | `docs/eval-generator/{slug}/output/baseline.json` |
| Scraper source (read, backup) | `docs/scraper-generator/{slug}/scraper.py` |
| Scraper validation (read) | `docs/scraper-generator/{slug}/output/validation.json` |
| Scraper backup (write) | `docs/scraper-generator/{slug}/scraper.py.pre-remediation` |
| Shared eval script | `eval/eval.py` |
| Remediation log (output) | `docs/scraper-remediation/{slug}/remediation_log.json` |

## Workflow

Read and follow `references/workflow.md`.

- Provide the file paths from the table above when the workflow references logical resources.
- The triage phase may invoke `/eval-generator` to regenerate eval_config.json if config drift is detected. This is the only case where another skill is invoked before entering fix cycles.
- Fix cycles invoke `/scraper-generator` in fix mode — pass the fix request JSON as input (see workflow for format).
- Re-run eval after each fix cycle: `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json --no-history`
- After successful remediation, delete `docs/eval-generator/{slug}/output/baseline.json` so the next regular eval creates a fresh baseline.
- Create the output directory before writing: `mkdir -p docs/scraper-remediation/{slug}`

## Escalation handling

When the workflow reaches an escalation point, present it to the user using this format and **wait for their response** before continuing:

```
**Escalation: `{decision_name}`**
**Stage:** Scraper Remediation
{One-sentence summary — from the decision's Context field.}
{Escalation payload — the specific evidence or candidates the workflow gathered.}
**Your options:**
1. {Action to resolve and continue}
2. {Alternative action, if applicable}
3. Stop — skip this company
```

User options per escalation:
- `unfixable_scraper` — 1) Run full re-discovery (`/product-discovery`), 2) Manually fix the scraper and re-run `/eval-generator`, 3) Stop
- `cycles_exhausted` — 1) Run full re-discovery (`/product-discovery`), 2) Manually investigate and fix, 3) Stop
- `insufficient_data_escalation` — 1) Check scraper output and re-run manually, 2) Run full re-discovery (`/product-discovery`), 3) Stop

## Notes

File-driven skill — reads eval and scraper artifacts, writes only to `docs/scraper-remediation/{slug}/`. One exception: creates `scraper.py.pre-remediation` backup in the scraper-generator directory before the first fix cycle.
