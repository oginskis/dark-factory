# Scraper Sub-Agent Output Persistence Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Persist label discoverer and validator diagnostic output as JSON files so scraper degradation can be debugged without re-running discovery.

**Architecture:** The orchestrator writes two new JSON files (`label-discovery.json`, `validation.json`) to the existing `output/` directory after each sub-agent dispatch. Sub-agents are unchanged — they return data in-memory and the orchestrator handles persistence.

**Tech Stack:** Markdown (skill/workflow files only — no code changes)

**Spec:** `docs/superpowers/specs/2026-03-16-scraper-subagent-output-persistence-design.md`

---

## Chunk 1: All changes

### Task 1: Add `value_translation_dicts` to label discoverer output contract

**Files:**
- Modify: `.claude/skills/scraper-generator/references/label-discoverer.md`

- [ ] **Step 1: Add field to output contract table**

In the `## Output Contract` table (after the `coverage_sufficient` row, before the closing paragraph), add:

```markdown
| `value_translation_dicts` | dict | Static translation dicts for closed value sets (e.g., `{"SPECIES_MAP": {"Egle": "Spruce", "Furu": "Pine"}}`). Empty dict if no closed value sets found. |
```

- [ ] **Step 2: Verify the table has 11 rows**

Read the file and count output contract fields. Expected: 11 (the original 10 + `value_translation_dicts`).

---

### Task 2: Add persist instructions to orchestrator

**Files:**
- Modify: `.claude/skills/scraper-generator/references/orchestrator.md`

- [ ] **Step 1: Add label discovery persistence instruction**

After the `### Dispatch conditions` block under `## Dispatch: Label Discovery (non-English only)` (after line 181, before the `---` separator), insert:

```markdown

### Diagnostic persistence

After the label discoverer returns (regardless of `coverage_sufficient`), persist its output as the label discovery diagnostic file. Include all output contract fields verbatim (including `value_translation_dicts`), plus two orchestrator-added fields:
- `site_language` — the ISO 639-1 code from the catalog assessment
- `generated_at` — ISO 8601 timestamp

On re-dispatch (coverage retry), overwrite the file with the updated results.
```

- [ ] **Step 2: Add validation persistence instruction**

After the `### Retry state machine` block under `## Dispatch: Validation` (after the closing ``` of the retry state machine code block, before the `---` separator), insert:

```markdown

### Diagnostic persistence

After the validator returns (any status, including failures), persist its output as the validation diagnostic file. Include all output contract fields verbatim, plus:
- `generated_at` — ISO 8601 timestamp

On re-dispatch (after code-generator fix), overwrite the file with the new attempt's results. The file always reflects the last validation run. Write this file for both English and non-English sites.
```

- [ ] **Step 3: Verify orchestrator remains harness-agnostic**

```bash
grep -ciE "docs/|\.claude/|WebSearch|WebFetch|Playwright" .claude/skills/scraper-generator/references/orchestrator.md
```

Expected: 0 matches. The new instructions use logical names ("the label discovery diagnostic file", "the validation diagnostic file"), not file paths.

---

### Task 3: Add file locations and wiring to SKILL.md

**Files:**
- Modify: `.claude/skills/scraper-generator/SKILL.md`

- [ ] **Step 1: Add rows to File locations table**

After the `Run summary (output)` row in the File locations table, add:

```markdown
| Label discovery diagnostics (output) | `docs/scraper-generator/{slug}/output/label-discovery.json` |
| Validation diagnostics (output) | `docs/scraper-generator/{slug}/output/validation.json` |
```

- [ ] **Step 2: Add wiring bullet for diagnostic persistence**

In the `## Workflow` section, after the bullet about data persistence (the one starting with "Data persistence: read the persist hook implementations file..."), add:

```markdown
- Diagnostic persistence: after the label discoverer returns (non-English sites only), write its output plus `site_language` and `generated_at` as JSON to the label discovery diagnostics path. After the validator returns (any status, any language), write its output plus `generated_at` as JSON to the validation diagnostics path. On re-dispatch, overwrite the previous file.
```

- [ ] **Step 3: Verify SKILL.md stays under 500 lines**

```bash
wc -l .claude/skills/scraper-generator/SKILL.md
```

Expected: under 500 lines (currently ~89, adding ~4 lines).

---

### Task 4: Run verification

- [ ] **Step 1: Run verify_skill.py**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py scraper-generator
```

Expected: 0 critical, 0 moderate issues.

- [ ] **Step 2: Run full verification**

```bash
uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
```

Expected: scraper-generator passes. Only pre-existing catalog-detector word count warning.

- [ ] **Step 3: Present diff for review**

Show `git diff` for all modified files before any commit.
