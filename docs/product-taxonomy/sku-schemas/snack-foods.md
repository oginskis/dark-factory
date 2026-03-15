# SKU Schema: Snack Foods

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.snack_foods`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor product identifier | 999CHIP001, SNK-LAY-24, 103MART0016 |
| Product Name | text | Full product name including key descriptors such as type, flavor, and pack configuration | Martin's Sea Salt Potato Chips 1 oz. - 30/Case, Herr's Sour Cream and Onion Rippled Chips 2.75 oz. - 24/Case |
| URL | text | Direct link to the product page | https://example.com/product/sea-salt-chips-30pk |
| Price | number | Numeric price per selling unit (case, box, or individual), excluding currency symbol | 18.99, 24.50, 42.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Snack Type | enum | Primary snack product classification | Potato Chips, Tortilla Chips, Pretzels, Popcorn, Crackers, Nuts and Seeds, Cookies, Puffed Snacks, Rice Cakes, Jerky, Granola Bars, Trail Mix, Cheese Snacks, Fruit Snacks |
| Packaging Format | enum | How individual units are packaged for sale | Individually Wrapped, Bulk Bag, Multi-Pack Box, Canister, Tub, Clip Strip |
| Country of Origin | text | Country where the product was manufactured or processed | USA, Canada, Mexico, UK, Germany |
| Ingredient Statement | text | Full list of ingredients as declared on the product label | Potatoes, Vegetable Oil (Sunflower, Corn, and/or Canola Oil), Sea Salt |
| Net Weight Per Unit | number (g) | Net weight of a single bag or package | 23, 28, 42, 78, 198, 283, 454 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Flavor | text | Specific flavor or seasoning of the product | Sea Salt, BBQ, Sour Cream and Onion, Jalapeño, Ranch, Cheddar, Salt and Vinegar, Sriracha and Honey, Voodoo |
| Texture or Style | text | Chip cut, processing style, or textural variant | Regular, Kettle Cooked, Rippled, Wavy, Baked, Popped, Puffed, Thin Cut, Thick Cut |
| Pack Quantity | number | Number of individual units per selling unit or case | 1, 8, 12, 24, 30, 56, 60, 64 |
| Shelf Life | number (days) | Expected shelf life from date of manufacture under recommended storage | 60, 90, 120, 180, 270, 365 |
| Storage Method | enum | Required storage condition | Ambient, Cool and Dry |
| Allergens | text (list) | Declared allergens present in the product | Wheat, Milk, Soy, Peanuts, Tree Nuts, Sesame, None |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications the product carries | Gluten-Free, Kosher, Non-GMO, Organic, Vegan, Vegetarian |
| Certifications | text (list) | Quality, safety, or sustainability certifications | USDA Organic, Non-GMO Project Verified, SQF, BRC, Fair Trade |
| Made in Dedicated Facility | boolean | Whether the product is made in a facility free from specific allergens | true, false |
| UPC | text | Universal Product Code or EAN barcode number | 028400001656, 072600001015 |
| GTIN | text | Global Trade Item Number for the selling unit | 00028400001656, 10072600001012 |
| Total Case Weight | number (kg) | Total net weight of all units in the selling case | 0.84, 1.68, 2.72, 4.54 |
| Serving Size | text | Labeled serving size with unit | 1 oz, 28 g, 15 chips, 1 bag |
| Servings Per Container | number | Number of servings per individual package | 1, 2, 6, 8, 13, 16 |
| Calories Per Serving | number (kcal) | Energy content per serving | 100, 130, 140, 150, 160, 250 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus industry standards (GS1 GDSN, Open Food Facts data model) | [WebstaurantStore](https://www.webstaurantstore.com/search/potato-chips.html), [Empire Snack Distributors](https://empiresnackdist.com/), [Redstone Foods](https://redstonefoods.com/), [Pitco Foods](https://pitcofoods.com/) |
