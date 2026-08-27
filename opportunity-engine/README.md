# Opportunity Engine

A standing origination process for finding **one buildable project per cycle** — replacing the R&D market
research format, which produced excellent research and nothing we could start.

## Start a cycle

Paste [`MASTER-PROMPT.md`](MASTER-PROMPT.md). It carries the operator profile, the gates, the surfaces, the
team structure, and the output contract.

## What changed, and why

The previous format searched for **defensible whitespace in large markets**. It kept returning verdicts
gated on things we cannot do — records requests, 30 customer interviews, a professional credential — because
those are the questions that decide whether *whitespace* is real. Five cycles, no projects.

This engine searches for **capability overhangs with observable demand that we can verify by building.**

| | Old format | This engine |
|---|---|---|
| Target | Defensible market whitespace | Capability overhang |
| Demand evidence | Inferred from analyst reports | Observed: money moving, hands doing the work |
| Distribution | Assessed last, if at all | **Gate one, with a veto** |
| Decisive test | Needed strangers | Must be runnable by us in 14 days |
| Depth | One thesis, six weeks | ~100 candidates → ~15 → 1, one week |
| Output | GO/PIVOT/KILL memo | **Project Charter with a build spec and a kill number** |
| Scale ceiling | The primary filter | A 5% tiebreaker |
| Memory | None — each cycle reset | `LEDGER.md` + `WATCHLIST.md` compound |

## The five gates

Applied in order, cheapest and most fatal first. A failure is a one-line kill.

1. **Cold-start distribution** — can we reach the first ten users with no audience? Name them.
2. **Observable demand** — is money already moving, or hands already doing it, visibly?
3. **Buildable by us** — is the bottleneck skilled work, or access?
4. **Self-verifiable in 14 days** — can we settle the riskiest assumption alone?
5. **The clock** — what changed in the last 24 months?

## Files

| File | Purpose |
|---|---|
| [`MASTER-PROMPT.md`](MASTER-PROMPT.md) | The prompt. Paste to run a cycle. |
| [`LEDGER.md`](LEDGER.md) | Every candidate ever assessed, with its kill reason. Prevents re-researching dead ideas. |
| [`WATCHLIST.md`](WATCHLIST.md) | Killed *on a clock* — with re-check dates and revival conditions. |
| [`POSTMORTEM.md`](POSTMORTEM.md) | Why the previous format failed, in detail. The source of the standing laws. |

## Operator profile currently encoded

One full-time operator plus agents · $5–50k before revenue · **cold start, no audience or industry access** ·
search anywhere. **Distribution is the binding constraint** — this is what the gate order and the scoring
weights are built around. Change the profile at the top of the master prompt and the weights should change
with it.
