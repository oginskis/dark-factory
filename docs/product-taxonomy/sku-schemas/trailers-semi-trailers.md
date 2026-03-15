# SKU Schema: Trailers & Semi-Trailers

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.trailers_semi_trailers`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | N124-BV, GD-CHP-53DV, WNI-HDVN-53 |
| Product Name | text | Full product name including trailer type, length, and key configuration | Great Dane Champion 53ft Dry Van, Fontaine Infinity 53ft Combo Flatbed, Wabash DuraPlate HD 53ft Dry Van |
| URL | text | Direct link to the product page | https://example.com/trailers/champion-53-dryvan |
| Price | number | Numeric price per unit excluding currency symbol | 42500, 68000, 125000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Trailer Type | enum | Primary functional category of the trailer | Dry Van, Refrigerated, Flatbed, Drop Deck, Lowboy, Dump, Tank, Enclosed, Curtainside, Chassis, Livestock |
| Suspension Type | enum | Type of suspension system | Air Ride, Mechanical Spring, Sliding |
| Floor Material | text | Material used for the trailer floor | Laminated Oak, Aluminum, Composite, Steel |
| Sidewall Material | text | Primary material of the sidewall construction | DuraPlate Composite, Sheet and Post, Aluminum, Steel, Fiberglass |
| Door Type | enum | Type of rear or side doors | Swing, Roll-Up, Side Door, Barn Door |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Brake Type | enum | Type of braking system installed | Drum, Disc, ABS 4S2M |
| Coupling Type | text | Fifth wheel coupling specification | 2 in Standard, 3-3/8 in SAE |
| Country of Origin | text | Country where the trailer was manufactured | USA, China, Germany, Mexico, India |
| Model | text | Manufacturer model name or series designation | Champion, DuraPlate HD, Infinity, Revolution, Everest |
| Year | number | Model year of manufacture | 2024, 2025, 2026 |
| Condition | enum | Whether the trailer is new or used | New, Used, Certified Pre-Owned |
| Overall Width | number (in) | Exterior width of the trailer | 96, 102 |
| Overall Height | number (ft-in) | Exterior height from ground to top of trailer | 13 ft 6 in, 13 ft 11 in |
| Interior Height Front | number (in) | Interior cargo height at the front wall | 108, 110.25 |
| Interior Height Rear | number (in) | Interior cargo height at the rear doors | 109, 111.25 |
| Interior Width | number (in) | Interior cargo width wall to wall | 98.5, 101 |
| GVWR | number (lb) | Gross Vehicle Weight Rating, the maximum allowable loaded weight | 68000, 80000, 105500 |
| GAWR | number (lb) | Gross Axle Weight Rating per axle assembly | 20000, 23000, 25000 |
| Frame Rating | number (lb) | Rated frame load capacity | 80000, 100000, 120000 |
| Floor Rating | number (lb) | Dynamic floor load rating for forklift operations | 16000, 20000, 24000, 28000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (TTMA, DOT FMVSS, NATM) | [Great Dane](https://greatdane.com/champion-dry-vans/), [Wabash National](https://ascendancetrucks.com/wabash-dry-van-hd), [Fontaine Trailer](https://www.renostrailer.com/product/2024-fontaine-qty10-infinity-53-combo-flatbed-wide-spread/), [TruckPaper](https://www.truckpaper.com/listings/for-sale/trailers/881) |
