# Construction Revenue Recovery — Market Research

An adversarial research program testing whether there is a large, defensible opportunity in helping
contractors recover or protect revenue lost because claims, change-order entitlements, notice deadlines,
delay evidence, contract clauses, and project records are fragmented across documents and systems.

**Research window: August 2026. Verdict: PIVOT.**

---

## The finding in one paragraph

Every product in this market builds up to *the number* and stops at *the number*. Five platforms with
different owners, ICPs, geographies and business models make the identical stop, and not one of them has a
field for clause reference, notice date, notice deadline or entitlement basis on its change object. The front
half of the pipeline — clause extraction, notice detection, notice drafting — is commoditised or free. The
back half — evidence sufficiency, causation, quantum, claim package — is empty in every product in every
language surveyed. The seam is real. What is **not** established is that anyone pays to recover, rather than
to defend or to bill hours: the closest analogue in the world ran the thesis for eight years under ideal
conditions, published eleven case studies containing **zero recovered claims in currency**, and shrank while
doing it.

## Verdict

**PIVOT** — from a per-matter chronology tool for claims consultancies to a **per-event artefact generator**
for the one US regime where a public owner has already written the specification and started the clock:
Caltrans' 20-day Supplemental Potential Claim Record, which mandates an itemised cost estimate and a time
impact analysis or the claim is waived and arbitration barred.

Gated behind **$2,500 and ten weeks** of tests. **No code before 30 October 2026.**
The decisive test — a California Public Records Act request on Caltrans ePCR filings — costs under $50,
takes three weeks, and produces a frequency number nobody in the industry has.

## Read in this order

| # | Deliverable |
|---|---|
| **10** | **[GO/PIVOT/KILL memo](outputs/10-go-pivot-kill-memo.md)** — start here. Verdict, gates, kill criteria, all 10 research questions, all 7 hypotheses |
| 5 | [Top 5 wedges](outputs/05-top-5-wedges.md) |
| 6 | [Red-team report](outputs/06-red-team-report.md) — killed 5 of 8 and inverted the ranking |
| 7 | [Solo-founder MVP](outputs/07-solo-founder-mvp.md) |
| 8 | [Pricing hypothesis](outputs/08-pricing-hypothesis.md) |
| 9 | [First-20-customer plan](outputs/09-first-20-customers.md) |
| 1 | [Competitor landscape](outputs/01-competitor-landscape.md) |
| 2 | [Capability matrix](outputs/02-capability-matrix.md) — 26 dimensions × 23 entities |
| 3 | [Substitute-stack matrix](outputs/03-substitute-stack-matrix.md) |
| 4 | [Buyer / JTBD matrix](outputs/04-buyer-jtbd-matrix.md) |

Underlying evidence: **17 competitor/substitute reports** in [`research/raw/`](research/raw/), four category
syntheses, the wedge generator, the red team, and the decision memo in [`research/`](research/).
[`research/NOTES-running.md`](research/NOTES-running.md) is the orchestrator's cross-agent record — every
correction, contradiction and confirmed constraint as it was found.

## Method

17 independent research agents → 4 category managers → 1 synthesis manager (8 wedges) → 1 red-team manager
(killed 5) → 1 final-decision manager. See [`docs/METHOD.md`](docs/METHOD.md).

Rules enforced throughout: a missing feature is **not** white space without evidence of paid-for pain; every
material claim carries a URL; unverifiable claims are labelled `UNVERIFIED` rather than smoothed over; the
founder is assumed solo.

## Ten things that changed the answer

1. **Procore shipped the Change Analysis Agent** (GA 23 Jul 2026) — event detection is no longer white space.
2. **Procore revoked Trunk Tools' API access** (Sept 2025) and forbids parsing in its Developer Policy — the
   layer-above-Procore hypothesis is dead.
3. **Trimble acquired Document Crunch** for $246.4M (closed 4 Apr 2026) — contract-clause AI as a V1 is dead.
4. **Aconex is the evidence *warehouse*, not the evidence *graph*** — "no super user" means no party can ever
   query the whole record, so the graph cannot be built inside it by anyone.
5. **Levelset is a cautionary comp, not a validating one** — the $59 notice and $349 lien *filing* was the
   revenue; contractual notice has no filing, no clerk, no fee.
6. **AACE RP 29R-03 §1.2(f) forecloses automated attribution** — and SCL Core Principle 12 means naive
   delay-days × rate is wrong by construction.
7. **The contract form manufactures the product's *shape*, not demand** — Germany, Sweden, Norway and Italy
   all mandate notice and produced zero entitlement products.
8. **Quantum is empty in every language** — the one good engine (Easyclaim, €599/case) has no AI, no ingest,
   and runs as a single offline HTML file.
9. **Technology budget is 0.26% of revenue** — so the product must be job-costed, never bought from IT.
10. **Gather's £300k "recovery" was a client-side saving** — money withheld *from* a contractor. The most
    on-thesis product in the world is evidenced as claims *defence*.

## Splitting this into its own repository

This was built as a self-contained project. The GitHub App in the originating session lacked
repository-creation scope, so it landed inside another repo. To give it its own remote:

```bash
# from the parent repository
git subtree split --prefix=construction-revenue-recovery-research -b crr-standalone
git checkout crr-standalone
# create an empty repo on GitHub, then:
git remote add crr git@github.com:<you>/construction-revenue-recovery-research.git
git push -u crr crr-standalone:main
```

## Status and limitations

Desk research only. No customer interviews were conducted — and the program's own conclusion is that ten
contractor interviews would settle more than another week of desk research. Specific gaps, all flagged in
place: no credible published dollar figure for change-order write-off *value* exists (the industry publishes
incidence); Reddit was IP-blocked and reached via archive, and that subreddit is heavily astroturfed; G2 and
TrustRadius returned 403 during the Procore pass, so review evidence is Capterra-weighted; and no case
enforcing the Caltrans §5-1.43A waiver was located.
