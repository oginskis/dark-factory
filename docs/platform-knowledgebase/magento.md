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
| VAT toggle changes displayed price | JSON-LD price is fixed (typically inc VAT); note which VAT state is used |
| Per-unit pricing (metre, pack, each) | Unit of sale not in JSON-LD; extract from page text if needed |

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| Harlow Bros | harlowbros | 2026-03-17 | Custom "Harlow" theme; JSON-LD verified; breadcrumb in `div.breadcrumbs` (not ol/ul); spec table in Specifications tab; SKU as "Product Code" `<strong>` label; sitemap-based discovery with priority 1.0 filter |
