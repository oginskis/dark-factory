# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_evaluate_semantic.py — M01-M04 validation rules."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_evaluate_semantic as es


# ---------------------------------------------------------------------------
# Fixtures — routing tables and products
# ---------------------------------------------------------------------------

# Simulates generator_input.json routing tables for wood.softwood_hardwood_lumber
TYPES = {
    "wood_type": "str",
    "nominal_thickness": "number",  # should be numeric, has unit "mm"
    "nominal_width": "number",      # should be numeric, has unit "mm"
    "pack_quantity": "number",      # should be numeric, no unit
    "species": "str",
}
UNITS = {
    "nominal_thickness": "mm",
    "nominal_width": "mm",
}


def make_product(**overrides) -> dict:
    """Create a product with correct numeric values and units."""
    base = {
        "sku": "SKU-001", "name": "PAR Timber", "url": "https://example.com/p1",
        "price": 9.99, "currency": "GBP", "brand": "TestBrand",
        "product_category": "wood.softwood_hardwood_lumber",
        "scraped_at": "2026-03-18T00:00:00Z",
        "category_path": "Timber > Softwood > PAR",
        "core_attributes": {"wood_type": "Softwood"},
        "extended_attributes": {
            "nominal_thickness": 18,       # correct: numeric
            "nominal_width": 50,           # correct: numeric
            "pack_quantity": 10,           # correct: numeric, no unit
            "species": "Redwood",          # correct: string
        },
        "extra_attributes": {},
        "attribute_units": {
            "nominal_thickness": "mm",
            "nominal_width": "mm",
        },
    }
    base.update(overrides)
    return base


# Product with concatenated units — the most common bug
BAD_CONCAT = make_product(
    extended_attributes={
        "nominal_thickness": "18mm",   # WRONG: should be 18 + units
        "nominal_width": "50mm",       # WRONG: should be 50 + units
        "pack_quantity": 10,
        "species": "Redwood",
    },
    attribute_units={},  # missing because values have units embedded
)

# Product with string numbers (no unit concatenation)
STRING_NUMBERS = make_product(
    extended_attributes={
        "nominal_thickness": "18",     # WRONG: string instead of int
        "nominal_width": "50",         # WRONG: string instead of int
        "pack_quantity": "10",         # WRONG: string instead of int
        "species": "Redwood",
    },
    attribute_units={"nominal_thickness": "mm", "nominal_width": "mm"},
)

VALID_PRODUCT = make_product()


class TestLoadRoutingTables:
    """load_routing_tables() correctly parses generator_input.json nesting."""

    def test_extracts_types_and_units(self, tmp_path):
        data = {
            "subcategory_schemas": {
                "wood.softwood_hardwood_lumber": {
                    "core_attribute_keys": ["wood_type"],
                    "extended_attribute_keys": ["nominal_thickness"],
                    "attribute_types": {"wood_type": "str", "nominal_thickness": "number"},
                    "units": {"nominal_thickness": "mm"},
                }
            }
        }
        path = tmp_path / "gen.json"
        path.write_text(json.dumps(data))

        types, units = es.load_routing_tables(path)
        assert types["nominal_thickness"] == "number"
        assert types["wood_type"] == "str"
        assert units["nominal_thickness"] == "mm"

    def test_merges_across_subcategories(self, tmp_path):
        data = {
            "subcategory_schemas": {
                "wood.lumber": {"attribute_types": {"wood_type": "str"}, "units": {}},
                "wood.plywood": {"attribute_types": {"panel_type": "str", "thickness": "number"}, "units": {"thickness": "mm"}},
            }
        }
        path = tmp_path / "gen.json"
        path.write_text(json.dumps(data))

        types, units = es.load_routing_tables(path)
        assert "wood_type" in types
        assert "panel_type" in types
        assert "thickness" in units


class TestM01UnitsSeparated:
    """M01: number+unit attrs must be numeric, not strings like '18mm'."""

    def test_correct_values_pass(self):
        r, i = es.m01([VALID_PRODUCT], TYPES, UNITS)
        assert r["status"] == "pass"
        assert i is None

    def test_concatenated_units_fail(self):
        r, i = es.m01([BAD_CONCAT], TYPES, UNITS)
        assert r["status"] == "fail"
        assert "nominal_thickness" in i["affected_attributes"]
        assert "18mm" in i["sample_values"]["nominal_thickness"]

    def test_string_without_unit_still_fails(self):
        r, i = es.m01([STRING_NUMBERS], TYPES, UNITS)
        assert r["status"] == "fail"

    def test_string_attr_not_flagged(self):
        p = make_product(core_attributes={"wood_type": "12mm Softwood"})
        r, _ = es.m01([p], TYPES, UNITS)
        assert r["status"] == "pass"


class TestM02TypeConformance:
    """M02: ALL number-typed attrs must be int/float (warning)."""

    def test_correct_types_pass(self):
        r, _ = es.m02([VALID_PRODUCT], TYPES)
        assert r["status"] == "pass"

    def test_string_number_warns(self):
        r, i = es.m02([STRING_NUMBERS], TYPES)
        assert r["status"] == "warn"
        assert "pack_quantity" in i["affected_attributes"]

    def test_string_typed_attrs_not_flagged(self):
        r, _ = es.m02([VALID_PRODUCT], TYPES)
        assert r["status"] == "pass"


class TestM03AttributeUnitsPopulated:
    """M03: attribute_units must have keys for attrs with units in routing table."""

    def test_all_units_present_passes(self):
        r, _ = es.m03([VALID_PRODUCT], UNITS)
        assert r["status"] == "pass"

    def test_missing_units_warns(self):
        p = make_product(attribute_units={})
        r, i = es.m03([p], UNITS)
        assert r["status"] == "warn"
        assert "nominal_thickness" in i["affected_attributes"]

    def test_attr_not_in_product_not_flagged(self):
        p = make_product(
            extended_attributes={"species": "Redwood"},
            attribute_units={},
        )
        r, _ = es.m03([p], UNITS)
        assert r["status"] == "pass"


class TestM04ConcatenationScan:
    """M04: regex scan for embedded units in number-typed or unit-bearing attrs."""

    def test_clean_values_pass(self):
        r, _ = es.m04([VALID_PRODUCT], TYPES, UNITS)
        assert r["status"] == "pass"

    def test_18mm_caught(self):
        r, i = es.m04([BAD_CONCAT], TYPES, UNITS)
        assert r["status"] == "fail"
        assert "18mm" in i["sample_values"]["nominal_thickness"]

    def test_string_attr_with_mm_not_flagged(self):
        p = make_product(extended_attributes={
            "species": "12mm Redwood",
            "nominal_thickness": 18,
            "nominal_width": 50,
            "pack_quantity": 10,
        })
        r, _ = es.m04([p], TYPES, UNITS)
        assert r["status"] == "pass"

    def test_various_unit_patterns(self):
        for val, attr in [("5kg", "weight"), ("220V", "voltage"), ("3.5kW", "power")]:
            types = {attr: "number"}
            units = {attr: "x"}
            p = make_product(extra_attributes={attr: val})
            r, _ = es.m04([p], types, units)
            assert r["status"] == "fail", f"Should catch '{val}'"


class TestVersionedFileSupport:
    """Script accepts versioned products file path directly."""

    def test_reads_versioned_products_file(self, tmp_path):
        pf = tmp_path / "products_2_b4d1.jsonl"
        pf.write_text(json.dumps(make_product()) + "\n")
        products = es.load_jsonl(pf)
        assert len(products) == 1
        r, _ = es.m01(products, TYPES, UNITS)
        assert r["status"] == "pass"

    def test_missing_versioned_file_returns_empty(self, tmp_path):
        pf = tmp_path / "products_99_xxxx.jsonl"
        products = es.load_jsonl(pf)
        assert products == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
