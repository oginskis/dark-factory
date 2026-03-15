# SKU Schema: Pulp (Mechanical, Chemical, Recycled)

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | NBSK-GP-001, SUZ-EB-500, IP-SBSK-200 |
| Product Name | text | Full commercial product name including grade and fiber origin | Suzano Eucabright BHKP, GP Cellulose NBSK Premium, Mercer Rosenthal BCTMP |
| URL | text | Direct link to the product page or datasheet | https://example.com/products/nbsk-premium |
| Price | number | Numeric price per metric tonne, excluding currency symbol | 678.00, 520.50, 1150.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, CNY, BRL |
| Brand/Manufacturer | text | Company producing or marketing the pulp | Suzano, International Paper, Mercer International, Stora Enso, Resolute Forest Products |
| Pulp Process | enum | Primary pulping method used to produce the product | Mechanical, Thermo-Mechanical (TMP), Chemi-Thermo-Mechanical (CTMP), Chemical Kraft, Chemical Sulfite, Recycled/Deinked (DIP) |
| Wood Type | enum | Whether the fiber source is softwood or hardwood | Softwood, Hardwood, Mixed, Non-Wood |
| Fiber Source Species | text | Tree species or raw material the pulp is made from | Spruce, Pine, Eucalyptus, Birch, Aspen, Acacia, Bagasse, Cotton |
| Trade Grade | text | Internationally recognized market pulp grade abbreviation | NBSK, SBSK, BHKP, BEK, BCTMP, DIP, UKP |
| Bleaching Sequence | enum | Bleaching chemistry classification | ECF (Elemental Chlorine Free), TCF (Totally Chlorine Free), Unbleached |
| ISO Brightness | number (%) | Brightness measured per ISO 2470 standard | 88, 90, 92, 60, 78 |
| Kappa Number | number | Measure of residual lignin; lower values indicate more delignification | 1.5, 8, 25, 45 |
| Viscosity | number (mPa.s) | Intrinsic viscosity indicating fiber degradation level | 750, 850, 1050 |
| Canadian Standard Freeness | number (mL) | Drainage rate indicating refining degree per TAPPI T 227 | 500, 650, 720 |
| Moisture Content | number (%) | Water content at point of sale | 10, 12, 50, 90 |
| Average Fiber Length | number (mm) | Weighted average fiber length | 0.9, 1.1, 2.5, 3.8 |
| Fiber Width | number (um) | Average fiber width in micrometres | 14, 18, 30, 38 |
| Fiber Coarseness | number (ug/m) | Mass per unit length of fiber | 80, 160, 250, 300 |
| Tensile Index | number (Nm/g) | Tensile strength normalized to basis weight | 37, 55, 70 |
| Tear Index | number (mN.m2/g) | Tear resistance normalized to basis weight | 3.5, 5.6, 10.2 |
| Burst Index | number (kPa.m2/g) | Burst strength normalized to basis weight | 1.9, 3.5, 5.0 |
| Bulk | number (cm3/g) | Specific volume; reciprocal of apparent sheet density | 1.5, 2.2, 2.9 |
| Dirt Count | number (mm2/m2) | Visible contaminant area per unit area of pulp sheet | 0.5, 2.0, 8.0 |
| Yield | number (%) | Mass of pulp produced as a percentage of raw material input | 45, 65, 85, 95 |
| Form | enum | Physical delivery form of the product | Bale, Sheet, Flash-Dried, Wet Lap, Roll, Big Bale |
| Bale Weight | number (kg) | Weight per bale or unit of shipment | 200, 250, 500 |
| Application | text (list) | Intended end-use paper or board categories | Tissue, Printing and Writing, Packaging Board, Newsprint, Specialty Paper, Hygiene |
| Certification | text (list) | Chain-of-custody and sustainability certifications | FSC, PEFC, SFI, FSC Mix, EU Ecolabel |
| Country of Origin | text | Country or region where the pulp was produced | Canada, Brazil, Sweden, Finland, USA, Indonesia |
| FDA Food Contact Compliance | enum | Whether the pulp meets FDA food-contact requirements | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (TAPPI, CEPI definitions, ISO 2470 brightness) | [Global Cellulose Fibers (IP)](https://www.globalcellulosefibers.com/papergrade-pulp), [Suzano Biopulp](https://biopulp.suzano.com.br/en/products), [PaperOnWeb Pulp Grades](https://www.paperonweb.com/gradepl.htm), [Mercer/MM NBSK](https://mm.group/board-paper/products/nbsk/) |
