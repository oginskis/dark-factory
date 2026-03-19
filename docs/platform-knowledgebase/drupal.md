# Platform: Drupal

## JSON-LD Patterns
No JSON-LD product schemas observed. Drupal sites typically do not include schema.org Product markup unless a dedicated module is installed.

## CSS Selectors
| Element | Selector | Notes |
|---------|----------|-------|
| Product card (listing) | `article.node.node--view-mode-image-box` | Drupal view mode for product listings |
| Product name (listing) | `article.node strong` | Inside listing card |
| Product link (listing) | `article.node a[href*="/solarmodul/"]` | URL pattern varies by content type |
| Product name (detail) | `h1` | Inside `<article>` |
| Product subtitle | `article h2` | Secondary heading below h1 |
| Spec container | `.node--type-{type}--details--info` | Type-specific; replace `{type}` with content type slug |
| Spec field | `.field` | Within spec container |
| Spec label | `.field__label` | Drupal standard field label |
| Spec value | `.field__item` | Drupal standard field value |
| Datasheet link | `a[href*=".pdf"]` | PDFs under `/sites/default/files/` |

## Pagination
- URL pattern: N/A — Drupal sites vary widely; check for Views pager (`?page=N`) or custom pagination
- Products per page: varies
- Next page detection: `.pager__item--next a` (Drupal default pager)

## Common Pitfalls
| Issue | Resolution |
|-------|-----------|
| Different content types have different field structures | Check `node--type-{type}` class on article to determine which selectors apply |
| Drupal field values may contain multi-line text in `<p>` with `<br>` tags | Split on `<br>` tags to get individual attribute lines |
| No sitemap.xml by default | Check for `/sitemap` HTML page or Drupal XML Sitemap module at `/sitemap.xml` |
| Cookie consent banners (Usercentrics, CookieBot) | Do not block content; ignore safely |
| Content may vary by language path prefix | Check for `/en/`, `/de/`, `/fr/` URL prefixes for multilingual sites |
| Multi-line field values with German "Label: Value" format | Split on `<br>`, then split each line on first `:` to extract sub-label and value |
| Numeric values with embedded units in German text | Parse leading number (handle comma-as-decimal), strip unit suffix and trailing text (e.g., "25 kg mit Rahmen" → 25.0) |

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| Axitec Energy | axitecsolar | 2026-03-19 | Drupal 10, theme "axitec_sass". Three content types: solarmodul (structured fields), stromspeicher (prose), wechselrichter (prose). No JSON-LD, no sitemap.xml, no prices (B2B). |
