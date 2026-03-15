# SKU Schema: Batteries & Portable Power

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.batteries_portable_power`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | MN1500B4, E91BP-4, EF-E1000V2 |
| Product Name | text | Full product name including key specs such as chemistry, size or capacity, and brand line | Duracell Coppertop AA Alkaline Battery 4-Pack, Jackery Explorer 1000 v2 Portable Power Station |
| URL | text | Direct link to the product page | https://example.com/product/coppertop-aa-4pk |
| Price | number | Numeric price per unit or pack, excluding currency symbol | 4.99, 29.95, 899.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD |
| Product Type | enum | Top-level product classification | Single-Use Battery, Rechargeable Battery, Portable Power Station, Battery Pack, Coin Cell, Button Cell |
| Battery Size/Form Factor | text | Standardised physical size designation | AA, AAA, C, D, 9V, CR2032, 18650, 21700, CR123A, AAAA |
| Inverter Type | enum | Type of AC waveform produced by the inverter | Pure Sine Wave, Modified Sine Wave |
| Country of Origin | text | Country where the product was manufactured | China, USA, Japan, South Korea |
| Nominal Voltage | number (V) | Rated voltage under normal discharge conditions | 1.2, 1.5, 3.0, 3.7, 12.0 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Battery Chemistry | text | Electrochemical system used for energy storage | Alkaline, Lithium Primary, Lithium-Ion, LiFePO4, NiMH, NiCd, Lead Acid, Zinc Air, Silver Oxide |
| AC Output Power | number (W) | Maximum continuous AC output wattage for portable power stations | 300, 500, 1000, 1500, 4000 |
| AC Surge Power | number (W) | Peak momentary AC wattage for motor startup loads | 500, 1000, 2000, 8000 |
| USB-C Output | text | USB Type-C port power delivery specification | 100W PD, 60W PD, 20W |
| USB-A Output | text | USB Type-A port power specification | 5V 2.4A, QC 3.0 18W, 5V 1A |
| DC Output | text | 12V DC car-port or barrel-plug output specification | 12V 10A, 12V 8A |
| Number of AC Outlets | number | Count of AC output receptacles on a portable power station | 1, 2, 3, 6 |
| Solar Charging Input | number (W) | Maximum solar panel charging wattage supported | 100, 200, 400, 2600 |
| Wall Charging Time | text | Time to fully charge from a wall outlet | 1 hr, 2 hr, 5.5 hr, 7.5 hr |
| Cycle Life | number | Number of charge-discharge cycles before capacity drops to 80% | 500, 1000, 2500, 4000 |
| Shelf Life | number (years) | Expected storage life before significant capacity loss | 2, 5, 8, 10, 15 |
| Dimensions (L x W x H) | text (mm) | Physical dimensions of the battery or power station | 50.5 x 14.5 dia, 340 x 262 x 255 |
| Operating Temperature Min | number (deg C) | Minimum ambient temperature for safe operation or discharge | -20, -10, 0 |
| Operating Temperature Max | number (deg C) | Maximum ambient temperature for safe operation or discharge | 40, 45, 60 |
| Charging Temperature Min | number (deg C) | Minimum temperature for safe recharging | -10, 0, 10 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 sources plus industry standards (IEC 60086, IEC 62133, UN38.3) | [Duracell](https://duracell.com/techlibrary/product-technical-data-sheets), [EcoFlow](https://www.ecoflow.com/us/blog/ecoflow-portable-power-station-specs), [Jackery](https://www.jackery.com/products/explorer-1000-portable-power-station), [MIT Battery Specifications Guide](https://web.mit.edu/evt/summary_battery_specifications.pdf) |
