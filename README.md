# Dark Factory

Product discovery pipeline: give it a company name or URL, get back a production-ready scraper that produces structured product data daily.

## How It Works

```
Expensive tier (LLM, runs once per company):

  Company URL  -->  [Classify]  -->  [Detect Catalog]  -->  [Generate Scraper]  -->  [Generate Eval]
                     Stage 1           Stage 2                Stage 3                 Stage 4

Cheap tier (no LLM, runs daily):

  scraper.py  -->  products.jsonl  -->  eval.py  -->  eval_result.json
                                                       |
                                                       +--> quality degrades? --> re-run expensive tier
```

The generated scripts are standalone Python — run them on any scheduler (cron, Airflow, K8s CronJobs, etc.) with zero LLM involvement. The expensive tier only re-runs when the eval detects quality degradation.

## Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| [Python](https://www.python.org/) | 3.10+ | Runtime for generated scrapers and evals |
| [uv](https://docs.astral.sh/uv/) | Latest | Python package manager — runs scripts with inline dependency resolution |
| [Claude Code](https://docs.anthropic.com/en/docs/claude-code) | Latest | CLI that powers the LLM pipeline stages |
| Claude subscription | Max plan | Required for the LLM-powered pipeline stages (classification, catalog detection, scraper/eval generation) |

Required Claude Code plugins (Playwright, Context7) are auto-installed when you open the project — no manual setup needed.

## Quick Start

### 1. Run the full pipeline

Inside Claude Code, type:

```
/product-discovery https://www.evergy.co.uk/
```

This runs all four stages sequentially:
1. **Classify** — researches the company and classifies it into the product taxonomy
2. **Detect catalog** — finds the product catalog, analyzes its structure, and picks a scraping strategy
3. **Generate scraper** — writes a standalone Python scraper, probes live pages, and runs a test
4. **Generate eval** — writes a quality validation script with seven weighted checks

Each stage can stop the pipeline if it hits a blocker (no physical products, no public catalog, anti-bot protection, etc.). You'll be told what happened and why.

### 2. Run the generated scraper

After the pipeline completes, run the scraper directly — no Claude Code needed:

```bash
# Full catalog scrape
uv run docs/scraper-generator/{slug}/scraper.py

# Limited test run (20 products)
uv run docs/scraper-generator/{slug}/scraper.py --limit 20
```

Replace `{slug}` with the company slug shown in the pipeline summary (e.g., `festool`, `finieris`).

`uv run` handles dependency installation automatically — the scraper declares its own dependencies via PEP 723 inline metadata.

### 3. Validate scraper output

Run the eval script to check scrape quality:

```bash
uv run docs/eval-generator/{slug}/eval.py
```

### 4. Interpret the results

**Scraper output** is written to `docs/scraper-generator/{slug}/output/`:

| File | Contents |
|------|----------|
| `products.jsonl` | One JSON object per line, each representing a product with universal fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) plus category-specific attributes |
| `summary.json` | Run metadata: total products, duration, error count, whether a limit was applied |

**Eval output** is written to `docs/eval-generator/{slug}/output/`:

| File | Contents |
|------|----------|
| `eval_result.json` | Quality report with seven weighted checks, a degradation score (0-100), and a pass/degraded/fail status |
| `eval_history.json` | Append-only log of all eval runs, used to detect trends |

**Eval status meanings:**

| Status | Score | Action |
|--------|-------|--------|
| `pass` | 0-30 | Quality acceptable, no action needed |
| `degraded` | 31-60 | Quality declining — review scraper output for issues |
| `fail` | 61-100 | Quality unacceptable — re-run the pipeline to regenerate the scraper |

When the eval recommends rediscovery (`"recommend_rediscovery": true`), the site has likely changed enough that a fresh pipeline run is needed.

## Running Individual Stages

Each stage can be run independently inside Claude Code. Upstream stages must have completed first.

| Command | What it does | Requires |
|---------|-------------|----------|
| `/product-classifier <url-or-name>` | Classify a company's products | Nothing |
| `/catalog-detector <slug>` | Assess catalog scrapability | Stage 1 |
| `/scraper-generator <slug>` | Generate a scraper | Stages 1-2 |
| `/eval-generator <slug>` | Generate quality validation | Stages 1-3 |

The slug is derived from the company's domain name (e.g., `festool` from festool.com, `finieris` from finieris.com).

## SKU Schemas

The scraper generator needs a SKU schema for the company's product subcategory to know which attributes to extract. If one doesn't exist yet, the pipeline generates it automatically.

To create or update a schema manually:

```
/product-taxonomy "Power Tools (Drills, Saws, Sanders)"
```

Schemas live in `docs/product-taxonomy/sku-schemas/` and define 20-40 category-specific attributes (dimensions, materials, certifications, etc.) that scrapers extract alongside the universal fields.

## Project Structure

```
dark-factory/
  agents/                                   # Harness-agnostic agent reasoning (tracked)
  .claude/skills/                           # Claude Code skill wrappers (tracked)
  docs/
    product-taxonomy/                       # Canonical taxonomy + SKU schemas (tracked)
      categories.md                         #   Master category list
      sku-schemas/                          #   Per-subcategory attribute schemas
    platform-knowledgebase/                 # Shared platform patterns (tracked)
    product-classifier/{slug}.md            # Company reports (gitignored)
    catalog-detector/{slug}.md              # Catalog assessments (gitignored)
    scraper-generator/{slug}/               # Scraper artifacts (gitignored)
      scraper.py                            #   Standalone scraper
      config.json                           #   Scraper metadata
      output/                               #   Scraped product data
    eval-generator/{slug}/                  # Eval artifacts (gitignored)
      eval.py                               #   Quality validation script
      output/                               #   Eval results and history
```

Per-company output (`product-classifier/`, `catalog-detector/`, `scraper-generator/`, `eval-generator/`) is gitignored — it's generated on demand and can be recreated by re-running the pipeline.
