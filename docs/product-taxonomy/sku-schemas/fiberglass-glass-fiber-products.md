# SKU Schema: Fiberglass & Glass Fiber Products

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | FG-7781-50, BGF-1543-38, JM-3000-MAT |
| Product Name | text | Full product name including key specs such as product form, weight, and glass type | Style 7781 E-Glass Fabric 8.9oz 38in, BGF 1543 S-Glass Fabric, Johns Manville Chopped Strand Mat 300gsm |
| URL | text | Direct link to the product page | https://example.com/product/7781-fiberglass-fabric |
| Price | number | Numeric price per linear metre, per square metre, per kg, or per roll, excluding currency symbol | 4.50, 12.99, 28.00, 85.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY, JPY |
| Brand | text | Manufacturer or supplier name | Owens Corning, Johns Manville, BGF Industries, Jushi, Fibre Glast, Hexcel, AGY, Nippon Electric Glass |
| Product Form | enum | Physical form of the fiberglass product | Woven Fabric, Chopped Strand Mat, Roving, Chopped Strand, Continuous Filament Mat, Tape, Sleeve, Veil, Stitched Combo Mat |
| Glass Type | enum | Type of glass fiber composition | E-Glass, S-Glass, S-2 Glass, C-Glass, ECR-Glass, AR-Glass, D-Glass, R-Glass |
| Weave Pattern | text | Weave construction style for woven fabrics | Plain Weave, Twill Weave, Satin Weave (4HS, 8HS), Leno Weave, Unidirectional, Biaxial, Triaxial |
| Fabric Style Number | text | Industry-standard style designation for woven fabrics | 108, 1080, 1522, 2116, 3313, 7628, 7781, 1543 |
| Areal Weight | number (g/m2) | Mass per unit area of the fabric, mat, or veil | 25, 50, 100, 200, 300, 450, 600, 800 |
| Thickness | number (mm) | Nominal thickness of the fabric, mat, or product | 0.04, 0.09, 0.17, 0.23, 0.38, 0.64, 1.00 |
| Width | number (mm) | Roll or tape width | 25, 50, 100, 254, 305, 914, 1016, 1270, 1524 |
| Roll Length | number (m) | Length of fabric or mat per roll | 10, 25, 50, 100, 250, 500 |
| Filament Diameter | number (um) | Diameter of individual glass filaments | 3, 5, 7, 9, 11, 13, 17, 24 |
| Tex/Yield | text | Linear density of yarn or roving (tex or yards per pound) | 22 tex, 68 tex, 136 tex, 2400 tex, 4800 tex, 9600 yards/lb |
| Thread Count (Warp) | number (threads/cm) | Number of warp threads per centimetre in woven fabric | 9, 12, 17, 22, 25 |
| Thread Count (Weft) | number (threads/cm) | Number of weft (fill) threads per centimetre in woven fabric | 7, 9, 12, 17, 22 |
| Tensile Strength (Warp) | number (N/25mm) | Breaking strength in the warp direction per 25mm strip | 200, 400, 600, 800, 1200, 2000 |
| Tensile Strength (Weft) | number (N/25mm) | Breaking strength in the weft direction per 25mm strip | 150, 350, 500, 700, 1000, 1800 |
| Sizing/Finish | text | Chemical treatment applied to the fibers for resin compatibility | Silane, Starch-Oil, Epoxy-Compatible, Vinyl Ester-Compatible, Polyester-Compatible, Multi-Compatible |
| Resin Compatibility | text (list) | Resin systems the product is designed to work with | Epoxy, Polyester, Vinyl Ester, Phenolic, Polyurethane |
| Moisture Content | number (%) | Maximum allowable moisture content of the product | 0.10, 0.15, 0.20, 0.50 |
| Loss on Ignition | number (%) | Percentage of organic content (binder/sizing) burned off at high temperature | 0.3, 0.5, 1.0, 2.0, 4.0, 5.5 |
| Melting Point | number (C) | Softening or melting temperature of the glass fibers | 840, 1065, 1120, 1500 |
| Application | text (list) | Primary intended uses for the product | Boat Building, Automotive, Aerospace, Wind Energy, Printed Circuit Board, Pipe Repair, Construction, Corrosion Barrier |
| Certification | text (list) | Quality and industry certifications | ISO 9001, IPC-4412, MIL-Y-1140, ABS, DNV, Lloyds |
| Applicable Standard | text (list) | Test and specification standards the product meets | ASTM D578, ASTM D579, ISO 2078, IPC-4412, EN 13496 |
| Country of Origin | text | Country where the product was manufactured | USA, China, France, Belgium, Japan, India |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (ASTM D578, IPC-4412) | [Fibre Glast](https://www.fibreglast.com/category/Fiberglass), [BGF Industries](https://bgf.com/glass-fabrics/), [Johns Manville Fiberglass](https://www.jm.com/en/fiberglass/), [Composite Envisions](https://www.compositeenvisions.com/composite-fabrics/fiberglass) |
