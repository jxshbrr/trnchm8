# Domain Docs

How the engineering skills should read and write this repo's domain documentation.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root: the glossary.
- **`docs/decisions/`**: the decision records that touch the area you're about to work in. The skills call these ADRs.
- **`docs/spec.md`** and **`docs/architecture.md`**: what we're building and how.

If `CONTEXT.md` doesn't exist yet, **proceed silently**.
Don't flag its absence or suggest creating it upfront.
The `/domain-modeling` skill (reached via `/grill-with-docs` and `/improve-codebase-architecture`) creates it when the first term is resolved.

## File structure

Single-context repo:

```
/
├── CONTEXT.md
└── docs/
    ├── decisions/
    │   ├── README.md                         ← template, open and decided tables
    │   ├── 0011-trade-closing-and-thesis.md
    │   └── ...
    ├── spec.md
    └── architecture.md
```

There is no `docs/adr/`.
Never create one, even when a skill's own instructions say decisions live there.

## Writing a decision record

- Use the template in `docs/decisions/README.md`, not the skills' ADR format.
- Settling an open decision (the README's open table, 0001-0010) keeps its reserved number.
- A new decision takes the next number after the highest one in the README.
- Move it from the open table to the decided table in the same change.
- A decision that changes the spec or architecture is written first, then the docs are updated to match (see `docs/workflow.md`).

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in `CONTEXT.md`.
Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, that's a signal: either you're inventing language the project doesn't use (reconsider) or there's a real gap (note it for `/domain-modeling`).

## Flag decision conflicts

If your output contradicts an existing decision record, surface it explicitly rather than silently overriding:

> _Contradicts 0012 (wallets and transfers), but worth reopening because…_
