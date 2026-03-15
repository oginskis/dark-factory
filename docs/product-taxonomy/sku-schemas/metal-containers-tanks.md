# SKU Schema: Metal Containers & Tanks

**Last updated:** 2026-03-15
**Parent category:** Metals & Metal Products
**Taxonomy ID:** `metals.containers_tanks`


## Core Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | HT-UL142-AST-1000, SC-ASME-SS-500 |
| Product Name | text | Full product name including type, material, capacity, and certification | UL-142 Double Wall Aboveground Steel Tank 1000 Gallon, ASME 316L Stainless Steel Pressure Vessel 500 Gallon |
| URL | text | Direct link to the product page | https://example.com/product/ul142-double-wall-steel-tank-1000gal |
| Price | number | Numeric unit price excluding currency symbol | 2500.00, 8500.00, 45000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, CAD |
| Tank Type | enum | Primary classification of the container or tank | Aboveground Storage Tank, Underground Storage Tank, Pressure Vessel, Transport Tank, IBC/Tote, Drum, Process Tank, Water Storage Tank, Chemical Storage Tank, Oil/Water Separator, Grease Interceptor |
| Material | text | Primary construction material | Carbon Steel, 304 Stainless Steel, 316 Stainless Steel, Aluminum, Galvanized Steel, Duplex Stainless |
| Material Thickness | text (in) | Shell and head wall thickness | 0.1875, 0.250, 0.3125, 0.375, 0.500, 0.750 |
| Head Type | text | Shape of the tank end closures | Flat, ASME Flanged & Dished, 2:1 Semi-Elliptical, Hemispherical, Conical |
| Country of Origin | text | Country where the tank was fabricated | USA, Canada, Germany, China, India |

## Extended Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Manufacturer | text | Tank or container manufacturer name | Highland Tank, Modern Welding, Sharpsville Container, MERIDIAN Manufacturing, KBK Industries |
| Orientation | enum | Physical orientation of the tank | Horizontal, Vertical |
| Overall Height | number (in) | Overall height for vertical tanks including legs or skirt | 48, 72, 96, 120, 180 |
| Design Pressure | number (psi) | Maximum allowable working pressure | Atmospheric (0), 2.5, 15, 50, 100, 150, 300, 3000 |
| Design Vacuum | number (in H2O) | Maximum allowable vacuum rating | 0, 1.0, 2.77, 15 |
| Design Temperature Range | text (F) | Operating temperature range | -20 to 650, -50 to 400, Ambient |
| Wall Construction | enum | Single or multi-wall configuration | Single Wall, Double Wall, Triple Wall |
| Interior Lining | text | Internal protective coating or lining | None, Epoxy Lined, Rubber Lined, Glass Lined, Phenolic Lined |
| Exterior Coating | text | External surface protection | Primer Only, Alkyd Enamel, Epoxy, Polyurethane, Powder Coated, Galvanized, Fiberglass Reinforced |
| Connections/Fittings | text (list) | Types and sizes of tank openings and fittings | 2in NPT Inlet, 2in NPT Outlet, 4in Manway, 2in Vent, Sight Glass, Drain |
| Mounting/Support | text | How the tank is supported or installed | Saddle Supports, Legs, Skirt, Concrete Pad, Cradle, Buried |
| Certifications | text (list) | Design and fabrication certifications | UL 142, UL 58, UL 2085 Fireguard, ASME Section VIII Div 1, API 650, STI F921, NFPA 30, UN/DOT |
| Seismic Rating | text | Seismic design classification if applicable | IBC Zone 4, ASCE 7, Site-Specific, N/A |
| Contents/Service | text | Intended stored contents or service application | Diesel Fuel, Gasoline, Potable Water, Wastewater, Chemicals, Propane, Lube Oil, Food Grade |
| Secondary Containment | boolean | Whether the tank includes built-in secondary containment | Yes, No |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus UL 142/58, ASME Section VIII, and API 650 standards | [Highland Tank](https://www.highlandtank.com/), [Modern Welding](https://www.modweldco.com/), [Sharpsville Container](https://sharpsvillecontainer.com/), [Tank Depot](https://www.tank-depot.com/industrial/steel/) |
