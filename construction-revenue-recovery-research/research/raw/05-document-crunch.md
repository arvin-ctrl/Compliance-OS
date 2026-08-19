# 05 — DOCUMENT CRUNCH (a Trimble company)
### Deep competitive assessment against the construction revenue-recovery thesis
Research date: **19 August 2026**. All URLs fetched on that date unless noted.

> **Headline for the orchestrator:** Document Crunch has moved *deep* into the construction phase — but as a **document-comprehension and document-generation** company, not a **project-monitoring** company. They already ship contract-aware **notice drafting** (Notice Builder / Project Assist). They ship **nothing** that watches a project for events, matches events to entitlements, assembles contemporaneous evidence, or quantifies recoverable dollars. The hardest single proof: their Procore app requests **zero data permissions** (`permissions: {"company": {}, "project": {}}`) and is a `sidepanel`-only embed. They read documents you upload. They do not read your project.
>
> **And the biggest change since the last time anyone looked: Trimble acquired them (announced 2 Apr 2026, closed Q2 2026).** That removes the data-access constraint that has shaped their product for seven years.

---

## 1. SNAPSHOT

| Field | Value | Source |
|---|---|---|
| **What it is** | "AI Risk Intelligence Platform Built for Construction." Three named layers: **CrunchAI** (find risk), **Project Assist** (act on it), **Platform** (align teams). | [documentcrunch.com](https://www.documentcrunch.com/) |
| **Founded** | 2019; first user logged in November 2019 | [/our-story](https://www.documentcrunch.com/our-story), [/blog/why-we-crunch](https://www.documentcrunch.com/blog/why-we-crunch) |
| **HQ** | 3000 Summit Place Ste. 200, Alpharetta, GA 30009. Second hub: Austin, TX. 16,000 sq ft HQ opened 2025. | [/careers](https://www.documentcrunch.com/careers), [Inc. 5000 PR](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies) |
| **Legal entity** | Document Crunch, LLC (security questionnaire) / Document Crunch, Inc. (marketplace "built by") | [Procore Marketplace listing JSON](https://marketplace.procore.com/apps/document-crunch) |
| **Ownership** | **Acquired by Trimble Inc.** Announced 2 Apr 2026; expected close Q2 2026; now branded "Document Crunch, A Trimble Company." Reports into Trimble's **AECO** segment. Terms undisclosed. | [Trimble IR](https://investor.trimble.com/news/news-details/2026/Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem/default.aspx), [news.trimble.com 2026-04-02](https://news.trimble.com/2026-04-02-Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem) |
| **Total funding pre-acquisition** | **$38M** across ~4 rounds. Seed → $9M Series A (Feb 2024, led Navitas Capital) → $21.5M Series B (Oct 2024, led Titanium Ventures). CB Insights lists $37.1M. | [Series A PR](https://www.documentcrunch.com/news/series-a), [Series B PR](https://www.documentcrunch.com/news/series-b), [Inc. 5000 PR](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies), [CB Insights](https://www.cbinsights.com/company/document-crunch) |
| **Investors** | Navitas Capital, Titanium Ventures (Yash Patel on board), **Nemetschek Group** (owner of Bluebeam), **Trimble** (strategic, invested at Series A — then acquirer), Fifth Wall, Ironspring Ventures, Zacua Ventures, Argonautic Ventures, Andres Construction, Satterfield & Pontikes, Holt Ventures | [Series B PR](https://www.documentcrunch.com/news/series-b), [Series A PR](https://www.documentcrunch.com/news/series-a) |
| **Headcount** | **30 → 90+ in the 12 months to Aug 2025** ("tripled our team since early 2024"). No current figure post-acquisition. | [Inc. 5000 PR, 12 Aug 2025](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies) |
| **Scale** | **10,000+ customer projects**; **500+ contractors**; **$380B+ annual construction volume** (Trimble Marketplace, Aug 2026 — up from "$350B" in the June 2026 PR); **400+ customers** and **6,000+ projects on Playbooks** as of Aug 2025 | [Trimble Marketplace listing](https://marketplace.trimble.com/en-US/apps/572173/document-crunch), [June 2026 platform PR](https://www.documentcrunch.com/news/document-crunch-launches-constructions-first-project-level-ai-risk-intelligence-platform), [Inc. 5000 PR](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies) |
| **Growth** | Inc. 5000 2025 **#311** overall, **#29 in Software**, **#10 in Atlanta metro**; "nearly tripled our revenue each of the last three years" | [Inc. 5000 PR](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies) |
| **ICP** | General contractors and specialty/trade contractors primarily; also owners, designers, insurance carriers, sureties, brokers, law firms, material suppliers | [/general-contractors](https://www.documentcrunch.com/general-contractors), [/subcontractors](https://www.documentcrunch.com/subcontractors), [/construction-insurance-sureties](https://www.documentcrunch.com/construction-insurance-sureties) |
| **Geography** | Procore app: **United States, Canada, EMEA (UK, UAE)**. Trimble listing: **US, Canada**. June 2026 platform launch: "available in the United States and Canada." Data processing: **United States only**. | [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch), [Trimble listing](https://marketplace.trimble.com/en-US/apps/572173/document-crunch) |
| **Named customers** | Balfour Beatty, Barton Malow, DPR, Swinerton, Webcor, Boldt, Haskell, PCL, Hathaway Dinwiddie, Hawaiian Dredging, Kaufman Lynn, Commodore Builders, E-J Electric, Walbridge, XL Construction, McCownGordon, Hill & Wilkinson, BOND, Big D Construction, Ben Hur, Bonland, S.P. McCarl, OE Construction, Marksmen, Blois, Grycon, Dant Clayton, C&S Companies, MBP, John W. McDougall, Level 10, Shawmut, Pioneer, American Global, Andres Construction, Press Mechanical, Silicon Valley Mechanical | [homepage](https://www.documentcrunch.com/), [/customer-stories](https://www.documentcrunch.com/customer-stories) |
| **Founders** | **Josh Levy** (CEO) — construction attorney; private practice, then in-house counsel at an ENR Top 50 GC (**J.E. Dunn**, per his 2026 webinar bio), then commercial contracts lead at an international EPC renewables contractor. **Adam Handfinger** — construction lawyer, managing partner of a national construction law firm's Miami office (Peckar & Abramson), national Executive Committee. **Adam Nadler** — serial entrepreneur. | [/blog/why-we-crunch](https://www.documentcrunch.com/blog/why-we-crunch), [webinar bio](https://www.documentcrunch.com/events/risk-intelligence-for-construction) |
| **Other key staff** | Chris Brunner, VP Product (ex-McKinsey); Trent Miskelly, COO/CTO | [webinar bio](https://www.documentcrunch.com/events/risk-intelligence-for-construction) |
| **Model stack** | Frontier models from **OpenAI and Anthropic**, proprietary models, purpose-built retrieval (RAG), patented pre-processing. Sub-processors declared to Procore: **AWS, Zuva, OpenAI, Anthropic**. Model-routing: "benchmarks leading models and routes each task to the best-fit LLM." | [Series A PR](https://www.documentcrunch.com/news/series-a), [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch), [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| **Security** | SOC 2 Type II, MFA, SAML SSO (Microsoft), AES-256 at rest, TLS 1.2+, no third-party model training on customer data | [/security](https://www.documentcrunch.com/security), [trust.documentcrunch.com](https://trust.documentcrunch.com/) |

### The founding story matters for this thesis
Levy and Handfinger are **claims lawyers who deliberately built the prevention product, not the claims product.** From their own blog:

> "Adam and Josh had personally been involved in **hundreds of millions of dollars worth of claims** over a decade in the business. In every single one of them, mismanagement of the contract was a factor." — [/blog/why-we-crunch](https://www.documentcrunch.com/blog/why-we-crunch)

> "Josh worked at large, well-staffed GCs… and often still had to hire Adam's team for contract help to review mountains of documents and **support project claims**." — same source

They saw the claims market from the inside and chose to go upstream. Their vision statement is literally **"A construction industry with zero disputes"** ([/our-story](https://www.documentcrunch.com/our-story)). This is the single most important strategic fact in this report — see §7 and §12.

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

The platform was re-architected and re-launched **9 June 2026** as three named layers. Prior module names (Risk Review, Checklists, Playbooks, Chat, Notice Builder, "Compliance Copilot") have been folded into these.

> **Note on "Compliance Copilot":** I could find **no evidence that Document Crunch has ever shipped or marketed a product named "Compliance Copilot."** No hit on their site, sitemaps (all 8 fetched), news archive (95 press items), blog archive (82 posts), or marketplace listings. Their project-execution product line was named, in sequence: *Project Playbooks / Checklists / Chat* (2024–2025) → **Project Assist** (June 2026). Treat "Compliance Copilot" as a mis-attribution. `UNVERIFIED` / likely nonexistent.

### 2.1 CrunchAI — the reading layer
| Capability | Evidence |
|---|---|
| Reads **contracts, specs, addenda, flow-downs, drawings, insurance policies, safety manuals, geotechnical reports, RFPs, subcontracts, NDAs** | [Product brochure PDF, Jun 2026](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf); [/construction-contract-review](https://www.documentcrunch.com/construction-contract-review); [Hill & Wilkinson case study](https://www.documentcrunch.com/case-studies/hill-wilkinson) |
| Cross-document reasoning — "the spec contradicts the contract, the addendum changed the LDs, the flow-down shifted liability" | [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| Every answer cited to **page + clause + source text** | [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| Self-verification before answering ("looks for what supports it and what contradicts it") | [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| Multi-model routing, always-current models | [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| **ConstructBench** — internal benchmarking/validation system; a public benchmarking product is teased but **not yet released** ("We're working on something exciting for the industry, but until then…") | [/constructbench](https://www.documentcrunch.com/constructbench), [/construction-contract-review](https://www.documentcrunch.com/construction-contract-review) |

**Critical scope statement, verbatim from the brochure:** *"Reads the full project, not one document at a time. **Contracts, specs, addenda, flow-downs together.** The conflict that costs you lives between them."*

That list is exhaustive and it is entirely **static project documents**. No RFI log, no daily report, no email, no schedule file, no meeting minutes, no photos.

### 2.2 Project Assist — the acting layer (the agentic layer)
| Capability | Evidence |
|---|---|
| Chat/Q&A across the whole project document set | [Product brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| **Auto-generate: redlines, submittals, notices, RFIs** as .xlsx / .pdf / .docx | [June 2026 PR](https://www.documentcrunch.com/news/document-crunch-launches-constructions-first-project-level-ai-risk-intelligence-platform); [Product brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| **Generate submittal logs, risk registers, and notices** "so critical obligations are seamlessly carried into execution" | [June 2026 Community Demo webinar](https://www.documentcrunch.com/events/june-community-demo-new-document-crunch-platform) |
| Version compare with risk analysis; auto-apply your risk tolerance to redlines | [Product brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| Identify scope gaps / conflicts "before they become RFIs, change orders, or disputes" | [Product brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |

### 2.3 Notice Builder — **the single feature that overlaps the thesis**
Launched **21 Oct 2024**, Procore-first. This is the closest thing anyone has built to the thesis' "notice drafting" step. Full mechanics, from their own blog:

> **Step 1: Create & Save a New Notice.** "First, in Situation Details, **you'll select the event type then describe what's going on and the relevant date.** Second, in Potential Impacts, **you'll select what's been impacted**: scope, schedule, and/or cost… Third, in Next Steps, **you'll explain** what actions have already been taken…"
>
> **Step 2:** "Document Crunch will reference the contract for the project and draft a notice that meets those contract requirements… will indicate where you need to edit and fill in additional details like extra dates or backup requirements."
>
> **Step 3:** "**Once the notice is ready, use your playbook or chat to find your submission instructions.** Use the event type's relevant playbook topic to find the relevant notice timing, and the Notices – Where and How section to find out if or how your contract specifies notices must be sent…"
>
> **Step 4:** "If you've put the notice into the **Emails tab**, you can track it on the Correspondence screen."
> — [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder)

**Read that carefully. Every input is typed by the human.** The AI's job begins *after* a person has already (a) noticed the event, (b) classified it, (c) dated it, (d) judged its impacts, and (e) decided a notice is warranted. And in Step 3 the *deadline* is not tracked or surfaced — the user must go **look it up** in the playbook.

Marketing language around it — worth quoting because it is the closest they come to the thesis pitch:

> "Make Sure Notices Never Lose You Money… With a comprehensive and correct notice that's been submitted the way the contract says, contractors have a much easier time **getting the entitlements they deserve** to complete a project." — [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder)

> Webinar agenda item: "**How the notice builder reduces disputes and missed claims**" — [/events/notice-builder-webinar](https://www.documentcrunch.com/events/notice-builder-webinar)

> Josh Levy's origin anecdote for the feature: "the owner's rep told the Project Executive… 'Don't worry about it. We got you. You don't give notice…' The owner's rep was later terminated and the owner refused to recognize that we were due delays because we didn't give notice per the terms of the contract. **That cost us millions of dollars in liability.**" — [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder)

### 2.4 Project Playbooks — contract → operational reference artifact
Launched **July 2024**; **6,000+ projects** using it by Aug 2025. The Playbook is an AI-generated, customizable operating manual derived from the contract. Its published table of contents includes, verbatim:

- **Change Management**: Change orders · **Notices – when, where, and how to send them** · Delays, Compensation, Remedies, Limitations · Material price escalation · Unforeseen conditions · Hazardous materials · Weather delays
- **Financial Management**: Progress payments · Final payment · Retainage · Contingencies · Allowances · Audits · Savings
- **Project Execution**: Parties · Designated representatives · Duration for performance · Initial schedule requirements · Completion milestones · Order of precedence
- Legal Procedures: audit rights · **"When do notice letters need to be sent?"** · **"How do notice letters need to be sent?"**
— [/blog/project-playbooks, 29 Jan 2025](https://www.documentcrunch.com/blog/project-playbooks)

**This is the strongest notice-requirement *extraction* in the market.** It is a reference document, not a clock.

### 2.5 Audience-specific packaging
| Segment | Page | Revenue-recovery-relevant language |
|---|---|---|
| **General contractors** | [/general-contractors](https://www.documentcrunch.com/general-contractors) | Framed entirely as review speed, team enablement, PM onboarding. No claims/notice language. |
| **Specialty/sub contractors** | [/subcontractors](https://www.documentcrunch.com/subcontractors) | *"**Compliance and change orders fall through the cracks impacting revenue**, with no scalable way to grow… Solution: We transform contract compliance and change order management for teams of all sizes."* — closest sub-facing revenue claim |
| **Execution phase** | [/construction-execution-solutions](https://www.documentcrunch.com/construction-execution-solutions) | Checklists, Playbooks, Explain, Chat. *"Stay Compliant with real-time answers about safety obligations, submittal processes, or **change order procedures**"* |
| **Insurers / sureties** | [/construction-insurance-sureties](https://www.documentcrunch.com/construction-insurance-sureties) | Pre-bind underwriting: "Identify exposures that could lead to higher claims," "Identify contractual red flags that could lead to bond claims." **Pre-bind only — no claims handling.** |
| **Owners / designers** | referenced in Trimble PR + platform FAQ | *"we also serve Specialty Contractors, Owners, Insurers, Attorneys"* — no dedicated page |

### 2.6 Their own marketing on "getting paid" / claims / entitlement — verbatim
This is where the thesis and Document Crunch touch most closely. They describe the pain **precisely** and then prescribe an upstream fix:

> "Project managers learned too late that **notice windows had already closed, converting otherwise valid claims into absorbed costs.**"
> — [Executive Brief: Post-Award Fee Erosion, 14 Jan 2026](https://www.documentcrunch.com/blog/causes-of-post-award-fee-erosion-in-construction)

> Their named "7 Most Common Causes of Post-Award Margin Erosion": Uncapped Liquidated Damages · Payment Terms That Erode Working Capital · Change Order Markup Ambiguity · Consequential Damages Left Unaddressed · **Notice Requirement Failures** · Contingency Rights Confusion · Insurance Requirements Underestimated at Bid — same source

> An operations leader they quote: *"We're identifying risks and then watching project teams step on the same landmines because nobody briefed them."* — same source

> Their prescribed remedy list — note that **every item is upstream of the event**: "Making contract risk visible beyond legal · Translating contract terms into executable operational guidance · Standardizing risk assessment across projects · **Transferring knowledge before execution begins** · Applying governance based on risk materiality" — same source

> "Project teams are responsible for ensuring compliance with contract obligations throughout the project lifecycle, including managing changes, obtaining and executing lien waivers, **issuing necessary notices** and handling payments." — [/blog/ai-for-project-compliance](https://www.documentcrunch.com/blog/ai-for-project-compliance)

> "Whether the contract is favorable or not, strict adherence is necessary to **maximize entitlements** and minimize risks." — same source

> Positioning: *"Every dispute started somewhere. It was probably page 47."* / *"**Disputes aren't a cost of construction. They're a cost of unmanaged risk.**"* — [homepage](https://www.documentcrunch.com/)

**Nowhere on any Document Crunch property did I find:** a dollar-recovery claim, a claim-package feature, an entitlement-quantification feature, a delay-analysis feature, a "we recovered $X for customer Y" case study, or any pricing tied to recovery.

---

## 3. CAPABILITY MATRIX (0–3)

| # | Dimension | Score | Justification | Evidence |
|---|---|---|---|---|
| 1 | contract_ingestion | **3** | Core competency. Contracts, subcontracts, specs, addenda, flow-downs, drawings, insurance policies, safety manuals, geotech reports, RFPs. Patented pre-processing. | [brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| 2 | clause_extraction | **3** | Best-in-class and evidenced: clause-level citation always-on, cross-document reasoning, ConstructBench validation, risk-tolerance-aware. | [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| 3 | notice_detection | **2** | Strong on **notice-requirement extraction** (Playbook: "Notices – when, where, and how to send them"). **Zero** on detecting a real-world event that triggers a notice — Notice Builder requires the human to select the event type and type the description. | [/blog/project-playbooks](https://www.documentcrunch.com/blog/project-playbooks), [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder) |
| 4 | deadline_tracking | **1** | Marketing claims it ("helps you track obligations and **manage deadlines**"), but no named feature, no date-driven alerting, no countdown. Notice Builder Step 3 tells the user to go *look up* the timing in the playbook. Homepage "open, overdue, done" refers to **internal review-task assignment**, not contractual deadlines. | [/construction-contract-review](https://www.documentcrunch.com/construction-contract-review), [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder), [homepage](https://www.documentcrunch.com/) |
| 5 | rfi_event_ingestion | **1** | Adjacent-only. They **generate** RFIs. They do not read your RFI log: the Procore app is `sidepanel`-only with **empty permissions**; it merely *renders beside* the RFI tool. | [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch) |
| 6 | email_ingestion | **0** | Absent. Notice Builder's email step is literally "copy and paste it into the Emails tab." No Outlook/Gmail connector anywhere. | [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder) |
| 7 | daily_report_ingestion | **0** | Absent. No mention of daily reports/logs on any page, PR, blog, webinar, or marketplace listing. | site-wide search of 8 sitemaps |
| 8 | schedule_integration | **1** | Adjacent-only. Extracts *contractual* schedule terms (milestones, duration for performance, initial schedule requirements) into the Playbook. No P6/MSP/Asta ingestion; no schedule file support. Side panel renders on Procore's Schedule tool but reads nothing. | [/blog/project-playbooks](https://www.documentcrunch.com/blog/project-playbooks), [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch) |
| 9 | change_order_workflow | **1** | Extracts CO clauses, markups, approval timelines, backup requirements into the Playbook and explicitly markets "change order management" to subs. No CO/PCO creation, no log, no routing, no pricing. Their own CO blog prescribes a *manual weekly PCO log*. | [/blog/change-order](https://www.documentcrunch.com/blog/change-order), [/subcontractors](https://www.documentcrunch.com/subcontractors) |
| 10 | claim_identification | **0** | Absent by design. Brand is "zero disputes"; disputes are framed as a **failure to prevent**, never as an asset to pursue. No feature identifies a claim. | [homepage](https://www.documentcrunch.com/), [/our-story](https://www.documentcrunch.com/our-story) |
| 11 | delay_detection | **0** | Absent. Delay is a category the *user* selects in Notice Builder. Playbook covers "Weather delays / Delays, Compensation, Remedies" as **contract clauses**. Nothing detects a delay. | [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder) |
| 12 | responsibility_attribution | **1** | Contractual allocation only: "reinforce roles, responsibilities and limitations," "identify scope gaps," "the flow-down shifted liability." No factual fault attribution for a specific event. | [/construction-execution-solutions](https://www.documentcrunch.com/construction-execution-solutions), [/crunch-ai](https://www.documentcrunch.com/crunch-ai) |
| 13 | contemporaneous_evidence_graph | **1** | Adjacent-only. They have a genuine **cross-document citation graph** (clause ↔ spec ↔ addendum ↔ flow-down, all cited to page). It contains no contemporaneous project records, so it cannot evidence an event. | [brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| 14 | evidence_completeness | **1** | Marginal. Notice Builder "will indicate where you need to edit and fill in additional details like extra dates or **backup requirements**" — a template placeholder derived from the contract, not an assessment of whether your evidence is sufficient. | [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder) |
| 15 | recoverable_dollar_estimation | **0** | Completely absent. Every ROI number they publish is **time saved / legal spend avoided** (80% review time, 50% billable hours, 75% review time). Zero dollars-recovered claims anywhere. | [case studies](https://www.documentcrunch.com/customer-stories) |
| 16 | claim_package_generation | **0** | Absent. Their generated artifacts are exhaustively enumerated: **redlines, submittals, notices, RFIs, submittal logs, risk registers**. Never a claim package, never a change-order request package. | [June 2026 PR](https://www.documentcrunch.com/news/document-crunch-launches-constructions-first-project-level-ai-risk-intelligence-platform), [brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf) |
| 17 | notice_drafting | **3** | **The one thesis step they own outright.** Notice Builder drafts contract-compliant notices referencing the project's actual contract, in Procore and natively. Marketed, evidenced, webinar'd, GA since Oct 2024. | [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder), [/events/notice-builder-webinar](https://www.documentcrunch.com/events/notice-builder-webinar) |
| 18 | schedule_impact_analysis | **0** | Absent. No float, no critical path, no windows analysis, no TIA. | site-wide |
| 19 | procore_integration | **2** | Real, live, Procore-certified, listed since Dec 2024 — **but architecturally shallow**: `components: ["sidepanel"]`, `permissions: {"company":{}, "project":{}}`, `connector_required: false`, `use_service_accounts: false`. **187 installs**, 0 ratings. Last app version Feb 2025. | [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch) |
| 20 | autodesk_integration | **0** | No Document Crunch app found in the Autodesk App Store or ACC partner directory (both searched 19 Aug 2026). Their one "Autodesk" news item is a **third-party Feb 2022 Autodesk blog** about 11 unrelated ACC integrations. Their design-adjacent partner is Nemetschek/Bluebeam, now Trimble. | [apps.autodesk.com search](https://apps.autodesk.com/en/List/Search?searchText=document+crunch), [/news/autodesk-construction-cloud-integration](https://www.documentcrunch.com/news/autodesk-construction-cloud-integration) |
| 21 | outlook_gmail_integration | **1** | Adjacent-only via Microsoft: a **Word add-in** for redlining, and Microsoft SAML SSO. No Outlook add-in, no mailbox connector, no email ingestion. | [/word-integration](https://www.documentcrunch.com/word-integration), [Procore listing JSON](https://marketplace.procore.com/apps/document-crunch) |
| 22 | mobile_workflow | **2** | Claimed and repeated: "Mobile access on smartphones and tablets"; "bringing that same intelligence… to the job site." Web-responsive; **no native app located in either app store**. | [homepage](https://www.documentcrunch.com/), [/why-us](https://www.documentcrunch.com/why-us) |
| 23 | audit_trail | **2** | SOC 2 Type II; "Enterprise-grade security and **audit trail**"; Share Log; review status tracking; every answer cited to source. Not an evidentiary chain-of-custody for a claim. | [homepage](https://www.documentcrunch.com/), [/security](https://www.documentcrunch.com/security) |
| 24 | portfolio_risk | **2** | Risk routed/tracked/visible across phases; "Assign and track risk… open, overdue, and done at a glance"; AXA XL contract benchmarking partnership. Their own Jan 2026 report admits "**few evaluate them systematically across the portfolio**" — i.e. the market (and arguably they) still lack it. | [homepage](https://www.documentcrunch.com/), [/blog/causes-of-post-award-fee-erosion-in-construction](https://www.documentcrunch.com/blog/causes-of-post-award-fee-erosion-in-construction) |
| 25 | performance_pricing_compatibility | **1** | Their entire value metric is cost **avoided**, not revenue **recovered** — structurally incompatible with success fees. Pricing is subscription scaled to project volume. The AXA XL / IRMI / surety relationships are the only theoretical path to outcome-linked economics. | [Procore listing pricing_description](https://marketplace.procore.com/apps/document-crunch), [/construction-insurance-sureties](https://www.documentcrunch.com/construction-insurance-sureties) |
| 26 | consultant_replacement_potential | **2** | **Strong for transactional contract-review counsel** — Balfour Beatty tripled revenue with flat legal headcount; "Grow over a half a billion dollars without a lawyer"; E-J Electric "reduced legal dependency"; they cite lawyer rates of "$600-800/hour." **Zero for claims consultants / quantum experts / delay analysts.** | [Balfour Beatty case study](https://www.documentcrunch.com/case-studies/balfour-beatty-2), [/blog/project-playbooks](https://www.documentcrunch.com/blog/project-playbooks) |

**SCORES| 3,3,2,1,1,0,0,1,1,0,0,1,1,1,0,0,3,0,2,0,1,2,2,2,1,2**

---

## 4. PRICING

**No published pricing exists.** Confidence: **HIGH** that none is published; **LOW** on any dollar figure.

### What is verifiable
The **Procore Marketplace listing carries a verbatim pricing statement** from Document Crunch — the single most useful pricing artifact available, because it reveals the *pricing axis*:

> "Pricing varies based on use case and needs, and we need to know your situation before we can price out.
>
> (Yes, we know no one likes that answers. But the truth is, **a heavy civil builder who does 3 major projects a year will use Document Crunch differently than a plumber doing 300 projects a year and we want to ensure the pricing reflects the scenario correctly.**)"
> — [Procore Marketplace listing JSON, `pricing_description`](https://marketplace.procore.com/apps/document-crunch)

**Interpretation (high confidence):** pricing scales with **project/document volume**, not seats alone, and is negotiated per company. Listing flags: `pricing: true`, `subscription_required: true`, **`has_trials: false`**, `pricing_url: ""`, `price_button: ""`.

Trimble Marketplace: `hidePricings: true`, `startingPrice` empty, single edition "Version 1 / 1 User / revenueType: FREE" (a lead-gen placeholder, not a real free tier). — [Trimble Marketplace](https://marketplace.trimble.com/en-US/apps/572173/document-crunch)

Their own site offers "Start a Trial" ([/trial](https://www.documentcrunch.com/trial)) — contradicting the Procore `has_trials: false` flag. Third-party listing: *"Document Crunch price plan can be **tailored to each customer's needs**"* — [SoftwareFinder](https://softwarefinder.com/legal/document-crunch).

### Reported figures — treat with strong caution
- **"~$200/month for small teams"** — surfaced only via AI-generated software-directory content farms (velocityaipartners, trendingaitools). No primary source, no reseller quote, no procurement record. **`UNVERIFIED` — I would not carry this number forward.**
- Anchor they set themselves: they benchmark against attorneys at **"$600-800/hour"** and against GCs "running several hundred projects a year" ([/blog/project-playbooks](https://www.documentcrunch.com/blog/project-playbooks)). An enterprise GC contract almost certainly sits in five to low-six figures annually. **`UNVERIFIED` inference.**

### Revenue scale inference
Trimble stated the acquisition is **"not anticipated to materially impact 2026 financial guidance"** ([Trimble IR](https://investor.trimble.com/news/news-details/2026/Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem/default.aspx)). Against Trimble's ~$3.7B revenue base, that bounds Document Crunch ARR well below ~$40M. Combined with 400+ customers (Aug 2025) and Inc. 5000 #311, a **$15–30M ARR** range is a reasonable estimate. **`UNVERIFIED` inference — no primary source.** A third-party aggregator lists "$12.6M" ([startupintros](https://startupintros.com/orgs/document-crunch)) but that page also contains demonstrable errors (wrong acquisition year, implausible investors), so treat it as noise.

---

## 5. INTEGRATIONS, API & DATA EGRESS REALITY

### 5.1 Procore — the decisive artifact
The Procore App Marketplace listing embeds a complete JSON manifest. This is the hardest evidence in this report:

```
id: 7126
name: Document Crunch
slug: document-crunch
components: ["sidepanel"]                       ← side-panel iframe ONLY
permissions: { "company": {}, "project": {} }   ← ZERO data permissions requested
connector_required: false
use_service_accounts: false
product_tools: [Correspondence, Documents, Inspections, Observations,
                Schedule, Budget, Change Events, Commitments,
                Prime Contracts, RFIs]          ← where the panel RENDERS, not what it READS
installation_count: 187
ratings: { average_rating: null, total_ratings: 0 }
subscription_required: true
has_trials: false
subprocessors_details: "AWS, Zuva, OpenAI, Anthropic"
security_standards: [SOC 2 Type 2]
sso_providers: ["Microsoft"]
data_processing_locations: ["United States"]
regions: [Canada, EMEA, United States]
countries (EMEA): [United Arab Emirates, United Kingdom]
created_at: 2024-12-06 | updated_at: 2026-05-06
versioning_history:
  3.0.0 (2024-03-28) "design updates, additional Side Panel locations, easier account logins"
  3.1.0 (2024-10-15) "Updating availability on more Procore tools"
  3.2.0 (2025-02-27) (no changelog)
```
— [marketplace.procore.com/apps/document-crunch](https://marketplace.procore.com/apps/document-crunch)

**Three findings follow directly:**
1. **They read nothing out of Procore.** Empty permission scopes is not an omission — Procore requires apps to declare every read/write scope. Document Crunch declares none. The `product_tools` list is the set of pages the panel is *allowed to appear on*.
2. Their own "how it works" confirms the direction of data flow: *"**Start by uploading your contract to Document Crunch.** Once uploaded, you'll be able to tailor a cheat sheet… **Your teams will be able to access and interact with this cheat sheet in Procore.**"* Contract goes *in* by upload; insight comes *out* into a panel.
3. **187 installs** against **400+ customers** and **10,000+ projects**. The Procore channel is thin. Combined with `total_ratings: 0` and no app release since Feb 2025, this is a **deprioritised surface**.

**This directly falsifies their own Procore marketing.** Their page promises: *"AVOID FUTURE LITIGATION: Stay in compliance without lifting a finger. **Receive notifications when key events occur within the project lifecycle**"* ([/procore](https://www.documentcrunch.com/procore), identical copy in the marketplace `description`). With zero data permissions, **there is no mechanism by which the product can know that a project event has occurred.** This claim is unsupported by the app's declared architecture.

### 5.2 Trimble
- Listed on Trimble Marketplace as a **Trimble Certified App**, tagged **ProjectSight**, category **Document Management** only. `features.items: []` — no features published. No pricing, no ratings. — [marketplace.trimble.com/en-US/apps/572173/document-crunch](https://marketplace.trimble.com/en-US/apps/572173/document-crunch)
- Trimble's stated post-acquisition plan is the important part: Document Crunch will provide *"a **'contractual rule set'** to serve as the intelligent DNA for the entire Trimble Construction One suite, **automatically pushing critical obligations, compliance requirements and payment terms into Trimble's robust project delivery ecosystem**."* — Mark Schwartz, SVP AECO Software, [Trimble IR](https://investor.trimble.com/news/news-details/2026/Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem/default.aspx)
- Note the direction: **obligations pushed OUT into project systems.** Still not project events pulled IN. But it puts Viewpoint Vista, Spectrum, ProjectSight, Trimble Connect and e-Builder data on the other side of a corporate firewall rather than a partnership.

### 5.3 Microsoft
- **Document Crunch for Word** — add-in for in-document redlining against your risk standards. — [/word-integration](https://www.documentcrunch.com/word-integration)
- Microsoft SAML SSO. **No Outlook, no Graph, no SharePoint, no OneDrive, no Teams.** No Egnyte. No Box. No Dropbox.

### 5.4 Nemetschek / Bluebeam
Strategic Series B investor; integration referenced in the Series B PR. — [Series B PR](https://www.documentcrunch.com/news/series-b)

### 5.5 Insurance / association channel
AXA XL (contract-review benchmarking for insureds), IRMI, ELECTRI, ABC, AGC New York State, NECA, NAWIC, Billd, Acrisure. — [/partnership](https://www.documentcrunch.com/partnership), [Series A PR](https://www.documentcrunch.com/news/series-a)

### 5.6 API — closed
| Probe | Result |
|---|---|
| `developers.documentcrunch.com` | 404 |
| `docs.documentcrunch.com` | 404 |
| `documentcrunch.com/api`, `/developers` | 404 |
| `api.documentcrunch.com` | **200 — returns `"Hello, I am alive"`**; `/docs`, `/swagger`, `/openapi.json`, `/v1` all 404 |

**There is no public API and no public developer documentation.** Integration is exclusively via first-party embeds (Procore side panel, Word add-in, ProjectSight). **Data egress reality: you get .pdf / .docx / .xlsx exports and annotated linked PDFs — no programmatic extraction path.** ([brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf); [/blog/launching-document-crunch-2-0](https://www.documentcrunch.com/blog/launching-document-crunch-2-0))

---

## 6. WEAKNESSES AND EXPLICIT GAPS — deliberate or unattended?

| Gap | Deliberate or unattended? | Reasoning |
|---|---|---|
| **No project-record ingestion** (RFIs, daily reports, emails, schedules, minutes, photos) | **DELIBERATE — and marketed as a virtue** | Their own FAQ sells the absence: *"There's **no heavy implementation or integration required**. Just instant insights delivered directly into your team's workflow."* ([/platform-old](https://www.documentcrunch.com/platform-old)). Zero-permission Procore app is a deliberate architecture: it makes the app trivially installable and keeps them out of every customer's data-governance review. |
| **No event detection** | **DELIBERATE, and structurally enforced** | You cannot detect events in data you never receive. This is the load-bearing gap for the thesis. |
| **No deadline clock** | **UNATTENDED — this is the softest spot** | They *market* deadline management on their own product page but ship no named feature. The Playbook already contains the notice-timing rules; the only missing pieces are a project start date and a scheduler. This is the gap most likely to close first, and it needs no new data source. |
| **No claim identification / quantification / claim package** | **DELIBERATE — brand-level and founder-level** | Vision is literally *"zero disputes."* Their positioning is *"Disputes aren't a cost of construction. They're a cost of unmanaged risk."* Building a claims engine would mean selling their customers a tool for the outcome they define as failure — and would put them opposite the owners, insurers and sureties who are also their customers and channel partners (AXA XL, IRMI). Two former construction-claims lawyers chose this deliberately. |
| **No delay / schedule-impact analysis** | **DELIBERATE (capability boundary)** | Requires CPM data and forensic methodology — a different discipline, different buyer, different liability posture. |
| **Procore channel is thin (187 installs, no release since Feb 2025)** | **UNATTENDED, now likely abandoned** | Post-Trimble, Procore is a competitor. Expect this surface to atrophy. |
| **No Autodesk presence** | **DELIBERATE (alliance choice)** | They aligned to Nemetschek, then Trimble. Autodesk is now firmly the other camp. |
| **No public API** | **DELIBERATE** | Closed-platform posture; embeds only. |
| **Thin public review corpus** | Unattended | Procore Marketplace: 0 ratings. Trimble Marketplace: ratings disabled. G2/Capterra/TrustRadius all bot-gated. For a company at 400+ customers this is a surprisingly quiet footprint. |
| **Zero open roles on their own ATS (Aug 2026)** | Consequence of acquisition | `api.rippling.com/platform/api/ats/v1/board/document-crunch-inc/jobs` returns `[]`. Hiring has moved to Trimble. Signals an integration period, not an expansion period. |
| **Owner-side product is unbuilt** | Unattended | They name owners as a segment but ship no owner page or owner workflow. |

---

## 7. ADJACENCY TEST — how hard for THEM to ship "event detection → entitlement matching → evidence → claim package"?

### Verdict: **MEDIUM** — and it splits sharply in two halves.

**The pipeline is not one thing. Score it in halves:**

**First half — event detection → entitlement matching → deadline clock: EASY (post-Trimble).**
- **Data access: was the blocker, now solved.** Pre-April 2026 they had no path to project records without building connectors they had explicitly refused to build. Trimble owns ProjectSight, Viewpoint Vista, Spectrum, e-Builder and Trimble Connect. Schwartz's own words — "automatically pushing critical obligations… into Trimble's project delivery ecosystem" — describe half the loop already; closing it to read events back is an internal integration, not a partnership negotiation.
- **The entitlement rule-set already exists.** The Playbook already encodes, per project: notice triggers, notice timing, notice delivery method, notice recipients, change-order procedure, markup limits, backup requirements, order of precedence, escalation clauses, weather/unforeseen-conditions terms. That is the hardest and most defensible asset in the whole thesis pipeline, and **they already have it on 6,000+ projects.**
- **Org incentive: aligned.** "Notice Requirement Failures" is already one of their published 7 causes of margin erosion. A deadline clock is a pure extension of their existing story with no brand conflict.
- **Shipping behaviour: fast.** Chat (Jan 2024) → Procore embed (2024) → Playbooks (Jul 2024) → Notice Builder (Oct 2024) → CrunchAI for Specs (2025) → full platform re-architecture (Jun 2026). Roughly two significant releases a year, each moving further into execution.

**Second half — evidence assembly → recoverable-dollar estimate → claim package: HARD.**
- **Legal exposure appetite: low, and explicitly so.** They repeatedly disclaim: *"we don't replace legal counsel"*; *"When it comes to state-specific laws or regulatory requirements, **we flag limitations clearly and encourage professional legal review**"* ([/platform-old](https://www.documentcrunch.com/platform-old)). Quantifying a claim is an opinion of entitlement and value — categorically different liability from summarising a clause.
- **Brand conflict is total.** "Zero disputes" is not a tagline they can quietly retire; it is the mission statement, the vision statement, the webinar series ("Disputes Are Not Inevitable"), and the founders' personal narrative.
- **Channel conflict.** Owners, insurers and sureties are named customers and partners. A contractor-side claims engine is a weapon pointed at them.
- **GTM motion mismatch.** They sell a standardisation/consistency story to legal, risk and precon buyers. Claims recovery is sold to operations and project controls on a *recovered dollars* promise — a different buyer, a different proof burden, and a proof burden they have never had to meet (every published ROI number is time-saved).
- **M&A behaviour: they were the target, not the acquirer.** No history of buying capability. Post-close, a 90-person team inside Trimble AECO will spend 12–18 months on TC1 integration, not on a new category.

**Net:** MEDIUM. They can close the front of the pipeline quickly and probably will. They are structurally and culturally unlikely to close the back of it.

---

## 8. STARTUP POSTURE: PARTNER / CHANNEL / ROADKILL

### Verdict: **PARTNER** — with a hard time limit and a required change of aim.

**Why not ROADKILL:** they do not do the thing. Not the event detection, not the evidence graph, not the quantification, not the claim package. And the two most senior people in the company have spent seven years and $38M establishing publicly that they *don't want to*. A startup that positions as "recover what you're owed" is not competing with a company whose stated goal is that nobody ever has to.

**Why not CHANNEL (yet):** no public API, no partner program for data, no marketplace with revenue share, closed embeds only. There is no mechanical way to plug into them today.

**Why PARTNER:** the complementarity is unusually clean. Document Crunch converts the contract into a structured entitlement rule-set — the single most expensive and least differentiating part of the thesis pipeline. A startup that starts at *events* and consumes *rules* is the natural other half. Their own published failure mode is the startup's entry point: *"Project managers learned too late that notice windows had already closed."* Document Crunch's answer is "brief the team better." The startup's answer is "watch the project." Those are additive, not competitive.

**The two caveats that matter:**
1. **Trimble changes the clock.** A partnership that would have been durable against a $38M-funded independent is not durable against a Trimble business unit with access to Vista, Spectrum, ProjectSight and e-Builder data. Assume a **12–24 month window** before the front half of the pipeline is native to TC1.
2. **A startup that stops at "notice drafting" is roadkill.** Notice Builder has been GA since Oct 2024 and is now core to Project Assist. Do not build there. The defensible ground is downstream of the notice: **evidence assembly, entitlement quantification, and the claim package** — where their brand, their founders' stated mission, and their legal-exposure appetite all prevent them from following.

---

## 9. TOP 5 CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

**Caveat, stated plainly:** G2, Capterra and TrustRadius are all bot-protected and returned 403/CAPTCHA to every retrieval method attempted (direct fetch, Googlebot UA, text-extraction proxy). Procore Marketplace shows **0 ratings**; Trimble Marketplace has ratings **disabled**. Reddit search is login-gated. **I could not obtain a corpus of verbatim first-party negative reviews.** What follows is what I could evidence, honestly labelled. This is a genuine hole — see §11.

1. **Processing latency on large documents.** *"[It] takes some time before the crunch is accessible… users can continue working on other documents while the crunch processes in the background."* — G2 pros-and-cons content, reached only via search-engine snippet, not verifiable on-page. `UNVERIFIED (second-hand)`. [g2.com/products/document-crunch/reviews?qs=pros-and-cons](https://www.g2.com/products/document-crunch/reviews?qs=pros-and-cons)
2. **Earlier checklists were manual and slow.** *"[E]arlier versions… were not nearly as helpful as the current setup, with checklists that used to be very manual and took a long time to craft and execute."* — same source, same caveat. Corroborated independently by the E-J Electric case study, which describes rebuilding "a formerly static checklist" into a CrunchAI Checklist. [E-J Electric case study](https://www.documentcrunch.com/case-studies/setting-a-new-standard-for-risk-management-how-e-j-electric-saves-time-reduces-legal-spend-and-drives-consistency)
3. **Missing redline / version compare (historic).** *"Lacks built-in redline or version comparison capabilities."* — [SoftwareFinder](https://softwarefinder.com/legal/document-crunch). **Now resolved** — the June 2026 platform added "auto redlining" and "version compare with risk analysis." Useful as a datapoint on their release cadence rather than a live complaint.
4. **No folder structure for team collaboration.** — [SoftwareFinder](https://softwarefinder.com/legal/document-crunch). `UNVERIFIED` third-party aggregator; date unknown.
5. **Structural complaint, evidenced from their own customers rather than reviews — the knowledge doesn't survive the handoff to execution.** Their own Jan 2026 research quotes an operations leader: *"**We're identifying risks and then watching project teams step on the same landmines because nobody briefed them.**"* And: *"Even when risks are flagged, contract intelligence often does not transfer to operations in time to change outcomes."* — [/blog/causes-of-post-award-fee-erosion-in-construction](https://www.documentcrunch.com/blog/causes-of-post-award-fee-erosion-in-construction). This is Document Crunch publishing, in 2026, that the problem their own product was built to solve **is still unsolved for their market**. It is the most thesis-relevant complaint I found, and it comes from their own primary research.

---

## 10. HARDEST FACTS (the 5 strongest, all numeric or literal)

1. **The Procore app requests zero data permissions and is a side-panel embed only:** `components: ["sidepanel"]`, `permissions: {"company": {}, "project": {}}`, `connector_required: false`. It reads nothing from Procore. — [marketplace.procore.com/apps/document-crunch](https://marketplace.procore.com/apps/document-crunch)
2. **187 Procore installations, 0 ratings, last app release Feb 2025** — against 400+ customers and 10,000+ projects. The deepest available integration surface is barely used and no longer being shipped. — [marketplace.procore.com/apps/document-crunch](https://marketplace.procore.com/apps/document-crunch)
3. **Trimble acquired Document Crunch** — announced 2 Apr 2026, closing Q2 2026, terms undisclosed, folded into Trimble AECO, **"not anticipated to materially impact 2026 financial guidance."** Trimble intends Document Crunch to be the *"contractual rule set… the intelligent DNA for the entire Trimble Construction One suite."* — [investor.trimble.com](https://investor.trimble.com/news/news-details/2026/Trimble-to-Acquire-Document-Crunch-to-Add-AI-Powered-Risk-Management-and-Document-Compliance-to-Trimble-Construction-One-Project-Delivery-Ecosystem/default.aspx)
4. **Scale: 10,000+ projects, 500+ contractors, $380B+ annual construction volume**; previously 400+ customers and 6,000+ projects on Playbooks (Aug 2025); headcount **30 → 90+** in twelve months; **$38M** total funding; **Inc. 5000 #311** (2025), #29 in Software; *"nearly tripled our revenue each of the last three years."* — [Trimble Marketplace](https://marketplace.trimble.com/en-US/apps/572173/document-crunch), [Inc. 5000 PR](https://www.documentcrunch.com/news/inc-5000-fastest-growing-private-companies)
5. **Notice Builder is entirely human-triggered.** *"you'll select the event type then describe what's going on and the relevant date… you'll select what's been impacted… you'll explain what actions have already been taken."* Then, for the deadline: *"**use your playbook or chat to find your submission instructions**… find the relevant notice timing."* Live since 21 Oct 2024. — [/blog/notice-builder](https://www.documentcrunch.com/blog/notice-builder)

**Bonus market-sizing facts they publish themselves:** US GCs and subs *"spend an estimated **$11B+ annually on profit loss** related to risk hidden within complicated contracts and project documents"* ([Series B PR](https://www.documentcrunch.com/news/series-b)); **81%** of construction companies say they've been hurt financially by a contract, average dispute value **$60.1M** ([/platform-old](https://www.documentcrunch.com/platform-old)); *"Construction disputes rose **40%** in North America last year. The **#1 cause** was errors and omissions in contract documents"* (Arcadis 15th Annual Construction Disputes Report 2025, cited in their [brochure](https://20893474.fs1.hubspotusercontent-na1.net/hubfs/20893474/Document%20Crunch%20AI%20Risk%20Intelligence%20Overview.pdf)).

---

## 11. UNKNOWNS — and what would settle each

| Unknown | What would settle it |
|---|---|
| **Does any shipped feature produce a date-driven deadline alert?** The single most important open question. Their marketing claims "manage deadlines" and "receive notifications when key events occur"; the architecture makes the second impossible and the first unevidenced. | A live product demo, a customer walkthrough, or in-app release notes. Their [June 2026 Community Demo recording](https://www.documentcrunch.com/events/june-community-demo-new-document-crunch-platform) is gated behind a form — **the highest-value next action.** |
| **Actual ARR** | Trimble 10-K/10-Q segment disclosure (unlikely to break out), or a purchase-price disclosure. |
| **Acquisition price** | Trimble 10-Q for Q2/Q3 2026 business-combination footnote. |
| **Post-acquisition roadmap** | Trimble Dimensions conference (they run a [/trimble-dimensions-demo](https://www.documentcrunch.com/trimble-dimensions-demo) page). Trimble AECO analyst-day materials. |
| **Real-world pricing** | Procurement documents, a reseller quote, or a public-sector contract award (their customers include public-sector GCs). |
| **Verbatim customer complaints** | G2/Capterra/TrustRadius are bot-gated to every method tried. Would need authenticated access or a human pull. |
| **Whether an Autodesk Construction Cloud integration exists** | Searched Autodesk App Store and ACC partner directory 19 Aug 2026 — no listing found. An ACC partner-directory API pull would confirm definitively. |
| **Headcount today** | LinkedIn company page (not fetchable in this environment). Note their own ATS shows **zero open roles**. |
| **Whether Project Assist can ingest a user-uploaded RFI log / daily report** | Nothing prohibits a user from uploading such a PDF; whether the product does anything structured with it is unknown. A trial account would settle it. **This matters:** if Project Assist can reason over an uploaded RFI log, the gap is narrower than the marketing suggests. |

---

## 12. DIRECT ANSWERS TO THE FOUR KEY QUESTIONS

### Q1. Has Document Crunch already moved from pre-signature contract review into during-construction entitlement/notice monitoring?

**They have moved into during-construction. They have NOT moved into monitoring.**

Split it precisely:

| Thesis pipeline step | Document Crunch today |
|---|---|
| Contract ingestion + clause extraction | **OWNED — best in class** |
| Commercial event detection | **ABSENT.** No project data in. Human types the event. |
| Entitlement / notice matching | **HALF.** The rule-set exists (Playbook). Nothing matches it to a real event automatically. |
| Deadline clock | **ABSENT as a feature.** Claimed in copy; the user looks the timing up manually. |
| Evidence collection | **ABSENT.** No contemporaneous project records exist in the system. |
| Recoverable-value estimate | **ABSENT — and never once mentioned across ~95 press items, 82 blog posts, 24 webinars, 16 case studies and 2 marketplace listings.** |
| Notice generation | **OWNED — Notice Builder, GA since Oct 2024** |
| Claim package | **ABSENT.** Their generated-artifact list is exhaustive and closed: redlines, submittals, notices, RFIs, submittal logs, risk registers. |

They moved *down the timeline* (pursuit → precon → execution → closeout) without ever moving *across the data boundary* (documents → project records). That distinction is the whole ballgame.

**The wedge is therefore NOT occupied — with one exception.** Notice *drafting* is occupied and should be treated as taken. Everything from *event detection* through *quantification* and *claim package* is open.

### Q2. If they have, what is left?

The middle and the end of the pipeline:
1. **Event detection from project records** — RFIs, daily reports, emails, schedule updates, meeting minutes, photos. They ingest none of these. This is the true wedge.
2. **The deadline clock** — turning extracted notice rules into a live countdown against a real event date. Soft ground; expect them here first.
3. **Contemporaneous evidence assembly** — linking an event to the records that prove it. Structurally impossible for them today.
4. **Recoverable-dollar quantification** — never attempted, never mentioned.
5. **Claim / change-order request package** — never attempted; brand-incompatible.
6. **Schedule impact analysis** — absent, different discipline.

Also left: the **owner side** (named as a segment, no product) and **email as an ingestion surface** (Outlook/Gmail — completely untouched, and the single lowest-friction V1 ingestion path for a solo founder).

### Q3. If they have not — deliberate strategy or roadmap gap, and how fast could they close it?

**Both, in different places, and the split is diagnostic.**

**Deliberate (and defended in their own words):**
- *No project-data ingestion* — they sell the absence: *"There's no heavy implementation or integration required."* Zero-permission Procore app is a design choice that makes them frictionless to buy.
- *No claims capability* — "zero disputes" is the vision statement. Two founders who ran hundreds of millions of dollars of claims chose prevention. They also sell to owners, insurers and sureties, whom a contractor-side claims engine would antagonise.
- *No legal opinions* — they explicitly disclaim: *"we flag limitations clearly and encourage professional legal review."*

**Unattended (genuine roadmap gap):**
- *The deadline clock.* They market it and don't ship it. The rule-set already exists in the Playbook. All that's missing is a start date and a scheduler.

**Speed to close:**
- **Deadline clock: 3–6 months.** No new data source required.
- **Event detection: 6–12 months post-Trimble-integration.** Trimble owns ProjectSight, Vista, Spectrum, e-Builder and Connect. The data-access blocker that shaped seven years of product decisions evaporated in April 2026. Their stated plan already runs obligations *outward* into project systems; running events *inward* is the same plumbing reversed.
- **Quantification + claim package: unlikely at any speed.** This is not a capability constraint. It is brand, mission, channel and liability. Closing it would require repudiating the company's stated reason for existing.

### Q4. Would the proposed product be a feature of Document Crunch within 18 months?

**Partially — and the split determines whether the thesis survives.**

| Layer | Probability of being a Document Crunch/Trimble feature by Feb 2028 | Reasoning |
|---|---|---|
| Notice drafting | **Already is.** 100%. | Notice Builder, GA Oct 2024. **Do not build here.** |
| Obligation/deadline register with reminders | **HIGH (~70%)** | Rule-set exists; they already market it; Trimble's stated plan is pushing obligations into project workflows; no brand conflict. |
| Event detection from project records | **MEDIUM (~40%)** | Newly feasible via TC1. Gated by 12–18 months of post-acquisition integration work and by their long-standing "no heavy integration" positioning. Also only reaches *Trimble* customers — leaving the Procore, Autodesk and no-PM-system majority untouched. |
| Contemporaneous evidence graph | **LOW (~20%)** | Requires everything above plus a new data model. |
| Recoverable-dollar estimation | **VERY LOW (~5–10%)** | Never mentioned in the entire corpus. Contradicts the mission. Creates liability they've spent seven years disclaiming. |
| Claim package generation | **VERY LOW (~5%)** | Contradicts "zero disputes." Antagonises the owner/insurer/surety channel. |

**Bottom line for the thesis.** Document Crunch is the strongest possible proof that the *upstream* half of this problem is real, valuable and monetisable — they built a $38M-funded, Inc.-5000-#311, Trimble-acquired business on it, and their own 2026 research names *"notice windows had already closed, converting otherwise valid claims into absorbed costs"* as a top-7 cause of margin erosion. They are also the strongest possible proof that the *downstream* half is unoccupied: they have every advantage needed to take it — the contract rule-set, 10,000 projects, 500 contractors, construction-lawyer founders, and now Trimble's data — and they have publicly, repeatedly and structurally declined to.

**A product that begins where Document Crunch's Notice Builder begins is a feature. A product that begins where the *event* begins — and ends at a priced, evidenced claim package — is a company, and Document Crunch has spent seven years explaining why it will not be them.**
