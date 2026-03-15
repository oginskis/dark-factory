# Platform Knowledgebase: PrestaShop

## JSON-LD Patterns

No JSON-LD Product schema observed on product pages (PATA Timber). Product data is embedded in HTML only. Google Tag Manager dataLayer contains product info (`item_id`, `item_name`, `price`, `item_category2`, `item_category3`) but is not accessible via simple HTTP scraping.

## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product links on listing pages | `a[href*="/p/"]` matching `/p/\d+-` pattern | Product URLs use `/p/{id}-{slug}` format |
| Product price | `.price` (first occurrence) | Multiple `.price` elements may exist — use first for primary price |
| Product name | `h1` | Standard heading |
| Breadcrumb | `.pata-breadcrumbs a` | Site-specific class; standard PrestaShop may use `nav.breadcrumb` or `ol.breadcrumb` |
| Product attributes | `table tr` with exactly 2 `td` cells | Label in first cell, value in second. NOT `dl/dt/dd` — PATA uses 2-column table rows in tab panels |
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
| No sitemap | No sitemap.xml available; category tree traversal is the only discovery method |

## Sites Using This Platform

| Company | Slug | Date | Notes |
|---------|------|------|-------|
| PATA Timber | pata | 2026-03-16 | Latvian timber retailer. No JSON-LD, no sitemap. Custom breadcrumb class `.pata-breadcrumbs`. All labels in Latvian. Product attributes in 2-column table rows (not dl/dt/dd). Category numeric IDs may differ from navigation links — verify via BFS discovery. Tabs: Informācija, Detalizēta informācija, Tehniskais apraksts, Kvalitātes apraksts. Specs in Detalizēta informācija tab. |
