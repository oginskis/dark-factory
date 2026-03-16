# SKU Schema: Bakery & Confectionery Products

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.bakery_confectionery`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | BKR-44210, 071146013506, SC-9920 |
| Product Name | product_name | text | — | Full product name including brand, product type, flavor, and size | Bridor Mini Chocolate Croissants 1.5oz 75ct, Ghirardelli 60% Cacao Bittersweet Chocolate Chips 10oz, Sara Lee Classic White Bread 20oz |
| URL | url | text | — | Direct link to the product page | https://example.com/product/bridor-mini-croissants |
| Price | price | number | — | Numeric price per selling unit (each, case, bag), excluding currency symbol | 3.49, 86.99, 5.29, 132.49 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | product_type | enum | — | Primary product type classification | Bread, Cake, Cookie, Pastry, Muffin, Croissant, Donut, Pie, Tart, Macaron, Chocolate Bar, Candy, Confection |
| Product Subcategory | product_subcategory | text | — | More specific product type within the category | Sourdough Loaf, Chocolate Chip Cookie, Fruit Danish, Dark Chocolate Truffle, Hard Candy |
| Storage Type | storage_type | enum | — | Required storage condition for the product | Ambient, Refrigerated, Frozen |
| Preparation Type | preparation_type | enum | — | How the product is prepared for serving | Ready to Eat, Thaw and Serve, Bake from Frozen, Proof and Bake, Heat and Serve |
| Packaging Type | packaging_type | enum | — | Primary packaging material and form | Box, Bag, Tray, Clamshell, Individually Wrapped, Bulk Case |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Chocolate Type | chocolate_type | enum | — | Classification of chocolate used or contained in the product | Milk Chocolate, Dark Chocolate, White Chocolate, Ruby Chocolate, Compound Coating |
| Ingredients List | ingredients_list | text | — | Full ingredient statement in descending order by weight | Enriched Wheat Flour, Sugar, Butter, Eggs, Cocoa Butter... |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, France, Belgium, Germany, Italy, Switzerland |
| Dough Type | dough_type | enum | — | Type of dough or batter base used, applicable to bakery items | Yeast, Laminated, Quick Bread, Puff Pastry, Shortcrust, Choux, Phyllo |
| Filling Type | filling_type | text | — | Type of filling or center in the product, if applicable | Cream, Fruit, Chocolate, Custard, Jam, Caramel, None |
| Manufacturer | manufacturer | text | — | Company that produces the product, if different from brand | Groupe Le Duff, Lindt & Sprungli, Bimbo Bakeries USA |
| UPC/EAN | upcean | text | — | Universal Product Code or European Article Number barcode | 071146013506, 3760178820024 |
| Shelf Life | shelf_life | number | days | Expected shelf life from date of manufacture under proper storage | 5, 14, 30, 180, 365 |
| Flavor/Variety | flavorvariety | text | — | Specific flavor or variety of the product | Chocolate, Vanilla, Cinnamon Raisin, Blueberry, Plain, Almond, Lemon |
| Pack Quantity | pack_quantity | number | — | Number of selling units per case for wholesale | 1, 4, 6, 12, 24, 48 |
| Cocoa Content | cocoa_content | number | % | Percentage of cocoa solids in chocolate products | 35, 50, 60, 72, 85 |
| Allergen Declaration | allergen_declaration | text (list) | — | Major allergens present in the product as declared on the label | Wheat, Milk, Eggs, Soy, Tree Nuts, Peanuts |
| Contains Allergen Free Claim | contains_allergen_free_claim | text (list) | — | Allergen-free claims stated on the label | Nut Free, Gluten Free, Dairy Free |
| Dietary Certifications | dietary_certifications | text (list) | — | Dietary or lifestyle certifications displayed on packaging | Organic, Non-GMO, Kosher, Halal, Vegan, Fair Trade, Rainforest Alliance |
| Coating/Topping | coatingtopping | text | — | Surface finish, coating, or topping on the product | Powdered Sugar, Icing, Chocolate Glaze, Streusel, Seeds, None |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from bakery/confectionery distributors, FDA chocolate standards of identity, and USDA commercial item descriptions for bakery products | [WebstaurantStore](https://www.webstaurantstore.com/54649/baked-goods.html), [Stover & Company](https://www.stovercompany.com/), [BakeMark](https://bakemark.com/), [USDA AMS Bakery CID](https://www.ams.usda.gov/grades-standards/cid/bakery-items) |
