# SKU Schema: Semiconductors & Integrated Circuits

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Distributor or retailer stock-keeping identifier | 296-1395-5-ND, 579-MCP2551-ISN, 511-L7805CV |
| Product Name | text | Full product name including manufacturer part number, function, and package | STM32F103C8T6 ARM Cortex-M3 MCU 64KB Flash LQFP-48, LM7805 Linear Voltage Regulator 5V TO-220 |
| URL | text | Direct link to the product page on a distributor or manufacturer site | https://example.com/product/stm32f103c8t6 |
| Price | number | Numeric unit price at a given quantity break, excluding currency symbol | 0.45, 2.89, 15.60 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Manufacturer | text | Semiconductor company that designed and fabricated the device | Texas Instruments, STMicroelectronics, Microchip, NXP, Infineon, Analog Devices, onsemi |
| Manufacturer Part Number | text | Official part number assigned by the manufacturer | STM32F103C8T6, LM7805CT, ATmega328P-AU, AD7606BSTZ |
| IC Type | text | Functional category of the integrated circuit | Microcontroller, Voltage Regulator, Op-Amp, ADC, DAC, Gate Driver, Memory, FPGA, Timer, Interface IC |
| Description | text | Brief functional description of the device | 8-Bit AVR Microcontroller with 32KB Flash, Quad 2-Input NAND Gate |
| Supply Voltage Min | number (V) | Minimum operating supply voltage | 1.8, 2.7, 3.0, 4.5 |
| Supply Voltage Max | number (V) | Maximum operating supply voltage | 3.6, 5.5, 18, 36 |
| Operating Temperature Min | number (C) | Lower bound of the operating temperature range in degrees Celsius | -40, -20, 0 |
| Operating Temperature Max | number (C) | Upper bound of the operating temperature range in degrees Celsius | 85, 105, 125, 150 |
| Package Type | text | Physical IC package designation | SOIC-8, TQFP-48, LQFP-64, QFN-32, BGA-256, DIP-14, SOT-23-5, SSOP-20, TO-220 |
| Mounting Type | enum | Method by which the component is attached to the PCB | Surface Mount (SMD/SMT), Through Hole, Chip |
| Pin Count | number | Total number of pins or pads on the package | 8, 14, 28, 48, 64, 100, 144, 256 |
| Lead Pitch | number (mm) | Center-to-center distance between adjacent leads or pads | 0.4, 0.5, 0.65, 0.8, 1.0, 1.27, 2.54 |
| Clock Speed Max | number (MHz) | Maximum clock frequency for processors, microcontrollers, and FPGAs | 8, 16, 48, 72, 168, 550 |
| Flash Memory Size | number (KB) | On-chip non-volatile program memory capacity for microcontrollers and processors | 8, 32, 64, 128, 256, 512, 1024 |
| RAM Size | number (KB) | On-chip volatile data memory capacity | 1, 4, 20, 64, 128, 256 |
| Number of I/O Lines | number | Count of general-purpose input/output pins available to the user | 11, 23, 37, 51, 86 |
| Number of ADC Channels | number | Number of analog-to-digital converter input channels | 1, 4, 8, 12, 16 |
| ADC Resolution | number (bits) | Resolution of the on-chip analog-to-digital converter | 8, 10, 12, 16, 24 |
| Output Current per Pin | number (mA) | Maximum current source or sink capability per output pin | 4, 8, 20, 25 |
| Quiescent Current | number (uA) | Current drawn by the device when idle or in standby mode | 0.5, 5.0, 45, 500 |
| Power Dissipation | number (mW) | Maximum power the device can dissipate at rated temperature | 100, 250, 500, 1000, 2000 |
| Data Bus Width | number (bits) | Width of the internal or external data bus | 8, 16, 32, 64 |
| Communication Interfaces | text (list) | On-chip communication peripherals | UART, SPI, I2C, CAN, USB, Ethernet, I2S |
| Logic Family | text | Logic standard or voltage level family for digital ICs | CMOS, TTL, LVTTL, LVCMOS, ECL |
| RoHS Status | enum | Compliance with the Restriction of Hazardous Substances directive | Compliant, Non-Compliant, Exempt |
| Lifecycle Status | enum | Current production and availability status | Active, NRND (Not Recommended for New Designs), Obsolete, Preview |
| Lead Free Status | text | Whether the component leads and terminations are lead-free | Lead Free, Contains Lead, Lead Free / RoHS Compliant |
| Moisture Sensitivity Level | text | IPC/JEDEC moisture sensitivity classification for reflow soldering | MSL 1, MSL 2, MSL 3, MSL 4 |
| Datasheet URL | text | Direct link to the manufacturer datasheet PDF | https://example.com/datasheet/stm32f103.pdf |
| Minimum Order Quantity | number | Minimum number of units that can be ordered | 1, 10, 100, 2500 |
| Packaging Format | enum | How components are packaged for shipping and assembly | Cut Tape, Tape and Reel, Tray, Tube, Bulk |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (JEDEC packaging, IPC moisture sensitivity, RoHS directive) | [Digi-Key](https://www.digikey.com/en/products/category/integrated-circuits-ics/32), [Mouser](https://www.mouser.com/c/semiconductors/), [Octopart](https://octopart.com/), [LCSC Electronics](https://www.lcsc.com/) |
