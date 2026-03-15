# SKU Schema: Technical & Industrial Textiles

**Last updated:** 2026-03-15
**Parent category:** Textiles, Fabrics & Leather

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | GT-315W, NW-8oz, HT-200PP |
| Product Name | text | Full product name including key specs such as type, weight, and strength class | Woven Polypropylene Geotextile 315 lbs Grab Tensile, Nonwoven Polyester Filter Fabric 8 oz |
| URL | text | Direct link to the product page | https://example.com/product/woven-geotextile-315 |
| Price | number | Numeric price per unit (per square yard, linear foot, or roll), excluding currency symbol | 0.45, 2.80, 350.00, 1200.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Brand/Manufacturer | text | Manufacturer or supplier name | WINFAB, US Fabrics, HUESKER, SKAPS Industries, AGRU, Mehler Engineered Products |
| Product Type | enum | Primary technical textile classification | Woven Geotextile, Nonwoven Geotextile, Geogrid, Geomembrane, Filter Fabric, Erosion Control Blanket, Conveyor Belt Fabric, Architectural Membrane, Protective Fabric, Airbag Fabric |
| Construction Method | enum | How the textile is manufactured | Woven Slit Film, Woven Monofilament, Woven Multifilament, Needlepunch Nonwoven, Spunbond, Meltblown, Knitted, Composite |
| Polymer Type | text | Base polymer material | Polypropylene, Polyester, HDPE, Nylon, Aramid, Fiberglass, PVC-Coated Polyester |
| Weight | number (oz/yd2) | Mass per unit area in ounces per square yard | 3.0, 4.5, 6.3, 8.0, 12.0, 16.0 |
| Weight Metric | number (GSM) | Mass per unit area in grams per square metre | 100, 150, 214, 270, 400, 540 |
| Thickness | number (mm) | Material thickness measured under standard pressure | 0.5, 1.0, 1.5, 2.5, 4.0 |
| Grab Tensile Strength MD | number (lbs) | Maximum load in the machine direction per ASTM D4632 | 115, 180, 247, 315, 500 |
| Grab Tensile Strength XD | number (lbs) | Maximum load in the cross-machine direction per ASTM D4632 | 100, 160, 220, 315, 450 |
| Grab Elongation | number (%) | Percentage stretch at break per ASTM D4632 | 15, 25, 50, 65 |
| Wide Width Tensile Strength | number (kN/m) | Tensile strength per unit width per ASTM D4595 for high-performance products | 20, 50, 100, 200, 400 |
| Trapezoid Tear Strength | number (lbs) | Tear resistance per ASTM D4533 | 50, 75, 120, 200 |
| CBR Puncture Resistance | number (lbs) | Resistance to puncture per ASTM D6241 | 200, 500, 1000, 1500, 3000 |
| Permittivity | number (1/s) | Rate of water flow through the fabric per unit head per ASTM D4491 | 0.02, 0.05, 0.10, 0.50, 1.50 |
| Water Flow Rate | number (gpm/ft2) | Volume of water passing through per unit area per ASTM D4491 | 4, 10, 25, 60, 120 |
| Apparent Opening Size | number (mm) | Effective pore size indicating filtration capability per ASTM D4751 | 0.15, 0.21, 0.30, 0.425, 0.60 |
| UV Resistance | text | Percentage of strength retained after UV exposure per ASTM D4355 | 50% at 500 hrs, 70% at 500 hrs, 90% at 1000 hrs |
| Width | number (ft) | Roll width in feet | 6, 12, 12.5, 15, 17.5 |
| Roll Length | number (ft) | Standard roll length in feet | 258, 300, 360, 432 |
| Roll Area | number (yd2) | Total area per roll in square yards | 300, 500, 600, 1000 |
| Max Operating Temperature | number (F) | Maximum continuous-use temperature | 200, 300, 400, 500 |
| Fire Retardancy | text | Flame resistance rating or standard compliance | FR Treated, Inherently FR, ASTM E84 Class A, DIN 4102-B1 |
| Coating Type | text | Surface coating or treatment applied to the textile | PVC, PTFE, Silicone, Rubber, Latex, Uncoated |
| Application | text (list) | Primary intended uses and end markets | Road Stabilization, Drainage Filtration, Erosion Control, Landfill Lining, Coastal Protection, Mining, Agriculture |
| Certification | text (list) | Product and quality certifications | AASHTO M288, ISO 9001, ISO 10318, CE Marked, NTPEP |
| AASHTO Class | text | Geotextile strength class per AASHTO M288 | Class 1, Class 2, Class 3 |
| Country of Origin | text | Country where the product was manufactured | USA, Germany, India, China, Netherlands |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 32 attributes from 4 companies plus ASTM and AASHTO geotextile standards | [WINFAB Industrial Fabrics](https://www.winfabusa.com/geotextile-fabric-types-and-applications/), [US Fabrics](https://www.usfabricsinc.com/products/geotextiles/), [Erosion Control Products](https://www.erosioncontrol-products.com/wovengeotextiles.html), [HUESKER](https://www.huesker.us/) |
