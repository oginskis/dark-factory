# Catalog Detector Redesign Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign catalog-detector to produce platform-first extraction blueprints that the scraper-generator can translate directly into code, with two-track workflow (fast path for known platforms, deep investigation for custom/unknown) and platform knowledgebase ownership.

**Architecture:** Rewrite SKILL.md and references/workflow.md to implement a two-track workflow that splits after platform detection. Known platforms use the knowledgebase as a recipe, verify it, and fill in site-specific values. Custom/unknown platforms do full investigation. Both produce the same extraction-blueprint-first output format. Downstream consumers (scraper-generator, product-discovery) are updated to match new section names and decision names.

**Tech Stack:** Markdown skill files, Python verification script (existing)

**Spec:** `docs/superpowers/specs/2026-03-17-catalog-detector-redesign.md`

---

## Chunk 1: Core catalog-detector skill rewrite

### Task 1: Rewrite SKILL.md

**Files:**
- Modify: `.claude/skills/catalog-detector/SKILL.md`

- [ ] **Step 1: Rewrite the SKILL.md file**

Replace the entire content of `.claude/skills/catalog-detector/SKILL.md` with:

```markdown
---
name: catalog-detector
description: >
  Detect whether a company has a public product catalog and produce a concrete extraction blueprint for the scraper-generator.
  Produces a catalog assessment with verified selectors, API endpoints, category tree, and platform-specific extraction recipe.
  Use this skill when the user wants to check catalog availability or scrapability for a company that has already been classified —
  "check if X has a catalog", "detect pricelist for X", "what scraping strategy for X", "can we scrape X",
  "does X have a public product listing". Requires a company report from /product-classifier to exist first.
  If the user wants the full pipeline, use /product-discovery instead.
user-invocable: true
---

# Catalog Detector

Produce a concrete extraction blueprint that the scraper-generator can translate directly into code, leveraging platform-specific knowledge to minimize downstream investigation.

## Input

`$ARGUMENTS` is the company slug (e.g., `festool`).

## File locations

| Resource | Path |
|----------|------|
| Company report | `docs/product-classifier/{slug}.md` |
| Catalog assessment (output) | `docs/catalog-detector/{slug}.md` |
| Platform knowledgebase (read+write) | `docs/platform-knowledgebase/{platform-slug}.md` |

The platform knowledgebase is both read and written by this skill. For known platforms, it is loaded as the primary extraction recipe. After every successful run, the knowledgebase is updated with site-specific findings. For newly identified platforms on the deep investigation path, a new knowledgebase file is created.

## Workflow

Read and follow `references/workflow.md`.

- Read the company report first for the company URL, categories, and business model context.
- Provide the file paths from the table above when the workflow references logical resources (e.g., "the company report", "write the catalog assessment report", "the platform knowledgebase").
- Use web search, web fetch, and Playwright browser tools to investigate catalog pages as the workflow directs.
- This skill does not escalate — all decisions are autonomous stops or track switches. If the workflow determines scraping is not viable (`no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, or `attributes_not_extractable`), it writes a minimal catalog assessment and stops. If the fast-path recipe verification fails (`platform_recipe_failed`), the workflow autonomously switches to the deep investigation path. Report the outcome to the user.
- The platform knowledgebase may not exist for platforms not yet encountered. On the fast path, a missing knowledgebase file means the platform is treated as unknown (deep investigation). On the deep investigation path, a new knowledgebase file is created if the platform is identifiable.

## Notes

File-driven skill — no database or external services required.
This skill owns the platform knowledgebase — it reads on every run and writes on every successful run.
```

- [ ] **Step 2: Verify SKILL.md structure**

Visually check:
- Frontmatter has name, description, user-invocable
- One-line summary after `# Catalog Detector`
- `## Input` section present
- `## File locations` table has all 3 resources
- `## Workflow` starts with "Read and follow `references/workflow.md`."
- `## Notes` has "File-driven skill" line
- No `## Escalation handling` (correct — no escalations)

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/catalog-detector/SKILL.md
git commit -m "Rewrite catalog-detector SKILL.md for platform-first extraction blueprints"
```

---

### Task 2: Rewrite references/workflow.md

**Files:**
- Modify: `.claude/skills/catalog-detector/references/workflow.md`

This is the largest task. The workflow.md is rewritten from scratch to implement the two-track design. The full content follows.

- [ ] **Step 1: Write the new workflow.md**

Replace the entire content of `.claude/skills/catalog-detector/references/workflow.md` with the content below. This is the complete file — do not merge with the old content.

```markdown
# Catalog Detector Workflow

**Input:** Company URL + category classification from the company report
**Output:** Catalog assessment with extraction blueprint

---

## Context

This workflow produces a concrete extraction blueprint that the scraper-generator can translate directly into code. It minimizes downstream investigation by leveraging platform-specific knowledge from the platform knowledgebase.

The workflow splits into two tracks after platform detection:

- **Fast path** — for known platforms with an existing knowledgebase file. Loads the known extraction recipe, verifies it works on this specific site, fills in site-specific values. Skips most investigation.
- **Deep investigation** — for custom/unknown platforms, or when the fast path fails. Full site investigation to discover extraction patterns from scratch.

Both tracks produce the same output format: a catalog assessment where the extraction blueprint is the primary content.

### Investigation vs. scraping constraint

This workflow can use any available tools during investigation — including rendering pages in a browser, observing network requests, and inspecting JavaScript behavior. The purpose is to discover how the site delivers product data.

However, the **scraping strategy recommended by this workflow** must be executable with simple HTTP request libraries (httpx, requests) plus HTML/JSON/PDF parsing. The recommended scraping strategy must work without a headless browser. So the investigation goal is: find a path to product data that works without JavaScript rendering — static HTML, JSON-LD, an internal API, or a downloadable file.

### Platform knowledgebase ownership

This workflow owns the platform knowledgebase (`docs/platform-knowledgebase/`). It reads on every run and writes on every successful run. The knowledgebase captures platform-level patterns (API endpoints, CSS selectors, pagination, pitfalls) that apply to any site on that platform — not site-specific quirks.

---

## Step 1: Platform Detection

Read the company report to get the company's website URL, subcategory taxonomy IDs, business model, and any notes about the online presence.

Fetch the company's homepage and identify the CMS or e-commerce platform. Check these signals:
- HTML meta generators (e.g., `<meta name="generator" content="WooCommerce">`)
- Known path patterns (`/wp-content/` for WordPress/WooCommerce, `/cdn.shopify.com/` for Shopify, `/static/version` for Magento)
- JavaScript globals and CSS class naming conventions
- Response headers (`X-Powered-By`, `X-Shopify-Stage`)

Record the platform using one of these values: `woocommerce`, `shopify`, `magento`, `prestashop`, `opencart`, `bigcommerce`, `squarespace`, `wix`, `drupal`, `custom`, `unknown`. This is a closed enumeration — if the platform is recognizable but not on this list, record `custom`. The slug is always lowercase, no spaces or special characters.

Also during this step, examine the homepage for evidence of a public product catalog:
- Look for navigation elements pointing to "Products", "Shop", "Catalog", "Price List", or equivalent terms
- Fetch `/robots.txt` for crawl permissions and sitemap references
- Fetch `/sitemap.xml` (and any sitemaps from robots.txt) — look for product URL patterns, estimate product count

**Track routing:** If the detected platform has a knowledgebase file at `docs/platform-knowledgebase/{platform-slug}.md`, proceed to Step 2 (Fast Path). Otherwise, proceed to Step 3 (Deep Investigation).

---

## Step 2: Fast Path (Known Platforms)

This track applies when a platform knowledgebase file exists.

### Step 2a: Load Platform Knowledgebase

Read the platform knowledgebase file. Extract the known extraction recipe:
- API endpoints and their parameters
- CSS selectors for product data (links, prices, names, breadcrumbs, spec tables)
- Pagination patterns (URL format, products per page, next-page detection)
- Common pitfalls and their resolutions

### Step 2b: Verify Recipe on This Site

Spot-check 2-3 product pages across different categories using the known patterns. Apply these pass/fail criteria:

- **API verification passes** if the endpoint returns HTTP 200 with product data containing at least name and price fields.
- **CSS selector verification passes** if the selectors extract non-empty text on all checked pages.
- **Pagination verification passes** if the URL pattern fetches page 2 successfully and returns a different set of products than page 1.

Any single verification failure triggers `platform_recipe_failed` — see the decision. The deep investigation path starts from Step 3b (Catalog Discovery) — platform detection does not repeat. Carry forward information about which patterns didn't work.

Record any deviations from the knowledgebase that don't constitute failures (e.g., additional CSS classes, slightly different field names, theme-specific variations).

### Step 2c: Build Extraction Blueprint

Fill in the site-specific values using the verified knowledgebase patterns:

1. **Data source** — which method works (API endpoint, JSON-LD, static HTML), with concrete endpoint URLs and parameters for this site.
2. **Product discovery** — how to find all products: discovery method, pagination URL pattern with this site's format, products per page.
3. **Verified category tree** — crawl the category tree starting from top-level categories found in Step 1. For each node: category path, exact URL, product count (for leaf nodes), depth level. Circuit breaker: stop at 100 nodes or depth 5.
4. **Product data extraction** — for each extraction point (price, name, SKU, spec table, breadcrumb), record the concrete selector or API path that was verified in Step 2b. Include 2-3 verified product URLs with actual extracted values.
5. **Sample attribute labels** — collect every unique attribute label from spec tables across 3-5 inspected product pages. Record: exact label text, frequency, one example value.

### Step 2d: Determine Scraping Strategy

Select exactly one strategy based on findings:

| Strategy | When to select |
|----------|---------------|
| `static_html` | Products in initial HTML, scrapable with simple HTTP requests + HTML parsing |
| `structured_data` | JSON-LD product data is rich and complete, or an internal JSON API returns full product listings via direct HTTP request |
| `pdf_pricelist` | Products are only available as a downloadable PDF catalog or price list |

If multiple strategies could work, prefer: `structured_data` > `static_html` > `pdf_pricelist`.

### Step 2e: Estimate Product Count

Estimate total products using the most reliable method:
- Sitemap product URL count
- "Showing X of Y results" text on listing pages
- Last page number multiplied by products per page
- Sum of product counts across leaf categories
- API response metadata (total count fields)

Record the estimation method alongside the number.

### Step 2f: Write Catalog Assessment

Write the catalog assessment using the success template (see Report Templates below). Proceed to Step 4 (Update Platform Knowledgebase).

---

## Step 3: Deep Investigation (Custom/Unknown Platforms)

This track applies when the platform is `custom`, `unknown`, or when the fast path fails via `platform_recipe_failed`.

### Step 3a: Anti-Bot Check

Before deep investigation, assess anti-bot measures:
- **None detected:** Standard HTTP responses, no challenges
- **Light:** Rate limiting, basic user-agent checks (manageable with respectful delays and proper headers)
- **Moderate:** Cookie-based bot detection, JavaScript challenges. If the only path to product data requires resolving these (no structured-data fallback), stop — see the `js_only` decision. If product data is accessible via API or JSON-LD without triggering these measures, record severity as `moderate` and proceed.
- **Severe:** CAPTCHA walls, Cloudflare Under Attack mode, DataDome, PerimeterX, or similar. Stop — see the `anti_bot_severe` decision.

### Step 3b: Catalog Discovery

Navigate to the most promising product listing area found in Step 1. If no obvious entry point was found, try common paths: `/products`, `/shop`, `/catalog`, `/collections`, `/prices`, `/pricelist`.

For each candidate listing page:
- Confirm it displays multiple products with at least some visible attributes (name, price, image)
- Note the URL pattern for individual product pages
- Note the URL pattern for category/listing pages

If no public product listing is found:
- Check for PDF price lists or downloadable catalogs. If found, this becomes the `pdf_pricelist` strategy.
- Check for product data behind login/registration walls. If gated, stop — see the `auth_required` decision.

If nothing yields a catalog, stop — see the `no_public_catalog` decision.

### Step 3c: Technical Assessment

#### Rendering Method
Load a product listing page and determine how content is delivered:
- **Static HTML:** Products present in initial HTML response.
- **Structured data available:** Even if the page renders via JavaScript, check for JSON-LD, microdata, or API endpoints that return product data as JSON.
- **JavaScript-rendered (no structured data fallback):** Products appear only after JavaScript executes, and no JSON-LD, microdata, or API endpoints provide the data via simple HTTP requests. Stop — see the `js_only` decision.

#### Structured Data and API Discovery

This is the most important investigation step. Even when the visible page requires JavaScript, the underlying data often comes from an API callable directly. Invest real effort here before concluding a site is not scrapable.

Check for machine-readable product data in this order:
1. **JSON-LD in page source** — `<script type="application/ld+json">` blocks with Product or ItemList schemas.
2. **Microdata** — `itemscope itemtype="https://schema.org/Product"` attributes.
3. **Internal APIs** — load the page in a browser and observe network requests. Look for XHR/fetch calls returning product data as JSON. Test whether they work as standalone HTTP requests.
4. **If API found** — document URL pattern, parameters, authentication requirements, response structure.

If an API or JSON-LD provides complete product data via direct HTTP, classify as `structured_data` strategy. Only stop if no such fallback exists.

### Step 3d: Product Attribute Extractability Check

Open 3-5 individual product pages across different categories and check:
- Are product attributes present as structured text (discrete fields like name, price, weight)?
- Or are they trapped in non-scrapable formats (images, PDFs, unstructured prose)?

If extraction is not feasible, stop — see the `attributes_not_extractable` decision.

While inspecting, also record extraction metadata:

**Price extraction method** — check in this order on raw HTML:
1. JSON-LD `<script type="application/ld+json">` with a `price` field
2. Price-related CSS classes (`.price`, `.product-price`, `.current-price`) with numeric text
3. `dataLayer.push(` containing `"price"`
4. Network requests for API calls returning price data

Record which method succeeded and the specific extraction pattern.

**Spec table selectors** — container, row iterator, label cell, value cell.

**Product name selector** — CSS selector for the main heading.

**SKU/reference location** — where the product identifier appears.

**Breadcrumb selector** — CSS selector for category breadcrumb navigation.

**Sample attribute labels** — every unique label from spec tables across inspected pages with frequency and example value.

### Step 3e: Build Extraction Blueprint

Same output as the fast path (Step 2c), but everything discovered from scratch. Build the verified category tree, determine pagination, record all selectors and verified examples.

**Verified category tree:** Starting from each top-level category:
1. Fetch the category page
2. Identify child category links
3. If children exist, recurse
4. If no children (leaf node), count product links
5. Record: category path, exact URL, product count, depth

Circuit breaker: stop at 100 nodes or depth 5.

### Step 3f: Determine Scraping Strategy

Same as Step 2d — select `static_html`, `structured_data`, or `pdf_pricelist`.

### Step 3g: Estimate Product Count

Same as Step 2e.

### Step 3h: Write Catalog Assessment

Write the catalog assessment using the success template (see Report Templates below). Proceed to Step 4 (Update Platform Knowledgebase).

---

## Step 4: Update Platform Knowledgebase

After writing the catalog assessment, update the platform knowledgebase. Skip for `unknown` or `custom` platforms unless the site is an identifiable CMS not yet in the enumeration (see criteria below).

### For known platforms (knowledgebase file exists)

1. **Append to Sites table** — add a row with: company name, slug, date, and 1-2 sentence summary of notable observations (theme name, product count, deviations).
2. **Add pattern corrections** — compare verified/discovered patterns against knowledgebase content:
   - A selector that doesn't work on this site's theme → add to Common Pitfalls with the theme name and working alternative
   - A new API endpoint pattern → add to the relevant section
   - A theme-specific variation → document in CSS Selectors with a theme qualifier
   - A fast-path failure (`platform_recipe_failed`) → add to Common Pitfalls explaining what didn't work and why

### For newly identified platforms (deep investigation path)

Create a new knowledgebase file if the site uses a recognizable CMS with consistent conventions across installations — identifiable via meta generators, known path patterns, or response headers. If the site is a bespoke build with no reusable patterns, skip.

New knowledgebase file template:

```markdown
# Platform: {Platform Name}

## JSON-LD Patterns
{What JSON-LD schemas are present, field mappings, known quirks}

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

### Rules

- **Additive, not destructive** — never remove patterns that worked for other sites.
- **Site-specific quirks stay in the catalog assessment**, not the knowledgebase. The knowledgebase captures platform-level patterns.

---

## Step 5: Self-Verification

Before presenting results, re-read the catalog assessment and check it against these quality gates. If any gate fails, fix the issue before proceeding.

### Success report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Correct template used** | Success template for scrapable catalogs, stop template for stop decisions |
| 2 | **Heading and slug present** | `# Catalog Assessment: {Company Name}` with correct slug |
| 3 | **Scraping strategy is valid** | One of: `static_html`, `structured_data`, `pdf_pricelist` |
| 4 | **Platform field present and valid** | One of the platform enumeration values |
| 5 | **Data source is concrete** | Primary method specified with actual endpoint/selector, not placeholders |
| 6 | **Product discovery is actionable** | Discovery method, pagination pattern, and products per page all specified |
| 7 | **Verified category tree is complete** | Every leaf category that maps to a taxonomy subcategory has a row with verified URL and product count > 0 |
| 8 | **Price method is verified** | At least 2 product URLs with actual extracted price values |
| 9 | **Spec table selectors verified** | At least 2 product URLs with attribute counts |
| 10 | **Product count has estimation method** | Number followed by method in parentheses |
| 11 | **Platform knowledgebase updated** | Sites table appended (known platforms) or new file created (newly identified platforms) |
| 12 | **Anti-bot uses exact value** | One of: `none`, `light`, `moderate` |

### Stop report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Stop template used** | Header fields include `Scraping strategy: none` and `Stop reason:` |
| 2 | **Stop reason is a valid decision name** | One of: `no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, `attributes_not_extractable` |
| 3 | **Findings explain why** | `## Findings` section describes what was found and why scraping is not viable |

---

## Report Templates

### Success template

```markdown
# Catalog Assessment: {Company Name}

**Slug:** {slug}
**Assessment date:** {date}
**Catalog found:** yes
**Scraping strategy:** static_html | structured_data | pdf_pricelist
**Platform:** {platform-slug}
**Anti-bot:** none | light | moderate {one-line mitigation note if needed}
**Estimated product count:** {number} ({estimation method})
**Currency:** {ISO 4217}

## Extraction Blueprint

### Data Source
- **Primary method:** {api_endpoint | static_html_css | json_ld | pdf}
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
- **Method:** {static_html_css | json_ld | dataLayer | api_endpoint}
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

Use when any stop decision is triggered.

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
| **Report starts with `#` heading** | `# Catalog Assessment: {Company Name}` | `## Catalog Assessment` (no H1), missing company name |
| **Slug matches the company slug from product-classifier** | `festool` | Company name, URL, or different slug |
| **Scraping strategy is a valid value** | `static_html`, `structured_data`, `pdf_pricelist`, or `none` | `headless_browser`, free-text descriptions |
| **Stop reports use the stop template** | `**Stop reason:** auth_required` with `## Findings` | Success template with empty sections |
| **Success reports have Extraction Blueprint** | `## Extraction Blueprint` with all subsections | Missing blueprint, survey-style sections instead |
| **Anti-bot uses exact values (success reports)** | `none`, `light`, `moderate` | `severe` (should be a stop), free-text, `low`/`high` |
| **Sections use `##` headings** | `## Extraction Blueprint` | `###` or other heading levels for top-level sections |
| **Platform uses closed enumeration** | `woocommerce`, `shopify`, `magento`, etc. | Free-text names, `WordPress`, `WooCommerce` (wrong case) |

---

## Boundaries

- This workflow produces extraction blueprints — it does not generate scrapers (scraper-generator) or classify companies (product-classifier).
- It does not test actual data extraction at scale — it verifies selectors on a few pages.
- It does not modify the product taxonomy or SKU schemas.
- It owns the platform knowledgebase — it reads and writes it on every successful run.

---

## Decisions

### Decision: no_public_catalog

**Context:** The site has no product listing pages, no downloadable catalog, and no discoverable product data. The company may sell products but does not expose them publicly online.
**Autonomous resolution:** Stop. Write a catalog assessment using the stop template with `Catalog found: no` and `Stop reason: no_public_catalog`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: auth_required

**Context:** A product catalog exists but is gated behind authentication — prices hidden until login, "dealer only" portals, registration-required storefronts.
**Autonomous resolution:** Stop. Write a catalog assessment using the stop template with `Stop reason: auth_required`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: anti_bot_severe

**Context:** Commercial bot protection (CAPTCHA walls, DataDome, PerimeterX, Cloudflare Under Attack, or equivalent) actively blocks automated access to product pages. Light or moderate measures do not trigger this — only protection that makes reliable daily scraping non-viable.
**Autonomous resolution:** Stop. Write a catalog assessment using the stop template with `Stop reason: anti_bot_severe`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: js_only

**Context:** The product catalog requires JavaScript rendering to display product data, and after thorough API discovery (observing network requests, checking JSON-LD, testing API endpoints), no structured data fallback was found that works via simple HTTP request. This also applies when anti-bot measures require JavaScript execution to resolve (cookie-based detection, JS challenges) and no alternative data path exists. This merges the former `requires_headless_browser` and `spa_not_scrapable` decisions.
**Autonomous resolution:** Stop. Write a catalog assessment using the stop template with `Catalog found: yes`, `Scraping strategy: none`, and `Stop reason: js_only`. Describe what was investigated: which API endpoints were checked, what network requests were observed, and why none provide product data without a browser.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: attributes_not_extractable

**Context:** The catalog exists and products are listable, but product attributes are not present in a scrapable form. Attributes may be trapped in images, locked inside downloadable PDFs, rendered as unstructured prose, or only visible after interactive product configuration.
**Autonomous resolution:** Stop. Write a catalog assessment using the stop template with `Catalog found: yes`, `Scraping strategy: none`, and `Stop reason: attributes_not_extractable`.
**Escalate when:** Never.
**Escalation payload:** N/A

### Decision: platform_recipe_failed

**Context:** The platform knowledgebase recipe doesn't work on this specific site — API returns 403, CSS selectors don't match, pagination pattern fails. The site uses a known platform but is too heavily customized for the standard recipe.
**Autonomous resolution:** Fall back to the deep investigation path (Step 3). Start from Step 3b (Catalog Discovery) — platform detection does not repeat. Carry forward information about which patterns didn't work and record them in the Platform-Specific Notes of the final report. Add the failure to the platform knowledgebase Common Pitfalls section.
**Escalate when:** Never. This is a track switch, not a stop.
**Escalation payload:** N/A
```

- [ ] **Step 2: Check word count**

Run: `wc -w .claude/skills/catalog-detector/references/workflow.md`

Expected: under ~3,500 words. If over 3,500, consider extracting fast path and deep investigation into separate reference files.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/catalog-detector/references/workflow.md
git commit -m "Rewrite catalog-detector workflow for two-track platform-first design"
```

---

## Chunk 2: Downstream consumer updates

### Task 3: Update product-discovery orchestrator

**Files:**
- Modify: `.claude/skills/product-discovery/SKILL.md:68-74`

- [ ] **Step 1: Update Stage 2 stop conditions**

Replace lines 68-74 of `.claude/skills/product-discovery/SKILL.md`:

```markdown
**Stop the pipeline if:**
- No public catalog is found (`Catalog found: no`)
- The catalog is behind authentication
- Severe anti-bot protection makes scraping non-viable
- The site requires a headless browser (JavaScript rendering with no structured data fallback)
- The site is a heavy SPA where products require complex user interaction to surface
- Product attributes are not extractable from product pages in a structured, scrapable form
```

With:

```markdown
**Stop the pipeline if:**
- No public catalog is found (`Catalog found: no`)
- The catalog is behind authentication
- Severe anti-bot protection makes scraping non-viable
- The site requires JavaScript rendering with no structured data fallback (`js_only`)
- Product attributes are not extractable from product pages in a structured, scrapable form
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/product-discovery/SKILL.md
git commit -m "Update product-discovery Stage 2 stop conditions for js_only decision"
```

---

### Task 4: Update scraper-generator orchestrator references

**Files:**
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md:100`
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md:157`

- [ ] **Step 1: Update Step 1 (Load Context) catalog assessment extraction description**

In `.claude/skills/scraper-generator/references/orchestrator.md`, find line 100:

```
Read the catalog assessment and extract: scraping strategy (`static_html`, `structured_data`, `pdf_pricelist`), catalog structure (categories, navigation paths, pagination patterns), estimated product count, catalog entry points, anti-bot notes, and platform (e.g., `woocommerce`, `shopify`, `unknown`).
```

Replace with:

```
Read the catalog assessment and extract: scraping strategy (`static_html`, `structured_data`, `pdf_pricelist`), platform, estimated product count, anti-bot severity, and currency from the header metadata. Read the `## Extraction Blueprint` section for the data source (API endpoints, selectors), product discovery (pagination, verified category tree), product data extraction (price, name, SKU, spec table, breadcrumb selectors with verified examples), and platform-specific notes.
```

- [ ] **Step 2: Update Step 2a extraction blueprint label reference**

In the same file, find the text at line 157:

```
2. **Extraction blueprint sample labels** — the catalog assessment's extraction blueprint contains sample attribute labels from 3-5 product pages. Map each label to a schema key using the attribute routing tables from Step 2a.
```

Replace with:

```
2. **Extraction blueprint sample labels** — the catalog assessment's `## Extraction Blueprint > ### Product Data Extraction > #### Sample Attribute Labels` table contains sample attribute labels from 3-5 product pages. Map each label to a schema key using the attribute routing tables from Step 2a.
```

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/scraper-generator/references/orchestrator.md
git commit -m "Update scraper-generator orchestrator to reference new catalog assessment structure"
```

---

### Task 5: Update scraper-generator validator reference

**Files:**
- Modify: `.claude/skills/scraper-generator/references/validator.md:13`

- [ ] **Step 1: Update catalog_structure field description**

In `.claude/skills/scraper-generator/references/validator.md`, find line 13:

```
| `catalog_structure` | object | Categories, navigation paths, and top-level category list from the catalog assessment |
```

Replace with:

```
| `catalog_structure` | object | Verified Category Tree and Product Discovery section from the catalog assessment's Extraction Blueprint |
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/scraper-generator/references/validator.md
git commit -m "Update validator catalog_structure description for new catalog assessment format"
```

---

## Chunk 3: Verification and codebase sweep

### Task 6: Retire old decision names across codebase

**Files:**
- Search all files under `.claude/skills/` for `requires_headless_browser` and `spa_not_scrapable`

- [ ] **Step 1: Search for remaining old decision name references**

Run:
```bash
grep -r "requires_headless_browser\|spa_not_scrapable" .claude/skills/ --include="*.md"
```

Expected: zero matches (all references should have been updated in Tasks 1-5). If any remain, update them to `js_only`.

- [ ] **Step 2: Commit if changes were needed**

```bash
git add -A .claude/skills/
git commit -m "Remove remaining old decision name references (requires_headless_browser, spa_not_scrapable)"
```

Skip this commit if no changes were needed.

---

### Task 7: Run convention verification

**Files:**
- No modifications — verification only

- [ ] **Step 1: Run the skill verification script**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py catalog-detector`

Expected: all checks pass (exit code 0).

- [ ] **Step 2: Fix any failures**

If the verification script reports failures, fix them in the relevant file (SKILL.md or workflow.md). Common issues:
- Missing required sections
- Decision blocks not matching expected format
- Logical resource names not mapped
- Word count warning (informational, not blocking)

- [ ] **Step 3: Re-run verification after fixes**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py catalog-detector`

Expected: all checks pass.

- [ ] **Step 4: Run full verification across all skills**

Run: `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all`

Expected: all skills pass. The product-discovery and scraper-generator changes should not break their own verification.

- [ ] **Step 5: Commit any fixes**

```bash
git add -A .claude/skills/
git commit -m "Fix convention compliance issues from skill verification"
```

Skip this commit if no fixes were needed.

---

### Task 8: Final review commit

- [ ] **Step 1: Verify git status is clean**

Run: `git status`

Expected: all changes committed, working tree clean.

- [ ] **Step 2: Review the full diff from this branch**

Run: `git diff main...HEAD --stat`

Verify that only these files were changed:
- `.claude/skills/catalog-detector/SKILL.md`
- `.claude/skills/catalog-detector/references/workflow.md`
- `.claude/skills/product-discovery/SKILL.md`
- `.claude/skills/scraper-generator/references/orchestrator.md`
- `.claude/skills/scraper-generator/references/validator.md`
- `docs/superpowers/specs/2026-03-17-catalog-detector-redesign.md`
- `docs/superpowers/plans/2026-03-17-catalog-detector-redesign.md`
