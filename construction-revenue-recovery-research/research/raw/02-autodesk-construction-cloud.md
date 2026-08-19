# TARGET REPORT 02 — Autodesk Construction Cloud (now "Autodesk Forma")

**Researched:** 2026-08-19 · **Analyst note:** all claims carry a URL. Anything I could not verify is tagged `UNVERIFIED`.

> **CRITICAL NAMING CHANGE.** On 2026-02-17 Autodesk announced that Autodesk Construction Cloud (ACC) is rebranded **Forma**, effective **2026-03-24**. Autodesk Docs → **Forma Data Management**; Autodesk Build → **Forma Build**; Takeoff → **Forma Takeoff**; BIM Collaborate Pro → **Forma Design Collaboration**; Accounts → **Hubs**. Autodesk states: *"No URL, login, API, or integration changes – Everything continues to function as it does today."*
> Source: https://www.autodesk.com/blogs/construction/autodesk-construction-cloud-is-now-autodesk-forma-heres-what-that-means-for-you/ (updated 2026-03-25). Corroborated in the 10-Q: *"By bringing Autodesk Construction Cloud's leading 26 construction management tools into Autodesk Forma…"* — https://www.sec.gov/Archives/edgar/data/769397/000076939726000044/adsk-20260430.htm (filed 2026-05-29).
> Throughout this report I use ACC/Forma interchangeably; product help pages already say "Forma Build".

---

## 1. SNAPSHOT

**What it is.** Autodesk, Inc. (NASDAQ: ADSK) is a ~$7.2B-revenue design and make software company. Its construction management suite — historically Autodesk Construction Cloud, now Forma — comprises Forma Data Management (ex-Autodesk Docs), Forma Build (ex-Autodesk Build; RFIs, Submittals, Issues, Forms, Photos, Meetings, Correspondence, Assets, Schedule, Sheets, **Cost Management**), Forma Takeoff, Forma Estimate, BIM Collaborate / Design Collaboration, plus acquired assets: BuildingConnected + Bid Board Pro + TradeTapp (bidding/prequal), ProEst (estimating), Assemble (model conditioning), Pype AutoSpecs + Pype Closeout (spec/submittal AI), Payapps/GCPay (payment applications), and legacy BIM 360 and PlanGrid.

**Scale / ownership (hard numbers).**
| Metric | Value | Source |
|---|---|---|
| FY2026 total net revenue (FYE 2026-01-31) | **$7,206M** | 10-K https://www.sec.gov/Archives/edgar/data/769397/000076939726000015/adsk-20260131.htm |
| FY2026 AECO product-family revenue | **$3,583M**, +22% YoY (FY25 $2,937M, FY24 $2,580M) | same 10-K |
| Q1 FY2027 (3mo to 2026-04-30) revenue | **$1,934M**; AECO **$970M**, +20% | 10-Q https://www.sec.gov/Archives/edgar/data/769397/000076939726000044/adsk-20260430.htm |
| Goodwill at 2026-01-31 | **$4,295M** | 10-Q (same) |
| "Construction management tools" in ACC/Forma | **26** | 10-Q (same) |

**Who it sells to / ICP.** General contractors, specialty/trade contractors, owners, and design firms. Unlike Procore, Autodesk's centre of gravity is **design-to-build data continuity** (Revit/BIM → Docs → Build), so its strongest ICP is design-led GCs and owners with heavy model workflows, plus the very large enterprise accounts served through EBAs (Enterprise Business Agreements — a named growth driver in the 10-K).

**Geography.** Global. FY2026 revenue split: Americas $3,178M / EMEA + APAC the balance (10-K). Payapps gives it AU/NZ/UK/IE statutory-payment coverage; GCPay gives North America lien-waiver coverage.

**Competitive framing.** Autodesk's own 10-K names **Procore Technologies, Inc.** among primary global competitors (alongside Bentley, Trimble, Hexagon, Oracle, Nemetschek). https://www.sec.gov/Archives/edgar/data/769397/000076939726000015/adsk-20260131.htm

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 Cost Management — the commercial workflow (DEEP)

This is the single most important finding of this report: **Autodesk's change-order machinery is genuinely deep — deeper than most people assume — and it is a mature, multi-party commercial workflow, not a toy.**

**Change order object model** (verbatim from Autodesk help):
> "PCO (Potential Change Order) is a starting point of the change order workflow… One or more PCOs can form a COR. One or more CORs can form an OCO. One or more SCOs can be generated from a single OCO."
> https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/Cost_Change_Orders_Overview.html

So the chain is **Cost Item → PCO → RFQ → COR → OCO → SCO**, with a hierarchy view that groups every downstream change order back to its originating PCO. Columns include Estimated / Proposed / Submitted / Committed / Approved, plus computed **Budget Impact** and **Cost Impact** that switch which value they use based on status.

**PCO fields that matter to this thesis** (https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/change-orders/Cost_Potential_Change_Orders.html):
- **Scope**: `In Scope` (cost-side only) / `Budget Only` / `Out of Scope` / `Contingency`. This is a genuine entitlement-adjacent distinction — "out of scope" vs "contingency-funded" is the commercial question.
- **Source Type** — a built-in commercial-event taxonomy, defaults: **ASI (Architect's Supplemental Instruction), CCD (Construction Change Directive), INT (Internal), ISSUE, RFI, RFP, T&M (Time and Materials)** — extensible by admins.
- **Source Ref #** — links back to the originating record.
- Create-a-PCO **directly from an RFI, Issue, or Submittal item** via the References panel; or link existing PCOs to those items. The RFI then appears in the change order's Linked References.
- Cost items importable from Excel (up to 100 batch-created), financial markup, internal budget transfers, forecast-adjustment-driven PCOs, and a **Collaborative PCO / change-order-transfer** flow for external parties with "collaborate" permission.

**Contracts & payment applications** (https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/Cost_About_Payments.html):
Main Contract → Schedule of Values → Billing Periods → Budget Payment Application (to owner) / Cost Payment Application (to supplier). Supports **retention**, **overbilling** detection, **advance payments & recoupment**, **foreign currency**, **payment stages (initial/progress/final)**, supplier input request/review, document generation from templates, and aggregated cost reports. Nov-2025 release added stage-specific compliance requirements.

**Construction Change Directives are handled explicitly** — verbatim:
> "Construction Change Directives (CCD) are used when work must proceed without an agreed price. Contractors can bill for completed work using estimated values under the Owner Directive change order type. As long as the OCO with CCD has a status of at least Open, it can be added to a budget payment application."
> https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/change-orders/Cost_COR_OCO_SCO.html

That is a real, non-trivial entitlement-adjacent workflow (bill for directed work at estimated value pending agreement).

**Compliance requirements** (https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/setup-cost/manage-documents-in-cost/Cost_Compliance_Requirements.html):
> "you can track and store lien waivers, certificates of insurance, bonding documents, and other required materials before submissions proceed… The system tracks compliance status and can block submissions until requirements are met."
Applies to Contracts, Cost Payment Applications, OCOs, RFQs, SCOs. Supports **expiration dates**, **calendar integration**, tax-based rules, and **condition-based rules using TradeTapp supplier risk data**. This is a document-obligation engine with deadlines — but for *insurance/waiver/bond compliance*, not contractual notice.

**GCPay integration** (https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/setup-cost/cost-integrations/Cost_GCPay_Integration.html): subcontractors submit pay apps in GCPay, which sync into Cost Management; lien waivers and compliance docs tracked centrally; SOV broken down at budget-code level.

**What is conspicuously absent from Cost Management.** No entitlement concept. No notice clause, notice register, or notice deadline. No time-impact / extension-of-time field on a change order. No delay or disruption cost head (prolongation, acceleration, loss of productivity). No claim object. No "days" on a PCO. The word "claim" does not appear anywhere in the Cost Management help tree I traversed; the Cost Management marketing page contains **no** mention of claims, disputes, entitlement or notices (https://construction.autodesk.com/workflows/construction-cost-management/).

### 2.2 Forma Build — RFIs, Issues, Submittals, Meetings, Photos, Correspondence

**RFIs.** RFI types drive workflow (default, or with an RFI Coordinator role), and each type carries a **Due date in calendar days**, **Cost impact (Yes/No/Unknown)**, **Schedule impact (Yes/No/Unknown)**, Priority, Discipline, Category, External ID. https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/admin-rfis/RFI_Types.html
On creation you set **Ball in court**, reviewers, and attach **References: Files, Sheets, Photos, Submittals, Issues, Schedule, Assets, PCO, Forms or other RFIs**. https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/work-rfis/Create_RFI.html

> **Notable — AI is already touching commercial fields.** The same help page: *"You can use the integrated AI-powered assistant to automatically populate fields in the RFI creation form from a simple text prompt."* Supported fields include **Title, Question, Category, Discipline, Cost Impact, Schedule Impact, Priority, Location Details**, and *"RFIs generated using AI will be logged in the activity log."* This is Autodesk auto-classifying cost and schedule impact from free text — the first step of commercial event detection, shipped.

**Meetings.** Agendas, attendance, decisions, action items with due dates, official minutes generation and distribution, and **references from Files, RFIs, Issues and other tools**; mobile. https://help.autodesk.com/cloudhelp/ENU/Build-Meetings/files/getting-started-meetings/About_Meetings.html

**Photos.** Unified photos/videos tool; new experience with albums and album-level permissions launching 2026-03-24. AutoTags applies ML metadata to photos. https://help.autodesk.com/cloudhelp/ENU/Build-Gallery/files/Photos_About.html ; https://construction.autodesk.com/workflows/artificial-intelligence-construction/

**Daily field records.** Field capture is delivered through configurable **Forms** templates (create-from-template, fill, modify, retrieve — API supports POST/PATCH) plus Photos and Issues. I could **not** locate a current, dedicated "Daily Logs" help book for Forma Build; the "daily construction report" marketing page is about the *Reports* engine, not a structured daily-log object (https://construction.autodesk.com/tools/construction-daily-reports/). A third-party integration vendor lists `Dailylogs` as an extractable object (https://datagrid.com/integrations/autodesk-construction-cloud-acc) — `UNVERIFIED` against Autodesk documentation. Treat structured weather/manpower/labour-hour capture as **template-dependent, not guaranteed**.

### 2.3 EMAIL INGESTION — yes, and it is real

**Autodesk Build/Forma Build has a native Correspondence tool with an email-ingestion path.** This is a materially different posture from "no email story".

> "External Email Correspondence Integration: The tool includes the ability to file correspondence from external email providers, thus ensuring no communication is left out of the project's record."
> https://help.autodesk.com/cloudhelp/ENU/Build-Correspondence/files/getting-started-correspondence/About_Correspondence.html

Mechanism, per an Autodesk reseller's release write-up (public beta 2023-05-24):
> "add in your unique Project Email Address to your recipient line in outlook" — and users can "reply to the thread from within the app as well as add attachments and references to other information in the Hub", including referencing an Issue to an email thread.
> https://www.arkance.us/blog/autodesk-construction-cloud-new-correspondence-tool-release

Autodesk's own admin settings corroborate a bulk-upload path: an Advanced Setting named **"Upload Emails - Private By Default"**, described as applying "when uploading external emails", and a note that "This setting doesn't apply to external emails filed into the system."
https://help.autodesk.com/cloudhelp/ENU/Build-Correspondence/files/getting-started-correspondence/Administration_Correspondence.html

Correspondence supports: **custom correspondence types** with initials embedded in the item ID (so a firm can literally create a "NOTICE" or "EOT" type), recipients including non-members, **status and due date**, attachments from device or Project Files, **references** to other records, rich-text, archive/unarchive, per-type visibility/creation permissions, and email-reply threading.
https://help.autodesk.com/cloudhelp/ENU/Build-Correspondence/files/work-correspondence/Create_Correspondence.html

**But note the two gaps that matter to a startup:**
1. **Correspondence is not in the Data Connector extraction list** (see §5). The official extracted-data list includes Cost, Issues, RFIs, Submittals, Schedule, Meeting minutes, Photos, Forms, Markups, Reviews, Transmittals, Relationships — **not Correspondence**. https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Data_Connector.html
2. I found **no public Correspondence API** in APS. The Autodesk-published Build Postman collection repo covers Forms, Locations, Photos, RFIs, Submittals and AutoSpecs — no Correspondence, no Cost. https://github.com/autodesk-platform-services/aps-autodesk.build.api-postman.collection/

So: Autodesk *captures* email into the record, but the emails are **the least egress-able asset in the platform**. That is a strategically interesting seam.

### 2.4 Pype — the closest thing Autodesk has to clause extraction

**What Pype is.** Acquired 2020-08-17 (announced 2020-07-22), price undisclosed. Products at acquisition: AutoSpecs, SmartPlans, Closeout, eBinder.
https://www.prnewswire.com/news-releases/autodesk-completes-acquisition-of-ai-powered-software-provider-pype-301112786.html

**AutoSpecs — what it actually extracts.** From the spec book (technical specifications, i.e. CSI Divisions), AutoSpecs uses AI to extract:
> "Action submittals, Product data, Closeout submittals, QA/QC submittals, Tests & inspections"
plus a **Suggested Submittals** feature "powered by Construction IQ" that "analyzes the current project specification against historical project data" to surface likely-missing submittals; plus **Versioning** that "tracks differences across design iterations and identifies modified submittal requirements"; plus **Spec View** side-by-side PDF/requirement view.
https://construction.autodesk.com/tools/autospecs-construction-submittal-log/

Operationally it works on **specification PDFs**, produces a **Smart Register** (sections + submittals, configurable columns, custom columns of type text/date/number), and can **publish submittals to Forma Build's Submittals tool or to Forma Data Management Files**.
https://help.autodesk.com/cloudhelp/ENU/AutoSpecs/files/Smart_Register.html ; https://help.autodesk.com/cloudhelp/ENU/AutoSpecs/files/spec-view/View_Edit_Add_Submittals_Spec_View.html

**Pype Closeout** "extracts commissioning requirements from specifications", notifies trade partners of their obligations, collects documents from subs, and compiles PDF turnover packages.
https://www.autodesk.com/products/pype/overview

**The honest verdict on Pype as "clause extraction":**
- ✅ It **is** genuine requirement/obligation extraction from long PDF documents with ML, in production, at scale, with versioned diffing. Autodesk owns a working document-obligation-extraction capability and the team behind it.
- ❌ It is pointed at the **wrong half of the contract documents**. AutoSpecs and Closeout read **Divisions 01–49 technical specifications** — submittals, tests, inspections, closeout deliverables. They do **not** read Division 00 / general conditions / supplementary conditions / the agreement — i.e. the place where **notice periods, claim procedures, extension-of-time mechanisms, change-order valuation rules, dispute escalation, and time bars** actually live. Nothing in Autodesk's public material describes AutoSpecs extracting a notice period, a claims clause, or a liquidated-damages provision.
- ❌ **The product line has been cut back, not expanded.** Pype **SmartPlans and eBinder were withdrawn from sale on 2024-03-26**, and Autodesk's own FAQ states that "once your current contract ends, you will no longer be able to access project data in eBinder or SmartPlans." Autodesk's stated rationale: "Pype AutoSpecs and Pype Closeout are the most widely adopted by customers and remain a focus of the development team."
  https://www.autodesk.com/blogs/construction/important-notice-regarding-pype-ebinder-and-or-pype-smartplans-subscription-faq/
- ❌ **The AutoSpecs API is a stub.** First release (2023-04-14) shipped **four read-only endpoints** — project metadata, smart register, requirements, summary — **3-legged auth only**, and even UI-visible data (subcontractor, source version, PDF link) is not exposed. No write. No document-level access.
  https://aps.autodesk.com/blog/autospecs-api-autodesk-construction-cloud
- ⚠️ **Packaging shift:** AutoSpecs and Closeout are now "only available through Forma for Construction Operations" — i.e. bundled into a suite, no longer standalone products. https://www.autodesk.com/products/pype/overview

**Read-through:** Autodesk had the closest adjacent asset in the industry to contract-clause extraction, and over six years it *narrowed* it to submittal logs and closeout packages, killed two of the four products, and gave it a four-endpoint read-only API. That is a deliberate de-prioritisation of document-AI-as-a-platform, not an accident.

### 2.5 Autodesk AI / Construction IQ — what it actually predicts

**Construction IQ** predicts risk in four domains and **none of them is commercial**:
> "Design Risk Factors… RFI Risk Factors helps teams identify RFIs that pose the greatest risk to project cost and schedule… Quality Risk Factors… Safety Risk Factors"
> https://construction.autodesk.com/tools/construction-iq/
It reviews issues/checklists/observations, ranks issues high/medium/low, estimates cost-to-fix for quality issues, and scores subcontractor risk. Autodesk explicitly disclaims accuracy: *"not every issue that Construction IQ identifies as high risk may be a high-risk issue, and… may not detect every high-risk issue."* https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Insight_Construction_IQ.html
Algorithms are "optimized for Commercial, Healthcare, Institutional, and Residential projects only" (same source).
Usage claim: Construction IQ "Trusted over 5 million times in the last year." https://construction.autodesk.com/workflows/artificial-intelligence-construction/

**Does it touch commercial entitlement? No.** The nearest adjacency is *RFI Risk Factors* — flagging RFIs likely to hurt cost/schedule. That is triage, not entitlement. There is no change-order risk model, no notice-deadline model, no claim-value model, no contract-clause model.

**Autodesk Assistant** (conversational AI across Forma, updated 2026-05-26). Its seven marketed everyday tasks:
1. Find related specifications for RFIs · 2. Assess project risk before problems escalate · 3. Summarize meetings and identify key action items · 4. Track safety topics across meetings · 5. Check schedule health at a glance · 6. Get high-level project health snapshots · 7. **Identify RFQs impacting project budget**
https://www.autodesk.com/blogs/construction/7-everyday-construction-tasks-made-faster-with-autodesk-assistant/
This is retrieval + summarisation over project data, gated by "license type and user permissions". Item 7 is the only commercial one and is described as connecting RFQs to cost changes — reporting, not entitlement.

Autodesk's Q1 FY27 10-Q states the strategy plainly: *"Autodesk has invested in the development, scaling, and monetization of agentic AI… Our strategy is built on the foundational pillars of proprietary data, deep contextual integration, and specialized AI expertise."* — i.e. AI as a platform feature that increases seat value, not as a new commercial-services product line. https://www.sec.gov/Archives/edgar/data/769397/000076939726000044/adsk-20260430.htm

### 2.6 Schedule

The Schedule tool **imports** from **Primavera P6, Microsoft Project and Asta Powerproject**; Gantt view; **version control to view and compare schedule versions**; each activity **linkable to objects across the platform**; granular permissions and attribute-level visibility control; **Schedule Managers** role.
**Workplan** adds Last-Planner-style production planning: task commitments, **Percent Plan Complete (PPC)**, and **"root causes for delays"** metrics.
https://help.autodesk.com/cloudhelp/ENU/Build-Schedule/files/About_Schedule.html
Schedule is an extractable Data Connector object and an attachable RFI reference.

**What it is not:** there is no CPM engine, no critical-path/float analysis surfaced for forensic use, no time impact analysis, no as-planned-vs-as-built windows analysis, no fragnet insertion. "Root causes for delays" is production-plan variance coding (Lean), not delay-event causation.

### 2.7 Other assets in the wider portfolio
- **Takeoff / Estimate / ProEst** — quantity takeoff and estimating (ProEst acquired Dec 2021, price undisclosed).
- **BuildingConnected / Bid Board Pro / TradeTapp** — bid management and subcontractor prequalification/risk. TradeTapp risk data feeds Cost Management contract compliance rules.
- **Assemble** — model conditioning/quantification; now sold in the Forma for Model Management bundle.
- **Payapps / GCPay** — see §7 and §8; this is the strategically loudest signal in the whole report.
- **BIM 360 (legacy)** — still receiving monthly Cost Management release notes as recently as Nov 2025: https://blogs.autodesk.com/bim360-release-notes/2025/11/18/bim-360-cost-management-november-2025/
- **PlanGrid (legacy)** — verbatim from Autodesk: *"PlanGrid is no longer available for purchase by net-new customers. Forma Build was developed by combining the best-in-class features of PlanGrid and BIM 360."* Existing users retain web/mobile/Windows access. https://construction.autodesk.com/products/plangrid/

---

## 3. CAPABILITY MATRIX (0–3)

| # | Dimension | Score | Justification + URL |
|---|---|---|---|
| 1 | contract_ingestion | **2** | Structured Contract objects (main contract + subcontracts) with SOV, billing periods, retention, attached documents and compliance packets; documents stored in Forma Data Management. But contracts are *keyed in*, not parsed. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/Cost_About_Payments.html |
| 2 | clause_extraction | **1** | Pype AutoSpecs extracts *submittal/test/closeout requirements* from technical specification PDFs with ML — real obligation extraction, wrong document set (no Div 00 general conditions, no notice/claims clauses). https://construction.autodesk.com/tools/autospecs-construction-submittal-log/ |
| 3 | notice_detection | **0** | No notice object, no notice register, no clause-triggered detection anywhere in Cost Management, Build or Pype. Cost Management marketing page has zero mentions of notices/claims/entitlement. https://construction.autodesk.com/workflows/construction-cost-management/ |
| 4 | deadline_tracking | **2** | RFI types carry "Due date in calendar days"; change orders carry a "Response Due date"; compliance requirements carry expiration dates with calendar integration; Meetings action items carry due dates. All workflow SLAs — none contractual. https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/admin-rfis/RFI_Types.html ; https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/setup-cost/manage-documents-in-cost/Cost_Compliance_Requirements.html |
| 5 | rfi_event_ingestion | **3** | Native RFI module + RFI **v3 API** with GET/POST/PATCH, `POST /search:rfis`, responses with attachments, rfi-types and workflow endpoints. https://aps.autodesk.com/blog/autodesk-build-rfi-v3-api-released ; https://aps.autodesk.com/en/docs/acc/v1/reference/http/rfis-v2-rfis-POST |
| 6 | email_ingestion | **3** | Correspondence tool files external email via a unique Project Email Address on the recipient line, threads replies, supports external-email upload (admin setting "Upload Emails - Private By Default"), attachments and cross-references. https://help.autodesk.com/cloudhelp/ENU/Build-Correspondence/files/getting-started-correspondence/Administration_Correspondence.html ; https://www.arkance.us/blog/autodesk-construction-cloud-new-correspondence-tool-release |
| 7 | daily_report_ingestion | **2** | Field capture via configurable Forms templates (Forms API supports templates + POST/PATCH) plus Photos/Issues; no documented dedicated Daily Log object with structured weather/manpower fields in current Forma Build help. https://github.com/autodesk-platform-services/aps-autodesk.build.api-postman.collection/ ; https://construction.autodesk.com/tools/construction-daily-reports/ |
| 8 | schedule_integration | **3** | Imports P6 / MS Project / Asta; Gantt; version control with version comparison; activities linkable to platform objects; Schedule is an RFI reference type and a Data Connector export. https://help.autodesk.com/cloudhelp/ENU/Build-Schedule/files/About_Schedule.html |
| 9 | change_order_workflow | **3** | Full PCO→RFQ→COR→OCO→SCO chain with hierarchy view, scope classification, source-type taxonomy (ASI/CCD/RFI/ISSUE/RFP/T&M/INT), markup, budget transfers, doc-template generation, and roll-through to payment applications. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/Cost_Change_Orders_Overview.html |
| 10 | claim_identification | **0** | No claim object, no entitlement concept, no claim-detection model. Construction IQ's four risk domains are design/RFI/quality/safety only. https://construction.autodesk.com/tools/construction-iq/ |
| 11 | delay_detection | **1** | Workplan surfaces "root causes for delays" and PPC as production-plan variance; schedule version comparison exists. No delay-event detection, no critical-path/float or as-built analysis. https://help.autodesk.com/cloudhelp/ENU/Build-Schedule/files/About_Schedule.html |
| 12 | responsibility_attribution | **1** | Manual metadata only: PCO Source Type/Source Ref, RFI Ball-in-court, issue assignment, TradeTapp subcontractor risk. No causation or liability inference. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/change-orders/Cost_Potential_Change_Orders.html |
| 13 | contemporaneous_evidence_graph | **3** | References link RFIs↔Issues↔Submittals↔PCO↔Photos↔Schedule↔Forms↔Assets↔Sheets↔Files↔Meetings, and Data Connector explicitly exports "Relationships between data. For example, RFIs that relate to PCOs." https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Data_Connector.html ; https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/work-rfis/Create_RFI.html |
| 14 | evidence_completeness | **1** | Compliance requirements can *block submission until documents are provided*, and Pype Closeout chases missing turnover docs — real completeness engines, but for waivers/COIs/bonds/closeout, not claim evidence. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/setup-cost/manage-documents-in-cost/Cost_Compliance_Requirements.html |
| 15 | recoverable_dollar_estimation | **1** | Budget Impact / Cost Impact / forecast columns compute the value of *user-entered* change amounts across statuses; no entitlement-conditioned recoverable estimate. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/Cost_Change_Orders_Overview.html |
| 16 | claim_package_generation | **1** | Document Templates generate change-order documents; PCO/COR/OCO/SCO reports export to PDF/CSV; Pype Closeout compiles PDF turnover packages (eBinder discontinued 2024-03-26). Nothing produces a narrative + evidence claim submission. https://help.autodesk.com/cloudhelp/ENU/Build-Cost/files/change-orders/Cost_COR_OCO_SCO.html ; https://www.autodesk.com/blogs/construction/important-notice-regarding-pype-ebinder-and-or-pype-smartplans-subscription-faq/ |
| 17 | notice_drafting | **1** | Correspondence gives rich-text drafting, custom types (a firm could create a "NOTICE" type whose initials appear in the item ID), recipients, due dates and references — a manual notice register at best, with zero legal content. https://help.autodesk.com/cloudhelp/ENU/Build-Correspondence/files/work-correspondence/Create_Correspondence.html |
| 18 | schedule_impact_analysis | **1** | RFI carries a `Schedule impact` Yes/No/Unknown flag (now AI-auto-populated) and schedule versions can be compared; no TIA, no windows analysis, no EOT quantification. https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/admin-rfis/RFI_Types.html |
| 19 | procore_integration | **2** | Pype officially "integrates with BIM 360, Procore, Bluebeam, Egnyte, and Box"; Autodesk's partner directory carries multi-platform connectors (AEC WorkBridge, Agave). Core Forma has no first-party Procore sync. https://www.autodesk.com/products/pype/overview ; https://autodesk.com/integrations |
| 20 | autodesk_integration | **3** | It is Autodesk. Native APS/ACC APIs, Data Connector, Data Management, Revit/BIM continuity. https://aps.autodesk.com/apis-and-services/autodesk-construction-cloud-acc-apis |
| 21 | outlook_gmail_integration | **2** | Project Email Address works from any mail client (Autodesk's own example is Outlook) and replies thread back in; no documented first-party Outlook/Gmail add-in, no Graph/Gmail API sync. https://www.arkance.us/blog/autodesk-construction-cloud-new-correspondence-tool-release |
| 22 | mobile_workflow | **3** | Forma mobile app: RFIs, Forms, Photos, Issues, Meetings, Workplan task status/percent-complete updates in the field; PlanGrid Build mobile still live for legacy users. https://help.autodesk.com/cloudhelp/ENU/Build-Schedule/files/About_Schedule.html ; https://construction.autodesk.com/products/plangrid/ |
| 23 | audit_trail | **2** | Item-level activity logs (explicitly cited for AI-generated RFIs), change-order status history, schedule/sheet version control. But exportable **activity data is capped at a 31-day range and limited to the last 12 months**, extraction files expire after 30 days, and there is no legal-hold / tamper-evidence feature. https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Data_Connector.html |
| 24 | portfolio_risk | **3** | Insight + Construction IQ risk cards at hub level, executive-overview access, hub-wide Data Connector extraction, portfolio dashboards. Risk domains are quality/safety/design/RFI — **not commercial**. https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Insight_Construction_IQ.html |
| 25 | performance_pricing_compatibility | **0** | Pure per-user/per-bundle subscription with quote-based enterprise agreements (EBAs). No success-fee, contingency, or value-share construct anywhere in the model. https://construction.autodesk.com/pricing/ |
| 26 | consultant_replacement_potential | **0** | Nothing in the platform substitutes for a quantum/delay consultant. The only "expert-replacing" AI is submittal-log generation and risk triage. https://construction.autodesk.com/workflows/artificial-intelligence-construction/ |

**SCORES line:** `2,1,0,2,3,3,2,3,3,0,1,1,3,1,1,1,1,1,2,3,2,3,2,3,0,0`

---

## 4. PRICING

**Official position: there is no published price.** I fetched https://construction.autodesk.com/pricing/ directly (2026-08-19) and confirmed by HTML inspection that the page contains **no dollar figures**. It presents three bundles, each with a "Get a Quote" CTA:

| Bundle | Contents (per Autodesk pricing page) |
|---|---|
| **Forma for Model Management** | Model Coordination, Design Collaboration, Forma Data Management, Insight, Assemble, Autodesk Tandem for AEC, Navisworks Manage, ReCap Pro |
| **Forma for Preconstruction** | Forma Data Management, ProEst, BuildingConnected Pro, Bid Board Pro, TradeTapp, Forma Takeoff, Forma Estimate |
| **Forma for Construction Operations** | Forma Data Management, **Forma Build**, **Pype AutoSpecs**, **Pype Closeout** |

Autodesk separately confirms Pype AutoSpecs and Closeout are "only available through Forma for Construction Operations" — i.e. no standalone Pype purchase. https://www.autodesk.com/products/pype/overview

**Third-party / aggregator figures (LOW-to-MEDIUM confidence, all secondary):**

| Source | Figure | Date |
|---|---|---|
| SelectHub | Autodesk Build "starting price **$165 per user, monthly**"; cons: "High Cost for Small Businesses", "Estimating Tools Limitations", "Limited Field Reporting" | 2026 https://www.selecthub.com/p/construction-management-software/autodesk-build/ |
| SoftwareConnect | "Forma Build Essentials **$100/month** (single user)"; "Forma Build – Per User **$175/user/month**"; "annual billing **$117/user/month**"; unlimited-user = custom quote | 2026 https://softwareconnect.com/reviews/autodesk-build/ |
| Aggregator summaries (Capterra/vendor guides) | Sheet-quota tiers: 550 sheets **$700/yr**, 5,000 sheets **$1,225/yr**, unlimited **$2,285/yr**; and a separate "unlimited sheets **$1,680/user/yr**" figure | 2026 https://www.capterra.com/p/255145/Autodesk-Build/pricing/ |
| ITQlick | Autodesk Build **$1,625.00/year** | 2026 https://www.itqlick.com/autodesk-build/pricing |
| Aggregators | Autodesk Docs from **$500/yr**; Autodesk Takeoff from **$1,250/yr** | 2026 https://www.capterra.com/p/255145/Autodesk-Build/pricing/ |

**Method & confidence.** Official = quote-only, so every number above is reseller/aggregator-derived and mutually inconsistent (the $165–$190/user/month band vs $117/user/month annualised vs $1,625/yr are not reconcilable without knowing the sheet tier). **Confidence: LOW on exact list price, MEDIUM on the band:** budget roughly **$1,400–$2,300 per user per year for Forma Build at list**, with Docs at the low hundreds and large accounts moving to EBAs. Cost Management appears to be a module of Build rather than a separately-listed SKU on the current pricing page (`UNVERIFIED` — historically ACC sold Cost Management as part of Autodesk Build).

**APS (developer) pricing.** New APS business model effective **2025-12-08**, with an app migration deadline of **2026-02-18** or API suspension. Only four APIs became rated: **Automation, Model Derivative, Flow Graph Engine, Reality Capture**. Verbatim: *"All other APS APIs will not be rated (charged for use) in the December launch."* — i.e. **the ACC/Forma construction APIs a startup would use are currently free**, subject to a qualifying subscription. Data Model API pricing was flagged for **2026-08-17**. https://aps.autodesk.com/blog/aps-business-model-evolution ; https://aps.autodesk.com/pricing-pilot

---

## 5. INTEGRATIONS & API — WHAT A STARTUP CAN ACTUALLY DO

### 5.1 The good: Data Connector is a gift to a solo founder

Data Connector performs scheduled or on-demand **bulk extraction** at project or hub level. Official extracted-data list:

> **Hub-level:** Activated services, Business units, Companies, Projects, Users, Roles
> **Project-level:** Assets, **Cost**, Forms, **Construction IQ**, **Issues**, Locations, Markups, **Meeting minutes**, **Relationships between data. For example, RFIs that relate to PCOs.**, Reviews, **RFIs**, **Schedule**, Sheets, **Submittals**, Takeoff (beta), Transmittals, Photos
> https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Data_Connector.html

This is, effectively, **a pre-built contemporaneous evidence graph in CSV form**, schedulable, with an API (`data-connector` requests) for automation, and a Power Query connector for BI. https://learn.microsoft.com/en-us/power-query/connectors/autodesk-construction-cloud

**Constraints to design around:**
- Access requires **project admin** or **executive overview** permission — not a normal PM.
- Extraction files are downloadable for **30 days** only.
- **Activity data** windows max **31 days** and only within the **last 12 months** — a hard ceiling for multi-year claim reconstruction.
- **Correspondence (email) is not on the list.** Neither is a dedicated Daily Log object.

### 5.2 Transactional APIs
| API | Read | Write | Notes |
|---|---|---|---|
| **RFIs v3** | ✅ | ✅ POST/PATCH incl. responses & attachments | `POST /search:rfis`, rfi-types, workflow. https://aps.autodesk.com/blog/autodesk-build-rfi-v3-api-released |
| **Issues** | ✅ | ✅ | Postman collection published by Autodesk. https://github.com/autodesk-platform-services/aps-acc.issues.api-postman.collection |
| **Forms** | ✅ | ✅ POST/PATCH from templates | **3-legged only** per community SDK. https://github.com/realdanielbyrne/acc_sdk |
| **Photos** | ✅ | ❌ (cannot upload) | 3-legged only. |
| **Submittals** | ✅ (9 endpoints: items, item types, packages, spec sections, attachments, responses) | ❌ at GA | GA **2024-02-22**, "first phase". https://aps.autodesk.com/blog/autodesk-build-submittals-api-general-availability |
| **AutoSpecs** | ✅ (4 endpoints) | ❌ | 3-legged only; subcontractor / source version / PDF link **not exposed**. https://aps.autodesk.com/blog/autospecs-api-autodesk-construction-cloud |
| **Cost Management** | ✅ | ✅ (POST endpoints documented for budgets, contracts, change-orders, sub-cost-items) | e.g. https://aps.autodesk.com/en/docs/acc/v1/reference/http/cost-change-orders-changeOrder-GET and `POST sub-cost-items` in the same reference tree. Predecessor BIM 360 Cost API explicitly supported export **and re-import** of budget data. https://aps.autodesk.com/en/docs/bim360/v1 |
| **Relationships** | ✅ | ✅ (creates links across ACC domains) | The mechanism behind the evidence graph. |
| **Data Connector** | ✅ bulk | n/a | https://aps.autodesk.com/en/docs/acc/v1/overview/field-guide/data-connector |
| **Correspondence** | ❌ **no public API found** | ❌ | Absent from Autodesk's own Build Postman collection repo. |

### 5.3 Marketplace reality
Autodesk's AECO partner directory lists **194 partners across 7 pages** (fetched 2026-08-19: https://autodesk.com/integrations), while construction.autodesk.com markets "over 400 pre-built integrations for ERPs, CRMs, document management, analytics tools, and more" (https://construction.autodesk.com/). Named partners relevant here: **Agave** (data-integration), **AEC WorkBridge** (cross-platform Autodesk/Procore/M365/Bluebeam/BuildingConnected/HCSS), **Aiprentice "Artifact"** (institutional-memory / document automation), **Aurigo** (owner-side risk & cashflow), **Billy** (compliance doc collection). **No claims, entitlement, delay-analysis, or contract-clause partner appears in the categories I reviewed** — this is an unoccupied shelf in Autodesk's own marketplace.

### 5.4 Data egress reality — summary judgment
- **Structured commercial + field records: WIDE OPEN.** Data Connector + REST APIs give a startup budgets, contracts, change orders, RFIs, issues, submittals, schedule, meeting minutes, photos and the relationship edges between them. A V1 could be built on scheduled CSV exports with **zero** Autodesk partnership.
- **Email: CLOSED.** The one dataset the thesis most depends on — contemporaneous correspondence — is the one Autodesk captures but does not expose. A startup must get email from the customer's Outlook/Gmail directly, not from Autodesk.
- **Contract documents: SEMI-OPEN.** PDFs live in Forma Data Management and are retrievable via the Data Management API, but Autodesk provides no parsed contract structure and AutoSpecs will not hand you its document layer.

---

## 6. WEAKNESSES AND EXPLICIT GAPS — DELIBERATE OR UNATTENDED?

| Gap | Deliberate (strategy) or Unattended (opportunity)? | Reasoning |
|---|---|---|
| **No entitlement / notice / claim layer at all** | **Deliberate.** | Autodesk is a design-and-make platform monetised by seats. Entitlement is advice-shaped, jurisdiction-shaped and liability-shaped. Their AI is explicitly disclaimed ("content is generated by AI and requires verification"), and Construction IQ ships with an accuracy disclaimer. They will not put an opinion in the box. |
| **AutoSpecs reads specs, never Division 00 / general conditions** | **Deliberate-by-neglect.** | The extraction engine exists and is proven. Extending it to contract conditions is a corpus + taxonomy problem, not a technology problem. That they haven't in six years — and instead killed SmartPlans/eBinder — signals no product intent. **This is the single largest unattended opportunity in the Autodesk estate.** |
| **No time/EOT dimension on change orders** | **Unattended.** | The object model has scope, source type, markup, budget/cost impact and CCD handling — but no days. Adding an EOT field is trivial; adding EOT *analysis* is not. Customers evidently work around it in custom columns. |
| **No delay analysis; schedule is import-and-view** | **Deliberate.** | Autodesk chose Lean/Workplan (forward-looking production planning) over forensic scheduling. Forensic CPM is a specialist tool market (Deltek Acumen, Oracle) Autodesk has never entered. |
| **Correspondence has no API and no Data Connector export** | Looks **unattended** (young product — public beta May 2023) but functions as **lock-in**. | Either way it is a moat around the richest evidence source. Assume it will get an API eventually; do not build a business that depends on Autodesk shipping one. |
| **Pype SmartPlans & eBinder withdrawn 2024-03-26 with data loss at contract end** | **Deliberate.** | Explicit portfolio pruning toward the two highest-adoption products. Also a reputational data point for any startup pitching "sell to Autodesk and your customers are safe". |
| **AutoSpecs API 4 read-only endpoints, 3-legged only, since Apr 2023** | **Deliberate.** | Autodesk does not want third parties building on Pype's extraction output. |
| **Pricing is quote-only; Pype bundled away** | **Deliberate.** | Suite consolidation and ASP protection. Makes it harder for a startup to price against them, and harder for a customer to buy a point solution from Autodesk. |
| **No claims/entitlement partner in a 194-partner marketplace** | **Unattended.** | Genuine empty shelf. Also weak evidence of demand — an empty shelf can mean no supply *or* no demand (see Unknowns). |
| **Cost Management is the least-reviewed part of the product** | **Structural.** | Public review corpora for Autodesk Build barely mention cost/change orders at all (see §9) — reviewers talk about docs, field, price and complexity. Procore, not Autodesk, is where cost-module complaints concentrate. Autodesk Cost is comparatively young and under-penetrated. |

---

## 7. ADJACENCY TEST — how hard for Autodesk to ship *event detection → entitlement matching → evidence → claim package*?

### **Rating: MEDIUM** (build), **EASY** (buy)

**Data access — trivially easy for them.** They already own the RFI/Issue/Submittal/PCO/Schedule/Meeting/Photo graph *plus the relationship edges*, plus the email in Correspondence, plus the spec extraction engine, plus the contract documents in Data Management. Nobody in the market has a better raw substrate. Data is not the constraint.

**Technical build — medium.** The missing pieces are (a) a Division 00/general-conditions clause taxonomy across FIDIC/NEC/AIA/ConsensusDocs/JCT/AS/bespoke, (b) an entitlement rule engine mapping event→clause→notice window→remedy, (c) quantum logic, (d) a narrative generator. Pype's team could do (a). (b)–(d) require construction-law domain hires Autodesk does not have and has never hired. 12–18 months for a credible v1 *if it were a priority*.

**Organisational incentive — weak, and this is decisive.** AECO grew 22% to $3.58B on collections, EBAs and Forma seats. Claims/entitlement is a low-seat-count, high-touch, services-adjacent motion that does not expand seats. Autodesk's stated AI strategy is *"proprietary data, deep contextual integration, and specialized AI expertise"* to augment existing workflows — not to enter a new commercial-services category.

**GTM motion — mismatched.** Autodesk sells through resellers and EBAs to IT/VDC/preconstruction buyers. A claims product sells to commercial directors, contracts managers and the legal function — a buying centre Autodesk does not currently touch. Payapps was bought partly *because* it already owned a different buying centre (finance/AP).

**Legal-exposure appetite — low.** Every AI surface ships with a verification disclaimer. An entitlement opinion or a notice draft that misses a time bar is a claim against Autodesk. They will ship "here is the evidence and the risk flag"; they will not ship "you are entitled to £1.4M and here is the notice."

**Past M&A and shipping behaviour — the strongest signal of all.** Autodesk's construction pattern is *buy the category, don't build it*:

| Target | Date | Consideration | What it bought |
|---|---|---|---|
| Assemble Systems | Jul 2018 | undisclosed | model conditioning |
| **PlanGrid** | Nov 2018 | **$875M** | field/drawings |
| **BuildingConnected** | Dec 2018 | **$275M** | bid management |
| **Pype** | Jul/Aug 2020 | undisclosed | document AI / submittals |
| ProEst | Dec 2021 | undisclosed | estimating |
| **Payapps (GCPay)** | announced 2024-01-24, closed **2024-02-20** | **$387M cash** | payment applications & statutory compliance |
| PIX | Mar 2024 | undisclosed | (media) |
| **MaintainX** | agreed **2026-05-28** | **~$3.6B cash**, debt-funded | maintenance & asset operations |

Sources: Fortune/Wikipedia refs https://en.wikipedia.org/wiki/Autodesk ; Payapps consideration https://investors.autodesk.com/static-files/34189a8b-9320-44a3-94ae-5e54ea30369a (10-Q, 2024-06-10) ; MaintainX https://www.sec.gov/Archives/edgar/data/769397/000076939726000044/adsk-20260430.htm (10-Q, 2026-05-29).

**The Payapps precedent is the tell.** Autodesk *already had* payment applications inside Cost Management — SOV, billing periods, retention, overbilling, supplier collaboration. It still paid **$387M cash** for a specialist that owned (i) statutory compliance depth (Australian Security of Payment Acts, NZ Construction Contracts Act, UK/IE regimes) and (ii) a different geography and buying centre. Payapps' own marketing is explicitly about statutory deadline risk — *"Get reminders to approve progress claims and issue payment schedules, and reduce the risk of payment disputes"* (https://www.payapps.com/), with a case study titled *"How a Weekend Progress Claim Email Triggered a Multimillion-Dollar SOPA Deadline Risk."*

**Read that again in thesis terms:** Autodesk has already paid nine figures for *a statutory-deadline, notice-and-claim compliance product* — it just happened to be the *payment* claim, not the *delay/variation* claim. The appetite is proven. The category is validated. The remaining question is only which claim type they buy next.

**Conclusion:** MEDIUM to build (capable but disinclined), EASY to buy (proven pattern, $3.6B just committed elsewhere, but $5B+ still authorised for buybacks and ready access to debt).

---

## 8. STARTUP POSTURE: PARTNER / CHANNEL / ROADKILL

### **PARTNER — with a real, dated acquisition path — provided you own the entitlement layer and do not depend on their email.**

**Why PARTNER, not ROADKILL:**
1. **Their marketplace has an empty shelf.** 194 listed partners, zero claims/entitlement/delay-analysis vendors. https://autodesk.com/integrations
2. **The data door is open and free.** ACC/Forma APIs are explicitly *not rated* under the Dec-2025 APS pricing model, and Data Connector hands you the evidence graph — including the relationship edges — as scheduled CSV. A solo founder can ship a V1 on file upload + a Data Connector export with no partnership, no procurement, no Autodesk approval.
3. **They will not build it.** Org incentive, GTM motion and legal-exposure appetite all point away. Their AI roadmap (Assistant: find specs for RFIs, summarise meetings, spot RFQs affecting budget) is retrieval and triage.
4. **They buy proven category leaders at nine figures.** Payapps $387M, PlanGrid $875M, MaintainX $3.6B. A claims/entitlement company with real ARR and a defensible clause corpus is exactly the shape of asset they buy.

**Why NOT pure CHANNEL:** Autodesk's app-store distribution is thin (194 partners, no revenue-share flywheel comparable to a true marketplace), and the bundle-and-quote pricing motion means Autodesk resells its own bundles, not yours. Treat the marketplace listing as credibility, not as a pipeline.

**Where ROADKILL risk is real — three concrete traps:**
1. **If your product is "prettier change-order reporting on ACC data", you are a feature.** PCO→COR→OCO→SCO with hierarchy view, doc templates and budget roll-through already exists and is good. Do not compete there.
2. **If your product is "AI that tags cost impact and schedule impact on an RFI", Autodesk already shipped it** (RFI AI field population, incl. Cost Impact and Schedule Impact, with activity-log audit). https://help.autodesk.com/cloudhelp/ENU/Build-Rfis/files/work-rfis/Create_RFI.html
3. **If your product is "extract submittal-like requirements from specs", Autodesk owns Pype.** Different corpus (Div 00 general conditions) is the defensible move; same corpus is suicide.

**The defensible wedge against Autodesk specifically:**
- **Own Division 00 / general conditions, not Divisions 01–49.** Autodesk has an extraction engine pointed at technical specs and has shown six years of no intent to point it at contract conditions.
- **Own the email.** Autodesk captures it in Correspondence and does not expose it. Ingest from Outlook/Gmail directly — that is a moat *and* an escape from Autodesk dependency, and it makes you Procore-portable at the same time.
- **Own the time dimension.** No EOT field, no TIA, no delay-cause analysis anywhere in Forma.
- **Own the output artefact.** A defensible notice/claim package with entitlement reasoning is precisely what Autodesk's liability appetite forbids.
- **Be multi-platform from day one.** Autodesk and Procore split the market; a claims layer that reads both is worth more to either acquirer than one that reads one.

**Timing note.** Autodesk has just committed ~$3.6B cash+debt to MaintainX (closing "later in fiscal 2027"). That likely suppresses large discretionary construction M&A for 4–8 quarters — which is *good* for a startup that needs runway to reach the revenue threshold at which Autodesk buys.

---

## 9. TOP CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

**Caveat, and it is an important finding in itself:** across Capterra, SoftwareAdvice, SelectHub, SoftwareConnect and GetApp, I could find **almost no verbatim reviewer complaints about Autodesk's change-order or cost-management workflows at all.** Reviewers talk about price, complexity, customisation and reporting. G2, TrustRadius, Reddit and the Autodesk forums returned HTTP 403/429 to automated fetching (`UNVERIFIED` for those corpora). The reasonable inference is that **Autodesk Cost Management is under-penetrated rather than disliked** — GCs run cost in Procore, Sage, Viewpoint or CMiC and use ACC for docs/field/models.

1. > "the cost seams to just keep getting more and more expensive for the platform" — **Caleb C., Estimator, Construction, 2+ yrs**, 2026-04-12. https://www.capterra.com/p/218046/Autodesk-Construction-Cloud/reviews/
2. > "I have to pay as a sub for my own subscription when a GC uses it" — **Adam L., Project Manager, Construction, 1–2 yrs**, 2024-10-02. https://www.capterra.com/p/218046/Autodesk-Construction-Cloud/reviews/
   *(Thesis-relevant: the party with the most to gain from claim recovery — the sub — is the party least willing to pay Autodesk. A sub-side claims tool cannot assume ACC seats.)*
3. > "Limited customization options in reports and forms could be improved" — **Om Prakash P., Civil Engineer, Construction**, 2025-07-04. https://www.capterra.com/p/255145/Autodesk-Build/reviews/
4. > "Limited Field Reporting: The field report features are restricted, which can hinder comprehensive on-site data collection" — SelectHub cons summary, 2026. https://www.selecthub.com/p/construction-management-software/autodesk-build/
   *(Thesis-relevant: weak structured field capture = weak contemporaneous delay evidence.)*
5. > "it would be nice if it worked with other products a little more seamlessly" — **Garrett U., Detailer and Project Assistant**, 2025-05-19. https://www.capterra.com/p/255145/Autodesk-Build/reviews/
6. > "Estimating Tools Limitations: Users have reported that the software's estimating capabilities are subpar" — SelectHub cons, 2026, plus "project scheduling feature… tedious and cumbersome". https://www.selecthub.com/p/construction-management-software/autodesk-build/
   *(Thesis-relevant: weak scheduling UX inside ACC is why P6/Asta remain the source of truth — and why delay evidence lives outside Autodesk.)*

---

## 10. HARDEST FACTS (numeric, sourced)

1. **Autodesk FY2026 revenue $7,206M; AECO product family $3,583M, +22% YoY** (FY25 $2,937M; FY24 $2,580M). — 10-K filed 2026-03-03: https://www.sec.gov/Archives/edgar/data/769397/000076939726000015/adsk-20260131.htm
2. **Autodesk agreed on 2026-05-28 to acquire MaintainX for approximately $3.6 billion in cash**, debt-funded, expected to close later in fiscal 2027. — 10-Q filed 2026-05-29: https://www.sec.gov/Archives/edgar/data/769397/000076939726000044/adsk-20260430.htm
3. **Autodesk paid $387 million in cash for 100% of Payapps Limited, closing 2024-02-20** — the payment-application/statutory-compliance category, bought rather than built despite Autodesk already shipping payment applications in Cost Management. — 10-Q filed 2024-06-10: https://investors.autodesk.com/static-files/34189a8b-9320-44a3-94ae-5e54ea30369a
4. **Payapps + GCPay processed nearly $50 billion in payment applications through 2023; subcontractors wait an average of 83 days after completing work to be paid; 73% of subcontractors front their own money for materials.** — Autodesk Digital Builder, 2024: https://www.autodesk.com/blogs/construction/transforming-construction-payments-autodesks-strategic-move-with-payapps-acquisition/
5. **PlanGrid $875M (Nov 2018) and BuildingConnected $275M (Dec 2018)** — establishing the buy-the-category pattern a decade before Payapps and MaintainX. — https://en.wikipedia.org/wiki/Autodesk (citing Fortune and Autodesk press releases)
6. **Pype SmartPlans and eBinder ceased to be offered for sale on 2024-03-26**, with Autodesk stating customers "will no longer be able to access project data in eBinder or SmartPlans" once the current contract ends. — https://www.autodesk.com/blogs/construction/important-notice-regarding-pype-ebinder-and-or-pype-smartplans-subscription-faq/
7. **The AutoSpecs API shipped (2023-04-14) with exactly 4 read-only endpoints and 3-legged auth only**, with subcontractor, source version and PDF link deliberately withheld. — https://aps.autodesk.com/blog/autospecs-api-autodesk-construction-cloud
8. **Construction IQ was "trusted over 5 million times in the last year"** — and its four risk domains are design, RFI, quality and safety; none is commercial. — https://construction.autodesk.com/workflows/artificial-intelligence-construction/
9. **Data Connector: extraction files downloadable for 30 days; activity-data windows capped at 31 days and limited to the last 12 months.** — https://help.autodesk.com/cloudhelp/ENU/Docs-Insight/files/Data_Connector.html
10. **Autodesk's AECO partner directory lists 194 partners (7 pages)** against a marketing claim of "over 400 pre-built integrations"; **zero** are claims/entitlement/delay-analysis vendors. — https://autodesk.com/integrations ; https://construction.autodesk.com/
11. **Under the APS business model change effective 2025-12-08, only Automation, Model Derivative, Flow Graph Engine and Reality Capture became rated APIs — "All other APS APIs will not be rated"**, i.e. ACC/Forma construction APIs remain free with a qualifying subscription (apps had to migrate to a developer hub by 2026-02-18). — https://aps.autodesk.com/blog/aps-business-model-evolution
12. **ACC → Forma rebrand: announced 2026-02-17, effective 2026-03-24, with "26 construction management tools" folded into Forma and explicitly no API/integration changes.** — https://www.autodesk.com/blogs/construction/autodesk-construction-cloud-is-now-autodesk-forma-heres-what-that-means-for-you/

---

## 11. UNKNOWNS — and what would settle them

| Unknown | What would settle it |
|---|---|
| **Actual list price of Forma Build / Cost Management, and whether Cost Management is separately licensed.** Official pricing is quote-only; aggregator numbers ($117–$190/user/month, $700–$2,285/yr) do not reconcile. | An Autodesk reseller quote (Graitec, Symetri, IMAGINiT, Arkance) or an Autodesk Store checkout screenshot; or a public-sector framework price list (e.g. UK G-Cloud) dated 2026. |
| **Whether Forma Build has a dedicated Daily Logs object** (with structured weather/manpower/labour hours) or only configurable Forms templates. | The `Build-Field` / `Build-Forms` help book on help.autodesk.com, or the Data Connector data-schema document listing table names. |
| **Whether the ACC Cost Management API supports POST/PATCH on change orders end-to-end** (I have indexed evidence of `POST sub-cost-items`, `POST budgets`, `POST contracts`, `POST change-orders` doc pages, but the APS docs site is a JS SPA that returns HTTP 200 for arbitrary paths, so URL existence proves nothing). | Render https://aps.autodesk.com/en/docs/acc/v1/reference/http/cost-change-orders-POST in a real browser, or run the Autodesk `aps-acc-cost-exchange` sample against a trial hub. |
| **Whether a Correspondence API or Data Connector export exists or is on the roadmap.** This determines whether email evidence can ever be read out of ACC. | APS roadmap / release notes on aps.autodesk.com/blog, or an Autodesk Forma release-notes post for Correspondence. |
| **How many ACC/Forma projects and users exist** (Autodesk discloses no construction MAU/project counts). | An Autodesk Investor Day deck or AU keynote slide with construction-specific metrics. |
| **Whether Payapps/GCPay is being extended toward variation/EOT claims** (it already handles contract variations and SOPA deadlines). This is the most likely path by which Autodesk accidentally enters the thesis space. | Payapps/GCPay release notes 2025–2026, or the AU class "The reason Autodesk acquired Payapps and GCPay…" (https://www.autodesk.com/autodesk-university/class/The-reason-Autodesk-acquired-Payapps-and-GCPay-and-its-importance-to-Autodesks-construction-platform-2024). |
| **Verbatim customer pain about ACC change orders** — review corpora on G2, TrustRadius, Reddit and forums.autodesk.com were unreachable (403/429). Absence of complaint here is not evidence of satisfaction. | Manual browser access to G2 "What do you dislike about Autodesk Build?" and the Autodesk Cost Management ideas board. |
| **Whether Autodesk has ever internally scoped a claims/entitlement product.** | AU 2025/2026 session catalogue search for "claims", "entitlement", "dispute", "delay analysis"; or Autodesk job postings for construction-law/contracts domain experts. |
