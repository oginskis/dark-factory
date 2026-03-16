# SKU Schema: Live Animals & Livestock (Cattle, Poultry, Swine, Sheep, Equine)

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.live_animals_livestock`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Listing or lot identifier assigned by the seller or auction platform | LM-2026-04521, SA-BULL-0088, MH-BR-2026-WL |
| Product Name | product_name | text | — | Descriptive listing title including species, breed, sex, and key details | Registered Angus Bull 2 yr, 50 Head Commercial Black Baldy Bred Heifers, Day-Old Rhode Island Red Pullets |
| URL | url | text | — | Direct link to the listing or lot page | https://example.com/listing/angus-bull-0088 |
| Price | price | number | — | Numeric price per head, per lot, per pound, or per cwt, excluding currency symbol | 3500.00, 225.00, 1.85, 5.50 |
| Currency | currency | text | — | ISO 4217 currency code | USD, CAD, EUR, GBP, AUD, NZD |
| Animal Class | animal_class | text | — | Production type or marketing classification | Breeding Stock, Feeder, Replacement, Cow-Calf Pair, Bred Female, Show Animal, Starter Flock, Layer, Broiler |
| Sale Type | sale_type | enum | — | Transaction format for the listing | Private Treaty, Online Auction, Live Auction, Production Sale, Consignment |
| Live Weight | live_weight | number | kg | Current live body weight or estimated weight | 340, 545, 115, 2.5, 27 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Pricing Unit | pricing_unit | enum | — | Unit of measure for the quoted price | Per Head, Per CWT, Per Pound, Per Lot, Per Dozen (eggs) |
| Species | species | enum | — | Animal species | Cattle, Poultry, Swine, Sheep, Goat, Equine |
| Breed | breed | text | — | Recognized breed or cross name | Angus, Hereford, Charolais, Simmental, Hampshire, Duroc, Rhode Island Red, Suffolk, Quarter Horse, Brahman |
| Crossbred or Purebred | crossbred_or_purebred | enum | — | Whether the animal is purebred or crossbred | Purebred, Crossbred, F1 Cross, Composite |
| Sex | sex | enum | — | Biological sex or castration status of the animal | Bull, Steer, Heifer, Cow, Boar, Barrow, Gilt, Sow, Ram, Ewe, Wether, Stallion, Gelding, Mare, Cockerel, Pullet, Straight Run |
| Age | age | text | — | Age of the animal expressed in appropriate units | 18 months, 2 years, 3 days old, Day-Old, 6 weeks, Coming 2 yr old |
| Body Condition Score | body_condition_score | number | — | Standardized visual assessment of body fat reserves (1-9 for cattle, 1-5 for sheep and swine) | 5, 6, 7, 3.5 |
| Registration Status | registration_status | enum | — | Whether the animal is registered with a recognized breed association | Registered, Eligible, Commercial, Grade |
| Registry Name | registry_name | text | — | Name of the breed registry or association holding the animals registration | American Angus Association, American Quarter Horse Association, American Hampshire Sheep Association |
| Registration Number | registration_number | text | — | Individual animal registration or tattoo number from the breed association | AAA 20145678, AQHA 5934210 |
| Pregnancy Status | pregnancy_status | text | — | Reproductive status for breeding females | Open, Bred, T1 (1-3 months), T2 (4-6 months), T3 (7-9 months), Confirmed Bred |
| Breeding Date or Due Date | breeding_date_or_due_date | text | — | Date of breeding or expected calving, lambing, farrowing, or foaling date | March 2026, Spring 2026, April 15 2026 |
| Sire | sire | text | — | Name or registration identifier of the animals father | SAV Resource 1441, Connealy Comrade 1385 |
| Dam | dam | text | — | Name or registration identifier of the animals mother | Blackcap Empress 7077, Rita 5E50 |
| EPD Calving Ease Direct | epd_calving_ease_direct | number | % | Expected Progeny Difference for unassisted birth percentage; higher values indicate easier calving | 8, 12, 15, 20 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus USDA AMS feeder cattle market report standards, American Angus Association EPD definitions, and NPIP poultry certification standards | [LivestockMarket.com](https://www.livestockmarket.com/), [CattleUSA](https://www.cattleusa.com/), [Meyer Hatchery](https://meyerhatchery.com/products/chickens), [Superior Livestock Auction](https://superiorlivestock.com/) |
