# Catalog Detector Self-Containment — Design Spec

## Problem

The catalog-detector skill violates the Mixture of Experts principle by referencing the scraper-generator's product record format definition (`.claude/skills/scraper-generator/references/code-generator.md`). This creates a dependency on a downstream skill and uses jargon ("four-level product record", "core_attributes", "extended_attributes") that is irrelevant to the catalog-detector's job. The workflow also contains scattered "downstream scraper" and "scraper-generator" language that couples it to downstream concerns. The catalog-detector should be a focused expert on one thing: detecting whether a site has a scrapable catalog.

## Solution

Remove the cross-reference to scraper-generator. Inline the minimum knowledge the catalog-detector needs for its attribute extractability check, framed from the detector's own perspective. Remove or reword all downstream-coupling language throughout the workflow. Remove the `## Role in the four-level product record` section from SKILL.md entirely.

## Changes

### 1. SKILL.md: Delete `## Role in the four-level product record` section

Remove the entire section (currently lines 29-31). No replacement. The SKILL.md becomes: frontmatter → Input → File locations → Workflow → Notes.

### 2. Workflow Step 5: Replace cross-reference with inlined extractability check

Remove lines 135-140 (the four-level block referencing `code-generator.md` with `core_attributes`, `extended_attributes`, `extra_attributes`).

Replace with self-contained language:

```markdown
### Product attribute extractability

Check whether product pages expose structured attributes — not just names and images.

| What to look for | Why it matters |
|-------------------|---------------|
| Spec table or attribute block with named properties (e.g., "Voltage: 18V", "Weight: 3.3 kg") | Indicates the site exposes structured attribute data |
| Price visible on the page (or in structured data / API) | Required for price tracking |
| SKU or model number visible | Required for product identification |
| Additional properties beyond the basics (dimensions, materials, certifications) | Indicates rich attribute availability |

If product pages show only a name, image, and "Add to cart" with no structured specs, stop — see the `attributes_not_extractable` decision.
```

### 3. Workflow: Disposition of all "scraper" / "downstream" references

Every occurrence has been audited. Disposition per line:

| Line | Current text | Disposition | Replacement |
|------|-------------|-------------|-------------|
| 22 | "The downstream scraper cannot use a headless browser." | **Reword** — legitimate constraint but should be framed as pipeline constraint, not downstream dependency | "The recommended scraping strategy must be executable with simple HTTP request libraries — no headless browser." |
| 70 | "The scraper-generator uses these patterns to classify products by taxonomy subcategory." | **Remove** — downstream coupling | "These URL patterns are part of the catalog structure finding." (or simply delete the sentence) |
| 98 | "The knowledgebase is maintained by the scraper-generator — this workflow only reads it." | **Reword** — remove attribution | "This workflow reads the knowledgebase but does not modify it." |
| 120 | "for the downstream scraper" | **Remove** — delete the phrase, keep the rest of the sentence | "Verify it returns sufficient product data (name, price, attributes)." |
| 135-140 | Four-level product record block with `code-generator.md` reference | **Replace** — see Change 2 above | Self-contained extractability table |
| 148 | "The test is whether a scraper can reliably extract" | **Keep** — "scraper" here is generic vocabulary (a scraper is what scrapes), not a reference to the scraper-generator skill |
| 191 | "scraper-relevant categories" | **Reword** | "product categories" |
| 209 | "All scrapers must work with simple HTTP requests" | **Keep** — generic vocabulary, states the pipeline constraint |
| 222 | "downstream agents" | **Reword** | "subsequent pipeline stages" |
| 252 | "This informs the scraper-generator's category mapping." | **Remove** — downstream coupling | Delete the sentence |
| 367 | "A scraper could follow the listed URL patterns" | **Keep** — generic vocabulary, part of self-verification gate |
| 387 | "it does not classify companies (product-classifier) or generate scrapers (scraper-generator)" | **Keep** — boundary statement, explicitly defines what this skill does NOT do |
| 418 | "the downstream scraper does not support" | **Reword** | "this pipeline does not support" |
| 432 | "the scraper cannot reliably extract" | **Reword** | "structured attribute data cannot be reliably extracted from product pages" |

**Rule of thumb applied:** The word "scraper" as generic vocabulary (a thing that scrapes) is fine. References to "the scraper-generator" (a specific skill) or "the downstream scraper" (implying awareness of the pipeline stage) are removed or reworded.

## What stays the same

- All 9 steps (no structural changes)
- All 6 decision blocks (names and logic unchanged, only wording adjustments in 2 blocks)
- Step 5a: Verified Category Tree (describes catalog structure — detection work)
- Step 6: Scraping Strategy (squarely the detector's job)
- SKILL.md file locations, workflow pointer, tool instructions, stop behavior description
- Word count stays borderline (~3,800 words, slight decrease from removals)

## What does NOT change

- No other skills are modified
- No cross-reference updates needed elsewhere
- verify_skill.py — no script changes needed
