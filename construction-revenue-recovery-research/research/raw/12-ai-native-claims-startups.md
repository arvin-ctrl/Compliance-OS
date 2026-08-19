# 12 — AI-NATIVE CONSTRUCTION CLAIMS / ENTITLEMENT / NOTICE / CONTRACT-COMPLIANCE PRODUCTS
### Global discovery sweep — landscape report
Research date: **19 August 2026**. Prepared against `research/BRIEF.md`.

---

## 0. METHOD, COVERAGE AND HONEST LIMITATIONS

**What I did.** Discovery sweep across: (a) direct product-page and pricing-page fetches for every candidate found; (b) the Y Combinator open company dataset (`yc-oss.github.io/api`, full 6,186-company dump, keyword-intersected on construction × claims/contract/compliance/notice terms); (c) vendor-authored comparison and "alternatives" pages, which are biased but are the densest source of competitor names in this category; (d) VC portfolio pages (Foundamental); (e) construction-tech funding roundups (Construction Dive, Crunchbase News); (f) UK Companies House; (g) Product Hunt construction topic; (h) Google autosuggest as a demand proxy.

**Limitation you must weigh.** The session's shared web-search budget was exhausted (200/200) early in this task by other agents, and every general search engine I could reach — DuckDuckGo, Mojeek, Brave, Ecosia, Qwant, Yep, four SearxNG instances — returned CAPTCHA, 403 or 429 through this environment's proxy. Bing's HTML and RSS endpoints returned geo-hijacked junk (South African construction firms, Westlake TX builders, Eventbrite listings) regardless of query. **So this sweep is directory-, dataset- and link-graph-driven rather than keyword-search-driven.** That biases discovery toward companies that (i) rank in vendor listicles, (ii) are in the YC dataset, or (iii) are linked from something I already found. Non-English products — German `Nachtragsmanagement`, French, Chinese, Japanese, Turkish, Korean — are almost certainly **under-covered**; I flag this in UNKNOWNS. I did reach India, UAE/KSA, Australia, UK and Turkey products via English-language link paths.

**Everything below is labelled.** Where I could not verify, it says `UNVERIFIED`.

---

## 1. HEADLINE ANSWERS TO THE FOUR KEY QUESTIONS

**(1) How strong are AI-native construction contract products right now — real products with customers, or demoware?**

**Bimodal, and the split is geographic and by pipeline position.**

- **Real, with named reference customers and quantified case studies:** Document Crunch (10,000+ projects, being acquired by Trimble), Gather (£25bn+ project value, 4,500+ daily users, Network Rail / Costain / Balfour Beatty / Amey / Circet case studies with named £ figures), Built Intelligence FastDraft (Environment Agency, National Grid, Balfour Beatty, Irish Rail), Sypro (VINCI, Willmott Dixon), Contract Bee (Yorkshire Water, Scottish Water, Anglo American), ContraVault (Adani, TATA, NTPC, Shapoorji Pallonji, thyssenkrupp), Provision ($7M seed, Ferrovial/EllisDon/PCL/Acciona), Trunk Tools (500+ jobsites, $50bn volume).
- **Claims-pipeline-specific AI products are conspicuously thinner:** Magra, Delay Claim Builder, ClaimMaster.ai, Lexilio, Aven-AI, CALIM 360 — all publish product surface, several publish *pricing*, but **none publishes a named customer for the claims workflow itself**. Magra publishes the most aggressive metrics in the whole sweep (92% event identification, $240K average recovered per event, 658x ROI) and simultaneously lists **every single integration — Procore, Autodesk, Bluebeam, P6, Outlook, Gmail, Box — as "Upcoming."** That is the signature of a pre-integration product selling a claimed pipeline.
- **Verdict:** the *contract-review* half of the space is real and consolidating. The *claims/entitlement* half is real as software but **pre-proof** as a business — with the single, important exception of Gather in the NEC market, which has done the detection layer with real customers and published £ recoveries.

**(2) Is there a product that already does the full thesis pipeline anywhere in the world?**

**Yes — two, and neither is in the US mid-market general-contractor position the thesis implies.**

- **Magra (US)** markets the literal thesis pipeline end to end: Radar ingests emails, daily logs, RFIs, meeting minutes, schedule updates and submittals → identifies entitlement and the clause → drafts the Notice of Claim / Change Order Request → prices it with Eichleay, measured-mile, extended general conditions, escalation and lost productivity → tracks the response and the notice window. That is *exactly* hypothesis A→E. It is unproven (no customers named, integrations pending).
- **Gather (UK, NEC4)** does the same loop within a different contractual regime and **with evidence**: site diary is the ingestion layer, the QS AI Agent reads 100% of diary entries against clause 60.1 categories, flags compensation events and early warnings, drafts the notice with the clause reference, and the Report module produces Cost Verification Records. It stops short of a full quantum/claim-narrative engine.
- Nobody found does **all five stages with proof at every stage**. Detection+notice is proven (Gather). Valuation+package is proven-ish as software (Delay Claim Builder, Magra) but not proven commercially.

**(3) What is the most dangerous competitor we had not named?**

**Gather (Gather Insights Limited, Manchester UK — gatherinsights.com).** See §4. It is dangerous for reasons that compound:
- It is the **only** product I found that attacks the *detection* gap rather than the *administration* gap, and it says so explicitly and publicly.
- Its team is the NEC establishment: **Ben Walker, Commercial Director — founder of CEMAR** (the UK's dominant NEC contract-management system, acquired by Thinkproject 2018) **and involved in drafting NEC4**; **Nick Woodrow, Operations Director — former COO of CEMAR and Thinkproject UK**. They know exactly where the incumbent they built stops.
- It was **formerly "Rail Diary Limited"** (renamed 16 Jan 2024, Companies House 10215108, incorporated 6 June 2016). So it has an 8-year installed base of site-record data and a rail/infrastructure customer list *predating* the AI pivot. That is the proprietary contemporaneous-record corpus a solo founder cannot conjure.
- It ships a **two-way Procore sync, a public API and an MCP server** — i.e. it is deliberately building the integration surface the thesis V1 needs.
- Runner-up dangerous: **Datagrid — "a Procore Company."** Procore now owns the AI-agent layer *and* Levelset (notice/lien deadlines). Combined with Procore's 20 pre-built agents (Contract Review, RFI, Daily Log, Risk, Deep Search), Procore holds every input the thesis pipeline needs.

**(4) Does the European/ME NEC-FIDIC niche prove the wedge works, or prove it only works where the contract form mandates the workflow?**

**Mostly the latter, with one crucial caveat that is the best news in this report.**

The NEC niche has **six-plus mature contract-administration products** (CEMAR/Thinkproject CONTRACTS, FastDraft, Sypro, C-COM, Contract Bee, Oracle Unifier NEC4 configurations) with published per-seat pricing from £25 to £584/user/month and blue-chip public-infrastructure customers. That is a real, paid, decade-old market. **But it exists because NEC4 makes the workflow contractually compulsory and time-barred** — clause 61.3's eight-week bar extinguishes the entitlement absolutely, and the Project Manager is contractually obliged to operate the same register. The software is sold as *compliance*, not as *revenue recovery*. Where the contract form does not mandate a shared register (AIA/ConsensusDocs US private work, most JCT), no equivalent installed base exists — the US analogue that actually got big was **Levelset**, and it monetised **statutory** lien/notice deadlines, not contractual ones. Pattern: **the wedge productises where a deadline is externally enforced (statute or standard form), not where it is merely commercially wise.**

**The caveat, and it is the important one:** every one of those six NEC systems begins *after a human has decided an event exists*. Gather's own competitive analysis states it flatly — *"They administer events a person has already identified"* … *"before that moment there is a gap … measured in days."* So the mature niche proves the **administration** layer monetises under a mandating contract form; it explicitly does **not** prove the **detection** layer, which remains genuinely unclaimed everywhere except Gather's NEC4 beachhead. **The detection layer is the white space; the mandating contract form is the go-to-market accelerant, not the requirement.**

---

## 2. THE FULL LANDSCAPE — EVERY PRODUCT FOUND

Pipeline key — **D** event Detection · **E** Entitlement matching · **V** eVidence assembly · **$** recoverable-Value estimation · **P** claim Package generation.

### TIER 1 — AI-NATIVE, CLAIMS/ENTITLEMENT-SPECIFIC (the direct competitive set)

| Product | URL | Geo | Stage | Pipeline |
|---|---|---|---|---|
| **Gather** (Gather Insights Ltd) | gatherinsights.com | UK | Founded 2018 (ex-Rail Diary Ltd); scaled, funding undisclosed | **D E V $(partial) P(partial)** |
| **Magra** | magra.app | US | Pre-proof, 2026 | **D E V $ P** (all claimed) |
| **Lexilio** | lexilio.co | UK/UAE/KSA/USA | Early; Microsoft for Startups + Baltic Ventures | **E $ P(register)**, weak D/V |
| **Delay Claim Builder** (+ SiteLog) | delayclaimbuilder.com | AU/global multi-currency | Self-serve, $299/mo published | **V $ P**, weak D |
| **ClaimMaster.ai** | claimmaster.ai | UK | Solo-founder (Paul Njonga), £39–£1,299/mo published | **V P**, **no D** |
| **ContraVault AI** | contravault.com | India / APAC | 200+ enterprise clients; funding undisclosed | **V P** (+ heavy pre-award) |
| **Aven-AI** | aven-ai.com | UAE / MENA | Early access, no licence yet | **E** + deadline tracking |
| **CALIM / CALIM 360** | calim.ai | Qatar/KSA/UAE (+India, USA) | Consultancy with a software wrapper | services-led **E V $ P** |
| **Quollnet DelayClaims AI** | quollnet.com | UNVERIFIED | Free chatbot + Excel templates | advisory only |
| **Opteam** | opteam.ai | UAE + Canada | 100+ companies (Dar, DAMAC, ALEC, Dutco) | **D(schedule) $(delay attribution)** |
| **Banamind** | banamind.ai | UAE/KSA (GCC) | Early, founder Viacheslav Muliukin | **V** (field record supply) |

### TIER 2 — THE NEC / FIDIC COMPENSATION-EVENT & EARLY-WARNING NICHE (mature, pre-AI, administration-layer)

| Product | Owner | Published price | Customers | Detects events? |
|---|---|---|---|---|
| **Thinkproject CONTRACTS (CEMAR)** | Thinkproject (acquired CEMAR 24 May 2018) | **£435 / licence / month** | Highways England, Network Rail, Sellafield, Heathrow, BAE, ITER, Nuclear New Build; **£75bn of works administered** | **No** |
| **FastDraft** | Built Intelligence Ltd (Bristol, co. 08323228) | **£250 / licence / month** | Environment Agency, National Grid, Kier, Mace, AECOM, Balfour Beatty, Galliford Try, BAM Nuttall, Wates, Transport Scotland, Irish Rail, DEFRA, Port of Dover | **No** — "AI Contract Coaching" is behavioural prompting |
| **Sypro Contract Manager** | Pagabo Group; built by **Dr Stuart Kings, NEC4 drafter** | **£25–£65 / user / month** | VINCI, Atkins Réalis, Willmott Dixon, Pick Everard | **No AI features stated** |
| **Contract Bee** | Digital Beehive Ltd (Leeds, co. 04046113) | **£30–£49.99 / user / month**, 30-day free trial | Yorkshire Water, Scottish Water, Sasol, Anglo American, Galliford Try, Costain | **No** |
| **C-COM** | UNVERIFIED (domain not resolvable from here) | not published | mining/energy focus | **No** |
| **Oracle Primavera Unifier — NEC4 config (RPC UK)** | Oracle / RPC | **£107.42–£584.82 / user / month** | UK public sector via G-Cloud | **No** |
| **NEC Digital** | NEC (neccontract.com) | UNVERIFIED | UNVERIFIED | UNVERIFIED |
| **Gather** | Gather Insights | not published | Network Rail, Costain, Balfour Beatty, Murphy, Amey, Circet, Siemens, NG Bailey, TfL | **YES — the only one** |

Pricing and the "none of them detect" finding come from Gather's own comparison page — **vendor-authored, therefore biased in Gather's favour** — but the *structural* claim is independently consistent with every one of those six vendors' own product pages, which describe registers, workflows, alerts and audit trails and never describe evidence-driven event identification.

### TIER 3 — AI CONTRACT REVIEW / OBLIGATIONS (pre-award and risk-first; adjacent, converging)

- **Document Crunch** — documentcrunch.com. Alpharetta GA. **Trimble announced intent to acquire, 2 April 2026, price undisclosed, expected to close Q2 2026.** 10,000+ projects; 500+ companies; Balfour Beatty, DPR, Swinerton, Boldt. Funding: $4.6M seed (Zacua Ventures) → +$2M Oct 2022 (Ironspring, with FifthWall, Argonautic, GTM Fund; ~$8M total at that point) → **$21.5M Series B, Jan 2025**. Modules: CrunchAI, Project Assist (generates submittals, **notices**, RFIs), risk routing, playbooks. **Procore embedded integration since 4 April 2024** explicitly moving "critical contract requirements and **notice provisions**" to field teams. **AXA XL contract-review benchmarking partnership, 28 Feb 2023** — insurance-adjacent, scores contracts on 11 key terms against peers.
- **Provision** — provision.com. YC S22, "Ironclad for construction". **$7M seed led by Cercano Management, 15 Oct 2025; $8.7M total**; angels Ryan Sutton-Gee (PlanGrid), Nicholas Pilkington (DroneDeploy). Ferrovial, EllisDon, PCL, Acciona, Bird, Colas, Cleveland Construction. **$100bn project value reviewed; $1.8M/yr saved at EllisDon.** Scope Agent GA 4 Aug 2026. **Pre-construction only — no claims/notice surface.**
- **Mastt** — mastt.com. AU/APAC + NA + MENA. **Free first project, then $150/month per project.** Contract review, pay-app compliance, jurisdiction checks, Risk module. **No dedicated EOT/variation/claims module.**
- **Contracts Connected** — contractsconnected.com. US, 500+ named clients (Aztec, FedVet, I.E.-Pacific, RORE). SOC 2. Drafting, e-signature, COI/bond/W-9 enforcement, change orders, audit-ready filing. **Vendor-compliance, not entitlement.**
- **Alloovium** — alloovium.com. **YC S26 + Startmate.** Sydney + SF. Ingests documents, emails and conversations; tracks requirements against ISO, OSHA, contractual obligations and codes; sentence-level citations. Customer quote: *"To be able to go into Alloovium and ask what my notice period is for NODs, that's unbelievable."* **Closest YC-backed adjacency to the thesis.**
- **Nomic** (AEC) — nomic.ai. **Self-service from $20/month.** Aurecon case study (+30% productivity). Publishes an extensive AI-claims-management glossary that names Magra and ContraVault as the category — i.e. Nomic is content-marketing *into* the claims category without shipping a claims module.
- Horizontal/legal, not construction-native: **Spellbook**, **LegalOn** (AIA/ConsensusDocs/EJCDC playbooks), **LexCheck**, **SuperLegal** (~$999/mo), **Evisort**, **Litera Kira**.

### TIER 4 — AI-NATIVE CONSTRUCTION DOC/AGENT PLATFORMS (no claims module today; the real medium-term threat)

- **Datagrid — "a Procore Company"** (datagrid.com). Built on Anthropic's Claude Agent SDK. Deep Search / Submittal Review / RFI / Daily Log agents. Level 10, Victaulic, Haskell, Grunley, Mortenson. Its own change-order article says it classifies change requests from emails, PDFs and field directives, extracts scope/pricing/schedule impact, and flags contract compliance gaps — **while explicitly declining to automate entitlement**: *"entitlement and approval stay with the responsible project professionals."* That is a deliberately drawn line, and it is drawn exactly at the thesis.
- **Procore** — 20 pre-built agents including Contract Review, RFI, Daily Log, Risk, Deep Search; three Digital Coworker packages; "Skills" for customer-taught standards (Aug 2026). Owns **Levelset** (statutory notice/lien deadlines, $59/recipient) and **Datagrid**.
- **Trunk Tools** — trunktools.com. TrunkText / TrunkSubmittal / TrunkReview / TrunkRFI / TrunkBid. 500+ jobsites, $50bn volume, 87% verified field accuracy. Gilbane, Suffolk, Granite, Consigli, Haskell. Integrates Procore, Autodesk, SharePoint, Box, Dropbox, Egnyte. **No contract/claims/notice surface today.** Funding UNVERIFIED.
- **nPlan** — nplan.io. 750,000+ historical schedules, $2tn of spend, **$500bn under active management**; Laing O'Rourke, Google, ExxonMobil, Skanska, Network Rail, Shell, HS2, Sizewell C. Schedule-risk forecasting. **No claims or entitlement layer.**
- **Autodesk / Payapps** — payapps.com, an Autodesk company. Progress claims + variations + retentions, Security of Payment Act (AU) and Construction Contracts Act (NZ) compliance. **34 of Australia's top 50 builders; 57,000+ users; AUD$35bn+ annual payment claims; 13,400+ projects/yr.** This is the AU statutory-deadline analogue of Levelset.
- Others with no claims surface: Helonic (YC F25), Structured AI (YC F25, $4.2M seed), InspectMind, Constructable, dili ("Automating Compliance for Construction", YC S23), Klava AI (pre-launch), FlowManual (YC S26), Foreman (YC W26).

### TIER 5 — INCUMBENT PM/ERP/CDE (own the data, don't own the workflow)

Oracle **Aconex**, Oracle **Primavera Unifier**, **InEight** (Contract / Change / Document / Compliance — AI only in Schedule), **Kahua**, **Autodesk Construction Cloud**, **Bluebeam**, **Xpedeon**, **Causeway**, **Riskonnect**, **Intelex**.

### TIER 6 — FALSE POSITIVES (named in listicles, do NOT do contract claims — record so nobody re-researches them)

- **ClaimBuild / Velit Solutions** (velitsolutions.com) — **insurance restoration** claims, Australia. 250k+ claims managed. Different market entirely.
- **Arched.ai** — India, government-tender pursuit and bid intelligence. Its own "12 Best Construction Claims Management Software" listicle is SEO fodder that lists Procore, Bluebeam, Riskonnect and Intelex as "claims software."
- **Red Marble AI** — Australian AI *consultancy* (Downer, Orica, Webjet); no construction-claims product.
- **Harmony CMC** — Istanbul construction-claims *consultancy* (Galataport, Emaar Square); services, not software.
- **Varicon** — Australian civil cost control; progress claims = payment applications, not entitlement claims.
- **Nomic.ai** — AEC AI platform; claims content marketing only, no claims module.

---

## 3. PIPELINE COVERAGE MAP — WHO OWNS WHICH STAGE

| Stage | Genuinely occupied by | Evidence quality |
|---|---|---|
| **Event detection** from contemporaneous records | **Gather** (site diary → CE/EWN), **Magra** (email/RFI/log/schedule → event) | Gather: strong, named customers. Magra: claimed only. |
| **Entitlement matching** to clause | **Gather** (clause 60.1 categories), **Magra** (AIA §15.1.3), **Lexilio**, **Aven-AI**, **Document Crunch** | Multiple credible players. **Most crowded stage.** |
| **Evidence assembly** | **Gather** (10M+ structured records), **ContraVault** (Claim Timeline + Evidence Trail), **Delay Claim Builder** (Evidence Assembler), **ClaimMaster.ai** (ERF + Defensibility Score) | Real but fragmented. |
| **Recoverable-value estimation** | **Magra** (Eichleay / measured-mile / extended GCs / escalation / lost productivity), **Lexilio** (predictive claim exposure engine, Enterprise tier), **Delay Claim Builder** (prolongation section) | **Thinnest, least proven stage.** Nobody has evidenced a quantum engine against real outcomes. |
| **Package generation** | **Delay Claim Builder** (9-section EOT narrative → Word), **Magra** (NOC/COR in 48h), **ContraVault**, **ClaimMaster.ai** | Software exists; commercial proof does not. |

**The structural finding:** every stage is occupied by *someone*, but **no one occupies all five with evidence**, and the two hardest stages — detection with real field data, and defensible quantum — are held by different companies on different continents under different contract forms.

---

## 4. CAPABILITY MATRIX — TOP 3 (plus a bonus 4th row)

### 4.1 GATHER (gatherinsights.com) — **most dangerous competitor found**

`SCORES| 2,2,3,3,2,1,3,3,2,3,2,2,3,3,2,2,3,2,3,1,1,3,3,2,2,2`

| # | Dimension | Score | Justification (source) |
|---|---|---|---|
| 1 | contract_ingestion | 2 | Ingests contract terms to map events, but not marketed as a contract-parsing engine — gatherinsights.com/en/qs-ai-agent |
| 2 | clause_extraction | 2 | "Maps events to contract clauses and specifies evaluation methods"; NEC3/NEC4/JCT/FIDIC — /en/qs-ai-agent |
| 3 | notice_detection | **3** | Core: flags compensation events and early warnings from diary entries — /en/qs-ai-agent |
| 4 | deadline_tracking | **3** | "Detects compensation events before notice periods expire"; eight-week time-bar tooling — /en/nec4/eight-week-time-bar |
| 5 | rfi_event_ingestion | 2 | Two-way Procore sync implies RFI reach; not explicitly marketed — gatherinsights.com |
| 6 | email_ingestion | 1 | Microsoft Copilot/365 integration listed "coming soon" — gatherinsights.com |
| 7 | daily_report_ingestion | **3** | This *is* the product: offline mobile diary, voice-to-text, GPS, 10M+ records — /en/about |
| 8 | schedule_integration | **3** | Plan module imports programmes, **pre-fills 64% of diary fields**, planned-vs-actual — gatherinsights.com |
| 9 | change_order_workflow | 2 | Flags change orders and drafts notices; administration still lives in CEMAR/FastDraft — /en/qs-ai-agent |
| 10 | claim_identification | **3** | "identifies 40% more change events than manual review" — /en/qs-ai-agent |
| 11 | delay_detection | 2 | Pattern recognition ("productivity dropped 30% since access change in Zone B"); not forensic — /en/qs-ai-agent |
| 12 | responsibility_attribution | 2 | Implicit via clause 60.1 categorisation; no explicit attribution engine — /en/nec4/compensation-events |
| 13 | contemporaneous_evidence_graph | **3** | Timestamped, GPS-tagged records linked to programme activities — gatherinsights.com |
| 14 | evidence_completeness | **3** | Analyses "100% of diary entries"; disallowed-cost defence; CVR generation — /en/nec4/disallowed-cost |
| 15 | recoverable_dollar_estimation | 2 | Cascade costing example (£21,000) + missed-CE cost estimator calculator; not a quantum engine — /en/qs-ai-agent |
| 16 | claim_package_generation | 2 | Drafts notices and EOT recommendations, not full claim narratives — /en/qs-ai-agent |
| 17 | notice_drafting | **3** | "drafts notices with contract clause references" — /en/qs-ai-agent |
| 18 | schedule_impact_analysis | 2 | EOT recommendations + planned-vs-actual; no TIA/windows methods — /en/qs-ai-agent |
| 19 | procore_integration | **3** | Two-way sync marketed — gatherinsights.com |
| 20 | autodesk_integration | 1 | Lists Thinkproject, Aconex, Viewpoint, Fieldwire; Autodesk not named — gatherinsights.com |
| 21 | outlook_gmail_integration | 1 | Copilot/365 "coming soon" only — gatherinsights.com |
| 22 | mobile_workflow | **3** | Offline mobile app, voice-to-text, GPS — core product — gatherinsights.com |
| 23 | audit_trail | **3** | Timestamped records, ISO 27001, ISO 9001, Cyber Essentials Plus, retention guidance — /en/site-diary/retention |
| 24 | portfolio_risk | 2 | Report dashboards across projects; Fourway runs 10 projects on it — /en/customer-stories |
| 25 | performance_pricing_compatibility | 2 | Publishes per-customer ROI (39x, 21x, 15x) and £ recovered — but sells flat SaaS — /en/customer-stories |
| 26 | consultant_replacement_potential | 2 | "QS AI Agent" does QS review work but positions as augmenting in-house QS — /en/qs-ai-agent |

**Total 62/78.**

### 4.2 MAGRA (magra.app) — the purest thesis clone

`SCORES| 3,3,3,3,3,2,3,2,3,3,3,2,2,2,3,3,3,2,1,1,1,3,1,2,3,3`

| # | Dimension | Score | Justification (source) |
|---|---|---|---|
| 1 | contract_ingestion | 3 | Magra Brain contract knowledge base; free 60-second contract analysis tool — magra.app/platform |
| 2 | clause_extraction | 3 | Clause search; drafts cite "the clause already cited"; AIA A201 §15.1.3 — /solutions/agent |
| 3 | notice_detection | 3 | Radar flags events requiring notice — /solutions/radar |
| 4 | deadline_tracking | 3 | Tracks notice windows and escalates as deadlines approach — /solutions/radar |
| 5 | rfi_event_ingestion | 3 | Radar monitors RFIs and submittals — /solutions/radar |
| 6 | email_ingestion | 2 | Radar claims email monitoring, but Outlook/Gmail listed "Upcoming" — /platform |
| 7 | daily_report_ingestion | 3 | Daily logs + Magra Text SMS/iMessage field logging with auto-tagging — /platform |
| 8 | schedule_integration | 2 | Monitors schedule updates; **P6 integration "Upcoming"** — /platform |
| 9 | change_order_workflow | 3 | Drafts COR, prices it, tracks owner response — /solutions/radar |
| 10 | claim_identification | 3 | "92% change order and claim event identification rate" (self-reported) — /solutions/radar |
| 11 | delay_detection | 3 | Delays and differing conditions; time impact analysis — /platform |
| 12 | responsibility_attribution | 2 | Backcharges + entitlement basis; no explicit attribution engine — /platform |
| 13 | contemporaneous_evidence_graph | 2 | Links event to records; no graph/chronology product named — /solutions/radar |
| 14 | evidence_completeness | 2 | "fully substantiated" NOC claimed; no completeness score — /solutions/radar |
| 15 | recoverable_dollar_estimation | 3 | **Eichleay, measured-mile, direct cost buildup, extended general conditions, escalation, lost productivity** — /platform |
| 16 | claim_package_generation | 3 | "$2.3M delay claim package in 48 hours"; 48h field-event-to-NOC — /solutions/radar |
| 17 | notice_drafting | 3 | Contract-compliant NOC with legal language and citations — /solutions/agent |
| 18 | schedule_impact_analysis | 2 | TIA named but P6 integration pending — /platform |
| 19 | procore_integration | 1 | Listed "Upcoming" — /platform |
| 20 | autodesk_integration | 1 | Autodesk/Bluebeam listed "Upcoming" — /platform |
| 21 | outlook_gmail_integration | 1 | Listed "Upcoming" — /platform |
| 22 | mobile_workflow | 3 | Magra Text: SMS/iMessage field logging, no app install — /solutions/text |
| 23 | audit_trail | 1 | Not marketed; no audit/immutability claim found — /platform |
| 24 | portfolio_risk | 2 | ROI calculator is portfolio-shaped (8–150 projects); no portfolio risk module — /roi-calculator |
| 25 | performance_pricing_compatibility | 3 | Publishes $240K average recovered per event vs $36K/yr cost — perfectly gainshare-shaped — /roi-calculator |
| 26 | consultant_replacement_potential | 3 | Explicitly replaces "$85,000 over 4 months" consultant engagements — /platform |

**Total 63/78 — but read it as 63 *claimed*.** No named customer, no shipped integration.

### 4.3 LEXILIO (lexilio.co) — contract-side entitlement + notice engine, published pricing

`SCORES| 3,3,2,3,0,0,0,0,1,2,0,1,1,0,2,1,3,0,0,0,1,0,3,3,2,2`

| # | Dimension | Score | Justification (source) |
|---|---|---|---|
| 1 | contract_ingestion | 3 | Whole contract suites; "847 clauses across multiple documents" in <2 min — lexilio.co |
| 2 | clause_extraction | 3 | FIDIC (Red/Silver), NEC3/NEC4, JCT, AIA — lexilio.co |
| 3 | notice_detection | 2 | "auto-drafts compliant notices **triggered by project events**" — but events are contract/user-derived, not evidence-derived — lexilio.co |
| 4 | deadline_tracking | 3 | **Notice & Deadline Tracker** (Professional tier) + Compliance Calendar — lexilio.co/pricing |
| 5 | rfi_event_ingestion | 0 | Not evidenced |
| 6 | email_ingestion | 0 | Email alerts out only; no ingestion — lexilio.co |
| 7 | daily_report_ingestion | 0 | Not evidenced |
| 8 | schedule_integration | 0 | Not evidenced |
| 9 | change_order_workflow | 1 | Variations analysed as documents in cross-document conflict module — lexilio.co |
| 10 | claim_identification | 2 | **Predictive claim exposure engine** (Enterprise); "Risks & Opportunities" surfaces margin opportunities — lexilio.co/pricing |
| 11 | delay_detection | 0 | Not evidenced |
| 12 | responsibility_attribution | 1 | Flow-down error mapping across main contract/subcontract — lexilio.co |
| 13 | contemporaneous_evidence_graph | 1 | Audit log is of platform activity, not project evidence — lexilio.co |
| 14 | evidence_completeness | 0 | Not evidenced |
| 15 | recoverable_dollar_estimation | 2 | "Expected exposure · weighted range $200k–$473k" — lexilio.co |
| 16 | claim_package_generation | 1 | Board-ready risk/obligation registers (PDF/Excel), not claim packages — lexilio.co |
| 17 | notice_drafting | 3 | Notice letter drafting from Professional tier up — lexilio.co/pricing |
| 18 | schedule_impact_analysis | 0 | Not evidenced |
| 19 | procore_integration | 0 | Not evidenced |
| 20 | autodesk_integration | 0 | Not evidenced |
| 21 | outlook_gmail_integration | 1 | Calendar integration + email alerts; no mailbox ingestion — lexilio.co |
| 22 | mobile_workflow | 0 | Not evidenced |
| 23 | audit_trail | 3 | "Module 05: Audit Log & Activity Trail — timestamped, attributed" — lexilio.co |
| 24 | portfolio_risk | 3 | Portfolio dashboard with benchmarking (Professional tier) — lexilio.co/pricing |
| 25 | performance_pricing_compatibility | 2 | Quantifies exposure but sells flat SaaS $29/$299/$1,999 — lexilio.co/pricing |
| 26 | consultant_replacement_potential | 2 | Replaces contract-review consultancy, not claims consultancy — lexilio.co |

**Total 36/78.**

### 4.4 BONUS — DELAY CLAIM BUILDER (delayclaimbuilder.com) — the back half of the pipeline, self-serve

`SCORES| 3,3,1,1,0,0,2,3,2,1,2,2,2,2,2,3,3,3,0,0,0,3,1,0,1,3`

Nine tools: Contract Clause Extractor · Notice of Delay Generator · Variation & Delay Notice · Delay Claim Builder · **The Rebutter** (drafts responses to rejections) · Programme Analyser (parses P6 `.xer`/`.xlsx`) · Transmittals · Delay Register · Evidence Assembler. Companion **SiteLog** mobile app for real-time delay capture. EOT methods: Time Impact Analysis, Windows, As-Planned vs As-Built, Impacted As-Planned, Collapsed As-Built. Contract forms: FIDIC 2017, NEC4, JCT, AS 4000, bespoke. **Published price: $299 USD/month single user**, enterprise custom. Currencies AUD/AED/EUR/GBP/JPY/USD. Exports to Word. **Total 32/78 — but note it scores 3 on package generation, notice drafting and schedule impact analysis, the exact stages Gather is weakest on.** No named customers; no company or founder information published anywhere on the site beyond `hello@delayclaimbuilder.com`.

---

## 5. SHORT PROFILES — THE REST

**ClaimMaster.ai** (UK). Founder **Paul Njonga** — MBA Imperial, MCIOB, RICS Expert Witness certificate, forensic quantum background. Positions as "the defensibility layer" beside your systems. Modules: Event Record Form, AI Evidence Structuring, Team Workflows, **Defensibility Score** (shows claim vulnerability before submission). Published pricing: **Standard £39/mo (20k AI credits, 5 events) · Pro £99/mo (100k credits, 30 events) · Whitelabel from £1,299/mo**. ICP: QSs, claims consultants, MEP/civils/façade subcontractors. **Critically: no event detection — everything enters via manual Event Record Forms.** Tagline: *"If You Can't Prove It, You Don't Get Paid."* The whitelabel tier is a claims-consultancy channel play, which is a genuinely interesting GTM signal.

**ContraVault AI** (India/APAC). 200+ enterprise clients — Adani, TATA, NTPC, Shapoorji Pallonji, thyssenkrupp, Toyo Engineering, Voltas, ISGEC, Kalpataru. Metrics: $630M+ project value processed, 200K+ RFPs analysed, 10M+ pages parsed, 25K+ RFI clarifications drafted, 95%+ extraction accuracy. Certifications are the most complete of anyone found: ISO 27001/27017/27018/9001/**42001 (AI management)**, SOC 2, GDPR. Claims modules: Claims Repository (tagged variation/delay/payment/scope), **Claim Timeline** (auto-structures events by date/topic/party), **Evidence Trail**, Response Drafting with citations. But the mass of the product and all the metrics are **pre-award bid intelligence** — claims is a bolt-on. Founders, funding, HQ all undisclosed.

**Aven-AI** (UAE/MENA). Governed, advisory-only: flags deadlines and drafts notices, human approves everything. AI Insights inbox, Programme module (P6/MS Project import, critical path and slippage), contract obligation extraction tied to activities, role cockpits (Project Director / PM / CM / QS / HSE), approvals queue, HSE module. FIDIC 1999 + NEC4 + heavily amended forms. Founder is an HSE professional with 19 years on UAE sites. **"Early access, no licence, no commitment"** — pre-revenue. References: Neo Towers, Meridian Consultants, Al Fares Construction. Single-tenant, immutable audit trail, project-level kill switch.

**CALIM / CALIM 360** (Qatar, KSA, UAE + India, USA). A **consultancy** — notice calendar at mobilisation through DAAB/arbitration, contemporary records, delay analysis, LD defence, quantum, close-out. Free lead-gen tools: **Notice Deadline Calculator, LD Exposure Estimator, Claim Readiness Score, Retention Release Calculator**. "CALIM 360" digital monitoring platform mentioned but not detailed. FIDIC 1999 cl. 20.1, FIDIC 2017 cl. 20.2, employer-amended GCC variants. **This is the pattern to watch: consultancies wrapping free calculators around a services business — an obvious channel, and an obvious future competitor.**

**Opteam** (Dubai Silicon Oasis + Waterloo, Ontario). AI project controls: Schedule Health Check, WhatsApp-based progress collection (claims 80% tracking-time reduction), automated P6 sync, **Delay Claims Analysis** (where delays occurred, root cause, responsibility, impact). Integrations: P6, MS Project, Excel, WhatsApp, email. 100+ companies including **Dar, SIAC, DAMAC, ALEC, Dutco, Al Ghurair**. The WhatsApp ingestion channel is the single cheapest field-evidence capture mechanism found in this entire sweep and is directly relevant to a solo-founder V1.

**Banamind** (GCC, UAE/KSA). Founder Viacheslav Muliukin. Photo/video jobsite documentation, progress tracking, AI cost estimation, document intelligence, delay prediction. Its own material positions delay AI as **"a ground-truth data supplier rather than a standalone forecasting engine."** Break-even framing: contractors with 2–3 projects >$100M/yr.

**Quollnet** — free "DelayClaims AI Assistant" chatbot trained on FIDIC, NEC, SCL Delay & Disruption Protocol; Delay Analysis Method Selector (an Excel file, 12 questions, score-based); templates and checklists. **Content-marketing funnel, not a product.**

**Nomic (AEC)** — nomic.ai. Nomic Platform + Agent API; 380+ building codes grounded; 200–800-page document parsing; SharePoint/Autodesk/Box/Egnyte/ProjectWise + 10 more. Self-service **from $20/month**. Aurecon: +30% productivity, +20% engineering capacity, ~20,000 hrs/yr saved. Publishes a whole AI-claims-management glossary naming Magra and ContraVault. **They are ranking for the claims keywords without shipping claims.** Watch them.

**Levelset (Procore)** — the US precedent that matters. Preliminary notices, lien deadline tracking, mechanics lien filing, lien waivers, pay apps, 50 states + DC/Guam/PR/USVI. **$59/recipient** for notices and payment demands. Monetises *statutory* deadlines. Acquisition price not confirmed from a primary source in this sweep (`UNVERIFIED`).

**Payapps (Autodesk)** — the Australian statutory analogue. 34 of AU's top 50 builders, 57,000+ users, **AUD$35bn+ annual payment claims**, 13,400+ projects/yr. AU/UK/IE/NZ. Security of Payment Act and Construction Contracts Act compliance. MYOB, Xero, Jobpac, Access Coins integrations.

---

## 6. PRICING — EVERYTHING PUBLISHED (highest-confidence facts in this report)

| Product | Published price | Confidence |
|---|---|---|
| Lexilio | **$29 / $299 / $1,999 per month** (Starter/Professional/Enterprise); 15% annual discount | HIGH — vendor pricing page |
| ClaimMaster.ai | **£39 / £99 / from £1,299 per month** | HIGH — vendor homepage |
| Delay Claim Builder | **$299 USD/month** single user | HIGH — vendor homepage |
| Mastt | **Free first project, then $150/month per project** | HIGH — Mastt comparison page |
| Nomic (AEC) | **from $20/month** self-service | MEDIUM — vendor glossary/homepage |
| Levelset | **$59 per recipient** (notices, payment demands) | HIGH — levelset.com |
| Magra | **$36,000/year** (used in own ROI calculator) | MEDIUM — implied, not a price list |
| Thinkproject CONTRACTS (CEMAR) | **£435 / licence / month** | MEDIUM — Gather comparison (competitor-sourced) |
| FastDraft | **£250 / licence / month** | MEDIUM — Gather comparison |
| Sypro | **£25–£65 / user / month** | MEDIUM — Gather comparison |
| Contract Bee | **£30–£49.99 / user / month**, 30-day free trial | MEDIUM — Gather comparison |
| Oracle Unifier NEC4 (RPC) | **£107.42–£584.82 / user / month** | MEDIUM — Gather comparison, sourced to G-Cloud |
| SuperLegal | ~**$999/month** | MEDIUM — Mastt comparison |
| Gather, Document Crunch, Provision, ContraVault, Aven-AI, Opteam, InEight, FastDraft-enterprise | **Not published** | — |

**Read this table twice.** The pure-play claims AI products all price at **$29–$300/month self-serve**. The NEC administration incumbents price at **£25–£584 per user per month, enterprise-contracted**. The claims-AI cohort has chosen prosumer pricing for a workflow whose *value event* is worth six figures. Either they cannot yet defend enterprise pricing, or they have not found the buyer who owns the P&L consequence. **That gap is the commercial opportunity and the commercial warning simultaneously.**

---

## 7. WEAKNESSES AND EXPLICIT GAPS — DELIBERATE OR UNATTENDED?

| Gap | Who has it | Deliberate or unattended? |
|---|---|---|
| **No event detection from evidence** | All six NEC administration systems; ClaimMaster.ai; Lexilio; Delay Claim Builder | **Deliberate for the NEC six** — their buyer is the Project Manager administering a *shared, contractually mandated* register; auto-detecting the contractor's events would put the vendor on one side of a bilateral contract. **Unattended for the AI-native cohort** — this is the actual white space. |
| **Entitlement automation refused** | Datagrid/Procore, explicitly: *"entitlement and approval stay with the responsible project professionals"* | **Deliberate — legal exposure.** Procore will not put its name on an entitlement opinion. This is the single most important defensive moat available to a startup. |
| **Quantum/valuation engine unproven** | Everyone. Magra names the methods; Lexilio gives exposure ranges; nobody evidences accuracy | **Unattended, and hard.** Eichleay and measured-mile are contested even between human experts. |
| **No email/mailbox ingestion** | Gather (Copilot "coming soon"), Lexilio (0), all NEC six | **Unattended.** Email is where 80% of commercial events actually get communicated. Gather compensates via the site diary; nobody does mailboxes properly. |
| **No named claims customers** | Magra, Lexilio, ClaimMaster.ai, Aven-AI, Delay Claim Builder | **Unattended / too early.** Also possibly *deliberate* — claims are adversarial and confidential; customers may refuse to be named. That is a permanent GTM handicap for the whole category and should be assumed, not discovered later. |
| **Detection is single-source** | Gather detects only from *its own* site diary | **Deliberate (it's their moat) and a genuine hole.** A competitor ingesting email + RFI + minutes + schedule alongside diaries sees events Gather cannot. |
| **US private-work market has no mandating form** | The entire NEC cohort is UK/infrastructure-locked | **Structural.** AIA A201 §15.1.3's 21-day notice is a condition precedent in many jurisdictions but there is no shared register and no Project Manager duty to maintain one. |
| **Nobody sells on outcome** | Every vendor sells flat SaaS despite publishing per-event recovery values | **Unattended.** Magra publishes "$240K average recovered per event" and charges $36K/yr flat. Somebody will eventually price on recovery. |

---

## 8. ADJACENCY TEST — HOW HARD FOR EACH TO SHIP THE FULL PIPELINE?

| Player | Rating | Reasoning |
|---|---|---|
| **Gather** | **EASY** | Already has detection + notice drafting + 10M contemporaneous records + programme integration + Procore sync + API/MCP. Missing only quantum and claim-narrative generation. Ex-CEMAR leadership knows the commercial workflow cold. Org incentive is total — this *is* their pitch. Legal exposure appetite already demonstrated (they publish detection accuracy claims). **Assume 6–12 months if they choose to.** |
| **Datagrid / Procore** | **EASY technically, HARD organisationally** | Owns Procore data, Levelset notice infrastructure, 20 agents, Claude Agent SDK. But has *publicly drawn the line at entitlement*, sells to owners and GCs simultaneously (bilateral conflict), and carries public-company legal exposure. They will do detection and drafting; they will not do entitlement opinions or quantum. **This is the shape of the opportunity: build what Procore has decided it will not.** |
| **Document Crunch / Trimble** | **MEDIUM** | Has notice provisions, obligations, Project Assist generating notices, and a Procore embed. Post-acquisition it becomes the "contractual rule set" for all of Trimble Construction One — a rules engine wired to ERP is an excellent claims substrate. But integration takes 12–24 months and Trimble's incentive is cross-suite risk control, not contractor revenue recovery. |
| **Magra** | **MEDIUM** | Product design is already the full pipeline; the hard part is *shipping the integrations it has listed as "Upcoming"* and getting one referenceable customer. It is the closest competitor by design and the furthest by evidence. |
| **Thinkproject / Built Intelligence / Sypro / Contract Bee** | **HARD** | Structurally bilateral: their buyer is the PM and the Contractor jointly. A detection engine that finds the contractor more money is a product their client-side users would veto. This is not a capability gap, it is a **business-model prohibition** — and it is why the NEC incumbents left the detection layer open for eight years. |
| **Trunk Tools / Nomic / Alloovium** | **MEDIUM** | Have the document infrastructure and citation quality; lack construction-commercial domain (entitlement, quantum, notice law). Nomic is already SEO-farming the claims keywords, which usually precedes a module. |
| **nPlan** | **HARD→MEDIUM** | Best delay-forecasting dataset on earth ($2tn, 750k schedules) but zero contract layer and an owner-side customer base (HS2, Network Rail, Shell). |
| **Claims consultancies (HKA, CALIM, Harmony CMC)** | **HARD** | Every hour the software saves is an hour they cannot bill. But note ClaimMaster.ai's **£1,299/mo whitelabel tier** — the consultancies are already being sold the tooling. |

---

## 9. STARTUP POSTURE

- **Procore / Datagrid / Autodesk / Trimble-Document Crunch → CHANNEL, trending to ROADKILL.** They own the data and the distribution but have publicly refused the entitlement opinion. Build on their APIs, sell the judgement layer they will not sell. The moment you become a feature rather than a liability-bearing opinion, you are roadkill.
- **Gather → ROADKILL if you compete in UK NEC4. PARTNER if you are US/AIA.** Do not enter NEC4 detection against a team containing CEMAR's founder and Thinkproject UK's ex-COO with an 8-year record corpus and Network Rail on the reference list. Their weakness is single-source detection (diary only) and geography.
- **The NEC administration six (CEMAR, FastDraft, Sypro, Contract Bee, C-COM, Unifier) → PARTNER.** Structurally barred from detection by their bilateral buyer. They need a detection feed; they cannot build one. This is the cleanest partnership shape found in the sweep.
- **Claims consultancies → CHANNEL.** ClaimMaster.ai has already proven they will buy whitelabel tooling at £1,299/month.
- **Magra, Lexilio, Delay Claim Builder, ClaimMaster.ai, Aven-AI → COMPETITORS, all beatable today.** None has a defended customer base. First one to publish three named GC references with recovered £/$ wins the category narrative.
- **Insurers → the unexplored channel.** AXA XL has been benchmarking contracts through Document Crunch since **Feb 2023**. Contract quality already touches construction insurance underwriting. Nobody has connected *entitlement preservation* to *premium or surety pricing*. That is the most defensible performance-pricing wedge visible in this landscape.

---

## 10. CUSTOMER VOICE — HONEST STATEMENT

**I could not obtain five verbatim customer complaints against the claims-AI cohort, and I will not invent them.** G2/Capterra have **no "construction claims management" category at all** — Capterra's construction-management filters are Budget Tracking, Change Order Management, Document Management, Mobile Access, Multiple Projects, Project Management, Scheduling, Task Management, Timesheet Management, Subcontractor Management, Inventory Management, Purchase Order Management. No claims, no contract administration, no variation tracking. Reddit/forum sourcing was not reachable with search unavailable.

What I did capture, verbatim:

1. *"We've never seen software that does what Gather can do with site records"* — Ian Adams, quoted at gatherinsights.com/en/qs-ai-agent. (Vendor-published testimonial.)
2. *"To be able to go into Alloovium and ask what my notice period is for NODs, that's unbelievable."* — customer testimonial, alloovium.com/en. **This is the clearest independent evidence in the whole sweep that "what is my notice period" is a live, unmet, felt pain for a contractor.**
3. *"I built Gather because I was sick and tired of terrible records."* — William Doyle, CEO, gatherinsights.com/en/about. Founder-pain statement, useful as market evidence.
4. *"An agent that can read a contract but doesn't know the difference between a conditional and unconditional lien waiver will create more problems than it solves."* — contractsconnected.com/research/ai-agents-construction. Domain-depth objection you will face in every sale.
5. *"projects lose money not because the work was done badly, but because the records were incomplete, scattered, or arrived too late."* — gatherinsights.com/en/nec4. Competitor's framing of the exact thesis.

**All five are vendor-published.** Treat as marketing, not as independent user research. **Recommendation: this is the single biggest evidence hole in the whole workstream. Commission or conduct 10 contractor interviews before capitalising on any of it.**

---

## 11. HARDEST FACTS (the strongest numeric findings, each with URL)

1. **Trimble announced its acquisition of Document Crunch on 2 April 2026**, expected to close Q2 2026; Document Crunch is deployed on **10,000+ projects**; Trimble will use it as "a contractual rule set … the intelligent DNA for the entire Trimble Construction One suite." Price undisclosed. — https://www.prnewswire.com/news-releases/trimble-to-acquire-document-crunch-to-add-ai-powered-risk-management-and-document-compliance-to-trimble-construction-one-project-delivery-ecosystem-302731851.html
2. **Document Crunch raised a $21.5M Series B (Jan 2025)**, after ~$8M across a $4.6M Zacua-led seed and a $2M Ironspring-led round (Oct 2022, with FifthWall, Argonautic, GTM Fund); team grew 3 → 23 in 24 months. — https://www.documentcrunch.com/news/hypepotamus-series-b and https://www.documentcrunch.com/news/document-crunch-takes-additional-strategic-investment-to-fuel-growth-and-expand-its-offering-to-include-key-data-benchmarking-partnerships
3. **Gather manages £25bn+ of project value with 4,500+ daily users and 10M+ records captured**, founded 2018, and publishes named recoveries: **£300,000+ saved on scope changes at Network Rail Birmingham New Street (39x ROI)**; **£140,000 saved in six months at Circet/TfL 4LM with 11% overall project cost reduction (15x ROI)**. Companies House 10215108, incorporated 6 June 2016, **renamed from RAIL DIARY LIMITED on 16 January 2024**. — https://www.gatherinsights.com/en/about · https://www.gatherinsights.com/en/customer-stories · https://find-and-update.company-information.service.gov.uk/company/10215108
4. **The NEC administration market has real, published enterprise pricing and £75bn of works under one product alone**: Thinkproject CONTRACTS (CEMAR) **£435/licence/month** administering **£75bn of works and services** for Highways England, Network Rail, Sellafield, Heathrow, ITER; FastDraft **£250/licence/month**; Sypro **£25–£65/user/month**; Contract Bee **£30–£49.99/user/month**; Oracle Unifier NEC4 **£107.42–£584.82/user/month**. — https://www.gatherinsights.com/en/comparisons/best-nec4-contract-management-software · https://www.thinkproject.com/products/thinkproject-cemar/
5. **Magra publishes the most aggressive economics in the category and cannot yet support them**: **92% claim-event identification**, **$240K average value recovered per event**, **48 hours from field event to substantiated Notice of Claim**, **$85K saved per claim vs consultant fees**, **$36K/yr price → 658x claimed ROI**, versus **zero named customers** and **every integration (Procore, Autodesk, Bluebeam, P6, Outlook, Gmail, Chat, Box) listed as "Upcoming."** — https://magra.app/solutions/radar · https://magra.app/roi-calculator · https://magra.app/platform
6. *(bonus)* **Across two 2025–26 construction-tech funding roundups totalling ~$250M — PermitFlow $54M, Attentive.AI $30.5M, Fyld $41M, Sensera $27M, XBuild $19M, Moab $16M, Payra $15M, Unlimited $12M, ConCntric $10M, Kojo $10M, Planera $8M, Brickanta $8M — not one dollar went to a claims, entitlement or notice startup.** — https://www.constructiondive.com/news/construction-tech-funding-Q4-2025/808986/ · https://www.constructiondive.com/news/contech-funding-fyld-sensera-xbuild-moab-payra/814452/
7. *(bonus)* **The NEC4 eight-week time bar is absolute and costs real money**: Gather documents a highways contractor losing **£149,850** (£135,000 Defined Cost + 11% Fee) because the CE was notified on 10 March against a 2 March bar. — https://www.gatherinsights.com/en/nec4/eight-week-time-bar

---

## 12. UNKNOWNS — AND WHAT WOULD SETTLE THEM

| Unknown | What would settle it |
|---|---|
| **Non-English products.** German `Nachtragsmanagement` (VOB/B §2 Nachträge) is a large, formalised claims market; France, Japan, Korea, China, Turkey, Brazil likewise. I reached none of them. | Native-language search in DE/FR/JA/ZH/TR/PT; Bau-IT / Digitales Bauen trade press; RIB Software and Nemetschek product catalogues. |
| **Gather's funding and revenue.** Investors and rounds are not published; Companies House shows accounts to 31 Mar 2026 but the figures were not on the overview page. | Companies House filing history — download the FY2026 accounts PDF. Also Beauhurst / UK Companies House charges register. |
| **Trunk Tools' funding.** Widely reported as a $40M Series B (`UNVERIFIED` — I could not confirm from a primary source). | Trunk Tools press page or a Crunchbase/PitchBook record. |
| **Procore's acquisition of Datagrid** — confirmed by datagrid.com's "a Procore Company" footer, but **date and price unverified**. | Procore investor-relations news release; SEC 8-K. |
| **Levelset acquisition price** (widely cited as ~$500M by Procore in 2021) — `UNVERIFIED` from a primary source here. | Procore 10-K / 8-K, 2021. |
| **Whether any claims-AI product has paying customers at all.** None publishes one. | Direct outreach; ask each vendor for a reference; check G-Cloud / Digital Marketplace supplier records for UK vendors (Gather, ClaimMaster, Lexilio). |
| **Real accuracy of detection claims** (Gather's "40% more events", Magra's "92%"). Both are self-reported with no published methodology. | Independent pilot; or a customer willing to run a blind back-test against a known claim outcome. |
| **Whether contractors will let software make an entitlement assertion.** Datagrid/Procore have publicly refused; Aven-AI is "advisory-only"; ClaimMaster.ai wraps everything in "governed AI within expert workflows." | Contractor interviews — specifically: *would you send a notice your software drafted without a QS reading it?* This is the single most important unanswered question in the entire thesis. |
| **US market: is there any AI-native claims product for AIA/ConsensusDocs private work besides Magra?** I found none. That is either the opportunity or the graveyard. | US-specific search once budget is restored; AGC / ABC / CFMA vendor exhibitor lists; ENR Top 25 Newsmakers tech coverage. |
| **Verbatim customer complaints.** Zero obtained (see §10). | Reddit r/ConstructionManagers, r/QuantitySurveyor; LinkedIn comment threads under Gather/Document Crunch posts; contractor interviews. |

---

## 13. WHAT THIS MEANS FOR THE THESIS (analyst view)

1. **The thesis is not novel — it is being attempted right now on three continents.** Magra is a near-literal implementation. Gather is the same idea, contractually localised, and already working with real customers. **Speed and evidence, not insight, are the scarce goods.**
2. **The detection layer is the only genuinely defensible stage.** Entitlement matching is crowded (five+ credible players), package generation is commoditising ($299/month), quantum is unproven by everyone. Detection is held by exactly one company with proof, in exactly one contractual regime, from exactly one data source (its own diary).
3. **The NEC/FIDIC niche proves the *administration* layer monetises under a mandating form. It does not prove the *detection* layer monetises anywhere.** Gather is the experiment currently running on that question and it is going well enough to be frightening.
4. **The two big precedents that actually got large — Levelset ($59/notice, US statutory liens, bought by Procore) and Payapps (AUD$35bn/yr, AU Security of Payment Act, bought by Autodesk) — both monetised *statutory* deadlines, not contractual ones, and both were acquired by the PM platform.** That is the most likely exit shape and the most likely ceiling.
5. **The single largest unexploited seam:** Procore/Datagrid have *publicly and deliberately* refused to automate entitlement. Everything upstream of that line is being commoditised by platforms with better data. **The defensible business is the liability-bearing judgement they will not touch — and the correct monetisation of a liability-bearing judgement is not $299/month.**
6. **Solo-founder feasibility check.** Gather needed a mobile field app, an 8-year record corpus and four senior construction hires. Magra needed none of that and has no customers. The V1 that threads this: **ingest email + attachments by forward, plus P6 export, plus a contract PDF** — that is the Opteam/Magra ingestion shape, requires no integration partner, and reaches the detection layer that everyone except Gather has left open.

