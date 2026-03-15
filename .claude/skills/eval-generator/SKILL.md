---
name: eval-generator
description: >
  Generate an eval config for a company that validates scraper quality using the shared eval script.
  Produces an eval_config.json that the shared eval script reads to run twelve weighted checks (with core/extended attribute split) against scrape output and report degradation.
  Supports both v1 (flat attributes) and v2 (core_attributes, extended_attributes, extra_attributes) scraper output formats.
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

## Claude Code wiring

- Provide the file paths from the table above when the agent references logical resources (e.g., "the scraper source", "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the scrape output file", "the scrape run summary", "the shared eval script", "the eval config file", "the eval result file", "the eval history file", "the eval baseline file").
- When the agent reaches an escalation point, present it using the standard escalation format (see orchestrator) and **wait for the user's response** before continuing. User options per escalation:
  - `no_sku_schema` (taxonomy issue) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
  - `scraper_output_format_unclear` — 1) Fix the scraper and retry, 2) Describe the expected output format so the eval can be generated
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema hasn't been created yet, invoke `/product-taxonomy` for that subcategory to generate the schema, then continue. Only escalate if the subcategory itself is missing from the taxonomy.
- Run the shared eval script for verification: `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`
- The `missing_product_count_estimate` decision is handled autonomously without escalation — the agent skips the pagination completeness check and redistributes its weight. This is a graceful degradation, not a stop. No user interaction needed.
- The eval config includes an `output_format` field (1 or 2) that tells the shared eval script how to interpret product records. v1 uses flat `attributes`; v2 uses `core_attributes`, `extended_attributes`, `extra_attributes`. For v1, `extended_attribute_coverage` and `extra_attributes_ratio` checks are skipped and their weights are redistributed.
- No web search or browsing tools are needed — this stage generates a config file locally.

## Notes

File-driven skill — no database or external services required.
