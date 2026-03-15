# SKU Schema: Cables, Wiring & Connectors

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 1746244, WM1234-ND, 174-6244 |
| Product Name | text | Full product name including key specs such as type, gauge, and conductor count | 3-Core 1.5mm PVC Flex Cable Black 10m, Cat6 UTP Ethernet Patch Cable 5ft Blue |
| URL | text | Direct link to the product page | https://example.com/product/multi-core-cable-1-5mm |
| Price | number | Numeric price per unit (metre, foot, reel, or piece depending on seller), excluding currency symbol | 0.85, 12.50, 249.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Cable, wire, or connector manufacturer name | Belden, TE Connectivity, Molex, Alpha Wire, Phoenix Contact, Amphenol |
| Product Type | enum | Top-level product classification | Cable, Wire, Connector, Terminal, Cable Assembly, Splice, Adapter |
| Cable/Connector Category | text | Specific subcategory within the product type | Multi-Core Cable, Coaxial Cable, Ethernet Cable, Circular Connector, Terminal Block, Wire-to-Board Connector |
| Conductor Material | text | Material of the current-carrying conductor | Bare Copper, Tinned Copper, Silver-Plated Copper, Copper Clad Aluminium |
| Conductor Type | enum | Physical construction of the conductor | Solid, Stranded, Braided, Flexible |
| Wire Gauge | text | Cross-sectional size of the conductor in AWG or metric | 18 AWG, 24 AWG, 1.5 mm², 2.5 mm², 0.75 mm² |
| Number of Conductors/Cores | number | Count of individual insulated conductors within a cable | 1, 2, 3, 4, 8, 25 |
| Voltage Rating | number (V) | Maximum rated voltage the product can safely carry | 300, 600, 1000, 1500 |
| Current Rating | number (A) | Maximum continuous current capacity | 1, 5, 10, 16, 20, 100 |
| Insulation Material | text | Material used for primary conductor insulation | PVC, XLPE, Teflon/PTFE, Silicone, Polyethylene, TPE |
| Jacket/Sheath Material | text | Material of the outer cable jacket or connector housing | PVC, Nylon, Thermoplastic, Rubber, LSZH |
| Jacket/Housing Colour | text | Colour of the outermost layer or connector body | Black, White, Grey, Blue, Orange, Red |
| Cable Length | number (m) | Total length of cable or cable assembly supplied | 1, 5, 10, 25, 50, 100, 305 |
| Outer Diameter | number (mm) | Overall outside diameter of the cable | 3.5, 5.2, 7.8, 12.0 |
| Number of Contacts/Pins | number | Count of electrical contacts in a connector | 2, 4, 8, 16, 24, 50 |
| Contact Pitch | number (mm) | Centre-to-centre distance between adjacent pins or terminals | 1.0, 1.27, 2.0, 2.54, 5.08 |
| Contact Plating | text | Finish applied to connector contacts for conductivity or corrosion resistance | Gold, Tin, Silver, Nickel |
| Termination Method | text | How the conductor is attached to the connector or terminal | Crimp, Solder, Screw, IDC, Push-In, Spring Cage |
| Gender | enum | Connector mating orientation | Male, Female, Hermaphroditic |
| Mounting Type | text | How the connector or terminal is installed | Panel Mount, PCB Mount, Cable Mount, DIN Rail, Through Hole, Surface Mount |
| Shielding | enum | Whether the cable or connector provides electromagnetic shielding | Shielded, Unshielded |
| Shield Type | text | Construction of the cable shield when present | Foil, Braid, Foil and Braid, Spiral |
| IP Rating | text | Ingress protection rating per IEC 60529 | IP20, IP44, IP65, IP67, IP68 |
| Operating Temperature Min | number (deg C) | Minimum rated operating temperature | -40, -20, -10, 0 |
| Operating Temperature Max | number (deg C) | Maximum rated operating temperature | 60, 80, 105, 150, 200 |
| Frequency Rating | text | Maximum signal frequency or bandwidth specification | 100 MHz, 250 MHz, 1 GHz, 10 GHz |
| LAN Category | text | Network performance category for data cables per TIA/ISO standards | Cat5e, Cat6, Cat6a, Cat7, Cat8 |
| Impedance | number (ohm) | Characteristic impedance for signal and coaxial cables | 50, 75, 100, 120 |
| Standards/Approvals | text (list) | Safety, quality, and regulatory certifications | UL, CSA, CE, RoHS, REACH, VDE, IEC 60320, IEC 60228, MIL-SPEC |
| Country of Origin | text | Country where the product was manufactured | China, USA, Germany, Japan, Mexico |
| Weight per Unit | number (kg) | Weight of one selling unit (piece, reel, or bag) | 0.02, 0.15, 1.50, 8.00 |
| Pack Quantity | number | Number of pieces per selling unit | 1, 5, 10, 50, 100, 1000 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus industry standards (IEC 60228, IEC 60320, TIA-568) | [RS Components](https://uk.rs-online.com/web/c/cables-wires/cable/multi-core-cable/), [Digi-Key](https://www.digikey.com/en/products/category/cables-wires/473), [Molex](https://www.molex.com/en-us/products/connectors), [Mouser](https://www.mouser.com/c/connectors/) |
