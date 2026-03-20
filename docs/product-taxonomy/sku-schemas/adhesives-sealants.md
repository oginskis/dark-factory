# SKU Schema: Adhesives & Sealants

**Last updated:** 2026-03-15
**Parent category:** Chemicals & Chemical Products
**Taxonomy ID:** `chemicals.adhesives_sealants`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 2068749, 62-3895-3785-1, MMM-DP420NS |
| Product Name | product_name | text | — | yes | Full product name including brand, product number, and type descriptor | LOCTITE 577 Thread Sealant 50mL, 3M Scotch-Weld Epoxy Adhesive 2216 B/A Gray, Henkel Teroson MS 930 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/loctite-577 |
| Price | price | number | — | yes | Numeric price per sales unit, excluding currency symbol | 34.62, 125.00, 8.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY, CNY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Category | product_category | enum | — | — | Primary functional classification | Structural Adhesive, Thread Sealant, Gasket Sealant, Pipe Sealant, Retaining Compound, Instant Adhesive, Construction Sealant, Potting Compound |
| Chemistry Type | chemistry_type | text | — | — | Chemical basis of the adhesive or sealant formulation | Epoxy, Cyanoacrylate, Anaerobic, Silicone, Polyurethane, MS Polymer, Acrylic, Methacrylate, Hot Melt |
| Packaging Form | packaging_form | enum | — | — | Physical packaging type for the product | Tube, Cartridge, Sausage, Bottle, Syringe, Pail, Drum, Dual Cartridge, Foil Pack |
| Hazard Class | hazard_class | text | — | — | Transport or storage hazard classification | Non-hazardous, Flammable Liquid Class 3, Corrosive Class 8 |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, Germany, Ireland, China, Japan |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Product Line | product_line | text | — | — | Named product series within the brand | Scotch-Weld, Hysol, Teroson, SikaFlex, Permabond, LOCTITE |
| Number of Components | number_of_components | enum | — | — | Number of parts that must be mixed or combined for use | 1, 2 |
| Cure Mechanism | cure_mechanism | text | — | — | Primary mechanism by which the product cures or sets | Anaerobic, Moisture Cure, UV Cure, Heat Cure, Room Temperature, Chemical Reaction, Pressure Sensitive |
| Color | color | text | — | — | Visual color of the cured or uncured product | Clear, Gray, Black, White, Red, Amber, Green |
| Viscosity | viscosity | text | mPa.s | — | Resistance to flow measured at a stated temperature, often at 25 C | 100, 4500-5500, 200000-500000, Thixotropic paste |
| Mix Ratio | mix_ratio | text | — | — | Volume or weight ratio for two-component products | 1:1, 2:1, 10:1, Not applicable |
| Gap Fill | gap_fill | text | mm | — | Maximum gap the product can bridge while maintaining performance | 0.05, 0.15, 0.25, 0.50, 5.0 |
| Fixture Time | fixture_time | text | — | — | Time for the bond to achieve handling strength under standard conditions | 5 s, 4 min, 25 min, 9-12 h |
| Full Cure Time | full_cure_time | text | — | — | Time to reach full mechanical and chemical properties | 24 h, 72 h, 7 days |
| Open Time / Working Life | open_time_working_life | text | — | — | Maximum usable time after mixing or applying before the product becomes unworkable | 30 s, 5 min, 45 min, 4 h |
| Lap Shear Strength | lap_shear_strength | text | MPa | — | Overlap shear strength measured on a standard substrate per ISO 4587 or ASTM D1002 | 1.3, 17.2, 25.0, 35.0 |
| Peel Strength | peel_strength | text | N/mm | — | Resistance to peeling force on a standard substrate | 3.5, 8.0, 12.0 |
| Tensile Strength | tensile_strength | text | MPa | — | Ultimate tensile strength of the cured product | 2.5, 10.0, 30.0, 45.0 |
| Elongation at Break | elongation_at_break | number | % | — | Percentage of stretch before the cured material fails | 2, 5, 100, 300, 600 |
| Operating Temperature Range | operating_temperature_range | text | — | — | Continuous service temperature range of the cured bond | -55 to 180 C, -40 to 120 C, -65 to 260 C |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus industry standards (ISO 4587, ASTM D1002, CGA adhesive classifications) | [Henkel Loctite](https://next.henkel-adhesives.com/us/en/products/industrial-sealants/central-pdp.html/loctite-577/BP000000168431.html), [3M Scotch-Weld](https://www.3m.com/3M/en_US/p/c/adhesives/), [Master Bond](https://www.masterbond.com/), [Ellsworth Adhesives](https://www.ellsworth.com/products/by-market/general-industry/sealants/anaerobic-threadlocker/henkel-loctite-565-thread-sealant-pst-pipe-sealant-with-ptfe-white-250-ml-tube/) |
