# Opportunity Dossier — Subcontractor Payment-Chain Ops (pay apps, lien waivers, retainage)

Validator: Wave-2 validator, H07 · Date: 2026-08-27 · Source hypothesis: H07 (Manager 1 promotion memo, Rank 7) · Ground(s): 03 (human-middleware jobs, S03-7), 08 (money friction, S08-1)

**Evidence ledger:** `outputs/evidence/dh07_subcontractor_payments.jsonl` (H07-E1…E28). All Reddit artifacts re-pulled from the Arctic Shift archive (post + comment level); all pricing pages re-accessed 2026-08-27.

**QC re-verification (Manager 1's flag on the "$50k retainage" quote) — RESOLVED IN FAVOR OF THE FIGURE.** The archived selftext of r/Construction thread `1uehqtf` does read "about $50 sitting out there," exactly as Manager 1's QC found. But the archived *comments* contain the poster's own correction, twice: a commenter asks "They are withholding fifty bucks from you?" and the OP replies **"Typo. $50k"** and again **"$50k, sorry"** (H07-E1). The $50k retainage magnitude is therefore restored on the poster's own words, and the thread's structural narrative (pay-if-paid clause, retainage frozen ~6 months behind work outside his scope) was verified verbatim. Retainage economics no longer rest on inference: this thread plus the 5%-for-3-4-years reply (H07-E2), the 18-month/60-90-day pay-when-paid millwork thread (H07-E3), and the retainage-vs-margin arithmetic (H07-E25) give four independent sourced magnitudes.

---

## 1. The pain, restated precisely

**Who hurts:** commercial specialty subcontractors — electrical, mechanical, millwork, concrete, glazing, roofing, waterproofing — roughly $0.5M–$20M revenue, US-wide. The acute segment is the **$0.5M–$5M sub with zero or one office person**, where the owner or a single coordinator runs the entire payment chain. (At $5M–$20M the same pain funds a dedicated $47k–$65k billing clerk — the budget proof — and becomes Siteline's market.)

**The workflow failure:** getting paid is a monthly, multi-artifact, multi-counterparty production the sub must run to the *payer's* specifications:

1. **Monthly pay application** per project — G702/G703-style continuation sheets off the schedule of values, formatted to each GC's requirements, submitted into whichever portal each GC dictates (Textura, GCPay, Procore, email PDF). Miss the GC's billing cutoff and payment slips a full month.
2. **Lien-waiver exchange in both directions** — conditional/unconditional, progress/final waivers to the GC with every billing/payment, plus collecting the same from their own sub-tier and suppliers before they can be paid.
3. **Statutory lien-rights machinery** on a deadline lattice that varies by state and project: preliminary notice within 20 days (CA/AZ), NTO received by day 45 (FL — "otherwise you forfeit your lien and bond claim rights," the harshest rule in the country), monthly fund-trapping notices by the 15th of the 3rd month (TX), then lien-recording windows. Miss the window, lose the right (H07-E19/E20/E21).
4. **Retainage recovery** — 5–10% of every invoice withheld until whole-project closeout, months to years after the sub's scope ends; early release "goes nowhere because early release is extra paperwork nobody owns" (GC-side commenter, H07-E2).

**Frequency:** monthly per project (hard cutoffs), waivers per payment event, notices per new project + monthly in TX, retainage per project tail. Cash arrives on 55–120-day cycles ("paid when paid… 60–90 days and there's no budging"; public-construction DSO 60–108 days per a commenter citing payment-index data, H07-E3).

**Strongest three artifacts:**
- **H07-E1/E2 — "Retainage $ stuck in the abyss" (r/Construction, Jun 2026):** ~$50k (OP-corrected) frozen ~6 months behind a pay-if-paid clause; peer: 5% routinely sits 3–4+ years; GC-side reply names the fix a product can systematize (line-item closeout on the GC's next owner application).
- **H07-E3 — millwork sub, ~$597k revenue (Mar 2025):** 55-day first payment on AIA billing, 25-day funding gap on net-30 materials, "uncomfortably close to breaking the bank."
- **H07-E27 — employer postings (live today):** 108 open US postings matching "construction billing coordinator lien waivers"; Vaco at $62–65k/yr for "100–200 invoices per billing cycle" of AIA progress billing; Loenbro at $25–28/hr to "manage lien waivers and construction payment documentation… across multiple projects" (S03-7-E1/E2 carried, count re-verified 2026-08-27).

## 2. Budget proof

Money already moving against this pain, per customer per year:

| Line | Evidence | Amount |
|---|---|---|
| In-house billing labor | BLS billing/posting clerks median (S08-1-E7); Loenbro/Vaco/TSU postings, 108 live (H07-E27) | **$47,170 median; $52k–$68k loaded** at subs big enough to hire; 0.25–0.5 FTE of owner/admin time below that (inference: $12k–$24k equivalent) |
| Portal usage fees the sub pays | Oracle Textura fee schedule (H07-E14) | **0.22% of contract value** per Textura project, capped $5,000; $100/contract sub-tier. A sub running $3M/yr through Textura GCs pays ~$6,600/yr just to submit |
| Per-document notice/lien services | Levelset $59/notice, $349/lien (H07-E6/E7); SunRay $25–35/notice (H07-E18); Texas Easy Lien $29 notice/$299 lien (H07-E22) | **$300–$1,800/yr** at 10–30 new projects, plus $299–$349 per lien event |
| Software (where bought) | Levelset from $149/user/mo (H07-E8); Siteline custom annual on billing volume (H07-E16); GC-side platforms $400–$8,000+/mo (H07-E28, low-trust) | **$1.8k–$10k/yr** sub-side when purchased at all |
| Financing the 55–120-day gap | Billd 2.99%/mo + 2% purchase fee, 120-day terms; Constrafor Early Pay ~2%/invoice for 48-hr payment (H07-E23) | **~2% of every advanced invoice**; ~36%/yr-equivalent on financed materials |
| Retainage float | 5–10% withheld vs margins "as low as 5–10%" (H07-E25); $50k/6mo and 5%/3–4yr artifacts (H07-E1/E2) | **Entire project profit parked** until closeout |
| Failure mode (episodic) | $10k+ lawyer fees, pay app >1yr old; ~$55k arbitration (H07-E4); TX lien lawyers $361/hr avg, $1,000–$2,500/lien (H07-E22) | **$1k–$55k per dispute** |
| Macro | Rabbet: $273B (2023) → $280B (2024) → $299B (2025), a "hidden 14% tax"; finance teams 5–10 hrs/person/wk on manual documents (H07-E24, S08-1-E6) | industry-wide, worsening |

The composite: a $2–5M sub carrying ~$500k of AR at any time is spending **$15k–$70k/yr** across labor fraction, portal fees, per-document services, and financing spread — before any dispute. (Composite is inference; each component is sourced.)

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| **Levelset (Procore)** | product (notices, waivers, liens) | subs/suppliers all sizes; SMB + mid-market sales motions (H07-E11) | $59/notice, $59/demand, $349/lien; subs from $149/user/mo; subscriptions sales-gated (H07-E6/E7/E8) | Post-acquisition the sub side decays: Jan 2026 reviews — support "unresponsive and unavailable," $67 notice charge "total scam," **GC payment-history vetting tools removed** ("predatory companies can take advantage of people") (H07-E9); "not a good match for any small business" (Mar 2024, H07-E8); parent redeployed the waiver tech into GC-side Procore Pay (H07-E12). Covers documents, not the billing workflow (no pay-app assembly) |
| **Siteline** | product (sub-side pay apps + waivers + compliance) | commercial trade contractors billing multiple projects/mo — the funded head-on neighbor | Custom annual contracts on billing volume, demo-gated; implementation fee; **lien rights is a paid add-on** (H07-E16) | Sales-led, no self-serve, no published price — structurally above the 0–1-office-person sub; $18.4M raised, Series A Feb 2022, no growth round found since; forms library (23k forms/17k GCs) proves the moat shape but the small tier is visibly still on Excel (H07-E5) |
| **GC portals: Oracle Textura, GCPay (Sage), Procore Pay, Trimble Pay (ex-Flashtract)** | products serving the GC | ENR-class GCs down to mid-market; sub is invited user | GC quote-based $500–$8,000+/mo (H07-E15/E28); **Textura charges the sub 0.22% of contract, $5k cap** (H07-E14) | Solve the GC's intake, multiply the sub's output formats (N GCs = N portals); consolidation 2021–2024 (Levelset→Procore $500M; Flashtract→Trimble) moved both young payment-chain startups to the GC side (H07-E10/E12/E13) |
| **Per-document notice services: SunRay, NCS, National Lien & Bond, Texas Easy Lien** | service | subs/suppliers, often single-state | $25–$59/notice; $299 lien affidavit; no monthly fees (H07-E18/E22) | Single-document scope: no pay-app cycle, no waiver tracking, no retainage ledger; deadline responsibility stays with the sub |
| **DrawFort** | product (new, low-end) | subs/small GCs wanting self-serve | Free tier, **$34/mo flat**, published (H07-E17) | Pay-app PDF math only — explicitly no lien waivers, no deadlines, no GC network; proves demand below the demo-gate while leaving the chain unowned |
| **In-house clerk + Excel + email** | headcount/DIY (the real incumbent) | everyone; universal below ~$5M | $47k–$65k salary or owner nights; Excel "not working out well" (H07-E5/E27) | Error-prone single point of failure; statutory deadlines forfeited silently (FL day-46 = rights gone); doesn't scale past ~10 projects |
| **Construction attorneys** | service (escalation) | any sub, after it breaks | $361/hr avg TX; $1,000–$2,500/lien; disputes $10k–$55k (H07-E4/E22) | After-the-fact; a lien "won't get you paid sooner" when owners drag closeout (H07-E4); no prevention |
| **Fintech: Billd, Constrafor, factoring, title-company escrow** | service (financing) | subs with credit; GC-sponsored programs | 2.99%/mo + 2% fee; ~2%/invoice for 48-hr pay; title escrow per-project (H07-E23, H07-E5) | Prices the delay instead of compressing it; stacks cost on thin margins; Constrafor requires the GC to sponsor |
| **Do nothing (LOC + wait)** | DIY | default | LOC interest; retainage written off late | The $299B/yr "14% hidden tax" (H07-E24); millwork sub near "breaking the bank" (H07-E3) |

**Deep-verification of the closest three:**
- **Levelset/Procore:** $500M acquisition closed 2021-11-02 at ~$25M ARR (H07-E10/E11). Strategy since: Procore Pay GA'd 2023 for GCs with "the digital lien waiver management system derived from… Levelset" integrated (H07-E12) — the payor is the customer now. Sub-side levelset.com still transacts per-document at $59, subscriptions demo-gated (H07-E6/E7), while 2026 reviews document support decay and removal of the sub-facing GC-vetting data asset (H07-E9). Verdict: **the sub side is a harvested cash flow, not a defended franchise — but the brand + SEO library still dominate discovery.**
- **Siteline:** the same wedge one segment up. Demo-gated volume-priced annual contracts, unlimited seats, lien rights as add-on (H07-E16); $15M Series A Feb 2022 led by Menlo, ~$18.4M total, no subsequent round found in public trackers — 4.5 years on a Series A implies either quiet efficiency or constrained growth; either way its motion (sales-led, ERP-integrated) prices out the 0–1-office-person sub. Its "23,000+ forms from 17,000+ GCs" is exactly the accumulating asset this hypothesis's moat predicts.
- **Trimble/Flashtract:** acquired 2024-05-08, rebranded Trimble Pay, aimed at contractors on Viewpoint Vista (H07-E13) — confirms the pattern: every funded payment-chain product ends up sold to the payor side, because that's where enterprise ACVs are. The sub side keeps being structurally orphaned.

**The unserved segment, stated precisely:** subs below ~$5M revenue — too small for Siteline's sales motion and Levelset's $149+/user subscriptions, too complex for DrawFort's PDF math, currently on Excel + a-la-carte notice services + the owner's evenings. Crowded-but-vacated: the incumbents' own pricing pages, review cohorts, and M&A destinations are the proof.

## 4. The wedge

**"The payment desk for small subs":** self-serve, published-price product that runs the whole monthly get-paid ritual for a sub with 3–25 active projects. Six features:

1. **Project intake → deadline lattice.** Contract/SOV upload (PDF/CSV; agent-extracted); auto-generates the per-state, per-project lien-rights calendar (prelim notice, TX monthly notices, lien window, bond claim) with escalating alerts. Launch states: TX, FL, CA, AZ, GA (largest volume + strictest forfeiture rules).
2. **Notice engine.** Statutory preliminary/monthly notices generated and dispatched (print+certified mail via API), flat-priced or bundled — undercutting the $35–$59 per-notice market the sub already pays.
3. **Pay-app assembly.** SOV progress → G702/G703 + GC-specific formats, per-GC billing-cutoff calendar, one-click monthly package (pay app + matching conditional waiver) ready for portal upload or email.
4. **Waiver desk, both directions.** Statutory conditional/unconditional, progress/final forms; tracks what's owed to the GC and what's outstanding from the sub's own sub-tier/suppliers before releasing their payments.
5. **Retainage ledger + closeout push.** Per-project withheld/billed/released; at scope completion, auto-drafts the "line-item closeout" request the GC-side commenter says actually works (H07-E2), then demand letters on aging.
6. **AR + escalation handoff.** Aging vs contract terms with lien-deadline countdown; one-click handoff to a filing service/attorney network. **We do not file liens or give legal advice** (per-document prep from statutory forms — the SunRay/Texas Easy Lien non-law-firm service model).

**Explicitly not:** money movement/payments, financing, GC-side tools, ERP replacement, automated portal submission (v1 produces the portal-ready package; the human pastes — that's minutes once assembly is done). Integration surface: QuickBooks/CSV import, PDF/email out, mail API.

**≤90 days, founder + agents? Yes.** The build is document generation + a rules/deadline engine + templates — no payments rails, no partner APIs on the critical path. Agents do the two labor-heavy parts: extracting SOV/contract terms from PDFs, and building/maintaining the 5-state statutory table + per-GC format library (each with attorney review — a bounded services cost). DrawFort shipping pay-app math at $34/mo shows the core is small; the compound (notices + waivers + retainage + deadlines) is the product.

## 5. Forcing function & why now

**Forcing function — grade A (held regime):** two interlocking clocks. (1) *Contractual:* each GC's monthly billing cutoff — miss it, cash slips 30 days (postings: "100–200 invoices per billing cycle"). (2) *Statutory:* notice/lien deadlines that extinguish rights — FL's NTO "RECEIVED by the 45th day… otherwise you forfeit your lien and bond claim rights," CA's 20-day rule, TX's monthly notices (H07-E19/E20/E21). These are state statutes, not agency promises — the deadline class that held throughout the sweep. "Millions of notices are sent to contractors each year" (Levelset's own content, H07-E21).

**Why now (2024–2026):**
- **The sub side was orphaned by consolidation.** Levelset → Procore (2021, $500M) with its waiver tech redeployed into GC-side Procore Pay (2023); Flashtract → Trimble Pay (2024, Viewpoint Vista). Jan 2026 reviews document the sub-side decay: support unresponsive, GC payment-history vetting removed (H07-E9/E10/E12/E13).
- **The float got expensive.** High-rate era prices the 55–120-day cycle at Billd's 2.99%/mo / Constrafor's ~2% per invoice (H07-E23); Rabbet's slow-payment cost climbed $273B → $280B → $299B, "a hidden 14% tax" (H07-E24).
- **Statutes keep moving** — states amend retainage/prompt-pay rules continuously (ASA's standing agenda and wins, H07-E26), so the compliance table is a living asset, not a one-time build.
- **Agents changed the economics** of exactly the two things that kept this tier unserved: bespoke per-GC formatting and 50-state statutory upkeep.

## 6. Distribution plan (solo-founder realistic)

First 10 customers, by named channel:
1. **r/Construction and trade subreddits** — the threads above are live solution-seeking ("Is anyone using a lien waiver software that works well?"); the OPs of H07-E1/E3/E5 are literal prospect archetypes. Direct, honest participation + a free per-state deadline calculator as the hook.
2. **ASA chapters** (~35 locals, "thousands" of member businesses) — the association's own agenda is "prompt payment, retainage, standard contract language" (H07-E26); chapter-meeting demos and newsletter sponsorships are cheap and on-topic. CFMA locals reach the billing coordinator herself.
3. **Supplier credit desks** — material suppliers send their own notices (SunRay's clientele) and watch their sub customers' solvency; a referral motion ("your customer pays you faster when they get paid") aligns incentives.
4. **Construction attorneys** — present in the threads (H07-E4); they see the failures and can't economically serve the $2k matters; two-way referral (we hand them lien filings, they hand us prevention).
5. **Trade Facebook groups** (electrician/plumber/GC owner groups — sizes unverified; labeled hypothesis) and construction-finance YouTube/podcasts.

**Sales cycle:** owner decision, days-to-weeks; self-serve trial mandatory (the segment demonstrably won't book demos — that's the gap). **Pricing hypothesis:** $149–$349/mo flat by active-project count, notices included (mail at cost) — anchored between DrawFort's $34 (too thin), SunRay's per-document $25–35, Levelset's $149/user/mo + $59/notice, and 0.3–0.7% of a clerk's salary. Comparable-price evidence: H07-E6/E8/E17/E18.

## 7. AI-structural advantage

The incumbents' economics require either enterprise ACV (Siteline/Textura/GCPay sales motions) or per-document take-rates on a sales-gated funnel (Levelset — which needed a quota-carrying expansion team to extract $500k/mo, H07-E11). Serving a $2–4k-ACV customer profitably requires zero-touch onboarding, automated document intelligence (SOV/contract extraction), and near-zero-marginal-cost support — the agent-heavy structure. Agents also collapse the two content problems that acted as fixed costs: the 50-state statutory engine (drafted by agents, reviewed by counsel, monitored for amendments) and the per-GC format library (assembled from customers' own uploaded requirements at ~zero cost — the asset Siteline built manually over years). Procore/Trimble won't chase this tier: their revenue center is the GC, and their Levelset playbook (harvest per-document fees, redeploy tech payor-side) is the observed behavior, not speculation.

## 8. Moat path

What accumulates: (1) **per-GC requirements/format library** — every customer's GCs add templates, cutoffs, and portal quirks (Siteline's "23k forms from 17k GCs" proves this compounds and matters); (2) **living statutory engine** with amendment history — expensive to bootstrap, cheap to maintain at scale, trust-critical; (3) **GC payment-behavior data** — days-to-pay and retainage-release patterns observed across customers; Levelset *retired* its public version of exactly this asset (H07-E9), vacating a defensible community position; (4) **workflow lock-in** — project records, waiver chains, and deadline history make switching mid-project painful. **Thin-wrapper risk: moderate-low.** A GPT-class model can draft one waiver; it cannot hold the deadline lattice, the per-GC library, the mail dispatch, the audit trail, or the liability posture. Honest caveat: the pay-app math itself is commodity (DrawFort ships it at $34/mo) — the moat is the compound plus the data, not any single document.

## 9. Risks & unknowns

1. **Siteline descends with a self-serve tier** (kill-level risk). *Test:* 15 discovery calls with ≤$5M subs including any who evaluated Siteline — did price/contract structure actually block them?; monitor siteline.com/pricing for a published tier; track their hiring (PLG roles = warning).
2. **WTP at the small tier is anchored near zero** (Excel is free; DrawFort $34). *Test:* pre-sell 10 paid pilots at $149–$299/mo off a landing page + deadline calculator through ASA/Reddit; kill threshold: <3 paying pilots in 60 days of trying.
3. **UPL exposure** — notice/waiver generation with deadline advice brushes legal practice. *Test:* attorney opinion letters in the 5 launch states; adopt the SunRay/Texas Easy Lien non-law-firm document-service structure with statutory-form fidelity + attorney-referral network; E&O quote in hand before launch.
4. **A wrong deadline = a customer's forfeited lien = liability + reputation death.** *Test:* per-state legal review pipeline cost; deadline engine ships with citation-to-statute on every date; carry E&O; start with 5 states, not 50.
5. **The real bottleneck is portal data entry, not assembly** — if subs experience the portal paste as the pain, a package-producer disappoints. *Test:* in the same 15 discovery calls, time-and-motion the monthly cycle (assembly vs entry); if entry dominates, validate an assisted-fill browser extension on the sub's own credentials and check Textura/GCPay ToS before promising it.

## 10. Scores

| # | Dimension | Weight | Score | Note |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 4 | Monthly ritual + per-payment waivers + forfeiture deadlines; emotional charge verified ("breaking the bank," "abyss"); not 5 — part of the pain is counterparty behavior software can't move |
| 2 | Budget proof | 15% | 4 | Salaries posted (108 live), Textura's 0.22% sub fee, $25–59/notice services, 2–3%/mo financing, $1k–55k legal; small-tier *software* WTP still thin |
| 3 | Competitive gap | 12% | 3 | ≤$5M tier evidenced on Excel + à-la-carte; Levelset harvested/decaying sub-side; but Siteline sits one tier up and DrawFort nibbles below |
| 4 | Forcing function | 10% | 4 | Statutory forfeiture (A-grade, held) + monthly contractual cutoffs; retainage release itself lacks a payer-side clock |
| 5 | Founder+agents feasibility | 12% | 4 | Doc generation + rules engine + templates in 90 days with 5-state scope; no payment rails on critical path |
| 6 | Distribution reachability | 10% | 3 | ASA/CFMA/Reddit/suppliers named and on-agenda; but Levelset owns the SEO layer and buyers are offline/busy; no founder-domain edge |
| 7 | AI-structural advantage | 8% | 3 | Agents make $2–4k ACV serviceable and collapse statutory/format content costs; incumbents' pricing isn't seat-based, so their resistance is strategic (GC focus) rather than structural |
| 8 | Moat path | 8% | 3 | Per-GC library + statutory engine + payment-behavior data accumulate; commodity core documents |
| 9 | Expansion ceiling | 5% | 3 | Up-market to Siteline's tier, financing referrals, supplier tier, sub-tier network; $500M exit precedent in-category |
| 10 | Durability | 5% | 3 | Statutes durable; cyclical industry; Procore/Siteline AI re-entry possible |

**Weighted: 70/100 → STRONG** (red team decides).

**Hard gates:** No budget proof — **PASS** (headcount, fees, services all verified). Unreachable buyer — **PASS** (owner-operator decision, community channels). Thin-wrapper — **PASS** (deadline lattice + library + dispatch + audit trail). Head-on collision — **PASS WITH CAUTION**: Siteline is the same wedge but demonstrably a different segment (sales-led, volume-priced annual contracts vs a tier still on Excel); this boundary is real today and fragile tomorrow — red team should attack it first. Platform hostage — **PASS** (statutory basis; multi-GC by nature; portal automation excluded from v1). Regulated practice — **PASS WITH DESIGN CONSTRAINT** (non-law-firm document-service structure per SunRay/Texas Easy Lien precedent; attorney network for filings; no legal advice).

**Displacement sentence:** Current solution = Excel + a $47k–$65k billing clerk (or the owner's nights) + $25–$59-per-notice services + Textura's 0.22% sub fee + financing the 55–120-day gap at ~2–3%/mo + $1k–$55k attorney escalations. New product = a $149–$349/mo self-serve payment desk that assembles pay apps, runs waivers both directions, dispatches statutory notices, and countdown-tracks every lien deadline and retainage dollar. The customer switches because ~$3k/yr replaces a $12k–$24k labor fraction plus per-document fees, and because one missed FL day-45 notice forfeits more than a decade of subscription.

## 11. Verdict proposal

**STRONG (70).** The pain, budget, and statutory forcing function are as verified as anything in this program, the QC cloud over the retainage figure is resolved in the evidence's favor, and 2021–2024 M&A demonstrably orphaned the sub side. Held back from PURSUE by two facts: Siteline already owns this wedge one segment up and could ship a self-serve tier at will, and small-tier software WTP is inferred from adjacent spend rather than observed subscriptions. Both resolve cheaply: 15 discovery calls + 10 paid-pilot pre-sells inside 60 days. Recommend advancing to red team with risk #1 and #2 as the designated attack surfaces.

## 12. Evidence ledger

Full ledger: `outputs/evidence/dh07_subcontractor_payments.jsonl` (28 records, H07-E1…E28; carried-forward scout records S03-7-E1…E5 and S08-1-E1…E7 remain in `s03`/`s08` ledgers, with S08-1-E1 superseded by H07-E1).

| ID | Claim (short) | Source | Status |
|---|---|---|---|
| E1 | Retainage "$50" is OP typo; corrected "$50k" twice in-thread; 6 mo frozen, pay-if-paid | r/Construction 1uehqtf (Arctic Shift) | verified verbatim |
| E2 | 5% retainage 3–4+ yrs; "early release is extra paperwork nobody owns" | same thread | verified verbatim |
| E3 | 55-day first payment, $597k sub; "60–90 days and there's no budging"; DSO 60–108d | r/Construction 1jbx8rh | verified verbatim |
| E4 | $10k+ lawyer fees, 1yr-old pay app; $55k arbitration; FL attorney in-thread | r/Construction 1kp0050 | verified verbatim |
| E5 | Excel failing; Levelset "buddy… good price"; title-escrow; RevnuPros | r/Construction 1bpe857 | verified verbatim |
| E6/E7 | Levelset $59/notice, $349/lien, subscriptions sales-gated | levelset.com | verified (today) |
| E8/E9 | $149/user/mo; "not a good match for any small business"; Jan-2026 support decay; GC-vetting tools removed post-Procore | Software Advice; Trustpilot | verified quotes |
| E10–E13 | Levelset→Procore $500M at ~$25M ARR; tech → GC-side Procore Pay (2023); Flashtract→Trimble Pay (2024) | Procore/SEC; GTM Newsletter; Trimble | verified |
| E14/E15 | Textura sub fee 0.22%/$5k cap/$100 sub-tier; GCPay GC-pays quote-based | Oracle docs; GCPay | verified |
| E16/E17 | Siteline demo-gated volume pricing, lien add-on, 23k forms/17k GCs, $18.4M; DrawFort $34/mo pay-app-only | siteline.com; drawfort.com | verified |
| E18–E22 | SunRay $25–35/notice; FL day-45 forfeiture; CA 20-day/TX monthly/AZ 20; "millions of notices"/yr; attorney $361/hr, $1,000–2,500/lien | SunRay; NLB; Levelset library; Texas Easy Lien | verified |
| E23–E25 | Billd 2.99%/mo/120-day; Constrafor ~2%/invoice, $106M; Rabbet $280B/$299B "14% tax"; retainage ≥ 5–10% margins | vendor pricing; TechCrunch; Rabbet; Siteline guide | verified |
| E26/E27 | ASA agenda = prompt pay/retainage, "thousands" of members; 108 live clerk postings, Vaco $62–65k live | asaonline.com; bebee | verified (today) |
| E28 | Levelset $400–800/mo GC plans; "reduced development investment outside Procore ecosystem" | US Tech Automations comparison | **low-trust, vendor-adjacent — color only** |
