# 13 — SCHEDULE ANALYTICS / DELAY FORENSICS LAYER

**Scope:** SmartPM, nPlan, Deltek Acumen (Fuse / Risk & 360 / Touchstone), ALICE Technologies,
Nodes & Links, "Basis", Contilio/Foresight, classic forensic-schedule tooling (Steelray Delay
Analyzer, Ron Winter Schedule Analyzer eForensic), and the governing standards
(AACE International RP 29R-03; SCL Delay and Disruption Protocol 2nd ed.).

**Researched:** 19 Aug 2026. All URLs accessed on that date unless noted.
**Report type:** ONE category report + per-company profiles + 3 scored rows
(combined best-of-category, SmartPM, nPlan).

---

## 0. HEADLINE ANSWER (read this first)

The single most important finding in this category is not a product fact — it is a standards fact,
and it is stated in black and white by the body that defines forensic schedule analysis:

> **"Schedules are a project management tool that, in and of themselves, do not demonstrate root
> causation or responsibility for delays. Legal entitlement to delay damages should be distinct and
> apart from the forensic schedule analysis methodologies contained in this RP."**
> — AACE International RP 29R-03, *Forensic Schedule Analysis*, Rev. April 25, 2011, §1.2(f)
> (https://web.aacei.org/docs/default-source/toc/toc_29r-03.pdf, sample/TOC PDF, p.10 of 136)

> **"…the RP primarily focuses on the use of forensic scheduling techniques and methods for factual
> analysis and quantification as opposed to assignment of delay responsibility."** — §1.3(c), ibid.

That is the whole game. **Delay QUANTIFICATION is a solved, automated, commoditised problem.**
SmartPM, Deltek Acumen Fuse and Steelray Delay Analyzer all compute the same half-step windows
arithmetic; SmartPM sells it for $25k/yr, Steelray for $3,990/user/yr. **Delay CAUSATION and
RESPONSIBILITY are not computed by any of them, by design, because the answer is not in the
schedule file** — it is in the RFIs, daily reports, meeting minutes, correspondence and contract.

Every serious methodology says the same thing in its own words. The SCL Protocol's description of
the two windows methods both end with the identical sentence:

> **"Thereafter, the analyst investigates the project records to determine what events might have
> caused the identified critical delay."**
> — SCL Delay and Disruption Protocol, 2nd ed. (Feb 2017), Part B §11.6(c) and §11.6(d)
> (https://www.scl.org.uk/sites/default/files/documents/SCL_Delay_Protocol_2nd_Edition_Final.pdf)

The schedule-analytics vendors have automated everything up to that sentence and nothing after it.
**The sentence itself is the thesis's white space.**

---

## 1. SNAPSHOT — WHAT THIS CATEGORY IS

### 1.1 The layer, defined
Tools that ingest CPM schedule files (Primavera P6 XER/XML, MS Project MPP/XML, Asta PowerProject,
Phoenix) and produce: schedule quality/health scores, version-to-version change detection, critical
path movement, delay quantification per period, probabilistic forecasts, and what-if/acceleration
scenarios. They are bought by **schedulers, project controls managers and PMO/risk leads** — NOT by
contract administrators, commercial managers or legal.

### 1.2 The four sub-segments

| Sub-segment | Players | What they sell | Buyer |
|---|---|---|---|
| **Automated retrospective delay quantification** | SmartPM, Deltek Acumen Fuse, Steelray Delay Analyzer, Ron Winter Schedule Analyzer eForensic, Nodes & Links (Delay Navigator) | "What moved, when, and by how much" — half-step / windows arithmetic | Scheduler, project controls, claims analyst |
| **Predictive / probabilistic schedule risk** | nPlan, Deltek Acumen Risk & 360, Nodes & Links (SRA) | "How likely are you to finish on time" — ML forecast + Monte Carlo | PMO, risk manager, owner |
| **Generative / optioneering scheduling** | ALICE Technologies | "What is a better way to build this / how do I recover" | Planner, ops leadership |
| **Physical-progress evidence capture** | Contilio (adjacent) | 3D/AI progress + quality verification from scans | Owner/PM reporting |

### 1.3 Company one-liners

- **SmartPM Technologies** — Atlanta GA, founded 2012 by Michael Pink. Series A **$5.5M, 29 May 2024**,
  led by **Building Ventures**, with **GS Futures** and existing investor **The Nemetschek Group**
  (https://smartpm.com/press/securing-series-a-funding;
  https://www.businesswire.com/news/home/20240529228732/en/). Sells to ENR-400-class GCs and owners.
  Tagline: **"Deliver Construction Projects On Time, On Budget, and Out of Court"** (https://smartpm.com/).
- **nPlan** — London, founded 2017 (https://sourceforge.net/software/product/nPlan/). Series B
  **$16M, 17 Oct 2025**, led by **CapHorn**, with **Chevron Technology Ventures, Suffolk Technologies,
  GV, Pentech, LocalGlobe**
  (https://www.nplan.io/press-releases/nplan-raises-16m-series-b-to-scale-its-ai-led-transformation-of-capital-project-delivery).
  Sells to **owners and mega-programme PMOs** (HS2, Network Rail, TRU, Anglian Water, Chevron, Shell,
  MTR, NEOM), not to GC commercial teams.
- **Deltek Acumen** — the incumbent. Fuse (diagnostics/forensics), Risk & 360 (Monte Carlo),
  Touchstone (schedule submittal gate). Sold into aerospace/defence/government/EPC and to the
  consultancies (https://www.deltek.com/en/products/project-and-portfolio-management/acumen).
- **ALICE Technologies** — Menlo Park + Prague + Pune, founded 2015 out of Stanford (René Morkos).
  Investors: Merus Capital, Foundamental, Future Ventures, Lightspeed, Blackhorn Ventures,
  Brick & Mortar Ventures (https://www.alicetechnologies.com/about). Claims deployment on
  **$297 billion** of global construction projects (https://www.alicetechnologies.com/).
- **Nodes & Links** — founded by Greg Lawton and Dr Christos Ellinas; team across 9 countries, 10 PhDs,
  ISO 27001 certified (https://nodeslinks.com/company/, https://nodeslinks.com/why-trust-our-ai/).
  Customer logos include Balfour Beatty, Vinci, BAM Nuttall, Costain, DPR, AtkinsRéalis,
  Burns & McDonnell, Ferrovial, Bechtel, AECOM, Turner, Intel, Equinix (https://www.nodeslinks.com/).
- **Steelray Delay Analyzer** — the cheapest credible forensic tool. **$3,990/user/yr or $390/user/mo**,
  "the Daily Progress Method to run a half-step analysis, **per AACE RP 29R-03**"
  (https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php).
- **Ron Winter Consulting — Schedule Analyzer eForensic** — "the complete and only set of software
  tools for the Claims Analyst"; **$2,750 perpetual single-user license**
  (https://www.ronwinterconsulting.com/, http://scheduleanalyzer.com/eforensic_order.htm).
- **Contilio** — London; 3D AI analytics from site scans/images for progress, quality, risk
  (https://www.contilio.com/). Adjacent evidence-capture, not delay analytics.
- **"Basis"** — `UNVERIFIED`. I could not identify a live company named "Basis" operating in
  construction schedule/delay analytics. `basis.build`, `basisplan.com`, `withbasis.com`,
  `basisconstruction.com` are non-resolving or parked GoDaddy pages; `getbasis.ai` is an accounting-AI
  company; `basis.com` is adtech; `buildbasis.com` is a UK VC firm. See §11 UNKNOWNS.
- **"Foresight"** — `UNVERIFIED / NOT RELEVANT`. The only live "Foresight" I could reach
  (https://www.foresightiq.co/) is a B2B competitive-intelligence SaaS with no construction product.

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 SmartPM — the most on-thesis product in the category

| Module | What it does | Evidence |
|---|---|---|
| **Delay Analysis (Half-Step / Windows)** | Marketed as **"Automated, Forensic-Grade Construction Half-Step Delay Analysis Software"**; "applies a windows analysis approach automatically across each period"; breaks each update into progress delay, gains and planned impacts | https://smartpm.com/features/delay-analysis |
| **Key delay metrics** | Four computed metrics only: **End Date Variance** (= Actual Progress Impact − Planned Changes Impact), **In-Period Delay (Critical Path Delay)**, **In-Period Gains**, **Planned Impact** | https://help.smartpm.com/key-delay-metrics |
| **Schedule Quality Checker** | 35+ CPM quality checks (missing logic, negative float, out-of-sequence, constraints) | https://smartpm.com/schedule-quality-checker |
| **Schedule Controls** | "No more manual forensic exercises. Controls automatically analyzes updates proactively to quantify delays, measure realized gains, and show the downstream impact of changes." | https://smartpm.com/schedule-controls |
| **Scenarios / TIA** | Controls tier includes "What-if scenarios and **time impact analysis**" | https://smartpm.com/pricing |
| **Analytics set** | Schedule Quality Grade, Project Health Index, End Date Variance, Critical Path Delay, Predicted Completion, SPI, Schedule Compression, Feasibility Signals, Planned Impact | https://smartpm.com/features/construction-schedule-analytics |
| **Open API** | "secure access to both raw schedule data and all the metrics we calculate… No extra fees. No limits on users." Power BI, Tableau, Domo, PMIS/ERP | https://smartpm.com/features/construction-data-api |

**What SmartPM does NOT have — verified, not inferred.** The analytics feature page lists no claims,
disputes, change-order, notice or entitlement functionality
(https://smartpm.com/features/construction-schedule-analytics). Its Procore integration is
**schedule-file-only and one-directional**: "uploading your project schedule to Procore, push your
schedule file to SmartPM" in **XER or MPP** format; the help docs make **no mention** of syncing RFIs,
change orders or daily logs (https://help.smartpm.com/procore-integrations). The Egnyte integration
syncs *files* from a mapped folder every 8 hours (https://help.smartpm.com/egnyte-integrations) — it
is a schedule-file fetcher, not a document-understanding pipeline.

### 2.2 nPlan

| Module | What it does | Evidence |
|---|---|---|
| **Portfolio** | "The world's first AI-powered platform for quantifying portfolio deliverability and risk" | https://www.nplan.io/products-overview |
| **Insights Pro / Risk Professional / PM Professional / Core** | ML forecast of activity performance, driving paths, scenario modelling, QSRA | https://www.nplan.io/products/insights-pro |
| **Decision Intelligence** | Optimise milestone timing + financial value; explicitly pitched at "project decision-makers seeking alternatives to **consultant-led approaches**" | https://www.nplan.io/products-overview |
| **Insights Contract Risk** | Tailored to **NEC4, JCT, FIDIC, AIA, GC21** collaborative frameworks; audience = commercial and contract managers | https://www.nplan.io/products-overview |
| **Schedule Studio** | "Generate and edit detailed, logic-linked schedules with an AI trained on 750,000 real-world plans" | https://www.nplan.io/products-overview |
| **Schedule Integrity Checker** | Free schedule-composition/integrity tool | https://www.nplan.io/products-overview |
| **AI stack** | Deep learning on ">750,000 programme files"; Graph Neural Networks; in-house Monte Carlo engine handling "programmes with tens of thousands of activities" | https://www.nplan.io/our-ai |

**Critical negative finding:** nPlan's own materials contain **no** causation analysis, no delay
attribution, and no claims/entitlement product. Their Knowledge Base contains **no** articles on
delay claims, entitlement disputes, forensic delay analysis or compensation events
(https://www.nplan.io/knowledge-base). "Insights Contract Risk" is contract-*framework*-aware
reporting for commercial managers — it is **not** compensation-event detection, notice generation or
entitlement matching. This is a forward-looking risk product, not a backward-looking recovery product.

### 2.3 Deltek Acumen — the incumbent consultant toolset

- **Fuse**: "600+ industry-aligned metrics" spanning **DCMA, DOE, NASA, GAO and AACE** standards;
  "Understand exactly what changed between schedule versions using automated forensic tools";
  **half-step delay analysis** to "separate progress from scope changes to accurately attribute delays";
  "produce defensible audit documentation". Works with P6, MS Project, Deltek Open Plan.
  (https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse)
- **Risk & 360**: "quantify cost and schedule uncertainty using transparent Monte Carlo simulation";
  "1,000s of Monte Carlo simulations in seconds"; AI risk surfacing; models acceleration/recovery
  scenarios (https://www.deltek.com/en/products/project-and-portfolio-management/acumen/risk).
- **Touchstone**: automated schedule submittal portal that scores incoming schedules; maintains
  **"full audit trails"** and version-controlled acceptance histories for IBRs and audits
  (https://www.deltek.com/en/products/project-and-portfolio-management/acumen).

Note the vocabulary overlap: **Deltek and SmartPM both sell "half-step delay analysis."** SmartPM's
product is, functionally, Acumen Fuse's forensic comparison rebuilt as a cloud service with
continuous ingestion. Steelray sells the same arithmetic per-seat at a sixth of the price.

### 2.4 ALICE Technologies

Three products — **ALICE Plan** (2D schedule over drawings), **ALICE Optimize** (optimise from a P6/MSP
file), **ALICE Model** (generate from BIM). Core claim: "automates 'what-if' scenario exploration with
AI — enabling you to rapidly test construction strategies, mitigate risk, and optimize schedules,"
simulating "millions of possible construction approaches," with explicit **delay recovery /
acceleration modelling** (https://www.alicetechnologies.com/).

**Relevance to the thesis:** ALICE is genuinely strong on **dimension 18 (schedule_impact_analysis)**
in its *prospective, mitigation* sense — "what does it cost in time and resource to recover 40 days"
is a real acceleration-claim input. But its performance-analysis page contains **no mention** of delay
analysis, delay attribution, claims support or change-order impact
(https://www.alicetechnologies.com/construction-project-performance-analysis-software). ALICE is an
optioneering tool, not an entitlement tool.

### 2.5 Nodes & Links

Features: **Delay Navigator**, Change Control, Schedule Risk Analysis, Schedule Integrity, Progress,
EVM, Portfolio, AI Reports (https://www.nodeslinks.com/). This is the most claims-adjacent
*positioning* in the category:

- Delay Navigator "inspects the specified activity, tracking through predecessors to reveal the start
  delay," then computes downstream impact; explicitly lists **"Gather evidence for use in disputes"**
  as a capability (https://nodeslinks.com/features/delay-navigator/).
- Activity-code filtering lets a user see "which suppliers, activities, or contractors contribute
  most to delays" — the nearest thing in this category to responsibility attribution, and it works
  only if the schedule is coded by responsible party.
- Their trust page frames outputs as "answers that directly leverage established fundamentals, and
  which you can directly verify… you can trace, trust, and sign off on"
  (https://nodeslinks.com/why-trust-our-ai/).
- **But**: neither AACE RP 29R-03 nor the SCL Protocol is mentioned anywhere on the Delay Navigator
  page, and there is no explicit claim about admissibility or use in formal dispute resolution.

### 2.6 The classic forensic tooling (the honest benchmark)

**Steelray Delay Analyzer** is the most methodologically explicit product I found in the entire
category, and its self-description is the cleanest statement of the category's ceiling:

> Employs "the Daily Progress Method to run a half-step analysis, **per AACE RP 29R-03**."
> **"The tool does not attribute responsibility to parties."** It provides objective analysis of
> *what changed* and *how those changes affected* the timeline, and "leaves interpretation of
> causation and fault to the analyst or expert witness."
> "Delay Analyzer is the choice of the industry experts, the professionals who are paid to conduct
> delay analyses." — https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php

**Ron Winter Consulting Schedule Analyzer Forensic** — "the complete and only set of software tools
for the Claims Analyst" (https://www.ronwinterconsulting.com/); **$2,750 perpetual single-user**
(http://scheduleanalyzer.com/eforensic_order.htm). Sold to the human expert, priced like a tool, not
a platform. That price point is the market's honest valuation of "automated delay quantification"
when sold without a SaaS wrapper.

---

## 3. THE STANDARDS — AND WHAT IS ACTUALLY AUTOMATABLE

This is the section that determines whether "schedule-impact analysis" can be productised at all by
a solo founder. Answer: **the arithmetic can; the opinion cannot.**

### 3.1 AACE International RP 29R-03, *Forensic Schedule Analysis*

- **Rev. April 25, 2011** (prior revisions 23 June 2009 and 25 June 2007). **136 pages.** Lead authors
  Kenji P. Hoshino, John C. Livengood, Christopher W. Carson; 20+ named contributors including
  Richard J. Long, Ron Winter, James G. Zack Jr.
  (https://web.aacei.org/docs/default-source/toc/toc_29r-03.pdf). RPs are free to AACE members and
  purchasable by non-members (https://web.aacei.org/resources/publications/recommended-practices).
  `UNVERIFIED`: whether a post-2011 revision exists — the current sample PDF served by AACE is the
  2011 revision.

**The layered taxonomy (Layer 1 Timing → Layer 2 Basic Method → Layer 3 Specific Method → MIP):**

| MIP | Classification | Common name |
|---|---|---|
| 3.1 | Observational / Static / Gross | As-planned vs as-built (project-wide) |
| 3.2 | Observational / Static / Periodic | As-planned vs as-built, windowed |
| 3.3 | Observational / Dynamic / Contemporaneous As-Is | Contemporaneous period / windows analysis on native updates |
| 3.4 | Observational / Dynamic / Contemporaneous Split | **Half-step** — splits progress from revisions within each period |
| 3.5 | Observational / Dynamic / Modified or Recreated | Windows on reconstructed updates |
| 3.6 | Modeled / Additive / Single Base | Impacted as-planned |
| 3.7 | Modeled / Additive / Multiple Base | Time impact analysis (stepped insertion) |
| 3.8 | Modeled / Subtractive / Single Simulation | Collapsed as-built / but-for |
| 3.9 | Modeled / Subtractive / Multiple Base | Windowed collapsed as-built |

(Taxonomy table cross-checked against Long International's summary,
https://www.long-intl.com/articles/schedule-analysis-method-2/, and against the RP's own
Appendix B taxonomy figure in the sample PDF.)

**Every one of the nine MIPs has the SAME sub-step structure**, and steps G–J are where the money is:

- G. Identification of Critical and Near-Critical Paths ← *computable*
- H. Identification and Quantification of **Concurrent Delays and Pacing** ← *judgement*
- I. Determination and Quantification of **Excusable and Compensable Delay** (ECD / END / NND) ← *judgement + contract*
- J. Identification and Quantification of **Mitigation / Constructive Acceleration** ← *judgement*

The RP also contains, verbatim as section headings: **§2.3.A.1.d "Delay Characterization is
Independent of Responsibility"**, **§2.3.A.4 "Cause of Variance"**, **§2.3.A.5 "Assigning or Assuming
Variance Responsibility" (a. Contractor Delay, b. Owner Delay, c. Force Majeure Delay)**, and
**§4.3.D.7 "Judgment Calls During the Forensic Process."**

**The four load-bearing quotes (all from the RP's own §1, sample PDF pp. 9–11):**

1. *"Forensic schedule analysis, like many other technical fields, is both a science and an art. As
   such, it relies upon professional judgment and expert opinion and usually requires many subjective
   decisions."*
2. *"All methods are subject to manipulation as they all involve judgment calls by the analyst whether
   in preparation or in interpretation."* (§1.2.d)
3. *"No forensic schedule analysis method is exact. The level of accuracy of the answers produced by
   each method is a function of the quality of the data used therein, the accuracy of the assumptions,
   and the subjective judgments made by the forensic schedule analyst."* (§1.2.e)
4. *"Schedules are a project management tool that, in and of themselves, do not demonstrate root
   causation or responsibility for delays."* (§1.2.f)

And a direct warning shot at automated black boxes: the RP's stated aim is to "increase both the
accountability and the **testability** of an opinion and minimize the need to contend with
**'black-box' or 'voodoo' analyses**" (§1.1).

**Section 5, "Choosing a Method", lists 11 selection factors** — contractual requirements, purpose of
analysis, source data availability/reliability, size of dispute, complexity, **budget**, **time
allowed**, **expertise of the analyst**, forum and audience, legal/procedural requirements, custom and
usage. Note factors 6, 7 and 8: method choice is partly an economics-and-staffing decision. That is
precisely the decision an automation product could disrupt — but only for the quantification half.

### 3.2 SCL Delay and Disruption Protocol, 2nd edition (February 2017)

Free PDF: https://www.scl.org.uk/sites/default/files/documents/SCL_Delay_Protocol_2nd_Edition_Final.pdf
Landing page: https://www.scl.org.uk/resources/delay-disruption-protocol/ — 38,500+ downloads across
142 countries between 2005 and April 2018 (UK 33%, UAE 9%, Australia 6%, Qatar 5%).

**Key change in the 2nd ed.:** *"There is **no longer a preferred delay analysis methodology** where
that analysis is carried out time-distant from the delay event or its effect."* (Introduction, ¶K(c)).
Method choice is now driven by 8 criteria (Part B §11.3), including "the nature, extent and quality of
the records available."

**The six methods (Part B §11.5 table, reproduced verbatim in structure):**

| Method | Analysis type | Critical path determined | Delay impact determined | Requires |
|---|---|---|---|---|
| Impacted As-Planned | Cause & Effect | Prospectively | Prospectively | Logic-linked baseline; a selection of delay events to be modelled |
| Time Impact Analysis | Cause & Effect | Contemporaneously | Prospectively | Logic-linked baseline; update programmes/progress info; a selection of delay events |
| Time Slice Windows | Effect & Cause | Contemporaneously | Retrospectively | Logic-linked baseline; update programmes/progress info |
| As-Planned vs As-Built Windows | Effect & Cause | Contemporaneously | Retrospectively | Baseline programme; as-built data |
| Retrospective Longest Path | Effect & Cause | Retrospectively | Retrospectively | Baseline programme; as-built programme |
| Collapsed As-Built | Cause & Effect | Retrospectively | Retrospectively | Logic-linked **as-built** programme; a selection of delay events |

**Concurrency (Core Principle 10):** *"True concurrent delay is the occurrence of two or more delay
events at the same time, one an Employer Risk Event, the other a Contractor Risk Event… Where
Contractor Delay to Completion occurs or has an effect concurrently with Employer Delay to Completion,
the Contractor's concurrent delay should not reduce any EOT due."*

**Entitlement ≠ money (Core Principle 12):** *"Entitlement to an EOT does not automatically lead to
entitlement to compensation (and vice versa)."* Note the "non-compensable Employer Risk Event"
category (e.g. adverse weather) — the owner bears time risk, the contractor bears cost risk. A naive
"delay days × daily rate" estimator is therefore **wrong by construction** for a large class of events.

**Records (Core Principle 1 + Appendix B):** six categories — programme, progress, resource, costs,
correspondence and administration, contract and tender documents. The Protocol's own diagnosis of
why claims fail: *"Those who assess delay and disruption claims often find that there is uncertainty
and a lack of records regarding what was delayed and/or disrupted and what and how parts of the works
were affected by delay or disruption events."*

### 3.3 THE AUTOMATABILITY TABLE (the answer to "can this be productised?")

| Step in any recognised method | Automatable today? | Who has automated it | Notes |
|---|---|---|---|
| Parse P6/MSP/Asta/Phoenix files, diff versions | **YES — fully** | SmartPM, Acumen Fuse, Steelray, N&L, nPlan | Commodity. Open-source XER parsers exist. |
| Schedule quality / integrity scoring (DCMA 14-point etc.) | **YES — fully** | SmartPM (35+), Acumen Fuse (600+), nPlan (free checker), N&L | Commodity; nPlan gives it away free. |
| Compute critical & near-critical path per update | **YES — fully** | All of the above | Pure CPM arithmetic. |
| Quantify in-period critical delay / gains / planned impact (**half-step**, MIP 3.4) | **YES — fully** | SmartPM, Acumen Fuse, Steelray | **This is the entire "automated delay analysis" market.** |
| Impacted as-planned / TIA (insert fragnet, recalculate) | **Mechanically yes; event & fragnet selection is judgement** | SmartPM Controls ("time impact analysis"), Acumen, ALICE | *Which* events, and *what the fragnet looks like*, is an opinion. SCL: the analyst must verify sequences are "reasonable, realistic and achievable." |
| Retrospective longest path trace | **YES, given a verified as-built** | Schedule Analyzer eForensic, Steelray | Verification of the as-built is manual. |
| **As-built reconstruction where native updates are missing** | **NO** | — | AACE §2.2 special procedure "Creating an Independent As-Built from Scratch ('Daily Specific As-Built')". Requires reading daily reports. |
| **Collapsed as-built (MIP 3.8/3.9)** | **NO** | — | SCL §11.6(f): *"It is rare that such a programme would exist… the analyst is usually required to introduce logic to a verified as-built programme. This can be a time consuming and complex endeavour."* |
| **As-planned vs as-built windows critical path** | **NO — explicitly** | — | SCL §11.6(d): *"The analyst determines the contemporaneous or actual critical path in each window by a common-sense and practical analysis of the available facts. As this task does not substantially rely on programming software…"* |
| **CAUSATION: linking quantified delay to a delay event** | **NO — nobody has** | — | SCL §11.6(c)/(d): *"Thereafter, the analyst investigates the project records to determine what events might have caused the identified critical delay."* **← the wedge** |
| **RESPONSIBILITY: Employer Risk Event vs Contractor Risk Event** | **NO — excluded by the standard** | — | AACE §1.3(c); §1.2(f). |
| **Excusable / compensable classification (ECD / END / NND)** | **NO** | — | Step "I" of all nine MIPs. Requires the contract's risk allocation. |
| **Concurrency & pacing findings** | **NO — highest-judgement step** | — | AACE §4.2 lists 6 families of factors that change the answer: literal vs functional concurrency; least float vs negative float; cause vs effect; frequency/duration/placement of analysis intervals; order of insertion/extraction; **hindsight vs blindsight**. Long International: *"the placement of cut-off date plays a major role."* |
| **Quantum ($) of the recoverable claim** | **NO — different discipline** | — | Not in any of these tools. Prolongation, disruption, acceleration, HOOH (Hudson/Emden/Eichleay) are separate. |

**Bottom line: rows 1–6 are done and commoditised. Rows 7–14 are untouched. Rows 11–13 are the
thesis.** Note that rows 11–13 are *document-reasoning* problems, not *schedule-mathematics* problems —
which is exactly the shape LLMs are good at and CPM engines are not.

---

## 4. CAPABILITY MATRIX — 26 DIMENSIONS

### 4A. COMBINED BEST-OF-CATEGORY
*(the single highest score achieved by ANY tool in this category — SmartPM, nPlan, Acumen, ALICE,
Nodes & Links, Steelray, Schedule Analyzer, Contilio)*

`SCORES| 1,0,1,1,1,0,1,3,1,1,3,1,1,2,1,1,0,3,3,3,0,1,3,3,1,2`

| # | Dimension | Score | Justification + URL |
|---|---|---|---|
| 1 | contract_ingestion | **1** | Best is SmartPM's Egnyte connector, which syncs *files* from a mapped folder every 8h — file access, zero contract parsing. https://help.smartpm.com/egnyte-integrations |
| 2 | clause_extraction | **0** | No tool in the category extracts clauses. nPlan's "Contract Risk" is framework-flavoured reporting for NEC/JCT/FIDIC/AIA/GC21, not clause extraction. https://www.nplan.io/products-overview |
| 3 | notice_detection | **1** | Nearest: nPlan's contract-framework orientation for commercial managers and N&L's early-warning-style risk surfacing. No notice-trigger logic anywhere. https://www.nplan.io/products-overview |
| 4 | deadline_tracking | **1** | Milestone & critical-path date tracking (SmartPM Controls) and probabilistic milestone dates (nPlan). Contractual notice deadlines: absent. https://smartpm.com/pricing |
| 5 | rfi_event_ingestion | **1** | `UNVERIFIED`. N&L claims to "integrate project data from multiple sources into a centralized workspace" but names no RFI object. SmartPM's Procore sync is schedule-only. https://help.smartpm.com/procore-integrations |
| 6 | email_ingestion | **0** | No product in the category ingests email. |
| 7 | daily_report_ingestion | **1** | Only Contilio touches field reality, and via 3D scans/images, not daily reports. https://www.contilio.com/ |
| 8 | schedule_integration | **3** | The category's whole reason to exist. P6 XER/XML, MSP, Asta PowerProject, Phoenix; Procore, ACC, Oracle Primavera Cloud, open API. https://smartpm.com/, https://smartpm.com/features/construction-data-api |
| 9 | change_order_workflow | **1** | N&L "Change Control — logs and traces every modification with immediate critical path impact visibility" — that is *schedule* change control, not a commercial change-order workflow. https://www.nodeslinks.com/ |
| 10 | claim_identification | **1** | SmartPM markets "a defensible basis for delay claims and time extension requests" and N&L "gather evidence for use in disputes" — but neither creates a claim object or tests entitlement. https://smartpm.com/features/delay-analysis, https://nodeslinks.com/features/delay-navigator/ |
| 11 | delay_detection | **3** | Best-in-class and fully automated: half-step windows quantification of in-period delay, gains and planned impact on every update. https://help.smartpm.com/key-delay-metrics, https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php |
| 12 | **responsibility_attribution** | **1** | **The category's defining gap.** Best available is activity-code filtering to see which supplier/subcontractor's activities drove delay (N&L), which requires a responsibility-coded schedule and attributes *within* the contractor's supply chain, not owner-vs-contractor. Steelray states flatly: "The tool does not attribute responsibility to parties… leaves interpretation of causation and fault to the analyst or expert witness." https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php |
| 13 | contemporaneous_evidence_graph | **1** | Versioned schedule-update history is a genuine contemporaneous record — but it is a record of *one* document type, with no links to correspondence, RFIs, minutes or photos. https://smartpm.com/schedule-controls |
| 14 | evidence_completeness | **2** | Strong but schedule-only: Acumen Fuse 600+ metrics against DCMA/DOE/NASA/GAO/AACE; Touchstone maintains version-controlled acceptance histories; SmartPM 35+ checks. https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse |
| 15 | recoverable_dollar_estimation | **1** | Acumen Risk quantifies **cost uncertainty** via Monte Carlo; nPlan quantifies milestone financial value. Nothing computes a recoverable claim value. https://www.deltek.com/en/products/project-and-portfolio-management/acumen/risk |
| 16 | claim_package_generation | **1** | Output is exhibits, not packages: charts, delay tables and exportable reports that a human pastes into an expert report. Acumen: "produce defensible audit documentation." https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse |
| 17 | notice_drafting | **0** | Absent everywhere. |
| 18 | schedule_impact_analysis | **3** | Genuinely strong across the category: SmartPM Controls "what-if scenarios and time impact analysis"; Acumen Risk models acceleration/recovery scenarios; ALICE simulates millions of build strategies; nPlan runs scenario/mitigation modelling. https://smartpm.com/pricing, https://www.alicetechnologies.com/ |
| 19 | procore_integration | **3** | SmartPM has a Procore Marketplace listing and embedded analytics; sync is real but schedule-file-only. https://marketplace.procore.com/apps/smartpm |
| 20 | autodesk_integration | **3** | SmartPM analytics embed directly in Autodesk Build Insights / BIM 360 Project Home dashboards (announced 1 Nov 2023). https://smartpm.com/press/integration-with-autodesk-construction-cloud |
| 21 | outlook_gmail_integration | **0** | None. |
| 22 | mobile_workflow | **1** | `UNVERIFIED`. Only Contilio implies field capture. No delay-analytics vendor markets a mobile app. |
| 23 | audit_trail | **3** | Deltek Acumen Touchstone: "full audit trails" + version-controlled acceptance histories for compliance reviews, IBRs and audits — marketed, native. https://www.deltek.com/en/products/project-and-portfolio-management/acumen |
| 24 | portfolio_risk | **3** | nPlan Portfolio ("quantify portfolio deliverability and risk"); SmartPM portfolio-wide insights across up to 50 Essentials projects; N&L Portfolio. https://www.nplan.io/products-overview, https://smartpm.com/pricing |
| 25 | performance_pricing_compatibility | **1** | All fixed subscription/licence. SmartPM's per-project slot model is the only structure that even *maps* to project-level value. No success-fee or gain-share evidenced anywhere. https://smartpm.com/pricing |
| 26 | consultant_replacement_potential | **2** | Real but partial — they replace the analyst's *arithmetic*, not the expert's *opinion*. Layton customer: "The Windows Analysis is a game changer. What used to take me weeks or months on some projects now takes minutes or hours." nPlan Decision Intelligence is explicitly for buyers "seeking alternatives to consultant-led approaches." https://smartpm.com/schedule-controls, https://www.nplan.io/products-overview |

### 4B. SmartPM (individual row)

`SCORES| 1,0,0,1,0,0,0,3,0,1,3,1,1,1,0,1,0,3,3,3,0,0,2,3,1,2`

| # | Dimension | Score | Justification |
|---|---|---|---|
| 1 | contract_ingestion | 1 | Egnyte file sync only; no parsing. https://help.smartpm.com/egnyte-integrations |
| 2 | clause_extraction | 0 | Absent. |
| 3 | notice_detection | 0 | Absent. |
| 4 | deadline_tracking | 1 | "Milestone & Critical Path Tracking" (Controls tier) — schedule dates, not contractual deadlines. https://smartpm.com/pricing |
| 5 | rfi_event_ingestion | 0 | Procore sync is schedule-file only; help docs mention no RFIs. https://help.smartpm.com/procore-integrations |
| 6 | email_ingestion | 0 | Absent. |
| 7 | daily_report_ingestion | 0 | Absent. |
| 8 | schedule_integration | 3 | P6 (XER/XML), MSP, Asta PowerProject, Phoenix + Procore/ACC/OPC/Egnyte + open API. https://smartpm.com/ |
| 9 | change_order_workflow | 0 | "Change logs" = schedule revision deltas, not commercial change orders. |
| 10 | claim_identification | 1 | Positioning ("Out of Court", "defensible basis for delay claims") without a claim object. https://smartpm.com/features/delay-analysis |
| 11 | delay_detection | 3 | Four computed metrics on every update: End Date Variance, In-Period Delay, In-Period Gains, Planned Impact; automated windows/half-step. https://help.smartpm.com/key-delay-metrics |
| 12 | responsibility_attribution | 1 | **See §5. Marketing implies it; the docs do not deliver it.** Their own help centre: the framework "focuses on quantifying schedule variance rather than assigning causation." Their own blog: "Delay causation is rarely singular; it requires proving sequence and responsibility with verifiable schedule data" — i.e. the analyst proves it, the software supplies the data. https://smartpm.com/blog/portfolio-level-construction-delay-analysis |
| 13 | contemporaneous_evidence_graph | 1 | Full versioned history of every schedule update is real contemporaneous evidence — of one document type only. |
| 14 | evidence_completeness | 1 | Schedule Quality Checker (35+ checks) assesses whether the *schedule* is fit for analysis. https://smartpm.com/schedule-quality-checker |
| 15 | recoverable_dollar_estimation | 0 | No cost/quantum module. Output is delay days. |
| 16 | claim_package_generation | 1 | "Exportable change and quality reports", "customizable reports with scheduled delivery". Exhibits, not packages. https://smartpm.com/pricing |
| 17 | notice_drafting | 0 | Absent. |
| 18 | schedule_impact_analysis | 3 | Controls tier: "What-if scenarios and time impact analysis"; scenario simulations in Project Workspace. https://smartpm.com/pricing, https://smartpm.com/project-workspace |
| 19 | procore_integration | 3 | Marketplace app + embedded views; one-way schedule push. https://marketplace.procore.com/apps/smartpm |
| 20 | autodesk_integration | 3 | Embedded in Autodesk Build Insights / BIM 360 Project Home. https://smartpm.com/press/integration-with-autodesk-construction-cloud |
| 21 | outlook_gmail_integration | 0 | Absent. |
| 22 | mobile_workflow | 0 | No mobile product evidenced. |
| 23 | audit_trail | 2 | Schedule revision history + change logs + report archive; no evidence of a legal-grade user-action audit log. https://smartpm.com/project-workspace |
| 24 | portfolio_risk | 3 | Executive/Company dashboards, portfolio-wide insights, Essentials covers up to 50 projects. https://smartpm.com/pricing |
| 25 | performance_pricing_compatibility | 1 | Flat annual tiers with per-project "controls slots"; no outcome pricing. https://smartpm.com/pricing |
| 26 | consultant_replacement_potential | 2 | Replaces the quantification labour ("weeks or months → minutes or hours"), not the expert opinion. https://smartpm.com/schedule-controls |

### 4C. nPlan (individual row)

`SCORES| 0,0,1,1,0,0,0,3,0,0,2,0,0,1,1,0,0,3,0,0,0,0,1,3,1,2`

| # | Dimension | Score | Justification |
|---|---|---|---|
| 1 | contract_ingestion | 0 | No contract ingestion. |
| 2 | clause_extraction | 0 | Absent. |
| 3 | notice_detection | 1 | "Insights Contract Risk" is tailored to NEC4/JCT/FIDIC/AIA/GC21 and aimed at commercial/contract managers — adjacent only. https://www.nplan.io/products-overview |
| 4 | deadline_tracking | 1 | Probabilistic milestone dates, not contractual deadlines. https://www.nplan.io/products/insights-pro |
| 5–7 | rfi / email / daily report ingestion | 0 | Schedules only. |
| 8 | schedule_integration | 3 | P6, MSP, PowerProject; exports to Power BI / Tableau. https://www.nplan.io/products/insights-pro |
| 9 | change_order_workflow | 0 | Absent. |
| 10 | claim_identification | 0 | Absent. Knowledge Base contains no articles on delay claims, entitlement, disputes or forensic delay analysis. https://www.nplan.io/knowledge-base |
| 11 | delay_detection | 2 | Prospective/probabilistic: forecasts delay risk, ranks risky activities, shows driving paths. Not retrospective forensic quantification. https://www.nplan.io/our-ai |
| 12 | responsibility_attribution | 0 | Nothing. Their AI materials do not address causation, attribution or disputes at all. https://www.nplan.io/our-ai |
| 13 | contemporaneous_evidence_graph | 0 | Absent. |
| 14 | evidence_completeness | 1 | Free Schedule Integrity Checker — schedule composition only. https://www.nplan.io/products-overview |
| 15 | recoverable_dollar_estimation | 1 | "Decision Intelligence… optimise milestone timing and financial value"; savings claims. Not recoverable-claim value. https://www.nplan.io/products-overview |
| 16 | claim_package_generation | 0 | Absent. |
| 17 | notice_drafting | 0 | Absent. |
| 18 | schedule_impact_analysis | 3 | ML forecasting + GNN + in-house Monte Carlo over "programmes with tens of thousands of activities"; scenario/mitigation testing; QSRA. https://www.nplan.io/our-ai |
| 19 | procore_integration | 0 | Not evidenced. |
| 20 | autodesk_integration | 0 | Not evidenced. |
| 21 | outlook_gmail_integration | 0 | Absent. |
| 22 | mobile_workflow | 0 | Absent. |
| 23 | audit_trail | 1 | Not marketed; forecasts presumably versioned. `UNVERIFIED`. |
| 24 | portfolio_risk | 3 | nPlan Portfolio is the flagship — "the world's first AI-powered platform for quantifying portfolio deliverability and risk." https://www.nplan.io/products-overview |
| 25 | performance_pricing_compatibility | 1 | Enterprise negotiated; savings-based *selling* ($1.2B claimed) but no evidenced gain-share contracts. |
| 26 | consultant_replacement_potential | 2 | Explicitly positioned as an alternative to consultant-led QSRA. https://www.nplan.io/products-overview |

---

## 5. THE DIMENSION-12 INVESTIGATION: DOES SmartPM ATTRIBUTE RESPONSIBILITY?

This was the assignment's hardest question. The answer is **no — and the gap between their marketing
copy and their product documentation is itself the finding.**

**What the marketing says (feature page):**
- "**Automated, Forensic-Grade** Construction Half-Step Delay Analysis Software"
- "applies a windows analysis approach automatically across each period"
- provides "**a defensible basis for delay claims and time extension requests**"
- helps teams "build a **defensible record**"
- on concurrency: "courts often deny both time extensions and damages when delays are genuinely
  concurrent," and SmartPM helps by "**isolating which activities drove the slip**"
  (https://smartpm.com/features/delay-analysis)

Note the careful verb: *isolating which activities drove the slip* — activities, not parties.

**What the product documentation says:**
The Key Delay Metrics page defines exactly four metrics (End Date Variance, In-Period Delay,
In-Period Gains, Planned Impact) and — in my extraction — contains **no** root-cause attribution,
responsibility assignment or formal delay-type classification. The framework "focuses on quantifying
schedule variance rather than assigning causation." (https://help.smartpm.com/key-delay-metrics)

**What their own blog concedes:**
- "Delay causation is rarely singular; it requires proving sequence and responsibility with
  **verifiable schedule data**" — the software supplies the data; a human proves responsibility.
- On excusable vs non-excusable: "Delay analysis establishes which category applies by **tracing
  causation through the schedule record**" — i.e. a human traces it.
- "without strong document management discipline, scope creep, owner-caused delay, and
  contractor-caused delay become **impossible to separate with confidence**."
  (https://smartpm.com/blog/portfolio-level-construction-delay-analysis)

That last sentence is SmartPM telling you, in their own SEO content, that the problem they do not
solve is a *document* problem.

**Their FAQ tell:** the delay-analysis page carries an FAQ headed "What is the difference between
excusable and compensable delays?" — and the answer does not address the distinction; it redirects to
general benefits of project-controls software. A vendor that could classify ECD/END/NND would answer
that question with a screenshot.

**Corroboration from the rest of the category.** Steelray, which implements the *same* AACE half-step
method, states without hedging: **"The tool does not attribute responsibility to parties… leaves
interpretation of causation and fault to the analyst or expert witness"**
(https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php). Nodes & Links' Delay Navigator traces
predecessors to find the origin of a start delay and can filter by activity code to show which
suppliers/contractors' activities contribute most — but assigns no owner-vs-contractor liability and
cites neither AACE nor SCL (https://nodeslinks.com/features/delay-navigator/). Deltek's Fuse page
uses the phrase "accurately attribute delays" but the mechanism described is "separate progress from
scope changes" — attribution to a *category of schedule movement*, not to a *contracting party*
(https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse).

**Verdict on dimension 12 across the whole category: 1/3, and it is a hard 1.** Nobody is at 2.

---

## 6. PRICING

| Vendor | Published price | Confidence | Method |
|---|---|---|---|
| **SmartPM Essentials** | **$12,000/year**, up to 50 projects, unlimited users, standard support | **HIGH** | Published on vendor pricing page, https://smartpm.com/pricing |
| **SmartPM Controls** | **$25,000/year**, 5 controls slots (expandable), Essentials projects retained, adds full analytics, interactive Gantt, **what-if + time impact analysis**, portfolio insights, premium support | **HIGH** | Same page |
| SmartPM trial | "Try SmartPM Risk-Free for 60 Days"; mid-contract upgrade with credit | HIGH | Same page |
| SmartPM (3rd-party) | "$400/project/month" single plan | LOW | Aggregator claim (softwarefinder.com / pricingnow.com); contradicts vendor page structure. Treat vendor page as authoritative. SoftwareAdvice lists SmartPM pricing as "Available upon request" (https://www.softwareadvice.com/construction/smartpm-profile/) |
| **Steelray Delay Analyzer** | **$3,990 per user per year** or **$390 per user per month**; unlimited projects, support and updates included | **HIGH** | https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php |
| **Schedule Analyzer eForensic** (Ron Winter) | **$2,750 perpetual single-user license**; 10% off for 4+; 5% off if bought with Schedule Analyzer | **HIGH** | http://scheduleanalyzer.com/eforensic_order.htm |
| **Deltek Acumen (Fuse / Risk / 360 / Touchstone)** | **No published price.** Quote-only. | — | Product pages carry no pricing (https://www.deltek.com/en/products/project-and-portfolio-management/acumen). `UNVERIFIED`. Weak proxy: Vendr reports a **median Deltek contract of $20,380/yr across 33 purchases, range $9,248–$63,900** — but that is all Deltek products, not Acumen specifically (https://www.vendr.com/buyer-guides/deltek) |
| **nPlan** | **No published price.** Enterprise custom, negotiated on project count and portfolio size. | — | No pricing on any nPlan product page; aggregators confirm quote-only. `UNVERIFIED` |
| **ALICE Technologies** | **No published price.** | — | https://www.alicetechnologies.com/ — demo-request only. `UNVERIFIED` |
| **Nodes & Links** | **No published price.** | — | https://www.nodeslinks.com/ — demo-request only. `UNVERIFIED` |
| **Contilio** | **No published price.** | — | https://www.contilio.com/. `UNVERIFIED` |

**The price signal that matters for the thesis:** the *identical* AACE-compliant half-step delay
computation is available at **$3,990/user/yr (Steelray)**, **$2,750 one-time (Ron Winter)**, and
**$25,000/yr (SmartPM Controls)**. SmartPM's 6–9× premium is being paid for continuous ingestion,
portfolio dashboards, unlimited users and a modern UI — **not** for a better answer. That is a
commodity core with a workflow wrapper. A new entrant cannot win here on the math; it can only win by
answering a question the math does not answer.

---

## 7. INTEGRATIONS & API — DATA EGRESS REALITY

**SmartPM (most open in the category):**
- **Open API**: "secure access to both **raw schedule data** and all the metrics we calculate… No
  extra fees. No limits on users. No heavy lift." Named consumers: Power BI, Tableau, Domo, internal
  PMIS/ERP (https://smartpm.com/features/construction-data-api). This is unusually generous and makes
  SmartPM an excellent *upstream supplier* to a claims product.
- **Procore**: Marketplace app; **one-way, schedule-file-only** (XER or MPP); insights render back
  inside Procore (https://help.smartpm.com/procore-integrations, https://marketplace.procore.com/apps/smartpm).
- **Autodesk Construction Cloud**: analytics embedded in Build Insights / BIM 360 Project Home,
  announced 1 Nov 2023 (https://smartpm.com/press/integration-with-autodesk-construction-cloud;
  https://www.businesswire.com/news/home/20231101465262/en/).
- **Egnyte**: folder-mapped file sync every 8 hours (https://help.smartpm.com/egnyte-integrations).
- **Oracle Primavera Cloud (OPC)** connector (https://help.smartpm.com/smartpm-set-up).
- File formats: **P6 XER/XML, MS Project, Asta PowerProject, Phoenix** (https://smartpm.com/).

**nPlan**: P6, MSP, PowerProject in; Power BI and Tableau out. No Procore/ACC integration evidenced.
**Deltek Acumen**: P6, MS Project, Deltek Open Plan. Desktop-rooted.
**Nodes & Links**: "P6-compatible models"; ISO 27001; multi-source data workspace claimed but
objects not enumerated.
**ALICE**: imports P6 / MSP files; BIM models for ALICE Model.

**The structural point:** every integration in this category terminates at the schedule file. Not one
vendor has built a pipe to RFIs, submittals, daily logs, meeting minutes, correspondence or email —
even where they already hold an authenticated Procore or ACC connection that *could* carry them. That
is a deliberate scoping choice (see §8), and it means the category has authenticated access to the
customer's PM system and is not using it for entitlement.

---

## 8. WEAKNESSES AND EXPLICIT GAPS — DELIBERATE OR UNATTENDED?

| Gap | Deliberate or unattended? | Evidence / reasoning |
|---|---|---|
| **No responsibility attribution (dim 12)** | **DELIBERATE — and standards-backed** | AACE §1.3(c) explicitly scopes forensic schedule analysis to "factual analysis and quantification **as opposed to** assignment of delay responsibility." Steelray says so outright. Attribution invites expert-witness liability and contradicts the "unbiased/neutral analytics" positioning that lets SmartPM sell to *both* owners and GCs. **Do not read this as white space without pairing it to paid pain.** |
| **No contract, no clauses, no notices (dims 1–4, 17)** | **DELIBERATE** | These are project-controls companies selling to schedulers. Contract administration is a different buyer, a different budget and a different risk profile. nPlan's "Contract Risk" product shows they *know* the commercial-manager persona exists and have chosen to serve it with risk reporting, not entitlement. |
| **No RFI / daily report / email ingestion (dims 5–7)** | **DELIBERATE, but softening** | SmartPM already holds Procore and ACC OAuth tokens and pulls only the schedule file. Egnyte was added to fetch schedule files from document stores — the connector exists, the *ambition* does not. This is the most attackable gap because the plumbing is half-built. |
| **No dollar quantum (dim 15)** | **DELIBERATE** | Cost is a different data source (ERP/job cost) and a different sale. Acumen Risk models cost *uncertainty*, not recoverable *entitlement*. |
| **Outputs are exhibits, not claim packages (dim 16)** | **DELIBERATE** | The category sells to the person who builds the exhibit. Producing the claim narrative crosses into legal work product. |
| **SmartPM's premium over Steelray/Ron Winter for the same math** | **UNATTENDED / structural risk** | 6–9× price for commoditised arithmetic. Defensible only while the workflow wrapper and portfolio view are worth more than the computation. |
| **Delay-analysis UI complexity** | **UNATTENDED** | Repeated in reviews (see §9). Suggests the automated output still needs an expert to interpret — undercutting "automated". |
| **nPlan's total absence from retrospective/dispute work** | **DELIBERATE** | Their entire GTM is forward-looking risk for owners of mega-programmes. Entering claims would put them opposite their own customers (owners are usually the defendant). |
| **ALICE has no delay-attribution surface at all** | **DELIBERATE** | Optioneering tool. Their performance-analysis page does not mention claims, change orders or attribution. |

---

## 9. ADJACENCY TEST — HOW HARD FOR THEM TO SHIP THE FULL PIPELINE?

**Pipeline:** commercial event detection → entitlement/notice matching → evidence collection →
recoverable-value estimate → notice/claim package.

| Vendor | Verdict | Reasoning |
|---|---|---|
| **SmartPM** | **MEDIUM** | *Data access:* best in category — Procore + ACC + Egnyte OAuth already in place; extending scope from schedules to RFIs/daily logs is a scope-request change, not new engineering. *Org incentive:* strong — "Out of Court" is already their tagline and Nemetschek (strategic investor) has adjacent commercial products. *GTM:* wrong buyer — they sell to schedulers; entitlement is bought by commercial/contracts. *Legal exposure:* this is the real brake — they currently sell "neutral analytics" to both owners and contractors; taking a contractor's side on entitlement breaks that. *Shipping behaviour:* small team, $5.5M Series A (May 2024) — capital-constrained relative to the build. **Most likely path: they add causation *tagging* (link a delay window to a Procore RFI/change event) before they ever add entitlement.** |
| **nPlan** | **HARD** | *Data access:* schedules only, and they are proud of that (the moat *is* the schedule corpus). *Org incentive:* negative — their buyers are owners/PMOs (HS2, Network Rail, Chevron, Shell); a contractor-side claims product would put them across the table from the people who pay them. *Legal exposure appetite:* their positioning is probabilistic forecasting, which is deliberately non-adversarial. *M&A/shipping:* $16M Series B is for scaling Portfolio, not for a new adversarial product line. |
| **Deltek Acumen** | **HARD** | Deltek is a large ERP/GovCon company; Acumen is a mature, quote-priced desktop-rooted line. Big-company incentive is to sell more Costpoint/Vantagepoint seats, not to enter contractor-side claims. They already have the *forensic* brand and have not moved in 10+ years. |
| **ALICE** | **HARD** | No documents, no contract surface, no commercial-event concept. Would be a from-scratch second product. |
| **Nodes & Links** | **MEDIUM-HARD** | Closest *language* to disputes ("gather evidence for use in disputes", "auditable answers you can trace, trust, and sign off on") and an AI-agent architecture that could reason over documents. But no evidenced document ingestion, no contract layer, and no published claim-package output. If any incumbent gets there first, it is probably them. |
| **Steelray / Ron Winter** | **HARD** | Deliberately tool-shaped, sold to the expert. Ron Winter Consulting is a consultancy with software; they have every incentive to keep the expert in the loop because the expert *is* the business. |

**Category verdict: MEDIUM (SmartPM) / HARD (everyone else).**

---

## 10. STARTUP POSTURE — PARTNER, CHANNEL, OR ROADKILL?

**PARTNER — strongly, and specifically with SmartPM.**

Reasons:
1. **They have deliberately stopped exactly where the thesis starts.** They compute *what moved*;
   the thesis computes *why and whose fault*. Complements, not substitutes.
2. **Their API is unusually open** — "raw schedule data and all the metrics we calculate… No extra
   fees. No limits on users" (https://smartpm.com/features/construction-data-api). A claims product can
   consume SmartPM's delay windows as an input and never build a CPM engine.
3. **They cannot easily take the attribution step themselves** without breaking their neutral,
   sells-to-both-sides positioning.
4. **Their tagline is already "Out of Court"** — they have created the demand narrative and left the
   delivery gap open.

**CHANNEL — plausible via Procore/ACC marketplaces**, where SmartPM's own listing proves distribution
exists for schedule-adjacent apps.

**ROADKILL risk — LOW but non-zero, and concentrated in one place:** if a startup's V1 is "automated
delay quantification with a nicer UI," it is roadkill immediately — SmartPM, Acumen, Steelray, Nodes &
Links and Ron Winter all already do it, two of them for under $4,000, and nPlan gives schedule-integrity
checking away free. **Do not build the CPM math.**

---

## 11. TOP 5 VERBATIM CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

All from Capterra, SmartPM (4.9/5, 46 reviews) — https://www.capterra.com/p/137005/SmartPM/reviews/

1. **Brady M., Planning and Scheduling Director, 21 Jul 2022** — *"challenged with some of the more
   complex functionality with the **delay analysis feature**"*
   → The flagship automated feature still needs expert interpretation.
   https://www.capterra.com/p/137005/SmartPM/reviews/?page=2
2. **Paul J., Director of Planning and Scheduling, 12 Jun 2024** — *"the chart view in the **delay
   analysis** is difficult to navigate"* → Output legibility problem in the exact module a claims
   product would depend on. https://www.capterra.com/p/137005/SmartPM/reviews/
3. **Seth J., Director of Scheduling, 7 Jun 2024** — concern over *"accuracy of its **SPI
   calculation**, particularly when the planned percentage completion reaches 100%"* → Accuracy
   doubts on a headline metric; a fatal objection if the number is going into an expert report.
   https://www.capterra.com/p/137005/SmartPM/reviews/
4. **Brendan J., Project Controls Manager, 30 May 2024** — *"cannot upload two schedules with the same
   data date"* (echoed by **Sara M., Scheduler, 8 Aug 2022**: *"cant compare two schedules with the
   same data date"*) → **Directly blocks the AACE half-step method (MIP 3.4)**, which requires
   comparing a progress-only and a revision-inclusive schedule at the *same* data date. A structural
   constraint, not a UI nit. https://www.capterra.com/p/137005/SmartPM/reviews/
5. **Chris M., Senior Project Controls Manager, 5 Jun 2024** — terminology *"confusing such as
   'Backdated Activities' 'Should Start Should Finish'"*; and **Michelle L., Scheduling Manager,
   26 Jul 2022** — *"The ability to report on specific data across multiple projects is missing"*
   → Proprietary vocabulary that maps to no standard, plus reporting gaps.
   https://www.capterra.com/p/137005/SmartPM/reviews/

Also relevant: **Ziad A., Project Manager, 8 Aug 2022** — *"Integration in the beginning was tough
because my view of workflows and connections was different than the software's"*; **Ben R., Schedule
Engineer, 28 Jun 2024** — *"The program is still in development"*; **Yolanda A., Scheduling Manager,
8 Aug 2022** — *"wish it would take XML files that way I don't have to convert."*

`UNVERIFIED`: G2 and TrustRadius blocked automated retrieval (403). Reddit is not fetchable from this
environment. No customer complaints could be gathered for nPlan (SourceForge lists **zero reviews**:
https://sourceforge.net/software/product/nPlan/), ALICE, Nodes & Links or Deltek Acumen.

---

## 12. HARDEST FACTS (5 strongest numeric/documentary facts)

1. **AACE RP 29R-03 §1.2(f), Rev. 25 Apr 2011, 136 pp:** *"Schedules are a project management tool
   that, in and of themselves, do not demonstrate root causation or responsibility for delays. Legal
   entitlement to delay damages should be distinct and apart from the forensic schedule analysis
   methodologies contained in this RP."* — https://web.aacei.org/docs/default-source/toc/toc_29r-03.pdf
2. **SmartPM published pricing: Essentials $12,000/yr (up to 50 projects, unlimited users);
   Controls $25,000/yr (5 controls slots, incl. what-if + time impact analysis); 60-day free trial.**
   — https://smartpm.com/pricing
3. **Steelray Delay Analyzer: $3,990/user/yr or $390/user/mo**, implementing "the Daily Progress
   Method to run a half-step analysis, per AACE RP 29R-03" — and **"The tool does not attribute
   responsibility to parties."** — https://www.steelray.com/DelayAnalyzer/DelayAnalyzerP6.php
4. **nPlan: >750,000 historical programme files representing >$2Tn of construction spend (site) /
   $2.5Tn (press release); $500bn of projects under active management; $16M Series B on 17 Oct 2025
   led by CapHorn with Chevron Technology Ventures, Suffolk Technologies, GV, Pentech, LocalGlobe;
   customers "saved well over $1.2B".** — https://www.nplan.io/ and
   https://www.nplan.io/press-releases/nplan-raises-16m-series-b-to-scale-its-ai-led-transformation-of-capital-project-delivery
5. **SCL Delay and Disruption Protocol 2nd ed. (Feb 2017) recognises exactly six methods and, for both
   windows methods, ends the description with: "Thereafter, the analyst investigates the project
   records to determine what events might have caused the identified critical delay."** The 2nd ed.
   removed the 1st edition's preferred methodology. 38,500+ downloads from 142 countries (2005–Apr 2018).
   — https://www.scl.org.uk/sites/default/files/documents/SCL_Delay_Protocol_2nd_Edition_Final.pdf

Runners-up: **Deltek Acumen Fuse evaluates against "600+ industry-aligned metrics" spanning DCMA, DOE,
NASA, GAO and AACE** (https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse);
**Ron Winter Schedule Analyzer eForensic $2,750 perpetual single-user**
(http://scheduleanalyzer.com/eforensic_order.htm); **ALICE deployed on $297 billion of global
construction projects** (https://www.alicetechnologies.com/); **SmartPM Series A $5.5M, 29 May 2024,
led by Building Ventures with GS Futures and Nemetschek**
(https://www.businesswire.com/news/home/20240529228732/en/).

---

## 13. DIRECT ANSWERS TO THE FOUR KEY QUESTIONS

### Q1. Is automated delay attribution technically and evidentially credible today, or is it the part of the thesis most likely to be undeliverable?

**It is the part most likely to be undeliverable *as an autonomous verdict*, and the part most likely
to be valuable *as an assisted draft*. Split the dimension in two.**

*Evidentially:* No. The governing standard forecloses it. AACE §1.2(f) says schedules do not
demonstrate causation or responsibility; §1.3(c) scopes the discipline to quantification "as opposed
to assignment of delay responsibility"; §1.2(d) warns that "all methods are subject to manipulation as
they all involve judgment calls by the analyst"; and §1.1 explicitly sets out to "minimize the need to
contend with **'black-box' or 'voodoo' analyses**." A tool that outputs "this 14-day slip is an
Employer Risk Event, excusable and compensable" and cannot expose every judgement call behind it will
be destroyed on cross-examination — and the AACE RP hands opposing counsel the script.

*Technically:* Partially, and the tractable part is not the part the incumbents work on. The causation
step as the SCL defines it is: *given a quantified critical delay in window N, search the project
records for events that could have caused it.* That is document retrieval, temporal alignment and
evidence ranking — an LLM-shaped problem, not a CPM-shaped one. It is credible today to produce, for
each delay window: (a) the ranked candidate causal events with citations to the source record, (b) the
contract clause that would govern each event type, and (c) a flagged **draft** classification with an
explicit confidence and an explicit list of the judgement calls a human must make (concurrency,
pacing, float ownership, hindsight-vs-blindsight). That is genuinely useful and genuinely defensible,
because it is *evidence assembly with a human verdict* — the same division of labour the standards
already assume.

**Practical rule: never ship "the software decided it was the owner's fault." Ship "here are the
six records that sit in this delay window, here is the clause each engages, here is what an analyst
would still have to decide." Sell time-to-first-draft, not verdicts.** Note also SCL Core Principle 12
— an EOT does not automatically carry compensation, and "non-compensable Employer Risk Events" exist —
so any auto-generated dollar figure attached to auto-attributed delay is wrong for a whole class of
events. Dimension 15 inherits dimension 12's fragility.

### Q2. Does SmartPM already own "automated delay analysis" for the mid-market?

**They own the *category name* and the mid-market GTM. They do not own the *capability*, and the
capability is a commodity.**

Owned: the phrase "Automated, Forensic-Grade Half-Step Delay Analysis", the ENR-400 GC logo wall
(Suffolk, JE Dunn, Barton Malow, Holder, Layton, Alberici, Yates, PJ Dick, Ryan, Toll Brothers,
Manhattan, Ferrovial, AECOM…), the "Out of Court" narrative, Procore + Autodesk marketplace placement,
Nemetschek as a strategic investor, and a credible mid-market price ($12k–$25k/yr).

Not owned: the math. Deltek Acumen Fuse ships the same half-step forensic comparison; Steelray ships
it per AACE RP 29R-03 for $3,990/user/yr; Ron Winter ships it for $2,750 perpetual; Nodes & Links
ships Delay Navigator. And not owned: attribution, causation, entitlement, notice, quantum, or any
non-schedule document.

**Competitive implication: attacking SmartPM head-on is suicide; attaching to SmartPM is cheap.**
Their open API hands a startup the delay windows for free. Treat "which windows are delayed and by
how much" as a solved upstream input, not as product.

### Q3. Is schedule-impact analysis a *required* component of a V1, or can a V1 deliberately avoid it?

**A V1 can and should deliberately avoid it.** Three independent reasons:

1. **It is the most commoditised, most contested and most expensive thing to build.** A defensible CPM
   engine plus XER/MPP/PP/PMXML parsing plus half-step windows logic plus schedule-quality checks is
   many months of solo work to reach parity with a $2,750 perpetual licence.
2. **The standards let you skip it for the highest-value V1 use case.** Notice and entitlement
   obligations are triggered by *events*, not by proven critical-path impact. SCL Core Principle 3:
   "The parties and the CA should comply with the contractual procedural requirements relating to
   notices, particulars, substantiation and assessment in relation to delay events." Core Principle 6:
   "For an EOT to be granted, it is **not necessary** for the Employer Risk Event already to have begun
   to affect the Contractor's progress with the works." **You can detect the event, match the clause,
   compute the notice deadline and assemble the evidence with zero schedule mathematics.** Missing a
   notice deadline destroys entitlement regardless of how good your delay analysis later is — so the
   notice layer is both higher-value and lower-build than the schedule layer.
3. **The founder constraints demand it.** Schedule ingestion means proprietary binary formats,
   version-specific P6 quirks, corrupted XERs (Ron Winter publishes research on P6 corruption), and a
   support burden. That is a team's problem, not a solo founder's.

**Recommended V1 shape:** documents in (contract PDF + Procore/ACC RFI & daily-log export + a forwarded
email inbox) → commercial event detection → clause & notice-deadline matching → evidence bundle with
citations → draft notice. **Schedule = optional enrichment in V2, and when you do add it, consume
SmartPM's API or a P6 XER parser for the windows — do not rebuild the engine.** If a V1 must show
schedule impact, show *unquantified* impact: "this event sits in the window where SmartPM/your update
shows 14 days of critical-path delay," and stop.

### Q4. Does a solo founder need a proprietary schedule dataset to compete here?

**No — and this is the most encouraging finding in the report.**

nPlan's moat is real *for nPlan's problem*: >750,000 programme files, and their own materials say
forecasting accuracy (mean absolute error) improves as the dataset grows
(https://www.nplan.io/our-ai). If your product is "predict the probability this activity slips," you
need that corpus and you cannot get it — it took nPlan 8 years, enterprise sales into national
infrastructure programmes, and multiple funding rounds culminating in a $16M Series B.

**But that is a different problem.** The thesis's hard step — causation and entitlement — is
*per-project, per-document reasoning*, not cross-project statistics:

- **Causation** needs *this project's* RFIs, daily reports, minutes and correspondence. A corpus of
  750,000 other projects' schedules tells you nothing about why *this* wall was late.
- **Entitlement** needs *this contract's* clauses read against a body of standard forms (NEC4, JCT,
  FIDIC, AIA A201, ConsensusDocs, AS 4000/GC21) — all **publicly documented**, with published
  commentary, and a bounded, learnable rule space.
- **Method knowledge** is public: AACE RP 29R-03 is a published 136-page RP (free to AACE members);
  the SCL Protocol 2nd ed. is a **free public PDF**. The taxonomy, the six methods, the concurrency
  factors and the record categories are all open knowledge.
- **Schedule mathematics** is public: CPM is deterministic, XER is a documented delimited text format,
  and half-step windows arithmetic is fully specified in the RP.

**What a solo founder does need** is not a dataset but a **corpus of worked entitlement reasoning** —
clause-to-event mappings across the standard forms, notice-period tables, and a library of
delay-event archetypes. That is a knowledge-engineering effort measured in weeks, not a data-acquisition
effort measured in years. And it compounds: every customer project adds labelled clause→event→outcome
pairs that no schedule-forecasting corpus contains.

**Verdict: the data moat in this category is real but it guards the wrong door.**

---

## 14. UNKNOWNS — AND WHAT WOULD SETTLE THEM

| Unknown | What would settle it |
|---|---|
| **Identity of "Basis"** in construction schedule analytics. Domain probes and search all failed; `getbasis.ai` = accounting AI, `basis.com` = adtech, `buildbasis.com` = UK VC. | The exact URL from the orchestrator, or a Crunchbase/PitchBook company page. |
| **"Foresight"** — which company was meant. `foresightiq.co` is competitive-intelligence SaaS, unrelated. | Clarification from the orchestrator. |
| **Deltek Acumen list pricing.** No public price; Vendr's $20,380 median is all-Deltek, not Acumen. | A GSA Advantage / SEWP schedule line item, a reseller quote, or a public-sector RFP award. |
| **nPlan, ALICE, Nodes & Links pricing.** All quote-only. | Public-sector procurement records (HS2, Network Rail, TRU contract awards for nPlan; UK Contracts Finder / TED). |
| **Whether a post-2011 revision of AACE 29R-03 exists.** AACE's own sample PDF still serves Rev. 25 Apr 2011. | The AACE members' RP library index, or the AACE store listing. |
| **Nodes & Links funding, headcount, revenue.** Company page discloses none. | Companies House (UK) filings; Crunchbase (403 for me). |
| **SmartPM customer count / ARR / "% of Top ENR GCs".** A third-party summary asserted "over 50% of Top ENR GCs" but I could not find that claim on any SmartPM page I retrieved; their own press release says only "ENR 400 firms". | SmartPM's about/press kit, or an investor update. Treat "50% of Top ENR GCs" as `UNVERIFIED`. |
| **Whether SmartPM's delay windows can be produced at the same data date** (blocking true MIP 3.4 half-step). Two reviewers say same-data-date uploads are rejected. | A SmartPM product demo or a support-doc statement on data-date handling. |
| **Whether Nodes & Links' Delay Navigator can classify excusability.** Nothing on their site claims it. | A product demo or their Academy whitepapers (https://nodeslinks.com/academy/resources/whitepapers/). |
| **Customer sentiment for nPlan / ALICE / N&L / Acumen.** G2 and TrustRadius returned 403; SourceForge shows nPlan with zero reviews; Reddit unfetchable. | Direct G2/TrustRadius access, or practitioner interviews. |
| **Whether any court or tribunal has accepted a software-generated delay analysis without an expert.** Not addressed in any source I could reach. | The SCL's judicial-references summary (linked from the Protocol page), or a construction-law database search. |

---

## 15. THE ONE-PARAGRAPH SYNTHESIS

The schedule analytics / delay forensics layer has fully automated everything that can be computed
from a schedule file — quality scoring, version diffing, critical-path movement, half-step windows
delay quantification — and has commoditised it, with the same AACE-compliant arithmetic available at
$2,750 perpetual, $3,990/user/year and $25,000/year. It has automated **nothing** that requires reading
a document, and this is deliberate: AACE RP 29R-03 explicitly scopes forensic schedule analysis to
quantification "as opposed to assignment of delay responsibility," and states that schedules "in and
of themselves, do not demonstrate root causation or responsibility for delays." Every recognised
method in both AACE and the SCL Protocol terminates in the same manual step — *the analyst investigates
the project records to determine what events caused the delay* — and no product in this category
crosses it. SmartPM owns the mid-market brand for the automated half but sells a schedule-file-only
pipeline through an unusually open API, making it a natural **partner** rather than a competitor. The
practical instruction for a solo founder is: **do not build the CPM math, do not chase nPlan's data
moat, and do not promise automated fault-finding. Build the document layer that turns "14 days of
critical-path delay in window 7" into "here are the six contemporaneous records inside window 7, here
is the clause each engages, and here is the notice that is due in 4 days" — and leave the verdict to
a human.**
