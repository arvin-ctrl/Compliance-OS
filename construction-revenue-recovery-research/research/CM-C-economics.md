# CM-C — ECONOMICS & ROI
### Building the economic case for construction revenue recovery — or destroying it

Compiled 2026-08-19. Sources dated. Conventions used throughout:
- `SOURCED` = a published figure with a URL.
- `DERIVED` = my arithmetic on sourced inputs; method shown.
- `ASSUMPTION` = not sourced anywhere. **Basis is stated every time.** These are the attackable parts.
- `UNVERIFIED` = could not be confirmed from a primary source.

---

## 0. THE EVIDENCE RULE THIS REPORT OPERATES UNDER

The orchestrator's instruction was explicit: **do not model ROI on a change-order write-off percentage
unless it can be independently sourced.** I tried, hard, in this pass:

| Attempted source | Result |
|---|---|
| HKA CRUX 8th annual (Nov 2025) | Headline figures **confirmed independently** via HKA's own release + Middle East Construction News + Consulting.us: $95.0bn claimed, **33.4% of budgets**, 65.8% of schedules, 2,200+ projects, 114 countries, $2.433tn CapEx. Full PDF still gated. https://www.hka.com/news/crux-insight-eighth-annual-report-from-insight-to-foresight/ · https://meconstructionnews.com/65160/hka-unveils-eight-annual-crux-insight-report |
| Arcadis 16th annual (2026) | **Reachable and read** (US-only). Value distribution + causes obtained. |
| Dodge Construction Network SmartMarket Insight on change orders (2026) | Two "coming soon" landing pages, **no methodology disclosed** (no n, no dates, no respondent breakdown) on any of Dodge's, Clearstory's or Businesswire's pages. https://www.construction.com/resource/coming-soon-upcoming-smartmarket-insight-on-change-order-management-for-specialty-trade-contractors/ |
| Rabbet 2024 Construction Payments Report | **Full PDF obtained and text-extracted.** Contains **zero** write-off, bad-debt or abandoned-claim figures. Its $280bn is a *modelled cost of slow payment* = "14% of total construction costs", and the sample is **93% general contractors / 7% subcontractors**, online, Aug 2024. https://cdn.prod.website-files.com/679b71850706204b0b01c1bb/67d8173245dbbd8a4eae3216_2024%20Construction%20Payments%20Report.pdf |
| Levelset 2021/2022 Cash Flow & Payment Reports | Read. **No write-off value.** The one write-off number Levelset publishes — "companies in the U.S. write-off an average of 4% of their accounts receivable every year" — is (a) all-industry, not construction, (b) sourced to a vendor (Anytime Collect), (c) from a 2017 post. **Do not use.** https://www.levelset.com/blog/you-know-what-is-expensive-bad-debt/ |
| CFMA 2025 Benchmarker | Free workbook has no claims/disputes/write-off line. The full questionnaire is paywalled. |
| Billd 2025/2026 National Subcontractor Market Report, Siteline 2026 | Payment-timing and working-capital data only. No write-off value. |
| FMI, ENR, JBKnowledge | JBKnowledge exited (last edition 2017). Nothing current with a write-off figure. |

### CONCLUSION — say this plainly and stop looking

> **There is no credible published dollar or percentage figure for the VALUE of construction change-order
> or entitlement write-offs. It does not exist. The industry publishes incidence, not value.**

The **only two value-side numbers found anywhere in this program**, and both are vendor-commissioned:

1. **"98% of GCs have experienced fee erosion due to change order negotiations"; "nearly half say erosion
   exceeded 10% of their fee on at least some projects."** — Dodge Construction Network research
   commissioned by Clearstory, 2026. https://www.clearstory.build/construction-blog/2026-gc-change-order-report
   *This is the single most useful value-side datapoint in the whole program and it has not been used before.
   It is still soft — "at least some projects" is an unquantified quantifier and the methodology is
   undisclosed — but it is a statement about MAGNITUDE, not merely incidence.*
2. **"After introducing Clearstory, our T&M write-offs were reduced by about 66%"** from a stated baseline of
   **30% of T&M revenue previously lost** — Accurate Firestop customer testimonial.
   https://www.clearstory.build/customers/accurate-firestop *(single customer, promotional, n=1.)*

### The distinction the thesis has been abusing

| | Incidence | Value |
|---|---|---|
| "77% of specialty contractors have written off change order work as bad debt" | **This is incidence.** It says 77% of firms have done it *at least once, ever*. | It says **nothing** about how much. A firm that wrote off $4,000 in 2019 answers yes. |
| "97% of trades begin work before COR approval" | **This is incidence of exposure**, not of loss. Most of that work does eventually get paid. | Unmeasured. |
| "56% of subs missed a critical lien deadline in 2 years" | Incidence. | Unmeasured. |
| "Nearly half of GCs say fee erosion exceeded 10% of fee on at least some projects" | Incidence of a **magnitude threshold** — the only one published. | Closest thing to value that exists. |

**Every ROI in §3 below is therefore built from a *modelled* leak with an explicitly stated basis, cross-checked
against the two value-side datapoints above, and paired with a downside case where the leak is near zero.**

---

## 1. THE ECONOMIC MAP

### 1.1 Dispute value and distribution — Arcadis (US only since 2024)

`SOURCED` — Arcadis 16th Annual Construction Disputes Report, "Disruption to Innovation", US, Feb 2026
(2025 data). https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2026/2026_construction-disputes-report.pdf

| Metric | 2025 | 2024 | 2023 |
|---|---|---|---|
| Average US dispute value | **US$56.0m** | $60.1m | $43.0m |
| Average duration | **12.2 months** | 12.5 | 14.4 |
| Highest reported | $100m | $1.1bn | $2bn |
| Respondents seeing more disputes | 57.9% | — | — |

**The distribution is the market, not the average** (2025 / 2024):

| Band | 2025 | 2024 |
|---|---|---|
| **< $5M** | **39%** | 41% |
| **$5–25M** | **34%** | 31% |
| $25–50M | 9% | 8% |
| $50–100M | 4% | 7% |
| $100–150M | 1% | 4% |
| $150–500M | 11% | 4% |
| $500M+ | 1% | 5% |

Arcadis states it directly: *"the vast majority (80%) of claim values are $25M or less and almost half of all
claims are valued at less than $5M… the overall average is heavily influenced by only a few 'mega' claims."*

**Economic consequence:** ~73–80% of US disputes sit below $25m and ~39% below $5m. At a $400/hr blended
consultant pyramid with a >30-hour engagement floor, and with litigation funders screening for
**awards ≥10x the funding requested** (Omni Bridgeway published criteria,
https://omnibridgeway.com/litigation-funding/arbitration-financing), the bottom two-thirds of the
distribution is served by **neither** the consultant **nor** the funder. That is a genuinely double-vacated
band, and it is where software unit economics work.

**Caveat that must travel with these numbers:** Arcadis's sample is its own Contract Solutions caseload plus
a survey of its own network. It is not a census, and the 2026 methodology section is two sentences long.

### 1.2 Claim frequency and value as % of budget — HKA CRUX

`SOURCED` — CRUX Insight, 6th/7th/8th annual reports.

| Edition | Date | Projects | Countries | CapEx | Sums claimed | **Cost claimed as % of CapEx** | EOT as % of schedule |
|---|---|---|---|---|---|---|---|
| 6th | Oct 2023 | 1,801 | 106 | $2.247tn | $91.3bn | **33.6%** | 67.1% |
| 7th | Sep 2024 | 2,002 | 107 | $2.254tn | $84.4bn | **33.2%** | 66.5% |
| 8th | Nov 2025 | 2,200+ | 114 | **$2.433tn** | **$95.0bn** | **33.4%** | **65.8%** |

**Stable within 1.0 percentage point across three independent dataset refreshes.** This is a structural
constant, not a cyclical artefact. It is the strongest single economic fact available to this program.

**Americas cut (8th edition, via Construction Dive 18 Dec 2025):** 703 projects, 20 countries, average CapEx
$639m; **cost claimed 31.1% of budget, EOT 57.5% of schedule.**
https://www.constructiondive.com/news/time-money-fewer-construction-disputes-americas/808089/

**THE CRUX TRAP — and it is a big one for ROI.** CRUX's inclusion rule is that a project enters the dataset
**once HKA has spent >30 hours on a claim or dispute on it** (7th annual, Methodology p.63). CRUX therefore
answers *"on a project that has already gone badly enough to hire HKA, how much is claimed?"* — **not**
*"how much does a typical contractor leave on the table?"*

> **Do not apply 33.4% to a healthy portfolio.** Doing so overstates any ROI by one to two orders of
> magnitude. 33.4% is a *conditional* number: conditional on the project already being distressed. The
> correct use of CRUX in an ROI model is as the **value of a single distressed project**, multiplied by an
> assumed distress rate — and the distress rate is not published by anyone.

### 1.3 Consultant fees and hours — the substitute's cost structure

`SOURCED` rates:

| Source | Metric | Value | Date |
|---|---|---|---|
| Exponent 10-K | Published professional rate band | **$225–$1,375/hr** | FY2025 |
| Exponent 10-K | `DERIVED` blended realised | ~$396/hr ($582.0m ÷ 1,468,000 hrs) | FY2025 |
| FTI 10-K | Forensic & Litigation Consulting average billable rate | **$442/hr** (2024: $390) — **+13.3% YoY** | FY2025 |
| FTI 10-K | FLC utilisation | 57% | FY2025 |
| Diales AR | Utilisation / underlying operating margin | 71.6% / **3.3%** (£1.4m on £43.0m) | FY2025 |
| Walter Lilly v Mackay ¶71 | Real, court-recorded claims-consultancy spend by one party on one project | **£750,000** (2007–08 money) | 2012 |

`DERIVED` engagement model (agent 11's model, priced at $400/hr blended — **a model, not a citation**):

| Dispute size | Total hrs | Cost @ $400/hr | **of which document review + chronology** |
|---|---|---|---|
| < $2m | 170–390 | $70k–$155k | 60–150 hrs |
| **$5–25m (the modal dispute)** | **600–1,650** | **$240k–$660k** | **200–600 hrs** |
| $25–100m | 1,650–5,100 | $660k–$2.0m | 600–2,000 hrs |
| >$100m | 5,000–20,000+ | $2m–$8m+ | — |

Cross-check: $660k–$2.0m against Arcadis's $56.0m average dispute = **1.2%–3.6% of the disputed sum**.
That ratio is the most useful single number in the section — see §6.

**And the corroborating admission from the incumbent itself:** Arcadis's own 16th annual states AI-assisted
eDiscovery and LLM review "compress weeks of document analysis into days, **cutting costs by as much as 85%**."
The incumbent is telling its clients the automatable block is 85% removable.

### 1.4 Contractor margins by type — the ROI denominator

`SOURCED` — CFMA 2025 Construction Financial Benchmarker, FY2024 data, n=1,558 (1,639 submitted).
https://cfma.org/files/o-files/download-file/5aff6a42-7a29-491c-bb4a-fde57e74487b

| Segment | Net income before taxes FY2024 |
|---|---|
| All companies | 6.7% |
| **Industrial & Nonresidential (commercial GC/CM)** | **4.4%** |
| **Heavy Construction (highway/civil)** | **8.3%** |
| **Specialty Trade (subcontractors)** | **7.7%** |
| Best in Class (top quartile, all) | 12.0% |
| Heavy Construction — Best in Class | 15.1% |

By revenue band:
- **Industrial & Nonresidential:** <$10M 3.3% · $10–24.9M 5.9% · $25–49.9M 4.7% · $50–99.9M 3.9% ·
  **$100–299.9M 4.2%** · $300M+ 3.4%
- **Heavy Construction:** <$10M 5.8% · $10–24.9M 8.1% · $25–49.9M 8.6% · **$50–99.9M 9.8%** ·
  **$100–199.9M 8.7%** · >$200M 7.1%

### 1.5 Overhead structure — where a purchase would actually come from

`SOURCED` — same workbook, FY2024, all companies, % of total revenue:

| Line | % of revenue | On $139.4M average revenue |
|---|---|---|
| Gross Profit | 17.77% | $24.8M |
| **Total SG&A** | **11.33%** | **$15.8M** |
| — Base Payroll / Payroll Related | 5.41% | $7.5M |
| — Other Expenses | 4.30% | $6.0M |
| — Administrative Bonuses | 0.59% | $823K |
| — **Professional Fees** | **0.50%** | **$697K** |
| — Sales & Marketing | 0.28% | $390K |
| — **Technology Costs** | **0.26%** | **$368K** |
| Net Income before Income Taxes | 6.70% | $7.27M |

Segment SG&A: Industrial & Nonresidential **7.3%**; Specialty Trade **14.8%**; Specialty Trade $100–300M 11.9%.
Technology Costs by cohort: all companies **0.26%**; **Specialty Trade 0.40%**; Electrical contractors 0.40%.

> ### THE MOST IMPORTANT UNDER-USED FACT IN THE CFMA DATA
> **"Professional Fees" (0.50% of revenue) is nearly TWICE the size of "Technology Costs" (0.26%).**
> On the average respondent that is **$697K vs $368K**. Professional Fees is where construction attorneys,
> claims consultants, expert witnesses and outside accountants are already paid.
> **A product sold as software competes for the smaller purse. The same product sold as a substitute for
> consultant and counsel hours competes for a purse roughly 1.9x larger — and one that is already
> uncomfortable, episodic and unloved.** This reframes the entire budget question in §4.

Context: revenue per FTE $514,587; Days in A/R 55.2; months in backlog 9.1; Underbillings to Equity 8.1%.
Corroboration `FLAG: 2017` — JBKnowledge ConTech Report: 46.4% of finance respondents spent <1% of sales on
IT; among firms under $100M sales, **only one respondent** allocated over 2%; **58.8% of contractors recover
none of their IT spend from project owners.**
https://civil808.com/sites/default/files/2017-jbknowledge-contech-report.pdf

---

## 2. WHICH MISSED-REVENUE PROBLEM HAPPENS MOST FREQUENTLY

Ranked by **frequency of occurrence**, with the value column filled only where a source exists.
`CONF` = my confidence in the row as a whole (frequency evidence + value evidence + relevance).

| # | Problem | Frequency evidence | Typical value evidence | CONF |
|---|---|---|---|---|
| **1** | **Unapproved / unbilled change-order work** | **97%** of specialty trades begin work before COR approval; **42%** do so more than half the time. **77%** have written off CO work as bad debt. **91%** of GCs sometimes short-pay; **>50%** don't pay in full on **20%+** of the COs they manage. **98%** of GCs have experienced fee erosion from CO negotiation. (Dodge/Clearstory 2026) | **Nearly half of GCs: erosion exceeded 10% of their fee on at least some projects** (Dodge/Clearstory 2026 — the only published magnitude figure). Single-customer anchor: **30% of T&M revenue** lost pre-Clearstory, reduced 66% after (Accurate Firestop). Change orders 5–10% of contract value on typical commercial work (`weak secondary`, trade-guide consensus). | **HIGH** on frequency, **LOW–MED** on value |
| **2** | **Disputed pricing on a submitted change order** | **66%** of GCs cite **disputed pricing** as the primary reason for withholding/reducing payment — *above* the **53%** citing insufficient backup. **More than half of all CORs require 2+ revision cycles.** 64% of GCs name pricing disputes as the leading disagreement cause. (Dodge/Clearstory 2026) | Not published anywhere. | **HIGH** frequency, **NONE** on value |
| **3** | **Scope creep absorbed (constructive change never converted to a COR)** | **Change in scope is the #1 cause of claims globally**, affecting **38.8%** cumulative / **~28%** of post-2020 projects (CRUX 8th); Americas 25.7%. **Two-thirds of GCs say poor management of *unsolicited* changes and T&M is the single biggest driver of their change-order risk** (Dodge/Clearstory 2026). | Not published. CRUX's 33.4%-of-budget applies **only to already-distressed projects** — see §1.2 trap. | **MED** frequency, **NONE** on value |
| **4** | **Retainage held / slow payment** | **43%** of subs wait 90+ days for retainage vs 15% of GCs; nearly **1 in 5** wait 6+ months; **92%** floated payroll in the past year; **59%** wait 46+ days to be paid; industry DSO ~83 days. (Siteline 2026, n=492, surveyed May 2026) https://www.siteline.com/blog/92-percent-of-subcontractors-floated-payroll-last-year-new-siteline-report-finds | Modelled at **$280bn/yr = 14% of total US construction cost** (Rabbet 2024) — but this is a **cost-of-capital**, not lost revenue. | **HIGH** frequency — but **WRONG PROBLEM**: timing, not entitlement; and already served by Billd/Constrafor/Siteline |
| **5** | **Missed statutory lien deadline** | **56%** of subcontractors missed a critical lien deadline in the past two years (Siteline 2026, n=492) — *fifteen years after Levelset, and five years after its $484.1M exit.* | Binary: the whole receivable becomes unsecured. | **HIGH** frequency — but **SOLVED AND OWNED**. Levelset proved the alert was free and the *filing* was the revenue ($59/notice, $349/lien). Contractual notice has no filing to sell. |
| **6** | **Missed contractual notice** | **NOT MEASURED ANYWHERE.** Best proxies: CRUX "contract management and/or administration failure" **19.5% → 18.0% → <9% post-2020** of projects (and the category is not decomposed); Document Crunch's own Jan 2026 research names it verbatim — *"notice windows had already closed, converting otherwise valid claims into absorbed costs"* — **with no number attached.** | Binary when it bites: the whole claim. *Van Oord v Allseas* [2015] EWHC 3074 (TCC): ~£10m claim lost entirely, repay **£1,895,349.89 + £588,882.98**, on out-of-time notice + Daily Progress Reports that "make so few references to standing time or disruption". https://caselaw.nationalarchives.gov.uk/ewhc/tcc/2015/3074 | **LOW** on frequency, **HIGH** on consequence — and **geographically concentrated**: AIA A201 §15.1.3 names 21 days with **no waiver clause**; US courts split; federal boards excuse late notice by default (*Hoel-Steffen*, 456 F.2d 760, 768). **Only state DOT provides a hard fuse** (Caltrans §5-1.43A: noncompliance is *"a waiver of the potential claim… and is a bar to arbitration"*). |
| **7** | **Delay / EOT not claimed** | On projects that reach a claim, EOT **is** claimed, heavily: **65.8% of planned schedule** globally, 57.5% Americas (CRUX 8th). That is evidence of *over*-claiming where it matters, not under-claiming. Frequency of *failing to claim* on ordinary projects: unmeasured. | High per event — but **SCL Protocol Core Principle 12: an EOT does not carry compensation.** Any `delay days × daily rate` figure is wrong by construction for non-compensable Employer Risk Events. | **LOW** |
| **8** | **Disruption / lost-productivity not claimed** | Unmeasured. Practitioner consensus is that it is the least-claimed and hardest-proved head. Long International, on 20+ years of process-industrial projects: *"there has not been a single instance where job conditions or project records would allow the proper 'textbook' use of the Measured Mile Method."* https://www.long-intl.com/articles/contemporaneous-project-records/ | Largest single quantum head when it succeeds; near-zero when records fail. | **LOW** frequency data — but **HIGHEST** confidence that the binding constraint is *evidence*, which is the thesis's own claim |
| **9** | **Backcharges** | **No published dataset found anywhere in this program.** | None. | **NONE — do not build on it** |
| **10** | **Escalation** | Not broken out by Arcadis or CRUX. Acute 2021–23, receding since. | None. | **NONE** |

### The ranking's verdict, stated as an economics finding

**Rank 1 (unapproved/unbilled change orders) is the only problem in the list with same-source-quality
frequency evidence AND a published magnitude threshold AND a buyer who is unambiguously the loser.**
Ranks 4 and 5 are more measurable but are owned. Ranks 6–10 are where the *value per event* is largest and
where **nobody has measured anything at all.**

**The economically correct reading of the whole table:** the money is in ranks 6–8 and the *evidence* is in
ranks 1–3. A product that attaches to rank 1 (frequent, billing-cadence, measurable, single-sided buyer) and
uses that foothold to reach ranks 6–8 (rare, high-value, unowned) is the only sequencing the data supports.
A product that starts at rank 6 has no cadence, no measured demand and, in the US outside state DOT, a weak
fear pitch.

---

## 3. ROI EXAMPLES

Common structure. **Recovered change-order revenue is near-pure margin** — the work is already performed and
the cost already incurred — so a recovered dollar drops almost entirely to NIBT. The correct framing is
Levelset's own: at a 3.4% net margin, *"it would take $29 million worth of new revenue to generate enough
cash to make up for that single, million dollar loss."*
https://www.levelset.com/blog/you-know-what-is-expensive-bad-debt/

---

### (a) SPECIALTY / TRADE SUBCONTRACTOR — ~$50M revenue

**Firm economics (all `SOURCED`, CFMA FY2024 n=1,558):**

| Input | Value | Source |
|---|---|---|
| Revenue | $50.0M | given |
| Net income before taxes @ Specialty Trade 7.7% | **$3.85M** | CFMA |
| Total SG&A @ Specialty Trade 14.8% | $7.4M | CFMA |
| **Technology Costs @ Specialty Trade 0.40%** | **$200K/yr** ($16.7K/mo) | CFMA |
| Professional Fees @ 0.50% (all-co proxy) | ~$250K/yr | CFMA |

**The leak — modelled, every step labelled:**

| Step | Value | Basis |
|---|---|---|
| Change-order work as % of contract value | **7.5%** → **$3.75M/yr** | `ASSUMPTION`. Basis: trade-guide consensus of 5–10% on typical commercial work; midpoint taken. **Weak secondary source. This is the softest input in the model.** |
| Share of CO dollars exposed to short-payment | **20%** → **$750K** | `SOURCED, but converted`: ">50% of GCs don't pay the full requested amount on **20%+** of the change orders they manage" (Dodge/Clearstory 2026). **Conversion caveat: that is 20% of change orders BY COUNT, applied here to dollars.** |
| Average shortfall when short-paid | **25%** → **$187.5K/yr** | `ASSUMPTION`. Basis: none published. 25% chosen as a mid-estimate consistent with "2+ revision cycles on >half of CORs". |
| **Modelled annual leak** | **~$188K** (band $150K–$400K) | = **0.38% of revenue** |
| Cross-check A | Accurate Firestop: 30% of T&M revenue lost pre-Clearstory. If T&M is ~30% of CO revenue ($1.13M), 30% = **$338K** | Same order of magnitude — my model sits at the conservative end. |
| Cross-check B | 77% incidence of write-off (Dodge/Clearstory) is consistent with a leak of this size being routine but not catastrophic | Consistent |

**Capture and value:**

| Step | Value | Basis |
|---|---|---|
| Realistic capture rate | **15–25%** | `ASSUMPTION`. Basis, stated honestly: (i) Clearstory's *workflow* fix already claims 66% reduction of the documentation half of the leak, so the entitlement layer is fighting over the residual; (ii) **66% of short-payment is disputed pricing, not missing backup** — better evidence moves that number but rarely closes it; (iii) the counterparty is adversarial and the sub will not push hard on a repeat GC. |
| Annual recovered | **$28K–$47K** (central ~$38K) | `DERIVED` |
| Effect on NIBT | +$38K on $3.85M = **+1.0% of company profit** | `DERIVED` |
| Equivalent new revenue at 7.7% net | **~$490K of new work** | `DERIVED` — this is the sales line |
| **Price they'd pay** | **$500–$1,000/mo = $6K–$12K/yr** | 3–6% of the $200K tech purse; below any procurement threshold; matches the NEC-proven band (Gather £500/mo ≈ $630; CEMAR £435/licence/mo ≈ $550) |
| **Payback** | **2–5 months** | `DERIVED` |
| ROI | **3–6x** | `DERIVED` |

**HONEST DOWNSIDE CASE.** Four ways this delivers nothing:
1. The sub is short-paid because **its prices are genuinely above market**, not because its entitlement is
   unproven. 66% of short-pay is a pricing disagreement. No evidence engine fixes an uncompetitive rate.
2. **The eSUB natural experiment.** eSUB sold this exact narrative ("It's not about the work you did; it's
   about the work you documented") to exactly this buyer for years and is the smallest, slowest-growing
   company in its category (~16k users, ~60 staff). Documentation hygiene does not sell to subs.
3. **Adoption.** 96% of Clearstory's own respondents cite ease-of-use as the top adoption factor. A field PM
   who will not open the app produces zero capture, and the $6–12K is a pure cost against a 7.7% margin.
4. **Relationship suppression.** Contractors deliberately suppress notice to protect owner/GC relationships —
   documented in print by construction lawyers (Smith Currie, Jun 2025). **27% of subs have already stopped
   working with a GC over change orders**; the other 73% are managing the relationship, not maximising
   recovery.
**In the downside case, capture ≈ 0 and the product is a $6–12K/yr expense on a firm earning $3.85M.**

---

### (b) MID-MARKET GENERAL CONTRACTOR — ~$200M revenue

**Firm economics (`SOURCED`, CFMA FY2024):**

| Input | Value |
|---|---|
| Revenue | $200M |
| NIBT @ Industrial & Nonresidential $100–299.9M band = **4.2%** | **$8.4M** |
| Total SG&A @ Industrial & Nonresidential 7.3% | $14.6M |
| **Technology Costs @ 0.26%** | **$520K/yr** ($43K/mo) |
| Professional Fees @ 0.50% | **$1.0M/yr** |
| Revenue per FTE (I&N) $1.24M → est. headcount | ~160 |

**The leak — and here the model is unusually well supported, because the GC-side Dodge research supplies a
magnitude:**

| Step | Value | Basis |
|---|---|---|
| GC fee on volume | **4%** → **$8.0M of fee** | `ASSUMPTION`. Basis: typical CM/GC fee range 3–5% on negotiated work; midpoint. |
| GCs experiencing fee erosion from CO negotiation | **98%** | `SOURCED` Dodge/Clearstory 2026 |
| GCs where erosion **exceeded 10% of fee** on at least some projects | **~50%** | `SOURCED` Dodge/Clearstory 2026 — **the only published magnitude figure in the category** |
| Share of projects affected in a year | **25%** | `ASSUMPTION`. Basis: "at least some projects" is unquantified; 25% chosen as a deliberately conservative reading of "some". |
| **Modelled annual fee erosion** | $8.0M × 10% × 25% = **$200K/yr** | `DERIVED` = **0.10% of revenue, 2.4% of NIBT** |
| Second leak (unrecovered cost from owner) | **Not modelled.** | Deliberately excluded — CRUX's 33.4% applies only to distressed projects and the distress rate is unpublished. **Including it would be the exact error the brief forbids.** |

**Capture and value:**

| Step | Value | Basis |
|---|---|---|
| Capture rate | **20–30%** | `ASSUMPTION`. Basis: the GC's erosion is driven by *unsolicited changes and T&M* — two-thirds of GCs name this as the single biggest risk driver — which is precisely the detectable, evidence-linkable class. Higher than the sub's rate because the GC controls the record. |
| Annual recovered | **$40K–$60K** | `DERIVED` |
| Effect on NIBT | +$50K on $8.4M = **+0.6% of company profit** | `DERIVED` |
| Equivalent new revenue at 4.2% net | **~$1.19M of new work** | `DERIVED` |
| **Price they'd pay** | **$2,000–$3,000/mo = $24K–$36K/yr** | **4.6–6.9% of the $520K tech purse** — board-visible, requires a CFO business case and must displace something |
| **Payback** | **7–11 months** | `DERIVED` |
| ROI | **1.4–2.5x** | `DERIVED` — **the weakest of the three** |

**HONEST DOWNSIDE CASE — and it is the strongest downside of the three.**
1. **The GC is structurally conflicted.** It is simultaneously the *claimant* against the owner and the
   *payer* short-paying its subs (91% of GCs sometimes short-pay). A product that surfaces entitlement
   surfaces the subs' entitlement against the GC too. Expect the GC to buy it **defensively**, which is
   exactly what Gather's UK evidence actually shows: its Network Rail "£300,000+" headline is **money
   withheld from the contractor**, not recovered by one, and across **eleven case studies not one documents a
   recovered compensation event in GBP.**
2. **4.2% net is the thinnest margin in the industry** and $36K/yr is a real line item on a $520K purse.
3. If the fee erosion is genuinely a *negotiation* outcome rather than an *evidence* outcome, capture is
   near zero — and the Dodge data says pricing disputes (64%) outrank documentation.
4. **Procore's Change Analysis agent went GA on 23 Jul 2026** and identifies "scope impacts, cost exposure,
   schedule risk and required follow-up actions" from project records, inside a credit bundle. For a GC
   already paying Procore, marginal willingness to pay for detection is falling.

**Verdict on (b): the commercial GC has the best *headline* arithmetic (a recovered dollar is a bigger % of a
4.2% margin) and the worst *actual* case. Do not lead with commercial GCs.**

---

### (c) HEAVY CIVIL / STATE DOT CONTRACTOR — ~$100M revenue, Caltrans-style contract

**Firm economics (`SOURCED`, CFMA FY2024):**

| Input | Value |
|---|---|
| Revenue | $100M |
| NIBT @ Heavy Construction $100–199.9M band = **8.7%** | **$8.7M** |
| Technology Costs @ 0.26% | **$260K/yr** ($21.7K/mo) |
| Professional Fees @ 0.50% | ~$500K/yr |
| Heavy Construction Best-in-Class margin | 15.1% |

**The contractual regime — this is what makes the case, and it is `SOURCED`:**

- Caltrans Standard Specifications **§5-1.43A** sets a **three-part potential claim record procedure**, and
  the Construction Manual states noncompliance results in **"a waiver of the potential claim, a waiver of the
  right to a corresponding claim for the disputed work in the administrative claims process, and is a bar to
  arbitration."** https://dot.ca.gov/programs/construction/construction-manual/section-5-4-disputes
- Initial Potential Claim Record within **5 business days**; supplemental record with an **itemised cost
  estimate + Time Impact Analysis within 15 days** (i.e. costed by ~day 20), per §§5-1.42–5-1.43D and the
  Full and Final Potential Claim Record forms (Exhibit 16-UF; Form CEM-6201E).
- Waiver is statutorily reinforced: **Pub. Cont. Code §10240.2**.
- **A hard fuse AND a mandated costed artefact on a 20-day clock. This is the only US regime that supplies
  both.**

**CRITICAL COMPETITIVE FACT NOT PREVIOUSLY IN THE PROGRAM:**
> **Caltrans already operates an Electronic Potential Claim Record (ePCR) system** — Adobe Forms on a
> database, used by **both contractors and Caltrans staff**, that generates **workflow and email
> notifications and reminders**. https://dot.ca.gov/programs/construction/epcr
> **The owner supplies the deadline-reminder layer for free.** This is the *fourth independent confirmation*
> that deadline alerting cannot be the wedge (after Aconex, Levelset and Trunk Tools' free extraction).
> **The wedge in this segment is the costed estimate + TIA, not the reminder.** That is precisely the
> `recoverable_dollar_estimation` gap where nobody in the world scores above 1.

**The leak — modelled:**

| Step | Value | Basis |
|---|---|---|
| Active contracts at $100M revenue | ~8–15 | `ASSUMPTION`. Basis: heavy civil average contract size; not sourced. |
| Potential-claim events per year that are **either** unfiled within 5 days **or** filed and never supplemented with a costed estimate + TIA by day 20 | **2–4** | `ASSUMPTION`. Basis: none published. **This is the single number I would most want verified by interview** — see §7. |
| Value per waived event | **$150K–$500K** | `ASSUMPTION` bracketed by `SOURCED` data: Arcadis 2025 shows **39% of US disputes are <$5m**; an individual DOT potential claim sits well below dispute threshold. Also consistent with the $412k figure used elsewhere in this program. |
| **Modelled annual waived entitlement** | **$300K–$1.5M** (central ~$600K) | `DERIVED` = 0.3–1.5% of revenue |
| Capture rate | **20–40%** | `ASSUMPTION`, and **the highest of the three** because the failure mode is *binary* (waiver, not negotiation) and the required artefact is **specified in writing by the counterparty**. There is no ambiguity about what "complete" means. |
| **Annual recovered** | **$120K–$240K** (central ~$180K) | `DERIVED` |
| Effect on NIBT | +$180K on $8.7M = **+2.1% of company profit** | `DERIVED` |
| **Price they'd pay** | **$3,000–$5,000/mo = $36K–$60K/yr**, or per-project $8K–$15K | 14–23% of the $260K tech purse **if bought as software** — see the budget answer below, which changes this entirely |
| **Payback** | **2–6 months** | `DERIVED` |
| ROI | **3–5x** | `DERIVED` |

> ### THE BUDGET FINDING THAT MAKES THIS CASE — and it is new to the program
> On federally-funded work, **claim-preparation costs are unallowable, but REA-preparation costs are not.**
> - **FAR 31.205-47(f)(1)**: costs incurred in connection with "the prosecution of claims or appeals against
>   the Federal Government" are **unallowable**. https://www.acquisition.gov/far/31.205-47
> - **BUT — *Tip Top Construction, Inc. v. Donahoe*, 695 F.3d 1276 (Fed. Cir. 2012)**: costs incurred "for
>   the genuine purpose of materially furthering the negotiation process" — including preparing and
>   negotiating a **Request for Equitable Adjustment** — are **allowable contract administration costs**
>   under **FAR 31.205-33**, *even if negotiation later fails and a CDA claim is submitted*. Unallowability
>   attaches only once the matter converts into a CDA claim under the disputes clause.
>   https://www.cafc.uscourts.gov/9-19-2012-2011-1509-tip-top-construction-inc-v-donahoe-11-1509/
>
> **Consequence: a product used in the pre-claim window — the exact window this thesis targets — is a
> job-costable, allowable contract-administration cost on federal and federally-aided work, not G&A.**
> It escapes the 0.26% technology cage entirely and answers the "58.8% of contractors recover nothing from
> owners" problem in one move. **This is the single strongest commercial argument in the entire report.**
> `CAVEAT`: Caltrans state-funded contracts are governed by Caltrans specifications and Public Contract Code,
> not the FAR. Allowability must be confirmed contract by contract. `UNVERIFIED` for Caltrans specifically.

**HONEST DOWNSIDE CASE.**
1. **Heavy civil contractors already have a claims culture.** Many run a dedicated schedule engineer and a
   cost engineer. If they already file PCRs religiously and already produce TIAs, the product saves *hours*,
   not *dollars* — and collapses to a $500–$1,500/mo efficiency tool with a 10–20 hr/month time saving.
2. **Caltrans's own ePCR already nags them.** The reminder half of the value is gone before you arrive.
3. **The event-count assumption (2–4/yr) is completely unsourced.** If it is 0–1, the model breaks.
4. **This is the most copyable beachhead.** The restated structural rule from CM-A is: *two-sided platforms
   ship adversarial machinery when an EXTERNAL AUTHORITY makes the judgement.* Caltrans **is** an external
   authority with a bright-line rule, a form and a statutory consequence — i.e. precisely the condition under
   which Procore, Trimble and Autodesk historically **do** ship (Levelset, Payapps). The fuse that makes the
   wedge also makes it the safest thing an incumbent could copy.
5. Heavy civil is where incumbents (Oracle P6, InEight, HCSS) are *strongest*, cutting against the program's
   recurring "fragmentation is weakest where incumbents are strongest" signal.

---

### (d) OPTIONAL — CLAIMS CONSULTANCY buying it to cut document-review hours

| Input | Value | Source |
|---|---|---|
| Document review + chronology per $5–25m matter | **200–600 hrs** | `DERIVED` model (agent 11) |
| Blended realised rate | **$396–$442/hr** | Exponent `DERIVED`; FTI FLC `SOURCED` |
| Value of that block | **$80K–$240K per matter** | `DERIVED` |
| Total matter fee | $240K–$660K | `DERIVED` |
| Incumbent's own stated AI saving | eDiscovery/LLM review cuts document-analysis cost **"by as much as 85%"** | Arcadis 16th annual, `SOURCED` |
| Realistic tool saving | **40–60% of the block = 80–360 hrs = $32K–$160K/matter** | `ASSUMPTION`, discounted heavily from Arcadis's 85% because chronology ≠ eDiscovery culling |
| **Price** | **$5K–$25K per matter**, or $2,000–$5,000/mo per analyst pod | Anchored at ~15% of the saved cost |
| Payback | **Within the first matter** | `DERIVED` |

**HONEST DOWNSIDE CASE — and it is structural, not fixable.**
- **A time-and-materials business cannot fund the destruction of its own hours.** CRA: *"In most instances,
  we charge clients on a time-and-materials basis."* FTI FLC runs **57% utilisation**; Diales runs 71.6%
  utilisation for a **3.3% underlying operating margin**. Cutting 300 billable hours out of a matter removes
  ~$120K of revenue and saves them nothing they can bank.
- The tool only sells into **fixed-fee and capped-T&M** engagements (FTI 10-K confirms these exist) and into
  **competitive bids for the sub-$5m matters they currently decline**. That is a narrow slice.
- **In ~9 years of aggressive M&A, none of the twelve major firms has bought or built a claims-detection
  product.** That is a revealed preference, not an oversight.
- The customer becomes a competitor the moment it understands the product.
**Verdict: real near-term revenue, genuine channel, terrible long-term strategic position. Use it to fund the
first 12 months and to acquire matter data — not as the business.**

---

### ROI summary

| | Leak modelled | Capture | $ recovered/yr | Price/yr | Payback | ROI | Confidence in the leak |
|---|---|---|---|---|---|---|---|
| **(a) $50M specialty sub** | ~$188K (0.38% of rev) | 15–25% | **$28–47K** | $6–12K | **2–5 mo** | 3–6x | **LOW** — CO% of contract is a trade-guide number |
| **(b) $200M commercial GC** | ~$200K (0.10% of rev) | 20–30% | **$40–60K** | $24–36K | **7–11 mo** | 1.4–2.5x | **MED** — the only published magnitude figure supports it |
| **(c) $100M heavy civil / DOT** | ~$600K (0.6% of rev) | 20–40% | **$120–240K** | $36–60K | **2–6 mo** | 3–5x | **LOW on event count, HIGH on consequence** |
| **(d) Claims consultancy** | $80–240K/matter of automatable hours | 40–60% | $32–160K/matter | $5–25K/matter | **1 matter** | 3–6x | **HIGH** on hours, **LOW** on willingness |

---

## 4. THE BUDGET QUESTION

### Is $500–$5,000/month realistic? — **YES at the bottom, NO at the top, and only if it leaves the IT line.**

| Price | $50M sub (purse $200K) | $100M heavy civil (purse $260K) | $200M GC (purse $520K) | Verdict |
|---|---|---|---|---|
| **$500/mo ($6K/yr)** | 3.0% | 2.3% | 1.2% | **YES everywhere.** Credit-card / departmental. Below any procurement threshold. **This is the right V1 price.** |
| **$1,500/mo ($18K/yr)** | 9.0% | 6.9% | 3.5% | **YES at $100M+.** Needs one manager's sign-off. |
| **$3,000/mo ($36K/yr)** | 18% | 13.8% | 6.9% | **NO at $50M. YES at $100M+ with a CFO business case and a displacement.** |
| **$5,000/mo ($60K/yr)** | **30% — impossible** | 23% | 11.5% | **NO below ~$150M revenue.** At $200M+ it is affordable but triggers enterprise procurement, security review and an MSA — all of which the solo-founder constraint penalises. |

Corroboration that the band is real at the top end, from a different continent and contract form:
**CEMAR £435/licence/month** (administering £75bn of works) ≈ **US$550/mo**; **Gather £500/month flat**;
**Contradic €199–349/user/month**. The $500–$5,000 band is proven — but the *proven* part is $500–$700.

### From which budget line? — **NOT IT. Three better answers, in priority order.**

**1. PROJECT / JOB COST (best answer).** Price **per project**, not per seat, so it can be job-costed rather
than absorbed into G&A. Three reasons this is materially better than the technology line:
   - It maps to how contractors already think and budget.
   - **58.8% of contractors currently recover no IT spend from owners** (JBKnowledge, `FLAG: 2017`) — a
     job-costable product is genuinely differentiated commercial design.
   - **On federal and federally-aided work it may be an *allowable* cost.** *Tip Top Construction v. Donahoe*,
     695 F.3d 1276 (Fed. Cir. 2012): REA-preparation costs incurred to further negotiation are allowable
     contract administration costs under FAR 31.205-33; only post-CDA-claim costs fall under the
     FAR 31.205-47(f)(1) bar. **A pre-claim product sits on the allowable side of that line.**

**2. PROFESSIONAL FEES (the larger purse, and the real displacement target).**
   **CFMA FY2024: Professional Fees = 0.50% of revenue vs Technology Costs = 0.26%.** On the average
   respondent that is **$697K vs $368K — 1.9x larger.** This is where construction attorneys, claims
   consultants and expert witnesses are already paid. **Sell the product as a substitute for consultant and
   counsel hours, not as software, and it competes for a purse nearly twice the size — one the CFO already
   dislikes because it is episodic, opaque, and arrives after the loss.**

**3. RECOVERY-FUNDED.** Legally constrained — see §5. Viable as a *component*, not as the whole price.

**Never the IT line.** At 0.26% of revenue the technology purse is already committed to the ERP, Procore
(mid-size GCs pay $20–40K/yr for it), Bluebeam and M365. A new entrant competing there is competing with the
system of record, and losing.

### Who signs?
- **$500–$1,500/mo:** a **project executive, VP Operations, or contracts manager**. Not IT, not the CFO.
- **$3,000+/mo:** the **CFO**, with a written business case.
- **Never the PM or superintendent.** Four separate 2025–26 r/ConstructionManagers threads probing exactly
  this product drew hostility that outscored the post — *"This is like GC 101 and no one needs more software
  for anything. CONTRACTING is in the name."* **But not one project executive or CFO appeared in any thread.
  The mockers are not the budget holder.**

### What does it displace?
- **Headcount, not software.** Tutor Perini **Change Order Engineer $85–120K**; AECOM **Claims Manager
  $140–182K**; 1,000+ open US Contract Administrator roles. **One such role costs 7–20x the annual
  subscription.** The pitch is "this makes the one person you already have cover three times the portfolio",
  not "replace a tool".
- **Consultant hours** (Professional Fees line) — the second displacement.
- **Nothing in the tech stack.** Procore, Clearstory and Siteline are all keeping their line; there is no
  incumbent SKU to cancel. That is a *problem*, because a purchase with no displacement is a net add on a
  4.4–8.3% margin.

### Is heavy civil (8.3%) or specialty trade (7.7%) genuinely a better first customer than commercial GCs (4.4%)?

**YES — but the margin number is the weakest of the reasons, and the "better ROI story" argument for GCs is a
trap.** Note the arithmetic first: a $200M GC at 4.2% earns $8.4M NIBT; a $100M heavy civil at 8.7% earns
$8.7M NIBT. **The absolute profit pools are nearly identical**, so the "recovering $1M is 12% of a GC's
profit" headline is a framing artefact of revenue scale, not a real advantage.

The real reasons, ranked:

| Rank | Segment | For | Against |
|---|---|---|---|
| **1** | **Heavy civil / state DOT** | Hard contractual fuse with **statutory waiver + bar to arbitration**; a **mandated costed artefact (estimate + TIA) on a 20-day clock** — i.e. the owner has written the product spec; **8.3–9.8% margin**; a single sophisticated counterparty; a claims culture that already exists; **potentially job-costable / allowable** (Tip Top); few contracts, so per-project pricing works | Incumbents strongest here (P6, InEight, HCSS); Caltrans already supplies ePCR reminders; **most copyable beachhead** because the judgement is externally adjudicated; long public-sector sales cycles |
| **2** | **Specialty trade** | **Highest incidence by far (97% / 77%)**; sharpest, most-felt pain; **largest tech purse as % of revenue (0.40%)**; cheapest, fastest sale; single-sided — the sub buys alone; thousands of buyers | **14.8% SG&A** (highest); least sophisticated buyer; **the eSUB natural experiment says this buyer does not pay for documentation**; relationship suppression is strongest here (94% report strained GC relationships, but only 27% ever walk away) |
| **3** | **Commercial GC** | Best headline % -of-profit arithmetic; largest tech purse in absolute dollars; the only published *magnitude* datapoint (fee erosion) is GC-side | **4.2–4.4% margin — thinnest in the industry**; **structurally conflicted** (claimant upward, payer downward); will use it defensively, as Gather's own eleven case studies demonstrate; Procore's Change Analysis agent is already in their bundle |

**Verdict: heavy civil / state DOT first (best fuse, best artefact spec, best budget line), specialty trade
second as the volume market, commercial GC last despite the best headline arithmetic.**

---

## 5. PERFORMANCE / CONTINGENCY PRICING — THE US LEGAL POSITION

**Question: is a % of recovery legal for a SOFTWARE vendor that is not an expert witness and not a law firm?**

**Short answer: YES in most US states, but only inside a narrow design envelope — and the envelope is much
tighter than "20% of what you recover."** Six bodies of law bear on it. Taken together they permit the model
and dictate its shape.

### Baseline
Contingent-fee compensation for *services* by non-lawyers is legal and commonplace in the United States.
Verified live analogues, each paid a share of money recovered, none of them lawyers:
- **Accounts-payable / profit recovery auditors: typically 20–30% of recoveries** (range cited 10–40%).
  https://www.apexanalytix.com/resources/blog/recovery-audit-cost/ · https://xelix.com/resources/accounts-payable-solutions/recovery-audit/what-is-a-recovery-audit
- **Public insurance adjusters:** licensed, and fee-capped by statute — **Florida 20% (10% during a declared
  state of emergency), Texas 10%, Illinois 10%, Hawaii 8%, Georgia 33.3%**.
  https://publicadjusterauthority.com/public-adjuster-contingency-fee-limits-by-state
- **Litigation funders** take a share of proceeds and are lawful in the major seats (§6).

So the question is not *whether* contingent service fees are lawful. It is *which* of six specific bars a
construction-entitlement software vendor would trip.

### BAR 1 — Testifying-expert contingency: **HARD BAR. Confirmed for the US.**
- **ABA Model Rule 3.4(b)** — a lawyer shall not "offer an inducement to a witness that is prohibited by law";
  the comment records that "it is improper to pay an expert witness a contingent fee."
  https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/rule_3_4_fairness_to_opposing_party_counsel/comment_on_rule_3_4/
- **Alabama State Bar Formal Opinion 1997-02**: an attorney may pay an expert a reasonable fee "but the
  expert's fee may not be contingent on the outcome of the proceeding."
  https://www.alabar.org/office-of-general-counsel/formal-opinions/1997-02/
- Parallel opinions: **Philadelphia Bar Ass'n Op. 94-27**; **California State Bar Formal Op. 1997-149**.
- **This resolves the `UNVERIFIED` flag agent 11 left on US law.** The prohibition operates through the
  rules of professional conduct binding the *instructing lawyer*, plus exclusion/impeachment at trial —
  not through a single federal statute. The practical effect is the same as **CJC Guidance ¶88** and
  ***Factortame (No.8)*** in England.
- **Crucial nuance that cuts the vendor's way:** in *Factortame (No.8)* the Court of Appeal held that
  **Grant Thornton's contingency arrangement to quantify damages was NOT champertous** — the CLSA 1990
  applied only to advocacy and litigation services, not to services *ancillary* to litigation. **The bar is
  on the witness role, not on quantum preparation.** That is the seam.
- **DESIGN RULE 1: the vendor must never be, contract as, or be named as the testifying expert, and its fee
  arrangement must never appear in an expert's instructions.** If the product's output is exhibited to an
  expert report, the vendor's fee arrangement becomes a disclosable and attackable fact.

### BAR 2 — Champerty and maintenance: **MOSTLY DEAD, BUT ONE STATE IS DIRECTLY ON POINT.**
Champerty has been abolished or was never recognised in roughly thirty states (including **California, Texas,
Massachusetts, North Carolina, Ohio, Colorado, Illinois, New Jersey, Virginia, Washington**); Minnesota
abolished it in *Maslowski v. Prospect Funding Partners* (2020). Secondary compilations list
**Alabama, Delaware, Georgia, Mississippi, New York and Pennsylvania** as still recognising it in some form
(`treat the list as secondary` — https://www.steptoe.com/en/news-publications/litigation-funding-update-abolishing-common-law.html).

**The one that matters, and it is a literal description of the proposed pricing model:**
> **KRS 372.060 (Kentucky) — "Champertous contracts and conveyances void."** Any contract or agreement made
> in consideration of **"services to be rendered in the prosecution or defense, or aiding in the prosecution
> or defense, in or out of court, of any suit, by any person not a party on record in the suit, whereby the
> thing sued for or in controversy or any part thereof, is to be taken, paid or received for such services"**
> is **void**. https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=35270

Note the reach: **"in or out of court"** and **"aiding in"**. A software vendor paid a slice of a recovered
claim, in Kentucky, once a suit exists or is in contemplation, is squarely inside that text.

**New York cuts the other way, and the distinction is the design rule.** **Judiciary Law §489** bars
*"buy[ing] or tak[ing] an assignment of… any claim or demand, with the intent and for the purpose of bringing
an action or proceeding thereon."* A fee-for-services contingency **takes no assignment**, so it sits outside
§489. *Justinian Capital SPC v. WestLB AG*, 28 N.Y.3d 160 (2016) confirms the statute and its $500,000 safe
harbour operate on the *purchase price of an assigned claim* — and specifically that a **contingent** payment
obligation defeats the safe harbour. https://www.nycourts.gov/ctapps/Decisions/2016/Oct16/155opn16-Decision.pdf

- **DESIGN RULE 2: the fee must be a fee for services. Never an assignment of, security interest in, lien
  upon, or right of subrogation to, the claim or its proceeds.**
- **DESIGN RULE 3: earn the fee on a PRE-LITIGATION outcome** — an executed change order, a settled REA, a
  negotiated release — **not on "proceeds of a suit."** This alone takes the model outside KRS 372.060's
  text, outside §489, and outside most champerty analyses, because there is no suit.

### BAR 3 — Unauthorized practice of law: **THE REAL RISK, AND CONTINGENCY MAKES IT WORSE.**
- Construction-specific US authority exists: **North Carolina State Bar v. Lienguard, Inc.** (N.C. Business
  Court) held that an online service **preparing claims of lien for others constitutes the unauthorized
  practice of law.** `CITATION UNVERIFIED` — I could not retrieve the primary judgment in this pass; the
  holding is reported at https://www.jdsupra.com/legalnews/business-court-makes-north-carolina-safe-70693/
  and should be confirmed before relying on it. **The direction of travel is clear and adverse:** preparing
  a claim document for another party, for a fee, is capable of being UPL.
- **Procore carries a standing UPL risk factor in its 10-K.** A product that interprets clauses, asserts
  entitlement and drafts notices carries strictly more exposure than Procore does.
- **Contingency pricing aggravates UPL exposure**, because a share-of-recovery fee makes the vendor look
  like counsel rather than a tool vendor.
- **DESIGN RULE 4:** the product generates **the customer's own document, for the customer to review, sign
  and send**; it **never contacts the counterparty**; it outputs *"here is what the contemporaneous record
  supports"*, never *"you are owed $X"*; and it never advises on the merits or prospects of litigation.
  (This also aligns with **AACE RP 29R-03 §1.2(f)** — schedules "do not demonstrate root causation or
  responsibility for delays" — and with the finding that a V1 must not ship an automated attribution verdict.)

### BAR 4 — Government and public contracts: **SPECIFIC RULES, AND ONE OF THEM IS AN ASSET.**
- **FAR 31.205-47(f)(1)** — costs of **prosecuting claims or appeals against the Federal Government** are
  **unallowable**. https://www.acquisition.gov/far/31.205-47
- ***Tip Top Construction, Inc. v. Donahoe*, 695 F.3d 1276 (Fed. Cir. 2012)** — **REA preparation and
  negotiation costs ARE allowable contract administration costs** under FAR 31.205-33 where incurred to
  materially further negotiation, even if negotiation later fails. **This is the asset, not the bar** (§4).
- **Anti-Assignment Act, 31 U.S.C. §3727** — assignments of claims against the United States are void unless
  made after allowance. Reinforces **Design Rule 2**: fee, never assignment.
- **FAR 3.4 / FAR 52.203-5, Covenant Against Contingent Fees** — applies to contingent fees for *soliciting
  or obtaining* the contract, **not** to claim preparation. But **state DOT general conditions may be
  drafted more broadly**; check per contract. `UNVERIFIED` for Caltrans.

### BAR 5 — Litigation-funding registration statutes: **NEW, MOVING, AND A GENUINE OPEN QUESTION.**
- **Georgia SB 69 (2025)**: from **1 January 2026**, any person or entity "engaged in… providing litigation
  financing in exchange for consideration of any kind" must **register with the Georgia Department of Banking
  and Finance**; penalties run from misdemeanour to felony, fines to **$10,000**, imprisonment 1–5 years.
  https://www.hklaw.com/en/insights/publications/2025/05/litigation-funding-in-georgia ·
  https://dbf.georgia.gov/litigation-financiers
- Comparable disclosure regimes: **West Virginia, Indiana, Louisiana, Kansas, Montana**; federal Rule 26
  disclosure proposals pending.
- **The open question:** a *deferred, contingent* fee is economically an extension of credit whose repayment
  depends on litigation outcome. Whether that constitutes "litigation financing" under these definitions is
  **unresolved**, and Georgia's definition is drafted broadly with no visible service-provider carve-out.
- **DESIGN RULE 5:** keep the fee **payable on a commercial outcome (executed CO / settled REA), not on
  litigation proceeds**, and take Georgia counsel before selling contingency into Georgia.

### BAR 6 — Public adjuster licensing: **DOES NOT APPLY — UNLESS YOU TOUCH INSURANCE.**
Public-adjuster licensing statutes (e.g. **Fla. Stat. §626.854**) govern the adjustment of **insurance**
claims. A construction *contract* claim against a GC or owner is not an insurance claim, so the regime does
not bite. **But it bites hard if it does:** in Florida a contractor adjusting an insurance claim without a
public-adjuster licence commits a felony, and the Department has held that even "securing a contract for
repairs" is "any other thing of value" within the definition.
https://www.myfloridacfo.com/division/agents/compliance/adjusters
- **DESIGN RULE 6: never take a contingent fee on an insurance recovery** (builder's risk, CGL, SDI,
  subguard) without a public-adjuster licence in the relevant state.

### VERDICT

> **A percentage-of-recovery fee IS legal in most US states for a software vendor that is neither a law firm
> nor a testifying expert — provided all six design rules hold: (1) never the expert; (2) a fee for services,
> never an assignment or lien on proceeds; (3) earned on pre-litigation commercial outcomes, not suit
> proceeds; (4) the customer's own document, never contacting the counterparty, never a merits opinion;
> (5) Kentucky carved out or restructured (KRS 372.060 is directly on point), Georgia registration checked
> from 1 Jan 2026; (6) insurance recoveries excluded.**

**But the commercial recommendation is: do not lead with contingency.** Three reasons:
1. It invites every one of the six analyses above, in fifty jurisdictions, before you have a customer.
2. The comparables (§6) show the sustainable take is **low single-digit percent**, which does not justify the
   legal overhead of a pure contingency model.
3. It converts the sale from an operating-expense decision (one signature) into a legal-and-finance decision
   (three signatures, one of them outside counsel) — fatal under the solo-founder constraint.

**Recommended structure: subscription or per-project fee as the base, plus a modest capped success component
(e.g. 3–8% of executed change-order value above an agreed baseline, capped per project) — earned at
execution of the change order, never at award of a claim.** This captures the pricing-power argument
(*"only a partisan product can price on recovery"*) without buying the legal exposure of a funder.

---

## 6. THE VALUE-CAPTURE CEILING

### The comparables ladder — and the rule that falls out of it

| Comparator | Take | Downside borne by the taker | Source |
|---|---|---|---|
| Field-layer construction SaaS | $15–90/user/mo | none | category anchor |
| M365 Copilot | $18–30/user/mo | none | Microsoft |
| **Levelset** | **$59/notice, $349/lien filing**; subscriptions from $149/user/mo | none | https://www.levelset.com/pricing/ |
| **Easyclaim (DE)** | **€599 net per case** for a 21-page court-ready quantum derivation | none | vendor |
| **Gather (UK)** | **£500/mo flat**, while publishing **39x ROI** | none | vendor |
| **CEMAR** | **£435/licence/mo**, administering £75bn of works | none | vendor |
| Entitlement-reasoning band (FR/UK/DE convergence) | **€200–500/seat/mo** | none | Contradic, Sypro, Unifier |
| **AP / profit recovery audit** | **20–30% of recoveries** (10–40% range) | **full delivery cost, zero recovery guarantee** | apexanalytix, Xelix |
| **Public insurance adjusters** | **8–33.3%, statutorily capped** (FL 20%/10%, TX 10%, IL 10%, HI 8%, GA 33.3%) | delivery cost | Public Adjuster Authority |
| **Claims consultants** | **100% of hours**: $240k–$660k per $5–25m matter = **1.2–3.6% of the disputed sum** | delivery cost | `DERIVED`, agent 11 |
| **Litigation funders** | **20–40% of proceeds** (widely cited; not published by Burford or Omni). Screen: **award ≥10x funding** | **full capital at risk + total loss on failure** | Omni Bridgeway criteria |

> ### THE STRUCTURAL RULE
> **Take scales with downside borne.** Funders take 20–40% because they lose everything if the claim fails.
> Recovery auditors take 20–30% because they carry the entire delivery cost with no recovery guarantee.
> Public adjusters take 8–20% under a statutory cap because their capital is only their own labour.
> Consultants take 1.2–3.6% of the disputed sum because they are paid regardless of outcome.
> **A software vendor bears neither capital risk nor material delivery cost. Its defensible take sits at the
> BOTTOM of this ladder, next to the consultant — not next to the funder.**

### Applied: what can be captured from a $412,000 enabled recovery?

| Model | Capture | % of $412K |
|---|---|---|
| Per-seat SaaS at the field-layer anchor | $3–10K/yr across the whole account | **<2.5%** (and not attributable to this claim) |
| Entitlement-reasoning subscription (€200–500/seat/mo, CEMAR/Gather band) | $6–12K/yr | **1.5–3%** |
| **Per-claim artefact fee** (Easyclaim proves the shape at €599; far too cheap for a US six-figure event) | **$2,500–$10,000** | **0.6–2.4%** |
| **Subscription + capped success component at 3–8%** | **$12K–$33K** | **3–8%** |
| Full consultant substitution (delivering chronology + priced position, bearing delivery risk) | at 1.2–3.6% of disputed sum | **$5K–$15K** |
| Funder-equivalent 20–40% | $82K–$165K | **NOT ACHIEVABLE.** Requires bearing capital and total-loss risk, invites the champerty analysis, and exceeds every public-adjuster statutory cap |

> **REALISTIC VALUE-CAPTURE CEILING ON A $412K RECOVERY: $5,000–$30,000, i.e. 1.5%–8%.**
> Note the convergence: the consultant's own revealed share (1.2–3.6% of disputed sum → $5–15K) and a
> 3–8% capped success fee ($12–33K) land in the same box from two completely independent directions.
> **That box is the ceiling. Anything above ~10% is funder pricing for non-funder risk.**

### The three consequences for pricing architecture

1. **Never price per seat.** The commodity price of contract reading is $0 (Trunk Tools gives it away;
   Procore ships it natively) and DocuSign IAM bundles AI extraction at $45–80/user/mo. Per-seat pricing is
   structurally capped at ~$50–150/user/mo — which is why the entire US field layer is locked out of recovery
   economics.
2. **Price per project or per claim.** Per-project maps to how contractors budget, is job-costable, and — on
   federal/federally-aided work — is potentially an **allowable** contract-administration cost (Tip Top).
3. **The business is a portfolio of $5–30K captures, not a share of megaclaims.** A $200M contractor with
   2–4 events per year yields $10K–$120K/yr. That is a real ACV, in the CEMAR/Gather band, reachable without
   contingency at all. **The recovery share is a pricing-power argument, not a business model.**
   BauAgent's line remains the most transplantable framing found anywhere:
   **"one Nachtrag finances the annual subscription."**

---

## 7. HARDEST FACTS FROM THIS PASS

1. **CFMA FY2024: "Professional Fees" (0.50% of revenue, ~$697K on $139.4M) is 1.9x "Technology Costs"
   (0.26%, $368K).** Sold as software the product competes for the smaller purse; sold as a substitute for
   consultant and counsel hours it competes for the larger one.
   https://cfma.org/files/o-files/download-file/5aff6a42-7a29-491c-bb4a-fde57e74487b
2. ***Tip Top Construction, Inc. v. Donahoe*, 695 F.3d 1276 (Fed. Cir. 2012): REA-preparation costs incurred
   to further negotiation are ALLOWABLE contract administration costs (FAR 31.205-33); only post-CDA-claim
   costs are unallowable (FAR 31.205-47(f)(1)).** A pre-claim product is job-costable and potentially
   recoverable on federal/federally-aided work — it escapes the 0.26% technology cage.
   https://www.cafc.uscourts.gov/9-19-2012-2011-1509-tip-top-construction-inc-v-donahoe-11-1509/
3. **"98% of GCs have experienced fee erosion due to change order negotiations; nearly half say erosion
   exceeded 10% of their fee on at least some projects."** The ONLY published *magnitude* figure in the
   category — everything else in the program is incidence.
   https://www.clearstory.build/construction-blog/2026-gc-change-order-report
4. **KRS 372.060 voids any contract for "services to be rendered in the prosecution or defense… in or out of
   court, of any suit, by any person not a party on record… whereby the thing sued for… is to be taken, paid
   or received for such services."** The single most on-point US statutory hazard for %-of-recovery software
   pricing. https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=35270
5. **Caltrans already runs an Electronic Potential Claim Record (ePCR) system — Adobe Forms on a database,
   used by contractors AND Caltrans, generating workflow and email notifications and reminders.**
   The owner supplies the deadline-alert layer free. Fourth independent confirmation that alerting is not the
   wedge; the wedge is the costed estimate + TIA. https://dot.ca.gov/programs/construction/epcr
6. **AP/profit recovery auditors take 20–30% of recoveries while bearing the full delivery cost; litigation
   funders take 20–40% while bearing full capital risk; claims consultants capture 1.2–3.6% of the disputed
   sum while bearing neither.** Take scales with downside borne — a software vendor belongs at the bottom.
7. **Rabbet's $280bn "cost of slow payment" is a modelled 14% of total construction cost from a survey that
   is 93% general contractors and 7% subcontractors.** It is not a write-off figure and must not be used as
   one. https://cdn.prod.website-files.com/679b71850706204b0b01c1bb/67d8173245dbbd8a4eae3216_2024%20Construction%20Payments%20Report.pdf

---

## 8. UNKNOWNS — AND WHAT WOULD SETTLE EACH

| Unknown | What would settle it |
|---|---|
| **THE NUMBER: dollar value of change-order/entitlement work written off per year, as % of revenue, for a named contractor.** Every ROI in §3 rests on a modelled leak of 0.1–0.6% of revenue and **no published source establishes it.** | 30 structured interviews with construction controllers/CFOs, one question: *"In your last fiscal year, what dollar value of work did you perform and either never bill, or bill and not collect, because the change order was never executed or was negotiated down?"* Sourceable through CFMA chapters. **This is the single number to verify before committing.** |
| **Potential-claim events per year per $100M of heavy-civil revenue** (the ROI (c) driver, currently a pure `ASSUMPTION` of 2–4) | Caltrans ePCR filing counts are likely obtainable under a California Public Records Act request: PCRs filed per contract per year, and how many were supplemented with a costed estimate + TIA within the deadline vs waived. **This is a public-records question, not a survey question — and it would produce a defensible number nobody has.** |
| **Change-order value as % of contract value** (the ROI (a) driver; currently a trade-guide 5–10%) | A state DOT change-order database (TxDOT's 3,957-project dataset, INDOT, FDOT) gives this precisely for heavy civil. For commercial building, a CFMA or AGC cut. |
| **Dodge/Clearstory SmartMarket methodology** — n, dates, respondent screening — is undisclosed on every public page. The 77% / 97% / 98% figures are load-bearing for the whole thesis and are vendor-commissioned. | The full SmartMarket Insight PDFs from construction.com, or a direct request to Dodge. |
| **Whether Caltrans/state DOT contracts permit claim-preparation costs to be job-costed or recovered** (the Tip Top logic is federal) | Caltrans Standard Specifications §9 and the Construction Manual; or a single interview with a heavy-civil controller. |
| **Actual conversion of a "priced, evidenced position" into paid dollars.** The one product in the world doing entitlement detection well (Gather) has **eleven case studies and not one documented recovered compensation event in GBP** — its named outcomes are client-side savings and admin efficiency. | A pilot with instrumented before/after change-order realisation on 3–5 projects. **Until this exists, the recovery pitch is unevidenced by anyone, anywhere.** |
| **N.C. State Bar v. Lienguard** primary citation and holding scope | The North Carolina Business Court opinion. |
| **Whether a deferred contingent software fee is "litigation financing" under Georgia SB 69** and its peers | Georgia counsel; Department of Banking and Finance guidance. |
