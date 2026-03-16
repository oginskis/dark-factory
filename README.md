# Dark Factory

Product discovery pipeline: give it a company name or URL, get back a production-ready scraper that produces structured product data daily.

## How It Works

```
Expensive tier (LLM, runs once per company):

  Company URL  -->  [Classify]  -->  [Detect Catalog]  -->  [Generate Scraper]  -->  [Generate Eval]
                     Stage 1           Stage 2                Stage 3                 Stage 4

Cheap tier (no LLM, runs daily):

  scraper.py  -->  products.jsonl  -->  eval  -->  eval_result.json
                                                    |
                                                    +--> quality degrades? --> re-run expensive tier
```

The expensive tier generates two artifacts per company: a **scraper** (standalone Python script) and an **eval config** (JSON file consumed by a shared eval script). Both run on any scheduler (cron, Airflow, K8s CronJobs) with zero LLM involvement. The expensive tier only re-runs when the eval detects quality degradation.

## Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Python](https://www.python.org/) | 3.10+ | Runtime for scrapers and eval |
| [uv](https://docs.astral.sh/uv/) | Latest | Runs scripts with inline dependency resolution |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Latest | CLI that powers the LLM pipeline stages |
| Claude subscription | Max plan | Required for classification, catalog detection, scraper/eval generation |

Required Claude Code plugins (Playwright, Context7) are auto-installed when you open the project.

## Quick Start

### 1. Run the full pipeline

Inside Claude Code:

```
/product-discovery https://www.evergy.co.uk/
```

This runs all four stages:
1. **Classify** — researches the company, classifies it into the product taxonomy
2. **Detect catalog** — finds the product catalog, analyzes structure, picks a scraping strategy
3. **Generate scraper** — writes a standalone Python scraper, probes live pages, runs a smoke test
4. **Generate eval** — creates an eval config with twelve weighted quality checks

Each stage can stop the pipeline if it hits a blocker (no physical products, no public catalog, anti-bot protection, etc.).

### 2. Run the generated scraper

No Claude Code needed:

```bash
# Full catalog scrape
uv run docs/scraper-generator/{slug}/scraper.py

# Smoke test (20 products)
uv run docs/scraper-generator/{slug}/scraper.py --limit 20
```

Replace `{slug}` with the company slug from the pipeline summary (e.g., `festool`, `britishhardwoods`). `uv run` handles dependencies automatically via PEP 723 inline metadata.

### 3. Validate scraper output

```bash
uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json
```

### 4. Interpret the results

**Scraper output** (`docs/scraper-generator/{slug}/output/`):

| File | Contents |
|------|----------|
| `products.jsonl` | One product per line — universal fields plus category-specific attributes (see [Product record format](#product-record-format) below) |
| `summary.json` | Run metadata: total products, duration, error count |

**Eval output** (`docs/eval-generator/{slug}/output/`):

| File | Contents |
|------|----------|
| `eval_result.json` | Twelve weighted checks, degradation score (0-100), pass/degraded/fail status |
| `eval_history.json` | Append-only log of all eval runs for trend detection |
| `baseline.json` | First-run attribute fill rates for regression detection |

| Status | Score | Action |
|--------|-------|--------|
| `pass` | 0-30 | No action needed |
| `degraded` | 31-60 | Review scraper output for issues |
| `fail` | 61-100 | Re-run the pipeline to regenerate the scraper |

When `"recommend_rediscovery": true`, the site has changed enough that a fresh pipeline run is needed.

## Product Taxonomy

The pipeline classifies every company into a canonical taxonomy of physical product subcategories. This classification drives everything downstream — which attributes to extract, how to validate quality, and how to compare products across companies.

### Taxonomy IDs

Every subcategory has a unique ID (e.g., `machinery.power_tools`, `wood.flooring_decking`) defined in `docs/product-taxonomy/categories.md`. A company gets one primary ID and may have additional subcategories:

```
Subcategories: wood.flooring_decking, wood.softwood_hardwood_lumber, wood.millwork
Primary:       wood.flooring_decking
```

The primary ID becomes the `product_category` field on every scraped product record.

### SKU Schemas

Each subcategory has a schema that defines which attributes to extract. Schemas are created by researching 3-5 real companies in the subcategory, then synthesizing the attributes that consistently appear on pricelists and product catalogs.

Attributes are split into two tiers:

| Tier | What goes here | Count | Fill rate target |
|------|----------------|-------|------------------|
| **Core** | Identity, material, primary dimension — what you'd compare across companies | 5-10 | >80% of products |
| **Extended** | Product-specific or rarely published — useful but not universal | 10-15 | >50% of products |

Each attribute row has a **Key** column (`snake_case` identifier) that scrapers use as the exact field name. This is the contract between schemas and scrapers — no renaming, no inference.

To create or enrich a schema manually:

```
/product-taxonomy "Power Tools (Drills, Saws, Sanders)"
```

If the pipeline encounters a subcategory without a schema, it generates one automatically.

### Product record format

Every scraped product has four attribute levels. The generated Python scraper handles all routing automatically.

| Level | What it contains | Extraction effort | Fill rate target |
|-------|-----------------|-------------------|------------------|
| **Universal top-level** | `sku`, `name`, `url`, `price`, `currency`, `brand`, `product_category`, `scraped_at`, `category_path` | Always extracted — mandatory for every product regardless of category | — |
| **`core_attributes`** | Attributes matching the SKU schema's Core table | **High** — scraper actively works to extract these (navigating tabs, parsing spec tables) | >80% of products |
| **`extended_attributes`** | Attributes matching the SKU schema's Extended table | **Moderate** — extracted when available, no complex parsing for marginal gains | >50% of products |
| **`extra_attributes`** | Everything else discovered on the page | **Low / opportunistic** — captured naturally, serves as feedback for schema evolution | — |

```json
{
  "sku": "CLASSIC",
  "name": "Classic Grade Solid European Oak Flooring",
  "url": "https://example.com/classic-oak",
  "price": 75.0,
  "currency": "GBP",
  "brand": "British Hardwoods",
  "product_category": "wood.flooring_decking",
  "scraped_at": "2026-03-16T12:00:00Z",
  "category_path": "Solid Wood Flooring > Oak",
  "core_attributes": {
    "finish_type": "Oiled",
    "grade": "Classic"
  },
  "extended_attributes": {
    "species": "European Oak",
    "thickness": "20mm"
  },
  "extra_attributes": {
    "edge_detail": "Micro Bevel",
    "moisture_content": "9-11%"
  }
}
```

**`core_attributes`** and **`extended_attributes`** use keys from the SKU schema exactly. **`extra_attributes`** catches everything else — when an extra attribute appears across multiple companies, the `/product-taxonomy` skill can promote it into the schema for future scrapers.

**Non-English sites:** All attribute keys are English (matching schema Key values or `snake_case`). For universal, core, and extended values, the scraper includes static translation dicts for known value sets (species names, material types, grade labels). Extra attribute values may remain in the original language.

### Schema lifecycle

1. **Auto-generated** when the pipeline hits a subcategory without one
2. **Evolved** via the scraper-generator's feedback loop (proposes extras for promotion)
3. **Manually enriched** via `/product-taxonomy`
4. **Append-only** — attributes are never deleted, only deprecated

## Running Individual Stages

Each stage can run independently. Upstream stages must have completed first.

| Command | What it does | Requires |
|---------|-------------|----------|
| `/product-classifier <url-or-name>` | Classify a company's products | Nothing |
| `/catalog-detector <slug>` | Assess catalog scrapability | Stage 1 |
| `/scraper-generator <slug>` | Generate a scraper | Stages 1-2 |
| `/eval-generator <slug>` | Generate quality validation | Stages 1-3 |

The slug comes from the company's domain (e.g., `festool` from festool.com, `britishhardwoods` from britishhardwoods.co.uk).

## Project Structure

```
dark-factory/
  agents/                                   # Harness-agnostic agent reasoning (tracked)
  .claude/skills/                           # Claude Code skill wrappers (tracked)
  eval/                                     # Shared eval script
  scripts/                                  # Utility scripts (schema verification, migrations)
  docs/
    product-taxonomy/                       # Canonical taxonomy + SKU schemas (tracked)
      categories.md                         #   Category list with taxonomy IDs
      sku-schemas/                          #   Per-subcategory attribute schemas
    platform-knowledgebase/                 # Shared platform patterns (tracked)
    product-classifier/{slug}.md            # Company reports (gitignored)
    catalog-detector/{slug}.md              # Catalog assessments (gitignored)
    scraper-generator/{slug}/               # Scraper artifacts (gitignored)
      scraper.py                            #   Standalone scraper
      config.json                           #   Category mapping + metadata
      output/                               #   products.jsonl + summary.json
    eval-generator/{slug}/                  # Eval artifacts (gitignored)
      eval_config.json                      #   12 weighted checks
      output/                               #   eval_result.json + history + baseline
```

Per-company output is gitignored — regenerate by re-running the pipeline.
