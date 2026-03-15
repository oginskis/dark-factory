# SKU Schema: Climate Control Appliances (Fans, Heaters, Air Purifiers)

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.climate_control`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HYF290B, HP07, DR-968H, GermGuardian AC4825 |
| Product Name | text | Full product name including key specs such as type, brand, and model | Honeywell QuietSet 8 Whole Room Oscillating Tower Fan, Dyson Purifier Cool TP07, De'Longhi Ceramic Tower Heater |
| URL | text | Direct link to the product page | https://example.com/product/tower-fan-hyf290b |
| Price | number | Numeric price per unit excluding currency symbol | 49.99, 299.99, 89.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | enum | Primary appliance category | Fan, Heater, Air Purifier, Fan/Heater Combo, Fan/Purifier Combo |
| Sub-Type | text | More specific product form factor | Tower Fan, Pedestal Fan, Box Fan, Desk Fan, Ceramic Heater, Radiant Heater, Oil-Filled Radiator, HEPA Purifier |
| Model Number | text | Manufacturer model or part number | HYF290B, TP07, TRD40615T, AC4825E |
| Filter Type | text | Primary filtration technology (purifiers) | True HEPA, HEPA H13, Activated Carbon, Electrostatic, ULPA |
| Country of Origin | text | Country where the product was manufactured | China, Malaysia, Mexico, USA |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Power Rating | number (W) | Electrical power consumption in watts | 40, 1500, 55, 2200 |
| Frequency | text (Hz) | Operating electrical frequency | 50, 60, 50/60 |
| CADR Smoke | number (CFM) | Clean Air Delivery Rate for smoke particles (purifiers only) | 116, 200, 350 |
| CADR Dust | number (CFM) | Clean Air Delivery Rate for dust particles (purifiers only) | 120, 215, 400 |
| CADR Pollen | number (CFM) | Clean Air Delivery Rate for pollen particles (purifiers only) | 130, 225, 450 |
| Room Coverage | number (sq ft) | Recommended maximum room size | 150, 350, 900, 1500 |
| Airflow | number (CFM) | Maximum airflow volume in cubic feet per minute (fans) | 14, 115, 350, 800 |
| Number of Speed Settings | number | Total number of fan or airflow speed levels | 3, 5, 8, 10 |
| Number of Heat Settings | number | Total number of heat output levels (heaters only) | 2, 3, 5 |
| Oscillation | enum | Whether the unit oscillates to distribute air | Yes, No |
| Oscillation Angle | number (degrees) | Range of oscillation arc | 70, 90, 180, 350 |
| Filter Life | number (months) | Recommended filter replacement interval | 6, 8, 12, 24 |
| Timer | text | Available auto-off or programmable timer settings | 1-12 hours, 2/4/8 hours, 24-hour programmable |
| Noise Level | number (dB) | Sound level at lowest or specified setting | 24, 35, 50, 64 |
| Remote Control | enum | Whether a remote control is included | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus AHAM CADR standard and Energy Star criteria | [Honeywell](https://www.honeywellpluggedin.com/fans/quietset-tower-fan/), [Dyson](https://www.dyson.com/air-treatment/air-purifiers), [De'Longhi](https://www.delonghi.com), [Grainger](https://www.grainger.com/category/hvac-and-refrigeration/air-treatment/air-cleaners/portable-air-cleaners) |
