# 09 — InEight (+ brief: CMiC, Deltek)

Research date: 2026-08-19. Target: **InEight Inc.** (wholly-owned subsidiary of Kiewit Corporation).
Secondary, brief coverage: **CMiC**, **Deltek**.

---

## 1. SNAPSHOT

**What it is.** InEight is an integrated capital-project controls and project-information platform for
heavy civil, industrial, energy and infrastructure work. It is explicitly positioned as
"Integrated Software for Capital Construction" and "the preferred choice for mega projects that require
tight control of scope, cost, and schedule."
- https://ineight.com/ (accessed 2026-08-19)
- https://ineight.com/industries/

**Ownership / origin.** InEight is "a wholly owned subsidiary" of Kiewit Corporation, launched in 2014.
It grew out of Kiewit's 2012 acquisition of **Hard Dollar** (estimating, founded 1989 lineage), and expanded
globally in part via the acquisition of **Aeka Consulting**. Kiewit itself is a US$18.2bn-revenue,
~34,500-employee contractor (2025).
- https://www.kiewit.com/about-us/technology-at-kiewit/ineight/
- https://en.wikipedia.org/wiki/Kiewit_Corporation
- Rebrand history: https://www.cioreview.com/news/kiewit-technology-inc-will-now-operate-with-the-name-ineight-inc-nid-2706-cid-25.html

**Teambinder lineage (confirmed).** InEight Document is the former **TeamBinder** product (Australian-origin
document control / project correspondence system). InEight's own current help documentation still instructs
users to look for the welcome email "from *system@teambinder.com*", and ITQlick's pricing page for InEight
Document still lives at the `/teambinder/` URL slug.
- https://learn.ineight.com/Document_Enhanced/Content/Categories/FAQStartPage.htm
- https://www.itqlick.com/teambinder/pricing

**Scale (best available).** InEight's own press release (7 Jan 2026) states it manages "projects worth over
**$1 trillion** globally" and serves "over **850 companies**."  A third-party profile adds "400,000+ users"
and "$400+ billion in projects" — treat the third-party numbers as `UNVERIFIED` and prefer InEight's own.
Revenue and headcount are **not disclosed** (private Kiewit subsidiary).
- https://ineight.com/news/fedramp-authorized-ineight-document/ (2026-01-07)
- https://softwarefinder.com/project-management-software/ineight (`UNVERIFIED` third-party)

**ICP.**
- *Sectors*: Construction & Engineering, Transportation (ports/rail/roads/bridges/airports), Power &
  Renewables, Nuclear, Water, Oil Gas & Chemical, Mining. https://ineight.com/industries/
- *Project size*: mega / capital projects. Explicit self-positioning at the top of the market. Named public
  customers on the homepage include **AECOM, Kiewit, WSP**. https://ineight.com/
- *Buyer types*: contractors, engineers, asset owners, program managers.
  https://www.kiewit.com/about-us/technology-at-kiewit/ineight/
- *Geography*: HQ Scottsdale AZ. Strong **APAC/Australia** footprint inherited from TeamBinder — APAC launch
  announced from Sydney with a dedicated APAC regional director
  (https://ineight.com/news/ineight-introduces-capital-project-management-software-solutions-asia-pacific/),
  and 2025-26 customer wins are heavily AU/mining/resources (Duratec — WA mine site; Mining3; REMCAN).
  https://ineight.com/news/
- *US federal*: InEight Document achieved **FedRAMP Moderate Equivalency Authorization** on 2026-01-07
  (325+ controls), after FedRAMP-Ready in 2025. https://ineight.com/news/fedramp-authorized-ineight-document/

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 Full module map

InEight groups 12-13 modules into four families (https://ineight.com/products/platform/, https://ineight.com/):

| Family | Modules |
|---|---|
| Project Controls | **Control**, **Contract**, **Change**, **Plan & Progress**, Billings |
| Pricing & Scheduling | **Estimate**, **Schedule** |
| Project Information Management | **Document** (ex-TeamBinder), **Model**, Design |
| Construction Intelligence | **Report & Explore** |
| Field / QA | **Compliance**, **Completions** |

---

### 2.2 InEight Change — the change/claims-adjacent module

**Verdict: change orders only. Not claims, not entitlement.**

Product page: https://ineight.com/products/ineight-change/ — headline is
"Streamlined Change Order Management for Capital Construction."

**Object model** (official docs): Issue → **PCO** (Potential Change Order) → **CCO** (Client Change Order).
Issues carry: issue name, full description, start date, **source/cause** (field conditions, client
instruction, etc.), **scope classification** (out of scope / in scope / contingency), and **client
notification status**.
- https://learn.ineight.com/Change/Content/CHNG20.5%201/1%202%20InEight%20Change%20Overview.htm

**PCO Details tab fields** (official docs) — the closest thing to notice/entitlement anywhere in InEight:
- Correspondence section: **"PCO Date client notified"**, "PCO Date price to client", "PCO Client approval
  date", "Executed change order date"
- Schedule impact: **"Requested time extension"**, **"Issue delay days"**, "Forecast days"
- Responsible parties; RFI tracking; Tasks; Revenue category; custom fields; eSign recipients
- https://learn.ineight.com/Change/Content/CHNG20.5%205/PCO%20Details%20tab.htm

These are **manually-entered date and day fields**. There is no clause reference, no notice-window
calculation, no entitlement basis, and no alerting off them in the documented field set.

**CCO object**: signing agreement type (bilateral / unilateral / unassigned), approved time extension,
executed change order amount, DocuSign eSign, and "Generate Change document" from the CCO log.
Supporting documents attach by file, link, or from InEight Document.
- https://learn.ineight.com/Change/Content/CHNG20.5%205/5%202%20Client%20Change%20Order%20CCO.htm

**Official 8-step business process** (InEight's own integrated-solutions doc): Identify Issue → Collect
Relevant Information → **Evaluate Schedule Impacts (build what-if schedules)** → Price the Issue → Create
PCO → Evaluate CCO → Execute Contract Changes → Accept Change into Budget.
- https://learn.ineight.com/integrated_solutions/Content/Business-Processes/Change-Order-Management/Change-Order-Home.htm

**Full published capability list for Change** — Change Order Management; Issue & Change Tracking; Field
Change Initiation (from RFIs or observations); Change Workflow & Approvals; Grouping & Change Order
Creation; Reporting & Audit Trail; Change Pricing & Markups (incl. ROM estimates); Budget Change
Management; Change Order Logging in Contract; Budget Integration of Changes; Budget Change Control;
Cross-Module Data Flow.
- https://ineight.com/software-capabilities-of-ineight-change/

**What is absent, verified across three official sources** (product page, capability page, business-process
doc): the words *claim*, *entitlement*, *notice obligation*, *dispute*, *contract clause*, *prolongation*,
*disruption*, *global claim*, *time-bar*. **`IMPORTANT SEMANTIC TRAP`**: the word "claim" *does* appear
throughout InEight — but it means **claiming quantities / progress claiming** (earned value), not
contractual claims. e.g. "InEight Plan — Claiming Quantities"
(https://learn.ineight.com/Plan/Content/Video-search/Claiming-Quantities-video.htm) and "Claim in InEight
Control" (https://learn.ineight.com/integrated_solutions/Content/Business-Processes/Earned-Value-Management/record-actuals/claim-in-control.htm).
Do not read those as claims management.

**Does it track notice obligations?** No. Evidence: (a) the only notice-shaped artefact is the manual
"Date client notified" field on a PCO; (b) InEight's own end-to-end change-order business process document
omits notice entirely; (c) there is no contract-clause object anywhere in the Change or Contract data model.

---

### 2.3 InEight Document (ex-TeamBinder) — the contemporaneous record

This is InEight's **strongest thesis-relevant asset**, and it is materially better than the marketing page
suggests. Detail below is from InEight's own Document Mail User Guide, Release 26.3 (58pp):
https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf

Modules inside Document: Document register, **Mail**, **Transmittals**, Packages, Submittals, Lots, Forms,
Checklists, Vendor Data, Reports, XL Upload, Bluebeam, Gallery, **Mobile App**, Tenders, Defects,
**Outlook Integration**, Office Integration.
- https://learn.ineight.com/Document_Enhanced/Content/Categories/TopicsStartPage.htm

Thesis-relevant mechanics, verbatim from the user guide:

- **Configurable contractual mail types.** Admins can "Configure a new mail workflow to create a new mail
  type" with a Base Template, mandatory recipients, mandatory fields, and default text input. This is how
  projects create *Notice of Delay*, *EOT Application*, *Variation Notice* mail types. (§3.2)
- **Response deadlines.** Mail type config includes **"Default Response period: Select the number of days
  the mail must be responded to by."** (§3.2)
- **Open/closed obligation state.** "The default status codes for mail are **outstanding** (applied to all
  mail by default) and **closed out**. Additional mail status codes can be configured by administrators."
  Users "Filter mail by status to see which items require action from you or a recipient." (§2.1, §3.7)
- **Automatic thread graph.** "InEight Document builds a thread link between mail items automatically when:
  a mail item is responded to via a reply or forward; a mail item is forwarded with other mail; mail is
  manually linked to other items (mail, documents, transmittals, forms, etc.)." (§3.5)
- **Direct Document → Change bridge.** Mail workflow config has **"Enable Issue Creation: Select this option
  for mail to create an issue in InEight Change."** (§3.2) This is the single most important integration
  fact in this report.
- **Email ingestion (email-In).** External emails route into the project via an InEight-provisioned address
  into an *Unregistered* mailbox; a nominated person assigns To/From/Cc and mail type; "The details of how
  and when the email was received and when it was processed are stored as part of the mail and **cannot be
  edited**." Reference numbers carry forward on replies. (§3.6, §3.8)
- **Outlook integration** as an alternative client. (§1, and https://ineight.com/resources/integrations/)
- **Mail history / audit.** History tab records links added/removed, folder updates, mail received, changes
  in mail or thread status; exportable to Excel. (§2.10)
- **Attachments become controlled documents.** "Process attachments as controlled documents" → bulk upload
  → optional transmittal. (§3.1)
- **Smart Folders / Dynamic Folders** auto-file mail by rules and by metadata. (§1.3)
- **Transmittals** "automatically record the date and time of each download."
  https://ineight.com/products/ineight-document/
- **Audit trail claim:** "Every file, version, and user action is captured in a secure, verifiable audit
  trail." https://ineight.com/products/ineight-document/
- **Published outcome numbers (vendor-claimed):** "75% reduction in project document search time";
  "30% decrease in RFI, submittal, and workflow processing time"; "up to a 90% drop in time spent emailing
  files and attachments"; "no limits on the number or size of files per project"; supports "thousands of
  users and millions of documents." https://ineight.com/products/ineight-document/

**vs. Aconex for contemporaneous record-keeping.** Honest read:
- Aconex's differentiator is the **immutable, neutral, cross-organisation mail log** that no party —
  including administrators — can edit, which is precisely why owners mandate it on rail/airport/LNG
  programmes, plus BSI Kitemark for ISO 19650. InEight Document's audit trail is strong and FedRAMP-Moderate
  authorised, but it is a *vendor-hosted audit trail on a single-tenant project*, not Aconex's
  "each organisation owns its own workspace, the shared record is un-rewritable" architecture.
  https://softwarefinder.com/resources/ineight-vs-aconex-comparison
- InEight's own comparison page attacks Aconex on folder structure, version distribution to field teams,
  workflow configurability, audit-trail retrieval speed, external-user friction, absence of a vendor
  deliverables module, and integration lock-in to the Oracle ecosystem. https://ineight.com/comp-oracle-aconex/
- **Net for the thesis:** for pure evidentiary weight in a dispute, Aconex is still the stronger artefact.
  For *linking* correspondence to a commercial change record, InEight is stronger (the Mail → Change issue
  bridge has no Aconex equivalent of comparable depth). Both are **passive registers**: neither reads the
  mail and tells you an entitlement exists.

**Data egress reality.** Project archives are available "upon request": a ZIP containing all mail, all
document revisions, comments, redlines, transmittals, packages, reports and address book, delivered with an
offline "QView" viewer, **with no security features** — and "individual contract archives from Portfolio
instances incur charges."
- https://learn.ineight.com/Document_Enhanced/Content/Categories/FAQStartPage.htm

---

### 2.4 InEight Contract — stores, does not extract

**Verdict: a commercial contract *register* + payment engine. It does not read contracts.**

Published capability list (verbatim groupings): Contract Creation & Tracking; Automated Contract Generation;
Bid to Contract Conversion; Contract Approval Workflows; Custom Fields & Attributes; Document Management &
E-Signature; Schedule of Values & Line Items; Multiple Contracts Support; Change Order Logging in Contract;
Vendor Management & Compliance; Retention Management; Transaction History; Progress Payment Invoicing;
Invoice Review & Approval Workflow; Payment Status & Analytics; Subcontractor Invoice Portal; Bills in
Process Views; Outstanding Bills View; Cross-Module Data Flow; ERP System Integration; Cost Reporting &
Dashboards; Committed vs. Uncommitted Costs; Project Cost Capture.
- https://ineight.com/software-capabilities-for-ineight-contract/
- https://ineight.com/products/ineight-contract/

Marketing language: "Speed up contract creation with intelligent, auto-filling **templates**"; "automated
validations ensure requests align with **contract terms**, which reduces disputes and delays."
Note the second phrase is about *pay-application validation against SOV/line items*, not clause semantics.

**Absent:** clause extraction, obligation registers, obligation owners/due dates, notice provisions,
liquidated damages tracking, time-bar clauses, insurance/bond expiry as a first-class object,
NLP/AI on contract text. The orientation is overwhelmingly **downstream (subcontracts, POs, vendor change
orders, progress payments)** rather than upstream prime-contract administration.

---

### 2.5 InEight Schedule / Plan — how close to delay-impact analysis?

- Full CPM; "knowledge-based planning" replacing pure CPM; integrated risk management; what-if scenarios;
  bidirectional sync with Primavera P6 and Microsoft Project.
  https://ineight.com/products/ineight-schedule/ , https://ineight.com/resources/integrations/
- **AI benchmarking (the real, long-standing AI feature).** "During the pre-planning stage, Schedule's
  artificial intelligence (AI) engine analyzes your Knowledge Library to make intelligent suggestions based
  on current project parameters related to scope, project type, geography and more." It calibrates durations
  against historical benchmarks with context adjustment (documented example: Topsides Detailed Engineering
  benchmarked at 212 days, adjusted to 147 days for 50 vs 72 drawings), and scores plans on a
  "**Basis Realism Index**" (0-10) with Detail and Continuity sub-metrics.
  https://ineight.com/news/ai-benchmarking/ (**2020-03-02 — `FLAG: source older than 2023`**)
- 2021 elaboration: AI suggests durations/sequencing/risks/costs from similar past projects, validates
  unrealistic durations and resource conflicts, and learns from accept/reject. Explicitly "an interactive
  tool" and "advisor," not a decision-maker.
  https://ineight.com/blog/leveraging-the-power-of-ai-in-construction-scheduling-software/ (2021-10-19)

**Distance to delay-impact analysis: large.** InEight Schedule is *forward-looking* (benchmarking, risk,
what-if). There is **no evidence** of: as-planned vs as-built, windows analysis, time impact analysis (TIA),
collapsed as-built, schedule-version forensic comparison, or delay attribution. Compare Deltek Acumen Fuse
(§10) which does exactly this. The one bridge is the change-order process step "Evaluate Schedule Impacts —
build what-if schedules," i.e. **prospective TIA-lite done manually by a planner**, not automated.

### 2.6 Plan & Progress, Compliance, Control, Report

- **Plan & Progress**: work packages; daily planning rolled up from work packages; **"Daily logs & field
  reports"** — "record daily jobsite notes and attachments"; mobile field app with **offline** quantities,
  hours, checklists; **photo/video capture with geofencing validation**; barcode scanning; digital timesheets
  with geofence enforcement; rules of credit; bidirectional P6 sync; Schedule of Values linking field
  progress to contract line items. **Field teams can initiate change issues from RFIs or observations.**
  https://ineight.com/software-capabilities-of-ineight-plan-progress/ , https://ineight.com/software-capabilities-of-ineight-change/
- **Compliance**: configurable form builder + mobile app, offline, incident reporting with notes/photos/GPS,
  automated reminders, status tracking. EHS-oriented; no dedicated daily-diary object.
  https://ineight.com/products/ineight-compliance/
- **Control**: cost forecasting, multiple budget versions, auto-baseline update on approved change orders,
  EVM (PF, LEI, CPI, SPI), field actuals integration. https://ineight.com/products/ineight-control/
- **Report & Explore**: portfolio reporting, printable formatted reports, report subscriptions, S-curve and
  earned-value reporting. No evidence found of a self-service warehouse, Power BI connector, or semantic
  layer on the public page. https://ineight.com/products/ineight-report/

### 2.7 AI features 2024-2026 — thinner than expected

- Homepage claims **"Outcome-Driven AI"**: "deeply detailed, structurally connected data" as "a foundation
  for AI that drives improved project outcomes." No named product, model, capability or metric.
  https://ineight.com/
- Schedule "AI-powered tools help you start with realistic, data-driven schedules based on previous
  projects." https://ineight.com/products/ineight-schedule/
- The substantive AI documentation is the 2020-2021 Basis/Schedule benchmarking engine (above).
- Platform release notes reviewed (Release 26.5 Jun 2026; 26.7 preview Sep 2026) contain **no AI features** —
  the notable items are a payroll WBS default and an APIM integrations framework with a breaking Account
  Codes API change planned for 26.10. https://learn.ineight.com/Platform/Content/Categories/ReleaseNotesStartPage.htm
- **No evidence found** of generative AI, LLM document analysis, AI agents, or AI contract/clause reading
  anywhere in InEight's product surface as of Aug 2026. Marked `UNVERIFIED-NEGATIVE` (absence of evidence in
  public sources; a customer roadmap NDA could contradict).

---

## 3. CAPABILITY MATRIX (0-3)

| # | Dimension | Score | Justification | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | **2** | Contract module stores/generates contracts from templates with SOV & line items; Document stores contract files. Stored as records + PDFs, never parsed. | https://ineight.com/software-capabilities-for-ineight-contract/ |
| 2 | clause_extraction | **0** | No clause object, no NLP, no obligation register anywhere in Contract's published capability list. | https://ineight.com/software-capabilities-for-ineight-contract/ |
| 3 | notice_detection | **1** | Only artefact is a manual "PCO Date client notified" field; the official change-order process omits notices entirely. Nothing detects. | https://learn.ineight.com/Change/Content/CHNG20.5%205/PCO%20Details%20tab.htm |
| 4 | deadline_tracking | **2** | Real per-mail-type "Default Response period (days)", outstanding/closed-out statuses, review due-by dates — but for correspondence turnaround, not contractual notice windows. | https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf §3.2 |
| 5 | rfi_event_ingestion | **3** | RFIs native in Document (forms/mail); RFI tab on Issues/PCOs/CCOs; field can raise change issues directly from RFIs. | https://ineight.com/software-capabilities-of-ineight-change/ |
| 6 | email_ingestion | **3** | Native Outlook integration plus provisioned email-In addresses routing external mail into the project register with immutable receipt timestamps. | https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf §3.8 |
| 7 | daily_report_ingestion | **3** | "Daily logs & field reports… record daily jobsite notes and attachments", offline mobile quantities/hours/checklists, geofenced photos/video, timesheets. | https://ineight.com/software-capabilities-of-ineight-plan-progress/ |
| 8 | schedule_integration | **3** | Native CPM module plus bidirectional Primavera P6 and MS Project sync; schedule impact step inside change process. | https://ineight.com/resources/integrations/ |
| 9 | change_order_workflow | **3** | Core strength: Issue→PCO→CCO, pricing & markups, approvals, grouping, budget auto-update, eSign, audit trail. | https://ineight.com/products/ineight-change/ |
| 10 | claim_identification | **1** | No claim object. Only adjacent fields are Issue "cause" and scope = out-of-scope. "Claim" in InEight means progress claiming (quantities), not contractual claims. | https://learn.ineight.com/Plan/Content/Video-search/Claiming-Quantities-video.htm |
| 11 | delay_detection | **1** | "Issue delay days" and "Requested time extension" exist as manually-keyed fields; no detection, no as-built comparison. | https://learn.ineight.com/Change/Content/CHNG20.5%205/PCO%20Details%20tab.htm |
| 12 | responsibility_attribution | **2** | Structured Issue "source/cause" + "responsible party"/"responsible parties" sections on Issue, PCO and CCO — manual entry, no inference. | https://learn.ineight.com/Change/Content/CHNG20.5%201/1%202%20InEight%20Change%20Overview.htm |
| 13 | contemporaneous_evidence_graph | **3** | Auto-built mail threads; manual links mail↔documents↔transmittals↔forms; Supporting Documents tab pulls from Document into Change; mail can auto-create a Change issue; exportable history. | https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf §3.2, §3.5, §3.7 |
| 14 | evidence_completeness | **0** | Nothing anywhere assesses whether a change/issue record is evidentially sufficient or flags missing proof. | https://ineight.com/software-capabilities-of-ineight-change/ |
| 15 | recoverable_dollar_estimation | **2** | "Change Pricing & Markups… including ROM estimates and custom markups", priced off the live estimate — but this prices a change order, not a claim (no prolongation/disruption/acceleration heads of claim). | https://ineight.com/software-capabilities-of-ineight-change/ |
| 16 | claim_package_generation | **1** | "Generate Change document" from the CCO log + Supporting Documents tab produces a change-order pack, not a narrative claim submission. | https://learn.ineight.com/Change/Content/CHNG20.5%205/5%202%20Client%20Change%20Order%20CCO.htm |
| 17 | notice_drafting | **1** | Configurable mail types with base templates, default text input, custom footers and mandatory fields — a form, not a drafted notice. | https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf §3.2 |
| 18 | schedule_impact_analysis | **2** | Documented step: "Evaluate Schedule Impacts… build what-if schedules" + Schedule risk/what-if. Prospective only; no TIA, windows, or forensic version comparison. | https://learn.ineight.com/integrated_solutions/Content/Business-Processes/Change-Order-Management/Change-Order-Home.htm |
| 19 | procore_integration | **0** | Procore does not appear anywhere on InEight's published integrations list (which does name CMiC, Sage, QuickBooks, Viewpoint Vista, etc.). | https://ineight.com/resources/integrations/ |
| 20 | autodesk_integration | **2** | Navisworks, Revit and Civil 3D listed (model/design side). No Autodesk Construction Cloud / BIM 360 document integration found. | https://ineight.com/resources/integrations/ |
| 21 | outlook_gmail_integration | **3** | Dedicated Outlook Integration tool + email-In; "all project mail is automatically stored, tracked, and accessible." Gmail absent (irrelevant for this ICP). | https://ineight.com/products/ineight-document/ |
| 22 | mobile_workflow | **3** | Document mobile app; Compliance mobile with offline forms/photos/GPS; Plan & Progress offline field app with geofencing and barcode scanning. | https://ineight.com/products/ineight-compliance/ |
| 23 | audit_trail | **3** | "Every file, version, and user action is captured in a secure, verifiable audit trail"; exportable mail history; uneditable email receipt metadata; FedRAMP Moderate Equivalency (325+ controls). | https://ineight.com/news/fedramp-authorized-ineight-document/ |
| 24 | portfolio_risk | **2** | Report & Explore gives portfolio status/issues/risks and EVM indices; Schedule has integrated risk. No portfolio-level entitlement/claims exposure view. | https://ineight.com/products/ineight-report/ |
| 25 | performance_pricing_compatibility | **0** | Pure seat subscription. InEight explicitly markets that "contractual pricing is clear and stable" with no change during the contract — the opposite of contingency/outcome pricing. | https://ineight.com/pricing/ |
| 26 | consultant_replacement_potential | **1** | It is the *source data* claims consultants request (mail register, threads, daily logs) — it does not perform any analysis a consultant would be paid for. | https://learn.ineight.com/Document_Enhanced/Content/Resources/PDFUserGuides/DocumentMail.pdf |

`SCORES| 2,0,1,2,3,3,3,3,3,1,1,2,3,0,2,1,1,2,0,2,3,3,3,2,0,1`

---

## 4. PRICING

**Published, high confidence — InEight NOW self-serve (per user):**

| Product | Month-to-month | Annual | Annual total |
|---|---|---|---|
| Estimate NOW | $260/mo | $199/mo | $2,388/yr |
| Schedule NOW | $199/mo | $150/mo | $1,800/yr |
| **Document NOW** | **$73/mo** | **$52/mo** | **$624/yr** |
| Compliance & Completions NOW | $55/mo | $37/mo | $444/yr |

Source: https://ineight.com/now/ . Self-service implementation; Estimate NOW excludes benchmarking;
Schedule NOW includes one "Expert NOW" session. **Note: Change and Contract are NOT sold via NOW** — the
change/claims-adjacent modules are enterprise-sales-only. InEight NOW launched 2025-01-22 "starting at
$1,250/6 months with unlimited users" (Estimate + Schedule at launch).
https://ineight.com/news/ineight-launches-new-software-buying-experience-ineight-now/

**Enterprise — not published.** "Pricing for your configurable, modular InEight solution starts with an
in-depth conversation about your business needs and priorities"; priced on company size, products, and
contract length; implementation timelines "weeks to months."  https://ineight.com/pricing/

**Third-party ranges (`LOW CONFIDENCE`, reverse-engineered, method disclosed by source):** ITQlick estimates
InEight Document at ~$52/user/month (~$6,240/yr for 10 users), implementation $1,000 (SMB) to $10,000+
(enterprise), maintenance/support ~20% of licence, training $100-$500/session, integrations $200-$2,000;
first-year total for 10 users $8,488-$20,288. https://www.itqlick.com/teambinder/pricing
SelectHub lists InEight as "Starts at $1,000 or more, Per User, Annually," no free trial.
https://www.selecthub.com/construction-management-software/ineight/

**Sales motion.** Two-track: (a) enterprise, consultative, services-attached, multi-module land-and-expand
("start with the products that solve your most urgent challenges and expand… on your timeline"); (b) since
Jan 2025, a self-serve PLG wedge (NOW) deliberately aimed at "individuals or small teams just getting
started" piloting before enterprise adoption. **Implementation services are effectively required for
enterprise** (custom proposal + weeks-to-months implementation), and P6 migration for Schedule reportedly
needs "about a week of services… for every big project converted" (`UNVERIFIED` third-party).

---

## 5. INTEGRATIONS & API

**Published integrations** (https://ineight.com/resources/integrations/):
- ERP: Oracle EBS / Cloud ERP / Fusion, SAP incl. S/4HANA, Microsoft Dynamics, JD Edwards (E1 & World),
  **Deltek Costpoint**, **CMiC**, Sage 300, QuickBooks Desktop, Viewpoint Vista
- Schedule: **Oracle Primavera P6**, Microsoft Project, Deltek Open Plan
- Design/model: Autodesk Navisworks, Revit, Civil 3D
- Docs/collab: Microsoft Office, SharePoint, **Outlook**, OneDrive, Dropbox, Objective ECM,
  **Bluebeam (two-way)**, Adobe Sign, DocuSign
- Field/specialist: EarthCam, Jovix, SiteSense, MC Squared, Felix
- SSO: Okta, F5, Ping Identity
- Self-description: "an open, integration-ready platform" with "open APIs that allow customers and partners
  to build additional connections," plus CSV and XML file utilities.

**API reality.**
- Developer portal at https://developer.ineight.com/ , organised into **Integration APIs** and
  **Reporting APIs**. "restful external APIs."
- Access model: create an **APIM** account via self-signup, then Products → External Integrations →
  Subscribe → obtain a **Subscription Key** sent in request headers; bearer tokens also documented.
  https://developer.ineight.com/getting-started
- Managed under Azure API Management; release notes show ongoing API versioning discipline (a breaking change
  to Account Codes APIs is announced for Release 26.10).
  https://learn.ineight.com/Platform/Content/Categories/ReleaseNotesStartPage.htm
- **Could not verify:** the actual endpoint catalogue per module (whether Document Mail, Change Issues/PCOs
  and Contract are exposed for read *and* write), rate limits, webhook/event support, or sandbox
  availability. All gated behind portal signup. `UNVERIFIED`.
- **No public app marketplace.** InEight has no equivalent of the Procore App Marketplace or Autodesk App
  Store. Integrations are a curated vendor list, not an ecosystem.
- **Data egress:** works, but as a service request — a ZIP project archive with an offline QView viewer,
  including all mail, all revisions, comments, redlines, transmittals, packages, reports and address book;
  chargeable for individual contract archives on Portfolio instances.
  https://learn.ineight.com/Document_Enhanced/Content/Categories/FAQStartPage.htm

**Notable absence: Procore.** InEight lists competitor-adjacent ERPs (CMiC, Sage, Viewpoint) but not Procore
or Autodesk Construction Cloud. Read as strategic: InEight sells against Procore in the mid/upper commercial
segment and has no incentive to be a Procore satellite.

---

## 6. WEAKNESSES AND EXPLICIT GAPS

| Gap | Deliberate or unattended? | Reasoning |
|---|---|---|
| No claims/entitlement object at all | **Deliberate** | InEight is owned by Kiewit, one of the largest contractors on earth. Shipping software that *tells a contractor it has a claim against an owner* creates legal-discovery exposure for the vendor and channel conflict with Kiewit's own owner relationships. Also: many InEight buyers are **owners** (the module map, pricing and FedRAMP push are owner-friendly). A claims engine has an inherently adversarial posture that a two-sided platform can't take. |
| No clause extraction / obligation register | **Unattended → opportunity** | Contract is a *downstream* commercial engine (subcontracts, POs, pay apps). Prime-contract administration is simply not on the product's map. Nothing about their architecture prevents it; they just haven't valued it. |
| No notice-window tracking | **Unattended → opportunity** | The primitives exist (mail types, response periods, outstanding/closed-out states, mail→issue creation). What's missing is the *contract-derived* deadline — i.e. exactly the layer this thesis proposes. |
| No delay/forensic schedule analysis | **Deliberate** | InEight's schedule thesis is explicitly forward-looking ("knowledge-driven planning", benchmarking, realism index). Forensic delay analysis is a different discipline and a different buyer (expert witness, not planner). Deltek Acumen owns that ground. |
| Evidence linking is 100% manual | **Unattended → opportunity** | Every documented link (Supporting Documents on an Issue, manual mail links) requires a human to remember the connection at the moment it matters. Nothing infers it retroactively. |
| Weak AI story | **Unattended** | Best documented AI is from 2020-2021. 2026 release notes contain zero AI. Homepage says "Outcome-Driven AI" with no product behind it. For a platform sitting on $1tn of structured project data this is a striking under-exploitation. |
| Reporting | **Unattended** | Recurring reviewer complaint (see §9), and Report & Explore's public page shows no modern BI/warehouse layer. |
| No Procore integration, no marketplace | **Deliberate** | Competitive positioning. |
| Steep learning curve / heavy config | **Deliberate trade-off** | "Unmatched configurability" is the stated differentiator; the cost is a documented adoption problem. |

---

## 7. ADJACENCY TEST — how hard for InEight to ship "event detection → entitlement matching → evidence → claim package"?

### **MEDIUM-HARD** (call it HARD for the full pipeline; MEDIUM for the first two-thirds)

**Data access — EASY.** They already hold everything the pipeline needs, in structured form and in one
tenancy: the correspondence register with threads and immutable receipt timestamps, RFIs, submittals,
transmittal download receipts, daily logs and geofenced photos, timesheets and quantities, the live estimate
(for pricing), the CPM schedule with P6 sync, the budget/EVM baseline, and an Issue→PCO→CCO spine with cause,
scope classification, responsible party, delay days and time extension already modelled. Nobody else has this
much of the pipeline's raw material under one roof for heavy civil. This is the single strongest argument
against the thesis.

**Missing technical pieces — MEDIUM.** They would need: (1) a contract-clause layer (they have none, and no
document-AI capability demonstrated anywhere); (2) an event-detection model over mail/daily logs (they have
no LLM/NLP product surface at all as of Aug 2026); (3) evidence-completeness scoring; (4) claim narrative
generation. Items 1, 2 and 4 are net-new competencies for this org, not extensions.

**Org incentive — HARD.** Kiewit ownership is the crux. A Kiewit subsidiary shipping an entitlement engine
sells contractors a weapon that Kiewit's own owner-side customers and JV partners will be on the receiving
end of. InEight has been steadily broadening toward **owners** (FedRAMP for federal agencies, owner-oriented
platform messaging, "owners, contractors and engineers"). Entitlement automation is structurally
contractor-partisan. That is a board-level conflict, not a roadmap conflict.

**GTM motion — MEDIUM.** Enterprise, services-attached, multi-year, land-and-expand. Adding a claims module
fits the motion (another SKU into an existing account). The Jan-2025 InEight NOW launch shows they can also
ship self-serve. Neither is an obstacle.

**Legal-exposure appetite — HARD.** Their public language is conspicuously non-adversarial: change orders are
framed as "protecting margins," "reducing disputes," "aligning stakeholders." Even the change-order product
page avoids the word *dispute* as an objective. A product that asserts entitlement and drafts notices carries
professional-liability and discoverability risk that a contractor-owned vendor will price very high.

**Past M&A and shipping behaviour — MEDIUM.** They do buy (Hard Dollar 2012, TeamBinder/Aeka), and they do
integrate acquisitions properly (TeamBinder is now genuinely wired into Change via mail→issue creation). But
shipping velocity on net-new intelligence is slow: the AI benchmarking engine dates to 2020 and has no
visible successor six years on. The likeliest path for them is **acquisition of a claims/entitlement startup**
rather than internal build — which is directly relevant to §8.

---

## 8. STARTUP POSTURE: **PARTNER**, tending to **ACQUISITION TARGET**. Not roadkill.

- **Not roadkill**, because the specific capability is (a) absent, (b) blocked by an ownership conflict that
  doesn't expire, and (c) requires a competency (document/clause AI) they have not demonstrated in any
  product as of Aug 2026.
- **Partner** is the natural shape: InEight is the *system of record*; the startup is the *system of
  inference* on top. The integration surface is real — REST Integration APIs + Reporting APIs under Azure
  APIM, Outlook/email-In already normalising correspondence, and full ZIP project archives available for
  bulk backfill. A V1 could start on **exported project archives + email forward**, exactly matching the
  solo-founder constraint, with no InEight cooperation required.
- **Channel is weak**, because there is no marketplace, no app store, and no partner-listing motion. Getting
  distribution through InEight means a bizdev relationship, not a self-serve listing.
- **Watch item:** if a claims/entitlement startup gets traction in heavy civil, InEight is a plausible
  acquirer *of the technology* — but Kiewit ownership means they'd more likely buy it to make it
  "dispute-avoidance" than to make it "claims maximisation."

---

## 9. TOP 5 VERBATIM CUSTOMER COMPLAINTS

**Caveat before reading these:** the public review corpus for InEight is thin (Capterra 4.4/5 from **15**
reviews; G2 ~48 reviews, page blocked to fetch; SelectHub aggregates 113) and is dominated by **InEight
Estimate** users, not Change or Document users. Treat as directional.

1. **"Lacks good reporting function/capability."** — Alec S., Estimator, 4★, 2021-08-19.
   https://www.capterra.com/p/161032/InEight/reviews/
2. **"Trying to get other programs to work with this software is a challenge."** — Capterra reviewer.
   https://www.capterra.com/p/161032/InEight/
3. **"It takes a long time to learn the program and get familiar with the actions."** — Chad O., Chief
   Estimator, 5★, 2018-06-12. https://www.capterra.com/p/161032/InEight/reviews/
4. **"The interface is not that easy to adopt. People with less interaction of digital devices can have
   tough time."** — Gultasab I., Lead Estimator, 4★, 2020-08-28.
   https://www.capterra.com/p/161032/InEight/reviews/
5. **"Customer support is not as responsive as it was years ago."** — Mark G., Federal Program Manager, 5★,
   2018-06-11. https://www.capterra.com/p/161032/InEight/reviews/

Supporting (aggregated, not verbatim-attributed): SelectHub reports a "steep learning curve" requiring
"substantial training to master," a company that "hesitated to continue using InEight due to its
complexity," and that "integrating InEight with other programs posed a challenge" — concluding it is
"better suited for larger firms with dedicated IT resources than smaller companies."
https://www.selecthub.com/construction-management-software/ineight/
Also: "It might take a while to generate its report if a project contains many components." — Jhonny D.,
Senior IT Manager, 5★, 2025-04-15. https://www.capterra.com/p/161032/InEight/reviews/

**Thesis-relevant read:** nobody publicly complains that InEight can't do claims — because nobody expects it
to. The complaints are about reporting, integration friction and complexity. That is *not* evidence of
proven, paid-for entitlement pain inside the InEight base. Per the brief's standard, a missing feature is
not white space.

---

## 10. HARDEST FACTS (5 strongest numeric facts)

1. InEight manages **projects worth over $1 trillion globally** and serves **over 850 companies** — vendor's
   own statement, 2026-01-07. https://ineight.com/news/fedramp-authorized-ineight-document/
2. **InEight Document NOW: $73/user/month month-to-month, $52/user/month annual ($624/yr)** — published
   self-serve price for the document-control/correspondence module.
   https://ineight.com/now/  (Estimate NOW $260/$199; Schedule NOW $199/$150; Compliance & Completions NOW $55/$37)
3. **InEight Document holds FedRAMP Moderate Equivalency Authorization, assessed against 325+ security
   controls**, granted 2026-01-07 (FedRAMP-Ready in 2025).
   https://ineight.com/news/fedramp-authorized-ineight-document/
4. Vendor-claimed Document outcomes: **75% reduction in project document search time; 30% decrease in RFI,
   submittal and workflow processing time; up to 90% drop in time spent emailing files and attachments.**
   https://ineight.com/products/ineight-document/
5. **Deltek Acumen Fuse evaluates schedules against 600+ industry-aligned metrics** (DCMA, DOE, GAO, NASA,
   AACE) and performs "half-step delay analysis" producing "audit-ready evidence that stands up to reviews,
   claims, and compliance audits." https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse

Bonus hard fact for the ICP question: **CMiC is used by 25% of ENR's Top 400 contractors**, has **400+ cloud
customers**, **30+ customers with $1B+ revenues**, and processes **$100B in construction revenue annually**.
https://cmicglobal.com/

---

## 11. UNKNOWNS

| Unknown | What would settle it |
|---|---|
| InEight's actual revenue, headcount, growth | Kiewit does not break out subsidiary financials; would need a Kiewit annual report segment note or an InEight exec interview. |
| The real API endpoint catalogue — is Document Mail readable/writable via API? Are Change Issues/PCOs writable? Webhooks? Rate limits? | Sign up at https://developer.ineight.com/ (free self-signup, APIM subscription key) and enumerate Products → External Integrations. **This is the single highest-value next step** — it determines whether a V1 can sit live on top of InEight or must run off exported archives. |
| Whether any customer has configured Document mail types as contractual notice registers (Notice of Delay, EOT) in practice | Interviews with 3-5 AU heavy-civil contract administrators using InEight Document; or an InEight AU case study. The mechanism exists (§2.3); adoption is unknown. |
| Whether the "Enable Issue Creation" mail→Change bridge is widely used or a dead setting | Same interviews, or an InEight implementation consultant. |
| Whether InEight has an unannounced LLM/document-AI roadmap | Attend/see materials from InEight's own "AI & Data Transformation in Construction 2026" event (https://ineight.com/event/ai-data-transformation-in-construction-2026/) or a customer under NDA. |
| Whether InEight NOW will ever carry Change/Contract | InEight NOW page changes over time; currently Estimate/Schedule/Document/Compliance only. |
| Whether any Procore↔InEight connector exists via a third party | Procore App Marketplace search (blocked/404 in this session). |
| G2's 48-review corpus (blocked, 403) | Manual browse of https://www.g2.com/products/ineight/reviews |

---
---

# BRIEF: CMiC

**What it is.** CMiC is a **single-database construction ERP** — accounting/financials, job costing, payroll/HCM,
project management, procurement, equipment/inventory, quality & safety, drawing and document management — now
marketing itself as "the **First AI-Powered Construction ERP**." Its ICP is enterprise and upper-mid general
contractors, subcontractors and civil/heavy-highway firms: **25% of ENR's Top 400 contractors**, **400+ cloud
customers**, **30+ customers with $1B+ revenues**, **$100B in construction revenue annually** on the platform.
Its project-management surface names **Change Management**, **Subcontract Management**, **Document
Management** and **Drawing Management**, with Project Controls covering financial forecasting (GC Monitor),
WIP, billing and change management — "identify issues early in the process and course correct in a timely
manner." It integrates with third-party construction AI (e.g. Trunk Tools) rather than shipping deep native
document AI. Crucially, CMiC is a **named integration partner of InEight** (ERP side), so the two coexist in
the same accounts rather than compete head-on.

**Claims/entitlement capability: NO.** Across the homepage, products index and project-management pages there
is **no mention of claims, entitlement, notices, time-bar tracking, delay analysis or dispute preparation**.
CMiC's change management is financial/commercial change-order processing tied to job cost and subcontracts —
the same shape as InEight Change, one layer more accounting-centric. Correspondence, RFIs, submittals, meeting
minutes and daily journals are not surfaced as first-class marketed features on the public product pages
(`UNVERIFIED` whether they exist deeper in the product — CMiC's public site is unusually thin, and several
product URLs 404'd during this research).

URLs:
- https://cmicglobal.com/
- https://cmicglobal.com/products/
- https://cmicglobal.com/products/project-management/
- https://cmicglobal.com/products/project-management (Project Controls detail)
- Listed as an InEight ERP integration: https://ineight.com/resources/integrations/

---

# BRIEF: Deltek

**What it is.** Deltek is a project-based-business software group (private equity owned; Roper Technologies
sold it — `UNVERIFIED` current ownership, not researched here). Its construction-relevant portfolio splits
three ways: **ComputerEase** (cloud ERP for small/mid contractors — job costing, WIP, committed costs, AIA and
unit billing, retainage, certified payroll, lien waivers, daily logs, job photos, submittals, RFIs and change
orders; **4,000+ contractors**; "growing small and specialty contractors to national general contractors";
**6,000+ construction firms** across Deltek overall); **Costpoint** (GovCon ERP) and **Vantagepoint** (A&E
firms); **GovWin IQ** (public-sector pursuit intelligence); and **Acumen** (schedule + risk).

**Claims/entitlement capability — split verdict:**
- **ComputerEase: NO.** Change orders exist and are linked to job costing, but there is **no claims,
  entitlement or notice capability** on the product page. It is a small/mid-contractor accounting-first ERP.
- **Acumen: PARTIAL, and the strongest schedule-forensics asset in this whole competitive set.** This is the
  one product across InEight/CMiC/Deltek that speaks the language of the thesis. Flagging explicitly:

> **`FLAG FOR THE SCHEDULE AGENT — Deltek Acumen Fuse / Risk / Touchstone`**
> - **Acumen Fuse**: "a schedule diagnostics and **forensics** solution," 600+ industry-aligned metrics
>   (DCMA, DOE, GAO, NASA, AACE). **"Forensic Schedule Comparison"** reveals "exactly what changed between
>   schedule versions." **"Half-step delay analysis"** to "separate progress from scope changes to
>   **accurately attribute delays**." Produces "**audit-ready evidence that stands up to reviews, claims,
>   and compliance audits**." Integrates with Primavera P6 and Microsoft Project. Supports IPMDAR SPD/CPD.
> - **Acumen Risk / 360**: Monte Carlo quantitative risk modelling; models acceleration and recovery
>   scenarios to find "the fastest viable path to completion."
> - **Acumen Touchstone**: automated schedule submittal portal that scores incoming schedules and returns
>   instant feedback; "governed audit trails and version-controlled acceptance histories to support IBRs,
>   PMRs, and audits."
> - This is a genuine, marketed **delay-attribution and claims-evidence** capability. It is *schedule-only*
>   (no contract, no correspondence, no entitlement matching, no dollarisation of a claim), and it is a
>   planner/expert tool rather than a contract-administrator tool — but on dimensions 11 (delay_detection),
>   18 (schedule_impact_analysis) and 26 (consultant_replacement_potential) Acumen is the incumbent to beat.

URLs:
- https://www.deltek.com/en/construction
- https://www.deltek.com/en/products/erp/computerease
- https://www.deltek.com/en/products/project-and-portfolio-management/acumen
- https://www.deltek.com/en/products/project-and-portfolio-management/acumen/fuse
- Deltek Costpoint and Deltek Open Plan are named InEight integrations: https://ineight.com/resources/integrations/

---
---

# ANSWERS TO THE THREE KEY QUESTIONS

### Q1. Does InEight Change + Document already constitute the full thesis pipeline for heavy civil?

**No — but it constitutes the entire *substrate* of the pipeline, which is more dangerous than it sounds.**

Map the hypothesis onto what exists:

| Pipeline stage | InEight today |
|---|---|
| Contract + RFIs + daily reports + emails + schedules + minutes + photos | **✅ All present, structured, one tenancy.** Mail register with threads, RFIs, daily logs, geofenced photos, timesheets, P6-synced CPM, contract SOV. |
| → commercial **event detection** | **❌ Absent.** A human raises an Issue. Nothing reads the mail or the daily log and says "that's compensable." |
| → **entitlement / notice matching** | **❌ Absent.** No clause layer exists in any module. The only notice artefact is a manual date field. |
| → **evidence collection** | **⚠️ Half.** The graph exists (threads auto-built, mail→Change issue creation, Supporting Documents tab) but every meaningful link is drawn by hand, at the moment someone remembers. Nothing retro-assembles. |
| → **recoverable-value estimate** | **⚠️ Half.** Change prices the *scope* of a change off the live estimate with ROM and markups. It does not price prolongation, disruption, acceleration or loss of productivity. |
| → **notice / claim package** | **⚠️ Quarter.** "Generate Change document" from a CCO produces a change-order pack. Not a claim submission. |

So: **stages 1, 3 and 5 are partly built; stages 2 and 4 — the two that create the value — are entirely
absent, and stage 2 (entitlement matching) is architecturally blocked because no clause object exists
anywhere in the platform.**

The honest threat is different from "they already do it." It is: **the pain may be smaller in the InEight base
than the thesis assumes**, because InEight customers already have a disciplined, auditable, threaded,
timestamped record. Mega-project heavy civil is the *best-instrumented* corner of construction. The pipeline
matters most where records are worst.

### Q2. Does incumbent strength in heavy civil push the wedge toward commercial building / mid-market?

**Yes — and the evidence for that is stronger than the evidence against InEight.**

Three reasons, all evidenced above:

1. **Record quality is inversely correlated with the wedge.** InEight (heavy civil), Aconex (owner-mandated
   mega-programmes) and Acumen (federal/CPM-mature) mean the top of the market already has: an immutable-ish
   correspondence register, response-period tracking, thread graphs, forensic schedule tooling, and — usually —
   a dedicated contracts team and a retained claims consultant. In commercial building and mid-market, the
   equivalent record is Outlook, a shared drive, Procore RFIs and a superintendent's daily log. That is where
   evidence fragmentation is real and where an ingestion-first product has something to do.

2. **Procurement physics.** Every incumbent here sells enterprise, services-attached, weeks-to-months
   implementation, custom-quoted, multi-year. InEight's own pricing page: "starts with an in-depth
   conversation." A solo founder cannot win a heavy-civil mega-project account. But InEight's own NOW launch
   (Jan 2025, self-serve, $52-$260/user/month) proves the vendor itself believes there's an underserved
   segment below its enterprise motion — and Change and Contract are conspicuously **not** in the NOW
   line-up.

3. **The buyer exists lower down.** Mid-market GCs and specialty subs lose entitlement to time-bars because
   nobody is watching, and they cannot afford a claims consultant to chase a $180k variation. That is the
   "proven, paid-for pain" test the brief demands — though **this report did not verify that pain**; it only
   establishes that the incumbents don't serve it.

Caveat to hold: heavy civil is where the *dollars per claim* are largest and where entitlement is most
formalised (NEC/FIDIC/AS4000 notice regimes with hard time-bars). The right synthesis is probably: **wedge in
mid-market/commercial building where records are bad and procurement is fast; sell the same engine upmarket
later as a layer beside InEight/Aconex, not against them.**

### Q3. Partner, channel, or roadkill?

**PARTNER** (with real acquisition-target upside). Not channel — no marketplace, no app store, no
self-serve listing motion exists. Not roadkill — the gap is protected by a structural conflict (Kiewit
ownership makes contractor-partisan entitlement software a board problem, not a roadmap problem), by a
missing competency (zero LLM/document-AI product surface as of Aug 2026, and the last real AI shipped in
2020), and by a legal-exposure posture their own marketing telegraphs ("reduce disputes," never "win
disputes").

The practical route in: **project archives + email forward**, both of which InEight hands over without any
partnership (ZIP archive with all mail, all revisions, transmittals and links; email-In already normalises
external correspondence into a register). That satisfies the solo-founder V1 constraint exactly. Formal
API integration via APIM comes later, once there's a customer asking for it.
