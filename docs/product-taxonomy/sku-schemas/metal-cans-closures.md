# SKU Schema: Metal Cans & Closures

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.metal_cans_closures`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | TRV-FD-307x409, TC-70G-CT, OBK-MT-16OZ |
| Product Name | product_name | text | — | Full product name including capacity, material, and format | 307x409 3-Piece Steel Food Can, 70G Tinplate Continuous Thread Closure, 16 oz Aluminum Beverage Can 202/211 |
| URL | url | text | — | Direct link to the product page | https://example.com/cans/307x409-food-can |
| Price | price | number | — | Numeric price per unit or per thousand, excluding currency symbol | 0.06, 0.12, 85.00, 250.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY, CNY |
| Product Category | product_category | enum | — | Broad classification of the metal packaging item | Food Can, Beverage Can, Aerosol Can, General Line Can, Closure/End, Metal Bottle, Paint Can, Drum |
| Body Material | body_material | enum | — | Primary metal used for the can body | Tinplate (ETP), Tin-Free Steel (TFS/ECCS), Aluminum Alloy, Chrome-Plated Steel |
| Body Material Thickness | body_material_thickness | number | mm | Thickness of the body wall material | 0.15, 0.18, 0.20, 0.23, 0.28, 0.30 |
| End Material | end_material | enum | — | Metal used for the can top and bottom ends | Tinplate, Tin-Free Steel, Aluminum |
| End/Closure Type | endclosure_type | enum | — | Style of the can end or closure mechanism | Standard Double Seam, Easy-Open (EOE), Ring-Pull, Stay-On Tab (SOT), Peel-Off, Twist-Off (Lug), Continuous Thread (CT), Press-On Twist-Off (PT), Pilfer-Proof (ROPP) |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the can or closure is manufactured | USA, UK, Germany, France, China, Brazil, Japan |
| Can Construction | can_construction | enum | — | Number of body pieces in the can | 2-Piece (Drawn and Ironed), 2-Piece (Draw-Redraw), 3-Piece (Welded Side Seam), 3-Piece (Soldered) |
| Can Height | can_height | number | mm | Overall height of the filled and seamed can | 50, 70, 95, 113, 122, 133, 178 |
| Interior Coating/Lining | interior_coatinglining | enum | — | Type of internal protective coating applied to the can body and ends | Epoxy, Polyester, BPA-NI (BPA Non-Intent), Oleoresin, Vinyl, Unlined |
| Exterior Coating | exterior_coating | enum | — | Protective or decorative coating on the can exterior | Litho-Printed, White Coated, Clear Lacquer, Uncoated, Matte Finish |
| Printing | printing | text | — | Description of decoration applied to the can exterior | Undecorated, 4-Color Litho, 6-Color Litho, Shrink Sleeve, Paper Label, Embossed |
| Retort Capability | retort_capability | enum | — | Whether the can is designed to withstand thermal retort processing (121C+) | Yes, No |
| Vacuum Pack | vacuum_pack | enum | — | Whether the can is designed for vacuum-packed contents | Yes, No |
| Pressure Rating | pressure_rating | number | bar | Maximum internal pressure the can is rated to withstand for carbonated or aerosol products | 0, 3.5, 6.2, 10, 18 |
| Shelf Life Support | shelf_life_support | text | — | Typical shelf life the packaging is designed to provide | 1 year, 2 years, 3 years, 5 years |
| Stacking Strength | stacking_strength | number | kg | Maximum load the filled can withstands in a vertical stack | 50, 80, 120, 200 |
| Pallet Quantity | pallet_quantity | number | — | Number of cans per standard pallet layer or full pallet | 1680, 2400, 4032, 5040 |
| Food Contact Compliance | food_contact_compliance | text (list) | — | Regulatory food-contact safety standards the product meets | FDA 21 CFR, EU 1935/2004, GB 4806, FSSC 22000 |
| Certification | certification | text (list) | — | Quality and sustainability certifications held by the manufacturer | ISO 9001, ISO 14001, BRC Packaging, ASI (Aluminium Stewardship Initiative), Metal Recycles Forever |
| Recyclability | recyclability | enum | — | Whether the metal packaging is recyclable in standard metal recycling streams | Infinitely Recyclable, Recyclable, Limited |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus industry standards (can-maker size codes, FDA 21 CFR, EU 1935/2004) | [Trivium Packaging Food Cans](https://www.triviumpackaging.com/products/industry/food), [Tecnocap Metal Closures](https://www.tecnocapclosures.com/metal-packaging-group/), [C.L. Smith Metal Cans](https://www.clsmith.com/packaging-solutions/metal-cans/), [Witop Tinplate Classification Guide](https://www.witoptinplate.com/metal-packaging-can-containers/) |
