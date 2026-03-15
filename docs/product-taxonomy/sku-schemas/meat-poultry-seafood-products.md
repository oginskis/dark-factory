# SKU Schema: Meat, Poultry & Seafood Products

**Last updated:** 2026-03-15
**Parent category:** Food & Beverage Products
**Taxonomy ID:** `food.meat_poultry_seafood`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | MPF-20145, IMPS-1112, 079893100036 |
| Product Name | text | Full product name including protein type, cut, grade, and weight | USDA Choice Boneless Ribeye Steak 12oz, Tyson Boneless Skinless Chicken Breast 40lb Case, Wild-Caught Sockeye Salmon Fillet 6oz |
| URL | text | Direct link to the product page | https://example.com/product/usda-choice-ribeye |
| Price | number | Numeric price per selling unit (per piece, per lb, or per case), excluding currency symbol | 12.99, 89.50, 7.49, 145.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Protein Type | enum | Primary animal protein category | Beef, Pork, Chicken, Turkey, Lamb, Veal, Salmon, Shrimp, Tuna, Cod, Crab, Lobster |
| Protein Category | enum | Broad grouping of the protein source | Red Meat, Poultry, Finfish, Shellfish, Game |
| Cut/Form | text | Specific cut name, portion, or product form | Ribeye, Tenderloin, Breast, Thigh, Wing, Fillet, Steak, Ground, Whole, Rack, Loin |
| USDA Quality Grade | enum | USDA quality grade for beef, poultry, or other graded products | Prime, Choice, Select, Standard, Grade A, Grade B |
| USDA Yield Grade | enum | USDA yield grade indicating ratio of lean meat to fat and bone in beef carcasses | 1, 2, 3, 4, 5 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country or ocean region where the product was raised, caught, or processed | USA, Canada, Chile, Norway, Thailand, Gulf of Mexico, North Atlantic |
| Packaging Type | enum | Primary packaging format | Vacuum Sealed, MAP, Tray Pack, IQF Bag, Cryovac, Bulk Case, Canned |
| Manufacturer/Processor | text | Company that processed or packed the product | JBS USA, Tyson Foods, Smithfield Foods, Perdue Farms |
| UPC/EAN | text | Universal Product Code or European Article Number barcode | 079893100036, 023700013835 |
| IMPS Number | text | Institutional Meat Purchase Specification number for standardized cut identification | 1112, 1180A, 1189A, P1100 |
| Bone Status | enum | Whether the product contains bone | Bone-In, Boneless, Semi-Boneless |
| Skin Status | enum | Whether poultry or fish product has skin | Skin-On, Skinless |
| Fat Content | number (%) | Maximum fat percentage, primarily for ground products | 5, 10, 15, 20, 27 |
| Product State | enum | Physical state of the product at point of sale | Fresh, Frozen, Previously Frozen, Smoked, Cured, Dried |
| Harvest Method | enum | How the seafood was sourced, applicable to fish and shellfish | Wild-Caught, Farm-Raised, Line-Caught, Trawl-Caught |
| Species | text | Specific species name for seafood products | Atlantic Salmon, Pacific Cod, Gulf Shrimp, Yellowfin Tuna, Blue Crab |
| Processing Level | enum | Degree of processing applied to the product | Whole, Portioned, Ground, Breaded, Marinated, Seasoned, Fully Cooked, Raw |
| Cooking State | enum | Whether the product has been cooked prior to sale | Raw, Partially Cooked, Fully Cooked, Ready to Eat |
| Storage Temperature | text | Required storage temperature | 0-4C, -18C or below |
| Shelf Life | number (days) | Expected shelf life from packaging date under proper storage | 5, 14, 21, 180, 365, 730 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from wholesale meat/seafood distributors, USDA grading standards, IMPS specifications, and MSC/ASC sustainability programs | [US Foods](https://www.usfoods.com/great-food/featured-products/meat-seafood.html), [Buckhead Meat & Seafood](https://www.buckheadmeat.com/), [USDA AMS Beef Grades](https://www.ams.usda.gov/grades-standards/beef), [MSC](https://www.msc.org/en-us/what-we-are-doing/our-approach/what-does-the-blue-msc-label-mean) |
