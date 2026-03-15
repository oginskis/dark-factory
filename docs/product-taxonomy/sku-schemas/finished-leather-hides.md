# SKU Schema: Finished Leather & Hides

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HO-SB-BLK-910, BG-VEG-NAT-45, UL-UPH-BRN |
| Product Name | text | Full product name including key specs such as animal type, tanning method, finish, and thickness | Hermann Oak Single Bend Vegetable Tan 9-10 oz Black, Italian Full Grain Aniline Lambskin 0.8mm Brown |
| URL | text | Direct link to the product page | https://example.com/product/veg-tan-single-bend-9-10oz |
| Price | number | Numeric price per selling unit (per hide, per square foot, per side), excluding currency symbol | 12.50, 185.00, 349.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP |
| Brand/Tannery | text | Tannery or brand name that produced the leather | Hermann Oak, Horween, Wickett & Craig, Sedgwick, Conceria Walpier |
| Animal Type | enum | Species of animal the hide originates from | Cowhide, Calfskin, Buffalo, Goatskin, Lambskin, Sheepskin, Pigskin, Deerskin, Kangaroo, Horsehide |
| Exotic Type | text | Exotic species for specialty hides, if applicable | Crocodile, Alligator, Ostrich, Python, Stingray, Lizard |
| Tanning Method | enum | Primary chemical or natural process used to convert raw hides into finished leather | Vegetable Tanned, Chrome Tanned, Combination Tanned, Brain Tanned, Alum Tanned |
| Grain Type | enum | Layer of the hide and degree of surface preservation | Full Grain, Top Grain, Corrected Grain, Split, Bonded |
| Finish Type | text | Surface treatment applied to the finished leather | Aniline, Semi-Aniline, Pigmented, Nubuck, Suede, Patent, Pull-Up, Distressed, Metallic, Embossed, Brushoff |
| Embossing Pattern | text | Decorative pattern pressed into the leather surface, if applicable | Crocodile, Ostrich, Lizard, Pebble, Saffiano, Smooth |
| Thickness | text (oz) | Leather thickness measured in ounces (1 oz equals approximately 0.4mm). May be expressed as a range | 2-3, 4-5, 8-9, 9-10 |
| Thickness Metric | number (mm) | Leather thickness in millimetres | 0.8, 1.2, 2.0, 3.6, 4.0 |
| Temper | enum | Firmness or flexibility of the finished leather | Soft, Semi-Soft, Medium, Firm, Hard |
| Hide Size | number (sq ft) | Total usable area of the hide or cut piece measured in square feet | 2, 8, 20, 45, 55 |
| Cut Type | enum | Section of the hide being sold | Full Hide, Side, Double Shoulder, Double Butt, Single Bend, Belly, Panel, Skirting |
| Color | text | Primary color of the finished leather | Natural, Black, Brown, Burgundy, Tan, Russet, Navy, Red, White, Grey |
| Dyeing Method | enum | How the color was applied to the leather | Drum Dyed, Struck-Through, Surface Dyed, Spray Dyed, Undyed |
| Grade | text | Quality grade assigned by the tannery based on blemishes and uniformity | A / #1, B / #2, C / #3, D / #4, Branded, Job Lot |
| Application | text (list) | Primary intended uses for the leather | Belts, Saddlery, Upholstery, Garments, Bags, Footwear, Bookbinding, Tooling, Holsters |
| Tooling Suitability | boolean | Whether the leather accepts carving and stamping for decorative work | true, false |
| Country of Origin | text | Country where the hide was tanned and finished | USA, Italy, England, Mexico, Argentina, India |
| Certification | text (list) | Environmental or quality certifications | Leather Working Group (LWG), ISO 14001, REACH Compliant, Chrome-Free |
| Minimum Order Quantity | number | Minimum number of units or area required for purchase | 1, 5, 25 |
| Selling Unit | enum | How the leather is sold | Per Hide, Per Square Foot, Per Side, Per Piece |
| Weight per Area | number (g/sq ft) | Weight of leather per square foot, relevant to garment and bag applications | 56, 85, 140, 200 |
| Specific Gravity | number | Density of the leather relative to water | 0.70, 0.86, 1.05 |
| Tear Strength | number (N) | Resistance to tearing under tension, measured per relevant ISO or ASTM standard | 20, 45, 80 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (leather grading, tanning methods, ISO leather testing) | [Buckleguy](https://www.buckleguy.com/leather-hides-skins/), [Hermann Oak](https://www.hermannoakleather.com/pages/leather-grading-guide), [BuyLeatherOnline](https://buyleatheronline.com/en/content/19-leather-wholesale), [Leather Unlimited](https://leatherunltd.com/) |
