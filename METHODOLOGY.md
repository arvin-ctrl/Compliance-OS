# Methodology

## Research date

All web research conducted **2026-08-19**. Every claim in this repository is timestamped to that date. Freight software moves fast; treat anything here as stale after roughly two quarters.

## Agent architecture

The brief specified a multi-agent structure. It was executed as follows.

### Layer 1 — 15 competitor / substitute / evidence agents (parallel)

| # | Lane | Targets |
|---|---|---|
| 01 | Carrier TMS billing | McLeod (LoadMaster, PowerBroker), Prophesy, Axon, Rose Rocket, AscendTMS |
| 02 | Enterprise TMS | MercuryGate, Trimble (TMW, TruckMate, Innovative, Kuebix) |
| 03 | Appointment / audit / visibility | Descartes (MacroPoint, Aljex, dock scheduling), Transporeon |
| 04 | ELD / telematics + API reality | Samsara, Motive |
| 05 | Visibility platforms | project44, FourKites |
| 06 | Freight audit & payment | Cass, nVision, Trax, Intelligent Audit, A3, Loop, AFS, CTSI |
| 07 | Factoring & payments | TriumphPay, OTR Solutions, Denim, RTS, Apex, eCapital, Relay, Corpay |
| 08 | Direct-competitor sweep | Every startup automating detention/accessorial recovery |
| 09 | Cargo claims / OS&D | TranSolutions, Loadsure, claims modules, contingency claims firms |
| 10 | Ocean/drayage D&D | FMC rules, Terminal49, Container xChange, PortPro, Envase, Vizion |
| 11 | Broker margin leakage | Turvo, Revenova, Tai, Alvys, Denim, PowerBroker, public-filer economics |
| 12 | Shipper side | Oracle OTM, Blue Yonder, SAP TM, e2open, Opendock, YMS |
| 13 | Freight back-office AI | Vooma, Drumkit, HappyRobot, Expedock, Loop, Cargado, Vector |
| 14 | Economics | DOT OIG, ATRI, FMCSA, BLS, DAT, public filings — hard numbers + 3 ROI models |
| 15 | Legal & contract | Broker-carrier agreements, pay-when-paid, 49 U.S.C. §14705, collection-agency licensing |

### Layer 2 — category managers

Four category managers consolidated Layer 1 into the four cross-cutting matrices (competitor landscape, capability matrix, substitute-stack matrix, buyer/JTBD matrix).

### Layer 3 — synthesis manager

Generated candidate wedges (minimum 5 required) from the consolidated evidence.

### Layer 4 — red-team manager

Attempted to kill every wedge along eight attack vectors: incumbents, substitute stacks, internal build, consultants, pricing, switching cost, legal risk, distribution.

### Layer 5 — final-decision manager

Issued exactly one verdict: **GO**, **PIVOT**, or **KILL**.

## Evidence standard

Every material claim carries one of three labels:

- **VERIFIED** — supported by a primary source: official docs, API reference, pricing page, published case study, regulatory filing, statute, or public-company financial disclosure.
- **CLAIMED** — asserted by the vendor in marketing copy but not independently confirmed.
- **UNKNOWN** — could not be established. Explicitly recorded rather than guessed.

Derived figures are labelled **DERIVED** and show their arithmetic. Assumptions in ROI models are individually marked CITED or ASSUMED.

Where no rigorous data exists, the finding recorded is "NO RIGOROUS DATA FOUND". That absence is treated as a research result, not a gap to be filled with an invented number.

## Scoring rubric

Capability scores use a three-point scale, applied per vendor per dimension:

| Score | Meaning |
|---|---|
| **0** | Absent. The product does not do this. |
| **1** | Partial. Possible but manual, requires services/configuration work, or exists only as a report rather than an action. |
| **2** | Strong. Native, automated, productised. |

A score of 1 is the most important value in this matrix. Most "does X" marketing claims resolve to 1, not 2 — the system can *hold* the data but a human still has to *decide and act*. The thesis lives or dies in the gap between 1 and 2.

## The "missing feature is not white space" rule

Applied strictly. For every gap identified, three questions had to be answered before it could be called white space:

1. Do customers actually feel this gap, with evidence?
2. Is the gap structural (incentive, data-ownership, or business-model conflict) or merely unbuilt?
3. Could the incumbent close it in one release cycle if it wanted to?

Only gaps that are structural, felt, and defensible survived into the wedge list.

## Repository map

```
00-MASTER-PROMPT.md      the brief, verbatim
METHODOLOGY.md           this file
outputs/                 the 10 required deliverables
research/raw/            unedited agent reports (the evidence base)
research/economics/      ROI models and cited figures
research/legal/          contract, statute and licensing analysis
data/                    machine-readable matrices (CSV) + dimension definitions
```

## Known limitations

- Web research only. No primary interviews with carriers, brokers, or shippers were conducted. Several conclusions below are explicitly flagged as requiring customer discovery before they can be trusted.
- Private-company pricing is frequently undisclosed; where pricing is marked UNKNOWN it means no public anchor was found, not that the product is free or cheap.
- Vendor capability was assessed from public artefacts, not hands-on trials. A demo would move several scores.
