# SKU Schema: Optical & Photographic Equipment (Cameras, Lenses, Binoculars)

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 1890, DB-214, 1765622-REG, SEL70200GM2 |
| Product Name | text | Full product name including brand, model, and key specs | Nikon Z6III Mirrorless Camera Body, Vortex Diamondback HD 8x42 Binoculars, Canon RF 70-200mm f/2.8L IS USM |
| URL | text | Direct link to the product page | https://example.com/product/nikon-z6iii |
| Price | number | Numeric retail price excluding currency symbol | 319.99, 1299.99, 2499.95, 6496.95 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand/Manufacturer | text | Company that produces the equipment | Nikon, Canon, Sony, Fujifilm, Leica, Vortex, Swarovski, Zeiss, Olympus |
| Product Type | enum | Primary equipment category | Mirrorless Camera, DSLR Camera, Compact Camera, Interchangeable Lens, Binoculars, Spotting Scope, Telescope, Monocular, Rangefinder |
| Sensor Type | text | Image sensor technology used in the camera | CMOS, BSI CMOS, Stacked CMOS, CCD |
| Sensor Format | text | Physical sensor size classification | Full Frame (FX), APS-C (DX), Micro Four Thirds, Medium Format, 1-inch |
| Sensor Size | text (mm) | Physical dimensions of the image sensor | 35.9 x 23.9, 23.5 x 15.7, 17.3 x 13, 43.8 x 32.9 |
| Effective Megapixels | number | Effective pixel count in megapixels | 20.1, 24.5, 45.7, 50.1, 61 |
| ISO Range | text | Native and expanded sensitivity range | 100-51200, 64-25600, Expanded to 204800 |
| Autofocus System | text | Type of autofocus technology | Hybrid Phase-Detection/Contrast, Dual Pixel CMOS AF II, Phase Detection |
| Autofocus Points | number | Number of selectable focus points or coverage zones | 51, 153, 273, 693, 1053 |
| Continuous Shooting Speed | number (fps) | Maximum frames per second in burst mode | 7, 10, 14, 20, 30, 120 |
| Shutter Speed Range | text | Minimum and maximum shutter speeds | 1/8000 to 30s, 1/16000 to 30s (electronic) |
| Video Resolution | text | Maximum video recording resolution and frame rate | 4K 60p, 6K 60p, 8K 30p |
| Image Stabilization | text | Type and effectiveness of built-in stabilization | 5-Axis In-Body (8 stops), Optical IS, Dual IS II, None |
| Lens Mount | text | Lens mount system for interchangeable lens cameras | Nikon Z, Canon RF, Sony E, Fujifilm X, Leica L, Micro Four Thirds |
| Focal Length | text (mm) | Focal length for lenses or fixed-lens cameras | 24-70, 70-200, 50, 100-400, 14-24 |
| Maximum Aperture | text | Widest aperture of the lens | f/1.4, f/1.8, f/2.8, f/4, f/5.6-6.3 |
| Magnification | text | Magnification power for binoculars and spotting scopes | 8x, 10x, 12x, 15x, 20-60x |
| Objective Lens Diameter | number (mm) | Diameter of the front objective lens element | 28, 42, 50, 56, 85 |
| Field of View | text | Angular or linear field of view | 6.2 degrees, 325 ft at 1000 yds, 7.4 degrees |
| Eye Relief | number (mm) | Distance from the eyepiece to the eye point | 15, 17, 18, 20 |
| Close Focus Distance | number (m) | Minimum focusing distance | 0.3, 0.45, 1.2, 2 |
| Prism Type | text | Optical prism design used in binoculars | Roof (Schmidt-Pechan), Roof (Abbe-Koenig), Porro |
| Lens Coating | text | Anti-reflection coating type on optical surfaces | Fully Multi-Coated, XR Anti-Reflective, ArmorTek, Super Spectra |
| Viewfinder Type | text | Type of viewfinder on the camera | OLED EVF (5760k-dot), Optical Pentaprism, LCD |
| Display | text | Rear display type and specifications | 3.2-inch Vari-Angle Touchscreen, 3-inch Tilting LCD |
| Weather Sealing | enum | Level of dust and moisture resistance | Weather Sealed, Splash Resistant, Nitrogen Purged/Fogproof, IP67, None |
| Body/Chassis Material | text | Primary construction material | Magnesium Alloy, Polycarbonate, Aluminum, Rubber Armored |
| Dimensions (W x H x D) | text (mm) | Physical dimensions of the product | 138.5 x 101.5 x 74, 130 x 102 x 67 |
| Product Weight | number (g) | Weight of the product body only (without batteries or lens) | 375, 580, 670, 1015, 1340 |
| Storage | text (list) | Memory card types and slot configuration | Dual CFexpress Type B + SD UHS-II, Single SD, CompactFlash |
| Connectivity | text (list) | Communication interfaces | USB-C, HDMI Type A, Wi-Fi 802.11ac, Bluetooth 5.0, GPS, NFC |
| Battery Life | text | Rated number of shots or recording time per charge | 360 shots, 500 shots, 100 min video |
| Country of Origin | text | Country where the product is manufactured | Japan, China, Thailand, USA |
| Warranty | text | Manufacturer warranty duration | 1 Year, 2 Year, Limited Lifetime, VIP Lifetime |
| UPC/EAN | text | Universal Product Code or European Article Number | 018208019090, 875874008489 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus CIPA standards for camera specifications | [Nikon](https://www.nikonusa.com/), [B&H Photo](https://www.bhphotovideo.com/), [Vortex Optics](https://vortexoptics.com/), [Canon](https://www.usa.canon.com/) |
