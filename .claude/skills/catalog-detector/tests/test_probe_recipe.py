# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest", "httpx", "selectolax"]
# ///
"""Tests for probe_recipe.py — knowledgebase parsing, recipe verification, match scoring."""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from probe_recipe import (
    compute_recipe_match,
    extract_md_section,
    parse_knowledgebase,
)


# ---------------------------------------------------------------------------
# extract_md_section
# ---------------------------------------------------------------------------


class TestExtractMdSection:
    def test_extract_existing_section(self):
        content = textwrap.dedent("""\
            # Title

            ## CSS Selectors

            Some CSS content here.
            More content.

            ## JSON-LD Patterns

            JSON-LD info here.
        """)
        result = extract_md_section(content, "CSS Selectors")
        assert result is not None
        assert "Some CSS content here." in result
        assert "More content." in result

    def test_extract_last_section(self):
        content = textwrap.dedent("""\
            ## First Section

            First content.

            ## Last Section

            Last content.
        """)
        result = extract_md_section(content, "Last Section")
        assert result is not None
        assert "Last content." in result

    def test_missing_section_returns_none(self):
        content = "## Other Section\n\nContent here.\n"
        result = extract_md_section(content, "Missing Section")
        assert result is None

    def test_empty_content(self):
        assert extract_md_section("", "Any") is None

    def test_section_with_special_chars(self):
        content = "## Spec Table / Attributes\n\nContent here.\n"
        result = extract_md_section(content, "Spec Table / Attributes")
        assert result is not None
        assert "Content here." in result


# ---------------------------------------------------------------------------
# parse_knowledgebase
# ---------------------------------------------------------------------------


class TestParseKnowledgebase:
    def test_full_knowledgebase(self, sample_knowledgebase_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text(sample_knowledgebase_content)

        result = parse_knowledgebase(kb_file)

        assert len(result["css_selectors"]) == 3
        assert result["css_selectors"][0]["element"] == "Product Title"
        assert result["css_selectors"][0]["selector"] == ".product-title"
        assert result["css_selectors"][1]["selector"] == ".price"

    def test_json_ld_types(self, sample_knowledgebase_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text(sample_knowledgebase_content)

        result = parse_knowledgebase(kb_file)
        assert "Product" in result["json_ld_types"]
        assert "BreadcrumbList" in result["json_ld_types"]

    def test_pagination(self, sample_knowledgebase_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text(sample_knowledgebase_content)

        result = parse_knowledgebase(kb_file)
        assert result["pagination_url_pattern"] == "?page={n}"
        assert result["products_per_page"] == 24

    def test_api_endpoints(self, sample_knowledgebase_content, tmp_path):
        kb_file = tmp_path / "shopify.md"
        kb_file.write_text(sample_knowledgebase_content)

        result = parse_knowledgebase(kb_file)
        assert len(result["api_endpoints"]) == 2
        assert any("/products/" in ep for ep in result["api_endpoints"])

    def test_missing_sections(self, tmp_path):
        kb_file = tmp_path / "empty.md"
        kb_file.write_text("# Empty Knowledgebase\n\nNo relevant sections here.\n")

        result = parse_knowledgebase(kb_file)
        assert result["css_selectors"] == []
        assert result["json_ld_types"] == []
        assert result["pagination_url_pattern"] is None
        assert result["products_per_page"] is None
        assert result["api_endpoints"] == []

    def test_css_table_skips_header(self, tmp_path):
        content = textwrap.dedent("""\
            ## CSS Selectors

            | Element | Selector | Notes |
            |---------|----------|-------|
            | Title | `.title` | Main heading |
        """)
        kb_file = tmp_path / "test.md"
        kb_file.write_text(content)

        result = parse_knowledgebase(kb_file)
        assert len(result["css_selectors"]) == 1
        assert result["css_selectors"][0]["selector"] == ".title"

    def test_css_table_skips_separator(self, tmp_path):
        """Separator rows with --- should be skipped."""
        content = textwrap.dedent("""\
            ## CSS Selectors

            | Element | Selector | Notes |
            |---------|----------|-------|
            | Price | `.amount` | |
        """)
        kb_file = tmp_path / "test.md"
        kb_file.write_text(content)

        result = parse_knowledgebase(kb_file)
        assert len(result["css_selectors"]) == 1


# ---------------------------------------------------------------------------
# compute_recipe_match
# ---------------------------------------------------------------------------


class TestComputeRecipeMatch:
    def test_untested_no_checks(self):
        assert compute_recipe_match([], {}) == "untested"

    def test_untested_all_non_200(self):
        checks = [
            {"status": 403, "json_ld_found": False, "css_checks": []},
            {"status": 500, "json_ld_found": False, "css_checks": []},
        ]
        assert compute_recipe_match(checks, {}) == "untested"

    def test_full_match(self):
        checks = [
            {
                "status": 200,
                "json_ld_found": True,
                "css_checks": [
                    {"selector": ".title", "found": True},
                    {"selector": ".price", "found": True},
                ],
            },
        ]
        pagination = {"tested": True, "next_page_found": True}
        assert compute_recipe_match(checks, pagination) == "full"

    def test_partial_match(self):
        checks = [
            {
                "status": 200,
                "json_ld_found": True,
                "css_checks": [
                    {"selector": ".title", "found": True},
                    {"selector": ".price", "found": False},
                ],
            },
        ]
        pagination = {"tested": False}
        assert compute_recipe_match(checks, pagination) == "partial"

    def test_poor_match(self):
        checks = [
            {
                "status": 200,
                "json_ld_found": False,
                "css_checks": [
                    {"selector": ".title", "found": False},
                    {"selector": ".price", "found": False},
                ],
            },
        ]
        pagination = {"tested": False}
        assert compute_recipe_match(checks, pagination) == "poor"

    def test_full_ratio_but_no_pagination(self):
        """100% ratio but pagination not tested -> partial (not full)."""
        checks = [
            {
                "status": 200,
                "json_ld_found": True,
                "css_checks": [
                    {"selector": ".title", "found": True},
                ],
            },
        ]
        pagination = {"tested": False}
        assert compute_recipe_match(checks, pagination) == "partial"

    def test_full_ratio_pagination_tested_no_next(self):
        """100% ratio, pagination tested but no next page -> partial."""
        checks = [
            {
                "status": 200,
                "json_ld_found": True,
                "css_checks": [
                    {"selector": ".title", "found": True},
                ],
            },
        ]
        pagination = {"tested": True, "next_page_found": False}
        assert compute_recipe_match(checks, pagination) == "partial"

    def test_mixed_statuses(self):
        """Some 200, some non-200 — only 200 responses count."""
        checks = [
            {
                "status": 200,
                "json_ld_found": True,
                "css_checks": [{"selector": ".title", "found": True}],
            },
            {
                "status": 403,
                "json_ld_found": False,
                "css_checks": [],
            },
        ]
        pagination = {"tested": True, "next_page_found": True}
        assert compute_recipe_match(checks, pagination) == "full"

    def test_boundary_half_ratio(self):
        """Exactly 50% passes -> NOT partial (needs > 0.5)."""
        checks = [
            {
                "status": 200,
                "json_ld_found": False,  # fails
                "css_checks": [{"selector": ".title", "found": True}],  # passes
            },
        ]
        # total_checks = 2 (1 for json_ld, 1 for css), passed = 1
        # ratio = 1/2 = 0.5, not > 0.5
        pagination = {"tested": False}
        assert compute_recipe_match(checks, pagination) == "poor"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
