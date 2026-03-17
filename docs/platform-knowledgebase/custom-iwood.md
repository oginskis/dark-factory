# Platform: iWood (Custom ASP.NET)

Site-specific knowledgebase for iwood.co.uk. Custom ASP.NET e-commerce platform — not a standard CMS.

## JSON-LD Patterns

- Product pages include `@type: Product` with `name`, `sku`, `material`, `category`, `brand`, and `offers` array
- Each offer: `sku` (encodes productType-speciesId-gradeId-dimensions-finish), `price` (GBP ex-VAT), `priceCurrency`, `availability`, `description` (human-readable grade/profile/dimension string)
- Some offers include `priceSpecification` with `unitCode` (MTK for per-m2 pricing, MTR for per-metre) and `valueAddedTaxIncluded: false`
- Beams page uses `@graph` format with multiple schemas: `ItemList` (grades), `FAQPage`, `Product`, `BreadcrumbList`
- BreadcrumbList present on ALL pages (including those without Product schema)
- **JSON-LD coverage:** Cladding (all profiles/species), beams, cedar slats, timber packs have full Product schema with offers
- **No JSON-LD Product schema:** Skirting, architrave, decking, oak sleepers, PAR, cut-to-size — prices are JavaScript-calculator-only or example-pricing HTML tables

## CSS Selectors

| Element | Selector | Notes |
|---------|----------|-------|
| Product name | `h1` | Main heading on product page |
| Breadcrumb | JSON-LD BreadcrumbList | Always present; reliable on all pages |
| Price (fallback) | `.price, [class*="price"]` | For pages without JSON-LD; may show "From £X.XX" only |

## URL Patterns

| Product Type | URL Pattern |
|---|---|
| Beams | `/beams/{speciesId}/{speciesSlug}/` |
| Planed All Round | `/planed-all-round/{speciesId}/{speciesSlug}/` |
| Cut to Size | `/cut-to-size/{speciesId}/{speciesSlug}/` |
| Skirting | `/skirting/{speciesId}/{speciesSlug}/` |
| Architrave | `/architrave/{speciesId}/{speciesSlug}/` |
| External Cladding | `/products/external-timber-cladding/{profileSlug}/{speciesSlug}/` |
| Decking | `/products/decking/{typeSlug}/` |
| Cladding Accessories | `/cladding-accessories/{speciesId}/{speciesSlug}/` |
| Timber Packs | `/packs/{speciesId}/{speciesSlug}/` |

Species IDs: European Oak=32, British Larch=18, Cedar British WR=44, Douglas Fir British=46, Whitewood/Spruce British=43, English Oak=45

## Pagination

- No pagination — each species × product-type combination = one page
- All SKU variants (dimension × grade × finish) are in the single `offers` array

## Product Discovery

- Sitemap at `/sitemap.xml` lists all ~119 product URLs; recommended as primary discovery method
- Probe reports sitemap `found: false` due to XML parsing; manual fetch confirms it works correctly

## Common Pitfalls

| Issue | Resolution |
|-------|-----------|
| JSON-LD missing on some product types | Skirting, architrave, decking, sleepers have no Product schema — prices are JavaScript-calculator-only |
| SKU encodes dimensions | `offers[].sku` segments: productTypeId-speciesId-gradeId-thickness-width-length-finish (beams) or categoryId-profileTypeId-speciesId-gradeId-profileCodeId (cladding) |
| Prices ex-VAT | All `offers.price` values exclude UK VAT (20%) |

## Sites Using This Platform

| Company | Slug | Date | Notes |
|---------|------|------|-------|
| iWood Timber Ltd | iwood | 2026-03-18 | UK wholesale timber merchant. Custom ASP.NET. JSON-LD on beams, PAR, cut-to-size, cladding. No JSON-LD on skirting/architrave/decking/sleepers (JS calculator). HTML sitemap at /sitemap/ (~150 product URLs). Prices ex-VAT. No pagination. |
