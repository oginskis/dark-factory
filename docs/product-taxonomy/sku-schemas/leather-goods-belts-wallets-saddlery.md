# SKU Schema: Leather Goods (Belts, Wallets, Saddlery)

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HB-TAH-BLK-36, BFC-BIF-BIS, TS-SAD-WRN-16 |
| Product Name | text | Full product name including product type, leather type, and key features | Tahoe Full Grain Bifold Wallet Black, 1.5 inch Bridle Leather Belt with Brass Buckle, Western Roping Saddle 16 inch Seat |
| URL | text | Direct link to the product page | https://example.com/product/bridle-leather-belt |
| Price | number | Numeric price per unit, excluding currency symbol | 45.00, 120.00, 895.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD |
| Brand/Manufacturer | text | Brand or maker name | Hanks Belts, Buffalo Billfold Company, Texas Saddlery, Tanner Goods |
| Product Type | enum | Specific type of leather good | Bifold Wallet, Trifold Wallet, Card Holder, Money Clip, Coin Purse, Dress Belt, Casual Belt, Work Belt, Western Saddle, English Saddle, Bridle, Halter, Saddlebag, Holster |
| Leather Type | text | Type and grade of leather used in the primary construction | Full Grain Cowhide, Top Grain Steerhide, Bison, Vegetable Tanned Bridle, Cordovan, Exotic Alligator |
| Leather Thickness | number (mm) | Thickness of the leather used in construction | 1.2, 2.0, 3.0, 4.5 |
| Tanning Method | enum | Tanning process used on the leather | Vegetable Tanned, Chrome Tanned, Combination Tanned |
| Color | text | Primary product color | Black, Brown, Dark Brown, Tan, Burgundy, Natural, Vintage Brown, Cognac |
| Dimensions Length | number (mm) | Overall length of the product. For belts this is the strap length; for wallets the longest exterior dimension | 110, 220, 915, 1200 |
| Dimensions Width | number (mm) | Overall width. For belts this is the strap width; for wallets the shorter exterior dimension | 22, 32, 38, 95, 110 |
| Dimensions Depth | number (mm) | Thickness or depth when closed | 10, 15, 20 |
| Weight | number (g) | Product weight | 55, 104, 145, 4500 |
| Belt Width | number (mm) | Width of the belt strap, a key specification for belt products | 25, 32, 38, 44 |
| Belt Size Range | text | Available waist sizes for belts | 28-44, 30-48, 26-70 |
| Buckle Type | enum | Style and mechanism of belt buckle | Pin Buckle, Snap Buckle, Roller Buckle, Plate Buckle, Western Buckle, No Buckle (strap only) |
| Buckle Material | text | Material of the buckle or primary hardware | Solid Brass, Stainless Steel, Zinc Alloy, Nickel Plated, Antique Silver |
| Number of Card Slots | number | Number of dedicated card pockets in a wallet or card holder | 4, 6, 8, 12 |
| ID Window | boolean | Whether the wallet includes a transparent identification card window | true, false |
| Coin Pocket | boolean | Whether the product includes a dedicated coin compartment | true, false |
| RFID Blocking | boolean | Whether the product contains a shielding lining to block contactless card scanning | true, false |
| Lining Material | text | Material used for interior lining | Cotton Twill, Nylon, Pigskin, Suede, Unlined |
| Closure Type | enum | Mechanism used to keep the product closed | Snap, Zipper, Magnetic, Fold-Over, Buckle, None |
| Stitching Type | text | Thread type and construction method | Hand-Stitched, Machine-Stitched, Saddle-Stitched, Riveted |
| Edge Finish | text | Treatment applied to the cut edges of the leather | Burnished, Painted, Raw, Waxed, Beveled |
| Saddle Seat Size | number (inches) | Rider seat size measured from pommel to cantle for saddle products | 14, 15, 16, 17 |
| Saddle Tree Type | text | Frame material and shape of the saddle tree for saddle products | Fiberglass, Wood, Ralide, Flex Tree |
| Saddle Gullet Width | number (inches) | Width of the saddle gullet channel for saddle products | 6.5, 7.0, 7.5, 8.0 |
| Country of Origin | text | Country where the product was manufactured | USA, India, Mexico, Italy, Argentina |
| Warranty | text | Manufacturer warranty duration or type | Lifetime, 100 Years, 5 Years, 1 Year |
| Personalization Available | boolean | Whether the product can be monogrammed, embossed, or otherwise customized | true, false |
| Pack Quantity | number | Number of units per pack for wholesale orders | 1, 6, 12, 24 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (belt sizing, saddle fitting, leather goods manufacturing specs) | [Hanks Belts](https://www.hanksbelts.com/collections/wallets), [Buffalo Billfold Company](https://buffalobillfoldcompany.com/wholesale-leather-goods/), [Texas Saddlery](https://txsaddlery.com/), [Tandy Leather](https://tandyleather.com/) |
