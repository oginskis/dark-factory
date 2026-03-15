# SKU Schema: Racquet & Golf Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | WIL-WR079411U, CAL-PRDX-AI, YON-EZONE100, TM-M6D |
| Product Name | text | Full product name including brand, model, and key specs | Wilson Blade 98 v9 18x20, Callaway Paradym Ai Smoke Driver 10.5 Stiff, Yonex EZONE 100 |
| URL | text | Direct link to the product page | https://example.com/product/blade-98-v9 |
| Price | number | Numeric retail price excluding currency symbol | 129.00, 249.99, 549.99, 599.99 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, CAD |
| Brand/Manufacturer | text | Equipment brand or manufacturer name | Wilson, Babolat, Head, Yonex, Callaway, TaylorMade, Titleist, Ping, Prince |
| Sport | enum | Primary sport category | Tennis, Badminton, Squash, Pickleball, Golf, Padel, Racquetball, Table Tennis |
| Equipment Type | text | Specific product category | Racquet, Driver, Fairway Wood, Hybrid, Iron Set, Wedge, Putter, Golf Ball, Golf Bag, Paddle, Grip, String |
| Head Size | number (sq in) | Hitting area of the racquet face in square inches | 95, 97, 98, 100, 105, 110 |
| Weight Unstrung | number (g) | Weight of a racquet without strings installed | 285, 295, 305, 310, 315 |
| Weight Strung | number (g) | Weight of a racquet with strings installed | 300, 310, 320, 325 |
| Balance | text (mm) | Distance from the butt end to the balance point; or head-light/heavy designation | 320 (7 pts HL), 330 (3 pts HL), 340 (Even), 345 (2 pts HH) |
| Swing Weight | number | Measure of how heavy the racquet feels during a swing (kg*cm2) | 280, 305, 315, 325, 340 |
| String Pattern | text | Number of main x cross strings | 16x19, 16x20, 18x20, 16x18 |
| Beam Width | text (mm) | Frame thickness at various points along the racquet | 21, 23-26-23, 21.5-23-21, 22 |
| Stiffness (RA) | number | Frame flex rating on the RA scale; higher is stiffer | 55, 62, 64, 68, 72 |
| Racquet Length | number (inches) | Overall length of the racquet | 27, 27.25, 27.5 |
| Grip Size | text | Handle circumference designation | 4 1/8 (L1), 4 1/4 (L2), 4 3/8 (L3), 4 1/2 (L4), 4 5/8 (L5) |
| Composition | text | Primary frame construction material | Graphite, Carbon Fiber, Graphene, Kevlar/Carbon, Fiberglass, Boron/Graphite |
| Club Loft | number (degrees) | Angle of the clubface relative to the shaft for golf clubs | 9, 10.5, 12, 15, 21, 46, 52, 56, 60 |
| Shaft Material | enum | Material of the golf club shaft | Graphite, Steel, Multi-Material |
| Shaft Flex | text | Stiffness designation of the golf club shaft | L (Ladies), A (Senior), R (Regular), S (Stiff), X (Extra Stiff) |
| Shaft Length | number (inches) | Overall length of the golf club | 35, 37.5, 43, 44, 45, 45.75 |
| Club Head Volume | number (cc) | Volume of the golf club head in cubic centimetres | 200, 380, 440, 460 |
| Club Head Material | text | Material of the golf club head | Titanium, Stainless Steel, Forged Carbon, Maraging Steel, Tungsten-Weighted |
| Lie Angle | number (degrees) | Angle between the shaft and the ground plane at address | 56, 58, 60, 62, 64 |
| Hand Orientation | enum | Left-handed or right-handed configuration | Right, Left |
| Golf Ball Construction | text | Internal layer structure of a golf ball | 2-Piece, 3-Piece, 4-Piece, 5-Piece |
| Golf Ball Cover Material | text | Outer cover material of a golf ball | Surlyn, Urethane, Cast Urethane |
| Golf Ball Compression | number | Compression rating indicating ball firmness | 50, 65, 75, 85, 90, 100 |
| Skill Level | text | Intended player skill level | Beginner, Intermediate, Advanced, Tour, Junior |
| Adjustable | boolean | Whether the equipment has adjustable loft, weight, or settings | Yes, No |
| Country of Origin | text | Country where the equipment was manufactured | China, Japan, USA, Taiwan, Thailand |
| Certification | text (list) | Governing body approval or conformance | ITF Approved, USGA Conforming, R and A Conforming, WPT Approved |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ITF racquet specifications, USGA equipment rules, and R and A conformance standards | [Wilson](https://www.wilson.com/en-us/tennis/rackets), [Callaway Golf](https://www.callawaygolf.com/), [Tennis Warehouse](https://www.tennis-warehouse.com/), [Titleist](https://www.titleist.com/) |
