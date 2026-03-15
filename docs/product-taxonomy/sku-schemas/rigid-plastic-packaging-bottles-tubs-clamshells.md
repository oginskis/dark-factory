# SKU Schema: Rigid Plastic Packaging (Bottles, Tubs, Clamshells)

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.rigid_plastic`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | TB-027123, VP-CS-200, IND-TR-4X6 |
| Product Name | product_name | text | Full product name including capacity, material, and format | 12 oz Natural HDPE Cylinder Round Bottle 38-400, Clear PET Clamshell 6x4x2, White PP Tub 16 oz with Lid |
| URL | url | text | Direct link to the product page | https://example.com/bottles/hdpe-12oz-cylinder |
| Price | price | number | Numeric price per unit or per case, excluding currency symbol | 0.22, 0.85, 45.00, 120.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Container Type | container_type | enum | Broad format classification of the plastic package | Bottle, Jar, Tub, Clamshell, Blister Pack, Tray, Vial, Canister, Jug |
| Resin Type | resin_type | enum | Primary plastic resin used in manufacturing | PET (1), HDPE (2), PVC (3), LDPE (4), PP (5), PS (6), Other (7) |
| Neck Finish Type | neck_finish_type | enum | Thread configuration of the bottle opening | Continuous Thread (CT), Lug, Snap-On, Press-On, Twist-Off (T/O), Child-Resistant (CR) |
| Country of Origin | country_of_origin | text | Country where the container is manufactured | USA, Canada, China, Mexico, India |
| Capacity | capacity | number (mL) | Nominal volume capacity of the container | 30, 60, 120, 250, 355, 473, 946, 3785 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Neck Finish | neck_finish | text | GPI/SPI standard neck finish code specifying thread diameter and style | 18-400, 20-410, 24-410, 28-400, 33-400, 38-400, 45-400, 53-400, 63-400, 89-400, 110-400 |
| Body Shape | body_shape | enum | Geometric profile of the container body | Round, Boston Round, Cylinder, Square, Oblong, Oval, Packer, Bullet, French Square, Custom |
| Height | height | number (mm) | Overall height of the container from base to top of finish | 50, 89, 127, 165, 200, 254, 305 |
| Width | width | number (mm) | Body width for non-round containers | 51, 76, 102, 127, 152, 203 |
| Wall Thickness | wall_thickness | number (mm) | Average wall thickness of the container body | 0.25, 0.38, 0.51, 0.76, 1.0, 1.5 |
| Color | color | text | Container body color | Natural, White, Amber, Clear, Blue, Green, Black, Custom |
| Opacity | opacity | enum | Light transmission characteristic of the container | Transparent, Translucent, Opaque |
| Manufacturing Process | manufacturing_process | enum | Primary forming process used to create the container | Injection Blow Molding (IBM), Extrusion Blow Molding (EBM), Injection Stretch Blow Molding (ISBM), Thermoforming, Injection Molding |
| Closure Included | closure_included | enum | Whether a matching closure or lid is supplied with the container | Yes, No, Sold Separately |
| Tamper Evidence | tamper_evidence | enum | Type of tamper-evident feature if present | None, Shrink Band, Break-Away Ring, Induction Seal, Snap Lock, Peel Tab |
| Food Contact Compliance | food_contact_compliance | enum | Whether the container meets food-contact safety requirements | FDA 21 CFR, EU 10/2011, Not Food Grade |
| BPA Free | bpa_free | enum | Whether the container is free of Bisphenol A | Yes, No |
| Recycled Content | recycled_content | number (%) | Percentage of post-consumer recycled (PCR) resin in the container | 0, 15, 25, 50, 100 |
| Certification | certification | text (list) | Regulatory and quality certifications | FDA, cGMP, ISO 9001, SQF, BRC, Kosher |
| Case Pack Quantity | case_pack_quantity | number | Number of containers per case or carton | 12, 24, 48, 72, 120, 250, 500 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus industry standards (GPI/SPI neck finish codes, ASTM D7611 resin identification, FDA 21 CFR) | [TricorBraun Bottles](https://www.tricorbraun.com/12-oz-natural-hdpe-plastic-cylinder-round-bottle-38-400-neck-finish-027123.html), [VisiPak Clamshells](https://www.visipak.com/clamshell-packaging/), [Indepak Rigid Packaging](https://indepak.com/rigid-packaging-materials-options/), [Alpha Packaging HDPE Catalog](https://www.pretiumpkg.com/wp-content/uploads/2021/04/Alpha_HDPE_PP_Stock_Product_Catalog.pdf) |
