# SKU Schema: Marine Vessels & Boats

**Last updated:** 2026-03-15
**Parent category:** Automotive & Vehicles

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | BW-230-OUT, GW-340-EXP, BAY-E18LE |
| Product Name | text | Full product name including manufacturer, model, and key variant | Boston Whaler 230 Outrage, Grady-White Express 340, Bayliner Element E18 |
| URL | text | Direct link to the product page | https://example.com/boats/230-outrage |
| Price | number | Numeric price per unit excluding currency symbol | 89500, 185000, 575000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD, SEK |
| Brand/Manufacturer | text | Boat manufacturer or builder name | Boston Whaler, Grady-White, Bayliner, Yamaha, Sea Ray, Beneteau |
| Model | text | Manufacturer model name or designation | 230 Outrage, Express 340, Element E18, 242 Center Console |
| Model Year | number | Model year of manufacture | 2023, 2024, 2025 |
| Condition | enum | Whether the vessel is new or used | New, Used, Certified Pre-Owned |
| Vessel Type | enum | Primary classification of the boat | Center Console, Bowrider, Cabin Cruiser, Sailboat, Pontoon, Catamaran, Trawler, Fishing Boat, Personal Watercraft, Yacht |
| Hull Type | enum | Hull configuration type | Monohull, Catamaran, Trimaran, Pontoon, Inflatable |
| Hull Material | enum | Primary material of hull construction | Fiberglass, Aluminum, Steel, Wood, Composite, Hypalon, PVC |
| Length Overall | number (ft) | Total length of the vessel from bow to stern | 18, 23, 34, 65 |
| Beam | number (ft-in) | Width of the vessel at the widest point | 6 ft 7 in, 8 ft 6 in, 11 ft 2 in |
| Draft | number (in) | Depth of hull below the waterline | 12, 18.5, 36, 48 |
| Air Draft | number (ft) | Height from waterline to the highest fixed point | 7, 9.1, 22 |
| Bridge Clearance | number (ft-in) | Height from waterline to the highest point requiring bridge clearance | 3 ft 6 in, 9 ft 1 in, 15 ft |
| Dry Weight | number (lb) | Weight of the vessel without engines, fuel, or water | 3800, 6500, 14200 |
| Displacement | number (lb) | Total weight of water displaced by the hull at full load | 5548, 12000, 28000 |
| Deadrise at Transom | number (deg) | Hull bottom angle at the transom, affecting ride quality | 17, 19, 21, 24 |
| Passenger Capacity | number | Maximum number of persons the vessel is rated to carry | 6, 10, 14, 20 |
| Maximum Weight Capacity | number (lb) | Maximum total load including passengers, gear, and fuel | 2100, 3100, 5500 |
| Fuel Capacity | number (gal) | Total fuel tank capacity | 13, 110, 200, 420 |
| Fuel Type | enum | Type of fuel the engine requires | Gasoline, Diesel, Electric |
| Freshwater Capacity | number (gal) | Onboard freshwater tank capacity | 0, 10, 30, 80 |
| Engine Brand | text | Engine manufacturer name | Mercury, Yamaha, Honda, Volvo Penta, Suzuki, Cummins |
| Engine Model | text | Specific engine model designation | Verado 300, F250XB, 6BTA 5.9, EVC D6-435 |
| Number of Engines | number | Count of installed or maximum engines | 1, 2, 3, 4 |
| Total Horsepower | number (hp) | Combined horsepower of all engines | 60, 300, 600, 1200 |
| Maximum Horsepower | number (hp) | Manufacturer-rated maximum engine power for the hull | 250, 500, 900 |
| Propulsion Type | enum | Type of propulsion system | Outboard, Inboard, Sterndrive, Jet Drive, Sail, Pod Drive, Electric |
| Maximum Speed | number (kn) | Top speed under optimal conditions | 25, 42, 55 |
| Engine Hours | number | Total accumulated engine running hours (used vessels) | 150, 520, 1200 |
| Cabins | number | Number of enclosed sleeping cabins | 0, 1, 2, 4 |
| Berths | number | Number of sleeping positions | 0, 2, 4, 6 |
| Heads | number | Number of onboard toilets or marine heads | 0, 1, 2 |
| Certification | text (list) | Regulatory and classification certifications | CE Category B, CE Category C, NMMA Certified, USCG, ABYC |
| Country of Origin | text | Country where the vessel was manufactured | USA, France, Italy, Japan, Australia, Taiwan |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (NMMA, ABYC, ISO 12217, CE Recreational Craft Directive) | [Boston Whaler](https://www.bostonwhaler.com/content/dam/boston-whaler/technical/spec-sheets/2023/Boston-Whaler-230-OUTRAGE.pdf), [Boat Trader](https://www.boattrader.com/boats/type-power/class-power-center/), [TheBoatDB](https://theboatdb.com/), [YachtBuyer Spec Guide](https://www.yachtbuyer.com/en-us/advice/first-time-boat-buyers-a-guide-to-boat-specifications) |
