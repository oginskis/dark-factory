# SKU Schema: Industrial Minerals (Silica, Talc, Kaolin)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.industrial_minerals`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier or manufacturer product identifier | IMS-SIL-200, KAO-HB4-325, TLC-MIC-10 |
| Product Name | product_name | text | — | yes | Full product name including mineral type, grade, and key specs | Microsil 200 Mesh Ground Silica, Imerys Hydrite PXN Kaolin, MicroTalc HAR T84 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/products/silica-flour-200-mesh |
| Price | price | number | — | yes | Numeric price per unit (per tonne, per bag, or per kg depending on seller) | 85.00, 250.00, 1200.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, ZAR |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Mineral Type | mineral_type | enum | — | — | Primary mineral classification | Silica Sand, Silica Flour, Ground Silica, Kaolin, Calcined Kaolin, Ball Clay, Talc, Wollastonite, Mica, Feldspar, Barytes |
| Chemical Formula | chemical_formula | text | — | — | Chemical formula of the primary mineral phase | SiO2, Al2Si2O5(OH)4, Mg3Si4O10(OH)2, BaSO4 |
| Mesh Grade | mesh_grade | text | — | — | US standard sieve mesh size designation | 100, 200, 325, 400, 500, 1500 |
| Physical Form | physical_form | enum | — | — | Physical form of the product as shipped | Powder, Granules, Lumps, Slurry, Pellets, Sand |
| Country of Origin | country_of_origin | text | — | — | Country where the mineral was mined or processed | USA, South Africa, UK, France, Brazil, India, China |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Primary Oxide Content | primary_oxide_content | number | % | — | Percentage of the dominant oxide (SiO2 for silica, Al2O3 for kaolin, MgO for talc) | 95.0, 99.5, 99.97, 38.0 |
| Specific Gravity | specific_gravity | number | — | — | Density relative to water | 2.20, 2.60, 2.65, 2.75, 4.50 |
| Mohs Hardness | mohs_hardness | number | — | — | Hardness on the Mohs scale | 1.0, 2.5, 3.0, 6.0, 7.0 |
| Brightness (ISO) | brightness_iso | number | % | — | ISO brightness as measured by reflectance | 70, 80, 88, 92, 96 |
| Whiteness (L*) | whiteness_l* | number | — | — | CIE L* whiteness value | 85, 90, 94, 97 |
| pH | ph | number | — | — | pH measured in aqueous suspension | 4.0, 5.5, 7.0, 9.0, 10.5 |
| Moisture Content | moisture_content | number | % | — | Free moisture as shipped | 0.1, 0.5, 1.0, 3.0 |
| Oil Absorption | oil_absorption | number | g/100g | — | Grams of oil absorbed per 100 g of mineral (relevant for fillers) | 20, 30, 45, 60, 80 |
| Loss on Ignition | loss_on_ignition | number | % | — | Weight loss at 1000 degC indicating volatiles and combined water | 0.1, 5.0, 12.0, 14.0 |
| Fe2O3 Content | fe2o3_content | number | % | — | Iron oxide impurity content | 0.01, 0.05, 0.20, 1.50 |
| TiO2 Content | tio2_content | number | % | — | Titanium dioxide impurity content | 0.01, 0.10, 0.50, 1.80 |
| Aspect Ratio | aspect_ratio | number | — | — | Length-to-thickness ratio of platy particles (talc, mica) | 5, 10, 20, 50, 80 |
| Application | application | text (list) | — | — | Primary intended industrial uses | Paints and Coatings, Ceramics, Glass, Foundry, Rubber, Plastics, Paper, Cosmetics, Construction |
| Packaging | packaging | text | — | — | Packaging options available | 25 kg bags, 50 lb bags, 1 MT bulk bags, Bulk tanker |
| Certification | certification | text (list) | — | — | Quality, purity, or safety certifications | ISO 9001, REACH, FDA compliant, Kosher, NSF |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM, ISO particle size standards) | [Imerys Talc](https://www.imerys.com/minerals/talc), [Imerys Kaolin](https://www.imerys.com/minerals/kaolin), [U.S. Silica](https://www.ussilica.com/), [Micronized](https://micronized.com/products/industrial-minerals/) |
