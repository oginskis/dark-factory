# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Structural validation for scraper output (attribute coverage, mandatory fields, execution).
See references/acceptance-criteria.md for the authoritative list of criteria and thresholds.

Agent: tester sub-agent (references/tester.md)

Reads all products_{n}_*.jsonl and summary_{n}_*.json files for the iteration,
merges them, then evaluates structural rules.

Usage:
    uv run tester_evaluate_structural.py \
        --output-dir docs/scraper-generator/acme/output \
        --iteration 1 --exit-code 0 \
        --routing-tables docs/scraper-generator/acme/generator_input.json

    uv run tester_evaluate_structural.py \
        --output-dir docs/scraper-generator/acme/output \
        --iteration 1 --exit-code 0 --skip-s06 \
        --routing-tables docs/scraper-generator/acme/generator_input.json
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path


def _find_repo_root() -> Path:
    path = Path(__file__).resolve().parent
    for _ in range(10):
        if (path / ".claude" / "skills").is_dir():
            return path
        path = path.parent
    raise RuntimeError("Cannot find repo root")


TAXONOMY_PATH = _find_repo_root() / "docs" / "product-taxonomy" / "categories.md"


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


def load_products_for_iteration(output_dir: Path, iteration: int) -> list[dict]:
    """Glob all products_{n}_*.jsonl files for the iteration and concatenate."""
    products = []
    for f in sorted(output_dir.glob(f"products_{iteration}_*.jsonl")):
        products.extend(load_jsonl(f))
    return products


def load_merged_summary(output_dir: Path, iteration: int) -> dict:
    """Glob all summary_{n}_*.json files for the iteration and merge."""
    merged: dict = {}
    for f in sorted(output_dir.glob(f"summary_{iteration}_*.json")):
        try:
            s = json.loads(f.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            continue
        if not merged:
            merged = s
        else:
            merged["total_products"] = merged.get("total_products", 0) + s.get("total_products", 0)
            merged["batches_written"] = merged.get("batches_written", 0) + s.get("batches_written", 0)
            merged["duration_seconds"] = round(
                merged.get("duration_seconds", 0) + s.get("duration_seconds", 0), 1)
            merged["errors_count"] = merged.get("errors_count", 0) + s.get("errors_count", 0)
            merged["limited"] = merged.get("limited", False) or s.get("limited", False)
            merged["timestamp"] = max(merged.get("timestamp", ""), s.get("timestamp", ""))
    return merged


def load_routing_tables(path: Path) -> dict:
    """Load generator_input.json routing tables."""
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {}


def load_taxonomy_ids() -> set[str]:
    ids: set[str] = set()
    if not TAXONOMY_PATH.exists():
        return ids
    pattern = re.compile(r"^- .+ `([a-z][a-z0-9_.]+)`$")
    for line in TAXONOMY_PATH.read_text(encoding="utf-8").splitlines():
        m = pattern.match(line.strip())
        if m:
            ids.add(m.group(1))
    return ids


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def top_category(p: dict) -> str:
    cp = p.get("category_path") or ""
    return cp.split(" > ")[0] if cp else "unknown"


def issue(rule_id: str, detail: str, failing: list[dict]) -> dict:
    return {
        "rule_id": rule_id,
        "detail": detail,
        "affected_categories": list({top_category(p) for p in failing[:20]}),
        "sample_urls": [p.get("url", "") for p in failing[:10] if p.get("url")],
    }


def _group_by_subcategory(products: list[dict]) -> dict[str, list[dict]]:
    """Group products by their product_category (taxonomy ID)."""
    by_subcat: dict[str, list[dict]] = {}
    for p in products:
        cat = p.get("product_category", "_unclassified")
        by_subcat.setdefault(cat, []).append(p)
    return by_subcat


def _key_coverage(products: list[dict], expected_keys: list[str], bucket: str) -> tuple[float, list[str]]:
    """Compute what fraction of expected_keys appear non-null in at least one product.

    Returns (coverage_ratio, missing_keys).
    """
    if not expected_keys:
        return 1.0, []
    found = set()
    for p in products:
        attrs = p.get(bucket) or {}
        for k, v in attrs.items():
            if v is not None:
                found.add(k)
    expected_set = set(expected_keys)
    matched = found & expected_set
    missing = [k for k in expected_keys if k not in matched]
    return len(matched) / len(expected_keys), missing


# ---------------------------------------------------------------------------
# Structural rules — see references/acceptance-criteria.md
# ---------------------------------------------------------------------------

def s01(products: list[dict], routing_tables: dict) -> tuple[dict, dict | None]:
    """S01: ≥75% of core_attribute_keys appear (non-null) in at least one product, per subcategory."""
    schemas = routing_tables.get("subcategory_schemas", {})
    if not products or not schemas:
        return {"id": "S01", "status": "fail", "value": 0, "threshold": 0.75, "per_category": {}}, \
            {"rule_id": "S01", "detail": "No products or no routing tables", "affected_categories": [], "sample_urls": []}

    by_subcat = _group_by_subcategory(products)
    per_category = {}
    worst = 1.0
    all_missing: dict[str, list[str]] = {}

    for subcat_id, schema in schemas.items():
        expected = schema.get("core_attribute_keys", [])
        if not expected:
            per_category[subcat_id] = {"value": 1.0, "threshold": 0.75, "status": "pass"}
            continue
        subcat_products = by_subcat.get(subcat_id, [])
        if not subcat_products:
            per_category[subcat_id] = {"value": 0, "threshold": 0.75, "status": "fail"}
            worst = 0
            all_missing[subcat_id] = expected
            continue
        cov, missing = _key_coverage(subcat_products, expected, "core_attributes")
        st = "pass" if cov >= 0.75 else "fail"
        per_category[subcat_id] = {"value": round(cov, 4), "threshold": 0.75, "status": st}
        worst = min(worst, cov)
        if missing:
            all_missing[subcat_id] = missing

    overall = "pass" if worst >= 0.75 else "fail"
    iss = None
    if overall == "fail":
        iss = {
            "rule_id": "S01",
            "detail": f"Core key coverage {worst:.0%} < 75%. Missing: {all_missing}",
            "affected_categories": list(all_missing.keys()),
            "sample_urls": [p.get("url", "") for p in products[:5] if p.get("url")],
        }
    return {"id": "S01", "status": overall, "value": round(worst, 4), "threshold": 0.75, "per_category": per_category}, iss


def s02(products: list[dict], routing_tables: dict) -> tuple[dict, dict | None]:
    """S02: ≥50% of extended_attribute_keys appear (non-null) in at least one product, per subcategory."""
    schemas = routing_tables.get("subcategory_schemas", {})
    if not products or not schemas:
        return {"id": "S02", "status": "fail", "value": 0, "threshold": 0.50, "per_category": {}}, \
            {"rule_id": "S02", "detail": "No products or no routing tables", "affected_categories": [], "sample_urls": []}

    by_subcat = _group_by_subcategory(products)
    per_category = {}
    worst = 1.0
    all_missing: dict[str, list[str]] = {}

    for subcat_id, schema in schemas.items():
        expected = schema.get("extended_attribute_keys", [])
        if not expected:
            per_category[subcat_id] = {"value": 1.0, "threshold": 0.50, "status": "pass"}
            continue
        subcat_products = by_subcat.get(subcat_id, [])
        if not subcat_products:
            per_category[subcat_id] = {"value": 0, "threshold": 0.50, "status": "fail"}
            worst = 0
            all_missing[subcat_id] = expected
            continue
        cov, missing = _key_coverage(subcat_products, expected, "extended_attributes")
        st = "pass" if cov >= 0.50 else "fail"
        per_category[subcat_id] = {"value": round(cov, 4), "threshold": 0.50, "status": st}
        worst = min(worst, cov)
        if missing:
            all_missing[subcat_id] = missing

    overall = "pass" if worst >= 0.50 else "fail"
    iss = None
    if overall == "fail":
        iss = {
            "rule_id": "S02",
            "detail": f"Extended key coverage {worst:.0%} < 50%. Missing: {all_missing}",
            "affected_categories": list(all_missing.keys()),
            "sample_urls": [p.get("url", "") for p in products[:5] if p.get("url")],
        }
    return {"id": "S02", "status": overall, "value": round(worst, 4), "threshold": 0.50, "per_category": per_category}, iss


def s03(products: list[dict]) -> tuple[dict, dict | None]:
    required = ["sku", "name", "url", "brand", "product_category", "scraped_at", "category_path"]
    nullable = ["price", "currency"]
    if not products:
        return {"id": "S03", "status": "fail", "value": 0, "threshold": 1.0}, None
    failing = [p for p in products
               if any(f not in p or p[f] is None for f in required)
               or any(f not in p for f in nullable)]
    rate = 1 - len(failing) / len(products)
    st = "pass" if not failing else "fail"
    iss = None
    if failing:
        counts: dict[str, int] = {}
        for p in failing:
            for f in required:
                if f not in p or p[f] is None:
                    counts[f] = counts.get(f, 0) + 1
            for f in nullable:
                if f not in p:
                    counts[f] = counts.get(f, 0) + 1
        iss = issue("S03", "Missing: " + ", ".join(sorted(counts, key=counts.get, reverse=True)), failing)
    return {"id": "S03", "status": st, "value": round(rate, 4), "threshold": 1.0}, iss


def s04(products: list[dict]) -> tuple[dict, dict | None]:
    valid = load_taxonomy_ids()
    if not products:
        return {"id": "S04", "status": "fail", "value": 0, "threshold": 1.0}, None
    failing = [p for p in products if p.get("product_category") not in valid]
    st = "pass" if not failing else "fail"
    iss = issue("S04", f"Invalid IDs: {list({p.get('product_category','?') for p in failing})}", failing) if failing else None
    return {"id": "S04", "status": st, "value": round(1 - len(failing) / len(products), 4), "threshold": 1.0}, iss


def s05(products: list[dict]) -> tuple[dict, dict | None]:
    if not products:
        return {"id": "S05", "status": "fail", "value": 0, "threshold": 1.0}, None
    failing = []
    for p in products:
        if "brand" not in p or p["brand"] is None:
            failing.append(p)
            continue
        if any("brand" in (p.get(b) or {}) for b in ("core_attributes", "extended_attributes", "extra_attributes")):
            failing.append(p)
    st = "pass" if not failing else "fail"
    iss = issue("S05", "brand missing or inside attribute buckets", failing) if failing else None
    return {"id": "S05", "status": st, "value": round(1 - len(failing) / len(products), 4), "threshold": 1.0}, iss


def s06(products: list[dict], skip: bool = False) -> tuple[dict, dict | None]:
    if skip:
        return {"id": "S06", "status": "skip", "value": 0}, None
    cats = {top_category(p) for p in products}
    n = len(cats)
    st = "pass" if n >= 2 else "warn"
    iss = issue("S06", f"Only {n} category: {cats}", products[:3]) if st == "warn" else None
    return {"id": "S06", "status": st, "value": n, "threshold": 2}, iss


def s07(merged_summary: dict) -> tuple[dict, dict | None]:
    """S07: errors_count across all summaries must be 0."""
    if not merged_summary:
        return {"id": "S07", "status": "fail", "value": -1, "threshold": 0}, None
    errors = merged_summary.get("errors_count", 0)
    st = "pass" if errors == 0 else "fail"
    iss = {"rule_id": "S07", "detail": f"{errors} errors", "affected_categories": [], "sample_urls": []} if errors else None
    return {"id": "S07", "status": st, "value": errors, "threshold": 0}, iss


def s08(exit_code: int) -> tuple[dict, dict | None]:
    st = "pass" if exit_code == 0 else "fail"
    iss = None
    if exit_code != 0:
        d = "Scraper timed out" if exit_code == -1 else f"Exit code {exit_code}"
        iss = {"rule_id": "S08", "detail": d, "affected_categories": [], "sample_urls": []}
    return {"id": "S08", "status": st, "value": exit_code}, iss


def s09(output_dir: Path, iteration: int) -> tuple[dict, dict | None]:
    """S09: at least one products file must exist and be non-empty."""
    files = sorted(output_dir.glob(f"products_{iteration}_*.jsonl"))
    if not files:
        return {"id": "S09", "status": "fail", "value": 0}, \
            {"rule_id": "S09", "detail": f"No products_{iteration}_*.jsonl files", "affected_categories": [], "sample_urls": []}
    total_lines = sum(
        len([l for l in f.read_text().splitlines() if l.strip()])
        for f in files
    )
    st = "pass" if total_lines > 0 else "fail"
    iss = {"rule_id": "S09", "detail": "All products files empty", "affected_categories": [], "sample_urls": []} if not total_lines else None
    return {"id": "S09", "status": st, "value": total_lines}, iss


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Structural validation (attribute coverage, mandatory fields, execution)")
    parser.add_argument("--output-dir", required=True,
                        help="Directory containing versioned output files")
    parser.add_argument("--iteration", required=True, type=int,
                        help="Iteration number to evaluate")
    parser.add_argument("--exit-code", type=int, default=0, help="Scraper exit code")
    parser.add_argument("--skip-s06", action="store_true",
                        help="Skip category diversity (retest mode)")
    parser.add_argument("--routing-tables", default=None,
                        help="Path to generator_input.json (required for S01/S02 schema-aware checks)")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    products = load_products_for_iteration(output_dir, args.iteration)
    merged_summary = load_merged_summary(output_dir, args.iteration)
    routing_tables = load_routing_tables(Path(args.routing_tables)) if args.routing_tables else {}

    results, issues = [], []

    # S01/S02 need routing tables for schema-aware key coverage
    r, i = s01(products, routing_tables)
    results.append(r)
    if i:
        issues.append(i)
    r, i = s02(products, routing_tables)
    results.append(r)
    if i:
        issues.append(i)

    for fn in [s03, s04, s05]:
        r, i = fn(products)
        results.append(r)
        if i:
            issues.append(i)
    r, i = s06(products, skip=args.skip_s06)
    results.append(r)
    if i:
        issues.append(i)
    r, i = s07(merged_summary)
    results.append(r)
    if i:
        issues.append(i)
    r, i = s08(args.exit_code)
    results.append(r)
    if i:
        issues.append(i)
    r, i = s09(output_dir, args.iteration)
    results.append(r)
    if i:
        issues.append(i)

    output = {"rule_results": results, "issues": issues, "products_count": len(products)}
    output_json = json.dumps(output, indent=2)

    # Write to versioned file
    h = os.urandom(2).hex()
    result_file = output_dir / f"structural_{args.iteration}_{h}.json"
    result_file.write_text(output_json)

    # Also print to stdout
    print(output_json)


if __name__ == "__main__":
    main()
