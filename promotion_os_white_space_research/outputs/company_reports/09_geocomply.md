# Company Report — GeoComply

Researcher: Research Agent 09 (GeoComply)
Date: 2026-08-18
Category: Compliance signals / orchestration
Manager: Manager C

## 1. Executive summary

GeoComply (founded 2011, Vancouver; minority investors Blackstone Growth and Atairos) is the de facto standard **geolocation-compliance and fraud-signal vendor for regulated online gambling**, now expanding the same stack into fintech/crypto sanctions compliance, streaming anti-piracy, and prediction markets. Its actual core product is a **managed, jurisdiction-aware "may this user perform this regulated action from where they are, on this device, as who they claim to be" decision service**: device-level location verification (Core/PinPoint/BrowserGuard), VPN/proxy detection (GeoGuard), orchestrated multi-vendor KYC/AML (IDComply), fraud analytics (RiskGuard/fraud suite), chargeback evidence (GCI), and licensing-workflow software (OneComply). [GEOCOMPLY-001, -003, -009, -017, -019]

Who buys it: compliance and risk officers at regulated operators — sportsbooks/iGaming (FanDuel, DraftKings, Caesars, BetMGM, Hard Rock), streaming (Amazon Prime Video, BBC, MultiChoice), fintech/crypto (Luno, Betr, Dabble), and now prediction markets — because state regulators (and in Kalshi's case, courts) effectively require this control. WSJ-reported >90% of the US sports-betting market are clients; ~2B transactions/month. [GEOCOMPLY-024, -026, -002]

The job it is hired to do: **keep a regulated operator provably inside its licensed jurisdictions and KYC obligations at transaction time, with pass rates high enough not to lose customers** — and produce the location/device evidence when disputes arise. Answer to the core question: the suite **already combines location + KYC + fraud into one converged decision layer** (one endpoint in Brazil/Alberta), and adds a **licensing** workflow product (OneComply) — but "compliance workflow" beyond licensing and "policy management" as a customer-facing product do **not** exist: all regulatory rule encoding is vendor-internal managed service. [GEOCOMPLY-027, -028, -010]

Note on assignment scope: no current product named **"Chameleon"** exists; the name traces to SBTech's "Chameleon360" platform (a GeoComply integration partner), not to GeoComply. Fraud capability lives in Core's fraud suite, RiskGuard, and GCI. [GEOCOMPLY-036, -035]

## 2. Product architecture

Concrete flow (documented for Core, the flagship; corroborated by official pages and third-party integration writeups):

**INPUT** → Client-side SDK (native iOS 16+/Android 10+; Windows/macOS PLC plugin bridged to the browser JS SDK over a local WebSocket; BrowserGuard silent browser checks in newer markets) collects GPS/Wi-Fi/cellular/IP plus device-integrity signals (jailbreak/root, emulators, fake-location apps, remote access tools) into an **encrypted, tamper-resistant payload**. [GEOCOMPLY-003, -004, -008, -028]

**DECISION/PROCESS** → Operator backend authenticates (per-environment API key/secret → short-lived license token) and submits the payload to GeoComply's server-side API. GeoComply's vendor-operated rules engine (~28,000 data-integrity conditions, new rule ~every 18h, ML anomaly models "RiskGuard") evaluates it against the **jurisdiction's regulatory geolocation requirements** in milliseconds. [GEOCOMPLY-005, -007, -035]

**OUTPUT** → A structured result: resolved jurisdiction/state code, an **allow/block decision**, and **reason codes ("troubleshooter")** that the operator maps to deny / prompt-user-to-fix / re-check logic; plus dashboards, fraud reports (multi-user devices, bonus-hunter hotspots), configurable auto-block rules, and 6-month-to-2-year historical location/device records that GCI packages into dispute-grade evidence reports. [GEOCOMPLY-007, -006, -017]

IDComply is a parallel decision service: one API call → waterfall across multiple KYC data/document/KBA/phone vendors per the jurisdiction's KYC rules → verified/not-verified outcome plus sanctions/PEP screening, sharing "a single back-office and API" with geolocation. [GEOCOMPLY-009, -010, -011, -013]

OneComply is separate workflow SaaS: entity/personnel data repository → OmniFill auto-generates jurisdiction-specific license applications → tracking, deadlines, material-change alerts, audit reporting, secure regulator file-sharing. [GEOCOMPLY-019, -020]

## 3. Main products/modules

| Product/module | What it does | Buyer | Core vs add-on | Evidence |
|---|---|---|---|---|
| GeoComply Core | Device-level geolocation compliance + anti-fraud decisioning (allow/block + reason codes) for regulated transactions; SDKs all platforms; dashboards | Compliance/risk at gaming operators (now fintech, prediction markets) | Core (flagship) | GEOCOMPLY-003, -004, -007 |
| IDComply | Managed multi-vendor KYC/AML waterfall via one API: data, doc+selfie, KBA, phone; PEP/OFAC/sanctions screening; per-jurisdiction requirement engine | Compliance at regulated operators | Core (second pillar) | GEOCOMPLY-009, -010, -011, -013 |
| GeoGuard | VPN/proxy/Tor/hijacked-residential-IP detection; 310M+ IP DB, hourly updates; cloud API, on-prem, CDN edge (CloudFront/Akamai, AWS Marketplace) | Streaming/OTT anti-piracy; sanctions compliance; gaming | Core for media vertical | GEOCOMPLY-014, -015 |
| PinPoint | Beacon-based on-property geofencing to ~1m for casino-property wagering | Land-based/omnichannel operators | Add-on | GEOCOMPLY-016 |
| GCI (Chargeback Integrator) | Evidence reports (≤60s) from 6mo–2yr location/device history; accepted by 70+ processors; Visa CE3.0; bulk case processing | Payments/fraud teams | Add-on (monetizes data exhaust) | GEOCOMPLY-017, -018 |
| OneComply | Licensing/compliance workflow: OmniFill application generation across US/Canada jurisdictions, license tracking, material-change alerts, audit reporting, regulator file-sharing | Legal/compliance & licensing teams; also regulators themselves | Add-on (acquired) | GEOCOMPLY-019, -020, -021 |
| RiskGuard / fraud suite | 24/7 ML anomaly detection on geolocation patterns; custom fraud tags; industry-shared fraud database; auto-block across jurisdictions | Fraud/risk teams | Embedded in Core offering | GEOCOMPLY-035, -006 |
| BrowserGuard / GeoValidator | Adaptive silent browser geolocation; real-time address matching + deepfake detection (newer markets: Alberta, Brazil) | Operators in new markets | Evolution of Core/IDComply | GEOCOMPLY-028, -027 |

## 4. API / developer capability

- **APIs**: Server-side decision/decryption API for Core (license-token auth, per-environment keys); IDComply "single API call" for full KYC waterfall; GeoGuard cloud API / on-prem DB / CDN-edge integration. No public, self-serve API reference: integrationdocs.geocomply.com is authentication-gated (and did not resolve from this environment — reduced confidence flag). [GEOCOMPLY-007, -013, -014]
- **SDKs**: iOS 16+, Android 10+, Windows 10+/macOS 12+ (PLC plugin), browser JS (local WebSocket bridge, port 54321); BrowserGuard silent web checks in newer markets. SDK binaries distributed via onboarding pack tied to the operator's license — not npm/self-serve. GitHub org has only ~4 public repos. [GEOCOMPLY-008, -028]
- **Webhooks**: not documented publicly (unresolved).
- **Sandbox**: per-environment (staging/production) credentials per third-party writeups; no public sandbox. [GEOCOMPLY-007]
- **Rules engine**: vendor-operated (28k conditions, ML); customer-facing configuration is limited to risk-tolerance/auto-block rules and KYC flow tuning, largely done with GeoComply's team. [GEOCOMPLY-005, -006, -013]
- **Synchronous decisioning / latency**: yes — location checks gate wager placement in real time; "milliseconds," 15,000 checks/sec capacity claim, 99.999% uptime in regulated environments. [GEOCOMPLY-003, -027, -028]
- **Versioning / idempotency / rate limits**: none documented publicly; third-party guidance treats idempotency/reconciliation as the integrator's job (unresolved).
- **Integration model**: heavyweight for Core (client SDK on every platform + server-side integration + regulator certification of the deployment); lightweight for GeoGuard (turn-on via CloudFront/Akamai/AWS Marketplace) and IDComply (single API). Ontario→Alberta activation "in hours with no code changes" shows jurisdiction expansion is config-only once integrated. [GEOCOMPLY-007, -015, -028]

## 5. Rules / decision model

- **Evaluate arbitrary attributes?** No evidence. Inputs are GeoComply-defined signal sets (location, device, identity). Custom fraud tags on accounts are the only documented customer-supplied attribute. [GEOCOMPLY-035]
- **Store customer/user state?** Yes — device/user history, behavioral profiles, 6mo–2yr location history, industry-shared fraud database. [GEOCOMPLY-004, -017, -035]
- **Return reason codes?** Yes — the "troubleshooter" reason-code set accompanying each allow/block result; official pages reference "enhanced troubleshooter messages." [GEOCOMPLY-003, -007]
- **Output allow/deny/review?** Allow/block plus reason codes documented; "review" exists only informally via fraud flags/reports, not as a formal triage state. [GEOCOMPLY-007, -006]
- **Simulate policies?** Not documented (unresolved).
- **Replay decisions?** Not as a product feature; historical evidence reports (GCI) reconstruct user location/device state at past transaction times, which is retrospective data reconstruction, not policy replay. [GEOCOMPLY-017, -018]
- **Version policies?** Vendor-internal; no customer-visible policy versioning documented (unresolved).
- **Deploy rules independently of app code?** For GeoComply's own rules, yes (vendor pushes rule updates ~every 18h; new jurisdictions activated config-only). Customers cannot author/deploy their own regulatory rules. [GEOCOMPLY-005, -028]

## 6. Regulatory and jurisdiction functionality

- **Promotion compliance**: none. Closest is *promotion-abuse* (bonus abuse) fraud detection — protecting the operator's promo budget, not administering or legally clearing promotions. [GEOCOMPLY-001, -004]
- **Generic regulatory workflow**: no. The only workflow product is OneComply, which is licensing-specific (applications, renewals, disclosures, personnel licensing). [GEOCOMPLY-019, -020]
- **Jurisdiction restrictions**: category-defining. Per-state/province/country geofencing of regulated actions is the core business; regulators/courts treat it as the standard control (Washington court ordered Kalshi to deploy "a GeoComply multi-source geofencing system"). [GEOCOMPLY-003, -026]
- **Location verification**: category-leading (multi-source device signals; PinPoint to ~1m; GeoGuard for IP integrity). [GEOCOMPLY-003, -014, -016]
- **Legal content/rules**: rules implementing each jurisdiction's geolocation/KYC requirements are encoded and maintained **by GeoComply internally** ("custom-built, locally tuned" per market; IDComply "customizable fields that meet each jurisdiction's compliance rules"). Not exposed as machine-readable policy, no legal-source citations surfaced. [GEOCOMPLY-027, -010]
- **Regulatory monitoring**: service-based, not software: a Government Relations team "stays ahead" of regulator requirements (AGLC example); IDComply relieves operators of tracking KYC rule changes. OneComply monitors *the customer's own* disclosure obligations (material-change alerts), not external regulation. [GEOCOMPLY-028, -010, -020]
- **Change management**: vendor-side rule updates every ~18h; day-one activation at market launches (Missouri: 2.6M checks in first 24h); no customer-facing change-management tooling documented. [GEOCOMPLY-005, -029]
- **Counsel approval**: no counsel-as-approver feature anywhere in the suite. OneComply routes licensing filings that legal teams work on, which is adjacent but not rule approval. [GEOCOMPLY-020]
- **Historical policy state**: not documented. Historical *data* is retained (6mo–2yr); historical *rule versions* are not customer-accessible. [GEOCOMPLY-017]

## 7. Audit / evidence

Can a customer reconstruct:
- **Exact inputs?** Partially — GCI evidence reports include location history, device-integrity results, IP data for a given user/transaction. [GEOCOMPLY-017]
- **Exact rule/policy?** No evidence. The rule set that produced a decision is vendor-internal.
- **Exact version?** No evidence (policy versioning not exposed).
- **Exact output?** Yes — decision + reason codes are returned to and logged by the operator; dashboards expose transaction analysis. [GEOCOMPLY-007, -003]
- **Exact timestamp?** Yes — "extremely precise timestamps on user activity and their location," strong enough to win bank disputes. [GEOCOMPLY-018]
- **Human approvals?** Only in OneComply's licensing-task domain (tasks, communications, audit reporting for regulatory reviews); not for decisions. [GEOCOMPLY-020]
- **Source/legal authority?** No evidence of legal-citation provenance on any decision.

Net: GeoComply produces **evidence-grade reconstructions of user/device/location facts** (its GCI business depends on them being accepted by 70+ processors and banks), but **not evidence-grade reconstructions of the decision logic** (which rule version, why, under whose approval). That half of the audit story is absent from all public materials.

## 8. Enterprise readiness

- **SSO/RBAC**: not publicly documented for the back office (unresolved; SOC 2 implies access controls internally). [GEOCOMPLY-22]
- **Multitenancy/multi-brand**: operates across operators' multiple brands/states (Caesars across every licensed market; FanDuel's full product line), but tenancy/brand hierarchy features are undocumented. [GEOCOMPLY-025]
- **Environments**: staging/production credentials per third-party docs. [GEOCOMPLY-007]
- **Security certifications**: SOC 2 (maintained, report under NDA via trust.geocomply.com); AES-256/IP-allowlisting/2FA claims on OneComply; ISO 27001 not mentioned. [GEOCOMPLY-022, -020]
- **SLA**: 99.999% uptime "in regulated environments" (official PR; homepage says 99.9999% — treat as marketing). [GEOCOMPLY-027, -002]
- **Support/professional services**: heavy managed-service model — in-house experts tune KYC flows and UX, "dedicated vendor management and optimization," Government Relations team per market. [GEOCOMPLY-013, -027, -028]
- **Customer scale**: FanDuel (13-year relationship), DraftKings, Caesars, BetMGM, Hard Rock, Amazon Prime Video, BBC, Kaizen/Betano; >90% of US sports-betting market (WSJ 2023); ~2B transactions/month; 400M+ installed devices. [GEOCOMPLY-024, -025, -027, -033]
- **Regulatory standing**: itself licensed by gaming regulators (NJ DGE approval for IDComply; Missouri sports wagering supplier license); claims "15+ years... $0 in compliance fines." [GEOCOMPLY-011, -029, -028]

## 9. Commercial model

- **Pricing**: not public for Core/IDComply (Capterra: contact vendor). Historic model reported as per-geolocation-check (competitor Radar attacks "per location ping" pricing with MTU pricing). IDComply brochure discloses model terms: one price, no integration/licensing fees, no volume commitments. [GEOCOMPLY-034, -032, -013]
- **Likely buyer**: Chief Compliance Officer / VP Risk & Compliance at regulated operators; fraud/payments leaders for GCI; licensing/legal ops for OneComply; content-protection leads for GeoGuard.
- **Implementation burden**: high for Core (multi-platform SDKs, desktop plugin, server integration, regulator certification); low for GeoGuard (CDN toggle/AWS Marketplace); medium-low for IDComply (single API + managed tuning). [GEOCOMPLY-007, -015, -013]
- **Sales motion**: enterprise sales-led, license-gated distribution; no self-serve except GeoGuard via AWS Marketplace. [GEOCOMPLY-008, -015]
- **Evidence of large customers**: multi-year renewals in 2026 with FanDuel (incl. FanDuel Predicts), DraftKings (super app), Caesars, Hard Rock. [GEOCOMPLY-025]

## 10. Strengths

- **Regulator-embedded moat**: the vendor itself is licensed by gaming regulators; courts and regulators name its product as the required control; "GeoComply multi-source geofencing" appears in a court order. [GEOCOMPLY-011, -029, -026]
- **Converged signal suite, genuinely unified**: location + device + identity + fraud through "a single back-office and API"; sold as one endpoint in Brazil/Alberta. This is real cross-signal integration, not bundling in name. [GEOCOMPLY-011, -027, -028]
- **Jurisdiction operations at scale**: 30+ jurisdictions, day-one market launches (Missouri 2.6M checks/24h), config-only expansion (Ontario→Alberta in hours). [GEOCOMPLY-027, -029, -028]
- **Vendor orchestration done as a business**: IDComply absorbs KYC vendor procurement, contracts, and waterfall logic behind one API with one price — the normalization layer as a managed service. [GEOCOMPLY-013]
- **Evidence monetization**: 6mo–2yr location/device history productized into dispute evidence accepted by 70+ processors (GCI). [GEOCOMPLY-017, -018]
- **Scale and reliability**: ~2B transactions/month, 15k checks/sec, 99.999% uptime claims, SOC 2. [GEOCOMPLY-002, -028, -022]

## 11. Weaknesses / constraints

- **No customer-facing policy layer**: rules are a black-box managed service; customers cannot author, version, simulate, approve, or replay policies. (Documented absence of any such feature across official materials; labeled inference.) [GEOCOMPLY-005, -007]
- **Decision evidence lacks policy provenance**: evidence reports reconstruct facts, not rule versions or approval chains (see Section 7).
- **Patent moat invalidated**: the "Geolocation Engine" patent was ruled too broad/non-inventive (Delaware 2023; Federal Circuit affirmed Nov 2024) — the market is legally open to Xpoint, Radar, LocationSmart. [GEOCOMPLY-031]
- **Competitive and structural pressure**: April 2026 layoffs of ~80 (~18%) citing AI shifts, regulatory change, and competition (Xpoint, Radar named). [GEOCOMPLY-030, -032]
- **Vertical concentration**: revenue overwhelmingly tied to regulated gambling's geolocation mandates; fintech/media are smaller adjacencies (inference from customer mix and market-share reporting). [GEOCOMPLY-024]
- **Closed developer experience**: license-gated SDKs/docs, no public API reference, no self-serve — a deliberate compliance posture, but a wedge competitors (Radar) attack with developer-first positioning. [GEOCOMPLY-008, -032]
- **Not a promotions/incentives system**: nothing in the suite touches promotion administration, official rules, fulfillment, or ledgers. [GEOCOMPLY-001]

## 12. Capability matrix scores

```csv
square,score,claim_ids
A01,0,GEOCOMPLY-001
A02,0,GEOCOMPLY-001
A03,0,GEOCOMPLY-001
A04,0,GEOCOMPLY-001
A05,0,GEOCOMPLY-001
A06,0,GEOCOMPLY-001
A07,0,GEOCOMPLY-001
A08,0,GEOCOMPLY-001
A09,0,GEOCOMPLY-001
A10,0,GEOCOMPLY-001
B01,2,GEOCOMPLY-007;GEOCOMPLY-003
B02,3,GEOCOMPLY-003;GEOCOMPLY-005;GEOCOMPLY-007
B03,3,GEOCOMPLY-003;GEOCOMPLY-027;GEOCOMPLY-028
B04,2,GEOCOMPLY-007;GEOCOMPLY-006;GEOCOMPLY-035
B05,3,GEOCOMPLY-003;GEOCOMPLY-007
B06,1,GEOCOMPLY-035;GEOCOMPLY-006
B07,3,GEOCOMPLY-003;GEOCOMPLY-004;GEOCOMPLY-017
B08,?,
B09,?,
B10,1,GEOCOMPLY-017;GEOCOMPLY-018
C01,3,GEOCOMPLY-010;GEOCOMPLY-011;GEOCOMPLY-027;GEOCOMPLY-028;GEOCOMPLY-029
C02,2,GEOCOMPLY-001;GEOCOMPLY-016;GEOCOMPLY-023
C03,2,GEOCOMPLY-007;GEOCOMPLY-026
C04,1,GEOCOMPLY-029;GEOCOMPLY-028
C05,?,
C06,2,GEOCOMPLY-028;GEOCOMPLY-010
C07,?,
C08,1,GEOCOMPLY-020
C09,?,
C10,0,GEOCOMPLY-005;GEOCOMPLY-007
D01,2,GEOCOMPLY-007;GEOCOMPLY-017
D02,3,GEOCOMPLY-017;GEOCOMPLY-003
D03,?,
D04,2,GEOCOMPLY-017;GEOCOMPLY-018
D05,1,GEOCOMPLY-020
D06,2,GEOCOMPLY-017;GEOCOMPLY-018
D07,3,GEOCOMPLY-017;GEOCOMPLY-018;GEOCOMPLY-020
D08,2,GEOCOMPLY-017
D09,2,GEOCOMPLY-005;GEOCOMPLY-003
D10,2,GEOCOMPLY-006;GEOCOMPLY-020
E01,3,GEOCOMPLY-009;GEOCOMPLY-011;GEOCOMPLY-012
E02,3,GEOCOMPLY-009;GEOCOMPLY-011
E03,2,GEOCOMPLY-009;GEOCOMPLY-028
E04,4,GEOCOMPLY-003;GEOCOMPLY-024;GEOCOMPLY-029;GEOCOMPLY-016
E05,3,GEOCOMPLY-004;GEOCOMPLY-005
E06,4,GEOCOMPLY-014;GEOCOMPLY-015
E07,3,GEOCOMPLY-035;GEOCOMPLY-028;GEOCOMPLY-006
E08,3,GEOCOMPLY-004;GEOCOMPLY-006;GEOCOMPLY-009
E09,2,GEOCOMPLY-017;GEOCOMPLY-035
E10,3,GEOCOMPLY-009;GEOCOMPLY-010;GEOCOMPLY-013
F01,0,GEOCOMPLY-001
F02,0,GEOCOMPLY-001
F03,0,GEOCOMPLY-001
F04,0,GEOCOMPLY-001
F05,0,GEOCOMPLY-001
F06,0,GEOCOMPLY-001
F07,0,GEOCOMPLY-001
F08,0,GEOCOMPLY-001
F09,0,GEOCOMPLY-001
F10,0,GEOCOMPLY-001
G01,2,GEOCOMPLY-024;GEOCOMPLY-025
G02,?,
G03,?,
G04,1,GEOCOMPLY-020
G05,2,GEOCOMPLY-007
G06,?,
G07,1,GEOCOMPLY-005;GEOCOMPLY-028
G08,?,
G09,3,GEOCOMPLY-027;GEOCOMPLY-028;GEOCOMPLY-002
G10,3,GEOCOMPLY-022
H01,2,GEOCOMPLY-007;GEOCOMPLY-012
H02,3,GEOCOMPLY-003;GEOCOMPLY-008
H03,?,
H04,1,GEOCOMPLY-007
H05,?,
H06,?,
H07,?,
H08,2,GEOCOMPLY-006;GEOCOMPLY-003;GEOCOMPLY-012
H09,?,
H10,0,GEOCOMPLY-008
I01,4,GEOCOMPLY-011;GEOCOMPLY-029;GEOCOMPLY-022;GEOCOMPLY-021
I02,2,GEOCOMPLY-007;GEOCOMPLY-008
I03,0,GEOCOMPLY-001
I04,3,GEOCOMPLY-006;GEOCOMPLY-017;GEOCOMPLY-035
I05,4,GEOCOMPLY-024;GEOCOMPLY-025;GEOCOMPLY-027
I06,1,GEOCOMPLY-015;GEOCOMPLY-034
I07,3,GEOCOMPLY-013;GEOCOMPLY-027;GEOCOMPLY-028
I08,3,GEOCOMPLY-025;GEOCOMPLY-024;GEOCOMPLY-031
I09,3,GEOCOMPLY-007;GEOCOMPLY-008
I10,1,GEOCOMPLY-034;GEOCOMPLY-013
J01,2,GEOCOMPLY-010;GEOCOMPLY-027;GEOCOMPLY-028
J02,0,GEOCOMPLY-005;GEOCOMPLY-028
J03,0,GEOCOMPLY-020;GEOCOMPLY-001
J04,?,
J05,2,GEOCOMPLY-025;GEOCOMPLY-026;GEOCOMPLY-029
J06,3,GEOCOMPLY-009;GEOCOMPLY-010;GEOCOMPLY-013
J07,2,GEOCOMPLY-017;GEOCOMPLY-018
J08,1,GEOCOMPLY-017
J09,2,GEOCOMPLY-028;GEOCOMPLY-027
J10,1,GEOCOMPLY-019;GEOCOMPLY-020;GEOCOMPLY-021
```

**Scoring notes (reasoned 0s, inferences, borderline calls):**

- **A01–A10 = 0 (inference, labeled)**: GeoComply's six-product suite is fully enumerated across its homepage, solutions page and official brochure (GEOCOMPLY-001); none touches promotion/sweepstakes administration, official rules, AMOE, drawings, fulfillment, or winner tax. "Promotion abuse" features are fraud detection (scored in E), not administration. Not scored 0 merely for non-mention — scored 0 because the full portfolio is positively enumerated and lies elsewhere.
- **F01–F10 = 0 (inference, labeled)**: same portfolio-enumeration basis; no wallet, ledger, credit, or entitlement functionality exists anywhere in the suite. Closest artifact (GCI chargeback evidence) is payments-dispute support, not a ledger.
- **B04 = 2**: allow/block + reason codes documented (official "troubleshooter" naming + third-party integration detail); a formal "review" output state is not evidenced.
- **B05 = 3**: reason codes are core, regulator-relevant behavior: official pages name the troubleshooter system, and operator help centers/third-party integration guides document code-driven handling. Combined evidence judged equivalently strong to official docs.
- **C10 = 0 (inference, labeled)**: the rules engine (28k conditions) is vendor-internal detection logic; the only exposed interfaces are SDK/decision API. No machine-readable policy library is offered; architecture and distribution model preclude it today.
- **H10 = 0 (inference, labeled)**: distribution is license-gated (no public packages, no public docs); no IaC surface exists to configure. 
- **I03 = 0 (inference, labeled)**: no marketing-facing product in the enumerated suite.
- **J02/J03 = 0 (inference, labeled)**: all rule changes are deployed by GeoComply internally as a managed service; no customer-facing policy-deployment pipeline exists to which a legal-approval step could attach. OneComply's approvals concern license filings, not rules.
- **I07/I08/I09 read as "degree present"**: professional-services dependency is high (managed tuning per market), switching cost is high (regulatory certifications, 13-year relationships) though demonstrably surmountable post-patent-invalidation (Radar/Xpoint wins), and integration burden is high for Core (multi-platform SDKs + certification), lower for IDComply/GeoGuard.
- **? squares**: B08 (rule priority), B09 (simulation), C05 (historical policy versions), C07 (impact analysis), C09 (legal provenance), D03 (policy-version linkage), G02/G03 (RBAC/SSO), G06 (policy testing), G08/H03 (webhooks), H05–H07 (versioning/idempotency/rate limits), H09 (config export), J04 (impact analysis) — all unresolved because integration documentation is auth-gated; these are plausibly present in some form internally but cannot be confirmed or denied from public sources.

## 13. White-space implications

**1. Which proposed Promotion OS capabilities are already solved?**
- **J06 (cross-vendor signal normalization) — for identity signals**: IDComply already normalizes multiple KYC/document/KBA/phone vendors behind one API, one contract, one price, with per-jurisdiction requirements applied (GEOCOMPLY-013). In gaming, the "signal orchestration" layer of Promotion OS is a solved, entrenched product.
- **Real-time jurisdiction-aware gating of a regulated action (the J05 kernel, for location/identity)**: every wager at >90% of US sportsbooks is already authorized in milliseconds against jurisdiction rules with reason codes (GEOCOMPLY-003, -007, -024).

**2. Which are partially solved?**
- **J01 (regulatory rules as executable product)**: jurisdiction rules ARE executable and in production — but as GeoComply's internal managed service, not as customer-authorable policy (GEOCOMPLY-027, -028).
- **J05**: authorization spans an operator's whole product line (sportsbook, casino, predictions) but only for the location/identity/fraud dimension — not arbitrary regulatory conditions (eligibility, promo terms, responsible-gaming rules) (GEOCOMPLY-025).
- **J07 (evidence-grade reconstruction)**: fact reconstruction (location/device/timestamps) is dispute-grade and bank-accepted via GCI; decision-logic reconstruction (rule version, approval chain) is absent (GEOCOMPLY-017, -018).
- **J09 (jurisdiction packs)**: functionally exists as vendor-managed per-market configuration (Ontario→Alberta "in hours, no code changes") but is not a reusable, customer-consumable policy-pack product (GEOCOMPLY-028).
- **J10**: OneComply is a lifecycle control plane for *licenses*, not for *policies* (GEOCOMPLY-019, -020).

**3. Which appear unsolved?**
- **J02 (legal-to-production deployment workflow)** and **J03 (counsel-as-approver)**: nothing customer-facing exists; rule deployment is a vendor black box.
- **J04 (regulatory impact analysis before rollout)**: no evidence in any product.
- **J08 (historical "why was this allowed?" replay)**: raw data exists but no replay-with-policy-version capability is exposed.
- All of section A (promotion administration) and F (ledger/entitlement provenance).

**4. Could this vendor add the missing capability easily?**
Partly. They own the hardest assets — jurisdiction rule expertise, regulator trust/licensure, signal collection at 2B tx/month, and the compliance buyer relationship. Exposing their internal rules as a versioned, simulatable, counsel-approvable policy product is a product/DNA pivot (from managed service to platform), not a data problem. OneComply proves appetite for compliance-workflow software. Countervailing: 2026 layoffs hit engineering/data science, the company is defending its core against Radar/Xpoint, and its whole pass-rate value proposition depends on *owning* rule tuning rather than handing customers a policy IDE. Verdict: capable but not naturally inclined; most plausible path is acquiring such a product, as with OneComply (GEOCOMPLY-021, -030).

**5. Could a customer assemble it using this vendor + internal engineering?**
Largely yes for the gaming vertical — and this is the strongest argument against the white space in that vertical: operators already receive jurisdiction-resolved allow/block + reason codes + KYC outcomes from GeoComply and wire them into internal eligibility/promo engines. What internal engineering still must build: the policy-authoring/versioning/approval layer, promo-specific legal rules, decision-log provenance joining GeoComply outputs to internal rule versions, and counsel workflow. Sophisticated operators (FanDuel/DraftKings scale) demonstrably do this today with in-house rules engines (GEOCOMPLY-007 third-party writeups describe exactly this pattern).

**6. What would make a customer buy a separate product instead?**
(a) Cross-vertical needs GeoComply doesn't serve (retail promotions, financial incentives, non-gaming sweepstakes) where no geolocation mandate exists; (b) need for **auditable policy provenance** — regulators asking "show me the rule version and who approved it," which GeoComply cannot answer for customers today; (c) desire to keep counsel-controlled rules in-house rather than outsourced to a vendor's black box; (d) multi-vendor strategy post-patent-invalidation — normalizing GeoComply/Xpoint/Radar/Socure signals behind one policy layer (Promotion OS's J06 generalized) is attractive precisely because GeoComply's normalization stops at its own and its KYC partners' signals; (e) price pressure on per-check fees.

## 14. Replacement risk

**HIGH.**

If a "regulatory action authorization + policy lifecycle" product proved valuable in regulated gaming, GeoComply is the best-positioned incumbent on earth to ship it: it already sits in the transaction path of >90% of the US market, already encodes jurisdiction rules, already holds supplier licenses and regulator/court legitimacy, already orchestrates third-party KYC vendors, and has shown it will acquire workflow software (OneComply) to round out "compliance under one roof." Its Brazil/Alberta "one endpoint" packaging is explicitly converging toward a unified compliance platform. Two mitigating factors keep this short of EXTREME: (1) its model is managed-service, not customer-programmable policy — exposing a policy control plane would partially cannibalize its tuning moat and is absent from any observed roadmap signal; (2) 2026 retrenchment (18% layoffs, engineering included) and a two-front defense against Radar/Xpoint constrain new-category investment. Outside gaming-style location-mandated verticals, its ability to follow drops sharply.

## 15. Adjacent discoveries

At least 2 required; 5 identified:

1. **Xpoint (xpoint.tech)** — direct geolocation-compliance competitor that defeated GeoComply's patent (invalidated 2023, affirmed 2024), legally opening the category; proves the signal layer is contestable and that a neutral policy layer above multiple geo vendors is plausible. [GEOCOMPLY-031]
2. **Radar (radar.com)** — developer-first geofencing platform that launched a gaming geo-compliance/fraud product with MTU pricing and self-serve DX, explicitly targeting GeoComply's pricing and closed model; customers Sleeper, Fliff, Everi. Represents the "modern developer platform" attack vector the white-space product would also ride. [GEOCOMPLY-032]
3. **LocationSmart** — carrier/IP-based location verification used in gaming; a lower-assurance substitute for some check types (named alongside GeoComply/Xpoint in industry comparisons). [GEOCOMPLY-030 coverage context]
4. **Vixio (GamblingCompliance / Regulatory Intelligence)** — regulatory-change monitoring and obligation intelligence for gambling/payments; the content/monitoring half (C06/J04) that GeoComply performs only as internal service; a natural complement or acquisition target in any policy-lifecycle play.
5. **Trulioo / Alloy (KYC orchestration platforms)** — horizontal identity-orchestration platforms with customer-configurable waterfalls and case management; substitutes for IDComply outside gaming and evidence that J06-style normalization is already a competitive product category beyond this vertical.

(Socure and Persona, also adjacent, are already assigned as companies 10–11.)

## 16. Evidence ledger

Full machine-readable ledger: `outputs/evidence/09_geocomply.jsonl` (36 records). Summary table:

| Claim ID | Claim | URL | Source type | Access date | Confidence |
|---|---|---|---|---|---|
| GEOCOMPLY-001 | Suite = Core, IDComply, PinPoint, GeoGuard, GCI, OneComply; "compliance, KYC, growth and anti-fraud under one roof"; no promo/ledger/marketing products | https://www.geocomply.com/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-002 | 2B+ transactions/month; 200M+ users; 99.9999% uptime (marketing) | https://www.geocomply.com/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-003 | Core: GPS/WiFi/cellular/IP device-level location; SDKs desktop/mobile/web; milliseconds; 1.2B checks/mo; dashboards; troubleshooter messages | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/geocomply-core/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-004 | 350+ checks/transaction: device integrity, spoofing, location jumping, proxy betting, account sharing | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/geocomply-core/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-005 | Vendor rules engine: new rule ~18h, ~28k conditions, ML models; milliseconds | https://www.geocomply.com/technology/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-006 | Customizable autoblock rules per risk tolerance; multi-user/bonus-hunter reports; high-risk location dashboard | https://www.geocomply.com/geocomply-fraud-solutions/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-007 | Integration: SDK collects encrypted payload; server API returns state code, allow/block, reason codes (troubleshooter); license tokens; per-env keys | https://tech-insider.org/igt-how-to-set-up-geocomply-gambling-geolocation-in-product-en-d176/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-008 | SDKs: iOS16+/Android10+/Win10+/macOS12+/browser PLC (local WebSocket); license-gated distribution; ~4 public GitHub repos | https://tech-insider.org/igt-how-to-set-up-geocomply-gambling-geolocation-in-product-en-d188/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-009 | IDComply: KYC/AML — data, doc+selfie, KBA, phone/email; PEP/OFAC/HIO/sanctions/criminal screening | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/idcomply/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-010 | IDComply waterfall + per-jurisdiction compliance engine; customizable fields per jurisdiction rules; tracks KYC reg changes | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/idcomply/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-011 | IDComply licensed by NJ DGE; KBA/digital-ID secondary auth; single back-office and API with geolocation | https://www.geocomply.com/news/geocomplys-idcomply-solution-for-kyc-licensed-in-new-jersey/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-012 | IDComply pass rates: up to 95% (46 US states, 2023), ~90% Ontario; single API call | https://www.geocomply.com/resources/brochures/idcomply/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-013 | IDComply: one price, no integration/licensing fees, no minimums; GeoComply handles vendor procurement; anonymized Player IDs | https://www.geocomply.com/wp-content/uploads/GeoComply-for-global-gaming-industry.pdf | official-doc | 2026-08-18 | HIGH |
| GEOCOMPLY-014 | GeoGuard: 310M+ IP DB, hourly updates, 98% accuracy; VPN/proxy/Tor/hijacked-residential/smart-DNS; cloud/on-prem/CDN edge; rules engine + ML | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/geoguard/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-015 | GeoGuard turn-on via CloudFront/AWS Marketplace; MultiChoice case study | https://aws.amazon.com/blogs/media/blocking-illegal-viewers-from-streaming-services/ | case-study | 2026-08-18 | MEDIUM |
| GEOCOMPLY-016 | PinPoint: beacon geofencing, ~1m accuracy, on-property compliance | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-017 | GCI: evidence reports ≤60s; 6mo–2yr location history; accepted by 70+ processors; Visa CE3.0; bulk case processing | https://www.geocomply.com/anti-fraud-and-geolocation-solutions/geocomply-chargeback-integrator/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-018 | Precise timestamps of activity/location "robust enough to win disputes from banks"; Sightline: fraud costs cut ≥85% | https://www.geocomply.com/wp-content/uploads/GeoComply-for-global-gaming-industry.pdf | case-study | 2026-08-18 | MEDIUM |
| GEOCOMPLY-019 | OneComply: single data source → multi-jurisdiction applications (USA/Canada); OmniFill; 97% redundancy reduction | https://onecomply.com/solutions/license-application-and-management/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-020 | OneComply License Control: tracking, alerts, material-change tasks with lead times, audit reporting, regulator file sharing; regulators use it | https://onecomply.com/solutions/license-control/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-021 | GeoComply acquired OneComply (first M&A); rationale: AML+KYC+licensing+geolocation+sanctions+fraud coverage | https://www.geocomply.com/news/geocomply-acquires-leading-licensing-and-compliance-platform-provider-onecomply/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-022 | SOC 2 maintained; trust.geocomply.com portal; report under NDA | https://www.geocomply.com/trust-center/security/ | official-doc | 2026-08-18 | HIGH |
| GEOCOMPLY-023 | FinServ: OFAC sanctioned-jurisdiction geofencing; AML location patterns; Dabble, Luno, Betr | https://www.geocomply.com/industries/financial-services/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-024 | >90% of US sports-betting market are clients (WSJ 2023); FanDuel/DraftKings/BetMGM/Amazon/BBC/Premier League | https://www.sportico.com/business/sports-betting/2026/geocomply-layoffs-employees-geolocation-1234890545/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-025 | 2026 renewals: FanDuel (all products incl. Predicts, 13-yr), DraftKings super app, Caesars all markets, Hard Rock all-in-one | https://sbcamericas.com/2026/08/17/fanduel-geocomply-multiyear-renewal/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-026 | WA court ordered Kalshi to deploy "GeoComply multi-source geofencing" by Sept 2 | https://thecurrencyanalytics.com/regulations/washington-court-shuts-kalshi-out-of-prediction-markets-across-key-contract-categories-284415 | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-027 | Brazil unified identity platform (Mar 2026): KYC+fraud+geo, one endpoint; 99.7% pass; 99.999% uptime; 30+ jurisdictions "custom-built, locally tuned" | https://www.businesswire.com/news/home/20260303195897/en/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-028 | Alberta: BrowserGuard adaptive silent geo; GeoValidator; ML ~18h updates; 15k checks/sec; Ontario→Alberta in hours no code changes; Gov Relations team; "$0 fines" | https://www.geocomply.com/alberta-igaming/ | official-marketing | 2026-08-18 | MEDIUM |
| GEOCOMPLY-029 | Missouri: 2.6M checks in 24h at launch; MO Gaming Commission supplier license | https://www.geocomply.com/news/the-show-me-state-shows-up-for-legal-sports-betting/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-030 | Apr 2026 layoffs: ~80 (~18% of 450+), eng/data science included; AI, regulation, competition (Xpoint, Radar), lost patent suit | https://thelogic.co/news/geocomply-layoffs/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-031 | Geolocation Engine patent invalidated (DE 2023; Fed. Cir. affirmed Nov 2024) in GeoComply v. Xpoint | https://www.casino.org/news/geocomply-loses-patent-infringement-case-vs-xpoint/ | third-party | 2026-08-18 | HIGH |
| GEOCOMPLY-032 | Radar launched geo-compliance/fraud vs GeoComply; MTU pricing; Sleeper, Fliff, Everi; 3 state licenses (2024) | https://radar.com/blog/introducing-fraud-detection-geo-compliance-solution | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-033 | Founded 2011, Vancouver; 9B+ tx/yr, 400M+ devices (2023); Sainsbury chairman, Levin CEO; Blackstone/Atairos minority investors | https://www.geocomply.com/about-us/ | official-marketing | 2026-08-18 | HIGH |
| GEOCOMPLY-034 | Core pricing not public (contact vendor) | https://www.capterra.com/p/236941/Geocomply-Core/ | third-party | 2026-08-18 | MEDIUM |
| GEOCOMPLY-035 | RiskGuard 24/7 ML anomaly detection; custom fraud tags; industry-shared fraud DB; auto-block across jurisdictions | https://www.geocomply.com/wp-content/uploads/GeoComply-for-global-gaming-industry.pdf | official-doc | 2026-08-18 | MEDIUM |
| GEOCOMPLY-036 | No GeoComply product named "Chameleon"; term traces to SBTech Chameleon360 partner platform (2018) | https://www.geocomply.com/news/sbtech-geocomply-integration/ | third-party | 2026-08-18 | MEDIUM |

## 17. Verdict

**MAJOR OVERLAP**

GeoComply is not a policy-management platform, but in regulated gaming it already performs the run-time heart of the Promotion OS hypothesis: jurisdiction-aware, millisecond authorization of regulated actions (J05, location/identity scope), cross-vendor identity-signal normalization behind one API (J06), vendor-maintained executable jurisdiction rules (J01, as managed service), evidence-grade factual reconstruction sold as a product (J07, facts only), and config-only jurisdiction expansion (J09, vendor-managed) — plus licensing-lifecycle workflow via OneComply. What it does not offer anywhere: customer-authorable policy, versioning, simulation, impact analysis, counsel approval, or decision-to-policy-version provenance (J02–J04, J08, and the policy half of J07/J10), and nothing in promotions (A) or ledgers (F). Any policy-control-plane pitch to regulated-gaming buyers lands on budget GeoComply already owns, and GeoComply is the likeliest acquirer/fast-follower in that vertical — hence major overlap rather than complement.
