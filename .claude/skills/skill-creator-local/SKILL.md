---
name: skill-creator-local
description: >
  Create or improve pipeline skills and their harness-agnostic agent files in this repository.
  Enforces the established skill-wrapper + agent-file conventions, proper cross-file references,
  and report template structures used throughout the product discovery pipeline.
  Use this skill when creating a new pipeline stage, improving an existing skill or agent,
  or reviewing skill/agent files for convention compliance —
  "create a new skill for X", "add a pipeline stage", "review skill conventions",
  "improve the scraper-generator agent", "make sure this skill follows our patterns",
  "check convention compliance", "verify cross-references", "audit skill structure".
  Do NOT use for the generic skill-creator plugin — this is specific to the dark-factory repo conventions.
user-invocable: true
---

# Skill Creator (Local)

Create and improve pipeline skills and their corresponding harness-agnostic agent files, following the conventions established in this repository.

This skill codifies the patterns distilled from `product-discovery`, `product-classifier`, and `catalog-detector` — the most mature skill/agent pairs in the pipeline. All new or revised skills must follow these conventions for consistency.

## Input

`$ARGUMENTS` describes what to create or improve (e.g., "create a new skill for X", "review catalog-detector agent", "improve scraper-generator conventions").

## When to use this skill

- Creating a new pipeline stage (skill + agent pair)
- Improving or reviewing an existing skill or agent for convention compliance
- Adding new decisions, stop conditions, or report sections to an existing agent
- Verifying cross-file references between skills, agents, and the orchestrator

## Architecture: Two Skill Patterns

### Pipeline stages: Two-File Pattern (wrapper + agent)

Most pipeline stages consist of two files:

```
.claude/skills/{name}/SKILL.md    ← Harness-specific wrapper (Claude Code adapter)
agents/{name}.md                  ← Harness-agnostic reasoning (shared logic)
```

The **skill wrapper** adapts the agent for Claude Code: provides file paths, maps logical resource names, specifies which tools to use, and describes escalation/stop behavior.

The **agent file** contains all reasoning, decision logic, and report templates. It is environment-agnostic — it works in Claude Code today and in an autonomous K8s service tomorrow.

The **product-discovery orchestrator** (`.claude/skills/product-discovery/SKILL.md`) chains all stages. When adding a new stage, update the orchestrator too.

### Standalone skills: Single-File Pattern

Some skills don't need the two-file split — they're Claude Code-only and have no autonomous service counterpart. Examples: `product-taxonomy` (all logic inline in SKILL.md with `references/`), `skill-creator-local` (this skill). Use the standalone pattern when:
- The skill is a meta-tool (creates/reviews other skills) rather than a pipeline stage
- The skill has no foreseeable need to run outside Claude Code
- The reasoning is simple enough to fit in SKILL.md without an agent file

Standalone skills still follow the general best practices (progressive disclosure, description triggering, writing style) but skip Conventions 1-3 and 5 since those are specific to the wrapper+agent pattern.

---

## Skill Writing Best Practices

These are general skill-writing principles (from the Anthropic skill-creator) that apply to all skills in this repo — both wrapper skills and standalone skills like `product-taxonomy`.

### Progressive Disclosure

Skills load in three tiers. Design with this in mind:
1. **Metadata** (name + description) — always in context (~100 words). This is the primary triggering mechanism.
2. **SKILL.md body** — loaded when skill triggers. Keep under 500 lines. If approaching this limit, move detail into `references/` files with clear pointers.
3. **Bundled resources** — loaded on demand (unlimited size). Use `scripts/` for executable code, `references/` for docs, `assets/` for templates.

```
skill-name/
├── SKILL.md              # Required — under 500 lines
├── scripts/              # Deterministic/repetitive tasks
├── references/           # Docs loaded into context as needed
└── assets/               # Templates, icons, fonts
```

### Description — Prevent Undertriggering

The `description` field in frontmatter is how Claude decides whether to invoke a skill. Be specific AND slightly "pushy" — include trigger phrases, contexts, and near-miss redirects. Claude tends to undertrigger, so err on the side of being explicit about when to use the skill.

Good: includes "what it does", "what it produces", trigger phrases in quotes, prerequisites, and pipeline redirects.
Bad: a single vague sentence like "Handles catalog detection."

### Writing Style

- **Explain the why** behind instructions rather than piling on rigid MUSTs. LLMs respond better to reasoning than to rules. If you find yourself writing ALWAYS or NEVER in all caps, reframe as an explanation of why the thing matters.
- **Use imperative form** — "Read the company report" not "You should read the company report."
- **Prefer examples over abstract rules** — a Correct/Wrong table communicates faster than a paragraph of constraints.
- **Keep it lean** — remove instructions that aren't pulling their weight. If test runs show the model wasting time on something, cut the instruction causing it.

### Output Format Definition

When a skill produces structured output, define the exact template:

```markdown
## Report structure
Use this exact template:
# [Title]
## Executive summary
## Key findings
## Recommendations
```

Include Correct/Wrong tables for formatting rules — they're the most effective way to prevent common mistakes.

### Domain Organization

When a skill supports multiple variants, organize by domain with a reference file per variant:

```
skill-name/
├── SKILL.md (workflow + selection logic)
└── references/
    ├── variant-a.md
    ├── variant-b.md
    └── variant-c.md
```

Claude reads only the relevant reference file, keeping context lean.

---

## Change Routing: What Goes Where

When the user asks to modify a skill, determine which file(s) to change. This is the most important judgment call — putting harness-specific detail in the agent file or reasoning logic in the wrapper breaks the architecture.

### Changes that go in the AGENT file only

These are about *what* the agent thinks and decides — pure reasoning, independent of environment:

| Change type | Example |
|-------------|---------|
| Add/change decision logic | "Stop if the site is a heavy SPA" |
| Add/change report sections or template | "Add a Findings section to the report" |
| Add/modify self-verification gates | "Check that classification values are verbatim" |
| Add/modify strict format rules | "Prices must not have currency symbols" |
| Change investigation steps | "Also check robots.txt" |
| Add/modify escalation decisions | "Escalate when no taxonomy match is found" |
| Change classification rules | "Allow at most one secondary category" |
| Add/modify boundaries | "This agent does not generate scrapers" |

**Abstraction level for agent files:** Write as if the agent has no idea what harness runs it. Say "search the web for" not "use WebSearch tool." Say "read the company report" not "read `docs/product-classifier/festool.md`." Say "escalate" not "ask the user." The agent describes *what to do and decide*, never *how to interact or which tools to call*.

### Changes that go in the SKILL WRAPPER only

These are about *how* Claude Code runs the agent — environment wiring:

| Change type | Example |
|-------------|---------|
| Change file paths | "Reports should go in `docs/reports/` instead" |
| Add/remove tools | "Use Playwright for this stage" |
| Change escalation behavior description | "This agent now has autonomous stops" |
| Update logical resource name mapping | "Map 'the catalog assessment' to the new path" |
| Change input format | "Input is now a URL, not a slug" |

### Changes that go in BOTH files

These require coordinated edits — change the agent's reasoning AND update the wrapper's wiring:

| Change type | Agent file change | Wrapper change |
|-------------|-------------------|----------------|
| **New stop condition** | Add `Decision:` block + reference in step | Add to wiring stop behavior description |
| **New escalation point** | Add `Decision:` block with "Escalate when" | Add decision name to wiring escalation list |
| **New input/output file** | Reference new logical resource name in steps | Add row to File locations table + wiring example |
| **Remove a decision** | Remove `Decision:` block + step references | Remove from wiring escalation/stop list |

After any BOTH-files change, also update the **orchestrator** (`.claude/skills/product-discovery/SKILL.md`) if the change affects pipeline stop conditions.

---

## Convention 1: Skill Wrapper Structure

Every wrapper skill follows this exact structure. No variations.

```markdown
---
name: {skill-name}
description: >
  {What it does — first sentence.}
  {What it produces — second sentence.}
  {When to use — trigger phrases and contexts.}
  {Prerequisites — what must exist first.}
  {Pipeline redirect — when to use /product-discovery instead, or note if independent.}
user-invocable: true
---

# {Skill Title}

Read and follow the agent instructions in `agents/{name}.md`.

## Input

`$ARGUMENTS` is {description of expected input} (e.g., `{example}`).

## File locations

| Resource | Path |
|----------|------|
| {Upstream input} | `docs/{upstream-stage}/{slug}.md` |
| {Other inputs} | `docs/...` |
| {Output} | `docs/{this-stage}/{slug}.md` |

## Claude Code wiring

- {Escalation handling — list escalation point names with numbered user options per decision, or state "does not escalate". See escalation presentation format below.}
- {Autonomous stop behavior — describe what happens on stops}
- {Tools to use — web search, web fetch, Playwright, etc.}
- Provide the file paths from the table above when the agent references logical resources (e.g., "{logical name 1}", "{logical name 2}").

## Notes

File-driven skill — no database or external services required.
```

### Wrapper rules

| Rule | Why |
|------|-----|
| **Description includes trigger phrases** | Prevents undertriggering — Claude needs explicit cues |
| **Description mentions prerequisites** | Prevents invocation before upstream stages complete |
| **Description mentions pipeline redirect** | Prevents confusion between individual stages and full pipeline |
| **File locations table is exhaustive** | Every file the agent reads or writes must have a row |
| **Wiring lists all escalation points with user options** | User must know what actions they can take when the agent escalates |
| **Wiring explicitly describes stop behavior** | Harness needs to know the agent may terminate without output |
| **Wiring examples match agent's logical resource names exactly** | Prevents mapping errors between wrapper and agent |
| **Notes line is identical across all wrappers** | Consistency signal |

### Escalation presentation format

When an agent escalates, the harness presents the decision to the user in a standard format. The **orchestrator** defines the format template (see `product-discovery/SKILL.md`). Each wrapper defines the specific **user options** per escalation decision.

Every escalation presentation must include:
1. **Decision name** — which decision was triggered
2. **Stage** — which pipeline stage hit the issue
3. **Context** — what was encountered (from the decision's Context field)
4. **Payload** — the specific evidence or candidates the agent gathered
5. **Numbered options** — clear actions the user can take to resolve or stop

The wrapper's wiring section lists each escalation decision with its numbered options. Example:

```
- `ambiguous_company` — 1) Pick a candidate by name or number, 2) Provide additional context, 3) Stop
- `category_not_found` — 1) Suggest a new subcategory, 2) Pick the closest existing category, 3) Stop
```

Every escalation must include a "Stop" option so the user can always halt the pipeline cleanly.

---

## Convention 2: Agent File Structure

Every agent file follows this structure. The sections are in order — do not rearrange.

```markdown
# {Agent Name} Agent

**Input:** {what the agent receives}
**Output:** {what it produces, or "escalation"}

---

## Purpose

{What this agent does, its role in the pipeline, and how it interacts. Use "## Purpose" for agents that act autonomously (product-classifier), or "## Context" for agents that need upstream data first (catalog-detector). Pick one — do not use both.}

---

## Step 1: {First Action}
{Instructions}
{Decision references: "stop — see the `{decision_name}` decision" or "escalate — see the `{decision_name}` decision"}

---

## Step 2: {Second Action}
{...}

---

## Step N: Write {Output Name}
{Report template(s) — success and stop variants if applicable}

### Strict format rules
{Correct/Wrong table}

---

## Step N+1: Self-Verification
{Quality gates table}

---

## {Optional: Investigation Guidance}
{Tips for exploring sites, catalogs, etc.}

---

## {Optional: Boundaries}
{What this agent does NOT do}

---

## Decisions
{All decision blocks, each following the escalation pattern}
```

### Agent rules

| Rule | Why |
|------|-----|
| **Three rules of environment agnosticism** | Agents must work in Claude Code AND autonomous K8s service |
| — Decisions, not interactions | Say "escalate" not "ask the user" |
| — Capabilities, not tools | Say "search the web" not "use WebSearch tool" |
| — Logical file references, not paths | Say "the company report" not `docs/product-classifier/festool.md` |
| **Every step that can stop or escalate must reference the decision by name** | Prevents orphaned decisions that nothing points to |
| **Report templates include both success and stop variants** | Stop cases must produce a minimal report, not leave gaps |
| **Strict format rules table after each report template** | Correct/Wrong columns prevent common formatting errors |
| **Self-verification step with numbered quality gates** | Agent must check its own output before completing |
| **Decisions section is always last** | Consistent location for the harness to find decision definitions |

### Escalation pattern (every decision block)

```markdown
### Decision: {snake_case_name}

**Context:** {what situation triggers this decision}
**Autonomous resolution:** {rule for auto-deciding, or "Never" if always escalate}
**Escalate when:** {conditions, or "Never" if autonomous stop}
**Escalation payload:** {what info to pass, or "N/A" if never escalates}
```

---

## Convention 3: Cross-File Reference Integrity

These rules prevent the most common bugs — broken references between wrapper, agent, and orchestrator.

### Logical resource name mapping

Every logical resource name used in the agent must appear in the wrapper's wiring examples, and must map to a row in the File locations table.

**Check:** grep the agent file for phrases like "the company report", "the product taxonomy categories file", "write the catalog assessment". Each must appear as an example in the wrapper's wiring bullet.

### Escalation/stop alignment

1. Every `Decision:` block in the agent must be either:
   - Listed as an escalation point in the wrapper's wiring (if it escalates), or
   - Covered by the wrapper's stop behavior description (if autonomous stop)
2. Every escalation point listed in the wrapper must exist as a `Decision:` block in the agent
3. Every stop condition must appear in the orchestrator's `**Stop the pipeline if:**` list for that stage

### Taxonomy references

When an agent references the product taxonomy, it must use the full logical name "the product taxonomy categories file" — not shortened forms like "the taxonomy file" or "the categories file." This prevents ambiguity with SKU schema files under `docs/product-taxonomy/sku-schemas/`.

---

## Convention 4: Report Templates

### Header fields

Every report starts with an `#` heading and metadata fields:

```markdown
# {Report Type}: {Company Name}

**Slug:** {slug}
**{Date field}:** {today's date}
```

The date field name varies by report type: `Discovery date` for company reports, `Assessment date` for catalog assessments. But every report has one.

### Success and stop template variants

Agents that can stop (autonomous stop decisions) need two report templates:
- **Success template** — full section list for the happy path
- **Stop template** — minimal report with `**Scraping strategy:** none`, `**Stop reason:** {decision_name}`, and a `## Findings` section explaining why

Both templates share the same heading format and slug/date fields.

### Section headings

Use `##` for all top-level sections within the report. The agent's template defines the canonical section list — no extras, none missing, none renamed.

### Classification values

Primary and Secondary classification values must be verbatim `Category > Subcategory` pairs from the product taxonomy categories file. Joined with ` > ` (space, greater-than, space). One primary (required), at most one secondary (optional, or "None").

---

## Convention 5: Orchestrator Integration

When adding or modifying a pipeline stage, update `.claude/skills/product-discovery/SKILL.md`:

1. Add/update the `## Stage N:` section with:
   - "Read file locations from `.claude/skills/{name}/SKILL.md`, then read and follow `agents/{name}.md` in full."
   - One-line description of what the stage does
   - `**Stop the pipeline if:**` list matching ALL stop/escalation conditions from the agent
2. Update the escalation instruction at the top if the new agent's escalation behavior differs
3. Update `## Pipeline Summary` if the new stage produces additional output files

---

## Relationship to the Skill-Creator Plugin

This skill and the generic `skill-creator:skill-creator` plugin are complementary — they handle different parts of the skill lifecycle:

| Concern | Handled by |
|---------|-----------|
| **Repo conventions** (wrapper+agent pattern, cross-references, orchestrator) | `skill-creator-local` (this skill) |
| **Convention verification** (programmatic checks) | `skill-creator-local/scripts/verify_skill.py` |
| **Skill writing best practices** (progressive disclosure, writing style) | `skill-creator-local` (this skill, see above) |
| **Eval testing** (run test prompts, grade outputs, compare with/without skill) | `skill-creator:skill-creator` plugin |
| **Description optimization** (trigger accuracy, train/test split, iterative improvement) | `skill-creator:skill-creator` plugin |
| **Benchmarking** (quantitative pass rates, timing, token usage) | `skill-creator:skill-creator` plugin |

**When to delegate to the plugin:** After the skill/agent pair passes convention verification, use `/skill-creator:skill-creator` to test it with real prompts and optimize the description for triggering accuracy. The plugin handles the eval loop (spawn test runs, grade, review, iterate) which this skill does not duplicate.

**Typical workflow:**
1. Use `skill-creator-local` to draft the skill/agent pair
2. Run `verify_skill.py` to check convention compliance
3. Use `skill-creator:skill-creator` to test with eval prompts and optimize the description
4. Run `verify_skill.py` again after any changes from step 3

---

## Workflow: Creating a New Pipeline Stage

1. **Draft the agent file** at `agents/{name}.md` following Convention 2
2. **Draft the skill wrapper** at `.claude/skills/{name}/SKILL.md` following Convention 1
3. **Verify cross-references** per Convention 3:
   - Every logical resource name in agent → mapped in wrapper
   - Every decision in agent → reflected in wrapper wiring
   - Every stop condition → reflected in orchestrator
4. **Update the orchestrator** per Convention 5
5. **Run verification:** `uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py <skill-name>`
6. **Test and optimize:** Use `/skill-creator:skill-creator` to run eval prompts and optimize the description
7. **Self-review checklist:**

| # | Check |
|---|-------|
| 1 | Agent file uses no tool names, no file paths, no user-facing language |
| 2 | Every step that can stop/escalate references the decision by name |
| 3 | Report template has success + stop variants (if applicable) |
| 4 | Strict format rules table present |
| 5 | Self-verification quality gates present |
| 6 | Wrapper's File locations table covers every file the agent reads or writes |
| 7 | Wrapper's wiring examples match agent's logical resource names exactly |
| 8 | Wrapper describes both escalation points and autonomous stops |
| 9 | Orchestrator's stop list matches agent's decisions |
| 10 | Logical resource names are unambiguous (full names, not short forms) |

## Workflow: Reviewing an Existing Skill/Agent Pair

1. **Run the verification script first** — it catches structural issues programmatically:
   ```bash
   uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py <skill-name>
   uv run python .claude/skills/skill-creator-local/scripts/verify_skill.py --all
   ```
2. Read both the skill wrapper and agent file for issues the script can't catch (clarity, flow, ambiguity)
3. Check cross-reference integrity (Convention 3)
4. Check report template compliance (Convention 4)
5. Check orchestrator alignment (Convention 5)
6. Report findings organized by severity: Critical > Moderate > Minor
7. Fix issues with the user's approval

## Scripts

| Script | Purpose | Usage |
|--------|---------|-------|
| `scripts/verify_skill.py` | Programmatic convention compliance checker | `uv run python scripts/verify_skill.py <skill-name>` or `--all` |

The verification script checks:
- Skill wrapper structure (frontmatter, required sections, agent reference)
- Agent file structure (heading, steps, decisions, self-verification, format rules)
- Cross-file reference integrity (logical resource names, escalation/stop alignment)
- Orchestrator alignment (stop conditions match agent decisions)
- Report template compliance (heading format, date field)
- Environment agnosticism (no tool names, no hardcoded paths in agent files)

Run it after creating or modifying any skill/agent pair. Fix all critical and moderate issues before considering the work done.

## Reference Files

- `.claude/skills/product-discovery/SKILL.md` — Orchestrator (update when adding stages)
- `docs/product-taxonomy/categories.md` — Canonical taxonomy (read-only for all skills except product-taxonomy)
