# Opportunity Dossier — Prior-Auth Production Line for Small Specialty Practices

Validator: Wave-2 validator, H03 · Date: 2026-08-27 · Source hypothesis: H03 (Manager 1 promotion memo, Rank 3, ★TOP-5) · Ground(s): 03 (human-middleware jobs), 05 (back-office pros), 11 (services-to-software)

**Validator's headline:** The pain, budget, and forcing function all re-verified and got *stronger* (WISeR now puts prior auth into traditional Medicare; MGMA April 2026 says burden still rising). But the competitive picture moved hard against the hypothesis in the 14 months before this validation: this is now the most heavily funded zone in healthcare AI (~$300M+ raised across seven named startups since 2024), and on **2026-06-23 Humata Health opened an early-access waitlist for exactly the "independent practices and specialty clinics" segment** this hypothesis claims. A defensible slice survives — procedural/imaging/surgical PA for small non-athenaOne specialty practices, attacked at the **evidence-assembly** step through billing companies — but it is a closing window and a race, not white space. Proposed verdict: **STRONG (73), conditional** — strongest as the shared-buyer bundle expansion behind H01/H02 rather than a standalone lead wedge.

---

## 1. The pain, restated precisely

**Who hurts:** PA-heavy small/independent specialty practices in the US — imaging, GI, interventional pain, ortho, dermatology (surgical), cardiology, urology, oncology (procedures), behavioral health — typically 1–12 providers, plus the small medical-billing companies that inherit their auth work. 40% of physicians employ staff who do *nothing but* prior auth [H03-E1].

**The workflow failure:** For every order, someone must (a) determine whether the payer requires a PA for that CPT × plan, (b) assemble clinical evidence from the EHR to that payer's criteria — chart notes, labs, imaging reports, conservative-therapy history, (c) submit via a specific payer portal, fax, or phone, (d) chase status, (e) track expiration dates and approved units, and (f) manage denials/appeals/peer-to-peers. The evidenced bottleneck is **(b) assembly**, not (c) submission: "the prep is where the day goes. i spend way more time chasing a rendering provider for a note or digging up labs than i ever spend on the submission itself" [H03-E5]. Billers' enumerated failure modes are assembly-and-tracking failures — missing chart notes, missing labs, wrong portal, expired auth dates [H03-E6]. A vendor operating this workflow in production independently confirms the shape: "the hard part isn't the form, it's that the work spans systems with no APIs. Chart is in the EMR, submission is in 10–40 payer portals, each with different forms, logins, MFA" [H03-E33].

**Frequency:** ~40 PAs per physician per week, consuming 13 hrs/wk of physician+staff time [H03-E1]; CAQH clocks each manual PA at 24 min (phone/fax) or 16 min (portal) — 40 × ~20 min ≈ 13 hrs, two independent sources triangulating [H03-E35]. Since 2026-01-01, WISeR adds PA to *traditional Medicare* for 13 service categories in six states [H03-E13], and practices feel it: "Is anyone else's prior auth workload getting worse now that traditional Medicare is doing it too?" (r/CodingandBilling, 2026-04-28) [H03-E15].

**Strongest three artifacts:** (1) AMA 2025 survey — 40/wk, 13 hrs/wk, 40% dedicated staff, 94% burnout, verified exact by Manager 1 [H03-E1]; (2) the staffer's assembly-is-the-day quote [H03-E5]; (3) fresh 2026 buyer voice — a billing firm publicly shopping for the end-to-end workflow, "looking at the patient chart, creating a note/form, submitting to payer, checking status, updating EMR" [H03-E32].

## 2. Budget proof

Money already moving against this pain, per customer per year:

| Line | Evidence | Per-physician/yr arithmetic |
|---|---|---|
| In-house PA specialist wages | $17.90–$25.00/hr posted; 6,971 open postings on one aggregator [H03-E2, E3, E4] | 13 hrs/wk staff-equivalent × 48 wk × $20–25/hr ≈ **$12.5k–15.6k** (staff hours only; physician hours extra) |
| Per-request outsourcing | $5–$15/request (vendor-published) [H03-E7] | ~1,900 requests/yr (40/wk × 48) × $5–15 = **$9.5k–28.5k** |
| Dedicated offshore specialist | $1,000–1,500+/mo, 2-resource minimum [H03-E8] | **$24k–36k+ per practice** |
| In-house all-in estimate | $80–100/request (vendor-published, labeled) [H03-E7] | implies $150k+/physician/yr at full volume — treat as ceiling, labeled vendor math |
| Software comparable | Myndshft ≈ $750/mo estimated for 1–3 providers [H03-E30] | **~$9k/practice/yr** — proves a paid down-market software price point exists |
| Downstream leakage | 10.4% of denied claims were *pre-approved* — auth work feeds denial rework [H03-E9] | ties into H01's $57/claim rework economics |

A 3-physician PA-heavy specialty practice credibly burns **$30k–90k/yr** in wages/services on this workflow. Budget-proof hard gate: **PASS** — salaried headcount (published wages, 6,971 postings), per-unit service prices, and an existing software price point all verified.

## 3. Competitive landscape

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| In-house PA staff | DIY/headcount | every practice | $17.90–25/hr, ~⅓+ FTE/physician [H03-E3,E4] | 13 hrs/wk/physician; turnover; 94% burnout link; still yields pre-approved denials [H03-E1,E9] |
| Offshore BPO / VAs | service | any; billing firms resell | $5–15/request; $1–1.5k/mo/specialist, 2-min [H03-E7,E8] | still human-speed; quality varies; billing firm in [H03-E32] is shopping *away* from BPOs |
| Payer portals + fax (Availity Essentials baseline) | stack ("do nothing") | all practices | free | "portal-based only; no automation of documentation compilation" [H03-E31]; OAA bans bots/scraping [H03-E34] |
| athenaOne Authorization Management | EHR-native co-sourcing | athenaOne practices only | add-on Service Fee (contract) | Binding service description **excludes** DME, therapy pre-certs, meds, labs, POCT, retro-auths, pre-determinations, **appeals**, **inbound orders**, and **IPA payers** [H03-E29] |
| eCW / Epic native ePA features | EHR modules | their installed bases | bundled | eCW shipped PA *indicators* + payer sends (2025) and an agent platform (HIMSS26) — trajectory real, coverage uneven today [H03-E37] |
| CoverMyMeds | product (free) | all prescribers | free | pharmacy/Rx PA only; "procedural PA coverage is incomplete" [H03-E30] |
| SamaCare | product (free, pharma-funded) | specialty practices — retina, onc, rheum, neuro infusion | free to practices | **medical-benefit drugs only** (1M+ PAs); procedures/imaging/surgery out of scope; coverage follows pharma sponsorship [H03-E27] |
| Silna Health ($27M, Accel/Bain) | product | **small therapy practices** — ABA, PT, OT, speech, behavioral | undisclosed | owns the therapy slice; no evidence of procedural specialties (GI, pain, imaging) [H03-E25] |
| Humata Health ($25M) | product | large health systems; **June 2026: waitlist for independent/specialty practices** | undisclosed, waitlist | practice product is drag-and-drop + doc *scoring* — **no EHR integration; the practice still finds and uploads the documents**; not GA [H03-E21,E22] |
| Latent ($80M, $600M val) | product | top-20 health systems, pharmacy/med access | enterprise | explicitly health-system GTM [H03-E23] |
| Tennr ($101M, $605M val) | product | *receiving* providers (DME, imaging) — inbound referral docs | enterprise-ish | referral-intake slice; not the practice-side outbound PA queue [H03-E24] |
| Develop Health ($17.6M) | product | prescribers/digital health — medication PA | undisclosed | drug lane only [H03-E26] |
| Myndshft | product | small–mid specialty, procedural | ≈$750/mo est. (1–3 providers) [H03-E30] | EHR-integration dependent (~270 EHRs); rules engine, not chart-assembly agent |
| Cohere ($200M+) / Anterior ($64M) / Rhyme / Availity AuthAI | payer-side / network | payers; 83 largest provider orgs (Rhyme) | N/A to practices | not purchasable by practices; AuthAI only where a payer activates it [H03-E19,E20,E28,E30] |
| Seed-stage agents: Asteroid AI, Datarovers, Linear Health, EasyPA | products (2025–26 entrants) | billing firms; athena specialty practices | undisclosed; Linear needs ~100+ PAs/mo | pitching in the same Reddit threads [H03-E33]; Linear athena-only [H03-E31]; unproven, but proof the wedge is visible to everyone |

**Deep-dives on the 3 closest:**
- **Humata** — the central threat. Funding $25M (Blue Venture Fund/LRVHealth/Optum — distribution-shaped investors) [H03-E21]. Shipping velocity: health-system product live (Allegheny "touchless" PA); practice product announced 2026-06-23, **waitlist only, no GA date, no pricing** [H03-E22]. Segment focus: moving down-market from systems. Roadmap tell: their own release concedes practices "historically have navigated the process without dedicated technology" — incumbent admission the segment was unserved — and their practice product deliberately skips EHR integration (drag-and-drop), leaving the assembly step manual. Window: whatever time waitlist→GA→small-practice pricing takes, likely 6–18 months.
- **Silna** — $27M, shipped, real customers in ABA/PT/OT/SLP/behavioral [H03-E25]. For those verticals this is a head-on collision — the wedge must *exclude* therapy. No evidence they cover procedural specialties yet; expansion risk is real (same playbook, adjacent specialty).
- **SamaCare** — free (pharma-funded), 1M+ PAs, ModMed/AmerisourceBergen channels, 4.4★ G2 [H03-E27]. Owns drug PA in specialty practices; any wedge that includes buy-and-bill drug auths competes with free. Exclude drugs.

**Why the funded players skip(ped) the small-procedural segment (evidenced, not asserted):** enterprise ACV economics (Rhyme: "83 of the largest providers"; Latent: top-20 systems) [H03-E28,E23]; payer-side monetization concentrates where review labor cost sits (Anterior/Cohere sell to plans) [H03-E19,E20]; the free products are funded by pharma and therefore stop at drugs [H03-E27]; and the small end means 10–40 portals × dozens of EHRs × tiny ACVs — exactly the fragmentation a browser-agent + FHIR approach now makes tractable, which is why seed entrants and Humata all arrived in 2025–26.

**The surviving unserved slice, precisely:** outbound **procedural/imaging/surgical** PA (not drugs, not therapy verticals, not athenaOne practices) at 1–12-provider specialty practices and the billing companies serving them — where the work that eats the day is **assembly from the practice's own EHR**, which neither the free portals ("no automation of documentation compilation" [H03-E31]), nor SamaCare (drugs), nor Humata's drag-and-drop practice portal (practice still uploads), nor athena's service (excludes appeals/inbound/IPA/DME/therapy [H03-E29]) performs today.

## 4. The wedge

Smallest product that removes the pain for one segment — **"the PA back office that reads your chart"** for 2 launch specialties (GI + interventional pain/ortho, the latter chosen because WISeR just imposed brand-new traditional-Medicare PA on their highest-volume codes in six states [H03-E13]):

1. **Order-watch + PA-required determination** — monitors scheduled procedures/orders (EHR read), answers "does this CPT × this plan need auth?" from a maintained payer-rule library incl. WISeR code lists.
2. **Evidence-packet assembly from the chart** — agent pulls notes, labs, imaging, conservative-therapy history via the EHR's certified FHIR/SMART API [H03-E36], maps them to the payer's documentation checklist, flags what's missing, and drafts the chase message to the ordering/rendering provider (the step the staffer artifact says eats the day [H03-E5]).
3. **Draft submission with human approve** — pre-filled payer form (portal via supervised browser automation with the practice's credentials, ePA rails, or fax), staff one-click review-and-submit; clinician signs anything clinical.
4. **Clock + expiration tracking** — status chase against the CMS-0057-F 72h/7-day decision clocks (live since Jan 2026 [H03-E10]) and WISeR timelines; expiration/units tied to the schedule (the tracked-by-hand duty in postings [H03-E3]).
5. **Denial packet assembly** — captures the now-mandatory specific denial reason [H03-E10], assembles the appeal-ready evidence bundle and peer-to-peer prep sheet (athena's service explicitly won't do appeals [H03-E29]).
6. **Full per-auth audit trail** of what the agent did.

**Explicitly does NOT do:** drug/pharmacy PA (CoverMyMeds/SamaCare/Develop own it, partly free); therapy-vertical intake (Silna); payer-side review; autonomous medical-necessity judgment (clinician retains sign-off — regulated-practice gate); claims/billing; athenaOne practices (served, and athena's API posture makes them the wrong first target).

**Integration surface:** FHIR R4/SMART on certified EHRs (eCW, ModMed, AdvancedMD, Tebra tier) [H03-E36]; payer portals via credentialed, supervised browser automation with fax/phone fallback (ToS risk managed — see §9); CMS-0057-F payer PA APIs adopted as they arrive in 2027 (the wedge sits a layer above them).

**≤90 days, founder + agents?** Yes, honestly — *as a concierge-plus-agent design-partner build*: 2 specialties, 5–10 payer/portal combos, 1–2 EHR integrations, human-in-the-loop on every submission. The payer-criteria library is seeded per design partner, not built universally. What does NOT fit in 90 days: broad EHR coverage, SOC 2 (start), touchless submission. The billing-company channel reduces integration surface (they already hold portal credentials and EHR access across clients). Precedent that the workflow is agent-runnable in production at seed scale: [H03-E33].

## 5. Forcing function & why now

- **Always-on money gate (grade A):** no auth, no procedure revenue — per-order, ~40×/wk/physician [H03-E1]; auth expirations create recurring hard deadlines [H03-E3].
- **CMS-0057-F (grade B, held so far):** decision clocks + specific denial reasons **live since 2026-01-01** (with 2026 enforcement discretion), payer FHIR PA APIs due **2027-01-01**, enforcement 2027-04-01 [H03-E10, E11]. Critically, the rule *excludes drugs* [H03-E12] and *exempts* self-insured employer plans, most commercial, and (except WISeR) traditional Medicare [H03-E11] — so the API wave standardizes only part of the surface and **does not erase the assembly wedge** (the API moves forms and status; the practice still has to find and attach the clinical evidence).
- **WISeR (new since promotion, grade B+):** PA arrived in traditional Medicare 2026-01-01 for six years in AZ/NJ/OH/OK/TX/WA — skin substitutes, epidural steroid injections, cervical fusion, knee procedures, nerve stimulators, etc.; AI reviewers paid a share of denial savings; survived the Senate CRA vote 46–50 on 2026-07-16 [H03-E13, E14]. A dated, live, geographically targetable demand event with zero incumbent tooling for the affected small practices.
- **What changed 2024–2026:** payers automated first (Cohere: ~85% real-time decisions [H03-E20]; WISeR is payer-side AI in Medicare itself) while the practice side still works by phone/fax/portal — the asymmetric-AI pattern Manager 1 flagged program-wide; AMA (May 2026) and MGMA (Apr 2026) both show burden *rising* a year into the payers' own reform pledge [H03-E1, E16, E18].

## 6. Distribution plan (solo-founder realistic)

First 10 customers, by named channel:
1. **Billing companies (the multiplier buyer):** r/CodingandBilling (31,998 members) has billing firms openly shopping for exactly this [H03-E32]; HBMA (hbma.org) membership/conference is the trade channel. One 20-client billing firm = 20 practices behind one integration and one BAA.
2. **The 6,971 job postings** [H03-E2]: practices currently hiring a PA specialist are self-identified, reachable buyers with budget already approved — direct outreach list ("before you fill the req…").
3. **WISeR six states:** CMS publishes the affected CPT lists — build a free "WISeR readiness checker" for pain/ortho/wound-care practices in TX/OH/NJ/AZ/WA/OK; ASIPP (pain societies) and state MGMA chapters are the watering holes; MGMA's own 2026 report makes PA the #1 member issue [H03-E16].
4. **Specialty administrator associations:** AAOE (ortho practice executives), ADAM (dermatology administrators), Community Oncology Alliance — small-conference sponsorships within solo-founder budget.

**Sales cycle estimate:** 30–90 days SMB (practice admin + physician-owner sign-off; BAA required). **Price/packaging hypothesis:** $500–1,500/mo per practice, or $2–4/auth — priced under the $5–15/request human outsourcers [H03-E7] and around the Myndshft ~$750/mo comparable [H03-E30]; billing-company OEM at per-auth wholesale. Comparable-price evidence: [H03-E7, E8, E30].

## 7. AI-structural advantage

The billable unit today is human minutes (16–24 min/auth [H03-E35]) sold at $5–15/request or $17.90–25/hr [H03-E7, E3]. An agent team collapses the assembly-submission-tracking loop to cents of inference plus a human review click — 10x under the cheapest offshore price at software margins. Incumbent resistance: EHR vendors monetize seats/percent-of-collections and athena's answer is *co-sourced humans* with a binding exclusions list [H03-E29]; payer-side vendors (Cohere/Anterior) are paid by the entity whose costs the practice-side agent inflicts; outsourcers' revenue *is* the labor line. None can chase per-auth software pricing without breaking their model. The founder's agent-heavy team is also the right shape for the long tail of payer-portal permutations that made this segment uneconomic for enterprise vendors — that fragmentation is the segment's historical moat-against-incumbents [H03-E33].

## 8. Moat path

**Accumulates with usage:** (1) payer-criteria/documentation-requirements corpus (payer × plan × CPT × state, incl. WISeR), maintained by live submissions; (2) approval-outcome data — which evidence packets got approved where (the asset SamaCare brags about on the drug side [H03-E27]); (3) portal-automation coverage map + exception handling; (4) EHR integrations; (5) workflow lock-in via expiration/units tracking tied to scheduling; (6) with H01/H02, the shared payer-portal + EHR spine across three products.

**Thin-wrapper honesty:** submission alone is thin — payer FHIR APIs (2027) + EHR-native ePA will commoditize form-filling; Humata's doc-scoring shows criteria-matching is replicable by better-funded teams. The durable pieces are the outcome-labeled criteria corpus, the multi-system glue (EHR↔portal↔schedule), and the audit/trust layer — real but **moderate**; this is a workflow-and-data business that must out-execute, not a structural monopoly. Hard gate: passes (workflow + integration depth + accumulated data ≠ one model call), scored honestly low.

## 9. Risks & unknowns (top 5, each with its test)

1. **Humata (or Myndshft/Linear/Silna-expansion) GAs down-market before entry** — *the* risk [H03-E22, E25, E30]. Test (30 days): join Humata's waitlist; demo Myndshft/Linear; interview 5 practices that evaluated any of them. Kill/reposition trigger: Humata GA at <$1k/mo *with chart-pull assembly* (not drag-and-drop).
2. **Portal automation ToS/enforcement** — Availity OAA bans bots with termination + legal action reserved [H03-E34]. Test: counsel review; pilot volume through practice-credentialed supervised automation and measure block/challenge rate; maintain fax/phone/ePA fallback; track CMS-0057 API availability per payer. Mitigant: multiple funded vendors already run portal submission at scale (SamaCare 1M+ [H03-E27]).
3. **Payer reform shrinks the pain surface** — AHIP pledge: volume reductions by 2026, 80% real-time ePA by 2027 [H03-E17]. Test: quarterly tracking of PA-list changes for the two launch specialties' top-10 payers. Current data says burden still rising (AMA May 2026, MGMA Apr 2026 [H03-E1, E16]) and NHeLP calls the pledge unaccountable [H03-E18] — but real-time approval of *clean* submissions actually helps an assembly product (its packet becomes the auto-approval input).
4. **EHR read-access friction** — g(10) FHIR is mandated [H03-E36], but marketplace approvals, per-vendor fees, and write-back limits vary. Test (first 30 days): register a SMART app with eCW + ModMed + one more; measure time-to-chart for 3 design partners; fallback = billing-company-held EHR credentials.
5. **Trust/liability bar for a solo founder** — a missed auth = unpaid procedure (potentially $10k+); buyers may default to humans they can blame; BAA/SOC 2 expectations. Test: 10 discovery interviews (≥3 billing companies) + 2 paid pilots at ≥$500/mo within 60 days sourced from r/CodingandBilling/HBMA; kill if zero conversion on a money-back pilot. Sub-risk: WISeR politics (survived July 2026 vote but contested [H03-E14]) — never let WISeR exceed ~⅓ of pipeline.

## 10. Scores

| # | Dimension | Weight | Score | Note |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 5 | 40/wk, 13 hrs/wk, 94% burnout; rising through 2026 [E1,E16] |
| 2 | Budget proof | 15% | 5 | wages + $5–15/request + $1–1.5k/mo + $750/mo software comp [E2,E3,E7,E8,E30] |
| 3 | Competitive gap | 12% | 2 | gap exists but is narrow, precisely bounded, and being entered (Humata waitlist; Silna therapy; seed agents) [E22,E25,E33] |
| 4 | Forcing function | 10% | 4 | per-order money gate live; CMS clocks live Jan 2026; WISeR live; API dates grade B [E10,E13] |
| 5 | Founder+agents feasibility | 12% | 3 | 90-day concierge wedge credible for 2 specialties; BAA/marketplace/trust weight is real |
| 6 | Distribution reachability | 10% | 3 | named channels + self-identifying buyers (job posts, shopping threads); but medical SMB trust cycle and channel noise |
| 7 | AI-structural advantage | 8% | 4 | collapses a published per-unit labor price; incumbents' models resist following |
| 8 | Moat path | 8% | 3 | outcome-labeled criteria corpus + integrations accumulate; submission layer commoditizes 2027 |
| 9 | Expansion ceiling | 5% | 4 | natural bundle with H01 denials + H02 credentialing = payer-facing back office for the same buyer |
| 10 | Durability | 5% | 2 | payer real-time ePA, EHR-native AI (eCW/athena), and volume-reduction pledges all aim at this pain [E17,E37] |
| | **Total (normalized)** | | **73/100** | STRONG band (70–79: red team decides) |

**Hard gates:** Budget proof PASS · Buyer reachability PASS (SMB + billing companies, no enterprise procurement) · Thin-wrapper PASS-with-flag (workflow/data depth required and planned; §8 honesty stands) · Head-on collision **PASS ONLY WITH the §3/§4 exclusions** (exclude therapy verticals→Silna, drug PA→SamaCare/CoverMyMeds, athenaOne base→athena; Humata is announced-not-GA in the remaining slice — this gate flips to FAIL if Humata GAs broadly before entry) · Platform hostage PASS (multi-payer, multi-portal, fax/phone/API alternatives; Availity ToS is a managed risk, not a single-platform dependency) · Regulated practice PASS (clinician retains all medical-necessity judgment; product assembles and files).

**Displacement sentence:** Current solution = a $17.90–25/hr PA specialist (~⅓+ FTE per physician) or a $5–15/request / $1,000–1,500/mo outsourcer, spending 16–24 min per auth across 10–40 portals. New product = a chart-reading PA agent ($500–1,500/mo or $2–4/auth) that assembles the evidence packet, files it, and runs the clocks. The customer switches because the same 40 auths/physician/week cost roughly half the cheapest human alternative, with an audit trail, no turnover, and appeal packets the EHR-native service contractually refuses to produce.

## 11. Verdict proposal

**STRONG (73) — conditional.** Pain/budget/forcing all re-verified and strengthening (WISeR, MGMA 2026). But the funding zone is crowded and Humata's June 2026 practice-portal waitlist targets this exact segment — the window is open only in the assembly-first, procedural, non-athena, non-therapy slice, and only for a fast mover through billing companies. **Bundle assessment: H03's strongest form is not standalone.** H01/H02/H03 share one buyer (practice admin/billing company), one integration spine (EHR read + payer portals + payer-rule library), and one channel (r/CodingandBilling, HBMA, MGMA); PA failures literally feed H01's denial pipeline (10.4% of denials were pre-approved) and H02's enrollment gates PA validity. Recommend red team evaluate H03 as the expansion module of a "payer-facing back office" bundle led by whichever of H01/H02 scores cleanest — and kill H03 standalone if Humata GAs with chart-pull assembly under $1k/mo.

## 12. Evidence ledger

JSONL at `outputs/evidence/dh03_prior_auth.jsonl` — 37 records, claim IDs H03-E1…H03-E37, all access-dated 2026-08-27. Carried-forward claims (E1–E10) were spot-verified by Manager 1 or drawn from schema-valid scout ledgers (s03/s05/s11); fresh claims (E11–E37) were newly fetched this validation. cms.gov remains bot-walled: E10/E12 are cited to the CMS URLs with capture method disclosed and independent corroborators (E11, health-samurai in s11 ledger).

| Claim ID | Anchor fact | Source type | Status |
|---|---|---|---|
| H03-E1 | AMA 2025: 40 PAs/wk, 13 hrs/wk, 40% dedicated staff, 94% burnout | official-doc | verified (M1 spot-check) |
| H03-E2 | 6,971 open PA-specialist postings | job-posting | verified (M1 spot-check) |
| H03-E3/E4 | $17.90–25/hr posted wages, portal/fax/appeal duties | job-posting | verified |
| H03-E5 | "the prep is where the day goes" (assembly bottleneck) | forum-post | verified (Arctic Shift) |
| H03-E6 | Failure modes: missing notes/labs, wrong portal, expired auths | forum-post | verified |
| H03-E7/E8 | $5–15/request outsourcing; $1–1.5k/mo offshore specialist | pricing-page | vendor-published, labeled |
| H03-E9 | 10.4% of denials were pre-approved (Premier) | official-doc | verified |
| H03-E10/E11/E12 | CMS-0057-F: Jan-2026 clocks, Jan-2027 APIs; commercial/ERISA/Medicare-FFS exempt; drugs excluded | regulator (+vendor corroborator) | cms.gov bot-walled, disclosed; corroborated |
| H03-E13/E14/E15 | WISeR live Jan 2026, 6 states, survived Senate 46–50 Jul 2026; operator thread | research-org/news/forum | fresh, verified |
| H03-E16 | MGMA Apr 2026: ~95% burden up; PA top issue | official-doc | fresh |
| H03-E17/E18 | AHIP pledge terms; NHeLP "no accountability" critique | official-doc/research-org | fresh |
| H03-E19–E28 | Funded competitor map: Anterior $64M (payer), Cohere $200M+ (payer), Humata $25M, Latent $80M, Tennr $101M, Silna $27M, Develop $17.6M, SamaCare free/1M PAs, Rhyme 83-largest | news/vendor | fresh |
| H03-E22 | Humata practice-segment waitlist launch 2026-06-23 | news | fresh — the load-bearing threat |
| H03-E29 | athenaOne Auth Mgmt binding exclusions (appeals, DME, therapy, meds, inbound, IPA) | vendor-doc (legal) | fresh, primary PDF |
| H03-E30/E31 | Down-market price points (Myndshft ~$750/mo); Availity "no documentation compilation"; Linear Health profile | news/vendor | fresh, labeled |
| H03-E32/E33 | Billing firm shopping for end-to-end PA; Asteroid AI selling the same wedge in-thread | forum-post | fresh (Arctic Shift) |
| H03-E34 | Availity OAA anti-bot clause verbatim | legal-doc | fresh, primary PDF |
| H03-E35 | CAQH 2024: 16–24 min per PA | research-org | fresh |
| H03-E36 | ONC g(10): certified-EHR FHIR/SMART APIs mandatory since Dec 2022 | regulator | fresh |
| H03-E37 | eCW native PA indicators + agent platform | news | fresh |
