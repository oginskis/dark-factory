# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_evaluate_structural.py — S01-S09 with glob-based file loading."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_evaluate_structural as es


def make_product(**overrides) -> dict:
    base = {
        "sku": "SKU-001", "name": "Test Product", "url": "https://example.com/p1",
        "price": 9.99, "currency": "GBP", "brand": "TestBrand",
        "product_category": "wood.softwood_hardwood_lumber",
        "scraped_at": "2026-03-18T00:00:00Z",
        "category_path": "Timber > Softwood > PAR",
        "core_attributes": {"wood_type": "Softwood", "treatment_type": "Untreated"},
        "extended_attributes": {"species": "Redwood"},
        "extra_attributes": {},
        "attribute_units": {},
    }
    base.update(overrides)
    return base


VALID_PRODUCT = make_product()
EMPTY_CORE = make_product(core_attributes={})
NO_BRAND = make_product(brand=None)
BRAND_IN_CORE = make_product(core_attributes={"brand": "Oops", "wood_type": "Oak"})


class TestS01:
    def test_pass(self):
        r, _ = es.s01([VALID_PRODUCT] * 5)
        assert r["status"] == "pass"

    def test_fail(self):
        r, _ = es.s01([EMPTY_CORE] * 5)
        assert r["status"] == "fail"

    def test_threshold(self):
        r, _ = es.s01([VALID_PRODUCT] * 3 + [EMPTY_CORE] * 7)
        assert r["status"] == "pass"

    def test_per_category(self):
        p1 = make_product(category_path="Timber > Softwood")
        p2 = make_product(category_path="Fencing > Panels", core_attributes={})
        r, _ = es.s01([p1, p2])
        assert "Timber" in r["per_category"]


class TestS03:
    def test_pass(self):
        r, _ = es.s03([VALID_PRODUCT])
        assert r["status"] == "pass"

    def test_missing_sku(self):
        r, i = es.s03([make_product(sku=None)])
        assert r["status"] == "fail"
        assert "sku" in i["detail"]

    def test_null_price_ok(self):
        r, _ = es.s03([make_product(price=None)])
        assert r["status"] == "pass"


class TestS04:
    @patch("tester_evaluate_structural.load_taxonomy_ids")
    def test_valid(self, mock_ids):
        mock_ids.return_value = {"wood.softwood_hardwood_lumber"}
        r, _ = es.s04([VALID_PRODUCT])
        assert r["status"] == "pass"

    @patch("tester_evaluate_structural.load_taxonomy_ids")
    def test_invalid(self, mock_ids):
        mock_ids.return_value = {"wood.plywood_engineered_panels"}
        r, _ = es.s04([VALID_PRODUCT])
        assert r["status"] == "fail"


class TestS05:
    def test_pass(self):
        r, _ = es.s05([VALID_PRODUCT])
        assert r["status"] == "pass"

    def test_missing(self):
        r, _ = es.s05([NO_BRAND])
        assert r["status"] == "fail"

    def test_in_core(self):
        r, _ = es.s05([BRAND_IN_CORE])
        assert r["status"] == "fail"


class TestS06:
    def test_pass(self):
        r, _ = es.s06([make_product(category_path="A > x"), make_product(category_path="B > y")])
        assert r["status"] == "pass"

    def test_warn(self):
        r, _ = es.s06([VALID_PRODUCT, VALID_PRODUCT])
        assert r["status"] == "warn"

    def test_skip(self):
        r, _ = es.s06([VALID_PRODUCT], skip=True)
        assert r["status"] == "skip"


class TestS07:
    def test_pass(self):
        r, _ = es.s07({"errors_count": 0})
        assert r["status"] == "pass"

    def test_fail(self):
        r, i = es.s07({"errors_count": 3})
        assert r["status"] == "fail"
        assert "3" in i["detail"]

    def test_empty_summary_fails(self):
        r, _ = es.s07({})
        assert r["status"] == "fail"  # no summary = can't verify


class TestS08:
    def test_pass(self):
        r, _ = es.s08(0)
        assert r["status"] == "pass"

    def test_fail(self):
        r, _ = es.s08(1)
        assert r["status"] == "fail"

    def test_timeout(self):
        r, i = es.s08(-1)
        assert "timed out" in i["detail"].lower()


class TestS09:
    def test_pass(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text('{"sku":"1"}\n')
        r, _ = es.s09(tmp_path, 1)
        assert r["status"] == "pass"

    def test_missing(self, tmp_path):
        r, i = es.s09(tmp_path, 1)
        assert r["status"] == "fail"
        assert "No products" in i["detail"]

    def test_empty(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text("")
        r, i = es.s09(tmp_path, 1)
        assert r["status"] == "fail"


class TestGlobLoading:
    """Evaluator globs products_{n}_*.jsonl and merges across files."""

    def test_loads_multiple_products_files(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text(json.dumps(make_product(sku="A")) + "\n")
        (tmp_path / "products_1_bbbb.jsonl").write_text(json.dumps(make_product(sku="B")) + "\n")
        products = es.load_products_for_iteration(tmp_path, 1)
        assert len(products) == 2
        assert {p["sku"] for p in products} == {"A", "B"}

    def test_merges_summaries(self, tmp_path):
        (tmp_path / "summary_1_aaaa.json").write_text(json.dumps({"errors_count": 1, "total_products": 10}))
        (tmp_path / "summary_1_bbbb.json").write_text(json.dumps({"errors_count": 2, "total_products": 5}))
        merged = es.load_merged_summary(tmp_path, 1)
        assert merged["errors_count"] == 3
        assert merged["total_products"] == 15

    def test_ignores_other_iterations(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text(json.dumps(make_product(sku="A")) + "\n")
        (tmp_path / "products_2_bbbb.jsonl").write_text(json.dumps(make_product(sku="B")) + "\n")
        products = es.load_products_for_iteration(tmp_path, 1)
        assert len(products) == 1
        assert products[0]["sku"] == "A"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
