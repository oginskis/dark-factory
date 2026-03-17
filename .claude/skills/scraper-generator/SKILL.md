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
| Catalog assessment | `docs/catalog-detector/{slug}.md` |
| Product taxonomy categories | `docs/product-taxonomy/categories.md` |
| SKU schema | `docs/product-taxonomy/sku-schemas/{category-slug}.md` |
| Platform knowledgebase | `docs/platform-knowledgebase/{platform-slug}.md` |
| Persist hook implementations | `.claude/skills/scraper-generator/references/persist-hooks.md` |
| Scraper output dir | `docs/scraper-generator/{slug}/` |
| Scraper script (output) | `docs/scraper-generator/{slug}/scraper.py` |
| Config metadata (output) | `docs/scraper-generator/{slug}/config.json` |
| Product data (output) | `docs/scraper-generator/{slug}/output/products.jsonl` |
| Run summary (output) | `docs/scraper-generator/{slug}/output/summary.json` |
| Generator input (pre-processed) | `docs/scraper-generator/{slug}/generator_input.json` |
| Language seed (non-English) | `docs/platform-knowledgebase/labels-{lang}.json` |
| Validation diagnostics (output) | `docs/scraper-generator/{slug}/output/validation.json` |
| Debug log (output) | `docs/scraper-generator/{slug}/output/debug.log` |

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `topwoodtimber`).
- **`{category-slug}`** — derived from the subcategory display name corresponding to the company's Primary taxonomy ID. Look up the taxonomy ID in `categories.md` to find the display name, then slugify: lowercase, replace spaces with hyphens, drop special characters (`&`, `/`, `(`, `)`, `,`). Example: taxonomy ID `wood.softwood_hardwood_lumber` → display name "Softwood & Hardwood Lumber" → slug `softwood-hardwood-lumber`.
- **`{platform-slug}`** — the platform name from the catalog assessment, lowercased. Example: WooCommerce → `woocommerce`, Shopify → `shopify`. If platform is `unknown` or `custom`, there is no knowledgebase file — skip it.

## Workflow

Read and follow `references/orchestrator.md`.

- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the platform knowledgebase", "the persist hooks reference file", "the pre-processed generator input file", "the language seed file").
- Dispatch the validator sub-agent using the Agent tool as directed by the orchestrator. Sub-agent file: `.claude/skills/scraper-generator/references/validator.md` — probe testing and smoke tests. The orchestrator specifies what data to pass and when to dispatch.
- The orchestrator handles label mapping and code generation inline (no sub-agent dispatch for these). Reference file `references/code-generator.md` defines the canonical product record format, library selection, required behavior, and code quality rules — the orchestrator reads it inline during Step 2c.
- Before starting the orchestrator, run the pre-processing script to build routing tables: `uv run python .claude/skills/scraper-generator/scripts/prepare_generator_input.py --schemas {taxonomy_ids} --output docs/scraper-generator/{slug}/generator_input.json` where `{taxonomy_ids}` are the space-separated subcategory taxonomy IDs from the company report.
- For non-English sites, check for a language seed file at `docs/platform-knowledgebase/labels-{lang}.json` where `{lang}` is the ISO 639-1 language code from the catalog assessment. If it exists, provide it to the orchestrator. After successful scraper generation, save the updated label map back to the seed file.
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema file hasn't been created yet, automatically invoke `/product-taxonomy` for that subcategory to generate the schema, then continue without user interaction. Before concluding a schema is missing, **list the `docs/product-taxonomy/sku-schemas/` directory** and search for the subcategory name — never guess the filename from a partial slug.
- Run the scraper using `uv run` (not `uv run python`). The PEP 723 inline metadata in the script declares its own dependencies, so `uv` resolves them automatically.
- Smoke test: `uv run docs/scraper-generator/{slug}/scraper.py --limit 10 2>docs/scraper-generator/{slug}/output/debug.log` with a 2-minute timeout (Bash tool timeout: 120000ms).
- Final verification: `uv run docs/scraper-generator/{slug}/scraper.py --limit {sample_size} 2>docs/scraper-generator/{slug}/output/debug.log` with timeout `max(120, sample_size * 6)` seconds (Bash tool timeout: `max(120000, sample_size * 6000)` ms).
- Probe: `uv run docs/scraper-generator/{slug}/scraper.py --probe <URL>` — the scraper fetches the page internally, prints JSON to stdout. No web fetch tools needed for probing.
- No web search or Playwright browser tools are needed.
- The knowledgebase write (Step 3) uses file write/edit tools to create or append to the platform knowledgebase file.
- Data persistence: read the persist hook implementations file for the `setup`/`persist`/`teardown` functions to include in the generated scraper. Write the scraper code to the scraper script path before running tests (so `uv run` can execute it). The scraper code is final once the validator returns `pass`. After config metadata is prepared (Step 4), persist it as JSON to the config metadata path.
- Diagnostic persistence: after the validator returns (any status, any language), write its output plus `generated_at` as JSON to the validation diagnostics path. On re-dispatch, overwrite the previous file.
- The canonical product record format definition lives in `references/code-generator.md`.

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
