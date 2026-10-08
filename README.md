# TrenchM8

A trading journal for memecoin traders that writes itself.

M8, an AI trading mate, watches your wallets and texts you on Telegram after you trade.
You reply in a few words or a voice note, and that reply becomes your journal.
Over time M8 shows you your own patterns, with receipts, and holds you to the rules you set.

> **Status:** pre-build.
> The product, architecture, design system and M8's doctrine are written; there is no app code yet.
> The next step is the Phase 0 spikes. See [docs/roadmap.md](docs/roadmap.md).

## How it works

1. Start the bot on Telegram and paste your wallets (Solana, Base, BNB Chain, Robinhood Chain).
2. Trades are picked up automatically, and PnL is computed in code, in your chain's native coin with a USD total.
3. About 2 hours after your last trade, M8 texts you:
   "8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?"
4. You reply by text or voice. M8 writes the day's journal entry in your words, tags the trades and keeps your reason for each buy.
5. Code finds your patterns (chasing, revenge entries, oversizing, late nights). M8 calls them out once, with the past trades that prove it.
6. The website is where you read your journal, see your stats and change settings.

Along the way M8 sends a first-day look at your last 30 days, a morning brief with the state of the trenches, live check-ins when you tilt or break a rule, and a Sunday recap card you can share.
Discord comes shortly after launch.

## What it is not

- Not a trading bot or terminal: it never trades, never holds keys and never asks you to sign anything.
- Not a signal or call group: no buy, sell or hold advice, and no verdicts on coins or KOLs.
- Not a PnL dashboard: Axiom, GMGN and Fomo already do live unrealized PnL well.
- Not a portfolio, tax or financial-planning tool, and not a therapist.
- It doesn't track perps, LP or staking.

## Stack

| Part | Choice |
|---|---|
| Backend | [Convex](https://convex.dev): database, functions, scheduler, crons, agent memory, file storage |
| Web | Next.js on Vercel |
| Chat | Vercel Chat SDK with the Telegram adapter (Discord after launch) |
| AI | Vercel AI SDK through AI Gateway; the cheapest model that passes the evals for each job |
| Trade data | One unified wallet-data API, picked in Phase 0 |
| Payments | USDC on Solana through a hosted crypto checkout, picked in Phase 0 |
| UI | shadcn/ui on our own tokens, Tailwind v4, Storybook |

## Repo map

```
docs/
  spec.md           what we're building and why, including what it is not
  architecture.md   how it gets built
  roadmap.md        phases, what each ships, and current status
  workflow.md       how a phase and a pull request run
  phases/           one plan per phase, written just before it starts
  decisions/        decision records and the open-decisions table
  archive/          reference material kept out of the product
design/
  DESIGN.md         design rules: read before any UI work
  tokens.json       design tokens, the single source for colours, type and spacing
  components.md     component inventory
convex/
  m8/
    doctrine.md     how M8 thinks and behaves, in every voice
    voices.md       the three voices: Trench friend, Calm coach, Blunt degen
    knowledge/      coaching knowledge loaded with the doctrine
AGENTS.md           instructions for coding agents working in this repo
```

## Where to start

- New to the project: [docs/spec.md](docs/spec.md), then [docs/roadmap.md](docs/roadmap.md).
- Building something: [docs/workflow.md](docs/workflow.md) and the current plan in [docs/phases/](docs/phases/).
- Touching UI: [design/DESIGN.md](design/DESIGN.md).
- Touching M8: [convex/m8/doctrine.md](convex/m8/doctrine.md).
- Wondering why something is the way it is: [docs/decisions/](docs/decisions/).

## Ground rules

- Numbers come from code, words come from the AI. M8 never computes a stat in a prompt.
- A locked decision changes only with a new record in [docs/decisions/](docs/decisions/).
- UI uses design tokens only, never raw colours or one-off sizes.
- Every Convex function takes the user from auth, never from its arguments.
