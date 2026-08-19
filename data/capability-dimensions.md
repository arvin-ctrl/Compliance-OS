# Capability dimensions — definitions

The 25 dimensions from the brief, with the precise test applied when scoring. Ambiguous definitions produce meaningless matrices, so each dimension states what earns a 2 rather than a 1.

| # | Dimension | What it tests | Earns a 2 only if... |
|---|---|---|---|
| 1 | `rate_confirmation_ingestion` | Can the system take in a rate confirmation as a document? | It parses the document automatically (PDF/email/fax), not just stores an attachment |
| 2 | `rate_rule_extraction` | Does it extract the *accessorial rules* — free time, $/hr, increment, cap, notice window, required docs? | Rules become structured, executable data, not text a human reads |
| 3 | `gps_eld_timestamps` | Does it hold arrival/departure timestamps from telematics? | Timestamps are load-associated and usable downstream, not just a map trail |
| 4 | `appointment_ingestion` | Does it know the scheduled appointment window? | Appointment is captured as structured data and compared against actuals |
| 5 | `pod_bol_ingestion` | Does it take in BOL/POD documents? | It reads them, including in/out times, not just files them |
| 6 | `detention` | Detention specifically | Auto-detects and calculates a detention entitlement |
| 7 | `tonu` | Truck Ordered Not Used | Auto-detects a TONU event and its entitlement |
| 8 | `layover` | Layover | Auto-detects and calculates |
| 9 | `lumper` | Lumper fee capture and reimbursement | Auto-captures receipt and pushes to reimbursement |
| 10 | `demurrage` | Container demurrage / per-diem | Auto-detects, validates against tariff, and disputes |
| 11 | `accessorial_detection` | The general case: does it *find* charges nobody entered? | Detection is proactive — the system raises the charge unprompted |
| 12 | `evidence_package` | Does it assemble a defensible bundle? | One artefact combining timestamps, documents and correspondence, generated automatically |
| 13 | `invoice_creation` | Does it produce the invoice? | Generates a billable supplemental/accessorial invoice |
| 14 | `claim_submission` | Does it deliver the claim to the payer? | Submits via portal/EDI/email automatically |
| 15 | `collection_tracking` | Does it track whether the money arrived? | Per-claim aging, short-pay and outcome tracking |
| 16 | `dispute_workflow` | Does it manage the argument? | Structured back-and-forth with evidence re-submission |
| 17 | `portal` | Is there a self-serve UI for the counterparty? | Counterparty can view and respond to claims |
| 18 | `tms_integration` | Does it connect to TMS? | Bidirectional, productised connectors — not a CSV export |
| 19 | `eld_integration` | Does it connect to ELD/telematics? | Productised connectors to major ELD vendors |
| 20 | `email_sms_ingestion` | Does it read the correspondence trail? | Parses inbound email/SMS into load-linked evidence |
| 21 | `accounting_integration` | Does it write to the books? | Native connector to QuickBooks/NetSuite/AR ledger |
| 22 | `recovered_revenue_analytics` | Does it report money recovered? | Attribution of recovered dollars, not generic dashboards |
| 23 | `performance_pricing` | Is it sold on % of recovery? | Vendor actually prices on outcomes |
| 24 | `customer_specific_rules` | Does it handle per-customer rule variation? | Per-customer rule sets applied automatically at scale |
| 25 | `multi_carrier_shipper_support` | Does it work across many counterparties? | Genuinely multi-tenant across trading partners |

## Scoring scale

- **0** — absent
- **1** — partial: possible, but manual, services-heavy, or reporting-only
- **2** — strong: native, automated, productised

## Why the 1-vs-2 boundary matters most

Almost every incumbent scores 1 on `detention`. They *can* bill detention — a user types it in. They *can* show dwell — on a dashboard. The question this research exists to answer is whether the distance between "the system holds the data" and "the system raises, evidences, invoices and collects the charge without a human" is a product, or a feature the incumbent ships next quarter.
