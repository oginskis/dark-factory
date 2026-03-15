# SKU Schema: Camping & Outdoor Gear

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.camping_outdoor`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | REI-243611, MSR-13113, TNF-A3HB, COL-2000038014 |
| Product Name | text | Full product name including brand, model, and key specs | REI Co-op Trailmade 2 Tent with Footprint, MSR Hubba Hubba NX 2-Person, Osprey Atmos AG 65 Pack |
| URL | text | Direct link to the product page | https://example.com/product/trailmade-2-tent |
| Price | number | Numeric retail price excluding currency symbol | 49.99, 179.00, 449.95, 599.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Equipment Type | text | Specific product category | Tent, Sleeping Bag, Sleeping Pad, Backpack, Camp Stove, Headlamp, Water Filter, Cooler, Trekking Poles, Camp Chair |
| Pole Material | text | Material of tent or trekking poles | DAC Featherlite NSL Aluminum, Carbon Fiber, Fiberglass, DAC Pressfit, Easton Syclone |
| Fly Material | text | Fabric specification of the rain fly | 20D Ripstop Nylon with 1200mm PU Coating, 40D Ripstop Nylon with Silicone/PU |
| Floor Material | text | Fabric specification of the tent floor | 30D Ripstop Nylon with 3000mm PU Coating, 40D Ripstop Nylon, 70D Nylon Taffeta |
| Setup Type | enum | Whether the tent is freestanding or requires stakes | Freestanding, Semi-Freestanding, Non-Freestanding (Staked) |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Fill Type | text | Insulation material for sleeping bags and pads | 650 Fill Goose Down, 800 Fill Goose Down, Primaloft Gold, Climashield Apex, Synthetic HL |
| Fuel Type | text | Type of fuel or energy source for stoves and lanterns | Isobutane/Propane Canister, White Gas, Alcohol, Wood, USB Rechargeable, AAA Battery, CR123A |
| Material (Shell) | text | Primary outer shell or body material | Ripstop Nylon, Cordura, Dyneema Composite Fabric, Polyester, Aluminum, Titanium, Stainless Steel |
| Country of Origin | text | Country where the gear was manufactured | China, Vietnam, USA, South Korea, Taiwan |
| Seasonality | text | Seasonal rating indicating the conditions the gear is designed for | 3-Season, 3+ Season, 4-Season, Summer |
| Packed Dimensions | text (cm) | Length x diameter or L x W x H when packed in its stuff sack | 46 x 15, 51 x 17, 53 x 18 x 18 |
| Floor Area | number (sq m) | Interior usable floor space of a tent or shelter | 2.4, 2.7, 3.2, 8.4 |
| Vestibule Area | number (sq m) | Covered storage area outside the tent door | 0.74, 0.84, 1.58 |
| Peak Height | number (cm) | Interior height at the tallest point | 91, 102, 112, 160 |
| Number of Doors | number | Count of entry/exit doors on a tent | 1, 2, 3 |
| Number of Poles | number | Count of structural poles in a tent | 1, 2, 3, 4 |
| Waterproof Rating | number (mm) | Hydrostatic head rating indicating waterproofness of coated fabrics | 1200, 1500, 3000, 5000, 10000 |
| Temperature Rating | number (C) | Comfort-rated temperature for sleeping bags | -18, -7, 0, 5, 10, 15 |
| R-Value | number | Thermal resistance rating for sleeping pads per ASTM F3340 | 1.0, 2.0, 3.2, 4.2, 5.7, 6.9 |
| Volume (Pack) | number (L) | Internal carrying capacity of a backpack | 20, 35, 50, 65, 75, 85 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ASTM F3340 (sleeping pad R-Value), CPAI-84 (tent flammability), and EN 13537 (sleeping bag temperature rating) standards | [REI Co-op](https://www.rei.com/), [MSR](https://www.msrgear.com/), [The North Face](https://www.thenorthface.com/), [Coleman](https://www.coleman.com/) |
