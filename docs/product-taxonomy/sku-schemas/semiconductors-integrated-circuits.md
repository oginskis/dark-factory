# SKU Schema: Semiconductors & Integrated Circuits

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.semiconductors_ics`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Distributor or retailer stock-keeping identifier | 296-1395-5-ND, 579-MCP2551-ISN, 511-L7805CV |
| Product Name | product_name | text | — | Full product name including manufacturer part number, function, and package | STM32F103C8T6 ARM Cortex-M3 MCU 64KB Flash LQFP-48, LM7805 Linear Voltage Regulator 5V TO-220 |
| URL | url | text | — | Direct link to the product page on a distributor or manufacturer site | https://example.com/product/stm32f103c8t6 |
| Price | price | number | — | Numeric unit price at a given quantity break, excluding currency symbol | 0.45, 2.89, 15.60 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY |
| IC Type | ic_type | text | — | Functional category of the integrated circuit | Microcontroller, Voltage Regulator, Op-Amp, ADC, DAC, Gate Driver, Memory, FPGA, Timer, Interface IC |
| Package Type | package_type | text | — | Physical IC package designation | SOIC-8, TQFP-48, LQFP-64, QFN-32, BGA-256, DIP-14, SOT-23-5, SSOP-20, TO-220 |
| Mounting Type | mounting_type | enum | — | Method by which the component is attached to the PCB | Surface Mount (SMD/SMT), Through Hole, Chip |
| Packaging Format | packaging_format | enum | — | How components are packaged for shipping and assembly | Cut Tape, Tape and Reel, Tray, Tube, Bulk |
| Supply Voltage Min | supply_voltage_min | number | V | Minimum operating supply voltage | 1.8, 2.7, 3.0, 4.5 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Manufacturer | manufacturer | text | — | Semiconductor company that designed and fabricated the device | Texas Instruments, STMicroelectronics, Microchip, NXP, Infineon, Analog Devices, onsemi |
| Manufacturer Part Number | manufacturer_part_number | text | — | Official part number assigned by the manufacturer | STM32F103C8T6, LM7805CT, ATmega328P-AU, AD7606BSTZ |
| Description | description | text | — | Brief functional description of the device | 8-Bit AVR Microcontroller with 32KB Flash, Quad 2-Input NAND Gate |
| Operating Temperature Min | operating_temperature_min | number | C | Lower bound of the operating temperature range in degrees Celsius | -40, -20, 0 |
| Operating Temperature Max | operating_temperature_max | number | C | Upper bound of the operating temperature range in degrees Celsius | 85, 105, 125, 150 |
| Lead Pitch | lead_pitch | number | mm | Center-to-center distance between adjacent leads or pads | 0.4, 0.5, 0.65, 0.8, 1.0, 1.27, 2.54 |
| Clock Speed Max | clock_speed_max | number | MHz | Maximum clock frequency for processors, microcontrollers, and FPGAs | 8, 16, 48, 72, 168, 550 |
| Number of I/O Lines | number_of_io_lines | number | — | Count of general-purpose input/output pins available to the user | 11, 23, 37, 51, 86 |
| Number of ADC Channels | number_of_adc_channels | number | — | Number of analog-to-digital converter input channels | 1, 4, 8, 12, 16 |
| ADC Resolution | adc_resolution | number | bits | Resolution of the on-chip analog-to-digital converter | 8, 10, 12, 16, 24 |
| Output Current per Pin | output_current_per_pin | number | mA | Maximum current source or sink capability per output pin | 4, 8, 20, 25 |
| Quiescent Current | quiescent_current | number | uA | Current drawn by the device when idle or in standby mode | 0.5, 5.0, 45, 500 |
| Power Dissipation | power_dissipation | number | mW | Maximum power the device can dissipate at rated temperature | 100, 250, 500, 1000, 2000 |
| Data Bus Width | data_bus_width | number | bits | Width of the internal or external data bus | 8, 16, 32, 64 |
| Communication Interfaces | communication_interfaces | text (list) | — | On-chip communication peripherals | UART, SPI, I2C, CAN, USB, Ethernet, I2S |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (JEDEC packaging, IPC moisture sensitivity, RoHS directive) | [Digi-Key](https://www.digikey.com/en/products/category/integrated-circuits-ics/32), [Mouser](https://www.mouser.com/c/semiconductors/), [Octopart](https://octopart.com/), [LCSC Electronics](https://www.lcsc.com/) |
