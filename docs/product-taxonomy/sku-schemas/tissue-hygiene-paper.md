# SKU Schema: Tissue & Hygiene Paper

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.tissue_hygiene`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | B012, 48280, T320, KC-13135 |
| Product Name | product_name | text | — | Full product name including brand, type, ply, and sheet count | Cascades PRO Select Standard Bath Tissue 1-Ply 1000 Sheets, Scott Hygienic High Capacity Folded Tissue 2-Ply 250 Sheets |
| URL | url | text | — | Direct link to the product page | https://example.com/product/cascades-b012-standard-1ply-1000 |
| Price | price | number | — | Numeric price per case or per unit excluding currency symbol | 45.99, 72.50, 3.25 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary tissue product category | Bath Tissue, Facial Tissue, Paper Towel, Napkin, Hand Towel, Wiper, Kitchen Roll |
| Dispenser Format | dispenser_format | enum | — | Form factor for dispensing or use | Standard Roll, Jumbo Roll, Coreless Roll, Folded, Flat Box, Pop-Up, Center-Pull |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, Canada, Mexico, Italy |
| Ply Count | ply_count | number | — | Number of tissue layers bonded together | 1, 2, 3 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Sheets per Roll/Pack | sheets_per_rollpack | number | — | Number of individual sheets per roll or per folded pack | 250, 400, 500, 700, 950, 1000, 1210 |
| Rolls/Packs per Case | rollspacks_per_case | number | — | Number of rolls or packs in a shipping case | 6, 12, 24, 36, 48, 80, 96 |
| Sheet Width | sheet_width | number | in | Width of an individual sheet | 3.25, 4.0, 4.25, 7.8, 8.0, 10.0 |
| Color | color | enum | — | Color of the tissue product | White, Natural, Ivory, Latte |
| Embossed | embossed | boolean | — | Whether the tissue has an embossed surface pattern | true, false |
| Fiber Content | fiber_content | text | — | Source fiber composition | 100% Recycled, 100% Virgin, 40% Recycled/60% Virgin, Bamboo |
| Recycled Content | recycled_content | number | % | Percentage of post-consumer recycled fiber | 0, 20, 40, 80, 100 |
| Bleaching Process | bleaching_process | text | — | Method used to whiten the fiber | TCF (Totally Chlorine Free), ECF (Elemental Chlorine Free), Unbleached |
| Softness Rating | softness_rating | text | — | Manufacturer softness classification | Standard, Premium, Ultra Soft |
| Absorbency | absorbency | text | — | Relative absorbency level of the product | Standard, High, Maximum |
| Wet Strength | wet_strength | boolean | — | Whether the product retains strength when wet | true, false |
| Septic Safe | septic_safe | boolean | — | Whether the product is safe for septic systems | true, false |
| Certification | certification | text (list) | — | Environmental and quality certifications | Green Seal, UL ECOLOGO, FSC, EPA CPG, Nordic Swan, EU Ecolabel |
| Case Dimensions | case_dimensions | text | in | Shipping case length x width x height | 13x17.25x16.5, 11.8x11.8x22.4 |
| UPC Code | upc_code | text | — | Universal Product Code for retail scanning | 067220610129, 036000482805 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (EPA CPG, Green Seal GS-1, UL ECOLOGO UL 175) | [Cascades PRO](https://www.pro.cascades.com/products/b012-standard-toilet-paper-1-ply-1000-sheets/), [Kimberly-Clark Professional](https://www.kcprofessional.com/en-us/products/restroom-and-hygiene/toilet-paper-and-seat-covers), [Marcal Paper](https://www.marcalpaper.com/), [Essity/Tork](https://www.torkusa.com/) |
