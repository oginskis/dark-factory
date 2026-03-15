# SKU Schema: Handbags, Luggage & Travel Goods

**Last updated:** 2026-03-15
**Parent category:** Apparel, Footwear & Accessories
**Taxonomy ID:** `apparel.handbags_luggage_travel`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | B013WFNNZI, MON-CO-BLK, TS-2201 |
| Product Name | text | Full product name including brand, style, and key features | Samsonite Omni PC 20 in Hardside Spinner Carry-On, Coach Tabby Shoulder Bag 26, Tumi Alpha 3 Expandable Organizer Laptop Brief |
| URL | text | Direct link to the product page | https://example.com/product/carry-on-12345 |
| Price | number | Numeric unit price excluding currency symbol | 119.99, 275.00, 495.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Product Type | enum | Primary classification of the item | Handbag, Tote, Crossbody, Backpack, Carry-On Suitcase, Checked Suitcase, Duffel, Garment Bag, Briefcase, Wallet, Travel Organizer |
| Exterior Material | text | Primary material used for the outer shell | Full-grain leather, Polycarbonate, Ballistic nylon, Canvas, Vegan leather, ABS, Aluminum |
| Lining Material | text | Material used for the interior lining | Polyester, Nylon, Cotton, Recycled polyester, Jacquard |
| Closure Type | enum | Primary method of securing the main compartment | Zipper, Magnetic Snap, Turn Lock, Drawstring, Flap, Buckle, Frame |
| Handle Type | text | Type of carry handle provided | Top handle, Telescopic handle, Rolled handle, Chain strap, No handle |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Strap Type | text | Type of shoulder or body strap included | Detachable shoulder strap, Adjustable crossbody strap, Fixed strap, Chain strap, None |
| Wheel Type | enum | Type of wheels for rolling luggage; not applicable for handbags | Spinner (4-wheel), Inline (2-wheel), None |
| Lock Type | enum | Built-in security lock type | TSA-approved combination, Key lock, None |
| Shell Type | enum | Rigidity classification for luggage | Hardside, Softside, Hybrid |
| Country of Origin | text | Country where the product was manufactured | China, Italy, France, India, Cambodia |
| Model Number | text | Manufacturer model or style number | 68309-1041, CO-4146,?"3 2203141 |
| Color | text | Exterior color or pattern name | Black, Desert Taupe, Olive Green, Monogram Canvas, Cognac |
| Height | number (cm) | Exterior height of the product | 23, 40, 76 |
| Depth | number (cm) | Exterior depth or gusset measurement | 12, 23, 34 |
| Volume | number (L) | Internal packing capacity in litres | 22, 37, 95 |
| Strap Drop | number (cm) | Distance from top of strap to top of bag when worn | 15, 30, 55 |
| Number of Compartments | number | Count of distinct main compartments | 1, 2, 3 |
| Interior Pockets | number | Total number of interior pockets including zippered and open | 2, 4, 6 |
| Exterior Pockets | number | Total number of exterior pockets | 0, 1, 3 |
| Laptop Compartment | boolean | Whether the product includes a padded laptop sleeve | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema -- 31 attributes from 4 sources plus industry sizing standards | [Samsonite](https://shop.samsonite.com/luggage/), [Monos](https://monos.com/products/carry-on), [72 Smalldive Bag Measurements Guide](https://www.72smalldive.com/pages/bag-measurements-sizing-fitting), [Travel Sentry Luggage Features](https://www.travelsentry.org/tsa-lock/how-to-choose-luggage-key-features-to-look-for/) |
