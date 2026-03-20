# SKU Schema: Trailers & Semi-Trailers

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.trailers_semi_trailers`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | N124-BV, GD-CHP-53DV, WNI-HDVN-53 |
| Product Name | product_name | text | — | yes | Full product name including trailer type, length, and key configuration | Great Dane Champion 53ft Dry Van, Fontaine Infinity 53ft Combo Flatbed, Wabash DuraPlate HD 53ft Dry Van |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/trailers/champion-53-dryvan |
| Price | price | number | — | yes | Numeric price per unit excluding currency symbol | 42500, 68000, 125000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Trailer Type | trailer_type | enum | — | — | Primary functional category of the trailer | Dry Van, Refrigerated, Flatbed, Drop Deck, Lowboy, Dump, Tank, Enclosed, Curtainside, Chassis, Livestock |
| Suspension Type | suspension_type | enum | — | — | Type of suspension system | Air Ride, Mechanical Spring, Sliding |
| Floor Material | floor_material | text | — | — | Material used for the trailer floor | Laminated Oak, Aluminum, Composite, Steel |
| Sidewall Material | sidewall_material | text | — | — | Primary material of the sidewall construction | DuraPlate Composite, Sheet and Post, Aluminum, Steel, Fiberglass |
| Door Type | door_type | enum | — | — | Type of rear or side doors | Swing, Roll-Up, Side Door, Barn Door |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Brake Type | brake_type | enum | — | — | Type of braking system installed | Drum, Disc, ABS 4S2M |
| Coupling Type | coupling_type | text | — | — | Fifth wheel coupling specification | 2 in Standard, 3-3/8 in SAE |
| Country of Origin | country_of_origin | text | — | — | Country where the trailer was manufactured | USA, China, Germany, Mexico, India |
| Model | model | text | — | — | Manufacturer model name or series designation | Champion, DuraPlate HD, Infinity, Revolution, Everest |
| Year | year | number | — | — | Model year of manufacture | 2024, 2025, 2026 |
| Condition | condition | enum | — | — | Whether the trailer is new or used | New, Used, Certified Pre-Owned |
| Overall Width | overall_width | number | in | — | Exterior width of the trailer | 96, 102 |
| Overall Height | overall_height | number | ft-in | — | Exterior height from ground to top of trailer | 13 ft 6 in, 13 ft 11 in |
| Interior Height Front | interior_height_front | number | in | — | Interior cargo height at the front wall | 108, 110.25 |
| Interior Height Rear | interior_height_rear | number | in | — | Interior cargo height at the rear doors | 109, 111.25 |
| Interior Width | interior_width | number | in | — | Interior cargo width wall to wall | 98.5, 101 |
| GVWR | gvwr | number | lb | — | Gross Vehicle Weight Rating, the maximum allowable loaded weight | 68000, 80000, 105500 |
| GAWR | gawr | number | lb | — | Gross Axle Weight Rating per axle assembly | 20000, 23000, 25000 |
| Frame Rating | frame_rating | number | lb | — | Rated frame load capacity | 80000, 100000, 120000 |
| Floor Rating | floor_rating | number | lb | — | Dynamic floor load rating for forklift operations | 16000, 20000, 24000, 28000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (TTMA, DOT FMVSS, NATM) | [Great Dane](https://greatdane.com/champion-dry-vans/), [Wabash National](https://ascendancetrucks.com/wabash-dry-van-hd), [Fontaine Trailer](https://www.renostrailer.com/product/2024-fontaine-qty10-infinity-53-combo-flatbed-wide-spread/), [TruckPaper](https://www.truckpaper.com/listings/for-sale/trailers/881) |
