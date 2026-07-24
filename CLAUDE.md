# kobescak-kristian.github.io

Public portfolio site. Every claim on these pages is evidence:
numbers trace to committed files in the public repos, case studies
are hash-pinned to specific commits.

## Session boot and governance (applies to every session here)
- Governance home: kristian-os (PRINCIPLES -> GOVERNANCE ->
  FAILURE_REGISTER). Read before any irreversible action.
- PUBLISH GATE: no push to this repo without a FULL
  repo-publish-gate run on the final diff (secrets history-wide,
  private-leak scan, eval-claim cross-check against source repos
  at HEAD, structure/10-second test, anti-patterns, link check).
  A re-run is required after ANY in-window fix; scoped runs are
  not accepted.
- Claims discipline: a number appears on this site only if it
  matches a committed file in a public repo at its pinned HEAD.
  No approximation, no rounding up, no unsourced figures.
- Post-push verification: Pages build confirmed bound to the new
  commit; changed pages 200 logged-out; served HTML carries the
  new content (not a cached hit).
- Before any write: environment fingerprint (pwd + git config
  user.email; /home/user/ or noreply@anthropic.com = cloud
  sandbox = read-only, no pen). Pen check on main at open AND
  pre-commit.
- Never write absolute local paths into tracked files —
  machine-specific values go to the gitignored local config.
- Evidence: case-study pages pin engine commits by hash. NO
  history rewrites, ever — here or in any pinned repo.
- Close ritual: commit -> push origin main -> verify
  origin/main..HEAD empty -> report verbatim.
- Work comes from the governance repo's queue (kristian-os,
  FABLE_QUEUE) and the webpage queue in its github-ops STATE;
  do not invent tasks.
