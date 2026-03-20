# SKU Schema: Aquaculture & Fish Stock

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.aquaculture_fish_stock`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or supplier product identifier | BT-FG-100, NTF-50, KOI-KH-8 |
| Product Name | product_name | text | — | yes | Full product name including species, life stage, grade, and quantity | Food Grade Blue Tilapia Fingerlings 100-Pack, Imported Premium Kohaku Koi 8-10 inch |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/blue-tilapia-fingerlings |
| Price | price | number | — | yes | Numeric price per unit or per lot, excluding currency symbol | 0.89, 24.75, 199.99 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Grade | grade | text | — | — | Quality or purpose grading assigned by the supplier | Food Grade, Aquaponics Grade, Pond Grade, Show Quality, Premium, Standard |
| Water Type | water_type | enum | — | — | Type of water habitat the species requires | Freshwater, Saltwater, Brackish |
| Diet Type | diet_type | enum | — | — | Feeding classification of the species | Omnivore, Herbivore, Carnivore, Filter Feeder |
| Country of Origin | country_of_origin | text | — | — | Country or region where the stock was bred or harvested | USA, Israel, Thailand, Ecuador |
| Supplier Type | supplier_type | enum | — | — | Type of operation selling the stock | Hatchery, Farm, Distributor, Breeder |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Species Common Name | species_common_name | text | — | — | Common name of the fish or aquatic organism | Blue Tilapia, Rainbow Trout, Koi, Channel Catfish, White Shrimp, Largemouth Bass |
| Species Scientific Name | species_scientific_name | text | — | — | Binomial Latin name of the species | Oreochromis aureus, Oncorhynchus mykiss, Cyprinus rubrofuscus |
| Life Stage | life_stage | enum | — | — | Developmental stage of the organism at time of sale | Egg, Fry, Fingerling, Stocker, Juvenile, Broodstock, Adult |
| Sex | sex | enum | — | — | Sex composition of the lot | Male, Female, Mixed, All-Male, Unsexed |
| Quantity per Lot | quantity_per_lot | number | — | — | Number of organisms included per purchase unit | 1, 15, 25, 50, 100, 500, 1000 |
| Pricing Unit | pricing_unit | enum | — | — | How the product is priced | Per Fish, Per Lot, Per Pound, Per Thousand |
| Temperature Range Min | temperature_range_min | number | F | — | Minimum water temperature the species tolerates | 47, 55, 60, 68 |
| Temperature Range Max | temperature_range_max | number | F | — | Maximum water temperature the species tolerates | 86, 90, 100, 106 |
| Optimal Temperature Min | optimal_temperature_min | number | F | — | Lower bound of the ideal temperature range for growth | 72, 75, 78 |
| Optimal Temperature Max | optimal_temperature_max | number | F | — | Upper bound of the ideal temperature range for growth | 82, 85, 90 |
| Growth Rate | growth_rate | text | — | — | Expected time to reach harvest or target size under optimal conditions | 7 months to 1 lb, 12-18 months to market size |
| Purpose | purpose | text (list) | — | — | Intended use for the stock | Food Production, Aquaponics, Pond Stocking, Ornamental, Sport Fishing, Algae Control, Breeding |
| Variety | variety | text | — | — | Named cultivar, color morph, or strain within a species | Kohaku, Showa, Sanke, Hawaiian Gold, Red Nile, Butterfly, Shubunkin |
| Color | color | text | — | — | Primary body coloration | Red, White, Orange, Black, Blue, Gold, Calico, Platinum |
| Pattern | pattern | text | — | — | Distinctive color pattern when applicable | Metallic, Two-tone, Tri-color, Calico, Solid |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry data standards | [Live Aquaponics](https://liveaquaponics.com/collections/tilapia), [Lakeway Tilapia](https://lakewaytilapia.com/Live_Tilapia_For_Sale.php), [Kloubec Koi Farm](https://www.kloubeckoi.com/koi-for-sale/), [Arizona Aquatic Gardens](https://azgardens.com/product-category/pond/koi-other-pond-fish/) |
