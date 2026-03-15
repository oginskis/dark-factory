# SKU Schema: Patient Monitoring Equipment

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer catalog or part number | 866471, 2060600-005, HC867030 |
| Product Name | text | Full product name including model and configuration | Philips IntelliVue MX750 Bedside Patient Monitor, GE Healthcare B40 V3 Patient Monitor |
| URL | text | Direct link to the product page | https://example.com/product/intellivue-mx750 |
| Price | number | List price or contract price per unit | 5500, 12000, 28000, 65000 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Brand/Manufacturer | text | Equipment manufacturer or brand | Philips, GE Healthcare, Nihon Kohden, Mindray, Draeger, Masimo, Spacelabs, BD (Edwards) |
| Model | text | Product model designation | IntelliVue MX750, B40 V3, BSM-1753, BeneVision N22, Infinity Delta |
| Monitor Type | enum | Primary clinical use category | Bedside, Transport, Telemetry, Central Station, Wearable/Remote, Fetal |
| Clinical Setting | text (list) | Intended care environment | ICU, OR/Anesthesia, Emergency Department, Step-Down/Med-Surg, Ambulance/Transport, Home/Remote |
| Display Size | number (in) | Diagonal screen measurement | 8.4, 10.4, 12.1, 15.6, 19, 22 |
| Display Resolution | text | Screen pixel resolution | 800 x 600, 1024 x 768, 1920 x 1080 |
| Display Type | text | Screen technology and touch capability | TFT LCD Touchscreen, pCAP Touchscreen, LED Backlit Non-Touch |
| Max Waveforms | number | Maximum number of simultaneous waveform traces | 4, 6, 8, 12, 16 |
| Standard Parameters | text (list) | Vital sign parameters included in the base configuration | ECG (3/5/12-lead), SpO2, NIBP, Temperature, Respiration |
| Optional Parameters | text (list) | Additional measurement modules available for purchase | IBP, EtCO2 (Capnography), Cardiac Output, BIS/Entropy, Agent Gas Analysis (O2/CO2/N2O), Neuromuscular Monitoring |
| ECG Lead Configuration | text | Supported ECG lead sets | 3-Lead, 5-Lead, 12-Lead |
| SpO2 Technology | text | Pulse oximetry sensor technology or brand | Masimo SET, Nellcor OxiMax, Philips TruSat, GE TruSignal |
| NIBP Method | text | Non-invasive blood pressure measurement technique | Oscillometric, DINAMAP SuperSTAT, SureBP |
| Arrhythmia Analysis | enum | Whether advanced arrhythmia detection software is included | Standard, Optional, Not Available |
| Alarm System | text | Alarm notification capabilities | Visual/Audible Bedside, Remote Alarm Notification, Nurse Call Relay, Smart Alarm Management |
| Modular Architecture | enum | Whether the monitor supports plug-in parameter modules | Modular, Semi-Modular, Fixed Configuration |
| Number of Module Slots | number | Available plug-in module bays | 0, 2, 4, 6, 8 |
| Connectivity | text (list) | Network and data interfaces | Wired Ethernet (RJ-45), Wi-Fi (802.11a/b/g/n/ac), HL7/FHIR, USB, Bluetooth, WMTS 1.4 GHz |
| EMR Integration | enum | Electronic medical record data export capability | Standard, Optional, Not Available |
| Data Storage | text | Internal trend and event data storage capacity | 72 hours trending, 96 hours full disclosure, Up to 1000 events |
| Battery Type | text | Internal battery chemistry and capacity | Lithium-Ion 10.8V 6.0Ah, Li-Ion 11.1V 4.8Ah |
| Battery Runtime | number (min) | Operating time on full battery charge | 60, 120, 180, 360 |
| Dimensions (W x H x D) | text (mm) | External dimensions excluding accessories | 312 x 312 x 158, 430 x 350 x 170, 485 x 380 x 190 |
| Weight | number (kg) | Net weight of the monitor without accessories | 3.2, 5.8, 8.5, 12.0 |
| Mounting Options | text (list) | Supported mounting configurations | Roll Stand, Wall Mount, Ceiling Boom, Rail Clamp, Tabletop |
| Power Supply | text | Input power requirements | 100-240 V AC, 50/60 Hz |
| Ingress Protection | text | IP rating for fluid and dust resistance | IP21, IPX1, IP32 |
| Operating Temperature | text | Ambient temperature operating range | 0 to 40 C, 5 to 40 C, 10 to 40 C |
| Regulatory Approval | text (list) | Medical device regulatory clearances | FDA 510(k), CE (MDR Class IIb), Health Canada, TGA |
| Safety Standards | text (list) | Applicable safety and EMC standards | IEC 60601-1, IEC 60601-1-2, IEC 80601-2-56 |
| Warranty | text | Standard manufacturer warranty period | 1 year, 2 years, 3 years |
| Country of Manufacture | text | Country where the device is produced | USA, Germany, Netherlands, Japan, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 sources plus IEC 60601 medical device standards | [Philips IntelliVue MX750](https://www.usa.philips.com/healthcare/product/HC866471/intellivue-mx750-bedside-patient-monitor), [GE Healthcare B40](https://sakomed.com/products/patient-monitors/ge-b40-patient-monitor/), [Nihon Kohden Patient Monitoring Catalog](https://us.nihonkohden.com/media/1569/patient-monitoring-product-catalog.pdf), [Infinium Medical](https://infiniummedical.com/) |
