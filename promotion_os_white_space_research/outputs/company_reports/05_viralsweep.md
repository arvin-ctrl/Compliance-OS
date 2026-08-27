# Company Report — ViralSweep

Researcher: Research Agent 05 (ViralSweep)
Date: 2026-08-18
Category: Promotion administration
Manager: Manager A

## 1. Executive summary

ViralSweep is a self-serve promotions SaaS: brands build hosted/embedded sweepstakes, giveaways, UGC contests, instant-win games, hashtag/comment giveaways, waitlists, referral milestones, and purchase-to-enter campaigns, primarily to grow email/SMS lists and drive e-commerce sales [VIRALSWEEP-001, -002]. Founded 2012 (bootstrapped, small team), it was acquired by AppHub in November 2021 and now sits inside the Clearer.io e-commerce app family alongside REVIEWS.io, Rich Returns, and Address Validator [VIRALSWEEP-027, -028].

The buyer is a marketer (brand or agency); the sales motion is self-serve ($49–$999/mo, 7-day trial, Shopify App Store 4.4/141 reviews) with a contact-sales Enterprise tier [VIRALSWEEP-003, -029]. The job it is hired to do is "run a legally-passable promotion quickly and turn it into leads/sales" — campaign execution, not compliance infrastructure.

Compliance capability exists in two disconnected forms: (a) thin product features (template rules generator with an explicit no-responsibility disclaimer, IP-based geo targeting, self-attested age gates, spam filtering) [VIRALSWEEP-008, -013, -022], and (b) a human managed service at Elite/Enterprise tiers (rules drafting, state registration/bonding, winner affidavits, 1099s, prize fulfillment, PO-box AMOE) [VIRALSWEEP-015, -016]. Its terms simultaneously disclaim legal advice and place all legal responsibility on the customer [VIRALSWEEP-017]. The API is a 7-endpoint data layer (read promotions/entries/winners; write entries/points/validation), not a decisioning or policy platform [VIRALSWEEP-005].

## 2. Product architecture

Core entities (as exposed by the product and API): **Account → Brands (1–6 per plan) → Promotions (campaigns, typed: sweepstakes/contest/instant win/etc.) → Entries (entrant records: email, name, address, birthday, IP, location, referral source, custom fields, points, valid/invalid + accepted state) → Winners (drawn from entries, linked to prizes)** [VIRALSWEEP-005, -021].

Concrete workflow:

- INPUT: A marketer configures a campaign in the web builder — form fields (incl. birthday-with-minimum-age, consent checkboxes, captcha, file upload for receipts), prizes, dates/timezone, entry limits/frequency, bonus-entry actions, geo-targeting allowlist, official-rules text (pasted or generated from the template). Entrants submit via the hosted page/embed; entries also arrive via Shopify/BigCommerce orders (minutes-delayed batch), JS-tracked custom actions, imports, or POST /api/entries [VIRALSWEEP-005, -022, -024, -025].
- DECISION/PROCESS: At entry time the platform applies mechanical gates — IP-based geo block ("Sorry, this promotion is not available in your location"), per-IP spam threshold (default 1 entry/IP), internal IP/email blacklists, captcha, optional email verification code, minimum-age check on the birthday field. Flagged entries land in an Invalid tab for manual re-validation. There is no configurable rules engine, no reason-code taxonomy, no allow/deny/review API [VIRALSWEEP-008, -009, -022, -023].
- OUTPUT: Lead data synced to 60+ ESP/CRM/SMS tools, entry webhook (single event, single delivery attempt) and Zapier trigger, CSV exports, dashboards; winners drawn by weighted random draw (with fraud caution labels and manual redraw), winner CSV; winners are NOT auto-notified — the sponsor (or ViralSweep's managed service) contacts them [VIRALSWEEP-007, -011, -035].

The managed service (Elite/Enterprise) wraps this same product with humans: rules drafting, registration/bonding filings, drawing administration, eligibility verification, affidavits/1099s, prize fulfillment, PO-box mail-in AMOE [VIRALSWEEP-015].

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| Sweepstakes/Giveaway apps | Hosted/embedded entry pages, bonus entries for social actions, refer-a-friend | Marketing | Core | VIRALSWEEP-001, -002 |
| Contest app | Photo/video UGC collection, voting/judging, galleries | Marketing | Core | VIRALSWEEP-001, -002 |
| Instant Win app | Random odds, seeded win times, winning codes; coupon prizes; re-entry timer | Marketing | Core | VIRALSWEEP-010 |
| Purchases app | Auto entries per $ spent on Shopify/BigCommerce orders (plan-capped order volumes) | E-commerce marketing | Core (plan-gated) | VIRALSWEEP-025 |
| Hashtags/Comments apps | Entries from Instagram/Twitter hashtags, FB/IG/YouTube comments | Marketing | Core | VIRALSWEEP-002 |
| Waitlist/Milestones apps | Referral-ranked waitlists, tiered referral rewards | Marketing/growth | Core | VIRALSWEEP-002 |
| Rules Generator | Free template-based official-rules text (US/CA focus), explicit no-liability disclaimer | Marketing | Free tool + in-builder | VIRALSWEEP-013, -014 |
| Geo Targeting | Country/state/province IP allowlisting; manual IP allowlist for misidentified users | Marketing | Feature (Business+) | VIRALSWEEP-008 |
| API | 7 data endpoints (brands/promotions/entries/points/validate/winners), x-api-key | Marketing ops/eng | Add-on (Premium+, enable via support) | VIRALSWEEP-004, -005 |
| Webhooks/Zapier | Entry-submitted POST (one attempt, no retry); Zapier entry trigger | Marketing ops | Feature (Business+) | VIRALSWEEP-007, -035 |
| Managed services | Rules drafting, compliance advice, state registration & bonding, drawings, affidavits, 1099s, fulfillment, PO-box AMOE | Marketing (legal-adjacent) | Add-on service (Elite/Enterprise) | VIRALSWEEP-015, -016 |

## 4. API / developer capability

- **APIs**: Single-page doc at viralsweep.com/api. Endpoints: GET /api/brands; GET /api/promotions/&lt;BRAND_ID&gt; (incl. archived); GET /api/entries/&lt;PROMOTION_ID&gt; (paginated, email search); POST /api/entries/&lt;PROMOTION_ID&gt;; POST /api/points/&lt;PROMOTION_ID&gt; (± points with description); POST /api/validate/&lt;PROMOTION_ID&gt; (valid/invalid/accept/unaccept, bulk); GET /api/winners/&lt;PROMOTION_ID&gt; (timestamp filters). Auth: `x-api-key` header. JSON responses [VIRALSWEEP-005]. **No endpoints create or configure promotions** — the support page's claim that you can "build, run, and manage your own promotions outside of your platform" exceeds the documented surface; campaigns must be built in the UI [VIRALSWEEP-004, -005].
- **SDKs**: None. Docs provide PHP/cURL examples as the intended substitute [VIRALSWEEP-005].
- **Webhooks**: One event (entry submitted), JSON POST, **single delivery attempt, no retry**, no signing documented; Business+ [VIRALSWEEP-007]. Zapier trigger mirrors it [VIRALSWEEP-035].
- **Sandbox**: None documented; guidance is Postman against the live account, and "test entries" are real entries later auto-purged [VIRALSWEEP-006, -019].
- **Rules engine / synchronous decisioning**: None. Entry-time gates (geo/IP/captcha/age field) are fixed platform behaviors, not customer-programmable rules [VIRALSWEEP-008, -009, -022].
- **Latency claims**: None; purchase-based entries "may take a few minutes to appear" (async ingestion) [VIRALSWEEP-025].
- **Versioning / idempotency / rate limits**: None documented; unversioned `/api/...` paths [VIRALSWEEP-005, -006].
- **Integration model**: JS embed + hosted pages; JS tracking scripts for custom actions (client-side, spoofable); 60+ ESP/CRM connectors; Shopify/BigCommerce apps [VIRALSWEEP-002, -024, -025]. Legacy readme.io docs are deprecated [VIRALSWEEP-038].

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** No. Custom form fields and custom actions capture arbitrary data [VIRALSWEEP-022, -024], but no rule language evaluates it; the only evaluated conditions are fixed (geo allowlist, per-IP limits, entry frequency, min-age field, captcha, email code).
- **Store customer/user state?** Partially: entries, points balances (API-adjustable), referral chains, audience segments across campaigns [VIRALSWEEP-003, -005].
- **Return reason codes?** No. Nearest analogs: Invalid tab (spam-filtered) and an orange "suspicious activity" caution label at drawing time [VIRALSWEEP-009, -011].
- **Output allow/deny/review?** Not as an output model. Geo block is a deny at page level; validate/invalidate + accept/unaccept is a post-hoc manual/API review state on entries [VIRALSWEEP-005, -008].
- **Simulate policies?** No. A/B testing exists for creative variants, not rules [VIRALSWEEP-003]; test entries are live entries [VIRALSWEEP-019].
- **Replay decisions?** No decision objects exist to replay [VIRALSWEEP-036].
- **Version policies?** No. Official-rules text is a static block; archived campaigns retain final state only (inference from the archived-promotions API flag) [VIRALSWEEP-005, -014].
- **Deploy rules independently of app code?** N/A — campaigns are configured in the SaaS UI; there is no customer rule artifact to deploy.

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance (product)**: Template rules generator (US/CA-oriented; eligibility countries/states, age 13+/18+/21+; .txt output) with the disclaimer "Viralsweep assumes no responsibility for whether you are in compliance with the law" [VIRALSWEEP-013]; in-builder template repeats "ViralSweep does not guarantee that your promotion complies with local laws" [VIRALSWEEP-014]; consent/disclaimer form fields [VIRALSWEEP-022].
- **Promotion compliance (service)**: Rules drafting, "we'll ensure your promotion complies with the law," state registration & bonding (NY/FL-type filings), winner eligibility verification, affidavits, 1099s over $600, PO-box AMOE — humans, days-level turnaround [VIRALSWEEP-015]. Enterprise tier: "Legal Administration," "Bonding & Registrations," "Security Assessments" [VIRALSWEEP-016].
- **Generic regulatory workflow**: None in product [VIRALSWEEP-036].
- **Jurisdiction restrictions**: IP-based geo targeting by country/state/province with manual IP allowlist overrides; country-only on purchase promos [VIRALSWEEP-008].
- **Location verification**: Basic IP geolocation; doc acknowledges ISP misattribution; no VPN/proxy detection documented [VIRALSWEEP-008].
- **Legal content/rules**: Prose blog series on state sweepstakes laws (Virginia, Alabama 19+, etc.) — educational content, not machine-readable [VIRALSWEEP-039].
- **Regulatory monitoring**: None productized; service team advises [VIRALSWEEP-015, -039].
- **Change management / counsel approval**: Recommended workflow is copy rules → "Submit to your legal team for review before launch" — entirely out-of-band; paid custom drafting by "ViralSweep's legal team" available [VIRALSWEEP-014]. Terms state "We do not provide any legal advice" and require customers to warrant legal compliance — the service marketing and the contract sit in tension [VIRALSWEEP-015, -017].
- **Historical policy state**: Archived campaigns retain final rules text (inference); no version history [VIRALSWEEP-005, -014].
- **Regulated verticals**: Gambling, illegal lotteries, and cryptocurrency promotions are prohibited uses — regulated domains are excluded, not encoded [VIRALSWEEP-017].

## 7. Audit / evidence

Reconstruction ability is entry-level, not decision-level:

- **Exact inputs?** Partially — entry records keep email, name, address, birthday, IP, location, timestamps, referral source, custom fields, and (per GDPR page) consent records; CSV/API export [VIRALSWEEP-005, -007, -018].
- **Exact rule/policy?** No — no rule objects; rules text is a static campaign attribute without versions [VIRALSWEEP-014, -036].
- **Exact version?** No policy/config versioning exists [VIRALSWEEP-036].
- **Exact output?** Winners with win date, entry date, prize, email, IP are retrievable [VIRALSWEEP-005, -011]; blocked/geo-denied attempts are not shown as logged.
- **Exact timestamp?** Entries and winners carry timestamps [VIRALSWEEP-005].
- **Human approvals?** Manual validate/invalidate exists but no documented audit trail of who changed what; the "Editing Entries" feature makes entrant records mutable post-hoc, and invalid entries are irreversibly auto-purged at 180 days — actively hostile to evidence-grade reconstruction [VIRALSWEEP-009, -019, -036].
- **Source/legal authority?** None — generated rules carry no legal citations [VIRALSWEEP-013].

## 8. Enterprise readiness

- **SSO/RBAC**: Two roles only (View Only, Editor), brand-scoped, no promotion-level permissions; no SSO/SAML in official docs (a LOW-confidence aggregator lists Okta SWA password vaulting) [VIRALSWEEP-020, -033].
- **Multitenancy/multi-brand**: Real: 1/2/4/6 brands per plan, per-brand users; agency "host partner sweepstakes" support [VIRALSWEEP-003, -021].
- **Environments**: None; test entries live in production and get purged [VIRALSWEEP-019].
- **Security certifications**: Unverifiable. The former /security page now serves the homepage (no public trust page); historical captures described AWS, encryption, Cloudflare, 2FA, daily encrypted backups; a third-party aggregator's SOC 2/ISO/HIPAA/FedRAMP list is implausible and conflicts with the official site's silence [VIRALSWEEP-032, -033]. Enterprise tier offers "Security Assessments" (participation in customer reviews) [VIRALSWEEP-016].
- **SLA**: None — terms are AS IS, no uptime commitment, liability capped at 12 months of fees [VIRALSWEEP-017].
- **Support/professional services**: Elite "White Glove" (1 promotion built/month); Enterprise custom design/integrations; managed legal-administration services [VIRALSWEEP-003, -015, -016].
- **Customer scale**: Logo wall includes UNIQLO, Georgia Lottery, TaylorMade, Purple, Crutchfield, Wix [VIRALSWEEP-030]; published case studies are SMB/mid-market e-commerce [VIRALSWEEP-031]; GDPR: DPA availability, consent tooling, deletion workflows (2018-era, Privacy Shield-dated) [VIRALSWEEP-018].

## 9. Commercial model

Public pricing $49/$199/$399/$999/mo plus contact-sales Enterprise; unlimited promotions/entries on all tiers; API gated to Premium+ (and enablement request); annual ~17% discount [VIRALSWEEP-003, -004]. Likely buyer: marketing/growth at DTC brands and agencies; legal-administration services purchased through the same marketing relationship [VIRALSWEEP-015]. Implementation burden: hours-to-days (hosted page or embed; JS snippet; native e-commerce apps) [VIRALSWEEP-002, -025]. Sales motion: self-serve + free trial + Shopify App Store (4.4/141 since 2013); services attach at Elite/Enterprise [VIRALSWEEP-029, -016]. Large-customer evidence is logo-level only; no enterprise case studies [VIRALSWEEP-030, -031]. Company: bootstrapped to acquisition by AppHub/Clearer.io (2021), an SMB e-commerce app rollup — the commercial center of gravity is SMB/mid-market e-commerce [VIRALSWEEP-027, -028].

## 10. Strengths

- Broad, mature promotion-type coverage (11 app types incl. instant win with three mechanics, UGC contests, purchase-to-enter) at a low price with unlimited promotions/entries [VIRALSWEEP-001, -002, -003, -010, -025].
- Genuine e-commerce depth: Shopify/BigCommerce order-triggered entries, sales tracking, coupon delivery, 60+ ESP/CRM syncs [VIRALSWEEP-002, -025].
- A real (if thin) escape hatch for developers: entry/points/validation API + entry webhook + Zapier [VIRALSWEEP-005, -007, -035].
- Vertically integrated human compliance service — rules drafting to bonding to 1099s to PO-box AMOE — rare among low-cost SaaS peers and credible enough to win brands like Georgia Lottery on the logo wall [VIRALSWEEP-015, -030].
- Practical anti-abuse defaults (per-IP limits, blacklists, email verification codes, fraud flags at draw time) [VIRALSWEEP-009, -011, -023].
- Multi-brand/agency model built into plans [VIRALSWEEP-021].

## 11. Weaknesses / constraints

Evidence-backed:
- No campaign-creation API, no SDKs, no sandbox, no rate limits/versioning/idempotency docs, one webhook event with single-attempt delivery — the developer platform is peripheral [VIRALSWEEP-005, -006, -007].
- Compliance features disclaim responsibility (rules template), and terms disclaim legal advice while marketing promises "we'll ensure your promotion complies with the law" — the compliance promise is a human service with contractual liability pushed to the customer [VIRALSWEEP-013, -014, -015, -017].
- Geolocation is basic IP allowlisting with manual IP exception handling; no VPN detection [VIRALSWEEP-008].
- Governance is thin: two roles, no SSO documented, no approval workflows, no audit logs, no environments; no public security/trust page today; AS-IS terms with no SLA [VIRALSWEEP-020, -032, -017, -036].
- Records are mutable ("Editing Entries") and invalid entries are irreversibly purged at 180 days — weak evidentiary posture [VIRALSWEEP-019, -036].
- Regulated verticals (gambling, crypto) are contractually excluded [VIRALSWEEP-017].

Inference (labeled): the small-team, bootstrapped-then-rolled-up trajectory [VIRALSWEEP-027, -028] implies limited capacity to build enterprise policy/decisioning infrastructure; nothing in the 58-article feature surface suggests such a roadmap [VIRALSWEEP-036].

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,4,VIRALSWEEP-001;VIRALSWEEP-005;VIRALSWEEP-013;VIRALSWEEP-036
A02,4,VIRALSWEEP-001;VIRALSWEEP-002;VIRALSWEEP-036
A03,3,VIRALSWEEP-010
A04,2,VIRALSWEEP-013;VIRALSWEEP-014
A05,3,VIRALSWEEP-014;VIRALSWEEP-015;VIRALSWEEP-016;VIRALSWEEP-017;VIRALSWEEP-034
A06,2,VIRALSWEEP-015;VIRALSWEEP-026;VIRALSWEEP-034;VIRALSWEEP-037
A07,4,VIRALSWEEP-005;VIRALSWEEP-009;VIRALSWEEP-019;VIRALSWEEP-022;VIRALSWEEP-036
A08,3,VIRALSWEEP-011;VIRALSWEEP-012;VIRALSWEEP-015;VIRALSWEEP-040
A09,2,VIRALSWEEP-015
A10,2,VIRALSWEEP-015;VIRALSWEEP-034
B01,1,VIRALSWEEP-005;VIRALSWEEP-007;VIRALSWEEP-024
B02,1,VIRALSWEEP-008;VIRALSWEEP-009;VIRALSWEEP-022
B03,0,VIRALSWEEP-025
B04,1,VIRALSWEEP-005;VIRALSWEEP-008
B05,1,VIRALSWEEP-009;VIRALSWEEP-011
B06,2,VIRALSWEEP-005;VIRALSWEEP-022;VIRALSWEEP-024
B07,2,VIRALSWEEP-003;VIRALSWEEP-005;VIRALSWEEP-009
B08,0,VIRALSWEEP-036
B09,1,VIRALSWEEP-003;VIRALSWEEP-019
B10,0,VIRALSWEEP-036
C01,1,VIRALSWEEP-008;VIRALSWEEP-013;VIRALSWEEP-039
C02,0,VIRALSWEEP-017;VIRALSWEEP-034
C03,0,VIRALSWEEP-017;VIRALSWEEP-036
C04,1,VIRALSWEEP-005;VIRALSWEEP-013
C05,1,VIRALSWEEP-005
C06,1,VIRALSWEEP-015;VIRALSWEEP-039
C07,0,VIRALSWEEP-036
C08,1,VIRALSWEEP-014;VIRALSWEEP-015
C09,0,VIRALSWEEP-013
C10,0,VIRALSWEEP-013;VIRALSWEEP-036
D01,1,VIRALSWEEP-005;VIRALSWEEP-036
D02,1,VIRALSWEEP-005;VIRALSWEEP-007
D03,0,VIRALSWEEP-014;VIRALSWEEP-036
D04,2,VIRALSWEEP-005;VIRALSWEEP-007;VIRALSWEEP-018
D05,1,VIRALSWEEP-009
D06,1,VIRALSWEEP-005;VIRALSWEEP-011
D07,1,VIRALSWEEP-011;VIRALSWEEP-015
D08,1,VIRALSWEEP-018;VIRALSWEEP-019
D09,0,VIRALSWEEP-019;VIRALSWEEP-036
D10,0,VIRALSWEEP-036
E01,1,VIRALSWEEP-023
E02,1,VIRALSWEEP-013;VIRALSWEEP-022
E03,1,VIRALSWEEP-022;VIRALSWEEP-028
E04,2,VIRALSWEEP-008
E05,?,
E06,0,VIRALSWEEP-008
E07,2,VIRALSWEEP-009;VIRALSWEEP-011
E08,2,VIRALSWEEP-009;VIRALSWEEP-023;VIRALSWEEP-036
E09,1,VIRALSWEEP-009
E10,1,VIRALSWEEP-022
F01,1,VIRALSWEEP-005
F02,1,VIRALSWEEP-005
F03,1,VIRALSWEEP-010;VIRALSWEEP-011
F04,2,VIRALSWEEP-025
F05,1,VIRALSWEEP-005
F06,0,VIRALSWEEP-005;VIRALSWEEP-036
F07,1,VIRALSWEEP-010
F08,0,VIRALSWEEP-005;VIRALSWEEP-036
F09,0,VIRALSWEEP-005;VIRALSWEEP-036
F10,0,VIRALSWEEP-005;VIRALSWEEP-036
G01,3,VIRALSWEEP-003;VIRALSWEEP-021
G02,1,VIRALSWEEP-020
G03,?,
G04,0,VIRALSWEEP-014;VIRALSWEEP-036
G05,1,VIRALSWEEP-019
G06,0,VIRALSWEEP-036
G07,0,VIRALSWEEP-036
G08,2,VIRALSWEEP-007;VIRALSWEEP-035
G09,0,VIRALSWEEP-017
G10,1,VIRALSWEEP-016;VIRALSWEEP-032;VIRALSWEEP-033
H01,2,VIRALSWEEP-004;VIRALSWEEP-005;VIRALSWEEP-038
H02,0,VIRALSWEEP-005
H03,2,VIRALSWEEP-007
H04,0,VIRALSWEEP-006;VIRALSWEEP-019
H05,0,VIRALSWEEP-005;VIRALSWEEP-006
H06,?,
H07,0,VIRALSWEEP-006
H08,?,
H09,1,VIRALSWEEP-011;VIRALSWEEP-013
H10,0,VIRALSWEEP-005
I01,1,VIRALSWEEP-015;VIRALSWEEP-016
I02,1,VIRALSWEEP-004
I03,4,VIRALSWEEP-001;VIRALSWEEP-002;VIRALSWEEP-003
I04,0,VIRALSWEEP-001;VIRALSWEEP-036
I05,2,VIRALSWEEP-030;VIRALSWEEP-031
I06,4,VIRALSWEEP-003;VIRALSWEEP-029
I07,2,VIRALSWEEP-003;VIRALSWEEP-015;VIRALSWEEP-016
I08,1,VIRALSWEEP-011;VIRALSWEEP-029
I09,1,VIRALSWEEP-002;VIRALSWEEP-035
I10,3,VIRALSWEEP-003
J01,1,VIRALSWEEP-008;VIRALSWEEP-013
J02,1,VIRALSWEEP-014;VIRALSWEEP-015
J03,1,VIRALSWEEP-014;VIRALSWEEP-015;VIRALSWEEP-017
J04,0,VIRALSWEEP-036
J05,0,VIRALSWEEP-005
J06,0,VIRALSWEEP-036
J07,0,VIRALSWEEP-019;VIRALSWEEP-036
J08,0,VIRALSWEEP-036
J09,1,VIRALSWEEP-013
J10,0,VIRALSWEEP-036
```

**Scoring notes (reasoned 0s, inferences, and ? squares):**

- **Feature-surface enumeration as absence evidence**: VIRALSWEEP-036 (the support center's complete 58-article Features collection) is used, per the brief, as positive evidence of the product's full feature set. Squares scored 0 citing it (B08, B10, C07, C10, D03, D09, D10, G04, G06, G07, J04, J06–J08, J10) reflect that no rules-engine, simulation, policy-versioning, approval-workflow, audit-log, or decision constructs exist anywhere in the documented product — labeled inference from enumerated scope, not mere non-mention.
- **B03 = 0**: no decisioning product exists to be low-latency; the one automated ingestion path (purchase entries) is documented as taking minutes (VIRALSWEEP-025).
- **C02/C03 = 0**: regulated product/action domains are contractually excluded (gambling, lotteries, crypto prohibited — VIRALSWEEP-017); competitor comparison corroborates no vertical (e.g., alcohol/ABC) expertise (VIRALSWEEP-034, LOW confidence, corroborative only). Labeled inference.
- **C05 = 1 (inference)**: archived campaigns remain retrievable (API archived flag), preserving final rules text — final-state retention, not version history.
- **C09/C10 = 0**: generated rules are boilerplate with no legal citations or machine-readable form (VIRALSWEEP-013); labeled inference from the artifact itself.
- **D09 = 0**: entries are editable post-hoc and invalid entries are irreversibly auto-purged — positive evidence against tamper-evidence (VIRALSWEEP-019, -036).
- **E06 = 0 (inference)**: the documented remedy for geolocation misidentification is a manual IP allowlist; no spoofing/VPN detection exists in docs (VIRALSWEEP-008).
- **F06/F08–F10 = 0**: the entire data model is brands→promotions→entries/points/winners (VIRALSWEEP-005); no value ledger exists for these features to attach to. Architecture-precluded, labeled inference.
- **G09 = 0**: terms are AS IS with no SLA (VIRALSWEEP-017); Enterprise custom paper unknown.
- **H02 = 0**: docs explicitly offer PHP/cURL examples in lieu of SDKs (VIRALSWEEP-005). **H04 = 0**: recommended testing is Postman against the live account; test entries are live data (VIRALSWEEP-006, -019). **H05 = 0**: unversioned paths, no versioning docs (labeled inference). **H07 = 0**: the square is documented rate limits; none are documented (VIRALSWEEP-006). **H10 = 0**: campaigns cannot be created via API, precluding config-as-code (VIRALSWEEP-005).
- **I04 = 0 (inference)**: positioning, plans, and features show no fraud/risk-buyer motion; anti-spam is an embedded feature, not a sold capability.
- **I07/I08/I09 scored as intensity** (higher = more dependency/cost/burden): I07=2 (services optional but prominent at Elite/Enterprise), I08=1 (low lock-in: CSV export, campaign-by-campaign use), I09=1 (light embed/hosted integration).
- **? squares**: E05 (device intelligence — only IP/email signals documented; fingerprinting unknown), G03 (SSO/SAML — absent from official docs; LOW-confidence third-party lists social login/Okta SWA; Enterprise custom unknown), H06 (idempotency semantics of POST /api/entries undocumented), H08 (no customer-facing API/request logs documented, but absence not certain).
- **Score-4 basis**: A01/A02/A07 are the core product per official docs and the API data model; I03/I06 are commercial-fit squares evidenced by official pricing/positioning and marketplace data.

## 13. White-space implications

1. **Already solved (by ViralSweep, for its segment)**: Promotion execution — sweepstakes/contest/instant-win creation, entry management, winner drawing (A01–A03, A07, A08); template rules text (A04, partial); lead-data plumbing to marketing stacks; and — as a human service — rules drafting, registration/bonding, affidavits/1099s, fulfillment, AMOE collection (A05, A06, A09, A10 at service level) [VIRALSWEEP-005, -011, -013, -015].
2. **Partially solved**: Jurisdiction gating (IP geo allowlists, self-attested age — manual per-campaign config, not law-derived) [VIRALSWEEP-008, -022]; fraud/duplicate control (IP thresholds, blacklists, email codes) [VIRALSWEEP-009, -023]; auditability (entry-level records/exports exist; decision-level evidence does not) [VIRALSWEEP-005, -019].
3. **Unsolved (by ViralSweep)**: Everything in the J-hypothesis core — executable jurisdiction-specific policy (J01), legal-to-production workflow with counsel approval in-product (J02/J03), impact analysis (J04), cross-product real-time authorization with reasons (J05, B01–B05), signal normalization (J06), evidence-grade reconstruction/replay (J07/J08 — actively undermined by mutable entries and forced 180-day purges), policy packs and lifecycle control plane (J09/J10) [VIRALSWEEP-005, -017, -019, -036].
4. **Could ViralSweep add the missing capability easily?** No. It would require a rules engine, decision API, policy versioning, audit infrastructure, and enterprise governance none of which exist even in embryo; the team is small, inside an SMB e-commerce app rollup, with a peripheral 7-endpoint API and no SDKs/sandbox [VIRALSWEEP-005, -027, -028, -036]. Labeled inference: capability and incentive both point away from enterprise policy infrastructure.
5. **Could a customer assemble it with ViralSweep + internal engineering?** Only weakly. ViralSweep could serve as the promotion-execution front end while internal systems make decisions, using POST /api/entries, /points, /validate for enforcement after the fact [VIRALSWEEP-005]. But with no campaign-creation API, no synchronous decision hook at entry time, one non-retried webhook event, and no policy/audit layer, the assembly would be post-hoc filtering, not authorization — the compliance logic and evidence would live entirely in the customer's code.
6. **What would make a customer buy a separate product instead?** Needs ViralSweep structurally cannot meet: real-time allow/deny/review with reason codes across multiple products (not one campaign page); counsel-governed, versioned policy with approvals and provenance; regulator-defensible decision reconstruction (immutable, retained, replayable — vs mutable entries and forced purges); multi-jurisdiction gambling/alcohol/financial-promotion rules (ViralSweep contractually excludes gambling); enterprise governance (SSO, audit logs, SLA, certifications) [VIRALSWEEP-005, -017, -019, -020, -032]. A buyer with those needs today pairs outside counsel and a full-service administrator or builds in-house — ViralSweep is not the tool they are extending.

## 14. Replacement risk

**LOW.**

ViralSweep's gravity is SMB/mid-market e-commerce marketing: self-serve pricing, Shopify-centric distribution, and an owner (Clearer.io) assembling conversion-tool apps [VIRALSWEEP-003, -028, -029]. Entering the proposed space would require building real-time decisioning, policy versioning/approvals, evidence infrastructure, identity/geo signal orchestration, and enterprise governance from zero — none is present even in minimal form, and several current behaviors (mutable entries, forced purges, AS-IS terms, no trust page) run opposite to it [VIRALSWEEP-005, -017, -019, -032, -036]. Its credible adjacent move is deepening the human legal-administration service, which competes with the proposed product only as a services substitute, not as software. Risk of ViralSweep productizing a regulatory control plane within a strategy horizon: low. (Inference from capability + ownership trajectory.)

## 15. Adjacent discoveries

Additional companies/substitutes that should be considered (beyond the assigned 15):

- **Gleam (gleam.io)** — the most frequently cross-shopped SaaS giveaway platform (from ~$79/mo); defines the self-serve segment's feature baseline and price ceiling; any promotion-administration white space must clear "Gleam + a lawyer is good enough" [VIRALSWEEP-041].
- **SweepWidget (sweepwidget.com)** — low-cost challenger (from ~$25/mo) with 90+ entry methods across 30+ platforms; evidence that campaign-execution features are commoditizing toward zero price [VIRALSWEEP-041].
- **Woobox (woobox.com)** — long-running contest/coupon platform with explicit enterprise plans; another incumbent for the same marketing buyer [VIRALSWEEP-034, -041].
- **Full-service promotion administrators (services substitute class)** — e.g., PrizeLogic, Marden-Kane, National Sweepstakes Company: agencies/administrators providing the same legal administration, bonding, drawings, and fulfillment ViralSweep sells at Elite/Enterprise, entirely as services. Flagged for Manager A: this class is the true incumbent for the compliance budget at enterprise scale (identified from landscape context during research; not deeply researched here — corroborated in kind by ViralSweep's own management offering [VIRALSWEEP-015] and Sweeppea's positioning [VIRALSWEEP-034]).
- **Clearer.io (parent)** — relevant as context: its portfolio logic (reviews, returns, address validation, promotions) shows where ViralSweep's roadmap points — e-commerce conversion, not compliance [VIRALSWEEP-028].

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/05_viralsweep.jsonl` (41 records). Same records:

| Claim ID | Claim (abbreviated) | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| VIRALSWEEP-001 | Core product: self-serve sweepstakes/giveaway/contest/instant-win SaaS for list growth | https://www.viralsweep.com | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-002 | 11 promotion app types; hosted/embed model; 60+ ESP/CRM + e-commerce integrations | https://www.viralsweep.com/products/ | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-003 | Pricing $49/$199/$399/$999 + Enterprise; API at Premium+; white glove at Elite | https://www.viralsweep.com/pricing | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-004 | API requires Premium+ AND support enablement; positioned for external promotion management | https://support.viralsweep.com/en/articles/9272675-api | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-005 | Full API surface = 7 data endpoints; x-api-key; no campaign creation; unversioned | https://www.viralsweep.com/api | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-006 | No rate limits, versioning, idempotency, sandbox, or error catalog documented; Postman-on-live testing | https://www.viralsweep.com/api | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-007 | Webhooks: entry-submitted only, JSON POST, single attempt, no retry/signing; Business+ | https://support.viralsweep.com/en/articles/9272620-webhooks | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-008 | Geo Targeting: IP-based country/state/province allowlist; manual IP exceptions; no VPN detection | https://support.viralsweep.com/en/articles/9272641-geo-targeting | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-009 | Spam filter: 1 entry/IP default, internal blacklists, Invalid tab, manual re-validation, events mode | https://support.viralsweep.com/en/articles/9272760-invalid-entries | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-010 | Instant win: random odds, seeded win times, winning codes; coupon prizes; re-entry timer | https://www.viralsweep.com/instant-win/ | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-011 | Draws: weighted random, date-range/daily draws, repeat toggle, fraud caution label, redraw, no auto-notify, CSV | https://support.viralsweep.com/en/articles/9272631-draw-winners | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-012 | Live Draws: streamable, fixed 10s countdown; no certification/recording documented | https://support.viralsweep.com/en/articles/9272630-live-draws | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-013 | Free rules generator: template, US/CA focus, age 13/18/21, "assumes no responsibility" disclaimer | https://www.viralsweep.com/sweepstakes-rules-generator/ | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-014 | In-builder template: "does not guarantee... complies with local laws"; external legal review recommended; paid drafting | https://support.viralsweep.com/en/articles/9272715-using-viralsweep-s-official-rules-template | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-015 | Managed services: rules drafting, compliance advice, registration/bonding, drawings, affidavits, 1099s, fulfillment, PO-box AMOE | https://www.viralsweep.com/management/ | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-016 | Enterprise tier = Custom Design/Integrations, Legal Administration, Bonding & Registrations, Security Assessments | https://www.viralsweep.com/pricing/ | official-marketing | 2026-08-18 | HIGH |
| VIRALSWEEP-017 | T&C (Clearer): no legal advice; customer warrants compliance; AS IS, no SLA; 12-mo liability cap; gambling/crypto prohibited | https://www.viralsweep.com/terms-and-conditions/ | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-018 | GDPR (2018): Privacy Shield, DPO, DPAs, standalone consent, per-email export, 30-day deletion | https://www.viralsweep.com/blog/gdpr/ | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-019 | Invalid entries auto-purged every 180 days, irreversibly; not user-controllable; test entries are live | https://support.viralsweep.com/en/articles/9272634-entry-purging | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-020 | Two roles (View Only/Editor), brand-scoped, no promotion-level perms, no SSO documented | https://support.viralsweep.com/en/articles/9272753-additional-users | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-021 | Multi-brand: 1/2/4/6 brands by plan; agency support | https://www.viralsweep.com/pricing | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-022 | Form fields: birthday w/ min age, US address autocomplete, consent/GDPR fields, reCAPTCHA, signature, payments | https://support.viralsweep.com/en/articles/9272639-custom-form-fields | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-023 | Verification Codes = email-possession verification (Business+) | https://support.viralsweep.com/en/articles/9272653-verification-codes | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-024 | Custom Actions: JS tracking scripts award bonus entries; client-side verification only | https://support.viralsweep.com/en/articles/9272717-custom-actions | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-025 | Purchases app: auto entries per $ on Shopify/BigCommerce orders, minutes delay, plan order caps | https://support.viralsweep.com/en/articles/9272785-shopify-purchase-promotions-setup | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-026 | Receipt upload via form File Upload; no automated validation documented | https://support.viralsweep.com/en/articles/15693296-how-to-upload-a-receipt-for-sweepstakes-entry | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-027 | Founded 2012 (Massaro/Kovar), bootstrapped, 1–10 employees listed | https://tracxn.com/d/companies/viralsweep/__4vda2O28v319VOPXXqOQZiOCYnv2e7cXpfMZVdoPyeM | third-party | 2026-08-18 | MEDIUM |
| VIRALSWEEP-028 | Acquired by AppHub Nov 2021; now in Clearer.io e-commerce app family | https://www.viralsweep.com/blog/clearer-io-smarter-ecommerce/ | official-marketing | 2026-08-18 | MEDIUM |
| VIRALSWEEP-029 | Shopify app since 2013; 4.4/5 across 141 reviews; HQ Boston per listing | https://apps.shopify.com/viralsweep | third-party | 2026-08-18 | HIGH |
| VIRALSWEEP-030 | Logo wall: UNIQLO, Georgia Lottery, TaylorMade, Purple, Crutchfield, Wix, etc. | https://www.viralsweep.com/sweepstakes/ | official-marketing | 2026-08-18 | MEDIUM |
| VIRALSWEEP-031 | Case studies are SMB/mid-market e-commerce; no enterprise/regulated case study | https://www.viralsweep.com/resources/case-studies | official-marketing | 2026-08-18 | MEDIUM |
| VIRALSWEEP-032 | No current public security/trust page; former /security URL serves homepage | https://www.viralsweep.com/security | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-033 | Aggregator lists implausible cert set (SOC 2/ISO/HIPAA/FedRAMP); conflicts with official silence | https://security-profiles.nudgesecurity.com/app/viralsweep-com | third-party | 2026-08-18 | LOW |
| VIRALSWEEP-034 | Sweeppea comparison: ViralSweep = agencies/e-comm lead gen; bonding as service; no third-party administrator drawing/AMOE mgmt/alcohol expertise | https://www.sweeppea.com/sweepstakes-platform-comparison | third-party | 2026-08-18 | LOW |
| VIRALSWEEP-035 | Zapier integration with "entry received" trigger to thousands of apps | https://zapier.com/apps/viralsweep/integrations | third-party | 2026-08-18 | MEDIUM |
| VIRALSWEEP-036 | Features collection enumerates full 58-article feature surface; no SSO/sandbox/approvals/audit-logs/rules-engine articles; entries editable | https://support.viralsweep.com/en/collections/9390193-features | official-doc | 2026-08-18 | HIGH |
| VIRALSWEEP-037 | AMOE "made easy" claim; no dedicated AMOE product tooling documented; mail-in AMOE = service PO box | https://www.viralsweep.com/blog/alternate-method-of-entry-sweepstakes | official-marketing | 2026-08-18 | MEDIUM |
| VIRALSWEEP-038 | readme.io developer docs deprecated in favor of support center | https://viralsweep.readme.io/docs/getting-started | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-039 | State-by-state sweepstakes-law blog series (prose education, e.g., Alabama 19+) | https://www.viralsweep.com/blog/sweepstakes-laws-by-state-virginia | official-marketing | 2026-08-18 | MEDIUM |
| VIRALSWEEP-040 | Legacy draw docs: auto-draw, FRAUD DETECTION redraw prompt, winner email+IP, no auto contact | https://viralsweep.readme.io/docs/choose-winners | official-doc | 2026-08-18 | MEDIUM |
| VIRALSWEEP-041 | Competitive set: Gleam (~$79+), SweepWidget (~$25+), Woobox, Rafflecopter, Vyper; commoditizing segment | https://www.saashub.com/viralsweep-alternatives | third-party | 2026-08-18 | MEDIUM |

## 17. Verdict

**SUBSTITUTE**

ViralSweep does not overlap the Promotion OS core: it has no rules engine, no decision API, no policy versioning, no counsel workflow, no evidence-grade audit (entries are editable; invalid entries are force-purged), and it contractually excludes gambling while disclaiming legal advice. But it is a potent substitute for the promotion-administration slice of the hypothesis: for a large share of brands, "ViralSweep at $49–$999/mo + template rules + geo blocking + its human legal-administration service (or outside counsel)" adequately absorbs the sweepstakes-compliance job, capping willingness to pay for platformized compliance in this vertical. Its buyer is marketing, not legal/risk, and its trajectory (Clearer.io e-commerce rollup) points away from enterprise policy infrastructure — so it is unlikely to enter the space (replacement risk LOW), yet it defines the "good enough" status quo any Promotion OS wedge must displace.

