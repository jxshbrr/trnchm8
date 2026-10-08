# How we build

The loop for every phase, so work stays small, reviewable and on-design.
Phases and their status are in [roadmap.md](roadmap.md).

## The loop

1. **Plan the phase.**
   Write `docs/phases/NN-name.md` from the [template](phases/README.md) right before the phase starts.
   It uses whatever the previous phases taught us, so later plans are not written in advance.
   The plan is reviewed and approved before any code.
2. **Split it into slices.**
   A slice is the smallest piece that works end to end and can be demoed, such as "paste a wallet in Telegram and its trades appear in the database".
   Each slice is one branch and one pull request.
3. **Build one slice at a time on the critical path.**
   Branch from `main` as `pNN/short-name`, keep the branch short-lived, and merge back as soon as it passes the gate.
   There are no long-lived phase branches.
4. **Gate every pull request.**
   Lint, typecheck, unit tests, Storybook screenshot tests, build, and an E2E run of the flow the slice touches.
   The `no-mistakes` pipeline runs the gate and opens the PR.
   `main` is always deployable.
5. **Check in at the end of the phase.**
   A demo you can watch, the exit criteria from the roadmap ticked off, the roadmap status updated, and anything learned carried into the next phase plan.

## Parallel work and worktrees

- Parallel work is the exception, used only for tracks a phase plan names as independent, such as the Phase 0 spikes or the design system next to auth in Phase 1.
- Each track runs in its own git worktree and branch, so agents never share a working copy.
- Every track owns a set of files written down in the phase plan.
  Shared contracts (schema, shared types, tokens) land on `main` first, then the tracks build on them.
- Tracks merge back one at a time, each through the normal gate.

## Changing the plan

- Anything that changes the spec or architecture gets a short decision record in [decisions/](decisions/) first, then the docs are updated to match.
- Small, reversible choices inside a slice don't need a record.

## Design

- UI follows [design/DESIGN.md](../design/DESIGN.md) and uses only tokens from `design/tokens.json`.
- A new screen starts as a mockup on the canvas, gets approved, then gets built.
- A new component gets a Storybook story covering its states before it is used on a page.
- Screenshot tests at mobile and desktop widths, in dark and light, catch drift.

## Environments

- **Local:** your own Convex dev deployment and test bots (one Telegram bot, one Discord app).
- **Preview:** a Vercel preview and a Convex preview deployment per pull request.
- **Production:** `main`, deployed on merge.

## Commits

- Small commits with clear messages.
- No agent co-author lines.
- Never edit generated files by hand.
