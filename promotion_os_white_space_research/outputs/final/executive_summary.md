# Executive Summary — Final Verdict

Author: Final Decision Manager · Date: 2026-08-18 · Full analysis: `outputs/final/final_decision.md`

## Verdict: PIVOT

The original idea — promotion administration software for enterprise brands — is dead. Services firms already absorb the pain and the legal liability itself at $3–15K per campaign, most brands run a handful of promotions a year, and a $166/month tool plus one attorney was good enough for Live Nation. Do not build it in any form.

Nothing else clears the GO bar either. After the red team's pass, the best candidates score 66–75 against a required 80, and the red team granted zero unconditional survivals. The counsel-approval workflow died because no regulator has ever fined anyone for lacking it. The promo-authorization beachhead died because the sweeps segment it targeted was banned out of existence in 2025, not regulated into buying software. The evidence archive is real but unpriced — nothing mandates it, and an internal team gets 80% of it in a quarter.

One thing survived, in a narrower shape than anything we drew, and it earns exactly one quarter of your time — not a build.

## The surviving opportunity (≈70/100 — investigate, not build)

**Counsel-adopted executable jurisdiction packs + a real-time promotional-conduct decision API + per-decision evidence, fused as one product, in one vertical: licensed real-money gaming bonusing/responsible-gaming conduct, then regulated fintech incentives.** One API call answers "may I give this bonus, to this person, in this state, right now?" with allow/deny/review, a citation, the rule version, and a sealed evidence record. Sweeps operators are not the beachhead — that market is being banned, not saved.

This exact shape — maintained executable regulatory content behind a decision API — is not a hypothesis. It has been built, bought by the most conservative compliance buyers alive, and acquired by the infrastructure incumbent three separate times: Droit (capital markets, acquired by FIS in March 2026), Apiax (cross-border conduct including marketing, 190+ countries), and Avalara/Sovos/Vertex (tax, 54B+ API calls a year). Promotions/gaming conduct is the vertical with the same ingredients — churning multi-state law, priced enforcement, duplicated counsel spend — and no occupant.

**Buyer.** VP/Director of Compliance plus General Counsel at licensed mid-market gaming operators (UK/EU/US-state — the tier below FanDuel/DraftKings, who build in-house); CCO at fintechs with regulated incentive programs.

**Current stack.** Vixio/law-firm alerts read by humans → outside counsel memos at five-to-six figures per jurisdiction-domain-year → engineers hand-encoding rules into Talon.One/Voucherify/internal engines → GeoComply/Socure supplying person/location facts → sign-off living in email and Jira → per-vendor ops logs that can't answer an auditor.

**Pain.** Regulators price exactly this failure: £1.17M (Sky Betting — promo emailed to 41,395 self-excluded customers), £490K (Paddy Power), $260K (BetMGM-PA), over $1.3M in Ohio's first year, $250M CFPB/OCC against Bank of America on promo bonuses. Meanwhile every operator re-derives the same state rules with its own counsel, and "why was this allowed on March 12" is unanswerable across all 36 vendors we studied.

**Why incumbents fail.** Verified refusal, not oversight: Socure states its regulatory neutrality twice in its own docs; GeoComply monetizes jurisdiction content by keeping it a black box; Vixio ships prose with no API of any kind; marketing-compliance vendors (PerformLine at 6 of the top 10 US banks) stop at ad copy — promotions conduct is verifiably absent from their rulebooks; the policy engines ship zero content by design. Nobody owns statute→rule→decision.

**Why they'd switch.** The pack subscription costs less than the counsel re-derivation it replaces; the API prevents the failures regulators actually fine; the evidence trail answers the interrogation no current assembly can. It's an add-on above their engines and signal vendors, not a rip-and-replace.

**Moat.** The content-and-counsel network only: exclusive digitization rights from promotion/gaming-law boutiques, named firms standing behind the rules, the provenance graph, and cross-customer adoption records. The mechanics are explicitly not a moat — Socure ships platform releases quarterly and AWS is commoditizing policy tooling; anything mechanics-shaped gets copied inside 18 months.

**Biggest risk.** Promotions has no mandatory computation point. Tax must be computed to issue an invoice; a trade can't execute without its Dodd-Frank check; nothing forces a promo-conduct check. Demand stays discretionary, the realistic market is low hundreds of accounts at six-figure ACVs, and the evidenced endgame is acquisition by GeoComply/Socure/FIS-class — a good outcome, not a platform outcome. Decide knowing that.

## Next step: a 90-day, two-test discovery — no build, no hires

1. **Prove someone pays.** Take a mock jurisdiction pack + API spec to ≥20 target accounts. Pass = **≥5 signed paid design-partner commitments at ≥$50K/yr** for executable, counsel-adopted packs — not prose. Kill if: fewer than 5; buyers map you onto PerformLine/Red Oak/Vixio/counsel budgets; or pricing lands at counsel-memo levels (<$25K).
2. **Lock the content.** Sign **exclusive-in-field digitization rights with 2–3 promotion/gaming-law boutiques** before Vixio, Haast, or PerformLine move. Kill if no boutique signs on viable economics, or an incumbent locks equivalent content first.

Cost: founder time, travel, legal paperwork — five figures. Standing kill: if buyers only pay when your lawyers replace theirs, the legal boundary fails — kill. **Either test failing converts this verdict to KILL, full stop.** Both passing earns a BUILD-MVP re-decision (~76–78, still short of GO) with paying partners and locked content in hand.

## If this becomes KILL, what would reopen it

(1) A mandate: any regulator or platform makes a promo-conduct check or promo-rule change-control certification mandatory — the Dodd-Frank moment, and the only path above 80. (2) An enforcement action citing missing sign-off, rule versioning, or decision-evidence as a violation — as of today, none exists. (3) A named recurring evidentiary event (RG audits, bonus disputes) with real economics, validated with ≥3 buyers. (4) An incumbent ships executable promotional-conduct content and the market pays — proof of budget, though the window narrows. Watch quarterly, at zero cost: Vixio, Haast, PerformLine, Sedric, Socure releases, GeoComply announcements, FIS/Droit's prediction-markets rollout.

**Bottom line:** don't build; don't walk away yet. Spend one quarter and five figures forcing the market to answer the one question three years of desk research cannot: will anyone pay real money for executable, counsel-adopted promotional-conduct law? Five signatures and two law-firm exclusives, or kill it with a clear conscience.
