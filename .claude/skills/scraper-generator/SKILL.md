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
- **`{category-slug}`** — derived from the subcategory display name corresponding to the company's Primary taxonomy ID. Look up the taxonomy ID in `categories.md` to find the display name, then slugify: lowercase, replace spaces with hyphens, drop special characters (`&`, `/`, `(`, `)`, `,`). Example: taxonomy ID `wood.softwood_hardwood_lumber` → display name "Softwood & Hardwood Lumber" → slug `softwood-hardwood-lumber`.
- **`{platform-slug}`** — the platform name from the catalog assessment, lowercased. Example: WooCommerce → `woocommerce`, Shopify → `shopify`. If platform is `unknown` or `custom`, there is no knowledgebase file — skip it.

## Claude Code wiring

- Provide the file paths from the table above when the agent references logical resources (e.g., "the company report", "the catalog assessment", "the SKU schema", "the product taxonomy categories file", "the platform knowledgebase").
- When the agent reaches an escalation point, present it using the standard escalation format (see orchestrator) and **wait for the user's response** before continuing. User options per escalation:
  - `missing_catalog_assessment` — 1) Run `/catalog-detector {slug}` first, then retry, 2) Stop
  - `no_sku_schema` (taxonomy issue, only escalates when subcategory is missing from taxonomy) — 1) Add the missing subcategory to `docs/product-taxonomy/categories.md` and retry, 2) Stop
  - `probe_extraction_failed` — 1) Provide guidance on how to extract from this site, 2) Stop
  - `scraper_test_failed` — 1) Provide debugging guidance or site-specific hints, 2) Stop
  - `unmapped_url_prefix` — 1) Provide the correct taxonomy ID for the URL prefix, 2) Stop
- The `no_sku_schema` decision has an autonomous resolution path: when the subcategory exists in the taxonomy but the SKU schema file hasn't been created yet, automatically invoke `/product-taxonomy` for that subcategory to generate the schema, then continue without user interaction. Only escalate if the subcategory itself is missing from the taxonomy entirely.
- **SKU schema lookup — CRITICAL:** Never guess the schema filename from a partial slug. The `{category-slug}` is derived from the FULL subcategory display name (e.g., "Wood Flooring & Decking" → `wood-flooring-decking`, NOT `flooring-decking`). Before concluding a schema is missing, **list the `docs/product-taxonomy/sku-schemas/` directory** and search for the subcategory name. Invoking `/product-taxonomy` for a schema that already exists wastes significant resources.
- Run the scraper using `uv run` (not `uv run python`) for the full verification test as directed by the agent in Step 5. The PEP 723 inline metadata in the script declares its own dependencies, so `uv` resolves them automatically.
- **Smoke test timeout enforcement (Step 5):** Run the `--limit 20` smoke test with a **2-minute timeout** (use `timeout 120` or the Bash tool's timeout parameter set to 120000ms). Redirect stderr to a debug log for post-mortem analysis: `uv run docs/scraper-generator/{slug}/scraper.py --limit 20 2>docs/scraper-generator/{slug}/output/debug.log`. If the process exceeds 2 minutes, kill it immediately, then read `docs/scraper-generator/{slug}/output/debug.log` to diagnose the failure, fix the scraper, and retry. A `--limit 20` test that exceeds 2 minutes is always broken — do not wait for it to finish naturally.
- **Final verification run (Step 5b):** After the smoke test passes, compute `sample_size = min(ceil(expected_product_count * 0.2), 100)` from the catalog assessment's estimated product count. If `sample_size <= 20`, skip this run — the smoke test output is sufficient. Otherwise, run `uv run docs/scraper-generator/{slug}/scraper.py --limit {sample_size} 2>docs/scraper-generator/{slug}/output/debug.log` with a timeout of `max(120, sample_size * 6)` seconds (i.e., Bash tool timeout = `max(120000, sample_size * 6000)` ms). This output is what the eval-generator validates against.
- **Probe execution:** Run probes using `uv run docs/scraper-generator/{slug}/scraper.py --probe <URL>`. The scraper fetches the page internally, runs the real extraction code, and prints the result as formatted JSON to stdout. Examine the output to verify extraction quality — no web fetch tools are needed for probing.
- No web search or Playwright browser tools are needed.
- The knowledgebase write (Step 6) uses file write/edit tools to create or append to the platform knowledgebase file.
- **Data persistence:** Current backend is NDJSON files on disk. Read the persist hook implementations file (see File locations table) for the `setup`/`persist`/`teardown` functions to include in the generated scraper. The agent defines the data contract and hook call pattern; the reference file defines what the hooks do. After the agent completes the smoke test (Step 5 succeeds), persist the scraper code to the scraper script path. After the agent prepares config metadata (Step 7), persist it as JSON to the config metadata path. Run the smoke test with `uv run docs/scraper-generator/{slug}/scraper.py --limit 20` as directed by the agent in Step 5. After Step 5b completes (or is skipped), the final output in `docs/scraper-generator/{slug}/output/` is the eval input.

### Product record format

Every product record has four attribute levels. This is the canonical definition — all other skills reference it.

| Level | What it contains | Extraction effort | Source |
|-------|-----------------|-------------------|--------|
| **Universal top-level fields** | `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path` | Always extract — these are mandatory for every product regardless of category. Never change across taxonomy updates. | Hardcoded in scraper and eval script |
| **`core_attributes`** | Attributes matching the **Key** column in the SKU schema's Core Attributes table | **High effort** — the agent must actively work to extract these. They define what makes a product identifiable and comparable within its subcategory. Target: >80% fill rate. | SKU schema (`docs/product-taxonomy/sku-schemas/`) |
| **`extended_attributes`** | Attributes matching the **Key** column in the SKU schema's Extended Attributes table | **Moderate effort** — extract when available on the page, but do not invent complex parsing for marginal gains. Target: >50% fill rate. | SKU schema (`docs/product-taxonomy/sku-schemas/`) |
| **`extra_attributes`** | Everything else discovered on the product page that doesn't match any Key in core or extended | **Low effort / opportunistic** — capture what is naturally available during extraction, but do not put significant effort into finding these. They serve as a feedback signal for future schema evolution. Keys must be `snake_case`, values must be primitives. | Discovered at runtime |

Additional rules:
- `brand` is a universal top-level field (not inside any attribute bucket)
- `product_category` is the taxonomy ID (e.g., `machinery.power_tools`)

### Language rules for non-English sites

| Level | Keys | Values |
|-------|------|--------|
| **Universal top-level** | English (fixed) | `name` may remain in the original language. Other values in English where a static mapping is feasible. |
| **`core_attributes`** | English only — must match SKU schema Key column exactly | Map to English via static translation dicts for known value sets (species, materials, grades). Values without a mapping pass through in original language. |
| **`extended_attributes`** | English only — must match SKU schema Key column exactly | Same as core — static mapping where feasible, pass-through otherwise. |
| **`extra_attributes`** | English `snake_case` — derived from non-English labels at code-generation time | Values may remain in the original language. No translation required. |

The generated Python scraper handles this via static `LABEL_MAP` and value translation dicts — not runtime AI translation. The scraper-generator agent builds these mappings into the code when generating a scraper for a non-English site.

The `config.json` includes:
- `category_mapping` (dict) — maps URL path prefixes to taxonomy IDs (e.g., `"/Head-Protection/": "safety.head_protection"`)
- `default_category` (string) — the company's primary taxonomy ID, used as fallback `product_category`

## Notes

File-driven skill — no database or external services required.
