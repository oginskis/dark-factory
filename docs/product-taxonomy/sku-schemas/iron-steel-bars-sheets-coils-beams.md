# SKU Schema: Iron & Steel (Bars, Sheets, Coils, Beams)

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.iron_steel`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | HRS-1048-4X8, A36-WF-W8X31, SS-304-16GA |
| Product Name | product_name | text | — | yes | Full product name including key specs such as grade, form, and dimensions | A36 Hot Rolled Steel Sheet 16 Gauge 48 x 96, W8x31 A992 Wide Flange Beam 20ft |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/a36-hot-rolled-sheet-16ga |
| Price | price | number | — | yes | Numeric unit price (per piece, per foot, or per pound depending on seller) excluding currency symbol | 45.99, 189.50, 2.35 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Form | product_form | enum | — | — | Physical shape of the product | Sheet, Plate, Coil, Flat Bar, Round Bar, Square Bar, Angle, Channel, Wide Flange Beam, I-Beam, Tube, Pipe, Hex Bar |
| Steel Type | steel_type | enum | — | — | Broad classification of the steel | Carbon Steel, Stainless Steel, Alloy Steel, Tool Steel, Galvanized Steel, Weathering Steel |
| Grade/Specification | gradespecification | text | — | — | ASTM, EN, or JIS grade designation | A36, A992, A572-50, A500, A1011 CS, 304, 316L, 4140, EN S275JR |
| Country of Origin | country_of_origin | text | — | — | Country where the steel was produced | USA, Brazil, South Korea, Japan, Germany, India |
| Length | length | number | ft | — | Length of the product. Sheets and plates in inches, bars and beams in feet | 8, 10, 20, 40 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Brand/Mill | brandmill | text | — | — | Steel manufacturer or mill name | Nucor, US Steel, ArcelorMittal, Nippon Steel, SSAB, Tata Steel |
| Thickness | thickness | text | in | — | Material thickness in inches or gauge. Sheets and plates in decimal inches or gauge number, structural shapes by web thickness | 0.0598 (16 ga), 0.25, 0.5, 1.0 |
| Width | width | number | in | — | Width of flat products (sheet, plate, coil, flat bar) | 36, 48, 60, 72 |
| Wall Thickness | wall_thickness | number | in | — | Wall thickness for tube and pipe products | 0.065, 0.120, 0.250, 0.500 |
| Yield Strength | yield_strength | number | ksi | — | Minimum yield strength of the material | 36, 50, 55, 70 |
| Tensile Strength | tensile_strength | number | ksi | — | Minimum ultimate tensile strength | 58, 65, 70, 100 |
| Surface Finish | surface_finish | text | — | — | Surface condition or coating applied to the product | Hot Rolled (Black), Cold Rolled, Pickled and Oiled, Galvanized, Galvannealed, Aluminized, Painted |
| Edge Condition | edge_condition | text | — | — | Edge type for sheet and coil products | Mill Edge, Slit Edge, Sheared Edge |
| Tolerance | tolerance | text | — | — | Dimensional tolerance standard | ASTM A568, ASTM A6, EN 10029 |
| Heat Number | heat_number | text | — | — | Mill heat number for traceability | A12345, B67890 |
| Chemistry | chemistry | text | — | — | Key alloying element percentages | C 0.26 max, Mn 0.60-0.90, Cr 18.0-20.0, Ni 8.0-10.5 |
| Hardness | hardness | text | — | — | Hardness measurement where applicable | HRB 70, HRC 28, BHN 120 |
| Mill Certification | mill_certification | boolean | — | — | Whether a mill test report (MTR) is included | Yes, No |
| Domestic/Import | domesticimport | enum | — | — | Origin classification | Domestic, Import |
| Certification | certification | text (list) | — | — | Quality and compliance certifications | ASTM, ISO 9001, CE, EN 10204 3.1 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM steel standards (A36, A992, A653, A568) | [Russel Metals](https://www.russelmetals.com/en/product/sheet-and-coil/), [Metals Depot](https://www.metalsdepot.com/), [Norfolk Iron & Metal](https://www.norfolkiron.com/steel-beams/), [Majestic Steel](https://www.majesticsteel.com/) |
