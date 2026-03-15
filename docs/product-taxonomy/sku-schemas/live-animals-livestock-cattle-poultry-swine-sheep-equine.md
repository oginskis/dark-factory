# SKU Schema: Live Animals & Livestock (Cattle, Poultry, Swine, Sheep, Equine)

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Listing or lot identifier assigned by the seller or auction platform | LM-2026-04521, SA-BULL-0088, MH-BR-2026-WL |
| Product Name | text | Descriptive listing title including species, breed, sex, and key details | Registered Angus Bull 2 yr, 50 Head Commercial Black Baldy Bred Heifers, Day-Old Rhode Island Red Pullets |
| URL | text | Direct link to the listing or lot page | https://example.com/listing/angus-bull-0088 |
| Price | number | Numeric price per head, per lot, per pound, or per cwt, excluding currency symbol | 3500.00, 225.00, 1.85, 5.50 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, GBP, AUD, NZD |
| Pricing Unit | enum | Unit of measure for the quoted price | Per Head, Per CWT, Per Pound, Per Lot, Per Dozen (eggs) |
| Species | enum | Animal species | Cattle, Poultry, Swine, Sheep, Goat, Equine |
| Breed | text | Recognized breed or cross name | Angus, Hereford, Charolais, Simmental, Hampshire, Duroc, Rhode Island Red, Suffolk, Quarter Horse, Brahman |
| Crossbred or Purebred | enum | Whether the animal is purebred or crossbred | Purebred, Crossbred, F1 Cross, Composite |
| Sex | enum | Biological sex or castration status of the animal | Bull, Steer, Heifer, Cow, Boar, Barrow, Gilt, Sow, Ram, Ewe, Wether, Stallion, Gelding, Mare, Cockerel, Pullet, Straight Run |
| Animal Class | text | Production type or marketing classification | Breeding Stock, Feeder, Replacement, Cow-Calf Pair, Bred Female, Show Animal, Starter Flock, Layer, Broiler |
| Age | text | Age of the animal expressed in appropriate units | 18 months, 2 years, 3 days old, Day-Old, 6 weeks, Coming 2 yr old |
| Live Weight | number (kg) | Current live body weight or estimated weight | 340, 545, 115, 2.5, 27 |
| Average Weight | number (kg) | Average weight per head in a multi-head lot | 295, 340, 386, 115 |
| Frame Size | enum | Visual frame score indicating skeletal size, primarily for cattle | Small, Medium, Large, Extra Large |
| Body Condition Score | number | Standardized visual assessment of body fat reserves (1-9 for cattle, 1-5 for sheep and swine) | 5, 6, 7, 3.5 |
| Head Count | number | Number of animals in the lot or listing | 1, 10, 50, 100, 500 |
| Registration Status | enum | Whether the animal is registered with a recognized breed association | Registered, Eligible, Commercial, Grade |
| Registry Name | text | Name of the breed registry or association holding the animals registration | American Angus Association, American Quarter Horse Association, American Hampshire Sheep Association |
| Registration Number | text | Individual animal registration or tattoo number from the breed association | AAA 20145678, AQHA 5934210 |
| Pregnancy Status | text | Reproductive status for breeding females | Open, Bred, T1 (1-3 months), T2 (4-6 months), T3 (7-9 months), Confirmed Bred |
| Breeding Date or Due Date | text | Date of breeding or expected calving, lambing, farrowing, or foaling date | March 2026, Spring 2026, April 15 2026 |
| Sire | text | Name or registration identifier of the animals father | SAV Resource 1441, Connealy Comrade 1385 |
| Dam | text | Name or registration identifier of the animals mother | Blackcap Empress 7077, Rita 5E50 |
| EPD Birth Weight | number (kg) | Expected Progeny Difference for birth weight; lower values indicate lighter birth weights | -1.5, 0.5, 2.0, 3.5 |
| EPD Weaning Weight | number (kg) | Expected Progeny Difference for weaning weight; higher values indicate heavier weaning weights | 40, 55, 70, 85 |
| EPD Calving Ease Direct | number (%) | Expected Progeny Difference for unassisted birth percentage; higher values indicate easier calving | 8, 12, 15, 20 |
| EPD Milk | number (kg) | Expected Progeny Difference for maternal milk production reflected in calf weaning weight | 15, 22, 28, 35 |
| Health Program | text (list) | Vaccinations and health treatments administered | Modified Live Viral, Blackleg 7-Way, Dewormed, BVD-PI Tested Negative, Brucellosis Calfhood Vaccinated, Pullorum-Typhoid Clean |
| Health Certificate | boolean | Whether a Certificate of Veterinary Inspection accompanies the animal | true, false |
| Location | text | Geographic location of the animal (state/province and country) | Texas USA, Alberta Canada, Queensland Australia, Yorkshire UK |
| Delivery Method | enum | How the animals are made available to the buyer | On-Farm Pickup, Seller Delivers, Buyer Arranges Transport, Shipped via Carrier |
| Sale Type | enum | Transaction format for the listing | Private Treaty, Online Auction, Live Auction, Production Sale, Consignment |
| Listing Date | text | Date the listing was posted or the sale is scheduled | 2026-03-15, March 20 2026 |
| Photos Available | number | Number of photos included with the listing | 0, 1, 3, 5, 10 |
| Video Available | boolean | Whether a video of the animal or lot is included with the listing | true, false |
| NPIP Status | text | National Poultry Improvement Plan disease testing status for poultry | Pullorum-Typhoid Clean, AI Clean, NPIP Certified, Not Tested |
| Egg Production | number (eggs/year) | Expected annual egg production rate for laying poultry breeds | 200, 250, 280, 320 |
| Egg Color | text | Shell color of eggs produced by the poultry breed | Brown, White, Blue, Green, Dark Brown, Cream |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 40 attributes from 4 companies plus USDA AMS feeder cattle market report standards, American Angus Association EPD definitions, and NPIP poultry certification standards | [LivestockMarket.com](https://www.livestockmarket.com/), [CattleUSA](https://www.cattleusa.com/), [Meyer Hatchery](https://meyerhatchery.com/products/chickens), [Superior Livestock Auction](https://superiorlivestock.com/) |
