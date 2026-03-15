# SKU Schema: Aggregates (Sand, Gravel, Crushed Stone)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Supplier or quarry product identifier | AGG-57-GRN, SND-C33-WSH, GRV-PEA-NAT |
| Product Name | text | Full product name including material type, size, and source | No. 57 Crushed Limestone, ASTM C33 Concrete Sand, 3/4 inch Pea Gravel Washed |
| URL | text | Direct link to the product page | https://example.com/products/57-crushed-stone |
| Price | number | Numeric price per unit (per ton, per cubic yard, or per load) | 18.50, 32.00, 45.00, 120.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Supplier | text | Quarry operator or materials company name | Heidelberg Materials, CRH Americas, Cemex, Geneva Rock, Martin Marietta, Vulcan Materials |
| Material Type | enum | Primary aggregate classification | Crushed Stone, Natural Gravel, Sand, Recycled Concrete Aggregate, Slag Aggregate, Riprap |
| Source Rock Type | text | Geological classification of the parent rock | Limestone, Granite, Basalt, Quartzite, Sandstone, Dolomite, Trap Rock, Gneiss |
| ASTM Size Number | text | ASTM D448 or C33 standard size designation | No. 2, No. 4, No. 57, No. 67, No. 8, No. 89, No. 10, C33 Fine |
| Nominal Size | text (mm) | Nominal maximum and minimum particle size range | 0-4.75, 4.75-25, 12.5-37.5, 25-63, 63-150 |
| Fineness Modulus | number | FM value for fine aggregates per ASTM C136 (2.3-3.1 for concrete sand) | 2.3, 2.6, 2.8, 3.1 |
| Shape | enum | Predominant particle shape | Angular, Sub-angular, Sub-rounded, Rounded, Flat and Elongated |
| Color | text | Visual color of the aggregate material | Gray, Tan, Brown, White, Red, Black, Mixed |
| Specific Gravity | number | Apparent specific gravity (saturated surface-dry) | 2.40, 2.55, 2.65, 2.70, 2.80 |
| Bulk Density | number (kg/m3) | Loose or compacted bulk density | 1400, 1520, 1600, 1760, 2000 |
| Absorption | number (%) | Water absorption capacity (ASTM C127/C128) | 0.5, 1.0, 2.0, 3.5 |
| LA Abrasion Loss | number (%) | Los Angeles abrasion loss percentage (ASTM C131) | 15, 20, 30, 40, 50 |
| Soundness Loss | number (%) | Magnesium or sodium sulfate soundness loss (ASTM C88) | 2, 5, 8, 12, 18 |
| Washed | enum | Whether the aggregate has been washed to remove fines | Yes, No |
| Gradation Compliance | text | Applicable standard specification the product meets | ASTM C33, ASTM D448, DOT Class A, DOT Class B |
| Deleterious Content | number (%) | Percentage of clay lumps, friable particles, and other deleterious materials | 0.5, 1.0, 2.0, 3.0 |
| Organic Impurity Test | text | ASTM C40 color test result for fine aggregates | Lighter than standard, Standard, Darker than standard |
| Application | text (list) | Primary intended construction uses | Ready-Mix Concrete, Asphalt, Road Base, Backfill, Drainage, Landscaping, Railroad Ballast, Rip Rap |
| Unit of Sale | text | How the product is sold | Per Ton, Per Cubic Yard, Per Load, Per Bag |
| Minimum Order Quantity | text | Minimum order size | 1 ton, 5 tons, Truckload, Barge Load |
| Delivery Method | text | How the product is delivered | Pickup, Dump Truck, Conveyor, Barge, Rail |
| Quarry Location | text | Name or location of the producing quarry | Geneva Rock Point of the Mountain, Martin Marietta Midlothian |
| DOT Approval | text | State or federal Department of Transportation approval status | Approved, Not Approved, Pending |
| Country of Origin | text | Country where the aggregate was quarried | USA, Canada, UK, Germany, Australia |
| Certification | text (list) | Quality or testing certifications | ASTM compliant, AMRL certified, DOT approved, ISO 9001 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM C33, ASTM D448, ASTM C131, ASTM C136) | [Heidelberg Materials](https://www.heidelbergmaterials.us/products/aggregates), [Geneva Rock](https://genevarock.com/products/sand-and-gravel/), [CRH Americas](https://www.crhamericasmaterials.com/products-and-services/aggregates), [Cemex](https://www.cemexusa.com/products/aggregates) |
