# SKU Schema: Flat Glass & Architectural Glass

**Last updated:** 2026-03-15
**Parent category:** Construction Materials & Glass/Ceramics

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Manufacturer or distributor product identifier | VIT-SB90-6MM, GRD-CG-8CLR, AGC-PP60-10 |
| Product Name | text | Full product name including key specs such as glass type, coating, and thickness | Vitro Solarban 90 Low-E Glass 6mm, Guardian ClimaGuard 80/70 IGU, AGC Planibel Clear Float 10mm |
| URL | text | Direct link to the product page | https://example.com/product/solarban-90-low-e |
| Price | number | Numeric price per square metre or per sheet, excluding currency symbol | 18.50, 42.00, 85.00, 150.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CNY |
| Brand | text | Manufacturer or brand name | Vitro, Guardian, AGC, Saint-Gobain, Pilkington, PPG, Schott, Cardinal |
| Glass Category | enum | Primary product classification | Float Glass, Low-E Glass, Tinted Glass, Reflective Glass, Laminated Glass, Tempered Glass, Insulating Glass Unit, Patterned Glass, Wired Glass, Low-Iron Glass |
| Glass Composition | text | Base glass type or formulation | Soda-Lime, Borosilicate, Aluminosilicate, Low-Iron (Ultra-Clear) |
| Coating Type | text | Type of performance coating applied to the glass surface | Soft-Coat (Sputtered), Hard-Coat (Pyrolytic), None |
| Coating Position | text | Surface number on which the coating is applied (surface 1 is exterior) | Surface 2, Surface 3, Surface 2 and 3 |
| Nominal Thickness | number (mm) | Thickness of a single glass lite | 2, 3, 4, 5, 6, 8, 10, 12, 15, 19, 25 |
| IGU Total Thickness | number (mm) | Overall thickness of the insulating glass unit including spacers and airspace | 20, 24, 28, 32, 36, 44 |
| Airspace Width | number (mm) | Width of the gas-filled cavity in an IGU | 6, 9, 12, 16, 20 |
| Gas Fill | text | Gas type in the IGU cavity | Air, Argon, Krypton, Argon/Krypton Mix |
| U-Value (Center of Glass) | number (W/m2K) | Center-of-glass thermal transmittance | 1.0, 1.3, 1.6, 2.7, 3.2, 5.8 |
| Solar Heat Gain Coefficient | number | Fraction of solar energy transmitted through the glass (0 to 1) | 0.20, 0.27, 0.34, 0.40, 0.60, 0.86 |
| Visible Light Transmittance | number (%) | Percentage of visible light (380-780nm) transmitted through the glass | 14, 40, 51, 62, 70, 82, 90 |
| Visible Light Reflectance (Exterior) | number (%) | Percentage of visible light reflected from the exterior surface | 8, 11, 15, 22, 33, 42 |
| Solar Reflectance | number (%) | Percentage of total solar energy reflected | 7, 12, 20, 33, 45 |
| UV Transmittance | number (%) | Percentage of ultraviolet light transmitted | 0.1, 1.0, 5.0, 25.0, 40.0 |
| Color (Transmitted) | text | Apparent color of the glass when viewed in transmission | Clear, Blue, Green, Gray, Bronze, Neutral |
| Color (Reflected Exterior) | text | Apparent color when viewed from outside | Silver, Blue-Green, Neutral Gray, Gold |
| Maximum Sheet Size | text (mm) | Maximum available sheet dimension (width x height) | 3210 x 6000, 3300 x 6000, 2540 x 3660 |
| Weight per Square Metre | number (kg/m2) | Mass per unit area of a single lite | 5.0, 7.5, 10.0, 12.5, 15.0, 20.0, 25.0 |
| Safety Classification | text | Safety glazing standard and class | ANSI Z97.1 Class A, ANSI Z97.1 Class B, EN 12600 1B1, EN 12600 2B2, CPSC 16 CFR 1201 Cat I, CPSC 16 CFR 1201 Cat II |
| Fire Rating | text | Fire resistance rating of the glass assembly | E 30, E 60, EW 30, EI 30, EI 60, EI 90, 20 min, 45 min, 60 min |
| Sound Transmission Class | number | STC acoustic attenuation rating | 28, 31, 34, 38, 42, 48 |
| Interlayer Type | text | Type of interlayer in laminated glass | PVB, SGP (SentryGlas), EVA, Acoustic PVB, Colored PVB |
| Applicable Standard | text (list) | Industry standards the product conforms to | ASTM C1036, ASTM C1048, EN 572, EN 1096, EN 12150, EN 14449, ISO 12543 |
| Certification | text (list) | Quality and performance certifications | IGCC/IGMA Certified, SGCC, CE, NFRC, Energy Star |
| Country of Origin | text | Country where the glass was manufactured | USA, Belgium, Japan, France, Germany, UK, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 31 attributes from 4 companies plus ASTM C1036 and NFRC standards | [Vitro Architectural Glass](https://www.vitroglazings.com/technical-information/technical-data-sheets/), [Guardian Glass](https://www.guardianglass.com/us/en/tools-and-resources/resources/technical-literature), [AGC Glass](https://www.agc.com/en/products/flat_glass/index.html), [ASTM C1036](https://store.astm.org/c1036-21.html) |
