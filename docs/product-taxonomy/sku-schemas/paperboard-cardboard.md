# SKU Schema: Paperboard & Cardboard

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | SW-CAND-016, GPI-EVR-018, CWP-NuVo-012 |
| Product Name | text | Full product name including board type, caliper, and coating | Candesce SBS C1S 16pt, PaceSetter CRB Double Coated 18pt, Coated Natural Kraft P1S 22pt |
| URL | text | Direct link to the product page | https://example.com/product/candesce-sbs-c1s-16pt |
| Price | number | Numeric price per ton, per MSI (thousand square inches), or per sheet excluding currency symbol | 1250.00, 14.50, 0.085 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Brand/Manufacturer | text | Paperboard manufacturer or brand name | Smurfit Westrock, Graphic Packaging, Clearwater Paper, Sappi, Holmen |
| Board Type | enum | Primary paperboard classification | SBS (Solid Bleached Sulfate), CRB (Coated Recycled Board), CUK (Coated Unbleached Kraft), URB (Uncoated Recycled Board), FBB (Folding Box Board), CNK (Coated Natural Kraft), UUK (Uncoated Unbleached Kraft) |
| Caliper | number (pt) | Board thickness measured in points (thousandths of an inch) | 10, 12, 14, 16, 18, 20, 22, 24 |
| Basis Weight | number (lb) | Weight in pounds per 3000 square feet (paperboard basis) | 140, 170, 200, 230, 260, 310 |
| Grammage | number (gsm) | Weight in grams per square metre | 200, 250, 300, 350, 400, 500 |
| Brightness | number (%) | GE or ISO brightness of the top surface | 82, 86, 88, 90, 93 |
| Coating Configuration | enum | Which sides are clay-coated | C1S (Coated One Side), C2S (Coated Two Sides), Uncoated |
| Coating Weight | text (lb/ream) | Amount of coating applied to each side | 8/0, 10/6, 12/8 |
| Surface Finish | enum | Visual and tactile quality of the coated surface | Gloss, Matte, Satin, Cast Coated, High Gloss |
| Stiffness MD | number (Taber) | Stiffness in the machine direction measured by Taber test | 20, 40, 60, 90, 130 |
| Stiffness CD | number (Taber) | Stiffness in the cross direction measured by Taber test | 12, 22, 35, 50, 70 |
| Ply Count | number | Number of fiber plies in the board construction | 1, 2, 3, 4, 5 |
| Fiber Source | text | Type of fiber furnish used | Virgin Bleached Hardwood, Virgin Bleached Softwood, 100% Recycled, Mixed Recycled, Unbleached Kraft |
| Recycled Content | number (%) | Percentage of post-consumer recycled fiber | 0, 30, 35, 50, 100 |
| Barrier Coating | text | Functional barrier coatings applied to the board | LDPE, PLA, Water-Based, None |
| Food Contact Safe | boolean | Whether the board is FDA-compliant for direct food contact | true, false |
| Printability | text | Print method compatibility and ink holdout characteristics | Excellent offset, Good flexo, Digital compatible |
| Sheet Size | text (in) | Standard sheet dimensions offered | 26x40, 28x44, 25.5x38, Custom |
| Roll Width | number (in) | Width of the board when supplied in rolls | 24, 36, 48, 60 |
| Scoring and Folding | text | Performance in creasing and folding operations | Clean fold with no cracking, Excellent score-to-fold |
| Gluability | text | Adhesive compatibility for converting operations | Compatible with hot melt, cold glue, and PVA |
| Certification | text (list) | Environmental and chain-of-custody certifications | FSC, SFI, PEFC, Green Seal, How2Recycle |
| FDA Compliance | text | Specific FDA regulation the board complies with for food contact | FDA 21 CFR 176.170, FDA 21 CFR 176.180 |
| End Use Application | text (list) | Primary packaging applications | Folding Carton, Cupstock, Plate Stock, Blister Card, Beverage Carrier, Pharmaceutical, Cosmetic |
| Country of Origin | text | Country where the paperboard was manufactured | USA, Canada, Finland, Sweden, Germany |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (TAPPI T411, ISO 536, FDA 21 CFR 176) | [Smurfit Westrock](https://www.smurfitwestrock.com/products/paper-and-board/paperboard), [Graphic Packaging](https://www.graphicpkg.com/packaging-materials/paperboard/), [Clearwater Paper](https://www.clearwaterpaper.com/paperboard-products/default.aspx), [Sappi](https://casepaper.com/product/sappi/) |
