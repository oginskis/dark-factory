# SKU Schema: Institutional Furniture (School, Hospital, Restaurant)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 9018, 164A3232BKD, MDS89, ZUM18 |
| Product Name | text | Full product name including series, type, and key dimensions | Virco 9000 Series 4-Leg Stack Chair 18in, Lancaster Alloy 32x32in Outdoor Table with 4 Chairs |
| URL | text | Direct link to the product page | https://virco.com/product/9000-series-4-leg-stack-chair/ |
| Price | number | Numeric unit price excluding currency symbol | 89.00, 349.99, 1250.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Virco, Lancaster Table and Seating, Medline, Stryker, Hillrom, KI |
| Institution Type | enum | Primary institutional market the product serves | School, Hospital/Healthcare, Restaurant/Foodservice, Office, Multi-Purpose |
| Product Type | enum | Specific furniture classification | Chair, Table, Desk, Bed, Bench, Booth, High Chair, Overbed Table, Combo Unit |
| Seat Height | text (mm) | Seat height or adjustable height range | 254, 305, 356, 406, 457, 559-787 |
| Overall Height | number (mm) | Total height of the product | 787, 762, 914 |
| Overall Width | number (mm) | Total width of the product | 457, 610, 813, 914 |
| Overall Depth | number (mm) | Total depth of the product | 457, 508, 610 |
| Tabletop/Surface Dimensions | text (mm) | Work surface or tabletop size as width x depth | 457x610, 610x1219, 813x813 |
| Weight Capacity | number (kg) | Maximum recommended user or load weight | 136, 181, 227, 454 |
| Product Weight | number (kg) | Net weight of the product | 4.5, 9.1, 18.2, 68.0 |
| Frame Material | text | Primary structural material | Tubular Steel, Steel, Aluminum, Chrome-Plated Steel |
| Seat/Surface Material | text | Material of the seating surface, tabletop, or work surface | Molded Polypropylene, Hard Plastic, High-Pressure Laminate, Upholstered Vinyl, Molded Polyethylene |
| Color | text | Available product color or finish | Black, Graphite, Navy, Red, Walnut, Oak, Onyx, Distressed Copper |
| Number of Colors Available | number | Total color options for the product | 5, 12, 39 |
| Height Adjustable | enum | Whether the height can be adjusted | Yes, No |
| Height Adjustment Range | text (mm) | Range of height adjustment | 559-787, 584-762, 660-864 |
| Stackable | enum | Whether items can be stacked for storage | Yes, No |
| Stack Limit | number | Maximum number of units in a stack | 6, 8, 10, 12 |
| Foldable | enum | Whether the product folds flat for storage | Yes, No |
| Indoor/Outdoor | enum | Intended use environment | Indoor, Outdoor, Both |
| Grade Level | text | Recommended student age or grade range for school furniture | Preschool, K-2, 3-4, 5-Adult, Adult |
| Antimicrobial | enum | Whether surfaces have antimicrobial treatment | Yes, No |
| Casters/Glides | text | Type of floor contact points | Nylon Glides, Steel Glides, Felt Glides, Locking Casters, Non-Marking Casters |
| Ganging Capability | enum | Whether units can be linked or ganged together | Yes, No, Optional |
| Certifications | text (list) | Product safety and environmental certifications | BIFMA, GREENGUARD, GREENGUARD Gold, CPSIA, ANSI/AAMI, CE, FDA |
| Fire Rating | text | Fire resistance or flammability certification | CAL 117, CAL 133, BS 5852 |
| Assembly Required | enum | Whether assembly is needed | Yes, No, Minimal |
| Warranty Duration | text | Length of the manufacturer warranty | 10 Years, 5 Years, Limited Lifetime, 1 Year |
| Country of Origin | text | Country where the product is manufactured | USA, China, Canada, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus BIFMA/GREENGUARD standards | [Virco 9000 Series Chair](https://virco.com/product/9000-series-4-leg-stack-chair/), [Lancaster Table and Seating](https://www.lancastertableandseating.com/seating/), [Hillrom Healthcare Furniture](https://www.hillrom.com/en/products-category/healthcare-furniture/), [Medline Healthcare Furniture](https://www.medline.com/media/catalog/Docs/MKT/WP/Healthcare-Furniture-catalog.pdf) |
