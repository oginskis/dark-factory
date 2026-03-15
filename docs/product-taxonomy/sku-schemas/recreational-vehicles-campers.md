# SKU Schema: Recreational Vehicles & Campers

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or dealer stock identifier | STK-71234, UNIT-CG260MLE |
| Product Name | text | Full product name including year, make, model, and floorplan | 2025 Keystone Cougar 260MLE, 2025 Winnebago View 24T, 2025 Airstream International 30RB |
| URL | text | Direct link to the product listing or specification page | https://example.com/rv/2025-keystone-cougar-260mle |
| Price | number | MSRP or listed sale price | 34500, 76763, 125000, 185000 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, AUD |
| Make | text | RV manufacturer or brand name | Keystone, Winnebago, Airstream, Forest River, Thor, Heartland, Jayco, Coachmen |
| Model | text | Model or product line name | Cougar, View, International, Rockwood, Minnie Winnie, Adventurer |
| Floorplan | text | Specific floorplan designation indicating layout | 260MLE, 24T, 30RB, 2500RL, 22MLS |
| Model Year | number | Production model year | 2024, 2025, 2026 |
| RV Type | enum | Broad recreational vehicle category | Travel Trailer, Fifth Wheel, Class A Motorhome, Class B Motorhome, Class C Motorhome, Truck Camper, Pop-Up/Folding Trailer, Toy Hauler |
| Overall Length | number (ft) | Total exterior length including hitch or tongue | 22.5, 29.5, 32.8, 36.0, 42.0 |
| Exterior Width | number (in) | Overall exterior width | 96, 100, 101, 102 |
| Exterior Height | number (in) | Overall exterior height from ground to top | 132, 140, 148, 152 |
| Interior Height | number (in) | Floor-to-ceiling height inside the main living area | 72, 78, 81, 84 |
| GVWR | number (lbs) | Gross Vehicle Weight Rating | 7500, 9000, 11000, 14200, 22000 |
| Dry Weight | number (lbs) | Unloaded vehicle weight as shipped from factory | 5200, 6150, 8893, 11000, 16500 |
| Payload Capacity | number (lbs) | Maximum cargo carrying capacity (GVWR minus dry weight) | 1500, 2107, 2800, 3500 |
| Hitch Weight | number (lbs) | Tongue or pin weight transferred to the tow vehicle (towable units) | 425, 680, 1200, 1630, 2200 |
| Tow Rating | number (lbs) | Maximum trailer weight this motorhome can tow | 3000, 3500, 5000, 10000 |
| GCWR | number (lbs) | Gross Combined Weight Rating (motorhomes) | 15000, 22000, 26000 |
| Chassis | text | Chassis or base vehicle platform (motorhomes) | Ford E-450, Mercedes-Benz 3500, Freightliner XCR, Ram ProMaster 3500 |
| Engine | text | Engine type and displacement (motorhomes) | 3.0L V6 Turbo Diesel, 6.8L V10, 7.3L V8, 6.7L Cummins Turbo Diesel |
| Sleeping Capacity | number | Maximum number of sleeping positions | 2, 3, 4, 6, 8, 10 |
| Number of Slide-Outs | number | Count of slide-out room extensions | 0, 1, 2, 3, 4 |
| Fresh Water Tank | number (gal) | Fresh water holding tank capacity | 30, 44, 54, 75, 100 |
| Gray Water Tank | number (gal) | Gray water (sink/shower) holding tank capacity | 30, 40, 60, 80 |
| Black Water Tank | number (gal) | Black water (toilet) holding tank capacity | 15, 30, 40, 50 |
| LP Gas Capacity | number (lbs) | Propane tank total capacity by weight | 20, 40, 60 |
| Fuel Tank Capacity | number (gal) | Vehicle fuel tank capacity (motorhomes) | 25, 44, 55, 80, 100 |
| Electrical System | text | Primary electrical configuration | 30 Amp, 50 Amp |
| Solar Pre-Wire | enum | Whether factory solar panel wiring is included | Standard, Optional, Not Available |
| Air Conditioning | text (BTU) | Roof-mounted AC unit capacity | 13500, 15000, 2x 13500, 2x 15000 |
| Awning Length | number (ft) | Power or manual awning length | 10, 14, 16, 18, 21 |
| Construction Type | text | Wall and roof construction method | Laminated Fiberglass, Aluminum Frame, Azdel Composite, Vacuum-Bonded |
| Tire Size | text | OEM tire specification | ST225/75R15, ST235/80R16, LT225/75R16 |
| Warranty (Structural) | text | Structural or frame warranty duration | 1 year, 3 years, 5 years limited, Lifetime |
| RVIA Seal | enum | Whether the unit bears an RVIA (RV Industry Association) compliance seal | Yes, No |
| Country of Assembly | text | Country where the RV was manufactured | USA, Canada |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 38 attributes from 4 sources plus RVIA standards | [Keystone RV Cougar Floorplans](https://www.keystonerv.com/product/cougar/premium-fifth-wheels/floorplans), [Winnebago View Specs](https://www.winnebago.com/models/product/specifications?ProductID=PROD396), [RVUSA Spec Guide](https://www.rvusa.com/rv-guide/specs-guide), [Price Digests RV Data](https://pricedigests.com/rv/) |
