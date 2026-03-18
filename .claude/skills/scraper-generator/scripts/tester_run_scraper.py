# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Scraper execution harness. Runs a scraper, captures output, manages iteration files.

Agent: tester sub-agent (references/tester.md)
No validation logic — just execution + file management + traces.
Accumulates summary.json across multiple scraper invocations within a step
so that errors_count reflects the total across all category runs.

Usage:
    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step probe --probe-urls "https://acme.com/p1,https://acme.com/p2" --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step categories --categories "/shop/tools,/shop/wood" --limit-per-cat 10 --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step depth --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step save-baseline --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step save-iteration --iteration 1
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


def _read_summary(output_dir: Path) -> dict:
    """Read summary.json from output dir. Returns empty dict if missing or malformed."""
    sp = output_dir / "summary.json"
    if sp.exists():
        try:
            return json.loads(sp.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            pass
    return {}


def _merge_summaries(accumulated: dict, run_summary: dict) -> dict:
    """Merge a single-run summary into an accumulated summary.

    Each scraper invocation writes its own summary.json via teardown().
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


def _clear_summary(output_dir: Path) -> None:
    """Remove summary.json so we can detect whether the scraper wrote a new one."""
    sp = output_dir / "summary.json"
    if sp.exists():
        sp.unlink()


def _write_summary(output_dir: Path, summary: dict) -> None:
    """Write accumulated summary to output dir."""
    output_dir.mkdir(parents=True, exist_ok=True)
    sp = output_dir / "summary.json"
    sp.write_text(json.dumps(summary, indent=2))


def run_scraper(
    scraper_path: Path,
    args: list[str],
    debug_log: Path,
    timeout: int,
) -> tuple[int, str, float]:
    """Run scraper, append stderr to debug_log. Returns (exit_code, stdout, duration_s)."""
    cmd = ["uv", "run", str(scraper_path)] + args
    start = time.monotonic()
    try:
        with open(debug_log, "a") as f:
            result = subprocess.run(
                cmd, stdout=subprocess.PIPE, stderr=f,
                timeout=timeout, text=True,
            )
        duration = time.monotonic() - start
        return result.returncode, result.stdout, duration
    except subprocess.TimeoutExpired:
        duration = time.monotonic() - start
        return -1, "", duration


def step_probe(scraper_path: Path, urls: list[str], debug_log: Path) -> None:
    """Run --probe for each URL. Traces each result."""
    for url in urls:
        code, stdout, duration = run_scraper(scraper_path, ["--probe", url], debug_log, timeout=30)
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
    debug_log: Path,
    *,
    append: bool = False,
) -> None:
    """Run scraper per category. First category uses --append only if append=True.
    Subsequent categories always use --append so outputs accumulate.

    Accumulates summary.json across all category runs so that errors_count
    reflects the total across all categories, not just the last one."""
    output_dir = scraper_path.parent / "output"
    accumulated = _read_summary(output_dir) if append else {}
    timeout_per = max(60, limit_per * 6)
    for i, cat in enumerate(categories):
        args = ["--categories", cat, "--limit", str(limit_per)]
        if i > 0 or append:
            args.append("--append")
        _clear_summary(output_dir)
        code, _, duration = run_scraper(scraper_path, args, debug_log, timeout_per)
        run_summary = _read_summary(output_dir)
        if run_summary:
            accumulated = _merge_summaries(accumulated, run_summary)
        status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
        trace("category", category=cat, status=status, exit_code=code,
              duration_s=round(duration, 1))
    if accumulated:
        _write_summary(output_dir, accumulated)


def step_depth(scraper_path: Path, debug_log: Path) -> None:
    """Run scraper with --limit 100 --append, no categories. Appends to preserve Step 2 output.

    Merges this run's summary with the existing accumulated summary from prior steps."""
    output_dir = scraper_path.parent / "output"
    accumulated = _read_summary(output_dir)
    _clear_summary(output_dir)
    code, _, duration = run_scraper(scraper_path, ["--limit", "100", "--append"], debug_log, timeout=600)
    run_summary = _read_summary(output_dir)
    if run_summary:
        accumulated = _merge_summaries(accumulated, run_summary)
    if accumulated:
        _write_summary(output_dir, accumulated)
    status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
    trace("depth_check", status=status, exit_code=code, duration_s=round(duration, 1))


def step_save_baseline(output_dir: Path) -> None:
    """Copy products.jsonl to baseline_products.jsonl."""
    src = output_dir / "products.jsonl"
    dst = output_dir / "baseline_products.jsonl"
    if src.exists():
        shutil.copy2(src, dst)
        trace("save_baseline", status="ok", size_bytes=src.stat().st_size)
    else:
        trace("save_baseline", status="error", detail="products.jsonl does not exist")


def step_save_iteration(output_dir: Path, iteration: int) -> None:
    """Copy products.jsonl and debug log to iteration-specific files."""
    products = output_dir / "products.jsonl"
    debug = output_dir / f"debug_iteration_{iteration}.log"

    if products.exists():
        shutil.copy2(products, output_dir / f"products_iteration_{iteration}.jsonl")
        trace("save_iteration", file="products", iteration=iteration,
              size_bytes=products.stat().st_size)

    if debug.exists():
        shutil.copy2(debug, output_dir / "debug.log")
        trace("save_iteration", file="debug", iteration=iteration,
              size_bytes=debug.stat().st_size)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper execution harness")
    parser.add_argument("--scraper", required=True, help="Path to scraper.py")
    parser.add_argument("--step", required=True,
                        choices=["probe", "categories", "depth", "save-baseline", "save-iteration"])
    parser.add_argument("--iteration", required=True, type=int)
    parser.add_argument("--probe-urls", help="Comma-separated product URLs (probe step)")
    parser.add_argument("--categories", help="Comma-separated category URL prefixes (categories step)")
    parser.add_argument("--limit-per-cat", type=int, default=10, help="Product limit per category")
    parser.add_argument("--append", action="store_true", help="Append to existing products.jsonl (categories step)")
    args = parser.parse_args()

    scraper_path = Path(args.scraper)
    if not scraper_path.exists():
        print(f"Error: scraper not found at {scraper_path}", file=sys.stderr)
        sys.exit(2)
    output_dir = scraper_path.parent / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    debug_log = output_dir / f"debug_iteration_{args.iteration}.log"

    if args.step == "probe":
        if not args.probe_urls:
            print("Error: --probe-urls required for probe step", file=sys.stderr)
            sys.exit(1)
        urls = [u.strip() for u in args.probe_urls.split(",") if u.strip()]
        step_probe(scraper_path, urls, debug_log)

    elif args.step == "categories":
        if not args.categories:
            print("Error: --categories required for categories step", file=sys.stderr)
            sys.exit(1)
        cats = [c.strip() for c in args.categories.split(",") if c.strip()]
        step_categories(scraper_path, cats, args.limit_per_cat, debug_log, append=args.append)

    elif args.step == "depth":
        step_depth(scraper_path, debug_log)

    elif args.step == "save-baseline":
        step_save_baseline(output_dir)

    elif args.step == "save-iteration":
        step_save_iteration(output_dir, args.iteration)


if __name__ == "__main__":
    main()
