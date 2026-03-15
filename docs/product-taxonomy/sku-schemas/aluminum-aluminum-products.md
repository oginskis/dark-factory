# SKU Schema: Aluminum & Aluminum Products

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | AL6061-T6-125-48X96, 3003-H14-063 |
| Product Name | text | Full product name including alloy, temper, form, and dimensions | 6061-T6 Aluminum Sheet 0.125in x 48in x 96in, 3003-H14 Aluminum Plate 0.250in |
| URL | text | Direct link to the product page | https://example.com/product/6061-t6-aluminum-sheet |
| Price | number | Numeric unit price (per piece, per foot, or per pound) excluding currency symbol | 89.50, 12.75, 3.45 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Mill | text | Aluminum manufacturer or mill name | Alcoa, Novelis, Kaiser Aluminum, Constellium, Hindalco, Norsk Hydro |
| Product Form | enum | Physical shape of the product | Sheet, Plate, Coil, Round Bar, Flat Bar, Square Bar, Hex Bar, Angle, Channel, Beam, Tube, Pipe, Extrusion, Disc, Tread Plate |
| Alloy | text | Aluminum alloy designation per Aluminum Association or EN standard | 1100, 2024, 3003, 5052, 5083, 6061, 6063, 7075, Mic-6 |
| Alloy Series | enum | Alloy series indicating primary alloying element | 1xxx (Pure), 2xxx (Copper), 3xxx (Manganese), 5xxx (Magnesium), 6xxx (Mg-Si), 7xxx (Zinc) |
| Temper | text | Temper designation indicating mechanical and thermal treatment | O, H14, H32, T3, T4, T6, T651, T73 |
| Thickness | number (in) | Material thickness for flat products | 0.020, 0.063, 0.125, 0.250, 0.500, 1.000 |
| Width | number (in) | Width of flat products (sheet, plate, coil) | 36, 48, 60, 72 |
| Length | number (in) | Length of flat products or bar stock | 96, 120, 144 |
| Outside Diameter | number (in) | Outer diameter for round bar, tube, and pipe | 0.250, 0.500, 1.000, 3.000, 6.000 |
| Wall Thickness | number (in) | Wall thickness for tube and pipe products | 0.035, 0.049, 0.065, 0.125, 0.250 |
| Profile Shape | text | Cross-section shape for extrusion products | T-Slot, U-Channel, L-Angle, Custom Profile, Square Tube, Rectangular Tube |
| Surface Finish | text | Surface treatment or condition | Mill Finish, Brushed, Anodized, Bright, Polished, Painted, Powder Coated |
| Anodize Type | text | Anodizing specification when applicable | Clear Anodize, Hard Anodize (Type III), Color Anodize, MIL-A-8625 Type II |
| Weight per Unit | number (lbs) | Weight of a single piece or per linear foot | 1.45, 5.80, 24.50 |
| Density | number (g/cm3) | Material density of the specific alloy | 2.70, 2.71, 2.78, 2.81 |
| Yield Strength | number (ksi) | Minimum yield strength of the alloy-temper combination | 4, 21, 35, 40, 73 |
| Tensile Strength | number (ksi) | Minimum ultimate tensile strength | 11, 26, 38, 45, 83 |
| Elongation | number (%) | Minimum elongation at break | 3, 8, 12, 18, 25 |
| Machinability | enum | Relative machinability rating | Poor, Fair, Good, Excellent |
| Weldability | enum | Relative weldability rating | Poor, Fair, Good, Excellent |
| Corrosion Resistance | enum | Relative corrosion resistance rating | Fair, Good, Very Good, Excellent |
| Tolerance | text | Dimensional tolerance standard | ASTM B209, AMS-QQ-A-250, EN 485 |
| Certification | text (list) | Quality and compliance certifications | ASTM, AMS, ISO 9001, EN 573, RoHS |
| Mill Test Report | boolean | Whether a mill test report is included with purchase | Yes, No |
| Country of Origin | text | Country where the aluminum was produced | USA, Canada, Germany, Norway, China, India |
| Unit of Measure | text | Pricing and selling unit | Per Piece, Per Foot, Per Pound |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus Aluminum Association standards and ASTM B209 | [Metals Depot](https://www.metalsdepot.com/aluminum-products/aluminum-sheet), [Pierce Aluminum](https://piercealuminum.com/products/), [Eastern Metal Supply](https://www.easternmetal.com/sheet-plate), [Howard Precision Metals](https://www.howardprecision.com/aluminum/) |
