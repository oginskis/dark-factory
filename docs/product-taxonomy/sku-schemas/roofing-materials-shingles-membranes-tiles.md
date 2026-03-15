# SKU Schema: Roofing Materials (Shingles, Membranes, Tiles)

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.roofing`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | OC-DUR-DW, GAF-TS-HDZ, FS-UPTPO60 |
| Product Name | text | Full product name including type, product line, and color or size | Owens Corning TruDefinition Duration Driftwood, GAF Timberline HDZ Charcoal, Firestone UltraPly TPO 60 mil |
| URL | text | Direct link to the product page | https://example.com/product/oc-duration-driftwood |
| Price | number | Numeric price per bundle, per square, per roll, or per tile, excluding currency symbol | 32.00, 98.00, 245.00, 1.85 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Roofing Type | enum | Primary product classification | Asphalt Shingle, Membrane, Clay Tile, Concrete Tile, Metal Panel, Synthetic Slate, Wood Shake |
| Membrane Material | text | Polymer type for flat roofing membranes (membranes only) | TPO, EPDM, PVC, Modified Bitumen, Built-Up |
| Tile Material | text | Base material of roofing tiles (tiles only) | Clay, Concrete, Slate, Synthetic |
| Fire Classification | text | Fire resistance rating per UL 790 or ASTM E 108 | Class A, Class B, Class C |
| Country of Origin | text | Manufacturing country | USA, Mexico, Canada, Spain, Italy, Japan |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Shingle Style | text | Architectural style of asphalt shingles (shingles only) | 3-Tab, Architectural/Dimensional, Designer, Luxury |
| Tile Profile | text | Shape profile of roofing tiles (tiles only) | Flat, S-Shape, Mission/Barrel, Interlocking, Shake |
| Thickness | number (mil) | Membrane thickness in mils or tile/shingle thickness in inches | 45, 60, 80, 90 |
| Width | number (in) | Individual shingle, tile, or membrane roll width | 12, 13.25, 36, 72, 120 |
| Exposure | number (in) | Exposed face area per unit when installed with overlap | 5, 5.625, 6.5, 17 |
| Coverage per Unit | number (sq ft) | Net roof area covered per bundle, roll, or pallet | 25, 32.3, 33.3, 98.4, 100 |
| Color | text | Product color or color blend name | Driftwood, Charcoal, Weathered Wood, Onyx Black, Antique Red, Terra Cotta, White, Tan |
| Wind Resistance | text | Maximum rated wind speed | 110 MPH, 130 MPH, 150 MPH, ASTM D7158 Class H |
| Impact Resistance | text | Hail impact resistance rating per UL 2218 | Class 1, Class 2, Class 3, Class 4 |
| Solar Reflectance | number | Initial solar reflectance index for cool roof rating | 0.25, 0.65, 0.78, 0.80 |
| Thermal Emittance | number | Infrared emittance for energy rating | 0.75, 0.85, 0.90 |
| Warranty | text | Manufacturer warranty term | Limited Lifetime, 30-Year, 25-Year, 50-Year, 20-Year |
| Installation Method | text | Primary installation technique | Nail-Down, Fully Adhered, Mechanically Attached, Ballasted, Self-Adhering |
| Application | text (list) | Roof type suitability | Steep Slope Residential, Low Slope Commercial, Flat Roof, Re-Roofing, New Construction |
| Underlayment Required | enum | Whether specific underlayment is required | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus ASTM and UL standards (D 3462, D 7158, E 108, UL 2218) | [Owens Corning](https://www.owenscorning.com/en-us/roofing/shingles), [GAF](https://www.gaf.com/en-us/roofing-materials/residential-roofing-materials/shingles), [Firestone Building Products](https://toplineroofing.com/imageserver/UserMedia/ywpgallery/Firestone/TPO/TPOUltraPly.pdf), [Eagle Roofing](https://eagleroofing.com/) |
