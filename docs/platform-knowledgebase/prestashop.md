# Platform Knowledgebase: PrestaShop

## JSON-LD Patterns

JSON-LD availability varies by site. UK Timber (PrestaShop 9.0.2) has full Product schema with `name`, `sku`, `mpn`, `brand`, `offers` (price, currency, availability), and BreadcrumbList. PATA Timber (older version) has no JSON-LD Product schema — product data is HTML-only. Always check for JSON-LD first; fall back to CSS selectors if absent.

## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on listing pages | `a[href$=".html"]` inside `article` elements | URL patterns vary: PATA uses `/p/{id}-{slug}`, UK Timber uses `/{category-slug}/{id}-{slug}.html`. Match by `.html` suffix within article containers. |
| Product price | `.price` (first occurrence) | Multiple `.price` elements may exist — use first for primary price |
| Product name | `h1` | Standard heading |
| Breadcrumb | `nav.breadcrumb` or JSON-LD BreadcrumbList | PATA uses custom `.pata-breadcrumbs`; UK Timber uses `nav.breadcrumb.hidden-sm-down`. Prefer JSON-LD BreadcrumbList when available. |
| Product attributes | `.product-variants .form-group` or `table tr` with 2 `td` cells | Varies by site: UK Timber uses variant selectors (select/radio in `.product-variants`); PATA uses 2-column table rows in tab panels |
| Subcategory links | `a[href]` matching `/{parent-id}-{parent-slug}/{child-id}-{child-slug}` pattern | Numeric ID prefix on all category URLs |

## Pagination

- URL pattern: `?page={n}` query parameter
- Products per page: 48 (default)
- Next page detection: look for `a[href]` containing `page={n+1}`
- Top-level categories are landing pages without products — must navigate to leaf subcategories

## Common Pitfalls

| Issue | Resolution |
|-------|-----------|
| Price shows 0.00 | Some product pages show 0.00 in variant/placeholder price elements. Use the first `.price` element, not `[itemprop='price']` which may match a hidden zero value |
| Top-level category returns no products | PrestaShop top-level categories are often landing/index pages. Must traverse to leaf subcategories to find products |
| 404 on some product URLs | Discontinued products return error pages ("Kļūda"). Skip gracefully |
| Latvian attribute labels | Product specs use Latvian: Norāde=SKU, Biezums=thickness, Platums=width, Garums=length, Suga=species, Mitrums=moisture, Kvalitāte=grade |
| No sitemap | No sitemap.xml available on either site; use category tree traversal or productlist module |
| Variant selectors as attributes | UK Timber uses PrestaShop variant selectors (`.product-variants .form-group` with select/radio) instead of spec tables. Label in `.control-label`, options in `select > option` or `input[type="radio"]` |
| Productlist module | Some PrestaShop sites expose `/module/productlist/productlist{n}` — a flat paginated product list useful for discovery when sitemaps are absent |

## Sites Using This Platform

| Company | Slug | Date | Notes |
|---------|------|------|-------|
| PATA Timber | pata | 2026-03-16 | Latvian timber retailer. No JSON-LD, no sitemap. Custom breadcrumb class `.pata-breadcrumbs`. All labels in Latvian. Product attributes in 2-column table rows (not dl/dt/dd). Category numeric IDs may differ from navigation links — verify via BFS discovery. Tabs: Informācija, Detalizēta informācija, Tehniskais apraksts, Kvalitātes apraksts. Specs in Detalizēta informācija tab. |
| UK Timber | uk-timber | 2026-03-18 | UK timber merchant. PrestaShop 9.0.2. Full JSON-LD Product + BreadcrumbList. Product URLs: `/{category-slug}/{id}-{slug}.html`; variants use `/{category-slug}/{id}-{combinationId}-{slug}.html`. Attributes via variant selectors (`.product-variants .form-group`), not spec tables. Productlist module at `/module/productlist/productlist{1-5}` (~250-300 products, 5 pages). Prices ex-VAT. No sitemap. Standard `nav.breadcrumb` class. Category URLs: `/{id}-{category-slug}`. probe returns `recipe_match: untested` (no sitemap URLs for probe to test) — manual verification confirmed JSON-LD and variant selectors work. |
