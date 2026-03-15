# SKU Schema: Printing & Writing Paper

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.printing_writing`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DOM-5462, UPM-FIN-OFC80, HP-CHP910 |
| Product Name | text | Full product name including grade, weight, and size | Domtar Husky Digital Opaque 60lb Text 8.5x11, UPM Office Copy A4 80gsm White |
| URL | text | Direct link to the product page | https://example.com/product/domtar-husky-60lb-text-8-5x11 |
| Price | number | Numeric price per ream, carton, or unit excluding currency symbol | 8.99, 42.50, 185.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Paper Grade | enum | General classification of the paper type | Bond, Offset, Text, Cover, Writing, Bristol, Vellum, Ledger |
| Coating Type | enum | Whether and how the paper surface is coated | Uncoated, Coated 1 Side (C1S), Coated 2 Sides (C2S), Film Coated |
| Country of Origin | text | Country where the paper was manufactured | USA, Finland, Germany, Canada, Brazil |
| Basis Weight | text (lb) | Weight in pounds per 500 sheets at the grade basic size | 20, 24, 50, 60, 70, 80, 100 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Coating Finish | enum | Surface finish for coated papers | Gloss, Matte, Dull, Satin, Silk |
| Grammage | number (gsm) | Weight in grams per square metre (ISO standard) | 75, 80, 90, 105, 120, 150, 216 |
| Caliper | number (pt) | Thickness per sheet in points (thousandths of an inch) | 3.2, 4.0, 4.8, 6.0, 8.5 |
| Brightness | number | GE brightness rating — percentage of blue light reflected from the surface | 84, 88, 92, 96, 100 |
| Whiteness | number | CIE whiteness value measuring overall white appearance | 145, 155, 163, 170 |
| Opacity | number (%) | Percentage of light blocked, indicating show-through resistance | 87, 90, 94, 97 |
| Smoothness | number (Sheffield) | Surface smoothness measured in Sheffield units (lower is smoother) | 50, 100, 150, 200, 250 |
| Color | text | Paper color or shade | White, Bright White, Natural, Cream, Ivory, Pastel Blue, Canary |
| Paper Shade | text | Undertone of the white paper | Blue-White, Warm White, Balanced White, True White |
| Fiber Content | text | Source and type of fiber in the paper | Virgin Wood Pulp, 30% PCR, 100% Recycled, Cotton, Mixed |
| Recycled Content | number (%) | Percentage of post-consumer recycled fiber | 0, 10, 30, 50, 100 |
| Printing Method Compatibility | text (list) | Printing processes the paper is designed for | Offset, Digital Toner, Inkjet, Letterpress, Flexography |
| Sheets per Ream | number | Number of sheets in one ream | 250, 500 |
| Reams per Carton | number | Number of reams in a shipping carton | 5, 8, 10 |
| Grain Direction | enum | Direction of paper fibers relative to sheet dimensions | Long Grain, Short Grain |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISO 536, ISO 2470, TAPPI brightness, GE brightness) | [Domtar](https://www.domtar.com/en/resources/paper-information/spec-sheets-and-stocking-information), [UPM Paper](https://www.upmpaper.com/products/paper-catalogue/), [WCP Solutions](https://www.wcpsolutions.com/printing-paper/), [Sappi](https://www.sappi.com/en-us/products-services/products/galerie) |
