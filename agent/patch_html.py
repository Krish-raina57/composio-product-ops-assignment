import re

path = 'C:/Users/krish/.gemini/antigravity/scratch/composio-product-ops-intern/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add prominent GitHub button to header
old_brand = '<span class="brand-badge">⚡ Composio AI Product Ops</span>'
new_brand = '''<span class="brand-badge">⚡ Composio AI Product Ops</span>
        <a href="https://github.com/Krish-raina57/composio-product-ops-assignment" target="_blank" class="nav-btn" style="background: #4f46e5; color: #fff; font-weight: 700; border-color: #6366f1; display: inline-flex; align-items: center; gap: 8px;">
          <span>⭐ GitHub Repository</span>
        </a>'''

html = html.replace(old_brand, new_brand, 1)

# 2. Add an explicit Banner right in the Hero Section
old_hero = '<p class="hero-subtitle">'
new_hero = '''<div style="background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.4); border-radius: 10px; padding: 14px 20px; margin-bottom: 22px; display: flex; flex-wrap: wrap; gap: 16px; align-items: center;">
        <span style="font-size: 0.9rem; color: #cbd5e1;"><strong>Candidate:</strong> Krish Raina (<a href="mailto:krishraina8472@gmail.com" style="color:#818cf8;">krishraina8472@gmail.com</a>)</span>
        <span style="color: rgba(255,255,255,0.3);">|</span>
        <a href="https://github.com/Krish-raina57/composio-product-ops-assignment" target="_blank" style="color: #38bdf8; font-weight: 700; text-decoration: underline; font-size: 0.9rem;">💻 View Source Code & Documentation on GitHub</a>
      </div>
      <p class="hero-subtitle">'''

html = html.replace(old_hero, new_hero, 1)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated index.html successfully with prominent header buttons and candidate banner!")
