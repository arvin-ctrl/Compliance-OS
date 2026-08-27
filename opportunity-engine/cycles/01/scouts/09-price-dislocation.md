# SCOUT 09 — PRICE DISLOCATION

**Surface:** services with a *published per-unit price* for work that is now machine-doable, where the buyer is the payer.
**Date:** 2026-08-27
**Verdict:** Surface is **wet but shallow**. Eight candidates below. Six documented kills. One structural finding that
matters more than any single candidate (§ Cross-cutting, read it first).

---

## METHOD AND ITS LIMITS

I hunted for services that publish a per-unit rate card, pulled the rate cards verbatim, then estimated a machine
cost per unit from an explicit assumption chain. Published price = T1 evidence ("freelancers/agencies with
published prices doing it by hand at volume").

**Two limits you must weigh when reading this:**

1. **Web-search budget was exhausted at 200 calls** partway through. Everything below is either a verbatim page
   fetch or a dated search snippet, but I could **not** go to Upwork/Fiverr/Reddit to pull named buyer handles.
   Where G1 asks for named people, I name **channels and directories** and say plainly that I did not verify
   individual handles. Treat every G1 in this file as **unproven**, not as passed.
2. **Machine-cost figures are ESTIMATES, not sourced numbers.** Assumption chain, used consistently throughout:
   - frontier vision-capable LLM at roughly **$3–15 / M input tokens, $15–75 / M output tokens** *(ASSUMPTION —
     list-price band, not verified this session)*
   - dense text page ≈ 700 tokens; scanned page image ≈ 1,500–2,500 tokens
   - TTS at single-digit dollars per million characters *(ASSUMPTION)*
   - our own operator time costed at $0 (per operator profile)
   Every "machine cost" below is derived from these. They are **not evidence**; the published prices are.

---

## CROSS-CUTTING FINDING — READ BEFORE THE CANDIDATES

I set out to find un-arbitraged gaps. What the rate cards actually show is more useful:

**Where an AI entrant already exists, it prices at 25–40% of the human price — not at machine cost.**

The cleanest proof is deposition summaries. Human services charge **$3–10 per page** (Ditto Transcripts:
**"$3.50 per page"**). SmartDepo, an AI-native entrant, publishes:
**"1–9: $85, 10–19: $75, 20–30: $65, 31–40: $55, 41+: $50"** per summary, or **"$25 flat per summary no matter the
volume"** on the **$99/month** plan — [smartdepo.law/pricing](https://www.smartdepo.law/pricing) (fetched 2026-08-27).
A 200-page transcript costs $600–2,000 by hand and $25–85 from the AI entrant. Their own marginal cost is well under
$1. **They kept ~98% of the arbitrage.**

Three consequences:

- **"Already arbitraged" is not the same as "no margin left."** These markets settle at a fraction of the human
  price, which is still 50–500× machine cost. The dangerous condition is not *an* AI competitor; it is *ten*.
- **The gap survives longest where the buyer is purchasing a warranty, not an output.** 3Play's state rate card
  sells **"99%+ measured accuracy"** and **"two rounds of human QA review"** at **$1.90/min** for captions in a
  world where ASR costs fractions of a cent per minute. That gap has survived a decade of commodity ASR because the
  product is the *guarantee*, not the transcript. A cold-start operator cannot sell a guarantee — we have no
  balance sheet and no reputation. **This kills every candidate whose value is a warranty**, and it is why I
  down-rate accessibility certification, medical chronology, and insurance estimating below.
- Therefore the only price dislocations we can actually take are ones where **the buyer verifies the output
  themselves in under a minute**. That filter, applied hard, is what produced the ranking below.

---

# CANDIDATES

---

## PD-1 · Scan-to-CAD — raster/PDF drawings to layered, dimensionally-correct DWG
**Confidence: 6/10 — the best fit on this surface for our profile**

**One sentence:** Upload a scanned or flat-PDF drawing, get back a properly layered AutoCAD DWG plus an overlay
image proving every line lands on the original.

**The artifact:** a `.dwg` with real layers (walls / doors / dimensions / text / equipment), correct scale, **plus a
red-on-black overlay diff of our output against the source PDF** — the buyer's own verification, shipped with the
product.

**Evidence — T1 (published per-sheet prices, all fetched 2026-08-27):**
- FG Baseline: **"Basic Floor Plan (1 page): $100"**, **"Detailed Plan (1 page): $150"**, **"Multi-Sheet Set (3+
  pages): from $400"**, **"Delivered within 48 hours of confirmation"** —
  [fgbaseline.com/pdf-to-cad-conversion-service](https://www.fgbaseline.com/pdf-to-cad-conversion-service)
- Convert2AutoCAD: **"Depending on the size, and time to redraw, pricing usually is in the range of $120-220 per
  sheet"**; **"Typically, converting to AutoCAD takes 3 full business days"**; **"rush 24-hour service for only $30
  per drawing"**; and — the important line — **"if you think you may do it often, we can set you up with an
  account, where you will be billed monthly"** —
  [convert2autocad.com FAQ](https://convert2autocad.com/convert-pdf-files-autocad-dwg/faq/)
- CADmore pricing guide: simple 2D redraw **"$40 to $200 per sheet industry-wide"** —
  [cadmore.com/blog/cad-conversion-cost](https://cadmore.com/blog/cad-conversion-cost)
- Convert2AutoCAD names its own recurring verticals: *"Legacy Drawing Conversions, Electrical Plans & Panel
  Layouts, Floor Plan Layouts, Site Plans, Survey Plans, Construction Drawing Sets."*

**Machine cost (ESTIMATE):** vector-PDF sources are a deterministic geometry parse ≈ **$0.02/sheet**. Scanned raster
needs vectorisation plus 3–6 vision passes for layer/symbol/scale classification on a ~2,000-token image ≈
**$0.30–$2.00/sheet**.
**Gross gap: 50–400×.**

**Who buys it today, by name (segments, from the vendors' own service lists):** sign shops, kitchen/bath and
millwork/cabinet shops, HVAC and sheet-metal fabricators, land surveyors, facilities managers, low-voltage and
solar designers, architects inheriting a legacy set. Convert2AutoCAD's **monthly-billed accounts** and
**reseller pricing** are direct evidence of repeat buyers, not one-off projects.

**Why the incumbent hasn't collapsed its own price:** because it is a body shop — the price *is* the labour. There
is no credential and no liability tail here; the binding constraint is **last-mile geometric accuracy** (a wall 2"
out is worthless) and **scale calibration from an unscaled scan**. That is an engineering problem, which is exactly
the failure mode our profile is strongest against.

**Verifiability: excellent.** Overlay the DWG on the source. Wrong is visible in one second. No trust required —
the single most important property on this surface.

**What stops ten others doing it:** at gig level, nothing. The defensible position is **distribution inside the
tool the buyer already lives in** — an AutoCAD/Revit plugin on the Autodesk App Store, where install counts are
public (T2 evidence available, not yet pulled) — plus a per-trade learned symbol library that compounds with volume.

**Gate check**
- G1 distribution — **PARTIAL**. Buyers post these jobs publicly with budgets attached (freelance marketplaces,
  r/AutoCAD, r/Surveying) and the Autodesk App Store is a self-serve storefront. **I did not verify named handles
  — search budget exhausted. This is the gate to test first.**
- G2 demand — **PASS.** Multiple vendors, published rate cards, monthly accounts, reseller tiers.
- G3 buildable — **PASS.** No credential, no gated data, no procurement. Pure software.
- G4 self-verifiable in 14 days — **PASS.** Buy 20 real scanned sheets from two of these vendors at $100–150 each
  (~$2.5k, inside budget), convert them ourselves, measure geometric error against what we paid for. No stranger's
  cooperation needed. This is the cleanest 14-day test in the whole file.
- G5 clock — **WEAK/UNDATED.** The change is vision models becoming able to read dense construction linework. I
  could not date that with a citable event this session. **Flagged as the honest weakness.**

**Price signal:** $85–$220 per sheet, today, published.

---

## PD-2 · Solar PV permit plan sets
**Confidence: 6/10 — best recurrence, credential caveat**

**One sentence:** Every residential solar install needs a permit drawing set; two published vendors sell the same
artifact at $249 and $1,425.

**The artifact:** a permit-ready PV plan set — site plan, single-line diagram, attachment/structural details,
placards, spec sheets, calculations — as a submittable PDF.

**Evidence — T1 (published per-set prices, fetched 2026-08-27):**
- Planet Plan Sets: **"PV Plan Set 0-10 kW AC – $249"** rising through **"PV Plan Set 30-35 kW AC – $499"**;
  battery adders **"ESS 0-20 kWh – $100"** to **"ESS 61-80 kWh – $160"**; interconnection processing **"0-25 kW
  SOLAR PV ONLY – $360"** to **"Over 25 kW SOLAR +STORAGE – $780"** with **"additional hours billed at $150/hr"**;
  **"Within 2-3 business days after receipt of order and system specs"**; **"We provide our plan drafting services
  to solar contractors only"** — [planetplansets.com](https://www.planetplansets.com/solar-permit-pricing/)
- Solar Permit Solutions: **"$1,200/plan set"** (residential/ADU ≤20 kW), **"$2,000/plan set"** (20–30 kW),
  **"Starting at $3,700/plan set"** (30 kW+); add-ons **"Interconnection with Utility: +$1,500"**, **"Local AHJ
  Submission: +$1,000"**; **"PE-stamped & sealed"**, **"2–5 business day delivery"**, **"Unlimited revisions"** —
  [solarpermitsolutions.com/pricing](https://www.solarpermitsolutions.com/pricing)
- GoGreenSolar (retail, sold to DIY homeowners): **"Starting at $1,425"** for the Plan Set & Interconnection
  Service; **"This service is only available to customers who purchase a complete solar panel kit from us"** —
  [gogreensolar.com](https://www.gogreensolar.com/products/solar-permitting-service)

**Machine cost (ESTIMATE):** template assembly + equipment spec lookup + AHJ-rule lookup + drawing generation ≈
**$2–15 per set**.
**Gross gap: 17–100× against the $249 wholesale tier; ~100–500× against the $1,425 retail tier.**

**Who buys it today:** residential solar installers — and they buy **one per install**, which is the strongest
recurrence in this file. DIY homeowners buy the retail version.

**Why the incumbent hasn't collapsed its own price:** three reasons, and one of them is fatal-ish.
(a) **The PE stamp** — Solar Permit Solutions' entire $1,200 vs. $249 premium is *"Every plan set is PE-stamped."*
That is a credential.
(b) **AHJ rule variability** across thousands of jurisdictions — that is a *data asset*, and a buildable one.
(c) Rejection risk carried by the installer.

**Verifiability: good but slow.** The AHJ approves or rejects. Feedback is days-to-weeks, not seconds.

**What stops ten others:** the AHJ requirements corpus (submittal checklists, plan-set conventions, placard rules
per jurisdiction) is a genuine scraped data asset that compounds. That is the moat, and it is exactly the kind of
thing we can build.

**Gate check**
- G1 — **PARTIAL.** Buyers are findable through installer directories and the DIY-solar communities; recurrence
  means one landed customer is an annuity. Named handles not verified.
- G2 — **PASS.** Three published rate cards, one of them retail-facing.
- G3 — **PARTIAL FAIL.** The *stamped* product needs a PE we do not hold. The *unstamped drafting* does not — and
  Planet Plan Sets proves the unstamped artifact is a real, separately-priced product at $249. Scope must be the
  unstamped set, with the customer arranging their own stamp. Anything that shades into "we designed your
  electrical system" is an unauthorised-practice-of-engineering problem. **Watch this hard.**
- G4 — **PASS.** Buy three plan sets at $249, reproduce them, compare against AHJ checklists.
- G5 — **UNDATED.** No citable event found this session.

**Price signal:** $249 wholesale / $1,200–1,425 retail, per install, published.

---

## PD-3 · Audio description for video
**Confidence: 4/10 — the biggest verified gap, the worst distribution**

**One sentence:** Describing what happens on screen for blind users costs $8.50 a minute from the market leader and
cents a minute by machine.

**The artifact:** a timed description track (WebVTT + mixed audio) merged with existing captions.

**Evidence — T1 (a *government contract rate card*, the strongest price evidence in this file):**
State of Minnesota published 3Play Media cost data, extracted verbatim 2026-08-27
([mn.gov PDF](https://mn.gov/admin/assets/Cost%20Data%203Play%20Media_tcm36-569448.pdf)):
- Audio Description: **"5-business day turnaround (standard audio description) $8.50/min ($510/hr)"**,
  **"2-business day $10.50/min ($630/hr)"**, **"1-business day $12.50/min ($750/hr)"**, **"Extended audio
  description add $5.00/min"**
- Prerecorded Captioning + Transcription: **"$1.90/min ($114/hr)"** (10-day) rising to **"$6.00/min ($360/hr)"**
  (2-hour), **"Includes 99%+ measured accuracy"**, **"99%+ accuracy with two rounds of human QA review"**
- **"The minimum charge for any service is 1 minute"**, **"Pricing is billed as you go (no commitment)"**
3Play's own current pricing page no longer publishes rates: *"Your per-minute rate will be personalized"*
([3playmedia.com/plans-pricing](https://www.3playmedia.com/plans-pricing/)) — the state rate card is the harder
evidence.

**Machine cost (ESTIMATE):** frame sampling + vision description + script timing + TTS ≈ **$0.10–$0.60/min**.
**Gross gap: 15–100×.**

**The clock — dated, and it moved the WRONG way:**
- DOJ ADA Title II web rule original compliance date was **April 24, 2026**. On **April 17, 2026** DOJ **extended
  the deadlines by one year** → **April 26, 2027** (entities serving ≥50,000) and **April 26, 2028** (<50,000).
  [Duane Morris alert](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html)
- HHS Section 504 rule's **May 2026** deadline was *not* extended.
  [Jackson Lewis](https://www.jacksonlewis.com/insights/doj-extends-public-entities-compliance-deadline-ada-related-website-accessibility-hhss-may-2026-deadline-still-looms)

**Why the incumbent hasn't collapsed its price:** it is selling a **warranty** ("99%+ measured accuracy", "two
rounds of human QA review") to institutional buyers who need documented compliance, plus **40+ integrations** into
Kaltura/Panopto/Brightcove. Neither is available to a cold-start operator.

**Gate check**
- G1 — **FAIL.** Buyers are universities, state agencies and health systems. That is procurement, an RFP, and a
  vendor security review. Our profile explicitly cannot do it.
- G2 — PASS (a state publishes what it pays).
- G3 — PASS technically.
- G4 — PASS.
- G5 — PASS but **negative**: the DOJ extension of 2026-04-17 removed a year of urgency from the largest buyer pool.

**Killed on G1.** Recorded because the price evidence is the best on the surface and because the DOJ extension is a
dated fact the whole accessibility cluster now has to be re-scored against.

---

## PD-4 · PDF / document accessibility remediation
**Confidence: 4/10 — half-arbitraged, and the residue is a certificate**

**One sentence:** Making a PDF screen-reader-usable is sold per page and the per-page price has not fallen to
machine cost.

**Evidence — T1 (published per-page prices):**
- Accessiblü, fetched 2026-08-27: Tier 1 *"Tag structure, reading order, language and metadata, and bookmarks"* at
  **"$10 per page"**; Tier 2 *(adds alt text + screen-reader QA)* **"$15 per page"**; Tier 3 *(adds an Adobe
  Acrobat accessibility audit, a PDF/UA conformance report and a Certificate of Remediation)* **"$18 per page"** —
  [accessiblu.com/pdf-remediation](https://www.accessiblu.com/pdf-remediation/)
- Vendor round-up **updated Jul 30, 2026**: Documenta11y **"Starting at $4 per page"**, Allyant **"$5–$8 per
  page"**, Softek **"$5–$30 per page"**, Accessible.org **"$7.50–$11.50 per page"**; industry average
  **"$5-$25 per page"** — [venngage.com/blog/pdf-accessibility-cost](https://venngage.com/blog/pdf-accessibility-cost/)
- Existing AI entrants already price at **"$1–$4 per page"** (PREP by Continual Engine, PDFix, DocAccess).

**Machine cost (ESTIMATE):** structure detection + tag tree + alt text ≈ **$0.05–$0.40/page**.
**Gross gap: 20–350× vs. human; 3–40× vs. the AI entrants who got here first.**

**The clock:** same DOJ Title II extension as PD-3 — deadlines pushed to **April 26, 2027 / 2028** on
**April 17, 2026**. HHS §504's **May 2026** date stands.

**Why the price hasn't collapsed:** reading order, table-header association and *meaningful* alt text still need
judgment — but note what Accessiblü's own tiering reveals: the top tier's premium is **a conformance report and a
certificate**. The residual value is *attestation*, not remediation. Per the cross-cutting finding, that is the
part we cannot sell.

**Gate check** — G1 **FAIL** (public entities, higher-ed, procurement). G2 PASS. G3 PASS. G4 PASS. G5 PASS-negative.
**Killed on G1**, with a note: the only version of this that survives is *selling tooling to the ~50 remediation
vendors themselves*, which is a different surface (buyer is not the payer of the per-page price) and belongs to a
different scout.

---

## PD-5 · Insurance restoration estimate writing (Xactimate)
**Confidence: 5/10 — best demand evidence, worst buildability**

**One sentence:** Roofers and restoration contractors pay $59–$299 per claim to have someone else write the
insurance estimate, and many pay a monthly retainer to do it repeatedly.

**Evidence — T1 (published per-claim prices, fetched 2026-08-27):**
- Estimate Writers: **"ROOF ESTIMATE $59"**, **"SIDING ESTIMATE $69"**; Water Damage & Pack In/Out **"1%"** of
  estimate total with **$100 minimum**; Smoke/Cleaning **"3%"**; Hurricane **"1%"**; add-ons **"30 Additional
  Items: $25"**, **"60 Additional Items: $50"**, **"Alternative materials 'clone' or updated pricing: $25"** —
  [estimatewriters.com/pricing](https://estimatewriters.com/pricing/)
- Rebuild Estimator: **"starts at just $99 per project"**; **"$1,999 monthly retainer that covers up to 10 full
  files per month"** — [rebuildestimator.com](https://rebuildestimator.com/)
- Claims Delegates: roof estimates **"starting at $299"**. QuickPay Claims: **"$99 per hour"**, interior
  restoration **"$125/hour"**.

**Machine cost (ESTIMATE):** $0.50–$3 of model calls per file — *plus* an Xactimate licence and the ability to emit
a valid ESX.
**Gross gap on the labour: 20–100×.**

**Who buys it today:** restoration contractors, roofing contractors and public adjusters. The **$1,999/mo for 10
files** retainer is published proof of recurring, subscription-shaped willingness to pay — rare on this surface.

**Why the incumbent hasn't collapsed its price:** Verisk's Xactimate is a walled garden. Carrier-accepted line
items and the regional price lists are **proprietary data inside a licensed desktop product**, and the estimate is
an **adversarial document** — the carrier's desk adjuster pushes back on every line.

**Gate check**
- G1 — **PARTIAL.** Buyers are small contractors, self-serve, reachable in trade communities. Genuinely better G1
  than the accessibility cluster.
- G2 — **PASS**, and the strongest recurrence evidence in the file.
- G3 — **FAIL (probable).** Programmatic ESX generation against a Verisk-controlled format and price list is
  precisely the "proprietary data / platform access" failure that killed the Procore-layer candidates in the
  ledger. Verisk's terms would need reading before another hour is spent here. **Assume it fails until proven
  otherwise.**
- G4 — PASS (buy 5 estimates at $59–99, reproduce, compare).
- G5 — UNDATED.

**Killed on G3, pending a terms review.** Worth 30 minutes of someone's time on the Verisk ToS before final burial,
because the demand signal is the best on the surface.

---

## PD-6 · Patent drawings
**Confidence: 4/10**

**One sentence:** Formal USPTO drawings are sold per sheet, at $29 offshore and $100–125 domestically.

**Evidence — T1 (fetched/dated 2026-08-27):**
- QuickPatents: **"Utility Patent Drawings are $100/sheet"**, **"Design Patent Drawings are $125/sheet"**,
  **"Delivery with one week!"** — [quickpatents.com/drawings](https://www.quickpatents.com/drawings/)
- Patent Drawing Experts: **$29 per sheet** utility, **$39 per sheet** design. PatDraw: **$28 per sheet**.
  The Patent Drawings Company **$59/sheet**; Patent Drawing Plus **$75–$100/sheet**.

**Machine cost (ESTIMATE):** $0.20–$2/sheet.
**Gross gap: 15–60× — already compressed by the $28–29 offshore tier.**

**Who buys:** patent attorneys and agents (repeat, 10–100 filings/yr each) and pro-se inventors.

**Why it hasn't collapsed:** 37 CFR § 1.84 formality rules, and reference-numeral consistency between the drawings
and the specification — which is a *cross-document* consistency problem, genuinely machine-suited. The real reason
is attorney trust and a slow feedback loop.

**Verifiability: poor timing.** The verdict is a Notice of Draftsperson's Patent Drawing Review, months later. A
buyer cannot check correctness at delivery — which per the cross-cutting finding pushes the sale back toward trust.

**Race to zero: already running.** `patentdrawingai.com` is publishing on this exact keyword in 2026.

**Gate check** — G1 PARTIAL (attorneys of record on published applications are public and dated, so the *buyer
list* is free — but reaching them is cold outbound, i.e. a sales motion). G2 PASS. G3 PASS. G4 PASS.
G5 UNDATED. **Weak — the slow verification loop is the killer.**

---

## PD-7 · Book indexing
**Confidence: 4/10 — the largest gross gap in the file, on the smallest market**

**One sentence:** A back-of-book index costs $750–$1,200 on a 300-page monograph and the author pays for it out of
their own royalties.

**Evidence — T1:**
- American Society for Indexing, fetched 2026-08-27 — on who pays: **"When the indexer is hired by the publisher,
  the fee is deducted from the money due the author"**; **"In the United States, according to tradition, the index
  for a non-fiction book is the responsibility of the author. Most authors don't actually do it."** —
  [asindexing.org FAQ](https://asindexing.org/about-indexing/frequently-asked-questions/)
- Rates referenced from ASI across multiple 2026 guides: **$2.50–$4.00 per page** ($22.20–$35.52/hr).

**Machine cost (ESTIMATE):** $1–$6 per whole book.
**Gross gap: 150–1,000× — the largest here.**

**Buyer is the payer, explicitly and structurally** — ASI says so in its own words. That is an unusually clean fit
to the surface definition.

**Why it hasn't collapsed:** an index is a *conceptual* artifact, not a lexical one — the hard part is deciding what
a reader will look up, not finding strings. And the market is small enough that nobody has fought for it.

**Race to zero: already running.** IndexStudio.app, IndexerLabs and Clear Indexing are all publishing on this in 2026.

**Gate check** — G1 PARTIAL (academic authors are reachable in academic communities and university-press author
guidelines name the requirement). G2 PASS. G3 PASS. G4 PASS (index three real monographs, hand to an ASI indexer
for scoring). G5 UNDATED. **Honest read: total addressable spend is too small to justify a full-time month.**

---

## PD-8 · Zoning / land-use due-diligence reports
**Confidence: 5/10 — evidence incomplete, flagged**

**One sentence:** A per-property zoning report sells for a few hundred to a few thousand dollars and is mostly the
output of a human reading a municipal code and a GIS layer.

**Evidence — T2/T1-partial, and I must flag it:** search snippets dated 2026 report Chicago Cityscape at
**"Standard reports from $1,000"** and Zoning Inc at **"Fees start at $75 and go up"**, with LightBox PZR reports
**"anywhere from a few hundred to a few thousand dollars."** **I attempted to fetch the Chicago Cityscape pricing
page directly and got HTTP 403.** So the $1,000 figure is a dated snippet, **not verbatim-verified**. Do not treat
it as T1 until re-fetched.

**Machine cost (ESTIMATE):** browser-agent traversal of municipal code + GIS + permit records ≈ **$1–10/property**.
**Gross gap if the snippet holds: 100–1,000×.**

**Why it hasn't collapsed:** the work is *navigation*, not reasoning — thousands of heterogeneous municipal websites.
That is exactly what browser-agent capability unlocked, and it is the one candidate here whose bottleneck was
**access-to-scattered-public-data** rather than judgment.

**What stops ten others:** the accumulated municipal-code + zoning-district corpus is a real data asset.

**Gate check** — G1 **WEAK** (buyers are CRE lenders, attorneys and appraisers — a relationship business).
G2 UNPROVEN pending re-fetch. G3 PASS. G4 PASS. G5 UNDATED.
**Carry to next cycle only if someone re-verifies the pricing page.**

---

# KILLED — traps I checked and rejected

| Candidate | Published human price | Why killed |
|---|---|---|
| **Deposition / transcript summaries** | Ditto **"$3.50 per page"**; traditional **$3–10/page** | **Fully arbitraged.** SmartDepo **$85→$50/summary**, **$25 flat** on a **$99/mo** plan; eData **$0.50/deposition page**; Dodonai **from $1/page, $30/mo for 200 pages**. Ten entrants, published prices, already in a price war. |
| **Virtual staging / real-estate photo editing** | VirtualStaging.com **$24/photo** ($19.20 bulk); roOomy **from $49/photo**; VHT **~$39/image** | **Fully arbitraged.** AI Home Design at **~$0.46/photo**, Styldod **"from $1 per image"**, PhotoUp **"$1.50/image"**, **"as low as $0.50"**. The floor has already been found. |
| **Medical record review / chronology** | **$25–35/hour**; **$3,000–6,000** per 1,000–1,500-page file | **Arbitraged + liability.** Multiple AI entrants (RapidCare, Medical Insightz, MedSum Labs, Chronicle at **"$50 per case"**). Residual value is a clinical warranty we cannot issue. |
| **Nutrition Facts labels** | Food Lab **$120 first recipe, $60 each additional**; lab analysis **$50–300/recipe** | **Arbitraged to free.** ReciPal **$29/recipe or unlimited subscription**, and its **"FDA and CFIA nutrition label templates are completely free"**; Food Label Maker free tier. Plus allergen liability. |
| **Lease abstraction** | **$75–$400 per lease**; offshore **$150–350**; full-service **$250–400** | **Arbitraged.** AI-powered services already at **"$25 per export"**. Named entrants: Lextract, GrowthFactor, LeaseWizard, Layer3Labs, RExeli, Unframe. Nothing left for a cold-start operator. |
| **Alt text as a standalone service** | Publishing-house image description **"$2.00 to $30.00 per image"** | **Arbitraged.** AltText.ai free tier; Shopify's AATG at **$4.99/mo for 250 credits**. The high-value residue (long descriptions of charts/maps for EPUB) is real but is a rounding error in revenue. |
| **Bid / tender writing** | £450–£750/day (up to £1,200) | **No per-unit price published** — day rates only, and the vendors say plainly there is *"no standard price for writing a bid."* Fails the surface's own test, and G1 is a relationship sale. |
| **P&ID digitization, FAI ballooning** | — | **No published per-unit service price found.** Vendors sell software/quotes only. Cannot compute a dislocation; fails the surface's method. |

---

# RANKING AND WHAT I'D DO NEXT

1. **PD-1 Scan-to-CAD** — the only candidate that is simultaneously (a) priced per unit and published, (b)
   instantly verifiable by the buyer, (c) free of credential and liability, (d) testable in 14 days for ~$2.5k with
   nobody's cooperation, and (e) has a self-serve storefront (Autodesk App Store) rather than a sales motion.
   **First action: spend the search budget you have on Autodesk App Store install counts for existing PDF-to-DWG
   plugins and on 20 live marketplace job posts with named buyers.** That single check settles G1 and G2 together.
2. **PD-2 Solar plan sets** — best recurrence and a genuine data-asset moat; the PE-stamp boundary must be drawn
   before anything is built.
3. **PD-5 Xactimate** — best demand evidence in the file, almost certainly blocked by Verisk. 30 minutes on the
   ToS decides it.
4. Everything else is either procurement-gated (PD-3, PD-4), slow-to-verify (PD-6), too small (PD-7), or
   evidence-incomplete (PD-8).

**The one thing I would tell the next cycle:** on this surface, stop asking *"is the gap big?"* — the gaps are all
big. Ask *"can the buyer see, in under a minute, that we got it right?"* Every candidate that fails that question
is really a warranty business, and a cold-start operator has no warranty to sell.
