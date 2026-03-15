---
name: product-taxonomy
description: Researches and documents SKU attribute schemas for tangible goods subcategories defined in the project's product taxonomy. Given a product subcategory (like "Electric Vehicle Charging Equipment" or "Power Tools (Drills, Saws, Sanders)"), researches multiple companies and product catalogs to determine the typical SKU attributes for that subcategory. Only works with subcategories already listed in categories.md — does not create new categories. Use this skill whenever the user wants to explore what attributes products in a subcategory typically have, build out SKU schemas, or understand how products in an industry are typically described and cataloged. Also trigger when the user says "what attributes do X products have", "build the taxonomy for Y", "what SKU fields are typical for Z", or "research attributes for [subcategory]".
user-invocable: true
---

# Product Taxonomy

You are a product data analyst. Your job is to research and document SKU attribute schemas for the subcategories defined in the project's product taxonomy — the data fields that describe products in each subcategory.

This taxonomy serves as a shared knowledge base. Other skills and workflows read from it — for example, to classify companies, validate product attributes against industry norms, or generate data models. The more complete and accurate this taxonomy is, the better all downstream analysis becomes.

## Input

The user provides a subcategory name or product type as the argument: `$ARGUMENTS`

Examples:
- "Power Tools (Drills, Saws, Sanders)"
- "Solar Panels & Photovoltaic Modules"
- "research SKU attributes for Major Appliances"
- "what fields do fasteners have"

If no input is provided, ask which subcategory to research. If the user names a top-level category, ask them to pick a specific subcategory within it.

## Data Files

The taxonomy is stored in two places:

1. **Category list**: `docs/product-taxonomy/categories.md` — the master taxonomy of all categories and subcategories. This is the single source of truth for product classification across all skills.

2. **SKU schema files**: `docs/product-taxonomy/sku-schemas/{subcategory-slug}.md` — one file per **subcategory**, documenting the typical attributes for products in that specific subcategory. This keeps each schema focused (20-40 attributes) rather than cramming unrelated product types into one file.

**Strictly per-subcategory.** Never create a schema file for a top-level category. Each file maps to exactly one subcategory from `categories.md`. If the user asks to research a top-level category (e.g., "Machinery & Industrial Equipment"), ask them to pick a specific subcategory within it. Attribute duplication across sibling subcategory files is expected and acceptable — each schema should stand on its own.

**Slugging convention:** lowercase, spaces to hyphens, strip special characters (`&`, `/`, `(`, `)`, `,`). The slug is derived from the **subcategory name**, not the top-level category. Examples:
- "Electric Vehicle Charging Equipment" → `electric-vehicle-charging-equipment.md`
- "Batteries & Grid-Scale Energy Storage" → `batteries-grid-scale-energy-storage.md`
- "Meat, Poultry & Seafood Products" → `meat-poultry-seafood-products.md`
- "Power Tools (Drills, Saws, Sanders)" → `power-tools-drills-saws-sanders.md`

Only `product-taxonomy` writes to these files. All other skills are read-only.

## Phase 1: Understand the Request and Check Existing Data

Determine what the user wants:

- **Research SKU attributes**: Research companies to discover typical attributes for a subcategory that doesn't have a schema file yet
- **Deepen an existing schema**: Research more companies to refine an existing attribute list
- **Browse/review**: Show what's in the taxonomy already

1. Read `docs/product-taxonomy/categories.md` — this is the **closed list** of valid subcategories.
2. **Match the input to an existing subcategory.** The user's input is free text — it may not exactly match a subcategory name. Find the closest semantic match:
   - Exact or near-exact match → proceed (e.g., "power tools" → "Power Tools (Drills, Saws, Sanders)")
   - Close semantic equivalent (one match) → confirm with the user (e.g., "drills" → "Power Tools (Drills, Saws, Sanders)" — say: "The closest subcategory is 'Power Tools (Drills, Saws, Sanders)'. Shall I research that?")
   - Ambiguous — matches multiple subcategories → list the candidates and ask the user to pick one (e.g., "clothing" matches "Men's Clothing", "Women's Clothing", and "Children's & Infants' Clothing" — list all three and ask which one)
   - No reasonable match → **stop and ask for clarification.** Do not create new subcategories or top-level categories. Explain what exists and ask the user to pick one, or to update `categories.md` themselves first.
   - Not a tangible goods category (e.g., "SaaS platforms", "consulting services") → explain that this taxonomy is exclusively for physical products and ask for a different input.
   - If the user names a **top-level category** (e.g., "Machinery & Industrial Equipment"), ask them to pick a specific subcategory within it — schema files are per-subcategory only.
3. Check if `docs/product-taxonomy/sku-schemas/{subcategory-slug}.md` already exists for the matched subcategory. If it does, read it in full — this is an **evolution run**, not a fresh start.
4. Check if any reports in `docs/` reference this subcategory. Those reports may contain real-world SKU attributes discovered from specific companies — useful input.

## Phase 2: Research SKU Attributes

Before starting research, read `.claude/skills/product-taxonomy/references/research-methodology.md` — it details how to select companies, what to look for on product pages, what counts as a tangible goods attribute (and what doesn't), and common pitfalls.

### If a schema file already exists (evolution run)

This is how schemas improve over time. The existing file is the baseline — your job is to enrich it, not replace it.

1. Read the existing schema and note which companies were already researched (listed in the Changelog's Sources column).
2. Research 2-3 **new** companies not already in the Sources — preferably from different regions or market segments to broaden coverage.
3. Compare what you find against the existing attribute list:
   - **New attribute found?** Add it to the table. This is how the schema grows.
   - **Existing attribute confirmed?** Leave it as-is. No change needed.
   - **Existing attribute seems wrong or redundant?** Do not remove it. Mark it as DEPRECATED per the append-only rule. Schemas only grow; they never shrink.
4. Update the "Last updated" date and prepend a new row to the Changelog documenting what changed and which companies were researched.

The schema evolves with each run — every time the skill is invoked for an existing subcategory, it gets a little better.

### If starting fresh

Investigate 3-5 companies selling products in the subcategory. The methodology file explains how to pick a mix of manufacturers, distributors, and retailers for breadth.

The goal is to identify the **most significant attributes** for the subcategory — the ones that consistently appear on pricelists and product catalogs across companies. Only record attributes that describe the **physical product itself**, not services, software, or marketing layered on top.

## Phase 3: Synthesize the Schema

After researching multiple companies, synthesize a **single, flat attribute list** for the subcategory. The schema should cover most products in the subcategory without drilling into sub-subcategories.

### One flat list

Produce a single attribute table — no Core/Common/Specialized split, no sub-sections by product type. Just one list of attributes for the subcategory.

**Which attributes to include:** the ones that are most significant for the subcategory AND commonly appear on pricelists and product catalogs. The test is: "Would this attribute appear on a typical pricelist or product comparison sheet for this subcategory?" If yes, include it. If it's only on deep spec sheets or niche enthusiast sites, leave it out.

Use this as a calibration guide:
- **Under 20** — too thin, misses important attributes
- **20-40** — what you'd see on a real pricelist or product comparison sheet
- **Over 40** — drifting into deep spec sheet territory, trim back

### Mandatory attributes

Every schema must include these 5 attributes. They appear in every schema regardless of category. Descriptions and example values should be tailored to the category, but the attribute names and data types are fixed.

| Attribute | Data Type | Why mandatory |
|-----------|-----------|---------------|
| SKU | text | Every product needs a unique identifier |
| Product Name | text | Every product needs a human-readable name |
| URL | text | Link to the product page or listing |
| Price | number | Numeric price value, no currency symbol |
| Currency | text | ISO 4217 currency code, always separate from Price |

Start the attribute table with these 5, then add category-specific attributes discovered through research.

### Synthesis steps

1. **Merge** attributes that are the same concept but named differently across companies (e.g., "Item No." / "Article Number" / "SKU" → standardize as "SKU")
2. **Prioritize by pricelist presence** — if 3 out of 5 companies show this attribute on their pricelist or catalog listing (not buried in a spec sheet), it belongs in the schema.

### Compliance attributes

Keep compliance and certification attributes **international and universal**. Include widely recognized standards (ISO, CE, UL, RoHS, REACH, HACCP, GMP) but avoid country-specific regulatory details (individual US state registrations, country-specific label requirements, locale-specific certifications). The goal is a schema that works globally, not one tuned to a single jurisdiction.

### Schema evolution rules

**What you can change freely:**
- Update the **Description** of an existing attribute (improve clarity, add detail)
- Update the **Example Values** (add better examples, fix typos)

**Descriptions and Example Values must be company-neutral.** Never mention specific company names in the Description or Example Values columns. Descriptions should explain what the attribute represents generically. Example Values should be realistic product data, not brand names. Company names belong only in two places: the Brand/Manufacturer attribute's Example Values (where they ARE the data), and the Changelog Sources column.

**What you cannot change:**
- **Attribute Name** — renaming breaks downstream references. If the name is wrong, deprecate and create a new one.
- **Data Type** — changing a type (e.g., text → enum, number → text) breaks downstream parsing. If the type needs to change, deprecate the old attribute and create a new one with the correct type.

**Never delete an attribute.** Downstream systems may depend on it. If an attribute is wrong, redundant, or no longer used, mark it as deprecated:

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| Old Attr | text | **DEPRECATED** (2026-03-14) — replaced by "New Attr". Was: original description | — |

Mark the description with **DEPRECATED** and the date. This preserves backward compatibility while keeping the schema clean for readers.

## Phase 4: Write the Output

### Verify subcategory exists in categories.md

The subcategory you are researching must already exist in `docs/product-taxonomy/categories.md`. This skill does not add new subcategories or top-level categories — that is done by editing `categories.md` directly, outside of this skill. If Phase 1 matched the user's input to an existing subcategory, proceed. Otherwise you should have already stopped in Phase 1.

### Write/Update the SKU schema file

Write to `docs/product-taxonomy/sku-schemas/{subcategory-slug}.md` using the **exact format** below. Every schema file must follow this structure precisely — no variations.

#### Canonical file structure

```markdown
# SKU Schema: {Subcategory Name}

**Last updated:** {today's date}
**Parent category:** {Top-Level Category Name}

## Attributes

| Attribute | Data Type | Description | Example Values |
|-----------|-----------|-------------|----------------|
| SKU | text | {category-specific description} | {examples} |
| Product Name | text | {category-specific description} | {examples} |
| URL | text | {category-specific description} | {examples} |
| Price | number | {category-specific description} | {examples} |
| Currency | text | {category-specific description} | {examples} |
| {category-specific attr} | {type} | {description} | {examples} |
| ... | ... | ... | ... |

## Changelog

| Date | Change | Sources |
|------|--------|---------|
| {today} | Initial schema — {N} attributes from {companies} | [{Company 1}]({URL}), [{Company 2}]({URL}) |
```

#### Strict format rules

These rules are non-negotiable. Every schema must comply exactly.

| Rule | Correct | Wrong |
|------|---------|-------|
| **Table has exactly 4 columns** | `\| Attribute \| Data Type \| Description \| Example Values \|` | `\| # \| Attribute \| Data Type \| ...` (no row-number column) |
| **No backticks in table cells** | `9x19mm, 5.56x45mm NATO` | `` `9x19mm`, `5.56x45mm NATO` `` |
| **Only two `##` sections** | `## Attributes` then `## Changelog` | No `## Notes`, `## Summary`, or other sections |
| **Example values are comma-separated plain text** | `Red, Blue, Green` | `Red \| Blue \| Green` or bullet lists |
| **Data types use lowercase** | `text`, `number`, `enum`, `boolean`. Append unit in parentheses when relevant: `number (kg)`, `number (kW)`, `text (mm)`. Use `text (list)` for multi-value fields. | `Text`, `Number`, `integer`, compound types without parentheses like `currency` |
| **No markdown formatting in table cells** | Plain text descriptions | No bold, italic, links, or code blocks inside cells (except **DEPRECATED** markers) |
| **Changelog sources use markdown links** | `[Company](url)` | Plain URLs or company names without links |

The Changelog is the history of the schema. Every run adds a row at the top (most recent first). On evolution runs, the new row should look like:

```
| 2026-03-15 | Added: Halal Cert, Kosher Cert. Deprecated: none. | [Al Islami](url), [Brakes UK](url) |
```

## Phase 5: Self-Verification

Before presenting results, re-read the schema file you just wrote and check it against these quality gates. If any gate fails, fix the issue before proceeding.

| # | Check | Pass criteria |
|---|-------|---------------|
| 1 | **Mandatory attributes present and first** | SKU, Product Name, URL, Price, Currency are rows 1-5 |
| 2 | **Attribute count in range** | 20-40 attributes total — no exceptions, trim if over 40 |
| 3 | **Single flat table** | Only `## Attributes` and `## Changelog` sections — no `## Notes`, no Core/Common/Specialized split, no sub-sections |
| 4 | **Currency separate from Price** | Price is `number`, Currency is `text` — two distinct rows |
| 5 | **Descriptions are company-neutral** | No company names in the Description column (Brand/Manufacturer example values are fine) |
| 6 | **Compliance is international** | Compliance and certification attributes use only international standards (ISO, CE, GHS, HACCP, IEC). No country-specific regulatory bodies (no EPA, FDA, FCC). Exception: widely recognized national grading systems used as international trade terms (e.g., USDA beef grades) are acceptable as product attributes — they describe the product, not regulatory compliance |
| 7 | **No sub-subcategory drilling** | No third-level nesting (e.g., no separate sections for Beef vs Pork vs Lamb within Meat) |
| 8 | **Changelog present** | Has a `## Changelog` section with at least one row documenting this run |
| 9 | **Pricelist test** | Could you hand this attribute list to a procurement team and they'd recognize every field from real pricelists? If any attribute would only appear on a deep spec sheet, remove it. |
| 10 | **Format compliance** | Table has exactly 4 columns (no `#` row-number column), no backticks in any table cell, no markdown formatting in cells (except **DEPRECATED** markers), example values are comma-separated plain text, data types are lowercase |

If all 10 pass, proceed to the summary.

## Phase 6: Summary

Tell the user:
- What subcategory was researched
- Where the schema file was saved (full path)
- How many companies were investigated (and which were new vs already in Sources)
- How many attributes are in the schema now
- **If evolution run:** how many new attributes were added, how many deprecated, and what the new attributes are
- Any interesting findings

## Investigation Tips

- B2B/industrial sites often have the most detailed product specs
- Distributor sites (Grainger, McMaster-Carr, RS Components) are goldmines for attribute discovery since they standardize across brands
- Manufacturer sites show brand-specific naming but often have the deepest spec sheets
- E-commerce platforms (Amazon, Home Depot) show which attributes consumers filter by — these are the most commercially important ones
- If a category is broad (e.g., "Machinery & Industrial Equipment" has 12 subcategories), research one subcategory at a time rather than trying to cover everything at once
