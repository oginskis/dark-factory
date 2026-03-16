# SKU Schema: Mobility Aids (Wheelchairs, Walkers)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.mobility_aids`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | WCK2, SSP218FA, TREX2XR, EX1 |
| Product Name | product_name | text | — | Full product name including key specs such as type, seat width, and model | Silver Sport 2 Wheelchair 18in Seat Detachable Arms, Nitro Sprint Rollator |
| URL | url | text | — | Direct link to the product page | https://example.com/product/silver-sport-2-wheelchair |
| Price | price | number | — | Numeric unit price excluding currency symbol | 179.95, 329.95, 549.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | product_type | enum | — | Primary device category | Manual Wheelchair, Transport Wheelchair, Power Wheelchair, Standard Walker, Rolling Walker, Rollator, Knee Walker |
| Patient Type | patient_type | enum | — | Intended user population | Adult, Pediatric, Bariatric |
| Frame Material | frame_material | text | — | Primary material of the frame | Steel, Aluminum, Titanium, Carbon Fiber, Chrome-Plated Steel |
| Armrest Type | armrest_type | text | — | Style and adjustability of the armrests | Fixed Full Length, Removable Desk Length, Flip Back Desk Length, Height Adjustable, Padded |
| Footrest Type | footrest_type | text | — | Style of the leg or foot support | Swing-Away, Elevating Leg Rest, Fixed, Removable, Composite |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Wheel Type | wheel_type | text | — | Material and style of wheels or casters | Solid Rubber, Pneumatic, Flat-Free, Mag Wheel |
| Upholstery Material | upholstery_material | text | — | Material covering the seat and backrest | Nylon, Vinyl, Mesh, Padded Nylon |
| Brake Type | brake_type | text | — | Type of braking mechanism | Loop Lock, Push-Down, Hand Brake, Wheel Lock |
| Country of Origin | country_of_origin | text | — | Country where the product was manufactured | China, Taiwan, USA |
| Seat Width | seat_width | text | in | Width of the seat surface | 16, 18, 20, 22, 24 |
| Seat Depth | seat_depth | text | in | Depth of the seat surface from front to back | 14, 16, 18, 20 |
| Seat Height | seat_height | text | in | Height of the seat from the ground. May be adjustable via dual axle | 17.5, 19.5, 18-20 |
| Overall Width | overall_width | number | in | Total width of the device including wheels or handles | 25, 27, 30 |
| Overall Height | overall_height | number | in | Total height from ground to top of push handles or backrest | 36, 38, 40 |
| Folded Width | folded_width | number | in | Width when folded for transport or storage | 11, 13, 15 |
| Color | color | text | — | Primary frame or upholstery color | Black, Blue, Red, Silver Vein, Chrome |
| Handle Height Range | handle_height_range | text | in | Adjustable handle height range for walkers and rollators | 32-37, 33-38, 35-40 |
| Folding Mechanism | folding_mechanism | text | — | How the device folds for storage or transport | Side-Fold, Cross-Fold, Quick-Release Wheels, Two-Button Release |
| Seat Included | seat_included | boolean | — | Whether a built-in seat is included (for rollators and transport chairs) | Yes, No |
| Backrest Included | backrest_included | boolean | — | Whether a backrest is included (for rollators) | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus WHO wheelchair specs and ISO 7176 standards | [Home Medical Equipment](https://home-med-equip.com/catalog/standard-size-wheelchairs.html), [1800Wheelchair](https://www.1800wheelchair.com/), [Drive Medical](https://www.drivemedical.com/mobility), [Carex](https://carex.com/collections/mobility-aids-products-and-accessories) |
