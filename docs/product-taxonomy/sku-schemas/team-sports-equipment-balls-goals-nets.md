# SKU Schema: Team Sports Equipment (Balls, Goals, Nets)

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | ADI-IA0953, WIL-WTB0730, NWS-FORZA-60, NK-SC3992 |
| Product Name | text | Full product name including brand, sport, and key specs | Adidas Al Rihla Pro Match Ball FIFA Quality Pro, FORZA Alu60 Soccer Goal 8ft x 24ft |
| URL | text | Direct link to the product page | https://example.com/product/al-rihla-match-ball |
| Price | number | Numeric retail price excluding currency symbol | 24.99, 49.99, 165.00, 799.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Brand/Manufacturer | text | Equipment brand or manufacturer name | Adidas, Nike, Wilson, Mikasa, Spalding, FORZA, Bownet, Brine, Molten |
| Sport | text | Primary sport the equipment is designed for | Soccer, Basketball, Football, Volleyball, Lacrosse, Field Hockey, Rugby, Handball, Cricket |
| Equipment Type | text | Specific product category within team sports | Match Ball, Training Ball, Goal, Net, Replacement Net, Rebounder, Cone Set, Agility Ladder, Scoreboard |
| Ball Size | text | Official size designation of the ball | Size 3, Size 4, Size 5, Size 7 (Basketball), Size 9 (Football), Official |
| Circumference | text (cm) | Ball circumference range per specifications | 68-70 (Soccer Size 5), 74.9-78 (Basketball Size 7) |
| Weight | text (g) | Ball weight or equipment weight | 410-450 (Soccer Size 5), 567-650 (Basketball), 25000 (Goal) |
| Panel Count | number | Number of panels on the ball surface | 6, 12, 18, 26, 32 |
| Panel Construction | text | Method of joining panels together | Thermo-Bonded, Machine-Stitched, Hand-Stitched, Laminated |
| Outer Material | text | Surface material of the ball or primary material of goals/nets | Polyurethane, TPU, Synthetic Leather, Rubber, Composite Leather, Aluminum, Steel |
| Bladder Type | text | Internal bladder material for inflatable balls | Butyl, Latex, Polyester-Wound Butyl |
| FIFA Certification | text | FIFA quality mark for soccer balls | FIFA Quality Pro, FIFA Quality, FIFA Basic, IMS (International Match Standard) |
| Goal Dimensions | text | Width x height of the goal frame opening | 8ft x 24ft, 6ft x 12ft, 4ft x 6ft, 12ft x 6ft, 21ft x 7ft |
| Frame Material | text | Material of the goal frame or post structure | Powder-Coated Aluminum, Galvanized Steel, PVC, UPVC, Fiberglass |
| Frame Tube Diameter | number (mm) | Outer diameter of the goal frame tubing | 48, 60, 76, 80, 102 |
| Net Material | text | Fiber material and construction of the net | HDPE, Polyethylene, Nylon, Polyester, Polypropylene |
| Net Mesh Size | text (mm) | Size of individual mesh openings in the net | 100 x 100, 120 x 120, 150 x 150, 4 inch square |
| Net Cord Thickness | text (mm) | Diameter or gauge of the net cord | 2.5, 3.0, 4.0, 5.0 |
| Ground Anchors Included | boolean | Whether ground stakes or anchors are included | Yes, No |
| Portability | text | Whether the equipment is fixed, portable, or collapsible | Permanent, Semi-Permanent, Portable, Pop-Up, Foldable, Wheeled |
| Assembly Required | boolean | Whether the equipment requires assembly from parts | Yes, No |
| Age Group | text | Target age range or level of play | Youth (U6-U8), Junior (U10-U12), Senior (U14+), Adult, All Ages |
| Playing Level | text | Intended standard of play | Recreational, Club, School, Competition, Professional, Match, Training |
| Indoor/Outdoor | enum | Intended usage environment | Indoor, Outdoor, Indoor/Outdoor |
| Color | text | Dominant color or color combination | White/Black, Yellow/Blue, Orange, Neon Green, Multi-Color |
| Dimensions (Packed) | text (mm) | Dimensions of the product in its shipping carton | 1220 x 610 x 150 |
| Country of Origin | text | Country where the equipment was manufactured | China, Pakistan, Thailand, India, UK |
| Certification | text (list) | Safety and sport-governing body certifications | CE, FIFA, FIVB, FIBA, IRB, World Rugby, EN 748 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus FIFA ball testing protocol, EN 748 goal safety standard, and sport federation certification systems | [Adidas](https://www.adidas.com/us/soccer-balls), [Net World Sports](https://www.networldsports.com/), [Wilson](https://www.wilson.com/en-us), [Dicks Sporting Goods](https://www.dickssportinggoods.com/) |
