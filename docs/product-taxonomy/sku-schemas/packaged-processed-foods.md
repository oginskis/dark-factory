# SKU Schema: Packaged & Processed Foods

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.packaged_processed_foods`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 041303010747, WMT-98765, SYS-4820031 |
| Product Name | product_name | text | — | yes | Full product name including brand, variety, and size | Campbell's Condensed Tomato Soup 10.75 oz, Heinz Baked Beans 415g, Del Monte Sliced Peaches in Light Syrup 15.25 oz |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/campbells-tomato-soup |
| Price | price | number | — | yes | Numeric price per selling unit (can, jar, case), excluding currency symbol | 1.29, 24.99, 3.49 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Category | product_category | text | — | — | Primary food category classification | Canned Vegetables, Pasta, Cereal, Snacks, Condiments, Frozen Meals |
| Product Subcategory | product_subcategory | text | — | — | More specific product type within the category | Tomato Soup, Penne Pasta, Granola Bars, Ketchup |
| Storage Type | storage_type | enum | — | — | Required storage condition for the product | Ambient, Refrigerated, Frozen |
| Preparation Type | preparation_type | enum | — | — | How the product is prepared for consumption | Ready to Eat, Heat and Serve, Requires Cooking, Add Water, Thaw and Serve |
| Packaging Type | packaging_type | enum | — | — | Primary packaging material and form | Can, Jar, Pouch, Box, Bag, Bottle, Tray, Carton, Tetra Pak |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product was manufactured or processed | USA, Italy, Canada, Thailand, China |
| Ingredients List | ingredients_list | text | — | — | Full ingredient statement in descending order by weight | Water, Tomato Paste, High Fructose Corn Syrup, Salt... |
| Product Form | product_form | enum | — | — | Physical form of the food product | Solid, Liquid, Powder, Paste, Granule, Sliced, Diced, Whole |
| Manufacturer | manufacturer | text | — | — | Company that produces the product, if different from brand | Conagra Brands, Kraft Heinz, Nestle |
| UPC/EAN | upcean | text | — | — | Universal Product Code or European Article Number barcode | 041303010747, 5000157024671 |
| GTIN | gtin | text | — | — | Global Trade Item Number for supply chain identification | 00041303010747 |
| Net Volume | net_volume | number | ml | — | Net volume for liquid or semi-liquid products | 355, 750, 946 |
| Storage Temperature | storage_temperature | text | — | — | Recommended storage temperature range | Room temperature, 0-4C, -18C or below |
| Shelf Life | shelf_life | number | days | — | Expected shelf life from date of manufacture under proper storage | 365, 730, 180, 90 |
| Pack Quantity | pack_quantity | number | — | — | Number of individual units in the selling pack | 1, 6, 12, 24, 48 |
| Case Pack | case_pack | number | — | — | Number of selling units per case for wholesale | 12, 24, 48 |
| Dietary Certifications | dietary_certifications | text (list) | — | — | Dietary or lifestyle certifications displayed on packaging | Organic, Non-GMO, Gluten Free, Kosher, Halal, Vegan, Fair Trade |
| Allergen Declaration | allergen_declaration | text (list) | — | — | Major allergens present in the product as declared on the label | Milk, Wheat, Soy, Tree Nuts, Peanuts, Eggs, Fish, Shellfish, Sesame |
| Contains Allergen Free Claim | contains_allergen_free_claim | text (list) | — | — | Allergen-free claims stated on the label | Nut Free, Dairy Free, Gluten Free |
| Nutritional Certifications | nutritional_certifications | text (list) | — | — | Health or nutritional claim certifications on the label | Heart Healthy, Low Sodium, Reduced Fat, Good Source of Fiber |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from foodservice distributors, GS1 GDSN data standards, and FDA labeling requirements | [Sysco](https://www.sysco.com/), [WebstaurantStore](https://www.webstaurantstore.com/), [GS1 GDSN Attribute Guide](https://documents.gs1us.org/adobe/assets/deliver/urn:aaid:aem:31ec08cf-e4be-4429-9ace-20bd50aaaa74/Guideline-Foodservice-GS1-US-GDSN-Attribute-Guide.pdf), [USDA AMS Product Specifications](https://www.ams.usda.gov/selling-food/product-specs) |
