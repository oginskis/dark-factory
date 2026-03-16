# SKU Schema: Aggregates (Sand, Gravel, Crushed Stone)

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials
**Taxonomy ID:** `minerals.aggregates`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Supplier or quarry product identifier | AGG-57-GRN, SND-C33-WSH, GRV-PEA-NAT |
| Product Name | product_name | text | — | Full product name including material type, size, and source | No. 57 Crushed Limestone, ASTM C33 Concrete Sand, 3/4 inch Pea Gravel Washed |
| URL | url | text | — | Direct link to the product page | https://example.com/products/57-crushed-stone |
| Price | price | number | — | Numeric price per unit (per ton, per cubic yard, or per load) | 18.50, 32.00, 45.00, 120.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Material Type | material_type | enum | — | Primary aggregate classification | Crushed Stone, Natural Gravel, Sand, Recycled Concrete Aggregate, Slag Aggregate, Riprap |
| Source Rock Type | source_rock_type | text | — | Geological classification of the parent rock | Limestone, Granite, Basalt, Quartzite, Sandstone, Dolomite, Trap Rock, Gneiss |
| Country of Origin | country_of_origin | text | — | Country where the aggregate was quarried | USA, Canada, UK, Germany, Australia |
| ASTM Size Number | astm_size_number | text | — | ASTM D448 or C33 standard size designation | No. 2, No. 4, No. 57, No. 67, No. 8, No. 89, No. 10, C33 Fine |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Supplier | supplier | text | — | Quarry operator or materials company name | Heidelberg Materials, CRH Americas, Cemex, Geneva Rock, Martin Marietta, Vulcan Materials |
| Fineness Modulus | fineness_modulus | number | — | FM value for fine aggregates per ASTM C136 (2.3-3.1 for concrete sand) | 2.3, 2.6, 2.8, 3.1 |
| Shape | shape | enum | — | Predominant particle shape | Angular, Sub-angular, Sub-rounded, Rounded, Flat and Elongated |
| Color | color | text | — | Visual color of the aggregate material | Gray, Tan, Brown, White, Red, Black, Mixed |
| Specific Gravity | specific_gravity | number | — | Apparent specific gravity (saturated surface-dry) | 2.40, 2.55, 2.65, 2.70, 2.80 |
| Bulk Density | bulk_density | number | kg/m3 | Loose or compacted bulk density | 1400, 1520, 1600, 1760, 2000 |
| Absorption | absorption | number | % | Water absorption capacity (ASTM C127/C128) | 0.5, 1.0, 2.0, 3.5 |
| LA Abrasion Loss | la_abrasion_loss | number | % | Los Angeles abrasion loss percentage (ASTM C131) | 15, 20, 30, 40, 50 |
| Soundness Loss | soundness_loss | number | % | Magnesium or sodium sulfate soundness loss (ASTM C88) | 2, 5, 8, 12, 18 |
| Washed | washed | enum | — | Whether the aggregate has been washed to remove fines | Yes, No |
| Gradation Compliance | gradation_compliance | text | — | Applicable standard specification the product meets | ASTM C33, ASTM D448, DOT Class A, DOT Class B |
| Deleterious Content | deleterious_content | number | % | Percentage of clay lumps, friable particles, and other deleterious materials | 0.5, 1.0, 2.0, 3.0 |
| Organic Impurity Test | organic_impurity_test | text | — | ASTM C40 color test result for fine aggregates | Lighter than standard, Standard, Darker than standard |
| Application | application | text (list) | — | Primary intended construction uses | Ready-Mix Concrete, Asphalt, Road Base, Backfill, Drainage, Landscaping, Railroad Ballast, Rip Rap |
| Unit of Sale | unit_of_sale | text | — | How the product is sold | Per Ton, Per Cubic Yard, Per Load, Per Bag |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 30 attributes from 4 companies plus industry standards (ASTM C33, ASTM D448, ASTM C131, ASTM C136) | [Heidelberg Materials](https://www.heidelbergmaterials.us/products/aggregates), [Geneva Rock](https://genevarock.com/products/sand-and-gravel/), [CRH Americas](https://www.crhamericasmaterials.com/products-and-services/aggregates), [Cemex](https://www.cemexusa.com/products/aggregates) |
