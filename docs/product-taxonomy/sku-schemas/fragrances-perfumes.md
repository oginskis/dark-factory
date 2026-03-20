# SKU Schema: Fragrances & Perfumes

**Last updated:** 2026-03-15
**Parent category:** Consumer Goods (Personal Care & Household)
**Taxonomy ID:** `consumer.fragrances_perfumes`


## Core Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| SKU | sku | text | — | yes | Retailer or manufacturer product identifier | Y0785220, 2525854, 3348901368254 |
| Product Name | product_name | text | — | yes | Full product name including brand, fragrance name, concentration, and size | Dior Sauvage Eau de Parfum 100ml, Chanel No. 5 Parfum 50ml |
| URL | url | text | — | yes | Direct link to the product page | https://www.dior.com/en_us/beauty/products/sauvage-eau-de-parfum-Y0785220.html |
| Price | price | number | — | yes | Numeric unit price excluding currency symbol | 105.00, 165.00, 38.00 |
| Currency | currency | text | — | yes | ISO 4217 currency code | USD, EUR, GBP, JPY |
| Price Includes VAT | price_includes_vat | boolean | — | — | Whether the listed price includes VAT or sales tax | true, false |
| Bottle Type | bottle_type | enum | — | — | Form factor of the fragrance container | Spray, Splash, Rollerball, Travel Spray, Decant |
| INCI Ingredients | inci_ingredients | text | — | — | Full INCI ingredient list from packaging | Alcohol, Parfum, Aqua, Limonene, Linalool, Coumarin, Citronellol |
| Packaging Material | packaging_material | text | — | — | Primary packaging material for the bottle | Glass, Glass with Metal Cap, Crystal |
| Country of Origin | country_of_origin | text | — | — | Country where the fragrance is manufactured | France, Italy, USA, Spain, UK |

## Extended Attributes

| Attribute | Key | Data Type | Unit | Mandatory | Description | Example Values |
|--------|--------|--------|--------|-----------|--------|--------|
| Fragrance Name | fragrance_name | text | — | — | The named fragrance within the brand | Sauvage, No. 5, Black Orchid, Bleu de Chanel, Light Blue |
| Concentration | concentration | enum | — | — | Fragrance concentration type indicating oil percentage | Eau de Cologne, Eau de Toilette, Eau de Parfum, Parfum, Extrait de Parfum, Elixir |
| Volume | volume | number | ml | — | Volume of the bottle | 30, 50, 75, 100, 150, 200 |
| Volume (oz) | volume_oz | number | oz | — | Volume in fluid ounces as commonly displayed in US retail | 1.0, 1.7, 2.5, 3.4, 5.0, 6.8 |
| Target Gender | target_gender | enum | — | — | Intended consumer gender | Men, Women, Unisex |
| Fragrance Family | fragrance_family | enum | — | — | Primary olfactory classification | Woody, Oriental, Floral, Fresh, Citrus, Aromatic, Gourmand, Chypre, Fougere, Aquatic |
| Top Notes | top_notes | text (list) | — | — | Initial scent notes perceived in the first minutes | Bergamot, Pepper, Lemon, Grapefruit, Pink Pepper, Mandarin |
| Heart Notes | heart_notes | text (list) | — | — | Middle notes that emerge after the top notes fade | Lavender, Geranium, Rose, Jasmine, Iris, Cinnamon, Star Anise |
| Base Notes | base_notes | text (list) | — | — | Long-lasting notes that form the foundation of the fragrance | Ambroxan, Vanilla, Sandalwood, Musk, Cedarwood, Tonka Bean, Patchouli, Vetiver |
| Perfumer | perfumer | text | — | — | Name of the perfumer or nose who created the fragrance | Francois Demachy, Jacques Polge, Alberto Morillas |
| Launch Year | launch_year | number | — | — | Year the fragrance was first released | 2015, 1921, 2006, 2018 |
| Refillable | refillable | enum | — | — | Whether the bottle supports refilling | Yes, No |
| Limited Edition | limited_edition | enum | — | — | Whether the product is a limited edition release | Yes, No |
| Gift Set | gift_set | enum | — | — | Whether the product is sold as part of a gift set | Yes, No |
| Set Contents | set_contents | text (list) | — | — | Items included in a gift set | EDP 100ml, Shower Gel 50ml, Travel Spray 10ml, Body Lotion 75ml |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| 2026-03-15 | Migrated to core/extended format | Migration script |
| 2026-03-15 | Initial schema — 30 attributes from 4 companies plus IFRA and fragrance classification standards | [Dior Sauvage EDP](https://www.dior.com/en_us/beauty/products/sauvage-eau-de-parfum-Y0785220.html), [Fragrantica Dior Sauvage](https://www.fragrantica.com/perfume/Dior/Sauvage-31861.html), [Ulta Beauty Dior Sauvage](https://www.ulta.com/p/sauvage-eau-de-parfum-xlsImpprod17941005), [The Perfume Shop Concentration Guide](https://www.theperfumeshop.com/blog/expertise/whats-the-difference-between-parfum-and-eau-de-parfum/) |
