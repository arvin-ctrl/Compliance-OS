# Opportunity Dossier — Collision-Shop Supplement & Short-Pay Defense ("Denial Defense for Auto Body")

Validator: Wave-2 validator, H20 (late promotion) · Date: 2026-08-27 · Source hypothesis: H20 ← S04B-1 (primary) + S04B-3 (estimating-capacity twin, folded in as the services-collapse angle) · Ground(s): 04b (vertical SMB re-run)

All new evidence: `outputs/evidence/dh20_collision_supplements.jsonl` (H20-E1…E30). Carried evidence cited by scout claim ID (S04B-1-*, S04B-2-*, S04B-3-*), all scout-verified via Arctic Shift or direct fetch on 2026-08-27. Shape analogy: H01 (healthcare denial defense, PURSUE 85) — compared in §10; this market validated on its own evidence.

---

## 1. The pain, restated precisely

**Who hurts:** Independent and small-MSO collision shops — 1–3 locations, 3–20 staff — which are ~68.7% of the ~30,200 US collision repair locations (Focus Advisors mid-2025, H20-E12; total-count arithmetic labeled inference: Big 5 = 4,019 locations = 13.3%). The owner, an estimator ($50–110k, S04B-3-E5), or a one-person front office (S04B-2-E5) runs the insurer fight. Customers are collateral: cars sit, rentals cap out, balances get billed to them (S04B-1-E4, E12).

**The workflow failure:** The insurer's first number now arrives increasingly from a photo/AI channel — photo estimates grew from <1% of initial repairable estimates (2016) to 25.6–26.4% (2024–25) while insurer staff-written estimates halved to 18% (H20-E4, E1); 7 of the top-10 carriers had adopted CCC's AI photo estimating by early 2023 (H20-E5); Progressive's photo-estimate-group sheets carry AI per its own staff (H20-E7). Photo initials are structurally low: supplements on photo estimates average **>50% of the original appraisal value** (Mitchell, H20-E3), i.e., "a $1,000 photo estimate turn[s] into a $20,000 blueprint" (S04B-1-E6). So essentially every non-DRP job becomes one or more supplements (panel study of 100 non-DRP jobs: "virtually all" ≥1, "vast majority" 2+, S04B-1-E5) — and the fight over each one is manual: photo packets, invoices, resubmissions, phone queues. Shops report supplements confirmed at ~30% of written value, supplements that "disappear on their end," calibrations refused "even when we have photos and invoices documenting," physical adjusters dispatched after repairs are complete, and 2-day bumper jobs stretching to 3+ weeks (S04B-1-E1…E4). In 2024 the counterparty automated the audit side too: CCC Intelligent Reinspection AI-reviews incoming shop estimates for insurers, auto-routing per insurer rules (H20-E6). The shop side still fights by hand.

**Frequency:** Per-claim, continuous. Supplement share of repairable appraisals rose YoY in each of the first three quarters of 2025 (CCC Crash Course 2026, H20-E1); ~70% of even DRP claims carry ≥1 supplement (up from <50% in 2001), 2–4-supplement claims tripled to >30% (H20-E2); 51.5% of ADAS calibrations appear only on supplements, forcing mid-repair approval loops (S04B-1-E7), and calibration lines grew 31.4% in 2025 at $688 avg when present (H20-E29). Response loops: 4.2 days average per supplement round, 6–8+ at some large insurers (S04B-1-E5), ~14 days reported at State Farm (S04B-1-E2) — while the completed car "stays on your lot until the final bill is paid" (H20-E8).

**Strongest three artifacts:**
1. **r/Autobody "Statefarm Nightmare Company" (2026-04, five independent shops in one thread, carried S04B-1-E1…E4):** supplements confirmed at ~30% of written value; 14-day response cycles; supplements canceled/vanishing; calibrations refused with documentation in hand.
2. **CCC's own numbers (new, H20-E1/E2/E4):** supplement frequency rising YoY through 2025 on top of ~70%-of-DRP-claims baseline; photo channel at 26.4% of inspections; insurer human appraisal capacity halved since 2017 — the mechanism, quantified by the counterparty's platform.
3. **CRASH Network 2026 Insurer Report Card (new, H20-E13):** 1,100+ shops graded 91 carriers; none of the top-10 insurers scored above C+ — market-wide, current, systematic.

---

## 2. Budget proof

| Budget line | Amount | Source |
|---|---|---|
| In-house estimator (writes + fights supplements) | $50,000–$110,000/yr (Caliber postings); "$70+k salary... to do these" (operator); same-day supplement communication a listed duty | S04B-3-E5, S04B-1-E9, S04B-1-E10 |
| Outsourced estimate/supplement writing | $125 per estimate or supplement incl. DRP; $75 desk reviews; claims handling w/ insurer negotiation from $25 (Shop Sheet); freelancers advertising per-estimate help in r/Autobody | S04B-1-E8, S04B-3-E4 |
| Software already priced at this pain | VaraFix $349/mo/location (launched 2026-08-25); OEC EstimateIQ quote-priced, "7X ROI" claim; Revv quote-priced with $20M VC behind it | H20-E15, E18, E17 |
| Revenue leakage absorbed | Vendor-measured: ~$548/estimate of missed operations (VaraFix sample), >$1,200/estimate calibration-adjacent (Revv claim); shop-reported: supplements paid at ~30% of written; secondary blogs: $1,200–$1,800 initial-to-final gap (unverified magnitude) | H20-E15, E17, S04B-1-E1, H20-E30 |
| Consultant/training spend | Collision Advice-class consulting and 20-Group coaching (quote-priced); the free Who Pays for What? survey franchise exists because shops systematically under-bill | H20-E28 |

**Per-shop arithmetic (labeled inference from the verified figures above):** a 1-location independent doing ~40 ROs/month (~$2.3M/yr at the $4,818 average RO, H20-E1) with a 50/50 DRP/non-DRP mix: (a) **labor**: ~20 non-DRP ROs × 1–2 supplements each = 25–40 supplement rounds/month; at Shop Sheet's $125/unit that is **$3–5k/month of labor-equivalent**, currently absorbed by the estimator/owner ("I'm doing two jobs for the amount of sheets I gotta write," S04B-1-E9); (b) **short-pay/missed-op pool**: at the vendors' $548–$1,200/estimate found-money claims and the shop-reported 30%-of-written approvals, the contested delta plausibly runs **$200–600/RO ≈ $4–12k/month** on the non-DRP side alone; (c) **cycle time**: each supplement round adds 4.2–14 days of stall occupancy and rental-clock risk billed to nobody. Against that, category software prices at $349/mo (H20-E15) — the ROI frame the incumbent entrant itself uses.

---

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| CCC ONE (estimating + DRP rails) + Estimating IQ AI | Product (platform incumbent) | Nearly all insurer-facing shops | ~$1,200/mo reported small-shop, custom-quote, 12-mo+ contracts (S04B-2-E2/E6) | Writes estimate/supplement lines and transmits; AI pre-populates *initial* estimates only (H20-E20); no missed-op review, no short-pay tracker, no fight workflow. Sells the audit AI to the *other* side (Intelligent Reinspection, H20-E6) |
| Mitchell Cloud Estimating / Audatex (Qapter) | Product | Shops (Mitchell gaining SF DRP share) | Custom | Same shape: estimating, not defense; Mitchell's AI (Intelligent Estimating) is carrier-facing; shops report inaccurate part data forcing hand-verification (S04B-2-E5) |
| VaraFix (launched 2026-08-25) | Product (new entrant, same wedge front half) | DRP + non-DRP shops | $349/mo/location, free 3-review trial | Pre-submission review only: CCC PDF ingest, missed-op flags + OEM-backed docs in 90s (H20-E15/E16). No supplement tracker, no response-clock/carrier analytics, no short-pay ledger; Mitchell "planned"; press-release-stage, no disclosed funding |
| OEC EstimateIQ | Product (rules-based, prior generation) | Shops/estimators | Quote-priced; "7X ROI" | Static rules from part codes, no AI, no negotiation/tracking layer (H20-E18); quote-gated sales motion |
| Revv | Product (funded adjacent: ADAS slice) | 200+ shops, calibration-heavy | Quote-priced; $20M Series A | Owns calibration ID + OEM documentation (H20-E17) — the single worst short-pay item — but not general supplements, not the response-cycle fight; expansion risk noted in §9 |
| Shop Sheet-class virtual estimating + freelance writers | Service (the priced human labor) | Backed-up/understaffed shops | $125/estimate or supplement; $75 reviews; $25+ claims handling | Human per-unit throughput; no leverage accumulation; licensing friction in appraiser-license states for remote writers (H20-E23/E24); doesn't fix the shop's own capacity (S04B-3) |
| Collision Advice-class consultants + Who Pays for What? + 20 Groups | Service (coaching) | Motivated owners | Quote-priced; survey free | Teaches billing norms quarterly in aggregate (H20-E28); nothing per-claim, nothing in the workflow at write/fight time |
| In-house estimator + phone/email/portal archaeology | Internal hire (status quo) | Everyone | $50–110k + owner nights | Undertrained ("zero estimating experience," 3.5 yrs untaught — S04B-3-E1/E2); shortage (S04B-3-E3); loses to 14-day loops and vanishing supplements (S04B-1-E2/E3) |
| Claimory (SMS entrant) | Product (adjacent) | Independent collision shops | Unknown (JS-walled) | Marketing a "Supplement Negotiation Playbook" (H20-E22) — collision SMS with claims angle; unproven, second entrant circling |
| Do nothing / eat it / fire the carrier / bill the customer | DIY default | The evidenced majority | 30%-of-written approvals; lost carriers' work | "Doesn't even accept State Farm customers anymore"; "We charge the customer for whatever their carrier won't pay" (S04B-1-E12); shops banning Progressive/SF (H20-E7) — revenue refused instead of recovered |

**Deep-verified closest three:**
- **VaraFix** — same buyer, same entry feature (estimate review for missed ops), launched two days before this dossier's access date. Real product, not vapor: self-serve trial, $349/mo public price, CCC-PDF-only ingest, sample economics $548/estimate, "~83% adjuster approval" claim (H20-E15). Team is industry veterans incl. carrier auditors; no funding disclosed (H20-E16). What it does NOT ship: the post-submission fight — supplement state machine, response clocks vs carrier norms, short-pay ledger, escalation packets. It proves demand and price point for the front half of the wedge and contests it.
- **Revv** — $20M Series A (Left Lane, Nov 2024), 200+ shops, vendor-claimed $1,200/estimate undiscovered revenue (H20-E17). Focused on ADAS calibration identification/documentation — adjacent, not the same wedge; the credible expansion threat if calibration documentation generalizes to all supplement documentation.
- **CCC** — both-sides platform: repairer AI = initial-estimate pre-population (2021, H20-E20) plus 2025 agentic back-office roadmap with *no supplement-defense product named* (H20-E19); insurer AI = Estimate-STP (H20-E5) and Intelligent Reinspection (2024, H20-E6). CCC's economics (carrier contracts are its anchor revenue) make a shop-side "recover more from insurers" product a channel conflict — the same structural reason Waystar didn't go down-market in H01.

**Which segment is unserved (proved):** nobody at any price ships the **post-submission defense layer** — per-supplement state tracking against carrier response norms, short-pay deltas per line per carrier, documentation packets built for reinspection AI, escalation artifacts (DOI complaint drafts, appraisal-clause handoff docs). The pre-submission *capture* half is newly contested (VaraFix, EstimateIQ, Revv's slice); the *fight* half has zero products and a $125/unit human proxy price (S04B-1-E8).

---

## 4. The wedge

**"Scan the estimate before it goes out; track every supplement until it's paid; log what each carrier actually pays."** A supplement defense desk for independent/small-MSO shops:

1. **Estimate/supplement ingest** — CCC ONE PDF upload (the path VaraFix proved shops accept, H20-E15) + EMS/BMS file parse; no CCC partnership required for v1.
2. **Missed-operation & short-pay scanner** — rules + LLM review against included-operations logic, OEM position statements, DEG corrections corpus (H20-E27), and Who Pays for What? billing norms (H20-E28); flags the $548–$1,200/estimate the entrants have benchmarked (H20-E15/E17). ADAS calibration lines cross-checked by VIN/build — complement, don't fight, Revv.
3. **Documentation packet generator** — per-line justification with photo checklist, OEM citation, invoice attach — formatted to survive AI desk review (Intelligent Reinspection reason codes, H20-E6) and the "photos and invoices" refusals shops report (S04B-1-E4).
4. **Supplement tracker (the state machine)** — per-claim per-round clock vs published norms (4.2-day average; carrier-specific medians from the product's own data); auto-generated status-request and escalation letters on breach; rental-clock and stall-occupancy cost surfaced per day of insurer delay.
5. **Carrier scoreboard & recovery ledger** — written vs approved by line, carrier, state; days-to-response by carrier; the ROI artifact for renewal and the seed of the data moat (a live, per-shop Who Pays for What?).
6. **Estimator copilot mode (S04B-3 fold-in)** — the same scanner + packet engine run pre-write as training wheels for the "zero estimating experience" hires (S04B-3-E1/E2), collapsing the $125/unit outsourced-writing market into software.

**Explicitly does NOT do:** initial estimates from photos (CCC's turf, H20-E20); negotiating with insurers *on behalf of the policyholder* (Texas UPPA line, H20-E25 — all artifacts are the shop's own invoice/documentation); appraisal-clause representation; DRP scorecard gaming; labor-time database authorship (cites DEG/OEM, doesn't invent times); total-loss valuation disputes.

**≤90 days by founder + AI agents? Yes, justified:** PDF/EMS parsing of standardized estimate formats is mature; the review layer is rules + LLM over a grindable research corpus (OEM position statements, P-pages logic, DEG archive, four years of public Who Pays results) that an agent team builds fast — VaraFix's veterans shipped the equivalent front half with no disclosed funding (H20-E16); the tracker is conventional CRUD + clocks; no PHI/BAA burden (H01's heaviest lift is absent — vehicle data, not health data). Real 90-day work: estimate-format parser robustness across CCC/Mitchell/Audatex PDFs, a 200-rule seed library for the top 20 missed operations, carrier-norm seed data (published response averages + crowdsourced), and packet templates per top-8 carriers.

---

## 5. Forcing function & why now

**Forcing function (money gate, contractual not statutory):** the shop is not paid — and the finished car sits on the lot — until each supplement round is approved ("it stays on your lot until the final bill is paid," H20-E8); insurer response windows set the shop's cash conversion cycle per claim (4.2–14 days/round, S04B-1-E5/E2); rental caps (30 days) put a hard consumer-facing clock on the fight (S04B-1 thread). No regulator compels purchase — this is grade-B versus H01's statutory appeal deadlines, but it recurs on every RO.

**Why now (2024–2026):**
- **The counterparty automated both ends first.** Initial estimates: photo channel <1%→26.4% of inspections (2016→2025), insurer staff halved to 18%, AI-STP at 7 of top-10 carriers (H20-E4/E1/E5), Progressive PEG sheets AI-flagged per its own staff (H20-E7). Audit: CCC Intelligent Reinspection (July 2024) AI-reviews shop estimates for insurers (H20-E6). Shops report the result as a 2025–26 squeeze: "town halls... which line items they're going to start cracking down on next" (H20-E8); "this year especially State Farm has gotten really bad" (S04B-1 thread).
- **Complexity keeps raising supplement stakes.** Calibration lines +31.4% in 2025 at $688 each (H20-E29); 51.5% of calibrations appear only on supplements (S04B-1-E7); supplement frequency rose YoY through 2025 (H20-E1).
- **The insurer side admits the bottleneck.** State Farm: 500 appraisers hired in two years, third-party appraiser reliance, "we haven't got that right yet" (H20-E14). None of the top-10 insurers graded above C+ by 1,100 shops (H20-E13).
- **The category just opened.** First AI entrant at this exact buyer launched 2026-08-25 at $349/mo (H20-E15) — demand and price point proven, window measured in months.

---

## 6. Distribution plan (solo-founder realistic)

**First 10 customers, by name:** (1) r/Autobody — 86,712 subscribers, verified operator voice (H20-E26); the "Statefarm Nightmare" and Progressive threads are literal buyer lists; sub bans blatant self-promo, so the motion is founder-as-operator content + free single-estimate scans. (2) State affiliate associations — SCRS's 38 affiliates / 6,000+ businesses (H20-E26): start with AASP-MA/NJ (Greco publications New England Automotive Report / Hammer & Dolly run Who Pays features, H20-E28) and WMABA. (3) Who Pays for What? audience — shops that fill in a quarterly billing survey are pre-qualified for a tool that operationalizes it. (4) 20 Groups / Collision Advice seminar attendees. (5) Paint jobbers' business-services reps (PPG/Axalta/Sherwin distributor councils) — the classic small-shop software channel. (6) DEG users (H20-E27) — shops already filing line-item disputes.

**Sales cycle estimate:** self-serve trial → paid in 1–4 weeks (VaraFix's free-3-reviews motion proves the pattern, H20-E15); association/jobber-mediated deals 1–3 months. **Price/packaging hypothesis:** $299/mo/location (scanner + packets) and $499/mo (adds tracker + carrier scoreboard), anchored by VaraFix $349 (H20-E15), Shop Sheet $125/unit (S04B-1-E8), Tekmetric $179–409 SMS comparables (S04B-2-E6). At 25–40 supplements/month the $499 tier prices below one outsourced supplement per week.

---

## 7. AI-structural advantage

The defense work is exactly what an agent-heavy team collapses: reading estimates against thousands of pages of OEM procedures/position statements, P-pages logic, and carrier behavior — then producing documentation packets and escalation letters per claim. Today that is a $50–110k estimator's overflow ("two jobs for the amount of sheets," S04B-1-E9), a $125/unit human service (S04B-1-E8), or forfeited. Incumbent economics resist following: CCC/Mitchell monetize carriers first (Estimate-STP, Intelligent Reinspection sold to insurers, H20-E5/E6) — shipping a shop-side "recover more from insurers" weapon attacks their anchor customers; the services (Shop Sheet, consultants) are per-unit human businesses whose margin the product deletes. The research corpus (OEM statements, DEG archive, survey norms) is the agent-grindable input; the per-carrier outcome data the product accumulates is the part a model call can't replicate.

---

## 8. Moat path

**Accumulates with usage:** (1) the **carrier scoreboard** — written-vs-approved and days-to-respond by carrier/line/state across shops: a live, evidence-grade Who Pays for What? that no single shop, and neither side's platform vendor, will publish (CCC is conflicted; CRASH Network's survey is quarterly and self-reported); (2) workflow lock-in — open supplements, clocks, and recovery history live in the tracker; (3) packet-outcome learning — which documentation survives which carrier's (AI) desk review; (4) association/jobber channel relationships. **Thin-wrapper honesty:** the scanner alone is one model call away — VaraFix ships it today, EstimateIQ shipped a rules version years ago, and CCC could bolt review onto Estimating IQ. A scanner-only product would fail the thin-wrapper gate; the tracker + carrier-outcome corpus is the defensible layer and must be built first-class, not as a roadmap promise. 12–24 months to data-moat critical mass, same as H01's.

---

## 9. Risks & unknowns (top 5)

1. **Same-wedge entrant velocity (VaraFix).** Industry-veteran team, live product, right price, two-day head start on this dossier. *Test:* run their trial + demo within 2 weeks; monitor releases/funding for 60 days; if they ship a supplement tracker or carrier analytics within 6 months, the differentiated wedge is gone — kill or partner.
2. **Recovery-delta reality.** Shops report refusals *despite* documentation ("photos and invoices documenting that it needs to be done," S04B-1-E4) — better packets may not move approvals at stonewalling carriers. *Test:* 10-shop pilot, matched carriers, measure median approved-$/RO and days-to-approval before/after packets; kill the defense claim (keep the capture claim) if delta <$150/RO or no cycle-time gain.
3. **Revv expands from calibrations to full supplement defense.** $20M, 200+ shops, adjacent data. *Test:* track Revv releases/job postings quarterly; if they announce general supplement review, reposition to tracker/scoreboard layer and integrate their calibration docs rather than compete.
4. **CCC platform friction.** PDF/EMS ingest lives at CCC's tolerance (Secure Share history: fees imposed, then dropped, H20-E21); a ToS change against third-party estimate parsing would raise switching cost. *Test:* legal read of CCC ONE license + Secure Share app terms pre-build; maintain Mitchell/Audatex parity and shop-owned-PDF framing (the shop's own work product).
5. **DRP drift shrinks the fight-side buyer pool.** Shops are returning to DRPs (H20-E11), and DRP scorecards *reward fewer supplements* (H20-E9) — the defense feature is a non-DRP feature. *Test:* instrument trial cohort DRP mix; if >70% of trialing shops are DRP-dominant, lead with capture/copilot (VaraFix's fight) instead — and expect a knife fight. Watch CRASH/FenderBender DRP trend annually.

*(6th, monitored:* insurer initial-estimate AI could eventually get accurate enough to shrink supplements — all current data runs the other way (H20-E1/E2/E29), but Estimating IQ-class tools narrowing the gap would erode capture value.)*

---

## 10. Scores

| # | Dimension | Weight | Score | Rationale (evidence) |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 5 | Per-claim, daily, 5+ carriers, 7+ independent 2025–26 shop voices, emotional (banned carriers, "nightmare"); trade press: "cruel and unusual punishment" (S04B-1-E1…E6, H20-E7/E8) |
| 2 | Budget proof | 15% | 4 | Salaries $50–110k, $125/unit services, live $349/mo SaaS price, $20M VC adjacent (S04B-3-E5, S04B-1-E8, H20-E15/E17); docked one: recovery-$ magnitudes partly vendor-claimed, no fine/penalty line |
| 3 | Competitive gap | 12% | 3 | Fight/tracker layer verifiably empty; but the capture half was contested the same week (VaraFix), EstimateIQ exists, Revv owns the calibration slice (§3) |
| 4 | Forcing function | 10% | 4 | Involuntary per-claim money gate + car-on-lot + rental clocks (H20-E8, S04B-1-E5); docked one: contractual/commercial, no statutory deadline analog |
| 5 | Founder+agents feasibility | 12% | 4 | PDF/EMS + rules/LLM + CRUD tracker in 90 days; no PHI; VaraFix proves small-team feasibility (H20-E15/E16); docked one for estimate-format breadth + OEM-data licensing |
| 6 | Distribution reachability | 10% | 4 | r/Autobody 86.7k verified, SCRS 6k businesses/38 affiliates, jobber channel, self-serve trial proven (H20-E26, E15); docked one: no-self-promo sub rules, regional association gatekeeping |
| 7 | AI-structural advantage | 8% | 4 | Collapses $125/unit writing + estimator overflow into software; CCC/Mitchell carrier-side revenue conflicts them out of the fight layer (§7) |
| 8 | Moat path | 8% | 3 | Carrier scoreboard + workflow accrue (§8); scanner is commodity; CCC owns the data rails |
| 9 | Expansion ceiling | 5% | 3 | ~30k shops × $4–6k/yr ≈ $120–180M wedge TAM; expansions (MSO tier, mechanical claims, parts disputes, appraisal-clause ecosystem) real but the vertical is 10x smaller than healthcare RCM |
| 10 | Durability | 5% | 3 | Complexity trend sustains supplements (H20-E1/E29); but CCC could ship completeness-AI to shops, and a both-sides platform can squeeze ingest (H20-E19/E21) |

**Weighted total: (75+60+36+40+48+40+32+24+15+15)/5 = 77.0 → 77/100 (strong band)** — conditional on building the *defense/tracker/scoreboard* wedge; a scanner-only me-too against VaraFix would score ~62 (gates 3/8/10 collapse).

**Hard gates:**
- **Budget proof: PASS** (salaried role + priced per-unit services + live in-category SaaS price).
- **Reachable buyer: PASS** (SMB owners, self-serve trial motion proven this month at this exact buyer).
- **Thin-wrapper: PASS conditionally** — scanner alone would FAIL; tracker + packet-outcome + carrier-data corpus is the required depth (§8).
- **Head-on collision: PASS, narrowly.** VaraFix is same-segment and currently shipping but overlaps only the pre-submission half and shows no funding (H20-E15/E16); Revv is well-funded but a different wedge (calibrations); CCC is conflicted out of the fight layer. Condition: do not lead with estimate review alone.
- **Platform hostage: PASS with note** — ingest is the shop's own estimate files (PDF/EMS), not an API grant; CCC tolerance improves UX but isn't load-bearing (H20-E21); multi-IP parity required.
- **Regulated practice: PASS with guardrails.** Auto-damage appraiser licenses exist in ~8 states (CT, DE, MA, NY, PA, SC, VT + RI; MA/NY reach shop estimators — H20-E23/E24): software assisting the shop's own licensed estimator practices nothing; the licensed human remains appraiser of record. The product must never negotiate on behalf of the *policyholder* (TX UPPA + 2024 TX Supreme Court, H20-E25) — all output is the shop's own invoice documentation. These same rules burden the gray-market remote-writing services, which helps the software. A "we write/negotiate for you" services pivot would re-trip this gate — documented as a standing constraint.
- **DRP-lock demand qualifier (Manager-assigned check): PASS with segmentation.** The market is not majority-DRP-locked: DRP is 46.7% of repairable-claim inspections — 53.3% of claims flow through photo/staff/IA channels where the fight is live (H20-E1/E4); the five-shop anchor thread is all non-DRP voices (S04B-1). DRP-locked shops are structurally *disincentivized* from fighting (scorecards punish supplements and reward low cost-of-repair, steering is the currency — H20-E9/E10) — they buy the *capture/copilot* half (write it complete and compliant the first time; VaraFix explicitly sells to DRP shops, H20-E16), not the defense half. Packaging must split along that line; the defense wedge's serviceable market is the non-DRP claim flow plus mixed shops' non-DRP work.

**Displacement sentence:** Current solution = a $50–110k estimator (or the owner at night) fighting each claim by phone/portal/email plus $125-per-supplement outsourced writers, with supplements approved at ~30% of written value, 4.2–14-day response loops stalling finished cars, and missed operations forfeited. New product = a supplement defense desk ($299–499/mo): pre-submission missed-op scan, reinspection-proof documentation packets, a per-supplement response-clock tracker, and a per-carrier recovery scoreboard. The customer switches because recovering even $200–400 per RO across 30–40 monthly ROs returns 15–50x the subscription — measured in the product's own ledger.

---

## 11. Verdict proposal

**STRONG (77).** The H01 shape holds on this market's own evidence: counterparty automated first (photo/AI initials at 26.4%, AI reinspection since 2024), per-claim money gate, human defense priced in public ($125/unit, $50–110k salaries), fresh multi-shop 2025–26 pain. It lands below PURSUE because the capture half was contested the same week (VaraFix, $349/mo, industry veterans), the forcing function is commercial not statutory, and the vertical is ~10x smaller than H01's. Wedge must lead with the unserved fight layer (tracker + packets + carrier scoreboard). Kill triggers: R1 (VaraFix ships tracker/analytics or announces funding), R2 pilot (<$150/RO median recovery delta). If Wave 3 concentrates capital, H01 remains the better pursue; H20 is a credible second theater or fast-follow.

---

## 12. Evidence ledger

New evidence: `outputs/evidence/dh20_collision_supplements.jsonl` — 30 records, H20-E1…E30, schema-valid, all accessed 2026-08-27. Fetch-blocked sources (RDN, BodyShop Business — Tollbit 403) disclosed in-record and routed via search-index capture or alternate outlets, per scout 04b access notes.

| ID | Claim (short) | Type |
|---|---|---|
| E1 | CCC 2026: supplement share up YoY each of Q1–Q3 2025; RO $4,818; photo 26.4%; DRP 46.7%; total loss 23.1% | report |
| E2 | CCC 2022: ~70% of DRP claims supplemented; 2–4-supp claims tripled; 4+ supp = >35% of cost | news |
| E3 | Mitchell: photo-estimate supplements >50% of original appraisal (52.9–67.4%) | news |
| E4 | Photo initials <1%→25.6% (2016→24); insurer staff estimates 40%→18% | news |
| E5 | CCC Estimate-STP: 15 insurers incl. 7 of top 10 (2023) | vendor-news |
| E6 | CCC Intelligent Reinspection (2024-07): AI review of shop estimates for insurers | vendor-news |
| E7 | Progressive PEG = AI photo estimates; "intransigence on supplements"; carriers banned (36-pt thread) | forum-post |
| E8 | Car stays on lot until final bill paid; SF Webex "write cheaper estimates"; line-item crackdown wave | forum-post |
| E9 | DRP scorecards punish supplements; low cost of repair = more cars; <800 = fewer assignments | forum-post |
| E10 | DRP contracts: supplement thresholds, insurer-set rates, KPI standing, removal risk | industry-blog |
| E11 | FenderBender 2026: insurer influence #2 concern; shops returning to DRP work; 80% in-house ADAS | news |
| E12 | Focus Advisors: independents 68.7% of locations; Big 5 4,019 = 13.3% (≈30.2k shops inferred) | report |
| E13 | 2026 Insurer Report Card: 1,100+ shops; no top-10 insurer above C+ | news |
| E14 | State Farm admits supplement delays; 500 appraisers hired; "haven't got that right yet" | news |
| E15 | VaraFix shipping: $349/mo, CCC PDF only, $548/estimate found, 83% approval claim | pricing-page |
| E16 | VaraFix team (veterans/carrier auditors), DRP+non-DRP positioning, no funding disclosed | news |
| E17 | Revv: $20M Series A, 200+ shops, calibration ID + OEM docs, $1,200/estimate claim | news |
| E18 | OEC EstimateIQ: rules-based missed-op analysis, "7X ROI," quote-priced | pricing-page |
| E19 | CCC 2025 shop AI roadmap: estimating/back-office agents; no supplement-defense product | news |
| E20 | CCC Estimating IQ (2021): initial-estimate pre-population only | vendor-news |
| E21 | CCC Secure Share: 50¢/workfile dev fee imposed then eliminated; third-party rail on CCC's terms | vendor-docs |
| E22 | Claimory marketing "Supplement Negotiation Playbook" (positioning only) | vendor-blog |
| E23 | Appraiser licenses: CT, DE, MA, NY, PA, SC, VT (+RI); MA 212 CMR reaches shop estimators | regulatory |
| E24 | NY: estimator license required to write shop estimates | regulatory |
| E25 | TX UPPA: no negotiating on behalf of insured; contractor dual-role ban (2024 TX Sup. Ct.) | regulatory |
| E26 | r/Autobody 86,712 subscribers (API-verified); SCRS 6,000+ businesses / 58,500 professionals | other |
| E27 | DEG: 1,000+ P-page corrections from shop inquiries in 2024; +11% utilization | industry-org |
| E28 | Who Pays for What?: measurable unbilled-procedure gaps; seatbelt-inspection pay 2x since 2016 | news |
| E29 | Enlyte 2026: calibration lines +31.4% in 2025, $688 avg when present | report |
| E30 | SECONDARY: 63%-of-repairs / $1,200–1,800 gap / $1,200–4,000 unsubmitted-supplement blogs — unverified magnitudes | vendor-blog |

Carried (scout-verified 2026-08-27): S04B-1-E1…E12 (five-shop SF thread, panel study, CCC calibration data, Shop Sheet pricing, estimator posting, VaraFix launch PR, coping evidence); S04B-3-E1…E6 (estimating capacity, gray-market writers, Caliber salaries); S04B-2-E2/E5/E6 (CCC ONE pricing/lock-in, front-office reality, Tekmetric comparables).
