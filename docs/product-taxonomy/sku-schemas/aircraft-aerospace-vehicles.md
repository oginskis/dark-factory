# SKU Schema: Aircraft & Aerospace Vehicles

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.aircraft_aerospace`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or listing identifier for the aircraft | CTL-5829341, TAP-2847612, GA-172SP-2025 |
| Product Name | product_name | text | — | yes | Full designation including manufacturer, model, and variant | Cessna 172SP Skyhawk, Diamond DA62, Piper M600 SLS, Beechcraft King Air 360 |
| URL | url | text | — | yes | Direct link to the listing or product page | https://example.com/aircraft/cessna-172sp |
| Price | price | number | — | yes | Numeric asking or list price excluding currency symbol | 89000, 465000, 1950000, 8500000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, BRL |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Aircraft Category | aircraft_category | enum | — | — | Primary classification of the aircraft | Single-Engine Piston, Multi-Engine Piston, Turboprop, Light Jet, Midsize Jet, Heavy Jet, Helicopter, Amphibian, Light Sport, Experimental |
| Fuel Type | fuel_type | enum | — | — | Required fuel type | Avgas 100LL, Jet-A, Jet-A1, JP-8, SAF Blend |
| Country of Origin | country_of_origin | text | — | — | Country where the aircraft was manufactured | USA, Austria, Brazil, Canada, France, Switzerland |
| Fuel Capacity | fuel_capacity | number | gal | — | Total usable fuel capacity | 49, 86.4, 122, 270 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Manufacturer | manufacturer | text | — | — | Aircraft manufacturer or OEM name | Cessna, Piper, Diamond, Beechcraft, Cirrus, Boeing, Airbus, Pilatus, Embraer |
| Model | model | text | — | — | Aircraft model name and designation | 172SP Skyhawk, DA62, M600 SLS, PC-12 NGX, Citation CJ4 |
| Model Year | model_year | number | — | — | Year of manufacture or model year | 1980, 2005, 2024, 2025 |
| Condition | condition | enum | — | — | Whether the aircraft is new or used | New, Used, Refurbished |
| Serial Number | serial_number | text | — | — | Factory-assigned airframe serial number | 17282456, 62.033, 4697582 |
| Registration Number | registration_number | text | — | — | National aviation authority registration (N-number, G-reg, etc.) | N172AB, G-DAJB, VH-ZXA |
| Total Time Airframe | total_time_airframe | number | hr | — | Total accumulated flight hours on the airframe since new | 1250, 3575, 4867, 12500 |
| Engine Make/Model | engine_makemodel | text | — | — | Engine manufacturer and model designation | Lycoming IO-360-L2A, Continental TSIO-550-C, Pratt and Whitney PT6A-42A, Austro Engine AE330 |
| Number of Engines | number_of_engines | number | — | — | Count of installed engines | 1, 2, 4 |
| Engine Horsepower | engine_horsepower | number | hp | — | Rated horsepower per engine | 180, 310, 600, 1200 |
| Engine Time SMOH | engine_time_smoh | number | hr | — | Engine hours since major overhaul | 50, 520, 1200, 2000 |
| Propeller Time SPOH | propeller_time_spoh | number | hr | — | Propeller hours since propeller overhaul | 100, 500, 1850 |
| TBO | tbo | number | hr | — | Manufacturer recommended time between overhauls | 1800, 2000, 3500 |
| Wingspan | wingspan | text | ft-in | — | Wingtip to wingtip measurement | 36 ft 1 in, 47 ft 9 in, 53 ft 4 in |
| Overall Height | overall_height | text | ft-in | — | Ground to highest point measurement | 8 ft 11 in, 9 ft 3 in, 14 ft 8 in |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 companies plus industry standards (FAA Type Certificate Data Sheets, EASA CS-23/25, ICAO Annex 8) | [Diamond Aircraft DA62](https://www.diamondaircraft.com/en/private-owners/aircraft/da62/tech-specs/), [Controller.com](https://www.controller.com/listings/for-sale/aircraft/all), [GlobalAir.com](https://www.globalair.com/aircraft-for-sale/specifications?specid=131), [Trade-A-Plane](https://www.trade-a-plane.com/search?make=CESSNA&model_group=CESSNA+172+SERIES&s-type=aircraft) |
