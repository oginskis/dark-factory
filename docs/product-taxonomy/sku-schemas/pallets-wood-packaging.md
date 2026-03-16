# SKU Schema: Pallets & Wood Packaging

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber
**Taxonomy ID:** `wood.pallets_packaging`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | UFP-STR-4840, PECO-GMA-48, PLT1-BLK-4840-HT |
| Product Name | product_name | text | — | Full product name including type, size, and treatment | 48x40 GMA Block Pallet Heat-Treated, Custom Stringer Pallet 48x48 Softwood |
| URL | url | text | — | Direct link to the product page | https://example.com/product/gma-block-pallet-48x40 |
| Price | price | number | — | Numeric price per pallet or per unit excluding currency symbol | 8.50, 15.00, 32.00, 65.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | — | Primary product category | Stringer Pallet, Block Pallet, Wing Pallet, CP Pallet, System Pallet, Crate, Skid, Box |
| Entry Type | entry_type | enum | — | Forklift and pallet jack access configuration | 2-Way, 4-Way, Partial 4-Way |
| Wood Type | wood_type | enum | — | Primary wood material classification | Hardwood, Softwood, Mixed, Composite |
| Lumber Grade | lumber_grade | text | — | Quality grade of the lumber used | Premium and BTR, No. 2, Pallet Grade, Recycled |
| Fastener Type | fastener_type | text | — | Type of fasteners used in construction | Smooth Shank Nails, Annular Ring Nails, Screws, Staples |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Country of Origin | country_of_origin | text | — | Country where the pallet was manufactured | USA, Canada, Mexico, Poland |
| Pallet Dimensions | pallet_dimensions | text | in | Overall length x width as standard designation | 48x40, 48x48, 42x42, 44x44, 48x20 |
| Overall Width | overall_width | number | in | Pallet width | 20, 40, 42, 44, 48 |
| Overall Height | overall_height | number | in | Total pallet height including top and bottom decks | 4.75, 5.50, 5.56, 6.00 |
| Deck Configuration | deck_configuration | enum | — | Board arrangement on top and bottom faces | Single-Face, Double-Face Reversible, Double-Face Non-Reversible |
| Number of Top Deck Boards | number_of_top_deck_boards | number | — | Count of boards forming the top deck surface | 5, 7, 9, 11 |
| Number of Bottom Deck Boards | number_of_bottom_deck_boards | number | — | Count of boards forming the bottom deck surface | 3, 5, 6 |
| Wood Species | wood_species | text | — | Specific wood species used | Southern Yellow Pine, Oak, Poplar, Spruce, Mixed Hardwood |
| Moisture Content | moisture_content | number | % | Kiln-dried or air-dried moisture content of the wood | 19, 22, 25 |
| Heat Treatment | heat_treatment | boolean | — | Whether the pallet has been heat-treated per ISPM-15 (core temperature 56C for 30 min) | true, false |
| ISPM-15 Certified | ispm-15_certified | boolean | — | Whether the pallet carries an ISPM-15 stamp for international shipment | true, false |
| CP Designation | cp_designation | text | — | Chemical industry standard pallet type designation (CP1 through CP9) | CP1, CP3, CP5, CP7, CP9 |
| Condition | condition | enum | — | Whether the pallet is new, recycled, or remanufactured | New, Recycled, Remanufactured, Grade A, Grade B |
| Number of Fasteners | number_of_fasteners | number | — | Total fastener count in the pallet | 42, 78, 110, 138 |
| Minimum Order Quantity | minimum_order_quantity | number | — | Minimum number of pallets per order | 1, 50, 100, 500 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISPM-15, GMA/CBA, NWPCA, ISO 6780) | [UFP Packaging](https://ufppackaging.com/products/pallets), [PECO Pallet](https://www.pecopallet.com/specifications/), [PalletOne](https://www.palletone.com/), [Kamps Pallets](https://www.kampspallets.com/standard-pallet-sizes-with-chart/) |
