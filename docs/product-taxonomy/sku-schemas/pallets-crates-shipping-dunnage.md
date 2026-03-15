# SKU Schema: Pallets, Crates & Shipping Dunnage

**Last updated:** 2026-03-15
**Parent category:** Packaging Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | H-1260, 239866, CPP336ACM |
| Product Name | text | Full product name including key specs such as material, size, and type | Heat Treated Wood GMA Pallet 48 x 40, Double Deck Plastic Pallet 4-Way Entry 48 x 40, Hardwood Dunnage 4x4x48 |
| URL | text | Direct link to the product page | https://example.com/product/gma-pallet-48x40 |
| Price | number | Numeric price per unit excluding currency symbol | 67.95, 12.50, 245.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Company that manufactures or supplies the product | Cabka, CHEP, ORBIS, PalletOne, Nefab |
| Product Type | enum | High-level product category | Pallet, Crate, Dunnage, Skid |
| Material | text | Primary construction material | Wood, Plastic (HDPE), Corrugated, Plywood, Metal, Foam |
| Length | number (mm) | Outer length of the pallet, crate, or dunnage piece | 1219, 1200, 1016 |
| Width | number (mm) | Outer width of the pallet, crate, or dunnage piece | 1016, 1000, 800 |
| Height | number (mm) | Overall height including runners or blocks | 140, 150, 762 |
| Pallet Size Standard | text | Named size standard if applicable | GMA 48x40, EUR 1200x800, ISO 1067x1067, Half Pallet 800x600 |
| Entry Type | enum | Fork access direction | 2-Way, 4-Way, Partial 4-Way |
| Deck Type | enum | Configuration of the top and bottom decks | Single Deck, Double Deck, Reversible, Solid Top, Open Deck |
| Number of Stringers/Blocks | number | Count of structural stringers or block supports | 3, 4, 9 |
| Static Load Capacity | number (kg) | Maximum evenly distributed load at rest | 8000, 5000, 2500 |
| Dynamic Load Capacity | number (kg) | Maximum load while being moved by forklift or pallet jack | 1360, 1000, 2270 |
| Racking Load Capacity | number (kg) | Maximum load when supported only at the ends on racking beams | 900, 600, 1100 |
| Unit Weight | number (kg) | Weight of the empty pallet, crate, or dunnage unit | 18.0, 22.5, 6.8 |
| Deck Board Thickness | number (mm) | Thickness of the top deck boards | 16, 19, 22 |
| Number of Deck Boards | number | Count of boards on the top deck | 5, 7, 11 |
| Nestable/Stackable | enum | Whether empty units can nest into each other or stack | Nestable, Stackable, Rackable, Non-Nestable |
| ISPM-15 Compliant | enum | Whether the wood meets International Standards for Phytosanitary Measures No. 15 for export | Yes - HT, Yes - MB, Not Applicable, No |
| Treatment Type | text | Phytosanitary or preservative treatment applied | Heat Treated (HT), Methyl Bromide (MB), Kiln Dried, Fumigated, None |
| Reusable | boolean | Whether the product is designed for multiple-trip use | true, false |
| Color | text | Primary color of the product | Natural Wood, Black, Blue, Red, Grey |
| Industry/Application | text (list) | Primary industries or use cases served | Grocery, Automotive, Chemical, Pharmaceutical, Export, Warehousing |
| Certification | text (list) | Quality, safety, or sustainability certifications | ISPM-15, FDA Compliant, ISO 8611, PEFC, FSC, NSF |
| Country of Origin | text | Country where the product is manufactured | USA, Canada, Germany, China, Poland |
| Recyclable | boolean | Whether the product can be recycled at end of life | true, false |
| MOQ | number | Minimum order quantity | 1, 10, 48, 200 |
| Interior Dimensions | text (mm) | Usable internal dimensions of a crate (L x W x H) | 1100 x 900 x 600, 800 x 600 x 400 |
| Closure Type | text | How the crate is sealed or closed | Nailed, Screwed, Hinged Lid, Collapsible, Banded |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus industry standards (ISPM-15, ISO 8611, GMA pallet spec) | [Global Industrial](https://www.globalindustrial.com/p/double-deck-plastic-pallet-48x40-capacity-3000-lbs), [ORBIS Corporation](https://www.orbiscorporation.com/en-us/products/dunnage/), [PalletOne](https://www.palletone.com/what-is-dunnage-a-clear-guide-for-shipping-professionals/), [Kamps Pallets](https://www.kampspallets.com/standard-pallet-sizes-with-chart/) |
