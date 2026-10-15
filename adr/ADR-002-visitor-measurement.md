# ADR-002 - Visitor measurement on the site

**Status:** Accepted (2026-10-16). The owner chose option B on
2026-10-16 and accepts the residual legal risk described in Context.
The repository checks under Verification passed at acceptance; the
live checks run after deployment and are recorded in `STATE.md`.

**Date:** 2026-10-16
**Author:** Kristian Kobescak (drafted with Claude Code)

## Context

The site has measured nothing since launch. ADR-001 decided "no
analytics", and `README.md` and `AGENTS.md` repeat that. The owner now
wants to know whether the site is visited: how many visits, which pages,
and where visitors come from (for example LinkedIn or a job
application). Changing this is a material architecture change, so
`AGENTS.md` requires a decision record first.

What is already in place: the site is verified in Google Search
Console (`google2a649f63aff332b7.html`, 2026-07-08). That reports
Google search impressions and clicks, with no code on the pages. It
does not see visits that arrive from LinkedIn, email or a CV link,
which is most of the traffic a portfolio site gets.

GitHub Pages gives no access to server logs, so log-based counting is
not possible. Any visit counting must run in the visitor's browser.

### Legal position (checked 2026-10-15)

Facts:

- EU rule: Article 5(3) of the ePrivacy Directive. Storing or reading
  information on a visitor's device needs consent, unless it is
  strictly necessary for the service the visitor asked for. Malta
  applies this through S.L. 586.01, regulation 5.
- The EDPB's Guidelines 2/2023 on the technical scope of Article 5(3)
  (version 2.0, adopted 7 October 2024) say the rule is not limited to
  cookies. A JavaScript snippet that makes the browser send information
  back is in scope (paragraphs 32 and 33), and so is a tracking pixel
  (paragraph 51). Paragraph 56 adds that being in scope does not always
  mean consent is needed; an exemption may apply case by case.
- Analytics is not on the list of exemptions in the current law. The
  Malta regulator's cookie guidance (August 2021) is about tracking and
  advertising cookies. No Maltese exemption for visit counting was
  found.
- The EU "Digital Omnibus" proposal (November 2025) would add a
  consent-free exemption for aggregated audience measurement. As of
  October 2026 it is still a proposal, its wording is still changing,
  and it is not law.
- Plausible states that its customers do not need cookie banners.
  GoatCounter states only that it "probably" needs no GDPR consent
  notice, and says nothing about the ePrivacy rule. Both are the
  vendors' readings, not a regulator's ruling.

Inference: a cookieless, aggregate-only counter on a personal site is
low-risk in practice, and many EU sites run one without a banner. It is
still not clearly compliant under the strict reading above. This
matters more than usual here, because the site presents the owner's
work on AI evaluation and governance, and it states its own limits
honestly.

## Decision

Count visits with GoatCounter's hosted service, cookieless and
aggregate-only, on every public page, without a consent banner, with a
short plain note in each page footer that names the tool and says what
it records (option B below, chosen by the owner on 2026-10-16).

The counts are a lower bound, not a complete total: visitors whose ad
blocker or browser blocks GoatCounter are not counted.

## Options compared

| Option | What it measures | Consent banner | Cost | Fit with ADR-001 |
|---|---|---|---|---|
| A. No page code: Search Console only | Google search clicks only | Not needed | Free | Unchanged |
| B. GoatCounter, no banner (chosen) | Visits, pages, referrers, country, device type | Not used; residual legal risk accepted | Free for reasonable use | One script tag per page |
| C. GoatCounter behind an opt-in prompt | Same as B, for visitors who accept | Yes, before the script loads | Free | Script plus prompt code per page |
| D. Plausible, no banner | Same as B, plus engagement | Not used; same residual risk as B | From 9 USD a month after a 30-day trial | One script tag per page |
| E. Cloudflare Web Analytics | Visits, pages, referrers, performance | Not used; same residual risk as B | Free | One script tag per page |
| F. Google Analytics 4 | Full behaviour analytics | Required (cookies) | Free | Script plus consent tool |

## Alternatives rejected

- **A. Search Console only.** Free of all risk, but it does not answer
  the owner's question. Visits from LinkedIn, email and CV links are
  invisible to it. It stays in place under every option.
- **C. Opt-in prompt.** The cleanest legal position. Rejected as the
  default because many visitors refuse or ignore prompts, so the counts
  become unreliable, and the prompt adds interface code to a site built
  to have none. Choose C if the owner does not accept the residual
  risk described in Context.
- **D. Plausible.** Comparable privacy design (daily-rotated hash, no
  cookies, EU-hosted), but it costs money and adds an account to pay
  for. Its extra features are not needed for a portfolio site.
- **E. Cloudflare Web Analytics.** Free, but a US company, and its
  documentation of the beacon is mainly about page performance. It
  offers nothing for this site that GoatCounter does not, at no
  lower risk.
- **F. Google Analytics 4.** Sets cookies, so it needs a consent tool,
  and it sends data to a US advertising company. Out of proportion for
  a personal site.
- **Self-hosted counter (Umami, GoatCounter).** Needs a server, which
  ADR-001 rules out.

## Consequences

- One GoatCounter script tag is added to `index.html` and to each page
  in `case-studies/`. The site gains its first third-party request.
- GoatCounter (per its privacy policy, checked 2026-10-15) keeps no
  cookies or browser storage, holds IP plus browser string in memory
  for at most 8 hours only to avoid counting a repeat visit twice, and
  stores data on Hetzner servers in Finland and Germany. These are the
  vendor's statements, not verified by this repository.
- Each page footer gains one plain line naming GoatCounter, saying
  what it does not record, and linking to GoatCounter's privacy policy.
  This is a minimal notice: the visitor's IP address passes through the
  service, and GDPR Article 13 lists more items (purpose, legal basis,
  retention, rights) than the line states.
- The residual legal risk in Context is accepted by the owner, in
  writing, by this record.
- The GoatCounter setting "collect individual pageviews" stays off
  (the default). With it on, GoatCounter stores a random session ID per
  visit, and the footer claim "no visitor profiles" would need review.
- Public text must change in the same pull request: `README.md`
  ("no tracking"), `AGENTS.md` (repository purpose and always-on
  constraints) and the status line of ADR-001, which gets a pointer
  saying its "no analytics" clause is replaced by this record. ADR-001's
  decision text is not edited.
- Per-application links (for example `?campaign=<company>` added to
  the homepage URL in a CV) appear in the GoatCounter campaigns view.
  This shows that a link given to one organisation was opened, not who
  opened it.
- The service is run by one person and offered free. If it stops, the
  site loses counting but nothing else breaks.

## Verification

At acceptance (repository, 2026-10-16), both commands return 1 for
each of the 9 public pages (`index.html` and the 8 files in
`case-studies/`):

- `grep -c "gc.zgo.at/count.js" index.html case-studies/*.html`
  (the counter script);
- `grep -c "THIS SITE COUNTS VISITS WITH" index.html case-studies/*.html`
  (the footer note).

After deployment (live site, recorded in `STATE.md`):

- a visit shows in the GoatCounter dashboard;
- browser developer tools show no cookie and no localStorage or
  sessionStorage entry set by the counter.

## Review

Reopen when any of these happens:

- the Digital Omnibus is adopted (an exemption may make B clearly
  compliant), or the EDPB or the Malta regulator publishes guidance on
  visit counting;
- any complaint or regulator contact about the site;
- GoatCounter changes its data handling or stops its free service;
- in any case, review by 2027-10-16.
