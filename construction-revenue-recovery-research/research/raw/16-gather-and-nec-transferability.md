# 16 — GATHER (gatherinsights.com) & THE NEC4→US TRANSFERABILITY QUESTION

Research date: 19 August 2026. All URLs live-fetched this session unless marked.
Primary sources used in brief-priority order: company website + API docs + G-Cloud filings,
UK Companies House statutory accounts (10215108), published case studies, then press.

---

# EXECUTIVE ANSWER (read this if you read nothing else)

**Gather is a THESIS-PROOF for the mechanism and a THESIS-KILLER for the naive version of the business.**

Four findings invert the prior agent's read of this company:

1. **Gather does NOT do quantum.** Confirmed from their own words on two independent pages.
   The AI stops at: detect event → map clause → start the clock → assemble substantiation.
   The QS prices the CE. See §A3.
2. **Not one of Gather's eleven published case studies documents a recovered compensation
   event in £.** The two headline numbers everyone quotes are the opposite of what they look
   like. The Network Rail "£300,000+ saved" is money the **client saved by cutting back the
   contractor's change requests**. The Circet "£140,000" is **administrative labour cost**
   (£1,012/wk + £2,400/wk × 26 weeks). Costain A12's headline is "**15% of claims rejected on
   the spot**." Gather's evidenced ROI is claims *defence* and admin efficiency — not revenue
   recovery. See §A4.
3. **Gather is a micro-company, not a rocket.** Statutory accounts to 31 Mar 2026: net assets
   £537,435; cash £134,699; **10 average employees, down from 14**; loss of £93,424; **lifetime
   equity raised ≈ £713k**; still repaying a Rail Supply Growth Fund loan. Published price:
   **£500/month**, unlimited users. See §A5–A6.
4. **There is zero evidence of a US move.** 337-URL sitemap: no AIA, no ConsensusDocs, no US
   page, no US customer, no US entity, no US job posting. Data residency contractually **UK/EEA
   only**. Contracts supported are NEC3, NEC4, JCT, FIDIC. They are not on the Procore App
   Marketplace at all. See §A7.

And on Part B, the decisive finding:

5. **The NEC4 workflow does NOT port to AIA A201 — but it ports almost perfectly to US
   *federal* and *state DOT* contracts, which are HARDER than NEC4.** Caltrans requires an
   Initial Potential Claim Record within **5 business days**, a Supplemental PCR **with an
   itemised cost estimate and a Time Impact Analysis within 15 days**, and states that failure
   is "**Waiver of the potential claim … [and] Bar to arbitration**." That is a shorter fuse
   than NEC4's eight weeks *and* it demands the quantum Gather refuses to produce. See §B6.

---

# PART A — GATHER, EXHAUSTIVELY

## A1. Snapshot

| Field | Value | Source |
|---|---|---|
| Legal entity | **Gather Insights Limited**, England & Wales, **10215108** | https://find-and-update.company-information.service.gov.uk/company/10215108 |
| Former name | **RAIL DIARY LIMITED**, 06 Jun 2016 – 16 Jan 2024 | Companies House, "Previous company names" |
| Incorporated | **6 June 2016** (site claims "Founded 2018") | Companies House overview |
| Registered office | 1 Silk Street, Manchester, M4 6LZ | https://www.gatherinsights.com/en/security |
| SIC | 62012 Business and domestic software development | Companies House |
| Headcount | **10** (avg monthly, FY to 31 Mar 2026), was 14 in FY25 and FY24. LinkedIn banding "11–50" | AA filed 10 Jun 2026, note 3; https://www.linkedin.com/company/gatherinsights/ |
| Ownership | **W J Doyle 48%** (ultimate controlling party). Angel-funded, no institutional VC | AA to 31 Mar 2025, note 11 |
| Published price | **£500 / month**, enterprise SaaS, **not per user**; setup ≈ 2× monthly; training £1,400 in person / £450 online | G-Cloud 14 pricing doc (28 Feb 2024) |
| Geography | **UK only**, plus Ireland via Dornan. Data residency **UK / EEA** | G-Cloud 14 service definition |
| Contracts supported | **NEC3, NEC4, JCT, FIDIC** — no AIA, no ConsensusDocs | https://www.gatherinsights.com/en/qs-ai-agent |
| ICP | UK infrastructure — rail, highways, water, energy, aviation, nuclear, defence; asset owners AND Tier 1 contractors | LinkedIn specialties; /en/client, /en/contractors |

**Leadership** (https://www.gatherinsights.com/en/about):
- **William (Will) Doyle — Founder & CEO.** RICS chartered quantity surveyor, 8 yrs Malaysia/HK/UK.
  *"I built Gather because I was sick and tired of terrible records."* Origin story: nearly lost
  £20m of entitlement on the North West Electrification Programme.
- **Paul Clegg — CTO.** Co-founded with Doyle 2018. **Resigned as director 4 April 2026** (TM01
  filed 30 Apr 2026) but still listed as CTO on the About page. Flag.
- **Ben Walker — Commercial Director.** Founder of **CEMAR** (2003, acquired by Thinkproject 2018),
  **NEC4 drafting team member since 2015**, NEC trainer at Thomas Telford (ICE). Appointed director
  **28 June 2024**, same day as the share allotment. This is the single strongest asset in the company.
- **Nick Woodrow — Operations Director.** Chartered civil engineer, ex-COO of CEMAR then Thinkproject
  UK. **Resigned as director 25 March 2025** (TM01 filed 1 Apr 2025). Still on the About page. Flag.
- **Steve Secker — non-executive chair** (McCarthy Stone). Director since 1 Apr 2019.

> **Correction to the prior pass:** Gather was NOT founded by Ben Walker. It was founded by
> Will Doyle as Rail Diary. Walker is a 2024 hire/investor. The CEMAR pedigree is real but it is
> two years old inside this company, and the other CEMAR alumnus (Woodrow) has already left the board.

## A2. The product surface — what the QS AI Agent actually is

**Four modules** (https://www.gatherinsights.com/en/qs-ai-agent, "How Gather works"):

| Module | Function |
|---|---|
| **Plan** | Programme & budget import. *"Your programme becomes your progress tracker."* Pre-populates 64% of diary fields from the programme. |
| **Record** | Mobile-native site diary. Offline-first, voice-to-text, GPS+timestamp photos, 3-minute shift record. |
| **Report** | Real-time dashboards, productivity, **CVR**, Power BI via Reporting API, branded shift PDFs. |
| **QS AI Agent** | *"Every event. Every clause. Caught in time."* Reads every shift record. |

**Six named QS AI Agent capabilities**, verbatim from the product page:

1. **Early Warning Detection** — *"scans every shift record for emerging risks… Late deliveries,
   resource constraints, access issues."* Contracts supported: NEC3 / NEC4 / JCT / FIDIC.
2. **Compensation Event Detection** — *"Your site team sees 'revised drainage layout' and files it
   away. The AI recognises it as a change to the Works Information under clause 60.1(1), calculates
   the impact, and tells you exactly what to do next."*
3. **Pattern Recognition** — *"Productivity dropped 30% since access change in Zone B. Cumulative
   delay now exceeds compensation threshold."*
4. **Contract Intelligence** — clause mapping (60.1(5)), **evaluation method** (63.1 "Assess using
   Defined Cost plus Fee"), **Documentation Required** list.
5. **Construction Methodology** — cascade impact demo: Piling Sequence Change → Crane Mob £5,400 →
   Steel Erectors £12,000 → Programme Impact £3,600 → **Total Impact £21,000**.
6. **Actionable Outputs** — *"Draft notices, flag EOT opportunities, suggest risk updates… Every
   insight comes with a confidence score."* 85%+ = "reliable enough to act on directly."

**Inputs:** structured shift/diary records from the Record module; contract type + amendments
declared at setup (*"You tell us your base contract and any key amendments during setup"*);
programme and budget from Plan; Met Office weather data; historical project records.

**Outputs:** event flag + type, clause reference, time impact narrative, cost impact narrative,
contractual notice status, recommendation, confidence score, documentation-required list, draft notice.

**Headline claim:** *"QS AI Agent identifies 40% more change events than manual review"* against an
asserted industry baseline that *"QSs only identify 60% of legitimate change events during manual
reviews."* The 60% baseline is asserted, not sourced. `UNVERIFIED`.

**Developer surface** (https://docs.gatherinsights.com/openapi.json — "Gather Platform Public API v1.0.0"):
18 endpoints, server `https://app.gatherinsights.com/public/api/v1`, Bearer auth from an API key.
Endpoints: `/auth`, `/workspace/{uuid}/projects|tags|people`, `/user/{uuid}/projects`,
`/project/{uuid}/assignments|resources/labour|shift-records`, `/shift-records/{uuid}`,
`/attribute/{uuid}/{attributeName}` (GET+PUT), `/fatigue/calculated`, `/assets/{uuid}`, `/assets/bulk`,
`/webhooks` (+ delete, rotate-secret), `/report-schemas/{uuid}`, `/cached-report/{uuid}/{reportName}`.

> **There is no compensation-event, entitlement, notice, or AI-agent endpoint in the public API.**
> The API exposes the *record layer*, not the *intelligence layer*. Rate limits are tiny
> (2 req/sec on shift records). This is a data-export API, not a platform API.

## A3. QUANTUM — definitive answer: **NO, they stop at notice + substantiation**

Three independent pieces of their own evidence:

**(i) The product page's own worked example.** Under "Compensation Event Detection", the demo output
reads: *"Cost Impact — **Cost of extra materials, labour, and plant to be calculated.**"* and
*"Recommendation: Acknowledge the instruction. Prepare and submit a detailed quotation for the change
within the contractual timeframe."* The system tells the QS to go and price it.
(https://www.gatherinsights.com/en/qs-ai-agent)

**(ii) Their own blog, 22 July 2026 — the clearest statement they have ever published.**
From "CE quotations that survive PM scrutiny under NEC4"
(https://www.gatherinsights.com/blog/ce-quotations-that-survive-pm-scrutiny):

> *"This is exactly the work the QS AI Agent is built to carry. Gather reads every site diary entry
> as it lands, links it to the programme activity and the cost code, and **surfaces the records that
> back a compensation event** before the notice period runs out. When it is time to price the CE,
> **the substantiation is already assembled**, not reconstructed from four spreadsheets and an inbox."*

The whole article is a *manual* how-to for a human QS to build the Defined-Cost-plus-Fee line by line
under clause 63.1, justify the clause 63.5 risk allowance, and show the programme change under 62.2.
It is written because the product does not do it. Its own worked example is a human QS pricing a
drainage CE at £48,000, being assessed down to £31,000, and settling at £44,000.

**(iii) The one apparent counter-example is a mockup.** Capability 05's £21,000 cascade panel is a
static illustration inside a marketing page; the page's own FAQ describes outputs as
"recommendations", "action plans" and "confidence scored recommendations", and states
*"Will this replace our QS team? **No.**"*

**Verdict: `recoverable_dollar_estimation` = 1.** The pipeline is
`detect → clause-map → start clock → assemble evidence → draft notice`.
**Quantum is the missing link, and it is missing deliberately** — see §A9 on why.

## A4. Every published case study, with the numbers read properly

Eleven customer stories at https://www.gatherinsights.com/en/customer-stories.
Every one is UK; ten of eleven are UK rail/highways/underground.

| Customer / project | Headline metric | **What the money actually is** |
|---|---|---|
| **Network Rail + J. Murphy & Sons**, Birmingham New Street (£15m) | **39× ROI; £300,000+ saved**; 383 records | **CLIENT-SIDE SAVING.** *"Network Rail's project team had all the resources to **scrutinise** labour, plant and time allocation to each of the relevant activities **included in change requests**. This resulted in total savings of well over £300,000."* Money **withheld from the contractor**, not recovered by one. |
| **Circet (KN Circet UK)**, TfL Four Lines Modernisation (£8m) | **15× ROI; £140,000 in 6 months; 11% cost reduction; 1,626 hrs** | **ADMIN LABOUR SAVING.** *"The savings spanned contractor management (£1,012 per week) and commercial management (£2,400 per week)."* Not entitlement. |
| **Costain**, A12 upgrade (£1.2bn), 100+ subcontractors | **15% of change events rejected weekly** | **CLAIMS DEFENCE.** *"the project team could immediately identify claims where records did not match the application."* Plus: *"All compensation events are now processed within the same week of application."* |
| **Cubby Construction** (£30m turnover) | 4,000+ records, 100+ users, **4,045 variances across 1,465 shifts on CSLR** | Variance categorisation aligned to clause 60.1. Note: *"**10 quantity surveyors now review and categorise shift records daily**."* Human-in-loop. |
| **Alma Rail** (£7m turnover) | **21× ROI**, 60+ records/mo, 100% adoption | *"time savings, reduced admin costs, and critically revenue protected through proper documentation"* — no £ recovered stated. |
| **Balfour Beatty**, Core Valley Lines (£378m TfW) | 30+ min saved/record; 6,935 records; 64% pre-fill | Efficiency only. |
| **Balfour Beatty**, Ealing Common Depot ITT (£2.5m) | 9,576 people-hours; 56 shifts; 3 weeks | Efficiency only. |
| **Costain**, Gatwick Airport Station (£150m) | 25–35 hrs/wk saved; 70 users in 4 weeks | Efficiency only. |
| **Amey**, Brent Cross | 10+ hrs/wk; 2,000+ records; 30 depots | Efficiency only. |
| **Dyer & Butler**, Bough Beech (£17m emergency) | 10,000+ hrs; 300+ workers; 48-hr deploy | Efficiency only. |
| **Fourway** (£35m/yr) | 70% reporting time cut; 17,500+ records; 5 yrs | Efficiency only. |

**Verification against the customer's side:** Circet's quoted Senior PM, **Nick Mansell**, later
became **an investor in Gather** (July 2024 round) and is quoted in the funding press release
re-stating the 11% figure — so the strongest "customer proof" is also a shareholder.
(https://www.gatherinsights.com/blog/construction-record-management-startup-gather-secures-new-investment-round)
The Circet release also mis-states the saving as *"1,626 work hours **per week**"* where the case
study says 1,626 hours over six months. Treat Gather's ROI multiples as **marketing arithmetic**,
`UNVERIFIED` independently.

> **This is the single most important finding in Part A.** Gather is *marketed* as
> "Get paid for compensation events" (/en/business: *"40% of variation revenue recovered"*)
> but is *proven* as an assurance-and-efficiency tool, and its biggest named number was earned
> **defending an owner against a contractor's change requests**. Their own About page says the
> quiet part: *"**We don't take sides.** We provide the objective, timestamped evidence that allows
> Contractors and Clients to agree on fair payment."*

## A5. Companies House — statutory financials (10215108)

All figures from the filed accounts. `Total exemption full accounts` = small-companies regime;
**no profit & loss account is filed**, so turnover is not public.

| £ | FY2024 (31 Mar 24) | FY2025 (31 Mar 25) | FY2026 (31 Mar 26) |
|---|---|---|---|
| Intangibles (capitalised R&D, NBV) | 1,173,014 | 1,285,123 | 1,259,496 |
| Cash at bank | 56,875 | 68,636 | **134,699** |
| Debtors | 150,274 | 186,531 | 72,691 |
| Creditors < 1 yr | (426,000) | (344,233) | (520,284) |
| — of which accruals & deferred income | — | 231,281 | **334,572** |
| Creditors > 1 yr (loans) | (574,759) | (567,063) | **(413,632)** |
| **Net assets** | 382,792 | 630,859 | **537,435** |
| Called-up share capital | 209 | 244 | 244 |
| **Share premium** | 355,307 | **712,919** | 712,919 |
| P&L reserves | +27,276 | (82,304) | **(175,728)** |
| **Implied result for year** | — | **loss (109,580)** | **loss (93,424)** |
| **Avg monthly employees** | **14** | **14** | **10** |
| R&D capitalised in year | — | 289,186 | **183,761** |
| R&D amortisation charge | — | 177,077 | **209,388** |

Directors' report, FY2025 (verbatim):
> *"Gather Insights has had a year of consolidation with turnover largely unchanged from the previous
> year. Profitability has taken a hit as we had invested in expanding the team… we experienced a
> **high level of churn** partly connected to the end of projects and the end of **Network Rail's
> control period**/uncertainty over its investment plans. We have refocused our efforts on achieving
> positive cash flow… **Sadly this has meant restructuring our team and saying goodbye to some valued
> colleagues.** We are grateful for the continued support of our lender the **Rail Supply Growth Fund**."*

Directors' report, FY2026 (verbatim):
> *"This year has been one of consolidation having taken decisions in early 2025 to refocus sales on
> enterprise infrastructure customers and reduce our costs. We've made good progress with our biggest
> contract wins across a number of sectors. Financially we have generated positive cash flow and
> started repaying our start-up debt. We are well placed to grow."*

**Reading:** they cut headcount 29%, halved R&D capitalisation, turned cash-flow positive, and
started paying down a £550k rail-sector development loan. **Amortisation (£209k) now exceeds new
capitalised R&D (£184k)** — the product asset is shrinking. Deferred income up 45% is the one clear
growth signal. Turnover is not disclosed; with 10 staff and Manchester salaries, a defensible
estimate is **£1.0m–£1.6m — `UNVERIFIED`, method: headcount × loaded cost + £93k loss + capitalised R&D.**

**Filing history — funding events (SH01 = share allotment):**

| Date | Event |
|---|---|
| 14 Dec 2018 | SH01, allotment 30 Nov 2018 (statement of capital £122.70); SH02 sub-division |
| 21 Mar 2019 | SH01 ×2 (£122.70) |
| 18 Mar 2019 | **MR01 — registration of charge 102151080002**, created 14 Mar 2019 |
| 26 Jul 2019 | SH01, allotment 22 Mar 2019 (£189.00) |
| 1 Jun 2021 | **SH01, allotment 7 May 2021 (£209.20)** — same date as Nick Woodrow's appointment |
| 16 Jan 2024 | **CERTNM — name changed from RAIL DIARY LIMITED to GATHER INSIGHTS LIMITED** |
| 2 May 2024 | MR04 — satisfaction of charge 102151080001 in full |
| 1 Jul 2024 | **AP01 — Benjamin Walker appointed director, 28 June 2024** |
| 18 Jul 2024 | **SH01, allotment 28 June 2024 (£244)** — the "new investment round" |
| 1 Apr 2025 | **TM01 — Nicholas Terence Woodrow terminated 25 Mar 2025** |
| 30 Apr 2026 | **TM01 — Paul David Clegg terminated 4 Apr 2026** |
| 10 Jun 2026 | AA to 31 Mar 2026 |

**Size of the July 2024 round, derived from the accounts:**
share premium 355,307 → 712,919 = **+£357,612**; share capital 209 → 244 = **+£35**;
shares 2,092 → 2,440 = **348 new ordinary 10p shares**.
⇒ **≈ £357,647 raised at ≈ £1,027.72/share, implying a ≈ £2.5m post-money valuation.**
`Derived, high confidence` — arithmetic from filed balance sheets.
**Lifetime equity raised across all rounds since 2016 ≈ £713,163.**

Investors named in the round (https://www.gatherinsights.com/blog/construction-record-management-startup-gather-secures-new-investment-round, 19 Jul 2024):
Nick Mansell (CEO Intermarine UK; ex-CPC Project Services PM on TfL 4LM), **Ben Walker**,
**Daniel Walker (former CIO, Thinkproject UK)**; existing: Steve Secker (McCarthy Stone),
Dave Price (Exxon Mobil). **No institutional VC. No PitchBook-verifiable round size** (profile
returns 403).

## A6. Pricing — published, not estimated

From the **G-Cloud 14 Pricing Document**, dated 2024-02-28, filed by Gather Insights Limited with the
Crown Commercial Service
(https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/719502/250831346049155-pricing-document-2024-02-28-0942.pdf):

> *"The Gather platform is provided as enterprise Software as a Solution (SaaS) and **not priced per
> User**… We offer a **single subscription price with no add-ons, uplifts or banded costs**."*

| Item | Price |
|---|---|
| One-off setup & configuration | **Typically 2× the monthly subscription fee** |
| Monthly enterprise subscription | **From £500 PCM** |
| Training | **£1,400 in person / £450 online** |
| Development (bespoke features, non-standard Power BI) | Priced on request |

Marketplace listing states **"£500 a licence a month. Free trial available."**
(https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/250831346049155)
Benefits list includes: *"On average clients achieve **minimum 10× ROI**."*

**Implication:** ≈ **$630/month**. Sub-CEMAR (£435/licence/month × many licences), sub-Procore, and
priced as an *efficiency* tool. A product that genuinely arbitraged six-figure entitlement would not
be sold flat at £500/month with no value component. **`performance_pricing_compatibility` = 1.**

## A7. GEOGRAPHY — are they entering the US? **No. Not remotely.**

Evidence, each independently checked:

| Test | Result |
|---|---|
| **Sitemap sweep** (337 URLs pulled from https://www.gatherinsights.com/sitemap.xml) | **Zero** URLs containing `aia`, `consensusdocs`, `us`, `usa`, `america`, `federal`, `texas`, `california`. Every contract page is `/en/nec4/*`. |
| **Contracts supported on the product page** | NEC3, NEC4, JCT, FIDIC. **AIA and ConsensusDocs absent.** |
| **Customer stories** | 11 of 11 UK. Network Rail, TfL, TfW, Balfour Beatty, Costain, Murphy, Amey, Circet, Cubby, Alma, Dyer & Butler, Fourway. |
| **Data residency** | G-Cloud service definition: *"Data storage and processing locations: **United Kingdom / European Economic Area (EEA)**"*, and *"User control over data storage and processing locations: **No**."* A hard blocker for US federal and most US enterprise procurement. |
| **Accreditations** | ISO 27001, ISO 9001, **Cyber Essentials Plus, G-Cloud 14 (Crown Commercial Service)** — an entirely UK-public-sector trust stack. **No SOC 2, no FedRAMP, no StateRAMP.** (https://www.gatherinsights.com/en/security) |
| **Support hours** | *"9 to 5 (**UK time**), Monday to Friday"* — no US coverage. |
| **Offices / entity** | LinkedIn: Manchester only, no international offices. No US-registered entity found. |
| **Job postings** | None found, US or otherwise. Headcount **fell** 14→10. |
| **Own meta description** | *"Gather AI flags compensation events before the NEC time bar, so **UK contractors** recover revenue."* |
| **Closest US linkage** | **Dornan — A Turner Company** (Sept 2025). Irish-HQ MEP specialist, 1,350 staff, part of **Turner Construction's European** arm. Semiconductor/biotech fabs. This is Turner's *Europe* business on *European* projects. It is the only plausible vector into a US GC — and it is indirect. (https://www.gatherinsights.com/blog/dornan-partners-with-gather) |

**Verdict: the US market is uncontested by Gather, and their architecture, certifications, contract
library and sales motion would all need rebuilding to enter it.** With 10 staff, £135k cash and a
loan to repay, they cannot. Runway to a US entry is measured in **years, not quarters** — if ever.

## A8. Procore relationship — weaker than claimed

- Gather's site advertises **"Procore — Two-way Sync"**, *"Sync Daily Log entries"* and *"Push
  documents"* (https://www.gatherinsights.com/en/contractors).
- **They are NOT listed on the Procore App Marketplace.** I pulled the full marketplace catalogue
  (https://marketplace.procore.com/apps, 4.48 MB, descriptions rendered inline) and grepped:
  `gather insights` = **0 hits**; `gatherinsights` = 0; `raildiary` = 0; `rail diary` = 0.
  Control test on the same file: `Document Crunch` = 1, `Clearstory` = 1, `Raken` = 1, `Bluebeam` = 1.
  Direct slug probes `/apps/gather`, `/apps/gather-insights`, `/apps/raildiary` all 302/404.
- Procore's marketplace holds **539 listings**, and **68.51% of ISV partners are US-based**
  (https://www.calanceus.com/blog/the-new-and-updated-procore-app-marketplace).

**Benchmark against Document Crunch (187 installs / zero data permissions): Gather is at ZERO
installs and NO listing.** Their Procore integration is a bespoke/customer-level connection, not a
distributed marketplace app. `procore_integration` = 2 (claimed and plausibly real, but unlisted,
unmeasured, and carrying none of the marketplace's distribution).

Other integrations claimed: **CEMAR**, Contract Bee, Autodesk Construction Cloud ("Direct Link —
sync issues & photos"), Aconex, Thinkproject, Viewpoint, Fieldwire, Microsoft Copilot & 365
(native add-in + SSO), Excel/Power BI, and an **MCP server**:
> *"Our MCP server exposes QS AI Agent capabilities to Microsoft Copilot, ChatGPT, and other
> compatible AI assistants. Query your project data, run compensation event analysis, or generate
> draft notices from whichever interface your team prefers."*

Note the strategic posture: Gather explicitly **feeds** CEMAR/Contract Bee/Aconex rather than
replacing them. They are the *sensing* layer for someone else's *administration* layer.

## A9. Roadmap signals

- **Content sprint, mid-2026.** Blog index shows ~10 posts dated 22–30 July 2026 plus March 2026,
  and a large programmatic SEO estate: `/en/nec4/*` (25 pages), `/en/earned-value/definitions/*`
  (~95 glossary pages), `/en/site-diary/*`, `/en/ai-construction/{quantity-surveyors, commercial-managers,
  project-managers, site-engineers, project-directors}`, `/en/free-templates-and-tools/*`.
  This is a **content/SEO growth motion, not a product motion**.
- **Calculators spun out to a free sister platform, "QS Tools."** The 8-week time-bar calculator and
  the "missed CE cost estimator" now live off-platform: *"QS Tools is our free sister platform,
  built by the founders of Gather. It's free, needs no Gather account."*
  (https://www.gatherinsights.com/en/nec4/time-bar-calculator)
- **MCP thought-leadership, Feb 2026** (https://www.gatherinsights.com/blog/mcp-quantity-surveyors-ai):
  Doyle predicts *"Within two years, specialist MCP servers will exist for…"* — betting the
  intelligence layer becomes accessible from Copilot/ChatGPT rather than from Gather's own UI.
- **Owner-mandated GTM.** The /en/client page is a playbook for asset owners to **fund the licences
  and specify Gather in the Works Information**: *"4.7 Commercial Record Management — The Contractor
  shall use the Employer's nominated Commercial Record Management System (Gather)…"* This is a
  contract-form-dependent channel with no direct US analogue.
- **Z-clause handling** — https://www.gatherinsights.com/blog/qs-ai-agent-z-clauses.
- **Hiring: none visible; headcount down.** No US posting, no sales expansion posting.
- **Not building quantum.** No roadmap signal, no blog, no job, no marketing claim points at
  CE pricing. The July 2026 quotations blog *teaches humans to do it manually*.

## A10. Capability matrix — Gather

| # | Dimension | Score | Justification (URL) |
|---|---|---|---|
| 1 | contract_ingestion | **2** | Contract *type + amendments declared at setup*, not document ingestion: *"You tell us your base contract and any key amendments during setup."* Z-clause handling exists. /en/qs-ai-agent |
| 2 | clause_extraction | **2** | Built-in clause library for NEC3/4, JCT, FIDIC (60.1(1), 60.1(2)/(5), 63.1) — mapping *to* clauses, not extraction *from* your contract PDF. /en/qs-ai-agent |
| 3 | notice_detection | **3** | The headline capability. Detects CEs and Early Warnings from every diary entry; "40% more change events than manual review." /en/qs-ai-agent |
| 4 | deadline_tracking | **3** | *"starts every NEC4 clock, from the 8-week compensation event bar to the 2-week quotation reply"*; "Alerts before time bars expire". /en/nec4/nec4-time-limits |
| 5 | rfi_event_ingestion | **1** | No RFI/TQ module. RFI-TQ register is a free downloadable Excel template only. /en/free-templates-and-tools/templates-rfi-tq-register |
| 6 | email_ingestion | **1** | No mailbox ingestion. M365/Copilot add-in + MCP are *query* surfaces. Blog actively complains that value is trapped in email/WhatsApp without ingesting either. /blog/qs-reviewing-whatsapp-messages |
| 7 | daily_report_ingestion | **3** | This IS the product. 10m+ records; 3-minute shift record; offline; voice-to-text; GPS. /en/record |
| 8 | schedule_integration | **3** | Plan module imports programme & budget; 64% pre-fill from programme; Primavera P6 translated to daily activities at Network Rail. /customer-stories/network-rail-murphy-birmingham-new-street |
| 9 | change_order_workflow | **1** | No CE register or workflow. Explicitly feeds CEMAR / Contract Bee / Aconex, which administer. /en/contractors |
| 10 | claim_identification | **3** | Identifies CEs, variations and EWs at event level with clause + confidence score. /en/qs-ai-agent |
| 11 | delay_detection | **2** | Pattern recognition (productivity drop, access/possession vs planned, weather vs contract threshold) but no CPM/critical-path delay analysis. /en/business |
| 12 | responsibility_attribution | **2** | Event types map to Employer failures (60.1(2)/(5)); *"they could easily identify the responsible contractor"*; three-tier supply-chain hierarchy at Costain A12. |
| 13 | contemporaneous_evidence_graph | **3** | Records linked to programme activity + cost code + shift + GPS/timestamped photo. *"links it to the programme activity and the cost code"*. /blog/ce-quotations-that-survive-pm-scrutiny |
| 14 | evidence_completeness | **3** | "Record Quality" tab; 87 avg shift score; 92.8 access score; 94% record compliance; "Documentation Required" lists. Homepage + /en/client |
| 15 | **recoverable_dollar_estimation** | **1** | **Explicitly not done.** *"Cost of extra materials, labour, and plant **to be calculated**."* The £21k cascade is a marketing mockup. /en/qs-ai-agent |
| 16 | claim_package_generation | **2** | Assembles substantiation + branded shift PDFs; does **not** generate the CE quotation. *"the substantiation is already assembled"*. /blog/ce-quotations-that-survive-pm-scrutiny |
| 17 | notice_drafting | **3** | Named output: *"Draft notices"*; MCP: *"generate draft notices"*. /en/qs-ai-agent |
| 18 | schedule_impact_analysis | **2** | Narrative time impact ("Potential 4-day delay to M&E final fix programme"), planned-v-actual; no TIA/windows analysis. |
| 19 | procore_integration | **2** | Claimed two-way Daily Log + document sync, but **zero Procore App Marketplace presence** (verified against full catalogue). |
| 20 | autodesk_integration | **2** | "Autodesk Construction Cloud — Direct Link, sync issues & photos"; BIM integration at Gatwick. /en/contractors |
| 21 | outlook_gmail_integration | **1** | Microsoft SSO + Copilot/365 add-in; no mailbox ingestion, no Gmail. /en/security |
| 22 | mobile_workflow | **3** | Offline-first in London Underground tunnels, voice-to-text, GPS+timestamp, iOS 10+/Android 7+. /customer-stories/kn-circet-tfl-4lm-gather |
| 23 | audit_trail | **3** | Timestamped, geotagged, "tamper-proof" metadata; ISO 27001 + Cyber Essentials Plus; contemporaneous by design. /en/security |
| 24 | portfolio_risk | **3** | Owner portfolio dashboards: Active Lots, Record Compliance %, Avg Quality Score, Risk Flags; drill from portfolio → shift in three clicks. /en/client |
| 25 | performance_pricing_compatibility | **1** | Flat £500 PCM, *"no add-ons, uplifts or banded costs"*, not per user. No value/contingency component despite publishing 10×–39× ROI. G-Cloud pricing doc |
| 26 | consultant_replacement_potential | **2** | *"senior QS review capacity without hiring more senior QSs"* — but *"Will this replace our QS team? No."* and Cubby still runs 10 QSs daily on the output. /en/qs-ai-agent |

`SCORES| 2,2,3,3,1,1,3,3,1,3,2,2,3,3,1,2,3,2,2,2,1,3,3,3,1,2`

## A11. Weaknesses and gaps — deliberate vs unattended

| Gap | Deliberate or unattended? | Why |
|---|---|---|
| **No quantum / CE pricing** | **DELIBERATE** | Two-sided positioning (*"We don't take sides"*) makes it impossible to price a CE for the contractor while selling assurance to the owner. Pricing the CE would make them a partisan tool and torch the Network Rail / TfL / owner-mandate channel. **This is a strategy-level refusal, like Document Crunch's.** |
| **No email / RFI / correspondence ingestion** | Unattended, but structurally hard | Their moat is *structured* records they generate. Ingesting unstructured email breaks the "one clean corpus" thesis. Still: this is where a large share of the entitlement evidence actually lives. |
| **No change-order/CE register** | **DELIBERATE** | They partner with CEMAR (their own Commercial Director's company) and Contract Bee rather than compete. Ben Walker will not cannibalise CEMAR. |
| **No US / AIA / ConsensusDocs** | Unattended — but unaffordable | 10 staff, £135k cash, £414k debt, UK-only data residency, UK-only certifications. Cannot fund a US entry. |
| **No Procore Marketplace listing** | Unattended | Free distribution they are not taking. Suggests engineering capacity constraint. |
| **Public API has no entitlement objects** | Deliberate for now | Keeps the intelligence layer proprietary; but also means partners can't build on it. |
| **Concentration in UK rail** | Structural | FY2025 accounts blame *"the end of Network Rail's control period"* for churn. Single-regulator revenue risk. |
| **Two of four listed leaders have resigned as directors** | Unattended risk signal | Woodrow (Mar 2025) and Clegg (Apr 2026) both off the board while still on the About page. |
| **Inconsistent scale claims** | Marketing hygiene | About page: *"£25bn+ project value, 4,500+ daily users, 10m+ records"*. Press page (via search index): *"£400 billion in projects"*. **16× discrepancy — treat both as `UNVERIFIED`.** |

## A12. Adjacency test — how hard for Gather to ship the full pipeline?

**Event detection → entitlement matching → evidence → recoverable-value estimate → claim package.**

**Rating: MEDIUM technically, HARD organisationally.**

- **Data access: EASY.** They already hold labour/plant/materials by shift, tied to programme
  activity and cost code. They are three-quarters of the way to a Defined-Cost build.
- **Technical: MEDIUM.** Clause 63.1 Defined Cost + Fee via the Schedule of Cost Components is
  formulaic. They know it — they wrote a 9-minute blog on how to do it by hand.
- **Org incentive: HARD.** The revenue proof they publish is owner-side and defence-side. Their
  biggest logos (Network Rail, TfL) are the *paying* party. Pricing CEs for contractors makes the
  product adversarial to half their book and destroys the *"you fund the licences for your supply
  chain"* motion that is their best distribution.
- **GTM: HARD.** £500/month flat pricing gives them no way to monetise a six-figure recovery.
  Repricing to value would break the G-Cloud framework listing.
- **Legal exposure appetite: MEDIUM.** They already draft notices, so they are past the first
  liability line. Quantum is a bigger step but not a new category.
- **Capacity: HARD.** 10 people, shrinking R&D spend, amortisation exceeding capitalisation.
- **Past shipping behaviour:** rebranded (2024), added the AI agent (2025), added MCP (2026),
  spun calculators *out* to a free site (2026). They ship steadily but small.

## A13. Startup posture toward Gather

**In the UK NEC4 market: ROADKILL. Do not fight them there.**
Eight years of records, Ben Walker's NEC4 authorship, an owner-mandate channel into Network Rail
and TfL, and £500/month pricing that no newcomer can undercut profitably.

**In the US: IRRELEVANT — and, more usefully, a free R&D report.**
They have proven, at their own expense, that (a) contract-aware event detection off daily records
works and gets bought, (b) the buyer is the commercial/QS function not the field, (c) owners will
mandate and fund the tool, and (d) **the quantum step is the one nobody has taken.**

**Potential PARTNER, narrowly.** If a US product ever needs a UK/NEC beachhead, or if Gather ever
needs quantum, there is a complementary fit. But at £2.5m post-money and 10 staff they are an
acqui-target, not a channel.

## A14. Top customer complaints — NONE OBTAINABLE

**I could not find a single independent customer review of Gather.**
- Not on the Procore App Marketplace (no listing at all).
- G2/Capterra: no "construction claims/NEC4" category; a GetApp "Gather" page exists but is a
  different product namespace collision.
- Every testimonial on the site is company-published, and one key testifier (Nick Mansell) is a
  shareholder.

**This is itself a finding:** a category with no independent review corpus. It cuts both ways —
no visible dissatisfaction, and no verifiable satisfaction either. **`UNVERIFIED` across the board.**

Closest thing to a complaint, from Gather's own FY2025 directors' report:
> *"we experienced a **high level of churn** partly connected to the end of projects and the end of
> Network Rail's control period."*

Second-closest, from the Cubby case study — the product still needs **10 QSs reviewing daily**.
And the /en/qs-ai-agent FAQ concedes the AI *"errs on the side of flagging opportunities for you
to assess rather than missing them entirely"* — i.e. **it generates false positives by design**,
and a human must triage them.

---

# PART B — TRANSFERABILITY: DOES THE NEC4 MECHANISM PORT TO US CONTRACTS?

## B1. Why NEC4 manufactures the workflow

The contract itself creates the product. Three properties, none of which A201 has:

**(1) The contract MANDATES the notice, on both parties.**
NEC4 ECC clause 15.1: *"The Contractor and the Project Manager give an early warning by notifying
the other **as soon as** either becomes aware of any matter which could [increase the total of the
Prices / delay Completion / delay meeting a Key Date / impair the performance of the works in use]."*
The Project Manager then enters it in the **Early Warning Register** (cl. 16) and an early warning
meeting follows. Notification is an *obligation of continuous performance*, not an option exercised
when you decide to claim.
(https://www.ceca.co.uk/wp-content/uploads/2022/09/CECA-NEC4-Bulletin-No.5-Early-Warnings-and-Liability-for-Not-Notifying-May-2021.pdf)

**(2) The contract NAMES the deadline AND states the forfeiture, in the same sentence.**
NEC4 clause 61.3, verbatim:
> *"If the Contractor does not notify a compensation event within **eight weeks** of becoming aware
> that the event has happened, **the Prices, the Completion Date or a Key Date are not changed**
> unless the event arises from the Project Manager or the Supervisor giving an instruction or
> notification, issuing a certificate or changing an earlier decision."*
(https://ramskillmartin.co.uk/technical/back-to-basics-nec-notices-and-time-bars-article-78)

Under English law this satisfies the **Bremer** test for a condition precedent —
*Bremer Handelgesellschaft mbH v Vanden Avenne Izegem nv* [1978] 2 Lloyd's Rep. 113 (HL): a notice
clause binds as a condition precedent if it **(i) states the precise time** for service **and
(ii) makes plain by express language that failure loses the right**. NEC4 61.3 does both. **A201
§15.1.3.1 does only (i).** That single structural difference is the whole transferability question.

Sub-contract equivalent is **seven** weeks, and the timescale is *"often shortened by way of
amendments to the standard form"* (Ramskill Martin) — some UK Z-clauses cut it to days.

**(3) The contract runs a full clock cascade with a duty on the assessor.**
- 61.1 — PM notifies the CE for PM/Supervisor-originated events and instructs a quotation at the
  same time (these are the events the 61.3 bar does *not* apply to: 60.1(1), (4), (7), (8), (10), (15), (17)).
- 61.4 — PM must decide within **one week** (or as extended) whether it is a CE; failure lets the
  Contractor notify and, after a further **two weeks** of silence, the PM's acceptance is **deemed**.
- 62.3 — Contractor submits the quotation within **three weeks**; PM replies within **two weeks**.
- 62.6 — **deemed acceptance** of the quotation if the PM stays silent two weeks after being chased.
- 63.1 — assessment is *"the effect of the compensation event on Defined Cost plus the Fee"*;
  actual Defined Cost for work done, forecast for work not done.
- 63.5 — risk allowance for cost and time where there is a significant chance of the risk occurring.
- 64.1 — **the PM makes their own assessment** if the Contractor fails to submit in time. As Gather
  put it: *"A PM assessment is rarely generous… it becomes the number unless you challenge it."*

**Net effect: NEC4 converts commercial diligence into a compliance obligation with a published
calendar and a named forfeiture.** That is why a UK product can sell "we watch the clock for you"
without ever having to argue the case for why the clock matters.

Contrast **Glen Water Ltd v Northern Ireland Water Ltd** [2017] NIQB 20, where a 21-day condition
precedent was enforced *despite* meetings, letters and repeated expressions of concern about the
very event: *"The contractual terms are clear and **commercial certainty is an overarching
consideration**. The evidence as to the commercial context and surrounding circumstances has not
remedied the defect in the letter."* **A UK court will kill a claim that the parties both knew about.
A US court usually will not.** Hold that thought.

## B2. FIDIC — a middle case, softened in 2017

FIDIC 2017 (Red/Yellow/Silver) **Sub-Clause 20.2.1**: a Notice of Claim must be given to the Engineer
**no later than 28 days after the claiming Party became aware, or should have become aware, of the
event or circumstance**. Miss it and *"the claiming Party is not entitled to its claim."*

But 2017 deliberately **tamed the time-bar beast** relative to 1999's Sub-Clause 20.1:
- **20.2.2** — if the Engineer considers the Notice late, the Engineer must say so **within 14 days**
  of receiving it; **if the Engineer fails to give that notice, the Notice of Claim is deemed valid.**
- **20.2.4** — a fully detailed claim within **84 days**; failure makes the Notice of Claim
  *"deemed to have lapsed"*, again subject to a 14-day Engineer notice, and again revived by
  Engineer silence.
- **20.2.5** — the Engineer (or DAAB) may **waive the time bar** having regard to any justification
  for late submission.
- **Sub-Clause 3.7** — the Engineer must **consult to agree, and failing agreement, make a fair
  determination** within defined periods.
(https://www.cmguide.com.au/the-fidic-2017-claims-mechanism-has-the-time-bar-beast-been-tamed/;
https://www.fenwickelliott.com/research-insight/newsletters/international-quarterly/changes-claim-provisions-2017-fidic-red-book)

**Mandatoriness: HIGH but reversible.** FIDIC 2017 keeps the calendar and the express forfeiture,
then builds in three escape hatches. Under civil-law seats the time bar is frequently attacked as
contrary to good faith (Fenwick Elliott, "Sub-Clause 20.1 – the FIDIC Time Bar under Common and
Civil Law"). **FIDIC is a strong second market for a Gather-shaped product, and Gather already
supports it.** It is not the US answer.

## B3. AIA A201-2017 — the calendar exists, the guillotine does not

From the official AIA sample text (https://assets.aiacontracts.com/ctrzdweb02/zdpdfs/preview_a201-2017.pdf):

| Provision | Text | Deadline |
|---|---|---|
| **§15.1.3.1** | *"Claims by either party under this Section 15.1.3.1 shall be initiated within **21 days** after occurrence of the event giving rise to such Claim or within 21 days after the claimant first recognizes the condition giving rise to the Claim, whichever is later."* | 21 days |
| **§15.1.3.2** | Claims discovered after the correction period: notice to the other party; **no IDM decision required**, and **no time limit stated**. | none |
| **§15.1.5** | Additional cost: *"notice as provided in Section 15.1.3 shall be given **before proceeding to execute** the portion of the Work that is the subject of the Claim."* | before the work |
| **§15.1.6.1** | Additional time: notice per 15.1.3; Claim *"shall include an estimate of cost and of probable effect of delay"*; *"In the case of a continuing delay, only one Claim is necessary."* | 21 days |
| **§15.1.6.2** | Weather: must be documented as abnormal, unforeseeable, and adverse. | — |
| **§3.7.4** | Concealed/unknown conditions: *"promptly provide notice… **before conditions are disturbed** and in no event later than **14 days** after first observance."* | 14 days |
| **§8.3.1–8.3.2** | Delay: Contract Time extended *"for such reasonable time as the **Architect** may determine"*; claims per Article 15. | — |
| **§7.3** | Construction Change Directive: Contractor must **proceed**; if no agreement on price, **§7.3.4 the Architect determines** the adjustment on reasonable expenditures/savings from an itemised accounting the Contractor must keep. | — |
| **§15.1.7** | **Mutual waiver of consequential damages** — including the Contractor's home-office overhead and lost profit on other work. | — |
| **§15.1.2** | Outer limit: all Claims and causes of action **within the applicable statute of limitations, and in any case not more than 10 years after Substantial Completion**. | 10 years |
| **§15.2.1** | An **Initial Decision** by the IDM is a **condition precedent to mediation** — but the deadline that is a condition precedent is the *decision*, not the *21-day notice*. | 30 days |

**The decisive absence: A201 nowhere says that failure to give the 21-day notice waives the Claim.**
Compare NEC4 61.3, which says exactly that, in the clause. A201's only express waiver language is
§15.1.2 (10-year backstop) and §15.1.7 (consequential damages).

**Real-world confirmation:** the owner-amended A201 I pulled from a US public-agency procurement
(Housing Opportunities Commission, Dec 2024) had **bolted the guillotine on by hand**:
> *"**Failure of Contractor to provide Initial Written Notice of claims as required by Section 7.1.1.1
> of these General Conditions constitutes a waiver of such claims against the Owner.**"*
and deleted §15.1.3.2 as "Intentionally Omitted."
(https://www.hocmc.org/wp-content/uploads/2024/12/Exhibit-F-AIA-A201-2017-General-Conditions.pdf)

**US owners amend A201 to add forfeiture precisely because the base form lacks it.** That amendment
is the market signal: where the guillotine exists in the US, someone had to negotiate it in.

## B4. THE KILLER QUESTION — is late notice actually fatal in the US?

**Answer: usually NOT, and the fear-based pitch is legally weaker in the US than under NEC4.
But the distribution is bimodal, not uniform — and the jurisdictions where it IS fatal are exactly
the jurisdictions worth selling into.**

### B4a. The federal boards read notice liberally

The governing authority is *Hoel-Steffen Constr. Co. v. United States*, 456 F.2d 760, 768
(Ct. Cl. 1972): notice provisions in contract-adjustment clauses
> *"should not be applied too technically and illiberally where the Government is quite aware of the
> operative facts."*

Applied consistently since. From the Cohen Seglias government-contracting database
(https://www.cohenseglias.com/contracting-database/differing-site-conditions-notice/):

| Decision | Holding |
|---|---|
| *Shumate Constructors, Inc.*, VABCA No. 2772, 90-3 BCA ¶ 22,946 | Contractor prevails without written notice where *"the government had either constructive or actual knowledge of the condition and was not prejudiced by the lack of a written notice."* |
| *S. Kane & Sons, Inc.*, VACAB 1254, 78-1 BCA ¶ 13,100 | Same rule. |
| *Leiden Corp.*, ASBCA No. 26136, 83-2 BCA ¶ 16,612 | Government **inspector's** knowledge on site is **imputed to the Contracting Officer**, excusing notice. |
| *Roy I. Strate*, ASBCA No. 19914, 78-1 BCA ¶ 13,128 | Same imputation. |
| *Sociometrics, Inc.*, ASBCA No. 51620, 00-1 BCA ¶ 30,620 | Same imputation. |
| *Parcoa, Inc.*, AGBCA No. 76-130, 77-2 BCA ¶ 12,658 | **"The burden to show prejudice is on the Government."** |
| *SIPCO Services & Marine v. US*, 41 Fed. Cl. 196, 224 (1998) | Substantial compliance: **"material prejudice"** required before a notice defect jeopardises the claim. |

The one clean federal loss on notice cited is *Eggers & Higgins v. United States*, 403 F.2d 225
(Ct. Cl. 1968) — where the claim came **nearly five years** after the required date, i.e. prejudice
was obvious.

**So: at federal level the clause text is hard, the application is soft, and the burden is on the
Government.** A US federal contractor who misses notice usually still gets paid.

### B4b. State courts split, and the split is real

**STRICT — notice is a condition precedent and late notice waives:**

| Case | Holding |
|---|---|
| *Brawner Builders, Inc. v. State Highway Admin.*, 258 A.3d 217, 232 (**Md.** 2021) | 30-day notice missed on a pass-through claim; **claim waived**. Notice is a condition precedent; strict compliance required. |
| *Mike M. Johnson, Inc. v. County of Spokane*, 78 P.3d 161 (**Wash.** 2003) | The leading harsh-enforcement case. Actual knowledge does **not** excuse. |
| *Absher Constr. Co. v. Kent School Dist. No. 415*, 890 P.2d 1071, 1073 (Wash. App. 1995) | *"Washington law requires contractors to follow contractual notice procedures, unless those procedures are waived."* 14-day written claim missed = no compensation. |
| *Commonwealth v. AMEC Civil, LLC*, 699 S.E.2d 499, 506–07 (**Va.** 2010) | **Actual notice insufficient**; written notice of intent to file a claim required at the time of occurrence. |
| *Huff Enterprises v. Triborough Bridge & Tunnel Auth.*, 595 N.Y.S.2d 178, 181 (**N.Y.** 1st Dep't 1993) | Allowing circumvention would *"eviscerate the viability of these clauses in public works projects."* |
| *Phoenix Signal & Elec. Corp. v. NYS Thruway Auth.*, 90 A.D.3d 1394 (N.Y. App. Div. 3d Dep't 2011) | NY courts harshly enforce notice provisions. |
| *Glynn v. City of Gloucester*, 487 N.E.2d 230, 235 (**Mass.** App. Ct. 1986) | Otherwise *"the contractual and statutory framework for the resolution of disputed claims would be virtually meaningless."* |
| *Westates Constr. Co. v. City of Cheyenne*, 775 P.2d 502, 504 (**Wyo.** 1989) | Failure to comply *"clearly and unambiguously deprives it of the right to compensation."* |
| *Starks Mechanical v. New Albany-Floyd Cty. Sch. Corp.*, 854 N.E.2d 936 (**Ind.** App. 2006) | RFIs and "potential claim" letters are **not** written notice. |
| *Cameo Homes v. Kraus-Anderson Constr.*, 394 F.3d 1084 (8th Cir. **Minn.** 2005) | Notice to the wrong party may preclude the claim. |

**LENIENT — actual notice / no prejudice / waiver / course of dealing excuse:**

| Case | Holding |
|---|---|
| *James Corp. v. N. Allegheny School Dist.*, 938 A.2d 474, 485–87 (**Pa.** Commw. 2007) | Notice defence **rejected** where the owner knew the underlying facts and suffered no prejudice; informal notice accepted; post-completion delay claims allowed on the owner's actual knowledge. |
| *James Constr. Grp. v. Westlake Chem. Corp.*, 650 S.W.3d 392, 406 (**Tex.** 2022) | *"A party's **minor deviations** from a contractual notice condition that **do not severely impair the purpose** underlying that condition and **cause no prejudice** do not and should not deprive that party of the benefit of its bargain."* **Caveat: if the contract requires writing, oral notice will not do — and Westlake lost its damages on exactly that point.** |
| *Del Lago Ventures v. QuikTrip Corp.*, 764 S.E.2d 595, 599 (**Ga.** App. 2014) | **Substantial compliance is the "general rule."** |
| *Okee Indus. v. National Grange Mut. Ins.*, 623 A.2d 483 (**Conn.** 1993) | A *"slightly imperfect letter of notice"* acceptable where the owner was not prejudiced. |
| *Vanderlinde Elec. Corp. v. City of Rochester*, 54 A.D.2d 155 (**N.Y.** 1976) | **Meeting minutes and monthly schedule updates accepted as written notice.** |
| *Charles T. Driscoll Masonry v. County of Ulster*, 40 A.D.3d 1289 (N.Y. 2007) | Parties' **course of conduct** can waive a written-notice requirement. |
| *Tupelo Redevelopment Agency v. Gray Corp.*, 972 So. 2d 495 (**Miss.** 2007) | A **"pattern of inconsistent conduct during the project"** waives enforcement. |
| *Welsh v. Gindele & Johnson*, 50 A.D.2d 971 (N.Y. 1975) | Owner **deemed to have waived** its right to enforce. |
| *Stone v. City of Arcola*, 536 N.E.2d 1329 (**Ill.** App. 1989) | Waiver where the owner told the contractor that giving notice would be **"useless."** |
| *New Pueblo Constructors v. State*, 696 P.2d 185 (**Ariz.** 1985) | Formal notice unnecessary where weather-driven claims are **obvious to the owner**. |
| *Blake Constr. v. C.J. Coakley Co.*, 431 A.2d 569 (**D.C.** 1981) | Construction requires **"rough, quick and ad hoc"** accommodation; affirmative conduct waives formalities. |

Sources: https://www.pecklaw.com/client_alerts/snooze-you-lose-enforcement-of-notice-and-timing-provisions/ ;
https://www.klconstructionlawblog.com/2014/10/20/enforcing-notice-provisions-in-construction-contracts-in-the-united-states/ ;
https://www.consensusdocs.org/news/snooze-you-lose-enforcement-of-notice-and-timing-provisions/

### B4c. Honest assessment of the distribution

| Regime | Does missing notice extinguish the claim? |
|---|---|
| **UK NEC4** | **YES — binary and total.** No proportionality, no prejudice test, no discretion. The clause states the forfeiture. |
| **FIDIC 2017** | **Usually yes**, but with three statutory escape hatches (Engineer's 14-day rebuttal duty, deemed validity on silence, express 20.2.5 waiver power) and a live civil-law good-faith challenge. |
| **US federal (FAR)** | **Rarely.** Clause text is hard; boards excuse on actual/constructive knowledge; **burden of proving prejudice is on the Government**. But there are hard *cost-truncation* rules — see B6. |
| **US private, unamended A201** | **Rarely.** No express forfeiture in the form. Outcome turns on state doctrine and on whether the owner was prejudiced. |
| **US private, amended A201 / negotiated forms** | **Often yes** — where the owner bolted in express waiver language, and in strict-compliance states. |
| **US state DOT** | **YES — and harder than NEC4.** See B6. |
| **US strict states (WA, MD, VA, NY, MA, WY, IN)** | **Often yes**, especially on public works. |
| **US lenient states (PA, GA, CT, MS, IL, AZ, DC; TX with a writing caveat)** | **Usually no** — claim weakened, negotiating position damaged, but survives. |

**Best estimate of the distribution for a typical US private commercial job on unamended A201:
late notice is *fatal* in perhaps 15–30% of cases, *materially damaging but survivable* in the
majority, and *irrelevant* where the owner plainly knew.** `UNVERIFIED — no published dataset
quantifies this; this is a synthesis of the case law split above, offered as a judgement, not a fact.`

**So the honest verdict on the killer question: YES, the fear-based pitch is weaker in the US.**
Selling "you will lose your entitlement if you miss the deadline" to a US private-work GC on
unamended AIA is, in most states, **overselling a legal proposition a construction lawyer will
correct in the room.** A US buyer's own counsel will say: *"we'd probably still get paid; we'd just
get beaten up on it."* Under NEC4 nobody says that, because nobody can.

## B5. So does the *lack* of a mandated workflow mean white space, or no demand?

**It means white space in the *category* and no demand for the *pitch*.** The pain is identical;
its expression is not.

The US pain is **cash-conversion**, not entitlement extinction:

- **77% of specialty contractors have had to write off change order work as bad debt.**
- **83%** say the change-order process negatively impacts cash flow.
- Average **22 days** internal processing + **26 days** GC approval; >50% take 8–14 days just to turn
  a signed T&M tag into a priced Change Order Request, and another 30% take 15–30 days.
  (Clearstory / Dodge Construction Network, *Optimizing the Change Order Process for Specialty Trade
  Contractors*, 2025 — https://www.clearstory.build/construction-blog/2025-specialty-contractor-change-order-report)
- **Average US construction dispute value $60.1m**, up **43%** since 2021; average North American
  dispute runs **12.5 months**. Globally the #1 cause is *"failure to properly administer the
  contract"*; in North America it is errors/omissions in contract documents.
  (Arcadis *Global Construction Disputes Report 2025*)

**Reframing the buying trigger for the US:**

| UK/NEC4 trigger | US equivalent trigger |
|---|---|
| *"You will lose entitlement at week 8."* | *"You wrote off $X last year because the tag never became a priced COR."* |
| *"The clause 61.3 clock is running."* | *"Your change orders are sitting 48 days unbilled. That is working capital."* |
| *"The PM will assess it under 64.1 and it will be low."* | *"When the GC asks for backup you can't produce it in 24 hours, so you settle at 70 cents."* |
| Fear of forfeiture | **Fear of the discount, the write-off, and the delay.** |

The Costain A12 case study already shows the mechanism working in the US idiom without any time
bar at all: *"All compensation events are now processed **within the same week** of application"*
and *"15% of claims rejected on the spot."* That is **speed and substantiation**, not forfeiture —
and speed and substantiation are exactly what the US market says it is bleeding on.

**Answer: MORE white space, but the wedge must be re-cut.** There is no incumbent habit, no
mandated register, no CEMAR — but there is also no automatic obligation to hang the sale on.
The founder must supply the *why now*, and the durable one is **cash, cycle time, and write-offs**,
with time-bar risk as a *secondary* argument reserved for the regimes where it's true.

## B6. WHICH US REGIMES DO HARD TIME-BAR — the beachhead

### (a) STATE DOT — the hardest notice regime in the developed world. **This is the beachhead.**

**Caltrans 2018 Standard Specifications** (verbatim, §5-1.42 and §5-1.43,
https://dot.ca.gov/-/media/dot-media/programs/design/documents/f00203402018stdspecs-a11y.pdf, pp. 58–60):

> **§5-1.43A General** — *"Failure to comply with this procedure is:
> 1. **Waiver of the potential claim and a waiver of the right to a corresponding claim for the
> disputed work in the administrative claim procedure**
> 2. **Bar to arbitration (Pub Cont Code § 10240.2)**"*

> **§5-1.42 Requests for Information** — *"Submit an RFI upon recognition of any event or question of
> fact arising under the Contract. The Engineer responds… within 5 business days. … You may protest
> the Engineer's response by: 1. Submitting an **Initial Potential Claim Record form within 5
> business days** after receiving the Engineer's response."*

> **§5-1.43B Initial PCR** — *"within **5 business days** of the Engineer's response to the RFI or
> within 5 business days from the date when a dispute arises… The nature and circumstances **must
> remain consistent**."*

> **§5-1.43C Supplemental PCR** — *"**Within 15 days** of submitting the Initial Potential Claim
> Record form, submit a Supplemental Potential Claim Record form including: 1. Complete nature and
> circumstances… 2. Contract specifications supporting the basis of a claim 3. **Estimated claim cost
> and an itemized breakdown of the individual costs stating how the estimate was determined** 4. **TIA**"*

> **§5-1.43D Full and Final PCR** — notify within **10 days** of the completion date of the claimed
> work; submit within **30 days** of completion, with itemised labour (individuals, classifications,
> regular/OT hours, dates), materials (invoices, POs, locations, dates), equipment (make, model,
> serial, hours, dates, rate book) and a **TIA**. *"The Department does not consider a Full and Final
> Potential Claim Record form that does not have the same nature, circumstances, and basis of claim
> as those specified on the Initial… and Supplemental…"*

**Read what this actually demands.** Caltrans requires, on a **5-business-day / 15-day / 30-day**
cascade, exactly the pipeline in the core hypothesis — event detection, entitlement matching,
contemporaneous evidence, **AND a costed, itemised recoverable-value estimate with a Time Impact
Analysis**. It is **shorter than NEC4's eight weeks**, the forfeiture is **express and statutory**
(Cal. Pub. Cont. Code § 10240.2 bars arbitration), and it **requires the quantum step Gather refuses
to build**. There is no actual-notice escape hatch drafted into the spec.

Sister regimes confirming the pattern:
- **VDOT** runs a formal **Notice of Intent to File Claim (NOI)** process with its own manual, last
  revised 2 June 2025 (https://www.vdot.virginia.gov/doing-business/technical-guidance-and-support/technical-guidance-documents/construction-and-maintenance-claims-and-notice-of-intent-to-file-claim-noi/) —
  and Virginia's Supreme Court has held in *AMEC Civil* that **actual notice is not enough**.
- **FDOT** §5-12.2 requires a written notice of intent to claim and its Construction Project
  Administration Manual §7.5 instructs the Project Administrator that *"the Department **shall
  enforce** the written notice requirement"* and that verbal indications must be converted to writing
  *"to preserve the claim for consideration by the Department"*
  (https://fdotwww.blob.core.windows.net/sitefinity/docs/default-source/construction/manuals/cpam/newcleanchapters/chapter7s5.pdf).

**Every US state DOT has its own spec book with its own clock.** That is 50 variants — a cost for a
solo founder, but also a **moat and a defensible content asset**, exactly the asset Gather built for
NEC4 with its `/en/nec4/*` estate.

### (b) US FEDERAL (FAR) — hard *cost-truncation* rules, softly applied

From eCFR (https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/):

| Clause | Verbatim rule |
|---|---|
| **52.243-4 Changes (d)** | *"no adjustment for any change under paragraph (b) of this clause shall be made **for any costs incurred more than 20 days before** the Contractor gives written notice as required."* |
| **52.243-4 (e)** | *"The Contractor **must assert its right to an adjustment** under this clause **within 30 days**…"* |
| **52.243-4 (f)** | *"No proposal by the Contractor for an equitable adjustment shall be allowed if asserted **after final payment**."* |
| **52.236-2 Differing Site Conditions (a),(c)** | Notice *"**promptly, and before the conditions are disturbed**"*; *"**No request** by the Contractor for an equitable adjustment to the contract under this clause **shall be allowed, unless** the Contractor has given the written notice required; **provided**, that the time prescribed… **may be extended by the Contracting Officer**."* |
| **52.242-14 Suspension of Work (c)** | *"A claim under this clause shall not be allowed (1) **for any costs incurred more than 20 days before** the Contractor shall have notified the Contracting Officer in writing…"* |
| **52.242-17 Government Delay of Work (b)** | Same 20-day cost cut-off. |

**Note the shape: this is not extinction, it is a rolling truncation.** Every day of silence deletes
a day of recoverable cost. That is *more* naturally SaaS-shaped than a cliff — it converts to
"each day you don't notice costs you money" and it is arithmetically demonstrable from a daily
report. And the outer boundary is the **Contract Disputes Act six-year limitation**
(41 U.S.C. § 7103(a)(4)(A)) plus final payment.

**Caveat that must be stated to any buyer honestly:** the boards apply *Hoel-Steffen* and put the
prejudice burden on the Government (§B4a). So the federal pitch is *"protect your cost recovery
window and your REA quality"*, not *"you'll lose everything."*

### (c) HEAVILY NEGOTIATED PRIVATE FORMS

Where a US owner has amended A201 to add express waiver language — as the HOC document above does —
the NEC4 logic applies verbatim. This is common on data centres, semiconductor fabs, pharma, and
large developer programmes: exactly the sectors currently spending most. Note **Dornan/Turner's**
work in semiconductor and biotech fabs — the same segment.

### (d) THE ANSWER TO "WHICH REGIME IS THE BEACHHEAD"

**Ranked by (time-bar hardness × quantum requirement × record availability × addressability by a solo founder):**

1. **State DOT heavy-civil subcontractors and mid-size primes** — hardest bar, mandatory quantum at
   day 20, daily reports already exist and are already required, single spec book per state, dense
   trade press, and a buyer who has *already lost claims this way*. **Start with one state.**
2. **Federal construction (FAR-based) primes and subs** — 20-day rolling cost truncation, REA
   discipline, existing daily-report culture, but a longer sales cycle and FedRAMP/StateRAMP friction.
3. **Amended-A201 private megaprojects (data centre / fab / pharma)** — the guillotine exists where
   the owner negotiated it; highest dollar value; hardest to reach as a solo founder.
4. **Unamended A201 private commercial** — **do NOT lead here with time-bar fear.** Lead with
   cash-conversion, write-off avoidance, and same-week substantiation.

---

# B7. THE FOUR KEY QUESTIONS, ANSWERED DIRECTLY

**1. Is Gather a thesis-proof or a thesis-killer for the US market?**
**Thesis-proof for the mechanism, thesis-killer for the lazy version.**
Proof: contract-aware event detection off daily site records is a real, sellable product with Tier 1
logos, and the buyer is the commercial/QS function. Killer: at £500/month, 10 staff, £713k lifetime
equity, ~£100k annual losses, no quantum, no independent reviews, and headline ROI numbers that on
inspection are admin savings and owner-side claim rejections. **Nobody has yet proven that a
contractor will pay a premium for recovered entitlement — including Gather.** They are not a
competitive threat in the US. They are a free, eight-year, publicly-audited feasibility study.

**2. Does the NEC4 mechanism port to US AIA contracts, or is the workflow contract-form-dependent?**
**It is contract-form-dependent — and A201 is the wrong form.** NEC4 61.3 satisfies both limbs of the
*Bremer* condition-precedent test: it names the time **and** states the forfeiture in the same
sentence. A201 §15.1.3.1 names 21 days and stops. There is no express waiver clause in A201 for late
notice, US courts split roughly half-and-half on excusing it, the federal boards excuse it as a
matter of course, and §15.1.3.2 imposes **no time limit at all** for post-correction-period claims.
**The workflow ports; the coercion does not.**

**3. If US notice is routinely excused, what replaces "you'll lose your claim" as the buying trigger?**
Three, in order of proven willingness to pay:
- **(a) Working capital / write-off.** 77% have written off change-order work as bad debt; 83% say it
  hurts cash flow; 22 + 26 days of approval lag. *"You wrote off $2.1m last year"* is a CFO sentence,
  not a lawyer sentence, and it is verifiable from the customer's own ledger.
- **(b) Speed and settlement rate.** Costain A12 proves the mechanism: same-week processing, 15%
  rejected on the spot. Substantiation delivered *with* the request converts at a higher rate and a
  lower discount. Gather's own worked example quantifies the discount at ~8% of the CE value
  (£48k asked → £31k assessed → £44k settled).
- **(c) The regimes where the bar IS real.** Caltrans 5 business days; FAR's 20-day cost truncation;
  amended-A201 waiver clauses. Here — and *only* here — the NEC pitch survives translation intact.
- Do **not** lead with dispute-avoidance. Arcadis has US disputes at **$60.1m average, 12.5 months**,
  which is a scary number that describes something the buyer believes will happen to someone else.

**4. Which US contract regime is the beachhead where notice IS hard-enforced?**
**State DOT heavy civil, starting with a single state, most likely California.** Caltrans §5-1.43
imposes a **5-business-day** Initial Potential Claim Record, a **15-day** Supplemental PCR that
requires an **itemised cost estimate and a Time Impact Analysis**, a **30-day** Full and Final PCR,
express **waiver of the claim** and a statutory **bar to arbitration** under Pub. Cont. Code § 10240.2.
That is a shorter, harder, more quantum-hungry version of NEC4 61.3 — and it is the one place in the
United States where "you will lose it" is literally true and the buyer already knows it.
Second: federal FAR work (20-day rolling cost cut-off). Third: amended-A201 megaprojects.

---

# HARDEST FACTS (the five strongest numeric facts, all primary-sourced)

1. **Gather Insights Ltd employed an average of 10 people in FY2026, down from 14 in FY2025 and
   FY2024; net assets £537,435; cash £134,699; loss for the year £93,424.**
   https://find-and-update.company-information.service.gov.uk/company/10215108/filing-history
   (AA filed 10 Jun 2026, balance sheet + note 3)
2. **Gather's entire lifetime equity is ≈ £713,163** (share premium £712,919 + capital £244);
   the July 2024 "investment round" was **≈ £357,647 for 348 shares (~£1,027.72/share, ≈ £2.5m
   post-money)**, derived from share premium moving £355,307 → £712,919. Angel investors only.
   Same source, AA to 31 Mar 2025 and 31 Mar 2026.
3. **Published price: £500 a licence a month, enterprise SaaS, "not priced per User", setup ≈ 2×
   monthly, training £1,400/£450.** Data residency **UK/EEA only**.
   https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/719502/250831346049155-pricing-document-2024-02-28-0942.pdf
   and https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/250831346049155
4. **Caltrans requires an Initial Potential Claim Record within 5 business days and a Supplemental
   PCR with an itemised cost estimate and Time Impact Analysis within 15 days; failure is
   "Waiver of the potential claim… [and] Bar to arbitration (Pub Cont Code § 10240.2)."**
   https://dot.ca.gov/-/media/dot-media/programs/design/documents/f00203402018stdspecs-a11y.pdf §§5-1.42–5-1.43D
5. **FAR 52.243-4(d) and 52.242-14(c): no adjustment/claim allowed "for any costs incurred more than
   20 days before" the Contractor gives written notice; 52.236-2(c): "No request… shall be allowed,
   unless the Contractor has given the written notice required."** Meanwhile *Hoel-Steffen*, 456 F.2d
   760, 768 (Ct. Cl. 1972): notice *"should not be applied too technically and illiberally where the
   Government is quite aware of the operative facts"*, and the burden to show prejudice is on the
   Government (*Parcoa*, AGBCA 76-130).
   https://www.ecfr.gov/current/title-48/chapter-1/subchapter-H/part-52/subpart-52.2/section-52.243-4

**Bonus (the one that reframes everything):**
**Network Rail's "£300,000+ saved" is the client cutting back the contractor's change requests, and
Costain's headline is "15% of claims rejected on the spot."**
https://www.gatherinsights.com/customer-stories/network-rail-murphy-birmingham-new-street ;
https://www.gatherinsights.com/customer-stories/costain-a12-upgrade-gather

---

# UNKNOWNS — and what would settle each

| Unknown | What would settle it |
|---|---|
| **Gather's turnover and ARR.** Small-companies exemption means no P&L is filed. | Full accounts (only if they exceed the small-company thresholds); a Crunchbase/PitchBook-verified figure; or a Beauhurst/Companies House Streaming API record of a funding round with stated raise. |
| **Whether "£25bn+" or "£400bn" of project value is correct** (16× discrepancy between the About page and the press page). | A dated press release or a named-customer contract register. Both currently `UNVERIFIED`. |
| **Actual customer count and net retention.** FY2025 admits "high level of churn." | Deferred income disclosure (only the combined accruals line is filed) or a Crown Commercial Service G-Cloud spend report by supplier. |
| **Whether the QS AI Agent is a shipping product or a design-partner beta.** No release notes, no changelog, no status-page incident history reviewed, no customer names attached to the AI specifically. | An AI-specific case study with a named customer, or a G-Cloud 15 service definition naming the agent. |
| **The real Procore integration scope and permissions.** They claim two-way sync but have no marketplace listing. | A Procore Developer Portal app record, or an OAuth consent screen screenshot from a customer tenant. |
| **Whether Paul Clegg and Nick Woodrow remain employees after leaving the board.** | LinkedIn profile checks; the FY2027 directors' report. |
| **Quantified US distribution of outcomes on late notice.** I found no dataset; only a case-law split. | An empirical study of AAA/ICC construction awards or ASBCA/CBCA dockets coded for notice defences — this does not appear to exist publicly and would itself be a defensible proprietary asset. |
| **Whether US contractors will pay a premium tied to recovered dollars.** Nobody in this program has evidenced it — Gather included, at £500/month flat. | A live pricing test: offer a US state-DOT sub a fixed fee vs a success fee on recovered COs and see which they sign. |
