# 10 — FIELD DATA CAPTURE / DAILY REPORTS / SUBCONTRACTOR OPS LAYER

**Category report.** Primary: **HCSS (HeavyJob, HeavyBid)**, **eSUB**, **Raken**.
Secondary/brief: **Fieldwire (Hilti)**, **Buildertrend**, **Knowify**, **Kojo**.
Research date: 2026-08-19. All URLs fetched live unless marked otherwise.

> **Note on "HCSS Skyline":** the assignment named "Skyline" as an HCSS product. I could not verify
> that any product called Skyline exists in the HCSS portfolio. The official product index
> (https://www.hcss.com/products/, fetched 2026-08-19) lists **HeavyBid, HeavyJob, HCSS Safety,
> HCSS Plans, Equipment360, HCSS Telematics, HCSS Dispatcher, HCSS Cloud, HCSS Insights** — no Skyline.
> A `"HCSS Skyline"` exact-phrase search returned no matching product page. **UNVERIFIED / likely does not exist.**
> If it does, it is not marketed on hcss.com and is immaterial to this thesis.

---

## 0. ONE-PARAGRAPH ANSWER TO THE ORCHESTRATOR'S THREE KEY QUESTIONS

1. **Did eSUB's "document your claims" pitch work commercially?** No — not at scale. eSUB is the ONLY
   vendor in this layer that has explicitly and repeatedly marketed claim/dispute documentation to
   subcontractors (peaking with a Feb-2024 press release literally titled *"Contractors Use Documentation
   Software To Help Prevent Legal Disputes In 2024"*), and it is by a wide margin the **smallest and
   slowest-growing** company in the category: **16,000+ users / 60+ employees / ~$22–23M raised since 2008**,
   versus HeavyJob's **128,000 active users** and Raken's **70,000 users across 4,500 firms**. eSUB has also
   rebuilt its product twice (Classic → Cloud → Fusion), publishes ~5 blog posts in 18 months, and its
   current homepage says *"Hundreds of Commercial Subcontractors Rely on eSUB"* — down from *"Thousands of
   trade contractors"* in its own Feb-2024 release. **Read: the pain is real and eSUB names it correctly,
   but "better documentation" is a weak, un-urgent buying trigger that loses to productivity/payroll ROI.**
2. **Is daily-report data good enough to found entitlement detection on?** **Partly, and only in heavy civil.**
   HeavyJob is genuinely the richest contemporaneous dataset in the category — but the reason is *not* the
   diary narrative, it's that the diary sits on top of **cost-coded time cards + planned-vs-actual production
   quantities**, so a "delay" is expressible as a *quantified* variance, not a sentence. That is a real
   entitlement-detection substrate. eSUB and Raken daily reports are much thinner: tagged free text, photos,
   hours, and (eSUB only) a "delay hours" field. **None of the three ties any of it to a contract, a clause,
   or a notice clock — that link is 100% absent across the entire category.**
3. **Data source, competitor, or irrelevant?** **Data source / partner — not a competitor.** Every vendor
   here stops at "we made a time-stamped record so you can win the argument later." None of them makes the
   argument. HCSS ships an open, scoped REST API (`heavyjob:read`) and a Power BI/Direct Access data path;
   Raken has a Procore/Autodesk/accounting integration shelf. The layer is the *supply* of contemporaneous
   evidence; the thesis product is the *demand* side.

---

## 1. SNAPSHOT

### 1.1 HCSS (HeavyJob / HeavyBid)

| Fact | Value | Source |
|---|---|---|
| Founded | 1986 (38+ years in business), Sugar Land, TX | https://www.hcss.com/press/hcss-unveils-heavyjob-for-utility-contractors/ |
| Ownership (now) | **Nemetschek Group** — acquisition **completed 1 July 2026** | https://www.hcss.com/press/nemetschek-group-completes-hcss-acquisition/ |
| Ownership (prior) | Thoma Bravo (acquired 2021; pre-2021 founder-led + 32% ESOP) | https://www.thomabravo.com/press-releases/thoma-bravo-completes-acquisition-of-hcss |
| 2025 revenue | **~USD 215 million** | https://www.hcss.com/press/nemetschek-group-completes-hcss-acquisition/ |
| ARR growth | **~21%** | same |
| EBITDA margin | **~40%** | same |
| Employees | **550+** | same |
| Customers | **4,000+ companies**, $1M to billions in revenue, US + Canada | https://www.hcss.com/products/ |
| HeavyJob scale | **128,000 active HeavyJob users**; **40,000 crews**; 9.4/10 avg rating; *"95% of HeavyJob projects close within budget"* | https://www.hcss.com/products/construction-project-management-software/ |
| ICP | Heavy civil / highway / utility / DOT contractors; self-perform earthwork, paving, underground | https://www.hcss.com/products/ |
| Geography | US + Canada | https://www.hcss.com/press/hcss-unveils-heavyjob-for-utility-contractors/ |

**Deal structure detail:** Nemetschek SE holds ~72% of the Build & Construct segment; Thoma Bravo funds
retain ~28% as minority shareholder. HCSS now sits alongside **Bluebeam, GoCanvas and Nevaris**. Impact on
Nemetschek net debt ~EUR 450 million. Announced 13 Apr 2026.
https://www.hcss.com/press/nemetschek-set-to-acquire-hcss-creates-next-global-construction-technology-leader/

**Marketing stat HCSS repeats:** *"HCSS customers win 75% of work across 50 U.S. Department of Transportation
markets"* and *"produce 40% more bids than competitors."* (same URL) — note these are bid-win stats, not claim stats.

### 1.2 eSUB

| Fact | Value | Source |
|---|---|---|
| Founded | 2008, San Diego, CA. Founder Wendy Rogers | https://esub.com/about-esub/ |
| Users | **16,000+ eSUB users** | https://esub.com/about-esub/ |
| Employees | **60+ team members** | https://esub.com/about-esub/ |
| Customers (homepage) | *"Hundreds of Commercial Subcontractors Rely on eSUB"* | https://esub.com/ |
| Customers (Feb 2024 PR) | *"Thousands of trade contractors"* have adopted eSUB Cloud | https://www.prnewswire.com/news-releases/contractors-use-documentation-software-to-help-prevent-legal-disputes-in-2024-302066628.html |
| Funding | $12M Series B, May 2019, led by Catalyst Investors w/ Revolution Ventures | https://www.prnewswire.com/news-releases/esub-construction-software-secures-12-million-series-b-led-by-catalyst-investors-300858217.html |
| Funding | Undisclosed growth-equity round, May 2023 (Catalyst + Revolution), to fund new eSUB Cloud | https://www.prnewswire.com/news-releases/esub-construction-software-announces-equity-funding-round-fueling-growth-for-new-version-of-esub-cloud-301831697.html |
| Total raised | ~$22–23M across ~6 rounds (Tracxn/Crunchbase, **secondary — MEDIUM confidence**) | https://www.crunchbase.com/organization/esub-construction-software |
| Acquired? | **No acquisition found.** Still independent, PE/VC-backed | — |
| ICP | Commercial **subcontractors / trade contractors** only — electrical, mechanical, HVAC, plumbing, drywall | https://esub.com/project-management-software/ |
| Product split | **eSUB Classic** (app.esub.com) and **eSUB Fusion** (esubcloud.com) — *"two distinct tools"* | https://esub.com/login-page/ |

> **Trajectory read (important):** eSUB has now been through *three* product generations — Classic → Cloud →
> Fusion — while headcount stayed at 60+ and users at 16k+. Blog cadence has collapsed: the blog index shows
> **five posts spanning Feb 2025 → Aug 2026** (https://esub.com/blog/). This is a company that found the right
> *narrative* (documentation → recoverable revenue) and could not convert it into growth.

### 1.3 Raken

| Fact | Value | Source |
|---|---|---|
| Founded | 2014, Carlsbad, CA | https://www.businesswire.com/news/home/20250909597910/en/Sverica-Capital-Management-Announces-Strategic-Growth-Investment-in-Raken |
| Ownership | **Sverica Capital took a majority stake, 9 Sept 2025.** CEO Ty Kalklosch stays; Sverica's Jordan Richards + Michael Dougherty join board | same |
| Scale | **4,500+ construction firms**; grew **13,000 → 70,000 users** | same |
| Sverica | $2.2B cumulative committed capital | same |
| Prior funding | ~$12M over 2 rounds (Tracxn — **secondary, MEDIUM confidence**); Latka lists it as bootstrapped (**contradictory — treat both as UNVERIFIED**) | https://tracxn.com/d/companies/raken/ |
| Revenue | Latka estimate $16.5M ARR (2025). **UNVERIFIED — self-reported aggregator, and internally inconsistent with its own 2024 figure.** | https://getlatka.com/companies/rakenapp.com |
| ICP | Mid-market commercial GCs and subs; daily-log-first, expanding into full field platform | https://www.rakenapp.com/features |

### 1.4 Secondary players (brief)

| Vendor | What it is | Scale / ownership | Pricing | Source |
|---|---|---|---|---|
| **Fieldwire** | Jobsite task/plan management, punch, forms; RFIs/Submittals/Change Orders only at top tier | Owned by **Hilti** | Basic free (5 users / 3 projects / 100 sheets); **Pro $39**, **Business $64**, **Business Plus $89** per user/mo annual; **API access only on custom contracts** | https://www.fieldwire.com/pricing/ |
| **Buildertrend** | Residential/remodel construction management + client portal | *"Trusted by 20,000+ builders"*; ownership **UNVERIFIED** | Not captured | https://buildertrend.com/ |
| **Knowify** | Specialty/trade contractor job costing, AIA billing, change orders | Small; ownership UNVERIFIED | **Core $99/mo** (1 user, +$29/user); **Advanced $329/mo** (10 users, adds T&M contracts, **daily logs**, WIP); **Enterprise custom** (adds **RFIs & submittals**) | https://www.knowify.com/pricing/ |
| **Kojo** | Materials procurement / purchasing / warehouse for trade contractors — **not a daily-report tool at all** | Investors incl. **Tiger Global, Battery Ventures, 8VC, Schneider Electric, Suffolk, Tishman Speyer, BoxGroup, Abstract, Bienville, RXR**. Amounts **UNVERIFIED** | Tiered, not published | https://www.usekojo.com/about |

**Kojo is largely off-thesis** for entitlement detection — it is a procurement/materials system. Its only
adjacency is material *price escalation* and *late delivery* evidence, which is a real claim driver but Kojo
does nothing commercial with it.

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 HCSS HeavyJob — the richest contemporaneous dataset in heavy civil

**Named features** (https://www.hcss.com/products/construction-project-management-software/):
Project management · Time cards · Job costing · Budget & forecasting · Material tracking · Map view ·
Field productivity · **T&M billing** · Work order import · Track pay items · **Daily field reporting (DFR)** ·
**Daily log** · Accounting integrations · **Construction forms**

**Why this dataset is different from every other field tool:** HeavyJob does not just capture a narrative.
Every field entry is bound to a **cost code** and a **planned quantity**, so a bad day is expressible as a
*number* (units installed vs. bid, hours burned vs. budget) rather than a paragraph. Production-vs-plan
variance is computed **daily**. That is the substrate an entitlement engine would want.

**Daily diary specifics** (https://www.hcss.com/videos/construction-site-daily-diaries-for-the-field-office/):
- Captures working conditions, photos, and time-card data
- Entry via typing **or voice transcription**, **no character limits**
- **Customizable tags** — the demo's examples are literally **`material delay`** and **`equipment breakdown`** —
  and *"you can run reports against"* those tags to see e.g. *"how many times I've had a subcontractor issue on the job site"*
- Office consumes a **"daily digest"** formatted like a newspaper
- HCSS's own demo example: **"Johnson Concrete showed up three hours late. At $1,500 a crew hour, that's a lot of money."**

> That last quote is the single most thesis-relevant thing HCSS says. **The data to compute a disruption
> claim exists inside HeavyJob and HCSS narrates the dollar impact out loud in its own demo — and then does
> nothing with it.** No entitlement, no notice, no letter, no attribution model, no package.

**Does HCSS market "dispute protection"? Yes — but weakly and only in a defensive/billing frame.** Verbatim:

- *"Daily logs help reduce disputes and risk by creating a **time-stamped record** of jobsite activity."*
  — https://www.hcss.com/products/daily-log-reporting-software/
- *"Teams can document delays, issues, and changes as they happen, providing **clear evidence** to support
  decisions, **resolve disputes, and protect against claims**."* — same URL
- *"Digital daily logs improve accuracy by capturing information in real time instead of relying on memory
  or handwritten notes."* — same URL
- T&M page: *"goodbye to common time and material billing headaches like **disputed invoices, lost tickets**"*;
  *"Having this **documentation trail** will go a long way towards **settling disputes** when it comes time to bill"*;
  *"**Stop losing revenue**"*; *"Time and material billing **reduces revenue leakage** by ensuring no billable
  work is missed."* — https://www.hcss.com/products/time-material-billing/
- Forms: completed forms become *"part of the overall record of the job"* and provide *"supporting records for
  audits, incident reviews, and **dispute resolution**."* — https://www.hcss.com/products/construction-forms/

**Critically: the framing is always "protect against claims" (defence) and "settle billing disputes"
(collect what you already invoiced) — never "identify and prosecute an entitlement" (offence).** HCSS is
selling *revenue capture at the invoice line*, not *revenue recovery at the contract line*.

**T&M sign-off workflow** (the closest thing to contemporaneous claim evidence HCSS ships):
- Quick **toggle switch** on a time card to flag work as T&M
- Foreman generates a **daily T&M report / preliminary hours report** on the jobsite
- **Captures owner/GC representative e-signature in the field**, same day
  — https://www.hcss.com/products/time-material-billing/

**Potential Change Order (PCO) module — shipped July 2024.** This is HCSS's one genuine step toward the thesis.
(https://www.hcss.com/blog/potential-change-order/ ; press 9 July 2024 via
https://csengineermag.com/hcss-announces-new-heavyjob-feature-for-enhanced-change-order-tracking/)

- Purpose: *"capture potential changes to an existing contract"*
- Tracks **status, scope change, cost impact**, and which parts of the project are impacted
- Records **rough order of magnitude (ROM)**, **schedule impact**, **cost impact**
- **Links related items: issues, RFIs, drawings, cost codes**
- **Revision log** of every change (audit trail)
- Field-originated: *"Foremen can communicate potential out-of-scope work from the field to the office team by
  **raising issues directly in the HCSS Field App**, and project managers can review issues and create RFIs for
  project owners, **linking those documents to the Potential Change Orders**"*
- Stated benefit: PMs can *"track out-of-scope changes and **request payment for work beyond the contract**"*

**What PCO does NOT do:** no contract ingestion, no clause reference, **no notice-deadline tracking of any kind**,
no automatic detection (a human must raise the issue), no notice letter, no claim narrative, no delay analysis.
The "schedule impact" field is a **manual free-entry field, not an analysis**.

**Utility HeavyJob (March 2025)** — HCSS's revenue-leakage marketing peak:
*"capture 100% of their earned revenue"*, targeting *"revenue leakage, inefficiencies, and billing inaccuracies"*
and *"billing errors and missed revenue opportunities."*
— https://www.hcss.com/press/hcss-unveils-heavyjob-for-utility-contractors/

**HCSS Insights** — Power BI white-labeled reporting, **80+ prebuilt reports** across operations, time cards, bid
performance, safety, equipment, incidents; cross-product reporting; **"Direct Access" for customers with their own
data warehouse**. https://www.hcss.com/products/hcss-insights/

### 2.2 eSUB — the only vendor that named the thesis out loud

**Modules** (https://esub.com/project-management-software/): Daily Reports · Project Management ·
**Time & Materials** · Field Communications · Drawings · Document Control · **Field Notes** · Time Management ·
Progress Billing · **Change Orders** · Reporting & Analytics · Purchase Orders · Job Costing · **RFIs** · **Submittals**

**Daily report fields** (https://esub.com/daily-reports/): *"Document weather conditions, crew mix, performed
labor, **delay hours**, accidents, equipment, visitors, and comments"*; photos/videos with markups; customizable
templates; *"Easily track internal issues and submit standard forms to General Contractors."*
Note **`delay hours` is a first-class field** — the only explicit delay quantum field I found in the category.

**Field Notes** (https://esub.com/field-notes/): document *"job progress"*, issues, delays, safety protocols,
material shipments; attach files/photos/videos; annotate with text and freehand markup; **keyword tags** to
*"draw attention to critical issues or setbacks"*; **location tagging** within the jobsite;
*"Track document-related activity, including **email activity, revisions, and edit history**."*

**Change Orders** (https://esub.com/change-orders/) — verbatim marketing:
- *"**Maximize Revenue and Minimize Losses** with eSUB Construction Change Order Software"*
- *"Transform Your Change Order Challenges with Confidence"*
- *"Comprehensive change order tracking: Keep track of change orders from start to finish"*
- Lump-sum or category-based quotes; detailed individual line items; faster approvals; custom access permissions
- Headline stat: **"Increase revenue on change orders by 25%"**

**The three eSUB numbers** (homepage, attributed to *"a 2023 survey of eSUB customers"* — i.e. **self-reported
customer survey, not independent**): **+29% productivity · −47% rework · +25% revenue on change orders.**
https://esub.com/

#### The on-thesis marketing — captured verbatim

**(a) Feb 21, 2024 press release, title: "Contractors Use Documentation Software To Help Prevent Legal Disputes In 2024"**
https://www.prnewswire.com/news-releases/contractors-use-documentation-software-to-help-prevent-legal-disputes-in-2024-302066628.html
- Cites **Arcadis 2023 Construction Disputes Report: dispute values in North America increased 42% from 2021 to 2022**
- References **"nuclear verdicts" exceeding $10 million**
- Dan Bawden (builder + attorney): ***"Most contractors have pretty disorganized books, so there's very little
  paper trail."*** / ***"A good lawyer is going to beat you up with that."***
- Andee Hidalgo (Spearhead Construction): ***"We genuinely rely on those field notes."*** / ***"That's the
  difference [between] surviving and not."***

**(b) Spearhead Construction case study** — the single best artifact in this whole category.
https://esub.com/spearhead-construction-case-study/
- eSUB frames it as: eSUB Cloud helped Spearhead ***protect profits and manage claims***; *"real-time data and
  field notes making claims management easier and more accurate"*
- ***"Managing claims is vital for protecting profits and ensuring fair compensation for delays and disruptions."***
- **"Attaching a professional Field Note document to a timely *Notice* has become a Best Practice for
  Spearhead's risk management."**
- Spearhead relies on the **"Correspondence Toolbox with pre-populated templates for contractual correspondence
  and notices"** ← **this is the only notice-drafting capability found anywhere in the category**
- Hidalgo: *"You see how this project came together or didn't. And you see all the issues involved in it. All
  these images mean something to me."*
- Hidalgo: *"Our Foreman can easily dictate a description of an image into his phone, and the office is instantly
  aware of the issue."*
- **No dollar amounts or recovery percentages are given.**

> **Caveat on the Correspondence Toolbox:** it appears in the case study but **not** on the current
> eSUB Cloud/Fusion module list (https://esub.com/project-management-software/) and I could not find a product
> page or help article for it. Best read: a **legacy eSUB Classic** feature — a static template library, not
> deadline-aware notice generation. Marked **PARTIALLY VERIFIED (single vendor-published source)**.

**(c) August 2026 blog — eSUB still says the thesis out loud, better than anyone:**
https://esub.com/blog/the-subcontractor-tech-gap-why-tools-built-for-gcs-keep-trades-behind (13 Aug 2026)
- ***"It's not about the work you did; it's about the work you documented."***
- ***"A missed approval deadline or insufficient documentation can result in thousands of dollars in
  unrecoverable costs."***
- ***"Disputes are rarely about whether the work was completed, but if it was documented, approved, and
  completed as specified."***
- *"Any billing delays, incomplete documentation, or missing approvals can significantly impact cash flow"*

**(d) eSUB's own delay-claim content admits the product does NOT generate claims.**
https://esub.com/blog/how-to-write-a-construction-delay-claim — the article says *"Daily reports, photos, and
email communications are critical pieces of documentation"* and that *"eSUB organizes all of your project
information in one place"* — **the claim letter itself must be drafted by the contractor.** No notice deadlines,
no clause references, no statistics.

**(e) eSUB on litigation** (https://esub.com/blog/4-major-benefits-field-reporting/):
- *"Today, it doesn't take much to get litigation started in the construction industry."*
- *"Contractors may well find themselves on either side of a dispute, which is why they should always be careful
  to have well-documented daily reports"*
- *"A number of clients, particularly government ones, now require daily reports"*
- **No external statistics cited anywhere in the article.**

### 2.3 Raken — daily reports at scale, deliberately apolitical about claims

**Feature set** (https://www.rakenapp.com/features):
Progress reporting (Daily Reports, **Collaborator Reports**, **Segmented Daily Reports**, Photo documentation,
Tasks, Messaging) · Time & production (Time Tracking, Time Clock, Kiosk Mode, **Production Tracking**, Material
Tracking, Equipment, Resource Scheduling, Labor Management) · Safety & quality (Safety, Quality, Managed
Checklists, **Observations**, Incidents, Toolbox Talks, **Dashboards & Insights**) · Project management
(**RFIs**, Document Management, Forms, Budget Management)

**Daily report data captured** (https://www.rakenapp.com/features/daily-reports): work logs · notes · photos,
videos & attachments · time · safety documentation · **cost codes, materials and equipment** · weather ·
manpower/onsite personnel · survey responses.

**The ONLY dispute-adjacent line on Raken's daily-report page:**
> *"Accurate daily construction reports can also help **protect firms from litigation** and prevent delays."*

That's it. **No claims module, no change orders, no notices, no entitlement language, no published statistics
on that page.** A reviewer confirms the gap directly (§9).

**Raken published research:** I could not locate a Raken "State of Daily Reporting" survey or any Raken-published
research report with hard numbers on documentation gaps. **UNVERIFIED — I believe none exists.** Their content
is feature marketing and customer case studies (https://www.rakenapp.com/case-studies), not primary research.

### 2.4 The category-wide blind spot

| Thesis primitive | HCSS | eSUB | Raken | Fieldwire | Knowify |
|---|---|---|---|---|---|
| Ingests the **contract/subcontract** as parsed data | ✗ | ✗ | ✗ | ✗ | ✗ |
| Extracts **clauses** (changes, notice, delay, LDs) | ✗ | ✗ | ✗ | ✗ | ✗ |
| Knows a **notice is required** for an event | ✗ | ✗ | ✗ | ✗ | ✗ |
| Tracks a **contractual notice deadline clock** | ✗ | ✗ | ✗ | ✗ | ✗ |
| Drafts a **notice letter** | ✗ | Legacy templates only | ✗ | ✗ | ✗ |
| Estimates **recoverable value** (entitlement-weighted) | ✗ (ROM field, manual) | ✗ | ✗ | ✗ | ✗ |
| Assembles a **claim package** | ✗ | ✗ | ✗ | ✗ | ✗ |

**Zero of seven vendors ingest the contract or track a notice deadline. This is the cleanest, widest gap
found in this layer — and it is unattended, not deliberate (see §6).**

---

## 3. CAPABILITY MATRIX — CATEGORY AS A SUBSTITUTE STACK (best-of-category per dimension)

`SCORES| 1,0,0,1,3,1,3,1,3,1,2,1,2,1,2,1,1,1,3,2,1,3,3,2,1,1`

| # | Dimension | Score | Justification (best-of-category) | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | **1** | eSUB Document Control / HCSS Plans store contract PDFs as inert files. No parsing, no structure, no scope model. | https://esub.com/project-management-software/ |
| 2 | clause_extraction | **0** | Absolutely nothing in any of the seven products reads a clause. | https://www.hcss.com/products/ |
| 3 | notice_detection | **0** | No product detects that an event triggers a notice obligation. HCSS PCO requires a human to raise the issue. | https://www.hcss.com/blog/potential-change-order/ |
| 4 | deadline_tracking | **1** | Generic task due-dates, RFI/submittal ball-in-court dates (eSUB, Raken, Fieldwire). **No contractual notice clock anywhere.** | https://esub.com/project-management-software/ |
| 5 | rfi_event_ingestion | **3** | Native marketed RFIs in eSUB, Raken, Fieldwire (Business Plus), and HCSS PCO links RFIs to change items. | https://www.rakenapp.com/features |
| 6 | email_ingestion | **1** | eSUB logs outbound *"email activity"* on documents; Raken emails report distributions. No inbound mailbox capture. | https://esub.com/field-notes/ |
| 7 | daily_report_ingestion | **3** | Category-defining strength. HeavyJob DFR + diary, Raken daily reports (70k users), eSUB daily reports w/ delay hours. | https://www.hcss.com/products/daily-log-reporting-software/ |
| 8 | schedule_integration | **1** | HCSS PCO has a manual "schedule impact" field; Raken "resource scheduling" is crew allocation. No P6/MSP/CPM integration found. | https://www.hcss.com/blog/potential-change-order/ |
| 9 | change_order_workflow | **3** | eSUB Change Orders (lump-sum/category quotes, line items, approvals, permissions); HCSS PCO; Fieldwire Business Plus; Knowify. | https://esub.com/change-orders/ |
| 10 | claim_identification | **1** | HCSS says *"protect against claims"*, eSUB says *"claims management easier"* — but no product identifies an entitlement. Adjacent language only. | https://www.hcss.com/products/daily-log-reporting-software/ |
| 11 | delay_detection | **2** | Best-in-class: HeavyJob computes **production-vs-plan and cost-vs-budget daily** and diary tags include `material delay`; eSUB has a **delay hours** field. Detects the *symptom* (productivity loss, logged delay events), never schedule delay vs. a baseline, never causation. | https://www.hcss.com/videos/construction-site-daily-diaries-for-the-field-office/ |
| 12 | responsibility_attribution | **1** | Diary text can name the culprit (*"Johnson Concrete showed up three hours late"*) and eSUB field notes are tagged, but there is no structured cause/responsible-party model. | https://www.hcss.com/videos/construction-site-daily-diaries-for-the-field-office/ |
| 13 | contemporaneous_evidence_graph | **2** | HCSS PCO links **issues → RFIs → drawings → cost codes** with a revision log; eSUB links field notes → daily reports → change orders, with edit history and location tags. Real linking, but confined to one vendor's own objects — no contract, schedule, or email nodes. | https://www.hcss.com/blog/potential-change-order/ |
| 14 | evidence_completeness | **1** | Raken tracks missing/incomplete daily reports; nobody scores whether the evidence for a *specific commercial event* is sufficient. | https://www.rakenapp.com/features/daily-reports |
| 15 | recoverable_dollar_estimation | **2** | HeavyJob quantifies actual-vs-budget cost by cost code daily and PCO captures **ROM + cost impact**; T&M billing computes billable value with field sign-off. Cost quantum yes; entitlement-weighted recoverable value no. | https://www.hcss.com/products/time-material-billing/ |
| 16 | claim_package_generation | **1** | Produces PDF daily reports, signed T&M tickets and photo logs that *become* claim exhibits. No assembly, narrative, or package. | https://www.hcss.com/products/time-material-billing/ |
| 17 | notice_drafting | **1** | eSUB **Correspondence Toolbox** — *"pre-populated templates for contractual correspondence and notices"* — evidenced only by one vendor case study and absent from the current Fusion module list. Static templates, deadline-unaware. | https://esub.com/spearhead-construction-case-study/ |
| 18 | schedule_impact_analysis | **1** | A manual "schedule impact" text/number field on a PCO. No windows analysis, no TIA, no as-planned-vs-as-built. | https://www.hcss.com/blog/potential-change-order/ |
| 19 | procore_integration | **3** | Raken lists Procore as a headline project-management integration; the layer broadly interoperates with Procore. | https://www.rakenapp.com/integrations |
| 20 | autodesk_integration | **2** | Raken lists Autodesk and Bluebeam integrations; Autodesk is also an eSUB investor. Depth of object sync not published. | https://www.rakenapp.com/integrations |
| 21 | outlook_gmail_integration | **1** | Automated report distribution by email (Raken Performance tier); no mailbox connector, no thread capture. | https://www.rakenapp.com/features |
| 22 | mobile_workflow | **3** | The one dimension where this layer is genuinely best-in-market: HCSS Field App (offline, **voice-transcribed diary with no character limit**, photos, **in-field e-signature capture**), Raken (offline mode, photo/video), Fieldwire (offline plans). Marketed and evidenced. | https://www.hcss.com/videos/construction-site-daily-diaries-for-the-field-office/ |
| 23 | audit_trail | **3** | HCSS PCO **revision log**; eSUB *"Track document-related activity, including email activity, revisions, and edit history"*; time-stamped daily logs; captured signatures. | https://esub.com/field-notes/ |
| 24 | portfolio_risk | **2** | HCSS Insights: Power BI white-label, **80+ prebuilt reports**, cross-product, plus **Direct Access** to a customer data warehouse; Raken Dashboards & Insights. Cost/production/safety risk — not commercial/claim risk. | https://www.hcss.com/products/hcss-insights/ |
| 25 | performance_pricing_compatibility | **1** | Every vendor is per-seat subscription (Raken $15–$46/user/mo; Fieldwire $39–$89/user/mo; Knowify $99–$329/mo). No contingency, success fee, or value-share model exists in the category. | https://www.fieldwire.com/pricing/ |
| 26 | consultant_replacement_potential | **1** | These systems *feed* the claims consultant (the consultant exports HeavyJob time cards and eSUB daily reports). They replace the paper diary, not the expert. | https://esub.com/blog/how-to-write-a-construction-delay-claim |

**Category totals: 3s = 7 · 2s = 6 · 1s = 11 · 0s = 2.**
Shape: strong on **capture, mobile, audit trail, change-order workflow**; **zero on contract/clause/notice**;
weak on everything between "an event happened" and "here is a claim."

---

## 4. PRICING

| Vendor | Published? | Numbers | Confidence / method |
|---|---|---|---|
| **HCSS HeavyJob** | **No** — quote only | HeavyBid secondary estimate: ~$4,000/yr single user; $25,000–$40,000/yr for 10 users (ITQlick) | **LOW** — third-party estimator, not vendor-published. HeavyJob itself: **no number found**. Enterprise sales motion with implementation/training. |
| **eSUB** | **No** — *"Contact vendor"* on Capterra; demo required | Secondary tiered estimates: ~$39/user/mo (Base), ~$59/user/mo (Advanced), Premium/Enterprise custom; other sources say "starts at $49/user/mo" | **LOW** — sources disagree; no vendor page. https://www.capterra.com/p/76833/eSUB-Subcontractor-Software/ |
| **Raken** | **Partially** (via reviewers, not a public price page) | **Basic $15/user/mo** ($12 annual) · Pro (adds timecards, production tracking, integrations) · **Performance ~$46/user/mo annual** (adds Super Daily, automated report distribution, quality/safety, **API access**) · Enterprise custom | **MEDIUM** — consistent across TrustRadius / Connecteam / SpotSaas; Raken confirms pricing is customized. |
| **Fieldwire** | **YES — fully published** | Basic **free** (5 users/3 projects/100 sheets) · Pro **$39** · Business **$64** · Business Plus **$89** per user/mo annual · Custom for API/SSO/unlimited | **HIGH** — https://www.fieldwire.com/pricing/ |
| **Knowify** | **YES — fully published** | Core **$99/mo** (1 user; +$29/user) · Advanced **$329/mo** (10 users; +$29/user) · Enterprise custom. Service Pro add-on $99/mo; equipment tracking $25/vehicle/mo | **HIGH** — https://www.knowify.com/pricing/ |
| **Buildertrend / Kojo** | Not captured | — | — |

**Pricing read for the thesis:** the whole layer prices **per seat, per month, in the $15–$90 band**, i.e. it is
priced as *tooling*, not as *recovered value*. A product that recovers $250k of entitlement cannot be sold at
$39/user/mo — which means a claims/entitlement product is **not** a natural line extension for any of them
without breaking their pricing architecture. That is a genuine structural moat for a startup.

---

## 5. INTEGRATIONS & API — DATA EGRESS REALITY

**HCSS — the most open, by a distance.**
- Public developer portal: https://developer.hcssapps.com/hcss — *"Create custom integrations to share data
  between your HCSS applications and your other applications"* and *"create custom web or mobile apps to add
  additional functionality."*
- HeavyJob API product page: https://developer.hcssapps.com/products/heavyjob/overview/
- **Scoped OAuth-style access**: each API exposes at least a read-only and a read/write scope. The
  `heavyjob:read` scope covers *"jobs, employees, time cards, and more."*
  https://developer.hcssapps.com/hcss/docs/api-scopes
- Postman/Insomnia collections provided; a community wrapper exists (https://github.com/apratt2003/HCSS_HJ_API)
- HCSS explicitly positions this as **"Your Data in Your Control"** (https://success.hcss.com/your-data-in-your-control-hcss-apis/)
- **HCSS Insights "Direct Access"** allows customers with their own data warehouse to pull HCSS data directly.
  https://www.hcss.com/products/hcss-insights/
- Third-party integration patterns exist in the wild (Acumatica ↔ HeavyJob/HeavyBid via Celigo iPaaS;
  OnStation ↔ HeavyJob).

> **This is the single most important integration fact in this report:** a solo founder can pull cost-coded
> time cards, production quantities, and diary entries out of HeavyJob with a documented, scoped REST API and
> no partnership negotiation. That is a **V1-compatible data source**, exactly what the founder constraint asks for.

**Raken — broad integration shelf, API gated behind the Performance tier.**
https://www.rakenapp.com/integrations
- Accounting/payroll: Sage 100 Contractor, Sage 300 CRE, Sage Intacct, Foundation, Deltek ComputerEase,
  QuickBooks Desktop & Online, Viewpoint Vista, Viewpoint Spectrum, Paychex, Points North, CMiC
- Project management: **Procore, Autodesk, Bluebeam**
- Cloud storage: Egnyte, Google Drive, Box, Dropbox, OneDrive
- Reality capture: EarthCam, DroneDeploy, HoloBuilder, TrueLook
- **API access is a Performance-tier (~$46/user/mo) and above feature** (secondary sources; Raken does not
  publish developer docs publicly — **no public developer portal found**).

**eSUB — API exists, documentation is not public.**
- eSUB's own terms reference an **"API Terms of Use"** users must accept (https://www.esubcloud.com login page),
  so a customer/partner API exists. `developer.esub.com` does not resolve; `esub.com/integrations/` returns 404.
  **Egress reality: closed-by-default, partner-negotiated. LOW confidence on scope.**
- Autodesk is an eSUB investor, implying at least a commercial relationship.

**Fieldwire** — API access **only on custom contracts**; app integrations gated at Business tier and above.
https://www.fieldwire.com/pricing/

**Egress verdict:** HCSS = **open** (best-in-class for this thesis). Raken = **semi-open** (paid tier).
eSUB = **closed/negotiated**. Fieldwire = **closed/enterprise**.

---

## 6. WEAKNESSES AND EXPLICIT GAPS — DELIBERATE OR UNATTENDED?

| Gap | Deliberate or unattended? | Reasoning |
|---|---|---|
| **No contract ingestion / clause extraction (all 7)** | **Unattended** | Nobody has decided *not* to do this — the contract simply isn't in their data model because their buyer (ops/payroll/field) never handed it to them. The subcontract lives with the PM/controller/owner. This is genuine white space **paired with proven paid pain** (see eSUB's own copy: *"A missed approval deadline… can result in thousands of dollars in unrecoverable costs"*). |
| **No notice-deadline clock (all 7)** | **Deliberate-adjacent** | Getting a notice deadline wrong creates *advice-shaped* liability. A field-productivity vendor with a 40% EBITDA margin and PE/strategic ownership has strong incentive not to acquire quasi-legal exposure. This is a **legal-appetite gap**, not a technical one — and therefore durable. |
| **Detection requires a human to raise the issue (HCSS PCO)** | **Unattended** | HCSS already computes daily production variance *and* has taggable diary events. Turning "variance + tag" into "auto-raise a PCO candidate" is a small model on data they already own. They have not done it in the two years since PCO shipped. |
| **HCSS frames everything as billing-dispute defence, never entitlement offence** | **Deliberate** | HCSS's buyer is the heavy-civil COO/controller. Its stat is *"95% of HeavyJob projects close within budget"* — a **cost-control** promise. "Help us go after the DOT" is culturally and commercially off-brand for a vendor whose customers *"win 75% of work across 50 DOT markets"* and want those relationships preserved. |
| **eSUB's claims narrative never became a product** | **Unattended (and instructive)** | eSUB *wrote* the thesis better than anyone (§2.2c) and shipped only templates + storage. 60 employees and three platform rewrites in 18 years explain why: no engineering capacity left for a hard NLP/entitlement problem. |
| **Raken has no change orders at all** | **Deliberate** | Raken's wedge is "the fastest daily report." Adding commercial workflow puts it into Procore's kill zone. A reviewer names the gap explicitly (§9). |
| **eSUB mobile app quality** | **Unattended** | Repeatedly criticised across Capterra/SoftwareAdvice (§9) — a serious problem for the vendor whose entire value prop is *field* documentation. |
| **Per-seat pricing caps value capture** | **Deliberate** | Predictable, PE-friendly ARR. But it structurally prevents them from pricing a recovery product at recovery-scale economics. |
| **No email ingestion (all 7)** | **Unattended** | The richest entitlement evidence in real projects is the email thread, and this layer ignores it entirely. |

---

## 7. ADJACENCY TEST — how hard for THEM to ship "event detection → entitlement matching → evidence → claim package"?

### HCSS — **MEDIUM**
- **Data access: EXCELLENT (the best in the market).** Cost-coded time cards, planned-vs-actual production
  quantities, tagged diary entries, photos, forms, PCOs with links to RFIs/drawings/cost codes, all with revision
  logs, all already in one warehouse, all exposed through a documented API and a Power BI layer. If anyone in
  construction could bootstrap contemporaneous entitlement detection from existing data, it is HCSS.
- **Org incentive: WEAK.** ~$215M revenue, ~40% EBITDA, ~21% ARR growth, just absorbed into Nemetschek's Build &
  Construct segment on 1 July 2026 alongside Bluebeam/GoCanvas/Nevaris. Post-close years go to integration,
  cross-sell and multiple-defence — not to a novel, legally-exposed, small-TAM module.
- **GTM motion: MISMATCHED.** HCSS sells to heavy-civil ops/controllers on cost control and 24/7 support
  (*"picks up within three rings"* — reviewer). Selling entitlement recovery means selling to a different buyer
  with a different sales cycle and different risk conversation.
- **Legal exposure appetite: LOW.** "Protect against claims" (defensive) is safe copy; "here is your $2.1M
  entitlement, send this notice by Thursday" is not.
- **Shipping behaviour: STEADY BUT CONSERVATIVE.** PCO (Jul 2024), Utility HeavyJob (Mar 2025), HeavyBid on the
  Web (Feb 2026), Shield AI dashcam (Feb 2026), Geotab integration (Apr 2026). Real cadence, all adjacent to
  existing surfaces, none legally novel.
- **Net:** they *could*, they *won't soon*, and the new owner makes near-term action less likely, not more.
  **MEDIUM.**

### eSUB — **MEDIUM-HARD**
- **Data access: GOOD** (daily reports with delay hours, field notes with tags/locations, change orders, RFIs,
  T&M) but **small** (16,000 users) and split across Classic and Fusion.
- **Org incentive: HIGH (this is their story) — capacity: LOW.** 60+ employees, mid-platform-migration, five
  blog posts in 18 months. They want to; they cannot afford to.
- **Legal exposure: they already lean in** (Feb-2024 dispute press release; notice templates), so appetite is
  the *least* of their problems.
- **Net: MEDIUM-HARD — blocked by resources and platform debt, not by will.**

### Raken — **HARD**
- Rich daily-report volume (70,000 users) but **no change orders, no contract, no commercial workflow**, and a
  new PE sponsor 11 months in whose thesis is expanding the field platform (safety, quality, scheduling) —
  not entering claims.

### Fieldwire / Buildertrend / Knowify / Kojo — **HARD to IRRELEVANT.**
Fieldwire is a Hilti tools-ecosystem asset; Buildertrend is residential; Knowify is a job-costing/AIA-billing
tool for small trades; Kojo is procurement. None has contract data or a claims motive.

**CATEGORY VERDICT: MEDIUM** (dragged up almost entirely by HCSS's data position, dragged down by every
vendor's incentives, pricing architecture, and legal appetite).

---

## 8. STARTUP POSTURE — PARTNER, CHANNEL, or ROADKILL?

### **PARTNER — strongly, and specifically HCSS first.**

**Why PARTNER:**
1. **They are the supply of contemporaneous evidence and they have deliberately stopped short of using it.**
   Every marketing line in this category ends at *"time-stamped record… to resolve disputes"* — the record is
   the deliverable. Turning the record into an entitlement is the unclaimed step.
2. **HCSS's API is a solo-founder-compatible V1.** Documented, scoped (`heavyjob:read`), Postman collections,
   plus HCSS Insights "Direct Access" for warehouse customers, plus HCSS's own *"Your Data in Your Control"*
   positioning. No partnership required to start; a customer can authorise read access themselves.
3. **The pricing architectures don't collide.** $15–$90/user/mo tooling vs. a recovery-priced product are
   different budgets (field ops vs. project controls/legal). No channel conflict, no cannibalisation.
4. **Their own copy pre-sells the problem.** eSUB: *"It's not about the work you did; it's about the work you
   documented"* and *"A missed approval deadline or insufficient documentation can result in thousands of
   dollars in unrecoverable costs."* HCSS: *"protect against claims."* They have already educated the buyer
   and then handed them a filing cabinet.

**Where it is a CHANNEL:** Raken (4,500 firms), eSUB (subs desperate for this specific outcome and with a vendor
too small to build it) and Knowify are plausible distribution partners — eSUB in particular would arguably rather
OEM this than build it.

**Why NOT roadkill:** none of them can price it, none of them wants the legal exposure, none of them owns the
contract document, and the two largest are both inside fresh PE/strategic ownership transitions
(Nemetschek/HCSS July 2026; Sverica/Raken Sept 2025) where new module risk is at its lowest.

**The real roadkill risk is not from this layer** — it is from Procore/Autodesk (who own the contract, the RFI
and the change order) or from Nemetschek deciding to point Bluebeam + HCSS at it post-integration.

---

## 9. TOP CUSTOMER COMPLAINTS RELEVANT TO THE THESIS (verbatim)

1. **"no change orders or drawings or being able to collaborate with our subcontractors"**
   — Kourtany O., Safety Coordinator, Raken, 1 Oct 2024. https://www.capterra.com/p/153591/RAKEN/reviews/
   *→ The daily-report leader has 70,000 users and no commercial workflow. The evidence and the entitlement live in different products.*

2. **"UX (hard to learn, too many clicks/wait time for numerous operations)."**
   — Ari S., Project Engineer, eSUB, 8 Oct 2024. https://www.capterra.com/p/76833/eSUB-Subcontractor-Software/reviews/
   *→ Documentation friction is the reason field documentation is thin. Every extra click is lost entitlement.*

3. **"It [is] difficult to upload pictures of work in progress - Biggest complaint from Team Members"**
   — Brian D., Construction Management, eSUB, 6 Feb 2023. Same URL.
   *→ Photos are the highest-value claim exhibit and the hardest thing to get out of the field.*

4. **"Hate when your time-out occurs and you lose communication with eSUB and have to log back in."**
   — Peter M., Project Manager, eSUB, 17 Jun 2026. Same URL.
   *→ Lost work in a documentation tool is the worst possible failure mode for contemporaneous evidence.*

5. **"Innovation has seemed to lag when compared to competitors"**
   — Ian S., eSUB. https://www.softwareadvice.com/construction/esub-profile/
   *→ Direct customer confirmation of the eSUB trajectory read.*

6. **"outdated database with a poorly constructed user interface... requires a ton of clicks"** and
   **"reporting system is also a mess of odd questions and functions"**
   — HeavyJob reviewers. https://www.softwareadvice.com/job-costing/heavyjob-profile/
   *→ The richest dataset in heavy civil is trapped behind a UI its own users call a mess — which is exactly why an analytical layer on top has room.*

7. **"Our foremen sometimes have issues with their iPAD syncing up with desktop computers."**
   — Alicia P., Payroll Coordinator, HeavyJob, 5 Jun 2025. https://www.capterra.com/p/140170/HeavyJob/reviews/

8. **"frequent issues. Inputting notes and pictures now require multiple attempts"**
   — Philip M., Superintendent, Raken, 8 Apr 2024. https://www.capterra.com/p/153591/RAKEN/reviews/

9. Counter-evidence worth respecting: **"real-time visibility into our production and costs has saved us from
   countless overruns"** — HeavyJob reviewer, https://www.softwareadvice.com/job-costing/heavyjob-profile/
   *→ HeavyJob genuinely detects cost/production deviation. It just never converts it into a commercial claim.*

**Ratings summary:** eSUB **4.4 / 256 reviews** (Capterra; 92% positive sentiment) ·
HeavyJob **4.5 / 96 reviews** (Capterra) — HCSS's own site claims 257 G2 / 507 Capterra / 117 TrustRadius /
618 App Store reviews across products · Raken **4.6 / 249 reviews** (Capterra).

---

## 10. HARDEST FACTS (strongest numeric facts found)

1. **HCSS 2025 revenue ≈ USD 215 million, ARR growth ≈ 21%, EBITDA margin ≈ 40%, 550+ employees, 4,000+ customers
   — acquisition by Nemetschek Group completed 1 July 2026.**
   https://www.hcss.com/press/nemetschek-group-completes-hcss-acquisition/
2. **128,000 active HeavyJob users; 40,000 crews; "95% of HeavyJob projects close within budget."**
   https://www.hcss.com/products/construction-project-management-software/
3. **Raken: 4,500+ construction firms; grew from 13,000 to 70,000 users; Sverica Capital took a majority stake
   on 9 September 2025.**
   https://www.businesswire.com/news/home/20250909597910/en/Sverica-Capital-Management-Announces-Strategic-Growth-Investment-in-Raken
4. **eSUB: 16,000+ users and 60+ employees, founded 2008 — the vendor that marketed claim documentation hardest
   is ~8x smaller by users than HeavyJob and ~4x smaller than Raken.**
   https://esub.com/about-esub/
5. **eSUB's own customer-survey stat: "Increase revenue on change orders by 25%" (with +29% productivity and
   −47% rework), attributed to "a 2023 survey of eSUB customers."**
   https://esub.com/ and https://esub.com/change-orders/
6. **Arcadis 2023 Construction Disputes Report, as cited by eSUB (21 Feb 2024): dispute values in North America
   increased 42% from 2021 to 2022; "nuclear verdicts" exceed $10 million.**
   https://www.prnewswire.com/news-releases/contractors-use-documentation-software-to-help-prevent-legal-disputes-in-2024-302066628.html
7. **Fieldwire gates RFIs, Submittals, Change Orders and Budget behind its top published tier at $89/user/month
   annual — i.e. commercial workflow is priced as a premium add-on to field capture, not as its core.**
   https://www.fieldwire.com/pricing/
8. **HCSS's own diary demo quantifies the loss and stops: "Johnson Concrete showed up three hours late. At
   $1,500 a crew hour, that's a lot of money."**
   https://www.hcss.com/videos/construction-site-daily-diaries-for-the-field-office/

---

## 11. UNKNOWNS — and what would settle each

| Unknown | What would settle it |
|---|---|
| **Does "HCSS Skyline" exist at all?** Not on hcss.com/products, no press release, no exact-phrase result. | HCSS sales/support confirmation, or an HCSS price list. Currently **UNVERIFIED — assume it does not exist**. |
| **Exact HeavyJob API object coverage** — are *diary entries*, *diary tags*, *production quantities* and *photos* readable, or only jobs/employees/time cards? The scope description says *"jobs, employees, time cards, **and more**."* | Fetch `https://developer.hcssapps.com/hcss/reference` (requires portal navigation) or request a sandbox key. **This is the single highest-value unknown for V1 feasibility.** |
| **eSUB Correspondence Toolbox** — does it still exist in Fusion? Is it deadline-aware? What templates ship? | An eSUB demo, or an eSUB Classic help-centre article. Currently evidenced by **one vendor case study only**. |
| **eSUB's true revenue / ARR and whether it is growing or flat.** The "hundreds" (homepage, 2026) vs "thousands" (PR, 2024) discrepancy is unexplained. | PitchBook/Crunchbase premium, an investor update, or a Catalyst Investors portfolio disclosure. |
| **Raken's actual revenue.** Latka lists $16.5M ARR 2025 vs $21.8M 2024 — an implausible decline in the year they took a majority PE investment. **Treat all Raken revenue figures as UNVERIFIED.** | Sverica portfolio disclosure or a credible trade-press deal write-up with figures. |
| **HeavyJob/eSUB/Raken published pricing.** All three are quote-only. | A published reseller price list or a redacted customer contract. |
| **Whether any of these vendors has an internal claims/entitlement roadmap item.** | Product roadmap webinars (HCSS Users Group / eSUB customer conference), or job postings mentioning claims/contract NLP. |
| **Hard, independent numbers on claims lost to documentation gaps.** eSUB cites Arcadis second-hand; nobody in this layer publishes primary research on it. Raken publishes none. | The primary Arcadis Global Construction Disputes Report (2024/2025/2026 editions) directly — likely covered by another agent's report, not this layer's. |
| **Kojo and Buildertrend funding/ownership specifics.** | Crunchbase/PitchBook; deprioritised as both are off-thesis for entitlement detection. |

---

## 12. SO WHAT — implications for the thesis

1. **The field layer is the evidence supply chain, and it is already digitised at scale.** 128,000 HeavyJob users,
   70,000 Raken users, 16,000 eSUB users. The contemporaneous record exists, is time-stamped, is photo-backed,
   and — in HeavyJob's case — is cost-coded and quantity-tracked. **The bottleneck is not capture. It is
   interpretation.**
2. **Heavy civil (HCSS) is the strongest founding beachhead in this layer**, because production-vs-plan variance
   gives you a *numeric* disruption signal instead of a text-mining problem, and because HCSS's API is open.
   Subcontractors (eSUB) are the strongest *demand* signal but the weakest data.
3. **The thesis-threatening finding is eSUB.** eSUB spent years marketing precisely the thesis — *"It's not
   about the work you did; it's about the work you documented"* — to precisely the right buyer, and stayed at
   60 employees. **"Better documentation" does not sell.** The lesson is not that the pain is fake; the eSUB
   copy and the Spearhead case study prove it is real. The lesson is that **documentation is a cost, and
   entitlement is a benefit — and eSUB only ever sold the cost.** Any product here must be sold on *recovered
   dollars*, quantified up front, or it inherits eSUB's growth curve.
4. **The gap is unusually clean and unusually wide.** Seven vendors, zero contract ingestion, zero clause
   extraction, zero notice detection, zero deadline clocks. Two of the three are inside ownership transitions
   with strong incentives against new legally-exposed modules. Per-seat pricing structurally blocks them from
   pricing recovery.
5. **Posture: build beside them, ingest from them, price against recovery, never compete on capture.**
