# SKU Schema: Baby Food & Infant Formula

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 3292933, HB-OIF-24, 019503771100 |
| Product Name | text | Full product name including brand, line, and key descriptors | Enfamil NeuroPro Infant Formula Powder 21.1 oz, Happy Baby Clearly Crafted Organic Carrots and Peas Jar 4 oz |
| URL | text | Direct link to the product page | https://example.com/products/infant-formula-powder |
| Price | number | Numeric price per unit excluding currency symbol | 33.49, 15.48, 2.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Enfamil, Similac, Gerber, Happy Baby, Bobbie, HiPP, Holle, Earth's Best |
| Product Type | enum | Primary product classification | Infant Formula, Baby Food Puree, Baby Cereal, Baby Snack, Toddler Drink |
| Format | enum | Physical form of the product | Powder, Ready-to-Feed Liquid, Liquid Concentrate, Jar Puree, Pouch Puree, Puff, Teething Wafer |
| Stage | text | Age or developmental stage the product is designed for | Stage 1, Stage 2, Stage 3, Newborn, Infant 0-6 Months, Supported Sitter, Crawler |
| Minimum Age | number (months) | Earliest recommended age in months | 0, 4, 6, 9, 12 |
| Maximum Age | number (months) | Latest recommended age in months | 6, 12, 24, 36 |
| Net Weight | number (g) | Net weight of the product in grams | 113, 354, 598, 800, 1130 |
| Net Volume | number (mL) | Net volume for liquid products in millilitres | 59, 118, 237, 946 |
| Serving Size | text | Labelled serving size with unit | 113 g, 5 fl oz prepared, 28 g |
| Servings per Container | number | Number of servings per package | 8, 16, 33, 45 |
| Calories per Serving | number (kcal) | Energy content per serving | 20, 45, 60, 100 |
| Protein Source | text | Primary protein base used in the formulation | Cow Milk, Soy, Goat Milk, Hydrolysed Whey, Amino Acid, A2 Milk |
| DHA Content | number (mg) | Docosahexaenoic acid per serving in milligrams | 4, 8, 17, 32 |
| Iron Content | number (mg) | Iron per serving in milligrams | 0.4, 1.5, 1.8, 2.2 |
| Allergen Declarations | text (list) | Major allergens present per regulatory labelling | Milk, Soy, Fish Oil, None |
| Allergen-Free Claims | text (list) | Allergens explicitly excluded from the product | Gluten-Free, Dairy-Free, Soy-Free, Nut-Free, Top 9 Allergen Free |
| Organic Certification | text | Organic standard the product is certified under | USDA Organic, EU Organic, Demeter Biodynamic, None |
| Special Dietary Claims | text (list) | Dietary or health-related label claims | Hypoallergenic, Gentle, Sensitive, Lactose-Free, Non-GMO, Kosher, Halal |
| Nutritional Focus | text (list) | Key nutritional benefits highlighted on the label | Brain Development, Immune Support, Digestive Health, Iron Fortified, Prebiotics, Probiotics |
| Ingredients Count | number | Total number of ingredients listed on the label | 3, 12, 25, 40 |
| Packaging Material | enum | Primary container material | Glass Jar, Plastic Tub, Carton Box, BPA-Free Pouch, Tetra Pak, Sachet |
| Pack Quantity | number | Number of individual units per pack or case | 1, 4, 6, 12, 24 |
| UPC | text | Universal Product Code barcode number | 300875119761, 819573015157 |
| Shelf Life | number (months) | Unopened shelf life in months from manufacture date | 12, 18, 24 |
| Country of Origin | text | Country where the product is manufactured | USA, Germany, Netherlands, New Zealand, Austria |
| Preparation Required | boolean | Whether the product requires mixing or heating before serving | true, false |
| GMP Certified | boolean | Whether the manufacturing facility is Good Manufacturing Practice certified | true, false |
| HACCP Certified | boolean | Whether the product is made under Hazard Analysis Critical Control Points protocols | true, false |
| Recall Status | enum | Current regulatory recall status if applicable | None, Voluntary Recall, Mandatory Recall |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 3 companies plus FDA infant formula labelling requirements and Codex Alimentarius standards | [Enfamil](https://www.enfamil.com/products/newborn-infant-formula/), [Happy Family Organics](https://www.happyfamilyorganics.com/shop/organic-products/organic-baby-food/), [Earth's Best](https://www.earthsbest.com/products/baby-food), [FDA Infant Formula](https://www.fda.gov/food/resources-you-food/infant-formula) |
