# Manager 1 — Demand Signals: Promotion Memo (Wave 1 → Wave 2)

**Author:** Manager 1 (Demand Signals) · **Date:** 2026-08-27
**Inputs:** 12 scout files (`outputs/signals/01…12`), 467 evidence records (`outputs/evidence/s01…s12.jsonl`, all schema-valid), spot-verification of 21 cited sources.
**Disposition of 87 candidates:** 38 contributing to 18 promoted hypotheses · 45 parked with reasons · 4 killed (3 evidence-bar/anti-pattern kills + 1 scout-filed negative finding confirmed).

---

## 1. QC summary and spot-verification results

Method: every candidate was checked against the SCOUT_BRIEF bar (3+ independent pain artifacts, frequency, economics, current-solution inventory). I then re-fetched the strongest claim of each ground and the claims that looked too convenient. WebSearch budget was exhausted program-wide, so all verification was WebFetch/curl of cited URLs, plus the Arctic Shift Reddit archive API (the working path scout 05 documented) for Reddit-anchored claims.

**Verification table (21 checks, all 12 grounds):**

| Ground | Claim re-checked | Result |
|---|---|---|
| 01 | Intuit official: QBD 2023 services die 2026-05-31 | VERIFIED verbatim on official policy page |
| 01 | Brady Martz Feb-2026 price table (Pro $999→$1,149; Premier $1,399→$1,609; Enterprise $1,703→$1,873; Payroll $550→$640; ACH $5→$10) | VERIFIED — all figures exact. **Flag:** the "Oct 1, 2026 second wave" and "Desktop 2024 dies 2027-09-30 / last version ever" claims are NOT on the two cited pages — treat as unverified narrative; Wave 2 must source or drop them |
| 02 | GOV.UK "864,000 sole traders and landlords… 6 April 2026" | VERIFIED (headline 864k / body "more than 860,000", £50k threshold, quarterly updates) |
| 02 | Marosa e-invoicing country dates (BE live Jan 2026 via Peppol; PL Feb/Apr 2026; FR Sep 2026; DE 2025/2027/2028) | VERIFIED — all dates as claimed |
| 02/11 | Accessible.org price list ($100–250/primary page; $1,250–2,750 typical; VPAT $350; EN 301 549 $650; PDF $7.50/pg; $195/hr) | VERIFIED — exact |
| 03/05/11 | AMA 2025 PA survey (40 PAs/wk; 13 hrs/wk; 40% dedicated staff; 94% burnout; 95% delays care; 74% denials up) | VERIFIED — exact, release 2026-05-13. Note 94% (burnout) and 95% (delays) are separate stats; both scouts quoted them correctly |
| 03 | bebee count 6,971 prior-auth-specialist postings | VERIFIED — exact count renders |
| 04 | Trustpilot ServiceTitan ETF quotes ($22,000 John Heger 2026-07-13; $37,000 Brian J 2026-06-15) | VERIFIED verbatim. (Overall page shows 3.9/409 — scouts cited only the 1–2★ cohort, no misquote) |
| 05 | r/InsuranceAgent COI post (veemaximus, 1tq8k1o) via Arctic Shift | VERIFIED verbatim (bottleneck / failed VA / payroll-math text matches) |
| 05/11 | Medwave credentialing prices ($100–300/payer/provider; $1,500–3,500 initial; 90–120 days; ~$120k delay example) | VERIFIED — exact |
| 06 | Stenberg "Death by a thousand slops" (20% slop; 5% valid; 3–4 people × 30min–3h; "Times eight the last week") | VERIFIED — exact |
| 06 | Gibson Dunn omnibus re-dating (Annex III → 2027-12-02; Annex I → 2028-08-02; Art. 50 live 2026-08-02, watermark grace to 2026-12-02) | VERIFIED — exact. Scout 06's re-dating stands |
| 07 | Microsoft SMTP-AUTH deprecation timeline page | NOT VERIFIABLE — page is JS-walled to fetcher (not dead). Date corroborated only by the MSP practitioner artifact. S07-3 is parked anyway |
| 07 | ECOM CPA payout-reconciliation article ($22k gross→$14k net; "nine ways simultaneously"; largest source of misstatement) | VERIFIED — exact. (TikTok tool-gap claim belongs to the other two artifacts, correctly attributed) |
| 08 | r/CodingandBilling 2026 "technical denials" thread (1rkfa6b) via Arctic Shift | VERIFIED — title/sub/2026 date/substance match (archive score 22 vs quoted 30 — mirror lag, scout disclosed) |
| 08 | r/Construction retainage thread (1uehqtf) | **DISCREPANCY:** archive selftext reads "about $50 sitting out there" — the "$50k" in scout 08's quote is an inserted interpretation (contextually plausible, but not the poster's literal text). Artifact S08-1-E1 downgraded; H07 economics now rest on E2/E4/E5/E6, which hold |
| 08 | r/msp Pax8 reconciliation thread (1b9r46c, PatD442, 2024-03) | VERIFIED verbatim |
| 09 | CBT News CDK settlement ($630M, 243-company vendor class; $100M dealer settlement) | VERIFIED — exact |
| 10 | Capterra HHAeXchange (3.6/5, 100 reviews; $18,000 syntax-error loss; 4-month non-payment; unpaid shifts; 3-hr holds) | VERIFIED — all five quotes verbatim |
| 11 | FTC accessiBe $1M order (widget "did not make all user websites WCAG-compliant") | VERIFIED — exact, 2025-01-03 |
| 11 | Moving Authority DOT pricing ($50–100 / $100–250 per driver/mo; 5-truck $500–1,250/mo; setup $500–2,000) | VERIFIED — exact |
| 12 | JVA uncollected-payments (10–12% of revenue; $20k on $200k; 3–5% reserve) | VERIFIED — exact; revision date 2026-07-06 confirmed (original 2018 — scout disclosed) |
| 12 | Trustpilot TeamSnap 1.1/5, 692 reviews | VERIFIED — exact |

**No dead URLs. No fabrications found.** Two narrative sub-claims flagged (Intuit 2027 date + Oct-2026 wave), one quote-transcription embellishment caught and downgraded ($50k retainage). Overall the scout org's evidence discipline was high; scouts disclosed their own weaknesses (blocked sources, dated artifacts, vendor-sourced figures) accurately in every file I checked.

### Per-scout QC notes

- **Scout 01 (orphaned customers):** Bar met on all 7. Strongest claims verified (Intuit date, Brady Martz table). Flags: S01-1's "Sept 30, 2027 / last version" and "Oct 2026 second wave" unverified on cited sources (Wave 2 to source or drop). S01-4's official EOS page is JS-walled (search-index capture disclosed). Honest negative findings (Vertafore/Covetrus/Eyefinity rumors) recorded to standing negative knowledge. No kills.
- **Scout 02 (regulatory deadlines):** Exemplary kill discipline in-flight (FinCEN RRE vacated; EUDR postponed — both dropped) and the deadline-credibility lesson (UK/EU-e-invoicing/card dates held; US federal & EU-green slipped) is adopted as this memo's grading standard. All 8 met the bar; strongest claims verified. No kills; 5 of 8 parked on opportunity (not evidence) grounds.
- **Scout 03 (human-middleware jobs):** Bar met on all 8 with employer-published wages as budget proof — the cleanest economics in the sweep; 6,971-count spot-verified exactly. Weakness disclosed: zero worker-side threads (Reddit blocked); Wave 2 must add operator/worker voice. No kills.
- **Scout 04 (vertical SMB complaints):** Bar met on all 7; ServiceTitan dollar quotes verified verbatim. But 6 of 7 candidates are one phenomenon (PE/public-market monetization of lock-in) where escape routes already exist — pain, not white space. All 7 parked; the pattern feeds clusters C2/C5 and the club/nonprofit hypotheses. Auto repair honestly reported as inaccessible, not dry. Re-run recommended (see §6).
- **Scout 05 (back-office pros):** Best primary-source craft of the wave (Arctic Shift permalinks all check out; COI artifact verbatim). Bar met on all 8. Self-disclosed vendor-sourced economics in S05-8 handled by demoting it to secondary evidence within H11. No kills.
- **Scout 06 (AI-created work):** Bar met; the two re-datings verified exactly (Gibson Dunn). S06-4 is a model negative finding — confirmed and recorded: **no bias-audit-SaaS hypothesis may be promoted in this program without new enforcement evidence.** 7 of 8 parked on crowding/hostage/budget-less-buyer grounds.
- **Scout 07 (platform shifts):** Bar met on all 7; ECOM CPA anchor verified. This ground contributed the sweep's most valuable *pricing* evidence (coping-service price lists) and zero promotions — three candidates are severe/extreme platform hostages (hard gate), two sit in crowded funded categories, and the scout disclosed vendor-adjacent sourcing honestly. S07-4 is first-reserve (see §5).
- **Scout 08 (money friction):** Bar met on all 7; two anchors verified verbatim; one quote embellishment caught (S08-1-E1 "$50k" → archive reads "$50") — artifact downgraded, candidate stands. Dropped cross-border contractors correctly (astroturfed, funded) — recorded as negative knowledge.
- **Scout 09 (legacy lock-in):** $630M/$100M/court-record chain verified. S09-7 KILLED (freshest first-person artifact 2022; buyer = government procurement, an anti-pattern the scout itself flagged). Remaining 6 parked — every one carries a gatekeeper/blocker risk where the pain-causer controls the surface a product would need. Ground under-sampled (pharmacy dry; forums blocked); re-run recommended with Arctic Shift toolkit.
- **Scout 10 (category-gap analytics):** Bar met on 5 promoted-in candidates; HHAeXchange quotes verified verbatim. The killed-category table is adopted as standing negative knowledge (do not re-litigate the 10 categories without new evidence). S10-4 parked with a re-hunt note (single-platform evidence; scout honestly refused to claim an OfficeMate EOL it couldn't verify).
- **Scout 11 (services-to-software):** Strong per-unit price evidence; FTC/pricing/AMA anchors verified. S11-7 KILLED (zero operator-voice pain artifacts — regulator text + vendor price list + enforcement analysis does not meet the brief's three-pain-artifact intent; re-huntable). UPL gate on immigration prep and the demoted RFP category confirmed as negative knowledge. Bench framing (services collapse must answer "why do agents change the math") is adopted as a required Wave-2 question for H17 and all services-collapse hypotheses.
- **Scout 12 (founder arena):** No home-turf charity detected — JVA and TeamSnap anchors verified exactly, weak veins (parent comms, coach payroll) honestly withheld. S12-8 KILLED (one independent pain artifact — below bar; scout itself said "reported for completeness, not promotion"). S12-6/S12-7 parked as dated/moderate; their evidence folds into H18/H12.

### Kills (evidence-bar / anti-pattern failures)
1. **S09-7 (gov permitting):** stale artifacts (2016–2022), unreachable buyer (government procurement). Contractor-side context preserved inside C2 notes only.
2. **S11-7 (I-9 compliance):** no operator-voice pain artifact at all; enforcement-triggered (probabilistic) forcing. Re-huntable if Wave 2 finds employer threads + audit-volume data.
3. **S12-8 (Facilitron gym access):** single independent complaint artifact; binding constraint is physical scarcity, not software.
4. **S06-4 (US employment-AI bias audits):** the scout's own negative finding, confirmed — statutes ignored in practice (2 complaints in 2 years; Colorado gutted). Recorded as a standing DO-NOT-BUILD.

### Standing negative knowledge (binding on Wave 2 — do not resurface)
- Scout 10's killed-category table (HOA, pest control, campgrounds, consignment, self-storage, mental-health group PM, auctions, funeral homes, machine-shop ERP, portable sanitation).
- Scout 01's disproven sunset rumors: Vertafore QQCatalyst, Covetrus ImproMed, Eyefinity OfficeMate.
- Scout 02's in-flight kills: FinCEN Residential RE rule (vacated 2026-03-19), EUDR (re-postponed, SMB obligation shrunk).
- Scout 06: bias-audit SaaS (S06-4); EU AI Act Aug-2026 high-risk deadline no longer exists (now Dec 2027 / Aug 2028); Colorado AI Act repealed-and-replaced.
- Scout 08: cross-border contractor payments (vendor-saturated, funded).
- Scout 11: RFP/bid response (funded incumbents, unverifiable economics); immigration form prep (UPL hard gate).

---

## 2. Cluster map (cross-ground convergence)

Convergence from independent hunting directions is treated as a positive signal and is recorded per hypothesis in §3.

| # | Cluster | Contributing S-IDs (ground count) |
|---|---|---|
| C1 | **Healthcare revenue-cycle middleware** — eligibility → prior auth → credentialing → claims/denials → EVV: portal↔EHR human bridging with payer-AI escalating the asymmetry | S03-1/2/3/4/8, S05-2/3/4, S08-2/3, S10-5, S11-2/3 (5 grounds: 03,05,08,10,11) — the sweep's largest single concentration |
| C2 | **Vertical-SMB PE/rollup monetization & lock-in** — auto-renew + ETF + fee unbundling + processor steering + integration tolls | S01-1/2/3/5, S04-1…7, S09-1/2/6, S10-1/2/3, S12-1 (5 grounds: 01,04,09,10,12) — mostly pain-not-opportunity except where no refuge exists (H13, H14, H15) |
| C3 | **Compliance deadline waves that held** — statutory per-event workflows SMBs demonstrably fail | S02-1/3/4/5/6/8, S11-1/5 (+suspended S02-7; deferred S06-3) (3 grounds: 02,06,11) |
| C4 | **Money that moves late/opaquely** — settlements, commissions, retainage, dues, disputes reconciled by hand | S07-1/4, S08-1/4/5/6/7, S05-8, S12-1/2 (4 grounds: 05,07,08,12) |
| C5 | **Club/academy/membership money layer** — registration funds held, dues leakage, fee stacking on volunteer-run orgs | S12-1/2/7, S10-3, S04-3/7 (pattern), S08-4 (horizontal) (4 grounds: 04,08,10,12) |
| C6 | **Human-middleware portal labor (non-healthcare)** — external portal ↔ internal system re-keying with published wages | S03-5/6/7, S05-5/6, S07-7 (3 grounds) |
| C7 | **Forced migrations / dated sunsets** | S01-1/2/4, S09-4/5, S02-3 (adjacent) (3 grounds: 01,02,09) |
| C8 | **Usage/license reconciliation** — MSP seat-billing vs SaaS AI-COGS variants (scored as alternatives, per scout 08) | S08-6, S08-7, S07-4 (settlement variant) (2 grounds) |
| C9 | **AI-created work & AI-proof demands** — slop cleanup, fake candidates, questionnaires, agent oversight | S06-2/5/6/7/8, S07-2 (2 grounds) |
| C10 | **Platform-hostage enforcement events** — bans/suspensions/policy flips with no API surface | S07-1/5/6, S09-1 (quasi), S12-8 (2 grounds) — hard-gate territory |

---

## 3. Promoted opportunity hypotheses (ranked)

Format per manager brief. **FF credibility grades** apply scout 02's lesson: **A** = in force or a held-date regime (UK statutory, EU e-invoicing/EAA, money-movement gates, federal mandates already operating); **B** = dated but with slip/whiplash risk (vendor sunsets, US federal future dates, new institutions); **C** = demonstrated-unstable regimes (none promoted on C).

---

### H01 — Denial & Underpayment Defense for Small Practices ("RCM defense desk") — RANK 1 ★TOP-5
- **Buyer job:** When a 1–12-provider practice or micro billing company needs to turn payer denials, auto-downcodes, and silent underpayments back into revenue, current solutions fail because scrubbers/clearinghouses don't catch 2026-era algorithmic edits and the rework is portal archaeology done by 1–2 exhausted humans, causing ~$57/claim rework on ~15% of claims, 60+ day AR piles, and write-offs of money legally forfeited at appeal deadlines.
- **Contributing (3 grounds):** S05-2, S08-2, S03-2, S08-3, S03-1. Strongest evidence: BCBS/HCSC blanket AI downcoding thread + Anthem "unable to explain the pricing difference" (r/CodingandBilling, Jul 2026, verified via Arctic Shift); Premier: $57.23/claim rework, ~70% of denials overturned = pure rework; Experian 2025: 41% say ≥1-in-10 denied, half still manual; Catholic Health $24–31/hr follow-up postings; 4–7%-of-collections outsourcing.
- **Forcing function: YES (A)** — the practice's own revenue is gated per claim; timely-filing/appeal windows are hard, self-enforcing deadlines. Payer-side AI (2026 payment-integrity edits) is escalating volume — an arms race, not a fading pain.
- **Wave 2 must verify/falsify:** (1) why Waystar/Availity/EHR denial modules don't reach the 1–12-provider tier (price? implementation weight? portal coverage?) — name the real current stack per segment; (2) WTP shape (% of recovered vs seat) against 4–7% outsourcing; (3) worker/practice-owner voice beyond r/CodingandBilling; (4) falsify if payer portals contractually/technically block automated status+resubmission at small scale (Availity ToS), or if 2026 denial spike is transient.

### H02 — Provider Credentialing & Enrollment Autopilot — RANK 2 ★TOP-5
- **Buyer job:** When a small practice, therapy group, or billing company needs a new provider enrolled with 5–15 payers, current solutions fail because it's a 90–180-day black box of CAQH upkeep, per-payer portals, and conflicting phone answers, causing $100–300/payer/provider service fees, $43–57k specialist salaries, and $6k–30k+/month of parked billings per waiting provider.
- **Contributing (3 grounds):** S03-4, S05-4, S11-2. Strongest evidence: Medwave price list verified exact ($100–300/payer, $1,500–3,500 initial, 90–120 days, ~$120k delay example); Nevada state doc: 6–9-month delays (official); 3,990 open credentialing-specialist postings with named portal trio (CAQH/PECOS/PAVE); Humana conflicting-answers thread (2026-07).
- **Forcing function: YES (A)** — cannot bill until enrolled (money gate); CAQH re-attestation ~120 days; recredentialing every 2–3 years; lapse = denials.
- **Wave 2 must verify/falsify:** (1) segment boundary vs Medallion/Verifiable/CertifyOS (they sell to systems/digital health — confirm the 2-provider practice and the credentialing-services firms themselves are truly unserved); (2) whether payer portals/CAQH permit agentic operation (ToS, MFA walls) — this is the technical moat question; (3) unit economics of "credentialing firm in software" (per-app pricing implies clean per-unit revenue); (4) falsify if CAQH/payer API programs are about to disintermediate (check CAQH roadmap).

### H03 — Prior-Auth Production Line for Small Specialty Practices — RANK 3 ★TOP-5
- **Buyer job:** When a PA-heavy small practice (imaging, oncology, derm, GI, behavioral) needs ~40 auths/physician/week submitted, tracked, and defended, current solutions fail because ePA platforms sell to payers/systems while practices run portals+fax+phone with dedicated staff, causing 13 hrs/wk of physician+staff time, $5–15/request outsourcing or ~⅓ FTE per physician, plus auth-related downstream denials (10.4% of denials were pre-approved).
- **Contributing (3 grounds):** S03-3, S05-3, S11-3. Strongest evidence: AMA 2025 survey verified exact (40/wk; 13 hrs; 40% dedicated staff; 94% burnout); 6,971 open PA-specialist postings verified exact; staffer verbatim: "the prep is where the day goes… chasing a rendering provider for a note… almost none of that is the actual authorization step."
- **Forcing function: YES (A on the money gate; B on the regulatory clock)** — no auth, no revenue (always-on); CMS-0057-F decision windows live Jan 2026 and FHIR PA APIs due Jan 2027 are US-federal future dates: no slip yet, but grade B per the deadline-credibility lesson. The pain stands even if the API date slips.
- **Wave 2 must verify/falsify:** (1) crowding — map funded ePA startups converging on the 2027 API and show a segment (small specialty + DME) they structurally miss, or kill; (2) the wedge is evidence ASSEMBLY (notes/labs chasing per the staffer artifact), not form submission — validate that framing with 5+ practice interviews; (3) EHR access at small practices (can an agent read the chart?); (4) falsify if payer APIs + EHR-native ePA make third-party tooling redundant by 2027.

### H04 — MTD ITSA Practice-Side Onboarding & Quarterly-Chase Layer — RANK 4 ★TOP-5
- **Buyer job:** When a UK accounting practice must convert hundreds of non-digital sole-trader/landlord clients to quarterly digital filing, current solutions fail because MTD software handles the filing but not the client-by-client onboarding, chasing, and 5×/year deadline management (42% of accountants say >half their clients submit nothing digitally), causing £250–400/client/yr of new service work the practice can't staff — across 864k mandated taxpayers now and ~2.9M by 2028, with half of wave 1 unregistered at the first deadline.
- **Contributing (1 ground, exceptional depth):** S02-5. Strongest evidence: GOV.UK 864k/6-April-2026 verified exact; Property118 "half unregistered as deadline passes" (2026-08-11); HMRC auto-sign-up began Aug 2026; Xero practice-pricing guide (£250–400 uplift); software true-cost dataset (£0–288/yr).
- **Forcing function: YES (A)** — UK statutory regime in force with points-based penalties; the held-date regime class; waves 2027 (>£30k) and 2028 (≥£20k) triple the market on legislated dates.
- **Wave 2 must verify/falsify:** (1) whether practice-management incumbents (TaxCalc/BTC/IRIS/Xero HQ) are already shipping the onboarding/chase layer — name gaps or kill; (2) buyer = practice (B2B) vs direct-to-landlord (B2C) — evidence favors practice; (3) UK distribution for a non-UK founder (falsifier: channel requires UK accounting-body presence); (4) unit economics at £10–30/client/mo against the £250–400 service uplift.

### H05 — Accessibility Conformance Factory (EAA + ADA + VPAT) — RANK 5 ★TOP-5
- **Buyer job:** When an SMB e-commerce/SaaS business must prove WCAG conformance (EAA scope, US demand letter, or procurement VPAT), current solutions fail because real audits are hand-priced per page ($100–250) by consultancies, overlays were federally discredited (FTC: accessiBe $1M), and scanners stop at ~30–40% of criteria, causing $1,250–2,750+ per audit engagement, repeat-lawsuit exposure (46% of federal suits hit repeat defendants), and stalled deals awaiting VPATs.
- **Contributing (2 grounds, independent directions):** S02-1 (deadline hunt), S11-5 (services-collapse hunt). Strongest evidence: Accessible.org price list verified exact; FTC order verified exact; 5,000+ suits/35–50k demand letters (2025); EAA in application since 2025-06-28 with French suits from Nov 2025 and spring-2026 audit prioritization.
- **Forcing function: YES (A)** — EAA is live (held EU date) with member-state fines; US private-litigation machine is continuous; procurement gates are money-movement. Double-jurisdiction redundancy protects the thesis if either side weakens.
- **Wave 2 must verify/falsify:** (1) the audit-work quality bar — can agents + human reviewer hit consultancy-grade findings (manual-review criteria) at 10x lower cost, with a licensed/insured sign-off structure? Prototype-level proof required; (2) competitive scan of audit-automation entrants (this will be crowded — find the segmentation, e.g., SMBs hit by demand letters + Shopify-class merchants in EAA scope); (3) whether EU enforcement against non-EU SMBs is real or theoretical (falsifier for half the market); (4) buyer-side WTP at $500–1,500/engagement via demand-letter recipients.

### H06 — EU E-Invoicing Onboarding for SMEs & Freelancers — RANK 6
- **Buyer job:** When a Belgian/Polish/French/German SME or freelancer must issue structured e-invoices through Peppol/KSeF/PDPs to get paid at all, current solutions fail because accounting suites are country-gapped and access points are priced/technical (€2,000/yr direct membership; certification), causing forced paid subscriptions replacing free email invoicing, validation-rejection rework, and — in clearance models — invoices that legally don't exist until accepted.
- **Contributing (1 ground):** S02-3. Strongest evidence: Marosa country-date table verified exact; HN Peppol thread verbatims ("2000 euros just for the peppol membership…"); Belgium adoption gap (~⅓ of SMEs vs 70% large firms); France removed the free public platform.
- **Forcing function: YES (A)** — per-invoice statutory compulsion, the highest-frequency forcing function in the sweep; the EU e-invoicing date regime held in 2025–26 (BE already live; PL Feb/Apr 2026 live; FR Sep 2026 next).
- **Wave 2 must verify/falsify:** (1) crowding is the kill risk: every EU accounting vendor + access-point providers (Storecove-class) are racing — the promotable slice must be proven (candidates: non-domestic sellers into mandate countries; freelancers below accounting-suite fit; vertical SaaS needing embedded compliance); (2) access-point economics (can a founder resell/ride an AP at margin?); (3) FR Sep-2026 readiness evidence — a live scramble would be the entry event; (4) falsify if national free tools (like PL KSeF's) are good enough for micro-sellers.

### H07 — Subcontractor Payment-Chain Ops (pay apps, lien waivers, retainage) — RANK 7
- **Buyer job:** When a commercial sub ($0.5–20M revenue) must get paid — monthly G702/G703 pay apps formatted per GC, waiver exchanges up and down the chain, retainage recovery, statutory lien deadlines — current solutions fail because tools cover fragments (Levelset = notices at $59/each; GC portals serve the GC; Excel for the rest), causing 55–120-day cash cycles, retainage frozen for months-to-years, $10k–55k legal fees when it breaks, and a $47k billing clerk to run it.
- **Contributing (2 grounds):** S03-7, S08-1. Strongest evidence: Vaco $62–65k posting "100–200 invoices per billing cycle" (AIA/NetSuite); Levelset $59/notice pricing (verified path); millwork sub 55-day-gap thread with "paid when paid… 60–90 days and there's no budging"; Rabbet 5–10 hrs/person/wk. (Note: the "$50k retainage" quote was downgraded in QC — archive reads "$50"; the thread's pain narrative stands, the dollar figure does not.)
- **Forcing function: YES (A)** — contractual monthly billing cutoffs (miss = slip a full month) + statutory lien/notice windows (miss = lose the right).
- **Wave 2 must verify/falsify:** (1) head-on check vs Siteline/Flashtract and Procore/Levelset roadmaps — is sub-side multi-GC-portal submission genuinely unowned?; (2) verified retainage dollar magnitudes (replace the downgraded artifact with 3+ sourced figures); (3) trade-vertical entry (electrical/mechanical subs via associations?) and willingness to pay vs the billing-clerk salary; (4) falsify if GC-portal ToS/API absence blocks automated submission.

### H08 — Small-Carrier DOT/FMCSA Compliance Autopilot — RANK 8
- **Buyer job:** When a 1–20-truck carrier must maintain authority (BOC-3, UCR, MCS-150, quarterly IFTA, DQ files, Clearinghouse, drug consortium) and survive the month-1–12 new-entrant audit, current solutions fail because J.J. Keller/Foley-class services are human subscriptions ($50–250/driver/mo) and the DIY path is confusing enough that $95–170 scam mills thrive, causing four-figure monthly service spend per small fleet or authority-ending audit failures.
- **Contributing (1 ground):** S11-1. Strongest evidence: Moving Authority price list verified exact; Foley's own testimonial ("cuts the time… in half" — half remains); FMCSA identity re-verification (~800k registrants) + Motus migration (legacy retired 2026-05-14) creating a 2026 upheaval cohort.
- **Forcing function: YES (A)** — federal filing calendar with out-of-service/revocation consequences, in force now; the audit is automatic-fail on missing paper. (Motus dates are already executed, not promises.)
- **Wave 2 must verify/falsify:** (1) refresh operator-voice artifacts to 2025–26 (scout's forum quotes are 2020; TruckersReport fetchable) — confirm the pain survived the FMCSA fraud crackdown; (2) J.J. Keller/Foley pricing-and-gap teardown (why hasn't this been productized down-market? churn? trust?); (3) reachable channel test (dispatcher networks, insurance agents, factoring companies as distribution); (4) falsify if new-authority volume collapse (halved in 2025) shrinks the entry cohort that buys first.

### H09 — Home-Care Agency EVV Survival Layer (+ referral intake) — RANK 9
- **Buyer job:** When a small Medicaid home-care agency must get every visit verified through a state-mandated aggregator (HHAeXchange-class) before it can bill or pay caregivers, current solutions fail because the mandated portal is 3.6★ with unconfirmed visits and vanished shifts and agency-side systems compete on breadth rather than making the pipe survivable, causing $18k single-incident losses, 4-month payment gaps, unpaid caregivers, and a coordinator reconciling every visit by hand.
- **Contributing (2 grounds):** S10-5, S03-8. Strongest evidence: five Capterra operator quotes verified verbatim (incl. $18k syntax-error loss); TMHP/Texas state-designation page; intake postings $58–60k with fax/portal→EMR re-keying duties (623 postings).
- **Forcing function: YES (A)** — 21st Century Cures EVV mandate in force; unverified visits are unpaid; state aggregator designations make the broken pipe unavoidable.
- **Wave 2 must verify/falsify:** (1) the aggregator itself is undisplaceable — validate the reconciliation/pre-flight layer wedge (scheduling↔EVV↔claims match before submission); (2) whether AxisCare/WellSky/AlayaCare have shipped real EVV-reconciliation (kill if solved); (3) state-by-state beachhead pick (TX/PA evidence strongest); (4) agency WTP given thin Medicaid margins — find the $/visit tolerance; (5) HHAeXchange API/export surface (platform-dependency check — the state relationship, not the vendor's goodwill, is the mitigant to verify).

### H10 — Client Document-Chase Autopilot for Tax & Bookkeeping Firms — RANK 10
- **Buyer job:** When a solo/small tax or bookkeeping firm must collect documents and signatures from hundreds of clients against statutory deadlines, current solutions fail because portals blast reminders that clients ignore while what's needed is judgment ("read the return-in-progress, know what's missing, chase with context"), causing unbillable admin burning $182/hr capacity, capped client books, and deadline-week crunches — while the firm already pays $74–149/user/mo for portals it hates.
- **Contributing (2 grounds):** S05-1 (+S01-3 as budget/channel evidence: the Drake cohort — verified TaxProTalk/Trustpilot/Capterra complaint chain — is the same buyer, newly shopping). Strongest evidence: six independent practitioner threads 2025–26 (Arctic Shift permalinks); NATP $182/hr; Canopy price card; TaxCaddy-wrecked refugees.
- **Forcing function: YES (A)** — Apr 15 / Mar 15 / Sep–Oct statutory deadlines every year; penalties/malpractice exposure downstream.
- **Wave 2 must verify/falsify:** (1) the crowding problem is acute (scout: 5+ mod-removed builder posts in r/Bookkeeping in Jul–Aug 2026 alone; TaxDome/Canopy/Liscio incumbents) — Wave 2 must define a differentiation that survives ("reads the workpapers, chases with judgment" vs reminder blasts) or kill; (2) seasonal-revenue shape (does the firm pay year-round?); (3) integration reality with TaxDome/Drake/Lacerte workpapers; (4) falsify via 10 practitioner interviews on switching appetite from bundled portals.

### H11 — Insurance Agency Service-Desk Automation (COI issuance wedge; commission recon expansion) — RANK 11
- **Buyer job:** When an independent P&C agency's service team must push out same-day certificates of insurance (and monthly, reconcile carrier commission statements), current solutions fail because AMS cert modules still leave a manual queue (and holder-side COI SaaS serves the other party), causing a dedicated $40–55k cert role or failed VA experiments, Patra outsourcing line items, and silent commission short-pays nobody can verify.
- **Contributing (2 grounds):** S05-5, S05-8 (secondary), S10-1 (environment: AMS duopoly squeeze — verified price/contract evidence). Strongest evidence: veemaximus COI post verified verbatim (pain + failed VA + payroll math in one artifact); Patra selling Certificate Processing and Commission Posting as paid services; AMS360/EZLynx review economics ($150–300/user/mo; 50% hike).
- **Forcing function: YES-WEAK (A on money-adjacency)** — contractors can't start jobs without certs (same-day contractual expectation); commissions are the agency's own revenue; no regulator. Graded honestly as money-movement-adjacent, not statutory.
- **Wave 2 must verify/falsify:** (1) breadth of the COI-issuance pain beyond the anchor artifact (pull 10+ agency threads/interviews — scout disclosed thinness); (2) AMS integration surface (Epic/AMS360/HawkSoft APIs vs screen-work); (3) commission-recon window check — Applied Recon shipped and Comulate is funded; confirm the small-agency tier remains unserved or drop that expansion; (4) WTP vs the $40–55k role and Patra's per-item pricing.

### H12 — Club & Academy Money Layer (registration funds, dues AR, fee transparency) — RANK 12
- **Buyer job:** When a competitive youth club ($100k–3M revenue) must collect $1,500–5,900/athlete in installments and actually receive its registration money, current solutions fail because the dominant platforms (1.1★ TeamSnap / 1.11★ SportsEngine) hold funds, stack fees (3.25% + $2/installment), and ship no real dunning/plan tooling, causing 10–12% of revenue never collected (JVA, verified), $5k–20k+ locked in processor holds, and volunteer treasurers running Zelle-and-spreadsheet AR.
- **Contributing (3 grounds):** S12-1, S12-2, S10-3 (membership-org variant), pattern support S04-3/S04-7, S08-4 (horizontal AR evidence). Strongest evidence: JVA 10–12% verified exact; TeamSnap 1.1/692 verified exact; SportsEngine fee-formula help doc; BBB fund-hold complaint ($5k locked/$20k AR).
- **Forcing function: YES-WEAK (money movement)** — every season's registration IS a payment event and in-season installments fund coach pay/rent; no regulator. Founder-domain distribution (Division 1 Academy network, club directors, JVA-class associations) is the differentiating asset per program rule 4.
- **Wave 2 must verify/falsify:** (1) displacement math vs staying on SportsEngine/TeamSnap + adding a payments layer (can the money layer land WITHOUT replatforming registration? if full replacement is required, weigh against funded PlayMetrics/LeagueApps/Bound); (2) processing economics (the fee stack IS the incumbent revenue — price the wedge honestly); (3) 10 club-director interviews from the founder's network on fund-holds and delinquency (fastest validation loop in the program); (4) falsify if delinquency is a family-hardship problem software dunning can't move.

### H13 — Trust-Accounting-That-Works for Solo/Small Law Firms — RANK 13
- **Buyer job:** When a solo/small firm must keep IOLTA client ledgers with monthly three-way reconciliation under bar audit rules (and PCLaw/Advantage refugees must land somewhere), current solutions fail because QuickBooks doesn't understand trust/PI accounting and Clio's accounting confuses even motivated solos, causing discipline/disbarment exposure (random bar audits), $45–57k billing-specialist salaries, and ~2.4 of 8 working hours becoming cash.
- **Contributing (2 grounds):** S05-7, S01-4. Strongest evidence: four independent 2026 r/LawFirm threads (IOLTA confusion; QBO failing PI; 30-lawyer PCLaw exit; Advantage exit); NC State Bar random-audit program (regulator); PCLaw EOS passed 2025-12-31 with a stranded base deciding now; LEAP $165/user/mo + $4,000 data-export toll.
- **Forcing function: YES (A)** — bar trust rules in force with random audits (enforcement-lottery-shaped, honestly noted); the PCLaw/Time Matters support cliff already fell (dated, executed).
- **Wave 2 must verify/falsify:** (1) incumbent-extension risk is the kill question: Clio/Smokeball/CARET are adding accounting — find the durable wedge (trust-only companion vs full PM) or kill; (2) size the PCLaw/Advantage refugee cohort (claimed 15k firms/130k users — verify); (3) malpractice-carrier/bar-association channels as distribution; (4) falsify if TrustBooks/LeanLaw already own "trust-only for solos" (scout named them — teardown required).

### H14 — MSP License & Usage Billing Reconciliation — RANK 14
- **Buyer job:** When an MSP must reconcile what distributors (Pax8/TD Synnex) bill it against what its PSA bills clients each month, current solutions fail because syncs drift (credits never sync, mid-cycle seat changes, NCE annual-vs-monthly mixes) and existing tools choke or partially cover, causing "a few thousand here and there" of silent monthly leakage per shop, owner evenings on line-by-line reconciliation ("a few thousand line items… there's simply no way"), and 6x billing surprises.
- **Contributing (2 grounds):** S08-6 (+S04-6 context: Kaseya-class contract/billing chaos radicalizing the same buyer). Strongest evidence: Pax8 thread verified verbatim; Gradient MSP "couldn't handle the size of our CW DB" + rebuild admission; 2026-08 6x-invoice thread.
- **Forcing function: YES (money movement, monthly, bidirectional)** — distributor auto-bills the MSP regardless; client invoices must go out; errors compound silently.
- **Wave 2 must verify/falsify:** (1) incumbent race: Gradient/CloudOlive/Rewst are shipping — the wedge must be the reconciliation+audit OUTCOME (found dollars) not another sync; validate outcome-pricing appetite (% of recovered leakage?); (2) PSA/distributor API depth for a newcomer; (3) size: does leakage scale with seats such that 200-endpoint shops pay $200–500/mo?; (4) falsify if Pax8's own tooling roadmap closes the drift at the source.

### H15 — Small-Nonprofit Donor-CRM Refuge (RE7 sunset + Bonterra squeeze) — RANK 15
- **Buyer job:** When a small nonprofit's development team must keep decades of donor history working while its vendor sunsets the product (Raiser's Edge Database View, summer 2027) or guts support and raises prices post-rollup (Bonterra/NFG), current solutions fail because NXT is "not a one-to-one replacement," migrations risk decades of gift data, and the affordable alternatives require full conversions, causing forced five-figure re-platform decisions, auto-renew traps, and deleted donor records to dodge contact-tier pricing.
- **Contributing (2 grounds):** S01-2, S01-5 (+S10-3 adjacent for the volunteer-membership variant, primary-assigned to H12). Strongest evidence: Heller sunset notice (summer 2027, verified in ledger); 82%-negative pricing mentions across 418 Capterra reviews; named-role Bonterra quotes 2024–25 ("canceled our account without our consent… cut us off").
- **Forcing function: YES (B)** — vendor-announced sunset with a date (slip-capable; single-source announcement via Blackbaud's consultant channel — Wave 2 must confirm on Blackbaud's own notices) + annual auto-renew windows.
- **Wave 2 must verify/falsify:** (1) confirm the 2027 sunset from Blackbaud primary sources; (2) head-on check: Bloomerang/Little Green Light/Virtuous already harvest defectors — the wedge must be either migration-with-fidelity (queries/reports/mail routines preserved) or the RE7-power-user segment they fail; teardown required; (3) migration-services economics (Heller-class consulting prices = displacement target); (4) falsify if the RE7 base is too enterprise-skewed for solo-founder distribution.

### H16 — QuickBooks Desktop Terminal Wind-Down: Refuge/Continuity Wedge — RANK 16
- **Buyer job:** When a job-costing/inventory SMB (contractor, wholesaler, light manufacturer) or its accountant faces Desktop 2023's service death (2026-05-31, verified) and escalating stop-sold pricing, current solutions fail because QBO lacks Desktop feature parity ("incredibly buggy" per practitioners) and alternatives mean consultant-led conversions, causing four-figure annual price ratchets, forced mid-year workflow blowups, and a multi-million-file installed base with no like-for-like destination.
- **Contributing (1 ground; +S01-3 same-ecosystem corroboration):** S01-1. Strongest evidence: Intuit official discontinuation policy (verified); Brady Martz Feb-2026 price table (verified exact); multi-year TaxProTalk revolt.
- **Forcing function: YES (A on executed dates; B on the 2027 claim)** — May 31, 2026 already executed per policy page; the "Desktop 2024 = last version, dies Sep 2027" claim is plausible but was NOT verified on cited sources — Wave 2 must source it before any dossier leans on it.
- **Wave 2 must verify/falsify:** (1) THE WEDGE IS UNDEFINED — this is promoted on evidence quality with the explicit mandate to pick one testable wedge (vertical job-costing accounting for trades? migration/continuity tooling? hosted-Desktop + data-portability layer?) and kill the rest — a full horizontal accounting engine is out of 90-day scope; (2) source the 2024-version EOL date from Intuit primary material; (3) map where the base actually flees (hosted providers' growth numbers, Sage 50 wins?) to find the underserved flow; (4) falsify if the remaining Desktop base is too Enterprise-skewed (Intuit keeps Enterprise alive) to need rescue.

### H17 — Catch-Up & Cleanup Bookkeeping at Software Margins — RANK 17
- **Buyer job:** When an SMB months-to-years behind on books hits a tax deadline, a diligence event, or a provider collapse, current solutions fail because human services price it as bespoke projects and tech-enabled services died on labor economics (Bench: $113M raised, 35k customers stranded), causing ~$3–4.5k/yr prepaid engagements, six-month IRS extensions, and $300k-grade cash-visibility errors.
- **Contributing (2 grounds):** S11-6, S01-6. Strongest evidence: HN shutdown thread (297 pts; verbatim stranded customers; Pilot founder confirming catch-up demand on-thread); relaunched Bench price card ($199–599/mo); insider post-mortems blaming pre-agent automation limits.
- **Forcing function: YES-WEAK (moderate)** — tax deadlines and diligence events are real but episodic; the provider-collapse trigger is aperiodic. Honest label: deadline-shaped, not statutory-recurring.
- **Wave 2 must verify/falsify:** (1) the mandated Bench question: show precisely which labor line (categorization? reconciliation? doc-chasing?) agents collapse and at what gross margin at $250–500/mo — with a worked pilot, not an assertion; (2) crowding scan of AI-bookkeeping entrants (hot category — find the catch-up/cleanup specialization gap); (3) licensed-professional structure for filings (PTIN/EA/CPA partner) per the regulated-practice gate; (4) falsify if QBO/Intuit ships credible AI catch-up natively.

### H18 — Athlete-Family Recruiting & NIL Navigation (via clubs/academies) — RANK 18
- **Buyer job:** When a HS athlete's family navigates recruiting and now NIL (every D-I deal >$600 must clear NIL Go), current solutions fail because the incumbent (NCSA/IMG) sells canned automation as $1,500–4,600 multi-year binding contracts and the NIL clearinghouse is visibly overwhelmed (only 25 of 384 collective deals approved; $90M declined; Deloitte's $45M data error), causing four-figure family spend, 7-year contracts with 3-day cancellation windows, and deal money stuck in pending queues.
- **Contributing (1 ground; 3 candidates):** S12-3, S12-4 (+S12-6 video economics as feature evidence). Strongest evidence: 2026 Trustpilot NCSA refund/lock-in quotes; CBS/FOS/ESPN NIL Go failure numbers + congressional letter; freelance video rate cards ($150–400).
- **Forcing function: YES (B)** — NIL Go is a mandatory computation point on every D-I dollar (new institution, litigation-exposed, rules still moving — grade B); recruiting-calendar deadlines are real but purchases are discretionary.
- **Wave 2 must verify/falsify:** (1) the sellable slice: family/club-level navigation is the founder-reachable wedge (institutional side is enterprise) — validate WTP at $300–800/cycle against NCSA's $1,500–4,600 with 10 families from the founder's academy network; (2) B2C churn/seasonality economics; (3) UPL/agent-regulation boundary check for NIL advice (state athlete-agent laws); (4) falsify if NIL Go stabilizes (institutional fix) and if recruiting outreach automation is a thin wrapper any incumbent replicates — the moat must be the club-channel trust + data, or kill.

**Diversification note for the director:** H01–H03 share one buyer pool (small practices + billing companies). All three are individually top-grade, but if Wave 3 should not concentrate, promote H06/H07 into the attack set behind them. Ranked purely by evidence×budget, the top five stand as flagged: **H01, H02, H03, H04, H05.**

**First reserves (promote if a slot opens or a top-18 dies in early Wave 2):** S02-6 DORA RoI factory (regulator-documented 6.5% pass rate; parked only on buyer reachability), S07-4 TikTok settlement reconciliation (incumbent race + vendor-adjacent sourcing), S06-2 AI-questionnaire/ISO-42001 pack for small vendors (deal-gated forcing; Vanta down-market risk).

---

## 4. Parked — real pain, not (currently) an opportunity (45)

**Near-miss reserves (parked, first in line for any opened slot — see §3):**
- S02-6 DORA Register-of-Information factory — regulator-grade evidence (6.5% pass rate, CSSF error-decoder) and an annual mandatory filing; parked solely on buyer reachability (mid-market regulated financial entities, examiner-shaped sales) and effort-shaped economics with no public price list.
- S07-4 TikTok Shop / multichannel settlement reconciliation — ECOM CPA anchor verified, fee churn real; parked on the A2X/Link-My-Books-class race to add TikTok coverage and on 2-of-5 artifacts being vendor-adjacent.
- S06-2 AI-questionnaire / ISO 42001 pack for small B2B vendors — deal-gated money forcing verified; parked on Vanta/Conveyor down-market risk inside a crowded trust-management category.

**Platform-hostage (hard gate; re-open only with a structural change):**
- S07-1 Amazon reimbursement flip — severe hostage; policy change also shrank the recoverable pool (attacking a shrinking pond).
- S07-5 Meta AI-moderation bans; S07-6 GBP suspension hell — extreme hostage, no API surface, gray-market services; pain verified, unproductizable.
- S09-1 Dealer DMS integration ransom — duopoly litigates uncertified access; the blocker IS the pain; capital/legal-heavy. (Litigation-won portability rights are worth watching.)
- S09-5 Epicor P21 cloud SQL loss — lives on vendor tolerance (whitelisted replica).

**Crowded/served or incumbents already harvesting (head-on gate):**
- S02-2 PCI script security (c/side-class shipping at $99/mo); S03-6 PO order entry (Conexiom/Esker + LLM commoditization); S04-1 ServiceTitan, S04-3 Mindbody, S04-4 Toast, S04-6 Kaseya, S04-7 Vagaro/Booksy (escape routes exist; defectors harvested in-category); S04-5 AppFolio/Buildium mid-tier (Rentec/TenantCloud/RentRedi-class named by the sources themselves); S07-2 GEO/AI-visibility (funded venture category); S07-3 DMARC/SMTP-cliff ops (crowded DMARC SaaS; device migration is a one-time 2026 event) — near-miss; S08-5 chargebacks (Chargeflow/Stripe Smart Disputes; adjudication randomness caps product efficacy); S10-2 SMB inventory/MRP squeeze (repricing rage real, but escape routes exist and the build is heavy); S06-1 shadow-AI enforcement (SSE/DLP collision).

**Forcing function failed the credibility grade:**
- S02-7 CMMC (Phase II suspended 2026-07; whiplash regime) — re-open on revival.
- S06-3 EU AI Act deployer ops (Annex III deferred to Dec 2027; omnibus churn; checker-tool flood) — re-open ~mid-2027 or on enforcement evidence.
- S02-4 Companies House IDV campaign layer — statutory but transient: the 12-month wave ends Nov 2026 before a Wave-2-validated product could ship; residual per-appointment volume is a point transaction already served by ACSP+IDV vendors; pain concentrated in a government funnel that may stabilize.

**Buyer/budget failures:**
- S01-7 VMware small-end eviction (migration projects = services, infra-heavy; wrong shape for solo SaaS).
- S03-5 freight track-and-trace (no forcing; freight-recession budgets; funded visibility adjacents).
- S04-2 solo-trades FSM tier (evidenced UNwillingness to pay; discretionary; crowded low end).
- S05-6 quoting re-key (no forcing; carrier-data moat unsolved; raters entrenched — commercial-lines submission noted as a future hunt).
- S06-5 AI application flood / fake candidates (identity end owned by funded Socure/Persona; ATS incumbents shipping; SMB wedge = thin-wrapper risk).
- S06-6 AI-slop QA (budget-less/fragmented buyers); S06-7 agent audit trails (Show-HN supply flood, pre-budget demand); S06-8 platform slop moderation (buyers are platforms = enterprise, or moderators = no budget).
- S07-7 retail-media reconciliation (enterprise served; mid-market existence unproven; vendor-sourced).
- S08-4 founder AR chasing (soft forcing; funded AR category; its vertical expression is promoted in H12 instead).
- S08-7 AI usage/credit billing ops (2026-native and interesting, but direct spend evidence thin; funded metering vendors above) — near-miss, revisit as the category matures.
- S09-2 bank/CU core lock-in (examiner-supervised buyer, 1033 enjoined, core gatekeeping — solo-founder sales fail); S09-3 dental data hostage (gray-space extraction; per-event revenue; conversion services exist); S09-4 RamQuest sunset (real dated forcing, but acquirer owns the migration path and operator-voice is thin — verify volume in Wave 2 if capacity); S09-6 green-screen TMS (no forcing; quote-only economics).
- S10-4 optometry PM/EHR (single-platform evidence; no confirmed OfficeMate EOL; needs re-hunt).
- S02-8 GPSR for non-EU micro-sellers — regulation + platform enforcement verified, but the evidenced seller behavior is exit-over-comply (Etsy shipped shop-level EEA/NI restriction settings = mass withdrawal), the authorized-representative role requires an EU-established legal entity, and per-seller WTP (€50–500/yr) is thin; verbatim seller quotes also sat behind blocked threads.
- S11-4 grant writing (discretionary; consultant-authored pain; crowded AI-drafting field).
- S12-5 tournament ops/stay-to-play (housing revenue model being litigated away is a disruption to watch, not yet a software wedge; scheduling pain rests on vendor claims) — founder-domain watchlist.
- S12-6 team video economics (complaints dated 2021; Hudl shipping AI; family retail folded into H18); S12-7 academy/facility software (dated, moderate temperature, no forcing — revisit only as an H12 expansion).

**Cross-references:** S01-3, S10-1, S10-3 are counted as contributing (evidence inside H10/H16, H11, and H12 respectively), not parked. S04-6, S12-6, S12-7 are parked above but their evidence folds into H14, H18, and H12 respectively.

---

## 5. What the sweep says about the 2026 market (≤300 words)

Five patterns dominate 87 candidates from 12 independent directions.

**1. SMB software is in its rent-extraction era.** Five grounds independently found PE/public-market owners monetizing locked-in vertical SMB bases — auto-renewing contracts, five-figure exit fees, fee unbundling, processor steering, integration tolls. The anger is universal; the opportunity is narrow. Where refuges exist, entrants already harvest defectors. The openings are where no refuge exists: sunsetting products, held funds, and the money layer itself.

**2. Compliance calendars are the reliable demand engine — if you grade the calendar.** UK statutory, EU e-invoicing/EAA, US EVV and FMCSA dates held and are producing documented mass failure (6.5% DORA pass rate; half of MTD wave 1 unregistered). US federal future dates and AI-specific regimes whiplashed (CMMC suspended, EU AI Act deferred, Colorado repealed). Build on held regimes; treat promised ones as options.

**3. The human-middleware layer is now priced in public.** Employers publish the wages ($16–31/hr) of portal↔system bridging; services publish per-unit rates ($5–15/prior auth, $100–300/credentialing app, $100–250/audit page, $50–250/driver). That price list is the AI-agent arbitrage surface, and healthcare revenue cycle is its largest concentration — five grounds converged there.

**4. The counterparty automated first.** Payers auto-downcode and deny at machine speed; platforms ban and suspend by AI with no human recourse. The defense side — practices, sellers, agencies — still works by hand. Asymmetric-AI defense is a durable demand well.

**5. Money that moves late or opaquely (settlements, commissions, retainage, dues, licenses) is reconciled manually everywhere,** and every such flow already funds a services line — the displacement target and the honest competitor.

The composite winning shape: a held forcing function + a published services price + a swivel-chair workflow + a buyer reachable in communities.

---

## 6. Re-run recommendations before Wave 2 concludes

1. **Ground 09 (legacy lock-in) — re-run with the proven toolkit** (Arctic Shift API + safereddit mirror + TruckersReport UA-curl, per scouts 05/08): pharmacy systems came up dry, dental/title/TMS operator voice is thin, and the ground produced zero promotions largely due to access, not absence. Targets: pharmacy PMS, title-agent RamQuest cohort volume, optometry (with scout 10's S10-4).
2. **Ground 04 (vertical SMB) — targeted extension, same toolkit:** auto repair (AutoShopOwner/iATN/r/autorepair) and agency verticals were inaccessible, not dry; r/msp and r/sweatystartup would also deepen H14/H12.
3. **Two one-check errands from scout 10:** (a) NFIRS→NERIS fire-reporting mandate — verify on usfa.fema.gov; (b) the Avalara beverage-alcohol sunset rumor (would leave Sovos ShipCompliant near-monopoly for small-winery filings). Each is one authoritative fetch from potentially material.
4. **Wave-2 validator standing instruction:** worker/operator-voice spot-checks via Arctic Shift for every promoted hypothesis whose scout was Reddit-blocked (H03's posting-based candidates especially), and primary-source confirmation of the two flagged Intuit sub-claims (H16) and the Blackbaud sunset (H15).
