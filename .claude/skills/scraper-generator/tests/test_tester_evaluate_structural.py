# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "pytest",
# ]
# ///
"""Tests for tester_evaluate_structural.py — S01-S09 validation rules."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import tester_evaluate_structural as es


# ---------------------------------------------------------------------------
# Fixtures — synthetic product records
# ---------------------------------------------------------------------------

def make_product(**overrides) -> dict:
    """Create a valid product record with all required fields."""
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


class TestS01CoreFillRate:
    """S01: >=30% of products must have non-empty core_attributes."""

    def test_all_have_core_passes(self):
        r, i = es.s01([VALID_PRODUCT] * 5)
        assert r["status"] == "pass"
        assert r["value"] == 1.0

    def test_none_have_core_fails(self):
        r, i = es.s01([EMPTY_CORE] * 5)
        assert r["status"] == "fail"
        assert r["value"] == 0
        assert i is not None

    def test_30_percent_threshold(self):
        # 3 valid + 7 empty = 30% — should pass
        products = [VALID_PRODUCT] * 3 + [EMPTY_CORE] * 7
        r, _ = es.s01(products)
        assert r["status"] == "pass"

    def test_29_percent_fails(self):
        # 29 valid + 71 empty = 29% — should fail
        products = [VALID_PRODUCT] * 29 + [EMPTY_CORE] * 71
        r, _ = es.s01(products)
        assert r["status"] == "fail"

    def test_empty_products_fails(self):
        r, _ = es.s01([])
        assert r["status"] == "fail"

    def test_per_category_breakdown(self):
        p1 = make_product(category_path="Timber > Softwood")
        p2 = make_product(category_path="Fencing > Panels", core_attributes={})
        r, _ = es.s01([p1, p2])
        assert "Timber" in r["per_category"]
        assert "Fencing" in r["per_category"]


class TestS02ExtendedFillRate:
    """S02: >=20% of products must have non-empty extended_attributes (warning)."""

    def test_all_have_extended_passes(self):
        r, _ = es.s02([VALID_PRODUCT] * 5)
        assert r["status"] == "pass"

    def test_none_have_extended_warns(self):
        empty_ext = make_product(extended_attributes={})
        r, i = es.s02([empty_ext] * 5)
        assert r["status"] == "warn"  # warning, not fail


class TestS03RequiredFields:
    """S03: 100% must have all top-level fields."""

    def test_valid_product_passes(self):
        r, _ = es.s03([VALID_PRODUCT])
        assert r["status"] == "pass"

    def test_missing_sku_fails(self):
        bad = make_product(sku=None)
        r, i = es.s03([bad])
        assert r["status"] == "fail"
        assert "sku" in i["detail"]

    def test_missing_price_key_fails(self):
        bad = make_product()
        del bad["price"]
        r, i = es.s03([bad])
        assert r["status"] == "fail"

    def test_null_price_passes(self):
        # price can be null (catalog doesn't show prices)
        p = make_product(price=None)
        r, _ = es.s03([p])
        assert r["status"] == "pass"


class TestS04TaxonomyID:
    """S04: product_category must be a valid taxonomy ID."""

    @patch("tester_evaluate_structural.load_taxonomy_ids")
    def test_valid_id_passes(self, mock_ids):
        mock_ids.return_value = {"wood.softwood_hardwood_lumber", "wood.plywood_engineered_panels"}
        r, _ = es.s04([VALID_PRODUCT])
        assert r["status"] == "pass"

    @patch("tester_evaluate_structural.load_taxonomy_ids")
    def test_invalid_id_fails(self, mock_ids):
        mock_ids.return_value = {"wood.plywood_engineered_panels"}
        r, i = es.s04([VALID_PRODUCT])  # has wood.softwood_hardwood_lumber
        assert r["status"] == "fail"
        assert i is not None


class TestS05BrandPlacement:
    """S05: brand must be top-level, not inside attribute buckets."""

    def test_brand_top_level_passes(self):
        r, _ = es.s05([VALID_PRODUCT])
        assert r["status"] == "pass"

    def test_brand_missing_fails(self):
        r, _ = es.s05([NO_BRAND])
        assert r["status"] == "fail"

    def test_brand_in_core_fails(self):
        r, i = es.s05([BRAND_IN_CORE])
        assert r["status"] == "fail"


class TestS06CategoryDiversity:
    """S06: >=2 distinct top-level category_path values."""

    def test_two_categories_passes(self):
        p1 = make_product(category_path="Timber > Softwood")
        p2 = make_product(category_path="Fencing > Panels")
        r, _ = es.s06([p1, p2])
        assert r["status"] == "pass"

    def test_one_category_warns(self):
        r, i = es.s06([VALID_PRODUCT, VALID_PRODUCT])
        assert r["status"] == "warn"

    def test_skip_in_retest(self):
        r, _ = es.s06([VALID_PRODUCT], skip=True)
        assert r["status"] == "skip"


class TestS07ZeroErrors:
    """S07: errors_count in summary.json must be 0."""

    def test_zero_errors_passes(self, tmp_path):
        (tmp_path / "summary.json").write_text(json.dumps({"errors_count": 0}))
        r, _ = es.s07(tmp_path)
        assert r["status"] == "pass"

    def test_nonzero_errors_fails(self, tmp_path):
        (tmp_path / "summary.json").write_text(json.dumps({"errors_count": 3}))
        r, i = es.s07(tmp_path)
        assert r["status"] == "fail"
        assert "3" in i["detail"]

    def test_missing_summary_fails(self, tmp_path):
        r, _ = es.s07(tmp_path)
        assert r["status"] == "fail"


class TestS08NoCrash:
    """S08: scraper must exit with code 0."""

    def test_zero_passes(self):
        r, _ = es.s08(0)
        assert r["status"] == "pass"

    def test_nonzero_fails(self):
        r, i = es.s08(1)
        assert r["status"] == "fail"

    def test_timeout_fails(self):
        r, i = es.s08(-1)
        assert r["status"] == "fail"
        assert "timed out" in i["detail"].lower()


class TestS09PersistHooks:
    """S09: products.jsonl must exist and be non-empty."""

    def test_nonempty_passes(self, tmp_path):
        (tmp_path / "products.jsonl").write_text('{"sku":"1"}\n')
        r, _ = es.s09(tmp_path)
        assert r["status"] == "pass"
        assert r["value"] == 1

    def test_empty_fails(self, tmp_path):
        (tmp_path / "products.jsonl").write_text("")
        r, i = es.s09(tmp_path)
        assert r["status"] == "fail"
        assert "empty" in i["detail"]

    def test_missing_fails(self, tmp_path):
        r, i = es.s09(tmp_path)
        assert r["status"] == "fail"
        assert "missing" in i["detail"]


class TestIterationFlag:
    """--iteration flag selects products_iteration_{N}.jsonl instead of products.jsonl."""

    def test_reads_iteration_file(self, tmp_path):
        # products.jsonl has 1 valid product
        (tmp_path / "products.jsonl").write_text(json.dumps(make_product()) + "\n")
        # products_iteration_2.jsonl has 1 product with empty core (will fail S01)
        (tmp_path / "products_iteration_2.jsonl").write_text(json.dumps(EMPTY_CORE) + "\n")
        (tmp_path / "summary.json").write_text(json.dumps({"errors_count": 0}))

        # Without --iteration: reads products.jsonl (valid) → S01 passes
        products_default = es.load_jsonl(tmp_path / "products.jsonl")
        r, _ = es.s01(products_default)
        assert r["status"] == "pass"

        # With --iteration 2: reads products_iteration_2.jsonl (empty core) → S01 fails
        products_iter2 = es.load_jsonl(tmp_path / "products_iteration_2.jsonl")
        r, _ = es.s01(products_iter2)
        assert r["status"] == "fail"

    def test_missing_iteration_file_returns_empty(self, tmp_path):
        products = es.load_jsonl(tmp_path / "products_iteration_99.jsonl")
        assert products == []


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
