# /// script
# requires-python = ">=3.10"
# ///
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from math import ceil
from pathlib import Path
from statistics import median
from typing import Any

# Mandatory core attributes — these live at product top level, not in attributes
MANDATORY_CORE_FIELDS = ["sku", "name", "url", "price", "currency", "brand", "scraped_at"]
MANDATORY_CORE_FIELDS_NO_PRICE = ["sku", "name", "url", "brand", "scraped_at"]

# 13 checks with weights summing to 100
CHECKS = {
    "core_attribute_coverage":     {"weight": 20, "threshold": 0.90},
    "extended_attribute_coverage": {"weight":  5, "threshold": 0.90},
    "pagination_completeness":     {"weight": 10, "threshold": 0.70},
    "category_diversity":          {"weight":  5, "threshold": 0.50},
    "category_classification":     {"weight": 10, "threshold": 0.95},
    "price_sanity":                {"weight": 10, "threshold": 1.00},
    "data_freshness":              {"weight":  5, "threshold": 1.00},
    "schema_conformance":          {"weight":  5, "threshold": 1.00},
    "row_count_trend":             {"weight":  5, "threshold": 0.80},
    "duplicate_detection":         {"weight":  5, "threshold": 0.99},
    "field_level_regression":      {"weight": 10, "threshold": 0.50},
    "extra_attributes_ratio":      {"weight":  5, "threshold": 0.50},
    "semantic_validation":         {"weight":  5, "threshold": 0.95},
}

# Semantic validation regex constants
NUMERIC_VALUE_RE = re.compile(r'^\d+(\.\d+)?\s*[a-zA-Z/"]*(\s+\d+(\.\d+)?\s*[a-zA-Z/"]*)?$')
NON_PRODUCT_NAME_RE = re.compile(
    r'Delivery|Contact Us|FAQ|Branch Locator|Information|Privacy|Terms|Cookie',
    re.IGNORECASE,
)
NON_PRODUCT_URL_RE = re.compile(
    r'/contact|/about|/faq|/terms|/privacy|/delivery|/cookie',
    re.IGNORECASE,
)

# Embedded-unit detection — consistent with scraper-generator's tester_evaluate_semantic.py
EMBEDDED_UNIT_RE = re.compile(
    r"\d+\s*(mm|cm|m|kg|g|lb|oz|ml|l|V|W|A|Hz|kW|kWh|MPa|Nm|bpm|psi|in|ft|rpm|dB|%)$"
)


def find_project_root(config_path: Path) -> Path:
    """Walk up from config file until a directory containing docs/ is found."""
    current = config_path.resolve().parent
    while current != current.parent:
        if (current / "docs").is_dir():
            return current
        current = current.parent
    print("Error: Could not find project root (no docs/ directory found)", file=sys.stderr)
    sys.exit(1)


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
# Sample size
# ---------------------------------------------------------------------------


def eval_sample_size(config: dict) -> dict:
    """20% of subcategory capacity, max 100 per subcategory."""
    sub_configs = config.get("_sub_configs", {})
    per_sub = {}
    for sub_id, sub_config in sub_configs.items():
        capacity = sub_config.get("expected_count", 0)
        per_sub[sub_id] = min(max(ceil(capacity * 0.20), 10), 100)
    total = sum(per_sub.values()) if per_sub else min(max(ceil(config.get("expected_product_count", 0) * 0.20), 10), 100)
    return {"total": total, "per_subcategory": per_sub}


# ---------------------------------------------------------------------------
# Scraper config helpers
# ---------------------------------------------------------------------------


def load_scraper_config(path: Path) -> dict | None:
    """Read the scraper's config.json. Returns None if missing or invalid."""
    return load_json(path)


def build_category_key_map(scraper_config: dict) -> dict[str, list[str]]:
    """Invert category_mapping (URL prefix -> taxonomy ID) to (taxonomy ID -> [URL prefixes]).

    The scraper's config.json has:
        "category_mapping": {"url-prefix-1": "taxonomy.id", "url-prefix-2": "taxonomy.id"}

    We need the inverse to run per-subcategory collection:
        {"taxonomy.id": ["url-prefix-1", "url-prefix-2"]}
    """
    category_mapping = scraper_config.get("category_mapping", {})
    inverted: dict[str, list[str]] = {}
    for key, taxonomy_id in category_mapping.items():
        inverted.setdefault(taxonomy_id, []).append(key)
    return inverted


# ---------------------------------------------------------------------------
# Check functions
# ---------------------------------------------------------------------------


def check_core_attribute_coverage(products: list[dict], config: dict) -> tuple[float, dict]:
    """Per-subcategory core attribute coverage. Returns (score, detail)."""
    if not products:
        return 0.0, {}
    sub_configs = config.get("_sub_configs", {})
    mandatory_fields = MANDATORY_CORE_FIELDS_NO_PRICE if not config["has_prices"] else MANDATORY_CORE_FIELDS
    default_core = config.get("core_attributes", [])

    sub_stats: dict[str, dict] = {}
    passing = 0

    for product in products:
        cat = product.get("product_category", "_unclassified")
        sub = sub_configs.get(cat)
        core_nested = sub.get("core_attributes", default_core) if sub else default_core
        total_core = len(mandatory_fields) + len(core_nested)
        if total_core == 0:
            passing += 1
            continue

        populated = 0
        missing = []
        for field in mandatory_fields:
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

        passed = populated / total_core >= 0.75
        if passed:
            passing += 1

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


def check_extended_attribute_coverage(
    products: list[dict], config: dict
) -> tuple[float, dict] | None:
    """Per-subcategory extended attribute coverage. Returns (score, detail) or None."""
    default_extended = config.get("extended_attributes", [])
    if not default_extended:
        return None
    if not products:
        return 0.0, {}

    sub_configs = config.get("_sub_configs", {})
    sub_stats: dict[str, dict] = {}
    passing = 0

    for product in products:
        cat = product.get("product_category", "_unclassified")
        sub = sub_configs.get(cat)
        extended_attrs = sub.get("extended_attributes", default_extended) if sub else default_extended
        if not extended_attrs:
            passing += 1
            continue

        ext = product.get("extended_attributes", {})
        populated = sum(1 for a in extended_attrs if ext.get(a) not in (None, "", []))
        missing = [a for a in extended_attrs if ext.get(a) in (None, "", [])]
        passed = populated / len(extended_attrs) > 0.50
        if passed:
            passing += 1

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


def check_semantic_validation(products: list[dict], config: dict) -> tuple[float, dict] | None:
    """Composite semantic check. Always runs (never returns None).

    Sub-checks:
    1. Value cleanliness — config-independent
    2. Non-product detection — config-independent
    3. Numeric field format — conditional on semantic_validation.numeric_fields
    4. Embedded-units detection — config-independent, scans all attribute buckets
    """
    if not products:
        return 0.0, {}

    sem_config = config.get("semantic_validation") or {}
    scores: list[float] = []
    detail: dict[str, Any] = {}
    has_prices = config.get("has_prices", True)

    # Sub-check 1: Value cleanliness
    clean = 0
    dirty_examples: list[str] = []
    for p in products:
        all_vals: list[str] = []
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
    cleanliness_score = clean / len(products)
    scores.append(cleanliness_score)
    detail["value_cleanliness"] = {
        "score": round(cleanliness_score, 4),
        "dirty_count": len(products) - clean,
        "examples": dirty_examples,
    }

    # Sub-check 2: Non-product detection
    real = 0
    non_product_examples: list[str] = []
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
            is_non_product = (
                (NON_PRODUCT_NAME_RE.search(name) and not has_attrs)
                or (NON_PRODUCT_URL_RE.search(url) and not has_attrs)
                or (not p.get("sku") and not has_attrs)
            )
        if not is_non_product:
            real += 1
        elif len(non_product_examples) < 3:
            non_product_examples.append(p.get("name", "?")[:60])
    non_product_score = real / len(products)
    scores.append(non_product_score)
    detail["non_product_detection"] = {
        "score": round(non_product_score, 4),
        "flagged_count": len(products) - real,
        "examples": non_product_examples,
    }

    # Sub-check 3: Numeric field format (conditional on config)
    numeric_fields = sem_config.get("numeric_fields", [])
    if numeric_fields:
        valid_products = 0
        checked_products = 0
        bad_examples: list[dict] = []
        for p in products:
            all_attrs = {
                **p.get("core_attributes", {}),
                **p.get("extended_attributes", {}),
                **p.get("extra_attributes", {}),
            }
            relevant = {
                k: v for k, v in all_attrs.items()
                if k in numeric_fields and v is not None and str(v).strip()
            }
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

    # Sub-check 4: Embedded-units detection
    clean_unit = 0
    embedded_unit_examples: list[dict] = []
    for p in products:
        has_embedded = False
        offending: dict[str, str] = {}
        for bucket in ("core_attributes", "extended_attributes", "extra_attributes"):
            for k, v in p.get(bucket, {}).items():
                if v is not None and isinstance(v, str) and EMBEDDED_UNIT_RE.search(v):
                    has_embedded = True
                    offending[k] = v
        if not has_embedded:
            clean_unit += 1
        elif len(embedded_unit_examples) < 3:
            embedded_unit_examples.append(offending)
    embedded_unit_score = clean_unit / len(products)
    scores.append(embedded_unit_score)
    detail["embedded_units"] = {
        "score": round(embedded_unit_score, 4),
        "flagged_count": len(products) - clean_unit,
        "examples": embedded_unit_examples,
    }

    composite = min(scores) if scores else 1.0
    return composite, detail


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
        attrs = {
            **product.get("core_attributes", {}),
            **product.get("extended_attributes", {}),
            **product.get("extra_attributes", {}),
        }
        for attr_name, attr_val in attrs.items():
            if attr_val is None:
                continue
            if attr_name in type_map:
                total += 1
                expected_type = type_map[attr_name]
                if attr_name in enum_attrs:
                    if attr_val in enum_attrs[attr_name]:
                        conforming += 1
                    continue
                if expected_type == "str" and isinstance(attr_val, str) and attr_val.strip():
                    conforming += 1
                elif expected_type == "number" and isinstance(attr_val, (int, float)):
                    conforming += 1
                elif expected_type == "list" and isinstance(attr_val, list):
                    conforming += 1
                elif expected_type == "bool" and isinstance(attr_val, bool):
                    conforming += 1
            else:
                # Attributes NOT in type_map: basic sanity check
                total += 1
                if isinstance(attr_val, (int, float, bool)):
                    conforming += 1
                elif isinstance(attr_val, list):
                    conforming += 1
                elif isinstance(attr_val, str):
                    # Must be non-empty and not contain HTML
                    if attr_val.strip() and not re.search(r'<[a-z]', attr_val):
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
    mandatory_fields = MANDATORY_CORE_FIELDS_NO_PRICE if not config["has_prices"] else MANDATORY_CORE_FIELDS
    all_core = list(mandatory_fields) + list(core_nested)
    if not all_core:
        return 1.0
    current_rates: dict[str, float] = {}
    for attr in all_core:
        if not products:
            current_rates[attr] = 0.0
            continue
        filled = 0
        for product in products:
            if attr in MANDATORY_CORE_FIELDS:
                val = product.get(attr)
            else:
                val = product.get("core_attributes", {}).get(attr)
            if val is not None and val != "" and val != []:
                filled += 1
        current_rates[attr] = filled / len(products)
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


def check_category_classification(
    products: list[dict], is_limited: bool
) -> float | None:
    """Fraction of products with a valid product_category. Skipped on limited runs."""
    if is_limited:
        return None
    if not products:
        return 0.0
    classified = sum(
        1 for p in products
        if p.get("product_category")
        and p["product_category"] != "_unclassified"
        and "." in p["product_category"]
    )
    return classified / len(products)


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


def check_extra_attributes_ratio(products: list[dict]) -> float | None:
    """Average of 1 - (extra_count / (core_count + extended_count))."""
    if not products:
        return 0.0
    ratios = []
    for product in products:
        core_count = len(product.get("core_attributes", {}))
        extended_count = len(product.get("extended_attributes", {}))
        extra_count = len(product.get("extra_attributes", {}))
        mapped = core_count + extended_count
        if mapped == 0:
            continue
        ratio = max(0.0, 1 - (extra_count / mapped))
        ratios.append(ratio)
    return sum(ratios) / len(ratios) if ratios else 1.0


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

    # Functions returning (value, detail)
    core_value, core_detail = check_core_attribute_coverage(products, config)
    ext_result = check_extended_attribute_coverage(products, config)
    if ext_result is not None:
        ext_value, ext_detail = ext_result
    else:
        ext_value, ext_detail = None, {}

    sem_result = check_semantic_validation(products, config)
    if sem_result is not None:
        sem_value, sem_detail = sem_result
    else:
        sem_value, sem_detail = None, {}

    raw_values = {
        "core_attribute_coverage": core_value,
        "extended_attribute_coverage": ext_value,
        "pagination_completeness": check_pagination_completeness(products_found, config, is_limited),
        "category_diversity": check_category_diversity(products, config, is_limited),
        "category_classification": check_category_classification(products, is_limited),
        "price_sanity": check_price_sanity(products, config),
        "data_freshness": check_data_freshness(products),
        "schema_conformance": check_schema_conformance(products, config),
        "row_count_trend": check_row_count_trend(products_found, is_limited, history),
        "duplicate_detection": check_duplicate_detection(products),
        "field_level_regression": check_field_level_regression(products, config, baseline),
        "extra_attributes_ratio": check_extra_attributes_ratio(products),
        "semantic_validation": sem_value,
    }

    check_details = {
        "core_attribute_coverage": core_detail,
        "extended_attribute_coverage": ext_detail,
        "semantic_validation": sem_detail,
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

    # Minimum scoreable checks — override status if too few checks ran
    scoreable = sum(1 for v in raw_values.values() if v is not None)
    if scoreable < 3:
        status = "insufficient_data"

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
        "check_details": check_details,
    }


# ---------------------------------------------------------------------------
# Baseline manager
# ---------------------------------------------------------------------------


def compute_fill_rates(products: list[dict], config: dict) -> dict[str, float]:
    """Compute fill rate for every mandatory core + category-specific core attribute."""
    mandatory_fields = MANDATORY_CORE_FIELDS if config["has_prices"] else MANDATORY_CORE_FIELDS_NO_PRICE
    all_attrs = list(mandatory_fields) + list(config["core_attributes"])
    rates: dict[str, float] = {}
    for attr in all_attrs:
        if not products:
            rates[attr] = 0.0
            continue
        filled = 0
        for product in products:
            if attr in MANDATORY_CORE_FIELDS:
                val = product.get(attr)
            else:
                val = product.get("core_attributes", {}).get(attr)
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
# Output formatting
# ---------------------------------------------------------------------------


def format_text_summary(result: dict, config: dict) -> str:
    """Human-readable text summary for stdout."""
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
                if sem.get("embedded_units", {}).get("flagged_count", 0):
                    parts.append(f"{sem['embedded_units']['flagged_count']} embedded units")
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
    sub_cats = set()
    core_detail = details.get("core_attribute_coverage", {})
    sub_cats.update(core_detail.keys())
    sub_count = len(sub_cats) if sub_cats else "?"
    sample_line = f"SAMPLE: {found} products from {sub_count} subcategories"
    if found < needed:
        sample_line += f" (need {needed} for full eval)"
    lines.append(sample_line)
    return "\n".join(lines)


def format_markdown_report(result: dict, config: dict, products: list[dict]) -> str:
    """Markdown report written to output directory."""
    lines = [f"# Eval Report: {config['company_slug']}", ""]
    lines.append(f"**Status:** {result['status'].upper()}")
    lines.append(f"**Degradation score:** {result['degradation_score']}")
    lines.append(f"**Products scored:** {result['products_found']}")

    sample = eval_sample_size(config)
    needed = sample["total"]
    if result["products_found"] < needed:
        lines.append(f"**Sample gap:** have {result['products_found']}, need {needed} for full eval")
    lines.append("")

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
                lines.append(f"- {info['flagged_count']} {'embedded unit values' if sub_check == 'embedded_units' else 'non-product records'} flagged")
            if "invalid_count" in info:
                lines.append(f"- {info['invalid_count']}/{info['checked']} products with invalid numeric fields")
            if info.get("examples"):
                lines.append(f"- Examples: {', '.join(str(e)[:80] for e in info['examples'][:3])}")
            lines.append("")

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


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate scraper output quality")
    parser.add_argument("config", type=Path, help="Path to eval_config.json")
    parser.add_argument("--collect", action="store_true",
                        help="Run scraper to collect sufficient sample before scoring")
    parser.add_argument("--no-history", action="store_true",
                        help="Write eval_result.json but skip eval_history.json and baseline updates (for remediation re-runs)")
    args = parser.parse_args()

    config = load_config(args.config)
    project_root = find_project_root(args.config)
    slug = config["company_slug"]

    # Resolve paths — eval writes its own products under eval-generator output
    scraper_dir = project_root / "docs" / "scraper-generator" / slug
    eval_output_dir = args.config.resolve().parent / "output"
    eval_products = eval_output_dir / "products.jsonl"
    eval_summary_path = eval_output_dir / "summary.json"
    eval_log_path = eval_output_dir / "debug.log"
    eval_result_path = eval_output_dir / "eval_result.json"
    eval_history_path = eval_output_dir / "eval_history.json"
    baseline_path = eval_output_dir / "baseline.json"
    eval_output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    products = load_jsonl(eval_products)
    summary = load_json(eval_summary_path) or {}
    history = load_json(eval_history_path) or []
    if not isinstance(history, list):
        history = []
    is_limited = summary.get("limited", False)

    # --collect: run scraper to collect per-subcategory sample
    if args.collect:
        sample = eval_sample_size(config)
        needed = sample["total"]
        scraper_path = scraper_dir / "scraper.py"
        if not scraper_path.exists():
            print(f"Warning: scraper not found at {scraper_path}", file=sys.stderr)
        else:
            per_sub = sample["per_subcategory"]
            scraper_config_path = scraper_dir / "config.json"
            scraper_config = load_scraper_config(scraper_config_path)
            category_key_map = build_category_key_map(scraper_config) if scraper_config else {}

            if len(per_sub) > 1 and category_key_map:
                # Multi-subcategory: collect per-subcategory
                # Clear existing products file
                if eval_products.exists():
                    eval_products.unlink()
                print(f"Collecting products per subcategory ({len(per_sub)} subcategories)...", file=sys.stderr)
                for sub_id, sub_limit in per_sub.items():
                    keys = category_key_map.get(sub_id, [])
                    if not keys:
                        print(f"  Warning: no category keys for {sub_id}, skipping", file=sys.stderr)
                        continue
                    categories_arg = ",".join(keys)
                    print(f"  {sub_id}: collecting {sub_limit} products (keys: {categories_arg})", file=sys.stderr)
                    try:
                        proc = subprocess.run(
                            [
                                "uv", "run", str(scraper_path),
                                "--categories", categories_arg,
                                "--limit", str(sub_limit),
                                "--output-file", str(eval_products),
                                "--summary-file", str(eval_summary_path),
                                "--log-file", str(eval_log_path),
                                "--append",
                            ],
                            cwd=project_root,
                            timeout=min(max(300, sub_limit * 10), 3600),
                            check=False,
                        )
                        if proc.returncode != 0:
                            print(f"  Warning: scraper exited with code {proc.returncode} for {sub_id}", file=sys.stderr)
                    except subprocess.TimeoutExpired:
                        print(f"  Warning: scraper timed out for {sub_id}", file=sys.stderr)
            else:
                # Single-subcategory or no config: collect with flat --limit
                print(f"Collecting {needed} products...", file=sys.stderr)
                try:
                    proc = subprocess.run(
                        [
                            "uv", "run", str(scraper_path),
                            "--limit", str(needed),
                            "--output-file", str(eval_products),
                            "--summary-file", str(eval_summary_path),
                            "--log-file", str(eval_log_path),
                        ],
                        cwd=project_root,
                        timeout=min(max(300, needed * 10), 3600),
                        check=False,
                    )
                    if proc.returncode != 0:
                        print(f"Warning: scraper exited with code {proc.returncode}", file=sys.stderr)
                except subprocess.TimeoutExpired:
                    print(f"Warning: scraper timed out after {min(max(300, needed * 10), 3600)}s", file=sys.stderr)

            # Reload data
            products = load_jsonl(eval_products)
            summary = load_json(eval_summary_path) or {}
            # When --collect is used, we intentionally sample, so mark as limited
            is_limited = True

    if not products:
        print("Warning: No products found in scraper output.", file=sys.stderr)

    # Inject is_limited into summary for compute_results
    summary["limited"] = is_limited

    # Baseline
    if args.no_history:
        baseline = load_json(baseline_path) if baseline_path.exists() else None
    else:
        baseline = maybe_create_baseline(products, config, is_limited, baseline_path)

    # Run checks
    result = compute_results(products, config, summary, history, baseline)

    # Write JSON result to file
    eval_result_path.write_text(json.dumps(result, indent=2))

    # Append to history (skip when --no-history is set, e.g. remediation re-runs)
    if not args.no_history:
        history_entry = {
            "status": result["status"],
            "degradation_score": result["degradation_score"],
            "products_found": result["products_found"],
            "limited": is_limited,
            "timestamp": result["timestamp"],
        }
        history.append(history_entry)
        eval_history_path.write_text(json.dumps(history, indent=2))

    # Text summary to stdout
    print(format_text_summary(result, config))

    # Markdown report to file
    report_path = eval_output_dir / "eval_report.md"
    report_path.write_text(format_markdown_report(result, config, products))


if __name__ == "__main__":
    main()
