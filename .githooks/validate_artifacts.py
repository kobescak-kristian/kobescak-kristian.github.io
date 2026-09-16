#!/usr/bin/env python3
"""Validate this repository against ARTIFACT_STANDARD.md Tier 0.

Site-compatible variant for a static GitHub Pages repository whose README
deliberately does not use the engine-specific section schema. It enforces
the Tier 0 checks appropriate to this repository plus the v2.7 AGENTS.md
requirement. It is not the canonical fleet validator; broader convergence
is separate work.

Exit 1 = violations printed. Exit 0 = "Tier 0: PASS".
"""
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")

# Legacy eight-name list, unexpanded on purpose: expanding it is fleet
# convergence work, not a check this repository already satisfies.
BANNED_WITHOUT_TRIGGER = ["SYSTEM_WALKTHROUGH.md", "CHANGELOG.md", "RUNBOOK.md",
                          "PRODUCTION_READINESS.md", "THREAT_MODEL.md", "MONITORING.md",
                          "INCIDENT_RESPONSE.md", "TEST_MATRIX.md"]
errors = []

# README: required to exist. The engine section headings (Problem /
# Solution / System / Outcome / Version Log) are deliberately NOT
# required here -- this site's README describes a static site, and
# imposing engine headings would turn artifact validation into an
# unrelated documentation rewrite.
readme = ROOT / "README.md"
if not readme.exists():
    errors.append("README.md missing")

# AGENTS.md (ARTIFACT_STANDARD v2.7, Tier 0): root file + required H2
# headings. Match is case-insensitive; "&" is accepted for "and". The
# optional "## Repository landmarks" section is not checked.
AGENTS_REQUIRED_HEADINGS = ["Repository purpose", "Authority and conflict handling",
                            "Task routing", "Always-on constraints", "Verification"]
agents = ROOT / "AGENTS.md"
if not agents.exists():
    errors.append("AGENTS.md missing (ARTIFACT_STANDARD v2.7 Tier 0)")
else:
    agents_text = agents.read_text(encoding="utf-8")
    for heading in AGENTS_REQUIRED_HEADINGS:
        words = [r"(?:and|&)" if w == "and" else re.escape(w) for w in heading.split()]
        pattern = r"^##\s+" + r"\s+".join(words) + r"\s*$"
        if not re.search(pattern, agents_text, re.I | re.M):
            errors.append(f"AGENTS.md missing section: ## {heading}")

# Decision-record requirement: adr/ and decisions/ both satisfy it -- a
# repo may use either name for its decision-record folder. At least one
# non-template record is required; there is no hard maximum.
adr = ROOT / "adr"
decisions = ROOT / "decisions"
decision_dirs = [d for d in (adr, decisions) if d.is_dir()]
if not decision_dirs:
    errors.append("adr/ (or decisions/) folder missing")
else:
    decision_files = [f for d in decision_dirs for f in d.glob("*.md")
                      if "template" not in f.name.lower()]
    if len(decision_files) == 0:
        errors.append("adr/ (or decisions/) has no decisions (need at least 1)")

for banned in BANNED_WITHOUT_TRIGGER:
    if (ROOT / banned).exists():
        # allowed only if a decision-record file mentions it (the trigger record)
        justified = any(
            re.search(re.escape(banned), f.read_text(encoding="utf-8"))
            for d in decision_dirs for f in d.glob("*.md"))
        if not justified:
            errors.append(f"{banned} exists without an ADR/decision record citing its trigger")

if errors:
    print("ARTIFACT_STANDARD violations:")
    for e in errors:
        print(f"  - {e}")
    sys.exit(1)
print("Tier 0: PASS")
