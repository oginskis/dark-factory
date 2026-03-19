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
| Youngstown Glove Company | ytgloves | 2026-03-19 | ~30 products, /products.json returns full catalog in one page, product_type uses internal labels ("YT Stock", "YT Promo") not product categories, tags useful for categorization (Arc Rated, Cut Resistant, etc.), body_html has specs as free-text (not tables), vendor is factory name not brand, Turbo Seoul theme, 429 rate limiting with bare httpx — add User-Agent header |
| Pyramex Safety Products | pyramex | 2026-03-19 | 467 products (sitemap), /products.json returns only ~10 (use sitemap + /products/{handle}.json), product_type well-populated with hierarchical values ("Eyewear > Sealed", "Gloves > Dipped"), body_html has free-text specs (safety ratings, NRR, materials), all prices $0.00 (B2B), 226 collections (many marketing), options array has variant axes (Body Color, Lens Color, Lens Treatment), Impulse theme v6.1.0, 429 rate limiting with bare httpx, handles with ® may 404 on .json endpoint |
| 360 Cookware | 360cookware | 2026-03-19 | ~50 products (sitemap has 187 URLs but many are non-products), /products.json returns only ~10 (use sitemap + /products/{handle}.json), product_type flat labels ("Saucepan", "Fry Pan", "360 Bakeware"), tags have structured prefixes (Category_, Measure_, Size_), body_html has colon-separated specs (dimensions, material grade, gauge, oven safe temp), real prices in USD ($100-$600), vendor is "Americraft Cookware" not brand, Dawn theme v10.0.0, hCaptcha non-blocking |
