---
name: scraper-generator
description: >
  Generate a production-ready Python scraper for a company's product catalog.
  Produces a standalone scraper.py, config.json, and test output.
  Scrapers output the four-level product record format with universal top-level fields, core_attributes, extended_attributes, and extra_attributes.
  Use this skill when the user wants to create a scraper for a company that already has a catalog assessment —
  "generate scraper for X", "create scraper for X", "build a scraper for X products", "scrape X's catalog".
  Requires both a company report from /product-classifier and a catalog assessment from /catalog-detector to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Scraper Generator

Generate a production-ready Python scraper for a company's product catalog, validated via probe testing and smoke tests.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment | `docs/catalog-detector/{slug}/assessment.md` |
| Product taxonomy categories | `docs/product-taxonomy/categories.md` |
| SKU schema | `docs/product-taxonomy/sku-schemas/{category-slug}.md` |
| Platform knowledgebase | `docs/platform-knowledgebase/{platform-slug}.md` |
| Scraper output dir | `docs/scraper-generator/{slug}/` |
| Archived previous runs | `docs/scraper-generator/{slug}-archived-{YYYYMMDDTHHMMSS}/` — never read these |
| Scraper script (output) | `docs/scraper-generator/{slug}/scraper.py` |
| Config metadata (output) | `docs/scraper-generator/{slug}/config.json` |
| Generator input (pre-processed) | `docs/scraper-generator/{slug}/generator_input.json` |
| Language seed (non-English) | `docs/platform-knowledgebase/labels-{lang}.json` |
| Test report (output) | `docs/scraper-generator/{slug}/output/report_{n}_{hash}.json` — never overwritten |
| Validation diagnostics (output) | `docs/scraper-generator/{slug}/output/validation_{n}_{hash}.json` — never overwritten |
| Products (output) | `docs/scraper-generator/{slug}/output/products_{n}_{hash}.jsonl` — never overwritten |
| Run summary (output) | `docs/scraper-generator/{slug}/output/summary_{n}_{hash}.json` — never overwritten |
| Debug log (output) | `docs/scraper-generator/{slug}/output/debug_{n}_{hash}.log` — never overwritten |
| Baseline products (output) | `docs/scraper-generator/{slug}/output/baseline_products.jsonl` — overwritten per test cycle |
| Test status viewer (utility) | `.claude/skills/scraper-generator/scripts/util_show_test_status.py` — accepts file or directory |

### Output file versioning

All output files in `output/` use `{name}_{n}_{hash}.{ext}` naming. **Files are never overwritten.**

- **`{n}`** — iteration number. Starts at 1 for the first test run, increments for each retest cycle.
- **`{hash}`** — 4 random hex chars (`os.urandom(2).hex()`), generated fresh per `tester_run_scraper.py` invocation. Each invocation creates its own uniquely-named files.

**How it works:** Each call to `tester_run_scraper.py` generates a unique hash and creates files like `products_1_a3f2.jsonl`. A second call in the same iteration gets a different hash — `products_1_b7c1.jsonl`. No file is ever overwritten. The evaluators glob `products_{n}_*.jsonl` and `summary_{n}_*.json` to find all files for an iteration.

**Finding files for an iteration:** Glob `{name}_{n}_*.{ext}` in the output directory. Multiple files per name per iteration is normal (one from categories, one from depth).

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `topwoodtimber`).
- **`{category-slug}`** — derived from the subcategory display name corresponding to the company's Primary taxonomy ID. Look up the taxonomy ID in `categories.md` to find the display name, then slugify: lowercase, replace spaces with hyphens, drop special characters (`&`, `/`, `(`, `)`, `,`). Example: taxonomy ID `wood.softwood_hardwood_lumber` → display name "Softwood & Hardwood Lumber" → slug `softwood-hardwood-lumber`.
- **`{platform-slug}`** — the platform name from the catalog assessment, lowercased. Example: WooCommerce → `woocommerce`, Shopify → `shopify`. If platform is `unknown` or `custom`, there is no knowledgebase file — skip it.

## Workflow

Read and follow `references/orchestrator.md`. It defines all steps, decisions, constants, and the fix→retest loop. The coder contract is in `references/coder.md`, the tester contract in `references/tester.md`.

### Before starting the orchestrator

1. **Archive previous run:** If `docs/scraper-generator/{slug}/` exists, archive it: `mv docs/scraper-generator/{slug} docs/scraper-generator/{slug}-archived-$(date -u +%Y%m%dT%H%M%S)`. Then `mkdir -p docs/scraper-generator/{slug}/output`. Never read archived directories.
2. **Build routing tables:** `uv run .claude/skills/scraper-generator/scripts/orchestrator_prepare_generator_input.py --schemas {taxonomy_ids} --output docs/scraper-generator/{slug}/generator_input.json` — `{taxonomy_ids}` are space-separated subcategory IDs from the company report. Exit 1 = some schemas missing (orchestrator resolves in Step 2). Exit 2 = crash, stop.
3. **Language seed (non-English only):** Check for `docs/platform-knowledgebase/labels-{lang}.json`. If it exists, provide it to the orchestrator. Save the updated label map back after successful generation.

### Dispatching sub-agents

- **Coder:** `.claude/skills/scraper-generator/references/coder.md` — writes and patches `scraper.py`.
- **Tester:** `.claude/skills/scraper-generator/references/tester.md` — runs scraper, evaluates output, writes `report_{n}_{hash}.json`.
- Include these rules in every sub-agent dispatch prompt:
  1. Only read files listed in your input contract. No other scrapers, no archived runs, no files outside the company's directory.
  2. Run external commands in the foreground. Never use background tasks.

### Operational notes

- Run scrapers with `uv run` (not `uv run python`). PEP 723 metadata resolves dependencies automatically.
- No web search or Playwright browser tools needed. Scrapers fetch pages internally.
- The `no_sku_schema` decision has an autonomous resolution: invoke `/product-taxonomy` for the missing subcategory. Before concluding a schema is missing, **list `docs/product-taxonomy/sku-schemas/`** — never guess the filename.

## Escalation handling

When the workflow reaches an escalation point, present it to the user using this format and **wait for their response** before continuing:

```
**Escalation: `{decision_name}`**
**Stage:** Scraper Generator
{One-sentence summary — from the decision's Context field.}
{Escalation payload — the specific evidence or candidates the workflow gathered.}
**Your options:**
1. {Action to resolve and continue}
2. {Alternative action, if applicable}
3. Stop — skip this company and end the pipeline
```

User options per escalation:
- `missing_catalog_assessment` — 1) Run `/catalog-detector {slug}` first, then retry, 2) Stop
- `no_sku_schema` (taxonomy issue, only escalates when subcategory is missing from taxonomy) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
- `label_coverage_insufficient` — 1) Provide additional label-to-schema mappings for the site, 2) Expand the relevant SKU schemas with missing attribute keys, 3) Stop
- `probe_extraction_failed` — 1) Provide guidance on how to extract from this site, 2) Stop
- `scraper_test_failed` — 1) Provide debugging guidance or site-specific hints, 2) Stop
- `unmapped_url_prefix` — 1) Provide the correct taxonomy ID for the URL prefix, 2) Stop

## Notes

File-driven skill — no database or external services required.
