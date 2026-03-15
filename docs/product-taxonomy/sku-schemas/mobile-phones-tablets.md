# SKU Schema: Mobile Phones & Tablets

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SM-S928BZKDEUB, MWXF3LL/A, GA06157-US |
| Product Name | text | Full product name including brand, model, storage, and color | Samsung Galaxy S25 Ultra 512GB Titanium Black, Apple iPhone 16 Pro Max 256GB, Google Pixel 9 Pro 128GB |
| URL | text | Direct link to the product page | https://example.com/product/galaxy-s25-ultra |
| Price | number | Numeric unit price excluding currency symbol | 799.99, 1199.00, 449.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Brand | text | Device manufacturer | Samsung, Apple, Google, Xiaomi, OnePlus, Motorola, Sony |
| Device Type | enum | Primary device category | Smartphone, Tablet, Phablet, Foldable Phone, Foldable Tablet |
| Model Number | text | Manufacturer internal model identifier | SM-S928B, A2894, GVU6C |
| Operating System | text | Pre-installed operating system and version | Android 15, iOS 18, iPadOS 18, HarmonyOS 4 |
| Chipset | text | System-on-chip model name | Qualcomm Snapdragon 8 Elite, Apple A18 Pro, Google Tensor G4, MediaTek Dimensity 9400 |
| RAM | number (GB) | Installed system memory | 6, 8, 12, 16 |
| Internal Storage | text | Built-in storage capacity | 64GB, 128GB, 256GB, 512GB, 1TB |
| Expandable Storage | boolean | Whether the device supports a microSD or similar card slot | true, false |
| Display Size | number (inches) | Screen diagonal measurement | 6.1, 6.7, 6.9, 10.9, 11.0, 12.9, 13.0 |
| Display Type | text | Panel technology used in the screen | Dynamic AMOLED 2X, Super Retina XDR OLED, LTPO AMOLED, IPS LCD |
| Display Resolution | text | Native screen resolution in pixels | 1080x2340, 1290x2796, 2420x1668, 2752x2064 |
| Refresh Rate | number (Hz) | Maximum display refresh rate | 60, 90, 120, 144 |
| Peak Brightness | number (nits) | Maximum display brightness | 1200, 1600, 2000, 2600 |
| Main Camera | text | Primary rear camera resolution and key feature | 50MP OIS, 200MP OIS, 48MP |
| Camera System | text (list) | All rear camera modules with resolutions | 50MP wide + 12MP ultrawide + 10MP telephoto 3x, 48MP main + 12MP ultrawide + 12MP telephoto 5x |
| Front Camera | text | Selfie camera resolution | 12MP, 16MP, 32MP |
| Video Recording | text | Maximum video recording capability | 8K at 30fps, 4K at 120fps, 4K at 60fps |
| Battery Capacity | number (mAh) | Battery size | 3000, 4000, 4685, 5000, 6000 |
| Wired Charging | number (W) | Maximum wired charging speed | 15, 25, 45, 67, 120 |
| Wireless Charging | number (W) | Maximum wireless charging speed (0 if not supported) | 0, 7.5, 15, 25 |
| SIM Type | text | SIM card format supported | Nano-SIM, Dual Nano-SIM, eSIM, Nano-SIM + eSIM |
| 5G Support | boolean | Whether the device supports 5G cellular networks | true, false |
| Wi-Fi Standard | text | Highest supported wireless networking standard | Wi-Fi 6, Wi-Fi 6E, Wi-Fi 7 |
| Bluetooth Version | text | Bluetooth specification version | 5.2, 5.3, 5.4, 6.0 |
| NFC | boolean | Whether near-field communication is supported | true, false |
| USB Port | text | Charging and data port type and standard | USB-C 3.2, USB-C 2.0, Lightning, Thunderbolt/USB 4 |
| Biometric Authentication | text (list) | Built-in biometric security methods | In-display Fingerprint, Face ID, Side Fingerprint, Iris Scanner |
| IP Rating | text | Ingress protection rating for dust and water resistance | IP68, IP67, IP65, IPX8 |
| Height | number (mm) | Device body height | 146.9, 160.1, 249.7, 281.6 |
| Width | number (mm) | Device body width | 70.5, 77.6, 177.5, 215.5 |
| Thickness | number (mm) | Device body depth or thickness | 5.1, 7.2, 7.6, 8.3 |
| Weight | number (g) | Device weight without accessories | 162, 199, 227, 444, 579, 682 |
| Body Material | text | Primary materials used in the chassis and frame | Aluminum, Titanium, Glass, Ceramic, Polycarbonate |
| Color | text | Device exterior color or finish | Titanium Black, Space Black, Natural Titanium, Silver, Obsidian, Porcelain |
| Country of Origin | text | Country where the device was manufactured | China, Vietnam, India, South Korea |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus GSMArena spec standards | [GSMArena Samsung Galaxy S25](https://www.gsmarena.com/samsung_galaxy_s25-13610.php), [Apple iPad Pro Specs](https://www.apple.com/ipad-pro/specs/), [Best Buy Tablets](https://www.bestbuy.com/site/shop/android-tablets), [Google Pixel Tablet Specs](https://store.google.com/product/pixel_tablet_specs?hl=en-US) |
