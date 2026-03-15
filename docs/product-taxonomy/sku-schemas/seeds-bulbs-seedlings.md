# SKU Schema: Seeds, Bulbs & Seedlings

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.seeds_bulbs_seedlings`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | EB-TUL-RED-10, JS-TOM-BFT-100, AM-WF-POLLINATOR |
| Product Name | text | Full product name including species, variety, and pack details | Brandywine Heirloom Tomato Seeds 100ct, Darwin Hybrid Red Tulip Bulbs 10-Pack, Sweet Basil Organic Seedling 4-inch Pot |
| URL | text | Direct link to the product page | https://example.com/products/brandywine-tomato-seeds |
| Price | number | Numeric price per unit excluding currency symbol | 1.99, 3.49, 12.95, 24.99 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Type | enum | Primary form of the propagation material | Seed Packet, Seed Bulk, Bulb, Corm, Tuber, Rhizome, Bare Root, Seedling, Plug, Liner |
| Plant Category | enum | Broad horticultural classification | Vegetable, Herb, Flower, Fruit, Grass, Wildflower, Cover Crop, Tree, Shrub |
| Seed Type | enum | Breeding and certification classification of the seed | Heirloom, Hybrid (F1), Open-Pollinated, GMO |
| Country of Origin | text | Country where the seed or plant material was produced | USA, Netherlands, Chile, New Zealand, Canada |
| Seed Count | number | Number of seeds per packet or unit | 25, 50, 100, 500, 1000, 5000 |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Species | text | Botanical or common species name | Solanum lycopersicum, Tulipa, Ocimum basilicum, Lavandula angustifolia |
| Variety Name | text | Named cultivar or variety | Brandywine, Big Beef, Cherry Belle, Sugar Snap, Darwin Hybrid Red |
| Organic Certification | text | Organic standard the product is certified under | USDA Organic, EU Organic, None |
| Non-GMO Verified | boolean | Whether the product carries a Non-GMO Project or equivalent verification | true, false |
| Germination Rate | number (%) | Percentage of seeds expected to germinate under standard test conditions | 75, 85, 90, 95 |
| Days to Germination | text | Typical number of days from sowing to seedling emergence | 5-10, 7-14, 14-21, 21-30 |
| Days to Maturity | number (days) | Days from transplant or direct sowing to first harvest or bloom | 55, 68, 75, 90, 120 |
| Planting Depth | text (cm) | Recommended sowing or planting depth | 0.5, 1, 2.5, 5, 10, 15 |
| Plant Spacing | text (cm) | Recommended distance between plants in the row | 5, 10, 15, 30, 45, 60, 90 |
| Row Spacing | text (cm) | Recommended distance between rows | 30, 45, 60, 75, 90, 120 |
| Hardiness Zone Min | number | Minimum USDA hardiness zone for perennial survival | 2, 3, 4, 5, 6, 7 |
| Hardiness Zone Max | number | Maximum USDA hardiness zone for perennial survival | 7, 8, 9, 10, 11 |
| Sun Exposure | enum | Light requirement for optimal growth | Full Sun, Partial Shade, Full Shade, Sun to Partial Shade |
| Mature Height | text (cm) | Expected height of the plant at maturity | 15, 30, 60, 90, 120, 180, 300 |
| Bloom Season | text | Period of flowering for ornamental plants | Early Spring, Spring, Late Spring, Summer, Fall, Year-Round |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus AOSA seed testing standards and USDA hardiness zone system | [Eden Brothers](https://www.edenbrothers.com/), [American Meadows](https://www.americanmeadows.com/), [Jung Seed](https://www.jungseed.com/ecatalogs), [Fedco Seeds](https://fedcoseeds.com/supplies/amendments-and-fertilizers) |
