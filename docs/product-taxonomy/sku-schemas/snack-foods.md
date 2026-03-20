# SKU Schema: Snack Foods

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.snack_foods`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or distributor product identifier | 999CHIP001, SNK-LAY-24, 103MART0016 |
| Product Name | product_name | text | — | yes | Full product name including key descriptors such as type, flavor, and pack configuration | Martin's Sea Salt Potato Chips 1 oz. - 30/Case, Herr's Sour Cream and Onion Rippled Chips 2.75 oz. - 24/Case |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/sea-salt-chips-30pk |
| Price | price | number | — | yes | Numeric price per selling unit (case, box, or individual), excluding currency symbol | 18.99, 24.50, 42.95 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Snack Type | snack_type | enum | — | — | Primary snack product classification | Potato Chips, Tortilla Chips, Pretzels, Popcorn, Crackers, Nuts and Seeds, Cookies, Puffed Snacks, Rice Cakes, Jerky, Granola Bars, Trail Mix, Cheese Snacks, Fruit Snacks |
| Packaging Format | packaging_format | enum | — | — | How individual units are packaged for sale | Individually Wrapped, Bulk Bag, Multi-Pack Box, Canister, Tub, Clip Strip |
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured or processed | USA, Canada, Mexico, UK, Germany |
| Ingredient Statement | ingredient_statement | text | — | — | Full list of ingredients as declared on the product label | Potatoes, Vegetable Oil (Sunflower, Corn, and/or Canola Oil), Sea Salt |
| Net Weight Per Unit | net_weight_per_unit | number | g | — | Net weight of a single bag or package | 23, 28, 42, 78, 198, 283, 454 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Flavor | flavor | text | — | — | Specific flavor or seasoning of the product | Sea Salt, BBQ, Sour Cream and Onion, Jalapeño, Ranch, Cheddar, Salt and Vinegar, Sriracha and Honey, Voodoo |
| Texture or Style | texture_or_style | text | — | — | Chip cut, processing style, or textural variant | Regular, Kettle Cooked, Rippled, Wavy, Baked, Popped, Puffed, Thin Cut, Thick Cut |
| Pack Quantity | pack_quantity | number | — | — | Number of individual units per selling unit or case | 1, 8, 12, 24, 30, 56, 60, 64 |
| Shelf Life | shelf_life | number | days | — | Expected shelf life from date of manufacture under recommended storage | 60, 90, 120, 180, 270, 365 |
| Storage Method | storage_method | enum | — | — | Required storage condition | Ambient, Cool and Dry |
| Allergens | allergens | text (list) | — | — | Declared allergens present in the product | Wheat, Milk, Soy, Peanuts, Tree Nuts, Sesame, None |
| Dietary Certifications | dietary_certifications | text (list) | — | — | Dietary or lifestyle certifications the product carries | Gluten-Free, Kosher, Non-GMO, Organic, Vegan, Vegetarian |
| Certifications | certifications | text (list) | — | — | Quality, safety, or sustainability certifications | USDA Organic, Non-GMO Project Verified, SQF, BRC, Fair Trade |
| Made in Dedicated Facility | made_in_dedicated_facility | boolean | — | — | Whether the product is made in a facility free from specific allergens | true, false |
| UPC | upc | text | — | — | Universal Product Code or EAN barcode number | 028400001656, 072600001015 |
| GTIN | gtin | text | — | — | Global Trade Item Number for the selling unit | 00028400001656, 10072600001012 |
| Total Case Weight | total_case_weight | number | kg | — | Total net weight of all units in the selling case | 0.84, 1.68, 2.72, 4.54 |
| Serving Size | serving_size | text | — | — | Labeled serving size with unit | 1 oz, 28 g, 15 chips, 1 bag |
| Servings Per Container | servings_per_container | number | — | — | Number of servings per individual package | 1, 2, 6, 8, 13, 16 |
| Calories Per Serving | calories_per_serving | number | kcal | — | Energy content per serving | 100, 130, 140, 150, 160, 250 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus industry standards (GS1 GDSN, Open Food Facts data model) | [WebstaurantStore](https://www.webstaurantstore.com/search/potato-chips.html), [Empire Snack Distributors](https://empiresnackdist.com/), [Redstone Foods](https://redstonefoods.com/), [Pitco Foods](https://pitcofoods.com/) |
