# SKU Schema: Non-Ferrous Ores (Bauxite, Nickel, Zinc, Tin)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or trader product identifier | BAU-MET-A44, NiC-LAT-15, ZnC-58-HG, SnC-CAS-70 |
| Product Name | text | Full product name including ore type, grade, and key specs | Rawmin Metallurgical Grade A Bauxite 44% Al2O3, Laterite Nickel Ore 1.5% Ni, Zinc Concentrate 58% Zn, Cassiterite Tin Concentrate 70% Sn |
| URL | text | Direct link to the product page | https://example.com/products/bauxite-met-grade-a |
| Price | number | Numeric price per dry metric tonne (ore/concentrate) or per lb (refined metal reference), excluding currency symbol | 35.00, 85.00, 120.00, 2800.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, AUD, CNY |
| Supplier | text | Mining company or trading house name | Rawmin, Rio Tinto Alcan, Alcoa, Vale, Glencore, Teck Resources, PT Timah |
| Ore Commodity | enum | Primary metal commodity the ore is sourced for | Bauxite, Nickel, Zinc, Tin |
| Product Form | enum | Physical form or processing stage of the product | Run-of-Mine Ore, Crushed Ore, Concentrate, Sinter, Matte, Calcined |
| Grade Classification | text | Industry or supplier grade designation | Metallurgical Grade A, Refractory Grade, Chemical Grade, Abrasive Grade, High Grade, Low Grade |
| Primary Metal Content | number (%) | Percentage of the target metal or its oxide in the product | 1.2, 15.0, 44.0, 58.0, 70.0 |
| Primary Metal Oxide | text | Chemical symbol or formula of the measured oxide or metal | Al2O3, Ni, Zn, Sn |
| SiO2 Content | number (%) | Silicon dioxide content on a dry basis | 1.0, 4.0, 7.0, 8.0, 15.0 |
| Fe2O3 Content | number (%) | Iron oxide content on a dry basis | 1.0, 5.0, 10.0, 18.0, 25.0 |
| TiO2 Content | number (%) | Titanium dioxide content on a dry basis | 0.5, 2.0, 3.5, 6.0 |
| CaO Content | number (%) | Calcium oxide content on a dry basis | 0.1, 0.5, 1.0, 3.0 |
| MgO Content | number (%) | Magnesium oxide content on a dry basis | 0.1, 0.5, 2.0, 5.0 |
| Sulfur Content | number (%) | Total sulfur content on a dry basis | 0.01, 0.5, 2.0, 15.0, 32.0 |
| Deleterious Elements | text | Penalty elements and their levels (As, Cd, Hg, Pb, Bi, F) | As less than 0.1%, Cd less than 0.05%, Hg less than 1 ppm |
| Loss on Ignition | number (%) | Weight loss at 1000 degC indicating volatiles and combined water | 5.0, 12.0, 20.0, 28.0 |
| Moisture Content | number (%) | Free moisture content as shipped | 2.0, 5.0, 8.0, 10.0, 15.0 |
| Size Range | text (mm) | Particle or lump size range of the product | 0-0.1, 0-3, 0-50, 0-100, 50 x down lumps |
| Mesh Grade | text | Sieve mesh size for concentrate or powder products | -3 mesh, -8 mesh, -100 mesh, -200 mesh, -325 mesh |
| Specific Gravity | number | Density relative to water of the ore or concentrate | 2.50, 3.50, 4.00, 6.99 |
| Ore Mineralogy | text | Primary mineral phase present in the ore | Gibbsite, Boehmite, Diaspore, Pentlandite, Garnierite, Sphalerite, Cassiterite |
| Ore Deposit Type | enum | Geological classification of the deposit | Laterite, Sulfide, Sedimentary, Placer, Alluvial, Hard Rock |
| Al/Si Ratio | number | Alumina to silica ratio (bauxite specific; must exceed 2.6 for metallurgical use) | 2.6, 4.0, 5.5, 8.0 |
| Mohs Hardness | number | Hardness of the primary mineral on the Mohs scale | 1.0, 2.5, 3.5, 5.0, 6.5 |
| Country of Origin | text | Country where the ore was mined | Australia, Guinea, Indonesia, Philippines, Brazil, Peru, Bolivia, DRC, Malaysia |
| Incoterms | text | Trade delivery terms | FOB, CFR, CIF, DAP |
| Minimum Order Quantity | text | Minimum order size | 100 MT, 1000 MT, 5000 MT, Full Cargo |
| Certification | text (list) | Quality, sustainability, or responsible sourcing certifications | ISO 9001, ISO 14001, ITSCI (tin), LME responsible sourcing, ASI (bauxite) |
| Intended Use | enum | Primary metallurgical or industrial application | Alumina Refining, Refractory, Nickel Smelting, HPAL, Zinc Smelting, Tin Smelting, Foundry, Abrasives |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 32 attributes from 4 companies plus industry standards (ASTM B6 zinc, LME specifications, ISO bauxite testing) | [Rawmin](https://www.rawmin.com/metallurgical_grade_bauxite.html), [Reade](https://reade.com/product/bauxite/), [American Elements Zinc Concentrate](https://www.americanelements.com/zinc-concentrate-7440-66-6), [Tancom Minerals (Cassiterite)](https://www.tancominerals.com/cassiterita) |
