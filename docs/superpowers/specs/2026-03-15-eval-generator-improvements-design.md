# Eval Generator Improvements: Shared Script + Better Checks

**Date:** 2026-03-15
**Status:** Approved

## Problem

The eval-generator currently produces a unique standalone `eval.py` per company (188-490 lines). Every generated script implements the same 7 checks with the same scoring logic — only the hardcoded constants differ. This creates two problems:

1. **Ineffective checks.** Across 14 companies, every eval passes with score 0 or near 0. On limited runs (the pipeline default), 3-4 of 7 checks skip, leaving only attribute coverage, data freshness, and schema conformance — all of which always pass on freshly scraped data. Real issues like duplicate products go undetected.

2. **Wasteful generation.** The LLM spends significant time and tokens generating 400 lines of Python that are 90% identical across companies. Bug fixes or new checks require regenerating all evals.

## Solution

Replace per-company code generation with a **shared eval script** (`eval/eval.py`) that reads a per-company **config file** (`eval_config.json`). Add two new checks and rebalance weights so limited runs are meaningful.

## Architecture

### File Layout

```
eval/
  eval.py                                    # Shared eval script (tracked in git)

docs/eval-generator/{slug}/
  eval_config.json                           # Per-company config (gitignored, LLM-generated)
  output/
    eval_result.json                         # Current run result
    eval_history.json                        # Append-only run log
    baseline.json                            # Auto-created on first full run
```

### Run Command

```bash
uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json
```

### Config Schema

The eval-generator agent produces this JSON. It is the only LLM-generated artifact.

```json
{
  "company_slug": "finieris",
  "expected_product_count": 31,
  "expected_top_level_categories": ["Riga Wood"],
  "core_attributes": [
    "sku", "name", "url", "scraped_at",
    "brand", "manufacturer", "panel_type", "wood_species", "surface_treatment"
  ],
  "type_map": {
    "applications": "list",
    "grades": "list",
    "standard_thicknesses": "str",
    "overlay_colors": "list"
  },
  "enum_attributes": {},
  "numeric_attributes": [],
  "has_prices": false
}
```

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `company_slug` | string | Company identifier, used to derive scraper output path |
| `expected_product_count` | number | From catalog assessment, used for pagination completeness |
| `expected_top_level_categories` | string[] | From catalog assessment, used for category diversity |
| `core_attributes` | string[] | Universal + category-specific attributes that every product should have. Includes top-level fields (sku, name, url, scraped_at) and attributes object fields. Price/currency excluded when `has_prices` is false. |
| `type_map` | object | Maps attribute names to expected types: "str", "number", "list", "bool". Used for schema conformance. |
| `enum_attributes` | object | Maps attribute names to arrays of allowed values. Used for schema conformance. |
| `numeric_attributes` | string[] | Attribute names expected to be numeric. Used for schema conformance. |
| `has_prices` | boolean | Whether the catalog has prices. When false, price_sanity check is skipped. |

### Path Resolution

The shared eval script derives all paths from the config file location and `company_slug`:

- **Config file:** provided as CLI argument
- **Scraper output:** `{project_root}/docs/scraper-generator/{slug}/output/products.jsonl`
- **Scraper summary:** `{project_root}/docs/scraper-generator/{slug}/output/summary.json`
- **Eval output dir:** sibling `output/` directory next to the config file
- **Project root:** walk up from config file until a directory containing `eval/` is found

## Checks

9 checks, rebalanced weights. Total weight: 100.

| Check | Weight | Threshold | What it catches | Skip condition |
|-------|--------|-----------|-----------------|----------------|
| attribute_coverage | 20 | 0.90 | Selector changes, missing fields | Never |
| duplicate_detection | 15 | 0.99 | Pagination bugs, sitemap overlaps | Never |
| price_sanity | 10 | 1.0 | Parser errors, currency confusion | `has_prices: false` |
| schema_conformance | 10 | 1.0 | Site redesign, new data format | Never |
| data_freshness | 10 | 1.0 | Stale cache, broken upsert | Never |
| field_level_regression | 10 | 0.50 | One selector broke for one field | No baseline exists |
| pagination_completeness | 10 | 0.70 | Broken pagination, removed categories | Limited run |
| category_diversity | 5 | 0.50 | Broken traversal, sitemap gaps | Limited run |
| row_count_trend | 10 | 0.80 | Category removal, pagination break | Limited run or first run |

### New Checks

**Duplicate detection (weight 15).** Count products sharing the same SKU. Measured value = number of unique SKUs / total products. Threshold: 0.99 (less than 1% duplicates). Never skips — duplicates can appear in any run.

**Field-level regression (weight 10).** After the first full run creates a baseline, compare each attribute's fill rate (fraction of products where it is non-null and non-empty) against the baseline. If any core attribute's fill rate drops by more than 50% relative to the baseline, the check fails. Measured value = fraction of core attributes whose fill rate has not regressed. Threshold: 0.50 (at least half of core attributes must maintain fill rates). Skips when no baseline exists.

### Weight Redistribution

When checks are skipped, redistribute weight proportionally across active checks:

```
effective_weight = base_weight * (100 / sum_of_active_base_weights)
```

On a limited run with no prices and no baseline, active checks are: attribute_coverage (20), duplicate_detection (15), schema_conformance (10), data_freshness (10) = 55 base weight. Multiplier = 100/55 = 1.82. This means the 4 active checks cover the full 0-100 score range, making limited runs meaningful rather than rubber stamps.

### Scoring

Same formula as current:

```
check_score = effective_weight * (threshold - actual) / threshold    when actual < threshold
check_score = 0                                                     when actual >= threshold
```

Total degradation score = sum of all check scores (0-100).

| Score | Status | Meaning |
|-------|--------|---------|
| 0-30 | pass | Quality acceptable |
| 31-60 | degraded | Quality declining |
| 61-100 | fail | Quality unacceptable |

Rediscovery recommendation: `true` when status is `fail`, or `degraded` for 3+ consecutive runs.

### Output Format

Same as current — no breaking change:

```json
{
  "status": "pass",
  "checks": {
    "attribute_coverage": { "score": 0, "value": 0.95, "threshold": 0.90, "weight": 20 },
    "duplicate_detection": { "score": 0, "value": 1.0, "threshold": 0.99, "weight": 15 },
    ...
  },
  "degradation_score": 0,
  "products_found": 31,
  "recommend_rediscovery": false,
  "timestamp": "2026-03-15T12:00:00Z"
}
```

Skipped checks include `"skipped": true` and `"value": null`.

## Baseline Mechanism

- The first full (non-limited) eval run automatically creates `baseline.json`
- Contains: product count, per-attribute fill rates, category list, timestamp
- Field-level regression compares current fill rates against baseline
- Re-establish by deleting `baseline.json` and running a full eval

```json
{
  "products_found": 31,
  "attribute_fill_rates": {
    "sku": 1.0,
    "name": 1.0,
    "price": 0.0,
    "brand": 1.0,
    "surface_treatment": 0.97
  },
  "categories": ["Riga Wood"],
  "timestamp": "2026-03-15T12:00:00Z"
}
```

## Shared Eval Script Structure

Single file `eval/eval.py`, ~300 lines, stdlib only, PEP 723 metadata:

1. **Config loader** — reads and validates eval_config.json
2. **Data loader** — reads products.jsonl, summary.json, eval_history.json, baseline.json
3. **9 check functions** — each returns `float | None` (None = skip)
4. **Scorer** — weight redistribution, degradation formula, status thresholds
5. **Baseline manager** — creates baseline on first full run, reads for regression
6. **Output writer** — writes eval_result.json, appends to eval_history.json
7. **CLI** — main() with argparse, human-readable stderr summary

## Skill and Agent Changes

### Agent (`agents/eval-generator.md`)

Rewrite. The agent's job simplifies:
- Steps 1-3: same (read scraper, catalog assessment, SKU schema)
- Step 4: produce `eval_config.json` instead of Python code
- Step 5: validate config JSON, run the shared eval script, check output
- Decisions: same (no_sku_schema, scraper_output_format_unclear, missing_product_count_estimate)

The agent no longer needs Python code quality instructions, PEP 723 guidance, scoring formula details, or check implementation specs. It determines the correct config values and writes JSON.

The agent references "the shared eval script" as a logical resource. The skill wrapper maps this to `eval/eval.py`.

### Skill wrapper (`.claude/skills/eval-generator/SKILL.md`)

Update file locations table:

| Resource | Path |
|----------|------|
| Shared eval script | `eval/eval.py` |
| Eval config (output) | `docs/eval-generator/{slug}/eval_config.json` |
| Eval result (output) | `docs/eval-generator/{slug}/output/eval_result.json` |
| Eval history (output) | `docs/eval-generator/{slug}/output/eval_history.json` |
| Eval baseline (output) | `docs/eval-generator/{slug}/output/baseline.json` |

Update wiring: run with `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`.

### Product discovery orchestrator (`.claude/skills/product-discovery/SKILL.md`)

Update Stage 4 description, run commands in summary template, and generated files table.

### README.md and CLAUDE.md

Update run commands, project structure, and descriptions.

## Migration

- Existing `eval.py` files (gitignored) become dead code — no cleanup needed
- Existing `eval_history.json` files are compatible — same format
- Existing `eval_result.json` files are compatible — same format
- Existing companies can be re-configured by running `/eval-generator {slug}` to generate `eval_config.json`
- No backward compatibility concerns — old files were standalone and gitignored
