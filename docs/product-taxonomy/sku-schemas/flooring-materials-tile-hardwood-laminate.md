# SKU Schema: Flooring Materials (Tile, Hardwood, Laminate)

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.flooring`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | DAL-NQ15-12241P, SHW-SW715-01079, MHK-CDL45-06 |
| Product Name | product_name | text | — | Full product name including key specs such as material, species or look, and format | Daltile Porcelain Wood-Look Plank 6x36, Shaw Repel Hardwood Oak Natural 5in, Mohawk RevWood Plus Alder Creek |
| URL | url | text | — | Direct link to the product page | https://example.com/product/porcelain-wood-plank |
| Price | price | number | — | Numeric price per unit area (per sq ft or per sq m) or per piece, excluding currency symbol | 2.49, 4.99, 8.75, 12.50 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Flooring Type | flooring_type | enum | — | Primary material category of the flooring | Ceramic Tile, Porcelain Tile, Solid Hardwood, Engineered Hardwood, Laminate, Luxury Vinyl Plank, Luxury Vinyl Tile, Natural Stone |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, Belgium, Germany, China, Brazil, Spain, Italy |
| Plank/Tile Length | planktile_length | number | mm | Face length of a single plank or tile | 305, 610, 914, 1219, 1524, 1829 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Species or Look | species_or_look | text | — | Wood species (hardwood) or visual appearance (tile/laminate) | Red Oak, White Oak, Hickory, Walnut, Maple, Wood-Look, Stone-Look, Marble-Look, Concrete-Look |
| Plank/Tile Width | planktile_width | number | mm | Face width of a single plank or tile | 76, 89, 127, 152, 178, 200, 300, 600 |
| Thickness | thickness | number | mm | Total thickness of the flooring product | 6, 7, 8, 10, 12, 14, 19 |
| Wear Layer Thickness | wear_layer_thickness | number | mm | Thickness of the surface wear layer (engineered, laminate, LVP) | 0.3, 0.5, 1.0, 2.0, 3.0, 4.0, 6.0 |
| AC Rating | ac_rating | enum | — | Abrasion class durability rating for laminate (EN 13329) | AC1, AC2, AC3, AC4, AC5 |
| PEI Rating | pei_rating | enum | — | Porcelain Enamel Institute hardness rating for glazed tile (0 to 5) | PEI 0, PEI 1, PEI 2, PEI 3, PEI 4, PEI 5 |
| Water Absorption | water_absorption | text | — | Water absorption classification per ASTM C373 / ISO 10545-3 | Impervious (less than 0.5%), Vitreous (0.5-3%), Semi-Vitreous (3-7%), Non-Vitreous (over 7%) |
| DCOF | dcof | number | — | Wet Dynamic Coefficient of Friction per ANSI A326.3 (0.42 or greater recommended for wet floors) | 0.42, 0.50, 0.55, 0.60 |
| Shade Variation | shade_variation | enum | — | Visual variation between pieces per ANSI A137.1 | V0 Uniform, V1 Slight, V2 Moderate, V3 Substantial, V4 Random |
| Finish | finish | text | — | Surface texture or coating of the flooring | Smooth, Hand-Scraped, Wire-Brushed, Embossed, Matte, Satin, Semi-Gloss, High-Gloss, Honed, Polished |
| Edge Profile | edge_profile | text | — | Edge treatment of planks or tiles | Square Edge, Micro-Bevel, Beveled, Eased Edge, Pressed Edge, Rectified |
| Color | color | text | — | Primary color or color family of the product | Natural, Golden, Espresso, Gray, White, Beige, Walnut, Charcoal |
| Installation Method | installation_method | text | — | How the flooring is installed | Click-Lock, Glue-Down, Nail-Down, Staple-Down, Floating, Thin-Set Mortar, Peel-and-Stick |
| Janka Hardness | janka_hardness | number | N | Janka hardness rating for solid or engineered hardwood | 1290, 1820, 2700, 5600, 8000 |
| Waterproof | waterproof | boolean | — | Whether the product is rated waterproof or water-resistant | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ANSI A137.1, ANSI A326.3, EN 13329, ASTM C373) | [Daltile](https://www.daltile.com/tile-product-category), [Shaw Flooring](https://www.shawfloors.com/), [Mohawk Flooring](https://www.mohawkflooring.com/), [Armstrong Flooring](https://www.armstrongflooring.com/) |
