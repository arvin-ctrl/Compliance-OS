# Agent 15 — Legal & contract: entitlement and evidence

**Research date:** 2026-08-19
**Scope note:** session WebSearch budget was exhausted by earlier agents; all findings come from direct fetches of primary documents (contracts, statutes, Federal Register, state codes). **Every quoted clause was read in full text.**

## What governs entitlement

**VERIFIED — the hierarchy is: Broker-Carrier Agreement (BCA) > Rate Confirmation > Bill of Lading.** All four real agreements pulled make the BCA supreme, make the rate con an addendum, and expressly subordinate the BOL.

**TQL rate confirmation (PO# 18507867), actual text:**
> *"THIS AGREEMENT IS SUBJECT TO THE TERMS OF THE BROKER/CARRIER AGREEMENT SIGNED BY THE CARRIER AND TQL. THIS AGREEMENT IS AN ADDENDUM TO THE BROKER/CARRIER AGREEMENT. THIS RATE CONFIRMATION IS INCLUSIVE OF ALL CHARGES."*
> *"DETENTION: Must arrive on time and have in/out times on BOL's. $25/hr after 3 hrs of waiting time. Cap at $150 layover"*
> *"Driver must accept cell phone or ELD tracking and consistently track (1 ping per 15 mins) from time of dispatch to completed delivery. **Failure to accept or consistently track will result in no detention or layover**"*
> *"Lumper receipt & detention must be sent in w/ BOL's within 3 days of delivery."*

**Flock Freight** subordinates the BOL explicitly: *"Any terms of the bill of lading, delivery receipt, or tariff…inconsistent with the terms of this Agreement shall not operate to alter or amend the provisions herein and shall be subordinate to this Agreement."*

**The Arrive Logistics (DM Trans, LLC) Broker Carrier Agreement, filed publicly in FMCSA docket FMCSA-2023-0257, is the single highest-value artefact found** — a top-15 broker's full BCA *plus* its Accessorial Addendum. ¶3–¶6:

> "3. Carrier shall notify Arrive **no later than 30 minutes prior to going into detention** at both the Shipper and Receiver locations…
> 4. Carrier must ensure that it obtains a signed bill of lading and/or proof of delivery **with both in and out dwell times**… Carrier shall submit all signed documentation **within forty-eight (48) hours** of delivery. **Failure to abide by these requirements may result in a reduction of Carrier's accessorial payment by up to 50%, to be determined in Arrive's sole discretion.**
> 5. …a. TONU: $200 flat rate b. Layover: $250 flat rate c. Detention: $50/hour up to 5 total hours (**Detention time begins 2 hours after the scheduled appointment time - Driver must be on time for appointment to qualify**)…
> 6. [reefer] a. TONU: $250 …c. Detention: $50/hour up to 6 total hours…"

Merger clause §15(g): *"This Agreement… constitutes the entire agreement… and may not be changed, waived or modified except in writing signed by both parties."*

**Critically, Arrive invokes the federal waiver statute in its preamble:** *"in accordance with 49 U.S.C. §14101(b)(1) and expressly waive any and all rights and remedies that each may have under 49 U.S.C. §13101 through §14914 that are contrary to the specific terms and conditions of this Agreement."* **VERIFIED: §14101(b)(1) permits exactly this waiver.**

**Practical consequence: statutory defaults do not rescue a carrier; the contract is the whole ballgame.**

The TIA-style model BCA (Freight360 sample, NTBA template) contains the gating clause appearing in nearly every agreement read: *"Rates or charges, including but not limited to stop-offs, detention, loading or unloading, fuel surcharges, or other accessorial charges… **shall only be valid when their terms are specifically agreed to in a writing signed by both Parties**."*

**This means an accessorial not priced on the rate con is presumptively unenforceable, not merely unpaid.**

## Pay-when-paid analysis (thesis risk)

**VERIFIED, real but not universal.** Dray Alliance's public BCA §6(a): *"Rates for any and all accessorial services… must be set forth in individual Rate Confirmations to be valid. **In no event will BROKER be responsible for payment of such rates unless paid by the Customer.**"* That is a pay-**if**-paid condition precedent scoped specifically to accessorials.

Counterweight — the industry-standard clause in the TIA model and NTBA template: *"The Parties agree that BROKER is the sole party responsible for payment of CARRIER's charges. **Failure of BROKER to collect payment from its customer shall not exonerate BROKER of its obligation to pay CARRIER.**"* Arrive's and Flock's agreements contain **no** pay-when-paid clause.

**Assessment: in a sample of 5 real BCAs, 1 of 5 had an express accessorial pay-if-paid; 2 of 5 had the opposite (broker is sole obligor).** UNKNOWN: true prevalence across the broker population, and enforceability. Construction-law doctrine voiding pay-if-paid on public-policy grounds is state-specific and **no freight case applying it could be verified — do not assume it transfers.** What *is* verified is that §14101(b)(1) lets parties contract around Part B, which cuts against a statutory override.

**Where it bites hardest is drayage/intermodal.** A recovery product should treat drayage as a separate, lower-yield segment.

## Notice/timing conditions precedent — THE SHARPEST THREAT TO THE THESIS

**VERIFIED across every document read.** Detention entitlement is gated by conditions the carrier must satisfy *at or before the moment of detention*, not afterward:

| Broker | Pre-detention notice | Doc deadline | Consequence of miss |
|---|---|---|---|
| **Arrive Logistics** | **30 min *before* detention starts** | Signed BOL w/ in-out times within **48 hrs** | Up to **50% reduction**, broker's sole discretion |
| **Dray Alliance** | **60 min** before detention accrues | Invoice within 180 days | No payment; accessorial invalid unless on rate con |
| **TQL** (rate con) | Continuous ELD/phone tracking, **1 ping/15 min** | BOL + detention within **3 days** | *"no detention or layover"* |
| **Flock Freight** | — | POD within 24 hrs; **90-day** outer limit | *"Carrier hereby forfeits and waives any right to payment"* |

FreightWaves (Adam Wingfield, 2025-05-22) confirms the practitioner view, flagging as red flags *"Must be approved in writing"* with no defined process and *"No detention will be paid without written authorization from agent."* A LawInsider-sourced brokerage agreement goes further: *"DRAYMAN shall not [charge] BROKER, and BROKER shall have no obligation to pay, for accessorial charges without the written agreement of BROKER."*

### Honest conclusion (answers RQ7)

**A purely post-hoc product that discovers unbilled detention weeks later recovers very little, because the entitlement was extinguished at the dock — no 30/60-minute call, no in/out times on the BOL, no tracking consent.**

**The defensible product is real-time (fire the notice before free time expires, force the in/out signature, capture the geofence), with post-hoc recovery as a secondary, lower-yield motion.**

**No case law** could be verified on how courts treat these notice conditions when a broker has actual knowledge of the delay — **UNKNOWN**; a genuine open legal question worth a lawyer's opinion before pricing the post-hoc product.

## Accessorial rule heterogeneity (answers RQ6)

| Source | Free time | Rate | Increment | Cap | TONU | Layover |
|---|---|---|---|---|---|---|
| Arrive (dry van) | 2 hr, on-time only | $50/hr | hourly | 5 hr ($250) | $200 | $250 |
| Arrive (reefer) | 2 hr, on-time only | $50/hr | hourly | 6 hr ($300) | $250 | $300 |
| TQL (rate con) | 3 hr, on-time only | $25/hr | hourly | $150 | conditional | — |
| LawInsider ex. 1 | weight-tiered: 30/60/90/120 min | $40 | **half-hour** | $360 | — | — |
| LawInsider ex. 2 | same weight tiers | $53.33 | **half-hour** | $480 | — | — |
| LawInsider ex. 3 | 2 hr | **$1.00/min** | per-minute | $360 | — | — |
| FMCSA NPRM commenter | 4 hr (to carrier) | $35/hr | hourly | — | — | — |
| Truckstop (industry) | 2 hr | $50–85/hr | hourly | — | $150–300 | $200–500/day |

**Answer to RQ6: the space is NOT a long tail of rule *shapes* — it is essentially one parametric template with a weight-tiered variant.** Every schedule reduces to `free_time → rate × increment → cap`, plus an **on-time-arrival predicate**. That is **2–3 shapes, ~5 parameters.**

The real heterogeneity is in (a) parameter values, (b) equipment-type splits (dry vs reefer differ *within* a single broker), (c) the conditions precedent, and (d) **unilateral amendment rights** — Arrive: *"Arrive reserves the right to modify the Accessorial Rates or time frames provided herein at any time, effective on notice to Carrier."*

**The engineering problem is not rule-shape modelling; it is per-account parameter capture and versioning.**

FMCSA itself confirms the underlying ambiguity: *"Although there is currently no standard definition of detention time…"* (88 FR, Docket FMCSA-2023-0172).

## Statutory billing windows

**VERIFIED. 49 U.S.C. §14705(a):** *"A carrier… must begin a civil action to recover charges for transportation or service provided by the carrier within 18 months after the claim accrues."* §14705(b): overcharge actions, 18 months (3 years before the Board/Secretary). §14705(c): loss/damage, 2 years minimum. §14705(d) extends 6 months from written disallowance and 90 days when the carrier begins collection.

**Critical correction to a common assumption: §14705(a) is a limitations period on *filing suit*, not a deadline to *bill*.** No federal statute prohibiting late accessorial billing for motor carriers was found (UNKNOWN whether one exists elsewhere in Part B).

**The operative deadlines are contractual and far shorter.** Arrive — invoice in 15 days, *"Carrier will waive its right for payment of any freight bills not submitted for payment within **90 days** of delivery. Carrier must provide written notice of any undercharge claim within **180 days** of Arrive's receipt of the applicable original invoice."* Dray Alliance uses the identical 180/180/18-month cascade.

**The recovery window for a supplemental accessorial claim is therefore typically 180 days from the original invoice, not 18 months. That materially compresses any backward-looking TAM — by roughly 3–4×.**

**49 CFR §371.3(c)** (VERIFIED): *"Each party to a brokered transaction has the right to review the record of the transaction required to be kept by these rules."* FMCSA's pending NPRM would upgrade this to *"Brokers must provide, upon request by any party to a brokered transaction, a copy of the record… electronically within 48 hours."* **No final rule had issued as of the Federal Register query** (latest: Proposed Rule, 2025-02-18).

**The same NPRM documents the broker arbitrage directly:** *"the broker charged the shipper for detention time after the first hour, at a rate of $50 per hour, but paid the carrier for detention only after 4 hours, and at a rate of $35 per hour."*

## Factoring assignment issue

**Partially VERIFIED; a real complication.** Freight factoring agreements sell "all accounts… and all proceeds thereof" — typical language: *"We hereby sell and assign to you, making you absolute owner thereof, all of our accounts, contract rights, notes, bills, acceptances and all other obligations to us… for the payment of money, in cash or in kind, together with all proceeds thereof."*

**Under that formulation a supplemental detention claim arising from the same shipment is plausibly a proceed of an already-sold account, and the carrier may no longer own the claim.** UCC §9-406(a) (VERIFIED) makes the broker dischargeable only by paying the assignee once notified. **A freight-specific factoring agreement's text could not be obtained — detention-specific scope is UNKNOWN and must be diligenced directly with 2–3 factors.**

Two verified aggravators: (1) the TQL rate confirmation's carrier remit-to address is *"RTS FINANCIAL (PO BOX 840267)"* — **factoring is the norm, not the exception, in the small-carrier segment this product targets**; (2) Arrive §8: *"Carrier will provide Arrive with at least 30 days' written notice prior to any assignment, factoring or other transfer of any of its rights… Arrive will accept or reject such proposed change in Arrive's sole discretion."* UCC §9-406(d) makes anti-assignment terms ineffective, but the notice/approval friction is real.

**Practical implication: the product likely needs a tri-party consent or must sell to factors rather than carriers.**

## Licensing / UPL exposure

**VERIFIED, and a genuine go-to-market risk commonly underestimated because founders check the FDCPA and stop.**

15 U.S.C. §1692a(5) defines "debt" as an obligation *"of a consumer… primarily for personal, family, or household purposes"* — **freight claims are commercial, so the FDCPA does not apply.** State collection-agency licensing is a different question, and several states cover **commercial** claims:

- **Washington (VERIFIED):** RCW 19.16.100 defines "claim" as *"[a]ny obligation for the payment of money or thing of value arising out of any agreement or contract, express or implied"* — **not consumer-limited.** RCW 19.16.110: *"No person shall act, assume to act, or advertise as a collection agency… without first having applied for and obtained a license."* Exemptions cover lawyers, banks, insurers, employees of one employer — **no fintech/billing-service exemption on point.**
- **North Carolina (VERIFIED):** G.S. §58-70-15(a) — a collection agency is one soliciting *"delinquent claims of any kind owed or due or asserted to be owed or due"*; permit required.
- **Minnesota (VERIFIED):** Minn. Stat. §332.31 — *"a person engaged in the business of collection for others any account, bill, or other indebtedness."*

**UPL (VERIFIED):** *Rowland v. California Men's Colony*, 506 U.S. 194 (1993) — *"a corporation may appear in the federal courts only through licensed counsel."* **A startup cannot litigate a carrier's claim, and in most states cannot take an assignment for the purpose of suing.** Non-litigation demand and negotiation by a licensed collection agency is generally permissible; **advising the carrier on whether a clause is enforceable is not.**

**Structural mitigations worth legal review (all UNKNOWN until opined on):**
1. Position as a **billing/invoice-preparation service submitting original invoices** rather than collecting delinquent debt — **many statutes hook on "delinquent"**
2. Contingency fee on *original* accessorial billing rather than on collection of past-due amounts
3. Take assignment/purchase the claim (converts you from collector-for-another to owner — several statutes exempt this; WA exempts fictitious-name self-collection only, so verify state by state)
4. Partner with a licensed commercial collection agency for the aged-receivable tail

## Evidence hierarchy: what wins and what gets rejected

Ranked by dispositive power, **derived from the contract requirements themselves** (which define what the payer will accept), not from opinion:

1. **Signed BOL/POD annotated with in *and* out times.** Named as required proof in Arrive ¶4, TQL's rate con, and the LawInsider shipper clause (*"(1) a 214 status update or (2) a signed BOL annotating the times checked in and out"*). **The only artefact that is simultaneously the carrier's proof and the receiver's admission.**
2. **EDI 214 status messages / broker-platform check-in-check-out.** Contractually co-equal with the signed BOL; superior in practice because the broker generated it.
3. **Real-time visibility/ELD geofence trail.** Arrive ¶1 mandates integration with a *"Real-Time Visibility Platform"*; TQL conditions detention on *"1 ping per 15 mins."* **Note this is a condition of eligibility as much as evidence — absence of tracking is an independent forfeiture, not merely a weak proof.**
4. **Appointment confirmation** — establishes the on-time predicate, which Arrive and TQL both make a hard gate.
5. **Timestamped/geotagged arrival photos, gate receipts, contemporaneous email/text to the broker.** Corroborate but rarely carry a claim alone.
6. **Driver macro / dispatch notes.** Self-serving and unilateral; weakest.

**What gets rejected, and why:**
- (a) **BOL with no out-time — the single most common failure, because the signature is captured at check-in**
- (b) late arrival, which voids entitlement entirely regardless of dwell
- (c) no pre-detention notice within the 30/60-minute window
- (d) documents submitted after 48 hours / 3 days / 90 / 180 days
- (e) accessorials not priced on the rate con
- (f) broken tracking
- (g) shipper audit reversal — *"Shipper reserves the right to audit Carrier's check in and out information and may deny or seek repayment for detention charges."*

## The 3 biggest legal threats to this thesis

1. **Conditions precedent are extinguishing, not curable.** VERIFIED in 4 of 4 real broker documents. Notice must precede detention by 30–60 minutes; documents must land in 48 hours to 3 days. **A product that finds missed detention after the fact is not recovering a live claim — it is asking for a discretionary gratuity. This is the thesis-defining risk, and it argues decisively for a real-time capture product over a recovery product.**
2. **The recovery window is contractual and short — ~180 days, not 18 months.** VERIFIED in Arrive and Dray Alliance. **Any backward-looking TAM built on §14705's 18 months is overstated by roughly 3–4×**, because §14705 governs *suit*, not billing, and is itself waivable under §14101(b)(1).
3. **Ownership and licensing sit on top of an already-thin claim.** Factored carriers may not own the supplemental claim (UCC §9-406; "all accounts and proceeds"), and collecting commercial claims for others requires a license in WA, NC, MN and likely others — with **no FDCPA safe harbour** and *Rowland* foreclosing self-representation. **Contingency-fee framing ("we recover your money for a %") is precisely the fact pattern those statutes describe.**

**Secondary risk:** accessorial pay-if-paid in drayage, and brokers' unilateral right to restate the accessorial schedule on notice (Arrive ¶7), **which lets a payer devalue the product's output at will.**

## Sources
downloads.regulations.gov/FMCSA-2023-0257-6912/attachment_2.pdf (**Arrive BCA + Accessorial Addendum**) · drayalliance.com/broker-carrier-agreement · fds-docs.sostruckingsoftware.com/api/Attachment/GetAttachmentById?id=25993 (**TQL rate con**) · flockfreight.com/resources/broker-carrier-agreement · freight360.net/wp-content/uploads/2023/10/Sample_Broker-Carrier_Agreement.pdf · ntba-brokers.com/wp-content/uploads/2020/03/ntba_broker_carrier_agreement_template.pdf · lawinsider.com/clause/detention (+/_2, /_9) · lawinsider.com/clause/accessorial-charges · law.cornell.edu/uscode/text/49/14705 · /49/14101 · law.cornell.edu/cfr/text/49/371.3 · federalregister.gov/documents/2024/11/20/2024-27115/transparency-in-property-broker-transactions · /2023/08/24/2023-18239/...impact-of-driver-detention-time · law.cornell.edu/ucc/9/9-406 · law.cornell.edu/uscode/text/15/1692a · app.leg.wa.gov/rcw/default.aspx?cite=19.16.100 (+19.16.110) · ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_58/GS_58-70-15.html · revisor.mn.gov/statutes/cite/332.31 · law.cornell.edu/supremecourt/text/506/194 (**Rowland**) · freightwaves.com/news/understanding-detention-pay-clauses · truckstop.com/blog/accessorial-charges/

**Not verified (do not cite downstream):** DOT OIG 2018 report URL (agent 14 verified it separately as ST2018019); case law on enforceability of accessorial notice conditions precedent or freight pay-if-paid; state collection statutes beyond WA/NC/MN; freight-specific factoring agreement text.
