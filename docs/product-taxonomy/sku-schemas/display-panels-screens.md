# SKU Schema: Display Panels & Screens

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 27GP850-B, LS32BG852NNXGO, PA278QV, C4422QN |
| Product Name | text | Full product name including brand, size, resolution, and key feature | LG 27GP850-B 27-inch QHD Nano IPS Gaming Monitor, Samsung Odyssey Neo G8 32-inch 4K Curved Monitor |
| URL | text | Direct link to the product page | https://example.com/product/lg-27gp850-b |
| Price | number | Numeric unit price excluding currency symbol | 179.99, 599.00, 1299.95, 4999.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Brand | text | Display manufacturer or brand | LG, Samsung, Dell, ASUS, BenQ, ViewSonic, Acer, MSI, Philips, NEC |
| Product Type | enum | Primary display category | Computer Monitor, Gaming Monitor, Professional Monitor, Digital Signage Display, Video Wall Panel, Touch Display, Portable Monitor |
| Model Number | text | Manufacturer model or part number | 27GP850-B, U2723QE, PA278QV, C4422QN |
| Screen Size | number (inches) | Viewable screen diagonal measurement | 15.6, 24, 27, 32, 34, 43, 49, 55, 65, 86 |
| Panel Type | enum | Display panel technology | IPS, VA, TN, OLED, QD-OLED, Mini LED, Nano IPS, Fast IPS |
| Native Resolution | text | Pixel resolution at native setting | 1920x1080, 2560x1440, 3440x1440, 3840x2160, 5120x2880 |
| Resolution Label | enum | Common marketing name for the resolution | Full HD, QHD, WQHD, UHD 4K, 5K, 8K |
| Refresh Rate | number (Hz) | Maximum panel refresh rate | 60, 75, 100, 144, 165, 240, 360, 480 |
| Response Time | number (ms) | Pixel response time (grey-to-grey or MPRT) | 0.03, 0.5, 1, 4, 5, 8 |
| Adaptive Sync | text | Variable refresh rate technology supported | NVIDIA G-Sync, G-Sync Compatible, AMD FreeSync, FreeSync Premium, FreeSync Premium Pro, None |
| Aspect Ratio | text | Display width to height ratio | 16:9, 16:10, 21:9, 32:9, 32:10 |
| Curvature | text | Screen curvature radius (Flat if not curved) | Flat, 1000R, 1500R, 1800R, 3800R |
| Brightness | number (nits) | Typical sustained brightness | 250, 350, 400, 600, 1000, 2000 |
| Peak Brightness | number (nits) | Maximum HDR peak brightness | 400, 600, 1000, 1400, 2000 |
| Contrast Ratio | text | Static or dynamic contrast ratio | 1000:1, 3000:1, 5000:1, 1000000:1 |
| HDR Support | text | Highest HDR certification or standard supported | HDR10, HDR400, HDR600, HDR1000, HDR1400, Dolby Vision, None |
| Color Gamut sRGB | number (%) | Percentage of sRGB color space coverage | 95, 99, 100, 135 |
| Color Gamut DCI-P3 | number (%) | Percentage of DCI-P3 color space coverage | 85, 95, 98, 99 |
| Color Depth | text | Number of displayable colors or bit depth | 16.7 Million (8-bit), 1.07 Billion (10-bit) |
| Video Inputs | text (list) | Available video input ports and versions | DisplayPort 1.4, DisplayPort 2.1, HDMI 2.0, HDMI 2.1, USB-C (DP Alt), DVI-D, VGA |
| USB Hub | text | Built-in USB hub ports and type | 4x USB-A 3.2, 1x USB-C upstream, None |
| USB-C Power Delivery | number (W) | Maximum power delivery through USB-C connection | 0, 65, 90, 96, 100, 140 |
| Built-in Speakers | text | Integrated speaker configuration and power | 2x 2W, 2x 5W, None |
| Stand Adjustments | text (list) | Available ergonomic adjustments on the included stand | Tilt, Swivel, Height, Pivot |
| VESA Mount | text | VESA mounting pattern dimensions | 75x75mm, 100x100mm, 200x200mm, 400x400mm |
| Height | number (mm) | Overall product height with stand at lowest position | 361, 425, 540, 638 |
| Width | number (mm) | Overall product width | 540, 614, 727, 1210 |
| Depth | number (mm) | Overall product depth with stand | 155, 207, 240, 310 |
| Weight with Stand | number (kg) | Product weight including stand | 3.60, 5.80, 7.20, 9.10, 14.50 |
| Weight without Stand | number (kg) | Panel weight excluding stand | 2.90, 4.20, 5.60, 8.30 |
| Power Consumption | number (W) | Typical operating power draw | 22, 35, 50, 75, 120, 200 |
| Energy Certification | text (list) | Energy and environmental certifications | ENERGY STAR, TCO Certified, EPEAT, TUV Rheinland |
| Flicker-Free | boolean | Whether the display uses a flicker-free backlight | true, false |
| Warranty | text | Manufacturer warranty duration | 1 Year, 3 Years, 5 Years |
| Country of Origin | text | Country where the display was manufactured | China, South Korea, Taiwan, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus VESA DisplayHDR and industry standards | [Newegg LCD/LED Monitors](https://www.newegg.com/LCD-LED-Monitors/SubCategory/ID-20), [Newegg Gaming Monitors](https://www.newegg.com/Gaming-Monitor/SubCategory/ID-3743), [LG Monitors](https://www.lg.com/us/monitors), [Panelook Display Database](https://www.panelook.com/) |
