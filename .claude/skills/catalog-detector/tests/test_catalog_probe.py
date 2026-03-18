# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Tests for catalog_probe.py — orchestrator (parse_args, run_script)."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from catalog_probe import parse_args, run_script, RECIPE_RANK


# ---------------------------------------------------------------------------
# RECIPE_RANK
# ---------------------------------------------------------------------------


class TestRecipeRank:
    def test_rank_ordering(self):
        assert RECIPE_RANK["full"] > RECIPE_RANK["partial"]
        assert RECIPE_RANK["partial"] > RECIPE_RANK["poor"]
        assert RECIPE_RANK["poor"] > RECIPE_RANK["untested"]

    def test_all_keys_present(self):
        assert set(RECIPE_RANK.keys()) == {"full", "partial", "poor", "untested"}


# ---------------------------------------------------------------------------
# parse_args
# ---------------------------------------------------------------------------


class TestParseArgs:
    def test_required_args(self):
        with patch("sys.argv", ["catalog_probe.py",
                                 "--url", "https://example.com",
                                 "--slug", "test-co",
                                 "--knowledgebase-dir", "/tmp/kb",
                                 "--output-dir", "/tmp/out"]):
            args = parse_args()
            assert args.url == "https://example.com"
            assert args.slug == "test-co"
            assert args.knowledgebase_dir == Path("/tmp/kb")
            assert args.output_dir == Path("/tmp/out")

    def test_missing_required_arg(self):
        with patch("sys.argv", ["catalog_probe.py", "--url", "https://example.com"]):
            with pytest.raises(SystemExit):
                parse_args()


# ---------------------------------------------------------------------------
# run_script
# ---------------------------------------------------------------------------


class TestRunScript:
    @patch("catalog_probe.subprocess.run")
    def test_successful_script(self, mock_run, tmp_path):
        result_data = {"url": "https://example.com", "status": 200}
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout=json.dumps(result_data),
            stderr="some log output",
        )
        log_parts = []

        result = run_script("probe_access.py", ["--url", "https://example.com"],
                            tmp_path, log_parts)

        assert result is not None
        assert result["url"] == "https://example.com"
        assert result["status"] == 200
        # Check that JSON was saved
        assert (tmp_path / "probe_access.json").exists()
        saved = json.loads((tmp_path / "probe_access.json").read_text())
        assert saved["url"] == "https://example.com"
        # Check log collection
        assert "some log output" in log_parts

    @patch("catalog_probe.subprocess.run")
    def test_script_crash_exit_code_2(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(
            returncode=2,
            stdout="",
            stderr="crash",
        )
        log_parts = []

        result = run_script("probe_access.py", ["--url", "https://example.com"],
                            tmp_path, log_parts)

        assert result is None
        assert "crash" in log_parts

    @patch("catalog_probe.subprocess.run")
    def test_script_invalid_json(self, mock_run, tmp_path):
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout="not valid json",
            stderr="",
        )
        log_parts = []

        result = run_script("probe_access.py", ["--url", "https://example.com"],
                            tmp_path, log_parts)

        assert result is None

    @patch("catalog_probe.subprocess.run")
    def test_partial_result_exit_code_1(self, mock_run, tmp_path):
        result_data = {"url": "https://example.com", "errors": [{"error": "something"}]}
        mock_run.return_value = MagicMock(
            returncode=1,
            stdout=json.dumps(result_data),
            stderr="warning",
        )
        log_parts = []

        result = run_script("probe_access.py", ["--url", "https://example.com"],
                            tmp_path, log_parts)

        # Exit code 1 is partial, not crash — should still parse
        assert result is not None
        assert result["url"] == "https://example.com"

    @patch("catalog_probe.subprocess.run")
    def test_output_file_naming(self, mock_run, tmp_path):
        """JSON output file should match script name with .json extension."""
        result_data = {"test": True}
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout=json.dumps(result_data),
            stderr="",
        )
        log_parts = []

        run_script("probe_platform.py", ["--url", "https://example.com"],
                   tmp_path, log_parts)

        assert (tmp_path / "probe_platform.json").exists()

    @patch("catalog_probe.subprocess.run")
    def test_run_script_uses_uv(self, mock_run, tmp_path):
        """Verify the script is invoked via uv run."""
        mock_run.return_value = MagicMock(
            returncode=0,
            stdout='{"ok": true}',
            stderr="",
        )
        log_parts = []

        run_script("probe_access.py", ["--url", "https://example.com"],
                   tmp_path, log_parts)

        call_args = mock_run.call_args
        cmd = call_args[0][0]
        assert cmd[0] == "uv"
        assert cmd[1] == "run"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
