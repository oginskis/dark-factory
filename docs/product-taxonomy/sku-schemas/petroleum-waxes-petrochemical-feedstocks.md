# SKU Schema: Petroleum Waxes & Petrochemical Feedstocks

**Last updated:** 2026-03-15
**Parent category:** Petroleum & Coal Products
**Taxonomy ID:** `petroleum.waxes_petrochemical_feedstocks`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | IGI-1230, HP-MC200, PARA-5825 |
| Product Name | text | Full product name including manufacturer, wax or feedstock type, and grade | IGI 1230A Fully Refined Paraffin Wax, Hase MC-200 Microcrystalline Wax, ExxonMobil Light Naphtha |
| URL | text | Direct link to the product data sheet or listing page | https://example.com/product/paraffin-wax-130 |
| Price | number | Numeric price per kilogram, pound, or metric ton, excluding currency symbol | 1.20, 850.00, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary product classification | Fully Refined Paraffin Wax, Semi-Refined Paraffin Wax, Slack Wax, Microcrystalline Wax, Petrolatum, Light Naphtha, Heavy Naphtha, Ethylene, Propylene, Butadiene, Benzene, Toluene, Xylene |
| Wax Sub-Type | text | Further classification within wax categories | Scale Wax, Slab Wax, Pellet, Pastille, Board, Low Melt, Medium Melt, High Melt |
| Physical Form | enum | Form in which the product is sold | Slab, Pellet, Pastille, Flake, Liquid, Bulk Liquid |
| Country of Origin | text | Country where the product was refined or produced | USA, China, Germany, India, South Korea |
| Molecular Weight | number | Average molecular weight of the hydrocarbon mixture | 280, 350, 420, 600, 800 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Manufacturer | text | Producer or refiner name | IGI Wax, Hase Petroleum Wax, Paramelt, Calumet, Sasol, ExxonMobil, Shell |
| Melting Point | number (deg F) | Melting point per ASTM D87 (paraffin) or ASTM D127 drop melt point (microcrystalline) | 118, 130, 145, 155, 175, 195 |
| Melting Point (Celsius) | number (deg C) | Melting point in degrees Celsius | 48, 54, 63, 68, 79, 91 |
| Oil Content | number (%) | Residual oil content by weight per ASTM D721 | 0.5, 1.0, 3.0, 10.0, 30.0 |
| Viscosity at 210F | number (SUS) | Saybolt Universal Seconds viscosity at 210 degrees F | 37, 42, 50, 65, 90 |
| Kinematic Viscosity at 100C | number (mm2/s) | Kinematic viscosity at 100 degrees C per ASTM D445 | 3.5, 5.2, 8.0, 15.0 |
| Penetration at 25C | number (dmm) | Needle penetration depth per ASTM D1321 (100g/5sec/25C) | 10, 15, 23, 33, 60 |
| Color | text | Color rating per ASTM D156 Saybolt or visual description | +21, +25, +30, White, Pale Yellow, Amber |
| Specific Gravity at 25C | number | Density relative to water at 25 degrees C | 0.880, 0.910, 0.920, 0.940 |
| Flash Point | number (deg C) | Minimum temperature at which vapors will ignite per ASTM D92 | 177, 200, 230, 260 |
| Congealing Point | number (deg C) | Temperature at which the wax solidifies per ASTM D938 | 48, 54, 60, 70 |
| Carbon Number Range | text | Range of carbon chain lengths in the product | C20-C36, C30-C60, C5-C6, C6-C12 |
| Boiling Range | text (deg C) | Distillation boiling range per ASTM D86 | 30-90 (light naphtha), 90-200 (heavy naphtha), 150-300 |
| Sulfur Content | number (ppm) | Total sulfur content | 1, 5, 50, 500 |
| Paraffin Content (PIONA) | number (%) | Percentage of paraffinic hydrocarbons in naphtha feedstock | 40, 55, 70, 85 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM wax testing standards (D87, D127, D721) and FDA food contact regulations | [IGI Wax](https://igiwax.com/products/petroleum-wax-types/), [IRM Wax Classification](https://www.irmwax.com/FAQ/Classification%20of%20petroleum%20waxes.aspx), [Hase Petroleum Wax](https://www.hpwax.com/wax.htm), [Hywax Petroleum Wax Types](https://www.hywax.com/blog/petroleum-wax-types) |
