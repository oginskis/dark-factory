# SKU Schema: Aircraft & Aerospace Vehicles

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or listing identifier for the aircraft | CTL-5829341, TAP-2847612, GA-172SP-2025 |
| Product Name | text | Full designation including manufacturer, model, and variant | Cessna 172SP Skyhawk, Diamond DA62, Piper M600 SLS, Beechcraft King Air 360 |
| URL | text | Direct link to the listing or product page | https://example.com/aircraft/cessna-172sp |
| Price | number | Numeric asking or list price excluding currency symbol | 89000, 465000, 1950000, 8500000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, BRL |
| Manufacturer | text | Aircraft manufacturer or OEM name | Cessna, Piper, Diamond, Beechcraft, Cirrus, Boeing, Airbus, Pilatus, Embraer |
| Model | text | Aircraft model name and designation | 172SP Skyhawk, DA62, M600 SLS, PC-12 NGX, Citation CJ4 |
| Model Year | number | Year of manufacture or model year | 1980, 2005, 2024, 2025 |
| Condition | enum | Whether the aircraft is new or used | New, Used, Refurbished |
| Aircraft Category | enum | Primary classification of the aircraft | Single-Engine Piston, Multi-Engine Piston, Turboprop, Light Jet, Midsize Jet, Heavy Jet, Helicopter, Amphibian, Light Sport, Experimental |
| Serial Number | text | Factory-assigned airframe serial number | 17282456, 62.033, 4697582 |
| Registration Number | text | National aviation authority registration (N-number, G-reg, etc.) | N172AB, G-DAJB, VH-ZXA |
| Total Time Airframe | number (hr) | Total accumulated flight hours on the airframe since new | 1250, 3575, 4867, 12500 |
| Engine Make/Model | text | Engine manufacturer and model designation | Lycoming IO-360-L2A, Continental TSIO-550-C, Pratt and Whitney PT6A-42A, Austro Engine AE330 |
| Number of Engines | number | Count of installed engines | 1, 2, 4 |
| Engine Horsepower | number (hp) | Rated horsepower per engine | 180, 310, 600, 1200 |
| Engine Time SMOH | number (hr) | Engine hours since major overhaul | 50, 520, 1200, 2000 |
| Propeller Time SPOH | number (hr) | Propeller hours since propeller overhaul | 100, 500, 1850 |
| TBO | number (hr) | Manufacturer recommended time between overhauls | 1800, 2000, 3500 |
| Fuel Type | enum | Required fuel type | Avgas 100LL, Jet-A, Jet-A1, JP-8, SAF Blend |
| Fuel Capacity | number (gal) | Total usable fuel capacity | 49, 86.4, 122, 270 |
| Wingspan | number (ft-in) | Wingtip to wingtip measurement | 36 ft 1 in, 47 ft 9 in, 53 ft 4 in |
| Overall Length | number (ft-in) | Nose to tail measurement | 27 ft 2 in, 30 ft 2 in, 48 ft 5 in |
| Overall Height | number (ft-in) | Ground to highest point measurement | 8 ft 11 in, 9 ft 3 in, 14 ft 8 in |
| Maximum Takeoff Weight | number (lb) | Maximum certified gross weight at takeoff | 2550, 5071, 12500, 73500 |
| Empty Weight | number (lb) | Equipped empty weight of the aircraft | 1680, 3523, 7800, 42000 |
| Useful Load | number (lb) | Maximum weight of fuel, passengers, baggage, and equipment | 870, 1055, 1545, 4500 |
| Maximum Cruise Speed | number (kn) | Maximum cruise speed at optimal altitude | 124, 180, 274, 460 |
| Range | number (nm) | Maximum range at economy cruise with full fuel | 640, 1288, 1406, 2850 |
| Service Ceiling | number (ft) | Maximum certified operating altitude | 14000, 20000, 30000, 45000 |
| Rate of Climb | number (ft/min) | Maximum rate of climb at sea level | 730, 1028, 1580, 3000 |
| Seating Capacity | number | Maximum number of seats including crew | 4, 5, 7, 9, 19 |
| Avionics Suite | text | Primary avionics package installed | Garmin G1000 NXi, Garmin G3000, Avidyne IFD540, Collins Pro Line Fusion |
| IFR Certified | boolean | Whether the aircraft is certified for instrument flight | Yes, No |
| Pressurized | boolean | Whether the cabin is pressurized | Yes, No |
| Annual Inspection Status | text | Date or status of most recent annual inspection | January 2026, Fresh Annual, Due June 2026 |
| Certification Basis | text (list) | Applicable type certificate and airworthiness standards | FAA Part 23, FAA Part 25, EASA CS-23, EASA CS-25, ICAO Annex 8 |
| Country of Origin | text | Country where the aircraft was manufactured | USA, Austria, Brazil, Canada, France, Switzerland |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus industry standards (FAA Type Certificate Data Sheets, EASA CS-23/25, ICAO Annex 8) | [Diamond Aircraft DA62](https://www.diamondaircraft.com/en/private-owners/aircraft/da62/tech-specs/), [Controller.com](https://www.controller.com/listings/for-sale/aircraft/all), [GlobalAir.com](https://www.globalair.com/aircraft-for-sale/specifications?specid=131), [Trade-A-Plane](https://www.trade-a-plane.com/search?make=CESSNA&model_group=CESSNA+172+SERIES&s-type=aircraft) |
