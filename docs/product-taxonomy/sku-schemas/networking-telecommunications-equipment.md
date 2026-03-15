# SKU Schema: Networking & Telecommunications Equipment

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | C9200L-24P-4G-E, R650, UAP-AC-PRO, TL-SG1024 |
| Product Name | text | Full product name including brand, model, port count, and speed tier | Cisco Catalyst 9200L 24-Port PoE+ 4x1G Switch, Ubiquiti UniFi 6 Long-Range Access Point |
| URL | text | Direct link to the product page | https://example.com/product/c9200l-24p-4g |
| Price | number | Numeric unit price excluding currency symbol | 149.99, 2895.00, 8750.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand | text | Equipment manufacturer | Cisco, Juniper, Aruba, Ubiquiti, TP-Link, Netgear, Fortinet, Ruckus, MikroTik |
| Product Type | enum | Primary equipment category | Switch, Router, Wireless Access Point, Firewall, Load Balancer, Media Converter, VoIP Gateway, Network Controller |
| Model Number | text | Manufacturer model or series identifier | C9200L-24P-4G-E, ISR4331, FortiGate-60F, EAP670 |
| Management Type | enum | Level of configuration and monitoring capability | Managed, Unmanaged, Smart Managed, Cloud Managed |
| Total Ports | number | Total number of network access ports | 5, 8, 16, 24, 48, 52 |
| Port Speed | text | Maximum speed of the primary downlink ports | 100 Mbps, 1 Gbps, 2.5 Gbps, 5 Gbps, 10 Gbps, 25 Gbps |
| Port Type | text | Physical connector type of the primary ports | RJ-45, SFP, SFP+, SFP28, QSFP+, QSFP28 |
| Uplink Ports | text | Number and type of uplink ports | 4x 1G SFP, 2x 10G SFP+, 4x 25G SFP28 |
| PoE Support | enum | Power over Ethernet capability | None, PoE (802.3af), PoE+ (802.3at), PoE++ (802.3bt) |
| PoE Budget | number (W) | Maximum power available for PoE devices | 60, 150, 370, 740, 1440 |
| Switching Capacity | number (Gbps) | Total backplane throughput | 16, 56, 128, 176, 400 |
| Forwarding Rate | number (Mpps) | Packet forwarding performance in million packets per second | 2.38, 14.88, 95.23, 297.61 |
| Layer Support | enum | OSI layer at which the device operates | Layer 2, Layer 2/3, Layer 3, Layer 4-7 |
| Wi-Fi Standard | text | Wireless standard supported (access points and routers) | Wi-Fi 5 (802.11ac), Wi-Fi 6 (802.11ax), Wi-Fi 6E, Wi-Fi 7 (802.11be) |
| Wireless Data Rate | text | Maximum aggregate wireless throughput | AC1200, AX3600, AX6000, BE30000 |
| Frequency Bands | enum | Radio frequency bands supported | Single Band, Dual Band, Tri-Band, Quad Band |
| WAN Ports | text | Wide area network port count and speed | 1x 1 Gbps RJ-45, 2x 10 Gbps SFP+ |
| Stackable | boolean | Whether the device supports hardware stacking with other units | true, false |
| Stacking Bandwidth | number (Gbps) | Maximum bandwidth when stacked with other units | 40, 80, 160, 480 |
| MAC Address Table | number | Maximum number of MAC addresses the device can learn | 8000, 16000, 32000, 128000 |
| Rack Mountable | boolean | Whether the device fits a standard 19-inch equipment rack | true, false |
| Form Factor | text | Physical chassis design | Desktop, 1U Rack, 2U Rack, Wall Mount, Ceiling Mount, DIN Rail |
| Height | number (mm) | Chassis height | 26, 44, 88 |
| Width | number (mm) | Chassis width | 209, 330, 445 |
| Depth | number (mm) | Chassis depth | 131, 257, 350 |
| Weight | number (kg) | Device weight without accessories | 0.35, 0.85, 3.60, 5.00, 8.20 |
| Power Consumption | number (W) | Maximum power draw under full load | 12, 45, 125, 600, 1000 |
| Input Voltage | text | Acceptable power input range | 100-240 VAC, 12V DC, -48V DC |
| Redundant Power | boolean | Whether the device supports dual or redundant power supplies | true, false |
| Operating Temperature | text | Allowable ambient temperature range during operation | 0 to 45 C, -5 to 50 C, -40 to 70 C |
| MTBF | number (hours) | Mean time between failures | 250000, 587800, 1000000 |
| Security Protocols | text (list) | Supported network security standards | WPA3, 802.1X, MACsec, IPSec, SSL VPN |
| Certifications | text (list) | Regulatory and safety certifications | CE, FCC, UL, RoHS, ENERGY STAR |
| Warranty | text | Manufacturer warranty duration | 1 Year, 3 Years, 5 Years, Limited Lifetime |
| Country of Origin | text | Country where the device was manufactured | China, Taiwan, USA, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus IEEE 802.3/802.11 standards | [Cisco Catalyst 9200 Datasheet](https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-9200-series-switches/nb-06-cat9200-ser-data-sheet-cte-en.html), [Newegg Network Switches](https://www.newegg.com/switches/subcategory/id-30), [Newegg Wireless Routers](https://www.newegg.com/Wireless-Routers/SubCategory/ID-145), [Ubiquiti UniFi Products](https://www.ui.com/wifi) |
