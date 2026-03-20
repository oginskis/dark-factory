# SKU Schema: Sensors & Instrumentation

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.sensors_instrumentation`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | PX309-100GI, TMP36GT9Z, 52PG26 |
| Product Name | product_name | text | — | yes | Full product name including key specs such as sensor type, range, and output | IFM Digital Pressure Sensor SPST 0-3620 psi, Pt100 RTD Probe 4-Wire 300mm |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/pressure-transducer-px309 |
| Price | price | number | — | yes | Numeric price per unit, excluding currency symbol | 5.60, 89.50, 425.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Sensor Type | sensor_type | text | — | — | Primary measurement principle or sensing technology | RTD, Thermocouple, Strain Gauge, Capacitive, Inductive, Photoelectric, Ultrasonic, Piezoelectric, MEMS |
| Output Type | output_type | text | — | — | Electrical signal format the sensor produces | 4-20 mA, 0-10 V, 0-5 V, Digital/I2C, Digital/SPI, RS-485, IO-Link, NPN, PNP, Relay |
| Sensing Element Material | sensing_element_material | text | — | — | Material or construction of the primary sensing element | Platinum (Pt100/Pt1000), Type K (Chromel-Alumel), Type J (Iron-Constantan), Silicon, Ceramic |
| Housing Material | housing_material | text | — | — | Material of the sensor body or enclosure | Stainless Steel 316, Aluminium, ABS, Nylon, Brass, Ceramic |
| Connector Type | connector_type | text | — | — | Electrical connector used for cable attachment | M8, M12, DIN 43650, Cable Gland, Flying Leads, Terminal Block |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the sensor was manufactured | USA, Germany, Japan, China, Switzerland |
| Measurand | measurand | enum | — | — | Physical quantity the sensor detects or measures | Temperature, Pressure, Flow, Level, Proximity, Humidity, Acceleration, Force, Vibration, Position, Gas Concentration |
| Measurement Range Min | measurement_range_min | number | — | — | Lower bound of the measurement range in the native unit | -200, 0, -40, -1 |
| Measurement Range Max | measurement_range_max | number | — | — | Upper bound of the measurement range in the native unit | 200, 850, 3620, 10000 |
| Measurement Unit | measurement_unit | text | — | — | Engineering unit for the measured quantity | deg C, psi, bar, L/min, mm, g, %RH, ppm |
| Accuracy | accuracy | text | — | — | Maximum deviation from true value, expressed as a percentage or absolute value | +-0.1%, +-0.5 deg C, +-1% FS, +-0.25% BFSL |
| Resolution | resolution | text | — | — | Smallest detectable change in the measured quantity | 0.01 deg C, 0.1 psi, 1 mm, 12-bit |
| Response Time | response_time | text | — | — | Time for the sensor output to reach a stated percentage of its final value after a step change | 10 ms, 100 ms, 1 s, T0.5 = 15 s |
| Power Consumption | power_consumption | number | W | — | Maximum power drawn during operation | 0.001, 0.05, 1.5, 5.0 |
| Wire Configuration | wire_configuration | text | — | — | Number of lead wires for resistance-based sensors | 2-Wire, 3-Wire, 4-Wire |
| Sensing Distance/Range | sensing_distancerange | text | — | — | Maximum detection distance for proximity, photoelectric, or ultrasonic sensors | 4 mm, 15 mm, 100 mm, 2 m, 10 m |
| Process Connection | process_connection | text | — | — | Mechanical fitting used to mount the sensor in a pipe, tank, or process line | 1/4 NPT, 1/2 BSP, G1/4, M20x1.5, Tri-Clamp |
| IP Rating | ip_rating | text | — | — | Ingress protection rating per IEC 60529 | IP54, IP65, IP67, IP68, IP69K |
| Operating Temperature Min | operating_temperature_min | number | deg C | — | Minimum ambient operating temperature for the sensor electronics | -40, -20, -10, 0 |
| Operating Temperature Max | operating_temperature_max | number | deg C | — | Maximum ambient operating temperature for the sensor electronics | 70, 85, 125, 150 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 33 attributes from 4 sources plus industry standards (IEC 60751, IEC 61298, NAMUR NE 43) | [Omega Engineering](https://www.dwyeromega.com/en-us/), [Digi-Key](https://www.digikey.com/en/products/category/sensors-transducers/25), [Grainger](https://www.grainger.com/category/test-instruments/pressure-vacuum-measurement/pressure-and-vacuum-transmitters/general-purpose-pressure-transmitters), [TE Connectivity](https://www.te.com/en/products/sensors/temperature-sensors/rtd-sensors.html) |
