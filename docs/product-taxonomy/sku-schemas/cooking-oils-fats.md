# SKU Schema: Cooking Oils & Fats

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.cooking_oils_fats`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or distributor product identifier | 101PNUTPURE, OIL-CAN-35, CVG-SOY-5GAL |
| Product Name | product_name | text | — | yes | Full product name including key descriptors such as oil type, size, and grade | 100% Peanut Oil 35 lb., Golden Barrel Canola Oil 1 Gallon, Catania Non-GMO Soybean Oil 35 lb. |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/peanut-oil-35lb |
| Price | price | number | — | yes | Numeric price per selling unit, excluding currency symbol | 11.99, 38.50, 68.99, 224.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Form | product_form | enum | — | — | Physical state and product type | Liquid Oil, Solid Shortening, Semi-Solid Fat, Spray, Margarine, Ghee, Lard Block |
| Container Type | container_type | enum | — | — | Type of primary packaging | Jug, Pail, Drum, Bottle, Tin, Bag-in-Box, Tote, Flexitank, Bulk Tank |
| Country of Origin | country_of_origin | text | — | — | Country where the oil was produced or refined | USA, Canada, Argentina, Brazil, Spain, Italy, Malaysia, Indonesia |
| Net Weight | net_weight | number | kg | — | Net weight of the product per selling unit | 0.45, 3.78, 15.88, 22.68, 158.76 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Oil Source | oil_source | enum | — | — | Primary plant or animal source of the oil or fat | Canola, Soybean, Peanut, Sunflower, Corn, Olive, Coconut, Avocado, Safflower, Cottonseed, Palm, Vegetable Blend, Lard, Tallow, Butter |
| Refinement Level | refinement_level | enum | — | — | Degree of processing applied to the oil | Crude, Refined, Extra Virgin, Virgin, Cold Pressed, Expeller Pressed, RBD |
| Smoke Point | smoke_point | number | °F | — | Temperature at which the oil begins to produce visible smoke, indicating suitability for frying | 320, 350, 400, 420, 450, 480, 520 |
| Volume | volume | number | L | — | Volume of the product per selling unit | 0.47, 0.95, 3.78, 18.93 |
| Pack Quantity | pack_quantity | number | — | — | Number of individual containers per selling unit | 1, 2, 4, 6 |
| Oleic Acid Content | oleic_acid_content | number | % | — | Percentage of oleic acid, relevant for high-oleic oil varieties | 28, 55, 65, 80, 82 |
| Fry Life | fry_life | text | — | — | Expected number of frying cycles or hours before oil degrades | 3-5 cycles, 40 hours, Extended |
| Flavor Transfer | flavor_transfer | boolean | — | — | Whether the oil imparts noticeable flavor to food during cooking | true, false |
| Allergens | allergens | text (list) | — | — | Declared allergens present in the product | Peanuts, Soy, Tree Nuts, Coconut, None |
| Dietary Certifications | dietary_certifications | text (list) | — | — | Dietary or lifestyle certifications the product carries | Kosher, Halal, Organic, Vegan, Non-GMO |
| Certifications | certifications | text (list) | — | — | Quality, safety, or regulatory certifications | USDA Organic, Non-GMO Project Verified, SQF, cGMP, NSF, USP/NF |
| Shelf Life | shelf_life | number | months | — | Expected shelf life from date of manufacture unopened at recommended storage | 6, 12, 18, 24 |
| Storage Method | storage_method | enum | — | — | Required storage condition | Ambient, Cool and Dry, Refrigerate After Opening |
| UPC | upc | text | — | — | Universal Product Code or EAN barcode number | 854651008478, 041224210004 |
| GTIN | gtin | text | — | — | Global Trade Item Number for the selling unit | 00854651008478, 10041224210001 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 sources plus industry standards (GS1 GDSN, smoke point data from WebstaurantStore, Open Food Facts data model) | [Bakers Authority](https://www.bakersauthority.com/collections/cooking-oils), [WebstaurantStore Peanut Oil](https://www.webstaurantstore.com/100-peanut-oil-35-lb/101PNUTPURE.html), [Columbus Vegetable Oils](https://cvoils.com/), [ADM Edible Oils](https://www.adm.com/en-us/products-services/human-nutrition/products/edible-specialty-oils/) |
