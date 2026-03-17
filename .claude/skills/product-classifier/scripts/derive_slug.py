# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""
Derive a deterministic company slug from a URL or hostname.

WHEN TO CALL: At the start of product-classifier, before any investigation.
ARGUMENTS: --url <url_or_hostname> (required)
EXIT CODES: 0 = slug derived, 2 = crash

The slug algorithm:
1. Extract hostname from URL
2. Strip subdomain prefixes (www., shop., store., etc.)
3. Drop the TLD (last segment for single-part TLDs, last two for known multi-part TLDs)
4. What remains is the slug. Keep hyphens.

INTERPRETATION:
    slug → use as the filename for the company report: {slug}.md
    hostname → the company's registrable domain (for redirect detection)
"""
from __future__ import annotations

import argparse
import json
import sys
from urllib.parse import urlparse


MULTI_PART_TLDS = {
    "co.uk", "com.au", "co.jp", "co.nz", "co.za", "com.br", "com.mx",
    "com.ar", "com.tr", "com.sg", "com.hk", "com.my", "co.kr", "co.in",
    "co.id", "co.th", "com.ua", "com.pl", "com.eg", "co.il", "com.vn",
    "com.pk", "com.ng", "com.bd", "com.ph", "com.tw", "com.pe", "com.co",
    "com.ve", "com.ec", "com.gt", "com.do", "org.uk", "net.au", "ac.uk",
}

SUBDOMAIN_PREFIXES = {"www", "shop", "store", "boutique", "webshop", "estore"}


def derive_slug(url_or_hostname: str) -> dict:
    """Derive slug from URL or hostname. Returns {"slug": str, "hostname": str}."""
    # Normalize: if it looks like a bare hostname, add scheme
    if "://" not in url_or_hostname:
        url_or_hostname = "https://" + url_or_hostname

    parsed = urlparse(url_or_hostname)
    hostname = parsed.hostname or parsed.path
    hostname = hostname.lower().rstrip(".")

    # Strip known subdomain prefixes
    parts = hostname.split(".")
    if len(parts) > 2 and parts[0] in SUBDOMAIN_PREFIXES:
        parts = parts[1:]
    registrable = ".".join(parts)

    # Drop TLD
    domain_parts = registrable.split(".")
    if len(domain_parts) >= 3:
        # Check for multi-part TLD
        candidate_tld = ".".join(domain_parts[-2:])
        if candidate_tld in MULTI_PART_TLDS:
            slug = ".".join(domain_parts[:-2])
        else:
            slug = ".".join(domain_parts[:-1])
    elif len(domain_parts) == 2:
        slug = domain_parts[0]
    else:
        slug = domain_parts[0]

    return {"slug": slug, "hostname": registrable}


def main() -> None:
    parser = argparse.ArgumentParser(description="Derive company slug from URL")
    parser.add_argument("--url", required=True, help="Company URL or hostname")
    args = parser.parse_args()

    try:
        result = derive_slug(args.url)
    except Exception as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        sys.exit(2)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
