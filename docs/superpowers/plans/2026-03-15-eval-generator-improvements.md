# Eval Generator Improvements Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace per-company eval code generation with a shared eval script reading per-company JSON config, adding 2 new checks (duplicate detection, field-level regression) and rebalancing weights.

**Architecture:** Single shared `eval/eval.py` (stdlib only, PEP 723) reads `eval_config.json` per company. 9 weighted checks, baseline mechanism for regression detection. Agent/skill/docs updated to produce config JSON instead of Python code.

**Tech Stack:** Python 3.10+ stdlib only (json, statistics, datetime, pathlib, argparse). PEP 723 inline metadata. `uv run` for execution.

**Spec:** `docs/superpowers/specs/2026-03-15-eval-generator-improvements-design.md`

---

## Chunk 1: Shared Eval Script

### Task 1: Create eval/eval.py — config loader and data loader

**Files:**
- Create: `eval/eval.py`

- [ ] **Step 1: Create the script skeleton with PEP 723 metadata, imports, constants, and config/data loaders**

```python
# /// script
# requires-python = ">=3.10"
# ///
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from statistics import median

# Universal fields hardcoded — these live at product top level, not in attributes
UNIVERSAL_FIELDS = ["sku", "name", "url", "price", "currency", "scraped_at"]
UNIVERSAL_FIELDS_NO_PRICE = ["sku", "name", "url", "scraped_at"]

CHECKS = {
    "attribute_coverage":      {"weight": 20, "threshold": 0.90},
    "duplicate_detection":     {"weight": 15, "threshold": 0.99},
    "price_sanity":            {"weight": 10, "threshold": 1.0},
    "schema_conformance":      {"weight": 10, "threshold": 1.0},
    "data_freshness":          {"weight": 10, "threshold": 1.0},
    "field_level_regression":  {"weight": 10, "threshold": 0.50},
    "pagination_completeness": {"weight": 10, "threshold": 0.70},
    "category_diversity":      {"weight":  5, "threshold": 0.50},
    "row_count_trend":         {"weight": 10, "threshold": 0.80},
}


def find_project_root(config_path: Path) -> Path:
    """Walk up from config file until a directory containing eval/ is found."""
    current = config_path.resolve().parent
    while current != current.parent:
        if (current / "eval").is_dir():
            return current
        current = current.parent
    print("Error: Could not find project root (no eval/ directory found)", file=sys.stderr)
    sys.exit(1)


def load_config(config_path: Path) -> dict:
    """Read and validate eval_config.json."""
    if not config_path.exists():
        print(f"Error: config not found at {config_path}", file=sys.stderr)
        sys.exit(1)
    config = json.loads(config_path.read_text())
    required = ["company_slug", "expected_product_count", "expected_top_level_categories",
                "core_attributes", "type_map", "enum_attributes", "has_prices"]
    missing = [k for k in required if k not in config]
    if missing:
        print(f"Error: config missing required fields: {missing}", file=sys.stderr)
        sys.exit(1)
    return config


def load_jsonl(path: Path) -> list[dict]:
    """Read NDJSON file, return list of dicts."""
    if not path.exists():
        return []
    products = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                products.append(json.loads(line))
    return products


def load_json(path: Path) -> dict | list | None:
    """Read a JSON file, return parsed content or None if missing/invalid."""
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, ValueError):
        return None
```

- [ ] **Step 2: Verify the skeleton parses**

Run: `uv run python -c "import ast; ast.parse(open('eval/eval.py').read()); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add eval/eval.py
git commit -m "feat(eval): add shared eval script skeleton with config/data loaders"
```

---

### Task 2: Implement all 9 check functions

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add all 9 check functions after the data loaders**

```python
# ---------------------------------------------------------------------------
# Check functions — each returns float (measured value) or None (skip)
# ---------------------------------------------------------------------------


def check_attribute_coverage(products: list[dict], config: dict) -> float:
    """Fraction of products with >80% of core attributes populated."""
    if not products:
        return 0.0
    universals = UNIVERSAL_FIELDS_NO_PRICE if not config["has_prices"] else UNIVERSAL_FIELDS
    core_nested = config["core_attributes"]
    total_core = len(universals) + len(core_nested)
    if total_core == 0:
        return 1.0
    passing = 0
    for product in products:
        populated = 0
        for field in universals:
            val = product.get(field)
            if val is not None and val != "" and val != []:
                populated += 1
        attrs = product.get("attributes", {})
        for field in core_nested:
            val = attrs.get(field)
            if val is not None and val != "" and val != []:
                populated += 1
        if populated / total_core > 0.80:
            passing += 1
    return passing / len(products)


def check_duplicate_detection(products: list[dict]) -> float:
    """Fraction of unique SKUs. 1.0 = no duplicates."""
    if not products:
        return 1.0
    skus = [p.get("sku") for p in products if p.get("sku")]
    if not skus:
        return 1.0
    return len(set(skus)) / len(skus)


def check_price_sanity(products: list[dict], config: dict) -> float | None:
    """Fraction of priced products with sane prices. None if no prices."""
    if not config["has_prices"]:
        return None
    prices = [p["price"] for p in products if p.get("price") is not None]
    if not prices:
        return None
    med = median(prices)
    max_ok = med * 10 if med > 0 else float("inf")
    sane = sum(1 for p in prices if p > 0 and p <= max_ok)
    return sane / len(prices)


def check_schema_conformance(products: list[dict], config: dict) -> float:
    """Fraction of attribute-value pairs conforming to expected types."""
    if not products:
        return 1.0
    type_map = config.get("type_map", {})
    enum_attrs = config.get("enum_attributes", {})
    total, conforming = 0, 0
    for product in products:
        attrs = product.get("attributes", {})
        for attr_name, attr_val in attrs.items():
            if attr_name not in type_map:
                continue
            if attr_val is None:
                continue
            total += 1
            expected_type = type_map[attr_name]
            # Enum check takes precedence
            if attr_name in enum_attrs:
                if attr_val in enum_attrs[attr_name]:
                    conforming += 1
                continue
            # Type check
            if expected_type == "str" and isinstance(attr_val, str) and attr_val.strip():
                conforming += 1
            elif expected_type == "number" and isinstance(attr_val, (int, float)):
                conforming += 1
            elif expected_type == "list" and isinstance(attr_val, list):
                conforming += 1
            elif expected_type == "bool" and isinstance(attr_val, bool):
                conforming += 1
    return conforming / total if total > 0 else 1.0


def check_data_freshness(products: list[dict]) -> float:
    """Fraction of products with scraped_at within last 24 hours."""
    if not products:
        return 0.0
    cutoff = datetime.now(timezone.utc) - timedelta(hours=24)
    fresh = 0
    for product in products:
        scraped_at = product.get("scraped_at", "")
        if not scraped_at:
            continue
        try:
            ts = datetime.fromisoformat(scraped_at)
            if ts >= cutoff:
                fresh += 1
        except ValueError:
            continue
    return fresh / len(products)


def check_field_level_regression(
    products: list[dict], config: dict, baseline: dict | None
) -> float | None:
    """Fraction of core attributes whose fill rate has not regressed vs baseline."""
    if baseline is None:
        return None
    baseline_rates = baseline.get("attribute_fill_rates", {})
    if not baseline_rates:
        return None
    core_nested = config["core_attributes"]
    universals = UNIVERSAL_FIELDS_NO_PRICE if not config["has_prices"] else UNIVERSAL_FIELDS
    all_core = list(universals) + list(core_nested)
    if not all_core:
        return 1.0
    # Compute current fill rates
    current_rates: dict[str, float] = {}
    for attr in all_core:
        if not products:
            current_rates[attr] = 0.0
            continue
        filled = 0
        for product in products:
            if attr in UNIVERSAL_FIELDS:
                val = product.get(attr)
            else:
                val = product.get("attributes", {}).get(attr)
            if val is not None and val != "" and val != []:
                filled += 1
        current_rates[attr] = filled / len(products)
    # Compare against baseline
    not_regressed = 0
    checked = 0
    for attr in all_core:
        bl_rate = baseline_rates.get(attr)
        if bl_rate is None or bl_rate == 0:
            not_regressed += 1
            checked += 1
            continue
        checked += 1
        cur_rate = current_rates.get(attr, 0.0)
        if cur_rate >= bl_rate * 0.5:
            not_regressed += 1
    return not_regressed / checked if checked > 0 else 1.0


def check_pagination_completeness(
    products_found: int, config: dict, is_limited: bool
) -> float | None:
    """Ratio of actual to expected product count. None on limited runs."""
    if is_limited:
        return None
    expected = config["expected_product_count"]
    if expected <= 0:
        return None
    return products_found / expected


def check_category_diversity(
    products: list[dict], config: dict, is_limited: bool
) -> float | None:
    """Set intersection of actual vs expected top-level categories."""
    if is_limited:
        return None
    expected = set(config.get("expected_top_level_categories", []))
    if not expected:
        return None
    actual: set[str] = set()
    for product in products:
        cat_path = product.get("category_path", "")
        if " > " in cat_path:
            actual.add(cat_path.split(" > ")[0])
        elif cat_path:
            actual.add(cat_path)
    return len(expected & actual) / len(expected)


def check_row_count_trend(
    products_found: int, is_limited: bool, history: list[dict]
) -> float | None:
    """Ratio of current to previous product count. None on limited/first run."""
    if is_limited:
        return None
    if not history:
        return None
    prev = history[-1]
    if prev.get("limited", False):
        return None
    prev_count = prev.get("products_found", 0)
    if prev_count == 0:
        return None
    return products_found / prev_count
```

- [ ] **Step 2: Verify the script still parses**

Run: `uv run python -c "import ast; ast.parse(open('eval/eval.py').read()); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add eval/eval.py
git commit -m "feat(eval): implement all 9 check functions"
```

---

### Task 3: Implement scorer, baseline manager, output writer, and CLI

**Files:**
- Modify: `eval/eval.py`

- [ ] **Step 1: Add scorer, baseline, output, and main() at the end of eval/eval.py**

```python
# ---------------------------------------------------------------------------
# Scorer — weight redistribution, degradation, status
# ---------------------------------------------------------------------------


def compute_results(
    products: list[dict],
    config: dict,
    summary: dict,
    history: list[dict],
    baseline: dict | None,
) -> dict:
    products_found = summary.get("total_products", len(products))
    is_limited = summary.get("limited", False)

    raw_values = {
        "attribute_coverage": check_attribute_coverage(products, config),
        "duplicate_detection": check_duplicate_detection(products),
        "price_sanity": check_price_sanity(products, config),
        "schema_conformance": check_schema_conformance(products, config),
        "data_freshness": check_data_freshness(products),
        "field_level_regression": check_field_level_regression(products, config, baseline),
        "pagination_completeness": check_pagination_completeness(products_found, config, is_limited),
        "category_diversity": check_category_diversity(products, config, is_limited),
        "row_count_trend": check_row_count_trend(products_found, is_limited, history),
    }

    # Weight redistribution
    skipped = {k for k, v in raw_values.items() if v is None}
    active_weight = sum(CHECKS[k]["weight"] for k in CHECKS if k not in skipped)
    multiplier = 100.0 / active_weight if active_weight > 0 else 1.0

    checks_output: dict[str, dict] = {}
    total_degradation = 0.0

    for name, spec in CHECKS.items():
        threshold = spec["threshold"]
        value = raw_values[name]
        if value is None:
            checks_output[name] = {
                "score": 0, "value": None, "threshold": threshold,
                "weight": spec["weight"], "skipped": True,
            }
        else:
            ew = spec["weight"] * multiplier
            score = ew * (threshold - value) / threshold if value < threshold else 0.0
            total_degradation += score
            checks_output[name] = {
                "score": round(score, 2), "value": round(value, 4),
                "threshold": threshold, "weight": spec["weight"],
            }

    total_degradation = round(total_degradation, 2)
    if total_degradation <= 30:
        status = "pass"
    elif total_degradation <= 60:
        status = "degraded"
    else:
        status = "fail"

    # Consecutive degradation count
    consecutive_degraded = 0
    if status == "degraded":
        consecutive_degraded = 1
        for prev in reversed(history):
            if prev.get("status") == "degraded":
                consecutive_degraded += 1
            else:
                break

    recommend_rediscovery = status == "fail" or consecutive_degraded >= 3

    return {
        "status": status,
        "checks": checks_output,
        "degradation_score": total_degradation,
        "products_found": products_found,
        "recommend_rediscovery": recommend_rediscovery,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------------------
# Baseline manager
# ---------------------------------------------------------------------------


def compute_fill_rates(products: list[dict], config: dict) -> dict[str, float]:
    """Compute fill rate for every universal + core attribute."""
    universals = UNIVERSAL_FIELDS if config["has_prices"] else UNIVERSAL_FIELDS_NO_PRICE
    all_attrs = list(universals) + list(config["core_attributes"])
    rates: dict[str, float] = {}
    for attr in all_attrs:
        if not products:
            rates[attr] = 0.0
            continue
        filled = 0
        for product in products:
            if attr in UNIVERSAL_FIELDS:
                val = product.get(attr)
            else:
                val = product.get("attributes", {}).get(attr)
            if val is not None and val != "" and val != []:
                filled += 1
        rates[attr] = round(filled / len(products), 4)
    return rates


def maybe_create_baseline(
    products: list[dict], config: dict, is_limited: bool, baseline_path: Path
) -> dict | None:
    """Create baseline on first full run. Returns existing or new baseline."""
    if baseline_path.exists():
        return load_json(baseline_path)
    if is_limited:
        return None
    if not products:
        return None
    # Create baseline
    top_cats: set[str] = set()
    for p in products:
        cat = p.get("category_path", "")
        if " > " in cat:
            top_cats.add(cat.split(" > ")[0])
        elif cat:
            top_cats.add(cat)
    baseline = {
        "products_found": len(products),
        "attribute_fill_rates": compute_fill_rates(products, config),
        "categories": sorted(top_cats),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    baseline_path.write_text(json.dumps(baseline, indent=2))
    print(f"Baseline created at {baseline_path}", file=sys.stderr)
    return baseline


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate scraper output quality")
    parser.add_argument("config", type=Path, help="Path to eval_config.json")
    args = parser.parse_args()

    config = load_config(args.config)
    project_root = find_project_root(args.config)
    slug = config["company_slug"]

    # Resolve paths
    scraper_output = project_root / "docs" / "scraper-generator" / slug / "output" / "products.jsonl"
    scraper_summary_path = project_root / "docs" / "scraper-generator" / slug / "output" / "summary.json"
    eval_output_dir = args.config.resolve().parent / "output"
    eval_result_path = eval_output_dir / "eval_result.json"
    eval_history_path = eval_output_dir / "eval_history.json"
    baseline_path = eval_output_dir / "baseline.json"
    eval_output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    products = load_jsonl(scraper_output)
    summary = load_json(scraper_summary_path) or {}
    history = load_json(eval_history_path) or []
    if not isinstance(history, list):
        history = []
    is_limited = summary.get("limited", False)

    if not products:
        print("Warning: No products found in scraper output.", file=sys.stderr)

    # Baseline
    baseline = maybe_create_baseline(products, config, is_limited, baseline_path)

    # Run checks
    result = compute_results(products, config, summary, history, baseline)

    # Write result
    eval_result_path.write_text(json.dumps(result, indent=2))

    # Append to history
    history_entry = {
        "status": result["status"],
        "degradation_score": result["degradation_score"],
        "products_found": result["products_found"],
        "limited": is_limited,
        "timestamp": result["timestamp"],
    }
    history.append(history_entry)
    eval_history_path.write_text(json.dumps(history, indent=2))

    # Print summary to stderr
    print(f"Status: {result['status']}", file=sys.stderr)
    print(f"Degradation score: {result['degradation_score']}", file=sys.stderr)
    print(f"Products found: {result['products_found']}", file=sys.stderr)
    print(f"Recommend rediscovery: {result['recommend_rediscovery']}", file=sys.stderr)
    for name, check in result["checks"].items():
        if check.get("skipped"):
            print(f"  {name}: SKIPPED", file=sys.stderr)
        else:
            print(f"  {name}: value={check['value']} threshold={check['threshold']} score={check['score']}", file=sys.stderr)

    # Print full result to stdout
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify the complete script parses**

Run: `uv run python -c "import ast; ast.parse(open('eval/eval.py').read()); print('OK')"`
Expected: `OK`

- [ ] **Step 3: Commit**

```bash
git add eval/eval.py
git commit -m "feat(eval): add scorer, baseline manager, output writer, and CLI"
```

---

### Task 4: Test the shared eval against an existing company

**Files:**
- Read: `docs/scraper-generator/finieris/output/products.jsonl`
- Create: `docs/eval-generator/finieris/eval_config.json`

- [ ] **Step 1: Create a test eval_config.json for finieris**

Write to `docs/eval-generator/finieris/eval_config.json`:

```json
{
  "company_slug": "finieris",
  "expected_product_count": 31,
  "expected_top_level_categories": ["Riga Wood"],
  "core_attributes": [
    "brand", "manufacturer", "panel_type", "wood_species",
    "surface_treatment", "description", "country_of_origin"
  ],
  "type_map": {
    "brand": "str",
    "manufacturer": "str",
    "panel_type": "str",
    "wood_species": "str",
    "surface_treatment": "str",
    "description": "str",
    "applications": "list",
    "advantages": "list",
    "available_sizes": "list",
    "standard_thicknesses": "str",
    "grades": "list",
    "overlay_colors": "list",
    "overlay_resin_types": "list",
    "further_processing": "str",
    "certifications": "list",
    "country_of_origin": "str"
  },
  "enum_attributes": {
    "surface_treatment": ["Uncoated", "Film-faced", "HPL", "Lacquered", "Melamine", "Primed", "Decorative", "Textured overlay", "Composite"]
  },
  "has_prices": false
}
```

- [ ] **Step 2: Check finieris summary.json to understand the limited flag**

Run: `uv run python -c "import json; s=json.load(open('docs/scraper-generator/finieris/output/summary.json')); print(f\"limited={s.get('limited')}\")"`
Expected: Shows `limited=True` or `limited=False` — this determines whether baseline.json gets created.

- [ ] **Step 3: Clear any previous eval output to start fresh**

Run: `rm -f docs/eval-generator/finieris/output/eval_result.json docs/eval-generator/finieris/output/eval_history.json docs/eval-generator/finieris/output/baseline.json`

- [ ] **Step 4: Run the shared eval script against finieris**

Run: `uv run eval/eval.py docs/eval-generator/finieris/eval_config.json`
Expected: Prints eval result JSON to stdout, summary to stderr. Status should be `pass`. No crash.

- [ ] **Step 5: Verify the output files were created**

Run: `ls -la docs/eval-generator/finieris/output/`
Expected: `eval_result.json` and `eval_history.json` exist. Whether `baseline.json` exists depends on the `limited` flag from Step 2 — if `limited=True`, no baseline; if `limited=False`, baseline is created.

- [ ] **Step 6: Verify output JSON structure has all 9 checks**

Run: `uv run python -c "import json; d=json.load(open('docs/eval-generator/finieris/output/eval_result.json')); assert len(d['checks']) == 9; assert all(c in d['checks'] for c in ['attribute_coverage','duplicate_detection','price_sanity','schema_conformance','data_freshness','field_level_regression','pagination_completeness','category_diversity','row_count_trend']); print('All 9 checks present')"`
Expected: `All 9 checks present`

- [ ] **Step 7: Commit**

```bash
git add eval/eval.py docs/eval-generator/finieris/eval_config.json
git commit -m "test(eval): verify shared eval against finieris scraper output"
```

---

## Chunk 2: Agent, Skill, and Documentation Updates

### Task 5: Rewrite the eval-generator agent

**Files:**
- Modify: `agents/eval-generator.md`

- [ ] **Step 1: Rewrite agents/eval-generator.md**

Replace the entire file. The agent's job is now:
1. Read scraper source, catalog assessment, SKU schema (Steps 1-3 — same context gathering)
2. Produce `eval_config.json` with the correct values (Step 4 — simplified from 400 lines of Python to 20 lines of JSON)
3. Run the shared eval script and verify output (Step 5 — validation)

Key changes from current:
- Remove all Python code quality instructions (PEP 723, imports, error handling, etc.)
- Remove all check implementation details (scoring formula, weight redistribution, etc.)
- Remove the "Generate the Eval Script" section — replace with "Generate the Eval Config"
- Keep decisions unchanged (no_sku_schema, scraper_output_format_unclear, missing_product_count_estimate)
- Add config schema reference and field descriptions
- Self-verification: validate config JSON has all required fields, run the shared eval, check 9 checks present in output

- [ ] **Step 2: Verify the agent file is valid markdown and references logical resources correctly**

Check that:
- No file paths appear in the agent file (harness-agnostic)
- References use logical names: "the shared eval script", "the eval config file", "the company report", etc.
- No tool names appear (no "WebFetch", "Read", etc.)

- [ ] **Step 3: Commit**

```bash
git add agents/eval-generator.md
git commit -m "feat(eval): rewrite eval-generator agent for config-based approach"
```

---

### Task 6: Update the eval-generator skill wrapper

**Files:**
- Modify: `.claude/skills/eval-generator/SKILL.md`

- [ ] **Step 1: Update .claude/skills/eval-generator/SKILL.md**

Key changes:
- Description: "Produces an eval_config.json" not "Produces an eval.py"
- File locations table: add `Shared eval script | eval/eval.py`, change output from `eval.py` to `eval_config.json`, add `baseline.json`
- Wiring section: run command changes to `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`
- Remove references to Python code generation
- Update slug derivation to only reference `{slug}` (no `{category-slug}` needed for eval — the config captures everything)

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/eval-generator/SKILL.md
git commit -m "feat(eval): update eval-generator skill wrapper for config approach"
```

---

### Task 7: Update the product-discovery orchestrator

**Files:**
- Modify: `.claude/skills/product-discovery/SKILL.md`

- [ ] **Step 1: Update .claude/skills/product-discovery/SKILL.md**

Changes needed:
- Line 94: "seven weighted checks" → "nine weighted checks"
- Line 131: `### Eval` section: "7 weighted checks" → "9 weighted checks"
- Line 151: Generated files table: `Eval script | docs/eval-generator/{slug}/eval.py` → `Eval config | docs/eval-generator/{slug}/eval_config.json`
- Line 162: Run command: `uv run docs/eval-generator/{slug}/eval.py` → `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/product-discovery/SKILL.md
git commit -m "feat(eval): update product-discovery orchestrator for new eval approach"
```

---

### Task 8: Update README.md and CLAUDE.md

**Files:**
- Modify: `README.md`
- Modify: `CLAUDE.md`

- [ ] **Step 1: Update README.md**

Changes:
- Line 15 diagram: `eval.py` → `eval` (still in the cheap tier diagram, no change needed to the flow)
- Line 47: "seven weighted checks" → "nine weighted checks"
- Line 72: Run command: `uv run docs/eval-generator/{slug}/eval.py` → `uv run eval/eval.py docs/eval-generator/{slug}/eval_config.json`
- Line 88: "seven weighted checks" → "nine weighted checks"
- Lines 143-145: Project structure: update eval-generator section to show `eval_config.json` instead of `eval.py`, add `eval/` directory
- Line 148: closing note unchanged

- [ ] **Step 2: Update CLAUDE.md**

Changes:
- Line 9: "eval.py" → "eval_config.json" in the cheap tier description or remove specific reference
- Line 21: `docs/eval-generator/` description: "Eval artifacts (eval.py, output/)" → "Eval artifacts (eval_config.json, output/)"
- Add `eval/` to the Key Directories section: `eval/` — Shared eval script (quality validation)

- [ ] **Step 3: Commit**

```bash
git add README.md CLAUDE.md
git commit -m "docs: update README and CLAUDE.md for new eval architecture"
```

---

### Task 9: Final integration test — run pipeline-style eval for multiple companies

**Files:**
- Create: `docs/eval-generator/festool/eval_config.json` (test)

- [ ] **Step 1: Create eval_config.json for festool to test a second company**

Read the existing festool scraper output to determine correct config values. Write the config file.

- [ ] **Step 2: Run the eval for festool**

Run: `uv run eval/eval.py docs/eval-generator/festool/eval_config.json`
Expected: Passes without error, prints 9 checks.

- [ ] **Step 3: Run the eval for finieris again to verify history append**

Run: `uv run eval/eval.py docs/eval-generator/finieris/eval_config.json`
Expected: `eval_history.json` now has 2 entries.

- [ ] **Step 4: Verify the eval_history has correct structure**

Run: `uv run python -c "import json; h=json.load(open('docs/eval-generator/finieris/output/eval_history.json')); assert len(h) >= 2; print(f'{len(h)} history entries')"`
Expected: `2 history entries` (or more)

- [ ] **Step 5: Push all changes**

```bash
git push
```
