# SKU Schema: Safety Gloves & Hand Protection

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 11-840-9, MG-05-010, S13TAFGP-L |
| Product Name | text | Full product name including key specs such as type, material, and cut level | Ansell HyFlex 11-840 Nitrile-Coated General Purpose Glove, Mechanix Wear Original Tactical Glove, Showa 7066 Nitrile Chemical Resistant Glove |
| URL | text | Direct link to the product page | https://example.com/product/hyflex-11-840 |
| Price | number | Numeric unit price per pair or per dozen | 3.49, 12.99, 24.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the glove manufacturer | Ansell, Mechanix Wear, Showa, Honeywell, MCR Safety, PIP, Superior Glove, Magid, Ironclad, Uvex |
| Product Type | enum | Primary type of hand protection | Cut-Resistant Glove, Chemical-Resistant Glove, General Purpose Glove, Disposable Glove, Welding Glove, Impact-Resistant Glove, Electrical Insulating Glove, Heat-Resistant Glove, Arm Sleeve |
| Liner Material | text | Material of the inner knit or woven liner | Nylon, HPPE, Kevlar, Dyneema, Polyester, Cotton, Spandex, Glass Fiber, Tungsten, Nylon/Spandex Blend |
| Coating Material | text | Material applied to the palm or fingers for grip and protection | Nitrile, Foam Nitrile, Polyurethane (PU), Latex, PVC, Sandy Nitrile, Micro-Foam, None |
| Coating Coverage | enum | Extent of the coating applied to the glove | Palm Coated, Full Coated, 3/4 Coated, Fingertip Coated, Uncoated |
| Gauge | number | Knit gauge indicating liner density; higher gauge means finer knit | 10, 13, 15, 18, 21 |
| ANSI/ISEA Cut Level | text | Cut resistance rating per ANSI/ISEA 105 | A1, A2, A3, A4, A5, A6, A7, A8, A9 |
| EN 388 Cut Level | text | Cut resistance rating per EN 388:2016 (coupe test and ISO 13997 TDM test) | A, B, C, D, E, F |
| EN 388 Performance Levels | text | Full EN 388 classification for abrasion, cut, tear, puncture, and ISO cut | 4X42E, 3131A, 4544DP |
| Puncture Resistance | text | Puncture resistance level per ANSI/ISEA 105 or EN 388 | ANSI Level 3, EN Level 2 |
| Chemical Resistance | text (list) | Chemicals or chemical families the glove resists per EN 374 or ASTM | Type A (6+ chemicals), Type B (3+ chemicals), Acids, Solvents, Oils, Fuels |
| Chemical Permeation Times | text | Breakthrough times for specific chemicals per EN 374-1 | Level 6 (480 min), Level 4 (120 min) |
| Impact Protection | boolean | Whether the glove includes TPR or other dorsal impact guards | true, false |
| Touchscreen Compatible | boolean | Whether the glove allows capacitive touchscreen operation | true, false |
| Grip Pattern | text | Surface texture or pattern to improve grip | Smooth, Micro-Foam, Diamond, Sandy, Dotted, Textured Fingers |
| Glove Length | text | Total length from fingertip to cuff | 230 mm, 310 mm, 380 mm, 450 mm, 18 inch |
| Cuff Style | text | Type of wrist or forearm cuff | Knit Wrist, Safety Cuff, Extended Gauntlet, Elastic Cuff, Hook and Loop |
| Thickness | number (mm) | Material thickness of the glove, especially for disposable and chemical gloves | 0.05, 0.13, 0.38, 0.56 |
| Size | text | Glove size designation | XS (6), S (7), M (8), L (9), XL (10), 2XL (11), 3XL (12) |
| Thermal Rating | text | Heat or cold resistance classification | EN 407 (Contact Heat Level 1), EN 511 (X1X), ANSI Heat Level 3 |
| Maximum Temperature | number (C) | Maximum contact or radiant heat temperature the glove withstands | 100, 250, 350, 500 |
| Electrical Rating | text | Voltage class for electrical insulating gloves per ASTM D120 | Class 00 (500V), Class 0 (1000V), Class 2 (17000V), Class 4 (36000V) |
| Disposable | boolean | Whether the glove is intended for single use | true, false |
| Powder Free | boolean | Whether disposable gloves are free of donning powder | true, false |
| Latex Free | boolean | Whether the product is free of natural rubber latex | true, false |
| Color | text | Glove color | Black, Gray, Blue, Orange, Yellow, Hi-Viz Green, White |
| Pack Quantity | number | Number of pairs or individual gloves per pack | 1, 12, 100, 250 |
| Certifications | text (list) | Applicable safety standards met | ANSI/ISEA 105-2024, EN 388:2016+A1:2018, EN 374-1:2016, EN 407, EN 511, ASTM D120, AS/NZS 2161 |
| Country of Origin | text | Country where the glove is manufactured | Sri Lanka, Vietnam, Malaysia, China, Mexico, USA |
| Model Number | text | Manufacturer model or part number | 11-840, MG-05, 7066, N-DEX 8005 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (ANSI/ISEA 105, EN 388, EN 374, ASTM D120) | [Ansell HyFlex](https://www.ansell.com/us/en/industrial/protections/mechanical-protection), [Mechanix Wear](https://www.mechanix.com/), [Showa Gloves](https://www.showagroup.com/), [Tenaquip](https://www.tenaquip.com/) |
