# SKU Schema: Team Sports Equipment (Balls, Goals, Nets)

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.team_sports`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | ADI-IA0953, WIL-WTB0730, NWS-FORZA-60, NK-SC3992 |
| Product Name | product_name | text | Full product name including brand, sport, and key specs | Adidas Al Rihla Pro Match Ball FIFA Quality Pro, FORZA Alu60 Soccer Goal 8ft x 24ft |
| URL | url | text | Direct link to the product page | https://example.com/product/al-rihla-match-ball |
| Price | price | number | Numeric retail price excluding currency symbol | 24.99, 49.99, 165.00, 799.00 |
| Currency | currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Equipment Type | equipment_type | text | Specific product category within team sports | Match Ball, Training Ball, Goal, Net, Replacement Net, Rebounder, Cone Set, Agility Ladder, Scoreboard |
| Outer Material | outer_material | text | Surface material of the ball or primary material of goals/nets | Polyurethane, TPU, Synthetic Leather, Rubber, Composite Leather, Aluminum, Steel |
| Bladder Type | bladder_type | text | Internal bladder material for inflatable balls | Butyl, Latex, Polyester-Wound Butyl |
| Frame Material | frame_material | text | Material of the goal frame or post structure | Powder-Coated Aluminum, Galvanized Steel, PVC, UPVC, Fiberglass |
| Net Material | net_material | text | Fiber material and construction of the net | HDPE, Polyethylene, Nylon, Polyester, Polypropylene |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the equipment was manufactured | China, Pakistan, Thailand, India, UK |
| Sport | sport | text | Primary sport the equipment is designed for | Soccer, Basketball, Football, Volleyball, Lacrosse, Field Hockey, Rugby, Handball, Cricket |
| Circumference | circumference | text (cm) | Ball circumference range per specifications | 68-70 (Soccer Size 5), 74.9-78 (Basketball Size 7) |
| Panel Construction | panel_construction | text | Method of joining panels together | Thermo-Bonded, Machine-Stitched, Hand-Stitched, Laminated |
| FIFA Certification | fifa_certification | text | FIFA quality mark for soccer balls | FIFA Quality Pro, FIFA Quality, FIFA Basic, IMS (International Match Standard) |
| Goal Dimensions | goal_dimensions | text | Width x height of the goal frame opening | 8ft x 24ft, 6ft x 12ft, 4ft x 6ft, 12ft x 6ft, 21ft x 7ft |
| Net Cord Thickness | net_cord_thickness | text (mm) | Diameter or gauge of the net cord | 2.5, 3.0, 4.0, 5.0 |
| Ground Anchors Included | ground_anchors_included | boolean | Whether ground stakes or anchors are included | Yes, No |
| Portability | portability | text | Whether the equipment is fixed, portable, or collapsible | Permanent, Semi-Permanent, Portable, Pop-Up, Foldable, Wheeled |
| Assembly Required | assembly_required | boolean | Whether the equipment requires assembly from parts | Yes, No |
| Age Group | age_group | text | Target age range or level of play | Youth (U6-U8), Junior (U10-U12), Senior (U14+), Adult, All Ages |
| Playing Level | playing_level | text | Intended standard of play | Recreational, Club, School, Competition, Professional, Match, Training |
| Indoor/Outdoor | indooroutdoor | enum | Intended usage environment | Indoor, Outdoor, Indoor/Outdoor |
| Color | color | text | Dominant color or color combination | White/Black, Yellow/Blue, Orange, Neon Green, Multi-Color |
| Dimensions (Packed) | dimensions_packed | text (mm) | Dimensions of the product in its shipping carton | 1220 x 610 x 150 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus FIFA ball testing protocol, EN 748 goal safety standard, and sport federation certification systems | [Adidas](https://www.adidas.com/us/soccer-balls), [Net World Sports](https://www.networldsports.com/), [Wilson](https://www.wilson.com/en-us), [Dicks Sporting Goods](https://www.dickssportinggoods.com/) |
