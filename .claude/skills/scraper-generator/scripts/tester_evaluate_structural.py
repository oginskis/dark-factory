# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Structural validation rules S01-S09 for scraper output.

Agent: tester sub-agent (references/tester.md)

Reads all products_{n}_*.jsonl and summary_{n}_*.json files for the iteration,
merges them, then evaluates structural rules.

Usage:
    uv run tester_evaluate_structural.py \
        --output-dir docs/scraper-generator/acme/output \
        --iteration 1 --exit-code 0

    uv run tester_evaluate_structural.py \
        --output-dir docs/scraper-generator/acme/output \
        --iteration 1 --exit-code 0 --skip-s06
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


def per_cat_rate(products: list[dict], pred) -> dict[str, float]:
    cats: dict[str, list[dict]] = {}
    for p in products:
        cats.setdefault(top_category(p), []).append(p)
    return {c: round(sum(1 for p in ps if pred(p)) / len(ps), 4) for c, ps in cats.items()}


def issue(rule_id: str, detail: str, failing: list[dict]) -> dict:
    return {
        "rule_id": rule_id,
        "detail": detail,
        "affected_categories": list({top_category(p) for p in failing[:20]}),
        "sample_urls": [p.get("url", "") for p in failing[:10] if p.get("url")],
    }


# ---------------------------------------------------------------------------
# Rules S01-S09
# ---------------------------------------------------------------------------

def s01(products: list[dict]) -> tuple[dict, dict | None]:
    def has(p):
        ca = p.get("core_attributes")
        return bool(ca and any(v is not None for v in ca.values()))
    if not products:
        return {"id": "S01", "status": "fail", "value": 0, "threshold": 0.30, "per_category": {}}, None
    rate = sum(1 for p in products if has(p)) / len(products)
    pc = per_cat_rate(products, has)
    st = "pass" if rate >= 0.30 else "fail"
    iss = issue("S01", f"Core fill {rate:.0%} < 30%", [p for p in products if not has(p)]) if st == "fail" else None
    return {"id": "S01", "status": st, "value": round(rate, 4), "threshold": 0.30, "per_category": pc}, iss


def s02(products: list[dict]) -> tuple[dict, dict | None]:
    def has(p):
        ea = p.get("extended_attributes")
        return bool(ea and any(v is not None for v in ea.values()))
    if not products:
        return {"id": "S02", "status": "warn", "value": 0, "threshold": 0.20}, None
    rate = sum(1 for p in products if has(p)) / len(products)
    st = "pass" if rate >= 0.20 else "warn"
    iss = issue("S02", f"Extended fill {rate:.0%} < 20%", [p for p in products if not has(p)]) if st == "warn" else None
    return {"id": "S02", "status": st, "value": round(rate, 4), "threshold": 0.20}, iss


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
    parser = argparse.ArgumentParser(description="Structural validation rules S01-S09")
    parser.add_argument("--output-dir", required=True,
                        help="Directory containing versioned output files")
    parser.add_argument("--iteration", required=True, type=int,
                        help="Iteration number to evaluate")
    parser.add_argument("--exit-code", type=int, default=0, help="Scraper exit code")
    parser.add_argument("--skip-s06", action="store_true",
                        help="Skip category diversity (retest mode)")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    products = load_products_for_iteration(output_dir, args.iteration)
    merged_summary = load_merged_summary(output_dir, args.iteration)

    results, issues = [], []
    for fn in [s01, s02, s03, s04, s05]:
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
