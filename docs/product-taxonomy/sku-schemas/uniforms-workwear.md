# SKU Schema: Uniforms & Workwear

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | DC-WD2279LW, UF-4820, WR-288UT11 |
| Product Name | text | Full product name including brand, garment type, and key features | Dickies Hi-Vis Lightweight Cotton Coverall, UniFirst Industrial Work Shirt, Workrite Tecasafe Plus FR Coverall |
| URL | text | Direct link to the product page | https://example.com/product/coverall-12345 |
| Price | number | Numeric unit price excluding currency symbol | 29.99, 65.00, 189.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Dickies, Cintas, Carhartt, Workrite, Bulwark, Red Kap, UniFirst |
| Garment Type | enum | Classification of the workwear item | Shirt, Polo, T-Shirt, Pants, Jeans, Coverall, Overalls, Jacket, Vest, Lab Coat, Scrub Top, Scrub Pants, Shorts, Sweatshirt |
| Gender | enum | Target gender fit | Men, Women, Unisex |
| Size | text | Size designation in the sellers system | S, M, L, XL, 2XL, 3XL, 32x30, 36R, 6XL Tall |
| Size Range | text | Range of sizes available for the product | XS-6XL, S-3XL Tall, 28-60 waist |
| Fit Type | enum | Garment cut and silhouette | Regular, Relaxed, Slim, Classic, Athletic |
| Color | text | Garment color name | Black, Navy, Khaki, Grey, Royal Blue, Hi-Vis Yellow, Hi-Vis Orange |
| Fabric Composition | text | Fiber content with percentages | 65% Polyester / 35% Cotton, 100% Cotton, 88% Cotton / 12% Nylon |
| Fabric Weight | number (oz/yd2) | Weight of the garment fabric per square yard | 4.5, 7.0, 7.75, 11.0 |
| Fabric Type | text | Weave or knit construction of the fabric | Twill, Ripstop, Poplin, Denim, Pique knit, Jersey knit, Canvas |
| Closure Type | enum | Primary method of fastening the garment | Button front, Snap front, Zip front, Pull-over, Hook and loop |
| Number of Pockets | number | Total count of all pockets on the garment | 2, 4, 7, 9 |
| Pocket Types | text (list) | Types of pockets included | Chest, Side slash, Cargo, Tool, Rule, Cell phone, Pencil division |
| Flame Resistant | boolean | Whether the garment is inherently or treated flame resistant | true, false |
| FR Standard | text | Flame resistance certification standard met | NFPA 2112, ASTM F1506, EN ISO 11612 |
| Arc Rating | number (cal/cm2) | Arc thermal performance value for electrical arc flash protection | 4.4, 8.9, 12.4, 20.0, 40.0 |
| HRC Level | enum | Hazard Risk Category level per NFPA 70E | PPE 1, PPE 2, PPE 3, PPE 4 |
| Hi-Vis Class | enum | ANSI/ISEA 107 high-visibility classification | Not rated, Class 1, Class 2, Class 3 |
| Reflective Tape | boolean | Whether the garment has retroreflective striping | true, false |
| Moisture Management | boolean | Whether the fabric is treated for moisture wicking | true, false |
| Stain Release | boolean | Whether the fabric has a soil or stain release finish | true, false |
| Wrinkle Resistant | boolean | Whether the garment has a wrinkle-free or no-iron treatment | true, false |
| Industrial Laundry Safe | boolean | Whether the garment is rated for commercial or industrial laundering | true, false |
| Industry Application | text (list) | Primary industries or job roles the garment is designed for | Automotive, Healthcare, Hospitality, Construction, Electrical, Food Processing, Manufacturing |
| Care Instructions | text | Laundering and care method | Machine wash warm, Industrial laundry, Dry clean only |
| Country of Origin | text | Country where the garment was manufactured | Mexico, Honduras, USA, Bangladesh, Vietnam |
| Model Number | text | Manufacturer style or model number | WD2279LW, 574, DP1000, 288UT11 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus NFPA 2112, NFPA 70E, and ANSI/ISEA 107 safety standards | [Dickies B2B](https://b2b.dickies.com/), [Cintas](https://www.cintas.com/uniform-work-apparel/), [UniFirst](https://unifirst.com/uniforms-workwear/all-products/), [HiVis Supply FR Clothing](https://www.hivissupply.com/hivis-fr-clothing.html) |
