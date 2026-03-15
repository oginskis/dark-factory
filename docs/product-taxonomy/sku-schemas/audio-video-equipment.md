# SKU Schema: Audio & Video Equipment

**Last updated:** 2026-03-15
**Parent category:** Electronics & Electrical Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | RX-A6A, VPL-FHZ85W, HTR6230, SLS-1A |
| Product Name | text | Full product name including brand, model, and primary capability | Yamaha RX-A6A 9.2-Channel AV Receiver, Sony VPL-FHZ85 WUXGA Laser Projector, JBL EON715 15-inch Powered Speaker |
| URL | text | Direct link to the product page | https://example.com/product/yamaha-rx-a6a |
| Price | number | Numeric unit price excluding currency symbol | 249.99, 1499.00, 7599.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CAD |
| Brand | text | Equipment manufacturer | Yamaha, Sony, Denon, JBL, Bose, Sonos, Marantz, Harman Kardon, QSC, Shure |
| Product Type | enum | Primary equipment category | AV Receiver, Soundbar, Powered Speaker, Passive Speaker, Subwoofer, Projector, Streaming Player, Amplifier, Turntable, Mixer |
| Model Number | text | Manufacturer model identifier | RX-A6A, VPL-FHZ85, EON715, SL-1500C |
| Channels | text | Audio channel configuration | 2.0, 2.1, 5.1, 5.2, 7.1, 7.2.4, 9.2.4 |
| Power Output per Channel | number (W) | Continuous power output per channel in watts RMS | 20, 50, 100, 150, 250 |
| Total Power Output | number (W) | Combined maximum power output across all channels | 40, 200, 500, 1000, 1500 |
| Frequency Response | text | Audible frequency range the device can reproduce | 20Hz-20kHz, 10Hz-100kHz, 45Hz-20kHz |
| Impedance | number (ohms) | Nominal speaker impedance rating | 4, 6, 8, 16 |
| Sensitivity | number (dB) | Speaker sensitivity measured at 1 watt from 1 metre | 84, 89, 95, 100, 112 |
| Driver Size | text | Diameter of primary speaker cone or transducer | 3.5 inches, 6.5 inches, 8 inches, 10 inches, 15 inches |
| HDMI Inputs | number | Number of HDMI input ports | 0, 2, 4, 6, 7, 8 |
| HDMI Outputs | number | Number of HDMI output ports | 0, 1, 2, 3 |
| HDMI Version | text | Highest HDMI specification supported | HDMI 2.0, HDMI 2.1, HDMI 2.1a |
| Video Resolution Support | text | Maximum video pass-through or output resolution | 1080p, 4K, 8K |
| HDR Formats | text (list) | Supported high dynamic range video formats | HDR10, HDR10+, Dolby Vision, HLG |
| Audio Decode Formats | text (list) | Supported surround and immersive audio formats | Dolby Atmos, DTS:X, Dolby Digital, DTS-HD Master Audio, Auro-3D |
| Projector Brightness | number (lumens) | Light output for projectors measured in ANSI lumens | 2000, 3000, 5000, 7300, 10000 |
| Projection Technology | text | Imaging engine used in projectors | 3LCD, DLP, LCoS, SXRD, Laser Phosphor |
| Native Resolution | text | Native pixel resolution for projectors and display devices | 1920x1080, 1920x1200, 3840x2160 |
| Throw Ratio | text | Projector throw ratio range | 0.8:1, 1.2:1-1.8:1, 1.39:1-2.23:1 |
| Wireless Connectivity | text (list) | Wireless streaming and communication protocols | Wi-Fi, Bluetooth 5.0, AirPlay 2, Chromecast, Spotify Connect |
| Analog Audio Inputs | text | Types and number of analog audio input connections | 2x RCA, 1x 3.5mm, Phono (MM), XLR |
| Digital Audio Inputs | text | Types and number of digital audio input connections | 2x Optical, 1x Coaxial, AES/EBU |
| Multi-Zone | boolean | Whether the device supports audio output to multiple zones simultaneously | true, false |
| Noise Level | number (dB) | Acoustic noise produced during operation (for projectors and active speakers) | 28, 36, 38, 42 |
| Lamp or Light Source Life | number (hours) | Expected operating life of the projector light source | 5000, 10000, 20000, 30000 |
| Height | number (mm) | Device height | 96, 170, 270, 450 |
| Width | number (mm) | Device width | 210, 435, 460 |
| Depth | number (mm) | Device depth | 200, 380, 490 |
| Weight | number (kg) | Device weight | 0.66, 3.20, 10.50, 13.00, 17.10 |
| Power Consumption | number (W) | Maximum power draw during operation | 25, 130, 350, 506, 715 |
| Color | text | Exterior finish color | Black, Silver, White, Gold |
| Warranty | text | Manufacturer warranty duration | 1 Year, 2 Years, 3 Years, 5 Years |
| Certifications | text (list) | Regulatory and environmental certifications | CE, FCC, UL, RoHS, ENERGY STAR |
| Country of Origin | text | Country where the device was manufactured | Japan, China, Malaysia, Indonesia, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 sources plus CTA/HDMI industry standards | [Newegg AV Receivers](https://www.newegg.com/Receivers/SubCategory/ID-488), [Sony Professional Projectors](https://pro.sony/ue_US/products/projectors), [Crutchfield Home Theater Receivers](https://www.crutchfield.com/g_10420/Home-Theater-Receivers.html), [ProjectorCentral Sony VPL-FHZ85](https://www.projectorcentral.com/Sony-VPL-FHZ85.htm) |
