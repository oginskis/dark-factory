# SKU Schema: Beverages (Non-Alcoholic)

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor product identifier | 103LANGGFR64, 4900030, BEV-WTR-24PK |
| Product Name | text | Full product name including key descriptors such as flavor, size, and pack configuration | Langers Ruby Red Grapefruit Juice 64 fl. oz. - 8/Case, Coca-Cola Classic 12 oz Can - 24/Case |
| URL | text | Direct link to the product page | https://example.com/product/grapefruit-juice-64oz |
| Price | number | Numeric price per selling unit (case, pack, or individual), excluding currency symbol | 39.99, 5.49, 22.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Beverage brand or manufacturer name | Coca-Cola, PepsiCo, Langers, Nestlé, Monster, Celsius |
| Beverage Type | enum | Primary product classification | Water, Juice, Soda, Energy Drink, Tea, Coffee, Sports Drink, Kombucha, Sparkling Water, Lemonade, Milk, Non-Dairy Milk, Smoothie Mix |
| Flavor | text | Primary flavor or variety of the beverage | Ruby Red Grapefruit, Original Cola, Lemon Lime, Mango Peach, Unflavored |
| Carbonation | enum | Whether the beverage is carbonated | Carbonated, Non-Carbonated, Lightly Carbonated |
| Caffeinated | boolean | Whether the beverage contains caffeine | true, false |
| Caffeine Content | number (mg) | Amount of caffeine per serving | 0, 34, 80, 160, 200 |
| Sweetener Type | enum | Type of sweetener used in the product | Sugar, High Fructose Corn Syrup, Stevia, Aspartame, Sucralose, Honey, Unsweetened |
| Container Type | enum | Type of primary packaging | Bottle, Can, Carton, Pouch, Bag-in-Box, Tetra Pak, Glass Bottle, Jug |
| Container Material | enum | Material of the primary container | PET Plastic, Glass, Aluminum, Paperboard, HDPE |
| Unit Volume | number (ml) | Volume of a single container in millilitres | 250, 330, 355, 473, 500, 591, 1000, 1893 |
| Pack Quantity | number | Number of individual containers per selling unit | 1, 6, 8, 12, 24, 28, 36 |
| Case Volume | number (ml) | Total volume per case or selling unit | 4260, 8520, 14184 |
| Serving Size | text | Labeled serving size with unit | 8 fl oz, 240 ml, 1 bottle |
| Servings Per Container | number | Number of servings per individual container | 1, 2, 2.5, 8 |
| Calories Per Serving | number (kcal) | Energy content per serving | 0, 10, 90, 110, 140, 170 |
| Total Sugars Per Serving | number (g) | Total sugar content per labeled serving | 0, 12, 27, 39, 46 |
| Juice Content | number (%) | Percentage of real juice in the product | 0, 5, 10, 50, 100 |
| Shipping Weight | number (kg) | Total weight of the selling unit for shipping purposes | 4.5, 8.2, 16.7 |
| Shelf Life | number (days) | Expected shelf life from date of manufacture under recommended storage | 90, 180, 270, 365 |
| Storage Method | enum | Required storage condition | Ambient, Refrigerated, Frozen |
| Allergens | text (list) | Declared allergens present in the product per major allergen regulations | Milk, Soy, Tree Nuts, Coconut, None |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications the product carries | Kosher, Halal, Organic, Vegan, Gluten-Free, Non-GMO |
| Certifications | text (list) | Quality, safety, or sustainability certifications | USDA Organic, Fair Trade, Rainforest Alliance, BPA Free, NSF |
| Country of Origin | text | Country where the beverage was manufactured or bottled | USA, Mexico, Germany, Japan, Italy |
| UPC | text | Universal Product Code or EAN barcode number | 049000028904, 012000001536 |
| GTIN | text | Global Trade Item Number for the selling unit | 00049000028904, 10012000001533 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus industry standards (GS1 GDSN, Open Food Facts data model) | [WebstaurantStore](https://www.webstaurantstore.com/48627/drinks-and-drink-mixes.html), [Langers Product Page](https://www.webstaurantstore.com/langers-ruby-red-grapefruit-juice-64-fl-oz-case/103LANGGFR64.html), [Big Geyser](https://www.biggeyser.com/), [Zepeim](https://zepeim.com/) |
