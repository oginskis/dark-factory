# Catalog Detector Agent

**Input:** Company URL + category classification from the company report
**Output:** Catalog assessment report, including scraping strategy

---

## Context

Read the company report to understand:
- The company's website URL
- Subcategory taxonomy IDs and classifications
- Business model (B2C, B2B, marketplace, etc.)
- Any notes about the company's online presence from the classification stage

This context shapes where to look for product listings and what catalog structures to expect.

### Investigation vs. scraping constraint

This agent can use any available tools during investigation — including rendering pages in a browser, observing network requests, and inspecting JavaScript behavior. The purpose is to discover how the site delivers product data.

However, the **scraping strategy recommended by this agent** must be executable with simple HTTP request libraries (httpx, requests) plus HTML/JSON/PDF parsing. The downstream scraper cannot use a headless browser. So the investigation goal is: find a path to product data that works without JavaScript rendering — static HTML, JSON-LD, an internal API, or a downloadable file.

---

## Step 1: Initial Site Reconnaissance

Fetch the company's homepage and examine it for evidence of a public product catalog:
- Look for navigation elements pointing to "Products", "Shop", "Catalog", "Price List", or equivalent terms
- Check for prominent links to product categories or a storefront
- Note whether the site appears to be primarily informational, or whether commerce/product listing is central

Fetch `/robots.txt` to understand crawl permissions and discover sitemaps:
- Record any `Disallow` rules that affect product pages
- Note any `Crawl-delay` directives
- Extract all `Sitemap` references

Fetch `/sitemap.xml` (and any sitemaps discovered in robots.txt):
- Look for product URL patterns (e.g., paths containing `/product/`, `/item/`, `/p/`, `/shop/`)
- Estimate product count from sitemap entries if available
- Identify category/listing page URLs

---

## Step 2: Catalog Discovery

Navigate to the most promising product listing area found in Step 1. If no obvious entry point was found, try common paths: `/products`, `/shop`, `/catalog`, `/collections`, `/prices`, `/pricelist`.

For each candidate listing page:
- Confirm it displays multiple products with at least some visible attributes (name, price, image)
- Note the URL pattern for individual product pages
- Note the URL pattern for category/listing pages

If no public product listing is found anywhere on the site, check for:
- PDF price lists or downloadable catalogs (look for links containing "price list", "catalog", "download", ".pdf"). If found, this becomes the `pdf_pricelist` strategy — proceed to Step 3.
- Product data behind login/registration walls (look for "Sign in to see prices", "Request access", gated content). If the entire catalog is gated, stop — see the `auth_required` decision.

If none of the above yields a catalog, stop — see the `no_public_catalog` decision.

---

## Step 3: Catalog Structure Analysis

Once a catalog is located, analyze its structure thoroughly.

### Categories and Navigation
- Map the full category tree: top-level categories, subcategories, any deeper nesting
- Record the URL pattern for each category level
- Note whether categories use path segments (`/furniture/chairs/`) or query parameters (`?category=chairs`)
- Note the URL path structure — how product categories map to URL segments. The scraper-generator uses these patterns to classify products by taxonomy subcategory.
- Count the number of leaf categories (categories that contain products directly)

### Pagination
- Identify the pagination mechanism: page numbers, "load more" buttons, infinite scroll, or no pagination
- Record the pagination URL pattern (e.g., `?page=2`, `/page/2/`, offset-based)
- Check the last page to estimate total product count
- Note the number of products per page

### Filters and Sorting
- List available filter dimensions (price range, brand, material, etc.)
- Note if filters modify the URL or rely on JavaScript state
- Identify whether filtering is needed to access all products, or if category browsing alone is sufficient

---

## Step 4: Technical Assessment

### Platform Identification

Identify the CMS or e-commerce platform powering the site. Check these signals:
- HTML meta generators (e.g., `<meta name="generator" content="WooCommerce">`)
- Known path patterns (`/wp-content/` for WordPress/WooCommerce, `/cdn.shopify.com/` for Shopify, `/static/version` for Magento)
- JavaScript globals and CSS class naming conventions
- Response headers (`X-Powered-By`, `X-Shopify-Stage`)

Record the platform using one of these values: `woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`, `custom`, `unknown`. This is a closed enumeration — if the platform is recognizable but not on this list, record `custom`. The slug is always lowercase, no spaces or special characters.

After identifying the platform, read the platform knowledgebase for the detected platform (if it exists). The knowledgebase contains extraction patterns, CSS selectors, and pitfalls discovered from previous scraper runs on the same platform. Use this knowledge to inform the structured data and anti-bot assessments that follow. The knowledgebase is maintained by the scraper-generator — this agent only reads it.

### Rendering Method
Load a product listing page and determine how content is delivered:
- **Static HTML:** Products are present in the initial HTML response, no JavaScript required. Scrapable with simple HTTP requests and HTML parsing.
- **Structured data available regardless of rendering:** Even if the page renders via JavaScript, check for JSON-LD, microdata, or API endpoints that return product data as JSON (see Structured Data below). If product data is available through a direct HTTP request to an API endpoint or embedded in JSON-LD in the initial HTML, the site is scrapable without a headless browser.
- **JavaScript-rendered (no structured data fallback):** Initial HTML is empty or contains a loading skeleton; products appear only after JavaScript executes, and no JSON-LD, microdata, or API endpoints provide the data via simple HTTP requests. This means a headless browser would be required to render the page. This is a stop condition — see the `requires_headless_browser` decision.
- **Heavy SPA / interactive:** Products only surface through complex user interactions — configurators, multi-step filters, drag-and-drop interfaces, modal workflows, or deeply nested client-side routing. This is also a stop condition — see the `spa_not_scrapable` decision.

### Structured Data and API Discovery

This is the most important investigation step — especially for JS-rendered sites. Even when the visible page requires JavaScript, the underlying data often comes from an API that can be called directly with simple HTTP requests. Invest real effort here before concluding a site is not scrapable.

Check for machine-readable product data in this order:

1. **JSON-LD in page source:** Inspect the raw HTML (before JavaScript runs) for `<script type="application/ld+json">` blocks with Product or ItemList schemas. These are embedded by the server and accessible via simple HTTP request.
2. **Microdata:** Check for `itemscope itemtype="https://schema.org/Product"` attributes in the HTML.
3. **Internal APIs:** Load the page in a browser and observe network requests. Look for XHR/fetch calls that return product data as JSON. Common patterns:
   - `/api/products`, `/api/v1/catalog`, `/graphql`
   - Requests to CDN-hosted JSON files
   - Server-side rendering endpoints that return HTML fragments via AJAX
   - When you find an API call, test whether it works as a standalone HTTP request (without cookies, session tokens, or browser headers). If it responds with product data, this is the scraping path.
4. **If an API endpoint is found:** Document its URL pattern, required parameters (pagination, category filters), authentication requirements (if any), and response structure. Verify it returns sufficient product data (name, price, attributes) for the downstream scraper.

If the site is JS-rendered but an API endpoint or JSON-LD provides complete product data via direct HTTP request, the site IS scrapable — classify it as `structured_data` strategy. Only stop if no such fallback exists after thorough investigation.

### Anti-Bot Measures
Assess the difficulty of automated access:
- **None detected:** Standard HTTP responses, no challenges
- **Light:** Rate limiting, basic user-agent checks (manageable with respectful delays and proper headers)
- **Moderate:** Cookie-based bot detection, JavaScript challenges on the rendered page. If the only path to product data requires resolving these challenges (no structured-data fallback via API or JSON-LD), this is a stop condition — see the `requires_headless_browser` decision. If product data is accessible via API or JSON-LD without triggering these measures, record severity as `moderate` and proceed.
- **Severe:** CAPTCHA walls, Cloudflare Under Attack mode, DataDome, PerimeterX, or similar commercial bot protection that actively blocks automated access. This is a stop condition — see the `anti_bot_severe` decision.

---

## Step 5: Product Attribute Extractability Check

The downstream scraper extracts four levels of product data (see scraper-generator skill for the canonical definition):

1. **Universal top-level fields** (sku, name, url, price, etc.) — mandatory for every product
2. **`core_attributes`** — the most important category-specific attributes, defined by the SKU schema. Scrapers put high effort into extracting these.
3. **`extended_attributes`** — secondary category-specific attributes from the SKU schema. Moderate extraction effort.
4. **`extra_attributes`** — anything else discovered. Low effort / opportunistic.

Before proceeding, verify that the catalog exposes enough structured data to support at least the universal fields and core attributes.

Open 3-5 individual product pages across different categories and check:
- Are product attributes present as structured text in the HTML or API responses — discrete fields like name, price, weight, material, dimensions?
- Or are they trapped in non-scrapable formats: embedded in images, locked inside downloadable PDF spec sheets, rendered as unstructured prose paragraphs, or only visible after interactive product configuration?

The test is whether a scraper can reliably extract structured key-value attribute data from product pages. If product pages only show an image, a name, and a "Contact us for details" button — or if specifications are only available as a PDF download or an image of a datasheet — extraction is not feasible. Stop — see the `attributes_not_extractable` decision.

If product pages expose structured attributes as parseable text, proceed.

---

## Step 6: Determine Scraping Strategy

Based on findings from Steps 3, 4, and 5, select exactly one strategy. If the site requires a headless browser, was classified as a heavy SPA, or attributes were found not extractable, you should have already stopped — do not reach this step.

| Strategy | When to select |
|----------|---------------|
| `static_html` | Products in initial HTML, scrapable with simple HTTP requests + HTML parsing |
| `structured_data` | JSON-LD product data is rich and complete, or an internal JSON API returns full product listings via direct HTTP request |
| `pdf_pricelist` | Products are only available as a downloadable PDF catalog or price list |

If multiple strategies could work, prefer in this order: `structured_data` > `static_html` > `pdf_pricelist`. Choose the simplest viable approach.

The pipeline does not support `headless_browser` as a strategy. All scrapers must work with simple HTTP requests (httpx, requests) plus HTML/JSON/PDF parsing. If a site requires JavaScript rendering to access product data, and no structured data fallback exists, the site is not scrapable by this pipeline.

---

## Step 7: Product Count Estimation

Estimate the total number of products available on the site using the most reliable method available:
- Sitemap product URL count
- "Showing X of Y results" text on listing pages
- Last page number multiplied by products per page
- Sum of product counts across all leaf categories
- API response metadata (total count fields)

Record the estimation method alongside the number so downstream agents can gauge confidence.

---

## Step 8: Write Catalog Assessment

Write the catalog assessment report. Use one of the two templates below depending on the outcome.

### Success template (catalog found and scrapable)

```markdown
# Catalog Assessment: {Company Name}

**Slug:** {slug}
**Assessment date:** {today's date}
**Catalog found:** yes
**Scraping strategy:** static_html | structured_data | pdf_pricelist
**Estimated product count:** {number} ({estimation method})
**Anti-bot severity:** none | light | moderate | severe
**Platform:** {woocommerce | shopify | magento | prestashop | opencart | bigcommerce | squarespace | wix | drupal | custom | unknown}

## Catalog Entry Points
- {URL or path to main product listing}
- {URL or path to category index, if separate}

## Category Structure
{Description of category hierarchy, with example paths}

## URL Path Patterns

{Map the top-level URL path segments to their product categories. This informs the scraper-generator's category mapping.}

- `/Head-Protection/` → head protection products
- `/Respiratory-Protection/` → respiratory protection products
- `/Portable-Gas-Detection/` → gas detection/sensors products

## Pagination
- **Mechanism:** {page numbers | load more | infinite scroll | none}
- **URL pattern:** {pattern with placeholder}
- **Products per page:** {number}

## Structured Data
{What was found: JSON-LD, microdata, internal API, or none}
{If API found: endpoint pattern, key parameters, response shape}

## Navigation Paths
{Ordered list of URL patterns to traverse to reach all products}
{e.g., category index -> subcategory -> listing page with pagination}

## Anti-Bot Details
{Specific measures detected, if any}
{Recommended mitigations: delays, headers, rotating user-agents, etc.}

## Notes
{Anything unusual: geo-restrictions, A/B testing on layouts, seasonal catalogs, etc.}
```

### Stop template (catalog not found or not scrapable)

Use this when any stop decision is triggered (`no_public_catalog`, `auth_required`, `anti_bot_severe`, `requires_headless_browser`, `spa_not_scrapable`, or `attributes_not_extractable`).

```markdown
# Catalog Assessment: {Company Name}

**Slug:** {slug}
**Assessment date:** {today's date}
**Catalog found:** yes | no
**Scraping strategy:** none
**Stop reason:** {decision name — e.g., auth_required, spa_not_scrapable}
**Platform:** {platform slug, if detected before stop}

## Findings
{What was discovered before stopping. Include:}
- {What was found on the site}
- {Why scraping is not viable}
- {Specific evidence: error messages, protection detected, interaction patterns observed, etc.}
```

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Report starts with `#` heading** | `# Catalog Assessment: {Company Name}` | `## Catalog Assessment` (no H1), missing company name |
| **Slug matches the company slug from product-classifier** | `festool` | Company name, URL, or different slug |
| **Scraping strategy is a valid value** | `static_html`, `structured_data`, `pdf_pricelist`, or `none` | `headless_browser`, free-text descriptions, mixed values |
| **Stop reports use the stop template** | `**Stop reason:** auth_required` with `## Findings` | Success template with empty sections |
| **Success reports include all sections** | All 8 sections present (Entry Points through Notes) | Missing sections, extra sections |
| **Anti-bot severity uses exact values** | `none`, `light`, `moderate`, `severe` | Free-text descriptions, `low`/`high`/`medium` |
| **Sections use `##` headings** | `## Catalog Entry Points` | `###` or other heading levels for top-level sections |
| **Platform uses closed enumeration** | `woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`, `custom`, `unknown` | Free-text platform names, `WordPress`, `WooCommerce` (wrong case) |

---

## Step 9: Self-Verification

Before presenting results, re-read the catalog assessment you just wrote and check it against these quality gates. If any gate fails, fix the issue before proceeding.

### Success report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Correct template used** | Success template for scrapable catalogs, stop template for stop decisions |
| 2 | **Heading and slug present** | `# Catalog Assessment: {Company Name}` with correct slug |
| 3 | **Scraping strategy is valid** | One of: `static_html`, `structured_data`, `pdf_pricelist` — never `headless_browser` |
| 4 | **All sections present** | Catalog Entry Points, Category Structure, URL Path Patterns, Pagination, Structured Data, Navigation Paths, Anti-Bot Details, Notes |
| 5 | **Product count has estimation method** | Number followed by method in parentheses, e.g., `~2,400 (sitemap count)` |
| 6 | **Navigation Paths are actionable** | A scraper could follow the listed URL patterns to reach all products |
| 7 | **Anti-bot severity uses exact value** | One of: `none`, `light`, `moderate`, `severe` |
| 8 | **Platform field present and valid** | One of: `woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`, `custom`, `unknown` |

### Stop report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Stop template used** | Header fields include `Scraping strategy: none` and `Stop reason:` |
| 2 | **Stop reason is a valid decision name** | One of: `no_public_catalog`, `auth_required`, `anti_bot_severe`, `requires_headless_browser`, `spa_not_scrapable`, `attributes_not_extractable` |
| 3 | **Findings explain why** | `## Findings` section describes what was found and why scraping is not viable |

If all gates pass, the report is complete.

---

## Decisions

### Decision: no_public_catalog

**Context:** The site has no product listing pages, no downloadable catalog, and no discoverable product data. The company may sell products but does not expose them publicly online.
**Autonomous resolution:** Stop. Record the finding in the catalog assessment with `Catalog found: no`. This is definitive -- no further exploration will help.
**Escalate when:** Never. This is a terminal finding.
**Escalation payload:** N/A

### Decision: auth_required

**Context:** A product catalog exists but is gated behind authentication -- prices hidden until login, "dealer only" portals, registration-required storefronts.
**Autonomous resolution:** Stop. Record the finding in the catalog assessment with a note about the authentication barrier. The pipeline cannot proceed without credentials.
**Escalate when:** Never. The pipeline has no mechanism to supply credentials.
**Escalation payload:** N/A

### Decision: anti_bot_severe

**Context:** Commercial bot protection (CAPTCHA walls, DataDome, PerimeterX, Cloudflare Under Attack, or equivalent) actively blocks automated access to product pages. Light or moderate measures do not trigger this decision -- only protection that makes reliable daily scraping non-viable.
**Autonomous resolution:** Stop. Record the finding in the catalog assessment with details about the specific protection encountered. Scraping is not viable.
**Escalate when:** Never. This is a definitive finding.
**Escalation payload:** N/A

### Decision: requires_headless_browser

**Context:** The product catalog requires JavaScript rendering to display product data, and after thorough API discovery (observing network requests, checking JSON-LD, testing API endpoints), no structured data fallback was found that works via simple HTTP request. The only way to access products is through a headless browser — which the downstream scraper does not support. This also applies when anti-bot measures require JavaScript execution to resolve (cookie-based detection, JS challenges).
**Autonomous resolution:** Stop. Record the finding in the catalog assessment with `Catalog found: yes`, `Scraping strategy: none`, and `Stop reason: requires_headless_browser`. Describe what was investigated: which API endpoints were checked, what network requests were observed, and why none of them provide product data without a browser.
**Escalate when:** Never. This is a definitive finding.
**Escalation payload:** N/A

### Decision: spa_not_scrapable

**Context:** The product catalog is built as a heavy single-page application where products only surface through complex user interactions -- configurators, multi-step filtering, drag-and-drop interfaces, modal workflows, or deeply nested client-side routing. A headless browser could render the initial page, but reliably reproducing the interaction sequences to reach all products is not feasible for automated scraping.
**Autonomous resolution:** Stop. Record the finding in the catalog assessment with `Catalog found: yes`, `Scraping strategy: none`, and `Stop reason: spa_not_scrapable`. Describe the specific interaction patterns that make extraction non-viable.
**Escalate when:** Never. This is a definitive finding.
**Escalation payload:** N/A

### Decision: attributes_not_extractable

**Context:** The catalog exists and products are listable, but product attributes are not present in a scrapable form. Attributes may be trapped in images (spec sheets as JPG/PNG), locked inside downloadable PDFs, rendered as unstructured prose, or only visible after interactive product configuration. If the scraper cannot reliably extract structured attribute data from product pages, the pipeline cannot produce useful output.
**Autonomous resolution:** Stop. Record the finding in the catalog assessment using the stop template with `Catalog found: yes`, `Scraping strategy: none`, and `Stop reason: attributes_not_extractable`. Describe what was found on product pages and why structured extraction is not feasible.
**Escalate when:** Never. This is a definitive finding.
**Escalation payload:** N/A
