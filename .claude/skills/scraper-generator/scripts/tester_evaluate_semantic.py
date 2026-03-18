# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Semantic validation rules M01-M04 for scraper output.

Agent: tester sub-agent (references/tester.md)

Checks attribute values against routing tables (types + units from generator_input.json).
Catches the most common scraper bug: "18mm" instead of value=18 + attribute_units={"attr": "mm"}.

Reads: products.jsonl, generator_input.json
Outputs: JSON to stdout with rule_results and issues arrays.

Usage:
    uv run tester_evaluate_semantic.py --output-dir docs/scraper-generator/acme/output \
        --routing-tables docs/scraper-generator/acme/generator_input.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# Matches values like "18mm", "3.5kg", "220V" — embedded unit in a string
UNIT_PATTERN = re.compile(r"\d+\s*(mm|cm|m|kg|g|lb|oz|ml|l|V|W|A|Hz|kW|MPa)$")


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_jsonl(path: Path) -> list[dict]:
    """Load NDJSON file, skip malformed lines."""
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


def load_routing_tables(path: Path) -> tuple[dict[str, str], dict[str, str]]:
    """Load generator_input.json, return (types, units) flattened across subcategories.

    Input structure: {"subcategory_schemas": {"wood.lumber": {"attribute_types": {...}, "units": {...}}, ...}}
    Output: merged {attr: type} and {attr: unit} dicts across all subcategories.
    """
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
    """First segment of category_path."""
    cp = p.get("category_path") or ""
    return cp.split(" > ")[0] if cp else "unknown"


def all_attrs(p: dict) -> dict:
    """Merge all three attribute buckets into one dict for checking."""
    return {
        **(p.get("core_attributes") or {}),
        **(p.get("extended_attributes") or {}),
        **(p.get("extra_attributes") or {}),
    }


def issue(rule_id: str, detail: str, failing: list[dict], *,
          attrs: list[str] | None = None, samples: dict | None = None) -> dict:
    """Build an issue dict with sample URLs and values for the coder to diagnose."""
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
    """M01: number-typed attrs WITH units must be numeric, not strings (error).

    Checks: for each attribute where types[attr]=="number" AND attr in units,
    the value must be int/float. Catches "18mm" where value should be 18
    and attribute_units should have {"nominal_width": "mm"}.
    """
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
    """M02: ALL number-typed attrs must be int/float, not strings (warning).

    Broader than M01 — catches "3" (should be 3) even for attrs without units.
    """
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
    """M03: attribute_units must contain keys for attrs that have units in routing table (warning).

    If the routing table says nominal_width has unit "mm" and the product has nominal_width
    in any bucket, then attribute_units must contain "nominal_width".
    """
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
    """M04: regex scan for embedded units like '18mm' in number-typed or unit-bearing attrs (error).

    Only checks attrs where routing table type is 'number' OR units dict has an entry.
    Does NOT flag string-typed attrs that happen to contain unit-like suffixes.
    """
    failing, attrs, svals = [], set(), {}
    for p in products:
        for a, v in all_attrs(p).items():
            if not isinstance(v, str):
                continue
            # Only check attrs that should be numeric or have units
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
    parser.add_argument("--output-dir", required=True, help="Scraper output directory")
    parser.add_argument("--routing-tables", required=True, help="Path to generator_input.json")
    parser.add_argument("--iteration", type=int, help="Evaluate products_iteration_{N}.jsonl instead of products.jsonl")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    # Read iteration-specific file if --iteration provided, otherwise latest products.jsonl
    products_file = output_dir / f"products_iteration_{args.iteration}.jsonl" if args.iteration else output_dir / "products.jsonl"
    products = load_jsonl(products_file)
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

    # Output JSON to stdout for the tester sub-agent to consume
    print(json.dumps({
        "rule_results": results,
        "issues": issues,
        "products_count": len(products),
        "types_count": len(types),
        "units_count": len(units),
    }, indent=2))


if __name__ == "__main__":
    main()
