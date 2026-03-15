# SKU Schema: Silicone Products

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SE-SG50GP, STK-4716, AR-SIL-100 |
| Product Name | text | Full product name including product form, grade, and size | Solid Silicone Sheet 50A 1/16 in x 12 in x 12 in, FDA Silicone Tubing 3/8 in ID x 5/8 in OD |
| URL | text | Direct link to the product page | https://example.com/product/silicone-sheet-50a-12x12 |
| Price | number | Numeric price per piece, per foot, or per unit, excluding currency symbol | 8.50, 24.00, 135.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | Stockwell Elastomerics, Accurate Rubber, Vanguard Products, ElastoStar, Shin-Etsu |
| Product Form | enum | Physical form of the silicone product | Sheet, Tubing, O-Ring, Gasket, Extrusion, Sponge, Cord, Molded Part, Adhesive, Sealant |
| Silicone Type | enum | Base silicone chemistry | HCR, LSR, RTV-1, RTV-2, Fluorosilicone |
| Cure System | enum | Vulcanization or cure method | Peroxide Cured, Platinum Cured, Condensation Cured, Addition Cured |
| Durometer | number (Shore A) | Hardness measurement on the Shore A scale | 10, 20, 30, 40, 50, 60, 70, 80 |
| Thickness | number (mm) | Material thickness for sheets, gaskets, and tubing walls | 0.25, 0.5, 1.0, 1.6, 3.2, 6.4, 12.7 |
| Inside Diameter | number (mm) | Internal bore for tubing and O-rings | 1.6, 3.2, 6.4, 9.5, 12.7, 25.4, 50.8 |
| Outside Diameter | number (mm) | External diameter for tubing and O-rings | 3.2, 6.4, 9.5, 12.7, 15.9, 31.8, 63.5 |
| Width | number (mm) | Sheet or roll width | 152, 305, 610, 914, 1219 |
| Length | number (mm) | Sheet, roll, or tubing length | 305, 610, 7620, 15240, 30480 |
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
| Operating Pressure | number (psi) | Maximum working pressure for tubing | 10, 25, 40, 80 |
| Dielectric Strength | number (V/mil) | Electrical insulation rating | 400, 500, 550, 700 |
| Specific Gravity | number | Material density relative to water | 1.10, 1.15, 1.25, 1.40 |
| Pack Quantity | number | Number of pieces per pack or per order | 1, 5, 10, 25, 100 |
| Country of Origin | text | Manufacturing country | USA, Germany, Japan, China, UK |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (A-A-59588, ASTM D2000) | [Stockwell Elastomerics](https://www.stockwell.com/solid-silicone-sheet/), [Accurate Rubber](https://www.accuraterubber.com/), [Vanguard Products](https://www.vanguardproducts.com/products/silicone-rubber-tubing/), [FIX Supply](https://www.fixsupply.com/) |
