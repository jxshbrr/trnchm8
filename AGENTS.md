# TrenchM8

A proactive memecoin trading journal: wallets are tracked automatically, M8 texts the trader on Telegram (Discord shortly after launch) after a session, and their reply becomes the journal.

## Read before working

- [docs/workflow.md](docs/workflow.md): how every phase and pull request runs. Read it before starting any work.
- [docs/roadmap.md](docs/roadmap.md): which phase is current and what it must ship.
- The current phase plan in [docs/phases/](docs/phases/): do only what it lists.
- [docs/spec.md](docs/spec.md) and [docs/architecture.md](docs/architecture.md): what we're building and how.
- [design/DESIGN.md](design/DESIGN.md): read it before any UI work.

## Rules

- Never change a locked decision without a record in [docs/decisions/](docs/decisions/).
- UI uses tokens from `design/tokens.json` only: no raw hex colors or one-off sizes.
- Numbers come from code, words come from the LLM: M8 never computes stats in a prompt.
- Every Convex query and mutation takes the user from auth, never from arguments.
- Don't use the em dash in copy or docs.
- Don't edit generated files by hand.
- The mockups in `design/mockups/` mirror the published canvas; change them only as part of a design task.

## Agent skills

### Issue tracker

GitHub Issues on `jxshbrr/trnchm8`, through the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Triage labels

The five defaults: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: one root `CONTEXT.md` for the glossary. See `docs/agents/domain.md`.

### Decision records

What the skills call ADRs are the decision records in `docs/decisions/`.
There is no `docs/adr/`: never create one, even when a skill's own instructions say to.
Write them with the template and numbering in `docs/decisions/README.md`, not the skills' ADR format.
