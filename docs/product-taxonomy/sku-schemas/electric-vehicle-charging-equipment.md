# SKU Schema: Electric Vehicle Charging Equipment

**Last updated:** 2026-03-14
**Parent category:** Energy Equipment & Storage

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer stock-keeping unit code | MG11CET25, PLP-X-O-2-4-9-XX1, TAC-W22-G5-R-C-0, CPF50 |
| Product Name | text | Commercial product name as shown on pricelist or catalog | Pulsar Max 22kW, Terra AC Wallbox, Easee Charge, EV Portable Charger 16A 11kW |
| URL | text | Link to the product page or catalog listing | https://example.com/products/ev-charger-1 |
| Price | number | Retail or list price per unit, always paired with the Currency attribute | 149, 249, 695, 749, 7899 |
| Currency | text | ISO 4217 currency code | EUR, USD, GBP, SEK |
| GTIN / EAN | text | Global Trade Item Number or European Article Number barcode identifier | 4751050930033, 4751050930057 |
| Brand | text | Manufacturer or brand name | Wallbox, ABB, ChargePoint, Easee, Zaptec, Blaupunkt |
| Charging Power (kW) | number (kW) | Maximum output power in kilowatts | 3.7, 7.4, 11, 22, 50, 150, 350 |
| Rated Current (A) | number (A) | Maximum output current in amperes | 16, 32, 50, 80, 125, 200 |
| Rated Voltage (V) | text | Input or output voltage rating, may be a range for DC chargers | 230V, 400V, 208-240V, 150-1000V DC |
| Number of Phases | enum | Electrical phase configuration for AC chargers | 1-phase, 3-phase |
| Charging Type | enum | AC or DC charging classification per IEC or SAE standards | AC Level 2, DC Fast (Level 3), AC/DC Combo |
| Connector Type | text | Physical plug or socket standard on the charger | Type 2, Type 1 (J1772), CCS1, CCS2, CHAdeMO, NACS (J3400), GB/T |
| Cable Configuration | enum | Whether the charger has a permanently attached cable or an untethered socket | Tethered, Socket, Socket with shutter |
| Cable Length (m) | number (m) | Length of the attached charging cable, if tethered | 5, 7, 7.5, 8 |
| Number of Charging Ports | number | Number of simultaneous charging outputs on the unit | 1, 2 |
| Configurable Current Range | text | Range of selectable amperage settings, if the charger supports user-adjustable current | 6A-16A, 6A-32A, 8A-32A |
| Mounting Type | enum | How the unit is physically installed | Wall mount, Pedestal, Ground mount, Portable |
| Dimensions (H x W x D) | text (mm) | Physical size of the unit | 198x201x99, 256x193x106, 770x584x294 |
| Weight (kg) | number (kg) | Unit weight | 1.3, 1.5, 3.5, 6.0, 60 |
| IP Rating | text | Ingress protection rating (dust and water resistance) | IP54, IP55, IP66, NEMA 3R |
| IK Rating | text | Impact resistance rating of the enclosure per IEC 62262 | IK08, IK10 |
| Operating Temperature | text (deg C) | Permissible ambient temperature range for operation | -25C to +50C, -30C to +50C, -40C to +50C |
| Color | text | Available housing color options | White, Black, Anthracite, Dark Blue, Red |
| Charging Mode | enum | IEC 61851 charging mode classification | Mode 2, Mode 3, Mode 4 |
| Display Type | text | Type of user interface or indicator on the charger | None, LED ring, LCD, 7-inch touchscreen, 8-inch color touch |
| Connectivity | text (list) | Communication interfaces for remote management and monitoring | Wi-Fi, Bluetooth, Ethernet, 4G LTE, eSIM |
| Network Protocol | text | Backend communication standard for charge point management systems | OCPP 1.6, OCPP 2.0.1, OCPI |
| Authentication Methods | text (list) | User identification capabilities supported by the charger | RFID, NFC, App, PIN code, Plug and Charge (ISO 15118), Autostart |
| Payment Capability | text | On-device payment options, if any | None, EMV contactless, Credit card chip reader |
| Residual Current Protection | text | Built-in RCD or leakage protection type and rating | 6mA DC (RDC-DD), Type A 30mA AC, Type B, None (external required) |
| Energy Meter | text | Built-in energy metering capability and accuracy class | None, Integrated (+/-2%), MID Class B (+/-1%) |
| Load Management | text | Power sharing or load balancing capability for multi-charger installations | None, Static, Dynamic, Phase balancing |
| Certifications | text (list) | International safety and performance certifications | IEC 61851-1, CE, UL 2594, ENERGY STAR, MID, UKCA |
| Application / Market Segment | enum | Target market segment the charger is designed for | Residential, Commercial, Fleet, Semi-public, Public |
| Warranty (years) | number (years) | Manufacturer warranty period | 2, 3, 5 |
| Compatible Vehicles | text (list) | EV brands or connector standards the charger is compatible with | All Type 2 EVs, All CCS2 EVs, Tesla (with adapter) |
| Country of Origin | text | Country where the product is manufactured or assembled | China, Germany, Norway, Spain, USA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-14 | Split from combined energy-equipment-storage.md into per-subcategory file. 38 EV charging-specific attributes. | [Wallbox - Pulsar Max](https://wallbox.com), [ABB - Terra AC Wallbox](https://new.abb.com/ev-charging), [ChargePoint - CPF50](https://www.chargepoint.com), [Easee - Easee Charge](https://easee.com), [evcharge.lv](https://evcharge.lv) |
