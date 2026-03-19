# Product Classifier Workflow

**Input:** Company name or URL
**Output:** Company profile report (URL, taxonomy classification, catalog structure) for catalog-detector

---

## Context

Resolve a company name or URL into a classified company profile focused on tangible, physical goods. This workflow decides whether a company belongs in the pipeline, assigns it a canonical taxonomy classification, and produces a structured report. It does not interact conversationally — it makes decisions and either completes the classification or escalates.

**Speed principle:** Do the minimum investigation needed to fill the report's required fields. One search, a few page visits. The catalog-detector does the deep site investigation later — this skill just needs enough to classify.

---

## Step 1: Resolve Company Identity and Derive Slug

Given the input, determine whether it is a URL or a company name.

**If URL:** Extract the hostname and resolve the company from the site.

**If company name:** Do one web search for the company name to find its official website.

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
| `Hilti UK` | `hilti.co.uk` | `hilti` |

The slug is always derived from the domain, never from the display name.

If the company name resolves to multiple plausible companies, escalate — see the `ambiguous_company` decision.

---

## Step 2: Quick Site Scan

Fetch the homepage. From the homepage alone, determine:

1. **Tangible goods gate** — Does the company sell physical products? If only services/software/digital → stop, no report. If general retailer/marketplace (Amazon, eBay, Walmart-scale breadth) → stop, no report.
2. **Product navigation** — Find the main product/catalog navigation links. Read the top-level category names from the nav menu.
3. **Catalog hints** — Note the catalog entry URL, platform signals (meta generators, URL patterns, known CMS paths), site language, and any access issues.

If the homepage doesn't show product categories clearly, visit ONE products/catalog/shop page to get the category list. Do not explore further.

If the company's relationship to physical goods is unclear, escalate — see the `tangible_ambiguous` decision. If the site is inaccessible, escalate — see the `inaccessible_site` decision.

---

## Step 3: Classify into Taxonomy

Read the product taxonomy categories file. Match the observed product categories from Step 2 against taxonomy subcategories.

Each subcategory line has a display name and a taxonomy ID in backticks. Extract taxonomy IDs using: `re.match(r'^- (.+?) \x60([a-z][a-z0-9_.]+)\x60$', line.strip())`.

**Classification steps:**

1. List every product category observed in the site navigation from Step 2.
2. For each, find the matching taxonomy subcategory. Record matches (taxonomy ID + display name).
3. Exclude marginal matches (branded swag, gift cards, services). A dedicated catalog section with real physical products is never marginal.
4. Pick the **Primary** — the single subcategory the company is most known for.
5. Business model (B2B, B2C, B2B2C), target market, and geographic focus — infer from what's visible. Don't search further.

If no taxonomy category fits, escalate — see the `category_not_found` decision.

---

## Step 4: Check for Existing Report

Check the company reports directory for `{slug}.md`.

**If exists:** Overwrite with fresh findings.
**If not:** Create a new file.

---

## Step 5: Produce Company Profile Report

Write the report. Every section is required.

```markdown
# Company Profile: {Company Name}

**Slug:** {slug}
**Website:** {URL}
**Discovery date:** {YYYY-MM-DD}

## Overview

{1-2 sentences: what the company does, what physical products it sells. No history essays.}

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

### {Product Line 1}
{1-2 sentences: what it is.}

### {Product Line 2}
{...}

## Product Catalog Analysis (Preliminary)

**Has structured catalog:** {Yes / No}
**Estimated catalog size:** {number or range, or "Unknown"}

### Catalog Hints

- **Catalog entry URL:** {URL where product listings were found, or "None found"}
- **Suspected platform:** {woocommerce / shopify / magento / prestashop / custom / unknown}
- **Access issues:** {none / cloudflare / login-gated / geo-restricted}
- **Site language:** {ISO 639-1 code}

### Categories

{Top-level categories from navigation, up to 2 levels:}

- **{Level 1 Category}**
  - {Level 2 Subcategory}
- **{Level 1 Category}**
  - ...

## Findings

{Bulleted list of anything the catalog-detector needs to know — access quirks, separate retail domains, unusual catalog structure. Skip if nothing noteworthy.}

## References

- [{Page description}]({URL})
- [{Page description}]({URL})
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
| **References use markdown links** | `[Products page](https://example.com/products)` | Plain URLs without link text |

---

## Step 6: Self-Verification

Check the report against these gates. Fix any failures.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **All canonical sections present** | Overview, Business Classification, Products, Product Catalog Analysis, Findings, References |
| 2 | **Primary is a valid taxonomy ID** | Exists in categories.md with matching display name |
| 3 | **Subcategories contain valid taxonomy IDs** | Every ID exists in categories.md |
| 4 | **All taxonomy IDs exist in categories.md** | No invented or paraphrased IDs |
| 5 | **Slug is correct** | Derived from domain, not display name |
| 6 | **Product lines described** | At least one `###` subsection under `## Products` |
| 7 | **References populated** | At least two URLs listed |
| 8 | **Primary in Subcategories** | Primary taxonomy ID appears in Subcategories row |

---

## Boundaries

- This workflow classifies and profiles. It does not generate scrapers or assess catalog scrapability.
- The product taxonomy categories file is read-only. If a category is missing, escalate — never modify it.
- Only tangible goods companies get reports. A rejected company gets a clear explanation but no file output.

---

## Decisions

### Decision: ambiguous_company

**Context:** The company name resolves to multiple plausible companies.
**Autonomous resolution:** Pick the match when confidence exceeds 80% — an exact domain match, dominant web presence, or input with qualifying context (industry, location, product type).
**Escalate when:** Multiple plausible matches, none clearly dominant.
**Escalation payload:** List of candidates with name, URL, and one-line description.

### Decision: tangible_ambiguous

**Context:** The company's relationship to physical goods is unclear.
**Autonomous resolution:** Proceed if the company sells any physical products directly to customers, even as a secondary business line.
**Escalate when:** Truly borderline — only trivial physical goods (branded swag) or indirect supply chain role.
**Escalation payload:** Company name, URL, what was found, why it's ambiguous.

### Decision: inaccessible_site

**Context:** The company's website blocks all access and no alternative source provides product information.
**Autonomous resolution:** If product information can be gathered from any alternative source, proceed. Record the access issue in Catalog Hints.
**Escalate when:** No product information is available from any source.
**Escalation payload:** Company name, URL, what access methods were tried.

### Decision: category_not_found

**Context:** No taxonomy subcategory fits the company's primary products.
**Autonomous resolution:** Never. Taxonomy integrity is critical.
**Escalate when:** Always.
**Escalation payload:** Company name, URL, what they produce, closest existing categories, suggested new category.
