# SKU Schema: Fabricated Structural Metalwork

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.fabricated_structural`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Fabricator or distributor product identifier | WF-W8X31-A992-20, STR-COL-HSS6X6-30 |
| Product Name | product_name | text | — | yes | Full product name including section type, size, grade, and length | W8x31 A992 Wide Flange Beam 20ft, HSS 6x6x0.25 A500 Grade B Column 30ft |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/w8x31-a992-wide-flange-beam |
| Price | price | number | — | yes | Numeric unit price (per piece, per foot, or per pound) excluding currency symbol | 320.00, 18.50, 0.85 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Category | product_category | enum | — | — | Primary structural product classification | Wide Flange Beam, I-Beam, Channel, Angle, HSS (Square Tube), HSS (Rectangular Tube), HSS (Round Tube), Plate, Base Plate, Column, Embed Plate, Grating, Stair Tread, Handrail, Ladder, Mezzanine Component, Truss, Joist |
| Steel Grade | steel_grade | text | — | — | Structural steel grade per ASTM, EN, or other standards | A36, A992, A572-50, A500 Grade B, A500 Grade C, A529, A709, EN S275JR, EN S355JR |
| Connection Type | connection_type | text | — | — | Method of field connection for structural members | Bolted, Welded, Bolted Moment, Shear Tab, Clip Angle, End Plate |
| AISC Certification Category | aisc_certification_category | text | — | — | AISC fabricator certification category if applicable | Standard (STD), Intermediate (INT), Major (MJR), Advanced (ADV) |
| Country of Origin | country_of_origin | text | — | — | Country where the material was rolled and/or fabricated | USA, Canada, Mexico, India, South Korea |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Fabricator/Supplier | fabricatorsupplier | text | — | — | Steel fabricator or distributor name | Triple-S Steel, Metals USA, Kloeckner Metals, Nucor, Infra-Metals, Steel Fabricators LLC |
| Section Designation | section_designation | text | — | — | Standard section size designation per AISC or EN | W8x31, W10x22, W12x40, C6x8.2, L3x3x0.25, HSS4x4x0.25, WT5x15, MC6x12 |
| Depth | depth | number | in | — | Nominal depth of the section or height of the member | 4, 6, 8, 10, 12, 14, 18, 24, 36 |
| Flange Width | flange_width | number | in | — | Width of the flange for beams, channels, and tees | 4.0, 5.25, 6.5, 8.0, 10.0, 12.0 |
| Web Thickness | web_thickness | number | in | — | Thickness of the web for rolled sections | 0.170, 0.240, 0.300, 0.375, 0.500 |
| Flange Thickness | flange_thickness | number | in | — | Thickness of the flange for rolled sections | 0.204, 0.345, 0.440, 0.575, 0.750 |
| Wall Thickness | wall_thickness | number | in | — | Wall thickness for HSS tube and pipe sections | 0.125, 0.188, 0.250, 0.313, 0.375, 0.500 |
| Plate Thickness | plate_thickness | number | in | — | Thickness for plate products (base plates, embed plates, grating) | 0.250, 0.375, 0.500, 0.750, 1.000, 2.000 |
| Plate Width | plate_width | number | in | — | Width for plate products | 6, 8, 12, 24, 48, 96 |
| Surface Treatment | surface_treatment | text | — | — | Surface preparation and coating on the fabricated piece | Mill Scale, Sandblasted (SSPC-SP6), Primed, Shop Painted, Hot-Dip Galvanized, Powder Coated, Zinc Rich Primer, Fireproofing |
| Paint System | paint_system | text | — | — | Specific paint or coating system specification | SSPC-PS Guide 12.00, Alkyd Primer, Epoxy Primer, Intumescent Coating |
| Fabrication Details | fabrication_details | text (list) | — | — | Post-rolling fabrication operations performed | Cutting, Drilling, Punching, Welding, Bending, Coping, Cambering, Notching, Slotting |
| Hole Pattern | hole_pattern | text | — | — | Description of bolt hole layout if pre-drilled | Standard Gauge, Short Slotted, Oversized, Custom Per Drawing |
| Weld Specification | weld_specification | text | — | — | Welding procedure standard for shop or field welds | AWS D1.1, AWS D1.8, EN 1090-2 |
| Certification | certification | text (list) | — | — | Fabricator and material certifications | AISC Certified Fabricator, AISC Certified Erector, ISO 9001, EN 1090, CWB (CSA W47.1) |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus AISC Steel Construction Manual, ASTM structural steel standards, and AWS D1.1 welding code | [Triple-S Steel](https://www.sss-steel.com/products), [Kloeckner Metals](https://www.kloecknermetals.com/products/structural-steel-shapes/), [Nucor](https://nucor.com/products/steel/beam), [Metals USA](https://www.metalsusa.com/structural-steel-beams/) |
