# SKU Schema: Optical & Photographic Equipment (Cameras, Lenses, Binoculars)

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.optical_photographic`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 1890, DB-214, 1765622-REG, SEL70200GM2 |
| Product Name | product_name | text | — | Full product name including brand, model, and key specs | Nikon Z6III Mirrorless Camera Body, Vortex Diamondback HD 8x42 Binoculars, Canon RF 70-200mm f/2.8L IS USM |
| URL | url | text | — | Direct link to the product page | https://example.com/product/nikon-z6iii |
| Price | price | number | — | Numeric retail price excluding currency symbol | 319.99, 1299.99, 2499.95, 6496.95 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Product Type | product_type | enum | — | Primary equipment category | Mirrorless Camera, DSLR Camera, Compact Camera, Interchangeable Lens, Binoculars, Spotting Scope, Telescope, Monocular, Rangefinder |
| Sensor Type | sensor_type | text | — | Image sensor technology used in the camera | CMOS, BSI CMOS, Stacked CMOS, CCD |
| Sensor Format | sensor_format | text | — | Physical sensor size classification | Full Frame (FX), APS-C (DX), Micro Four Thirds, Medium Format, 1-inch |
| Prism Type | prism_type | text | — | Optical prism design used in binoculars | Roof (Schmidt-Pechan), Roof (Abbe-Koenig), Porro |
| Viewfinder Type | viewfinder_type | text | — | Type of viewfinder on the camera | OLED EVF (5760k-dot), Optical Pentaprism, LCD |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Body/Chassis Material | bodychassis_material | text | — | Primary construction material | Magnesium Alloy, Polycarbonate, Aluminum, Rubber Armored |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | Japan, China, Thailand, USA |
| Effective Megapixels | effective_megapixels | number | — | Effective pixel count in megapixels | 20.1, 24.5, 45.7, 50.1, 61 |
| ISO Range | iso_range | text | — | Native and expanded sensitivity range | 100-51200, 64-25600, Expanded to 204800 |
| Autofocus System | autofocus_system | text | — | Type of autofocus technology | Hybrid Phase-Detection/Contrast, Dual Pixel CMOS AF II, Phase Detection |
| Autofocus Points | autofocus_points | number | — | Number of selectable focus points or coverage zones | 51, 153, 273, 693, 1053 |
| Continuous Shooting Speed | continuous_shooting_speed | number | fps | Maximum frames per second in burst mode | 7, 10, 14, 20, 30, 120 |
| Shutter Speed Range | shutter_speed_range | text | — | Minimum and maximum shutter speeds | 1/8000 to 30s, 1/16000 to 30s (electronic) |
| Video Resolution | video_resolution | text | — | Maximum video recording resolution and frame rate | 4K 60p, 6K 60p, 8K 30p |
| Image Stabilization | image_stabilization | text | — | Type and effectiveness of built-in stabilization | 5-Axis In-Body (8 stops), Optical IS, Dual IS II, None |
| Lens Mount | lens_mount | text | — | Lens mount system for interchangeable lens cameras | Nikon Z, Canon RF, Sony E, Fujifilm X, Leica L, Micro Four Thirds |
| Maximum Aperture | maximum_aperture | text | — | Widest aperture of the lens | f/1.4, f/1.8, f/2.8, f/4, f/5.6-6.3 |
| Magnification | magnification | text | — | Magnification power for binoculars and spotting scopes | 8x, 10x, 12x, 15x, 20-60x |
| Field of View | field_of_view | text | — | Angular or linear field of view | 6.2 degrees, 325 ft at 1000 yds, 7.4 degrees |
| Eye Relief | eye_relief | number | mm | Distance from the eyepiece to the eye point | 15, 17, 18, 20 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus CIPA standards for camera specifications | [Nikon](https://www.nikonusa.com/), [B&H Photo](https://www.bhphotovideo.com/), [Vortex Optics](https://vortexoptics.com/), [Canon](https://www.usa.canon.com/) |
