# SKU Schema: HVAC Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment
**Taxonomy ID:** `machinery.hvac`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 4TTV0024A1000C, WS024GMFI20HLD, 819RZ3 |
| Product Name | product_name | text | — | Full product name including key specs such as type, tonnage, and efficiency | Trane XV20i 2 Ton 20 SEER Variable Stage AC Condenser, Pioneer 24000 BTU 18 SEER2 Ductless Mini-Split |
| URL | url | text | — | Direct link to the product page | https://example.com/product/xv20i-2ton |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 11628.90, 1899.00, 3450.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, CAD, EUR, GBP |
| Equipment Type | equipment_type | enum | — | Primary HVAC equipment category | Central Air Conditioner, Heat Pump, Furnace, Mini-Split, Package Unit, Boiler, Air Handler, Chiller, Unit Heater |
| Model Number | model_number | text | — | Manufacturer model number | 4TTV0024A1000C, FHPW142AC1, WYS024GMFI22RL |
| Refrigerant Type | refrigerant_type | text | — | Refrigerant used in the system | R-410A, R-32, R-454B, R-134a |
| Compressor Type | compressor_type | enum | — | Type of compressor technology | Single Stage, Two Stage, Variable Speed, Scroll, Rotary, Reciprocating, Inverter |
| Country of Origin | country_of_origin | text | — | Country where the unit is manufactured | USA, China, Thailand, Japan, Mexico |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| System Configuration | system_configuration | enum | — | Installation and ductwork configuration | Split System, Packaged System, Ductless Mini-Split, Multi-Zone Mini-Split, PTAC, VRF |
| Tonnage | tonnage | number | ton | Cooling capacity in tons (1 ton = 12000 BTU/h) | 1.5, 2, 2.5, 3, 4, 5 |
| SEER2 | seer2 | number | — | Seasonal Energy Efficiency Ratio 2 rating | 14, 16, 18, 20, 23.6 |
| EER2 | eer2 | number | — | Energy Efficiency Ratio 2 at 95F outdoor temperature | 7.8, 9.0, 11.0, 12.5 |
| HSPF2 | hspf2 | number | — | Heating Seasonal Performance Factor 2 for heat pumps | 6.6, 7.8, 8.6, 10.0 |
| COP | cop | number | — | Coefficient of Performance at rated conditions | 1.78, 3.03, 3.5, 4.2 |
| Phase | phase | text | — | Electrical phase configuration | 1Ph, 3Ph |
| Frequency | frequency | text | Hz | Electrical supply frequency | 60, 50/60 |
| Airflow Rate | airflow_rate | number | CFM | Maximum airflow in cubic feet per minute | 353, 450, 588, 800, 1200 |
| Sound Level - Indoor | sound_level_-_indoor | number | dB | Indoor unit noise level at rated conditions | 25, 35, 39.5, 45.5 |
| Sound Level - Outdoor | sound_level_-_outdoor | number | dB | Outdoor unit noise level at rated conditions | 52, 56, 60, 68, 76 |
| Indoor Unit Dimensions (W x D x H) | indoor_unit_dimensions_w_x_d_x_h | text | in | Indoor unit width, depth, and height | 42.5 x 8.875 x 13.125, 28 x 9.5 x 11.5 |
| Outdoor Unit Dimensions (W x D x H) | outdoor_unit_dimensions_w_x_d_x_h | text | in | Outdoor unit or condenser width, depth, and height | 35 x 13.5 x 26.5, 31.5 x 31.5 x 37 |
| Coverage Area | coverage_area | text | sq ft | Recommended room or area size | 350-500, 650-900, 1000-1500 |
| AHRI Certification Number | ahri_certification_number | text | — | AHRI-certified reference number for performance verification | 210039845, 7100503 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 39 attributes from 4 companies plus AHRI/DOE efficiency standards (SEER2, EER2, HSPF2) | [Pioneer Mini-Split](https://www.pioneerminisplit.com/products/24-000-btu-ductless-dc-inverter-mini-split-air-conditioner-heat-pump-230-vac), [Trane Residential](https://www.trane.com/residential/en/products/air-conditioners/), [ACWholesalers](https://www.acwholesalers.com/), [Grainger HVAC](https://www.grainger.com/category/hvac-and-refrigeration/air-conditioners-accessories/air-conditioners) |
