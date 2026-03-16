# Pure Skills Refactor — Design Spec

## Problem

The pipeline uses a two-file pattern: `.claude/skills/{name}/SKILL.md` (wrapper) + `agents/{name}.md` (agent reasoning). This creates cross-reference overhead (wrapper↔agent alignment, Convention 1-3 enforcement, wiring boundary policing) and a conceptual split (HOW vs WHAT) that no longer serves its original purpose — harness portability. Since SKILL.md is now an open standard supported by 6+ agent harnesses (Claude Code, Codex, Gemini CLI, Copilot, Cursor, Kiro, PydanticAI), the skills format IS the portable format. The separate `agents/` directory is unnecessary indirection.

## Solution

Move all agent content into `references/` under each skill directory. Delete `agents/` entirely. Simplify skill-creator-local conventions by removing the wiring boundary and collapsing 5 conventions to 4. Update verify_skill.py. Clean break — no backwards compatibility shims, stubs, or redirects.

## Target Architecture

Every pipeline stage is a self-contained skill directory:

```
.claude/skills/{name}/
├── SKILL.md              ← Entry point (file paths, tools, escalation, workflow pointer)
└── references/
    ├── workflow.md        ← Core reasoning (steps, decisions, report templates)
    └── {other}.md         ← Additional reference files as needed
```

For decomposed skills (scraper-generator):
```
.claude/skills/scraper-generator/
├── SKILL.md
└── references/
    ├── orchestrator.md
    ├── label-discoverer.md
    ├── code-generator.md
    ├── validator.md
    └── persist-hooks.md
```

The product-discovery orchestrator invokes stage skills directly (`/product-classifier`, `/catalog-detector`, etc.) instead of reading agent files.

## skill-creator-local Simplification

### Convention restructuring

| Current | After |
|---------|-------|
| Convention 1: Skill Wrapper Structure | Convention 1: Skill Structure (merged wrapper+agent rules) |
| Convention 2: Agent File Structure | Convention 2: Workflow File Structure (renamed) |
| Convention 3: Cross-File Reference Integrity | Convention 3: Cross-Reference Integrity (simplified) |
| Convention 4: Report Templates | Folded into Convention 2 |
| Convention 5: Orchestrator Integration | Convention 4: Orchestrator Integration (renumbered) |

### What's deleted

- "What belongs in Claude Code wiring" section and HOW vs WHAT test
- "Sub-agent dispatch wiring" as a separate section (folded into decomposition in Convention 2)
- "Sub-agent reference integrity" as a separate section (folded into Convention 3)
- 4 items from the 12-item self-review checklist (boundary-specific items)

### The simplified boundary rule

"SKILL.md is the entry point — file paths, tools, escalation handling, and a pointer to the workflow. If it exceeds ~100 lines of wiring, move detail to references/. Workflow files contain reasoning, steps, decisions, and templates."

No HOW vs WHAT test. No "would this be useful to a K8s service?" litmus test. Just progressive disclosure.

## verify_skill.py Updates

| Check | Current | After |
|-------|---------|-------|
| Workflow file exists | `agents/{name}.md` | `references/workflow.md` or `references/orchestrator.md` |
| Workflow reference in SKILL.md | `agents/{name}.md` in SKILL.md | `references/workflow.md` or `references/orchestrator.md` |
| Sub-agent directory | `agents/{name}/` | Sub-agent files in `references/` matching sub-agent pattern |
| Harness-agnosticism | Checks agent files | Checks workflow and sub-agent files (same rules, different paths) |
| Word count | `agents/{name}.md` | `references/workflow.md` or `references/orchestrator.md` |
| SKILL.md structure | `## Claude Code wiring` | `## Workflow` starting with `Read and follow references/` |

Cross-reference integrity, orchestrator alignment, decision block validation, report template checks, and escalation format checks remain unchanged — just pointed at different paths.

## Migration (completed)

All migration work was completed in the same session as the scraper-generator decomposition:

1. **`agents/` directory deleted** — clean break, no stubs or redirects
2. **`skill-creator-local/SKILL.md` rewritten** — 4-convention structure, 12-item self-review checklist
3. **`references/conventions.md` rewritten** — 4 simplified conventions
4. **`verify_skill.py` updated** — all `agents/` path references changed to `references/` paths
5. **All stale `agents/` references swept** — zero remaining in SKILL.md files, product-discovery, CLAUDE.md
6. **`verify_skill.py --all` passes** — 0 critical, 0 moderate

### What did NOT change

- Workflow file content (migrated from agents/ to references/)
- Sub-agent file content (migrated from agents/scraper-generator/ to references/)
- Product-discovery orchestrator (uses skill invocation)
- Output directory structure, product taxonomy, eval script
- Scraper-generator decomposition (preserved)

### No backwards compatibility

- `agents/` directory deleted outright
- No stubs, redirects, "moved to" comments, or re-exports
- All references updated in one shot
