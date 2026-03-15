# SKU Schema: Sensors & Instrumentation

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | PX309-100GI, TMP36GT9Z, 52PG26 |
| Product Name | text | Full product name including key specs such as sensor type, range, and output | IFM Digital Pressure Sensor SPST 0-3620 psi, Pt100 RTD Probe 4-Wire 300mm |
| URL | text | Direct link to the product page | https://example.com/product/pressure-transducer-px309 |
| Price | number | Numeric price per unit, excluding currency symbol | 5.60, 89.50, 425.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Sensor or instrument manufacturer name | Omega, Honeywell, TE Connectivity, IFM, Banner Engineering, Siemens, Bosch |
| Sensor Type | text | Primary measurement principle or sensing technology | RTD, Thermocouple, Strain Gauge, Capacitive, Inductive, Photoelectric, Ultrasonic, Piezoelectric, MEMS |
| Measurand | enum | Physical quantity the sensor detects or measures | Temperature, Pressure, Flow, Level, Proximity, Humidity, Acceleration, Force, Vibration, Position, Gas Concentration |
| Measurement Range Min | number | Lower bound of the measurement range in the native unit | -200, 0, -40, -1 |
| Measurement Range Max | number | Upper bound of the measurement range in the native unit | 200, 850, 3620, 10000 |
| Measurement Unit | text | Engineering unit for the measured quantity | deg C, psi, bar, L/min, mm, g, %RH, ppm |
| Accuracy | text | Maximum deviation from true value, expressed as a percentage or absolute value | +-0.1%, +-0.5 deg C, +-1% FS, +-0.25% BFSL |
| Resolution | text | Smallest detectable change in the measured quantity | 0.01 deg C, 0.1 psi, 1 mm, 12-bit |
| Response Time | text | Time for the sensor output to reach a stated percentage of its final value after a step change | 10 ms, 100 ms, 1 s, T0.5 = 15 s |
| Output Type | text | Electrical signal format the sensor produces | 4-20 mA, 0-10 V, 0-5 V, Digital/I2C, Digital/SPI, RS-485, IO-Link, NPN, PNP, Relay |
| Supply Voltage | text | Required input power voltage range | 10-30 VDC, 5 VDC, 24 VDC, 3.3 VDC, 85-264 VAC |
| Power Consumption | number (W) | Maximum power drawn during operation | 0.001, 0.05, 1.5, 5.0 |
| Sensing Element Material | text | Material or construction of the primary sensing element | Platinum (Pt100/Pt1000), Type K (Chromel-Alumel), Type J (Iron-Constantan), Silicon, Ceramic |
| Wire Configuration | text | Number of lead wires for resistance-based sensors | 2-Wire, 3-Wire, 4-Wire |
| Sensing Distance/Range | text | Maximum detection distance for proximity, photoelectric, or ultrasonic sensors | 4 mm, 15 mm, 100 mm, 2 m, 10 m |
| Process Connection | text | Mechanical fitting used to mount the sensor in a pipe, tank, or process line | 1/4 NPT, 1/2 BSP, G1/4, M20x1.5, Tri-Clamp |
| Probe Length | number (mm) | Insertion length of the sensing probe or element | 50, 100, 200, 300, 500 |
| Probe Diameter | number (mm) | Outside diameter of the sensing probe sheath | 1.5, 3, 6, 8, 12 |
| Housing Material | text | Material of the sensor body or enclosure | Stainless Steel 316, Aluminium, ABS, Nylon, Brass, Ceramic |
| IP Rating | text | Ingress protection rating per IEC 60529 | IP54, IP65, IP67, IP68, IP69K |
| Operating Temperature Min | number (deg C) | Minimum ambient operating temperature for the sensor electronics | -40, -20, -10, 0 |
| Operating Temperature Max | number (deg C) | Maximum ambient operating temperature for the sensor electronics | 70, 85, 125, 150 |
| Media Temperature Max | number (deg C) | Maximum temperature of the fluid or medium in contact with the sensing element | 150, 260, 500, 850 |
| Connector Type | text | Electrical connector used for cable attachment | M8, M12, DIN 43650, Cable Gland, Flying Leads, Terminal Block |
| Display | enum | Whether the sensor has an integrated readout | Yes, No |
| Dimensions (L x W x H) | text (mm) | Overall sensor body dimensions | 30 x 18 x 12, 80 x 40 x 35, 150 x 25 dia |
| Weight | number (g) | Mass of the sensor unit without packaging | 15, 50, 120, 350 |
| Certifications | text (list) | Safety, hazardous-area, and regulatory approvals | CE, UL, ATEX, IECEx, RoHS, SIL 2, FM, CSA |
| Country of Origin | text | Country where the sensor was manufactured | USA, Germany, Japan, China, Switzerland |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 33 attributes from 4 sources plus industry standards (IEC 60751, IEC 61298, NAMUR NE 43) | [Omega Engineering](https://www.dwyeromega.com/en-us/), [Digi-Key](https://www.digikey.com/en/products/category/sensors-transducers/25), [Grainger](https://www.grainger.com/category/test-instruments/pressure-vacuum-measurement/pressure-and-vacuum-transmitters/general-purpose-pressure-transmitters), [TE Connectivity](https://www.te.com/en/products/sensors/temperature-sensors/rtd-sensors.html) |
