# Agent 08 — Direct-competitor sweep

**Research date:** 2026-08-19 · 20 web searches + 24 page fetches; search budget capped mid-run.

## The critical framing, found early and confirmed repeatedly

**There are two opposite businesses using the same vocabulary.**
- **Payer-side** ("freight audit & pay") recovers money for *shippers/brokers* by **denying** accessorials.
- **Biller-side** (this thesis) recovers money for *carriers/brokers* by **capturing unbilled** accessorials.

**The funded companies are almost all payer-side. That is the single most important finding.**

## Direct competitors

| Company | Model | Funding | Accessorials | Pricing | Customer | Status |
|---|---|---|---|---|---|---|
| **ClearLane** (getclearlane.com) | BPO + TMS-embedded team | None disclosed | Detention, layover, TONU, lumper, rate discrepancies | **10–25% of recovered revenue** (VERIFIED) | Brokers, 3PLs, carriers, forwarders | Launched May 2026 |
| **Detention Source** | Enterprise SaaS | None disclosed | Detention only | $5K–$50K+/yr (CLAIMED, competitor-sourced) | Enterprise carriers + shippers | Established |
| **detentioniq** | SaaS on ELD feed | UNKNOWN | Detention only | Not disclosed | 50–200 truck carriers | Live |
| **DockClaim** | Mobile GPS app | UNKNOWN | Detention only | $49/mo (CLAIMED) | Owner-ops, small fleets | Rolling out |
| **Detenly** | SaaS claim engine | UNKNOWN | Detention only | Not disclosed | 3–50 truck carriers | **Pre-launch, zero customers** |
| **Tiriel** (fka TrackChain) | AI dispatch workforce; "Auditor" agent | YC S21, amounts undisclosed | Detention, TONU | $99 first month, then $349+/mo | Dispatchers, 5–30+ truck fleets | Team of 20 |
| **FreightAI** (freightai.us) | Billing automation SaaS | UNKNOWN | Detention, lumper, TONU, layover | Not disclosed; 14-day trial | Small/mid carriers | Claims 500+ carriers (CLAIMED) |
| **Detention Gun** (iOS) | Consumer app | None | Detention, lumper | $3.99/invoice or $12.99/mo | Owner-operators | Jan 2025; **too few ratings to display** |
| **Detention Tracker System** (whop.com) | $299 Google Sheets template | None | Detention + accessorials | $299 one-time | Small carriers | "No AI. No complicated software." |

**ClearLane** is the closest analogue and the only one charging on outcome. Verbatim: *"ClearLane charges 10 to 25% of the additional revenue recovered from missed billable charges such as detection, layover, TONU, and rate discrepancies… If the audit finds nothing, you pay nothing."* Its accessorial audit *"reviews every load before the shipper invoice is finalized"* — genuine **entitlement detection**. Traction thin and self-reported: $42K recovered "this month", $247K over six months, no named logos, no case studies (CLAIMED). **It is a human BPO — "a dedicated team inside the TMS you already run" — not a product.**

**detentioniq** is the cleanest software statement of the thesis: *"captures dwell from your ELD, builds the proof, and invoices it — so you stop writing off detention you already earned."* Detention only, no pricing, no customers, no funding, no team disclosed. **Detenly** is the same shape one stage earlier — explicitly *"looking for U.S. carriers to prove these numbers with us."*

**Detention Source is the quiet incumbent and the most instructive datapoint:** automated detention invoicing with a shipper approve/deny workflow, McLeod/TMW/Oracle integration, and *"the largest repository of facility-level detention data in the trucking industry"* — and it has stayed small and unfunded for years. **It has the entitlement data nobody else has and does not monetise recovery.**

**Tiriel is the pivot signal.** YC S21 as TrackChain ("AI-native logistics OS"), now *"the AI workforce for freight dispatch."* Detention recovery survived only as one of five agents: the Auditor *"catches detection, TONU, and other recoverable revenue."* **Detention recovery was not strong enough to be the company.**

## Adjacent — payer-side, structurally adversarial

- **Freehand AI — $75M Series C, Battery Ventures + NewRoad, backed by Penny Pritzker (July 2026).** *"Freehand's AI Teams audit every invoice, enforce every contract, and close every dispute… recover 3–5% of freight spend."* Logos: Meta, GE, J&J, Unilever, Pfizer, Saks. Claims $260M recovered in 2025. **Explicitly hunts "unearned accessorial charges."** This is a well-funded machine built to **deny** the exact revenue a carrier-side product tries to collect.
- **Loop** — $35M Series B (Oct 2023), co-led J.P. Morgan Growth Equity + Index; founded 2021 by ex-Uber/Flexport engineers. *"never approves an invoice with an incorrect rate, service, or accessorial."*
- **Lighthouz AI** — YC S24. "AI Accountants for Logistics." Broker AP audit (45+ audits/document, accessorial validation, reweighs, reclasses, auto dispute filing) plus AR invoicing/collections. 70–85% no-touch. **Audits what carriers billed — does not detect what the broker failed to bill.**
- **Laneproof** — broker invoice reconciliation; catches detention padding, TONU/layover *overcharges*. Same inverse direction.
- **Opereit** (Barcelona) — **$2.5M pre-seed, 2026-06-03**, Seedcamp + Yellow lead. AI agents *"detect invoice errors, identify lost and damaged shipments, and file carrier claims through to resolution, fully autonomously, with no human in the loop."* Parcel/e-comm, not truckload — **but the closest *funded* company to "autonomous claim recovery" as a category.**
- **Windward** — AI detention & demurrage automation, Feb 2025 (ocean containers, cost avoidance).
- FreightMynd, Lojistic, STAT, Infinity IPS — freight audit / BPO, payer-side.

## Adjacent — AI freight agents (not competitors)
Vooma ($16.6M). HappyRobot ($44M Series B Sept 2025 ~$500M val, now Series C; 150+ enterprise customers, DHL, Kuehne+Nagel; has a "collections" workflow but no accessorial entitlement logic). Drumkit (PLS Logistics, NFI). FreightHero.ai ($5M seed; RateCon-to-POD ops, **no billing**). Reform (YC W24, 13 people). Alvys ($40M Series B, Sept 2025). 5U AI ($3.2M pre-seed, EU forwarders). **Vector** — YMS that *reduces* detention 30–67%, i.e. shrinks the pool.

**TMS-embedded (the real default):** Toro TMS, Trimble TMW, and McLeod all auto-flag detention against configurable free time and can auto-calculate at billing. **This is the "good enough" incumbent every sale must displace.**

## Failed / pivoted attempts
- **TrackChain → Tiriel** (YC S21). Detention/TONU claims demoted to one agent inside a dispatch product. **Strongest available evidence that detention recovery alone does not support a venture-scale company.**
- Convoy (2023 shutdown) — general digital brokerage, not detention-specific; not evidence either way.
- **No company found that built pure detention/accessorial recovery and died.** Genuinely UNKNOWN, not "none exist" — an absence of visible corpses more likely reflects that nobody has been big enough to make news.

## Funding landscape

**Total disclosed capital into companies whose primary product is carrier/broker-side recovery of unbilled accessorials: $0 identified.** Not one of ClearLane, Detention Source, detentioniq, DockClaim, Detenly, or FreightAI discloses any raise. Tiriel is YC-backed but recovery is a feature.

**Meanwhile the inverse has raised heavily: Freehand $75M, Loop $35M+, plus Lighthouz (YC) and Laneproof.** Claims-recovery-as-autonomous-agent is only now attracting seed money (Opereit, $2.5M, June 2026) — in parcel, not truckload.

Market size not in dispute: ATRI 2024 — 94.5% of fleets charge detention, **fewer than 50% of those invoices get collected**; $3.6B direct uncompensated detention in 2023 plus $11.5B lost productivity; DAT calls it a $15B problem (Oct 2024).

## Is the direct-competitor lane occupied?

**No — not by anyone well funded. Verdict: the lane is crowded at the bottom and empty at the top.**

Evidence: (1) Zero disclosed venture funding in any carrier-side unbilled-accessorial recovery company. (2) The best-capitalised adjacent players — Freehand ($75M), Loop ($35M) — are on the *opposite side of the invoice* and profit from denying these charges. (3) The one company with genuine entitlement detection and contingency pricing (ClearLane, 10–25%) is a three-month-old human BPO with no named customers. (4) The one company with the best proprietary data (Detention Source) has never scaled or raised. (5) The YC company that had this exact wedge pivoted away from it.

**Caveat that should temper the verdict: the floor is very crowded** — a $49/mo app, a $12.99/mo iOS app, and a $299 Google Sheet all attack the same job. **That is evidence of real demand and of brutal price anchoring at the SMB end, not of a defended incumbent.**

## What nobody is doing
1. **Contract-aware entitlement detection.** Every tool found uses a global default threshold (detentioniq: 2 hours). **Nobody parses each rate confirmation for that shipper's actual free time, grace, rounding and cap and computes entitlement per load.** This is the hard part and the moat.
2. **Multi-accessorial breadth.** Six of nine direct competitors are detention-only. Nobody systematically covers layover, TONU, driver-assist, reconsignment, redelivery, stop-offs, pallet exchange, chassis split and lumper together.
3. **Contingency-priced *software*.** ClearLane proves carriers will pay 10–25% of recovery — but only for humans. No software product is priced on outcome.
4. **The counterparty to Freehand.** A $75M-funded engine is systematically denying carrier accessorials with contract-level evidence, and carriers have nothing but a Google Sheet. **Nobody is arming the biller side with symmetric evidence.**
5. **Retroactive recovery.** Every tool is forward-looking from install date. **Nobody mines the trailing 6–12 months of closed loads against ELD history — the only way to show ROI before the first new load moves.**
6. **Proof of collection, not submission.** Nobody publishes a *paid* rate. Given ATRI's sub-50% baseline, **collection — not invoicing — is the actual product.**
7. **Facility-level entitlement intelligence married to recovery.** Detention Source has the facility dwell database and doesn't sell recovery; the recovery startups have no facility priors.

## Sources
natlawreview.com/press-releases/clearlane-offers-accessorial-charge-recovery-audit-help-freight-companies · getclearlane.com + /pricing · detentionsource.com/home · detentioniq.com · detenly.com · dockclaim.com/compare/detention-source-alternative (403; snippet-sourced) · tiriel.ai/about-us · ycombinator.com/companies/trackchain · freightai.us · apps.apple.com/us/app/detention-gun/id6756655896 · whop.com/detention-tracker/detention-tracker-system/ · freehand.ai + /articles/freight-accessorial-charge · businesswire.com/news/home/20231003388240/en/...Loop...35-Million-Series-B · lighthouz.ai · laneproof.com/blog/invoice-reconciliation-software-freight-overbilling · seedcamp.com/views/opereit-raises-2-5m-to-fix-logistics-e1-billion-blind-spot/ · windward.ai/news/windward-launches-detention-demurrage-automation-solution/ · freightwaves.com/news/vooma-grabs-16-6m-in-funding... · happyrobot.ai · drumkit.ai · freighthero.ai · ycombinator.com/companies/reform · torotms.com/blog/driver-detention-management-software · withvector.com/solutions/dwell-detention-fees/ · millennialstrucking.com/blog/accessorial-charges-trucking-uncollected-revenue · 5u.ai/blog/5u-ai-raises-3-2m-pre-seed-funding · artificialintelligence-news.com/news/alvys-ai-agents-freight-tms/
