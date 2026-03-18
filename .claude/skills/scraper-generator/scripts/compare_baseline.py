# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Compare scraper output against a baseline to detect regressions.

Used by the tester during retest mode. Matches products by URL,
compares key fields (sku, price, core_attributes population).

Usage:
    python compare_baseline.py --baseline output/baseline_products.jsonl --retest output/products.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REGRESSION_FIELDS = ["sku", "price", "brand", "product_category"]


def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    products = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            products.append(json.loads(line))
    return products


def compare_products(baseline: list[dict], retest: list[dict]) -> dict:
    """Compare retest products against baseline, report regressions.

    Only compares products present in BOTH sets (matched by URL).
    Products in baseline but not in retest are ignored (retest is scoped).
    """
    baseline_by_url = {p["url"]: p for p in baseline if "url" in p}
    regressions = []

    for product in retest:
        url = product.get("url")
        if not url or url not in baseline_by_url:
            continue

        base = baseline_by_url[url]

        for field in REGRESSION_FIELDS:
            base_val = base.get(field)
            new_val = product.get(field)
            if base_val is not None and new_val is None:
                regressions.append({
                    "url": url,
                    "field": field,
                    "baseline_value": base_val,
                    "retest_value": new_val,
                })

        base_core = base.get("core_attributes", {})
        new_core = product.get("core_attributes", {})
        if len(base_core) > 0 and len(new_core) == 0:
            regressions.append({
                "url": url,
                "field": "core_attributes",
                "baseline_value": f"{len(base_core)} attributes",
                "retest_value": "empty",
            })

    return {
        "status": "fail" if regressions else "pass",
        "products_compared": len([p for p in retest if p.get("url") in baseline_by_url]),
        "regressions": regressions,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare scraper output against baseline")
    parser.add_argument("--baseline", required=True, help="Path to baseline JSONL")
    parser.add_argument("--retest", required=True, help="Path to retest JSONL")
    args = parser.parse_args()

    baseline = load_jsonl(Path(args.baseline))
    retest = load_jsonl(Path(args.retest))
    result = compare_products(baseline, retest)

    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
