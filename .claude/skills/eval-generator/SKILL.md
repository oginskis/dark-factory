---
name: eval-generator
description: >
  Generate an eval config for a company that validates scraper quality using the shared eval script.
  Produces an eval_config.json that the shared eval script reads to run twelve weighted checks (with core/extended attribute split) against scrape output and report degradation.
  Use this skill when the user wants to create quality validation for an existing scraper —
  "generate eval for X scraper", "create eval config for X", "build eval for X",
  "add quality checks for X scraper", "configure eval for X". Requires a scraper from /scraper-generator to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Eval Generator

Read and follow the agent instructions in `agents/eval-generator.md`.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment | `docs/catalog-detector/{slug}.md` |
| Scraper source | `docs/scraper-generator/{slug}/scraper.py` |
| Product taxonomy categories | `docs/product-taxonomy/categories.md` |
| SKU schema | `docs/product-taxonomy/sku-schemas/{category-slug}.md` |
| Scrape output (products) | `docs/scraper-generator/{slug}/output/products.jsonl` |
| Scrape run summary | `docs/scraper-generator/{slug}/output/summary.json` |
| Shared eval script | `eval/eval.py` |
| Eval config (output) | `docs/eval-generator/{slug}/eval_config.json` |
| Eval result (output) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval history (output) | `docs/eval-generator/{slug}/output/eval_history.json` |
| Eval baseline (output) | `docs/eval-generator/{slug}/output/baseline.json` |

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `festool`).
- **`{category-slug}`** — derived from the subcategory display name corresponding to the company's Primary taxonomy ID. Look up the taxonomy ID in `categories.md` to find the display name, then slugify: lowercase, replace spaces with hyphens, drop special characters (`&`, `/`, `(`, `)`, `,`). Example: taxonomy ID `wood.softwood_hardwood_lumber` → display name "Softwood & Hardwood Lumber" → slug `softwood-hardwood-lumber`.

## Eval and the four-level product record

The eval validates scraper output against the four-level product record format (see scraper-generator skill for the canonical definition). Check weights reflect the extraction effort hierarchy:

| Level | Eval check | Weight | Threshold | Rationale |
|-------|-----------|--------|-----------|-----------|
| Universal top-level | Hardcoded in eval script | — | — | Always validated (sku, name, url, price, etc.) |
| `core_attributes` | `core_attribute_coverage` | 20 | 0.90 | High effort expected → strict validation |
| `extended_attributes` | `extended_attribute_coverage` | 5 | 0.50 | Moderate effort → lighter validation |
| `extra_attributes` | `extra_attributes_ratio` | 5 | 0.50 | Low effort / opportunistic → monitors schema adequacy |

## Claude Code wiring

- Provide the file paths from the table above when the agent references logical resources (e.g., "the scraper source", "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the scrape output file", "the scrape run summary", "the shared eval script", "the eval config file", "the eval result file", "the eval history file", "the eval baseline file").
- When the agent reaches an escalation point, present it to the user using this format and **wait for their response** before continuing:
  ```
  **Escalation: `{decision_name}`**
  **Stage:** Eval Generator
  {One-sentence summary — from the decision's Context field.}
  {Escalation payload — the specific evidence the agent gathered.}
  **Your options:**
  1. {Action to resolve and continue}
  2. {Alternative action, if applicable}
  3. Stop — skip this company and end the pipeline
  ```
  User options per escalation:
  - `no_sku_schema` (taxonomy issue) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
  - `scraper_output_format_unclear` — 1) Fix the scraper and retry, 2) Describe the expected output format so the eval can be generated, 3) Stop
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema hasn't been created yet, invoke `/product-taxonomy` for that subcategory to generate the schema, then continue. Only escalate if the subcategory itself is missing from the taxonomy.
- Run the shared eval script for verification: `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`
- The `missing_product_count_estimate` decision is handled autonomously without escalation — the agent uses the best available estimate (from scraper source, category structure, or current output count). This is a graceful degradation, not a stop. No user interaction needed.
- No web search or browsing tools are needed — this stage generates a config file locally.

## Notes

File-driven skill — no database or external services required.
