# SKU Schema: Fall Protection Equipment (Harnesses, Lanyards)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.fall_protection`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 1113001, 1246305, 1340185 |
| Product Name | text | Full product name including key specs such as type, model, and configuration | 3M DBI-SALA ExoFit X300 Comfort Vest Safety Harness 2D QC, Miller TurboLite Edge 6 ft Self-Retracting Lifeline |
| URL | text | Direct link to the product page | https://example.com/product/exofit-x300-vest-harness |
| Price | number | Numeric unit price excluding currency symbol | 89.99, 249.50, 499.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary type of fall protection equipment | Full Body Harness, Vest-Style Harness, Self-Retracting Lifeline (SRL), Shock-Absorbing Lanyard, Positioning Lanyard, Rope Grab, Anchor Point, Horizontal Lifeline, Retractable with Rescue, Body Belt |
| D-Ring Material | enum | Material of the D-ring connectors | Alloy Steel, Aluminum, Zinc Plated Steel, Stainless Steel |
| Webbing Material | text | Material of the load-bearing straps | Polyester, Nylon, Nomex/Kevlar Blend |
| Leg Buckle Type | enum | Closure mechanism for leg straps | Tongue Buckle, Quick Connect, Pass-Through |
| Chest Buckle Type | enum | Closure mechanism for chest strap | Quick Connect, Pass-Through, Tongue Buckle |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Lifeline Cable Material | text | Material of the cable or webbing in self-retracting lifelines | Galvanized Steel Cable, Stainless Steel Cable, Dyneema Webbing, Nylon Webbing |
| Connector Type | text | Type of snap hook or carabiner on the lanyard | Snap Hook, Rebar Hook, Carabiner, Scaffold Hook |
| Energy Absorber Type | text | Shock absorption mechanism on lanyards | Internal Pack, External Pack, Tear-Away, SRL Brake, None |
| Reflective Material | boolean | Whether the equipment includes reflective striping for visibility | true, false |
| Country of Origin | text | Country where the product is manufactured | USA, Mexico, China, France |
| Model Number | text | Manufacturer model or part number | 1113001, 1401052,DERA2, T7FD611 |
| Harness Style | enum | Body coverage and attachment configuration for harnesses | Vest, Cross-Over, Tongue Buckle, Construction, Tower Climbing, Rescue |
| Number of D-Rings | number | Total count of attachment D-ring connection points | 1, 2, 3, 4, 5 |
| D-Ring Positions | text (list) | Locations of D-ring attachment points on the harness | Back (Dorsal), Front (Sternal), Side (Hip), Shoulder, Seat |
| Webbing Width | number (mm) | Width of the primary webbing straps | 44, 45, 50 |
| Webbing Strength | text | Rated breaking strength of the webbing | 6000 lb, 5000 lb |
| Padding | text | Type and location of comfort padding | Shoulder Pads, Lumbar Pad, Leg Pads, Full Body, None |
| Connector Gate Opening | number (mm) | Gate opening width of the connector | 19, 22, 50, 65 |
| Free Fall Distance | number (m) | Maximum permitted free fall before arrest engages | 0.6, 1.2, 1.8 |
| Arrest Distance | number (m) | Maximum deceleration distance after free fall | 1.07, 1.2, 1.5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI Z359, CSA Z259, EN 361/355/360) | [3M DBI-SALA](https://www.3m.com/3M/en_US/p/c/ppe/fall-protection/b/dbi-sala/), [Honeywell Miller](https://automation.honeywell.com/us/en/products/personal-protective-equipment/fall-protection), [Werner Fall Protection](https://www.wernerco.com/fall-protection), [GME Supply](https://www.gmesupply.com/brands/dbi-sala) |
