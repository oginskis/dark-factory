# SKU Schema: Climate Control Appliances (Fans, Heaters, Air Purifiers)

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.climate_control`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | HYF290B, HP07, DR-968H, GermGuardian AC4825 |
| Product Name | product_name | text | — | Full product name including key specs such as type, brand, and model | Honeywell QuietSet 8 Whole Room Oscillating Tower Fan, Dyson Purifier Cool TP07, De'Longhi Ceramic Tower Heater |
| URL | url | text | — | Direct link to the product page | https://example.com/product/tower-fan-hyf290b |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 49.99, 299.99, 89.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | product_type | enum | — | Primary appliance category | Fan, Heater, Air Purifier, Fan/Heater Combo, Fan/Purifier Combo |
| Sub-Type | sub-type | text | — | More specific product form factor | Tower Fan, Pedestal Fan, Box Fan, Desk Fan, Ceramic Heater, Radiant Heater, Oil-Filled Radiator, HEPA Purifier |
| Model Number | model_number | text | — | Manufacturer model or part number | HYF290B, TP07, TRD40615T, AC4825E |
| Filter Type | filter_type | text | — | Primary filtration technology (purifiers) | True HEPA, HEPA H13, Activated Carbon, Electrostatic, ULPA |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | China, Malaysia, Mexico, USA |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Power Rating | power_rating | number | W | Electrical power consumption in watts | 40, 1500, 55, 2200 |
| Frequency | frequency | text | Hz | Operating electrical frequency | 50, 60, 50/60 |
| CADR Smoke | cadr_smoke | number | CFM | Clean Air Delivery Rate for smoke particles (purifiers only) | 116, 200, 350 |
| CADR Dust | cadr_dust | number | CFM | Clean Air Delivery Rate for dust particles (purifiers only) | 120, 215, 400 |
| CADR Pollen | cadr_pollen | number | CFM | Clean Air Delivery Rate for pollen particles (purifiers only) | 130, 225, 450 |
| Room Coverage | room_coverage | number | sq ft | Recommended maximum room size | 150, 350, 900, 1500 |
| Airflow | airflow | number | CFM | Maximum airflow volume in cubic feet per minute (fans) | 14, 115, 350, 800 |
| Number of Speed Settings | number_of_speed_settings | number | — | Total number of fan or airflow speed levels | 3, 5, 8, 10 |
| Number of Heat Settings | number_of_heat_settings | number | — | Total number of heat output levels (heaters only) | 2, 3, 5 |
| Oscillation | oscillation | enum | — | Whether the unit oscillates to distribute air | Yes, No |
| Oscillation Angle | oscillation_angle | number | degrees | Range of oscillation arc | 70, 90, 180, 350 |
| Filter Life | filter_life | number | months | Recommended filter replacement interval | 6, 8, 12, 24 |
| Timer | timer | text | — | Available auto-off or programmable timer settings | 1-12 hours, 2/4/8 hours, 24-hour programmable |
| Noise Level | noise_level | number | dB | Sound level at lowest or specified setting | 24, 35, 50, 64 |
| Remote Control | remote_control | enum | — | Whether a remote control is included | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus AHAM CADR standard and Energy Star criteria | [Honeywell](https://www.honeywellpluggedin.com/fans/quietset-tower-fan/), [Dyson](https://www.dyson.com/air-treatment/air-purifiers), [De'Longhi](https://www.delonghi.com), [Grainger](https://www.grainger.com/category/hvac-and-refrigeration/air-treatment/air-cleaners/portable-air-cleaners) |
