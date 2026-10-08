# TrenchM8 - architecture

How the product in [spec.md](spec.md) gets built.
Phases and status are in [roadmap.md](roadmap.md).

## Architecture

```
Telegram ----webhook---->  Next.js (Vercel): Chat SDK  --calls-->  Convex
Discord  --gateway (cron-kept listener)-->  /api/chat/discord   (shortly after launch)
Next.js (Vercel)  <-- live queries -->  Convex
                                          |- http: /payments/webhook, /auth/*
                                          |- crons: poll-scheduler (1m), trench snapshot (daily per chain), briefs/recaps (1h), reminders (1h)
                                          |- workpool: wallet polls (capped parallelism, retries)
                                          |- scheduler: per-user nudge (runAfter, cancelled + rescheduled on each fill)
                                          |- agent component: M8 threads, memory, vector search
                                          |- rate limiter: chat cap, spam, LLM budget
                                          |- file storage: chart PNGs, recap cards
                                          '- actions -> unified trade API, AI Gateway, market sources, outbound messages via the chat layer
```

### Trade ingestion
- **Spike:** run Mobula (`/wallet/trades`) and Zerion against real wallets on all 4 chains, including a pump.fun trade and a Robinhood Chain trade. Compare swap detection, side, USD values, platform labels, latency, rate limits and price. The winner becomes the single adapter behind a `TradeSource` interface.
- **Push vs polling:** the spike also prices push (Helius webhooks on Solana, address-activity webhooks on EVM) against polling, at 30 wallets per user with mostly idle wallets.
  Pro's price depends on it ([0013](decisions/0013-plans-base-pro.md)).
- The adapter must return token transfers as well as swaps, so moves between wallets can be matched.
- Normalized `Fill`: `{chain, wallet, txHash, logIndex, ts, token, side, tokenAmount, usdValue, priceUsd, platform}`. It's unique on `(chain, txHash, logIndex)`, so overlapping polls can't create duplicates.
- **Adaptive polling** (if the spike picks polling, or as the fallback behind push):
  - Wallets with a fill in the last 2h are polled every 1-2 min.
  - Wallets active this week, every 10 min.
  - Dormant wallets, every 60 min.
  - Expired accounts, never.
  - A cron each minute enqueues due wallets into a Workpool. Each poll fetches only trades after the wallet's cursor.
- 30-day backfill on wallet add, and a gap backfill on renewal.
- Spot swaps and token transfers only; perps, LP and staking are ignored.

### Positions and transfers
See [0011](decisions/0011-trade-closing-and-thesis.md) and [0012](decisions/0012-wallets-and-transfers.md).
- FIFO lots per (user, chain, token) across all the user's wallets, valued in the native coin and USD at fill time.
- **Internal transfer** (both wallets tracked): the lots move with the tokens; nothing is realized.
- **Transfer to an untracked wallet:** the lots are marked "moved out" and M8 asks once (Mine, track it / Not mine / Ignore).
  - Mine: the wallet is added and backfilled, and its sells close the lots.
  - Not mine: the lots close at market value at the transfer time, counted as an exit.
  - Ignore: the lots stay "moved out", with no PnL.
- **Inbound transfer** from outside: zero-cost lots.
  When one is sold for real money, M8 asks once what they paid, and the answer re-prices the lot.
- **Trade close:** a position closes when what's left is worth under $1, checked after each fill and by a daily sweep (catches dead and rugged bags).
  Leftover dust sold later adds to the closed trade; a new buy opens a new trade.
- **Thesis and source:** the nudge after a buy asks why, and where the idea came from (KOL or call group, own scanning, copy-trade, narrative).
  The answer is saved on the trade and quoted back when it closes.

### Chat layer
- Vercel Chat SDK in Next.js routes, with `@chat-adapter/telegram` and `@chat-adapter/discord`. The Discord adapter's Gateway listener is kept alive by a Vercel cron and forwards DMs to our webhook.
- Inbound messages are normalized and handed to Convex; M8 replies with channel-neutral messages (text, buttons, image) that the adapter renders: Telegram inline keyboards and photos, Discord components and embeds.
- Outbound proactive messages go to the user's primary channel only.
- Voice notes: Telegram voice and Discord voice-message attachments both go through the same transcription step.

### Nudge mechanics
- Each new fill runs a mutation that cancels the user's pending nudge (`scheduler.cancel`) and schedules a fresh one with `runAfter(nudgeDelay)`. When it fires, the session closes, stats are computed and M8 writes and sends the nudge.

### M8 agent
- `@convex-dev/agent` on the AI SDK through AI Gateway, any provider.
- **Model routing** ([0014](decisions/0014-m8-model-routing-and-caching.md), provisional per [0017](decisions/0017-launch-scope.md)): the cheapest thing that's still right. The tiers below are the starting point; models and providers are chosen during the build against the eval set, and written text is tested against live AI for each message type.
  - Templates in code (all 3 voices): rule alerts, tilt check-in, loss limit, trial reminders, coin facts.
  - Haiku 5.5: intent triage, extraction, memory, conversation names and summaries, short replies; never the harm line.
  - Sonnet 5.5 at effort `low`: nudges, journaling, chat.
  - Opus 5.5 with adaptive thinking: Sunday recap, deep multi-tool questions.
  - A conversation stays on one model unless it escalates, because caches are model-scoped.
- **Prompt caching:**
  - `[tools][doctrine][voice]` shared by all users (1h TTL), then `[profile, rules, memory]` per user (1h TTL), then the conversation with automatic caching.
  - No dates or names in the shared prefix; the date is a mid-conversation system message.
  - AI Gateway pins Anthropic direct so the cache stays in one workspace; hits are logged from `usage.cache_read_input_tokens`.
- **Batch API:** Sunday recaps, nightly memory extraction, conversation summaries, and morning briefs started an hour early.
- **Daily chat cap:** a cost budget in the rate limiter, shown as a percentage.
- M8 is reached only through the chat app; the web has no M8 chat.
- Tools: `get_trades`, `get_stats`, `get_patterns`, `get_market`, `get_token_facts` (facts only, see doctrine: age, bonding stage and migration, market cap and all-time-high market cap, liquidity and liquidity to market cap, 24h volume and volume to market cap, holder count, top holder % excluding the pool, top 10 %, dev share, LP locked or burned, mint and freeze authority, creator prior launches; also snapshotted at entry on each trade), `get_rules`, `set_rule`, `write_trade_note`, `write_day_summary`, `remember`, `render_chart`.
- The system prompt is doctrine + coaching knowledge ([0016](decisions/0016-m8-knowledge.md)) + voice preset + user profile, in that order for caching. Facts are identical across voices; only the phrasing changes.
- **One thread per user, split into conversations.** A conversation ends after ~6h of quiet or `/new`; a light model writes a short summary used as context later.
- **What goes into each turn:**
  - Always: doctrine, voice, profile memory.
  - Recent messages from the current conversation only.
  - Summaries of earlier conversations.
  - Vector search hits from the whole thread and the journal.
- Voice notes are transcribed through an STT model, and the audio is deleted afterwards.

### Rules, patterns, stats
- Rules: `daily_loss_limit`, `max_trades_per_day`, `max_position` (summed across all the user's wallets), `no_trading_after`, `cooldown_after_big_loss`. They're checked after each sync that adds fills, and a breach alert goes out once per rule per day.
  - A big loss is worse than the 90th percentile of the user's past losses in USD; with fewer than ~20 losses, half the user's median buy. Users can set a fixed amount instead.
- Tags (code, per trade): `chase` (bought back higher soon after selling, or into a pump once pre-buy price data is proven), `revenge` (entry right after a loss), `oversized` (well above the user's median size, including right after a win), `held_too_long` (a loser held far past the usual winning hold), plus `planned` from the user.
- Live alerts: tilt (revenge and oversized stacking within a session) and repeat mistake (a tag matching past receipts), one per session between them.
- Pattern detectors are pure TypeScript functions over positions. At launch ([0017](decisions/0017-launch-scope.md)):
  - the tags and live alerts above
  - PnL by coin age at entry
  - hour map: PnL by weekday and hour (late-night trading is a pattern with receipts)
  - hold time of winners vs losers
  - entry size bands
  - rule adherence
- Later:
  - PnL by source (KOL or call group, own scanning, copy-trade, narrative)
  - pulling back too far after a drawdown (count and size well below normal)
  - dead capital (losers held far past the usual winning hold)
  - roundtrips (a trade that was well up and closed near or below cost)
  - spreading thin (more open positions than usual)
  - entries near the all-time high
  - quick losses after a call (source tag)
  - trading more in a cold stretch (count up, results down)
  - PnL by market-cap band and by bonding stage at entry
  - safety facts at entry on losers vs winners (top holder, dev share, volume to market cap; default lines 3.5%, 5% and 80% live in code, used only in reviews, never on a coin the user is looking at)
  - Findings are stored with evidence (position ids).
- Stats are kept as `dailyStats` rows, updated whenever a position changes, so the web and M8 read precomputed numbers.

### Proactive messages
- All at launch, inside the doctrine's budget: first-day insight, nudge, live check-in, rule alerts, morning brief, Sunday recap, account messages ([0017](decisions/0017-launch-scope.md)).
- Morning brief: hourly cron picks users whose local morning hour has arrived and reads the shared trench snapshot plus their own yesterday.
- Sunday recap: saved as a journal entry and rendered as a shareable card.
- **Trench snapshot:** built once each morning per chain and shared by every user, so cost doesn't grow with users.
  - Majors: SOL, ETH and BNB overnight change.
  - Trench temperature: chain DEX volume vs yesterday (e.g. DefiLlama), launches and graduations (launchpad data, e.g. Bitquery or Moralis for pump.fun), how high the standout new coins got (e.g. GeckoTerminal or DexScreener new pools).
  - Named standout coins and big rugs, as context.
  - Sources per chain are picked in Phase 0; a chain with no source shows majors and volume only.
- Prices of coins users hold, and `get_token_facts` on request.

### Charts
- Charts in chat come after launch. The web uses SVG chart components; the Sunday recap card is the only image at launch.
- When charts come to chat, the same SVG components are rasterized to PNG with satori/resvg, stored in Convex file storage and sent as a photo (Telegram) or embed image (Discord).

## UI

The look, tokens, components, motion and feedback rules live in [design/DESIGN.md](../design/DESIGN.md).
The mockups are in [design/mockups/](../design/mockups/) and published at https://claude.ai/artifact/QmewGj69mk6Qr8uLsYED2V.

## Repo layout

```
docs/             # spec, architecture, roadmap, workflow, phase plans, decision records
design/           # DESIGN.md, tokens.json (source of truth), components.md, mockups/
app/              # Next.js pages + api/chat/{telegram,discord} (Chat SDK), auth callbacks
components/       # UI kit (shadcn + TrenchM8 tokens), shared charts; *.stories.tsx next to each component
.storybook/       # Storybook config; Playwright screenshots of every story in both themes
convex/
  schema.ts
  http.ts         # telegram, payments webhook, auth endpoints
  crons.ts
  auth/           # telegram verify, login tokens, sessions, JWT minting
  ingest/         # TradeSource, provider adapter, normalize, poll scheduler
  pnl/            # FIFO engine, sessions, dailyStats
  patterns/  rules/  market/  billing/
  m8/             # agent, tools, doctrine.md, voices.md, evals/
  chat/           # channel-neutral message builders, onboarding flow, identity linking
tests/            # vitest (convex-test) + playwright
```

## Verification

- **Unit (vitest + convex-test):**
  - FIFO edge cases: partial sells, the same token across wallets, dust, zero-cost airdrops.
  - Transfers: internal moves keep cost basis, untracked transfers stay "moved out" until answered, the under-$1 close rule.
  - Normalizer against recorded real API responses.
  - Each pattern detector and each rule.
  - The poll scheduler.
  - Nudge reschedule and cancel.
  - Trial and expiry state transitions.
  - Auth: tokens are single-use, Telegram signatures and Discord OAuth are verified, identity linking can't steal another user's identity, users are isolated from each other.
- **M8 evals:** the doctrine eval set runs on every prompt change and has to pass.
- **E2E with real usage:**
  - A test bot on Telegram (Discord once it ships) plus small real trades on each chain; the full loop is run once per channel.
  - Fills appear within one active poll interval.
  - PnL matches the wallet's own UI.
  - The nudge fires after a shortened dev delay.
  - A reply becomes journal entries on the web, written in the chosen voice.
  - A test-mode payment extends `paid_until`.
- **Web:** Playwright at mobile and desktop widths, in dark and light themes, plus a pixel-level review.
- Lint, typecheck, tests and build all pass before each phase check-in.
