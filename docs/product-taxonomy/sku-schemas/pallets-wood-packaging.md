# SKU Schema: Pallets & Wood Packaging

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | UFP-STR-4840, PECO-GMA-48, PLT1-BLK-4840-HT |
| Product Name | text | Full product name including type, size, and treatment | 48x40 GMA Block Pallet Heat-Treated, Custom Stringer Pallet 48x48 Softwood |
| URL | text | Direct link to the product page | https://example.com/product/gma-block-pallet-48x40 |
| Price | number | Numeric price per pallet or per unit excluding currency symbol | 8.50, 15.00, 32.00, 65.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Pallet manufacturer or supplier | UFP Packaging, PalletOne, PECO Pallet, Kamps, CHEP |
| Product Type | enum | Primary product category | Stringer Pallet, Block Pallet, Wing Pallet, CP Pallet, System Pallet, Crate, Skid, Box |
| Pallet Dimensions | text (in) | Overall length x width as standard designation | 48x40, 48x48, 42x42, 44x44, 48x20 |
| Overall Length | number (in) | Pallet length | 40, 42, 44, 48 |
| Overall Width | number (in) | Pallet width | 20, 40, 42, 44, 48 |
| Overall Height | number (in) | Total pallet height including top and bottom decks | 4.75, 5.50, 5.56, 6.00 |
| Pallet Weight | number (lbs) | Total weight of the empty pallet | 28, 37, 45, 55, 75 |
| Static Load Capacity | number (lbs) | Maximum weight the pallet can support when stationary on a flat surface | 1400, 2800, 4600, 6000, 8000 |
| Dynamic Load Capacity | number (lbs) | Maximum weight supported when being moved by forklift or pallet jack | 2200, 2500, 2800, 3000 |
| Racking Load Capacity | number (lbs) | Maximum weight supported when placed on pallet racking with specified span | 1500, 2000, 2500, 2800 |
| Entry Type | enum | Forklift and pallet jack access configuration | 2-Way, 4-Way, Partial 4-Way |
| Deck Configuration | enum | Board arrangement on top and bottom faces | Single-Face, Double-Face Reversible, Double-Face Non-Reversible |
| Number of Top Deck Boards | number | Count of boards forming the top deck surface | 5, 7, 9, 11 |
| Number of Bottom Deck Boards | number | Count of boards forming the bottom deck surface | 3, 5, 6 |
| Wood Type | enum | Primary wood material classification | Hardwood, Softwood, Mixed, Composite |
| Wood Species | text | Specific wood species used | Southern Yellow Pine, Oak, Poplar, Spruce, Mixed Hardwood |
| Lumber Grade | text | Quality grade of the lumber used | Premium and BTR, No. 2, Pallet Grade, Recycled |
| Moisture Content | number (%) | Kiln-dried or air-dried moisture content of the wood | 19, 22, 25 |
| Heat Treatment | boolean | Whether the pallet has been heat-treated per ISPM-15 (core temperature 56C for 30 min) | true, false |
| ISPM-15 Certified | boolean | Whether the pallet carries an ISPM-15 stamp for international shipment | true, false |
| CP Designation | text | Chemical industry standard pallet type designation (CP1 through CP9) | CP1, CP3, CP5, CP7, CP9 |
| Condition | enum | Whether the pallet is new, recycled, or remanufactured | New, Recycled, Remanufactured, Grade A, Grade B |
| Fastener Type | text | Type of fasteners used in construction | Smooth Shank Nails, Annular Ring Nails, Screws, Staples |
| Number of Fasteners | number | Total fastener count in the pallet | 42, 78, 110, 138 |
| Minimum Order Quantity | number | Minimum number of pallets per order | 1, 50, 100, 500 |
| Country of Origin | text | Country where the pallet was manufactured | USA, Canada, Mexico, Poland |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISPM-15, GMA/CBA, NWPCA, ISO 6780) | [UFP Packaging](https://ufppackaging.com/products/pallets), [PECO Pallet](https://www.pecopallet.com/specifications/), [PalletOne](https://www.palletone.com/), [Kamps Pallets](https://www.kampspallets.com/standard-pallet-sizes-with-chart/) |
