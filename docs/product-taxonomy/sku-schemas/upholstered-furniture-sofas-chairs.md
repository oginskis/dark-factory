# SKU Schema: Upholstered Furniture (Sofas, Chairs)

**Last updated:** 2026-03-15
**Parent category:** Furniture & Home Furnishings
**Taxonomy ID:** `furniture.upholstered`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | 3590138, LM-S78-BK, 902-501.66 |
| Product Name | text | Full product name including key descriptors such as style, configuration, and upholstery | Ektorp 3-Seat Sofa Tallmyra Beige, Chesterfield Tufted Leather Loveseat, Lincoln 3-Seater Modular Sectional |
| URL | text | Direct link to the product page | https://example.com/product/ektorp-sofa |
| Price | number | Numeric price per unit excluding currency symbol | 499.00, 1299.99, 3200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, AUD |
| Furniture Type | enum | Specific type of upholstered seating | Sofa, Loveseat, Sectional, Accent Chair, Recliner, Chaise Lounge, Sleeper Sofa, Ottoman, Swivel Chair |
| Upholstery Material | text | Primary covering fabric or material | Polyester, Linen, Velvet, Full-Grain Leather, Top-Grain Leather, Faux Leather, Performance Fabric, Cotton Blend |
| Frame Material | text | Internal structural frame material | Solid Hardwood, Engineered Wood, Plywood, Metal, Kiln-Dried Pine |
| Suspension Type | text | Support system under the seat cushions | Sinuous Springs, Webbing, Eight-Way Hand-Tied Springs, No-Sag Springs |
| Leg Material | text | Material of the visible feet or legs | Solid Wood, Metal, Plastic, Brass, Chrome |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Country of Origin | text | Country where the piece is manufactured | China, Vietnam, Italy, USA, Poland, Mexico |
| Overall Width | number (mm) | Total width of the piece from arm to arm | 1800, 2200, 2600, 3050 |
| Overall Depth | number (mm) | Total depth from front to back | 850, 950, 1000, 1420 |
| Overall Height | number (mm) | Total height from floor to top of back | 700, 850, 950 |
| Seat Height | number (mm) | Height from floor to top of seat cushion | 380, 430, 480 |
| Seat Depth | number (mm) | Depth of the seating area from front edge to backrest | 530, 560, 600 |
| Arm Height | number (mm) | Height from floor to top of armrest | 580, 620, 680 |
| Number of Seats | number | Seating positions or nominal capacity | 1, 2, 3, 4, 5 |
| Cushion Fill | text | Seat and back cushion filling material | High-Resilience Foam, Down Blend, Polyester Fiber, Memory Foam, Sinuous Spring, Pocket Coil |
| Foam Density | number (kg/m3) | Density of the seat foam core | 24, 28, 32, 35 |
| Leg Height | number (mm) | Height of the legs from floor to underside of frame | 50, 100, 150, 200 |
| Color | text | Primary upholstery color | Grey, Navy Blue, Beige, Charcoal, Cognac, Cream |
| Style | text | Design or aesthetic style | Modern, Mid-Century Modern, Traditional, Chesterfield, Transitional, Scandinavian |
| Removable Covers | boolean | Whether the upholstery covers are removable and washable | true, false |
| Reversible Cushions | boolean | Whether seat or back cushions can be flipped for extended wear | true, false |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus industry standards (BIFMA, ASTM F1566, EN 12520) | [IKEA](https://www.ikea.com/us/en/cat/sofas-fu003/), [Wayfair](https://www.wayfair.com/furniture/sb0/sofas-c413892.html), [LeisureMod](https://www.leisuremod.com/collections/sofa-manufacturer-and-supplier-usa), [Dimensions.com](https://www.dimensions.com/element/outline-sectional-with-chaise) |
