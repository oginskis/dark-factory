# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Orchestrator: coordinate the four probe scripts, assemble combined JSON, save per-slug output.

This script contains NO analysis logic — only coordination, file I/O, and JSON assembly.
It runs probe_access, probe_platform, probe_discovery, and probe_recipe as subprocesses,
saves each result to {output-dir}/, and assembles them into a flat JSON dict on stdout.

ARGUMENTS:
    --url                Target website URL (required)
    --slug               Company slug (required)
    --knowledgebase-dir  Path to platform knowledgebase directory (required)
    --output-dir         Output directory for per-slug results (required)

EXIT CODES:
    0 = full result (all scripts ran successfully)
    1 = partial result (some scripts had errors; errors[] explains gaps)
    2 = script crash
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


RECIPE_RANK = {"full": 3, "partial": 2, "poor": 1, "untested": 0}


def run_script(script_name: str, args: list[str], output_dir: Path,
               log_parts: list[str]) -> dict | None:
    """Run a sibling probe script, save JSON to output_dir, collect stderr.

    Returns parsed JSON dict or None if the script crashed (exit code 2) or
    produced invalid output.
    """
    script_path = Path(__file__).parent / script_name
    result = subprocess.run(
        ["uv", "run", str(script_path)] + args,
        capture_output=True, text=True,
    )
    log_parts.append(result.stderr)
    if result.returncode == 2:
        return None
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return None
    # Save individual result
    json_name = script_name.replace(".py", ".json")
    (output_dir / json_name).write_text(json.dumps(data, indent=2))
    return data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Orchestrate catalog probe scripts")
    parser.add_argument("--url", required=True, help="Target website URL")
    parser.add_argument("--slug", required=True, help="Company slug")
    parser.add_argument("--knowledgebase-dir", required=True, type=Path,
                        help="Path to platform knowledgebase directory")
    parser.add_argument("--output-dir", required=True, type=Path,
                        help="Output directory for per-slug results")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    log_parts: list[str] = []
    errors: list[dict] = []
    had_partial = False

    assembled: dict = {}

    try:
        # 1. probe_access
        access = run_script("probe_access.py", ["--url", args.url], args.output_dir, log_parts)
        if access is None:
            errors.append({"section": "access", "error": "probe_access crashed"})
            had_partial = True
        else:
            assembled.update({
                "url": access.get("url"),
                "final_url": access.get("final_url"),
                "redirected": access.get("redirected"),
                "cross_domain_redirect": access.get("cross_domain_redirect"),
                "homepage_status": access.get("homepage_status"),
                "transport_health": access.get("transport_health"),
                "anti_bot": access.get("anti_bot"),
            })
            errors.extend(access.get("errors", []))

            # Early exit if blocked
            if access.get("transport_health") == "blocked":
                assembled["errors"] = errors
                print(json.dumps(assembled, indent=2))
                # Save log
                (args.output_dir / "probe.log").write_text("".join(log_parts))
                sys.exit(1)

        # 2. probe_platform
        platform = run_script("probe_platform.py", ["--url", args.url], args.output_dir, log_parts)
        if platform is None:
            errors.append({"section": "platform", "error": "probe_platform crashed"})
            had_partial = True
        else:
            assembled.update({
                "platform_guess": platform.get("platform_guess"),
                "platform_confidence": platform.get("platform_confidence"),
                "platform_signal_count": platform.get("platform_signal_count"),
                "platform_conflict": platform.get("platform_conflict"),
                "platform_version": platform.get("platform_version"),
                "js_rendering_signals": platform.get("js_rendering_signals"),
                "geo_hints": platform.get("geo_hints"),
            })
            errors.extend(platform.get("errors", []))

        # 3. probe_discovery
        discovery = run_script("probe_discovery.py", ["--url", args.url], args.output_dir, log_parts)
        if discovery is None:
            errors.append({"section": "discovery", "error": "probe_discovery crashed"})
            had_partial = True
        else:
            assembled.update({
                "robots_txt": discovery.get("robots_txt"),
                "sitemap": discovery.get("sitemap"),
                "homepage_links": discovery.get("homepage_links"),
                "json_ld_on_homepage": discovery.get("json_ld_on_homepage"),
            })
            errors.extend(discovery.get("errors", []))

        # 4. probe_recipe — conditional on platform + knowledgebase
        sample_urls = []
        if discovery and discovery.get("sitemap", {}).get("sample_product_urls"):
            sample_urls = discovery["sitemap"]["sample_product_urls"]

        platform_guess = (platform or {}).get("platform_guess", "unknown")
        platform_conflict = (platform or {}).get("platform_conflict", False)

        # Determine which platforms to test
        platforms_to_test = []
        if platform_conflict:
            # When conflict, test all candidates that have a knowledgebase
            # The platform script doesn't expose raw candidates, so we check
            # the main guess plus common platforms
            candidates = {platform_guess}
            # Check which knowledgebases exist
            for kb_file in args.knowledgebase_dir.glob("*.md"):
                candidates.add(kb_file.stem)
            platforms_to_test = [p for p in candidates
                                 if (args.knowledgebase_dir / f"{p}.md").exists()]
        elif platform_guess != "unknown":
            kb_file = args.knowledgebase_dir / f"{platform_guess}.md"
            if kb_file.exists():
                platforms_to_test = [platform_guess]

        best_recipe = None
        if platforms_to_test and sample_urls:
            for test_platform in platforms_to_test:
                recipe_args = [
                    "--url", args.url,
                    "--platform", test_platform,
                    "--knowledgebase-dir", str(args.knowledgebase_dir),
                    "--product-urls", ",".join(sample_urls),
                ]
                recipe = run_script("probe_recipe.py", recipe_args, args.output_dir, log_parts)
                if recipe is None:
                    continue
                match = recipe.get("recipe_match", "untested")
                if best_recipe is None or RECIPE_RANK.get(match, 0) > RECIPE_RANK.get(
                        best_recipe.get("recipe_match", "untested"), 0):
                    best_recipe = recipe

        if best_recipe:
            # Re-save the winning recipe (in case conflict produced multiple)
            (args.output_dir / "probe_recipe.json").write_text(
                json.dumps(best_recipe, indent=2))
            assembled["recipe_verification"] = {
                "knowledgebase_file": best_recipe.get("knowledgebase_file"),
                "knowledgebase_found": best_recipe.get("knowledgebase_found"),
                "knowledgebase_selectors_parsed": best_recipe.get("knowledgebase_selectors_parsed"),
                "knowledgebase_api_endpoints_parsed": best_recipe.get("knowledgebase_api_endpoints_parsed"),
                "recipe_match": best_recipe.get("recipe_match"),
                "product_pages_tested": best_recipe.get("product_pages_tested"),
                "checks": best_recipe.get("checks"),
                "pagination_check": best_recipe.get("pagination_check"),
            }
            errors.extend(best_recipe.get("errors", []))
        else:
            assembled["recipe_verification"] = {
                "knowledgebase_file": None,
                "knowledgebase_found": False,
                "knowledgebase_selectors_parsed": 0,
                "knowledgebase_api_endpoints_parsed": 0,
                "recipe_match": "untested",
                "product_pages_tested": 0,
                "checks": [],
                "pagination_check": {"tested": False, "pattern_confirmed": None, "next_page_found": False},
            }

        assembled["errors"] = errors

    except Exception as exc:
        print(json.dumps({"error": str(exc)}, indent=2), file=sys.stderr)
        sys.exit(2)

    # Save merged log
    (args.output_dir / "probe.log").write_text("".join(log_parts))

    print(json.dumps(assembled, indent=2))
    sys.exit(0 if not errors and not had_partial else 1)


if __name__ == "__main__":
    main()
