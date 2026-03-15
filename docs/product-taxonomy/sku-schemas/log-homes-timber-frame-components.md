# SKU Schema: Log Homes & Timber Frame Components

**Last updated:** 2026-03-15
**Parent category:** Wood Products & Lumber

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or retailer product identifier | GE-DL8x8-R38, TH-FL8-KIT, COV-PKG-2400 |
| Product Name | text | Full product name including component type, profile, and key dimensions | 8x8 D-Log Wall System R-38, Timber Frame Post and Beam Kit 2400 sqft, Full Round Log 10in Kiln-Dried Package |
| URL | text | Direct link to the product page | https://example.com/product/d-log-8x8-r38-package |
| Price | number | Numeric price per component, per linear foot, or per package excluding currency symbol | 45.00, 185000.00, 3.75 |
| Currency | text | ISO 4217 currency code | USD, CAD, EUR, GBP |
| Brand/Manufacturer | text | Log home or timber frame manufacturer | Golden Eagle, Timberhaven, PrecisionCraft, Honest Abe, Coventry Log Homes |
| Component Type | enum | Type of structural or architectural component | Log Wall System, Timber Frame Post, Beam, Rafter, Purlin, Ridge Beam, Collar Tie, Truss, Staircase, Gable End, Porch Package |
| Product Form | enum | Whether the product is an individual component or a complete package | Individual Component, Shell Package, Dry-In Package, Complete Kit, Turnkey Package |
| Log Profile | enum | Cross-sectional shape of the log | D-Log, Full Round, Square, Rectangular, Swedish Cope, Beveled, Shiplap, Half Log (Siding) |
| Log/Timber Dimensions | text (in) | Cross-section dimensions of the log or timber | 6x8, 8x8, 6.5in diameter, 10in diameter, 12in diameter |
| Wall Thickness | number (in) | Effective thickness of the wall assembly | 6, 8, 10, 12, 14 |
| Wood Species | text | Tree species used for the logs or timbers | Eastern White Pine, Western Red Cedar, Douglas Fir, Northern White Cedar, Spruce, Yellow Pine |
| Drying Method | enum | How the wood is dried before use | Kiln Dried, Air Dried, Standing Dead, Green |
| Moisture Content | number (%) | Moisture content of wood at time of delivery | 12, 15, 19 |
| Corner Style | text | How logs or timbers interlock at wall corners | Dovetail, Saddle Notch, Butt and Pass, Tongue and Groove, Mortise and Tenon |
| Joinery Method | text | Connection technique between structural members | Tongue and Groove, Double Tongue and Groove, Triple Tongue and Groove, Mortise and Tenon, Steel Gusset, Wooden Peg |
| R-Value | number | Thermal resistance rating of the wall system | 10, 19, 31, 38, 51, 72 |
| Insulation Type | text | Type of insulation used in the wall or roof assembly | Closed-Cell Spray Foam, Rigid Foam, Fiberglass Batt, None (solid log) |
| Sealant System | text | Weather sealing method between logs or panels | Foam Gasket, Log Builder Caulk, 5-Point Seal System, Spline |
| Structural Grade | text | Lumber grading for structural timber components | No. 1, No. 2, Select Structural, Machine Stress Rated |
| Treatment Type | text | Preservative or protective treatment applied to the wood | Borate Treated, Pressure Treated, Untreated, Stained |
| Square Footage | number (sqft) | Total floor area covered by the package or component set | 800, 1500, 2400, 3500, 5000 |
| Package Contents | text (list) | Key components included in a kit or package | Wall Logs, Roof Beams, Purlins, Rafters, T&G Decking, Windows, Doors, Fasteners, Stain |
| Certification | text (list) | Sustainability and building code certifications | FSC, SFI, ICC-ES, PEFC |
| Building Code Compliance | text | Building code standards the product meets | IRC, IBC, NBC (Canada) |
| Energy Rating | text | Energy performance standard compliance | Energy Star, Passive House, LEED Applicable |
| Assembly Method | enum | How components are assembled on site | Pre-Cut Numbered, Handcrafted, CNC Milled, Panelized |
| Country of Origin | text | Country where the logs or timber were sourced and manufactured | USA, Canada, Finland |
| Lead Time | text | Typical manufacturing and delivery timeframe | 8-12 weeks, 12-16 weeks, 16-20 weeks |
| Warranty Duration | text | Length of structural or product warranty | 5 years, 10 years, 25 years, Lifetime |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 29 attributes from 4 companies plus building standards (IRC, IBC, NAHB log home guidelines) | [Golden Eagle Log Homes](https://goldeneagleloghomes.com/research/log-timber-wall-systems.asp), [Timberhaven](https://www.timberhavenloghomes.com/our-products/material-package-specifications/), [Honest Abe Log Homes](https://www.honestabe.com/packages-kits/timber-frame-package-contents/), [Coventry Log Homes](https://coventryloghomes.com/) |
