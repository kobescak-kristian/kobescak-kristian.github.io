# ADR-001 — Single static file hosted on GitHub Pages

**Status:** Accepted — 2026-07-07

## Context

A personal site is needed as a portfolio entry point for recruiters and
hiring managers. Options considered: static site generator, JavaScript
framework with build pipeline, paid hosting, or a single hand-written
static file on GitHub Pages.

## Decision

One `index.html` containing all markup, CSS, and JavaScript, deployed via
GitHub Pages from the `main` branch root. No build step, no dependencies,
no analytics.

## Consequences

- Zero hosting cost; deploy = git push; the full site history is auditable
  in git.
- No server-side capability — acceptable, the site is informational.
- All page claims must be maintained by hand; repository facts shown on the
  page (commit hashes, audit date) reflect the last manual audit, and a
  future automation may refresh mechanical facts only.
- One section ships commented out until its target repository is public;
  enabling it is a deliberate future commit, not an oversight.

## Verification

Post-deploy check: `curl -s -o /dev/null -w "%{http_code}" -L
https://kobescak-kristian.github.io` returns 200, plus a manual render
check on a device that never had the local file.
