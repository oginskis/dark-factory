# SKU Schema: Condiments, Sauces & Seasonings

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.condiments_sauces_seasonings`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or distributor product identifier | WBS-HNY-001, 171FRNCH12, COND-SRC-060 |
| Product Name | product_name | text | Full product name including key descriptors such as type, flavor, and pack configuration | French's Classic Yellow Mustard 12 oz. - 12/Case, Huy Fong Sriracha Hot Chili Sauce 28 oz. |
| URL | url | text | Direct link to the product page | https://example.com/product/yellow-mustard-12oz |
| Price | price | number | Numeric price per selling unit (case, bottle, or portion pack box), excluding currency symbol | 5.99, 24.49, 38.95 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary condiment or seasoning classification | Ketchup, Mustard, Mayonnaise, Hot Sauce, BBQ Sauce, Soy Sauce, Salad Dressing, Salsa, Relish, Honey, Jam and Jelly, Vinegar, Worcestershire, Tartar Sauce, Horseradish, Steak Sauce, Seasoning Blend, Dried Herbs, Dried Spices, Spice Rub |
| Form | form | enum | Physical form of the product | Liquid, Paste, Powder, Granular, Whole, Crushed, Flakes, Gel, Cream |
| Container Type | container_type | enum | Type of primary packaging | Bottle, Squeeze Bottle, Jar, Pouch, Packet, Pail, Tub, Shaker, Tin, Piping Bag, Bag-in-Box |
| Country of Origin | country_of_origin | text | Country where the product was manufactured or processed | USA, Thailand, Mexico, China, France, Japan, India |
| Ingredient Statement | ingredient_statement | text | Full list of ingredients as declared on the product label | Distilled Vinegar, Mustard Seed, Water, Salt, Turmeric, Paprika |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Flavor or Variety | flavor_or_variety | text | Specific flavor profile, variety, or recipe name | Classic Yellow, Sriracha, Chipotle, Dijon, Ranch, Buffalo, Teriyaki, Sweet and Sour, Honey Mustard |
| Heat Level | heat_level | enum | Spiciness or heat intensity for hot sauces and spicy condiments | Mild, Medium, Hot, Extra Hot |
| Scoville Rating | scoville_rating | number (SHU) | Scoville Heat Units measuring capsaicin concentration for pepper-based products | 450, 2500, 5000, 8000, 50000 |
| Portion Control | portion_control | boolean | Whether the product is packaged in individual single-serve portions | true, false |
| Pack Quantity | pack_quantity | number | Number of individual containers or packets per selling unit | 1, 6, 12, 100, 200, 500, 1000 |
| Shelf Life | shelf_life | number (months) | Expected shelf life from date of manufacture unopened at recommended storage | 6, 12, 18, 24, 36 |
| Storage Method | storage_method | enum | Required storage condition before opening | Ambient, Refrigerate After Opening, Refrigerated, Cool and Dry |
| Allergens | allergens | text (list) | Declared allergens present in the product | Wheat, Soy, Milk, Egg, Fish, Mustard, Sesame, None |
| Dietary Certifications | dietary_certifications | text (list) | Dietary or lifestyle certifications the product carries | Kosher, Halal, Organic, Vegan, Vegetarian, Gluten-Free, Non-GMO |
| Certifications | certifications | text (list) | Quality, safety, or sustainability certifications | USDA Organic, Non-GMO Project Verified, SQF, BRC, HACCP, GMP |
| UPC | upc | text | Universal Product Code or EAN barcode number | 041500000244, 024463061095 |
| GTIN | gtin | text | Global Trade Item Number for the selling unit | 00041500000244, 10024463061092 |
| Net Weight or Volume | net_weight_or_volume | text | Net weight or volume per individual container with unit | 12 oz, 28 oz, 1 gal, 5 lb, 0.25 fl oz, 7 g |
| Portion Size | portion_size | text | Weight or volume of each individual portion packet, if applicable | 7 g, 9 g, 0.25 fl oz, 0.5 fl oz, 1 oz |
| Serving Size | serving_size | text | Labeled serving size with unit | 1 tbsp, 5 g, 1 tsp, 2 tbsp, 1 packet |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus industry standards (GS1 GDSN, Open Food Facts data model, Scoville scale) | [WebstaurantStore](https://www.webstaurantstore.com/171/condiments-and-sauces.html), [Gourmet Food Marketplace](https://gourmetfoodmarketplace.com/collection/condiments/33), [Great Lakes Wholesale](https://www.glwholesale.com/category/wholesale-condiments-sauces/ac), [Bakers Authority](https://www.bakersauthority.com/collections/condiments) |
