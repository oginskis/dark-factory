# SKU Schema: Water & Winter Sports Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Retailer or manufacturer product identifier | BUR-10688107, SAL-L47038, HO-67231, JS-5011 |
| Product Name | text | Full product name including brand, model, and key specs | Burton Custom Camber Snowboard 158cm, Salomon QST Stella 106 Skis 2027, Channel Islands Rocket Wide 6-0 |
| URL | text | Direct link to the product page | https://example.com/product/custom-camber-snowboard |
| Price | number | Numeric retail price excluding currency symbol | 199.99, 449.95, 599.99, 899.00 |
| Currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Brand/Manufacturer | text | Equipment brand or manufacturer name | Burton, Salomon, Rossignol, Volkl, Lib Tech, Channel Islands, Firewire, HO Sports, Hyperlite, Ronix |
| Sport | text | Primary sport the product is designed for | Snowboarding, Alpine Skiing, Cross-Country Skiing, Surfing, Wakeboarding, Water Skiing, Kitesurfing, Stand-Up Paddleboarding |
| Equipment Type | text | Specific product category | Snowboard, Alpine Ski, Surfboard, Wakeboard, Water Ski, SUP Board, Ski Boots, Snowboard Boots, Bindings, Wetsuit |
| Length | number (cm) | Overall length of the board or ski | 148, 155, 158, 168, 172, 182 |
| Length (Surfboard) | text (ft-in) | Overall length of a surfboard in feet and inches | 5-8, 6-0, 6-4, 7-6, 9-0 |
| Width (Waist) | number (mm) | Width at the narrowest point of a ski or snowboard | 80, 88, 100, 106, 252, 260 |
| Tip Width | number (mm) | Width at the widest point of the tip/nose | 120, 134, 280, 295, 302 |
| Tail Width | number (mm) | Width at the widest point of the tail | 115, 128, 270, 285, 295 |
| Effective Edge | number (mm) | Length of the metal edge that contacts the snow surface | 1140, 1200, 1260 |
| Sidecut Radius | text (m) | Turn radius determined by the side profile shape | 7.8, 11.3, 15, 17.5, 22 |
| Profile/Camber | text | Longitudinal flex profile of the board or ski | Camber, Rocker, Flat, Hybrid Camber-Rocker, Reverse Camber, All-Mountain Rocker |
| Flex Rating | text | Stiffness rating on the manufacturer scale (typically 1-10) | 3 (Soft), 5 (Medium), 6 (Medium-Stiff), 8 (Stiff), 10 (Very Stiff) |
| Shape | text | Directional profile of the board or ski | Twin, Directional Twin, Directional, Tapered Directional, Asymmetric |
| Core Material | text | Internal construction material of the board or ski | Wood (Poplar), Super Fly II 700G, Paulownia/Balsa, Titanal/Wood, Carbon Stringer, Foam (EPS), Polyurethane (PU) |
| Base Material | text | Bottom surface material | Sintered, Extruded, Sintered Stone Ground, Epoxy/Fiberglass |
| Construction | text | Layup method for the board or ski | Sandwich, Cap, Hybrid, Full Wrap, Fiberglass Layup, Carbon Wrap |
| Fin Setup | text | Fin configuration for surfboards, wakeboards, or SUPs | Thruster (3-Fin), Quad (4-Fin), 2+1, Single Fin, Twin Fin, 5-Fin Box, Removable |
| Tail Shape | text | Shape of the tail end for surfboards | Squash, Round, Swallow, Pin, Diamond, Square |
| Volume (Surfboard) | number (L) | Total volume of a surfboard in litres affecting buoyancy | 22.5, 28.0, 33.5, 42.0, 65.0 |
| Thickness (Surfboard) | text (inches) | Maximum thickness of a surfboard | 2 1/4, 2 3/8, 2 1/2, 2 5/8, 3 |
| Rider Weight Range | text (kg) | Recommended weight range for the rider | 54-82, 68-91, 82-118 |
| Stance Width | text (mm) | Recommended distance between bindings | 530, 560, 580 |
| Setback | number (mm) | Distance the stance is set back from center toward the tail | 0, 12.5, 25, 50 |
| Binding Compatibility | text | Binding mounting system supported | Burton Channel, 4x4 Insert, 2x4 Insert, Universal Disc, EST |
| DIN Range | text | Release force setting range for ski bindings | 3-10, 4-12, 6-16, 8-18 |
| Terrain | text (list) | Intended snow or water conditions | All-Mountain, Freestyle, Freeride, Powder, Groomed, Park/Pipe, Backcountry, Course, Open Water |
| Skill Level | text | Intended rider ability level | Beginner, Intermediate, Advanced, Expert, All Levels |
| Gender | enum | Target demographic | Men, Women, Unisex, Kids |
| Weight | number (kg) | Weight of the equipment itself | 1.8, 2.5, 3.2, 4.0, 8.5 |
| Certification | text (list) | Safety and performance certifications | CE EN 13319, ISO 6185, CE EN 1077, ASTM F2040 |
| Country of Origin | text | Country where the equipment was manufactured | USA, Austria, France, China, Australia, Thailand |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (ISO 5355 ski boot sole, CE EN 1077 helmet, EN 13319 dive instruments) | [Burton](https://www.burton.com/), [Evo](https://www.evo.com/), [HO Sports](https://www.hosports.com/), [Channel Islands Surfboards](https://cisurfboards.com/) |
