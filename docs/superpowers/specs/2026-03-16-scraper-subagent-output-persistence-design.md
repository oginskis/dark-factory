# Scraper Sub-Agent Output Persistence — Design Spec

## Problem

The scraper-generator orchestrates three sub-agents (label discoverer, code generator, validator), but only the code generator's output (scraper.py) is persisted to disk. The label discoverer's LABEL_MAP, coverage metrics, and unmapped labels exist only in-memory and are lost when the orchestrator's context window ends. The validator's probe results, fill rate metrics, and taxonomy feedback are similarly ephemeral — only `products.jsonl` and `summary.json` (written by the scraper's own persist hooks) survive.

When a scraper degrades months later, there is no diagnostic data to understand why label coverage was borderline, which labels were unmapped, which probes failed, or what taxonomy feedback was proposed. Re-running label discovery from scratch is the only option.

## Solution

Persist diagnostic output from the label discoverer and validator as JSON files in the existing `output/` directory, written by the orchestrator after each sub-agent dispatch.

## Output Directory (after)

```
docs/scraper-generator/{slug}/
├── scraper.py              ← code generator (existing)
├── config.json             ← orchestrator Step 4 (existing)
└── output/
    ├── products.jsonl      ← scraper persist hooks (existing)
    ├── summary.json        ← scraper persist hooks (existing)
    ├── label-discovery.json ← NEW — orchestrator writes after label discoverer returns
    └── validation.json      ← NEW — orchestrator writes after validator returns
```

## label-discovery.json

Written by the orchestrator after receiving the label discoverer's response. **Only for non-English sites** — skipped entirely for English.

The file contains the label discoverer's output contract fields, plus two orchestrator-added fields (`value_translation_dicts` and `generated_at`).

```json
{
  "site_language": "no",
  "sample_size": 87,
  "inventory_size": 143,
  "coverage": 0.78,
  "coverage_sufficient": true,
  "extension_attempts": 1,
  "per_subcategory_coverage": {
    "building_materials.lumber": 0.82,
    "building_materials.doors": 0.71
  },
  "label_map": {
    "Treslag": "wood_type",
    "Bredde": "width",
    "Lengde": "length"
  },
  "category_aliases": {
    "building_materials.lumber": { "width": "nominal_width" },
    "building_materials.doors": { "width": "unit_width" }
  },
  "value_translation_dicts": {
    "SPECIES_MAP": { "Egle": "Spruce", "Furu": "Pine" }
  },
  "unmapped_labels": ["Farge", "Materiale"],
  "discarded_labels": ["Legg i handlekurv", "Se mer"],
  "generated_at": "2026-03-16T14:30:00Z"
}
```

### Field sources

| Field | Source |
|-------|--------|
| `site_language` | Orchestrator (from catalog assessment) |
| `sample_size`, `inventory_size`, `coverage`, `coverage_sufficient`, `extension_attempts`, `per_subcategory_coverage`, `label_map`, `category_aliases`, `unmapped_labels`, `discarded_labels` | Label discoverer output contract (verbatim) |
| `value_translation_dicts` | Orchestrator-assembled from the label discoverer's translation dicts (e.g., `SPECIES_MAP`). The label discoverer mentions these in its "Notes on Translation Quality" section — this is a prerequisite change to add them to its formal output contract. |
| `generated_at` | Orchestrator (ISO 8601 timestamp at write time) |

### Prerequisite: update label discoverer output contract

Add `value_translation_dicts` (dict of dict) to the label discoverer's output contract table in `references/label-discoverer.md`. This formalizes what the sub-agent already produces informally.

On re-dispatch (coverage retry), the file is overwritten with updated results.

## validation.json

Written by the orchestrator after the validator returns with **any** status (including failures, including for English sites). Captures all four validation phases.

The orchestrator transforms the validator's output contract into a structured persistence format. The mapping is documented below.

```json
{
  "status": "pass",
  "probe_results": [
    {
      "url": "https://example.com/product/123",
      "category": "building_materials.lumber",
      "pass": true,
      "universal_fields_populated": true,
      "core_attributes_count": 5,
      "extended_attributes_count": 3
    },
    {
      "url": "https://example.com/product/456",
      "category": "building_materials.doors",
      "pass": false,
      "universal_fields_populated": true,
      "core_attributes_count": 0,
      "extended_attributes_count": 0,
      "issues": "No spec table found — product page uses image-only layout with no structured attributes"
    }
  ],
  "smoke_test_summary": {
    "total_products": 20,
    "errors_count": 0,
    "duration_seconds": 47.2,
    "core_fill_rate": 0.85,
    "extended_fill_rate": 0.60,
    "category_diversity": 3,
    "limited": true
  },
  "taxonomy_feedback": {
    "candidates_proposed": 2,
    "attributes": [
      { "key": "surface_finish", "frequency": 0.90, "example_values": ["Matte", "Glossy"] }
    ]
  },
  "final_verification_summary": {
    "sample_size": 50,
    "total_products": 50,
    "errors_count": 0,
    "duration_seconds": 142.8,
    "limited": true
  },
  "label_coverage_at_probe": 0.76,
  "fix_cycles_used": { "probe": 1, "fill_rate": 0 },
  "generated_at": "2026-03-16T14:45:00Z"
}
```

### Field mapping from validator output contract

| Persisted field | Validator output contract field | Notes |
|----------------|-------------------------------|-------|
| `status` | `status` | Verbatim |
| `probe_results` | `probe_results` | Verbatim |
| `smoke_test_summary` | `smoke_test_summary` | Verbatim. `limited` comes from the scraper's teardown summary — `true` when `--limit` was the binding constraint. |
| `taxonomy_feedback` | `taxonomy_feedback` | Verbatim |
| `final_verification_summary` | `final_verification_summary` | Verbatim. `limited` same as smoke test. |
| `label_coverage_at_probe` | `label_coverage_at_probe` | Verbatim |
| `fix_cycles_used` | `fix_cycles_used` | Verbatim |
| `generated_at` | — | Orchestrator-added (ISO 8601 timestamp) |

### Nullable fields

- `taxonomy_feedback` — `null` when skipped (no extra attribute appears on >80% of products, or test failed)
- `final_verification_summary` — `null` when Phase 4 was skipped (computed sample size ≤ 20, so smoke test output is sufficient)
- `label_coverage_at_probe` — `null` for English sites
- `probe_results[].issues` — string field, present only when `pass: false`
- `smoke_test_summary` — `null` if validator did not reach Phase 2 (e.g., returned `probe_failed`)

On re-dispatch (after code-generator fix), the file is overwritten with the new attempt's results. The file always reflects the last validation run.

## Who writes, when

The **orchestrator** writes both files. Sub-agents return structured data in-memory; the orchestrator persists after each dispatch. Sub-agents remain pure — they don't know about file paths.

| File | Written after | Overwritten on |
|------|--------------|----------------|
| `label-discovery.json` | Label discoverer returns (before code-generator dispatch) | Re-dispatch for coverage retry |
| `validation.json` | Validator returns (any status, including English sites) | Re-dispatch after code-generator fix |

## Changes needed

1. **Label discoverer** (`references/label-discoverer.md`) — add `value_translation_dicts` to the output contract table (prerequisite).
2. **Orchestrator** (`references/orchestrator.md`) — add "persist the label discovery diagnostic output" after the label discovery dispatch block, and "persist the validation diagnostic output" after the validation dispatch block. These instructions must remain harness-agnostic (use logical names like "the label discovery diagnostic file", not file paths). The SKILL.md maps logical names to concrete paths.
3. **SKILL.md** (`.claude/skills/scraper-generator/SKILL.md`) — add two rows to the File locations table: `Label discovery diagnostics (output)` → `docs/scraper-generator/{slug}/output/label-discovery.json` and `Validation diagnostics (output)` → `docs/scraper-generator/{slug}/output/validation.json`. Add a wiring bullet mapping the orchestrator's logical names to these paths.
4. **No changes to code-generator or validator** — their output contracts already cover the persisted fields (except the prerequisite in #1).

## What doesn't change

- `scraper.py` persistence — handled by SKILL.md wiring
- `config.json` persistence — handled by orchestrator Step 4
- `products.jsonl` + `summary.json` — written by the scraper's persist hooks at runtime
