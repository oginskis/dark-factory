# SKU Schema: Trailers & Semi-Trailers

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | N124-BV, GD-CHP-53DV, WNI-HDVN-53 |
| Product Name | text | Full product name including trailer type, length, and key configuration | Great Dane Champion 53ft Dry Van, Fontaine Infinity 53ft Combo Flatbed, Wabash DuraPlate HD 53ft Dry Van |
| URL | text | Direct link to the product page | https://example.com/trailers/champion-53-dryvan |
| Price | number | Numeric price per unit excluding currency symbol | 42500, 68000, 125000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Trailer manufacturer or brand name | Great Dane, Wabash National, Fontaine, Utility Trailer, Hyundai Translead, Schmitz Cargobull |
| Model | text | Manufacturer model name or series designation | Champion, DuraPlate HD, Infinity, Revolution, Everest |
| Year | number | Model year of manufacture | 2024, 2025, 2026 |
| Condition | enum | Whether the trailer is new or used | New, Used, Certified Pre-Owned |
| Trailer Type | enum | Primary functional category of the trailer | Dry Van, Refrigerated, Flatbed, Drop Deck, Lowboy, Dump, Tank, Enclosed, Curtainside, Chassis, Livestock |
| Body Length | number (ft) | Overall length of the trailer body | 28, 40, 45, 48, 53 |
| Overall Width | number (in) | Exterior width of the trailer | 96, 102 |
| Overall Height | number (ft-in) | Exterior height from ground to top of trailer | 13 ft 6 in, 13 ft 11 in |
| Interior Height Front | number (in) | Interior cargo height at the front wall | 108, 110.25 |
| Interior Height Rear | number (in) | Interior cargo height at the rear doors | 109, 111.25 |
| Interior Width | number (in) | Interior cargo width wall to wall | 98.5, 101 |
| GVWR | number (lb) | Gross Vehicle Weight Rating, the maximum allowable loaded weight | 68000, 80000, 105500 |
| GAWR | number (lb) | Gross Axle Weight Rating per axle assembly | 20000, 23000, 25000 |
| Empty Weight | number (lb) | Tare weight of the trailer without cargo | 10836, 12500, 15200 |
| Payload Capacity | number (lb) | Maximum cargo weight (GVWR minus empty weight) | 45000, 48000, 55000 |
| Frame Rating | number (lb) | Rated frame load capacity | 80000, 100000, 120000 |
| Floor Rating | number (lb) | Dynamic floor load rating for forklift operations | 16000, 20000, 24000, 28000 |
| Axle Configuration | enum | Number and arrangement of axles | Single, Tandem, Tridem, Spread Tandem |
| Axle Spacing | text (in) | Distance between axles in the axle group | 49, 60, 72, 121, 122 |
| Suspension Type | enum | Type of suspension system | Air Ride, Mechanical Spring, Sliding |
| King Pin Setting | number (in) | Distance from the nose of the trailer to the king pin centerline | 24, 30, 36 |
| Floor Material | text | Material used for the trailer floor | Laminated Oak, Aluminum, Composite, Steel |
| Sidewall Material | text | Primary material of the sidewall construction | DuraPlate Composite, Sheet and Post, Aluminum, Steel, Fiberglass |
| Door Type | enum | Type of rear or side doors | Swing, Roll-Up, Side Door, Barn Door |
| Refrigeration Unit | text | Make and model of reefer unit for refrigerated trailers | Carrier X4 7500, Thermo King S-700, Carrier Vector 8611MT |
| Temperature Range | text (deg F) | Operating temperature range for refrigerated trailers | -20 to 80, 0 to 65 |
| Tire Size | text | Tire specification designation | 295/75R22.5, 11R22.5, 255/70R22.5 |
| Brake Type | enum | Type of braking system installed | Drum, Disc, ABS 4S2M |
| Lighting | enum | Type of lighting system installed | All LED, Incandescent, LED/Incandescent Combination |
| Coupling Type | text | Fifth wheel coupling specification | 2 in Standard, 3-3/8 in SAE |
| Telematics | text | Integrated tracking or telematics system | FleetPulse, Spireon, SkyBitz, None |
| Certification | text (list) | Regulatory and safety certifications | DOT, TTMA, SmartWay, ISO 9001, CARB |
| Country of Origin | text | Country where the trailer was manufactured | USA, China, Germany, Mexico, India |
| Warranty | text | Summary of manufacturer warranty coverage | 5-Year Limited, 10-Year Sidewall, 2-Year Bumper-to-Bumper |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus industry standards (TTMA, DOT FMVSS, NATM) | [Great Dane](https://greatdane.com/champion-dry-vans/), [Wabash National](https://ascendancetrucks.com/wabash-dry-van-hd), [Fontaine Trailer](https://www.renostrailer.com/product/2024-fontaine-qty10-infinity-53-combo-flatbed-wide-spread/), [TruckPaper](https://www.truckpaper.com/listings/for-sale/trailers/881) |
