# Platform: WooCommerce

## JSON-LD Patterns
- Product pages usually have `<script type="application/ld+json">` with `@type: Product`, but some custom WooCommerce themes omit the Product schema entirely — only WebPage, BreadcrumbList, and Organization types are present. In these cases, extract product data from HTML instead.
- The `offers` field is always a **list**, even for single-offer products — never a bare dict
- Variable products use `AggregateOffer` inside the list, with `lowPrice` and `highPrice`
- Single-price products and quantity-tiered products use `Offer` objects inside the list
- `Offer` objects may use `priceSpecification` (a list of `UnitPriceSpecification`) instead of a direct `price` field — always check `priceSpecification[0].price` as a fallback
- `priceCurrency` may be on the `AggregateOffer`/`Offer` directly, or nested inside `priceSpecification[0].priceCurrency`
- `sku` can be numeric (integer) in the JSON-LD — always convert to string

## CSS Selectors
- **Product links on category pages:** `ul.products li.product a` — filter for `href` containing `/product/`
- **Pagination next page:** `a.next.page-numbers`
- **Breadcrumb:** Varies by theme:
  - Kadence theme: `.kadence-breadcrumbs`
  - Default WooCommerce: `nav.woocommerce-breadcrumb`
  - Yoast SEO: `.yoast-breadcrumb`
  - Custom themes with `nav[aria-label='breadcrumb']`
  - Always check all selectors, falling back in order
- **Product short description:** `.woocommerce-product-details__short-description`
- **Product full description:** `.woocommerce-Tabs-panel--description`

## Pagination
- URL pattern: `/product-category/{category}/page/{N}/`
- Products per page: typically 24 (configurable by theme)
- Next page link uses CSS class `a.next.page-numbers`
- When no next page exists, the element is absent (no disabled state)

## Common Pitfalls
- `offers` being a list instead of a dict caused `AttributeError: 'list' object has no attribute 'get'` — always handle list-typed offers with recursion or iteration
- `priceSpecification` nesting: some Offer objects have no direct `price` field, only `priceSpecification` — must check both paths
- Breadcrumb selector varies by WordPress theme — the default `.woocommerce-breadcrumb` does not work on Kadence-themed sites
- Wholesale/bulk categories often duplicate products from other categories — skip or deduplicate by URL
- Variable products show price ranges — use `lowPrice` as the base price for the product record
- Some WooCommerce sites display prices using `.woocommerce-Price-amount` inside the product page AND inside the header cart widget. Always scope price extraction to `main .woocommerce-Price-amount` to avoid matching the cart's €0.00 total
- Custom themes may use `<dt>`/`<dd>` pairs for product attributes alongside stock/availability data — department-level stock also uses dt/dd, so filter by label to avoid capturing stock info as product attributes
- Estonian/multilingual WooCommerce uses `/toode/` instead of `/product/` for product URLs, `/tootekategooria/` instead of `/product-category/` for category URLs

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| Topwood Timber | topwoodtimber | 2026-03-15 | Kadence theme, list-wrapped offers with priceSpecification, ~120 products |
| Electric Vehicle Equipment | electricvehicleequipment | 2026-03-15 | Standard WooCommerce, JSON-LD with @graph wrapper, AggregateOffer for variable products, 5 products |
| EVCharge | evcharge | 2026-03-15 | Woodmart theme with AJAX shop, direct JSON-LD Product (no @graph wrapper), list-wrapped offers, GTIN field present, multilingual (LV/EN/RU), ~70 products |
| Puumarket | puumarket | 2026-03-16 | Custom theme, NO Product JSON-LD (only WebPage/BreadcrumbList), dt/dd product attributes, multilingual (ET/EN/RU), sitemap-based discovery (8 product sitemaps), ~5000 products, no anti-bot |
