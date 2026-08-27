# SCOUT 12 — THE TWO-TABS PROBLEM

**Surface:** people manually shuttling data between two systems, at volume, visibly, forever.
**Run date:** 2026-08-27
**Verdict:** Surface is **wet, but shallower than it looks.** 8 candidates returned. The generic
version of this problem is dead (Zapier/Make/Magical own it). The live money is in a narrow band:
**semantic reconciliation between two file-based systems that Zapier does not list at all.**

---

## METHOD AND ITS LIMITS — read this before trusting anything below

**What I could reach:** vendor pricing pages, Shopify App Store listings and dated reviews, Chrome
Web Store install counts, the Zapier public app directory, Discourse forums (n8n, Make), UserVoice
boards, BiggerPockets, vendor blogs with datelines.

**What I could NOT reach, and it matters:**
- **reddit.com is blocked to this crawler** (hard 400 from the search tool, HTML shell from curl).
  The brief's single richest named-handle source was unavailable. **Every "first ten users" field
  below is therefore weaker than it should be. I have named channels, not people. I have not
  invented a single handle.**
- **Upwork returns 403** to this crawler. I could not pull gig listings with published prices, which
  would have been the T1 evidence for several candidates.
- **Federal Register redirects to an unblock gate.** One regulatory date below is labelled UNVERIFIED.
- **WebSearch budget was exhausted at 200/200 calls mid-run** (shared across the scout fleet).
  The last third of this report was built by direct URL fetch only. Candidates TT-6, TT-7 and TT-8
  are consequently thinner on evidence than TT-1 through TT-5 and are marked accordingly.

**A reusable technique I established, which the Triage Manager should keep:** the Zapier app
directory answers discriminator 1 mechanically. `https://zapier.com/apps/<slug>/integrations`
returns **200** if Zapier supports the app and **404** if it does not. Verified against known-good
controls (quickbooks → 200, shopify → 200) and known-absent apps. Results below.

### Zapier directory presence — checked 2026-08-27

| App | Zapier | App | Zapier |
|---|---|---|---|
| QuickBooks Online | **200** (control) | AppFolio | **404** |
| Shopify | **200** (control) | Buildium | **404** |
| AgencyBloc | 200 | Rent Manager | **404** |
| Vertafore | 200 | AMS360 | **404** |
| ServiceTitan | 200 | Applied Epic | **404** |
| Jobber | 200 | SAP Fieldglass | **404** |
| Housecall Pro | 200 | Beeline | **404** |
| Clio | 200 | Bullhorn | **404** |
| Mindbody | 200 | Toast | **404** |
| Hostaway | 200 | Restaurant365 / xtraCHEF | **404** |
| Guesty | 200 | UNFI / KeHE | **404** |
| Planning Center | 200 | Dentrix / Eaglesoft / Open Dental | **404** |
| | | Availity / Waystar | **404** |
| | | Procare / brightwheel | **404** |
| | | LCPtracker | **404** |
| | | MarginEdge | **404** |

*(200s confirmed by page fetch. 404s: AppFolio, AMS360 and SAP Fieldglass confirmed by two
independent fetch methods; the remainder by HTTP status probe with slug variants tried. Slug-guessing
is the residual risk — Bullhorn in particular I tried under five slugs and got 404 on all five, which
I flag as **likely but not certain**.)*

---

## SURFACE READ — three structural findings that should shape triage

**1. The horizontal two-tabs tool cannot monetise, and its owner just admitted it.**
Magical — the canonical "move data between two browser tabs" product — has **300,000 users and 3.5K
ratings at 4.4★** on the Chrome Web Store
(`chromewebstore.google.com/detail/magical-ai-automation-and/iibninhmiggehlcdolcilmhacighjamp`,
fetched 2026-08-27). That is 300,000 people whose job is literally this problem: **the demand is not
in question.** But getmagical.com/pricing as of 2026-08-27 no longer sells a horizontal product — the
page reads *"execute real operational work across healthcare systems — from patient access to revenue
cycle"* and is demo-gated. **The best-distributed horizontal player in this category went vertical
into healthcare and hid its price.** Read that as: the generic wedge is a free-tier commodity; the
money is one vertical at a time. Any candidate framed as "a better clipboard" is dead on arrival.

**2. Zapier's absence is a better signal than Zapier's presence.**
Every candidate below sits on a pair where at least one side returns 404 from the Zapier directory.
That is not proof of opportunity — it is proof that the cheap generic answer does not exist, which
is the *first* thing the brief asked me to check. Where both sides were on Zapier I killed the
candidate outright (see the kill list).

**3. The valuable half is never the transport — it is the *verdict*.**
In every live candidate below, the file moves easily. What is hard is deciding *what the row means*:
is this deduction valid, is this commission short-paid, which of 60 supplier columns is the SKU,
which prevailing-wage classification does this hour belong to. **This is judgement work priced as
data entry**, which is precisely the overhang. It is also why Zapier structurally cannot take it:
a Zap has no opinion.

---

# CANDIDATES

---

## TT-1 — Distributor deduction adjudicator for small CPG brands

**1. Name.** Upload a UNFI or KeHE remittance PDF and get back coded QuickBooks credit memos plus a
per-line verdict on which deductions are invalid and a ready-to-file dispute packet for each.

**2. The artifact.** Two files per remittance cycle: (a) a QBO-importable credit-memo file with GL
coding and promotion linkage already applied; (b) a per-deduction dispute packet PDF containing the
deduction line, the matched PO/BOL/invoice, the authorised promo (or the absence of one), and the
dispute letter — the thing the brand pastes into the distributor portal before the window closes.

**3. Evidence — T1 + T2.**
- **T1, money moving now:** OverDeduct sells this manually and by software at **"$49/month (Starter)
  or $99/month (Pro)"** self-serve and **"25% of what's actually recovered — no minimum, no
  retainer"** done-for-you (`overdeduct.com/faq`, fetched 2026-08-27). A 25% contingency is revealed
  willingness-to-pay in its purest form.
- **T1:** Promomash prices its Deductions module explicitly on volume — *"Plans and pricing are based
  on monthly deduction invoice (DI) volume to process"* (`promomash.com/plans`, fetched 2026-08-27).
- **T1:** Vividly's Deduction Scanner *"supports more than 50 common backup sources, including UNFI,
  KeHE, Walmart, Target, McLane"* and describes today's workflow as *"Your Accounting teams might be
  combing through hundreds or thousands of pages of PDF files and adding up totals by hand."* A named
  customer case study title claims *"Health-Ade recovered 700k"* (`govividly.com/deduction-scanner`,
  fetched 2026-08-27).
- **T2, dated volume figure:** *"A remittance containing 50–200 deduction rows can easily take 2–6
  hours per cycle—and that's just for processing the deductions"* — RemitParse, **March 2026**
  (`remitparse.com/blog/kehe-deductions-explained`).
- **T2, dated:** *"hundreds of deduction line items per month"*, each needing documentation retrieval,
  PO cross-reference and timely filing — Glimpse, **July 2026**
  (`tryglimpse.com/post/unfi-kehe-supplier-deductions`).
- **Zapier check: UNFI 404, KeHE 404.** Zapier cannot touch this. Confirmed 2026-08-27.

**4. The clock.** Two things. (a) Cheap, accurate LLM extraction of multi-page distributor remittance
PDFs became economic in the last ~18 months — the whole entrant cohort below is dated 2025–2026, not
earlier. (b) The distributor deduction codes and portal flows changed in 2026 per Glimpse (Jul 2026),
which is why the *"monthly cadence may no longer catch everything before the dispute window closes"*
— dispute windows are *"often 30 to 90 days"* (overdeduct.com/faq).

**5. First ten users.** **Channel named, individuals not named.** Startup CPG runs a free public
Slack with **"30,000+ members"** and **"10 city hubs"**, joined by newsletter signup with no
gatekeeper (`startupcpg.com/community`, fetched 2026-08-27). That is a genuine cold-start channel for
exactly this buyer — emerging CPG founders — and it costs nothing to enter. **I could not name ten
individual members** because I could not reach Reddit or the Slack archive. Distribution Lead must
close this before the candidate advances.

**6. Gate check.**
- G1 distribution — **PASS with a caveat.** Startup CPG Slack is a real, free, named, on-problem
  channel of 30,000+. Caveat: no named individuals yet.
- G2 observable demand — **PASS (T1).** Six vendors selling this today, one on 25% contingency.
- G3 buildable — **PASS.** Both sides are files. No API dependency on UNFI or KeHE. Standing Law 11 is
  satisfied better here than anywhere else on this surface.
- G4 self-verifiable in 14 days — **PASS.** Buy or obtain three real remittance PDFs and score our
  verdict accuracy against a human's. Needs no stranger's cooperation beyond obtaining sample files.
- G5 clock — **PASS.** Entrant cohort all dated 2025–2026.

**7. What already exists.** Vividly (deduction scanner, 50+ backup sources), Promomash (volume-priced
Deductions module), TrewUp, Glimpse, RemitParse, OverDeduct. **This is the honest problem: six
entrants, at least four of them 2025–2026 indies.** Vividly and Promomash sell up-market to funded
brands; OverDeduct at $49/$99 is already sitting on the low end. **Inadequacy we could attack:** every
one of them stops at *extraction and categorisation*. None publicly claims to render a **validity
verdict** with the matched backup attached — the actual thing that recovers money. That is the
judgement half, and it is exactly what got cheap.

**8. Price signal.** $49–$99/month self-serve; **25% of recovered dollars** done-for-you; Promomash
and Vividly quote-gated (higher).

**9. Confidence: 6/10.** Best evidence on the surface, worst competitive picture. It would be
dishonest to score this higher with six entrants already in the water.

---

## TT-2 — Carrier commission statement reconciler for small insurance agencies

**1. Name.** Upload this month's 10–40 carrier commission statements plus your agency's book-of-business
export, and get back a list naming every policy that was paid short, paid late, or never paid at all.

**2. The artifact.** One reconciliation report per month with three named lists — *short-paid*,
*missing*, *unexpected* — each line carrying policy number, insured, expected vs received, carrier
and statement date; plus a per-carrier chase list formatted to send to the carrier's commission desk.

**3. Evidence — T1 + T2.**
- **T1:** AgencyBloc sells Commissions+ against exactly this, describing today's method as
  *"comparing spreadsheets line-by-line and hoping your payments are right"* and claiming it
  *"cut time spent on commission processing by 75-95%"*
  (`agencybloc.com/software-solutions/commissions-processing/`, fetched 2026-08-27). Commissions+ is
  quote-priced on transaction volume — i.e. money is moving, at an undisclosed number.
- **T1:** Comulate sells the same job to *"Large insurance brokers (top 100)"*, claiming *"90% Less
  manual work"* and processing *"100% of carrier statements"* out of the box, integrating to AMS360,
  BenefitPoint and Epic (`comulate.com`, fetched 2026-08-27). **The incumbent has publicly drawn its
  own line at the top 100 brokers.** Everyone below that line is unserved by it.
- **T1:** Commission Tracker sells a standalone product for this (commission-tracker.com — the site
  403s to this crawler; its existence and positioning are visible in its indexed pages, **pricing
  UNVERIFIED**).
- **T2:** The pain is universal across carriers by construction — *"Every carrier sends commission
  statements in a different format—some arrive as PDFs, others as CSV files or Excel spreadsheets,
  with varying data fields and naming conventions"* (invoicedataextraction.com, insurance commission
  statement OCR guide, 2026).
- **Zapier check: AMS360 404, Applied Epic 404.** AgencyBloc is on Zapier (200) but with generic
  CRM triggers, not statement reconciliation. Zapier does not solve this.

**4. The clock.** Applied Systems shipped **Epic Autofill on/around 2026-07-16**
(`www1.appliedsystems.com/en-us/blog/posts/insurance-document-automation/`, dated 2026-07-16) —
the AMS vendor itself has started repricing document re-keying. That is a *warning* for the adjacent
ACORD-entry candidate (killed below) and a *clock* for this one: the vendor's own move validates that
LLM document handling in insurance became viable in 2026, and Autofill addresses inbound ACORD/policy
documents, **not** commission reconciliation.

**5. First ten users.** **Could not name them.** The natural venues — r/InsuranceAgent, agency-owner
Facebook groups, InsuranceForums.net — were unreachable (Reddit blocked; the others not indexed into
my reachable set). This is a real gate-1 hole. The honest read is that insurance agency owners are
*not* assembled in a free public channel the way CPG founders are, which is a structural distribution
weakness, not a research gap.

**6. Gate check.**
- G1 distribution — **FAIL / UNPROVEN.** No named channel, no named people. This is the gate that
  should kill it unless the Distribution Lead finds something I could not.
- G2 observable demand — **PASS (T1).** Three paid vendors, one enterprise-only by its own admission.
- G3 buildable — **PASS, and unusually cleanly.** Both sides are files the agency already possesses.
  Zero API exposure to Vertafore or Applied. Standing Law 11 fully satisfied.
- G4 self-verifiable — **PASS.** Reconciliation accuracy is testable against synthetic and obtained
  statements alone.
- G5 clock — **PASS.** Vendor's own 2026-07-16 move.

**7. What already exists.** AgencyBloc Commissions+ (quote-priced, bundled into an AMS you must
adopt), Comulate (top-100 brokers, explicitly), Commission Tracker (standalone, pricing unverified).
**Inadequacy:** AgencyBloc requires you to run your agency on AgencyBloc; Comulate requires you to be
enormous. A 3–15 person agency running on AMS360 or a spreadsheet has neither option and is the
buyer, the user and the payer simultaneously.

**8. Price signal.** All quote-gated. **No public price found — UNVERIFIED.** That is itself a
finding: nobody sells this to a small agency at a listed price.

**9. Confidence: 5/10.** Cleanest build, cleanest API story, best buyer alignment on the entire
surface — and it fails gate 1, which per Standing Law 4 is the only gate that matters. **Recommend
triage kills it unless the Distribution Lead can name a channel.**

---

## TT-3 — Supplier catalogue interpreter for Shopify merchants

**1. Name.** Drop in a supplier's price list — any format, any season — and get back a Shopify-ready
product file with the taxonomy category, variant options, and titles already decided, not just the
columns renamed.

**2. The artifact.** A validated Matrixify/Shopify-format import file plus a diff report showing every
judgement the tool made (which column was the SKU, which products are variants of one another, which
Shopify Standard Taxonomy category was assigned and why, which rows were rejected and why).

**3. Evidence — T1 + T2, with a named dated user.**
- **T1, and the incumbent's own reviewers describe the residual pain:** Matrixify —
  **1,431 reviews, 4.9★, 96% five-star**, priced **Free / $20 / $50 / $200 per month**
  (`apps.shopify.com/excel-export-import`, fetched 2026-08-27). Its most recent review, from the
  store **Rare Beauty Brands Wholesale on 2026-08-06**, reads verbatim: *"It's worked well every time
  I need to make an import/export. **It's still a lot of work to be done manually**, but Shopify
  doesn't have a free bulk import tool, so I'm using this."* A five-star reviewer of the market leader
  stating the job is still manual is about as clean a wedge statement as this surface produces.
- **T2, dated, quantified:** manual supplier-file reformatting takes *"a day or two"* and consists of
  *"renaming columns, splitting and merging cells, fixing units, guessing which field is the SKU, and
  copy-pasting until it roughly matches Shopify's import template"* — repeated *"each season from
  scratch"* (Apimio, published **May 2026, updated June 2026**).
- **T2, disconfirming and important:** the one entrant that already sells AI column mapping into
  Shopify — Apimio PIM — has **1 review, 2.0★**, at **$199/month (Basic) / $399/month (Advanced)**,
  listed since **2021-02-02**, and its single reviewer writes *"the prices listed are wrong. It costs
  much more"* (`apps.shopify.com/apimio-pim`, fetched 2026-08-27). **The AI-mapping wedge has been
  attempted and has no traction at PIM pricing.** Either the price is wrong or the framing is.
- **Zapier check:** Shopify is on Zapier (200) but bulk catalogue transformation is not expressible as
  a Zap; Matrixify owns the mechanical half and does not do the semantic half.

**4. The clock.** **Shopify Standard Product Taxonomy.** Versions listed run **2024-07, 2024-10,
2025-03, 2025-09, 2025-12, 2026-02, 2026-05, 2026-08** (`shopify.github.io/product-taxonomy`, fetched
2026-08-27). Since mid-2024 every product needs a taxonomy category, and the taxonomy has been
revised roughly quarterly ever since. **Assigning it is a per-product judgement call that did not
exist before July 2024 and that changes four times a year** — a mechanical importer structurally
cannot keep up, and a merchant re-doing it by hand every season is the two-tabs problem with a
regulator-like clock attached.

**5. First ten users.** **Named, and this is the strongest gate-1 story in the report.** The Shopify
App Store is itself the channel — install counts are public demand data and the marketplace is the
cold-start route (Master Prompt §5.8). Beyond that, **Matrixify's public review feed names real
stores with dated statements of the pain**, and those stores are directly reachable:
- **Rare Beauty Brands Wholesale** — 2026-08-06 — *"It's still a lot of work to be done manually"*
- **My Hometown Vermont** — 2026-07-07 — print-on-demand, *"hundreds of variations on templates…
  organizing them into coherent collections and categories is even harder"*
- **Lawn and Pets** — 2026-06-20 — prepares product/variant/image/pricing/SEO files outside Shopify
- **Cambridge University Press Bookshop** — 2026-06-18 — *"making sure the uploads have the right
  column headers"*
- **Carroll's Staging** — 2026-06-18
That is five named storefronts with dated evidence of the exact pain, from one page. The same page
paginates to 1,431 of them. **Ten is a scroll away.**

**6. Gate check.**
- G1 distribution — **PASS, strongest on the surface.** App Store listing + 1,431 dated named leads.
- G2 observable demand — **PASS (T1).** $20–$200/mo incumbent with 1,431 reviews.
- G3 buildable — **PASS.** Input is an uploaded file; output is a file. Shopify Admin API is used only
  for the optional push, and Shopify has no history of revoking app access for this use.
- G4 self-verifiable — **PASS.** Take twenty real supplier files, score our category/variant/SKU
  decisions against a human's. Fourteen days is generous.
- G5 clock — **PASS.** Taxonomy since 2024-07, revised through 2026-08.

**7. What already exists.** Matrixify ($20–$200/mo, 1,431 reviews) — **mechanical only, and adequate
at being mechanical; do not try to beat it there.** Apimio ($199/$399, 1 review) — attempted the
semantic wedge, no traction. DataFeedWatch/Feedonomics — outbound channel feeds, not inbound supplier
onboarding. **Inadequacy:** nobody sells the judgement layer at a merchant price point. The gap is
priced, not technical.

**8. Price signal.** Merchants pay **$20–$200/month** for the mechanical half today. Apimio's failure
at $199 suggests the semantic layer must land **at or under ~$49/month**, or be priced per supplier
file.

**9. Confidence: 7/10.** Highest on this surface. It wins on gate 1 and gate 4, which are the two the
Postmortem says the old format got wrong. The Apimio data point is a real warning and is reported here
rather than smoothed over.

---

## TT-4 — Property-management ledger translator (AppFolio/Buildium → QuickBooks)

**1. Name.** Turn a property-management system's general-ledger export into per-entity QuickBooks
journal entries that actually match the owner's books, every month, without re-keying.

**2. The artifact.** A per-owner-entity QuickBooks import file (IIF/CSV/JE) with the PM system's chart
of accounts already remapped, trust vs operating split, and owner distributions reconciled — plus an
exceptions list of every transaction the mapping could not decide.

**3. Evidence — T2, thin and vendor-authored. Flagged.**
- **T2, dated, quantified:** *"every month, someone on your team exports data from AppFolio,
  reformats it, and imports it into QuickBooks"*; for firms with 100+ properties the manual approach
  consumes **"8 to 15 hours a month"**; and *"The two platforms were not designed to talk to each
  other natively"* — Numetix, **2026-02-19**
  (`numetix.ai/resources/appfolio-quickbooks-dont-sync-pm-firms-fix-it`).
- **T2, durability evidence:** BiggerPockets thread **2016-11-26**, 5 replies: *"Is anyone integrating
  AppFolio with QB or Xero (without re-keying everything)?"* — the OP resorted to *"converting an
  AppFolio PDF to CSV and imported it into Xero"*
  (`biggerpockets.com/forums/52/topics/382495`). **Ten years old and still unanswered natively** —
  which is the "forever" the brief asked for, and also a warning (Master Prompt G5: "this has always
  been a problem" is a warning, not an opening).
- **Zapier check: AppFolio 404, Buildium 404, Rent Manager 404.** All three absent.

**4. The clock.** **Weak, and I will not dress it up.** The only defensible clock is the general
collapse in cost of semantic mapping. I found **no dated 2024–2026 change specific to this pair.**
Per Gate 5 this is close to an automatic fail.

**5. First ten users.** **Could not name them.** BiggerPockets is fetchable and its forums carry real
usernames with dates, but its search endpoint 404s to this crawler and the one thread I reached is
from 2016. Channel is plausible (BiggerPockets forums); individuals unnamed.

**6. Gate check.**
- G1 distribution — **UNPROVEN.** BiggerPockets is a plausible free channel; no names.
- G2 observable demand — **WEAK PASS (T2 only, and vendor-authored).** No paid competitor with a
  public price found. That absence is a verdict, not an opening (Standing Law 2).
- G3 buildable — **PASS.** File in, file out; no API dependency.
- G4 self-verifiable — **PASS.**
- G5 clock — **FAIL.** Ten-year-old unanswered forum thread and no dated change.

**7. What already exists.** Bookkeeping services and a thin layer of AI-SEO integration vendors
(Numetix, smbaccountants). No product with a public price. AppFolio's own GL export is the incumbent
"solution."

**8. Price signal.** **None found — UNVERIFIED.** Nobody sells this at a listed price, which is the
strongest argument against it.

**9. Confidence: 4/10.** Include for completeness. **Recommend triage kills on G5.**

---

## TT-5 — VMS timesheet reconciler for staffing agencies

**1. Name.** Reconcile the hours a client's VMS portal approved against the hours your agency actually
paid, per contractor, per week, before you invoice.

**2. The artifact.** A per-client, per-cycle exception report: every contractor whose VMS-approved
hours, bill rate or cost centre disagrees with the agency's back-office record, with the delta in
dollars and the specific line to dispute.

**3. Evidence — T2.**
- **T2, dated:** VMS exports arrive as *"CSV, Excel, or PDF depending on the platform"* and *"the
  format varies not only between VMS providers but between client configurations within the same
  platform"*; reconciliation is *"line-by-line comparison that consumes hours per billing cycle per
  client"* — invoicedataextraction.com, **2026-04-05, updated 2026-05-09**.
- **T2, population size:** *"According to American Staffing Association quarterly data, U.S. staffing
  companies employed an average of two million temporary and contract workers per week in the fourth
  quarter of 2025"* (same source, citing ASA — **ASA figure itself UNVERIFIED by me**).
- **Zapier check: SAP Fieldglass 404, Beeline 404, Bullhorn 404 (five slugs tried).** The entire
  chain is absent from Zapier.

**4. The clock.** **Weak.** No dated 2024–2026 change found specific to VMS reconciliation.

**5. First ten users.** **Could not name them.** r/staffing was unreachable.

**6. Gate check.**
- G1 distribution — **UNPROVEN.** No named channel.
- G2 observable demand — **WEAK PASS (T2 only).** No paid competitor with public pricing found.
- G3 buildable — **PASS.** All inputs are exports the agency already downloads.
- G4 self-verifiable — **PASS.**
- G5 clock — **FAIL.** Nothing dated.
- **Discriminator 4 (the brief's own): FAIL.** The person doing the shuttling is a back-office
  employee whose time the agency owner has already decided to buy. The buyer is not the sufferer.

**7. What already exists.** Back-office platforms bundle it (Bullhorn Back Office, Avionté). Nothing
standalone with a public price found.

**8. Price signal.** **None found — UNVERIFIED.**

**9. Confidence: 3/10.** **Recommend triage kills** — fails G5 and the brief's own discriminator 4.
Reported because the Zapier-absence pattern is unusually complete and someone may see something I do
not.

---

## TT-6 — Certified payroll and fringe-fund remitter for small union/prevailing-wage contractors

**1. Name.** Take one week's payroll register and produce every certified-payroll upload and every
benefit-fund remittance form that week requires, each in the format its own recipient demands.

**2. The artifact.** A weekly bundle: the LCPtracker/eMars-format upload file, the WH-347 (or state
equivalent), and one completed remittance form per trust fund — health & welfare, pension, annuity,
apprenticeship, industry fund — each on that fund's own template, with hours already allocated to the
right classification and fringe credits applied.

**3. Evidence — T2, and I could not get as deep as I wanted.**
- **T2:** Contractors *"must complete a separate report for each Local Union with which they have a
  contribution obligation under a collective bargaining agreement and for each contract, jurisdiction,
  and industry"* — Sheet Metal Workers' National Pension Fund remittance instructions
  (`smwnpf.org/forms/remittance-report-form-instructions/`). Forms are fund-specific by construction.
- **T2:** Contractors with 200+ union workers reportedly spend *"10-15 hours weekly on manual union
  payroll processing using spreadsheet-based systems"* (industry guides, 2026 — **vendor-authored,
  figure UNVERIFIED**).
- **Zapier check: LCPtracker 404.** The mandated receiving system is absent from Zapier.
- **Structural refusal:** LCPtracker sells to the *awarding agency*, not the contractor — the
  contractor is a compelled user with no purchasing power over it. It has *"FedRAMP® Authorization"*
  (`lcptracker.com`, fetched 2026-08-27), which tells you who its customer is. **It will never
  integrate with the contractor's payroll system, because the contractor is not its buyer.** That is
  the permanent permission the brief asked for.

**4. The clock.** The DOL Davis-Bacon final rule ("Updating the Davis-Bacon and Related Acts
Regulations") published **2023-08-23**, effective **2023-10-23**, and the IRA prevailing-wage and
apprenticeship final regulations of **June 2024**, together pulled a large new population of
contractors — solar, EV charging, energy retrofit — into weekly certified payroll for the first time.
**Both dates are UNVERIFIED by me: federalregister.gov redirects this crawler to an unblock gate.**
Triage must verify before this advances. If the dates hold, this is the best clock on the surface.

**5. First ten users.** **Could not name them.**

**6. Gate check.**
- G1 distribution — **UNPROVEN.**
- G2 observable demand — **WEAK PASS (T2).** eBacon, Points North and Miter all sell union/certified
  payroll, which proves money moves; none of their prices were reachable.
- G3 buildable — **PASS.** Payroll register in (file), fund forms out (files). No API anywhere.
- G4 self-verifiable — **PASS.** Fund forms and WH-347 are public; correctness is checkable alone.
- G5 clock — **PASS IF the 2023/2024 dates verify.**
- **Construction-adjacency check:** this is **not** on the killed list. The ledger killed claims/
  entitlement, notice deadlines, the Procore API layer, clause extraction and delay attribution. None
  of those is this. It also needs **no credential** — the contractor signs their own WH-347, we do
  not sign anything (clears Standing Law 6 and the failure mode that killed cycle 0).

**7. What already exists.** eBacon, Points North, Miter, Foundation, and payroll-service add-ons.
**Inadequacy: unverified** — I could not reach their pricing or feature boundaries. Triage should
treat "is this already adequately served?" as the open question.

**8. Price signal.** **None obtained — UNVERIFIED.**

**9. Confidence: 5/10.** Best structural story on the surface (compelled user, vendor that will never
integrate, regulatory clock, zero API exposure, no credential) and the weakest evidence, purely
because my search budget ran out before I could price the incumbents. **Recommend triage sends this
one back for a 30-minute evidence top-up rather than killing it.**

---

## TT-7 — Retailer new-item setup form filler for CPG brands

**1. Name.** Fill in every retailer's and distributor's new-item setup spreadsheet from one product
record, instead of retyping the same sixty facts into six different forms.

**2. The artifact.** One completed new-item form per destination — UNFI, KeHE, a regional chain, Faire,
Shopify — each on that destination's own template, units converted, fields named their way, with a
flagged list of the facts no form could answer.

**3. Evidence — T2, weakest in the report. Reported as a lead, not a candidate.**
- **Zapier check: UNFI 404, KeHE 404.** Same absence as TT-1.
- **Same buyer and same free channel as TT-1** — Startup CPG Slack, 30,000+ members
  (`startupcpg.com/community`, 2026-08-27) — which is the only reason it is in this report at all: it
  is a second product for a channel we would already be in.
- **I found no dated thread, no price, and no competitor for this specific job.** Per Standing Law 2
  and the T4 line of the evidence ladder, **absence of competitors is not evidence** and my own
  reasoning that founders must hate this is **not evidence**.

**4. The clock.** None found.

**5. First ten users.** Same channel as TT-1. No individuals named.

**6. Gate check.** G1 — plausible (shared with TT-1). G2 — **FAIL. T4 evidence only.**
G3 — pass. G4 — pass. G5 — **FAIL.**

**7. What already exists.** Unknown. Not established.

**8. Price signal.** **None. UNVERIFIED.**

**9. Confidence: 2/10.** **Kill it.** Included only so the Triage Manager can see the shape of an
attachment-to-a-good-channel idea and reject it explicitly. It fails the exact test the Postmortem was
written about.

---

## TT-8 — Royalty statement generator for micro-presses and multi-author indie publishers

**1. Name.** Turn a month of KDP, IngramSpark, Draft2Digital and Audible sales reports into a per-author,
per-collaborator royalty statement and a payment list.

**2. The artifact.** One PDF royalty statement per author/narrator/co-writer, with units, territory,
currency conversion and contractual split applied — plus a single payment CSV.

**3. Evidence — T1 on the adjacent half, nothing on this half.**
- **T1, adjacent:** indie authors demonstrably pay to aggregate these reports. **Book Report:**
  $19/$29/$49/$99/$249 per month by earnings band, free under $1,000/mo, covering *"up to ten leading
  publishing platforms"* including KDP, Ingram, Google Play, Kobo and D2D (`getbookreport.com`,
  fetched 2026-08-27). **ScribeCount:** $5.99 / $16.99 / $24.99 / $34.99 per month by income band,
  *"All 40+ publishing platforms"* (`scribecount.com/pricing`, fetched 2026-08-27).
- **T1, the other half, enterprise only:** MetaComet sells Royalty Tracker and a Sales Aggregator to
  publishers, *"trusted by 190+ companies"*, no public pricing (`metacomet.com`, fetched 2026-08-27).
- **The gap:** Book Report and ScribeCount stop at a **dashboard for one owner**. MetaComet does
  **statements and payments** but sells to real publishing houses. Nothing found in between for the
  1–50-author micro-press.
- **Structural refusal:** Amazon KDP has **no public royalty API** and never has. Reports are manual
  CSV/XLSX downloads. That is permanent permission *and* Standing Law 11 compliance — we would never
  depend on an API that can be revoked.

**4. The clock.** None found specific to this pair.

**5. First ten users.** **Could not name them.** The named channels — the 20BooksTo50K Facebook group,
KBoards' Writers' Cafe, r/selfpublish — are real and free but I could not reach any of them to pull
handles or verify sizes. **All membership figures I might quote would be invented, so I quote none.**

**6. Gate check.**
- G1 distribution — **UNPROVEN.** Channels named, sizes unverified, people unnamed.
- G2 observable demand — **SPLIT.** T1 for the aggregation half (which is already well served at
  $5.99–$249/mo). **T4 only for the statement half** — I am reasoning that micro-presses need it, and
  reasoning is not evidence.
- G3 buildable — **PASS.** Downloads in, PDFs out.
- G4 self-verifiable — **PASS.**
- G5 clock — **FAIL.**

**7. What already exists.** Book Report and ScribeCount, both cheap and **adequate for aggregation —
so the aggregation product is dead.** MetaComet for statements, enterprise-priced. The unserved slice
is real but unevidenced.

**8. Price signal.** $5.99–$249/month for the adjacent half. **Nothing for the statement half.**

**9. Confidence: 3/10.** **Recommend kill** on G2/G5 unless a later cycle can evidence the statement
half. Recorded so cycle 2 does not re-research it.

---

# KILLED ON SIGHT — checked, and dead. Do not re-research.

Discriminator 1 says check Zapier first, every time, and say so explicitly. Here is where that check,
or an adequate incumbent, killed the idea outright.

| Pair | Why it is dead | Evidence, fetched 2026-08-27 |
|---|---|---|
| **Planning Center Giving → QuickBooks Online** | **Zapier solves it natively, both sides.** Planning Center 200, QuickBooks 200 in the app directory, with published multi-step Zaps for this exact flow. | `zapier.com/apps/planning-center/integrations/quickbooks` |
| **Restaurant distributor invoices → accounting/COGS** | **Adequate incumbent at a public price.** MarginEdge is **$350/month per location**, unlimited invoice processing and bill pay, no contract, 10% off annual. xtraCHEF was absorbed by Toast. There is no room under $350 that an LLM opens up. | `marginedge.com/pricing` |
| **Bank/credit-card statement PDF → accounting** | **Adequate and cheap.** DocuClipper: **$20/mo (60 pages), $111/mo (640 pages), $360/mo (2,000 pages)**, exporting QBO/OFX/QFX/QIF/IIF into QuickBooks, Xero, Sage, NetSuite and Dynamics. Crowded and solved. | `docuclipper.com/pricing` |
| **Amazon / Shopify payouts → QuickBooks or Xero** | Solved by A2X and peers for years; both platforms are first-class Zapier apps. Nothing newly cheap changes it. | Zapier: shopify 200, quickbooks 200 |
| **TikTok Shop ↔ Shopify inventory** | Native TikTok sales channel for Shopify plus a crowded app tier (Sumtracker, QuickSync, Prediko). Overselling complaints are real but the market has ≥4 paid answers. | `seller-us.tiktok.com/university` FAQ; multiple Shopify apps |
| **ACORD forms / carrier documents → Applied Epic** | **The incumbent just repriced it.** Applied Systems shipped **Epic Autofill**, announced **2026-07-16**, explicitly to stop CSRs re-keying *"ACORD forms, carrier documents, benefits documents, and endorsement emails."* Competing with the AMS vendor inside its own AMS is unwinnable for a cold-start operator. | `www1.appliedsystems.com/.../insurance-document-automation/`, dated 2026-07-16 |
| **Recruiter CV → client-branded submission** | **Adequate, and brutally priced.** Candidately sells it at **$1 per exported resume**, unlimited users, with Bullhorn export; client portal $99/mo + $49/mo per extra seat. Nothing left to win. | `candidately.com/pricing` |
| **Indie author multi-retailer sales dashboard** | **Adequate and cheap.** Book Report $19–$249/mo (free under $1k/mo earnings); ScribeCount $5.99–$34.99/mo across "40+ platforms." | `getbookreport.com`, `scribecount.com/pricing` |
| **Payer portal (Availity/Waystar) ↔ dental/medical PM (Dentrix, Eaglesoft, Open Dental)** | Zapier absent on all five (404) and the pain is real — but **G3 fatal**: write access into Dentrix/Eaglesoft runs through paid, gated vendor developer programmes controlled by Henry Schein and Patterson, plus PHI handling. This is the Procore situation from the ledger, in a different industry. | Zapier 404 ×5; Standing Law 11 |
| **Auto-dealer DMS (CDK / Reynolds) ↔ anything** | **G3 fatal and precedented.** These vendors have litigated to block third-party data access. A better-funded company than us lost that fight. Standing Law 11 applies directly. | Not researched further, by design |
| **Any "better clipboard" / generic cross-tab copier** | **Dead category.** Magical has 300,000 Chrome users at 4.4★ and still could not monetise horizontally — it has pivoted to demo-gated healthcare vertical software in 2026. | Chrome Web Store; `getmagical.com/pricing` |

---

# WHAT THIS SURFACE ACTUALLY TAUGHT US

**1. The two-tabs problem is real and enormous — and almost entirely already priced.** Of roughly
twenty pairs examined, eleven died on discriminator 1 within minutes. The brief's instruction to
check Zapier first was worth more than any other single rule; it is the cheapest kill available and
should be promoted into the general triage checklist.

**2. Where it is not priced, it is because one vendor's customer is not the sufferer.** LCPtracker
sells to awarding agencies and is FedRAMP-authorised; the contractor keying into it has no leverage.
Comulate sells to the top 100 brokers; the 8-person agency has no option. AppFolio sells to the
property manager; the owner's accountant has no path. **"Whose customer is the person doing the
typing?" is a better discriminator than "do both vendors have an API?"** — I propose it as a standing
question for future two-tabs work.

**3. The three candidates worth advancing are TT-3, TT-1 and TT-6, in that order.**
- **TT-3 (Shopify supplier catalogue)** because it is the only one that passes gate 1 with named,
  dated leads and a marketplace that *is* the channel.
- **TT-1 (CPG deductions)** because the evidence is T1 and the channel is a free 30,000-member Slack —
  discounted hard for six existing entrants.
- **TT-6 (certified payroll / fringe remittance)** because the structure is perfect and the evidence
  is merely absent rather than negative. It deserves 30 more minutes, not a kill.

**4. Honest failure to report.** The brief asked for named first-ten users per candidate. **I produced
them for exactly one candidate (TT-3).** Reddit and Upwork — the two sources the brief named first —
were both hard-blocked to this crawler, and the WebSearch budget ran out at 200/200 partway through.
Per Standing Law 5, seven of these eight candidates do not yet have a channel. That is the finding,
and it should be weighed against them rather than excused.

**5. Proposed 13th surface, recorded per the brief's invitation: "compelled users."** Populations
legally or contractually required to key data into a system that someone else buys — certified payroll
portals, state childcare subsidy portals, EVV aggregators, vendor compliance portals, court e-filing.
The refusal to integrate is permanent by construction (the sufferer is not the customer), the
receiving format is usually a published file spec rather than an API, and the population is
enumerable from the mandate itself. TT-6 is the only one I reached; the surface looked wider than my
remaining budget.
