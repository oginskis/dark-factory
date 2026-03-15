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
    "brand", "manufacturer", "panel_type", "wood_species", "surface_treatment"
  ],
  "type_map": {
    "brand": "str",
    "manufacturer": "str",
    "panel_type": "str",
    "wood_species": "str",
    "surface_treatment": "str",
    "applications": "list",
    "grades": "list",
    "standard_thicknesses": "str",
    "overlay_colors": "list",
    "certifications": "list",
    "country_of_origin": "str"
  },
  "enum_attributes": {
    "surface_treatment": ["Uncoated", "Film-faced", "HPL", "Lacquered", "Melamine", "Primed", "Decorative", "Textured overlay", "Composite"]
  },
  "has_prices": false
}
```

**Fields:**

| Field | Type | Description |
|-------|------|-------------|
| `company_slug` | string | Company identifier, used to derive scraper output path |
| `expected_product_count` | number | From catalog assessment, used for pagination completeness |
| `expected_top_level_categories` | string[] | Expected top-level category names from catalog assessment. Category diversity uses set intersection: `len(expected & actual) / len(expected)`. |
| `core_attributes` | string[] | Category-specific attributes (inside the `attributes` object) that every product should have populated. Used for attribute coverage check alongside universal fields. |
| `type_map` | object | Maps attribute names (inside `attributes` object) to expected types: "str", "number", "list", "bool". Used for schema conformance. Covers all attributes the scraper extracts, both core and optional. |
| `enum_attributes` | object | Maps attribute names to arrays of allowed values. Products with values outside the set count as schema conformance failures for that attribute-value pair. Example: `{"surface_treatment": ["Uncoated", "Film-faced", "HPL"]}`. |
| `has_prices` | boolean | Whether the catalog has prices. When false, price_sanity check is skipped. |

**Universal fields are hardcoded in the shared script, not in the config.** The 6 universal product fields (`sku`, `name`, `url`, `price`, `currency`, `scraped_at`) live at the top level of each product record and are fixed across all companies. The shared eval script knows to check `product["sku"]` for these. The `core_attributes` in the config lists only category-specific attributes that live inside `product["attributes"]`. The eval checks `product["attributes"]["brand"]` for those. This avoids the ambiguity of mixing top-level and nested fields in one list.

### Path Resolution

The shared eval script derives all paths from the config file location and `company_slug`:

- **Config file:** provided as CLI argument
- **Scraper output:** `{project_root}/docs/scraper-generator/{slug}/output/products.jsonl`
- **Scraper summary:** `{project_root}/docs/scraper-generator/{slug}/output/summary.json`
- **Eval output dir:** sibling `output/` directory next to the config file
- **Project root:** walk up from config file until a directory containing `eval/` is found. If not found after reaching filesystem root, exit with error: "Could not find project root (no eval/ directory found)"

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

### Check Implementation Details

All 9 checks are implemented in the shared eval script. The definitions below are authoritative — the agent does not need to know these details.

**Attribute coverage (weight 20).** For each product, count how many core attributes are present and non-empty. Core = the 6 universal fields (sku, name, url, price, currency, scraped_at — with price/currency excluded when `has_prices` is false) plus the `core_attributes` from the config (checked inside `product["attributes"]`). Compute per-product coverage ratio, then measure what fraction of products exceed 80% coverage. Measured value = that fraction. Threshold: 0.90. Never skips.

**Duplicate detection (weight 15).** Count products sharing the same SKU. Measured value = number of unique SKUs / total products. Threshold: 0.99 (less than 1% duplicates). Never skips — duplicates can appear in any run.

**Price sanity (weight 10).** Check every product's price: no zeros, no negatives, no value exceeding 10x the median price in this run. Products with null price are excluded from the check (not counted as failures). Measured value = fraction of products-with-prices that have sane prices. Threshold: 1.0. Skips when `has_prices` is false in the config.

**Schema conformance (weight 10).** For each product, validate attribute values in `product["attributes"]` against `type_map` and `enum_attributes` from the config. Type checks: "str" must be a non-empty string, "number" must be int or float, "list" must be a list, "bool" must be boolean. Enum checks: value must be in the allowed set. Attributes not in `type_map` are ignored. Null values are ignored (not counted). Measured value = fraction of all checked attribute-value pairs across all products that conform. Threshold: 1.0. Never skips.

**Data freshness (weight 10).** Every product must have a `scraped_at` timestamp within the last 24 hours. Measured value = fraction of products with current timestamps. Threshold: 1.0. Never skips.

**Field-level regression (weight 10).** After the first full run creates a baseline, compare each core attribute's fill rate (fraction of products where it is non-null and non-empty) against the baseline fill rate for that attribute. An attribute "regresses" if its current fill rate is less than 50% of its baseline fill rate. Measured value = fraction of core attributes whose fill rate has not regressed. Threshold: 0.50. Skips when no baseline exists.

**Pagination completeness (weight 10).** Compare `products_found` from the scraper summary against `expected_product_count` from the config. Measured value = `actual / expected`. Threshold: 0.70. Skips on limited runs (`limited: true` in summary).

**Category diversity (weight 5).** Extract the top-level category from each product's `category_path` (first segment before ` > `). Compare against `expected_top_level_categories` from the config using set intersection: `len(expected_set & actual_set) / len(expected_set)`. Threshold: 0.50. Skips on limited runs.

**Row count trend (weight 10).** Compare current `products_found` against the previous run's count from eval history. Measured value = `current / previous`. Threshold: 0.80. Skips on limited runs, first run, or when the previous run was limited.

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

Skipped checks have `"score": 0, "value": null, "skipped": true`.

## Baseline Mechanism

- The first full (non-limited) eval run automatically creates `baseline.json`
- Contains: product count, per-attribute fill rates, category list, timestamp
- Field-level regression compares current fill rates against baseline
- Re-establish by deleting `baseline.json` and running a full eval
- The pipeline default is a limited run (`--limit 20`). To activate field_level_regression and establish the baseline, schedule a periodic full eval run (no `--limit`). The first full run creates the baseline automatically.

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
- Behavioral change: price_sanity previously always ran (returning 1.0 when no prices existed), now explicitly skips when `has_prices: false`. This changes the `skipped` flag in output but not the effective score.
- The agent's self-verification step updates to expect 9 checks instead of 7
