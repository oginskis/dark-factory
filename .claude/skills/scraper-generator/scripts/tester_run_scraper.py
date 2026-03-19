# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Scraper execution harness. Runs a scraper, captures output, manages versioned files.

Agent: tester sub-agent (references/tester.md)
No validation logic — just execution + file management + traces.
Accumulates summary across multiple scraper invocations within a step
so that errors_count reflects the total across all category runs.

The orchestrator computes all versioned output paths (products_{n}_{hash}.jsonl,
summary_{n}_{hash}.json, debug_{n}_{hash}.log) and passes them through the tester
to this script. The scraper receives them as --output-file, --summary-file, --log-file.

Usage:
    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step probe --probe-urls "https://acme.com/p1,https://acme.com/p2" --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step categories --categories "/shop/tools,/shop/wood" --limit-per-cat 10 \
        --output-file output/products_1_a3f2.jsonl \
        --summary-file output/summary_1_a3f2.json \
        --log-file output/debug_1_a3f2.log \
        --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step depth \
        --output-file output/products_1_a3f2.jsonl \
        --summary-file output/summary_1_a3f2.json \
        --log-file output/debug_1_a3f2.log \
        --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step save-baseline \
        --output-file output/products_1_a3f2.jsonl \
        --iteration 1

Exit codes: 0 = success, 1 = missing required args, 2 = scraper not found
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


def trace(phase: str, **kwargs) -> None:
    """Emit a structured JSON trace line to stdout."""
    entry = {"phase": phase, "timestamp": datetime.now(timezone.utc).isoformat(), **kwargs}
    print(json.dumps(entry), flush=True)


def _read_summary(summary_file: Path) -> dict:
    """Read summary JSON file. Returns empty dict if missing or malformed."""
    if summary_file and summary_file.exists():
        try:
            return json.loads(summary_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _merge_summaries(accumulated: dict, run_summary: dict) -> dict:
    """Merge a single-run summary into an accumulated summary.

    Each scraper invocation writes its own summary via teardown().
    This function accumulates totals across multiple invocations so that
    tester_evaluate_structural.py sees the combined result (especially errors_count).
    """
    if not accumulated:
        return run_summary
    if not run_summary:
        return accumulated
    return {
        "total_products": accumulated.get("total_products", 0) + run_summary.get("total_products", 0),
        "batches_written": accumulated.get("batches_written", 0) + run_summary.get("batches_written", 0),
        "duration_seconds": round(
            accumulated.get("duration_seconds", 0) + run_summary.get("duration_seconds", 0), 1
        ),
        "errors_count": accumulated.get("errors_count", 0) + run_summary.get("errors_count", 0),
        "limited": accumulated.get("limited", False) or run_summary.get("limited", False),
        "timestamp": max(accumulated.get("timestamp", ""), run_summary.get("timestamp", "")),
    }


def _clear_summary(summary_file: Path) -> None:
    """Remove summary file so we can detect whether the scraper wrote a new one."""
    if summary_file and summary_file.exists():
        summary_file.unlink()


def _write_summary(summary_file: Path, summary: dict) -> None:
    """Write accumulated summary to the versioned summary file."""
    summary_file.parent.mkdir(parents=True, exist_ok=True)
    summary_file.write_text(json.dumps(summary, indent=2))


def run_scraper(
    scraper_path: Path,
    args: list[str],
    log_file: Path | None,
    timeout: int,
) -> tuple[int, str, float]:
    """Run scraper subprocess. Captures stderr and appends to log_file if non-empty.

    Returns (exit_code, stdout, duration_s). Exit code -1 means timeout.
    """
    cmd = ["uv", "run", str(scraper_path)] + args
    start = time.monotonic()
    try:
        result = subprocess.run(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            timeout=timeout, text=True,
        )
        duration = time.monotonic() - start
        if result.stderr and log_file:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            with open(log_file, "a") as f:
                f.write(result.stderr)
        return result.returncode, result.stdout, duration
    except subprocess.TimeoutExpired:
        duration = time.monotonic() - start
        return -1, "", duration


def step_probe(scraper_path: Path, urls: list[str], log_file: Path | None) -> None:
    """Run --probe for each URL. Traces each result.

    --probe is exclusive with all other scraper flags (per coder.md),
    so no --output-file/--summary-file/--log-file is passed to the scraper.
    Stderr is captured by run_scraper and appended to log_file.
    """
    for url in urls:
        code, stdout, duration = run_scraper(scraper_path, ["--probe", url], log_file, timeout=30)
        if code == 0 and stdout.strip():
            try:
                product = json.loads(stdout.strip())
                trace("probe", url=url, status="ok", exit_code=code,
                      duration_s=round(duration, 1), fields=list(product.keys()))
            except json.JSONDecodeError:
                trace("probe", url=url, status="parse_error", exit_code=code,
                      stdout_snippet=stdout[:200])
        elif code == -1:
            trace("probe", url=url, status="timeout", exit_code=-1, duration_s=round(duration, 1))
        else:
            trace("probe", url=url, status="error", exit_code=code,
                  duration_s=round(duration, 1))


def step_categories(
    scraper_path: Path,
    categories: list[str],
    limit_per: int,
    output_file: Path,
    summary_file: Path,
    log_file: Path | None,
    *,
    append: bool = False,
) -> None:
    """Run scraper per category with versioned output paths.

    First category uses --append only if append=True.
    Subsequent categories always use --append so outputs accumulate.

    Accumulates summary across all category runs so that errors_count
    reflects the total across all categories, not just the last one.
    """
    accumulated = _read_summary(summary_file) if append else {}
    timeout_per = max(60, limit_per * 6)
    for i, cat in enumerate(categories):
        scraper_args = [
            "--categories", cat,
            "--limit", str(limit_per),
            "--output-file", str(output_file),
            "--summary-file", str(summary_file),
        ]
        if log_file:
            scraper_args += ["--log-file", str(log_file)]
        if i > 0 or append:
            scraper_args.append("--append")
        _clear_summary(summary_file)
        code, _, duration = run_scraper(scraper_path, scraper_args, log_file, timeout_per)
        run_summary = _read_summary(summary_file)
        if run_summary:
            accumulated = _merge_summaries(accumulated, run_summary)
        status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
        trace("category", category=cat, status=status, exit_code=code,
              duration_s=round(duration, 1))
    if accumulated:
        _write_summary(summary_file, accumulated)


def step_depth(
    scraper_path: Path,
    output_file: Path,
    summary_file: Path,
    log_file: Path | None,
) -> None:
    """Run scraper with --limit 100 --append using versioned output paths.

    Merges this run's summary with the existing accumulated summary from prior steps.
    """
    accumulated = _read_summary(summary_file)
    _clear_summary(summary_file)
    scraper_args = [
        "--limit", "100", "--append",
        "--output-file", str(output_file),
        "--summary-file", str(summary_file),
    ]
    if log_file:
        scraper_args += ["--log-file", str(log_file)]
    code, _, duration = run_scraper(scraper_path, scraper_args, log_file, timeout=600)
    run_summary = _read_summary(summary_file)
    if run_summary:
        accumulated = _merge_summaries(accumulated, run_summary)
    if accumulated:
        _write_summary(summary_file, accumulated)
    status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
    trace("depth_check", status=status, exit_code=code, duration_s=round(duration, 1))


def step_save_baseline(output_file: Path) -> None:
    """Copy versioned products file to baseline_products.jsonl in the same directory."""
    baseline = output_file.parent / "baseline_products.jsonl"
    if output_file.exists():
        shutil.copy2(output_file, baseline)
        trace("save_baseline", status="ok", source=str(output_file.name),
              size_bytes=output_file.stat().st_size)
    else:
        trace("save_baseline", status="error",
              detail=f"{output_file.name} does not exist")


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper execution harness")
    parser.add_argument("--scraper", required=True, help="Path to scraper.py")
    parser.add_argument("--step", required=True,
                        choices=["probe", "categories", "depth", "save-baseline"])
    parser.add_argument("--iteration", required=True, type=int)
    parser.add_argument("--probe-urls", help="Comma-separated product URLs (probe step)")
    parser.add_argument("--categories", help="Comma-separated category URL prefixes (categories step)")
    parser.add_argument("--limit-per-cat", type=int, default=10, help="Product limit per category")
    parser.add_argument("--append", action="store_true",
                        help="Append to existing products file (categories step)")
    parser.add_argument("--output-file",
                        help="Versioned products JSONL path (categories, depth, save-baseline steps)")
    parser.add_argument("--summary-file",
                        help="Versioned summary JSON path (categories, depth steps)")
    parser.add_argument("--log-file",
                        help="Versioned debug log path (probe, categories, depth steps)")
    args = parser.parse_args()

    scraper_path = Path(args.scraper)
    if not scraper_path.exists():
        print(f"Error: scraper not found at {scraper_path}", file=sys.stderr)
        sys.exit(2)

    output_file = Path(args.output_file) if args.output_file else None
    summary_file = Path(args.summary_file) if args.summary_file else None
    log_file = Path(args.log_file) if args.log_file else None

    if args.step == "probe":
        if not args.probe_urls:
            print("Error: --probe-urls required for probe step", file=sys.stderr)
            sys.exit(1)
        urls = [u.strip() for u in args.probe_urls.split(",") if u.strip()]
        step_probe(scraper_path, urls, log_file)

    elif args.step == "categories":
        if not args.categories:
            print("Error: --categories required for categories step", file=sys.stderr)
            sys.exit(1)
        if not output_file or not summary_file:
            print("Error: --output-file and --summary-file required for categories step",
                  file=sys.stderr)
            sys.exit(1)
        cats = [c.strip() for c in args.categories.split(",") if c.strip()]
        step_categories(scraper_path, cats, args.limit_per_cat,
                        output_file, summary_file, log_file, append=args.append)

    elif args.step == "depth":
        if not output_file or not summary_file:
            print("Error: --output-file and --summary-file required for depth step",
                  file=sys.stderr)
            sys.exit(1)
        step_depth(scraper_path, output_file, summary_file, log_file)

    elif args.step == "save-baseline":
        if not output_file:
            print("Error: --output-file required for save-baseline step", file=sys.stderr)
            sys.exit(1)
        step_save_baseline(output_file)


if __name__ == "__main__":
    main()
