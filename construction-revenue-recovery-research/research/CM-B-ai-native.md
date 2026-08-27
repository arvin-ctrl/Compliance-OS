# CM-B — AI-NATIVE & POINT SOLUTIONS
## Category synthesis: who occupies the thesis pipeline, at what price, and where the floor falls out

**Category manager:** B · **Date:** 19 August 2026
**Sources synthesised:** raw/05 (Document Crunch), 06 (Trunk Tools), 07 (Clearstory), 12 (AI-native claims startups), 13 (schedule/delay analytics), 14 (legaltech/CLM), 16 (Gather & NEC transferability), 17 (non-English markets), plus SCORES.csv and NOTES-running.md.
**Additional live verification this pass (19 Aug 2026):** magra.app, magra.app/platform, lexilio.co/pricing, claimmaster.ai, delayclaimbuilder.com, trunktools.com/resources/contracts, gatherinsights.com/en/qs-ai-agent, alloovium.com — plus targeted research on Eichleay prerequisites, measured-mile methodology, and Procore AI credit pricing.

---

# 0. THE FOUR HEADLINES

1. **The pipeline is occupied at both ends and hollow in the middle-back.** Stages (a) contract ingestion, (b) clause extraction and (i) notice drafting are saturated *and free or near-free*. Stages (g) causation and (h) quantum have **no product in any language**. Stage (f) evidence sufficiency has two products, both scoring the wrong thing.
2. **Quantum is genuinely empty — CONFIRMED — but not for the reason anyone assumed.** It is not too hard (a one-man German firm ships court-grade quantum as a single offline HTML file). It is not unvalued (consultants charge $240k–$660k a matter for it; Caltrans *compels* it on a 20-day clock; 66% of GCs say disputed pricing is the #1 reason they short-pay). It is empty because **the law only supplies a computable cost method in one country, and everyone who could build it either sells to both sides or sells hours.**
3. **Exactly one vendor on earth has verified paying customers for a quantum artefact — Easyclaim, Germany, €599/case, no AI, no ingest, one person.** Exactly one has verified paying customers for entitlement-event detection — Gather, UK, £500/month — and its published outcomes are claims *defence* and admin savings, not recovery. Everything else in the AI-native claims cohort is product surface without a customer.
4. **Magra is demoware and the evidence is now arithmetic.** Its headline recovery figure has moved from **"$240K average value recovered per event"** to **"$17,824 avg. recoverable per event"** — a 13.5× revision — and the methodology is now disclosed as *"Estimates based on industry data: recoverable events at 5–10% of project value... from ASCE research on construction change orders."* That is a model output, not a measurement. All eight integrations remain **"Upcoming"** as of today.

---

# 1. THE PIPELINE OCCUPANCY MAP

**Legend for "how well":** ●●● strong, marketed and evidenced · ●●○ partial or single-source or heavy caveat · ●○○ marginal/adjacent · ○○○ absent
**Legend for evidence:** **[P]** proven with named customers · **[S]** shipping, customers unverified · **[C]** claimed only, no shipped data path

| Stage | Who occupies it | How well | Price today |
|---|---|---|---|
| **(a) Contract ingestion** | **Trunk Tools** free tool (AIA/ConsensusDocs/custom to 100MB, no account) **[P]**<br>**Document Crunch/Trimble** — contracts, specs, addenda, flow-downs, drawings, insurance, geotech, RFPs **[P]** ●●●<br>**Procore Contract Review agent** (GA 21 May 2026) **[S]**<br>Lexilio **[S]**, Magra **[C]**, Contradic **[S]**, ContraVault **[S]**, Ronayz **[C]**<br>Horizontal: DocuSign IAM, M365 Copilot, Icertis, Luminance **[P]**<br>*Not* Gather (declares contract *type* at setup, ●●○); *not* Easyclaim (takes numbers, ●○○) | ●●● | **$0** (Trunk Tools free tool)<br>$18–30/user/mo (M365 Copilot)<br>$45–80/user/mo (DocuSign IAM, incl. AI extraction)<br>$29–1,999/mo (Lexilio)<br>bundled credits (Procore)<br>undisclosed, project-volume-scaled (Doc Crunch) |
| **(b) Clause / entitlement rule extraction** | **Document Crunch Playbooks** — the market's strongest notice-requirement extraction ("Notices – when, where and how to send them", CO procedures, markup limits, backup requirements), **6,000+ projects** **[P]** ●●●<br>**Trunk Tools free tool** — 14 categories incl. *Notice Deadlines & Methods, Change Order Procedures, Delay & LDs, Dispute Resolution* → *"compliance calendar, critical deadline matrix, delegation chart by role"* **[P]**<br>Lexilio ("847 clauses in <2 min") **[S]**, Contradic **[S]**, ContraVault **[S]**, Magra **[C]**<br>Gather ●●○ (clause *library* for NEC3/4/JCT/FIDIC, not extraction from your PDF)<br>BauAgent ●○○ (statutory VOB/B §§, not your contract)<br>Horizontal CLM ●●● but **zero construction standard forms anywhere** | ●●● | **$0–$30/user/mo.** Free (Trunk Tools); $18–30 (Copilot, 75.1% extraction accuracy vs 71.1% lawyer baseline); $45–80 (DocuSign); $88k median ACV (Icertis, wrong buyer) |
| **(c) Commercial event detection from project records** | **Gather** ●●● **[P]** — but **single-source**: its own site diary only. 10M+ records; "40% more change events than manual review" (baseline unsourced)<br>**Procore Change Analysis agent** (GA 23 Jul 2026) ●●● **[S]** — *"identifies scope impacts, cost exposure, schedule risk and required follow-up actions"* from changes, RFIs, drawings, specs, project records; **Triggers** fire on new RFI/submittal/CO<br>**Trunk Tools TrunkReview** ●●○ **[P]** — finds clouded *and non-clouded* drawing changes; the ~$60k unclouded-electrical anecdote is literally an entitlement trigger<br>**Contradic (FR)** ●●○ **[S]** — detects *"événements clés, retards, changements de périmètre"* across contracts, emails, minutes, schedules<br>**Clearstory Change Notification Agent** ●●○ (open beta) — identifies impacted trades + cost exposure from a design change<br>Autodesk Build RFI AI ●●○ — auto-populates Cost Impact + Schedule Impact from free text<br>BauAgent ●●○ (human initiates via WhatsApp); Alloovium ●●○ (ingests email/calls to sentence level, no entitlement object)<br>**Magra Radar** ●●● **[C] — zero shipped integrations**<br>**Document Crunch: ○○○** (Procore app declares `permissions: {"company":{},"project":{}}` — it reads nothing) | ●●○ | **£500/mo flat** (Gather, unlimited users, UK/EEA only)<br>**Credits** (Procore — bundled starter pool, Control Tower metering)<br>**$0** in beta (Clearstory)<br>**€199–349/user/mo** (Contradic)<br>**Undisclosed** (Trunk Tools; Gilbane "seven-figure" / 200+ projects / 2 yrs ⇒ ~$2.5–7.5k/project/yr) |
| **(d) Entitlement matching** | **Gather** ●●● **[P]** — clause 60.1 categories + evaluation method (63.1 Defined Cost + Fee) + "Documentation Required" list. **NEC/JCT/FIDIC only**<br>**BauAgent** ●●○ **[S]** — classifies a site message into §2 / §4 / §6 VOB/B. Closed beta<br>**Magra** ●●● **[C]** — AIA A201 §15.1.3<br>Lexilio ●●○, Aven-AI ●●○ ("advisory only"), ContraVault ●●○<br>**Document Crunch: HALF** — the rule-set exists on 6,000+ projects; nothing matches it to a real event<br>**Datagrid/Procore: EXPLICIT REFUSAL** — *"entitlement and approval stay with the responsible project professionals"*<br>**Clearstory: 0 by published doctrine** — *"A T&M Tag only proves the work happened... You still need to submit a formal Change Order Request"* | ●●○ | **£500/mo** (Gather) · **€199–349/user/mo** (Contradic) · **$299–$1,999/mo** (Lexilio) · unpriced beta (BauAgent)<br>Under NEC administration: **£25–£584/user/mo** (Sypro → Unifier), **£435/licence/mo** (CEMAR, £75bn of works) — but these administer events *a human already identified* |
| **(e) Evidence collection / linking** | **Gather** ●●● **[P]** — records tied to programme activity + cost code + shift + GPS/timestamp; *"links it to the programme activity and the cost code"*<br>**Clearstory** ●●● **[P]** — **$2.1B/month** of two-sided, signed, timestamped, photo-backed COR/T&M evidence across **14,000+ contractors**; best contemporaneous extra-work record in US commercial construction<br>**Contradic** ●●● **[S]** — strongest cross-document chronology claim in any language<br>**Trunk Tools Cortex** ●●○ — 2M+ labelled artifacts, doc↔object↔spec↔schedule graph, but a *design/scope* graph not a dated event chronology; own roadmap: *"How might a bulletin relate to a change order request?... an area we continue to work on"*<br>ContraVault ●●○ (Claim Timeline + Evidence Trail); Aconex = warehouse, **structurally never a graph** ("no super user")<br>**Autodesk Data Connector** — hands the whole evidence graph out as scheduled CSV **including relationship edges ("RFIs that relate to PCOs")** | ●●○ | **$0** — Clearstory Basic (5 tags + 5 CORs/mo, unlimited projects); invited counterparties free<br>**$0** — Autodesk Data Connector CSV export<br>**£500/mo** (Gather) · **€199–349/user/mo** (Contradic)<br>Clearstory Standard/Pro: per-user fee **+** per-project platform fee, undisclosed |
| **(f) Evidence sufficiency assessment** | **ClaimMaster.ai Defensibility Score** ●●○ **[S]** — rates a claim across *causation, entitlement, substantiation, mitigation*. Solo founder (RICS Expert Witness cert, forensic quantum background). **No named customers**<br>**Gather "Record Quality"** ●●● **[P]** — 87 avg shift score, 92.8 access score, 94% record compliance, "Documentation Required" lists. **But scores hygiene against Gather's own diary schema, not against what a tribunal needs**<br>**Clearstory COR Review Agent** ●●○ (**closed beta**) — *"confirms backup documentation"* — **against company standards, not contract requirements**<br>CALIM free "Claim Readiness Score" (consultancy lead-gen)<br>Document Crunch ●○○ (template placeholder for "backup requirements"); Trunk Tools ●○○ (completeness vs *specs* only); everyone else 0–1 | ●○○ | **£39–£99/mo**, whitelabel **from £1,299/mo** (ClaimMaster.ai)<br>**Included** in £500/mo (Gather)<br>**$0** (CALIM lead-gen calculator)<br>**Nobody sells tribunal-standard sufficiency at any price** |
| **(g) Causation / attribution** | **NOBODY.** Category-wide ceiling is a hard 1/3.<br>**Steelray states it outright: *"The tool does not attribute responsibility to parties... leaves interpretation of causation and fault to the analyst or expert witness."***<br>SmartPM markets "defensible basis for delay claims" while its own docs say the framework *"focuses on quantifying schedule variance rather than assigning causation"*<br>Nodes & Links: activity-code filtering **within your own supply chain only**<br>Germany: BGH-mandated *bauablaufbezogene Darstellung* still executed **by professors, by hand, in MS Project and Excel**<br>**Standards-blocked:** AACE RP 29R-03 §1.2(f) — *"Schedules... do not demonstrate root causation or responsibility for delays"*; §1.3(c) scopes the discipline to quantification *"as opposed to assignment of delay responsibility"*; §1.1 exists to *"minimize the need to contend with 'black-box' or 'voodoo' analyses"* | ○○○ | **The arithmetic** (windows/half-step, which is *not* causation): **$2,750 perpetual** (Ron Winter) / **$3,990/user/yr** (Steelray) / **$12,000–$25,000/yr** (SmartPM)<br>**The opinion:** **$225–$1,375/hr** (Exponent card); FTI FLC realised **$442/hr**<br>**No product at any price** |
| **(h) Recoverable-dollar quantification** | **Easyclaim (DE)** ●●● **[P] — the only one on earth.** Reverse-engineers the bid, 26 cost categories, standstill/operating split, markup→daily-rate conversion, dual method (combined-markup **and Opitz**), 21-page court-ready derivation under §642 BGB / §6(6) VOB/B / §2(3) VOB/B. **No AI. No ingest. Single offline HTML file. One person.** Named customers: Beethovenhalle Bonn, OLG Stuttgart, Zoo Leipzig, Zoo Gelsenkirchen, Flughafen Paderborn<br>**Clearstory COR Pricing Agent** ●●○ — prices **known** work off a rate library. That is *pricing*, not quantum<br>**Magra** ●●● **[C]** — Eichleay, measured mile, extended GCs, escalation, lost productivity. Zero customers, zero integrations, headline number restated 13.5× downward<br>**Lexilio Enterprise** ●●○ — "Predictive claim exposure engine", *"weighted range $200k–$473k"*. Exposure ≠ quantum. $1,999/mo tier only<br>**Delay Claim Builder** ●●○ — writes a *"prolongation costs"* narrative **section**; the site does not claim it computes the number<br>**ClaimMaster.ai: explicitly refuses** — *"The platform does not estimate dollar or quantum recovery"*<br>**Gather: 1** — *"Cost of extra materials, labour, and plant **to be calculated**"* (re-verified today, unchanged)<br>**0 across the board:** Contradic, SmartClaim, BauAgent, ContraVault, Ronayz, Document Crunch, SmartPM, Icertis(1), Luminance, Copilot | ○○○ **(one non-AI exception)** | **€599 net per case** (Easyclaim, done-for-you) — *the only per-claim price in the world for a quantum artefact*<br>**$240k–$660k per $5–25m matter** (consultants: 600–1,650 hrs, of which 200–600 hrs is the automatable document/chronology work). Anchor: **£750,000** spent on Knowles by one employer (*Walter Lilly v Mackay*)<br>**No AI product at any price, in any language** |
| **(i) Notice drafting** | **Document Crunch Notice Builder** ●●● **[P]** — GA 21 Oct 2024; **agentic since 9 Jun 2026**. But every input is typed by a human, and for the deadline the user must *"use your playbook or chat to find your submission instructions"*<br>**Gather** ●●● **[P]** — drafts clause-cited notices with confidence scores<br>**BauAgent** ●●● **[S]** — three statutory VOB/B notice types, PDF on letterhead, **30 seconds**<br>Lexilio ●●●, Magra ●●● **[C]**, ContraVault ●●○, Ronayz ●●○, Delay Claim Builder ●●●<br>**Procore** ships 24 correspondence templates incl. Early Warning Notice / Notice of Delay / Extension of Time<br>**M365 Copilot ●●○** — *"genuinely good at drafting a notice letter from contract text — this is table stakes now"* | ●●● | **$18–30/user/mo** (Copilot — the real floor)<br>Bundled (Document Crunch, Procore)<br>From **$299/mo** (Lexilio Professional) · **£500/mo** (Gather) |
| **(j) Claim package generation** | **Easyclaim** ●●● **[P]** — the 21-page pack: cover, ToC, cost breakdown by category and working day, methodology with legal citation, full traceable arithmetic with consistent rounding<br>**Delay Claim Builder** ●●● **[S]** — 9-section EOT narrative → Word; TIA/Windows/APvAB/IAP/Collapsed As-Built; FIDIC 2017/NEC4/JCT/AS4000<br>**Contradic** ●●● **[S]** — one energy client cut dossier build from **3 weeks to 5 days**<br>Magra ●●● **[C]** ("$2.3M delay claim package in 48 hours"); ContraVault ●●○ (first-draft EOT/variation replies with citation trails)<br>**Gather ●●○** — assembles the substantiation, does **not** generate the CE quotation<br>**Document Crunch: 0** — generated-artifact list is exhaustive and closed (redlines, submittals, notices, RFIs, submittal logs, risk registers)<br>Schedule-analytics category: **exhibits, not packages** | ●●○ | **€599/case** (Easyclaim) · **$299/mo** (Delay Claim Builder) · **€199–349/user/mo** (Contradic)<br>Consultant equivalent: **$240k–$660k/matter** |

### The single-sentence read of the table
**Every stage is occupied by someone, but no one occupies (c)→(h) together, and the two stages nobody occupies at all — causation and quantum — are exactly the two the consultants charge $240k–$660k a matter to perform by hand.**

---

# 2. THE COMMODITISATION FRONTIER

## 2.1 What is already free or near-free

| Stage | Price floor | Who set it, and why |
|---|---|---|
| (a) Contract ingestion | **$0** | Trunk Tools ships a free, no-account, 100MB AI contract review tool as lead-gen — from a company at a reported **$325M valuation**. Its stated logic: *"AI can handle many tasks for construction teams. Some should be free."* This is **strategically hostile pricing**, deliberately aimed at devaluing point solutions. |
| (b) Clause / rule extraction | **$0 → $30/user/mo** | Same free tool returns *"a compliance calendar, critical deadline matrix, delegation chart by role, and warning flags for high-risk provisions"* across 14 categories. Procore shipped a native Contract Review agent 21 May 2026. M365 Copilot at $18–30/user/mo already answers "what are my notice deadlines" — at **75.1% best-AI extraction accuracy vs a 71.1% lawyer baseline** and **94.8% document Q&A vs 70.1%**. |
| (i) Notice drafting | **$18–30/user/mo** | Copilot drafts a serviceable notice from contract text. Document Crunch bundles Notice Builder. Procore ships the templates. |
| (e) Evidence capture (extra-work subset) | **$0** | Clearstory Basic is free for all stakeholders (5 tags + 5 CORs/month, unlimited projects, mobile app, Bulk AI import), and **invited counterparties get paid features free** — a deliberate viral give-away. Autodesk Data Connector exports the evidence graph, relationship edges included, as free scheduled CSV. |
| Delay quantification arithmetic | **$2,750 once** | Ron Winter's Schedule Analyzer eForensic, perpetual single-user, implementing the same AACE half-step SmartPM sells at $25,000/yr. nPlan gives schedule-integrity checking away free. |

**Consequence, stated bluntly: any wedge whose core value is reading a contract, listing deadlines, or drafting a notice is dead on arrival.** Three independent parties — Procore (native), Autodesk (Pype + Forma), Trunk Tools (free) — will price it at zero, and Microsoft prices it at $18/seat.

## 2.2 What is priced, and where the step-change happens

The non-English data gives the cleanest price ladder in the whole program, and it is corroborated by the NEC market on a different continent under a different contract form:

```
$0            Trunk Tools contract tool, Clearstory Basic, Autodesk Data Connector
$18–30/user   M365 Copilot                    — reading + drafting
$45–80/user   DocuSign IAM                    — repository + AI extraction
€15/user      Contracktime (FR)               — evidence capture, no AI, no entitlement
€39/user      Capmo (DE)                      — logging + AI search
────────────────── the 13× step ──────────────────
€199/user     Contradic Team (FR)             — event detection + evidence graph + claim drafting
$299/mo       Lexilio Professional            — notice tracker + notice generation
€349/user     Contradic Enterprise
£435/licence  CEMAR (UK NEC)                  — register + clock, £75bn of works administered
£500/licence  Gather (UK)                     — detection + clause map + notice, unlimited users
$1,999/mo     Lexilio Enterprise              — + "predictive claim exposure engine"
────────────── per-artefact pricing ──────────────
€599/CASE     Easyclaim (DE)                  — quantum + court-ready package
$240k–660k    Human consultants per $5–25m matter
```

**The step-change is not at "AI". It is at the point where the product stops recording and starts reasoning about entitlement.** Two regimes — French general contracts and UK NEC — converged independently on the **€200–500/seat/month** band, and Germany independently discovered **per-claim pricing at €599**. Below that line the anchor price is $15–90/user/month tooling, which is why the entire US field layer is structurally locked out of recovery economics.

**And the warning in the same table:** the pure-play AI claims cohort prices a six-figure value event at **$29–$300/month**. Magra publishes a per-event recovery number and charges a flat annual fee. Either they are wrong about the value, or they cannot yet defend the price. Both readings are bad for them and useful to a new entrant.

## 2.3 Which stages have NOBODY

| Stage | Occupancy | Price today | Why it is empty |
|---|---|---|---|
| **(g) Causation / attribution** | **Zero products, worldwide** | Arithmetic $2,750–$25,000; opinion $225–$1,375/hr | **Standards-blocked and deliberately so.** AACE excludes responsibility assignment from the discipline; SCL's method descriptions both end *"the analyst investigates the project records to determine what events might have caused the identified critical delay"*; Steelray says so on its own product page. An automated verdict hands opposing counsel a ready-made cross-examination. |
| **(h) Recoverable-dollar quantification** | **Zero AI products, worldwide.** One non-AI product in one country | €599/case (DE only); otherwise consultant hours | See §3 — the full adjudication. |
| **(f) Evidence sufficiency vs a tribunal standard** | **Zero.** Two products score the wrong thing | £39–£99/mo (own-schema); included (own-schema) | Nobody asks "would this survive *Van Oord*?" Gather scores diary hygiene; ClaimMaster scores its own ERF; Clearstory checks backup against *company* standards. **Cheapest empty stage to build, and it is the natural pre-requisite to quantum.** |
| **The join (c)→(d)→(h)** | **Zero.** Gather has c/d/e/f and refuses h. Easyclaim has h/j and has no a–g. Magra claims all and ships none | — | This is the actual white space: not a stage, a **seam**. |

---

# 3. ADJUDICATING THE QUANTUM FINDING

**The finding under test:** `recoverable_dollar_estimation` scores 0–1 across every product in every language — Contradic, Magra (claimed 3, evidenced 0), Lexilio, BauAgent, ContraVault, Gather, SmartPM, Document Crunch, Trunk Tools, Clearstory (2, but only rate-library pricing of known work), the entire schedule-analytics category, the entire CLM category. The one exception, Easyclaim (Germany, €599/case), has no AI and no ingest.

## VERDICT: **CONFIRMED — quantum is genuinely unoccupied. But three of the five candidate explanations are FALSE, and correcting them changes what the wedge is.**

### (i) Too hard? **REJECTED.**

Three independent proofs that the mathematics is not the barrier:

1. **Easyclaim exists.** One *Sachverständiger*, no AI, no server, no account, a single HTML file you run by double-clicking, shipping since 2017 and tested on the most litigated public projects in Germany. It reverse-engineers the bid where no documented *Urkalkulation* exists, distributes cost across 26 categories, separates standstill from operating cost by cost type, converts markup percentages into daily rates, consolidates overlapping disruption windows automatically, and presents the answer under **two competing methods simultaneously** (combined markup and Opitz) with consistent rounding at every stage. **If a solo expert can ship court-grade quantum as one HTML file, quantum is not a technical problem.**
2. **Eichleay is arithmetic.** The formula itself is trivial. What is hard is the two judicially-imposed prerequisites — *uncertainty of the delay/standby period*, and *impracticability of taking on replacement work to absorb the overhead*. Those are **evidentiary conditions, not computations.** The Federal Circuit reinstated Eichleay after *Capital Electric*; judges have granted recovery under it in 100+ cases. The formula is settled; the *proof of the predicate* is the work.
3. **Measured mile is arithmetic too, once you have the baseline.** The literature is explicit that the method *"is a concept, not a procedure"*, that damage-quantification methods are *"indirect and imprecise"*, and that *"rarely will a contractor have the ability to foresee that a tracking system is necessary before it is too late."* **The blocker is input data, not calculation.**

**Restated: the barrier to quantum is (1) proving the legal predicate and (2) having the contemporaneous data. Both are evidence problems — i.e. stages (e) and (f), which is precisely where the tractable AI work is.**

### (ii) Too legally exposed? **PARTIALLY TRUE — but it only explains the platforms.**

The evidence for exposure is real and consistent:
- **Datagrid (a Procore company): *"entitlement and approval stay with the responsible project professionals."*** The platform holding all the data drew its line exactly where quantum begins.
- Procore carries a standing **UPL risk factor**; Document Crunch disclaims — *"we flag limitations clearly and encourage professional legal review"*; Aven-AI is "advisory-only"; ClaimMaster wraps everything in "governed AI within expert workflows"; Clearstory AI *"never acts without human review"*; every Autodesk AI surface carries a "requires verification" disclaimer.
- AACE §1.2(d): *"all methods are subject to manipulation as they all involve judgment calls by the analyst"*; §1.1 exists to defeat *"'black-box' or 'voodoo' analyses."*

**But this cannot be the whole answer**, because the startups with no franchise and no public-company disclosure obligations *also* don't build it. Magra names the methods without visible fear. Lexilio publishes exposure ranges. ClaimMaster's founder is a **RICS-certified expert witness with a forensic quantum background** — the single person in the cohort most qualified to ship quantum — and he shipped a **Defensibility Score instead**, and states plainly that the platform *"does not estimate dollar or quantum recovery."* That is a deliberate, informed choice by a domain expert. Legal exposure is an amplifier, not the cause.

### (iii) Too contract-specific / jurisdiction-specific? **TRUE — AND THIS IS THE PRIMARY CAUSE.**

The distribution of quantum products across the world is not random. It is a perfect one-to-one with **where the law supplies a computable cost methodology**:

| Regime | Computable cost method in law? | Quantum product exists? |
|---|---|---|
| **Germany** | **YES** — §642 BGB (Entschädigung), §650c BGB *tatsächlich erforderliche Kosten*, §2(3) VOB/B (quantity deviation), plus the Opitz method as an accepted alternative derivation | **YES — Easyclaim, CAC NAM** |
| UK NEC4 | Partly — cl. 63.1 Defined Cost + Fee via the Schedule of Cost Components is formulaic | **NO** — and Gather is *"three-quarters of the way to a Defined-Cost build"* and refuses (see §5) |
| FIDIC / GCC | No — Engineer determination under 3.7 | **NO** |
| US private (AIA) | No statutory or form-based cost method; §15.1.7 *mutually waives consequential damages* incl. home-office overhead and lost profit on other work | **NO** |
| Sweden / Norway / Italy / Netherlands / Spain / Poland / Japan / Korea / China | No | **NO — in any of them** |

Germany also uniquely supplies **the input file**: **GAEB / GAEB DA XML** is the mandated open exchange standard for bills of quantities, calculations and billing — and unlike XER it **carries the priced bill of quantities, i.e. the quantum baseline.** Germany hands a builder both the formula and the data.

**This is the correct diagnosis and it has been half-stated elsewhere in the program.** The note that "the US supplies no computable statutory cost method" is **not quite right**, and the exception is the whole opportunity:

- **Eichleay is a US federal, case-law-fixed formula** with defined prerequisites and 60+ years of board decisions.
- **FAR 52.243-4(d) / 52.242-14(c) / 52.242-17(b)** create a *rolling 20-day cost truncation* — an arithmetically demonstrable, per-day dollar consequence computable straight from a daily report.
- **Caltrans §5-1.43C** requires, within 15 days of the Initial PCR, *"Estimated claim cost and an itemized breakdown of the individual costs stating how the estimate was determined"* **plus a Time Impact Analysis**; §5-1.43D requires itemised labour (individuals, classifications, regular/OT hours, dates), materials (invoices, POs, locations, dates) and equipment (make, model, serial, hours, dates, rate book). Failure = *"Waiver of the potential claim... Bar to arbitration (Pub Cont Code §10240.2)."*

**Read that as what it is: a US public buyer has written the functional specification for a quantum engine, mandated its output on a 20-day clock, and attached statutory forfeiture to non-delivery. The computable method the US "lacks" exists in the spec book.**

### (iv) Not valued by buyers? **REJECTED — the counter-evidence is the strongest in the program.**

- **Easyclaim sells the number, per case, for €599, and has done since 2017,** to named public projects (Beethovenhalle Bonn, OLG Stuttgart, Flughafen Paderborn, multiple university hospitals). **This is the chargeable artefact the Levelset analysis concluded contractual notice lacks.** It is not a filing — it is a submission that survives judicial scrutiny.
- **Consultants are paid $240k–$660k per $5–25m matter** for exactly this work, at **$225–$1,375/hr**, and **Diales — the only listed pure-play — runs a 3.3% operating margin on £43.0m revenue.** That is a large, paid, unproductised market with no product leverage.
- **Clearstory's own Dodge research: 66% of GCs cite disputed pricing as the primary reason for withholding or reducing payment — above the 53% citing insufficient backup.** The market's **largest** cause of non-payment is disagreement about the number, and Clearstory's product optimises the smaller cause. Add: **91% of GCs sometimes short-pay; more than half short-pay on 20%+ of change orders; 77% of specialty contractors have written off change-order work as bad debt.**
- **Arcadis: "Poorly drafted or incomplete and unsubstantiated claims" was the #1 global cause of construction disputes.** The incumbent's own report says bad claim substantiation, not bad building, drives disputes.
- **Caltrans compels it.** Demand is not a matter of preference in the state-DOT segment; it is a condition precedent.

### (v) Genuinely unattended? **YES — and the mechanism is a supply-side alignment failure, not absent demand.**

Three populations could build it. Each is structurally disqualified:

1. **Those who can do it** (HKA, Diales, Exponent, FTI, CALIM, Drees & Sommer, Heilfort) **sell hours and cannot self-disrupt.** 57–73% utilisation cannot fund the destruction of its own hours. In ~9 years of aggressive M&A none of the twelve firms has bought or built a claims-detection product. Drees & Sommer's Dreso.AI is expressly **internal productivity**. Prof. Heilfort teaches the *Bauablauf-Differenzverfahren* and executes it in MS Project and Excel. **HKA's CRUX dataset only counts a project once >30 hours of claim work exists — they structurally cannot see the pre-dispute phase.**
2. **Those who have the data** (Procore, Trimble, Autodesk, Oracle, Clearstory, and all six NEC administration systems) **sell to owner and contractor on the same records and cannot take a side.** Quantum is inherently partisan: it is a number one party asserts against another. Five vendors, five countries, one identical stopping point.
3. **Those building AI claims products** (Magra, Lexilio, ClaimMaster, Delay Claim Builder, Contradic, SmartClaim, BauAgent, ContraVault, Ronayz, Aven-AI) are **1–5 person teams pricing at $29–$300/month.** That price cannot fund the domain depth quantum demands, and would not recover the cost if it did. They are stuck below the €200/seat line where reasoning starts to pay.

**And nobody is defending the ground.** Zero of ~$250M of 2025–26 contech funding went to a claims/entitlement/notice startup. Neither the Procore marketplace (455–539 apps) nor the Autodesk marketplace (194 partners) contains a single claims/entitlement/delay vendor.

## 3.1 The three hard constraints — the honest counterweight

I am confirming the wedge, not clearing it. Three constraints must be built into any V1:

1. **EOT ≠ money.** SCL Core Principle 12: entitlement to an extension of time does not automatically carry compensation, and *non-compensable Employer Risk Events* exist (weather being the canonical case). **Any auto-generated `delay days × daily rate` is wrong by construction for a whole class of events.** Time and money must be modelled separately, always.
2. **Quantum is downstream of causation, and causation is standards-blocked.** A number computed on an unproven causal chain is worthless and dangerous. **Quantum therefore cannot be sold as a standalone wedge.** It must ship attached to (e) evidence linking and (f) sufficiency — which is convenient, because (f) is the second-emptiest stage and far cheaper to build.
3. **The inputs are the constraint, not the formula.** Eichleay needs a proven standby period and proven impracticability of replacement work. Measured mile needs a clean undisrupted baseline with the same crews on the same project. Defined Cost needs the Schedule of Cost Components. **The product that wins on quantum is the one that assembles the evidence for the prerequisites — not the one that does the arithmetic.**

## 3.2 The reframe

> **Do not build "a quantum engine." Build "the priced, evidenced position": the number, plus the contemporaneous records that satisfy each legal prerequisite, plus an explicit list of the judgement calls a human must still make — and separate time from money at the data model level.**

Easyclaim proves the artefact is chargeable per case (€599). Consultants prove it is worth $240k–$660k done by hand. Caltrans proves a US buyer is contractually compelled to produce one in 20 days or forfeit. **Nobody has connected those three facts.**

---

# 4. DEMOWARE DETECTION

## 4.1 My evidence standard (stated before the verdicts)

A vendor is treated as **REAL for entitlement work** only if it passes at least three of four tests. I apply these uniformly and record which test fails.

| Test | What it requires | Why it is the right test |
|---|---|---|
| **T1 — Named customer, doing the entitlement workflow** | A named company on a page that company would object to if false — and doing *entitlement*, not the adjacent workflow (contract review, logging, billing, bidding) | The category's confidentiality excuse is real but not unlimited: Gather, Document Crunch, Easyclaim and the NEC six all publish names. If they can, the others' silence is a datapoint. |
| **T2 — A shipped data path** | At least one live integration, export, capture channel or upload flow — **not** "Upcoming", "coming soon" or "closed beta" | **Entitlement work is impossible without project data.** A detection claim with no data source is a claim about a product that cannot function. This is the single most discriminating test in the category. |
| **T3 — Independent corroboration** | A statutory filing, a marketplace listing with an install count, a procurement/framework record, a certification audit, or press not written by the vendor | Removes reliance on vendor marketing, which is all this category otherwise offers. |
| **T4 — Price consistent with the claim** | The price must be reconcilable with the asserted value | A vendor claiming six-figure per-event recovery and charging $29–$300/month is either wrong about the value or wrong about the product. |

**Standing caveat applied to everyone:** there is **no independent review corpus for this category anywhere.** G2/Capterra have no "construction claims" category; Capterra Germany has no *Nachtragsmanagement* category; Gather has zero independent reviews and no Procore Marketplace listing at all; Trunk Tools has zero reviews on Capterra/Software Advice/SourceForge; Document Crunch has 0 ratings on Procore Marketplace and ratings disabled on Trimble's. **Absence of complaints is not evidence of satisfaction here.**

## 4.2 Verdicts

### REAL, with verified paying customers — but note precisely *what* they are paid for

| Vendor | T1 | T2 | T3 | T4 | What the customers actually pay for |
|---|---|---|---|---|---|
| **Gather (UK)** | ✅ 11 named case studies — Network Rail, Costain ×2, Balfour Beatty ×2, Murphy, Amey, Circet, Cubby, Alma Rail, Dyer & Butler, Fourway, Dornan | ✅ mobile diary is the product; Procore/ACC connections live | ✅ **Companies House 10215108** (deferred income £334,572, +45%; cash-flow positive; loan repayment started); **G-Cloud 14 / Crown Commercial Service filing at £500/mo** | ❌ £500/mo flat while publishing 10×–39× ROI | **Detection + clause mapping + notice drafting + record assurance.** Evidenced outcomes are *defence* and *admin savings* — see §5 |
| **Document Crunch (Trimble)** | ✅ 36 named GCs | ✅ upload flow; Word add-in; Procore side-panel (reads nothing) | ✅ **Trimble 10-Q: $246.4M cash, $207.0M goodwill**; Inc. 5000 #311 | ✅ negotiated by project volume | **Contract reading + Playbooks + notice *drafting*.** Zero event detection, zero quantum |
| **Clearstory (US)** | ✅ Accurate Firestop, Marinship, Goodman, PCI Memphis, Clayco, Suffolk + 50 case studies | ✅ Procore/Autodesk/Vista/CMiC/Sage/Plexxis/HCSS live | ✅ Businesswire Series B; $2.1B/mo; 13 of top-25 NA GCs | ✅ free tier + per-user + per-project | **Change-order workflow and evidence capture.** Explicitly *not* entitlement, by published doctrine |
| **Trunk Tools (US)** | ✅ Gilbane, Suffolk, HITT, DPR, Consigli, Haskell, Torcon, Cleveland | ✅ Autodesk App Store v1.0.0; SharePoint/Box/Dropbox/Egnyte/Teams | ✅ **ENR** on the Gilbane seven-figure deal; **Globenewswire** on Suffolk; Insight Partners Series B | ✅ enterprise | **Document QA, submittal review, drawing-revision detection.** No claims surface at all |
| **Easyclaim (DE)** | ✅ Beethovenhalle Bonn, OLG Stuttgart, Zoo Leipzig, Zoo Gelsenkirchen, Flughafen Paderborn + named company testimonials | ❌ **none by design** (offline HTML, no server, no account — this is the trust pitch, not a lie) | ⚠️ court usage asserted, not independently indexed | ✅ **€599/case — perfectly consistent** | ✅ **THE QUANTUM ARTEFACT.** The only vendor on earth with paying customers for a recoverable-dollar computation |
| **NEC six** (CEMAR/Thinkproject, FastDraft, Sypro, Contract Bee, Unifier NEC4) | ✅ Highways England, Network Rail, Sellafield, Heathrow, ITER, VINCI, Yorkshire Water | ✅ mature | ✅ **£75bn of works** under CEMAR; G-Cloud listings | ✅ £25–£584/user/mo | **Administration of events a human already identified.** Zero detection, zero quantum |
| **ContraVault (IN)** | ⚠️ 30+ enterprise logos (Adani, Tata, NTPC, thyssenkrupp) — but for **pre-award bidding** | ✅ Procore/ACC/PlanGrid/MSP + API | ✅ **ISO 42001 / 27001 / 27017 / 27018 / 9001, SOC 2** (third-party audited) | ❌ no published price | **Bid intelligence.** The claims module is one marketing page. **Entitlement customers: unproven** |

### VAPOUR / UNPROVEN — no verified paying customer for entitlement work

| Vendor | Fails | The decisive evidence |
|---|---|---|
| **MAGRA** | **T1, T2, T3, T4** | **All eight integrations (Procore, Autodesk, Bluebeam, P6, Outlook, Gmail, Chat, Box) still listed "Upcoming" — re-verified 19 Aug 2026.** Zero named customers. No team page beyond one first name (`nazli@magra.app`). **And the killer:** the headline moved from **"$240K average value recovered per event"** to **"$17,824 avg. recoverable per event"** — 13.5× down — with methodology now stated as *"Estimates based on industry data: recoverable events at 5–10% of project value, identification and recovery benchmarks from ASCE research on construction change orders."* **A vendor that had recovered $240K per event would not restate it from ASCE literature.** Every Magra number is a spreadsheet output. Prices a claimed six-figure value event at $36k/yr flat. |
| **Lexilio** | T1, T3 | Published pricing ($29 / $299 / $1,999 per month) and zero named customers. Scores 0 on RFI, email, daily report, schedule, Procore and Autodesk — i.e. **no project-data path of any kind**, so its "notices triggered by project events" cannot be triggered by project events. The "Predictive claim exposure engine" is gated to the $1,999 tier and is an exposure *range*, not quantum. |
| **Delay Claim Builder** | T1, T3 | $299/mo published; nine tools; **no company name, no founder name, no address, no jurisdiction, no customers** — only `hello@delayclaimbuilder.com`. That is a lot of product surface for an entity that will not identify itself. |
| **ClaimMaster.ai** | T1 | Founder credentials are verifiable and specific (MBA Imperial, MCIOB, RICS Expert Witness certificate). Testimonials are **role-only** — "Commercial Director at a main contractor (London)". **Not demoware — an honest product with unproven distribution.** Notably it *refuses* the quantum claim rather than faking it. The £1,299/mo whitelabel tier is a genuinely interesting consultancy-channel signal. |
| **Aven-AI** | T1, T2 | *"Early access, no licence, no commitment"* — pre-revenue by its own admission. |
| **BauAgent.ai (DE)** | T1, T2, T3 | **Closed beta**, pilot firms only; email-analysis add-on and calendar integration *"coming mid-2026"*; Gantt "coming". Single founder. |
| **Contradic (FR)** | T1 (for construction) | SAS active since **1 Aug 2025**; funding round only *planned* for 2026; one **unnamed** energy client; independent review names *hallucinations on highly technical, jargon-heavy documents*, responsive-design failures, no multi-LLM, integrations "future". **Zero evidence of a single BTP/construction customer.** ICP is law firms. |
| **Handwai (DE)** | T3 | Claims **600+ firms, 4,000+ VOB projects, 86% repurchase, +7% margin** — **all vendor-stated, zero third-party corroboration found.** If directionally true it is the largest adoption figure in the category. `UNVERIFIED`. |
| **SmartClaim (FR), Ronayz (TR), Quollnet, CALIM 360, Alloovium** | T1 and/or T2 | SmartClaim: beta, no pricing, no customers, valuation absent. Ronayz: pre-launch, "Request a Meeting" the only conversion path. Quollnet: a chatbot and an Excel file — content marketing. CALIM 360: behind a contact form; the shipping assets are free lead-gen calculators. Alloovium (YC S26 + Startmate): real testimonials but **role-only**, no pricing, no funding figure; notice period is a *query*, not a clock. |

### The bottom line on the cohort

> **Across the entire AI-native construction claims cohort, worldwide: ONE vendor has verified paying customers for a quantum artefact (Easyclaim, Germany, no AI). ONE has verified paying customers for entitlement-event detection (Gather, UK, £500/mo, single-source, outcomes are defence). NOT ONE has a verified paying customer for the full detection→entitlement→evidence→quantum→package pipeline. The "competition" in this category is a set of product surfaces without customers.**

This cuts both ways and I will not soften either edge. **In your favour:** the category is uncontested by anyone with proof, and the first entrant to publish three named US GC references with recovered dollars owns the category narrative. **Against you:** an entire global cohort has failed to find that customer, and *"nobody has proven demand"* is a materially different situation from *"nobody has built it."* The eSUB natural experiment and the funding void say the same thing from two other directions.

---

# 5. THE GATHER LESSON

Gather is the closest thing to the thesis running anywhere: it detects compensation events off 10M+ diary records, maps them to clause 60.1 categories with an evaluation method, starts every NEC4 clock, scores record quality, and drafts clause-cited notices with confidence scores. It occupies stages (c), (d), (e), (f) and (i). **And in eleven published case studies it documents not one recovered compensation event in pounds.**

## 5.1 What the numbers actually are

| Headline | What it is |
|---|---|
| Network Rail / Murphy, Birmingham New Street: **"39× ROI; £300,000+ saved"** | **A CLIENT-SIDE SAVING.** *"Network Rail's project team had all the resources to **scrutinise** labour, plant and time allocation to each of the relevant activities **included in change requests**."* Money **withheld from the contractor**. |
| Circet / TfL 4LM: **"15× ROI; £140,000 in six months"** | **ADMIN LABOUR.** £1,012/wk contractor management + £2,400/wk commercial management. Not entitlement. (And the quoted Senior PM later became a **shareholder** in Gather.) |
| Costain A12: headline metric | **CLAIMS DEFENCE.** *"15% of claims rejected on the spot"*; *"the project team could immediately identify claims where records did not match the application."* |
| The other eight | Efficiency only — hours saved, records captured, pre-fill rates. |

Their own About page says the quiet part: ***"We don't take sides. We provide the objective, timestamped evidence that allows Contractors and Clients to agree on fair payment."***

## 5.2 What that teaches about what this product sells as

**It sells as ASSURANCE, not as RECOVERY.** And assurance is bought by whoever has the most to lose from a bad record — which, on Gather's own evidence, is the party paying the bills.

The distribution model confirms it. Gather's `/en/client` page is a playbook for asset owners to fund the licences and write the tool into the contract: *"4.7 Commercial Record Management — The Contractor shall use the Employer's nominated Commercial Record Management System (Gather)..."* **Owner-mandated, owner-funded, contractor-used.** That is not a contractor-recovery business; it is an owner-assurance business with a contractor-facing UI.

## 5.3 Does it imply the buyer is the owner, not the contractor?

Three readings. All three are true at once, and the third is the one that matters.

**(a) The weak-thesis reading — and it is real.** Owner-side defence is the easier sale. The owner has budget, mandate power, and a use case that prices itself: money withheld is money saved, immediately, on this project, verifiable in this month's application. Contractor recovery is speculative, adversarial, lands on a future P&L, and requires the buyer to admit their records are bad. **This materially strengthens hypothesis G (owner-side defence) and weakens the naive contractor-recovery pitch.** It is corroborated by every field-layer vendor's pricing: the entire segment anchors at $15–90/user/month because it sells hygiene, and hygiene is a cost.

**(b) But it is a lesson about NEUTRALITY, not about the buyer.** Gather chose to be neutral *first* — *"We don't take sides"* — and then discovered that a neutral evidence tool sells best to the party who benefits from neutral evidence, which on a disputed change request is the payer. **It never ran the contractor-side experiment.** A product that openly takes the contractor's side, asserts a number, and aims a document at the other party has never been tested at scale in any market. Gather's outcome tells you what happens to *neutral evidence tools*. It does not tell you what happens to *partisan recovery tools*, because nobody has built one.

**(c) The decisive corroboration — and this is the real lesson.** It is not just Gather. **Procore, Trimble, Autodesk, Oracle, Clearstory and all six NEC administration systems sell to both sides of the same project record, and every one of them stops at the identical line.** Datagrid says it in words: *"entitlement and approval stay with the responsible project professionals."* Clearstory publishes a doctrine to stay on the safe side of it. Aconex guarantees no party can query the whole record. Trimble's split is explicit: claim identification and dollar quantification are *deliberate* omissions. **Six independent vendors, five countries, three contract regimes, one identical stopping point.** That convergence is not six coincidences — it is the shape of a structural constraint, and it means **the seam is real: taking a side is the one thing none of them can do, and quantum lives inside it.**

## 5.4 The pricing mechanism this exposes

**Gather publishes 10×–39× ROI and charges £500/month flat, "not priced per User", with no value component.** That is not a mistake. **A neutral evidence tool cannot capture recovery economics because it has no claim on the recovery.** Neutrality caps price at tooling rates. The corollary: **only a partisan product can price on recovery** — and pricing on recovery is the only way past the $15–90/user/month anchor the entire field layer is stuck behind. This is the most transferable single finding in the whole category.

## 5.5 The counterweight I must state

Gather is also the strongest available evidence *against* the contractor-recovery pitch. FY2025 directors' report admits *"a high level of churn"*; headcount fell 14 → 10; FY2026 loss £93,424; lifetime equity ≈ **£713,163** (angels only, ≈£2.5m post-money); amortisation (£209k) now exceeds capitalised R&D (£184k) — **the product asset is shrinking.** Two of four leaders listed on the About page have resigned as directors. **Nobody has yet proven that a contractor will pay a premium for recovered entitlement — including the company best positioned in the world to prove it.**

**Net:** Gather is a free, eight-year, publicly-audited feasibility study that establishes four things at someone else's expense — (1) contract-aware event detection off daily records works and gets bought; (2) the buyer is the commercial/QS function, not the field; (3) owners will mandate and fund it; and (4) **the quantum step is the one nobody has taken, and the reason is neutrality, not difficulty.**

---

# 6. THREAT RANKING TO A NEW US ENTRANT

Ranked on: does it occupy the target stages · can it reach the US buyer · will it move downstream · does it price at zero.

### TIER 1 — EXISTENTIAL (threat is supply and price, not competition)

**1. Procore (with Datagrid) — HIGHEST THREAT.**
Owns the data plane and has now shipped the front three stages: Contract Review agent (21 May 2026), **Change Analysis agent (GA 23 Jul 2026)** identifying *"scope impacts, cost exposure, schedule risk and required follow-up actions"* from project records, **Triggers** firing on new RFI/submittal/change order, 150+ Actions writing Change Events, plus Levelset and 24 correspondence templates including Notice of Delay and Extension of Time. Prices it inside a credit bundle with a free starter pool. **It cannot do entitlement** — bilateral customer base, standing UPL risk factor, and Datagrid's explicit public refusal. **But it does not need to compete with you to hurt you.** It denied Trunk Tools API access in September 2025 and refunded its Groundbreak booth; its Developer Policy (eff. 30 Sep 2025) forbids developers to *"scrape, parse, harvest, build databases, bulk export"* API Data or use it to train AI. **A $70M-funded, Insight-backed company with 200+ Gilbane projects was cut off. A solo founder has no better standing.** Mitigation: file-upload / email-forward / customer-authorised-export V1 — which paradoxically gives you *better* commercial-record coverage than the best-funded incumbent.

**2. Trimble / Document Crunch — HIGHEST STRATEGIC THREAT.**
Owns (a), (b) and (i) outright. **$246.4M cash, closed 4 Apr 2026, of which $207.0M is goodwill — Trimble paid 84% of the price for future product.** Agentically generates notices, RFIs and submittals since 9 Jun 2026, and now has Vista, Spectrum, ProjectSight, e-Builder and Trimble Connect data inside the firewall — dissolving the data-access constraint that shaped seven years of its product. Will close the deadline clock in 3–6 months and event detection in 6–12 post-integration. **Will not cross into claims:** *"a construction industry with zero disputes"* is the literal vision statement, written by two ex-construction-claims lawyers who also sell to owners, insurers and sureties (AXA XL since Feb 2023). Their own Jan 2026 research names the thesis pain verbatim — *"notice windows had already closed, converting otherwise valid claims into absorbed costs"* — and prescribes *"brief the team better."* **Cleanest incumbent refusal in the program. Partner window ≈ 12–24 months.**

### TIER 2 — SERIOUS

**3. Trunk Tools.** ~$70M raised, reported $325M valuation, 100+ staff, a new evaluated agent every 4–6 weeks, revenue 4× then ~3.5×. TrunkReview already performs de-facto scope-change event detection, and the Cortex roadmap **explicitly names the missing edge**: *"How might a bulletin relate to a change order request?... This is an area we continue to work on."* **And it prices contract review at $0 to devalue point solutions.** Restraints: no email/Outlook connector, no daily-log agent, schedule agent stale since Aug 2024, Procore-severed, zero claims vocabulary anywhere on the site, and Liberty Mutual on the cap table. **Threat is price-setting and shipping speed, not intent.** Watch for: a daily-log or correspondence agent, an Outlook connector, the free contract tool moving into the authenticated platform with persistence, or any hire with "claims/risk/contracts/counsel" in the title.

**4. Clearstory.** Holds $2.1B/month of exactly the evidence a claims engine needs, across 14,000+ contractors and 13 of the 25 largest North American GCs, with six Gemini agents in production including a COR Pricing Agent and a **COR Review Agent (closed beta) that "confirms backup documentation."** Structurally barred from entitlement by three-sided neutrality — but **that agent is one product decision from checking backup against *contract* requirements rather than company standards.** Watch that release; it is the single highest-signal event in the US category. Otherwise: **the cleanest partner in the program** — a partner who cannot become a competitor.

**5. Autodesk.** Threat is acquisition of your category, not competition with it. **$387M cash for Payapps/GCPay despite already shipping pay applications; ~$3.6B for MaintainX.** Build ingests external email natively (unique project email address, threaded replies, custom types, references) and its RFI AI assistant auto-populates Cost Impact and Schedule Impact. But Pype points at Divisions 01–49 technical specs and **never Division 00 general conditions, where notice and claims clauses live**; SmartPlans and eBinder were withdrawn from sale 26 Mar 2024; every AI surface carries a "requires verification" disclaimer. **Exploitable asymmetry: Correspondence is the only major object with no public API and no Data Connector export — Autodesk captures the richest claim evidence and cannot get it back out, while Data Connector hands you the rest of the evidence graph as free scheduled CSV.**

### TIER 3 — REAL BUT CONTAINED

**6. Eve (template risk).** $103M Series B, 1,200+ plaintiff firms, running ***"nightly audits of active caseloads to surface missed opportunities"*** — structurally identical to "nightly audits of active projects to surface missed entitlement," proven in a different vertical. Not in construction today; pointable at it at any time by a well-capitalised team.

**7. Contradic (FR).** The only AI-native product combining a genuine cross-document evidence graph with **no owner-side franchise to protect** — i.e. it *can* take a side, which Procore/Trimble/Clearstory/Gather cannot. Its €199–349/user/month pricing independently proves the band outside NEC. Constrained by: active only since 1 Aug 2025, unfunded, law-firm ICP, French-only, zero construction customers, and documented hallucinations on technical documents. **Highest-threat startup in the world if it translates and pivots to contractors. Watch its 2026 round announcement.**

**8. Gather.** **ROADKILL to you only inside UK NEC4** — do not fight eight years of records, an NEC4 drafter, an owner-mandate channel into Network Rail and TfL, and £500/month pricing. **In the US: irrelevant.** 10 staff, £134,699 cash, £413,632 debt, **UK/EEA-only data residency with "user control over storage location: No"**, no SOC 2 / FedRAMP / StateRAMP, 9–5 UK support, and **zero US/AIA/ConsensusDocs URLs in a 337-URL sitemap**. Runway to US entry is years, if ever.

**9. SmartPM.** Not a threat — a **supplier**. $12,000/$25,000 per year, Procore + Autodesk marketplace placement, tagline already *"Out of Court"*, and an **open API giving "raw schedule data and all the metrics we calculate... No extra fees. No limits on users."** It stops exactly where you start. Consume its delay windows; never rebuild the CPM math (it is available at $2,750 perpetual).

**10. Horizontal CLM / contract AI (Icertis, Sirion, Agiloft, Luminance, Robin AI, Spellbook, LegalOn, DocuSign).** Threat is **narrative, not product**: a GC who has bought Spellbook or Luminance will ask "doesn't my tool already do this?" and you must answer in the first meeting. They built hypothesis A to full maturity (Sirion: 99% on-time obligation compliance, 80% fewer post-signature disputes, 8–12% spend-leakage reduction) and pointed it at renewals, terminations and SLAs at ~$88k median ACV. **Icertis' full published integration list contains zero construction systems; Sirion's 8 verticals and Agiloft's 7 exclude construction entirely.** DocuSign is the only one with a construction GTM and a Procore integration, at $45–$80/user/month. **Their recurring buyer complaints — "too many dependencies on back end team for configuration", "uploading third-party contracts is difficult" — are exactly the failure mode that kills CLM in construction, where every subcontract is third-party paper and nobody has a configuration team.**

**11. Microsoft 365 Copilot ($18–30/user/mo).** Threat to your *price*, not your product. It takes stage (a), most of (b) and half of (i). It cannot do persistent deadline state (stateless; requires a Copilot Studio agent with Recurrence triggers, maker credentials, DLP approval and metered credits), cannot see project traffic (no Procore/Autodesk grounding connector), cannot build a durable evidence graph, and 75% extraction accuracy is fine for a draft and unacceptable as the only guard on a time bar. **Consequence: never price per seat. Price per project, per event or per recovery.**

### TIER 4 — LOW / NOISE / PARTNER

**12. ContraVault (IN)** — connectors and 30+ enterprise logos, one-page claims module, zero quantum. **Partner or channel** into a market you would otherwise never reach.
**13. Magra** — threat only as a *narrative* competitor: it will rank in the same searches and make claims you cannot honestly match. **Its restatement from $240K to $17,824 per event is ammunition for you, not against you** — use it to establish an evidence standard the category cannot meet.
**14. Lexilio, ClaimMaster.ai, Delay Claim Builder, Aven-AI, Ronayz, SmartClaim, Quollnet, CALIM 360, Alloovium** — not one has a defended customer base. First to publish three named US GC references with recovered dollars takes the category.
**15. Easyclaim (DE) — NOT A THREAT; THE HIGHEST-VALUE PARTNER IN THE PROGRAM.** It holds the one capability nobody else on earth has — defensible, court-tested construction quantum — inside a one-person company with no distribution, no ingest, no AI and a 2017-era delivery model, and its trust pitch (*"das Dokument wurde nicht von einem Automaten erstellt"*) actively prevents it from adding AI itself. **You bring detection and evidence; they bring the number that survives court.** A licensing or white-label conversation is available to a solo founder in a way a Procore conversation is not.
**16. BauAgent, Handwai, CAC NAM, Capmo, PlanRadar, Nordic/Italian/Dutch/Spanish/Polish vendors** — non-threats in the US. Transplant **BauAgent's pricing line verbatim**: *"one Nachtrag finances the annual subscription."*
**17. nPlan, ALICE, Nodes & Links, Deltek Acumen, Steelray, Ron Winter** — schedule mathematics, commoditised at $2,750–$25,000. **nPlan's 750,000-schedule moat guards the wrong door**: causation is per-project document reasoning, not cross-project statistics.

---

# 7. HARDEST FACTS FROM THIS SYNTHESIS

1. **Magra's headline recovery figure has been restated from "$240K average value recovered per event" to "$17,824 avg. recoverable per event"** — 13.5× down — with the methodology now disclosed as *"Estimates based on industry data: recoverable events at 5–10% of project value... from ASCE research on construction change orders."* All eight integrations remain **"Upcoming"** (magra.app, magra.app/platform, verified 19 Aug 2026).
2. **Easyclaim (C. Abraham GmbH) is the only vendor worldwide with paying customers for a quantum artefact: €599 net per case, a 21-page court-ready derivation across 26 cost categories under §642 BGB / §6(6) VOB/B, dual method (combined markup and Opitz), delivered as a single offline HTML file with no AI, no server and no account** (bauzeitnachtrag-leichtgemacht.de).
3. **Trunk Tools gives away, free and with no account, an AI contract review across 14 categories including "Notice Deadlines & Methods", "Change Order Procedures", "Delay & Liquidated Damages" and "Dispute Resolution", returning "a compliance calendar, critical deadline matrix, delegation chart by role, and warning flags for high-risk provisions"** — verified live today (trunktools.com/resources/contracts). **The front half of the pipeline has a market price of $0.**
4. **ClaimMaster.ai — built by an MCIOB, RICS-certified expert witness with a forensic quantum background — explicitly does not estimate quantum, and ships a "Defensibility Score" across causation, entitlement, substantiation and mitigation instead** (claimmaster.ai). The most qualified person in the cohort chose evidence sufficiency over quantum.
5. **Gather still says, verbatim, "Cost of extra materials, labour, and plant to be calculated"** — re-verified 19 Aug 2026 (gatherinsights.com/en/qs-ai-agent). The most on-thesis product in the world has not moved on quantum, and its own About page explains why: *"We don't take sides."*
6. **Steelray, implementing the same AACE RP 29R-03 half-step method as SmartPM at a sixth of the price, states: "The tool does not attribute responsibility to parties... leaves interpretation of causation and fault to the analyst or expert witness."** ($3,990/user/yr vs SmartPM $25,000/yr; Ron Winter $2,750 perpetual.)
7. **Eichleay's barrier is legal, not computational**: the formula is trivial arithmetic, but courts require proof of (a) an uncertain delay/standby period and (b) impracticability of taking on replacement work to absorb the overhead. **Measured mile's barrier is data, not computation**: the literature calls it *"a concept, not a procedure"*, and notes contractors *"rarely... foresee that a tracking system is necessary before it is too late."* **Both barriers are evidence problems, i.e. stages (e) and (f).**
8. **Clearstory's own Dodge research: 66% of GCs cite disputed pricing as the primary reason for withholding or reducing payment — above the 53% citing insufficient backup.** The market's largest cause of non-payment is disagreement about the number, and no product anywhere addresses it.

---

# 8. UNKNOWNS — AND WHAT WOULD SETTLE EACH

| Unknown | What would settle it |
|---|---|
| **Whether any AI claims vendor in the cohort has a single paying entitlement customer.** None publishes one. | Direct vendor outreach for a reference; UK G-Cloud / Digital Marketplace supplier spend records for ClaimMaster and Lexilio; Companies House filings for the UK entities. |
| **Whether Clearstory's COR Review Agent (closed beta) will check backup against the *contract* rather than company standards.** This single release changes the US competitive picture. | The GA release notes, or a customer walkthrough. **Highest-value single watch item in the US.** |
| **Whether Procore's Change Analysis agent produces a dollar figure or only a qualitative "cost exposure" flag**, and the real credit cost of running it across a portfolio. | A Procore Digital Coworker package price sheet, or a customer Control Tower screenshot showing credit burn per agent. |
| **Whether Easyclaim would license or white-label.** The single highest-leverage partnership in the program. | A direct approach to Carsten Abraham. The software-licence price is only disclosed in a demo. |
| **Whether Contradic is planning English/US entry or has any construction customer.** | Its 2026 funding-round announcement; an English-language site; a named BTP case study. |
| **Real accuracy of the two detection claims** — Gather's "40% more change events than manual review" (against an *unsourced* 60% baseline) and Magra's "92% identification rate". Both self-reported, no published methodology. | A blind back-test against a project with a known claim outcome. **This benchmark does not exist and building it would itself be a defensible asset.** |
| **Whether a US contractor will send a notice, or assert a number, that software drafted without a QS or counsel reading it.** The single most important unanswered question in the thesis. | 10 contractor interviews. Nothing in this corpus answers it. |
| **Whether any tribunal has accepted a software-generated quantum or delay analysis without a testifying expert.** | SCL judicial-references summary; a construction-law database search of ASBCA/CBCA and AAA awards. Not addressed by any source reached. |
| **Whether Magra has any revenue at all.** | A Delaware/state filing, a funding announcement, or a named customer. Currently: one first name and a ROI calculator. |
