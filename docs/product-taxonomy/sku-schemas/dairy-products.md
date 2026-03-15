# SKU Schema: Dairy Products

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.dairy`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | DRY-10042, 070470496511, PD-8831 |
| Product Name | product_name | text | Full product name including brand, type, fat level, and size | Organic Valley Whole Milk 1 Gallon, Tillamook Medium Cheddar 8oz Block, Chobani Vanilla Greek Yogurt 5.3oz |
| URL | url | text | Direct link to the product page | https://example.com/product/organic-valley-whole-milk |
| Price | price | number | Numeric price per selling unit, excluding currency symbol | 4.99, 3.49, 1.29, 6.79 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Dairy Type | dairy_type | enum | Primary type of dairy product | Milk, Cheese, Yogurt, Butter, Cream, Ice Cream, Sour Cream, Cottage Cheese, Kefir |
| Pasteurization Type | pasteurization_type | enum | Heat treatment method used in processing | Pasteurized, Ultra-Pasteurized, UHT, Raw, HTST |
| Cheese Type | cheese_type | text | Specific cheese variety, applicable to cheese products only | Cheddar, Mozzarella, Brie, Gouda, Parmesan, Swiss, Feta, Cream Cheese |
| Cheese Form | cheese_form | enum | Physical format of the cheese product | Block, Sliced, Shredded, Crumbled, Spread, Wheel, Wedge, String |
| Packaging Type | packaging_type | enum | Primary packaging material and form | Tub, Carton, Bottle, Cup, Bag, Foil Wrap, Wax Paper, Block Wrap |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the product was manufactured or sourced | USA, France, Ireland, Netherlands, Greece, New Zealand |
| USDA Grade | usda_grade | text | USDA quality grade designation where applicable | Grade AA, Grade A, Grade B |
| Manufacturer | manufacturer | text | Company that produces the product, if different from brand | Lactalis, Saputo, Dairy Farmers of America |
| UPC/EAN | upcean | text | Universal Product Code or European Article Number barcode | 070470496511, 5021345001022 |
| Milk Source | milk_source | enum | Animal source of the milk used | Cow, Goat, Sheep, Buffalo, Plant-Based |
| Fat Content | fat_content | text | Fat percentage or fat designation as stated on the label | 3.25%, 2%, 1%, 0%, Whole, Reduced Fat, Low Fat, Fat Free |
| Net Volume | net_volume | number (ml) | Net volume for liquid dairy products | 236, 473, 946, 1893, 3785 |
| Cheese Texture | cheese_texture | enum | Texture classification for cheese products | Fresh, Soft, Semi-Soft, Semi-Hard, Hard, Very Hard |
| Aging Duration | aging_duration | text | Length of time the product has been aged or ripened | 3 months, 6 months, 12 months, 24 months, Unaged |
| Yogurt Style | yogurt_style | enum | Style or preparation method for yogurt products | Greek, Regular, Icelandic (Skyr), Australian, Drinkable, Plant-Based |
| Live Cultures | live_cultures | boolean | Whether the product contains live and active cultures | true, false |
| Flavor/Variety | flavorvariety | text | Specific flavor or variety of the product | Plain, Strawberry, Vanilla, Blueberry, Garlic Herb, Salted, Unsalted |
| Organic | organic | boolean | Whether the product is certified organic | true, false |
| Storage Temperature | storage_temperature | text | Required storage temperature range | 1-4C, -18C or below, Room Temperature |
| Shelf Life | shelf_life | number (days) | Expected shelf life from date of manufacture under proper storage | 14, 21, 60, 90, 180, 365 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from dairy distributors, USDA dairy standards, and FDA standards of identity for dairy products | [Honor Foods](https://www.honorfoods.com/dairy-products/), [ThinkUSAdairy Supplier Directory](https://www.thinkusadairy.org/applications/supplier-search), [Penn State Dairy Food Standards](https://extension.psu.edu/dairy-food-standards), [American Cheese Society](https://www.cheesesociety.org/competition/cheese-entry-categories) |
