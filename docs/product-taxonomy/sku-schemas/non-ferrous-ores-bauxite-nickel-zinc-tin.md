# SKU Schema: Non-Ferrous Ores (Bauxite, Nickel, Zinc, Tin)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.non_ferrous_ores`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Supplier or trader product identifier | BAU-MET-A44, NiC-LAT-15, ZnC-58-HG, SnC-CAS-70 |
| Product Name | product_name | text | Full product name including ore type, grade, and key specs | Rawmin Metallurgical Grade A Bauxite 44% Al2O3, Laterite Nickel Ore 1.5% Ni, Zinc Concentrate 58% Zn, Cassiterite Tin Concentrate 70% Sn |
| URL | url | text | Direct link to the product page | https://example.com/products/bauxite-met-grade-a |
| Price | price | number | Numeric price per dry metric tonne (ore/concentrate) or per lb (refined metal reference), excluding currency symbol | 35.00, 85.00, 120.00, 2800.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, AUD, CNY |
| Product Form | product_form | enum | Physical form or processing stage of the product | Run-of-Mine Ore, Crushed Ore, Concentrate, Sinter, Matte, Calcined |
| Grade Classification | grade_classification | text | Industry or supplier grade designation | Metallurgical Grade A, Refractory Grade, Chemical Grade, Abrasive Grade, High Grade, Low Grade |
| Mesh Grade | mesh_grade | text | Sieve mesh size for concentrate or powder products | -3 mesh, -8 mesh, -100 mesh, -200 mesh, -325 mesh |
| Ore Deposit Type | ore_deposit_type | enum | Geological classification of the deposit | Laterite, Sulfide, Sedimentary, Placer, Alluvial, Hard Rock |
| Country of Origin | country_of_origin | text | Country where the ore was mined | Australia, Guinea, Indonesia, Philippines, Brazil, Peru, Bolivia, DRC, Malaysia |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Supplier | supplier | text | Mining company or trading house name | Rawmin, Rio Tinto Alcan, Alcoa, Vale, Glencore, Teck Resources, PT Timah |
| Ore Commodity | ore_commodity | enum | Primary metal commodity the ore is sourced for | Bauxite, Nickel, Zinc, Tin |
| Primary Metal Content | primary_metal_content | number (%) | Percentage of the target metal or its oxide in the product | 1.2, 15.0, 44.0, 58.0, 70.0 |
| Primary Metal Oxide | primary_metal_oxide | text | Chemical symbol or formula of the measured oxide or metal | Al2O3, Ni, Zn, Sn |
| SiO2 Content | sio2_content | number (%) | Silicon dioxide content on a dry basis | 1.0, 4.0, 7.0, 8.0, 15.0 |
| Fe2O3 Content | fe2o3_content | number (%) | Iron oxide content on a dry basis | 1.0, 5.0, 10.0, 18.0, 25.0 |
| TiO2 Content | tio2_content | number (%) | Titanium dioxide content on a dry basis | 0.5, 2.0, 3.5, 6.0 |
| CaO Content | cao_content | number (%) | Calcium oxide content on a dry basis | 0.1, 0.5, 1.0, 3.0 |
| MgO Content | mgo_content | number (%) | Magnesium oxide content on a dry basis | 0.1, 0.5, 2.0, 5.0 |
| Sulfur Content | sulfur_content | number (%) | Total sulfur content on a dry basis | 0.01, 0.5, 2.0, 15.0, 32.0 |
| Deleterious Elements | deleterious_elements | text | Penalty elements and their levels (As, Cd, Hg, Pb, Bi, F) | As less than 0.1%, Cd less than 0.05%, Hg less than 1 ppm |
| Loss on Ignition | loss_on_ignition | number (%) | Weight loss at 1000 degC indicating volatiles and combined water | 5.0, 12.0, 20.0, 28.0 |
| Moisture Content | moisture_content | number (%) | Free moisture content as shipped | 2.0, 5.0, 8.0, 10.0, 15.0 |
| Specific Gravity | specific_gravity | number | Density relative to water of the ore or concentrate | 2.50, 3.50, 4.00, 6.99 |
| Ore Mineralogy | ore_mineralogy | text | Primary mineral phase present in the ore | Gibbsite, Boehmite, Diaspore, Pentlandite, Garnierite, Sphalerite, Cassiterite |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 32 attributes from 4 companies plus industry standards (ASTM B6 zinc, LME specifications, ISO bauxite testing) | [Rawmin](https://www.rawmin.com/metallurgical_grade_bauxite.html), [Reade](https://reade.com/product/bauxite/), [American Elements Zinc Concentrate](https://www.americanelements.com/zinc-concentrate-7440-66-6), [Tancom Minerals (Cassiterite)](https://www.tancominerals.com/cassiterita) |
