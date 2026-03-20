# SKU Schema: Patient Monitoring Equipment

**Last updated:** 2026-03-15
**Parent category:** Pharmaceuticals & Medical Devices
**Taxonomy ID:** `pharma.patient_monitoring`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Manufacturer catalog or part number | 866471, 2060600-005, HC867030 |
| Product Name | product_name | text | — | yes | Full product name including model and configuration | Philips IntelliVue MX750 Bedside Patient Monitor, GE Healthcare B40 V3 Patient Monitor |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/intellivue-mx750 |
| Price | price | number | — | yes | List price or contract price per unit | 5500, 12000, 28000, 65000 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Monitor Type | monitor_type | enum | — | — | Primary clinical use category | Bedside, Transport, Telemetry, Central Station, Wearable/Remote, Fetal |
| Display Type | display_type | text | — | — | Screen technology and touch capability | TFT LCD Touchscreen, pCAP Touchscreen, LED Backlit Non-Touch |
| Max Waveforms | max_waveforms | number | — | — | Maximum number of simultaneous waveform traces | 4, 6, 8, 12, 16 |
| Battery Type | battery_type | text | — | — | Internal battery chemistry and capacity | Lithium-Ion 10.8V 6.0Ah, Li-Ion 11.1V 4.8Ah |
| Display Size | display_size | number | in | — | Diagonal screen measurement | 8.4, 10.4, 12.1, 15.6, 19, 22 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Model | model | text | — | — | Product model designation | IntelliVue MX750, B40 V3, BSM-1753, BeneVision N22, Infinity Delta |
| Clinical Setting | clinical_setting | text (list) | — | — | Intended care environment | ICU, OR/Anesthesia, Emergency Department, Step-Down/Med-Surg, Ambulance/Transport, Home/Remote |
| Display Resolution | display_resolution | text | — | — | Screen pixel resolution | 800 x 600, 1024 x 768, 1920 x 1080 |
| Standard Parameters | standard_parameters | text (list) | — | — | Vital sign parameters included in the base configuration | ECG (3/5/12-lead), SpO2, NIBP, Temperature, Respiration |
| Optional Parameters | optional_parameters | text (list) | — | — | Additional measurement modules available for purchase | IBP, EtCO2 (Capnography), Cardiac Output, BIS/Entropy, Agent Gas Analysis (O2/CO2/N2O), Neuromuscular Monitoring |
| ECG Lead Configuration | ecg_lead_configuration | text | — | — | Supported ECG lead sets | 3-Lead, 5-Lead, 12-Lead |
| SpO2 Technology | spo2_technology | text | — | — | Pulse oximetry sensor technology or brand | Masimo SET, Nellcor OxiMax, Philips TruSat, GE TruSignal |
| NIBP Method | nibp_method | text | — | — | Non-invasive blood pressure measurement technique | Oscillometric, DINAMAP SuperSTAT, SureBP |
| Arrhythmia Analysis | arrhythmia_analysis | enum | — | — | Whether advanced arrhythmia detection software is included | Standard, Optional, Not Available |
| Alarm System | alarm_system | text | — | — | Alarm notification capabilities | Visual/Audible Bedside, Remote Alarm Notification, Nurse Call Relay, Smart Alarm Management |
| Modular Architecture | modular_architecture | enum | — | — | Whether the monitor supports plug-in parameter modules | Modular, Semi-Modular, Fixed Configuration |
| Number of Module Slots | number_of_module_slots | number | — | — | Available plug-in module bays | 0, 2, 4, 6, 8 |
| Connectivity | connectivity | text (list) | — | — | Network and data interfaces | Wired Ethernet (RJ-45), Wi-Fi (802.11a/b/g/n/ac), HL7/FHIR, USB, Bluetooth, WMTS 1.4 GHz |
| EMR Integration | emr_integration | enum | — | — | Electronic medical record data export capability | Standard, Optional, Not Available |
| Data Storage | data_storage | text | — | — | Internal trend and event data storage capacity | 72 hours trending, 96 hours full disclosure, Up to 1000 events |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 sources plus IEC 60601 medical device standards | [Philips IntelliVue MX750](https://www.usa.philips.com/healthcare/product/HC866471/intellivue-mx750-bedside-patient-monitor), [GE Healthcare B40](https://sakomed.com/products/patient-monitors/ge-b40-patient-monitor/), [Nihon Kohden Patient Monitoring Catalog](https://us.nihonkohden.com/media/1569/patient-monitoring-product-catalog.pdf), [Infinium Medical](https://infiniummedical.com/) |
