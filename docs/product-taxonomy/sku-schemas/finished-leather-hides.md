# SKU Schema: Finished Leather & Hides

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather
**Taxonomy ID:** `textiles.finished_leather_hides`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | HO-SB-BLK-910, BG-VEG-NAT-45, UL-UPH-BRN |
| Product Name | product_name | text | — | Full product name including key specs such as animal type, tanning method, finish, and thickness | Hermann Oak Single Bend Vegetable Tan 9-10 oz Black, Italian Full Grain Aniline Lambskin 0.8mm Brown |
| URL | url | text | — | Direct link to the product page | https://example.com/product/veg-tan-single-bend-9-10oz |
| Price | price | number | — | Numeric price per selling unit (per hide, per square foot, per side), excluding currency symbol | 12.50, 185.00, 349.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP |
| Animal Type | animal_type | enum | — | Species of animal the hide originates from | Cowhide, Calfskin, Buffalo, Goatskin, Lambskin, Sheepskin, Pigskin, Deerskin, Kangaroo, Horsehide |
| Exotic Type | exotic_type | text | — | Exotic species for specialty hides, if applicable | Crocodile, Alligator, Ostrich, Python, Stingray, Lizard |
| Grain Type | grain_type | enum | — | Layer of the hide and degree of surface preservation | Full Grain, Top Grain, Corrected Grain, Split, Bonded |
| Finish Type | finish_type | text | — | Surface treatment applied to the finished leather | Aniline, Semi-Aniline, Pigmented, Nubuck, Suede, Patent, Pull-Up, Distressed, Metallic, Embossed, Brushoff |
| Cut Type | cut_type | enum | — | Section of the hide being sold | Full Hide, Side, Double Shoulder, Double Butt, Single Bend, Belly, Panel, Skirting |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Grade | grade | text | — | Quality grade assigned by the tannery based on blemishes and uniformity | A / #1, B / #2, C / #3, D / #4, Branded, Job Lot |
| Country of Origin | country_of_origin | text | — | Country where the hide was tanned and finished | USA, Italy, England, Mexico, Argentina, India |
| Brand/Tannery | brandtannery | text | — | Tannery or brand name that produced the leather | Hermann Oak, Horween, Wickett & Craig, Sedgwick, Conceria Walpier |
| Tanning Method | tanning_method | enum | — | Primary chemical or natural process used to convert raw hides into finished leather | Vegetable Tanned, Chrome Tanned, Combination Tanned, Brain Tanned, Alum Tanned |
| Embossing Pattern | embossing_pattern | text | — | Decorative pattern pressed into the leather surface, if applicable | Crocodile, Ostrich, Lizard, Pebble, Saffiano, Smooth |
| Thickness | thickness | text | oz | Leather thickness measured in ounces (1 oz equals approximately 0.4mm). May be expressed as a range | 2-3, 4-5, 8-9, 9-10 |
| Thickness Metric | thickness_metric | number | mm | Leather thickness in millimetres | 0.8, 1.2, 2.0, 3.6, 4.0 |
| Temper | temper | enum | — | Firmness or flexibility of the finished leather | Soft, Semi-Soft, Medium, Firm, Hard |
| Color | color | text | — | Primary color of the finished leather | Natural, Black, Brown, Burgundy, Tan, Russet, Navy, Red, White, Grey |
| Dyeing Method | dyeing_method | enum | — | How the color was applied to the leather | Drum Dyed, Struck-Through, Surface Dyed, Spray Dyed, Undyed |
| Application | application | text (list) | — | Primary intended uses for the leather | Belts, Saddlery, Upholstery, Garments, Bags, Footwear, Bookbinding, Tooling, Holsters |
| Tooling Suitability | tooling_suitability | boolean | — | Whether the leather accepts carving and stamping for decorative work | true, false |
| Certification | certification | text (list) | — | Environmental or quality certifications | Leather Working Group (LWG), ISO 14001, REACH Compliant, Chrome-Free |
| Minimum Order Quantity | minimum_order_quantity | number | — | Minimum number of units or area required for purchase | 1, 5, 25 |
| Selling Unit | selling_unit | enum | — | How the leather is sold | Per Hide, Per Square Foot, Per Side, Per Piece |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus industry standards (leather grading, tanning methods, ISO leather testing) | [Buckleguy](https://www.buckleguy.com/leather-hides-skins/), [Hermann Oak](https://www.hermannoakleather.com/pages/leather-grading-guide), [BuyLeatherOnline](https://buyleatheronline.com/en/content/19-leather-wholesale), [Leather Unlimited](https://leatherunltd.com/) |
