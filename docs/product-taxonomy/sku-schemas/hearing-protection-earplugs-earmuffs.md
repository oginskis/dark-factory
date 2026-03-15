# SKU Schema: Hearing Protection (Earplugs, Earmuffs)

**Last updated:** 2026-03-15
**Parent category:** Safety & Personal Protective Equipment
**Taxonomy ID:** `safety.hearing_protection`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | X5A, 1100, 340-4004, H10A |
| Product Name | text | Full product name including key specs such as type, NRR, and model | 3M PELTOR X5A Over-the-Head Earmuffs NRR 31 dB, Howard Leight MAX Disposable Foam Earplugs NRR 33 |
| URL | text | Direct link to the product page | https://example.com/product/peltor-x5a-earmuffs |
| Price | number | Numeric unit price excluding currency symbol | 0.15, 8.99, 54.95, 349.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | enum | Primary type of hearing protection device | Disposable Foam Earplug, Reusable Earplug, Banded Earplug (Canal Cap), Passive Earmuff, Electronic Earmuff, Communication Headset |
| Cup Material | text | Material of the earmuff outer shell | ABS, Polycarbonate, Stainless Steel |
| Cushion Material | text | Material of the ear seal pads | PVC Foam, Liquid/Gel Filled, Memory Foam, Silicone |
| Headband Material | text | Material of the earmuff headband | Stainless Steel Wire, Padded Plastic, Dielectric Wire, Spring Steel |
| Earplug Material | text | Material of the earplug body | PVC Foam, Polyurethane Foam, Silicone, Thermoplastic Elastomer, Flanged Polymer |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Battery Type | text | Power source for electronic models | AAA, AA, Rechargeable Li-Ion, CR2032 |
| Country of Origin | text | Country where the product is manufactured | USA, Sweden, Mexico, China |
| Model Number | text | Manufacturer model or part number | X5A, H10A, 1100, MAX-1, 6300 |
| NRR | number (dB) | Noise Reduction Rating per EPA/ANSI S3.19 or S12.6 test method | 22, 25, 27, 29, 31, 33 |
| SNR | number (dB) | Single Number Rating per EN 352 test standard (European equivalent of NRR) | 24, 28, 32, 35, 37 |
| Attenuation by Frequency | text | Mean attenuation values at key frequencies (typically 125 Hz through 8000 Hz) | H=34 M=27 L=19, See datasheet |
| Wearing Position | enum | How the device is worn on the head | In-Ear, Over-the-Head, Behind-the-Head, Neckband, Cap-Mounted, Helmet-Attached |
| Earplug Shape | text | Form factor of the earplug | Bullet, Bell, Tapered, Flanged (Triple Flange), Pod, Custom Molded |
| Corded | boolean | Whether the earplugs come with a connecting cord | true, false |
| Electronic Features | text (list) | Active electronic capabilities for electronic earmuffs | Level-Dependent Sound Amplification, Bluetooth, Audio Input Jack, AM/FM Radio, Two-Way Communication, Environmental Listening |
| Attack Time | number (ms) | Speed at which electronic earmuffs cut off dangerous impulse noise | 0.01, 0.3, 1.5 |
| External Microphone | boolean | Whether the earmuff has an external microphone for ambient sound pickup | true, false |
| Audio Input | text | Connectivity options for external audio devices | 3.5mm AUX, Bluetooth 5.0, Both, None |
| Battery Life | text | Expected operating time on a single charge or set of batteries | 50 hours, 80 hours, 500 hours, 600 hours |
| Dielectric | boolean | Whether the earmuff is non-conductive for use near electrical hazards | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (ANSI S3.19, ANSI S12.6, EN 352) | [3M Hearing Protection](https://www.3m.com/3M/en_US/p/c/ppe/hearing-protection/), [Honeywell Howard Leight](https://www.honeywellstore.com/store/category/hearing-protection-earmuffs-and-earbuds.htm), [Moldex](https://www.moldex.com/product-category/hearing-protection/), [3M PELTOR](https://multimedia.3m.com/mws/media/845196O/3m-peltor-x-series-earmuffs-technical-specifications.pdf) |
