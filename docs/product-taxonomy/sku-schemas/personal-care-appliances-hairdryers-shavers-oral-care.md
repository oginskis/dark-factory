# SKU Schema: Personal Care Appliances (Hairdryers, Shavers, Oral Care)

**Last updated:** 2026-03-15
**Parent category:** Household Appliances
**Taxonomy ID:** `appliances.personal_care`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HD435, 8567cc, iO9-4A, EH-NA67-W |
| Product Name | text | Full product name including key specs such as type, brand, and model | Braun Series 8 Electric Shaver 8567cc, Dyson Supersonic Hair Dryer, Oral-B iO Series 9 Electric Toothbrush |
| URL | text | Direct link to the product page | https://example.com/product/braun-series-8-8567cc |
| Price | number | Numeric price per unit excluding currency symbol | 29.99, 149.99, 279.99, 429.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | enum | Primary appliance category | Hair Dryer, Electric Shaver, Electric Toothbrush, Hair Straightener, Hair Curler, Trimmer, Epilator, IPL Device |
| Model Number | text | Manufacturer model or part number | 8567cc, HD07, iO Series 9, EH-NA67-W, S9502/83 |
| Motor Type | text | Type of motor technology used | Dyson V9 Digital Motor, Linear Motor, Sonic, Rotary, Foil Oscillating |
| Battery Type | text | Battery chemistry | Lithium-Ion, NiMH |
| Display Type | text | Type of information display on the device | LED, LCD, OLED, None |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the product was manufactured | Germany, Japan, China, Hungary |
| Motor Speed | number (RPM) | Maximum motor or oscillation speed | 2100, 8800, 40000, 110000 |
| Cutting/Brushing Actions | number (per min) | Strokes, pulsations, or cutting actions per minute (shavers and toothbrushes) | 8800, 20000, 30000, 31000, 62000 |
| Power Rating | number (W) | Electrical power consumption | 1200, 1600, 1875, 2200 |
| Number of Heat Settings | number | Heat or temperature level options (hair dryers, straighteners) | 2, 3, 4, 5 |
| Number of Speed Settings | number | Airflow or motor speed level options | 2, 3, 4 |
| Operating Modes | text (list) | Named cleaning or operating modes | Daily Clean, Whitening, Sensitive, Gum Care, Turbo, Gentle, Standard |
| Number of Operating Modes | number | Total count of selectable operating or cleaning modes | 2, 3, 5, 7 |
| Corded/Cordless | enum | Power source type | Corded, Cordless, Corded and Cordless |
| Battery Runtime | number (min) | Maximum runtime on a full charge | 20, 45, 60, 120 |
| Charge Time | number (h) | Time to fully recharge the battery | 1, 3, 5, 16 |
| Fast Charge | text | Quick-charge duration and resulting runtime | 5 min charge for 1 shave, 3 hours for full charge |
| Wet/Dry Use | enum | Whether the device can be used with water or shaving foam | Dry Only, Wet and Dry |
| Shaving System | text | Cutting element technology (shavers only) | Foil 4+1, Rotary 3-Head, Lift and Cut, CloseCut |
| Ionic Technology | enum | Whether the device emits ions to reduce frizz (hair dryers) | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus ADA oral care standards | [Braun](https://us.braun.com/en-us/male-grooming/electric-shavers/series-8-8567cc), [Dyson](https://www.dyson.com/hair-care/hair-dryers/supersonic), [Oral-B](https://oralb.com/en-us/products/compare/electric-toothbrushes), [Panasonic](https://shop.panasonic.com/pages/personalcare) |
