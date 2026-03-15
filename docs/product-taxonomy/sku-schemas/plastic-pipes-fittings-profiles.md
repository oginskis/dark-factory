# SKU Schema: Plastic Pipes, Fittings & Profiles

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | PVC-040-100, 48740, CP-1120 |
| Product Name | text | Full product name including material, type, schedule, and size | PVC Schedule 40 Pressure Pipe 1 in x 10 ft, CPVC 90-Degree Elbow 3/4 in |
| URL | text | Direct link to the product page | https://example.com/product/pvc-sch40-1in |
| Price | number | Numeric price per unit or per foot, excluding currency symbol | 4.98, 12.50, 0.89 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | Charlotte Pipe, Spears Manufacturing, Georg Fischer, LESSO |
| Product Type | enum | Primary product classification | Pipe, Elbow, Tee, Coupling, Reducer, Union, Valve, Cap, Adapter, Profile |
| Material | enum | Primary polymer material | PVC, CPVC, ABS, HDPE, PP, PE, PVDF |
| Schedule/Class | text | Pipe schedule or pressure class designation | Schedule 40, Schedule 80, SDR 11, SDR 17, Class 125, Class 150 |
| Nominal Size | text | Nominal pipe size (NPS or DN) | 1/2 in, 3/4 in, 2 in, DN 50, DN 100 |
| Outside Diameter | number (mm) | Measured outside diameter of the pipe or fitting | 21.3, 26.7, 60.3, 114.3 |
| Wall Thickness | number (mm) | Minimum wall thickness per schedule | 2.77, 3.38, 3.91, 5.54 |
| Inside Diameter | number (mm) | Calculated internal bore diameter | 15.8, 20.9, 52.5, 102.3 |
| Length | number (mm) | Standard pipe length or fitting laying length | 3048, 6096, 1524 |
| Working Pressure | number (psi) | Maximum continuous operating pressure at rated temperature | 150, 280, 370, 480, 630 |
| Connection Type | enum | Method of joining | Solvent Weld, Socket Fusion, Butt Fusion, Threaded, Push-Fit, Flanged, Compression |
| End Style | text | Configuration of pipe or fitting ends | Socket, Spigot, Plain End, Hub, MPT, FPT |
| Application | text (list) | Intended piping system or use | Potable Water, DWV, Sewer, Chemical Transfer, Irrigation, Conduit, Industrial Process |
| Temperature Rating | text | Maximum continuous service temperature | 140 F (60 C), 200 F (93 C), 180 F (82 C) |
| Color | text | Product body color | White, Gray, Dark Gray, Orange, Black, Blue, Yellow |
| ASTM Standard | text (list) | Governing ASTM specifications | ASTM D 1785, ASTM D 2466, ASTM D 2665, ASTM F 441, ASTM D 3034 |
| Certification | text (list) | Third-party certifications and listings | NSF 14, NSF 61, NSF/ANSI 372, UL, UPC, ICC-ES |
| Fitting Configuration | text | Geometry or angle of fitting | 90 Degree, 45 Degree, Straight, Reducing, Wye, Sanitary Tee, Long Turn |
| Chemical Resistance | text | Resistance classification for chemical environments | Excellent, Good, Not Recommended |
| UV Resistance | enum | Whether the product is rated for outdoor UV exposure | Yes, No |
| Flammability Rating | text | Fire-spread and smoke-development rating | UL 94 V-0, ASTM E 84 Class A |
| Weight per Unit | number (kg) | Weight of a single pipe length or fitting | 0.12, 0.45, 2.30, 8.50 |
| Pack Quantity | number | Number of pieces per pack or case | 1, 10, 25, 50, 100 |
| Country of Origin | text | Manufacturing country | USA, China, India, Germany |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 28 attributes from 4 companies plus ASTM standards (D 1785, D 2466, F 441) | [Charlotte Pipe](https://www.charlottepipe.com/products/plastics), [Spears Manufacturing](https://spearsmfg.com/), [U.S. Plastic Corp.](https://www.usplastic.com/catalog/default.aspx?catid=690), [LESSO America](https://lessoamerica.com/) |
