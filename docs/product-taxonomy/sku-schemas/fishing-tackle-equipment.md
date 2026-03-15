# SKU Schema: Fishing Tackle & Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.fishing_tackle`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SHM-4805, STA-0472, ABU-REVO5X, PEN-BTLIII5000 |
| Product Name | text | Full product name including brand, model series, and key differentiating specs | Shimano Stradic FM 3000XG Spinning Reel, Star Rods Stellar Surf Spinning Rod 12ft, Rapala X-Rap Saltwater 10 Crankbait |
| URL | text | Direct link to the product page | https://example.com/product/stradic-fm-3000xg |
| Price | number | Numeric retail price per unit excluding currency symbol | 39.99, 149.95, 254.99, 449.99 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, CAD, AUD |
| Equipment Type | enum | Primary product category within fishing tackle | Spinning Reel, Baitcasting Reel, Conventional Reel, Fly Reel, Spinning Rod, Casting Rod, Fly Rod, Rod and Reel Combo, Hard Lure, Soft Lure, Spinnerbait, Jig, Fly, Fishing Line, Leader, Hook, Sinker, Swivel, Float, Net |
| Model Number | text | Manufacturer part number or model designation | STC3000XGFM, SG22040S12, CVS60MB |
| Rod Blank Material | text | Primary construction material of the rod blank | IM6 Graphite, IM7 Graphite, 30-Ton Graphite, 36-Ton Graphite, High Modulus Carbon, Fiberglass, E-Glass, Composite |
| Guide Type | text | Material and style of the line guides including tip-top | Fuji Alconite, Fuji K-Guide, Stainless Steel SiC, Titanium Oxide, Aluminum Oxide Insert |
| Handle Material | text | Material of the rod grip | Cork, EVA Foam, Hypalon, Split Cork/EVA, Winn Polymer, Cork Tape |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Body Material | text | Primary material of the reel frame or lure body | Graphite, Aluminum, Magnesium, Carbon Composite, HAGANE Metal, ABS Plastic, Balsa Wood |
| Lure Type | text | Specific lure subcategory | Crankbait, Jerkbait, Topwater Popper, Swimbait, Spoon, In-Line Spinner, Spinnerbait, Buzzbait, Soft Plastic Worm, Soft Plastic Creature, Jig, Fly |
| Line Material | enum | Construction material of the fishing line | Monofilament, Fluorocarbon, Braided (4-strand), Braided (8-strand), Copolymer, Wire |
| UPC/EAN | text | Universal product barcode identifier | 022255275903, 768721544219 |
| Rod Power | enum | Backbone strength classification of a rod | Ultra-Light (UL), Light (L), Medium-Light (ML), Medium (M), Medium-Heavy (MH), Heavy (H), Extra-Heavy (XH) |
| Rod Action | enum | Where the rod flexes under load from tip toward butt | Extra Fast, Fast, Moderate Fast, Moderate, Slow |
| Number of Pieces | number | Number of sections the rod or combo breaks down into | 1, 2, 3, 4 |
| Gear Ratio | text | Spool rotations per full handle turn for reels | 5.2:1, 5.8:1, 6.0:1, 6.2:1, 6.4:1, 7.1:1, 8.1:1 |
| Ball Bearings | text | Count and type of bearings in the reel, typically expressed as ball bearings plus roller bearing | 4+1, 6+1 S A-RB, 7+1, 10+1, 11+1, 14+1 HPB |
| Max Drag | number (lb) | Maximum drag force the reel can apply | 10, 15, 20, 25, 30, 44 |
| Line Retrieve Per Crank | number (in) | Length of line recovered per full handle turn | 22, 26, 33, 37, 41 |
| Drag System | text | Type of drag mechanism in the reel | Carbon Fiber Washers, HT-100, Cross Carbon, Dura Cross, Felt |
| Diving Depth | text (ft) | Maximum running depth of a diving lure on a standard retrieve | 0 (surface), 2-4, 4-8, 8-12, 12-16, 16-20 |
| Hook Configuration | text | Number, type, and size of hooks on a lure or in a terminal tackle pack | 2 Treble No. 6, 3 Treble No. 4, Single 1/0, Circle 3/0, Octopus 2/0 |
| Color/Pattern | text | Primary color or pattern designation of a lure, line, or accessory | Chartreuse Shad, Bone, Firetiger, Ghost Minnow, Watermelon Red, Pumpkinseed, Black/Gold |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes covering rods, reels, lures, lines, and terminal tackle from 4 companies plus AFTMA rod power standards and industry line test conventions | [TackleDirect](https://www.tackledirect.com/), [Shimano Fishing](https://fish.shimano.com/), [Bass Pro Shops](https://www.basspro.com/), [Len Thompson Lures](https://www.lenthompson.com/) |
