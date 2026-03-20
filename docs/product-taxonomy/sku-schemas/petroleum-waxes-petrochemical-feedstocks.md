# SKU Schema: Petroleum Waxes & Petrochemical Feedstocks

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.waxes_petrochemical_feedstocks`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | IGI-1230, HP-MC200, PARA-5825 |
| Product Name | product_name | text | — | yes | Full product name including manufacturer, wax or feedstock type, and grade | IGI 1230A Fully Refined Paraffin Wax, Hase MC-200 Microcrystalline Wax, ExxonMobil Light Naphtha |
| URL | url | text | — | yes | Direct link to the product data sheet or listing page | https://example.com/product/paraffin-wax-130 |
| Price | price | number | — | yes | Numeric price per kilogram, pound, or metric ton, excluding currency symbol | 1.20, 850.00, 1250.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary product classification | Fully Refined Paraffin Wax, Semi-Refined Paraffin Wax, Slack Wax, Microcrystalline Wax, Petrolatum, Light Naphtha, Heavy Naphtha, Ethylene, Propylene, Butadiene, Benzene, Toluene, Xylene |
| Wax Sub-Type | wax_sub-type | text | — | — | Further classification within wax categories | Scale Wax, Slab Wax, Pellet, Pastille, Board, Low Melt, Medium Melt, High Melt |
| Physical Form | physical_form | enum | — | — | Form in which the product is sold | Slab, Pellet, Pastille, Flake, Liquid, Bulk Liquid |
| Country of Origin | country_of_origin | text | — | — | Country where the product was refined or produced | USA, China, Germany, India, South Korea |
| Molecular Weight | molecular_weight | number | g/mol | — | Average molecular weight of the hydrocarbon mixture | 280, 350, 420, 600, 800 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Manufacturer | manufacturer | text | — | — | Producer or refiner name | IGI Wax, Hase Petroleum Wax, Paramelt, Calumet, Sasol, ExxonMobil, Shell |
| Melting Point | melting_point | number | deg F | — | Melting point per ASTM D87 (paraffin) or ASTM D127 drop melt point (microcrystalline) | 118, 130, 145, 155, 175, 195 |
| Melting Point (Celsius) | melting_point_celsius | number | deg C | — | Melting point in degrees Celsius | 48, 54, 63, 68, 79, 91 |
| Oil Content | oil_content | number | % | — | Residual oil content by weight per ASTM D721 | 0.5, 1.0, 3.0, 10.0, 30.0 |
| Viscosity at 210F | viscosity_at_210f | number | SUS | — | Saybolt Universal Seconds viscosity at 210 degrees F | 37, 42, 50, 65, 90 |
| Kinematic Viscosity at 100C | kinematic_viscosity_at_100c | number | mm2/s | — | Kinematic viscosity at 100 degrees C per ASTM D445 | 3.5, 5.2, 8.0, 15.0 |
| Penetration at 25C | penetration_at_25c | number | dmm | — | Needle penetration depth per ASTM D1321 (100g/5sec/25C) | 10, 15, 23, 33, 60 |
| Color | color | text | — | — | Color rating per ASTM D156 Saybolt or visual description | +21, +25, +30, White, Pale Yellow, Amber |
| Specific Gravity at 25C | specific_gravity_at_25c | number | — | — | Density relative to water at 25 degrees C | 0.880, 0.910, 0.920, 0.940 |
| Flash Point | flash_point | number | deg C | — | Minimum temperature at which vapors will ignite per ASTM D92 | 177, 200, 230, 260 |
| Congealing Point | congealing_point | number | deg C | — | Temperature at which the wax solidifies per ASTM D938 | 48, 54, 60, 70 |
| Carbon Number Range | carbon_number_range | text | — | — | Range of carbon chain lengths in the product | C20-C36, C30-C60, C5-C6, C6-C12 |
| Boiling Range | boiling_range | text | deg C | — | Distillation boiling range per ASTM D86 | 30-90 (light naphtha), 90-200 (heavy naphtha), 150-300 |
| Sulfur Content | sulfur_content | number | ppm | — | Total sulfur content | 1, 5, 50, 500 |
| Paraffin Content (PIONA) | paraffin_content_piona | number | % | — | Percentage of paraffinic hydrocarbons in naphtha feedstock | 40, 55, 70, 85 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM wax testing standards (D87, D127, D721) and FDA food contact regulations | [IGI Wax](https://igiwax.com/products/petroleum-wax-types/), [IRM Wax Classification](https://www.irmwax.com/FAQ/Classification%20of%20petroleum%20waxes.aspx), [Hase Petroleum Wax](https://www.hpwax.com/wax.htm), [Hywax Petroleum Wax Types](https://www.hywax.com/blog/petroleum-wax-types) |
