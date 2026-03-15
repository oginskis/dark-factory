# SKU Schema: Watches & Clocks

**Last updated:** 2026-03-15
**Parent category:** Jewelry, Watches & Accessories
**Taxonomy ID:** `jewelry.watches_clocks`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | OMG-21030422, SEI-SWR054, CIT-BN0151-09L |
| Product Name | text | Full product name including brand, collection, and key specs | Omega Seamaster Diver 300M Co-Axial Master Chronometer 42mm, Seiko Presage Automatic SPB167 |
| URL | text | Direct link to the product page | https://example.com/product/seamaster-diver-300m |
| Price | number | Numeric retail price excluding currency symbol | 175.00, 5400.00, 42500.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, JPY, CHF |
| Product Type | enum | Primary product category | Wristwatch, Pocket Watch, Wall Clock, Mantel Clock, Desk Clock, Alarm Clock, Grandfather Clock, Cuckoo Clock |
| Case Material | text | Material of the watch case body | Stainless Steel, Titanium, Ceramic, 18K Yellow Gold, Carbon Fiber, Resin, Bronze |
| Movement Type | enum | Timekeeping mechanism category | Automatic (Mechanical), Manual Winding, Quartz, Solar (Eco-Drive), Spring Drive, Kinetic |
| Crystal Type | text | Material covering the dial face | Sapphire, Hardlex, Mineral, Hesalite, Acrylic |
| Bezel Type | text | Type and function of the rotating or fixed bezel | Unidirectional Diving, Bidirectional, Fixed, Tachymeter, GMT, Fluted |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Bezel Material | text | Material of the bezel insert or ring | Ceramic, Aluminum, Stainless Steel, 18K Gold |
| Bracelet/Strap Material | text | Material of the band or bracelet | Stainless Steel, Leather, Rubber, NATO Nylon, Titanium, Mesh, Canvas |
| Clasp Type | text | Type of bracelet or strap closure | Deployant, Folding, Pin Buckle, Butterfly, Jewelry Clasp |
| Country of Origin | text | Country where the watch or clock was manufactured | Switzerland, Japan, Germany, China, USA |
| Collection | text | Named product line or series | Seamaster, Speedmaster, Prospex, Prestige, G-Shock, Eco-Drive |
| Case Thickness | number (mm) | Height of the watch case from caseback to crystal | 4.88, 11.5, 13.7 |
| Case Shape | enum | Geometric shape of the watch case | Round, Square, Rectangular, Tonneau, Cushion, Octagonal |
| Dial Color | text | Color of the watch face or clock face | Black, White, Blue, Silver, Green, Champagne, Mother of Pearl |
| Caliber | text | Manufacturer designation for the specific movement | 8800, 4N30, Miyota 9015, NH35A, B873, ETA 2824-2 |
| Power Reserve | number (hours) | Hours of operation on a full wind or charge | 40, 44, 55, 60, 80, 168 |
| Frequency | number (vph) | Oscillation rate of the movement in vibrations per hour | 21600, 25200, 28800, 36000 |
| Water Resistance | text (m) | Maximum depth rating in metres | 30, 50, 100, 200, 300, 600 |
| Lug Width | number (mm) | Distance between lugs where the strap attaches | 14, 18, 20, 22, 24 |
| Lug-to-Lug | number (mm) | Total vertical span from lug tip to lug tip | 42, 45, 47, 50, 52 |
| Complications | text (list) | Additional functions beyond basic timekeeping | Date, Day-Date, Chronograph, GMT, Moon Phase, Tourbillon, Perpetual Calendar, Alarm, World Time |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ISO 6425, COSC, and METAS certification standards | [Omega](https://www.omegawatches.com/watches), [Seiko](https://seikousa.com/), [Citizen](https://www.citizenwatch.com/), [Howard Miller](https://www.howardmiller.com/) |
