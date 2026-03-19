# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Compare scraper output against a baseline to detect regressions.

Agent: tester sub-agent (references/tester.md)

Used by the tester during retest mode. Matches products by URL,
compares key fields (sku, price, core_attributes population).

Usage:
    uv run tester_compare_baseline.py --baseline output/baseline_products.jsonl --retest output/products.jsonl
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REGRESSION_FIELDS = ["sku", "price", "brand", "product_category"]


def load_jsonl(path: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts, skip malformed lines."""
    products = []
    if not path.exists():
        return products
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                products.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return products


def _top_category(p: dict) -> str:
    """First segment of category_path."""
    cp = p.get("category_path") or ""
    return cp.split(" > ")[0] if cp else "unknown"


def compare_products(
    baseline: list[dict],
    retest: list[dict],
    retest_categories: list[str] | None = None,
) -> dict:
    """Compare retest products against baseline, report regressions.

    Only compares products present in BOTH sets (matched by URL).
    Products in baseline but not in retest are ignored (retest is scoped).

    When retest_categories is provided, also checks for category-level dropouts:
    categories that had products in baseline but zero in retest.
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

    # Category-level dropout detection
    category_dropouts: list[dict] = []
    if retest_categories:
        baseline_cats: dict[str, int] = {}
        for p in baseline:
            cat = _top_category(p)
            baseline_cats[cat] = baseline_cats.get(cat, 0) + 1

        retest_cats: dict[str, int] = {}
        for p in retest:
            cat = _top_category(p)
            retest_cats[cat] = retest_cats.get(cat, 0) + 1

        for cat_prefix in retest_categories:
            # Match URL path prefixes to category_path display names.
            # Limitation: uses last URL segment as heuristic (e.g., "/shop/timber"
            # matches categories starting with "timber"). May fail for non-English
            # sites where URL slugs don't match display names.
            for bcat, bcount in baseline_cats.items():
                if bcat.lower().startswith(cat_prefix.strip("/").split("/")[-1].lower()) or cat_prefix in str(bcat):
                    if bcount > 0 and retest_cats.get(bcat, 0) == 0:
                        category_dropouts.append({
                            "category": bcat,
                            "baseline_count": bcount,
                            "retest_count": 0,
                            "prefix": cat_prefix,
                        })

    has_issues = bool(regressions) or bool(category_dropouts)
    return {
        "status": "fail" if has_issues else "pass",
        "products_compared": len([p for p in retest if p.get("url") in baseline_by_url]),
        "regressions": regressions,
        "category_dropouts": category_dropouts,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Compare scraper output against baseline")
    parser.add_argument("--baseline", required=True, help="Path to baseline JSONL")
    parser.add_argument("--retest", required=True, help="Path to retest JSONL")
    parser.add_argument("--retest-categories", help="Comma-separated category prefixes that were retested (for dropout detection)")
    parser.add_argument("--output-dir", help="Directory for versioned result file")
    parser.add_argument("--iteration", type=int, help="Iteration number for result file naming")
    args = parser.parse_args()

    baseline = load_jsonl(Path(args.baseline))
    retest = load_jsonl(Path(args.retest))
    retest_cats = [c.strip() for c in args.retest_categories.split(",") if c.strip()] if args.retest_categories else None
    result = compare_products(baseline, retest, retest_categories=retest_cats)

    output_json = json.dumps(result, indent=2)

    # Write to versioned file if output-dir provided
    if args.output_dir and args.iteration is not None:
        import os
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        h = os.urandom(2).hex()
        result_file = output_dir / f"regression_{args.iteration}_{h}.json"
        result_file.write_text(output_json)

    print(output_json)


if __name__ == "__main__":
    main()
