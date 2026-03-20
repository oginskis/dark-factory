# SKU Schema: Paperboard & Cardboard

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.paperboard_cardboard`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer or distributor product identifier | SW-CAND-016, GPI-EVR-018, CWP-NuVo-012 |
| Product Name | product_name | text | — | yes | Full product name including board type, caliper, and coating | Candesce SBS C1S 16pt, PaceSetter CRB Double Coated 18pt, Coated Natural Kraft P1S 22pt |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/candesce-sbs-c1s-16pt |
| Price | price | number | — | yes | Numeric price per ton, per MSI (thousand square inches), or per sheet excluding currency symbol | 1250.00, 14.50, 0.085 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Board Type | board_type | enum | — | — | Primary paperboard classification | SBS (Solid Bleached Sulfate), CRB (Coated Recycled Board), CUK (Coated Unbleached Kraft), URB (Uncoated Recycled Board), FBB (Folding Box Board), CNK (Coated Natural Kraft), UUK (Uncoated Unbleached Kraft) |
| Country of Origin | country_of_origin | text | — | — | Country where the paperboard was manufactured | USA, Canada, Finland, Sweden, Germany |
| Basis Weight | basis_weight | number | lb | — | Weight in pounds per 3000 square feet (paperboard basis) | 140, 170, 200, 230, 260, 310 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Caliper | caliper | number | pt | — | Board thickness measured in points (thousandths of an inch) | 10, 12, 14, 16, 18, 20, 22, 24 |
| Grammage | grammage | number | gsm | — | Weight in grams per square metre | 200, 250, 300, 350, 400, 500 |
| Brightness | brightness | number | % | — | GE or ISO brightness of the top surface | 82, 86, 88, 90, 93 |
| Coating Configuration | coating_configuration | enum | — | — | Which sides are clay-coated | C1S (Coated One Side), C2S (Coated Two Sides), Uncoated |
| Surface Finish | surface_finish | enum | — | — | Visual and tactile quality of the coated surface | Gloss, Matte, Satin, Cast Coated, High Gloss |
| Stiffness MD | stiffness_md | number | Taber | — | Stiffness in the machine direction measured by Taber test | 20, 40, 60, 90, 130 |
| Stiffness CD | stiffness_cd | number | Taber | — | Stiffness in the cross direction measured by Taber test | 12, 22, 35, 50, 70 |
| Fiber Source | fiber_source | text | — | — | Type of fiber furnish used | Virgin Bleached Hardwood, Virgin Bleached Softwood, 100% Recycled, Mixed Recycled, Unbleached Kraft |
| Recycled Content | recycled_content | number | % | — | Percentage of post-consumer recycled fiber | 0, 30, 35, 50, 100 |
| Barrier Coating | barrier_coating | text | — | — | Functional barrier coatings applied to the board | LDPE, PLA, Water-Based, None |
| Food Contact Safe | food_contact_safe | boolean | — | — | Whether the board is FDA-compliant for direct food contact | true, false |
| Printability | printability | text | — | — | Print method compatibility and ink holdout characteristics | Excellent offset, Good flexo, Digital compatible |
| Roll Width | roll_width | number | in | — | Width of the board when supplied in rolls | 24, 36, 48, 60 |
| Scoring and Folding | scoring_and_folding | text | — | — | Performance in creasing and folding operations | Clean fold with no cracking, Excellent score-to-fold |
| Gluability | gluability | text | — | — | Adhesive compatibility for converting operations | Compatible with hot melt, cold glue, and PVA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (TAPPI T411, ISO 536, FDA 21 CFR 176) | [Smurfit Westrock](https://www.smurfitwestrock.com/products/paper-and-board/paperboard), [Graphic Packaging](https://www.graphicpkg.com/packaging-materials/paperboard/), [Clearwater Paper](https://www.clearwaterpaper.com/paperboard-products/default.aspx), [Sappi](https://casepaper.com/product/sappi/) |
