---
name: skill-creator-local
description: >
  Create or improve pipeline skills in this repository.
  Enforces the established skill conventions, proper cross-file references,
  and report template structures used throughout the product discovery pipeline.
  Use this skill when creating a new pipeline stage, improving an existing skill,
  or reviewing skill files for convention compliance —
  "create a new skill for X", "add a pipeline stage", "review skill conventions",
  "improve the scraper-generator skill", "make sure this skill follows our patterns",
  "check convention compliance", "verify cross-references", "audit skill structure".
  Do NOT use for the generic skill-creator plugin — this is specific to the dark-factory repo conventions.
user-invocable: true
---

# Skill Creator (Local)

Create and improve pipeline skills following the conventions established in this repository.

## Input

`$ARGUMENTS` describes what to create or improve (e.g., "create a new skill for X", "review catalog-detector", "improve scraper-generator conventions").

## When to use this skill

- Creating a new pipeline stage skill
- Improving or reviewing an existing skill for convention compliance
- Adding new decisions, stop conditions, or report sections to an existing skill
- Verifying cross-file references between skills and the orchestrator

## Architecture: Skill Pattern

Pipeline skills use a SKILL.md with a `references/` directory:

```
.claude/skills/{name}/
├── SKILL.md              <- Skill entry point (file paths, tools, escalation handling)
└── references/
    ├── workflow.md        <- Core reasoning (steps, decisions, report templates)
    └── {other}.md         <- Additional reference files as needed
```

The **SKILL.md** is the entry point: provides file paths, maps logical resource names, specifies tools, and describes escalation/stop behavior.

The **references/workflow.md** contains all reasoning, decision logic, and report templates. It describes *what to do and decide* — SKILL.md handles *how to interact*.

The **product-discovery orchestrator** (`.claude/skills/product-discovery/SKILL.md`) chains all stages. When adding a new stage, update the orchestrator too.

### Standalone skills

Some skills don't need the full pattern — they're utility skills with no workflow reference file. Examples: `product-taxonomy` (all logic inline in SKILL.md with `references/`), `skill-creator-local` (this skill). Use standalone when:
- The skill is a meta-tool (creates/reviews other skills) rather than a pipeline stage
- The reasoning is simple enough to fit in SKILL.md without a workflow file

Standalone skills still follow the general best practices below but skip Conventions 1-3 since those are specific to the pipeline pattern.

---

## Skill Writing Best Practices

### Purpose-Driven Design

Every skill should answer: **what does the downstream consumer need?** Design the output for the next stage in the pipeline, not as a generic report. If a skill's output doesn't directly enable the next step, it's doing work for its own sake.

Example: catalog-detector doesn't produce a site survey — it produces an extraction blueprint with verified selectors, API endpoints, and category tree that the scraper-generator can translate directly into code.

### Progressive Disclosure

Skills load in three tiers. Design with this in mind:
1. **Metadata** (name + description) — always in context (~100 words). Primary triggering mechanism.
2. **SKILL.md body** — loaded when skill triggers. Keep under 500 lines. Move detail into `references/` with clear pointers.
3. **Bundled resources** — loaded on demand (unlimited size). Use `scripts/` for code, `references/` for docs, `assets/` for templates.

### Description — Be Concrete, Not Vague

The `description` field is how Claude decides whether to invoke a skill. Include trigger phrases, contexts, and near-miss redirects. State prerequisites by naming the specific upstream skill, not vague references.

| Wrong | Right |
|-------|-------|
| "for a company that has already been classified" | "for a company that already has a company report from /product-classifier" |
| "requires upstream data" | "requires a catalog assessment from /catalog-detector" |

### Writing Style

- **Explain the why** behind instructions rather than piling on rigid MUSTs. LLMs respond better to reasoning than to rules.
- **Use imperative form** — "Read the company report" not "You should read the company report."
- **Prefer examples over abstract rules** — a Correct/Wrong table communicates faster than a paragraph of constraints.
- **Keep it lean** — remove instructions that aren't pulling their weight. If a line says "Same as Step X", the step should be shared, not duplicated.

### Notes Section

The `## Notes` section should contain information that actually helps. Skill ownership, unusual behaviors, operational constraints. Drop boilerplate that applies to every skill equally — it adds noise without signal.

### Workflow Structure — Branch at the Narrow Point

When a workflow has variants (e.g., different paths for known vs. unknown inputs), identify what's actually different and share everything else:

```
Shared: Step 1 (detection/setup)
Branch: Step 2 (fast path) OR Step 3 (full investigation)  ← only this differs
Shared: Step 4 (build output)
Shared: Step 5 (write report)
Shared: Step 6 (verify)
```

Never duplicate shared steps across branches. If you're writing "Same as Step X" — that step should be shared, not in the branch. This typically cuts 30-40% of workflow length.

### Output Format Definition

When a skill produces structured output, define the exact template with Correct/Wrong tables for formatting rules.

### Domain Organization

When a skill supports multiple variants, organize by domain with a reference file per variant. Claude reads only the relevant reference file, keeping context lean.

---

## Workflow: Creating a New Pipeline Stage

1. **Draft `references/workflow.md`** following Convention 2 in `references/conventions.md`
2. **Draft SKILL.md** following Convention 1 in `references/conventions.md`
3. **Verify cross-references** per Convention 3:
   - Every logical resource name in workflow -> mapped in SKILL.md
   - Every decision in workflow -> reflected in SKILL.md workflow section
   - Every stop condition -> reflected in orchestrator
4. **Update the orchestrator** per Convention 4
5. **Run verification:** `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py <skill-name>`
6. **Test and optimize:** Use `/skill-creator:skill-creator` to run eval prompts
7. **Self-review checklist:**

| # | Check |
|---|-------|
| 1 | Workflow heading ends with "Workflow" (e.g., `# Catalog Detector Workflow`) |
| 2 | Workflow has `**Input:**` and `**Output:**` fields, `## Context`, `## Boundaries`, `## Decisions` |
| 3 | Every step that can stop/escalate references the decision by name |
| 4 | Report template has success + stop variants (if applicable) |
| 5 | Strict format rules table present |
| 6 | Self-verification quality gates present |
| 7 | SKILL.md has one-line summary after `# Title` |
| 8 | SKILL.md `## Workflow` starts with `Read and follow references/workflow.md.` |
| 9 | SKILL.md File locations table covers every file the workflow reads or writes |
| 10 | SKILL.md escalation template says "workflow" not "agent" |
| 11 | Orchestrator's stop list matches workflow decisions |
| 12 | Logical resource names are unambiguous (full names, not short forms) |
| 13 | No duplicated steps across workflow branches — shared logic is shared |
| 14 | Output designed for downstream consumer, not as a generic survey |
| 15 | Prerequisites name the specific upstream skill |

## Workflow: Reviewing an Existing Skill

1. **Run the verification script first** — it catches structural issues programmatically:
   ```bash
   uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py <skill-name>
   uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
   ```
2. Read both the SKILL.md and `references/workflow.md` for issues the script can't catch (clarity, flow, ambiguity)
3. Check cross-reference integrity (Convention 3 in `references/conventions.md`)
4. Check orchestrator alignment (Convention 4 in `references/conventions.md`)
5. **Check for common anti-patterns:**
   - "Same as Step X" duplication — refactor into shared steps
   - Survey-style output that doesn't serve the downstream consumer
   - Vague prerequisites ("already classified" instead of naming the skill)
   - Boilerplate notes that add no information
   - Branches that duplicate shared logic before/after the divergence point
6. Report findings organized by severity: Critical > Moderate > Minor
7. Fix issues with the user's approval

Read `references/conventions.md` for detailed convention definitions.

---

## Relationship to the Skill-Creator Plugin

This skill and the generic `skill-creator:skill-creator` plugin are complementary:

| Concern | Handled by |
|---------|-----------|
| **Repo conventions** (skill pattern, cross-references, orchestrator) | `skill-creator-local` (this skill) |
| **Convention verification** (programmatic checks) | `skill-creator-local/scripts/verify_skill.py` |
| **Skill writing best practices** (progressive disclosure, writing style) | `skill-creator-local` (this skill) |
| **Eval testing** (run test prompts, grade outputs) | `skill-creator:skill-creator` plugin |
| **Description optimization** (trigger accuracy, iterative improvement) | `skill-creator:skill-creator` plugin |
| **Benchmarking** (quantitative pass rates, timing, token usage) | `skill-creator:skill-creator` plugin |

**Typical workflow:**
1. Use `skill-creator-local` to draft the skill
2. Run `verify_skill.py` to check convention compliance
3. Use `skill-creator:skill-creator` to test with eval prompts and optimize the description
4. Run `verify_skill.py` again after any changes from step 3

---

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/verify_skill.py` | Programmatic convention compliance checker | `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py <skill-name>` or `--all` |

The verification script checks:
- Skill structure (frontmatter, required sections, one-line summary, workflow delegation line, escalation template wording)
- Workflow structure (heading ends with "Workflow", `## Context`/`## Boundaries`/`## Decisions` present, Input/Output fields, steps, format rules)
- Sub-agent structure (heading contains "Sub-Agent", `**Input:**`/`**Output:**` fields, `## Input Contract`/`## Output Contract`, no Decision blocks, word count)
- Cross-file reference integrity (logical resource names, escalation/stop alignment, escalation template markers)
- Orchestrator alignment (stop conditions match workflow decisions)
- Word count (>3,000 words warns about decomposition need)

Run it after creating or modifying any skill. Fix all critical and moderate issues before considering the work done.

## Reference Files

- `references/conventions.md` — Detailed convention definitions for pipeline skills
- `.claude/skills/product-discovery/SKILL.md` — Orchestrator (update when adding stages)
- `docs/product-taxonomy/categories.md` — Canonical taxonomy (read-only for all skills except product-taxonomy)
