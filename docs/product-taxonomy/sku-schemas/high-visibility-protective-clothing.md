# SKU Schema: High-Visibility & Protective Clothing

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | US466-HVY-BLK-L, 25023, ERG-8384 |
| Product Name | text | Full product name including key specs such as garment type, class, and color | Portwest US466 ANSI Class 3 Hi-Vis Contrast Traffic Jacket Yellow/Black, Ergodyne GloWear 8310HL Class 3 Economy Vest Lime |
| URL | text | Direct link to the product page | https://example.com/product/portwest-us466-hivis-jacket |
| Price | number | Numeric unit price excluding currency symbol | 9.99, 34.95, 89.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the hi-vis clothing manufacturer | Portwest, Ergodyne, Tingley, ML Kishigo, PIP, Radians, Occunomix, Pyramex |
| Garment Type | enum | Primary type of hi-vis garment | Vest, Jacket, Coat, Shirt, T-Shirt, Sweatshirt, Hoodie, Pants, Coverall, Bib Overalls, Rain Jacket, Bomber Jacket |
| ANSI/ISEA Type | enum | Garment type classification per ANSI/ISEA 107-2020 | Type O (Off-Road), Type R (Roadway), Type P (Public Safety) |
| ANSI/ISEA Class | enum | Minimum visibility performance class per ANSI/ISEA 107-2020 | Class 1, Class 2, Class 3 |
| EN ISO 20471 Class | enum | European high-visibility classification | Class 1, Class 2, Class 3 |
| Background Material Color | enum | Fluorescent base fabric color | Fluorescent Yellow-Green, Fluorescent Orange-Red, Fluorescent Red |
| Reflective Tape Color | text | Color of the retroreflective striping | Silver, Prismatic Silver, Segmented Silver, Yellow |
| Reflective Tape Width | text | Width of the retroreflective bands | 2 inch, 50 mm, 1 inch |
| Reflective Tape Configuration | text | Placement pattern of reflective bands on the garment | 360-Degree, Two Horizontal/Two Vertical, X-Back, Two Horizontal |
| Shell Material | text | Primary fabric of the garment outer shell | 100% Polyester, Polyester/Cotton Blend, 300D Oxford Polyester, Nylon, Modacrylic |
| Material Weight | text | Fabric weight or density | 150 gsm, 5.5 oz, 300D |
| Lining Material | text | Inner lining or insulation material if applicable | Polyester Fleece, Quilted Polyester, Mesh, None |
| Waterproof/Water Resistant | text | Water protection level of the garment | Waterproof (Sealed Seams), Water Resistant, PU Coated, None |
| Breathability | text | Moisture vapor transmission or mesh ventilation features | Mesh Back Panel, Moisture Wicking, Ventilated, Sealed |
| Closure Type | text | Primary garment closure mechanism | Full Zipper, Hook and Loop, Snaps, Elastic, Open Front |
| Pockets | text | Number and type of pockets | 2 Front, 1 Chest, 1 Inside, 2 Cargo, 4 Total |
| Flame Resistance | text | Fire-resistant treatment or inherent flame resistance | FR Treated, NFPA 2112, NFPA 70E CAT 2, HRC 2, None |
| Arc Rating | text | Arc thermal performance value for electrical hazard protection | 8.8 cal/sq cm, 12 cal/sq cm, None |
| Size Range | text | Available garment sizes | S-5XL, M-7XL, Universal |
| Size | text | Specific size of the garment | Small, Medium, Large, XL, 2XL, 3XL, 4XL, 5XL |
| Fit | enum | Garment fit style | Regular, Tall, Extended, Unisex |
| Contrast Bottom | boolean | Whether the garment has a dark-colored lower section to hide dirt | true, false |
| Hood | enum | Hood inclusion and type | Attached, Detachable, Stow-Away, None |
| Weight | number (g) | Total weight of the garment | 150, 340, 680, 950 |
| Certifications | text (list) | Applicable safety and visibility standards met | ANSI/ISEA 107-2020, EN ISO 20471:2013, CSA Z96-15, AS/NZS 4602.1 |
| Country of Origin | text | Country where the garment is manufactured | Bangladesh, China, Vietnam, India, USA |
| Model Number | text | Manufacturer model or part number | US466, 8310HL, 25023, V1025 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI/ISEA 107-2020, EN ISO 20471, CSA Z96) | [HiVis Supply](https://www.hivissupply.com/hivis-safety-clothing.html), [Portwest](https://www.portwest.com/), [Ergodyne](https://www.ergodyne.com/blog/understanding-hi-vis-standards-ansi-isea-107), [PIP Global](https://us.pipglobal.com/en/products/hi-vis-apparel-experts/) |
