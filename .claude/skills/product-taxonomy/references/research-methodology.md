# SKU Attribute Research Methodology

This guide describes how to systematically discover and document the SKU attributes for a tangible goods subcategory. Read this before starting any research.

## Scope: Tangible Goods Only

This research is exclusively about **physical, tangible products** — items that are manufactured, shipped, stored in warehouses, and handled by customers. Every attribute you record should describe something about a physical object.

**In scope:**
- Physical dimensions, weight, materials, color, finish
- Manufacturing specs: power, voltage, capacity, tolerances, pressure ratings
- Packaging: box dimensions, shipping weight, units per case
- Identifiers: SKU, model number, part number, UPC/EAN/GTIN
- Commercial: price, MOQ, lead time, availability
- Compliance: safety certifications, environmental ratings, country of origin
- Categorization: product line, series, intended application

**Out of scope — ignore these even if you see them on product pages:**
- Software features, app integrations, cloud services
- Subscription plans, SaaS tiers, license types
- Digital downloads, e-books, streaming content
- Service agreements, warranty plans (note warranty *duration* as an attribute, but not the plan details)
- User reviews, ratings, Q&A content (these describe customer opinion, not the product)

When in doubt, ask: "Does this attribute describe the physical object itself, or something layered on top of it?" Only record the former.

## Research Angles

Cover these 4 angles to build a complete picture. Each angle reveals different attributes that the others miss.

### Angle 1: Product Catalogs (3-5 websites)

Visit actual product pages from a mix of company types:

| Company Type | Why | Example Sources |
|---|---|---|
| **Manufacturer** | Deepest technical specs, proprietary naming | Company's own product pages |
| **B2B Distributor** | Standardized attributes across brands, filterable catalogs | Grainger, McMaster-Carr, RS Components, MSC Industrial |
| **Retail / E-commerce** | Consumer-facing attributes, what people filter by | Amazon, Home Depot, Walmart |
| **Specialty retailer** | Category-specific attributes that generalists miss | Woodcraft (tools), Wayfair (furniture), Digi-Key (electronics) |

Distributors are often the most valuable — they normalize attributes across dozens of brands, revealing the "industry standard" schema.

### Angle 2: Industry Standards & Classification Systems

Research how the industry itself classifies and describes products:
- **International standards bodies**: ISO standards for the category, IEC, ASTM, EN standards
- **Product classification systems**: How does UNSPSC or GPC classify products in this category? What attributes do they use?
- **Industry associations**: Trade groups often publish product data standards (e.g., GS1 for retail, CEFIC for chemicals, AHAM for appliances)

This grounds the schema in internationally accepted terminology rather than any single company's or country's naming.

### Angle 3: Regulatory & Compliance (international only)

Identify the universal compliance attributes for the category:
- What international certifications apply? (ISO, CE, GMP, HACCP, RoHS, REACH)
- What labeling is required globally, not just in one country?
- Avoid country-specific regulatory details — no individual country registrations, no locale-specific certifications

The goal is a compliance attribute set that works across markets.

### Angle 4: Data Model Patterns

Check how existing product data platforms model this category:
- How do major e-commerce platforms structure their product data? (What are the required vs optional fields?)
- Are there open product data standards for this category?
- What do comparison/review sites use as their attribute columns?

This reveals which attributes are commercially important — the ones platforms actually use to filter, compare, and match products.

## Tool Selection for Web Research

**WebFetch** works well for most manufacturer and B2B distributor sites — they tend to serve content as static HTML.

**Playwright** (browser automation) is better for JavaScript-heavy sites that WebFetch can't render. Use Playwright when:
- The site is a modern e-commerce platform (fashion brands, consumer electronics retailers)
- WebFetch returns empty or incomplete content (missing product specs, no tables)
- The site requires interaction to reveal specs (clicking tabs, expanding sections, selecting variants)
- You need to use faceted navigation filters to discover filterable attributes

Typical Playwright workflow: `browser_navigate` to the URL, then `browser_snapshot` to read the rendered content. Use `browser_click` to expand spec tabs or interact with filters.

**WebSearch** is for finding companies and product page URLs — don't use it to extract product specs directly.

## What to Look For on a Product Page

For each product page you visit, systematically scan these areas:

### 1. Product Title and Naming
- How is the product named? Is there a naming convention encoding attributes? (e.g., Festool "TS 55 FEQ-F-Plus" encodes tool type, size, features, and bundle)
- Model number, series name, collection name

### 2. Specification Table
- This is the primary source. Copy every row.
- Note both the label and the value format (number, text, enum, boolean)
- Pay attention to units (mm vs inches, W vs HP, kg vs lbs)

### 3. Product Identifiers
- SKU / Article number / Item number
- UPC / EAN / GTIN barcodes
- Manufacturer part number vs retailer SKU (often different)

### 4. Variant Selectors
- What can the customer choose? Color, size, material, voltage, configuration
- Each variant selector is an attribute

### 5. Filtering / Faceted Navigation
- Go to the category listing page and look at the left sidebar filters
- These are the attributes the platform considers most important for product differentiation
- Record every filter option and its possible values

### 6. Comparison Tables
- If the site has a "compare products" feature, use it
- Comparison tables explicitly show which attributes the manufacturer considers differentiating

### 7. Downloads and Documents
- Spec sheet PDFs often contain attributes not shown on the web page
- Safety data sheets reveal compliance attributes
- CAD files indicate engineering-grade dimensional data is available

### 8. Packaging and Shipping Info
- Box dimensions, shipping weight, units per carton
- Often hidden in a "Shipping" tab — don't skip it

## Recording Attributes

For each attribute you discover, record:

| Field | What to capture |
|---|---|
| **Name** | The label as it appears on the site (you'll standardize later) |
| **Data type** | text, number, enum, boolean (append unit in parentheses when relevant, e.g. number (kg), text (mm); use text (list) for multi-value fields) |
| **Unit** | mm, inches, kg, lbs, W, V, °C, PSI, etc. |
| **Example values** | 2-3 real values from actual products |
| **Where found** | Which company/page (for sourcing) |
| **Prevalence** | Did you see this on most products, or just some? |

## Attribute Types to Watch For

Don't stop at the obvious specs. Physical products have attributes across many dimensions:

**Identity & Classification**
- Product name, model, SKU, UPC/EAN
- Product line / series / collection / family
- Application / use case / trade

**Physical Properties**
- Dimensions (L×W×H), weight, volume
- Material, finish, color, texture
- Operating temperature range, IP rating

**Performance / Technical**
- Power (W, HP, V, A), speed (RPM), torque
- Capacity, flow rate, pressure, tolerance
- Battery voltage, battery capacity (Ah)

**Commercial**
- Price (number only — never include currency symbol in the value)
- Currency (separate attribute: USD, EUR, GBP, JPY, etc.)
- MSRP, MAP price
- Availability, lead time, MOQ
- Country of origin, manufacturer

**Packaging & Logistics**
- Package dimensions, shipping weight
- Units per case/pallet, HTS code
- Hazmat classification

**Compliance & Certification**
Keep these international and universal. Include widely recognized standards only:
- Safety: CE, UL, ISO standards
- Environmental: RoHS, REACH, Energy Star
- Industry-specific: ISO 9001, GMP, HACCP (for food)
- Avoid country-specific regulatory details (individual state registrations, locale-specific certifications, country-specific label requirements)

**Media & Documentation**
- Number of product images, has video, has 360° view
- Spec sheet PDF available, CAD files available
- Assembly instructions included

## Common Pitfalls

- **Don't record marketing copy as attributes.** "Best-in-class performance" is not an attribute. "1,400W motor" is.
- **Don't confuse category navigation with product attributes.** "Power Tools > Saws > Track Saws" is a catalog path, not a product attribute. But "Tool Type: Track Saw" is.
- **Watch for regional variants.** The same product may have different specs by region (voltage, certifications). Note the region if specs differ.
- **Normalize units later, not during collection.** Record what you see. Standardize in the synthesis phase.
