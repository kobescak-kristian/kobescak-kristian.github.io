# STATE — kobescak-kristian.github.io

**Classification:** PROJECT · T0 (static public portfolio site, served from GitHub Pages — `AGENTS.md`; `domains/github-ops/CONVENTIONS.md` PROJECT/SYSTEM/EXPERIMENT taxonomy).

**RECONSTRUCTED** (GOVERNANCE.md Build-repo STATE rule, clause 7): derived from git history at scaffold time (2026-09-19), not written contemporaneously. Reconstructed entries are retrospective evidence, not contemporaneous record — the commit that adds this file begins the contemporaneous record going forward.

## Current state

Live static site (`index.html` + `case-studies/`), three case studies shipped (AI Reliability Engine, AI Context Engine's failed-gate run, AI Impact Scoring Engine's ledger reconciliation), one decision record (`adr/ADR-001-static-single-file-on-github-pages.md`).

The homepage runs systems → reference architecture → method → experience. `ai-portfolio-sentinel` leads as portfolio/hiring flagship with its bounded status ("in development toward production-ready"); the featured set is the six systems of the governance repository's ADR-2026-09-21 §4, in that order. The original five-engine diagram is retained only as a labelled reference architecture and is explicitly not presented as one integrated runtime. `ai-reliability-engine` remains a linked case study and is not labelled flagship on any site surface; `ai-decision-engine` remains linked. The Tier-1 documentation flagship designation is unaffected by anything on this site — it lives in `ARTIFACT_STANDARD.md` and still sits on `ai-reliability-engine`.

## Build history (from `git log --reverse`, oldest → newest)

- **2026-07-07** (`284a73f`, `1d64fa7`) — Site v1 shipped (content from an evidence-passed landing-page draft, agent block gated); Tier 0 artifacts added (README, ADR-001).
- **2026-07-08** (`8e60684`, `726b9d7`, `96edc8e`) — Flagship case study with evidence-backed stats and OG image, verified-at chip labels; Google Search Console verification token; case study #2 (AI Context Engine's failed-gate run) published.
- **2026-07-10** (`25157dc`) — Agent card shipped once the repo went public and its link was verified.
- **2026-07-11** (`d86f418`) — CLAUDE.md: session boot + publish-gate discipline.
- **2026-07-13** (`c6bc5ab`, `5bbd54c`) — Automation work section streamlined; engagement-availability note added.
- **2026-07-14** (`c06c187`, `1139ab8`) — Dead PDF-pipeline card removed; AI Compliance Orchestrator card shipped with honest-FAIL framing (gate run `gate-9328e564`).
- **2026-07-20** (`a4c9f06`) — Case study #3 (AI Impact Scoring Engine's ledger reconciliation) published, pinned at `b127fc4`.
- **2026-07-24** (`69ae28e`) — Canonical pre-commit local-path guard added.
- **2026-08-03** (`82f19ab`) — Publish-gate coverage canary added.
- **2026-08-04** (`8f786e2`, `bf1fbe6`, `5439d8d`) — Internal references redacted (entry-exact allowlist); Apache-2.0 license added; pre-push hook installed with the validator call left disabled ("no validator yet" — accurate at the time, no local validator file existed until the next entry).
- **2026-09-16** (`de66cad`) — Canonical AGENTS.md router adopted; this is also when `.githooks/validate_artifacts.py` was first added — the pre-push comment from `5439d8d` was not revisited at that point.
- **2026-09-19** (`5078243`) — STATE.md added (this file); validator gains a STATE.md-existence check; the pre-push validator call, dormant since before the validator file existed, is enabled.
- **2026-09-22** (this commit) — `portfolio-site-refresh-a`: site brought into line with the governance repository's ADR-2026-09-21 (portfolio positioning and flagship separation). Sentinel leads as portfolio flagship with bounded status; six-system featured hierarchy adopted; the "one decision system, five engines / not five demos — one pipeline" framing removed and the diagram relabelled as reference architecture; metadata, hero and method copy rewritten off the adopted positioning, dropping the portfolio-wide wording retired in the marketing record the same week; the 2026-07-07 page-audit PASS badge replaced with neutral dated wording; Reliability-specific hero stats folded back into the Reliability card; the five engine hash chips relabelled as dated July audit anchors rather than current HEADs; the claim-verification card now states that its published evaluation is confounded by case-name hints and does not present its scores as blind accuracy evidence.

## Open loops

None. The previously open sixth-repository dark card was already discharged in build history — the claim-verification agent card shipped `25157dc` (2026-07-10) and the compliance orchestrator card shipped `1139ab8` (2026-07-14). Only the README's "ships dark" note lagged; it is removed in the 2026-09-22 commit.
