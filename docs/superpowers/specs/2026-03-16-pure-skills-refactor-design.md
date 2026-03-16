# Pure Skills Refactor — Design Spec

## Problem

The dark-factory pipeline uses a two-file pattern: a thin SKILL.md wrapper in `.claude/skills/` paired with a "harness-agnostic" agent file in `agents/`. This was designed for portability — agents could run in Claude Code today and a K8s service tomorrow.

This creates real costs:
- **Two files to maintain per stage** with an ambiguous boundary between them
- **Convention overhead** — skill-creator-local's 567-line SKILL.md spends 3 conventions defining what goes where
- **Cross-directory references** — skills point to `agents/{name}.md`, agent files use logical names that skills must map
- **Wiring boundary debates** — "does this belong in the wrapper or the agent?" is the most common source of misplacement (the scraper-generator wrapper had ballooned to 112 lines with reasoning content)

The portability argument no longer holds. As of December 2025, Anthropic published Agent Skills as an open standard. SKILL.md is now natively supported by Claude Code, OpenAI Codex CLI, Google Gemini CLI, GitHub Copilot, Cursor, and Kiro (AWS). The skills format IS the portable format — separate "harness-agnostic" agent files are unnecessary indirection.

## Solution

Eliminate the `agents/` directory. Move all agent content into `references/` files under each skill following the standard skills progressive disclosure pattern. Rewrite skill-creator-local conventions for the pure-skills model. Update the product-discovery orchestrator to invoke stage skills via `/skill-name`.

## Architecture

### Before

```
.claude/skills/{name}/SKILL.md    ← thin wrapper (file paths, tool wiring)
agents/{name}.md                  ← reasoning (steps, decisions, verification)
```

SKILL.md says: "Read and follow the agent instructions in `agents/{name}.md`."

### After

```
.claude/skills/{name}/
├── SKILL.md                      ← integrated instructions + wiring
├── references/
│   └── workflow.md               ← detailed reasoning (steps, decisions, verification)
├── scripts/                      ← verification, utilities
└── assets/                       ← templates
```

SKILL.md says: "Read and follow `references/workflow.md`."

Everything for a skill lives in one directory. No cross-directory references.

### Target directory layout

```
.claude/skills/
├── product-classifier/
│   ├── SKILL.md
│   └── references/
│       └── workflow.md
│
├── catalog-detector/
│   ├── SKILL.md
│   └── references/
│       └── workflow.md
│
├── scraper-generator/
│   ├── SKILL.md
│   └── references/
│       ├── orchestrator.md
│       ├── label-discoverer.md
│       ├── code-generator.md       ← canonical product record format
│       ├── validator.md
│       └── persist-hooks.md        ← already exists here
│
├── eval-generator/
│   ├── SKILL.md
│   └── references/
│       └── workflow.md
│
├── product-discovery/
│   └── SKILL.md                    ← invokes /product-classifier, /catalog-detector,
│                                      /scraper-generator, /eval-generator
│
├── product-taxonomy/
│   ├── SKILL.md                    ← already standalone
│   └── references/
│       └── research-methodology.md ← already exists
│
└── skill-creator-local/
    ├── SKILL.md                    ← simplified conventions
    └── scripts/
        └── verify_skill.py
```

**Deleted:** The entire `agents/` directory.

## SKILL.md Integrated Template

Each pipeline skill follows this structure:

```markdown
---
name: {skill-name}
description: >
  {What it does. What it produces. Trigger phrases. Prerequisites. Pipeline redirect.}
user-invocable: true
---

# {Skill Title}

{Brief context — role in the pipeline, what it does.}

## Input

`$ARGUMENTS` is {description} (e.g., `{example}`).

## File locations

| Resource | Path |
|----------|------|
| {Upstream input} | `docs/{upstream-stage}/{slug}.md` |
| {Other inputs} | `docs/...` |
| {Output} | `docs/{this-stage}/{slug}.md` |

## Workflow

Read and follow `references/workflow.md`.

{Harness-specific instructions integrated here:}
- Provide file paths from the table above when the workflow references logical resources
- {Tool instructions — web search, Playwright, etc.}
- {Execution commands with flags and timeouts}
- {Sub-agent dispatch instructions, if applicable}

## Escalation handling

{Escalation format template}
{User options per decision}

## Notes

File-driven skill — no database or external services required.
```

### Key change: no wiring boundary

The old pattern had a hard boundary: "wrapper = HOW, agent = WHAT." This created constant misplacement debates.

The new pattern has one simple rule: **progressive disclosure**. If SKILL.md stays under 500 lines, the instruction can go there. If it's getting long, move detail to `references/`. There's no purity question.

## Workflow Reference Structure

The `references/workflow.md` file (formerly the agent file) keeps the same internal structure:

```markdown
# {Stage Name} Workflow

**Input:** {what the workflow receives}
**Output:** {what it produces}

---

## Step 1: {First Action}
{Instructions}
{Decision references}

---

## Step N: Self-Verification
{Quality gates table}

---

## Decisions
{All decision blocks}
```

The content of these files is unchanged from the current agent files — they just move from `agents/{name}.md` to `.claude/skills/{name}/references/workflow.md`.

### References files CAN include harness-specific content

Unlike agent files which had a strict "no tool names, no file paths" rule, references files have no such restriction. In practice, keeping them capability-focused is good for readability, but it's not a hard convention. If a reference file benefits from mentioning a specific tool or path, that's fine.

## Scraper Generator Decomposition

The decomposition completed in this branch maps directly:

| Current | New |
|---|---|
| `agents/scraper-generator.md` | `references/orchestrator.md` |
| `agents/scraper-generator/label-discoverer.md` | `references/label-discoverer.md` |
| `agents/scraper-generator/code-generator.md` | `references/code-generator.md` |
| `agents/scraper-generator/validator.md` | `references/validator.md` |

The SKILL.md says "Read and follow `references/orchestrator.md`" and lists the sub-agent files for dispatch. The orchestrator.md directs when to dispatch each sub-agent; the SKILL.md provides the Agent tool mechanics.

### Decomposition pattern (generalized)

When a workflow reference exceeds ~3,000 words, decompose it:

```
.claude/skills/{name}/
├── SKILL.md
└── references/
    ├── orchestrator.md          ← state machine, contracts, decisions
    ├── {phase-1}.md             ← sub-agent (focused task)
    ├── {phase-2}.md             ← sub-agent
    └── {phase-3}.md             ← sub-agent
```

Same decomposition criteria as before (distinct cognitive tasks, defined outputs, independent failure). The only change is the file location.

## Product Discovery Orchestrator

The product-discovery SKILL.md changes from reading agent files to invoking stage skills:

**Before:**
```markdown
## Stage 1: Product Classifier
Read file locations from `.claude/skills/product-classifier/SKILL.md`,
then read and follow `agents/product-classifier.md` in full.
```

**After:**
```markdown
## Stage 1: Product Classifier
Invoke `/product-classifier {slug}`.
```

**Invocation mechanism:** `/skill-name` is an inline skill invocation — it loads the stage skill's SKILL.md into the current conversation context. This is NOT a sub-agent dispatch. The orchestrator and stage skill share the same conversation, which preserves the current behavior: escalations bubble up to the user within the same session, stage outputs are visible to subsequent stages, and the orchestrator can inspect results before proceeding to the next stage.

Each stage is a self-contained skill invocation. The orchestrator keeps:
- Stage sequence and dependency logic
- Per-stage stop conditions
- Escalation format template
- Pipeline summary template

The orchestrator no longer needs to read file locations or agent files — each stage skill handles its own wiring.

## skill-creator-local Convention Rewrite

### Current conventions (two-file pattern)

| # | Convention | Lines |
|---|---|---|
| 1 | Skill Wrapper Structure | ~90 lines |
| 2 | Agent File Structure | ~80 lines |
| 3 | Cross-File Reference Integrity | ~40 lines |
| 4 | Report Templates | ~30 lines |
| 5 | Orchestrator Integration | ~20 lines |

Plus: wiring boundary definition, sub-agent dispatch wiring, sub-agent reference integrity, change routing table.

### New conventions (pure-skills pattern)

| # | Convention | What it covers |
|---|---|---|
| 1 | Skill Structure | Integrated SKILL.md template (frontmatter, input, file locations, workflow pointer, escalation handling). Replaces old Convention 1. |
| 2 | Workflow Reference Structure | references/workflow.md template (steps, decisions, verification gates, report templates, format rules). Replaces old Convention 2. Absorbs Convention 4 (report templates). |
| 3 | Reference Integrity | Referenced files must exist. Escalation decisions align between SKILL.md and workflow.md. Canonical definition pointers are valid. Replaces old Convention 3. |
| 4 | Orchestrator Integration | product-discovery invokes `/skill-name`, stop conditions must align. Simplified from old Convention 5. |

**Sections that disappear entirely:**
- "What belongs in Claude Code wiring" — no more boundary question
- "Sub-agent dispatch (orchestrator pattern)" — becomes a note in Convention 2 about decomposition
- "Change Routing: What Goes Where" — gone (no wrapper vs agent decision)
- The entire "Three rules of environment agnosticism" section — no longer a hard rule

**Estimated new size:** ~350 lines (down from 567).

### verify_skill.py updates

- Check for `references/workflow.md` (or `references/orchestrator.md` for decomposed skills) instead of `agents/{name}.md`
- Sub-agent checks look in `references/` instead of `agents/{name}/`
- Remove wrapper↔agent cross-reference checks
- Keep: word count checks, escalation alignment, decision-step references, report template compliance
- Add: check that all files listed in `references/` exist

## Cross-Reference Updates

| File | Current reference | New reference |
|---|---|---|
| eval-generator SKILL.md | `agents/scraper-generator/code-generator.md` | `references/code-generator.md` in scraper-generator skill |
| catalog-detector SKILL.md | `agents/scraper-generator/code-generator.md` | `references/code-generator.md` in scraper-generator skill |
| product-taxonomy SKILL.md | "see scraper-generator skill for the full four-level product record format" | "see scraper-generator skill's `references/code-generator.md`" (make pointer specific) |
| product-discovery SKILL.md | "see scraper-generator skill for the canonical definition" | "see scraper-generator skill's `references/code-generator.md`" (make pointer specific) |
| CLAUDE.md | References `agents/` directory | Remove agents/ from Key Directories, update Git tracking table |

## CLAUDE.md Updates

Remove from Key Directories:
```
- `agents/` — Harness-agnostic agent files (shared reasoning, no tool names or file paths)
```

Update Git tracking table:
```
`.claude/` (skills, settings) and `agents/` are always tracked
```
→
```
`.claude/` (skills, settings) is always tracked
```

Update Architecture section to reflect pure-skills pattern.

## Migration Sequencing

### Phase 1: Move files (mechanical)

Move all agent files to their new locations under `references/`. This is a pure file move — content unchanged.

1. `agents/product-classifier.md` → `.claude/skills/product-classifier/references/workflow.md`
2. `agents/catalog-detector.md` → `.claude/skills/catalog-detector/references/workflow.md`
3. `agents/eval-generator.md` → `.claude/skills/eval-generator/references/workflow.md`
4. `agents/scraper-generator.md` → `.claude/skills/scraper-generator/references/orchestrator.md`
5. `agents/scraper-generator/label-discoverer.md` → `.claude/skills/scraper-generator/references/label-discoverer.md`
6. `agents/scraper-generator/code-generator.md` → `.claude/skills/scraper-generator/references/code-generator.md`
7. `agents/scraper-generator/validator.md` → `.claude/skills/scraper-generator/references/validator.md`
8. Delete `agents/` directory

### Phase 2: Rewrite 4 pipeline SKILL.md files

Rewrite product-classifier, catalog-detector, scraper-generator, and eval-generator SKILL.md files to the integrated template. Each replaces the thin wrapper with the full integrated pattern.

### Phase 3: Rewrite product-discovery orchestrator

Replace "read file locations + read agent file" per stage with "invoke `/skill-name {slug}`". Simplify the SKILL.md since stage skills are now self-contained.

### Phase 4: Rewrite skill-creator-local

Rewrite conventions 1-5 for the pure-skills pattern. Update verify_skill.py for the new file layout. Run `verify_skill.py --all`.

### Phase 5: Update cross-references and CLAUDE.md

Update canonical product record format pointers. Update CLAUDE.md to remove agents/ references. Update any remaining cross-references.

### Phase 6: Verify

Run `verify_skill.py --all` → 0 critical, 0 moderate. Test with a real company.
