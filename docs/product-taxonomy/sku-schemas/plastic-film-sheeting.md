# SKU Schema: Plastic Film & Sheeting

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.film_sheeting`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | IDL-1650-4C, USP-23655, VP-612PE |
| Product Name | text | Full product name including material, thickness, and dimensions | Clear 6 mil LDPE Sheeting 20 ft x 100 ft, Black HDPE Vapor Barrier 10 mil |
| URL | text | Direct link to the product page | https://example.com/product/ldpe-6mil-20x100 |
| Price | number | Numeric price per roll or per sheet, excluding currency symbol | 54.95, 189.00, 12.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Material | enum | Primary polymer type | LDPE, LLDPE, HDPE, PVC, PTFE, EVA, PP |
| Country of Origin | text | Manufacturing country | USA, China, Germany, Canada |
| Length | number (ft) | Roll or sheet length | 25, 50, 100, 200, 500 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Thickness | number (mil) | Film or sheet thickness in mils (thousandths of an inch) | 1, 2, 4, 6, 10, 20, 40 |
| Width | number (ft) | Roll or sheet width | 3, 8, 10, 12, 16, 20, 24, 36 |
| Area Coverage | number (sq ft) | Total surface area per roll or sheet | 150, 500, 1000, 2000 |
| Color/Clarity | text | Visual appearance of the film | Clear, Black, White, Translucent, Blue, Amber, Frosted |
| Density | number (g/cm3) | Material density | 0.91, 0.92, 0.95, 0.96 |
| Tensile Strength | number (psi) | Maximum stress before breaking | 850, 1400, 2200, 3500 |
| Elongation at Break | number (%) | Percentage stretch before failure | 100, 300, 500, 700 |
| Puncture Resistance | text | Resistance to tearing and puncture | Low, Medium, High |
| Temperature Range | text | Continuous service temperature range | -60 F to 150 F, -40 F to 180 F |
| UV Stabilized | enum | Whether UV inhibitors are added for outdoor use | Yes, No |
| Flame Retardant | enum | Whether flame-retardant additives are present | Yes, No |
| Fire Rating | text | Fire safety classification when flame retardant | NFPA 701 Test 1, ASTM E-84 Class A, FAR 25.853a |
| Moisture Vapor Transmission | number (perms) | Water vapor permeability rate | 0.01, 0.06, 0.5, 1.2 |
| Application | text (list) | Primary intended uses | Vapor Barrier, Construction Enclosure, Painting Protection, Greenhouse Cover, Packaging, Fumigation |
| Slip Treatment | enum | Whether the film has a slip-resistant or anti-static surface | Slip, Non-Slip, Anti-Static |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 28 attributes from 4 companies plus ASTM standards (D 4635, D 4801, D 882) | [IDL Packaging](https://idlpack.com/all-catalog/home-gardening/polyethylene-sheeting/), [U.S. Plastic Corp.](https://www.usplastic.com/catalog/item.aspx?itemid=23655), [Brentwood Plastics](https://brentwoodplastics.com/data-sheets), [Americover](https://www.americover.com/) |
