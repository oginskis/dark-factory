"""Unit tests for eval.py semantic validation and per-subcategory scoring."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

# Make eval importable
sys.path.insert(0, str(Path(__file__).parent))

from eval import (
    check_core_attribute_coverage,
    check_extended_attribute_coverage,
    check_semantic_validation,
    eval_sample_size,
    load_config,
    main as eval_main,
    NUMERIC_VALUE_RE,
    NON_PRODUCT_NAME_RE,
)


# ---------------------------------------------------------------------------
# NUMERIC_VALUE_RE edge cases
# ---------------------------------------------------------------------------


class TestNumericValueRegex:
    def test_simple_metric(self):
        assert NUMERIC_VALUE_RE.match("150mm")

    def test_dual_metric_imperial(self):
        assert NUMERIC_VALUE_RE.match('47mm 2"')

    def test_decimal_metric(self):
        assert NUMERIC_VALUE_RE.match("2.5m")

    def test_bare_number(self):
        assert NUMERIC_VALUE_RE.match("150")

    def test_bare_decimal(self):
        assert NUMERIC_VALUE_RE.match("3.14")

    def test_empty_string_no_match(self):
        assert not NUMERIC_VALUE_RE.match("")

    def test_prose_with_number_no_match(self):
        assert not NUMERIC_VALUE_RE.match("ternal Cladding - 150mm")

    def test_html_no_match(self):
        assert not NUMERIC_VALUE_RE.match("<div>150</div>")

    def test_prose_prefix_no_match(self):
        assert not NUMERIC_VALUE_RE.match("approximately 150mm")

    def test_just_unit_no_match(self):
        assert not NUMERIC_VALUE_RE.match("mm")

    def test_number_with_slash(self):
        assert NUMERIC_VALUE_RE.match('6/"')


# ---------------------------------------------------------------------------
# NON_PRODUCT_NAME_RE — documented false positives
# ---------------------------------------------------------------------------


class TestNonProductNameRegex:
    def test_delivery_page(self):
        """Pure navigation page names match."""
        assert NON_PRODUCT_NAME_RE.search("Delivery Information")

    def test_contact_page(self):
        assert NON_PRODUCT_NAME_RE.search("Contact Us")

    def test_delivery_pallet_matches(self):
        """Known false positive — the has_data guard in check_semantic_validation
        prevents this from being flagged if the product has attributes."""
        assert NON_PRODUCT_NAME_RE.search("Delivery Pallet")

    def test_information_board_matches(self):
        """Known false positive — guarded by has_data check."""
        assert NON_PRODUCT_NAME_RE.search("Oak Information Board")

    def test_normal_product_no_match(self):
        assert not NON_PRODUCT_NAME_RE.search("Treated Softwood Timber 47mm x 100mm")


# ---------------------------------------------------------------------------
# check_semantic_validation — has_prices=false
# ---------------------------------------------------------------------------


class TestSemanticValidationNoPrices:
    def _make_products_no_price(self):
        """Products with no price but valid attributes — common in no-price catalogs."""
        return [
            {
                "name": "Softwood Timber 47x100",
                "sku": "SW-47-100",
                "url": "https://example.com/product/1",
                "core_attributes": {"wood_type": "Softwood"},
                "extended_attributes": {"nominal_thickness": "47mm"},
                "extra_attributes": {},
            },
            {
                "name": "Hardwood Oak Board",
                "sku": "HW-OAK-01",
                "url": "https://example.com/product/2",
                "core_attributes": {"wood_type": "Hardwood"},
                "extended_attributes": {"species": "Oak"},
                "extra_attributes": {},
            },
        ]

    def test_no_price_products_not_flagged(self):
        """Products without prices but WITH attributes should NOT be flagged
        as non-products when has_prices=False."""
        config = {
            "has_prices": False,
            "semantic_validation": {"numeric_fields": ["nominal_thickness"]},
        }
        products = self._make_products_no_price()
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["non_product_detection"]["flagged_count"] == 0

    def test_no_price_empty_record_flagged(self):
        """Empty records should still be flagged even with has_prices=False."""
        config = {
            "has_prices": False,
            "semantic_validation": {"numeric_fields": []},
        }
        products = [
            {
                "name": "Something",
                "url": "https://example.com/p/1",
                # No sku, no attributes
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["non_product_detection"]["flagged_count"] == 1

    def test_has_prices_true_flags_no_price_no_sku(self):
        """With has_prices=True, products missing price AND sku AND attrs are flagged."""
        config = {
            "has_prices": True,
            "semantic_validation": {"numeric_fields": []},
        }
        products = [
            {
                "name": "Something",
                "url": "https://example.com/p/1",
                # No price, no sku, no attributes
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        _, detail = result
        assert detail["non_product_detection"]["flagged_count"] == 1


# ---------------------------------------------------------------------------
# check_core_attribute_coverage — per-subcategory scoring
# ---------------------------------------------------------------------------


class TestCoreAttributeCoveragePerSubcategory:
    def _make_config(self):
        return {
            "has_prices": True,
            "core_attributes": ["wood_type", "material"],  # union
            "_sub_configs": {
                "wood.lumber": {
                    "core_attributes": ["wood_type"],
                    "extended_attributes": [],
                },
                "wood.millwork": {
                    "core_attributes": ["material"],
                    "extended_attributes": [],
                },
            },
        }

    def test_products_scored_against_own_subcategory(self):
        """A lumber product should be scored against lumber schema (wood_type),
        NOT the union (wood_type + material)."""
        config = self._make_config()
        products = [
            {
                "product_category": "wood.lumber",
                "sku": "L1", "name": "Timber", "url": "http://x",
                "price": 10, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"wood_type": "Softwood"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        # 7 mandatory core fields + 1 core (wood_type) = 8 fields
        # All 8 populated -> 100% > 80% threshold -> passes
        assert score == 1.0
        assert detail["wood.lumber"]["coverage"] == 1.0

    def test_millwork_not_penalized_for_lumber_attrs(self):
        """A millwork product should NOT be penalized for missing wood_type."""
        config = self._make_config()
        products = [
            {
                "product_category": "wood.millwork",
                "sku": "M1", "name": "Moulding", "url": "http://x",
                "price": 5, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"material": "MDF"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        assert score == 1.0
        assert detail["wood.millwork"]["coverage"] == 1.0

    def test_mixed_subcategories(self):
        """Products from different subcategories get independent scoring."""
        config = self._make_config()
        products = [
            {
                "product_category": "wood.lumber",
                "sku": "L1", "name": "Timber", "url": "http://x",
                "price": 10, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"wood_type": "Softwood"},
                "extended_attributes": {},
            },
            {
                "product_category": "wood.millwork",
                "sku": "M1", "name": "Moulding", "url": "http://x",
                "price": 5, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"material": "MDF"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        assert score == 1.0
        assert "wood.lumber" in detail
        assert "wood.millwork" in detail


class TestCoreAttributeCoverageUnclassified:
    def test_unclassified_falls_back_to_union(self):
        """Products without a matching subcategory use the default (union) core list."""
        config = {
            "has_prices": True,
            "core_attributes": ["wood_type", "material"],  # union
            "_sub_configs": {
                "wood.lumber": {
                    "core_attributes": ["wood_type"],
                    "extended_attributes": [],
                },
            },
        }
        products = [
            {
                "product_category": "unknown.thing",
                "sku": "U1", "name": "Unknown", "url": "http://x",
                "price": 10, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"wood_type": "Softwood"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        # 7 mandatory core fields + 2 union core (wood_type, material) = 9 fields
        # 8 populated (missing material) -> 8/9 = 88.9% > 80% -> passes
        assert score == 1.0
        assert "unknown.thing" in detail

    def test_truly_unclassified_product(self):
        """Product with no product_category at all."""
        config = {
            "has_prices": True,
            "core_attributes": ["wood_type"],
            "_sub_configs": {},
        }
        products = [
            {
                "sku": "X1", "name": "Thing", "url": "http://x",
                "price": 10, "currency": "GBP", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"wood_type": "Softwood"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        assert score == 1.0
        assert "_unclassified" in detail


# ---------------------------------------------------------------------------
# eval_sample_size
# ---------------------------------------------------------------------------


class TestEvalSampleSize:
    def test_basic_calculation(self):
        config = {
            "expected_product_count": 1000,
            "_sub_configs": {
                "a": {"expected_count": 500},
                "b": {"expected_count": 500},
            },
        }
        result = eval_sample_size(config)
        assert result["total"] == 300  # min(max(300, 50), 300)
        assert result["per_subcategory"]["a"] == 50
        assert result["per_subcategory"]["b"] == 50

    def test_floor_applied(self):
        config = {
            "expected_product_count": 100,
            "_sub_configs": {
                "a": {"expected_count": 50},
                "b": {"expected_count": 50},
            },
        }
        result = eval_sample_size(config)
        assert result["total"] == 50  # max(30, 50) = 50; per_sub = 5+5=10; max(50,10)=50

    def test_per_sub_minimums_lift_total(self):
        config = {
            "expected_product_count": 100,
            "_sub_configs": {
                f"sub_{i}": {"expected_count": 10} for i in range(10)
            },
        }
        result = eval_sample_size(config)
        # Each sub: max(ceil(10*0.1), 10) = 10, total per_sub = 100
        # total_target = min(max(ceil(100*0.3), 50), 300) = 50
        # actual = max(50, 100) = 100
        assert result["total"] == 100


# ---------------------------------------------------------------------------
# check_semantic_validation — returns None when no config
# ---------------------------------------------------------------------------


class TestSemanticValidationSkip:
    def test_returns_none_without_config(self):
        config = {"has_prices": True}
        products = [{"name": "test", "sku": "1"}]
        assert check_semantic_validation(products, config) is None

    def test_returns_tuple_with_config(self):
        config = {"has_prices": True, "semantic_validation": {"numeric_fields": []}}
        products = [{"name": "test", "sku": "1", "url": "http://x", "price": 10}]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert isinstance(score, float)
        assert isinstance(detail, dict)


# ---------------------------------------------------------------------------
# --no-history flag
# ---------------------------------------------------------------------------


class TestNoHistoryFlag:
    """Verify --no-history skips eval_history.json append and baseline creation."""

    def _setup_eval_tree(self, tmp_path):
        """Build the directory structure that eval.py's main() expects."""
        # Project root marker — find_project_root needs eval/ dir
        (tmp_path / "eval").mkdir()

        # Config at docs/eval-generator/testco/eval_config.json
        config_dir = tmp_path / "docs" / "eval-generator" / "testco"
        config_dir.mkdir(parents=True)
        config = {
            "company_slug": "testco",
            "expected_product_count": 10,
            "expected_top_level_categories": ["Cat A"],
            "subcategories": {
                "wood.softwood_hardwood_lumber": {
                    "core_attributes": ["wood_type"],
                    "extended_attributes": [],
                    "expected_count": 10,
                }
            },
            "type_map": {"wood_type": "str"},
            "enum_attributes": {},
            "has_prices": True,
        }
        config_path = config_dir / "eval_config.json"
        config_path.write_text(json.dumps(config))

        # Scraper output at docs/scraper-generator/testco/output/
        scraper_dir = tmp_path / "docs" / "scraper-generator" / "testco" / "output"
        scraper_dir.mkdir(parents=True)
        product = {
            "sku": "SKU1", "name": "Test", "url": "https://example.com/p1",
            "price": 10.0, "currency": "GBP", "brand": "Test",
            "product_category": "wood.softwood_hardwood_lumber",
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "category_path": "Cat A",
            "core_attributes": {"wood_type": "Softwood"},
            "extended_attributes": {}, "extra_attributes": {},
        }
        (scraper_dir / "products.jsonl").write_text(json.dumps(product) + "\n")
        (scraper_dir / "summary.json").write_text(json.dumps({
            "total_products": 1, "limited": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }))

        return config_path

    def test_no_history_skips_history_and_baseline(self, tmp_path):
        """With --no-history: eval_result.json written, history and baseline skipped."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval.py", str(config_path), "--no-history"]):
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert not (eval_output / "eval_history.json").exists()
        assert not (eval_output / "baseline.json").exists()

    def test_without_no_history_writes_history(self, tmp_path):
        """Without --no-history: eval_history.json IS created."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval.py", str(config_path)]):
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert (eval_output / "eval_history.json").exists()

    def test_no_history_still_reads_existing_baseline(self, tmp_path):
        """--no-history reads existing baseline for scoring but does not create one."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"
        eval_output.mkdir(parents=True, exist_ok=True)

        # Pre-create a baseline
        baseline = {"attribute_fill_rates": {"wood_type": 1.0}, "products_found": 1}
        (eval_output / "baseline.json").write_text(json.dumps(baseline))

        with patch("sys.argv", ["eval.py", str(config_path), "--no-history"]):
            eval_main()

        # Baseline should still exist and be unchanged
        result_baseline = json.loads((eval_output / "baseline.json").read_text())
        assert result_baseline == baseline
