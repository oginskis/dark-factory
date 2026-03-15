# SKU Schema: Animal Feed & Supplements

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.animal_feed_supplements`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 3003591-206, TSC-4412850, PUR-0046612 |
| Product Name | text | Full product name including key specs such as animal type, protein level, form, and weight | Purina Wind and Rain All Season 4 Beef Cattle Mineral Tub 125 lb, DuMOR 16% Protein Livestock Supplement 200 lb |
| URL | text | Direct link to the product page | https://example.com/product/cattle-mineral-tub-125lb |
| Price | number | Numeric price per unit (bag, tub, block, pail, or ton), excluding currency symbol | 54.99, 129.99, 18.49, 425.00 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, GBP, AUD |
| Animal Class | text | Life stage or production class within the target species | Cow-Calf, Weaned Calf, Grower-Finisher, Lactating, Breeding, Layer, Broiler, Starter |
| Feed Type | enum | Primary classification of the feed product | Complete Feed, Supplement, Mineral, Vitamin Premix, Milk Replacer, Protein Supplement, Medicated Feed, Scratch Grain |
| Form | enum | Physical form of the feed product | Pellet, Crumble, Tub, Block, Meal, Liquid, Mash, Textured, Cube, Powder, Granule |
| Active Drug Ingredient | text | Name of the active pharmaceutical ingredient in medicated feeds | Monensin, Lasalocid, Decoquinate, Chlortetracycline |
| Ingredient List | text (list) | Primary ingredients in descending order by weight | Processed Grain By-Products, Molasses Products, Soybean Meal, Calcium Carbonate, Salt, Monocalcium Phosphate |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Packaging Type | enum | Type of container or packaging | Bag, Tub, Block, Pail, Bulk, Drum |
| Country of Origin | text | Country where the product was manufactured | USA, Canada, Netherlands, Brazil |
| Animal Species | text (list) | Target animal species the product is formulated for | Cattle, Horse, Poultry, Swine, Goat, Sheep, Rabbit, Deer, Fish |
| Crude Protein Min | number (%) | Guaranteed minimum crude protein content | 12, 16, 20, 30, 38 |
| Crude Fat Min | number (%) | Guaranteed minimum crude fat content | 2.0, 3.5, 5.0, 8.0 |
| Crude Fiber Max | number (%) | Guaranteed maximum crude fiber content | 6.0, 12.0, 15.0, 25.0 |
| Moisture Max | number (%) | Guaranteed maximum moisture content | 10.0, 12.0, 18.0 |
| Calcium Min | number (%) | Guaranteed minimum calcium content | 1.5, 3.0, 5.0, 12.0 |
| Calcium Max | number (%) | Guaranteed maximum calcium content | 2.0, 4.0, 6.0, 14.0 |
| Phosphorus Min | number (%) | Guaranteed minimum phosphorus content | 0.5, 1.0, 4.0, 6.0 |
| Salt Min | number (%) | Guaranteed minimum salt (sodium chloride) content | 1.0, 3.5, 10.0 |
| Salt Max | number (%) | Guaranteed maximum salt (sodium chloride) content | 2.0, 4.5, 12.0 |
| Medicated | boolean | Whether the product contains a veterinary drug or feed additive requiring a veterinary feed directive | true, false |
| Medication Purpose | text | Intended purpose of the medication or additive | Coccidiosis Prevention, Growth Promotion, Horn Fly Control, Bloat Prevention |
| Feeding Rate | text | Recommended daily feeding amount per animal | 0.1 lb per 100 lb body weight, 2-4 oz per head per day, Free choice |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus AAFCO feed labeling standards and USDA organic feed regulations | [Tractor Supply Co.](https://www.tractorsupply.com/a/cattle-feed-supplements), [Purina Mills](https://www.purinamills.com/), [Alltech](https://www.alltech.com/animal-nutrition/products), [Trouw Nutrition](https://www.trouwnutrition.com/) |
