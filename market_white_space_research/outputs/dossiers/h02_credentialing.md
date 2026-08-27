# Opportunity Dossier — Provider Credentialing & Payer-Enrollment Autopilot

Validator: Wave-2 validator, H02 · Date: 2026-08-27 · Source hypothesis: H02 (Manager 1 promotion memo, Rank 2 ★TOP-5) · Ground(s): 03 (human-middleware jobs), 05 (back-office pros), 11 (services-to-software)

Evidence ledger: `outputs/evidence/dh02_credentialing.jsonl` (H02-E1…E35). Carried claims retain their Manager-1 verification status; all fresh claims fetched 2026-08-27.

---

## 1. The pain, restated precisely

**Who hurts:** (a) solo and small medical/behavioral-health/therapy practices (1–10 providers) in the US — every new practice launch and every clinician hire; (b) practice managers at small groups and specialty MSOs adding providers; (c) the billing companies and credentialing-services firms that sell this work as piecework and run it on humans + Excel. Segment (a)–(b) is the buyer; segment (c) is both a competitor and a white-label channel.

**The workflow failure:** enrolling one provider with 5–15 payers is a 60–180-day black box: CAQH profile creation and quarterly re-attestation, payer-specific applications (each panel has its own forms), document collection (license, DEA, malpractice COI, work history), PECOS/Medicaid portal enrollment, then months of status-chasing calls in which the payer itself gives conflicting answers. Until it clears, the provider's insured sessions cannot be billed in-network — revenue is parked. Lapses (missed re-attestation, expired documents, unanswered directory verification) cause claim denials and directory removal.

**Frequency — honest segmentation (H02-E2):** for a settled solo practice the pain is front-loaded ("Once you're set up it's fine" — top comment, score 29). The always-on cadence — quarterly CAQH re-attestation under the No Surprises Act directory regime (H02-E32), expirables, recredentialing every 2–3 years, PECOS revalidation, per-hire enrollment — makes groups, MSOs, and billing companies the recurring buyers; solos are a high-volume transactional entry tier.

**Strongest three artifacts:**
1. **Fresh, 2026-08-24 (H02-E1):** r/therapists, score 17/26 comments — "Every panel has its own credentialing forms, and half of them lost my paperwork or sat on it for three months before telling me they needed a document I already sent… I got into this work to actually help people, not to become a full-time credentialing and billing clerk." (Carries H02 and H01 pain in one buyer — bundle evidence.)
2. **Fresh, 2026-08-26 (H02-E3):** therapist paid credentialing service "Intelix" — six months, zero movement on BCBS/Aetna, refunded at month 8. The $100–300/app service layer is chase-and-wait and visibly fails.
3. **Official (H02-E7):** Nevada state provider-network review — willing providers "can face delays of 6-9 months before being able to see patients due to the protracted credentialing process."

Supporting: Humana giving a practice manager different network answers on every call (H02-E4, manager-verified); UHC telling a practice to resubmit claims its own credentialing desk confirms are enrolled (H02-E5); a standing freelance market for pure CAQH upkeep (H02-E6); vendor analyses attributing ~85% of delays to clerical CAQH errors — i.e., the delay driver is systematizable paperwork, not medicine (S11-2-E7, vendor-labeled).

## 2. Budget proof

Money already moves against this pain on four distinct lines (per customer per year):

| Line | Amount | Source |
|---|---|---|
| Outsourced per-application fees | $100–300/payer/provider (Medwave, manager-verified); $200–500/payer (Medicotech 2026, fresh); $150/app–$500+/provider/mo (PPS) | H02-E10, E11, E12 |
| Initial multi-payer credentialing, one provider | $1,500–3,500 (both Medwave and Medicotech independently); to $7,000+ complex | H02-E10, E11 |
| Ongoing maintenance | $600–2,400/provider/yr (recredentialing + CAQH upkeep) | H02-E11 |
| In-house headcount | $43,750–57,000 (Robert Half); $48,152–64,916 posted by QualDerm MSO (re-verified 2026-08-27); 3,990 open specialist postings on one aggregator | H02-E14, E15, E16 |
| Parked billings during the gap (the forcing cost) | $6,000–8,000/provider/mo average (Medicotech); $8,000–15,000/mo PCP and $30,000+/mo specialist (PayerReady) — vendor-labeled | H02-E11, E13 |
| Substitute platforms at the solo tier | Alma $125/mo membership; Headway 10–15% of every reimbursement; leaving forfeits the panel to the platform | H02-E17 |

**Worked arithmetic.** A 5-provider group adding 2 providers/yr and maintaining 10 payer relationships spends today: 2 × ($1,500–3,500) initial + 5 × ($600–2,400) maintenance = **$6,000–19,000/yr in service fees alone**, or ~⅓–1 FTE of a $46k specialist — before counting a single week of avoidable delay at $200–1,000/day of parked billings per waiting provider. A solo therapist spends $500–2,000 one-time (5–8 payers at $100–300) or surrenders 10–15% of gross to Headway indefinitely. A billing company doing 30 applications/month books $4,500–15,000/mo of piecework revenue produced by $22/hr labor. Budget is proven at every tier.

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| **Medallion** (FirstLayerAI Inc.) | Product+service, AI | Provider groups 5–50+, health systems, payers, RCM, digital health | No public pricing; "tailored engagement"; ~$200–500/provider/mo per 3rd-party comparison | Sales-led, quote-gated; reviewers ask for "a better self service option"; "CAQH pull doesn't pull all information over"; enrollment/contracting timelines still frustrate (H02-E18–E21) |
| **Assured** (withassured.com) | Product, AI-agent-native | Health systems, digital health, growth-stage groups (customers: Tono, Birches, Blossom) | No public pricing; demo-only funnel | Closest head-on tech; $19M Series A Jul 2026 (Insight). GTM is sales-led and upmarket; its own therapist-facing guide lists zero self-serve options and pitches Assured at "enterprise health systems" (H02-E22, E23) |
| **Verifiable** | Product + NCQA CVO | Health plans, digital health/telehealth at scale | No public pricing; $27M Series B | Enterprise motion; CVO/compliance-centric, not a small-practice enrollment desk (H02-E25) |
| **CertifyOS (Certify)** | Product/API | Health plans, digital health, multi-state groups | No public pricing; $40M Series B | Provider-data infrastructure for plans — not sold to a 2-provider practice (H02-E24) |
| **Modio OneView** (CHG-owned) | Product | Mid-market/enterprise 20+ providers | ~$1,000–3,000/mo entry per 3rd-party comparison | Minimums price out small groups; owned by a staffing company, roadmap serves staffing/enterprise (H02-E21, E26) |
| **symplr / CredentialStream** | Product | Hospital medical staff offices | Enterprise custom | Hospital privileging DNA; irrelevant to a therapy group (H02-E21) |
| **MedTrainer** | Product+service | SMB clinics (most accessible incumbent) | $20–50/user/mo software (quote-gated); services extra | Compliance-suite breadth, not an enrollment autopilot; still sales-quoted, not self-serve (H02-E27) |
| **Credentialing-services firms** (Medwave, PPS, Intelix, thousands of micro-firms) | Service | Everyone incl. 1–10-provider practices | $100–500/payer/provider; $1,500–3,500 initial; $600–2,400/yr | Chase-and-wait piecework on the same portals; opaque; the fresh Intelix artifact: 6 months, no movement, refund (H02-E3, E10–E12) |
| **In-house specialist / freelance CAQH labor** | Headcount | Groups/MSOs | $43,750–64,916/yr; $10–25/hr | Excel trackers, single point of failure, 3,990 unfilled postings show supply strain (H02-E14–E16, E6) |
| **Headway / Alma / Rula / Grow** | Platform (credentialing as loss-leader) | Solo therapists | "Free" credentialing for 10–15% of reimbursements or $125/mo | Panel belongs to the platform on exit; therapists explicitly credential independently for "protection against potential platform shutdowns" (H02-E17, E9) |
| **EHR add-ons** (SimplePractice/TheraNest assisted credentialing) | Product add-on | Solo therapists | Add-on fees | Assisted service referral, not an autopilot; named in community as "help", not a solution (thread H02-E1 comments) |
| **DIY: CAQH + spreadsheets + phone** | Stack / "do nothing" | 1–3-provider practices (the advised default) | $0 + owner evenings | The advice published for small practices is literally "free CAQH + spreadsheet" — the segment is unserved by software on purpose (H02-E21); produces the 2026 complaint stream above |

**Deep-read of the closest two.** *Medallion:* $130M raised; Aug-2025 pivot announcement into AI infrastructure + **CredAlliance**, a payer-side clearinghouse ("verifies providers once and syndicates the results across participating payer networks") — shipping velocity is real, but pointed at payers and 1M-provider enterprise scale, and its review record shows the small buyer still can't buy it without a sales cycle (H02-E19, E20). *Assured:* AI agents that "Complete payer-specific PDFs" and "Navigate supported payer portals," NCQA-certified, 2-business-day credentialing claim, 100+ customers — the same technical thesis as this wedge, one month post-Series-A. Its funnel is 100% demo-gated; no price on the site; customer logos are venture digital-health startups (H02-E22). **Nobody sells a self-serve, published-price enrollment autopilot to the 1–10-provider practice.** The segment's current "software" is a free data portal (CAQH), and its current service layer fails visibly.

## 4. The wedge

**Product:** an enrollment autopilot for small practices and their billing companies — "the credentialing firm, as software you can watch."

Feature list (≤6):
1. **Provider vault + document chase:** one intake, all credentials/expirables (license, DEA, malpractice COI, work history); automated collection reminders to the provider.
2. **CAQH autopilot** (via the official Practice Administrator delegated role): profile build, error-lint against the payer-rejection ruleset (the "85% of delays are CAQH errors" class), quarterly re-attestation and NSA directory confirmation on schedule.
3. **Application assembly:** agent-filled payer enrollment applications (PDF + portal) for a launch matrix of ~20 national/regional payers + PECOS + 2 state Medicaids, human-review checkpoint before every submission.
4. **Status-chase agent:** scheduled portal status checks under the customer's own delegated credentials, templated follow-up emails/faxes, call scripts with logged outcomes (AI voice later); every touch lands on a visible per-application timeline — the anti-black-box.
5. **The tracker Excel replaced:** provider × payer pipeline with aging, expected dates vs. payer SLAs, and parked-revenue counter ($/day per waiting provider).
6. **Deadline guard:** recredentialing windows, expirables, re-attestation, revalidation alerts.

**Explicitly does NOT do:** primary-source verification as a certified CVO, delegated credentialing, hospital privileging, state licensing, payer contract-rate negotiation, clinical anything, and no headless scraping of portals that prohibit it (all portal work runs as authorized delegated users — CAQH Practice Administrator, CMS I&A surrogacy — the same legal posture as a credentialing firm employee; H02-E29, E30).

**≤90 days, founder + agents? Yes, with a bounded matrix.** This wedge needs no EHR integration (unlike H01/H03) — its surfaces are CAQH, PECOS, payer forms/portals, email/fax. The build is a CRUD vault + a form-fill library + agent runbooks + a tracker UI. The 90-day constraint is covered by capping the launch matrix (one vertical — behavioral health; ~20 payers; 2 states) and running weeks 1–8 as concierge-with-agents on 10 design-partner enrollments to harvest the payer-quirk library. The long tail of payers/states is deliberately deferred, not denied.

## 5. Forcing function & why now

**Forcing function (grade A, money-movement + standing federal cadence):** a provider generates $0 in-network until enrollment approves — self-enforcing, per hire, no regulator required. On top: quarterly CAQH re-attestation with directory REMOVAL for non-response under the No Surprises Act 90-day verification regime (H02-E32); recredentialing every 2–3 years; PECOS revalidation with PECOS 2.0's stricter revocation authority (H02-E31). Purchase is compelled at a known moment: the new NPI / new hire — an event so legible that an outbound spam industry already mines NPPES for it within days (H02-E8, E35).

**What changed 2024–2026:** (1) LLM agents crossed the threshold for exactly this work — form assembly, document lint, status-chasing, 120-day-long follow-up without forgetting — while the incumbent price list ($100–500/app) hasn't repriced; (2) the AI-native proof arrived upmarket: Medallion's Aug-2025 AI pivot and Assured's Jul-2026 Series A validate the technical thesis while both stay sales-led enterprise (H02-E19, E22); (3) PECOS 2.0 (late 2025 → 2026 migration) put every Medicare-enrolled provider through a new system with mandatory MFA — an upheaval cohort re-learning enrollment (H02-E31); (4) NSA directory enforcement converted upkeep from episodic to quarterly (H02-E32); (5) behavioral-health supply keeps growing and its platform escape-hatch (Headway/Alma) now visibly costs 10–15% of gross plus panel ownership — creating an independence-seeking cohort (H02-E17, E9, plus the Headway backlash thread in the same week's r/therapists).

## 6. Distribution plan (solo-founder realistic)

First 10 customers, by named channel:
1. **r/therapists and r/CodingandBilling** — live, current-week demand: the 2026-08-24 mess thread (26 comments), the 2026-08-26 "which credentialing service?" referral thread. Answer-first participation, not link-drops (r/CodingandBilling already hosts builder reality-check posts as accepted practice; H02-E1, E3).
2. **NPPES new-registrant motion, counter-positioned:** the weekly new-NPI list is public and already productized by a free digest (H02-E35). The incumbent motion against it is dozens of daily spam calls that the buyer hates (H02-E8) — a content/PLG motion ("your enrollment checklist + free tracker, no phone calls") aimed at the same trigger moment differentiates on arrival.
3. **Billing companies as white-label channel:** the r/CodingandBilling freelancer/billco community sells credentialing as $100–300/app piecework run on $22/hr labor; 2–3 white-label partners each bring a book of small-practice clients (H02-E6, E10).
4. **Therapist-practice consultants & communities:** the substack-guide authors (H02-E9), private-practice courses, and state counseling-association listservs — the people currently teaching DIY credentialing.
5. **Later (not first-10):** EHR marketplaces (SimplePractice/TherapyNotes/Tebra), MGMA/HBMA/AAPC state chapters for the group/billco tier.

**Sales cycle estimate:** solo/self-serve tier: days (transactional, card-swipe at the new-NPI moment). Groups 3–10 providers: 2–6 weeks. Billing-company white-label: 1–2 months. No procurement anywhere.

**Price & packaging hypothesis (comparable-anchored):** solo — $99/payer application or $499 flat for a 6-payer panel start plus $39/mo maintenance autopilot (vs. $100–300/app human services and Alma's $125/mo; H02-E10, E17). Group — $59–99/provider/mo (vs. $600–2,400/provider/yr services maintenance ≈ break-even, plus the specialist salary avoided; H02-E11, E15). Billco white-label — $25–49/application at volume (their COGS today is ~2–5 labor hours/app). Each tier undercuts the evidenced current spend by ~½–⅓ while carrying software margins.

## 7. AI-structural advantage

The unit being sold today is human hours: $22/hr specialists (posted), $100–500 per application (priced), 3,990 unfilled seats (counted). The work is document lint + form transcription + polite persistence on a 120-day clock — the exact shape agents hold cheaply and humans hold badly. An agent-heavy team collapses the per-application labor cost toward pennies while *improving* the artifact (every touch logged, nothing forgotten at day 90), so a $99 application can carry software margins where a service firm needs $150–300 to pay a human.

Why incumbents' economics resist following down-market: Medallion/Assured/Verifiable/CertifyOS monetize via sales-led enterprise contracts (every one of them is quote-gated — verified across all four pricing surfaces; H02-E18, E22–E25). Serving 1–10-provider practices requires published prices, card-swipe onboarding, and support economics their CAC and ACV structures aren't built for; their capital ($130M/$40M/$27M/$25M) is pointed at payers, health systems, and 1M-provider clearinghouses. The honest caveat: this is a **go-to-market** advantage, not a capability exclusivity — Assured's agents already "navigate supported payer portals." The structural bet is that a venture enterprise vendor won't rebuild as a PLG business for $99 customers before a focused entrant owns the segment.

## 8. Moat path

What accumulates with usage:
- **The payer-quirk library:** per-payer, per-state form versions, rejection reasons, real turnaround distributions, follow-up cadences that work — harvested from every application processed. This is the asset service firms hold in employees' heads and never systematize.
- **Outcome data:** predicted approval timelines and error-risk lint ("this CAQH field pattern triggers Aetna rework") get better with volume — the basis of an SLA no human firm can honestly offer.
- **Workflow lock-in:** after enrollment, the maintenance autopilot (quarterly re-attestation, expirables, recredentialing, directory confirmations) makes the product the practice's standing compliance layer — the reason the solo tier doesn't churn after panel completion.
- **Channel embed:** white-label billing companies route their books through it.

**Thin-wrapper honesty:** form-filling alone is one model call away from commodity — a GPT-class tool can draft a CAQH profile today. The defensibility is NOT the drafting; it is (a) the delegated-access integration surface (Practice Administrator/I&A surrogate wiring per customer), (b) the longitudinal quirk/outcome data, and (c) being the system of record for a 2–3-year compliance calendar. If the wedge shipped as "AI fills your PDFs" it would fail the thin-wrapper gate; shipped as the autopilot workflow above, it does not. Moderate risk remains and is scored accordingly (Moat 3/5).

## 9. Risks & unknowns (top 5, each with a resolving test)

1. **Portal-automation fragility (the biggest technical risk).** Availity's OAA explicitly prohibits bot/scraping methods with sole-discretion termination and polices VPN-obfuscated access; CAQH gates logins with robot checks; PECOS 2.0 mandates MFA (H02-E28, E31). Mitigant: the lawful path is delegated human-credentialed access (CAQH Practice Administrator module; CMS I&A third-party surrogacy — both official; H02-E29, E30) with agents working under supervision rather than headless scale-scraping; Availity is central to claims (H01) but peripheral to enrollment. **Test (weeks 1–6):** run 10 real enrollments end-to-end under delegated credentials; measure % of touches automatable without ToS-prohibited methods; counsel review of CAQH/Availity/PECOS/2-state-Medicaid terms; design every portal step to degrade gracefully to assisted-human mode.
2. **Head-on drift: Assured or Medallion launches self-serve down-market.** Assured already SEO-markets to therapists (H02-E23); one pricing-page change collapses the segment gap. **Test (continuous):** monitor both vendors' pricing pages/job postings monthly; run 10 competitive deals and log why the buyer couldn't buy them today; kill-trigger = either ships published pricing ≤$200/provider/mo with self-serve onboarding before we reach 50 customers.
3. **Payer-side compression erodes the delay pain.** CredAlliance (payer clearinghouse), UHC Onboard Pro, and NCQA-aligned digitization could cut 90–180 days toward 30 (H02-E19, E33). The maintenance/monitoring layer survives; the "parked revenue" urgency shrinks. **Test:** instrument actual per-payer turnaround on our own applications from day 1; if median top-5-payer approval falls below ~30 days by end-2027, re-weight the product toward maintenance + multi-payer roster compliance.
4. **Solo-tier churn (front-loaded pain).** "Once you're set up it's fine" (H02-E2) — the transactional tier may one-and-done. **Test:** cohort retention of first 20 solos on the $39/mo maintenance plan at month 6; if <40% retain, re-center packaging on groups (per-provider/mo) and billco white-label (per-app) where cadence is structural.
5. **Trust & liability: an agent error delays a provider's income or triggers a payer revocation** (PECOS 2.0's stricter revocation regime raises stakes; H02-E31). **Test:** E&O/professional-liability quote for credentialing-services scope in week 1 (services firms are insurable today — same risk class); mandatory human-review checkpoint before every submission in v1; track error rate vs. the Intelix-class service baseline on the first 50 applications; publish the log to the customer as the product's core trust artifact.

## 10. Scores

| # | Dimension | Weight | Score | Rationale (one line) |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 4 | Money-gated, emotionally charged, fresh 2026 artifacts; docked one for front-loaded shape at the solo tier (H02-E1–E7, E2) |
| 2 | Budget proof | 15% | 5 | Per-app price lists ×3 independent, posted salaries, 3,990 open seats, platform take-rates — money moves at every tier (H02-E10–E17) |
| 3 | Competitive gap | 12% | 4 | $220M+ of incumbents all quote-gated enterprise; published advice for 1–3-provider practices is "free CAQH + spreadsheet"; services fail visibly (H02-E21, E3) |
| 4 | Forcing function | 10% | 5 | Can't bill until enrolled; NSA quarterly re-attestation with directory removal; recredentialing/revalidation clocks (H02-E32, E31) |
| 5 | Founder+agents feasibility | 12% | 4 | No EHR needed; forms/docs/follow-up are agent-shaped; docked for portal fragility + phone tail (H02-E28–E31) |
| 6 | Distribution reachability | 10% | 4 | Live communities, public trigger event (new NPI), white-label channel; docked for spam-saturated channel trust (H02-E8, E35) |
| 7 | AI-structural advantage | 8% | 3 | Agents collapse the $100–500/app labor line, but two funded AI-natives exist — advantage is GTM segment, not capability (H02-E22) |
| 8 | Moat path | 8% | 3 | Quirk library + outcome data + compliance-calendar lock-in accumulate; drafting layer itself is commoditizing (§8) |
| 9 | Expansion ceiling | 5% | 4 | Natural bundle to denials/PA/licensing/roster for the same buyer; category proven at nine-figure funding scale |
| 10 | Durability | 5% | 3 | CredAlliance/payer digitization compresses delay pain over years; 1,000-plan fragmentation persists (H02-E19, E34) |

**Weighted total: 80.8 / 100 → "pursue" band (80–100).**

**Hard gates:**
- No budget proof — **PASS** (overwhelming; §2).
- Unreachable buyer — **PASS** (self-serve solos, SMB groups, white-label billcos; no procurement).
- Thin-wrapper risk — **PASS, conditionally** (workflow + delegated-access integrations + 120-day statefulness + compliance calendar; a form-fill-only version WOULD fail — wedge definition matters; §8).
- Head-on collision — **PASS, narrowly — the closest gate.** Assured/Medallion are funded, competent, currently shipping AI credentialing — but verifiably sell sales-led to health systems/digital health with no self-serve or published pricing (H02-E18, E22, E23); the 1–10-provider segment is documented as advised to DIY (H02-E21). Risk #2 carries the standing kill-trigger.
- Platform hostage — **PASS** (multi-surface: CAQH + PECOS + ~1,000 payers; official delegation paths exist on the two federal-ish spines (H02-E29, E30); no single platform's tolerance is load-bearing, though Availity-class ToS constrains method choices).
- Regulated practice — **PASS** (administrative enrollment work; credentialing-services industry operates unlicensed today; no UPL analog; optional NCQA CVO certification explicitly out of wedge scope).

**Displacement sentence:**
> Current solution = outsourced credentialing firms at $100–500 per payer application plus $600–2,400/provider/yr maintenance, or a $43,750–64,916 in-house specialist, or free-CAQH-plus-spreadsheet DIY — all running a 60–180-day black-box chase that parks $6,000–30,000+/month per waiting provider. New product = an enrollment autopilot (vault → CAQH autopilot → application assembly → status-chase agents → deadline guard) at ~$99/application or $59–99/provider/mo. The customer switches because the same enrollment costs ½–⅓ of the service price, every application has a visible logged status instead of conflicting phone answers, and cutting even two weeks of clerical delay returns $3,000–15,000 per provider.

## 11. Verdict proposal

**PURSUE (80.8).** Budget proof and forcing function are top-of-program; the segment gap below the $220M-funded enterprise tier is verified on every vendor's own pricing surface; fresh August-2026 operator pain confirms nothing has closed it. Honest weaknesses: moat must be earned (3/5), Assured is one pricing page from head-on, and portal ToS constrains method (delegated access, not headless bots). Carry Risk-#2's kill-trigger into any build. *(Manager 2 decides.)*

**Bundle assessment (H01/H03 shared buyer):** the strongest artifact here (H02-E1) contains H01's pain in the same sentence, and billing companies sell all three jobs. H02 is the correct **land** wedge: bounded, EHR-free, transactional pricing mapped to existing per-app spend, and it builds the exact assets H01 needs next — per-payer portal delegated access, payer-quirk data, and the practice's trust. H03 (needs chart access) should trail. If the director consolidates, propose sequence H02 → H01 → H03 under one "small-practice payer-defense desk"; if only one proceeds to red team as-is, H02 stands alone on this dossier.

## 12. Evidence ledger

Full JSONL: `outputs/evidence/dh02_credentialing.jsonl` — 35 records, claim IDs H02-E1…E35. Carried records marked CARRIED with original scout IDs and Manager-1 verification status; fresh records fetched 2026-08-27.

| ID | Type | Anchor claim | Source |
|---|---|---|---|
| E1 | forum (fresh) | "Every panel has its own credentialing forms… lost my paperwork or sat on it for three months" | r/therapists 1vx21do, 2026-08-24 |
| E2 | forum (fresh) | Counter-signal: "Once you're set up it's fine" — solo pain is front-loaded | same thread, top comment |
| E3 | forum (fresh) | Service failure: Intelix — 6 months, no movement, refunded | r/therapists 1vyyoq1, 2026-08-26 |
| E4–E6 | forum (carried, re-verified) | Humana conflicting answers; UHC resubmit loop; freelance CAQH labor market | r/CodingandBilling, Jul–Aug 2026 |
| E7 | official (carried) | Nevada: 6–9-month credentialing delays | ppc.nv.gov |
| E8 | forum (fresh) | New NPI triggers dozens of daily service spam calls — market density + trigger moment | r/therapists 1vy8xia |
| E9 | guide (carried) | DIY workflow + platform-independence motive | matthewryanlcsw.substack.com |
| E10–E13 | pricing (carried) | $100–300/app; $1,500–3,500 initial; $150–500 range; $8–30k+/mo enrollment gap | Medwave, PPS, PayerReady |
| E11 | pricing (fresh) | $200–500/app; $600–2,400/yr maintenance; $6–8k/mo delay loss (2026) | medicotechllc.com |
| E14–E16 | jobs (E14 re-verified fresh) | QualDerm $48,152–64,916; Robert Half $43,750–57,000; 3,990 open postings | bebee, roberthalf |
| E17 | pricing (fresh) | Alma $125/mo; Headway 10–15%; panel belongs to platform on exit | therapydial.com |
| E18–E21 | vendor/reviews (fresh) | Medallion: quote-gated, $43M Aug-2025 + CredAlliance, 4.3/5 with self-service complaints; small practices advised to DIY | medallion.co, PRNewswire, SoftwareAdvice, GetPracticeHelp |
| E22–E23 | vendor/news (fresh) | Assured: $19M Jul-2026, agent tech, demo-gated, enterprise-targeted incl. its own therapist guide | GlobeNewswire, withassured.com |
| E24–E27 | vendor (fresh) | CertifyOS $40M B (plans/digital health); Verifiable $27M B (CVO); Modio CHG-owned mid-market; MedTrainer $20–50/user/mo | certifyos.com, verifiable.com, Preqin, medtrainer.com |
| E28 | official (fresh) | Availity OAA: bot/scraping prohibition, sole-discretion termination, VPN policing | Availity_OAA.pdf |
| E29–E30 | official (fresh) | CAQH Practice Administrator delegation; CMS I&A third-party surrogacy for PECOS | dataspring.com, Noridian |
| E31 | vendor (fresh) | PECOS 2.0 late-2025: mandatory MFA, stricter revocation, 2026 migration | payerready.com |
| E32 | official (fresh) | NSA 90-day directory verification → quarterly DirectAssure re-attestation, removal for non-response | bcbsks.com |
| E33–E34 | vendor/official (fresh) | UHC Onboard Pro CAQH integration; CAQH scale 4.8M records/~1,000 plans/50 states | uhcprovider.com, caqh.org |
| E35 | forum (fresh) | NPPES new-practice digest: "a new practice picks its billing/credentialing partner in its first few weeks" | r/CodingandBilling 1vcs0q0 |
