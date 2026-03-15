# SKU Schema: Hand Tools (Hammers, Wrenches, Screwdrivers)

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 51-944, 401M21, WRN-14MM, 26015, 54-024 |
| Product Name | text | Full product name including key specs such as tool type, size, and series | Stanley Anti-Vibe 20 oz Curved Claw Hammer, TEKTON 14 mm Combination Wrench, Klein Tools #1 Insulated Square Screwdriver |
| URL | text | Direct link to the product page | https://example.com/product/anti-vibe-20oz-hammer |
| Price | number | Numeric price per unit excluding currency symbol | 12.99, 24.50, 89.95, 7.49 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Tool manufacturer or brand name | Stanley, TEKTON, GEARWRENCH, Klein Tools, Wiha, Snap-on, Wera, Knipex, Proto |
| Tool Category | enum | Primary hand tool category | Hammer, Wrench, Screwdriver |
| Tool Type | text | Specific type within the category | Claw Hammer, Ball Pein Hammer, Sledge Hammer, Combination Wrench, Adjustable Wrench, Socket Wrench, Torque Wrench, Phillips Screwdriver, Slotted Screwdriver, Torx Screwdriver |
| Model Number | text | Manufacturer part or model number | 51-508, STHT51512, 56-220, WRN-14102, 661-4-INS |
| Product Line/Series | text | Named series or collection the tool belongs to | FatMax, Anti-Vibe, GEARWRENCH 120XP, TEKTON Everybit, Klein Journeyman |
| Size | text | Primary size designation relevant to the tool type: head weight for hammers, jaw size for wrenches, tip size for screwdrivers | 20 oz, 14 mm, 3/4 in, #2, T30, 1/4 in |
| Measurement System | enum | Whether the tool uses imperial or metric sizing | SAE, Metric |
| Drive Size | text | Socket drive size for wrenches and ratchets | 1/4 in, 3/8 in, 1/2 in, 3/4 in, 1 in |
| Tip Type | enum | Screwdriver or bit tip profile | Phillips, Slotted, Torx, Hex, Square, Robertson, Pozidriv, Tri-Wing |
| Tip Size | text | Specific tip or bit size designation | #0, #1, #2, #3, T8, T10, T15, T20, T30, 1/8 in, 1 mm, 5/32 in |
| Overall Length | number (in) | Total length of the tool from end to end | 4.5, 6, 8.25, 10.75, 12.5, 13.25, 15.06, 18 |
| Head Weight | text | Weight of the hammer head only | 8 oz, 16 oz, 20 oz, 24 oz, 3 lb, 4 lb |
| Head Material | text | Material of the hammer head or wrench jaw | Forged High Carbon Steel, Alloy Steel, Chrome Vanadium Steel, Drop Forged Steel |
| Head Type | text | Shape or style of the hammer head or wrench head | Curved Claw, Straight Rip Claw, Ball Pein, Cross Pein, Smooth Face, Milled Face |
| Handle Material | text | Material used for the grip or handle | Hickory, Fiberglass, Graphite, Rubber, Bi-material, Hard Plastic, Cushion Grip |
| Shaft Material | text | Material used for the tool shaft or shank | Steel, Chrome Vanadium, Fiberglass, Graphite Composite |
| Finish | text | Surface treatment or coating applied to metal parts | Chrome, Satin Chrome, Black Oxide, Polished, Nickel Plated |
| Weight | number (oz) | Total tool weight including handle | 6, 12, 18.5, 24, 32, 64 |
| Jaw Capacity | text | Maximum opening size for adjustable wrenches | 1 in, 1-1/8 in, 1-1/2 in, 2 in |
| Ratchet Tooth Count | number | Number of gear teeth in ratcheting mechanisms | 36, 72, 90, 120 |
| Torque Range | text | Minimum and maximum torque for torque tools | 20-150 ft-lbs, 10-80 Nm, 5-25 in-lbs |
| Insulated | boolean | Whether the tool has a VDE-rated insulated handle for live electrical work | Yes, No |
| Insulation Rating | text (V) | Maximum voltage rating for insulated tools | 1000V AC, 1500V DC |
| ESD Safe | boolean | Whether the tool is rated for electrostatic discharge sensitive environments | Yes, No |
| Set Piece Count | number | Number of pieces if sold as a set | 3, 6, 10, 15, 22, 65 |
| Included Sizes | text (list) | Range or list of sizes included in a set | 8-19 mm, 1/4-1 in, #1 to #3 Phillips |
| Magnetic Tip | boolean | Whether the screwdriver has a magnetized tip | Yes, No |
| Country of Origin | text | Country where the tool is manufactured | USA, Germany, Taiwan, China, Japan |
| Certifications | text (list) | Safety and quality certifications | ANSI, ASME, IEC 60900, VDE, GS, DIN/ISO |
| Warranty | text | Manufacturer warranty type and duration | Lifetime, Limited Lifetime, Full Lifetime, 1 Year |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 35 attributes from 4 companies plus standards (ANSI, ASME, IEC 60900/VDE for insulated tools) | [Stanley Hammers (via Grainger)](https://www.grainger.com/), [TEKTON Hand Tools](https://www.tekton.com/), [Klein Tools Catalog](https://www.kleintools.com/catalog), [GEARWRENCH 2025 Catalog](https://www.gearwrench.com/resources/catalogs/gearwrench-catalog-2025) |
