# SKU Schema: Structural Steel & Rebar

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | MU-RB5-20, SS-W8X31, KM-A992-W10 |
| Product Name | text | Full product name including product type, grade, and size | No. 5 Grade 60 Rebar 20 ft, W8x31 A992 Wide Flange Beam, A36 Angle 3 x 3 x 1/4 |
| URL | text | Direct link to the product page | https://example.com/product/rebar-5-grade60-20ft |
| Price | number | Numeric price per piece, per foot, or per ton, excluding currency symbol | 12.50, 45.00, 850.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | Metals USA, CMC, Nucor, Gerdau, Hyundai Steel, ArcelorMittal |
| Product Type | enum | Primary product classification | Rebar, Wide Flange Beam, I-Beam, Channel, Angle, Plate, Tube/Pipe, Flat Bar, Round Bar, Wire Mesh |
| Steel Grade | text | Material grade specification | Grade 40, Grade 60, Grade 75, Grade 80, A36, A992, A706, A615, A572 Grade 50 |
| ASTM Specification | text | Primary ASTM material standard | ASTM A615, ASTM A706, ASTM A992, ASTM A36, ASTM A572, ASTM A955 |
| Bar Size | text | Rebar bar number designation (rebar only) | 3, 4, 5, 6, 7, 8, 9, 10, 11, 14, 18 |
| Nominal Diameter | number (in) | Nominal bar diameter for rebar or round bar | 0.375, 0.500, 0.625, 0.750, 1.000, 1.128, 1.270 |
| Depth | number (in) | Nominal depth of structural shapes (beams, channels) | 4, 6, 8, 10, 12, 14, 18, 24, 36 |
| Flange Width | number (in) | Width of flanges on beams and channels | 4.0, 5.25, 6.5, 8.0, 10.0, 12.0 |
| Web Thickness | number (in) | Thickness of the web on structural shapes | 0.170, 0.230, 0.285, 0.350, 0.500 |
| Flange Thickness | number (in) | Thickness of flanges on structural shapes | 0.205, 0.310, 0.435, 0.560, 0.680 |
| Length | number (ft) | Standard stock length | 20, 30, 40, 60 |
| Weight per Foot | number (lb/ft) | Linear weight of bar or structural section | 0.38, 0.67, 1.04, 2.67, 31, 50, 120 |
| Yield Strength | number (ksi) | Minimum yield point stress | 36, 40, 50, 60, 75, 80 |
| Tensile Strength | number (ksi) | Minimum ultimate tensile stress | 58, 60, 65, 80, 90, 100 |
| Elongation | number (%) | Minimum percentage elongation in gauge length | 8, 9, 12, 14, 18, 21 |
| Coating/Finish | text | Surface treatment or coating applied | Black (Bare), Epoxy Coated, Galvanized, Painted, Weathering Steel |
| Deformation Pattern | text | Surface deformation type for rebar | Deformed, Plain, Bamboo Pattern |
| Weldability | enum | Whether the product is suitable for field welding | Yes, No, With Preheat |
| Carbon Equivalent | number | Maximum carbon equivalent for weldability | 0.45, 0.55, 0.75 |
| Cross-Sectional Area | number (sq in) | Area of the bar or shape cross section | 0.11, 0.20, 0.31, 0.60, 1.00, 9.12, 14.7 |
| Moment of Inertia | number (in4) | Second moment of area for structural shapes | 30.8, 64.7, 110, 245, 510, 1530 |
| Section Modulus | number (in3) | Elastic section modulus for structural shapes | 9.91, 14.1, 24.3, 35.0, 54.6, 98.3 |
| Application | text (list) | Primary intended uses | Concrete Reinforcement, Building Frames, Bridges, Columns, Foundation, Retaining Wall, Highway, Parking Garage |
| Bundle Quantity | number | Number of pieces per standard bundle | 1, 10, 25, 50 |
| Country of Origin | text | Manufacturing country | USA, Turkey, China, Brazil, India, South Korea |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus ASTM and AISC standards (A615, A992, A36) | [Metals USA](https://www.metalsusa.com/structural-steel-rebar/), [CRSI](https://www.crsi.org/reinforcing-basics/reinforcing-steel/rebar-properties/), [Kloeckner Metals](https://www.kloecknermetals.com/products/steel-beams/a992/), [Hyundai Steel](https://www.hyundai-steel.com/en/product-tech/rebar) |
