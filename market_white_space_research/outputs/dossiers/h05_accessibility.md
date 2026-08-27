# Opportunity Dossier — Accessibility Conformance Factory (EAA + ADA + VPAT)

Validator: Wave-2 validator, H05 · Date: 2026-08-27 · Source hypothesis: H05 (Manager 1 promotion memo, Rank 5 ★TOP-5) · Ground(s): 02 (regulatory deadlines, S02-1) + 11 (services-to-software, S11-5)

All new evidence accessed 2026-08-27; ledger at `outputs/evidence/dh05_accessibility.jsonl` (claim IDs H05-E1…E30). Carried-forward scout claims cited by their S-IDs (already Manager-1-verified).

---

## 1. The pain, restated precisely

**Who hurts.**
1. **US SMB e-commerce** (79% of 2026 digital-accessibility suits target e-commerce; 64% of sued companies under $25M revenue [H05-E1]) — hit by serial-plaintiff lawsuits and a 5–10x larger shadow volume of private demand letters.
2. **EU-scope merchants and digital-service SMBs above the microenterprise line** (≥10 staff or >€2M turnover — smaller firms are exempt until they relaunch their site [H05-E10]) — in EAA scope since 2025-06-28, now facing real enforcement: French court orders, German Abmahnung (competitor/law-firm warning-letter) waves, Swedish complaint queues.
3. **B2B SaaS vendors** selling into government, education, healthcare, and accessibility-policy enterprises — blocked at procurement without a completed ACR ("buyers ask for a VPAT, what they need is an ACR"; documented gov-procurement rejections over incomplete self-assessed VPATs [H05-E26]).
4. Agencies serving all three, who absorb the overflow without accessibility staff.

**The workflow failure.** Real conformance requires a page-by-page expert audit against WCAG 2.1/2.2 AA (55 success criteria), keyboard and screen-reader testing, issue write-ups with code locations, remediation, re-test, then paperwork (ACR/VPAT, EAA accessibility statement per member-state format, evidence archive). Automated scanners reliably cover only ~13% of WCAG 2.2 AA criteria (45% more only partially, still needing human review) [H05-E12]; the W3C ACT task force shows approved automated rules touch just 17 of 55 A/AA criteria (~31%), and only partially [H05-E13]. So the work is hand-priced expert labor at $100–250/primary page (S02-1-E3), and the cheap software substitute — overlay widgets — was federally discredited (FTC: accessiBe $1M, final April 2025 [S11-5-E4]) and demonstrably fails: **113 of July 2026's 401 US suits hit defendants who had a widget installed at the time** [H05-E2].

**Frequency.** Continuous on both jurisdictions: ~514 US suits/month pace in 2026 plus demand letters at 5–10x that rate [H05-E1, E3]; per-release conformance decay (every theme change breaks it); annual re-audit norms; per-procurement VPAT requests; EAA statements to maintain per service. A company that gets hit once stays in the pool: 77 of July 2026's 401 defendants were repeat targets [H05-E2]; the Level Access litigation-support lead's own prescription to clients is a full manual audit per site annually + weekly/biweekly scans + 3 years of retained evidence, because suits "will NEVER stop" [H05-E22].

**Strongest three artifacts.**
1. **Carrefour ruling** (Tribunal judiciaire de Caen, 2026-06-04): first EAA enforcement ruling anywhere — six months to make site and app *fully* accessible, €500/day penalty after deadline; Carrefour's defense that it was 71% RGAA-compliant was rejected: accessibility is an "obligation of result," not effort [H05-E7]. Partial compliance is now legally worthless in France.
2. **UsableNet July 2026 tracker**: 401 suits in one month; 113 against widget users; 77 repeat defendants [H05-E2] — proof the cheap substitute fails and the pain recurs.
3. **Practitioner corroboration on record** (r/accessibility, Aug 2026, via Arctic Shift): an operator whose company was sued now "pay[s] for a service to manually audit once per year" plus his own screen-reader spot-tests — "a continual, and never-ending process" [H05-E23]; a 508-era practitioner in the same thread: "Various scanners get about 30% of the things, some paid for models can get up to 80%, so you must manual test at least a bit" [H05-E22].

## 2. Budget proof

Money already moving against this pain, per customer per year:

| Line | Amount | Source |
|---|---|---|
| Manual audit, small site (recurring ~annually) | $1,250–$2,750 typical; $100–250/primary page; $500–$12,500+ range | Accessible.org price list (S02-1-E3, verified exact); DigitalA11Y [S11-5-E2] |
| VPAT/ACR with audit ("defensible VPAT") | $1,850–$4,450; ranges to $3k–$10k; doc-only add-on $350–$950 | Kris Rivenburgh / ADA Compliance Pros / Accessible.org [H05-E26] |
| Overlay/widget subscriptions (the failed substitute, still bought at scale) | accessiBe $490–$3,990/yr; UserWay Pro $490/yr + scans $990–$10,990/yr; AudioEye $49–$799/mo; UserWay claims ~1M sites | vendor/3rd-party pricing [H05-E16, E17, E18] |
| Enterprise platform umbrella (what the tier above pays) | Level Access $25k–$150k+/yr (most $40k–$90k); Siteimprove $15k–$150k+; Deque enterprise $30k–$200k+ | Vendr/TestParty teardowns [H05-E19, E20, E21] |
| US demand-letter event | $5k–$25k settlement (small biz often <$5k–$10k) + $3k–$15k own attorney for the response; $50k+ if litigated | Accessible.org settlement page; defense-cost guides [H05-E4, E5] |
| German Abmahnung event | €3,500–€20,000 per warning letter incl. fees; BFSG fines €10k–€100k in Q1-2026 formal proceedings | German legal/agency reports [H05-E9] |
| EAA penalty ceilings | €10k–€100k/infringement most states; Spain €1M, Hungary €1.26M, Italy 5% of turnover; product withdrawal + public naming | S11-5-E6/E7 (verified) |
| Expert labor line being arbitraged | $195/hr expert support (Accessible.org); auditor manual testing 8–16 hrs for a small site | S02-1-E3; audit-time guides [H05-E24] |

Steady-state spend for a conscientious SMB today: **$2,000–$6,000/yr** (annual manual audit + scanner/widget subscription), spiking **$10k–$40k** in any letter/lawsuit year. SaaS vendors additionally pay $1,850–$4,450 per product per VPAT cycle, with deal revenue gated on it. Budget proof is overwhelming and published — this is one of the few categories with a public per-page services price list.

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| Deque (axe-core, axe DevTools, axe Auditor, audit services) | Product + service | Developers, enterprise a11y programs | Free OSS; Pro $79–99/user/mo; enterprise $30k–$200k+/yr | Sells *tooling to teams that have accessibility staff*; axe-core catches 57% of issue **volume** but automated rules reliably cover only ~13–31% of **criteria**; audits sold at consultancy prices; no SMB conformance-paperwork product [H05-E12, E13, E15, E19] |
| Level Access (incl. UserWay since 3/2024, $98.7M) | Product + service + overlay | Enterprise/mid-market; UserWay = mass-market overlay | $25k–$150k+/yr (most $40k–$90k); UserWay $490/yr | SMB priced out of the real platform; owns and keeps selling the overlay class that 113 July-2026 defendants learned doesn't stop suits; community trust damaged by the acquisition (Eric Eggert: "crosses the line") [H05-E2, E20, E21] |
| Siteimprove | Product (monitoring suite) | Enterprise marketing/digital teams | $15k–$150k+/yr custom | Scanner-first (same ~13–31% reliable-coverage ceiling); no audit-grade findings or sign-off; enterprise sales motion [H05-E19] |
| AudioEye | Overlay + "expert testing" hybrid | SMB→mid-market | $49–$799/mo | Widget-led; its own 2026 report admits 38.5% of sued businesses already had an accessibility solution installed; tests 37/55 WCAG 2.2 criteria per own marketing; customers still get sued — the "protection" is marketing [H05-E1, E18] |
| accessiBe / overlay class post-FTC | Overlay | SMB mass market | $490–$3,990/yr | FTC $1M order (final 4/2025) bars its compliance claims; overlays legally established as non-compliance in EAA guides; widget presence now *attracts* serial plaintiffs (28% of July 2026 defendants had one) [S11-5-E4; H05-E2, E16] |
| Boutique manual audit firms (Accessible.org, DigitalA11Y, TestPros, Vispero/allyant class) | Service | SMB→enterprise | $100–250/page; $1,250–$2,750 typical; VPATs $1,850–$4,450 | Hand-priced human labor, 2–6+ week turnarounds; no continuous monitoring; capacity-constrained. **Accessible.org itself says AI-hybrid audits (AI layer + human sign-off) arrive ~Q1 2027 with "lower audit prices"** — the incumbent service class is pre-announcing its own disruption [H05-E11, E26] |
| TestParty | AI remediation product | Shopify/e-com dev teams | $4M seed (7/2024); $1,000–$5,000/mo | Remediation-first (rewrites source), priced $12k–$60k/yr — above SMB audit budgets; doesn't sell the conformance-paperwork outcome (audit report + ACR + statement + evidence trail) [H05-E25] |
| AccessivePath | AI audit + human pair-review | Enterprise/Fortune-500 positioning | Unpublished; free 50-page tier | Proves the hybrid architecture is buildable NOW (AI audit 1–4 hrs; IAAP-format ACR; human review on paid tiers) but targets enterprise, not the SMB/e-com conformance factory [H05-E27] |
| DIY open-source stack (axe-core, WAVE, Lighthouse, pa11y + hire auditor at $195/hr) | Stack | Technical teams | Free + expert hours | Covers the automatable ~13–31% of criteria; manual review found 7.5x more issues across 3x as many criteria than the best free tool (Roselli); SMBs without a11y skills can't run it [H05-E13, E14] |
| Do nothing / wait for the letter | Default | Majority of SMBs | $0 until event | The letter costs $5k–$25k + fees (US) or €3.5k–€20k (DE); repeat targeting documented (46% of federal 2025 suits) [H05-E4, E9; S11-5-E3] |

**Deep-read of closest 3:**
- **Deque** — shipping velocity high: auto-run Intelligent Guided Tests announced (+10% automated coverage initially; IGT reaches ~80% of issue *volume* with human answers; axe Assistant chatbot) [H05-E15]. AI roadmap aims at *developer productivity inside enterprise licenses*, not at delivering signed SMB conformance packages. Their published research also honestly caps pure automation (~57% of issue volume) [H05-E12].
- **Level Access** — consolidation play (UserWay $98.7M closed 3/2024) gives it the mass-market overlay funnel + enterprise platform; litigation-support practice confirms recurring-audit norms. Its economics (seat/contract enterprise ACV + overlay volume) resist a $1.5k self-serve audit product that would cannibalize both [H05-E20, E21, E22].
- **Accessible.org (Kris Rivenburgh)** — the SMB price-list leader; December 2025 announcement is the single most load-bearing competitive fact: current scans "reliably detect only 13% of WCAG 2.2 AA criteria"; their AI-hybrid audit (targeting 75% reliable AI detection, <0.5% false positives, with mandatory "Layer 2 human review… and overall sign off") is expected **Q1 2027** inside their Accessibility Tracker, with "lower audit prices, faster audit timelines" [H05-E11]. Translation: the segment's most credible service player has validated exactly this thesis and started the clock. The white space is real and it is ~2 quarters wide.

**Unserved segment, stated precisely:** businesses with no accessibility staff that need *audit-grade findings plus conformance paperwork plus a defense-ready evidence trail* at a $1–4k/yr price: US e-com SMBs (the 79% of suit volume), EAA-scope EU merchants above the micro line (esp. Germany's Abmahnung zone), and sub-$50M-ARR SaaS vendors needing VPAT/ACRs to close deals. Everyone present today sells them either a discredited widget, a $15k+ platform, a $1,250–$2,750 hand-made PDF with no monitoring, or dev tooling they can't operate.

## 4. The wedge

**"Audit-grade conformance factory":** agentic audit + human expert sign-off + all the paperwork, for one segment first (Shopify-class e-commerce in US-litigation/EAA scope), at ~$1,500 initial + $150–$300/mo.

Feature list (≤6):
1. **Agentic full-site audit engine** — crawl + axe-core baseline + browser-agent interaction testing (keyboard traps, focus order, dynamic states) + frontier-model evaluation of the judgment criteria, producing findings with WCAG 2.2 AA mapping, evidence screenshots, and code locations. (Architecture per the critics' own consensus: automation surfaces candidates, humans verify — AFixt/Groves; Accessible.org Layer-1/Layer-2 [H05-E10, E11].)
2. **Human expert verification + sign-off queue** — every report reviewed by a contracted IAAP-certified (WAS/CPWA) auditor before delivery; reviewer verifies agent-flagged candidates and performs the irreducibly-manual checks (screen-reader pass). No report ships unsigned.
3. **Conformance paperwork generator** — ACR on VPAT 2.5 (WCAG / 508 / EU-EN 301 549 editions), EAA accessibility statement in member-state formats (EN/DE/FR), auto-maintained.
4. **Remediation tickets, platform-aware** — Shopify theme/Liquid-level fix instructions per finding; export to GitHub/Jira; re-test on fix.
5. **Continuous evidence trail** — weekly automated scans + quarterly agent re-audits, all findings/fixes/reports archived and timestamped 3+ years (exactly the defense posture Level Access's litigation lead prescribes [H05-E22]).
6. **Demand-letter/Abmahnung response pack** — technical exhibit bundle (current audit, remediation plan + timeline, statement) formatted for the customer's defense counsel. *Technical exhibits only — no legal advice.*

**Explicitly does NOT do:** overlay/widget injection; "guaranteed compliance/lawsuit protection" claims (the FTC order defines the marketing line [S11-5-E4]); full-service human remediation; native mobile-app audits (v2); legal representation.

**≤90 days, founder + agents? Yes, with one ops dependency.** Components: crawler + axe-core + Playwright-driven browser agents + LLM evaluation + report/ACR templating + Shopify app wrapper — all standard agent-engineering. The long pole is not code: it is (a) recruiting 2–5 freelance IAAP-certified reviewers ($50–90/hr contract — plentiful; the community is organized and findable via IAAP/#a11y), and (b) the calibration benchmark (run the pipeline against 2 independently-purchased consultancy audits of the same sites and measure recall/precision before selling — this is the Manager-1-mandated "prototype-level proof" and the go/no-go gate). AccessivePath's shipping product (AI audit in 1–4 hrs + human pair-review in 24–48 hrs) is existence proof of the architecture at production quality [H05-E27].

## 5. Forcing function & why now

**Three independent, live compulsion pumps (grade A on two, B on the third):**
- **US private litigation (A, continuous):** 2026 on pace for ~6,176 suits, +20% YoY, the highest ever tracked; 79% e-commerce; demand letters 5–10x suits; repeat defendants standard [H05-E1, E2, E3]. This machine has run for a decade and accelerated through 2026.
- **EAA (A, in force and now court-tested):** applicable since 2025-06-28 (held EU date); France: DGCCRF formal notices to Auchan/Carrefour/E.Leclerc/Picard (11/2025) and the Caen ruling (6/2026, "obligation of result," €500/day) [H05-E7, E8]; Germany: law-firm Abmahnung wave from ~6 weeks after in-force, formal fine proceedings from Q1 2026 [H05-E9]; Sweden: 124 formal complaints by 10/2025; Netherlands enforcement expected 2H 2026 [H05-E7].
- **US public-sector wave (B, dated but slipped once):** DOJ Title II WCAG 2.1 AA deadlines extended 4/2026 to April 2027 (≥50k pop.) / April 2028 (smaller) [H05-E28] — graded B per the deadline-credibility lesson; treated as expansion, not load-bearing. (HHS §504 health-sector deadline May 2026 adjacent.)
- **Procurement (A, money-movement):** no ACR, no deal — documented procurement rejections [H05-E26].

**What changed 2024–2026:** (1) FTC killed the cheap-overlay escape hatch (1/2025) and July-2026 data shows widgets now correlate with getting sued, not protection [S11-5-E4; H05-E2]; (2) EAA moved from theory to court orders and fee-bearing warning letters (11/2025–Q2 2026) [H05-E7, E8, E9]; (3) the Carrefour "obligation of result" standard made partial compliance legally worthless in the first-mover jurisdiction [H05-E7]; (4) frontier multimodal models + browser agents crossed the threshold where the industry itself (Deque auto-IGT, Accessible.org Q1-2027 hybrid, AccessivePath, academic WCAG-EM copilot frameworks) declares hybrid audits imminent [H05-E11, E15, E27, E30] — but almost nobody ships it at SMB price yet. The window is approximately now → Q1 2027.

## 6. Distribution plan (solo-founder realistic)

First 10 customers, by named channel:
1. **Shopify App Store — "accessibility" category** (today dominated by overlay apps, i.e., discredited incumbents): a free scan-grade audit as the app's hook, paid conversion to the signed audit + paperwork. Shopify merchants are the exact US-suit demographic (79% e-com) and Shopify pushes compliance responsibility to merchants (themes cover only ~16–22% of WCAG criteria out of the box, per vendor teardowns) [H05-E29].
2. **ADA-defense law firms** (the $3k–$15k response-fee earners — named specialists advertise openly): they need fast, credible technical exhibits for every letter; become their standing audit supplier. 3–5 firms cover hundreds of letters/yr [H05-E4, E5].
3. **Germany's Abmahnung panic channel**: Händlerbund / IT-Recht Kanzlei ecosystem and e-commerce agencies serving 10–250-employee shops; the warning-letter wave (€3.5k–€20k a letter) is an acute purchase trigger [H05-E9]. Requires DE-language statement formats (in wedge).
4. **B2B SaaS VPAT inbound**: SEO on "VPAT fast/cost" (high-intent, procurement-deadline-driven; comps show 2–4 week incumbent turnarounds — beat with 72-hour signed ACR) + G2/LinkedIn. [H05-E26]
5. **Agencies white-label**: web agencies asked "are we compliant?" by clients; audit-per-client resale. (The r/accessibility monitoring thread is literally an agency-side builder asking how this is handled [H05-E22].)

**Sales cycle estimate:** event-driven (letter/Abmahnung/procurement ask) = days; preventive SMB = 2–6 weeks self-serve. No enterprise motion.
**Pricing hypothesis:** $990–$1,990 initial signed audit + paperwork (vs $1,250–$2,750 boutique + $1,850–$4,450 VPAT bundles); $149–$299/mo monitoring/re-verification (vs $490–$4k/yr widgets that don't work and $15k+ platforms); demand-letter pack $2,490 (vs $3k–$15k legal response spend it feeds into). Comparable-price evidence: §2 table.
**Channel caution (evidenced):** r/accessibility is hostile to stealth marketing (mod-removed posts, founder call-outs in the sampled threads [H05-E22]) — participate as practitioner or not at all; sell where the buyers are (Shopify/legal/agency channels), not where the auditors are.

## 7. AI-structural advantage

The services line being collapsed is priced in public: $100–250/primary page, $195/hr, 8–16 expert hours per small-site audit [S02-1-E3; H05-E24]. Decomposition of that labor: crawl/inventory (fully agentic), per-criterion automated checks (agentic), interaction testing — keyboard/focus/dynamic states (largely agentic via browser agents), judgment criteria — alt-text quality, reading order, error-message usefulness (agent-proposed, human-verified), screen-reader pass (human, targeted), report/ACR/statement writing (agentic from verified findings — Accessible.org: VPAT remarks that "take hours manually" generate "in seconds" [H05-E26]). Human hours per SMB engagement compress from ~10–16 to an estimated 3–5 (inference — the pilot benchmark measures this). At $70/hr contractor cost that is ~$250–$350 COGS on a $1,500 engagement → ~75–80% gross margin at ~40% below boutique price, plus pure-software monitoring ARR.

**The Bench question, answered specifically.** Bench died because bookkeeping is open-ended monthly judgment against messy private data — pre-agent automation hit ~30% and the rest stayed human forever, at human margins. WCAG auditing is the opposite shape: a **fixed, public, versioned rubric** (55 criteria), per-criterion machine-verifiable evidence (DOM + screenshot + interaction trace), a **standardized output artifact** (ACR/VPAT), and an event-then-monitor cadence rather than bespoke monthly production. The expensive human step becomes *verification of machine-surfaced candidates* — a queue, not a craft project. This is why the industry's own service leaders (Accessible.org) and toolmakers (Deque auto-IGT) are converging on the same hybrid architecture right now [H05-E11, E15] — and why incumbent *service* economics (per-page billing) and incumbent *platform* economics (enterprise ACV + overlay volume) both resist pricing it at $1.5k self-serve.

## 8. Moat path

What accumulates: (1) **platform-fix corpus** — verified finding→fix pairs per Shopify theme/app/component (the same 30 themes recur across thousands of stores), making each subsequent audit cheaper and remediation guidance better; (2) **the evidence archive as switching cost** — 3 years of timestamped audits/fixes is precisely the litigation-defense asset (incumbent-prescribed [H05-E22]); leaving the product means abandoning the trail; (3) **reviewer network + calibration data** — graded human-verification outcomes are training data for raising the agent's reliable-detection share toward Accessible.org's stated 75% frontier [H05-E11]; (4) member-state statement/format coverage (DE/FR legal-format depth is real work others skip); (5) app-store install base + defense-firm relationships.

**Honest thin-wrapper assessment:** the AI evaluation layer itself WILL commoditize — Deque is shipping auto-IGT, Accessible.org arrives ~Q1 2027, models keep improving. A bare "AI audit" is a thin wrapper and would fail the gate. The defensible product is the **factory**: signed human verification, paperwork in every required legal format, continuous evidence custody, platform-specific remediation, and channel position — none of which is one model call. Moat is operational and data-accumulative, not structural; it must be earned by shipping first into the ~2-quarter window and converting speed into archive + corpus + channel lock.

## 9. Risks & unknowns (top 5, each with its test)

1. **Quality/liability crux — can agents+human actually hit consultancy grade?** If the pipeline's recall on manual-only criteria is materially below a boutique audit, the product is a liability machine (and an FTC target if oversold). *Test (go/no-go, weeks 2–6):* commission 2 independent consultancy audits ($2.5–5.5k total) on benchmark sites; run the pipeline + reviewer on the same sites; require ≥90% recall of consultancy findings at A/AA and <5% false-finding rate before any sale; publish the methodology. (Precedent that the bar is passable: AccessivePath ships; Accessible.org targets 75%/<0.5%FP for the AI layer alone [H05-E11, E27].)
2. **Fast-following incumbents close the window** (Accessible.org Q1 2027; Deque auto-IGT; AudioEye "expert testing" repricing; TestParty adding audit paperwork). *Test:* ship in ≤90 days; 25 paying customers before 2027-01; track competitor releases monthly; kill criterion = a credible <$2k signed-audit product from any of them before we reach 10 customers.
3. **EAA enforcement against SMBs (esp. non-EU) stays theoretical** — to date, court action hit French majors; German letters hit domestic shops; no documented cross-border SMB enforcement. Half the EU thesis rests on deterrence, not cases. *Test:* 20 interviews with DE/FR-exposed merchants (are they spending?); track member-state actions quarterly (German Abmahnung volume = leading indicator); if EU WTP is absent by month 4, concentrate on US-litigation + VPAT segments (which alone carry the model).
4. **US litigation-reform tail risk** — serial-plaintiff standing challenges or state fee-shifting rules could cut suit volume. *Test:* monitor circuit splits/state legislation quarterly; diversification across three pumps (litigation, EAA, procurement) is the structural hedge; kill criterion = >40% YoY national suit-volume decline for 2 consecutive quarters.
5. **Human-review economics creep** — if reviewer hours stay >8/engagement (agents surface too much noise or too little signal), margins collapse to services and Bench's ghost wins. *Test:* instrument reviewer hours from engagement #1; target <5h by #20; kill/reprice criterion = >8h sustained at #20 despite two pipeline iterations.

## 10. Scores

| # | Dimension | Weight | Score | Rationale (evidence) |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 4 | Continuous two-jurisdiction enforcement + monthly suit cadence; per-customer pain is episodic-until-hit, then chronic (repeat defendants; "never stop") [H05-E1, E2, E22] |
| 2 | Budget proof | 15% | 5 | Public per-page price lists, $1.85–4.45k VPAT bundles, widget subscriptions at ~1M-site scale, settlements, Abmahnung fees, $15k–150k platform umbrella [§2] |
| 3 | Competitive gap | 12% | 3.5 | Crowded and racing, but the SMB audit-grade+paperwork tier is demonstrably empty today: overlays discredited, platforms $15k+, boutiques hand-priced, hybrid entrants enterprise-first, segment leader not shipping until Q1 2027 [§3] |
| 4 | Forcing function | 10% | 5 | Live statute (court-tested, daily fines), live litigation machine at record volume, procurement money-gates; two A-grade pumps + one B [§5] |
| 5 | Founder+agents feasibility | 12% | 4 | 90-day wedge is standard agent engineering + templating; ops dependency on 2–5 contract reviewers and a calibration benchmark [§4] |
| 6 | Distribution reachability | 10% | 3.5 | Shopify App Store + defense firms + agencies + VPAT SEO are solo-reachable with event-driven cycles; German channel needs language/local work; a11y community itself is marketing-hostile [§6] |
| 7 | AI-structural advantage | 8% | 4.5 | Published $100–250/page human line collapses to ~$250–350 COGS at equal output; fixed public rubric = best-case agent shape; incumbents' per-page and enterprise-ACV models resist following [§7] |
| 8 | Moat path | 8% | 3 | Evidence-archive switching cost + platform-fix corpus + reviewer calibration data accumulate; but the AI layer commoditizes and window is short [§8] |
| 9 | Expansion ceiling | 5% | 4 | Adjacent: PDF/document remediation ($7.50/pg line), mobile apps, Title II/§504 public-sector wave 2027–28, EU statement upkeep, agency white-label → credible path toward compliance-ops platform [§5, §2] |
| 10 | Durability | 5% | 3 | Model jumps help rather than hurt; main threats are incumbent AI releases (18-month horizon) and US litigation reform [§9] |

**Weighted: 81/100 → "pursue" band.**

**Hard gates:** Budget proof PASS · Reachable buyer PASS (self-serve/event-driven SMB) · Thin-wrapper PASS with condition (the factory — human sign-off, paperwork formats, evidence custody, integrations — is the product; a bare AI-audit variant would FAIL this gate) · Head-on collision PASS narrowly (no funded incumbent currently ships SMB-priced signed audits + paperwork; nearest threats 1–2 quarters out — re-check at Manager 2) · Platform hostage PASS (three demand pumps, multi-channel; Shopify is one channel, not the business) · Regulated practice PASS (accessibility auditing is unlicensed; IAAP certs are credentials, not licenses; demand-letter pack ships technical exhibits only, no legal advice; carry E&O insurance).

**Displacement sentence:** Current solution = a boutique manual audit ($1,250–$2,750/engagement at $100–250/page) plus a widget subscription ($490–$3,990/yr) plus panic legal spend ($3k–$15k per letter), or a $15k–$150k enterprise platform. New product = agent-audited, human-signed conformance factory at ~$1,500 + $150–300/mo. The customer switches because they get consultancy-grade findings and every required document at 40–70% below boutique price with a continuous defense-ready evidence trail — instead of a widget that 113 of July 2026's 401 defendants proved doesn't stop lawsuits.

## 11. Verdict proposal

**PURSUE (81/100), conditional on the quality benchmark.** Evidence base is exceptional: published services prices, record 2026 litigation, court-tested EAA with daily fines, regulator-killed substitute, and the industry itself validating the hybrid-audit thesis. The window is real but ~2 quarters (Accessible.org Q1 2027; Deque auto-IGT). Go/no-go gate: the §9-R1 benchmark (≥90% recall vs consultancy audits, <5% false findings, <5 reviewer-hours) inside the first 6 weeks — pass and sprint the Shopify/demand-letter wedge; fail twice and PARK. First paying test: 10 signed audits at ≥$990 from Shopify-merchant and demand-letter channels inside 60 days of the benchmark passing.

## 12. Evidence ledger

Full ledger: `outputs/evidence/dh05_accessibility.jsonl` (30 records, H05-E1…E30, all accessed 2026-08-27). Carried-forward verified scout claims: S02-1-E1…E6, S11-5-E1…E7.

| ID | Claim (short) | Source |
|---|---|---|
| H05-E1 | 2026 pace ~6,176 suits (+~20%), highest ever; 79% e-commerce; 36% of sued >$25M rev (⇒64% smaller) | UsableNet midyear blog |
| H05-E2 | July 2026: 401 suits; 113 had widgets; 77 repeat defendants | UsableNet tracker |
| H05-E3 | Demand letters outnumber suits ~5–10x (2026) | UsableNet trends blog |
| H05-E4 | Settlements $5k–$20k typical, small biz often <$5k–$10k | Accessible.org settlements page |
| H05-E5 | Letter-response legal fees $3k–$15k; defense retainers $10k–$25k, $50k+ litigated | ADA-defense cost guides |
| H05-E6 | AudioEye 2026 report: 38.5% of sued businesses already had an a11y solution | AudioEye litigation report |
| H05-E7 | Carrefour ruling: Caen 2026-06-04; 6 months to full accessibility; €500/day; 71% ≠ compliant; obligation of result; SE 124 complaints; NL 2H-2026 | Codeslog analysis |
| H05-E8 | DGCCRF notices to Auchan/Carrefour/E.Leclerc/Picard 11/2025; emergency injunctions 11/12/2025 | TestParty/BarrierBreak reports |
| H05-E9 | German Abmahnwelle: letters from ~6 wks post-BFSG; €3.5k–€20k/letter; Q1-2026 fine proceedings €10k–€100k | German legal/agency reports |
| H05-E10 | Microenterprise exemption (<10 staff AND ≤€2M); relaunch loses protection | SiteCockpit/Grau law |
| H05-E11 | Accessible.org: scans reliably detect 13% of WCAG 2.2 AA; AI-hybrid (75% target, human Layer-2 + sign-off) expected Q1 2027, "lower audit prices" | Accessible.org Labs |
| H05-E12 | Deque study: automation finds ~57% of issue volume | Deque coverage report |
| H05-E13 | W3C ACT: approved automated rules cover only 17/55 A/AA criteria (~31%), partially | Roselli (3/2026 update) |
| H05-E14 | Manual review found 7.5x more issues across 3x criteria vs best free tool | Roselli comparison |
| H05-E15 | Deque shipping auto-IGT (+10% automated coverage; IGT ~80% of volume); axe Assistant | Deque AI pages |
| H05-E16 | accessiBe still sells post-FTC, $490–$3,990/yr | 3rd-party pricing teardowns |
| H05-E17 | UserWay $490/yr; scans $990–$10,990/yr; ~1M sites | 3rd-party pricing/Forbes |
| H05-E18 | AudioEye $49–$799/mo; "37 of 55 WCAG 2.2 criteria" tested | Capterra/AudioEye |
| H05-E19 | Siteimprove $15k–$150k+/yr; Deque enterprise $30k–$200k+; axe Pro $79–99/user/mo | Vendr/pricing teardowns |
| H05-E20 | Level Access $25k–$150k+/yr, most $40k–$90k | Vendr/TestParty |
| H05-E21 | Level Access closed UserWay $98.7M 3/2024; community backlash | Forbes/Eggert |
| H05-E22 | Practitioners: scanners ~30% (paid models to 80%); Level Access demand-lead prescribes annual manual audit + weekly scans + 3-yr records; "will NEVER stop" | r/accessibility via Arctic Shift |
| H05-E23 | Sued operator now pays annual manual-audit service + own screen-reader tests | r/accessibility via Arctic Shift |
| H05-E24 | Manual audit time: 8–16 hrs screen-reader testing small sites | Audit-time guides |
| H05-E25 | TestParty: $4M seed; AI source-code remediation; $1k–$5k/mo Shopify | AlleyWatch/TestParty |
| H05-E26 | VPAT market: defensible VPAT $1,850–$4,450 (to $3k–$10k); doc-only $350–$950; procurement rejections documented; AI fills VPATs w/ human correction | Rivenburgh/ADA-CP/Accessible.org |
| H05-E27 | AccessivePath ships AI audit (1–4h) + human pair-review (24–48h), IAAP-format ACR, enterprise-targeted | accessivepath.com |
| H05-E28 | DOJ Title II deadlines extended to 4/2027 and 4/2028 (slip evidence + future wave) | Jackson Lewis/UPCEA |
| H05-E29 | Shopify: merchant owns compliance; themes ~16–22% of WCAG out of box; overlays don't satisfy EAA | Vendor teardowns (labeled) |
| H05-E30 | Academic: MLLM-copilot WCAG-EM audit framework (AAA/GRASP/MaC), human-AI partnership | arXiv 2511.03471 |
