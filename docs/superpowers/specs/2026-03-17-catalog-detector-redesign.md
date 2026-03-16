# Catalog Detector Redesign: Platform-First Extraction Blueprints

## Problem

The catalog-detector skill produces a survey-style report that describes what a site looks like rather than telling the scraper-generator exactly how to extract data from it. This forces the scraper-generator to rediscover API endpoints, selectors, pagination patterns, and category structures — work the catalog-detector already did but captured in prose rather than actionable detail.

For known platforms (Shopify, WooCommerce, PrestaShop, etc.), the problem is worse: the platform knowledgebase already contains extraction recipes, but catalog-detector treats it as optional reading rather than the primary source of strategy.

The result is wasted LLM time downstream, unnecessary probe-fix cycles in the scraper-generator, and a platform knowledgebase that grows slowly because nothing actively maintains it.

## Goal

Redesign catalog-detector so that its output (the catalog assessment) is a concrete extraction blueprint that the scraper-generator can translate directly into code — minimizing downstream investigation and probe-fix cycles.

**Success metric:** For known platforms, the scraper-generator's first probe pass should succeed without selector/API discovery — it's translating the blueprint into Python.

## Design

### Two-Track Workflow

The workflow splits after platform detection into a fast path (known platforms) and a deep investigation path (custom/unknown platforms). Both tracks produce the same output format.

#### Fast Path (known platforms)

Applies when the detected platform has a knowledgebase file in `docs/platform-knowledgebase/{platform-slug}.md`.

1. **Detect platform** — fetch homepage, check meta generators, known path patterns, headers, JS globals. Result: one of the platform enumeration values.
2. **Load platform knowledgebase** — read the known extraction recipe: API endpoints, CSS selectors, pagination patterns, common pitfalls.
3. **Verify recipe on this site** — spot-check 2-3 product pages using the known patterns. Pass/fail criteria:
   - **API verification passes** if the endpoint returns HTTP 200 with product data containing at least name and price fields.
   - **CSS selector verification passes** if the selectors extract non-empty text on all checked pages (2-3 pages across different categories).
   - **Pagination verification passes** if the URL pattern fetches page 2 successfully and returns a different set of products than page 1.
   - Any single verification failure triggers `platform_recipe_failed` (track switch).
   - Record any deviations from the knowledgebase that don't constitute failures (e.g., additional CSS classes, slightly different field names).
4. **Build site-specific extraction blueprint** — fill in the knowledgebase template with this site's concrete values: actual category URLs, actual product count, actual currency, any site-specific quirks discovered in verification.
5. **Update platform knowledgebase** — see Platform Knowledgebase Maintenance section below for mechanics.
6. **Write catalog assessment** — the extraction blueprint is the primary content.
7. **Self-verification** — check the report against quality gates.

**Track switch:** If verification fails (API returns 403, selectors don't match, site heavily customized), trigger `platform_recipe_failed` and fall back to the deep investigation path. This is not a stop — it's a track switch. The deep investigation path starts from Step 2 (catalog discovery) — platform detection does not repeat. Any information gathered during the failed fast path (which patterns didn't work, which pages were checked) is carried forward and recorded in the Platform-Specific Notes section of the final report. The failure is also added to the platform knowledgebase Common Pitfalls section (e.g., "Site X uses a heavily customized Shopify theme — standard selectors did not match").

#### Deep Investigation Path (custom/unknown platforms)

Applies when the platform is `custom`, `unknown`, or when the fast path fails via `platform_recipe_failed`.

1. **Detect platform** — same as above, result is `custom`/`unknown` (or already detected if arriving via track switch).
2. **Catalog discovery** — find product listing pages via navigation, common paths, sitemaps.
3. **Technical assessment** — rendering method, structured data/API discovery, anti-bot assessment.
4. **Product attribute extractability check** — inspect 3-5 product pages for structured attribute data.
5. **Build extraction blueprint** — same output format as fast path, but everything discovered from scratch: selectors, API endpoints, pagination, category tree, price extraction, sample attributes.
6. **Seed platform knowledgebase** — see Platform Knowledgebase Maintenance section below for mechanics. Criteria for creating a new knowledgebase file: the site uses a recognizable CMS that has consistent conventions across installations (e.g., OpenCart, BigCommerce) — identifiable via meta generators, known path patterns, or response headers. If the site is a bespoke build with no reusable patterns, skip.
7. **Write catalog assessment**
8. **Self-verification** — check the report against quality gates.

### Output: Restructured Catalog Assessment

The extraction blueprint moves from a buried appendix to the primary content. Survey-style sections are either absorbed into the blueprint or dropped.

#### Success template

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
- **Price variants:** {description if applicable, e.g., "variable products use lowPrice from AggregateOffer"}

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

#### Stop template

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

### Platform Knowledgebase Maintenance

Catalog-detector owns the platform knowledgebase. It reads on every run and writes on every successful run.

**Read:** After detecting the platform, load `docs/platform-knowledgebase/{platform-slug}.md`. Use its patterns as the starting point for the extraction blueprint.

**Write — happens after writing the catalog assessment and before self-verification.** Two types of updates:

1. **Sites table** — always append a row with: company name, slug, date, and 1-2 sentence summary of notable observations (theme name, product count, any deviations from standard patterns).
2. **Pattern corrections/additions** — compare what was verified/discovered against what the knowledgebase contains. If verification reveals new information:
   - A selector that doesn't work on this site's theme → add to Common Pitfalls with the theme name and working alternative
   - A new API endpoint pattern → add to the relevant section
   - A theme-specific variation (e.g., different breadcrumb selector) → document in CSS Selectors with a theme qualifier
   - A fast-path failure (`platform_recipe_failed`) → add to Common Pitfalls explaining what didn't work and why

**Rules:**
- Additive, not destructive — never remove patterns that worked for other sites
- Site-specific quirks stay in the catalog assessment, not the knowledgebase. The knowledgebase captures platform-level patterns that apply to any site on that platform.
- New platforms — if a custom/unknown site is an identifiable CMS (recognizable via meta generators, known path patterns, or response headers with consistent conventions), create a new knowledgebase file using this template:

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

**Existing format preserved:** The three existing knowledgebase files (shopify.md, woocommerce.md, prestashop.md) already follow this structure.

### Section Migration

How current report sections map to the new structure:

| Current Section | New Location |
|---|---|
| Catalog Entry Points | Absorbed into "Product Discovery > Discovery method" and Verified Category Tree |
| Category Structure | Absorbed into Verified Category Tree |
| URL Path Patterns | Absorbed into Verified Category Tree URLs |
| Pagination | Absorbed into "Product Discovery" subsection |
| Structured Data | Absorbed into "Data Source" subsection |
| Navigation Paths | Dropped — the blueprint's category tree + pagination makes this redundant |
| Anti-Bot Details | Compressed to top-level `Anti-bot:` metadata field with one-line mitigation note |
| Notes | Absorbed into "Platform-Specific Notes" subsection |
| Extraction Blueprint (appendix) | Promoted to `## Extraction Blueprint` — the primary content |

The `Anti-bot` field drops `severe` from inline values because severe anti-bot is a stop condition — it never appears in a success report.

### Self-Verification Quality Gates

#### Success report gates

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
| 11 | **Platform knowledgebase updated** | Sites table has been appended (for known platforms) or new file created (for newly identified platforms) |
| 12 | **Anti-bot uses exact value** | One of: `none`, `light`, `moderate` |

#### Stop report gates

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Stop template used** | Header fields include `Scraping strategy: none` and `Stop reason:` |
| 2 | **Stop reason is a valid decision name** | One of: `no_public_catalog`, `auth_required`, `anti_bot_severe`, `js_only`, `attributes_not_extractable` |
| 3 | **Findings explain why** | `## Findings` section describes what was found and why scraping is not viable |

### Decisions

Five autonomous stops + one track-switch:

| Decision | Type | Trigger |
|---|---|---|
| `no_public_catalog` | Stop | No catalog found anywhere on the site |
| `auth_required` | Stop | Catalog behind login/registration |
| `anti_bot_severe` | Stop | CAPTCHA/DataDome/PerimeterX blocking access |
| `js_only` | Stop | JS-rendered, no structured data fallback (merges `requires_headless_browser` + `spa_not_scrapable`) |
| `attributes_not_extractable` | Stop | Attributes in non-scrapable format (images, PDFs, prose) |
| `platform_recipe_failed` | Track switch | Knowledgebase recipe doesn't work on this site → fall back to deep investigation |

All stops are autonomous — no user escalation. The track switch is also autonomous.

### Downstream Impact

The scraper-generator is the primary consumer of the catalog assessment. It reads the report as free-form text and extracts specific fields: scraping strategy, catalog structure (categories, navigation paths, pagination patterns), estimated product count, catalog entry points, anti-bot notes, platform, and the extraction blueprint.

**This is a coordinated change.** The scraper-generator's references must be updated in the same changeset to read the new template format:

1. **`references/orchestrator.md`** — Step 1 (Read inputs) currently says "extract: scraping strategy, catalog structure (categories, navigation paths, pagination patterns), estimated product count, catalog entry points, anti-bot notes, and platform." Update to reference the new section names: `## Extraction Blueprint > ### Data Source`, `### Product Discovery`, `### Product Data Extraction`, `### Platform-Specific Notes`.
2. **`references/orchestrator.md`** — Step 2a currently references "extraction blueprint sample labels." Update the path description to match the new location (`## Extraction Blueprint > ### Product Data Extraction > #### Sample Attribute Labels`).
3. **`references/orchestrator.md`** — Step 3 references "the extraction blueprint from the catalog assessment for verified selectors." This still works — the section is now more prominent, not renamed.
4. **`references/validator.md`** — the `catalog_structure` input field description references "Categories, navigation paths, and top-level category list from the catalog assessment." Update to reference "Verified Category Tree and Product Discovery section."
5. **`references/code-generator.md`** — references to "catalog assessment" for navigation paths, category structure, and sitemap remain valid — the information is still present, just in different sections.

**product-discovery orchestrator** — update Stage 2 stop conditions:
- Replace "The site requires a headless browser (JavaScript rendering with no structured data fallback)" and "The site is a heavy SPA where products require complex user interaction to surface" with a single line: "The site requires JavaScript rendering with no structured data fallback (`js_only`)"

### Workflow Decomposition

The current workflow is ~3,200 words and the redesigned version will be larger due to two tracks. Per convention (decomposition at ~3,000 words), the workflow decomposes into an orchestrator + inline track descriptions.

**File layout:**

```
.claude/skills/catalog-detector/
├── SKILL.md                          ← Skill entry point (unchanged structure)
└── references/
    └── workflow.md                   ← Orchestrator with both tracks inline
```

The two tracks share enough structure (same output format, same decisions, same verification gates) that splitting into separate sub-agent files would create duplication. Instead, workflow.md uses the orchestrator pattern with clearly labeled track sections:

- `## Context` — purpose, two-track overview
- `## Step 1: Platform Detection` — shared entry point
- `## Step 2: Fast Path` — Steps 2-6 for known platforms (subsections: Load Knowledgebase, Verify Recipe, Build Blueprint, Update Knowledgebase, Write Report)
- `## Step 3: Deep Investigation` — Steps 2-7 for custom/unknown (subsections: Catalog Discovery, Technical Assessment, Extractability Check, Build Blueprint, Seed Knowledgebase, Write Report)
- `## Step 4: Self-Verification` — shared quality gates
- `## Report Templates` — success + stop templates with strict format rules
- `## Boundaries`
- `## Decisions` — all 6 decision blocks

If the final word count exceeds ~3,500 after implementation, the fast path and deep investigation tracks can be extracted into `references/fast-path.md` and `references/deep-investigation.md` as sub-agent specs. But attempt the single-file approach first.

### Convention Compliance

**SKILL.md changes:**
- Rewrite one-line summary to reflect extraction blueprint purpose
- Update file locations table: platform knowledgebase marked as read+write (not read-only), add note about new file creation for unknown platforms
- Update stop behavior list (5 stops + 1 track-switch)
- Add note about platform knowledgebase ownership

**workflow.md changes:**
- Rewrite Context section to articulate two-track purpose and platform knowledgebase ownership
- Restructure steps into platform detection → fast path / deep investigation → self-verification
- Update report template to new extraction-blueprint-first structure
- Replace self-verification quality gates with the new gates from this spec
- Update Decisions section: merge `requires_headless_browser` + `spa_not_scrapable` into `js_only`, add `platform_recipe_failed`
- Update Boundaries to include knowledgebase write responsibility

**product-discovery SKILL.md changes:**
- Update Stage 2 stop conditions to use `js_only` instead of the two old decision names

**scraper-generator reference changes:**
- Update section name references in orchestrator.md and validator.md as described in Downstream Impact

**Decision name retirement:** The old names `requires_headless_browser` and `spa_not_scrapable` are retired. All references across the codebase must be updated to `js_only`.

**Verification:** `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py catalog-detector` must pass after implementation.

### What Doesn't Change

- Pipeline position: still runs after product-classifier, before scraper-generator
- Input: company slug
- Output path: `docs/catalog-detector/{slug}.md`
- Platform enumeration values
- Scraping strategy values: `static_html`, `structured_data`, `pdf_pricelist`
- File-driven skill — no database or external services
