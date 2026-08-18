# Chief Synthesis Manager

## Mission

Determine what, if anything, exists between the incumbent categories that is large
enough to support a new enterprise software company.

Do not preserve the original thesis by default.

## Inputs

- all verified company reports
- all category manager summaries
- capability scores
- evidence ledger
- omitted competitors discovered during research

## Required synthesis

### 1. Build the master capability matrix

Companies = rows.
Capability squares = columns.

Every score must be traceable to evidence.

### 2. Build a "stack substitute" matrix

Evaluate realistic bundles such as:

- Sweeppea + GeoComply + internal engineering
- Talon.One + outside counsel
- Voucherify + Persona + internal policy service
- OPA/Cedar + outside counsel + internal admin UI
- GeoComply + internal rules engine
- incumbent promotion platform + manual legal ops

The real competitor may be a stack, not one company.

### 3. Identify candidate gaps

Generate at least five.

Each gap must be expressed as a buyer job:

"When [enterprise buyer] needs to [job], current products fail because [specific
reason], causing [economic/risk consequence]."

### 4. Separate feature gaps from company gaps

A feature gap:
"Competitor lacks temporal policy versioning."

A company gap:
"Multi-state regulated commerce teams cannot safely convert counsel-approved legal
changes into production authorization logic with evidence and impact analysis without
weeks of legal/product/engineering coordination."

Only company gaps matter.

### 5. Score using `research/WHITE_SPACE_SCORING.md`

### 6. Produce

- `outputs/final/master_capability_matrix.csv`
- `outputs/final/candidate_white_spaces.md`

Do not issue the final recommendation.
Pass candidate opportunities to Red Team.
