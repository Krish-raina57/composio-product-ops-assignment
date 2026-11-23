"""
Composio AI Product Ops Intern Assessment
-----------------------------------------
Automated Research Pipeline, Multi-Pass Verification Loop,
and Case Study Generator.
"""

import json
import os
import sys
import subprocess
from collections import Counter

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENT_DIR = os.path.join(PROJECT_ROOT, "agent")
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

def log(msg, symbol="ℹ️"):
    print(f"[{symbol}] {msg}")

def run_step(script_name, description):
    script_path = os.path.join(AGENT_DIR, script_name)
    log(f"Running: {description} ({script_name})...", "⚙️")
    res = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error executing {script_name}:\n{res.stderr}")
        sys.exit(1)
    else:
        log(f"Completed {description}.", "✅")

def main():
    print("=" * 70)
    print("   COMPOSIO AI PRODUCT OPS RESEARCH & VERIFICATION AGENT PIPELINE")
    print("=" * 70)

    # 1. Compile 100 Apps Dataset (Pass 2 Ground Truth)
    run_step("generate_research_data.py", "Stage 1: Deep App Documentation & Verification Dataset")

    # 2. Generate Pass 1 Heuristics, Audit Sample, and Statistical Clusters
    run_step("generate_verification_and_patterns.py", "Stage 2: Pass 1 Simulation & Verification Loop Audit")

    # 3. Build Standalone Interactive HTML Case Study
    run_step("build_site.py", "Stage 3: Build Standalone Single-Page Case Study HTML")

    # Load summary stats
    with open(os.path.join(DATA_DIR, "accuracy_audit.json"), "r", encoding="utf-8") as f:
        audit = json.load(f)
    with open(os.path.join(DATA_DIR, "patterns.json"), "r", encoding="utf-8") as f:
        patterns = json.load(f)

    print("\n" + "=" * 70)
    print("   PIPELINE EXECUTION SUMMARY")
    print("=" * 70)
    print(f"Total Target Apps Researched:   {patterns['total_apps']}")
    print(f"Pass 1 Heuristic Accuracy:      {audit['pass1_accuracy_rate']}%")
    print(f"Pass 2 Post-Verification Gain:  {audit['pass2_verification_accuracy_rate']}%")
    print(f"Ready for Instant Toolkits:     {patterns['buildability_distribution'].get('Ready', 0)} / 100")
    print(f"Dual-Auth Support (OAuth+Key):  {patterns['auth_distribution'].get('Dual (OAuth2 + API Key / PAT)', 0)} / 100")
    print(f"Single-Page Case Study:         {os.path.join(PROJECT_ROOT, 'index.html')}")
    print("=" * 70)
    print("Pipeline finished successfully! You can now open index.html or deploy to GitHub Pages.")

if __name__ == "__main__":
    main()
