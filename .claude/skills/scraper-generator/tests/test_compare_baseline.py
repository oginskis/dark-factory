# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for compare_baseline.py — JSONL regression detection."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from compare_baseline import compare_products, load_jsonl


class TestLoadJsonl:
    def test_loads_valid_jsonl(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text('{"sku": "A", "url": "https://x.com/a"}\n{"sku": "B", "url": "https://x.com/b"}\n')
        products = load_jsonl(f)
        assert len(products) == 2
        assert products[0]["sku"] == "A"

    def test_empty_file(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text("")
        products = load_jsonl(f)
        assert products == []

    def test_skips_blank_lines(self, tmp_path):
        f = tmp_path / "products.jsonl"
        f.write_text('{"sku": "A"}\n\n{"sku": "B"}\n')
        products = load_jsonl(f)
        assert len(products) == 2


class TestCompareProducts:
    def test_no_regressions(self):
        baseline = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}},
        ]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}},
        ]
        result = compare_products(baseline, retest)
        assert result["regressions"] == []
        assert result["status"] == "pass"

    def test_price_changed(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [{"url": "https://x.com/a", "sku": "A", "price": None, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1
        assert result["regressions"][0]["field"] == "price"
        assert result["status"] == "fail"

    def test_core_attributes_disappeared(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {"weight": 5}}]
        retest = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1
        assert result["regressions"][0]["field"] == "core_attributes"

    def test_sku_disappeared(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [{"url": "https://x.com/a", "sku": None, "price": 10.0, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert len(result["regressions"]) == 1

    def test_product_missing_from_retest_not_regression(self):
        baseline = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
            {"url": "https://x.com/b", "sku": "B", "price": 20.0, "core_attributes": {}},
        ]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
        ]
        result = compare_products(baseline, retest)
        assert result["status"] == "pass"

    def test_unmatched_retest_product_ignored(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}}]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
            {"url": "https://x.com/new", "sku": "NEW", "price": 5.0, "core_attributes": {}},
        ]
        result = compare_products(baseline, retest)
        assert result["status"] == "pass"

    def test_products_compared_count(self):
        baseline = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
            {"url": "https://x.com/b", "sku": "B", "price": 20.0, "core_attributes": {}},
        ]
        retest = [
            {"url": "https://x.com/a", "sku": "A", "price": 10.0, "core_attributes": {}},
        ]
        result = compare_products(baseline, retest)
        assert result["products_compared"] == 1

    def test_multiple_regressions_on_same_product(self):
        baseline = [{"url": "https://x.com/a", "sku": "A", "price": 10.0, "brand": "Acme", "core_attributes": {"w": 5}}]
        retest = [{"url": "https://x.com/a", "sku": None, "price": None, "brand": None, "core_attributes": {}}]
        result = compare_products(baseline, retest)
        assert result["status"] == "fail"
        fields = {r["field"] for r in result["regressions"]}
        assert "sku" in fields
        assert "price" in fields
        assert "brand" in fields
        assert "core_attributes" in fields


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
