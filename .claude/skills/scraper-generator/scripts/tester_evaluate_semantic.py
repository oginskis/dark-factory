# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Semantic validation rules M01-M04 for scraper output.

Agent: tester sub-agent (references/tester.md)

Reads all products_{n}_*.jsonl files for the iteration, then evaluates
semantic rules against routing tables.

Usage:
    uv run tester_evaluate_semantic.py \
        --output-dir docs/scraper-generator/acme/output \
        --iteration 1 \
        --routing-tables docs/scraper-generator/acme/generator_input.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

UNIT_PATTERN = re.compile(r"\d+\s*(mm|cm|m|kg|g|lb|oz|ml|l|V|W|A|Hz|kW|MPa)$")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_jsonl(path: Path) -> list[dict]:
    products = []
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                try:
                    products.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
    return products


def load_products_for_iteration(output_dir: Path, iteration: int) -> list[dict]:
    """Glob all products_{n}_*.jsonl files for the iteration and concatenate."""
    products = []
    for f in sorted(output_dir.glob(f"products_{iteration}_*.jsonl")):
        products.extend(load_jsonl(f))
    return products


def load_routing_tables(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    routing = data.get("subcategory_schemas", data)
    types: dict[str, str] = {}
    units: dict[str, str] = {}
    for subcat_data in routing.values():
        if not isinstance(subcat_data, dict):
            continue
        for attr, typ in (subcat_data.get("attribute_types") or {}).items():
            types[attr] = typ
        for attr, unit in (subcat_data.get("units") or {}).items():
            units[attr] = unit
    return types, units


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def top_category(p: dict) -> str:
    cp = p.get("category_path") or ""
    return cp.split(" > ")[0] if cp else "unknown"


def all_attrs(p: dict) -> dict:
    return {
        **(p.get("core_attributes") or {}),
        **(p.get("extended_attributes") or {}),
        **(p.get("extra_attributes") or {}),
    }


def issue(rule_id: str, detail: str, failing: list[dict], *,
          attrs: list[str] | None = None, samples: dict | None = None) -> dict:
    d: dict = {
        "rule_id": rule_id,
        "detail": detail,
        "affected_categories": list({top_category(p) for p in failing[:20]}),
        "sample_urls": [p.get("url", "") for p in failing[:10] if p.get("url")],
    }
    if attrs:
        d["affected_attributes"] = attrs
    if samples:
        d["sample_values"] = {k: v[:10] for k, v in samples.items()}
    return d


# ---------------------------------------------------------------------------
# Rules M01-M04
# ---------------------------------------------------------------------------

def m01(products: list[dict], types: dict, units: dict) -> tuple[dict, dict | None]:
    failing, attrs, svals = [], set(), {}
    for p in products:
        for a, v in all_attrs(p).items():
            if types.get(a) == "number" and a in units and isinstance(v, str):
                attrs.add(a)
                svals.setdefault(a, []).append(v)
                if p not in failing:
                    failing.append(p)
    st = "fail" if failing else "pass"
    r = len(failing) / len(products) if products else 0
    iss = issue("M01", f"{len(failing)} products: string values for number+unit attrs",
                failing, attrs=sorted(attrs), samples=svals) if failing else None
    return {"id": "M01", "status": st, "value": round(r, 4)}, iss


def m02(products: list[dict], types: dict) -> tuple[dict, dict | None]:
    failing, attrs, svals = [], set(), {}
    for p in products:
        for a, v in all_attrs(p).items():
            if types.get(a) == "number" and isinstance(v, str):
                attrs.add(a)
                svals.setdefault(a, []).append(v)
                if p not in failing:
                    failing.append(p)
    st = "warn" if failing else "pass"
    r = len(failing) / len(products) if products else 0
    iss = issue("M02", f"{len(failing)} products: string values for number-typed attrs",
                failing, attrs=sorted(attrs), samples=svals) if failing else None
    return {"id": "M02", "status": st, "value": round(r, 4)}, iss


def m03(products: list[dict], units: dict) -> tuple[dict, dict | None]:
    missing, attrs, failing = 0, set(), []
    for p in products:
        pu = p.get("attribute_units") or {}
        for a in all_attrs(p):
            if a in units and a not in pu:
                missing += 1
                attrs.add(a)
                if p not in failing:
                    failing.append(p)
    st = "warn" if missing else "pass"
    iss = issue("M03", f"{missing} missing attribute_units entries",
                failing, attrs=sorted(attrs)) if failing else None
    return {"id": "M03", "status": st, "value": missing}, iss


def m04(products: list[dict], types: dict, units: dict) -> tuple[dict, dict | None]:
    failing, attrs, svals = [], set(), {}
    for p in products:
        for a, v in all_attrs(p).items():
            if not isinstance(v, str):
                continue
            if types.get(a) != "number" and a not in units:
                continue
            if UNIT_PATTERN.search(v):
                attrs.add(a)
                svals.setdefault(a, []).append(v)
                if p not in failing:
                    failing.append(p)
    st = "fail" if failing else "pass"
    r = len(failing) / len(products) if products else 0
    iss = issue("M04", f"{len(failing)} products: value/unit concatenation",
                failing, attrs=sorted(attrs), samples=svals) if failing else None
    return {"id": "M04", "status": st, "value": round(r, 4)}, iss


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Semantic validation rules M01-M04")
    parser.add_argument("--output-dir", required=True,
                        help="Directory containing versioned output files")
    parser.add_argument("--iteration", required=True, type=int,
                        help="Iteration number to evaluate")
    parser.add_argument("--routing-tables", required=True,
                        help="Path to generator_input.json")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    products = load_products_for_iteration(output_dir, args.iteration)
    types, units = load_routing_tables(Path(args.routing_tables))

    results, issues = [], []
    for fn in [
        lambda p: m01(p, types, units),
        lambda p: m02(p, types),
        lambda p: m03(p, units),
        lambda p: m04(p, types, units),
    ]:
        r, i = fn(products)
        results.append(r)
        if i:
            issues.append(i)

    print(json.dumps({
        "rule_results": results,
        "issues": issues,
        "products_count": len(products),
        "types_count": len(types),
        "units_count": len(units),
    }, indent=2))


if __name__ == "__main__":
    main()
