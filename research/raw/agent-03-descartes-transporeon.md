# Agent 03 — Descartes + Transporeon

**Research date:** 2026-08-19

## Q1 — Appointment vs actual arrival
Both expose the two halves; **neither closes the loop into money.**

**Descartes MacroPoint** Create Order API takes per-stop appointment windows (`StartDateTime`/`EndDateTime`; flat-file `Appointment Begin/End Date/Time`). Trip Events callback returns FTL event codes **X3 Arrived-Pickup, AF Departed-Pickup, X1 Arrived-DropOff, D1 Departed-DropOff** with `EventDateTime` (ISO8601 UTC) and `UpdatedBy` (Customer/Carrier/Driver/MacroPoint-geofence). Schedule Alerts carries `ScheduledStartTimeInLocalTimeForStop` and alert code **4 = "Past Appointment Time"**. Arrival-minus-appointment is fully computable — **by you, not by Descartes.**

**The 4.6 MB MacroPoint API doc contains ZERO occurrences of "detention", "dwell", "accessorial", "demurrage" or "lumper."** (VERIFIED)

**Transporeon** Booking DTO gives `from_timestamp`/`until_timestamp`/`gate`/`location`/`timezone`; Process Status gives `status.loading.arrival`, `status.loading.departure`, `status.unloading.arrival`, `status.unloading.departure` with `declared_timestamp`, lat/long, `trigger` (GPS|EVENT), `source`. Real-Time Yard Management's "Arrival Monitor" is ETA-based, operational, not billable.

The one downstream billing path is Transporeon **Surcharge Management** — and it is manual: *"Carrier has the possibility to request surcharges… Typical examples are surcharges for waiting times… Shipper can accept or decline… The set of possible surcharge requests (type, amount and timeframe) is defined by Shipper."* **The Surcharge DTO has `price` as a single FLOAT — no hours, no rate, no quantity.** Accept Surcharge lets the shipper unilaterally amend the price down. Freight Audit adds a killer clause: *"Surcharges cannot be added to the transport after an agreed cut-off time past the delivery of the transport."* (VERIFIED)

## Q2 — Whose side is Transporeon's audit on?
**Unambiguously the shipper's payables.** FASS *"prevents [overbilling] at the source. Carriers are guided to create invoices within the shipper's enforced billing rules."* Managed Freight Audit is self-billing: *"Service Provider creates a billing instruction for Carriers."* Markets "9% savings on logistics expenditures" and "Say goodbye to manual freight audits and overpayments."

**No under-billing detection anywhere.** The carrier's only levers are a manual Surcharge request or a Dispute, both shipper-adjudicated. Scope is also narrow: FASS is *"limited to road transports managed through Transport Assignment only"*, and *"Only transports executed via Platform are eligible."*

## Q3 — Automatic detention entitlement against a contract?
**Neither. No.** Descartes' closest is a configurable threshold: *"a broker can set a custom amount of time indicating 'free time'. This will be the trigger for the detention period to start"*, producing *"customizable detention alerts and reports"* so *"brokers can be proactive and bill their shippers earlier."* **That is an alert, not an entitlement calculation, not an invoice.** Transporeon has no computation at all — a human types a number.

## Capability scores

| Capability | Descartes | Transporeon |
|---|:--:|:--:|
| rate_confirmation_ingestion | 1 | 1 |
| rate_rule_extraction | **0** | **0** |
| gps_eld_timestamps | 2 | 2 |
| appointment_ingestion | 2 | 2 |
| pod_bol_ingestion | 2 | 2 |
| detention | 1 | 1 |
| tonu / layover / lumper | 0 | 0 |
| demurrage | 1 | 1 |
| accessorial_detection | 1 | **0** |
| evidence_package | 1 | 1 |
| invoice_creation | 2 | 2 |
| claim_submission | 0 | 2 |
| collection_tracking | 1 | 1 |
| dispute_workflow | 1 | 2 |
| portal | 2 | 2 |
| tms_integration | 2 | 2 |
| eld_integration | 2 | 2 |
| email_sms_ingestion | 1 | 1 |
| accounting_integration | 1 | 2 |
| recovered_revenue_analytics | **0** | **0** |
| performance_pricing | **0** | **0** |
| customer_specific_rules | 1 | 2 |
| multi_carrier_shipper_support | 2 | 2 |

## API/data access reality for a third party

**Descartes — the practical back door.** MacroPoint is Basic Auth over `https://macropoint-lite.com/api/1.0/`, XML. Access requires an MPID under a customer contract. But callbacks are *"Endpoint established by Customer"* and **`PostOverrideMPID`** exists: *"Second MPID utilized to return tracking data. Typically used to return data to separated endpoints for specific shipments."*

**A broker can point MacroPoint arrival/departure/appointment callbacks at a startup's URL without Descartes brokering the deal.** Carriers pay nothing (*"we do not charge for any of our carrier integration methods"*), so the data cost sits with the broker who already pays. **This is a low-barrier wedge.** (VERIFIED)

**Transporeon — front door narrow, third-party door deliberately blunted.** The **Open Visibility API** (`https://api.sixfold.com/v1/open-visibility/shipments`, Bearer key scoped to a "beforehand agreed filter") returns stop `status` values `at_stop`/`departed` — **but no arrival or departure timestamps.** Only `eta`, `eta_checked_at`, `latest_position.timestamp`. And `status` is "missing by default." **You cannot compute detention from Transporeon's third-party API.**

The **Appointment Scheduling API is Beta**, inside the Transporeon Integrated App Program (TIAP), OAuth2 against `id.eu.trimble-transportation.com`, and states: *"Access to the Appointment API endpoints is restricted, and authorization requires contacting the Trimble team to obtain credentials"* — plus *"We are no longer accepting volunteers."* Real timestamps live in per-project Shipper Standard Interfaces. Worse for data hygiene: *"Dispatch status timestamps are defined as local timestamps… please omit the timezone."* **Barrier: HIGH — partner-program gate plus a paid Transporeon customer sponsor.**

## Europe vs North America
The products faithfully encode the regional norm difference. **NA:** detention is a contractual $/hr after free time; the broker is the recovery agent. Descartes matches: configurable free time → detention alert → *"bill their shippers earlier."* **Europe:** no free-time-clock convention for road; waiting time is a negotiated *surcharge* (Standgeld-style) requested after the fact and shipper-approved. Transporeon matches: shipper-defined surcharge types, shipper-set amounts, hard cut-off. TSM markets *avoidance* — "up to a 40% reduction of waiting times."

**Consequence: a recovery product must be two products — a US clock-and-invoice engine, and an EU evidence-and-negotiation engine that beats the cut-off window.**

## Honest gaps
1. **The calculation itself.** Neither converts (appointment, arrival, departure, contract terms) into an entitled amount. Descartes stops at an alert; Transporeon starts at a human-entered FLOAT.
2. **Rate-rule extraction.** Neither reads free time, hourly rate, cap, or notice window out of a rate con. Manual per-lane/per-customer config.
3. **Everything that isn't detention.** TONU, layover, lumper, redelivery, reconsignment, shortage/damage: **0 across both.** That is the majority of leaked accessorial dollars and it is genuinely uncovered.
4. **Under-billing detection.** Transporeon is architecturally shipper-side; a self-billing platform that generates the billing instruction has no incentive to find money the shipper owes. **Structural, not a roadmap gap.**
5. **Claim packaging and collections.** No evidence assembly, no aging/dunning, no recovered-revenue analytics, no contingency pricing.
6. **Scope exclusion.** FASS covers only platform-executed transports. **Off-platform, spot, and subcontracted freight — where accessorials concentrate — is out of scope by contract.**
7. **The cut-off clause.** Transporeon shippers can extinguish late surcharge claims. A third party that files inside the window has a defensible, quantifiable value prop.

## Threat level
**Descartes: MEDIUM-LOW as competitor, HIGH as data channel.** They own the arrival/departure timestamp and appointment window in NA brokerage, and Aljex owns the invoice. If Descartes wires "free time exceeded" → Aljex accessorial line → invoice, the wedge narrows fast — all pieces in-house, an obvious roadmap item. Mitigating: the detention feature has sat as "alerts and reports" since ~2018 with no visible progression, and their freight audit investment went to **ocean**. `PostOverrideMPID` plus customer-defined callbacks means **you can partner around them today without their permission.**

**Transporeon: LOW as competitor, HIGH as gatekeeper.** Will not build carrier-side under-billing recovery — directly adverse to the shipper who signs the MSA. But controls EU dock data, deliberately shipped a third-party visibility API *without arrival/departure timestamps*, and gated the Appointment API behind a closed partner program.

**Net: the white space is real and structural (calculation, rule extraction, non-detention accessorials, carrier-side advocacy), but the moat is data access — much thinner in North America than in Europe.**

## Caveats
No public pricing for either (UNKNOWN in dollars). "Transporeon Autonomous Dock Scheduling" could not be confirmed as a named product. Nexogen could not be verified as a Transporeon/Trimble asset. The Descartes Dock Appointment Scheduling PDF carries a 2011 copyright, so those specifics may be dated. Search budget exhausted.

## Sources
docs.macropoint.com · carrierdocs.macropoint.com · descartes.com/resources/knowledge-center/new-capabilities-descartes-macropoint-solution-help-improve-your · macropoint.com/features/dock-appointment-scheduling/ · /faqs/ · /news/demurrage-detention/ · descartes.com/content/documents/pi_dock_appointment_scheduling_0.pdf · aljex.com/features/accounting/ · descartes.com/documents/descartes-rate-builder-ocean-freight-auditing-software · transporeon.com/website/Legal/msd/5.0/EN_Modules_and_Services_description_V5.0.pdf · transporeon-hcskb.atlassian.net/wiki/spaces/ADPD (API Reference, Open Visibility Data, Appointment Scheduling Beta, Freight Audit data, Booking/Dispatch Status/Process Status/Surcharge DTOs) · transporeon.com/en/platform/freight-audit-payment-hub/freight-audit/selfservice · /en/platform/dock-yard-management-hub/shipper/time-slot-management
