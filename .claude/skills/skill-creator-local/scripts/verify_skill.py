#!/usr/bin/env python3
"""
Verify a skill-wrapper + agent pair follows the dark-factory pipeline conventions.

Usage:
    python verify_skill.py <skill-name>
    python verify_skill.py product-classifier
    python verify_skill.py --all

Checks:
  1. Skill wrapper structure (required sections, frontmatter)
  2. Agent file structure (required sections, ordering)
  3. Cross-file reference integrity (logical names, decisions, file locations)
  4. Orchestrator alignment (stop conditions)
  5. Report template compliance (heading, date, sections)
  6. Decision-step references (steps must point to decisions by name)

Exit code 0 = all checks pass, 1 = failures found.
"""

import sys
import re
from pathlib import Path


def find_repo_root():
    """Walk up from script location to find the repo root (directory containing agents/)."""
    path = Path(__file__).resolve().parent
    for _ in range(10):
        if (path / "agents").is_dir() and (path / ".claude" / "skills").is_dir():
            return path
        path = path.parent
    raise RuntimeError("Cannot find repo root (directory with agents/ and .claude/skills/)")


REPO_ROOT = find_repo_root()
SKILLS_DIR = REPO_ROOT / ".claude" / "skills"
AGENTS_DIR = REPO_ROOT / "agents"
ORCHESTRATOR = SKILLS_DIR / "product-discovery" / "SKILL.md"

# Skills that follow the standalone pattern (no agent file, reduced checks)
STANDALONE_SKILLS = {"product-taxonomy", "product-discovery", "skill-creator-local"}


class Issue:
    def __init__(self, severity, check, message):
        self.severity = severity  # "critical", "moderate", "minor"
        self.check = check
        self.message = message

    def __str__(self):
        icon = {"critical": "!!!", "moderate": " ! ", "minor": " . "}[self.severity]
        return f"  [{icon}] {self.check}: {self.message}"


def read_file(path):
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            key, val = line.split(":", 1)
            fm[key.strip()] = val.strip()
    return fm


def extract_h2_sections(content):
    """Extract ## section headings in order."""
    return re.findall(r"^## (.+)$", content, re.MULTILINE)


def extract_decisions(content):
    """Extract Decision: names from agent file."""
    return re.findall(r"^### Decision: (\w+)", content, re.MULTILINE)


def extract_decision_blocks(content):
    """Extract full decision blocks with their escalation behavior."""
    blocks = {}
    pattern = r"### Decision: (\w+)\n\n(.*?)(?=\n### Decision:|\n---|\Z)"
    for match in re.finditer(pattern, content, re.DOTALL):
        name = match.group(1)
        body = match.group(2)
        # Check if "Escalate when:" contains "Never"
        esc_match = re.search(r"\*\*Escalate when:\*\*(.+?)$", body, re.MULTILINE)
        if esc_match:
            escalates = "Never" not in esc_match.group(1)
        else:
            escalates = False  # No "Escalate when" field — treat as non-escalating
        blocks[name] = {"body": body, "escalates": escalates}
    return blocks


def extract_file_locations(content):
    """Extract resource names from File locations table."""
    resources = []
    in_table = False
    for line in content.split("\n"):
        if "| Resource" in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 2:
                resources.append({"name": parts[0], "path": parts[1]})
        elif in_table:
            in_table = False
    return resources


def extract_wiring_examples(content):
    """Extract logical resource name examples from wiring section."""
    examples = []
    wiring_match = re.search(r"## Claude Code wiring\n(.*?)(?=\n## |\Z)", content, re.DOTALL)
    if wiring_match:
        wiring = wiring_match.group(1)
        examples = re.findall(r'"([^"]+)"', wiring)
    return examples


def extract_orchestrator_stops(content, stage_name):
    """Extract stop conditions for a given stage from the orchestrator."""
    pattern = rf"## Stage \d+: .*?{stage_name}.*?\n(.*?)(?=\n## Stage|\n## Pipeline|\Z)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    section = match.group(1)
    stops = re.findall(r"^- (.+)$", section, re.MULTILINE)
    return [s for s in stops if s.strip()]


def is_inside_code_block(content, position):
    """Check if a position in the content is inside a fenced code block."""
    # Count ``` fences before this position
    fences_before = content[:position].count("```")
    # Odd count means we're inside a code block
    return fences_before % 2 == 1


def extract_logical_refs_from_agent(content):
    """Extract logical resource name references from agent file.

    Looks for patterns like:
    - "Read the company report"
    - "from the product taxonomy categories file"
    - "in the company reports directory"
    - "write the catalog assessment report"
    """
    patterns = [
        r'(?:Read|Write|Check|read|write|check|from|in|into)\s+the\s+([a-z][a-z ]+(?:file|report|directory|assessment|schema))',
        r'(?:Read|Write|Check|read|write|check|from|in|into)\s+the\s+(company report)',
        r'the\s+(product taxonomy categories file)',
        r'the\s+(catalog assessment(?:\s+report)?)',
        r'the\s+(company reports? directory)',
    ]
    refs = set()
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            if not is_inside_code_block(content, match.start()):
                refs.add(match.group(1).strip())
    return list(refs)


# ── Check functions ──────────────────────────────────────────────────────────


def check_standalone_skill(skill_name, content, issues):
    """Check standalone skill structure (no agent file, single-file pattern)."""
    check = "standalone-structure"

    # Frontmatter
    fm = extract_frontmatter(content)
    if "name" not in fm:
        issues.append(Issue("critical", check, "Missing 'name' in frontmatter"))
    elif fm["name"] != skill_name:
        issues.append(Issue("moderate", check, f"Frontmatter name '{fm['name']}' != directory name '{skill_name}'"))
    if "description" not in fm and "description:" not in content[:500]:
        issues.append(Issue("critical", check, "Missing 'description' in frontmatter"))
    if "user-invocable" not in fm:
        issues.append(Issue("moderate", check, "Missing 'user-invocable: true' in frontmatter"))

    # Input section (expected for all skills)
    sections = extract_h2_sections(content)
    if not any("input" in s.lower() for s in sections):
        issues.append(Issue("moderate", check, "Missing ## Input section"))


def check_skill_wrapper(skill_name, content, issues):
    """Check skill wrapper structure."""
    check = "wrapper-structure"

    # Frontmatter
    fm = extract_frontmatter(content)
    if "name" not in fm:
        issues.append(Issue("critical", check, "Missing 'name' in frontmatter"))
    elif fm["name"] != skill_name:
        issues.append(Issue("moderate", check, f"Frontmatter name '{fm['name']}' != directory name '{skill_name}'"))
    if "description" not in fm and "description:" not in content[:500]:
        issues.append(Issue("critical", check, "Missing 'description' in frontmatter"))
    if "user-invocable" not in fm:
        issues.append(Issue("moderate", check, "Missing 'user-invocable: true' in frontmatter"))

    # Required sections
    sections = extract_h2_sections(content)
    required = ["Input", "File locations", "Claude Code wiring", "Notes"]
    for req in required:
        if not any(req.lower() in s.lower() for s in sections):
            issues.append(Issue("critical", check, f"Missing required section: ## {req}"))

    # Agent reference
    if f"agents/{skill_name}.md" not in content:
        issues.append(Issue("critical", check, f"Missing agent reference: agents/{skill_name}.md"))

    # Notes line
    if "File-driven skill" not in content:
        issues.append(Issue("minor", check, "Notes section missing standard 'File-driven skill' line"))

    # Description content checks
    desc_match = re.search(r"description:\s*>\s*\n((?:\s+.+\n)+)", content)
    if desc_match:
        desc = desc_match.group(1)
        if "/product-discovery" not in desc and "pipeline" not in desc.lower():
            issues.append(Issue("moderate", check, "Description should mention pipeline redirect or independence"))


def check_agent_file(skill_name, content, issues):
    """Check agent file structure."""
    check = "agent-structure"

    # Header
    if not re.search(r"^# .+ Agent$", content, re.MULTILINE):
        issues.append(Issue("moderate", check, "Missing '# {Name} Agent' heading"))
    if "**Input:**" not in content:
        issues.append(Issue("moderate", check, "Missing **Input:** field"))
    if "**Output:**" not in content:
        issues.append(Issue("moderate", check, "Missing **Output:** field"))

    # Steps
    steps = re.findall(r"^## Step (\d+):", content, re.MULTILINE)
    if not steps:
        issues.append(Issue("critical", check, "No numbered steps found"))
    elif len(steps) < 2:
        issues.append(Issue("moderate", check, f"Only {len(steps)} step(s) found — expected at least 2"))

    # Step numbering is sequential
    for i, step_num in enumerate(steps):
        if int(step_num) != i + 1:
            issues.append(Issue("moderate", check, f"Step numbering gap: expected Step {i+1}, found Step {step_num}"))
            break

    # Self-verification
    if "Self-Verification" not in content and "Self-verification" not in content:
        issues.append(Issue("moderate", check, "Missing Self-Verification step"))

    # Strict format rules
    if "Strict format rules" not in content and "format rules" not in content.lower():
        issues.append(Issue("moderate", check, "Missing Strict format rules table"))

    # Decisions section
    decisions = extract_decisions(content)
    if not decisions:
        issues.append(Issue("moderate", check, "No Decision: blocks found"))

    # Decision block format
    for dec in decisions:
        dec_pattern = rf"### Decision: {dec}\n\n.*?\*\*Context:\*\*"
        if not re.search(dec_pattern, content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Context:** field"))
        if not re.search(rf"### Decision: {dec}.*?\*\*Autonomous resolution:\*\*", content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Autonomous resolution:** field"))
        if not re.search(rf"### Decision: {dec}.*?\*\*Escalate when:\*\*", content, re.DOTALL):
            issues.append(Issue("moderate", check, f"Decision '{dec}' missing **Escalate when:** field"))

    # Decision-step references: every decision should be referenced by name in a step
    for dec in decisions:
        # Look for the decision name referenced outside the Decisions section
        decisions_section_start = content.find("## Decisions")
        if decisions_section_start == -1:
            decisions_section_start = len(content)
        steps_content = content[:decisions_section_start]
        if f"`{dec}`" not in steps_content and dec not in steps_content.split("## Decisions")[0]:
            issues.append(Issue("moderate", check, f"Decision '{dec}' is defined but never referenced in any step"))

    # Environment agnosticism
    tool_names = ["WebSearch", "WebFetch", "Read tool", "Edit tool", "Bash tool"]
    for tool in tool_names:
        if tool in content:
            issues.append(Issue("critical", check, f"Agent references specific tool name '{tool}' — must be harness-agnostic"))

    # Hardcoded paths — check outside code blocks
    path_pattern = r"(?:docs/|\.claude/)[a-z-]+/[a-z-]+"
    for match in re.finditer(path_pattern, content):
        if not is_inside_code_block(content, match.start()):
            # Also allow paths in table cells (report templates use tables)
            line_start = content.rfind("\n", 0, match.start()) + 1
            line = content[line_start:content.find("\n", match.end())]
            if not line.strip().startswith("|"):
                issues.append(Issue("critical", check, f"Agent contains hardcoded path: '{match.group()}' — use logical resource names"))
                break  # Report only first occurrence

    # Taxonomy reference consistency
    if "taxonomy file" in content.lower() and "product taxonomy categories file" not in content:
        issues.append(Issue("moderate", check, "Uses shortened 'taxonomy file' — should use full name 'product taxonomy categories file'"))


def check_cross_references(skill_name, skill_content, agent_content, issues):
    """Check cross-file reference integrity."""
    check = "cross-references"

    # Extract data from both files
    file_locations = extract_file_locations(skill_content)
    wiring_examples = extract_wiring_examples(skill_content)
    decision_blocks = extract_decision_blocks(agent_content)

    # Check: every agent logical resource name should appear in wiring examples
    logical_refs = extract_logical_refs_from_agent(agent_content)
    for ref in logical_refs:
        ref_lower = ref.lower().strip()
        # Normalize: strip leading adjectives like "full" and trailing qualifiers like "for an existing report"
        ref_core = re.sub(r'^(full|the)\s+', '', ref_lower)
        ref_core = re.sub(r'\s+(for|from|in|to|of)\s+.*$', '', ref_core)
        # Check if any wiring example contains the core reference
        matched = False
        for ex in wiring_examples:
            ex_lower = ex.lower()
            if ref_core in ex_lower or ex_lower in ref_core or ref_lower in ex_lower or ex_lower in ref_lower:
                matched = True
                break
        if not matched:
            issues.append(Issue("moderate", check, f"Agent references '{ref}' but it's not in wrapper wiring examples"))

    # Check: every decision should be reflected in wrapper wiring
    escalating = [name for name, block in decision_blocks.items() if block["escalates"]]
    non_escalating = [name for name, block in decision_blocks.items() if not block["escalates"]]

    # Escalating decisions should be listed in wiring
    for dec in escalating:
        if dec not in skill_content:
            issues.append(Issue("critical", check, f"Escalating decision '{dec}' not mentioned in wrapper wiring"))

    # Non-escalating decisions should be covered by stop behavior description
    if non_escalating:
        # Check for explicit stop/autonomous language in the wiring section
        wiring_match = re.search(r"## Claude Code wiring\n(.*?)(?=\n## |\Z)", skill_content, re.DOTALL)
        wiring_text = wiring_match.group(1) if wiring_match else ""
        has_stop_description = any(phrase in wiring_text.lower() for phrase in [
            "does not escalate",
            "autonomous stop",
            "stop autonomously",
            "stops autonomously",
            "writes a minimal",
            "no report",
            "graceful degradation",
            "handled autonomously",
            "without escalation",
        ])
        if not has_stop_description:
            issues.append(Issue("moderate", check,
                f"Agent has autonomous stops ({', '.join(non_escalating)}) but wrapper wiring doesn't describe stop behavior"))

    # Check: file locations cover agent's read/write needs
    if not file_locations:
        issues.append(Issue("critical", check, "Wrapper has no File locations table"))


def check_orchestrator_alignment(skill_name, agent_content, orchestrator_content, issues):
    """Check that orchestrator stop conditions match agent decisions."""
    check = "orchestrator-alignment"

    if not orchestrator_content:
        issues.append(Issue("minor", check, "Cannot read orchestrator file"))
        return

    # Map skill names to stage names in orchestrator
    stage_map = {
        "product-classifier": "Product Classifier",
        "catalog-detector": "Catalog Detector",
        "scraper-generator": "Scraper Generator",
        "eval-generator": "Eval Generator",
    }

    stage_name = stage_map.get(skill_name)
    if not stage_name:
        return  # Not a pipeline stage

    # Check the stage exists in orchestrator
    if stage_name not in orchestrator_content:
        issues.append(Issue("critical", check, f"Stage '{stage_name}' not found in orchestrator"))
        return

    # Extract stop conditions
    stops = extract_orchestrator_stops(orchestrator_content, stage_name)
    decisions = extract_decisions(agent_content)

    if not stops and decisions:
        issues.append(Issue("critical", check, f"Orchestrator has no stop conditions for '{stage_name}' but agent has {len(decisions)} decisions"))


def check_report_template(agent_content, issues):
    """Check report template compliance."""
    check = "report-template"

    # Check for H1 heading in template — only inside code blocks
    templates = re.findall(r"```markdown\n(.*?)```", agent_content, re.DOTALL)
    if not templates:
        templates = re.findall(r"```\n(.*?)```", agent_content, re.DOTALL)

    for template in templates:
        if "# " in template and "**Slug:**" in template:
            # This looks like a report template
            if not re.search(r"^# .+: \{", template, re.MULTILINE):
                issues.append(Issue("moderate", check, "Report template heading should be '# {Type}: {Company Name}'"))
            if "date" not in template.lower():
                issues.append(Issue("moderate", check, "Report template missing date field"))


# ── Main ─────────────────────────────────────────────────────────────────────


def verify_skill(skill_name):
    """Run all checks for a skill/agent pair."""
    issues = []

    skill_path = SKILLS_DIR / skill_name / "SKILL.md"
    agent_path = AGENTS_DIR / f"{skill_name}.md"
    orchestrator_content = read_file(ORCHESTRATOR)

    skill_content = read_file(skill_path)

    if not skill_content:
        issues.append(Issue("critical", "file-exists", f"Skill file not found: {skill_path}"))
        return issues

    # Standalone skills get reduced checks (no agent file, no wrapper+agent conventions)
    if skill_name in STANDALONE_SKILLS:
        check_standalone_skill(skill_name, skill_content, issues)
        return issues

    agent_content = read_file(agent_path)
    if not agent_content:
        issues.append(Issue("critical", "file-exists", f"Agent file not found: {agent_path}"))
        # Still check skill wrapper
        check_skill_wrapper(skill_name, skill_content, issues)
        return issues

    check_skill_wrapper(skill_name, skill_content, issues)
    check_agent_file(skill_name, agent_content, issues)
    check_cross_references(skill_name, skill_content, agent_content, issues)
    check_orchestrator_alignment(skill_name, agent_content, orchestrator_content, issues)
    check_report_template(agent_content, issues)

    return issues


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <skill-name> | --all")
        sys.exit(1)

    if sys.argv[1] == "--all":
        skill_names = [
            d.name for d in SKILLS_DIR.iterdir()
            if d.is_dir() and (d / "SKILL.md").exists()
        ]
    else:
        skill_names = [sys.argv[1]]

    total_issues = 0
    for skill_name in sorted(skill_names):
        issues = verify_skill(skill_name)
        critical = [i for i in issues if i.severity == "critical"]
        moderate = [i for i in issues if i.severity == "moderate"]
        minor = [i for i in issues if i.severity == "minor"]

        status = "PASS" if not critical and not moderate else "FAIL" if critical else "WARN"
        icon = {"PASS": "+", "FAIL": "x", "WARN": "~"}[status]

        print(f"\n[{icon}] {skill_name} — {status} ({len(critical)} critical, {len(moderate)} moderate, {len(minor)} minor)")

        for issue in critical + moderate + minor:
            print(issue)

        total_issues += len(critical) + len(moderate)

    print(f"\n{'='*60}")
    print(f"Total: {len(skill_names)} skills checked, {total_issues} issues found")
    sys.exit(1 if total_issues > 0 else 0)


if __name__ == "__main__":
    main()
