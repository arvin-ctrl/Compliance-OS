# SCOUT 05 — NEWLY PUBLIC OR NEWLY CHEAP DATA

**Cycle 1 · surface: datasets that just opened, got an API, or collapsed in price**
**Researched:** 2026-08-27 · **Scout:** 05

---

## HEADLINE VERDICT — read this first

**This surface is rich in data and poor in buyers, and the poverty is structural, not accidental.**

I found plenty of genuine 2024–2026 data openings with hard dates. What I could not find, in most
cases, is the thing Gate 2 and Gate 1 actually require: **a named, self-serve buyer already paying money
for the refined artifact.** The pattern that recurs on this surface is:

> Public data is refined into a product. The product is sold to enterprises, because enterprises are the
> only buyers who will pay four figures for a list. The niches where a *small* buyer self-serves
> (building permits, government bids, local-government meetings, hospital prices, POI data) have all
> been entered in the last 36 months by funded companies that already did the ingestion work.

Concretely: building permits → **Shovels** (170M permits, 2,770 jurisdictions). Local government
meetings → **Curate/FiscalNote** (400,000 documents/week) plus **Cloverleaf AI** ($2.8M raised) plus
**Starbridge** plus **USLege**. UK tenders → **Tenders Direct**, **Stotles**, **Tussell**, **BiP**.
Grid data → **gridstatus.io**. Hospital prices → **Turquoise Health**, **Serif Health**. These are
Gate-2 proofs *and* Gate-1 obstacles simultaneously.

**Live candidates I would actually spend a month on: 2 (C1, C2).**
**Candidates worth 14 days of cheap testing: 2 more (C3, C4).**
**Documented kills: 5 in-report + 8 in the kill list.**

Per the brief's standard (6–10 candidates), I am returning 8 entries with evidence attached, but I am
labelling honestly which are live and which are corpses. I am also flagging that **my WebSearch budget
was exhausted at call 200 partway through this run** (shared session budget), which limited my ability
to compile named first-ten-user lists. Where I could not name them, I say so rather than inventing.

---

## C1 · Design-mark (image) trademark clearance and watch

**One sentence:** A US trademark image-similarity search and weekly watch service — you upload your logo
and get back visually confusing marks already on the USPTO register — sold for a fraction of what
Corsearch charges.

**The artifact:** (a) a one-off *clearance report* PDF: your mark vs. the N most visually and
phonetically similar live US marks, with class overlap, status, and owner; (b) a *weekly watch email*:
newly filed applications that are visually confusable with a mark you own.

**Evidence — Tier T1 + T2**
- **Corsearch**, the incumbent, is reported at **"$12,320 per year for unlimited online text searches
  (USPTO + state)"** — https://thecmo.com/services/trademark-monitoring-service/ (accessed 2026-08-27).
  *Third-party reported, not read off Corsearch's own pricing page — treat as T2 until confirmed.*
- **Markify** (the discount incumbent) is reported at **"pricing starts at $89, and for the US, the
  starting price is $169"** — https://softwarefinder.com/legal/markify and
  https://www.getapp.com/legal-law-software/a/markify-watch/ (accessed 2026-08-27). Markify's own site
  (https://www.markify.com/) confirms the product line — ProSearch, **US Design Mark (image marks)**,
  **All countries device/image marks**, trademark watch, bulk watch, domain watch, and "API's & data
  access" — but does **not publish prices on the homepage**. *Product line verified; prices T2.*
- Markify selling a distinct, higher-priced **"US Design Mark (image marks)"** SKU separate from word
  marks is itself the demand signal: image search is the part people pay extra for, because it is the
  part that could not be automated.

**The clock**
- **12 February 2025** — USPTO launched the **Open Data Portal** (https://data.uspto.gov/), replacing
  both PEDS and the **Bulk Data Storage System**, with free JSON REST APIs and bulk extraction in one
  place (https://www.uspto.gov/subscription-center/2025/uspto-launches-new-open-data-portal-easy-quick-access-data).
  API key requires a USPTO.gov account linked to ID.me — free, but a signup step.
- The larger half of the clock is a **cost collapse, not a data opening**: visual-similarity search over
  a multi-million-image corpus went from a proprietary ML asset (Clarivate's TrademarkVision,
  Corsearch's image engine) to ~an afternoon of CLIP-style embeddings plus a vector index. I am being
  explicit that this is a capability overhang wearing a data-opening costume.
- **UNVERIFIED and load-bearing:** whether USPTO design-mark *images* specifically are obtainable in
  bulk through ODP or only through the older trademark daily/annual XML + TSDR routes. **This is the
  first thing to check and it is a 30-minute check.**

**First ten users:** *Could not name them in this session* (search budget exhausted). The channel,
however, is the strongest on this whole surface and is not a sales motion: high-commercial-intent search
("trademark image search", "logo trademark search", "is my logo taken"), plus the Amazon Brand Registry
and Etsy/Shopify seller populations who must hold a registered mark and currently buy $199–$399 filing
packages from LegalZoom/Trademark Engine tier vendors. **A free image search tool is the ad.**

**Gate check**
- **G1 distribution — PASS (channel), UNPROVEN (names).** Search-led, self-serve, free tool as the ad.
  No warm intro, no enterprise procurement. But I did not compile the ten names.
- **G2 observable demand — PASS.** Two incumbents with published-ish prices and a dedicated paid image
  SKU. Money moves at both $169 and $12,320.
- **G3 buildable — PASS.** USPTO data is US Government work, public domain, freely redistributable
  commercially. No credential needed: Markify is not a law firm. Output is a search report, not legal
  advice.
- **G4 self-verifiable in 14 days — PASS.** Build the index, run it against 200 known USPTO refusal
  decisions (2(d) likelihood-of-confusion refusals are public), and measure recall against the examiner's
  cited mark. That is a pure, solo, offline test with a hard number.
- **G5 clock — PARTIAL.** ODP is 12 Feb 2025 (good). But trademark data was *already* accessible; the
  real clock is embedding cost. Honest read: G5 is the weakest gate here.

**What already exists:** Corsearch (adequate but priced for corporate IP departments), Markify (the real
competitor — cheap, image-capable, has an API). **Markify is the reason to be careful.** Their existence
proves the market; their price floor of ~$169 caps ours. The wedge is not "cheaper watch" — it is
*clearance before filing* for the pro-se and legal-tech-filed applicant, where the current alternative is
a $0 keyword search on USPTO's site that misses every design mark.

**Price signal:** $169/yr (Markify entry) → $12,320/yr (Corsearch). LegalZoom-tier trademark filing
packages sit at $199–$399 per filing and bundle a "comprehensive search" — that is the adjacent budget.

**Confidence: 6/10.** Best Gate-1 story on the surface. Weakest Gate-5 story. Kill it fast if the
USPTO design-mark image bulk route turns out to be gated.

---

## C2 · UK Procurement Act 2023 — the pre-tender window

**One sentence:** An alert product built on the notice types that did not exist before 24 February 2025 —
**pipeline notices** and **preliminary market engagement notices** — which tell an SME supplier what a
public body is going to buy *months before the tender appears*.

**The artifact:** A weekly digest, per supplier, of (a) planned procurements from pipeline notices with
estimated value and expected start date, (b) preliminary market engagement notices where the buyer is
actively soliciting supplier input, with the named contact and the closing date, and (c) a one-page
"how to respond" brief per opportunity. The artifact is the *pre-tender* brief, not the tender alert —
tender alerts are commoditised.

**Evidence — Tier T1 + T2**
- **Tenders Direct** (Proactis): *"subscriptions start from £1,359 per year"*, including personalised
  alerts, bid management tooling, and 7+ years of UK/EU contracts and awards —
  https://app.tendersdirect.co.uk/b/pricing-plans (page returned HTTP 403 to my fetcher; figure is from
  the indexed snippet, accessed 2026-08-27). **T2 until read off the live page.**
- **BidPrime** (US equivalent, same product shape): no public pricing; third-party reviews report
  **~$399–$2,300/year**, with national SLED plans reported at **$10,000–$12,000+/year** —
  https://govbid.ca/compare/bidprime, https://coldiq.com/tools/bidprime (accessed 2026-08-27).
  **T2, third-party reported.**
- The new dataset is real and large. Open Contracting Partnership, **23 June 2025**, analysing
  24 Feb – 31 May 2025 (https://www.open-contracting.org/2025/06/23/uk-procurement-act-implementation-what-does-the-first-three-months-of-data-tell-us/):
  - **~600 buyers published 1,691 preliminary market engagement notices**, growing **22 (late Feb) → 831 (May)**.
  - Competitive flexible procedure use: **67 (March) → 315 (May)**, 159 of them at pipeline/pre-market stage.
  - Direct awards rose from **15% of procedures (March) to 24% (May)**.

**The clock — this is the strongest clock I found**
- **24 February 2025** — the Procurement Act 2023 came into force UK-wide and the **Central Digital
  Platform** went live inside Find a Tender, creating for the first time a single structured dataset
  across the whole procurement lifecycle in **OCDS JSON**.
- New notice types that did not previously exist: **UK1 pipeline**, **UK2 preliminary market engagement**,
  UK3 tender, UK4 award, **UK5 direct award transparency**.

**The raw form is genuinely hostile — which is the opportunity**
Per OCP's own analysis of the platform:
- **OCDS JSON via API only. No bulk download, no Excel/CSV on the platform itself.** OCP's words:
  *"using an API assumes quite a level of sophistication."*
- **Buyer identifier coverage: 12% (Jan 2025) → 43% (March 2025). Supplier IDs: 36% (May 2025).**
  The same organisations appear under multiple IDs and name variants.
- **Only 9.5%** of lots with quality criteria publish the criteria weights.
- **Only 58%** of tenders carry a tender-document link; ~**10%** of those links go to a registration wall
  or a generic page.

Entity resolution and link-following are exactly the work an agent fleet does cheaply and a £1,359/yr
incumbent has not bothered to do.

**A second, unclaimed artifact from the same Act:** the Act also mandates **contract performance / KPI
notices** (for larger contracts), **contract payment notices**, and **payments compliance notices**, plus
a central **debarment list**. That is a public *supplier-performance* dataset that nobody currently
resells. I could not verify the debarment list's contents this session (the gov.uk URL I tried 404'd) —
**flagged for the next scout.**

**First ten users:** *Could not name them.* This is the candidate's real weakness. The buyer population
(UK SMEs bidding for public work) is large and self-serve-shaped, but I did not compile ten named firms
or ten dated forum posts. **Do not advance this past a 14-day test without that list.**

**Gate check**
- **G1 distribution — UNPROVEN.** Plausible SEO/self-serve shape ("find a tender alternative", "pipeline
  notices"), but zero named first ten. Treat as the gate to test first.
- **G2 observable demand — PASS.** Tenders Direct £1,359/yr, BidPrime $399–$2,300/yr, Stotles and Tussell
  both funded and operating in exactly this data.
- **G3 buildable — PASS.** Public API, no procurement, no credential. Licensing: Find a Tender data is
  **believed to be Open Government Licence v3.0** (commercial reuse permitted) — **VERIFY before build.**
- **G4 self-verifiable in 14 days — PASS.** Ingest the OCDS feed, resolve buyer/supplier entities, and
  measure: how many pipeline + PME notices per week, how many carry a named contact, and what fraction
  of eventual tenders were foreshadowed by a pipeline notice ≥30 days earlier. That last number *is* the
  product's entire value proposition and it can be computed alone, from history, in under two weeks.
- **G5 clock — PASS, dated. 24 February 2025.**

**What already exists:** Stotles (freemium, VC-backed, explicitly markets pre-tender signals — this is
the direct threat and the reason to check whether the gap is already closed), Tussell (market
intelligence, enterprise-priced), Tenders Direct, BiP Solutions, Bidstats (free). **Stotles being
free at the entry tier is the single biggest Gate-2 risk here** — a free incumbent means the money is
not moving at the tier we could reach.

**Price signal:** £1,359/yr entry (Tenders Direct).

**Confidence: 5/10.** Best clock, best hostile-raw-form story, unproven distribution, and a free
competitor sitting on the exact wedge.

---

## C3 · Local-government meeting **video** (not minutes) — sliced to one vertical

**One sentence:** Every US town posts hours of council and planning-commission video that nobody
transcribes; ASR now costs cents per hour, so the video archive is functionally a new dataset — sold as
a keyword alert into one vertical that already buys leads.

**The artifact:** A daily email: "Your keyword appeared in [Township] Planning Commission, 26 Aug,
at 01:14:32 — here is the 90-second transcript, the speaker, the agenda item, the linked packet PDF,
and a jump link into the video."

**Evidence — Tier T1**
- **Curate** (acquired by **FiscalNote**, **August 2021**) scans **"400,000+ meeting minutes & agendas
  each week"** from **"more than 12,000 local government entities"**, and maintains contact data for
  **"more than 112,000 elected officials, city staff, and other stakeholders"** —
  https://www.curatesolutions.com/ , https://www.curatesolutions.com/curate-data-sources (accessed
  2026-08-27). A public company bought this. That is money.
- **Cloverleaf AI** raised **$2.8M** and runs *"a database of millions of hours of city council meetings
  with each meeting video transcribed"*, with next-day email alerts —
  https://www.govtech.com/biz/cloverleaf-ai-raises-2-8m-to-help-gov-tech-suppliers ,
  https://www.cloverleaf.ai/ (accessed 2026-08-27). Pricing is quote-only.
- **USLege** (https://www.uslege.ai/) and **Starbridge** (https://starbridge.ai/) are doing the same
  thing. **HeyGov's ClerkMinutes**, launched **2024**, is used by **"more than 450 municipalities"**
  (https://clerkminutes.com/press) — that is the *supply* side of the same collapse.

**The clock:** not a data opening — a **price collapse in extraction**. Whisper-class ASR plus long-context
summarisation took a 3-hour meeting from "a human watches it" to "cents". Curate's business is built on
*minutes and agendas* (text documents that clerks publish weeks late, or never, for small bodies);
**video is published within 24–48 hours and is where the actual discussion happens.** That asymmetry is
the entire wedge and it is dated by the ASR cost curve rather than by a statute.

**First ten users:** *Could not name them.* The only version of this that survives Gate 1 is **one narrow
vertical whose members already buy leads and are individually findable** — my candidate slice is
**data-centre / battery-storage / solar siting**, where rezoning and special-use applications surface in
planning-commission video months before any permit record exists, and where both developers *and*
organised opposition groups are publicly identifiable. I did not build that list.

**Gate check**
- **G1 distribution — FAIL as a horizontal, UNPROVEN as a vertical.** Cloverleaf, Curate and Starbridge
  all sell top-down to B2G sales teams and government-affairs departments. We cannot run that motion.
- **G2 observable demand — PASS, emphatically.** FiscalNote acquisition + $2.8M seed + three live
  competitors.
- **G3 buildable — PASS on skill, RISK on licensing.** The compute is trivial. **The licensing is not
  clean:** meeting video is hosted on Granicus / Swagit / CivicPlus / YouTube under platform ToS, and
  municipal copyright status varies by state. Bulk retrieval may breach a host's ToS even where the
  underlying record is public. **This needs a real answer before build.**
- **G4 self-verifiable in 14 days — PASS.** Transcribe 200 meetings from 50 bodies in one target county
  and count: how many rezoning/special-use items appeared in video **before** appearing in any permit or
  minutes record, and by how many days. Solo, offline, a hard number.
- **G5 clock — PARTIAL.** Real but undated; and the competitors already acted on it, which is the
  problem.

**What already exists:** Cloverleaf AI is doing precisely this (video, transcribed, keyword alerts,
next-day email). **On the horizontal, it is adequate — kill.** The only surviving question is whether a
vertical slice with a self-serve price point is unserved.

**Price signal:** All quote-only. Adjacent published anchor: BidPrime $399–$2,300/yr for a strictly
worse signal (published bids, i.e. too late).

**Confidence: 4/10.** Strong G2, strong G4, but G1 requires a vertical I have not evidenced and G3 has a
real ToS problem.

---

## C4 · Chain store openings and closings, from differenced open POI snapshots

**One sentence:** Foursquare now publishes 106 million places under Apache 2.0 and refreshes them
monthly — diff consecutive snapshots and you get a free, national feed of which chains opened and closed
which locations, which is a thing people currently buy.

**The artifact:** A monthly "openings and closures" table per brand — chain, address, geo, first-seen /
last-seen month, confidence — plus an alert when a watched brand crosses a threshold in a watched metro.

**Evidence — Tier T1 + T2**
- **FSQ OS Places**: GA **November 2024**; **Apache 2.0**, explicitly permitting commercial use;
  Parquet on S3 / Iceberg catalog; **updated monthly**; the **December 2025** release reported
  **106,205,195 POIs** with 20+ attributes and 1,000+ categories —
  https://docs.foursquare.com/data-products/docs/fsq-places-open-source ,
  https://foursquare.com/resources/blog/products/foursquare-open-source-places-a-new-foundational-dataset-for-the-geospatial-community/ ,
  https://simonwillison.net/2024/Nov/20/foursquare-open-source-places/ (accessed 2026-08-27).
  **Licence verified: commercial redistribution permitted.**
- **Overture Maps Foundation** reached GA in **July 2024** with an independent places layer — a second
  free corpus to cross-check against. *Licence believed CDLA-Permissive-2.0 for places — VERIFY.*
- **T2 demand signal:** the community project **`alltheplaces/alltheplaces`** —
  **816 stars, 272 forks, 841 open issues** (https://github.com/alltheplaces/alltheplaces, checked
  2026-08-27) — exists solely because people want per-brand store location data and are willing to
  hand-write a scraper per chain to get it. 841 open issues is 841 people who want a specific brand
  covered.
- Paid comparators for store-location data (**T2/UNVERIFIED prices** — I could not read their pricing
  pages this session): ScrapeHero store-location datasets, Chain Store Guide directories, Advan (ex-
  SafeGraph) Places, Placer.ai.

**The clock:** **November 2024** (FSQ OS Places GA) + **July 2024** (Overture GA). Before that, a
national POI corpus with commercial redistribution rights cost real money; SafeGraph's Places product
was the reference and it was not free.

**First ten users:** *Could not name them.* Plausible: CRE brokers, franchise suppliers, retail-focused
newsletters, short-side equity researchers, local news desks. None named.

**Gate check**
- **G1 distribution — UNPROVEN.** "The dataset is the ad" is a real cold-start pattern (gridstatus did
  exactly this), and a free openings/closings tracker posted to HN is a credible launch. But no names.
- **G2 observable demand — WEAK.** This is where it wobbles. I have a 816-star GitHub project (T2) and a
  set of vendors whose prices I could not verify. **I do not have a single confirmed price for the
  refined artifact.** Under Gate 2 as written, that is not enough.
- **G3 buildable — PASS.** Apache 2.0, verified. Diffing monthly Parquet snapshots is trivial.
- **G4 self-verifiable in 14 days — PASS, and this is the decisive test.** Download the last 12 monthly
  FSQ snapshots, diff them for 20 chains whose real openings/closings are publicly known from press
  releases and 10-K store counts, and measure precision/recall of detected closures and the lag in
  months. **If FSQ's monthly refresh does not actually retire closed locations promptly, the product does
  not exist.** My prior is that it does not — dump-based POI corpora are notoriously slow to remove
  closures. This is a two-day test that probably kills the candidate.
- **G5 clock — PASS, dated. November 2024.**

**What already exists:** Placer.ai and Advan sell far richer retail intelligence (foot traffic, not just
existence) at enterprise prices. Free openings/closings trackers do not exist that I found.

**Price signal:** **UNVERIFIED.** I could not confirm any price for store-location or openings/closings
data. That is a genuine Gate-2 gap, not a research shortcut.

**Confidence: 3/10.** Cheapest test on the list (two days), most likely to die in that test.

---

## C5 · NISAR free global L-band InSAR — **killed in place**

**Clock (excellent, freshest on the surface):** **20 July 2026** — the first public release of calibrated
NASA-ISRO NISAR L-band products through the Alaska Satellite Facility DAAC, covering observations from
**17 June 2026** onward, free of charge, with the complete first-year science record expected by end of
2026. 12-day repeat, global, and specifically good at ground deformation in vegetated terrain
(https://www.earthdata.nasa.gov/news/nisar-l-band-data-released-expanding-record-of-surface-changes ,
https://nisar-docs.asf.alaska.edu/availability-overview/ , accessed 2026-08-27).

**Why it dies:**
- **G2 fails on a specific mechanism: the refined artifact is already being given away by governments.**
  ESA/Copernicus **EGMS** publishes free ground-motion for all of Europe, and NASA's **OPERA** project
  publishes free Sentinel-1 surface-displacement products for North America. Selling derived ground
  motion means competing with two free national services.
- **G1 fails.** The buyers who pay for InSAR — pipeline operators, rail infrastructure owners, mining
  companies, tailings-dam regulators, reinsurers — are enterprise procurement with security reviews.
  The one per-transaction market I identified (UK conveyancing ground/subsidence search reports, sold
  per property by Landmark, Groundsure, Terrafirma) is ordered through search-provider panels that
  conveyancers do not switch casually, and it carries a professional-liability tail.
- **G3 risk:** NISAR is a joint NASA-ISRO mission. NASA's open-data policy is unrestricted, but **I did
  not verify that ISRO co-ownership imposes no commercial-reuse condition on the L-band products.**

**Verdict: KILL.** Note it in the watchlist only if a per-transaction, self-serve ground-risk buyer is
ever identified.

---

## C6 · EU High-Value Datasets — free company registries and geospatial across 27 states — **killed in place**

**Clock (real, dated):** Commission Implementing Regulation **(EU) 2023/138** has applied since **2024**
(compliance deadline **9 June 2024**), requiring every member state to publish six categories of
high-value dataset — **geospatial, earth observation and environment, meteorological, statistics,
companies and company ownership, and mobility** — **free of charge, machine-readable, via APIs, and as
bulk download where indicated**
(https://eur-lex.europa.eu/eli/reg_impl/2023/138/oj/eng ,
https://www.lexisnexis.com/en-gb/legal/news/new-high-value-datasets-rules-start-applying-in-eu ,
accessed 2026-08-27). Company registration data and filed accounts that member states used to charge for
are now legally required to be free.

**Why it dies for *us*:**
- **G1 fails hard.** Everyone who pays for pan-European company data is a KYC/AML, credit-risk,
  supply-chain-diligence or sanctions function inside a regulated institution. That is enterprise
  procurement plus a security review — two automatic Gate-3 fails and a Gate-1 fail.
- **G2 is strong** (Creditsafe, Bureau van Dijk/Moody's, Dun & Bradstreet, OpenCorporates all charge
  real money), which is exactly why the well-capitalised incumbents will absorb the free feeds first.
- Implementation is uneven across 27 states, so the arbitrage window is a multi-year, multi-jurisdiction
  ingestion slog — a fragmentation cost, not a moat. The postmortem names this exact trap.

**Verdict: KILL.** Correct read: this is a *cost reduction for incumbents*, not an opening for a
cold-start operator.

---

## C7 · FDA Complete Response Letters — **killed in place**

**Clock:** **10 July 2025** — FDA published **more than 200 Complete Response Letters** issued
2020–2024, via openFDA, with a dedicated API endpoint
(https://open.fda.gov/apis/transparency/completeresponseletters ,
https://www.pharmtech.com/view/fda-publishes-more-than-200-complete-response-letters , accessed
2026-08-27). Genuinely new: FDA historically never published these, and a 2015 FDA study found sponsors
omitted **85%** of FDA safety/efficacy concerns from their own announcements.

**Why it dies:**
- **Volume.** 200 documents is not a dataset; it is a reading list. The FDA Law Blog's own headline was
  *"Radical Transparency or Radical Redundancy? … Most of Which Are Already Public"*
  (https://www.thefdalawblog.com/2025/07/).
- **G1 fails.** Every buyer of regulatory intelligence (Citeline, Cortellis, AlphaSense) is a pharma
  enterprise account.

**Verdict: KILL.**

---

## C8 · The TRAC vacuum — federal immigration and enforcement case data

**One sentence:** Syracuse University took down TRAC, the 30-year-old clearinghouse that refined DOJ/DHS
FOIA record dumps into usable statistics; the underlying raw data is still published, and the people who
depended on the refined version are loudly stranded.

**The artifact:** The specific queries practitioners used TRAC for — immigration court backlog and
outcome rates **by court, by judge, by nationality, by representation status** — as a live dashboard plus
a CSV/API.

**Evidence — Tier T2 (and this is the honest ceiling)**
- Syracuse University, which housed TRAC for **more than 30 years**, **took the website down**; the data
  is no longer available on the university's site, and the immigration databases moved to a separate site
  at **tracreports.org** — https://www.houstonchronicle.com/news/houston-texas/immigration/article/trac-syracuse-data-20066522.php
  (accessed 2026-08-27). The stated cause was an audit dispute over the financial relationship between
  TRAC and TRAC Reports, Inc., not a data-access problem.
- The raw substrate — EOIR's case-by-case FOIA data release — remains a US Government public-domain
  bulk publication.

**The clock:** the takedown itself (2025). An unusual shape: **the opening was created by a refiner
disappearing, not by data appearing.**

**Why I am submitting it anyway, with low confidence:** Gate 2 requires that money already moves. I could
**not verify that TRAC ever charged a price**, and I could not verify what immigration attorneys pay for
comparable case analytics. Without that, this sits on T2 (a visibly stranded user population) and cannot
carry a candidate alone under this cycle's rules.

**Gate check**
- **G1 — PLAUSIBLE, UNPROVEN.** Immigration attorneys, journalists and researchers are exceptionally
  visible and self-organised online, and the loss was publicly discussed. No named ten.
- **G2 — FAIL AS EVIDENCED.** No confirmed price for the refined artifact. **This is the gate that kills
  it unless someone verifies TRAC's subscription pricing and any commercial competitor.**
- **G3 — PASS.** EOIR bulk FOIA data is public domain; the work is ingestion and entity resolution.
- **G4 — PASS.** Reproduce three of TRAC's headline statistics from raw EOIR data and check them against
  TRAC's last published figures. Solo, two weeks, hard number.
- **G5 — PASS.** Dated to the takedown.

**Price signal: UNVERIFIED.** Do not advance without it.

**Confidence: 4/10.**

---

## KILL LIST — checked and killed fast, with the reason

| # | Candidate | Clock checked | Killed on | Reason |
|---|---|---|---|---|
| K1 | **US building permit data products** | — | G5, G1 | No recent opening. **Shovels** already ingests **170M+ permits / 3M contractors / 2,770+ jurisdictions** and is third-party-reported at **~$599/mo** (https://permit-stack.com/blog/building-permit-data-api-pricing-compared.html). The long-tail ingestion *is* the moat and it is already built. |
| K2 | **SEC Form N-PORT monthly public holdings** | Amendments adopted Aug 2024 | G5 | **Compliance delayed to 17 Nov 2027** (≥$1bn fund groups) and **18 May 2028** (below $1bn) — https://www.federalregister.gov/documents/2025/04/22/2025-06861/. The clock is outside the window. |
| K3 | **PACER / free federal court records** | Open Courts Act of 2026 (S.4667), introduced June 2026 by Kennedy & Wyden | G5 | **A bill is not a clock.** A near-identical bill stalled in 2020. PACER still charges $0.10/page. Nothing has opened. |
| K4 | **UK Find Case Law bulk judgments** | Service launched 2022 | G4, G3 | The **Open Justice Licence permits commercial use but explicitly "does not permit computational analysis"** — bulk programmatic extraction requires a **separate licence application** to The National Archives (caselawlicence@nationalarchives.gov.uk). https://caselaw.nationalarchives.gov.uk/re-use-find-case-law-records. **The decisive step is a stranger granting permission → Standing Law 3.** |
| K5 | **UK Companies House small-company P&L accounts** | ECCTA 2023 | G5 | Genuinely enormous (revenue and profit for millions of small companies for the first time) but **introduced April 2028**, and small/micro companies **get an opt-out from publication** whose mechanism is still undefined. https://changestoukcompanylaw.campaign.gov.uk/changes-to-accounts/. **→ WATCHLIST, re-check Q3 2027.** |
| K6 | **Tariff-stack / landed-duty lookup (2025–26 tariff churn)** | Continuous EO churn through 2025–26 | G2 | The refined artifact is **already free and abundant** — Gateway Lines, The Trade Lab, DutyGlobal, Greenwich Mercantile, TariffsTool and CargoTrans all publish free stacking calculators as lead magnets for forwarding/customs services. Money moves *around* the calculator, not *for* it. |
| K7 | **Local-government meeting monitoring, horizontal** | ASR cost collapse | G1 | Adequate competitor. **Cloverleaf AI** already does video → transcript → next-day keyword alerts, and sells the same way Curate/FiscalNote and Starbridge do: quote-only, to B2G sales and government-affairs teams. We cannot run that motion. (Surviving fragment kept as C3.) |
| K8 | **Hospital price transparency / payer MRF refinement** | CMS rule changes + Feb 2025 EO | G1 | Turquoise Health, Serif Health and Payerset already ingest terabyte-scale MRFs and sell to payers, hospitals and employers — all enterprise procurement. Not resurveyed in depth; killed on distribution shape. |

---

## LEADS I COULD NOT VERIFY — hand these to whoever still has search budget

My WebSearch budget hit its 200-call session cap partway through. These are specific, checkable, and I
believe at least two are worth 30 minutes each:

1. **CMS-0057-F prior-authorization public metrics.** Belief (**UNVERIFIED — do not act on this until
   confirmed**): impacted payers — Medicare Advantage, Medicaid/CHIP managed care, and FFE qualified
   health plans — must **publicly post prior-authorization approval/denial rates, appeal outcomes and
   decision times on their websites, first due 31 March 2026**, annually thereafter. If true, that is a
   brand-new public dataset scattered across hundreds of payer websites in HTML and PDF — textbook
   hostile raw form. **Verify the date and the exact required fields in the CMS-0057-F final rule.**
   Buyer question to answer: does anyone below enterprise scale pay for denial-rate benchmarking?
2. **European Single Access Point (ESAP).** Regulation (EU) 2023/2859 established a single free API for
   EU corporate and financial disclosures, with a phased start believed to be **10 July 2026**.
   **Verify whether phase 1 is actually live and what it contains.** If live, it is six weeks old.
3. **USPTO design-mark image bulk availability** — the single load-bearing unknown under C1.
4. **Procurement Act 2023 debarment list and contract-performance/KPI notices** — do they exist yet, how
   many entries, and is anyone reselling them? My gov.uk URL 404'd.
5. **NAIC Property & Casualty Market Intelligence Data Call** — first-ever national ZIP-code-level
   homeowners insurance non-renewal, premium and claims data, believed released January 2025. **Verify
   release, granularity, and redistribution terms.**
6. **Stotles' current free tier.** If Stotles gives away pre-tender pipeline signals for free, C2 dies.
7. **Tenders Direct's live pricing page** (403s to automated fetchers — needs a browser).
8. **TRAC Reports' historical subscription pricing** — the gate that decides C8.

---

## HONEST NOTES ON MY OWN OUTPUT

- **I could not name the first ten users for a single candidate.** Under Gate 1 as written
  (*"You must be able to name actual people, handles, repos, storefronts or threads"*), that means
  **no candidate on this page has passed Gate 1.** I am reporting them as leads with clocks and price
  anchors, not as cleared candidates. The next pass on any of these should start by building that list,
  and should abandon the candidate if the list cannot be built.
- **Several prices here are third-party-reported, not read off vendor pricing pages** (Corsearch,
  Markify, BidPrime, Shovels, Tenders Direct). I have marked each. Vendor pricing pages for
  gridstatus.io, Tenders Direct and Transect all returned HTTP 403 to automated fetching — they need a
  real browser.
- **Licensing was checked where it mattered and is clean on two:** USPTO data (US Government work,
  public domain) and FSQ OS Places (Apache 2.0, commercial use explicit). It is **unresolved** on
  Find a Tender (believed OGL v3.0), NISAR (ISRO co-ownership), Overture places (believed
  CDLA-Permissive-2.0), and **actively hostile** on UK Find Case Law (computational analysis needs a
  separate licence) and on municipal meeting video (platform ToS).
- **The structural finding is the most valuable thing on this page:** on this surface, a dataset opening
  is a *cost reduction for the incumbent who already sells the refined artifact*, far more often than it
  is an opening for a new entrant. The open-data candidates that clear Gate 2 almost all fail Gate 1 for
  the same reason — the people who pay four figures for a refined public dataset are institutions, and
  institutions require a sales motion we do not have. **The only shapes that survive are the ones where
  the artifact is itself the advertisement and the buyer arrives through search** — which is why C1 is
  ranked first despite having the weakest clock.

---

**Ranked for follow-up:** C1 (trademark image clearance) → C2 (UK Procurement Act pre-tender) →
C4 (POI diffing — cheapest kill test, run it first, two days) → C3 (meeting video, vertical only) →
C8 (TRAC vacuum, only if pricing verifies).
