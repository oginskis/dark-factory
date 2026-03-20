# SKU Schema: Beverages (Non-Alcoholic)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.beverages_non_alcoholic`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or distributor product identifier | 103LANGGFR64, 4900030, BEV-WTR-24PK |
| Product Name | product_name | text | — | yes | Full product name including key descriptors such as flavor, size, and pack configuration | Langers Ruby Red Grapefruit Juice 64 fl. oz. - 8/Case, Coca-Cola Classic 12 oz Can - 24/Case |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/grapefruit-juice-64oz |
| Price | price | number | — | yes | Numeric price per selling unit (case, pack, or individual), excluding currency symbol | 39.99, 5.49, 22.95 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Beverage Type | beverage_type | enum | — | — | Primary product classification | Water, Juice, Soda, Energy Drink, Tea, Coffee, Sports Drink, Kombucha, Sparkling Water, Lemonade, Milk, Non-Dairy Milk, Smoothie Mix |
| Sweetener Type | sweetener_type | enum | — | — | Type of sweetener used in the product | Sugar, High Fructose Corn Syrup, Stevia, Aspartame, Sucralose, Honey, Unsweetened |
| Container Type | container_type | enum | — | — | Type of primary packaging | Bottle, Can, Carton, Pouch, Bag-in-Box, Tetra Pak, Glass Bottle, Jug |
| Country of Origin | country_of_origin | text | — | — | Country where the beverage was manufactured or bottled | USA, Mexico, Germany, Japan, Italy |
| Serving Size | serving_size | text | — | — | Labeled serving size with unit | 8 fl oz, 240 ml, 1 bottle |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Flavor | flavor | text | — | — | Primary flavor or variety of the beverage | Ruby Red Grapefruit, Original Cola, Lemon Lime, Mango Peach, Unflavored |
| Carbonation | carbonation | enum | — | — | Whether the beverage is carbonated | Carbonated, Non-Carbonated, Lightly Carbonated |
| Caffeinated | caffeinated | boolean | — | — | Whether the beverage contains caffeine | true, false |
| Caffeine Content | caffeine_content | number | mg | — | Amount of caffeine per serving | 0, 34, 80, 160, 200 |
| Unit Volume | unit_volume | number | ml | — | Volume of a single container in millilitres | 250, 330, 355, 473, 500, 591, 1000, 1893 |
| Pack Quantity | pack_quantity | number | — | — | Number of individual containers per selling unit | 1, 6, 8, 12, 24, 28, 36 |
| Case Volume | case_volume | number | ml | — | Total volume per case or selling unit | 4260, 8520, 14184 |
| Juice Content | juice_content | number | % | — | Percentage of real juice in the product | 0, 5, 10, 50, 100 |
| Shelf Life | shelf_life | number | days | — | Expected shelf life from date of manufacture under recommended storage | 90, 180, 270, 365 |
| Storage Method | storage_method | enum | — | — | Required storage condition | Ambient, Refrigerated, Frozen |
| Allergens | allergens | text (list) | — | — | Declared allergens present in the product per major allergen regulations | Milk, Soy, Tree Nuts, Coconut, None |
| Dietary Certifications | dietary_certifications | text (list) | — | — | Dietary or lifestyle certifications the product carries | Kosher, Halal, Organic, Vegan, Gluten-Free, Non-GMO |
| Certifications | certifications | text (list) | — | — | Quality, safety, or sustainability certifications | USDA Organic, Fair Trade, Rainforest Alliance, BPA Free, NSF |
| UPC | upc | text | — | — | Universal Product Code or EAN barcode number | 049000028904, 012000001536 |
| GTIN | gtin | text | — | — | Global Trade Item Number for the selling unit | 00049000028904, 10012000001533 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus industry standards (GS1 GDSN, Open Food Facts data model) | [WebstaurantStore](https://www.webstaurantstore.com/48627/drinks-and-drink-mixes.html), [Langers Product Page](https://www.webstaurantstore.com/langers-ruby-red-grapefruit-juice-64-fl-oz-case/103LANGGFR64.html), [Big Geyser](https://www.biggeyser.com/), [Zepeim](https://zepeim.com/) |
