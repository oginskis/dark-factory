---
name: scraper-generator
description: >
  Generate a production-ready Python scraper for a company's product catalog.
  Produces a standalone scraper.py, config.json, and test output.
  Scrapers output the three-bucket product record format (_format: 2) with core_attributes, extended_attributes, and extra_attributes.
  Use this skill when the user wants to create a scraper for a company that already has a catalog assessment —
  "generate scraper for X", "create scraper for X", "build a scraper for X products", "scrape X's catalog".
  Requires both a company report from /product-classifier and a catalog assessment from /catalog-detector to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Scraper Generator

Read and follow the agent instructions in `agents/scraper-generator.md`.

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

### Slug derivation

- **`{slug}`** — the company slug from `$ARGUMENTS` (e.g., `topwoodtimber`).
- **`{category-slug}`** — derived from the **subcategory** in the company report's Primary classification. Take the part after ` > `, lowercase it, replace spaces with hyphens, drop special characters. Example: `Wood Products & Lumber > Softwood & Hardwood Lumber` → `softwood-hardwood-lumber`.
- **`{platform-slug}`** — the platform name from the catalog assessment, lowercased. Example: WooCommerce → `woocommerce`, Shopify → `shopify`. If platform is `unknown` or `custom`, there is no knowledgebase file — skip it.

## Claude Code wiring

- Provide the file paths from the table above when the agent references logical resources (e.g., "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the platform knowledgebase").
- When the agent reaches an escalation point, present it using the standard escalation format (see orchestrator) and **wait for the user's response** before continuing. User options per escalation:
  - `missing_catalog_assessment` — 1) Run `/catalog-detector {slug}` first, then retry, 2) Stop
  - `no_sku_schema` (taxonomy issue, only escalates when subcategory is missing from taxonomy) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
  - `probe_extraction_failed` — 1) Provide guidance on how to extract from this site, 2) Stop
  - `scraper_test_failed` — 1) Provide debugging guidance or site-specific hints, 2) Stop
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema file hasn't been created yet, automatically invoke `/product-taxonomy` for that subcategory to generate the schema, then continue without user interaction. Only escalate if the subcategory itself is missing from the taxonomy entirely.
- Run the scraper using `uv run` (not `uv run python`) for the full verification test as directed by the agent in Step 5. The PEP 723 inline metadata in the script declares its own dependencies, so `uv` resolves them automatically.
- **Test timeout enforcement:** Run the `--limit 20` test with a **2-minute timeout** (use `timeout 120` or the Bash tool's timeout parameter set to 120000ms). Redirect stderr to a debug log for post-mortem analysis: `uv run docs/scraper-generator/{slug}/scraper.py --limit 20 2>docs/scraper-generator/{slug}/output/debug.log`. If the process exceeds 2 minutes, kill it immediately, then read `docs/scraper-generator/{slug}/output/debug.log` to diagnose the failure, fix the scraper, and retry. A `--limit 20` test that exceeds 2 minutes is always broken — do not wait for it to finish naturally.
- **Probe execution:** Run probes using `uv run docs/scraper-generator/{slug}/scraper.py --probe <URL>`. The scraper fetches the page internally, runs the real extraction code, and prints the result as formatted JSON to stdout. Examine the output to verify extraction quality — no web fetch tools are needed for probing.
- No web search or Playwright browser tools are needed.
- The knowledgebase write (Step 6) uses file write/edit tools to create or append to the platform knowledgebase file.
- **Data persistence:** Current backend is NDJSON files on disk. Read the persist hook implementations file (see File locations table) for the `setup`/`persist`/`teardown` functions to include in the generated scraper. The agent defines the data contract and hook call pattern; the reference file defines what the hooks do. After the agent completes the full test (Step 5 succeeds), persist the scraper code to the scraper script path. After the agent prepares config metadata (Step 7), persist it as JSON to the config metadata path. Run the dry-run test with `uv run docs/scraper-generator/{slug}/scraper.py --limit 20` as directed by the agent in Step 5.

## Product record format

Scrapers output the **three-bucket format** (`_format: 2`):
- **Top-level fields:** `_format`, `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path`
- `brand` is a top-level field (not inside any attribute bucket)
- `product_category` is the taxonomy ID (e.g., `machinery.power_tools`)
- **`core_attributes`** — attributes matching core names in the SKU schema
- **`extended_attributes`** — attributes matching extended names in the SKU schema
- **`extra_attributes`** — everything else (snake_case keys, primitive values only)

The `config.json` includes:
- `category_mapping` (dict) — maps site category paths to taxonomy IDs; must include at least a `"default"` key
- `default_category` (string) — the company's primary taxonomy ID, used as fallback `product_category`

## Notes

File-driven skill — no database or external services required.
