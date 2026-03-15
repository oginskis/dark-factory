# SKU Schema: Computers & Peripherals

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 6XK89EA, N82E16883360282, CTX4070 |
| Product Name | text | Full product name including key specs such as brand, model, processor, and form factor | Dell OptiPlex 7020 SFF Desktop Intel Core i5-14500, ASUS ROG Strix G16 Gaming Laptop |
| URL | text | Direct link to the product page | https://example.com/product/dell-optiplex-7020 |
| Price | number | Numeric unit price excluding currency symbol | 849.99, 1299.00, 2499.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, JPY |
| Brand | text | Manufacturer or brand name | Dell, HP, Lenovo, ASUS, Apple, Acer, MSI |
| Product Type | enum | Primary device category | Desktop, Laptop, All-in-One, Mini PC, Workstation, Thin Client, Chromebook |
| Model Number | text | Manufacturer model or part number | OptiPlex 7020, ThinkPad T14s Gen 5, MacBook Pro 16 |
| Processor Brand | enum | CPU manufacturer | Intel, AMD, Apple, Qualcomm |
| Processor Model | text | Full processor name including generation and tier | Intel Core i7-14700, AMD Ryzen 9 9950X, Apple M4 Pro |
| Processor Cores | number | Total number of CPU cores | 6, 8, 12, 16, 24 |
| Processor Base Clock | number (GHz) | Base operating frequency of the processor | 1.8, 2.5, 3.4, 4.7 |
| Processor Boost Clock | number (GHz) | Maximum turbo or boost frequency of the processor | 4.8, 5.2, 5.6 |
| RAM Capacity | number (GB) | Installed system memory | 8, 16, 32, 64, 96, 128 |
| RAM Type | enum | Memory technology generation | DDR4, DDR5, LPDDR5, LPDDR5X |
| Storage Capacity | text | Primary storage size | 256GB, 512GB, 1TB, 2TB, 4TB |
| Storage Type | enum | Primary storage technology | SSD, NVMe SSD, HDD, eMMC, SSD + HDD |
| Graphics Card | text | Discrete or integrated GPU model | NVIDIA GeForce RTX 5070, AMD Radeon RX 9070 XT, Intel UHD Graphics 770, Apple M4 GPU |
| Graphics Memory | number (GB) | Dedicated video memory capacity (discrete GPU only) | 4, 8, 12, 16, 24 |
| Display Size | number (inches) | Screen diagonal for laptops and all-in-ones | 13.3, 14, 15.6, 16, 17.3, 23.8, 27 |
| Display Resolution | text | Native screen resolution in pixels | 1920x1080, 2560x1440, 2560x1600, 3840x2160 |
| Operating System | text | Pre-installed operating system | Windows 11 Home, Windows 11 Pro, macOS Sequoia, Chrome OS, Ubuntu |
| Form Factor | enum | Physical chassis design | Tower, Small Form Factor, Ultra Small, Mini PC, Clamshell, Convertible, All-in-One |
| Connectivity Ports | text (list) | Available physical ports | USB-A 3.2, USB-C, Thunderbolt 4, HDMI 2.1, DisplayPort 1.4, Ethernet RJ-45, SD Card |
| Wireless Connectivity | text (list) | Wireless networking and communication standards | Wi-Fi 6E, Wi-Fi 7, Bluetooth 5.3, Bluetooth 5.4 |
| Ethernet Speed | text | Maximum wired network speed | 1 Gbps, 2.5 Gbps, 10 Gbps |
| Battery Capacity | number (Wh) | Battery size for portable devices | 54, 72, 86, 100 |
| Weight | number (kg) | Total device weight | 1.24, 1.85, 2.50, 7.80 |
| Height | number (mm) | Chassis height or thickness | 15.5, 17.9, 344, 427 |
| Width | number (mm) | Chassis width | 312, 356, 170, 396 |
| Depth | number (mm) | Chassis depth | 221, 252, 170, 340 |
| Webcam | text | Built-in camera resolution and features | 720p, 1080p, 1080p IR, 5MP, None |
| Power Supply | number (W) | Power supply unit wattage for desktops or adapter wattage for laptops | 65, 90, 140, 500, 750, 1000 |
| Color | text | Exterior chassis color or finish | Black, Silver, Space Gray, Midnight, White |
| Warranty | text | Manufacturer warranty duration | 1 Year, 2 Years, 3 Years |
| Energy Certification | text (list) | Energy efficiency and environmental certifications | ENERGY STAR, EPEAT Gold, EPEAT Silver, TCO Certified |
| Security Features | text (list) | Built-in hardware security capabilities | TPM 2.0, Fingerprint Reader, IR Camera, Kensington Lock Slot |
| Country of Origin | text | Country where the product was manufactured or assembled | China, Taiwan, USA, Mexico, Czech Republic |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 38 attributes from 4 sources plus industry data standards | [Newegg Desktops](https://www.newegg.com/Desktop-Computer/Category/ID-228), [CDW PC Towers](https://www.cdw.com/category/computers/desktops/towers/?w=CA4), [B&H Photo Laptops](https://www.bhphotovideo.com/c/buy/laptops/ci/18818), [Dell Desktops](https://www.dell.com/en-us/shop/desktop-computers/scr/desktops) |
