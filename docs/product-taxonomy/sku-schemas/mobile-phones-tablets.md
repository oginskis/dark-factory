# SKU Schema: Mobile Phones & Tablets

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.mobile_phones_tablets`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | SM-S928BZKDEUB, MWXF3LL/A, GA06157-US |
| Product Name | product_name | text | — | yes | Full product name including brand, model, storage, and color | Samsung Galaxy S25 Ultra 512GB Titanium Black, Apple iPhone 16 Pro Max 256GB, Google Pixel 9 Pro 128GB |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/galaxy-s25-ultra |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 799.99, 1199.00, 449.95 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Device Type | device_type | enum | — | — | Primary device category | Smartphone, Tablet, Phablet, Foldable Phone, Foldable Tablet |
| Model Number | model_number | text | — | — | Manufacturer internal model identifier | SM-S928B, A2894, GVU6C |
| Display Type | display_type | text | — | — | Panel technology used in the screen | Dynamic AMOLED 2X, Super Retina XDR OLED, LTPO AMOLED, IPS LCD |
| SIM Type | sim_type | text | — | — | SIM card format supported | Nano-SIM, Dual Nano-SIM, eSIM, Nano-SIM + eSIM |
| Body Material | body_material | text | — | — | Primary materials used in the chassis and frame | Aluminum, Titanium, Glass, Ceramic, Polycarbonate |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the device was manufactured | China, Vietnam, India, South Korea |
| Operating System | operating_system | text | — | — | Pre-installed operating system and version | Android 15, iOS 18, iPadOS 18, HarmonyOS 4 |
| Chipset | chipset | text | — | — | System-on-chip model name | Qualcomm Snapdragon 8 Elite, Apple A18 Pro, Google Tensor G4, MediaTek Dimensity 9400 |
| RAM | ram | number | GB | — | Installed system memory | 6, 8, 12, 16 |
| Internal Storage | internal_storage | text | — | — | Built-in storage capacity | 64GB, 128GB, 256GB, 512GB, 1TB |
| Expandable Storage | expandable_storage | boolean | — | — | Whether the device supports a microSD or similar card slot | true, false |
| Display Resolution | display_resolution | text | — | — | Native screen resolution in pixels | 1080x2340, 1290x2796, 2420x1668, 2752x2064 |
| Refresh Rate | refresh_rate | number | Hz | — | Maximum display refresh rate | 60, 90, 120, 144 |
| Peak Brightness | peak_brightness | number | nits | — | Maximum display brightness | 1200, 1600, 2000, 2600 |
| Main Camera | main_camera | text | — | — | Primary rear camera resolution and key feature | 50MP OIS, 200MP OIS, 48MP |
| Camera System | camera_system | text (list) | — | — | All rear camera modules with resolutions | 50MP wide + 12MP ultrawide + 10MP telephoto 3x, 48MP main + 12MP ultrawide + 12MP telephoto 5x |
| Front Camera | front_camera | text | — | — | Selfie camera resolution | 12MP, 16MP, 32MP |
| Video Recording | video_recording | text | — | — | Maximum video recording capability | 8K at 30fps, 4K at 120fps, 4K at 60fps |
| Wired Charging | wired_charging | number | W | — | Maximum wired charging speed | 15, 25, 45, 67, 120 |
| Wireless Charging | wireless_charging | number | W | — | Maximum wireless charging speed (0 if not supported) | 0, 7.5, 15, 25 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus GSMArena spec standards | [GSMArena Samsung Galaxy S25](https://www.gsmarena.com/samsung_galaxy_s25-13610.php), [Apple iPad Pro Specs](https://www.apple.com/ipad-pro/specs/), [Best Buy Tablets](https://www.bestbuy.com/site/shop/android-tablets), [Google Pixel Tablet Specs](https://store.google.com/product/pixel_tablet_specs?hl=en-US) |
