# Platform: Magento 2

## Detection
- Meta/JS: `Magento_Ui/js/core/app`, `Magento_PageBuilder`, `Magento_PageCache` in require config
- Path pattern: `/static/version{timestamp}/frontend/{theme}/{package}/{locale}/`
- Checkout URLs: `/checkout/`, `/checkout/cart/`
- Body classes: `catalog-product-view`, `catalog-category-view`, `checkout-index-index`

## JSON-LD Patterns
- Product pages contain `<script type="application/ld+json">` with `@type: Product`
- Standard fields: `name`, `description`, `image`, `offers.price`, `offers.priceCurrency`, `offers.availability`
- BreadcrumbList schema may also be present
- **Pitfall:** Some sites embed third-party JSON-LD blocks — always filter by matching `offers.url` hostname to the target domain

## CSS Selectors
| Element | Selector | Notes |
|---------|----------|-------|
| Product name | `h1` | First H1 on product page; theme-specific classes vary |
| Price | `[data-role="priceBox"] .price` or `span.price` | Standard Magento price box; may need theme-specific adjustment |
| SKU | `.product.attribute.sku .value` | Standard Magento; custom themes may use different markup |
| Spec table | `#product-attribute-specs-table` or `table.data.table.additional-attributes` | In "Additional Information" or "Specifications" tab |
| Spec row label | `th` (rowheader) | Within spec table tbody tr |
| Spec row value | `td` (cell) | Within spec table tbody tr |
| Breadcrumb | `.breadcrumbs li a` | Standard Magento breadcrumb |

## Pagination
- URL pattern: `?p={page_number}` for category listing pages
- Products per page: Typically 12 (configurable via `?product_list_limit=N`)
- Next page detection: "Next" link in pagination or "Items X-Y of Z" text
- Show all: `?product_list_limit=all` parameter available on some installations

## Sitemap
- Default location: `/media/sitemap/sitemap.xml` (referenced in robots.txt)
- Product URLs typically have priority 1.0, category URLs have priority 0.5
- Product URL format varies by theme/config — often descriptive slug with SKU suffix

## Common Pitfalls
| Issue | Resolution |
|-------|-----------|
| Third-party JSON-LD injected on product pages | Filter `@type: Product` blocks by matching `offers.url` hostname to target domain |
| Category pages at non-leaf levels return empty | Only leaf categories contain products; traverse to leaf level |
| Custom themes override standard selectors | Use JSON-LD as primary data source; fall back to HTML only when needed |
| Crawl delay in robots.txt | Respect the specified delay (commonly 10s) |
| Spec table selector varies by theme | Standard `#product-attribute-specs-table` absent on some themes — try `table tr th`/`td` first, then `dl dt`/`dl dd` pairs inside Specifications tab |
| JSON-LD missing sku field | Harlow theme JSON-LD has name/price/availability only — get SKU from "Product Code" page text or URL suffix |
| VAT toggle changes displayed price | JSON-LD price is fixed (typically inc VAT); note which VAT state is used |
| Per-unit pricing (metre, pack, each) | Unit of sale not in JSON-LD; extract from page text if needed |
| Sparse spec tables | Some Magento sites only include dimensional attributes in spec tables. Core classification attributes (wood type, treatment, material) may need to be extracted from product names using pattern matching |
| Product listing CSS varies by theme | Standard `.product-item-link` may not work. Also try `.products-grid a`, `.product-items a`, `ol.products a` |
| Breadcrumb links contain category paths | `.breadcrumbs li a[href]` links under `/shop/` can be used to infer product category when the referrer category URL is unavailable (e.g., probe mode) |

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| Harlow Bros | harlowbros | 2026-03-18 | Custom "Harlow" theme. JSON-LD present (name, price, availability only — no sku). Spec table uses standard `<table>` with `<th>`/`<td>` in Specifications tab. SKU as "Product Code" text label, also in URL suffix. Product pages at domain root `/{slug}`; category pages at `/shop/{path}`. Product links via `.products-grid a`. Sparse spec tables — core attributes enriched from product names. 8 subcategories across 10 top-level departments. |
