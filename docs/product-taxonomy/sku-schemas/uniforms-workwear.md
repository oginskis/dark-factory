# SKU Schema: Uniforms & Workwear

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.uniforms_workwear`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | DC-WD2279LW, UF-4820, WR-288UT11 |
| Product Name | product_name | text | — | Full product name including brand, garment type, and key features | Dickies Hi-Vis Lightweight Cotton Coverall, UniFirst Industrial Work Shirt, Workrite Tecasafe Plus FR Coverall |
| URL | url | text | — | Direct link to the product page | https://example.com/product/coverall-12345 |
| Price | price | number | — | Numeric unit price excluding currency symbol | 29.99, 65.00, 189.50 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Garment Type | garment_type | enum | — | Classification of the workwear item | Shirt, Polo, T-Shirt, Pants, Jeans, Coverall, Overalls, Jacket, Vest, Lab Coat, Scrub Top, Scrub Pants, Shorts, Sweatshirt |
| Fit Type | fit_type | enum | — | Garment cut and silhouette | Regular, Relaxed, Slim, Classic, Athletic |
| Fabric Composition | fabric_composition | text | — | Fiber content with percentages | 65% Polyester / 35% Cotton, 100% Cotton, 88% Cotton / 12% Nylon |
| Fabric Type | fabric_type | text | — | Weave or knit construction of the fabric | Twill, Ripstop, Poplin, Denim, Pique knit, Jersey knit, Canvas |
| Closure Type | closure_type | enum | — | Primary method of fastening the garment | Button front, Snap front, Zip front, Pull-over, Hook and loop |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Pocket Types | pocket_types | text (list) | — | Types of pockets included | Chest, Side slash, Cargo, Tool, Rule, Cell phone, Pencil division |
| Hi-Vis Class | hi-vis_class | enum | — | ANSI/ISEA 107 high-visibility classification | Not rated, Class 1, Class 2, Class 3 |
| Country of Origin | country_of_origin | text | — | Country where the garment was manufactured | Mexico, Honduras, USA, Bangladesh, Vietnam |
| Model Number | model_number | text | — | Manufacturer style or model number | WD2279LW, 574, DP1000, 288UT11 |
| Gender | gender | enum | — | Target gender fit | Men, Women, Unisex |
| Color | color | text | — | Garment color name | Black, Navy, Khaki, Grey, Royal Blue, Hi-Vis Yellow, Hi-Vis Orange |
| Number of Pockets | number_of_pockets | number | — | Total count of all pockets on the garment | 2, 4, 7, 9 |
| Flame Resistant | flame_resistant | boolean | — | Whether the garment is inherently or treated flame resistant | true, false |
| FR Standard | fr_standard | text | — | Flame resistance certification standard met | NFPA 2112, ASTM F1506, EN ISO 11612 |
| Arc Rating | arc_rating | number | cal/cm2 | Arc thermal performance value for electrical arc flash protection | 4.4, 8.9, 12.4, 20.0, 40.0 |
| HRC Level | hrc_level | enum | — | Hazard Risk Category level per NFPA 70E | PPE 1, PPE 2, PPE 3, PPE 4 |
| Reflective Tape | reflective_tape | boolean | — | Whether the garment has retroreflective striping | true, false |
| Moisture Management | moisture_management | boolean | — | Whether the fabric is treated for moisture wicking | true, false |
| Stain Release | stain_release | boolean | — | Whether the fabric has a soil or stain release finish | true, false |
| Wrinkle Resistant | wrinkle_resistant | boolean | — | Whether the garment has a wrinkle-free or no-iron treatment | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus NFPA 2112, NFPA 70E, and ANSI/ISEA 107 safety standards | [Dickies B2B](https://b2b.dickies.com/), [Cintas](https://www.cintas.com/uniform-work-apparel/), [UniFirst](https://unifirst.com/uniforms-workwear/all-products/), [HiVis Supply FR Clothing](https://www.hivissupply.com/hivis-fr-clothing.html) |
