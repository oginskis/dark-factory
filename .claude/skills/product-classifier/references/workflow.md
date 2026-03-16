# Product Classifier Workflow

**Input:** Company name or URL
**Output:** Company profile report, or escalation

---

## Context

Resolve a company name or URL into a classified company profile focused on tangible, physical goods. This workflow decides whether a company belongs in the pipeline, assigns it a canonical taxonomy classification, and produces a structured report. It does not interact conversationally -- it makes decisions and either completes the classification or escalates.

---

## Step 1: Resolve Company Identity and Derive Slug

Given the input, determine whether it is a URL or a company name.

**If URL:** Extract the hostname and resolve the company from the site.

**If company name:** Search the web for the company name to find its official website.

### Slug derivation

The slug is derived from the company's primary domain name. This is deterministic — the same company must always produce the same slug, regardless of how the input was phrased.

**Algorithm:**

1. Take the company's official website hostname (e.g., `www.festool.com`, `shop.bosch.de`)
2. Strip any subdomain prefix (`www.`, `shop.`, `store.`, etc.) to get the registrable domain (e.g., `festool.com`, `bosch.de`)
3. Drop the TLD — everything from the last dot onward for single-part TLDs (`.com`, `.de`, `.fr`), or the last two segments for known multi-part TLDs (`.co.uk`, `.com.au`, `.co.jp`)
4. What remains is the slug. Keep hyphens. No further transformations.

**Examples:**

| Input | Official site | Slug |
|-------|--------------|------|
| `https://www.festool.com/products` | `festool.com` | `festool` |
| `Bosch` | `bosch.com` | `bosch` |
| `https://shop.3m.com` | `3m.com` | `3m` |
| `Johnson & Johnson` | `jnj.com` | `jnj` |
| `Marks & Spencer` | `marksandspencer.com` | `marksandspencer` |
| `Hilti UK` | `hilti.co.uk` | `hilti` |
| `RS Components` | `rs-online.com` | `rs-online` |

The slug is always derived from the domain, never from the display name. This avoids ambiguity — "Johnson & Johnson" could slugify to `johnson-johnson`, `johnson--johnson`, or `jnj` depending on the rules, but `jnj.com` always produces `jnj`.

If the company name resolves to multiple plausible companies, escalate — see the `ambiguous_company` decision.

---

## Step 2: Tangible Goods Gate

This is a hard go/no-go. Fetch the company's homepage and explore "About", "Products", or equivalent pages. Determine whether the company produces, manufactures, distributes, or sells any tangible, physical goods -- items you can touch, ship, and inventory.

**Pass** (proceed to Step 3): The company has physical products, even if it also offers services, software, or digital products alongside them. Examples: a furniture manufacturer, a food producer, an electronics retailer, a chemical supplier.

**Fail** (stop immediately): The company offers only services, software, SaaS, consulting, financial products, media, or purely digital goods. Do not produce a report. Report what the company does and why it was filtered out.

**Fail — general retailer / marketplace** (stop immediately): The company is an internet shop or marketplace that sells a wide variety of goods spanning many unrelated product domains (e.g., Amazon, eBay, AliExpress, Walmart.com, Temu). A general retailer that sells everything from electronics to clothing to groceries is out of scope — the product range is too broad for a meaningful classification. Do not produce a report. Explain that the company is a general retailer and suggest investigating a specific brand or manufacturer instead. This is a common-sense judgment — if the company is obviously a general retailer, reject it here without needing the product taxonomy categories file. Borderline cases proceed to Step 3 where the taxonomy provides a definitive answer.

This does **not** exclude focused resellers or distributors. A company that resells within one product domain passes (e.g., a power tool reseller, a plumbing supply distributor, a specialty food importer). A company with a clear primary product line plus supplementary accessories also passes (e.g., a cycling shop that also sells helmets, lights, and repair kits).

If the company's relationship to physical goods is unclear, escalate — see the `tangible_ambiguous` decision.

---

## Step 3: Classify into Taxonomy

Read the product taxonomy categories file. This file is the single source of truth for all category and subcategory values. Every value used in classification must appear in this file verbatim -- no paraphrasing, no invented categories, no abbreviations.

Each subcategory line in the product taxonomy categories file has a display name and a taxonomy ID in backticks. Extract taxonomy IDs using this regex pattern: `re.match(r'^- (.+?) \x60([a-z][a-z0-9_.]+)\x60$', line.strip())` — group 1 is the display name, group 2 is the taxonomy ID (e.g., `machinery.power_tools`).

**Unlimited subcategories.** A company gets one **Primary** subcategory and may have additional subcategories listed in **Subcategories**. There is no hard limit on the number of subcategories. Add every subcategory that genuinely describes a distinct product line the company offers — but do not pad the list with marginal matches or subcategories that merely overlap with the primary.

**Classification steps:**

1. Read the full product taxonomy categories file.
2. List every product category observed on the company's website during investigation — from navigation menus, category pages, and sitemaps. This is the exhaustive list of what the company sells. Do not filter yet.
3. For each observed category from step 2, search the product taxonomy categories file for a matching subcategory. Record matches (taxonomy ID + display name). Only exclude a match if the products are truly marginal (branded swag, gift cards, services, or consumables sold only as accessories to the main product). A dedicated catalog section with real physical products for sale is never marginal — if it has its own navigation entry, it is a distinct product line.
4. The **Subcategories** list is the union of all matches from step 3.
5. Identify the **primary** -- the single subcategory (by taxonomy ID) that best represents what the company is most known for or where it earns the most revenue.
6. Classification values must use the taxonomy ID with the display name in parentheses for readability. Example: `machinery.power_tools` (Power Tools (Drills, Saws, Sanders)).
7. Determine business model (B2B, B2C, B2B2C, marketplace, etc.), target market, and geographic focus.

If no existing category or subcategory fits the company's primary products, escalate — see the `category_not_found` decision.

---

## Step 4: Check for Existing Report

Check the company reports directory for an existing report matching `{slug}.md`, using the slug derived in Step 1.

The slug is deterministic — if a report exists with this slug, it is the same company. Do not scan for similar slugs or fuzzy matches.

**If a report exists:** Update it in place. Preserve any content that is still accurate while refreshing and expanding with new findings. Keep the same file path.

**If no report exists:** Create a new file at the standard location.

---

## Step 5: Produce Company Profile Report

Write the company report. Create the output directory if it does not exist.

Use this exact structure. Every section is required -- if information is unavailable, state that explicitly rather than omitting the section.

```markdown
# Company Profile: {Company Name}

**Slug:** {slug}
**Website:** {URL}
**Discovery date:** {today's date}

## Overview

{2-3 paragraph summary of what this company is and does, focusing on their physical products and market position.}

**Entity type:** {Company / Nonprofit / Government Agency / etc.}

## Business Classification

| Attribute | Value |
|-----------|-------|
| Subcategories | `{id1}` ({Display Name 1}), `{id2}` ({Display Name 2}) |
| Primary | `{id}` ({Display Name}) |
| Business model | {B2B / B2C / B2B2C / etc.} |
| Target market | {who they sell to} |
| Geographic focus | {where they operate} |

## Products

{Description of the company's tangible product lines. Organize by product family or division.}

### {Product Line 1}
{Description, target customer, key differentiators}

### {Product Line 2}
{...}

## Product Catalog Analysis (Preliminary)

This is a surface-level scan — the catalog-detector performs the deep technical assessment later. Capture what is visible from basic navigation.

**Has structured catalog:** {Yes / No}
**Estimated catalog size:** {number or range, or "Unknown"}

### Categories

{Catalog hierarchy, up to 3 levels deep:}

- **{Level 1 Category}**
  - {Level 2 Subcategory}
    - {Level 3 if applicable}
  - {Level 2 Subcategory}
- **{Level 1 Category}**
  - ...

## Findings

{Bulleted list of notable discoveries:}
- {Key insight about the business}
- {Interesting pattern in their catalog}
- {Anything surprising or useful for downstream analysis}

## References

{Specific URLs visited during investigation:}
- [{Page title or description}]({URL})
- [{Page title or description}]({URL})
```

### Strict format rules

| Rule | Correct | Wrong |
|------|---------|-------|
| **Canonical sections only** | `## Overview`, `## Business Classification`, `## Products`, `## Product Catalog Analysis (Preliminary)`, `## Findings`, `## References` | Extra sections, missing sections, renamed sections |
| **Subcategories lists all taxonomy IDs** | `` `safety.head_protection` (Head Protection), `safety.respiratory_protection` (Respiratory Protection) `` | Display names only, missing backticks, IDs not from categories.md |
| **Primary is one taxonomy ID** | `` `safety.respiratory_protection` (Respiratory Protection) `` | Two IDs, display name without ID, ID not in categories.md |
| **Taxonomy IDs are verbatim from categories.md** | Exact ID from the file in backticks + display name in parentheses | Paraphrased, abbreviated, invented, or reworded IDs |
| **Primary must appear in Subcategories** | Primary ID is also listed in the Subcategories row | Primary ID absent from Subcategories |
| **Product lines use `###` subsections** | `### Power Tools` under `## Products` | Bullet lists, numbered lists, flat paragraphs |
| **Catalog categories use nested bullet lists** | `- **Level 1**` → `  - Level 2` → `    - Level 3` | Tables, flat lists, heading-based hierarchy |
| **References use markdown links** | `[Products page](https://example.com/products)` | Plain URLs without link text |

---

## Step 6: Self-Verification

Before presenting results, re-read the report you just wrote and check it against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **All canonical sections present** | Overview, Business Classification, Products, Product Catalog Analysis (Preliminary), Findings, References — no extras, none missing |
| 2 | **Primary is a valid taxonomy ID** | The taxonomy ID in the Primary row exists in categories.md and the display name in parentheses matches |
| 3 | **Subcategories contain valid taxonomy IDs** | Every taxonomy ID in the Subcategories row exists in categories.md with a matching display name |
| 4 | **All taxonomy IDs exist in categories.md** | No invented, paraphrased, or abbreviated IDs — every ID used in Subcategories and Primary appears verbatim in categories.md |
| 5 | **Slug is correct** | Matches the algorithm from Step 1 — derived from domain, not display name |
| 6 | **Product lines described** | At least one `###` subsection under `## Products` |
| 7 | **References populated** | At least two URLs visited during investigation are listed with markdown links |
| 8 | **Catalog categories covered** | Walk each Level 1 bullet in `## Product Catalog Analysis (Preliminary)`. For each, either a matching taxonomy ID appears in the Subcategories row, or `## Findings` explains why it was excluded (services, digital-only, no taxonomy entry). A catalog section selling tangible goods with a matching taxonomy entry must appear in Subcategories — omitting it is the most common classification error. |

If all 8 pass, the report is complete.

---

## Investigation Guidance

- Do not stop at the homepage. Real product data lives 2-3 clicks deep in "Products", "Shop", "Catalog", or "Collections" pages.
- Footer navigation often links to important pages not in the main nav.
- Check the site's sitemap for pages that might be missed through navigation.
- "For Professionals" or "B2B" sections often contain more detailed product specs than the consumer-facing pages.
- When exploring catalogs, navigate into 2-3 different product categories to understand the breadth and structure of the company's offerings.

---

## Boundaries

- This workflow classifies and profiles. It does not generate scrapers, assess catalog scrapability, or deploy anything.
- The product taxonomy categories file is read-only. If a category is missing, escalate -- never modify it.
- Only tangible goods companies get reports. A rejected company gets a clear explanation but no file output.
- Digital products, services, and subscriptions should be noted if they exist alongside physical goods, but they are not cataloged in detail.

---

## Decisions

### Decision: ambiguous_company

**Context:** The company name resolves to multiple plausible companies (e.g., "Mercury" could be Mercury Insurance, Mercury Systems, Mercury Marine).
**Autonomous resolution:** Pick the match when confidence exceeds 80% -- an exact domain match, dominant web presence, or overwhelming search result consensus all qualify. When the input includes qualifying context (industry, location, product type), use it to disambiguate.
**Escalate when:** Multiple plausible matches exist and none is clearly dominant. No single candidate reaches 80% confidence.
**Escalation payload:** List of candidate companies, each with: name, URL, one-line description, and why it is a plausible match.

### Decision: tangible_ambiguous

**Context:** The company's relationship to physical goods is unclear. Examples: a software company that also sells branded merchandise; a platform that facilitates sales of physical goods but holds no inventory; a design firm that licenses product designs but does not manufacture.
**Autonomous resolution:** Proceed if the company sells any physical products directly to customers, even as a secondary business line. The threshold is "would a customer receive a physical item shipped to them?"
**Escalate when:** Truly borderline -- the only physical goods are trivial (branded swag, promotional items) or the company's role in the physical supply chain is indirect (pure licensor, pure platform with no first-party inventory).
**Escalation payload:** Company name, URL, description of what the company does, the specific reason tangibility is ambiguous, and examples of any physical products found.

### Decision: category_not_found

**Context:** No existing category or subcategory in the product taxonomy categories file adequately describes the company's primary products.
**Autonomous resolution:** Never. Taxonomy integrity is critical -- downstream systems (search, comparison, scraping schemas) depend on exact category values. Inventing or approximating a category corrupts the data.
**Escalate when:** Always. This decision is never auto-resolved.
**Escalation payload:** Company name, URL, description of what the company produces, the closest existing taxonomy categories considered and why they do not fit, and a suggested category name and subcategories that would cover the gap.
