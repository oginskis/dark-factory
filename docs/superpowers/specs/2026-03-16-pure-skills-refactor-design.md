# Pure Skills Refactor — Design Spec

## Problem

The dark-factory pipeline uses a two-file pattern: a thin SKILL.md wrapper in `.claude/skills/` paired with a "harness-agnostic" agent file in `agents/`. This was designed for portability — agents could run in Claude Code today and a K8s service tomorrow.

This creates real costs:
- **Two files to maintain per stage** with an ambiguous boundary between them
- **Convention overhead** — skill-creator-local's 567-line SKILL.md spends 3 conventions defining what goes where
- **Cross-directory references** — skills point to `agents/{name}.md`, agent files use logical names that skills must map
- **Wiring boundary debates** — "does this belong in the wrapper or the agent?" is the most common source of misplacement (the scraper-generator wrapper had ballooned to 112 lines with reasoning content)

The portability argument no longer justifies the cost. As of December 2025, Anthropic published Agent Skills as an open standard. The SKILL.md *format* (frontmatter, progressive disclosure, references/) is natively supported by Claude Code, OpenAI Codex CLI, Google Gemini CLI, GitHub Copilot, Cursor, and Kiro (AWS). The *execution wiring* (Agent tool dispatch, Bash tool timeouts, `/skill-name` invocation, `uv run` commands) remains Claude Code-specific and would need adaptation for other harnesses. We accept this trade-off: the format is portable for discoverability; the execution content targets Claude Code, which is our only harness. Maintaining a separate "harness-agnostic" layer for theoretical portability to harnesses we don't use is unnecessary indirection.

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
    ├── SKILL.md                    ← skill overview, workflows, script docs
    ├── references/
    │   └── conventions.md          ← detailed convention definitions (Conventions 1-4)
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

### Key change: soft boundary replaces hard boundary

The old pattern had a hard boundary: "wrapper = HOW, agent = WHAT." This created constant misplacement debates.

The new pattern uses a **soft guideline**: SKILL.md focuses on wiring (file paths, tool instructions, execution commands, escalation presentation). `references/` focuses on reasoning (steps, decisions, verification gates). This is a guideline, not a hard rule — when a reference file benefits from a specific path or tool mention, that's fine. The primary organizing principle is **progressive disclosure**: keep SKILL.md under 500 lines, move detail to `references/`.

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

### References files and harness-specific content

Unlike agent files which had a strict "no tool names, no file paths" rule, references files have no hard restriction. The soft guideline is: **prefer capability-focused language in references/ files** (say "search the web" not "use WebSearch tool"), but include harness-specific details when they genuinely improve clarity. This keeps references/ files readable and broadly useful while eliminating the enforcement overhead of a hard rule.

**Exception: sub-agent reference files** (like `label-discoverer.md`, `code-generator.md`, `validator.md`) that are dispatched via the Agent tool into isolated context windows still benefit strongly from being lean and tool-name-free. These files become the sub-agent's entire instruction set — polluting them with harness wiring wastes context tokens. The soft guideline applies more strictly here.

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

**Invocation mechanism:** The orchestrator uses the Skill tool to invoke each stage (e.g., `Skill: product-classifier, args: "{slug}"`). This loads the stage skill's SKILL.md into the current conversation context as an inline expansion — NOT a sub-agent dispatch. The orchestrator and stage skill share the same conversation, which preserves the current behavior: escalations bubble up to the user, stage outputs are visible to subsequent stages, and the orchestrator can inspect results before proceeding.

**$ARGUMENTS passing:** When the orchestrator invokes a stage skill with args, the stage skill receives those args as its `$ARGUMENTS`. The slug flows through automatically.

**Context management:** Each stage skill loads its SKILL.md + references/workflow.md into context. To prevent context pressure from accumulating across 4 stages, the orchestrator should treat each stage as a discrete unit — the model naturally processes one stage at a time since each skill invocation triggers reading and following the stage's workflow before returning to the orchestrator.

**Risk note:** This invocation mechanism should be validated during Phase 3 implementation by testing a single stage invocation (e.g., `/product-classifier {slug}` from within a product-discovery session) before rewriting all 4 stages. If skill invocation causes unexpected behavior (competing instructions, context confusion), the fallback is explicit `Read` of the stage SKILL.md: "Read `.claude/skills/product-classifier/SKILL.md` and follow its instructions." This achieves the same colocation benefit without changing execution semantics.

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

**Estimated new size:** SKILL.md ~200 lines (skill overview, workflows, script docs) + `references/conventions.md` ~200 lines (convention definitions). Total ~400 lines of content (down from 567), split across two files for progressive disclosure. This leaves headroom for future convention additions without approaching the 500-line SKILL.md limit.

### verify_skill.py updates

**Structural changes:**
- `find_repo_root()` currently requires `agents/` to exist (line 30). Remove this check — locate repo root using `.claude/skills/` only.
- Remove `AGENTS_DIR` constant. Add `REFERENCES_DIR` helper: `SKILLS_DIR / skill_name / "references"`.
- `check_skill_wrapper()`: replace check for `agents/{skill_name}.md` in content with check for `references/workflow.md` or `references/orchestrator.md`.

**Check function changes:**
- `check_agent_file()` → rename to `check_workflow_reference()`. Read from `references/workflow.md` (or `references/orchestrator.md` for decomposed skills). Keep: step structure, decision blocks, self-verification, format rules, decision-step references. Remove: the hard environment agnosticism checks (no tool names, no hardcoded paths) — replace with an advisory-level note when tool names appear in workflow references.
- `check_subagent_pattern()` → repoint from `AGENTS_DIR / skill_name` to `SKILLS_DIR / skill_name / "references"`. Keep: sub-agent files must not have Decision blocks, word count ≤2,500. Soften: tool name and path checks to advisory level for sub-agent files.
- `check_cross_references()` → update to check `references/` paths instead of `agents/` paths. Validate that cross-skill references using full paths (`.claude/skills/{name}/references/{file}`) resolve to existing files.

**Keep unchanged:** word count checks, escalation alignment, report template compliance, orchestrator alignment.
**Add:** check that every file referenced as `references/{name}` in SKILL.md exists in the skill's `references/` directory.

## Cross-Reference Updates

| File | Current reference | New reference |
|---|---|---|
| eval-generator SKILL.md | `agents/scraper-generator/code-generator.md` | `.claude/skills/scraper-generator/references/code-generator.md` |
| catalog-detector SKILL.md | `agents/scraper-generator/code-generator.md` | `.claude/skills/scraper-generator/references/code-generator.md` |
| product-taxonomy SKILL.md | "see scraper-generator skill for the full four-level product record format" | "see `.claude/skills/scraper-generator/references/code-generator.md`" |
| product-discovery SKILL.md | "see scraper-generator skill for the canonical definition" | "see `.claude/skills/scraper-generator/references/code-generator.md`" |
| product-discovery SKILL.md | "see the slug derivation algorithm in `agents/product-classifier.md` Step 1" | "see `.claude/skills/product-classifier/references/workflow.md` Step 1" |
| CLAUDE.md Key Directories | `agents/` listed as key directory | Remove `agents/` entry |
| CLAUDE.md Git table | "`agents/` are always tracked" | Remove `agents/` from tracking note |
| CLAUDE.md Conventions | "Skill wrappers and agent files are a paired two-file pattern" | Rewrite for pure-skills pattern |
| CLAUDE.md Conventions | "Agent files must be harness-agnostic: no tool names, no file paths" | Remove (no longer applicable) |

**Note:** Cross-skill references use full paths (`.claude/skills/{name}/references/{file}`) rather than prose descriptions ("in {name} skill"). Full paths are unambiguous, grep-able, and verifiable by verify_skill.py.

**Note:** Historical spec and plan files under `docs/superpowers/` that reference `agents/` paths are left as-is — they document the state at the time they were written.

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

Remove from Conventions:
```
- Skill wrappers and agent files are a paired two-file pattern. See `/skill-creator-local` for the full convention spec.
- Agent files must be harness-agnostic: no tool names, no file paths, no user-facing language.
```

Replace with:
```
- Each pipeline skill is self-contained under `.claude/skills/{name}/` with SKILL.md + references/. See `/skill-creator-local` for conventions.
```

Update Architecture section to reflect pure-skills pattern.

## What this refactor does NOT change

- Pipeline stages, their inputs, outputs, and decision logic
- The product record format (canonical definition moves files but content is identical)
- The scraper-generator decomposition (orchestrator + 3 sub-agents — just relocated)
- The product-discovery stage sequence and stop conditions
- The escalation format and user options
- Any generated output (scrapers, configs, eval configs, reports)
- The product-taxonomy and its SKU schemas

Only file layout, SKILL.md structure, and skill-creator-local conventions change.

## Migration Sequencing

**Atomicity requirement:** All phases must be completed on a single feature branch and merged as one unit. Between Phase 1 (move files) and Phase 2 (rewrite SKILL.md references), the system is broken — SKILL.md files point to `agents/{name}.md` but those files no longer exist. There is no safe incremental migration.

**Dependency:** The scraper-generator decomposition branch must be merged first (or completed simultaneously on the same branch), since this refactor moves the decomposed sub-agent files.

**Git history:** `git mv` from `agents/{name}.md` to `.claude/skills/{name}/references/workflow.md` changes both directory and filename. Git's rename detection may not track this as a rename. `git log --follow` may lose history. This is an accepted trade-off.

### Phase 1: Move files (mechanical)

Move all agent files to their new locations under `references/`. This is a pure file move — content unchanged. Use `git mv` where possible.

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
