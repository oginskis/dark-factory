---
name: eval-generator
description: >
  Generate an eval config for a company that validates scraper quality using the shared eval script.
  Produces an eval_config.json with per-subcategory attribute maps and optional semantic_validation that the shared eval script reads to run thirteen weighted checks against scrape output and report degradation.
  Use this skill when the user wants to create quality validation for an existing scraper —
  "generate eval for X scraper", "create eval config for X", "build eval for X",
  "add quality checks for X scraper", "configure eval for X". Requires a scraper from /scraper-generator to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Eval Generator

Generate an eval config that validates scraper quality using thirteen weighted checks against scrape output.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment | `docs/catalog-detector/{slug}/assessment.md` |
| Scraper source | `docs/scraper-generator/{slug}/scraper.py` |
| Generator input (routing tables) | `docs/scraper-generator/{slug}/generator_input.json` — pre-processed SKU schemas with core/extended keys, types, and units per subcategory |
| Eval products (output) | `docs/eval-generator/{slug}/output/products.jsonl` — eval_run.py writes here via `--output-file` when running the scraper |
| Eval run summary (output) | `docs/eval-generator/{slug}/output/summary.json` — eval_run.py writes here via `--summary-file` when running the scraper |
| Eval debug log (output) | `docs/eval-generator/{slug}/output/debug.log` — eval_run.py writes here via `--log-file` when running the scraper |
| Eval script | `.claude/skills/eval-generator/scripts/eval_run.py` |
| Archived previous runs | `docs/eval-generator/{slug}-archived-{YYYYMMDDTHHMMSS}/` — never read these |
| Eval config (output) | `docs/eval-generator/{slug}/eval_config.json` |
| Eval result (output) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval history (output) | `docs/eval-generator/{slug}/output/eval_history.json` |
| Eval baseline (output) | `docs/eval-generator/{slug}/output/baseline.json` |

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `festool`).

## Eval conditions

All eval conditions — collection strategy, quality checks, thresholds, scoring rules, config format rules — are defined in `references/conditions.md` (single source of truth).

## Workflow

Read and follow `references/workflow.md`.

- **Archive previous run:** Before starting, check if `docs/eval-generator/{slug}/` exists. If it does, archive it: `mv docs/eval-generator/{slug} docs/eval-generator/{slug}-archived-$(date -u +%Y%m%dT%H%M%S)`. Then create the fresh directory: `mkdir -p docs/eval-generator/{slug}/output`. Every invocation generates from scratch — never read from or make decisions based on archived directories (`{slug}-archived-*`).
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "the catalog assessment", "the generator input file", "the eval result file").
- The `missing_generator_input` decision has an autonomous resolution path: re-run the prepare script to generate `generator_input.json`. Only escalate if the scraper-generator stage has never been run for this company.
- The `missing_product_count_estimate` decision is handled autonomously without escalation — the workflow uses the best available estimate (from scraper source, category structure, or current output count). No user interaction needed.
- No web search or browsing tools are needed — this stage generates a config file locally.

## Escalation handling

When the workflow reaches an escalation point, present it to the user using this format and **wait for their response** before continuing:

```
**Escalation: `{decision_name}`**
**Stage:** Eval Generator
{One-sentence summary — from the decision's Context field.}
{Escalation payload — the specific evidence or candidates the workflow gathered.}
**Your options:**
1. {Action to resolve and continue}
2. {Alternative action, if applicable}
3. Stop — skip this company and end the pipeline
```

User options per escalation:
- `missing_generator_input` — 1) Run `/scraper-generator {slug}` to produce the scraper and generator input, then retry, 2) Stop
- `scraper_output_format_unclear` — 1) Fix the scraper and retry, 2) Describe the expected output format so the eval can be generated, 3) Stop

## Notes

File-driven skill — no database or external services required.
