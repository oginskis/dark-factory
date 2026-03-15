# SKU Schema: Recreational Vehicles & Campers

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.recreational_vehicles_campers`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or dealer stock identifier | STK-71234, UNIT-CG260MLE |
| Product Name | text | Full product name including year, make, model, and floorplan | 2025 Keystone Cougar 260MLE, 2025 Winnebago View 24T, 2025 Airstream International 30RB |
| URL | text | Direct link to the product listing or specification page | https://example.com/rv/2025-keystone-cougar-260mle |
| Price | number | MSRP or listed sale price | 34500, 76763, 125000, 185000 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, AUD |
| RV Type | enum | Broad recreational vehicle category | Travel Trailer, Fifth Wheel, Class A Motorhome, Class B Motorhome, Class C Motorhome, Truck Camper, Pop-Up/Folding Trailer, Toy Hauler |
| Construction Type | text | Wall and roof construction method | Laminated Fiberglass, Aluminum Frame, Azdel Composite, Vacuum-Bonded |
| Overall Length | number (ft) | Total exterior length including hitch or tongue | 22.5, 29.5, 32.8, 36.0, 42.0 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Make | text | RV manufacturer or brand name | Keystone, Winnebago, Airstream, Forest River, Thor, Heartland, Jayco, Coachmen |
| Model | text | Model or product line name | Cougar, View, International, Rockwood, Minnie Winnie, Adventurer |
| Floorplan | text | Specific floorplan designation indicating layout | 260MLE, 24T, 30RB, 2500RL, 22MLS |
| Model Year | number | Production model year | 2024, 2025, 2026 |
| Exterior Width | number (in) | Overall exterior width | 96, 100, 101, 102 |
| Exterior Height | number (in) | Overall exterior height from ground to top | 132, 140, 148, 152 |
| Interior Height | number (in) | Floor-to-ceiling height inside the main living area | 72, 78, 81, 84 |
| GVWR | number (lbs) | Gross Vehicle Weight Rating | 7500, 9000, 11000, 14200, 22000 |
| Tow Rating | number (lbs) | Maximum trailer weight this motorhome can tow | 3000, 3500, 5000, 10000 |
| GCWR | number (lbs) | Gross Combined Weight Rating (motorhomes) | 15000, 22000, 26000 |
| Chassis | text | Chassis or base vehicle platform (motorhomes) | Ford E-450, Mercedes-Benz 3500, Freightliner XCR, Ram ProMaster 3500 |
| Engine | text | Engine type and displacement (motorhomes) | 3.0L V6 Turbo Diesel, 6.8L V10, 7.3L V8, 6.7L Cummins Turbo Diesel |
| Number of Slide-Outs | number | Count of slide-out room extensions | 0, 1, 2, 3, 4 |
| Fresh Water Tank | number (gal) | Fresh water holding tank capacity | 30, 44, 54, 75, 100 |
| Gray Water Tank | number (gal) | Gray water (sink/shower) holding tank capacity | 30, 40, 60, 80 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 sources plus RVIA standards | [Keystone RV Cougar Floorplans](https://www.keystonerv.com/product/cougar/premium-fifth-wheels/floorplans), [Winnebago View Specs](https://www.winnebago.com/models/product/specifications?ProductID=PROD396), [RVUSA Spec Guide](https://www.rvusa.com/rv-guide/specs-guide), [Price Digests RV Data](https://pricedigests.com/rv/) |
