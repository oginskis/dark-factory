# SKU Schema: Metal Castings & Forgings

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | CF-A36-OD-5000, IC-316-FLANGE-6IN |
| Product Name | text | Full product name including process, material, and key dimensions | A36 Open Die Forged Round Bar 5in OD x 120in, 316 Stainless Investment Cast Flange 6in 150# |
| URL | text | Direct link to the product page | https://example.com/product/a36-open-die-forged-round |
| Price | number | Numeric unit price (per piece or per pound) excluding currency symbol | 450.00, 1250.00, 8.50 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Manufacturer | text | Name of the foundry or forge shop | Scot Forge, Bharat Forge, PCC Structurals, Hitachi Metals, Signicast |
| Manufacturing Process | enum | Primary production method | Open Die Forging, Closed Die Forging, Ring Rolling, Seamless Rolled Ring, Sand Casting, Investment Casting, Die Casting, Permanent Mold Casting, Centrifugal Casting |
| Material Type | enum | Broad category of the base metal | Carbon Steel, Alloy Steel, Stainless Steel, Aluminum, Copper Alloy, Nickel Alloy, Titanium, Ductile Iron, Gray Iron |
| Material Grade | text | Specific alloy grade or specification | ASTM A105, AISI 4140, AISI 4340, 316L, A356, C95400, Inconel 718, Grade 65-45-12 |
| Part Shape | text | General shape or form of the finished casting or forging | Round Bar, Disc, Ring, Block, Flange, Shaft, Hub, Cylinder, Custom |
| Outside Diameter | number (in) | Outer diameter for round and ring shapes | 4, 12, 36, 72, 120 |
| Inside Diameter | number (in) | Inner diameter for ring and hollow shapes | 2, 8, 24, 48, 96 |
| Length/Height | number (in) | Length or height of the part | 6, 12, 36, 120, 240 |
| Width | number (in) | Width for rectangular blocks and custom shapes | 6, 12, 24, 48 |
| Wall Thickness | number (in) | Wall thickness for hollow castings and rolled rings | 0.125, 0.250, 1.0, 3.0, 6.0 |
| Weight | number (lbs) | Finished part weight | 5, 50, 500, 5000, 50000 |
| Weight Range Class | text | General weight category for capability matching | Under 10 lbs, 10-100 lbs, 100-1000 lbs, 1000-10000 lbs, Over 10000 lbs |
| Heat Treatment | text | Post-process thermal treatment applied | Normalized, Quenched and Tempered, Annealed, Solution Treated, Aged, Stress Relieved, None |
| Surface Condition | text | Surface finish state after processing | As-Forged, As-Cast, Rough Machined, Finish Machined, Shot Blasted, Ground |
| Dimensional Tolerance | text | Achievable dimensional tolerance class | ASTM A788 Standard, ISO 8062 CT4-CT8, NADCA Standard, Near Net Shape |
| Surface Roughness | number (Ra um) | Surface roughness in micrometres Ra | 0.8, 1.6, 3.2, 6.3, 12.5, 25.0 |
| Tensile Strength | number (ksi) | Minimum ultimate tensile strength of the finished part | 60, 75, 95, 120, 150 |
| Yield Strength | number (ksi) | Minimum yield strength of the finished part | 36, 45, 65, 100, 130 |
| Elongation | number (%) | Minimum elongation at break | 4, 10, 15, 20, 25 |
| Hardness | text | Hardness measurement of the finished part | HRB 70, HRC 22-28, BHN 170-220 |
| Impact Test | text | Charpy V-notch impact test results or requirements if applicable | 15 ft-lbs at -20F, 25 ft-lbs at -50F, N/A |
| NDE/Testing | text (list) | Non-destructive examination methods performed | UT (Ultrasonic), MT (Magnetic Particle), RT (Radiographic), PT (Dye Penetrant), VT (Visual), None |
| Certification | text (list) | Quality and industry certifications | ISO 9001, AS9100, NADCAP, ASME, PED, NORSOK |
| Specification | text (list) | Applicable material and process specifications | ASTM A788, ASTM A781, ASTM A105, AMS 2175, ASME SA-352 |
| Country of Origin | text | Country where the part was produced | USA, India, Germany, Japan, China, Italy |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus ASTM forging/casting standards (A788, A781, A105) and NADCA die casting product specification standards | [Scot Forge](https://www.scotforge.com/), [Integrated Solutions](https://www.integratedsolutionsco.com/products-services/castings-forging/), [EB Castworld](https://ebcastworld.com/), [Bunty LLC](https://buntyllc.com/castings/) |
