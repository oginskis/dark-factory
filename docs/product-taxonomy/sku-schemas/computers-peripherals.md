# SKU Schema: Computers & Peripherals

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.computers_peripherals`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | 6XK89EA, N82E16883360282, CTX4070 |
| Product Name | product_name | text | Full product name including key specs such as brand, model, processor, and form factor | Dell OptiPlex 7020 SFF Desktop Intel Core i5-14500, ASUS ROG Strix G16 Gaming Laptop |
| URL | url | text | Direct link to the product page | https://example.com/product/dell-optiplex-7020 |
| Price | price | number | Numeric unit price excluding currency symbol | 849.99, 1299.00, 2499.95 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, JPY |
| Product Type | product_type | enum | Primary device category | Desktop, Laptop, All-in-One, Mini PC, Workstation, Thin Client, Chromebook |
| Model Number | model_number | text | Manufacturer model or part number | OptiPlex 7020, ThinkPad T14s Gen 5, MacBook Pro 16 |
| RAM Type | ram_type | enum | Memory technology generation | DDR4, DDR5, LPDDR5, LPDDR5X |
| Storage Type | storage_type | enum | Primary storage technology | SSD, NVMe SSD, HDD, eMMC, SSD + HDD |
| Form Factor | form_factor | enum | Physical chassis design | Tower, Small Form Factor, Ultra Small, Mini PC, Clamshell, Convertible, All-in-One |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the product was manufactured or assembled | China, Taiwan, USA, Mexico, Czech Republic |
| Processor Brand | processor_brand | enum | CPU manufacturer | Intel, AMD, Apple, Qualcomm |
| Processor Model | processor_model | text | Full processor name including generation and tier | Intel Core i7-14700, AMD Ryzen 9 9950X, Apple M4 Pro |
| Processor Cores | processor_cores | number | Total number of CPU cores | 6, 8, 12, 16, 24 |
| Processor Base Clock | processor_base_clock | number (GHz) | Base operating frequency of the processor | 1.8, 2.5, 3.4, 4.7 |
| Processor Boost Clock | processor_boost_clock | number (GHz) | Maximum turbo or boost frequency of the processor | 4.8, 5.2, 5.6 |
| Graphics Card | graphics_card | text | Discrete or integrated GPU model | NVIDIA GeForce RTX 5070, AMD Radeon RX 9070 XT, Intel UHD Graphics 770, Apple M4 GPU |
| Graphics Memory | graphics_memory | number (GB) | Dedicated video memory capacity (discrete GPU only) | 4, 8, 12, 16, 24 |
| Display Resolution | display_resolution | text | Native screen resolution in pixels | 1920x1080, 2560x1440, 2560x1600, 3840x2160 |
| Operating System | operating_system | text | Pre-installed operating system | Windows 11 Home, Windows 11 Pro, macOS Sequoia, Chrome OS, Ubuntu |
| Connectivity Ports | connectivity_ports | text (list) | Available physical ports | USB-A 3.2, USB-C, Thunderbolt 4, HDMI 2.1, DisplayPort 1.4, Ethernet RJ-45, SD Card |
| Wireless Connectivity | wireless_connectivity | text (list) | Wireless networking and communication standards | Wi-Fi 6E, Wi-Fi 7, Bluetooth 5.3, Bluetooth 5.4 |
| Ethernet Speed | ethernet_speed | text | Maximum wired network speed | 1 Gbps, 2.5 Gbps, 10 Gbps |
| Height | height | number (mm) | Chassis height or thickness | 15.5, 17.9, 344, 427 |
| Width | width | number (mm) | Chassis width | 312, 356, 170, 396 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 38 attributes from 4 sources plus industry data standards | [Newegg Desktops](https://www.newegg.com/Desktop-Computer/Category/ID-228), [CDW PC Towers](https://www.cdw.com/category/computers/desktops/towers/?w=CA4), [B&H Photo Laptops](https://www.bhphotovideo.com/c/buy/laptops/ci/18818), [Dell Desktops](https://www.dell.com/en-us/shop/desktop-computers/scr/desktops) |
