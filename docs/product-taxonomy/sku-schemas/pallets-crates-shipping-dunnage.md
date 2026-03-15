# SKU Schema: Pallets, Crates & Shipping Dunnage

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials
**Taxonomy ID:** `packaging.pallets_crates_dunnage`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | H-1260, 239866, CPP336ACM |
| Product Name | product_name | text | Full product name including key specs such as material, size, and type | Heat Treated Wood GMA Pallet 48 x 40, Double Deck Plastic Pallet 4-Way Entry 48 x 40, Hardwood Dunnage 4x4x48 |
| URL | url | text | Direct link to the product page | https://example.com/product/gma-pallet-48x40 |
| Price | price | number | Numeric price per unit excluding currency symbol | 67.95, 12.50, 245.00 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Product Type | product_type | enum | High-level product category | Pallet, Crate, Dunnage, Skid |
| Material | material | text | Primary construction material | Wood, Plastic (HDPE), Corrugated, Plywood, Metal, Foam |
| Entry Type | entry_type | enum | Fork access direction | 2-Way, 4-Way, Partial 4-Way |
| Deck Type | deck_type | enum | Configuration of the top and bottom decks | Single Deck, Double Deck, Reversible, Solid Top, Open Deck |
| Treatment Type | treatment_type | text | Phytosanitary or preservative treatment applied | Heat Treated (HT), Methyl Bromide (MB), Kiln Dried, Fumigated, None |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Country of Origin | country_of_origin | text | Country where the product is manufactured | USA, Canada, Germany, China, Poland |
| Closure Type | closure_type | text | How the crate is sealed or closed | Nailed, Screwed, Hinged Lid, Collapsible, Banded |
| Width | width | number (mm) | Outer width of the pallet, crate, or dunnage piece | 1016, 1000, 800 |
| Height | height | number (mm) | Overall height including runners or blocks | 140, 150, 762 |
| Number of Stringers/Blocks | number_of_stringersblocks | number | Count of structural stringers or block supports | 3, 4, 9 |
| Deck Board Thickness | deck_board_thickness | number (mm) | Thickness of the top deck boards | 16, 19, 22 |
| Number of Deck Boards | number_of_deck_boards | number | Count of boards on the top deck | 5, 7, 11 |
| Nestable/Stackable | nestablestackable | enum | Whether empty units can nest into each other or stack | Nestable, Stackable, Rackable, Non-Nestable |
| ISPM-15 Compliant | ispm-15_compliant | enum | Whether the wood meets International Standards for Phytosanitary Measures No. 15 for export | Yes - HT, Yes - MB, Not Applicable, No |
| Reusable | reusable | boolean | Whether the product is designed for multiple-trip use | true, false |
| Color | color | text | Primary color of the product | Natural Wood, Black, Blue, Red, Grey |
| Industry/Application | industryapplication | text (list) | Primary industries or use cases served | Grocery, Automotive, Chemical, Pharmaceutical, Export, Warehousing |
| Certification | certification | text (list) | Quality, safety, or sustainability certifications | ISPM-15, FDA Compliant, ISO 8611, PEFC, FSC, NSF |
| Recyclable | recyclable | boolean | Whether the product can be recycled at end of life | true, false |
| MOQ | moq | number | Minimum order quantity | 1, 10, 48, 200 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISPM-15, ISO 8611, GMA pallet spec) | [Global Industrial](https://www.globalindustrial.com/p/double-deck-plastic-pallet-48x40-capacity-3000-lbs), [ORBIS Corporation](https://www.orbiscorporation.com/en-us/products/dunnage/), [PalletOne](https://www.palletone.com/what-is-dunnage-a-clear-guide-for-shipping-professionals/), [Kamps Pallets](https://www.kampspallets.com/standard-pallet-sizes-with-chart/) |
