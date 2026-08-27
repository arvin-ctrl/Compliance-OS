# SCOUT 11 — UNBUNDLING

**Surface:** a module inside an expensive suite that has its own standalone search demand, its own
angry users, and no standalone product.

**Verdict up front:** the surface is **thin but not dry**. It yielded **one strong candidate, one
moderate, three weak**, and — more valuable — **eleven evidenced kills** and a structural finding
that should change how the engine treats this surface in future cycles.

---

## HEADLINE FINDING — read this before the candidates

**Unbundling is the most-picked-over arbitrage in vertical SaaS, and the picking already happened.**

Every module I probed with a real complaint trail already has 3–8 funded standalone vendors:

| Module I probed | Suite it sits in | Standalone vendors already selling it |
|---|---|---|
| Quoting | ConnectWise Sell | QuoteWerks, Quoter, Zomentum, Salesbuildr, ITQuoter, Socket, Datto Commerce |
| Controlled-drug log | ezyVet / Cornerstone / AVImark | VetSnap |
| Insurance verification | Dentrix / Eaglesoft / Open Dental | Zuub, Dentifi, Vyne Trellis, eAssist, Needletail, Stratus, Guardian |
| COI tracking | Yardi / AppFolio / MRI | myCOI→Illumend, TrustLayer, CertFocus, BCS, Exigis RiskWorks |
| Org documentation | Salesforce | Elements.cloud, Metazoa, Sonar |
| PDF accessibility | Adobe Acrobat Pro | CommonLook/Allyant, Equidox, axesPDF, PREP/Continual Engine, GrackleDocs, PDFix, YuJa Panorama, remediate-pdf.com (AWS+ASU+Ohio State) |
| IFTA filing | McLeod / TMW / Samsara | ExpressIFTA ($14.90/qtr), TruckingOffice, FleetCollect, TruckLogics |
| Fuel-tax / sales-tax filing | Toast | Davo ($58/mo) |
| SF330 proposals | Deltek Vantagepoint | OpenAsset ("1000+ firms"), Flowcase, RFPM.ai |

**The inference for the engine:** on this surface, *absence* of a standalone product is almost never
an opening — it is nearly always a signal that the module cannot survive outside the suite (see the
Inverse Ledger at the end). The only two places an opening survived are:

1. **A regulatory clock just manufactured a new module** faster than incumbents could re-price for it, and
2. **The module is too small for a funded startup but large enough for one operator** — specifically,
   the segment that is priced out by enterprise licences and paid *by the page or by the document*.

Candidate A1 is the only one that sits in both. Everything else below is honest but weaker, and I say so.

---

## PROVENANCE NOTE (read before trusting a quote)

Session tooling was degraded: the WebSearch budget was exhausted by other scouts (200/200) and
`reddit.com` is unfetchable from this environment. I recovered search via Brave/Bing through WebFetch.

- **Directly verified by me, primary source:** ADA.gov rule page · OSHA injuryreporting page ·
  Adobe Acrobat business pricing page · Deltek Vantagepoint help documentation · ScalePad/Quoter
  pricing page · AppFolio pricing page · Suralink pricing page · Accurate Legal Billing site +
  SoftwareAdvice listing · WebAIM discussion thread 11134 · WebAIM discussion index page ·
  Allyant comparison article · illumend.ai.
- **Search-snippet evidence (URL + date + snippet surfaced by the search engine, thread body NOT
  read by me):** every Reddit citation below. Dates and quotes are as surfaced. **Any candidate
  advanced from here must have its Reddit quotes re-read against the live threads first.** I flag
  this because the last program died of unverified foundational numbers.
- **Never invented:** where a number does not exist I have written `UNVERIFIED` or "no public price".

---

# CANDIDATE A1 — Per-document accessibility remediation, priced per document

**One sentence:** A self-serve web tool where you drop in a PDF (or InDesign/Word export), it returns
a properly tagged, PAC/veraPDF-passing file plus a remediation report, and you pay per document —
unbundling the accessibility module that everybody currently limps through inside Adobe Acrobat Pro.

**The artifact:** the remediated tagged PDF **plus** a one-page conformance report (PAC/veraPDF
result, WCAG 2.1 AA / PDF-UA checklist, list of what was auto-fixed and what a human must still
confirm) that the buyer can hand to a compliance officer or attach to an accessibility statement.
The report is the thing that gets paid for — the tagged file alone is not defensible.

## Evidence — **T1 + T2, sufficient**

**T1 — money is moving now, to humans, at published prices:**
- r/webdev, **19 Mar 2026** — someone with ~2,000 PDFs asking for price benchmarks; answers give a
  full public rate card: simple native PDFs **"$0.50–$2/page"**, complex native with tables/forms
  **"$2–$5/page"**, scanned with OCR **"$3–$8/page"**, highly complex **"$8–$15+/page"**; the
  project is sized at **"$15K–$60K"**.
  https://www.reddit.com/r/webdev/comments/1rxzxoj/how_much_does_pdf_accessibility_remediation/
- r/accessibility, **20 May 2026** — an expert's advice to an org seeking automation: automation
  "will only be very reliable… fix about **30–50% of issues**", recommends hiring remediators at
  **"$15–20 an hour"** instead.
  https://www.reddit.com/r/accessibility/comments/1tiezfl/which_are_the_best_tools_automate_pdf_data_entry/
- r/accessibility, **2 Feb 2026** — an engineer with 8 years of university remediation experience
  says his university employs **"10+ student remediators"** and spends **"thousands of dollars in
  the best enterprise software."**
  https://www.reddit.com/r/accessibility/comments/1qtpxl4/building_a_pdf_remediation_tool_that_anyone_can/
- r/accessibility, **7 Apr 2025** — thread titled *"Am I undercharging for PDF remediation?"* — a
  freelancer market with price discovery happening in public.
  https://www.reddit.com/r/accessibility/comments/1jtiqxv/am_i_undercharging_for_pdf_remediation/

**T1 — paid competitors with published prices:** CommonLook PDF ≈ **$1,500/yr**; Equidox ≈
**$2,000/yr**; axesPDF **$500–$2,000/licence**; a 2017 CommonLook commercial quote of
**CAD $15,000 annually per licence** cited by Philip Kiff on the WebAIM list. Against
**Adobe Acrobat Pro for teams at US$23.99/mo per licence / US$287.88/yr** (verified on
adobe.com/acrobat/pricing/business.html, Aug 2026).

**T2 — the module is visibly the weakest part of the suite.** WebAIM discussion thread "Tools for PDF
Remediation", **31 Oct – 4 Nov 2024**, https://webaim.org/discussion/mail_thread?thread=11134 —
Cody Michaels: *"Acrobat wasn't sufficient for the types of documents I was working with."*
Philip Kiff: *"Adobe has incorporated so-called AI features into Acrobat and you can't get rid of the
constant nagging to try it"* and *"Adobe now periodically also breaks essential functionality and
sometimes releases versions with new critical bugs."* Allyant's comparison (**21 Jul 2021**):
*"Passing Acrobat's Accessibility Check does not guarantee compliance with any accessibility
standards"*; *"Remediating data tables is a lengthy, inefficient and time-consuming process."*

**T2 — the standalone-demand queries exist and are dated:** r/accessibility "Best PDF Remediation
Tool for Freelance" (25 Oct 2024) · "What software do you use for PDF accessibility?" (14 Mar 2025) ·
"How are you folks creating accessible PDFs?" (9 Jun 2025) — that last one on an incumbent:
*"doesn't inspire a lot of confidence. Looks slow and clunky. And the pricing is not very
transparent."* · "Remediating hundreds of websites with hundreds of PDFs" (29 Dec 2025) ·
"What's the easiest way to meet Section 508 compliance for PDFs?" (15 Apr 2026).

## The clock — the strongest of any candidate on this surface

- **DOJ ADA Title II final rule**, published **24 April 2024**, effective 24 April 2024. Compliance
  deadline **26 April 2027** for entities serving 50,000+ people; **26 April 2028** for smaller
  entities and special districts. Verified at ada.gov: the rule explicitly covers
  *"word processing, presentation, PDF, or spreadsheet files"* created after the compliance date.
  Every US state agency, county, city, school district and public university is inside it.
- **European Accessibility Act** in force **28 June 2025**; French disability organisations issued
  formal legal notices to four major retailers within days, and filed **emergency injunctions in
  November 2025**.
- **Counter-clock, and it matters:** the **WebAIM mailing list was decommissioned in August 2025**
  (verified on webaim.org/discussion/). The field's central watering hole closed; the audience
  redistributed to r/accessibility, the a11y Slack and LinkedIn. That is simultaneously a
  distribution risk and the reason a new, tool-shaped hub has room.

## First ten users — nameable, and they are the freelancers, not the agencies

The buyers are **the people doing the remediation by hand**, not the government entities that
procure. Named, dated, currently-open threads:

1. r/accessibility `1jtiqxv` — freelancer pricing their own remediation work (7 Apr 2025)
2. r/accessibility `1qtpxl4` — engineer at a university with 10+ student remediators (2 Feb 2026)
3. r/accessibility `1pysx19` — dev managing 200+ WordPress sites, hundreds of PDFs each (29 Dec 2025)
4. r/webdev `1rxzxoj` — 2,000-PDF backlog, actively price-shopping (19 Mar 2026)
5. r/ArtificialInteligence `1r729ju` — educator, hundreds of scanned PDFs, hard April deadline (17 Feb 2026)
6. r/accessibility `1tiezfl` — org seeking tagging automation at scale (20 May 2026)
7. r/accessibility `1sar71z` — mid-size educational org benchmarking ASU's open-source tool (3 Apr 2026)
8. r/accessibility `1ivyrne` — small company that ground a 200-doc backlog down to 60 (23 Feb 2025)
9. r/graphic_design `1p5fphm` — designer stuck tagging infographics in Acrobat (24 Nov 2025)
10. **@theaccessibilityguy** on YouTube — named in-thread as *the* teaching resource for Acrobat
    tag/reading-order work; his audience is precisely this buyer.

r/accessibility **tolerates vendors**: an Equidox representative replied in-thread
(r/accessibility `f3auwe`) and the community engaged rather than removing it. That is a verified,
repeatable G1 path.

## Gate check
- **G1 distribution — PASS.** Ten named threads above; a vendor-tolerant subreddit; a named creator.
  Buyers are individuals with credit cards, not procurement offices. Do **not** try to sell to
  school districts — sell to the person the district hired.
- **G2 observable demand — PASS.** Published per-page rates, humans doing it hourly at volume,
  paid competitors at $1,500–$2,000/yr, university budgets described in-thread.
- **G3 buildable — PASS with a caveat.** Tagging, reading order, table structure, alt text, and
  PAC/veraPDF validation are all doable with open PDF libraries plus a vision model. The caveat is
  the ceiling: two independent 2026 threads put automation at **30–50%** and **~70% compliance
  against a 95% threshold**. This is a human-in-the-loop product, not a magic button. Design for
  "cut the human time by 70%", not "eliminate the human".
- **G4 self-verifiable in 14 days — PASS.** Take 50 real public-sector PDFs (freely downloadable),
  run them, score against PAC and veraPDF, and measure minutes-to-conformance versus doing them in
  Acrobat. No stranger required. That is exactly the test the postmortem demands.
- **G5 clock — PASS.** ADA Title II 24 Apr 2024 / 26 Apr 2027; EAA 28 Jun 2025.

## What already exists, and why it is inadequate
CommonLook/Allyant, Equidox, axesPDF, PREP (Continual Engine), GrackleDocs, PDFix, YuJa Panorama, and
**remediate-pdf.com** (an AWS + Arizona State + Ohio State project, cited in-thread at
**"about $1 per document"**). This is a **crowded field** — that is the honest headline. But every
one of them sells an **annual seat licence with opaque pricing to an institution**. Nobody sells
**per-document, no-contract, self-serve** to the freelancer and the one-person accessibility team,
which is where the money quoted above is actually being spent. Two independent 2026 threads
(`1sar71z`, `1tiezfl`) show buyers rejecting the institutional tools on price/ceiling grounds and
falling back to $15–20/hr humans.

**The load-bearing risk:** the community's own consensus answer, stated twice in 2026, is
*"convert to HTML, and only remediate the PDF as a very last resort."* If the market moves to
HTML-first publishing, this demand shrinks. It will not shrink before April 2027.

## Price signal
$0.50–$15+/page paid to humans today · $15K–$60K for a 2,000-document project · $15–20/hr for
remediators · $1,500–$2,000/yr for incumbent tools · ~$1/document for the ASU/AWS partnership ·
$287.88/yr for the Acrobat Pro seat everyone already has.

## Confidence: **7/10**

---

# CANDIDATE A2 — COI collection and verification for sub-50-unit property managers and small GCs

**One sentence:** Vendors and tenants email you certificates of insurance; this tool reads each one,
checks it against the coverage you actually require, chases the ones that fall short, and produces a
dated compliance file — for firms too small to buy the enterprise COI suites.

**The artifact:** a per-vendor compliance record (COI parsed, limits/endorsements/additional-insured
status checked against a requirement template, expiry tracked, chase emails sent) and a portfolio
compliance report you can put in front of your own insurer or lender.

## Evidence — **T2, and it needs a T1 leg before this advances**
Dated threads, all surfaced with URLs:
- r/PropertyManagement, *"COI tracking for tenants, whats the best way to do it?"* — a manager of
  **200 units** asking; answers are **spreadsheets with calendar reminders**.
  https://www.reddit.com/r/PropertyManagement/comments/1u63uhp/
- r/PropertyManagement, *"Is COI tracking actually a pain point for smaller PM teams?"* —
  https://www.reddit.com/r/PropertyManagement/comments/1pgesg6/
  **Note: this poster is another developer probing this exact wedge.** Competition is forming in
  public.
- r/PropertyManagement, *"PMs and GCs how do you track subcontractor and vendor insurance
  expirations"* — answers describe hand-rolled spreadsheets with calculated status fields.
  https://www.reddit.com/r/PropertyManagement/comments/1v35mue/
- r/InsuranceProfessional, **Dec 2024**, *"I cried today at work because i still don't understand how
  to do certificates of insurance…"* — https://www.reddit.com/r/InsuranceProfessional/comments/1hcvzc2/
- r/FreightBrokers, *"I Fell Victim to a Fraudulent Certificate of Insurance (COI)"* —
  https://www.reddit.com/r/FreightBrokers/comments/1tszcfn/
- **r/COItracking exists as its own subreddit** — a whole community named after the job.
  https://www.reddit.com/r/COItracking/comments/1icxv9m/

**The unbundling structure is real.** AppFolio's own pricing page (verified) publishes no rate at all
— only *"Minimum spend and 50 unit minimum apply. Contact us for details."* A 30-unit manager cannot
buy the suite that contains the vendor-insurance module at any price.

**Every incumbent hides its price.** myCOI (now **illumend.ai** — verified rebrand), TrustLayer,
CertFocus, BCS, Exigis RiskWorks: none publish a number. Price opacity across an entire category is
a reliable tell that the category is sold to enterprises by salespeople.

## Discriminator tests
1. **Is integration the product?** *No.* COIs arrive as email attachments and PDFs. Input and output
   are both documents. This is the cleanest doc-in/doc-out job I found on the whole surface.
2. **Switching cost?** *None.* You adopt this alongside AppFolio/Yardi/Buildium. You never rip
   anything out. Strongest structural fit of any candidate here.
3. **Self-contained?** *Yes.*
4. **Community reachable?** *Yes* — r/PropertyManagement, r/COItracking, r/RealEstateInvesting.

## Gate check
- **G1 — PASS (with a competitor already in the same threads).** Named threads above.
- **G2 — WEAK PASS.** People are visibly doing this by hand in spreadsheets, and five enterprise
  vendors sell it. But I found **no published price** anywhere in the category, and no freelancer
  market. That is a T2-only case. **Do not advance this without finding one seller with a public
  number.**
- **G3 — PASS.** ACORD 25 is a fixed form; parsing it and diffing against a requirement template is
  squarely in our capability.
- **G4 — PASS.** Collect 100 real ACORD 25s (they are widely published), build the extractor, measure
  field-level accuracy against hand-scored ground truth. No stranger needed.
- **G5 — FAIL.** I could not name anything that changed in the last 24 months. No clock.

## What already exists / price signal
Illumend (ex-myCOI), TrustLayer, CertFocus, BCS, Exigis — all enterprise, all price-opaque. Yardi
and MRI have native modules; AppFolio gates entry at 50 units. **Price signal: none published
anywhere. That is the honest answer, and it is a problem.**

## Confidence: **5/10** — best structure, weakest evidence and no clock.

---

# CANDIDATE A3 — SF330 Part I assembly, unbundled from Deltek's CRM edition

**One sentence:** Small architecture/engineering firms bidding federal work must file a Standard Form
330; Deltek automates it but **only if you buy the CRM upgrade** — this would build the SF330 from a
firm's own résumés and project sheets without the ERP.

**The artifact:** a completed, correctly paginated SF330 Part I (Sections A–H) plus the Section E
résumés and Section F project sheets, as a submission-ready PDF.

## Evidence — **T2**
- **Verified primary source, Deltek's own documentation:** *"Vantagepoint CRM Plus is required for
  the SF330 module."* — https://help.deltek.com/product/vantagepoint/6.0/DVP_Prop_SF330.html
  This is the textbook edition-gate: the form is a federal obligation, the automation is behind a
  paid CRM tier the firm may not otherwise want.
- Standalone demand is real enough to have attracted vendors: **OpenAsset** (self-described
  "Trusted by 1000+ firms"), **Flowcase**, **RFPM.ai** — all selling SF330 assembly outside Deltek.
- A dedicated hiring market exists for the manual role: ZipRecruiter lists "Federal Proposal
  Coordinator SF330" roles, average **$64,796/yr** as of 9 May 2026.

## Gate check
- **G1 — FAIL.** I could **not name ten reachable individuals**. The buyer is an A/E marketing
  coordinator; their communities (SMPS) are membership associations, not open forums, and I found no
  vendor-tolerant public thread. This is the gate that kills it for a cold-start operator.
- **G2 — PASS.** Job postings for the manual role, three vendors selling the automation.
- **G3 — PASS.** Structured data in, fixed federal form out.
- **G4 — PASS.** SF330s are published in FOIA'd award files; build one and score it.
- **G5 — FAIL.** No clock identified in the last 24 months.

## What already exists / price signal
OpenAsset, Flowcase, RFPM.ai. None publishes a price. Deltek does not publish Vantagepoint pricing.
Unanet CRM (Cosential) reported at "around $50/user/month" — **UNVERIFIED**, secondhand.

## Confidence: **4/10.** Clean unbundling structure, dead on distribution.

---

# CANDIDATE A4 — Outside-counsel-guideline pre-bill scrubber

**One sentence:** Small insurance-defence and panel-counsel firms bill through carrier e-billing
systems that reject or cut invoices for guideline violations; this would scrub time entries and emit
a clean LEDES file, without replacing Clio.

**The artifact:** a scrubbed pre-bill with each flagged entry, the specific guideline it violates, and
a LEDES 1998B/XML file that passes the clearinghouse.

## Evidence — **T2, thin**
- Clio does export LEDES 1998B/1998BI/XML 2.0/2.1 natively (Clio help centre), so the format itself
  is **not** the gap — guideline compliance is.
- **A standalone already exists and is cheap:** Accurate Legal Billing, verified listed at
  **"$30.00 per month"** starting price on SoftwareAdvice, integrating with Clio; its own site
  carries a customer testimonial — *"since we started using ALB platform in 2019, we have seen zero
  reductions from e-billing vendors."* It names Chubb, Liberty Mutual, Travelers, State Farm,
  Progressive, USAA and Farmers guideline sets.
- **Counter-signal:** that SoftwareAdvice listing shows **zero reviews**. A $30/mo incumbent with no
  visible traction is a bad neighbour — it caps our price and proves nothing about demand.

## Gate check
- **G1 — FAIL (unproven).** I could **not find named threads or handles.** r/LawFirm and
  r/Lawyertalk exist but I did not verify a single relevant dated thread. Stating this plainly rather
  than asserting a channel.
- **G2 — WEAK.** One priced competitor with zero reviews. No freelancer market found. No thread trail.
- **G3 — PASS.**
- **G4 — PASS.** UTBMS/LEDES specs and carrier guidelines are public; build and self-score.
- **G5 — FAIL.** No clock.

## Confidence: **4/10.** Include for the ledger; do not advance.

---

# CANDIDATE A5 — Occasional-use catering / BEO packet, unbundled from Toast's $100/mo catering module

**One sentence:** A restaurant that caters three events a month pays Toast **$100/month** for the
catering module; this would produce the quote, banquet event order and invoice as documents, with no
module subscription.

**The artifact:** a catering proposal, a kitchen-ready BEO, and an invoice — three documents.

## Evidence — **T2, strong on the pricing complaint, weak on the module**
This is the purest example of **per-module pricing punishing occasional users** that I found, and the
quotes are specific and dated:
- r/ToastPOS, **23 Nov 2024**, *"Toast module subscriptions are frigging expensive!"* —
  *"Want to have gift cards? $50/month! Want to use 3rd party delivery? $30/month per service!
  **Want to do catering? $100/month!** Want a handheld device? $50/month! As a very small business I
  just can't justify all of these add-ons."*
  https://www.reddit.com/r/ToastPOS/comments/1gybgod/
- r/ToastPOS, **17 Oct 2024** — *"Toast's current strategy is to bundle products you don't want to
  charge a higher price."* https://www.reddit.com/r/ToastPOS/comments/1g5k0lt/
- r/ToastPOS, **22 Oct 2025** — *"Do you guys pay Toast's $50/month per location 'Restaurant
  management suite' subscription… Is it me or is that an absurd amount to be charging just for API
  access? I'm already paying R365 $600/month for 2 locations."*
  https://www.reddit.com/r/ToastPOS/comments/1oddxsa/
- r/smallbusiness, **10 Jan 2024** — *"Is $1,000 per month in POS fees ever worth it?"*
  https://www.reddit.com/r/smallbusiness/comments/192kc3l/
- r/ToastPOS, **10 May 2025** — the lock-in quote: *"we have easily invested over 500 hours into
  optimizing and perfecting this menu setup. So we are now stuck and no doubt they know it."*

## Gate check
- **G1 — PASS.** r/ToastPOS and r/restaurantowners are active, specific, and full of named threads.
- **G2 — WEAK.** The complaint is about the *bundle price*, not about the catering module being bad.
  Nobody in these threads is asking for a standalone catering tool.
- **G3 — PASS.**
- **G4 — PASS.**
- **G5 — WEAK.** Toast's **Oct 2025 $50/mo/location API fee** is dated and real, but it works
  *against* us — it means any tool that touches Toast data makes the customer pay Toast a toll first.
- **Existing:** Tripleseat, Caterease, Curate, Total Party Planner already own event/BEO software.

## Confidence: **3/10.** The pricing anger is real; the specific module demand is not evidenced.
The genuinely useful output here is the **API-toll finding**, which belongs in the Inverse Ledger.

---

# EVIDENCED KILLS — ledger entries, do not re-research

| # | Candidate | Suite | Kill reason | Evidence |
|---|---|---|---|---|
| K1 | MSP quoting | ConnectWise Sell | **Fully unbundled, adequate.** A ten-year public thread trail (2015→2025) in r/msp uniformly recommending standalone quoting. Quoter publishes **$299/$449/$599 per month with *unlimited users*** — the exact anti-per-seat wedge, already taken. | r/msp `1ls3mce` (5 Jul 2025, Sell *"absolute garbage"*), `143isbd` (7 Jun 2023), `120wxg3` (24 Mar 2023, *"trash"*), `3kfxkw` (11 Sep 2015). scalepad.com/quoter/pricing (verified) |
| K2 | OSHA 300/300A recordkeeping | Intelex / Cority / VelocityEHS | **Incumbent is free.** *"OSHA has its own reporting software that is extremely straightforward. They even have an excel document for the 300 log."* J.J. Keller's suite at ~$1,000/yr is the paid ceiling. Verified on osha.gov: 100+ employee establishments in Appendix B industries submit Forms 300/301 "beginning in 2024", deadline 2 March. Real clock, zero price umbrella. | r/SafetyProfessionals `19e1rlp`, `1sm35dw`, `1hqf76d`; osha.gov/injuryreporting |
| K3 | Dental insurance verification | Dentrix / Eaglesoft / Open Dental | **Crowded and access-blocked.** 6+ vendors with published prices (eAssist tiers **$299/$499/$849/$1,499 per month**, urgent **$10–15/verification**). Requires payer-portal credentials (G3 access-fatal) and write-back into the PMS coverage table (integration *is* the product). | dentalbilling.com/pricing-dental-insurance-verification |
| K4 | Veterinary controlled-drug log | ezyVet / Cornerstone / AVImark | **Adequate — VetSnap owns it.** Kept as the surface's best *worked example*: see Inverse Ledger #2. | go.vetsnap.com |
| K5 | Affordable-housing (LIHTC/HUD) compliance | Yardi / RealPage | **Integration IS the product.** Yardi's own description: *"subsidy payments and housing assistance flow through the same system that tracks financials, so compliance activity syncs with cash flow rather than a standalone reporting tool."* Fails discriminator #1 outright. | yardi.com affordable-housing material |
| K6 | IFTA fuel-tax filing | McLeod / TMW / Samsara | **Price floor destroyed.** ExpressIFTA **$14.90/quarter**; FleetCollect $14/mo; TruckingOffice $20/mo. No room. | vendor pricing pages |
| K7 | Mindbody bookings / Toast POS core | — | **The module is the system of record.** Fails discriminator #2: you cannot adopt it without ripping out the suite. Operators describe Mindbody as *"difficult to leave once their business was fully built inside it."* | vibefam.com Mindbody review compilation |
| K8 | Blackbaud Raiser's Edge NXT | Blackbaud | **Angriest users I found, wrong module.** *"The most expensive and most poorly supported CRM you can get"* (24 Sep 2025); documented **23% renewal increases**, *"in three years we will be paying 40% more"* (17 Jun 2025). But the donor record IS the system of record, and the one peripheral module people want to unbundle — email marketing (r/Emailmarketing `1rphily`, 10 Mar 2026) — is the most commoditised software on earth. | r/nonprofit `1npjy72`, `1ldpjfj`, `1mtsxk9`, `1c1xix3` |
| K9 | Salesforce org documentation | Salesforce | Elements.cloud, Metazoa, Sonar all established on AppExchange. Adequate. | AppExchange listings |
| K10 | Small-landlord property management | AppFolio / Buildium | Free-to-cheap incumbents (TurboTenant, Avail, RentRedi, Zillow Rental Manager) already took the sub-50-unit segment. | vendor pricing |
| K11 | DCAA incurred-cost submission (ICE) | Deltek Costpoint / Unanet | **Fails discriminator #3 and G2.** The ICE model reconciles to the general ledger, job-cost reports and cumulative billings — continuous shared state, not document-in/document-out. And **no consultancy publishes a price** (ReliAscent, Capital Edge, RSM, BDO all quote-only), so the T1 leg does not exist. | reliascent.com/incurred-cost-proposals; dcaa.mil ICE manual |

---

# THE INVERSE LEDGER — when unbundling fails, and why

The brief asked for this explicitly. These are the five failure modes, each with evidence.

**1. The module writes back into the suite's system of record → unbundling fails.**
Dental insurance verification only pays off when eligibility data *lands in the coverage table*:
*"Fully integrated systems work from your appointment book to send requests for eligibility, gather
benefit information, and import that directly into your coverage table."* Yardi's affordable-housing
compliance is worse still — compliance events move subsidy cash. In both, the shared state is the
value. **Test to apply: if the output has to be written back, it is not unbundlable.**

**2. The unbundled winner must rebuild every integration anyway — the integration was always the
moat.** VetSnap is the surface's clean success: a standalone controlled-drug log unbundled from
veterinary PIMS. But it only works because it integrates with **AVImark, IDEXX Cornerstone, ezyVet,
Vetspire, Impromed, Shepherd, DaySmart Vet, NectarVet, Instinct and more than a dozen others**, and
runs a nightly reconciliation against invoices. The log was never the product; the twenty
integrations are. **A solo operator cannot fund twenty integrations. Prefer modules whose input
arrives as an email attachment.**

**3. Successful unbundles get re-bundled, and the window closes.** Quosal was acquired and became
ConnectWise Sell. **Quoter, the standalone that beat Sell, is now a ScalePad product** — sold
alongside Lifecycle Manager, ControlMap, Backup Radar and Cognition360 (verified on
scalepad.com/quoter/pricing). IT Glue → Kaseya; Gluh → Datto → Kaseya; myCOI → illumend. The
unbundler becomes the bundler within a cycle. **A pure unbundling play has a finite life; price and
plan accordingly.**

**4. The suite can toll-gate its API.** r/ToastPOS, **22 Oct 2025**: Toast charges **$50/month per
location** for what the operator describes as *"just for API access."* This is the same structural
move the ledger already recorded for Procore (API access revoked, Sept 2025). **Any unbundling
candidate that depends on the suite's API is holding a lease, not an asset.** The strongest
candidates read documents the *user* already possesses.

**5. The "module" turns out to be the system of record.** Mindbody bookings, Raiser's Edge donors,
Toast's POS, AppFolio's ledger. Users complain loudest about exactly these — because they are locked
in — and that anger is worthless to us, because relieving it means replacing the suite.
**Loudness of complaint is inversely correlated with unbundlability.** This is the single most
useful thing I learned on this surface.

---

# WHAT I WOULD DO NEXT

1. **Advance A1 only.** It is the only candidate that passes all five gates. The 14-day test is
   self-contained and needs no stranger: 50 public-sector PDFs, PAC + veraPDF scoring,
   minutes-to-conformance versus Acrobat. Kill it fast if automation cannot beat 50% of issues on
   native PDFs, because two independent 2026 threads say that is the ceiling.
2. **Before advancing, re-read every Reddit thread cited above against the live pages.** My quotes
   came through search snippets, not the threads themselves (see Provenance Note). This engine died
   once on an unverified number.
3. **A2 goes on the watchlist** pending one published price anywhere in the COI category. Its
   structure is the best on the surface; its evidence is the weakest. Also note a competing builder
   is already probing r/PropertyManagement in public.
4. **Retire this surface after this cycle.** The headline finding stands: unbundling is a harvested
   arbitrage. Future cycles should spend their budget where a clock *manufactures* a module rather
   than where a suite merely overcharges for one.
