# SKU Schema: Dairy Products

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.dairy`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DRY-10042, 070470496511, PD-8831 |
| Product Name | text | Full product name including brand, type, fat level, and size | Organic Valley Whole Milk 1 Gallon, Tillamook Medium Cheddar 8oz Block, Chobani Vanilla Greek Yogurt 5.3oz |
| URL | text | Direct link to the product page | https://example.com/product/organic-valley-whole-milk |
| Price | number | Numeric price per selling unit, excluding currency symbol | 4.99, 3.49, 1.29, 6.79 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Dairy Type | enum | Primary type of dairy product | Milk, Cheese, Yogurt, Butter, Cream, Ice Cream, Sour Cream, Cottage Cheese, Kefir |
| Pasteurization Type | enum | Heat treatment method used in processing | Pasteurized, Ultra-Pasteurized, UHT, Raw, HTST |
| Cheese Type | text | Specific cheese variety, applicable to cheese products only | Cheddar, Mozzarella, Brie, Gouda, Parmesan, Swiss, Feta, Cream Cheese |
| Cheese Form | enum | Physical format of the cheese product | Block, Sliced, Shredded, Crumbled, Spread, Wheel, Wedge, String |
| Packaging Type | enum | Primary packaging material and form | Tub, Carton, Bottle, Cup, Bag, Foil Wrap, Wax Paper, Block Wrap |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the product was manufactured or sourced | USA, France, Ireland, Netherlands, Greece, New Zealand |
| USDA Grade | text | USDA quality grade designation where applicable | Grade AA, Grade A, Grade B |
| Manufacturer | text | Company that produces the product, if different from brand | Lactalis, Saputo, Dairy Farmers of America |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 070470496511, 5021345001022 |
| Milk Source | enum | Animal source of the milk used | Cow, Goat, Sheep, Buffalo, Plant-Based |
| Fat Content | text | Fat percentage or fat designation as stated on the label | 3.25%, 2%, 1%, 0%, Whole, Reduced Fat, Low Fat, Fat Free |
| Net Volume | number (ml) | Net volume for liquid dairy products | 236, 473, 946, 1893, 3785 |
| Cheese Texture | enum | Texture classification for cheese products | Fresh, Soft, Semi-Soft, Semi-Hard, Hard, Very Hard |
| Aging Duration | text | Length of time the product has been aged or ripened | 3 months, 6 months, 12 months, 24 months, Unaged |
| Yogurt Style | enum | Style or preparation method for yogurt products | Greek, Regular, Icelandic (Skyr), Australian, Drinkable, Plant-Based |
| Live Cultures | boolean | Whether the product contains live and active cultures | true, false |
| Flavor/Variety | text | Specific flavor or variety of the product | Plain, Strawberry, Vanilla, Blueberry, Garlic Herb, Salted, Unsalted |
| Organic | boolean | Whether the product is certified organic | true, false |
| Storage Temperature | text | Required storage temperature range | 1-4C, -18C or below, Room Temperature |
| Shelf Life | number (days) | Expected shelf life from date of manufacture under proper storage | 14, 21, 60, 90, 180, 365 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from dairy distributors, USDA dairy standards, and FDA standards of identity for dairy products | [Honor Foods](https://www.honorfoods.com/dairy-products/), [ThinkUSAdairy Supplier Directory](https://www.thinkusadairy.org/applications/supplier-search), [Penn State Dairy Food Standards](https://extension.psu.edu/dairy-food-standards), [American Cheese Society](https://www.cheesesociety.org/competition/cheese-entry-categories) |
