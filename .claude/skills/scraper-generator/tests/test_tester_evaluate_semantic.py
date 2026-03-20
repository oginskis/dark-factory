# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_evaluate_semantic.py — semantic validation with glob-based file loading."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_evaluate_semantic as es

TYPES = {
    "wood_type": "str",
    "nominal_thickness": "number",
    "nominal_width": "number",
    "pack_quantity": "number",
    "species": "str",
}
UNITS = {"nominal_thickness": "mm", "nominal_width": "mm"}


def make_product(**overrides) -> dict:
    base = {
        "sku": "SKU-001", "name": "PAR Timber", "url": "https://example.com/p1",
        "price": 9.99, "currency": "GBP", "brand": "TestBrand",
        "product_category": "wood.softwood_hardwood_lumber",
        "scraped_at": "2026-03-18T00:00:00Z",
        "category_path": "Timber > Softwood > PAR",
        "core_attributes": {"wood_type": "Softwood"},
        "extended_attributes": {
            "nominal_thickness": 18, "nominal_width": 50,
            "pack_quantity": 10, "species": "Redwood",
        },
        "extra_attributes": {},
        "attribute_units": {"nominal_thickness": "mm", "nominal_width": "mm"},
    }
    base.update(overrides)
    return base


BAD_CONCAT = make_product(
    extended_attributes={"nominal_thickness": "18mm", "nominal_width": "50mm",
                         "pack_quantity": 10, "species": "Redwood"},
    attribute_units={},
)
STRING_NUMBERS = make_product(
    extended_attributes={"nominal_thickness": "18", "nominal_width": "50",
                         "pack_quantity": "10", "species": "Redwood"},
    attribute_units={"nominal_thickness": "mm", "nominal_width": "mm"},
)
VALID_PRODUCT = make_product()


class TestM01:
    def test_pass(self):
        r, _ = es.m01([VALID_PRODUCT], TYPES, UNITS)
        assert r["status"] == "pass"

    def test_fail(self):
        r, i = es.m01([BAD_CONCAT], TYPES, UNITS)
        assert r["status"] == "fail"
        assert "nominal_thickness" in i["affected_attributes"]

    def test_string_without_unit(self):
        r, _ = es.m01([STRING_NUMBERS], TYPES, UNITS)
        assert r["status"] == "fail"


class TestM02:
    def test_pass(self):
        r, _ = es.m02([VALID_PRODUCT], TYPES)
        assert r["status"] == "pass"

    def test_warn(self):
        r, i = es.m02([STRING_NUMBERS], TYPES)
        assert r["status"] == "warn"
        assert "pack_quantity" in i["affected_attributes"]


class TestM03:
    def test_pass(self):
        r, _ = es.m03([VALID_PRODUCT], UNITS)
        assert r["status"] == "pass"

    def test_warn(self):
        r, i = es.m03([make_product(attribute_units={})], UNITS)
        assert r["status"] == "warn"


class TestM04:
    def test_pass(self):
        r, _ = es.m04([VALID_PRODUCT], TYPES, UNITS)
        assert r["status"] == "pass"

    def test_fail(self):
        r, i = es.m04([BAD_CONCAT], TYPES, UNITS)
        assert r["status"] == "fail"
        assert "18mm" in i["sample_values"]["nominal_thickness"]

    def test_various_units(self):
        for val, attr in [("5kg", "weight"), ("220V", "voltage")]:
            types = {attr: "number"}
            units = {attr: "x"}
            p = make_product(extra_attributes={attr: val})
            r, _ = es.m04([p], types, units)
            assert r["status"] == "fail", f"Should catch '{val}'"


class TestGlobLoading:
    def test_loads_multiple_files(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text(json.dumps(make_product(sku="A")) + "\n")
        (tmp_path / "products_1_bbbb.jsonl").write_text(json.dumps(make_product(sku="B")) + "\n")
        products = es.load_products_for_iteration(tmp_path, 1)
        assert len(products) == 2

    def test_ignores_other_iterations(self, tmp_path):
        (tmp_path / "products_1_aaaa.jsonl").write_text(json.dumps(make_product()) + "\n")
        (tmp_path / "products_2_bbbb.jsonl").write_text(json.dumps(make_product()) + "\n")
        products = es.load_products_for_iteration(tmp_path, 1)
        assert len(products) == 1


class TestLoadRoutingTables:
    def test_extracts(self, tmp_path):
        data = {"subcategory_schemas": {"wood.lumber": {
            "attribute_types": {"wood_type": "str", "nominal_thickness": "number"},
            "units": {"nominal_thickness": "mm"},
        }}}
        path = tmp_path / "gen.json"
        path.write_text(json.dumps(data))
        types, units = es.load_routing_tables(path)
        assert types["nominal_thickness"] == "number"
        assert units["nominal_thickness"] == "mm"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
