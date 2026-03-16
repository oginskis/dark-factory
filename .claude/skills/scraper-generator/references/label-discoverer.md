# Label Discoverer Sub-Agent

**Input:** Site access (URL, scraping strategy, catalog structure), loaded SKU schemas for all subcategories
**Output:** `LABEL_MAP` dict, `CATEGORY_ALIASES` dict, label coverage report

Systematically discover the full set of attribute labels a non-English site uses before scraper code is generated. Build `LABEL_MAP` and `CATEGORY_ALIASES` and verify ≥70% label coverage. Skip for English-language sites.

---

## Input Contract

The caller provides:

| Field | Type | Description |
|---|---|---|
| `site_url` | string | Base URL of the site |
| `scraping_strategy` | enum | `static_html`, `structured_data`, or `pdf_pricelist` |
| `catalog_structure` | object | Categories, subcategory URLs, and navigation paths from the catalog assessment |
| `sku_schemas` | object | Map of taxonomy ID → loaded schema (core + extended attribute tables) |
| `subcategory_ids` | list | All taxonomy IDs the company covers |
| `site_language` | string | ISO 639-1 language code (e.g., `no`, `fi`, `de`) |

---

## Procedure

### Step 1: Sample Products

Draw a sample of 50–100 products from the site, distributed across all subcategories.

- For multi-subcategory companies, include products from every top-level category listed in the catalog structure. Aim for proportional representation — if a category has more URL paths, sample more from it.
- Use the same scraping strategy established from the catalog assessment (API calls, HTML fetches, or sitemap + page fetches). Do not switch strategies mid-discovery.
- Retrieve raw product data including all visible attribute labels and their values. For structured-data strategies, this means the raw JSON object or API response. For static HTML, this means the full spec table or attribute block from the product page.
- Stop when 100 unique products are collected, or when all top-level categories have at least one sampled product and the total is ≥ 50.

If the site has fewer than 50 accessible products, use all available products. Record the actual sample size for the coverage report.

### Step 2: Collect the Label Inventory

From the sampled products, extract every unique attribute label or key that appears anywhere in product data.

- For HTML pages: collect all table row headers, `dt` elements, label text, and spec section headings that precede attribute values.
- For JSON/API responses: collect all property names that carry attribute values (exclude structural keys like `id`, `url`, `images`).
- Normalise labels before deduplication: trim whitespace, collapse internal whitespace to a single space, preserve original casing (do not lowercase — some sites use casing to distinguish labels).
- The result is the **label inventory**: a list of unique normalised labels found across all sampled products.

Record how many products each label appeared in. Labels present in only one product may still be valid category-specific attributes — do not exclude them.

### Step 3: Match Labels to Schema Keys

For each label in the inventory, attempt to match it to a schema Key from the loaded SKU schemas. Two match types apply:

**Direct translation:** The label translates to a single schema Key regardless of subcategory. Examples:
- `"Treslag"` → `wood_type`
- `"Vekt"` → `weight`
- `"Lengde"` → `length`

**Subcategory-variable translation:** The same label translates to different schema Keys depending on subcategory. This occurs when the same physical measurement appears in multiple schemas under different names. Examples:
- `"Bredde"` → `nominal_width` (lumber), `unit_width` (doors), `tile_width` (tiles)
- `"Høyde"` → `nominal_height` (lumber), `unit_height` (doors)

For each label, consult the Key column of every loaded schema. Translation requires semantic understanding — the label in the source language describes a physical property, and the schema Key captures that same property. Do not invent Keys; only use Keys that exist in a loaded schema.

Labels that cannot be matched to any schema Key in any loaded schema are **unmapped**. Record them separately. They may represent:
- Attributes the taxonomy has not yet captured (candidates for `extra_attributes`)
- Navigation or UI artefacts that are not product attributes (discard these)
- Variants of already-mapped labels with different casing or punctuation (consolidate these)

### Step 4: Build LABEL_MAP

Construct a Python dict `LABEL_MAP` mapping source-language labels to generic English intermediate keys.

Rules:
- Keys are the exact normalised labels from the inventory.
- Values are English intermediate keys — these may be schema Keys directly, or generic English names when the same label maps to different schema Keys across subcategories.
- When a label has a direct translation (same schema Key in all applicable subcategories), use the schema Key as the value.
- When a label is subcategory-variable, use a generic English intermediate key as the value (e.g., `"width"`) and record the per-subcategory mapping in `CATEGORY_ALIASES`.
- Do not include unmapped labels in `LABEL_MAP`.

Example structure:
```python
LABEL_MAP = {
    "Treslag": "wood_type",
    "Lengde": "length",
    "Bredde": "width",          # subcategory-variable: see CATEGORY_ALIASES
    "Vekt": "weight",
    "Overflatebehandling": "surface_treatment",
}
```

### Step 5: Build CATEGORY_ALIASES

Construct a Python dict `CATEGORY_ALIASES` mapping taxonomy IDs to per-subcategory Key overrides.

- Only include entries for labels that are subcategory-variable (i.e., where `LABEL_MAP` points to a generic intermediate key).
- Structure: outer key is taxonomy ID, inner dict maps generic intermediate key → schema Key for that subcategory.
- Every taxonomy ID in `subcategory_ids` that has at least one alias must appear as an outer key.

Example structure:
```python
CATEGORY_ALIASES = {
    "building_materials.lumber": {
        "width": "nominal_width",
        "height": "nominal_height",
    },
    "building_materials.doors": {
        "width": "unit_width",
        "height": "unit_height",
    },
    "building_materials.tiles": {
        "width": "tile_width",
    },
}
```

Subcategories where the generic key matches the schema Key directly do not need an alias entry — the scraper falls back to using the generic key as the schema Key.

### Step 6: Compute Label Coverage

Label coverage is the fraction of inventory labels that are successfully mapped.

**A label is covered if:**
- It appears in `LABEL_MAP`, AND
- Its value (direct or via `CATEGORY_ALIASES`) resolves to a schema Key present in the core or extended attributes of at least one loaded schema.

**Formula:**
```
coverage = covered_labels / total_inventory_labels
```

**Target: ≥ 70%.**

For multi-subcategory companies, also compute per-subcategory coverage:
```
per_subcategory_coverage[taxon_id] = labels_covered_in_that_schema / labels_appearing_in_products_of_that_subcategory
```

If any subcategory falls below 50% while overall coverage is above 70%, record a warning in the coverage report but treat this as a pass. The per-subcategory threshold is advisory.

---

## Circuit Breaker: Extension Attempts

If coverage is below 70%, attempt to extend `LABEL_MAP` by examining unmapped labels more carefully:

1. Re-examine unmapped labels for variant spellings, punctuation differences, or abbreviations that could match already-identified translations.
2. Review the loaded schemas for Keys that were not yet matched — look for labels in the inventory that correspond semantically even if the translation is non-obvious.
3. Identify unmapped labels that are UI artefacts (e.g., "Legg i handlekurv", "Se mer") and explicitly mark them as discards rather than attribute labels.

Each such review-and-extend cycle counts as one attempt. **Maximum 3 extension attempts.** If coverage remains below 70% after 3 attempts, report the final coverage figure and the list of unmapped labels to the caller. Do not attempt further mapping. The caller decides how to proceed.

---

## Output Contract

Return a structured result to the caller:

| Field | Type | Description |
|---|---|---|
| `label_map` | dict | `LABEL_MAP`: normalised site labels → English intermediate keys |
| `category_aliases` | dict | `CATEGORY_ALIASES`: taxonomy ID → intermediate key → schema Key overrides |
| `coverage` | float | Overall label coverage (0.0–1.0) |
| `per_subcategory_coverage` | dict | Taxonomy ID → coverage float, for multi-subcategory companies |
| `unmapped_labels` | list | Labels present in inventory but not in `LABEL_MAP` |
| `discarded_labels` | list | Labels identified as UI artefacts, excluded from coverage denominator |
| `sample_size` | int | Number of products sampled |
| `inventory_size` | int | Total unique labels found before discards |
| `extension_attempts` | int | Number of extension cycles performed (0–3) |
| `coverage_sufficient` | bool | `true` if coverage ≥ 70%, `false` otherwise |

The caller uses `coverage_sufficient` to decide whether to proceed to scraper generation or escalate. This sub-agent does not make that decision.

---

## Notes on Translation Quality

**Closed value sets:** Where the site uses a fixed vocabulary for attribute values (e.g., species names, grade labels, material types), identify the mapping at discovery time. Record these as static translation dicts alongside `LABEL_MAP` in the output — for example, `SPECIES_MAP = {"Egle": "Spruce", "Furu": "Pine"}`. The caller will pass these to the scraper generation step.

**Casing in values:** Value translations should normalise to English title case for string values that correspond to schema-defined controlled vocabularies. For free-text values (descriptions, model names), pass through as-is.

**Do not translate at runtime:** All label-to-key translation must be static and encoded into `LABEL_MAP` and `CATEGORY_ALIASES`. The generated scraper must not perform any language detection or dynamic label translation at runtime.
