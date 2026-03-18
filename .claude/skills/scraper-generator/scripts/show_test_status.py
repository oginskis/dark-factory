# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Print human-readable status from test_reports.json (array of all iterations).

Usage:
    uv run show_test_status.py docs/scraper-generator/harlowbros/output/test_reports.json

Supports both:
- Array format (new): [{report1}, {report2}, ...]
- Single object format (old): {report}
"""
from __future__ import annotations

import json
import sys
from pathlib import Path


def format_report(report: dict, index: int | None = None) -> str:
    lines = []
    mode = report.get("mode", "?")
    status = report.get("status", "?")
    ts = report.get("timestamp", "?")

    # Header
    prefix = f"[{index}] " if index is not None else ""
    lines.append(f"{prefix}=== {mode.upper()} mode — {status.upper()} === ({ts})")
    lines.append("")

    # Rule results
    rules = report.get("rule_results", [])
    if rules:
        failed = [r for r in rules if r.get("status") == "fail"]
        warned = [r for r in rules if r.get("status") == "warn"]
        passed = [r for r in rules if r.get("status") == "pass"]
        skipped = [r for r in rules if r.get("status") == "skip"]

        if failed:
            lines.append("  FAILED:")
            for r in failed:
                detail = r.get("detail") or f"value={r.get('value')} threshold={r.get('threshold')}"
                lines.append(f"    {r['id']}: {detail}")
        if warned:
            lines.append("  WARNINGS:")
            for r in warned:
                detail = r.get("detail") or f"value={r.get('value')}"
                lines.append(f"    {r['id']}: {detail}")
        if passed:
            lines.append(f"  PASSED: {', '.join(r['id'] for r in passed)}")
        if skipped:
            lines.append(f"  SKIPPED: {', '.join(r['id'] for r in skipped)}")
        lines.append("")

    # Issues
    issues = report.get("issues", [])
    if issues:
        lines.append("  ISSUES:")
        for issue in issues:
            lines.append(f"    [{issue.get('rule_id')}] {issue.get('detail', '')[:120]}")
            attrs = issue.get("affected_attributes", [])
            if attrs:
                lines.append(f"      Attributes: {', '.join(attrs)}")
            vals = issue.get("sample_values", {})
            if vals:
                for attr, examples in list(vals.items())[:2]:
                    lines.append(f"      {attr}: {examples[:3]}")
        lines.append("")

    # Fix results (retest mode)
    fix_results = report.get("fix_results", {})
    if fix_results:
        lines.append("  FIX RESULTS:")
        for rule_id, result in fix_results.items():
            lines.append(f"    {rule_id}: {result.get('status', '?').upper()} — {result.get('detail', '')[:100]}")
        lines.append("")

    # Regression results (retest mode)
    reg = report.get("regression_results", {})
    if reg:
        reg_status = reg.get("status", "?").upper()
        lines.append(f"  REGRESSIONS: {reg_status} ({reg.get('products_compared', 0)} compared)")
        regs = reg.get("regressions", [])
        if regs:
            for r in regs[:5]:
                lines.append(f"    {r.get('field')}: {r.get('baseline_value')} -> {r.get('retest_value')} ({r.get('url', '')[:50]})")
        lines.append("")

    # New issues (retest mode)
    new_issues = report.get("new_issues", [])
    if new_issues:
        lines.append("  NEW ISSUES:")
        for ni in new_issues:
            lines.append(f"    [{ni.get('rule_id')}] {ni.get('detail', '')[:120]}")
        lines.append("")

    # Passing categories
    passing = report.get("passing_categories", [])
    if passing:
        lines.append(f"  PASSING CATEGORIES: {len(passing)}")

    return "\n".join(lines)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: show_test_status.py <test_reports.json>", file=sys.stderr)
        sys.exit(1)

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"No test report at {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text(encoding="utf-8"))

    if isinstance(data, list):
        print(f"=== {len(data)} iterations ===\n")
        for i, report in enumerate(data, 1):
            print(format_report(report, index=i))
            print("---")
    else:
        print(format_report(data))


if __name__ == "__main__":
    main()
