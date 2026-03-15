# SKU Schema: Bedroom Furniture (Beds, Mattresses, Dressers)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 890.066.63, B553-77, TN-QN-10 |
| Product Name | text | Full product name including key specs such as type, size, and style | MALM Queen Bed Frame with 4 Storage Boxes Black-Brown, Willowton King Panel Bed, Sealy Posturepedic Plus Mount Auburn 13 in Plush Queen Mattress |
| URL | text | Direct link to the product page | https://example.com/product/malm-bed-frame |
| Price | number | Numeric price per unit excluding currency symbol | 299.00, 849.99, 1599.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Furniture brand or manufacturer name | IKEA, Ashley Furniture, Sealy, Tempur-Pedic, Casper, Pottery Barn |
| Product Type | enum | Specific type of bedroom furniture | Bed Frame, Platform Bed, Panel Bed, Mattress, Dresser, Nightstand, Chest of Drawers, Wardrobe, Vanity, Headboard |
| Bed Size | enum | Standard mattress size category | Twin, Twin XL, Full/Double, Queen, King, California King |
| Mattress Dimensions | text (mm) | Mattress length x width as specified by the size standard | 1905 x 990, 1905 x 1370, 2030 x 1525, 2030 x 1930, 2135 x 1830 |
| Overall Width | number (mm) | Total outer width of the piece | 1000, 1540, 1670, 2000 |
| Overall Depth/Length | number (mm) | Total outer depth or length of the piece | 2100, 400, 500, 2200 |
| Overall Height | number (mm) | Total height from floor to top (headboard for beds, top surface for dressers) | 1000, 1200, 850, 780 |
| Headboard Height | number (mm) | Height of the headboard measured from the floor | 1100, 1300, 1450 |
| Footboard Height | number (mm) | Height of the footboard measured from the floor | 300, 450, 600 |
| Clearance Under Bed | number (mm) | Space between the floor and the bed base for under-bed storage | 100, 200, 260, 350 |
| Frame Material | text | Primary structural material of the bed frame or dresser | Solid Pine, Engineered Wood, Metal, Solid Oak, Walnut Veneer, Upholstered |
| Finish | text | Surface finish or color of the piece | White, Black-Brown, Natural Oak, Espresso, Grey Wash, Weathered Pine |
| Slat System | text | Type of mattress support system included in bed frames | Slatted Base Included, Platform (No Slats), Bunkie Board Required, Foundation Required |
| Number of Drawers | number | Count of storage drawers in beds with storage, dressers, or nightstands | 2, 3, 4, 6, 8 |
| Storage Type | text | Type of built-in storage in beds or dressers | Under-Bed Drawers, Ottoman Lift, Bookcase Headboard, Felt-Lined Top Drawer, None |
| Mattress Type | enum | Construction category for mattresses | Innerspring, Pocket Coil, Memory Foam, Latex, Hybrid, Pillow Top |
| Firmness Level | text | Comfort firmness rating for mattresses | Plush, Medium, Medium-Firm, Firm, Extra Firm |
| Mattress Thickness | number (mm) | Total height/profile of the mattress | 200, 254, 305, 356 |
| Coil Count | number | Number of coils or springs in innerspring and hybrid mattresses | 300, 600, 800, 1000, 1200 |
| Coil Gauge | number | Wire gauge of the coils (lower number equals firmer) | 13, 14, 15, 16 |
| Comfort Layer Material | text | Material of the top comfort layers in mattresses | Gel Memory Foam, Latex, Pillow Top Fiber, Copper-Infused Foam |
| Weight Capacity | number (kg) | Maximum recommended weight the bed frame or mattress supports | 136, 227, 300, 450 |
| Product Weight | number (kg) | Total weight of the product as shipped or assembled | 25, 45, 68, 95 |
| Assembly Required | boolean | Whether the product requires assembly | true, false |
| Style | text | Design or aesthetic style | Modern, Farmhouse, Traditional, Mid-Century, Industrial, Coastal |
| Collection | text | Named product line or series from the manufacturer | MALM, Hemnes, Willowton, Crestaire, Beautyrest Black |
| Warranty | text | Manufacturer warranty coverage period | 1 Year, 5 Years, 10 Years, 25 Years |
| Certification | text (list) | Safety, quality, or environmental certifications | CertiPUR-US, GREENGUARD Gold, OEKO-TEX, BIFMA, CPSC Compliant |
| Country of Origin | text | Country where the product is manufactured | China, Vietnam, USA, Sweden, Malaysia, Mexico |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 34 attributes from 4 companies plus industry standards (BIFMA, EN 1725, ASTM F1566) | [IKEA](https://www.ikea.com/us/en/cat/beds-bm003/), [Ashley Furniture](https://www.ashleyfurniture.com/c/bedroom/beds/), [ESF Wholesale Furniture](https://www.esfwholesalefurniture.com/catalog/Bedroom-Furniture/), [Casper](https://casper.com/blogs/article/mattress-firmness-scale) |
