# SKU Schema: Iron Ore

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.iron_ore`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier or trader product identifier | IORE-PEL-67, KIO-LMP-651, VALE-FIN-632 |
| Product Name | product_name | text | — | yes | Full product name including form, grade, and key specs | LKAB Blast Furnace Pellets 67% Fe, Kumba Premium Lump 65.1% Fe, Pilbara Blend Fines 62% Fe |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/products/iron-ore-pellets |
| Price | price | number | — | yes | Numeric price per dry metric tonne, excluding currency symbol | 120.50, 98.75, 145.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, CNY, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Form | product_form | enum | — | — | Physical form of the iron ore product | Fines, Lump, Pellets, Concentrate, Sinter Feed |
| Ore Type | ore_type | enum | — | — | Primary iron-bearing mineral in the ore | Hematite, Magnetite, Goethite, Limonite |
| Country of Origin | country_of_origin | text | — | — | Country where the ore was mined | Australia, Brazil, Sweden, South Africa, India, Canada |
| Size Range | size_range | text | mm | — | Particle size range of the product | 0-0.15, 0-6.3, 6-30, 8-18, 10-50 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Supplier | supplier | text | — | — | Mining company or trading house name | LKAB, Vale, Rio Tinto, Anglo American Kumba, BHP, Fortescue |
| Fe Content | fe_content | number | % | — | Total iron content on a dry basis | 58.0, 62.0, 65.1, 67.0, 70.0 |
| SiO2 Content | sio2_content | number | % | — | Silicon dioxide (silica) content on a dry basis | 0.6, 1.65, 4.0, 5.7 |
| Al2O3 Content | al2o3_content | number | % | — | Aluminium oxide (alumina) content on a dry basis | 0.6, 1.2, 2.5, 3.7 |
| P Content | p_content | number | % | — | Phosphorus content on a dry basis | 0.02, 0.05, 0.08, 0.12 |
| S Content | s_content | number | % | — | Sulfur content on a dry basis | 0.005, 0.01, 0.03, 0.05 |
| Moisture | moisture | number | % | — | Free moisture content as shipped | 2.0, 5.0, 8.0, 10.0 |
| LOI | loi | number | % | — | Loss on ignition, indicating combined water and volatile matter | 0.5, 2.0, 5.0, 10.0 |
| TiO2 Content | tio2_content | number | % | — | Titanium dioxide content on a dry basis | 0.05, 0.10, 0.50, 1.20 |
| MnO Content | mno_content | number | % | — | Manganese oxide content on a dry basis | 0.05, 0.10, 0.30 |
| MgO Content | mgo_content | number | % | — | Magnesium oxide content on a dry basis | 0.01, 0.10, 0.50, 1.50 |
| CaO Content | cao_content | number | % | — | Calcium oxide content on a dry basis | 0.05, 0.20, 1.00, 3.00 |
| Alkali Content | alkali_content | number | % | — | Combined Na2O and K2O content on a dry basis | 0.02, 0.05, 0.10, 0.20 |
| Bulk Density | bulk_density | number | t/m3 | — | Bulk density of the product as shipped | 1.8, 2.0, 2.3, 2.5 |
| Compression Strength | compression_strength | number | kg/pellet | — | Compressive strength per pellet (pellets only) | 200, 250, 300, 350 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (S&P Global Platts iron ore specifications, ISO tumble test standards) | [LKAB](https://lkab.com/en/what-we-do/our-products-and-services/iron-ore-pellets-and-fines/), [Anglo American Kumba](https://www.angloamericankumba.com/products/iron-ore), [Call2Supply](https://call2supply.com/product/iron-ore/), [Rio Tinto](https://www.riotinto.com/en/products/iron-ore) |
