# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest"]
# ///
"""Unit tests for derive_slug.py slug derivation from company URLs."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from derive_slug import MULTI_PART_TLDS, SUBDOMAIN_PREFIXES, derive_slug


# ---------------------------------------------------------------------------
# Core slug derivation — real company URLs
# ---------------------------------------------------------------------------


class TestDeriveSlugRealURLs:
    """Test with real company URLs from the pipeline."""

    def test_harlowbros_co_uk(self):
        result = derive_slug("https://www.harlowbros.co.uk")
        assert result["slug"] == "harlowbros"
        assert result["hostname"] == "harlowbros.co.uk"

    def test_iwood_lv(self):
        result = derive_slug("https://shop.iwood.lv")
        assert result["slug"] == "iwood"
        assert result["hostname"] == "iwood.lv"

    def test_simple_com_domain(self):
        result = derive_slug("https://www.example.com")
        assert result["slug"] == "example"
        assert result["hostname"] == "example.com"


# ---------------------------------------------------------------------------
# Multi-part TLDs
# ---------------------------------------------------------------------------


class TestMultiPartTLDs:
    """Ensure multi-part TLDs (.co.uk, .com.au, etc.) are correctly stripped."""

    def test_co_uk(self):
        result = derive_slug("https://www.timber-merchants.co.uk")
        assert result["slug"] == "timber-merchants"

    def test_com_au(self):
        result = derive_slug("https://www.bushtools.com.au")
        assert result["slug"] == "bushtools"

    def test_co_jp(self):
        result = derive_slug("https://www.sakura-tools.co.jp")
        assert result["slug"] == "sakura-tools"

    def test_co_nz(self):
        result = derive_slug("https://www.kiwilumber.co.nz")
        assert result["slug"] == "kiwilumber"

    def test_com_br(self):
        result = derive_slug("https://www.madeira.com.br")
        assert result["slug"] == "madeira"

    def test_org_uk(self):
        result = derive_slug("https://www.woodfoundation.org.uk")
        assert result["slug"] == "woodfoundation"

    def test_net_au(self):
        result = derive_slug("https://www.timberstock.net.au")
        assert result["slug"] == "timberstock"


# ---------------------------------------------------------------------------
# Subdomain prefix stripping
# ---------------------------------------------------------------------------


class TestSubdomainPrefixes:
    """Verify all known subdomain prefixes are stripped."""

    def test_www_prefix(self):
        result = derive_slug("https://www.example.com")
        assert result["slug"] == "example"

    def test_shop_prefix(self):
        result = derive_slug("https://shop.example.com")
        assert result["slug"] == "example"

    def test_store_prefix(self):
        result = derive_slug("https://store.example.com")
        assert result["slug"] == "example"

    def test_boutique_prefix(self):
        result = derive_slug("https://boutique.example.com")
        assert result["slug"] == "example"

    def test_webshop_prefix(self):
        result = derive_slug("https://webshop.example.com")
        assert result["slug"] == "example"

    def test_estore_prefix(self):
        result = derive_slug("https://estore.example.com")
        assert result["slug"] == "example"

    def test_unknown_subdomain_kept(self):
        """Non-standard subdomains should be kept as part of the slug."""
        result = derive_slug("https://catalog.example.com")
        assert result["slug"] == "catalog.example"
        assert result["hostname"] == "catalog.example.com"

    def test_subdomain_with_multi_part_tld(self):
        result = derive_slug("https://shop.timber.co.uk")
        assert result["slug"] == "timber"
        assert result["hostname"] == "timber.co.uk"


# ---------------------------------------------------------------------------
# Edge cases — URL formats
# ---------------------------------------------------------------------------


class TestEdgeCases:
    """Edge cases: trailing slashes, deep paths, bare hostnames, etc."""

    def test_trailing_slash(self):
        result = derive_slug("https://www.example.com/")
        assert result["slug"] == "example"

    def test_deep_path(self):
        result = derive_slug("https://www.example.com/shop/products/timber")
        assert result["slug"] == "example"

    def test_with_query_string(self):
        result = derive_slug("https://www.example.com/products?page=1")
        assert result["slug"] == "example"

    def test_with_fragment(self):
        result = derive_slug("https://www.example.com/page#section")
        assert result["slug"] == "example"

    def test_bare_hostname_no_scheme(self):
        """Bare hostname (no https://) should be auto-prefixed."""
        result = derive_slug("example.com")
        assert result["slug"] == "example"
        assert result["hostname"] == "example.com"

    def test_bare_hostname_with_www(self):
        result = derive_slug("www.example.com")
        assert result["slug"] == "example"

    def test_http_scheme(self):
        result = derive_slug("http://www.example.com")
        assert result["slug"] == "example"

    def test_uppercase_url(self):
        """Hostnames should be lowercased."""
        result = derive_slug("https://WWW.EXAMPLE.COM")
        assert result["slug"] == "example"

    def test_trailing_dot_in_hostname(self):
        """Trailing dot (FQDN notation) should be stripped."""
        result = derive_slug("https://www.example.com.")
        assert result["slug"] == "example"

    def test_hyphenated_domain(self):
        """Hyphens in domain names should be preserved."""
        result = derive_slug("https://www.my-timber-shop.com")
        assert result["slug"] == "my-timber-shop"

    def test_single_segment_hostname(self):
        """Edge case: a single label (e.g., localhost)."""
        result = derive_slug("localhost")
        assert result["slug"] == "localhost"

    def test_two_segment_no_prefix(self):
        """Two segment domain without any known prefix."""
        result = derive_slug("example.com")
        assert result["slug"] == "example"
        assert result["hostname"] == "example.com"


# ---------------------------------------------------------------------------
# Return structure
# ---------------------------------------------------------------------------


class TestReturnStructure:
    """Verify the return dict has the expected keys."""

    def test_keys_present(self):
        result = derive_slug("https://www.example.com")
        assert "slug" in result
        assert "hostname" in result
        assert len(result) == 2

    def test_hostname_is_registrable_domain(self):
        """Hostname should be the registrable domain (subdomain stripped)."""
        result = derive_slug("https://www.harlowbros.co.uk")
        assert result["hostname"] == "harlowbros.co.uk"


# ---------------------------------------------------------------------------
# Constants completeness
# ---------------------------------------------------------------------------


class TestConstants:
    """Verify the module constants are properly defined."""

    def test_multi_part_tlds_is_set(self):
        assert isinstance(MULTI_PART_TLDS, set)
        assert "co.uk" in MULTI_PART_TLDS
        assert "com.au" in MULTI_PART_TLDS

    def test_subdomain_prefixes_is_set(self):
        assert isinstance(SUBDOMAIN_PREFIXES, set)
        assert "www" in SUBDOMAIN_PREFIXES
        assert "shop" in SUBDOMAIN_PREFIXES
        assert "store" in SUBDOMAIN_PREFIXES


# ---------------------------------------------------------------------------
# CLI entrypoint (main)
# ---------------------------------------------------------------------------


class TestMainCLI:
    """Test the command-line interface via subprocess."""

    def test_cli_success(self):
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "derive_slug.py"
        )
        result = subprocess.run(
            [sys.executable, script, "--url", "https://www.harlowbros.co.uk"],
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0
        data = json.loads(result.stdout)
        assert data["slug"] == "harlowbros"
        assert data["hostname"] == "harlowbros.co.uk"

    def test_cli_missing_url(self):
        script = str(
            Path(__file__).resolve().parents[1] / "scripts" / "derive_slug.py"
        )
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True,
            text=True,
        )
        assert result.returncode != 0


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
