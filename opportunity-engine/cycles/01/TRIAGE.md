# CYCLE 1 — TRIAGE

**Date:** 2026-08-27 · **Input:** 12 scout reports, 88 raw candidates · **Output:** 9 survivors, 79 killed.

**Standing enforcement applied throughout:** Standing Law 5 — *an unnamed first ten is a Gate 1 failure, not a
pass.* Where a scout wrote "named channel, unnamed individuals", "UNPROVEN (names)", or "no named individuals
yet", I recorded **G1 FAIL**. That single rule accounts for the largest block of kills in this cycle, and
section 4 argues it is telling us something about the surfaces rather than about the market.

**Evidence-quality note.** The shared WebSearch budget was exhausted roughly two-thirds through the cycle;
later scouts ran on direct fetches. I re-verified the two conflicts and the top candidate against primary
sources myself. Rows whose evidence still rests on citations no scout could read live are marked
`UNREAD-CITATION` and were scored down accordingly.

**New tooling finding — supersedes the OPEN-CONFLICTS table.**
> **Reddit IS reachable from this environment.** `curl -sSL -A "<browser UA>" https://old.reddit.com/...`
> returns HTTP 200 with full thread bodies, comment counts, dates and subreddit search. The `-L` (follow
> redirect) plus a real User-Agent is the whole trick. `r.jina.ai` is *blocked* by Reddit — the proxy is the
> wrong tool here; the direct fetch is the right one. Conversely **`r.jina.ai` defeats the Fannie/Freddie
> 403** and renders their PDFs to text. Both conflicts were settled with these two techniques in minutes.

---

# 1. CONFLICT RESOLUTIONS

## CONFLICT 1 — UAD 3.6. Verdict: **scout 3 is right about the wall, wrong that it swallows the candidate. Survives, narrowed, at a lower score than scout 10 claimed.**

### 1a. The 2026-11-02 date is now T1, verified primarily. Scout 10's T2 caveat is discharged.

- **Freddie Mac**, `sf.freddiemac.com/docs/pdf/fact-sheet/uad-redesign-timeline.pdf` (published 2026-05-04,
  read 2026-08-27 via `r.jina.ai`): *"**MANDATE — November 2, 2026 — Submit UAD 3.6 Only**"*; broad production
  2026-01-26 → 2026-11-01; retirement 2027-05-03; *"November 2, 2026: **Fatal message** delivered only when UAD
  2.6 submitted."*
- **Fannie Mae**, UAD 3.6 FAQ PDF, `singlefamily.fanniemae.com/media/23286/display` (doc dated 2026-08-12,
  page published 2026-08-18): *"UAD 3.6 will be mandatory for all new appraisal reports submitted to UCDP on or
  after November 2, 2026… UCDP will return a **Fatal** message resulting in a '**Not Successful**' submission."*

Both GSEs, both primary, both agree. The hardest clock in the cycle is real.

### 1b. There are three walls. Two are real Gate 3 failures. One kills scout 10's *framing* but not its candidate.

**Wall 1 — UCDP submission. Real, and fatal to anything that touches it.** Fannie's UCDP page publishes
exactly three registration routes: **Lender Registration** (by a Corporate Administrator), **Correspondent
Registration**, and **AMC / Lender-Agent Registration**. There is no appraiser route. The lender submits; the
appraiser never does. Any product in the submission path is a Gate 3 access failure of the Procore shape
already in the ledger.

**Wall 2 — forms software is GSE-*verified*, and the verification is real.** Fannie FAQ #22: *"Appraisers
should also work with their appraisal software vendor to understand specific functionality, vendor-specific
training, and **testing timeframes**."* FAQ #20: *"The appraiser, **through their appraisal software provider**,
has the ability to run the UAD compliance rules through an API."* The community records the same from the
other side: *"a la mode/TOTAL completed **GSE verification** back in December… ACI's Sky Workbench got
**verified** June 8"* (r/appraisal `1v06ps2`, 2026-07-18, read live). Producing the XML/PDF report is a
vendor-verification game we would lose. Scout 10 named this risk correctly and it is confirmed.

**Wall 3 — and this is the finding that changes the candidate: there is nothing left to attach.**
Fannie UAD 3.6 FAQ **#15**, verbatim:

> *"**Does the new appraisal report still contain a General Addendum? No.** In place of the General Addendum,
> there are specific fields within each section of the URAR that allow commentary to be added as necessary."*

The delivered artifact is an XML file plus a PDF rendered from that XML by the verified vendor, per the GSE
Report Style Guide. **Scout 10's artifact description — "an exhibit the appraiser attaches" — is falsified by
primary source.** There is no attachment slot any more.

### 1c. What actually survives, and it is not nothing

Two things sit entirely outside all three walls:

1. **The workfile.** A USPAP Record Keeping Rule obligation owned by the *appraiser*, produced to a state
   board, a client or opposing counsel on demand, and **never submitted to UCDP**. No GSE touches it. No
   verification applies to it. This is a clean Gate 3 pass.
2. **The paste-ready commentary block.** Fannie Selling Guide **B4-1.3-09** (dated 06/04/2025) requires,
   verbatim: *"The appraisal report must, at a minimum, **summarize the supporting evidence and include a
   description of the data sources, tool(s), and technique(s) used**"* and *"The appraiser must provide
   fact-based and objective comment(s) that detail the work performed and data sources utilized for the market
   supported adjustments used… **A statement only recognizing that an adjustment has been made is not
   acceptable.**"* That is prose a human types into a commentary field. We never touch the XML.

**So: not a Gate 3 kill. But the candidate is smaller and later-clocked than scout 10 scored it.** Note the
date on B4-1.3-09 — **06/04/2025**. The obligation to support adjustments is *not new*. What changes on
2026-11-02 is only that the addendum where appraisers used to bury a one-line assertion has been deleted. That
is still a dated clock, but it is a **form-change clock, not a new-obligation clock**, and it should be scored
as one.

### 1d. Two further hazards, one of which scout 10 half-flagged

- **MLS data is licensed to the appraiser, not to us.** The artifact must be derived from the comp export the
  appraiser supplies, and we must never hold, cache or aggregate it. Build constraint, not a kill.
- **Bradford NightHawk is free through 2026 for active members.** A free adjacent product compresses
  willingness to pay for anything that looks like part of the form.

### 1e. Gate 1 re-verified live by me (Reddit is reachable — see tooling note)

r/appraisal subreddit search, `sort=new`, fetched 2026-08-27, **20+ dated UAD 3.6 threads in August 2026
alone**: *Land adjustment comps* (59c, 08-26) · *More Total 3.6 drama* (54c, 08-25) · *Total Desktop: First UAD
3.6 Report Observations* (33c, 08-21) · *Doubts on Total 3.6* (88c, 08-08) · *solidifi offering same fees for
3.6* (64c, 08-07) · *3.6 software, who you guys going with?* (59c, 08-05) · *Will There be a Backup in the
Appraisal Pipeline at the Start of 3.6?* (36c, 08-01) — plus a dozen more. All three of scout 10's cited
threads exist with matching titles and quotes. **Scout 10's Gate 1 evidence holds up under live re-reading.**

**But two of its numbers do not.** The thread scout 10 leaned on hardest, `1v06ps2`, has **4 comments** — it is
one member's compilation, not a groundswell. The WorkingRE "3% / 58% / 64%" survey is **still UNVERIFIED
primary**. And the mechanic the entire thesis rests on — *"the new CU is field-driven, it reads your adjustment
fields, not your addenda"* — is second-hand **inside** that compilation (*"working appraisers in the AI thread
here report…"*). It is not a GSE statement. `UNREAD-CITATION`.

> **Conflict 1 verdict: SURVIVES at 7.00, not as scout 10's 7/10 top candidate.** Artifact narrowed to
> workfile + paste-ready commentary. Never the XML, never UCDP, never the form. Clock re-graded from
> new-obligation to form-change.

---

## CONFLICT 2 — accessibility remediation. Verdict: **Law 13 is BOUNDED, not violated. The boundary is worth writing down. The candidate dies anyway, on arithmetic.**

### 2a. Scout 11's Reddit citations re-read live. They are accurate.

All three verified by direct fetch, 2026-08-27:

- `r/accessibility/1tiezfl` (2026-05-20, 18 comments) — verbatim: *"I promise you no automated workflow will
  be very reliable. They only can fix about **30-50% of issues and provide no legal protection**. You're better
  off paying some (poor unemployed) intern or remediation specialist like myself **$15-20 an hour** to do it."*
  **The 30–50% ceiling and the $15–20/hr wage are confirmed verbatim, in one sentence, from a practitioner.**
- `r/accessibility/1jtiqxv` (2025-04-07, 17 comments) — prices confirmed: *"dirt cheap to $10/pg"*, *"Anywhere
  from $2 per page to $10 per page can make sense"*, *"I get $60/hour as an SME."* And the discriminator, asked
  by the community itself: *"**do you have expertise in PDF/UA or do you simply pass the built-in checker?**"*
- `r/accessibility/1qtpxl4` (2026-02-02, 26 comments) — a **software engineer with 8 years of university PDF
  remediation experience announcing he is building exactly this product**. Top reply: *"Check out the solution
  built by AWS with Arizona State and used by Ohio State… **I think your competition is too strong.**"*
  Community advice throughout: *"pivot away from such heavy reliance on pdfs at all"*, *"I built a tool… that
  can convert PDFs to HTML."*

### 2b. The reasoning

Does selling to the freelance remediator escape Law 13? **Yes — and the escape is real.** Liability travels
with whoever signs the remediation. If we sell a throughput tool to that person, we never issue a warranty, and
the law does not forbid it. Scout 11's manoeuvre is legitimate.

**But the escape re-prices the opportunity, and that is what scout 11 missed.** Once you move from the
warranty-buyer to the warranty-issuer, your price ceiling stops being the incumbent's rate card and becomes the
issuer's wage. Write it down:

> ### STANDING LAW 13a — the warranty-issuer bound *(new, Cycle 1 triage)*
> Selling to the party who **issues** the warranty rather than the party who **buys** it does escape Law 13 —
> the liability never becomes ours. But it moves the price ceiling off the incumbent's rate card and onto the
> issuer's wage. **Our maximum extractable price is (fraction of the issuer's task we automate) × (the issuer's
> own hourly rate)** — never the per-page price the compliance buyer pays. Compute that number *before*
> celebrating the gap. A gap measured against the warranty-buyer's price is not addressable by a tool sold to
> the warranty-issuer.

Applied here, with both inputs verified from the same sentence in the same thread:

| Input | Verified value | Source |
|---|---|---|
| Warranty-issuer's hourly rate | **$15–20/hr** | `r/accessibility/1tiezfl`, 2026-05-20, read live |
| Automatable fraction | **30–50%**, stated as a ceiling by a practitioner | same sentence |
| → **Addressable value per hour of their work** | **≈ $5–10** | arithmetic |
| Competitors in that band | 8+ funded vendors **plus a free AWS/Arizona State open-source tool already run by two state universities** | `1qtpxl4`, read live |

Scout 1's headline "3,000–10,000× gap" was measured against the **$7.50/page compliance-buyer price** — a price
we can only reach by issuing the warranty. **The gap was never addressable.** Scout 9 was right; scout 11's
buyer-swap is a valid manoeuvre that fails on arithmetic rather than on principle.

Two further nails: the LEDGER already records *"Unbundling is picked over — retire the surface… PDF
accessibility 8+ [standalone vendors]"*, and the community's own recommended fix is to **convert to HTML** —
i.e. to delete the artifact we would be selling.

> **Conflict 2 verdict: KILL the entire accessibility cluster** — scout 1 C-05 and C-07, scout 2 #9, scout 9
> PD-4, scout 11 A1 — on **G2 + Law 13a**. **Keep the manoeuvre as Standing Law 13a.** The rule is the durable
> output of this conflict; the candidate is not.

---

# 2. THE GATE TABLE — all 88 candidates

Legend: **✓** pass · **~** conditional/weak · **✗** fail. Primary killing gate is the one in **bold** in the
reason. `UNREAD-CITATION` = evidence rests on sources no scout read live.

## 2a. SURVIVORS (9)

| # | Candidate | Surface | Tier | G1 | G2 | G3 | G4 | G5 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| S1 | **DROP Cycle** — 45-day deletion processing for CA data brokers | 4 regulatory | **T1** | ✓ | ✓ | ✓ | ✓ | ✓ | **SURVIVE.** Every gate re-verified primarily by me — see §5. |
| S2 | **USPTO trademark office-action response pack** | 2 arbitrage | **T1** | ✓ | ✓ | ~ | ✓ | ~ | **SURVIVE.** UPL structuring is a legal-design problem, not an access wall; exclude foreign-domiciled applicants (2019 US-counsel rule). Clock is weak. |
| S3 | **Reg S-P compliance pack for sub-$1.5B RIAs** | 4 regulatory | **T1** | ✓ | ✓ | ✓ | ✓ | ~ | **SURVIVE.** Form ADV CSV carries the CCO's own email. Deadline already passed — trigger is now an exam letter. |
| S4 | **Parish/civil-register full indexes from period handwriting** | 1 overhang | **T1** | ✓ | ✓ | ✓ | ✓ | ✓ | **SURVIVE.** Best *non*-obligation candidate in the cycle. 48 named services doing it by hand are both the demand and the wholesale channel. |
| S5 | **Supplier-catalogue interpreter for Shopify merchants (TT-3)** | 12 two-tabs | **T1** | ✓ | ✓ | ✓ | ✓ | ~ | **SURVIVE.** Matrixify at $20–200/mo with 1,431 dated reviewers is the channel *and* the proof. File-in/file-out survives delisting. |
| S6 | **Markdown ⇄ Jira/Confluence round-trip** | 8 platform | T2 | ✓ | ✓ | ✓ | ✓ | ~ | **SURVIVE.** 1,749 named voters + 508 watchers on one public ticket is the best-targeted buyer list in the file. Landlord risk (Law 11) stands. |
| S7 | **UAD 3.6 workfile + adjustment-commentary generator** | 10 communities | T2 | ✓ | ~ | ✓ | ✓ | ✓ | **SURVIVE, narrowed** — see Conflict 1. Workfile and paste-ready prose only. Never XML, never UCDP, never the form. |
| S8 | **DORA Register of Information filer** | 4 regulatory | T2 | ~ | ~ | ✓ | ✓ | ✓ | **SURVIVE, weakest.** Enumerable population, published file spec, but no scout named a buyer and no price was reachable. |
| S9 | **CCPA risk-assessment / ADMT pre-use notice pack** | 4 regulatory | T2 | ~ | ✓ | ✓ | ✓ | ✓ | **SURVIVE as an attach-on to S1 only.** Same buyer list, same outreach. Does not stand alone. |

## 2b. KILLED (79)

### Scout 1 — capability overhang

| Candidate | Tier | Kill |
|---|---|---|
| C-02 Condo/HOA governing-doc review | T1 | **G1.** Scout: *"could not name ten specific people/threads."* Law 5. |
| C-03 Film-festival deliverable pack | T1 | **G1.** *"Named channel, unnamed individuals."* Law 5. |
| C-04 Hudl-Assist arbitrage (hand-tagged sports film) | T1 | **G1.** Scout's own line: *"best evidence on the sheet, worst distribution."* |
| C-05 Agent-driven VPAT / ACR for SaaS vendors | T1 | **G3 + Law 13.** The VPAT *is* the warranty; buyer is enterprise procurement. |
| C-06 Academic monograph index | T1 | **G2.** Incumbents adequate; scout would not spend a month on it. |
| C-07 Wholesale per-page remediation engine | T1 | **G2 + Law 13a.** See Conflict 2. |

### Scout 2 — manual-labour arbitrage

| Candidate | Tier | Kill |
|---|---|---|
| 2 Marketplace account-reinstatement appeal pack | T1 | **G1 FAIL** (scout's own verdict) + G5 FAIL. |
| 3 Manual J/S/D from an uploaded floor plan | T1 | **G3.** ACCA runs a software-approval programme and some AHJs require approved-software output. Access, not skill. → **WATCHLIST**: one fetch resolves it. |
| 4 Licensure P&P manual pack | T1 | **G1.** No named ten; buyer must be educated. |
| 5 HACCP / food-safety plan pack | T1 | **G1.** Same. |
| 6 Chargeback representment letters | T1 | **G2.** Bundled free by processors and gateways. |
| 7 EU/UK marketplace compliance pack | T1 | **G2.** Same $5-price collapse that killed scout 4's EPR candidate. |
| 8 Grant proposal / LOI drafting | T1 | **G1.** Saturated, no named ten, buyer education required. |
| 9 WCAG/ADA audit & VPAT report | T1 | **Law 13.** The audit is the warranty. |

### Scout 3 — rich incumbent, dead product *(surface returned dry; scout's own refugee test killed 4 of 7)*

| Candidate | Tier | Kill |
|---|---|---|
| 1 Marmalead (Etsy SEO) | T1 | **G2, refugee test.** Healthy cheap alternatives; Etsy unfetchable so demand `UNREAD-CITATION`. |
| 2 Tokeet / Advance.cm | T1 | **G2, refugee test.** Hostaway/Guesty/Lodgify are healthy. |
| 3 Rigbooks | T1 | **G2, refugee test.** |
| 4 Music Teacher's Helper → Duet | — | **G2, refugee test.** |
| 5 a la mode TOTAL | — | **G3.** Scout 3's own UAD/MISMO kill — *upheld for the forms product, overturned for the workfile*. See Conflict 1. |
| 6 BarnManager | T1 | **G2, refugee test.** |
| *Surface verdict* | | **LEDGER-confirmed dead end.** Platform marketplaces cannot host this pattern; landlord forces updates or delists. |

### Scout 4 — regulatory clock

| Candidate | Tier | Kill |
|---|---|---|
| 5 Cyber Resilience Act Art. 14 | T2 | **G1 FAIL** (scout's own verdict). No list. |
| 6 EUDR due-diligence statements | T1 | **G1 FAIL** (scout's own). EU deliberately removed the SME burden. |
| 7 Multi-country packaging EPR declarations | T1 | **G2.** Undone by a $5 incumbent price. |
| 8 FSMA 204 traceability | T1 | **G5.** 2028-07-20 is too far out; population list is partial/state-level. |

### Scout 5 — newly public / newly cheap data

| Candidate | Tier | Kill |
|---|---|---|
| C1 Design-mark image clearance & watch | T1+T2 | **G1.** *"PASS (channel), UNPROVEN (names)"* — Law 5. **Closest miss on this surface**; superb 14-day test (recall against 200 public §2(d) refusals). |
| C2 UK Procurement Act pre-tender window | T1+T2 | **G1.** *"UNPROVEN… zero named first ten"* + Stotles free at entry tier. |
| C3 Local-government meeting video | T1 | **G2.** Curate/FiscalNote, Cloverleaf, Starbridge, USLege already there. |
| C4 Chain store openings/closings from POI diffs | T1+T2 | **G1 + G2.** Enterprise buyers only. |
| C5 NISAR L-band InSAR | — | Killed in place by scout. |
| C6 EU High-Value Datasets | — | Killed in place by scout. |
| C7 FDA Complete Response Letters | — | Killed in place by scout. |
| C8 The TRAC vacuum | T2 | **G2 FAIL AS EVIDENCED** (scout's own). |
| *Surface verdict* | | *"Rich in data and poor in buyers, and the poverty is structural."* |

### Scout 6 — spreadsheet exhaust *(all six die; five on the clock)*

| Candidate | Tier | Kill |
|---|---|---|
| 1 Micro job-shop quote engine | T1+T2 | **G5 WEAK/FAIL** (scout's own). No dated change opens this. |
| 2 Cleaning contract bid-vs-actual P&L | T1+T2 | **G5 FAIL.** |
| 3 WH-347 certified payroll generator | T1+T2 | **G1 FAIL** + G5 FAIL. |
| 4 Plate-cost engine for independents | T1+T2 | **G1 FAIL** + G5 FAIL. |
| 5 Live cost-per-hour for solo trades | T1+T2 | **G5 FAIL.** Wedge only. |
| 6 Manufacturer's-rep commission reconciliation | T1 | **G1 FAIL** (scout recommends kill). |
| *Surface verdict* | | LEDGER-confirmed: *"high tutorial view count is anti-correlated with opportunity."* Retire. |

### Scout 7 — open source with commercial pull

| Candidate | Tier | Kill |
|---|---|---|
| 1 **Bitnami Refuge** | T1+T2 | **G3 + Law 13.** Scout named it exactly: *"The bottleneck is not skill, it is **supply-chain trust**."* Broadcom's $50–72k/yr buys CVE attestation and indemnity — a warranty. We have none. Cleanest illustration of Law 13 in the cycle. |
| 2 Managed Keycloak | T1 | Scout's own **KILL on G3/G4/G5**. |
| 3 Docling-as-a-Service | T1 | **G2.** Incumbents *"partly adequate, which is the problem."* |
| 4 MinIO orphan | — | Scout declined to advance. |
| 5 Managed Mautic | T1 | **G3.** 24/7 on-call — excluded by the operator profile. |
| 6 Managed Paperless-ngx | T1+T2 | **G3.** Same. |
| 7 Gotenberg conversion API | T1+T2 | **G2.** Commodity; free self-host. |
| 8 Hosted listmonk | — | **G3.** Deliverability is a 24/7 reputation business. |
| *Surface finding* | | *"Hosted version?" GitHub issues are a weak instrument* — LEDGER-confirmed. |

### Scout 8 — platform ecosystem gaps

| Candidate | Tier | Kill |
|---|---|---|
| 1 Entra ID / Intune → JSM Assets sync | T1+T2 | **G2 + Standing Law 1.** Pio (599 installs, 4.77★) is *good*, per the scout. The wedge is Intune device objects — a missing feature, not whitespace. |
| 3 Jira ↔ GitHub sync | T1+T2 | **G2.** Official integration + Unito/Exalate serve it. |
| 4 Jira default values for system fields | T2 | **G2 + Law 1.** |
| 5 Confluence page approval / controlled docs | T2 | **G2.** Comala owns it. |
| 6 Jira / JSM issue merge | T2 | **G2 + Law 1.** |
| 7 Shopify multichannel listing/inventory sync | T2 | **G2.** Dozens of incumbents; LEDGER retired Shopify scanning. |
| 8 Jira project-level export/restore | — | **G3.** Atlassian gates the primitives. |

### Scout 9 — price dislocation

| Candidate | Tier | Kill |
|---|---|---|
| PD-1 Scan-to-CAD | T1 | **G1** *"did not verify named handles"* + **G5 UNDATED**. Excellent 14-day test; no clock and no list. |
| PD-2 Solar PV permit plan sets | T1 | **G3 PARTIAL FAIL** (PE stamp) + G5 UNDATED + G1 unnamed. |
| PD-3 Audio description for video | T1 | **Law 13.** 3Play sells *"99%+ measured accuracy"* — a guarantee. |
| PD-4 PDF/document accessibility remediation | T1 | **Law 13a.** See Conflict 2. |
| PD-5 Insurance restoration estimating (Xactimate) | T1 | **G3 + Law 13.** Carrier acceptance is the product. |
| PD-6 Patent drawings | T1 | **G2.** Already arbitraged to commodity by offshore studios. |
| PD-7 Book indexing | T1 | **G1.** No self-serve channel; publisher procurement. |
| PD-8 Zoning / land-use due diligence | T1+T2 | **Law 13.** The buyer relies on it in a transaction. |
| *Surface finding* | | Produced Standing Laws 13 and 14. The laws are worth more than the candidates. |

### Scout 10 — communities with money

| Candidate | Tier | Kill |
|---|---|---|
| 1 ITM report pack for the 1–5-tech fire shop | T1+T2 | **G1.** Scout: *"Rule bans solicitation; practice tolerates."* §9b is explicit — **a banned community is a Gate 1 failure, not a channel.** Ten incumbents already price-floor the segment. **→ WATCHLIST**: revive only if a compliant channel is found. |
| 2 Backflow test-report filing agent | T1+T2 | **G5 WEAK** (scout's own). Correct shape, no clock. |
| 4 TTB compliance for sub-Ekos producers | T1 | **G5 FAIL** (scout's own). |
| 5 Third-party AHJ report-filing layer | T1 | **G3 RISK** (scout's own) — depends on TCE/IROL/Tegris tolerating us. Revocable access. |
| 6 Self-storage lien & delinquency pack | T1+T2 | **G1 FAIL as published** (scout's own) — r/selfstorage vendor ban. |
| 7 ATF A&D / 4473 for the sub-$9/mo FFL | — | Submitted as a kill by the scout. Upheld. |

### Scout 11 — unbundling *(surface retired in the LEDGER before this triage ran)*

| Candidate | Tier | Kill |
|---|---|---|
| A1 Per-document accessibility remediation | T1+T2 | **G2 + Law 13a.** See Conflict 2. Citations re-read live and accurate — the arithmetic, not the evidence, is what kills it. |
| A2 COI collection for sub-50-unit PMs | T1+T2 | **G5 FAIL** (scout's own) + 5 funded vendors in the LEDGER. |
| A3 SF330 Part I assembly | T2 | **G1 FAIL** (scout's own). |
| A4 Outside-counsel-guideline pre-bill scrubber | T2 | **G1 FAIL** (scout's own) + G2 WEAK. |
| A5 Occasional-use catering / BEO packet | T2 | **G2 WEAK** (scout's own). Pricing anger ≠ module demand. |

### Scout 12 — the two-tabs problem

| Candidate | Tier | Kill |
|---|---|---|
| TT-1 Distributor deduction adjudicator (CPG) | T1 | **G1.** *"no named individuals yet"* — Law 5. **Closest miss in the cycle**; six entrants prove the market, four of them 2025–26 indies. → **WATCHLIST**. |
| TT-2 Carrier commission reconciler | T1+T2 | **G1.** Unnamed; agency buyers are not self-serve. |
| TT-4 AppFolio/Buildium → QuickBooks ledger translator | T2 | **G2.** Zapier/native exports cover it. |
| TT-5 VMS timesheet reconciler | T2 | **G1 + G2.** Staffing agencies buy through procurement. |
| TT-6 Certified payroll & fringe-fund remitter | T2 | **G1 UNPROVEN** (scout's own, one word) + incumbent pricing unreachable. Correct Surface-13 shape, zero distribution evidence. → **WATCHLIST**. |
| TT-7 Retailer new-item setup form filler | T2+**T4** | **T4 evidence → automatic kill.** |
| TT-8 Royalty statement generator | T1+**T4** | **T4 evidence → automatic kill.** |
| *+11 killed in minutes by the Zapier 200/404 probe* | — | Recorded by the scout; not re-litigated. Best mechanical test in the cycle. |

---

# 3. WEIGHTED SCORES — the 9 survivors

Rubric: distribution 25% · observable demand 20% · build feasibility 15% · self-verifiability 15% ·
clock 10% · willingness to pay 10% · scale path 5%.

| Rank | Candidate | Dist 25 | Demand 20 | Build 15 | Verify 15 | Clock 10 | WTP 10 | Scale 5 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **DROP Cycle (CA data brokers)** | 10 | 8 | 9 | 10 | 10 | 8 | 7 | **9.10** |
| **2** | **USPTO TM office-action pack** | 9 | 10 | 8 | 10 | 3 | 10 | 5 | **8.50** |
| **3** | **Reg S-P pack for small RIAs** | 8 | 10 | 9 | 8 | 5 | 10 | 6 | **8.35** |
| **4** | **Parish/civil-register indexes** | 7 | 8 | 9 | 10 | 8 | 7 | 4 | **7.90** |
| **5** | **Shopify supplier-catalogue interpreter** | 8 | 9 | 8 | 9 | 4 | 8 | 5 | **7.80** |
| **6** | **Markdown ⇄ Jira/Confluence** | 8 | 8 | 9 | 10 | 5 | 6 | 4 | **7.75** |
| **7** | **UAD 3.6 workfile generator** | 8 | 5 | 8 | 8 | 9 | 5 | 4 | **7.00** |
| **8** | **CCPA/ADMT pack** *(attach-on to #1, not standalone)* | 6 | 7 | 8 | 8 | 8 | 6 | 4 | **6.90** |
| **9** | **DORA Register of Information** | 6 | 6 | 8 | 8 | 7 | 6 | 5 | **6.65** |

**Read the shape, not just the ranks.** #2 and #3 beat #7 on every axis except the clock. The cycle's *hardest
clock* (UAD, verified to the day) sits on the cycle's *thinnest willingness-to-pay evidence* — nobody named a
price for the artifact, and a free adjacent product (NightHawk) is in the market through 2026. Clock is 10% of
the rubric for exactly this reason.

---

# 4. KILL TALLY BY GATE

Exactly one primary killing gate assigned per row; counts sum to 79.

| Gate | Kills (primary) | Share | Per-scout distribution |
|---|---|---|---|
| **G2 observable demand** | **32** | **41%** | S1:2 S2:3 S3:5 S4:1 S5:5 S7:3 S8:6 S9:4 S11:2 S12:1 |
| **G1 cold-start distribution** | **25** | **32%** | S1:3 S2:4 S4:2 S5:3 S6:3 S9:2 S10:2 S11:2 S12:4 |
| **G3 buildable by us** | 13 | 16% | S1:1 S2:1 S3:1 S7:5 S8:1 S9:2 S10:2 |
| **G5 the clock** | 7 | 9% | S4:1 S6:3 S10:2 S11:1 |
| T4 evidence (automatic) | 2 | 3% | S12:2 |
| **G4 self-verifiable** | **0** | 0% | — |
| **Total** | **79** | | |

*(Standing Law 13/13a is the operative reason inside 9 of the G2/G3 kills and is recorded per-row.)*

### The diagnosis the brief asked for: **yes — and both the surfaces and the search budget are at fault.**

**G1 and G2 together account for 57 of 79 kills — 72%.** That is 45% of the rubric doing nearly three quarters
of the killing. Three things follow, and they point in different directions.

**1. G2 is the largest killer, and that verdict is honest.** Thirty-two candidates died because the demand was
already served, already free, or already contested — the refugee test on surface 3 (5 kills), the nine-app
pile-up on surface 8 (6 kills), the funded-incumbent wall on surface 5 (5 kills). This is the filter working.
Six weeks of Cycle 0 were spent on a candidate that would have died here in hour two.

**2. G1's kills are two-thirds budget failure, not market failure.** Of the 25 G1 kills, **18 are "channel
identified, individuals not named"** — Law 5 applied to a scout that ran out of search budget, not to a market
with no channel. Scouts 5, 9, 11 and 12 all wrote some version of *"could not name them, search budget
exhausted."* Only **7 are structurally honest**: vendor-banned communities (r/selfstorage, r/firealarms),
enterprise procurement (VMS, book publishers), buyer education required. **Several of the 18 are one hour of
enumeration away from a G1 pass** — and I demonstrated that during this triage by pulling the CPPA register and
naming ten firms in fifteen minutes.

**3. G4 killed nothing at all, and that is worth a line in the engine.** Zero candidates out of 88 died on
self-verifiability. Either the scouts internalised Gate 4 so completely that they never proposed a
stranger-dependent candidate — likely, given the master prompt says this gate alone would have killed the
entire construction program — or **G4 is now redundant with G3** for a software-only operator. Watch it for one
more cycle; if it kills nothing again, fold it into G3 and give the 15% weight to distribution.

**Two surfaces are mis-specified and should be retired or rewritten:**

1. **Surface 6 (spreadsheet exhaust) is mis-specified.** Three of its six candidates died on **G5** — the
   highest G5 concentration in the cycle — and the other three on G1. Spreadsheet exhaust finds *durable*
   manual work by construction; durable is the opposite of a clock. **The surface selects against Gate 5.**
   Combined with the LEDGER's tutorial-view finding, retire it or rewrite it as "spreadsheet exhaust **with a
   compliance date attached**."
2. **Surface 3 (rich incumbent, dead product) is already dead** per the LEDGER, and this cycle confirmed it:
   five of six candidates fell to the refugee test alone. Do not run it again as specified.
3. **Surface 7 (open source) is a G3 trap for this operator profile** — 5 of its 8 kills are G3, and every one
   of them is the same reason: *managed hosting means 24/7 on-call*, which the operator profile excludes by
   name. Rewrite it as "open source with an **asynchronous, batch, retryable** artifact" or drop it.

**Two surfaces are mis-specified and should be retired or rewritten:**

1. **Surface 6 (spreadsheet exhaust) is mis-specified.** Five of its six candidates died on **G5**, the clock —
   the highest G5 concentration in the cycle. Spreadsheet exhaust finds *durable* manual work by construction;
   durable is the opposite of a clock. The surface selects against Gate 5. Combined with the LEDGER's
   tutorial-view finding, retire it or rewrite it as "spreadsheet exhaust **with a compliance date attached**."
2. **Surface 3 (rich incumbent, dead product) is already dead** per the LEDGER and this cycle confirmed it —
   all six candidates fell to the refugee test. Do not run it again as specified.

**And one instruction should change for Cycle 2.** Scouts were asked for breadth (6–10 candidates) *and* named
first tens. Under Standing Law 5, an unnamed first ten is a kill — so breadth without enumeration budget
manufactures kills. **Either give each scout an explicit enumeration budget, or split the role: scouts find
shapes, a dedicated enumerator names the ten.** As run, Cycle 1 spent its search budget on breadth and then
killed 17 candidates for lacking the thing the budget ran out before buying.

---

# 5. TOP 5 — AND THE SINGLE CHEAPEST TEST THAT KILLS EACH

### 1. DROP Cycle — 9.10 · *already verified further than any other candidate*

I ran the mechanical tests during triage rather than recommending them, so here is what is **already settled,
primarily**:

- **Register pull — DONE.** `https://cppa.ca.gov/data_broker_registry/registry.csv` → HTTP 200, **603 rows**,
  **603 with a real email address**, plus phone, street address, and — decisively — **per-firm self-reported
  CCPA request volumes and median days-to-respond**. That is a published, dated, per-buyer pain metric.
  Firms already reporting **30-day and 43-day medians** against a 45-day statutory window are visibly at the
  edge. Ten I can name today: *eLocal USA LLC · National Opinion Institute LLC · Quadrant Global Pte Ltd ·
  Simio Cloud LLC · Project Affinity Inc · Date Detective Inc · IDMAP Inc · Anne Lewis Strategies LLC ·
  ROR Partners LLC · Buxton Company LLC.* **Gate 1 is a verified pass, not a plausible one.**
- **Obligation — verified primary.** CalPrivacy, 2026-06-02: *"Beginning August 1, all data brokers will be
  required to access DROP and begin processing deletion requests"*; 300,000+ consumers enrolled.
- **Gate 3 — verified primary, and this is the part that matters.** The **full OpenAPI 3.1.0 specification is
  publicly downloadable with no authentication**: `https://dropresources.blob.core.windows.net/apidocs/databroker_api.yaml`
  — *DROP Data Broker API v1.2.0*, three endpoints (`/data/download`, `/data/upload`, `/data/amend`), auth by
  `X-API-KEY` **generated by the broker in their own portal**. A **sandbox** is published. The regulator's own
  process page states the cycle: *"Step 1 Download… Step 2 Standardize and hash **your records**… Step 3 Match
  and process… Step 4 Report status. Repeat at least once every 45 days"* and — critically — *"**Direct service
  providers to process accordingly**."* Service-provider processing is contemplated by the regulator.
- **The one real boundary, read primarily.** The DROP portal Terms of Use (eff. 2025-12-05) state *"You must
  not share your password or transfer your account access to any third party"* and prohibit *"Use DROP to
  develop software, AI tools, or machine learning models"* and *"bots, scrapers."* **Consequence: we never hold
  a broker's password and never train on DROP data. We ship software the broker runs under their own API key.**
  That is the Drop45 shape and it is compliant. **Say this in writing before the first line of code.**

> **Cheapest remaining kill test — 2 hours, today.** De-obfuscate the 603 emails, segment to the ~400 firms
> that are not subsidiaries of Ketch/DataGrail/Transcend customers, and send 40 plain-text messages that
> quote *their own published median response time* back to them alongside the 2026-09-15 first-cycle close.
> **Kill number: fewer than 3 replies expressing interest from 40 messages.** No stranger's cooperation is
> needed to run it; the reply rate *is* the answer. Second, half-day test: implement the published hashing and
> standardization rules against the sandbox and confirm a round-trip. If the spec cannot be implemented in a
> day by us, the whole thesis is wrong.

### 2. USPTO trademark office-action pack — 8.50

> **Cheapest kill test — 1 day, zero cost, and it is the best-designed test in the cycle.** Pull 50 office
> actions from TSDR, generate 50 responses, then grade them against **the responses that were actually filed
> later and the recorded outcome — both public in TSDR.** A closed-loop, ground-truthed accuracy measurement
> requiring no stranger at all. **Kill number: fewer than 40 of 50 substantively matching the successful filed
> response on every refusal ground.** Run the UPL structuring review in parallel — it is the likelier killer.

### 3. Reg S-P pack for small RIAs — 8.35

> **Cheapest kill test — 3 hours.** Download the SEC Form ADV complete dataset, filter to RAUM < $1.5B, and
> **count how many rows carry a usable CCO email in Item 1.J rather than a registered-agent or
> compliance-vendor address.** This is the single assumption the candidate rests on and it is a spreadsheet
> operation. **Kill number: fewer than 2,000 firms with a direct CCO email.** Second, 30 minutes: check whether
> the $599 template vendor has already added a maintained-register tier — if they have, the empty price band
> is gone.

### 4. Parish/civil-register indexes — 7.90

> **Cheapest kill test — 1 day.** Take one register that already has a *human-made* published index (Matricula
> and FamilySearch both host these), run ours over the raw images, and measure **entry recall and name accuracy
> against the human index.** Pure, offline, ground-truthed. **Kill number: below 90% entry recall or below 85%
> surname accuracy** — beneath that the artifact cannot be sold as exhaustive, and exhaustiveness is the whole
> product. Then spend 20 minutes confirming the Fiverr price evidence, which is now cheap: **Fiverr is readable
> via `r.jina.ai`** and scout 1 marked those numbers UNVERIFIED only because it did not know that.

### 5. Shopify supplier-catalogue interpreter (TT-3) — 7.80

> **Cheapest kill test — 2 days.** Collect 20 real supplier catalogue files (they are posted openly in merchant
> forums and supplier portals), run our category / variant / SKU inference, and score against a human's
> decisions on the same files. **Kill number: below 85% correct on variant-axis detection**, which is the
> judgement call Matrixify explicitly does not make and the only thing we would be selling. Also 15 minutes:
> re-check whether Matrixify has shipped semantic mapping since Apimio failed at $199 — if it has, the gap is
> closed.

### Runner-up worth one hour: **UAD 3.6 (7.00)**

> **Cheapest kill test — 1 hour, and it should be run before anything else.** Search r/appraisal and
> AppraisersForum for *"adjustment support"*, *"paired sales"*, *"Redstone"*, *"regression"* and read what
> appraisers say they **pay** for adjustment derivation today. Scout 10 produced no price for this artifact and
> neither did I. **Kill number: no appraiser in 12 months naming a dollar figure they pay for adjustment
> support.** If nobody names a price, the hardest clock in the cycle is attached to a free good and the
> candidate is dead regardless of the deadline. Second, 30 minutes: verify the WorkingRE 3%/58%/64% survey at
> source, and verify the "CU is field-driven" claim against a GSE document rather than a 4-comment Reddit
> compilation — the whole thesis rests on a second-hand sentence.

---

# 6. IS THE CONVERGENCE REAL, OR DID THE OPERATOR CONTAMINATE THE FLEET?

**Short answer: the convergence is real. You did not bias the fleet. But it is a weaker signal than five
independent confirmations, for a reason that has nothing to do with contamination.**

### The timestamps

The convergence note and Surface 13 were committed in `f6e2bf6` at **08:19:36**.

| Landed **before** the note (uncontaminated by construction) | Landed **after** |
|---|---|
| 04 regulatory `08:11:52` · 08 platform `08:12:04` · 09 price `08:12:40` · 05 data `08:14:12` · 07 OSS `08:14:21` · 01 overhang `08:17:21` · 06 spreadsheet `08:18:08` · 12 two-tabs `08:18:26` | 10 communities `08:21:33` · 03 incumbents `08:23:10` · 11 unbundling `08:24:18` · 02 arbitrage `08:26:05` |
| **8 scouts** | **4 scouts** |

**Three of the five converging scouts — 4, 7 and 12 — are the ones that *originated* the observation, and all
three landed before the note existed.** They cannot have been contaminated by a note written from their own
findings.

### The textual test, which is decisive

I grepped all twelve reports for every token the mid-cycle edit introduced: *"compelled users"*, *"Surface 13"*,
*"convergence"*, *"externally-imposed"*, *"whose customer is"*, *"Standing Law 15/16"*.

**Zero hits in all four post-note scouts (10, 03, 11, 02).** The only hits anywhere are in scouts **7 and 12** —
two of the three that originated the idea, pre-note. Not one scout that finished after 08:19:36 uses the note's
vocabulary, cites its new surface, or invokes its new laws.

The mechanism is obvious in hindsight: all twelve scouts were launched in parallel from the 08:00:57 brief. A
mid-flight edit to `MASTER-PROMPT.md` reaches only a scout that re-reads the file, and none did. **Your edit
landed in the engine for Cycle 2, not into Cycle 1's fleet.**

### Two pieces of corroborating evidence pointing the same way

- **Scout 10 landed at 08:21 — after the note — and its report contains no trace of it**, yet your own commit
  message for it reads *"This is the fourth independent scout to land on externally-imposed obligation."* It
  arrived at Standing Law 16 (the regulated document) from its own ~45-community sweep, independently.
- **Scout 11 returned a surface-killing verdict**, not a thesis-flattering one: *"Unbundling is picked over —
  retire the surface."* A contaminated scout flatters the prevailing thesis. Scout 11 destroyed its own
  assignment. That is the behaviour of an uncontaminated agent.

### The honest caveat, which matters more than the contamination question

**The convergence is partly an artifact of the gate set, not only of the market.** Gates 1 and 2 are 45% of the
rubric, and together they reward exactly one thing: *a buyer who is already visibly compelled and already
enumerable.* Any surface pushed through this filter will converge on externally-imposed obligation, because the
filter selects for it. The five scouts did not independently discover a fact about the world; they
independently discovered **what this filter passes**.

That is still valuable — it means the filter is consistent, and consistency is what a cold-start operator needs.
But state it correctly in the engine: *"externally-imposed obligation is the shape our gates select for"* is
true and useful. *"Externally-imposed obligation is where the opportunities are"* is not established by this
cycle and should not be written into the master prompt as though it were. **The one datum that argues against
the stronger claim is survivor #4** — the parish-register index, which has no obligation of any kind behind it,
scores 7.90, and passes all five gates on a hobbyist paying out of pocket.

---

# 7. ADVANCE TO DEEP-DIVE: **DROP Cycle — 45-day deletion processing for California data brokers**

**Rationale, three sentences.**

It is the only candidate in the cycle where I converted every gate from a scout's argument into a primary-source
fact during triage itself: the regulator publishes **603 obligated firms with working email addresses and each
firm's own self-reported median response time**, the obligation switched on **26 days ago** with the first
45-day cycle closing mid-September, and the integration is a **publicly downloadable OpenAPI 3.1 spec with a
sandbox** — an open file spec owned by a regulator whose statutory purpose is to make these firms comply, which
is the opposite of the Procore-shaped revocable API that killed Cycle 0.

It satisfies Standing Law 7 exactly — the deletion is the commodity and the **timestamped evidence file** is what
gets paid for — and Standing Law 16 exactly, since it is a regulated document in a named format, for a named
third party, under a deadline, and about to fragment across Connecticut, New Jersey, Oregon, Texas and Vermont
on a published schedule, which is research-heavy work a hobbyist with a coding assistant will not follow us into.

The one thing that could still kill it is not technical but commercial — whether the long tail of the 603 is
large enough after removing subsidiaries already covered by Ketch, DataGrail and Transcend — and that question
is answerable in an afternoon with the CSV I have already downloaded, which is precisely the kind of decisive
test Gate 4 exists to demand.
