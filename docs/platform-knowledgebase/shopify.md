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
- **Product links on collection pages:** `.product-card a`, `.product-item a` — varies by theme
- **Pagination:** `.pagination a[rel="next"]` or `a.next`
- **Breadcrumb:** Varies by theme — check `.breadcrumb`, `.breadcrumbs`, `nav[aria-label="Breadcrumb"]`

## Pagination
- JSON API: `?limit=250&page={N}` — keep incrementing page until empty `products` array
- HTML collection pages: `/collections/{name}?page={N}`, typically 16-24 products per page
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
| EV OneStop | evonestop | 2026-03-15 | 112 products, JSON API works, tags used for categorization, product_type empty |
