# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for validate_assessment.py — all gate functions, template detection, field extraction."""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from validate_assessment import (
    check_anti_bot_value,
    check_category_tree_complete,
    check_correct_template,
    check_data_source_concrete,
    check_discovery_actionable,
    check_findings_explain,
    check_heading_and_slug,
    check_knowledgebase_updated,
    check_platform_valid,
    check_price_verified,
    check_product_count,
    check_spec_table_verified,
    check_stop_template,
    check_strategy_valid,
    check_valid_stop_reason,
    detect_template,
    extract_field,
    extract_section,
    extract_slug,
    run_gates,
)


# ---------------------------------------------------------------------------
# detect_template
# ---------------------------------------------------------------------------


class TestDetectTemplate:
    def test_success_template(self, success_assessment_content):
        assert detect_template(success_assessment_content) == "success"

    def test_stop_template(self, stop_assessment_content):
        assert detect_template(stop_assessment_content) == "stop"

    def test_unknown_template(self):
        content = "# Some Document\n\nNo template markers here.\n"
        assert detect_template(content) == "unknown"

    def test_stop_takes_precedence_over_success(self):
        """If both markers are present, stop wins."""
        content = textwrap.dedent("""\
            ## Extraction Blueprint

            Some content.

            **Scraping strategy:** none
            **Stop reason:** anti_bot_severe
        """)
        assert detect_template(content) == "stop"

    def test_blueprint_without_stop_is_success(self):
        content = "## Extraction Blueprint\n\nSome content.\n"
        assert detect_template(content) == "success"


# ---------------------------------------------------------------------------
# extract_field
# ---------------------------------------------------------------------------


class TestExtractField:
    def test_extract_existing_field(self):
        content = "**Platform:** shopify\n**Strategy:** html_css\n"
        assert extract_field(content, "Platform") == "shopify"

    def test_extract_with_extra_content(self):
        content = "**Anti-bot:** none (no challenges detected)\n"
        result = extract_field(content, "Anti-bot")
        assert result == "none (no challenges detected)"

    def test_missing_field(self):
        content = "**Platform:** shopify\n"
        assert extract_field(content, "Missing") is None

    def test_field_with_url(self):
        content = "**URL:** https://www.example.com\n"
        assert extract_field(content, "URL") == "https://www.example.com"


# ---------------------------------------------------------------------------
# extract_slug
# ---------------------------------------------------------------------------


class TestExtractSlug:
    def test_slug_extraction(self):
        content = "**Slug:** test-company\n"
        assert extract_slug(content) == "test-company"

    def test_slug_missing(self):
        content = "**Platform:** shopify\n"
        assert extract_slug(content) is None


# ---------------------------------------------------------------------------
# extract_section
# ---------------------------------------------------------------------------


class TestExtractSection:
    def test_h2_section(self):
        content = "## Findings\n\n- Found something\n- Another finding\n"
        result = extract_section(content, "Findings")
        assert result is not None
        assert "Found something" in result

    def test_h3_section(self):
        content = "### Data Source\n\n**Primary method:** JSON-LD\n\n### Other\n\nStuff\n"
        result = extract_section(content, "Data Source")
        assert result is not None
        assert "Primary method" in result

    def test_h4_section(self):
        content = "#### Price\n\nPrice data here.\n\n#### Spec Table\n\nSpec data.\n"
        result = extract_section(content, "Price")
        assert result is not None
        assert "Price data here." in result

    def test_missing_section(self):
        content = "## Something Else\n\nContent.\n"
        assert extract_section(content, "Missing") is None

    def test_last_section_captures_to_end(self):
        content = "## Last Section\n\nFinal content.\n"
        result = extract_section(content, "Last Section")
        assert result is not None
        assert "Final content." in result


# ---------------------------------------------------------------------------
# Success gate checks
# ---------------------------------------------------------------------------


class TestCheckCorrectTemplate:
    def test_success_passes(self):
        result = check_correct_template("success")
        assert result["pass"] is True

    def test_stop_passes(self):
        result = check_correct_template("stop")
        assert result["pass"] is True

    def test_unknown_fails(self):
        result = check_correct_template("unknown")
        assert result["pass"] is False


class TestCheckHeadingAndSlug:
    def test_valid(self, success_assessment_content):
        result = check_heading_and_slug(success_assessment_content)
        assert result["pass"] is True
        assert "test-company" in result["details"]

    def test_missing_h1(self):
        content = "**Slug:** test-co\nSome content\n"
        result = check_heading_and_slug(content)
        assert result["pass"] is False
        assert "H1 missing" in result["details"]

    def test_missing_slug(self):
        content = "# Catalog Assessment: Test\n\nNo slug.\n"
        result = check_heading_and_slug(content)
        assert result["pass"] is False
        assert "Slug field missing" in result["details"]

    def test_both_missing(self):
        content = "No heading, no slug.\n"
        result = check_heading_and_slug(content)
        assert result["pass"] is False


class TestCheckStrategyValid:
    def test_html_css(self):
        content = "**Scraping strategy:** html_css\n"
        result = check_strategy_valid(content)
        assert result["pass"] is True

    def test_json_api(self):
        content = "**Scraping strategy:** json_api\n"
        result = check_strategy_valid(content)
        assert result["pass"] is True

    def test_pdf(self):
        content = "**Scraping strategy:** pdf\n"
        result = check_strategy_valid(content)
        assert result["pass"] is True

    def test_none_strategy(self):
        content = "**Scraping strategy:** none\n"
        result = check_strategy_valid(content)
        assert result["pass"] is True

    def test_invalid_strategy(self):
        content = "**Scraping strategy:** api_only\n"
        result = check_strategy_valid(content)
        assert result["pass"] is False

    def test_missing_strategy(self):
        content = "No strategy field.\n"
        result = check_strategy_valid(content)
        assert result["pass"] is False

    def test_strategy_with_extra_text(self):
        """Strategy with additional description after the value should still pass."""
        content = "**Scraping strategy:** json_api (JSON-LD primary)\n"
        result = check_strategy_valid(content)
        assert result["pass"] is True


class TestCheckPlatformValid:
    def test_shopify(self):
        content = "**Platform:** shopify\n"
        result = check_platform_valid(content)
        assert result["pass"] is True

    def test_woocommerce(self):
        content = "**Platform:** woocommerce\n"
        result = check_platform_valid(content)
        assert result["pass"] is True

    def test_unknown_platform(self):
        content = "**Platform:** unknown\n"
        result = check_platform_valid(content)
        assert result["pass"] is True

    def test_custom_platform(self):
        content = "**Platform:** custom\n"
        result = check_platform_valid(content)
        assert result["pass"] is True

    def test_invalid_platform(self):
        content = "**Platform:** wordpress\n"
        result = check_platform_valid(content)
        assert result["pass"] is False

    def test_missing_platform(self):
        content = "No platform field.\n"
        result = check_platform_valid(content)
        assert result["pass"] is False

    def test_platform_with_extra_text(self):
        content = "**Platform:** magento (version 2.4)\n"
        result = check_platform_valid(content)
        assert result["pass"] is True


class TestCheckDataSourceConcrete:
    def test_valid(self, success_assessment_content):
        result = check_data_source_concrete(success_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No data source section.\n"
        result = check_data_source_concrete(content)
        assert result["pass"] is False
        assert "missing" in result["details"].lower()

    def test_missing_method(self):
        content = "### Data Source\n\n**Endpoint/URL pattern:** /api/products\n"
        result = check_data_source_concrete(content)
        assert result["pass"] is False

    def test_missing_endpoint(self):
        content = "### Data Source\n\n**Primary method:** JSON-LD\n"
        result = check_data_source_concrete(content)
        assert result["pass"] is False


class TestCheckDiscoveryActionable:
    def test_valid(self, success_assessment_content):
        result = check_discovery_actionable(success_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No discovery section.\n"
        result = check_discovery_actionable(content)
        assert result["pass"] is False

    def test_missing_fields(self):
        content = "### Product Discovery\n\n**Discovery method:** sitemap\n"
        result = check_discovery_actionable(content)
        assert result["pass"] is False
        assert "Pagination mechanism" in result["details"]

    def test_all_fields_present(self):
        content = textwrap.dedent("""\
            ### Product Discovery

            **Discovery method:** sitemap
            **Pagination mechanism:** query parameter
            **Products per page:** 24
            **Pagination URL pattern:** ?page={n}
        """)
        result = check_discovery_actionable(content)
        assert result["pass"] is True


class TestCheckCategoryTreeComplete:
    def test_valid(self, success_assessment_content):
        result = check_category_tree_complete(success_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No category tree section.\n"
        result = check_category_tree_complete(content)
        assert result["pass"] is False

    def test_no_data_rows(self):
        content = "#### Verified Category Tree\n\n| Category | URL | Product Count |\n|---|---|---|\n"
        result = check_category_tree_complete(content)
        assert result["pass"] is False

    def test_empty_product_count_accepted(self):
        """Empty product count cell is treated as an acknowledged placeholder."""
        content = textwrap.dedent("""\
            #### Verified Category Tree

            | Category | URL | Product Count |
            |---|---|---|
            | Tools | /tools | 150 |
            | Parts | /parts | |
        """)
        result = check_category_tree_complete(content)
        assert result["pass"] is True

    def test_non_numeric_product_count_fails(self):
        """A non-numeric, non-placeholder count cell should fail."""
        content = textwrap.dedent("""\
            #### Verified Category Tree

            | Category | URL | Product Count |
            |---|---|---|
            | Tools | /tools | 150 |
            | Parts | /parts | many |
        """)
        result = check_category_tree_complete(content)
        assert result["pass"] is False

    def test_star_as_count_accepted(self):
        content = textwrap.dedent("""\
            #### Verified Category Tree

            | Category | URL | Product Count |
            |---|---|---|
            | Tools | /tools | * |
            | Parts | /parts | 150 |
        """)
        result = check_category_tree_complete(content)
        assert result["pass"] is True

    def test_landing_pages_skipped(self):
        content = textwrap.dedent("""\
            #### Verified Category Tree

            | Category | URL | Product Count |
            |---|---|---|
            | Tools | /tools | (landing) |
            | Parts | /parts | 150 |
        """)
        result = check_category_tree_complete(content)
        assert result["pass"] is True


class TestCheckPriceVerified:
    def test_valid(self, success_assessment_content):
        result = check_price_verified(success_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No price section.\n"
        result = check_price_verified(content)
        assert result["pass"] is False

    def test_only_one_url(self):
        content = "#### Price\n\n- https://example.com/p/1 - $29.99\n"
        result = check_price_verified(content)
        assert result["pass"] is False
        assert "1" in result["details"]

    def test_two_urls(self):
        content = textwrap.dedent("""\
            #### Price

            **Verified on:**
            - https://example.com/p/1 - $29.99
            - https://example.com/p/2 - $49.99
        """)
        result = check_price_verified(content)
        assert result["pass"] is True


class TestCheckSpecTableVerified:
    def test_valid(self, success_assessment_content):
        result = check_spec_table_verified(success_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No spec table section.\n"
        result = check_spec_table_verified(content)
        assert result["pass"] is False

    def test_attributes_heading_alternative(self):
        content = textwrap.dedent("""\
            #### Attributes

            **Verified on:**
            - https://example.com/p/1 - 5 attributes
            - https://example.com/p/2 - 3 attributes
        """)
        result = check_spec_table_verified(content)
        assert result["pass"] is True

    def test_spec_table_heading_alternative(self):
        content = textwrap.dedent("""\
            #### Spec Table

            **Verified on:**
            - https://example.com/p/1 - 5 attributes
            - https://example.com/p/2 - 3 attributes
        """)
        result = check_spec_table_verified(content)
        assert result["pass"] is True


class TestCheckProductCount:
    def test_valid_numeric(self):
        content = "**Estimated product count:** ~500\n"
        result = check_product_count(content)
        assert result["pass"] is True

    def test_valid_exact(self):
        content = "**Estimated product count:** 1200\n"
        result = check_product_count(content)
        assert result["pass"] is True

    def test_missing(self):
        content = "No product count.\n"
        result = check_product_count(content)
        assert result["pass"] is False

    def test_non_numeric(self):
        content = "**Estimated product count:** unknown\n"
        result = check_product_count(content)
        assert result["pass"] is False


class TestCheckKnowledgebaseUpdated:
    def test_slug_found_in_kb(self, tmp_path):
        content = "**Slug:** test-store\n**Platform:** shopify\n"
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text("## Sites\n\n| test-store | https://test-store.com |\n")

        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is True

    def test_slug_not_found_in_kb(self, tmp_path):
        content = "**Slug:** new-store\n**Platform:** shopify\n"
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text("## Sites\n\n| other-store | https://other.com |\n")

        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is False

    def test_kb_file_missing(self, tmp_path):
        content = "**Slug:** test-store\n**Platform:** shopify\n"
        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is False

    def test_unknown_platform_no_kb_expected(self, tmp_path):
        content = "**Slug:** test-store\n**Platform:** unknown\n"
        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is True

    def test_custom_platform_no_kb_expected(self, tmp_path):
        content = "**Slug:** test-store\n**Platform:** custom\n"
        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is True

    def test_missing_slug(self, tmp_path):
        content = "**Platform:** shopify\n"
        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is False

    def test_missing_platform(self, tmp_path):
        content = "**Slug:** test-store\n"
        result = check_knowledgebase_updated(content, tmp_path)
        assert result["pass"] is False


class TestCheckAntiBotValue:
    def test_none_value(self):
        content = "**Anti-bot:** none\n"
        result = check_anti_bot_value(content)
        assert result["pass"] is True

    def test_light_value(self):
        content = "**Anti-bot:** light (rate limiting only)\n"
        result = check_anti_bot_value(content)
        assert result["pass"] is True

    def test_moderate_value(self):
        content = "**Anti-bot:** moderate (Cloudflare basic)\n"
        result = check_anti_bot_value(content)
        assert result["pass"] is True

    def test_severe_not_valid_for_success(self):
        content = "**Anti-bot:** severe\n"
        result = check_anti_bot_value(content)
        assert result["pass"] is False

    def test_missing(self):
        content = "No anti-bot field.\n"
        result = check_anti_bot_value(content)
        assert result["pass"] is False


# ---------------------------------------------------------------------------
# Stop gate checks
# ---------------------------------------------------------------------------


class TestCheckStopTemplate:
    def test_valid(self, stop_assessment_content):
        result = check_stop_template(stop_assessment_content)
        assert result["pass"] is True

    def test_missing_strategy_none(self):
        content = "**Stop reason:** anti_bot_severe\n"
        result = check_stop_template(content)
        assert result["pass"] is False

    def test_missing_stop_reason(self):
        content = "**Scraping strategy:** none\n"
        result = check_stop_template(content)
        assert result["pass"] is False


class TestCheckValidStopReason:
    def test_valid_reasons(self):
        for reason in ["no_public_catalog", "auth_required", "anti_bot_severe",
                       "js_only", "attributes_not_extractable"]:
            content = f"**Stop reason:** {reason}\n"
            result = check_valid_stop_reason(content)
            assert result["pass"] is True, f"Failed for reason: {reason}"

    def test_invalid_reason(self):
        content = "**Stop reason:** too_expensive\n"
        result = check_valid_stop_reason(content)
        assert result["pass"] is False

    def test_missing_reason(self):
        content = "No stop reason.\n"
        result = check_valid_stop_reason(content)
        assert result["pass"] is False


class TestCheckFindingsExplain:
    def test_valid(self, stop_assessment_content):
        result = check_findings_explain(stop_assessment_content)
        assert result["pass"] is True

    def test_missing_section(self):
        content = "No findings section.\n"
        result = check_findings_explain(content)
        assert result["pass"] is False

    def test_section_without_bullets(self):
        content = "## Findings\n\nJust a paragraph, no bullets.\n"
        result = check_findings_explain(content)
        assert result["pass"] is False

    def test_section_with_bullets(self):
        content = "## Findings\n\n- First finding\n- Second finding\n"
        result = check_findings_explain(content)
        assert result["pass"] is True


# ---------------------------------------------------------------------------
# run_gates
# ---------------------------------------------------------------------------


class TestRunGates:
    def test_success_template_gates(self, success_assessment_content, tmp_path):
        # Create a knowledgebase file for the platform
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text("## Sites\n\n| test-company | https://test-company.com |\n")

        result = run_gates(success_assessment_content, tmp_path)
        assert result["detected_template"] == "success"
        assert "correct_template" in result["gates"]
        assert "heading_and_slug" in result["gates"]
        assert "strategy_valid" in result["gates"]
        assert "platform_valid" in result["gates"]
        assert "data_source_concrete" in result["gates"]
        assert "discovery_actionable" in result["gates"]
        assert "category_tree_complete" in result["gates"]
        assert "price_verified" in result["gates"]
        assert "spec_table_verified" in result["gates"]
        assert "product_count" in result["gates"]
        assert "knowledgebase_updated" in result["gates"]
        assert "anti_bot_value" in result["gates"]
        assert len(result["gates"]) == 12

    def test_stop_template_gates(self, stop_assessment_content, tmp_path):
        result = run_gates(stop_assessment_content, tmp_path)
        assert result["detected_template"] == "stop"
        assert "stop_template" in result["gates"]
        assert "valid_stop_reason" in result["gates"]
        assert "findings_explain" in result["gates"]
        assert len(result["gates"]) == 3

    def test_unknown_template(self, tmp_path):
        content = "# Random Document\n\nNo template markers.\n"
        result = run_gates(content, tmp_path)
        assert result["detected_template"] == "unknown"
        assert result["failed"] == 1
        assert len(result["issues"]) == 1

    def test_all_success_gates_pass(self, success_assessment_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text("## Sites\n\n| test-company | https://test-company.com |\n")

        result = run_gates(success_assessment_content, tmp_path)
        assert result["passed"] == 12
        assert result["failed"] == 0
        assert result["issues"] == []

    def test_all_stop_gates_pass(self, stop_assessment_content, tmp_path):
        result = run_gates(stop_assessment_content, tmp_path)
        assert result["passed"] == 3
        assert result["failed"] == 0
        assert result["issues"] == []

    def test_issues_populated_on_failure(self, tmp_path):
        content = textwrap.dedent("""\
            # Catalog Assessment: Test

            **Slug:** test
            **Scraping strategy:** invalid_strategy
            **Platform:** invalid_platform
            **Anti-bot:** severe

            ## Extraction Blueprint

            ### Data Source

            **Primary method:** unknown

            ### Product Discovery

            **Discovery method:** manual
        """)
        result = run_gates(content, tmp_path)
        assert result["detected_template"] == "success"
        assert result["failed"] > 0
        assert len(result["issues"]) > 0

    def test_result_structure(self, success_assessment_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text("## Sites\n\n| test-company | https://test-company.com |\n")

        result = run_gates(success_assessment_content, tmp_path)
        assert "file" in result
        assert "detected_template" in result
        assert "gates" in result
        assert "passed" in result
        assert "failed" in result
        assert "issues" in result


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
