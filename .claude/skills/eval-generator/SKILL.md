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
| Scrape output (products) | `docs/scraper-generator/{slug}/output/products.jsonl` — eval.py writes here via `--output-file` when running the scraper |
| Scrape run summary | `docs/scraper-generator/{slug}/output/summary.json` — eval.py writes here via `--summary-file` when running the scraper |
| Shared eval script | `eval/eval.py` |
| Archived previous runs | `docs/eval-generator/{slug}-archived-{YYYYMMDDTHHMMSS}/` — never read these |
| Eval config (output) | `docs/eval-generator/{slug}/eval_config.json` |
| Eval result (output) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval history (output) | `docs/eval-generator/{slug}/output/eval_history.json` |
| Eval baseline (output) | `docs/eval-generator/{slug}/output/baseline.json` |

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `festool`).

## Eval and the four-level product record

The eval validates scraper output against the four-level product record format (see `.claude/skills/scraper-generator/references/coder.md` for the canonical definition). Check weights reflect the extraction effort hierarchy:

| Level | Eval check | Weight | Threshold | Rationale |
|-------|-----------|--------|-----------|-----------|
| Mandatory core | Hardcoded in eval script | — | — | Always validated (sku, name, url, price, etc.) |
| `core_attributes` | `core_attribute_coverage` | 20 | 0.90 | High effort expected → strict validation |
| `extended_attributes` | `extended_attribute_coverage` | 5 | 0.50 | Moderate effort → lighter validation |
| `extra_attributes` | `extra_attributes_ratio` | 5 | 0.50 | Low effort / opportunistic → monitors schema adequacy |

## Workflow

Read and follow `references/workflow.md`.

- **Archive previous run:** Before starting, check if `docs/eval-generator/{slug}/` exists. If it does, archive it: `mv docs/eval-generator/{slug} docs/eval-generator/{slug}-archived-$(date -u +%Y%m%dT%H%M%S)`. Then create the fresh directory: `mkdir -p docs/eval-generator/{slug}/output`. Every invocation generates from scratch — never read from or make decisions based on archived directories (`{slug}-archived-*`).
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the scraper source", "the company report", "the catalog assessment", "the generator input file", "the scrape output file", "the scrape run summary", "the shared eval script", "the eval config file", "the eval result file", "the eval history file", "the eval baseline file").
- The `missing_generator_input` decision has an autonomous resolution path: re-run the prepare script to generate `generator_input.json`. Only escalate if the scraper-generator stage has never been run for this company.
- Run the shared eval script for verification — see the commands reference below for the correct invocation.
- The `missing_product_count_estimate` decision is handled autonomously without escalation — the workflow uses the best available estimate (from scraper source, category structure, or current output count). This is a graceful degradation, not a stop. No user interaction needed.
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

## Eval commands

The shared eval script (`eval/eval.py`) supports these invocations:

| Command | When to use |
|---------|-------------|
| `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json --collect` | **Primary verification.** Runs the scraper to collect a sufficient sample, then scores. Use this in Step 5 to validate the config end-to-end. |
| `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json` | Score existing scraper output only (no scraper invocation). Use when `products.jsonl` already exists and you just want to re-score. |
| `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json --no-history` | Score without updating `eval_history.json` or baseline. Use for remediation re-runs where you don't want to pollute the history timeline. |

## Notes

File-driven skill — no database or external services required.
