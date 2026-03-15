# SKU Schema: Hearing Protection (Earplugs, Earmuffs)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.hearing_protection`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | X5A, 1100, 340-4004, H10A |
| Product Name | product_name | text | Full product name including key specs such as type, NRR, and model | 3M PELTOR X5A Over-the-Head Earmuffs NRR 31 dB, Howard Leight MAX Disposable Foam Earplugs NRR 33 |
| URL | url | text | Direct link to the product page | https://example.com/product/peltor-x5a-earmuffs |
| Price | price | number | Numeric unit price excluding currency symbol | 0.15, 8.99, 54.95, 349.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | Primary type of hearing protection device | Disposable Foam Earplug, Reusable Earplug, Banded Earplug (Canal Cap), Passive Earmuff, Electronic Earmuff, Communication Headset |
| Cup Material | cup_material | text | Material of the earmuff outer shell | ABS, Polycarbonate, Stainless Steel |
| Cushion Material | cushion_material | text | Material of the ear seal pads | PVC Foam, Liquid/Gel Filled, Memory Foam, Silicone |
| Headband Material | headband_material | text | Material of the earmuff headband | Stainless Steel Wire, Padded Plastic, Dielectric Wire, Spring Steel |
| Earplug Material | earplug_material | text | Material of the earplug body | PVC Foam, Polyurethane Foam, Silicone, Thermoplastic Elastomer, Flanged Polymer |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Battery Type | battery_type | text | Power source for electronic models | AAA, AA, Rechargeable Li-Ion, CR2032 |
| Country of Origin | country_of_origin | text | Country where the product is manufactured | USA, Sweden, Mexico, China |
| Model Number | model_number | text | Manufacturer model or part number | X5A, H10A, 1100, MAX-1, 6300 |
| NRR | nrr | number (dB) | Noise Reduction Rating per EPA/ANSI S3.19 or S12.6 test method | 22, 25, 27, 29, 31, 33 |
| SNR | snr | number (dB) | Single Number Rating per EN 352 test standard (European equivalent of NRR) | 24, 28, 32, 35, 37 |
| Attenuation by Frequency | attenuation_by_frequency | text | Mean attenuation values at key frequencies (typically 125 Hz through 8000 Hz) | H=34 M=27 L=19, See datasheet |
| Wearing Position | wearing_position | enum | How the device is worn on the head | In-Ear, Over-the-Head, Behind-the-Head, Neckband, Cap-Mounted, Helmet-Attached |
| Earplug Shape | earplug_shape | text | Form factor of the earplug | Bullet, Bell, Tapered, Flanged (Triple Flange), Pod, Custom Molded |
| Corded | corded | boolean | Whether the earplugs come with a connecting cord | true, false |
| Electronic Features | electronic_features | text (list) | Active electronic capabilities for electronic earmuffs | Level-Dependent Sound Amplification, Bluetooth, Audio Input Jack, AM/FM Radio, Two-Way Communication, Environmental Listening |
| Attack Time | attack_time | number (ms) | Speed at which electronic earmuffs cut off dangerous impulse noise | 0.01, 0.3, 1.5 |
| External Microphone | external_microphone | boolean | Whether the earmuff has an external microphone for ambient sound pickup | true, false |
| Audio Input | audio_input | text | Connectivity options for external audio devices | 3.5mm AUX, Bluetooth 5.0, Both, None |
| Battery Life | battery_life | text | Expected operating time on a single charge or set of batteries | 50 hours, 80 hours, 500 hours, 600 hours |
| Dielectric | dielectric | boolean | Whether the earmuff is non-conductive for use near electrical hazards | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI S3.19, ANSI S12.6, EN 352) | [3M Hearing Protection](https://www.3m.com/3M/en_US/p/c/ppe/hearing-protection/), [Honeywell Howard Leight](https://www.honeywellstore.com/store/category/hearing-protection-earmuffs-and-earbuds.htm), [Moldex](https://www.moldex.com/product-category/hearing-protection/), [3M PELTOR](https://multimedia.3m.com/mws/media/845196O/3m-peltor-x-series-earmuffs-technical-specifications.pdf) |
