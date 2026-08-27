# Opportunity Dossier — Home-Care Agency EVV Survival Layer ("EVV Defense Desk")

Validator: Wave-2 validator, H09 · Date: 2026-08-27 · Source hypothesis: H09 (Manager 1 promotion memo, Rank 9) · Ground(s): 10 (category_gap_analytics), 03 (human_middleware_jobs)

All new evidence: `outputs/evidence/dh09_evv_homecare.jsonl` (H09-E1…E25). Carried evidence cited by scout claim ID (S10-5-*, S03-8-*), all Manager-1-verified. Scope note up front: this dossier validates the **EVV/billing survival layer** as the wedge and demotes the promotion entry's "+ referral intake" half to expansion (see §4) — intake has a different competitive set (Forcura-class fax workflow), a weaker forcing function, and would dilute a 90-day build.

---

## 1. The pain, restated precisely

**Who hurts:** Small-to-mid licensed home-care agencies (Medicaid personal care services and home health) — roughly 2–200 caregivers, median agency revenue ~$2.3M with ~10% net margins (H09-E19, vendor-adjacent, labeled) — in the ~40 states that route EVV through a designated aggregator, plus the FMSAs/CDS employers in consumer-directed programs. The buyer is the owner/administrator; the worker is a billing/EVV coordinator (3,253 open postings for "EVV coordinator home care" on one aggregator alone, H09-E16; 623 intake-coordinator postings carried, S03-8-E4).

**The workflow failure:** The 21st Century Cures Act makes EVV mandatory for Medicaid personal care (in force since 2020–21) and home health (2023). States designate an aggregator — after HHAeXchange bought Sandata (Oct 2024), essentially **one company's systems** sit in the mandated path in ~40 states (26 Sandata + 14 HHAX, H09-E25/E11). Every visit must be captured, verified, and *accepted* by the aggregator, then **match the claim line item on six data elements** (Medicaid ID, date, NPI/EVV provider ID, HCPCS, modifiers, units — H09-E1) or the claim **denies** (TX result codes EVV02–EVV06). The agency therefore runs a permanent four-way reconciliation — authorized vs. scheduled vs. EVV-verified vs. billed/paid — across its scheduling system, the aggregator portal, and payer remits, by hand. The mandated portal itself is rated 3.6/5 with an **F** BBB rating and 11 of 12 complaints unanswered (S10-5-E1, H09-E13); its glitches are the coordinator's job ("Imagine spending hours per day fixing glitches HHAeXchange creates," H09-E14).

**Frequency:** Per-visit, daily (485M visits/yr flow through HHAX systems alone, H09-E12); claims each cycle; a 95-day hard visit-maintenance window in TX after which visits lock (H09-E2); quarterly usage-score reviews with an 80% floor (H09-E3/E5).

**Strongest three artifacts:**
1. **Delaware biller, r/CodingandBilling, May 2026 (new, H09-E15, Arctic Shift-verified):** "all visits show verified in Sandata but only 50% are linking to claims at the MCO level. The failures are intermittent… With the October 1st EVV mandate coming, these will all start getting denied and I need to fix this before then." Three MCOs, a third-party AMS (Rosemark), a hard date — the entire hypothesis in one post, unanswered.
2. **Capterra operator quotes on the mandated aggregator (carried, S10-5-E1…E4, verified verbatim):** "Lost over $18000 dollars because of a syntax error in the software"; "We didn't get paid for over 4 months"; "Shifts worked don't show up so they are not paid"; 3-hour support holds.
3. **Texas policy mechanics (new, H09-E1/E2/E3, official):** deny codes EVV02–06; 95-day lock with unlock only for state-system error; recoupment if visit data changes post-claim; 80% usage score → CAP → payment hold → contract termination. The pain is codified, not anecdotal.

---

## 2. Budget proof

| Budget line | Amount | Source |
|---|---|---|
| EVV/billing coordinator headcount | 3,253 open "EVV coordinator home care" postings; e.g., $3,120/mo (Erie PA); intake coordinators $58,240–60,320/yr | H09-E16; S03-8-E1 |
| Outsourced billing | 4–10% of collections, or $3–12/claim; **TX/NY Medicaid must be flat/per-claim** (fee-splitting rules) | H09-E17 |
| Pure-play home-care RCM incumbent | Paradigm: ~4,000 agencies pay for VA/Medicaid RCM; $1.6B claims/yr processed | H09-E24 |
| Exact-wedge software comp | Reeve: $750–1,000/branch/mo, month-to-month | H09-E23 |
| Aggregator's own paid tier + RCM services | HHAX from ~$375/mo; sells "RCM Services"/"Billing & Claims" into its own captive base | H09-E14, E12 |
| Losses absorbed | $18k single-incident; 4-month payment gaps; denied claims after 95-day lock are forfeited; sub-80% usage = payment holds | S10-5-E2/E3; H09-E2/E3 |

**Per-customer arithmetic (labeled inference from verified figures):** a Medicaid-heavy agency at ~$2M revenue bills roughly 8–12k visit-claims/yr. At the Delaware artifact's failure class (intermittent link failures on even 5% of visits post-hard-edit), ~400–600 claim lines/yr deny or stall; at ~$80–120/visit-day line values that is **$40–70k/yr gated**, plus the 95-day forfeiture risk on whatever isn't worked in time, on ~10% margins ($200k profit) — i.e., unworked EVV exceptions can consume a quarter of profit. The standing cost is the coordinator ($37–60k loaded) whose job is this reconciliation. A $300–800/mo tool is 6–25% of that head and pays back on one prevented batch denial. Reeve's $9–12k/yr price and Paradigm's 4,000 paying agencies prove the budget line is real at both software and service price points.

---

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| HHAeXchange free state portal (+ Sandata) | Product (mandated aggregator) | Every provider in ~40 designated states | Free (state-sponsored) | It IS the pain: 3.6/5, BBB F, 11/12 complaints unanswered; unconfirmed visits, vanished shifts, $18k syntax-error loss, months-long support (S10-5-E1…E4; H09-E13/E14). Cannot be displaced — only survived |
| HHAeXchange paid platform + RCM Services (+ Cashé, Generations AMS) | Product + service (vertically integrated incumbent) | Agencies upselling from free portal | From ~$375/mo (H09-E14) | Same vendor as the wound; support 3.1; conflict of interest — it monetizes both the pipe and the fix; March-2026 review: third-party billed shifts "will not populate" (H09-E14) |
| AxisCare / AlayaCare / WellSky Personal Care / CareVoyant / Alora | Product (agency management systems) | Small→large agencies | AxisCare custom (EVV bundled); AlayaCare ~$1,000–1,650/mo + setup; WellSky ~$100/active client/mo (H09-E20/E21) | Liked (AxisCare 4.7/729) but sell breadth: scheduling-first, EVV as compliance checkbox + billing add-on service ("Medicaid experts… claim scrubbing" = humans). None owns cross-system reconciliation: visits verified in the aggregator still fail to link to claims (H09-E15) and shifts billed in the AMS never populate in HHAX (H09-E14) |
| Paradigm (+ Careswitch AI, Sept 2025) | Service (pure-play home-care RCM) | ~4,000 agencies, VA + Medicaid | Undisclosed; flat/per-claim for TX/NY Medicaid (H09-E17 context) | Outsourcing displacement: agency hands billing away. Doesn't serve agencies keeping billing in-house (the coordinator-employing majority per 3,253 postings); franchise-network GTM (Amada) skews larger (H09-E24) |
| Reeve | Product (exact wedge: read-only margin recovery) | Medicaid home care, 49 jurisdictions claimed | Free review; $750–1,000/branch/mo (H09-E23) | Validates wedge + price. Pre-traction: no funding, launch coverage, or customers found (searched 2026-08-27); browser-only/read-only = no workflow, deadline machine, or fix-tracking depth yet |
| Regional billing services / consultants (CareBravo, Hayes RCM, HealthRev, PMB) | Service | State-local agency clusters | 4–10% of collections or per-claim (H09-E17) | Human labor at service prices; per-claim Medicaid pricing in TX/NY caps their margin; they absorb, not remove, the reconciliation |
| In-house coordinator + portal archaeology | Internal hire (status quo) | Everyone | $37–60k/yr (H09-E16; S03-8-E1) | "Hours per day fixing glitches" (H09-E14); intermittent failures defeat manual pattern-finding (H09-E15); one human vs. quarterly usage scores + 95-day locks |
| Do nothing (write off / eat holds) | DIY default | Marginal agencies | Forfeited claims + payment holds | 95-day lock makes forfeiture permanent (H09-E2); sub-80% usage escalates to payment holds and contract termination (H09-E3) |

**Deep-verified closest three:**
- **HHAeXchange (the platform-monopoly incumbent):** acquired Sandata (Oct 2024), Cashé, and Generations in one year (H09-E11) — now spans ~40 states' aggregation (H09-E25), 32k providers, $38B payments (H09-E12), plus agency-side AMS and RCM services. Shipping velocity on payer/state products is high; agency-side experience quality is the documented casualty (3.6★, BBB F). Its incentive structure (paid by states/payers; upsells captive agencies) has left the agency-side wound open through five years of reviews (2021→2026).
- **Paradigm:** the budget-proof giant of the space — ~4,000 agencies, $1.6B claims/yr, 30% of VA home-care spend, now with Careswitch's "agentic claims processing" (H09-E24). It is a **service** that takes the billing function; it validates AI-in-home-care-RCM and will press down-market. The in-house-software counter-positioning must be explicit to survive it.
- **Reeve:** same wedge, read-only, $750–1,000/branch/mo, agency-export-based, privacy-forward (client-side processing). No observable traction. Treat as Muni-Health-analog (H01): proof of demand shape, not a blocker — but a 6–12-month clock.

**Which segment is unserved (proved):** agencies that keep billing in-house (the 3,253-posting majority) in hard-edit aggregator states, running a third-party or state-portal EVV stack, who need **pre-claim match assurance + exception triage + deadline/usage-score defense** as software. Aggregator (HHAX) won't build it well for them (track record + conflict), AMS vendors bundle humans instead (AxisCare's "Medicaid experts"), Paradigm requires outsourcing, Reeve is embryonic.

---

## 4. The wedge

**"Match every visit to money before the state does."** A read-first EVV defense desk for Medicaid home-care agencies, beachhead **Texas** (largest single-aggregator program; codified 95-day/80% mechanics; TAHC&H channel) with **Ohio** fast-follow (freshest hard-deny cohort, H09-E7):

1. **Nightly ingestion** of what the agency already exports: AMS schedule/visit files (AxisCare/WellSky/AlayaCare/Rosemark CSVs — the surface Reeve proves, H09-E23), aggregator visit-status reports (TMHP EVV Portal accepted-visit/history searches; HHAX/Sandata provider reports), and 835/837s.
2. **Five-way match engine** — authorized : scheduled : EVV-accepted : billed : paid — every exception coded by cause (unverified visit, units drift, modifier mismatch, missing auth, accepted-but-unbilled, billed-but-unmatched) mirroring state result codes (EVV01–08 in TX, H09-E1).
3. **Pre-claim gate:** "these lines will deny EVV02–06 — fix before submission," with per-line fix instructions keyed to the state rulebook (the deterministic advantage: unlike H01's payer-discretion denials, EVV mismatches are computable in advance).
4. **Deadline + score state machine:** per-visit 95-day maintenance countdown, payer timely-filing clocks, projected quarterly EVV Usage Score vs. the 80% floor with per-cause remediation lists (H09-E2/E3/E5).
5. **Fix-packet drafting (agent-drafted, human-executed):** reason codes, documentation checklists, and unlock-request drafts; staff performs corrections in the EVV system/portal — deliberately **no bot write-back** into the aggregator.
6. **Recovery ledger:** dollars prevented/recovered per payer/cause — the renewal artifact and the free-audit hook ("upload last 90 days of exports; see what's leaking").

**Explicitly does NOT do:** EVV capture (no clock-in app — never compete with the mandate), claim submission (v1), scheduling, payroll, clinical documentation, **referral intake** (S03-8 evidence is real but is expansion slot #2 — different competitors, softer forcing function), and no autonomous portal automation.

**≤90 days by founder + AI agents? Yes, for a 1–2 state beachhead — justified:** CSV/report ingestion + matching + countdowns are conventional engineering; the grindable surface (state EVV policy handbooks, result codes, payer billing rules, reason-code libraries) is exactly what the agent team compiles fast; Reeve demonstrates a browser-based read-only v1 is buildable by a tiny team (H09-E23); BAA/PHI posture is the standard SaaS pattern (same as H01). The 49-state rules matrix is explicitly NOT the 90-day scope — Texas + Ohio only.

---

## 5. Forcing function & why now

**Forcing function (Grade A, held and escalating):** federal statute (Cures Act) + state designation makes the pipe unavoidable; **per-claim money gate** (unmatched = denied, H09-E1/E4/E6); **hard per-visit deadline** (95-day lock, forfeiture-shaped, H09-E2); **quarterly compliance score** with payment holds and contract termination above it (H09-E3). Three stacked compulsion layers, all currently in force.

**Why now (2024–2026):**
- **The soft→hard edit wave just landed:** TX claims-matching denials live Apr 1, 2024 (H09-E4); NC managed-care home health hard launch Oct 1, 2025 — "claims… without the required EVV data will be denied" (H09-E6); Ohio phased hard-deny through Mar 1, 2026 with recoupment (H09-E7); Delaware biller bracing for Oct 1 (H09-E15). Pay-and-report is over; the reconciliation debt now prices in denials.
- **Enforcement re-armed in 2026:** TX MCO usage-score reviews resumed March 2026 at the 80% floor (H09-E5); sub-80% = CAP + payment holds (H09-E3/E25).
- **The aggregator consolidated into a monopoly (Oct 2024):** HHAX + Sandata + agency-side AMS acquisitions (H09-E11) — a single counterparty whose agency-side quality is documented as bad (3.6★/BBB F) and whose incentives point at payers and upsells, not fixing the small agency's reconciliation.
- **Medicaid rate pressure (H.R. 1, 2025) is squeezing margins** — at ~10% net (H09-E19), leakage defense is one of the few controllable profit levers; KFF documents states managing home-care spending down ahead of H.R. 1 effects (H09-E18 context).

---

## 6. Distribution plan (solo-founder realistic)

**Named channels for the first 10 customers:**
1. **TAHC&H (Texas Association for Home Care & Hospice)** — vendor member + one conference/webinar slot; Texas is a single-aggregator, codified-mechanics beachhead.
2. **Ohio Council for Home Care & Hospice / the Mar-2026 MyCare hard-deny cohort** — same-quarter outreach hook ("no match, no pay started March 1 — free margin audit").
3. **HCAOA (3,500+ member agencies) state chapters** (H09-E22) — the proven vendor channel (Paradigm markets through it), webinars on "surviving hard edits."
4. **Pennsylvania Homecare Association (~700 providers)** (H09-E22) — HHAX-aggregator open-model state with carried MCO-mandate evidence (S10-5-E5).
5. **Home-care owner Facebook groups and forums** — the administrator watering holes the promotion memo named; plus r/CodingandBilling home-care threads (the Delaware poster class, H09-E15) for the biller-influencer motion.
6. **Free "EVV margin audit"** on the agency's own exports as the demo-close (Reeve's free Margin Review proves the motion; ours adds the deadline/score state machine).

**Sales cycle estimate:** 2–6 weeks; owner-operator buyers, no procurement; audit-to-paid conversion when the audit shows ≥$5k at-risk. **Price & packaging hypothesis (comparable-priced):** $299/mo (≤50 clients), $599/mo (≤150), $999/mo multi-branch — under Reeve's $750–1,000/branch (H09-E23), ~10–20% of a coordinator (H09-E16), flat-fee (which the TX/NY Medicaid fee-splitting environment structurally favors over %-of-collections, H09-E17).

---

## 7. AI-structural advantage

The reconciliation labor is salaried and posted (3,253 openings, H09-E16); services price it at 4–10% of collections or $3–12/claim (H09-E17). Agents collapse the marginal cost of "compare five datasets, classify the exception, look up the state rule, draft the fix packet, track the deadline" to cents — a flat $299–999/mo product profitably serves a 60-client agency no incumbent economics reach: Paradigm's service model needs the whole billing relationship; AMS vendors monetize breadth seats and bundled human billing teams; HHAX monetizes the payer side and upsells; none can sell a $500/mo *defense layer against HHAX's own pipe* without breaking their model or their state contracts. The per-state rulebook compilation (handbooks, result codes, MCO alerts — H09-E1/E2/E3/E5/E6/E7) is precisely agent-grindable research that a seat-based incumbent staffs humans for.

---

## 8. Moat path

**Accumulates with usage:** (1) the **state × payer × cause × fix outcome corpus** — which exception codes actually deny, which fixes clear them, per MCO (intermittent-failure patterns like H09-E15 are invisible to any single agency); (2) a maintained **50-state EVV rulebook** (deadlines, codes, thresholds, MCO alerts) that decays without constant tending — a content asset competitors must re-grind; (3) **workflow lock-in**: open exception queues, deadline clocks, and usage-score history live in the product mid-quarter; (4) cross-agency benchmarking ("your EVV02 rate vs. TX peers").

**Thin-wrapper honesty:** the matching itself is deterministic joins — copyable; Reeve exists. The defensible product is rulebook maintenance + deadline/score state machine + outcome data + multi-branch workflow. Moderate moat (3/5): real accumulation, 12–24 months ahead of a funded copier, and the aggregator could bundle a version (see R1).

---

## 9. Risks & unknowns (top 5 + 1)

| # | Risk | Resolving test |
|---|---|---|
| R1 | **Incumbent extension:** HHAX (owner of the pipe + AMS + RCM services) ships native five-way reconciliation into state portals or its paid tier | Quarterly release monitoring (HHAX/Sandata release notes, state portal updates). Kill trigger: state-funded portals gain cross-system pre-claim reconciliation + deadline tooling for third-party-AMS agencies. Mitigant: 5 years of reviews (2021→2026) show agency-side neglect; state contracts scope them to aggregation, not agency tooling |
| R2 | **Paradigm/Careswitch productizes self-serve software** at small-agency prices (they own the AI team and 4,000 logos) | Track Paradigm releases/pricing; 10 interviews with agencies that evaluated-but-rejected outsourcing (why keep in-house?). Kill trigger: Paradigm launches sub-$1k/mo self-serve reconciliation software, not service |
| R3 | **Data-access friction (the residual hostage risk):** portal report formats change; exports get rate-limited; fix execution stays manual | TX pilot on 3 agencies' real exports: measure ingestion coverage, hours saved/wk (target ≥60%), and whether portal reports suffice without APIs. Design rule: state-run surfaces (TMHP portal, 835s) and agency-owned exports only; no HHAX-goodwill dependency load-bearing |
| R4 | **WTP at ~10% margins:** owners may tolerate leakage rather than add spend | Free-audit conversion test: 20 audits via TAHC&H/HCAOA; convert ≥25% at $299–599/mo when audit shows ≥$5k at risk. Reeve's conversion motion is the comparable to beat |
| R5 | **Buyer-pool contraction:** H.R. 1 Medicaid cuts + rate pressure consolidate/kill small agencies | Track KFF H.R.1 analyses + TX/OH provider-enrollment counts annually; consolidation raises per-agency sophistication (multi-branch tier) even as counts fall — retest pricing mix |
| R6 | **Wedge-specific operator-voice thinness:** most public rage targets the aggregator generally, not the reconciliation task by name | 15 owner/coordinator interviews (via associations + the H09-E15/E16 populations): confirm a named human currently owns EVV reconciliation and what their exception volume is |

---

## 10. Scores

| # | Dimension | Weight | Score | Rationale (evidence) |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 5 | Per-visit daily; unpaid caregivers, $18k losses, 4-month gaps (S10-5-E2/E3); 2026 hard-deny wave (H09-E6/E7); emotionally charged, lawyer-threat grade (H09-E13) |
| 2 | Budget proof | 15% | 4 | Salaried coordinators (3,253 postings), 4–10%/per-claim services, Paradigm's 4,000 paying agencies, Reeve's $750–1,000/branch price (H09-E16/E17/E23/E24); docked one: thin ~10% margins cap ceiling and home-care-specific salary depth is thinner than H01's |
| 3 | Competitive gap | 12% | 4 | Aggregator hated + undisplaceable; AMS tier liked but bundles humans, doesn't reconcile cross-system (H09-E14/E15/E20); Paradigm = outsourcing only; Reeve pre-traction. In-house software layer demonstrably open; docked one for the number of adjacent players circling |
| 4 | Forcing function | 10% | 5 | Federal mandate + per-claim denial gate + 95-day forfeiture locks + quarterly 80% score with payment holds (H09-E1/E2/E3/E5) — the strongest stacked compulsion in the promoted set |
| 5 | Founder+agents feasibility | 12% | 4 | Read-only exports + deterministic matching + agent-grindable rulebooks; Reeve proves tiny-team buildability (H09-E23); docked one for PHI trust and per-state rules breadth beyond the beachhead |
| 6 | Distribution reachability | 10% | 3 | Real, named channels (TAHC&H, HCAOA 3,500, PHA 700, owner FB groups) but no dense open forum equivalent to H01's subreddit; association channels are pay/relationship-gated |
| 7 | AI-structural advantage | 8% | 4 | Collapses posted coordinator labor to software price; incumbents' service/seat/state-contract models resist selling a cheap defense layer against their own pipe (§7) |
| 8 | Moat path | 8% | 3 | Rulebook + outcome corpus + deadline lock-in accumulate; matching core is copyable; aggregator bundling risk (§8, R1) |
| 9 | Expansion ceiling | 5% | 4 | Same buyer expands to referral intake (S03-8), auth tracking, full Medicaid home-care back office; $145.9B HCBS spend growing 12.8%/yr (H09-E18); shared engine with the H01–H03 RCM bundle |
| 10 | Durability | 5% | 3 | Statutory mandate is durable and enforcement is tightening (good); but HHAX bundling, Paradigm's AI push, and Medicaid funding cuts are live erosion vectors |

**Weighted total: (75+60+48+50+48+30+32+24+20+15)/5 = 80.4 → 80/100 (bottom of pursue band).**

**Hard gates:**
- **Budget proof: PASS** (salaries, services, two priced software comps, HHAX's own paid RCM).
- **Reachable buyer: PASS** (owner-operators, association/community channels, free-audit self-serve motion).
- **Thin-wrapper: PASS** (multi-source ingestion + deterministic match engine + deadline/score state machine + rulebook; not a model call — the LLM is garnish here, the workflow is the product).
- **Head-on collision: PASS, narrow.** No funded incumbent ships this wedge to this segment as software: Paradigm = same pain, service model, larger/franchise GTM (H09-E24); HHAX = same buyer, conflicted incumbent whose agency-side quality is the documented failure (H09-E13/E14); Reeve = same wedge, pre-traction micro-entrant (H09-E23). Kill triggers defined at R1/R2.
- **Platform hostage: PASS, conditional — the decisive gate, examined:** the mandated aggregator cannot be displaced, but the wedge does not require its permission. It reads (a) the agency's own AMS exports, (b) state-run portal reports (TMHP's EVV Portal is state infrastructure; provider report access is a program requirement, H09-E1-page context), (c) 835/837 files from payers/clearinghouses. Writes are human-executed in the agency's existing tools. Alternate-EVV/PSO integration paths are state-published contractual specs, not vendor goodwill (H09-E8/E9/E10). Reeve's shipped client-side model proves the surface exists today (H09-E23). Residual honesty: deep automation (write-back, API reads of HHAX) WOULD be tolerance-dependent — the design rule (R3) is that nothing load-bearing depends on it. This is a multi-surface, human-in-the-loop read layer, not a single-API business.
- **Regulated practice: PASS** (billing-operations software under agency staff execution; flat pricing also sidesteps TX/NY fee-splitting exposure that constrains %-based services, H09-E17).

**Displacement sentence:** Current solution = a $37–60k EVV/billing coordinator (3,253 open postings) or a 4–10%-of-collections / $3–12-per-claim billing service reconciling scheduler ↔ aggregator ↔ claims by hand, while hard edits deny mismatches, 95-day locks forfeit unworked visits, and sub-80% usage scores trigger payment holds. New product = a $299–999/mo EVV defense desk that matches authorized/scheduled/verified/billed/paid nightly, gates claims before they deny, and works the fix queue against every clock. The customer switches because one prevented denial batch or one recovered month of a caregiver's visits (the $18k-class incident) repays a year, verifiable in the product's own ledger.

---

## 11. Verdict proposal

**PURSUE (80/100, lower band edge) — as the Medicaid-home-care expression of the RCM-defense thesis, not an independent bet.** Stacked Grade-A forcing functions (per-claim denial + 95-day forfeiture + quarterly score holds), a 2025–26 hard-edit wave, a hated monopoly pipe, and a priced, provably open in-house-software gap. **Bundle note (mandated question): yes — H09 is a vertical instance of the H01/H02/H03 denial/billing-defense shape** (counterparty automated first; defense manual; deadlines forfeit money; middleware wages published), with two differences that cut both ways: denials here are deterministic data mismatches (higher product efficacy, prevention possible) but the buyer pool is thinner-margined and differently distributed. If Wave 3 concentrates the bundle, attack H01 first and hold H09 as the expansion vertical sharing the 835/deadline/recovery-ledger engine; as a standalone, proceed only past R1/R2 kill triggers and the R4 conversion test.

---

## 12. Evidence ledger

New evidence: `outputs/evidence/dh09_evv_homecare.jsonl` — 25 records, H09-E1…E25, schema-valid, all accessed 2026-08-27.

| ID | Claim (short) | Type |
|---|---|---|
| H09-E1 | TX claims matching: 6 match elements; EVV02–06 = deny; post-match changes = recoupment | official-doc |
| H09-E2 | TX 95-day visit-maintenance lock; unlock only for state error | official-doc |
| H09-E3 | TX 80% quarterly usage score; training→CAP→payment hold→termination | official-doc |
| H09-E4 | TX matching live 2024-04-01; unmatched claims deny | official-doc |
| H09-E5 | TX MCO reviews resume 2026-03 at 80% floor | official-doc (payer) |
| H09-E6 | NC hard launch 2025-10-01: no EVV data = denied | official-doc |
| H09-E7 | OH phased hard-deny 2025→2026-03-01 (no match, no pay) | vendor-blog (corroborated ×4) |
| H09-E8 | TX PSO path: approved third-party systems exchange data with aggregator | official-doc |
| H09-E9 | HHAX EDI/API third-party integration + prebilling stage | vendor-docs |
| H09-E10 | NJ: third-party EVV imports via published EDI specs | vendor-docs |
| H09-E11 | HHAX acquired Sandata (2024-10) + Cashé + Generations | press-release |
| H09-E12 | HHAX scale: 32k providers, 30 states, 485M visits, $38B; sells RCM itself | vendor-marketing |
| H09-E13 | HHAX BBB F; 11/12 complaints unanswered; owner quotes | review |
| H09-E14 | HHAX 3.6/5; ~$375/mo start; 2026 integration-failure quote | review |
| H09-E15 | Delaware biller: 50% verified visits not linking; Oct 1 dread (Arctic Shift) | forum-post |
| H09-E16 | 3,253 EVV-coordinator postings; $3,120/mo example | job-posting |
| H09-E17 | Billing services 4–10% / $3–12 claim; TX/NY Medicaid flat-fee rule | vendor-blog |
| H09-E18 | HCBS: 8.4M users, $145.9B (2023), +50.2% 2019–23; Medicaid ⅔ of home care | report (KFF/MACPAC) |
| H09-E19 | Agency economics: $2.3M median revenue, ~10% net; 51% high EVV concern | vendor-blog (labeled) |
| H09-E20 | AxisCare 4.7/729; EVV bundled; human "claim scrubbing" service | review |
| H09-E21 | AlayaCare ~$1,000–1,650/mo; WellSky ~$100/client/mo | vendor-pricing (3rd-party) |
| H09-E22 | HCAOA 3,500+ members; PHA ~700 providers | association |
| H09-E23 | Reeve: exact wedge, $750–1,000/branch/mo, export-based, pre-traction | vendor-pricing |
| H09-E24 | Paradigm: ~4,000 agencies, $1.6B claims/yr, Careswitch AI acq 2025-09 | press-release |
| H09-E25 | 2026 landscape: Sandata 26 + HHAX 14 states; 85% norms; TX/OH escalation | vendor-blog (labeled) |

Carried (verified upstream): S10-5-E1…E6 (Capterra operator quotes incl. $18k loss; TMHP/HHAX designation), S03-8-E1…E4 (intake coordinator postings/salaries) — see `outputs/evidence/s10_category_gap_analytics.jsonl`, `s03_human_middleware_jobs.jsonl`.
