# Agent 04 — ELD / Telematics (Samsara, Motive)

**Research date:** 2026-08-19

**Headline: they produce the *timestamp*, never the *claim*.** Neither is a competitor; both are **data suppliers with restrictive terms**.

## Native detention capability

**Samsara — report only, no billable claim (VERIFIED).** Ships a **Detention Report** and a **Time on Site Report**. The Detention Report is **trailer-scoped and only visible if you have at least one AG-tracked trailer** — it does not work off tractor GPS alone. Aggregates detention hours by location/trailer with "Average Time Per Visit" in two-hour buckets. Samsara's launch post frames output as leverage, not money: *"When you have detention data you can rely on, you can have more frank and transparent conversations with customers."* No free-time subtraction, no per-customer rate, no dollar amount, no claim object, no invoice. **There is no detention or dwell endpoint anywhere in the Samsara API — the report is dashboard-only and not API-addressable.**

**Motive — dwell duration in the API, no claim (VERIFIED).** No standalone Detention Report product. What exists: (a) geofence events carrying a computed dwell `duration`, (b) **Facility Insights** (Enterprise tier, CLAIMED) showing average dwell across 80,000+ facilities.

## API access reality

### Samsara
| Need | Endpoint / event |
|---|---|
| GPS breadcrumbs | `GET /fleet/vehicles/stats?types=gps`, `/stats/feed` (poll 5–30s), `/stats/history`, `GET /beta/fleet/trailers/stats` |
| **Geofence arrival/departure** | `GET /assets/location-and-speed/stream?includeReverseGeo=true&includeGeofenceLookup=true` — location joined to geofence, **the single most useful endpoint here**. Webhooks `GeofenceEntry`/`GeofenceExit` (**both Beta**), `RouteStopArrival`/`RouteStopDeparture` |
| HOS/duty | `GET /fleet/hos/clocks`, `/logs`, `/daily-logs` |
| Vehicle↔load | `GET/POST/PATCH /fleet/routes` with `scheduledArrivalTime`/`scheduledDepartureTime` + actual per stop |

The `GeofenceEntry` payload includes `address.geofence.circle.radiusMeters`, polygon `vertices`, `address.externalIds`, `vehicle.vin` — **a third party can read the actual geofence geometry used, which matters for defending a claim.**

**Two documented Samsara modelling gaps that hurt:** *"Samsara doesn't have a first-class 'order' entity"* — order/PO/load data must be stuffed into a stop's `notes`. And *"Samsara doesn't have an explicit delivery window concept."* Load↔stop identity is fragile unless the carrier's TMS already writes routes into Samsara.

**Auth:** Bearer token with granular scopes, or **OAuth 2.0** ("recommended for all Marketplace apps"). Access token 1 hour, auth code 10 min, refresh tokens single-use. **OAuth scopes are coarse — only `admin:read` and `admin:write`.** App registration self-serve in Settings > OAuth 2.0 Apps; no partner approval to build.

**Rate limits (VERIFIED):** 150 req/s per token, 200 req/s per org. Level One 100 req/min, Level Two 5 req/s, Level Three 10 req/s. 429 + `Retry-After`. Kafka connector for high volume.

**Cost: none documented. Legal is the real cost.** Integration Partner Terms **§3.1**: partner *"shall not sell, license, sublicense, or otherwise transfer or disclose any Customer Data obtained through Samsara's Products, API or platform to any third party without explicit consent and written notice to Samsara."* **A detention product transmits carrier telematics to a broker/shipper — a third party.** §4.6(d) separately bars using Samsara IP *"to create products or services that compete with Samsara's."*

### Motive
| Need | Endpoint |
|---|---|
| GPS | `GET /v1/vehicle_locations` (+v2, v3 — v3 requires Motive Vehicle Gateway) |
| **Geofence arrival/departure** | **`GET /v1/geofences/events`** — params `start_date`, `end_date`, `geofence_ids[]`, `driver_ids[]`, `vehicle_ids[]`, `updated_after`. Response: `start_time`, `end_time`, **`duration` (seconds)**, `vehicle{}`, **`start_driver{}`, `end_driver{}`** |
| HOS | HOS list/violations/logs v1,v2; webhook `user_duty_status_updated` |
| Vehicle↔load | **`GET /v3/dispatches`** — `dispatch_trips[]` (`driver_id`, `vehicle_id`, `co_drivers[]`); `dispatch_stops[]` with **`early_date`/`late_date` (a real appointment window)** |

**`GET /v1/geofences/events` is materially better than anything Samsara exposes** — a pre-computed entry/exit pair with dwell seconds, driver at entry *and* exit (**drop-and-hook detection**), filterable by geofence and date. Webhooks v2 add `vehicle_geofence_event`/`asset_geofence_event`. No dispatch stop arrival/departure webhook documented — must poll `/v3/dispatches`.

**Auth:** OAuth 2.0 with genuinely granular scopes — `geofence_events.read`, `locations.vehicle_locations_list`, `hos_logs.hours_of_service`, `dispatches.read`, `documents.read`. Far better least-privilege story than Samsara.

**Rate limits: UNKNOWN — genuinely undocumented.** The Response Codes page lists 200/201/400/401/403/404/500 and **does not include 429**. API ToS instead says Motive *"may limit the number of transactions… at any time in its sole discretion."* Unbounded operational risk.

**Legal — worse than Samsara's.** API ToS requires *"Motive's prior written authorization and consent (which may be withheld in Motive's sole discretion)"* before distributing an app commercially, bars publishing/selling User Data to third parties, and prohibits use *"to create a substitute for or substantially similar product… or any other use cases which Motive deems outside of the scope."* **That last clause is unilateral and open-ended.**

## Timestamp accuracy reality

- Samsara VG GPS: *accurate within a few meters in most conditions* (VERIFIED).
- **Cell-based approximate location for Asset Gateways carries a 0.1–1.5 mile error radius** — fatal for a yard-vs-dock distinction on trailer-based detention, which is exactly what the Detention Report runs on.
- Geofence geometry is **user-drawn**, box/circle/freehand, "as small as a subsection of a parking lot or as large as an entire state." **No documented minimum radius, no documented dwell debounce, no hysteresis** on either platform — UNKNOWN.
- **Documented drop-and-hook problem (Samsara, verbatim):** for multiple orders at one location, *"Arrival and departure to and from the location's geofence trigger only once so all orders will have the same En Route, ETA, Arrival, and Departure times."* Workaround requires **the driver to manually arrive/depart each stop** — reintroducing exactly the human error a detention product exists to remove. Also *"Route arrive/depart webhook events are only sent for vehicle assigned routes."*
- Motive's `start_driver`/`end_driver` split is the one genuine drop-and-hook advantage across both.

**Practical implication: the product must re-derive detention from raw breadcrumbs against its own geofence with its own debounce, and treat vendor geofence events as corroboration, not truth.**

## Capability scores

| Capability | Samsara | Motive |
|---|:--:|:--:|
| rate_confirmation_ingestion | 0 | 0 |
| rate_rule_extraction | 0 | 0 |
| gps_eld_timestamps | **2** | **2** |
| appointment_ingestion | 1 | **2** |
| pod_bol_ingestion | 1 | 1 |
| detention | 1 | 1 |
| tonu / layover / lumper / demurrage | 0 | 0 |
| accessorial_detection | 0 | 0 |
| evidence_package | 1 | 1 |
| invoice_creation | 0 | 0 |
| claim_submission | 0 | 0 |
| collection_tracking | 0 | 0 |
| dispute_workflow | 0 | 0 |
| portal | 1 | 1 |
| tms_integration | **2** | **2** |
| eld_integration | **2** | **2** |
| email_sms_ingestion | 0 | 0 |
| accounting_integration | 0 | 0 |
| recovered_revenue_analytics | 0 | 0 |
| performance_pricing | 0 | 0 |
| customer_specific_rules | 0 | 0 |
| multi_carrier_shipper_support | 0 | 1 |
| **Total** | **11** | **15** |

## Marketplace path for a solo founder

**Motive is dramatically easier to *build* on. Samsara is easier to *list* on.**

**Motive (VERIFIED):** fully self-serve — sign up at developer.gomotive.com, accept Developer ToS, +Create App, immediately get **Client ID and Client Secret**. Sandbox = your own dummy fleet. **Zero gatekeeping, zero fee, same-day.** But *publishing* requires the partner application (company registration, type, technical/security/business detail, review) — **timeline and fees not published (UNKNOWN)** — and the ToS's "prior written authorization" clause gates commercial distribution even if you never list.

**Samsara (VERIFIED):** Technology Partner Program application — **company email required** (*"non-personal emails may result in denial"* — a real solo-founder trap), revenue field optional and "$0" acceptable, reviewed weekly, 5–7 business day response. Portal invite link **expires in 24 hours**. App lifecycle Draft → Beta → Ready for Review → Public.

**Critical friction: "Apps are reviewed on a quarterly basis."** **Workaround a solo founder should use: stay in Beta** — Beta apps install via direct install URLs or beta codes, so paying design partners onboard without waiting a quarter. EU and Canada require **separate developer portals and separate listings**. No fees documented on either.

## Strategic threat

**Motive: HIGH on detection, LOW on billing.** At **Vision 26** Motive shipped **Atlas** (*"It doesn't just surface insights. Rather, it takes action on your behalf"*) and an **Automations** engine (*"Teams define the conditions and actions once, then AI takes the actions for you"*). Cited triggers: pre-HOS-violation alerts, threshold-based training, camera disabling. **Detention, dwell, accessorial, billing and invoicing receive no mention.** But Automations + `geofence_events` is precisely the primitive for "dwell > 2h → notify". Motive has no A/R, no broker relationships, no claim object.

**Samsara: MODERATE, and the tell is warranty.** May 2026 releases included **AI-powered warranty management with a Claims Center** where *"teams can track statuses, reimbursement amounts."* **That is a working template for detect → evidence → claim → track reimbursement, already shipped, just pointed at OEM warranty instead of shipper detention.** Samsara has the AG trailer hardware, door/cargo sensors, and a Detention Report un-monetised since launch. If they choose to, the pivot is short.

**Read:** neither ships auto-detention *billing* in 12 months — both lack the broker-side relationship, rate-confirmation ingest, and collections motion. **The durable moat is not the timestamp (they own it and will keep improving it) but rate-con parsing → contractual free-time rules → evidence packet → broker submission → collections.** Build geofence/debounce logic from raw breadcrumbs; treat Samsara/Motive as interchangeable feeds; **integrate at least a third (Geotab/ELD-agnostic) so no single ToS clause can end the company.**

## Two legal risks to flag, in priority order
1. **Motive's ToS clause prohibiting anything *"Motive deems outside of the scope"* is unilateral and could be invoked at any time.**
2. **Samsara §3.1's bar on transferring Customer Data to third parties without written notice to Samsara may be triggered by the core act of sending a detention claim to a broker.**

Both warrant counsel before signing a design partner.

## Pricing (CLAIMED, third-party only — neither publishes)
Samsara ~$27–33/vehicle/mo on 3-yr, hardware $99–148. Motive Starter $25 / Pro $40 / Enterprise $50 per vehicle/mo, hardware ~$150, 1–3 yr terms.

## Sources
developers.samsara.com/docs/{rate-limits,rest-api-overview,oauth-20,tms-integration,tms-gps-tracking,tms-compliance,routing-guide,creating-routes-via-api,geofenceentry,geofenceexit,marketplace-apps,application-process,integration-partner-terms} · kb.samsara.com/hc/en-us/articles/360042870072-Detention-Report · /360043256251-Time-on-Site-Report · /40045080679821-GPS-Data-Accuracy-in-Vehicle-Gateways-VGs · samsara.com/blog/introducing-detention-reports · /blog/may-product-updates-2026 · developer-docs.gomotive.com/reference/{fetch-a-list-of-all-the-geofence-events,webhooks-v2,fetch-all-the-company-dispatch-records-v3} · /docs/{oauth-scopes,prerequisites,response-codes} · gomotive.com/legal/api-terms-of-service/ · /blog/announced-at-vision-26-motive-ai-innovation/ · /blog/detention-time-cost-safety-data/
