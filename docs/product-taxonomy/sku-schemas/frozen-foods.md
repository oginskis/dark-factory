# SKU Schema: Frozen Foods

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.frozen_foods`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor product identifier | 877RE220068, FRZ-PZ-24CS, 403340060121 |
| Product Name | text | Full product name including key descriptors such as product type, flavor, and pack configuration | Still Riding Foods Gluten-Free Pizza 5 in. Square - 24/Case, IQF 5 Way Mixed Vegetable Blend 2.5 lb. - 12/Case |
| URL | text | Direct link to the product page | https://example.com/product/frozen-pizza-24-case |
| Price | number | Numeric price per selling unit (case or individual), excluding currency symbol | 49.92, 72.49, 15.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Primary frozen food classification | Frozen Vegetables, Frozen Fruit, Frozen Pizza, Frozen Entrees, Frozen Seafood, Frozen Meat, Frozen Poultry, Frozen Desserts, Frozen Appetizers, Frozen Bread and Dough, Frozen Breakfast |
| Protein Type | text | Primary protein in the product, if applicable | Chicken, Beef, Pork, Fish, Shrimp, Turkey, Plant-Based, None |
| Country of Origin | text | Country where the product was manufactured or processed | USA, Canada, Mexico, Thailand, China, Belgium |
| Ingredient Statement | text | Full list of ingredients as declared on the product label | Water, Enriched Flour, Mozzarella Cheese, Tomato Sauce, Soybean Oil |
| Net Weight Per Unit | number (g) | Net weight of a single unit within the case | 142, 340, 454, 907, 1134 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Flavor or Variety | text | Specific flavor, variety, or filling description | Cheese, Pepperoni, Mixed Vegetable, Strawberry, Buffalo Chicken |
| Pack Quantity | number | Number of individual units per selling unit or case | 1, 6, 12, 24, 48 |
| Preparation Method | text (list) | Recommended methods of cooking or preparation | Oven Bake, Microwave, Deep Fry, Air Fry, Stovetop, Boil, Steam |
| Cooking Temperature | number (°F) | Recommended oven or cooking temperature | 350, 375, 400, 425, 450 |
| Cooking Time | text | Recommended cooking duration | 8-12 min, 15-20 min, 25-30 min, 3-4 min |
| Storage Temperature | number (°F) | Required freezer storage temperature or below | 0, -10, -18 |
| Shelf Life Frozen | number (months) | Expected shelf life when stored at recommended frozen temperature | 6, 12, 18, 24 |
| Ships Frozen | boolean | Whether the product is shipped frozen with cold chain logistics | true, false |
| Allergens | text (list) | Declared allergens present in the product | Wheat, Milk, Egg, Soy, Fish, Shellfish, Tree Nuts, Peanuts, Sesame, None |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications the product carries | Gluten-Free, Organic, Vegan, Vegetarian, Kosher, Halal, Non-GMO |
| Certifications | text (list) | Quality, safety, or regulatory certifications | USDA Organic, HACCP, SQF, BRC, IFS, GMP |
| USDA Child Nutrition | boolean | Whether the product meets USDA Child Nutrition program requirements | true, false |
| IQF | boolean | Whether the product uses Individual Quick Freezing technology | true, false |
| UPC | text | Universal Product Code or EAN barcode number | 400016851694, 071421001123 |
| GTIN | text | Global Trade Item Number for the selling unit | 00400016851694, 10071421001120 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 sources plus industry standards (HACCP, GS1 GDSN, Open Food Facts data model) | [WebstaurantStore](https://www.webstaurantstore.com/search/frozen-food.html), [Still Riding Foods Product Page](https://www.webstaurantstore.com/pizza-5in-gluten-free-24-case-still-riding-foods/878STI612306.html), [Sysco Frozen Catalog](https://foodie.sysco.com/sysco-products/), [FrozenFoodInc](https://frozenfoodinc.com/) |
