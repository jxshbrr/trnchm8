# TrenchM8 - roadmap

The order of work, what each phase ships, and how we know it's done.
Each phase gets a detailed plan in [phases/](phases/) written right before it starts, because earlier phases (especially the Phase 0 spikes) change what later ones look like.
How a phase runs, day to day, is in [workflow.md](workflow.md).

Status: `not started` · `planning` · `in progress` · `done`.

## Before the build

| Step | Status | Output |
|---|---|---|
| Spec, architecture and roadmap in the repo | in progress | `docs/` |
| Mockups for every screen and both bots | done | [design/mockups/](../design/mockups/), [published canvas](https://claude.ai/artifact/QmewGj69mk6Qr8uLsYED2V) |
| Design system spec (tokens, components, rules) | done | `design/DESIGN.md`, `design/tokens.json`, `design/components.md` |
| M8 doctrine session (together) | in progress | `convex/m8/doctrine.md` draft, voice presets, first eval cases |
| Landing v2 (more product, less template) | parked | B2 and B3 on the canvas; pick one during the Phase 9 plan |
| Mockup follow-ups from the doctrine | done | "Facts, no verdict" coin replies in TgAsk, DcAsk and M8Chat |
| Trader interviews: wallets, transfers, trade close, unit, plans, M8 cost | done | decisions [0011](decisions/0011-trade-closing-and-thesis.md)-[0015](decisions/0015-pnl-unit.md), doctrine v0.2 |
| M8 knowledge audit | done | [0016](decisions/0016-m8-knowledge.md), `convex/m8/knowledge/coaching.md` |
| Launch scope | done | [0017](decisions/0017-launch-scope.md) |
| Mockup follow-ups from the interviews and launch scope | not started | Native-coin PnL; Base / Pro and the 6th-wallet offer; the "moved out" question; open positions list; web M8 chat boards marked out of scope and "Talk to M8" / "Ask M8" removed; tags merged (FOMO into Chase); the 5 rules in Settings (max position, cooldown after a big loss); morning brief with trench numbers; Discord boards marked after launch |
| Phase 0 plan | not started | `docs/phases/00-spikes.md` |

## Critical path

```
0 Spikes ─▶ 1 Foundation + design system ─▶ 2 Ingestion + PnL ─┬─▶ 3 Core loop (Telegram) ─▶ 5 Rules + patterns ─▶ 6 Briefs + recap ─▶ 7 Ask M8
                                                               └─▶ 4 Web journal + stats ──────────────────────────────────────────────▶ 8 Billing ─▶ 9 Launch ─▶ 10 Discord
```

Phases 3 and 4 can run side by side once Phase 2 is done: both read the same positions and stats, one through the bots and one through the web.
Everything else runs in order.

## Phases

### 0. Spikes
- **Goal:** settle the unknowns that would be expensive to get wrong later.
- **Tracks (parallel, one worktree each):**
  - Trade data: Mobula vs Zerion on real wallets on all 4 chains, including a pump.fun and a Robinhood Chain trade, with token transfers as well as swaps, 30-day backfill speed, and price data from just before a buy (for Chase).
  - Trench data: a source per chain for DEX volume, launches and graduations, and standout new coins' peak market cap, priced as one shared daily snapshot.
  - Sync cost: push (Helius webhooks, EVM address-activity webhooks) vs polling, priced at 30 wallets per user. Sets Pro's price.
  - M8 models: the doctrine evals on cheap and frontier models across providers through AI Gateway, with cost per turn and cache hit rate. Feeds the plan numbers.
  - Payments: processor test with USDC on Solana (MoonPay Commerce, Coinbase Commerce, NOWPayments).
  - Chat layer: Chat SDK with the Telegram adapter on Vercel calling Convex; does it need a Redis state store; AI Gateway hello world.
- **Exit:** one decision record per track in [decisions/](decisions/), plus a short writeup with measured cost and latency. Spike code stays on spike branches and is never merged.
- **Status:** not started

### 1. Foundation + design system
- **Goal:** a deployed skeleton you can log into from Telegram, built on the design system from day one.
- **Ships:**
  - Next.js on Vercel and Convex, with CI (lint, typecheck, tests, build) and preview deployments per PR.
  - Design system in code: `tokens.json` turned into CSS variables and Tailwind v4 theme, shadcn/ui primitives restyled, Storybook with screenshot tests in both themes, lint bans on raw colors and one-off values, a project UI skill.
  - Schema with users and identities (ready for a second app); `/start` on Telegram; login by bot link and the Telegram widget; sessions.
- **Exit:** start the test bot on Telegram, tap "Open journal", and land logged in on an empty, on-design journal page.
- **Status:** not started

### 2. Ingestion + PnL
- **Goal:** trades appear on their own and the numbers are right.
- **Ships:** the chosen data adapter behind `TradeSource`, push or adaptive polling, 30-day backfill, FIFO engine in native coin and USD, transfers between tracked wallets, "moved out" and inbound zero-cost lots, the under-$1 trade close, positions, sessions, `dailyStats`.
- **Exit:** with your real wallets, every trade appears within one active poll interval, PnL matches the wallet's own UI to the cent on a sample of 20 positions, and a buy in one wallet sold from another shows as one trade.
- **Status:** not started

### 3. Core loop
- **Goal:** the product's reason to exist: M8 texts you, you reply, the journal writes itself.
- **Needs:** the doctrine and voice presets.
- **Ships:** the first-day insight, nudge scheduling, the nudge (with the thesis and source question), the untracked-transfer question, text and voice replies, journal entries in your voice and M8's take, memory, the doctrine eval set in CI, and the written-text vs live-AI test that sets the first model routing.
- **Exit:** a week of dogfooding on your own wallets in Telegram, with every nudge answered turning into a correct journal entry.
- **Status:** not started

### 4. Web journal + stats
- **Goal:** the website from the mockups, on real data.
- **Ships:** journal (day picker, trades, entries, edits with Undo, share), stats, settings without billing. No M8 chat on the web.
- **Exit:** screens match the mockups at mobile and desktop widths in both themes, checked with Playwright screenshots.
- **Status:** not started

### 5. Rules + patterns + alerts
- **Ships:** the five rules (daily loss limit, max trades per day, max position, no new entries after a time, cooldown after a big loss), the four tags, tilt and repeat-mistake live alerts with receipts, rule alerts.
- **Exit:** replaying Sep 18 style sessions in a test fires the right alert once, with the right receipts.
- **Status:** not started

### 6. Market + morning brief + Sunday recap
- **Ships:** the shared trench snapshot per chain, the morning brief, the Sunday recap and its shareable card.
- **Status:** not started

### 7. Ask M8
- **Ships:** asking M8 anything in Telegram with tools and facts on request, the daily cost cap and its meter in Settings. Charts in chat come after launch.
- **Status:** not started

### 8. Billing + trial lifecycle
- **Ships:** the plans set after Phase 0 (provisionally Base and Pro), checkout, payment webhook, trial and expiry states, the 6th-wallet Pro offer, reminders, read-only mode.
- **Exit:** a test-mode payment extends `paid_until`; an expired account is read-only and gets exactly one recap.
- **Status:** not started

### 9. Launch hardening
- **Ships:** rate limits and budgets, error tracking, analytics funnel, legal pages, the landing page (pick B2 or B3).
- **Status:** not started

### 10. Discord
- **Goal:** the same M8 on Discord, shortly after launch, from the flow already designed.
- **Needs:** a Discord spike first: proactive DMs (user-installed app vs server join), DMs and voice messages through the Gateway listener, monetization policy (open decisions 0003 and 0005).
- **Ships:** the Discord adapter, `/start`, `/ask`, `/voice`, Discord OAuth login, linking a second app, primary channel choice.
- **Status:** not started
