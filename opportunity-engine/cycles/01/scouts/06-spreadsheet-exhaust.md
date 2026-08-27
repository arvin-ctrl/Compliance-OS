# SCOUT 06 — SPREADSHEET EXHAUST

**Surface:** High-volume manual workflows that visibly run on Excel/Google Sheets, evidenced by paid
template sales, tutorial view counts, courses, forum threads, and consultants selling the setup.
**Date of research:** 2026-08-27
**Verdict on the surface:** **PARTIALLY DRY — loud but mostly colonised.** 6 candidates worth carrying
forward, 2 flagged as thin, 9 killed outright. See "Surface Assessment" at the end — the meta-finding
matters more than any single candidate.

---

## METHOD AND ITS LIMITS — READ THIS BEFORE TRUSTING ANY NUMBER BELOW

Evidence was gathered three ways: (a) the session WebSearch tool, (b) direct page fetch, (c) a scraper
against YouTube's `ytInitialData` for exact view counts.

**Sources that were bot-blocked this session and therefore could NOT be used for primary evidence:**

| Source | Result | Consequence |
|---|---|---|
| etsy.com | HTTP 403 to fetch, curl, and reader-proxy | **Could not verify a single Etsy price or review count directly.** Any Etsy figure below is quoted from a search-engine summary and marked as such |
| reddit.com / old.reddit.com (incl. `.json`) | HTTP 403 | No thread scores, no dated recurring-thread counts |
| practicalmachinist.com | HTTP 403 | Thread **titles and URLs** captured via search index; **post bodies, reply counts and view counts not verified** |
| stackoverflow.com, fiverr.com, upwork.com, ebay.com, creativemarket.com, ko-fi.com, udemy.com | HTTP 403 | No gig prices, no "orders in queue", no course enrolment counts |
| Bing, Brave, Mojeek, DuckDuckGo, SearXNG instances, Google | blocked, JS-walled, or geo-mis-routed | No fallback search once the WebSearch budget was exhausted at 200/200 calls session-wide |

The proxy itself was clean (`recentRelayFailures: []`) — these are destination-side bot walls, not
egress policy.

**What this means:** the brief's single strongest requested signal — *"the template's price and sales
count with URL"* on Etsy/Gumroad — is the signal I was **least** able to capture. Every T1 figure below
comes from an independently-hosted seller store or a vendor pricing page that was actually fetched.
Where I have no number, I write `UNVERIFIED` rather than estimating. **There are no invented numbers in
this file.**

---

## THE SIX-POINT VERBATIM T1 BASE (all directly fetched 2026-08-27)

These are the prices people are actually paying for spreadsheets and spreadsheet-replacements. They
anchor every candidate below.

| Product | Verbatim price | Verbatim social proof | URL |
|---|---|---|---|
| Janitorial Bidding Calculator (Method Clean Biz) | **"$297 one-time purchase with lifetime access"** | **"used by over 170,000 cleaning professionals over the past 10 years"** | https://methodcleanbiz.com/janitorial-bid-calculator/ |
| Janitorial Bid Template & Forms packet (The Janitorial Store) | **"Non-Member: $67.00 / Member: FREE"** | 3 named testimonials incl. *"Potential customers have been so impressed by the bid packet that it has won contracts that I might not have gotten previously."* | https://www.thejanitorialstore.com/products/janitorial-bid-template-662.cfm |
| Etsy Seller Spreadsheet (Paper + Spark) | **"$97.00 USD (one-time purchase)"** | **"118 reviews \| 98% positive (116 five-star ratings)"** | https://shop.paperandspark.com/products/etsy-seller-spreadsheet |
| Floral Pricing & Ordering Spreadsheet 2.0 (Mulberry & Moss) | **"$75.00 USD"** | **"7 reviews with 100% five-star rating"** | https://shopmulberryandmoss.com/products/copy-of-floral-business-tools-bundle |
| Someka Excel templates (sample of catalogue) | Procurement KPI Dashboard **$39.95–$79.95** (4.55/5) · Sales Pipeline **$34.95–$69.95** (4.60/5) · Balance Sheet **$29.95–$59.95** (4.63/5) · Mileage Log **$29.95–$59.95** (4.50/5) | ratings shown per product | https://www.someka.net/products/etsy-seller-excel-template/ |
| Etsy Business Tracker (Templatables, own store) | **"$8.00 (reduced from $13.00)"** | **"28 reviews"** | https://www.templatables.com/en-us/products/etsy-small-business-tracker-google-sheets |

**The headline fact of this surface:** a *single* spreadsheet-based bid calculator for cleaning
contractors sells at **$297 one-time** and claims **170,000 users over ten years**. That is direct,
verbatim, T1 proof that small-business owners will pay three figures, self-serve, with no sales call,
for a piece of pricing math delivered as a spreadsheet.

---

# CANDIDATE 1 — Micro Job-Shop Quote Engine

**One sentence:** A quoting tool for 1–10-person CNC and fabrication shops that turns an RFQ into a
costed, defensible quote in minutes, priced for a shop that will never take a demo call.

### 2. The artifact
A quote PDF the shop sends the customer, plus the thing behind it: a **versioned rate card** (machine
rates, labour burden, setup vs run time, material with markup ladder, tooling amortisation, finishing,
outside processes, minimum lot charge) that produces a line-itemised cost build-up, a quantity-break
table (1/10/50/100 without re-keying), and a saved quote history so "what did we quote this part at in
2024?" is answerable.

### 3. Evidence

**T1 — money moving now for a worse version:**
- **Paperless Parts** — the incumbent — has raised, per aggregator profiles, **$51.1M total**, including
  a **"$30M Series B Funding Led by OpenView Partners"** announced **13 September 2021**
  (https://www.businesswire.com/news/home/20210913005163/en/Paperless-Parts-Announces-30M-Series-B-Funding-Led-by-OpenView-Partners)
  and a Series C of $5M dated 22 December 2023 (aggregator-reported — treat the $51.1M and Series C as
  `UNVERIFIED` against a primary filing). Pricing is **demo-gated with no public price**
  (https://www.paperlessparts.com/pricing/). A third-party pricing-estimate site put a 50-user
  mid-size manufacturer at ~$150,000/year — **explicitly `UNVERIFIED`, an estimate, not a quoted price.**
- **Machine Research** also publishes **no price** — "book a demo" only (https://machineresearch.com/).
- Etsy listing **"CNC Quote Calculator – Machine Shop Job Cost Estimator Excel Template | Accurate
  Pricing Tool"** (https://www.etsy.com/listing/4469106868/) exists — **price and sales count
  `UNVERIFIED`, Etsy was 403 to every fetch method.**

**T2 — humans doing it manually at volume, visibly:**
- **CNCCookbook quoting survey**, n=100, page last modified **9 March 2024**
  (https://www.cnccookbook.com/job-quote-cost-estimation-survey-results/). Verbatim: spreadsheets are
  **"the number one player by a wide margin"**, followed closely by **"Eyeball Guestimate"**; and
  **"today's solutions are too inaccurate and time consuming."**
- **Paperless Parts' own blog** (https://www.paperlessparts.com/blog/where-can-i-find-the-best-spreadsheet-template-for-quoting-parts/):
  shops using spreadsheets rate their process **"around 5 out of 10"**, one describing it as merely
  **"It's fine"**; ERP-based quoting scored **~6.5 out of 10** — *only marginally better*. The company
  describes its own product as **"an Excel Macro on steroids."**
- **Machine Research** homepage, verbatim: **"Spreadsheets and outdated software just can't keep up"**,
  and a **"52% higher chance of winning the work"** claim for faster RFQ response.
- **YouTube view counts (exact, scraped 2026-08-27):**
  - NYC CNC — *How I Quote CNC Machining and Machine Shop Work* — **160,685 views**
  - TITANS of CNC — *How to Build a CNC Machine Shop - Part 2 (Quoting - Learn the Secret)* — **155,796 views**
  - NYC CNC — *How to Quote Jobshop Work - How Much to Charge?* — **98,878 views**
  - **Practical Machinist — *Every Machine Shop Makes This Quoting Mistake | Machine Shop Talk Ep.155* — 53,361 views, published ~2 months ago (≈June 2026)**
  - NYC CNC — *Quoting Job Shop Work: Charge for Custom Tooling?* — **25,326 views**
- **Recurring, specific, dated forum threads** (titles/URLs from search index; bodies `UNVERIFIED`):
  - `.../built-a-free-quoting-calculator-to-get-off-my-spreadsheet-would-love-you-guys-to-tear-it-apart.449764/` — **dated ~July 2026** in the search summary
  - `.../whats-your-shop-rate-these-days.368039/`
  - `.../job-shop-quoting-charging.391807/`
  - `.../quoting-change-of-quantities.440099/`
  - `.../quoting-issues.367319/`
  - `.../quoting-work-how-do-you-do-it.218165/`
  - `.../quoting-jobs.208021/`
  - `.../what-is-in-a-quote.298090/`
  - cnczone.com `/forums/general-metalwork-discussion/42072-quote-job.html`

  Verbatim fragments surfaced from those threads: a machinist *"tells customers they're at $65/hr, but
  recently using $75-85/hr on their quote spreadsheet"*; another has *"a spreadsheet listing common
  operations for each machine that calculates material markups, tooling costs, setup times, subcontract
  markups, and shipping costs"*; the July 2026 poster *"has been quoting off a homemade spreadsheet for
  years but noted issues like inconsistent numbers and forgetting minimum lot charges."*

### 4. The clock
**Weakest part of this candidate — the clock is soft.** What I can date: Paperless Parts' partnership
with **Hexagon** (2024, https://hexagon.com/company/newsroom/press-releases/2024/hexagon-and-paperless-parts-slash-quoting-times-for-americas-precision-manufacturers-with-advanced-software-solutions)
pushed the incumbent further into ITAR/CMMC aerospace-and-defence territory and further from the
three-person shop. And **July 2026**: a shop owner shipped a free quoting calculator on Practical
Machinist to get off his own spreadsheet — the segment is being probed right now and is not captured.
I did **not** find a regulatory or platform change that opens this. Score this gate honestly as weak.

### 5. First ten users
**Named and findable.** The July 2026 Practical Machinist thread 449764 is direct proof that posting a
free quoting calculator into that forum gets engagement from the exact buyer. Named venues with named
threads: the eight Practical Machinist thread URLs above, cnczone thread 42072, and the comment sections
of NYC CNC, TITANS of CNC MACHINING and Practical Machinist's own channel. **I did not enumerate ten
named individuals** — I have venues and threads, not handles.

### 6. Gate check
- **G1 cold-start distribution — PASS.** A public forum where a competitor's free tool was posted in
  July 2026 and drew discussion. Self-serve price point. No sales motion required.
- **G2 observable demand — PASS.** T1 (a $51M-funded incumbent charging enterprise money) + T2 (n=100
  survey saying spreadsheets dominate; ~500k combined tutorial views; 8+ recurring dated threads).
- **G3 buildable by us — PASS with a scope caveat.** Rate-card + cost build-up + quantity breaks is
  plain software. **3D geometry/feature recognition from STEP files is the hard part and must be cut
  from v1** — v1 takes manual operation entry, which is what the spreadsheets already do.
- **G4 self-verifiable in 14 days — PASS.** Build the calculator, post it in the same forum the July 2026
  poster used, count sign-ups. No stranger's cooperation needed.
- **G5 the clock — WEAK/FAIL.** No dated change in 24 months that opens this. Carry forward, but this is
  the gate that should worry us.

### 7. What already exists
**Paperless Parts** — closest competitor. Inadequate for this buyer because: pricing is demo-gated with
no public number; positioning is ITAR/CMMC/aerospace-defence; it assumes a shop with a dedicated
estimator. **Machine Research** — same shape, demo-gated. **G-Wizard Estimator** (CNCCookbook) exists as
a cheap tool but its pricing page did not render — `UNVERIFIED`. Verdict: the category's upper half is
owned; the 1–10 person shop is priced and positioned out.

### 8. Price signal
Comparable self-serve trade calculators clear **$297 one-time** (janitorial, verified). Incumbent
enterprise pricing is unpublished. A defensible test price is **$29–79/month or $199–349 one-time**.

### 9. Confidence: **6/10**
Strong demand evidence and a genuinely reachable audience; the clock is the problem and the enterprise
incumbent may come downmarket.

---

# CANDIDATE 2 — Cleaning Contract Bid-vs-Actual P&L

**One sentence:** For commercial cleaning company owners, the thing that tells them which of their
accounts is actually making money — bid hours versus the hours their crews really worked, per account,
every month.

### 2. The artifact
A per-account monthly profit sheet: bid production hours vs actual clocked hours, labour cost vs bid
labour, supplies drawn vs supplies allowed, and a red/amber/green list of accounts that have drifted
below the margin they were bid at — with the specific line that caused the drift.

### 3. Evidence

**T1 — strongest on this whole surface, and fully verified:**
- **Method Clean Biz Janitorial Bidding Calculator**: **"$297 one-time purchase with lifetime access"**,
  **"used by over 170,000 cleaning professionals over the past 10 years"**
  (https://methodcleanbiz.com/janitorial-bid-calculator/, fetched 2026-08-27). This is a **spreadsheet
  calculator**, sold at a three-figure price, to a six-figure user base, self-serve.
- **The Janitorial Store** bid packet: **"Non-Member: $67.00 / Member: FREE"** — i.e. the templates are
  the funnel and a paid membership ("Pro & Premium Members", 14 bidding calculators behind it) is the
  product (https://www.thejanitorialstore.com/products/janitorial-bid-template-662.cfm and
  https://www.thejanitorialstore.com/public/Bidding-Calculators.cfm).
- Etsy **"Commercial Janitorial Bidding Calculator"** (https://www.etsy.com/listing/1552492212/) — price
  and review count `UNVERIFIED` (Etsy 403).

**T2 — exact YouTube view counts, scraped 2026-08-27:**
- OctoClean Media — *How to Bid Commercial Cleaning Jobs (FORMULA INCLUDED)* — **150,981 views**
- Cleaning Launch — *How To Price Your Commercial Cleaning Services THE RIGHT WAY* — **83,490 views**
- Ricky Funk — *How to calculate PROFIT / OVERHEAD / LABOR COST [CLEANING INDUSTRY]* — **79,872 views**
- AJ SIMMONS — *How To Bid Cleaning Jobs Per Hour Or Per Sqft* — **72,946 views**
- Johnny & Sergio — *How To Price Residential CLEANING Services (Step by Step Guide)* — **60,721 views**
- AJ SIMMONS — *How To Get A Commercial Cleaning Contract in 30 Days or Less* — **48,991 views**
- The Janitorial Store — *How to price a 2,400 square foot office space* — **32,126 views**
- OctoClean Media — *How to Create a Kickass Commercial Cleaning Proposal* — **28,136 views**
- AJ SIMMONS (1 year ago) — *How To Bid Commercial and Residential Cleaning Jobs (Formula Included)* — **23,760 views**
- Cleaning Launch — *How To PRICE COMMERCIAL CLEANING Contracts In 2025 [Secret Formula]* — **10,070 views**

  **Roughly 590,000 combined views on "how do I price a cleaning job" alone.**

**Why a spreadsheet is genuinely the wrong tool here — and this is the important distinction:**
The *bid* is fine in a spreadsheet. One bid, one sheet, done — which is exactly why the $297 calculator
sells and works. **The spreadsheet dies after the bid is won.** Bid-vs-actual requires (a) time data
from many cleaners on many sites, (b) a monthly recomputation across a growing portfolio, (c) more than
one person touching the file — the owner, whoever runs payroll, sometimes a supervisor. At roughly
ten-plus accounts the sheet becomes a stack of tabs nobody reconciles, and owners discover a loss-making
account only when the year's numbers land. That is the software wedge, not the bid calculator.

### 4. The clock
**FAIL — I found no dated change in the last 24 months.** Labour cost inflation is a pressure, not a
clock, and I did not verify it with a dated source. Marked honestly as a fail rather than dressed up.

### 5. First ten users
Named venues, not named individuals: the YouTube channels above (AJ SIMMONS, Cleaning Launch, OctoClean
Media, Johnny & Sergio, Mike Mak, The Janitorial Store) all run active comment sections of owner-operators;
The Janitorial Store runs a paid member community. The $297 calculator's existence proves this buyer
purchases self-serve without a call. **I could not name ten individuals.**

### 6. Gate check
- **G1 — PASS.** Proven self-serve purchase behaviour at $297; large, public, creator-led communities.
- **G2 — PASS (T1, verified).** 170,000 users × $297 list is money moving for a spreadsheet.
- **G3 — PASS**, with one dependency: actual hours must come from somewhere. v1 accepts a CSV/photo of a
  timesheet rather than building time-tracking.
- **G4 — PASS.** Build it, post it, count sign-ups.
- **G5 — FAIL.** No clock.

### 7. What already exists
**Janitorial Manager, CleanTelligent, Swept**, and **Aspire** (ServiceTitan-owned) all serve janitorial
operations. Pricing not verified this session. **Honest assessment: this category is partially owned.**
The gap I believe is real is the owner with 3–15 accounts who finds those platforms too heavy and is
currently paying $297 for a calculator instead. That belief is not yet evidenced — it is the thing a
14-day test would have to prove.

### 8. Price signal
**$297 one-time, verified.** Plus a membership model (The Janitorial Store) whose price I could not read.

### 9. Confidence: **6/10**
Best T1 evidence on the surface; no clock; incumbents exist and I could not price them.

---

# CANDIDATE 3 — WH-347 Certified Payroll Generator for Small Subcontractors

**One sentence:** For a 5–25-person subcontractor on a federally funded job, a tool that turns the
payroll they already ran into the weekly WH-347 certified payroll report and the state variants, without
re-keying every employee twice.

### 2. The artifact
A signed, submission-ready **WH-347 + WH-348 Statement of Compliance** per week per job, generated from
a payroll export (QuickBooks/Gusto/ADP CSV), with per-classification hour splits, fringe benefit
treatment, and a matching upload file for the agency portal the GC demands.

### 3. Evidence

**T1:**
- **eBacon** (https://www.ebacon.com/) sells exactly this to **small-to-mid construction contractors**.
  Verbatim customer claim on its homepage: **"We have gained back 16-20 hours that we can dedicate to
  running our business."** Case studies reference contractors scaling **"from $500K to $2M in municipal
  contracts."** **No public pricing.**
- **Points North Certified Payroll Reporting** and **LCPtracker** exist in the category (LCPtracker sold
  to public agencies, which then force subs onto it). Pricing `UNVERIFIED` — the Points North page 404'd.

**T2:**
- Etsy: **"Automated WH-347/348 Davis-bacon EXCEL Payroll Template With 167 Autofill Fields!"**
  (https://www.etsy.com/listing/1552421135/) — description verbatim from search index: worksheets
  *"autofill 107 fields and allow manual entry of FICA and Withholding, pulling all data from the same
  Tables1 worksheet."* **Price and sales count `UNVERIFIED`.** The existence of a 167-autofill-field
  Excel template is itself the tell: someone built a small application inside a spreadsheet because no
  affordable software did it.
- YouTube: *Completing a Certified Payroll Report* (Power Summit) — **165,582 views**; Alliant Consulting
  — *How To Complete the WH-347 Form* — **12,353 views** (1 year ago).

**Why the spreadsheet is genuinely wrong:** weekly cadence × every employee × every classification they
worked that week × fringe treatment × a legally-binding signature. It is a *filing*, not a calculation,
and it is wrong in a way that carries penalties. Multiple people touch it (payroll clerk, owner who
signs, GC who rejects it).

### 4. The clock
**PARTIALLY VERIFIED — and probably too old.** The DOL Davis-Bacon final rule took effect **23 October
2023** (~34 months ago) and the IRA prevailing-wage/apprenticeship final regulations published **June
2024** (~26 months ago) — **both fall outside the brief's 24-month window**, and I could not verify
either date from a primary source this session (federalregister.gov redirected to an unblock page;
trade.gov 404'd). **Do not treat the clock as established.**

### 5. First ten users
**COULD NOT FIND THEM.** Construction subcontractors do not congregate in a public, fetchable forum I
could reach (Reddit 403). This is the candidate's fatal-looking problem.

### 6. Gate check
- **G1 — FAIL (probable).** No named cold-start channel found. This buyer is normally reached through
  GCs, agencies, or payroll resellers — all sales motions.
- **G2 — PASS.** Incumbents charging real money; a 167-field Excel template in the wild; 165k tutorial views.
- **G3 — PASS.** Form generation from a payroll CSV is squarely buildable.
- **G4 — PASS.** We can build and self-test against the published WH-347.
- **G5 — FAIL/UNVERIFIED.** Clock dates outside 24 months and unverified.

### 7. What already exists
eBacon (payroll-service-shaped, so it requires *being* a payroll provider — a much bigger build than
form generation), Points North, LCPtracker, Payroll4Construction. Category is served at the top; the
5-person sub filing by hand is the gap.

### 8. Price signal
`UNVERIFIED` — every vendor in the category hides pricing.

### 9. Confidence: **4/10**
**Recommend killing on G1 unless someone can name the channel.** Included because the workflow evidence
is strong and the artifact is unusually crisp; excluded from any build recommendation.
**Adjacency note:** this is construction, but it is *payroll compliance*, not claims/entitlement, notice
deadlines, Procore-layered tooling, clause extraction, or delay attribution — so it is not a re-submission
of anything in `LEDGER.md`.

---

# CANDIDATE 4 — Plate-Cost Engine for Single-Unit Independent Restaurants

**One sentence:** Recipe and menu costing for the independent restaurant or café that re-prices itself
when supplier invoice prices move, aimed below the price floor the incumbent charges.

### 2. The artifact
A live menu-margin sheet: every dish costed from current invoice prices, flagged when a dish crosses a
target food-cost percentage because an ingredient moved, with the specific ingredient named.

### 3. Evidence

**T1 — the price floor is verified and it is high:**
- **MarginEdge**: verbatim **"$350 per location per month"** (or **"$500 per month per location"** bundled
  with Freepour), including **"Recipe costing"**, **"Recipe management with robust menu analysis"**,
  **"unlimited invoices processed (for everyone)"** and **"Product price monitoring & alerts"**
  (https://www.marginedge.com/pricing, fetched 2026-08-27).
- A dense population of paid Etsy templates in this exact niche — *Recipe Cost Calculator Excel Template,
  Baker Profit Tool* (listing 1786495395), *Recipe Cost Template Excel & Google Sheets* (4335403660),
  *Recipe Cost Calculator Google Sheets* (1563215737), *Excel Template | Recipe/baked Goods Cost
  Calculator* (860574895). **Prices and review counts all `UNVERIFIED` — Etsy 403.**
- Craftybase publishes a free bakery costing spreadsheet as lead-gen
  (https://craftybase.com/resources/bakery-costing-spreadsheet) — i.e. a funded vendor uses the
  spreadsheet as the hook, which is itself evidence the spreadsheet is the incumbent behaviour.

**T2:** RestaurantSystemsPro — *How to Calculate Restaurant Cost of Goods Sold* — **34,520 views**;
Dave Allred TheRealBarman — *How to Count Food Inventory Like a Pro* — **44,490 views** and *Bar
Inventory [How to Count Open Liquor Bottles]* — **42,817 views**.

**Why the spreadsheet is genuinely wrong:** the cost basis changes weekly and comes in as invoices, not
as typed numbers. A static recipe sheet is correct on the day it is built and quietly wrong for the next
eleven months. That is a data-freshness problem, which is software's job, not a spreadsheet's.

### 4. The clock
**FAIL — none found.** Food-cost inflation is a condition, not a dated change.

### 5. First ten users
**COULD NOT FIND THEM.** No fetchable public venue where independent restaurateurs congregate
(Reddit 403). Etsy template buyers exist but are not reachable.

### 6. Gate check
- **G1 — FAIL.** No named channel. Independent restaurants are famously the hardest self-serve SaaS buyer.
- **G2 — PASS.** $350/location/month incumbent + a dense paid-template market.
- **G3 — PASS.** Invoice parsing → ingredient price → recipe rollup is well within capability.
- **G4 — PASS.**
- **G5 — FAIL.** No clock.

### 7. What already exists
**MarginEdge at $350/location/month** — genuinely good, and genuinely unaffordable for a single café.
Also xtraCHEF (Toast), MarketMan, Restaurant365, meez, Craftybase. **Honest read: the category is served
above ~$350/mo and flooded with $10 templates below it; the middle is empty for a reason nobody has
proven is a good reason.**

### 8. Price signal
Templates in the ~$10–30 band (`UNVERIFIED`); incumbent software **$350/location/month** (verified).

### 9. Confidence: **4/10** — carried for completeness; G1 is the killer.

---

# CANDIDATE 5 — Live Cost-Per-Hour Engine for Solo Trades

**One sentence:** The number every one-person trade business gets wrong — what one hour of their own
time actually costs once overhead, unbillable time, and equipment are loaded in — kept current instead
of computed once and forgotten.

### 2. The artifact
A single defensible hourly rate, recomputed as costs change, that flows into every estimate the operator
writes — plus the break-even it implies (billable hours needed per week) and a warning when a quoted job
falls below it.

### 3. Evidence

**T2 — this is the single highest-volume "spreadsheet exhaust" signal I measured:**
- Ian Johnson — *Calculating Hourly Rates for a Contractor or Small Business* — **966,415 views**
- Contractor Fight TV — *What's It Cost You To Operate Your Business For One Hour* — **84,389 views**
- Ricky Funk — *How to calculate PROFIT / OVERHEAD / LABOR COST [CLEANING INDUSTRY]* — **79,872 views**
- PHCC Educational Foundation — *Overhead and Profit Calculator Webinar* — **57,022 views**
- Intuit QuickBooks — *How to calculate and track overhead costs for your business* — **52,306 views**
- Lawn Care Millionaire — *Fixed Overhead Per Man Hour Calculation Explained* — **33,965 views**

Adjacent per-trade pricing demand (exact counts, same scrape): pressure washing **321,285 / 199,537 /
123,123 / 108,657 / 93,222 / 78,029 / 46,119**; landscaping **248,802 / 185,605 / 78,112 / 60,756 /
57,506 / 53,897 / 43,277 / 40,010**; snow removal **125,827 / 114,052 / 109,813 / 100,937 / 58,835 /
47,647**; painting **138,591 / 108,585 / 67,562 / 66,281**; general contractor estimating **426,811**
(Jesse Lane, *How to Estimate Construction Projects as a General Contractor *Excel Spreadsheet**).

**T1:** the $297 janitorial calculator (verified above) is the same product shape for one trade —
proof that this exact calculation sells at a three-figure price. Etsy **"Job Estimate Spreadsheet
Excel"** (listing 1743631875) markets on the claim, verbatim from the search index, that *"between 50-70%
of skilled trades businesses underprice their jobs"* — **a seller's own marketing claim, not a verified
statistic; do not repeat it as fact.**

### 4. The clock
**FAIL — none found.**

### 5. First ten users
Named channels with active owner-operator comment sections (Keith Kalfas, Mike Andes, Brian's Lawn
Maintenance, Contractor Fight TV, AJ SIMMONS, Pressure Washing Pastor). **No named individuals.**

### 6. Gate check
- **G1 — PARTIAL PASS.** Enormous, public, creator-led audiences; proven $297 purchase behaviour. But
  reaching them means being the person in the comments, which is slow.
- **G2 — PASS.** ~2.9M combined views across trade-pricing tutorials, plus a verified $297 T1.
- **G3 — PASS** (trivially — this is arithmetic plus good UX).
- **G4 — PASS.**
- **G5 — FAIL.**

### 7. What already exists
**Jobber is actively colonising exactly this content niche** — its own videos rank in these searches
(*How to Estimate Painting Jobs (With 50% Profit Margin)* **40,592 views**; *How to Price Pressure
Washing Jobs* **108,657 views**). Jobber sells scheduling/CRM/invoicing, not a cost-per-hour engine, so
the *product* gap is real — but a well-funded incumbent is already buying the attention.
**Honest caveat: a cost-per-hour calculator is a feature, not a company.** It is a wedge, and should
only be pursued as the front door to Candidate 1 or 2.

### 8. Price signal
**$297 one-time** (verified, janitorial); **$67** for a template packet (verified).

### 9. Confidence: **5/10** — huge demand, thin product, no clock. Wedge only.

---

# CANDIDATE 6 — Manufacturer's-Rep / Small-Agency Commission Statement Reconciliation

**One sentence:** For a small sales-rep agency paid by a dozen different manufacturers, the tool that
checks each incoming commission statement line-by-line against what was actually owed and flags what is
missing.

### 2. The artifact
A monthly exception report: every order that should have paid commission and didn't, every rate that
came in below the agreement, every split misallocated — with the dollar amount and the statement it came
from, ready to email the manufacturer.

### 3. Evidence

**T1 — an entire vendor category exists, which proves the money but also weakens the case:**
- **dynaMACS** sells a dedicated **Commission Reconciliation Module**
  (https://www.dynamacs.com/optional-modules/commission-reconciliation/) whose described job is to
  *"reconcile the commission statements received from their manufacturers, against the invoices in the
  system"*, with an *"Auto Apply that pays full balances from the first open invoice forward, until the
  check balance is zero."*
- **MRSware**, **Repfabric** (*"importing manufacturer sales and commission statements from Excel"*), and
  **Flow RMS** — the last describing itself as an *"AI-First Operations Platform for Manufacturer Sales"*
  — all target the same buyer. Verbatim from the category's own marketing: **"Most rep firms run on a
  patchwork of spreadsheets, shared drives, and disconnected tools."** All prices `UNVERIFIED`.
- Parallel category in insurance: **Commission Tracker**, **CommissionIQ**, **Neudash**
  (*"Carrier Commission Statement Reconciliation for Insurance Agencies"*) — same workflow, same
  spreadsheet incumbency. Verbatim from that category: *"Missing a single carrier statement can distort
  your entire ledger"*; *"Policies simply fall off statements when a renewal misses a cycle or a policy
  number changes after an amendment."*

**Why the spreadsheet is genuinely wrong:** statements arrive as N differently-formatted PDFs/CSVs per
month, each needing to be matched against a different agreement's rate and split rules. It is a
multi-source data-matching problem — the canonical case where a spreadsheet is the wrong tool and where
LLM-based document extraction is a genuine new capability.

### 4. The clock
**PARTIAL.** **Flow RMS** positioning itself as "AI-first" for this exact buyer indicates the category is
being re-attacked *now* on the strength of document-extraction models. **I could not date its launch or
funding — `UNVERIFIED`.**

### 5. First ten users
**COULD NOT FIND THEM.** Rep agencies and insurance agencies do not congregate anywhere I could fetch.
Association-led (AIM/MANA, Big I) which is a sales motion.

### 6. Gate check
- **G1 — FAIL.** No cold-start channel found. This is the gate that kills it.
- **G2 — PASS.** Four-plus vendors monetising the workflow; explicit "patchwork of spreadsheets" framing.
- **G3 — PASS.** Statement extraction + rule matching is directly in our wheelhouse.
- **G4 — PASS**, provided we can obtain sample statements — which requires a stranger's cooperation, so
  call this **borderline**.
- **G5 — PARTIAL/UNVERIFIED.**

### 7. What already exists
dynaMACS, MRSware, Repfabric, Flow RMS (rep agencies); AgencyBloc, Commission Tracker, CommissionIQ,
Neudash (insurance). **This category is adequately served by count of vendors.** The only opening is
that the incumbents are old and the extraction step is newly cheap — not enough on its own.

### 8. Price signal `UNVERIFIED` — every vendor hides pricing.

### 9. Confidence: **4/10** — **recommend kill on G1.**

---

# FLAGGED AS THIN — DO NOT ACTION WITHOUT FURTHER VERIFICATION

### T1. Small-importer per-SKU landed cost that restacks when duty rates change
The clock *should* be excellent — the 2025–2026 US tariff regime — but **I could not verify a single
tariff date from a primary source this session**: federalregister.gov redirected to an unblock page,
trade.gov 404'd, and the White & Case tracker 404'd. The only tariff figures I saw came from a
marketing blog (*"Section 301 tariffs on Chinese goods have added 7.5%–25% ... as of 2025–2026"*) which
is **T3 at best and must not be relied on.**
What I do have: Etsy listing **"US Tariff Cost Calculator Toolkit Import Duty Spreadsheet + PDF Guide"**
(https://www.etsy.com/listing/4348370647/) — price/sales `UNVERIFIED`; a Flevy listing *"Landed Cost
Calculator for USA Imports Dashboard - Excel Template"* — price `UNVERIFIED` (403); IncoDocs *Calculate
Landed Cost Excel Template for Import Export* — **72,262 views** (8 years old, so not evidence of a
recent clock); and **Zonos** as the incumbent with **no public pricing**.
**Verdict: the idea is promising and the evidence is not there yet. One hour with a working
federalregister.gov would settle it.**

### T2. Tip-pool allocation + qualified-tip reporting prep for bars and restaurants
**The clock is the best-verified on this whole surface** — and the candidate is still weak.
Verified: **IRS Notice 2025-69**, release **IR-2025-114**, dated **21 November 2025**
(https://www.irs.gov/newsroom/treasury-irs-provide-guidance-for-individuals-who-received-tips-or-overtime-during-tax-year-2025):
the tips deduction runs **2025–2028** at **$25,000 maximum annually**, phasing out above **$150,000
MAGI**; Form W-2 is **unchanged for tax year 2025**, and the IRS is **"in the process of updating income
tax forms and instructions."** Secondary reporting (accounting-firm summaries, not primary) says
separate reporting of cash tips plus a **"tip occupation code"** lands for **tax year 2026** with
penalty relief for 2025 only — **`UNVERIFIED` against the notice text itself.**
Why it is still weak: **T2 demand is thin** (TouchBistro *3 Best Ways to Distribute Your Tip Pool*
**22,547 views**; TheRealBarman **16,221**; Tip Reports **16,039** — an order of magnitude below every
other niche here), and **the W-2 half of the job belongs to payroll providers**, who will absorb it for
free. Only the upstream *pool allocation* is unowned, and 7shifts, Kickfin and Toast are all adjacent.
**Verdict: great clock, wrong owner.**

---

## KILLED ON THIS SURFACE — with the reason and the name of who owns it

| Killed candidate | Why | Who owns it (verbatim price where verified) |
|---|---|---|
| **Employee scheduling / rostering** | Enormous demand — *How to create a work schedule in Excel* **618,830 views**, MyOnlineTrainingHub **232,284**, Chandoo **67,528**, Simple Sheets **54,121**, plus six more above 20k — and **zero** willingness to pay, because the incumbent is free | **Homebase Basic: $0/month, up to 10 employees, 1 location, "Basic scheduling," "Basic time tracking."** Essentials $30/mo. Also When I Work, 7shifts |
| **Small-business inventory management** | The single loudest signal measured — **2,087,683** views (*Stock Control Sheet In Excel*), **1,857,834** (Excel For Freelancers), **887,506**, **472,932**, **370,810**, **296,124**, **220,763**, **150,286** — and the most crowded software category in existence | Everyone. Zoho, Sortly, inFlow, Craftybase, Katana, plus every ERP |
| **Construction job costing for small subs** | Etsy *Construction Job Costing Template for Contractors* reportedly **"4.6 stars, 135 reviews"** (search-index summary, `UNVERIFIED`) and **426,811 views** on Jesse Lane's estimating video — but the software is already cheap and self-serve | **Contractor Foreman: Basic $49/month, 1 user, job costing YES, estimating YES** (verified). Also Buildertrend, Knowify, Jobber |
| **Wedding/event florist recipe & proposal costing** | The template market is real (**Mulberry & Moss $75.00, 7 reviews, 100% five-star**, verified) but the category is fully productised at a florist-affordable price | **Details Flowers Software: Starter $25/month (1 user, 3 events) → Business $150/month; Enterprise $2,250/year** — combines *"client proposals, recipes, stem counts, contracts, payments, and delivery documents in one system."* Also Curate |
| **Owner-operator trucking books / IFTA / cost-per-mile** | Strong demand (*Cost Per Mile: How to Calculate It* **146,001 views**, ET Transport **76,651**) but the software is cheaper than the spreadsheet template | **TruckingOffice: Owner/Operator (1-2 trucks) $25/month Basic, $35/month Pro**, includes mileage calculation and multi-user (verified). Also Rigbooks, TruckBytes |
| **Nonprofit grant tracking** | Every template found is **free vendor lead-gen** (Smartsheet, Knack, Jotform, Airtable, Instrumentl all give it away) — no money moves for the spreadsheet | Instrumentl, Submittable, Foundant GrantHub, Fluxx |
| **Etsy-seller / small-maker bookkeeping** | Money genuinely moves (**Paper + Spark $97.00, 118 reviews, 98% positive**, verified) but the seller's entire pitch is *"Replaces Expensive Software"* — these buyers are choosing the spreadsheet *over* SaaS on purpose | Craftybase, Inventora, QuickBooks; and Paper + Spark itself, profitably |
| **CAM / lease reconciliation for small commercial landlords** | Genuinely painful and multi-party, but I could verify **no T1 at all** — the lease-audit firm page 503'd and the only signal was **92,504 views** on a *vendor's own* CAM video (STRATAFOLIO). T4 reasoning, not evidence | STRATAFOLIO; Yardi/MRI above it |
| **Agriculture, clinical-trial-site, self-storage, vending, equipment rental, event production** | Swept for demand; all returned **below-threshold or zero** results at a 25–30k view floor. Where signal existed it was a vendor's own video (CattleMax **68,016**) | — |

---

## SURFACE ASSESSMENT — THE META-FINDING

**The spreadsheet-exhaust surface is loud, and the loudness is mostly a trap.** The pattern that repeats
across nine kills is this: *the niches with the largest visible spreadsheet exhaust are the niches where
vertical SaaS has already arrived, because the exhaust is exactly how those vendors found the niche.*
Scheduling has 618k views and Homebase gives it away free. Inventory has 2.1M views and thirty vendors.
Job costing has 426k views and Contractor Foreman charges $49. **Tutorial view count measures demand
for the workflow, not the absence of a product** — and on this surface, high view count is
anti-correlated with opportunity.

Three things did survive that filter, and they share a shape:

1. **Money moves for the spreadsheet itself at a three-figure price** — the verified **$297 / 170,000
   users** janitorial calculator, the **$97 / 118-review** Paper + Spark sheet. People paying $297 for
   arithmetic is the real T1 on this surface.
2. **The incumbent hides its price behind a demo.** Paperless Parts, Machine Research, eBacon, Zonos,
   dynaMACS, Points North — *every single serious vendor in every surviving candidate refuses to publish
   a number.* That is the tell for a segment that has been abandoned to spreadsheets because it cannot
   absorb a sales call. It is also precisely the segment a solo operator with no sales motion can serve.
3. **The workflow breaks after the calculation, not during it.** The bid is fine in Excel; bid-vs-actual
   across fifteen accounts is not. The recipe is fine in Excel; the recipe eleven months after invoice
   prices moved is not. The quote is fine in Excel; the quote history and the quantity-break rebuild is
   not. **Every genuine opportunity here was one step downstream of where the templates sell.**

**The gate that killed the most here was G5 (the clock) — six of eight candidates have no dated change
in 24 months.** That is a real structural finding about this surface: spreadsheet pain is chronic, not
event-driven, so a scouting brief that requires a clock will systematically starve on it. The one
candidate with a genuinely excellent, verified clock (tips, IRS Notice 2025-69, 21 Nov 2025) fails
because the clock belongs to payroll providers, not to us.

**Recommendation:** carry **Candidate 1 (micro job-shop quoting)** and **Candidate 2 (cleaning
bid-vs-actual)** forward. Candidate 1 is the only one on this surface that passes G1 with a *named,
demonstrated* cold-start channel — a competitor posted a free quoting calculator into Practical Machinist
in July 2026 and got engagement. Candidate 2 has the best verified T1 on the surface. Both fail G5;
whether that is disqualifying is a judgment for the operator, not for a scout.

**Re-run request:** the Etsy block cost this scout its best evidence class. If a future cycle can reach
Etsy listing pages (residential proxy, Etsy's own API, or a paid marketplace-analytics feed such as
eRank/EverBee), the sales-count evidence for Candidates 1, 3, 4 and Thin-1 becomes checkable in about an
hour, and several of the nine kills above deserve a re-test with real numbers rather than search-index
summaries.
