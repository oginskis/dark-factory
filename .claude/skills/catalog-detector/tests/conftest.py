"""Shared fixtures for catalog-detector script tests."""
from __future__ import annotations

import textwrap

import pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "integration: marks tests that require network access")


# ---------------------------------------------------------------------------
# Sample HTML pages
# ---------------------------------------------------------------------------

@pytest.fixture
def minimal_html():
    """Minimal valid HTML page with nav, article, and main tags."""
    return textwrap.dedent("""\
        <html lang="en">
        <head><title>Test</title></head>
        <body>
            <nav><a href="/products">Products</a></nav>
            <main>
                <article>
                    <h1>Welcome to Test Store</h1>
                    <p>We sell quality products at great prices.</p>
                </article>
            </main>
        </body>
        </html>
    """)


@pytest.fixture
def challenge_page_html():
    """HTML that mimics a Cloudflare challenge/interstitial page (small, with markers)."""
    return textwrap.dedent("""\
        <html>
        <head><title>Just a moment...</title></head>
        <body>
            <div id="challenge-platform">
                <div class="cf-browser-verification">
                    Checking if the site connection is secure
                </div>
                <div class="cf-turnstile"></div>
            </div>
        </body>
        </html>
    """)


@pytest.fixture
def shopify_html():
    """HTML page with Shopify platform signals."""
    return textwrap.dedent("""\
        <html lang="en-GB">
        <head>
            <meta name="generator" content="Shopify">
            <link rel="stylesheet" href="https://cdn.shopify.com/s/files/theme.css">
        </head>
        <body>
            <nav><a href="/collections/all">All Products</a></nav>
            <main>
                <h1>Shopify Store</h1>
                <p>This store runs on Shopify and sells widgets.</p>
            </main>
            <script type="application/ld+json">
            {"@type": "Organization", "name": "Test Store"}
            </script>
        </body>
        </html>
    """)


@pytest.fixture
def woocommerce_html():
    """HTML page with WooCommerce platform signals."""
    return textwrap.dedent("""\
        <html>
        <head><title>WooCommerce Store</title></head>
        <body class="woocommerce">
            <link rel="stylesheet" href="/wp-content/themes/storefront/style.css">
            <nav><a href="/shop/">Shop</a></nav>
            <main>
                <div class="products">
                    <div class="product">Widget A</div>
                </div>
            </main>
        </body>
        </html>
    """)


@pytest.fixture
def spa_html():
    """HTML page that looks like a JS-rendered SPA (empty body, Next.js signals)."""
    return textwrap.dedent("""\
        <html>
        <head><title>SPA App</title></head>
        <body>
            <div id="__next" data-reactroot></div>
            <script id="__NEXT_DATA__" type="application/json">{"props":{}}</script>
            <noscript>You need JavaScript to view this page.</noscript>
        </body>
        </html>
    """)


@pytest.fixture
def product_page_html():
    """HTML product page with JSON-LD Product data and CSS-selectable elements."""
    return textwrap.dedent("""\
        <html>
        <head><title>Super Widget - Buy Now</title></head>
        <body>
            <h1 class="product-title">Super Widget</h1>
            <span class="price">$29.99</span>
            <div class="product-description">A fantastic widget for all your needs.</div>
            <table class="spec-table">
                <tr><td>Weight</td><td>250g</td></tr>
                <tr><td>Material</td><td>Steel</td></tr>
            </table>
            <script type="application/ld+json">
            {"@type": "Product", "name": "Super Widget", "offers": {"@type": "Offer", "price": "29.99"}}
            </script>
        </body>
        </html>
    """)


@pytest.fixture
def homepage_with_links():
    """Homepage HTML with catalog and navigation links."""
    return textwrap.dedent("""\
        <html>
        <head><title>Home</title></head>
        <body>
            <nav class="main-menu">
                <a href="/products">Products</a>
                <a href="/shop/tools">Tools</a>
                <a href="/about">About Us</a>
                <a href="/contact">Contact</a>
            </nav>
            <main>
                <a href="/catalog/summer">Summer Catalog</a>
                <a href="/collections/new">New Arrivals</a>
                <a href="javascript:void(0)">Ignore Me</a>
                <a href="#">Also Ignore</a>
            </main>
        </body>
        </html>
    """)


# ---------------------------------------------------------------------------
# Sample robots.txt
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_robots_txt():
    return textwrap.dedent("""\
        User-agent: *
        Disallow: /admin/
        Disallow: /checkout/
        Crawl-delay: 10

        Sitemap: https://www.example.com/sitemap.xml
        Sitemap: https://www.example.com/sitemap-products.xml
    """)


# ---------------------------------------------------------------------------
# Sample sitemap XML
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_sitemap_xml():
    return textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <url><loc>https://www.example.com/product/widget-a</loc></url>
            <url><loc>https://www.example.com/product/widget-b</loc></url>
            <url><loc>https://www.example.com/about</loc></url>
            <url><loc>https://www.example.com/product/gizmo-c</loc></url>
        </urlset>
    """)


@pytest.fixture
def sample_sitemap_index_xml():
    return textwrap.dedent("""\
        <?xml version="1.0" encoding="UTF-8"?>
        <sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
            <sitemap><loc>https://www.example.com/sitemap-products.xml</loc></sitemap>
            <sitemap><loc>https://www.example.com/sitemap-pages.xml</loc></sitemap>
        </sitemapindex>
    """)


# ---------------------------------------------------------------------------
# Sample knowledgebase content
# ---------------------------------------------------------------------------

@pytest.fixture
def sample_knowledgebase_content():
    return textwrap.dedent("""\
        # Shopify Platform Knowledgebase

        ## CSS Selectors

        | Element | Selector | Notes |
        |---------|----------|-------|
        | Product Title | `.product-title` | Main product heading |
        | Price | `.price` | Current price |
        | Description | `.product-description` | Product description text |

        ## JSON-LD Patterns

        Shopify pages typically include `Product` and `BreadcrumbList` JSON-LD types.

        ## Pagination

        URL pattern: `?page={n}`
        Products per page: 24

        ## Shopify JSON API

        - Product JSON: `/products/{handle}.json`
        - Collection JSON: `/collections/{handle}/products.json?page={n}`

        ## Sites Using This Platform

        | Slug | URL | Notes |
        |------|-----|-------|
        | test-store | https://test-store.com | Test |
    """)


# ---------------------------------------------------------------------------
# Sample assessment markdown (success template)
# ---------------------------------------------------------------------------

@pytest.fixture
def success_assessment_content():
    return textwrap.dedent("""\
        # Catalog Assessment: Test Company

        **Slug:** test-company
        **URL:** https://www.test-company.com
        **Platform:** shopify
        **Scraping strategy:** json_api
        **Anti-bot:** none (no challenges detected)
        **Estimated product count:** ~500

        ## Extraction Blueprint

        ### Data Source

        **Primary method:** JSON-LD structured data
        **Endpoint/URL pattern:** /products/{handle}.json

        ### Product Discovery

        **Discovery method:** sitemap
        **Pagination mechanism:** query parameter
        **Products per page:** 24
        **Pagination URL pattern:** ?page={n}

        #### Verified Category Tree

        | Category | URL | Product Count |
        |----------|-----|---------------|
        | Tools | /collections/tools | 150 |
        | Parts | /collections/parts | 350 |

        #### Price

        **CSS selector:** `.price`
        **Verified on:**
        - https://www.test-company.com/products/widget-a - $29.99
        - https://www.test-company.com/products/widget-b - $49.99

        #### Spec Table / Attributes

        **CSS selector:** `.spec-table td`
        **Verified on:**
        - https://www.test-company.com/products/widget-a - 5 attributes
        - https://www.test-company.com/products/widget-b - 3 attributes

        ## Platform-Specific Notes

        Standard Shopify setup with no customizations.
    """)


# ---------------------------------------------------------------------------
# Sample assessment markdown (stop template)
# ---------------------------------------------------------------------------

@pytest.fixture
def stop_assessment_content():
    return textwrap.dedent("""\
        # Catalog Assessment: Blocked Company

        **Slug:** blocked-company
        **URL:** https://www.blocked-company.com
        **Platform:** unknown
        **Scraping strategy:** none
        **Stop reason:** anti_bot_severe

        ## Findings

        - Site uses Cloudflare Turnstile with aggressive challenge on every page
        - No public API endpoints detected
        - All product pages return 403 after initial challenge
    """)
