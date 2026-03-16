# SKU Schema: Electrical Wiring Devices & Conduit

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics
**Taxonomy ID:** `construction.electrical_wiring_conduit`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | LEV-5320-WMP, HBL-5362I, CAN-A40AEB |
| Product Name | product_name | text | — | Full product name including key specs such as device type, rating, and color | Leviton 20A 125V Duplex Receptacle White, Hubbell Snap-Connect 15A Toggle Switch, Cantex Schedule 40 PVC Conduit 1in x 10ft |
| URL | url | text | — | Direct link to the product page | https://example.com/product/20a-duplex-receptacle |
| Price | price | number | — | Numeric price per unit, excluding currency symbol | 1.29, 4.75, 12.99, 38.50 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Category | product_category | enum | — | General product category | Receptacle, Switch, Conduit, Conduit Fitting, Wall Plate, Junction Box, Outlet Box, Wire Connector, GFCI, AFCI, Dimmer |
| Device Type | device_type | text | — | Specific device variant within the category | Duplex Receptacle, Toggle Switch, Decora Switch, GFCI Outlet, USB Receptacle, EMT Coupling, PVC Elbow, Weatherproof Box |
| Grounding Type | grounding_type | enum | — | Grounding configuration of the device | Self-Grounding, Equipment Ground, Isolated Ground, Non-Grounding |
| Conduit Material | conduit_material | enum | — | Material of the conduit (conduit products only) | Steel, Aluminum, PVC, HDPE, Liquid-Tight Flexible, Galvanized Steel |
| Conduit Type | conduit_type | text | — | Classification of the conduit product | EMT, IMC, Rigid Metal (RMC), Schedule 40 PVC, Schedule 80 PVC, Flexible, Liquid-Tight |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Housing Material | housing_material | text | — | Body or housing material of the device | Nylon, Thermoplastic, Polycarbonate, Steel, Stainless Steel, Die-Cast Zinc |
| Mounting Type | mounting_type | text | — | How the device is installed | Flush, Surface, DIN Rail, Snap-In, Screw Terminal, Push-In |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | USA, Mexico, China, Canada |
| Amperage Rating | amperage_rating | number | A | Maximum current rating of the device | 15, 20, 30, 50, 60, 100 |
| NEMA Configuration | nema_configuration | text | — | NEMA plug and receptacle configuration code | 5-15R, 5-20R, 6-20R, 6-50R, L5-30R, L14-30R, 14-50R |
| Number of Poles | number_of_poles | number | — | Number of electrical poles in the device | 2, 3, 4 |
| Number of Wires | number_of_wires | number | — | Number of wires the device accommodates | 2, 3, 4, 5 |
| Wall Thickness | wall_thickness | number | mm | Conduit wall thickness | 1.07, 1.24, 1.45, 1.65, 1.80, 2.05, 2.41, 3.18 |
| Color | color | text | — | Color of the device or conduit | White, Ivory, Gray, Black, Brown, Almond, Light Almond, Red, Blue, Orange |
| Wire Gauge Range | wire_gauge_range | text | — | Compatible conductor sizes | 14-10 AWG, 12-8 AWG, 8-2 AWG |
| IP Rating | ip_rating | text | — | Ingress protection rating for outdoor or industrial devices | IP20, IP44, IP55, IP66, IP67 |
| UL Listing | ul_listing | text | — | UL standard the product is listed under | UL 498, UL 20, UL 514A, UL 651, UL 797, UL 1242 |
| Certification | certification | text (list) | — | Safety and compliance certifications | UL, CSA, NEC, CE, NEMA, ETL |
| Application | application | text (list) | — | Intended installation environments | Residential, Commercial, Industrial, Hospital Grade, Hazardous Location, Outdoor, Underground |
| Voltage Rating | voltage_rating | number | V | Maximum voltage rating of the device | 120, 125, 250, 277, 347, 480, 600 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus NEC/NEMA standards and UL listing categories | [Hubbell Wiring Devices](https://www.hubbell.com/wiringdevice-kellems/en/wiring-devices), [Cantex](https://www.cantexinc.com/products/conduit-pipe/), [Wheatland Tube](https://www.westerntube.com/), [American Fittings](https://amftgs.com/rigid-imc-and-emt-conduit-size-chart-info-on-steel-conduit/) |
