# Pipeline Quality Improvements — Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fix eval to score per-subcategory, add semantic validation, human-readable output, and sample size rules.

**Architecture:** All changes center on `eval/eval.py` and the eval_config schema. The eval_config changes from flat `core_attributes`/`extended_attributes` lists to per-subcategory maps. Check functions that provide per-subcategory detail return `(float, detail_dict)` tuples — float for scoring, dict for breakdowns in text/markdown/JSON output. eval-generator workflow produces the new config format.

**Parallelism note:** Tasks 1-4 modify only `eval/eval.py`. Tasks 5-6 modify only skill files. These two groups can execute in parallel.

**Tech Stack:** Python 3.10+, stdlib only (json, re, argparse, pathlib, statistics, math, subprocess)

**Spec:** `docs/superpowers/specs/2026-03-18-pipeline-quality-improvements-design.md`

---

## File Structure

| File | Action | Responsibility |
|------|--------|---------------|
| `eval/eval.py` | Rewrite | Per-subcategory scoring, semantic validation, text output, `--collect` flag |
| `eval/test_eval.py` | Create | Unit tests for semantic validation, per-subcategory scoring, regex edge cases |
| `.claude/skills/eval-generator/references/workflow.md` | Modify | Generate per-subcategory config, semantic_validation settings |
| `.claude/skills/eval-generator/SKILL.md` | Modify | Updated eval_config schema reference |
| `.claude/skills/scraper-generator/references/validator.md` | Modify | Sample size formula: 10%/20/100 |

---

## Task 0: Create test fixture (new-format eval config)

Hand-craft one new-format eval config so Tasks 1-4 can be tested against real data without waiting for Task 5 (eval-generator workflow update).

**Files:**
- Modify: `docs/eval-generator/harlowbros/eval_config.json`

- [ ] **Step 1: Read the current harlowbros eval config**

Read `docs/eval-generator/harlowbros/eval_config.json` and note the current `core_attributes` and `extended_attributes` flat lists.

- [ ] **Step 2: Read the SKU schemas for harlowbros subcategories**

Harlowbros has 7 subcategories. Read the SKU schemas for each from `docs/product-taxonomy/sku-schemas/`. For each subcategory, extract its core and extended attribute Key lists.

- [ ] **Step 3: Rewrite the config with per-subcategory format**

Replace flat `core_attributes`/`extended_attributes` with a `subcategories` dict. Each subcategory gets its own attribute lists and `expected_count`. Add `semantic_validation` config. Keep `type_map`, `enum_attributes`, `has_prices`, `expected_product_count`, `expected_top_level_categories` unchanged.

```json
{
  "company_slug": "harlowbros",
  "expected_product_count": 4000,
  "expected_top_level_categories": ["..."],
  "subcategories": {
    "wood.softwood_hardwood_lumber": {
      "core_attributes": ["wood_type", "structural_grade", "treatment_type"],
      "extended_attributes": ["species", "nominal_thickness", "nominal_width"],
      "expected_count": 2000
    },
    "wood.plywood_engineered_panels": {
      "core_attributes": ["panel_type", "surface_grade_front"],
      "extended_attributes": ["thickness", "width"],
      "expected_count": 300
    }
  },
  "type_map": {"...": "..."},
  "enum_attributes": {},
  "has_prices": true,
  "semantic_validation": {
    "numeric_fields": ["nominal_width", "nominal_thickness", "width", "thickness"]
  }
}
```

(Fill in actual values from the SKU schemas. The above is illustrative.)

- [ ] **Step 4: Verify the config is valid JSON**

```bash
python3 -c "import json; json.load(open('docs/eval-generator/harlowbros/eval_config.json'))"
```

- [ ] **Step 5: Commit**

```
git add docs/eval-generator/harlowbros/eval_config.json
```

---

## Task 1: Per-subcategory eval scoring in eval.py

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add imports**

Add at the top of the file alongside existing imports:

```python
import re
from math import ceil
```

- [ ] **Step 2: Replace load_config with dual-format support**

Delete the entire current `load_config` function (lines 45-58) and replace with:

```python
def load_config(config_path: Path) -> dict:
    """Read eval_config.json. Supports both per-subcategory and flat formats."""
    if not config_path.exists():
        print(f"Error: config not found at {config_path}", file=sys.stderr)
        sys.exit(1)
    config = json.loads(config_path.read_text())

    # Required in all formats
    for field in ["company_slug", "expected_product_count", "has_prices"]:
        if field not in config:
            print(f"Error: config missing required field: {field}", file=sys.stderr)
            sys.exit(1)

    # Build per-subcategory lookup
    if "subcategories" in config:
        config["_sub_configs"] = config["subcategories"]
        # Build union for checks that need flat lists (schema_conformance, extra_attributes_ratio)
        all_core = set()
        all_extended = set()
        for sub in config["subcategories"].values():
            all_core.update(sub.get("core_attributes", []))
            all_extended.update(sub.get("extended_attributes", []))
        config.setdefault("core_attributes", sorted(all_core))
        config.setdefault("extended_attributes", sorted(all_extended))
    else:
        # Old flat format — no per-subcategory data
        config["_sub_configs"] = {}
        for field in ["core_attributes", "extended_attributes", "type_map", "enum_attributes"]:
            if field not in config:
                print(f"Error: flat-format config missing: {field}", file=sys.stderr)
                sys.exit(1)

    config.setdefault("type_map", {})
    config.setdefault("enum_attributes", {})
    config.setdefault("expected_top_level_categories", [])
    return config
```

- [ ] **Step 3: Rewrite check_core_attribute_coverage to return (float, dict)**

```python
def check_core_attribute_coverage(products: list[dict], config: dict) -> tuple[float, dict]:
    """Per-subcategory core attribute coverage. Returns (score, detail)."""
    if not products:
        return 0.0, {}
    sub_configs = config.get("_sub_configs", {})
    universals = UNIVERSAL_FIELDS_NO_PRICE if not config["has_prices"] else UNIVERSAL_FIELDS
    default_core = config.get("core_attributes", [])

    # Per-subcategory tracking
    sub_stats: dict[str, dict] = {}  # {cat: {"passing": N, "total": N, "missing_fields": {field: count}}}
    passing = 0

    for product in products:
        cat = product.get("product_category", "_unclassified")
        sub = sub_configs.get(cat)
        core_nested = sub.get("core_attributes", default_core) if sub else default_core
        total_core = len(universals) + len(core_nested)
        if total_core == 0:
            passing += 1
            continue

        populated = 0
        missing = []
        for field in universals:
            val = product.get(field)
            if val is not None and val != "" and val != []:
                populated += 1
            else:
                missing.append(field)
        attrs = product.get("core_attributes", {})
        for field in core_nested:
            val = attrs.get(field)
            if val is not None and val != "" and val != []:
                populated += 1
            else:
                missing.append(field)

        passed = populated / total_core > 0.80
        if passed:
            passing += 1

        # Track per-subcategory
        if cat not in sub_stats:
            sub_stats[cat] = {"passing": 0, "total": 0, "missing_fields": {}}
        sub_stats[cat]["total"] += 1
        if passed:
            sub_stats[cat]["passing"] += 1
        for f in missing:
            sub_stats[cat]["missing_fields"][f] = sub_stats[cat]["missing_fields"].get(f, 0) + 1

    detail = {}
    for cat, st in sub_stats.items():
        detail[cat] = {
            "coverage": round(st["passing"] / st["total"], 4) if st["total"] else 0,
            "products": st["total"],
            "top_missing": sorted(st["missing_fields"].items(), key=lambda x: -x[1])[:5],
        }

    return passing / len(products), detail
```

- [ ] **Step 4: Rewrite check_extended_attribute_coverage the same way**

Same pattern — return `(float, dict)` with per-subcategory breakdown. Look up per-subcategory `extended_attributes` via `product_category`. Use defensive `sub.get("extended_attributes", default_extended)` (same pattern as Step 3 fix).

- [ ] **Step 5: Update compute_results to handle (float, dict) tuples**

Check functions that return tuples need unpacking. Others still return `float | None`. Update `compute_results`:

```python
def compute_results(products, config, summary, history, baseline):
    ...
    # Functions returning (value, detail)
    core_value, core_detail = check_core_attribute_coverage(products, config)
    ext_value, ext_detail = check_extended_attribute_coverage(products, config)

    raw_values = {
        "core_attribute_coverage": core_value,
        "extended_attribute_coverage": ext_value,
        "pagination_completeness": check_pagination_completeness(...),
        ...  # other checks unchanged, return float | None
    }

    # Store detail for text/markdown/JSON output
    check_details = {
        "core_attribute_coverage": core_detail,
        "extended_attribute_coverage": ext_detail,
    }
    ...
    # IMPORTANT: Add check_details to the return dict alongside existing fields
    return {
        "status": status,
        "checks": checks_output,
        "degradation_score": total_degradation,
        "products_found": products_found,
        "recommend_rediscovery": recommend_rediscovery,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "check_details": check_details,
    }
```

- [ ] **Step 6: Update check_field_level_regression and compute_fill_rates**

These reference `config["core_attributes"]` — the union is already built in `load_config`, so they work without changes. Verify by reading the code.

- [ ] **Step 7: Test against harlowbros new-format config (from Task 0)**

```bash
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json
```

Expected: `core_attribute_coverage` jumps from ~0% to ~80%.

- [ ] **Step 8: Commit**

```
git add eval/eval.py
```

---

## Task 2: Semantic validation checks

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add CHECKS entry and regex constants**

`import re` was already added in Task 1. Add semantic_validation to CHECKS dict and the regex constants:

```python
# In CHECKS dict — change duplicate_detection weight from 10 to 5, add:
"duplicate_detection":         {"weight":  5, "threshold": 0.99},
"semantic_validation":         {"weight":  5, "threshold": 0.95},

# After CHECKS dict, add:
NUMERIC_VALUE_RE = re.compile(r'^\d+(\.\d+)?\s*[a-zA-Z/"]*(\s+\d+(\.\d+)?\s*[a-zA-Z/"]*)?$')
NON_PRODUCT_NAME_RE = re.compile(
    r'Delivery|Contact Us|FAQ|Branch Locator|Information|Privacy|Terms|Cookie',
    re.IGNORECASE,
)
NON_PRODUCT_URL_RE = re.compile(
    r'/contact|/about|/faq|/terms|/privacy|/delivery|/cookie',
    re.IGNORECASE,
)
```

- [ ] **Step 2: Implement check_semantic_validation**

Returns `(float, dict)` tuple like the attribute coverage checks, so detail can appear in text/markdown output.

```python
def check_semantic_validation(products: list[dict], config: dict) -> tuple[float, dict] | None:
    """Composite semantic check. Returns (min_score, detail_dict) or None if no config."""
    sem_config = config.get("semantic_validation")
    if sem_config is None:
        return None

    scores = []
    detail: dict[str, Any] = {}
    has_prices = config.get("has_prices", True)

    # Sub-check 1: Value cleanliness
    clean = 0
    dirty_examples = []
    for p in products:
        all_vals = []
        for bucket in ("core_attributes", "extended_attributes", "extra_attributes"):
            all_vals.extend(str(v) for v in p.get(bucket, {}).values() if v is not None)
        all_vals.append(str(p.get("sku", "")))
        dirty = any(
            (re.search(r'<[a-z]', v) or len(v) > 200 or any(ord(c) < 32 and c not in '\n\r\t' for c in v))
            for v in all_vals if v
        )
        if not dirty:
            clean += 1
        elif len(dirty_examples) < 3:
            dirty_examples.append(p.get("name", "?")[:60])
    cleanliness_score = clean / len(products) if products else 1.0
    scores.append(cleanliness_score)
    detail["value_cleanliness"] = {
        "score": round(cleanliness_score, 4),
        "dirty_count": len(products) - clean,
        "examples": dirty_examples,
    }

    # Sub-check 2: Non-product detection
    # For no-price catalogs, relax the "no price" heuristic — only flag if
    # the product has NO identifying data at all (no sku, no attributes).
    real = 0
    non_product_examples = []
    for p in products:
        name = p.get("name", "")
        url = p.get("url", "")
        has_attrs = bool(p.get("core_attributes") or p.get("extended_attributes"))
        has_data = bool(p.get("price") or has_attrs)
        if has_prices:
            is_non_product = (
                (NON_PRODUCT_NAME_RE.search(name) and not has_data)
                or (NON_PRODUCT_URL_RE.search(url) and not has_data)
                or (not p.get("price") and not p.get("sku") and not has_attrs)
            )
        else:
            # No-price catalog: only flag truly empty records or nav pages
            is_non_product = (
                (NON_PRODUCT_NAME_RE.search(name) and not has_attrs)
                or (NON_PRODUCT_URL_RE.search(url) and not has_attrs)
                or (not p.get("sku") and not has_attrs)
            )
        if not is_non_product:
            real += 1
        elif len(non_product_examples) < 3:
            non_product_examples.append(p.get("name", "?")[:60])
    non_product_score = real / len(products) if products else 1.0
    scores.append(non_product_score)
    detail["non_product_detection"] = {
        "score": round(non_product_score, 4),
        "flagged_count": len(products) - real,
        "examples": non_product_examples,
    }

    # Sub-check 3: Numeric field format
    numeric_fields = sem_config.get("numeric_fields", [])
    if numeric_fields:
        valid_products = 0
        checked_products = 0
        bad_examples = []
        for p in products:
            all_attrs = {**p.get("core_attributes", {}), **p.get("extended_attributes", {}), **p.get("extra_attributes", {})}
            relevant = {k: v for k, v in all_attrs.items() if k in numeric_fields and v is not None and str(v).strip()}
            if not relevant:
                continue
            checked_products += 1
            all_valid = all(NUMERIC_VALUE_RE.match(str(v).strip()) for v in relevant.values())
            if all_valid:
                valid_products += 1
            elif len(bad_examples) < 3:
                bad_vals = {k: str(v) for k, v in relevant.items() if not NUMERIC_VALUE_RE.match(str(v).strip())}
                bad_examples.append(bad_vals)
        if checked_products > 0:
            num_score = valid_products / checked_products
            scores.append(num_score)
            detail["numeric_format"] = {
                "score": round(num_score, 4),
                "invalid_count": checked_products - valid_products,
                "checked": checked_products,
                "examples": bad_examples,
            }

    composite = min(scores) if scores else 1.0
    return composite, detail
```

- [ ] **Step 3: Wire into compute_results**

Unpack like the other tuple-returning checks:
```python
sem_result = check_semantic_validation(products, config)
if sem_result is not None:
    sem_value, sem_detail = sem_result
else:
    sem_value, sem_detail = None, {}

raw_values["semantic_validation"] = sem_value

# Add to check_details dict (alongside core/extended detail)
check_details["semantic_validation"] = sem_detail
```

- [ ] **Step 4: Test against harlowbros config (has semantic_validation key)**

```bash
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json
```

Expected: `semantic_validation` appears in output (not skipped).

- [ ] **Step 5: Commit**

```
git add eval/eval.py
```

---

## Task 3: Human-readable eval output

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add format_text_summary function**

Uses `check_details` from Task 1 for per-subcategory breakdowns and semantic validation detail.

```python
def format_text_summary(result: dict, config: dict) -> str:
    slug = config["company_slug"]
    status = result["status"].upper()
    score = result["degradation_score"]
    lines = [f"=== EVAL: {slug} -- {status} (score: {score}) ===", ""]

    failing = [(n, c) for n, c in result["checks"].items() if not c.get("skipped") and c.get("score", 0) > 0]
    passing = [(n, c) for n, c in result["checks"].items() if not c.get("skipped") and c.get("score", 0) == 0]
    skipped = [(n, c) for n, c in result["checks"].items() if c.get("skipped")]
    details = result.get("check_details", {})

    if failing:
        lines.append(f"FAILING ({len(failing)}):")
        for name, check in failing:
            val = check.get("value", 0) or 0
            pct = min(int(val * 100), 100)
            thr = int(check["threshold"] * 100)
            lines.append(f"  [FAIL] {name}: {pct}% (need {thr}%)")
            # Per-subcategory breakdown for attribute coverage checks
            if name in details and name in ("core_attribute_coverage", "extended_attribute_coverage"):
                for cat, d in details[name].items():
                    cat_pct = int(d["coverage"] * 100)
                    miss = ", ".join(f[0] for f in d.get("top_missing", [])[:3])
                    line = f"         {cat}: {cat_pct}% ({d['products']} products)"
                    if miss:
                        line += f" -- missing: {miss}"
                    lines.append(line)
            # Semantic validation detail
            elif name == "semantic_validation" and name in details:
                sem = details[name]
                parts = []
                if sem.get("value_cleanliness", {}).get("dirty_count", 0):
                    parts.append(f"{sem['value_cleanliness']['dirty_count']} dirty values")
                if sem.get("non_product_detection", {}).get("flagged_count", 0):
                    parts.append(f"{sem['non_product_detection']['flagged_count']} non-products")
                if sem.get("numeric_format", {}).get("invalid_count", 0):
                    parts.append(f"{sem['numeric_format']['invalid_count']} bad numeric values")
                if parts:
                    lines.append(f"         {', '.join(parts)}")
        lines.append("")

    if passing:
        lines.append(f"PASSING ({len(passing)}):")
        for name, check in passing:
            val = check.get("value", 0) or 0
            pct = min(int(val * 100), 100)
            lines.append(f"  [PASS] {name}: {pct}%")
        lines.append("")

    if skipped:
        lines.append(f"SKIPPED ({len(skipped)}):")
        for name, _ in skipped:
            lines.append(f"  [SKIP] {name}")
        lines.append("")

    # Sample size info
    sample = eval_sample_size(config)
    needed = sample["total"]
    found = result["products_found"]
    # Subcategory count from attribute coverage detail
    sub_cats = set()
    core_detail = details.get("core_attribute_coverage", {})
    sub_cats.update(core_detail.keys())
    sub_count = len(sub_cats) if sub_cats else "?"
    sample_line = f"SAMPLE: {found} products from {sub_count} subcategories"
    if found < needed:
        sample_line += f" (need {needed} for full eval)"
    lines.append(sample_line)
    return "\n".join(lines)
```

- [ ] **Step 2: Add format_markdown_report function**

```python
def format_markdown_report(result: dict, config: dict, products: list[dict]) -> str:
    lines = [f"# Eval Report: {config['company_slug']}", ""]
    lines.append(f"**Status:** {result['status'].upper()}")
    lines.append(f"**Degradation score:** {result['degradation_score']}")
    lines.append(f"**Products scored:** {result['products_found']}")

    # Sample size adequacy
    sample = eval_sample_size(config)
    needed = sample["total"]
    if result["products_found"] < needed:
        lines.append(f"**Sample gap:** have {result['products_found']}, need {needed} for full eval")
    lines.append("")

    # Per-subcategory coverage table
    details = result.get("check_details", {})
    core_detail = details.get("core_attribute_coverage", {})
    if core_detail:
        lines.append("## Core Attribute Coverage by Subcategory")
        lines.append("")
        lines.append("| Subcategory | Coverage | Products | Top Missing Fields |")
        lines.append("|---|---|---|---|")
        for cat, d in sorted(core_detail.items()):
            pct = int(d["coverage"] * 100)
            miss = ", ".join(f[0] for f in d.get("top_missing", [])[:5])
            lines.append(f"| {cat} | {pct}% | {d['products']} | {miss or 'none'} |")
        lines.append("")

    # Semantic validation detail (reuse check_details, not independent heuristics)
    sem_detail = details.get("semantic_validation", {})
    if sem_detail:
        lines.append("## Semantic Validation Detail")
        lines.append("")
        for sub_check, info in sem_detail.items():
            score_pct = int(info.get("score", 1.0) * 100)
            lines.append(f"### {sub_check.replace('_', ' ').title()} ({score_pct}%)")
            if "dirty_count" in info:
                lines.append(f"- {info['dirty_count']} dirty values detected")
            if "flagged_count" in info:
                lines.append(f"- {info['flagged_count']} non-product records flagged")
            if "invalid_count" in info:
                lines.append(f"- {info['invalid_count']}/{info['checked']} products with invalid numeric fields")
            if info.get("examples"):
                lines.append(f"- Examples: {', '.join(str(e)[:80] for e in info['examples'][:3])}")
            lines.append("")

    # Check results table
    lines.append("## Check Results")
    lines.append("")
    lines.append("| Check | Value | Threshold | Score | Status |")
    lines.append("|---|---|---|---|---|")
    for name, check in result["checks"].items():
        if check.get("skipped"):
            lines.append(f"| {name} | - | {check['threshold']} | - | SKIP |")
        else:
            val = check.get("value", 0)
            status = "PASS" if check.get("score", 0) == 0 else "FAIL"
            lines.append(f"| {name} | {val:.2%} | {check['threshold']:.0%} | {check['score']} | {status} |")
    lines.append("")

    return "\n".join(lines)
```

- [ ] **Step 3: Wire into main()**

Replace the current stdout JSON print and stderr summary with:

```python
# Compute results
result = compute_results(products, config, summary, history, baseline)

# Text summary to stdout
print(format_text_summary(result, config))

# Markdown report
report_path = eval_output_dir / "eval_report.md"
report_path.write_text(format_markdown_report(result, config, products))

# JSON result to file only (not stdout)
eval_result_path.write_text(json.dumps(result, indent=2))

# Remove the old stderr summary and the old stdout JSON print
```

- [ ] **Step 4: Test**

```bash
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json
```

Expected: readable text on stdout with per-subcategory breakdowns, eval_report.md in output dir.

- [ ] **Step 5: Commit**

```
git add eval/eval.py
```

---

## Task 4a: Sample size rules (safe, no subprocess)

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add eval_sample_size function**

```python
def eval_sample_size(config: dict) -> dict:
    expected = config.get("expected_product_count", 0)
    total_target = min(max(ceil(expected * 0.3), 50), 300)
    sub_configs = config.get("_sub_configs", {})
    n_subs = len(sub_configs) or 1
    per_sub = {}
    for sub_id, sub_config in sub_configs.items():
        # Fallback: divide total expected by number of subcategories
        sub_expected = sub_config.get("expected_count", expected // n_subs)
        per_sub[sub_id] = max(ceil(sub_expected * 0.1), 10)
    actual_total = max(total_target, sum(per_sub.values())) if per_sub else total_target
    return {"total": actual_total, "per_subcategory": per_sub}
```

- [ ] **Step 2: Add minimum scoreable checks rule**

In `compute_results`, AFTER the status assignment but BEFORE the consecutive degradation logic:

```python
    # Status from degradation score
    if total_degradation <= 30:
        status = "pass"
    elif total_degradation <= 60:
        status = "degraded"
    else:
        status = "fail"

    # Minimum scoreable checks — override status if too few checks ran
    scoreable = sum(1 for v in raw_values.values() if v is not None)
    if scoreable < 3:
        status = "insufficient_data"

    # Consecutive degradation count (only meaningful if status is degraded)
    consecutive_degraded = 0
    if status == "degraded":
        ...
```

- [ ] **Step 3: Test**

```bash
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json
```

Verify `eval_sample_size` returns reasonable numbers by adding a temporary print.

- [ ] **Step 4: Commit**

```
git add eval/eval.py
```

---

## Task 4b: --collect flag (subprocess, higher risk)

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add subprocess import and --collect argparse flag**

```python
import subprocess  # at top of file

# In main():
parser.add_argument("--collect", action="store_true",
                    help="Run scraper to collect sufficient sample before scoring")
```

- [ ] **Step 2: Implement collection logic with error handling**

Place after `products = load_jsonl(scraper_output)` but before baseline/scoring:

```python
if args.collect:
    sample = eval_sample_size(config)
    needed = sample["total"]
    if len(products) < needed:
        scraper_path = project_root / "docs" / "scraper-generator" / slug / "scraper.py"
        if scraper_path.exists():
            print(f"Collecting {needed} products (have {len(products)})...", file=sys.stderr)
            try:
                proc = subprocess.run(
                    ["uv", "run", str(scraper_path), "--limit", str(needed)],
                    cwd=project_root,
                    timeout=min(max(300, needed * 10), 3600),  # cap at 1 hour
                    check=False,  # don't crash on non-zero exit
                )
                if proc.returncode != 0:
                    print(f"Warning: scraper exited with code {proc.returncode}", file=sys.stderr)
            except subprocess.TimeoutExpired:
                print(f"Warning: scraper timed out after {min(max(300, needed * 10), 3600)}s", file=sys.stderr)
            # Reload data
            products = load_jsonl(scraper_output)
            summary = load_json(scraper_summary_path) or {}
            is_limited = summary.get("limited", False)
        else:
            print(f"Warning: scraper not found at {scraper_path}", file=sys.stderr)
```

- [ ] **Step 3: Test with --collect**

```bash
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json --collect
```

Expected: scraper runs, collects more products, then eval scores the larger dataset.

- [ ] **Step 4: Commit**

```
git add eval/eval.py
```

---

## Task 5: Update eval-generator workflow

**Files:**
- Modify: `.claude/skills/eval-generator/references/workflow.md`
- Modify: `.claude/skills/eval-generator/SKILL.md`

- [ ] **Step 1: Update Step 3 (Load SKU Schema) in workflow.md**

Change "use the union of their core/extended Key lists" to:

> For multi-subcategory companies, read ALL subcategory schemas and build a per-subcategory map. Each subcategory gets its own `core_attributes`, `extended_attributes`, and `expected_count`. Do NOT union them. Derive `expected_count` per subcategory from the catalog assessment's category tree — sum leaf category product counts that map to each subcategory. If not derivable, divide `expected_product_count` equally among subcategories.

- [ ] **Step 2: Update Step 4 (Generate Config) in workflow.md**

Replace the flat config schema with the new per-subcategory format:

```json
{
  "company_slug": "<slug>",
  "expected_product_count": 500,
  "expected_top_level_categories": ["Category A", "Category B"],
  "subcategories": {
    "wood.softwood_hardwood_lumber": {
      "core_attributes": ["wood_type", "structural_grade"],
      "extended_attributes": ["species", "nominal_thickness"],
      "expected_count": 300
    },
    "wood.millwork": {
      "core_attributes": ["material", "joint_type"],
      "extended_attributes": ["species", "profile_pattern"],
      "expected_count": 200
    }
  },
  "type_map": {"wood_type": "str", "structural_grade": "str"},
  "enum_attributes": {},
  "has_prices": true,
  "semantic_validation": {
    "numeric_fields": ["nominal_width", "nominal_thickness", "width", "thickness"]
  }
}
```

Update the field derivation table: replace `core_attributes` and `extended_attributes` rows with `subcategories` row.

- [ ] **Step 3: Update checks table and self-verification**

Add check 13 (`semantic_validation`, weight 5, threshold 0.95). Change `duplicate_detection` weight from 10 to 5. Update Step 6 self-verification table to 13 checks.

- [ ] **Step 4: Update strict format rules**

Replace `core_attributes`/`extended_attributes` rules with `subcategories` rules. Add `semantic_validation` rule.

- [ ] **Step 5: Update SKILL.md**

Reference the new config schema in any inline examples.

- [ ] **Step 6: Run skill convention review**

Per CLAUDE.md requirement — run after every change to skill files:

```
/skill-creator-local deep review
```

Fix any convention violations before committing.

- [ ] **Step 7: Commit**

```
git add .claude/skills/eval-generator/references/workflow.md .claude/skills/eval-generator/SKILL.md
```

---

## Task 5b: Regenerate all eval configs

Run `/eval-generator` for each company to produce new-format configs. This enables the final verification.

- [ ] **Step 0: Back up existing configs**

Before regeneration, copy current configs so we can diff and restore if needed:

```bash
for slug in harlowbros iwood thetimbermerchants uk-timber uksleepers pata; do
  cp docs/eval-generator/$slug/eval_config.json docs/eval-generator/$slug/eval_config.json.bak 2>/dev/null || true
done
```

- [ ] **Step 1: Regenerate configs for all 6 companies**

Run in parallel where possible:
```
/eval-generator harlowbros
/eval-generator iwood
/eval-generator thetimbermerchants
/eval-generator uk-timber
/eval-generator uksleepers
/eval-generator pata
```

- [ ] **Step 2: Verify all configs have the `subcategories` key**

```bash
for slug in harlowbros iwood thetimbermerchants uk-timber uksleepers pata; do
  has_subs=$(python3 -c "import json; print('subcategories' in json.load(open('docs/eval-generator/$slug/eval_config.json')))")
  echo "$slug: subcategories=$has_subs"
done
```

- [ ] **Step 3: Commit**

```
git add docs/eval-generator/*/eval_config.json
```

---

## Task 6: Update scraper-generator sample sizes

**Files:**
- Modify: `.claude/skills/scraper-generator/references/validator.md`

- [ ] **Step 1: Update final verification formula**

Change `sample_size = min(ceil(expected_product_count * 0.2), 100)` to:

```
sample_size = min(max(ceil(expected_product_count * 0.1), 20), 100)
```

Update examples: "50 products -> sample 20, 200 -> sample 20, 500 -> sample 50, 1000+ -> sample 100."

- [ ] **Step 2: Update "When to skip" rule**

Change to: "If `expected_product_count <= 20`, skip this phase — the smoke test already covered the full catalog."

- [ ] **Step 3: Run skill convention review**

Per CLAUDE.md requirement — run after every change to skill files:

```
/skill-creator-local deep review
```

Fix any convention violations before committing.

- [ ] **Step 4: Commit**

```
git add .claude/skills/scraper-generator/references/validator.md
```

---

## Task 7: Unit tests for semantic validation

**Files:**
- Create: `eval/test_eval.py`

- [ ] **Step 1: Create test file with fixtures**

```python
"""Unit tests for eval.py semantic validation and per-subcategory scoring."""
from __future__ import annotations
import json
import pytest
from pathlib import Path
from eval import (
    check_semantic_validation,
    check_core_attribute_coverage,
    NUMERIC_VALUE_RE,
    NON_PRODUCT_NAME_RE,
)
```

- [ ] **Step 2: Test NUMERIC_VALUE_RE edge cases**

Test cases:
- `"150mm"` → match (simple metric)
- `"47mm 2\""` → match (dual metric+imperial, common in UK timber)
- `"2.5m"` → match (decimal metric)
- `"150"` → match (bare number)
- `""` → no match (empty)
- `"ternal Cladding - 150mm"` → no match (prose with number)
- `"<div>150</div>"` → no match (HTML)
- `"approximately 150mm"` → no match (prose prefix)

- [ ] **Step 3: Test NON_PRODUCT_NAME_RE false positives**

Verify that the regex does NOT match legitimate product names:
- `"Delivery Pallet"` → matches regex (known limitation, guarded by `has_data` check)
- `"Oak Information Board"` → matches regex (known limitation, guarded by `has_data` check)

Document these as accepted false positives that are handled by the `has_data` guard in sub-check 2.

- [ ] **Step 4: Test check_semantic_validation with has_prices=false**

Create test products with no price but valid attributes. Verify they are NOT flagged as non-products when `config["has_prices"]` is False.

- [ ] **Step 5: Test check_core_attribute_coverage per-subcategory scoring**

Create products with different `product_category` values. Use a config with `_sub_configs` having different core_attributes per subcategory. Verify each product is scored against its own subcategory's schema, not the union.

- [ ] **Step 6: Test with unclassified products**

Products with `product_category` not in `_sub_configs` should fall back to the union list (`default_core`).

- [ ] **Step 7: Run tests**

```bash
uv run python -m pytest eval/test_eval.py -v
```

- [ ] **Step 8: Commit**

```
git add eval/test_eval.py
```

---

## Verification

After all tasks, run eval for all 6 companies:

```bash
for slug in harlowbros iwood thetimbermerchants uk-timber uksleepers pata; do
  echo ""
  uv run eval/eval.py docs/eval-generator/$slug/eval_config.json 2>/dev/null
done
```

Expected:
- harlowbros: core_attribute_coverage ~80% (was 0%), text summary with per-subcategory breakdown
- uk-timber: core_attribute_coverage ~50% (was 30%)
- uksleepers: semantic_validation flags corrupted dimension values
- iwood: semantic_validation flags HTML-in-SKU
- All: eval_report.md generated in output dirs
- All: JSON result in eval_result.json (no longer on stdout)
- All: sample size info in text output (e.g., "need 300 for full eval")
- All: semantic validation detail in markdown report (sub-check scores, examples)

Also test:
```bash
# --collect flag
uv run eval/eval.py docs/eval-generator/harlowbros/eval_config.json --collect

# Verify markdown report has semantic detail section
head -40 docs/eval-generator/harlowbros/output/eval_report.md

# Unit tests
uv run python -m pytest eval/test_eval.py -v
```
