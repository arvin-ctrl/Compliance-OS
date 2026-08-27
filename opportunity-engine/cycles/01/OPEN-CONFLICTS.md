# Cycle 1 — cross-scout conflicts for triage to resolve

Two candidates were independently assessed by more than one scout, with opposing verdicts. These must be
resolved before any charter is written. **Both conflicts are more informative than either scout alone.**

---

## CONFLICT 1 — UAD 3.6 appraisal tooling: is the form standard an access wall?

| Scout | Verdict |
|---|---|
| **10 (communities)** | **Top candidate of the cycle, 7/10.** Hardest clock found: mandatory for all new UCDP submissions **2026-11-02**, ten weeks out; a reported ~3% of ~1,800 surveyed appraisers have completed one report; the 30-year incumbent publicly abandoned in-thread. Named the risk unprompted: *"the fatal risk is drifting into GSE-certified forms software, which we must not do."* |
| **3 (dead incumbents)** | **Killed a la mode TOTAL** on the grounds that **the UAD/MISMO form standard is an access problem** — explicitly the same shape as the Procore-layer and AACE candidates already dead in the ledger. |

**The question triage must answer:** can a tool produce *adjustment support and workfile documentation* — an
artifact the appraiser attaches — **without** touching UCDP submission or becoming GSE-certified forms
software? If yes, scout 10's candidate survives and the clock is real. If no, it is a Gate 3 failure and the
cycle's strongest clock dies with it.

**Cheap resolution:** read the UAD 3.6 spec and the UCDP submission path directly. Primary sources only —
scout 10's dates are community-corroborated **T2**, because Fannie and Freddie both returned 403 to this
environment. **Verify the 2026-11-02 date primarily before anything else.**

---

## CONFLICT 2 — Accessibility remediation: killed on warranty, or revived by changing the buyer?

| Scout | Verdict |
|---|---|
| **1 (capability overhang)** | The **cleanest price overhang in the cycle**: vendors describe themselves as already "AI + human" while quoting **$4–$11.50/page**; machine cost $0.001–$0.002. A 3,000–10,000x gap held open by an unchallenged price. |
| **9 (price dislocation)** | **Killed the entire accessibility cluster on structure.** Incumbents sell a *warranty* (measured accuracy, liability), not an output. A cold-start operator has no warranty to sell — now Standing Law 13. |
| **11 (unbundling)** | **Top candidate, 7/10 — and it may dissolve scout 9's kill by changing the buyer.** Sells to **the freelance remediators doing the work**, not the agencies procuring compliance. T1 rate card $0.50–$15+/page, $15K–$60K per 2,000-doc project, remediators hired at $15–20/hr. Hard clock verified primary on ada.gov: DOJ ADA Title II published 24 Apr 2024, compliance 26 Apr 2027/2028, PDFs explicitly covered. Ten named dated threads; r/accessibility verifiably tolerates vendors. |

**The question triage must answer:** does selling to the *freelancer* rather than the *compliance buyer*
escape Standing Law 13? The freelancer wants throughput and carries their own liability — so arguably the
warranty stays with them and never becomes ours. If that holds, the law is not violated but *bounded*, and
the bound is worth writing down.

**Load-bearing risk to test:** scout 11 reports an **automation ceiling of 30–50%** per two independent 2026
threads, and the community's own advice is *"convert to HTML instead."* A 30–50% ceiling may still be a
business if the freelancer bills by the page — that is exactly what the 14-day proof should measure.

**Before advancing:** scout 11's Reddit citations are URL + date + search-engine snippet — it did **not**
read the thread bodies, because Reddit is unfetchable from this environment. **Its quotes must be re-read
live.** This program died once on an unverified number.

---

## TOOLING FINDINGS — carry into every future cycle

| Environment fact | Consequence |
|---|---|
| **Fiverr is fully readable via the `r.jina.ai` text proxy** (direct curl 403s) — returns gig titles, review counts, prices, full package tables with delivery times, and *dated* reviews with buyer price bands | The single most useful access discovery of Cycle 1. Use it first on any marketplace surface |
| **Unreachable from this environment:** Reddit (403 JSON, HTML shell), Upwork, Etsy, eBay, Stack Overflow, Practical Machinist, CodeCanyon (Cloudflare), Fannie/Freddie, federalregister.gov, Amazon Seller Forums | Any Gate 1 resting on these is **unproven, not passed**. CodeCanyon is the biggest single miss — it publishes per-item **sales counts** beside last-update dates |
| **`old.reddit.com` HTML is scrapeable** where the JSON API is not — quotes and URLs survive, but **subscriber counts do not** | Use comment counts and thread frequency as a size proxy, and say so |
| **WebSearch budget is 200 calls, shared across the whole scout fleet** | Cycle 1 exhausted it roughly two-thirds through. **Cycle 2 must budget searches per scout explicitly**, or stagger scouts so late surfaces are not starved |
