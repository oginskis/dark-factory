# SKU Schema: Oral Care Products (Toothpaste, Toothbrushes)

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.oral_care`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 35000510853, B003UKM9CO, 324599 |
| Product Name | product_name | text | — | yes | Full product name including brand, product line, variant, and size | Colgate Cavity Protection Toothpaste 6.0 oz, Oral-B iO Series 9 Rechargeable Electric Toothbrush Black |
| URL | url | text | — | yes | Direct link to the product page | https://www.colgate.com/en-us/products/toothpaste/cc-cavity-protection |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 2.49, 7.99, 199.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary product classification | Toothpaste, Manual Toothbrush, Electric Toothbrush, Mouthwash, Dental Floss, Whitening Kit, Tongue Cleaner, Interdental Brush, Water Flosser, Replacement Brush Head |
| Active Ingredients | active_ingredients | text (list) | — | — | Pharmacologically active ingredients | Sodium Monofluorophosphate, Stannous Fluoride, Sodium Fluoride, Potassium Nitrate, Hydrogen Peroxide |
| Fluoride Type | fluoride_type | text | — | — | Chemical form of the fluoride compound | Sodium Fluoride, Stannous Fluoride, Sodium Monofluorophosphate |
| Inactive Ingredients | inactive_ingredients | text | — | — | Full list of inactive ingredients from label | Dicalcium Phosphate Dihydrate, Water, Glycerin, Sodium Lauryl Sulfate, Cellulose Gum |
| Bristle Material | bristle_material | text | — | — | Material the bristles are made from | Nylon, Charcoal-Infused Nylon, Silicone |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, Germany, China, Ireland, Mexico |
| Volume | volume | number | ml | — | Volume for liquid products such as mouthwash | 250, 473, 500, 1000 |
| Fluoride Concentration | fluoride_concentration | number | ppm | — | Fluoride content in parts per million | 1000, 1100, 1450, 5000 |
| Flavor | flavor | text | — | — | Taste or flavor of the product | Mint, Spearmint, Peppermint, Cinnamon, Bubblegum, Unflavored |
| Product Purpose | product_purpose | text (list) | — | — | Specific oral care function the product addresses | Cavity Protection, Whitening, Sensitivity Relief, Gum Health, Tartar Control, Fresh Breath, Enamel Repair |
| Bristle Stiffness | bristle_stiffness | enum | — | — | Firmness of toothbrush bristles | Extra Soft, Soft, Medium, Hard |
| Power Source | power_source | enum | — | — | Type of power for electric toothbrushes | Rechargeable, Battery (AA), Battery (AAA), Manual (none) |
| Battery Life | battery_life | number | days | — | Battery life on a full charge for electric models | 14, 21, 30 |
| Cleaning Modes | cleaning_modes | number | — | — | Number of cleaning modes for electric toothbrushes | 1, 3, 5, 7 |
| Cleaning Mode Names | cleaning_mode_names | text (list) | — | — | Names of available cleaning modes | Daily Clean, Sensitive, Whitening, Deep Clean, Gum Care, Tongue Clean |
| Timer | timer | enum | — | — | Whether a 2-minute brushing timer is built in | Yes, No |
| Pressure Sensor | pressure_sensor | enum | — | — | Whether a pressure sensor alerts against excessive force | Yes, No |
| Smart Features | smart_features | text (list) | — | — | Connected or intelligent features | Bluetooth, App Connectivity, AI Brushing Recognition, Interactive Display |
| Replacement Head Compatible | replacement_head_compatible | text | — | — | Compatible replacement brush head model names | iO Series, FlossAction, Precision Clean, CrossAction |
| Age Group | age_group | enum | — | — | Intended age group | Adults, Kids, Baby, All Ages |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ADA standards and FDA OTC monograph | [Colgate Cavity Protection](https://www.colgate.com/en-us/products/toothpaste/cc-cavity-protection), [Oral-B Electric Toothbrush Comparison](https://oralb.com/en-us/products/compare/electric-toothbrushes), [ADA Toothbrush Guidelines](https://www.ada.org/resources/ada-library/oral-health-topics/toothbrushes), [Colgate Toothpaste Ingredients](https://www.colgate.com/en-us/oral-health/selecting-dental-products/what-is-in-toothpaste-five-ingredients-and-what-they-do) |
