# Catalog Detector Workflow

**Input:** Company URL + category classification from the company report
**Output:** Catalog assessment with extraction blueprint

---

## Context

This workflow produces a concrete extraction blueprint that the scraper-generator can translate directly into code. It leverages the platform knowledgebase to skip redundant investigation for known platforms.

The workflow has one branch point — **discovery** — where known platforms use a fast path (load + verify knowledgebase recipe) and unknown platforms do full site investigation. Everything before and after discovery is shared.

### Investigation vs. scraping constraint

This workflow can use any tools during investigation — including a browser, network inspection, and JavaScript analysis. But the **recommended scraping strategy** must work with simple HTTP libraries (httpx) plus HTML/JSON/PDF parsing. No headless browser. The goal: find a data path that works without JavaScript rendering.

### Platform knowledgebase ownership

This workflow owns `docs/platform-knowledgebase/`. Reads on every run, writes on every successful run. The knowledgebase captures platform-level patterns — not site-specific quirks.

---

## Step 1: Platform Detection

Read the company report for the website URL, taxonomy IDs, and business model.

Fetch the homepage and identify the platform:
- HTML meta generators (`<meta name="generator" content="WooCommerce">`)
- Known path patterns (`/wp-content/`, `/cdn.shopify.com/`, `/static/version`)
- JavaScript globals and CSS class conventions
- Response headers (`X-Powered-By`, `X-Shopify-Stage`)

Record the platform: `woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`, `custom`, `unknown`. Closed enumeration — if recognizable but not listed, use `custom`.

Also check for catalog evidence:
- Navigation links to "Products", "Shop", "Catalog", "Price List"
- `/robots.txt` for sitemap references
- `/sitemap.xml` for product URL patterns and count estimates

**Routing:** If a knowledgebase file exists at `docs/platform-knowledgebase/{platform-slug}.md` → Step 2 (Fast Path). Otherwise → Step 3 (Deep Investigation).

---

## Step 2: Fast Path Discovery (Known Platforms)

Applies when a platform knowledgebase exists.

### Step 2a: Load Knowledgebase

Read the platform knowledgebase. Extract: API endpoints, CSS selectors, pagination patterns, common pitfalls.

### Step 2b: Verify Recipe

Spot-check 2-3 product pages across different categories using the known patterns:

- **API verification passes** if the endpoint returns HTTP 200 with product data containing at least name and price.
- **CSS selector verification passes** if selectors extract non-empty text on all checked pages.
- **Pagination verification passes** if page 2 returns different products than page 1.

Any single failure triggers `platform_recipe_failed` — fall back to Step 3 (starting at 3b, skipping platform detection). Carry forward what didn't work.

Record deviations that aren't failures (theme variations, extra CSS classes).

After verification passes, proceed to Step 4 (Build Extraction Blueprint).

---

## Step 3: Deep Investigation Discovery (Custom/Unknown Platforms)

Applies when the platform is `custom`, `unknown`, or fast path failed.

### Step 3a: Anti-Bot Check

- **None / Light:** proceed
- **Moderate:** if data accessible via API/JSON-LD without triggering measures, record `moderate` and proceed. If not, stop — see `js_only` decision.
- **Severe:** CAPTCHA, DataDome, PerimeterX, Cloudflare Under Attack. Stop — see `anti_bot_severe` decision.

### Step 3b: Catalog Discovery

Find product listing pages via navigation links from Step 1, or try: `/products`, `/shop`, `/catalog`, `/collections`, `/prices`, `/pricelist`.

For each candidate: confirm products with visible attributes, note URL patterns for products and categories.

If no listing found:
- PDF catalogs → `pdf` strategy, continue
- Login-gated → stop, see `auth_required` decision
- Nothing → stop, see `no_public_catalog` decision

### Step 3c: Technical Assessment

**Rendering:** Static HTML, structured data available (JSON-LD/API), or JS-only. If JS-only with no structured data fallback after thorough API discovery → stop, see `js_only` decision.

**API Discovery** — the most important step. Check in order:
1. JSON-LD (`<script type="application/ld+json">`) with Product/ItemList schemas
2. Microdata (`itemscope itemtype="https://schema.org/Product"`)
3. Internal APIs — observe network requests in browser, test as standalone HTTP calls
4. Document any API: URL pattern, parameters, auth requirements, response structure

### Step 3d: Extractability Check

Open 3-5 product pages across categories. Are attributes structured text or trapped in images/PDFs/prose? If not extractable → stop, see `attributes_not_extractable` decision.

While inspecting, record extraction metadata:
- **Price method:** JSON-LD price field → CSS price classes → dataLayer → API calls
- **Spec table selectors:** container, row iterator, label cell, value cell
- **Product name selector**, **SKU location**, **breadcrumb selector**
- **Sample attribute labels:** every unique label with frequency and example value

After completing discovery, proceed to Step 4.

---

## Step 4: Build Extraction Blueprint

This step is shared — uses whatever was discovered in Step 2 or Step 3.

### Scraping strategy

Select one: `html_css`, `json_api`, `pdf`. Prefer: `json_api` > `html_css` > `pdf`.

### Product count estimate

Use the most reliable method: sitemap count, "X of Y results" text, last page × products per page, sum of leaf categories, or API metadata. Record the method.

### Blueprint content

1. **Data source** — primary method (API, JSON-LD, static HTML, PDF), concrete endpoint/selector, parameters, response shape.
2. **Product discovery** — discovery method, pagination URL pattern, products per page.
3. **Verified category tree** — crawl from top-level categories. For each node: category path, exact URL, product count (leaf nodes), depth. Circuit breaker: 100 nodes or depth 5.
4. **Product data extraction** — for each field (price, name, SKU, spec table, breadcrumb): concrete selector or API path, verified on 2-3 product URLs with actual extracted values.
5. **Sample attribute labels** — every unique label from spec tables across 3-5 pages, with frequency and example value.

### Write catalog assessment

Write the report using the success template (see Report Templates below). Proceed to Step 5.

---

## Step 5: Update Platform Knowledgebase

Skip for `unknown` or `custom` platforms (unless the site is a recognizable CMS — see below).

### Known platforms

1. **Append to Sites table** — company name, slug, date, 1-2 sentence summary.
2. **Add pattern corrections** — new selectors, theme variations, pitfalls discovered.

### Newly identified platforms

If the site uses a recognizable CMS (identifiable via meta generators, known paths, response headers) with consistent conventions, create a new knowledgebase file:

```markdown
# Platform: {Platform Name}

## JSON-LD Patterns
{Schemas present, field mappings, quirks}

## CSS Selectors
| Element | Selector | Notes |
|---------|----------|-------|
| {element} | {selector} | {notes} |

## Pagination
- URL pattern: {pattern}
- Products per page: {number}
- Next page detection: {method}

## Common Pitfalls
| Issue | Resolution |
|-------|-----------|
| {issue} | {resolution} |

## Sites Using This Platform
| Company | Slug | Date | Notes |
|---------|------|------|-------|
| {company} | {slug} | {date} | {notes} |
```

**Rules:** Additive only — never remove patterns that worked for other sites. Site-specific quirks stay in the catalog assessment.

---

## Step 6: Self-Verification

Re-read the catalog assessment and check against these gates. Fix any failures before proceeding.

### Success report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Correct template** | Success template for scrapable catalogs, stop template for stops |
| 2 | **Heading and slug** | `# Catalog Assessment: {Company Name}` with correct slug |
| 3 | **Strategy valid** | One of: `html_css`, `json_api`, `pdf` |
| 4 | **Platform valid** | One of the platform enumeration values |
| 5 | **Data source concrete** | Actual endpoint/selector, not placeholders |
| 6 | **Discovery actionable** | Discovery method, pagination pattern, products per page all specified |
| 7 | **Category tree complete** | Every leaf category has a row with verified URL and count > 0 |
| 8 | **Price verified** | At least 2 product URLs with actual extracted prices |
| 9 | **Spec table verified** | At least 2 product URLs with attribute counts |
| 10 | **Product count** | Number with estimation method in parentheses |
| 11 | **Knowledgebase updated** | Sites table appended or new file created |
| 12 | **Anti-bot value** | One of: `none`, `light`, `moderate` |

### Stop report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Stop template** | `Scraping strategy: none` and `Stop reason:` present |
| 2 | **Valid stop reason** | One of: `no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, `attributes_not_extractable` |
| 3 | **Findings explain why** | `## Findings` describes what was found and why scraping is not viable |

---

## Report Templates

### Success template

```markdown
# Catalog Assessment: {Company Name}

**Slug:** {slug}
**Assessment date:** {date}
**Catalog found:** yes
**Scraping strategy:** html_css | json_api | pdf
**Platform:** {platform-slug}
**Anti-bot:** none | light | moderate {one-line mitigation note if needed}
**Estimated product count:** {number} ({estimation method})
**Currency:** {ISO 4217}

## Extraction Blueprint

### Data Source
- **Primary method:** {api_endpoint | html_css_css | json_ld | pdf}
- **Endpoint/URL pattern:** {concrete pattern with placeholders}
- **Parameters:** {pagination, category filters, limits}
- **Response shape:** {brief description of JSON structure or HTML layout}
- **Authentication:** none
- **Fallback method:** {if primary fails — or "none"}

### Product Discovery
- **Discovery method:** {sitemap | api_pagination | category_traversal}
- **Pagination mechanism:** {page numbers | cursor | offset | none}
- **Pagination URL pattern:** {concrete pattern}
- **Products per page:** {number}

#### Verified Category Tree

| Category Path | URL | Product Count | Depth |
|---|---|---|---|
| {Level 1} > {Level 2} > {Leaf} | {exact URL} | {count} | {depth} |

### Product Data Extraction

#### Price
- **Method:** {html_css_css | json_ld | dataLayer | api_endpoint}
- **Selector/path:** {concrete CSS selector or JSON path}
- **Verified on:** {2-3 product URLs with actual extracted prices}
- **Price variants:** {description if applicable}

#### Product Name
- **Selector:** {CSS selector or JSON path}

#### SKU/Reference
- **Source:** {spec table label | JSON-LD field | API field | dedicated element}
- **Selector/path:** {concrete selector or path}

#### Spec Table / Attributes
- **Container:** {CSS selector or API response path}
- **Row selector:** {CSS selector for attribute rows}
- **Label cell:** {CSS selector or position}
- **Value cell:** {CSS selector or position}
- **Verified on:** {2-3 product URLs with attribute counts}

#### Breadcrumb
- **Selector:** {CSS selector}

#### Sample Attribute Labels

| Site Label | Frequency | Example Value |
|---|---|---|
| {exact label text} | {N/M pages} | {example} |

### Platform-Specific Notes
- {Known pitfalls from knowledgebase that apply}
- {Site-specific deviations from standard platform behavior}
- {Anything unusual: geo-restrictions, A/B testing, seasonal catalogs}
```

### Stop template

```markdown
# Catalog Assessment: {Company Name}

**Slug:** {slug}
**Assessment date:** {date}
**Catalog found:** yes | no
**Scraping strategy:** none
**Stop reason:** {decision name}
**Platform:** {platform slug, if detected before stop}

## Findings
{What was discovered before stopping:}
- {What was found on the site}
- {Why scraping is not viable}
- {Specific evidence}
```

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **H1 heading** | `# Catalog Assessment: {Company Name}` | `## Catalog Assessment`, missing name |
| **Slug** | `festool` | Company name, URL, different slug |
| **Strategy** | `html_css`, `json_api`, `pdf`, `none` | `headless_browser`, free-text |
| **Stop reports** | `**Stop reason:** auth_required` + `## Findings` | Success template with empty sections |
| **Success reports** | `## Extraction Blueprint` with all subsections | Survey-style sections |
| **Anti-bot** | `none`, `light`, `moderate` | `severe` (should be stop), free-text |
| **Platform** | `woocommerce`, `shopify`, `magento`, etc. | `WordPress`, `WooCommerce` (wrong case) |

---

## Boundaries

- Produces extraction blueprints — does not generate scrapers or classify companies.
- Verifies selectors on a few pages — does not test extraction at scale.
- Does not modify the product taxonomy or SKU schemas.
- Owns the platform knowledgebase.

---

## Decisions

### Decision: no_public_catalog

**Context:** No product listing pages, no downloadable catalog, no discoverable product data.
**Autonomous resolution:** Stop. Write stop template with `Catalog found: no` and `Stop reason: no_public_catalog`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: auth_required

**Context:** Catalog gated behind authentication — login-only prices, dealer portals.
**Autonomous resolution:** Stop. Write stop template with `Stop reason: auth_required`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: anti_bot_severe

**Context:** Commercial bot protection (CAPTCHA, DataDome, PerimeterX, Cloudflare Under Attack) blocks automated access.
**Autonomous resolution:** Stop. Write stop template with `Stop reason: anti_bot_severe`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: js_only

**Context:** Site requires JavaScript rendering with no structured data fallback (JSON-LD, API) after thorough discovery. Also applies when anti-bot requires JS execution with no alternative data path. Merges the former `requires_headless_browser` and `spa_not_scrapable` decisions.
**Autonomous resolution:** Stop. Write stop template with `Catalog found: yes`, `Stop reason: js_only`. Describe what was investigated.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: attributes_not_extractable

**Context:** Catalog exists but attributes are trapped in images, PDFs, prose, or interactive configurators.
**Autonomous resolution:** Stop. Write stop template with `Catalog found: yes`, `Stop reason: attributes_not_extractable`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: platform_recipe_failed

**Context:** Knowledgebase recipe doesn't work on this site — API returns 403, selectors don't match, pagination fails.
**Autonomous resolution:** Fall back to Step 3 (starting at 3b). Carry forward what didn't work, record in Platform-Specific Notes and knowledgebase Common Pitfalls.
**Escalate when:** Never. Track switch, not a stop.
**Escalation payload:** N/A
