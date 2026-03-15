# SKU Schema: Labels, Tags & Commercial Print Products

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.labels_tags_commercial_print`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | DL-BOPP-4X6-P, ITG-VNL-2X3, CTC-1234-W |
| Product Name | text | Full product name including material, size, and key features | White BOPP Permanent Labels 4x6 Roll, Vinyl Industrial Tags 2x3 with Eyelet, Custom Die-Cut Circle Labels 3 in |
| URL | text | Direct link to the product page | https://example.com/labels/bopp-4x6-permanent |
| Price | number | Numeric price per unit quantity (per roll, per sheet, per thousand), excluding currency symbol | 42.50, 0.08, 125.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Broad category of the printed product | Pressure-Sensitive Label, Hang Tag, Shrink Sleeve, In-Mold Label, Heat Transfer Label, Woven Label, Printed Tag, Barcode Label |
| Face Material | text | Substrate material of the label or tag face stock | White BOPP, Clear BOPP, Vinyl (PVC), Polyester (PET), Semi-Gloss Paper, Kraft Paper, Tyvek, Anodized Aluminum, Cardstock |
| Adhesive Type | enum | Classification of the adhesive backing for labels | Permanent, Removable, Repositionable, Freezer Grade, High-Tack, None (tags) |
| Liner Material | text | Backing liner material for peel-and-stick labels | Silicone-Coated Paper, PET Liner, Glassine, Kraft |
| Delivery Form | enum | How the finished labels or tags are supplied | Roll, Sheet, Fan-Fold, Individual Cut, Strip |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Face Thickness | number (mil) | Thickness of the face stock material in mils | 1.0, 2.0, 2.4, 3.5, 5.0 |
| Adhesive Chemistry | text | Chemical composition of the adhesive | Acrylic, Rubber, Hot-Melt, Water-Based |
| Width | number (mm) | Finished width of the label or tag | 25, 51, 76, 102, 152 |
| Height | number (mm) | Finished height of the label or tag | 13, 25, 51, 76, 102, 152 |
| Shape | enum | Die-cut shape of the label or tag | Rectangle, Square, Circle, Oval, Custom Die-Cut, Rounded Rectangle |
| Corner Radius | number (mm) | Radius of rounded corners where applicable | 0, 1.5, 3, 6 |
| Printing Method | enum | Primary print technology used for production | Flexography, Digital, Thermal Transfer, Direct Thermal, Offset, Screen, Letterpress |
| Number of Colors | number | Maximum number of ink colors in the print design | 1, 2, 4, 6, 8 |
| Finish | enum | Surface treatment applied after printing | Gloss Laminate, Matte Laminate, UV Coating, Soft-Touch Laminate, Uncoated, Varnish |
| Labels per Roll | number | Count of labels per roll for roll-form delivery | 250, 500, 1000, 5000, 10000 |
| Operating Temperature Range | text | Minimum to maximum service temperature after application | -40F to +175F, -20F to +150F, -60F to +300F |
| Outdoor Durability | text | Rated outdoor lifespan of the applied label or tag | 1 year, 3 years, 5 years, 10 years, 20 years |
| Chemical Resistance | enum | Resistance to oils, solvents, and chemicals | None, Moderate, High |
| Water Resistance | enum | Degree of resistance to water and moisture exposure | Not Water Resistant, Water Resistant, Waterproof |
| Variable Data Capability | enum | Whether the product supports barcodes, numbering, or variable text | None, Barcode, Sequential Numbering, QR Code, Full Variable Data |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus industry standards (GHS labeling, UL recognition, Library of Congress label specifications) | [Discount Labels](https://www.discountlabels.com/), [IndustriTAG Catalogs](https://www.industritag.com/resources/catalogs/), [Badger Tag and Label](https://badgertag.com/), [Oliver Guide to Label Printing](https://oliverinc.com/the-oliver-guide-to-commercial-label-printing/) |
