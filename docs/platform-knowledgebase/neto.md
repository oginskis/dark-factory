# Platform: Neto (Maropost Commerce Cloud)

Australian e-commerce platform, now branded as Maropost Commerce Cloud. Used primarily by Australian retailers.

## JSON-LD Patterns
No JSON-LD support. Uses schema.org microdata instead (`itemscope itemtype="http://schema.org/Product"`).

## Microdata Patterns
| Element | Itemprop | Selector | Notes |
|---------|----------|----------|-------|
| Product name | `name` | `h1[itemprop="name"]` | Plain text |
| Price | `price` | `div[itemprop="price"]` | `content` attr has numeric value |
| Currency | `priceCurrency` | `meta[itemprop="priceCurrency"]` | `content` attr (e.g., "AUD") |
| SKU | `productID` | `span[itemprop="productID"]` | Neto product SKU |
| Brand | `brand` | `meta[itemprop="brand"]` | `content` attr |
| Description | `description` | `p[itemprop="description"]` | Short description |
| Image | `image` | `img[itemprop="image"]` | Main product image |
| MPN | `mpn` | `meta[itemprop="mpn"]` | Manufacturer part number |

## CSS Selectors
| Element | Selector | Notes |
|---------|----------|-------|
| Product container | `div[itemtype*="Product"]` | Schema.org Product scope |
| Price (main) | `.card-price_nowwar div[itemprop="price"]` | Primary product price |
| Breadcrumb | `ol.breadcrumb li.breadcrumb-item` | Schema.org BreadcrumbList |
| Spec tab | `#specifications` | Tab pane with dimensions/specs |
| Spec items (list) | `#specifications li` | "Label: Value" format |
| Spec items (para) | `#specifications p` | `<strong>Label:</strong> Value` format |
| Features tab | `#features` | Product features as `<li>` items |
| Product cards (listing) | `.thumbnail, .card.thumbnail` | Product grid items |
| Product card name | `p.card-title.h4[itemprop="name"]` | On listing pages |
| Product card price | `div.price span[itemprop="price"]` | On listing pages |
| Products found count | Text matching `\d+ Products? Found` | At top of listing pages |

## JavaScript Objects
The `k4n` global object is embedded as an inline `<script>var k4n = {...};</script>`. Structure:
```javascript
var k4n = {
  current_page: "product",
  product: {
    sku: "SKU123",
    product_id: "123",
    name: "URL-encoded%20name",    // URL-encoded with HTML entities
    categories: ["Cat1", "Cat2"],  // URL-encoded
    image: "URL-encoded-image-url",
    url: "URL-encoded-product-url",
    brand: "URL-encoded%20brand",
    price: "249.95",
    rrp: ""                        // Recommended retail price, often empty
  }
};
```
Values are URL-encoded with HTML entities (e.g., `%26%23x2122%3B` for ™). Requires `urllib.parse.unquote()` + `html.unescape()`.

## Pagination
- URL pattern: `{category_url}?pgnum={n}`
- Products per page: ~24
- Next page detection: Check for pagination links with `pgnum` parameter

## Common Pitfalls
| Issue | Resolution |
|-------|-----------|
| k4n values are URL-encoded with HTML entities | Apply `urllib.parse.unquote()` then `html.unescape()` |
| Spec tab may be empty for some products | Check for content before parsing — kitchen tools/accessories often lack specs |
| Multiple `itemprop="price"` on page | Related products also have microdata; scope selectors to main product container `div[itemtype*="Product"]` |
| `.gaec-product` data attributes | These are on recommended product cards, not the main product — do not use for primary extraction |
| robots.txt crawl delay | Respect 1-second crawl delay |
| Sitemap is gzipped | `sitemap_index.xml.gz` — requires decompression |

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| SOLIDteknics | solidteknics | 2026-03-20 | Australian cookware manufacturer. Specs in li/p format, some products have empty spec tabs. Spec content inside accordion collapse `#accordionSpecifications`. |
