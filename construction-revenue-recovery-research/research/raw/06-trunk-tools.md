# 06 — TRUNK TOOLS
### AI agents for construction document intelligence
Research date: 2026-08-19 · Analyst pass against `research/BRIEF.md`

---

## 0. ONE-PARAGRAPH VERDICT

Trunk Tools is the best-funded, fastest-shipping **field-and-office productivity agent company** in construction — not a commercial/entitlement company. Its entire shipping surface (TrunkText, TrunkSubmittal, TrunkReview, TrunkRFI, TrunkBid, TrunkRegister, TrunkBrowse, TrunkSOP) is *pre-dispute*: find the answer faster, catch the discrepancy earlier, submit the cleaner RFI. It has built the single most valuable substrate for the revenue-recovery thesis — a construction-native drawing/document knowledge graph called **Cortex**, trained on 2M+ hand-labelled drawing artifacts — and it explicitly says its knowledge-graph roadmap includes *"How might a bulletin relate to a change order request?"*. It also quietly ships a **free AI contract review tool** that extracts *Notice Deadlines & Methods*, *Change Order Procedures*, *Delay & Liquidated Damages* and emits a "compliance calendar, critical deadline matrix". So: the evidence-collection half of the thesis is being commoditised in front of us. What is *not* being built is entitlement logic, causation, quantum, or a claim/notice package — and there is a structural reason (they sell to GC operations, not GC legal/risk, and they are actively de-risking their platform relationships after Procore cut their API access).

---

## 1. SNAPSHOT

| | |
|---|---|
| **Legal/brand** | Trunk Tools, Inc. ("Trunk.Tools") |
| **Founded** | 2021, by Dr. Sarah Buchner (Founder & CEO) while at Stanford GSB |
| **HQ** | New York, NY (10012) |
| **Founder background** | Austrian carpenter from age 12 → GC project manager/group leader in Europe → PhD in Civil Engineering & Data Science → Stanford GSB |
| **Total raised** | ~$70M (Seed + Series A + $40M Series B) |
| **Series B** | $40M, announced **24 Jul 2025**, led by **Insight Partners**; with Redpoint Ventures, Innovation Endeavors, StepStone, Liberty Mutual Strategic Ventures, Prudence |
| **Valuation** | **$325M** post-Series B (2025) — `UNVERIFIED` beyond one secondary source |
| **Headcount** | **100+** employees (Aug 2026) — single secondary source |
| **Revenue trajectory** | "scaled revenue 5x over the past six months" (Jul 2025); "fourfold last year… ~3.5x projected this year" (Aug 2026). No absolute ARR disclosed anywhere. |
| **Scale claims** | 500+ live jobsites; >$50B cumulative construction volume; 115,000+ project questions answered |
| **Sells to** | Enterprise **general contractors** first (ENR-Top-400 class), plus specialty/self-perform trades and one multifamily developer-builder (AMLI) |
| **Buyer persona** | VP/Director of Operations Technology, CTO/Chief Innovation, COO — *operations*, not legal/risk/claims |
| **Geography** | United States (all named logos are US; "hundreds of jobsites across the US") |
| **ICP (derived from their own ROI calculator defaults)** | 25 projects/yr · 1.5-yr average duration · **$25M median contract value** · 8% contingency · 200 submittals/project |

Sources:
- https://trunktools.com/resources/company-updates/trunk-tools-closes-40m-series-b-construction-ai-transformation/ (24 Jul 2025)
- https://www.insightpartners.com/ideas/trunk-tools-closes-40m-series-b-to-lead-constructions-ai-transformation/
- https://trunktools.com/about-us/
- https://news.crunchbase.com/venture/carpenter-founder-ai-construction-startup-trunk-tools-buchner/ (18 Aug 2026) — valuation $325M, 100+ headcount, 10+ live agents, 4x/3.5x revenue growth
- https://trunktools.com/roi-calculator/ (ICP defaults)
- https://bricks-bytes.com/ai/trunk-tools-copilot-to-system-of-action/ (15 Jul 2026)

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 The substrate: **Cortex** (launched 17 Jun 2026)
> *"Cortex … reads drawings — not just text — and connects your project data, powering a network of assistants."*

- Two structural components: a **construction ontology** (how submittals, specs, RFIs, drawing details and schedule activities relate) and a **knowledge graph** linking every document/datapoint on a project.
- Trained on **2,000,000+ in-house expert-verified labelled drawing artifacts**; recognises **~400 object types**.
- Benchmark: **97% precision / 90% recall on door detection vs ~26% for frontier general models**.
- Reads across: **drawings, specifications, RFIs, submittals, schedules, contracts, change orders, bids, revision bulletins, meeting minutes, procurement logs, field reports**.
- Buchner (Jul 2026): three tiers — integrations/preprocessing (Cortex) → agent orchestration → agent-to-agent handoff. She killed the old "co-pilot" chat product entirely; everything is now **file-triggered and completes work end-to-end**.
- Evidence: https://cortex.trunktools.com/ · https://trunktools.com/resources/company-updates/trunk-tools-builds-cortex-purpose-built-ai/ (22 Jun 2026) · https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings (17 Jun 2026)

### 2.2 Shipping agents

| Agent | What it does (their words) | Thesis relevance | URL |
|---|---|---|---|
| **TrunkText** (Project Intelligence Agent) | Q&A over "specs, drawings, RFIs, submittals, schedules, and contracts" via **SMS**, mobile and web; cited answers with source highlighting | **HIGH** — this is the evidence-retrieval layer | https://trunktools.com/trunktext/ |
| **TrunkSubmittal** (Submittal Review Agent) | Reads each submittal against specs + RFI responses; classifies Fully / Partially / Non-Compliant; drafts response to trade partner | MEDIUM — compliance evidence trail | https://trunktools.com/trunksubmittal/ |
| **Submittal Register / TrunkRegister** | Reads entire spec book, extracts every submittal directive, writes register back to Procore/Autodesk | LOW-MED — spec obligation extraction | https://trunktools.com/trunkregister/ |
| **TrunkReview** (Drawing Revision Agent) | Compares every sheet of a new bulletin to prior rev; finds **clouded AND non-clouded changes**; writes the change narrative; "**accelerate the change order process**" | **HIGHEST** — this is de-facto scope-change *event detection* | https://trunktools.com/trunkreview/ |
| **TrunkRFI** (RFI Agent) | Watches Procore/Autodesk for draft RFIs; kills duplicates; drafts sourced RFIs; on response, "**summarizes the response and its impact on your project, catches potential conflicts**" and gives a prioritized to-do | **HIGH** — closest thing they have to impact analysis | https://trunktools.com/trunkrfi/ |
| **TrunkBid** (Bid Analysis Agent) | Levels sub bids vs scope; surfaces "gaps, exclusions, alternates, **scope silence**"; cites "25.7% of disputes connected back to scope gaps" | MEDIUM — dispute *prevention*, precon | https://trunktools.com/trunkbid/ |
| **TrunkBrowse** | Click an object on a sheet → its schedule row, spec section by CSI code, its RFIs and submittals, every sheet it appears on. GA **September 2026**. | **HIGH** — the visual surface of the evidence graph | https://trunktools.com/trunkbrowse/ |
| **TrunkSOP** | SOP Q&A over SMS / web / MS Teams; 1,000+ Suffolk users, 100+ jobsites | LOW | https://trunktools.com/resources/case-studies/case-study-suffolk-standardized-field-operations-trunk-tools-sop/ (24 Sep 2025) |
| **Schedule / Look-ahead Agent** | Connects P6 schedule to submittals, RFIs, invoices; flags "potential risks due to missed tasks in relation to other project documents, i.e. overdue Submittals"; CSV look-ahead export. **Still beta as of the 2024 write-up and absent from the 2026 marquee agent list.** | MEDIUM (if real) | https://trunktools.com/resources/product-updates/product-deep-dive-schedule-lookahead-agent-connecting-the-dots-in-construction-scheduling/ (21 Aug 2024) |

### 2.3 **The free AI Contract Review tool** — the single most thesis-threatening artifact I found
`https://trunktools.com/resources/contracts/` (page last-modified 12 Jun 2026)

Positioned as a free, no-account lead magnet: *"AI can handle many tasks for construction teams. Some should be free."* Accepts **AIA, ConsensusDocs, and custom construction contracts up to 100MB**. Two modes:

**Post-signature "Compliance Guide"** — *"Transform contract legalese into an actionable field operations guide"*, covering:
`Notice Deadlines & Methods` · `Submittal Requirements` · `Payment Application Process` · `Schedule Compliance` · `Change Order Procedures` · `Testing & Inspections` · `Safety Requirements` · `Documentation Standards` · `Meeting Cadence` · `Closeout Checklists` · `Insurance Renewals` · `Certified Payroll`
> *"You'll receive a **compliance calendar, critical deadline matrix, delegation chart by role, and warning flags for high-risk provisions**."*

**Pre-signature review across 14 categories:**
`Payment & Retainage Terms` · `Change Order Procedures` · `Delay & Liquidated Damages` · `Indemnification & Liability` · `Insurance Requirements` · `Warranty Obligations` · `Termination Rights` · `Dispute Resolution` · `Bond & Lien Provisions` · `Site Conditions` · `Subcontract Flow-Down` · `Labor Compliance` · `Scope & Precedence` · `Consequential Damages`
> *"You'll receive an executive summary with risk ratings, top issues requiring negotiation, and specific contract language to push back on."*

Caveats that matter: it is **not wired into the platform**. Report links expire in 7 days, contract is "never stored long-term", no account required. This is a marketing instrument and a capability demonstration — *not* a managed clause register that lives alongside project events. But it proves the clause-extraction half of the pipeline is now a free giveaway from a $325M-valuation vendor.

### 2.4 What they explicitly do NOT ship
No claims module. No notice-issuance workflow. No delay/causation analysis. No quantum or recoverable-value estimation. No dispute/claim package. No daily-log agent (Procore/Datagrid has one; Trunk does not). No email ingestion. The words "claim", "entitlement", "notice of delay", "constructive change", "cumulative impact" appear **nowhere** on any product page I read.

---

## 3. CAPABILITY MATRIX (0–3)

| # | Dimension | Score | Justification | Evidence |
|---|---|---|---|---|
| 1 | contract_ingestion | **3** | Contracts named as a first-class pre-processed doc type by TrunkText/Cortex; free tool accepts AIA/ConsensusDocs/custom PDFs to 100MB | https://trunktools.com/trunktext/ ; https://trunktools.com/resources/contracts/ |
| 2 | clause_extraction | **2** | 14 named clause categories extracted with risk ratings — but only in a standalone, ephemeral free tool, not a persistent product module | https://trunktools.com/resources/contracts/ |
| 3 | notice_detection | **1** | Extracts "Notice Deadlines & Methods" from the contract; **no** event-triggered detection that a notice obligation has been activated | https://trunktools.com/resources/contracts/ |
| 4 | deadline_tracking | **2** | Free tool emits "compliance calendar, critical deadline matrix"; Schedule Agent monitors upcoming activities & overdue submittals; TrunkSubmittal tracks >60-day stuck submittals | https://trunktools.com/resources/contracts/ ; https://trunktools.com/trunksubmittal/ |
| 5 | rfi_event_ingestion | **3** | TrunkRFI watches Procore/Autodesk for draft RFIs, searches full RFI history, drafts, submits, analyses responses | https://trunktools.com/trunkrfi/ |
| 6 | email_ingestion | **1** | No email connector on any integration list (Procore, Autodesk, SharePoint, Box, Dropbox, Egnyte, Teams). Agents *draft outbound* emails. One journalist paraphrase says they sit on top of "…and email" — `UNVERIFIED` | https://trunktools.com/ ; https://bricks-bytes.com/ai/trunk-tools-copilot-to-system-of-action/ |
| 7 | daily_report_ingestion | **2** | Homepage says TrunkText pre-processes "meeting notes, field reports"; but there is no daily-log agent or field-report workflow product | https://trunktools.com/ |
| 8 | schedule_integration | **2** | P6 look-ahead agent (beta, 2024); Cortex ingests schedules; TrunkBrowse links objects to schedule rows; Oracle Primavera Cloud listed as an integration on 3rd-party directories | https://trunktools.com/resources/product-updates/product-deep-dive-schedule-lookahead-agent-connecting-the-dots-in-construction-scheduling/ ; https://trunktools.com/trunkbrowse/ |
| 9 | change_order_workflow | **2** | Reads change orders as a document type; TrunkReview claims "70–85% faster path to trade partner coordination, pricing updates, and **change order submission**". No CO log, no COR pricing workflow, no CO approval routing | https://trunktools.com/trunkreview/ ; https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings |
| 10 | claim_identification | **0** | No claims product, language, or workflow anywhere on the site | (absence across https://trunktools.com/product/ and all agent pages) |
| 11 | delay_detection | **1** | Schedule Agent flags "potential risks due to missed tasks"; TrunkRFI mentions "schedule/trade impacts". No delay event detection, no as-planned-vs-as-built | https://trunktools.com/resources/product-updates/product-deep-dive-schedule-lookahead-agent-connecting-the-dots-in-construction-scheduling/ |
| 12 | responsibility_attribution | **1** | Implicit only: TrunkReview surfaces designer-introduced non-clouded changes ("we can tell you exactly what changed, **what the architects are trying to hide**"); TrunkSubmittal attributes non-compliance to the sub. No formal party/fault model | https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings |
| 13 | contemporaneous_evidence_graph | **2** | Cortex knowledge graph links doc→doc→object→spec→schedule row, with 2M+ labels; but it is a *design/scope* graph, not a dated event chronology. They state graph relations like "how might a bulletin relate to a change order request" are "**an area we continue to work on**" | https://cortex.trunktools.com/ ; https://trunktools.com/faq-data-security-and-privacy/ |
| 14 | evidence_completeness | **1** | Completeness checking exists but only against *specs* (TrunkSubmittal) and *scope docs* (TrunkBid "scope silence"). No notion of file completeness for a commercial position | https://trunktools.com/trunksubmittal/ ; https://trunktools.com/trunkbid/ |
| 15 | recoverable_dollar_estimation | **1** | Marketing-level only: ROI calculator estimates contingency reduction; "$10,000+ rework event prevented in 1 of every 5 reviews"; Buchner's ~$60,000 non-clouded-change anecdote. No in-product per-event valuation | https://trunktools.com/roi-calculator/ ; https://trunktools.com/ |
| 16 | claim_package_generation | **0** | Absent | — |
| 17 | notice_drafting | **1** | Drafts RFIs, sub emails, submittal responses — not contractual notices. (Contrast Document Crunch, which explicitly generates "notices") | https://trunktools.com/trunkrfi/ ; https://www.documentcrunch.com/ |
| 18 | schedule_impact_analysis | **2** | TrunkRFI markets "impact analysis for design responses and schedule/trade impacts"; Cortex "analyze how those changes affect related project documentation". No CPM/fragnet modelling evidenced | https://trunktools.com/trunkrfi/ ; https://www.globenewswire.com/news-release/2026/06/17/3313698/0/en/trunk-tools-launches-cortex-to-tackle-construction-s-hardest-ai-problem-drawings.html |
| 19 | procore_integration | **2** | Functionally deep (watches Procore for draft RFIs/submittals/bulletins, writes back) **but politically broken**: API access denied Sept 2025 and **still absent from the Procore Marketplace as of 19 Aug 2026** (455 apps enumerated, zero "trunk") | https://www.enr.com/articles/61789-trunk-tools-removed-from-procore-api-access-groundbreak-attendance-refunded ; https://marketplace.procore.com/sitemap.xml |
| 20 | autodesk_integration | **3** | Autodesk App Store listing v1.0.0 (24 Feb 2026), free, scopes: view/manage/write data on ACC + BIM 360; Autodesk AECO Technology Partner; Forma Build integration launched 12 May 2026; register writes back to Forma | https://marketplace.autodesk.com/apps/e416596b-a570-4073-ae0e-c8e26397d0a3 ; https://www.autodesk.com/integrations/partner/trunk-tools |
| 21 | outlook_gmail_integration | **0** | No Outlook/Gmail connector anywhere. Microsoft **Teams** yes, Outlook no | https://trunktools.com/ ; https://trunktools.com/resources/in-the-news/trunk-tools-announces-integration-with-microsoft-teams/ |
| 22 | mobile_workflow | **3** | SMS-first by design ("text a project-specific phone number"), plus mobile + web apps; 500+ live jobsites; field-user-count-based enterprise deals (Suffolk: 1,500+ field users) | https://trunktools.com/trunktext/ ; https://www.globenewswire.com/news-release/2026/03/04/3249580/0/en/Suffolk-Inks-Enterprise-Agreement-with-Trunk-Tools-Cementing-AI-Partnership.html |
| 23 | audit_trail | **2** | Every answer cites and highlights sources (73% cite ≥2 sources); per-decision confidence scores; SOC 2 Type II; project-level logical isolation. But no legal-grade, exportable chain-of-custody record marketed | https://trunktools.com/trunktext/ ; https://trunktools.com/faq-data-security-and-privacy/ ; https://bricks-bytes.com/ai/trunk-tools-copilot-to-system-of-action/ |
| 24 | portfolio_risk | **1** | "Portfolio Risk" is an *input slider* on the ROI calculator, not an output; TrunkBid mentions portfolio profitability. No portfolio risk dashboard product | https://trunktools.com/roi-calculator/ |
| 25 | performance_pricing_compatibility | **1** | Enterprise seat/project subscription; "seven-figure" agreements. Heavy ROI-proof culture (ROI calculator, "Proof of Value" doc) makes them *culturally* compatible with outcome pricing, but no evidence of any success-fee model | https://www.enr.com/articles/61435-gilbane-rolls-out-trunk-tools-ai-agents-across-its-jobsites ; https://www.autodesk.com/integrations/partner/trunk-tools |
| 26 | consultant_replacement_potential | **1** | Replaces junior PE/APM labour ("gives a PE two months out of school the equivalent of five-plus years"), not claims consultants, delay experts, or construction counsel | https://trunktools.com/trunksubmittal/ |

`SCORES| 3,2,1,2,3,1,2,2,2,0,1,1,2,1,1,0,1,2,2,3,0,3,2,1,1,1`

---

## 4. PRICING

**Published list pricing: none.** Every directory records "Contact vendor" / "Pricing available upon request" (Capterra, Software Advice, GetApp, aec+tech, SoftwareFinder). Confidence in the following: **MEDIUM for the anchor, LOW for the derived unit rate.**

| Evidence | Figure | Source |
|---|---|---|
| Gilbane enterprise agreement | **"seven-figure"**, covering rollout of TrunkSubmittal + TrunkText + TrunkSOP across **200+ projects over two years** | https://www.enr.com/articles/61435-gilbane-rolls-out-trunk-tools-ai-agents-across-its-jobsites (26 Sep 2025) |
| Suffolk enterprise agreement | 1,500+ field users nationwide; **no dollar figure disclosed** | https://www.globenewswire.com/news-release/2026/03/04/3249580/0/en/Suffolk-Inks-Enterprise-Agreement-with-Trunk-Tools-Cementing-AI-Partnership.html (4 Mar 2026) |
| Autodesk App Store connector | **"Free"** (the connector; the platform is licensed separately) | https://marketplace.autodesk.com/apps/e416596b-a570-4073-ae0e-c8e26397d0a3 |
| Value framing they sell against | ROI calculator default scenario returns **$3.6M annual savings / $144,391 per project** on a 25-project, $25M-median portfolio, assuming only TrunkSubmittal + TrunkText | https://trunktools.com/roi-calculator/ |

**Derived unit economics (`UNVERIFIED`, arithmetic only):** if "seven-figure" = $1–3M over 2 years across 200+ projects, that implies roughly **$2,500–$7,500 per project per year**, or a low-six-figure annual enterprise floor. Motion is clearly **land per-project / pilot → expand to enterprise agreement**, with pilots reported at Gilbane (Baird Center), Cleveland Construction, Torcon, Suffolk (via BOOST accelerator, 2023). Pilots are explicitly instrumented for ROI (37 working days, 246 questions, 6.5x labour ROI, 40x with rework) — this company sells on measured proof, which is a useful signal for any startup pricing alongside them.

---

## 5. INTEGRATIONS, API & DATA EGRESS REALITY

**Open / working:**
- **Autodesk** — App Store listing v1.0.0 (24 Feb 2026), works with Autodesk Construction Cloud + BIM 360 + Forma Build; scopes include *view / manage / write data*. Register and RFIs write back. This is now their primary sanctioned platform relationship. https://marketplace.autodesk.com/apps/e416596b-a570-4073-ae0e-c8e26397d0a3
- **Document repositories** — SharePoint, Box, Dropbox (30 Jun 2025), Egnyte, Microsoft Teams.
- **Schedule** — P6 (look-ahead agent); third-party directories additionally list Oracle Primavera Cloud, CMiC and InEight (`UNVERIFIED` against vendor material).

**Closed / broken:**
- **Procore.** In **September 2025 Procore denied Trunk Tools' API access**, and refunded its Groundbreak booth. Procore introduced a new Developer Policy on **30 Sep 2025** whose terms *"state that marketplace partners cannot bulk download data from its platform for commercial purposes, including the training of large language models."* Agave (the integration middleware many contech startups used to reach Procore) told Trunk Tools and others to change practice; Trunk Tools complied in early October, agreed to curtail Agave use, and **still was not granted marketplace status**. Buchner: *"We applied for marketplace status on the day that they alerted us… and every other startup got approved on the marketplace to our knowledge, besides us."* Trunk Tools told customers it would support Agave until 1 Dec and ship a compliant fix, and stated it *"firmly believes your data is yours — no third party should limit your access and use of your own data."* At Groundbreak (14–16 Oct 2025) Procore unveiled **Agent Builder**, a competing natural-language agent beta.
  https://www.enr.com/articles/61789-trunk-tools-removed-from-procore-api-access-groundbreak-attendance-refunded (31 Oct 2025)
- **Independent check, 19 Aug 2026:** I enumerated the Procore Marketplace sitemap — **455 app listings, zero containing "trunk"**, while `document-crunch`, `clearstory`, `datagrid`, `smartpm`, `pype-autospecs` and `newforma-*` are all present. Trunk Tools' product pages still say "push the RFI straight to Procore", so *some* customer-authorised connection evidently persists, but **they are not a sanctioned Procore marketplace partner as of today**. https://marketplace.procore.com/sitemap.xml
- **No public API or developer docs.** `docs.`, `api.`, `developers.trunktools.com` all fail to resolve; robots.txt exposes only a WordPress marketing sitemap. There is no third-party build surface. (Buchner does say enterprise customers now negotiate "API rate limits and MCP limits directly into contracts" — so an MCP surface exists commercially, but nothing is published.)

**Data posture (matters for any partnership):** SOC 2 Type II; CCPA/CPRA; encryption at rest and in transit; **zero-retention, zero-training contracts with every large model provider they use**; customer training data used **only with explicit written permission**, de-identified, with opt-out; each project is a "sealed box". They also have an internal AI Governance Committee.
https://trunktools.com/faq-data-security-and-privacy/ · https://bricks-bytes.com/ai/trunk-tools-copilot-to-system-of-action/

---

## 6. WEAKNESSES AND EXPLICIT GAPS

| Gap | Deliberate or unattended? | Read |
|---|---|---|
| **No claims / entitlement / notice product** | **Deliberate.** They sell to Operations. Buchner's stated purpose is *"If I get to a point where no human has to do data entry anymore into one of these systems of record, I feel like I have achieved my purpose on this earth."* Nothing in that mission points at recovering money from an owner. | The single largest opportunity in the whole competitor set. |
| **No email ingestion (Outlook/Gmail)** | **Unattended.** They connect to every document repository but not to the medium where 70% of commercial correspondence and de-facto directives live. Procore/Datagrid's daily-log agent already ingests "photos, emails, and voice notes". | Real hole; also the cheapest V1 wedge for a solo founder (email forward). |
| **No daily log / diary agent** | Unattended-to-date. Competitors have shipped it. | Contemporaneous record is the backbone of any claim. |
| **Schedule capability is thin and stale** | Looks **unattended**. The Schedule Look-Ahead Agent write-up is from Aug 2024 and marked beta; it is absent from the 2026 seven-agent Cortex lineup. | Without CPM impact they cannot do entitlement. |
| **Procore relationship is severed** | Not deliberate — it was done *to* them. Their mitigation (Cortex as a platform-agnostic layer, Autodesk Forma as the sanctioned home) is deliberate. | Structural fragility for anyone whose data lives in Procore. |
| **No public API/marketplace/developer surface** | Deliberate (enterprise direct-sales motion). | Hard to be their channel; easy to be invisible to them. |
| **Zero independent reviews** | Consequence of enterprise motion. Capterra: "0 user reviews"; Software Advice: "No reviews yet"; SourceForge: 0.0/5, unreviewed; G2 page not reachable. **All published praise is vendor-controlled.** | Their ROI numbers are unaudited by any third party except one customer-commissioned consultant. |
| **Contract capability is a free giveaway, not a product** | Deliberate — it is lead-gen, priced at zero to devalue point solutions. | This is *strategically hostile* to a clause-extraction startup, even though it is technically shallow. |
| **Own-stated cons** | Third-party directory lists cons as *"Works best with curated data only"* and *"Some agents are still limited to beta version only"*. https://softwarefinder.com/construction/trunk-tools | Garbage-in fragility; agent maturity is uneven. |

---

## 7. ADJACENCY TEST — how hard for THEM to ship "event detection → entitlement matching → evidence → claim package"?

### Verdict: **MEDIUM** (technically EASY, organisationally HARD)

**Arguments for EASY:**
- They already do **event detection**: TrunkReview finds non-clouded scope changes and writes the narrative; Buchner cites a $60k electrical change hidden outside a revision cloud. That is *literally* a change-order entitlement trigger.
- They already do **evidence collection with citation**: 73% of answers cite ≥2 sources, source-highlighted PDFs, per-decision confidence scores.
- They already extract **entitlement primitives**: the free contract tool pulls Notice Deadlines & Methods, Change Order Procedures, Delay & LDs, Dispute Resolution, Scope & Precedence.
- Their **knowledge-graph roadmap explicitly names the missing edges**: *"How might a bulletin relate to a change order request? How does a rejected submittal impact the project schedule? This is an area we continue to work on."* (https://trunktools.com/faq-data-security-and-privacy/)
- Shipping cadence is a **new evaluated agent every 4–6 weeks**, and Buchner keeps only a 3-year vision + 3-to-6-month roadmap deliberately so she can absorb whatever becomes possible each quarter.
- They already have contract-grade enterprise data access at Gilbane (200+ projects), Suffolk (1,500+ users), Cleveland Construction, Torcon, HITT, DPR, Harkins, Consigli, McGough, Haskell, AMLI, Charps.

**Arguments for HARD:**
- **GTM motion is wrong.** Every buyer, persona page, testimonial and ROI model is Operations/field productivity. The claims buyer (risk, legal, contracts, the CFO) is a different budget, a different sales cycle, and a different reference set. Their own customer page segments only Superintendent / Project Manager / Executive.
- **Legal exposure appetite is low and getting lower.** An agent that says "you are entitled to $X and here is your notice" creates unauthorised-practice-of-law and professional-liability surface that a $325M venture company with Liberty Mutual on the cap table will avoid. Note their contract tool's design: ephemeral, no account, no storage, no advice — a *deliberately* de-risked artifact.
- **Adversarial positioning breaks the design-team relationship they sell.** Their marketing repeatedly promises the opposite: "protects your reputation with your client and their architect of record", "avoid uncomfortable OAC meetings", "an architect was sufficiently impressed… to recommend Cleveland Construction for another project". A claims product is a direct contradiction of the value proposition.
- **No M&A history.** Zero acquisitions. They build. That means an entitlement capability arrives on their own roadmap clock, not by purchase.
- **Schedule/CPM is their weakest muscle** and entitlement without schedule impact is half a product.
- **Procore data severance** removes the very corpus (COs, prime contract, correspondence, cost) that entitlement work depends on for a large share of the US GC market.

**How we would know they are turning:** watch for (a) a **daily-log or correspondence agent**, (b) an **Outlook/Gmail connector**, (c) the contract review tool moving from `/resources/contracts/` into the authenticated platform with persistence, (d) a **revived, non-beta schedule agent with impact modelling**, (e) any hire with "risk", "claims", "contracts" or "counsel" in the title, (f) the knowledge-graph "bulletin → change order request" edge shipping as a named agent (e.g. "TrunkChange"). Today: **none of these are visible**.

---

## 8. STARTUP POSTURE: **PARTNER** (with a hard clock on it)

Not roadkill — they are not building claims. Not a channel — no API, no marketplace, no partner program. **Partner, asymmetric and time-limited:**

- **Why partner:** They win the retrieval/QA layer at the enterprise GC. A commercial-entitlement product consumes their outputs (change narratives, RFI impact summaries, submittal non-compliance findings, cited source sets) and adds the layer they refuse to build: entitlement matching, causation, quantum, notice. Their own customers (Gilbane, Suffolk) are exactly the accounts where a claims layer has budget.
- **Why the clock matters:** TrunkReview's own tagline is "70–85% faster path to … change order submission". They are one product decision away from owning the front half of the pipeline. And their free contract tool has already published the clause taxonomy a startup would have charged for.
- **The defensible ground:** entitlement *reasoning* (clause → event → obligation → remedy), causation and delay quantum, contemporaneous chronology across email and daily logs, dollarisation, and the notice/claim artifact with its legal posture. None of that is on their roadmap; all of it is outside their risk appetite.
- **The asymmetric advantage a solo founder has over them right now:** Trunk Tools *cannot* read the Procore corpus through a sanctioned channel and has no email connector. A file-upload / email-forward / customer-authorised-export V1 has, paradoxically, **better commercial-record coverage than the $70M incumbent**.
- **Practical partnering path:** go via **Autodesk** (their sanctioned platform) or via joint accounts where they own field QA and you own the commercial file. Do not build anything whose core value is "ask a question of the project documents" — that is priced at zero by them and by Procore.

---

## 9. TOP 5 VERBATIM COMMENTS RELEVANT TO THE THESIS

There are **no independent review-site reviews** of Trunk Tools (Capterra: 0; Software Advice: none; SourceForge: unreviewed; G2 unreachable; Reddit not fetchable from this environment). The following are the closest available verbatim signals — note that 1–3 are vendor-published and must be discounted accordingly.

1. **On non-clouded change → change order (the entitlement moment):**
> *"I had a situation where, through the use of TrunkReview, [we realized] there was an entire room added inside a mechanical room. Our drywall contractor sent us a change order, and I noticed that this was added. So I asked him: did you pick up the fact that you have a new small room with ceiling grid and tile? And they said: oh no, I didn't catch that, that wasn't clouded."* — Josue Paredes, Senior Project Manager, HITT. https://trunktools.com/trunkreview/

2. **On design-team-introduced change (adversarial framing, from the CEO):**
> *"We can tell you exactly what changed, what the architects are trying to hide."* — Dr. Sarah Buchner, on revised drawing sets; she cited an electrical issue outside a revision cloud carrying ~**$60,000** in project impact. https://www.enr.com/articles/63178-trunk-tools-launches-cortex-ai-platform-to-interpret-construction-drawings (17 Jun 2026)

3. **On what the RFI product actually replaces:**
> *"Too many responses like 'Did you actually read the contract documents?' strain the relationship with design teams and your customer and diminishing your likelihood of winning repeat work."* — TrunkRFI executive-persona page. This is the anti-claims worldview stated plainly. https://trunktools.com/trunkrfi/

4. **On the platform-dependency risk (the CEO, publicly):**
> *"We applied for marketplace status on the day that they alerted us, which was a few weeks before Groundbreak and every other startup got approved on the marketplace to our knowledge, besides us."* — Dr. Sarah Buchner. https://www.enr.com/articles/61789-trunk-tools-removed-from-procore-api-access-groundbreak-attendance-refunded (31 Oct 2025)

5. **Third-party stated limitations:**
> Cons: *"Works best with curated data only"*; *"Some agents are still limited to beta version only."* — SoftwareFinder product listing. https://softwarefinder.com/construction/trunk-tools

*(Bonus, from the market's referee: an independent consultant contracted by a Trunk Tools customer compared Trunk Tools with Procore Assist across 700+ questions and concluded Trunk Tools was "**statistically overwhelming and technically meaningful superiority**". Vendor-published, customer-commissioned — treat as marketing, but note it exists and that Procore is now the benchmark they measure against. https://trunktools.com/trunktext/)*

---

## 10. HARDEST FACTS

1. **$40M Series B led by Insight Partners closed 24 Jul 2025; ~$70M raised total; reported $325M valuation and 100+ headcount as of Aug 2026.** https://trunktools.com/resources/company-updates/trunk-tools-closes-40m-series-b-construction-ai-transformation/ · https://news.crunchbase.com/venture/carpenter-founder-ai-construction-startup-trunk-tools-buchner/
2. **Gilbane signed a "seven-figure" enterprise agreement to roll TrunkSubmittal/TrunkText/TrunkSOP across 200+ projects over two years; on the first 30 projects, 72% of submittals were non-compliant, 25% partially compliant, 3% fully compliant, and cycle times fell ~50%.** https://www.enr.com/articles/61435-gilbane-rolls-out-trunk-tools-ai-agents-across-its-jobsites (26 Sep 2025)
3. **Procore denied Trunk Tools API access in Sept 2025 and refunded its Groundbreak booth; Procore's new Developer Policy (30 Sep 2025) bans bulk data download for commercial purposes including LLM training. As of 19 Aug 2026 Trunk Tools is absent from all 455 Procore Marketplace app listings, while Document Crunch, Clearstory, Datagrid and SmartPM are present.** https://www.enr.com/articles/61789-trunk-tools-removed-from-procore-api-access-groundbreak-attendance-refunded · https://marketplace.procore.com/sitemap.xml
4. **Cortex is trained on 2,000,000+ expert-verified drawing labels across ~400 object types, scoring 97% precision / 90% recall on door detection versus ~26% for frontier general models; 35,000 submittal reviews to date with median first-pass review of 3.92 minutes and median cycle time cut 74% (54.8 → 14.0 days).** https://cortex.trunktools.com/ · https://trunktools.com/resources/company-updates/trunk-tools-builds-cortex-purpose-built-ai/ (22 Jun 2026)
5. **Trunk Tools publishes a free, no-account AI contract review tool that extracts "Notice Deadlines & Methods", "Change Order Procedures", "Delay & Liquidated Damages" and "Dispute Resolution" across 14 categories and returns "a compliance calendar, critical deadline matrix, delegation chart by role, and warning flags for high-risk provisions."** https://trunktools.com/resources/contracts/ (page updated 12 Jun 2026)

Runner-up hard facts worth keeping: Suffolk enterprise agreement across **1,500+ field users** (4 Mar 2026); **500+ live jobsites / 115,000+ questions / 34.6 min average saving per question / 73% of answers citing ≥2 sources**; Gilbane Baird Center pilot on a **$456M** project — 33.7 GB / 20.6K documents / 246 questions / 37 working days / 87% correctness / **6.5x labour ROI, 40x including rework**; Procore acquired agentic-AI vendor **Datagrid on 20 Jan 2026** and shipped five prebuilt agents — including a **contract review agent** — on 21 May 2026.

---

## 11. UNKNOWNS (and what would settle each)

| Unknown | What would settle it |
|---|---|
| Absolute ARR / customer count | Insight Partners portfolio disclosure, a Series C filing, or a credible ARR figure in a founder interview. Only growth multiples are public. |
| Whether the Procore connection is restored, and on what basis | A Procore Marketplace listing appearing; a Trunk Tools statement post-1 Dec 2025 (the fix deadline they gave customers); or the "long-term fix" they promised, which I could not locate. |
| Whether "custom agents" can be configured by customers for contract review / delay notices | One third-party directory summary implied customer-configurable agents including "contract reviews, delay notices"; I could **not** corroborate this on any Trunk Tools page. A product demo or the authenticated app would settle it. |
| Whether the Schedule/Look-Ahead Agent is still alive | It is absent from the 2026 Cortex agent lineup. A pricing sheet, a demo, or a 2026 product page would settle it. |
| Real per-project / per-seat price | An RFP response, a public-sector procurement award, or a reseller quote. |
| Independent user sentiment | No G2/Capterra/Software Advice reviews exist; Reddit was not fetchable from this environment. A manual Reddit/LinkedIn sweep is required. |
| Whether an MCP/API surface exists commercially | Buchner says enterprise customers write "API rate limits and MCP limits" into contracts, implying a private surface. A customer contract or a partner brief would settle it. |
| Acquisition status | Buchner declined to comment on two years of acquisition rumours in Jul 2026, saying she is "sharpening the skill" of building a standalone company. |

---

# PART II — CATEGORY SURVEY
## "AI document intelligence for construction" — every credible player found

Discovery method: Trunk Tools' own competitive references, ENR/VentureBeat/Bricks&Bytes coverage, CB Insights competitor set, the **full 455-app Procore Marketplace sitemap**, the Autodesk App Store, and direct site verification. Entries marked `UNVERIFIED` were seen only in a directory listing and not verified against the vendor's own site.

### A. Direct analogues — document/drawing intelligence + agents for contractors

| Company | One line | URL |
|---|---|---|
| **Trunk Tools** | Cortex knowledge graph + 7–10 agents (TrunkText/Submittal/Review/RFI/Bid/Register/Browse/SOP) over drawings, specs, RFIs, submittals, schedules, contracts | https://trunktools.com |
| **Document Crunch** | The closest thing to the thesis in market: CrunchAI reads contracts, specs and addenda for risk, and "Project Assist" generates **reviews, submittals, notices and RFIs**; 500+ companies, tagline *"Every dispute started somewhere. It was probably page 47."* | https://www.documentcrunch.com |
| **Datagrid (a Procore Company)** | Agentic AI — Deep Search, Submittal Review, RFI and Daily Log agents across 40+ tools; **acquired by Procore 20 Jan 2026**, founder Thiago Da Costa now Procore SVP of AI & Data | https://www.datagrid.com |
| **Procore (AI Agents / Agent Builder)** | The platform itself now ships five prebuilt agents — deep search, submittal review, RFI, daily log and a **contract review agent** that flags liability language — launched 21 May 2026 | https://www.procore.com |
| **Autodesk (Forma Build, Pype AutoSpecs / Pype Closeout)** | Spec parsing, automated submittal register, closeout doc automation embedded in ACC; Trunk Tools' sanctioned host platform | https://construction.autodesk.com · https://marketplace.procore.com/apps/pype-autospecs |
| **Primepoint** | *"Construction intelligence, built on drawings"* — Connected Documents, Constructability Review, Submittal Review, **Revision Narrative**, RFI Assistant, Schedule Assistant, and "Ask Marvin" Q&A; ~$10M seed, ex-Meta founders | https://www.primepoint.ai |
| **Constructable** | AI-native PM platform with AI Search over plans/photos/docs with citations, "Magic Extractor" table/text extraction, submittal pre-check, AI punch list | https://www.constructable.ai |
| **Civils.ai** | AI takeoff plus **specification and contract checking** and geotechnical/borehole extraction; 200+ firms across 8 countries incl. AECOM, Arup, Jacobs, WSP, Kajima | https://civils.ai |
| **Togal.AI** | AI drawing takeoff (claimed up to 98% accuracy on floor plans) plus **Togal.CHAT** conversational plan Q&A | https://www.togal.ai |
| **Part3** | Construction administration for architects/engineers — submittals, RFIs, **change orders**, field reports with AI-automated document review | https://www.part3.io |
| **Morta** | Connected project-controls / document-control layer replacing spreadsheet workflows across CDEs, ERPs and programme tools; published pricing from £100/paid user/month | https://www.morta.io |
| **Newforma (Project Center / Konekt)** | Long-standing project information management and email/correspondence record-keeping for AEC; in the Procore Marketplace | https://www.newforma.com |
| **Bluebeam** | PDF/drawing markup incumbent; "Bluebeam for Submittals" and Bluebeam on the Web in the Procore Marketplace; publishes construction-AI commentary | https://www.bluebeam.com |
| **BuildCognition** | "Construction Quality Automation Platform" (Procore Marketplace listing) `UNVERIFIED` beyond listing | https://marketplace.procore.com/apps/buildcognition |
| **Drawing Change A.I. & Drawing Management** | "Seamless Tracking of All Drawing Changes" — a direct point competitor to TrunkReview (Procore Marketplace) `UNVERIFIED` beyond listing | https://marketplace.procore.com/apps/drawing-change-a-i-drawing-management |
| **Firmus RFI Connector** | "RFI's Simplified" — RFI automation in the Procore Marketplace `UNVERIFIED` beyond listing | https://marketplace.procore.com/apps/firmus-rfi-connector |
| **NYFTY.AI** | "Does the work you hate" — AI field automation (Procore Marketplace) `UNVERIFIED` beyond listing | https://marketplace.procore.com/apps/nyfty-ai-field-automation |
| **ConstructivIQ** | "Intelligent Procurement Planning" — spec/submittal-driven procurement AI `UNVERIFIED` beyond listing | https://marketplace.procore.com/apps/constructiviq |
| **ConTech by MindPal / Planaut / Space AI / KonstructIQ / ConWize** | Small vendors listed as Trunk Tools alternatives (blueprint analysis, RFI routing, scope/schedule extraction from documents, estimating) — all `UNVERIFIED`, low-signal | https://sourceforge.net/software/product/Trunk-Tools/ |

### B. Commercial / entitlement adjacency (the half Trunk Tools does not build)

| Company | One line | URL |
|---|---|---|
| **Clearstory** | Change-order and T&M communication network — live shareable COR log, photo-backed T&M tags, real-time allowance/contingency balances, "Clearstory AI"; 14,000+ contractors, **$2.1B in CORs shared monthly**. **Extracker.com now 301-redirects to Clearstory** (consolidation of the two COR-communication players) | https://www.clearstory.build |
| **SmartPM** | Automated CPM schedule analytics on P6/MS Project — SPI, critical-path history, compression, completion forecasting; the closest thing to delay-analysis-as-software in the marketplace | https://smartpm.com |
| **Document Crunch** | (see above) — the only vendor found that explicitly generates **notices** from contract obligations | https://www.documentcrunch.com |

### C. Adjacent AI but not document intelligence (named for completeness; do not confuse with the category)
Reality capture / progress AI: **Buildots**, **Doxel**, **OpenSpace**, **Disperse**, **Reconstruct**, **Track3D**, **HoloBuilder/Sphere XG**, **Multivista**, **Versatile**, **Contilio**, **Foresight**, **Augrade**, **Dalux**. Safety AI: **Newmetrix (fka Smartvid.io)**, **Kwant**. Materials/procurement: **Kojo**, **Field Materials**, **StructShare**. Scheduling: **ALICE Technologies**, **nPlan**, **Touchplan**, **Planera**, **Outbuild**. (Sources: Procore Marketplace app enumeration; https://www.cbinsights.com/company/trunk-tools competitor set.)

### D. Category read
1. **The document-QA layer is being commoditised from three directions at once**: Procore ships it natively (post-Datagrid), Autodesk ships it natively (Pype + Forma), and Trunk Tools gives away contract review for free. Any startup whose core promise is "ask your project documents a question" is entering a knife fight against three parties who will price it at zero.
2. **Nobody in the category has crossed from *information* to *entitlement*.** Document Crunch is the only one at the boundary (it generates notices), and it approaches from the contract side, not the event side. No player found does causation, delay quantum, recoverable-value estimation, or claim-package assembly.
3. **Platform gatekeeping is now the dominant strategic risk in this category.** Procore's Sept 2025 Developer Policy plus its Datagrid acquisition plus its own agent suite is a textbook platform squeeze, and Trunk Tools — the best-funded independent — is the demonstrated casualty. Any thesis that depends on reading a GC's Procore corpus through a vendor API is building on rented land; customer-authorised export, email forward, and file upload are the durable ingest paths.
