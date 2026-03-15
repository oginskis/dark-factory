# SKU Schema: Electrical Wiring Devices & Conduit

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | LEV-5320-WMP, HBL-5362I, CAN-A40AEB |
| Product Name | text | Full product name including key specs such as device type, rating, and color | Leviton 20A 125V Duplex Receptacle White, Hubbell Snap-Connect 15A Toggle Switch, Cantex Schedule 40 PVC Conduit 1in x 10ft |
| URL | text | Direct link to the product page | https://example.com/product/20a-duplex-receptacle |
| Price | number | Numeric price per unit, excluding currency symbol | 1.29, 4.75, 12.99, 38.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand | text | Manufacturer or brand name | Leviton, Hubbell, Eaton, Legrand, Pass and Seymour, Cantex, Carlon, Wheatland |
| Product Category | enum | General product category | Receptacle, Switch, Conduit, Conduit Fitting, Wall Plate, Junction Box, Outlet Box, Wire Connector, GFCI, AFCI, Dimmer |
| Device Type | text | Specific device variant within the category | Duplex Receptacle, Toggle Switch, Decora Switch, GFCI Outlet, USB Receptacle, EMT Coupling, PVC Elbow, Weatherproof Box |
| Amperage Rating | number (A) | Maximum current rating of the device | 15, 20, 30, 50, 60, 100 |
| Voltage Rating | number (V) | Maximum voltage rating of the device | 120, 125, 250, 277, 347, 480, 600 |
| NEMA Configuration | text | NEMA plug and receptacle configuration code | 5-15R, 5-20R, 6-20R, 6-50R, L5-30R, L14-30R, 14-50R |
| Number of Poles | number | Number of electrical poles in the device | 2, 3, 4 |
| Number of Wires | number | Number of wires the device accommodates | 2, 3, 4, 5 |
| Grounding Type | enum | Grounding configuration of the device | Self-Grounding, Equipment Ground, Isolated Ground, Non-Grounding |
| Conduit Material | enum | Material of the conduit (conduit products only) | Steel, Aluminum, PVC, HDPE, Liquid-Tight Flexible, Galvanized Steel |
| Conduit Type | text | Classification of the conduit product | EMT, IMC, Rigid Metal (RMC), Schedule 40 PVC, Schedule 80 PVC, Flexible, Liquid-Tight |
| Trade Size | text | Nominal conduit trade size | 1/2, 3/4, 1, 1-1/4, 1-1/2, 2, 2-1/2, 3, 4 |
| Inner Diameter | number (mm) | Actual internal diameter of the conduit | 15.8, 20.9, 26.6, 35.1, 40.9, 52.5, 62.7, 78.0, 102.3 |
| Outer Diameter | number (mm) | Actual external diameter of the conduit | 17.9, 23.4, 29.5, 37.6, 42.2, 53.8, 64.9, 82.3, 106.2 |
| Wall Thickness | number (mm) | Conduit wall thickness | 1.07, 1.24, 1.45, 1.65, 1.80, 2.05, 2.41, 3.18 |
| Length | number (m) | Standard length of conduit stick | 3.05, 6.10 |
| Weight per Metre | number (kg/m) | Linear weight of conduit | 0.42, 0.71, 1.00, 1.50, 2.26, 3.41, 5.32 |
| Color | text | Color of the device or conduit | White, Ivory, Gray, Black, Brown, Almond, Light Almond, Red, Blue, Orange |
| Housing Material | text | Body or housing material of the device | Nylon, Thermoplastic, Polycarbonate, Steel, Stainless Steel, Die-Cast Zinc |
| Wire Gauge Range | text | Compatible conductor sizes | 14-10 AWG, 12-8 AWG, 8-2 AWG |
| IP Rating | text | Ingress protection rating for outdoor or industrial devices | IP20, IP44, IP55, IP66, IP67 |
| Mounting Type | text | How the device is installed | Flush, Surface, DIN Rail, Snap-In, Screw Terminal, Push-In |
| UL Listing | text | UL standard the product is listed under | UL 498, UL 20, UL 514A, UL 651, UL 797, UL 1242 |
| Certification | text (list) | Safety and compliance certifications | UL, CSA, NEC, CE, NEMA, ETL |
| Country of Origin | text | Country where the product was manufactured | USA, Mexico, China, Canada |
| Application | text (list) | Intended installation environments | Residential, Commercial, Industrial, Hospital Grade, Hazardous Location, Outdoor, Underground |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus NEC/NEMA standards and UL listing categories | [Hubbell Wiring Devices](https://www.hubbell.com/wiringdevice-kellems/en/wiring-devices), [Cantex](https://www.cantexinc.com/products/conduit-pipe/), [Wheatland Tube](https://www.westerntube.com/), [American Fittings](https://amftgs.com/rigid-imc-and-emt-conduit-size-chart-info-on-steel-conduit/) |
