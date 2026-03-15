# SKU Schema: Tissue & Hygiene Paper

**Last updated:** 2026-03-15
**Parent category:** Paper, Pulp & Printed Products
**Taxonomy ID:** `paper.tissue_hygiene`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | B012, 48280, T320, KC-13135 |
| Product Name | text | Full product name including brand, type, ply, and sheet count | Cascades PRO Select Standard Bath Tissue 1-Ply 1000 Sheets, Scott Hygienic High Capacity Folded Tissue 2-Ply 250 Sheets |
| URL | text | Direct link to the product page | https://example.com/product/cascades-b012-standard-1ply-1000 |
| Price | number | Numeric price per case or per unit excluding currency symbol | 45.99, 72.50, 3.25 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary tissue product category | Bath Tissue, Facial Tissue, Paper Towel, Napkin, Hand Towel, Wiper, Kitchen Roll |
| Dispenser Format | enum | Form factor for dispensing or use | Standard Roll, Jumbo Roll, Coreless Roll, Folded, Flat Box, Pop-Up, Center-Pull |
| Country of Origin | text | Country where the product was manufactured | USA, Canada, Mexico, Italy |
| Ply Count | number | Number of tissue layers bonded together | 1, 2, 3 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Sheets per Roll/Pack | number | Number of individual sheets per roll or per folded pack | 250, 400, 500, 700, 950, 1000, 1210 |
| Rolls/Packs per Case | number | Number of rolls or packs in a shipping case | 6, 12, 24, 36, 48, 80, 96 |
| Sheet Width | number (in) | Width of an individual sheet | 3.25, 4.0, 4.25, 7.8, 8.0, 10.0 |
| Color | enum | Color of the tissue product | White, Natural, Ivory, Latte |
| Embossed | boolean | Whether the tissue has an embossed surface pattern | true, false |
| Fiber Content | text | Source fiber composition | 100% Recycled, 100% Virgin, 40% Recycled/60% Virgin, Bamboo |
| Recycled Content | number (%) | Percentage of post-consumer recycled fiber | 0, 20, 40, 80, 100 |
| Bleaching Process | text | Method used to whiten the fiber | TCF (Totally Chlorine Free), ECF (Elemental Chlorine Free), Unbleached |
| Softness Rating | text | Manufacturer softness classification | Standard, Premium, Ultra Soft |
| Absorbency | text | Relative absorbency level of the product | Standard, High, Maximum |
| Wet Strength | boolean | Whether the product retains strength when wet | true, false |
| Septic Safe | boolean | Whether the product is safe for septic systems | true, false |
| Certification | text (list) | Environmental and quality certifications | Green Seal, UL ECOLOGO, FSC, EPA CPG, Nordic Swan, EU Ecolabel |
| Case Dimensions | text (in) | Shipping case length x width x height | 13x17.25x16.5, 11.8x11.8x22.4 |
| UPC Code | text | Universal Product Code for retail scanning | 067220610129, 036000482805 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (EPA CPG, Green Seal GS-1, UL ECOLOGO UL 175) | [Cascades PRO](https://www.pro.cascades.com/products/b012-standard-toilet-paper-1-ply-1000-sheets/), [Kimberly-Clark Professional](https://www.kcprofessional.com/en-us/products/restroom-and-hygiene/toilet-paper-and-seat-covers), [Marcal Paper](https://www.marcalpaper.com/), [Essity/Tork](https://www.torkusa.com/) |
