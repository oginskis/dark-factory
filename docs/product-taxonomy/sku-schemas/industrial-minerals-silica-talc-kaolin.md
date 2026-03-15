# SKU Schema: Industrial Minerals (Silica, Talc, Kaolin)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.industrial_minerals`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or manufacturer product identifier | IMS-SIL-200, KAO-HB4-325, TLC-MIC-10 |
| Product Name | text | Full product name including mineral type, grade, and key specs | Microsil 200 Mesh Ground Silica, Imerys Hydrite PXN Kaolin, MicroTalc HAR T84 |
| URL | text | Direct link to the product page | https://example.com/products/silica-flour-200-mesh |
| Price | number | Numeric price per unit (per tonne, per bag, or per kg depending on seller) | 85.00, 250.00, 1200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, ZAR |
| Mineral Type | enum | Primary mineral classification | Silica Sand, Silica Flour, Ground Silica, Kaolin, Calcined Kaolin, Ball Clay, Talc, Wollastonite, Mica, Feldspar, Barytes |
| Chemical Formula | text | Chemical formula of the primary mineral phase | SiO2, Al2Si2O5(OH)4, Mg3Si4O10(OH)2, BaSO4 |
| Mesh Grade | text | US standard sieve mesh size designation | 100, 200, 325, 400, 500, 1500 |
| Physical Form | enum | Physical form of the product as shipped | Powder, Granules, Lumps, Slurry, Pellets, Sand |
| Country of Origin | text | Country where the mineral was mined or processed | USA, South Africa, UK, France, Brazil, India, China |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Primary Oxide Content | number (%) | Percentage of the dominant oxide (SiO2 for silica, Al2O3 for kaolin, MgO for talc) | 95.0, 99.5, 99.97, 38.0 |
| Specific Gravity | number | Density relative to water | 2.20, 2.60, 2.65, 2.75, 4.50 |
| Mohs Hardness | number | Hardness on the Mohs scale | 1.0, 2.5, 3.0, 6.0, 7.0 |
| Brightness (ISO) | number (%) | ISO brightness as measured by reflectance | 70, 80, 88, 92, 96 |
| Whiteness (L*) | number | CIE L* whiteness value | 85, 90, 94, 97 |
| pH | number | pH measured in aqueous suspension | 4.0, 5.5, 7.0, 9.0, 10.5 |
| Moisture Content | number (%) | Free moisture as shipped | 0.1, 0.5, 1.0, 3.0 |
| Oil Absorption | number (g/100g) | Grams of oil absorbed per 100 g of mineral (relevant for fillers) | 20, 30, 45, 60, 80 |
| Loss on Ignition | number (%) | Weight loss at 1000 degC indicating volatiles and combined water | 0.1, 5.0, 12.0, 14.0 |
| Fe2O3 Content | number (%) | Iron oxide impurity content | 0.01, 0.05, 0.20, 1.50 |
| TiO2 Content | number (%) | Titanium dioxide impurity content | 0.01, 0.10, 0.50, 1.80 |
| Aspect Ratio | number | Length-to-thickness ratio of platy particles (talc, mica) | 5, 10, 20, 50, 80 |
| Application | text (list) | Primary intended industrial uses | Paints and Coatings, Ceramics, Glass, Foundry, Rubber, Plastics, Paper, Cosmetics, Construction |
| Packaging | text | Packaging options available | 25 kg bags, 50 lb bags, 1 MT bulk bags, Bulk tanker |
| Certification | text (list) | Quality, purity, or safety certifications | ISO 9001, REACH, FDA compliant, Kosher, NSF |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM, ISO particle size standards) | [Imerys Talc](https://www.imerys.com/minerals/talc), [Imerys Kaolin](https://www.imerys.com/minerals/kaolin), [U.S. Silica](https://www.ussilica.com/), [Micronized](https://micronized.com/products/industrial-minerals/) |
