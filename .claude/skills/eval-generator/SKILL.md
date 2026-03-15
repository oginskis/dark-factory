---
name: eval-generator
description: >
  Generate a standalone eval script that validates scraper quality for a company.
  Produces an eval.py that runs seven weighted checks against scrape output and reports degradation.
  Use this skill when the user wants to create quality validation for an existing scraper —
  "generate eval for X scraper", "create validation for X", "build eval script for X",
  "add quality checks for X scraper". Requires a scraper from /scraper-generator to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Eval Generator

Read and follow the agent instructions in `agents/eval-generator.md`.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS`.
- **`{category-slug}`** — derived from the **subcategory** in the company report's Primary classification. Take the part after ` > `, lowercase it, replace spaces with hyphens, drop special characters. Example: `Wood Products & Lumber > Softwood & Hardwood Lumber` → `softwood-hardwood-lumber`.

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment | `docs/catalog-detector/{slug}.md` |
| Scraper source | `docs/scraper-generator/{slug}/scraper.py` |
| Product taxonomy categories | `docs/product-taxonomy/categories.md` |
| SKU schema | `docs/product-taxonomy/sku-schemas/{category-slug}.md` (see slug derivation below) |
| Scrape output (products) | `docs/scraper-generator/{slug}/output/products.jsonl` |
| Scrape run summary | `docs/scraper-generator/{slug}/output/summary.json` |
| Eval script (output) | `docs/eval-generator/{slug}/eval.py` |
| Eval result (output) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval history (output) | `docs/eval-generator/{slug}/output/eval_history.json` |

## Claude Code wiring

- Provide the file paths from the table above when the agent references logical resources (e.g., "the scraper source", "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the scrape output file", "the scrape run summary", "the eval result file", "the eval history file").
- When the agent reaches an escalation point, present it using the standard escalation format (see orchestrator) and **wait for the user's response** before continuing. User options per escalation:
  - `no_sku_schema` (taxonomy issue) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
  - `scraper_output_format_unclear` — 1) Fix the scraper and retry, 2) Describe the expected output format so the eval can be generated
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema hasn't been created yet, invoke `/product-taxonomy` for that subcategory to generate the schema, then continue. Only escalate if the subcategory itself is missing from the taxonomy.
- Run the eval script using `uv run` (not `uv run python`) for verification. The PEP 723 inline metadata in the script declares its Python version requirement, so `uv` resolves it automatically.
- The `missing_product_count_estimate` decision is handled autonomously without escalation — the agent skips the pagination completeness check and redistributes its weight. This is a graceful degradation, not a stop. No user interaction needed.
- No web search or browsing tools are needed — this stage generates code locally.

## Notes

File-driven skill — no database or external services required.
