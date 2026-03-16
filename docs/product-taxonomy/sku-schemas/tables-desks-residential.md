# SKU Schema: Tables & Desks (Residential)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.tables_desks_residential`


## Core Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| SKU | sku | text | — | Retailer or manufacturer product identifier | 904.736.05, D631-35, PB-FH-DSK-72 |
| Product Name | product_name | text | — | Full product name including key specs such as type, shape, and material | LISABO Dining Table Ash Veneer 140x78 cm, Owingsville Rectangular Dining Table, Tremont Reclaimed Wood Desk 72 in |
| URL | url | text | — | Direct link to the product page | https://example.com/product/lisabo-table |
| Price | price | number | — | Numeric price per unit excluding currency symbol | 29.99, 449.00, 1895.00 |
| Currency | currency | text | — | ISO 4217 currency code | USD, EUR, GBP, AUD, CAD |
| Furniture Type | furniture_type | enum | — | Specific type of table or desk | Dining Table, Coffee Table, Console Table, Side Table, Writing Desk, Executive Desk, Standing Desk, Vanity Desk, Accent Table, Counter-Height Table |
| Top Material | top_material | text | — | Material of the table or desk top surface | Solid Oak, Walnut Veneer, Marble, Glass, Engineered Wood, Reclaimed Pine, Concrete, MDF, Bamboo |
| Base/Leg Material | baseleg_material | text | — | Material of the legs or pedestal base | Solid Wood, Metal (Steel), Cast Iron, Chrome, Brass, Turned Wood, Trestle |
| Country of Origin | country_of_origin | text | — | Country where the product is manufactured | China, Vietnam, Poland, USA, India, Indonesia |
| Top Length | top_length | number | mm | Length or diameter of the table top | 750, 1200, 1600, 2000, 2440 |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Description | Example Values |
|--------|--------|--------|--------|--------|--------|
| Shape | shape | enum | — | Top surface shape | Rectangular, Round, Oval, Square, L-Shaped, Kidney |
| Top Width | top_width | number | mm | Width of the table top (depth for desks) | 500, 600, 750, 900, 1050 |
| Height | height | number | mm | Overall height from floor to top surface | 460, 650, 750, 900, 1050 |
| Top Thickness | top_thickness | number | mm | Thickness of the table or desk top surface | 18, 25, 38, 50 |
| Finish | finish | text | — | Surface finish or color of the product | Natural, White, Black, Espresso, Honey, Distressed Grey, Oiled Walnut |
| Number of Drawers | number_of_drawers | number | — | Count of built-in drawers | 0, 1, 2, 3, 5 |
| Number of Shelves | number_of_shelves | number | — | Count of open shelves or cubbies | 0, 1, 2, 3 |
| Extendable | extendable | boolean | — | Whether the table has extension leaves or a slide-out mechanism | true, false |
| Number of Leaves | number_of_leaves | number | — | Count of removable or fold-out extension leaves | 0, 1, 2 |
| Height Adjustable | height_adjustable | boolean | — | Whether the desk height can be adjusted (sit-stand desks) | true, false |
| Minimum Height | minimum_height | number | mm | Lowest height setting for adjustable desks | 600, 650, 720 |
| Maximum Height | maximum_height | number | mm | Highest height setting for adjustable desks | 1050, 1200, 1270 |
| Cable Management | cable_management | boolean | — | Whether the desk includes built-in cable routing holes or trays | true, false |
| Assembly Required | assembly_required | boolean | — | Whether the product requires assembly by the buyer | true, false |
| Style | style | text | — | Design or aesthetic style | Modern, Farmhouse, Industrial, Mid-Century Modern, Traditional, Rustic, Scandinavian |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus industry standards (BIFMA, EN 527, EN 12521) | [IKEA](https://www.ikea.com/us/en/cat/desks-tables-20649/), [Ashley Furniture](https://www.ashleyfurniture.com/c/dining-room/tables/), [Pottery Barn](https://www.potterybarn.com/shop/furniture/tables-desks/), [Four Hands](https://fourhands.com/) |
