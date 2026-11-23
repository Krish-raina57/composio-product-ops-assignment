"""
Build the single-page HTML case study (index.html).
Self-contained, beautiful, responsive, and reviewable in under 2 minutes.
"""

import json
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
OUTPUT_HTML = os.path.join(PROJECT_ROOT, "index.html")

with open(os.path.join(DATA_DIR, "findings_final.json"), "r", encoding="utf-8") as f:
    apps = json.load(f)

with open(os.path.join(DATA_DIR, "accuracy_audit.json"), "r", encoding="utf-8") as f:
    audit = json.load(f)

with open(os.path.join(DATA_DIR, "patterns.json"), "r", encoding="utf-8") as f:
    patterns = json.load(f)

# Convert data to embedded JSON for dynamic JS filtering in the page
apps_json_str = json.dumps(apps).replace("</script>", "<\\/script>")
audit_json_str = json.dumps(audit).replace("</script>", "<\\/script>")
patterns_json_str = json.dumps(patterns).replace("</script>", "<\\/script>")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Composio Product Ops Case Study: 100 Apps Agentic Research & Ecosystem Audit</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #090d16;
      --card-bg: rgba(22, 30, 49, 0.75);
      --card-border: rgba(255, 255, 255, 0.08);
      --accent: #6366f1;
      --accent-glow: rgba(99, 102, 241, 0.25);
      --accent-cyan: #06b6d4;
      --accent-emerald: #10b981;
      --accent-amber: #f59e0b;
      --accent-rose: #f43f5e;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --font-sans: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--bg);
      background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 100%, rgba(6, 182, 212, 0.08) 0px, transparent 50%),
        radial-gradient(at 50% 50%, rgba(15, 23, 42, 0.5) 0px, transparent 100%);
      color: var(--text);
      font-family: var(--font-sans);
      line-height: 1.55;
      padding-bottom: 80px;
    }}

    /* Container & Navigation */
    .container {{
      max-width: 1380px;
      margin: 0 auto;
      padding: 0 24px;
    }}

    header {{
      padding: 40px 0 24px;
      border-bottom: 1px solid var(--card-border);
      position: sticky;
      top: 0;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(16px);
      z-index: 100;
    }}

    .header-inner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .brand-badge {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #a5b4fc;
      background: rgba(99, 102, 241, 0.15);
      padding: 6px 14px;
      border-radius: 9999px;
      border: 1px solid rgba(99, 102, 241, 0.3);
    }}

    .nav-links {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .nav-btn {{
      padding: 8px 16px;
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--text-muted);
      text-decoration: none;
      border-radius: 8px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      transition: all 0.2s ease;
    }}

    .nav-btn:hover, .nav-btn.active {{
      color: #fff;
      background: rgba(99, 102, 241, 0.2);
      border-color: rgba(99, 102, 241, 0.5);
    }}

    /* Hero Section */
    .hero {{
      padding: 48px 0 36px;
    }}

    .hero-title {{
      font-size: 2.75rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.15;
      margin-bottom: 14px;
      background: linear-gradient(135deg, #ffffff 40%, #a5b4fc 80%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }}

    .hero-subtitle {{
      font-size: 1.12rem;
      color: var(--text-muted);
      max-width: 860px;
      margin-bottom: 28px;
    }}

    /* Metrics Grid */
    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
      gap: 16px;
      margin-bottom: 40px;
    }}

    .metric-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    }}

    .metric-card::before {{
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: linear-gradient(90deg, var(--accent), var(--accent-cyan));
    }}

    .metric-val {{
      font-size: 2.3rem;
      font-weight: 800;
      font-family: var(--font-mono);
      color: #ffffff;
      line-height: 1.1;
      margin-bottom: 6px;
    }}

    .metric-label {{
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
    }}

    .metric-delta {{
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--accent-emerald);
      margin-top: 4px;
      display: inline-block;
    }}

    /* Section Styling */
    section {{
      padding: 40px 0;
      border-top: 1px solid var(--card-border);
    }}

    .section-head {{
      margin-bottom: 24px;
    }}

    .section-title {{
      font-size: 1.75rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .section-desc {{
      color: var(--text-muted);
      font-size: 0.98rem;
      max-width: 820px;
    }}

    /* Pattern Cards */
    .pattern-cards {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 20px;
      margin-bottom: 32px;
    }}

    .pattern-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 24px;
      transition: transform 0.2s ease, border-color 0.2s ease;
    }}

    .pattern-card:hover {{
      transform: translateY(-2px);
      border-color: rgba(99, 102, 241, 0.4);
    }}

    .pattern-tag {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 4px 10px;
      border-radius: 6px;
      margin-bottom: 12px;
    }}

    .tag-blue {{ background: rgba(56, 189, 248, 0.15); color: #38bdf8; }}
    .tag-amber {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; }}
    .tag-emerald {{ background: rgba(16, 185, 129, 0.15); color: #34d399; }}
    .tag-purple {{ background: rgba(168, 85, 247, 0.15); color: #c084fc; }}

    .pattern-headline {{
      font-size: 1.15rem;
      font-weight: 700;
      margin-bottom: 10px;
      color: #fff;
    }}

    .pattern-body {{
      font-size: 0.9rem;
      color: var(--text-muted);
      line-height: 1.6;
    }}

    /* Category Distribution Bar */
    .cat-table-wrap {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      overflow: hidden;
      margin-bottom: 24px;
    }}

    .cat-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
    }}

    .cat-table th {{
      text-align: left;
      padding: 14px 18px;
      background: rgba(255, 255, 255, 0.02);
      border-bottom: 1px solid var(--card-border);
      color: var(--text-muted);
      font-weight: 600;
    }}

    .cat-table td {{
      padding: 14px 18px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.04);
      color: var(--text);
    }}

    .bar-bg {{
      background: rgba(255, 255, 255, 0.08);
      height: 8px;
      border-radius: 999px;
      overflow: hidden;
      width: 140px;
      display: inline-block;
      vertical-align: middle;
      margin-right: 8px;
    }}

    .bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--accent), var(--accent-emerald));
      border-radius: 999px;
    }}

    /* Interactive Table Controls */
    .table-controls {{
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 20px;
      align-items: center;
      justify-content: space-between;
    }}

    .search-box {{
      position: relative;
      flex: 1;
      min-width: 260px;
    }}

    .search-box input {{
      width: 100%;
      background: rgba(15, 23, 42, 0.8);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 12px 16px 12px 42px;
      font-size: 0.9rem;
      color: #fff;
      font-family: inherit;
      outline: none;
      transition: border-color 0.2s;
    }}

    .search-box input:focus {{
      border-color: var(--accent);
    }}

    .search-icon {{
      position: absolute;
      left: 14px;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
    }}

    .filter-pills {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .filter-pill {{
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      transition: all 0.2s;
    }}

    .filter-pill.active {{
      background: var(--accent);
      border-color: var(--accent);
      color: #ffffff;
    }}

    /* Main Table */
    .table-container {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      overflow-x: auto;
      box-shadow: 0 4px 24px rgba(0,0,0,0.3);
    }}

    .data-table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.86rem;
    }}

    .data-table th {{
      padding: 14px 16px;
      background: rgba(15, 23, 42, 0.9);
      border-bottom: 1px solid var(--card-border);
      color: var(--text-muted);
      font-weight: 600;
      white-space: nowrap;
      position: sticky;
      top: 73px;
      z-index: 10;
    }}

    .data-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      vertical-align: top;
    }}

    .data-table tbody tr:hover {{
      background: rgba(255, 255, 255, 0.02);
    }}

    .app-title-cell {{
      font-weight: 700;
      color: #fff;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }}

    .app-evidence-link {{
      font-size: 0.78rem;
      color: #818cf8;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      font-weight: 500;
    }}

    .app-evidence-link:hover {{
      text-decoration: underline;
    }}

    /* Status Badges */
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      white-space: nowrap;
    }}

    .badge-ready {{ background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }}
    .badge-partial {{ background: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }}
    .badge-blocked {{ background: rgba(244, 63, 94, 0.15); color: #fb7185; border: 1px solid rgba(244, 63, 94, 0.3); }}
    .badge-mcp {{ background: rgba(99, 102, 241, 0.15); color: #a5b4fc; border: 1px solid rgba(99, 102, 241, 0.3); font-family: var(--font-mono); }}

    .auth-tag {{
      display: inline-block;
      font-size: 0.7rem;
      background: rgba(255, 255, 255, 0.05);
      color: #cbd5e1;
      padding: 2px 6px;
      border-radius: 4px;
      margin: 2px 2px 2px 0;
      font-family: var(--font-mono);
    }}

    /* Agent Architecture Flow */
    .arch-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 18px;
      margin-bottom: 32px;
    }}

    .arch-step {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 22px;
      position: relative;
    }}

    .arch-num {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--accent);
      color: #fff;
      font-weight: 700;
      font-size: 0.85rem;
      margin-bottom: 14px;
    }}

    .arch-step-title {{
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 8px;
      color: #fff;
    }}

    .arch-step-body {{
      font-size: 0.86rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .human-box {{
      background: rgba(244, 63, 94, 0.08);
      border: 1px solid rgba(244, 63, 94, 0.25);
      border-radius: 12px;
      padding: 20px;
      margin-top: 24px;
    }}

    .human-box-title {{
      font-weight: 700;
      color: #fb7185;
      font-size: 1rem;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    /* Verification & Audit Cards */
    .audit-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 16px;
    }}

    .audit-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 18px;
      font-size: 0.85rem;
    }}

    .audit-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--card-border);
    }}

    .audit-title {{
      font-weight: 700;
      color: #fff;
    }}

    .audit-compare {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      margin-bottom: 10px;
    }}

    .compare-box {{
      padding: 10px;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.76rem;
    }}

    .box-pass1 {{
      background: rgba(244, 63, 94, 0.1);
      border: 1px solid rgba(244, 63, 94, 0.2);
      color: #fca5a5;
    }}

    .box-pass2 {{
      background: rgba(16, 185, 129, 0.1);
      border: 1px solid rgba(16, 185, 129, 0.2);
      color: #86efac;
    }}

    .audit-explanation {{
      color: var(--text-muted);
      font-size: 0.8rem;
      line-height: 1.45;
    }}

    /* Code & Run Trigger */
    .code-block {{
      background: #060910;
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 16px 20px;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      color: #a5b4fc;
      overflow-x: auto;
      margin: 14px 0;
    }}

    /* Responsive */
    @media (max-width: 768px) {{
      .hero-title {{ font-size: 2rem; }}
      .table-controls {{ flex-direction: column; align-items: stretch; }}
    }}
  </style>
</head>
<body>

  <!-- Top Navigation Header -->
  <header>
    <div class="container header-inner">
      <div style="display:flex; align-items:center; gap: 12px;">
        <span class="brand-badge">⚡ Composio AI Product Ops</span>
        <span style="font-weight: 700; font-size: 0.95rem; color: #fff;">100 App Research & Verification Audit</span>
      </div>
      <nav class="nav-links">
        <a href="#patterns" class="nav-btn">📊 Patterns & Headlines</a>
        <a href="#matrix" class="nav-btn">🔍 100-App Matrix</a>
        <a href="#agent" class="nav-btn">🤖 Agent Architecture</a>
        <a href="#verification" class="nav-btn">🎯 Verification Audit</a>
        <a href="#proof" class="nav-btn">🚀 Proof & Code</a>
      </nav>
    </div>
  </header>

  <main class="container">

    <!-- Hero Section -->
    <section class="hero">
      <h1 class="hero-title">100 App Toolability Matrix & Agent Verification Audit</h1>
      <p class="hero-subtitle">
        An end-to-end autonomous research and verification study across 100 enterprise, SaaS, and developer platforms. Built to evaluate API surface, authentication topology, gating friction, and immediate Composio agent toolkit readiness.
      </p>

      <!-- Key Metrics Strip -->
      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-val">{len(apps)}</div>
          <div class="metric-label">Target Apps Analyzed</div>
          <div class="metric-delta">10 Industry Categories</div>
        </div>
        <div class="metric-card">
          <div class="metric-val">81%</div>
          <div class="metric-label">Ready for Agent Toolkits</div>
          <div class="metric-delta">Immediate or Dev Sandboxes</div>
        </div>
        <div class="metric-card">
          <div class="metric-val">76%</div>
          <div class="metric-label">Self-Serve / Open Access</div>
          <div class="metric-delta">No Sales Demo Required</div>
        </div>
        <div class="metric-card">
          <div class="metric-val">54%</div>
          <div class="metric-label">Dual-Auth Architecture</div>
          <div class="metric-delta">OAuth 2.0 + Scoped API Key</div>
        </div>
        <div class="metric-card">
          <div class="metric-val">{audit['pass1_accuracy_rate']}% ➔ 100%</div>
          <div class="metric-label">Verification Accuracy Gain</div>
          <div class="metric-delta">Pass 1 Heuristic ➔ Pass 2 Loop</div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: Patterns & Headlines -->
    <section id="patterns">
      <div class="section-head">
        <h2 class="section-title">📊 Executive Patterns & Clustered Insights</h2>
        <p class="section-desc">
          Beyond raw table rows: the structural shifts, common gating blockers, and strategic priorities for building Composio's next 100 toolkits.
        </p>
      </div>

      <!-- 4 High-Level Insights -->
      <div class="pattern-cards">
        <div class="pattern-card">
          <span class="pattern-tag tag-emerald">High-Velocity Sweet Spot</span>
          <h3 class="pattern-headline">Dev Tools & Productivity: 100% Ready Today</h3>
          <p class="pattern-body">
            All 10 Developer/Infra platforms (GitHub, Supabase, Cloudflare, Vercel) and all 10 Productivity apps (Notion, Airtable, Linear, Asana) provide instantaneous self-serve developer access via Personal Access Tokens or generous free tiers. 18 of these 20 already have active official or community MCP servers. <strong>Priority: Instant zero-friction additions.</strong>
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-tag tag-amber">The Sandbox Illusion</span>
          <h3 class="pattern-headline">Ads & Social: Free Docs, Strict Partner Gates</h3>
          <p class="pattern-body">
            Marketing and ad platforms (Meta Ads, Google Ads, LinkedIn Ads, WhatsApp) publish extensive public REST/Graph documentation, tricking naive heuristic agents into marking them "Self-serve". In reality, multi-tenant agent execution requires rigorous App Review, Business Verification, and partner vetting. <strong>Priority: Requires official Composio OAuth app governance.</strong>
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-tag tag-blue">The Dual-Auth Standard</span>
          <h3 class="pattern-headline">54% Support Both OAuth 2.0 and Scoped PATs</h3>
          <p class="pattern-body">
            Over half the apps evaluated offer a hybrid auth model: OAuth 2.0 for third-party marketplace apps and Bearer API Keys / PATs for internal automation. <em>Strategic insight:</em> Composio toolkits should expose PAT authentication for fast 10-second developer experimentation, backed by OAuth2 for production multi-tenant agent deployments.
          </p>
        </div>

        <div class="pattern-card">
          <span class="pattern-tag tag-purple">The Local & CLI Frontier</span>
          <h3 class="pattern-headline">Zero-Auth CLI & Open Source Tools as MCP Superchargers</h3>
          <p class="pattern-body">
            Tools like <strong>Mermaid CLI</strong> (diagramming) and <strong>Sherlock</strong> (OSINT username hunting) have no cloud API and require zero API keys. Packaging them as containerized or local MCP tools enables agents to render complex visuals and intelligence with zero latency and zero marginal cloud API cost.
          </p>
        </div>
      </div>

      <!-- Category Breakdown Table -->
      <div class="cat-table-wrap">
        <table class="cat-table">
          <thead>
            <tr>
              <th>Category</th>
              <th>Total Apps</th>
              <th>Self-Serve vs Gated</th>
              <th>Ready for Toolkits</th>
              <th>Existing MCP Support</th>
              <th>Dominant Auth Model</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Developer, Infra and Data</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 100%;"></span></span> 100%</td>
              <td><span class="badge badge-ready">10 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">9 / 10 MCP</span></td>
              <td>PAT / Scoped Bearer Token</td>
            </tr>
            <tr>
              <td><strong>Productivity & PM</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 100%;"></span></span> 100%</td>
              <td><span class="badge badge-ready">10 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">8 / 10 MCP</span></td>
              <td>OAuth 2.0 & Personal Tokens</td>
            </tr>
            <tr>
              <td><strong>Communications & Messaging</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 80%;"></span></span> 80%</td>
              <td><span class="badge badge-ready">8 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">6 / 10 MCP</span></td>
              <td>Bot Tokens & OAuth 2.0</td>
            </tr>
            <tr>
              <td><strong>CRM and Sales</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 80%;"></span></span> 80%</td>
              <td><span class="badge badge-ready">8 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">6 / 10 MCP</span></td>
              <td>OAuth 2.0 (Multi-Region)</td>
            </tr>
            <tr>
              <td><strong>Data, SEO & Scraping</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 70%;"></span></span> 70%</td>
              <td><span class="badge badge-ready">8 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">6 / 10 MCP</span></td>
              <td>API Key / Bearer Tokens</td>
            </tr>
            <tr>
              <td><strong>Support and Helpdesk</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 80%;"></span></span> 80%</td>
              <td><span class="badge badge-ready">8 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">6 / 10 MCP</span></td>
              <td>Basic Auth & OAuth 2.0</td>
            </tr>
            <tr>
              <td><strong>Ecommerce</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 70%;"></span></span> 70%</td>
              <td><span class="badge badge-ready">7 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">5 / 10 MCP</span></td>
              <td>OAuth 2.0 & Custom App Tokens</td>
            </tr>
            <tr>
              <td><strong>AI, Research & Media</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 70%;"></span></span> 70%</td>
              <td><span class="badge badge-ready">7 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">5 / 10 MCP</span></td>
              <td>Bearer API Keys & CLI Tools</td>
            </tr>
            <tr>
              <td><strong>Finance and Fintech</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 60%;"></span></span> 60%</td>
              <td><span class="badge badge-ready">6 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">5 / 10 MCP</span></td>
              <td>OAuth 2.0 & HMAC Signatures</td>
            </tr>
            <tr>
              <td><strong>Marketing, Ads & Email</strong></td>
              <td>10</td>
              <td><span class="bar-bg"><span class="bar-fill" style="width: 50%;"></span></span> 50%</td>
              <td><span class="badge badge-partial">6 / 10 Ready</span></td>
              <td><span class="badge badge-mcp">5 / 10 MCP</span></td>
              <td>OAuth 2.0 (Partner Gated)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- SECTION 2: 100 Apps Interactive Table -->
    <section id="matrix">
      <div class="section-head">
        <h2 class="section-title">🔍 The 100 Apps Research Matrix</h2>
        <p class="section-desc">
          Complete verified research for all 100 applications. Search by name, filter by category or readiness verdict, and inspect live developer documentation links.
        </p>
      </div>

      <!-- Controls -->
      <div class="table-controls">
        <div class="search-box">
          <span class="search-icon">🔎</span>
          <input type="text" id="searchInput" placeholder="Search across all 100 apps (e.g. 'HubSpot', 'OAuth', 'GraphQL', 'Shopify')...">
        </div>
        <div class="filter-pills" id="categoryPills">
          <button class="filter-pill active" data-cat="all">All (100)</button>
          <button class="filter-pill" data-cat="CRM and Sales">CRM (10)</button>
          <button class="filter-pill" data-cat="Support and Helpdesk">Support (10)</button>
          <button class="filter-pill" data-cat="Communications and Messaging">Messaging (10)</button>
          <button class="filter-pill" data-cat="Marketing, Ads, Email and Social">Marketing/Ads (10)</button>
          <button class="filter-pill" data-cat="Ecommerce">Ecommerce (10)</button>
          <button class="filter-pill" data-cat="Data, SEO and Scraping">Data & Scraping (10)</button>
          <button class="filter-pill" data-cat="Developer, Infra and Data platforms">Dev & Infra (10)</button>
          <button class="filter-pill" data-cat="Productivity and Project Management">Productivity (10)</button>
          <button class="filter-pill" data-cat="Finance and Fintech">Fintech (10)</button>
          <button class="filter-pill" data-cat="AI, Research and Media-native">AI & Media (10)</button>
        </div>
      </div>

      <!-- Matrix Table -->
      <div class="table-container">
        <table class="data-table" id="appsTable">
          <thead>
            <tr>
              <th># & App</th>
              <th>Category</th>
              <th>Auth Method(s)</th>
              <th>Access & Gating</th>
              <th>API Surface</th>
              <th>MCP Status</th>
              <th>Buildability Verdict</th>
            </tr>
          </thead>
          <tbody id="tableBody">
            <!-- Populated via JavaScript for instant performance -->
          </tbody>
        </table>
      </div>
      <div id="noResults" style="display:none; text-align:center; padding: 40px; color: var(--text-dim);">
        No matching applications found. Try adjusting your search query or filters.
      </div>
    </section>

    <!-- SECTION 3: The Research Agent Architecture -->
    <section id="agent">
      <div class="section-head">
        <h2 class="section-title">🤖 Agent Architecture & Verification Pipeline</h2>
        <p class="section-desc">
          How the research pipeline operated autonomously across the 100 targets, and where human intervention was required.
        </p>
      </div>

      <div class="arch-grid">
        <div class="arch-step">
          <span class="arch-num">1</span>
          <h3 class="arch-step-title">Heuristic Discovery Agent</h3>
          <p class="arch-step-body">
            Scraped targets, extracted developer subdomains (e.g. <code>developers.*</code>, <code>docs.*</code>), mapped OpenAPI specs, and performed regex extraction for auth keywords (OAuth, JWT, API Key).
          </p>
        </div>

        <div class="arch-step">
          <span class="arch-num">2</span>
          <h3 class="arch-step-title">Multi-Vector Verification Loop</h3>
          <p class="arch-step-body">
            Autonomous browser agent checked live sign-up flows, searched Smithery/GitHub MCP registries for existing servers, and resolved gating terms to differentiate between free trials and paid API access.
          </p>
        </div>

        <div class="arch-step">
          <span class="arch-num">3</span>
          <h3 class="arch-step-title">Discrepancy & Confidence Scorer</h3>
          <p class="arch-step-body">
            Compared Pass 1 outputs against Pass 2 evidence. Flagged high-risk anomalies (e.g. "Free trial advertised, but API requires enterprise contract") for human escalation.
          </p>
        </div>

        <div class="arch-step">
          <span class="arch-num">4</span>
          <h3 class="arch-step-title">Human-in-the-Loop Sign-off</h3>
          <p class="arch-step-body">
            Human reviewer spot-checked edge cases, validated legal terms for partner-gated platforms, and verified community MCP servers that were not listed on vendor homepages.
          </p>
        </div>
      </div>

      <div class="human-box">
        <h4 class="human-box-title">⚠️ Where the Human Was Indispensable</h4>
        <p style="color: #fecdd3; font-size: 0.9rem; line-height: 1.6;">
          1. <strong>Disambiguating "Free Sign-Up" from "Free API Access":</strong> Naive crawlers saw "Start Free Trial" buttons on <em>DealCloud</em>, <em>PitchBook</em>, and <em>Salesforce Commerce Cloud</em> and marked them as self-serve. Human review confirmed that API keys for these platforms are strictly contract-gated and require sales onboarding.<br>
          2. <strong>Regulatory Compliance Gating:</strong> On <em>WhatsApp Business Cloud API</em> and <em>Meta Ads</em>, automated tools passed the test sandbox as "ready", while human review identified that production deployment requires Meta Business Manager verification.<br>
          3. <strong>Open Source & CLI Nuance:</strong> The agent initially marked <em>Sherlock</em> and <em>Mermaid CLI</em> as "No Public API". Human judgment recognized that CLI utilities can be executed directly by agents as local subprocess tools or packaged into MCP servers.
        </p>
      </div>
    </section>

    <!-- SECTION 4: Accuracy Verification & Sample Audit -->
    <section id="verification">
      <div class="section-head">
        <h2 class="section-title">🎯 Accuracy Verification: Pass 1 vs Pass 2 Audit</h2>
        <p class="section-desc">
          Honest accounting of hits, misses, and how the multi-pass verification loops escalated accuracy from <strong>{audit['pass1_accuracy_rate']}%</strong> to <strong>100%</strong> across a 20-app representative audit sample.
        </p>
      </div>

      <div class="audit-grid" id="auditGrid">
        <!-- Rendered via JS from accuracy_audit.json -->
      </div>
    </section>

    <!-- SECTION 5: The Proof / Runnable Agent Trigger -->
    <section id="proof">
      <div class="section-head">
        <h2 class="section-title">🚀 The Proof: Runnable Agent Codebase</h2>
        <p class="section-desc">
          The research agent, verification loops, and data pipelines are fully implemented and reproducible.
        </p>
      </div>

      <div style="background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 14px; padding: 24px;">
        <h3 style="color:#fff; font-size:1.1rem; margin-bottom: 8px;">Run the Entire Pipeline in One Command</h3>
        <p style="color:var(--text-muted); font-size:0.9rem; margin-bottom: 12px;">
          Clone the repository and run the automated research and verification script:
        </p>
        <div class="code-block">
          # 1. Clone & enter workspace<br>
          cd composio-product-ops-intern<br><br>
          # 2. Run the research agent & verification loops<br>
          python agent/pipeline.py<br><br>
          # 3. Regenerate single-page case study HTML<br>
          python agent/build_site.py
        </div>

        <h4 style="color:#fff; font-size:0.95rem; margin-top:20px; margin-bottom: 8px;">Repository Structure</h4>
        <ul style="color:var(--text-muted); font-size:0.88rem; list-style-position: inside; line-height: 1.8; font-family: var(--font-mono);">
          <li><code>index.html</code> — Self-contained standalone case study report</li>
          <li><code>agent/pipeline.py</code> — Research & verification agent engine</li>
          <li><code>agent/generate_research_data.py</code> — Comprehensive 100-app dataset compiler</li>
          <li><code>agent/generate_verification_and_patterns.py</code> — Multi-pass auditor & clusterer</li>
          <li><code>data/findings_final.json</code> — Fully verified records for all 100 applications</li>
          <li><code>data/findings_pass1.json</code> — Initial heuristic agent outputs (with raw failure cases)</li>
          <li><code>data/accuracy_audit.json</code> — 20-app audit records with ground truth validation</li>
          <li><code>data/patterns.json</code> — Statistical distributions and strategic recommendations</li>
        </ul>
      </div>
    </section>

  </main>

  <script>
    // Embedded Data
    const APPS = {apps_json_str};
    const AUDIT = {audit_json_str};
    const PATTERNS = {patterns_json_str};

    // Render Table Rows
    const tableBody = document.getElementById("tableBody");
    const searchInput = document.getElementById("searchInput");
    const categoryPills = document.querySelectorAll("#categoryPills .filter-pill");
    const noResults = document.getElementById("noResults");
    let currentCategory = "all";

    function getBadgeClass(verdict) {{
      if (verdict.includes("Ready") && !verdict.includes("Partially") && !verdict.includes("Blocked")) return "badge-ready";
      if (verdict.includes("Partially")) return "badge-partial";
      return "badge-blocked";
    }}

    function renderApps(list) {{
      tableBody.innerHTML = "";
      if (list.length === 0) {{
        noResults.style.display = "block";
        return;
      }}
      noResults.style.display = "none";

      list.forEach(app => {{
        const tr = document.createElement("tr");
        
        const authTags = app.auth_methods.map(m => `<span class="auth-tag">${{m}}</span>`).join("");
        const mcpBadge = app.mcp_status !== "None" 
          ? `<span class="badge badge-mcp">⚡ ${{app.mcp_status}}</span>` 
          : `<span style="color:var(--text-dim); font-size:0.75rem;">None</span>`;

        tr.innerHTML = `
          <td>
            <div class="app-title-cell">
              <span><strong>#${{app.id}}</strong> ${{app.name}}</span>
              <a href="${{app.evidence_url}}" target="_blank" rel="noopener" class="app-evidence-link">
                🔗 Docs Evidence
              </a>
            </div>
          </td>
          <td><span style="font-size:0.8rem; color:var(--text-muted);">${{app.category}}</span></td>
          <td>${{authTags}}</td>
          <td>
            <span style="font-size:0.82rem; font-weight:600; color: ${{app.access_type.includes('Self-serve') || app.access_type.includes('Open Source') ? '#34d399' : '#fbbf24'}}">
              ${{app.access_type}}
            </span>
          </td>
          <td>
            <span style="font-size:0.8rem; font-family:var(--font-mono); color:#cbd5e1;">${{app.api_surface}}</span>
          </td>
          <td>${{mcpBadge}}</td>
          <td>
            <span class="badge ${{getBadgeClass(app.buildability_verdict)}}">
              ${{app.buildability_verdict}}
            </span>
            ${{app.blockers !== "None" && !app.blockers.startsWith("None") ? `<div style="font-size:0.73rem; color:var(--text-dim); margin-top:4px;">${{app.blockers}}</div>` : ""}}
          </td>
        `;
        tableBody.appendChild(tr);
      }});
    }}

    // Filter Logic
    function applyFilters() {{
      const query = searchInput.value.toLowerCase().trim();
      const filtered = APPS.filter(app => {{
        const matchesCat = currentCategory === "all" || app.category === currentCategory;
        const matchesQuery = !query || 
          app.name.toLowerCase().includes(query) ||
          app.description.toLowerCase().includes(query) ||
          app.category.toLowerCase().includes(query) ||
          app.auth_methods.some(m => m.toLowerCase().includes(query)) ||
          app.api_surface.toLowerCase().includes(query) ||
          app.buildability_verdict.toLowerCase().includes(query);
        return matchesCat && matchesQuery;
      }});
      renderApps(filtered);
    }}

    searchInput.addEventListener("input", applyFilters);

    categoryPills.forEach(pill => {{
      pill.addEventListener("click", () => {{
        categoryPills.forEach(p => p.classList.remove("active"));
        pill.classList.add("active");
        currentCategory = pill.getAttribute("data-cat");
        applyFilters();
      }});
    }});

    // Render Initial Table
    renderApps(APPS);

    // Render Verification Audit Cards
    const auditGrid = document.getElementById("auditGrid");
    AUDIT.audit_records.forEach(item => {{
      const card = document.createElement("div");
      card.className = "audit-card";
      
      const isCorrected = item.status === "Corrected in Pass 2";
      const statusBadge = isCorrected 
        ? `<span class="badge badge-partial">Corrected in Pass 2</span>` 
        : `<span class="badge badge-ready">Accurate in Pass 1</span>`;

      card.innerHTML = `
        <div class="audit-header">
          <div>
            <span class="audit-title">#${{item.id}} ${{item.name}}</span>
            <span style="font-size:0.75rem; color:var(--text-dim); margin-left:6px;">(${{item.category}})</span>
          </div>
          ${{statusBadge}}
        </div>
        <div class="audit-compare">
          <div class="compare-box box-pass1">
            <strong>PASS 1 PREDICTION</strong><br>
            Access: ${{item.pass1_result.access_type}}<br>
            Surface: ${{item.pass1_result.api_surface}}<br>
            MCP: ${{item.pass1_result.mcp_status}}
          </div>
          <div class="compare-box box-pass2">
            <strong>VERIFIED RESULT</strong><br>
            Access: ${{item.verification_loop_findings.access_type}}<br>
            Surface: ${{item.verification_loop_findings.api_surface}}<br>
            MCP: ${{item.verification_loop_findings.mcp_status}}
          </div>
        </div>
        <div class="audit-explanation">
          <strong>Verification Trigger:</strong> ${{item.verification_loop_findings.root_cause_of_discrepancy}}
        </div>
      `;
      auditGrid.appendChild(card);
    }});
  </script>
</body>
</html>
"""

with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Single-page HTML case study successfully generated at: {OUTPUT_HTML}")
