# /// script
# requires-python = ">=3.10"
# ///
"""
Validate that eval_run.py's CHECKS dict matches conditions.md.

Parses the quality checks table and collection strategy from conditions.md,
compares against the hardcoded values in eval_run.py. Exits 0 if consistent,
1 if mismatches found.

Usage:
    uv run .claude/skills/eval-generator/scripts/validate_conditions.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
CONDITIONS_MD = SCRIPT_DIR.parent / "references" / "conditions.md"

# Import CHECKS from eval_run
sys.path.insert(0, str(SCRIPT_DIR))
from eval_run import CHECKS, eval_sample_size


def parse_checks_table(text: str) -> dict[str, dict]:
    """Parse the quality checks markdown table into {name: {weight, threshold}}."""
    checks = {}
    in_table = False
    for line in text.splitlines():
        if "| Check " in line and "| Weight " in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 3:
                name = cols[0].strip("`")
                weight = int(cols[1])
                threshold = float(cols[2])
                checks[name] = {"weight": weight, "threshold": threshold}
        elif in_table and not line.startswith("|"):
            break
    return checks


def parse_collection_strategy(text: str) -> dict:
    """Parse collection strategy numbers from conditions.md."""
    strategy = {}
    for line in text.splitlines():
        if "**Per subcategory:**" in line:
            m = re.search(r"(\d+)%.*minimum (\d+).*maximum (\d+)", line)
            if m:
                strategy["per_sub_percent"] = int(m.group(1))
                strategy["per_sub_min"] = int(m.group(2))
                strategy["per_sub_max"] = int(m.group(3))
        if "**Single-subcategory fallback:**" in line:
            m = re.search(r"(\d+)%.*minimum (\d+).*maximum (\d+)", line)
            if m:
                strategy["fallback_percent"] = int(m.group(1))
                strategy["fallback_min"] = int(m.group(2))
                strategy["fallback_max"] = int(m.group(3))
    return strategy


def validate_checks(doc_checks: dict, code_checks: dict) -> list[str]:
    """Compare documented checks against code. Returns list of errors."""
    errors = []

    doc_names = set(doc_checks.keys())
    code_names = set(code_checks.keys())

    for name in doc_names - code_names:
        errors.append(f"Check '{name}' in conditions.md but NOT in eval_run.py")
    for name in code_names - doc_names:
        errors.append(f"Check '{name}' in eval_run.py but NOT in conditions.md")

    for name in doc_names & code_names:
        dw = doc_checks[name]["weight"]
        cw = code_checks[name]["weight"]
        if dw != cw:
            errors.append(f"'{name}' weight: conditions.md={dw}, eval_run.py={cw}")

        dt = doc_checks[name]["threshold"]
        ct = code_checks[name]["threshold"]
        if abs(dt - ct) > 0.001:
            errors.append(f"'{name}' threshold: conditions.md={dt}, eval_run.py={ct}")

    doc_total = sum(c["weight"] for c in doc_checks.values())
    code_total = sum(c["weight"] for c in code_checks.values())
    if doc_total != 100:
        errors.append(f"conditions.md weights sum to {doc_total}, expected 100")
    if code_total != 100:
        errors.append(f"eval_run.py weights sum to {code_total}, expected 100")

    return errors


def validate_collection(strategy: dict) -> list[str]:
    """Validate collection strategy numbers match eval_sample_size behavior."""
    errors = []

    if not strategy:
        errors.append("Could not parse collection strategy from conditions.md")
        return errors

    # Test: single sub with 500 expected → 20% = 100, capped at 100
    config = {"expected_product_count": 500, "_sub_configs": {}}
    result = eval_sample_size(config)
    expected_total = min(max(
        round(500 * strategy["fallback_percent"] / 100),
        strategy["fallback_min"]
    ), strategy["fallback_max"])
    if result["total"] != expected_total:
        errors.append(
            f"Single-sub sample: eval_sample_size gives {result['total']}, "
            f"conditions.md formula gives {expected_total}"
        )

    # Test: per-sub with 200 expected → 20% = 40, within [10, 100]
    config2 = {
        "expected_product_count": 200,
        "_sub_configs": {"a": {"expected_count": 200}},
    }
    result2 = eval_sample_size(config2)
    expected_per = min(max(
        round(200 * strategy["per_sub_percent"] / 100),
        strategy["per_sub_min"]
    ), strategy["per_sub_max"])
    actual_per = result2["per_subcategory"].get("a", 0)
    if actual_per != expected_per:
        errors.append(
            f"Per-sub sample (200 expected): eval_sample_size gives {actual_per}, "
            f"conditions.md formula gives {expected_per}"
        )

    return errors


def main() -> int:
    if not CONDITIONS_MD.exists():
        print(f"ERROR: {CONDITIONS_MD} not found", file=sys.stderr)
        return 1

    text = CONDITIONS_MD.read_text()
    doc_checks = parse_checks_table(text)
    strategy = parse_collection_strategy(text)

    errors = []
    errors.extend(validate_checks(doc_checks, CHECKS))
    errors.extend(validate_collection(strategy))

    if errors:
        print(f"FAIL — {len(errors)} mismatches between conditions.md and eval_run.py:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK — {len(doc_checks)} checks and collection strategy match between conditions.md and eval_run.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
