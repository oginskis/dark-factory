# SKU Schema: Copper & Copper Alloys

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.copper_alloys`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | CU110-RB-0500, C260-SHT-032 |
| Product Name | product_name | text | Full product name including alloy, form, and dimensions | C11000 ETP Copper Round Bar 0.5in x 36in, C26000 Cartridge Brass Sheet 0.032in |
| URL | url | text | Direct link to the product page | https://example.com/product/c11000-copper-round-bar |
| Price | price | number | Numeric unit price (per piece, per foot, or per pound) excluding currency symbol | 24.50, 78.95, 5.60 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Form | product_form | enum | Physical shape of the product | Sheet, Plate, Strip, Coil, Round Bar, Flat Bar, Hex Bar, Square Bar, Tube, Pipe, Wire, Bus Bar, Casting |
| Tube Type | tube_type | text | Tubing classification for plumbing and HVAC copper tube | Type K, Type L, Type M, DWV, ACR |
| Country of Origin | country_of_origin | text | Country where the copper product was manufactured | USA, Germany, Finland, Chile, Japan |
| Length | length | number (in) | Length of flat products or bar stock | 36, 48, 72, 96, 120 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Alloy Designation (UNS) | alloy_designation_uns | text | Unified Numbering System alloy designation | C10100, C10200, C11000, C17200, C26000, C36000, C51000, C71500 |
| Common Name | common_name | text | Trade or common name of the alloy | ETP Copper, Oxygen-Free Copper, Beryllium Copper, Cartridge Brass, Free-Cutting Brass, Phosphor Bronze, Copper-Nickel |
| Alloy Family | alloy_family | enum | Broad classification of the copper alloy | Pure Copper, High-Copper Alloy, Brass, Bronze, Copper-Nickel, Nickel Silver |
| Temper | temper | text | Temper designation per ASTM or EN standard | O60 (Soft), H01 (Quarter Hard), H02 (Half Hard), H04 (Hard), H08 (Spring), TF00 (Solution Treated) |
| Thickness | thickness | number (in) | Material thickness for flat products (sheet, plate, strip) | 0.010, 0.032, 0.064, 0.125, 0.250, 0.500 |
| Width | width | number (in) | Width of flat products | 12, 24, 36, 48 |
| Wall Thickness | wall_thickness | number (in) | Wall thickness for tube and pipe products | 0.032, 0.049, 0.065, 0.125 |
| Copper Content | copper_content | number (%) | Minimum copper purity or copper percentage in the alloy | 99.99, 99.95, 99.90, 85.0, 70.0, 65.0 |
| Electrical Conductivity | electrical_conductivity | number (% IACS) | Electrical conductivity as a percentage of the International Annealed Copper Standard | 101, 100, 98, 44, 28, 15 |
| Thermal Conductivity | thermal_conductivity | number (W/mK) | Thermal conductivity of the alloy | 391, 388, 226, 120, 62 |
| Density | density | number (g/cm3) | Material density of the specific alloy | 8.89, 8.91, 8.94, 8.53, 8.80 |
| Tensile Strength | tensile_strength | number (ksi) | Ultimate tensile strength for the alloy-temper combination | 32, 47, 54, 68, 140 |
| Yield Strength | yield_strength | number (ksi) | Yield strength for the alloy-temper combination | 10, 36, 50, 63, 120 |
| Hardness | hardness | text | Rockwell or Vickers hardness value | HRB 10, HRB 55, HRB 78, HRC 36 |
| Machinability Rating | machinability_rating | number (%) | Machinability relative to C36000 Free-Cutting Brass at 100% | 20, 30, 60, 80, 100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus CDA/UNS designation system and ASTM copper standards | [Aviva Metals](https://www.avivametals.com/collections/copper-alloys), [Southern Copper & Supply](https://southerncopper.com/copper-alloys/), [Copper.org](https://copper.org/resources/standards/), [Online Metals](https://www.onlinemetals.com/en/product-guide/alloy/110) |
