# Opportunity Dossier — Denial & Underpayment Defense for Small Practices ("RCM Defense Desk")

Validator: Wave-2 validator, H01 · Date: 2026-08-27 · Source hypothesis: H01 (Manager 1 promotion memo, Rank 1 ★TOP-5) · Ground(s): 05 (backoffice_pros), 08 (money_friction), 03 (human_middleware_jobs)

All new evidence: `outputs/evidence/dh01_denial_defense.jsonl` (H01-E1…E25). Carried evidence cited by scout claim ID (S05-2-*, S08-2-*, S08-3-*, S03-1-*, S03-2-*), all Manager-1-verified or re-verified here.

---

## 1. The pain, restated precisely

**Who hurts:** (a) 1–12-provider independent practices — specialty (derm, GI, ophtho, cardio), primary care, and behavioral health — where 1–2 humans carry posting + denials + appeals + patient calls; (b) solo/group behavioral clinicians (SimplePractice-class: 250k+ practitioners, 58.8% of sessions insurance-based, H01-E21); (c) 1–50-person third-party billing companies (~2,000 firms nationwide, H01-E20) doing the same work across many clients. US-wide; 47.4% of physicians still practice in groups of ≤10 (AMA 2024, H01-E19).

**The workflow failure:** Payers now deny, auto-downcode, and silently underpay at machine speed; the defense side works each item by hand — portal archaeology (Availity + payer portal + phone queue), CARC/RARC spreadsheets, resubmission loops, reconsiderations, appeals — against hard per-claim deadlines (UHC 65 days to appeal; MA plans 60; timely filing often 90–180 days from DOS, H01-E17). Scrubbers and EHR worklists "aren't catching half of this" (S08-2-E1); ~half of providers still review claims manually (Experian, S08-2-E6). What isn't worked in time is legally forfeited: 35–60% of denials are never resubmitted (AHIMA via H01-E18) even though ~70% of appealed denials overturn (Premier, S05-2-E5).

**Frequency:** Daily, per-claim. ~15% initial denial rate (Premier S05-2-E5; AHA: MA ~15.7%, commercial ~13.9%, H01-E18); biller quotas of 40+ denials/day (S08-2-E2); "10–20 denials per 20k check" (S08-2-E3). The 2026 payer-edit wave added batch downcoding on top: one Chicago psychiatric practice had **2,400 claims reduced in July 2026 alone**; a pediatrician saw ~40% of higher-level sick visits downcoded (WBEZ, H01-E1).

**Strongest three artifacts:**
1. **WBEZ 2026-08-26 (new, H01-E1):** BCBSIL blanket downcoding live 2026-07-01; 2,400 reduced claims at one small psychiatric practice in one month; ISMS survey: 72% of practices experienced automatic downcoding; the Illinois ban passed but doesn't bite until **2028** — a legislated 18-month window in which defense is the only option.
2. **r/CodingandBilling "technical denials" thread (carried, S08-2-E1, verified via Arctic Shift):** "denials for stuff that used to sail through… like they're using some new AI bot to auto-reject… Our current scrubbers aren't catching half of this, and everything is just sitting in the 60+ day AR pile."
3. **Premier national survey (carried, S05-2-E5, verified):** $43.84→$57.23 per-claim rework cost, ~15% denial rate, ~70% of denials overturned when worked = the pain is pure, recoverable rework.

---

## 2. Budget proof

Money already moves against this pain through four channels (each sourced):

| Budget line | Amount | Source |
|---|---|---|
| Outsourced billing (denial work bundled) | 4–10% of collections; 24.5% of firms charge 6–7%; per-claim $3–10 | H01-E10 (Tebra survey data); S08-2-E5 (practitioner-quoted 4–7%) |
| In-house denials headcount | Denials Specialist $37,500–$50,500 salary ("Generating appeals and online reconsiderations") — re-verified 2026-08-27 | H01-E22; insurance follow-up reps $24–31/hr (Catholic Health, S03-2-E1); 1,177 open follow-up postings (S03-2-E3) |
| Contingency recovery services | 20–35% of recovered dollars, no upfront | H01-E16 |
| Rework cost / leakage absorbed | $25–$181 per reworked claim (AHIMA); $57.23/claim hospital benchmark; underpayments ≈ 7–11% of claims ≈ 1–3% of net revenue (vendor-estimated) | H01-E18, S05-2-E5, H01-E15 |

**Per-customer arithmetic (labeled inference from the verified figures above):**
- **3-provider specialty practice, ~$1.5M annual collections.** Outsourced path: 5–8% = **$75–120k/yr**. In-house path: 1 biller + part of a second ≈ **$50–90k/yr** loaded. Denial exposure: ~13,000 claims/yr × ~13% denied ≈ 1,700 denials; at $25–57 rework each ≈ **$43–97k/yr of labor equivalent**, of which 35–60% is currently just written off. Underpayments at 1–3% of net revenue ≈ **$15–45k/yr silently lost**. A defense tool at $6k/yr clears its cost by recovering ~2–5% of the write-off/underpayment pool.
- **Solo behavioral practice, ~$150k revenue, ~59% insurance-based (H01-E21):** BCBS-class downcoding shaves $20–40/session; at 25 insurance sessions/wk this is **$12–25k/yr at risk** — versus a $99–199/mo tool.
- **Micro billing company (10–40 practice clients):** revenue is 4–7% of each client's collections; denial rework is its largest labor line (staff quotas 40+/day, S08-2-E2). Tooling budget exists today: threads name moving denial tracking off spreadsheets into dedicated tools (S08-2-E1).

---

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| Waystar (+ AltitudeAI/AltitudeCreate gen-AI appeals) | Product (clearinghouse/RCM suite) | Mid-market → enterprise; health systems | ~$100–300/provider/mo custom + $2–10k implementation, multi-year (competitor-reported, H01-E3) | Sales-quoted, implementation-heavy, "best for organizations with high claim volume and dedicated billing staff" (H01-E3). AI appeals shipped Jan 2025 and accelerating (H01-E4) — but sold into existing enterprise accounts, not $300/mo self-serve |
| AKASA / Adonis (AI-RCM startups) | Product (AI RCM) | Health systems, large groups (Mount Sinai, AdventHealth, Cleveland Clinic) | Custom enterprise | $205M / $95M+ raised, explicitly enterprise logos and 650-hospital deployments (H01-E5, E6); no 1–12-provider product or price point |
| Availity Essentials (+ payer portals) | Product (free portal) — the incumbent *surface* | Everyone incl. small practices | Free | It IS the manual labor: "not very helpful due to recons and appeal in progress status" (S08-2-E1 thread); bot access eliminated (H01-E7); no appeals API (H01-E8) |
| Rivet / MD Clarity (underpayment & contract tools) | Product | Mid-size groups & provider orgs (51–200-employee reviewers) | Rivet from $6,000/yr; MD Clarity demo-gated (H01-E13, E14) | Price floor and contract-loading burden sit above solo/1–12 practices; review-noted data-accuracy and workflow gaps (H01-E13) |
| Muni Health | Product (new entrant, 2025–26) | **2–10-provider specialty practices** (same segment) | $20/appeal, first 3 free, no subscription (H01-E11) | Per-letter appeal economics: no ERA ingestion, no deadline state machine, no underpayment detection; at downcode-wave volume (2,400 claims/mo, H01-E1) $20/appeal = $48k/mo — wrong shape for batch defense. No disclosed funding |
| Aegis (YC S25) / ClaimCure | Product (new entrants) | Hospitals + billing teams / small practices | Undisclosed | Seed-stage; Aegis aims at hospitals/billing groups with EHR integrations and portal-bot submission (H01-E12) — the portal-automation approach Availity has contractually banned (H01-E7) is a compliance overhang for them |
| Outsourced billing / RCM firms (~2,000 cos.) | Service | All small practices | 4–10% of collections (H01-E10) | Human labor at % of revenue; threads show the outsourcers themselves drowning (40+/day quotas, S08-2-E2) — they are also prospective *customers* |
| Contingency underpayment recovery firms | Service | Mostly hospitals/large groups | 20–35% of recovered (H01-E16) | Doesn't reach small practices; engagement-shaped, not continuous |
| In-house denials specialist / biller | Internal hire | Practices that can afford it | $37.5–50.5k salary (H01-E22) | Can't absorb 2026 volumes: "I work all the time, and get half the work done that I used to" (S05-2-E4); "job should realistically be 3–4 people" (S08-2-E3) |
| EHR/PM native worklists (Tebra, SimplePractice, eCW) | Product feature | 1–12-provider tier | Bundled | Basic claim tracking; SimplePractice's own report names ongoing "struggles with… claim denials" among its 250k users (H01-E21); no appeal drafting, no deadline machine, no variance detection |
| Excel CARC/RARC trackers + portal archaeology | Stack (status quo) | The evidenced majority | Staff time | "Spreadsheets couldn't keep up with the volume" (S08-2-E1); ~half of providers still review claims manually (S08-2-E6) |
| Do nothing (write off) | DIY default | Everyone at the margin | 35–60% of denials never resubmitted (H01-E18) | ~70% of appealed denials overturn (S05-2-E5) — the default forfeits recoverable revenue at appeal deadlines |
| Patient-side appeal AI (Claimable, Counterforce, Fight Health Insurance) | Product (adjacent) | Patients, not practices | Low/free | Different buyer and claim types; validates LLM appeal efficacy but no provider workflow |

**Deep-verified closest three:**
- **Waystar** — shipping velocity high: AltitudeCreate launched 2025-01-13; by Sep 2025 "hundreds of appeal packages simultaneously, >90% faster (38 hrs→2), early adopters overturning 40% more denials" (H01-E4). Public company, enterprise GTM, multi-year contracts, implementation fees (H01-E3). Capability exists; the 1–12-provider tier is a GTM hole, not a technology hole — an important honesty point.
- **Muni Health** — the same buyer and job, launched into 2–10-provider specialty practices with $20/appeal transactional pricing and AI payer calls (H01-E11); active content velocity through 2026 (payer-deadline SEO library). No funding announcements found (searched Crunchbase/Fierce trackers, 2026-08-27). Muni proves demand and self-serve viability at this tier; it does not own ERA-level workflow, underpayments, or batch downcode defense.
- **Rivet** — nearest underpayment product: $6,000/yr floor, 9 total public reviews, mid-size reviewer base, complaints on claim filtering and plan-data accuracy (H01-E13). Not moving down-market visibly.

**Which segment is unserved (proved):** practices too small for Waystar/Rivet economics and too complex for $20/letter — plus micro billing companies who need multi-client denial ops. Nobody at any tier ships **batch downcode/underpayment defense keyed off the practice's own 835 history** — the 2026-specific pain in H01-E1/S05-2-E1.

---

## 4. The wedge

**"Upload your ERAs; see the money payers shaved; fight it before the clock runs out."** An ERA-native defense desk for 1–12-provider practices and micro billing companies:

1. **835/ERA + denial ingestion** — nightly file pull from the clearinghouses this tier already uses (Claim.MD $30–120/mo unlimited-ERA tier, H01-E9/E25; Office Ally; Availity remit files) or drag-and-drop. No EHR integration in v1.
2. **Denial workdesk** — CARC/RARC × payer × dollars × **appeal-deadline countdown** (per-payer rules: UHC 65d, Aetna/BCBS/Cigna 180d, MA 60d — H01-E17), replacing the Excel tracker that "couldn't keep up."
3. **Downcode & underpayment detector** — compares each remit's allowed amount against the practice's own 835 history and optional uploaded fee schedules; flags algorithmic downcodes (the 99214→99213 wave) and variance patterns like Anthem's unexplained $178 vs $418 on identical claims (S05-2-E2).
4. **Agent-drafted appeal/reconsideration packets** — payer-specific letter + form + records checklist, drafted from the denial code, remit data, and payer policy citations; **staff reviews and submits** (portal upload/fax/mail) — deliberately no portal bots (see §9 R2).
5. **Batch reconsideration machinery** — one workflow to contest 200 downcoded claims at once with shared evidence (the 2,400-claims-in-July case, H01-E1); this is the feature the $20/letter and enterprise players both lack at this tier.
6. **Recovery ledger** — dollars recovered per payer/action; the ROI artifact that drives renewal and referral.

**Explicitly does NOT do:** claim scrubbing/first-pass submission (clearinghouse's job), EHR write-back, prior auth (H03), credentialing (H02), patient-side appeals, autonomous portal submission, coding advice positioned as replacing certified coders (drafts are provider-reviewed).

**≤90 days by founder + AI agents? Yes, justified:** 835 parsing is a stable open standard with mature open-source parsers; the deadline state machine and workdesk are conventional CRUD; LLM appeal drafting at production quality is proven by Waystar's own published results (H01-E4) and Muni/Aegis (H01-E11/E12); v1 payer-rules library covers the top ~8 payers which dominate the evidence (UHC, Aetna, Cigna, BCBS plans, Humana, MA). Real work items that fit inside 90 days: BAA + encrypted PHI storage (standard SaaS-on-AWS pattern), fee-schedule-optional variance baseline (histogram of historical allowed amounts — avoids the contract-loading burden that stalls Rivet-class tools), CSV/835 import UX. The agent team leverage: payer-policy research, CARC mapping tables, appeal-letter template corpus, and per-payer deadline rules are exactly the grindable research surface agents build fast.

---

## 5. Forcing function & why now

**Forcing function (Grade A, held):** the practice's own revenue is gated per claim; appeal windows (60–180 days) and timely-filing limits are hard, self-executing deadlines — miss them and the money is legally gone (H01-E17; S03-2 "revenue legally forfeited"). This runs continuously, not annually.

**Why now (2024–2026):**
- **The counterparty automated first, at scale, in 2026:** BCBSTX/BCBSIL blanket E&M downcoding live July 2026 (H01-E1, S05-2-E1); Aetna/Cigna automated pre-screening reported by billers Jan 2026 (S08-2-E1); Experian: 54% say denials increasing, 68% say clean claims harder than a year ago (S08-2-E6); initial denial rates climbed to ~11.8% in 2024 and MA to ~15.7% (H01-E18).
- **Regulators validate the fight but won't end it soon:** Maryland ordered Cigna to halt downcoding or show cause (Mar 2026, H01-E2); Illinois banned automated downcoding — **effective 2028** (H01-E1). The 2026–28 gap is a legislated arms-race window; post-2028, state-by-state bans convert the product's downcode module into an enforcement-evidence tool rather than killing the denial core (denials long predate payer AI).
- **CMS-0057-F:** from 2026-01-01 impacted payers must give specific denial reasons and decision timelines (S05-3-E2) — machine-readable denial rationale makes agent-drafted rebuttals materially better.
- **LLM capability crossed the threshold:** enterprise results published (40% more overturns, 90% faster — H01-E4) prove the technical bet; the down-market tier is a distribution race now.

---

## 6. Distribution plan (solo-founder realistic)

**Named channels for the first 10 customers:**
1. **r/CodingandBilling (19,338 subscribers, H01-E24)** — the anchor threads themselves; respectful build-in-public participation + free "ERA X-ray" audits for thread participants (the BCBSTX downcode victims of July 2026 are live in-thread now, S05-2-E1).
2. **Behavioral-health practice communities** — SimplePractice-adjacent Facebook groups and r/therapists (the Maryland/Cigna thread, H01-E2); the BCBSIL wave (H01-E1) gives a same-week outreach hook to IL group practices.
3. **HBMA (~300 billing-company members, H01-E20)** — one webinar/sponsor slot reaches firms that each cover 10–50 practices; billing companies are the multi-client wedge customer.
4. **AAPC local chapters (400+; 300k members, H01-E23)** — chapter talks on "beating the 2026 downcode wave" = content-led inbound from the exact workers who choose tools.
5. **State medical societies mobilized on downcoding** (ISMS; Memphis Medical Society alert; per H01-E1 coverage) — they are actively alerting members and need something to point to.
6. **Founder-led "recovered dollars" case studies** recycled into the payer-deadline SEO space Muni has proven crawlable (H01-E17-class content).

**Sales cycle estimate:** self-serve trial ("upload last 90 days of ERAs → see flagged dollars in minutes") makes the demo the close; 1–4 weeks for practices, 4–8 weeks for billing companies. No procurement apparatus at this tier (the anti-requirement is proven by Muni's no-credit-card motion, H01-E11).

**Price & packaging hypothesis (comparable-priced):** Solo behavioral $99–199/mo; specialty practice $299–599/mo; billing companies $79–129/client/mo. Optional batch-recovery campaigns at 10–15% of recovered — half the 20–35% services rate (H01-E16). Anchors: Rivet $6k/yr floor (H01-E13), Muni $20/appeal (≈$600–1,200/mo at evidenced denial volumes), outsourcers 4–10% of collections (H01-E10), specialist salary $37.5–50.5k (H01-E22). At $499/mo the product costs ~12% of one denials specialist.

---

## 7. AI-structural advantage

The rework is priced in public: $25–181/claim (H01-E18), $37.5–50.5k/yr salaried (H01-E22), 20–35% contingency (H01-E16). Agents collapse the marginal cost of classify→research→draft→track to cents, so a $99–599/mo product can profitably serve accounts that cannot pay any incumbent's floor: Waystar's model needs implementation fees and multi-year contracts (H01-E3); Adonis/AKASA raised on enterprise ACVs (H01-E5/E6); outsourcers cannot cut the 4–10% take that IS their revenue; contingency firms need large recoveries per engagement. Down-market self-serve at this price point structurally breaks all four models — the incumbents' economics resist following even though their AI already can (the honest statement of the advantage: it is a GTM/economics moat window, not a capability gap).

---

## 8. Moat path

**Accumulates with usage:** (1) payer × CARC × argument × outcome corpus — which appeal language overturns which denial at which payer, measurable in the recovery ledger; nobody at this tier holds this data and enterprise players' data lives in enterprise contracts; (2) allowed-amount baselines per payer/CPT/region built from ingested 835s — a fee-schedule shadow-map practices themselves don't have; (3) workflow lock-in — open AR and deadline state live in the system; leaving mid-pipeline risks forfeiting live appeals; (4) billing-company multi-client operations (roles, client reporting) that per-letter tools lack.

**Thin-wrapper honesty:** appeal-letter *drafting* is already commoditized — ChatGPT can draft one, Waystar ships it (H01-E4), Muni sells it for $20 (H01-E11). If the product were only drafting, it would fail the thin-wrapper gate. The defensible product is the ERA ingestion + deadline state machine + variance detection + outcome data. Rated honestly as a moderate moat (3/5): real accumulation, but 12–24 months of it before it deters a funded copier.

---

## 9. Risks & unknowns (top 5 + 1)

| # | Risk | Resolving test |
|---|---|---|
| R1 | **Entrant race**: Muni/Aegis/ClaimCure validate and contest the tier; one could raise and sprint | Monthly tracker on funding/traction (Crunchbase, YC demo days). Kill-adjacent trigger: a competitor raises ≥$10M AND ships ERA-level underpayment/batch-downcode defense for this tier before our first 25 customers |
| R2 | **Portal automation gray zone**: Availity bans bots (H01-E7); appeals have no API (H01-E8). Does packet-not-portal automation save enough time? | 5-practice pilot measuring minutes/denial with human-submit flow; target ≥60% time reduction. Also: apply for Availity vendor API partnership (eligibility/claim-status APIs are legitimately available, H01-E8) — outcome documents the compliant rail |
| R3 | **Transience**: 2026 downcode wave could retreat under regulatory pressure (IL 2028 ban; MD order) | Track denial/downcode rates through 2027 (Experian annual, ISMS follow-ups). Mitigant already in design: denials + underpayments + deadlines predate and outlive payer-AI downcoding; downcode module is one of six features |
| R4 | **PHI trust at solo-founder scale**: will practices upload ERAs to a new vendor? | 10 discovery calls with BAA-only posture (SOC 2 roadmap); Muni's no-credit-card traction motion suggests yes — verify directly; billing companies as early adopters are more risk-tolerant and tech-literate |
| R5 | **Incumbent down-market move**: Tebra/SimplePractice ship native AI denial tools, or Waystar launches self-serve | Quarterly release monitoring. Structural hedge: billing companies are multi-PM by nature — a cross-platform defense desk survives any single EHR's native feature; EHR-native tools also can't see claims billed outside their system |
| R6 | **Fee-schedule data quality**: practices don't have contracts organized; variance detection could false-positive | Pilot the historical-835-baseline approach (no contract upload needed) on 3 practices' real remit files; measure precision of flagged variances against biller adjudication |

---

## 10. Scores

| # | Dimension | Weight | Score | Rationale (evidence) |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 5 | Daily, per-claim, emotionally charged ("our practice future depends on them" S05-2-E1; "half the work done" S05-2-E4); 2,400-claim monthly batch events (H01-E1) |
| 2 | Budget proof | 15% | 5 | Four live budget lines: 4–10% of collections, $37.5–50.5k salaries, 20–35% contingency, $25–181/claim rework (H01-E10/E22/E16/E18) |
| 3 | Competitive gap | 12% | 4 | Enterprise served (Waystar/AKASA/Adonis); tier below served only by seed per-letter entrants; ERA-native batch/underpayment defense unserved (§3). Docked one for the closing window |
| 4 | Forcing function | 10% | 5 | Per-claim money gate + statutory-grade deadlines (60–180d) + live 2026 payer-AI wave + CMS-0057 denial-reason mandate (H01-E17/E1; S05-3-E2) |
| 5 | Founder+agents feasibility | 12% | 4 | 835-file integration (no EHR dependency), proven LLM drafting, standard BAA posture; docked one for PHI/trust and payer-rules breadth (§4) |
| 6 | Distribution reachability | 10% | 4 | Named, dense watering holes (19.3k-sub subreddit, 400+ AAPC chapters, HBMA's 300 firms, mobilized medical societies); self-serve demo motion; docked one because communities are moderated/vendor-wary |
| 7 | AI-structural advantage | 8% | 4 | Collapses a published labor price; incumbents' ACV/%-of-collections economics resist following (§7); docked one because capability (not economics) is already commodity |
| 8 | Moat path | 8% | 3 | Outcome corpus + allowed-amount baselines + workflow lock-in accumulate, but need 12–24 months (§8); drafting layer is commodity |
| 9 | Expansion ceiling | 5% | 4 | Same buyer expands to eligibility/COB (S08-3), PA (H03), credentialing (H02), then the 4–10%-of-collections services line itself — an AI-native billing company shape |
| 10 | Durability | 5% | 3 | Arms race is durable; but state downcode bans (2028+), possible payer retreat, and GPT-class drafting commoditization cap certainty |

**Weighted total: (75+75+48+50+48+40+32+24+20+15)/5 = 85.4 → 85/100 (pursue band)** — conditional on building the differentiated wedge (ERA-native + batch + underpayments + billing-company channel), not a me-too appeal-letter generator (which would score ~65 on gates 3/8/10).

**Hard gates:** Budget proof PASS (overwhelming). Reachable buyer PASS (self-serve SMB, proven by Muni's motion). Thin-wrapper PASS with honesty note (workflow/data depth required — §8; drafting alone would fail). Head-on collision PASS (no well-funded, competent incumbent at this wedge+segment: Waystar = same job, different segment/GTM; Muni = same segment, seed-stage, different product shape; Adonis/AKASA = enterprise). Platform hostage PASS (rails are HIPAA-standard X12 835/276/277 across all payers + human-submit appeals; no single platform's tolerance required; Availity APIs optional, not load-bearing). Regulated practice PASS (drafts issued under provider review/signature; no medicine/law practiced by vendor).

**Displacement sentence:** Current solution = a $37.5–50.5k denials specialist (or 4–10%-of-collections outsourcer) plus Excel trackers, with 35–60% of denials never worked and 1–3% of net revenue silently underpaid. New product = an ERA-native denial-and-underpayment defense desk ($99–599/mo) with deadline state machine, batch downcode reconsiderations, and agent-drafted appeal packets. The customer switches because ~70% of worked denials overturn — recovering even a fifth of the currently-forfeited pool returns 10–40x the subscription, verifiable in the product's own recovery ledger.

---

## 11. Verdict proposal

**PURSUE.** The sweep's best evidence base: per-claim forcing function, four verified budget lines, a 2026 payer-AI escalation with a legislated 18-month defense window, and a buyer reachable self-serve. The window is real but closing — seed entrants (Muni, Aegis) prove the wedge and will contest it; differentiation must be ERA-native batch downcode/underpayment defense and the billing-company channel, not appeal letters. **Bundle note:** H01 shares its buyer with H02/H03; H01 is the correct entry product (fastest money-now ROI), with credentialing/PA as expansion — if Wave 3 concentrates, attack this one. Kill triggers: R1 funding trigger; pilot fails R2's ≥60% time-saving bar.

---

## 12. Evidence ledger

New evidence: `outputs/evidence/dh01_denial_defense.jsonl` — 25 records, H01-E1…E25, schema-valid, all accessed 2026-08-27.

| ID | Claim (short) | Type |
|---|---|---|
| H01-E1 | BCBSIL downcoding live 7/2026; 2,400 claims/mo one practice; ISMS 72%; IL ban eff. 2028 | news (WBEZ) |
| H01-E2 | Maryland orders Cigna to halt downcoding (3/2026); r/therapists tracking | forum-post (Arctic Shift-verified) |
| H01-E3 | Waystar $100–300/provider/mo + $2–10k impl., multi-year (competitor-reported) | vendor-blog (labeled secondary) |
| H01-E4 | Waystar AltitudeAI: gen-AI appeals 1/2025→9/2025, 40% more overturns | press-release |
| H01-E5 | Adonis $40M Series C 3/2026; enterprise logos | press-release |
| H01-E6 | AKASA $205M; 650 hospitals | press-release |
| H01-E7 | Availity eliminated bot access; gated vendor APIs | vendor-blog |
| H01-E8 | Availity API list: eligibility/PA/status — no appeals API | vendor-docs |
| H01-E9 | Claim.MD $30/$60/$120/mo; unlimited ERA | vendor-pricing |
| H01-E10 | Outsourcing 4–10% of collections; per-claim $3–10 | vendor-blog (Tebra survey) |
| H01-E11 | Muni Health: $20/appeal, 2–10-provider specialty segment | vendor-pricing |
| H01-E12 | Aegis YC S25: hospitals/billing teams, portal submission | vendor-docs |
| H01-E13 | Rivet from $6,000/yr; 9 reviews; mid-size base | review-site |
| H01-E14 | MD Clarity RevFind: contract-variance detection, demo-gated | vendor-docs |
| H01-E15 | Underpayments 7–11% of claims ≈ 1–3% of net revenue (vendor-estimated) | vendor-blog |
| H01-E16 | Recovery services: 20–35% contingency | vendor-blog |
| H01-E17 | Appeal windows: UHC 65d; Aetna/BCBS/Cigna 180d; MA 60d; TF 90–180d | vendor-blog (payer-manual-consistent) |
| H01-E18 | 35–60% never resubmitted (AHIMA); $25–181 rework; denial-rate trend | vendor aggregation citing AHIMA/AHA/KFF/Health Affairs |
| H01-E19 | AMA 2024: 47.4% of physicians in ≤10-physician practices | report |
| H01-E20 | HBMA: ~300 firms/47k employees/~80% of third-party claims; ~2,000 cos. | association |
| H01-E21 | SimplePractice: 250k practitioners; 58.8% insurance sessions; denial struggles | press-release |
| H01-E22 | Robert Half denials specialist $37.5–50.5k (re-verified 8/2026) | job-posting |
| H01-E23 | AAPC 300k+ members, 400+ chapters | association |
| H01-E24 | r/CodingandBilling 19,338 subscribers | api-data |
| H01-E25 | Claim.MD eligibility API + batch claims + ERA formats | vendor-docs |

Carried (verified upstream): S05-2-E1…E8, S08-2-E1…E6, S08-3-E1…E4, S03-1-E1…E5, S03-2-E1…E5, S05-3-E2 (CMS-0057-F) — see `outputs/evidence/s05_backoffice_pros.jsonl`, `s08_money_friction.jsonl`, `s03_human_middleware_jobs.jsonl`.
