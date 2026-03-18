# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Unit tests for validate_report.py company report validation gates."""
from __future__ import annotations

import json
import subprocess
import sys
import textwrap
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from validate_report import (
    check_all_ids_in_taxonomy,
    check_primary_in_subcategories,
    check_primary_valid,
    check_product_lines,
    check_references,
    check_sections_present,
    check_slug_present,
    check_subcategories_valid,
    extract_field,
    extract_primary_id,
    extract_subcategory_ids,
    parse_taxonomy_ids,
    run_gates,
)

# Path to the real taxonomy file used by the pipeline
CATEGORIES_FILE = (
    Path(__file__).resolve().parents[4] / "docs" / "product-taxonomy" / "categories.md"
)


def _load_real_taxonomy() -> dict[str, str]:
    """Load the actual categories.md taxonomy for validation tests."""
    return parse_taxonomy_ids(CATEGORIES_FILE)


# ---------------------------------------------------------------------------
# Realistic company report fixture
# ---------------------------------------------------------------------------

VALID_REPORT = textwrap.dedent("""\
    # Company Profile: Harlow Bros

    **Slug:** harlowbros
    **Website:** https://www.harlowbros.co.uk
    **Discovery date:** 2026-03-18

    ## Overview

    Harlow Bros is a timber merchant and building materials supplier based in the UK.

    **Entity type:** Company

    ## Business Classification

    | Attribute | Value |
    |-----------|-------|
    | Subcategories | `wood.softwood_hardwood_lumber` (Softwood & Hardwood Lumber), `wood.plywood_engineered_panels` (Plywood & Engineered Wood Panels), `wood.flooring_decking` (Wood Flooring & Decking) |
    | Primary | `wood.softwood_hardwood_lumber` (Softwood & Hardwood Lumber) |
    | Business model | B2B2C |
    | Target market | Builders, contractors |

    ## Products

    ### Timber & Joinery Wood

    Building grade timber, joinery timber, sawn timber, and specialist hardwoods.

    ### Sheet Materials & MDF

    Plywood, chipboard, OSB boards, MDF, and melamine boards.

    ### Flooring & Decking

    Timber floorboards, engineered wood flooring, and composite decking.

    ## Product Catalog Analysis (Preliminary)

    **Has structured catalog:** Yes
    **Estimated catalog size:** 2,000-5,000 products

    ## Findings

    - Harlow Bros is a well-established timber merchant.
    - They offer a wide range of products.

    ## References

    - [Harlow Bros Homepage](https://www.harlowbros.co.uk)
    - [Shop All Products](https://www.harlowbros.co.uk/shop)
    - [Timber Products](https://www.harlowbros.co.uk/timber)
""")


# ---------------------------------------------------------------------------
# extract_field
# ---------------------------------------------------------------------------


class TestExtractField:
    def test_extract_slug(self):
        assert extract_field(VALID_REPORT, "Slug") == "harlowbros"

    def test_extract_website(self):
        assert extract_field(VALID_REPORT, "Website") == "https://www.harlowbros.co.uk"

    def test_extract_discovery_date(self):
        assert extract_field(VALID_REPORT, "Discovery date") == "2026-03-18"

    def test_missing_field_returns_none(self):
        assert extract_field(VALID_REPORT, "Nonexistent") is None

    def test_empty_content(self):
        assert extract_field("", "Slug") is None


# ---------------------------------------------------------------------------
# extract_primary_id
# ---------------------------------------------------------------------------


class TestExtractPrimaryId:
    def test_extracts_primary_from_table(self):
        assert extract_primary_id(VALID_REPORT) == "wood.softwood_hardwood_lumber"

    def test_no_primary_returns_none(self):
        content = "## Business Classification\n\nSome text without a Primary row."
        assert extract_primary_id(content) is None

    def test_primary_with_dotted_id(self):
        content = "| Primary | `construction.cement_concrete` (Cement) |"
        assert extract_primary_id(content) == "construction.cement_concrete"


# ---------------------------------------------------------------------------
# extract_subcategory_ids
# ---------------------------------------------------------------------------


class TestExtractSubcategoryIds:
    def test_extracts_all_ids(self):
        ids = extract_subcategory_ids(VALID_REPORT)
        assert "wood.softwood_hardwood_lumber" in ids
        assert "wood.plywood_engineered_panels" in ids
        assert "wood.flooring_decking" in ids
        assert len(ids) == 3

    def test_no_subcategories_row(self):
        content = "## Business Classification\n\nNo table here."
        assert extract_subcategory_ids(content) == []

    def test_single_subcategory(self):
        content = "| Subcategories | `food.dairy` (Dairy Products) |"
        ids = extract_subcategory_ids(content)
        assert ids == ["food.dairy"]


# ---------------------------------------------------------------------------
# parse_taxonomy_ids — using real categories.md
# ---------------------------------------------------------------------------


class TestParseTaxonomyIds:
    def test_loads_real_taxonomy(self):
        taxonomy = _load_real_taxonomy()
        assert len(taxonomy) > 50  # we know there are many entries
        assert "wood.softwood_hardwood_lumber" in taxonomy
        assert "food.dairy" in taxonomy
        assert "construction.cement_concrete" in taxonomy

    def test_taxonomy_values_are_display_names(self):
        taxonomy = _load_real_taxonomy()
        assert taxonomy["wood.softwood_hardwood_lumber"] == "Softwood & Hardwood Lumber"
        assert taxonomy["food.dairy"] == "Dairy Products"

    def test_no_empty_ids(self):
        taxonomy = _load_real_taxonomy()
        for tid in taxonomy:
            assert tid, "Taxonomy ID should not be empty"
            assert "." in tid, f"Taxonomy ID should contain a dot: {tid}"


# ---------------------------------------------------------------------------
# Gate: check_sections_present
# ---------------------------------------------------------------------------


class TestCheckSectionsPresent:
    def test_all_sections_present(self):
        result = check_sections_present(VALID_REPORT)
        assert result["pass"] is True
        assert "All 6" in result["details"]

    def test_missing_overview(self):
        content = VALID_REPORT.replace("## Overview", "## About")
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Overview" in result["details"]

    def test_missing_multiple_sections(self):
        content = VALID_REPORT.replace("## Overview", "## About").replace(
            "## References", "## Sources"
        )
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Overview" in result["details"]
        assert "References" in result["details"]

    def test_missing_findings(self):
        content = VALID_REPORT.replace("## Findings", "## Analysis")
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Findings" in result["details"]

    def test_missing_business_classification(self):
        content = VALID_REPORT.replace("## Business Classification", "## Classification")
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Business Classification" in result["details"]

    def test_missing_products(self):
        content = VALID_REPORT.replace("## Products", "## Product Lines")
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Products" in result["details"]

    def test_missing_catalog_analysis(self):
        content = VALID_REPORT.replace(
            "## Product Catalog Analysis (Preliminary)",
            "## Catalog Info"
        )
        result = check_sections_present(content)
        assert result["pass"] is False
        assert "Product Catalog Analysis (Preliminary)" in result["details"]

    def test_empty_content(self):
        result = check_sections_present("")
        assert result["pass"] is False


# ---------------------------------------------------------------------------
# Gate: check_primary_valid — using real taxonomy
# ---------------------------------------------------------------------------


class TestCheckPrimaryValid:
    def test_valid_primary(self):
        taxonomy = _load_real_taxonomy()
        result = check_primary_valid(VALID_REPORT, taxonomy)
        assert result["pass"] is True
        assert "wood.softwood_hardwood_lumber" in result["details"]

    def test_invalid_primary(self):
        taxonomy = _load_real_taxonomy()
        content = VALID_REPORT.replace(
            "`wood.softwood_hardwood_lumber` (Softwood & Hardwood Lumber) |",
            "`wood.nonexistent_category` (Fake) |",
        )
        # Also update the Subcategories row
        content = content.replace(
            "| Primary | `wood.softwood_hardwood_lumber` (Softwood & Hardwood Lumber) |",
            "| Primary | `wood.nonexistent_category` (Fake) |",
        )
        result = check_primary_valid(content, taxonomy)
        assert result["pass"] is False
        assert "NOT in categories.md" in result["details"]

    def test_no_primary_found(self):
        taxonomy = _load_real_taxonomy()
        content = "## Business Classification\n\nNo table here."
        result = check_primary_valid(content, taxonomy)
        assert result["pass"] is False
        assert "No Primary" in result["details"]


# ---------------------------------------------------------------------------
# Gate: check_subcategories_valid — using real taxonomy
# ---------------------------------------------------------------------------


class TestCheckSubcategoriesValid:
    def test_all_valid_subcategories(self):
        taxonomy = _load_real_taxonomy()
        result = check_subcategories_valid(VALID_REPORT, taxonomy)
        assert result["pass"] is True
        assert "3" in result["details"]

    def test_one_invalid_subcategory(self):
        taxonomy = _load_real_taxonomy()
        content = VALID_REPORT.replace(
            "`wood.flooring_decking` (Wood Flooring & Decking)",
            "`wood.fake_subcategory` (Fake)"
        )
        result = check_subcategories_valid(content, taxonomy)
        assert result["pass"] is False
        assert "wood.fake_subcategory" in result["details"]

    def test_no_subcategories(self):
        taxonomy = _load_real_taxonomy()
        content = "## Business Classification\n\nNo subcategories row."
        result = check_subcategories_valid(content, taxonomy)
        assert result["pass"] is False
        assert "No taxonomy IDs" in result["details"]


# ---------------------------------------------------------------------------
# Gate: check_all_ids_in_taxonomy — using real taxonomy
# ---------------------------------------------------------------------------


class TestCheckAllIdsInTaxonomy:
    def test_all_ids_valid(self):
        taxonomy = _load_real_taxonomy()
        result = check_all_ids_in_taxonomy(VALID_REPORT, taxonomy)
        assert result["pass"] is True

    def test_invented_id(self):
        taxonomy = _load_real_taxonomy()
        content = VALID_REPORT.replace(
            "`wood.plywood_engineered_panels` (Plywood & Engineered Wood Panels)",
            "`wood.invented_panels` (Invented Panels)"
        )
        result = check_all_ids_in_taxonomy(content, taxonomy)
        assert result["pass"] is False
        assert "wood.invented_panels" in result["details"]


# ---------------------------------------------------------------------------
# Gate: check_slug_present
# ---------------------------------------------------------------------------


class TestCheckSlugPresent:
    def test_slug_present(self):
        result = check_slug_present(VALID_REPORT)
        assert result["pass"] is True
        assert "harlowbros" in result["details"]

    def test_slug_missing(self):
        content = VALID_REPORT.replace("**Slug:** harlowbros", "")
        result = check_slug_present(content)
        assert result["pass"] is False
        assert "missing" in result["details"].lower()

    def test_slug_different_value(self):
        content = VALID_REPORT.replace("**Slug:** harlowbros", "**Slug:** timber-co")
        result = check_slug_present(content)
        assert result["pass"] is True
        assert "timber-co" in result["details"]


# ---------------------------------------------------------------------------
# Gate: check_product_lines
# ---------------------------------------------------------------------------


class TestCheckProductLines:
    def test_product_lines_present(self):
        result = check_product_lines(VALID_REPORT)
        assert result["pass"] is True
        assert "3" in result["details"]  # 3 ### subsections

    def test_no_subsections(self):
        content = textwrap.dedent("""\
            ## Products

            Just some text without any ### subsections.

            ## Findings

            Some findings.
        """)
        result = check_product_lines(content)
        assert result["pass"] is False
        assert "No ###" in result["details"]

    def test_no_products_section(self):
        content = "## Overview\n\nSome content.\n\n## Findings\n\nFindings."
        result = check_product_lines(content)
        assert result["pass"] is False
        assert "not found" in result["details"].lower()

    def test_single_subsection(self):
        content = textwrap.dedent("""\
            ## Products

            ### Main Product Line

            Description of the main product line.

            ## Findings

            Some findings.
        """)
        result = check_product_lines(content)
        assert result["pass"] is True
        assert "1" in result["details"]

    def test_products_at_end_of_document(self):
        """Products section at end of file (no following ## section)."""
        content = textwrap.dedent("""\
            ## Products

            ### Product A

            Description A.

            ### Product B

            Description B.
        """)
        result = check_product_lines(content)
        assert result["pass"] is True
        assert "2" in result["details"]


# ---------------------------------------------------------------------------
# Gate: check_references
# ---------------------------------------------------------------------------


class TestCheckReferences:
    def test_sufficient_references(self):
        result = check_references(VALID_REPORT)
        assert result["pass"] is True
        assert "3" in result["details"]

    def test_no_references_section(self):
        content = "## Overview\n\nContent.\n\n## Findings\n\nFindings."
        result = check_references(content)
        assert result["pass"] is False
        assert "not found" in result["details"].lower()

    def test_only_one_reference(self):
        content = textwrap.dedent("""\
            ## References

            - [Homepage](https://www.example.com)

            ## Findings

            Stuff.
        """)
        result = check_references(content)
        assert result["pass"] is False
        assert "1" in result["details"]

    def test_exactly_two_references(self):
        content = textwrap.dedent("""\
            ## References

            - [Homepage](https://www.example.com)
            - [Shop](https://www.example.com/shop)
        """)
        result = check_references(content)
        assert result["pass"] is True
        assert "2" in result["details"]

    def test_references_without_markdown_links(self):
        content = textwrap.dedent("""\
            ## References

            - https://www.example.com
            - https://www.example.com/shop
        """)
        result = check_references(content)
        assert result["pass"] is False
        assert "0" in result["details"]

    def test_references_at_end_of_document(self):
        """References section at end of file (no following ## section)."""
        content = textwrap.dedent("""\
            ## References

            - [Link A](https://www.a.com)
            - [Link B](https://www.b.com)
            - [Link C](https://www.c.com)
        """)
        result = check_references(content)
        assert result["pass"] is True


# ---------------------------------------------------------------------------
# Gate: check_primary_in_subcategories
# ---------------------------------------------------------------------------


class TestCheckPrimaryInSubcategories:
    def test_primary_in_subcategories(self):
        result = check_primary_in_subcategories(VALID_REPORT)
        assert result["pass"] is True
        assert "wood.softwood_hardwood_lumber" in result["details"]

    def test_primary_not_in_subcategories(self):
        content = textwrap.dedent("""\
            ## Business Classification

            | Attribute | Value |
            |-----------|-------|
            | Subcategories | `wood.plywood_engineered_panels` (Plywood), `wood.flooring_decking` (Flooring) |
            | Primary | `wood.softwood_hardwood_lumber` (Softwood & Hardwood Lumber) |
        """)
        result = check_primary_in_subcategories(content)
        assert result["pass"] is False
        assert "not found" in result["details"].lower()

    def test_no_primary_id(self):
        content = "## Business Classification\n\nNo primary row."
        result = check_primary_in_subcategories(content)
        assert result["pass"] is False
        assert "Cannot check" in result["details"]


# ---------------------------------------------------------------------------
# run_gates — integration
# ---------------------------------------------------------------------------


class TestRunGates:
    def test_valid_report_all_pass(self):
        taxonomy = _load_real_taxonomy()
        result = run_gates(VALID_REPORT, taxonomy)
        assert result["passed"] == 8
        assert result["failed"] == 0
        assert result["issues"] == []
        assert "file" in result
        assert "gates" in result

    def test_all_gate_names_present(self):
        taxonomy = _load_real_taxonomy()
        result = run_gates(VALID_REPORT, taxonomy)
        expected_gates = {
            "sections_present",
            "primary_valid",
            "subcategories_valid",
            "all_ids_in_taxonomy",
            "slug_present",
            "product_lines",
            "references",
            "primary_in_subcategories",
        }
        assert set(result["gates"].keys()) == expected_gates

    def test_empty_report_fails_gates(self):
        taxonomy = _load_real_taxonomy()
        result = run_gates("", taxonomy)
        assert result["failed"] > 0
        # all_ids_in_taxonomy passes on empty content because there are
        # zero IDs and zero of them are invalid, so 1 gate passes
        assert result["passed"] == 1
        assert result["failed"] == 7

    def test_report_with_invalid_taxonomy(self):
        taxonomy = _load_real_taxonomy()
        content = VALID_REPORT.replace(
            "`wood.softwood_hardwood_lumber`",
            "`wood.invented_category`",
        )
        result = run_gates(content, taxonomy)
        # primary_valid, subcategories_valid, all_ids_in_taxonomy,
        # primary_in_subcategories should fail
        assert result["failed"] > 0
        assert len(result["issues"]) > 0

    def test_issues_list_populated_on_failure(self):
        taxonomy = _load_real_taxonomy()
        content = VALID_REPORT.replace("**Slug:** harlowbros", "")
        result = run_gates(content, taxonomy)
        failing_gates = [
            name for name, g in result["gates"].items() if g["pass"] is False
        ]
        assert "slug_present" in failing_gates
        assert any("slug_present" in issue for issue in result["issues"])


# ---------------------------------------------------------------------------
# CLI entrypoint (main)
# ---------------------------------------------------------------------------


class TestMainCLI:
    def test_cli_with_valid_report(self, tmp_path):
        report_file = tmp_path / "test_report.md"
        report_file.write_text(VALID_REPORT)
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "validate_report.py"
        )
        result = subprocess.run(
            [
                sys.executable,
                script,
                str(report_file),
                "--categories-file",
                str(CATEGORIES_FILE),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert data["passed"] == 8

    def test_cli_with_nonexistent_file(self):
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "validate_report.py"
        )
        result = subprocess.run(
            [sys.executable, script, "/nonexistent/report.md"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 2

    def test_cli_output_json(self, tmp_path):
        report_file = tmp_path / "test_report.md"
        report_file.write_text(VALID_REPORT)
        output_file = tmp_path / "output" / "result.json"
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "validate_report.py"
        )
        result = subprocess.run(
            [
                sys.executable,
                script,
                str(report_file),
                "--categories-file",
                str(CATEGORIES_FILE),
                "--output-json",
                str(output_file),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        assert output_file.exists()
        data = json.loads(output_file.read_text())
        assert data["passed"] == 8

    def test_cli_empty_file(self, tmp_path):
        report_file = tmp_path / "empty.md"
        report_file.write_text("")
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "validate_report.py"
        )
        result = subprocess.run(
            [
                sys.executable,
                script,
                str(report_file),
                "--categories-file",
                str(CATEGORIES_FILE),
            ],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 2


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
