# SKU Schema: Action Figures, Dolls & Plush Toys

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.action_figures_dolls_plush`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | F4793, 209068, HLC87, 87-2204 |
| Product Name | product_name | text | Full product name including character, line, and scale | Marvel Legends Series 6-Inch Venom Action Figure, Star Wars Black Series Darth Vader, Barbie Dreamhouse Adventures Doll |
| URL | url | text | Direct link to the product page | https://example.com/product/marvel-legends-venom |
| Price | price | number | Numeric retail price excluding currency symbol | 24.99, 49.99, 129.99 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Product Type | product_type | enum | Primary toy category | Action Figure, Fashion Doll, Baby Doll, Plush Toy, Statue, Collectible Figure, Vinyl Figure |
| Material | material | text (list) | Primary materials used in construction | ABS Plastic, PVC, Die-Cast Metal, Fabric, Polyester Plush, Vinyl, Silicone |
| Collector Grade | collector_grade | enum | Whether the item is positioned as a mass-market toy or collector piece | Standard, Premium, Deluxe, Ultimate, Collector Edition |
| Doll Body Type | doll_body_type | text | Body style or articulation type for fashion dolls | Standard, Curvy, Petite, Tall, Made to Move |
| Plush Fill Material | plush_fill_material | text | Internal stuffing material for plush toys | Polyester Fiber, Bean Pellets, Memory Foam |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Plush Size Category | plush_size_category | text | Size classification for plush toys | Mini, Small, Medium, Large, Jumbo |
| Packaging Type | packaging_type | enum | How the product is packaged for sale | Window Box, Blister Card, Collector Box, Polybag, Tin |
| Country of Origin | country_of_origin | text | Country where the product is manufactured | China, Vietnam, Indonesia, Japan |
| Franchise/License | franchiselicense | text | Intellectual property or brand the product is based on | Marvel, Star Wars, Transformers, Barbie, Disney Princess, Pokemon, DC Comics |
| Character Name | character_name | text | Specific character represented by the figure or doll | Spider-Man, Darth Vader, Optimus Prime, Barbie, Pikachu |
| Scale | scale | text | Proportional scale of the figure relative to real-world size | 1/12, 1/6, 1/18, 1/4, 1/10 |
| Figure Height | figure_height | number (inches) | Height of the figure measured standing upright | 3.75, 5.5, 6, 7, 12 |
| Articulation Points | articulation_points | number | Number of movable joints on the figure | 5, 14, 20, 30, 36 |
| Accessories Included | accessories_included | text (list) | Items packaged with the figure or doll | Alternate Hands, Weapon, Shield, Stand, Clothing Set, Hairbrush, Pet |
| Series/Wave | serieswave | text | Product line, wave number, or collection name | Wave 3, Black Series, Legends Series, Signature Collection, Build-A-Figure |
| Build-A-Figure Part | build-a-figure_part | text | Component included for building a larger figure across a wave | Left Arm, Right Leg, Torso, Head, Wings |
| Age Recommendation | age_recommendation | text | Recommended minimum age for the product | 3+, 4+, 8+, 14+, 15+ |
| Paint Application | paint_application | text | Type of paint finish or decoration method | Hand-Painted, Tampo Print, Metallic, Wash, Dry Brush |
| Product Dimensions (L x W x H) | product_dimensions_l_x_w_x_h | text (inches) | Overall package or product dimensions | 8.5 x 2.5 x 12, 4 x 3 x 6.5 |
| Interactivity | interactivity | text (list) | Electronic or interactive features built into the toy | Sound Effects, Light-Up, Voice, Motion Sensor, App-Enabled |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 sources plus ASTM F963 and EN 71 toy safety standards | [BigBadToyStore](https://www.bigbadtoystore.com/), [Hasbro](https://shop.hasbro.com/), [Amazon Toys](https://www.amazon.com/Action-Toy-Figures/b?node=2514571011), [Walmart Toys](https://www.walmart.com/cp/action-figures-playsets/4172) |
