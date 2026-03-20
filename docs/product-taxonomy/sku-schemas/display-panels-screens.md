# SKU Schema: Display Panels & Screens

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.display_panels_screens`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | 27GP850-B, LS32BG852NNXGO, PA278QV, C4422QN |
| Product Name | product_name | text | — | yes | Full product name including brand, size, resolution, and key feature | LG 27GP850-B 27-inch QHD Nano IPS Gaming Monitor, Samsung Odyssey Neo G8 32-inch 4K Curved Monitor |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/lg-27gp850-b |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 179.99, 599.00, 1299.95, 4999.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY, KRW |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Primary display category | Computer Monitor, Gaming Monitor, Professional Monitor, Digital Signage Display, Video Wall Panel, Touch Display, Portable Monitor |
| Model Number | model_number | text | — | — | Manufacturer model or part number | 27GP850-B, U2723QE, PA278QV, C4422QN |
| Panel Type | panel_type | enum | — | — | Display panel technology | IPS, VA, TN, OLED, QD-OLED, Mini LED, Nano IPS, Fast IPS |
| Country of Origin | country_of_origin | text | — | — | Country where the display was manufactured | China, South Korea, Taiwan, Mexico |
| Screen Size | screen_size | number | inches | — | Viewable screen diagonal measurement | 15.6, 24, 27, 32, 34, 43, 49, 55, 65, 86 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Native Resolution | native_resolution | text | — | — | Pixel resolution at native setting | 1920x1080, 2560x1440, 3440x1440, 3840x2160, 5120x2880 |
| Resolution Label | resolution_label | enum | — | — | Common marketing name for the resolution | Full HD, QHD, WQHD, UHD 4K, 5K, 8K |
| Refresh Rate | refresh_rate | number | Hz | — | Maximum panel refresh rate | 60, 75, 100, 144, 165, 240, 360, 480 |
| Response Time | response_time | number | ms | — | Pixel response time (grey-to-grey or MPRT) | 0.03, 0.5, 1, 4, 5, 8 |
| Adaptive Sync | adaptive_sync | text | — | — | Variable refresh rate technology supported | NVIDIA G-Sync, G-Sync Compatible, AMD FreeSync, FreeSync Premium, FreeSync Premium Pro, None |
| Aspect Ratio | aspect_ratio | text | — | — | Display width to height ratio | 16:9, 16:10, 21:9, 32:9, 32:10 |
| Curvature | curvature | text | — | — | Screen curvature radius (Flat if not curved) | Flat, 1000R, 1500R, 1800R, 3800R |
| Brightness | brightness | number | nits | — | Typical sustained brightness | 250, 350, 400, 600, 1000, 2000 |
| Peak Brightness | peak_brightness | number | nits | — | Maximum HDR peak brightness | 400, 600, 1000, 1400, 2000 |
| Contrast Ratio | contrast_ratio | text | — | — | Static or dynamic contrast ratio | 1000:1, 3000:1, 5000:1, 1000000:1 |
| HDR Support | hdr_support | text | — | — | Highest HDR certification or standard supported | HDR10, HDR400, HDR600, HDR1000, HDR1400, Dolby Vision, None |
| Color Gamut sRGB | color_gamut_srgb | number | % | — | Percentage of sRGB color space coverage | 95, 99, 100, 135 |
| Color Gamut DCI-P3 | color_gamut_dci-p3 | number | % | — | Percentage of DCI-P3 color space coverage | 85, 95, 98, 99 |
| Color Depth | color_depth | text | — | — | Number of displayable colors or bit depth | 16.7 Million (8-bit), 1.07 Billion (10-bit) |
| Video Inputs | video_inputs | text (list) | — | — | Available video input ports and versions | DisplayPort 1.4, DisplayPort 2.1, HDMI 2.0, HDMI 2.1, USB-C (DP Alt), DVI-D, VGA |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus VESA DisplayHDR and industry standards | [Newegg LCD/LED Monitors](https://www.newegg.com/LCD-LED-Monitors/SubCategory/ID-20), [Newegg Gaming Monitors](https://www.newegg.com/Gaming-Monitor/SubCategory/ID-3743), [LG Monitors](https://www.lg.com/us/monitors), [Panelook Display Database](https://www.panelook.com/) |
