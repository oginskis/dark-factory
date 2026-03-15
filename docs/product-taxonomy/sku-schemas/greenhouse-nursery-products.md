# SKU Schema: Greenhouse & Nursery Products

**Last updated:** 2026-03-15
**Parent category:** Agricultural Products, Livestock & Equipment

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | HG-CCTW-0812BR, GM-5050, AML-4620, PG0101-13GY |
| Product Name | text | Full product name including key specs such as product type, material, and dimensions | Traditional Fivewall Polycarbonate Greenhouse Kit 8x12 ft, Standard Round Nursery Pot 5 Gallon, 50-Cell Forestry Tray |
| URL | text | Direct link to the product page | https://example.com/product/greenhouse-kit-8x12 |
| Price | number | Numeric price per unit or per pack, excluding currency symbol | 14718.00, 3.49, 24.95, 544.34 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD, AUD |
| Brand | text | Manufacturer or brand name | BC Greenhouse, Canopia by Palram, Greenhouse Megastore, T.O. Plastics, Stuewe and Sons, The HC Companies |
| Product Category | enum | Primary product classification within greenhouse and nursery supplies | Greenhouse Kit, Growing Container, Seed Starting Tray, Growing Media, Greenhouse Film, Shade Cloth, Frost Blanket, Heat Mat, Plant Label, Plant Support, Ventilation Equipment, Irrigation Component, Bench or Shelving, Propagation Dome |
| Material | text | Primary construction material | Polycarbonate, Tempered Glass, Polyethylene Film, Aluminum, Galvanized Steel, Plastic, Bamboo, Fiber |
| Panel Type | text | Glazing or covering panel specification for greenhouse structures | 16mm Five-Wall Polycarbonate, 6mm Twin-Wall Polycarbonate, 4mm Tempered Glass, 6 mil Poly Film, 8mm Twin-Wall Polycarbonate |
| Panel Thickness | number (mm) | Thickness of glazing or covering panel material | 0.15, 4, 6, 8, 10, 16 |
| Light Transmission | number (%) | Percentage of photosynthetically active radiation (PAR) transmitted through the covering material | 40, 62, 82, 90 |
| R-Value | number | Thermal insulation rating of the covering material (higher is more insulating) | 0.83, 1.54, 2.30, 3.03 |
| UV Protection | boolean | Whether the material includes UV stabilization or blocking | true, false |
| UV Rating | text | Expected lifespan of UV protection or stabilization treatment | 4 year, 5 year, 10 year, Lifetime |
| Width | number (mm) | Overall width of the structure, container, or product | 152, 610, 2616, 3251 |
| Length | number (mm) | Overall length or depth of the structure or product | 279, 559, 3861, 12649 |
| Height | number (mm) | Overall height or peak height of the structure | 50, 127, 2134, 2794 |
| Sidewall Height | number (mm) | Height of the vertical sidewall for greenhouse structures | 1219, 1372, 1676, 1829 |
| Floor Area | number (m2) | Interior growing floor area of a greenhouse structure | 7.4, 14.9, 24.8, 55.7 |
| Volume | number (L) | Volume capacity for containers, pots, or trays | 0.5, 3.8, 11.4, 18.9 |
| Cell Count | number | Number of individual growing cells in a plug tray or flat | 21, 32, 50, 72, 128, 606 |
| Container Diameter | number (mm) | Top inside diameter of round nursery pots | 76, 102, 152, 254, 381 |
| Drainage | enum | Drainage provision in growing containers | Drainage Holes, No Holes, Mesh Bottom, Slit |
| Ventilation Type | text (list) | Types of ventilation provided in a greenhouse structure | Roof Vent, Side Louvre, Roll-Up Side, Ridge Vent, Exhaust Fan |
| Number of Vents | number | Count of ventilation openings included in the structure | 1, 2, 4, 8 |
| Automatic Vent Opener | boolean | Whether temperature-activated automatic vent openers are included or available | true, false |
| Door Type | text | Entry door style and configuration | Single Hinged, Double Sliding, Roll-Up, Dutch Door |
| Door Dimensions | text | Width and height of the entry door | 32x76 in, 48x77 in, 4x6.5 ft |
| Wind Load Rating | number (km/h) | Maximum wind speed the structure is rated to withstand | 90, 120, 145, 160 |
| Snow Load Rating | number (kg/m2) | Maximum snow load the structure is rated to support | 50, 75, 100, 150 |
| Frame Color | text | Color or finish of the structural frame | Green, White, Silver, Brown, Gray, Blue Grass |
| Weight | number (kg) | Shipping or assembled weight of the product | 0.05, 2.5, 45.0, 250.0 |
| Pack Quantity | number | Number of units per pack or case (1 if sold individually) | 1, 10, 50, 100, 1000 |
| Foundation Type | text | Required or recommended base or foundation for greenhouse structures | Concrete Slab, Concrete Piers, Treated Timber Base, Ground Stakes, None Required |
| Warranty | text | Manufacturer warranty terms | 1 year, 5 year frame, 10 year panels, Lifetime frame |
| Country of Origin | text | Country where the product was manufactured | USA, Canada, UK, China, Israel, Netherlands |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 37 attributes from 4 companies plus USDA hardiness zone standards and NGMA greenhouse classification guidelines | [Greenhouse Megastore](https://www.greenhousemegastore.com/collections/supplies), [A.M. Leonard](https://www.amleo.com/c/greenhouse-supplies), [Growers Supply](https://www.growerssupply.com/home), [Farm Plastic Supply](https://farmplasticsupply.com/greenhouse-supplies) |
