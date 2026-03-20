# SKU Schema: Coal & Coke

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.coal_coke`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Supplier or trader product identifier | MET-HCC-01, THM-5500-LV, COKE-MET-60 |
| Product Name | product_name | text | — | yes | Full product name including type, grade, and key specs | BMA Peak Downs Hard Coking Coal, South African RB1 Thermal Coal 6000 kcal, Metallurgical Coke CSR 65 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/products/met-coal-hcc |
| Price | price | number | — | yes | Numeric price per metric tonne, excluding currency symbol | 180.00, 95.50, 320.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, AUD, CNY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary classification of the coal or coke product | Hard Coking Coal, Semi-Hard Coking Coal, Semi-Soft Coking Coal, PCI Coal, Thermal Coal, Metallurgical Coke, Foundry Coke, Coke Breeze |
| Country of Origin | country_of_origin | text | — | — | Country where the coal was mined or coke was produced | Australia, USA, Canada, South Africa, Colombia, Russia |
| Size Range | size_range | text | mm | — | Particle or lump size range of the product | 0-50, 25-50, 40-80, 60-90 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Supplier | supplier | text | — | — | Mining company or trading house name | BHP, Corsa Coal, Whitehaven Coal, SunCoke Energy, Teck Resources |
| Coal Rank | coal_rank | enum | — | — | Rank classification based on degree of coalification | Anthracite, Bituminous, Sub-bituminous, Lignite |
| Total Moisture | total_moisture | number | % | — | Total moisture content as received | 6.0, 8.0, 10.0, 15.0 |
| Inherent Moisture | inherent_moisture | number | % | — | Moisture held within the coal structure (air-dried basis) | 1.0, 2.0, 4.5, 8.0 |
| Ash Content | ash_content | number | % | — | Non-combustible mineral residue (dry basis) | 6.0, 8.0, 10.0, 15.0 |
| Volatile Matter | volatile_matter | number | % | — | Gases released on heating (dry ash-free basis) | 18.0, 22.0, 28.0, 36.0 |
| Fixed Carbon | fixed_carbon | number | % | — | Solid combustible residue remaining after removal of moisture, ash, and volatile matter | 50.0, 58.0, 65.0, 85.0 |
| Total Sulfur | total_sulfur | number | % | — | Sulfur content (dry basis) | 0.3, 0.5, 0.8, 1.5 |
| Phosphorus | phosphorus | number | % | — | Phosphorus content (dry basis) | 0.005, 0.02, 0.05, 0.10 |
| Gross Calorific Value | gross_calorific_value | number | kcal/kg | — | Heat energy released on complete combustion (gross/higher heating value) | 5000, 5500, 6000, 7500, 8200 |
| Net Calorific Value | net_calorific_value | number | kcal/kg | — | Lower heating value (net of moisture evaporation energy) | 4800, 5200, 5800, 7200 |
| Hardgrove Grindability Index | hardgrove_grindability_index | number | — | — | HGI value indicating ease of pulverizing the coal | 40, 55, 70, 90 |
| Crucible Swelling Number | crucible_swelling_number | number | — | — | Free swelling index (FSI) indicating coking potential (0-9 scale) | 1.0, 4.0, 6.5, 8.0 |
| Maximum Fluidity | maximum_fluidity | number | ddpm | — | Gieseler maximum fluidity in dial divisions per minute | 20, 200, 1000, 30000 |
| Coke Strength After Reaction | coke_strength_after_reaction | number | % | — | CSR value measuring coke strength after CO2 reaction (coke only) | 55.0, 60.0, 65.0, 72.0 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 companies plus industry standards (S&P Global Platts coal methodology, ASTM coal standards, SCoTA specifications) | [BHP](https://www.bhp.com/what-we-do/products/metallurgical-coal), [Corsa Coal](https://www.corsacoal.com/about-corsa/coal-in-steelmaking/), [Whitehaven Coal](https://whitehavencoal.com.au/), [BCCL](https://bcclweb.in/?page_id=4308) |
