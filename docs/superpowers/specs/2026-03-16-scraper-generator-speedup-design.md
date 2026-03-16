# Scraper Generator Speedup — Design Spec

## Problem

The scraper-generator stage takes ~37 minutes for a multi-subcategory, non-English site (pata.lv). The total pipeline is ~47 minutes. The target is 10-15 minutes end-to-end, with Stage 3 under 10 minutes.

Root causes from the pata.lv run:

| Time sink | Minutes | Root cause |
|-----------|---------|------------|
| Wrong category URL IDs | ~10 | Catalog assessment described categories by name but scraper assumed wrong numeric IDs. Required probe → fix → retest cycle. |
| Price extraction bug | ~8 | Price div empty in static HTML (JS-rendered via dataLayer). Scraper tried CSS selectors, failed, required diagnosis + fix + retest. |
| Label discovery sub-agent | ~7 | Separate sub-agent sampled 57 products via sequential WebFetch to build LABEL_MAP. Duplicated work the scraper would do anyway. |
| Schema loading by LLM | ~3 | LLM read 6 SKU schema files and extracted attribute key lists. Mechanical string processing, no reasoning needed. |
| Sub-agent dispatch overhead | ~3 | Two sub-agent dispatches (label-discoverer, code-generator) each created new context windows, re-loaded input data. |
| Multiple smoke test attempts | ~6 | Three smoke test runs because first two failed due to bugs above. |

## Solution

Four changes that eliminate the root causes:

1. **Extraction blueprint** in catalog-detector — verified URLs, price method, CSS selectors
2. **Eliminate label-discoverer and code-generator sub-agents** — orchestrator does everything inline
3. **Pre-processing script** for schema loading — Python replaces LLM token generation
4. **Reduced smoke test** — 10 products, 1 attempt (with 1 fix budget)

## Time Budget

| Phase | Current | Optimized | How |
|---|---|---|---|
| Stage 1: Classify | 3 min | 3 min | No change |
| Stage 2: Catalog detect | 5 min | 6 min | +1 min for extraction blueprint |
| Stage 3: Load context + schemas | 5 min | 1 min | Pre-processing script |
| Stage 3: Label mapping | 7 min | 1 min | Blueprint labels + language seed, no sub-agent |
| Stage 3: Code generation | 4 min | 3 min | Single orchestrator, no sub-agent dispatch |
| Stage 3: Probe + smoke test | 21 min | 3 min | Verified selectors → first-attempt success + 10-product test |
| Stage 4: Eval generation | 2 min | 2 min | No change |
| **Total** | **~47 min** | **~19 min** | |
| **Stage 3 only** | **~37 min** | **~8 min** | **~78% reduction** |

---

## Change 1: Extraction Blueprint in Catalog-Detector

### What it is

A new `## Extraction Blueprint` section appended to the catalog assessment report (not a separate file). Produced by the catalog-detector as part of its existing product page inspection.

### Blueprint fields

**Verified Category Tree** — exact leaf URLs with product counts, crawled and confirmed:

```markdown
| Category Path | URL | Product Count | Depth |
|---|---|---|---|
| Kokmateriāli > Zāģmateriāli > Žāvēts | /54-kokmateriali/82-zagmateriali/374-zavets | 12 | 3 |
| Kokmateriāli > Zāģmateriāli > Nežāvēts | /54-kokmateriali/82-zagmateriali/375-nezavets | 20 | 3 |
| ... | ... | ... | ... |
```

The scraper-generator reads this table directly for `CATEGORY_MAPPING` — no discovery crawl, no URL guessing.

**Price Extraction Method:**

```markdown
- **Primary method:** dataLayer | static_html_css | json_ld | api_endpoint
- **Static HTML price:** {yes: selector | no: reason}
- **dataLayer price:** {yes: event name and JSON path | no}
- **JSON-LD price:** {yes | no}
- **Verified on:** {2-3 product URLs with actual extracted prices}
- **Currency:** EUR
- **Price variants:** per-unit (€/gab.) vs per-area (€/m²); dataLayer has per-unit
```

**Spec Table Selectors:**

```markdown
- **Row selector:** table tr
- **Label cell:** td:first-child (strip trailing ":")
- **Value cell:** td:nth-child(2)
- **Verified on:** {2-3 product URLs with attribute counts}
```

**Sample Attribute Labels:**

```markdown
| Site Label | Frequency | Example Value |
|---|---|---|
| Biezums | 5/5 | 21 |
| Platums | 5/5 | 135 |
| Suga | 5/5 | Egle |
| Mitrums | 5/5 | KD18% |
| Kvalitāte | 4/5 | ABC |
| ... | ... | ... |
```

**Product Name Selector, SKU Location, Breadcrumb Selector** — CSS paths verified on 3-5 product pages.

### How the catalog-detector produces it

The catalog-detector already visits 3-5 product pages in Step 5 (attribute extractability check). The blueprint piggybacks on that work:

- **Step 5 enhanced:** For each product page already fetched, also record: CSS selector paths (spec table, price, name, breadcrumb), all attribute labels and values, price rendering method (check static HTML → JSON-LD → dataLayer in order).
- **New Step 5a (Verified Category Tree):** After Step 5 passes, crawl the full category tree from top-level navigation. Record exact URLs, product counts, and depth for every node. This is the only new crawl — adds ~60-90 seconds.

### Cost

~60-90 additional seconds in the catalog-detector (verified category tree crawl). The rest is free — inspecting pages already fetched. Saves ~18 minutes downstream.

### Blueprint in the report template

The success template gains the `## Extraction Blueprint` section after `## Notes`. The stop template is unchanged (no blueprint if the site isn't scrapable).

Two new self-verification gates:
- Verified category tree has at least one leaf URL per top-level category
- Price method is verified on at least 2 product URLs with actual values

---

## Change 2: Eliminate Sub-Agents

### Current: 3 sub-agents

The scraper-generator dispatches three sub-agents:
1. **label-discoverer** — samples products, builds LABEL_MAP (~7 min)
2. **code-generator** — writes scraper.py (~4 min)
3. **validator** — probe tests + smoke test (~varies)

### New: 1 sub-agent (validator only)

The orchestrator handles label mapping and code generation inline. The validator remains a sub-agent because it runs the actual scraper (external process).

**Label mapping** moves to the orchestrator:
- The extraction blueprint provides sample attribute labels from 3-5 product pages
- The orchestrator maps these to schema keys using the pre-built routing tables
- For non-English sites, a **language-level seed file** (e.g., `docs/platform-knowledgebase/latvian-labels.json`) provides common translations. The orchestrator merges site-specific labels on top.
- The `LABEL_MAP` and `CATEGORY_ALIASES` remain static dicts embedded in the scraper — no runtime label learning.

**Code generation** moves to the orchestrator:
- The orchestrator generates scraper.py directly, using the blueprint's verified selectors, price method, and mapped labels.
- No sub-agent dispatch overhead, no context duplication.
- The code-generator.md file is kept as a **reference** (canonical product record format) but is no longer dispatched as a sub-agent.

### File changes

| File | Change |
|---|---|
| `references/label-discoverer.md` | **Delete** — absorbed by blueprint + orchestrator |
| `references/code-generator.md` | **Keep as reference** — product record format canonical definition. No longer dispatched. |
| `references/validator.md` | **Keep as sub-agent** — still dispatched for probe + smoke test |
| `references/orchestrator.md` | Remove label-discoverer and code-generator dispatch sections. Add inline label mapping + code generation steps. |
| SKILL.md | Update sub-agent list (only validator). Remove label-discoverer and code-generator from dispatch instructions. |

### Language-level seed files

For each non-English language encountered, store common attribute label translations:

```
docs/platform-knowledgebase/labels-lv.json  (Latvian)
docs/platform-knowledgebase/labels-lt.json  (Lithuanian)
docs/platform-knowledgebase/labels-de.json  (German)
```

Format:
```json
{
  "Platums": "width",
  "Biezums": "thickness",
  "Garums": "length",
  "Suga": "species",
  "Mitrums": "moisture_content"
}
```

The orchestrator loads the language seed, merges blueprint's sample labels on top, and uses the combined map for code generation. After generation, the merged map is saved back to the seed file — future sites in the same language start with a richer seed.

---

## Change 3: Pre-Processing Script

### What it does

A Python script at `.claude/skills/scraper-generator/scripts/prepare_generator_input.py` that:

1. Reads SKU schema files for all relevant subcategories
2. Extracts attribute key lists (core + extended), data types, enum values
3. Builds per-subcategory routing tables
4. Outputs a compact `generator_input.json`

### When it runs

The scraper-generator SKILL.md invokes the script before the orchestrator starts:

```
uv run python .claude/skills/scraper-generator/scripts/prepare_generator_input.py \
  --schemas wood.softwood_hardwood_lumber wood.flooring_decking wood.millwork ... \
  --output docs/scraper-generator/{slug}/generator_input.json
```

### What it outputs

```json
{
  "routing_tables": {
    "wood.softwood_hardwood_lumber": {
      "core": ["wood_type", "structural_grade", "appearance_grade", ...],
      "extended": ["species", "nominal_thickness", "nominal_width", ...],
      "types": {"wood_type": "str", "nominal_thickness": "str", ...}
    },
    "wood.flooring_decking": { ... }
  }
}
```

The orchestrator reads this JSON instead of parsing 6 schema files. Saves ~3 minutes of LLM token generation.

---

## Change 4: Reduced Smoke Test

### Current

- 20 products per test
- ~6s per product (1.5s delay + fetch + parse)
- 3 attempts (first two fail due to bugs)
- Total: ~6 min just for test execution

### New

- 10 products per test (sufficient for validation)
- Same 6s per product timing
- 1 attempt expected to pass (blueprint provides correct selectors)
- 1 fix cycle budgeted (for unexpected issues)
- Total: ~2-3 min

The final verification run (Step 5b, larger sample) is unchanged — it validates the full scraper at higher volume.

---

## What Doesn't Change

- Pipeline stages, their inputs/outputs, and decision logic
- Product record format (canonical definition stays in code-generator.md)
- Validator sub-agent (still dispatched — runs external scraper process)
- Eval generator (no changes)
- Product classifier (no changes)
- Daily scraper runtime (no LLM, no new overhead)
- LABEL_MAP / CATEGORY_ALIASES architecture (static dicts at generation time)

## Migration

This spec builds on the current pure-skills architecture. Changes are to file content (skill workflows), not file structure.

Phases:
1. Add extraction blueprint to catalog-detector workflow + report template
2. Create pre-processing script
3. Rewrite scraper-generator orchestrator (inline label mapping + code generation, remove 2 sub-agent dispatches)
4. Update scraper-generator SKILL.md (remove label-discoverer and code-generator from sub-agent list)
5. Create language seed infrastructure
6. Test with a real company run
