# /// script
# requires-python = ">=3.10"
# dependencies = ["pytest", "httpx", "selectolax"]
# ///
"""Tests for probe_discovery.py — robots.txt parsing, sitemap handling, homepage links."""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import pytest

from _probe_lib import TransportTracker
from probe_discovery import (
    extract_homepage_links,
    guess_url_pattern,
    parse_robots_txt,
    parse_sitemap,
    sample_diverse,
)


# ---------------------------------------------------------------------------
# parse_robots_txt
# ---------------------------------------------------------------------------


class TestParseRobotsTxt:
    def test_full_robots_txt(self, sample_robots_txt):
        result = parse_robots_txt(sample_robots_txt)
        assert len(result["sitemaps"]) == 2
        assert "https://www.example.com/sitemap.xml" in result["sitemaps"]
        assert "https://www.example.com/sitemap-products.xml" in result["sitemaps"]
        assert "/admin/" in result["disallowed_paths"]
        assert "/checkout/" in result["disallowed_paths"]
        assert result["crawl_delay"] == 10

    def test_empty_robots_txt(self):
        result = parse_robots_txt("")
        assert result["sitemaps"] == []
        assert result["disallowed_paths"] == []
        assert result["crawl_delay"] is None

    def test_no_sitemaps(self):
        text = "User-agent: *\nDisallow: /private/\n"
        result = parse_robots_txt(text)
        assert result["sitemaps"] == []
        assert result["disallowed_paths"] == ["/private/"]

    def test_crawl_delay_invalid(self):
        text = "Crawl-delay: abc\n"
        result = parse_robots_txt(text)
        assert result["crawl_delay"] is None

    def test_crawl_delay_valid(self):
        text = "Crawl-delay: 5\n"
        result = parse_robots_txt(text)
        assert result["crawl_delay"] == 5

    def test_empty_disallow(self):
        """Empty Disallow: lines should be ignored."""
        text = "Disallow:\nDisallow: /secret/\n"
        result = parse_robots_txt(text)
        assert result["disallowed_paths"] == ["/secret/"]

    def test_case_insensitive_directives(self):
        text = "SITEMAP: https://example.com/sitemap.xml\nDISALLOW: /blocked/\nCRAWL-DELAY: 3\n"
        result = parse_robots_txt(text)
        assert len(result["sitemaps"]) == 1
        assert result["disallowed_paths"] == ["/blocked/"]
        assert result["crawl_delay"] == 3


# ---------------------------------------------------------------------------
# sample_diverse
# ---------------------------------------------------------------------------


class TestSampleDiverse:
    def test_fewer_than_n(self):
        urls = ["a", "b"]
        assert sample_diverse(urls, 5) == ["a", "b"]

    def test_exact_n(self):
        urls = ["a", "b", "c"]
        assert sample_diverse(urls, 3) == ["a", "b", "c"]

    def test_more_than_n(self):
        urls = list(range(20))
        result = sample_diverse(urls, 5)
        assert len(result) == 5
        # Should pick from diverse positions
        assert result[0] == 0  # beginning
        assert result[-1] == 16  # near end (step=4, index 4*4=16)

    def test_empty_list(self):
        assert sample_diverse([], 5) == []

    def test_sample_one(self):
        urls = list(range(10))
        result = sample_diverse(urls, 1)
        assert len(result) == 1
        assert result[0] == 0


# ---------------------------------------------------------------------------
# extract_homepage_links
# ---------------------------------------------------------------------------


class TestExtractHomepageLinks:
    def test_catalog_links_extracted(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        assert "/products" in result["catalog_links"] or any(
            "product" in l for l in result["catalog_links"]
        )

    def test_catalog_links_from_shop(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        assert any("shop" in l for l in result["catalog_links"])

    def test_catalog_links_from_collection(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        assert any("collection" in l for l in result["catalog_links"])

    def test_javascript_links_ignored(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        for link in result["catalog_links"]:
            assert "javascript:" not in link

    def test_hash_links_ignored(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        for link in result["catalog_links"]:
            assert link != "#"

    def test_nav_categories_extracted(self, homepage_with_links):
        result = extract_homepage_links(homepage_with_links, "https://example.com")
        assert "Products" in result["nav_categories"]
        assert "Tools" in result["nav_categories"]

    def test_empty_page_no_links(self):
        html = "<html><body></body></html>"
        result = extract_homepage_links(html, "https://example.com")
        assert result["catalog_links"] == []
        assert result["nav_categories"] == []

    def test_absolute_url_matching_base(self):
        html = '<html><body><a href="https://example.com/shop/tools">Tools</a></body></html>'
        result = extract_homepage_links(html, "https://example.com")
        assert any("shop" in l for l in result["catalog_links"])

    def test_catalog_links_capped_at_10(self):
        links = "".join(f'<a href="/product/{i}">Product {i}</a>' for i in range(20))
        html = f"<html><body>{links}</body></html>"
        result = extract_homepage_links(html, "https://example.com")
        assert len(result["catalog_links"]) <= 10

    def test_nav_categories_capped_at_20(self):
        nav_links = "".join(f'<a href="/cat/{i}">Category {i}</a>' for i in range(30))
        html = f'<html><body><nav>{nav_links}</nav></body></html>'
        result = extract_homepage_links(html, "https://example.com")
        assert len(result["nav_categories"]) <= 20


# ---------------------------------------------------------------------------
# guess_url_pattern
# ---------------------------------------------------------------------------


class TestGuessUrlPattern:
    def test_html_pattern(self):
        urls = ["https://example.com/widget-a.html", "https://example.com/widget-b.html"]
        assert guess_url_pattern(urls) == "/{path}.html"

    def test_product_slug_pattern(self):
        urls = ["https://example.com/product/abc", "https://example.com/product/def"]
        assert guess_url_pattern(urls) == "/product/{slug}"

    def test_p_id_pattern(self):
        urls = ["https://example.com/p/123-abc", "https://example.com/p/456-def"]
        assert guess_url_pattern(urls) == "/p/{id}-{slug}"

    def test_products_handle_pattern(self):
        urls = ["https://example.com/products/widget", "https://example.com/products/gizmo"]
        assert guess_url_pattern(urls) == "/products/{handle}"

    def test_mixed_urls_no_pattern(self):
        urls = ["https://example.com/a", "https://example.com/b/c.php"]
        assert guess_url_pattern(urls) is None

    def test_empty_list(self):
        assert guess_url_pattern([]) is None


# ---------------------------------------------------------------------------
# parse_sitemap (mocked HTTP)
# ---------------------------------------------------------------------------


class TestParseSitemap:
    def _make_fetch_return(self, text, status=200):
        """Create a tuple matching the fetch return signature."""
        return (text, status, False, {}, None)

    @patch("probe_discovery.fetch")
    def test_simple_sitemap(self, mock_fetch, sample_sitemap_xml):
        mock_fetch.return_value = self._make_fetch_return(sample_sitemap_xml)
        tracker = TransportTracker()
        client = MagicMock()

        urls = parse_sitemap(client, "https://example.com/sitemap.xml",
                             timeout=10, delay=0, max_size=2_000_000, tracker=tracker)

        # Only URLs matching PRODUCT_URL_PATTERNS are returned
        assert len(urls) == 3  # 3 /product/ URLs, /about is excluded
        assert all("/product/" in u for u in urls)

    @patch("probe_discovery.fetch")
    def test_sitemap_index(self, mock_fetch, sample_sitemap_index_xml, sample_sitemap_xml):
        """Test recursive sitemap index parsing."""
        def side_effect(client, url, *, timeout, delay, max_size, tracker):
            if "sitemapindex" in url or url.endswith("sitemap.xml"):
                return self._make_fetch_return(sample_sitemap_index_xml)
            elif "products" in url:
                return self._make_fetch_return(sample_sitemap_xml)
            else:
                # pages sitemap with no product URLs
                return self._make_fetch_return(
                    '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                    '<url><loc>https://example.com/about</loc></url></urlset>'
                )

        mock_fetch.side_effect = side_effect
        tracker = TransportTracker()
        client = MagicMock()

        urls = parse_sitemap(client, "https://example.com/sitemap.xml",
                             timeout=10, delay=0, max_size=2_000_000, tracker=tracker)

        assert len(urls) == 3  # product URLs from the products sitemap

    @patch("probe_discovery.fetch")
    def test_sitemap_fetch_failure(self, mock_fetch):
        mock_fetch.return_value = (None, None, False, {}, None)
        tracker = TransportTracker()
        client = MagicMock()

        urls = parse_sitemap(client, "https://example.com/sitemap.xml",
                             timeout=10, delay=0, max_size=2_000_000, tracker=tracker)

        assert urls == []

    @patch("probe_discovery.fetch")
    def test_sitemap_invalid_xml(self, mock_fetch):
        mock_fetch.return_value = self._make_fetch_return("this is not xml")
        tracker = TransportTracker()
        client = MagicMock()

        urls = parse_sitemap(client, "https://example.com/sitemap.xml",
                             timeout=10, delay=0, max_size=2_000_000, tracker=tracker)

        assert urls == []

    @patch("probe_discovery.fetch")
    def test_depth_limit(self, mock_fetch):
        """Recursion should stop at MAX_SITEMAP_DEPTH."""
        tracker = TransportTracker()
        client = MagicMock()

        # depth > 3 should return empty immediately without fetching
        urls = parse_sitemap(client, "https://example.com/sitemap.xml",
                             timeout=10, delay=0, max_size=2_000_000, tracker=tracker,
                             depth=4)

        assert urls == []
        mock_fetch.assert_not_called()


# ---------------------------------------------------------------------------
# Integration test — real URL (requires network)
# ---------------------------------------------------------------------------


@pytest.mark.integration
class TestParseRobotsTxtIntegration:
    def test_real_robots_txt(self):
        """Fetch and parse robots.txt from a real website."""
        import httpx

        resp = httpx.get("https://www.harlowbros.co.uk/robots.txt", timeout=15,
                         follow_redirects=True)
        assert resp.status_code == 200

        result = parse_robots_txt(resp.text)
        # robots.txt should have at least one sitemap
        assert len(result["sitemaps"]) >= 1
        # Should have some disallowed paths
        assert isinstance(result["disallowed_paths"], list)


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
