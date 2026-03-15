# SKU Schema: Oil & Gas Field Equipment (Drill Bits, Wellheads, Valves)

**Last updated:** 2026-03-15
**Parent category:** Energy Equipment & Storage
**Taxonomy ID:** `energy.oil_gas_field_equipment`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Manufacturer or distributor product identifier | FC-2916-5K, HCR-3016-10K, PDC-812-M |
| Product Name | product_name | text | Full product name including type, size, and pressure class | Cameron FC 2-9/16 5000 PSI Slab Gate Valve, 8-1/2 in PDC Drill Bit 5-Blade Matrix Body |
| URL | url | text | Direct link to the product page | https://example.com/product/fc-gate-valve-2916 |
| Price | price | number | Numeric unit price excluding currency symbol | 3450.00, 12500.00, 850.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CNY |
| Equipment Type | equipment_type | enum | High-level product category | Drill Bit, Gate Valve, Wellhead Assembly, Choke Valve, Christmas Tree, Casing Head, Tubing Head Spool |
| Performance Requirement Level | performance_requirement_level | enum | API 6A performance requirement level for testing validation | PR 1, PR 2 |
| Material Class | material_class | enum | API 6A material class designation | AA, BB, CC, DD, EE, FF, HH |
| Body Material | body_material | text | Primary material of the valve or equipment body | Low-Alloy Steel, Carbon Steel, Stainless Steel, Duplex Stainless Steel, Inconel 718 |
| Connection Type | connection_type | text | End connection or flange type | Flanged (API 6BX), Studded, Threaded, Weco Union, Clamp Hub |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Bit Type | bit_type | enum | Drill bit design classification | PDC, Tricone (Roller Cone), Diamond Impregnated, Hybrid |
| Body Type | body_type | enum | Bit body construction material (for drill bits) | Matrix, Steel |
| Seal Type | seal_type | text | Primary sealing mechanism | Metal-to-Metal, Soft Seat, Resilient Seat, Lip Seal, Ring Gasket (BX, RX, R) |
| Stem Type | stem_type | enum | Valve stem design | Rising Stem, Non-Rising Stem |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | USA, China, United Kingdom, India |
| Working Pressure | working_pressure | number (PSI) | Rated working pressure per API 6A | 2000, 3000, 5000, 10000, 15000, 20000 |
| API Standard | api_standard | text (list) | Applicable API specification numbers | API 6A, API 16A, API 16C, API 7-1 |
| Product Specification Level | product_specification_level | enum | API 6A product specification level indicating quality and testing requirements | PSL 1, PSL 2, PSL 3, PSL 3G, PSL 4 |
| Temperature Rating | temperature_rating | enum | API 6A temperature class designating the rated operating range | K (-60 to 82 C), L (-46 to 82 C), P (-29 to 82 C), R (ambient), S (-18 to 121 C), T (-18 to 180 C), U (-18 to 121 C), V (2 to 121 C) |
| NACE Compliance | nace_compliance | enum | Sour service compliance per NACE MR-0175/ISO 15156 | Compliant, Non-Compliant |
| IADC Code | iadc_code | text | International Association of Drilling Contractors classification code | M432, S223, 517, 637 |
| Number of Blades/Cones | number_of_bladescones | number | Number of cutting blades (PDC) or roller cones (tricone) | 3, 4, 5, 6, 7, 8 |
| Actuation Method | actuation_method | enum | How the valve or device is operated | Manual (Handwheel), Hydraulic, Pneumatic, Ball Screw, Spring Return |
| Flow Direction | flow_direction | enum | Whether the valve seals in one or both directions | Unidirectional, Bi-directional |
| Overall Dimensions (L x W x H) | overall_dimensions_l_x_w_x_h | text (mm) | External envelope dimensions of the equipment | 450 x 350 x 600, 1200 x 800 x 900 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (API 6A, IADC bit classification, NACE MR-0175) | [SLB Cameron](https://www.slb.com/valves/api-spec-6a-technologies/api-spec-6a-gate-valves), [AQE Machinery](https://www.aqemachinery.com/product-list-wellhead-equipment.html), [Baker Hughes Drill Bits](https://dam.bakerhughes.com/m/70246e3a57c19fcf/original/Baker-Hughes-Drill-Bits-Catalog.pdf), [Rockpecker IADC Guide](https://www.rockpecker.com/drilling-news/2023/11/6/understanding-iadc-codes-a-guide-to-picking-the-right-tricone-and-pdc-drill-bit) |
