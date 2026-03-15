# SKU Schema: Fine Jewelry (Gold, Silver, Gemstone)

**Last updated:** 2026-03-15
**Parent category:** Jewelry, Watches & Accessories
**Taxonomy ID:** `jewelry.fine_jewelry`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | BN-15979451, JA-W2R6D8, TF-60957430 |
| Product Name | text | Full product name including metal type, stone details, and style | Riviera Pave Diamond Eternity Ring in Platinum, 18K Gold Sapphire Pendant Necklace |
| URL | text | Direct link to the product page | https://example.com/product/diamond-eternity-ring |
| Price | number | Numeric retail price excluding currency symbol | 2450.00, 599.99, 18500.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, CAD |
| Jewelry Type | enum | Primary product category | Ring, Necklace, Earrings, Bracelet, Brooch, Pendant, Anklet |
| Metal Type | text | Primary metal or alloy used in the setting | Platinum, 14K White Gold, 18K Yellow Gold, 18K Rose Gold, Sterling Silver, Palladium |
| Primary Stone Type | text | Main gemstone species or variety | Diamond, Sapphire, Ruby, Emerald, Tanzanite, Opal, Amethyst |
| Diamond Cut Grade | enum | Cut quality grading for diamonds per GIA or equivalent scale | Ideal, Excellent, Very Good, Good, Fair |
| Diamond Color Grade | text | Color grading for diamonds (GIA D-Z scale or fancy color name) | D, E, F, G, Fancy Vivid Yellow, Fancy Pink |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Diamond Clarity Grade | enum | Clarity grading for diamonds per GIA scale | FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1 |
| Setting Type | text | Method used to secure stones in the mounting | Prong, Bezel, Channel, Pave, Tension, Flush, Halo, Cluster |
| Clasp Type | text | Type of closure mechanism | Lobster Claw, Spring Ring, Box Clasp, Toggle, Push-Back, Screw-Back, Lever-Back |
| Country of Origin | text | Country where the piece was manufactured or assembled | USA, Italy, France, Thailand, India |
| Polish Grade | enum | Surface finish quality of the diamond | Excellent, Very Good, Good, Fair |
| Symmetry Grade | enum | Symmetry grading of the diamond facets | Excellent, Very Good, Good, Fair |
| Metal Purity | text | Fineness or karat designation of the metal | 750 (18K), 585 (14K), 950 (Platinum), 925 (Sterling Silver) |
| Stone Origin | enum | Whether the stone is natural or laboratory-created | Natural, Lab-Created |
| Center Stone Carat | number (ct) | Carat weight of the center or primary stone | 0.75, 1.00, 2.50 |
| Stone Shape | text | Cut shape of the primary gemstone | Round Brilliant, Princess, Cushion, Oval, Emerald, Pear, Marquise, Asscher, Radiant, Heart |
| Stone Dimensions | text (mm) | Length x width x depth measurements of the primary stone | 6.19 x 6.23 x 3.97, 8.02 x 6.01 x 4.15 |
| Number of Stones | number | Total count of all stones in the piece | 1, 11, 36, 72 |
| Certification Lab | text | Independent grading laboratory that certified the primary stone | GIA, AGS, IGI, HRD, GCAL |
| Certificate Number | text | Report or certificate number from the grading laboratory | 2225391422, 14203857 |
| Hallmark | text | Official assay or purity mark stamped on the piece | 750, 585, 925, PT950, AU750 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus GIA grading standards and industry classification systems | [Blue Nile](https://www.bluenile.com/diamond-jewelry), [James Allen](https://www.jamesallen.com/fine-jewelry/), [Tiffany and Co.](https://www.tiffany.com/jewelry/), [Kay Jewelers](https://www.kay.com/) |
