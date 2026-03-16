# SKU Schema: Baby Food & Infant Formula

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.baby_food_infant_formula`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 3292933, HB-OIF-24, 019503771100 |
| Product Name | product_name | text | — | Full product name including brand, line, and key descriptors | Enfamil NeuroPro Infant Formula Powder 21.1 oz, Happy Baby Clearly Crafted Organic Carrots and Peas Jar 4 oz |
| URL | url | text | — | Direct link to the product page | https://example.com/products/infant-formula-powder |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 33.49, 15.48, 2.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | product_type | enum | — | Primary product classification | Infant Formula, Baby Food Puree, Baby Cereal, Baby Snack, Toddler Drink |
| Format | format | enum | — | Physical form of the product | Powder, Ready-to-Feed Liquid, Liquid Concentrate, Jar Puree, Pouch Puree, Puff, Teething Wafer |
| Ingredients Count | ingredients_count | number | — | Total number of ingredients listed on the label | 3, 12, 25, 40 |
| Packaging Material | packaging_material | enum | — | Primary container material | Glass Jar, Plastic Tub, Carton Box, BPA-Free Pouch, Tetra Pak, Sachet |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | USA, Germany, Netherlands, New Zealand, Austria |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Stage | stage | text | — | Age or developmental stage the product is designed for | Stage 1, Stage 2, Stage 3, Newborn, Infant 0-6 Months, Supported Sitter, Crawler |
| Minimum Age | minimum_age | number | months | Earliest recommended age in months | 0, 4, 6, 9, 12 |
| Maximum Age | maximum_age | number | months | Latest recommended age in months | 6, 12, 24, 36 |
| Net Volume | net_volume | number | mL | Net volume for liquid products in millilitres | 59, 118, 237, 946 |
| Protein Source | protein_source | text | — | Primary protein base used in the formulation | Cow Milk, Soy, Goat Milk, Hydrolysed Whey, Amino Acid, A2 Milk |
| DHA Content | dha_content | number | mg | Docosahexaenoic acid per serving in milligrams | 4, 8, 17, 32 |
| Iron Content | iron_content | number | mg | Iron per serving in milligrams | 0.4, 1.5, 1.8, 2.2 |
| Allergen Declarations | allergen_declarations | text (list) | — | Major allergens present per regulatory labelling | Milk, Soy, Fish Oil, None |
| Allergen-Free Claims | allergen-free_claims | text (list) | — | Allergens explicitly excluded from the product | Gluten-Free, Dairy-Free, Soy-Free, Nut-Free, Top 9 Allergen Free |
| Organic Certification | organic_certification | text | — | Organic standard the product is certified under | USDA Organic, EU Organic, Demeter Biodynamic, None |
| Special Dietary Claims | special_dietary_claims | text (list) | — | Dietary or health-related label claims | Hypoallergenic, Gentle, Sensitive, Lactose-Free, Non-GMO, Kosher, Halal |
| Nutritional Focus | nutritional_focus | text (list) | — | Key nutritional benefits highlighted on the label | Brain Development, Immune Support, Digestive Health, Iron Fortified, Prebiotics, Probiotics |
| Pack Quantity | pack_quantity | number | — | Number of individual units per pack or case | 1, 4, 6, 12, 24 |
| UPC | upc | text | — | Universal Product Code barcode number | 300875119761, 819573015157 |
| Shelf Life | shelf_life | number | months | Unopened shelf life in months from manufacture date | 12, 18, 24 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 3 companies plus FDA infant formula labelling requirements and Codex Alimentarius standards | [Enfamil](https://www.enfamil.com/products/newborn-infant-formula/), [Happy Family Organics](https://www.happyfamilyorganics.com/shop/organic-products/organic-baby-food/), [Earth's Best](https://www.earthsbest.com/products/baby-food), [FDA Infant Formula](https://www.fda.gov/food/resources-you-food/infant-formula) |
