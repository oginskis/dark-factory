# SKU Schema: Silicone Products

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.silicone`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SE-SG50GP, STK-4716, AR-SIL-100 |
| Product Name | text | Full product name including product form, grade, and size | Solid Silicone Sheet 50A 1/16 in x 12 in x 12 in, FDA Silicone Tubing 3/8 in ID x 5/8 in OD |
| URL | text | Direct link to the product page | https://example.com/product/silicone-sheet-50a-12x12 |
| Price | number | Numeric price per piece, per foot, or per unit, excluding currency symbol | 8.50, 24.00, 135.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Form | enum | Physical form of the silicone product | Sheet, Tubing, O-Ring, Gasket, Extrusion, Sponge, Cord, Molded Part, Adhesive, Sealant |
| Silicone Type | enum | Base silicone chemistry | HCR, LSR, RTV-1, RTV-2, Fluorosilicone |
| Country of Origin | text | Manufacturing country | USA, Germany, Japan, China, UK |
| Inside Diameter | number (mm) | Internal bore for tubing and O-rings | 1.6, 3.2, 6.4, 9.5, 12.7, 25.4, 50.8 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Cure System | enum | Vulcanization or cure method | Peroxide Cured, Platinum Cured, Condensation Cured, Addition Cured |
| Durometer | number (Shore A) | Hardness measurement on the Shore A scale | 10, 20, 30, 40, 50, 60, 70, 80 |
| Thickness | number (mm) | Material thickness for sheets, gaskets, and tubing walls | 0.25, 0.5, 1.0, 1.6, 3.2, 6.4, 12.7 |
| Width | number (mm) | Sheet or roll width | 152, 305, 610, 914, 1219 |
| Temperature Range | text | Continuous service temperature range | -100 F to 500 F, -75 F to 400 F, -116 C to 250 C |
| Tensile Strength | number (psi) | Maximum pull-apart stress before failure | 400, 725, 850, 1080, 1350 |
| Elongation at Break | number (%) | Percentage stretch before failure | 200, 325, 500, 600, 750 |
| Tear Strength | number (ppi) | Resistance to tearing per Die B test | 40, 75, 110, 125, 150 |
| Compression Set | number (%) | Permanent deformation after sustained compression | 10, 15, 20, 25, 35 |
| Color | text | Product body color | Red, Black, Gray, White, Blue, Translucent, Clear |
| Cell Structure | enum | Structure type for sponge and foam grades | Solid, Open Cell, Closed Cell |
| Application | text (list) | Primary intended uses | Gasket Sealing, Medical Device, Food Contact, Aerospace, Electrical Insulation, Pharmaceutical, Automotive |
| FDA Compliance | enum | Whether the product meets FDA 21 CFR 177.2600 | Yes, No |
| Certification | text (list) | Safety and quality certifications | FDA, USP Class VI, 3-A Sanitary, NSF 51, UL, A-A-59588, AMS 3301, MIL-SPEC, RoHS |
| ASTM Standard | text (list) | Governing ASTM specifications | ASTM D2000, ASTM D395, ASTM D412, ASTM D2240 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (A-A-59588, ASTM D2000) | [Stockwell Elastomerics](https://www.stockwell.com/solid-silicone-sheet/), [Accurate Rubber](https://www.accuraterubber.com/), [Vanguard Products](https://www.vanguardproducts.com/products/silicone-rubber-tubing/), [FIX Supply](https://www.fixsupply.com/) |
