# SKU Schema: Fishing Tackle & Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SHM-ST2500HGFM, ABU-REVO5X, PEN-BTLIII5000, DAI-BG4000 |
| Product Name | text | Full product name including brand, model series, and key specs | Shimano Stradic FM 2500 HG Spinning Reel, Penn Battle III 5000 Spinning Reel, St. Croix Legend X 7ft Medium Fast Spinning Rod |
| URL | text | Direct link to the product page | https://example.com/product/stradic-fm-2500hg |
| Price | number | Numeric retail price excluding currency symbol | 39.99, 149.95, 249.99, 449.99 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, CAD |
| Brand/Manufacturer | text | Tackle brand or manufacturer name | Shimano, Daiwa, Penn, Abu Garcia, St. Croix, G. Loomis, Rapala, Berkley, Okuma |
| Equipment Type | text | Specific product category | Spinning Reel, Baitcasting Reel, Conventional Reel, Fly Reel, Spinning Rod, Casting Rod, Fly Rod, Combo, Lure, Line, Terminal Tackle |
| Rod Length | text (ft) | Overall length of a fishing rod, expressed in feet and inches | 5-6, 6-6, 7-0, 7-6, 8-0, 9-0, 10-0 |
| Rod Power | text | Power or weight classification of a rod indicating backbone strength | Ultralight (UL), Light (L), Medium-Light (ML), Medium (M), Medium-Heavy (MH), Heavy (H), Extra Heavy (XH) |
| Rod Action | text | Where the rod flexes under load, from tip to butt | Extra Fast, Fast, Moderate Fast, Moderate, Slow |
| Number of Pieces | number | Number of sections the rod breaks down into | 1, 2, 3, 4 |
| Line Weight Rating | text (lb) | Recommended monofilament line strength range | 2-6, 4-10, 6-12, 8-17, 10-20, 15-30 |
| Lure Weight Rating | text (oz) | Recommended casting lure weight range | 1/32-1/4, 1/8-1/2, 1/4-3/4, 3/8-1, 1/2-1.5 |
| Rod Material | text | Primary blank construction material | IM6 Graphite, IM7 Graphite, High Modulus Carbon, SCIII Carbon, Fiberglass, Composite |
| Guide Count | number | Number of line guides including the tip-top | 6, 7, 8, 9, 10, 12 |
| Guide Material | text | Material and frame type of the line guides | Stainless Steel SiC, Fuji Alconite, Fuji K-Guide, Titanium SiC, Zirconia Insert |
| Handle Material | text | Material of the rod grip | Cork, EVA Foam, Hypalon, Split Cork/EVA, Winn Polymer |
| Gear Ratio | text | Spool rotations per handle crank for reels | 5.2:1, 5.8:1, 6.2:1, 6.4:1, 7.1:1, 8.1:1 |
| Ball Bearings | text | Number and type of bearings in the reel | 6+1, 7+1, 10+1, 11+1 S A-RB, 14+1 HPB |
| Max Drag | number (kg) | Maximum drag force the reel can apply | 3.0, 4.5, 9.0, 10.9, 13.6 |
| Reel Weight | number (g) | Weight of the reel body and handle | 155, 185, 221, 310, 480 |
| Line Capacity (Mono) | text | Monofilament line capacity expressed as lb test / yards | 6/200, 8/240, 10/200, 12/160, 20/270 |
| Line Capacity (Braid) | text | Braided line capacity expressed as lb test / yards | 10/150, 15/220, 20/230, 30/275, 50/300 |
| Line Retrieve Per Crank | number (cm) | Length of line recovered per full handle turn | 64, 75, 84, 94, 102 |
| Reel Size | text | Manufacturer size designation for the reel | 1000, 2500, 3000, 4000, 5000, 8000, 200, 300 |
| Body Material | text | Material of the reel frame and body | Graphite, Aluminum, Magnesium, Carbon Composite, HAGANE Metal |
| Spool Material | text | Material of the line spool | Machined Aluminum, Cold-Forged Aluminum, Graphite, Carbon Fiber |
| Drag System | text | Type of drag mechanism in the reel | Carbon Fiber Washers, HT-100, Cross Carbon, Dura Cross, Felt |
| Anti-Reverse | boolean | Whether the reel has an instant anti-reverse mechanism | Yes, No |
| Fishing Environment | text (list) | Intended water type and conditions | Freshwater, Saltwater, Inshore, Offshore, Ice, Fly |
| Target Species | text (list) | Fish species the equipment is designed for | Bass, Trout, Walleye, Salmon, Tuna, Redfish, Panfish, Musky, Catfish |
| Country of Origin | text | Country where the tackle was manufactured | Japan, China, South Korea, USA, Malaysia, Thailand |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus AFTMA line weight standards and IGFA tackle class specifications | [Shimano](https://fish.shimano.com/), [Penn](https://www.pennfishing.com/), [TackleDirect](https://www.tackledirect.com/), [Abu Garcia](https://www.abugarcia.com/) |
