# Platform: Shopify

## JSON-LD Patterns
- Product pages have `<script type="application/ld+json">` with `@type: Product`
- Standard Shopify JSON-LD includes name, sku, brand, price, availability, description, image
- Brand is an object with `@type: Brand` and `name` field

## Shopify JSON API
- **Products endpoint:** `/products.json?limit=250&page={N}` — returns up to 250 products per page
- **Single product:** `/products/{handle}.json` — returns full product data
- No authentication required for public storefronts
- Response contains: `id`, `title`, `handle`, `body_html`, `vendor`, `product_type`, `tags`, `variants`, `images`, `options`
- `variants` array includes: `id`, `title`, `sku`, `price`, `available`, `option1/option2/option3`
- `tags` is a comma-separated string or array depending on endpoint — always normalize to array

## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on collection pages | `.product-card a` | Varies by theme: also try `.product-item a`, `.grid-product a` |
| Pagination next | `.pagination a[rel="next"]` | Also try `a.next` |
| Breadcrumb | `.breadcrumb` | Varies: also `.breadcrumbs`, `nav[aria-label="Breadcrumb"]` |

## Pagination
- URL pattern: `/collections/{name}?page={N}` (HTML) or `/products.json?limit=250&page={N}` (JSON API)
- Products per page: 16-24 (HTML collections), 250 (JSON API)
- Next page detection: `.pagination a[rel="next"]` (HTML) or empty `products` array (JSON API)
- Product sitemap: `sitemap_products_1.xml` — lists all product URLs

## Common Pitfalls
- `product_type` field is often empty — use `tags` for categorization instead
- `tags` may be a comma-separated string (HTML) or array (JSON API) — normalize
- Shopify product URLs use `handle` slugs — append `.json` to get individual product JSON
- Products in the sitemap may include unpublished/draft items not visible on the storefront
- `body_html` contains raw HTML — strip tags before text analysis
- Variable products may have many variants — use the first available variant for the primary SKU/price
- Crawl delays in robots.txt for specific bots (AhrefsBot: 10s, Pinterest: 1s)

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| EV OneStop | evonestop | 2026-03-15 | ~123 products (sitemap), JSON API works, collection JSON endpoints work for category mapping, product_type empty, tags used for categorization, body_html has rich specs (kW, IP/IK ratings, OCPP, connectivity) |
| Evolution Power Tools | evolutionpowertools | 2026-03-19 | ~390 products (sitemap), JSON API works via collection endpoints, /products.json returns only 6 (use /collections/{handle}/products.json instead), product_type populated (Mitre Saw, Chop Saw, etc.), body_html has rich spec tables, Empire theme v9.0.1, hCaptcha present but non-blocking, UK store (shop.evolutionpowertools.com) — US store geo-blocked |
| Youngstown Glove Company | ytgloves | 2026-03-20 | 79 products (sitemap), /products.json returns only 25 (use sitemap + /products/{handle}.json), product_type uses internal labels ("YT Stock", "YT Promo") not product categories, tags useful for categorization (Arc Rated, Cut Resistant, etc.), body_html has specs as free-text bullet lists (not tables), vendor is factory name not brand, Turbo Seoul theme, 429 rate limiting with bare httpx — add User-Agent header, handles with ® need URL-encoding |
| Pyramex Safety Products | pyramex | 2026-03-19 | 467 products (sitemap), /products.json returns only ~10 (use sitemap + /products/{handle}.json), product_type well-populated with hierarchical values ("Eyewear > Sealed", "Gloves > Dipped"), body_html has free-text specs (safety ratings, NRR, materials), all prices $0.00 (B2B), 226 collections (many marketing), options array has variant axes (Body Color, Lens Color, Lens Treatment), Impulse theme v6.1.0, 429 rate limiting with bare httpx, handles with ® may 404 on .json endpoint |
| 360 Cookware | 360cookware | 2026-03-20 | 72 products extracted via sitemap + /products/{handle}.json, product_type flat labels ("Saucepan", "Fry Pan", "360 Bakeware", "Sets", "Slow Cooker"), body_html specs are BR-separated (not HTML tables) under "Product Features:" heading — standalone feature lines (no colon) need special parsing, T-316/T-304 material grades, real prices in USD ($95-$2845), vendor is "Americraft Cookware" not brand, Cloudflare challenge triggers 429 after rapid requests — space requests to avoid cf-mitigated:challenge, Dawn theme v10.0.0 |
| Heritage Steel | heritagesteel | 2026-03-20 | 169 products in sitemap (includes third-party: Earlywood, Algae Cooking Club), /products.json returns only 27 (use sitemap + /products/{handle}.json), product_type flat labels ("Cookware", "Cutlery", "Bakeware"), body_html is brief prose with no structured specs, attributes inferred from title (sizes), product_type, vendor, tags, weight, multi-vendor store (Heritage Steel, Hammer Stahl, HS Kitchen, Earlywood, Algae Cooking Club), hCaptcha present but non-blocking, Impulse theme v6.0.0, real prices in USD ($18-$1600+) |
| Portland Pet Food Company | portlandpetfoodcompany | 2026-03-20 | 21 products, /products.json returns all on one page, product_type well-populated ("Dog Food", "Dog Treat", "Cat Food", "Gear", "Carbon Offset"), body_html is prose (no spec tables), attributes from variant fields (weight, weight_unit, sku) and tags, non-food items (Gear, Carbon Offset) need filtering, Cloudflare cf-mitigated:challenge blocks bare httpx — use curl_cffi with Chrome TLS impersonation, Mode theme v4.0.1 |
| The Honest Kitchen | thehonestkitchen | 2026-03-20 | 127 products (sitemap), /products.json returns only ~24 (use sitemap + /products/{handle}.json), product_type well-populated ("Dry Dog Food", "Dehydrated Dog Food", "Dog Treat", "Câté Wet Cat Food", "Digestive Supplement"), body_html is marketing prose (no spec tables), tags contain rich categorization (protein source, life stage, grain status, recipe:: prefix for protein), ~8 merchandise items need filtering, bundles present, Locksmith access control (currently unlocked), 429 rate limiting on collection HTML pages, Cloudflare active but JSON API works with proper spacing |
| Smithey Ironware | smithey | 2026-03-20 | 50 products, /products.json?limit=250 returns all on one page, product_type populated for cookware ("Cast Iron", "Carbon Steel") but blank for sets/bundles, body_html has dimensions as colon-separated text (not tables), specs include diameter/depth/weight, Shoplift A/B testing modifies rendered prices (use JSON API for accurate prices), 429 rate limiting on bare httpx, 33 collections (many marketing/contextual duplicates) |
| Open Farm | openfarmpet | 2026-03-20 | 493 products (sitemap), /products.json returns only 32 (use sitemap + /products/{handle}.json), product_type minimal ("Dog Food", "Cat Food"), tags use structured _key::value format extensively (_protein, _lifestage, _productType, _grains, _sensitivity, _format, _goals, category::, store_category::), body_html is narrative prose (no spec tables), variants are size options (weight/count), GTIN/barcode available, 489 collections (mostly marketing), Cloudflare with captcha on HTML pages but JSON API unaffected, vendor alternates "Open Farm"/"Open Farm Pet" |
| Triton Tools | tritontools | 2026-03-20 | 40 products, /products.json?limit=250 returns all on one page (includes regional duplicates tagged AU/KR/JA/ZA with $0.00 prices — filter by empty tags for UK products), product_type contains model numbers not categories ("TRA001", "TWX7PS001"), body_html has specs as colon-separated list items under "Technical Specification" heading (not HTML tables), PageFly page builder renders product pages, 429 rate limiting with bare httpx — add User-Agent header, Warehouse theme v6.3.0, hCaptcha present but non-blocking, Langify multilingual (EN/DE/FR/IT/ES/NL/PL/JA), owned by Timbecon Pty Ltd |
