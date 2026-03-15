# SKU Schema: Foam & Expanded Plastic Products

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | UF-EPS150-2, FBM-EPP13B, AF-XPS200 |
| Product Name | text | Full product name including foam type, density, and dimensions | EPS Foam Board Insulation 2 in x 4 ft x 8 ft 1.5 lb, Polyurethane Expanding Foam 1 lb Density |
| URL | text | Direct link to the product page | https://example.com/product/eps-2in-4x8-15lb |
| Price | number | Numeric price per sheet, block, or unit, excluding currency symbol | 22.50, 48.00, 89.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | Owens Corning, Dow, Universal Foam Products, Atlas Foam, Foam Factory |
| Foam Type | enum | Primary foam material classification | EPS, XPS, Polyurethane, Polyisocyanurate, EPP, EPE, EVA, Melamine |
| Cell Structure | enum | Open or closed cell configuration | Open Cell, Closed Cell |
| Density | number (pcf) | Weight per cubic foot (pounds per cubic foot) | 0.9, 1.0, 1.5, 2.0, 3.0, 4.0, 6.0 |
| Thickness | number (in) | Panel, sheet, or block thickness | 0.5, 1, 1.5, 2, 3, 4, 6 |
| Width | number (in) | Panel or sheet width | 12, 16, 24, 48 |
| Length | number (in) | Panel, sheet, or block length | 24, 48, 96, 108 |
| R-Value per Inch | number | Thermal resistance per inch of thickness | 3.6, 3.85, 4.0, 5.0, 6.5 |
| Total R-Value | number | Total thermal resistance at stated thickness | 4.0, 7.7, 10.0, 13.0, 19.5 |
| Compressive Strength | number (psi) | Resistance to compression at 10% deformation | 10, 15, 25, 33, 60, 100 |
| Flexural Strength | number (psi) | Resistance to bending force | 25, 40, 50, 75 |
| Tensile Strength | number (psi) | Maximum pull-apart stress before failure | 16, 20, 25, 27, 50 |
| Water Absorption | number (%) | Percentage of water absorbed by volume | 0.5, 1.0, 2.0, 4.0 |
| Water Vapor Permeance | number (perm-in) | Moisture vapor transmission rate | 0.6, 1.0, 2.0, 3.5, 5.0 |
| Temperature Range | text | Continuous service temperature limits | -40 F to 165 F, -297 F to 250 F, -40 F to 300 F |
| Flame Spread Rating | number | ASTM E 84 flame spread index | 5, 15, 25, 75 |
| Smoke Development Rating | number | ASTM E 84 smoke developed index | 45, 100, 165, 450 |
| Color | text | Product body color | White, Pink, Blue, Yellow, Gray, Black |
| Application | text (list) | Primary intended uses | Wall Insulation, Roof Insulation, Below Grade, Packaging, Cushioning, Flotation, Acoustic Panel |
| Edge Profile | text | Edge configuration of rigid boards | Square Edge, Shiplap, Tongue and Groove |
| Facing/Cladding | text | Surface lamination on rigid boards | Unfaced, Foil Faced, Poly Faced, OSB Faced, Glass Mat |
| ASTM Standard | text (list) | Governing ASTM specifications | ASTM C 578, ASTM C 591, ASTM D 1621, ASTM E 84, ASTM E 96 |
| Certification | text (list) | Third-party certifications and listings | UL, ICC-ES ESR, GREENGUARD, Energy Star |
| Pack Quantity | number | Number of sheets or units per pack | 1, 4, 6, 8, 12 |
| Weight per Unit | number (kg) | Weight of a single sheet, block, or package | 0.5, 1.2, 3.0, 5.5 |
| Country of Origin | text | Manufacturing country | USA, Canada, Germany, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM standards (C 578, E 84, D 1621) | [Universal Foam Products](https://univfoam.com/), [Northwest Foam](https://northwestfoam.com/documents/eps-facts/), [Foam Factory Inc.](https://www.foambymail.com/), [Owens Corning FOAMULAR](https://www.owenscorning.com/) |
