# 3. Substitute-Stack Matrix

The question this answers: **if a contractor does nothing new, what already covers each stage of the
pipeline, at what cost, and how well?**

This matters more than the competitor matrix. The DIY stack kills more startups than any vendor, and in this
market it is not a stack of software — it is *a staffed manual process defended by professional identity*.

## The six substitute stacks

| Stack | What it is | Annual cost | Where it wins | Where it fails |
|---|---|---|---|---|
| **A. Excel + Outlook + SharePoint** | COR log in a spreadsheet, notice tracked in a calendar reminder or nothing at all, evidence in email folders | ~$0 marginal | Zero switching cost, total flexibility, nobody has to be trained | No completeness check, no cross-document linkage, collapses beyond 3–4 concurrent jobs |
| **B. Stack A + M365 Copilot / ChatGPT** | Upload the contract, ask for notice deadlines | $18–30/user/mo | **Answers contract questions better than a lawyer answers document questions** (Vals: 94.8% vs 70.1% doc Q&A) | No persistent state, no event monitoring, no evidence linkage, no audit trail, no artefact |
| **C. Procore / ACC + Stack A** | Platform holds the records; commercial reasoning still happens in Excel and email | Procore priced on construction volume; ACC per-user | Records are captured, timestamped, permissioned | **No field for clause reference, notice date, notice deadline or entitlement basis on the change object** |
| **D. Hire a person** | Change Order Engineer, Contract Administrator, Claims Manager | **$85–120K** (Tutor Perini CO Engineer); **$140–182K** (AECOM Claims Manager); 1,000+ open US CA roles | Judgement, relationships, accountability, credential | Doesn't scale, doesn't work weekends, leaves; costs 7–20x any software subscription |
| **E. Call a consultant** | HKA, Ankura, Trauner, Long International, VERTEX | **$225–1,375/hr**; full delay+quantum claim **600–1,650 hrs / $240k–660k** | Court-grade, credentialed, testifiable | **Starts after the loss.** Uneconomic below ~$5m in dispute — which is **39% of all disputes** |
| **F. Relativity / Everlaw (eDiscovery)** | Document review at litigation stage | RelativityOne licence | **aiR for Case Strategy, GA 12 Jan 2026: fact chronologies with citations *and evidence-gap analysis*, included at no extra cost** | Litigation-stage, law-firm buyer, no construction entitlement layer, no notice register, no EOT/compensable split |

## Coverage by pipeline stage

| Stage | Best substitute | How well | Price today |
|---|---|---|---|
| Contract ingestion | B / F | **Fully covered** | $0–30/user/mo |
| Clause & notice extraction | B, or Trunk Tools' free tool | **Fully covered** | **$0** |
| Event detection from project records | C (Procore Change Analysis, GA 23 Jul 2026) | Covered and improving | Credits |
| Entitlement matching | D or E — a human | Covered by judgement, not tooling | $85–182K or $400/hr |
| Evidence collection & linking | A, or F at litigation stage | Manual, or free CSV from ACC Data Connector | ~$0 |
| **Evidence sufficiency** | **NOTHING** | **Scores 0 in the DIY stack** | **—** |
| **Causation / attribution** | E only | Standards say a tool *cannot* do it | $225–1,375/hr |
| **Recoverable-dollar quantum** | E only | Easyclaim (DE) is the sole product, €599/case, no AI | $240k–660k/matter |
| Notice drafting | B, or Document Crunch | **Commoditised** | $18–30/user/mo |
| Claim package assembly | E only | 600–1,650 hours | $240k–660k |

## The four findings that constrain any product

**1. The substitute is a person, not a tool.** A Change Order Engineer at $85–120K is the incumbent. That is
7–20x any realistic subscription — which is favourable arithmetic — but it means the sale is a *headcount*
argument made to whoever owns headcount, not a software argument made to IT.

**2. The stack is culturally defended, and the defence is rational.** Contractors **deliberately suppress
notice to protect owner relationships** — confirmed in print by construction counsel. Practitioner reaction to
this exact product idea, in four separate 2025–26 threads:

> *"This is like GC 101 and no one needs more software for anything. CONTRACTING is in the name."*

> *"Another shitty GPT wrapper… Go away. Reported."*

**Not one project executive or CFO appeared in any of those threads.** The hostility is real and comes from
the wrong persona — but it means the product must never make a PM feel audited, and **must never contact the
owner**.

**3. Only one gap is culturally undefended.** Notice tracking and evidence linkage are gaps, but they are
gaps *by choice*. **Evidence completeness is the single gap the industry admits to** — nothing checks whether
a claim's proof is complete before a human submits it. That converges with the capability matrix
(nobody >1 on dims 14/15/16) and with the pipeline occupancy map (the void is the detection→entitlement→quantum
seam). Three independent methods, one answer.

**4. The budget is smaller than the pain.** CFMA (n=1,558): **Technology Costs = 0.26% of revenue**
($368K on $139.4M average). Commercial GCs run **4.4% net income before taxes**; heavy civil 8.3%; specialty
trade 7.7%. A $200M GC has ~$500K of *total* technology budget — so the product must either displace headcount
or be **job-costed as project overhead**, never bought from the IT line.
