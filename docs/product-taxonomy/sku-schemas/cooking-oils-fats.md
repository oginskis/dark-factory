# SKU Schema: Cooking Oils & Fats

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or distributor product identifier | 101PNUTPURE, OIL-CAN-35, CVG-SOY-5GAL |
| Product Name | text | Full product name including key descriptors such as oil type, size, and grade | 100% Peanut Oil 35 lb., Golden Barrel Canola Oil 1 Gallon, Catania Non-GMO Soybean Oil 35 lb. |
| URL | text | Direct link to the product page | https://example.com/product/peanut-oil-35lb |
| Price | number | Numeric price per selling unit, excluding currency symbol | 11.99, 38.50, 68.99, 224.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Product brand or manufacturer name | Golden Barrel, Catania, Admiration, WHIRL, Nutola, Bunge, ADM, Cargill, Columbus Vegetable Oils |
| Oil Source | enum | Primary plant or animal source of the oil or fat | Canola, Soybean, Peanut, Sunflower, Corn, Olive, Coconut, Avocado, Safflower, Cottonseed, Palm, Vegetable Blend, Lard, Tallow, Butter |
| Product Form | enum | Physical state and product type | Liquid Oil, Solid Shortening, Semi-Solid Fat, Spray, Margarine, Ghee, Lard Block |
| Refinement Level | enum | Degree of processing applied to the oil | Crude, Refined, Extra Virgin, Virgin, Cold Pressed, Expeller Pressed, RBD |
| Smoke Point | number (°F) | Temperature at which the oil begins to produce visible smoke, indicating suitability for frying | 320, 350, 400, 420, 450, 480, 520 |
| Container Type | enum | Type of primary packaging | Jug, Pail, Drum, Bottle, Tin, Bag-in-Box, Tote, Flexitank, Bulk Tank |
| Container Material | enum | Material of the primary container | HDPE Plastic, Metal, Glass, PET Plastic |
| Net Weight | number (kg) | Net weight of the product per selling unit | 0.45, 3.78, 15.88, 22.68, 158.76 |
| Volume | number (L) | Volume of the product per selling unit | 0.47, 0.95, 3.78, 18.93 |
| Pack Quantity | number | Number of individual containers per selling unit | 1, 2, 4, 6 |
| Serving Size | text | Labeled serving size with unit | 1 tbsp, 14 g, 15 ml |
| Calories Per Serving | number (kcal) | Energy content per serving | 120, 130 |
| Total Fat Per Serving | number (g) | Total fat content per serving | 14 |
| Saturated Fat Per Serving | number (g) | Saturated fat content per serving | 1, 2, 3.5, 7, 12 |
| Trans Fat Per Serving | number (g) | Trans fat content per serving | 0 |
| Monounsaturated Fat Per Serving | number (g) | Monounsaturated fat content per serving | 3, 4, 8, 10 |
| Polyunsaturated Fat Per Serving | number (g) | Polyunsaturated fat content per serving | 1, 4, 5, 8 |
| Oleic Acid Content | number (%) | Percentage of oleic acid, relevant for high-oleic oil varieties | 28, 55, 65, 80, 82 |
| Fry Life | text | Expected number of frying cycles or hours before oil degrades | 3-5 cycles, 40 hours, Extended |
| Flavor Transfer | boolean | Whether the oil imparts noticeable flavor to food during cooking | true, false |
| Allergens | text (list) | Declared allergens present in the product | Peanuts, Soy, Tree Nuts, Coconut, None |
| Dietary Certifications | text (list) | Dietary or lifestyle certifications the product carries | Kosher, Halal, Organic, Vegan, Non-GMO |
| Certifications | text (list) | Quality, safety, or regulatory certifications | USDA Organic, Non-GMO Project Verified, SQF, cGMP, NSF, USP/NF |
| Shelf Life | number (months) | Expected shelf life from date of manufacture unopened at recommended storage | 6, 12, 18, 24 |
| Storage Method | enum | Required storage condition | Ambient, Cool and Dry, Refrigerate After Opening |
| Country of Origin | text | Country where the oil was produced or refined | USA, Canada, Argentina, Brazil, Spain, Italy, Malaysia, Indonesia |
| Shipping Weight | number (kg) | Total weight of the selling unit including packaging for shipping | 1.0, 4.2, 16.7, 23.5 |
| UPC | text | Universal Product Code or EAN barcode number | 854651008478, 041224210004 |
| GTIN | text | Global Trade Item Number for the selling unit | 00854651008478, 10041224210001 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 sources plus industry standards (GS1 GDSN, smoke point data from WebstaurantStore, Open Food Facts data model) | [Bakers Authority](https://www.bakersauthority.com/collections/cooking-oils), [WebstaurantStore Peanut Oil](https://www.webstaurantstore.com/100-peanut-oil-35-lb/101PNUTPURE.html), [Columbus Vegetable Oils](https://cvoils.com/), [ADM Edible Oils](https://www.adm.com/en-us/products-services/human-nutrition/products/edible-specialty-oils/) |
