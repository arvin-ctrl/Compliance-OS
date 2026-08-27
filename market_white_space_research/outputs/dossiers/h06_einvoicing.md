# Opportunity Dossier — EU E-Invoicing Onboarding for SMEs & Freelancers

Validator: Wave-2 validator, H06 · Date: 2026-08-27 · Source hypothesis: H06 (Manager 1 promotion memo, rank 6) · Ground(s): 02 (regulatory deadlines; single-ground promotion, S02-3)

**Headline finding:** the mandate map verified perfectly — this is the strongest forcing-function class in the program (statutory, per-invoice, dates executed or days away). And that is exactly why the wedge is gone. Tested country by country against the H04 failure mode (mandate verifies hard → incumbents race to the same layer → free offerings erase the wedge), H06 fails the head-on gate **in all four countries, harder than H04 did in one**: Poland's tax ministry ships three free apps and says so on gov.pl ("free tools are sufficient"); Belgium has a Let's-Encrypt-style free open-source access point plus free suite tiers plus a 120% state subsidy for buying incumbent software; France has **nine** accredited platforms with €0 full-compliance plans (including neobanks Qonto and Shine) out of 137–147 registered platforms; Germany's obligation is currently "have an email inbox," with free generators everywhere. The founding "€2,000/yr Peppol" complaint turns out to be the fee for *operating an access point*, which no SME needs. Proposal: KILL, with recorded re-open conditions.

## 1. The pain, restated precisely

**Who hurts:** VAT-registered SMEs and freelancers established in Belgium (~1.2M entities, mandate live 2026-01-01), Poland (all VAT businesses since 2026-04-01 via the state KSeF platform), France (receive-all from 2026-09-01 — five days from access date; SME/micro issuance 2027-09-01), and Germany (receive since 2025-01-01; issue 2027/2028) [H06-E1, E7, E14, E18]. Invoicing stops being a free PDF email and becomes a validated, networked (BE/FR) or state-cleared (PL) data transaction.

**The workflow failure, as verified in 2026:** it is real but *front-loaded and mostly behind us or absorbed*. Belgium: 54% of SMEs waited until the final six months and 20% registered late, but four months post-mandate 49% report time savings vs 31% time loss and residual r/BEFreelance threads are edge-case questions ("Which EV charging card supports Peppol invoicing?"), not tooling distress [H06-E13, E25]. Poland: go-live week produced a 483-point r/Polska thread whose sharpest operator pain is state-schema edge cases *inside existing tools* — "I issue foreign invoices and I'm devastated... Fakturownia throws an error that the NIP is invalid, because the client HAS NO NIP" [H06-E17]. France: a genuine live scramble — 38% of businesses have taken no concrete steps, 40% can't name a platform — but the state announced no sanctions for good-faith companies through end-2026, and freelancer threads resolve to "signed up free in under 10 minutes" [H06-E3, E5].

**Frequency:** per invoice (highest in the program), plus one-time onboarding and per-rejection rework. Carried forward intact.

**Strongest three artifacts:** (1) r/BEFreelance "Peppol is mandatory now — what are you using?" — every answer is a free or €5/mo tool or "whatever my accountant recommended... expensable at more than 100%" [H06-E12]; (2) Ministry of Finance (PL) official page: "Free tools are sufficient for issuing e-invoices in KSeF" [H06-E15]; (3) the nine-free-platform census for France incl. Indy/Tiime/Qonto unlimited-free-no-conditions [H06-E4].

**Correction to carried evidence:** the S02-3 anchor complaint ("2000 euros just for the peppol membership and on top of that you need to get certified") describes OpenPeppol *service-provider* membership — Access-Point-only membership is €1,850/yr + €1,500 certification. End businesses never pay it; they ride an AP at €0–€0.25/invoice [H06-E20, E21, E9]. The scout's pain framing ("forced paid subscriptions replacing free email invoicing") was true as fear in Jan 2025 and is false as outcome in Aug 2026: the market and three governments drove the SME price floor to zero.

## 2. Budget proof

Money moves in this category — but almost none of it through the promoted segment:

| Money flow | Amount | Source |
|---|---|---|
| Freelancer/micro software spend, BE | €0 (Accountable free unlimited Peppol; Let's Peppol; Odoo 1-app; Digivak free) to €4–15/mo (Lucy, Kyte €5, Onfact); Dexxter €180/yr | [H06-E9, E10, E12] |
| State subsidy, BE | 120% tax deduction on e-invoicing software + advice, 2024–2027 (the state pays SMEs to buy incumbent tools) | [H06-E11] |
| Freelancer/micro spend, FR | €0 — nine accredited platforms with free full-compliance plans; Indy/Tiime/Qonto unlimited both directions, no entry conditions | [H06-E4, E5] |
| Micro spend, PL | PLN 0 (three free Ministry of Finance apps; Fakturownia Micro free) to ~PLN 10–23/mo (Fakturownia Start/Standard, KSeF included in every plan, no per-invoice fees) | [H06-E15, E16] |
| Micro spend, DE | €0 today (receiving = email inbox; free ZUGFeRD/XRechnung generators, no registration); suites €0–~€20/mo when issuing starts 2027–28 | [H06-E18, E19] |
| Per-invoice infrastructure (what a founder would resell) | €0.18–€0.25/invoice pay-per-use (e-invoice.be), being competed downward; Storecove ~€495+/mo for software-vendor API accounts | [H06-E21] |
| Enterprise/ERP compliance projects | Real budgets (Basware, Sovos, EDICOM, Comarch, consultants) — enterprise sales motion, out of solo-founder scope | context |
| Self-host path (the HN complaint) | OpenPeppol AP membership €1,850/yr + €1,500 certification — a service-provider cost, not an SME cost | [H06-E20] |

**Per-customer-per-year arithmetic:** the promoted buyer (freelancer/SME below suite fit) budgets **€0–€288/yr, with the anchor at €0 in all four countries** — the same shape that broke H04 (£0–288/yr, median £36), except here two governments and a nonprofit hold the floor down deliberately. Operator verbatim on WTP: "pour un CA à quelques centaines d'euros par mois c'est vite disproportionné" [H06-E5]. Budget-proof hard gate technically passes (money and salaried time do move), but the monetizable residue in the promoted segment rounds to a €5–15/mo commodity already supplied by dozens of local vendors per country.

## 3. Competitive landscape

The crux question — *in each country, does a free government portal or bundled bank/suite feature erase the SME pain before a startup can monetize it?* — answers **YES four times**:

| Country | Free/state erasure | Bundled erasure | Verdict on white space |
|---|---|---|---|
| Poland | KSeF **is** the state platform; MoF ships 3 free apps and officially states free tools suffice [H06-E15] | Every local invoicing incumbent (Fakturownia, iFirma…) includes KSeF in all plans, free tier up [H06-E16] | None — state owns the floor |
| Belgium | Let's Peppol: free, open-source, nonprofit AP "like Let's Encrypt" [H06-E9]; state retired its own Hermes fallback *because market coverage sufficed* [H06-E8] | Accountable free unlimited Peppol; €4–15/mo tools; accountant-channel bundles; 120% deduction [H06-E10–E12] | None — nonprofit + subsidy own the floor |
| France | 9 of 137–147 accredited platforms run €0 full-compliance plans [H06-E2, E4] | Neobanks Qonto & Shine are free accredited platforms (bank-bundling realized); Odoo free app is an accredited platform; Pennylane free micro tier | None — 140+ vendors racing, floor at €0 |
| Germany | Receiving obligation = an email inbox; free ZUGFeRD/XRechnung generators without registration [H06-E18, E19] | All major suites (DATEV, Lexware, sevDesk, Papierkram) ship both formats both directions before the 2027–28 issuing wave | None — no network to onboard onto |

| Solution | Type | Segment served | Price | Where it fails (evidenced) |
|---|---|---|---|---|
| **State platforms & free apps** (KSeF + Aplikacja Podatnika/e-mikrofirma; formerly Hermes BE) | Government product | PL all; micro especially | Free | UX griping and edge cases (FX, no-NIP buyers) [H06-E17]; but it is the legally-defined pipe — undisplaceable |
| **Let's Peppol (BARGE vzw)** | Nonprofit OSS product | BE/Peppol-country SMEs, freelancers, accountants | Free, "no costs and no fees" | Young; web-inbox simplicity; sets the price floor at €0 [H06-E9] |
| **Accounting/invoicing suites with native e-invoicing** (Accountable, Billit, Teamleader, Dexxter, Yuki; sevDesk/Lexware/DATEV; Fakturownia/iFirma; Odoo) | Product | Country-native SMEs/freelancers | €0 free tiers to ~€20/mo; Odoo free 1-app | Country-gapped for multi-country firms (real but small segment served by ERP/tax-tech); Lexware pushes sending to higher tiers [H06-E10, E16, E19] |
| **French accredited platforms (PAs)** incl. Indy, Tiime, Solo, Abby, Kolecto, Pennylane | Product | French TPE/PME | 9 with €0 plans; paid €9–19/mo | Choice overload (40% of firms can't name one) — but comparison sites already flood that gap for free [H06-E3, E4, E6] |
| **Neobanks as platforms** (Qonto, Shine) | Bank bundle | French freelancers/SMEs | Free e-invoicing; banking from €9/mo | Crowded-but-hated evidence exists (r/vosfinances "Qonto est la pire banque… fuyez !", 36 pts) — defectors land on other free PAs, not on a paid entrant |
| **Peppol access-point / API providers** (e-invoice.be €0.25/inv; Storecove €495+/mo; Recommand, Peppr, Unifiedpost/Banqup) | Product/infrastructure | Developers, SaaS vendors, ERPs | €0.18–0.25/invoice; subscriptions | The embeddable-compliance slice is already a competed multi-vendor market being driven to cents [H06-E21, E22] |
| **Enterprise e-invoicing/tax-tech** (Basware, Pagero/Thomson Reuters, Sovos, Avalara, EDICOM, Comarch) | Product/service | Mid-market+, multi-country, non-established registrants | Project/contract pricing | Overkill below mid-market; owns the only slice where foreign sellers are actually in scope (PL) [H06-E23] |
| **Accountant/fiduciary channel** | Service/stack | BE/FR/DE SMEs who "let the accountant pick" | Bundled into accounting fees | The trust gatekeeper: tool choice is made by the accountant, subsidized 120% in BE [H06-E12, E11] |
| **Do nothing / ride tolerance** | DIY | Laggards | Free until enforcement | BE: penalties €1,500/3,000/5,000 live since Apr 2026; PL: fines from Jan 2027; FR: explicit state tolerance to end-2026 [H06-E7, E14, E3] |

**Deep-verify of the closest 3:** (1) **Accountable** (BE) — free plan includes unlimited Peppol send/receive and free Peppol registration; paid tiers €1.50–9.90/mo; segment focus is exactly Manager 1's "freelancers below accounting-suite fit" [H06-E10]. (2) **Indy/Tiime/Qonto** (FR) — unlimited free e-invoicing both directions with zero entry conditions; operator threads confirm sub-10-minute free onboarding at scale [H06-E4, E5]. (3) **e-invoice.be vs Storecove** (the API slice a founder would occupy) — published pay-per-use at €0.25/invoice explicitly marketed as "Peppol e-invoicing, without enterprise pricing" against Storecove's €495+/mo custom quotes: the "ride an AP at margin" idea is already someone's shipped low-price product, and more than one (Recommand, Peppr, Thelawin, Eleata launched into it during 2026 with 0–2 points of HN traction) [H06-E21, E22].

**Is there a served-badly segment?** Candidates from the promotion memo, tested: (a) *non-domestic sellers into mandate countries* — out of legal scope in BE/FR/DE (no forcing function); in scope in PL only if PL-VAT-registered, an enterprise-shaped niche owned by tax-tech [H06-E23]. (b) *Freelancers below suite fit* — the free floor was built for exactly them, by governments (PL), nonprofits (BE), and venture-funded land-grabbers (FR) [H06-E4, E9, E15]. (c) *Vertical SaaS needing embedded compliance* — real and growing (ViDA 2030 guarantees it) but already a competed API market from €0.25/invoice to enterprise [H06-E21, E24]. (d) *Practice-side onboarding layer* (the H04-analog: accountants converting client books) — BE wave already executed; FR experts-comptables are courted by 147 PAs and the profession's own platform; identical head-on shape to H04. No structurally unserved segment found.

## 4. The wedge (as promoted — and why it's blocked)

Smallest product per the hypothesis: a multi-country onboarding + issuing layer for SMEs/freelancers — (1) register the business on Peppol/KSeF/a French PA, (2) generate/validate EN 16931-compliant invoices from simple inputs, (3) route via an access point, (4) handle rejections with plain-language fixes, (5) archive compliantly, (6) explicitly NOT bookkeeping or tax filing.

≤90 days for founder + agents? **Technically yes** for BE/DE/PL-adjacent function: ride e-invoice.be/Storecove-class APIs (Peppol) and KSeF's open state API; formats are public standards with OSS libraries. **France is gated:** operating as the customer's platform requires PA accreditation (audit-gated, 137–147 already registered) or riding as an unaccredited operator through someone else's PA — a dependency plus a certification wall a solo founder cannot clear by Sept 2026 [H06-E1, E2].

**But the wedge is already shipped, at zero, in every country** — by the state (PL), a nonprofit (BE), and nine accredited free plans including two neobanks (FR), with Germany not needing a network at all until 2027–28, by which time its entire suite market has pre-shipped both formats [H06-E15, E9, E4, E19]. What H04's incumbents did to one wedge in one country, four different actor classes (governments, nonprofits, suites, banks) have done to this wedge in four.

## 5. Forcing function & why now

The strongest FF in the program, grade A across the board: per-invoice statutory compulsion; Belgium executed (penalties €1,500/3,000/5,000 enforced since 1 Apr 2026); Poland executed (state clearance since Feb/Apr 2026); France days away (verified held); Germany receiving executed, issuing dated 2027/2028; ViDA locks the EU trajectory to 2030 [H06-E7, E14, E1, E18, E24].

**Material Wave-2 nuance:** every regime shipped a soft landing that diffuses the panic a paid rescue product would monetize — PL penalties deferred to 1 Jan 2027 with micro-sellers (≤PLN 10k/mo) outside KSeF until 2027 [H06-E14]; FR "no sanctions... for good-faith companies" through end-2026 [H06-E3]; DE issuing still 16 months out. The FF compels *action*, and the action available is free. A forcing function shared by the customer, the state, and forty free vendors forces purchases to no one in particular.

## 6. Distribution plan (solo-founder realistic)

Named channels exist per country: BE — r/BEFreelance, accountant/fiduciary networks, UNIZO/UCM; FR — experts-comptables, CCI webinars, r/vosfinances/r/autoentrepreneurs, URSSAF-adjacent portals; PL — accounting offices (biura rachunkowe), Facebook JDG groups, infakt/Fakturownia content ecosystems; DE — Steuerberater channel, r/selbststaendig.

Honest assessment: **worse than H04, which scored 1.** Four languages (NL/FR/DE/PL + FR), four separate trust markets, each gated by a local accountant channel that is already subsidized (BE: 120% deduction routed through advisors) or courted by 137+ registered platforms (FR), competing against the buyer's own bank, suite, tax authority, and a nonprofit — with a US founder, no EU entity, and support hours across CET. The organic channels answer newcomers with "use Indy/Tiime free" or "use the ministry app" in-thread today [H06-E5, E12, E15]. Even EU-native builders can't find the channel: "I built a Factur-X-compliant SaaS and I don't know how to sell it" [H06-E6]. First-10-customers path: does not credibly exist at a price above €0.

## 7. AI-structural advantage

Near nil. The work the mandate creates is deterministic schema mapping, validation, and transport — solved by format libraries and APs, not judgment. There is no services price list to collapse: the "labor line" (onboarding help) is a one-time task the free platforms compressed to minutes ("inscription... en trois minutes chrono"), and the residual edge cases (PL FX rules, no-NIP foreign buyers) are patch-shaped features for local incumbents, in local languages [H06-E5, E17]. LLM-shaped assists (plain-language rejection fixes, field extraction from legacy invoices) are one-model-call features every suite can add — and the deepest AI surface (reading invoice flows) belongs to whoever holds the ledger and the pipe: suites, banks, PAs, and in Poland the state itself.

## 8. Moat path

What would accumulate: onboarding playbooks per country, rejection-fix knowledge, a directory of counterparty capabilities. Honest thin-wrapper assessment: **high risk — the highest in my batch.** The rails are standardized public infrastructure (EN 16931, Peppol BIS, FA(3)); the moatable layers (network operation, accreditation, the ledger, the bank account, the accountant relationship) are all owned by others; the wedge product is a UI over someone else's API, in a market where a nonprofit gives that UI away and two governments distribute their own. Nothing proprietary accumulates from micro-invoicing volume that Fakturownia, Accountable, Qonto, or the Ministry of Finance don't already have more of.

## 9. Risks & unknowns (top 5, with tests)

1. **Head-on collision + free-floor erasure is realized, not prospective** (kill driver). Test: 20-item feature/price teardown of Accountable-free, Let's Peppol, Indy/Tiime-free, and Aplikacja Podatnika against the wedge spec — desk evidence already shows ≥80% coverage at €0; a hands-on trial would finalize.
2. **WTP ≈ €0 in the promoted segment.** Test: two-locale landing-page pre-sale at €9/mo against free incumbents; <3 conversions from 200 targeted freelancer-community visitors in 4 weeks confirms (expected).
3. **France PA dependency for any FR wedge.** Test: request unaccredited-operator partnership terms from 2 PAs; if terms require white-labeling under their brand/pricing, the FR entry is structurally a reseller role, not a company.
4. **Residual edge-case slivers might be real niches** (PL foreign-currency/no-NIP invoicing; BE cross-border customer confusion). Test: 10 interviews with PL exporters/BE freelancers with foreign clients; check whether Fakturownia/Accountable patch within one quarter (their velocity on KSeF FA(3)/Peppol suggests yes).
5. **The 2027–28 German issuing wave or ViDA-2030 could produce a genuinely failed segment later.** Test: monitor DATEV/Lexware/sevDesk free-tier issuing coverage and Steuerberater discourse through mid-2027; re-open only on documented incumbent failure in a named segment with money moving to outside help.

## 10. Scores

| # | Dimension | Weight | Score | Note |
|---|---|---|---|---|
| 1 | Pain severity & frequency | 15% | 3 | Per-invoice frequency, real go-live friction; but front-loaded, half report net time savings post-adoption, residual pain = edge cases |
| 2 | Budget proof | 15% | 3 | Money moves (suites, APs, subsidy, enterprise) — but the promoted segment's anchor is €0 in all four countries |
| 3 | Competitive gap | 12% | 1 | No unserved segment found; every candidate slice occupied by state, nonprofit, suite, bank, or API incumbents |
| 4 | Forcing function | 10% | 5 | Statutory, per-invoice, executed/held — the program's strongest FF class (soft landings noted) |
| 5 | Founder+agents feasibility | 12% | 2 | Buildable ≤90 days on APs/KSeF API; France gated by PA accreditation; four locales of support |
| 6 | Distribution reachability | 10% | 1 | Four languages/trust markets, accountant-gated, state and banks as competitors; non-EU solo founder confirmed disadvantage |
| 7 | AI-structural advantage | 8% | 1 | Deterministic schema work; no services line to collapse; AI features are incumbents' fastest fast-follow |
| 8 | Moat path | 8% | 1 | Standardized public rails; UI-over-API thin wrapper; free floor held by nonprofit + governments |
| 9 | Expansion ceiling | 5% | 3 | ViDA 2030 + more country waves = huge TAM, but the same incumbents scale with it |
| 10 | Durability | 5% | 2 | Survives model jumps; does not survive free-floor gravity; state platforms absorb scope over time |
| | **Weighted total** | | **45/100** | kill band |

**Hard gates:** Budget proof PASS (money/salaried time demonstrably moves in-category) · Reachable buyer PASS nominally (SMB, PLG motion) but distribution-scored 1 · **Thin-wrapper FAIL-adjacent** (UI over public standards and others' APIs; free OSS equivalent exists) · **Head-on collision FAIL** — same wedge (SME e-invoicing onboarding/issuing), same segment, occupied in every target country by well-funded, competent, currently-shipping incumbents *plus* free state tooling (PL), a free nonprofit AP (BE), and nine free accredited platforms including two neobanks (FR) · **Platform hostage PARTIAL-FAIL for France** (any FR wedge operates under PA accreditation or as a dependent of an accredited platform; Peppol/KSeF themselves are regulated multi-vendor/state utilities — PASS in BE/PL/DE) · Regulated practice PASS.

**Displacement sentence:** Current solution = free state apps (PL), €0–15/mo suite tiers and a nonprofit open-source access point (BE), nine free accredited platforms including the buyer's own neobank (FR), and an email inbox (DE) — costing €0–€288/yr, subsidized at 120% deductibility in Belgium. New product = another onboarding/issuing layer. The customer does not switch, because the incumbent path is already free or near-free, chosen by their accountant, bundled by their bank or suite, or operated by their tax authority — and the segment's own stated willingness to pay for this at a few hundred euros of monthly revenue is "disproportionate."

## 11. Verdict proposal

**KILL.** The mandate map verified perfectly — Belgium and Poland executed, France days away, Germany dated — which is precisely why four actor classes already built the wedge: governments ship free apps (PL), a nonprofit runs a free open-source access point (BE), nine accredited platforms including neobanks give full compliance away (FR), and suites pre-shipped both formats before Germany's issuing wave. The founding €2,000/yr complaint was the service-provider fee, not the SME's path. H04's single-country head-on failure repeats here four times with a €0 floor. **Re-open only if:** the DE 2027–28 issuing wave or ViDA-2030 cross-border wave produces documented incumbent failure in a named segment with money already moving to outside help. (Manager 2 decides.)

## 12. Evidence ledger

JSONL at `outputs/evidence/dh06_einvoicing.jsonl` (claim IDs H06-E1…H06-E25; schema per scout records). Summary:

| ID | Claim (short) | Source |
|---|---|---|
| H06-E1 | France dates held: receive-all + large/ETI issue 2026-09-01; SME issue 2027-09-01; PDP→PA | Basware compliance map (search-corroborated) |
| H06-E2 | 137–147 registered French PAs (Aug 2026); Odoo accredited 2026-04-15 | facturation-electronique-tpe.fr + fonciere-euris.fr |
| H06-E3 | FR: 38% not ready; 40% can't name a platform; state tolerance/no sanctions to end-2026 (Amiel, 2026-07-10) | Le Journal des Entreprises |
| H06-E4 | Nine French PAs with €0 full-compliance plans; Indy/Tiime/Qonto unlimited free, no conditions | ma-facture-electronique.org |
| H06-E5 | FR freelancer verbatims: free tiers adopted in minutes; WTP "disproportionné" at micro revenue | r/france via Arctic Shift |
| H06-E6 | Builder flood, no buyers: "built a Factur-X SaaS… don't know how to sell it"; PDPlibre OSS; free comparators | r/france via Arctic Shift |
| H06-E7 | BE live 2026-01-01, ~1.2M entities; tolerance ended 2026-03-31; penalties €1,500/3,000/5,000 enforced | peppolvalidator.com (search-corroborated) |
| H06-E8 | BE retired its own Hermes fallback 2025-12-31 — market coverage judged sufficient | Sovos regulatory update |
| H06-E9 | Let's Peppol: free, open-source, nonprofit AP "like Let's Encrypt," built for SMEs/freelancers/accountants | letspeppol.org |
| H06-E10 | BE tool price band €0–15/mo; Accountable free = unlimited Peppol | accountable.eu (vendor comparison, disclosed) |
| H06-E11 | BE 120% tax deduction on e-invoicing software/advice, 2024–2027 | billit.eu |
| H06-E12 | r/BEFreelance "what are you using": Odoo free, Kyte €5, Let's Peppol, Digivak free, accountant-picked +120% | Arctic Shift |
| H06-E13 | Horus/iVox (2026-04): 54% adopted in final 6 months, 20% late; 49% time savings vs 31% loss | ITdaily |
| H06-E14 | PL live Feb/Apr 2026; penalties (≤100% of VAT) deferred to 2027-01-01; micro ≤PLN 10k/mo outside until 2027 | e-invoice.app guide (search-corroborated w/ MoF Q&A coverage) |
| H06-E15 | Official MoF: "Free tools are sufficient for issuing e-invoices in KSeF" — 3 free apps | gov.pl (2023 page; 2026 apps corroborated) |
| H06-E16 | Fakturownia: KSeF in every plan, free tier up; Start ~PLN 10–12.5/mo | ksef-dla.pl |
| H06-E17 | r/Polska go-live threads (483 pts); edge-case pain verbatim (FX, no-NIP) inside existing tools | Arctic Shift |
| H06-E18 | DE: receive live since 2025 (email suffices); issue 2027 (>€800k)/2028 (all); domestic-established only | Marosa (search-corroborated) |
| H06-E19 | sevDesk free e-invoice generator, free tier; DATEV/Lexware/sevDesk/Papierkram all ship both formats | sevdesk.de (search-corroborated) |
| H06-E20 | OpenPeppol fees: AP-only €1,850/yr + €1,500 cert — the "€2,000" is the self-host path, not the SME path | peppol.org/join/fees |
| H06-E21 | AP/API market competed to €0.18–0.25/invoice (e-invoice.be) vs Storecove €495+/mo for platforms | e-invoice.be (vendor comparison, disclosed) |
| H06-E22 | HN 2026 launches against the live mandate flatlined at 1–2 points (Peppr, Thelawin, Eleata) | HN Algolia API |
| H06-E23 | Non-established foreign sellers out of scope BE/FR/DE; in scope PL only if PL-VAT-registered | OpenText blog (search-corroborated) |
| H06-E24 | ViDA adopted 2025-03-11; intra-EU e-invoicing/DRR from 2030-07-01 | Marosa (search-corroborated) |
| H06-E25 | BE normalization: mid-2026 threads are edge-case questions; homemade tools at 0 points | Arctic Shift listing |
