# SKU Schema: Bakery & Confectionery Products

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | BKR-44210, 071146013506, SC-9920 |
| Product Name | text | Full product name including brand, product type, flavor, and size | Bridor Mini Chocolate Croissants 1.5oz 75ct, Ghirardelli 60% Cacao Bittersweet Chocolate Chips 10oz, Sara Lee Classic White Bread 20oz |
| URL | text | Direct link to the product page | https://example.com/product/bridor-mini-croissants |
| Price | number | Numeric price per selling unit (each, case, bag), excluding currency symbol | 3.49, 86.99, 5.29, 132.49 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Consumer-facing brand name of the product | Bridor, Ghirardelli, Sara Lee, BakeMark, Entenmann's, Lindt |
| Manufacturer | text | Company that produces the product, if different from brand | Groupe Le Duff, Lindt & Sprungli, Bimbo Bakeries USA |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 071146013506, 3760178820024 |
| Product Type | enum | Primary product type classification | Bread, Cake, Cookie, Pastry, Muffin, Croissant, Donut, Pie, Tart, Macaron, Chocolate Bar, Candy, Confection |
| Product Subcategory | text | More specific product type within the category | Sourdough Loaf, Chocolate Chip Cookie, Fruit Danish, Dark Chocolate Truffle, Hard Candy |
| Net Weight | number (g) | Net weight of the product contents | 283, 567, 907, 340, 100 |
| Piece Count | number | Number of individual pieces or items per package | 6, 12, 24, 48, 75 |
| Piece Weight | number (g) | Weight of a single individual piece | 28, 42, 57, 85, 120 |
| Serving Size | text | Labelled serving size with unit | 1 slice (32g), 2 cookies (30g), 1 piece (40g) |
| Servings Per Container | number | Number of servings per package | 10, 12, 20, 75 |
| Calories Per Serving | number (kcal) | Energy content per serving | 80, 120, 180, 250 |
| Storage Type | enum | Required storage condition for the product | Ambient, Refrigerated, Frozen |
| Preparation Type | enum | How the product is prepared for serving | Ready to Eat, Thaw and Serve, Bake from Frozen, Proof and Bake, Heat and Serve |
| Shelf Life | number (days) | Expected shelf life from date of manufacture under proper storage | 5, 14, 30, 180, 365 |
| Flavor/Variety | text | Specific flavor or variety of the product | Chocolate, Vanilla, Cinnamon Raisin, Blueberry, Plain, Almond, Lemon |
| Packaging Type | enum | Primary packaging material and form | Box, Bag, Tray, Clamshell, Individually Wrapped, Bulk Case |
| Pack Quantity | number | Number of selling units per case for wholesale | 1, 4, 6, 12, 24, 48 |
| Cocoa Content | number (%) | Percentage of cocoa solids in chocolate products | 35, 50, 60, 72, 85 |
| Chocolate Type | enum | Classification of chocolate used or contained in the product | Milk Chocolate, Dark Chocolate, White Chocolate, Ruby Chocolate, Compound Coating |
| Allergen Declaration | text (list) | Major allergens present in the product as declared on the label | Wheat, Milk, Eggs, Soy, Tree Nuts, Peanuts |
| Contains Allergen Free Claim | text (list) | Allergen-free claims stated on the label | Nut Free, Gluten Free, Dairy Free |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications displayed on packaging | Organic, Non-GMO, Kosher, Halal, Vegan, Fair Trade, Rainforest Alliance |
| Ingredients List | text | Full ingredient statement in descending order by weight | Enriched Wheat Flour, Sugar, Butter, Eggs, Cocoa Butter... |
| Country of Origin | text | Country where the product was manufactured | USA, France, Belgium, Germany, Italy, Switzerland |
| Dough Type | enum | Type of dough or batter base used, applicable to bakery items | Yeast, Laminated, Quick Bread, Puff Pastry, Shortcrust, Choux, Phyllo |
| Sugar Content Per Serving | number (g) | Total sugar content per serving as stated on the nutrition label | 5, 12, 18, 24, 30 |
| Filling Type | text | Type of filling or center in the product, if applicable | Cream, Fruit, Chocolate, Custard, Jam, Caramel, None |
| Coating/Topping | text | Surface finish, coating, or topping on the product | Powdered Sugar, Icing, Chocolate Glaze, Streusel, Seeds, None |
| Frozen Indicator | boolean | Whether the product is sold in frozen state | true, false |
| Food Safety Certifications | text (list) | Food safety and quality certifications | GMP, HACCP, SQF, BRC, ISO 22000, IFS |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from bakery/confectionery distributors, FDA chocolate standards of identity, and USDA commercial item descriptions for bakery products | [WebstaurantStore](https://www.webstaurantstore.com/54649/baked-goods.html), [Stover & Company](https://www.stovercompany.com/), [BakeMark](https://bakemark.com/), [USDA AMS Bakery CID](https://www.ams.usda.gov/grades-standards/cid/bakery-items) |
