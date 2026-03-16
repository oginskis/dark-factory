# Dark Factory

Product discovery pipeline that takes a company name or URL and produces continuously updated product/price data. The system separates expensive LLM reasoning (runs once per company + on degradation) from cheap daily scraping (standalone Python scripts).

## Architecture

Two-tier cost model:
- **Expensive tier** — LLM skills classify companies, detect catalogs, generate scrapers and evals. Runs once per company and on degradation.
- **Cheap tier** — Generated Python scripts (scraper.py) + eval configs (eval_config.json) run as daily K8s CronJobs via the shared eval script. No LLM involved.

Pipeline stages: product-classifier → catalog-detector → scraper-generator → eval-generator.

## Key Directories

- `.claude/skills/` — Pipeline skills (SKILL.md + references/ for each stage)
- `docs/product-taxonomy/` — Canonical taxonomy (`categories.md`) and SKU schemas (`sku-schemas/`)
- `docs/product-classifier/` — Company reports (output of product-classifier)
- `docs/catalog-detector/` — Catalog assessments (output of catalog-detector)
- `docs/scraper-generator/` — Scraper artifacts (scraper.py, config.json, output/)
- `eval/` — Shared eval script (quality validation for scrapers)
- `docs/eval-generator/` — Eval artifacts (eval_config.json, output/)
- `scripts/` — Utility scripts (schema verification, migrations)

## Skills-First Approach

**When a skill matches the task, use it.** This project relies heavily on skills to encode domain knowledge, enforce conventions, and maintain consistency across the pipeline. Do not improvise workflows that a skill already covers — invoke the skill and follow its instructions.

Key skills:
- `/product-discovery` — Full end-to-end pipeline for a company
- `/product-classifier` — Classify a company into the taxonomy
- `/catalog-detector` — Assess catalog scrapability
- `/scraper-generator` — Generate a scraper from catalog assessment + SKU schema
- `/eval-generator` — Generate quality validation for a scraper
- `/product-taxonomy` — Research SKU attributes for a product subcategory
- `/skill-creator-local` — Create or review pipeline skills following repo conventions

## Python

Always use `uv` to run Python in this project — never bare `python` or `python3`.

```bash
uv run python script.py          # run a script
uv run python -m module           # run a module
uv pip install package            # install a package
```

## Git

Per-company pipeline output under `docs/` is gitignored — only shared knowledge is tracked:

| Tracked | Gitignored |
|---------|------------|
| `docs/product-taxonomy/` | `docs/product-classifier/` |
| `docs/platform-knowledgebase/` | `docs/catalog-detector/` |
| | `docs/scraper-generator/` |
| | `docs/eval-generator/` |

`.claude/` (skills, settings) is always tracked — never gitignore it.

## Conventions

- **After every change to any skill file**, run `/skill-creator-local deep review` to verify convention compliance. This is not optional.
- Each pipeline skill is self-contained under `.claude/skills/{name}/` with SKILL.md + references/. See `/skill-creator-local` for conventions.
- Run `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all` to check convention compliance.
- Taxonomy IDs (e.g., `machinery.power_tools`) are the canonical identifiers — always from `docs/product-taxonomy/categories.md`.
- The product taxonomy categories file is read-only for all skills except product-taxonomy.
