# Pipeline Quality Improvements — Design Spec

**Date:** 2026-03-18
**Goal:** Fix eval scoring to be per-subcategory, add semantic validation, make eval output human-readable, define sample size rules.

## Problem

After running the full pipeline on 7 companies, 4 of 6 scored "degraded." Root cause analysis against actual data:

1. **Eval scores against wrong schema** — eval checks each product against the UNION of all subcategory schemas. A harlowbros lumber product is penalized for missing `joint_type` (a millwork field) and `fastener_type` (a fasteners field). Harlowbros actually has ~80% core fill when scored against its own subcategory — eval reports 0%. This is the #1 problem.
2. **No semantic validation** — eval checks structure but not whether values make sense. HTML in SKU fields, "ternal Cladding - 150mm" in dimension fields, navigation pages scraped as products — all pass silently.
3. **Eval output is raw JSON** — numeric scores need manual interpretation. No guidance on what's broken.
4. **Undefined sample sizes** — evaluating 20 products from 1 category of a 7-subcategory company is meaningless.

---

## A: Per-Subcategory Eval Scoring

The single highest-impact fix. Each product is scored against its OWN subcategory's schema, not the union.

### Current behavior (broken)

```python
# eval.py builds union of all core keys across all subcategories
all_core_keys = set()
for sub in config["subcategories"]:
    all_core_keys.update(sub["core_attributes"])
# Then scores every product against this union
```

A lumber product missing `joint_type` (millwork), `fastener_type` (fasteners), `panel_type` (plywood) scores 1/31 = 3% core coverage even though it has 1/1 lumber-relevant core fields filled.

### New behavior

```python
# Score each product against its own subcategory's schema
product_category = product.get("product_category")
sub_config = subcategory_configs.get(product_category)
if sub_config:
    core_keys = sub_config["core_attributes"]
    extended_keys = sub_config["extended_attributes"]
else:
    core_keys = all_core_keys  # fallback for unclassified products
```

### eval_config.json change

Currently `core_attributes` and `extended_attributes` are flat lists (union). Change to per-subcategory:

```json
{
  "subcategories": {
    "wood.softwood_hardwood_lumber": {
      "core_attributes": ["wood_type", "structural_grade", "treatment_type"],
      "extended_attributes": ["species", "nominal_thickness", "nominal_width"]
    },
    "wood.millwork": {
      "core_attributes": ["material", "joint_type"],
      "extended_attributes": ["species", "profile_pattern", "finish"]
    }
  }
}
```

The flat `core_attributes`/`extended_attributes` keys are removed. All attribute scoring is per-subcategory.

### Impact on current companies

| Company | Current core | Per-subcategory core (estimated) |
|---|---|---|
| harlowbros | 0% (union of 7 schemas) | ~80% (lumber products scored against lumber schema) |
| PATA | 0% (union of 5 schemas) | ~5% (millwork products — `grade` fills 1 core field) |
| uk-timber | 30% | ~50% (scored against correct schemas) |
| uksleepers | 12.5% | ~40% (scored against lumber schema) |
| iwood | 36.7% | ~60% (scored against correct schemas) |
| thetimbermerchants | 77.8% | ~80% (already mostly single-subcategory) |

---

## B: Semantic Validation Checks

3 sub-checks added to eval.py as a `semantic_validation` composite check. Composite score = minimum of sub-check scores. Threshold: 0.95. Weight: 5 (take 5 from `duplicate_detection`, reducing it from 10 to 5).

### Sub-check 1: Value cleanliness
- HTML tags (`<[a-z]`) in any attribute value
- Values longer than 200 characters
- Control characters or null bytes

Score: clean products / total.

### Sub-check 2: Non-product detection
- Product name matches: `Delivery|Contact|FAQ|Branch Locator|Information|Privacy|Terms`
- No price AND no attributes (completely empty record)
- URL contains `/contact/|/about/|/faq/|/terms/|/privacy/|/delivery`

Score: real products / total.

### Sub-check 3: Numeric field format
- Fields listed in `numeric_fields` config must be a number or `{number}{unit}` (e.g., "150mm")
- Must NOT contain prose ("ternal Cladding - 150mm" → fail)
- Dual-format values like "47mm 2\"" are valid (metric + imperial is common in UK timber)

Regex: `^\d+(\.\d+)?\s*[a-zA-Z/"]*(\s+\d+(\.\d+)?\s*[a-zA-Z/"]*)?$`

Score: products with valid numeric fields / products that have those fields.

### eval_config.json addition

```json
{
  "semantic_validation": {
    "numeric_fields": ["nominal_width", "nominal_thickness", "width", "thickness", "length"]
  }
}
```

---

## C: Human-Readable Eval Output

### Stdout summary

eval.py prints a text summary to stdout. ASCII-only for terminal compatibility:

```
=== EVAL: {slug} -- {STATUS} (score: {score}) ===

FAILING ({n}):
  [FAIL] core_attribute_coverage: 30% (need 90%)
         wood.softwood_hardwood_lumber: 80% (12 products)
         wood.millwork: 5% (8 products) -- missing: material, joint_type
  [FAIL] semantic_validation: 88% (need 95%)
         3 bad numeric values, 2 non-products, 1 HTML in SKU

PASSING ({n}):
  [PASS] schema_conformance: 100%
  [PASS] data_freshness: 100%

SKIPPED ({n}):
  [SKIP] pagination_completeness -- limited run

SAMPLE: {products_scored} products from {subcategories_covered} subcategories
```

Note: the per-subcategory breakdown in the core_attribute_coverage line is new — enabled by Section A.

### Markdown report

Written to `{output-dir}/eval_report.md`. Same content as stdout plus:
- Per-subcategory attribute coverage breakdown table
- Top 5 worst products with specific issues and URLs
- Actionable fix suggestions per failing check

### JSON output

`eval_result.json` gains per-subcategory breakdowns in the check details. Top-level schema unchanged.

---

## D: Sample Size Rules

### Scraper validation (inside scraper-generator)

| Phase | Size | Floor | Ceiling | Purpose |
|-------|------|-------|---------|---------|
| Smoke test | fixed | 20 | 20 | Does it crash? |
| Final verification | 10% of expected | 20 | 100 | Structural check |

### Eval validation

| Metric | Value |
|--------|-------|
| Total sample | 30% of expected catalog |
| Floor | 50 products |
| Ceiling | 300 (soft — lifted when per-subcategory minimums exceed it) |
| Per subcategory | 10% of subcategory's expected count, min 10 (hard) |

Per-subcategory minimums are hard requirements. If 7 subcategories each need 10 products (= 70) but 30% formula says 50, eval needs 70.

### Formula

```python
def eval_sample_size(expected_total, subcategories):
    total_target = min(max(ceil(expected_total * 0.3), 50), 300)
    per_sub = {}
    for sub in subcategories:
        per_sub[sub["id"]] = max(ceil(sub["expected_count"] * 0.1), 10)
    # Per-sub minimums take precedence over the soft ceiling
    return {"total": max(total_target, sum(per_sub.values())), "per_subcategory": per_sub}
```

### Eval collects its own data

eval.py gains a `--collect` flag. When set, eval runs the scraper to collect a sufficient sample before scoring. Scraper location: `docs/scraper-generator/{slug}/scraper.py` (convention-based, slug from eval_config).

Without `--collect`, eval scores whatever JSONL exists.

### Minimum scoreable checks

At least 3 checks must produce meaningful scores. If fewer than 3 are scoreable, result is `"status": "insufficient_data"` — prevents misleading pass/fail from tiny samples.

---

## Files changed

| File | Change |
|------|--------|
| `eval/eval.py` | Per-subcategory scoring, semantic_validation check (3 sub-checks), text summary to stdout, markdown report, `--collect` flag, minimum scoreable checks |
| `.claude/skills/eval-generator/SKILL.md` | eval_config schema: per-subcategory core/extended attrs, semantic_validation config |
| `.claude/skills/eval-generator/references/workflow.md` | Generate per-subcategory config, semantic_validation settings |
| `.claude/skills/scraper-generator/references/validator.md` | Update sample size rules (final verification: 10%/20/100) |
