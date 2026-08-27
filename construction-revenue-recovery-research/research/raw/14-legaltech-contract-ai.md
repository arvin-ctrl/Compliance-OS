# 14 — Horizontal Legal-Tech / Contract-AI / Obligation-Management (Category Report)

**Scope:** Luminance, Ironclad, LegalOn, Harvey, Eve, Spellbook, Robin AI, Icertis, Agiloft, Sirion, Evisort (Workday), DocuSign IAM/Navigator, Relativity/Everlaw, and the commodity substitutes (Microsoft 365 Copilot, ChatGPT, Claude, Gemini in Workspace).

**Research date:** 19 August 2026. All URLs fetched on that date unless stated.

**Method note / caveat up front:** this session's keyword-search budget was exhausted early, so most evidence below is from **direct fetches of vendor primary sources** (product pages, pricing pages, customer pages, integration pages) plus Microsoft Learn docs, arXiv, and the Vals AI benchmark site. Secondary pricing aggregators are used only where labelled, and their confidence is marked. Several vendors (Icertis, Sirion, Ironclad, Luminance, Robin AI, Harvey, LegalOn, Spellbook, Agiloft, Relativity, Everlaw) **publish no pricing at all**; that itself is a finding and is documented.

---

## 0. THE ONE-PARAGRAPH ANSWER

The horizontal category has already built **hypothesis A** — "extract obligations from a contract, assign owners, alert before deadlines, keep an audit-ready log" — and ships it as a mature, named, GA product (Icertis *Vera Obligations*; Sirion *Obligations Agent*; Agiloft *Astra*; Robin AI *obligation workflows*; Luminance *Analyze*). It costs **$50k–$500k+/yr** and is sold to **enterprise Legal/Procurement**, whose contracts are MSAs and supplier agreements, not projects. It has **not** taken construction because the horizontal product is anchored to the wrong object (the *contract as an enterprise asset*), the wrong buyer (GC/CLO/CPO), and the wrong data plane (SAP/Salesforce/Workday/iManage — **zero** construction systems appear in any integration list I could find). Meanwhile the commodity LLM already does the *reading* half of the thesis for ~$18–$30/user/month and does it well enough that the reading half cannot be the product. What is left over is everything downstream of reading: persistent state, event detection over project traffic, evidence linkage, and the served-notice audit record. That is a real remainder — but it compresses the price ceiling for anything that is mostly "chat with your contract."

---

## 1. SNAPSHOT — WHAT EACH VENDOR IS, WHO IT SELLS TO, SCALE

### 1A. Enterprise CLM / obligation management (the direct thesis-A competitors)

**Icertis** — AI-native CLM, founded 2009, Bellevue WA. Products organised into **Engage / Operate / Analyze** with a "Vera" agent family; **Vera Obligations** and **Vera Fulfillment Agent** sit in Operate. Sells to Fortune 500 legal + procurement. Scale: "90+" countries, "2,000+" employees, "40+" languages (https://www.icertis.com/company/). Raised **>$500M**; valued at **$5B** four years ago; Bloomberg reported Feb 2026 it was exploring a sale at "as much as $5 billion"; CEO Anand Subbaraman departed July 2026 after <1 year, CFO + a board member named interim co-CEOs (https://www.geekwire.com/2026/icertis-ceo-is-departing-contract-management-company-names-cfo-and-board-member-interim-leaders/, 17 Jul 2026). **This is the only vendor in the category with a construction solution page** (below).

**Sirion** — AI-native CLM built around post-signature governance (its origin is IT/BPO outsourcing SLA management). Platform = **Store / Create / Manage** plus named agents including an **Obligations Agent** and an **Invoice Agent** (https://www.sirion.ai/platform/). Ownership changed hands: **Haveli Investments agreed a majority investment, announced 8 Jan 2026** (Law.com Legaltech News via Bing News RSS) — i.e. PE control, not growth-stage. Industries listed: Financial Services, Insurance, Automotive, IT Services, Healthcare, Pharma/Life Sciences, Telecom, Oil & Gas — **construction/E&C/AEC appears nowhere** (https://www.sirion.ai/solutions/).

**Agiloft** — no-code CLM + **Astra** contracts-AI layer covering "pre and post-signature," with "AI extraction surface the terms, risks, and obligations" and obligation/renewal tracking (https://www.agiloft.com/). Industry pages: Healthcare, Financial Services, Pharma/Biotech, Manufacturing, Energy, Software/Tech, Business Services — **no construction**. Strong in public sector (e.g. King County DCHS uses it for solicitations/contracting/invoices — https://kingcounty.gov/en/dept/dchs/human-social-services/funding-opportunities-dchs/agiloft).

**Ironclad** — CLM for in-house legal, workflow-first. No published price tiers ("get a thoughtful quote" — https://ironcladapp.com/pricing). Integrates *into* Harvey (Harvey lists Ironclad as a "Contract Intelligence" integration — https://www.harvey.ai/platform).

**Evisort → Workday** — acquisition announced **17 Sep 2024**, undisclosed price (Law.com Legaltech News 17 Sep 2024; Nasdaq 18 Sep 2024, via Bing News RSS). **evisort.com now 301-redirects to workday.com** (verified 19 Aug 2026). Evisort's document-intelligence capability is now a Workday feature aimed at Finance/HR, not a standalone CLM sold to contractors.

**DocuSign IAM / Navigator** — the only horizontal vendor with a **real, published construction go-to-market**: a construction industry page naming change orders, purchase orders, lien waivers, subcontractor agreements and owner agreements, an explicit **Procore** integration, and construction customers **Camden Property Trust** ("6x faster turnaround time", ">$25K saved on shipping costs annually") and **Crossland Construction** ("85% completion rate", "70% same-day turnaround") — https://www.docusign.com/solutions/industries/construction. Autodesk is not mentioned. Navigator/IAM adds an AI agreement repository with "AI-powered data extractions."

### 1B. Contract-AI / review copilots

**Luminance** — Cambridge UK; modules **Draft / Negotiate / Analyze / Comply / Investigate / Collaborate** (https://www.luminance.com/). Scale: "more than 1,000 organizations across 70 countries," all Big Four, >25% of the Global Top 100 law firms; **$75M Series C in early 2025**; investors incl. Forestay, March Capital, National Grid Partners, Slaughter and May, Schroders, Point72 (https://www.luminance.com/about/). Launched a proprietary contract LLM, **Luna Crescent**, 22 Jun 2026 (Law.com via Bing News RSS) and announced a **LexisNexis strategic alliance** 21 Apr 2026 (Yahoo Finance via Bing News RSS). **Has a genuine construction-industry customer** (Buro Happold — see §3).

**Robin AI** — London; contract review/editing plus explicit **obligation management**: "Manage obligation workflows end-to-end… Tasks, reminders and dashboards ensure you will never miss an auto-renewal or deadline again" (https://robinai.com/platform). Backed by Google, PayPal, Temasek (https://robinai.com). Its own customer verticals, from its sitemap, are **private markets, entertainment, insurance, financial services, technology, manufacturing** — **no construction** (https://robinai.com/sitemap.xml → pages sitemap). No pricing page exists; /upgrade is a contact form.

**Spellbook** — Word-native drafting/review for in-house + firms. "**4,500+ customers** across 80+ countries"; industry pages = Energy, Healthcare, Financial Services, Technology, Manufacturing, Retail & Consumer Goods (https://spellbook.com/). Notably, its named customer logos include **AtkinsRéalis** — a top-tier global engineering & construction firm — alongside Dropbox, eBay, ASICS, Fender, Franklin Templeton. Pricing is "custom… determined by the number of team members on a license" (https://spellbook.com/pricing).

**LegalOn** — three published tiers (Core Review / Contracting Suite / Productivity Suite) but **no published prices**; "priced around your team size" (https://www.legalontech.com/pricing). **Closed a $50M Series E led by Goldman Sachs, 24 Jul 2025**; business "quadrupled over the past year in the US and UK" (https://www.nasdaq.com/press-release/legalon-closes-50-million-series-e-led-goldman-sachs-2025-07-24).

### 1C. Law-firm AI (the "does the buyer change?" vendors)

**Harvey** — sells to law firms and corporate legal. Products: **Agents, Vault, Workflows, Knowledge**; integrations with iManage, NetDocuments, SharePoint, Google Drive, Word, Outlook, LexisNexis, Aderant and **Ironclad**. Claims "**50M+ files per day**" processed and "**850,000+ queries per day**"; customer page claims "**200,000+ lawyers**" and "**92%**" monthly adoption (https://www.harvey.ai/platform, https://www.harvey.ai/customers). Named customers include firms with very large construction/infrastructure disputes practices — **Reed Smith, Dentons, CMS, A&O Shearman, Vinson & Elkins** — but **no construction, engineering or infrastructure company is named as a customer**.

**Eve** — "AI operating system for **plaintiff** law firms," explicitly vertical-by-buyer: personal injury, labour & employment, med-mal, SSDI, workers' comp. Capabilities include intake, medical chronologies, demand letters, discovery, and — importantly for our thesis — "**nightly audits of active caseloads to surface missed opportunities**." Claims "**trusted by 1,200+ firms**" and a **$103M Series B** (Spark, a16z, Lightspeed, Menlo) (https://www.eve.legal/). This is the closest structural analogue to what a construction-claims product would be.

### 1D. eDiscovery (how disputes actually get document-reviewed)

**Relativity** — RelativityOne plus the **aiR** suite (aiR for Review / Privilege / Case Strategy / Data Breach Response) and **claiR**. Critically: **"Relativity aiR for Review, aiR for Privilege, and aiR for Case Strategy are included at no additional cost with RelativityOne"** and licensing is "Pay as you go or commit to one or three years to save" (https://www.relativity.com/pricing/). Published outcome claims: an independent study found aiR for Review "**cuts human review hours by 98% with higher recall than active learning**"; JND 96% recall; Purpose Legal "$70k+ savings on a single project reviewing 300,000+ documents in one week"; Teneo "1 million documents processed in 18 days" (https://www.relativity.com/data-solutions/air/review).

**Everlaw** — usage-based, **priced per GB with unlimited user licences** and no upload limits; single-document AI actions "Included (No Extra Cost)"; batch AI actions consume credits with admin spend caps. No dollar figures published (https://www.everlaw.com/pricing/).

**Microsoft Purview eDiscovery** — the commodity floor. Microsoft 365 data storage in eDiscovery cases is **included in the enterprise subscription**; only non-M365 AI-app data and Graph API *exports* are pay-as-you-go per GB (https://learn.microsoft.com/en-us/purview/edisc-billing, updated 1 Dec 2025). Meaning: for a dispute whose evidence lives in Exchange/SharePoint/Teams, hold + search + export is already paid for.

### 1E. The commodity substitute

**Microsoft 365 Copilot** — **$30.00/user/month paid yearly** for enterprise (https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365); the SMB add-on "Microsoft 365 Copilot Business" is listed at **$18.00 user/month paid yearly (promotional, originally $21.00, through Sept 2026)**, and Business Premium **with** Copilot bundles at **$32.00 user/month paid yearly** (https://www.microsoft.com/en-us/microsoft-365/copilot/business).
**Copilot Studio** (needed for anything autonomous) — **$200.00/pack/month for 25,000 Copilot Credits**, or pay-as-you-go; requires an Azure subscription (https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio).
**Claude** — Team **$20/user/mo annual** ($25 monthly), min 2 users; Enterprise "$20/seat plus usage costs scaled to API rates" (https://claude.com/pricing).
**Google Workspace** — Gemini is now bundled: Starter gets "Limited" Gemini in Workspace apps, Standard/Plus/Enterprise get "Expanded access" (https://workspace.google.com/pricing). Per-seat dollar figures did not render in fetch — `UNVERIFIED`.
**ChatGPT Business/Enterprise** — openai.com returned HTTP 403 to fetch; **`UNVERIFIED` — do not quote a number.**

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY (with evidence)

| Capability the thesis needs | Who actually ships it, verbatim | Evidence URL |
|---|---|---|
| Obligation **discovery** from contracts | Icertis: "AI-assisted extraction to discover obligations across documents, classify using smart rules"; "uncovers hidden obligations, simplifies legal terms, and assigns tasks to the right owners" | https://www.icertis.com/products/operate/vera-obligations/ |
| Obligation **deadline alerting** | Icertis: "Trigger timely alerts that help owners act early and avoid penalties"; dashboards surface "obligation status, upcoming deadlines, and risk exposure across the entire contract portfolio" | same |
| Fulfilment **evidence capture + audit log** | Icertis: "captures fulfillment evidence automatically so compliance teams maintain clean, audit-ready records"; "audit-ready logs and KPI dashboards" | same |
| Obligation tracing to **source clause** | Sirion: monitors "all types of obligations, milestones, deliverables, and policy and regulatory requirements," and any obligation is traceable "directly to its source clause within the contract document" | https://www.sirion.ai/platform/manage/ |
| **Money** attached to obligations | Sirion: identifies financial consequences "including payments and penalties—and automatically matches each to corresponding invoice line items," claiming **8–12% reduction in spend leakage**, **99% on-time obligation compliance**, **80% reduction in post-signature disputes**, **60% lower cost of contract governance** | same |
| Obligations as **task workflow** | Robin AI: "Manage obligation workflows end-to-end… Tasks, reminders and dashboards ensure you will never miss an auto-renewal or deadline again" | https://robinai.com/platform |
| Date alerts on contract events | Luminance Analyze: "automatic alerts for key periods such as break or termination dates, to ensure nothing is missed"; surfaces "over 1,000 legal concepts"; flags "a missing clause or unusual wording" | https://www.luminance.com/analyze/ |
| Obligation + renewal tracking, cheaper tier | Agiloft Astra: "AI extraction surface the terms, risks, and obligations"; obligation tracking and renewal management; "1,000+ pre-built connectors" | https://www.agiloft.com/ |
| Agreement repository + AI extraction at commodity price | DocuSign IAM: "AI-powered data extractions," "Unlimited Processing with Agreement Manager for new documents + one-time allotment of 5000 historical documents per user" | https://ecom.docusign.com/plans-and-pricing/iam |
| Autonomous, event-triggered agents on the M365 stack | Copilot Studio event triggers: "event triggers allow your agent to act autonomously in response to the defined event occurring"; examples include "When an item is created in SharePoint", "A set amount of time passed (a **Recurrence** trigger)" | https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about (updated 3 Aug 2026) |

**What NOBODY in the category ships:** commercial *event* detection from project traffic (RFIs, daily reports, site instructions), entitlement matching to a *specific* contractual mechanism, delay/causation attribution, schedule-impact analysis, recoverable-value estimation, or a claim/notice package assembled from contemporaneous project records. I found zero marketed instances of any of these across all 14 vendors.

---

## 3. THE CONSTRUCTION QUESTION — DOES ANY OF THEM ACTUALLY TOUCH IT?

**Icertis — yes, nominally.** Its Industrial solutions page carries a Construction card, verbatim: *"Leverage a single source of truth for all your contracts as you manage large scale capital projects with customers, architecture companies, engineering firms, and construction management partners."* It also claims engineering & construction firms can "compare variances between contracts and actuals to pinpoint factors that contribute to margin erosion such as materials, shipping, labor, and inflation" (https://www.icertis.com/solutions/industry/industrial/). **However**: the dedicated construction sub-page `/solutions/industry/industrial/construction/` is indexed by search engines but **returned HTTP 404 on every attempt on 19 Aug 2026** (three fetches, incl. via reader proxy). Whether that is a temporary CMS fault or a quiet de-prioritisation is `UNVERIFIED`. The nearest thing to a construction customer story on the site is **Shermco** ("Shermco Powers Scalable Growth with AI-Driven Contract Intelligence") — an electrical testing/maintenance/commissioning specialty contractor, "North America's largest… electrical testing organization," 40+ service centres, acquired by Blackstone for ~$1.6B in 2025 (https://www.icertis.com/customers/customer-stories/; https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-shermco-for-approximately-1-6-billion/). That is a services company's commercial contract book — not project claims.

**Luminance — yes, one real E&C reference, and it is instructive.** **Buro Happold** (2,000+ employee international engineering consultancy) uses Luminance because "at least 50% of review time was spent manually locating information across multiple sources (playbooks, risk matrices, precedent agreements)." Outcomes: "**90% time savings** on contract-related business inquiries"; urgent inquiries cut from **2 hours to 15 minutes**. Quote: *"With Luminance, we now have a single source of truth where previously we needed to manually pull from three or four sources."* — Phillip Thompson, Associate Director (https://www.luminance.com/customers/buro-happold/). **Note what this is:** an in-house *legal* team doing faster *pre-signature* review and repository Q&A. It is not project-level notice or claims work. No mention of NEC, JCT, FIDIC or AIA anywhere in the case study.

**Spellbook — AtkinsRéalis** appears in its named customer logos (https://spellbook.com/) — again an E&C firm's legal function buying a Word-native drafting/review tool.

**DocuSign — the deepest construction presence in the whole category**, and it is e-signature: change orders, lien waivers, subcontracts, owner agreements, with a native Procore integration and named contractor customers (see §1A).

**Sirion, Agiloft, Robin AI, Ironclad, Harvey, LegalOn, Eve — no construction vertical, no construction industry page, no construction customer I could find.** For Sirion and Agiloft this is explicit: their published industry lists (8 and 7 verticals respectively) exclude construction entirely.

**Contract forms (AIA / ConsensusDocs / FIDIC / NEC):** I found **no evidence** that any horizontal vendor ships pre-trained playbooks or clause libraries for construction standard forms. Not one of Luminance's "1,000+ legal concepts," Icertis's clause library, Spellbook's playbooks, LegalOn's "50+ pre-built playbooks" or Robin AI's playbooks is documented as covering them. Contrast: the incumbent **forms publisher** is moving instead — AIA Contract Documents reports **1,000,000+ contracts written annually, 15,000+ annual subscribers, 45,000+ companies**, and now ships a "**Collaborative AI Assistant**" for drafting guidance, though no clause comparison or deadline tracking (https://aiacontracts.com/). And the construction-specific challenger already exists: **Document Crunch** — "500+ companies including Balfour Beatty, DPR, Swinerton, Webcor, Boldt, Barton Malow," CrunchAI + Project Assist, generating "submittals, RFIs, notices" with "real-time compliance tracking across project phases" and "Every answer, grounded to the exact clause" (https://www.documentcrunch.com/). Horizontal vendors are not competing there; a vertical one already is.

---

## 4. CAPABILITY MATRIX — THE THREE MOST THREATENING

Scoring: 0 absent | 1 marginal/adjacent | 2 partial or needs heavy config/services/3rd party | 3 strong native, marketed and evidenced.

### 4A. ICERTIS (best-in-class horizontal obligation management)

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 3 | Enterprise repository, bulk ingest, "structure and connect every kind of contract"; SAP/Salesforce/MS connectors | https://www.icertis.com/products/ |
| 2 | clause_extraction | 3 | Vera "discovers, extracts, and classifies obligations from contracts"; clause/attribute model trained on "millions of contracts" | https://www.icertis.com/products/operate/vera-obligations/ |
| 3 | notice_detection | 1 | Obligation extraction would surface a notice clause as text, but no notice-mechanism logic, no event→notice mapping marketed | same |
| 4 | deadline_tracking | 3 | "Trigger timely alerts… before deadlines"; dashboards of "upcoming deadlines" across portfolio | same |
| 5 | rfi_event_ingestion | 0 | No construction system in the integration list at all | https://www.icertis.com/products/platform/integrations/ |
| 6 | email_ingestion | 2 | Outlook and Teams integrations exist, but for contract request/negotiation flow, not event mining | same |
| 7 | daily_report_ingestion | 0 | Not a document type the platform recognises | same |
| 8 | schedule_integration | 0 | No P6/MSP/Asta integration | same |
| 9 | change_order_workflow | 1 | Contract amendment workflow ≠ construction change order (no pricing/schedule/entitlement logic) | https://www.icertis.com/products/operate/contract-lifecycle-management/ |
| 10 | claim_identification | 0 | Nothing marketed | — |
| 11 | delay_detection | 0 | Nothing marketed | — |
| 12 | responsibility_attribution | 1 | Assigns obligation *owners* internally; no counterparty fault attribution | https://www.icertis.com/products/operate/vera-obligations/ |
| 13 | contemporaneous_evidence_graph | 1 | "Captures fulfillment evidence automatically" — compliance artefacts only, not a project record graph | same |
| 14 | evidence_completeness | 1 | "Audit-ready logs" per obligation; no completeness test against a claim standard | same |
| 15 | recoverable_dollar_estimation | 1 | Marketed variance-vs-actuals for margin erosion, but needs ERP integration and is procurement-side | https://www.icertis.com/solutions/industry/industrial/ |
| 16 | claim_package_generation | 0 | Nothing marketed | — |
| 17 | notice_drafting | 1 | Vera Composer generates contract documents from templates; a notice letter is possible but unsupported as a use case | https://www.icertis.com/products/ |
| 18 | schedule_impact_analysis | 0 | Nothing | — |
| 19 | procore_integration | 0 | Absent from integrations page | https://www.icertis.com/products/platform/integrations/ |
| 20 | autodesk_integration | 0 | Absent | same |
| 21 | outlook_gmail_integration | 2 | Outlook + Teams + M365 for web named; Gmail not | same |
| 22 | mobile_workflow | 1 | Mobile approvals referenced in CLM generally; depth `UNVERIFIED` | https://www.icertis.com/products/operate/contract-lifecycle-management/ |
| 23 | audit_trail | 3 | "Audit-ready" is the product's central compliance claim; SOC1/SOC2/ISO 27001 | https://trustcenter.icertis.com/ |
| 24 | portfolio_risk | 3 | Portfolio-wide obligation/risk dashboards tied to "revenue, cost, risk, compliance" KPIs | https://www.icertis.com/products/operate/vera-obligations/ |
| 25 | performance_pricing_compatibility | 0 | Enterprise subscription + implementation services; no success/contingency model anywhere | https://www.icertis.com/ (no pricing published) |
| 26 | consultant_replacement_potential | 0 | Does not touch quantum/delay expert work | — |

**ICERTIS SCORES| 3,3,1,3,0,2,0,0,1,0,0,1,1,1,1,0,1,0,0,0,2,1,3,3,0,0**

### 4B. LUMINANCE (best-evidenced contract-AI with a real E&C customer)

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 3 | Enterprise-wide contract ingestion + repository; "<5 minutes to review 80-page MSA" | https://www.luminance.com/ |
| 2 | clause_extraction | 3 | "over 1,000 legal concepts"; anomaly + missing-clause detection | https://www.luminance.com/analyze/ |
| 3 | notice_detection | 1 | Would surface notice wording as a "legal concept"; no notice-mechanism modelling | same |
| 4 | deadline_tracking | 2 | Alerts limited to "key periods such as break or termination dates" — renewal/termination, not arbitrary obligation clocks | same |
| 5 | rfi_event_ingestion | 0 | Not a supported source | https://www.luminance.com/ |
| 6 | email_ingestion | 1 | Word-native (Negotiate); no documented email-stream ingestion for event detection | https://www.luminance.com/negotiate/ |
| 7 | daily_report_ingestion | 0 | — | — |
| 8 | schedule_integration | 0 | — | — |
| 9 | change_order_workflow | 1 | Draft can generate variations/amendments from templates | https://www.luminance.com/draft/ |
| 10 | claim_identification | 0 | — | — |
| 11 | delay_detection | 0 | — | — |
| 12 | responsibility_attribution | 0 | — | — |
| 13 | contemporaneous_evidence_graph | 1 | **Investigate** module supports "discovery, arbitrations, and litigation matters"; document-set analysis only | https://www.luminance.com/investigate/ |
| 14 | evidence_completeness | 1 | Missing-clause detection is a completeness test on the *contract*, not on the evidence file | https://www.luminance.com/analyze/ |
| 15 | recoverable_dollar_estimation | 0 | — | — |
| 16 | claim_package_generation | 0 | — | — |
| 17 | notice_drafting | 1 | Automated contract generation exists; notices not a marketed output | https://www.luminance.com/draft/ |
| 18 | schedule_impact_analysis | 0 | — | — |
| 19 | procore_integration | 0 | Not listed | https://www.luminance.com/ |
| 20 | autodesk_integration | 0 | Not listed | same |
| 21 | outlook_gmail_integration | 1 | Microsoft Word add-in confirmed; Outlook/Gmail integration `UNVERIFIED` | https://www.luminance.com/negotiate/ |
| 22 | mobile_workflow | 0 | No mobile product documented | — |
| 23 | audit_trail | 2 | Negotiation history/version tracking; no legal-hold-grade chain-of-custody marketed outside Investigate | https://www.luminance.com/negotiate/ |
| 24 | portfolio_risk | 3 | Enterprise-wide portfolio visibility, anomaly detection, benchmarking; Buro Happold sanctions-portfolio review "weeks condensed to minutes" | https://www.luminance.com/customers/buro-happold/ |
| 25 | performance_pricing_compatibility | 0 | No published pricing; enterprise licence + modules | https://www.luminance.com/ |
| 26 | consultant_replacement_potential | 1 | Investigate displaces some disclosure-review spend in arbitration; not quantum/delay expertise | https://www.luminance.com/investigate/ |

**LUMINANCE SCORES| 3,3,1,2,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,0,2,3,0,1**

### 4C. MICROSOFT 365 COPILOT (the commodity baseline — the one that matters most)

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | 2 | Reads any contract the user can already access in SharePoint/OneDrive/Teams/Outlook; no contract-native ingestion, no repository model | https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365 |
| 2 | clause_extraction | 2 | Will extract clauses on demand with good fluency but no schema, no confidence, no persistence; accuracy ceiling discussed in §7 | Vals VLAIR data extraction: 75.1% best AI vs 71.1% lawyer baseline — https://www.vals.ai/vlair |
| 3 | notice_detection | 2 | *This is the commodity's strongest thesis-relevant capability*: ask "list the notice provisions and their time limits" and you get a usable first-pass list. But no verification, no completeness guarantee | https://www.vals.ai/vlair (Document Q&A 94.8% best AI vs 70.1% lawyer baseline) |
| 4 | deadline_tracking | 1 | **No persistent deadline state.** Copilot is per-prompt and stateless. Recurring/event-driven behaviour requires building a Copilot Studio agent with event triggers | https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about |
| 5 | rfi_event_ingestion | 1 | Only if RFIs happen to live as M365 email/files; nothing reads Procore RFIs | same |
| 6 | email_ingestion | 3 | Native Outlook/Graph grounding is the single strongest thing it has | https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365 |
| 7 | daily_report_ingestion | 1 | Only if daily reports are uploaded to M365 as files; no field capture | same |
| 8 | schedule_integration | 1 | Copilot in Planner/Project exists; no P6/MSP CPM logic, no float/critical-path reasoning | same |
| 9 | change_order_workflow | 0 | No workflow object | — |
| 10 | claim_identification | 0 | No concept of a commercial event | — |
| 11 | delay_detection | 0 | No | — |
| 12 | responsibility_attribution | 0 | No | — |
| 13 | contemporaneous_evidence_graph | 1 | Microsoft Graph links people/files/meetings, and Copilot cites sources, but it is a productivity graph, not an evidence graph | same |
| 14 | evidence_completeness | 0 | No completeness model | — |
| 15 | recoverable_dollar_estimation | 0 | No | — |
| 16 | claim_package_generation | 1 | Can draft a document in Word; cannot assemble a structured, exhibit-linked package | same |
| 17 | notice_drafting | 2 | Genuinely good at drafting a notice letter from contract text — this is table stakes now | same |
| 18 | schedule_impact_analysis | 0 | No | — |
| 19 | procore_integration | 0 | No native connector documented | — |
| 20 | autodesk_integration | 0 | No | — |
| 21 | outlook_gmail_integration | 3 | Outlook is native (Gmail is not) | same |
| 22 | mobile_workflow | 2 | Copilot mobile app + Teams mobile; not a field workflow | same |
| 23 | audit_trail | 2 | Purview captures Copilot interactions for eDiscovery/audit — a real audit trail of *AI use*, not of *notice service* | https://learn.microsoft.com/en-us/purview/edisc-billing |
| 24 | portfolio_risk | 0 | No cross-project aggregation object | — |
| 25 | performance_pricing_compatibility | 0 | Flat $30/user/mo seat licence | https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365 |
| 26 | consultant_replacement_potential | 0 | Replaces none of the expert workflow | — |

**COPILOT SCORES| 2,2,2,1,1,3,1,1,0,0,0,0,1,0,0,1,2,0,0,0,3,2,2,0,0,0**

### 4D. Category best-of (max across all vendors in this report)

**SCORES| 3,3,2,3,1,3,1,1,1,0,0,1,1,1,2,1,2,0,0,0,3,2,3,3,0,1**
(15 = 2 on the strength of Sirion's invoice-line matching / 8–12% spend-leakage claim; 4 = 3 on Icertis/Sirion/Robin obligation alerting; 6 and 21 = 3 on Copilot.)

---

## 5. PRICING — REAL NUMBERS, WITH CONFIDENCE LABELS

### 5A. Published / directly verifiable (HIGH confidence)

| Vendor | Published price | Source |
|---|---|---|
| **DocuSign IAM Starter** | **$45/user/month**, 100 envelopes/user/yr, 1 workflow, "AI search, management and analysis" | https://ecom.docusign.com/plans-and-pricing/iam |
| **DocuSign IAM Standard** | **$50/user/month**, 3-user min, unlimited envelopes, 3 workflows | same |
| **DocuSign IAM Professional** | **$80/user/month**, 3-user min, 10 workflows, AI-Assisted Review | same |
| DocuSign eSignature Standard / Business Pro | **$30 / $45 per user/month** (annual), 100 envelopes/user/yr | https://ecom.docusign.com/plans-and-pricing/esignature |
| **Microsoft 365 Copilot (enterprise)** | **$30.00/user/month paid yearly** | https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365 |
| **Microsoft 365 Copilot Business (SMB add-on)** | **$18.00/user/month paid yearly** (promo, orig. $21.00, through Sept 2026) | https://www.microsoft.com/en-us/microsoft-365/copilot/business |
| M365 Business Premium **with** Copilot | **$32.00/user/month paid yearly** | same |
| **Copilot Studio** | **$200.00/pack/month for 25,000 Copilot Credits**, or PAYG; Azure sub required | https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio |
| **Claude Team** | **$20/user/mo annual** ($25 monthly), 2–150 users | https://claude.com/pricing |
| **Claude Enterprise** | **$20/seat + usage at API rates** | same |
| **Relativity aiR** | **$0 incremental** — aiR for Review/Privilege/Case Strategy "included at no additional cost with RelativityOne" | https://www.relativity.com/pricing/ |
| **Everlaw** | per-GB, **unlimited user licences**, single-doc AI actions "Included (No Extra Cost)" | https://www.everlaw.com/pricing/ |
| **Purview eDiscovery (M365 data)** | included in enterprise subscription; only non-M365 AI data + Graph export metered per GB | https://learn.microsoft.com/en-us/purview/edisc-billing |

### 5B. Aggregator / secondary (MEDIUM confidence — triangulate before use)

- **Icertis**: median annual contract value **$88,000** (attributed to Vendr 2025); first-year all-in **$100k–$300k**; **~34% above CLM market average** (attributed to G2). Source: https://www.hyperstart.com/blog/icertis-pricing/ (9 Jul 2026). Icertis publishes nothing itself.
- **Ironclad**: **$15,000 minimum annual contract**; "$30,000 to $120,000 based on specific business needs"; implementation **$5k–$50k+**. Source: https://www.concord.app/blog/clm-pricing-exposed-real-costs-hidden-fees-vendor-quotes (18 Aug 2025), which claims to use "real quotes, actual invoices" from 47 organisations. Separately, SoftwareAdvice lists Ironclad starting price at **$500/month** (https://www.softwareadvice.com/contract-management/ironclad-profile/, 4.4/5, 64 reviews).
- **Enterprise CLM generally**: "starts around **$50,000 annually** and can climb into six figures"; mid-market **$15,000–$50,000/yr**; SMB **$30–$100 per user/month**. Source: Sirion's own buyer guide, https://www.sirion.ai/library/clm-platform/contract-management-software-cost/ (updated 24 Jul 2026).
- **SAP Ariba CLM** "starts at $200,000 annually"; **LinkSquares** "around $10,000 per year"; **ContractWorks** $399/month; **PandaDoc** $49/user/month with 10-user minimum. Same Concord source.
- **Luminance**: SelectHub lists a range of **$10–$100 per user/month, quote-based** (https://www.selecthub.com/p/legal-software/luminance/) — this looks implausibly low against the "five-to-six figures annually" characterisation elsewhere; treat as `LOW confidence`.
- **Harvey**: aggregator figures are wildly inconsistent (one source says $1,200–$1,500/seat/**month**, another says $100–$200/user/month at 200+ seats, another says $50k–$300k annual contracts with 20–50 seat minimums). **I could not verify any Harvey price against a primary source. Treat all Harvey per-seat numbers as `UNVERIFIED`.**
- **Spellbook**: aggregators cluster around **$99–$199/user/month**, with an enterprise tier reported at ~$350/user/month on 10-seat, 6-month minimums after a late-2025 price rise. Spellbook's own page says only "pricing is determined by the number of team members on a license." `MEDIUM-LOW confidence`.
- **Sirion, Agiloft, Robin AI, LegalOn, Relativity, Everlaw, Ironclad, Luminance, Harvey, Eve**: **no published price**. Verified by fetching each pricing page.

### 5C. What this calibrates for our own pricing

Three price shelves are visible, and they are far apart:
1. **Commodity AI reading**: $18–$32 per user/month (Copilot, Claude Team, Gemini-in-Workspace bundling). This shelf is *falling* and is being given away inside suites.
2. **Repository + AI extraction + alerts, self-serve**: **$45–$80 per user/month** (DocuSign IAM). This is the price of "structured agreement data with AI extraction" bought without a salesperson.
3. **Enterprise obligation management**: **$50k–$500k+/yr plus implementation**, 3–6 month rollouts. This is the price of the *governed, audited, integrated* version.

A construction revenue-recovery product that reads contracts and answers questions is competing on shelf 1–2. A product that owns deadline state, evidence and the audit record is on shelf 3 — but shelf 3 buyers are enterprise legal/procurement, and construction firms mostly do not have that function at that scale.

---

## 6. INTEGRATIONS & DATA EGRESS REALITY

- **Icertis integrations, in full, as published:** SAP (Ariba, S/4HANA), Microsoft (Dynamics 365 F&O, Dynamics 365 Sales, Teams, M365 for the web, Outlook), Salesforce (CRM & CPQ), Workday (financial data), Adobe Sign, DocuSign, SAM.gov, Federal Clause, Whatfix, custom API — plus agent connectors for **OpenAI, Claude (Anthropic), Microsoft Copilot and SAP Joule**. **No Procore. No Autodesk Construction Cloud. No Oracle Aconex. No construction system of any kind.** (https://www.icertis.com/products/platform/integrations/)
- **Agiloft**: "over 1,000 pre-built connectors," Salesforce/SAP/Oracle/DocuSign/Adobe Sign named; no construction system named (https://www.agiloft.com/).
- **Harvey**: iManage, NetDocuments, SharePoint, Google Drive, Word, Outlook, LexisNexis, Rettsdata, Aderant, **Ironclad**, APIs (https://www.harvey.ai/platform). Law-firm DMS plane, not project plane.
- **Robin AI**: "out-the-box integrations" for bulk document import, plus a documented **API** (`/robin-api`) (https://robinai.com/platform, https://robinai.com/sitemap.xml).
- **DocuSign**: the exception — a published **Procore** integration and a construction industry page (https://www.docusign.com/solutions/industries/construction).
- **Copilot Studio**: the honest "build it yourself" path — event triggers include SharePoint item created, OneDrive file created, Planner task completed, and a **Recurrence** trigger; triggers require **generative orchestration turned on**, run on **the maker's credentials** ("event triggers can only use the agent maker's credentials for authentication"), are subject to **admin DLP policies** that can block them entirely, count each trigger payload as a billable message ("a recurrence trigger set to activate every 10 minutes sends a trigger payload as a message to an agent every 10 minutes"), and can be **throttled** for exceeding Power Platform quotas (https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about).

**Egress:** all of these are closed SaaS repositories with API access sold as an add-on (Ironclad explicitly lists "API access" as an optional extra — https://ironcladapp.com/pricing). One Concord-sourced anecdote reports a client facing **"$45,000 in data export fees"** (https://www.concord.app/blog/clm-pricing-exposed-real-costs-hidden-fees-vendor-quotes) — `MEDIUM confidence`, single sourced.

---

## 7. THE COMMODITY BASELINE — TESTED HONESTLY

**Question: how good is a generic LLM at "read this contract and tell me the notice deadlines" today?**

**Answer: very good at the reading, and that is the whole point.** The best published evidence:

- **Vals Legal AI Report (VLAIR), 27 Feb 2025** — the first independent, vendor-participating legal AI benchmark, run against a **lawyer baseline** from independent attorneys answering identical questions (https://www.vals.ai/vlair). Results relevant to us:
  - **Document Q&A**: Harvey **94.8%**, CoCounsel **89.6%**, Oliver **74.0%**, Vincent **72.7%** — vs **lawyer baseline 70.1%**. *AI beats lawyers, decisively, at "answer a question about this document."*
  - **Data Extraction**: Harvey **75.1%**, CoCounsel **73.2%**, Vincent **69.2%**, Oliver **64.0%** — vs **lawyer baseline 71.1%**. *AI is at parity, not superiority.* This is the closest proxy to "extract every notice provision and its time limit," and best-in-class is **~75%**.
  - **Redlining**: Harvey **65.0%**, Vincent **53.6%** — vs **lawyer baseline 79.7%**. *AI loses, badly.*
  - **Chronology generation**: Harvey **80.2%**, tying the lawyer baseline of 80.2%.
  - Speed: AI was "six times faster than the lawyers at the lowest end, and 80 times faster at the highest end."
- **Hallucination is not solved.** Magesh, Surani, Dahl, Suzgun, Manning & Ho, *"Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools"* (30 May 2024, https://arxiv.org/abs/2405.20362) found **17–33% hallucination rates** for Lexis+ AI, Westlaw AI-Assisted Research and Ask Practical Law AI — purpose-built, RAG-grounded, *marketed as hallucination-free* legal tools.
- **Agentic legal work is still weak.** On Vals' **Harvey Legal Agent Benchmark (HLAB)** — "tests an agent's ability to complete legal work using documents, spreadsheets, presentations, and file-system tools," updated **17 Aug 2026**, 22 frontier models — the leaders score **~9–11%** (Claude Fable 5 11.25%, Claude Opus 4.8 9.58%). On Vals' **Legal Research Bench** the leaders score **~39–44% all-pass** (Claude Opus 4.8 43.75%, GPT 5.5 40.39%). By contrast **LegalBench**, a much simpler classification suite, is at **83–89%** (https://www.vals.ai/, https://www.vals.ai/benchmarks/hlab).
- **Construction contracts specifically are harder than generic ones, and the literature says so.** Zheng, Wong, Su, Tang, Nawaz & Kassem, *"Automating construction contract review using knowledge graph-enhanced large language models"* (arXiv, Sep 2023, updated 19 May 2025) needed a **Nested Contract Knowledge Graph** on top of an LLM to beat baseline models on international EPC contracts — i.e. the raw LLM was not sufficient. Companion paper: Wong, Zheng, Su & Tang, *"Construction contract risk identification based on knowledge-augmented language model"* (arXiv, 22 Sep 2023). Neither paper publishes clean headline accuracy numbers in the abstract. **`UNVERIFIED`: I could find no published benchmark of any model on construction *notice-provision* extraction specifically.**

**What the commodity CANNOT do (all verifiable from primary docs, not opinion):**
1. **No persistent deadline state.** Copilot is prompt-scoped and stateless. To make it watch a clock you must build a Copilot Studio agent with a Recurrence trigger — a Power Platform project with maker-credential authentication, DLP-policy exposure, per-payload billing, and quota throttling (https://learn.microsoft.com/en-us/microsoft-copilot-studio/authoring-triggers-about).
2. **No monitoring of project events.** Its grounding is the Microsoft Graph — email, Teams, SharePoint, OneDrive. RFIs, submittals, daily reports, site instructions and schedule updates live in Procore/ACC/Aconex/P6. Microsoft publishes no Procore or Autodesk connector for Copilot grounding.
3. **No evidence linkage.** Copilot cites the file it read; it does not build a durable claim→clause→event→document graph that survives the session.
4. **No audit trail of the thing that matters.** Purview does log Copilot prompts and responses and makes them discoverable (https://learn.microsoft.com/en-us/purview/edisc-billing). That is an audit trail of *AI usage*. It is not an audit trail of *"notice X was served on date Y under clause Z, here is the delivery proof."*
5. **Accuracy that is fine for a draft and not fine for a limitation period.** ~75% extraction accuracy is excellent for triage and unacceptable as the only check on a 14-day time bar where one miss forfeits the entitlement.

**Bottom line for the thesis:** a generic LLM with a contract PDF at $18–$30/user/month already delivers **the contract-reading step and a decent first draft of a notice letter**. It delivers **none** of: event detection over project traffic, entitlement matching, deadline state, evidence assembly, completeness testing, quantum, or the audit record. Roughly speaking, the commodity has taken step 1 of the seven-step pipeline and half of step 7.

---

## 8. WEAKNESSES AND GAPS — DELIBERATE OR UNATTENDED?

| Gap | Deliberate (strategy) or unattended (opportunity)? | Reasoning |
|---|---|---|
| No construction system integrations anywhere (except DocuSign→Procore) | **Deliberate.** Icertis, Sirion and Agiloft have built dozens of ERP/CRM/HCM connectors. They know how. They have not built Procore because their buyer isn't in Procore. | https://www.icertis.com/products/platform/integrations/ |
| No project-event ingestion (RFIs, daily reports, minutes, photos) | **Deliberate.** The CLM data model is contract-centric; adding an event stream means a new object model and a new buyer. | Platform pages, all vendors |
| No claim identification / delay / quantum | **Deliberate — legal exposure.** These vendors sell compliance and governance; asserting entitlement and estimating recoverable dollars is adjacent to giving legal/expert opinion. Nobody in the category makes an entitlement assertion. | Absence across all 14 |
| Obligation modules skew to renewals, terminations and SLAs | **Deliberate.** That is where enterprise money leaks (auto-renewals, service credits). Luminance's alerts are explicitly for "break or termination dates." | https://www.luminance.com/analyze/ |
| No construction standard-form playbooks (AIA/ConsensusDocs/FIDIC/NEC) | **Unattended — genuine gap**, but small TAM per their unit economics, and the incumbent forms publisher (AIA) is moving into it itself. | https://aiacontracts.com/ |
| No field/mobile workflow | **Deliberate.** Their user is at a desk. | Product pages |
| No performance/contingency pricing | **Deliberate.** Enterprise SaaS revenue recognition. | All pricing pages |
| Post-signature modules require heavy configuration to actually work | **Unattended.** See complaints in §10 — the recurring theme is configuration dependency and time-to-value. | §10 |

---

## 9. ADJACENCY TEST — HOW HARD FOR THEM TO SHIP OUR PIPELINE?

**"event detection → entitlement matching → evidence → claim package"**

| Vendor group | Verdict | Reasoning |
|---|---|---|
| **Icertis / Sirion / Agiloft (CLM)** | **HARD** | *Data access*: they have the contract but nothing else — no RFIs, no dailies, no schedule, and no construction connectors. *Org incentive*: their revenue is Fortune-500 legal/procurement seats; construction is a low-ARPU, low-legal-headcount vertical. *GTM*: 3–6 month enterprise sales into CLO/CPO, wrong motion for a $400M contractor's project controls team. *Legal exposure*: none of them asserts entitlement anywhere; that is a deliberate line. *Shipping behaviour*: Icertis is leaderless (CEO out July 2026, interim co-CEOs) and reportedly exploring a $5B sale; Sirion just went to PE majority control in Jan 2026 — neither is in a posture to open a new vertical. |
| **Luminance / Robin AI / Spellbook / LegalOn (contract AI)** | **HARD** | *Data access*: contract text only. *Org incentive*: Luminance just spent Series C money building its own LLM (Luna Crescent) and doing a LexisNexis alliance — that is a horizontal-depth strategy, not a vertical-breadth one. *Legal exposure*: same line. They could ship "construction contract playbooks" in a quarter (that part is **EASY**), but the pipeline beyond clause extraction is **HARD**. |
| **Harvey / Eve (law-firm AI)** | **MEDIUM** | *Data access*: Harvey already sits inside iManage/NetDocuments where a construction disputes practice keeps its matter files — that is exactly the evidence corpus. *Org incentive*: Harvey sells horizontally across practice areas and is unlikely to build construction-specific entitlement logic, but a firm could assemble it in Harvey Workflows. Eve proves the vertical-by-buyer model works ($103M Series B, 1,200+ firms, "nightly audits of active caseloads to surface missed opportunities") — an "Eve for construction disputes" is a **credible and near** competitor. |
| **Microsoft / Google (commodity)** | **MEDIUM on capability, HARD on intent** | The Copilot Studio primitives (event triggers, Recurrence, connectors, Power Automate) are sufficient to build a crude deadline monitor today. Microsoft will not build a construction-claims product; a **partner or a customer's IT team will**, and that is the real substitution risk — a competent contractor IT group could stand up a 60%-solution internally for the price of Copilot licences plus a $200/month credit pack. |
| **DocuSign** | **MEDIUM** | Only vendor with construction GTM + Procore integration + a published $45–$80/user/mo AI repository. If anyone in the horizontal set stumbles into this, it is DocuSign — but its centre of gravity is signature and agreement data, not entitlement. |
| **Relativity / Everlaw** | **HARD (upstream), and already ROADKILL-adjacent (downstream)** | They own the *dispute* stage after documents are collected. They will not move upstream into live projects. But note: aiR is now **bundled at no extra cost**, which means AI document review as a *paid feature* has already been commoditised inside eDiscovery. |

---

## 10. TOP CUSTOMER COMPLAINTS RELEVANT TO THE THESIS (verbatim)

Review coverage of this category is genuinely thin (G2, TrustRadius, Gartner Peer Insights and Reddit all refused fetch; PeerSpot has **zero** reviews for Sirion — "We have not yet collected reviews for Sirion"). What I could obtain:

1. **"Too many dependencies on back end team for configuration. A lot of downtime."** — Nilesh K., Legal Services, 10,000+ employees, Nov 2022, on Icertis. https://www.softwareadvice.com/contract-management/icertis-profile/
2. **"A bit clunky with larger agreements; negotiations often occur outside software."** / **"Uploading third-party contracts to the system is difficult."** — Trevor J., daily user, Apr 2018, on Icertis. Same URL. *(Directly relevant: construction subcontracts are almost always third-party paper.)*
3. **"It is practically impossible to find old documents and contracts"** — harry w., Computer Software, 501–1,000 employees, Dec 2025, on Ironclad. https://www.softwareadvice.com/contract-management/ironclad-profile/
4. **"Setup and customization can take time for complex workflows"** — Janapher S., Insurance, 1,001–5,000 employees, Jul 2026, on Ironclad. Same URL.
5. **"Very costly and I do not recommend it for small businesses"** — VR, Research, 2–10 employees, Jan 2026, on Ironclad. Same URL.
6. On Luminance, aggregated user limitations: **"Luminance may not be suitable for all legal tasks, particularly those outside of its pre-trained areas"**; **"Achieving optimal performance for niche legal tasks may require extensive data tagging and training"**; it **"sometimes struggles to provide the context and nuanced understanding that a human lawyer would bring."** https://www.selecthub.com/p/legal-software/luminance/ (`MEDIUM confidence`, undated aggregation).
7. Icertis on Software Advice sits at **4.3/5 from 41 reviews**; Ironclad at **4.4/5 from 64 reviews** — note how small those review counts are for platforms costing $88k–$300k/yr. That is an enterprise-procurement product with almost no bottom-up voice.

**The thesis-relevant pattern:** the complaints are about *configuration dependency, third-party paper, retrieval, and cost* — not about the AI's reading ability. The horizontal product's failure mode is exactly the failure mode that would kill it in construction, where every subcontract is third-party paper and nobody has a back-end configuration team.

---

## 11. HARDEST FACTS (top 10, all with URL)

1. **DocuSign IAM publishes $45 / $50 / $80 per user/month** for tiers that all include "AI-powered data extractions" and an agreement repository — the true commodity price of "structured contract data with AI." https://ecom.docusign.com/plans-and-pricing/iam
2. **Microsoft 365 Copilot is $30.00/user/month paid yearly** (enterprise); the SMB add-on is **$18.00/user/month** on promo through Sept 2026. https://www.microsoft.com/en-us/microsoft-365/enterprise/copilot-for-microsoft-365 ; https://www.microsoft.com/en-us/microsoft-365/copilot/business
3. **Vals Legal AI Report (27 Feb 2025): best AI data extraction = 75.1% vs 71.1% lawyer baseline; best Document Q&A = 94.8% vs 70.1%; best redlining = 65.0% vs 79.7% lawyer baseline.** AI wins at answering, ties at extracting, loses at redlining. https://www.vals.ai/vlair
4. **Leading legal-research AI tools hallucinate 17–33% of the time** (Stanford RegLab/HAI preregistered study, 30 May 2024). https://arxiv.org/abs/2405.20362
5. **Sirion claims 99% on-time obligation compliance, 80% reduction in post-signature disputes, 60% lower cost of contract governance, and 8–12% reduction in spend leakage** — hypothesis A, already productised and quantified, for enterprises. https://www.sirion.ai/platform/manage/
6. **Icertis' published integration list contains zero construction systems** — no Procore, no Autodesk, no Aconex. https://www.icertis.com/products/platform/integrations/
7. **Sirion's published industry list (8 verticals) and Agiloft's (7 verticals) both exclude construction/E&C/AEC entirely.** https://www.sirion.ai/solutions/ ; https://www.agiloft.com/
8. **Relativity now includes aiR for Review, aiR for Privilege and aiR for Case Strategy at no additional cost with RelativityOne**, and an independent study found aiR for Review "cuts human review hours by 98% with higher recall than active learning." https://www.relativity.com/pricing/ ; https://www.relativity.com/data-solutions/air/review
9. **Icertis median annual contract value $88,000; first-year all-in $100k–$300k; ~34% above CLM market average** (`MEDIUM confidence`, aggregator citing Vendr 2025 and G2). https://www.hyperstart.com/blog/icertis-pricing/
10. **Luminance's flagship E&C customer, Buro Happold, uses it for pre-signature legal review and repository Q&A — 90% time savings, urgent inquiries from 2 hours to 15 minutes — with no mention of notices, claims, NEC/FIDIC/JCT/AIA, or project events.** https://www.luminance.com/customers/buro-happold/

Runners-up: Harvey processes "50M+ files per day" / "850,000+ queries per day" and claims 200,000+ lawyers (https://www.harvey.ai/platform, /customers). Eve: $103M Series B, "1,200+ firms," plaintiff-only (https://www.eve.legal/). Luminance: 1,000+ organisations, 70 countries, $75M Series C early 2025 (https://www.luminance.com/about/). Spellbook: 4,500+ customers, 80+ countries, AtkinsRéalis a named logo (https://spellbook.com/). AIA Contract Documents: 1,000,000+ contracts/yr, 15,000+ subscribers, 45,000+ companies, now with an AI assistant (https://aiacontracts.com/). Icertis: >$500M raised, $5B valuation, CEO departed Jul 2026, exploring sale (https://www.geekwire.com/2026/icertis-ceo-is-departing-contract-management-company-names-cfo-and-board-member-interim-leaders/). Sirion: Haveli majority investment, 8 Jan 2026.

---

## 12. STARTUP POSTURE — PARTNER, CHANNEL, OR ROADKILL?

- **vs Icertis / Sirion / Agiloft / Ironclad (CLM):** **PARTNER, tending to irrelevant.** They will never have the project data. Their contract repository is a *source* we would want to read, not a competitor for the workflow. In practice most contractors do not run a CLM at all, so the integration is optional. Neither is in an acquisitive posture (Icertis leaderless and for sale; Sirion PE-controlled).
- **vs Luminance / Robin AI / Spellbook / LegalOn:** **PARTNER on clause extraction, competitor on positioning.** The real risk is narrative, not product: a contractor's GC who has already bought Spellbook or Luminance will ask "doesn't my tool already do this?" The answer is no — but you have to prove it in the first meeting.
- **vs Harvey / Eve:** **CHANNEL — and the most interesting relationship in this report.** Construction disputes law firms (Reed Smith, CMS, Dentons, Clyde & Co, Vinson & Elkins) are already Harvey/Luminance customers with construction practices. Selling *through* the firm — the firm brings the tool to the contractor client as part of a contract-administration or claims-avoidance retainer — solves the hardest thing about the contractor sale (no budget line, no legal headcount, project-by-project buying).
- **vs Microsoft / Google:** **ROADKILL RISK, at the low end only.** Anything whose whole value is "chat with your contract" gets absorbed at $18–$30/seat. Anything whose value is persistent state + evidence + audit record does not, because building that on Copilot Studio is a real engineering project with credential, DLP and quota constraints.
- **vs Relativity / Everlaw:** **PARTNER, downstream.** They own the dispute once it is a dispute. A product that produces a well-evidenced, contemporaneous record *before* the dispute reduces their review volume — commercially neutral to them, and a natural referral relationship with the disputes bar.
- **vs Document Crunch:** not in my scope, but note that the *vertical* competitor — not the horizontal one — is the live threat: 500+ construction companies including Balfour Beatty, DPR, Swinerton, Webcor, Boldt, Barton Malow, already generating "submittals, RFIs, notices" with clause-grounded citations (https://www.documentcrunch.com/).

---

## 13. DIRECT ANSWERS TO THE FOUR KEY QUESTIONS

**(1) Why hasn't horizontal CLM/obligation-management taken construction — durable, or timing accident?**
**Durable, with one soft edge.** Three structural reasons, all evidenced: (a) **wrong object** — CLM models a contract as a standing enterprise asset with renewal/termination/SLA clocks; a construction contract's live obligations are triggered by *project events* that CLM has no representation of; (b) **wrong buyer** — CLM is sold to CLO/CPO on 3–6 month enterprise cycles at $88k median ACV, and construction firms have thin legal functions and project-level (not enterprise-level) budgets; (c) **wrong data plane** — Icertis' full published connector list is SAP/Microsoft/Salesforce/Workday/DocuSign/SAM.gov with **zero** construction systems, and Sirion and Agiloft do not even list construction as a vertical. (a) and (c) are durable — they would each require a new object model and a new integration surface, both of which these vendors are capable of and have deliberately declined to build for a decade. The soft edge is (b): if a big-enough contractor cohort ever centralises contract administration, DocuSign — which already has the construction GTM and the Procore integration — is best placed to move, and its $45–$80/user/mo published tier is much closer to what a contractor would pay than Icertis' $88k ACV.

**(2) How much does a generic LLM at ~$30/user/month already deliver, and what is left?**
**It delivers roughly step 1 of 7, plus half of step 7.** Concretely, it delivers: read the contract; list the notice provisions, time bars and conditions precedent; answer follow-up questions with citations; draft a serviceable notice letter. On the best published proxy, that reading is ~75% accurate on extraction and ~95% on document Q&A — better than a lawyer at Q&A, at parity on extraction. **What is left, and is not close to solved by the commodity:** (i) knowing an event happened at all — no LLM is watching your RFI log, your dailies or your schedule updates; (ii) persistent deadline state that survives the session and escalates — requires a Copilot Studio agent with Recurrence triggers, maker credentials, DLP approval, and metered credits; (iii) linking the entitlement to the specific contemporaneous documents that prove it, durably; (iv) testing evidence *completeness* against what a tribunal will want; (v) quantum; (vi) the audit record that a notice was served, when, by whom, under which clause, with delivery proof. Items (i)–(iii) and (vi) are the defensible remainder, and they are all *state and workflow*, not *language*.

**(3) Does cheap generic contract Q&A compress the pricing ceiling?**
**Yes for the reading layer, no for the state layer — and you must price on the state layer.** Three published shelves make this concrete: $18–$32/user/mo for AI reading bundled into productivity suites; $45–$80/user/mo for a repository with AI extraction bought self-serve (DocuSign IAM); $50k–$500k+/yr for governed, audited, integrated obligation management. Additional deflationary evidence: **Relativity now bundles aiR at no incremental cost** and **Everlaw includes single-document AI actions free** — AI document analysis as a separately-priced feature is already dying in the adjacent eDiscovery market. Implication: a per-seat "contract copilot for construction" is capped at roughly $50–$150/user/month. A per-project or per-portfolio product that owns deadline state, evidence and the audit record can price against the *value at risk* (a single missed 14-day notice), not against Copilot — and that is the only durable pricing story. Anchoring to seats is how you get commoditised.

**(4) Is the real buyer construction law firms rather than contractors?**
**Law firms are the best first *channel*; contractors remain the best long-term *buyer*.** Evidence for firms: Harvey claims 200,000+ lawyers and 92% monthly adoption, with named customers including several of the largest construction-disputes practices (Reed Smith, CMS, Dentons, A&O Shearman), and integrates with the DMS (iManage/NetDocuments) where the matter evidence already lives; **Eve proves the model** — a vertical-by-buyer legal AI for plaintiff firms, $103M Series B, 1,200+ firms, doing "nightly audits of active caseloads to surface missed opportunities," which is structurally the same product as "nightly audits of active projects to surface missed notices." Firms have budget, a professional-services pricing culture that tolerates value pricing, and a client-relationship reason to bring the tool in. Evidence against firms as the end state: firms are engaged *after* entitlement is already prejudiced, which is exactly the failure the thesis is trying to prevent; the recurring revenue is per-matter and lumpy; and the money at stake belongs to the contractor. **Recommended read: sell through construction disputes practices and claims consultancies as a channel to win the first 10–20 logos and the domain credibility, while building the product for the contractor's project controls / commercial manager, who is the eventual seat-and-project buyer.** For a solo founder this is also the cheapest GTM in the report — one construction partner at one firm can introduce five contractor clients, versus a 3–6 month enterprise CLM-style cycle.

---

## 14. UNKNOWNS — AND WHAT WOULD SETTLE THEM

| Unknown | What would settle it |
|---|---|
| Whether Icertis' construction sub-page is genuinely retired or a transient 404 | A crawl of icertis.com's sitemap.xml over time, or asking an Icertis AE directly; an archived snapshot comparison (web.archive.org was unreachable from this environment) |
| Real Icertis / Sirion / Agiloft contract values | A public-sector procurement award document (state/county/federal) naming the vendor and the annual licence fee; USAspending.gov's award search API (requires POST, unavailable to this toolchain) |
| Harvey's actual per-seat price | Any primary source — a law firm's published tender, a Legaltech News piece quoting a firm CFO. Every aggregator figure I found contradicted the others; **do not use any Harvey per-seat number from this report** |
| Whether any CLM vendor has a construction contractor as a *named* customer beyond Shermco | Vendor case-study libraries filtered by industry; ENR Top 400 contractors' tech-stack disclosures |
| Accuracy of any model specifically on construction notice provisions | No published benchmark exists. A 100-clause hand-labelled set across AIA A201, ConsensusDocs 200, FIDIC Red Book 2017 cl. 20.2 and NEC4 cl. 61.3 would settle it — and building it is itself a defensible asset |
| Google Workspace and ChatGPT Business/Enterprise per-seat prices | Both pages refused fetch (Workspace prices did not render; openai.com returned 403). Fetch from a residential IP or a Google/OpenAI partner price list |
| Whether Sirion under Haveli will cut or expand vertical investment | Haveli's portfolio-company announcements; Sirion product releases through H2 2026 |
| Whether any horizontal vendor ships construction standard-form playbooks | Direct demo request; none is documented publicly today |
