# STATE — kobescak-kristian.github.io

**Classification:** PROJECT · T0 (static public portfolio site, served from GitHub Pages — `AGENTS.md`; `domains/github-ops/CONVENTIONS.md` PROJECT/SYSTEM/EXPERIMENT taxonomy).

**RECONSTRUCTED** (GOVERNANCE.md Build-repo STATE rule, clause 7): derived from git history at scaffold time (2026-09-19, Q-72(f)), not written contemporaneously. Reconstructed entries are retrospective evidence, not contemporaneous record — the commit that adds this file begins the contemporaneous record going forward.

## Current state

Live static site (`index.html` + `case-studies/`), three case studies shipped (flagship, AI Context Engine's failed-gate run, AI Impact Scoring Engine's ledger reconciliation), one decision record (`adr/ADR-001-static-single-file-on-github-pages.md`). One card (a sixth repository) ships dark, pending that repo's publication and link verification (README, "How it updates").

## Build history (from `git log --reverse`, oldest → newest)

- **2026-07-07** (`284a73f`, `1d64fa7`) — Site v1 shipped (content from an evidence-passed landing-page draft, agent block gated); Tier 0 artifacts added (README, ADR-001).
- **2026-07-08** (`8e60684`, `726b9d7`, `96edc8e`) — Flagship case study with evidence-backed stats and OG image, verified-at chip labels; Google Search Console verification token; case study #2 (AI Context Engine's failed-gate run) published.
- **2026-07-10** (`25157dc`) — Agent card shipped once the repo went public and its link was verified.
- **2026-07-11** (`d86f418`) — CLAUDE.md: session boot + publish-gate discipline.
- **2026-07-13** (`c6bc5ab`, `5bbd54c`) — Automation work section streamlined; engagement-availability note added.
- **2026-07-14** (`c06c187`, `1139ab8`) — Dead PDF-pipeline card removed; AI Compliance Orchestrator card shipped with honest-FAIL framing (gate run `gate-9328e564`).
- **2026-07-20** (`a4c9f06`) — Case study #3 (AI Impact Scoring Engine's ledger reconciliation) published, pinned at `b127fc4`.
- **2026-07-24** (`69ae28e`) — Canonical pre-commit local-path guard added (Q-48 wave 1).
- **2026-08-03** (`82f19ab`) — Publish-gate coverage canary added.
- **2026-08-04** (`8f786e2`, `bf1fbe6`, `5439d8d`) — Internal references redacted (entry-exact allowlist); Apache-2.0 license added; Q-35 pre-push hook installed with the validator call left disabled ("no validator yet" — accurate at the time, no local validator file existed until the next entry).
- **2026-09-16** (`de66cad`) — Canonical AGENTS.md router adopted (Q-93); this is also when `.githooks/validate_artifacts.py` was first added — the pre-push comment from `5439d8d` was not revisited at that point.
- **2026-09-19** (this commit) — Q-72(f): STATE.md added (this file); validator gains a STATE.md-existence check; the pre-push validator call, dormant since before the validator file existed, is enabled.

## Open loops

The sixth, still-dark repository card — held until that repo is public and its link independently verified, per README's own stated update rule.
