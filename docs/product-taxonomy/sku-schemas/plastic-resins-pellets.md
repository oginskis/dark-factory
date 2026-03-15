# SKU Schema: Plastic Resins & Pellets

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.resins_pellets`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or supplier product identifier (often the grade name) | DOW-DMDA-8904, CPChem-HHM-TR144, PPR-HDPE-VN-01 |
| Product Name | product_name | text | Full product name including resin type, grade, and key property descriptors | Dow DMDA-8904 NT7 HDPE Blow Molding Resin, Marlex HHM TR-144 High Molecular Weight HDPE, Tipelin BA 550-13 HDPE |
| URL | url | text | Direct link to the product page or technical data sheet | https://example.com/products/hdpe-blow-molding-8904 |
| Price | price | number | Numeric price per unit (per kg, per lb, or per MT), excluding currency symbol | 1.15, 1450.00, 2.30 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, CNY, INR |
| Polymer Type | polymer_type | enum | Base polymer classification | HDPE, LDPE, LLDPE, MDPE, PP Homopolymer, PP Copolymer, PS, GPPS, HIPS, PET, ABS, PC, PA (Nylon), POM (Acetal), PVC, TPE, TPU |
| Resin Grade Name | resin_grade_name | text | Manufacturer-assigned grade or trade name | DMDA-8904, Marlex HHM TR-144, Tipelin BA 550-13, SABIC HDPE B5429 |
| Resin Category | resin_category | enum | Functional classification of the resin | Commodity, Engineering, High Performance, Recycled (PCR), Recycled (PIR), Bio-based |
| Physical Form | physical_form | enum | Form in which the resin is supplied | Pellets, Granules, Powder, Flakes, Bales |
| Country of Origin | country_of_origin | text | Country where the resin was manufactured | USA, Germany, Saudi Arabia, South Korea, Belgium, China, India |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Virgin vs Recycled | virgin_vs_recycled | enum | Whether the resin is virgin, post-consumer recycled, or post-industrial recycled | Virgin, PCR (Post-Consumer Recycled), PIR (Post-Industrial Recycled), Ocean-Bound, Regrind |
| Melt Flow Rate | melt_flow_rate | number (g/10min) | Melt flow index measured at standard conditions per ISO 1133 or ASTM D1238 | 0.3, 1.0, 4.0, 12.0, 25.0, 50.0 |
| MFR Test Conditions | mfr_test_conditions | text | Temperature and load used for MFR measurement | 190 degC / 2.16 kg, 190 degC / 5 kg, 230 degC / 2.16 kg, 190 degC / 21.6 kg |
| Density | density | number (g/cm3) | Resin density measured per ASTM D792 or ISO 1183 | 0.918, 0.935, 0.954, 0.960, 1.05, 1.20, 1.40 |
| Tensile Strength at Yield | tensile_strength_at_yield | number (MPa) | Tensile strength at yield per ASTM D638 or ISO 527 | 10, 21, 28, 38, 60, 80 |
| Flexural Modulus | flexural_modulus | number (MPa) | Stiffness measured per ASTM D790 or ISO 178 | 200, 800, 1200, 1500, 2500, 3000 |
| Impact Strength (Izod) | impact_strength_izod | number (J/m) | Notched Izod impact strength per ASTM D256 | 20, 50, 100, 200, 800, NB (no break) |
| Heat Deflection Temperature | heat_deflection_temperature | number (degC) | HDT at 0.45 MPa per ASTM D648 or ISO 75 | 40, 65, 80, 105, 130, 260 |
| Vicat Softening Point | vicat_softening_point | number (degC) | Temperature at which a flat-ended needle penetrates the specimen | 80, 100, 125, 150 |
| ESCR | escr | number (hours) | Environmental stress crack resistance per ASTM D1693 or ISO 22088 | 24, 100, 300, 1000, greater than 1000 |
| Processing Method | processing_method | text (list) | Recommended processing technologies | Injection Molding, Blow Molding, Film Extrusion, Sheet Extrusion, Pipe Extrusion, Rotational Molding, Fiber Spinning, Thermoforming |
| Color | color | text | Color of the resin as supplied | Natural, White, Black, Custom |
| Application | application | text (list) | Primary intended end-use applications | Bottles, Film, Pipe, Automotive Parts, Packaging, Containers, Caps and Closures, Wire and Cable, Geomembranes |
| Additive Content | additive_content | text | Pre-compounded additives included in the resin | UV Stabilizer, Antioxidant, Slip Agent, Anti-Block, Nucleating Agent, Flame Retardant, Antistatic |
| FDA Compliance | fda_compliance | enum | Whether the resin meets FDA food-contact regulations (21 CFR) | Yes, No, Specific grades only |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM D1238, ASTM D792, ISO 1133, ISO 1183) | [Dow HDPE](https://www.dow.com/en-us/product-technology/pt-polyethylene/pg-polyethylene-hdpe.html), [Chevron Phillips Polyethylene](https://www.cpchem.com/what-we-do/solutions/polyethylene/products), [Premier Plastic Resins](https://premierplasticresins.com/), [MOL Group HDPE Catalog](https://molgroupchemicals.com/userfiles/catalog/hdpe/HDPE_2024-EN.pdf) |
