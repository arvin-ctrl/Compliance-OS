# Master Capability Matrix

Every company must be scored on the same squares.

Allowed scores:
- 0 = no evidence / not offered
- 1 = minimal / manual / peripheral
- 2 = meaningful but incomplete
- 3 = strong capability
- 4 = category-leading / core product
- ? = unresolved

Never use 0 merely because the website did not mention a feature.

## A. Promotion administration

A01 Sweepstakes creation
A02 Contest creation
A03 Instant-win mechanics
A04 Official rules generation
A05 Rules review / legal administration
A06 AMOE workflow
A07 Entry management
A08 Winner selection / certified drawings
A09 Prize fulfillment
A10 Tax reporting / winner tax workflows

## B. Real-time decisioning

B01 Event/action API
B02 Rules evaluated synchronously
B03 Low-latency production decisioning
B04 Allow / deny / review output model
B05 Reason codes
B06 Custom attributes / merchant data
B07 Stateful user/customer context
B08 Rule priority / conflict resolution
B09 Simulation / dry-run
B10 Decision replay

## C. Regulatory / jurisdiction intelligence

C01 Jurisdiction-specific rules
C02 Product-type-specific rules
C03 Action-specific legal rules
C04 Effective dates / temporal rules
C05 Historical policy versions
C06 Regulatory change monitoring
C07 Impact analysis before policy rollout
C08 Counsel approval workflow
C09 Legal-source provenance
C10 Machine-readable legal policy library

## D. Evidence / auditability

D01 Immutable decision ID
D02 Decision log
D03 Policy version linked to decision
D04 Input facts linked to decision
D05 Human approval history
D06 Reconstruct past decision
D07 Evidence export / regulator package
D08 Retention controls
D09 Tamper-evidence / integrity features
D10 Enterprise audit tooling

## E. Identity / location / risk

E01 Identity verification
E02 Age verification
E03 Address verification
E04 Geolocation
E05 Device intelligence
E06 VPN / spoofing detection
E07 Fraud scoring
E08 Duplicate-account detection
E09 Case management
E10 Third-party signal orchestration

## F. Ledger / entitlement provenance

F01 Wallet / balance support
F02 Ledger events
F03 Reward provenance
F04 Promotion-linked credits
F05 Expiration rules
F06 Restricted vs unrestricted value
F07 Redemption eligibility
F08 Balance reconstruction
F09 Multi-asset support
F10 External ledger integration

## G. Enterprise governance

G01 Multi-tenant / multi-brand
G02 RBAC
G03 SSO / SAML
G04 Approval workflows
G05 Environments / staging
G06 Policy testing
G07 Change management
G08 Webhooks
G09 Enterprise SLA
G10 SOC 2 / relevant security posture

## H. Developer platform

H01 Public API
H02 SDKs
H03 Webhooks
H04 Sandbox
H05 API versioning
H06 Idempotency
H07 Rate limits documented
H08 Observability / request logs
H09 Policy/config export
H10 Infrastructure-as-code support

## I. Buyer / commercial fit

I01 Legal/compliance buyer
I02 Engineering/platform buyer
I03 Marketing buyer
I04 Fraud/risk buyer
I05 Enterprise customers
I06 Self-serve motion
I07 Professional services dependency
I08 Switching cost
I09 Integration burden
I10 Pricing transparency

## J. Proposed differentiators

J01 Regulatory rules as executable product
J02 Legal-to-production deployment workflow
J03 Counsel-as-approver model
J04 Regulatory impact analysis
J05 Cross-product action authorization
J06 Cross-vendor signal normalization
J07 Evidence-grade decision reconstruction
J08 Historical "why was this allowed?" replay
J09 Policy network / reusable domain packs
J10 Regulatory policy lifecycle control plane

## Required output

Managers create `outputs/final/master_capability_matrix.csv`.

Every non-? score must trace to at least one evidence record.
