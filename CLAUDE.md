# Compliance-OS — working agreements for Claude

## Default working style: the agent-team loop

For any **project-scale** request in this repo — building an app or feature, writing a
document, plan, strategy, or report, designing pages or systems — use the `agent-team` skill
(`.claude/skills/agent-team/`) rather than answering in a single pass. That skill runs the
work through a team of parallel agents that draft, cross-critique each other with fresh eyes,
revise, and loop under an independent judge until the quality bar is met. This is the owner's
standing preference: projects here always take that path.

Answer directly (no team) only for quick questions, single-file edits, small fixes, and
conversational turns.

## Conventions

- Temporary run artifacts from agent-team loops belong in the session scratchpad, not the
  repo. Only deliverables get committed.
- When a loop ships work, include the "How it evolved" summary in the PR description.
