# SKU Schema: Electric Vehicle Charging Equipment

**Last updated:** 2026-03-16
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.ev_charging`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or retailer stock-keeping unit code | MG11CET25, PLP-X-O-2-4-9-XX1, TAC-W22-G5-R-C-0, CPF50 |
| Product Name | product_name | text | Commercial product name as shown on pricelist or catalog | Pulsar Max 22kW, Terra AC Wallbox, Easee Charge, EV Portable Charger 16A 11kW |
| URL | url | text | Link to the product page or catalog listing | https://example.com/products/ev-charger-1 |
| Price | price | number | Retail or list price per unit, always paired with the Currency attribute | 149, 249, 695, 749, 7899 |
| Currency | currency | text | ISO 4217 currency code | EUR, USD, GBP, SEK |
| Charging Type | charging_type | enum | AC or DC charging classification per IEC or SAE standards | AC Level 2, DC Fast (Level 3), AC/DC Combo |
| Connector Type | connector_type | text | Physical plug or socket standard on the charger | Type 2, Type 1 (J1772), CCS1, CCS2, CHAdeMO, NACS (J3400), GB/T |
| Mounting Type | mounting_type | enum | How the unit is physically installed | Wall mount, Pedestal, Ground mount, Portable |
| Display Type | display_type | text | Type of user interface or indicator on the charger | None, LED ring, LCD, 7-inch touchscreen, 8-inch color touch |
| Country of Origin | country_of_origin | text | Country where the product is manufactured or assembled | China, Germany, Norway, Spain, USA |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| GTIN / EAN | gtin_ean | text | Global Trade Item Number or European Article Number barcode identifier | 4751050930033, 4751050930057 |
| Charging Power (kW) | charging_power_kw | number (kW) | Maximum output power in kilowatts | 3.7, 7.4, 11, 22, 50, 150, 350 |
| Rated Current (A) | rated_current_a | number (A) | Maximum output current in amperes | 16, 32, 50, 80, 125, 200 |
| Number of Phases | number_of_phases | enum | Electrical phase configuration for AC chargers | 1-phase, 3-phase |
| Cable Configuration | cable_configuration | enum | Whether the charger has a permanently attached cable or an untethered socket | Tethered, Socket, Socket with shutter |
| Number of Charging Ports | number_of_charging_ports | number | Number of simultaneous charging outputs on the unit | 1, 2 |
| Configurable Current Range | configurable_current_range | text | Range of selectable amperage settings, if the charger supports user-adjustable current | 6A-16A, 6A-32A, 8A-32A |
| Dimensions (H x W x D) | dimensions_h_x_w_x_d | text (mm) | Physical size of the unit | 198x201x99, 256x193x106, 770x584x294 |
| IP Rating | ip_rating | text | Ingress protection rating (dust and water resistance) | IP54, IP55, IP66, NEMA 3R |
| IK Rating | ik_rating | text | Impact resistance rating of the enclosure per IEC 62262 | IK08, IK10 |
| Operating Temperature | operating_temperature | text (deg C) | Permissible ambient temperature range for operation | -25C to +50C, -30C to +50C, -40C to +50C |
| Color | color | text | Available housing color options | White, Black, Anthracite, Dark Blue, Red |
| Charging Mode | charging_mode | enum | IEC 61851 charging mode classification | Mode 2, Mode 3, Mode 4 |
| Connectivity | connectivity | text (list) | Communication interfaces for remote management and monitoring | Wi-Fi, Bluetooth, Ethernet, 4G LTE, eSIM |
| Network Protocol | network_protocol | text | Backend communication standard for charge point management systems | OCPP 1.6, OCPP 2.0.1, OCPI |
| Weight | weight | number (kg) | Total weight of the charger unit excluding packaging | 1.5, 4, 8.5, 25, 120 |
| Cable Length | cable_length | number (m) | Length of the tethered charging cable, if applicable | 5, 7.5, 8, 10 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-16 | Added: Weight, Cable Length. Added Key column to all attribute tables. Deprecated: none. | [Schneider Electric - EVlink](https://www.se.com/us/en/product-range/61151-evlink-home-ev-charging-station/), [Ohme - Home Pro](https://ohme-ev.com/product/ohme-home-pro/) |
| 2026-03-15 | Migrated to core/extended format. Added Key column. | Migration script |
| 2026-03-14 | Split from combined energy-equipment-storage.md into per-subcategory file. 38 EV charging-specific attributes. | [Wallbox - Pulsar Max](https://wallbox.com), [ABB - Terra AC Wallbox](https://new.abb.com/ev-charging), [ChargePoint - CPF50](https://www.chargepoint.com), [Easee - Easee Charge](https://easee.com), [evcharge.lv](https://evcharge.lv) |
