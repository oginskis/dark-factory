# SKU Schema: Printed Circuit Boards & Electronic Components

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.pcbs_electronic_components`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer, manufacturer, or distributor product identifier | PCB-FR4-2L-1.6, CAP-0805-100NF, CON-USB-C-SMT |
| Product Name | text | Full product name including key specs such as component type, value, and package | FR-4 Double-Sided PCB 1.6mm 1oz HASL, 100nF 50V X7R Ceramic Capacitor 0805, USB Type-C Receptacle 24-Pin SMT |
| URL | text | Direct link to the product page | https://example.com/product/fr4-2layer-pcb |
| Price | number | Numeric price per unit or per lot, excluding currency symbol | 0.02, 1.45, 5.80, 49.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Component Category | enum | High-level classification of the electronic component or board | PCB, Resistor, Capacitor, Inductor, Connector, Relay, Crystal, Transformer, Fuse, LED, Switch, Sensor |
| Board Material | text | Base laminate material for PCBs | FR-4, Aluminum, Rogers 4003C, CEM-3, Polyimide, PTFE |
| Mounting Type | enum | Method by which the component is attached to the PCB | Surface Mount (SMD), Through Hole (THT), Press Fit |
| Dielectric Material | text | Insulating material type for capacitors or PCB substrate | X5R, X7R, C0G/NP0, Y5V, Electrolytic |
| IPC Class | enum | IPC quality and reliability classification for PCB fabrication | Class 1 (General), Class 2 (Dedicated Service), Class 3 (High Reliability) |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Packaging Format | enum | How components are packaged for shipping and assembly | Cut Tape, Tape and Reel, Tray, Tube, Bulk, Panel |
| Manufacturer | text | Company that manufactured the component or fabricated the PCB | JLCPCB, PCBWay, Murata, TDK, Yageo, TE Connectivity, Amphenol, Wurth Elektronik |
| Manufacturer Part Number | text | Official part number assigned by the manufacturer | GRM21BR71H104KA01L, CRCW08051K00FKEA, USB4110-GF-A |
| Number of Layers | number | Total number of conductive copper layers in the PCB stackup | 1, 2, 4, 6, 8, 10, 12 |
| Board Thickness | number (mm) | Overall thickness of the finished PCB including all layers | 0.4, 0.8, 1.0, 1.6, 2.0, 2.4, 3.2 |
| Surface Finish | text | Protective finish applied to exposed copper pads on the PCB | HASL Lead-Free, ENIG, OSP, Immersion Silver, Immersion Tin, Hard Gold, ENEPIG |
| Solder Mask Color | enum | Color of the protective solder mask layer on the PCB | Green, Red, Blue, Black, White, Yellow, Matte Green, Matte Black, Purple |
| Silkscreen Color | enum | Color of the legend and reference designator printing on the PCB | White, Black, Yellow |
| Minimum Trace Width | number (mm) | Smallest allowable copper trace width on the board | 0.1, 0.127, 0.15, 0.2 |
| Minimum Trace Spacing | number (mm) | Smallest allowable gap between adjacent copper features | 0.1, 0.127, 0.15, 0.2 |
| Board Dimensions Width | number (mm) | Width of the finished PCB | 15, 30, 80, 200, 400 |
| Impedance Controlled | boolean | Whether controlled impedance traces are required and tested | true, false |
| Component Value | text | Primary electrical value for passive components | 10K, 100nF, 4.7uH, 12MHz |
| Tolerance | text (%) | Allowable deviation from the nominal component value | 1%, 5%, 10%, 20% |
| Current Rating | number (A) | Maximum continuous current the component can carry | 0.5, 1.0, 3.0, 10.0, 20.0 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus industry standards (IPC-6011 PCB classification, IPC/JEDEC, RoHS, UL 94) | [PCBWay](https://www.pcbway.com/capabilities.html), [JLCPCB](https://jlcpcb.com/parts/all-electronic-components), [Digi-Key](https://www.digikey.com/en/products), [Mouser](https://www.mouser.com/electronic-components/) |
