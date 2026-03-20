# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_evaluate_structural.py — structural validation with schema-aware key coverage."""
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


ROUTING_TABLES = {
    "subcategory_schemas": {
        "wood.softwood_hardwood_lumber": {
            "core_attribute_keys": ["wood_type", "treatment_type", "structural_grade", "appearance_grade"],
            "extended_attribute_keys": ["species", "nominal_thickness", "nominal_width", "length"],
            "attribute_types": {
                "wood_type": "str", "treatment_type": "str",
                "structural_grade": "str", "appearance_grade": "str",
                "species": "str", "nominal_thickness": "number",
                "nominal_width": "number", "length": "number",
            },
            "units": {"nominal_thickness": "mm", "nominal_width": "mm", "length": "m"},
        }
    }
}

VALID_PRODUCT = make_product()
EMPTY_CORE = make_product(core_attributes={})
NO_BRAND = make_product(brand=None)
BRAND_IN_CORE = make_product(core_attributes={"brand": "Oops", "wood_type": "Oak"})


class TestS01:
    """S01: ≥75% of core_attribute_keys from routing table appear in at least one product."""

    def test_pass_all_keys_present(self):
        """All 4 core keys present → 100% coverage → pass."""
        p = make_product(core_attributes={
            "wood_type": "Softwood", "treatment_type": "Untreated",
            "structural_grade": "C24", "appearance_grade": "A",
        })
        r, _ = es.s01([p], ROUTING_TABLES)
        assert r["status"] == "pass"
        assert r["value"] == 1.0

    def test_pass_at_75_percent(self):
        """3 of 4 core keys present → 75% → pass."""
        p = make_product(core_attributes={
            "wood_type": "Softwood", "treatment_type": "Untreated",
            "structural_grade": "C24",
        })
        r, _ = es.s01([p], ROUTING_TABLES)
        assert r["status"] == "pass"
        assert r["value"] == 0.75

    def test_fail_below_75_percent(self):
        """2 of 4 core keys → 50% < 75% → fail."""
        p = make_product(core_attributes={
            "wood_type": "Softwood", "treatment_type": "Untreated",
        })
        r, iss = es.s01([p], ROUTING_TABLES)
        assert r["status"] == "fail"
        assert r["value"] == 0.5
        assert iss is not None
        assert "structural_grade" in str(iss["detail"])

    def test_fail_empty_core(self):
        """No core keys → 0% → fail."""
        r, iss = es.s01([EMPTY_CORE], ROUTING_TABLES)
        assert r["status"] == "fail"
        assert r["value"] == 0

    def test_fail_no_products(self):
        r, iss = es.s01([], ROUTING_TABLES)
        assert r["status"] == "fail"

    def test_fail_no_routing_tables(self):
        r, _ = es.s01([VALID_PRODUCT], {})
        assert r["status"] == "fail"

    def test_keys_found_across_multiple_products(self):
        """Key found in ANY product counts — doesn't need to be in every product."""
        p1 = make_product(core_attributes={"wood_type": "Softwood", "treatment_type": "Untreated"})
        p2 = make_product(core_attributes={"structural_grade": "C24", "appearance_grade": "A"})
        r, _ = es.s01([p1, p2], ROUTING_TABLES)
        assert r["status"] == "pass"
        assert r["value"] == 1.0

    def test_null_values_not_counted(self):
        """Keys with None values don't count as found."""
        p = make_product(core_attributes={
            "wood_type": "Softwood", "treatment_type": None,
            "structural_grade": None, "appearance_grade": None,
        })
        r, _ = es.s01([p], ROUTING_TABLES)
        assert r["status"] == "fail"
        assert r["value"] == 0.25

    def test_per_category_breakdown(self):
        """Per-subcategory coverage is reported."""
        p = make_product(core_attributes={"wood_type": "Softwood", "treatment_type": "Untreated"})
        r, _ = es.s01([p], ROUTING_TABLES)
        assert "wood.softwood_hardwood_lumber" in r["per_category"]
        subcat = r["per_category"]["wood.softwood_hardwood_lumber"]
        assert subcat["value"] == 0.5
        assert subcat["status"] == "fail"

    def test_no_products_for_subcategory(self):
        """Subcategory in routing tables but no products with that product_category."""
        p = make_product(product_category="other.category",
                         core_attributes={"wood_type": "X"})
        r, _ = es.s01([p], ROUTING_TABLES)
        assert r["status"] == "fail"
        subcat = r["per_category"]["wood.softwood_hardwood_lumber"]
        assert subcat["value"] == 0

    def test_empty_core_keys_passes(self):
        """Subcategory with no expected core keys → auto-pass."""
        rt = {"subcategory_schemas": {"cat.empty": {
            "core_attribute_keys": [],
            "extended_attribute_keys": ["x"],
        }}}
        p = make_product(product_category="cat.empty")
        r, _ = es.s01([p], rt)
        assert r["status"] == "pass"


class TestS02:
    """S02: ≥50% of extended_attribute_keys from routing table appear in at least one product."""

    def test_pass_all_keys(self):
        p = make_product(extended_attributes={
            "species": "Redwood", "nominal_thickness": 47,
            "nominal_width": 100, "length": 3.6,
        })
        r, _ = es.s02([p], ROUTING_TABLES)
        assert r["status"] == "pass"
        assert r["value"] == 1.0

    def test_pass_at_50_percent(self):
        """2 of 4 extended keys → 50% → pass."""
        p = make_product(extended_attributes={"species": "Redwood", "nominal_thickness": 47})
        r, _ = es.s02([p], ROUTING_TABLES)
        assert r["status"] == "pass"
        assert r["value"] == 0.5

    def test_fail_below_50_percent(self):
        """1 of 4 extended keys → 25% < 50% → fail."""
        p = make_product(extended_attributes={"species": "Redwood"})
        r, iss = es.s02([p], ROUTING_TABLES)
        assert r["status"] == "fail"
        assert r["value"] == 0.25
        assert iss is not None

    def test_fail_no_products(self):
        r, _ = es.s02([], ROUTING_TABLES)
        assert r["status"] == "fail"

    def test_now_error_severity(self):
        """S02 is error severity — fail status is 'fail' not 'warn'."""
        p = make_product(extended_attributes={})
        r, _ = es.s02([p], ROUTING_TABLES)
        assert r["status"] == "fail"


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


class TestKeyCoverage:
    """Test the _key_coverage helper directly."""

    def test_full_coverage(self):
        products = [{"core_attributes": {"a": 1, "b": 2, "c": 3}}]
        cov, missing = es._key_coverage(products, ["a", "b", "c"], "core_attributes")
        assert cov == 1.0
        assert missing == []

    def test_partial_coverage(self):
        products = [{"core_attributes": {"a": 1}}]
        cov, missing = es._key_coverage(products, ["a", "b", "c"], "core_attributes")
        assert abs(cov - 1 / 3) < 0.01
        assert set(missing) == {"b", "c"}

    def test_none_values_excluded(self):
        products = [{"core_attributes": {"a": 1, "b": None}}]
        cov, missing = es._key_coverage(products, ["a", "b"], "core_attributes")
        assert cov == 0.5
        assert missing == ["b"]

    def test_empty_expected(self):
        cov, missing = es._key_coverage([], [], "core_attributes")
        assert cov == 1.0

    def test_across_products(self):
        products = [
            {"core_attributes": {"a": 1}},
            {"core_attributes": {"b": 2}},
        ]
        cov, missing = es._key_coverage(products, ["a", "b"], "core_attributes")
        assert cov == 1.0


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


class TestMultiSubcategory:
    """S01/S02 with multiple subcategories in routing tables."""

    def test_worst_subcategory_determines_status(self):
        """If one subcategory passes and another fails, overall status is fail."""
        rt = {"subcategory_schemas": {
            "cat.good": {
                "core_attribute_keys": ["a", "b"],
                "extended_attribute_keys": [],
            },
            "cat.bad": {
                "core_attribute_keys": ["x", "y", "z", "w"],
                "extended_attribute_keys": [],
            },
        }}
        products = [
            make_product(product_category="cat.good", core_attributes={"a": 1, "b": 2}),
            make_product(product_category="cat.bad", core_attributes={"x": 1}),  # 1/4 = 25%
        ]
        r, iss = es.s01(products, rt)
        assert r["status"] == "fail"
        assert r["per_category"]["cat.good"]["status"] == "pass"
        assert r["per_category"]["cat.bad"]["status"] == "fail"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
