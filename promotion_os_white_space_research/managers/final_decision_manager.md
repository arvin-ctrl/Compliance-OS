# Final Decision Manager

## Inputs

- master capability matrix
- category summaries
- candidate white spaces
- red-team report
- evidence ledger

## Decision standard

Do not recommend building because the concept is technically interesting.

Recommend GO only when at least one opportunity:

1. scores >=80/100 under the white-space framework
2. survives Red Team
3. has a specific enterprise buyer
4. has a strong add/switch rationale
5. is materially different from incumbent promotion management
6. cannot be cheaply replicated with generic policy infrastructure + normal counsel
7. has a believable path to defensibility

## Final verdict

Choose exactly one:

### GO
A large, defensible opportunity is supported by current evidence.

### PIVOT
The original thesis is not large enough, but a materially different adjacent
opportunity survives.

### KILL
No opportunity currently justifies significant development.

## Required final artifacts

### `outputs/final/final_decision.md`
Detailed analysis.

### `outputs/final/executive_summary.md`
Maximum 2 pages worth of text containing:

- verdict
- top surviving opportunity
- buyer
- current stack
- pain
- why incumbents fail
- switching reason
- moat
- biggest risk
- next validation step

If verdict is KILL, explain what evidence would have to change to reopen the project.
