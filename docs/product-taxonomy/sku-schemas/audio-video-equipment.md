# SKU Schema: Audio & Video Equipment

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment
**Taxonomy ID:** `electronics.audio_video`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | RX-A6A, VPL-FHZ85W, HTR6230, SLS-1A |
| Product Name | product_name | text | Full product name including brand, model, and primary capability | Yamaha RX-A6A 9.2-Channel AV Receiver, Sony VPL-FHZ85 WUXGA Laser Projector, JBL EON715 15-inch Powered Speaker |
| URL | url | text | Direct link to the product page | https://example.com/product/yamaha-rx-a6a |
| Price | price | number | Numeric unit price excluding currency symbol | 249.99, 1499.00, 7599.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Product Type | product_type | enum | Primary equipment category | AV Receiver, Soundbar, Powered Speaker, Passive Speaker, Subwoofer, Projector, Streaming Player, Amplifier, Turntable, Mixer |
| Model Number | model_number | text | Manufacturer model identifier | RX-A6A, VPL-FHZ85, EON715, SL-1500C |
| HDR Formats | hdr_formats | text (list) | Supported high dynamic range video formats | HDR10, HDR10+, Dolby Vision, HLG |
| Audio Decode Formats | audio_decode_formats | text (list) | Supported surround and immersive audio formats | Dolby Atmos, DTS:X, Dolby Digital, DTS-HD Master Audio, Auro-3D |
| Country of Origin | country_of_origin | text | Country where the device was manufactured | Japan, China, Malaysia, Indonesia, Mexico |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Channels | channels | text | Audio channel configuration | 2.0, 2.1, 5.1, 5.2, 7.1, 7.2.4, 9.2.4 |
| Power Output per Channel | power_output_per_channel | number (W) | Continuous power output per channel in watts RMS | 20, 50, 100, 150, 250 |
| Total Power Output | total_power_output | number (W) | Combined maximum power output across all channels | 40, 200, 500, 1000, 1500 |
| Frequency Response | frequency_response | text | Audible frequency range the device can reproduce | 20Hz-20kHz, 10Hz-100kHz, 45Hz-20kHz |
| Impedance | impedance | number (ohms) | Nominal speaker impedance rating | 4, 6, 8, 16 |
| Sensitivity | sensitivity | number (dB) | Speaker sensitivity measured at 1 watt from 1 metre | 84, 89, 95, 100, 112 |
| HDMI Inputs | hdmi_inputs | number | Number of HDMI input ports | 0, 2, 4, 6, 7, 8 |
| HDMI Outputs | hdmi_outputs | number | Number of HDMI output ports | 0, 1, 2, 3 |
| HDMI Version | hdmi_version | text | Highest HDMI specification supported | HDMI 2.0, HDMI 2.1, HDMI 2.1a |
| Video Resolution Support | video_resolution_support | text | Maximum video pass-through or output resolution | 1080p, 4K, 8K |
| Projector Brightness | projector_brightness | number (lumens) | Light output for projectors measured in ANSI lumens | 2000, 3000, 5000, 7300, 10000 |
| Projection Technology | projection_technology | text | Imaging engine used in projectors | 3LCD, DLP, LCoS, SXRD, Laser Phosphor |
| Native Resolution | native_resolution | text | Native pixel resolution for projectors and display devices | 1920x1080, 1920x1200, 3840x2160 |
| Throw Ratio | throw_ratio | text | Projector throw ratio range | 0.8:1, 1.2:1-1.8:1, 1.39:1-2.23:1 |
| Wireless Connectivity | wireless_connectivity | text (list) | Wireless streaming and communication protocols | Wi-Fi, Bluetooth 5.0, AirPlay 2, Chromecast, Spotify Connect |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus CTA/HDMI industry standards | [Newegg AV Receivers](https://www.newegg.com/Receivers/SubCategory/ID-488), [Sony Professional Projectors](https://pro.sony/ue_US/products/projectors), [Crutchfield Home Theater Receivers](https://www.crutchfield.com/g_10420/Home-Theater-Receivers.html), [ProjectorCentral Sony VPL-FHZ85](https://www.projectorcentral.com/Sony-VPL-FHZ85.htm) |
