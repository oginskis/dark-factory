# SKU Schema: Marine Vessels & Boats

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles
**Taxonomy ID:** `automotive.marine_vessels_boats`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | BW-230-OUT, GW-340-EXP, BAY-E18LE |
| Product Name | product_name | text | — | yes | Full product name including manufacturer, model, and key variant | Boston Whaler 230 Outrage, Grady-White Express 340, Bayliner Element E18 |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/boats/230-outrage |
| Price | price | number | — | yes | Numeric price per unit excluding currency symbol | 89500, 185000, 575000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, AUD, SEK |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Vessel Type | vessel_type | enum | — | — | Primary classification of the boat | Center Console, Bowrider, Cabin Cruiser, Sailboat, Pontoon, Catamaran, Trawler, Fishing Boat, Personal Watercraft, Yacht |
| Hull Type | hull_type | enum | — | — | Hull configuration type | Monohull, Catamaran, Trimaran, Pontoon, Inflatable |
| Hull Material | hull_material | enum | — | — | Primary material of hull construction | Fiberglass, Aluminum, Steel, Wood, Composite, Hypalon, PVC |
| Fuel Type | fuel_type | enum | — | — | Type of fuel the engine requires | Gasoline, Diesel, Electric |
| Propulsion Type | propulsion_type | enum | — | — | Type of propulsion system | Outboard, Inboard, Sterndrive, Jet Drive, Sail, Pod Drive, Electric |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the vessel was manufactured | USA, France, Italy, Japan, Australia, Taiwan |
| Model | model | text | — | — | Manufacturer model name or designation | 230 Outrage, Express 340, Element E18, 242 Center Console |
| Model Year | model_year | number | — | — | Model year of manufacture | 2023, 2024, 2025 |
| Condition | condition | enum | — | — | Whether the vessel is new or used | New, Used, Certified Pre-Owned |
| Beam | beam | number | ft-in | — | Width of the vessel at the widest point | 6 ft 7 in, 8 ft 6 in, 11 ft 2 in |
| Draft | draft | number | in | — | Depth of hull below the waterline | 12, 18.5, 36, 48 |
| Air Draft | air_draft | number | ft | — | Height from waterline to the highest fixed point | 7, 9.1, 22 |
| Bridge Clearance | bridge_clearance | number | ft-in | — | Height from waterline to the highest point requiring bridge clearance | 3 ft 6 in, 9 ft 1 in, 15 ft |
| Displacement | displacement | number | lb | — | Total weight of water displaced by the hull at full load | 5548, 12000, 28000 |
| Deadrise at Transom | deadrise_at_transom | number | deg | — | Hull bottom angle at the transom, affecting ride quality | 17, 19, 21, 24 |
| Engine Brand | engine_brand | text | — | — | Engine manufacturer name | Mercury, Yamaha, Honda, Volvo Penta, Suzuki, Cummins |
| Engine Model | engine_model | text | — | — | Specific engine model designation | Verado 300, F250XB, 6BTA 5.9, EVC D6-435 |
| Number of Engines | number_of_engines | number | — | — | Count of installed or maximum engines | 1, 2, 3, 4 |
| Total Horsepower | total_horsepower | number | hp | — | Combined horsepower of all engines | 60, 300, 600, 1200 |
| Maximum Horsepower | maximum_horsepower | number | hp | — | Manufacturer-rated maximum engine power for the hull | 250, 500, 900 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (NMMA, ABYC, ISO 12217, CE Recreational Craft Directive) | [Boston Whaler](https://www.bostonwhaler.com/content/dam/boston-whaler/technical/spec-sheets/2023/Boston-Whaler-230-OUTRAGE.pdf), [Boat Trader](https://www.boattrader.com/boats/type-power/class-power-center/), [TheBoatDB](https://theboatdb.com/), [YachtBuyer Spec Guide](https://www.yachtbuyer.com/en-us/advice/first-time-boat-buyers-a-guide-to-boat-specifications) |
