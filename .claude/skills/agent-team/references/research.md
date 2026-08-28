# Research: why the agent-team loop is built the way it is

Compiled 2026-08-28 from three parallel research passes: (1) the two X posts the workspace
owner shared as reference points, (2) industry multi-agent orchestration patterns and the
2026 practitioner trend, (3) the academic literature on critique loops — including the
counter-evidence. Every claim carries a source; secondary/social-source numbers are flagged.

## Table of contents

1. [The two reference posts, decoded](#1-the-two-reference-posts-decoded)
2. [The big picture: where the field landed in 2026](#2-the-big-picture-where-the-field-landed-in-2026)
3. [Named orchestration patterns](#3-named-orchestration-patterns)
4. [What the viral demos actually do](#4-what-the-viral-demos-actually-do)
5. [The science of critique loops — what works](#5-the-science-of-critique-loops--what-works)
6. [The counter-evidence — when critique loops fail](#6-the-counter-evidence--when-critique-loops-fail)
7. [Design traceability: finding → rule in SKILL.md](#7-design-traceability-finding--rule-in-skillmd)
8. [Costs and failure modes](#8-costs-and-failure-modes)
9. [Sources](#9-sources)

---

## 1. The two reference posts, decoded

**Post 1 — @0xJokker (Aug 27, 2026).** A Spanish-subtitled repost of Anthropic's viral
~37-minute guide video on building AI agent teams that "automate an entire company" — agents
that divide up tasks among themselves and execute autonomously (the same video went viral in
English via @mikenevermiss on Aug 9, 2026; secondhand descriptions frame it as configuring
Claude as a "Company OS" with ~four specialist agents covering research, writing, sales, and
operations coordinating from one setup). The takeaway the post is selling: **specialist
agents + task division + autonomous execution**.

**Post 2 — @choopyplug1 (Aug 16, 2026).** A widely-bookmarked X Article titled *"Harness
Engineering: the skill that replaced prompt engineering in 2026"* (~355k views). Its argument:
in 2024 the skill was prompts, in 2025 context, in 2026 it's **the harness** — everything
around the model. It names seven layers: tool orchestration, **verification loops ("separate
maker from checker")**, context & memory, guardrails, observability, routing/model selection,
and **feedback/self-improvement**. Closing line: "Skip one and you have a demo. Build all
seven and you have a system that gets better every time it runs." The term "harness
engineering" traces to Mitchell Hashimoto (Feb 2026) and is echoed across 2026 industry
writing.

Together the two posts are the owner's spec in the wild: *a team of specialists that divide
work* (post 1) wrapped in *maker≠checker verification loops that make the system improve
every run* (post 2). That is precisely the shape of this skill.

## 2. The big picture: where the field landed in 2026

The 2025-2026 literature organizes around one axis: **who holds the control flow.**
Anthropic's canonical "Building Effective Agents" (Dec 2024) distinguishes *workflows*
(LLMs orchestrated through predefined code paths) from *agents* (LLMs directing their own
process), and advises starting with the simplest thing that works.

Two landmark posts staked out the poles, and the field synthesized them:

- **For multi-agent:** Anthropic's "How we built our multi-agent research system" (June 2025)
  — an orchestrator (Opus) spawning 3-5 parallel subagents (Sonnet) **outperformed
  single-agent Opus by 90.2%** on their internal research eval. Cost: agents use ~4× the
  tokens of chat; **multi-agent systems ~15×**. Token spend itself explained 80% of
  performance variance — multi-agent architectures work largely because they buy more
  focused thinking in parallel context windows.
- **Against (by default):** Cognition's "Don't Build Multi-Agents" (June 2025) — parallel
  subagents that can't see each other's work make **conflicting implicit decisions** and
  merge incoherently. Principles: share full traces; actions carry implicit decisions.
- **The 2026 synthesis:** *parallelize reads, serialize writes.* Fan out research, review,
  critique, and exploration; keep implementation single-threaded or partitioned by strict
  ownership boundaries. Context engineering decides which side any given task is on.

Meanwhile every major vendor converged on shipping BOTH an LLM-routed mode and a
deterministic loop/graph mode: LangGraph's cyclic graphs and supervisor pattern, OpenAI's
Agents SDK (handoffs, agents-as-tools, while-loop-with-evaluator as recommended code
orchestration), Microsoft Agent Framework (AutoGen + Semantic Kernel merged, 1.0 in Apr
2026, pairing "Agent Orchestration" with deterministic "Workflow Orchestration"), Google
ADK (SequentialAgent / ParallelAgent / **LoopAgent** — the generate-critique loop as a
literal class), CrewAI (role-based crews + hierarchical manager + Flows). Claude Code ships
the same trio natively: **subagents** (isolated context, summary back), **agent teams**
(peer sessions with a shared task list and mailboxes — the "swarms" feature), and **dynamic
workflows** (a script orchestrates dozens-to-hundreds of agents deterministically, with
convergence-loop idioms like "keep fixing until the type check passes or two rounds in a
row make no progress" in the docs themselves).

The consistent honest finding across field reports: throughput is real, **verification is
the bottleneck**, and unreviewed swarm output is frequently broken. The MAST failure
taxonomy (Berkeley, NeurIPS 2025; 14 failure modes from 1,600+ annotated traces across 7
frameworks) found most multi-agent failures are **system-design failures** — agents
ignoring peer input, wrong assumptions, missing verification — not model-capability
failures. Design the harness, get the gains.

## 3. Named orchestration patterns

The vocabulary, from Anthropic's pattern catalog unless noted:

| Pattern | One-liner | Use when |
|---|---|---|
| Prompt chaining | Fixed sequence of calls, gates between steps | Task decomposes cleanly into fixed subtasks |
| Routing | Classify input → specialized handler | Distinct categories handled better separately |
| Parallelization: sectioning | Independent subtasks run simultaneously | Speed on divisible work |
| Parallelization: voting | Same task run N times, aggregate | Confidence via diverse attempts |
| Orchestrator-workers | Central LLM decomposes dynamically, delegates, synthesizes | Subtasks can't be predicted upfront |
| Evaluator-optimizer | Generator + evaluator in a loop until pass/budget | Clear criteria + iteration measurably helps |
| Supervisor / hierarchical (LangGraph) | Agents as graph nodes; supervisor routes; cycles allowed | Team topologies, reflection loops |
| Handoffs / swarm (OpenAI SDK) | Peers transfer control directly, no central boss | Specialist should own the conversation |
| Group chat (AutoGen/AG2) | Shared thread, manager picks next speaker | Turn-based debate, writer/editor/critic |
| Plan-execute-reflect | Planner → executors → re-planner | Long tool workflows, cost control |
| Fixed-prompt loop ("Ralph Wiggum") | Re-feed the same prompt; state lives in files/git | Well-defined tasks with automatic verification |

**This skill composes four of them**: orchestrator-workers (Phase 0-1), parallelization-
sectioning (Phase 1) with fresh-eyes cross-review (Phase 2), evaluator-optimizer as the
outer loop (Phase 5), and plan-execute-reflect memory via round verdicts feeding the next
round's drafts.

Key production lessons from Anthropic's research system that the role templates encode:
delegate with **explicit objective, output format, tool guidance, and task boundaries**
(vague delegation → duplicated/dropped work); **scale effort to complexity by rule**
(simple = 1 agent / 3-10 tool calls; complex = 10+ subagents with divided responsibilities);
search wide-then-narrow; use durable artifacts and checkpoints because stateful errors
compound.

## 4. What the viral demos actually do

The demo grammar behind the 2026 wave of agent-swarm videos, decomposed:

1. **16 parallel Claudes build a C compiler** (Anthropic engineering, Feb 2026). 16 agents,
   *no orchestrator at all*: task claiming via lock files in a shared git repo (a merge
   conflict = "pick another task"). ~2,000 sessions, ~$20k, → a 100k-line Rust C compiler
   that builds Linux 6.9 on three architectures and passes ~99% of GCC's torture tests.
   The load-bearing insight: **an independent, high-quality test suite was the coordination
   mechanism**. Regressions were the recurring failure; monolithic tasks stalled the swarm
   until decomposed.
2. **Gas Town + Beads** (Steve Yegge, Jan 2026). 20-30 parallel coding agents with named
   roles — Mayor (chief of staff), Polecats (workers), **Witness (patrol/monitor), Refinery
   (merge-queue serializer)** — over a git+SQLite issue/memory ledger (Beads) that solves
   agents' "no memory between sessions" problem. Field tests: real autonomous PR flow at
   ~$100/hour, and when review gates were missing it merged broken PRs — verification again.
3. **Ralph Wiggum loops** (Geoffrey Huntley → official Claude Code plugin). `while true` re-
   feeds one fixed prompt; each iteration sees its own past work in the files; exits on a
   completion promise or max-iterations. Viral claims (6 repos overnight; "$50k contract for
   $297") come with the plugin's own caveat: works on well-defined tasks with **automatic
   verification**; burns without progress when success criteria are fuzzy.
4. **Worktree orchestrator dashboards** (Conductor, Vibe Kanban, Claude Squad, …): N agents,
   each in an isolated git worktree, kanban/diff UI on top — the mainstreamed form of
   parallel agents, endorsed by Claude Code's own worktree docs.
5. **claude-flow / Ruflo** ("hive-mind"): Queen-led swarm over shared SQLite memory — the
   maximalist GitHub take on persistent swarm memory.
6. **Claude Code agent teams**: the shipped "swarms" feature — teammates with own contexts,
   shared task list, direct messaging, and hook-based quality gates (a `TaskCompleted` hook
   exiting 2 = a programmable critic that blocks completion). The docs' signature demo is
   five teammates instructed to **disprove each other's theories "like a scientific
   debate"** — adversarial peers as an anchoring-bias defense.

Common grammar: (a) parallel isolated workspaces; (b) a shared durable task/artifact ledger
instead of chat; (c) **reviewer/verifier agents gating a merge**; (d) a loop that re-prompts
with critique or test failures until green; (e) a status dashboard. The skill's run
directory + role structure is this grammar, sized for one session.

## 5. The science of critique loops — what works

- **Reflexion** (Shinn et al., NeurIPS 2023): act → external failure signal → verbal
  self-reflection stored in memory → retry. HumanEval 80%→91%; hallucinated actions in
  failures fell 32%→3%. The trigger is an *external* signal — tests, environment success.
- **Self-Refine** (Madaan et al., NeurIPS 2023): generate → self-feedback → refine, ~20%
  average improvement across 7 tasks — but gains concentrate where quality is
  *rubric-improvable* (style, coverage, code readability), and actionable, specific feedback
  is the binding constraint.
- **CRITIC** (Gou et al., ICLR 2024): critiques grounded in tools (search, interpreter):
  +7 points where ungrounded self-talk lost points. The paper's own words: relying on
  self-correction without external feedback "may result in modest improvements or even
  deteriorated performance."
- **Multi-agent debate** (Du et al., ICML 2024): 3 agents × 2 rounds reading each other's
  answers beat both single-agent and single-agent reflection (GSM8K 77→85; notably,
  *solo reflection made GSM8K and MMLU worse*). Gains saturate by ~4 rounds.
- **LLM-as-a-Judge** (Zheng et al., NeurIPS 2023): a strong judge agrees with human
  preference >80% — human-level in aggregate — but has measured biases: **position bias**
  (only ~65% position-consistent uncontrolled), **verbosity bias**, **self-enhancement
  bias**, and weak math grading that reference-anchoring fixed (failure rate 70%→15%).
  Mitigations: pairwise with position swap (win both orders or it's a tie), rubric/reference
  anchoring, CoT judging.
- **Tree/Graph of Thoughts** (Yao et al.; Besta et al.): treat intermediate ideas as a
  searched population — evaluate states, prune, backtrack, and (GoT) *merge* partial
  solutions. Game of 24: 4%→74%. Evaluator quality bounds everything.
- **STORM / Co-STORM** (Stanford, NAACL 2024): the real multi-agent *writing* pipeline —
  perspective-conditioned agents interview a grounded expert agent, then curate an outline
  before prose. +25% on organization vs an outline-driven baseline. Highest-leverage
  iteration target: **the outline (structure), not sentence polish**.
- **Mixture-of-Agents** (Wang et al., 2024): layers where each agent sees all previous-layer
  drafts; open models beat GPT-4o on AlpacaEval 2.0 (65.1% vs 57.5%). 2025 correction
  (**Self-MoA**): aggregating N samples from your *best* model beat mixing weaker models
  (+6.6%) — diversity pays only above a quality floor.
- **FunSearch / AlphaEvolve** (DeepMind, Nature 2023 / May 2025): the strongest
  self-improvement results in existence — new mathematics, a Strassen-beating matmul
  algorithm, 0.7% of Google's fleet compute recovered — all share one architecture:
  **generator + cheap objective automated evaluator + population-level selection**. No
  verbal self-critique anywhere.

## 6. The counter-evidence — when critique loops fail

This is the half most viral demos skip, and it shaped the skill's rules more than the
positive results did:

- **Ungrounded self-correction is net negative on reasoning.** Huang et al. (ICLR 2024):
  "review your answer" with no external signal took GPT-4 GSM8K from 95.5% → 89.0% over two
  rounds; models flip correct answers to wrong more often than the reverse. Earlier positive
  results leaked ground truth via oracle stopping.
- **The bottleneck is error *detection*, not correction.** Tyen et al. (ACL 2024): given the
  error's location, correction is robust — so put your effort into finding errors (rubrics,
  tests, fresh eyes), not into exhorting revision.
- **The self-correction blind spot.** Tsui (2025/COLM 2026): across 14 models, a 64.5% blind
  spot — models fix an error attributed to the *user* but miss the identical error they
  generated themselves. Attribution/framing is the barrier → critics must be fresh contexts
  reviewing "someone else's work."
- **Debate ≈ self-consistency at matched compute.** Huang's reframe (88.2% for
  self-consistency vs 83.0% for debate at 9 total responses) and Zhang et al. 2025 ("Stop
  Overvaluing Multi-Agent Debate," 9 benchmarks): debate often loses to sampling+voting at
  equal budget. Model/role heterogeneity is the one consistent improver.
- **Sycophancy and premature consensus.** Wynn et al. 2025: agents flip correct→incorrect
  to agree. Yao et al. 2025: inter-agent sycophancy collapses disagreement below
  single-agent accuracy. Bertalanič & Fortuna 2026 quantify three pathways in homogeneous
  debate: conformity (up to 85.5% modal-answer adoption), contextual fragility (peer
  rationales destabilize previously-correct reasoning), and **consensus collapse** —
  majority vote discarding correct answers already present (oracle gap up to 32.3 points) —
  while burning 2-3× the tokens.
- **More review rounds add noise.** Song 2026: single-pass fresh-context review beat every
  multi-turn variant; extra rounds bought +0.08 recall for **62% more false positives** via
  false-positive pressure (reviewers fabricate once real errors run out) and review-target
  drift (critiquing the conversation instead of the artifact).
- **Degeneration-of-Thought** (Liang et al., EMNLP 2024): a model confident in its answer
  cannot generate novel objections to it — the formal argument for external critics.
- **Self-correction is trainable but not promptable** (SCoRe, DeepMind, ICLR 2025): RL
  training flipped intrinsic self-correction from −11.2% to +4.4% on MATH — consistent with
  "don't expect prompting alone to make a model catch its own reasoning errors."

## 7. Design traceability: finding → rule in SKILL.md

| Research finding | Rule it produced |
|---|---|
| Ungrounded self-critique degrades output (Huang; CRITIC) | Critiques must anchor to rubric/brief/demonstrated error; critics verify cheaply (run code, check numbers) |
| 64.5% self-correction blind spot; Degeneration-of-Thought; self-enhancement bias | Critics and judge are always fresh contexts; nobody reviews their own section |
| Detection, not correction, is the bottleneck (Tyen) | Effort goes into the rubric, cross-review, red team — revision itself is the easy part |
| Gains saturate by rounds 2-4 (Du; Song) | Loop budget: default 2, max 3; diminishing-returns stop rule |
| Extra review rounds → false-positive flood (Song) | One thorough critique pass per version; no critic dialogues; next round gets *new* fresh critics |
| Conformity when agents see peers early (Wynn; Bertalanič) | Round-1 drafts are independent; cross-pollination only after drafts exist |
| Consensus collapse: voting discards correct answers | A judge *selects* against the rubric over all versions; no majority voting; best version may not be the last |
| Judge position bias (~65% consistency); reference anchoring fixes grading | Judge scores new version before reading old; close calls re-run with order swapped; rubric is the only standard |
| Diversity pays only above a quality floor (Self-MoA); heterogeneity helps (Zhang) | Diversity via *roles and perspectives* (sections, red team, integrator), not weaker models |
| Reflexion: external signal + memory across trials | Judge verdicts persist per round and feed the next round's drafters as directives |
| Structure beats polish for writing (STORM) | Phase 0 invests in brief/rubric/section split; critics flag structure first |
| Verification is the swarm bottleneck (C compiler; Gas Town; MAST) | Code rubrics gate on tests/runs; integrator builds before judge; MAST's "verification" category is Phase 5's job |
| Explicit objective/format/boundaries per subagent (Anthropic research system) | Role templates fill every placeholder; sections name what's OUT of scope |
| 15× token cost of multi-agent (Anthropic) | Cost-honesty section; scaling table; "answer directly" carve-out |
| Parallelize reads, serialize writes (Anthropic vs Cognition synthesis) | Parallel drafting on disjoint sections; single integrator merges; worktrees only when overlap is unavoidable |
| Maker ≠ checker as a harness layer (Harness Engineering, post 2) | The entire Phase 2/Phase 5 separation |

## 8. Costs and failure modes

- **Tokens:** agents ≈ 4× chat; multi-agent ≈ 15× chat (Anthropic). Field reports of big
  swarms: ~$100/hour (Gas Town), ~$20k for the C compiler. This skill's configurations are
  sized so a medium run stays in the low-multiple range of a single-pass answer — the
  scaling table exists to stop reflexive over-spawning.
- **When single-agent is simply better** (composite of Anthropic + LangChain + Claude Code
  docs + Cognition): sequential/high-dependency tasks, same-file edits, work fitting one
  context window, low-value tasks, anything where writes must share implicit decisions.
- **MAST's three failure categories** map to the skill's phases: system-design issues →
  Phase 0 (brief/rubric/boundaries); inter-agent misalignment → Phase 2/4 (cross-review,
  integration); task-verification failures → Phase 5 (judge with gates).
- **Judge-bias magnitudes** (practitioner compilations; secondary sources): position bias
  ~10-15 points of win-rate swing, verbosity bias 15-30 points, self-preference ~10-25%.
  Off-the-shelf generic judge metrics are widely reported as near-useless; task-specific
  binary/rubric judges validated against human judgment are the working practice.

## 9. Sources

**The two posts:** x.com/0xJokker/status/2092974589529727199 (via syndication CDN +
fxtwitter API) · x.com/choopyplug1/status/2088973320964215253 → x.com/i/article/2088576943155290112
· English original of post 1's video meme: x.com/mikenevermiss/status/2086591051041587708

**Anthropic canonical:** anthropic.com/engineering/building-effective-agents ·
anthropic.com/engineering/multi-agent-research-system ·
anthropic.com/engineering/building-c-compiler · code.claude.com/docs/en/sub-agents ·
code.claude.com/docs/en/agent-teams · code.claude.com/docs/en/workflows ·
code.claude.com/docs/en/worktrees ·
github.com/anthropics/claude-code/blob/main/plugins/ralph-wiggum/README.md

**Frameworks:** docs.langchain.com/oss/python/langchain/multi-agent · langchain.com/langgraph ·
langchain.com/blog/command-a-new-tool-for-multi-agent-architectures-in-langgraph ·
langchain.com/blog/planning-agents · docs.crewai.com (concepts/processes) ·
microsoft.github.io/autogen (group-chat pattern; conversation patterns) · docs.ag2.ai ·
learn.microsoft.com/en-us/agent-framework/overview · openai.github.io/openai-agents-python
(+ /multi_agent/) · google.github.io/adk-docs/agents/workflow-agents/ ·
en.wikipedia.org/wiki/Agent2Agent

**Practitioner trend:** ghuntley.com/ralph · theregister.com/2026/01/27/ralph_wiggum_claude_loops ·
tessl.io/blog/unpacking-the-unpossible-logic-of-ralph-wiggumstyle-ai-coding · yegge.ai/gastown ·
steve-yegge.medium.com/welcome-to-gas-town-4f25ee16dd04 ·
dolthub.com/blog/2026-01-15-a-day-in-gas-town · github.com/ruvnet/ruflo/wiki/Hive-Mind-Intelligence ·
addyosmani.com/blog/claude-code-agent-teams · infoq.com/news/2026/06/dynamic-workflows-claude-code ·
infoq.com/news/2026/02/claude-built-c-compiler · augmentcode.com/tools/open-source-agent-orchestrators ·
github.com/andyrewlee/awesome-agent-orchestrators · nimbalyst.com/blog/git-worktrees-for-ai-coding-agents-complete-guide

**Papers:** Reflexion arxiv.org/abs/2303.11366 · Self-Refine arxiv.org/abs/2303.17651 ·
CRITIC arxiv.org/abs/2305.11738 · Debate (Du) arxiv.org/abs/2305.14325 · LLM-as-Judge
arxiv.org/abs/2306.05685 · ToT arxiv.org/abs/2305.10601 · GoT arxiv.org/abs/2308.09687 ·
STORM arxiv.org/abs/2402.14207 · Co-STORM arxiv.org/abs/2408.15232 · MoA arxiv.org/abs/2406.04692 ·
Self-MoA arxiv.org/abs/2502.00674 · FunSearch (Nature, Dec 2023, deepmind.google blog) ·
AlphaEvolve (deepmind.google blog, May 2025) · Huang self-correction arxiv.org/abs/2310.01798 ·
Tyen error-location arxiv.org/abs/2311.08516 · Kamoi TACL survey arxiv.org/abs/2406.01297 ·
SCoRe arxiv.org/abs/2409.12917 · Self-Correction Bench arxiv.org/abs/2507.02778 ·
Smit MAD arxiv.org/abs/2311.17371 · Zhang Stop-Overvaluing-MAD arxiv.org/abs/2502.08788 ·
Liang DoT/MAD arxiv.org/abs/2305.19118 · Wynn arxiv.org/abs/2509.05396 ·
Yao sycophancy arxiv.org/abs/2509.23055 · Bertalanič & Fortuna arxiv.org/abs/2605.00914 ·
Song More-Rounds-More-Noise arxiv.org/abs/2603.16244 · MAST arxiv.org/abs/2503.13657 ·
Cognition cognition.com/blog/dont-build-multi-agents
