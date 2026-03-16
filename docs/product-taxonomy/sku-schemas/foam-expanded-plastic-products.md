# SKU Schema: Foam & Expanded Plastic Products

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.foam_expanded`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | UF-EPS150-2, FBM-EPP13B, AF-XPS200 |
| Product Name | product_name | text | — | Full product name including foam type, density, and dimensions | EPS Foam Board Insulation 2 in x 4 ft x 8 ft 1.5 lb, Polyurethane Expanding Foam 1 lb Density |
| URL | url | text | — | Direct link to the product page | https://example.com/product/eps-2in-4x8-15lb |
| Price | price | number | — | Numeric price per sheet, block, or unit, excluding currency symbol | 22.50, 48.00, 89.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Foam Type | foam_type | enum | — | Primary foam material classification | EPS, XPS, Polyurethane, Polyisocyanurate, EPP, EPE, EVA, Melamine |
| Country of Origin | country_of_origin | text | — | Manufacturing country | USA, Canada, Germany, China |
| Length | length | number | in | Panel, sheet, or block length | 24, 48, 96, 108 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Cell Structure | cell_structure | enum | — | Open or closed cell configuration | Open Cell, Closed Cell |
| Density | density | number | pcf | Weight per cubic foot (pounds per cubic foot) | 0.9, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0 |
| Thickness | thickness | number | in | Panel, sheet, or block thickness | 0.5, 1, 1.5, 2, 3, 4, 6 |
| Width | width | number | in | Panel or sheet width | 12, 16, 24, 48 |
| R-Value per Inch | r-value_per_inch | number | — | Thermal resistance per inch of thickness | 3.6, 3.85, 4.0, 5.0, 6.5 |
| Total R-Value | total_r-value | number | — | Total thermal resistance at stated thickness | 4.0, 7.7, 10.0, 13.0, 19.5 |
| Compressive Strength | compressive_strength | number | psi | Resistance to compression at 10% deformation | 10, 15, 25, 33, 60, 100 |
| Flexural Strength | flexural_strength | number | psi | Resistance to bending force | 25, 40, 50, 75 |
| Tensile Strength | tensile_strength | number | psi | Maximum pull-apart stress before failure | 16, 20, 25, 27, 50 |
| Water Absorption | water_absorption | number | % | Percentage of water absorbed by volume | 0.5, 1.0, 2.0, 4.0 |
| Water Vapor Permeance | water_vapor_permeance | number | perm-in | Moisture vapor transmission rate | 0.6, 1.0, 2.0, 3.5, 5.0 |
| Temperature Range | temperature_range | text | — | Continuous service temperature limits | -40 F to 165 F, -297 F to 250 F, -40 F to 300 F |
| Flame Spread Rating | flame_spread_rating | number | — | ASTM E 84 flame spread index | 5, 15, 25, 75 |
| Smoke Development Rating | smoke_development_rating | number | — | ASTM E 84 smoke developed index | 45, 100, 165, 450 |
| Color | color | text | — | Product body color | White, Pink, Blue, Yellow, Gray, Black |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM standards (C 578, E 84, D 1621) | [Universal Foam Products](https://univfoam.com/), [Northwest Foam](https://northwestfoam.com/documents/eps-facts/), [Foam Factory Inc.](https://www.foambymail.com/), [Owens Corning FOAMULAR](https://www.owenscorning.com/) |
