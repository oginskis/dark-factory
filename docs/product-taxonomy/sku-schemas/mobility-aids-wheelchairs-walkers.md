# SKU Schema: Mobility Aids (Wheelchairs, Walkers)

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | WCK2, SSP218FA, TREX2XR, EX1 |
| Product Name | text | Full product name including key specs such as type, seat width, and model | Silver Sport 2 Wheelchair 18in Seat Detachable Arms, Nitro Sprint Rollator |
| URL | text | Direct link to the product page | https://example.com/product/silver-sport-2-wheelchair |
| Price | number | Numeric unit price excluding currency symbol | 179.95, 329.95, 549.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | Drive Medical, Invacare, Medline, Karman, Sunrise Medical, Permobil |
| Product Type | enum | Primary device category | Manual Wheelchair, Transport Wheelchair, Power Wheelchair, Standard Walker, Rolling Walker, Rollator, Knee Walker |
| Patient Type | enum | Intended user population | Adult, Pediatric, Bariatric |
| Frame Material | text | Primary material of the frame | Steel, Aluminum, Titanium, Carbon Fiber, Chrome-Plated Steel |
| Seat Width | text (in) | Width of the seat surface | 16, 18, 20, 22, 24 |
| Seat Depth | text (in) | Depth of the seat surface from front to back | 14, 16, 18, 20 |
| Seat Height | text (in) | Height of the seat from the ground. May be adjustable via dual axle | 17.5, 19.5, 18-20 |
| Weight Capacity | number (lbs) | Maximum user weight the device supports | 250, 300, 350, 450, 600 |
| Product Weight | number (lbs) | Weight of the device without user | 13.5, 36, 41, 55 |
| Overall Width | number (in) | Total width of the device including wheels or handles | 25, 27, 30 |
| Overall Length | number (in) | Total length from front to back | 36, 42, 46 |
| Overall Height | number (in) | Total height from ground to top of push handles or backrest | 36, 38, 40 |
| Folded Width | number (in) | Width when folded for transport or storage | 11, 13, 15 |
| Armrest Type | text | Style and adjustability of the armrests | Fixed Full Length, Removable Desk Length, Flip Back Desk Length, Height Adjustable, Padded |
| Footrest Type | text | Style of the leg or foot support | Swing-Away, Elevating Leg Rest, Fixed, Removable, Composite |
| Rear Wheel Diameter | number (in) | Diameter of rear wheels (large wheels on manual wheelchairs) | 8, 12, 24 |
| Front Caster Diameter | number (in) | Diameter of front caster wheels | 6, 7, 8 |
| Wheel Type | text | Material and style of wheels or casters | Solid Rubber, Pneumatic, Flat-Free, Mag Wheel |
| Upholstery Material | text | Material covering the seat and backrest | Nylon, Vinyl, Mesh, Padded Nylon |
| Color | text | Primary frame or upholstery color | Black, Blue, Red, Silver Vein, Chrome |
| Handle Height Range | text (in) | Adjustable handle height range for walkers and rollators | 32-37, 33-38, 35-40 |
| Folding Mechanism | text | How the device folds for storage or transport | Side-Fold, Cross-Fold, Quick-Release Wheels, Two-Button Release |
| Brake Type | text | Type of braking mechanism | Loop Lock, Push-Down, Hand Brake, Wheel Lock |
| Seat Included | boolean | Whether a built-in seat is included (for rollators and transport chairs) | Yes, No |
| Backrest Included | boolean | Whether a backrest is included (for rollators) | Yes, No |
| Storage Pouch | boolean | Whether a carry pouch or basket is included | Yes, No |
| Certification | text (list) | Regulatory and quality certifications | FDA Class I, ISO 7176, CE, HCPCS E1161 |
| HCPCS Code | text | Healthcare Common Procedure Coding System code for insurance billing | E1161, E0143, E0130, K0001 |
| Warranty | text | Manufacturer warranty period | Lifetime Frame, 1 Year Parts, 3 Year Frame |
| Country of Origin | text | Country where the product was manufactured | China, Taiwan, USA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 companies plus WHO wheelchair specs and ISO 7176 standards | [Home Medical Equipment](https://home-med-equip.com/catalog/standard-size-wheelchairs.html), [1800Wheelchair](https://www.1800wheelchair.com/), [Drive Medical](https://www.drivemedical.com/mobility), [Carex](https://carex.com/collections/mobility-aids-products-and-accessories) |
