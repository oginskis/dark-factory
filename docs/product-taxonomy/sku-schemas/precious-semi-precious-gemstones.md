# SKU Schema: Precious & Semi-Precious Gemstones

**Last updated:** 2026-03-15
**Parent category:** Minerals, Ores & Raw Materials

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | Dealer or supplier product identifier | GEM-SAP-OV-215, DIA-RND-100-DVS1, RBY-CSH-350 |
| Product Name | text | Full product name including stone type, shape, weight, and key quality descriptors | Natural Blue Sapphire Oval 2.15 ct, GIA Certified Round Brilliant Diamond 1.00 ct D/VS1, Cushion Ruby 3.50 ct Pigeon Blood |
| URL | text | Direct link to the product page | https://example.com/gemstones/sapphire-oval-215ct |
| Price | number | Numeric price per stone or per carat, excluding currency symbol | 150.00, 2500.00, 18000.00 |
| Currency | text | ISO 4217 currency code | USD, EUR, GBP, JPY, CHF |
| Dealer/Supplier | text | Gemstone dealer or supplier name | Stuller, Gandhara Gems, Stachura Wholesale, GemsVisor, Leibish |
| Stone Type | text | Gemological species or variety name | Diamond, Ruby, Sapphire, Emerald, Alexandrite, Tourmaline, Spinel, Garnet, Opal, Tanzanite, Aquamarine, Topaz |
| Stone Category | enum | Whether the stone is classified as precious or semi-precious | Precious, Semi-Precious |
| Natural vs Lab | enum | Whether the stone is natural, laboratory-grown, or simulant | Natural, Lab-Grown, Simulant |
| Carat Weight | number (ct) | Weight of the gemstone in carats (1 carat = 200 mg) | 0.25, 1.00, 2.15, 5.03, 12.50 |
| Shape | text | Cut shape or outline of the gemstone | Round, Oval, Cushion, Emerald, Pear, Marquise, Princess, Heart, Trillion, Cabochon, Rough |
| Cut Quality | enum | Overall quality rating of the cut proportions and finish | Excellent, Very Good, Good, Fair, Poor |
| Length | number (mm) | Maximum length dimension of the stone | 4.0, 6.5, 8.2, 10.0, 14.5 |
| Width | number (mm) | Maximum width dimension of the stone | 3.5, 5.0, 6.8, 8.0, 11.0 |
| Depth | number (mm) | Height/depth dimension of the stone from table to culet | 2.0, 3.5, 4.8, 6.2, 8.0 |
| Color Grade | text | Color assessment following GIA or industry-specific grading scales | D, E, F, G, H, Vivid Blue, Pigeon Blood Red, Medium Green, Fancy Yellow, Padparadscha |
| Hue | text | Dominant spectral color of the gemstone | Red, Blue, Green, Yellow, Orange, Pink, Purple, Colorless |
| Tone | enum | Lightness or darkness of the color | Very Light, Light, Medium Light, Medium, Medium Dark, Dark, Very Dark |
| Saturation | enum | Intensity or vividness of the color | Grayish, Slightly Grayish, Moderately Strong, Strong, Vivid |
| Clarity Grade | text | Clarity assessment per GIA or equivalent grading system | FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, Eye Clean, Moderately Included, Heavily Included |
| Transparency | enum | Degree to which light passes through the stone | Transparent, Semi-Transparent, Translucent, Semi-Translucent, Opaque |
| Treatment | text | Enhancement or treatment applied to the gemstone, disclosed per AGTA codes | None (No Heat), Heat Only (H), Fracture Filled (F), Oiled (O), Irradiated (R), Diffusion (D), Coated (C) |
| Geographic Origin | text | Country or region of mining origin | Myanmar (Burma), Sri Lanka (Ceylon), Colombia, Zambia, Madagascar, Tanzania, Kashmir, Montana USA |
| Certification Lab | text | Gemological laboratory that issued the grading report | GIA, GRS, AGTA, AGL, Gubelin, SSEF, IGI |
| Certificate Number | text | Unique identification number of the grading report | 6214567890, GRS2024-012345 |
| Fluorescence | enum | Ultraviolet fluorescence intensity | None, Faint, Medium, Strong, Very Strong |
| Optical Phenomena | text | Special optical effects exhibited by the stone | Star (Asterism), Cats Eye (Chatoyancy), Color Change, Adularescence, Play of Color |
| Refractive Index | text | Measured refractive index range for the stone species | 1.544-1.553, 1.762-1.770, 2.417, 1.577-1.583 |
| Specific Gravity | number | Measured density relative to water | 2.72, 3.52, 4.00, 4.03, 3.10 |
| Mohs Hardness | number | Hardness on the Mohs scale for the species | 5.5, 7.0, 8.0, 9.0, 10.0 |
| Country of Cutting | text | Country where the stone was cut and polished | India, Thailand, Sri Lanka, Germany, USA, China |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Initial schema -- 31 attributes from 4 companies plus gemological standards (GIA 4Cs, AGTA treatment codes, ISO gemstone nomenclature) | [Stuller](https://www.stuller.com/browse/gemstones), [Gandhara Gems](https://www.gandharagems.com/collections/loose-gemstones), [IGS Gem Society](https://www.gemsociety.org/article/gem-pricing-guide-sample/), [GIA](https://4cs.gia.edu/en-us/types-gia-reports/) |
