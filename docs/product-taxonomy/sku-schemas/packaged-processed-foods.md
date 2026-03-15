# SKU Schema: Packaged & Processed Foods

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 041303010747, WMT-98765, SYS-4820031 |
| Product Name | text | Full product name including brand, variety, and size | Campbell's Condensed Tomato Soup 10.75 oz, Heinz Baked Beans 415g, Del Monte Sliced Peaches in Light Syrup 15.25 oz |
| URL | text | Direct link to the product page | https://example.com/product/campbells-tomato-soup |
| Price | number | Numeric price per selling unit (can, jar, case), excluding currency symbol | 1.29, 24.99, 3.49 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Consumer-facing brand name of the product | Campbell's, Heinz, Del Monte, General Mills, Barilla |
| Manufacturer | text | Company that produces the product, if different from brand | Conagra Brands, Kraft Heinz, Nestle |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 041303010747, 5000157024671 |
| GTIN | text | Global Trade Item Number for supply chain identification | 00041303010747 |
| Product Category | text | Primary food category classification | Canned Vegetables, Pasta, Cereal, Snacks, Condiments, Frozen Meals |
| Product Subcategory | text | More specific product type within the category | Tomato Soup, Penne Pasta, Granola Bars, Ketchup |
| Net Weight | number (g) | Net weight of the product contents excluding packaging | 305, 415, 907, 1360 |
| Net Volume | number (ml) | Net volume for liquid or semi-liquid products | 355, 750, 946 |
| Serving Size | text | Labelled serving size with unit | 125 ml, 1/2 cup (120g), 2 tbsp (30g) |
| Servings Per Container | number | Number of servings per package as stated on the nutrition label | 2, 4, 8, 25 |
| Calories Per Serving | number (kcal) | Energy content per serving | 90, 150, 230, 340 |
| Storage Type | enum | Required storage condition for the product | Ambient, Refrigerated, Frozen |
| Storage Temperature | text | Recommended storage temperature range | Room temperature, 0-4C, -18C or below |
| Shelf Life | number (days) | Expected shelf life from date of manufacture under proper storage | 365, 730, 180, 90 |
| Preparation Type | enum | How the product is prepared for consumption | Ready to Eat, Heat and Serve, Requires Cooking, Add Water, Thaw and Serve |
| Packaging Type | enum | Primary packaging material and form | Can, Jar, Pouch, Box, Bag, Bottle, Tray, Carton, Tetra Pak |
| Pack Quantity | number | Number of individual units in the selling pack | 1, 6, 12, 24, 48 |
| Case Pack | number | Number of selling units per case for wholesale | 12, 24, 48 |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications displayed on packaging | Organic, Non-GMO, Gluten Free, Kosher, Halal, Vegan, Fair Trade |
| Allergen Declaration | text (list) | Major allergens present in the product as declared on the label | Milk, Wheat, Soy, Tree Nuts, Peanuts, Eggs, Fish, Shellfish, Sesame |
| Contains Allergen Free Claim | text (list) | Allergen-free claims stated on the label | Nut Free, Dairy Free, Gluten Free |
| Country of Origin | text | Country where the product was manufactured or processed | USA, Italy, Canada, Thailand, China |
| Ingredients List | text | Full ingredient statement in descending order by weight | Water, Tomato Paste, High Fructose Corn Syrup, Salt... |
| Nutritional Certifications | text (list) | Health or nutritional claim certifications on the label | Heart Healthy, Low Sodium, Reduced Fat, Good Source of Fiber |
| Food Safety Certifications | text (list) | Food safety and quality certifications | GMP, HACCP, SQF, BRC, ISO 22000 |
| Gross Weight | number (g) | Total weight of the product including packaging | 340, 450, 950 |
| Package Dimensions | text (mm) | Physical dimensions of the package length x width x height | 75 x 75 x 110, 200 x 80 x 250 |
| Product Form | enum | Physical form of the food product | Solid, Liquid, Powder, Paste, Granule, Sliced, Diced, Whole |
| Flavor/Variety | text | Specific flavor or variety of the product | Original, Spicy, Garlic Herb, Low Sodium, Family Size |
| Private Label | boolean | Whether the product is a store or private-label brand | true, false |
| Best Before Date Format | text | Date code format used on the product | YYYY-MM-DD, MM/DD/YY, Best By, Use By |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from foodservice distributors, GS1 GDSN data standards, and FDA labeling requirements | [Sysco](https://www.sysco.com/), [WebstaurantStore](https://www.webstaurantstore.com/), [GS1 GDSN Attribute Guide](https://documents.gs1us.org/adobe/assets/deliver/urn:aaid:aem:31ec08cf-e4be-4429-9ace-20bd50aaaa74/Guideline-Foodservice-GS1-US-GDSN-Attribute-Guide.pdf), [USDA AMS Product Specifications](https://www.ams.usda.gov/selling-food/product-specs) |
