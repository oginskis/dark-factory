# SKU Schema: Office Desks, Workstations & Cubicles

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | EOD660MR, WN-6630-BK, BBF-ProPanels-66H |
| Product Name | text | Full product name including key specs such as configuration, size, and panel height | Bush Easy Office 60W 4-Person Cubicle 66H, VersaDesk WorkNest Corner Workstation, Herman Miller Layout Studio 120x60 Desk |
| URL | text | Direct link to the product page | https://example.com/product/easy-office-4person-cubicle |
| Price | number | Numeric price per unit or per configuration excluding currency symbol | 649.99, 1299.00, 4500.00, 12000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand/Manufacturer | text | Office furniture brand or manufacturer | Bush Business Furniture, Herman Miller, Steelcase, VersaDesk, Kimball, National, Global, Haworth |
| Product Type | enum | Specific type of office desk or workstation | Single Desk, L-Shaped Desk, U-Shaped Desk, Standing Desk, Cubicle System, Benching System, Workstation Cluster, Reception Desk, Credenza, Corner Workstation |
| Number of Workstations | number | Count of individual workspaces in a multi-person configuration | 1, 2, 4, 6, 8, 12 |
| Desktop Width | number (mm) | Width of the primary work surface | 1200, 1500, 1800, 2100 |
| Desktop Depth | number (mm) | Depth of the primary work surface | 600, 700, 750, 800 |
| Desktop Height | number (mm) | Height of the work surface from floor (fixed desks) | 710, 730, 750, 760 |
| Desktop Thickness | number (mm) | Thickness of the work surface | 22, 25, 30 |
| Desktop Material | text | Material of the work surface | High-Pressure Laminate (HPL), Thermally Fused Laminate (TFL), Solid Wood, Veneer, Glass, Bamboo, Linoleum |
| Panel Height | number (mm) | Height of surrounding privacy panels in cubicle systems | 1040, 1350, 1520, 1680, 2100 |
| Panel Thickness | number (mm) | Thickness of the partition panels | 50, 64, 75 |
| Panel Material | text | Material and surface of the partition panels | Fabric-Wrapped, Frosted Acrylic, Glass, Metal, Tackable Fabric, Laminate, Acoustic Felt |
| Frame/Leg Material | text | Material of the desk frame or support legs | Powder-Coated Steel, Aluminum, Chrome, Laminate End Panels |
| Finish | text | Surface finish or color of the desktop and panels | White, Mahogany, Natural Maple, Mocha Cherry, Espresso, Storm Grey, Black |
| Height Adjustable | boolean | Whether the desk supports electric or manual sit-stand adjustment | true, false |
| Minimum Height | number (mm) | Lowest height setting for height-adjustable desks | 600, 630, 650 |
| Maximum Height | number (mm) | Highest height setting for height-adjustable desks | 1050, 1200, 1270 |
| Number of Drawers | number | Count of built-in pedestal or under-desk drawers | 0, 1, 2, 3 |
| Pedestal Type | text | Type of under-desk storage pedestal | Box/Box/File, File/File, Mobile Pedestal, Fixed Pedestal, None |
| Cable Management | boolean | Whether the desk includes built-in grommets, trays, or channels for cable routing | true, false |
| Power/Data Integration | text | Built-in electrical outlets and data connectivity | 2 AC Outlets + 2 USB, 4 AC Outlets, Daisy-Chain Power, Data Port Ready, None |
| Power Entry Method | enum | How electrical power is fed into the cubicle system | Floor Entry, Ceiling Pole, Wall Feed, Not Applicable |
| Wire Management Pathway | text | Where cables are routed within the cubicle panels | Base Raceway, Beltline Pathway, Top Cap Raceway, Vertical Channel |
| Acoustic Rating | text | Sound absorption class or NRC rating of the panels | NRC 0.50, NRC 0.65, NRC 0.85, STC 18, STC 24 |
| Configuration Layout | text | Spatial arrangement of the workstation cluster | Inline, L-Shape, T-Shape, Bullpen, 120-Degree, Back-to-Back, Pod of 4 |
| Weight Capacity | number (kg) | Maximum recommended load on the desktop surface | 50, 80, 100, 160 |
| Product Weight | number (kg) | Total weight of the desk or system as shipped | 30, 55, 90, 200 |
| Assembly Required | boolean | Whether the product requires professional or DIY assembly | true, false |
| GSA Contract | boolean | Whether the product is available under a US General Services Administration contract | true, false |
| Warranty | text | Manufacturer warranty duration | 5 Years, 10 Years, 12 Years, Lifetime |
| Certification | text (list) | Safety, quality, or environmental certifications | BIFMA Certified, GREENGUARD Gold, level by BIFMA, SCS Indoor Advantage Gold, ANSI/BIFMA X5.5, FSC |
| Country of Origin | text | Country where the product is manufactured | USA, China, Canada, Mexico, Germany |
| Style | text | Design or aesthetic style | Modern, Corporate, Industrial, Minimalist, Contemporary |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus industry standards (BIFMA X5.5, ANSI/BIFMA X5.6, EN 527) | [Bush Business Furniture](https://www.bushbusinessfurniture.com/collections/commercial-office-cubicles-and-partitions), [National Business Furniture](https://www.nationalbusinessfurniture.com/cubicles-partitions/office-cubicles), [VersaDesk](https://versadesk.com/collections/worknest-office-cubicles), [Cubicles.com](https://www.cubicles.com/office-workstations/) |
