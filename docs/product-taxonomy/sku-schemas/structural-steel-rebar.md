# SKU Schema: Structural Steel & Rebar

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.structural_steel_rebar`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | MU-RB5-20, SS-W8X31, KM-A992-W10 |
| Product Name | product_name | text | Full product name including product type, grade, and size | No. 5 Grade 60 Rebar 20 ft, W8x31 A992 Wide Flange Beam, A36 Angle 3 x 3 x 1/4 |
| URL | url | text | Direct link to the product page | https://example.com/product/rebar-5-grade60-20ft |
| Price | price | number | Numeric price per piece, per foot, or per ton, excluding currency symbol | 12.50, 45.00, 850.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary product classification | Rebar, Wide Flange Beam, I-Beam, Channel, Angle, Plate, Tube/Pipe, Flat Bar, Round Bar, Wire Mesh |
| Steel Grade | steel_grade | text | Material grade specification | Grade 40, Grade 60, Grade 75, Grade 80, A36, A992, A706, A615, A572 Grade 50 |
| Deformation Pattern | deformation_pattern | text | Surface deformation type for rebar | Deformed, Plain, Bamboo Pattern |
| Country of Origin | country_of_origin | text | Manufacturing country | USA, Turkey, China, Brazil, India, South Korea |
| Bar Size | bar_size | text | Rebar bar number designation (rebar only) | 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| ASTM Specification | astm_specification | text | Primary ASTM material standard | ASTM A615, ASTM A706, ASTM A992, ASTM A36, ASTM A572, ASTM A955 |
| Depth | depth | number (in) | Nominal depth of structural shapes (beams, channels) | 4, 6, 8, 10, 12, 14, 18, 24, 36 |
| Flange Width | flange_width | number (in) | Width of flanges on beams and channels | 4.0, 5.25, 6.5, 8.0, 10.0, 12.0 |
| Web Thickness | web_thickness | number (in) | Thickness of the web on structural shapes | 0.170, 0.230, 0.285, 0.350, 0.500 |
| Flange Thickness | flange_thickness | number (in) | Thickness of flanges on structural shapes | 0.205, 0.310, 0.435, 0.560, 0.680 |
| Yield Strength | yield_strength | number (ksi) | Minimum yield point stress | 36, 40, 50, 60, 75, 80 |
| Tensile Strength | tensile_strength | number (ksi) | Minimum ultimate tensile stress | 58, 60, 65, 80, 90, 100 |
| Elongation | elongation | number (%) | Minimum percentage elongation in gauge length | 8, 9, 12, 14, 18, 21 |
| Coating/Finish | coatingfinish | text | Surface treatment or coating applied | Black (Bare), Epoxy Coated, Galvanized, Painted, Weathering Steel |
| Weldability | weldability | enum | Whether the product is suitable for field welding | Yes, No, With Preheat |
| Carbon Equivalent | carbon_equivalent | number | Maximum carbon equivalent for weldability | 0.45, 0.55, 0.75 |
| Cross-Sectional Area | cross-sectional_area | number (sq in) | Area of the bar or shape cross section | 0.11, 0.20, 0.31, 0.60, 1.00, 9.12, 14.7 |
| Moment of Inertia | moment_of_inertia | number (in4) | Second moment of area for structural shapes | 30.8, 64.7, 110, 245, 510, 1530 |
| Section Modulus | section_modulus | number (in3) | Elastic section modulus for structural shapes | 9.91, 14.1, 24.3, 35.0, 54.6, 98.3 |
| Application | application | text (list) | Primary intended uses | Concrete Reinforcement, Building Frames, Bridges, Columns, Foundation, Retaining Wall, Highway, Parking Garage |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus ASTM and AISC standards (A615, A992, A36) | [Metals USA](https://www.metalsusa.com/structural-steel-rebar/), [CRSI](https://www.crsi.org/reinforcing-basics/reinforcing-steel/rebar-properties/), [Kloeckner Metals](https://www.kloecknermetals.com/products/steel-beams/a992/), [Hyundai Steel](https://www.hyundai-steel.com/en/product-tech/rebar) |
