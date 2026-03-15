# SKU Schema: Water & Winter Sports Equipment

**Last updated:** 2026-03-15
**Parent category:** Sporting Goods, Toys & Recreation
**Taxonomy ID:** `sports.water_winter_sports`


## Core Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| SKU | sku | text | Retailer or manufacturer product identifier | BUR-10688107, SAL-L47038, HO-67231, JS-5011 |
| Product Name | product_name | text | Full product name including brand, model, and key specs | Burton Custom Camber Snowboard 158cm, Salomon QST Stella 106 Skis 2027, Channel Islands Rocket Wide 6-0 |
| URL | url | text | Direct link to the product page | https://example.com/product/custom-camber-snowboard |
| Price | price | number | Numeric retail price excluding currency symbol | 199.99, 449.95, 599.99, 899.00 |
| Currency | currency | text | ISO 4217 currency code | USD, GBP, EUR, CAD, AUD |
| Equipment Type | equipment_type | text | Specific product category | Snowboard, Alpine Ski, Surfboard, Wakeboard, Water Ski, SUP Board, Ski Boots, Snowboard Boots, Bindings, Wetsuit |
| Core Material | core_material | text | Internal construction material of the board or ski | Wood (Poplar), Super Fly II 700G, Paulownia/Balsa, Titanal/Wood, Carbon Stringer, Foam (EPS), Polyurethane (PU) |
| Base Material | base_material | text | Bottom surface material | Sintered, Extruded, Sintered Stone Ground, Epoxy/Fiberglass |
| Country of Origin | country_of_origin | text | Country where the equipment was manufactured | USA, Austria, France, China, Australia, Thailand |
| Length | length | number (cm) | Overall length of the board or ski | 148, 155, 158, 168, 172, 182 |

## Extended Attributes

| Attribute | Key | Data Type | Description | Example Values |
|-----------|-----|-----------|-------------|----------------|
| Sport | sport | text | Primary sport the product is designed for | Snowboarding, Alpine Skiing, Cross-Country Skiing, Surfing, Wakeboarding, Water Skiing, Kitesurfing, Stand-Up Paddleboarding |
| Width (Waist) | width_waist | number (mm) | Width at the narrowest point of a ski or snowboard | 80, 88, 100, 106, 252, 260 |
| Tip Width | tip_width | number (mm) | Width at the widest point of the tip/nose | 120, 134, 280, 295, 302 |
| Tail Width | tail_width | number (mm) | Width at the widest point of the tail | 115, 128, 270, 285, 295 |
| Effective Edge | effective_edge | number (mm) | Length of the metal edge that contacts the snow surface | 1140, 1200, 1260 |
| Sidecut Radius | sidecut_radius | text (m) | Turn radius determined by the side profile shape | 7.8, 11.3, 15, 17.5, 22 |
| Profile/Camber | profilecamber | text | Longitudinal flex profile of the board or ski | Camber, Rocker, Flat, Hybrid Camber-Rocker, Reverse Camber, All-Mountain Rocker |
| Flex Rating | flex_rating | text | Stiffness rating on the manufacturer scale (typically 1-10) | 3 (Soft), 5 (Medium), 6 (Medium-Stiff), 8 (Stiff), 10 (Very Stiff) |
| Shape | shape | text | Directional profile of the board or ski | Twin, Directional Twin, Directional, Tapered Directional, Asymmetric |
| Construction | construction | text | Layup method for the board or ski | Sandwich, Cap, Hybrid, Full Wrap, Fiberglass Layup, Carbon Wrap |
| Fin Setup | fin_setup | text | Fin configuration for surfboards, wakeboards, or SUPs | Thruster (3-Fin), Quad (4-Fin), 2+1, Single Fin, Twin Fin, 5-Fin Box, Removable |
| Tail Shape | tail_shape | text | Shape of the tail end for surfboards | Squash, Round, Swallow, Pin, Diamond, Square |
| Volume (Surfboard) | volume_surfboard | number (L) | Total volume of a surfboard in litres affecting buoyancy | 22.5, 28.0, 33.5, 42.0, 65.0 |
| Thickness (Surfboard) | thickness_surfboard | text (inches) | Maximum thickness of a surfboard | 2 1/4, 2 3/8, 2 1/2, 2 5/8, 3 |
| Stance Width | stance_width | text (mm) | Recommended distance between bindings | 530, 560, 580 |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 36 attributes from 4 companies plus industry standards (ISO 5355 ski boot sole, CE EN 1077 helmet, EN 13319 dive instruments) | [Burton](https://www.burton.com/), [Evo](https://www.evo.com/), [HO Sports](https://www.hosports.com/), [Channel Islands Surfboards](https://cisurfboards.com/) |
