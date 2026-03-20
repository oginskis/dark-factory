# SKU Schema: Office & School Supplies (Pens, Notebooks, Binders)

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.office_school_supplies`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 50786-CC, ST63315, 2498023 |
| Product Name | product_name | text | — | yes | Full product name including brand, type, and key specification | Staples Retractable Ballpoint Pen Fine 0.7mm Black Dozen, Five Star 3-Subject Notebook College Ruled 150 Sheets, Avery Heavy-Duty 3-Ring Binder 2 Inch |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/ballpoint-pen-fine-black |
| Price | price | number | — | yes | Numeric price per unit or pack, excluding currency symbol | 3.49, 8.99, 12.49 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Category | product_category | enum | — | — | Primary product type | Pens, Pencils, Markers, Highlighters, Notebooks, Notepads, Binders, Folders, Sticky Notes, Tape, Staplers, Paper Clips |
| Sub-Type | sub-type | text | — | — | Specific product sub-type within category | Ballpoint, Gel, Rollerball, Felt Tip, Mechanical Pencil, Composition Book, Spiral Notebook, Ring Binder, Pocket Folder |
| Ink Type | ink_type | enum | — | — | Type of ink for writing instruments | Ballpoint, Gel, Rollerball, Felt Tip, Liquid Ink, Dry Erase, Permanent |
| Barrel Material | barrel_material | text | — | — | Material of the pen or pencil body | Plastic, Rubber Grip, Metal, Stainless Steel, Wood |
| Ruling Type | ruling_type | enum | — | — | Line pattern printed on the paper | College Ruled, Wide Ruled, Graph (Quad), Dot Grid, Unlined, Legal Ruled |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Binder Ring Type | binder_ring_type | enum | — | — | Ring mechanism type for binders | O-Ring, D-Ring, EZD Ring, Slant-D |
| Cover Material | cover_material | text | — | — | Cover or binding material | Polypropylene, Cardboard, Vinyl, Leather, Poly, Pressboard |
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, China, Japan, Mexico, Germany |
| Ink Color | ink_color | text (list) | — | — | Available ink or lead colors | Black, Blue, Red, Green, Assorted |
| Tip Style | tip_style | enum | — | — | Tip shape classification | Fine, Medium, Bold, Ultra-Fine, Chisel, Bullet |
| Retractable | retractable | boolean | — | — | Whether the pen has a retractable tip mechanism | true, false |
| Refillable | refillable | boolean | — | — | Whether the writing instrument accepts ink refills | true, false |
| Color | color | text (list) | — | — | Exterior or body color options | Black, Blue, Red, White, Assorted, Clear |
| Pack Quantity | pack_quantity | number | — | — | Number of items per pack or box | 1, 4, 12, 24, 60 |
| Recycled Content | recycled_content | text | % | — | Percentage of post-consumer or recycled material | 0%, 30%, 50%, 100% |
| Certifications | certifications | text (list) | — | — | Environmental or quality certifications | FSC Certified, SFI Certified, Green Seal, PEFC |
| Dimensions | dimensions | text | in | — | Overall product dimensions length x width x height | 5.75 x 0.5 x 0.5, 10.5 x 8 x 0.6, 11.5 x 10.3 x 2.3 |
| UPC | upc | text | — | — | Universal Product Code barcode number | 071641104525, 078895501254 |
| Tip Size | tip_size | text | mm | — | Point or tip diameter for writing instruments | 0.5mm, 0.7mm, 1.0mm, 1.5mm |
| Paper Size | paper_size | text | — | — | Sheet dimensions for notebooks, pads, and binders | 8.5 x 11 in, A4, 6 x 9 in, 5 x 8 in, A5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry classification systems (GPC, UNSPSC) | [Staples](https://www.staples.com/Pens/cat_CL110001), [Amazon Office Supplies](https://www.amazon.com/Office-Supplies/b?node=1069242), [Target School Supplies](https://www.target.com/c/school-office-supplies/-/N-5xsxr), [FedEx Office](https://www.office.fedex.com/default/office-supplies) |
