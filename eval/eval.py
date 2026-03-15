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
