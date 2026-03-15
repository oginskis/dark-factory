# SKU Schema: Oral Care Products (Toothpaste, Toothbrushes)

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 35000510853, B003UKM9CO, 324599 |
| Product Name | text | Full product name including brand, product line, variant, and size | Colgate Cavity Protection Toothpaste 6.0 oz, Oral-B iO Series 9 Rechargeable Electric Toothbrush Black |
| URL | text | Direct link to the product page | https://www.colgate.com/en-us/products/toothpaste/cc-cavity-protection |
| Price | number | Numeric unit price excluding currency symbol | 2.49, 7.99, 199.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand | text | Manufacturer or brand name | Colgate, Oral-B, Crest, Sensodyne, Philips Sonicare, quip, Waterpik |
| Product Type | enum | Primary product classification | Toothpaste, Manual Toothbrush, Electric Toothbrush, Mouthwash, Dental Floss, Whitening Kit, Tongue Cleaner, Interdental Brush, Water Flosser, Replacement Brush Head |
| Net Weight | number (g) | Net weight for toothpaste and solid products | 75, 100, 170, 232 |
| Volume | number (ml) | Volume for liquid products such as mouthwash | 250, 473, 500, 1000 |
| Active Ingredients | text (list) | Pharmacologically active ingredients | Sodium Monofluorophosphate, Stannous Fluoride, Sodium Fluoride, Potassium Nitrate, Hydrogen Peroxide |
| Fluoride Concentration | number (ppm) | Fluoride content in parts per million | 1000, 1100, 1450, 5000 |
| Fluoride Type | text | Chemical form of the fluoride compound | Sodium Fluoride, Stannous Fluoride, Sodium Monofluorophosphate |
| Inactive Ingredients | text | Full list of inactive ingredients from label | Dicalcium Phosphate Dihydrate, Water, Glycerin, Sodium Lauryl Sulfate, Cellulose Gum |
| Flavor | text | Taste or flavor of the product | Mint, Spearmint, Peppermint, Cinnamon, Bubblegum, Unflavored |
| Product Purpose | text (list) | Specific oral care function the product addresses | Cavity Protection, Whitening, Sensitivity Relief, Gum Health, Tartar Control, Fresh Breath, Enamel Repair |
| Bristle Stiffness | enum | Firmness of toothbrush bristles | Extra Soft, Soft, Medium, Hard |
| Bristle Material | text | Material the bristles are made from | Nylon, Charcoal-Infused Nylon, Silicone |
| Head Size | enum | Size of the toothbrush head | Compact, Full, Large |
| Power Source | enum | Type of power for electric toothbrushes | Rechargeable, Battery (AA), Battery (AAA), Manual (none) |
| Battery Life | number (days) | Battery life on a full charge for electric models | 14, 21, 30 |
| Cleaning Modes | number | Number of cleaning modes for electric toothbrushes | 1, 3, 5, 7 |
| Cleaning Mode Names | text (list) | Names of available cleaning modes | Daily Clean, Sensitive, Whitening, Deep Clean, Gum Care, Tongue Clean |
| Timer | enum | Whether a 2-minute brushing timer is built in | Yes, No |
| Pressure Sensor | enum | Whether a pressure sensor alerts against excessive force | Yes, No |
| Smart Features | text (list) | Connected or intelligent features | Bluetooth, App Connectivity, AI Brushing Recognition, Interactive Display |
| Replacement Head Compatible | text | Compatible replacement brush head model names | iO Series, FlossAction, Precision Clean, CrossAction |
| Age Group | enum | Intended age group | Adults, Kids, Baby, All Ages |
| Pack Quantity | number | Number of units in the pack | 1, 2, 3, 6, 24 |
| ADA Accepted | enum | Whether the product has the ADA Seal of Acceptance | Yes, No |
| Certifications | text (list) | Product regulatory and quality certifications | ADA Seal, CE, FDA Registered, ISO 13485 |
| SLS Free | enum | Whether the product is free of sodium lauryl sulfate | Yes, No |
| Country of Origin | text | Country where the product is manufactured | USA, Germany, China, Ireland, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ADA standards and FDA OTC monograph | [Colgate Cavity Protection](https://www.colgate.com/en-us/products/toothpaste/cc-cavity-protection), [Oral-B Electric Toothbrush Comparison](https://oralb.com/en-us/products/compare/electric-toothbrushes), [ADA Toothbrush Guidelines](https://www.ada.org/resources/ada-library/oral-health-topics/toothbrushes), [Colgate Toothpaste Ingredients](https://www.colgate.com/en-us/oral-health/selecting-dental-products/what-is-in-toothpaste-five-ingredients-and-what-they-do) |
