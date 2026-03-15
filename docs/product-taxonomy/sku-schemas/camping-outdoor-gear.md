# SKU Schema: Camping & Outdoor Gear

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.camping_outdoor`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | REI-243611, MSR-13113, TNF-A3HB, COL-2000038014 |
| Product Name | product_name | text | Full product name including brand, model, and key specs | REI Co-op Trailmade 2 Tent with Footprint, MSR Hubba Hubba NX 2-Person, Osprey Atmos AG 65 Pack |
| URL | url | text | Direct link to the product page | https://example.com/product/trailmade-2-tent |
| Price | price | number | Numeric retail price excluding currency symbol | 49.99, 179.00, 449.95, 599.00 |
| Currency | currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Equipment Type | equipment_type | text | Specific product category | Tent, Sleeping Bag, Sleeping Pad, Backpack, Camp Stove, Headlamp, Water Filter, Cooler, Trekking Poles, Camp Chair |
| Pole Material | pole_material | text | Material of tent or trekking poles | DAC Featherlite NSL Aluminum, Carbon Fiber, Fiberglass, DAC Pressfit, Easton Syclone |
| Fly Material | fly_material | text | Fabric specification of the rain fly | 20D Ripstop Nylon with 1200mm PU Coating, 40D Ripstop Nylon with Silicone/PU |
| Floor Material | floor_material | text | Fabric specification of the tent floor | 30D Ripstop Nylon with 3000mm PU Coating, 40D Ripstop Nylon, 70D Nylon Taffeta |
| Setup Type | setup_type | enum | Whether the tent is freestanding or requires stakes | Freestanding, Semi-Freestanding, Non-Freestanding (Staked) |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Fill Type | fill_type | text | Insulation material for sleeping bags and pads | 650 Fill Goose Down, 800 Fill Goose Down, Primaloft Gold, Climashield Apex, Synthetic HL |
| Fuel Type | fuel_type | text | Type of fuel or energy source for stoves and lanterns | Isobutane/Propane Canister, White Gas, Alcohol, Wood, USB Rechargeable, AAA Battery, CR123A |
| Material (Shell) | material_shell | text | Primary outer shell or body material | Ripstop Nylon, Cordura, Dyneema Composite Fabric, Polyester, Aluminum, Titanium, Stainless Steel |
| Country of Origin | country_of_origin | text | Country where the gear was manufactured | China, Vietnam, USA, South Korea, Taiwan |
| Seasonality | seasonality | text | Seasonal rating indicating the conditions the gear is designed for | 3-Season, 3+ Season, 4-Season, Summer |
| Packed Dimensions | packed_dimensions | text (cm) | Length x diameter or L x W x H when packed in its stuff sack | 46 x 15, 51 x 17, 53 x 18 x 18 |
| Floor Area | floor_area | number (sq m) | Interior usable floor space of a tent or shelter | 2.4, 2.7, 3.2, 8.4 |
| Vestibule Area | vestibule_area | number (sq m) | Covered storage area outside the tent door | 0.74, 0.84, 1.58 |
| Peak Height | peak_height | number (cm) | Interior height at the tallest point | 91, 102, 112, 160 |
| Number of Doors | number_of_doors | number | Count of entry/exit doors on a tent | 1, 2, 3 |
| Number of Poles | number_of_poles | number | Count of structural poles in a tent | 1, 2, 3, 4 |
| Waterproof Rating | waterproof_rating | number (mm) | Hydrostatic head rating indicating waterproofness of coated fabrics | 1200, 1500, 3000, 5000, 10000 |
| Temperature Rating | temperature_rating | number (C) | Comfort-rated temperature for sleeping bags | -18, -7, 0, 5, 10, 15 |
| R-Value | r-value | number | Thermal resistance rating for sleeping pads per ASTM F3340 | 1.0, 2.0, 3.2, 4.2, 5.7, 6.9 |
| Volume (Pack) | volume_pack | number (L) | Internal carrying capacity of a backpack | 20, 35, 50, 65, 75, 85 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus ASTM F3340 (sleeping pad R-Value), CPAI-84 (tent flammability), and EN 13537 (sleeping bag temperature rating) standards | [REI Co-op](https://www.rei.com/), [MSR](https://www.msrgear.com/), [The North Face](https://www.thenorthface.com/), [Coleman](https://www.coleman.com/) |
