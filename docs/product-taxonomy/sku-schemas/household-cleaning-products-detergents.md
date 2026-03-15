# SKU Schema: Household Cleaning Products & Detergents

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.household_cleaning_detergents`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 5037629800, B07L67Z4CQ, 24434557 |
| Product Name | text | Full product name including brand, product line, variant, scent, and size | Tide Original Liquid Laundry Detergent 132 fl oz 100 Loads, Mrs. Meyers Lemon Verbena Multi-Surface Cleaner 16 oz |
| URL | text | Direct link to the product page | https://tide.com/en-us/shop/type/liquid/tide-original-liquid |
| Price | number | Numeric unit price excluding currency symbol | 12.97, 5.99, 24.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary product classification | Laundry Detergent, All-Purpose Cleaner, Dish Soap, Disinfectant, Glass Cleaner, Bathroom Cleaner, Floor Cleaner, Bleach, Fabric Softener, Stain Remover, Dishwasher Detergent |
| Form | enum | Physical form of the product | Liquid, Powder, Gel, Pod/Pac, Tablet, Spray, Wipe, Foam, Concentrate |
| Surface Types | text (list) | Surfaces the product is designed to clean | All Surfaces, Glass, Stainless Steel, Wood, Tile, Granite, Fabric, Carpet |
| Active Ingredients | text (list) | Antimicrobial or cleaning active ingredients when disclosed | Sodium Hypochlorite, Quaternary Ammonium, Hydrogen Peroxide, Citric Acid, Alkyl Polyglucoside |
| Packaging Material | text | Primary packaging material | HDPE Bottle, PET Bottle, Cardboard Box, Refill Pouch, Spray Bottle |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the product is manufactured | USA, Germany, UK, Canada, Mexico |
| Volume | number (ml) | Volume for liquid products | 473, 946, 2840, 3785, 5000 |
| Scent | text | Fragrance name or description | Original, Lemon Verbena, Lavender, Free and Clear, Ocean Mist, Fresh Linen, Unscented |
| Fragrance Free | enum | Whether the product is unscented or fragrance-free | Yes, No |
| Concentration Level | enum | Whether the product is standard or concentrated formula | Standard, Concentrated, Ultra Concentrated |
| HE Compatible | enum | Whether the product is safe for high-efficiency washing machines | Yes, No |
| Disinfectant Claims | text (list) | Specific germ-killing claims made by the product | Kills 99.9% of Germs, Kills Bacteria, Kills Viruses, EPA Registered Disinfectant |
| EPA Registration Number | text | EPA registration number for products classified as disinfectants or pesticides | 5813-21, 777-114, 4091-20 |
| Plant-Based | enum | Whether the product uses primarily plant-derived cleaning ingredients | Yes, No, Partially |
| Dye Free | enum | Whether the product is free of artificial dyes | Yes, No |
| Phosphate Free | enum | Whether the product is phosphate-free | Yes, No |
| Chlorine Free | enum | Whether the product is chlorine-free | Yes, No |
| Biodegradable | enum | Whether the product is biodegradable | Yes, No |
| Pack Quantity | number | Number of units in the pack | 1, 2, 3, 4 |
| Dispensing Mechanism | enum | Type of dispenser | Pour, Trigger Spray, Pump, Screw Cap, Pod (single-use), Squeeze |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus EPA Safer Choice and GHS standards | [Tide Original Liquid](https://tide.com/en-us/shop/type/liquid/tide-original-liquid), [Persil Original Liquid](https://www.amazon.com/Persil-ProClean-Detergent-Original-Concentrated/dp/B07L67Z4CQ), [Mrs. Meyers Multi-Surface Cleaner](https://mrsmeyers.com/products/multi-surface-cleaner-basil), [Seventh Generation](https://www.seventhgeneration.com) |
