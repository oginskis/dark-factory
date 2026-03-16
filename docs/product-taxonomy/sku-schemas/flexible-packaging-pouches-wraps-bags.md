# SKU Schema: Flexible Packaging (Pouches, Wraps, Bags)

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.flexible`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Manufacturer or distributor product identifier | EPAC-SUP-8X10, GR-3SS-6X9, PPC-FLAT-5X7 |
| Product Name | product_name | text | — | Full product name including format, material, and key dimensions | Metalized Stand-Up Pouch 8x10x3, Clear 3-Side-Seal Flat Pouch 6x9, Kraft Side-Gusset Bag 5x7x2 |
| URL | url | text | — | Direct link to the product page | https://example.com/pouches/metalized-sup-8x10 |
| Price | price | number | — | Numeric price per unit or per thousand, excluding currency symbol | 0.15, 0.45, 120.00, 350.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Material Structure | material_structure | text | — | Shorthand notation of laminate layers from outside to inside | PET/PE, PET/AL/PE, PET/MPET/PE, OPP/OPP, Paper/AL/PE, Nylon/PE |
| Closure Type | closure_type | text (list) | — | Reclosure or opening features built into the pouch | Zipper (Press-to-Close), Slider Zipper, Spout, Tear Notch, Peel-and-Reseal, Valve, Hang Hole, None |
| Seal Type | seal_type | enum | — | Method used to create the pouch seals | Heat Seal, Ultrasonic, Cold Seal |
| Country of Origin | country_of_origin | text | — | Country where the flexible packaging is manufactured | USA, China, India, Germany, Thailand, Vietnam |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Pouch Style | pouch_style | enum | — | Structural format of the flexible package | Stand-Up Pouch (SUP), 3-Side-Seal Flat, Pillow Pouch, Side-Gusset Bag, Quad-Seal, Sachet, Roll Stock, Wrap/Film |
| Width | width | number | mm | Finished pouch width (face dimension) | 100, 152, 203, 254, 305 |
| Height | height | number | mm | Finished pouch height (face dimension) | 127, 178, 254, 305, 381 |
| Gusset Depth | gusset_depth | number | mm | Bottom or side gusset depth for stand-up and gusseted formats | 50, 64, 76, 89, 102 |
| Fill Volume | fill_volume | number | mL | Nominal internal volume capacity of the pouch | 100, 250, 500, 1000, 2000, 5000 |
| Total Thickness | total_thickness | number | um | Combined thickness of all laminate layers in micrometres | 60, 80, 100, 120, 150, 200 |
| Number of Layers | number_of_layers | number | — | Count of material plies in the laminate structure | 2, 3, 4 |
| Outer Layer | outer_layer | text | — | Material of the outermost printed layer | PET, OPP, Nylon, Paper, BOPA |
| Barrier Layer | barrier_layer | text | — | Material of the middle barrier layer if present | Aluminum Foil, Metalized PET (MPET), EVOH, SiOx, AlOx, PVDC, None |
| Sealant Layer | sealant_layer | text | — | Material of the inner heat-seal layer | LLDPE, LDPE, CPP, Ionomer, mPE |
| Oxygen Transmission Rate | oxygen_transmission_rate | number | cc/m2/day | OTR measured at 23C 0% RH per ASTM D3985 or ASTM F1927 | 0.01, 0.5, 1.0, 5.0, 50, 1500 |
| Moisture Vapor Transmission Rate | moisture_vapor_transmission_rate | number | g/m2/day | MVTR measured at 38C 90% RH per ASTM F1249 | 0.01, 0.5, 1.0, 3.0, 10, 15 |
| Printing Method | printing_method | enum | — | Primary print technology used on the pouch | Flexography, Rotogravure, Digital (HP Indigo), Offset |
| Print Colors | print_colors | number | — | Maximum number of ink colors in the design | 1, 4, 8, 10 |
| Print Finish | print_finish | enum | — | Surface appearance of the printed pouch exterior | Gloss, Matte, Soft-Touch, Registered Matte/Gloss, Metallic |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 manufacturers plus barrier property standards (ASTM D3985 OTR, ASTM F1249 MVTR) | [ePac Flexibles](https://epacflexibles.com/products/), [Glenroy Stand-Up Pouches](https://www.glenroy.com/flexible-packaging/stand-up-pouches/), [Mondi Flexible Packaging](https://northamerica.mondigroup.com/products-solutions/flexible-packaging-bags-and-pouches/), [EcoEnclose Metalized Pouches](https://www.ecoenclose.com/metalized-pcr-stand-up-pouch-7-x-9-x-3/) |
