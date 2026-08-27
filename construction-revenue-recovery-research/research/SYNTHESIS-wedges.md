# SYNTHESIS — CANDIDATE WEDGES

**Synthesis Manager · 19 August 2026**
**Inputs:** BRIEF.md · NOTES-running.md · CM-A · CM-B · CM-C · CM-D · SCORES.csv · raw/01–17
**Purpose:** convert the evidence base into 8 rigorously-specified candidate wedges, ranked, for red-team attack.

Confidence labels used throughout: `SOURCED` (published figure + URL in the corpus) · `DERIVED` (arithmetic on
sourced inputs) · `ASSUMPTION` (basis stated) · `UNVERIFIED`.

---

## 0. THE CONSTRAINT SET EVERY WEDGE IS SCORED AGAINST

Restated from NOTES-running.md and the four CM syntheses. A wedge either respects these or explicitly buys its
violation.

| # | Constraint | Source of the constraint |
|---|---|---|
| C1 | Clause extraction, notice detection and notice drafting are **commoditised or owned** | Trunk Tools free tool (14 categories, no account); Procore Contract Review agent GA 21 May 2026; Document Crunch agentic notices since 9 Jun 2026, Trimble-owned since 4 Apr 2026 ($246.4M, $207.0M goodwill) |
| C2 | **Responsibility attribution is standards-blocked** | AACE RP 29R-03 §1.2(f), §1.3(c), §1.1; Steelray states it on its own product page |
| C3 | **EOT ≠ money** | SCL Protocol 2nd ed., Core Principle 12 |
| C4 | **Quantum cannot ship standalone** — it sits downstream of causation | CM-B §3.1; must bundle evidence linking (e) + sufficiency (f) + quantum (h) |
| C5 | **No Procore API dependency** | Trunk Tools access revoked Sept 2025; Developer Policy eff. 30 Sep 2025 forbids parse/database-build/AI-training |
| C6 | **V1 must never contact the owner** | Smith Currie Jun 2025: contractors deliberately suppress notice to protect relationships. raw/15 §11 Q4 |
| C7 | **Inbound/SEO falsified five times** | No G2/Capterra category · no Procore-review articulation · zero contech funding · non-English markets articulate it as legal complexity · r/ConstructionManagers hostility |
| C8 | **Per-seat capped $50–150/user/mo; $29–300/mo is the demoware graveyard; $5,000/mo fails below ~$150M revenue** | DocuSign IAM $45/50/80; Copilot $18–30; Magra/Lexilio/DCB/ClaimMaster all $29–300 with zero named customers; CFMA 0.26% tech purse |
| C9 | **Value-capture ceiling on a $412k recovery is $5,000–$30,000 (1.5–8%)** | Take scales with downside borne; consultants capture 1.2–3.6% of disputed sum bearing neither capital nor delivery risk |
| C10 | **Solo founder** | No large team, no deep integrations, no multi-year procurement, no proprietary dataset, no 24/7 staffing pre-revenue |
| C11 | **A missing feature is not white space without paid-for pain** | BRIEF.md |

**The two facts that generate most of the wedge space:**
1. **Nobody exceeds 1 on dimensions 14 (evidence_completeness), 15 (recoverable_dollar_estimation) or
   16 (claim_package_generation)** — across 23 scored entities including the DIY substitute stack, which scores
   **0** on evidence_completeness. (CM-A §1.3, SCORES.csv)
2. **The pipeline is occupied at both ends and hollow in the middle-back.** The void is not a stage, it is the
   **seam (c)→(d)→(h)**. Gather has c/d/e/f and refuses h. Easyclaim has h/j and has no a–g. Magra claims all
   and ships none. (CM-B §1)

---

## 1. THE EIGHT WEDGES

*Presented in rank order (see §2). Wedge 6 is owner/defence-side; Wedge 3 is a pure
productised service; Wedge 4 attacks the pricing step rather than the evidence step; Wedge 5 is deliberately
unfashionable with no AI in the pitch; Wedge 7 is the obvious idea evaluated honestly; Wedge 8 is the
deliberately WEAK control case.*

---

# WEDGE 1 — **MATTER ZERO**
### *Same-day linked chronology, notice/entitlement register and missing-evidence schedule from a raw document dump, sold per matter to small and mid-size claims consultancies and DOT on-call primes.*

**1. Name & description.** Matter Zero. The consultancy sends the file dump it already receives from counsel;
it gets back, same day, the linked chronology, the notice and entitlement register, an evidence-completeness
score per event, a missing-evidence schedule, and a source-cited exhibit set. The human analyst still makes
every judgement call. No verdict, no attribution, no owner contact.

**2. The specific missed-revenue problem, with frequency and value.**
The problem is **not** the contractor's lost claim — it is the consultancy's unrecovered analyst hours.
- **200–600 hours of document review and chronology per $5–25m matter**, out of 600–1,650 total hours
  (`DERIVED`, raw/11 §12 Q2 — a model at $400/hr blended, **not a citation**). Value of that block:
  **$80,000–$240,000 per matter.** Confidence: **HIGH on the hours' existence, MEDIUM on the range.**
- **Blended realised rates are `SOURCED`:** Exponent published card $225–$1,375/hr, derived blended ~$396/hr;
  **FTI FLC $442/hr in 2025 (up 13.3% YoY) at 57% utilisation**; Diales 71.6% utilisation.
- **Diales — the only listed pure-play — turned £43.0m revenue into £1.4m underlying operating profit: a
  3.3% margin.** `SOURCED`. That is what "no product leverage" looks like on a P&L, and it is the single
  cleanest proof in the program that these hours are real, paid, and unproductised.
- **Nobody markets a chronology product.** Across HKA, BRG, Ankura, Secretariat, FTI, Exponent and Arcadis
  service pages, not one. HKA's own analytics page says it *implements* standard stacks rather than building.
  `SOURCED` (absence, checked at seven firms).
- **Arcadis is priming its own clients:** AI-assisted eDiscovery "compress[es] weeks of document analysis into
  days, **cutting costs by as much as 85%**." `SOURCED`, Arcadis 16th annual.
- **The abandoned band:** 39% of US disputes are <$5m and ~73% <$25m (Arcadis 16th, 2025 data), while a
  $400/hr pyramid at 57–73% utilisation with a >30-hour engagement floor cannot serve them. `SOURCED`.
  That band is served by neither the consultant nor the litigation funder (Omni Bridgeway screens for
  awards ≥10× funding).

**3. Buyer.** Managing partner / practice lead at a **10–50 person claims, delay or quantum consultancy**, or
the holder of a **state-DOT on-call claims contract**. Named profile from CM-D §1.10: Trauner Consulting
(~36 staff), Imperium Consulting Group (~23), Long International, VERTEX, Capital Consulting International,
RLB contract advisory. **Explicitly not HKA/FTI/Exponent** — conflict checks, procurement, InfoSec, and their
analyst layer *is* their P&L. **Signer: the partner, same week, and the cost is rebilled to the client as a
disbursement or absorbed against a fixed fee.** It never touches an IT budget.

**4. The artefact.** Five documents, delivered as one pack:
(i) a dated, source-cited **chronology** linking event → instruction → notice → schedule impact → cost;
(ii) a **notice and entitlement register** (clause, date served, date due, basis asserted, status);
(iii) an **evidence-completeness score per event** against the tribunal-facing question — not against a house
schema (this is the distinction Gather and ClaimMaster both get wrong: Gather scores its own diary hygiene,
ClaimMaster scores its own ERF);
(iv) a **missing-evidence schedule** — what the record does not yet contain and where it would have been;
(v) an **exhibit set** with page-level citations.
The artefact is the product. The alert is not.

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
They already have Nuix Neo Discover with CAL, Relativity/Everlaw, P6, Deltek Acumen Fuse and Excel — and
**none of those builds a chronology**. eDiscovery culls a corpus; it does not construct a dated causal
narrative linking a verbal instruction to a schedule window to a cost code. The staff *are* the chronology
tool, and they are the cost. The consultant they might otherwise hire is themselves.
The purchase is made for **two reasons that do not require them to admit weakness**:
(a) **it converts declined revenue into won revenue** — at $7,500 they can bid the sub-$5m matters they
currently turn away, which is 39% of the US dispute distribution; and
(b) **it protects fixed-fee margin** — the block they currently write off against a capped fee.
The pitch that survives (CM-D §5.1): *"You bill 200 to 600 hours of chronology per matter and write most of
it off against the fixed fee. Send me the document dump. You get the chronology and the missing-evidence
schedule back the same day — and you can bid the sub-$5m matters you currently turn away."*
Note the structure: **"we already know how to do this" is agreement, not resistance.** They know how; the
labour *is* the cost. The objection has no purchase.

**6. Incumbent coverage.** Closest is **Relativity aiR**, now bundled at **no additional cost** with
RelativityOne — generic, not construction, and it culls rather than constructs. **Nuix Neo Discover** at HKA
is the same shape. **Deltek Acumen Fuse** (600+ metrics) does schedule forensics, not documentary chronology.
To close it, an eDiscovery vendor would have to build construction-specific entitlement semantics — notice
clauses, EOT/compensable separation, Division 00 general conditions — into a horizontal product whose buyers
are litigators, not construction claims analysts. **Estimated 24–36 months and unlikely to be attempted**:
Relativity's addressable market is all litigation; construction claims is a rounding error. The consultancies
themselves are structurally disqualified — **in ~9 years of aggressive M&A none of the twelve major firms has
bought or built a claims-detection product** (`SOURCED`, revealed preference).
**Real risk is not an incumbent; it is Eve** ($103M Series B, 1,200+ plaintiff firms, running *"nightly audits
of active caseloads to surface missed opportunities"*) pointing a proven template at construction.

**7. Substitute-stack coverage.** Excel + Outlook + a paralegal + Copilot achieves: document storage, keyword
search, a manual chronology in a Word table, and — with Copilot at $18–30/user/mo — a serviceable summary of
any single document (Vals Legal AI Report: **94.8% document Q&A vs 70.1% lawyer baseline**; **75.1%
extraction vs 71.1%**). What it does **not** achieve: cross-document linkage at scale, a per-event
sufficiency judgement, or a missing-evidence schedule. Copilot is stateless, has no persistent evidence graph,
and cannot answer *"which of these 47 events has no contemporaneous record of the instruction."*
**Substitute strength: 7/10 on the individual document, 2/10 on the corpus.** That asymmetry is the wedge.

**8. Solo-founder V1.**
- **Ships:** upload-only ingest (PDF/DOCX/XLSX/MSG/EML/ZIP, XER/MPP schedule snapshots, CSV registers), a
  dedicated forwarding address, OCR, entity/date extraction, event clustering, chronology assembly, the
  notice/entitlement register against the contract form supplied, per-event completeness scoring against a
  published rubric (SCL 2nd ed. + AACE RP 29R-03 are both free/public — **no proprietary dataset is required**;
  nPlan's 750,000-schedule moat guards the wrong door because causation is per-project document reasoning),
  missing-evidence schedule, exhibit export.
- **Ingestion path:** file upload and email forward **only**. This is not a compromise — for this buyer the
  file dump from counsel *is* the native format. No API, no OAuth, no security architecture, no Procore key.
- **Deliberately excluded:** any responsibility verdict (C2); any delay-days × rate figure (C3); any schedule
  impact analysis (CM-A: weakest V1 component, defer); any owner contact (C6); any cross-customer training or
  benchmarking (privilege — this is non-negotiable with this buyer); any integration.
- **Founder-in-the-loop is acceptable and expected** for the first 10 matters. Sell the output, not the
  automation.

**9. Pricing.** **SKU 1 — Matter Pack.** $7,500/matter up to 25,000 documents · $15,000 to 100,000 ·
$0.10/document above · **10-matter annual pre-buy $60,000 (the ARR conversion)**.
**Why these numbers:** the displaced alternative is $80,000–$240,000 of the same work, so you are **3–9% of
the thing you replace** — small enough for one partner signature with no business case, large enough to sit
clearly above the $29–300/mo demoware band (C8). **Budget line: client disbursement or engagement cost —
never IT, never SG&A.** **Signer: the partner.** No procurement, no MSA, no security questionnaire.

**10. Defensibility.** Three compounding assets, in ascending order of durability:
(i) **the entitlement rubric library** — contract form × jurisdiction × head of claim, built once, reused
per matter (public sources only);
(ii) **the record-quality-vs-outcome dataset** — process 30–50 anonymised *closed* matters with known
outcomes and you own **the only number in the industry**. Nobody publishes a figure for claims lost to poor
records; Long International's practitioner literature states explicitly that it contains no data. This is the
content moat, the conference talk, the reason a partner takes the meeting, and the answer to *"prove it"*;
(iii) **the accuracy benchmark itself** — a blind back-test against matters with known outcomes does not
exist anywhere (CM-B §8 names it as an unknown), and building it is itself a defensible asset.
**What stops a fast follower:** not the software. The rubric library and the outcome dataset take 12–18 months
of customer relationships to accumulate and cannot be scraped. **What does not stop them:** the extraction and
clustering, which is 2026-commodity work.

**11. Expansion path.** Wedge 2 = **Day 20** (below) — the same engine, pointed at a live project instead of a
closed matter, sold to the heavy-civil contractor the consultancy's DOT client already employs; the on-call
prime is the introduction. Wedge 3 = **The Defensible Price** — the quantum layer, once the evidence layer has
produced enough matters to calibrate. Long-term: the owner "review mode" (Xactimate precedent: sells the price
book to carriers *and* to the contractors fighting them) — but **only after** contractor-side references exist,
because the sequence is one-way.

**12. Kill conditions — concrete and falsifiable.**
- **By 31 Dec 2026: fewer than 4 paid matters and fewer than 2 repeats** from 10–12 targeted firms. The
  channel is a courtesy, not a market.
- **Any two of the first six pilots report that the chronology required more analyst correction time than it
  saved** (measured: analyst hours to first defensible draft, before vs after, on the same matter type).
- **A consultancy runs the pilot and then builds it internally within 6 months.** One instance is noise; two
  is the kill.
- **Relativity, Everlaw or Nuix ships a construction-entitlement chronology module** with a named construction
  claims customer.
- **Blind back-test fails:** on 20 closed matters with known outcomes, the completeness score has no
  discriminating power (AUC < 0.6) between claims that succeeded and claims that failed on records. This is
  the single most important internal test and it should be run in Phase 0, before any sales.
- **Privilege blocks the dataset:** if 8 of 10 firms refuse to permit even anonymised outcome retention, the
  compounding asset does not exist and this collapses to a services business.

**13. Confidence: 8/10.**
Highest in the set. The pain is an invoiced, published, quantified line item at a firm with a `SOURCED` 3.3%
operating margin; the buyer signs the same week; the ingestion constraint costs nothing because upload is the
native format; and the wedge produces the only compounding dataset available. **The two points deducted:**
(a) the 200–600 hour figure is `DERIVED`, not cited — it is a model built by agent 11 and never independently
confirmed; (b) the strategic end-state is genuinely poor — you become a tool vendor into a 3.3%-margin
industry whose customers can become competitors. CM-C §3(d) states it plainly: *"real near-term revenue,
genuine channel, terrible long-term strategic position."* This is a **wedge**, not a business.

---

# WEDGE 2 — **DAY 20**
### *The Supplemental Potential Claim Record engine: an itemised costed estimate and a Time Impact Analysis produced inside Caltrans' 20-day statutory window, from daily reports and schedule snapshots the contractor already files.*

**1. Name & description.** Day 20. On a state-DOT job, when the Engineer's RFI response triggers a protest,
the contractor has **5 business days** for the Initial PCR and **15 more days** for the Supplemental PCR — which
must contain an **itemised cost estimate with the derivation stated, plus a Time Impact Analysis**. Day 20
produces both, from the daily reports and XER snapshots already contractually mandated. It never files, never
signs, never contacts Caltrans.

**2. The specific missed-revenue problem, with frequency and value.**
- **The fuse is `SOURCED` and statutory.** Caltrans 2018 Std Specs §5-1.43A: failure to comply is
  *"Waiver of the potential claim and a waiver of the right to a corresponding claim for the disputed work in
  the administrative claim procedure"* and *"Bar to arbitration (Pub Cont Code §10240.2)."*
  §5-1.43C mandates, within 15 days of the Initial PCR: *"Estimated claim cost and an itemized breakdown of
  the individual costs stating how the estimate was determined"* **plus a TIA**. §5-1.43D adds itemised
  labour, materials and equipment plus a further TIA within 30 days of completion.
- **This is the only US regime supplying both a hard fuse AND a mandated costed artefact on a clock.**
  Sister regimes confirm the pattern: **VDOT NOI** (manual rev. 2 Jun 2025; *AMEC Civil* — actual notice is
  not enough); **FDOT CPAM §7.5** — *"the Department shall enforce the written notice requirement."*
- **Frequency: `ASSUMPTION`, and this is the model's weakest input.** CM-C models **2–4 waived-or-unsupplemented
  events per year per $100M of heavy-civil revenue**. **No published source establishes it.** Confidence: **LOW**.
- **Value per event: $150K–$500K** (`ASSUMPTION` bracketed by `SOURCED` Arcadis distribution — 39% of US
  disputes <$5m, and an individual DOT potential claim sits well below dispute threshold).
- **Modelled annual waived entitlement: ~$600K central (band $300K–$1.5M) = 0.3–1.5% of revenue.**
  Capture 20–40% — **the highest of the three ROI cases, because the failure mode is binary (waiver, not
  negotiation) and the required artefact is specified in writing by the counterparty.** Recovered
  $120K–$240K/yr on a $100M firm earning $8.7M NIBT = **+2.1% of company profit.** `DERIVED`.
- **Margin supports it:** Heavy Construction NIBT **8.3% FY2024** (9.8% in the $50–100M band, 8.7% at
  $100–200M, 15.1% best-in-class) vs commercial GC 4.4%. `SOURCED`, CFMA n=1,558.

**3. Buyer.** **Project executive or VP Operations at a $50M–$300M heavy-civil contractor working state-DOT
work**, with the project engineer / change-order engineer as champion. **Signer: the project executive at
$1,200–$4,500/mo (job-costable, within a $5–25K signature authority); CFO above ~$36K/yr.**
Reachable: **UCON (800+ California union-signatory heavy-civil firms) + IRTBA (300+) + Georgia HCA (~250)
≈ 1,350 named firms with published directories**, all operating under a handful of state spec books. Plus
state DOT bid tabs, which give contract value before the first email.

**4. The artefact.** The **Supplemental PCR pack**: (i) the itemised cost estimate with the derivation stated
line by line (labour by individual, classification, regular/OT hours and dates; materials by invoice, PO,
location, date; equipment by make, model, serial, hours, rate book), (ii) the TIA, (iii) the evidence index
mapping every line to a dated source document, (iv) the missing-evidence schedule for what the record does not
support, and (v) **time and money separated at the data-model level** (C3) — the TIA establishes days, the
cost build establishes dollars, and the pack never multiplies one by the other.

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
They have HCSS HeavyJob (daily reports, cost codes, 128,000 active users), P6, and a schedule engineer. **None
of them produces a costed, itemised, TIA-backed claim record inside 20 days.** HCSS's own diary demo says the
quiet part out loud — *"Johnson Concrete showed up three hours late. At $1,500 a crew hour, that's a lot of
money"* — **and then does nothing with it.** The detection substrate exists; the commercial step is
deliberately unbuilt.
They have a claims consultant — **who they call after the waiver, not before it**, because CRUX's own inclusion
rule (>30 hours of claim work) means the consultant's economics cannot serve a day-20 deadline on a $300K event.
They add it because **the buyer's own spec book demands the artefact and no human can produce it by hand in the
window.** This is the only wedge in the set where the "GC 101 / no one needs more software" objection is
answered by the counterparty rather than by the vendor. And it **displaces headcount, not software**: a
Tutor Perini Change Order Engineer costs $85–120K, i.e. **7–20× the subscription**.

**6. Incumbent coverage.** Closest is **nobody**, and the gap is triple-locked: `recoverable_dollar_estimation`
is **1 everywhere** after CM-A's correction (Procore and InEight both dropped 2→1 because they price a change
order, not a claim). SmartPM ($12K–$25K/yr) and Steelray ($3,990/user/yr) do the TIA arithmetic and **stop**;
Steelray states on its own page that it does not attribute responsibility. Ron Winter ships the same AACE
half-step at $2,750 perpetual.
**To close it, an incumbent must originate a partisan number.** Datagrid (a Procore company) has publicly
refused: *"entitlement and approval stay with the responsible project professionals."*
**BUT — and this is the honest counterweight, from CM-A §3.3:** the restated durable rule is that *two-sided
platforms ship adversarial machinery when an EXTERNAL AUTHORITY makes the judgement*. **Caltrans is an external
authority with a bright-line rule, a published form and a statutory consequence** — precisely the condition
under which Procore shipped Levelset ($484.1M) and Autodesk shipped Payapps ($387M). **This is simultaneously
the best beachhead and the most copyable one.** Estimated time to parity if an incumbent chooses to move:
**12–24 months**, and it is a strategy decision, not an engineering one.
Also live: **Caltrans already runs ePCR** — Adobe Forms on a database, used by contractors *and* Caltrans, with
workflow and email reminders. **The owner supplies the alerting layer free.** Fourth independent confirmation
that alerting is not the wedge.

**7. Substitute-stack coverage.** Excel + Outlook + a schedule engineer + a consultant achieves: the daily
reports (score 3 in the DIY matrix), the cost data (estimators price COs competently, score 2), a TIA if you
have three weeks and a schedule engineer, and the PCR form itself (Caltrans supplies it, Form CEM-6201E). What
it does not achieve: **all of it inside 20 days, repeatably, across 8–15 concurrent contracts.** The DIY stack
scores **0 on evidence_completeness** and **1 on notice_detection, deadline_tracking, claim_identification,
delay_detection and contemporaneous_evidence_graph**. **Substitute strength: 6/10 at leisure, 2/10 at day 20.**
The wedge is the clock, not the capability.

**8. Solo-founder V1.**
- **Ships:** upload of the Engineer's RFI response + daily reports (PDF/CSV/HeavyJob export) + XER/MPP
  snapshots + cost ledger CSV; date arithmetic against the state spec book (5 business days / 15 days /
  30 days, correctly handling business days); the itemised cost build with derivation text; a windows-based
  TIA computed on dated snapshots; the evidence index; the missing-evidence schedule; the completed
  Supplemental PCR form as a PDF **for a human to review and file**.
- **Ingestion path:** **XER upload is the free path in.** Oracle publicly documents the XER field mappings;
  contracts already mandate monthly XER deliverables so the file is already being produced and sent; prior
  art (XER Schedule Toolkit, Schedule Auditor, ScheduleLens) proves it works with zero Oracle relationship;
  **and forensic delay analysis runs on dated snapshots anyway, so upload loses nothing evidentially.**
  Upload beats integrate on cost, speed, legal risk and procurement, with no evidential penalty.
- **Deliberately excluded:** one state (California) only in V1 — the other 49 spec books are the moat, not the
  MVP; no responsibility verdict (C2); no automated filing; no Caltrans contact; no delay-days × rate (C3);
  no Procore/HCSS integration.

**9. Pricing.** **SKU 2 — Project Licence.** **$1,200/project/month, unlimited users, 6-month minimum**;
5 projects $4,500/mo; 15 projects $11,000/mo; **company cap $72,000/yr**; one-off state-spec configuration
$2,500, waived on annual commitment. **Never per seat** — the unlimited-user term is the precondition for
daily-report ingestion, not generosity.
**Why $1,200:** CEMAR proves £435/licence/month (~$550) works under a hard notice regime administering £75bn
of works; Gather's £500 flat is the floor set by *neutrality*, not by willingness to pay. $14,400/yr/project
is **7–11% of a $50M contractor's entire technology purse if charged to G&A — impossible there — but 0.07% of
contract value on a $20M job if job-costed.**
**Budget line: JOB COST, not IT.** On federal and federally-aided work this is materially strengthened by
***Tip Top Construction v. Donahoe*, 695 F.3d 1276 (Fed. Cir. 2012)**: **REA-preparation costs are allowable
contract administration costs under FAR 31.205-33**; only post-CDA-claim costs fall under the
FAR 31.205-47(f)(1) bar. **A pre-claim product is a billable project cost, not an IT purchase.**
`CAVEAT: Caltrans state-funded contracts are governed by the Public Contract Code, not the FAR. Allowability
for Caltrans specifically is UNVERIFIED and must be confirmed contract by contract.`
**Signer: project executive.**

**10. Defensibility.** (i) **Fifty state spec books, each with its own clock, forms and evidentiary
requirements** — a cost for a solo founder and a genuine content moat, exactly the asset Gather built for NEC4
with its `/en/nec4/*` estate. (ii) **The cost-build method library** (labour burden, equipment rate books,
escalation) per state. (iii) **Association endorsement** as a distribution and credibility asset.
**What stops a fast follower:** the per-state configuration depth and the association relationships.
**What does not:** the date arithmetic, which is trivially copyable — and it is the part the customer can
check in 30 seconds, which is precisely why it is the right *free* artefact and the wrong *paid* one.

**11. Expansion path.** Wedge 2 = second and third states (Illinois/IRTBA, Georgia/GHCA, Virginia, Florida) on
the same engine. Wedge 3 = **FAR federal work**, where FAR 52.243-4(d) / 52.242-14(c) / 52.242-17(b) create a
**rolling 20-day cost truncation** — every day of silence deletes a day of recoverable cost, which is *more*
SaaS-shaped than a cliff and is arithmetically demonstrable from a daily report. Then amended-A201 private
megaprojects (data centre / fab / pharma), where the owner negotiated the waiver clause in.

**12. Kill conditions — concrete and falsifiable.**
- **By 31 Mar 2027: fewer than 5 heavy-civil contractors paying ≥$1,000/mo/project for ≥2 months.** The
  contractor will not pay a premium for entitlement and the Gather null result generalises.
- **A California Public Records Act request for Caltrans ePCR filing counts returns fewer than ~1 PCR per
  active contract per year, or shows that supplementation-within-deadline is already near-universal.** This is
  a **free, public-records test of the load-bearing frequency assumption** and it should be run in week 1.
  If Caltrans data shows 0–1 events per $100M per year, the ROI model breaks and this wedge dies on arithmetic.
- **In 10 conversations with heavy-civil project executives, ≥7 report they already produce the Supplemental
  PCR in-house on time.** Then the product saves hours, not dollars, and collapses to a $500/mo efficiency tool.
- **Procore, Trimble or Autodesk ships a state-DOT claim-record module, or adds `clause_reference` /
  `notice_date` / `notice_deadline` / `entitlement_basis` to its change object.** That schema change is one
  quarter of engineering with no liability tail and it is the cheapest leading indicator in the program.
  **Watch Procore Groundbreak, 21–22 Oct 2026, Orlando.**
- **Caltrans amends §5-1.43 to soften the waiver, or a California court reads a prejudice requirement into it.**

**13. Confidence: 7/10.**
The artefact is specified in writing by the counterparty, the fuse is statutory, the margin is the industry's
best, the budget line escapes the 0.26% cage, and the messaging survives both the "GC 101" test and the eSUB
test. **Three points deducted:** (a) **the event frequency is a pure `ASSUMPTION`** and the whole ROI rests on
it; (b) **CM-A's restated rule predicts this is exactly what an incumbent would copy**, because the judgement
is externally adjudicated; (c) heavy civil is where incumbents (P6, InEight, HCSS) are strongest, cutting
against the program's own "fragmentation is weakest where incumbents are strongest" signal.

---

# WEDGE 3 — **THE WRITE-OFF AUTOPSY**
### *A fixed-fee, done-for-you retrospective audit: send last year's closed jobs and your write-off ledger, and get back which write-offs had the evidence to bill and which did not. Pure service. No software sold.*

**1. Name & description.** The Write-Off Autopsy. Not a product — an engagement. The contractor sends closed
job files and the accounting ledger of change-order work written off, absorbed or negotiated down. The output
is a schedule: for each write-off, what the contemporaneous record actually supported, what was missing, and
what the pattern is. Delivered as a report and a 90-minute readout. The founder does the work, with an internal
pipeline nobody sees.

**2. The specific missed-revenue problem, with frequency and value.**
- **The problem is that the buyer does not know their own number.** `SOURCED` incidence is abundant:
  **97%** of specialty trades begin work before COR approval (42% more than half the time); **77%** have
  written off change-order work as bad debt; **91%** of GCs sometimes short-pay; **>50%** don't pay in full on
  **20%+** of the COs they manage; **48%** have had a CO dispute escalate to arbitration or legal.
  (Dodge/Clearstory 2026.)
- **The only published magnitude figure in the entire category:** *"98% of GCs have experienced fee erosion
  due to change order negotiations; nearly half say erosion exceeded 10% of their fee on at least some
  projects."* `SOURCED`, Dodge/Clearstory 2026. Everything else in the program is incidence, not value.
- **And CM-C's finding, stated plainly: there is no credible published dollar figure for the VALUE of
  change-order or entitlement write-offs. It does not exist.** HKA CRUX, Arcadis, Dodge, CFMA, Rabbet,
  Levelset, Billd, Siteline, FMI and JBKnowledge were all attempted. Rabbet's $280bn is a modelled
  cost-of-capital from a 93%-GC sample, not a write-off. Levelset's 4% AR write-off is all-industry,
  vendor-sourced, 2017. **Do not model on it.**
- **Value of the engagement to the buyer:** on CM-C's models, $188K/yr modelled leak at a $50M sub,
  ~$200K/yr fee erosion at a $200M GC. **Confidence LOW on both** — they are models with `ASSUMPTION` inputs.
  **The autopsy's value is that it replaces the model with the buyer's own audited number.**

**3. Buyer.** **CFO or controller at a $25M–$150M specialty trade contractor, or the CFO at a $100M–$500M GC.**
Ranked #3 in CM-D (4.25) and **the persona absent from every hostile practitioner thread** — the mockery came
from PMs and supers; **not one CFO or project executive appeared in any of the four threads.**
They are measured on Days in A/R (55.2), Days of cash (27), Underbillings-to-Equity (8.1%), WIP accuracy and
the surety relationship. **Unrecovered COs are literally a line on their WIP schedule.**
**Reachable for under $700/year: CFMA has 11,000+ members across 90+ chapters; associate membership $515/yr
national + $50–100 chapter.** Chapters run monthly dinner meetings that perpetually need speakers.
**Signer: the CFO. Budget line: Professional Fees (0.50% of revenue = $697K on $139.4M average) — a purse
1.9× larger than Technology Costs (0.26% = $368K), and one the CFO already dislikes because it is episodic,
opaque and arrives after the loss.**

**4. The artefact.** A **write-off autopsy report**: (i) every written-off/negotiated-down change-order dollar
in the period, classified by whether the contemporaneous record supported entitlement, supported quantum,
supported both, or supported neither; (ii) the **recoverable-if-evidenced** subtotal; (iii) the failure-mode
histogram (no written instruction / no notice / no cost segregation / no schedule linkage / genuinely
uncompetitive price); (iv) three named jobs walked through in detail; (v) a one-page policy recommendation.
Deliberately **backward-looking and non-accusatory** — it audits the file, not the people.

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
Their CPA audits the WIP schedule but never asks whether a write-off was *entitled*. Their claims consultant
arrives after a dispute exists and bills 30+ hours minimum. Their PMs will tell them "we couldn't have
collected it" and there is no mechanism to test that assertion. **Nobody in their stack, internal or external,
ever answers the question "how much of what we wrote off last year was actually billable?"**
The purchase is easy for four reasons the other wedges don't have:
(a) **it is checkable against their own ledger** — the single strongest available antidote to *"another shitty
GPT wrapper,"* because a GPT wrapper cannot be checked and a reconciliation to their own general ledger can;
(b) **it asks nobody to change behaviour** — the eSUB trap is avoided entirely, because there is nothing to
adopt;
(c) **it lands in the Professional Fees purse**, where episodic six-figure spend is already normal;
(d) **it is a diagnosis, not a tool** — and CM-D's channel finding is that a session titled *"What your unbilled
change orders are doing to your WIP schedule"* sells where a booth does not.
The pitch (CM-D §5.1 #3): *"Your unapproved change orders are unbilled WIP. Tell me what you wrote off last
year and what's sitting past 60 days without backup. I'll show you which of those had the evidence to bill —
from your own closed files, before you buy anything."*

**6. Incumbent coverage.** **Zero.** No software vendor offers it (it is a service). No consultancy offers it
(**CRUX only counts a project once >30 hours of claim work exists — HKA structurally cannot see the pre-dispute
phase**, and none of the twelve firms markets a retrospective portfolio autopsy). No CPA offers it (they audit
the number, not the entitlement). Time for an incumbent to close: **immediate if any consultancy chose to** —
this is a services offering, not a technology, and it has no technical barrier at all. **The only thing
protecting it is that a T&M business at 57–73% utilisation has no incentive to sell a $15K diagnostic that
might conclude "you had no claim."** That is a real but thin moat.

**7. Substitute-stack coverage.** Excel + the ERP + the controller's own memory achieves the *list* of
write-offs — the ledger already has it. It cannot achieve the *classification*, because that requires reading
the job file. Copilot over a SharePoint job folder gets partway on a single job and falls over on a portfolio.
A CPA will not opine on entitlement. **Substitute strength: 4/10 — they can produce the number, not the
diagnosis.**

**8. Solo-founder V1.** There is **no product**. Ships: a one-page offer, an intake checklist, a secure upload
folder, an NDA, and the founder's own internal pipeline (the same engine as Wedge 1, unbranded and
unproductised). **Deliberately excluded: any software licence, any login for the customer, any recurring
commitment, any owner contact, any recommendation that anyone document better.** Delivery: 2–3 weeks per
engagement, 1–2 concurrently. This is the **only wedge in the set that requires zero software to sell.**

**9. Pricing.** **$12,500 per engagement** (one fiscal year, up to 25 closed jobs); **$25,000** for a two-year
look-back or a multi-entity roll-up. **Budget line: Professional Fees. Signer: CFO.** No procurement, no
security review, no MSA — it is a consulting engagement, and the industry buys those routinely.
Anchor check: Easyclaim proves per-artefact pricing at €599/case for a 21-page derivation; consultants charge
$240K–$660K per matter. **$12,500 for a portfolio diagnosis sits comfortably between, and it is below every
signature threshold that triggers a board conversation.**

**10. Defensibility.** **This is the wedge whose entire defensibility is the dataset it produces.** Run it 30–50
times across anonymised closed matters and closed jobs and you own **the only record-quality-vs-outcome number
in the construction industry** — a number NOTES-running.md identifies as either the fatal evidence gap in the
thesis or the opportunity itself. Nothing else here compounds: the delivery is founder-bound, the method is
copyable, and the customer relationship is episodic. **The correct read is that this is not a business — it is
the cheapest possible way to buy the asset that makes every other wedge defensible, while being paid to do it.**

**11. Expansion path.** Wedge 2 = **Matter Zero** (the same engine, sold to the consultancies whose closed
matters you are already processing). Wedge 3 = the forward-looking product sold to the *same CFO* who has now
seen their own number — which is the only version of the contractor-side pitch that arrives with evidence
rather than a model. This wedge is **Phase 0 of the CM-D first-20 plan, monetised** instead of given away free.

**12. Kill conditions — concrete and falsifiable.**
- **Fewer than 3 CFOs out of 25 approached (via CFMA chapters, not cold) will send closed job files.** The
  confidentiality barrier is fatal.
- **On the first 5 engagements, the median "recoverable-if-evidenced" subtotal is under $50,000** — the
  diagnosis is real but the number is too small to fund anything downstream, and the leak modelled at
  0.1–0.6% of revenue does not exist.
- **≥4 of the first 5 autopsies conclude the dominant failure mode is *uncompetitive pricing*, not missing
  evidence.** This is the live risk: **66% of GCs cite disputed pricing as the primary reason for
  short-payment, above the 53% citing insufficient backup.** If the money is lost on price, no evidence
  engine recovers it, and the entire evidence-sufficiency thesis is attacking the smaller cause.
- **Delivery cannot be compressed below ~40 founder-hours per engagement after 10 iterations.** Then the
  economics never permit the transition to product.
- **No CFO converts to a forward-looking purchase within 6 months of receiving an autopsy showing >$200K
  of recoverable-if-evidenced write-offs.** That is the cleanest possible falsification of contractor-side
  willingness to pay, and it is cheap to run.

**13. Confidence: 7/10.**
Deducted for scale, not for validity: it is founder-bound, non-recurring and structurally unventurable.
But it is the **highest-information, lowest-capital experiment in the program**, it is the only wedge that
tests the load-bearing unknown (*will a contractor pay for recovered entitlement?*) with the buyer's own money,
and its output is the asset that every other wedge needs and nobody has.

---

# WEDGE 4 — **THE DEFENSIBLE PRICE**
### *Loss-of-productivity and disruption pricing computed with the buyer's own trade association's published method, cited on the face of the output — attacking disputed pricing, the largest cause of short-payment, which no product anywhere addresses.*

**1. Name & description.** The Defensible Price. When a COR's cost is challenged, the fight is about the
*number*, not the paperwork. This wedge prices the labour-impact component using **MCAA's published labor
productivity factors** (mechanical) or the **ELECTRI International / NECA Hanna overtime studies** (electrical),
with the association's own document cited line by line on the output, plus the measured-mile computation where
the baseline data exists and an explicit statement of where it does not.

**2. The specific missed-revenue problem, with frequency and value.**
- **`SOURCED`, and it is the most under-exploited number in the program: 66% of GCs cite disputed pricing as
  the primary reason for withholding or reducing payment — above the 53% citing insufficient backup. 64% name
  pricing disputes as the leading disagreement cause. More than half of all CORs require 2+ revision cycles.**
  (Dodge/Clearstory 2026.) **HIGH frequency.**
- **Value: NO published data.** CM-C rates this row *"HIGH frequency, NONE on value."* That is a real gap.
- **Disruption/lost productivity is separately identified as the head with the highest evidence-gated value
  and the lowest claim frequency** — Long International, on 20+ years of process-industrial projects:
  *"there has not been a single instance where job conditions or project records would allow the proper
  'textbook' use of the Measured Mile Method."* `SOURCED`. That is simultaneously the opportunity and the
  warning.
- **The category-wide fact:** `recoverable_dollar_estimation` scores **0 across every AI product in every
  language** — Contradic, SmartClaim, BauAgent, ContraVault, Ronayz, Magra, Lexilio, Gather. The **one** product
  doing quantum properly is **Easyclaim: €599 net per case, 21 pages, 26 cost categories, dual method
  (combined markup and Opitz), no AI, no ingest, one person, since 2017** — with named public customers.
  **Quantum is empty because the law only supplies a computable method in one country. This wedge asserts that
  the association-published method is the US functional equivalent.**

**3. Buyer.** **CFO/controller or chief estimator at a $25M–$150M mechanical or electrical contractor** —
i.e. an MCAA or NECA member. These are the trades with the **highest technology spend ratio in construction
(0.40% of revenue vs 0.26% industry)** and 7.7% net margin. Signer: CFO. Champion: chief estimator (paid
$250–310K — a persona that already owns the number and will defend the method).

**4. The artefact.** A **priced position on the labour-impact head**: the productivity factor applied, the
association source cited with page and table, the affected hours derived from dated records, the measured-mile
computation where a clean baseline exists, an explicit "the record does not support X" section where it does
not, and the arithmetic fully traceable. **Time and money separated (C3); no attribution verdict (C2);
delivered as the contractor's own document for the contractor to send (never owner-facing, C6).**

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
Their estimators price change orders competently — the DIY stack scores **2** on
`recoverable_dollar_estimation`. What estimators cannot do is **defend the productivity-loss component under
challenge**, because the honest answer today is a percentage someone chose. The GC rejects it precisely because
it is unsupported. Their consultant can do it properly, at $225–$1,375/hr, but only once it is already a
dispute (>30 hours).
They add it because **an association-published factor with the citation on the face of the output changes the
argument from "your number is made up" to "argue with MCAA."** CM-D §4.5 identifies this as the highest-leverage
product play in the plan for exactly this reason: it **converts the AACE §1.1 "black box / voodoo analysis"
objection into an audited method**, and simultaneously gives the association a reason to endorse.
Clearstory's COR Pricing Agent prices *known* work off a rate library — that is pricing, not quantum, and it
does not touch productivity loss.

**6. Incumbent coverage.** **Nobody, worldwide.** `recoverable_dollar_estimation` = 0–1 across every scored
entity; the only 3 is Easyclaim, in Germany, offline, non-AI, for a German statutory method. Time for an
incumbent to close: **structurally indefinite** — this is the one stage protected by CM-A's durable rule
(no external adjudicator exists, so the number must be *originated*, and origination carries E&O/UPL/discovery
exposure a seat-priced public company will not take). **Datagrid's public line is the tell.**
**But note the constraint that comes with the protection: quantum cannot ship standalone (C4).** It must be
bundled with evidence linking and sufficiency — which is why this is a Wedge-2-or-3 expansion, not an entry.

**7. Substitute-stack coverage.** Estimator + Excel + the MCAA primer PDF achieves this **if the estimator
knows the primer exists, has the affected hours by activity and day, and has a clean baseline period.** The
first is rare, the second requires the daily-report/cost-code join nobody performs, and the third is the
documented blocker. Copilot cannot do it (it has no project data path). **Substitute strength: 5/10 — the
method is public, the inputs are not assembled.**

**8. Solo-founder V1.** Ingest cost-coded labour hours (ERP/HeavyJob/timesheet CSV) + daily reports + the COR;
identify impacted periods; apply the association factor set; compute the measured mile where a baseline exists
and **state clearly where it does not**; emit the priced position with citations.
**Deliberately excluded:** Eichleay (needs proof of an uncertain standby period and impracticability of
replacement work — both *evidentiary* prerequisites, not computations); any total-cost or modified-total-cost
method; any EOT-to-money conversion; any attribution.
**Prerequisite: written permission or endorsement from MCAA / ELECTRI.** A refusal changes this wedge
materially and should be tested early — it is a free phone call.

**9. Pricing.** **Per priced position: $2,500** (single head, single project period), or bundled into SKU 2 at
$1,200/project/month. Anchor: Easyclaim €599/case proves the per-artefact shape; a US six-figure event supports
4–5× that. **Budget line: job cost or Professional Fees. Signer: CFO or project executive.**

**10. Defensibility.** (i) **The association relationship** — a licence or endorsement from MCAA/NECA is a
genuine, hard-to-replicate distribution and credibility moat, and it is the thing that neutralises the AACE
objection. (ii) **The implemented method library** across trades and heads. (iii) The evidence-prerequisite
logic, which is the actual hard part (CM-B §3.1: *"the product that wins on quantum is the one that assembles
the evidence for the prerequisites — not the one that does the arithmetic"*).

**11. Expansion path.** → other heads (prolongation, escalation, acceleration) → other trades (SMACNA) →
the full priced, evidenced position, which is the convergence point of Wedges 1, 2 and 4.

**12. Kill conditions.** MCAA and ELECTRI both refuse to permit citation of their published factors in a
software output (this is checkable in two weeks and is close to fatal); or on 10 real CORs the productivity
component is under 8% of the COR value (too small to price at $2,500); or fewer than 3 in 10 target contractors
can supply labour hours joined to activity and date at sufficient granularity to compute anything (the
input problem defeats it); or a GC-side rebuttal using the same association document defeats the position in
2 of the first 5 uses.

**13. Confidence: 6/10.**
Attacks the largest `SOURCED` cause of non-payment, occupies the only structurally-protected stage, and has a
real credibility mechanism nobody else has used. **Deducted for:** the input-data prerequisite (which is the
documented reason measured mile is *"a concept, not a procedure"*), the absence of any value-side data for the
disputed-pricing problem, and C4 — it cannot be sold on its own.

---

# WEDGE 5 — **BACKUP PACK**
### *The deliberately boring one. Every change-order request goes out with its substantiation attached, indexed and cross-referenced, first time. No AI in the pitch.*

**1. Name & description.** Backup Pack. At the moment a COR is submitted, the product assembles the
substantiation bundle — signed T&M tags, the daily reports for the affected days, photos, the email or RFI
that directed the work, the contract clause relied on, and the cost breakdown — into one indexed PDF appended
to the COR. Sold as a **billing-hygiene tool**, not an AI product. The word "AI" does not appear on the
pricing page.

**2. The specific missed-revenue problem, with frequency and value.**
- **`SOURCED` frequency, and it is the highest in the program:** **97%** begin work before authorisation;
  **77%** have written off CO work as bad debt; **83%** say the process hurts cash flow; **53% of GCs cite
  insufficient documentation as a reason for withholding payment**; **>50% of CORs require 2+ revision cycles**;
  cycle time **22 days** signed tag → priced COR plus **26 days** COR → signed CO (≈48–49 days).
- **Value: LOW–MEDIUM and honestly contested.** The single-customer anchor is Accurate Firestop: 30% of T&M
  revenue lost pre-Clearstory, reduced 66% after (n=1, promotional).
- **The honest problem with this wedge:** it attacks the **53% (insufficient backup)** cause of short-payment,
  when the larger cause is the **66% (disputed pricing)**. **Clearstory's own commissioned research says the
  market's biggest cause of non-payment is disagreement about the number, and this wedge optimises the smaller
  cause — the same criticism CM-B levels at Clearstory itself.**

**3. Buyer.** Controller or operations manager at a **$10M–$75M specialty trade contractor**. Signer: the
owner/president or the controller, on a credit card, at $500/mo. Champion: the project engineer who assembles
the bundles today.

**4. The artefact.** The indexed backup bundle: cover sheet, index, cross-reference table (COR line → source
document → page), and the source documents in dated order, as a single signed PDF. Plus the COR log entry.
**Nothing else. No score, no verdict, no estimate.**

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
**This is the weakest "why add it" answer in the set, and I will not dress it up.** The honest version:
they add it because assembling the bundle by hand takes a project engineer 45–90 minutes per COR and they
submit 10–40 CORs a month, and because a COR that arrives complete converts faster and discounts less. The
displacement is **project-engineer hours at the billing cadence**, and the payback is cycle-time, not recovery.
**The reasons they might not:** the DIY stack here is *competently built and emotionally owned* —
*"Sheet 1 is a COR Log… Sheets 3-100… This is the bare minimum. Do you not already have something similar in
place?"* The stack is not perceived as a deficiency; it is perceived as **competence**. And Clearstory gives
away a free tier (5 tags + 5 CORs/month, unlimited projects, invited counterparties free) that covers the
adjacent workflow. **This wedge sells documentation hygiene, which is exactly what the eSUB natural experiment
says does not sell.**

**6. Incumbent coverage.** **The closest incumbent is one product decision away.** **Clearstory** carries
**$2.1B/month of two-sided, signed, timestamped, photo-backed COR/T&M evidence across 14,000+ contractors and
13 of the 25 largest North American GCs**, and its **COR Review Agent is in closed beta, "confirms backup
documentation"** — currently against *company* standards. **The day it checks backup against *contract*
requirements instead, this wedge is a feature of a free tier.** CM-B names that release as *"the single
highest-signal event in the US category."* Time to close: **one product decision, 0–2 quarters.**

**7. Substitute-stack coverage.** **The highest in the set.** Excel COR log (`change_order_workflow` scores 3
in the DIY matrix) + folder-per-issue + Bluebeam signing + a PDF printer already produces exactly this artefact,
described end-to-end by practitioners. Copilot can assemble a summary. Clearstory Basic does the capture free.
**Substitute strength: 7/10 — this is the one wedge where the substitute genuinely almost works.**

**8. Solo-founder V1.** Upload/forward T&M tags, daily reports, photos and the COR; auto-index by date and
cost code; emit the bundle. Deliberately excluded: entitlement, quantum, completeness scoring, deadlines,
anything owner-facing.

**9. Pricing.** $500/mo flat per company, unlimited projects and users. **3.0% of a $50M sub's $200K technology
purse** — a credit-card purchase below any threshold, and the one price CM-C says is a **YES everywhere**.
Budget line: technology (this one cannot escape the 0.26% cage — it is a tool). Signer: owner or controller.

**10. Defensibility.** **Effectively none.** Format conventions and a state of ingest connectors. A fast
follower ships this in a quarter and Clearstory ships it in a release. The only compounding asset would be
the two-sided network Clearstory already owns.

**11. Expansion path.** → completeness scoring → entitlement → the priced position. Which is to say: this is
the same destination as Wedge 1 approached from the least defensible end, against the best-capitalised
incumbent, with the weakest pricing.

**12. Kill conditions.** Clearstory's COR Review Agent goes GA checking against contract requirements (near
certain within 12 months); or fewer than 15% of trial users complete a second bundle in month 2 (the eSUB
adoption failure); or measured COR approval time and discount rate are statistically unchanged across
100 CORs before/after.

**13. Confidence: 4/10.**
Included deliberately as the unfashionable, no-AI, high-frequency option — and it fails on three of the
program's own rules at once: it sells documentation hygiene (eSUB), it prices as tooling inside the 0.26%
cage (C8), and it sits directly in the blast radius of a $2.1B/month incumbent with a closed-beta version of
the same feature.

---

# WEDGE 6 — **DEFICIENCY SCHEDULE** *(owner / defence side)*
### *Score the contractor's change request against the contract's own substantiation requirements and output the deficiency schedule — the basis on which the payer reduces or rejects.*

**1. Name & description.** Deficiency Schedule. Sold to owner's representatives, program managers and public
owners. Same engine as Wedge 1, inverted: instead of *"here is what your record supports"* it produces
*"here is what their application does not support"* — line by line, against the substantiation the contract
actually requires.

**2. The specific missed-revenue problem, with frequency and value.**
This is a **money-not-paid-out** problem, and it is the best-evidenced budget in the entire program.
- **Caltrans District 3 alone is procuring $7,000,000 over three years for "Construction Claims and Scheduling
  Support" (03CONTCLM27, advertised Dec 2025).** A prior D5/D6/D10 claims-support contract was $1,000,000.
  **Caltrans has twelve districts.** `SOURCED`. **There is no comparable published contractor-side procurement
  anywhere in this program.**
- **The mechanism is proven, by the most on-thesis product in the world.** Gather's headline outcomes, read
  properly, are all defence-side: Network Rail **"£300,000+ saved"** is *money withheld from the contractor*
  after the client used Gather to *"scrutinise labour, plant and time allocation… included in change
  requests"*; Costain A12: **"15% of claims rejected on the spot"**; Circet's £140,000 is admin labour.
  **Across eleven case studies, not one documents a recovered compensation event in GBP.** `SOURCED`.
- **Owners mandate software and the clause language is public boilerplate:** *"The Contractor shall use the
  Owner's Project Management software, e-Builder… licenses shall be provided to the Contractor."*
- Value per engagement: immediate, same-month, verifiable in this application. **No attribution problem, no
  relationship problem, no "prove it recovered something."**

**3. Buyer.** Program manager or commercial lead at an **owner's rep / PM consultancy** (Jacobs, WSP, Hill,
Turner & Townsend, AECOM) or a public owner. Budget is **pass-through** — they bill the owner — **and they hold
the mandate pen.** Signer: the program director for the consultancy; a procurement officer for the public owner.

**4. The artefact.** The **deficiency schedule**: per change request, the contract's required substantiation,
what was supplied, what is missing, and the reduction or rejection basis. Plus a portfolio roll-up of
application quality by contractor.

**5. Why they add it despite already having software, staff and consultants — REQUIRED ANSWER.**
They already have e-Builder / Unifier / Kahua / PMWeb and a staffed commercial team whose job this literally
is (Microsoft staffs a Construction Contract Lead at $116,900–$203,600 on the owner side). They add it because
**the review is currently a human reading a PDF against a spec, and it does not scale across a program** —
and because the value is provable in the same month. This is the **easiest sale in the set on its merits.**

**6. Incumbent coverage.** **This is the most copyable thing in the entire program, and that is decisive.**
CM-D §3.2(c): every incumbent stops at *taking a side*, not at *checking records* — and **"does the application
match the record?" is assurance, and assurance is the half of the market they already serve.** Procore,
Trimble, Oracle, Clearstory and Gather can all ship this **without breaking neutrality**. Clearstory's COR
Review Agent (closed beta) is already the contractor-facing half of it. **Time to parity: 0–4 quarters, and
they face no liability barrier at all.** You would be building inside the incumbents' blast radius.

**7. Substitute-stack coverage.** Owner's rep humans + e-Builder workflow + the spec book. Caltrans buys the
gap as consulting hours ($7.0M/3yr). **Substitute strength: 6/10 — expensive but functional, and already
funded.**

**8. Solo-founder V1.** Same upload engine as Wedge 1, plus a per-contract substantiation rule set. But the
sales motion is the problem, not the product: **9–24 month public procurement, StateRAMP, sole-source
prohibition, no credit card, prime-contractor structures, DBE/SB requirements** — the exact profile the BRIEF
instructs us to penalise. The only viable path is **through the prime consultant already holding the on-call
contract**, which is Wedge 1's buyer wearing a different hat.

**9. Pricing.** Program licence $3,000–$8,000/month, or per-application review at $250–$500. Signer: program
director (consultancy) or procurement (public owner). **Neutrality caps the price**: Gather charges **£500/mo
flat while publishing 10×–39× ROI**, with **no value component**, because a neutral tool has no claim on the
money it saves. Expect the same ceiling.

**10. Defensibility.** Weak. Assurance is copyable, incumbent-safe, and price-capped by its own neutrality.
The only durable asset would be an owner mandate, which propagates the tool to every contractor on the program
at zero marginal CAC — genuinely the cheapest distribution mechanism in construction, and unavailable to a solo
founder because **a mandate is won by a procurement.**

**11. Expansion path.** → owner portfolio risk → mandate-driven contractor distribution. **But see 12.**

**12. Kill conditions — and this one has a structural kill built in.**
**THE ONE-WAY DOOR: take owner money first and you can never credibly sell contractors.** You will have been
paid to make contractors' claims fail, and every contractor prospect will find out. The reverse *is* available
(Xactimate sells the price book to carriers **and** to the contractors fighting them) — **so the sequence, not
the compatibility, is the binding issue.** Choosing this wedge forecloses Wedges 1, 2, 3 and 4 for years.
Other kills: any incumbent ships application-vs-record checking (near certain); or a first public procurement
takes >9 months (near certain); or the pricing lands at Gather's £500 neutrality ceiling (likely).

**13. Confidence: 5/10.**
The best-evidenced budget in the program, the easiest value story, the fastest verification — and the wrong
wedge, because it is maximally copyable, price-capped by neutrality, procurement-gated against a solo founder,
and **forecloses the rest of the plan.** If the founder constraint were "capital-rich, patient, two-year
runway," this would rank materially higher. Under the stated constraint it does not.

---

# WEDGE 7 — **NOTICE SENTINEL** *(someone else's obvious idea, evaluated honestly)*
### *Ingest your contracts, extract every notice obligation, run a live per-project clock, alert before each deadline and draft the notice. The idea everybody has. Verdict: mostly dead, with one narrow survivable form.*

**1. Name & description.** Notice Sentinel — the "never miss a notice deadline" product. This is the idea the
brief's Hypothesis A describes, that Magra, Lexilio, Aven-AI and BauAgent all built, and that any competent
founder proposes in week one. It is evaluated here honestly rather than dismissed.

**2. The specific missed-revenue problem.** Missed contractual notice.
**`SOURCED` verdict: NOT MEASURED ANYWHERE.** CM-C ranks it **6th of 10** on frequency with **LOW frequency,
HIGH consequence**. The best proxy is CRUX's "contract management and/or administration failure," which fell
**19.5% → 18.0% → <9% post-2020** and is not decomposed. Document Crunch's own Jan 2026 research names the pain
verbatim — *"notice windows had already closed, converting otherwise valid claims into absorbed costs"* — **with
no number attached.**
The consequence evidence is a single case: ***Van Oord v Allseas* [2015] EWHC 3074 (TCC)** — ~£10m claim lost
entirely, repay **£1,895,349.89 + £588,882.98**, on out-of-time notice plus Daily Progress Reports that
*"make so few references to standing time or disruption."* **One judgment is a story, not a frequency.**

**3. Buyer.** Notionally the contracts manager or commercial director. **Actually: nobody with budget.** The
contract administrator is **CHAMPION, NEVER BUYER** (CM-D ranks the persona 10th, budget authority 1/5).

**4. The artefact.** An alert and a draft. **That is the fatal design flaw: neither is an artefact anyone pays
for.** Levelset's alert was **free bait**; the revenue was the **chargeable filing** ($59/notice, $349/lien).
**Contractual notice has no filing, no clerk and no fee.**

**5. Why they'd add it — REQUIRED ANSWER, and it fails.**
They wouldn't, for five independently sufficient reasons:
(a) **Alerting is already solved and free where it matters.** Oracle Aconex scores **3** on deadline_tracking —
mandatory per-Mail-Type Response Required, auto due dates in **working days** against the project working week,
automatic Outstanding→Overdue per recipient. **Caltrans runs ePCR with email reminders, free.** Trunk Tools
gives clause + deadline extraction away with **no account** as lead-gen. **Copilot at $18–30/user/mo already
answers "what are my notice deadlines"** at 75.1% extraction accuracy.
(b) **Drafting is taken.** Document Crunch Notice Builder GA Oct 2024, **agentic since 9 Jun 2026**, now
Trimble-owned. Procore ships 24 correspondence templates including Early Warning Notice, Notice of Delay and
Extension of Time.
(c) **The fear pitch is factually weak in the US.** AIA A201 §15.1.3.1 names 21 days and stops — **no waiver
clause anywhere**; §15.1.3.2 imposes no limit at all. NEC4 61.3 passes **both** limbs of the *Bremer*
condition-precedent test; AIA passes only one. US courts split ~half; **federal boards excuse late notice by
default with the prejudice burden on the Government** (*Hoel-Steffen*, 456 F.2d 760, 768). Best estimate:
late notice is fatal in perhaps **15–30%** of US private-work cases `UNVERIFIED`. **A construction lawyer will
correct this pitch in the room.**
(d) **The behaviour is deliberate.** Contractors **suppress notice on purpose** to protect relationships
(Smith Currie, Jun 2025). A tracker that surfaces deadlines forces a decision they are actively avoiding.
**This gap is defended by culture, not by a competitor** — the hardest kind.
(e) **Nobody articulates it.** No reviewer anywhere complains Procore fails to warn about notice deadlines.
In German, French, Norwegian and Dutch the pain is articulated as legal complexity or behavioural discipline,
**never as a software gap.**

**6. Incumbent coverage.** Fully covered or free at every layer. **Notice DRAFTING is taken; notice TRIGGERING
is the only unoccupied sliver** — Document Crunch's Notice Builder is 100% human-triggered (*"you'll select the
event type then describe what's going on"*). **CM-A gives that sliver ~6–12 months**, and Procore Skills +
Triggers + Actions already makes it available as *customer-authored configuration*, which carries no Procore
liability. **Watch Groundbreak, 21–22 Oct 2026.**

**7. Substitute-stack coverage.** Copilot + Outlook + the contract PDF + a calendar reminder. Plus Aconex where
it is mandated, plus ePCR on Caltrans work, plus Trunk Tools free. **Substitute strength: 8/10 — the highest
in the set.**

**8. Solo-founder V1.** Trivially buildable in 4–6 weeks, which is precisely the problem.

**9. Pricing.** The market has already answered: **$29–$300/month — the demoware graveyard.** Magra, Lexilio,
Delay Claim Builder and ClaimMaster all price here and **not one has a named entitlement customer.**

**10. Defensibility.** None.

**11. Expansion path.** The only honest one is: use notice triggering as the **trigger inside a larger
artefact** (Wedge 1 or 2), never as the product.

**12. Kill conditions.** Already met, five times over. If one wanted to test it anyway: **can 10 contractors
name a specific claim they lost to a missed notice in the last 3 years, with a dollar figure?** If fewer than
3 can, it is dead. My prediction: fewer than 3.

**13. Confidence: 2/10. INCLUDED AS A DELIBERATE NEGATIVE CONTROL.**
Everything about it is attractive — it is easy to build, easy to explain, and the mechanism is real. It is
also the single most thoroughly falsified idea in the corpus: killed independently by Aconex, by Levelset's
economics, by Trunk Tools' free tool, by Copilot's price, by Document Crunch's ownership, by Caltrans ePCR, by
US case law, and by the customers' own deliberate behaviour. **Eight independent kills. If the red team can
resurrect this, the whole evidence base is unsound.**

---

# WEDGE 8 — **PORTFOLIO COMMERCIAL RISK RADAR** *(the wedge I believe is WEAK — the control case)*
### *An executive dashboard of unclaimed commercial exposure across every active project. A genuine, verified, uncontested gap — with zero evidence anyone will pay for it.*

**1. Name & description.** Portfolio Commercial Risk Radar. One screen for the project executive or CFO:
across all active jobs, the unpriced change events, the unbilled COR value, the events past their notice
window, the evidence-completeness distribution, and the trend. **I do not believe this works, and it is
included so the red team has a control case with a real gap behind it.**

**2. The specific missed-revenue problem, with frequency and value.**
- **The gap is verified and unusual.** CM-A found that **Procore's and Autodesk's `portfolio_risk` scores of 3
  are inflated** — both agents wrote in their own justification that the risk domains are *quality, safety,
  design, RFI* and **never commercial**. CM-A added row 24b: **all five incumbents score 1 on commercial
  portfolio risk.** No agent had flagged this.
- **The failure mode is documented:** portfolio roll-up fails at **3–4 concurrent projects** — *"those
  workbooks start living in different states and nobody trusts the roll-up numbers anymore."*
- **And here is the disqualifier, stated by CM-A itself: "Genuine gap, zero evidence of paid-for pain. Do not
  lead with it."** Under the BRIEF's rule (C11), that ends the analysis. There is no complaint, no job
  posting, no budget line, no vendor, no survey question, no case study, and no price point anywhere in the
  corpus attached to commercial portfolio visibility.

**3. Buyer.** Project executive ("know which of my six jobs is bleeding before the owner tells me") or CFO.
Clear persona, real measurement (project margin vs buyout, fee erosion), **and no budget line for a dashboard.**

**4. The artefact.** A dashboard. **Which is the core problem: a dashboard is not an artefact, it is an alert
with charts** — and the entire corpus says the artefact is the product.

**5. Why they'd add it — REQUIRED ANSWER, and it is weak.**
They have Procore portfolio views, Power BI over the ERP, and a monthly project review meeting. They would add
this only if it surfaced dollars the other three do not — which requires the full detection + evidence +
completeness engine underneath it. **The dashboard is therefore an output of Wedges 1/2/4, not a wedge.**
Sold alone it is a net add on a 4.4–8.3% margin that displaces nothing. **"A purchase with no displacement"**
is CM-C's named failure condition.

**6. Incumbent coverage.** Genuinely open (24b = 1 everywhere). But **open because nobody wants it**, and any
incumbent could ship a commercial-risk tab in one quarter the moment demand appeared — with no liability tail,
because a roll-up asserts nothing.

**7. Substitute-stack coverage.** Excel roll-up (fails at 3–4 projects), Power BI, the monthly review meeting.
**Substitute strength: 5/10 — bad, and tolerated.**

**8. Solo-founder V1.** Cannot exist standalone. Requires the whole engine to have anything to display. **This
is a feature that pretends to be a product.**

**9. Pricing.** Notionally $1,000–$2,000/month company-wide. **No budget line. Signer unclear.**

**10. Defensibility.** None.

**11. Expansion path.** Inverted — it is the expansion, not the wedge.

**12. Kill conditions.** Already met by C11. Falsifiable test if wanted: **in 20 conversations with project
executives, does even one name commercial portfolio visibility as a problem they have tried to buy a solution
for?** Corpus prediction: zero.

**13. Confidence: 2/10. EXPLICITLY LABELLED WEAK — CONTROL CASE.**
It is the cleanest illustration of the BRIEF's central rule: a verified, uncontested, correctly-identified gap
at five incumbents, in a real persona's real blind spot — and **still not white space**, because absence of a
feature is not evidence of paid-for pain. **If a red team can find paid-for-pain evidence here, the corpus has
a hole in it.**

---

## 2. RANKING TABLE

Scored 1–10 on each of nine axes. **Incumbent coverage** and **substitute coverage** are scored *inverted*
(10 = incumbents/substitutes cover it least well = best for us). Total out of 90.

| # | Wedge | Pain | Econ value | Buyer clarity | Incumbent cov. (inv.) | Substitute cov. (inv.) | Add/switch rationale | MVP feasibility | Defensibility | Expansion | **TOTAL** |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **1** | **Matter Zero** (consultancy chronology + sufficiency) | 9 | 7 | 9 | 9 | 7 | 7 | 10 | 6 | 8 | **72** |
| **2** | **Day 20** (Caltrans Supplemental PCR: costed estimate + TIA) | 8 | 8 | 8 | 8 | 7 | 9 | 7 | 7 | 8 | **70** |
| **3** | **The Write-Off Autopsy** (productised service to CFOs) | 7 | 5 | 8 | 9 | 8 | 8 | 10 | 4 | 9 | **68** |
| **4** | **The Defensible Price** (association-method productivity quantum) | 8 | 7 | 7 | 9 | 7 | 7 | 6 | 7 | 7 | **65** |
| **5** | **Backup Pack** (boring, no-AI substantiation bundle) | 7 | 5 | 7 | 4 | 5 | 5 | 8 | 3 | 5 | **49** |
| **6** | **Deficiency Schedule** (owner / defence side) | 7 | 8 | 6 | 4 | 6 | 6 | 5 | 3 | 2 | **47** |
| **7** | **Notice Sentinel** (someone else's obvious idea) | 4 | 3 | 5 | 2 | 3 | 3 | 9 | 2 | 4 | **35** |
| **8** | **Portfolio Commercial Risk Radar** (WEAK — control) | 3 | 3 | 5 | 6 | 6 | 2 | 4 | 2 | 3 | **34** |

### Notes on the scoring that a red team should attack first
- **Wedge 1's "pain 9"** rests on a `DERIVED` 200–600 hour figure that was modelled by agent 11 and never
  independently confirmed. If that block is really 80–150 hours, the wedge drops to ~62.
- **Wedge 2's "econ value 8"** rests on a pure `ASSUMPTION` of 2–4 waivable events per $100M/year. It is the
  single most attackable number in the set and it is **free to test** via a California Public Records Act
  request on Caltrans ePCR filing counts.
- **Wedge 2's "incumbent coverage 8" is internally contested.** CM-A's restated structural rule predicts that
  an externally-adjudicated regime is *exactly* where incumbents historically DO ship adversarial machinery
  (Levelset, Payapps). A defensible counter-score is 5, which would drop Wedge 2 to 67 and behind Wedge 1.
- **Wedge 3's "defensibility 4"** is generous only if the outcome dataset is actually retainable through
  privilege and confidentiality constraints. If it is not, score 2.
- **Wedge 6's "expansion 2"** encodes the one-way door. If the red team believes the sequence constraint is
  soft, that score should be 7 and the wedge moves to 52 — still fifth, but materially closer.

---

## 3. "WHAT MUST BE TRUE" — TOP THREE WEDGES

### WEDGE 1 — MATTER ZERO

| # | Assumption | Weight | How to test, and how fast |
|---|---|---|---|
| 1 | **The 200–600 hour document-review block is real, and 40–60% of it is automatable.** Everything else follows from this. It is `DERIVED`, not cited. | **Load-bearing** | Ask 5 partners directly, and instrument one live matter: analyst hours to first defensible chronology draft, before vs after. **4 weeks, free.** |
| 2 | **A consultancy will buy rather than build.** All current evidence is structural (they buy Nuix/Relativity/Acumen; none of twelve firms has built claims software in 9 years of M&A) — none of it is a stated preference. | **High** | 5 partner conversations at **Construction SuperConference, 1–3 Dec 2026, Huntington Beach.** |
| 3 | **Cannibalisation is answerable by the revenue framing.** They must value bidding the sub-$5m matters they decline (39% of the distribution) more than they value protecting the hours. | **High** | Price test in Phase 1: offer per-matter vs per-analyst-seat and observe which they choose. |
| 4 | **Privilege permits retention of anonymised outcome data.** Without it the compounding asset does not exist and this is a services business. | **High** | Put the clause in the first 3 contracts and count acceptances. **6 weeks.** |
| 5 | **Evidence-completeness scoring has real discriminating power.** If a blind back-test on 20 closed matters cannot separate claims that succeeded from claims that failed on records, the core capability is decorative. | **Load-bearing, and untested by anyone anywhere** | Phase 0 back-test. **This benchmark does not exist in the world; building it is itself an asset.** |
| 6 | **The tribunal-standard rubric is buildable from public sources.** SCL 2nd ed. (free), AACE RP 29R-03 (free to members), published standard forms, case law. nPlan's dataset moat guards the wrong door because causation is per-project document reasoning. | Medium | Build it and have one testifying expert review it. |

### WEDGE 2 — DAY 20

| # | Assumption | Weight | How to test, and how fast |
|---|---|---|---|
| 1 | **2–4 waived-or-unsupplemented potential-claim events occur per $100M of heavy-civil revenue per year.** Pure `ASSUMPTION`. If it is 0–1, the model breaks. | **Load-bearing** | **California Public Records Act request on Caltrans ePCR**: PCRs filed per contract per year, how many were supplemented with a costed estimate + TIA inside the deadline, how many were waived. **Free, public, and it would produce a defensible number nobody in the industry has.** Run in week 1. |
| 2 | **Heavy-civil contractors cannot already produce the Supplemental PCR inside 20 days.** Many run a schedule engineer and a cost engineer; if they already comply religiously the product saves hours, not dollars. | **Load-bearing** | 10 project-executive conversations via UCON. |
| 3 | **Caltrans actually enforces §5-1.43A waiver in practice**, rather than routinely accepting late or thin records. The spec is unambiguous; enforcement behaviour is not documented anywhere. | **High** | PRA request on waiver determinations; ask 5 contractors whether they have personally had a PCR waived. |
| 4 | **Per-project spend is job-costable under Caltrans contracts.** The *Tip Top* logic is **federal**; Caltrans state-funded work is governed by the Public Contract Code. Currently `UNVERIFIED`. | **High** — it is what escapes the 0.26% cage | Caltrans Std Specs §9 + Construction Manual; one heavy-civil controller interview. |
| 5 | **No incumbent ships a state-DOT claim-record module within 24 months.** CM-A's own restated rule predicts this is the *most* copyable regime. | Medium-High | **Groundbreak, 21–22 Oct 2026.** Watch for `clause_reference` / `notice_date` / `notice_deadline` / `entitlement_basis` appearing on any change object. |
| 6 | **The TIA computed from uploaded XER snapshots is defensible without a testifying expert**, or is at least accepted as the contractor's own submission. No tribunal is known to have accepted software-generated delay analysis without an expert. | Medium | SCL judicial-references summary; ASBCA/CBCA award search. Currently unanswered by any source in the corpus. |

### WEDGE 3 — THE WRITE-OFF AUTOPSY

| # | Assumption | Weight | How to test, and how fast |
|---|---|---|---|
| 1 | **CFOs will hand over closed job files and the write-off ledger to an outsider.** The entire engagement depends on it. | **Load-bearing** | Ask 25 CFOs via 3 CFMA chapters. **8 weeks, ~$700 of membership.** |
| 2 | **A meaningful share of write-offs were evidenced-and-billable.** If the dominant failure mode is genuinely uncompetitive pricing (**66% disputed pricing vs 53% insufficient backup**), the evidence thesis is attacking the smaller cause and the autopsy proves it. | **Load-bearing — and it cuts both ways** | The first 5 engagements answer it definitively. **This is the cheapest possible test of the entire program's core hypothesis, and the customer pays for it.** |
| 3 | **The modelled leak of 0.1–0.6% of revenue exists at all.** Every ROI in CM-C rests on it and **no published source establishes it.** | **Load-bearing for the whole program** | The autopsy *is* the test. Also: the 30-controller question — *"In your last fiscal year, what dollar value of work did you perform and either never bill, or bill and not collect, because the change order was never executed or was negotiated down?"* |
| 4 | **The engagement compresses below ~40 founder-hours after 10 iterations**, or it never becomes product. | High | Instrument every engagement from #1. |
| 5 | **A CFO who sees their own number converts to a forward-looking purchase.** This is the load-bearing unknown of the entire thesis and **nobody has produced this evidence, including Gather.** | **Load-bearing** | 6-month conversion tracking from engagement #1. |

---

## 4. THE FUNDED PICK

> ### **FUND WEDGE 1 — MATTER ZERO**, with **THE WRITE-OFF AUTOPSY** run concurrently as a paid Phase-0 data-acquisition programme, and **DAY 20** as the declared destination at month 9.

**Why.** It is the only wedge where the pain is an **already-invoiced line item** — 200–600 hours per matter
at a $396–$442/hr realised rate, at firms running a `SOURCED` 3.3% operating margin — rather than a modelled
leak nobody has published. The buyer signs the same week, rebills the cost as a disbursement, and never touches
an IT budget or a procurement. And uniquely among the eight, **the solo-founder ingestion constraint is not a
compromise but the native format**: the consultancy's data arrives as a file dump from counsel, so
upload-only V1 is exactly what the buyer already does — which means the founder has better commercial-record
coverage than Trunk Tools, whose Procore access was revoked, and no dependency on any platform's permission.

**Why the others lose.**
- **DAY 20 (rank 2, 70)** is the better *business* and the worse *wedge*: its entire ROI rests on an unsourced
  event-frequency assumption, and CM-A's own restated rule predicts that an externally-adjudicated regime is
  precisely where a two-sided incumbent *will* ship adversarial machinery (Levelset $484.1M; Payapps $387M).
  It is the destination, reached with a proven engine and a reference list — not the entry.
- **THE WRITE-OFF AUTOPSY (rank 3, 68)** is founder-bound, non-recurring and unventurable, but it is **too valuable to skip**: it is
  the only way to buy the record-quality-vs-outcome dataset **while being paid**, and it tests the program's
  load-bearing unknown with the customer's money. Run it, do not fund it as the business.
- **THE DEFENSIBLE PRICE (rank 4, 65)** cannot ship standalone (C4: quantum sits downstream of standards-blocked causation) and its
  input prerequisite — labour hours joined to activity and date — is the documented reason measured mile is
  *"a concept, not a procedure."* It is step 3 of the roadmap, not the entry.
- **BACKUP PACK (rank 5, 49)** sells documentation hygiene into the eSUB graveyard, prices as tooling inside the 0.26%
  cage, and sits under a closed-beta feature at a vendor carrying $2.1B/month of the exact evidence.
- **DEFICIENCY SCHEDULE (rank 6, 47)** has the best-evidenced budget in the program ($7.0M at one Caltrans district) and loses
  anyway: it is the **most copyable** thing available (assurance does not break neutrality), **neutrality caps
  its price** (Gather: £500/mo flat against published 39× ROI), it requires a 9–24 month public procurement,
  and it is a **one-way door** that forecloses every contractor-side wedge.
- **NOTICE SENTINEL (rank 7, 35)** is falsified eight independent ways and has no chargeable artefact — Levelset's alert was
  free bait and the **filing** was the revenue; contractual notice has no filing.
- **PORTFOLIO COMMERCIAL RISK RADAR (rank 8, 34)** is the control: a verified, uncontested gap at all five incumbents with **zero** evidence of
  paid-for pain, which under the BRIEF's own rule is not white space at all.

**The one thing that would change this pick:** if the Caltrans PRA request returns ≥3 waived-or-unsupplemented
PCRs per active contract per year, DAY 20's economic value becomes `SOURCED` rather than `ASSUMPTION`, and it
overtakes MATTER ZERO. **That request is free and takes two weeks. Run it before committing.**

---

## 5. TOP FIVE "WHAT MUST BE TRUE" ACROSS THE WHOLE PROGRAM

1. **A contractor will pay a premium for recovered entitlement, sustained for four quarters.** Nobody has ever
   produced this evidence — **including Gather, the company best positioned in the world to produce it, whose
   eleven case studies contain not one recovered compensation event in GBP.** This is the load-bearing unknown
   of the entire thesis.
2. **The modelled leak of 0.1–0.6% of revenue exists.** There is **no credible published dollar figure for the
   value of construction change-order or entitlement write-offs.** The industry publishes incidence, not value.
   Every ROI in the program is built on an `ASSUMPTION`.
3. **The money is lost to missing evidence, not to price.** **66% of GCs cite disputed pricing as the primary
   reason for short-payment, above the 53% citing insufficient backup.** If the dominant cause is price, the
   evidence-sufficiency thesis is optimising the smaller half of the problem.
4. **Evidence-completeness scoring has real discriminating power against actual outcomes.** No such benchmark
   exists anywhere in the world; the thesis currently rests on one judgment with numbers (*Van Oord*) and a
   2021 dispute-cause ranking.
5. **The documented practitioner hostility does not generalise to the budget holder.** Four hostile
   r/ConstructionManagers threads probed exactly this product — *"This is like GC 101 and no one needs more
   software for anything"* — and **not one project executive or CFO appeared in any of them.** The mockers are
   real, and they are the wrong persona. If the CFO reacts the same way, the contractor-side market does not
   exist at any price.
