# SKU Schema: Aluminum & Aluminum Products

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.aluminum`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | AL6061-T6-125-48X96, 3003-H14-063 |
| Product Name | product_name | text | — | yes | Full product name including alloy, temper, form, and dimensions | 6061-T6 Aluminum Sheet 0.125in x 48in x 96in, 3003-H14 Aluminum Plate 0.250in |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/6061-t6-aluminum-sheet |
| Price | price | number | — | yes | Numeric unit price (per piece, per foot, or per pound) excluding currency symbol | 89.50, 12.75, 3.45 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Form | product_form | enum | — | — | Physical shape of the product | Sheet, Plate, Coil, Round Bar, Flat Bar, Square Bar, Hex Bar, Angle, Channel, Beam, Tube, Pipe, Extrusion, Disc, Tread Plate |
| Anodize Type | anodize_type | text | — | — | Anodizing specification when applicable | Clear Anodize, Hard Anodize (Type III), Color Anodize, MIL-A-8625 Type II |
| Country of Origin | country_of_origin | text | — | — | Country where the aluminum was produced | USA, Canada, Germany, Norway, China, India |
| Length | length | number | in | — | Length of flat products or bar stock | 96, 120, 144 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Brand/Mill | brandmill | text | — | — | Aluminum manufacturer or mill name | Alcoa, Novelis, Kaiser Aluminum, Constellium, Hindalco, Norsk Hydro |
| Alloy | alloy | text | — | — | Aluminum alloy designation per Aluminum Association or EN standard | 1100, 2024, 3003, 5052, 5083, 6061, 6063, 7075, Mic-6 |
| Alloy Series | alloy_series | enum | — | — | Alloy series indicating primary alloying element | 1xxx (Pure), 2xxx (Copper), 3xxx (Manganese), 5xxx (Magnesium), 6xxx (Mg-Si), 7xxx (Zinc) |
| Temper | temper | text | — | — | Temper designation indicating mechanical and thermal treatment | O, H14, H32, T3, T4, T6, T651, T73 |
| Thickness | thickness | number | in | — | Material thickness for flat products | 0.020, 0.063, 0.125, 0.250, 0.500, 1.000 |
| Width | width | number | in | — | Width of flat products (sheet, plate, coil) | 36, 48, 60, 72 |
| Wall Thickness | wall_thickness | number | in | — | Wall thickness for tube and pipe products | 0.035, 0.049, 0.065, 0.125, 0.250 |
| Profile Shape | profile_shape | text | — | — | Cross-section shape for extrusion products | T-Slot, U-Channel, L-Angle, Custom Profile, Square Tube, Rectangular Tube |
| Surface Finish | surface_finish | text | — | — | Surface treatment or condition | Mill Finish, Brushed, Anodized, Bright, Polished, Painted, Powder Coated |
| Density | density | number | g/cm3 | — | Material density of the specific alloy | 2.70, 2.71, 2.78, 2.81 |
| Yield Strength | yield_strength | number | ksi | — | Minimum yield strength of the alloy-temper combination | 4, 21, 35, 40, 73 |
| Tensile Strength | tensile_strength | number | ksi | — | Minimum ultimate tensile strength | 11, 26, 38, 45, 83 |
| Elongation | elongation | number | % | — | Minimum elongation at break | 3, 8, 12, 18, 25 |
| Machinability | machinability | enum | — | — | Relative machinability rating | Poor, Fair, Good, Excellent |
| Weldability | weldability | enum | — | — | Relative weldability rating | Poor, Fair, Good, Excellent |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus Aluminum Association standards and ASTM B209 | [Metals Depot](https://www.metalsdepot.com/aluminum-products/aluminum-sheet), [Pierce Aluminum](https://piercealuminum.com/products/), [Eastern Metal Supply](https://www.easternmetal.com/sheet-plate), [Howard Precision Metals](https://www.howardprecision.com/aluminum/) |
