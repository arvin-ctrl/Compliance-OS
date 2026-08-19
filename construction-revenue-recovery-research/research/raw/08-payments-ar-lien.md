# 08 — Construction Cash / AR / Lien / Payment-Compliance Stack
**Category report.** Siteline · Levelset (Procore) · Handle · Built Technologies · Flashtract (Trimble Pay) · GCPay (Autodesk) · Oracle Textura · Billd · Constrafor
Research date: 2026-08-19. All URLs verified live on that date unless noted.

---

## 0. ONE-PARAGRAPH VERDICT

This category has **already won the deadline-tracking war — for statutory deadlines only** — and the winner was bought for $484.1M and then quietly demoted from "product" to "plumbing." The category is extremely strong at *document completeness at the billing gate* (evidence_completeness = 3, audit_trail = 3, deadline_tracking = 3) and is a total blank at *commercial event detection* (rfi/daily-report/schedule/email ingestion = 0, clause_extraction = 0, delay_detection = 0). The single most valuable finding in this report is that the highest-frequency revenue leak in construction is **not** the missed lien deadline (56% of subs in 2 years) but the **unapproved change order performed anyway** (97% of specialty contractors, 77% of whom have written that work off) — and *nobody in this category surfaces it*. The one company that does (Clearstory) sits outside this category and stops at digitising the T&M tag, not at proving entitlement.

---

## 1. SNAPSHOT — WHO THESE COMPANIES ARE

### 1.1 Siteline
- **What it is.** Construction billing / AR platform for **subcontractors** (trade contractors). Pay app generation and submission (AIA G702/G703 and 23,000+ GC-specific custom forms), lien waiver generation and lower-tier waiver collection, compliance document tracking, change order tracking, A/R aging, collections, cash and billing forecasting, and a **Lien Rights Management add-on**. Source: https://www.siteline.com/ , https://www.siteline.com/feature/construction-payment-application-software
- **ICP.** Commercial subcontractors; buyer is the CFO / controller / A/R manager / billing manager. Explicitly *not* GCs (GCs are the counterparty). Source: https://www.siteline.com/
- **Scale claims (vendor-published, 2026).** "$14B billed across 250k+ projects"; "23,000+ pay app and lien waiver forms from 17,000+ GCs digitized." Source: https://www.siteline.com/
- **Funding.** $18.4M total: $3.4M seed (First Round Capital, Brick & Mortar Ventures, Designer Fund, South Park Commons) + $15M Series A led by Menlo Ventures, announced 2022-02-24. Tyler Sosin (Menlo) joined the board. At Series A the company disclosed "over $180 million in annualized billing" processed. Source: https://www.businesswire.com/news/home/20220224005099/en/Siteline-Raises-$18.4M-to-Reimagine-Construction-Finance ; https://menlovc.com/perspective/siteline-attacking-the-payments-problem-in-construction/
- **No publicly announced round since Feb 2022** (searched to Aug 2026). `UNVERIFIED` whether a later round exists. Latka lists "$4.7M est. ARR, 43 employees (Sept 2025), $0 raised, bootstrapped" — **the "$0 raised / bootstrapped" claim is demonstrably false** (BusinessWire, above), so I treat the entire Latka row as **unreliable** and do not use it. Source (flagged unreliable): https://getlatka.com/companies/siteline.com
- **Geography.** US (all 50 states for lien rights content); GC-portal integrations are US-centric.

### 1.2 Levelset (formerly zlien / legal entity Express Lien, Inc.) — a Procore company
- **What it is.** The category-defining **statutory lien rights** platform: preliminary notices, notices of intent to lien, mechanics lien filing and cancellation, lien waivers, job/owner research ("who is actually on this job and who pays"), payment-risk intelligence, and a 50-state + DC deadline rules engine. Source: https://www.levelset.com/ , https://www.siteline.com/compare/levelset
- **ICP.** Material suppliers, equipment rental, subcontractors, GCs — SMB and mid-market. Historically a self-serve/freemium motion layered with an inside sales team.
- **Ownership.** Acquired by Procore, closed **2021-11-02**. Source: https://investors.procore.com/news/news-details/2021/Procore-Completes-Acquisition-of-Levelset-to-Simplify-Lien-Management-Workflows-for-Construction/default.aspx
- **Pre-acquisition funding.** ~$47–48M venture across seed/A/B/C, including a $30M Series C at end of 2019. Source: https://thegtmnewsletter.substack.com/p/how-levelset-scaled-to-25m-arr-then ; https://tracxn.com/d/companies/levelset/__RBaqPI6NMUCk_xlSrO1CnLhNM6g47TB30L8RWvIoLmk (Tracxn = secondary)
- **Geography.** US 50 states + DC.

### 1.3 Handle (handle.com)
- **What it is.** Enterprise "financial infrastructure for construction credit teams": lien & notice management with an automatic statutory deadline engine, waiver automation, credit management / job sheets, construction-native online payments, and a **human "Full Service Research"** layer (manual verification, senior-level audits, dedicated account managers described as "former credit managers, lien specialists, and construction finance veterans"). Next-day eRecording and in-person courier delivery to county clerks. Source: https://www.handle.com/ , https://www.handle.com/payment-compliance/notice-management/
- **ICP.** **Enterprise material suppliers, equipment dealers, distributors** — CFO, VP/Director of Credit, Credit Manager, A/R Manager, Controller. Named customers: Ferguson, ABC Supply, US LBM, Oldcastle, EquipmentShare, Crescent Electric, HOLT CAT, SRS Distribution, The Home Depot, Cemex, Builders FirstSource, Floor & Decor, Vulcan, Heidelberg Materials, Herc Rentals, WillScot, TDIndustries. Source: https://www.handle.com/
- **Funding.** **$27M Series B led by Marbruck**, with Energize Capital, Suffolk Technologies, Liquid 2 Ventures, RXR participating and a new strategic investment from WEX. Disclosed metrics: "almost doubled its contracted ARR bookings" over the preceding six months; platform manages "more than $160B+ in construction invoices and financial workflows." Source: https://www.handle.com/series-b/ — **`UNVERIFIED`: announcement date and total-raised-to-date are not stated on the page; Crunchbase returned HTTP 403.**
- **Geography.** All 50 US states + Canada.

### 1.4 Built Technologies
- **What it is.** Construction **finance** platform on the **lender/owner** side: construction loan administration, AI Draw Agent, draw inspections, budget management, deal management/underwriting, portfolio reporting, plus "Construction Financials" for owners/GCs (budget, invoice management, lien waiver management, capital requests, compliance tracking, payments). Source: https://getbuilt.com/
- **ICP.** Banks, credit unions, private credit, owners/developers, GCs. Named: Fifth Third, Glacier Bank, Valley Bank, D.R. Horton, Camden, Goldman Sachs, AllianceBernstein. Source: https://getbuilt.com/
- **Scale.** "More than 625 banks, private credit lenders, owners, and general contractors rely on Built to manage over $350 billion in real estate and construction activity annually"; AI trained on "$3T+ in real estate finance data." Source: https://getbuilt.com/
- **Funding / valuation.** $289.1M raised across 5 rounds, most recently a $125M Series D (2021); **$1.5B valuation, unicorn status reached 2021**; "more than $200B in total construction value managed" as of the 2022 announcement. Source: https://www.businesswire.com/news/home/20220207005629/en/Built-Technologies-Reached-More-Than-200B-in-Total-Construction-Value-Managed-Achieved-1.5B-Valuation-and-Unicorn-Status-in-2021 ; funding totals via Tracxn/PitchBook (secondary). 2024 revenue $83M per Latka — **`UNVERIFIED`, estimate only**: https://getlatka.com/companies/built-technologies
- **Note on posture.** Built sits with the party that **withholds** money (the lender releasing draws), not the party claiming it. Strategically this is the opposite side of the thesis.

### 1.5 Flashtract → **Trimble Pay**
- **What it is.** GC↔sub payment application and compliance-document exchange (pay apps, lien waivers, compliance docs).
- **Funding & exit.** Launched 2020; $15M Series A early 2022 led by Addition with Shine Capital. **Acquired by Trimble, announced 2024-05-08, financial terms not disclosed**; rebranded **Trimble Pay**, first integrating with Trimble Viewpoint Vista ERP inside Trimble Construction One. Source: https://www.prnewswire.com/news-releases/trimble-acquires-flashtract-adding-construction-payment-and-subcontractor-compliance-technology-to-minimize-risk-and-improve-efficiency-for-contractors-302139057.html ; https://www.ironpros.com/accounting-financial-tools-job-costing-software/article/22908755/what-15m-vc-infusion-for-flashtract-payment-app-reveals-about-the-construction-tech-market
- **Pricing model (rare disclosure).** "Flashtract charges a SaaS fee for ongoing product enhancement and also collects a fee based on **annual approved pay applications**." Source: https://www.ironpros.com/accounting-financial-tools-job-costing-software/article/22908755/what-15m-vc-infusion-for-flashtract-payment-app-reveals-about-the-construction-tech-market

### 1.6 GCPay (parent: Payapps) → **Autodesk**
- **What it is.** GC-side subcontractor billing rail: pay applications, schedule-of-values review, lien waivers, compliance document collection, approvals, e-payments, ERP integration, and a **named Change Order Management module**. Source: https://ww3.gcpay.com/
- **Scale (vendor-published).** "$27.9B+ in payment applications processed annually"; "48,000+ active companies"; "over 50 customers from ENR's Top 400"; "1.4M+ compliance documents exchanged"; "2.7M+ lien waivers exchanged." Source: https://ww3.gcpay.com/
- **Ownership.** Autodesk signed the definitive agreement to acquire Payapps (GCPay in North America; Payapps in AU/NZ/UK/IE) on **2024-01-24**, expected to close in Autodesk Q1 FY2025. Price not disclosed. Through 2023 Payapps + GCPay "collectively processed close to **$50 billion** in payment applications" and "helped construction teams save nearly 350,000 project hours a year." Source: https://adsknews.autodesk.com/en/news/autodesk-to-acquire-payapps/ ; https://www.enr.com/articles/58067-autodesk-acquires-payapps-maker-of-gcpay-to-compete-in-payments
- **Integrations documented.** Sage Viewpoint, CMiC, Autodesk Build Cost Management. FOUNDATION not listed. Source: https://www.contechindex.com/products/gcpay

### 1.7 Oracle Textura Payment Management
- **What it is.** The incumbent enterprise GC↔sub invoicing/payment/compliance rail (collaborative subcontractor invoicing, compliance, lien waivers, notarisation, disbursement). Owned by Oracle since the 2016 Textura acquisition.
- **ICP.** Large GCs and their subcontractor bases; subs are usually **compelled** onto it by the GC.
- **Reputation.** G2: 4.1/5 across 44 reviews (vs GCPay 4.6/5 across 282). Capterra/GetApp: **2.6/5 across 23 reviews**. Sources: https://www.g2.com/compare/gcpay-vs-oracle-textura-payment-management ; https://www.capterra.com/p/181520/Oracle-Textura-Payment-management/ ; https://www.getapp.com/all-software/a/oracle-textura-payment-management/

### 1.8 Billd (financing)
- **What it is.** Working capital for commercial subcontractors: 120-day material financing, **Pay App Advance**, Flex Line, Supplier Direct-Pay, **Predictable Pay** (an early-pay program co-designed with GCs), plus insurance products. Founded 2018. Source: https://billd.com/about/
- **Funding.** $30M Series B (2021); **$17.5M on 2024-10-29** led by LL Funds and MissionOG with RJT Credit, Ulysses Management, HighSage Ventures; a **$144M financing facility with Atlas SP Partners (Dec 2024)**; **$7.3M in Nov 2025** led by MissionOG with HighSage and RJT to accelerate Predictable Pay. Disclosed 120% revenue growth 2021→2024; **surpassed $1B in total material purchases financed** (as of 2023). Sources: https://www.prnewswire.com/news-releases/billd-secures-17-5m-funding-round-to-supercharge-growth-expand-product-suite-302289102.html ; https://www.pymnts.com/news/investment-tracker/2025/billd-raises-7-3-million-for-capital-solutions-for-subcontractors/ ; https://billd.com/about/ ; https://www.prnewswire.com/news-releases/billd-launches-predictable-pay-with-general-contractors-establishing-a-new-payment-standard-in-construction-302563544.html

### 1.9 Constrafor (financing + compliance)
- **What it is.** GC-side subcontractor prequalification, contract management, **COI (certificate of insurance) management**, invoice management, payments and diversity procurement tracking; sub-side **Early Pay** (invoice financing). Source: https://www.constrafor.com/
- **Scale (vendor-published).** "40,000+ contractors in network; 7,000+ projects; $125M+ in invoices financed; $500M+ in invoices managed; $10B+ in COIs managed." Named clients: Balfour Beatty, Skanska, Allan Myers, McHugh, M.B. Kahn, Ames. SOC 2 certified. Source: https://www.constrafor.com/
- **Funding.** `UNVERIFIED` — no total disclosed on site; press/blog pages 404'd during research.

---

## 2. PRODUCT SURFACE RELEVANT TO REVENUE RECOVERY

| Module | Vendor(s) | What it actually does | Evidence |
|---|---|---|---|
| Statutory deadline rules engine (50 states + DC, ± Canada) | Levelset, Handle, Siteline (add-on) | Computes preliminary-notice / NOI / lien-filing / enforcement deadlines from job facts | https://www.levelset.com/mechanics-lien-deadline-calculator/ ; https://www.handle.com/payment-compliance/notice-management/ |
| Free public deadline calculator + 50-state charts (SEO engine) | Levelset | Zip code + labor/supplies/rental + project type + who hired you + work dates → "a custom recommendation" of what to send and when. Free, no account required. | https://www.levelset.com/mechanics-lien-deadline-calculator/ ; https://www.levelset.com/blog/lien-and-notice-deadlines-in-all-50-states/ |
| Statutory notice/lien drafting + service (certified mail, eRecording, courier) | Levelset, Handle | Generates and *serves* the instrument; monetised per document | https://www.levelset.com/pricing/ ; https://www.handle.com/payment-compliance/notice-management/ |
| Pay app generation on GC-specific forms | Siteline, GCPay, Textura, Flashtract | 23,000+ digitised forms from 17,000+ GCs (Siteline) | https://www.siteline.com/ |
| Lien waiver generation + lower-tier waiver chase | Siteline, GCPay, Textura, Handle, Built, Procore Pay | Conditional/unconditional generation, e-sig, bulk request, reminders, status tracking | https://www.siteline.com/feature/lien-waiver-management-software |
| Compliance-document gating of payment | GCPay, Textura, Flashtract, Procore Pay | Payment does not release until COIs, waivers, certified payroll etc. are complete | https://ww3.gcpay.com/ |
| Change order tracking (post-document) | Siteline, GCPay, Textura | Compile forms + backup, sign/submit, **add approved line items to the SOV** | https://www.siteline.com/blog/the-ultimate-guide-to-construction-change-orders |
| A/R + exposure reporting | Siteline | Overview (billed / **unbilled work** / **retention held** / open items), Billing, A/R Aging 30/60/90/120+, Billing Forecast, Time-to-Payment, Cash Forecast, **Project Snapshot health grade A/B/C incl. "pending change orders"** | https://www.siteline.com/blog/sitelines-reports-what-they-show-and-why-it-matters |
| Counterparty / job risk intelligence | Levelset, Handle, Constrafor | Who is on the job, who pays slowly, owner/GC payment history, prequal, COI | https://www.siteline.com/compare/levelset ; https://www.constrafor.com/ |
| Draw / lender-side compliance | Built | Draw requests, inspections, budget, policy adherence, AI Draw Agent | https://getbuilt.com/ |
| Working capital against receivable | Billd, Constrafor | Pay App Advance, Early Pay, material financing | https://billd.com/about/ ; https://www.constrafor.com/ |

**What is conspicuously absent across every vendor in this category:** contract-document ingestion, clause extraction, RFI ingestion, daily-report ingestion, schedule integration, delay detection, causation/responsibility attribution, and any notion of a **contractual** (as opposed to statutory) notice deadline. I found **zero** evidence that any product in this category has ever tracked a contract-clause notice period.

---

## 3. CAPABILITY MATRIX — CATEGORY AS A SUBSTITUTE STACK (best-of-category per dimension)

`SCORES| 1,0,3,3,0,1,0,0,2,1,0,1,1,3,2,2,3,0,3,3,1,2,3,3,2,2`

| # | Dimension | Score | Justification (best-of-category) | URL |
|---|---|---|---|---|
| 1 | contract_ingestion | **1** | Only contract *metadata* is ingested — contract value, SOV line items, retainage %, payment terms — imported from ERP. No contract document is read. | https://www.siteline.com/integrations |
| 2 | clause_extraction | **0** | No vendor extracts clauses. Levelset publishes *statute* guides, never parses *your* contract. | https://www.levelset.com/blog/lien-and-notice-deadlines-in-all-50-states/ |
| 3 | notice_detection | **3 (statutory) / 0 (contractual)** | Levelset & Handle natively determine which statutory notices a party must send from job facts — this is the whole product, monetised. **Zero** capability for contract-clause notice obligations. | https://www.levelset.com/mechanics-lien-deadline-calculator/ |
| 4 | deadline_tracking | **3 (statutory) / 0 (contractual)** | 50 states + DC (+ Canada for Handle), automatic deadline engine with alerts; Siteline sells it as a paid add-on. Statutory only. | https://www.handle.com/payment-compliance/notice-management/ ; https://www.siteline.com/pricing |
| 5 | rfi_event_ingestion | **0** | No vendor ingests RFIs. | (absence across all product pages cited in §2) |
| 6 | email_ingestion | **1** | Email is used as a *transport* for waiver requests, reminders and collections; nothing parses inbound mail for commercial events. | https://www.siteline.com/feature/lien-waiver-management-software |
| 7 | daily_report_ingestion | **0** | None. Siteline supports T&M as a *billing type*, not as field-record ingestion. | https://www.siteline.com/feature/construction-payment-application-software |
| 8 | schedule_integration | **0** | No P6 / MS Project / Primavera integration anywhere in the category. | https://www.siteline.com/integrations |
| 9 | change_order_workflow | **2** | Real and marketed (GCPay has a dedicated Change Order Management module; Siteline compiles CO forms + backup and pushes approved lines into the SOV) — but the workflow **begins after a change order document exists**. | https://ww3.gcpay.com/ ; https://www.siteline.com/blog/the-ultimate-guide-to-construction-change-orders |
| 10 | claim_identification | **1** | Only the *payment* claim: unpaid invoice → NOI → mechanics lien. No construction-claim (entitlement) identification. | https://www.levelset.com/pricing/ |
| 11 | delay_detection | **0** | None. | — |
| 12 | responsibility_attribution | **1** | Party/role identification only ("job research": who hired whom, owner, lender, GC). No causation or fault attribution. | https://www.siteline.com/compare/levelset |
| 13 | contemporaneous_evidence_graph | **1** | A timestamped *document* trail (waivers, notices, proof of service, eRecording receipts) exists, but nothing links events → obligations → evidence. | https://www.handle.com/payment-compliance/notice-management/ |
| 14 | evidence_completeness | **3** | The category's strongest capability. Siteline flags missing lien waivers and lien status ("protected / at risk / missing info"); GCPay/Textura/Flashtract/Procore Pay *block payment* until the compliance package is complete. Market is fully trained on "software tells me which document is missing before money moves." | https://www.siteline.com/blog/sitelines-reports-what-they-show-and-why-it-matters ; https://ww3.gcpay.com/ |
| 15 | recoverable_dollar_estimation | **2** | Dollars-at-risk on the *receivable*: unbilled work, retention held, balance to finish, aging buckets, cash forecast, A/B/C project health grade. No entitlement valuation or quantum. | https://www.siteline.com/blog/sitelines-reports-what-they-show-and-why-it-matters |
| 16 | claim_package_generation | **2** | Generates, executes, serves and records the *statutory instrument* (a form plus an amount) and charges per document — but that is not a claim package with narrative, exhibits and quantum. | https://www.levelset.com/pricing/ |
| 17 | notice_drafting | **3 (statutory) / 0 (contractual)** | Drafting and serving statutory notices at industrial scale is the core monetised act. Nothing drafts a contractual notice citing a clause. | https://www.levelset.com/pricing/ |
| 18 | schedule_impact_analysis | **0** | None. | — |
| 19 | procore_integration | **3** | Levelset **is** Procore (acquired 2021); Procore Pay lien waivers are "powered by Levelset"; Siteline lists Procore Pay as an integration. Caveat: a Siteline reviewer reports "The Procore integration doesn't work well." | https://support.procore.com/integrations/levelset ; https://www.siteline.com/integrations ; https://www.softwareadvice.com/product/393521-Siteline/ |
| 20 | autodesk_integration | **3** | GCPay/Payapps **is** an Autodesk company; documented integration with Autodesk Build Cost Management. | https://adsknews.autodesk.com/en/news/autodesk-to-acquire-payapps/ ; https://www.contechindex.com/products/gcpay |
| 21 | outlook_gmail_integration | **1** | Outbound email only; no mailbox add-in, no thread ingestion, no evidence capture from mail. | https://www.siteline.com/integrations |
| 22 | mobile_workflow | **2** | "Web-based, mobile-optimized" (Siteline); Built has mobile draw inspections. No field-first capture product in this category. | https://www.siteline.com/pricing ; https://getbuilt.com/ |
| 23 | audit_trail | **3** | The category *is* an audit-trail category: every pay app, waiver, approval, notice has a timestamped record, plus certified-mail proof of service and county eRecording receipts. | https://www.handle.com/payment-compliance/notice-management/ ; https://ww3.gcpay.com/ |
| 24 | portfolio_risk | **3** | Siteline: portfolio A/R aging, project health grades, GC payment-behaviour tracking, cash forecast. Levelset: owner/GC payment-history risk intelligence. Built: lender portfolio reporting. | https://www.siteline.com/blog/sitelines-reports-what-they-show-and-why-it-matters ; https://getbuilt.com/ |
| 25 | performance_pricing_compatibility | **2** | Precedent exists for value-linked pricing — Flashtract charged "a fee based on annual approved pay applications"; Levelset charged per document ($59 notice / $349 lien); Procore prices on Annual Construction Volume; Billd/Constrafor earn on financed dollars. But **no contingency / % -of-recovery pricing anywhere.** | https://www.ironpros.com/accounting-financial-tools-job-costing-software/article/22908755/what-15m-vc-infusion-for-flashtract-payment-app-reveals-about-the-construction-tech-market ; https://www.levelset.com/pricing/ ; https://www.procore.com/pricing |
| 26 | consultant_replacement_potential | **2** | Levelset genuinely substituted for construction attorneys on routine lien filings — hard proof: Procore's 10-K carries a standing **unauthorized-practice-of-law** risk factor. Handle substitutes for in-house credit staff via a human service layer. Neither touches claims consultants / delay experts. | Procore FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm |

### Per-company deltas vs the category score
- **Levelset** — the *only* member scoring 3 on notice_detection / deadline_tracking / notice_drafting; also the only one with a nationwide free SEO deadline-calculator funnel and an attorney network. Weak on 9 (change_order_workflow = 0) and 15.
- **Siteline** — the only one that puts unbilled work + retention held + pending change orders + lien status on **one screen** for the sub; strongest on 15 and 24 within the category. Weakest on 19 in practice (reviewer-reported broken Procore integration).
- **Handle** — strongest on 13/23 for suppliers (manual verification + courier + next-day eRecording); strongest human-in-the-loop service layer, which is the closest thing in the category to consultant replacement (26).
- **GCPay / Textura / Flashtract** — strongest on 14 (they hold the payment gate) and 23; near-zero on everything upstream of the pay app. GCPay uniquely ships a named Change Order Management module (9).
- **Built** — strongest on 23/24 for the *lender*; structurally on the withholding side of the money.
- **Billd / Constrafor** — score 0–1 on almost all 26 dimensions; they are balance-sheet products, not information products. Their relevance is that they prove subs will pay a **spread on the receivable** rather than a SaaS fee (25).

---

## 4. PRICING

| Vendor | Published pricing | Confidence / method |
|---|---|---|
| **Levelset** | **$59/recipient** to send a notice or demand; lien filing requires a subscription. Third-party: **$349 per mechanics lien filing** (incl. project research, party confirmation, filing), **$149 lien cancellation**; preliminary notices first 3 free then **$19/send**; NOIs first 3 free then **$49/send**; **subscriptions from $149/user/month**. Freemium account available. | Per-document fees **HIGH** (vendor pricing page). Subscription $149/user/mo **MEDIUM** — Capterra listing + Siteline competitor page agree. https://www.levelset.com/pricing/ ; https://www.capterra.com/p/145317/zlien/ ; https://www.siteline.com/compare/levelset |
| **Siteline** | No published price. Annual contracts **priced on billing volume**; unlimited users and offices, unlimited custom forms, dedicated onboarding, GC portal integrations (GCPay, Textura, Procore Pay) and one ERP integration included; **one-time implementation cost**; **Lien Rights Tracker is a paid add-on**. Two SKUs: Siteline Suite and Siteline Vendor Management. | **MEDIUM** on structure (vendor pricing page + Capterra summary), **NONE** on dollar amounts. https://www.siteline.com/pricing |
| **Handle** | None published. | **NONE**. https://www.handle.com/ |
| **Built** | None published. | **NONE**. https://getbuilt.com/ |
| **Flashtract / Trimble Pay** | SaaS fee **plus a fee based on annual approved pay applications**. No dollar amounts. | **MEDIUM** (trade press, 2022). https://www.ironpros.com/accounting-financial-tools-job-costing-software/article/22908755/what-15m-vc-infusion-for-flashtract-payment-app-reveals-about-the-construction-tech-market |
| **GCPay** | Contact sales; "scalable model based on project and pay-application volume." | **MEDIUM** (analyst listing). https://www.contechindex.com/products/gcpay |
| **Oracle Textura** | Capterra/GetApp list a starting price of **"$5,000 per feature"**; no tiers, core platform + add-ons. | **LOW** — review-site field, not an Oracle price list. https://www.capterra.com/p/181520/Oracle-Textura-Payment-management/ |
| **Procore (incl. Levelset-derived features)** | No published dollar prices. Model = **upfront annual fee by product, based on Annual Construction Volume (ACV)**; unlimited users/storage/support/implementation included. Four bundles introduced Feb 2026: Project Execution, Cost Management, Resource Management, Project Lifecycle Management. **Lien rights management / Levelset does not appear on the pricing page at all.** | **HIGH** on model, **NONE** on numbers. https://www.procore.com/pricing ; FY2025 10-K |
| **Billd / Constrafor** | None published (financing rates quoted per deal). | **NONE**. |

**Pricing pattern that matters for the thesis:** the only *published* prices in this whole category are Levelset's **per-document** fees. The alert was free; the **filing** was the product. Everything else in the category is volume-priced (billing volume, pay-app volume, ACV) — i.e. the category has already normalised **charging on the dollars flowing through**, which is the nearest available analogue to performance pricing.

---

## 5. INTEGRATIONS, API AND DATA EGRESS

**Siteline** — publishes a named integration list: Sage 300 CRE, Sage 100 Contractor, Sage Intacct, QuickBooks Enterprise Contractor, QuickBooks Online, Oracle NetSuite, Acumatica, Viewpoint Vista, Viewpoint Spectrum, Procore Pay, CMiC, Foundation Software, Deltek ComputerEase, Oracle Textura. **No public API documentation, no endpoints, no auth docs**; several entries are marked "coming soon." Listed on the Sage Intacct marketplace. Sources: https://www.siteline.com/integrations ; https://marketplace.intacct.com/MPListing?lid=a2DRn00000VzwVSMAZ

**Handle** — claims "Handle integrates with any ERP" but names none publicly. Implementation requires "read-only or scoped access to ERP data. Standard export files or API credentials." **No public API docs.** Source: https://www.handle.com/integrations/

**Levelset/Procore** — the Levelset↔Procore integration syncs waivers and notices into the Procore project document library and automates waiver requests off approved requisitions. Procore has a genuine public developer platform and App Marketplace, but lien-rights endpoints are not a marketed developer surface. Source: https://support.procore.com/integrations/levelset

**GCPay** — documented direct connections to Sage Viewpoint, CMiC, Autodesk Build Cost Management. FOUNDATION not supported. Source: https://www.contechindex.com/products/gcpay

**Data egress reality.** This is a **document-custody** category, not a data category. What a startup could realistically get out today, without a partnership: (a) PDFs the contractor already possesses (pay apps, waivers, COs, SOVs) via upload or email forward; (b) CSV exports of A/R aging and SOV from the ERP, which is the true system of record; (c) nothing at all from Textura/GCPay/Procore Pay without the GC's cooperation, because those are the GC's rails. **Founder-relevant conclusion:** the ERP + file upload + email forward path is fully viable for a V1 and does not require any of these vendors' consent.

---

## 6. WEAKNESSES AND GAPS — DELIBERATE OR UNATTENDED?

| Gap | Deliberate (strategy) or unattended (opportunity)? | Reasoning |
|---|---|---|
| **No contractual notice-deadline tracking anywhere** | **Unattended — but for a structural reason, not neglect.** | Every one of these products is built on a rules engine that can be authored **once** (50 statutes) and sold to everyone. A contractual deadline must be extracted per contract, which converts a fixed cost into a variable cost. The category avoided it because its unit economics forbid it, not because nobody noticed. **This is the real opportunity and the real risk.** |
| **Change order leak surfaced only after the document exists** | **Deliberate.** | Siteline/GCPay/Textura sit at the pay-app gate; their job is to make the *approved* CO billable. Detecting entitlement before a CO exists means owning field records, which is a different product and a different buyer. |
| **No RFI / daily report / schedule ingestion** | **Deliberate.** | These are finance-department products. The buyer (controller/CFO) does not own that data; the PM does. Crossing that line means selling to a second buyer. |
| **Levelset demoted from product to plumbing inside Procore** | **Deliberate — and the single most important signal in this report.** | See §8. Procore chose to monetise the *payment rail*, not the *rights product*. |
| **No claim/entitlement narrative or quantum** | **Deliberate — legal exposure.** | Procore's own 10-K carries a standing UPL risk factor from Levelset. Moving from "here is the statutory form" to "here is why you are entitled" materially worsens that exposure. Big-co legal departments will not take that trade. |
| **Siteline's reporting is thin and Procore integration is reported broken** | **Unattended.** | Verbatim reviewer complaints, §9. Small team, no publicly announced round since Feb 2022. |
| **Textura UX and support** | **Unattended / abandoned.** | 2.6/5 on 23 reviews; subs are captive because the GC mandates it. |
| **Lien deadlines still missed by a majority of subs** | **Unattended — and it is an adoption problem, not a software problem.** | 56% of subs missed a critical lien deadline in the last 2 years (Siteline 2026, n=492) *five years after* the category leader's $484M exit. Software existence ≠ software adoption. |

---

## 7. ADJACENCY TEST — how hard for THEM to ship "event detection → entitlement matching → evidence → claim package"?

**Category verdict: MEDIUM — but that MEDIUM is carried entirely by Procore and Autodesk. Every pure-play in this category is HARD.**

- **Procore (owns Levelset): data access EASY, org incentive HARD → MEDIUM.** Procore already holds contract documents, RFIs, daily logs, submittals, correspondence, photos, schedule and a native "Change Events" object. It is the single best-positioned company on earth for this pipeline. Against that: (a) it has held that data for over a decade and has never built entitlement logic; (b) its core buyer is the **GC**, and the claims pipeline is predominantly a weapon aimed *at* GCs and owners — Procore would be arming the counterparty against its own customer; (c) it has an active UPL risk factor and repeated UPL proceedings; (d) its 2024–2026 shipping behaviour shows it moving *toward* money movement (Procore Pay, ACV pricing, Feb 2026 bundles) and *away* from rights products. M&A behaviour says it buys rather than builds (Levelset $484.1M, LaborChart $76.2M, Intelliwave $29.8M) — so the realistic path is **acquisition, not construction**.
- **Autodesk (owns GCPay/Payapps): MEDIUM.** Holds ACC project records; but GCPay is a GC-side compliance gate and Autodesk's construction roadmap is broad and slow.
- **Trimble (owns Flashtract/Trimble Pay): MEDIUM-HARD.** Has Viewpoint ERP data; Trimble Pay is brand new and ERP-anchored.
- **Siteline: HARD.** Its entire data model is a downstream mirror of the ERP — SOV, invoices, waivers, aging. It has no RFIs, no daily reports, no schedule, no contract documents, and (per its own integrations page) several ERP connectors still "coming soon." Small team, no new capital announced since 2022. It would have to buy the capability.
- **Handle: HARD.** Supplier/credit ICP, no project-record access, service-heavy delivery model.
- **Built: HARD and misaligned.** Lender-side; its customers are the parties withholding money.
- **Textura/Oracle: HARD.** Effectively in maintenance.
- **Billd / Constrafor: HARD.** Balance-sheet businesses; underwriting incentive, not evidence incentive.

---

## 8. STARTUP POSTURE — PARTNER / CHANNEL / ROADKILL

**PARTNER and CHANNEL, with a narrow ROADKILL zone.**

- **PARTNER / CHANNEL — Siteline, Handle, Billd, Constrafor (and Clearstory).** These sell to *exactly* the buyer a revenue-recovery product needs (the subcontractor CFO/controller), and none of them has the upstream event data. Siteline in particular already renders an **"unbilled work"** tile and a **"pending change orders"** input to its project health grade with nothing intelligent behind them — a feed of "here is work you performed that you have not billed and here is the evidence" makes their dashboard true instead of decorative. Billd and Constrafor are strong **channels** specifically: they underwrite the receivable, so anything that increases the certainty of a receivable is directly accretive to their loss rate. Their sales motions already reach subs at the moment of cash pain.
- **ROADKILL zone — do not build the pay app, the lien waiver rail, the compliance-document gate, or the statutory deadline engine.** Those are owned by Procore, Autodesk, Trimble, Oracle and Levelset, they are commoditised, and the GC controls the rail. Building there means competing with four public companies on their strongest capability (evidence_completeness = 3, audit_trail = 3) with no differentiation.
- **NEUTRAL — Built.** Lender-side; not a competitor, not a useful channel to claimants.
- **Acquisition reality.** This category buys rather than builds: Levelset→Procore ($484.1M), Payapps/GCPay→Autodesk, Flashtract→Trimble, Textura→Oracle. That is a genuine exit path *and* a warning: the multiples paid were for **distribution + a rules engine + a transactional fee**, not for AI. Levelset's ~$25M run-rate fetched roughly **19–22x revenue**, which is the ceiling comp for this category.

---

## 9. TOP 5 VERBATIM CUSTOMER COMPLAINTS (thesis-relevant)

1. **Oracle Textura** — *"Navigating various compliance sections for my company and all of our subtiers is challenging and not organized in user friendly fashion."* → the compliance-document burden the category was supposed to solve is still experienced as chaos. https://www.capterra.com/p/181520/Oracle-Textura-Payment-management/
2. **Oracle Textura** — *"It is difficult to navigate, the changes we can make are limited, and they have failed to process payments and don't realize they have not processed the payment costing us a lot of time bringing to their attention and having to follow up constantly."* → the payment rail itself is a source of lost money and unbilled admin time. https://www.getapp.com/all-software/a/oracle-textura-payment-management/
3. **Levelset** — *"The lien I placed through this software was wrong and a lawsuit was used due to Levelsets error."* → automated legal-instrument generation carries real, customer-visible liability; directly relevant to any product that drafts notices. https://www.capterra.com/p/145317/zlien/
4. **Levelset** — *"They sold me on my ability to utilize an attorney to answer my questions- WHICH IS NOT TRUE!"* → the demand that shows up at the deadline is for *judgement*, not for a form; the category monetised the form and left the judgement gap open. https://www.capterra.com/p/145317/zlien/
5. **Siteline** — *"The Procore integration doesn't work well, and you can't import projects for 'quick bill'."* and *"It would be helpful if the reporting was a little more robust."* → even the best-liked product in the category (5.0/5 but only 4 reviews) is thin on integration depth and analytics. https://www.softwareadvice.com/product/393521-Siteline/ ; https://www.capterra.com/p/252004/Siteline/
6. **Oracle Textura** — *"Works inefficiently. Not logical at all. No help available. Waited 30 minutes for help, never answered."* https://www.capterra.com/p/181520/Oracle-Textura-Payment-management/

---

## 10. HARDEST FACTS

1. **Procore paid $484.104M for Levelset** (closed 2021-11-02): $426.076M cash + $58.028M stock (610,499 shares @ $95.05), $35.0M in escrow (released May 2023), plus 199,670 retention RSAs worth $19.0M excluded from consideration. Allocation: developed technology **$105.5M (7-yr life)**, customer relationships **$38.8M (4-yr life)**, **goodwill $348.318M**. Procore FY2021 10-K → https://www.sec.gov/Archives/edgar/data/1611052/000156459022008783/pcor-10k_20211231.htm
2. **Levelset's revenue was ~$25M annualised at exit, from a primary source.** "The acquisition of Levelset in November 2021 contributed **$4.2 million in revenue in 2021**" (≈2 months post-close). Pro-forma combined FY2021 revenue $532.690M vs Procore standalone $514.821M implies ≈$17.9M of Levelset revenue in the 10 pre-close months → ≈$22M FY2021 revenue. Purchase price ≈ **19–22x revenue**. Same filing.
3. **Levelset's customer-relationships intangible was assigned a 4-year useful life — vs 10 years for LaborChart (2021) and 10 years for Intelliwave (2024).** Procore's own valuation work assumed Levelset's customer base churns roughly 2.5x faster than its other acquisitions. FY2021 10-K (above); FY2024 10-K → https://www.sec.gov/Archives/edgar/data/1611052/000162828025008121/pcor-20241231.htm
4. **"Lien Rights Management" was deleted from Procore's product catalogue between the FY2023 and FY2024 10-Ks.** It is a named product bullet in the FY2021 10-K (filed 2022-03-04) and the FY2023 10-K (filed 2024-02-26, where Procore Pay is described as combining "functionality from Invoice Management and Lien Rights Management with money movement"). It appears **zero times** in the FY2024 10-K (filed 2025-02-26) and the FY2025 10-K (filed 2026-02-24), where Financial Management is only "Project Financials, Accounting Integrations, and Procore Pay." The four Feb-2026 bundles contain no lien/payment-rights package, and procore.com/pricing (Aug 2026) does not mention lien rights or Levelset. → https://www.sec.gov/Archives/edgar/data/1611052/000162828024006848/pcor-20231231.htm ; https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm ; https://www.procore.com/pricing
5. **97% of specialty contractors start work before official change-order authorization; 42% do so more than half the time; 77% have written off change-order work as unrecoverable; 83% say the process hurts cash flow.** Timeline: **22 days** from signed T&M tag to submitted COR + **26 days** from COR submission to signed change order (≈48 days). **53% of GCs cite insufficient documentation as a reason for withholding payment**; 66% cite disputed pricing; >50% of GCs don't pay the full requested amount on 20%+ of CORs; 48% of subs have had a CO dispute escalate to arbitration or legal action. Dodge x Clearstory, *The State of Change Orders in 2026* → https://www.clearstory.build/construction-blog/2026-sc-change-order-report
6. **56% of subcontractors missed a critical mechanic's lien deadline in the past two years** (Siteline, *The State of Subcontractor Billing in 2026*, n=492 construction finance/ops professionals, surveyed May 2026) — five years after Levelset's exit. Same survey: 92% floated payroll in the past year (28% most months); 43% wait 90+ days for retainage vs 15% of GCs; nearly 1 in 5 wait 6+ months; 67% spend 11+ hours/month on pay apps; 59% wait 46+ days to be paid. → https://www.siteline.com/blog/92-percent-of-subcontractors-floated-payroll-last-year-new-siteline-report-finds
7. **Only 5% of subcontractors are always paid on time; only 12% of construction businesses overall; only 15% are always paid in full; just 25% would consider filing a mechanics lien in response to late payment; 13% of businesses would not work again with a sub or supplier who files a lien.** Levelset 2022 Construction Cash Flow & Payment Report, n=519 US construction companies, published 2022-05-02. → https://www.levelset.com/news/construction-cash-flow-payment-report-2022/
8. **Slow payment cost the US construction industry $208B in 2022 (+53% YoY) and $280B in 2024** (Rabbet); average sub waits **96 days** invoice→payment (Siteline 2025, up from 90 in 2019); industry DSO ~83 days (CreditPulse 2025); Autodesk cites **83 days** average for subs to be paid after work in place. → https://bdcnetwork.com/slow-payments-cost-construction-industry-208-billion-2022 ; https://www.siteline.com/blog/siteline-report-reveals-deepening-crisis-in-construction-payments-and-offers-a-blueprint-for-faster-cash-flow ; https://adsknews.autodesk.com/en/news/autodesk-to-acquire-payapps/ ; https://www.docjoist.com/reports/construction-payment-statistics (aggregator — underlying Rabbet/CreditPulse reports not read at source, treat as **secondary**)
9. **Procore carries a standing unauthorized-practice-of-law risk factor because of Levelset:** *"In the past, various aspects of Levelset's lien rights management offering have been subject to claims of UPL... Levelset has incurred in the past, and we expect to incur in the future, costs associated with responding to, defending, resolving, and settling UPL claims, actions, and proceedings."* Procore FY2025 10-K → https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm

---

## 11. KEY QUESTION 1 — Does Levelset PROVE the deadline-tracking wedge, or PROVE that contractual deadlines are a worse business than statutory ones?

**Answer: both, and the second is the more important half. Levelset validates the *shape* of the business and invalidates the *substrate*. "Levelset for contractual deadlines" is a false analogy, and hypothesis A is a materially harder business than Levelset was.**

### What Levelset unambiguously proved
1. **Contractors will pay real money to not miss a deadline.** ~$25M annualised revenue at exit (SEC-confirmed via the $4.2M two-month contribution), $484.1M purchase price, ~19–22x revenue — the largest acquisition Procore had ever made.
2. **The GTM works: free deadline calculator + 50-state guides → SEO dominance → freemium account → per-document transaction → subscription.** The alert was the bait; the filing was the revenue. Levelset's calculator is free and requires no account; the notice costs $59 and the lien costs $349.
3. **A solo-founder-shaped V1 was viable.** Levelset began as "a bootstrapped, transactional platform... the founder's side business" and ran five years with no formal sales playbook. It required **zero** project-record integration — only five job facts (state, work type, project type, who hired you, work dates).

### The six reasons those proofs do not transfer to contractual notice deadlines

| # | Statutory deadlines | Contractual deadlines |
|---|---|---|
| 1 | **Rules engine is authored once and sold to everyone.** 50 states × role × project type is finite, public and free to obtain. Fixed cost, amortised across every customer. | **Rules must be derived per contract.** Every prime, every subcontract, every flow-down is different. Cost of goods scales with customers instead of being amortised — the exact economics the incumbents avoided. |
| 2 | **Bright-line, catastrophic, legally final consequence.** Miss it and the lien right is gone forever. That generates insurance-shaped, fear-driven willingness to pay. | **Soft, negotiable consequence.** GCs routinely accept late notices; many jurisdictions disfavour forfeiture; the sub often still gets paid or settles. Lower fear, lower WTP. |
| 3 | **Trigger requires no project data.** "I started a job." Five fields. | **Trigger is a commercial event** — a differing site condition, a directive, an out-of-sequence instruction. Detecting it requires RFIs, daily reports, emails, schedules. That is the difference between a file-upload V1 and a multi-integration program. |
| 4 | **A physical, chargeable fulfilment layer exists.** Certified mail, county eRecording, courier to the clerk. That is why $349 per lien is defensible. | **No filing, no clerk, no statutory form, no fee.** A contractual notice is an email or letter. **The monetisation event is missing.** Levelset never proved anyone will pay a subscription for the *alert alone* — its alert was free. |
| 5 | **UPL is survivable.** Filling in a statutory form is defensible as "document processing," and Levelset still drew repeated UPL proceedings. | **UPL is worse.** "Your contract's clause 8.3 requires notice within 7 days and here is the letter" is far closer to legal advice, with far less statutory cover. Procore's 10-K shows this cost is real and recurring for a public company; it will be worse for an uninsured solo founder. |
| 6 | **Statutes are stable and public.** Siteline counts only **six** state lien-law changes since 2023 (NM 2023, FL 2023, IL 2025, TX 2025, IA 2026, CO 2026) — a maintainable rate. | **Contracts change every deal.** There is no stable corpus to maintain, only a per-customer extraction problem. |

### What the *exit outcome* additionally proves — the part nobody talks about
Levelset did not become a durable platform pillar. It became a **feature inside a payments rail**:
- FY2021 and FY2023 10-Ks list **"Lien Rights Management"** as a named Procore product. FY2024 and FY2025 10-Ks do not mention it at all. Procore's product line is now "Project Financials, Accounting Integrations, and Procore Pay." The Feb 2026 bundles contain no rights package. procore.com/pricing does not mention it.
- Procore's own valuation assigned Levelset's customer relationships a **4-year** life vs 10 years for its other acquisitions — an explicit assumption of fast churn in the SMB rights business.
- Procore chose to monetise **money movement** (Procore Pay, licensed money transmitter, ACV pricing) rather than **rights**. The deadline product's residual role is to generate the lien waiver that lets a payment clear.

**Read that as the market's verdict:** deadline tracking is a *feature that sells a transaction*, not a *platform that compounds*. Whoever builds hypothesis A should assume the same gravity — the product will be pulled toward whatever transaction it can attach to.

### And the counter-evidence that keeps hypothesis A alive
**56% of subcontractors missed a critical lien deadline in the last two years** (Siteline 2026, n=492) — *after* fifteen years of Levelset, SEO dominance, a free calculator, three competitors and a $484M exit. If the best-funded, best-distributed statutory deadline product on earth leaves a majority miss rate, then the binding constraint was never "the rules engine did not exist." It was **someone has to notice the job started and type five fields in**. Hypothesis A's version of that constraint is far heavier (someone has to notice a commercial event occurred), which is precisely where automated ingestion could be genuinely differentiating — and precisely where Levelset never competed.

**Net verdict for hypothesis A (missed notice deadline prevention): PARTIALLY VALIDATED, RISK RELOCATED.** The willingness-to-pay is proven, the monetisation mechanism is not. Do **not** pitch "Levelset for contract deadlines." Attach the deadline to a **billable dollar** (a change order that can be submitted, a claim that can be invoiced), not to a filing fee that does not exist.

---

## 12. KEY QUESTION 2 — Is "unbilled/unapproved change order" the highest-frequency revenue leak, and who already surfaces it?

**Yes — by a wide margin — and almost nobody in this category surfaces it.**

### Frequency comparison (both 2026, both survey-based)
| Leak | Incidence | Source |
|---|---|---|
| Performed change-order work without authorization | **97% of specialty contractors** (42% more than half the time) | Dodge x Clearstory 2026 |
| Wrote off change-order work as unrecoverable | **77%** | Dodge x Clearstory 2026 |
| Missed a critical statutory lien deadline (2 yrs) | **56%** | Siteline 2026, n=492 |
| Floated payroll while waiting to be paid | **92%** | Siteline 2026, n=492 |

### Dollar comparison
- Change orders and T&M are **10–30% of a specialty contractor's annual revenue**, and subs "not get paid for 10%, 15%, even up to 30% of extra work performed" (Clearstory CEO Cameron Page — vendor assertion, no source cited, treat as **directional**). https://www.clearstory.build/construction-blog/how-change-orders-affect-subcontractor-cash-flow
- **>50% of GCs do not pay the full requested amount on 20%+ of CORs.** 66% cite disputed pricing; **53% cite insufficient documentation**. Dodge x Clearstory 2026.
- On the GC side: **98% have experienced fee erosion from change-order negotiation; nearly 50% report erosion exceeding 10% of their fee** on at least some projects. https://www.clearstory.build/construction-blog/2026-gc-change-order-report
- The gap between work performed and money owed is ~**48 days** (22 internal + 26 external) *before* a dispute even starts.

### Who surfaces it
- **Nobody in the assigned category does.** Siteline's Overview report has an "unbilled work" tile but it is derived from the **contract SOV** (billed-to-date vs contract value) — it cannot see work performed *outside* the contract, which is exactly where the leak is. Its Project Snapshot grade takes "pending change orders" as an input, but only once a CO document exists. GCPay/Textura/Flashtract/Procore Pay **gate** the pay app on approved COs — they *enforce* the leak rather than surface it. Levelset and Handle have **no change-order capability at all**. Built sees it only as a lender-side budget variance.
- **Clearstory does surface it** — and it sits outside this category. Its **Days Aging report** buckets change-order exposure at 30/60/90/120+ across the portfolio, filterable by customer/region/project, with roll-up reporting on "CORs outstanding and aging, unsigned T&M Tags, total exposure." Case study: Castle Contracting, **$4M in protected revenue-at-risk identified on a single project**, 96.7% reduction in T&M tag processing time. Scale: 14,000+ contractors, **$2.1B in CORs shared monthly**, ~$9.2M est. ARR (Latka — **UNVERIFIED**), $7M Series A led by Cloud Apps Capital, named the standard across Suffolk's national portfolio. https://www.clearstory.build/cor-tm-reporting-analytics ; https://www.clearstory.build/
- **What Clearstory does NOT do — the open half.** It digitises the **T&M tag** and ages the **COR**. It does not read the contract, does not identify *which clause* creates entitlement, does not attribute responsibility, does not assess schedule impact, and does not assemble the entitlement narrative. That matters because **53% of GCs name insufficient documentation as their reason for withholding** — the barrier is not "the COR wasn't logged," it is "the COR wasn't *proved*."

**Conclusion for the thesis: yes, the unapproved/unbilled change order is the highest-frequency and highest-dollar revenue leak in construction, it is 1.7x more common than the missed lien deadline, and the market's incumbent (Clearstory) has claimed the *logging* layer and left the *entitlement/evidence* layer open.** Note for the orchestrator: Clearstory overlaps whichever category report covers change-order management — reconcile before scoring.

---

## 13. KEY QUESTION 3 — Is the money wound better attacked at billing time than at claim time?

**Yes, decisively — with one critical caveat about *where* in billing time.**

**Four reasons for billing time:**
1. **Cadence.** Billing happens monthly on every project; claims happen rarely and late. A billing-time product gets a monthly heartbeat — retention, data freshness, habitual use. A claim-time product is episodic and forgotten between uses. Siteline's own economics depend on this: it prices on **billing volume**, i.e. it is paid for a recurring event.
2. **Evidence quality decays fast.** At billing time the T&M tag is hours old and signed by the GC's superintendent in the field. Dodge/Clearstory measures **22 days** from signed T&M tag to submitted COR — the decay begins immediately. At claim time the same record is a year old, the super has left, and the signature is contested.
3. **Leverage inverts at the waiver.** Before the sub signs the lien waiver and before the CO is absorbed into an approved SOV, the sub is holding money the GC wants released. Siteline's own case study — Beaty Masonry, **"75% of payments on hold due to missing or late lower-tier lien waivers"** — shows money stopping at the billing gate, not at the claim gate. After the waiver, it is a claim against a closed contract.
4. **Buyer and budget already exist.** The billing-time buyer (controller / CFO / A/R manager) is a repeat software buyer with an operating budget, already paying Siteline / GCPay / Textura / Procore Pay. The claim-time buyer is a one-off legal/exec budget where consultants and construction attorneys are the incumbents and the purchase is a distress purchase.

**The caveat — attack *upstream of* the pay app, not *at* it.** The pay app itself is the most crowded and least defensible square in construction software (Siteline, GCPay/Autodesk, Textura/Oracle, Trimble Pay, Procore Pay, plus Handle on the supplier side), and the rail is controlled by the **GC**, not the sub who is losing the money. The defensible position is the step **before** the pay app: *event → entitlement → priced COR/notice with attached evidence → hand it to whatever billing rail the customer already uses.* That posture makes Siteline, GCPay, Textura and Procore Pay **channels**, not competitors — and it puts the product on the sub's side of the table, where the willingness to pay actually lives.

---

## 14. UNKNOWNS — and what would settle them

| Unknown | What would settle it |
|---|---|
| Siteline's current ARR, customer count, and whether it has raised since Feb 2022 | A funding press release, SEC Form D, or a management interview. Latka's row is provably wrong on funding and must not be used. |
| Whether Levelset still sells **new** standalone subscriptions, and its current standalone revenue | Procore does not break it out in any 10-K. Settled by a Procore IR/analyst-call transcript or a live sales quote from levelset.com. |
| Handle's total raised, founding year, and Series B date | Crunchbase returned HTTP 403 and handle.com/series-b/ omits the date. Settled by PitchBook/Crunchbase or a dated press wire. |
| Flashtract and Payapps/GCPay acquisition prices | Both undisclosed. Settled by Trimble's and Autodesk's 10-K business-combination notes (materiality thresholds may mean they are never disclosed). |
| Siteline Lien Rights Tracker: state coverage, alert mechanics, add-on price | Siteline does not publish a feature page for it (URL 404s). Settled by a demo/quote. |
| Dodge x Clearstory 2026 sample size and methodology | The blog posts omit both. Settled by the Dodge SmartMarket report PDF. |
| Constrafor total funding | Press/blog pages 404'd. Settled by Crunchbase/PitchBook. |
| Rabbet's $208B / $280B methodology and sample size | Only reached via secondary coverage. Settled by the original Rabbet report PDFs. |
| **Whether ANY vendor in this category has ever tracked a contractual (non-statutory) notice deadline** | I found **zero** evidence in product pages, pricing pages, support docs or reviews. A negative is hard to prove; a targeted vendor Q&A or support-docs search would confirm. Current read: **it does not exist.** |

