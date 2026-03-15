# SKU Schema: Coal & Coke

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or trader product identifier | MET-HCC-01, THM-5500-LV, COKE-MET-60 |
| Product Name | text | Full product name including type, grade, and key specs | BMA Peak Downs Hard Coking Coal, South African RB1 Thermal Coal 6000 kcal, Metallurgical Coke CSR 65 |
| URL | text | Direct link to the product page | https://example.com/products/met-coal-hcc |
| Price | number | Numeric price per metric tonne, excluding currency symbol | 180.00, 95.50, 320.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, AUD, CNY |
| Supplier | text | Mining company or trading house name | BHP, Corsa Coal, Whitehaven Coal, SunCoke Energy, Teck Resources |
| Product Type | enum | Primary classification of the coal or coke product | Hard Coking Coal, Semi-Hard Coking Coal, Semi-Soft Coking Coal, PCI Coal, Thermal Coal, Metallurgical Coke, Foundry Coke, Coke Breeze |
| Coal Rank | enum | Rank classification based on degree of coalification | Anthracite, Bituminous, Sub-bituminous, Lignite |
| Total Moisture | number (%) | Total moisture content as received | 6.0, 8.0, 10.0, 15.0 |
| Inherent Moisture | number (%) | Moisture held within the coal structure (air-dried basis) | 1.0, 2.0, 4.5, 8.0 |
| Ash Content | number (%) | Non-combustible mineral residue (dry basis) | 6.0, 8.0, 10.0, 15.0 |
| Volatile Matter | number (%) | Gases released on heating (dry ash-free basis) | 18.0, 22.0, 28.0, 36.0 |
| Fixed Carbon | number (%) | Solid combustible residue remaining after removal of moisture, ash, and volatile matter | 50.0, 58.0, 65.0, 85.0 |
| Total Sulfur | number (%) | Sulfur content (dry basis) | 0.3, 0.5, 0.8, 1.5 |
| Phosphorus | number (%) | Phosphorus content (dry basis) | 0.005, 0.02, 0.05, 0.10 |
| Gross Calorific Value | number (kcal/kg) | Heat energy released on complete combustion (gross/higher heating value) | 5000, 5500, 6000, 7500, 8200 |
| Net Calorific Value | number (kcal/kg) | Lower heating value (net of moisture evaporation energy) | 4800, 5200, 5800, 7200 |
| Hardgrove Grindability Index | number | HGI value indicating ease of pulverizing the coal | 40, 55, 70, 90 |
| Crucible Swelling Number | number | Free swelling index (FSI) indicating coking potential (0-9 scale) | 1.0, 4.0, 6.5, 8.0 |
| Maximum Fluidity | number (ddpm) | Gieseler maximum fluidity in dial divisions per minute | 20, 200, 1000, 30000 |
| Coke Strength After Reaction | number (%) | CSR value measuring coke strength after CO2 reaction (coke only) | 55.0, 60.0, 65.0, 72.0 |
| Coke Reactivity Index | number (%) | CRI value measuring reactivity of coke with CO2 (coke only) | 20.0, 25.0, 28.0, 32.0 |
| Size Range | text (mm) | Particle or lump size range of the product | 0-50, 25-50, 40-80, 60-90 |
| Coke M40 | number (%) | Micum M40 drum test measuring percentage retained above 40 mm (coke only) | 78.0, 82.0, 85.0, 88.0 |
| Coke M10 | number (%) | Micum M10 drum test measuring percentage passing 10 mm (coke only) | 5.0, 7.0, 8.5, 10.0 |
| Nitrogen Content | number (%) | Nitrogen content (dry basis) | 1.0, 1.5, 1.8, 2.2 |
| Intended Use | enum | Primary industrial application | Steelmaking, Power Generation, Cement, Foundry, Sintering, PCI |
| Country of Origin | text | Country where the coal was mined or coke was produced | Australia, USA, Canada, South Africa, Colombia, Russia |
| Incoterms | text | Trade delivery terms | FOB, CFR, CIF |
| Minimum Order Quantity | text | Minimum order size | 1000 MT, 5000 MT, Full Cargo |
| Certification | text (list) | Quality or sustainability certifications | ISO 9001, ISO 14001, Bettercoal |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 31 attributes from 4 companies plus industry standards (S&P Global Platts coal methodology, ASTM coal standards, SCoTA specifications) | [BHP](https://www.bhp.com/what-we-do/products/metallurgical-coal), [Corsa Coal](https://www.corsacoal.com/about-corsa/coal-in-steelmaking/), [Whitehaven Coal](https://whitehavencoal.com.au/), [BCCL](https://bcclweb.in/?page_id=4308) |
