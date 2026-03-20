# SKU Schema: Office Desks, Workstations & Cubicles

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.office_desks_workstations`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | EOD660MR, WN-6630-BK, BBF-ProPanels-66H |
| Product Name | product_name | text | — | yes | Full product name including key specs such as configuration, size, and panel height | Bush Easy Office 60W 4-Person Cubicle 66H, VersaDesk WorkNest Corner Workstation, Herman Miller Layout Studio 120x60 Desk |
| URL | url | text | — | yes | Direct link to the product page | https://example.com/product/easy-office-4person-cubicle |
| Price | price | number | — | yes | Numeric price per unit or per configuration excluding currency symbol | 649.99, 1299.00, 4500.00, 12000.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Product Type | product_type | enum | — | — | Specific type of office desk or workstation | Single Desk, L-Shaped Desk, U-Shaped Desk, Standing Desk, Cubicle System, Benching System, Workstation Cluster, Reception Desk, Credenza, Corner Workstation |
| Desktop Material | desktop_material | text | — | — | Material of the work surface | High-Pressure Laminate (HPL), Thermally Fused Laminate (TFL), Solid Wood, Veneer, Glass, Bamboo, Linoleum |
| Panel Material | panel_material | text | — | — | Material and surface of the partition panels | Fabric-Wrapped, Frosted Acrylic, Glass, Metal, Tackable Fabric, Laminate, Acoustic Felt |
| Frame/Leg Material | frameleg_material | text | — | — | Material of the desk frame or support legs | Powder-Coated Steel, Aluminum, Chrome, Laminate End Panels |
| Pedestal Type | pedestal_type | text | — | — | Type of under-desk storage pedestal | Box/Box/File, File/File, Mobile Pedestal, Fixed Pedestal, None |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Country of Origin | country_of_origin | text | — | — | Country where the product is manufactured | USA, China, Canada, Mexico, Germany |
| Number of Workstations | number_of_workstations | number | — | — | Count of individual workspaces in a multi-person configuration | 1, 2, 4, 6, 8, 12 |
| Desktop Width | desktop_width | number | mm | — | Width of the primary work surface | 1200, 1500, 1800, 2100 |
| Desktop Depth | desktop_depth | number | mm | — | Depth of the primary work surface | 600, 700, 750, 800 |
| Desktop Height | desktop_height | number | mm | — | Height of the work surface from floor (fixed desks) | 710, 730, 750, 760 |
| Desktop Thickness | desktop_thickness | number | mm | — | Thickness of the work surface | 22, 25, 30 |
| Panel Height | panel_height | number | mm | — | Height of surrounding privacy panels in cubicle systems | 1040, 1350, 1520, 1680, 2100 |
| Panel Thickness | panel_thickness | number | mm | — | Thickness of the partition panels | 50, 64, 75 |
| Finish | finish | text | — | — | Surface finish or color of the desktop and panels | White, Mahogany, Natural Maple, Mocha Cherry, Espresso, Storm Grey, Black |
| Height Adjustable | height_adjustable | boolean | — | — | Whether the desk supports electric or manual sit-stand adjustment | true, false |
| Minimum Height | minimum_height | number | mm | — | Lowest height setting for height-adjustable desks | 600, 630, 650 |
| Maximum Height | maximum_height | number | mm | — | Highest height setting for height-adjustable desks | 1050, 1200, 1270 |
| Number of Drawers | number_of_drawers | number | — | — | Count of built-in pedestal or under-desk drawers | 0, 1, 2, 3 |
| Cable Management | cable_management | boolean | — | — | Whether the desk includes built-in grommets, trays, or channels for cable routing | true, false |
| Power/Data Integration | powerdata_integration | text | — | — | Built-in electrical outlets and data connectivity | 2 AC Outlets + 2 USB, 4 AC Outlets, Daisy-Chain Power, Data Port Ready, None |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (BIFMA X5.5, ANSI/BIFMA X5.6, EN 527) | [Bush Business Furniture](https://www.bushbusinessfurniture.com/collections/commercial-office-cubicles-and-partitions), [National Business Furniture](https://www.nationalbusinessfurniture.com/cubicles-partitions/office-cubicles), [VersaDesk](https://versadesk.com/collections/worknest-office-cubicles), [Cubicles.com](https://www.cubicles.com/office-workstations/) |
