# Catalog Detector Self-Containment Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Make catalog-detector a self-contained MoE expert by removing all cross-references to scraper-generator and reframing downstream language.

**Architecture:** Delete the "Role in the four-level product record" section from SKILL.md, replace the Step 5 cross-reference with an inlined extractability check, and reword/remove 10 downstream-coupled phrases throughout the workflow.

**Tech Stack:** Markdown only

**Spec:** `docs/superpowers/specs/2026-03-17-catalog-detector-self-contained-design.md`

---

## Chunk 1: All changes

### Task 1: Delete SKILL.md cross-reference section

**Files:**
- Modify: `.claude/skills/catalog-detector/SKILL.md`

- [ ] **Step 1: Delete the `## Role in the four-level product record` section**

Remove this entire block (currently between `## File locations` and `## Workflow`):

```markdown
## Role in the four-level product record

The catalog-detector determines whether a site can support the four-level product record format (see `.claude/skills/scraper-generator/references/code-generator.md` for the canonical definition). Specifically, Step 5 (Product Attribute Extractability Check) verifies that the catalog exposes enough structured data to support at least the universal top-level fields and core attributes. A site that only shows product names and images — without structured specs — cannot produce meaningful core_attributes and is stopped via `attributes_not_extractable`.
```

- [ ] **Step 2: Verify SKILL.md structure**

Read the file and confirm sections are: frontmatter → `# Catalog Detector` → `## Input` → `## File locations` → `## Workflow` → `## Notes`. No other `##` sections.

---

### Task 2: Replace Step 5 four-level block in workflow

**Files:**
- Modify: `.claude/skills/catalog-detector/references/workflow.md`

- [ ] **Step 1: Replace the four-level product record block in Step 5**

Find and replace the block starting with `The downstream scraper extracts four levels of product data` (around line 135) through the `extra_attributes` bullet (around line 140) with:

```markdown
Check whether product pages expose structured attributes — not just names and images.

| What to look for | Why it matters |
|-------------------|---------------|
| Spec table or attribute block with named properties (e.g., "Voltage: 18V", "Weight: 3.3 kg") | Indicates the site exposes structured attribute data |
| Price visible on the page (or in structured data / API) | Required for price tracking |
| SKU or model number visible | Required for product identification |
| Additional properties beyond the basics (dimensions, materials, certifications) | Indicates rich attribute availability |
```

- [ ] **Step 2: Verify no `code-generator.md` references remain**

```bash
grep -c "code-generator.md" .claude/skills/catalog-detector/references/workflow.md
```

Expected: 0

---

### Task 3: Reword downstream-coupled language throughout workflow

**Files:**
- Modify: `.claude/skills/catalog-detector/references/workflow.md`

Apply each edit in order. All are simple find-and-replace operations.

- [ ] **Step 1: Line 22 — reword "downstream scraper" constraint**

Replace:
```
The downstream scraper cannot use a headless browser.
```
With:
```
The recommended scraping strategy must work without a headless browser.
```

- [ ] **Step 2: Line 70 — remove scraper-generator reference**

Replace:
```
The scraper-generator uses these patterns to classify products by taxonomy subcategory.
```
With:
```
These URL patterns are part of the catalog structure finding.
```

- [ ] **Step 3: Line 98 — remove scraper-generator attribution**

Replace:
```
The knowledgebase is maintained by the scraper-generator — this workflow only reads it.
```
With:
```
This workflow reads the knowledgebase but does not modify it.
```

- [ ] **Step 4: Line 120 — remove "for the downstream scraper"**

Replace:
```
Verify it returns sufficient product data (name, price, attributes) for the downstream scraper.
```
With:
```
Verify it returns sufficient product data (name, price, attributes).
```

- [ ] **Step 5: Line 191 — reword "scraper-relevant"**

Replace:
```
scraper-relevant categories
```
With:
```
product categories
```

- [ ] **Step 6: Line 222 — reword "downstream agents"**

Replace:
```
downstream agents
```
With:
```
subsequent pipeline stages
```

- [ ] **Step 7: Line 252 — remove scraper-generator reference**

Remove the sentence:
```
This informs the scraper-generator's category mapping.
```

- [ ] **Step 8: Line 418 — reword decision block**

Replace:
```
the downstream scraper does not support
```
With:
```
this pipeline does not support
```

- [ ] **Step 9: Line 432 — reword decision block**

Replace:
```
the scraper cannot reliably extract structured attribute data from product pages
```
With:
```
structured attribute data cannot be reliably extracted from product pages
```

- [ ] **Step 10: Verify no "scraper-generator" or "downstream scraper" references remain**

```bash
grep -ciE "scraper-generator|downstream scraper|downstream agents" .claude/skills/catalog-detector/references/workflow.md
```

Expected: 0

---

### Task 4: Verification

- [ ] **Step 1: Run verify_skill.py**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py catalog-detector
```

Expected: 0 critical, 0 moderate.

- [ ] **Step 2: Verify remaining "scraper" uses are generic vocabulary**

```bash
grep -n "scraper" .claude/skills/catalog-detector/references/workflow.md
```

Review output — every remaining occurrence should be generic vocabulary ("a scraper", "scraping strategy", "scrapable") not a reference to the scraper-generator skill. Expected ~10 remaining generic uses.

- [ ] **Step 3: Present diff for review**

Show `git diff` for both modified files before any commit.
