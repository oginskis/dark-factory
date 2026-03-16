# SKU Schema: Plastic Containers & Packaging

**Last updated:** 2026-03-15
**Parent category:** Plastics & Rubber Products
**Taxonomy ID:** `plastics.containers_packaging`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Supplier or manufacturer product identifier | SKS-PET-BOS-8OZ, FHP-200CC-38, OBK-HDPE-32-JR |
| Product Name | product_name | text | — | Full product name including container type, material, volume, and color | 8 oz Clear PET Boston Round Bottle, 200cc White HDPE Packer Bottle 38-400, 32 oz Natural HDPE Wide Mouth Jar |
| URL | url | text | — | Direct link to the product page | https://example.com/products/pet-boston-round-8oz-clear |
| Price | price | number | — | Numeric price per unit or per case, excluding currency symbol | 0.35, 0.85, 12.50, 95.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Container Type | container_type | enum | — | Primary container classification | Bottle, Jar, Jug, Tub, Pail, Vial, Tube, Canister, Drum, Airless Bottle, Foamer Bottle, Roll-On |
| Material | material | enum | — | Primary plastic material of the container body | PET, HDPE, LDPE, PP, PVC, PS, PETG, PCR PET, PCR HDPE, Bioplastic |
| Closure Type | closure_type | text | — | Compatible closure or cap type | Continuous Thread Cap, Child Resistant Cap, Flip Top Cap, Disc Top Cap, Pump Dispenser, Trigger Sprayer, Fine Mist Sprayer, Dropper, Press-On Cap, Tamper Evident Band |
| Mouth Type | mouth_type | enum | — | Opening width classification | Narrow Mouth, Standard Mouth, Wide Mouth |
| Country of Origin | country_of_origin | text | — | Country where the container was manufactured | USA, China, Canada, Mexico, India |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Neck Finish | neck_finish | text | — | GPI/SPI neck finish designation (diameter/thread style) | 20-410, 24-400, 24-410, 28-400, 33-400, 38-400, 43-400, 53-400, 63-400, 89-400 |
| Shape | shape | enum | — | Body shape of the container | Boston Round, Cosmo Round, Cylinder, Square, Oblong, Oval, Bullet, Straight Sided, Tapered |
| Color | color | text | — | Color of the container body | Clear, Natural, Amber, White, Black, Blue, Green, Cobalt, Frosted, Purple |
| Height | height | number | mm | Overall height of the container including neck | 60, 95, 130, 165, 200, 250 |
| Wall Thickness | wall_thickness | number | mm | Nominal wall thickness of the container body | 0.3, 0.5, 0.8, 1.0, 1.5, 2.0 |
| Label Panel Height | label_panel_height | number | mm | Height of the flat labeling area on the container body | 30, 50, 70, 90, 120 |
| Barrier Properties | barrier_properties | text | — | Special barrier layers or coatings for shelf life extension | None, UV Protection, Oxygen Barrier, Moisture Barrier, Multi-Layer Co-Extrusion |
| PCR Content | pcr_content | number | % | Percentage of post-consumer recycled content in the container | 0, 25, 30, 50, 100 |
| FDA Compliant | fda_compliant | enum | — | Whether the container meets FDA food-contact requirements (21 CFR) | Yes, No |
| BPA Free | bpa_free | enum | — | Whether the container is free of bisphenol A | Yes, No |
| Resin Identification Code | resin_identification_code | text | — | SPI resin identification code molded into the container | 1 (PET), 2 (HDPE), 3 (PVC), 4 (LDPE), 5 (PP), 6 (PS), 7 (Other) |
| Industry Application | industry_application | text (list) | — | Target industries for the container | Personal Care, Pharmaceutical, Food and Beverage, Nutraceutical, Chemical, Household, Pet Care, Agriculture, Cannabis |
| Case Pack Quantity | case_pack_quantity | number | — | Number of containers per case or carton | 12, 24, 48, 72, 120, 250, 500 |
| Decoration Options | decoration_options | text (list) | — | Available decoration or labeling methods | Screen Printing, Hot Stamping, Pressure Sensitive Label, Shrink Sleeve, Pad Printing, Embossing |
| Certification | certification | text (list) | — | Quality, regulatory, or sustainability certifications | ISO 9001, cGMP, SQF, BRC, FDA registered, CPSC compliant |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 companies plus industry standards (GPI/SPI neck finish standards, SPI resin identification codes, ASTM D2911 bottle dimensions) | [SKS Bottle and Packaging](https://www.sks-bottle.com/), [FH Packaging](https://fhpkg.com/product-category/plastic-containers/), [O.Berk](https://www.oberk.com/containers/plastic), [Silgan Plastics](https://www.silganplastics.com/product-solutions/bottles-jars/) |
