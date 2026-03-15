# SKU Schema: Floor Care & Cleaning Appliances

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.floor_care_cleaning`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | IP3251, RVA101, 1940A, V15-DETECT |
| Product Name | text | Full product name including key specs such as type, brand, and model | Shark PowerDetect Clean and Empty Cordless Stick Vacuum, iRobot Roomba Combo j9+, Bissell PowerFresh Steam Mop |
| URL | text | Direct link to the product page | https://example.com/product/shark-powerdetect-ip3251 |
| Price | number | Numeric price per unit excluding currency symbol | 149.99, 499.99, 89.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | enum | Primary appliance category | Upright Vacuum, Stick Vacuum, Robot Vacuum, Canister Vacuum, Handheld Vacuum, Carpet Cleaner, Steam Mop, Wet/Dry Vacuum |
| Model Number | text | Manufacturer model or part number | IP3251, j9+, 1940A, V15 Detect, Roborock S8 Pro |
| Battery Type | text | Battery chemistry | Lithium-Ion, NiMH |
| Filtration Type | text | Primary filtration technology | HEPA, HEPA H13, Cyclonic, Washable Foam, Multi-Stage |
| Brush Roll Type | text | Type of agitation mechanism on the cleaning head | Motorized Brush Roll, Dual Brush Roll, Rubber Extractors, Self-Cleaning Brush Roll, Soft Roller |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the product was manufactured | China, Malaysia, Germany, USA |
| Corded/Cordless | enum | Power source type | Corded, Cordless |
| Power Rating | number (W) | Motor or appliance power consumption (corded models) | 1000, 1200, 1500, 1600 |
| Suction Power | number (AW) | Maximum suction power in air watts | 80, 150, 230, 262 |
| Battery Runtime | number (min) | Maximum runtime on a full charge at lowest power setting | 40, 60, 70, 90, 120 |
| Charge Time | number (h) | Time to fully recharge the battery | 2.5, 3.5, 4.0, 6.0 |
| Auto-Empty Interval | text | How long the auto-empty base holds debris before emptying | 30 days, 45 days, 60 days |
| Filtration Efficiency | text | Particle capture rate and minimum particle size | 99.97% at 0.3 microns, 99.99% at 0.3 microns |
| Cleaning Path Width | number (mm) | Width of the cleaning head or brush roll | 250, 270, 305, 340 |
| Navigation Technology | text | Navigation method for robot vacuums | Random Bounce, Gyroscope, LiDAR, Camera (vSLAM), PrecisionVision |
| Mopping Function | enum | Whether the unit includes a mopping capability | Yes, No |
| Steam Ready Time | number (s) | Time to produce steam from cold start (steam mops) | 15, 30, 45 |
| Noise Level | number (dB) | Sound level at standard operating mode | 65, 72, 78, 85 |
| Smart Connectivity | text (list) | Smart home or app connectivity protocols | Wi-Fi, Bluetooth, Alexa, Google Home, Apple HomeKit |
| Dimensions (H x W x D) | text (mm) | Product height, width, and depth | 1150 x 270 x 250, 348 x 348 x 87 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus industry filtration standards | [Shark](https://www.sharkninja.com/), [Dyson](https://www.dyson.com/vacuum-cleaners), [iRobot](https://www.irobot.com/en_US/comparison-chart.html), [Bissell](https://www.bissell.com/) |
