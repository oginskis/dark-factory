# SKU Schema: HVAC Equipment

**Last updated:** 2026-03-15
**Parent category:** Machinery & Industrial Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 4TTV0024A1000C, WS024GMFI20HLD, 819RZ3 |
| Product Name | text | Full product name including key specs such as type, tonnage, and efficiency | Trane XV20i 2 Ton 20 SEER Variable Stage AC Condenser, Pioneer 24000 BTU 18 SEER2 Ductless Mini-Split |
| URL | text | Direct link to the product page | https://example.com/product/xv20i-2ton |
| Price | number | Numeric price per unit excluding currency symbol | 11628.90, 1899.00, 3450.00 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, GBP |
| Brand/Manufacturer | text | Equipment manufacturer or brand name | Trane, Carrier, Daikin, Fujitsu, Goodman, Lennox, Pioneer, Mitsubishi, Friedrich |
| Equipment Type | enum | Primary HVAC equipment category | Central Air Conditioner, Heat Pump, Furnace, Mini-Split, Package Unit, Boiler, Air Handler, Chiller, Unit Heater |
| System Configuration | enum | Installation and ductwork configuration | Split System, Packaged System, Ductless Mini-Split, Multi-Zone Mini-Split, PTAC, VRF |
| Model Number | text | Manufacturer model number | 4TTV0024A1000C, FHPW142AC1, WYS024GMFI22RL |
| Cooling Capacity | number (BTU/h) | Rated cooling output in BTU per hour | 12000, 24000, 36000, 48000, 60000 |
| Tonnage | number | Cooling capacity in tons (1 ton = 12000 BTU/h) | 1.5, 2, 2.5, 3, 4, 5 |
| Heating Capacity | number (BTU/h) | Rated heating output in BTU per hour | 24000, 28100, 40000, 80000 |
| SEER2 | number | Seasonal Energy Efficiency Ratio 2 rating | 14, 16, 18, 20, 23.6 |
| EER2 | number | Energy Efficiency Ratio 2 at 95F outdoor temperature | 7.8, 9.0, 11.0, 12.5 |
| HSPF2 | number | Heating Seasonal Performance Factor 2 for heat pumps | 6.6, 7.8, 8.6, 10.0 |
| COP | number | Coefficient of Performance at rated conditions | 1.78, 3.03, 3.5, 4.2 |
| Voltage | text | Input electrical voltage requirement | 115V, 208/230V, 208-230/460V, 277/480V |
| Phase | text | Electrical phase configuration | 1Ph, 3Ph |
| Frequency | text (Hz) | Electrical supply frequency | 60, 50/60 |
| Breaker Size | text (A) | Required circuit breaker amperage | 15A, 20A, 30A, 40A, 60A |
| Refrigerant Type | text | Refrigerant used in the system | R-410A, R-32, R-454B, R-134a |
| Compressor Type | enum | Type of compressor technology | Single Stage, Two Stage, Variable Speed, Scroll, Rotary, Reciprocating, Inverter |
| Airflow Rate | number (CFM) | Maximum airflow in cubic feet per minute | 353, 450, 588, 800, 1200 |
| Sound Level - Indoor | number (dB) | Indoor unit noise level at rated conditions | 25, 35, 39.5, 45.5 |
| Sound Level - Outdoor | number (dB) | Outdoor unit noise level at rated conditions | 52, 56, 60, 68, 76 |
| Indoor Unit Dimensions (W x D x H) | text (in) | Indoor unit width, depth, and height | 42.5 x 8.875 x 13.125, 28 x 9.5 x 11.5 |
| Outdoor Unit Dimensions (W x D x H) | text (in) | Outdoor unit or condenser width, depth, and height | 35 x 13.5 x 26.5, 31.5 x 31.5 x 37 |
| Unit Weight | number (lbs) | Net weight of the primary unit | 30, 81, 97.9, 185, 250 |
| Shipping Weight | number (lbs) | Gross weight including packaging | 38.6, 104.6, 210, 300 |
| Coverage Area | text (sq ft) | Recommended room or area size | 350-500, 650-900, 1000-1500 |
| Line Set Size | text (in) | Refrigerant line set diameters (liquid/suction) | 1/4 x 3/8, 3/8 x 5/8, 3/8 x 3/4 |
| Maximum Line Set Length | number (ft) | Maximum allowable distance between indoor and outdoor units | 25, 50, 75, 100, 164 |
| AHRI Certification Number | text | AHRI-certified reference number for performance verification | 210039845, 7100503 |
| Energy Star Certified | boolean | Whether the unit meets Energy Star requirements | Yes, No |
| Annual Cooling Cost | number | Estimated annual cooling operating cost in local currency | 176, 225, 350 |
| Certifications | text (list) | Safety and performance certifications | AHRI, UL, ETL, CSA, Energy Star, CE |
| Warranty - Parts | text | Duration of parts warranty | 5 years, 10 years |
| Warranty - Compressor | text | Duration of compressor warranty | 5 years, 10 years, Lifetime |
| Country of Origin | text | Country where the unit is manufactured | USA, China, Thailand, Japan, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 39 attributes from 4 companies plus AHRI/DOE efficiency standards (SEER2, EER2, HSPF2) | [Pioneer Mini-Split](https://www.pioneerminisplit.com/products/24-000-btu-ductless-dc-inverter-mini-split-air-conditioner-heat-pump-230-vac), [Trane Residential](https://www.trane.com/residential/en/products/air-conditioners/), [ACWholesalers](https://www.acwholesalers.com/), [Grainger HVAC](https://www.grainger.com/category/hvac-and-refrigeration/air-conditioners-accessories/air-conditioners) |
