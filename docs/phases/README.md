# Phase plans

One file per phase, `NN-name.md`, written right before the phase starts and approved before any code.
Copy the template below.

```markdown
# Phase NN - Name

Status: planning | approved | in progress | done

## Goal
One or two sentences: what a user can do at the end that they couldn't before.

## Out of scope
What this phase deliberately leaves for later.

## Decisions needed first
Links to decision records this phase depends on, and any new ones it has to make.

## Design references
Mockup boards and DESIGN.md sections this phase builds.

## Data model changes
Tables, indexes and fields added or changed.

## Slices
For each slice, in order:
- **Name** (`pNN/branch-name`)
- What it does, end to end.
- Areas it touches.
- Acceptance check: how we know it works.
- Tests: unit, E2E, screenshots.

## Parallel tracks
Only if some slices are independent: which tracks, which worktree each, which files each one owns, and which shared contracts land on main first.

## Risks
What could go wrong and how we'd notice early.

## Exit criteria and demo
The checklist from the roadmap, plus the exact steps of the demo at the check-in.

## Check-in notes
Filled in at the end: what shipped, what changed from the plan, what carries into the next phase.
```
