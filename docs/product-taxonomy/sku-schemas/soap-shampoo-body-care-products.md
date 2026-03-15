# SKU Schema: Soap, Shampoo & Body Care Products

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 00011111610798, B07CX5KFK3, 324021 |
| Product Name | text | Full product name including brand, variant, and key claims | Dove Original Beauty Bar 3.75oz, Head and Shoulders Classic Clean Shampoo 13.5 fl oz |
| URL | text | Direct link to the product page | https://www.dove.com/us/en/p/original-beauty-bar.html |
| Price | number | Numeric unit price excluding currency symbol | 1.29, 6.99, 12.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | Dove, Head and Shoulders, Olay, Nivea, Bath and Body Works, Dr. Bronner |
| Product Type | enum | Primary product classification | Bar Soap, Liquid Soap, Body Wash, Shampoo, Conditioner, Shampoo Bar, Hand Wash, Lotion, Body Cream, Shower Gel |
| Net Weight | number (g) | Net weight for solid products such as bar soap | 90, 106, 150, 250 |
| Volume | number (ml) | Volume for liquid products | 236, 400, 500, 946 |
| Form | enum | Physical form of the product | Bar, Liquid, Gel, Cream, Foam, Mousse, Oil, Powder |
| Fragrance | text | Scent name or description | Original, Lavender, Coconut Milk, Unscented, Cucumber Melon, Shea Butter |
| Fragrance Free | enum | Whether the product is explicitly fragrance-free | Yes, No |
| Key Ingredients | text (list) | Featured or highlighted active ingredients | Shea Butter, Coconut Oil, Argan Oil, Aloe Vera, Colloidal Oatmeal, Tea Tree Oil, Charcoal |
| INCI Ingredients | text | Full INCI ingredient list as printed on packaging | Sodium Lauroyl Isethionate, Stearic Acid, Lauric Acid, Sodium Oleate, Water |
| Skin Type | text (list) | Targeted skin type | Normal, Dry, Oily, Sensitive, Combination, All Skin Types |
| Hair Type | text (list) | Targeted hair type for hair care products | Normal, Dry, Oily, Color-Treated, Curly, Fine, Thick |
| Product Claims | text (list) | Marketing and functional claims | Moisturizing, Antibacterial, Sulfate-Free, Paraben-Free, Dermatologist Tested, Hypoallergenic |
| Organic/Natural Certification | text (list) | Organic or natural product certifications | USDA Organic, COSMOS, Ecocert, Leaping Bunny, NATRUE |
| Cruelty Free | enum | Whether the product is certified cruelty-free | Yes, No |
| Vegan | enum | Whether the product contains no animal-derived ingredients | Yes, No |
| pH Level | number | Product pH value when specified | 5.5, 7.0, 4.5 |
| Pack Quantity | number | Number of units per pack or multipack | 1, 2, 3, 6, 12 |
| Dispensing Mechanism | enum | Type of dispenser for liquid products | Pump, Flip Cap, Squeeze Tube, Spray, Pour, Bar (none) |
| Packaging Material | text | Primary packaging material | Plastic Bottle, Paperboard Box, Glass Bottle, Refill Pouch, Aluminum Tube |
| Recyclable Packaging | enum | Whether the packaging is recyclable | Yes, No, Partially |
| Target Gender | enum | Intended consumer gender | Unisex, Men, Women, Kids |
| Target Age Group | enum | Intended consumer age group | Adult, Baby, Kids, Teen |
| Country of Origin | text | Country where the product is manufactured | USA, France, Germany, UK, India, Japan |
| Shelf Life | number (months) | Expected product shelf life from date of manufacture | 12, 24, 30, 36 |
| Certifications | text (list) | Regulatory and quality certifications | GMP, ISO 22716, FDA Registered, EU Cosmetics Regulation Compliant |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus INCI/ISO 22716 standards | [Dove Original Beauty Bar](https://www.dove.com/us/en/p/original-beauty-bar.html/00011111610798), [Botanie Soap Wholesale](https://botaniesoap.com/pages/shop), [Zogics Bulk Shampoo](https://zogics.com/bath-body/shampoo-conditioner/bulk-shampoo/), [Petra Soap Bulk Shampoo](https://www.petrasoap.com/hair-care/bulk-shampoo/) |
