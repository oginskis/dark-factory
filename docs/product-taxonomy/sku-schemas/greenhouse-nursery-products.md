# SKU Schema: Greenhouse & Nursery Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment
**Taxonomy ID:** `agriculture.greenhouse_nursery`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | HG-CCTW-0812BR, GM-5050, AML-4620, PG0101-13GY |
| Product Name | product_name | text | Full product name including key specs such as product type, material, and dimensions | Traditional Fivewall Polycarbonate Greenhouse Kit 8x12 ft, Standard Round Nursery Pot 5 Gallon, 50-Cell Forestry Tray |
| URL | url | text | Direct link to the product page | https://example.com/product/greenhouse-kit-8x12 |
| Price | price | number | Numeric price per unit or per pack, excluding currency symbol | 14718.00, 3.49, 24.95, 544.34 |
| Currency | currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Product Category | product_category | enum | Primary product classification within greenhouse and nursery supplies | Greenhouse Kit, Growing Container, Seed Starting Tray, Growing Media, Greenhouse Film, Shade Cloth, Frost Blanket, Heat Mat, Plant Label, Plant Support, Ventilation Equipment, Irrigation Component, Bench or Shelving, Propagation Dome |
| Material | material | text | Primary construction material | Polycarbonate, Tempered Glass, Polyethylene Film, Aluminum, Galvanized Steel, Plastic, Bamboo, Fiber |
| Panel Type | panel_type | text | Glazing or covering panel specification for greenhouse structures | 16mm Five-Wall Polycarbonate, 6mm Twin-Wall Polycarbonate, 4mm Tempered Glass, 6 mil Poly Film, 8mm Twin-Wall Polycarbonate |
| Ventilation Type | ventilation_type | text (list) | Types of ventilation provided in a greenhouse structure | Roof Vent, Side Louvre, Roll-Up Side, Ridge Vent, Exhaust Fan |
| Door Type | door_type | text | Entry door style and configuration | Single Hinged, Double Sliding, Roll-Up, Dutch Door |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Foundation Type | foundation_type | text | Required or recommended base or foundation for greenhouse structures | Concrete Slab, Concrete Piers, Treated Timber Base, Ground Stakes, None Required |
| Country of Origin | country_of_origin | text | Country where the product was manufactured | USA, Canada, UK, China, Israel, Netherlands |
| Panel Thickness | panel_thickness | number (mm) | Thickness of glazing or covering panel material | 0.15, 4, 6, 8, 10, 16 |
| Light Transmission | light_transmission | number (%) | Percentage of photosynthetically active radiation (PAR) transmitted through the covering material | 40, 62, 82, 90 |
| R-Value | r-value | number | Thermal insulation rating of the covering material (higher is more insulating) | 0.83, 1.54, 2.30, 3.03 |
| UV Protection | uv_protection | boolean | Whether the material includes UV stabilization or blocking | true, false |
| UV Rating | uv_rating | text | Expected lifespan of UV protection or stabilization treatment | 4 year, 5 year, 10 year, Lifetime |
| Width | width | number (mm) | Overall width of the structure, container, or product | 152, 610, 2616, 3251 |
| Height | height | number (mm) | Overall height or peak height of the structure | 50, 127, 2134, 2794 |
| Sidewall Height | sidewall_height | number (mm) | Height of the vertical sidewall for greenhouse structures | 1219, 1372, 1676, 1829 |
| Floor Area | floor_area | number (m2) | Interior growing floor area of a greenhouse structure | 7.4, 14.9, 24.8, 55.7 |
| Volume | volume | number (L) | Volume capacity for containers, pots, or trays | 0.5, 3.8, 11.4, 18.9 |
| Drainage | drainage | enum | Drainage provision in growing containers | Drainage Holes, No Holes, Mesh Bottom, Slit |
| Number of Vents | number_of_vents | number | Count of ventilation openings included in the structure | 1, 2, 4, 8 |
| Automatic Vent Opener | automatic_vent_opener | boolean | Whether temperature-activated automatic vent openers are included or available | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus USDA hardiness zone standards and NGMA greenhouse classification guidelines | [Greenhouse Megastore](https://www.greenhousemegastore.com/collections/supplies), [A.M. Leonard](https://www.amleo.com/c/greenhouse-supplies), [Growers Supply](https://www.growerssupply.com/home), [Farm Plastic Supply](https://farmplasticsupply.com/greenhouse-supplies) |
