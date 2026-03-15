# SKU Schema: Fall Protection Equipment (Harnesses, Lanyards)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.fall_protection`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 1113001, 1246305, 1340185 |
| Product Name | product_name | text | Full product name including key specs such as type, model, and configuration | 3M DBI-SALA ExoFit X300 Comfort Vest Safety Harness 2D QC, Miller TurboLite Edge 6 ft Self-Retracting Lifeline |
| URL | url | text | Direct link to the product page | https://example.com/product/exofit-x300-vest-harness |
| Price | price | number | Numeric unit price excluding currency symbol | 89.99, 249.50, 499.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary type of fall protection equipment | Full Body Harness, Vest-Style Harness, Self-Retracting Lifeline (SRL), Shock-Absorbing Lanyard, Positioning Lanyard, Rope Grab, Anchor Point, Horizontal Lifeline, Retractable with Rescue, Body Belt |
| D-Ring Material | d-ring_material | enum | Material of the D-ring connectors | Alloy Steel, Aluminum, Zinc Plated Steel, Stainless Steel |
| Webbing Material | webbing_material | text | Material of the load-bearing straps | Polyester, Nylon, Nomex/Kevlar Blend |
| Leg Buckle Type | leg_buckle_type | enum | Closure mechanism for leg straps | Tongue Buckle, Quick Connect, Pass-Through |
| Chest Buckle Type | chest_buckle_type | enum | Closure mechanism for chest strap | Quick Connect, Pass-Through, Tongue Buckle |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Lifeline Cable Material | lifeline_cable_material | text | Material of the cable or webbing in self-retracting lifelines | Galvanized Steel Cable, Stainless Steel Cable, Dyneema Webbing, Nylon Webbing |
| Connector Type | connector_type | text | Type of snap hook or carabiner on the lanyard | Snap Hook, Rebar Hook, Carabiner, Scaffold Hook |
| Energy Absorber Type | energy_absorber_type | text | Shock absorption mechanism on lanyards | Internal Pack, External Pack, Tear-Away, SRL Brake, None |
| Reflective Material | reflective_material | boolean | Whether the equipment includes reflective striping for visibility | true, false |
| Country of Origin | country_of_origin | text | Country where the product is manufactured | USA, Mexico, China, France |
| Model Number | model_number | text | Manufacturer model or part number | 1113001, 1401052,DERA2, T7FD611 |
| Harness Style | harness_style | enum | Body coverage and attachment configuration for harnesses | Vest, Cross-Over, Tongue Buckle, Construction, Tower Climbing, Rescue |
| Number of D-Rings | number_of_d-rings | number | Total count of attachment D-ring connection points | 1, 2, 3, 4, 5 |
| D-Ring Positions | d-ring_positions | text (list) | Locations of D-ring attachment points on the harness | Back (Dorsal), Front (Sternal), Side (Hip), Shoulder, Seat |
| Webbing Width | webbing_width | number (mm) | Width of the primary webbing straps | 44, 45, 50 |
| Webbing Strength | webbing_strength | text | Rated breaking strength of the webbing | 6000 lb, 5000 lb |
| Padding | padding | text | Type and location of comfort padding | Shoulder Pads, Lumbar Pad, Leg Pads, Full Body, None |
| Connector Gate Opening | connector_gate_opening | number (mm) | Gate opening width of the connector | 19, 22, 50, 65 |
| Free Fall Distance | free_fall_distance | number (m) | Maximum permitted free fall before arrest engages | 0.6, 1.2, 1.8 |
| Arrest Distance | arrest_distance | number (m) | Maximum deceleration distance after free fall | 1.07, 1.2, 1.5 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI Z359, CSA Z259, EN 361/355/360) | [3M DBI-SALA](https://www.3m.com/3M/en_US/p/c/ppe/fall-protection/b/dbi-sala/), [Honeywell Miller](https://automation.honeywell.com/us/en/products/personal-protective-equipment/fall-protection), [Werner Fall Protection](https://www.wernerco.com/fall-protection), [GME Supply](https://www.gmesupply.com/brands/dbi-sala) |
