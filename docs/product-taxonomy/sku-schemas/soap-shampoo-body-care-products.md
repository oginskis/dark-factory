# SKU Schema: Soap, Shampoo & Body Care Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.soap_shampoo_body_care`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 00011111610798, B07CX5KFK3, 324021 |
| Product Name | product_name | text | — | yes | Full product name including brand, variant, and key claims | Dove Original Beauty Bar 3.75oz, Head and Shoulders Classic Clean Shampoo 13.5 fl oz |
| URL | url | text | — | yes | Direct link to the product page | https://www.dove.com/us/en/p/original-beauty-bar.html |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 1.29, 6.99, 12.50 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary product classification | Bar Soap, Liquid Soap, Body Wash, Shampoo, Conditioner, Shampoo Bar, Hand Wash, Lotion, Body Cream, Shower Gel |
| Form | form | enum | — | — | Physical form of the product | Bar, Liquid, Gel, Cream, Foam, Mousse, Oil, Powder |
| Key Ingredients | key_ingredients | text (list) | — | — | Featured or highlighted active ingredients | Shea Butter, Coconut Oil, Argan Oil, Aloe Vera, Colloidal Oatmeal, Tea Tree Oil, Charcoal |
| INCI Ingredients | inci_ingredients | text | — | — | Full INCI ingredient list as printed on packaging | Sodium Lauroyl Isethionate, Stearic Acid, Lauric Acid, Sodium Oleate, Water |
| Skin Type | skin_type | text (list) | — | — | Targeted skin type | Normal, Dry, Oily, Sensitive, Combination, All Skin Types |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Hair Type | hair_type | text (list) | — | — | Targeted hair type for hair care products | Normal, Dry, Oily, Color-Treated, Curly, Fine, Thick |
| Packaging Material | packaging_material | text | — | — | Primary packaging material | Plastic Bottle, Paperboard Box, Glass Bottle, Refill Pouch, Aluminum Tube |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, France, Germany, UK, India, Japan |
| Volume | volume | number | ml | — | Volume for liquid products | 236, 400, 500, 946 |
| Fragrance | fragrance | text | — | — | Scent name or description | Original, Lavender, Coconut Milk, Unscented, Cucumber Melon, Shea Butter |
| Fragrance Free | fragrance_free | enum | — | — | Whether the product is explicitly fragrance-free | Yes, No |
| Product Claims | product_claims | text (list) | — | — | Marketing and functional claims | Moisturizing, Antibacterial, Sulfate-Free, Paraben-Free, Dermatologist Tested, Hypoallergenic |
| Organic/Natural Certification | organicnatural_certification | text (list) | — | — | Organic or natural product certifications | USDA Organic, COSMOS, Ecocert, Leaping Bunny, NATRUE |
| Cruelty Free | cruelty_free | enum | — | — | Whether the product is certified cruelty-free | Yes, No |
| Vegan | vegan | enum | — | — | Whether the product contains no animal-derived ingredients | Yes, No |
| pH Level | ph_level | number | — | — | Product pH value when specified | 5.5, 7.0, 4.5 |
| Pack Quantity | pack_quantity | number | — | — | Number of units per pack or multipack | 1, 2, 3, 6, 12 |
| Dispensing Mechanism | dispensing_mechanism | enum | — | — | Type of dispenser for liquid products | Pump, Flip Cap, Squeeze Tube, Spray, Pour, Bar (none) |
| Recyclable Packaging | recyclable_packaging | enum | — | — | Whether the packaging is recyclable | Yes, No, Partially |
| Target Gender | target_gender | enum | — | — | Intended consumer gender | Unisex, Men, Women, Kids |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus INCI/ISO 22716 standards | [Dove Original Beauty Bar](https://www.dove.com/us/en/p/original-beauty-bar.html/00011111610798), [Botanie Soap Wholesale](https://botaniesoap.com/pages/shop), [Zogics Bulk Shampoo](https://zogics.com/bath-body/shampoo-conditioner/bulk-shampoo/), [Petra Soap Bulk Shampoo](https://www.petrasoap.com/hair-care/bulk-shampoo/) |
