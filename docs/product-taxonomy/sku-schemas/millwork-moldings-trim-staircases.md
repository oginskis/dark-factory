# SKU Schema: Millwork (Moldings, Trim, Staircases)

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber
**Taxonomy ID:** `wood.millwork`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | MFP620, MO-CAS-612, BLDR-WM327 |
| Product Name | text | Full product name including profile type, species, and dimensions | 1/2in x 4-1/4in x 16ft Primed MDF Baseboard, Poplar Colonial Casing 11/16 x 2-1/4 |
| URL | text | Direct link to the product page | https://example.com/product/primed-mdf-baseboard-4-25 |
| Price | number | Numeric price per linear foot or per piece excluding currency symbol | 1.81, 3.49, 12.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | enum | Primary millwork product type | Baseboard, Casing, Crown Molding, Chair Rail, Panel Mold, Handrail, Stair Tread, Stair Riser, Baluster, Newel Post, Door Stop, Shoe Molding, Window Sill, Plinth Block |
| Material | enum | Primary material the product is made from | Solid Wood, MDF, Finger-Joint Pine, PVC, Polyurethane, Polystyrene, HDF |
| Joint Type | text | How pieces connect at corners or ends | Miter, Cope, Butt, Scarf |
| Formaldehyde Compliance | text | Emission standard compliance for composite materials | CARB Phase 2, EPA TSCA Title VI, E1 |
| Country of Origin | text | Country where the product was manufactured | USA, Canada, Chile, China, Brazil |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Species | text | Wood species for solid wood products | Poplar, Oak, Maple, Cherry, Walnut, Mahogany, Pine, Cedar, Hemlock, Douglas Fir |
| Thickness | text (in) | Product thickness (depth from wall) | 1/2, 9/16, 11/16, 3/4, 1 |
| Width | text (in) | Product face width or height | 2-1/4, 3-1/2, 4-1/4, 5-1/4, 7-1/4 |
| Profile Pattern | text | Manufacturer profile number or pattern name | Colonial, Craftsman, Modern, M0620X, WM327, WM49, WM163 |
| Finish | enum | Surface finish state of the product | Primed, Unfinished, Stain-Grade, Paint-Grade, Pre-Finished, Raw |
| Edge Detail | text | Specific edge or face profile design | Ogee, Cove, Bead, Stepped, Flat, Beveled, Radius |
| Paintable | boolean | Whether the product is designed to accept paint | true, false |
| Stainable | boolean | Whether the product is designed to accept wood stain | true, false |
| Moisture Resistant | boolean | Whether the product is rated for moisture-prone areas | true, false |
| Interior/Exterior | enum | Intended installation environment | Interior, Exterior, Both |
| Architectural Style | text (list) | Design styles the profile complements | Colonial, Craftsman, Modern, Victorian, Transitional, Traditional |
| Installation Method | text (list) | Recommended attachment methods | Nail, Glue, Brad Nail, Screw, Snap-Fit |
| Fire Rating | text | Fire performance classification where applicable | Class A, Class 1, ASTM E84 Class A |
| Pack Quantity | number | Number of pieces per pack or bundle | 1, 6, 10, 20 |
| Certification | text (list) | Environmental and quality certifications | FSC, SFI, GreenGuard, PEFC |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 27 attributes from 4 companies plus industry standards (WM pattern numbering, ASTM E84, CARB Phase 2) | [Mouldings One](https://www.mouldingsone.com/shop-mouldings/), [Metrie](https://www.metrie.com/products/moulding), [Builders FirstSource](https://www.bldr.com/products/moulding-millwork), [Horner Millwork](https://hornermillwork.com/products/mouldings-and-millwork/) |
