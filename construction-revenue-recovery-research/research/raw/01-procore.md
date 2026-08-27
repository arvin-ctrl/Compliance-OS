# 01 — PROCORE TECHNOLOGIES (NYSE: PCOR)

**Researched:** 19 August 2026. All figures from primary sources unless labelled `UNVERIFIED`.
**Headline verdict up front:** Between May and July 2026 Procore shipped the exact middle of this thesis's
pipeline as native, generally-available product. A startup can still sit above Procore — but not on the
axis most people would pick, and not under Procore's current developer policy without express written consent.

---

## 1. SNAPSHOT

| Item | Value | Source |
|---|---|---|
| What it is | Cloud construction management platform: project execution, cost management, resource management, project lifecycle management, plus an agentic-AI layer | [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm) |
| Ownership | Public, NYSE: PCOR. IPO 2021. | 10-K |
| CEO | Ajei Gopal (appointed 2025, succeeded founder Tooey Courtemanche) | [press](https://www.procore.com/press/procore-announces-appointment-of-ajei-gopal-as-chief-executive-officer) |
| FY2025 revenue | **$1,322.5M** (+15% YoY; 2024 $1,151.7M; 2023 $950.0M) | 10-K, Consolidated Statements of Operations |
| Q2 2026 revenue | **$375M**, +16% YoY | [Q2'26 PR, 29 Jul 2026](https://www.procore.com/press/procore-announces-second-quarter-2026-financial-results) |
| FY2026 guidance | $1,510–1,514M (+14.5% at high end) | Q2'26 PR |
| Total customers | **17,850** (31 Dec 2025), +4% YoY (17,088 in 2024, 16,367 in 2023) | 10-K |
| Customers >$100k ARR | **2,710** (Dec 2025) → **2,871** (30 Jun 2026, +14% YoY). 66% of total ARR | 10-K; Q2'26 PR |
| Customers >$1M ARR | **115** (Dec 2025), +34% YoY; 20% of total ARR | 10-K |
| Implied ARPU | **~$74k/customer/yr** ($1.3225B ÷ 17,850) — but the distribution is brutally skewed | derived from 10-K |
| GRR / NRR | **GRR 95%** (2025, 2023) / **NRR 106%** (2025 and 2024). Procore explicitly says "we do not believe NRR is a key metric due to the impact of pooled volume contracts" | 10-K |
| R&D expense | **$362.4M** FY2025 (vs $313.0M 2024, $300.6M 2023) — 27% of revenue. Q2'26 alone $93.3M | 10-K; Q2'26 8-K |
| S&M expense | $580.7M FY2025 (44% of revenue) | 10-K |
| Headcount | 4,421 FTE (31 Dec 2025); 3,075 US | 10-K |
| Geography | US 85% of revenue, RoW 15% (FY2025). 150+ countries claimed, 3M+ projects | 10-K; press boilerplate |
| ICP | Owners, general contractors, specialty contractors; residential and non-residential. "From small businesses managing a few million dollars of annual construction volume to global enterprises managing billions" | 10-K |
| Profitability | GAAP operating margin **1%** in Q2'26 (first GAAP operating profit); non-GAAP 21%. FY2027 guide: 25% non-GAAP OM | Q2'26 PR |

**Recent M&A / strategic posture (this is the story):**
- **20 Jan 2026 — acquired Datagrid** (legal entity Toric Labs, Inc. d/b/a Datagrid), a San Francisco agentic-AI/data-connectivity company. Founder/CEO Thiago da Costa became SVP of AI & Data at Procore. Terms undisclosed. ([press](https://www.procore.com/press/procore-acquires-datagrid); confirmed in [10-K](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm))
- **29 Jul 2026 — agreed to acquire DroneDeploy for ~$845M cash.** ([press](https://www.procore.com/press/procore-to-acquire-dronedeploy-creating-next-generation-platform-that-sees-understands-and-acts-on-the-jobsite))
- **Feb 2026 — repackaged the whole product line** into four bundles (Project Execution, Cost Management, Resource Management, Project Lifecycle Management) × three tiers (Essentials, Base, Enterprise), with product renames. (10-K)
- Procore is explicitly repositioning "from the system of collaboration and record to the **system of intelligence** for construction." (DroneDeploy press release)

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 Project Financials / change management — strong, and the category benchmark

| Module | What it does | Evidence |
|---|---|---|
| **Change Events** | The commercial-event container. Fields: Origin (link to source item), Change Event #, Title, Status, **Scope (In Scope / Out of Scope / TBD)**, **Type (TBD / Allowance / Contingency / Owner Change / Transfer)**, **Change Reason** (customisable), Description, Attachments, Prime Contract (for markup). Line items carry Budget Code, Vendor, Contract, Qty, UOM, Unit Cost, **Cost ROM** and **Revenue ROM**. | [Change Events tool](https://support.procore.com/products/online/user-guide/project-level/change-events); [Create a Change Event](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-a-change-event) |
| **Change Event origination** | Manually, **from an RFI**, and **from an Email** in the Emails tool. Not auto-detected historically. | [Emails tool](https://support.procore.com/products/online/user-guide/project-level/emails); [RFIs tool](https://support.procore.com/products/online/user-guide/project-level/rfis) |
| **RFQ → PCO → PCCO / CCO** | 1-tier, 2-tier, 3-tier change-order configurations. Prime contract must be Approved before change orders can be raised. Change event line items populate the change order SOV. | [Create a PCCO from a Change Event](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-a-prime-contract-change-order-from-a-change-event); [Change Orders](https://support.procore.com/products/online/user-guide/project-level/change-orders) |
| **Prime Contracts** | Contract header record: SOV, issued-on date, LOI date, substantial completion date, contract termination date, change-order rollup, budget sync. | [Prime Contracts](https://support.procore.com/products/online/user-guide/project-level/prime-contracts); [product page](https://www.procore.com/financial-management/prime-contracts) |
| **Commitments** | Subcontracts & POs, commitment change orders. | [Project Financials](https://www.procore.com/project-financials) |
| **Budget / Direct Costs / Forecasting** | Time-phased cost forecasts, WBS, labour/production feeding budget. | [Project Financials](https://www.procore.com/project-financials) |
| **Invoice Management** | Owner invoicing + subcontractor invoicing, approval workflows with conditional-logic thresholds. | [Invoice Management](https://www.procore.com/invoice-management) |
| **Procore Pay** | GC→sub disbursements, pay requirements checklist, **automated lien-waiver exchange** (unconditional waivers released only on payment), Workflows-driven disbursement approval with audit trail. | [Pay](https://www.procore.com/pay) |

Marketing language worth noting — the Project Financials page literally sells **"Reduce unrecoverable change orders with quicker approvals"** and **"eliminating the need to proceed at risk."** ([procore.com/project-financials](https://www.procore.com/project-financials)) Procore already owns the *vocabulary* of unrecovered change value; it just solves it with speed, not entitlement.

**Critical negative finding:** a Procore Change Event has **no field for contract clause reference, notice date, notice deadline, or entitlement basis.** ([Create a Change Event](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-a-change-event)) Change Reason is a free customisable dropdown — it is a cost-coding taxonomy, not a contractual-entitlement taxonomy.

### 2.2 The Correspondence tool — the single most under-appreciated asset here

Procore ships **24 out-of-the-box correspondence type templates**, built on the "custom tool" framework so each type is effectively its own tool with its own fieldset, statuses, assignees, distribution list and permissions. The list includes, verbatim from Procore's own descriptions:

- **Early Warning Notice (EWN)** — "alert others of anything that may delay the work, or increase costs"
- **Notice of Delay (NOD)** — "to make a claim to extend the completion date or to recover costs"
- **Extension of Time (EOT)** — "communication identifying events causing delays"
- **Notification of Backcharge (NOB)**, **Change Request (CR)**, **Constraints (CON)**, **Risk Identification (RI)**, **Mitigation Plan (MP)**, **Site Instruction (SI)**, **Client Instruction (CI)**, **Variation Request**, **Bulletin**, **Addendum**, **Transmittal**, **Notice to Proceed**, **Letters**, **Letters of Intent**, **Lessons Learned**, **Material Request**, **Permit Request**, **Project Request**, **General Correspondence**

Source: [Add a Template Correspondence Type](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-template-correspondence-type); type list also at [FAQ](https://en-gb.support.procore.com/faq/what-types-of-correspondences-can-be-created-with-the-correspondence-tool). Support notes these templates are "often built into the project contract" ([FAQ: what is the Correspondence tool](https://support.procore.com/faq/what-is-the-correspondence-tool)).

So: **Procore already ships the notice containers.** What it does not ship is anything that decides *whether* a notice is due, *by when*, or *under which clause*. Correspondence items support workflows (status auto-populates, "Current Step Due Date", assignees from workflow steps) and there is **one optional global setting for automatic email reminders when items are overdue** — but the due date comes from a workflow template a human configured, not from a contract. ([Correspondence](https://support.procore.com/products/online/user-guide/project-level/correspondence))

Package limits matter for a startup: GC/SC Essentials-Enhance-Premier starter packs are capped at **10 correspondence types created from a Procore template**; other packages at **30 types (custom or template)**. ([FAQ](https://en-gb.support.procore.com/faq/what-types-of-correspondences-can-be-created-with-the-correspondence-tool))

### 2.3 Evidence-bearing field tools
RFIs (due dates, assignees, distribution, related items, custom fieldsets, "answer RFIs by email", "create a change event from an RFI"), Submittals, Daily Log, Meetings, Photos, Documents, Drawings, Punch List, Observations, Coordination Issues, Inspections, Incidents, Timecards. All are first-class, all are API-addressable, all are mobile. ([RFIs](https://support.procore.com/products/online/user-guide/project-level/rfis))

**Emails tool** is more useful than people realise: each project has an **inbound email address**; "anyone who knows the exact inbound email address for the project can send an email," Procore-user or not. Emails are searchable with advanced search operators, and you can **create a change event directly from an email**. ([Emails](https://support.procore.com/products/online/user-guide/project-level/emails)) Plus free first-party [Procore for Gmail](https://marketplace.procore.com/apps/procore-for-gmail) (1,867 installs) and Procore for Outlook add-ins.

### 2.4 Schedule — the weakest link
Procore's Schedule tool imports **Primavera P6, MS Project, Asta, Phoenix and MPX** files via Procore Drive or connector apps, and displays Gantt/lookahead views. It is not a CPM engine. Documented constraints:
- **only a single schedule can be linked to a Procore project**; new versions overwrite the prior one
- **only one Baseline Start and Baseline Finish** is supported (P6 multi-baseline does not carry over)
- unmapped fields are silently dropped
- the current Schedule support page is flagged as the "legacy schedule experience"

Sources: [Schedule overview](https://support.procore.com/products/online/user-guide/project-level/schedule/overview); [Integrate a Primavera P6 Schedule using Procore Drive](https://support.procore.com/products/procore-drive/schedule/tutorials/integrate-a-primavera-p6-schedule-using-procore-drive); [Primavera schedule detailed data mapping](https://support.procore.com/integrations/oracle-primavera/primavera-schedule-detailed-data-mapping)

There is **no critical path calculation, no baseline-vs-as-built windows analysis, no time-impact analysis, no what-if** in Procore. Delay analysis is outsourced to marketplace partners (SmartPM, Planera) or done outside the platform entirely.

### 2.5 Procore AI — and this is where the thesis gets tested

Timeline, all primary-sourced:

| Date | Event |
|---|---|
| 20 Nov 2024 | [Procore AI announced](https://www.procore.com/press/procore-launches-procore-ai-with-new-agents-to-boost-construction-management-efficiency): Copilot (GA), Insights (early 2025), Agents, Agent Studio (2025). No contract/change-order/claims content. |
| 15 Oct 2025 | [Groundbreak 2025](https://www.procore.com/press/procore-advances-the-future-of-construction-with-new-ai-innovations): Procore Assist enhancements (Photo Intelligence, Spanish/Polish, mobile), **Agent Builder open beta**. Still no contract/claims content. |
| 20 Jan 2026 | **Datagrid acquired.** |
| 21 May 2026 | [Datagrid embedded into Procore](https://www.procore.com/press/new-procore-ai-experience-embeds-datagrid-into-procore). First five native agents ship: Deep Search, Submittal Review, RFI, Daily Log, **Contract Review**. Introduces **Actions** (agents execute live steps inside Procore) and **Triggers** (agents fire automatically on events in Procore — "such as new submittals, RFIs, or change order"). |
| 23 Jul 2026 | [Digital Coworker packages + 20-agent library](https://www.procore.com/press/procore-introduces-digital-coworker-packages-expands-ai-agent-library-and-previews-skills-to-help-construction-teams-put-ai-to-work) — **all three packages generally available**. New agents include **Schedule Analyst Agent** and **Change Analysis Agent**. Previews **Skills** (teach agents your SOPs, rolling out August 2026) and ships **Control Tower** (credit/usage governance). |

**The 20 agents currently listed** ([procore.com/ai/agents](https://www.procore.com/ai/agents)), verbatim descriptions for the thesis-relevant ones:

- **Change Analysis Agent** — *"Review changes, RFIs, drawings, and records to identify scope shifts, cost exposure, and schedule risk."* Press release version is stronger: *"Reviews changes, RFIs, drawings, specifications, and project records to identify scope impacts, cost exposure, schedule risk, and **required follow-up actions**."*
- **Contract Review Agent** — *"Reconcile contracts and drawings against internal benchmarks to flag potential conflicts directly within the document."* Detail page: *"checks contracts and drawings against compliance standards, helping flag risks, missing terms, and SOP deviations with clear explanations linked back to the source"*; *"Upload your SOPs and standards to build custom review skills the agent checks against"*; *"Get clear redlines on risky clauses, gaps, and conflicts"*; *"Review color-coded risk levels."* ([/ai/agents/contract-review](https://www.procore.com/ai/agents/contract-review))
- **Schedule Analyst Agent** — *"Review milestones, logic, and activity relationships to flag sequencing issues and delays."*
- **Financial Analyst Agent** — *"Analyze commitments, change events, and cost trends to flag exposure and overruns early."*
- **Lessons Learned Agent** — *"Mine RFIs, changes, and logs for trends."*
- **Deep Search Agent**, **Fast Search Agent**, **Daily Log Agent**, **RFI Agent**, **Submittal Review Agent**, **Drawing Analysis Agent**, **Drawings and Specs Specialist Agent**, **Scope Writer Agent**, **Meeting Minutes Publisher Agent**, **Photo Analyzer Agent**, **Field Observations Agent**, **Site Safety Agent**, **Procurement Log Creator Agent**, **Bid Analyzer Agent**, **Bid Leveling Agent**.

Platform claims from [procore.com/ai](https://www.procore.com/ai): a proprietary reasoning model called **"Magpie"**, "specifically trained on industry data to map and interpret complex relationships across messy, real-world jobsite data rather than simply summarizing text"; **"Over 150 built-in actions"** that let agents create/update RFIs, **Change Events**, Daily Logs and Action Plans; multimodal embeddings over "drawings, blueprints, PDFs, audio, video"; numbered citations to source files; permission-aware; "your data is never used to train third-party frontier models."

**What is still absent from Procore AI, verified by reading the agent library and every AI page:** no agent for notice generation, no agent that reads a contract's notice provisions and starts a clock, no entitlement matching, no evidence-completeness scoring, no claim/quantum package, no cost-recovery estimation. The Contract Review Agent is a **pre-award / document-conflict risk reviewer against your own SOPs** — not an **in-flight obligations engine**.

### 2.6 AI pricing — a genuine business-model change
Three **Digital Coworker** packages, all GA as of 23 Jul 2026 ([procore.com/ai/plans](https://www.procore.com/ai/plans)):

| Package | Term | Pricing | Contents |
|---|---|---|---|
| Starter Pack | 6-month | **Flat-rate; includes up to 3 projects** | 5 agents (Deep Search, Submittal Review, RFI, Daily Log, Contract Review), **250 actions**, generative search, voice agent, agentic memory, 15-min data sync, credit & activity dashboard. LLMs: Anthropic, Google |
| Pro | 12-month | **Credit usage-based** | 20 agents, 1,000+ actions, video analysis, scheduled automations. LLMs: Anthropic, Google, OpenAI |
| Enterprise | 12-month | **Credit usage-based** | 25+ agents, Agent Studio, deployment specialist, BI connection, phone/SMS |

Procore's own definition: *"Credits are consumed at data ingest, and when agents are performing value-add tasks."* No published dollar figures. **This is the first time Procore has sold consumption, not just ACV-based subscription** — and it means Procore now has a direct revenue reason to keep third-party AI off its data.

---

## 3. CAPABILITY MATRIX (0–3)

| # | Dimension | Score | Justification + source |
|---|---|---|---|
| 1 | contract_ingestion | **3** | Contract Review Agent ingests contracts, drawings and specs into Datagrid's multimodal index; Documents/Prime Contracts store the executed contract. Marketed and GA since May 2026. [/ai/agents/contract-review](https://www.procore.com/ai/agents/contract-review) |
| 2 | clause_extraction | **3** | "Get clear redlines on risky clauses, gaps, and conflicts—each linked back to the source"; "flag risks, missing terms, and SOP deviations". Caveat: pre-award risk review, not a structured obligations/notice register. [/ai/agents/contract-review](https://www.procore.com/ai/agents/contract-review) |
| 3 | notice_detection | **1** | Notice *containers* exist (EWN, NOD, EOT correspondence templates) but nothing detects that a notice obligation has been triggered by an event. No clause→trigger link anywhere in docs. [correspondence templates](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-template-correspondence-type) |
| 4 | deadline_tracking | **2** | Generic due dates on RFIs/submittals/correspondence; workflow "Current Step Due Date"; optional global setting for automatic overdue email reminders. No contract-derived deadlines. [Correspondence](https://support.procore.com/products/online/user-guide/project-level/correspondence) |
| 5 | rfi_event_ingestion | **3** | Native RFI tool, REST API, webhooks, RFI Agent, "create a change event from an RFI". [RFIs](https://support.procore.com/products/online/user-guide/project-level/rfis) |
| 6 | email_ingestion | **3** | Per-project inbound email address open to non-users; Gmail/Outlook add-ins; "create a change event from an email"; Daily Log Agent consumes emails. [Emails](https://support.procore.com/products/online/user-guide/project-level/emails) |
| 7 | daily_report_ingestion | **3** | Daily Log tool + Daily Log Agent turning "field photos, emails, video, and voice into completed daily logs". [/ai/agents](https://www.procore.com/ai/agents) |
| 8 | schedule_integration | **2** | Imports P6/MSP/Asta/Phoenix, but one schedule per project, one baseline, unmapped fields dropped, no CPM engine. [Schedule overview](https://support.procore.com/products/online/user-guide/project-level/schedule/overview) |
| 9 | change_order_workflow | **3** | Change Event → RFQ → PCO → PCCO/CCO with 1/2/3-tier configs, budget + ERP sync. Category benchmark. [Change Orders](https://support.procore.com/products/online/user-guide/project-level/change-orders) |
| 10 | claim_identification | **2** | Change Analysis Agent identifies "scope impacts, cost exposure, schedule risk, and required follow-up actions" — but framed as change management; no claim register, no entitlement test. [23 Jul 2026 PR](https://www.procore.com/press/procore-introduces-digital-coworker-packages-expands-ai-agent-library-and-previews-skills-to-help-construction-teams-put-ai-to-work) |
| 11 | delay_detection | **2** | Schedule Analyst Agent flags "sequencing issues, delays, dependencies, and potential schedule risks"; no forensic/windows method, no CPM. [/ai/agents](https://www.procore.com/ai/agents) |
| 12 | responsibility_attribution | **1** | Ball-in-court, assignees, customisable Change Reason codes and full change history exist; no causation or liability attribution anywhere. [Change Events](https://support.procore.com/products/online/user-guide/project-level/change-events) |
| 13 | contemporaneous_evidence_graph | **2** | Best raw dataset in the industry + manual "Related Items" linking + Magpie claiming to "map the complex relationships across your project records". Not a purpose-built evidence graph. [/ai](https://www.procore.com/ai) |
| 14 | evidence_completeness | **1** | Insights benchmarks submittal/RFI cycle times as "project risk"; Change Analysis Agent names "required follow-up actions". Nothing scores whether a record set would survive a claim. [10-K platform capabilities] |
| 15 | recoverable_dollar_estimation | **2** | Change Events carry **Cost ROM** and **Revenue ROM** columns and roll into budget/forecast; this is cost-of-change, not entitlement-weighted recoverable value. [Change Events](https://support.procore.com/products/online/user-guide/project-level/change-events) |
| 16 | claim_package_generation | **1** | Can export change orders and reports to PDF/CSV; no claim/dispute submission assembly. Reviewers complain reports are format-restricted. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/) |
| 17 | notice_drafting | **2** | 24 correspondence templates including EWN/NOD/EOT with fieldsets, distribution, response tracking and overdue reminders — human-authored, no AI drafting, no clause linkage. [templates](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-template-correspondence-type) |
| 18 | schedule_impact_analysis | **2** | Schedule Analyst Agent is marketed for delay/sequencing analysis; no TIA, no as-planned-vs-as-built, no fragnet. [/ai/agents](https://www.procore.com/ai/agents) |
| 19 | procore_integration | **3** | It is Procore. Plus 446 marketplace apps and a documented REST/webhook platform. |
| 20 | autodesk_integration | **1** | Direct competitor. Only third-party bridges exist on the marketplace (BIMLauncher Connector for Autodesk Construction Cloud/BIM 360; ProjectReady WorkBridge). [marketplace](https://marketplace.procore.com/apps) |
| 21 | outlook_gmail_integration | **3** | First-party Procore for Outlook and Procore for Gmail add-ins (free), plus Mail Manager (302 installs) and TonicDM (1,935 installs). [marketplace](https://marketplace.procore.com/apps) |
| 22 | mobile_workflow | **3** | iOS/Android across RFIs, daily logs, photos, change events; "bring change management to the field". [Project Financials](https://www.procore.com/project-financials) |
| 23 | audit_trail | **3** | Item change history, permission model, Procore Pay disbursement audit trail ("shows who reviewed and approved each disbursement"). [Pay](https://www.procore.com/pay) |
| 24 | portfolio_risk | **3** | Insights ("identifying trends and predicting potential project risks"), Portfolio Financials, and the 2026 Portfolio Management & Capital Planning suite. [10-K; press](https://www.procore.com/press) |
| 25 | performance_pricing_compatibility | **1** | Fixed annual fee by Annual Construction Volume; "We do not provide refunds for unused construction volume"; "We generally do not charge customers based on consumption or on a per-project basis." AI credits are the sole crack in this. [10-K](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm) |
| 26 | consultant_replacement_potential | **1** | No quantum, no entitlement, no expert-report output. Procore replaces admin hours, not claims consultants. |

`SCORES| 3,3,1,2,3,3,3,2,3,2,2,1,2,1,2,1,2,2,3,1,3,3,3,3,1,1`

---

## 4. PRICING

**Published by Procore (high confidence):**
- *"We charge an upfront annual fee by product and based upon your **Annual Construction Volume (ACV)** — the aggregate dollar value of the construction work across your projects."* — [procore.com/pricing](https://www.procore.com/pricing)
- *"Unlimited users, unrivaled support, unlimited data storage, and product enhancements, at no additional cost."* No per-seat fee. — same page
- 10-K detail: three contract shapes — (a) annual subscription with volume over one year; (b) multi-year with volume measured over successive one-year periods; (c) **pooled volume contracts** with fixed flat annual fees over 2–3 years. *"We do not provide refunds for unused construction volume. We generally do not charge customers based on consumption or on a per-project basis."*
- Feb 2026: four bundles × Essentials/Base/Enterprise tiers replace pure à-la-carte. AI capability moved into bundles/tiers "in lieu of, or in addition to, on an à la carte basis." (10-K)
- **AI is now separately priced**: Starter = flat rate, up to 3 projects, 6-month term, 250 actions; Pro and Enterprise = **credit usage-based**, credits consumed "at data ingest, and when agents are performing value-add tasks." ([procore.com/ai/plans](https://www.procore.com/ai/plans))

**Third-party estimates (LOW–MEDIUM confidence — all from vendors selling alternatives; Procore publishes no numbers):**
- $15,000–30,000/yr for small GCs at $10–50M ACV; $30,000–80,000/yr at $50–200M ACV; implementation $50,000–150,000+ in year one — [scanmanifold.com, 2026](https://www.scanmanifold.com/blog-posts/procore-pricing-2026-contractors) (competitor content, methodology undisclosed)
- Rule of thumb quoted around 0.1–0.3% of ACV — [projul.com](https://projul.com/blog/procore-pricing-analysis-2026/) `UNVERIFIED`
- Sanity check from the filings: FY2025 revenue $1.3225B ÷ 17,850 customers = **~$74k average**, but 2,710 customers >$100k ARR account for 66% of ARR and 115 customers >$1M ARR account for 20%. So the median customer is materially below $74k and the enterprise tail is where the money is.

**Implication for a startup selling alongside:** Procore's contract is a large, annual, pre-committed, volume-based number with unlimited seats. A revenue-recovery product cannot be priced per-seat credibly in this ecosystem, and cannot be sold as "cheaper than Procore." It has to be priced against **recovered dollars** or against **a project/claim**, i.e. against a budget Procore does not currently touch (the claims-consultant / commercial-manager budget). The good news: because Procore charges no per-seat fee, the buyer has no seat-count objection to adding a second tool. The bad news: Procore now sells **AI credits**, which means every AI dollar a contractor spends is a dollar Procore is actively competing for.

---

## 5. INTEGRATIONS & API — WHAT IS OPEN, WHAT IS CLOSED

### 5.1 What is technically open
- REST API v1 and v2 covering RFIs, submittals, change events, change orders, budget, budget changes, subcontractor invoices, daily logs, incidents, observations, timecards, documents, drawings, direct uploads, **Correspondence** (via the Generic Tools API — correspondence types are `generic_tools`, items are `generic_tool_items`), configurable fieldsets, WBS, users/permissions, and Workflows. ([REST API Overview](https://procore.github.io/documentation/rest-api-overview); [Correspondence API guide](https://procore.github.io/documentation/tutorial-correspondence))
- OAuth 2.0 (auth-code grant and client-credentials / service accounts), webhooks, Developer Managed Service Accounts, sandboxes.
- **Rate limits**: two limits — an **hourly** limit (60-min window) and a **spike** limit (10-second window). Documented header examples: `X-Rate-Limit-Limit: 600` hourly and `X-Rate-Limit-Limit: 25` for the spike window. Procore explicitly warns *"Don't assume a single fixed window (for example, only 3600/hour)"*. **Failed calls count**: "A `400`, `403`, or `404` response consumes quota exactly like a successful call." v2 collections default to 10 per page, max 100. ([Rate Limiting](https://procore.github.io/documentation/rate-limiting); [Pagination](https://procore.github.io/documentation/rest-api-overview))
- Rate-limit increases are per-app, reviewed by an "API Review Board" against 30 days of production traffic; declined for apps with no production traffic, no backoff after 429, high 4xx rates, or "bulk extraction better served by Procore Analytics." Only the hourly limit is requestable; the spike limit is set by Procore. ([Request a Rate Limit Increase](https://procore.github.io/documentation/rate-limit-increase))

### 5.2 What is closed — and this is the decisive section
The **Procore Developer Policy** (effective 30 September 2025) prohibits, verbatim:

> *"Use API Data to train, re-train, fine-tune, or benchmark any machine learning or artificial intelligence algorithm, model, software, or system."*

> *"Scrape, **parse**, harvest, **build databases**, bulk export, or otherwise create copies of any API Data accessed or obtained using the APIs by your Application or otherwise **without Procore's express consent**."*

> *"Use API Data collected from one organization to directly benefit a different organization or any third party."*

> *"Use the Procore APIs to create, develop, or build a competitive product or offering, or a product or offering that **substantially replicates any features or functionality of the Procore Services** … except as expressly authorized by Procore in writing."*

Source: [Procore Developer Policy](https://procore.github.io/documentation/marketplace-policy)

The **API Usage Guidelines** reinforce it: REST APIs are *"not intended for … Large-scale data extraction or bulk export for purposes outside of your app's core integration … Building datasets for training, fine-tuning, or benchmarking AI/ML models (including LLMs) … High-volume data retrieval to power non-complementary analytics or intelligence solutions."* And: *"If your use case involves AI agents, semantic retrieval, or large-scale analytics, see **Agentic APIs** for the intended path."* ([API Usage Guidelines](https://procore.github.io/documentation/api-usage-guidelines))

Read plainly: **a revenue-recovery layer that pulls RFIs, emails, daily logs and correspondence out of Procore, parses them, builds an evidence database and runs LLM reasoning over it is squarely inside the prohibited zone unless Procore consents in writing.** Cross-portfolio benchmarking (the thing that would make entitlement matching smart) is separately prohibited by the one-org-to-another-org clause.

### 5.3 The Agentic API — the new front door, and it is a gate
Procore now runs a **Design Partner pilot** for **Agentic APIs**, built on Datagrid, centred on a **Converse API** ("natural-language prompt → agent response, with optional citations to source records and a conversation ID"). Explicit positioning: *"If your app currently uses REST APIs for AI-powered features or large-scale data workloads, those use cases are intended for Agentic APIs."*

Access mechanics: rolling review by Procore's Ecosystem team; selection based on *"whether the use case fits the API's capabilities and whether customers are asking for it"*; 30-minute discovery call with a Procore PM and a Datagrid engineer; signed pilot agreement; access **"scoped to their use case"**. GA "in development, and we're not committing to a date."

Roadmap on the same page: declaring MCP servers and agents in your app manifest, and an **"Agent Marketplace — a managed marketplace for publishing AI agents to Procore's customer base, where partners list certified agents alongside traditional apps."**

Source: [Agentic APIs](https://procore.github.io/documentation/agentic-apis)

### 5.4 Partner program mechanics (relevant to a solo founder)
Two verification paths ([Verification & Production Access](https://procore.github.io/documentation/verification-and-production-access)):
- **Private Developer** — for a single Procore account, "not sold as a product." Fast approval. Explicitly **not** the right path if "You're building a product or SaaS that connects to Procore, even if only one customer uses it today" or "You're piloting with a single customer before listing publicly — that's still a Marketplace product."
- **Marketplace Partner** — required for anything commercial. Five steps: Partner Application (with a "Better Together" story assessed for "complementarity, strategic alignment, and ecosystem eligibility") → Technical Feasibility Assessment → Build/Test/**Certification Assessment** (security, API efficiency, reliability; integration diagram + demo video) → sign **Procore Framework Agreement + Technology Partner Addendum** → Marketplace listing review. ([Technology Partner Overview](https://procore.github.io/documentation/procore-partner-overview); [Marketplace Approval Checklist](https://procore.github.io/documentation/marketplace-checklist))
- **Business email required — personal email domains (Gmail, Yahoo, Outlook.com) are rejected.**
- Ongoing requirement: "your app must have at least one (1) active customer using it within any rolling 12-month period" or it can be unlisted. ([Marketplace Requirements](https://procore.github.io/documentation/marketplace-requirements))
- **Fees exist but are not published.** Procore says: *"The Program Guide outlines what to expect regarding **partner tiers, benefits, and associated fees**."* The Program Guide is not publicly linked from the docs site. Publicly-summarised tier gates: entry tier needs 1+ test customer and 1+ monthly active customer with app validation and <48h partner SLA; next tier needs **100+ monthly active customers**, bi-directional data, a customer case study, <36h SLA; top tier is **invitation only**. `UNVERIFIED` on exact tier names and dollar fees — settled only by the Partner Program Guide PDF or a Procore partner rep.

**Startup-relevant conclusion on egress:** the practical, sanctioned bulk-data path is **Procore Analytics** (Databricks-backed, hourly refresh, Power BI / Databricks / SQL Server / ADLS / S3 / Microsoft Fabric / Delta Sharing) — but it is **licensed at the company level to the customer, not to you**. Procore's own guidance to developers: *"Procore Analytics is licensed at the company level. If you are building an integration for your own company, check with your Procore administrator… If you are building on behalf of a customer, raise it with that company."* ([Rate Limit Increase](https://procore.github.io/documentation/rate-limit-increase); [Procore Analytics](https://support.procore.com/products/online/user-guide/company-level/analytics))
That is actually a **usable wedge**: the *customer* owns the Analytics licence and can point it at your warehouse. The customer's data rights, not your API rights, are the lever.

### 5.5 The App Marketplace — hard numbers I pulled directly
Scraped from Procore's own marketplace search payload (`marketplace.procore.com/search_data`, 19 Aug 2026): **446 published apps**, **115,558 cumulative installs** across all of them.

Thesis-relevant apps, with install counts:

| App | Installs | What it is |
|---|---|---|
| **Document Crunch** | **187** | AI contract intelligence. Listing: *"from generating timely notices to delivering daily contract insights straight to the field… PROTECT FROM PROFIT LOSS: No more late notice and missing dates… AVOID FUTURE LITIGATION… Receive notifications when key events occur within the project lifecycle."* Side-panel embedded app. |
| **Clearstory** (formerly Extracker) | **173** | Change Order Requests + T&M tags pushed into Procore Change Events. |
| **SmartPM** | **137** | Schedule analytics / delay analysis on MPP/P6 files stored in Procore. Schedule Compression Index, Schedule Quality Grade, Project Health Index. |
| **Datagrid** | **294** | Now Procore-owned; still listed as a marketplace app. |
| **Levelset (Lien Waivers & Notices)** | 468 | **Statutory** lien notices/waivers — not contractual notices. |
| **Payapps** | 67 | Progress claims & variations (ANZ/UK terminology). |
| **Smoothx Advanced Payments** | 5 | *"empowers Procore invoicing to manage FIDIC and other international contract standards"* — the only FIDIC-aware app on the marketplace, with 5 installs. |
| **Mail Manager** | 302 / **TonicDM** 1,935 | Email filing/records for project teams. |
| **Planera** 36 / **P6 & OPC Schedule Connectors** | — | CPM scheduling. |
| **Aclaimant** | 9 | Insurance/incident claims — **not** construction commercial claims. |
| Top of marketplace for scale reference | Procore Estimating 17,566; EarthCam 5,813; Newforma Project Center 3,771; Procore ERP Connector by Agave 1,908 | |

**There is not a single dedicated construction claims / entitlement / quantum / delay-claim / notice-deadline application in the Procore App Marketplace.** Not one. Document Crunch is the nearest thing and it is a contract-review product that markets notice generation as a secondary benefit.

**What the marketplace tells us about the gap — read both ways:**
1. *Bull case:* 446 apps, ~$1.3B of platform revenue, 17,850 customers, and zero claims/entitlement apps. Either nobody has tried, or nobody has succeeded.
2. *Bear case:* Document Crunch — the best-funded, best-known contract-intelligence product in construction, with Trimble and Nemetschek money behind it — has **187 installs against 17,850 Procore customers, i.e. ~1.0% penetration**, after a partnership that began in 2022. Clearstory, which solves a much more visceral pain (getting T&M tickets signed), has 173. **The Procore marketplace is not a distribution channel for commercial-risk products.** It is a distribution channel for ERP connectors, cameras and takeoff tools.

---

## 6. WEAKNESSES AND EXPLICIT GAPS

| Gap | Deliberate or unattended? | Evidence |
|---|---|---|
| **No contract-clause → obligation → deadline engine.** Prime Contracts is a financial header record with four dates (issued on, LOI, substantial completion, termination). No notice periods, no clause register. | **Deliberate.** Procore's whole model is a neutral collaboration platform used by owner, GC and sub on the same project. Encoding "your contract says you must notify within 14 days or waive" makes Procore a partisan on one side of a two-sided network. | [Prime Contracts](https://support.procore.com/products/online/user-guide/project-level/prime-contracts) |
| **No notice-trigger detection.** 24 notice templates exist as empty containers. | **Deliberate-ish, drifting toward unattended.** The Contract Review Agent shows they now have the technical capability; they have not pointed it at in-flight notice obligations. | [templates](https://support.procore.com/products/online/user-guide/company-level/admin/tutorials/add-a-template-correspondence-type) |
| **No CPM engine, one schedule per project, one baseline.** | **Deliberate** — they ceded scheduling to P6/MSP and partners (SmartPM, Planera) for a decade. But the Schedule Analyst Agent is the first sign of re-entry. | [Schedule overview](https://support.procore.com/products/online/user-guide/project-level/schedule/overview) |
| **No quantum / recoverable-value estimation, no claim package.** | **Deliberate.** Legal-exposure appetite: a public company will not put a number on "what you could recover from your client" and take the E&O tail. | absence across [/ai/agents](https://www.procore.com/ai/agents), [Change Orders](https://support.procore.com/products/online/user-guide/project-level/change-orders) |
| **No responsibility/causation attribution.** | **Deliberate.** Same two-sided-network reason. | — |
| **Change Event fields have no entitlement dimension.** Change Reason is a cost taxonomy. | **Unattended.** This is a small schema change Procore could make in a quarter; they simply haven't thought in entitlement terms. | [Create a Change Event](https://support.procore.com/products/online/user-guide/project-level/change-events/tutorials/create-a-change-event) |
| **Reporting rigidity.** Custom reports "only use Procore's columns, not custom fields from subcontracts"; report formats restricted. | **Unattended.** Long-standing complaint. | Capterra reviews (§9) |
| **Financials UX is genuinely hard.** Multiple reviewers describe the change-order/change-event double step as redundant and the budget tool as clunky. | **Unattended.** | Capterra reviews (§9) |
| **Total customer growth is only +4%/yr** (16,367 → 17,088 → 17,850). Growth is now almost entirely expansion within existing large accounts. | Strategic — SMB de-emphasised. Relevant because it means **the installed base a startup can sell into is essentially fixed**, and the buying centres are concentrated in ~2,871 accounts. | [10-K](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm) |

---

## 7. ADJACENCY TEST — how hard for Procore to ship "event detection → entitlement matching → evidence → claim package"?

### Verdict: **EASY for the first three steps. HARD for the fourth.**

**Data access — trivial.** They already hold the contract, the RFIs, the submittals, the daily logs, the emails (inbound project address), the photos, the drawings, the meeting minutes, the schedule file, the change events and the budget. No integration required. Datagrid gives them a multimodal index over all of it and Magpie a reasoning layer. This is the single biggest structural advantage any player in this space has.

**Event detection — already shipped.** The Change Analysis Agent, as of 23 July 2026, *"Reviews changes, RFIs, drawings, specifications, and project records to identify scope impacts, cost exposure, schedule risk, and required follow-up actions."* That is step one of the thesis pipeline, GA, in the base Pro package.

**Entitlement matching — one Skill away.** "Skills" (previewed 23 Jul 2026, rolling out August 2026) let a customer *"teach Procore AI their own processes, standards, and best practices"* using *"plain-language prompts or company documents, such as standard operating procedures."* A contractor's commercial director can upload their subcontract notice matrix as a Skill and get most of the way to clause-driven detection **without Procore building anything**. Combined with **Triggers** (agents fire on "new submittals, RFIs, or change order") and **150+ Actions** (create/update Change Events), the raw machinery for "event fires → agent checks contract → agent drafts correspondence item" already exists.

**Evidence collection — already there.** Citations to source files, permission-aware retrieval, multimodal index. This is what Deep Search Agent does.

**Recoverable-dollar estimate and claim package — HARD, and probably permanently so.** Three blockers, in order of severity:
1. **Two-sided network.** Owners, GCs and specialty contractors are all Procore customers on the same project, on the same records. A tool that computes "the owner owes you $412k and here is why they are wrong" is a tool that one Procore customer uses against another Procore customer inside Procore. This is not a technology problem; it is a business-model problem, and it is the reason Procore's marketing for change orders talks about *speed and accuracy* and never about *entitlement*.
2. **Legal exposure appetite.** A public company with a 25% non-GAAP operating margin target for FY2027 does not volunteer to put a number on a disputed claim, or to be discoverable as the party that told a contractor its claim was worth $2M. They already carry an Oracle trade-secrets suit; they are not adding professional-liability exposure.
3. **GTM motion.** Procore sells annual ACV-based platform subscriptions to VPs of Operations and IT, with unlimited seats. Claims/entitlement is bought episodically, by commercial managers and general counsel, often at project level, often on a contingency or day-rate basis. Procore has no motion for that and its pricing model explicitly rejects per-project charging.

**Past behaviour is the tiebreaker.** Procore's shipping record in 2026 is aggressive and fast: Datagrid closed in January, embedded and shipping five agents by 21 May, 20 agents plus a packaged consumption business by 23 July, DroneDeploy agreed for $845M on 29 July. They ship adjacent capability in months, not years, and they buy rather than build when it's faster. Anything a startup proves out on Procore data that looks like *workflow automation* will be a Procore agent within two release cycles. Anything that looks like *taking a commercial position against a counterparty* will not.

**Rating: MEDIUM overall**, decomposing as EASY (detection, evidence, drafting) / HARD (quantum, claim package, adversarial posture).

---

## 8. STARTUP POSTURE: PARTNER, CHANNEL, or ROADKILL?

### Verdict: **ROADKILL if you build "AI over Procore data." PARTNER — narrowly, and on Procore's terms — if you build the adversarial layer Procore structurally cannot.**

**The case for ROADKILL** (and it is strong, and it got much stronger in the last 90 days):
- The Developer Policy forbids parsing, building databases from, or copying API Data without express consent, and forbids using API Data to train/fine-tune/benchmark any AI system. A generic "read Procore, reason over it, output a claim" product is non-compliant by default. ([Developer Policy](https://procore.github.io/documentation/marketplace-policy))
- The API Usage Guidelines route all AI/semantic/analytics use cases away from REST and into a **Design-Partner-gated Agentic API** with no GA date, access "scoped to their use case," and a Procore PM in the loop deciding "whether the use case fits." ([Agentic APIs](https://procore.github.io/documentation/agentic-apis))
- Procore's own SVP of AI & Data said the quiet part out loud on 21 May 2026: *"With Datagrid embedded into Procore, teams **no longer need to rely on separate third-party AI tools** to get answers or move work forward on their projects."*
- Procore now monetises AI by **credit consumption**, so every third-party AI tool on Procore data is direct revenue cannibalisation, not ecosystem enrichment.
- The competitive-product clause ("substantially replicates any features or functionality of the Procore Services") is now much broader than it was in 2024, because Procore Services now include change analysis, contract review, schedule analysis and financial analysis agents.
- Empirically, the marketplace does not distribute this category: Document Crunch 187 installs / 17,850 customers ≈ 1.0% after four years of partnership.

**The case for PARTNER:**
- The three things Procore will not do — **take a side, put a number on it, and produce a document intended to extract money from another Procore customer** — are exactly the three things a revenue-recovery product must do. That is not a feature gap; it is a permanent structural asymmetry created by the two-sided network.
- Procore's own product page sells *"reduce unrecoverable change orders"* — it has named the problem and declined to solve the recovery half.
- The buyer is different. Procore's buyer is Ops/IT with an annual platform budget. The revenue-recovery buyer is the commercial manager / contracts director / CFO with a claims-consultant budget and a live loss. Different budget, different urgency, no seat-count objection (Procore charges no per-seat fee, so nobody is counting logins).
- **Data egress is solvable without fighting Procore's API policy**: the *customer* licenses Procore Analytics (Databricks / Delta Sharing / S3 / Fabric) and can direct their own data to you. Customer data rights, not developer API rights.
- V1 is startable exactly as the founder constraints require: contract PDF upload + a forwarded email address + a CSV/PDF export of the RFI and change-event logs. No Procore partnership needed to prove value on the first ten claims.

**Concretely, the posture that survives:**
1. **Do not position as "AI for your Procore data."** That is the one framing that is both policy-non-compliant and directly competitive with a GA Procore product.
2. **Position as the commercial/entitlement layer that ends in a document with a number on it** — notice packs, entitlement registers, claim submissions — sold to the contracts/commercial function, priced against recovered value or per claim.
3. **Take data from the customer, not the API, for V1** (upload, email forward, Analytics/Delta Share). Add a Procore Marketplace listing later as a *convenience* feature and a trust badge, not as the data spine. Note you cannot use the Private Developer path for a commercial product even with one customer — you would need full Marketplace Partner status.
4. **Assume the Agentic API / Agent Marketplace is a channel you may be invited into, and may be evicted from.** Procore's roadmap explicitly includes an "Agent Marketplace" where "discovery and install handled by Procore." That is a channel with a landlord.
5. **Do not build cross-customer benchmarking on Procore data.** Explicitly prohibited: "Use API Data collected from one organization to directly benefit a different organization or any third party."

**Net:** Procore is not roadkill-you-on-purpose. It is roadkill-you-by-accident, because the thing you'd naturally build first (detect commercial events from project records using AI) is now a shipped Procore agent, and the API terms were rewritten in 2025–26 to keep exactly that work inside Procore. Survive by being adversarial and document-producing, which Procore cannot be.

---

## 9. TOP 5 VERBATIM CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

1. **"The PCO step and Change Event step are redundant and one should be…"** and **"If a user has to edit an older change order for some reason, all subsequent change order statuses need to be edited which is a big waste of productive time."** — Travis J., Project Manager, 2 Sep 2025. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/)
2. **"Financial management is convoluted and requires too many steps."** — Travis J., Project Manager, 2 Sep 2025. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/)
3. **"It can be annoying that you can't amend variations after they are approved. You also can't amend PO/SC SOV line items after an invoice has been uploaded, which makes the invoice process quite time consuming."** — Nikki M., Contract Administrator, 24 Jul 2024. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/?page=5)
4. **"Custom reports only use Procore's columns, not custom fields from subcontracts"** — Gabriela A., PA, 6 Nov 2022; and **"Restricted format of reports. Would like them to be more friendly to share in presented form in an OAC meeting"** — Pete B., Project Executive, 10 Jul 2025. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/) — *the evidence is in there; getting it out in a form you can put in front of a counterparty is the complaint.*
5. **"The Procore cost management tool can be clunky when I was using. The budget tool also falls under this area"** — Verified Reviewer, Assistant Project Manager, 26 Jul 2026; and **"The commitments/billing system is not very detailed. There is not really a good SOV option"** — Lauren G., Office Manager, 22 Mar 2026. [Capterra](https://www.capterra.com/p/56250/Procore/reviews/?page=2)

**Important negative observation about these reviews:** across every review page I could read, **nobody complains that Procore fails to protect their entitlement, fails to warn them about notice deadlines, or fails to help them get paid for extras.** The complaints are about UX friction, cost, reporting rigidity and accounting integration. This is a real signal and it cuts against the thesis on this vendor's surface: the pain the thesis targets is not currently articulated by users as a Procore gap — which means the buyer will not arrive via a "Procore is missing X" search. `Caveat: I could not access Reddit (blocked in this environment) or G2/TrustRadius (403), so the review sample is Capterra-weighted; a Reddit r/ConstructionManagers sweep could still surface the entitlement complaint in the wild.`

---

## 10. HARDEST FACTS (the five strongest numeric findings)

1. **Procore shipped a "Change Analysis Agent" to GA on 23 July 2026** that *"Reviews changes, RFIs, drawings, specifications, and project records to identify scope impacts, cost exposure, schedule risk, and required follow-up actions."* — [procore.com/press/procore-introduces-digital-coworker-packages…](https://www.procore.com/press/procore-introduces-digital-coworker-packages-expands-ai-agent-library-and-previews-skills-to-help-construction-teams-put-ai-to-work)
2. **Document Crunch — the leading AI contract-intelligence product in construction — has 187 installs on the Procore App Marketplace, against Procore's 17,850 customers (~1.0%).** Marketplace totals: **446 apps, 115,558 cumulative installs.** — scraped from [marketplace.procore.com](https://marketplace.procore.com/apps) 19 Aug 2026; customer count from [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm)
3. **Procore's Developer Policy (eff. 30 Sep 2025) prohibits developers from "Scrape, parse, harvest, build databases, bulk export, or otherwise create copies of any API Data… without Procore's express consent" and from using API Data "to train, re-train, fine-tune, or benchmark any machine learning or artificial intelligence algorithm, model, software, or system."** — [Developer Policy](https://procore.github.io/documentation/marketplace-policy)
4. **Procore FY2025: revenue $1,322.5M (+15%), R&D $362.4M (27% of revenue), GRR 95%, NRR 106%, 17,850 customers (+4%), 2,710 customers >$100k ARR (66% of ARR), 115 customers >$1M ARR (20% of ARR), 4,421 employees.** — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm)
5. **Procore agreed to acquire DroneDeploy for ~$845M cash on 29 July 2026, six months after acquiring Datagrid (Jan 2026) — and Procore's SVP of AI & Data stated on 21 May 2026 that with Datagrid embedded, "teams no longer need to rely on separate third-party AI tools."** — [DroneDeploy press](https://www.procore.com/press/procore-to-acquire-dronedeploy-creating-next-generation-platform-that-sees-understands-and-acts-on-the-jobsite); [Datagrid embed press](https://www.procore.com/press/new-procore-ai-experience-embeds-datagrid-into-procore)

**Bonus hard fact (API):** documented Procore rate-limit header examples are **hourly `X-Rate-Limit-Limit: 600`** and **spike `X-Rate-Limit-Limit: 25` per 10 seconds**; failed calls (400/403/404) consume quota identically to successful ones; v2 collection pages default to 10 and max 100. — [Rate Limiting](https://procore.github.io/documentation/rate-limiting)

---

## 11. UNKNOWNS — and what would settle each

| Unknown | What would settle it |
|---|---|
| **Actual dollar cost of Procore, by ACV band.** All published ranges are from competitors selling alternatives. | A real customer quote/renewal invoice, or a public-sector procurement award (US state/municipal RFP tabulations often publish awarded Procore pricing). |
| **Procore Technology Partner fees and tier names.** Procore's docs confirm "associated fees" exist but the Partner Program Guide is not publicly linked. | Request the Procore Partner Program Guide PDF from techpartners@procore.com, or a partner willing to share their Framework Agreement + Technology Partner Addendum commercial terms. |
| **Real adoption of the AI agents.** All 20 are listed as available; Procore gives no attach rate, no AI ARR, no credit-consumption disclosure. Q2'26 results mention AI only as a "business highlight," never as a revenue line. | Q3 2026 earnings call transcript (call held 30 Jul 2026 for Q2; Q3 due late Oct 2026) — analysts will press on AI attach and credit revenue. Or the FY2026 10-K if they begin disclosing an AI metric. |
| **Whether Procore would grant a claims/entitlement startup Agentic API design-partner access**, given the competitive-product clause. | Submit a Design Partner Pilot application with a deliberately adversarial use case and see what the Ecosystem team says. This is a cheap, high-information experiment and I recommend running it. |
| **Whether the Change Analysis Agent actually reads contract clauses or only project records.** Marketing lists "changes, RFIs, drawings, specifications, and project records" — specifications yes, contract terms not stated. | Hands-on trial (Digital Coworker Starter Pack, 6-month term, 3 projects, flat rate) or a Procore demo focused on that agent. |
| **Whether users articulate entitlement/notice pain about Procore anywhere.** Reddit was inaccessible; G2 and TrustRadius returned 403. | A Reddit sweep of r/ConstructionManagers, r/Construction and r/civilengineering for "Procore" + "change order"/"notice"/"claim", plus G2 filtered 1–2 star reviews. |
| **Number of Procore customers who also run a formal claims/commercial function** (i.e. TAM inside the Procore base for this product). | Cross-reference ENR Top 400 against Procore's published customer list; or an industry survey (Dodge/FMI). |
| **Whether Procore's Feb 2026 bundling raised or lowered the effective price of Project Financials** (relevant to how much budget headroom a startup has). | Procore reseller/consultant commentary post-Feb-2026, or a customer renewal comparison. |
