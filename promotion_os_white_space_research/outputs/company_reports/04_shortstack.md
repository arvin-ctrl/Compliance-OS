# Company Report — ShortStack

Researcher: Research Agent 04 (ShortStack)
Date: 2026-08-18
Category: Promotion administration
Manager: Manager A

Core question assigned: **How much rules/compliance infrastructure exists beneath campaign creation?**
Short answer: **Very little.** Beneath the campaign builder sit (a) a free, disclaimered rules-document generator, (b) IP-based country visibility toggles and a DIY age-gate pattern, (c) an admin-authored pattern fraud filter plus third-party CAPTCHA, and (d) permission-gated publishing that customers like Live Nation adapt into their own legal-review process. There is no rules engine, no policy versioning, no decision API, no legal administration service, and compliance responsibility is contractually pushed entirely onto the customer.

## 1. Executive summary

ShortStack (legal entity Pancake Laboratories, Inc., Reno, NV; founded ~2010 by Jim Belosic; bootstrapped) is a **self-serve, no-code campaign builder** for contests, sweepstakes, instant-win games, quizzes, landing pages, pop-ups, and lead forms [SHORTSTACK-001, SHORTSTACK-024]. It claims 50,000+ businesses over 15 years, with enterprise logos (Netflix, UFC, PetSmart, Live Nation), but its reviewer base is predominantly small business/mid-market marketing teams [SHORTSTACK-001, SHORTSTACK-025].

**Who buys it:** marketers (in-house SMB/mid-market marketers and agencies; occasionally enterprise marketing teams like Live Nation's) [SHORTSTACK-014, SHORTSTACK-025]. **Job it is hired to do:** launch a branded promotion or lead-capture experience quickly without developers, collect and moderate entries, pick winners, and push leads into the email/CRM stack [SHORTSTACK-001, SHORTSTACK-007].

Compliance posture: ShortStack supplies *content and guardrails* (free official-rules generator with some jurisdiction logic, rules-page hosting, age-gate template, country visibility limits, entry caps, fraud filter) while explicitly disclaiming legal advice and making the customer "solely responsible" for legal compliance [SHORTSTACK-003, SHORTSTACK-017]. Its "Compliance" page is about data-privacy law (GDPR/CCPA/DPF), not promotion law [SHORTSTACK-004].

## 2. Product architecture

Core entities: **Campaign** (a hosted or embedded page/pop-up built from widgets) → **Form** (fields, restrictions, instant-win config) → **Entries** (records in the Entries Manager) → **Lists** (marketing lists) → **Team members** (roles/permissions) → **Templates/Themes**.

INPUT → DECISION/PROCESS → OUTPUT:

- INPUT: a visitor loads a hosted/embedded campaign page; submits a form (custom fields, DOB for age gates, uploads, votes, referral links, social comments imported); IP address captured automatically [SHORTSTACK-010, SHORTSTACK-018].
- DECISION/PROCESS (all inside ShortStack's hosted campaign runtime, none exposed as a service): widget visibility rules (country by IP, date, age-gate action widgets); entry restrictions (per-email one-time/frequency/cap); CAPTCHA (reCAPTCHA/Turnstile); Fraud Filter pattern match → label or silent reject; instant-win prize allocation (prize pools/code lists, weighting, day distribution — odds not settable); points-for-actions accrual [SHORTSTACK-010, SHORTSTACK-012, SHORTSTACK-013, SHORTSTACK-023].
- OUTPUT: stored entry record (name/email, IP, location, timestamp, source, referral URL, labels); autoresponder/scheduled emails incl. unique codes; webhook POST per new entry (optionally HMAC-signed); CRM/ESP sync; CSV export and read-only Entries API; analytics; manual random winner draws with labels [SHORTSTACK-008, SHORTSTACK-009, SHORTSTACK-016, SHORTSTACK-018, SHORTSTACK-021, SHORTSTACK-022].

The decision logic is **configuration inside a page builder**, evaluated only for ShortStack-hosted interactions. There is no callable decision endpoint, no rule objects with versions/priorities, and denied entry attempts (fraud-filter rejects) leave no customer-visible record [SHORTSTACK-008, SHORTSTACK-012, SHORTSTACK-031].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Campaign builder (landing pages, pop-ups, forms) | Drag-and-drop builder; embed or hosted; custom CSS/JS (Build+) | Marketing | Core | SHORTSTACK-001, SHORTSTACK-027 |
| Contests & sweepstakes | Form/social/hashtag entries, voting, bonus entries | Marketing | Core | SHORTSTACK-001, SHORTSTACK-007 |
| Instant win | Wheels/scratch/slots; prize pools & unique code lists; weighting/day distribution | Marketing | Core (Advanced at Scale+) | SHORTSTACK-013, SHORTSTACK-032 |
| Refer-a-friend / Points for actions | Unique referral links, campaign-scoped points → bonus entries/votes | Marketing | Core (Build+/Launch+) | SHORTSTACK-023, SHORTSTACK-007 |
| Entries Manager | Entry DB: details (IP/location/time), filters, labels, approve/reject, export profiles | Marketing | Core | SHORTSTACK-018, SHORTSTACK-019 |
| Anti-fraud suite | Fraud Filter patterns, reCAPTCHA/Turnstile, country limits, entry caps | Marketing | Scale+ tier feature | SHORTSTACK-002, SHORTSTACK-007, SHORTSTACK-012 |
| Winner selection | Random entry picker with labels, weighted chances, pre-draw filtering | Marketing | Core | SHORTSTACK-016 |
| Rules Generator (free tool) | Questionnaire → official rules + short-form rules PDF; state/Canada logic; heavy disclaimers | Anyone (lead magnet) | Free standalone tool | SHORTSTACK-003 |
| Emails & code redemption | Autoresponders/scheduled emails, unique single-use codes, redemption tracking | Marketing | Scale+ for codes | SHORTSTACK-021 |
| Teams / white label | 4 roles + custom permissions, permission tags, client folders, custom domains/branding | Agencies/enterprise marketing | Max/Enterprise | SHORTSTACK-015, SHORTSTACK-006 |
| Entries API + webhooks | Read-only entry retrieval; per-entry webhook POST | Marketing ops/devs | Max tier | SHORTSTACK-008, SHORTSTACK-009 |
| Professional services | "We build it for you" campaign builds; dedicated AM | Enterprise/agencies | Add-on | SHORTSTACK-006 |

## 4. API / developer capability

- **API:** one documented public API — the **Entries API**, read-only retrieval of stored entries (`https://entries.shortstack.com/entries`), token header auth, filters (date ranges, numeric ranges, search, export-profile mapping), `per_page` max 5000, Link-header pagination, JSON responses [SHORTSTACK-008]. Gated to the Max plan ($166/mo annual) and Enterprise [SHORTSTACK-007]. No campaign-management API, no entry-creation API, no decision/eligibility API documented [SHORTSTACK-008, SHORTSTACK-031].
- **SDKs:** none documented; docs present raw curl examples (inference: no SDKs exist) [SHORTSTACK-008].
- **Webhooks:** outbound HTTP POST per new form entry; JSON or form-encoded; optional secret → `X-Ss-Signature` integrity header; Zapier/Make patterns [SHORTSTACK-009]. Single event type (new entry).
- **Sandbox:** none; free tier plus builder preview/test-before-publish serve that role [SHORTSTACK-033].
- **Rules engine:** none exposed. Restriction toggles and widget visibility conditions inside the builder only [SHORTSTACK-010].
- **Synchronous decisioning:** internal to hosted campaigns (restrictions, CAPTCHA, fraud filter, instant-win allocation at submission time); not callable by external systems [SHORTSTACK-012, SHORTSTACK-013].
- **Latency claims:** none published; enterprise page claims handling "millions of entries and traffic spikes" [SHORTSTACK-006].
- **Versioning/idempotency/rate limits/request logs:** not documented (unresolved; help center direct access was Cloudflare-blocked) [SHORTSTACK-008, SHORTSTACK-031].
- **Integration model:** embed script/hosted pages + native ESP/CRM connectors (Mailchimp, HubSpot, Klaviyo), GA4/Pixel, Zapier, CSV export, custom client-side JavaScript via Code Widget ("integrate complex APIs" — client-side only) [SHORTSTACK-001, SHORTSTACK-027].

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** Only attributes captured by its own forms/widgets (custom fields, IP-derived country, DOB field); usable in widget visibility and restrictions, filterable in API [SHORTSTACK-008, SHORTSTACK-010, SHORTSTACK-011]. Not a general attribute-evaluation engine.
- **Store customer/user state?** Campaign-scoped: per-email entry counts, points, referral credit; marketing lists persist cross-campaign. No cross-campaign decisioning state [SHORTSTACK-010, SHORTSTACK-023].
- **Reason codes?** No. Fraud filter applies labels naming matched patterns; nothing machine-readable per decision [SHORTSTACK-012].
- **Allow/deny/review output?** Internally analogous: entry accepted / silently rejected (fraud filter) / flagged-labeled + human approve-reject permission. Not exposed as an output model; rejects are invisible to the customer [SHORTSTACK-012, SHORTSTACK-015].
- **Simulate policies?** No. Campaign preview/test-before-publish only [SHORTSTACK-033].
- **Replay decisions?** No. Entry records partially reconstruct accepted entries; rejected attempts leave no record [SHORTSTACK-012, SHORTSTACK-018].
- **Version policies?** No policy objects, no version history documented [SHORTSTACK-031].
- **Deploy rules independently of app code?** Campaign config changes publish instantly without customer code changes (one-click republish), but that is page config, not rules-as-artifact [SHORTSTACK-033].

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance:** free Rules Generator (sweepstakes vs contest, eligibility age/geography, ARV, winner selection; short-form social rules; PDF) with real but shallow jurisdiction logic: US state picker, NY/FL registration-threshold warnings, Canada skill-testing question, Quebec exclusion [SHORTSTACK-003]. Help-center rules templates and platform-rules guidance (Meta etc.) [SHORTSTACK-019, SHORTSTACK-030]. Rules pages can be hosted on campaigns (Live Nation does) [SHORTSTACK-014].
- **Generic regulatory workflow:** none. No workflow product for regulatory obligations [SHORTSTACK-031].
- **Jurisdiction restrictions:** country-level widget visibility via IP; "country limits" in the anti-fraud suite. No state-level enforcement, no jurisdiction rule packs [SHORTSTACK-007, SHORTSTACK-010].
- **Location verification:** coarse IP-country only; no GPS, no VPN/proxy detection documented [SHORTSTACK-010, SHORTSTACK-031].
- **Legal content/rules:** template text generation only, "AS IS," attorney review recommended; ShortStack "is not a law firm" [SHORTSTACK-003].
- **Regulatory monitoring:** none (blog/education only) [SHORTSTACK-030, SHORTSTACK-031].
- **Change management:** one-click publish; no staged rollouts or change records documented [SHORTSTACK-033].
- **Counsel approval:** no counsel-specific feature. Publish permission + roles let a customer make legal a gatekeeper — Live Nation runs a "review approve publish" process this way [SHORTSTACK-014, SHORTSTACK-015]. No sign-off records/attestation artifacts documented.
- **Historical policy state:** none; entries are timestamped but campaign/rule config history is not exposed [SHORTSTACK-031].

## 7. Audit / evidence

Can a customer reconstruct:

- **Exact inputs?** Partially — accepted entries store submitted fields + IP + location + source + referral link [SHORTSTACK-018]. Rejected (fraud-filtered) attempts are not visible at all [SHORTSTACK-012].
- **Exact rule/policy?** No — restrictions/config are not versioned artifacts linked to entries [SHORTSTACK-031].
- **Exact version?** No policy/config version history documented [SHORTSTACK-031].
- **Exact output?** Partially — entry exists/labels/winner labels; instant-win prize assignment recorded via codes traceable to customer and campaign [SHORTSTACK-016, SHORTSTACK-021].
- **Exact timestamp?** Yes for accepted entries [SHORTSTACK-018].
- **Human approvals?** Approve/reject permissions exist; whether an approval audit trail (who/when) is recorded is undocumented (unresolved) [SHORTSTACK-015].
- **Source/legal authority?** No — generated rules carry no legal-source provenance [SHORTSTACK-003].

Other evidence properties: entries are admin-deletable (not immutable) [SHORTSTACK-018]; CSV export anytime [SHORTSTACK-019]; webhook payload signing is the only integrity feature [SHORTSTACK-009]; retention = plan storage caps + deletion within 90 days of account closure + DPA audit rights [SHORTSTACK-005, SHORTSTACK-007]. Net: marketing-grade recordkeeping, not evidence-grade auditability.

## 8. Enterprise readiness

- **SSO/RBAC:** RBAC yes — 4 roles + customizable permissions + permission tags [SHORTSTACK-015]. SSO/SAML: no evidence found despite targeted search (unresolved; likely absent — inference) [SHORTSTACK-031].
- **Multitenancy/multi-brand:** agency-grade — client folders/tags, per-client white label, unlimited campaigns, team seats by tier [SHORTSTACK-006, SHORTSTACK-015, SHORTSTACK-007].
- **Environments:** none; preview/test then publish [SHORTSTACK-033].
- **Security certifications:** own certifications limited to EU-U.S. DPF; SOC 2 II/ISO 27001/PCI are the infrastructure provider's (AWS), not ShortStack's; real but modest security program (annual pen tests, AES-256, TLS 1.2+, access reviews) [SHORTSTACK-004, SHORTSTACK-005].
- **SLA:** public status page (~99.996% observed); no published SLA; Enterprise "custom agreements" [SHORTSTACK-026, SHORTSTACK-007].
- **Support:** 5-star-rated support; dedicated AM at Enterprise [SHORTSTACK-006, SHORTSTACK-025].
- **Professional services:** optional campaign design/build services — not legal, fulfillment, or winner administration [SHORTSTACK-006].
- **Customer scale examples:** Live Nation (daily heavy multi-team use, legal-review workflow, consent forms, rules hosting) [SHORTSTACK-014]; logo wall incl. Netflix, UFC, PetSmart [SHORTSTACK-001].

## 9. Commercial model

- **Pricing (public, transparent):** Free $0 → Launch $24 → Build $49 → Scale $99 → Max $166/mo (annual billing), gated by monthly views/stored entries; published overage rates; Enterprise custom [SHORTSTACK-007]. Notable gates: custom JS at Build; anti-fraud suite + country limits + code redemption + advanced instant win at Scale; Entry API + full white label at Max.
- **Likely buyer:** marketing manager/agency; legal appears only as an internal reviewer at enterprise customers [SHORTSTACK-014, SHORTSTACK-025].
- **Implementation burden:** minimal — hosted pages or embed script; no-code [SHORTSTACK-001].
- **Sales motion:** self-serve free-trial-led with demo/AM motion for enterprise/agencies [SHORTSTACK-001, SHORTSTACK-006].
- **Large customers:** real but marketing-department-shaped (Live Nation case study is the strongest documented) [SHORTSTACK-014]. Bootstrapped company; no disclosed enterprise revenue mix [SHORTSTACK-024].

## 10. Strengths

- Breadth and speed of promotion creation: templates, instant win, refer-a-friend, voting, hashtag import — genuinely core-product depth on A-row mechanics [SHORTSTACK-001, SHORTSTACK-013, SHORTSTACK-032].
- Entry lifecycle tooling: restrictions, moderation, labels, IP/location capture, exports, read API [SHORTSTACK-008, SHORTSTACK-010, SHORTSTACK-018].
- Practical compliance guardrails for SMBs at zero cost: rules generator with real jurisdiction touches (Quebec, skill-testing, NY/FL registration warnings), age-gate template, country limits [SHORTSTACK-003, SHORTSTACK-011].
- Agency/multi-brand operating model (white label, client folders, permission tags) [SHORTSTACK-006, SHORTSTACK-015].
- Transparent pricing and low-friction self-serve motion; strong support reputation [SHORTSTACK-007, SHORTSTACK-025].
- Durable, bootstrapped 15-year business with enterprise-tolerable reliability (status page ~99.996%) [SHORTSTACK-024, SHORTSTACK-026].

## 11. Weaknesses / constraints

- **No compliance infrastructure beneath the builder** (evidence-backed): rules are disclaimered documents, not executable policy; no policy versioning, no legal review service, no counsel sign-off records, no registration/bonding support, no AMOE/tax/fulfillment workflows [SHORTSTACK-003, SHORTSTACK-017, SHORTSTACK-031].
- **Audit gaps:** rejected entries invisible; entries deletable; no config history; approval trail undocumented [SHORTSTACK-012, SHORTSTACK-015, SHORTSTACK-018].
- **Thin developer platform:** one read-only API at top tier; single webhook event; no SDKs; no sandbox/versioning/idempotency documentation [SHORTSTACK-007, SHORTSTACK-008, SHORTSTACK-009].
- **Enterprise procurement gaps:** no own SOC 2; no SSO evidence; no published SLA [SHORTSTACK-005, SHORTSTACK-026, SHORTSTACK-031].
- **Coarse risk signals:** IP-country only; self-attested age; manual fraud patterns; third-party CAPTCHA [SHORTSTACK-010, SHORTSTACK-011, SHORTSTACK-012].
- Perception: SMB-centric feature depth; data-egress friction reported by reviewers ("difficult to divorce from their system and get data") [SHORTSTACK-025].
- Inference: as a bootstrapped marketing-tools company, it lacks the legal/services DNA and enterprise compliance posture needed to move down-stack into regulated decisioning.

## 12. Capability matrix scores

Scoring notes: scores follow `research/CAPABILITY_MATRIX.md` (0–4, ?). All 0 scores are **reasoned inferences** justified below the block (mostly grounded in SHORTSTACK-031's documented-absence methodology and the architecture: hosted no-code campaigns, read-only API, no policy layer) — none are "website didn't mention it" zeros. `?` = genuinely unresolved.

```csv
square,score,claim_ids
A01,4,SHORTSTACK-001;SHORTSTACK-007;SHORTSTACK-014
A02,4,SHORTSTACK-001;SHORTSTACK-007;SHORTSTACK-016
A03,3,SHORTSTACK-013;SHORTSTACK-032;SHORTSTACK-007
A04,2,SHORTSTACK-003;SHORTSTACK-030
A05,1,SHORTSTACK-003;SHORTSTACK-017;SHORTSTACK-014
A06,1,SHORTSTACK-031
A07,4,SHORTSTACK-018;SHORTSTACK-010;SHORTSTACK-008;SHORTSTACK-019
A08,3,SHORTSTACK-016;SHORTSTACK-013;SHORTSTACK-032
A09,1,SHORTSTACK-021;SHORTSTACK-032;SHORTSTACK-031
A10,0,SHORTSTACK-031
B01,1,SHORTSTACK-008;SHORTSTACK-009
B02,1,SHORTSTACK-010;SHORTSTACK-012;SHORTSTACK-013
B03,0,SHORTSTACK-008;SHORTSTACK-031
B04,1,SHORTSTACK-012;SHORTSTACK-015
B05,1,SHORTSTACK-012
B06,2,SHORTSTACK-008;SHORTSTACK-018;SHORTSTACK-027
B07,1,SHORTSTACK-010;SHORTSTACK-023
B08,0,SHORTSTACK-010;SHORTSTACK-012
B09,1,SHORTSTACK-033
B10,0,SHORTSTACK-012;SHORTSTACK-031
C01,2,SHORTSTACK-003;SHORTSTACK-010
C02,1,SHORTSTACK-003;SHORTSTACK-017
C03,0,SHORTSTACK-003;SHORTSTACK-031
C04,1,SHORTSTACK-003;SHORTSTACK-013;SHORTSTACK-033
C05,?,
C06,0,SHORTSTACK-030;SHORTSTACK-031
C07,0,SHORTSTACK-031
C08,1,SHORTSTACK-014;SHORTSTACK-015
C09,0,SHORTSTACK-003
C10,0,SHORTSTACK-003;SHORTSTACK-031
D01,1,SHORTSTACK-008;SHORTSTACK-018
D02,1,SHORTSTACK-018;SHORTSTACK-012
D03,0,SHORTSTACK-031
D04,2,SHORTSTACK-018;SHORTSTACK-009
D05,?,
D06,1,SHORTSTACK-018;SHORTSTACK-008
D07,1,SHORTSTACK-019;SHORTSTACK-008
D08,1,SHORTSTACK-005;SHORTSTACK-007
D09,1,SHORTSTACK-009
D10,1,SHORTSTACK-005
E01,0,SHORTSTACK-031
E02,1,SHORTSTACK-011
E03,0,SHORTSTACK-031
E04,2,SHORTSTACK-010;SHORTSTACK-018
E05,1,SHORTSTACK-022
E06,?,
E07,1,SHORTSTACK-002;SHORTSTACK-012
E08,2,SHORTSTACK-010;SHORTSTACK-012;SHORTSTACK-019
E09,1,SHORTSTACK-015;SHORTSTACK-018
E10,1,SHORTSTACK-002;SHORTSTACK-009
F01,1,SHORTSTACK-023
F02,1,SHORTSTACK-023
F03,2,SHORTSTACK-021
F04,2,SHORTSTACK-021;SHORTSTACK-032
F05,?,
F06,0,SHORTSTACK-023;SHORTSTACK-031
F07,2,SHORTSTACK-021
F08,0,SHORTSTACK-023;SHORTSTACK-031
F09,0,SHORTSTACK-023;SHORTSTACK-031
F10,1,SHORTSTACK-009
G01,3,SHORTSTACK-006;SHORTSTACK-015
G02,3,SHORTSTACK-015;SHORTSTACK-007
G03,?,
G04,2,SHORTSTACK-015;SHORTSTACK-014
G05,1,SHORTSTACK-033
G06,1,SHORTSTACK-033
G07,1,SHORTSTACK-015;SHORTSTACK-033
G08,2,SHORTSTACK-009
G09,1,SHORTSTACK-007;SHORTSTACK-026
G10,2,SHORTSTACK-005;SHORTSTACK-004
H01,2,SHORTSTACK-008
H02,0,SHORTSTACK-008
H03,2,SHORTSTACK-009
H04,1,SHORTSTACK-007;SHORTSTACK-033
H05,?,
H06,?,
H07,?,
H08,?,
H09,1,SHORTSTACK-019;SHORTSTACK-015
H10,0,SHORTSTACK-008;SHORTSTACK-031
I01,1,SHORTSTACK-014;SHORTSTACK-017
I02,1,SHORTSTACK-027;SHORTSTACK-008
I03,4,SHORTSTACK-001;SHORTSTACK-022;SHORTSTACK-025
I04,1,SHORTSTACK-002
I05,2,SHORTSTACK-001;SHORTSTACK-014;SHORTSTACK-025
I06,4,SHORTSTACK-007;SHORTSTACK-001
I07,1,SHORTSTACK-006
I08,1,SHORTSTACK-025;SHORTSTACK-019
I09,1,SHORTSTACK-001;SHORTSTACK-027
I10,3,SHORTSTACK-007
J01,1,SHORTSTACK-003
J02,1,SHORTSTACK-015;SHORTSTACK-014
J03,1,SHORTSTACK-014;SHORTSTACK-015
J04,0,SHORTSTACK-031
J05,0,SHORTSTACK-008;SHORTSTACK-031
J06,0,SHORTSTACK-002;SHORTSTACK-031
J07,1,SHORTSTACK-018;SHORTSTACK-012
J08,0,SHORTSTACK-012;SHORTSTACK-031
J09,1,SHORTSTACK-003;SHORTSTACK-011
J10,0,SHORTSTACK-031
```

**Reasoning for 0 scores (all labeled inference, per brief):**
- A10, C06, C07, J04, J10: no policy/regulatory workflow layer exists anywhere in docs, pricing, or services; SHORTSTACK-031 documents the targeted-search methodology. Educational blog/help content (SHORTSTACK-030) is not product capability.
- B03, B10, J05, J08, H10: architecture precludes them — the entire integration surface is read-only Entries API + outbound entry webhooks + embeds (SHORTSTACK-008/009); there is no decision endpoint to be low-latency, replayed, or called cross-product, and no management API for IaC.
- B08: restrictions are independent toggles in a page builder; no rule objects exist to prioritize or conflict-resolve (SHORTSTACK-010/012).
- C03, C09, C10, D03: the only "legal rules" artifact is generated prose provided "AS IS" with no citations, no machine-readable form, no versions (SHORTSTACK-003).
- E01, E03: only self-submitted form data is collected; no verification vendor integrations exist in the documented integration set (SHORTSTACK-031).
- F06, F08, F09: no value ledger of any kind — points are per-campaign contest tallies (SHORTSTACK-023).
- H02: the API doc is the complete developer surface and presents raw curl only; no SDK exists to find (SHORTSTACK-008).

**Direction-of-scale notes (I-row):** I07 = 1 means *low* professional-services dependency (self-serve; services optional). I08 = 1 means *low* switching cost (ephemeral campaigns, CSV export; mild egress friction per reviews). I09 = 1 means *low* integration burden (no-code embed). Managers should read these as descriptors, not merits.

**Material `?` squares:** G03 (SSO — none found; likely absent, would matter for enterprise fit), D05 (approval history recording — matters for the counsel-workflow comparison), H05–H08 (API versioning/idempotency/rate limits/logs — undocumented; help center Cloudflare-blocked direct reads), C05 (campaign config history), E06 (VPN detection), F05 (code expiration).

## 13. White-space implications

1. **Already solved (by ShortStack, for its segment):** promotion front-end creation and administration mechanics — sweepstakes/contest/instant-win creation, entry management, entry restrictions, winner picking, basic fraud filtering, template-level official rules, marketing-grade multi-brand governance (A01–A03, A07, A08 at 3–4).
2. **Partially solved:** rules generation with shallow jurisdiction logic (A04=2); customer-run legal review via publish permissions (C08/J02/J03=1); coarse geo-eligibility (E04=2, country-only); duplicate-entry control (E08=2); code provenance/redemption (F03/F04/F07=2); privacy-law compliance tooling (consent, DPA) — a different axis than promotion law.
3. **Unsolved (by ShortStack):** everything beneath the surface — executable jurisdiction policy, policy versioning/effective dates, counsel sign-off records, impact analysis, real-time authorization APIs, reason codes, decision replay, evidence-grade audit (rejects are invisible; entries deletable), identity/age verification, VPN detection, signal orchestration, AMOE administration, registration/bonding, tax/affidavit workflows, certified drawings (J01–J10 ≈ 0–1; A05/A06/A09/A10 ≈ 0–1).
4. **Could ShortStack add the missing capability easily?** Incremental additions (state-level geo, an approvals log, SOC 2, an entry-write API) — plausible. The core hypothesis stack (policy-as-code, counsel workflow, decision APIs with evidence) — no: it would be a second product on a different architecture for a different buyer, from a bootstrapped SMB-marketing company with no legal/services arm (inference from SHORTSTACK-006/024/031).
5. **Could a customer assemble it using ShortStack + internal engineering?** Only superficially. Custom JS (Code Widget) can call external APIs client-side (e.g., a geo/verification service), and webhooks can feed external systems post-entry — but enforcement stays client-side and post-hoc; no server-side policy evaluation, no versioned decision records, denied attempts unlogged. A sophisticated enterprise could use ShortStack as the *presentation layer* while building all authorization/evidence elsewhere — which is precisely the current-stack pattern the hypothesis targets [SHORTSTACK-008, SHORTSTACK-009, SHORTSTACK-012, SHORTSTACK-027].
6. **What would make a customer buy a separate product instead?** When stakes exceed marketing-grade tolerance: regulated verticals (alcohol, cannabis, gaming/sweepstakes-casino, finance), high-value prize pools triggering registration/bonding and audits, multi-jurisdiction programs needing provable eligibility enforcement and "why was this allowed" evidence, or legal teams demanding sign-off records and immutable trails. ShortStack's own terms (customer "solely responsible"; liability cap 3x monthly fee) leave all of that risk with the sponsor [SHORTSTACK-017]. Counter-consideration: for most SMB/mid-market promotions, ShortStack + its free rules generator + one attorney review is demonstrably "good enough," including for Live Nation's marketing workflow — which argues *against* broad willingness to pay for a separate compliance layer at those tiers [SHORTSTACK-003, SHORTSTACK-014].

## 14. Replacement risk

**LOW.**

ShortStack would have to build a policy engine, decision APIs, evidence infrastructure, verification-vendor orchestration, and a counsel-facing workflow — none of which exist even embryonically (its one API is read-only entry export; its compliance page is about data privacy). Its buyer (marketer), motion (self-serve $24–$166/mo), company profile (bootstrapped, Reno-based marketing-tools DNA), and explicit "not a law firm" positioning all point away from regulated-decisioning infrastructure. The realistic competitive scenario is not ShortStack moving down-stack but ShortStack remaining the low-cost front-end that (a) anchors prices for promotion tooling and (b) demonstrates that template-level compliance satisfies most of the market — a demand-side headwind for the hypothesis, not a vendor threat [SHORTSTACK-003, SHORTSTACK-007, SHORTSTACK-008, SHORTSTACK-024, SHORTSTACK-031].

## 15. Adjacent discoveries

Companies/substitutes surfaced during research that the project should consider (beyond the assigned 15):

1. **Gleam** (gleam.io) — high-volume DIY giveaway/rewards widget platform; a top ShortStack alternative on G2; same "compliance-lite" pattern at even larger self-serve scale [SHORTSTACK-028].
2. **Easypromos** — Barcelona-based promotions platform with broader built-in legal-terms tooling and EU market depth; frequently cross-shopped with ShortStack [SHORTSTACK-028].
3. **Woobox** — long-running contest/coupon platform, near-substitute for ShortStack's core [SHORTSTACK-028].
4. **PromoVeritas** (promoveritas.com) — global promotion-compliance *services* agency (90+ countries, legal drafting, registration, W-9 winner management, independent draws). Matters because it is the human-services incumbent for exactly the compliance layer software would need to displace; a Promotion OS competes with this services model more than with ShortStack [SHORTSTACK-029].
5. **Promosis** — US sweepstakes administration services firm (same substitute class as PromoVeritas/RTM) [SHORTSTACK-029 notes].
6. **KickoffLabs / SweepWidget / Vyper / Wishpond / Woorise / Rafflecopter** — the long tail of near-substitutable DIY contest builders, confirming the front-end category is crowded and price-anchored near zero [SHORTSTACK-028].

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/04_shortstack.jsonl` (33 records). Same records rendered:

| Claim ID | Claim (abbrev.) | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| SHORTSTACK-001 | No-code contest/landing-page platform; 50k+ businesses; Netflix/UFC/PetSmart/Live Nation logos | https://www.shortstack.com/ | official-marketing | 2026-08-18 | HIGH |
| SHORTSTACK-002 | Fraud Filter labels/silently rejects; reCAPTCHA; Cloudflare Turnstile | https://www.shortstack.com/features/ | official-marketing | 2026-08-18 | HIGH |
| SHORTSTACK-003 | Free standalone rules generator; state/Canada/Quebec logic; NY/FL registration warnings; "not a law firm", "AS IS", attorney review recommended | https://www.shortstack.com/rules-generator/ | official-doc | 2026-08-18 | HIGH |
| SHORTSTACK-004 | Compliance page = data privacy only (GDPR/CCPA/PIPEDA, EU-US DPF, DPA, subprocessors) | https://www.shortstack.com/compliance/ | official-doc | 2026-08-18 | HIGH |
| SHORTSTACK-005 | AWS US hosting; SOC 2/ISO/PCI are infra provider's; TLS1.2+/AES-256; annual pen tests; 90-day deletion; DPA audit rights | https://www.shortstack.com/security-faqs/ | official-doc | 2026-08-18 | HIGH |
| SHORTSTACK-006 | Enterprise/agency: white label, multi-team, client folders, dedicated AM, custom builds, "millions of entries" | https://www.shortstack.com/enterprise/ | official-marketing | 2026-08-18 | MEDIUM |
| SHORTSTACK-007 | Pricing $0–$166/mo; Entry API at Max; anti-fraud suite + country limits at Scale; overages published; Enterprise custom | https://www.shortstack.com/pricing/ | official-marketing | 2026-08-18 | HIGH |
| SHORTSTACK-008 | Entries API read-only: token auth, filters, per_page≤5000, Link pagination; no create/manage/decision endpoints, no SDKs | https://help.shortstackapp.com/hc/en-us/articles/29277366901901-Entries-API | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-009 | Per-entry outbound webhooks; JSON/form; secret-keyed X-Ss-Signature; Zapier/Make | https://help.shortstackapp.com/hc/en-us/articles/234467468-Securing-Webhook-Form-Integrations | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-010 | IP-based country visibility; per-email entry limits (one-time/frequency/cap); reCAPTCHA settings | https://help.shortstackapp.com/hc/en-us/articles/26209704066573-Entry-Restrictions | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-011 | DIY age gate: DOB field + action widget; self-attested; age-gate template | https://help.shortstackapp.com/hc/en-us/articles/15452183945101-How-to-Add-an-Age-Gate | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-012 | Fraud Filter: manual wildcard patterns on fields incl. IP; label or silent reject; rejects invisible to admin | https://help.shortstackapp.com/hc/en-us/articles/29441917161101-Prohibit-Fraudulent-and-Spam-Entries-with-Fraud-Filter-Feature | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-013 | Instant win: prize pools/code lists (Scale+); odds not settable; weighting/day distribution | https://help.shortstackapp.com/hc/en-us/articles/360020039671-Instant-Win | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-014 | Live Nation: sweepstakes/instant win/consent forms/rules hosting; "review approve publish" legal oversight; daily heavy use | https://www.shortstack.com/blog/live-nation-entertainment-leverages-shortstacks-hassle-free-customization-and-compliance-features-for-contest-success | case-study | 2026-08-18 | HIGH |
| SHORTSTACK-015 | Teams: 4 roles + custom permissions incl. Approve Entries and Publish; permission tags; owner-centric | https://help.shortstackapp.com/hc/en-us/articles/234472288-ShortStack-for-Teams | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-016 | Random winner picker: count, labels, weighted extra chances, pre-draw filtering; no certification artifact | https://help.shortstackapp.com/hc/en-us/articles/234451408-How-to-Select-Winners | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-017 | Terms: user "solely responsible" for legal compliance; liability cap 3x monthly fee; gambling/age-sensitive content restrictions; indemnification | https://www.shortstack.com/terms-and-conditions | official-doc | 2026-08-18 | HIGH |
| SHORTSTACK-018 | Entry Details: name/email, IP, location, timestamp, source, referral; filterable; labels; deletable | https://help.shortstackapp.com/hc/en-us/articles/234467548-Entry-Details | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-019 | FAQ: CSV export anytime; Meta-guideline tooling but user responsibility; entry restrictions | https://www.shortstack.com/faqs/ | official-doc | 2026-08-18 | HIGH |
| SHORTSTACK-020 | GDPR tooling: opt-in checkboxes, double opt-in links, account-level require-double-opt-in | https://help.shortstackapp.com/hc/en-us/articles/360004168631-ShortStack-and-the-General-Data-Protection-Regulation-GDPR | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-021 | Unique single-use code lists; distribution via email/instant win; redemption traceable to customer+campaign | https://help.shortstackapp.com/hc/en-us/articles/360050803492-Setting-Up-Code-Redemption | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-022 | Analytics: funnel, UTM sources, shares, device breakdown, engagement, real-time | https://www.shortstack.com/analytics/ | official-marketing | 2026-08-18 | HIGH |
| SHORTSTACK-023 | Points for actions + refer-a-friend: campaign-scoped points → extra entries/votes; unique referral links | https://help.shortstackapp.com/hc/en-us/articles/4412742731149-Points-for-Actions | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-024 | Pancake Laboratories, Reno NV; founded ~2010 by Jim Belosic (w/ Doug Churchill); bootstrapped | https://killerstartups.com/startup-reviews/jim-belosic-co-founder-pancake-laboratories | third-party | 2026-08-18 | MEDIUM |
| SHORTSTACK-025 | G2 4.5/5 (83 reviews); mostly SMB (~52–81%), ~13% mid-market; praise support/ease; cons depth + data egress | https://www.g2.com/products/shortstack/reviews | third-party | 2026-08-18 | MEDIUM |
| SHORTSTACK-026 | Public status page ~99.996% observed uptime; no published SLA | https://status.shortstack.com/ | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-027 | Code Widget: raw HTML/JS, snippet library; custom JS from Build plan; client-side API integration point | https://help.shortstackapp.com/hc/en-us/articles/360047082571-Code-Widget | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-028 | Alternatives: Wishpond, Gleam, ViralSweep top; plus Easypromos, Woobox, SweepWidget, KickoffLabs, Vyper, Woorise | https://www.g2.com/products/shortstack/competitors/alternatives | third-party | 2026-08-18 | HIGH |
| SHORTSTACK-029 | PromoVeritas: global promotion-compliance services agency, 90+ countries, W-9 winner management, independent draws | https://www.promoveritas.com/ | third-party | 2026-08-18 | HIGH |
| SHORTSTACK-030 | Help-center rules guide/templates; ARV, chance-vs-skill; advises attorney review | https://help.shortstackapp.com/hc/en-us/articles/231757027-Social-Media-Sweepstakes-Rules-Includes-Template | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-031 | Documented-absence finding (inference): no AMOE, tax/affidavit, fulfillment, certified drawing, SSO, policy versioning, decision/management API, simulation/replay, or regulatory monitoring | https://help.shortstackapp.com/hc/en-us | official-doc | 2026-08-18 | MEDIUM |
| SHORTSTACK-032 | Instant win marketing: wheels/scratch/slots; auto winner notifications, prize claim management; no compliance mentions | https://www.shortstack.com/instant-win/ | official-marketing | 2026-08-18 | HIGH |
| SHORTSTACK-033 | One-click publish/republish; preview/test or share with team/clients pre-publish; no environments | https://help.shortstackapp.com/hc/en-us/articles/231746187-Publishing-A-Campaign | official-doc | 2026-08-18 | MEDIUM |

Note on access method: help.shortstackapp.com blocks automated fetches (Cloudflare); help-center claims were corroborated across multiple independent search snippets per the brief's fallback, and confidence was capped at MEDIUM for those records.

## 17. Verdict

**SUBSTITUTE**

ShortStack is the archetypal DIY front-end for the exact promotions the hypothesis targets: it scores 3–4 on creation and entry administration, and its free rules generator + templates + permission-gated publishing let even an enterprise like Live Nation run promotion compliance as an internal marketing-plus-legal process for $166/month or less. That bundle — tool + free rules template + one attorney review — is the incumbent alternative a Promotion OS must displace at the SMB/mid-market tier, and it price-anchors the category near zero. Beneath the builder, however, there is essentially no compliance infrastructure: no executable or versioned policy, no decision APIs, no evidence-grade audit (denied entries are invisible), no verification, no legal services, and liability contractually stays with the sponsor. It neither overlaps nor threatens the J-row control-plane concept; replacement risk LOW. It substitutes for the problem being felt, not for the proposed product's capabilities.
