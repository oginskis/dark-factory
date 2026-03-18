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
| Product data (output) | `docs/scraper-generator/{slug}/output/products.jsonl` |
| Baseline products (output) | `docs/scraper-generator/{slug}/output/baseline_products.jsonl` |
| Run summary (output) | `docs/scraper-generator/{slug}/output/summary.json` |
| Generator input (pre-processed) | `docs/scraper-generator/{slug}/generator_input.json` |
| Language seed (non-English) | `docs/platform-knowledgebase/labels-{lang}.json` |
| Test report, current iteration (output) | `docs/scraper-generator/{slug}/output/test_report.json` |
| Test reports history (output) | `docs/scraper-generator/{slug}/output/test_reports.json` |
| Test summary, human-readable (output) | `docs/scraper-generator/{slug}/output/test_summary.txt` |
| Per-iteration products (output) | `docs/scraper-generator/{slug}/output/products_iteration_{N}.jsonl` |
| Per-iteration debug log (output) | `docs/scraper-generator/{slug}/output/debug_iteration_{N}.log` |
| Validation diagnostics (output) | `docs/scraper-generator/{slug}/output/validation.json` |
| Debug log (output) | `docs/scraper-generator/{slug}/output/debug.log` |
| Test status viewer (utility) | `.claude/skills/scraper-generator/scripts/util_show_test_status.py` |

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `topwoodtimber`).
- **`{category-slug}`** — derived from the subcategory display name corresponding to the company's Primary taxonomy ID. Look up the taxonomy ID in `categories.md` to find the display name, then slugify: lowercase, replace spaces with hyphens, drop special characters (`&`, `/`, `(`, `)`, `,`). Example: taxonomy ID `wood.softwood_hardwood_lumber` → display name "Softwood & Hardwood Lumber" → slug `softwood-hardwood-lumber`.
- **`{platform-slug}`** — the platform name from the catalog assessment, lowercased. Example: WooCommerce → `woocommerce`, Shopify → `shopify`. If platform is `unknown` or `custom`, there is no knowledgebase file — skip it.

## Workflow

Read and follow `references/orchestrator.md`.

- **Archive previous run:** Before starting, check if `docs/scraper-generator/{slug}/` exists. If it does, archive it: `mv docs/scraper-generator/{slug} docs/scraper-generator/{slug}-archived-$(date -u +%Y%m%dT%H%M%S)`. Then create the fresh directory: `mkdir -p docs/scraper-generator/{slug}/output`. Every invocation generates from scratch — never read from or make decisions based on archived directories (`{slug}-archived-*`).
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the pre-processed generator input file", "the language seed file").
- Dispatch the coder sub-agent using the Agent tool as directed by the orchestrator. Sub-agent file: `.claude/skills/scraper-generator/references/coder.md` — writes and patches `scraper.py`. The orchestrator specifies what data to pass and when to dispatch.
- Dispatch the tester sub-agent using the Agent tool as directed by the orchestrator. Sub-agent file: `.claude/skills/scraper-generator/references/tester.md` — runs scraper, evaluates output, writes `test_report.json`. The orchestrator specifies what data to pass and when to dispatch.
- **Sub-agent rules** — include these in every sub-agent dispatch prompt:
  1. Only read files listed in your input contract. No other scrapers, no archived runs, no files outside the company's directory.
  2. Run external commands in the foreground. Never use background tasks.
- The orchestrator handles label mapping inline. It dispatches the coder for code generation and the tester for validation — it never writes code or runs the scraper itself.
- Before starting the orchestrator, run the pre-processing script to build routing tables: `uv run .claude/skills/scraper-generator/scripts/orchestrator_prepare_generator_input.py --schemas {taxonomy_ids} --output docs/scraper-generator/{slug}/generator_input.json` where `{taxonomy_ids}` are the space-separated subcategory taxonomy IDs from the company report. If exit code is 1, some schemas are missing — read the `errors` array from stdout to identify them. The orchestrator resolves these in Step 2 via the `no_sku_schema` decision. If exit code is 2, the script crashed — report the error and stop.
- For non-English sites, check for a language seed file at `docs/platform-knowledgebase/labels-{lang}.json` where `{lang}` is the ISO 639-1 language code from the catalog assessment. If it exists, provide it to the orchestrator. After successful scraper generation, save the updated label map back to the seed file.
- For non-English sites, when `test_report.json` reveals low label coverage or issues referencing unknown attribute labels, the orchestrator enters a label extension retry: it reads the unmapped labels from the test report, extends the LABEL_MAP, and re-dispatches the coder and tester. Max 3 label extension attempts before escalating `label_coverage_insufficient`.
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema file hasn't been created yet, automatically invoke `/product-taxonomy` for that subcategory to generate the schema, then continue without user interaction. Before concluding a schema is missing, **list the `docs/product-taxonomy/sku-schemas/` directory** and search for the subcategory name — never guess the filename from a partial slug.
- Run the scraper using `uv run` (not `uv run python`). The PEP 723 inline metadata in the script declares its own dependencies, so `uv` resolves them automatically.
- Probe: `uv run docs/scraper-generator/{slug}/scraper.py --probe <URL>` — the scraper fetches the page internally, prints JSON to stdout. No web fetch tools needed for probing.
- Category-scoped run: `uv run docs/scraper-generator/{slug}/scraper.py --categories "/shop/timber-joinery" --limit 10` — only traverse matching categories.
- Append mode: `uv run docs/scraper-generator/{slug}/scraper.py --categories "/shop/fencing" --limit 10 --append` — append to existing products.jsonl without truncating.
- No web search or Playwright browser tools are needed.
- The knowledgebase write (Step 3) uses file write/edit tools to create or append to the platform knowledgebase file.
- Data persistence: the coder sub-agent writes scraper.py with persist hooks (`setup`/`persist`/`teardown`). The scraper code is final once the tester returns `pass`. After config metadata is prepared (Step 4), persist it as JSON to the config metadata path.
- Diagnostic persistence: the tester writes `test_report.json` after each dispatch. After successful validation, the orchestrator derives `validation.json` from `test_report.json` for eval-generator compatibility.
- The canonical product record format definition lives in `references/coder.md`.

## Fix Mode

When invoked by `/scraper-remediation` with a fix request (`mode: "fix"`), the scraper-generator operates differently:

- **Skip the archive step** — do not archive or regenerate from scratch. Patch the existing scraper in place.
- The remediation skill creates `scraper.py.pre-remediation` backup before invoking fix mode — rollback is the remediation skill's responsibility.
- Read the fix request JSON to understand which eval checks failed and what needs fixing.
- Read and follow the "## Fix Mode" section in `references/orchestrator.md` for the step flow. The orchestrator maps eval check names to internal rule IDs and dispatches the coder sub-agent in fix mode.
- Validation (tester dispatch with retest + final modes) runs the same as normal mode.
- Write a `fix_summary` field to `validation.json` describing what was changed and the `fix_outcome` (`"fixed"`, `"partial"`, or `"unfixable"`).

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
