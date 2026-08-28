---
name: agent-team
description: Run any substantial project through a team of agents that draft in parallel, cross-critique each other's work with fresh eyes, revise, and loop until an independent judge says the quality bar is met. Use this for EVERY project-scale request — build an app or feature, write a document/plan/strategy/report, design a page or system, create a curriculum or campaign — even when the user doesn't mention agents, teams, or loops; in this workspace it is the default path for projects. Also triggers on "use the team", "run the loop", "agent team", "best possible version", "don't one-shot this". Do NOT use for quick questions, single-file edits, small fixes, or conversational turns — those deserve a direct answer, not a team.
---

# Agent Team: the draft → critique → revise loop

## Why this exists

A single pass through a project produces a first draft with a deliverable's formatting. The
things that make work actually good — catching the weak section, noticing two parts contradict
each other, stealing the best idea from one part to fix another, cutting what doesn't serve the
goal — only happen in revision, and revision only works when the reviewer isn't the author. A
model re-reading its own output in the same context is biased toward defending it; a fresh
agent reading it cold is not. This skill manufactures that separation: parallel specialists
draft, fresh-context critics attack, revisers integrate the critique, an independent judge
decides whether to ship or loop. Maker and checker are never the same context.

The evidence for each design choice is collected in [references/research.md](references/research.md)
— read it when you want to know *why* a rule below is a rule, or when adapting the process.
The short version, from the literature: **ungrounded self-critique makes work worse** (asking a
model to "review your answer" with no external signal degraded GPT-4's GSM8K accuracy from
95.5% to 89.0% over two rounds — Huang et al., ICLR 2024), while **grounded critique reliably
helps** (tool-verified critique gained ~+7 points where self-talk lost points — CRITIC, ICLR
2024). Models fix errors attributed to someone else that they cannot see in their own output
(a measured 64.5% "self-correction blind spot" — hence fresh-context critics). Gains saturate
by rounds 2-4 and extra review rounds then *add* false positives (hence the bounded loop and
one thorough critique pass per version). Diverse perspectives help only above a quality floor
and only when initial drafts are independent (hence roles, and no peeking before round 1).

## Cost honesty (read before committing)

This process spends multiples of a direct answer's tokens — Anthropic measured multi-agent
systems at ~15× chat-level token use, and that spend is also *why* they win (token budget
explained 80% of performance variance in their research system). The trade is right for work
the user will actually use — a product, a document that matters, a plan they'll execute. It is
wrong for anything you could answer well in one pass. When the
request is genuinely small, say you're answering directly and why. When in doubt for mid-sized
work, run the **small configuration** (see Scaling, below) rather than skipping the loop.

## The loop at a glance

```
Phase 0  FRAME      you: brief + rubric + section split + loop budget
Phase 1  DRAFT      N agents in parallel, one per section
Phase 2  CRITIQUE   fresh critics cross-review sections (never their own) + red team attacks the whole
Phase 3  REVISE     revisers apply/decline critiques, steal sibling ideas
Phase 4  INTEGRATE  one agent merges sections into Version N, smooths seams
Phase 5  JUDGE      fresh judge scores vs rubric → SHIP, or ITERATE with directives → back to Phase 1
Phase 6  DELIVER    final version + how it evolved
```

Full prompt templates for every role are in [references/roles.md](references/roles.md) — use
them, filling every placeholder. The templates encode hard-won rules (critics must anchor to
the rubric, revisers must decline-with-argument rather than ignore, judges score before
comparing) that casual re-phrasings tend to lose.

**Run directory layout** (the templates' paths depend on this — follow it exactly). A
*cycle*'s critiques sit beside the drafts they review; its revisions, integrated version, and
verdict land in the next round directory. So a 1-cycle run ends in `round-2/`:

```
brief.md                      Phase 0
round-1/draft-*.md            cycle 1: independent first drafts
round-1/critique-*.md         cycle 1: critiques of those drafts
round-1/redteam.md            cycle 1: red team on the whole set
round-2/draft-*.md            cycle 1: revised sections
round-2/version.md            cycle 1: integrated Version 1
round-2/verdict.md            cycle 1: judge → SHIP or ITERATE
round-2/critique-*.md ...     cycle 2 (if ITERATE): critics review the round-2 drafts,
round-3/draft-*.md ...        revisers apply critiques + the round-2 verdict's directives,
round-3/version.md, verdict.md   and the judge closes cycle 2 in round-3/
```

Fresh drafters exist only in cycle 1; from cycle 2 on, Phase 1's work is done by revisers
following the previous verdict's directives.

## Phase 0 — Frame (you, in the main conversation)

Do not spawn anything yet. First create a run directory
(`<scratchpad>/agent-team/<project-slug>/`) and write `brief.md` containing:

1. **Goal** — one paragraph: what's being made, for whom, and what "done" means.
2. **Audience & constraints** — who consumes this, format, length, stack, tone, deadline-driven
   scope cuts. Pull constraints from the user's message and the repo's CLAUDE.md; if a
   constraint is genuinely ambiguous AND getting it wrong would waste the whole run, ask the
   user now — one question round, before the team launches, never during.
3. **Quality rubric** — 5-7 criteria the finished work must meet, each *measurable by a reader*
   ("every claim has a source", "a first-time visitor understands the offer in 10 seconds",
   "runs end-to-end from a fresh clone"), not vibes ("high quality", "engaging"). The rubric is
   the contract for the whole loop: critics cite it, the judge scores it, ship/iterate hangs on
   it. A weak rubric makes every later phase noise — spend real effort here. For code, always
   include gate criteria: "tests pass" and "runs end-to-end" (scored 1 or 10, nothing between).
4. **Section split** — 2-6 sections with owner-shaped boundaries (by page, module, chapter,
   workstream). Good splits minimize overlap; every section names what is explicitly OUT of its
   scope. For code, split so sections touch disjoint files wherever possible.
5. **Loop budget** — default 2 cycles; 3 for large or user-emphasized-quality work; 1 cycle
   (draft → critique → revise → integrate → judge, no second loop) for small work. Also set
   the bar: judge verdict SHIP requires every criterion ≥ 8/10 by default.

If facts are missing (market data, API docs, competitor examples), spawn 1-3 researcher agents
in parallel now (template in roles.md) and have drafters read their digests.

## Phase 1 — Draft (parallel)

Spawn one drafter per section **in a single message** so they run concurrently. Each drafter
reads `brief.md`, owns exactly one section, produces a *complete* draft (not an outline), and
ends with two blocks: `## Decisions I made` and `## Ideas for other sections` (up to 3). That
second block is the team talking to each other — it's how a good idea born in the pricing
section reaches the hero section. Drafts are written to `round-1/draft-<slug>.md`; agents
return only summaries, keeping your context small.

First drafts are independent by design: drafters see the brief and research, never each
other's in-progress work. Cross-pollination happens *after* drafts exist (critique and
revision phases). This ordering matters — models exposed to peer answers before forming their
own conform to them, which destroys the diversity the loop feeds on.

## Phase 2 — Critique (parallel, fresh eyes)

When all drafts land, spawn critics — **fresh agents, never the drafter re-reading its own
work in the same conversation**. Assignment rule: no critic reviews a section it had any hand
in writing; critics get team context by skimming the sibling drafts, not by role-playing
authorship. Every critique must anchor each complaint to a rubric criterion, the
brief, or a demonstrated error — critics who can verify cheaply (run the code, check the
number) must do so. Critiques also list *steal-worthy ideas from sibling sections*: critique
is not only fault-finding, it's the cross-pollination mechanism.

In the same parallel batch, spawn one **red-team critic** on the whole draft set: goal
substitution ("did the team quietly solve an easier problem?"), audience walk-through on their
worst day, correctness verification, required gaps, safety/compliance exposure.

Critics do not rewrite, do not invent requirements, and are told a strong section deserves a
short critique — reviewers pressed to keep finding problems start fabricating them (measured:
extra review rounds trade a little recall for ~60% more false positives). For the same reason,
critique is **one thorough pass per version**: critics don't dialogue with each other, don't
re-review after revision (the next round's fresh critics do that), and always critique the
artifact on disk — never the conversation about it.

## Phase 3 — Revise (parallel)

One reviser per section (continuity with the draft is fine here — revision, unlike critique,
benefits from knowing the intent). Each reviser must handle *every* concrete fix and relevant
red-team finding in one of exactly two ways: make the change, or decline it with a one-sentence
argument in `## Fixes declined`. Silent ignoring is the failure mode that makes loops
converge on nothing. Revisers also adopt flagged sibling ideas and — critically — preserve
what critics praised: regressions on praised material are how rounds churn.

## Phase 4 — Integrate

One integrator merges revised sections into Version N: assemble per the brief's structure,
unify voice and terminology, kill duplication, resolve contradictions, make transitions and
interfaces real (for code: it builds and the pieces actually call each other). Integration
means one strong voice, not the average of five voices.

## Phase 5 — Judge (fresh context, decides the loop)

A fresh judge scores Version N against the rubric only — 1-10 per criterion with quoted
evidence. From round 2 on, the judge scores the new version FIRST, then compares to the
previous one per criterion, flagging regressions explicitly. Judges have measured biases —
they favor the position read first and confident-sounding prose — so the templates pin them to
the rubric, and on a close call between versions the judge re-runs the comparison with the
versions in swapped order and calls it a tie unless one wins both ways.

- **SHIP** when every criterion ≥ bar and nothing regressed.
- **ITERATE** otherwise, with 3-5 numbered directives, each naming a target section and the
  rubric criterion it serves. Directives are the next round's marching orders — concrete,
  no new scope, no relitigating settled calls.
- **Stop regardless** when the loop budget is spent, or when a round's scores improved by less
  than ~1 point total (diminishing returns — more rounds now add cost, not quality). When the
  budget ends the loop, the judge names the best version produced; it is not always the last.

Then loop: directives feed Phase 1 revisions of the next round.

## Phase 6 — Deliver

Ship the final version where it belongs (repo files, document, artifact — per the brief), then
report to the user: the outcome first, then a short **How it evolved** note — what the critics
caught, what the red team caught, what changed between rounds, final judge scores, and anything
the judge still flags at ship time. Honest scores, including sub-bar ones when the budget ended
the loop. Keep the run directory intact; it's the audit trail.

## Scaling the team

| Project size | Sections | Critics | Red team | Cycles | Example |
|---|---|---|---|---|---|
| Small (single doc/page/module) | 2-3 | 1 shared | same sitting | 1 | one landing page, a policy doc |
| Medium (default) | 3-4 | 1 per section | 1 | 2 | multi-page site, feature with tests, full plan |
| Large / "best possible" | 4-6 | 1 per section | 1 per cycle | 3 | product build, compliance program, book-length doc |

**Small configuration, operationally:** one critic sitting reviews every section — one
critique file per section using the Critic template — and then also writes `redteam.md`
using the Red-team template, in the same sitting. File names and reviser read-lists stay
identical to the larger configurations; only the number of agents shrinks. The "never your
own work" rule still binds whoever plays the critic.

Under-scaling wastes the setup; over-scaling wastes tokens on coordination. More agents help
breadth (more sections, more angles); more rounds help depth (harder integration, subtler
fixes). Past 3 rounds, spend the tokens on a better rubric instead.

## Mechanics: how to actually run it

**Default — Agent tool.** Orchestrate from the main conversation: each phase's agents go out
as parallel Agent calls in one message; you sequence the phases as results land. All artifacts
live in the run directory; agents read/write files and return short summaries, so your context
stays small no matter how big the project is. Check the Agent tool actually exists in your
current toolset before promising this mode — nested subagents and some environments don't
have it, and the fallback below is the plan for them, not an apology.

**Heavy mode — Workflow tool.** For large configurations, run the loop as a deterministic
script: see [references/workflow-script.md](references/workflow-script.md) for a ready
launch-and-adapt template (the user's invocation of this skill is the opt-in that authorizes
Workflow). Prefer it when rounds ≥ 2 and sections ≥ 4, or when the user wants to watch
progress phase-by-phase.

**No-subagent fallback.** In environments without the Agent tool, run the same loop in-thread
as sequential "sittings", one role at a time. The file boundary substitutes for the context
boundary: every artifact goes to its file, and before the two roles where fresh eyes are
load-bearing — critic and judge — re-read the artifact under review from disk and work only
from what the file says, never from your memory of writing it. (Inputs you just wrote and
that are verbatim in context don't need ceremonial re-reads for the other roles.) Be honest
about the fallback's one real limit: in-thread, later drafters inevitably have earlier drafts
in context, so draft ALL sections before critiquing any, and lean harder on rubric anchoring
to compensate for the lost independence. "Return only:" lines in the templates apply to
spawned agents; in-thread, just move to the next sitting.

**Code-project specifics.** The governing principle is *parallelize reads, serialize writes*:
research, review, and critique fan out freely, but implementation is partitioned by strict
file ownership — sections = modules/features on disjoint files (worktrees only when overlap
is unavoidable), and one integrator owns the merge. Parallel writers who can't see each other
make conflicting implicit decisions; ownership boundaries are what prevent that. Critics run
the code and tests — a critique of unexecuted code is an opinion. Judge gates on "tests pass"
and "runs end-to-end". The integrator gets the whole thing building before the judge sees it.

## Failure modes to watch (each of these has burned real runs)

- **Rubber-stamp critique** — critiques with no rubric citations. Re-spawn the critic with the
  anchoring requirement restated; don't accept "looks good" from a critic in round 1.
- **Regression churn** — round 2 undoes round 1's praised material. The reviser's "preserve
  what works" list and the judge's regression flag exist for this; treat a flagged regression
  as the next round's first directive.
- **Scope creep via critique** — critics inventing requirements. The brief is the boundary;
  "consider adding X" goes to the user as an option at delivery, not into the loop.
- **Goal drift by the judge** — the judge grading its own taste instead of the rubric. The
  judge prompt pins it to the rubric; if scores and rubric visibly disagree, fix the rubric
  with the user, not the judge.
- **Convergence theater** — every agent politely agreeing by round 2. The red team exists to
  keep pressure on; if the red team finds nothing two rounds running, ship.
- **Lost seams** — great sections, incoherent whole. That's an integrator failure, not a
  drafter failure; strengthen the integration pass rather than adding rounds.

## Quick reference

- Templates: [references/roles.md](references/roles.md)
- Workflow script: [references/workflow-script.md](references/workflow-script.md)
- Evidence & trend research behind the design: [references/research.md](references/research.md)
