# SKU Schema: Hand Tools (Hammers, Wrenches, Screwdrivers)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.hand_tools`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 51-944, 401M21, WRN-14MM, 26015, 54-024 |
| Product Name | product_name | text | Full product name including key specs such as tool type, size, and series | Stanley Anti-Vibe 20 oz Curved Claw Hammer, TEKTON 14 mm Combination Wrench, Klein Tools #1 Insulated Square Screwdriver |
| URL | url | text | Direct link to the product page | https://example.com/product/anti-vibe-20oz-hammer |
| Price | price | number | Numeric price per unit excluding currency symbol | 12.99, 24.50, 89.95, 7.49 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Tool Category | tool_category | enum | Primary hand tool category | Hammer, Wrench, Screwdriver |
| Tool Type | tool_type | text | Specific type within the category | Claw Hammer, Ball Pein Hammer, Sledge Hammer, Combination Wrench, Adjustable Wrench, Socket Wrench, Torque Wrench, Phillips Screwdriver, Slotted Screwdriver, Torx Screwdriver |
| Model Number | model_number | text | Manufacturer part or model number | 51-508, STHT51512, 56-220, WRN-14102, 661-4-INS |
| Tip Type | tip_type | enum | Screwdriver or bit tip profile | Phillips, Slotted, Torx, Hex, Square, Robertson, Pozidriv, Tri-Wing |
| Head Material | head_material | text | Material of the hammer head or wrench jaw | Forged High Carbon Steel, Alloy Steel, Chrome Vanadium Steel, Drop Forged Steel |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Head Type | head_type | text | Shape or style of the hammer head or wrench head | Curved Claw, Straight Rip Claw, Ball Pein, Cross Pein, Smooth Face, Milled Face |
| Handle Material | handle_material | text | Material used for the grip or handle | Hickory, Fiberglass, Graphite, Rubber, Bi-material, Hard Plastic, Cushion Grip |
| Shaft Material | shaft_material | text | Material used for the tool shaft or shank | Steel, Chrome Vanadium, Fiberglass, Graphite Composite |
| Country of Origin | country_of_origin | text | Country where the tool is manufactured | USA, Germany, Taiwan, China, Japan |
| Product Line/Series | product_lineseries | text | Named series or collection the tool belongs to | FatMax, Anti-Vibe, GEARWRENCH 120XP, TEKTON Everybit, Klein Journeyman |
| Measurement System | measurement_system | enum | Whether the tool uses imperial or metric sizing | SAE, Metric |
| Finish | finish | text | Surface treatment or coating applied to metal parts | Chrome, Satin Chrome, Black Oxide, Polished, Nickel Plated |
| Torque Range | torque_range | text | Minimum and maximum torque for torque tools | 20-150 ft-lbs, 10-80 Nm, 5-25 in-lbs |
| Insulated | insulated | boolean | Whether the tool has a VDE-rated insulated handle for live electrical work | Yes, No |
| Insulation Rating | insulation_rating | text (V) | Maximum voltage rating for insulated tools | 1000V AC, 1500V DC |
| ESD Safe | esd_safe | boolean | Whether the tool is rated for electrostatic discharge sensitive environments | Yes, No |
| Magnetic Tip | magnetic_tip | boolean | Whether the screwdriver has a magnetized tip | Yes, No |
| Certifications | certifications | text (list) | Safety and quality certifications | ANSI, ASME, IEC 60900, VDE, GS, DIN/ISO |
| Warranty | warranty | text | Manufacturer warranty type and duration | Lifetime, Limited Lifetime, Full Lifetime, 1 Year |
| Size | size | text | Primary size designation relevant to the tool type: head weight for hammers, jaw size for wrenches, tip size for screwdrivers | 20 oz, 14 mm, 3/4 in, #2, T30, 1/4 in |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus standards (ANSI, ASME, IEC 60900/VDE for insulated tools) | [Stanley Hammers (via Grainger)](https://www.grainger.com/), [TEKTON Hand Tools](https://www.tekton.com/), [Klein Tools Catalog](https://www.kleintools.com/catalog), [GEARWRENCH 2025 Catalog](https://www.gearwrench.com/resources/catalogs/gearwrench-catalog-2025) |
