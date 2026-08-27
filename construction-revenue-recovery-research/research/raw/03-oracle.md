# 03 — ORACLE CONSTRUCTION & ENGINEERING STACK
### Aconex · Unifier · Primavera P6 EPPM · Primavera Cloud (OPC) · Textura · Construction Intelligence Cloud · Smart Construction Platform

Research date: 2026-08-19. All claims URL-cited. `UNVERIFIED` used where I could not confirm.
Note on method: web-search quota was exhausted partway through; the back half of this research is
direct-fetch against Oracle documentation, Oracle help sites, Oracle press releases, the UK Government
Digital Marketplace, and review aggregators. Where a fact rests on a secondary source I say so.

---

## 1. SNAPSHOT

**What it is.** Oracle Construction and Engineering (OCE, part of "Oracle Infrastructure Industries") is a
portfolio of ten named products, assembled largely by acquisition, marketed as the "Oracle Smart
Construction Platform." Named products on the division landing page:
Oracle Aconex, Oracle Primavera Cloud, Primavera Unifier, Oracle Construction and Engineering Intelligence,
Oracle Textura Payment Management, Oracle Primavera Cloud Portfolio and Capital Planning, Oracle Aconex for
Defense, Primavera P6 EPPM, Primavera Submittal Exchange, Oracle Primavera Portfolio Management (OPPM).
— https://www.oracle.com/construction-engineering/

**Division-level scale claims (Oracle's own, current page):**
- "More than $9T in project value managed"
- "More than 4M projects and initiatives managed"
- "More than 1.8B documents exchanged"
- "Nearly $20B in subcontractor payments processed monthly"
— https://www.oracle.com/construction-engineering/

**Ownership / how it was assembled.**
- **Aconex**: acquired by Oracle, announced 17 Dec 2017, A$7.80/share ≈ **US$1.2B** net of cash. At
  acquisition Aconex was described as "used in over $1 trillion in projects," "70,000 user organizations,"
  "over 70 countries." — https://www.oracle.com/corporate/pressrelease/oracle-buys-aconex-121717.html
- **Textura**: acquired 2016 (price not stated on the Oracle product page I could reach;
  the widely-reported ~$663M figure is `UNVERIFIED` from an Oracle-owned source).
  — https://www.oracle.com/corporate/acquisitions/textura/
- **Primavera**: acquired 2008. **Skire (→ Unifier/uDesigner)**: acquired 2012. Both pre-date my
  citation window; treat as background.

**A 2020 Aconex datasheet still in Oracle's CDN claims** (flagged: source is older than 2023):
> "With more than 6 million users and more than US$1 trillion of project value delivered in 70 countries,
> it is the industry's most widely adopted and trusted platform."
> "With more than 70,000 user organizations and more than $1 trillion of project value delivered in more
> than 70 countries…"
— https://www.oracle.com/a/ocom/docs/industries/construction-and-engineering/oracle-aconex-ds.pdf
(v1.01, © 2020; the file at this path is the *Aconex Project Controls Cloud Service* datasheet)

**ICP.** Asset **owners**, government/infrastructure agencies, and tier-1 contractors/EPCs on
**mega-projects**. Everything about the licensing confirms it: Unifier and P6 EPPM carry **25-user minimums**
(50 for UK Government editions), Aconex is sold "on a Project Value or Enterprise metric" for large projects,
and Unifier ships an NEC4 edition (NEC4 is the UK/infrastructure public-sector standard form).
— https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf

**Geography.** Confirmed hard: Aconex runs **regional instances AU1, MEA, KSA1, UK1, HK1, CN1, US1, EU1, CA1**.
The Australian instance is "AU1" (Aconex was founded in Melbourne), and there are *dedicated* Middle East
and **Saudi Arabia (KSA1)** instances — an unusual amount of infrastructure for a region unless the revenue
justifies it. — https://help.aconex.com/apis/cost-api-developer-guide/
Oracle's own OIC adapter documentation uses `https://au1.aconex.com` as the worked example.
— https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/aconex-adapter/create-aconex-connection.html
UK/Commonwealth skew is further evidenced by Oracle selling a **Unifier "with NEC4"** SKU and
**UK Government Cloud Service** editions of both P6 and Unifier.
US federal presence exists via **Oracle Aconex for Defense**. — https://www.oracle.com/construction-engineering/

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

### 2.1 Aconex — the correspondence + document system of record

This is the product that matters most to the thesis. Oracle's positioning is *explicitly* about disputes.

**Verbatim marketing claims (Oracle Aconex product page):**
- "unalterable audit trail that minimizes disputes"
- "Track and capture every project decision, ensuring accountability"
- "tracks and captures all documents, correspondence, and every project decision"
- **"Nothing can be deleted or edited"**
- provides "reliable evidence to help prevent or resolve disputes"
- "Complete, searchable project record that captures project information from design through construction,
  handover, and project closeout"
— https://www.oracle.com/construction-engineering/aconex/

**And, notably, from the datasheet — Oracle sells Aconex partly on litigation cost:**
> "The unique security model behind the Oracle Aconex platform ensures adoption, accurate insights, and
> **fewer resources spent on litigation**. There is no super user — meaning you own your own data.
> Information is private until shared, and the platform provides an unalterable audit trail."
— https://www.oracle.com/a/ocom/docs/industries/construction-and-engineering/oracle-aconex-ds.pdf (© 2020)

**Modules (from the product page + the official price list):**
| Module | Evidence |
|---|---|
| Document & drawing management, versioning | https://www.oracle.com/construction-engineering/aconex/ |
| Project **Mail** (correspondence) with configurable **Mail Types** | https://help.aconex.com/mail/create-mail/ |
| Review & approval **Workflows**; **Document Processes** | https://www.oracle.com/news/announcement/new-oracle-aconex-capabilities-improve-project-transparency-and-control-2026-04-13/ |
| **RFIs** (implemented as a Mail Type) | https://help.aconex.com/mail/create-mail/ |
| **Aconex Field** — issues, defects, punchlists, inspections (checklist + PDF form), **daily reports**, photos, offline mobile, QR location scan, event logs | https://help.aconex.com/aconex/our-main-application/using-aconex/field/ |
| **Aconex Connected Cost** — contracts, change events, budgets, forecasts, payment claims/applications, cost activity stream | https://help.aconex.com/cost/what-is-cost/ |
| **Test Plans (ITPs)** — new 2026, "exportable audit-ready documentation packages" | https://www.oracle.com/news/announcement/new-oracle-aconex-capabilities-improve-project-transparency-and-control-2026-04-13/ |
| Packages, Tenders, Supplier Documents, Handover, Model Coordination, Scheduled Archive | https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf |

**Does Aconex track notice deadlines / response-due dates on contractual correspondence? YES — natively.**
This is the single most thesis-relevant finding.
- Every Mail Type can carry a **"Response required"** field with a **"respond by" date**.
- A Project Admin can make Response Required **mandatory per Mail Type**: "When they select one of the
  options from the drop down list it **enforces a due date to be entered**… the mail cannot be sent without
  the fields being completed." Applies to "all Mail Types except Transmittals."
  — https://help.aconex.com/project-admins/making-response-required-mandatory-for-mail-types/
- Admins can set **default response times per Mail Type in days**, choosing **working days (per the project
  working week) or calendar days** — so due dates are auto-calculated rather than hand-typed.
  — https://help.aconex.com/project-admins/setting-up-default-response-times-for-your-mail/
- Recipient-level status: **Outstanding** until responded, flipping automatically to **Overdue** past the
  date. CC recipients show N/A. — https://help.aconex.com/mail/create-mail/
- Sent mail can be **closed out** for "more accurate reporting."
  — https://help.aconex.com/en/aconex/our-main-application/using-aconex/using-project-mail

**Does Aconex template notices? Partially.**
- **Mail templates** exist (listed in the Mail user guide under "creating templates") and **"auto text"**
  lets a user insert predefined repeatable body content.
- **No** contract-clause referencing, **no** clause-aware auto-population, **no** notice-drafting logic.
— https://help.aconex.com/mail/create-mail/ ; https://help.aconex.com/en/aconex/our-main-application/using-aconex/using-project-mail

**The structural caveat that everyone misses:** Aconex's trust model is *deliberately* one of
information asymmetry. "There is **no super user** — meaning you own your own data. **Information is private
until shared**, and the platform provides an unalterable audit trail." Each organisation on an Aconex project
sees only what it sent, received, or was shared. **No single party holds the complete project record.**
— https://www.oracle.com/a/ocom/docs/industries/construction-and-engineering/oracle-aconex-ds.pdf

### 2.2 Unifier — configurable business-process / cost / contract engine

- **Cost controls**: forecasting, budgeting, cash flow, multi-level funding sources, schedule-based cash flow.
- **Change management**: "Connected change order processing with automatic cost/schedule impact visibility";
  approval workflows; contracts and commitments update on approval.
- **Contract management**: enterprise + project level, **NEC4 and FIDIC** methodologies, schedule of values,
  retention, DocuSign / Adobe Acrobat Sign e-signature.
- **Document management**: Bluebeam markup integration, attachments inside business processes.
- **BPA**: form-based workflow engine, dynamic routing, event-driven processes via OCI Integration, mobile offline.
- **uDesigner**: no-code business-process designer; "Over 125 preconfigured processes in Unifier Accelerator";
  unlimited custom processes. Claims "12 languages, 183 currencies, and unlimited exchange rates."
— https://www.oracle.com/construction-engineering/primavera-unifier-project-controls-asset-management/

**NEC4 is the closest thing Oracle has to a notice-and-entitlement product.** Oracle ships and separately
prices a **Unifier NEC4** edition with four role-specific guides (NEC4 Administrator, Project Manager,
Supervisor, Contractor). The Project Manager guide explicitly covers **submitting Notifications**, creating
and replying to **Instructions**, creating and replying to **Compensation Events**, and a **Pain/Gain
calculator**. NEC4 compensation events carry hard time-bars, so this *is* a contractual-notice workflow
product — but it is form-and-workflow, not detection.
— https://docs.oracle.com/en/industries/construction-engineering/primavera-unifier/26/nec4.html
— https://docs.oracle.com/pls/topic/lookup?ctx=en/industries/construction-engineering/primavera-unifier/26&id=UNECP-GUID-B143AB5F-33B1-4C92-8426-A679256FF067

**How configurable / how much services?** uDesigner is marketed as no-code, and the Accelerator ships 125+
processes. But reviewers describe the reality differently — see §9. Notably, Unifier requires
**AutoVue 2D or 3D as a licensed pre-requisite**, and "Number of users needs to match the Unifier users" —
i.e. a mandatory second licence line per seat.
— https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf

### 2.3 Primavera P6 EPPM / Primavera Cloud — the delay-analysis substrate

- P6 EPPM is the schedule of record for large capital projects. **XER** is its native export.
- Oracle publishes **public, official XER field-mapping documentation**: three separate guides —
  *XER Project*, *XER Resource*, *XER Role* import/export data maps — plus MS Project MPX and XML, XLSX,
  UN/CEFACT, **IPMDAR**, **Contractor Project Performance (CPP)**, and Unifier Schedule Sheet maps.
  — https://docs.oracle.com/cd/G48897_01/102093.htm
  — https://docs.oracle.com/cd/G48897_01/English/Mapping_and_Schema/xer_import_export_data_map_project/index.htm
- **Who consumes XER files?** Everyone downstream of the scheduler: owners' project-controls teams,
  delay/forensic analysts, and a visible cottage industry of third-party XER tools —
  XER Schedule Toolkit (https://xertoolkit.com/), Schedule Auditor (https://www.scheduleauditor.org/about),
  ScheduleLens (https://schedulelens.com/blog/xer-file-analysis/). Their existence is the proof that
  XER-in-isolation is a viable product surface: these tools read XER without touching P6 at all.
  Forensic practice is explicitly built on XER snapshots — training courses teach
  "as-planned vs as-built, impacted as-planned, and collapsed as-built" using P6.
  — https://www.rpc.uk.com/training/project-controls-skills/using-primavera-p6-for-schedule-forensic-delay-analysis

### 2.4 Textura — payment, compliance, lien waivers

- Automated subcontractor pay-app workflow, e-signed lien waivers (prime and sub-tier), **automated payment
  holds for lien-waiver or compliance deficiencies**, ACH payments, ERP integration, portfolio dashboards,
  optional **Payment Accelerator**.
- Case study: Austin Commercial "accelerated pay application processing by over 50%," payment cycles from
  5+ days to 2 days; pay-app prep from 4–5 days to 1–2 days.
— https://www.oracle.com/construction-engineering/textura-construction-payment-management/datasheet/
— https://www.oracle.com/construction-engineering/textura-construction-payment-management/
Division-level: "Nearly $20B in subcontractor payments processed monthly."
— https://www.oracle.com/construction-engineering/

### 2.5 Construction and Engineering Intelligence (CIC) + AI

- **Analytics**: managed ETL and "prebuilt data pipelines to Oracle Applications, such as Primavera P6 EPPM,
  Unifier, Aconex, and Primavera Cloud"; dashboards; "Ask natural language questions to uncover insights";
  "AI summarizes the selected fields to explain the insights generated."
- **Advisor for Safety**: "weekly risk forecasts predict where and when safety incidents are most likely to
  occur"; models "trained on decades of construction project data"; consumes safety observations, incidents,
  workforce, schedule, documents, weather.
- **Explicit gap**: the page does **not** address claims management, change-order entitlement, or delay
  analysis. Oracle's only shipped predictive AI in this stack is aimed at **safety**, not commercial risk.
— https://www.oracle.com/construction-engineering/intelligence/
- CIC is **"under controlled availability"** per Oracle's own reseller price list — i.e. not generally sold.
— https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf

### 2.6 What Oracle shipped most recently (13 Apr 2026)

New Aconex capabilities: collaborative **Document Process** review with integrated comment management, an
**automated Review Matrix** that starts approval flows from document metadata, **built-in audit trail for
unalterable review records**, a new **Observation** capability, and structured **Test Plans (ITP)** with
"exportable audit-ready documentation packages" and evidence attachment on site.
Mark Webster, SVP/GM Oracle Infrastructure Industries: *"The new Oracle Aconex enhancements help
organizations collaborate with confidence, knowing the project system is tracking all material changes for
improved traceability and control across the full lifecycle of a project."*
— https://www.oracle.com/news/announcement/new-oracle-aconex-capabilities-improve-project-transparency-and-control-2026-04-13/

**Read that quote carefully.** In April 2026 Oracle's flagship construction release was: better review
routing, better ITP evidence capture, better audit trail. Not entitlement. Not claims. Not notices.
Oracle is doubling down on *record integrity*, not on *record interpretation*.

---

## 3. CAPABILITY MATRIX (0–3), whole Oracle C&E stack

| # | Dimension | Score | Justification + URL |
|---|---|---|---|
| 1 | contract_ingestion | **2** | Structured contract objects exist (Connected Cost contracts w/ pay items; Unifier contract mgmt w/ NEC4/FIDIC, SOV, retention) and contract PDFs live in the doc register — but records are keyed in, not parsed from the document. https://help.aconex.com/cost/introduction-to-contracts-in-cost/ ; https://www.oracle.com/construction-engineering/primavera-unifier-project-controls-asset-management/ |
| 2 | clause_extraction | **0** | No clause extraction/NLP anywhere in the stack. Oracle's only shipped predictive AI is Advisor for **Safety**. https://www.oracle.com/construction-engineering/intelligence/ |
| 3 | notice_detection | **1** | Nothing detects that a notice is *due*. Marginal credit only because Unifier NEC4 provides structured Notification/Compensation-Event forms that a human initiates. https://docs.oracle.com/en/industries/construction-engineering/primavera-unifier/26/nec4.html |
| 4 | deadline_tracking | **3** | Best-in-class and native: mandatory per-Mail-Type "Response required", auto due dates in working or calendar days, automatic Outstanding→Overdue status per recipient. https://help.aconex.com/project-admins/making-response-required-mandatory-for-mail-types/ ; https://help.aconex.com/project-admins/setting-up-default-response-times-for-your-mail/ |
| 5 | rfi_event_ingestion | **3** | RFIs are a first-class Mail Type; Unifier has RFI business processes; Field issues feed the record. https://help.aconex.com/mail/create-mail/ |
| 6 | email_ingestion | **2** | Email replies to Aconex notifications are captured back into the record with the "Email" mail type, and an "Aconex for Outlook" tool exists — but no mailbox-level ingestion is documented. https://help.aconex.com/mail/configure-your-email-notifications/ |
| 7 | daily_report_ingestion | **2** | Aconex Field covers punchlists and **daily reports** with photos and offline capture, but it is a separately licensed module and mobile is a known weak spot. https://help.aconex.com/aconex/our-main-application/using-aconex/field/ |
| 8 | schedule_integration | **3** | P6 and OPC are Oracle's own; Connected Cost advertises "one-click integration with Oracle Primavera P6 and Oracle Primavera Cloud"; Unifier↔P6↔OPC recipes ship prebuilt. https://www.oracle.com/a/ocom/docs/industries/construction-and-engineering/oracle-aconex-ds.pdf ; https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/integration-documentation.html |
| 9 | change_order_workflow | **3** | Connected Cost change-event wizard (downstream/upstream contracts, cost + budget estimates, markup, ETC drawdown); Unifier "connected change order processing." https://help.aconex.com/cost/change-event-wizard/ |
| 10 | claim_identification | **0** | Nothing in the stack identifies that a claim/entitlement exists. Division landing page contains no claims or disputes language at all. https://www.oracle.com/construction-engineering/ |
| 11 | delay_detection | **2** | P6 gives baselines, longest path, variance and baseline comparison — the substrate for delay analysis — but detection/attribution is done by humans and third-party XER tools. https://docs.oracle.com/cd/G48897_01/102093.htm ; https://xertoolkit.com/our-features/schedule-comparison/ |
| 12 | responsibility_attribution | **1** | The audit trail attributes *actions to users and organisations* ("who performed each action, when it occurred"). That is authorship, not causation. https://www.oracle.com/construction-engineering/aconex/ |
| 13 | contemporaneous_evidence_graph | **2** | Strongest partial in the stack: unalterable record, versioned docs, mail attaching documents and other mail, Field records linking to Mail/Documents/Packages, and a **Related Items API** with GET/POST/DELETE on document relationships. But there is no semantic entity graph, no cross-product linkage to P6 activities or Unifier cost records, and no party sees the whole project. https://help.aconex.com/apis/related-items-api-developer-guide/ ; https://help.aconex.com/aconex/our-main-application/using-aconex/field/ |
| 14 | evidence_completeness | **1** | New Test Plans produce "exportable audit-ready documentation packages" for ITPs only. No notion of whether a *claim's* evidence is complete. https://www.oracle.com/news/announcement/new-oracle-aconex-capabilities-improve-project-transparency-and-control-2026-04-13/ |
| 15 | recoverable_dollar_estimation | **1** | Connected Cost captures user-entered cost estimates per change event and rolls into ETC/forecast; nothing estimates *recoverable* value or entitlement probability. https://help.aconex.com/cost/change-event-wizard/ |
| 16 | claim_package_generation | **1** | Export exists (search results, mail register, Field PDF/Excel/CSV, project archive/handover, ITP packs). No claim narrative, no chronology assembly, no submission pack. https://help.aconex.com/aconex/our-main-application/using-aconex/field/ |
| 17 | notice_drafting | **2** | Mail templates + "auto text" prefill, plus NEC4 structured notification/instruction/compensation-event forms. Forms and boilerplate, not drafting. https://help.aconex.com/mail/create-mail/ ; https://docs.oracle.com/en/industries/construction-engineering/primavera-unifier/26/nec4.html |
| 18 | schedule_impact_analysis | **2** | P6 supports baselines, what-if and scheduling; Unifier claims "automatic cost/schedule impact visibility" on change orders. Fragnet/TIA remains manual expert work. https://www.oracle.com/construction-engineering/primavera-unifier-project-controls-asset-management/ |
| 19 | procore_integration | **1** | Oracle's Smart Construction Platform integration catalogue lists **no Procore connector**. Any link is third-party/DIY. https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/integration-documentation.html |
| 20 | autodesk_integration | **2** | Oracle publishes Aconex plug-ins for **Revit, Navisworks and Solibri** (model coordination). No ACC/BIM 360 data exchange in the catalogue. https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/integration-documentation.html |
| 21 | outlook_gmail_integration | **2** | "Aconex for Outlook" tool exists; Outlook replies register in Aconex as "Email" mail type. Gmail: nothing found. https://help.aconex.com/mail/configure-your-email-notifications/ |
| 22 | mobile_workflow | **2** | Oracle Aconex Mobile does offline issue capture with auto-sync; Unifier has mobile offline. But reviewers: "Mobile access is bad." https://help.aconex.com/aconex/our-main-application/using-aconex/field/ ; https://www.capterra.com/p/220249/Oracle-Aconex/reviews/ |
| 23 | audit_trail | **3** | The defining feature. "Nothing can be deleted or edited"; records who/when/how-related; marketed as an "unalterable audit trail that minimizes disputes." https://www.oracle.com/construction-engineering/aconex/ |
| 24 | portfolio_risk | **2** | CIC Analytics + Advisor for Safety + OPC Portfolio & Capital Planning give portfolio visibility and *safety* risk forecasting — no commercial/claims risk. And CIC is "under controlled availability." https://www.oracle.com/construction-engineering/intelligence/ |
| 25 | performance_pricing_compatibility | **1** | Aconex is sold on a **Project Value** metric, so Oracle is comfortable with value-linked pricing — but everything is a fixed subscription; no outcome/success-fee construct exists. https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf |
| 26 | consultant_replacement_potential | **1** | Oracle's stack *creates* consultant demand — uDesigner configuration partners, implementation SIs, delay analysts consuming XER. It replaces no claims consultant. https://www.psgincs.com/product-solutions/oracle-primavera-software/primavera-unifier/ |

`SCORES| 2,0,1,3,3,2,2,3,3,0,2,1,2,1,1,1,2,2,1,2,2,2,3,2,1,1`

---

## 4. PRICING — with real numbers

### 4.1 Official reseller list price (HIGH confidence)
Source: **"Oracle Primavera Pricing — G-Cloud 14," Document Reference BD.G14.OCS.002, Version 1.1, dated
May 2025**, published on the UK Government Digital Marketplace by Oracle reseller **TRC Companies Ltd**
(service ID 423103118187025).
- PDF: https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf
- Listing: https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/423103118187025

**Aconex (Enterprise base services), per hosted named user per month, min 5 users:**
| SKU | £/user/mo |
|---|---|
| Oracle Aconex Enterprise Cloud Service | **46** |
| Aconex **Connected Cost** Enterprise | **280** |
| Aconex **Contract Management** (Single Project, for Enterprise) | **176** |
| Aconex **Field** (Single Project, for Enterprise) | **52** |
| Aconex Model Coordination | 9 |
| Aconex Handover | 8 |
| Aconex Packages | 8 |
| Aconex Tenders | 7 |
| Aconex Supplier Documents | 7 |
| Aconex Scheduled Archive | 4 |
| Aconex Model Coordination Early Access | 639 per customer (flat) |

**Primavera P6 EPPM:** £220/hosted named user/month, **min 25 users**.
P6 Progress Reporter £24. **P6 EPPM *Web Services* Cloud Service £36/user/month** (see §5 — this is the API tax).
UK Government edition: £439/user/month, min 50; additional non-production environment £7,188/month.

**Primavera Unifier:** Project Controls £132/user/month, min 25. **With NEC4: £180/user/month, min 25.**
Essentials for Building Owners £80. Facilities & Real Estate Mgmt £132. Earned Value Mgmt add-on £44.
**Team for External Collaborators £44/user/month (min 10); with NEC4 £56.** Portal User £2 (min 100).
Mandatory pre-req: AutoVue 2D £12 or AutoVue 3D Professional Advanced £44, user count must match Unifier users.
UK Government edition £459 (min 50); with NEC4 £539; non-production environment £7,188/month.

**Oracle Primavera Cloud:** Schedule £96/user/month (min 5); Task Management £44; Progress £10;
Portfolio & Capital Planning £176 (min 5).

**Construction Intelligence Cloud:** Analytics £40/user/month (min 10), **plus £799/month per data-source
connector** — separately for Aconex, Primavera Cloud, P6 EPPM SaaS, and Unifier. "Under controlled availability."

**Volume discounts (all products):** 10% at 101–200 users, 15% at 201–500, 20% at 501–1,000, 25% at 1,001+.

**Critical licensing note in the same document:** "All Cloud Service pricing is based on the assumption that
services will be **non-cancellable** during the term of any Call-Off Contract."

**Alternative metric:** "Aconex is also available on a **Project Value** or Enterprise metric. These are
priced per requirement." Same for Primavera Cloud. This is the mega-project motion.

### 4.2 Secondary / lower-confidence estimates
- ITQlick (analyst estimate, not verified contracts, page dated Jun 2026): Aconex "starts at $3,000 per
  user/year"; ~$15k/yr for 10 users; $100k+/yr at 100 users; implementation/customisation/training/migration
  "$5,000 to $50,000" additional; 5-year TCO for a large enterprise project ~$600,000 vs Procore ~$500,000.
  Treat as directional only. — https://www.itqlick.com/oracle-aconex/pricing
- Capterra lists Primavera Unifier starting at **$100 per user/month**. — https://www.capterra.com/p/181519/Oracle-Primavera-Unifier/
- Redress Compliance (Oracle licensing advisory, secondary): Unifier perpetual list ~$10,450/user with 22%
  support; P6 EPPM historical ~$2,750/user + $605 support; **Aconex is subscription-only, priced on a
  Project Value Allowance (PVA) basis, and any increase in project value triggers a new order**; "Guest
  users are explicitly considered Hosted Named Users."
  — https://redresscompliance.com/oracle-primavera-unifier-aconex-licensing-2026

**Sales motion.** Enterprise, owner-led, long procurement. Evidence: 25–50 user minimums, non-cancellable
terms, "controlled availability" SKUs requiring you to "contact Oracle or an authorized Partner," a
Project-Value metric that requires a new order when the project grows, and an entire third-party licensing-
advisory industry (Redress Compliance et al.) built around Oracle construction audits.

---

## 5. INTEGRATIONS & API — data egress reality

### 5.1 What is open
**Aconex REST APIs** are real, documented, and reasonably broad. Modules covered: **Mail, Documents,
Projects, Workflows, Cost, Directory, Tasks/Test Plans, Packages, Package Reviews, Field, Lobby, Models,
Supplier Documents, Document Processes, Related Items, User Role, Project Fields.**
— https://help.aconex.com/aconex/aconex-apis/
- Auth: **OAuth 2.0** (recommended) or Basic Auth. "Basic Auth will be retired in early 2027" —
  "Towards the beginning of 2027 we're planning to retire all Integration IDs."
  — https://help.aconex.com/apis/getting-started-with-apis/ ; https://help.aconex.com/api-news/api-news-may-2026/
- **New (May 2026): Mail Search API** — `POST /api/projects/{projectid}/mail/search` "allows retrieving mail
  data with project fields in a single call." This is materially useful for the thesis.
  — https://help.aconex.com/api-news/api-news-may-2026/
- **Documents API**: project-wide search using **Lucene query syntax**, filter on document type, status,
  discipline, dates, attributes and custom fields; PAGED / NUMBER_LIMITED (default 250, max 500) / COUNT_ONLY.
  — https://help.aconex.com/apis/api-guide-documents/
- **Related Items API**: Transactions/Activity (GET) plus Document Relationships (**GET/POST/DELETE**) —
  you can read *and write* the relationship graph. — https://help.aconex.com/apis/related-items-api-developer-guide/
- **Projects API** exposes project id/name/code, type, **value**, dates, status, addresses, owner org, and
  **ProjectResponsibilities** (Client, Contractor, Architect, Engineers).
  — https://help.aconex.com/apis/api-guide-project/
- **Cost API**: per-region Swagger (au1, mea, ksa1, uk1, hk1, cn1, us1, eu1, ca1); May 2026 added filtering
  contract changes by status and attachment file sizes. — https://help.aconex.com/apis/cost-api-developer-guide/
- **P6 EPPM REST API (v26)** is broad and read-write: Activity, Project, WBS (via copyWBS), **Relationship,
  BaselineProject, BaselineType**, ResourceAssignment, ActivityCode/Note/Comment/Step/Expense, EPS, OBS,
  Calendar, UDFValue, Document, Job. — https://docs.oracle.com/en/industries/construction-engineering/primavera-p6-project/26/rest-api/rest-endpoints.html
- **P6 XER field mappings are publicly documented by Oracle** (XER Project / Resource / Role data maps),
  alongside XLSX, MS Project XML/MPX, IPMDAR, CPP and UN/CEFACT. — https://docs.oracle.com/cd/G48897_01/102093.htm
- **Unifier**: an SOAP-era *Integration Interface Guide* plus a **read-only REST "Data Service"** for
  transactional data. — https://docs.oracle.com/en/industries/construction-engineering/primavera-unifier/26/integration.html
- **Oracle Integration adapters** ship for Primavera Cloud, P6 EPPM, Unifier, Aconex, and Primavera Cloud
  Data Service; plug-ins for Navisworks/Solibri/Revit; a Zapier plug-in for Primavera Cloud.
  — https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/integration-documentation.html

### 5.2 What is closed / the friction that actually matters
1. **Registration gate.** "All integrations with Aconex must be registered." And the killer clause for a
   solo founder: *"If you intend to build an integration with Oracle Aconex that you will make commercially
   available for one or more Customers, you must join the Oracle PartnerNetwork (OPN) and become an Oracle
   Technology Partner."* Partners "must … complete their testing in the Early Access (EA) environment before
   publishing to production." — https://help.aconex.com/apis/getting-started-with-apis/
   *Workaround that exists today:* for a bespoke integration for one customer, "that customer should handle
   registration." So a design-partner-led V1 is legal without OPN. Scaling it is not.
2. **No bulk file download.** Verbatim: *"Due to the URL structure, the service can only retrieve one backing
   file at a time. Unlike the GUI, the service cannot retrieve multiple backing files in a single request."*
   Rebuilding a project's evidence corpus means N sequential HTTP calls. — https://help.aconex.com/apis/api-guide-documents/
3. **Throttling.** Concurrency and frequency limits enforced with HTTP 503
   `CONCURRENCY_THROTTLE_LIMIT_REACHED` / `MAX_FREQUENCY_THROTTLE_LIMIT_REACHED`; Oracle publishes no numbers.
   — https://help.aconex.com/apis/getting-started-with-apis/
4. **The P6 API tax.** Oracle's own price list states: *"For the purposes of the following programs:
   Primavera P6 EPPM Cloud Service and Primavera P6 EPPM Web Services Cloud Service, developers and/or users
   (i) who are not already licensed for the P6 EPPM Cloud Service program and (ii) who access applications,
   must be licensed for the P6 EPPM Web Services Cloud Service program."* £36/user/month.
   Programmatic access to P6 is a **paid, separately licensed** privilege.
   — https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf
   A licensing advisory adds that Oracle's Peripheral Access Program can create indirect-use liability for
   downstream consumers of P6 data (secondary source, treat with care).
   — https://redresscompliance.com/oracle-primavera-unifier-aconex-licensing-2026
5. **Per-connector data tax.** Even Oracle's own analytics product charges **£799/month per data source**
   to read Aconex, P6, Unifier or OPC. Oracle prices data egress into its *own* BI tool.
6. **Visibility ceiling.** The Projects API "retrieves the list of projects that the authorizing user has
   access to." Combined with "information is private until shared," an integration inherits one
   organisation's partial view — never the project's whole record.
7. **No Procore connector, no Autodesk Construction Cloud connector, no SAP connector** in Oracle's own
   integration catalogue. Oracle's integration story is Oracle-to-Oracle.
   — https://docs.oracle.com/en/industries/construction-engineering/smart-construction-platform/integration-documentation.html

**Marketplace presence:** Oracle's construction integration surface is a documentation page, not an app
store. There is no Aconex/Primavera app marketplace comparable to Procore's or Autodesk's. A startup gets no
discovery channel from Oracle.

---

## 6. WEAKNESSES AND EXPLICIT GAPS — deliberate or unattended?

| Gap | Deliberate or unattended? | Reasoning |
|---|---|---|
| No claim identification / entitlement matching | **DELIBERATE** | Aconex's entire trust proposition is neutrality: "There is no super user"; "Information is private until shared." A product that told the contractor "you have a claim against the owner" would break the neutrality that gets Aconex mandated by owners in the first place. Oracle sells *to owners*. |
| No clause extraction | **UNATTENDED but low-priority** | Oracle has the AI muscle; it chose to point it at safety. Advisor for Safety exists; no Advisor for Commercial exists. |
| No recoverable-value estimation / claim package | **DELIBERATE** | Legal exposure. Oracle's own datasheet disclaims: *"We specifically disclaim any liability with respect to this document, and no contractual obligations are formed."* A quantum opinion is a professional service with liability attached; Oracle does not sell professional opinions. |
| No cross-product evidence graph (Aconex mail ↔ P6 activity ↔ Unifier cost record) | **UNATTENDED — and this is the real opening** | Oracle sells the connectors as *sync* recipes and charges £799/month/source to get the data into its own BI. Ten years post-Primavera and nine post-Aconex there is still no unified project entity model. |
| Mid-market ($5M–$500M projects) | **DELIBERATE** | 25-user minimums on P6/Unifier, Project-Value licensing on Aconex, non-cancellable terms, "controlled availability" SKUs, and a partner-led implementation motion all price the mid-market out structurally. |
| Usability / mobile | **UNATTENDED** | Persistent across a decade of reviews (§9). Oracle's own competing datasheet even attacks "incumbent products [that] are disconnected, provide a poor user experience, are costly and time consuming to deploy" — an unintentionally accurate self-description of P6/Unifier. |
| No Procore/Autodesk/SAP connectors | **DELIBERATE** | Oracle wants the whole stack. |
| Bulk egress friction | **DELIBERATE** | Single-file-at-a-time download plus per-source BI connector fees plus a Web Services licence for P6 is a coherent posture, not an oversight. |

---

## 7. ADJACENCY TEST — how hard for Oracle to ship "event detection → entitlement matching → evidence → claim package"?

### Verdict: **HARD**

**Data access — EASY for them.** Oracle already holds the corpus: mail with response-required dates and
overdue flags, RFIs, documents with versions, Field issues and daily reports, change events with cost
estimates, contracts with SOVs, and the P6 baseline set. Nobody on earth has a better starting corpus for
this problem. This dimension is genuinely a 10/10 for Oracle.

**Org incentive — HARD.** Aconex's commercial value to Oracle is that *owners mandate it on their projects
and make the whole supply chain use it*. Neutrality is the product. The moment Aconex starts telling one
party that it has an entitlement against another, the owner who pays the bill has a reason to remove it.
This is not a technical constraint; it is the business model. The datasheet is explicit that the security
model produces "fewer resources spent on litigation" — Oracle's pitch is *dispute suppression*, and a claims
engine is *dispute production*.

**GTM motion — HARD.** Oracle sells 25-seat-minimum, non-cancellable, partner-implemented enterprise
subscriptions to owners with multi-quarter procurement. Claims work is episodic, contractor-side, urgent,
and often needs to start on a Tuesday. Oracle has no motion for that.

**Legal exposure appetite — HARD.** Producing a quantified entitlement position is adjacent to giving
professional advice. Oracle disclaims liability aggressively even on marketing collateral. It sells
"unalterable audit trail," which is a *factual* claim that is cheap to defend; "you are owed £4.2m," which is
an *opinion*, is not.

**Past M&A and shipping behaviour — MEDIUM-HARD.** Oracle *does* buy in this space (Primavera 2008,
Skire 2012, Textura 2016, Aconex 2017, Newmetrix ~2022). So an acquisition of a claims-analytics startup is
plausible. But shipping behaviour post-acquisition is slow: nine years after Aconex, the April 2026 flagship
release was review routing and ITP packs. The only AI shipped is a **safety** predictor. Oracle's revealed
preference over a decade is record integrity, never record interpretation.

**Where Oracle is closest, and it's worth respecting:** Unifier NEC4 already ships notification, instruction
and compensation-event workflows with role-based guides. If Oracle wanted to extend NEC4-style time-bar
enforcement into a general entitlement engine, the product primitives are there. It has not done so in the
years the module has existed, and it charges +£48/user/month for it, which suggests it is a compliance
checkbox for UK public infrastructure procurement rather than a strategic bet.

---

## 8. STARTUP POSTURE: **PARTNER (weak) — not CHANNEL, not ROADKILL**

**Not ROADKILL.** Oracle is structurally prevented from shipping the entitlement layer by the neutrality that
makes Aconex valuable, and its shipping cadence in this domain is glacial. There is no realistic path where
Oracle crushes a claims-intelligence startup in the next 3 years by shipping the feature.

**Not CHANNEL.** There is no Aconex/Primavera app marketplace to be listed in. Distribution runs through
Oracle sales and OPN partners, and OPN membership is a prerequisite for a *commercially available*
integration. Oracle does not do lightweight ISV co-sell in this vertical.

**PARTNER, but weakly and asymmetrically.** The realistic relationship is: the startup reads from Oracle and
gives Oracle customers more value from data they already pay Oracle to store. Oracle tolerates that. Practical
form: a customer-registered integration (the customer registers, per Oracle's own ISV guidance) pulling Mail
Search + Documents + Related Items, plus **XER upload for schedule**. Do not depend on Oracle for
distribution, do not build the whole product on Oracle-only data, and expect to be asked to join OPN once you
have more than a couple of Aconex customers.

**The real strategic read for a solo founder:** Oracle is *not* the competitor. Oracle is the **evidence
warehouse** and the reason contemporaneous records exist at all on the projects most worth working on.
The competitor is the claims consultant billing £250/hr to read that warehouse.

---

## 9. TOP 5 VERBATIM CUSTOMER COMPLAINTS RELEVANT TO THE THESIS

1. **"Platform is dated. Mobile access is bad. Web platform is not responsive"**
   — Joe V, Contracts Administrator, Construction, 10 Oct 2023, 3.0★.
   https://www.capterra.com/p/220249/Oracle-Aconex/reviews/
   *Relevance: the Contracts Administrator — the exact persona who runs notices and claims — rates the tool 3/5.*

2. **"user has to write the name of the document using exact letters… otherwise, it shows 'no results found'"**
   — Malek S, Architect, Architecture & Planning, 19 Jul 2022.
   https://www.capterra.com/p/220249/Oracle-Aconex/reviews/?page=2
   *Relevance: the "complete, searchable project record" is only searchable if you already know what you're
   looking for. That is precisely the failure mode a retrieval/RAG layer solves.*

3. **"Expensive License is the major drawback I see in this software"** and
   **"The cost of software is extremely high if compare to the local software"**
   — Malek S, Architect (19 Jul 2022); Marisa O, HR Manager, Hospitality (25 Dec 2021).
   https://www.capterra.com/p/220249/Oracle-Aconex/reviews/?page=2
   *Relevance: corroborates the mid-market exclusion.*

4. **"It is not simple to use, certainly for beginners, due to its complexity"** / **"A bit of programming
   required to truly unlock its full potential"** / requires "some knowledge in coding (ie. Java)"
   — Primavera Unifier reviewers, Capterra (4.4★, 13 reviews).
   https://www.capterra.com/p/181519/Oracle-Primavera-Unifier/
   *Relevance: "no-code uDesigner" is not experienced as no-code. Unifier is a consulting-services product.*

5. **"Using Aconex for review documents is a real pain."** and **"Some of the process can be long winded and
   require additional steps that are not normally with our companies procedures."**
   — Software Advice Aconex reviews (reviewer metadata not exposed on the page).
   https://www.softwareadvice.com/construction/aconex-profile/reviews/
   *Relevance: process rigidity is why records get created outside Aconex — in email, WhatsApp, and
   spreadsheets — which is exactly the fragmentation the thesis targets.*

Honourable mentions: **"steep learning curve for new users, and the interface may feel complex"** (Ansuman R,
5 Aug 2026, Capterra p2); **"Aconex is very slow with very limited tools"** (Capterra NZ,
https://www.capterra.co.nz/reviews/118711/oracle-aconex). Aconex sits at **4.4/5 across 216–217 Capterra
reviews** — genuinely liked, but liked as a *filing cabinet*.

---

## 10. HARDEST FACTS (5 strongest numeric facts)

1. **Aconex Enterprise Cloud Service lists at £46 per hosted named user per month (min 5); Aconex Connected
   Cost at £280; Aconex Contract Management (single project) £176; Aconex Field £52** — official Oracle
   reseller price list, G-Cloud 14, doc ref BD.G14.OCS.002 v1.1, May 2025.
   https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf

2. **P6 EPPM lists at £220/user/month with a 25-user minimum; Unifier Project Controls £132 (min 25), £180
   with NEC4; and API access to P6 requires a separately licensed "P6 EPPM Web Services Cloud Service" at
   £36/user/month** — same document. Programmatic access to the schedule of record is a paid SKU.

3. **Oracle Construction Intelligence charges £799 per month per data source connector** — separately for
   Aconex, Primavera Cloud, P6 EPPM SaaS and Unifier — on top of £40/user/month for Analytics. Oracle prices
   getting data out of its own products into its own BI tool. Same document.

4. **Oracle claims "$9T in project value managed," "4M projects," "1.8B documents exchanged," and "nearly
   $20B in subcontractor payments processed monthly."**
   https://www.oracle.com/construction-engineering/

5. **Oracle paid ≈US$1.2B for Aconex (A$7.80/share, announced 17 Dec 2017)**, then described it as covering
   "over $1 trillion in projects," "70,000 user organizations," "over 70 countries."
   https://www.oracle.com/corporate/pressrelease/oracle-buys-aconex-121717.html

Bonus hard fact worth carrying: the **Aconex Documents API cannot bulk-download**: *"the service can only
retrieve one backing file at a time. Unlike the GUI, the service cannot retrieve multiple backing files in a
single request."* https://help.aconex.com/apis/api-guide-documents/

---

## 11. KEY QUESTIONS — DIRECT ANSWERS

### Q1. Is Aconex already the "contemporaneous evidence graph" the thesis proposes to build?

**No — it is the evidence *warehouse*, not the evidence *graph*, and it is structurally incapable of being
the graph for any single party.** Four pieces of evidence:

**(a) It is genuinely an immutable, attributed, contemporaneous record — that part is real and should not be
underestimated.** "Nothing can be deleted or edited"; the trail records "who performed each action, when it
occurred, and how it relates to associated documents, correspondence, reviews, workflows, and approvals."
Mail carries mandatory response-required dates that auto-flip to Overdue. Field issues link to Mail,
Documents and Packages. A Related Items API exposes document relationships for read *and* write.
— https://www.oracle.com/construction-engineering/aconex/ ;
https://help.aconex.com/project-admins/making-response-required-mandatory-for-mail-types/ ;
https://help.aconex.com/apis/related-items-api-developer-guide/

**(b) But no party can see the whole record.** *"There is no super user — meaning you own your own data.
**Information is private until shared.**"* Each organisation's Aconex view is its own correspondence plus what
was shared with it. The Projects API returns only "projects that the authorizing user has access to."
The "complete project record" exists as a *union* across parties that no single party can query.
— https://www.oracle.com/a/ocom/docs/industries/construction-and-engineering/oracle-aconex-ds.pdf ;
https://help.aconex.com/apis/api-guide-project/

**(c) There is no semantic layer and no cross-product linkage.** Aconex mail does not link to a P6 activity.
A Connected Cost change event does not link to the RFI that caused it as a typed causal edge. There is no
entity for "delay event," "notice," "entitlement," or "clause." Search is Lucene keyword — and reviewers say
you must type the document name in "exact letters" or get "no results found."
— https://help.aconex.com/apis/api-guide-documents/ ; https://www.capterra.com/p/220249/Oracle-Aconex/reviews/?page=2

**(d) Oracle's own positioning is dispute *suppression*, not claim *construction*.** The marketed outcome is
"minimizes disputes," "fewer resources spent on litigation." Nothing in the stack scores a claim, quantifies
recovery, or assembles a package. The April 2026 flagship release was review routing and ITP evidence packs.
— https://www.oracle.com/construction-engineering/aconex/ ;
https://www.oracle.com/news/announcement/new-oracle-aconex-capabilities-improve-project-transparency-and-control-2026-04-13/

**The honest thesis-threatening part:** Aconex already owns **deadline_tracking = 3**. If the startup's wedge
is "we tell you when a notice is due," on an Aconex project that is already solved and configured — mandatory
response-required, working-day due dates, automatic Overdue status. **The wedge cannot be deadline alerting.
It has to be the interpretive layer above the record: what the event *means*, what clause it triggers, what
it is worth, and what the package looks like.** That is where Aconex is 0–1 across the board.

### Q2. Oracle serves mega-projects; does that leave the mid-market ($5M–$500M) uncovered?

**Uncovered by Oracle — yes, structurally and deliberately. But "uncovered by Oracle" is not the same as
"uncovered."**

Evidence that Oracle abandons the mid-market by design:
- P6 EPPM and Unifier carry **25-user minimums** (50 for government editions) at £220 and £132/user/month —
  a floor of roughly **£66k/yr for P6 and £40k/yr for Unifier before implementation**.
- Aconex's alternate metric is **Project Value**; a licensing advisory notes any increase in project value
  triggers a new order. Value-based pricing prices small projects out at the top of the funnel.
- Contracts are **"non-cancellable during the term."**
- Several SKUs are "under controlled availability."
- Implementation runs through OPN partners; reviewers report Unifier needs "a bit of programming" and Java
  knowledge.
— https://assets.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-14/documents/717959/423103118187025-pricing-document-2025-06-25-1321.pdf ;
https://redresscompliance.com/oracle-primavera-unifier-aconex-licensing-2026 ;
https://www.capterra.com/p/181519/Oracle-Primavera-Unifier/

Two caveats that matter for the founder:
- Aconex Enterprise at £46/user/month with a **5-user minimum** is not actually expensive. Oracle *can* land
  small; it just doesn't hunt there.
- **The mid-market gap is Procore's and Autodesk's territory, not empty land.** The correct reading is: the
  mid-market is uncovered *for Oracle-grade contemporaneous records*, which is a different and more
  interesting statement. Mid-market projects run on Procore/ACC/email/WhatsApp, which means their record is
  *fragmented* — which is precisely the thesis's premise. Oracle's absence is evidence *for* the thesis about
  the mid-market, but the competitive set there is Procore and Autodesk (see sibling reports), not Oracle.

### Q3. Does P6/XER being a de-facto standard create an easy lightweight-integration path for a solo founder?

**YES — this is the single most actionable finding in this report.**

- **XER is a file, and files can be uploaded.** No auth, no OPN membership, no throttling, no per-user
  licence, no procurement. A drag-and-drop XER upload gets you activities, logic, calendars, WBS, resources,
  UDFs and — critically — the ability to diff two dated snapshots.
- **Oracle publicly documents the mapping.** Official *XER Project*, *XER Resource* and *XER Role*
  import/export data maps sit on docs.oracle.com. You do not have to reverse-engineer the format.
  — https://docs.oracle.com/cd/G48897_01/102093.htm
- **A market has already validated the pattern.** XER Schedule Toolkit, Schedule Auditor and ScheduleLens all
  ship products that read XER without touching P6 — including schedule-comparison/change-detection, which is
  the exact primitive delay analysis needs.
  https://xertoolkit.com/our-features/schedule-comparison/ ; https://www.scheduleauditor.org/about ;
  https://schedulelens.com/blog/xer-file-analysis/
- **Contracts already require the file.** Monthly XER submission is a standard programme deliverable; the
  evidentiary chain in delay disputes is literally the sequence of dated XER snapshots.
- **The alternative is expensive.** Live P6 EPPM API access requires the separately licensed Web Services
  Cloud Service at £36/user/month plus potential indirect-use exposure. **Upload beats integrate on cost,
  speed, legal risk and procurement, and loses nothing evidentially** — because forensic delay analysis works
  on snapshots anyway.

**Recommended V1 data posture for a solo founder, in priority order:**
1. **XER upload** (schedule spine + baseline diffing) — zero-friction, zero-licence, contractually already available.
2. **Email forward / .msg + .pdf upload** (correspondence and notices) — no vendor dependency at all.
3. **Aconex Mail Search API + Documents API + Related Items API**, registered *by the customer* under
   Oracle's own ISV guidance — for design partners already on Aconex. Budget for single-file-at-a-time
   downloads and 503 throttling.
4. Only join OPN when you have enough Aconex customers that "commercially available" is unavoidable.

---

## 12. UNKNOWNS — and what would settle them

| Unknown | What would settle it |
|---|---|
| Oracle Construction & Engineering revenue and growth | Oracle does not break out OCE in its 10-K; "Cloud services and license support" is reported at segment level only. Would need Oracle segment disclosure or an analyst teardown. |
| Aconex's *current* user/organisation/project-value figures | The only figures I could source are the 2020 datasheet (6M users, 70,000 orgs, $1T, 70 countries) and the 2017 press release. A current Aconex datasheet or an Oracle CloudWorld keynote deck would settle it. |
| Textura acquisition price from an Oracle-owned source | Oracle's Textura product page carries no price; the ~$663M figure is `UNVERIFIED` here. Oracle's 2016 8-K / press release archive would settle it. |
| Exact Aconex API rate limits | Oracle publishes only "reasonable limits." Only a registered Early Access account would reveal the real numbers. |
| Whether "Aconex for Outlook" can file *inbound external* email into the project record | The help index links the tool but I could not retrieve its content page. `UNVERIFIED`. The Aconex for Outlook user guide would settle it — this materially affects the email_ingestion score (currently 2). |
| Whether an Aconex change event can be created directly from an RFI/mail item | The change-event wizard docs do not say; the Connected Cost datasheet says you can "easily track the cost impact of RFIs, variation requests, and other correspondence." `UNVERIFIED` whether that link is a typed relation or manual re-keying. |
| Real-world Aconex/Unifier implementation cost and elapsed time | Only ITQlick's $5k–$50k estimate, explicitly an analyst estimate. A public-sector procurement award notice (UK Find a Tender / TED) naming Aconex or Unifier implementation services would settle it with real figures. |
| Aconex market share vs Procore/ACC by project count or revenue | No credible current source found. A Gartner/IDC or JBKnowledge ConTech Report cut would settle it. |
| Whether any third party already sells claims analytics on top of Aconex | Oracle has no marketplace, so absence of evidence is weak evidence. OPN Technology Partner directory search would settle it. |
