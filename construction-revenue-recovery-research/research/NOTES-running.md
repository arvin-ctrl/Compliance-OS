# Running notes / corrections (orchestrator)

- **Extracker IS Clearstory.** Rebranded 27 Jun 2023. One company. Do not treat as two competitors.
- **Semantic trap: "claim".** In InEight (and much of heavy-civil / earned-value tooling) "claim" means
  *progress/quantity claiming* (earned value), NOT contractual claims. Do not mis-score on keyword match.
- **Levelset precedent** to be resolved by agent 08: statutory lien deadlines vs contractual notice deadlines.
- Recurring cross-agent signal to test in synthesis: **evidence fragmentation is weakest where incumbents are
  strongest (heavy civil / mega-projects), pushing any wedge toward commercial building + mid-market.**

## Thesis-threatening findings (must survive red team)

1. **The eSUB natural experiment.** eSUB marketed the thesis verbatim for years
   ("It's not about the work you did; it's about the work you documented") to exactly the right buyer
   (subcontractors), and is the smallest, slowest-growing company in its category (~16k users, ~60 staff).
   Reading: *"better documentation" is a cost, not a benefit, and does not sell.* Any product here must be
   sold on **quantified recovered dollars**, never on documentation hygiene.
2. **Pricing architecture lock-in.** The entire field layer prices at $15-90/user/month as tooling, which
   structurally prevents those vendors from pricing at recovery economics — this is an opportunity, but it
   also shows the segment's *anchor price* is low.
3. **HCSS diary demo says the quiet part out loud** ("Johnson Concrete showed up three hours late.
   At $1,500 a crew hour, that's a lot of money") and then does nothing with it. Detection substrate exists;
   the commercial step is deliberately unbuilt.

## Corrections / unverified
- "HCSS Skyline" (named in the orchestrator's brief) appears not to exist as a product. Flagged UNVERIFIED.

## PROCORE — the central strategic fact of the program

**Threat.** May-Jul 2026 Procore converted the Datagrid acquisition into 20 GA agents including
**Contract Review**, **Change Analysis** (GA 23 Jul 2026: "identifies scope impacts, cost exposure,
schedule risk, and required follow-up actions" from changes, RFIs, drawings, specs, project records),
**Schedule Analyst**, **Financial Analyst**, plus **Triggers** (fire on new RFI/submittal/change order),
**150+ Actions** (write Change Events), **Skills** (upload own SOPs), on a credit-consumption model.
=> Steps 1-3 of the thesis pipeline are already shipped by the platform of record.

**Moat closing.** Developer Policy (eff. 30 Sep 2025) forbids developers to "Scrape, **parse**, harvest,
**build databases**, bulk export, or otherwise create copies of any API Data" without consent, and forbids
using API Data to train/fine-tune/benchmark AI. Procore now has direct revenue reason to keep third-party
AI off its data. **This alone may kill hypothesis E (commercial-risk layer above Procore).**

**The seam Procore structurally cannot enter.** Owner, GC and sub are ALL Procore customers on the same
project records. Procore can never compute "your client owes you $412k and here is why they are wrong."
Confirmed by product shape: 24 correspondence templates incl. Early Warning Notice / Notice of Delay /
Extension of Time, but a Change Event has NO field for clause reference, notice date, notice deadline or
entitlement. No quantum, no evidence-completeness scoring, no claim package — in the product or in all 446
marketplace apps.
=> **Taking a side + putting a number on it + producing a document aimed at another Procore customer**
   is the one framing incumbents cannot copy. This is the strongest defensibility candidate so far.

**Distribution warning.** Document Crunch has 187 installs against Procore's 17,850 customers (~1.0%) after
four years of partnership. **The Procore marketplace does not distribute commercial-risk products.**
Any GTM plan that relies on the marketplace is already falsified.

**Demand-articulation warning.** No reviewer anywhere complains that Procore fails to protect entitlement or
warn about notice deadlines. The pain is NOT articulated as a Procore gap => the buyer will not arrive via
that search term. Inbound/SEO GTM is suspect. (Caveat: Reddit blocked, G2/TrustRadius 403 during this pass;
review read is Capterra-weighted and needs a second pass.)

## LEVELSET — resolves hypothesis A (missed notice deadline prevention). It is a CAUTIONARY comp.

Procore paid **$484.1M** for Levelset (~19-22x revenue; ~$22-25M ARR). But every mechanism that made
statutory deadline tracking monetisable is **absent** from contractual notice:

| Levelset (statutory) | Contractual notice |
|---|---|
| Public rules corpus authored ONCE (50 statutes), sold to everyone | Per-contract variable cost, authored every time |
| Bright-line catastrophic consequence (lose lien right) | Fuzzy, arguable, often waived in practice |
| 5-field trigger, zero integration needed | Needs project event data |
| **A chargeable filing: $59/notice, $349/lien** | **No filing, no clerk, no fee** |

**The alert was free bait; the FILING was the revenue.** Contractual notice has no filing to sell.
Further: Procore de-emphasised it — "Lien Rights Management" was deleted from the product catalogue between
the FY2023 and FY2024 10-Ks (zero mentions FY2024/FY2025), and Procore assigned Levelset customer
relationships a **4-year life vs 10 years for LaborChart/Intelliwave** (i.e. they modelled ~2.5x faster churn).

=> **Hypothesis A (notice-deadline prevention as the product) is weak on its own.** Deadline alerting is a
feature, not a business, unless attached to a chargeable artefact.

## Where the leak actually is (frequency comparison, same-source-quality)
- **97%** of specialty contractors start change-order work before authorization; **77%** have written it off
- **56%** of subcontractors missed a critical lien deadline in past 2 years (Siteline 2026, n=492)
=> the unauthorized-CO leak is ~1.7x more common than the statutory-deadline leak, and Clearstory holds only
   the *logging* layer, leaving **entitlement + evidence + valuation** open.

=> **Attach the wedge to a billable dollar at billing time, upstream of the pay app — not to a deadline alert.**

## Legal exposure flag
Procore carries a standing **UPL (unauthorized practice of law) risk factor**. It will be *worse* for any
product interpreting contract clauses and drafting notices. Red team must attack this.

## COMMODITISATION OF THE FRONT HALF (confirmed from two independent agents)

- Trunk Tools gives away a **free, no-account AI contract review tool** extracting "Notice Deadlines &
  Methods", "Change Order Procedures", "Delay & Liquidated Damages", "Dispute Resolution" and returning a
  "compliance calendar, critical deadline matrix, delegation chart by role" — as LEAD-GEN, from a company
  reported at $325M valuation.
- Procore shipped a native **Contract Review agent** (21 May 2026).
- Document Crunch already **generates notices** (per Clearstory agent).

=> **Clause extraction + deadline listing is at or near zero price.** Any wedge that IS this is dead on
   arrival. Defensible ground is downstream: entitlement *reasoning*, causation, dollarisation, and the
   notice/claim artefact.

## PLATFORM RISK — now confirmed, not theoretical

**Procore denied Trunk Tools API access (Sept 2025)** and refunded its Groundbreak booth. Marketplace
enumeration 19 Aug 2026: 455 apps, **zero "trunk"** — while Document Crunch, Clearstory, Datagrid and
SmartPM are all listed. A $70M-funded, Insight-backed company with 200+ Gilbane projects was cut off.
A solo founder has no better standing.

=> Any V1 depending on Procore API access is betting the company on a permission Procore has already
   revoked from a better-capitalised player. **Reinforces: file-upload / email-forward V1.**

## COUNTERINTUITIVE ADVANTAGE
Because the best-funded incumbents cannot legally read Procore data, a **file-upload / email-forward V1 has
better commercial-record coverage than they do.** Ingest constraint is a moat, not just a limitation.
Also note: Trunk Tools has NO email/Outlook connector and NO daily-log agent — the two richest sources of
contemporaneous commercial record sit outside the best-funded competitor's corpus.

## *** STRUCTURAL CHANGE: TRIMBLE ACQUIRED DOCUMENT CRUNCH ***
**$246.4M cash, closed 4 Apr 2026.** $39.4M net identifiable assets, **$207.0M goodwill** (84% of price =
future product/synergy). Source: Trimble 10-Q, https://www.sec.gov/Archives/edgar/data/0000864749/000086474926000108/trmb-20260703.htm

Consequences:
- Document Crunch is NOT an independent startup competitor. It is now the contract-intelligence layer of a
  $1.577B-ARR AECO business. Trimble SVP: it is "a contractual rule set... the intelligent DNA for the entire
  Trimble Construction One suite." CEO framing is construction litigation risk.
- Since **9 Jun 2026** (post-close) it **agentically generates notices, RFIs and submittals**.
- => **Contract-clause-AI as a V1 is dead.** Confirms the commoditisation note above from the other direction:
  the front half is now owned by a strategic, not merely given away by a startup.

**What remains uncontested** (absent from Document Crunch product pages, Trimble cost docs, and every agent on
Trimble's 2025-26 AI roadmap):
  1. event detection from *project data* (not contract text)
  2. causation / responsibility attribution
  3. contemporaneous evidence sufficiency
  4. recoverable-dollar quantification

## Strongest single white-space datapoint found so far
e-Builder's official **Cost Guide (340,174 chars)**: 745 mentions of "invoice", 611 "funding",
306 "commitment change" — and **ZERO** occurrences of "claim", "dispute", "entitlement", "delay",
"backcharge", "liquidated damages", "time extension".
https://help.e-builder.net/Content/PDFs/e-Builder-Cost.pdf

## The recurring structural moat (now confirmed at THREE incumbents)
Procore, Trimble and Clearstory all sell to BOTH sides (owner + GC + sub) on the same records.
None can build a tool that takes a side. Trimble's split is explicit: claim identification and dollar
quantification are *deliberate* omissions (a contractor claims tool attacks the owner franchise generating
half of AECO's $1.5B ARR); delay analysis and ball-in-court are merely *unattended*.

## API hostility, second data point
Viewpoint Vista API returns only **12 months of history** — structurally prevents retrospective claim
analytics from the cloud API. (Trimble Unity Construct: 15,000 calls/day, HTTP 426 on exceed.)

## ORACLE / ACONEX — resolves "is Aconex already the contemporaneous evidence graph?"

**Answer: it is the evidence WAREHOUSE, never the evidence GRAPH.**
Because "information is private until shared" and "there is no super user", **no single party can ever query
the whole project record.** That is a design guarantee sold to owners, not a bug — and it means the
cross-record graph the thesis proposes cannot be built inside Aconex by anyone, including Oracle.

**But: Aconex scores 3 on deadline_tracking.** Response-required is enforceable per mail type, due dates
auto-calculate in *working days* against the project working week, status auto-flips Outstanding->Overdue per
recipient. On an Aconex project, "we alert you when a notice is due" is ALREADY SOLVED AND CONFIGURED.
=> Third independent confirmation that **deadline alerting cannot be the wedge.**

**Why Oracle cannot follow:** Aconex is mandated by *owners* on the strength of neutrality. An entitlement
engine that tells one party it has a claim against another destroys the franchise. Nine years post-acquisition
its only shipped AI is a *safety* predictor; the Apr 2026 flagship release was review routing and ITP packs.

**Mid-market is deliberately excluded** — 25-seat minimums (P6 EPPM, Unifier), project-value metric,
non-cancellable terms, partner-led implementation. Oracle prices egress into its own BI tool at
**GBP 799/month per data-source connector**, and P6 API access is a separately licensed SKU (GBP 36/user/mo).

## *** MOST ACTIONABLE FINDING OF THE PROGRAM SO FAR: XER IS THE FREE PATH IN ***
- Oracle publicly documents XER field mappings: https://docs.oracle.com/cd/G48897_01/102093.htm
- **Contracts already mandate monthly XER deliverables** — the file is already being produced and sent.
- Prior art proves it works with zero Oracle relationship: XER Schedule Toolkit, Schedule Auditor, ScheduleLens.
- Forensic delay analysis runs on **dated snapshots anyway**, so upload loses NOTHING evidentially.
=> **Upload beats integrate on cost, speed, legal risk AND procurement — with no evidential penalty.**
   This is the single strongest support for the solo-founder upload-first V1.

## DOCUMENT CRUNCH — the boundary is now precisely located

**The decisive distinction: they moved DOWN THE TIMELINE (pursuit -> execution -> closeout) but NEVER CROSSED
THE DATA BOUNDARY** from static documents into project records.
They ingest: contracts, specs, addenda, flow-downs, drawings. **And nothing else.**
Consequently: no event detection, no deadline clock, no contemporaneous evidence, no dollar quantification,
no claim package.

Proof of the boundary, hard:
- Their Procore app requests **ZERO data permissions**: `components:["sidepanel"]`,
  `permissions:{"company":{},"project":{}}`, `connector_required:false`. **It reads nothing from Procore.**
- **187 installs, 0 ratings, no app release since Feb 2025** — against 400+ customers / 10,000+ projects.
- **Notice Builder (GA Oct 2024) is 100% human-triggered**: "you'll select the event type then describe what's
  going on and the relevant date"; for the deadline, "use your playbook or chat to find your submission
  instructions." The human must already KNOW an event occurred and that a notice is due.

=> **Notice DRAFTING is taken. Notice TRIGGERING is not.** Any V1 that stops at drafting is a feature.

## *** STRONGEST VALIDATION IN THE PROGRAM ***
Document Crunch's own Jan 2026 primary research names the exact thesis pain verbatim:
> "Project managers learned too late that **notice windows had already closed, converting otherwise valid
>  claims into absorbed costs**"
...lists "Notice Requirement Failures" among 7 causes of post-award margin erosion — **and then prescribes a
purely upstream remedy ("brief the team better").**
They have every asset needed to watch the project and have PUBLICLY CHOSEN NOT TO.

**Why they won't cross it:** "zero disputes" is the literal vision statement, written by two ex-construction-
claims lawyers who also sell to owners, insurers and sureties. The refusal is identity-level, not roadmap-level.
=> This is the cleanest incumbent-refusal evidence in the program. Partner window est. 12-24 months.

## *** MOST DANGEROUS COMPETITOR FOUND: GATHER (gatherinsights.com) — UK/NEC4 ***
**The thesis is already running, with proof, in the UK NEC4 market.**
- Team: ex-**CEMAR founder** Ben Walker (an NEC4 drafter) + ex-Thinkproject UK COO Nick Woodrow.
- 8-year site-record corpus inherited from **Rail Diary Ltd** (renamed to Gather 16 Jan 2024, Companies House 10215108).
- QS AI Agent **detects compensation events off diaries** and **drafts clause-cited notices**.
- Two-way Procore sync + public API + MCP server.
- GBP 25bn+ project value, 4,500+ daily users, 10M+ records.
- Named recoveries: **GBP 300k at Network Rail (39x ROI)**, GBP 140k at Circet/TfL (15x ROI);
  Costain, Balfour Beatty, Amey case studies.
- **Missing only quantum.**
=> ROADKILL if we fight them in UK NEC4. Their existence VALIDATES the mechanism and their gap (quantum)
   plus geography (US) defines the opening.

## *** THE CLEANEST STATEMENT OF THE OPENING, FROM THE PLATFORM THAT OWNS THE DATA ***
**Datagrid (a Procore company) explicitly refuses to automate entitlement:**
> "entitlement and approval stay with the responsible project professionals"
The platform holding all the data has drawn its line EXACTLY where the defensible business begins.

## NEC4 niche has real enterprise pricing (refutes "contractors won't pay")
- **CEMAR: GBP 435/licence/month**, administering **GBP 75bn of works**
- FastDraft GBP 250; Sypro GBP 25-65/user; Contract Bee GBP 30-49.99/user; Oracle Unifier NEC4 GBP 107-585/user
=> GBP 435/mo/licence ~= USD 550/mo. **The $500-$5,000/mo band is proven in the NEC regime.**
BUT: all six mature NEC systems administer events **after a human identifies one**. None detects.

## Funding-signal check (cuts both ways)
Across ~$250M of 2025-26 contech funding (PermitFlow $54M, Attentive $30.5M, Fyld $41M, Sensera $27M,
XBuild $19M, Kojo $10M, Planera $8M...), **ZERO went to a claims/entitlement/notice startup.**
Read either as (a) unvalidated category, or (b) uncontested category. Red team must adjudicate.

## Weak claims-AI cohort (do not mistake for competition)
Magra, Lexilio, ClaimMaster.ai, Delay Claim Builder, Aven-AI: publish product and pricing but **not one named
customer** for the claims workflow, and price a six-figure value event at **$29-$300/month** — prosumer pricing
for an enterprise consequence. Magra claims 92% detection / $240k per event / 658x ROI while listing EVERY
integration as "Upcoming" and naming zero customers. Treat as demoware.

## GAPS THIS PASS DID NOT CLOSE (gap-fill agents launched)
1. Non-English markets, esp. German **Nachtragsmanagement** — under-covered.
2. **Zero independent customer complaints** obtained; G2/Capterra have no "construction claims" category.
3. Whether Gather is entering the US / AIA-contract market.

## *** THE STANDARDS FORECLOSE PART OF THE THESIS — HARD CONSTRAINT ON V1 SCOPE ***

**Automated responsibility attribution (dimension 12) is not merely hard, it is standards-blocked:**
- AACE RP 29R-03 §1.2(f): *"Schedules are a project management tool that, in and of themselves, **do not
  demonstrate root causation or responsibility for delays**."*
- AACE §1.3(c) scopes forensic schedule analysis to quantification *"as opposed to assignment of delay
  responsibility"*.
- AACE §1.2(d): *"all methods are subject to manipulation as they all involve judgment calls by the analyst"*.
- AACE §1.1 purpose is to *"minimize the need to contend with 'black-box' or 'voodoo' analyses"*
  => **any automated attribution verdict hands opposing counsel a ready-made attack.**
- SCL Protocol 2nd ed, both windows methods: *"the analyst investigates the project records to determine what
  events might have caused the identified critical delay."* (human investigation is the method)
- Steelray, which implements the AACE half-step, states plainly: *"The tool does not attribute responsibility
  to parties."*

**Also threatens dimension 15 (recoverable-dollar estimation):** SCL Core Principle 12 — an EOT does NOT carry
compensation, and "non-compensable Employer Risk Events" exist.
=> **any auto-generated `delay days x daily rate` figure is WRONG BY CONSTRUCTION for a whole class of events.**

### Consequences for V1 (carry into synthesis and MVP definition)
1. Do NOT ship an automated "who is responsible" verdict. Ship **evidence assembly + the argument**, with the
   human making the call. Position as *"here is what the record supports"*, not *"you are owed X"*.
2. Do NOT ship a naive delay-days x rate number. Must separate **time** (EOT) from **money** (compensable).
3. Schedule-impact analysis is the WEAKEST candidate component of a V1 and should probably be deferred.

## Category is commoditised where computable, absent where documentary
Identical AACE half-step arithmetic sells at $2,750 perpetual (Ron Winter) / $3,990/user/yr (Steelray) /
$25,000/yr (SmartPM Controls; Essentials $12,000/yr for 50 projects, unlimited users).
**No contract, clause, notice, RFI, daily-report or email ingestion ANYWHERE in the category.**
Gaps are deliberate and standards-backed => NOT automatically white space (brief rule applied).

## Solo-founder-positive finding
**nPlan's 750,000-schedule moat guards the wrong door.** Causation is per-project document reasoning, not
cross-project statistics. Both governing standards are public (SCL free, AACE free to members).
=> **No proprietary dataset is required to compete on entitlement.** Directly answers RQ on data moats.

## SmartPM = free delay windows
Open API: "raw schedule data and all the metrics we calculate... No extra fees. No limits."
Holds Procore + Autodesk + Egnyte OAuth but pulls only the schedule file. Stops exactly where thesis starts.

## LEGAL-TECH / CLM — answers "why hasn't horizontal obligation management taken construction?"

**They built hypothesis A to full maturity — and pointed it elsewhere.** Sirion already sells it with numbers:
99% on-time obligation compliance, 80% fewer post-signature disputes, 8-12% spend-leakage reduction.
But it is anchored to **renewals, terminations and SLAs**, sold at **~$88k median ACV** to enterprise
Legal/Procurement, wired to SAP/Salesforce/Workday.
- **Icertis' full published integration list contains ZERO construction systems** — no Procore, no Autodesk,
  no Aconex. Sirion's 8 verticals and Agiloft's 7 exclude construction entirely.
- Not one vendor ingests an RFI, a daily report or a schedule. Not one asserts entitlement.
- Recurring buyer complaint — *"too many dependencies on back end team for configuration"*, *"uploading
  third-party contracts is difficult"* — is **exactly the failure mode that kills CLM in construction**, where
  every subcontract is third-party paper and nobody has a configuration team.
=> The reason is durable (buyer, wiring, ACV, config model), not a timing accident.

## *** PRICING CEILING — hard constraint on the pricing hypothesis ***
- DocuSign IAM: **$45/$50/$80 per user/month**, all tiers include "AI-powered data extractions"
  => the commodity price of structured contract data.
- M365 Copilot at $18-30/user/mo already answers "what are my notice deadlines".
- Vals Legal AI Report (27 Feb 2025): best AI data extraction **75.1% vs 71.1% lawyer baseline**;
  Document Q&A **94.8% vs 70.1%**; redlining 65.0% vs 79.7% (**AI loses at redlining**).
- Relativity now bundles aiR at **no additional cost** with RelativityOne.
=> **Contract READING cannot be the product. Per-seat pricing is capped ~$50-150/user/mo.**
=> Therefore pricing must be **per-project / per-event / per-recovery**, not per-seat. Carry to pricing section.

## Template risk (and proof of mechanism in another vertical)
**Eve** ($103M Series B, 1,200+ plaintiff law firms) runs **"nightly audits of active caseloads to surface
missed opportunities"** — structurally identical to the thesis, proven in a different vertical. A well-funded
template that someone can point at construction at any time.

## Construction is already buying horizontal contract AI — for the wrong half
Luminance's one real E&C customer, **Buro Happold**, bought it for **pre-signature legal review** (90% time
savings), with no mention of notices, claims or NEC/FIDIC/AIA.
=> Demand for contract AI in construction is demonstrated; demand for *entitlement* AI is still unproven.

## AUTODESK — buys categories rather than building them; and one exploitable asymmetry

**Acquisition pattern is the strategic fact:** paid **$387M cash for Payapps/GCPay** (closed 20 Feb 2024)
*despite already shipping payment applications in Cost Management*; agreed **~$3.6B cash for MaintainX**
(28 May 2026). AECO revenue $3,583M, +22% YoY.
=> Proven move is **buy the category at nine figures rather than build it.** Acquisition path is real,
   but so is "they will simply purchase the category away from you."
**Their 194-partner marketplace has ZERO claims/entitlement/delay vendors** — second marketplace with the
same void (cf. Procore 455 apps, none commercial-risk).

**Threat — commercial event detection already shipped:** Autodesk Build ingests **external email natively**
(Correspondence, unique Project Email Address, threaded replies, custom types, references), and its
**RFI AI assistant auto-populates Cost Impact and Schedule Impact from free text**, logged to an activity log.

**Deliberate limit:** Pype — their only clause-extraction asset — is pointed at **Divisions 01-49 technical
specs** (submittals, tests, closeout) and **never Division 00 general conditions, where notice and claims
clauses live.** Six years of narrowing, not extending (SmartPlans + eBinder **withdrawn from sale 26 Mar 2024**).
No notion of entitlement, notice, time bar, EOT days, delay causation or claim anywhere. Construction IQ's
four risk domains (design/RFI/quality/safety) never touch commercial. Every AI surface carries a
"requires verification" disclaimer => no legal-exposure appetite.

## *** EXPLOITABLE ASYMMETRY ***
**Correspondence is the ONLY major object with no public API and no Data Connector export.**
Autodesk captures the richest claim evidence **and cannot get it back out.**
Meanwhile **Data Connector hands a solo founder the entire evidence graph as scheduled CSV — free, unrated
APIs — including relationship edges ("RFIs that relate to PCOs").**
=> **Build on email you ingest yourself; never depend on theirs.** And CSV export is a legitimate,
   policy-safe ingestion path (contrast with Procore's anti-parsing Developer Policy).

## *** ECONOMICS — THE CORE NUMBERS (agent 11) ***

- **HKA CRUX 8th (Nov 2025):** across **2,200+ projects / 114 countries / $2.433tn**, contractors claimed
  **$95.0bn = 33.4% of budgets and 65.8% of schedules**. Stable within 1pt across three refreshes
  (33.6 / 33.2 / 33.4) => this is a structural constant, not a cyclical blip.
- **Arcadis 16th (2026):** US average dispute **$56.0m / 12.2 months**. BUT **39% of disputes are <$5m and
  ~73% are <$25m**. **The distribution is the market, not the average** — and the sub-$25m band is exactly
  what consultants cannot serve economically.
- **Arcadis 2022: "Poorly drafted or incomplete and unsubstantiated claims" was the #1 GLOBAL CAUSE of
  construction disputes.** The incumbent's own report says **bad claim evidence, not bad building, drives
  disputes.** Strongest single validation of the thesis mechanism found anywhere.
- **Rates:** Exponent **$225-$1,375/hr** published card; FTI FLC realised **$442/hr in 2025** at 57% utilisation.
- **Full delay+quantum claim on a $5-25m dispute = 600-1,650 hours / $240k-$660k**, of which
  **200-600 hours is document review and chronology** (the automatable part).
  Anchor: **£750,000** spent on Knowles by one employer, recorded verbatim in *Walter Lilly v Mackay*.
- **Diales (only listed pure-play): £43.0m revenue -> £1.4m underlying operating profit = 3.3% margin.**
  That is what "no product leverage" looks like on a P&L.
- **Consultants cannot self-disrupt:** an hours business at 57-73% utilisation cannot fund the destruction of
  its own hours; in ~9 years of aggressive M&A none of the twelve firms has bought or built a claims-detection
  product. HKA's CRUX dataset only counts a project once **>30 hours** of claim work exists — they literally
  cannot see the pre-dispute phase.

## *** THE CASE THAT SELLS THE PRODUCT ***
**Van Oord v Allseas [2015] EWHC 3074 (TCC)** — a **~£10m claim failed entirely** and the claimant was ordered
to repay **£1,895,349.89 + £588,882.98**, because Daily Progress Reports did not record standing time and every
notice was out of time. https://caselaw.nationalarchives.gov.uk/ewhc/tcc/2015/3074

## *** THE HONEST HOLE IN THE THESIS — RED TEAM MUST ADJUDICATE ***
**Nobody publishes a figure for claims lost to poor records or missed notice.** The practitioner literature
that describes the mechanism most precisely (Long International) **states explicitly that it contains no data**.
The thesis currently rests on: one judgment with numbers (Van Oord), its mirror-image case, and a #1
dispute-cause ranking from 2021.
=> Either (a) a fatal evidence gap under the brief's "missing feature is not white space" rule, or
   (b) THE opportunity — a startup that quantifies record-quality vs claim outcome across even 50 real matters
   would own the only number in the industry. Currently unoccupied.

## Performance pricing — resolved
**Contingency is LEGAL for claim preparation, effectively barred for testifying experts**
(CJC Guidance para 88; *Factortame No.8*: "a rare case indeed"). The industry ALREADY separates the two roles.
=> **That separation is the seam performance pricing can legitimately occupy.**

## GTM implication
Consultants = **CHANNEL first** (sell chronology automation into their analyst layer — file-upload V1, they
rebill it), **PARTNER structurally**, never roadkill. 200-600 chargeable hours of document review per matter is
the wedge's first revenue.

## *** THE CONTRACT-FORM QUESTION IS RESOLVED (agent 17) ***

**"The contract form does not manufacture DEMAND — it manufactures the product's SHAPE. Mandated notice is
neither necessary nor sufficient."**

Evidence: Germany, Sweden, Norway and Italy all impose notice regimes as strict as or stricter than NEC4
(Italy's *riserve* forfeits the claim outright) and **all four produced ZERO entitlement products.**
Sweden/Norway produced only mobile approve-and-invoice logging — **exact clones of Clearstory.**

The register-and-clock product (CEMAR, Gather, CALIM) appears **only** where the form supplies
**(a) an integer deadline AND (b) a named administrator.**
- NEC4 has both => CEMAR/Gather exist.
- Germany has neither — VOB/B §6(1) says "unverzüglich" (unclockable) and §6(1) S.2 **forgives omission where
  facts were *offenkundig*** => Germany built notice **drafting** instead, not tracking.
- **Corroborating tell: Thinkproject (Munich) has owned CEMAR since 2018 and has NEVER built a VOB/B
  equivalent for its home market.**

=> Applied to the US: AIA has neither an integer deadline that reliably bites nor a named administrator.
   **Do not copy the Gather/CEMAR register-and-clock shape into the US.** (Await agent 16 for the
   US-enforceability half of this question.)

## German regime detail (relevant if EU is ever a target)
- VOB/B **§2(6)** requires announcing the claim **BEFORE starting the work**; **§4(3)** requires a
  Bedenkenanzeige; §6(1) the Behinderungsanzeige. **Three mandated pre-emptive notices — and no German notice
  product exists.**
- German Bauhauptgewerbe 2025: **EUR 171.9bn revenue (+2.4% real), EUR 113.0bn orders (+9.2%)**.
- **GAEB / GAEB DA XML** = Germany's XER-equivalent free ingest path, and it carries the **priced bill of
  quantities** — i.e. a quantum baseline, which XER lacks.

## Universal gap confirmed across ALL languages
**Every AI claims product in every language scores 0 on recoverable_dollar_estimation** — Contradic, SmartClaim,
BauAgent, ContraVault, Ronayz alike. The only product doing quantum well (**Easyclaim, EUR 599 net per case**,
21-page derivation over 26 cost categories under §642 BGB / §6(6) VOB/B) has **no AI, no ingest, and runs
offline as a single HTML file**, operated by one Sachverständiger.
**No European product does causation/disruption analysis** — Germany's BGH-mandated *bauablaufbezogene
Darstellung* is still executed **by professors by hand in MS Project and Excel.**
**No vendor anywhere detects events from passive project data**; German trade press asserts it as a 2026 trend
and **credits no vendor with it.**

## FOURTH independent falsification of inbound/SEO GTM
In German, French, Norwegian and Dutch the pain is articulated as **legal complexity** or **behavioural
discipline** — never as a software gap. (Prior three: Procore reviews, G2/Capterra having no construction-claims
category, zero contech funding to the category.)

## Transplantable pricing line
BauAgent.ai: **"one Nachtrag finances the annual subscription."** Most directly transplantable framing found.
Also: Contradic **EUR 199/user/mo (EUR 1,990/yr)** Team, from EUR 349/user/mo Enterprise — with **zero quantum**.

## *** GATHER RE-SCORED — THE PRIOR READ WAS WRONG (agent 16 supersedes agent 12) ***
SCORES.csv row replaced. Key deltas: recoverable_dollar_estimation 2->**1**, change_order_workflow 2->**1**,
procore_integration 3->**2**, rfi_event_ingestion 2->**1**. claim_identification held at 3.

**1. Gather does NOT do quantum, and says so.**
Product page: *"Cost Impact — cost of extra materials, labour, and plant **to be calculated**."*
Jul 2026 blog: the agent *"surfaces the records that back a compensation event... the substantiation is already
assembled"* — then teaches a human QS to price it by hand. **The GBP 21k cascade panel is a marketing mockup.**

**2. The "named recoveries" are NOT recoveries.**
- Network Rail **GBP 300,000+ is a CLIENT-SIDE SAVING** — money **withheld from the contractor** after Network
  Rail used Gather *"to scrutinise labour, plant and time allocation... included in change requests."*
- Circet **GBP 140,000 is admin labour** (GBP 1,012/wk + GBP 2,400/wk).
- Costain A12 headline: *"15% of claims rejected on the spot."*
- **Across ELEVEN case studies, not one documents a recovered CE in GBP.**
=> The most on-thesis product in the world is evidenced as a **claims-DEFENCE and efficiency tool**, not a
   recovery tool. This materially strengthens hypothesis G (owner-side defence) and weakens the naive
   contractor-recovery pitch.

**3. Gather is small and shrinking.** 10 average employees FY2026, **down from 14**; net assets GBP 537,435;
cash GBP 134,699; loss GBP 93,424; lifetime equity ~GBP 713,163 (angels only, ~GBP 2.5m post-money Jul 2024).
Flat **GBP 500/licence/month, "not priced per User"**, no value component despite publishing 39x ROI.
**No Procore Marketplace listing at all** (verified against the full 539-app catalogue). Public API = 18 mostly-GET
endpoints with **zero compensation-event or entitlement objects**. Two of four About-page leaders have resigned
as directors.
=> Not roadkill in the US. Most useful as a **free, eight-year, publicly-audited feasibility study.**

## *** THE US BEACHHEAD IS STATE DOT, NOT AIA ***
**AIA does not port.** A201 §15.1.3.1 names 21 days and stops — **no waiver clause anywhere**; §15.1.3.2 imposes
no limit at all. NEC4 61.3 passes **both** limbs of the *Bremer* condition-precedent test (names the time AND
states the forfeiture); AIA passes only one. US courts split ~half on excusing late notice; **federal boards
excuse it by default with the prejudice burden on the Government** (*Hoel-Steffen*, 456 F.2d 760, 768: notice
"should not be applied too technically and illiberally where the Government is quite aware of the operative
facts"). FAR 52.243-4(d)/52.242-14(c) bar costs incurred **more than 20 days before** written notice.
=> **The "you'll lose your claim" fear pitch is genuinely weaker in the US.** Confirmed.

**EXCEPT state DOT — and this is the beachhead:**
**Caltrans** Std Specs §§5-1.42-5-1.43D: Initial Potential Claim Record in **5 business days**; Supplemental with
**itemised cost estimate + TIA in 15 days** (i.e. costed by day 20); failure = *"Waiver of the potential claim...
Bar to arbitration (Pub Cont Code §10240.2)."*
=> A hard statutory fuse **AND a mandated costed estimate + TIA on a 20-day clock.**
=> **This is simultaneously the beachhead and the proof that the quantum gap IS the business.**

## *** CM-B VERDICT: QUANTUM IS CONFIRMED EMPTY — AND THE REASON IS ACTIONABLE ***

**Pipeline occupancy — FREE stages:** (a) contract ingestion, (b) clause/rule extraction, (i) notice drafting,
plus evidence capture (Clearstory Basic, Autodesk Data Connector CSV).
**EMPTY stages:** (g) causation/attribution, (h) quantum, and tribunal-standard (f) evidence sufficiency.
**THE REAL VOID IS THE SEAM (c) -> (d) -> (h). Nobody spans it.**

**Why quantum is empty — three of five candidate explanations are FALSE:**
- *Too hard?* **NO.** Easyclaim ships court-grade quantum as one offline HTML file, no AI, one person, since 2017.
  Eichleay is trivial arithmetic gated by two *evidentiary* prerequisites; measured mile is "a concept, not a
  procedure" gated by missing baseline data. **Both barriers are EVIDENCE problems — stages (e)/(f).**
- *Unvalued?* **NO.** EUR 599/case paid since 2017; consultants $240k-660k/matter; **Caltrans mandates an
  itemised costed estimate + TIA by day 20 or waiver**; 66% of GCs say **disputed pricing** is the #1 reason
  they short-pay (vs 53% missing backup).
- *Too legally exposed?* **Explains platforms ONLY** — ClaimMaster's founder (RICS expert witness) refuses
  quantum voluntarily.
- **PRIMARY CAUSE = JURISDICTION-SPECIFICITY.** Quantum products exist **iff the law supplies a computable cost
  method.** Germany does (§642/§650c BGB, §2(3) VOB/B, Opitz) *and* supplies the priced BoQ via GAEB.
  **The US public-works subset ALSO does: Eichleay is case-law-fixed, FAR gives a 20-day rolling cost
  truncation, and Caltrans §5-1.43C/D is literally a written spec for a quantum engine.**
- SECONDARY = supply-side misalignment: those who can do it sell hours; those with data sell to both sides;
  those building AI price at $29-300/mo and cannot fund the depth.

**Hard constraints on any quantum product:**
- SCL Core Principle 12: EOT != money. Naive days x rate is wrong by construction.
- Quantum sits downstream of standards-blocked causation => **it CANNOT ship standalone. Bundle (e)+(f)+(h).**

## Neutrality is the constraint — not buyer identity (CM-B correction to my earlier read)
Procore, Trimble, Autodesk, Oracle, Clearstory, Gather and the NEC six **all stop at the identical line**.
Six vendors, five countries => a structural constraint, not coincidence.
**Neutrality CAPS PRICE**: Gather charges GBP 500/mo flat despite publishing 39x ROI.
=> **Only a partisan product can price on recovery.** This is the defensibility argument, sharpened.

## Demoware confirmed
**Magra's headline moved $240K -> $17,824 per event (13.5x reduction)**, methodology now "estimates... from
ASCE research"; all 8 integrations still "Upcoming" (verified). Treat as vapour.
**Verified paying entitlement customers exist ONLY for:** Easyclaim (quantum artefact), Gather (detection;
outcomes = defence), Document Crunch (notice *drafting* only), Clearstory (workflow), NEC six (administration).

## CM-B highest-conviction claim (candidate wedge #1)
**Build "the priced, evidenced position" — the number PLUS the records proving each legal prerequisite, with
time separated from money — priced per claim (EUR 599 proves the shape), sold into US state DOT.
Nobody has connected Eichleay + FAR's 20-day truncation + Caltrans' mandated itemised estimate and TIA.**

## *** CM-A: THE STRUCTURAL-REFUSAL THESIS IS HALF TRUE — STRONG FORM IS A RATIONALISATION ***
I over-claimed this earlier. CM-A falsified the strong form with six cases, two in-industry and nine-figure:
- **Procore paid ~$500M for Levelset** — the mechanics lien is the most adversarial instrument in US
  construction, filed by one Procore customer against another's property — and still sells it in 2026.
- **Autodesk paid $387M for Payapps**; in *Roberts Co v Sharvain Facades* [2025] NSWCA 161 a **$3.2M judgment**
  turned on the timestamp Payapps recorded, stripping one customer of the right to dispute another's claim.
- Amazon Project Zero; Airbnb Resolution Center/AirCover (14-day bar, evidence standards tightened Apr 2026 —
  **structurally our exact product**); Verisk Xactimate (sells the price book to carriers AND the contractors
  fighting them); Lex Machina.
Two-sidedness also is not *sufficient*: the single-sided cohort (Magra, Lexilio, Aven-AI) all score **0** on
quantum, and the one product doing quantum properly is an offline HTML file.

**RESTATED AND DURABLE FORM:**
> *Two-sided platforms ship adversarial machinery when an EXTERNAL AUTHORITY — statute, court, clerk — makes
> the judgement. They will not ORIGINATE the judgement.*
Liens have a statute; SOPA has s14(4); **construction entitlement has no adjudicator**, so the number must be
originated, and origination carries E&O / UPL / discovery exposure.
Datagrid (Procore) says it out loud: *"entitlement and approval stay with the responsible project professionals."*

**WARNING THIS GENERATES (important, cuts against the beachhead):** Caltrans is *externally adjudicated*
(5-day fuse, costed estimate + TIA by day 20, statutory waiver). That makes it the best beachhead **AND the
most copyable one** — precisely the condition under which incumbents DO ship adversarial machinery.
Red team must attack this directly.

## No incumbent scores 3 on 12 of 26 dimensions — but only SIX survive the paid-for-pain rule
**Survive:** 14 evidence_completeness, 15 recoverable_dollar_estimation, 16 claim_package_generation,
26 consultant_replacement_potential, 25 performance_pricing (as pricing architecture), 10 claim_identification
*on a clock*.
**Killed by the rule:** 3 notice_detection + 17 notice_drafting (commoditised — DC ships drafting at 3, Trunk
Tools gives extraction away free); 11 delay_detection + 18 schedule_impact (served at $2.7k-$25k by
Acumen/SmartPM/Steelray); 12 responsibility_attribution (standards-blocked); 24 portfolio_risk (real gap,
**zero pain evidence**).

## Score corrections applied by CM-A (SCORES.csv to be regenerated)
- Procore & InEight `recoverable_dollar_estimation` 2 -> **1** (both price a change order, not a claim;
  differentiation vs Autodesk/Trimble was spurious).
  **=> RESULT: NOBODY EXCEEDS 1 ON DIMENSIONS 14, 15, 16.**
- Autodesk `claim_identification` 0 -> **1** (RFI AI auto-populates Cost Impact/Schedule Impact from free text).
- Autodesk + Procore `portfolio_risk` 3s are **inflated** — their own justifications say the risk domains are
  quality/safety/design, never commercial.
- Trimble `notice_detection` 2 held but **relabelled: that 2 is obligation extraction. On event-triggered
  detection all five score 0.**

## *** THE CHEAPEST LEADING INDICATOR IN THE PROGRAM ***
**All five incumbents build up to the number and stop AT the number** — identical stop across five companies
with different owners, ICPs, geographies and business models => not a roadmap accident.
All five ship notice containers or drafts; **not one has a field for clause reference, notice date, notice
deadline or entitlement basis on its change object.** That schema change is ~one quarter of work with no
liability tail.
**WATCH: Procore Groundbreak, 21-22 Oct 2026, Orlando.** (Cadence: acquisition -> 20 GA agents in ~6 months.)
Detection is already gone (23 Jul 2026). Notice triggering has ~6-12 months.
**Evidence sufficiency and quantum are structurally protected.**

## INGESTION STRATEGY THAT SURVIVES ALL FIVE PLATFORMS
No API path survives all five. **File-based, under the customer's own data rights:**
1. Uploads — contract PDFs, **XER/MPP snapshots**, CSV/PDF registers, InEight ZIP archives.
2. **A dedicated forwarding address** — email is the richest corpus and the least contested (Autodesk captures
   Correspondence and has NO API/Data Connector export; ProjectSight has none; Trunk Tools has no email connector).
3. Route any pulls through **customer-owned credentials** (Procore Analytics licensed to the company; Autodesk
   Data Connector on customer admin; Aconex integrations registered by the customer).
4. **Never train or benchmark cross-customer.**
Verified 19 Aug 2026: only Manufacturing Data Model APIs became rated (17 Aug 2026); **ACC/Forma APIs and Data
Connector remain free.**
**Hostility rank: Procore >> Oracle > Trimble > InEight > Autodesk.**

## *** DIY STACK — THE HARDEST CONSTRAINTS IN THE PROGRAM ***

**BUDGET CEILING (hard number, CFMA n=1,558):**
- **"Technology Costs" = 0.26% of revenue** (0.40% specialty trade) = **$368K on $139.4M average revenue**,
  inside SG&A of 11.33%.
- Commercial GCs ran **4.4% net income before taxes** FY2024 (4.2% at $100-300M, 3.4% above $300M);
  6.7% all contractors, 8.3% heavy civil, 7.7% specialty trade.
=> A $200M GC has ~$500K of TOTAL technology budget. **$500-$5,000/mo is feasible but must displace something
   or be funded from recovery, not from the IT line.** Heavy civil and specialty trade have ~2x the margin of
   commercial GCs => **better first customers than commercial GCs.**

**EVIDENCE-COMPLETENESS SCORES 0 IN THE DIY STACK — the only culturally undefended gap.**
> *"nothing on earth checks whether a claim's proof is complete before a human submits it"*
Change-order *workflow* is well covered (Excel COR logs, Procore, DocuSign, 30-step processes) — **that is not
the gap.** Notice tracking (1), evidence linkage (1) and portfolio roll-up (1) are gaps but **culturally
defended**; evidence-completeness is the one gap the industry admits to.
=> Converges exactly with CM-A (nobody exceeds 1 on dims 14/15/16) and CM-B (the void is the (c)->(d)->(h) seam).

**CULTURAL REJECTION RISK IS REAL AND DOCUMENTED:**
Contractors **deliberately suppress notice to protect owner relationships** — confirmed in print by
construction lawyers (Smith Currie, Jun 2025). This is not inertia; it is a strategy.
=> Any product that *automatically contacts the owner* will be rejected. **V1 must never contact the owner.**

**FIFTH INDEPENDENT FALSIFICATION OF INBOUND GTM — and it is savage.**
Four separate 2025-26 r/ConstructionManagers threads probing exactly this product idea drew hostility
outscoring the post: *"What are you selling? Another shitty GPT wrapper... Go away. Reported."*,
*"Your entire goal is to extract value out of these people to create some software. Fuck you."*, and the killer:
*"This is like GC 101 and no one needs more software for anything. CONTRACTING is in the name."*
**BUT: not one project executive or CFO appeared in any thread.** The mockers are PMs and supers —
**not the budget holder.** => Reddit is unusable as a channel; and the objection is from the wrong persona.

**Dedicated headcount already exists and is priced (the displacement target):**
Tutor Perini **Change Order Engineer $85-120K**; AECOM **Claims Manager $140-182K**; Microsoft Contract Lead
$116.9-203.6K; **1,000+ open US Contract Administrator roles.**

**Procore's growth tell:** total customers grew **4% in 2024 and 4% in 2025** (16,367 -> 17,088 -> 17,850)
while revenue grew 21%/15% — **all growth from existing accounts**; stops disclosing customer count in 2026.
=> The market is not adding new software buyers. Land-and-expand inside existing accounts, or sell to
   non-Procore contractors.

## EVIDENCE CAVEATS TO CARRY INTO ROI (do not overstate)
- **No credible published dollar figure for change-order write-offs could be established.** Levelset/Rabbet
  reports 404; Arcadis latest reachable edition 2022; HKA CRUX blocked to this agent.
  **DO NOT model ROI on a write-off percentage.** Use Clearstory's Dodge-sourced 77% *incidence* (not value)
  and the consultant-hours figures instead.
- Reddit was IP-blocked; evidence came via Arctic-Shift archive with live permalinks, quotes labelled
  [PRACTITIONER] vs [VENDOR/SUSPECT] because the subreddit is heavily astroturfed by AI-written vendor accounts.
- JBKnowledge ConTech Report: **2017 is the last edition** (JBKnowledge has exited construction tech).
  71% of estimating and 46% of PM workflows on spreadsheets; 48.7% moved data manually; 30% said nothing
  integrates. **Dated — label accordingly.**

## *** CM-C: ECONOMICS RESOLVED ***

**Evidence rule honoured — the write-off VALUE number does not exist.** Re-attempted HKA CRUX 8th (headlines
independently confirmed: $95.0bn / 33.4% budgets / 65.8% schedules), Arcadis 2026, Dodge SmartMarket, CFMA,
Rabbet (full PDF extracted), Levelset, Billd, Siteline, FMI. Rabbet's $280bn is a **modelled 14% of construction
cost from a 93%-GC sample — not a write-off.** Levelset's 4% AR write-off is all-industry, vendor-sourced, 2017.
**ONE new value-side number found, previously unused by anyone:**
> **"98% of GCs have experienced fee erosion from CO negotiations; nearly half say erosion exceeded 10% of their
> fee on at least some projects"** (Dodge/Clearstory 2026 GC report).
**That is the only value-side number in the category. Everything else is incidence.**

**FREQUENCY RANKING (freq / value / confidence)**
1. **Unapproved-unbilled change orders** — 97% start before approval; 77% written off; 91% of GCs short-pay —
   HIGH freq / LOW-MED value
2. **Disputed pricing on submitted COs** — 66% of GCs (vs 53% bad backup); >half of CORs need 2+ revisions —
   HIGH freq / NO value data
3. **Scope creep absorbed** — CRUX #1 cause, 38.8% cumulative — MED / none
4. Retainage & slow pay — **wrong problem, already served**
5. Missed lien deadline — **solved and owned (Levelset)**
6. **Missed contractual notice — NOT MEASURED ANYWHERE.** Proxy: CRUX contract-admin failure 19.5%->
   <9%. LOW freq / HIGH consequence / **only state DOT has a real fuse**
7. Delay/EOT — actually OVER-claimed where it matters (65.8% of schedule); SCL P12: EOT != money — LOW
8. Disruption/productivity — unmeasured; measured mile "never textbook-usable" — LOW freq / **highest
   evidence-gated value**
9-10. Backcharges, escalation — **zero data. Do not build on them.**

**ROI MODELS (every input sourced or labelled; full derivations in CM-C file)**
| Case | Leak | Capture | $/yr | Price/yr | Payback | ROI |
|---|---|---|---|---|---|---|
| (a) $50M specialty sub (7.7% net) | ~$188K (0.38% rev) | 15-25% | $28-47K | $6-12K | **2-5 mo** | 3-6x |
| (b) $200M commercial GC (4.2% net) | ~$200K fee erosion | 20-30% | $40-60K | $24-36K | **7-11 mo** | 1.4-2.5x |
| (c) $100M heavy civil/Caltrans (8.7% net) | ~$600K waived | 20-40% | $120-240K | $36-60K | **2-6 mo** | 3-5x |
| (d) consultancy | 200-600 hrs @ $400 | 40-60% | $32-160K/matter | $5-25K/matter | 1 matter | 3-6x |
**Key downside: Gather — the only working analogue — has 11 case studies and NOT ONE documented recovered CE in
GBP. The recovery pitch is unevidenced by anyone, anywhere.**

**PRICING BAND: PARTIAL YES.** $500/mo YES everywhere (1-3% of tech purse). $1,500 YES at $100M+.
$3,000 NO at $50M / YES at $100M+ with CFO case. **$5,000 NO below ~$150M** (= 30% of a $50M sub's ENTIRE tech purse).

## *** THE BUDGET-LINE UNLOCK — escapes the 0.26% technology cage entirely ***
1. **Job cost / project overhead.** On federal & federally-aided work, ***Tip Top Construction v. Donahoe*,
   695 F.3d 1276 (Fed. Cir. 2012)** makes **REA-preparation costs ALLOWABLE contract administration**
   (FAR 31.205-33). Only POST-CDA-claim costs fall under FAR 31.205-47(f)(1).
   => **A PRE-CLAIM product is a billable project cost, not an IT purchase.**
2. **Professional Fees = 0.50% of revenue vs Technology 0.26% — a purse 1.9x larger**, where consultants and
   counsel are already paid.
**Signer:** project exec at $500-1,500/mo; CFO above. **Displaces HEADCOUNT** (Change Order Engineer
$85-120K = 7-20x the subscription), not software.
**Sequence: heavy civil FIRST** — not for margin, but because Caltrans supplies a statutory waiver fuse AND
writes the product spec (costed estimate + TIA by day 20). Specialty trade second. **Commercial GC last**
(structurally conflicted, thinnest margin).
**CAUTION: Caltrans already runs ePCR with email reminders => alerting is FREE. The ARTEFACT is the wedge.**

## *** US PERFORMANCE PRICING: LEGAL INSIDE A NARROW ENVELOPE (closes agent 11's UNVERIFIED) ***
- **Testifying-expert contingency is BARRED** — ABA Model Rule 3.4(b) cmt.; Ala. Formal Op. 1997-02;
  Phila. 94-27; Cal. 1997-149.
- **BUT *Factortame No.8* held Grant Thornton's QUANTUM-PREPARATION contingency was NOT champertous.**
  **The bar is the WITNESS ROLE, not the fee.**
- Champerty dead in ~30 states. **Live hazard: KRS 372.060** (Kentucky) voids contracts for services "in the
  prosecution or defense... whereby the thing sued for... is to be taken, paid or received for such services."
- NY Jud. Law §489 targets *assignment*, not fees (*Justinian Capital*, 28 N.Y.3d 160).
- **Real risk is UPL** (*NC State Bar v. Lienguard* — preparing lien claims = UPL; **citation needs verification**).
- Also: Georgia SB 69 registration from 1 Jan 2026; Anti-Assignment Act §3727; public-adjuster felony exposure
  if insurance recoveries are touched.
**RECOMMENDATION: do NOT lead with contingency. Subscription + capped 3-8% success component earned on an
EXECUTED CHANGE ORDER — never on suit proceeds.**

## *** VALUE-CAPTURE CEILING (kills any 20-40% fantasy) ***
Take scales with downside borne: funders 20-40% (full capital risk); recovery auditors 20-30% (full delivery
cost); public adjusters 8-20% capped; **consultants 1.2-3.6% of disputed sum.** A software vendor bears neither.
**On a $412K recovery: $5,000-$30,000 = 1.5-8%.** Confirmed from two independent directions.

## THE ONE NUMBER TO VERIFY BEFORE COMMITTING (ask 30 controllers)
> *"In your last fiscal year, what dollar value of work did you perform and either never bill, or bill and not
> collect, because the change order was never executed or was negotiated down?"*
Every ROI above rests on a modelled leak of **0.1-0.6% of revenue that no published source establishes.**
**Free alternative: a California Public Records Act request for Caltrans ePCR filing counts** — PCRs filed vs
supplemented-with-costed-estimate-and-TIA vs waived. Would produce a defensible frequency number nobody has.

## *** CM-D: BUYER RESOLVED — CONTRACTOR-SIDE IS THE MARKET, OWNER-SIDE IS DISTRIBUTION ***

**Ranked buyers** (pain 30% / budget 25% / reach 25% / speed 20%):
1. **Claims consultancy (10-50 ppl + DOT on-call primes) — 4.75 — FIRST REVENUE**
2. **Heavy civil / state-DOT contractor — 4.30 — contractor beachhead**
3. **Sub CFO/controller ($25-150M) — 4.25 — budget holder, cheapest channel**
4. Sub owner/president <$50M — 4.05 — max pain but UNREACHABLE (**eSUB is the warning**)
10. Contract administrator — 3.10 — **CHAMPION, NEVER BUYER**
12. Surety/insurer — 2.35 — V3 only (only 7 SDI carriers exist)
> **Do not sell to the highest-pain buyer. Sell to whoever can sign and can be found.**

**Owner-side evidence is real but does not win:**
- **Caltrans D3 alone is procuring $7.0M/3yr for claims-and-scheduling support (03CONTCLM27)** — the
  best-evidenced budget in the entire program.
- Owner mandate language is standard boilerplate ("The Contractor shall use the Owner's Project Management
  software, e-Builder...").
**Resolves contractor-side on four grounds:** (a) the Gather result is about **neutrality, not which side has
money** — they chose "We don't take sides" first and never ran the contractor-side experiment; (b) neutrality
**caps price** (GBP 500/mo flat vs published 39x ROI); (c) owner-side assurance is exactly what incumbents CAN
ship without breaking neutrality => **most copyable thing available**; (d) all pain data is contractor-side.
**One engine serves both** — the evidence-completeness score is a claim-strength score to the claimant and a
rejection basis to the payer (**and scores 0 across every incumbent AND the DIY stack**).
**BUT THE ORDER IS ONE-WAY: take owner money first and you can never sell contractors. Reverse works
(Xactimate precedent).** Owner mandate = year 2-3 unlock; unusable now (requires a procurement).

**FIRST-20 PLAN (sequenced, named)**
- **Phase 0 (wks 0-6):** build the **record-quality-vs-outcome dataset on 30-50 anonymised closed matters** —
  the only such number in the industry, currently unoccupied. Upload-only V1. **No attribution verdict, no
  owner contact.**
- **Phase 1 (wks 4-16) -> customers 1-6:** Trauner (~36 staff), Imperium (~23), Long International, VERTEX,
  CCI, RLB + holders of Caltrans/FDOT/VDOT on-call claims contracts.
  **Construction SuperConference, 1-3 Dec 2026, Huntington Beach** — attend, 40 pre-booked meetings.
- **Phase 2 (wks 10-30) -> 7-14:** California heavy civil via **UCON (800+ firms)**, IRTBA (300+), GHCA (~250).
  **AGC/CFMA CFMC 28-30 Oct 2026, Las Vegas** for the CFO. Free "PCR Readiness Check" distributed **by
  association, not search.**
- **Phase 3 (wks 20-44) -> 15-20:** specialty trade, after implementing **MCAA labor productivity factors** and
  ELECTRI/Hanna overtime studies **with the association document cited on the output** — converts the AACE
  "black box" objection into an audited method.
  **MCAA 7-11 Mar 2027 San Diego; NECA 4-7 Oct 2026; CFMA Annual 22-26 May 2027 Nashville.** CFMA associate
  access ~$600/yr.
- **NOT doing:** Reddit, SEO, Procore marketplace, ads, direct DOT procurement, anything needing a Procore key.

**3 SURVIVING POSITIONS**
1. *Consultant:* "You bill 200-600 hours of chronology per matter and write most of it off against the fixed
   fee. Send the dump; get the chronology and missing-evidence schedule back same-day — and bid the sub-$5m
   matters you turn away."
2. *Heavy civil:* "Caltrans gives you 5 business days for the Initial PCR and 15 more for a Supplemental with an
   itemised cost estimate and a TIA. Miss it and §5-1.43A waives the claim and bars arbitration. We produce both
   from the daily reports you already file." (**"GC 101" is answered by their own spec book.**)
3. *CFO:* "Your unapproved change orders are unbilled WIP. Tell me what you wrote off last year — I'll show you
   which had the evidence to bill, from your own closed files, before you buy anything."
**FAIL:** "Never miss a notice deadline" (Aconex solved it; Levelset proved the *filing* was the revenue);
"AI-powered documentation... capture everything" (**eSUB verbatim**); "AI detects entitlement" (Procore shipped
detection 23 Jul 2026; AACE §1.2(f) blocks attribution).

**PRICING ARCHITECTURE**
- **SKU 1 Matter Pack** — $7,500/matter <=25k docs; $15,000 to 100k; $0.10/doc after; **10-matter pre-buy
  $60,000**. Anchor: 200-600 hrs x ~$400 = $80-240k of the same work => **you are 3-9% of it, rebillable, no
  procurement.** Targets the consultancy.
- **SKU 2 Project Licence** — **$1,200/project/month, unlimited users**, 6-mo min; 5 projects $4,500/mo;
  15 $11,000/mo; **company cap $72,000/yr**; setup $2,500 waived. CEMAR's GBP 435/licence/mo proves the band;
  **job-costable => escapes the 0.26% cage** (0.07% of a $20M job).
- **SKU 3 Recovery Fee** — 8% of recovered amounts, $50k/event cap, credited against SKU 2. **Deferred to
  ~customer #10** (attribution needs a baseline).
- **FORBIDDEN:** any $29-300/mo tier (**the demoware graveyard**), any per-seat line, free version of the same
  artefact.
**Model at customer #20: ~$710k ARR, blended ACV ~$35.5k, zero enterprise procurements.**

## SYNTHESIS: 8 WEDGES RANKED (/90)
1. **MATTER ZERO (72)** — same-day linked chronology + notice/entitlement register + missing-evidence schedule
   from a raw document dump; per-matter to 10-50 person claims consultancies and DOT on-call primes. **FUNDED PICK.**
2. **DAY 20 (70)** — Caltrans Supplemental PCR engine: itemised costed estimate + TIA inside the 20-day
   statutory window, from daily reports + XER snapshots already mandated.
3. **WRITE-OFF AUTOPSY (68)** — pure productised service, no software: send last year's closed jobs + write-off
   ledger, get back which write-offs had the evidence to bill.
4. **THE DEFENSIBLE PRICE (65)** — loss-of-productivity quantum using MCAA/ELECTRI published factors cited on
   the face of the output; attacks **disputed pricing**, the LARGER cause of short-payment.
5. **BACKUP PACK (49)** — deliberately boring, no AI in pitch: every COR ships with indexed substantiation.
6. **DEFICIENCY SCHEDULE (47)** — owner/defence side: score contractor applications against the contract's own
   substantiation requirements.
7. **NOTICE SENTINEL (35)** — the obvious idea. **Falsified eight independent ways.**
8. **PORTFOLIO RISK RADAR (34)** — labelled WEAK, control case: verified uncontested gap at all five incumbents,
   **zero paid-for-pain evidence.**

**Funded rationale:** Matter Zero is the only wedge where the pain is an **already-invoiced line item**
(200-600 hrs/matter at $396-442/hr realised, at firms on a sourced 3.3% operating margin) rather than a modelled
leak. Buyer is a partner who signs same-week and **rebills as a disbursement** — never touches IT budget or
procurement. Ingestion constraint is **native, not a compromise**: the file dump from counsel IS how this
buyer's data arrives.
**One thing flips this to Day 20:** a California PRA request on Caltrans ePCR filing counts (free, ~2 weeks).
If >=3 waived-or-unsupplemented PCRs per active contract per year, Day 20's economics become sourced.

## TOP 5 "WHAT MUST BE TRUE" (the load-bearing assumptions of the entire program)
1. A contractor will pay a premium for recovered entitlement, **sustained four quarters**. Never evidenced by
   anyone — including Gather (11 case studies, zero recovered CEs in GBP).
2. The modelled leak of **0.1-0.6% of revenue** exists. No credible published dollar figure exists.
3. **The money is lost to missing evidence, not to price.** 66% of GCs cite disputed pricing vs 53% insufficient
   backup — **if price dominates, the evidence thesis optimises the smaller half.**
4. Evidence-completeness scoring **discriminates against real outcomes**. No such benchmark exists anywhere.
5. Documented practitioner hostility **does not generalise to the budget holder** (no CFO/PX in any thread).

## *** RED TEAM: 5 OF 8 KILLED, RANKING INVERTED ***

| # | Wedge | Kill argument | Verdict |
|---|---|---|---|
| 1 | Matter Zero | **Relativity aiR for Case Strategy (GA 12 Jan 2026)** builds fact chronologies with citations **and evidence-gap analysis**, **included in RelativityOne at no extra cost** — the claimed 24-36mo moat shipped 7 months ago, free | **WOUNDED** |
| 2 | Day 20 | Frequency still unverifiable; **no located case enforcing §5-1.43A waiver**; subscription-generated gap schedule is ordinary-course + discoverable | **WOUNDED — STRONGEST SURVIVOR** |
| 3 | Write-Off Autopsy | Artefact is a CFO-commissioned portfolio-wide catalogue of the buyer's own record failures — a business audit, **NOT work product** — usable against every future claim | **KILLED as paid work** |
| 4 | Defensible Price | MCAA factors are "based on contractor opinions not empirical studies"; boards prefer measured mile; **Ankura publishes the attack**. "Argue with MCAA" **arms the payer** | **KILLED** |
| 5 | Backup Pack | **Clearstory COR Pricing Agent** in closed beta 28 May 2026 (drafts COR, prices, backup), GA later 2026, on $2.1B/mo of evidence | **KILLED** |
| 6 | Deficiency Schedule | Copyable, neutrality-price-capped, procurement-gated, one-way door; $7M Caltrans budget buys **consulting hours a solo founder cannot prime** | **KILLED** |
| 7 | Notice Sentinel | Resurrection attempted and FAILED — Copilot **Researcher** (GA Jun 2025) answers it at $30/user/mo | **KILLED (corpus passed)** |
| 8 | Portfolio Radar | Searched for paid-for-pain, found none; adjacent budget already spent on **Briq** | **KILLED (corpus passed)** |

### THREE FINDINGS THAT CHANGE THE RANKING
1. **THE $400/HR RATE IS WRONG.** raw/11 itself derives Diales (only listed pure-play) at **GBP 165-200/hr**.
   The displaced block is worth **$24-108K, not $80-240K**. **$7,500/matter is 15-70% of value created, not 3-9%.**
2. **"Bid the sub-$5m matters you turn away" is ARITHMETICALLY FALSE.** On the corpus's own table the tool
   removes **13-22% of matter hours**. A matter uneconomic at $240K is still uneconomic at $190K.
   **This was the SOLE rebuttal to channel cannibalisation.**
3. **DISCOVERY RISK LANDS OPPOSITE TO EXPECTATION.** Per-matter, counsel-engaged work fits *William A. Gross*
   (Hill Int'l) — **HELD PROTECTED**. Subscription / contractually-required output fits *Alta Refrigeration* and
   *G.M. Harston* — **HELD NOT PROTECTED**. It wounds wedges 2/3/5, **not** wedge 1.
   Plus FRCP 26(a)(2)(B)(ii): "considered" = anything the expert received or read.

**FAILED KILL that STRENGTHENS Day 20:** PCC §9204 **expressly exempts Transportation** => the PCR regime is
not statutorily displaced.

### SURVIVORS + REQUIRED RESHAPING
- **DAY 20 (promoted to first):** sell costed estimate + TIA + evidence index; ship gap analysis **ephemeral and
  purgeable**; per-project job-costed; **buy a PSP/CCP/PE to sign every TIA**; California only;
  **do not build until the CPRA returns.**
- **MATTER ZERO (demoted):** stop selling chronology — sell the **entitlement layer ON TOP OF** aiR/Everlaw at
  **$2,500-4,000/matter**; delete the sub-$5m claim; solve privilege/OCG before pitching.
- **WRITE-OFF AUTOPSY:** free, anonymised, counsel-mediated, **verbal readout only**. You can be paid or safe,
  not both.

### MOST LIKELY REASON THE WHOLE THESIS FAILS (unhedged)
> **Assembled evidence monetises as SAVINGS for payers and HOURS for professionals — never as RECOVERY for
> claimants. Gather proved it over eight years under ideal conditions and shrank while doing it.**

### THREE CHEAPEST EXPERIMENTS
1. **CPRA request to Caltrans on ePCR** — $0-50, 3-6 weeks. Kills or funds the top wedge; produces a number
   nobody in the industry has.
2. **Rate-and-hours audit, 5 partners, no product** — $0 + ~$2,000 conference pass, 4 weeks. Settles price,
   pain and cannibalisation at once.
3. **Counsel-veto test on a mock missing-evidence schedule** — $0, 2 weeks. **Currently unrun.** Determines
   whether the artefact can persist at all.

**RED TEAM LEAN: PIVOT.** KILL if the CPRA returns <1 waived PCR per contract/year AND counsel vetoes the
persisted schedule — both testable for **under $2,500 in six weeks**.
