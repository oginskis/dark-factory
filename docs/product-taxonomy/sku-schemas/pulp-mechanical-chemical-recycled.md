# SKU Schema: Pulp (Mechanical, Chemical, Recycled)

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.pulp`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | NBSK-GP-001, SUZ-EB-500, IP-SBSK-200 |
| Product Name | product_name | text | Full commercial product name including grade and fiber origin | Suzano Eucabright BHKP, GP Cellulose NBSK Premium, Mercer Rosenthal BCTMP |
| URL | url | text | Direct link to the product page or datasheet | https://example.com/products/nbsk-premium |
| Price | price | number | Numeric price per metric tonne, excluding currency symbol | 678.00, 520.50, 1150.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, CNY, BRL |
| Wood Type | wood_type | enum | Whether the fiber source is softwood or hardwood | Softwood, Hardwood, Mixed, Non-Wood |
| Trade Grade | trade_grade | text | Internationally recognized market pulp grade abbreviation | NBSK, SBSK, BHKP, BEK, BCTMP, DIP, UKP |
| Form | form | enum | Physical delivery form of the product | Bale, Sheet, Flash-Dried, Wet Lap, Roll, Big Bale |
| Country of Origin | country_of_origin | text | Country or region where the pulp was produced | Canada, Brazil, Sweden, Finland, USA, Indonesia |
| Average Fiber Length | average_fiber_length | number (mm) | Weighted average fiber length | 0.9, 1.1, 2.5, 3.8 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Pulp Process | pulp_process | enum | Primary pulping method used to produce the product | Mechanical, Thermo-Mechanical (TMP), Chemi-Thermo-Mechanical (CTMP), Chemical Kraft, Chemical Sulfite, Recycled/Deinked (DIP) |
| Fiber Source Species | fiber_source_species | text | Tree species or raw material the pulp is made from | Spruce, Pine, Eucalyptus, Birch, Aspen, Acacia, Bagasse, Cotton |
| Bleaching Sequence | bleaching_sequence | enum | Bleaching chemistry classification | ECF (Elemental Chlorine Free), TCF (Totally Chlorine Free), Unbleached |
| ISO Brightness | iso_brightness | number (%) | Brightness measured per ISO 2470 standard | 88, 90, 92, 60, 78 |
| Kappa Number | kappa_number | number | Measure of residual lignin; lower values indicate more delignification | 1.5, 8, 25, 45 |
| Viscosity | viscosity | number (mPa.s) | Intrinsic viscosity indicating fiber degradation level | 750, 850, 1050 |
| Canadian Standard Freeness | canadian_standard_freeness | number (mL) | Drainage rate indicating refining degree per TAPPI T 227 | 500, 650, 720 |
| Moisture Content | moisture_content | number (%) | Water content at point of sale | 10, 12, 50, 90 |
| Fiber Width | fiber_width | number (um) | Average fiber width in micrometres | 14, 18, 30, 38 |
| Fiber Coarseness | fiber_coarseness | number (ug/m) | Mass per unit length of fiber | 80, 160, 250, 300 |
| Tensile Index | tensile_index | number (Nm/g) | Tensile strength normalized to basis weight | 37, 55, 70 |
| Tear Index | tear_index | number (mN.m2/g) | Tear resistance normalized to basis weight | 3.5, 5.6, 10.2 |
| Burst Index | burst_index | number (kPa.m2/g) | Burst strength normalized to basis weight | 1.9, 3.5, 5.0 |
| Bulk | bulk | number (cm3/g) | Specific volume; reciprocal of apparent sheet density | 1.5, 2.2, 2.9 |
| Yield | yield | number (%) | Mass of pulp produced as a percentage of raw material input | 45, 65, 85, 95 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (TAPPI, CEPI definitions, ISO 2470 brightness) | [Global Cellulose Fibers (IP)](https://www.globalcellulosefibers.com/papergrade-pulp), [Suzano Biopulp](https://biopulp.suzano.com.br/en/products), [PaperOnWeb Pulp Grades](https://www.paperonweb.com/gradepl.htm), [Mercer/MM NBSK](https://mm.group/board-paper/products/nbsk/) |
