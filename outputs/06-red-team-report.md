# 6. Red-Team Report

Every wedge attacked along the eight vectors the brief specifies. The standard is not "could this fail" — everything can. It is: **is there a specific, evidenced mechanism that kills it?**

Verdicts: **KILLED** · **WOUNDED** (survives only with a named change) · **HOLDS**.

---

## W1 — Real-time entitlement capture

| Vector | Attack | Verdict |
|---|---|---|
| **Incumbent** | Trimble scores **37/50** — the highest software score in the study. It owns ELD + geofence + TMS + rating, and has shipped auto-detention since 2004 with per-customer contracted tolerances. For a carrier on TMW.Suite with the modules licensed, you are selling a feature they own. | **WOUNDED.** Counter: Trimble has **no concept of a notice window**, scores **0 on `claim_submission`**, 1 on `evidence_package` and `collection_tracking`, and its Nov 2025 six-agent AI release contains **no detention, accessorial, settlement or claims agent.** Sell alongside, never against. |
| **Substitute stack** | A billing clerk at $61K loaded cost already does this. | **HOLDS.** The clerk cannot be at the dock at minute 89 of free time. This is precisely the job a human cannot do. |
| **Internal build** | A 150-truck carrier's IT person wires a Motive `geofence_events` webhook to a Slack alert in a weekend. | **WOUNDED, seriously.** The naive version genuinely is a weekend. What is not a weekend: per-broker rule extraction, versioning when Arrive amends rates *"at any time, effective on notice"*, drop-and-hook disambiguation, and evidence packaging. **But you must prove that gap in the demo, because the buyer will price you against the weekend version.** |
| **Consultants** | None operate here. | **HOLDS.** |
| **Pricing** | ROI Model A: a 25-truck carrier yields **~$9,800 ACV at 25% of recovery** — below the cost of one AE touch. Only **61,777 carriers have 11+ trucks.** | **WOUNDED.** The sub-50-truck tier is unsellable by direct sales. Requires self-serve or embedded distribution. |
| **Switching cost** | Low — sits alongside the TMS. | **HOLDS.** |
| **Legal** | **The severe one.** Samsara Integration Partner Terms §3.1 bars transferring Customer Data to any third party *"without explicit consent and written notice to Samsara"* — **and sending a detention claim to a broker is exactly that transfer.** Motive's ToS prohibits use *"which Motive deems outside of the scope"* — unilateral and open-ended. | **WOUNDED.** Mitigation: integrate three-plus ELD sources including an ELD-agnostic one, get counsel before the first design partner, and structure so the *carrier* transmits, not you. |
| **Distribution** | Requires driver behaviour change in the moment — the failure mode of every prior attempt. | **WOUNDED.** The notice must fire automatically without the driver acting, or it inherits the failure it is meant to fix. |

**Verdict: WOUNDED — survives only as (a) automatic, no-driver-action notice, (b) sold at 50+ trucks or embedded, (c) with multi-ELD legal cover.**

---

## W2 — FMC D&D invoice-defect engine

| Vector | Attack | Verdict |
|---|---|---|
| **Incumbent** | Terminal49, Vizion, PortPro, Container xChange. | **HOLDS.** Terminal49's own D&D page makes **no** dispute or recovery claim. Container xChange **is not a D&D product at all** — it is a container trading marketplace. The dispute + submission + collection + analytics quadrant is **empty**. |
| **Substitute stack** | OceanAudit does exactly this on contingency. | **HOLDS, narrowly.** OceanAudit is one expert reading invoices manually. That is the thinnest substitute in the study. |
| **Internal build** | An NVOCC's ops lead builds a 20-field checklist in a spreadsheet. | **WOUNDED.** The checklist genuinely is buildable. What is not: doing it on every invoice inside the 30-day window at volume, and maintaining it as templates change. Thin moat. |
| **Consultants** | Ocean freight consultancies would add this to a service line quickly. | **WOUNDED.** Low barrier to a services competitor. |
| **Pricing** | Pool is ~1.7M invoices/yr × ~$1,500 ≈ **$2.5–3B billed**; at 12–22% waivable and a 20% contingency on a third of it, the fee pool is **~$25–50M/yr.** Real, but small. | **WOUNDED.** This is a $25–50M category, not a venture-scale one on its own. |
| **Switching cost** | None — customer emails a PDF. | **HOLDS.** Best in the study. |
| **Legal** | **The strongest position anywhere in this research.** §541.5 voids the obligation; §541.7 voids late invoices; §41310(b)(2) puts the burden on the carrier; escalation is free or $176. | **HOLDS.** |
| **Distribution** | Named, reachable segment (mid-market NVOCC/forwarder), and the pitch is a federal citation. | **HOLDS.** |
| **THE KILL SHOT** | **Concentration.** 354 regulated billers, 9 carriers dominating. Carriers have had two years since 2024-05-28 to fix templates. **One Maersk template revision erases most of the defect population overnight.** Defect density on 2026 invoices is **UNKNOWN**. And the strongest defence — §541.4, "you billed the wrong party" — **was vacated by the D.C. Circuit in Sept 2025 and removed from the CFR in Dec 2025.** | **CONDITIONALLY KILLED.** |

**Verdict: CONDITIONALLY KILLED — revived only if a measured defect rate on 200–500 real 2026 invoices exceeds ~15%. Below ~5%, the compliance window has closed and the residual is consulting, not software. This is a one-experiment wedge.**

---

## W3 — Broker AR margin recovery

| Vector | Attack | Verdict |
|---|---|---|
| **Incumbent** | McLeod PowerBroker scores **36/50**, Turvo 28, Tai has an audit engine. | **HOLDS.** All three point at **AP**. Tai's own copy: *"compares LTL invoices against rate confirmations… **before payment**."* `accessorial_detection` in the AR direction is **0** across every broker vendor scored. |
| **Substitute stack** | Excel plus an AR clerk (19/50) and a monthly margin review. | **HOLDS.** Monthly is too late for the customer's dispute window; the failure is silent by construction. |
| **Internal build** | A broker's BI analyst joins the AP and AR tables in the TMS and writes the report themselves. | **WOUNDED, badly. This is the most credible internal build in the study** — it is a SQL join on data they already own. The defence is rule extraction (was it *billable* under that customer's contract?) and running it weekly with evidence attached — but **you must assume a sophisticated broker builds v1 internally.** |
| **Consultants** | Contingency freight-audit shops (25–50% of savings) could pivot to the AR side. | **WOUNDED.** Low barrier. |
| **Pricing** | ROI Model C: $80M broker → **$194,535 incremental recovery, ~$49K price.** Healthy. | **HOLDS.** |
| **Switching cost** | CSV export. None. | **HOLDS.** |
| **Legal** | Rebilling your own customer under your own MSA. **No collection-agency exposure, no third-party liability assertion, no factoring assignment problem.** | **HOLDS. Cleanest legal position of any wedge.** |
| **Distribution** | CFO of a $50–500M brokerage; 28,351 registered brokers. Reachable. | **HOLDS.** |
| **THE KILL SHOT** | **There is no published magnitude for broker paid-but-not-billed leakage. None. Every figure in this space traces to vendor marketing, and the widely-cited "3–15% of revenue" numbers describe *warehouse* value-added billing.** Worse: **Truckstop actively teaches brokers to absorb accessorials** — *"Not every accessorial charge should automatically land on the shipper's invoice… Does the relationship support friction?"* **If absorption is a deliberate commercial policy rather than an error, the entire product is noise.** | **WOUNDED — potentially fatally.** |

**Verdict: WOUNDED — highest-scoring wedge, but gated on one measurement. Run a retro on 2–3 real brokers' TMS exports before writing a line of production code. If leakage is 0.05% of revenue rather than 0.5%, only the $500M+ tier works: ~200 companies.**

---

## W6 — Short-pay / deduction ledger

| Vector | Attack | Verdict |
|---|---|---|
| **Incumbent** | McLeod 26.1 shipped an interactive AR Collections screen. | **HOLDS.** Still no short-pay reason codes, no deduction matching, no win/loss by accessorial type. Everyone scores 0–1. |
| **Substitute** | A clerk's memory and a notes field. | **HOLDS.** |
| **Internal build** | Requires disciplined outcome capture on every claim — culturally hard, not technically hard. | **HOLDS.** |
| **Consultants** | None. | **HOLDS.** |
| **Pricing** | **It is analytics. Analytics does not command contingency pricing, and CFOs underpay for dashboards.** | **WOUNDED.** |
| **Switching cost** | Low. | **HOLDS.** |
| **Legal** | None. | **HOLDS.** |
| **Distribution** | **You cannot sell an outcome ledger to someone whose outcomes you do not already process.** | **KILLED as a standalone.** |

**Verdict: KILLED as a standalone wedge; PROMOTED to mandatory architecture inside W1 and W3. Design outcome capture into the first schema — retrofitting it is exactly how every incumbent ended up at 0.**

---

## W5 — Contingency accessorial BPO

| Vector | Attack | Verdict |
|---|---|---|
| **Incumbent** | **ClearLane launched May 2026 at 10–25% of recovered revenue**, embedded in the customer's own TMS, adding accessorial audit July 2026. | **WOUNDED.** Occupied, though with no named logos and only $247K recovered over six months. |
| **Substitute** | The broker's own clerk. | **HOLDS.** |
| **Internal build** | Hire another clerk — a genuinely rational alternative at $61K loaded. | **WOUNDED.** |
| **Consultants** | This *is* the consultant. | **N/A** |
| **Pricing** | Validated: ClearLane 10–25%, Recoupex 20–50%, law firms 25–40%, Betachon 50%. | **HOLDS.** |
| **Switching cost** | None. | **HOLDS.** |
| **Legal** | **"We recover your money for a percentage" is precisely the fact pattern in WA RCW 19.16.100 ("any obligation for the payment of money… arising out of any agreement or contract" — not consumer-limited), NC G.S. §58-70-15, and Minn. Stat. §332.31. No FDCPA safe harbour (freight is commercial). *Rowland v. California Men's Colony* forecloses appearing in court.** | **WOUNDED.** Mitigable by positioning as invoice *preparation* on original billing rather than collection of delinquent debt — but that needs an opinion, not an assumption. |
| **Distribution** | Fine. | **HOLDS.** |
| **THE KILL SHOT** | **The brief explicitly penalises ideas requiring staffing before first revenue, and service margins do not compound: every new customer needs new hours.** | **KILLED as the business.** |

**Verdict: KILLED as the company; RETAINED as the paid discovery instrument. It is the only way to measure the collection uplift that every ROI model assumes.**

---

## Cross-cutting attacks that hit everything

### 1. The thesis's central number rests on one self-selected survey
Every ROI figure derives from ATRI 2024: 94.5% of fleets charge detention, ~75% of incidents billed, **fewer than 50% of invoices paid** → a derived 37.5% end-to-end collection rate. The agent that sourced it stated plainly: **voluntary survey, self-reported, not audited, reached through secondary reporting because ATRI's PDF is lead-gated, and the 75%/50% figures may not be legitimately multiplicable.** DOT OIG's own conclusion, unchanged since 2018: *"Accurate industrywide data on driver detention do not currently exist."* **FMCSA never implemented the data collection OIG recommended eight years ago.**

**Every ROI figure scales linearly with an ASSUMED 37.5%→60% uplift. At 45%, ROI Model A's recovery falls to $13,125/yr and the 25-truck tier becomes uninvestable.**

### 2. The backward-looking TAM is overstated 3–4×
§14705's 18 months governs **filing suit**, not billing — and is waivable under §14101(b)(1), which Arrive's BCA does expressly. **The real window is contractual: Arrive and Dray Alliance both run a 90-day billing waiver and a 180-day undercharge-notice cascade.** Any retro-recovery pitch built on 18 months is wrong.

### 3. Factored carriers may not own the claim
Factoring agreements assign *"all of our accounts… together with all proceeds thereof."* A supplemental detention claim on the same shipment is plausibly a proceed of an already-sold account. **TQL's own rate confirmation remits to RTS Financial** — factoring is the norm in the target segment. UCC §9-406 makes the broker dischargeable by paying the assignee. **The product may need tri-party consent, or may need to sell to factors rather than carriers.**

### 4. Handwriting will inject errors into invoices
Best available benchmark (arXiv 2604.16504, Apr 2026, 17 multimodal LLMs): **~85% accuracy, best-in-class hallucination rate 6%.** One field in sixteen is confidently invented. **On a 4-character in/out time, a single wrong character destroys the calculation — and a fabricated "0800" is worse than a blank, because it enters a dispute you will lose.** Confidence-gated human review is permanent architecture, not a V1 shortcut.

### 5. The pool is shrinking at the best accounts
FourKites markets detention reductions of **40–80%**; Trane removed **$2.69M**; Vector claims 30–67%. **Every enterprise facility that adopts a YMS shrinks the recoverable pool at exactly the accounts worth pursuing.** The counter-position — target the long tail of facilities with no YMS — is correct but caps the ceiling.

### 6. A YC company already tried and left
**TrackChain (YC S21) → Tiriel.** Detention/TONU recovery survived the pivot only as one of five agents inside a dispatch product. **The clearest available evidence that detention recovery alone did not support a venture-scale company for a funded, YC-backed team.**

### 7. The counterparty is arming itself faster than the carrier
**Freehand AI raised $75M in July 2026 to deny "unearned accessorial charges" for Meta, GE, J&J, Pfizer and Saks.** Loop has $95M. Lighthouz is YC-backed. **The payer side has nine figures and the biller side has a $299 Google Sheet.** That is the opportunity — and it means any biller-side product will be adjudicated by an adversary with better tooling than the claimant.

---

## What survives

| Wedge | Verdict | Condition of survival |
|---|---|---|
| **W3 Broker AR margin recovery** | **WOUNDED, survives** | Measure real leakage on 2–3 TMS exports first. Support absorb-by-policy. Run weekly. Assume a sophisticated broker builds v1 internally. |
| **W1 Real-time entitlement capture** | **WOUNDED, survives** | Notice must fire with no driver action. Sell at 50+ trucks or embed. Three-plus ELD sources. Counsel on Samsara §3.1 before the first design partner. |
| **W2 FMC D&D defect engine** | **CONDITIONALLY KILLED** | Revived only by a measured 2026 defect rate above ~15%. One experiment decides it. |
| **W6 Short-pay ledger** | **KILLED standalone** | Becomes mandatory architecture inside W1/W3. |
| **W5 Contingency BPO** | **KILLED as the business** | Retained as the paid discovery instrument. |
| **W4 Rule engine** | Not a wedge | Shared infrastructure under W1/W3. |
| **W7 Shipper-side prevention** | **KILLED** | No revival path. |

**Two wedges survive the red team, both wounded, and both gated on a measurement that has never been published.**
