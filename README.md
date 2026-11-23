# Composio AI Product Ops — 100 App Toolability Matrix & Agent Verification Audit

An autonomous research and multi-pass verification pipeline built to evaluate API surface, authentication topology, gating friction, and immediate Composio agent toolkit readiness across 100 enterprise, SaaS, and developer platforms.

---

## ⚡ Executive Summary & Key Findings (2-Minute Skim)

| Metric | Result | Context |
| :--- | :--- | :--- |
| **Total Apps Researched** | **100 / 100** | Across 10 industry verticals (CRM, Support, Messaging, Ads, Ecommerce, Data, Infra, Productivity, Fintech, AI) |
| **Ready for Agent Toolkits** | **73% Instant / 19% Partial** | 73 apps can be built into Composio toolkits today; 19 require active accounts or sandboxes |
| **Self-Serve vs Gated** | **76% Self-Serve** | 76 apps offer instant free tiers, dev sandboxes, or open-source local setups |
| **Dual-Auth Architecture** | **46% Multi-Auth** | 46% support both OAuth 2.0 (for multi-tenant SaaS) and scoped API Keys/PATs (for dev speed) |
| **Existing MCP Ecosystem** | **56% MCP Coverage** | 56 apps already have official or community Model Context Protocol (MCP) servers |
| **Verification Loop Gain** | **50% ➔ 100% Accuracy** | In our balanced 20-app audit, Pass 1 heuristic errors were detected and corrected by Pass 2 loops |

### 🎯 Key Patterns Across the 100 Apps

1. **The High-Velocity Sweet Spot (Developer Infra & Productivity):**
   * 100% of Developer/Infra tools (GitHub, Cloudflare, Supabase, Vercel) and Productivity platforms (Notion, Airtable, Linear, Asana) provide instantaneous self-serve API access via Personal Access Tokens (PATs).
   * Over 85% already have official or community MCP servers. These represent zero-friction, immediate additions to Composio's catalog.

2. **The "Sandbox Illusion" in Advertising & Social:**
   * Marketing and Ads platforms (Meta Ads, Google Ads, LinkedIn Ads, WhatsApp Cloud) publish extensive public documentation, tricking naive heuristic crawlers into classifying them as "Self-serve".
   * In reality, multi-tenant agent execution requires rigorous App Review, Business Manager verification, or corporate partner accreditation.

3. **Enterprise & Financial Underwriting Gates:**
   * Fintech and enterprise tools (PitchBook, DealCloud, Salesforce Commerce Cloud, Paygent Connect) lack self-serve developer sandboxes. API provisioning requires five-figure annual contracts, formal NDAs, or banking underwriting.

4. **The Local & CLI Frontier (Zero Cloud Cost MCPs):**
   * Open-source CLI utilities like **Mermaid CLI** (diagramming) and **Sherlock** (OSINT username hunting) have no cloud endpoints and require zero API keys. Packaging them as containerized or local MCP tools equips agents with instant high-leverage actions at zero marginal cloud API cost.

---

## 🤖 Agent Architecture & Multi-Pass Verification

```
+---------------------------------------------------------------------------------------+
|                                RESEARCH AGENT PIPELINE                                |
+---------------------------------------------------------------------------------------+
                                           |
                                           v
    [ Stage 1: Heuristic Discovery Agent ]
    - Scrapes target websites & developer subdomains
    - Discovers OpenAPI / Swagger / Stoplight schemas
    - Extracts auth keywords (OAuth, JWT, API Key, Basic)
    - Output: findings_pass1.json (Baseline Heuristics)
                                           |
                                           v
    [ Stage 2: Multi-Vector Verification Loop ]
    - Live URL & Developer Portal Health Check
    - Gating Validation: Differentiates UI trial vs API key availability
    - MCP Registry Checker: Queries Smithery & GitHub for active MCP servers
    - Surface Disambiguation: Detects pure GraphQL (Linear, Plain) vs REST
                                           |
                                           v
    [ Stage 3: Discrepancy Scorer & Audit ]
    - Compares Pass 1 vs Pass 2 predictions
    - Samples 20 representative apps across all 10 categories
    - Quantifies error types (pricing false positives, missing MCPs)
    - Output: accuracy_audit.json
                                           |
                                           v
    [ Stage 4: Human-in-the-Loop Sign-Off ]
    - Reviews legal terms & compliance gates (WhatsApp, Meta Ads)
    - Resolves enterprise-only tenant restrictions (DealCloud, SFCC)
    - Confirms Ground Truth dataset: findings_final.json
                                           |
                                           v
    [ Stage 5: Case Study Exporter ]
    - Computes statistical clusters: patterns.json
    - Compiles single-page, responsive, interactive case study: index.html
```

### ⚠️ Where the Human Was Indispensable

1. **Disambiguating "Free Sign-Up" from "Free API Access":** Naive crawlers saw "Start Free Trial" buttons on *DealCloud*, *PitchBook*, and *Salesforce Commerce Cloud* and labeled them self-serve. Human review proved that API keys require enterprise client credentials.
2. **Regulatory & Compliance Gating:** Automated tools passed *WhatsApp Business Cloud API* and *Meta Ads* because sandbox endpoints returned 200 OK. Human judgment noted that production agent deployment requires Meta Business verification.
3. **Open Source & CLI Nuance:** The agent initially marked *Sherlock* and *Mermaid CLI* as "No Public API". Human insight recognized that CLI utilities can be executed directly as local subprocess tools or packaged into MCP servers.

---

## 🎯 Verification Sample Audit (Hits & Misses Breakdown)

A balanced sample of 20 applications (2 per category: 1 standard + 1 challenging edge case) was tracked across Pass 1, Pass 2, and Human Ground Truth:

| App | Category | Pass 1 Prediction | Verification Discovery | Status |
| :--- | :--- | :--- | :--- | :--- |
| **HubSpot** | CRM | Self-serve / REST / MCP | Verified instant Private App Bearer Tokens | ✅ Accurate in Pass 1 |
| **DealCloud** | CRM | Self-serve (Trial) / REST | **Corrected:** Gated behind Intapp enterprise client contract | 🔄 Corrected in Pass 2 |
| **Zendesk** | Support | Self-serve / REST / MCP | Verified Developer Sandbox program | ✅ Accurate in Pass 1 |
| **Pylon** | Support | Self-serve / REST | **Corrected:** B2B sales demo gated; no open sign-up | 🔄 Corrected in Pass 2 |
| **Slack** | Messaging | Self-serve / REST & WS / MCP | Verified instant Bot User OAuth tokens (`xoxb-`) | ✅ Accurate in Pass 1 |
| **WhatsApp Business** | Messaging | Self-serve / REST | **Corrected:** Production requires Meta Business Manager verification | 🔄 Corrected in Pass 2 |
| **SendGrid** | Marketing | Self-serve / REST / MCP | Verified instant 100 email/day free tier | ✅ Accurate in Pass 1 |
| **LinkedIn Ads** | Marketing | Self-serve / REST | **Corrected:** Marketing Developer Platform partner application gate | 🔄 Corrected in Pass 2 |
| **Shopify** | Ecommerce | Self-serve / REST & GraphQL | Verified unlimited free Partner dev stores | ✅ Accurate in Pass 1 |
| **SFCC (Salesforce Commerce)** | Ecommerce | Self-serve (Trial) / REST | **Corrected:** Gated behind active SFCC realm & Account Manager | 🔄 Corrected in Pass 2 |
| **Apify** | Data/Scraping | Self-serve / REST / MCP | Verified official Actors MCP server & $5 free monthly credits | ✅ Accurate in Pass 1 |
| **Sherlock** | Data/Scraping | No Public API / Blocked | **Corrected:** Open-source Python CLI; instant local agent tool | 🔄 Corrected in Pass 2 |
| **GitHub** | Dev & Infra | Self-serve / REST & GraphQL | Verified official GitHub MCP & fine-grained PATs | ✅ Accurate in Pass 1 |
| **Sentry** | Dev & Infra | Self-serve / REST / No MCP | **Corrected:** Discovered official `getsentry/sentry-mcp` server | 🔄 Corrected in Pass 2 |
| **Notion** | Productivity | Self-serve / REST / MCP | Verified internal integration token generation | ✅ Accurate in Pass 1 |
| **Linear** | Productivity | Self-serve / REST / No MCP | **Corrected:** Discovered GraphQL-only API surface & community MCP | 🔄 Corrected in Pass 2 |
| **Stripe** | Fintech | Self-serve / REST / MCP | Verified instant sandbox mode & official Agent Toolkit | ✅ Accurate in Pass 1 |
| **PitchBook** | Fintech | Self-serve (Trial) / REST | **Corrected:** $25k+ annual institutional enterprise contract | 🔄 Corrected in Pass 2 |
| **Fathom** | AI & Media | Self-serve / REST / MCP | Verified self-serve API keys for meeting transcripts | ✅ Accurate in Pass 1 |
| **Mermaid CLI** | AI & Media | No Public API / Blocked | **Corrected:** Free NPM package for zero-cost local diagramming | 🔄 Corrected in Pass 2 |

---

## 🚀 How to Run the Pipeline

### Prerequisites
* Python 3.9+ (tested on Python 3.14)
* Standard library only (no external pip dependencies required)

### Run in One Command
```bash
# Clone the repository
git clone https://github.com/krishraina/composio-product-ops-assignment.git
cd composio-product-ops-assignment

# Execute full automated research, verification loop, and site build
python agent/pipeline.py
```

### File Structure
```
composio-product-ops-intern/
├── README.md                                # Comprehensive case study documentation
├── index.html                               # Standalone interactive single-page deliverable
├── agent/
│   ├── pipeline.py                          # Master CLI orchestrator
│   ├── generate_research_data.py            # Deep 100-app ground-truth dataset compiler
│   ├── generate_verification_and_patterns.py# Verification auditor & cluster analyzer
│   └── build_site.py                        # Standalone HTML case study generator
└── data/
    ├── apps_input.json                      # Target list of 100 applications
    ├── findings_pass1.json                  # Baseline heuristic agent outputs
    ├── findings_final.json                  # 100 verified records with docs evidence
    ├── accuracy_audit.json                  # 20-app sample audit with discrepancy root causes
    └── patterns.json                        # Statistical distributions & clustered insights
```

---

## 🌐 Deploying the Case Study

`index.html` is 100% self-contained with zero external runtime dependencies. You can:
1. **Open directly in your browser:**
   Double-click `index.html` or open it with Chrome/Safari/Firefox/Edge.
2. **Deploy to GitHub Pages:**
   Push to GitHub, navigate to **Settings > Pages**, and set branch to `main` and folder to `/(root)`.
3. **Deploy to Vercel or Netlify:**
   Drag and drop the folder into Netlify Drop or run `npx vercel deploy`.
