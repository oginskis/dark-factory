# SKU Schema: Pet Food & Pet Care Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.pet_food_pet_care`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 14926, PRO-PLN-CHK-35, B07DC8BR3B |
| Product Name | text | Full product name including brand, product line, protein, and size | Purina Pro Plan Adult Chicken and Rice 35 lb, Blue Buffalo Wilderness Salmon Cat Food 12 lb, Frontline Plus for Dogs |
| URL | text | Direct link to the product page | https://example.com/product/dog-food-chicken-35lb |
| Price | number | Numeric price per package or unit, excluding currency symbol | 9.99, 34.98, 64.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Primary product type within pet care | Dry Food, Wet Food, Treats, Flea and Tick, Grooming, Supplements, Litter, Toys, Beds, Collars and Leashes |
| Pet Type | enum | Target animal species | Dog, Cat, Fish, Bird, Small Animal, Reptile |
| Food Form | enum | Physical form of the food product | Kibble, Pate, Shredded, Stew, Semi-Moist, Freeze-Dried, Raw |
| Ingredients Source | enum | Quality tier or sourcing claim | Natural, Organic, Human-Grade, Non-GMO, Sustainably Sourced |
| Country of Origin | text | Country where the product is manufactured | USA, Canada, France, Thailand |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Life Stage | enum | Age or developmental stage the product is designed for | Puppy, Kitten, Adult, Senior, All Life Stages |
| Primary Protein | text | Main protein source in food products | Chicken, Salmon, Beef, Lamb, Turkey, Venison, Duck |
| Flavor | text | Flavor variant or combination | Chicken and Rice, Salmon and Sweet Potato, Beef Stew, Ocean Fish |
| Pack Quantity | number | Number of cans, pouches, or units per pack | 1, 6, 12, 24, 30 |
| Guaranteed Analysis - Crude Protein | text (%) | Minimum crude protein content as percentage | 26%, 30%, 38% |
| Guaranteed Analysis - Crude Fat | text (%) | Minimum crude fat content as percentage | 12%, 16%, 20% |
| Guaranteed Analysis - Crude Fiber | text (%) | Maximum crude fiber content as percentage | 3%, 4.5%, 6% |
| Guaranteed Analysis - Moisture | text (%) | Maximum moisture content as percentage | 10%, 12%, 78% |
| AAFCO Statement | text | Nutritional adequacy statement per AAFCO guidelines | Complete and Balanced for Adult Maintenance, Complete and Balanced for Growth |
| Special Diet | text (list) | Dietary features or restrictions | Grain-Free, Limited Ingredient, High-Protein, Weight Management, Sensitive Stomach, Prescription |
| Health Benefit | text (list) | Targeted health support claims | Joint Support, Digestive Health, Skin and Coat, Immune Support, Dental Health |
| Caloric Content | text (kcal) | Energy content per unit | 380 kcal/cup, 175 kcal/can, 3500 kcal/kg |
| Shelf Life | text | Stated shelf life or best-by period | 18 months, 24 months |
| UPC | text | Universal Product Code barcode number | 038100175854, 859610006489 |
| Product Line | text | Sub-brand or product series | Pro Plan Sport, Wilderness, Science Diet Sensitive, Prescription Diet |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus AAFCO nutritional standards and labeling requirements | [PetSmart](https://www.petsmart.com/dog/food-and-treats/dry-food/), [Chewy](https://www.chewy.com/b/dog-food-332), [Purina](https://www.purina.com/dogs/dog-food), [AAFCO](https://www.aafco.org/consumers/understanding-pet-food/reading-labels/) |
