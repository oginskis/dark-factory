# SKU Schema: Fall Protection Equipment (Harnesses, Lanyards)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 1113001, 1246305, 1340185 |
| Product Name | text | Full product name including key specs such as type, model, and configuration | 3M DBI-SALA ExoFit X300 Comfort Vest Safety Harness 2D QC, Miller TurboLite Edge 6 ft Self-Retracting Lifeline |
| URL | text | Direct link to the product page | https://example.com/product/exofit-x300-vest-harness |
| Price | number | Numeric unit price excluding currency symbol | 89.99, 249.50, 499.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Name of the fall protection manufacturer | 3M DBI-SALA, 3M Protecta, Honeywell Miller, Werner, MSA, Guardian Fall Protection, FallTech, Petzl |
| Product Type | enum | Primary type of fall protection equipment | Full Body Harness, Vest-Style Harness, Self-Retracting Lifeline (SRL), Shock-Absorbing Lanyard, Positioning Lanyard, Rope Grab, Anchor Point, Horizontal Lifeline, Retractable with Rescue, Body Belt |
| Harness Style | enum | Body coverage and attachment configuration for harnesses | Vest, Cross-Over, Tongue Buckle, Construction, Tower Climbing, Rescue |
| Number of D-Rings | number | Total count of attachment D-ring connection points | 1, 2, 3, 4, 5 |
| D-Ring Positions | text (list) | Locations of D-ring attachment points on the harness | Back (Dorsal), Front (Sternal), Side (Hip), Shoulder, Seat |
| D-Ring Material | enum | Material of the D-ring connectors | Alloy Steel, Aluminum, Zinc Plated Steel, Stainless Steel |
| Webbing Material | text | Material of the load-bearing straps | Polyester, Nylon, Nomex/Kevlar Blend |
| Webbing Width | number (mm) | Width of the primary webbing straps | 44, 45, 50 |
| Webbing Strength | text | Rated breaking strength of the webbing | 6000 lb, 5000 lb |
| Leg Buckle Type | enum | Closure mechanism for leg straps | Tongue Buckle, Quick Connect, Pass-Through |
| Chest Buckle Type | enum | Closure mechanism for chest strap | Quick Connect, Pass-Through, Tongue Buckle |
| Padding | text | Type and location of comfort padding | Shoulder Pads, Lumbar Pad, Leg Pads, Full Body, None |
| Weight Capacity | text | Maximum user weight including tools and equipment | 130-310 lb, 130-420 lb, 400 lb |
| Lanyard Length | number (m) | Length of lanyard or retractable lifeline | 1.2, 1.8, 2.4, 3.0, 6.0, 15.0 |
| Lifeline Cable Material | text | Material of the cable or webbing in self-retracting lifelines | Galvanized Steel Cable, Stainless Steel Cable, Dyneema Webbing, Nylon Webbing |
| Connector Type | text | Type of snap hook or carabiner on the lanyard | Snap Hook, Rebar Hook, Carabiner, Scaffold Hook |
| Connector Gate Opening | number (mm) | Gate opening width of the connector | 19, 22, 50, 65 |
| Energy Absorber Type | text | Shock absorption mechanism on lanyards | Internal Pack, External Pack, Tear-Away, SRL Brake, None |
| Free Fall Distance | number (m) | Maximum permitted free fall before arrest engages | 0.6, 1.2, 1.8 |
| Arrest Distance | number (m) | Maximum deceleration distance after free fall | 1.07, 1.2, 1.5 |
| Size | text | Harness size designation | Small, Medium, Large, XL, Universal, 2XL |
| Reflective Material | boolean | Whether the equipment includes reflective striping for visibility | true, false |
| Color | text | Primary color of the webbing or harness | Black, Yellow, Blue, Orange, Hi-Viz Lime |
| Weight | number (g) | Weight of the equipment | 1200, 1800, 2500, 3600 |
| Certifications | text (list) | Applicable safety standards met | ANSI Z359.1, ANSI Z359.11, ANSI Z359.13, ANSI Z359.14, CSA Z259, EN 361, EN 355, EN 360, AS/NZS 1891 |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, China, France |
| Model Number | text | Manufacturer model or part number | 1113001, 1401052,DERA2, T7FD611 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI Z359, CSA Z259, EN 361/355/360) | [3M DBI-SALA](https://www.3m.com/3M/en_US/p/c/ppe/fall-protection/b/dbi-sala/), [Honeywell Miller](https://automation.honeywell.com/us/en/products/personal-protective-equipment/fall-protection), [Werner Fall Protection](https://www.wernerco.com/fall-protection), [GME Supply](https://www.gmesupply.com/brands/dbi-sala) |
