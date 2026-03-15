# SKU Schema: Mobile Phones & Tablets

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.mobile_phones_tablets`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | SM-S928BZKDEUB, MWXF3LL/A, GA06157-US |
| Product Name | text | Full product name including brand, model, storage, and color | Samsung Galaxy S25 Ultra 512GB Titanium Black, Apple iPhone 16 Pro Max 256GB, Google Pixel 9 Pro 128GB |
| URL | text | Direct link to the product page | https://example.com/product/galaxy-s25-ultra |
| Price | number | Numeric unit price excluding currency symbol | 799.99, 1199.00, 449.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Device Type | enum | Primary device category | Smartphone, Tablet, Phablet, Foldable Phone, Foldable Tablet |
| Model Number | text | Manufacturer internal model identifier | SM-S928B, A2894, GVU6C |
| Display Type | text | Panel technology used in the screen | Dynamic AMOLED 2X, Super Retina XDR OLED, LTPO AMOLED, IPS LCD |
| SIM Type | text | SIM card format supported | Nano-SIM, Dual Nano-SIM, eSIM, Nano-SIM + eSIM |
| Body Material | text | Primary materials used in the chassis and frame | Aluminum, Titanium, Glass, Ceramic, Polycarbonate |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the device was manufactured | China, Vietnam, India, South Korea |
| Operating System | text | Pre-installed operating system and version | Android 15, iOS 18, iPadOS 18, HarmonyOS 4 |
| Chipset | text | System-on-chip model name | Qualcomm Snapdragon 8 Elite, Apple A18 Pro, Google Tensor G4, MediaTek Dimensity 9400 |
| RAM | number (GB) | Installed system memory | 6, 8, 12, 16 |
| Internal Storage | text | Built-in storage capacity | 64GB, 128GB, 256GB, 512GB, 1TB |
| Expandable Storage | boolean | Whether the device supports a microSD or similar card slot | true, false |
| Display Resolution | text | Native screen resolution in pixels | 1080x2340, 1290x2796, 2420x1668, 2752x2064 |
| Refresh Rate | number (Hz) | Maximum display refresh rate | 60, 90, 120, 144 |
| Peak Brightness | number (nits) | Maximum display brightness | 1200, 1600, 2000, 2600 |
| Main Camera | text | Primary rear camera resolution and key feature | 50MP OIS, 200MP OIS, 48MP |
| Camera System | text (list) | All rear camera modules with resolutions | 50MP wide + 12MP ultrawide + 10MP telephoto 3x, 48MP main + 12MP ultrawide + 12MP telephoto 5x |
| Front Camera | text | Selfie camera resolution | 12MP, 16MP, 32MP |
| Video Recording | text | Maximum video recording capability | 8K at 30fps, 4K at 120fps, 4K at 60fps |
| Wired Charging | number (W) | Maximum wired charging speed | 15, 25, 45, 67, 120 |
| Wireless Charging | number (W) | Maximum wireless charging speed (0 if not supported) | 0, 7.5, 15, 25 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus GSMArena spec standards | [GSMArena Samsung Galaxy S25](https://www.gsmarena.com/samsung_galaxy_s25-13610.php), [Apple iPad Pro Specs](https://www.apple.com/ipad-pro/specs/), [Best Buy Tablets](https://www.bestbuy.com/site/shop/android-tablets), [Google Pixel Tablet Specs](https://store.google.com/product/pixel_tablet_specs?hl=en-US) |
