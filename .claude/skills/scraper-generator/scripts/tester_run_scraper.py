# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Scraper execution harness. Runs a scraper, captures output, manages versioned files.

Agent: tester sub-agent (references/tester.md)
No validation logic — just execution + file management + traces.

Every invocation generates a unique hash and creates its own output files.
Files are NEVER overwritten. The hash is 4 hex chars from os.urandom.

Within step_categories, multiple scraper runs (one per category) share the
invocation's hash and accumulate into a single products file via --append.

Usage:
    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step probe --probe-urls "https://acme.com/p1,https://acme.com/p2" \
        --output-dir docs/scraper-generator/acme/output --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step categories --categories "/shop/tools,/shop/wood" --limit-per-cat 10 \
        --output-dir docs/scraper-generator/acme/output --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step depth \
        --output-dir docs/scraper-generator/acme/output --iteration 1

    uv run tester_run_scraper.py --scraper docs/scraper-generator/acme/scraper.py \
        --step save-baseline \
        --output-dir docs/scraper-generator/acme/output --iteration 1

Exit codes: 0 = success, 1 = missing required args, 2 = scraper not found

The script emits a {"phase": "files", ...} trace with the generated paths
so the tester agent knows where files ended up.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path


def _make_hash() -> str:
    """Generate a unique 4-char hex hash for this invocation."""
    return os.urandom(2).hex()


def trace(phase: str, **kwargs) -> None:
    """Emit a structured JSON trace line to stdout."""
    entry = {"phase": phase, "timestamp": datetime.now(timezone.utc).isoformat(), **kwargs}
    print(json.dumps(entry), flush=True)


def _merge_summaries(accumulated: dict, run_summary: dict) -> dict:
    """Merge a single-run summary into an accumulated summary.

    Used within step_categories to accumulate across per-category scraper runs.
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


def step_probe(scraper_path: Path, urls: list[str], log_file: Path, probe_file: Path) -> None:
    """Run --probe for each URL. Writes results to probe_{n}_{hash}.json.

    --probe is exclusive with all other scraper flags (per coder.md),
    so no --output-file/--summary-file/--log-file is passed to the scraper.
    Stderr is captured by run_scraper and appended to log_file.
    """
    results = []
    for url in urls:
        code, stdout, duration = run_scraper(scraper_path, ["--probe", url], log_file, timeout=30)
        entry: dict = {"url": url, "exit_code": code, "duration_s": round(duration, 1)}
        if code == 0 and stdout.strip():
            try:
                product = json.loads(stdout.strip())
                entry["status"] = "ok"
                entry["fields"] = list(product.keys())
                entry["product"] = product
            except json.JSONDecodeError:
                entry["status"] = "parse_error"
                entry["stdout_snippet"] = stdout[:200]
        elif code == -1:
            entry["status"] = "timeout"
        else:
            entry["status"] = "error"
        results.append(entry)
        trace("probe", **{k: v for k, v in entry.items() if k != "product"})

    # Write probe results to versioned file
    output = {"probes": results, "total": len(results),
              "ok": sum(1 for r in results if r.get("status") == "ok")}
    probe_file.parent.mkdir(parents=True, exist_ok=True)
    probe_file.write_text(json.dumps(output, indent=2))


def step_categories(
    scraper_path: Path,
    categories: list[str],
    limit_per: int,
    output_file: Path,
    summary_file: Path,
    log_file: Path,
) -> None:
    """Run scraper per category. All categories accumulate into this invocation's files.

    First category creates the files, subsequent categories use --append.
    Summary is accumulated across all category runs within this invocation.
    """
    accumulated: dict = {}
    timeout_per = max(60, limit_per * 6)
    # Temp summary path — scraper overwrites this on each teardown, we read and merge
    temp_summary = summary_file.parent / f"_tmp_summary_{os.urandom(2).hex()}.json"
    for i, cat in enumerate(categories):
        scraper_args = [
            "--categories", cat,
            "--limit", str(limit_per),
            "--output-file", str(output_file),
            "--summary-file", str(temp_summary),
            "--log-file", str(log_file),
        ]
        if i > 0:
            scraper_args.append("--append")
        if temp_summary.exists():
            temp_summary.unlink()
        code, _, duration = run_scraper(scraper_path, scraper_args, log_file, timeout_per)
        if temp_summary.exists():
            try:
                run_summary = json.loads(temp_summary.read_text(encoding="utf-8"))
                accumulated = _merge_summaries(accumulated, run_summary)
            except (json.JSONDecodeError, OSError):
                pass
        status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
        trace("category", category=cat, status=status, exit_code=code,
              duration_s=round(duration, 1))
    # Write final accumulated summary to the versioned summary file (never overwrites — unique hash)
    if accumulated:
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        summary_file.write_text(json.dumps(accumulated, indent=2))
    # Clean up temp
    if temp_summary.exists():
        temp_summary.unlink()


def step_depth(
    scraper_path: Path,
    output_file: Path,
    summary_file: Path,
    log_file: Path,
) -> None:
    """Run scraper with --limit 100. Creates its own versioned files (unique hash)."""
    scraper_args = [
        "--limit", "100",
        "--output-file", str(output_file),
        "--summary-file", str(summary_file),
        "--log-file", str(log_file),
    ]
    code, _, duration = run_scraper(scraper_path, scraper_args, log_file, timeout=600)
    status = "ok" if code == 0 else ("timeout" if code == -1 else "error")
    trace("depth_check", status=status, exit_code=code, duration_s=round(duration, 1))


def step_save_baseline(output_dir: Path, iteration: int) -> None:
    """Find all products files for this iteration and concatenate into baseline."""
    baseline = output_dir / "baseline_products.jsonl"
    pattern = f"products_{iteration}_*.jsonl"
    files = sorted(output_dir.glob(pattern))
    if not files:
        trace("save_baseline", status="error", detail=f"No {pattern} files found")
        return
    with open(baseline, "w") as out:
        for f in files:
            out.write(f.read_text())
    total = sum(1 for line in baseline.read_text().splitlines() if line.strip())
    trace("save_baseline", status="ok", files=[f.name for f in files],
          total_products=total, size_bytes=baseline.stat().st_size)


def main() -> None:
    parser = argparse.ArgumentParser(description="Scraper execution harness")
    parser.add_argument("--scraper", required=True, help="Path to scraper.py")
    parser.add_argument("--step", required=True,
                        choices=["probe", "categories", "depth", "save-baseline"])
    parser.add_argument("--iteration", required=True, type=int)
    parser.add_argument("--output-dir", required=True,
                        help="Directory for versioned output files")
    parser.add_argument("--probe-urls", help="Comma-separated product URLs (probe step)")
    parser.add_argument("--categories", help="Comma-separated category URL prefixes")
    parser.add_argument("--limit-per-cat", type=int, default=10, help="Product limit per category")
    args = parser.parse_args()

    scraper_path = Path(args.scraper)
    if not scraper_path.exists():
        print(f"Error: scraper not found at {scraper_path}", file=sys.stderr)
        sys.exit(2)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    n = args.iteration
    h = _make_hash()

    # Compute versioned paths for this invocation
    products_file = output_dir / f"products_{n}_{h}.jsonl"
    summary_file = output_dir / f"summary_{n}_{h}.json"
    log_file = output_dir / f"debug_{n}_{h}.log"

    if args.step == "probe":
        if not args.probe_urls:
            print("Error: --probe-urls required for probe step", file=sys.stderr)
            sys.exit(1)
        urls = [u.strip() for u in args.probe_urls.split(",") if u.strip()]
        probe_file = output_dir / f"probe_{n}_{h}.json"
        trace("files", probe=str(probe_file), debug_log=str(log_file))
        step_probe(scraper_path, urls, log_file, probe_file)

    elif args.step == "categories":
        if not args.categories:
            print("Error: --categories required for categories step", file=sys.stderr)
            sys.exit(1)
        cats = [c.strip() for c in args.categories.split(",") if c.strip()]
        trace("files", products=str(products_file), summary=str(summary_file),
              debug_log=str(log_file))
        step_categories(scraper_path, cats, args.limit_per_cat,
                        products_file, summary_file, log_file)

    elif args.step == "depth":
        trace("files", products=str(products_file), summary=str(summary_file),
              debug_log=str(log_file))
        step_depth(scraper_path, products_file, summary_file, log_file)

    elif args.step == "save-baseline":
        step_save_baseline(output_dir, n)


if __name__ == "__main__":
    main()
