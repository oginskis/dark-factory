# SKU Schema: Animal Feed & Supplements

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.animal_feed_supplements`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 3003591-206, TSC-4412850, PUR-0046612 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as animal type, protein level, form, and weight | Purina Wind and Rain All Season 4 Beef Cattle Mineral Tub 125 lb, DuMOR 16% Protein Livestock Supplement 200 lb |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/cattle-mineral-tub-125lb |
| Price | price | number | — | yes | Numeric price per unit (bag, tub, block, pail, or ton), excluding currency symbol | 54.99, 129.99, 18.49, 425.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, CAD, EUR, GBP, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Animal Class | animal_class | text | — | — | Life stage or production class within the target species | Cow-Calf, Weaned Calf, Grower-Finisher, Lactating, Breeding, Layer, Broiler, Starter |
| Feed Type | feed_type | enum | — | — | Primary classification of the feed product | Complete Feed, Supplement, Mineral, Vitamin Premix, Milk Replacer, Protein Supplement, Medicated Feed, Scratch Grain |
| Form | form | enum | — | — | Physical form of the feed product | Pellet, Crumble, Tub, Block, Meal, Liquid, Mash, Textured, Cube, Powder, Granule |
| Active Drug Ingredient | active_drug_ingredient | text | — | — | Name of the active pharmaceutical ingredient in medicated feeds | Monensin, Lasalocid, Decoquinate, Chlortetracycline |
| Ingredient List | ingredient_list | text (list) | — | — | Primary ingredients in descending order by weight | Processed Grain By-Products, Molasses Products, Soybean Meal, Calcium Carbonate, Salt, Monocalcium Phosphate |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Packaging Type | packaging_type | enum | — | — | Type of container or packaging | Bag, Tub, Block, Pail, Bulk, Drum |
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured | USA, Canada, Netherlands, Brazil |
| Animal Species | animal_species | text (list) | — | — | Target animal species the product is formulated for | Cattle, Horse, Poultry, Swine, Goat, Sheep, Rabbit, Deer, Fish |
| Crude Protein Min | crude_protein_min | number | % | — | Guaranteed minimum crude protein content | 12, 16, 20, 30, 38 |
| Crude Fat Min | crude_fat_min | number | % | — | Guaranteed minimum crude fat content | 2.0, 3.5, 5.0, 8.0 |
| Crude Fiber Max | crude_fiber_max | number | % | — | Guaranteed maximum crude fiber content | 6.0, 12.0, 15.0, 25.0 |
| Moisture Max | moisture_max | number | % | — | Guaranteed maximum moisture content | 10.0, 12.0, 18.0 |
| Calcium Min | calcium_min | number | % | — | Guaranteed minimum calcium content | 1.5, 3.0, 5.0, 12.0 |
| Calcium Max | calcium_max | number | % | — | Guaranteed maximum calcium content | 2.0, 4.0, 6.0, 14.0 |
| Phosphorus Min | phosphorus_min | number | % | — | Guaranteed minimum phosphorus content | 0.5, 1.0, 4.0, 6.0 |
| Salt Min | salt_min | number | % | — | Guaranteed minimum salt (sodium chloride) content | 1.0, 3.5, 10.0 |
| Salt Max | salt_max | number | % | — | Guaranteed maximum salt (sodium chloride) content | 2.0, 4.5, 12.0 |
| Medicated | medicated | boolean | — | — | Whether the product contains a veterinary drug or feed additive requiring a veterinary feed directive | true, false |
| Medication Purpose | medication_purpose | text | — | — | Intended purpose of the medication or additive | Coccidiosis Prevention, Growth Promotion, Horn Fly Control, Bloat Prevention |
| Feeding Rate | feeding_rate | text | — | — | Recommended daily feeding amount per animal | 0.1 lb per 100 lb body weight, 2-4 oz per head per day, Free choice |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus AAFCO feed labeling standards and USDA organic feed regulations | [Tractor Supply Co.](https://www.tractorsupply.com/a/cattle-feed-supplements), [Purina Mills](https://www.purinamills.com/), [Alltech](https://www.alltech.com/animal-nutrition/products), [Trouw Nutrition](https://www.trouwnutrition.com/) |
