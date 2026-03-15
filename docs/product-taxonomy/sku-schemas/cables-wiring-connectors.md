# SKU Schema: Cables, Wiring & Connectors

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.cables_wiring_connectors`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 1746244, WM1234-ND, 174-6244 |
| Product Name | product_name | text | Full product name including key specs such as type, gauge, and conductor count | 3-Core 1.5mm PVC Flex Cable Black 10m, Cat6 UTP Ethernet Patch Cable 5ft Blue |
| URL | url | text | Direct link to the product page | https://example.com/product/multi-core-cable-1-5mm |
| Price | price | number | Numeric price per unit (metre, foot, reel, or piece depending on seller), excluding currency symbol | 0.85, 12.50, 249.99 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Top-level product classification | Cable, Wire, Connector, Terminal, Cable Assembly, Splice, Adapter |
| Cable/Connector Category | cableconnector_category | text | Specific subcategory within the product type | Multi-Core Cable, Coaxial Cable, Ethernet Cable, Circular Connector, Terminal Block, Wire-to-Board Connector |
| Conductor Material | conductor_material | text | Material of the current-carrying conductor | Bare Copper, Tinned Copper, Silver-Plated Copper, Copper Clad Aluminium |
| Conductor Type | conductor_type | enum | Physical construction of the conductor | Solid, Stranded, Braided, Flexible |
| Insulation Material | insulation_material | text | Material used for primary conductor insulation | PVC, XLPE, Teflon/PTFE, Silicone, Polyethylene, TPE |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Jacket/Sheath Material | jacketsheath_material | text | Material of the outer cable jacket or connector housing | PVC, Nylon, Thermoplastic, Rubber, LSZH |
| Mounting Type | mounting_type | text | How the connector or terminal is installed | Panel Mount, PCB Mount, Cable Mount, DIN Rail, Through Hole, Surface Mount |
| Shield Type | shield_type | text | Construction of the cable shield when present | Foil, Braid, Foil and Braid, Spiral |
| LAN Category | lan_category | text | Network performance category for data cables per TIA/ISO standards | Cat5e, Cat6, Cat6a, Cat7, Cat8 |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | China, USA, Germany, Japan, Mexico |
| Wire Gauge | wire_gauge | text | Cross-sectional size of the conductor in AWG or metric | 18 AWG, 24 AWG, 1.5 mm², 2.5 mm², 0.75 mm² |
| Number of Conductors/Cores | number_of_conductorscores | number | Count of individual insulated conductors within a cable | 1, 2, 3, 4, 8, 25 |
| Current Rating | current_rating | number (A) | Maximum continuous current capacity | 1, 5, 10, 16, 20, 100 |
| Jacket/Housing Colour | jackethousing_colour | text | Colour of the outermost layer or connector body | Black, White, Grey, Blue, Orange, Red |
| Number of Contacts/Pins | number_of_contactspins | number | Count of electrical contacts in a connector | 2, 4, 8, 16, 24, 50 |
| Contact Pitch | contact_pitch | number (mm) | Centre-to-centre distance between adjacent pins or terminals | 1.0, 1.27, 2.0, 2.54, 5.08 |
| Contact Plating | contact_plating | text | Finish applied to connector contacts for conductivity or corrosion resistance | Gold, Tin, Silver, Nickel |
| Termination Method | termination_method | text | How the conductor is attached to the connector or terminal | Crimp, Solder, Screw, IDC, Push-In, Spring Cage |
| Gender | gender | enum | Connector mating orientation | Male, Female, Hermaphroditic |
| Shielding | shielding | enum | Whether the cable or connector provides electromagnetic shielding | Shielded, Unshielded |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 sources plus industry standards (IEC 60228, IEC 60320, TIA-568) | [RS Components](https://uk.rs-online.com/web/c/cables-wires/cable/multi-core-cable/), [Digi-Key](https://www.digikey.com/en/products/category/cables-wires/473), [Molex](https://www.molex.com/en-us/products/connectors), [Mouser](https://www.mouser.com/c/connectors/) |
