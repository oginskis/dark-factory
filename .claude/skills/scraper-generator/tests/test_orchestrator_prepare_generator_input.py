# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Unit tests for orchestrator_prepare_generator_input.py — SKU schema pre-processing."""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from orchestrator_prepare_generator_input import (
    extract_routing_table,
    find_schema_file,
    parse_schema_table,
    slugify_display_name,
    SCHEMAS_DIR,
    TAXONOMY_FILE,
    TYPE_MAP,
    UNIVERSAL_KEYS,
)


# ---------------------------------------------------------------------------
# slugify_display_name
# ---------------------------------------------------------------------------


class TestSlugifyDisplayName:
    """Verify taxonomy display names convert to schema filename slugs."""

    def test_ampersand_removal(self):
        assert slugify_display_name("Softwood & Hardwood Lumber") == "softwood-hardwood-lumber"

    def test_parentheses_and_commas(self):
        result = slugify_display_name(
            "Plywood & Engineered Wood Panels (OSB, Particle Board)"
        )
        assert result == "plywood-engineered-wood-panels-osb-particle-board"

    def test_simple_name(self):
        assert slugify_display_name("Dairy Products") == "dairy-products"

    def test_slash_removal(self):
        assert slugify_display_name("Audio / Video Equipment") == "audio-video-equipment"

    def test_leading_trailing_whitespace(self):
        assert slugify_display_name("  Foam Products  ") == "foam-products"

    def test_multiple_spaces_collapse(self):
        assert slugify_display_name("Big   Spaced   Name") == "big-spaced-name"

    def test_multiple_ampersands(self):
        result = slugify_display_name("A & B & C")
        assert result == "a-b-c"

    def test_empty_string(self):
        assert slugify_display_name("") == ""

    def test_no_special_chars(self):
        assert slugify_display_name("Books") == "books"

    def test_complex_parenthetical(self):
        result = slugify_display_name(
            "Machine Tools (Lathes, Mills, Grinders)"
        )
        assert result == "machine-tools-lathes-mills-grinders"

    def test_millwork_with_parenthetical(self):
        result = slugify_display_name("Millwork (Moldings, Trim, Staircases)")
        assert result == "millwork-moldings-trim-staircases"


# ---------------------------------------------------------------------------
# parse_schema_table
# ---------------------------------------------------------------------------


class TestParseSchemaTable:
    """Verify markdown table parsing from SKU schema files."""

    SAMPLE_SCHEMA = textwrap.dedent("""\
        # SKU Schema: Test Product

        **Last updated:** 2026-03-15

        ## Core Attributes

        | Attribute | Key | Data Type | Unit | Description | Example Values |
        |--------|--------|--------|--------|--------|--------|
        | SKU | sku | text | — | Product identifier | ABC-123 |
        | Product Name | product_name | text | — | Full product name | Widget Pro |
        | Price | price | number | — | Numeric price | 19.99 |
        | Widget Type | widget_type | enum | — | Category of widget | Type A, Type B |
        | Weight | weight | number | kg | Product weight | 2.5, 5.0 |

        ## Extended Attributes

        | Attribute | Key | Data Type | Unit | Description | Example Values |
        |--------|--------|--------|--------|--------|--------|
        | Color | color | text | — | Primary color | Red, Blue |
        | Material | material | text (list) | — | Construction material | Steel, Aluminum |

        ## Changelog

        | Date | Change | Sources |
        |------|--------|---------|
        | 2026-03-15 | Initial schema | N/A |
    """)

    def test_core_attributes_row_count(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Core Attributes")
        assert len(rows) == 5

    def test_core_attributes_keys(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Core Attributes")
        keys = [r["Key"] for r in rows]
        assert keys == ["sku", "product_name", "price", "widget_type", "weight"]

    def test_core_attributes_data_types(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Core Attributes")
        types = {r["Key"]: r["Data Type"] for r in rows}
        assert types["sku"] == "text"
        assert types["price"] == "number"
        assert types["widget_type"] == "enum"

    def test_extended_attributes_row_count(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Extended Attributes")
        assert len(rows) == 2

    def test_extended_attributes_keys(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Extended Attributes")
        keys = [r["Key"] for r in rows]
        assert keys == ["color", "material"]

    def test_extended_text_list_type(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Extended Attributes")
        material_row = [r for r in rows if r["Key"] == "material"][0]
        assert material_row["Data Type"] == "text (list)"

    def test_nonexistent_section_returns_empty(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Nonexistent Section")
        assert rows == []

    def test_changelog_section(self):
        """Changelog section has different columns — should still parse."""
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Changelog")
        assert len(rows) == 1
        assert "Date" in rows[0]

    def test_empty_content(self):
        rows = parse_schema_table("", "Core Attributes")
        assert rows == []

    def test_section_with_no_table(self):
        content = "## Core Attributes\n\nNo table here.\n\n## Extended Attributes\n"
        rows = parse_schema_table(content, "Core Attributes")
        assert rows == []

    def test_section_with_only_header_and_separator(self):
        content = textwrap.dedent("""\
            ## Core Attributes

            | Col1 | Col2 |
            |------|------|

            ## Extended Attributes
        """)
        rows = parse_schema_table(content, "Core Attributes")
        assert rows == []

    def test_preserves_all_columns(self):
        rows = parse_schema_table(self.SAMPLE_SCHEMA, "Core Attributes")
        first_row = rows[0]
        assert "Attribute" in first_row
        assert "Key" in first_row
        assert "Data Type" in first_row
        assert "Unit" in first_row
        assert "Description" in first_row
        assert "Example Values" in first_row


# ---------------------------------------------------------------------------
# extract_routing_table
# ---------------------------------------------------------------------------


class TestExtractRoutingTable:
    """Verify routing table extraction from schema files."""

    def _write_schema(self, tmp_path: Path, content: str) -> Path:
        schema_file = tmp_path / "test-schema.md"
        schema_file.write_text(content, encoding="utf-8")
        return schema_file

    SAMPLE_SCHEMA = textwrap.dedent("""\
        # SKU Schema: Test Product

        ## Core Attributes

        | Attribute | Key | Data Type | Unit | Description | Example Values |
        |--------|--------|--------|--------|--------|--------|
        | SKU | sku | text | — | Product identifier | ABC-123 |
        | Product Name | product_name | text | — | Full product name | Widget Pro |
        | URL | url | text | — | Product URL | https://example.com |
        | Price | price | number | — | Numeric price | 19.99 |
        | Currency | currency | text | — | Currency code | USD |
        | Brand | brand | text | — | Brand name | Acme |
        | Widget Type | widget_type | enum | — | Category of widget | Type A, Type B |
        | Weight | weight | number | kg | Product weight | 2.5 |

        ## Extended Attributes

        | Attribute | Key | Data Type | Unit | Description | Example Values |
        |--------|--------|--------|--------|--------|--------|
        | Color | color | text | — | Primary color | Red, Blue |
        | Tags | tags | text (list) | — | Product tags | Indoor, Outdoor |
        | Is Active | is_active | boolean | — | Whether product is active | true, false |
    """)

    def test_core_keys_exclude_universal(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        # sku, product_name, url, price, currency, brand are all UNIVERSAL_KEYS
        assert "sku" not in result["core_attribute_keys"]
        assert "product_name" not in result["core_attribute_keys"]
        assert "url" not in result["core_attribute_keys"]
        assert "price" not in result["core_attribute_keys"]
        assert "currency" not in result["core_attribute_keys"]
        assert "brand" not in result["core_attribute_keys"]
        # Non-universal core keys should be present
        assert "widget_type" in result["core_attribute_keys"]
        assert "weight" in result["core_attribute_keys"]

    def test_extended_keys(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert "color" in result["extended_attribute_keys"]
        assert "tags" in result["extended_attribute_keys"]
        assert "is_active" in result["extended_attribute_keys"]

    def test_type_mapping_enum(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["widget_type"] == "str"

    def test_type_mapping_number(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["weight"] == "number"

    def test_type_mapping_text(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["color"] == "str"

    def test_type_mapping_text_list(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["tags"] == "list"

    def test_type_mapping_boolean(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["is_active"] == "bool"

    def test_structure_has_four_keys(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert set(result.keys()) == {"core_attribute_keys", "extended_attribute_keys", "attribute_types", "units"}

    def test_units_extracted(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert result["units"]["weight"] == "kg"

    def test_units_skips_dash(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert "widget_type" not in result["units"]
        assert "color" not in result["units"]

    def test_units_skips_universal_keys(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        assert "price" not in result["units"]

    def test_empty_schema(self, tmp_path):
        schema_file = self._write_schema(tmp_path, "# Empty Schema\n")
        result = extract_routing_table(schema_file)
        assert result["core_attribute_keys"] == []
        assert result["extended_attribute_keys"] == []
        assert result["attribute_types"] == {}

    def test_universal_keys_not_in_types(self, tmp_path):
        schema_file = self._write_schema(tmp_path, self.SAMPLE_SCHEMA)
        result = extract_routing_table(schema_file)
        for key in UNIVERSAL_KEYS:
            assert key not in result["attribute_types"]

    def test_unknown_data_type_defaults_to_str(self, tmp_path):
        content = textwrap.dedent("""\
            ## Core Attributes

            | Attribute | Key | Data Type | Unit | Description | Example Values |
            |--------|--------|--------|--------|--------|--------|
            | Foo | foo | weird_type | — | Some attr | bar |
        """)
        schema_file = self._write_schema(tmp_path, content)
        result = extract_routing_table(schema_file)
        assert result["attribute_types"]["foo"] == "str"


# ---------------------------------------------------------------------------
# extract_routing_table — integration with real schema files
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestExtractRoutingTableIntegration:
    """Integration tests using actual SKU schema files from the repository."""

    def test_softwood_hardwood_lumber_core_keys(self):
        schema_path = SCHEMAS_DIR / "softwood-hardwood-lumber.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        # Core keys from the actual schema (excluding universals)
        expected_core = [
            "wood_type",
            "structural_grade",
            "appearance_grade",
            "treatment_type",
            "use_class",
        ]
        assert result["core_attribute_keys"] == expected_core

    def test_softwood_hardwood_lumber_extended_keys(self):
        schema_path = SCHEMAS_DIR / "softwood-hardwood-lumber.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        # Verify some expected extended attributes
        assert "species" in result["extended_attribute_keys"]
        assert "nominal_thickness" in result["extended_attribute_keys"]
        assert "moisture_content" in result["extended_attribute_keys"]
        assert "certification" in result["extended_attribute_keys"]
        assert "janka_hardness" in result["extended_attribute_keys"]

    def test_softwood_hardwood_lumber_types(self):
        schema_path = SCHEMAS_DIR / "softwood-hardwood-lumber.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        assert result["attribute_types"]["wood_type"] == "str"  # enum -> str
        assert result["attribute_types"]["actual_thickness"] == "number"
        assert result["attribute_types"]["application"] == "list"  # text (list) -> list
        assert result["attribute_types"]["certification"] == "list"
        assert result["attribute_types"]["pack_quantity"] == "number"

    def test_softwood_hardwood_lumber_units(self):
        schema_path = SCHEMAS_DIR / "softwood-hardwood-lumber.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        assert "units" in result
        # Numeric attributes with physical units should be present
        assert result["units"].get("actual_thickness") is not None
        assert result["units"].get("actual_width") is not None
        # Enum/text fields should not have units
        assert "wood_type" not in result["units"]
        assert "species" not in result["units"]

    def test_plywood_panels_core_keys(self):
        schema_path = SCHEMAS_DIR / "plywood-engineered-wood-panels-osb-particle-board.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        expected_core = [
            "panel_type",
            "surface_grade_front",
            "surface_grade_back",
            "glue_type",
            "structural_class",
        ]
        assert result["core_attribute_keys"] == expected_core

    def test_plywood_panels_types(self):
        schema_path = SCHEMAS_DIR / "plywood-engineered-wood-panels-osb-particle-board.md"
        if not schema_path.exists():
            pytest.skip("Schema file not present in working tree")
        result = extract_routing_table(schema_path)
        assert result["attribute_types"]["panel_type"] == "str"  # enum -> str
        assert result["attribute_types"]["glue_type"] == "str"  # enum -> str
        assert result["attribute_types"]["thickness"] == "number"
        assert result["attribute_types"]["surface_treatment"] == "str"  # enum -> str


# ---------------------------------------------------------------------------
# find_schema_file
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestFindSchemaFile:
    """Verify taxonomy ID to schema file resolution."""

    def test_softwood_hardwood_lumber(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("wood.softwood_hardwood_lumber")
        assert result is not None
        assert result.name == "softwood-hardwood-lumber.md"

    def test_plywood_engineered_panels(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("wood.plywood_engineered_panels")
        assert result is not None
        assert result.name == "plywood-engineered-wood-panels-osb-particle-board.md"

    def test_flooring_decking(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("wood.flooring_decking")
        if result is not None:
            assert result.exists()

    def test_nonexistent_taxonomy_id(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("fake.nonexistent_category_xyz")
        assert result is None

    def test_dairy_products(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("food.dairy")
        if result is not None:
            assert result.name == "dairy-products.md"
            assert result.exists()

    def test_returned_path_exists(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        result = find_schema_file("wood.softwood_hardwood_lumber")
        assert result is not None
        assert result.exists()
        assert result.is_file()


# ---------------------------------------------------------------------------
# End-to-end: taxonomy ID -> routing table
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestEndToEnd:
    """Verify full pipeline: taxonomy ID -> find schema -> extract routing table."""

    def test_softwood_hardwood_lumber_full_pipeline(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        schema_path = find_schema_file("wood.softwood_hardwood_lumber")
        assert schema_path is not None, "Schema file not found for wood.softwood_hardwood_lumber"
        routing = extract_routing_table(schema_path)

        # Structure check
        assert "core_attribute_keys" in routing
        assert "extended_attribute_keys" in routing
        assert "attribute_types" in routing

        # Core should have non-universal keys
        assert len(routing["core_attribute_keys"]) > 0
        assert "wood_type" in routing["core_attribute_keys"]

        # Extended should have additional detail keys
        assert len(routing["extended_attribute_keys"]) > 0
        assert "species" in routing["extended_attribute_keys"]
        assert "nominal_thickness" in routing["extended_attribute_keys"]

        # Types mapping should cover all core + extended keys
        all_keys = set(routing["core_attribute_keys"]) | set(routing["extended_attribute_keys"])
        assert all_keys == set(routing["attribute_types"].keys())

        # No universal keys should leak through
        for key in UNIVERSAL_KEYS:
            assert key not in routing["core_attribute_keys"]
            assert key not in routing["extended_attribute_keys"]
            assert key not in routing["attribute_types"]

    def test_plywood_panels_full_pipeline(self):
        if not TAXONOMY_FILE.exists():
            pytest.skip("Taxonomy file not present in working tree")
        schema_path = find_schema_file("wood.plywood_engineered_panels")
        assert schema_path is not None, "Schema file not found for wood.plywood_engineered_panels"
        routing = extract_routing_table(schema_path)

        assert "panel_type" in routing["core_attribute_keys"]
        assert routing["attribute_types"]["panel_type"] == "str"
        assert "thickness" in routing["extended_attribute_keys"]
        assert routing["attribute_types"]["thickness"] == "number"

        # Every key in core/extended should have a type entry
        for key in routing["core_attribute_keys"] + routing["extended_attribute_keys"]:
            assert key in routing["attribute_types"], f"Missing type for key: {key}"


# ---------------------------------------------------------------------------
# TYPE_MAP and UNIVERSAL_KEYS constants
# ---------------------------------------------------------------------------


class TestConstants:
    """Verify the module-level constants are correctly defined."""

    def test_type_map_covers_expected_types(self):
        assert TYPE_MAP["text"] == "str"
        assert TYPE_MAP["enum"] == "str"
        assert TYPE_MAP["number"] == "number"
        assert TYPE_MAP["text (list)"] == "list"
        assert TYPE_MAP["boolean"] == "bool"

    def test_universal_keys_include_essentials(self):
        assert "sku" in UNIVERSAL_KEYS
        assert "product_name" in UNIVERSAL_KEYS
        assert "url" in UNIVERSAL_KEYS
        assert "price" in UNIVERSAL_KEYS
        assert "currency" in UNIVERSAL_KEYS
        assert "brand" in UNIVERSAL_KEYS

    def test_universal_keys_is_a_set(self):
        assert isinstance(UNIVERSAL_KEYS, set)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
