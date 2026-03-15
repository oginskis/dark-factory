# SKU Schema: Welding Equipment & Supplies

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.welding_equipment_supplies`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | K2481-1, 951787, 0558102436, K5257-1 |
| Product Name | text | Full product name including key specs such as process type, amperage, and model | Lincoln PRO MIG 180 Wire Feed Welder, Miller Millermatic 355 MIG Welder, ESAB Rebel EMP 235ic |
| URL | text | Direct link to the product page | https://example.com/product/pro-mig-180 |
| Price | number | Numeric price per unit excluding currency symbol | 599.00, 2499.00, 4850.00, 12.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Category | enum | Whether the item is equipment or a consumable supply | Welding Machine, Filler Metal/Wire, Electrode/Rod, Welding Helmet, Welding Torch, Gas Regulator, Welding Clamp, Welding Cart, Safety Accessory |
| Model Number | text | Manufacturer model or series designation | Millermatic 355, PRO MIG 180, Rebel EMP 235ic, Powerwave S350 |
| Output Type | enum | Power source output characteristic | Constant Voltage (CV), Constant Current (CC), CV/CC Multi-Process |
| Wire/Electrode Type | text | Filler metal product form and classification | Solid Wire ER70S-6, Flux-Cored E71T-1, Stick Electrode E7018, Aluminum ER4043 |
| AWS Classification | text | American Welding Society filler metal classification | ER70S-3, ER70S-6, E7018, E71T-1, ER308L, E6013 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Shielding Gas Type | text | Required or recommended shielding gas | 75% Ar/25% CO2, 100% CO2, 100% Argon, Self-Shielded, 90% Ar/10% CO2 |
| Material Thickness Range | text | Maximum weldable material thickness | Up to 1/4 in, Up to 1/2 in, Up to 3/4 in |
| Base Material Compatibility | text (list) | Metals the equipment or consumable is designed for | Mild Steel, Stainless Steel, Aluminum, Cast Iron, Chrome-Moly |
| Display Type | text | Control panel display technology | Digital LED, LCD, Analog Meter, None |
| Country of Origin | text | Country where the product is manufactured | USA, Sweden, Austria, Italy, China |
| Welding Process | text (list) | Supported welding process types | MIG/GMAW, TIG/GTAW, Stick/SMAW, Flux-Cored/FCAW, Multi-Process, Plasma Cutting |
| Amperage Range | text (A) | Minimum to maximum output amperage | 30-180, 20-400, 25-160, 40-150 |
| Rated Output | text | Output current and voltage at rated duty cycle | 165A/22V, 310A/29.5V, 100A/19V |
| Duty Cycle | text | Percentage of 10-minute cycle at rated amperage | 30% at 180A, 60% at 100A, 100% at 80A |
| Input Phase | text | Electrical phase requirement | Single Phase, 3-Phase |
| Input Frequency | text (Hz) | Electrical supply frequency | 50/60, 60 |
| Wire Feed Speed | text | Wire feed speed range | 60-600 IPM, 1.5-15.2 m/min, 50-800 IPM |
| Welding Position | text (list) | Approved welding positions | Flat, Horizontal, Vertical Up, Vertical Down, Overhead, All Position |
| Polarity | text | Output polarity configuration | DCEP (DC+), DCEN (DC-), AC, AC/DC |
| Machine Dimensions (W x D x H) | text (in) | Overall equipment dimensions | 14 x 10.5 x 18, 22 x 17 x 30 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus AWS filler metal standards (A5.1, A5.18, A5.20) and EN 60974 welding equipment standard | [Lincoln Electric](https://www.lincolnelectric.com/en/), [Miller Electric (via CentralWelding)](https://www.centralwelding.com/welding-and-cutting-catalog/p/miller-millermatic-141-mig-welder), [ESAB Welding Equipment](https://esab.com/us/nam_en/products-solutions/categories/welding-equipment/), [Central Welding Supply Filler Metals](https://www.centralwelding.com/filler-metals) |
