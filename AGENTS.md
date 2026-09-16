# AGENTS.md — kobescak-kristian.github.io

Tool-neutral context router for coding agents working in this repository.
It points to where repository truth lives. It is not evidence of what the
site currently publishes, and not a record of any claim's current value:
cite the source it routes to, never this file.

## Repository purpose

`kobescak-kristian.github.io` is Kristian Kobescak's static public
portfolio site, served from GitHub Pages. It presents the portfolio and
system narrative, repository-backed claims about the public AI systems,
selected case studies, operating background and positioning, and links to
the public evidence behind each claim.

The site is intentionally static: no application framework, no package
manager or build step, no dependency layer, no server-side component, and
no analytics or tracking. Deployment is the committed static files served
by GitHub Pages. Human overview: `README.md`.

Metrics, engine scores, record and failure counts, pinned commit hashes,
audit dates, role and location text, case-study count and publication
status are mutable public content. They live in the HTML, in `README.md`
and in the external source repositories, and are deliberately not
restated here.

## Authority and conflict handling

| Question | Canonical source |
|---|---|
| Repository-level description, static-site model, content and evidence rule, structure, update method | `README.md` |
| Live homepage content, published narrative, displayed claims, links, page metadata, styling, client-side behaviour | `index.html` |
| A public case-study narrative and its page-specific claims and evidence | the relevant `case-studies/*.html` |
| Architecture and deployment decision for the site | `adr/ADR-001-static-single-file-on-github-pages.md` |
| Claude session mechanics for this repository | `CLAUDE.md` |
| Machine-local absolute path guard at write time | `.githooks/pre-commit` |
| Push freshness guard | `.githooks/pre-push` |
| Adjudicated, entry-exact publication exceptions | `.publicgate-allow` |
| The technical fact behind a repository claim shown on the site | the linked public source repository at its cited commit |
| Licence terms | `LICENSE` |

When sources disagree:

- The accepted decision record governs the static-site architecture and
  deployment decision it records.
- `README.md` owns the repository-level description and rules.
- The HTML owns what is actually published.
- The external public source repositories own the technical facts the
  site claims about them.
- If a page and its cited or pinned evidence disagree, that is a claim
  defect. Do not change the evidence to fit the page, and do not round or
  reinterpret the claim to fit the evidence.
- If the requested task materially depends on an unresolved
  disagreement, surface it and stop for owner review.

## Task routing

These are starting points, not exhaustive reading lists.

| Task class | Start here |
|---|---|
| Repository purpose, static-site structure, update method | `README.md` |
| Homepage content, public claims, search and social metadata, layout, styling, client-side interaction | `index.html` |
| Case-study content | `case-studies/*.html` |
| Static-site architecture or deployment decision | `adr/ADR-001-static-single-file-on-github-pages.md` |
| Evidence behind a repository claim | the linked or pinned public source repository, read together with the site HTML that makes the claim |
| Publication exception for an otherwise-blocked line | `.publicgate-allow` |
| Machine-local path guard | `.githooks/pre-commit` |
| Push freshness | `.githooks/pre-push` |
| Artifact validation | `.githooks/validate_artifacts.py` |
| Licence | `LICENSE` |

## Always-on constraints

- The static architecture is deliberate. Do not introduce a framework,
  build pipeline, package manager, dependency layer, server-side
  component, analytics or tracking as unrelated work. A material
  architecture change requires an authorized decision recorded in `adr/`.
- Repository and technical claims displayed on the site must trace to
  committed, publicly inspectable evidence. Do not invent, approximate,
  round upward or otherwise improve a number because it reads better.
- Site content and source evidence are different authorities. The HTML
  owns what the site says; the linked source repository owns the
  technical fact being claimed. When they disagree, the site claim is
  stale or wrong. Never rewrite source evidence to rescue a page.
- Pinned evidence must stay traceable. Case studies and homepage claims
  cite commit hashes and other evidence anchors; do not casually replace,
  re-point or reinterpret one.
- Never rewrite pushed history. The site and its case studies depend on
  hash-stable public repositories and on this repository's auditable
  history. No amend, rebase or force-push of already-pushed commits.
- Every push to this repository runs the full repository publish gate
  against the final staged diff first. A scoped or private-leak-only scan
  is not a substitute. If an in-window fix changes the staged publication
  diff, rerun the gate.
- No credentials, private operational data, machine-local absolute paths
  or private internal documentation content may be newly introduced into
  public files. The existing exceptions are exact entries in
  `.publicgate-allow`; do not broaden them casually.
- Any edit that changes a factual repository or system claim must be
  re-derived from the authoritative public source before publication, not
  from memory and not from an earlier value on the page.
- Work-history claims are not repository-evidence claims. This repository
  keeps the two apart: technical claims backed by public repositories,
  and career facts maintained as career facts. Do not label career prose
  as repository-verified technical evidence.
- Case-study pages are public evidence surfaces. A change must preserve
  evidence traceability and scope-honest claims; do not silently sanitize
  a recorded failure or a declared limitation.
- Post-push verification is part of a site-content change: the deployed
  site resolves, changed public pages resolve logged out, and the served
  content reflects the pushed commit rather than only the local file. A
  push alone does not complete a site-content change. For a
  documentation-only change where no served page changes, verify instead
  that Pages remains healthy and that the pushed file is publicly
  readable; do not claim a content deployment that did not happen.
- Changing one surface does not authorize cleanup of another. Refreshing
  hashes, metrics, dates, links, wording, page design or positioning is
  separate work. A stale public claim found while doing something else is
  a finding to report, not a licence to edit.
- Decision records are created only for genuine material decisions and
  have no hard maximum. Documentation requirements written for the
  code-bearing repositories do not automatically apply to this site's
  `README.md`. If validator policy and this repository's structure
  disagree, surface the mismatch rather than reshaping unrelated
  artifacts to satisfy it.
- `AGENTS.md` is guidance, not enforcement. The git guards, the publish
  gate tooling, public-source verification and the deployment checks
  remain the enforcement.

## Verification

This site's architecture has no application build step. Routine
verification must use repository surfaces that actually exist for the
task; never fabricate a test, build or CI result.

Routine, safe, bounded checks:

```bash
python .githooks/validate_artifacts.py .
git diff --check
```

For publication-affecting work, additionally:

- the full repository publish gate against the final staged diff, rerun
  after any in-window fix;
- post-push public verification appropriate to the surface that changed,
  as described under Always-on constraints.
