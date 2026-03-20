# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Unit tests for eval_run.py semantic validation, per-subcategory scoring, and collection logic."""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from unittest.mock import patch

import pytest

# Make eval_run importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from eval_run import (
    build_category_key_map,
    check_core_attribute_coverage,
    check_extended_attribute_coverage,
    check_schema_conformance,
    check_semantic_validation,
    eval_sample_size,
    load_config,
    main as eval_main,
    EMBEDDED_UNIT_RE,
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
        # All 8 populated -> 100% >= 75% threshold -> passes
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
        # 8 populated (missing material) -> 8/9 = 88.9% >= 75% -> passes
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
# eval_sample_size — new 20%/max-100 formula
# ---------------------------------------------------------------------------


class TestEvalSampleSize:
    def test_basic_20_percent(self):
        """20% of 500 = 100 per sub, total 200."""
        config = {
            "expected_product_count": 1000,
            "_sub_configs": {
                "a": {"expected_count": 500},
                "b": {"expected_count": 500},
            },
        }
        result = eval_sample_size(config)
        assert result["per_subcategory"]["a"] == 100  # min(max(ceil(500*0.2), 10), 100)
        assert result["per_subcategory"]["b"] == 100
        assert result["total"] == 200

    def test_floor_applied(self):
        """Small subcategories get floor of 10."""
        config = {
            "expected_product_count": 100,
            "_sub_configs": {
                "a": {"expected_count": 20},
                "b": {"expected_count": 20},
            },
        }
        result = eval_sample_size(config)
        # ceil(20 * 0.2) = 4, max(4, 10) = 10, min(10, 100) = 10
        assert result["per_subcategory"]["a"] == 10
        assert result["per_subcategory"]["b"] == 10
        assert result["total"] == 20

    def test_cap_at_100(self):
        """Large subcategories get capped at 100."""
        config = {
            "expected_product_count": 5000,
            "_sub_configs": {
                "a": {"expected_count": 3000},
                "b": {"expected_count": 2000},
            },
        }
        result = eval_sample_size(config)
        # ceil(3000 * 0.2) = 600, min(600, 100) = 100
        assert result["per_subcategory"]["a"] == 100
        # ceil(2000 * 0.2) = 400, min(400, 100) = 100
        assert result["per_subcategory"]["b"] == 100
        assert result["total"] == 200

    def test_many_small_subcategories(self):
        """Each sub gets floor of 10, total = sum."""
        config = {
            "expected_product_count": 100,
            "_sub_configs": {
                f"sub_{i}": {"expected_count": 10} for i in range(10)
            },
        }
        result = eval_sample_size(config)
        # ceil(10 * 0.2) = 2, max(2, 10) = 10
        for sub_id in config["_sub_configs"]:
            assert result["per_subcategory"][sub_id] == 10
        assert result["total"] == 100

    def test_no_subcategories_fallback(self):
        """No subcategories: use expected_product_count directly."""
        config = {
            "expected_product_count": 500,
            "_sub_configs": {},
        }
        result = eval_sample_size(config)
        # min(max(ceil(500*0.2), 10), 100) = min(100, 100) = 100
        assert result["total"] == 100
        assert result["per_subcategory"] == {}


# ---------------------------------------------------------------------------
# check_semantic_validation — always runs (never returns None)
# ---------------------------------------------------------------------------


class TestSemanticValidationAlwaysRuns:
    def test_returns_tuple_without_config(self):
        """semantic_validation now always runs, even without config key."""
        config = {"has_prices": True}
        products = [{"name": "test", "sku": "1", "url": "http://x", "price": 10}]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert isinstance(score, float)
        assert "value_cleanliness" in detail
        assert "non_product_detection" in detail
        assert "embedded_units" in detail

    def test_returns_tuple_with_config(self):
        config = {"has_prices": True, "semantic_validation": {"numeric_fields": []}}
        products = [{"name": "test", "sku": "1", "url": "http://x", "price": 10}]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert isinstance(score, float)
        assert isinstance(detail, dict)


# ---------------------------------------------------------------------------
# Embedded-units detection
# ---------------------------------------------------------------------------


class TestEmbeddedUnits:
    def test_clean_values_pass(self):
        """Products with no embedded units should pass."""
        config = {"has_prices": True}
        products = [
            {
                "name": "Product A", "sku": "A1", "url": "http://x", "price": 10,
                "core_attributes": {"material": "Steel", "color": "Red"},
                "extended_attributes": {"weight": "5"},
                "extra_attributes": {"finish": "Matte"},
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["embedded_units"]["flagged_count"] == 0
        assert detail["embedded_units"]["score"] == 1.0

    def test_core_attr_embedded_unit_detected(self):
        """Embedded unit in core_attributes is detected."""
        config = {"has_prices": True}
        products = [
            {
                "name": "Timber", "sku": "T1", "url": "http://x", "price": 10,
                "core_attributes": {"thickness": "18mm"},
                "extended_attributes": {},
                "extra_attributes": {},
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["embedded_units"]["flagged_count"] == 1

    def test_extended_attr_embedded_unit_detected(self):
        """Embedded unit in extended_attributes is detected."""
        config = {"has_prices": True}
        products = [
            {
                "name": "Board", "sku": "B1", "url": "http://x", "price": 10,
                "core_attributes": {"material": "MDF"},
                "extended_attributes": {"weight": "5kg"},
                "extra_attributes": {},
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["embedded_units"]["flagged_count"] == 1

    def test_extra_attr_embedded_unit_detected(self):
        """Embedded unit in extra_attributes is detected."""
        config = {"has_prices": True}
        products = [
            {
                "name": "Motor", "sku": "M1", "url": "http://x", "price": 100,
                "core_attributes": {},
                "extended_attributes": {},
                "extra_attributes": {"power_output": "500W"},
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        assert detail["embedded_units"]["flagged_count"] == 1

    def test_embedded_units_drag_composite_score(self):
        """Embedded units use min(scores) so they drag the entire check."""
        config = {"has_prices": True}
        products = [
            {
                "name": "Clean Product", "sku": "C1", "url": "http://x", "price": 10,
                "core_attributes": {"material": "Steel"},
                "extended_attributes": {},
                "extra_attributes": {},
            },
            {
                "name": "Dirty Product", "sku": "D1", "url": "http://x", "price": 20,
                "core_attributes": {"thickness": "18mm"},
                "extended_attributes": {},
                "extra_attributes": {},
            },
        ]
        result = check_semantic_validation(products, config)
        assert result is not None
        score, detail = result
        # embedded_units score is 0.5 (1/2 clean), which drags composite to 0.5
        assert score <= 0.5

    def test_embedded_unit_regex_patterns(self):
        """Test various unit patterns are detected."""
        assert EMBEDDED_UNIT_RE.search("18mm")
        assert EMBEDDED_UNIT_RE.search("5kg")
        assert EMBEDDED_UNIT_RE.search("100W")
        assert EMBEDDED_UNIT_RE.search("230V")
        assert EMBEDDED_UNIT_RE.search("50Hz")
        assert EMBEDDED_UNIT_RE.search("1500rpm")
        assert EMBEDDED_UNIT_RE.search("85dB")
        assert EMBEDDED_UNIT_RE.search("10kWh")
        assert EMBEDDED_UNIT_RE.search("50psi")
        assert EMBEDDED_UNIT_RE.search("12ft")
        assert EMBEDDED_UNIT_RE.search("75%")

    def test_non_unit_strings_not_flagged(self):
        """Regular strings should not match the embedded unit regex."""
        assert not EMBEDDED_UNIT_RE.search("Steel")
        assert not EMBEDDED_UNIT_RE.search("Red")
        assert not EMBEDDED_UNIT_RE.search("")
        assert not EMBEDDED_UNIT_RE.search("Heavy duty")


# ---------------------------------------------------------------------------
# build_category_key_map
# ---------------------------------------------------------------------------


class TestBuildCategoryKeyMap:
    def test_inverts_mapping(self):
        """category_mapping is inverted: URL prefix -> taxonomy becomes taxonomy -> [prefixes]."""
        scraper_config = {
            "category_mapping": {
                "/softwood": "wood.lumber",
                "/hardwood": "wood.lumber",
                "/mouldings": "wood.millwork",
            }
        }
        result = build_category_key_map(scraper_config)
        assert set(result["wood.lumber"]) == {"/softwood", "/hardwood"}
        assert result["wood.millwork"] == ["/mouldings"]

    def test_empty_mapping(self):
        """Empty category_mapping produces empty result."""
        assert build_category_key_map({"category_mapping": {}}) == {}
        assert build_category_key_map({}) == {}

    def test_single_entry(self):
        scraper_config = {"category_mapping": {"/tools": "machinery.power_tools"}}
        result = build_category_key_map(scraper_config)
        assert result == {"machinery.power_tools": ["/tools"]}


# ---------------------------------------------------------------------------
# Core threshold 75%
# ---------------------------------------------------------------------------


class TestCoreThreshold75:
    def test_75_percent_boundary_passes(self):
        """A product with exactly 75% core coverage should pass."""
        config = {
            "has_prices": True,
            "core_attributes": ["a1", "a2", "a3", "a4", "a5"],
            "_sub_configs": {},
        }
        # 7 mandatory + 5 core = 12 total
        # Need >= 75% = 9 populated
        products = [
            {
                "sku": "S1", "name": "P", "url": "http://x",
                "price": 10, "currency": "USD", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"a1": "v", "a2": "v"},
                # a3, a4, a5 missing -> populated = 7 mandatory + 2 = 9
                # 9/12 = 0.75 -> passes (>= 0.75)
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        assert score == 1.0

    def test_below_75_percent_fails(self):
        """A product below 75% core coverage should fail."""
        config = {
            "has_prices": True,
            "core_attributes": ["a1", "a2", "a3", "a4", "a5"],
            "_sub_configs": {},
        }
        # 7 mandatory + 5 core = 12 total
        # populated = 7 mandatory + 1 = 8 -> 8/12 = 66.7% < 75%
        products = [
            {
                "sku": "S1", "name": "P", "url": "http://x",
                "price": 10, "currency": "USD", "brand": "B",
                "scraped_at": "2026-01-01T00:00:00+00:00",
                "core_attributes": {"a1": "v"},
                "extended_attributes": {},
            },
        ]
        score, detail = check_core_attribute_coverage(products, config)
        assert score == 0.0


# ---------------------------------------------------------------------------
# Schema conformance — attributes not in type_map
# ---------------------------------------------------------------------------


class TestSchemaConformanceBroadened:
    def test_unknown_attr_valid_primitive(self):
        """Attributes NOT in type_map: valid primitives pass."""
        config = {"type_map": {}, "enum_attributes": {}}
        products = [
            {
                "core_attributes": {"unknown_field": "some value"},
                "extended_attributes": {},
                "extra_attributes": {},
            }
        ]
        score = check_schema_conformance(products, config)
        assert score == 1.0

    def test_unknown_attr_empty_string_fails(self):
        """Attributes NOT in type_map: empty string fails."""
        config = {"type_map": {}, "enum_attributes": {}}
        products = [
            {
                "core_attributes": {"unknown_field": ""},
                "extended_attributes": {},
                "extra_attributes": {},
            }
        ]
        score = check_schema_conformance(products, config)
        assert score == 0.0

    def test_unknown_attr_html_fails(self):
        """Attributes NOT in type_map: HTML content fails."""
        config = {"type_map": {}, "enum_attributes": {}}
        products = [
            {
                "core_attributes": {"unknown_field": "<div>content</div>"},
                "extended_attributes": {},
                "extra_attributes": {},
            }
        ]
        score = check_schema_conformance(products, config)
        assert score == 0.0

    def test_unknown_attr_number_passes(self):
        """Attributes NOT in type_map: numbers pass."""
        config = {"type_map": {}, "enum_attributes": {}}
        products = [
            {
                "core_attributes": {"unknown_field": 42},
                "extended_attributes": {},
                "extra_attributes": {},
            }
        ]
        score = check_schema_conformance(products, config)
        assert score == 1.0


# ---------------------------------------------------------------------------
# --no-history flag
# ---------------------------------------------------------------------------


class TestNoHistoryFlag:
    """Verify --no-history skips eval_history.json append and baseline creation."""

    def _setup_eval_tree(self, tmp_path):
        """Build the directory structure that eval_run.py's main() expects."""
        # Project root marker — find_project_root needs docs/ dir
        (tmp_path / "docs").mkdir()

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

        # Eval output products at docs/eval-generator/testco/output/
        eval_output_dir = config_dir / "output"
        eval_output_dir.mkdir(parents=True)
        product = {
            "sku": "SKU1", "name": "Test", "url": "https://example.com/p1",
            "price": 10.0, "currency": "GBP", "brand": "Test",
            "product_category": "wood.softwood_hardwood_lumber",
            "scraped_at": datetime.now(timezone.utc).isoformat(),
            "category_path": "Cat A",
            "core_attributes": {"wood_type": "Softwood"},
            "extended_attributes": {}, "extra_attributes": {},
        }
        (eval_output_dir / "products.jsonl").write_text(json.dumps(product) + "\n")
        (eval_output_dir / "summary.json").write_text(json.dumps({
            "total_products": 1, "limited": True,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }))

        return config_path

    def test_no_history_skips_history_and_baseline(self, tmp_path):
        """With --no-history: eval_result.json written, history and baseline skipped."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval_run.py", str(config_path), "--no-history"]):
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert not (eval_output / "eval_history.json").exists()
        assert not (eval_output / "baseline.json").exists()

    def test_without_no_history_writes_history(self, tmp_path):
        """Without --no-history: eval_history.json IS created."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        with patch("sys.argv", ["eval_run.py", str(config_path)]):
            eval_main()

        assert (eval_output / "eval_result.json").exists()
        assert (eval_output / "eval_history.json").exists()

    def test_no_history_still_reads_existing_baseline(self, tmp_path):
        """--no-history reads existing baseline for scoring but does not create one."""
        config_path = self._setup_eval_tree(tmp_path)
        eval_output = config_path.parent / "output"

        # Pre-create a baseline
        baseline = {"attribute_fill_rates": {"wood_type": 1.0}, "products_found": 1}
        (eval_output / "baseline.json").write_text(json.dumps(baseline))

        with patch("sys.argv", ["eval_run.py", str(config_path), "--no-history"]):
            eval_main()

        # Baseline should still exist and be unchanged
        result_baseline = json.loads((eval_output / "baseline.json").read_text())
        assert result_baseline == baseline


# ---------------------------------------------------------------------------
# Conditions consistency — conditions.md must match eval_run.py
# ---------------------------------------------------------------------------


class TestConditionsConsistency:
    """Verify conditions.md documents the same checks/thresholds as eval_run.py."""

    CONDITIONS_PATH = Path(__file__).resolve().parent.parent / "references" / "conditions.md"

    def _parse_checks_table(self) -> dict[str, dict]:
        text = self.CONDITIONS_PATH.read_text()
        checks = {}
        in_table = False
        for line in text.splitlines():
            if "| Check " in line and "| Weight " in line:
                in_table = True
                continue
            if in_table and line.startswith("|---"):
                continue
            if in_table and line.startswith("|"):
                cols = [c.strip() for c in line.split("|")[1:-1]]
                if len(cols) >= 3:
                    name = cols[0].strip("`")
                    weight = int(cols[1])
                    threshold = float(cols[2])
                    checks[name] = {"weight": weight, "threshold": threshold}
            elif in_table and not line.startswith("|"):
                break
        return checks

    def test_all_checks_documented(self):
        """Every check in eval_run.py appears in conditions.md."""
        from eval_run import CHECKS
        doc_checks = self._parse_checks_table()
        for name in CHECKS:
            assert name in doc_checks, f"'{name}' in eval_run.py but missing from conditions.md"

    def test_no_extra_checks_in_docs(self):
        """No checks in conditions.md that aren't in eval_run.py."""
        from eval_run import CHECKS
        doc_checks = self._parse_checks_table()
        for name in doc_checks:
            assert name in CHECKS, f"'{name}' in conditions.md but missing from eval_run.py"

    def test_weights_match(self):
        """Weights in conditions.md match eval_run.py."""
        from eval_run import CHECKS
        doc_checks = self._parse_checks_table()
        for name in CHECKS:
            if name in doc_checks:
                assert CHECKS[name]["weight"] == doc_checks[name]["weight"], \
                    f"'{name}' weight: code={CHECKS[name]['weight']}, doc={doc_checks[name]['weight']}"

    def test_thresholds_match(self):
        """Thresholds in conditions.md match eval_run.py."""
        from eval_run import CHECKS
        doc_checks = self._parse_checks_table()
        for name in CHECKS:
            if name in doc_checks:
                assert abs(CHECKS[name]["threshold"] - doc_checks[name]["threshold"]) < 0.001, \
                    f"'{name}' threshold: code={CHECKS[name]['threshold']}, doc={doc_checks[name]['threshold']}"

    def test_weights_sum_to_100(self):
        """Both code and docs weights sum to 100."""
        from eval_run import CHECKS
        doc_checks = self._parse_checks_table()
        assert sum(c["weight"] for c in CHECKS.values()) == 100, "Code weights don't sum to 100"
        assert sum(c["weight"] for c in doc_checks.values()) == 100, "Doc weights don't sum to 100"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
