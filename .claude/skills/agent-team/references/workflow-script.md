# Heavy mode: running the loop with the Workflow tool

Use this when the project is big enough that deterministic orchestration pays off (≥4 sections,
2-3 rounds, or the user asked for maximum quality). The Workflow tool runs a script that spawns
and sequences the agents for you — the loop control (rounds, stop conditions) becomes code
instead of judgment calls mid-conversation. Invoking the agent-team skill is the opt-in that
authorizes calling Workflow.

Before Phase 1, you (the main conversation) still do Phase 0 yourself: write `brief.md` with
the rubric and section decomposition into the run directory, then launch the workflow with the
section list as `args`. After the workflow returns, you still do Phase 6 (deliver) yourself.

Notes that keep the script working:
- The script's directory layout is intentionally SIMPLER than the roles.md fallback layout:
  here each `round-N/` is self-contained (drafts, critiques, redteam, version, verdict all in
  one dir), because revision happens inside the next round's draft stage. Both layouts are
  fine — every prompt embeds its full paths — just don't mix conventions inside one run.
- Scripts are plain JavaScript, no TypeScript syntax.
- `Date.now()` / `new Date()` / `Math.random()` are unavailable inside scripts — the run
  directory path is created BEFORE launching and passed in via `args`.
- Round phases use real barriers (`parallel`) deliberately: critics must see ALL drafts of a
  round (cross-pollination), the judge must see the integrated version. This is the case where
  barriers are correct — stage N genuinely needs every stage N-1 result.
- Agents write artifacts to files in the run directory; `agent()` return values carry only
  small summaries/scores. The judge uses a `schema` so loop control never parses prose.
- `.filter(Boolean)` after every `parallel` — a skipped/dead agent resolves to null.

## Launch call

```
Workflow({
  args: {
    runDir: "<absolute run dir you already created, containing brief.md>",
    sections: [
      { name: "Landing page hero + copy", slug: "hero" },
      { name: "Pricing section", slug: "pricing" },
      { name: "Backend signup flow", slug: "signup" }
    ],
    bar: 8,
    maxRounds: 3
  },
  script: <the script below>
})
```

## The script

```javascript
export const meta = {
  name: 'agent-team-loop',
  description: 'Draft in parallel, cross-critique, revise, integrate, judge — loop until the bar is met',
  phases: [
    { title: 'Round 1', detail: 'draft → critique + red team → revise → integrate → judge' },
    { title: 'Round 2', detail: 'directed revision loop' },
    { title: 'Round 3', detail: 'final revision loop' },
  ],
}

const { runDir, sections, bar = 8, maxRounds = 3 } = args
const VERDICT = {
  type: 'object',
  properties: {
    scores: { type: 'array', items: { type: 'number' } },
    minScore: { type: 'number' },
    regression: { type: 'boolean' },
    verdict: { type: 'string', enum: ['SHIP', 'ITERATE'] },
    directives: { type: 'array', items: { type: 'string' } },
  },
  required: ['scores', 'minScore', 'regression', 'verdict', 'directives'],
}

// Role prompts live in the skill's references/roles.md; the strings below are the compact
// workflow-adapted forms. {runDir} paths let every agent find its inputs on disk.
const draftP = (s, r) =>
  `You are the DRAFTER for section "${s.name}" of a team project, round ${r}. ` +
  `Read ${runDir}/brief.md (brief + rubric)` +
  (r > 1 ? ` and ${runDir}/round-${r - 1}/verdict.md (judge directives — they outrank all else), ` +
    `then revise ${runDir}/round-${r - 1}/draft-${s.slug}.md addressing every critique in ` +
    `${runDir}/round-${r - 1}/critique-${s.slug}.md and the red-team findings for your section in ` +
    `${runDir}/round-${r - 1}/redteam.md. Adopt steal-worthy ideas critics flagged. Preserve what ` +
    `critics praised. Address each fix or decline it with one argued sentence under "## Fixes declined".`
   : `. Write a complete first draft of ONLY your section. Other agents own the other sections: ` +
    sections.filter(x => x.slug !== s.slug).map(x => x.name).join('; ') +
    `. End with "## Decisions I made" and "## Ideas for other sections" (max 3, 1-2 sentences each).`) +
  ` Write the draft to ${runDir}/round-${r}/draft-${s.slug}.md. Return only a 3-bullet summary.`

const critiqueP = (s, r) =>
  `You are a fresh-context CRITIC. You did not write any of this — that's deliberate. Read ` +
  `${runDir}/brief.md, then review ${runDir}/round-${r}/draft-${s.slug}.md against the rubric; ` +
  `skim sibling drafts in ${runDir}/round-${r}/ for fit and steal-worthy ideas. Structure: ` +
  `"## Verdict in one line", "## What genuinely works" (specific — the reviser treats it as a ` +
  `do-not-cut list), "## Rubric failures" (each anchored to a criterion + quoted evidence — no ` +
  `vibes; verify claims cheaply where possible, e.g. run code), "## Steal-worthy ideas from ` +
  `sibling sections", "## Concrete fixes" (numbered, most important first, each actionable). ` +
  `Do not rewrite it; do not invent requirements; if it is strong, say so briefly — this is your ` +
  `one pass, and manufacturing complaints is worse than a short critique. ` +
  `Write to ${runDir}/round-${r}/critique-${s.slug}.md. Return the one-line verdict + failure count.`

const redteamP = (r) =>
  `You are the RED TEAM. Read ${runDir}/brief.md then every draft in ${runDir}/round-${r}/. Attack: ` +
  `(1) goal substitution — where did the team solve an easier problem than the brief's? (2) audience ` +
  `walk-through on their worst day; (3) correctness — verify claims/code/numbers, run what you can; ` +
  `(4) required gaps; (5) safety/compliance exposure. Report up to 10 findings, numbered, most ` +
  `damaging first — fewer rather than manufactured, each with evidence and the smallest defusing ` +
  `change. Write to ${runDir}/round-${r}/redteam.md. Return your top 3 findings as one-liners.`

const integrateP = (r) =>
  `You are the INTEGRATOR. Read ${runDir}/brief.md and every draft in ${runDir}/round-${r}/. Merge ` +
  `into one coherent version: assemble per the brief's structure, unify voice/terminology/format, ` +
  `kill duplication, resolve cross-section contradictions per the brief, strip the working blocks ` +
  `("## Decisions I made", "## Ideas for other sections", "## Fixes declined" stay in the draft ` +
  `files, not the deliverable), make transitions and interfaces real (code must actually ` +
  `build/import correctly). One strong voice, not an average of voices. Write the assembled ` +
  `version to ${runDir}/round-${r}/version.md; when the deliverable's real format isn't markdown, ` +
  `put the real files where the brief names and make version.md the manifest (what lives where + ` +
  `build/test status). Return integration changes + unresolved conflicts for the judge.`

const judgeP = (r) =>
  `You are the JUDGE, fresh context, no stake in the work. Read ${runDir}/brief.md — the rubric is ` +
  `your ONLY standard. Score ${runDir}/round-${r}/version.md: per criterion 1-10 with quoted evidence ` +
  `(10 = could not be meaningfully improved for this audience; <5 = fails).` +
  (r > 1 ? ` Score FIRST, then read ${runDir}/round-${r - 1}/version.md and compare per criterion; flag any ` +
    `regression explicitly.` : '') +
  ` Verdict SHIP if every criterion >= ${bar} and no regression, else ITERATE with 3-5 numbered ` +
  `directives (each names a section + the rubric criterion it serves; no new scope; do not relitigate ` +
  `settled calls). On SHIP, end the report with "## Flags at ship" — non-blocking observations for ` +
  `delivery, or "none". Write the full report to ${runDir}/round-${r}/verdict.md. Return the structured verdict.`

let verdict = null
let round = 0
while (round < maxRounds) {
  round++
  const ph = `Round ${round}`
  log(`Round ${round}: drafting ${sections.length} sections in parallel`)

  // Barrier justified: critics need ALL drafts (cross-pollination), red team needs the full set.
  const drafts = (await parallel(sections.map(s => () =>
    agent(draftP(s, round), { label: `draft:${s.slug}`, phase: ph })))).filter(Boolean)
  if (!drafts.length) throw new Error('all drafters failed')

  // Critics are all fresh spawns (they drafted nothing), one per section, plus the red team.
  await parallel([
    ...sections.map(s => () =>
      agent(critiqueP(s, round), { label: `critique:${s.slug}`, phase: ph })),
    () => agent(redteamP(round), { label: 'red-team', phase: ph }),
  ])

  // Round 1 revision happens inside next round's draftP; but every round still needs an
  // integrated version for the judge, so integrate + judge now.
  await agent(integrateP(round), { label: 'integrate', phase: ph })
  verdict = await agent(judgeP(round), { label: 'judge', phase: ph, schema: VERDICT, effort: 'high' })
  if (!verdict) throw new Error('judge died — inspect the run dir and re-run')

  log(`Round ${round} judge: min score ${verdict.minScore}, verdict ${verdict.verdict}`)
  if (verdict.verdict === 'SHIP') break
  if (round === maxRounds) log(`Loop budget spent after round ${round}; shipping best version — see verdict.md`)
}

return {
  rounds: round,
  finalVersion: `${runDir}/round-${round}/version.md`,
  verdict,
}
```

## After the workflow returns

1. Read the final `version.md` (and `verdict.md`) from the run directory.
2. Do Phase 6 from SKILL.md yourself: place/ship the deliverable properly, write the short
   evolution changelog, report scores honestly — including a verdict of "budget spent, best
   version was round N" when the judge never said SHIP.
3. If the user then asks for another push, resume cheaply: relaunch with
   `resumeFromRunId` and a raised `maxRounds` — completed rounds return from cache.

## Adapting the script

- **Code projects**: add `isolation: 'worktree'` to drafter/reviser agents ONLY if sections
  touch overlapping files; prefer decomposing so they don't. Give the judge a gate: tests
  pass = scored, tests fail = automatic ITERATE regardless of other scores.
- **Research-heavy projects**: add a Phase-0-style `parallel` of researcher agents before the
  loop, writing `research-*.md` files the drafters are told to read.
- **Tight budget**: `maxRounds: 2`, drop the red team, one critic for two sections. The
  draft → fresh critique → revise → judge core is the part that must survive any cut.
