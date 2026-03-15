# SKU Schema: Iron & Steel (Bars, Sheets, Coils, Beams)

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HRS-1048-4X8, A36-WF-W8X31, SS-304-16GA |
| Product Name | text | Full product name including key specs such as grade, form, and dimensions | A36 Hot Rolled Steel Sheet 16 Gauge 48 x 96, W8x31 A992 Wide Flange Beam 20ft |
| URL | text | Direct link to the product page | https://example.com/product/a36-hot-rolled-sheet-16ga |
| Price | number | Numeric unit price (per piece, per foot, or per pound depending on seller) excluding currency symbol | 45.99, 189.50, 2.35 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Mill | text | Steel manufacturer or mill name | Nucor, US Steel, ArcelorMittal, Nippon Steel, SSAB, Tata Steel |
| Product Form | enum | Physical shape of the product | Sheet, Plate, Coil, Flat Bar, Round Bar, Square Bar, Angle, Channel, Wide Flange Beam, I-Beam, Tube, Pipe, Hex Bar |
| Steel Type | enum | Broad classification of the steel | Carbon Steel, Stainless Steel, Alloy Steel, Tool Steel, Galvanized Steel, Weathering Steel |
| Grade/Specification | text | ASTM, EN, or JIS grade designation | A36, A992, A572-50, A500, A1011 CS, 304, 316L, 4140, EN S275JR |
| Thickness | text (in) | Material thickness in inches or gauge. Sheets and plates in decimal inches or gauge number, structural shapes by web thickness | 0.0598 (16 ga), 0.25, 0.5, 1.0 |
| Width | number (in) | Width of flat products (sheet, plate, coil, flat bar) | 36, 48, 60, 72 |
| Length | number (ft) | Length of the product. Sheets and plates in inches, bars and beams in feet | 8, 10, 20, 40 |
| Outside Diameter | number (in) | Outer diameter for round bar, tube, and pipe products | 0.5, 1.0, 2.0, 6.625 |
| Wall Thickness | number (in) | Wall thickness for tube and pipe products | 0.065, 0.120, 0.250, 0.500 |
| Section Size | text | Standard designation for structural shapes (depth x weight per foot) | W8x31, W10x22, C6x8.2, L3x3x0.25, HSS4x4x0.25 |
| Weight per Unit Length | number (lbs/ft) | Linear weight for bars, beams, channels, and angles | 8.2, 22, 31, 50 |
| Yield Strength | number (ksi) | Minimum yield strength of the material | 36, 50, 55, 70 |
| Tensile Strength | number (ksi) | Minimum ultimate tensile strength | 58, 65, 70, 100 |
| Surface Finish | text | Surface condition or coating applied to the product | Hot Rolled (Black), Cold Rolled, Pickled and Oiled, Galvanized, Galvannealed, Aluminized, Painted |
| Coating Weight | text | Zinc or other coating weight designation for coated products | G30, G60, G90, A25, A40 |
| Edge Condition | text | Edge type for sheet and coil products | Mill Edge, Slit Edge, Sheared Edge |
| Tolerance | text | Dimensional tolerance standard | ASTM A568, ASTM A6, EN 10029 |
| Heat Number | text | Mill heat number for traceability | A12345, B67890 |
| Chemistry | text | Key alloying element percentages | C 0.26 max, Mn 0.60-0.90, Cr 18.0-20.0, Ni 8.0-10.5 |
| Hardness | text | Hardness measurement where applicable | HRB 70, HRC 28, BHN 120 |
| Mill Certification | boolean | Whether a mill test report (MTR) is included | Yes, No |
| Domestic/Import | enum | Origin classification | Domestic, Import |
| Country of Origin | text | Country where the steel was produced | USA, Brazil, South Korea, Japan, Germany, India |
| Certification | text (list) | Quality and compliance certifications | ASTM, ISO 9001, CE, EN 10204 3.1 |
| Unit of Measure | text | Pricing and selling unit | Per Piece, Per Foot, Per Pound, Per CWT |
| Minimum Order Quantity | number | Minimum quantity required for purchase | 1, 5, 100 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM steel standards (A36, A992, A653, A568) | [Russel Metals](https://www.russelmetals.com/en/product/sheet-and-coil/), [Metals Depot](https://www.metalsdepot.com/), [Norfolk Iron & Metal](https://www.norfolkiron.com/steel-beams/), [Majestic Steel](https://www.majesticsteel.com/) |
