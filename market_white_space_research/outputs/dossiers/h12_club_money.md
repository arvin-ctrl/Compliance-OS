# Opportunity Dossier — H12: Club & Academy Money Layer (dues AR, registration funds, fee transparency)

Validator: Wave-2 validator, H12 · Date: 2026-08-27 · Source hypothesis: H12 (Manager 1 promotion memo, rank 12) · Ground(s): 12 (founder arena), 08 (money friction), 04 (vertical SMB pattern), 10 (membership-org variant)

**Founder-domain note:** the founder operates a sports academy (Division 1 Academy) and sits inside the buyer community. Per program rules this was treated as a distribution asset only — every claim below was validated at the standard evidence bar, and two of the promoted hypothesis's headline claims were **downgraded** in this pass (see §1 and §3).

---

## 1. The pain, restated precisely

**Who hurts:** directors, registrars, and volunteer treasurers of competitive youth sports clubs (volleyball, soccer, basketball, hockey, baseball, swim), roughly 100–2,000 athletes and $100K–$3M annual revenue, US-wide; secondarily rec leagues and academies run by the same kind of volunteer/1-admin back office. Dues run $1,325–$2,313/season at the median by age band (Baseline 2026 dataset, H12-E5) up to $3,900–$5,900 at elite clubs (S12-2-E3), collected as deposit + 4–8 monthly installments.

**The workflow failure:** the club's season revenue arrives as hundreds of small consumer installments across card, ACH, Zelle, check, and cash. The platforms that take the online share (SportsEngine, TeamSnap, LeagueApps class) charge 3.25–5%+ plus ~$2 per installment, pay out on 2–7-day settlement, can freeze funds in underwriting/verification holds, and — per their own documentation — stop trying after at most three failed card attempts, with no card-account updater, no restructuring tooling, and until mid-2026 not even automated overdue reminders. The offline share is reconciled by a volunteer treasurer in spreadsheets ("he did everything by hand and handed me paper notes" — r/nonprofit treasurer, Mar 2025, H12-E23). What doesn't arrive gets chased by hand and then enforced socially: benching, work-off arrangements, non-payment registries, small-claims court (JVA playbook, S12-2-E2), up to a statewide cross-club debtor blacklist with $1,000 fines for using an unpaid player (Texas Amateur Hockey Association Outstanding Debt List, H12-E6).

**Frequency:** monthly installment due dates Sept–Mar; per-registration windows 2–4×/yr; escalation events several times per season; treasurer reconciliation weekly.

**Downgrade recorded (leak size).** The promoted headline — "10–12% of revenue never collected (JVA, verified)" — survives as a *verbatim quote* but not as an attributed statistic: re-fetch confirms the JVA article (revised 2026-07-06) cites **no study, no member data, no source** for the 10–12% figure (H12-E1). Corroboration found this pass brackets rather than confirms it: two payments vendors independently claim "5–10% of dues left unpaid" and "40+ hours per season collecting" (unattributed vendor claims, H12-E2/E3); a CPA firm's club example works out to a $12,000 shortfall on an 80-member club (H12-E4); and the best quantified dataset found — Baseline's 2026 report on 337 clubs / $85.7M of team fees, with disclosed adversarial re-derivation — shows clubs on a modern collection stack recover **96.3% of matured dues overall, 98.2% of online dollars, but only 83.6% of offline dollars**, with card-failure rates climbing from 0.6% on installment #1 to 4.5% by installment #9 (H12-E5). Honest synthesis: **the leak is real, concentrated in offline rails and the late-installment tail, and ranges ~2–4% for well-tooled clubs to ~16% for offline-heavy clubs; the JVA's 10–12% is a plausible blended figure for the legacy-stack majority, not a verified constant.**

**Strongest three artifacts (carried + new):**
1. SportsEngine BBB fund-hold complaint — "$5K … over $20K in accounts receivable … coaches and facilities to pay and are now behind on payments" (S12-1-E2, verified verbatim by Manager 1), on a 1.11/5 BBB profile; TeamSnap 1.1/5 across 692 Trustpilot reviews (S12-1-E1).
2. Baseline 2026 registration dataset: 96.3%/98.2%/83.6% collection splits and the 0.6%→4.5% installment-position failure curve — the money mechanics of the leak, quantified (H12-E5, new).
3. The enforcement infrastructure itself: JVA's manual collection playbook (benching, registries, small claims, "may not be worth the total cost, time and effort") and TAHA's cross-club Outstanding Debt List with player ineligibility and $1,000 fines (S12-2-E2 + H12-E6, new) — governing bodies institutionalizing manual AR because software doesn't do it.

## 2. Budget proof

Money already moving against this pain, per club per year (worked at a $200K-revenue club, ~110 athletes, ~7-installment plans):

| Line | Amount | Source |
|---|---|---|
| Revenue leakage (uncollected dues) | $7K–$24K/yr: JVA estimate $20–24K (unattributed); conservative re-derivation from Baseline splits — modern stack ~3.7% ≈ $7.4K; offline-heavy club 30–50% offline share at 83.6% ≈ $12–18K | H12-E1, H12-E5 |
| Platform + processing fees | ≈ $8.9K/yr on SportsEngine Premium: $749 subscription + 3.25% of $200K ($6.5K) + $2 × ~840 installments ($1.68K); Free tier runs 3.5% + $2. Worked vendor example: $100 in 3 installments costs $9.25 (9.25%) vs $5.25 paid in full | H12-E7, H12-E8 |
| Admin labor on collections | "40+ hours/season collecting" (two vendors, unattributed) at $20.09/hr youth-sport admin wage ≈ $800+/season — usually donated volunteer time | H12-E2/E3, S12-1-E6 |
| Failure remediation | Small claims $90–100+/filing (JVA); consumer collection agencies at 50/50 contingency (Rocket Receivables); chargebacks at $35/dispute passed to leagues | S12-2-E2, H12-E20, H12-E21 |
| Budgeted reserve for the leak | JVA advises a dedicated 3–5%-of-revenue uncollected-funds line item ($6–10K on $200K) | H12-E1 |
| Adjacent-industry price precedent | Health-club billing vendors have sold exactly this recovery layer for 40+ years (Club Systems: weekly resubmits, call center, text-to-pay Instapay links) — the collection layer is a proven paid category one vertical over | H12-E19 |

Total addressable spend per club: **$15K–$35K/yr of leak + fees + labor + reserve**, before counting the $1,016/child/yr (+46% since 2019) family-side inflation that makes delinquency structural (S12-2-E5, Aspen).

## 3. Competitive landscape

| Solution | Type | Segment served | Price / fee stack | Where it fails (evidenced) |
|---|---|---|---|---|
| **SportsEngine HQ** (now PlayMetrics/Genstar, since 2026-05-01) | product (payfac) | clubs/leagues, all sports | Free tier: 3.5% + $2/installment; Premium $69/mo ($749/yr): 3.25% + $2; ($300 minimum-processing fee if <$1,000/yr processed — reported by comparison sites, labeled secondary) | 1.11/5 BBB; fund-hold complaint stranding $5K+/$20K AR; payouts 2 business days (card) / 7 (eCheck); $2/installment penalizes payment plans (worked example: 9.25% on $100×3); installment options only shipped Jan 2025; no dunning/card-updater in docs (H12-E7/E8/E9/E13; S12-1-E2) |
| **TeamSnap** (PE-backed) | product | teams + clubs/leagues | Classic payments ≈ 5% total (PayPal 2.9%+30¢ + 2% TeamSnap); business tier custom; payouts 2-day rolling | 1.1/5 Trustpilot (692); failed registration installments retried max 3× then abandoned; invoice installments retried **zero** times — admin must manually reset or re-invoice; overdue email reminders only shipped Jul 2026; no card updater, no recovery workflows (H12-E10/E11/E12; S12-1-E1) |
| **LeagueApps** | product | competitive clubs/leagues | unpublished; user-reported ~5–5.9% effective per-transaction take; own blog: 41.6% of registrations carry a $1–5 pass-through fee | call-for-pricing opacity; per-transaction take on top of processing; no published AR/dunning tooling (H12-E14) |
| **PlayMetrics + Stack Sports + SportsEngine (Genstar rollup)** | product (consolidating) | soccer-led, now all sports + swim (TeamUnify/Motion) | PlayMetrics unpublished, custom-quoted | The category's modern leader merged with Stack (Jun 2025) then bought all of SportsEngine (May 2026) — 4 months into integrating three companies; PE rollup economics historically precede fee extraction (ground 04 pattern); club-level AR recovery not in shipped docs; Motion shipped basic installment options Jan 2025 (H12-E15/E16/E17) |
| **Jersey Watch** | product (budget) | rec leagues, small clubs | $29/mo (annual) + 3.5% + $1/transaction | budget tier; no dues-AR depth; positions on simplicity not recovery (H12-E18) |
| **TeamUnify / SportsEngine Motion** (now PlayMetrics) | product | swim clubs | club-side pass-throughs documented: 6% card surcharge, $25 late fees, $30 NSF fees imposed by clubs to cope | the coping fees ARE the evidence: clubs surcharge families 6% and levy manual NSF/late fees because the platform layer doesn't manage failure (H12-E17 club docs) |
| **Modern fee-light entrants: Baseline, Centro, Crossbar, Bound, Clubside, Vanta (UK), Finli** | products | clubs leaving legacy platforms | e.g. Centro $25/mo + Stripe 2.9%+30¢ + 2% platform fee; Crossbar subscription, "no per-registration fees" | crowded replatform race; all require full registration migration to capture the money layer; none found selling recovery on top of a club's existing stack (H12-E5, H12-E22) |
| **Stripe DIY** (payment links / Billing) | stack | tech-capable clubs | 2.9% + 30¢ + 0.7% Billing (includes ML Smart Retries, auto reminders, recovery automations) | machinery exists but nothing club-shaped: no rosters, sibling discounts, benching lists, season lifecycle, governing-body artifacts; someone must build and run it (H12-E24) |
| **Treasurer + spreadsheet + Zelle/check/cash** | DIY/human | the long tail (majority of rec + many competitive clubs) | volunteer time + $14–23/hr admin; 2.5% cash discounts offered to dodge card fees | 83.6% collection on offline dollars (vs 98.2% online); paper-notes handoffs; JVA/TAHA manual enforcement playbook; embezzlement exposure (H12-E5, H12-E23, S12-2-E3) |
| **Collection agencies / small claims** | service | aged debt | 50/50 contingency (Rocket Receivables); $90–100+/filing | relationship-destroying, uneconomic at $300–800 balances; JVA itself says often "not worth the total cost, time and effort" (S12-2-E2, H12-E20) |
| **Do nothing (reserve + bench + write off)** | default | most clubs | 3–5% revenue reserve (JVA) | the incumbent to beat: codified by the association itself (H12-E1) |

**Close-competitor deep-read (velocity/funding/focus):** The **Genstar rollup** (PlayMetrics ← Stack Sports Jun-2025 ← SportsEngine May-2026, incl. HQ/Motion/Tourney/Play/AES; USA Swimming partnership through 2030) is now the category's center of gravity — well-capitalized, governing-body-connected, and mid-integration. **TeamSnap** shipped real payments velocity in 18 months: fully customizable payment plans (Apr 16, 2025), reimagined invoicing + ACH + automated overdue reminders at days 1/7/14/30 + up to 24 installments (TeamSnap ONE, Jul 7, 2026) — but its own help docs still show 0–3 retry ceilings, manual plan resets, and no card updater or recovery workflow (H12-E10/E12/E13). **Baseline** is the sharpest new money-layer thinker (its 2026 report is the best data in the category) but sells a full replatform. **Verdict on the claimed gap:** "incumbents ship no plan tooling" is **stale** — both majors shipped plans in 2025 and reminders in 2026. What remains demonstrably unshipped anywhere: card-account-updater/dunning-grade failed-payment recovery, delinquent-balance restructuring, offline-dollar reconciliation, and season-end AR/writeoff governance — i.e., the recovery layer, not the plan layer.

## 4. The wedge

Three candidate wedges were evaluated per the promotion mandate:

- **(a) Full club platform (registration + money):** KILLED — head-on with the Genstar rollup, TeamSnap, and a dense modern-entrant field (Baseline/Centro/Crossbar/Bound/Clubside/Vanta) all racing the same replatform sale. Fails the head-on hard gate.
- **(b) Embedded payments/payfac for clubs:** deferred — competing on processing spread alone is a capital-and-compliance game (underwriting, fraud, chargebacks) with no workflow moat at entry; it is the season-2 expansion, not the wedge.
- **(c) Dues-AR recovery layer that lands WITHOUT replatforming:** SUPPORTED — this is where the evidence points: the leak concentrates in offline rails and the installment tail (H12-E5); incumbents' own docs show the recovery hole (H12-E10); the club can adopt it mid-season without touching registration; the health-club industry proves the layer is a durable paid category (H12-E19).

**The wedge — "the club's AR desk" (first-party, no custody):**
1. **AR intake:** import roster + balances (CSV exports every incumbent already provides — TeamSnap export wizard/financial exports verified — or a spreadsheet) into a live family-level delinquency ledger.
2. **Club-branded payment links** (card/ACH) for past-due balances via **Stripe Connect — funds settle directly to the club's own connected account; we never hold funds**.
3. **Restructuring engine:** convert delinquent balances into card-on-file installment plans (deposit + N) riding Stripe Billing's Smart Retries, with reminder cadence (1/7/14/30), late fees, and hardship rescheduling per the club's written policy.
4. **Offline reconciliation:** log Zelle/check/cash against the same ledger — the 83.6%-collection rail gets the same visibility as cards.
5. **Enforcement artifacts:** director's at-risk list, eligibility/benching report, season-end writeoff + 3–5% reserve report (JVA-framing), TAHA/registry-compatible statements.
6. **Weekly director digest:** recovered $, at-risk $, aging, forecast.

Explicitly NOT: registration, scheduling, websites, team comms; NOT a collection agency (all outreach in the club's name from the club's account — first-party); NO fund custody, NO wallets/team accounts in v1.

**≤90 days by founder + agents? Yes.** The heavy machinery (retries, reminders, card networks, MTL compliance) is Stripe's; the build is CSV ingestion + a family/balance data model + Stripe Connect standard onboarding + Billing plan orchestration + messaging + three reports. No incumbent API dependency in v1 (CSV path). The founder's own academy and 2–3 network clubs are the live test bed in week 1.

## 5. Forcing function & why now

- **Forcing function: money movement, honest grade WEAK-MODERATE.** Every installment date is a self-enforcing money event and missed collections cascade into the club's own payables (verified BBB artifact: club "behind on payments" to coaches and facilities). No regulator, no statutory deadline. This remains the hypothesis's structural ceiling versus H01–H05-class forcing.
- **Why now (validated 2025–26):** (1) **The category consolidated 4 months ago** — Genstar's PlayMetrics+Stack+SportsEngine rollup (May 1, 2026) puts the legacy installed base into exactly the PE-integration churn (ground 04's documented playbook: fee extraction, support decay, migration anxiety) that historically opens defection windows — and the defection race is for the *replatform*; nobody is harvesting the money layer in place. (2) **Family cost inflation (+46% since 2019, $1,016/child average)** makes delinquency structural (Aspen). (3) **Stripe-class rails now include the entire recovery machinery** (Smart Retries ML, reminders, recovery automations at 0.7%) that incumbents' payfac stacks never shipped — the build cost of this product collapsed. (4) Incumbents began shipping the *plan* layer (2025–26) but not the *recovery* layer, confirming demand while leaving the outcome unowned.

## 6. Distribution plan (solo-founder realistic)

**First 10 customers, by name of channel:**
1. The founder's own academy (Division 1 Academy) + its club-director peer network — 3–5 pilots by direct ask (Manager 1: "fastest validation loop in the program").
2. **JVA** — 1,700-team national championship scale; education channels (Club Direction LIVE, Align Volleyball Summit, webinars) that demonstrably sell vendor solutions (the Aug 26, 2026 chargeback article is co-branded with ViCoverage/Vertical Insure — the channel is open and monetizable, H12-E21); the JVA's own uncollected-payments guidance is the product's sales deck.
3. **USAV Regional Volleyball Associations** (40 RVAs, 400K+ members) and **AAU district club communities**; **US Club Soccer** ("thousands of clubs, 800K+ participants") director programs for the soccer beachhead.
4. State governing bodies with institutionalized debt pain (TAHA-class ODL administrators) — warm intro path to hockey associations.
5. r/nonprofit + treasurer communities where volunteer treasurers ask for exactly this (H12-E23).

**Sales motion:** free **"AR audit"** — club sends its aging export, product returns recoverable-dollar analysis in 24h; convert to paid recovery pilot. Sales cycle estimate: 2–6 weeks (club director + treasurer, no procurement). **Pricing hypothesis:** $99–$249/mo per club (anchored between Jersey Watch $29 and Upper Hand $79–199, far under SportsEngine Premium + fee stack) + optional 10–15% success fee on recovered aged balances (vs 50% agencies, 25–30% chargeback-recovery comparables); ACV $1.5K–$4K against a $7K–$24K leak.

## 7. AI-structural advantage

The recovered dollar requires judgment work software hasn't done: reading a family's payment history, drafting the firm-but-relationship-preserving message in the club's voice, negotiating a restructured plan, knowing when to route to the director versus auto-retry — today this is the treasurer's evenings (the same emotional labor evidenced horizontally in S08-4: "the part that used to kill me was rewriting the same chase emails"). Agents do the chase-with-context at zero marginal cost, per family, in both English and the club's policy. Incumbents' economics resist copying: SportsEngine/LeagueApps monetize the *fee stack itself* (3.25–5% + $2/installment is their revenue line) — a recovery layer that moves families onto cheaper rails and fewer failed transactions cannibalizes them; the Genstar rollup is mid-integration of three companies; TeamSnap's model is seat/subscription breadth, not collections outcomes. A success-fee-on-recovery model is structurally available to us and structurally awkward for every incumbent.

## 8. Moat path

Accumulates with usage: (1) family-level payment-behavior data across seasons and clubs (who pays, when, on what cadence — the underwriting asset for later embedded finance); (2) the club-policy library (late fees, hardship, benching thresholds by sport/governing body); (3) card-on-file restructured plans — switching away means re-collecting payment credentials from delinquent families; (4) governing-body artifacts (ODL-compatible reporting, reserve reports) that make the product the club's financial system of record; (5) season-2 expansion into registration-linked billing converts the AR layer into the payments layer at ~2.9%+30¢+1% vs incumbents' 3.25–3.5%+$2. **Honest thin-wrapper assessment:** v1 is a workflow wrapper on Stripe Billing plus club-shaped data; the durable asset is the data + policy + credential accumulation, not the retry engine. Thin-wrapper risk is real for the first two quarters and is listed as a risk with a test below. Not a hard-gate failure: the club-specific workflow (rosters, benching, offline reconciliation, governance reports) is genuinely absent from both Stripe and incumbents.

## 9. Risks & unknowns (top 5, each with its resolving test)

1. **The leak may be smaller than promoted** (JVA 10–12% is unattributed; modern-stack clubs already collect 96–98%). *Test:* AR audits on 10 clubs from the founder network in 30 days — measure actual aged-AR books. **Kill if median recoverable AR < $5K/club.**
2. **Hardship, not process, may dominate delinquency** — software cannot collect from families who are broke; benching is the real enforcement (Manager 1's explicit falsifier). *Test:* in the first 3 pilots, classify every delinquent dollar (process failure: dead card/no reminder/offline invisibility vs hardship) and measure recovery rate on the process share. Baseline's 98.2%-online vs 83.6%-offline split argues process dominates. **Kill if <30% of aged AR is process-recoverable.**
3. **Incumbent extension** — TeamSnap added overdue reminders (Jul 2026); the Genstar rollup or TeamSnap could ship retries/card-updater natively and close the gap. *Test:* quarterly release monitoring (launchnotes feeds); the wedge survives while card-updater + restructuring + success-pricing remain unshipped. **Mitigation:** land the multi-platform + offline share incumbents structurally can't see; expand to registration billing within 12 months.
4. **Collections-regulatory boundary** — chasing in our own name, or taking assignment of defaulted debts, can make the vendor a "debt collector" under FDCPA/state collection-agency licensing; success-fee framing can look like contingency collection in some states. *Test:* legal memo pre-launch; structure strictly as first-party tooling (club's name, club's Stripe account, club controls policy); confirm success-fee lawfulness per state or fall back to flat SaaS. **Also:** card-network recurring/card-on-file mandates compliance via Stripe Billing defaults.
5. **Seasonality + small ACV churn** — clubs may buy Sept–Mar and lapse. *Test:* measure off-season retention in year 1; mitigate by season-2 registration-payments expansion (year-round rails) and academy segment (year-round billing). **Kill signal:** logo churn >40% at first off-season with no expansion revenue.

Also logged: chargeback exposure when chasing benched families ($35/dispute passed to clubs; 60-day rulings; registration-protection insurance already sold into this exact flow by Vertical Insure via JVA — an adjacency, not a blocker).

## 10. Scores

| # | Dimension | Weight | Score | Note |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 4 | monthly installment cycles + verified operator anger (1.1★/1.11★, fund-hold cash wounds); short of 5 — pain peaks seasonally |
| 2 | Budget proof | 15% | 4 | leak $7–24K + fees ~$9K + reserve 3–5% + agencies at 50% + gym-vertical precedent; headline % downgraded to estimate |
| 3 | Competitive gap | 12% | 3 | recovery layer demonstrably unshipped anywhere; but plan+reminder layers shipped 2025–26 and modern entrants shrink the leak at source |
| 4 | Forcing function | 10% | 2 | money movement only; no regulator; discretionary purchase |
| 5 | Founder+agents feasibility | 12% | 5 | CSV + Stripe Connect/Billing; no incumbent dependency; live test bed in founder's academy |
| 6 | Distribution reachability | 10% | 4 | founder-domain + named, provably monetizable association channels (JVA/RVAs/AAU); B2B-lite cycle |
| 7 | AI-structural advantage | 8% | 3 | agentic chase-with-judgment at zero marginal cost; but core dunning is deterministic/commoditized |
| 8 | Moat path | 8% | 3 | payment-behavior data + card-on-file plans + policy library accumulate; v1 admits thin-wrapper exposure |
| 9 | Expansion ceiling | 5% | 4 | AR → registration billing → club money OS across $40B family spend |
| 10 | Durability | 5% | 2 | incumbents could ship dunning; Stripe-based entrants numerous; survives via multi-platform + offline coverage |
| | **Weighted total** | | **71/100** | STRONG band (70–79: red team decides) |

**Hard gates:** No-budget-proof — PASS (leak + fees + reserves + services already paid). Unreachable buyer — PASS (club directors, founder-domain). Thin-wrapper — PASS WITH FLAG (workflow/data depth beyond one model call, but v1 rides Stripe Billing; see §8/risk). Head-on collision — PASS **only for wedge (c)**; the full-platform variant fails this gate and is killed in §4. Platform hostage — PASS (CSV + club's own Stripe account; no incumbent API dependency). Regulated practice — PASS WITH FLAG (first-party structure avoids FDCPA collection-agency status; money transmission avoided by design: Stripe Payments Company holds the MTLs, funds settle club-direct, no custody features in v1–v2; any future wallet/team-account feature triggers licensed-partner requirements — Stripe Treasury/BaaS — and is explicitly out of wedge scope).

**Displacement sentence:** Current solution = volunteer treasurer + platform reminder emails + spreadsheets/Zelle + benching/registries + occasional 50%-contingency agencies, leaking ~$7K–$24K/yr per $200K club while paying ~$9K/yr in platform + processing fees (3.25–3.5% + $2/installment). New product = a first-party dues-AR recovery desk (imports any roster, payment links + restructured card-on-file plans + retries + offline reconciliation + benching artifacts) on the club's own Stripe account at $99–249/mo (+optional 10–15% of recovered aged balances). The customer switches because recovering even half the conservative leak returns 2–5× the product's price in season one, with no replatforming.

## 11. Verdict proposal

**STRONG (71) — advance to red team with the wedge narrowed.** The money layer is real, evidenced, and founder-reachable, but two promoted claims were downgraded (10–12% now an unattributed association estimate bracketed at 2–16% by rail; "no plan tooling" stale — both majors shipped plans 2025–26). What remains genuinely unowned is failed-payment *recovery* + offline reconciliation + AR governance, deliverable in 90 days on Stripe rails without replatforming, into a consolidation-shocked installed base (Genstar's May-2026 SportsEngine takeover), through the founder's own community. Weak forcing function and incumbent-extension durability cap it below PURSUE. Kill criteria are pre-registered in §9 (#1, #2, #5).

## 12. Evidence ledger

Full ledger: `outputs/evidence/dh12_club_money.jsonl` (claim IDs H12-E1…E26; access date 2026-08-27). Carried-forward artifacts cited by scout ID (S12-x, S10-3, S08-4, S04-x) live in `outputs/evidence/s12_founder_arena.jsonl` etc. and were spot-verified by Manager 1.

| ID | Claim (short) | Source | Status |
|---|---|---|---|
| H12-E1 | JVA 10–12% verbatim; **no attribution/source cited**; rev. 2026-07-06; 3–5% reserve advice | jvavolleyball.org | verified verbatim; statistic downgraded to unattributed estimate |
| H12-E2 | Snap! Mobile: checks = 4.7× uncollected, 5–10× time, "$10,000s"; no methodology | snapraise.com | vendor claim, labeled |
| H12-E3 | Vanta Sports: "40+ hours/season collecting; 5–10% unpaid"; 95% autopilot | vantasports.ai | vendor claim, labeled |
| H12-E4 | CPA example: 80-member club, $150 avg/unpaid → $12,000 shortfall; 4 leak mechanisms | jsmorlu.com | independent CPA blog |
| H12-E5 | Baseline 2026: 337 clubs/$85.7M; 96.3% overall, 98.2% online vs 83.6% offline; 0.6%→4.5% failure by installment #9; median fees $1,325–2,313; 21.4% pay-in-full configs | baselinepro.com | vendor dataset, disclosed adversarial methodology; strongest quantified source |
| H12-E6 | TAHA Outstanding Debt List: cross-club ineligibility registry; $1,000 fines | tahahockey.org | governing-body primary |
| H12-E7 | SportsEngine current tiers: Free 3.5%+$2; Premium $69/mo (=$749/yr) 3.25%+$2 | discover.sportsengineplay.com | vendor primary, fetched |
| H12-E8 | SE management-fee formula + worked example: $100×3 installments = $9.25 (9.25%) | help.sportsengine.com | vendor primary |
| H12-E9 | SE payouts: card 2 business days; eCheck 7; failure/hold conditions | help.sportsengine.com | vendor primary |
| H12-E10 | TeamSnap: registration installments ≤3 retries then stop; invoices 0 retries; manual admin reset; no dunning/card updater in docs | helpme.teamsnap.com | vendor primary |
| H12-E11 | TeamSnap classic ≈5% (2.9%+30¢+2%); integrated payouts 2-day rolling | helpme.teamsnap.com | search-capture of help articles; medium confidence |
| H12-E12 | TeamSnap Apr 16, 2025: fully customizable payment plans (no recovery features) | teamsnap.launchnotes.io | vendor primary |
| H12-E13 | TeamSnap ONE Jul 7, 2026: invoicing, ACH, auto overdue reminders d1/7/14/30, 24 installments; no retries/card-updater | teamsnapone.launchnotes.io | vendor primary |
| H12-E14 | LeagueApps: unpublished pricing; ~5–5.9% user-reported take; own blog: 41.6% registrations carry $1–5 fee | leagueapps.com + comparison sites | mixed; take-rate secondary |
| H12-E15 | PlayMetrics acquired ALL SportsEngine assets from Versant, completed 2026-05-01 | home.playmetrics.com | vendor primary |
| H12-E16 | PlayMetrics + Stack Sports merged under Genstar, announced 2025-06-11 | businesswire.com | primary release |
| H12-E17 | Swim-club pass-through coping fees: 6% card surcharge, $25 late, $30 NSF; Motion installment options shipped Jan 2025 | gomotionapp.com club docs; help.sportsengine.com | club-imposed fees, labeled |
| H12-E18 | Jersey Watch: $29/mo annual + 3.5%+$1 | jerseywatch.com | search-capture; medium confidence |
| H12-E19 | Club Systems (gyms, 40+ yrs): collections layer — weekly resubmits, live call center, Instapay texts, "no cost to your club" | healthclubsystems.com | adjacent-vertical precedent |
| H12-E20 | Rocket Receivables: 50/50 recovery split (carried S08-4-E5) | rocketreceivables.com | carried forward |
| H12-E21 | Chargebacks: $35 fee passed to leagues, 60-day rulings (Sports Connect); JVA chargeback guidance co-branded ViCoverage/Vertical Insure 2026-08-26 | sportsconnect.com; jvavolleyball.org | search-capture + fetched |
| H12-E22 | Centro: $25/mo + Stripe 2.9%+30¢ + 2% platform fee; Crossbar "no per-registration fees" | withcentro.com; crossbar.org | vendor primaries/marketing |
| H12-E23 | r/nonprofit treasurer 2025-03-14 (1jb70fx): inherited "paper notes," wants cheap software, asks about Venmo | reddit via Arctic Shift | operator voice, verified archive |
| H12-E24 | Stripe Billing 0.7% incl. Smart Retries (ML), auto reminders, recovery automations | stripe.com/billing/pricing | vendor primary |
| H12-E25 | Money transmission: Stripe Payments Company is the licensed money transmitter; control-of-funds is the licensing trigger; platform avoids MTL by never taking custody | stripe.com docs/resources | vendor primary + legal-adjacent |
| H12-E26 | Scale anchors: USAV 40 RVAs/400K+ members; US Club Soccer "thousands of clubs"/800K+ participants; JVA championship 1,700 teams | usavolleyball.org; usclubsoccer.org; jvavolleyball.org | search-capture; sizing anchors only |
