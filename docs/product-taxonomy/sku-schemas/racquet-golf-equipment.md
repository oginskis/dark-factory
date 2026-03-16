# SKU Schema: Racquet & Golf Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.racquet_golf`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | WIL-WR079411U, CAL-PRDX-AI, YON-EZONE100, TM-M6D |
| Product Name | product_name | text | — | Full product name including brand, model, and key specs | Wilson Blade 98 v9 18x20, Callaway Paradym Ai Smoke Driver 10.5 Stiff, Yonex EZONE 100 |
| URL | url | text | — | Direct link to the product page | https://example.com/product/blade-98-v9 |
| Price | price | number | — | Numeric retail price excluding currency symbol | 129.00, 249.99, 549.99, 599.99 |
| Currency | currency | text | — | ISO 4217 currency code | USD, GBP, EUR, JPY, CAD |
| Equipment Type | equipment_type | text | — | Specific product category | Racquet, Driver, Fairway Wood, Hybrid, Iron Set, Wedge, Putter, Golf Ball, Golf Bag, Paddle, Grip, String |
| Composition | composition | text | — | Primary frame construction material | Graphite, Carbon Fiber, Graphene, Kevlar/Carbon, Fiberglass, Boron/Graphite |
| Shaft Material | shaft_material | enum | — | Material of the golf club shaft | Graphite, Steel, Multi-Material |
| Club Head Material | club_head_material | text | — | Material of the golf club head | Titanium, Stainless Steel, Forged Carbon, Maraging Steel, Tungsten-Weighted |
| Golf Ball Cover Material | golf_ball_cover_material | text | — | Outer cover material of a golf ball | Surlyn, Urethane, Cast Urethane |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the equipment was manufactured | China, Japan, USA, Taiwan, Thailand |
| Sport | sport | enum | — | Primary sport category | Tennis, Badminton, Squash, Pickleball, Golf, Padel, Racquetball, Table Tennis |
| Balance | balance | text | mm | Distance from the butt end to the balance point; or head-light/heavy designation | 320 (7 pts HL), 330 (3 pts HL), 340 (Even), 345 (2 pts HH) |
| String Pattern | string_pattern | text | — | Number of main x cross strings | 16x19, 16x20, 18x20, 16x18 |
| Beam Width | beam_width | text | mm | Frame thickness at various points along the racquet | 21, 23-26-23, 21.5-23-21, 22 |
| Stiffness (RA) | stiffness_ra | number | — | Frame flex rating on the RA scale; higher is stiffer | 55, 62, 64, 68, 72 |
| Club Loft | club_loft | number | degrees | Angle of the clubface relative to the shaft for golf clubs | 9, 10.5, 12, 15, 21, 46, 52, 56, 60 |
| Shaft Flex | shaft_flex | text | — | Stiffness designation of the golf club shaft | L (Ladies), A (Senior), R (Regular), S (Stiff), X (Extra Stiff) |
| Club Head Volume | club_head_volume | number | cc | Volume of the golf club head in cubic centimetres | 200, 380, 440, 460 |
| Lie Angle | lie_angle | number | degrees | Angle between the shaft and the ground plane at address | 56, 58, 60, 62, 64 |
| Hand Orientation | hand_orientation | enum | — | Left-handed or right-handed configuration | Right, Left |
| Golf Ball Construction | golf_ball_construction | text | — | Internal layer structure of a golf ball | 2-Piece, 3-Piece, 4-Piece, 5-Piece |
| Golf Ball Compression | golf_ball_compression | number | — | Compression rating indicating ball firmness | 50, 65, 75, 85, 90, 100 |
| Skill Level | skill_level | text | — | Intended player skill level | Beginner, Intermediate, Advanced, Tour, Junior |
| Adjustable | adjustable | boolean | — | Whether the equipment has adjustable loft, weight, or settings | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ITF racquet specifications, USGA equipment rules, and R and A conformance standards | [Wilson](https://www.wilson.com/en-us/tennis/rackets), [Callaway Golf](https://www.callawaygolf.com/), [Tennis Warehouse](https://www.tennis-warehouse.com/), [Titleist](https://www.titleist.com/) |
