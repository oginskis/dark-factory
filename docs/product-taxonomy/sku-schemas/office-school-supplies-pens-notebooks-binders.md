# SKU Schema: Office & School Supplies (Pens, Notebooks, Binders)

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 50786-CC, ST63315, 2498023 |
| Product Name | text | Full product name including brand, type, and key specification | Staples Retractable Ballpoint Pen Fine 0.7mm Black Dozen, Five Star 3-Subject Notebook College Ruled 150 Sheets, Avery Heavy-Duty 3-Ring Binder 2 Inch |
| URL | text | Direct link to the product page | https://example.com/product/ballpoint-pen-fine-black |
| Price | number | Numeric price per unit or pack, excluding currency symbol | 3.49, 8.99, 12.49 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or product brand name | Staples, Pilot, Paper Mate, Bic, Mead, Five Star, Avery, 3M |
| Product Category | enum | Primary product type | Pens, Pencils, Markers, Highlighters, Notebooks, Notepads, Binders, Folders, Sticky Notes, Tape, Staplers, Paper Clips |
| Sub-Type | text | Specific product sub-type within category | Ballpoint, Gel, Rollerball, Felt Tip, Mechanical Pencil, Composition Book, Spiral Notebook, Ring Binder, Pocket Folder |
| Ink Type | enum | Type of ink for writing instruments | Ballpoint, Gel, Rollerball, Felt Tip, Liquid Ink, Dry Erase, Permanent |
| Ink Color | text (list) | Available ink or lead colors | Black, Blue, Red, Green, Assorted |
| Tip Size | text (mm) | Point or tip diameter for writing instruments | 0.5mm, 0.7mm, 1.0mm, 1.5mm |
| Tip Style | enum | Tip shape classification | Fine, Medium, Bold, Ultra-Fine, Chisel, Bullet |
| Barrel Material | text | Material of the pen or pencil body | Plastic, Rubber Grip, Metal, Stainless Steel, Wood |
| Retractable | boolean | Whether the pen has a retractable tip mechanism | true, false |
| Refillable | boolean | Whether the writing instrument accepts ink refills | true, false |
| Paper Size | text | Sheet dimensions for notebooks, pads, and binders | 8.5 x 11 in, A4, 6 x 9 in, 5 x 8 in, A5 |
| Ruling Type | enum | Line pattern printed on the paper | College Ruled, Wide Ruled, Graph (Quad), Dot Grid, Unlined, Legal Ruled |
| Sheet Count | number | Number of sheets or pages in a notebook or pad | 70, 100, 150, 200, 500 |
| Paper Weight | text (gsm) | Paper weight or thickness in grams per square metre | 56 gsm, 75 gsm, 90 gsm |
| Binder Ring Type | enum | Ring mechanism type for binders | O-Ring, D-Ring, EZD Ring, Slant-D |
| Binder Capacity | text (in) | Ring diameter or sheet capacity for binders | 0.5 in, 1 in, 2 in, 3 in, 4 in |
| Cover Material | text | Cover or binding material | Polypropylene, Cardboard, Vinyl, Leather, Poly, Pressboard |
| Color | text (list) | Exterior or body color options | Black, Blue, Red, White, Assorted, Clear |
| Pack Quantity | number | Number of items per pack or box | 1, 4, 12, 24, 60 |
| Recycled Content | text (%) | Percentage of post-consumer or recycled material | 0%, 30%, 50%, 100% |
| Certifications | text (list) | Environmental or quality certifications | FSC Certified, SFI Certified, Green Seal, PEFC |
| Dimensions | text (in) | Overall product dimensions length x width x height | 5.75 x 0.5 x 0.5, 10.5 x 8 x 0.6, 11.5 x 10.3 x 2.3 |
| Weight | number (oz) | Product weight | 0.3, 8.0, 14.5 |
| UPC | text | Universal Product Code barcode number | 071641104525, 078895501254 |
| Country of Origin | text | Country where the product is manufactured | USA, China, Japan, Mexico, Germany |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry classification systems (GPC, UNSPSC) | [Staples](https://www.staples.com/Pens/cat_CL110001), [Amazon Office Supplies](https://www.amazon.com/Office-Supplies/b?node=1069242), [Target School Supplies](https://www.target.com/c/school-office-supplies/-/N-5xsxr), [FedEx Office](https://www.office.fedex.com/default/office-supplies) |
