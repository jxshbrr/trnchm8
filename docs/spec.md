# TrenchM8 - product spec

## Context

Memecoin traders don't keep journals because writing them is boring.
TrenchM8 writes the journal for them: it watches their wallets, texts them on Telegram or Discord about 2h after they stop trading, and turns their casual reply into journal notes.
This doc is the agreed product spec: what TrenchM8 does and why.
How it gets built is in [architecture.md](architecture.md), the order of work is in [roadmap.md](roadmap.md), and the look is in [design/DESIGN.md](../design/DESIGN.md).
Changing a locked decision means writing a decision record in [decisions/](decisions/) first.

## Who it's for

Memecoin traders, from newer traders with 1-5 wallets to advanced traders running 10-30+ wallets.
They trade through Telegram bots (Trojan, BonkBot, Maestro, Banana Gun), web terminals (Axiom, Photon, BullX, GMGN, Padre), launchpads (pump.fun, LetsBonk, Four.meme, Clanker, Zora) and normal wallet swaps.
Trade counts range from under 20 to 100+ a day, depending on the trader.
Advanced traders spread across wallets to hide supply, dodge copy-traders, bundle launch buys and separate strategies, and they move tokens between wallets.
The product stays simple on purpose: one rule beats three clever ones.

## What it is not

- Not a trading terminal or bot: it never trades, never holds keys and never asks the user to sign anything.
- Not a signal or call group: no buy, sell or hold advice, and no verdicts on coins or KOLs.
- Not a PnL dashboard: Axiom, GMGN and Fomo already do live unrealized PnL. Open positions are a plain list.
- Not a portfolio, tax or financial-planning tool, and not a therapist.
- It doesn't track perps, LP or staking.
- It doesn't guess which wallets are the user's, where a trade idea came from, or patterns: the user adds wallets, the user names sources, and code finds patterns.
- It doesn't help hide supply or time dumps.
- No social feed, leaderboards, public profiles, in-bot payments or confetti over PnL.

## Decisions (locked)

| Area | Decision |
|---|---|
| Audience | Public product |
| Scope | Launch scope in [0017](decisions/0017-launch-scope.md): the core loop, all proactive messages, rules, the mocked stats, morning brief with trench data, ask-anything in the chat app, voice notes. Discord and charts come after launch |
| Chains | Solana, Base, BNB Chain, Robinhood Chain (evm:4663) |
| Business model | 7-day free trial, then paid only |
| Plans | Provisional until Phase 0 measures sync cost. Base: 5 wallets, $20 / 30 days or $50 / 90 days. Pro: 30 wallets, $50 / 30 days or $125 / 90 days. Identical otherwise, prepaid in crypto ([0013](decisions/0013-plans-base-pro.md)) |
| Payments | Crypto payment processor (picked in spike), USDC on Solana only, checkout on the website |
| Wallets | Trading wallets only, one slot each, no roles (an EVM address counts once across Base/BNB/Robinhood) ([0012](decisions/0012-wallets-and-transfers.md)) |
| PnL unit | Each chain's native coin with a USD total; switchable to USD ([0015](decisions/0015-pnl-unit.md)) |
| AI usage | Fair-use cap on asking M8 in the chat app, measured in cost rather than messages (a cheap reply uses less), shown as a percentage meter ("M8 today") in Settings > Your plan; resets at midnight; proactive messages and journaling never count |
| Expiry | Read-only journal forever, polling + AI stop, one gentle "here's your week + renew" message, then quiet |
| Channels | Telegram at launch, Discord shortly after ([0017](decisions/0017-launch-scope.md)). Once both exist, users sign up on either, can link both, and pick one primary channel for M8's messages |
| Login | One-time link from the bot and the Telegram Login widget; Discord OAuth when Discord ships |
| Backend | Convex (DB, functions, scheduler, crons, agent memory, file storage) |
| Web | Next.js on Vercel |
| AI | Vercel AI SDK + AI Gateway, any provider. Each task goes to the cheapest model that's still right, frontier models only where writing or reasoning needs them; written text for alerts, tested against live AI during development. Final routing is chosen during the build ([0014](decisions/0014-m8-model-routing-and-caching.md), [0017](decisions/0017-launch-scope.md)) |
| Ingestion | One unified API. Mobula vs Zerion, and push vs polling, decided by a spike |
| Talking to M8 | Only in the chat app (Telegram, then Discord), as one continuous thread with shared memory; `/new` starts a fresh topic. The web has no M8 chat: it is the journal, stats and settings ([0017](decisions/0017-launch-scope.md)) |
| Chat layer | Vercel Chat SDK with the Telegram adapter, Discord adapter added after launch (replaces grammY). One message model: text, buttons, images, voice |
| Look | Fomo + Phantom inspired: consumer-grade, rounded, friendly, mobile-first |
| Direction | Citrus night: near-black ground, Manrope, rounded cards, dark-first with light supported |
| Accent | User picks in Settings > Appearance from a curated set: Citrus, Cornflower, Sky, Lilac, Bubblegum, Tangerine, Apricot. No free hex, so contrast stays safe and no accent collides with PnL green/red. Brand default: Sky (#7CD4FF), used for new users, the landing page and the bot avatars. Charts and recap cards M8 sends use the user's own accent |
| M8 identity | Subtle avatar/glyph |
| M8 voice | User picks: Trench friend / Calm coach / Blunt degen |
| M8 doctrine | Written together in a dedicated session before M8 is built |

## Product definitions

- **Trade** (user-facing) = one position in one coin, from the first buy until what's left is worth under $1. That covers a full sell, dust and dead or rugged bags. Individual swaps ("fills") roll up into it ([0011](decisions/0011-trade-closing-and-thesis.md)).
- **Open positions** are a plain list with current value only. Axiom, GMGN and Fomo already do unrealized PnL well.
- **Thesis:** M8 asks why the user bought in the nudge after the buy, and quotes it back when the trade closes.
- **PnL** = FIFO cost basis per (user, chain, token) across all the user's wallets, in the native coin and USD at fill time.
- **Transfers between tracked wallets** are internal moves: cost basis follows the tokens and nothing is realized.
- **Tokens sent to an untracked wallet** stay open as "moved out" until M8 asks once: Mine, track it / Not mine (closed at market value, counted as an exit) / Ignore ([0012](decisions/0012-wallets-and-transfers.md)).
- **Tokens received from outside** (airdrops, a friend, creator rewards) start at zero cost; M8 asks what they paid only when one gets sold for real money.
- **Source:** where a trade idea came from (KOL or call group, own scanning, copy-trade, narrative). It comes only from the user: picked up from their reply, or one tap on the session's 1-2 biggest coins. Untagged trades stay untagged.
- **Devs** launching their own coins are normal traders: dev buys and sells are fills, creator fees count as income.
- **Not tracked:** perps, LP and staking. Spot swaps and token transfers only.
- **Tags** (code-detected, shown on trades and in entries): Chase, Revenge, Oversized, Held too long, plus Planned when the user disputes one. Tilt and repeat mistakes are live alerts, not tags.
- **Rules:** daily loss limit, max trades per day, max position size (across all wallets), no new entries after a time, cooldown after a big loss (worse than 9 in 10 of the user's past losses in money; half a normal buy until there's history).
- **Session** = a run of fills with no gap longer than the nudge delay (default 2h). When the gap passes, M8 nudges.
- **Numbers come from code, words come from the LLM.** Stats, patterns and rule breaches are computed in code and handed to the model as facts.

## Account lifecycle

1. **Start:** `/start` in the Telegram bot (and in Discord once it ships). Creates the account; the Telegram or Discord id becomes its first linked identity.
2. **Onboarding in chat:** paste a wallet -> pick M8's voice (three sample nudges as buttons) -> pick a unit (native coin or USD) -> confirm timezone. 30-day backfill runs; M8 sends a first "here's your last month" message so value shows up in minute one.
3. **Trial:** 7 calendar days, starting when the first wallet is added. Full features, 5-wallet limit; adding a 6th wallet offers Pro.
   - Abuse guard: one trial per Telegram or Discord identity, and per wallet address. An address that has already had a trial can't start another under a new account.
4. **Day 6:** M8 mentions the trial ends tomorrow, with a link to the website checkout.
5. **Paid:** Base or Pro, prepaid 30 or 90 days. Because crypto has no auto-renew, M8 reminds the user 3 days before expiry and on the expiry day.
6. **Expired:**
   - Polling, nudges, briefs and chat stop.
   - M8 sends one "your trial ended, here's your week" recap with a renew link, then stays quiet.
   - The journal and stats on the web stay readable forever.
   - Paying again resumes everything and backfills the gap.
7. **Delete account:** from /settings or `/delete` in the bot. Hard-deletes all data.

## Plans and limits

| | Trial | Base | Pro | Expired |
|---|---|---|---|---|
| Trading wallets | 5 | 5 | 30 | tracking off |
| 30 / 90 days | free, 7 days | $20 / $50 | $50 / $125 | - |
| Auto-tracking | yes | yes | yes | no |
| Nudges, journaling, rule alerts | yes | yes | yes | no |
| Morning brief, Sunday recap | yes | yes | yes | no |
| Ask-anything chat | daily cap | daily cap | daily cap | no |
| Web journal + stats | yes | yes | yes | read-only |

- The chat cap is a daily cost budget and shows as a percentage (never a message count). When it is hit, M8 says something like "I'm tapped out for today, back tomorrow." A per-minute spam limit also applies.
- Plans and their prices are provisional until Phase 0 measures the cost of syncing wallets.
- Per-user daily LLM token budget as a backstop against runaway cost, with an alert to us if anyone hits it.
- **Unit economics (rough, to be verified):** an active trader costs ~$2-4/month in AI (~$6-8 heavy) with model routing and caching, plus a data-API cost per wallet, against $16.67-20/month revenue on Base. The spike measures the real cost per wallet at 30 wallets per user; if it's high, Pro's price changes, not the plan structure.

## Payments

- The website `/billing` page shows the plan, its expiry date and a "Pay with USDC (Solana)" button that opens the processor's hosted checkout.
- The processor's webhook hits Convex. We verify the signature, record the payment and extend `paid_until` by 30 or 90 days. If the user pays again while still active, the new days stack on top.
- **Never take payment inside a bot.** Telegram requires bot payments for digital goods to go through Telegram Stars; Discord's monetization policy is checked in the spike. Bots only link to the website.
- Processor shortlist for the spike: MoonPay Commerce (Helio), Coinbase Commerce, NOWPayments. Must support USDC on Solana, webhooks and a hosted checkout.

## Login and sessions

- **From either bot:** an "Open journal" button gives a one-time link. The token is short-lived, single-use and stored hashed.
- **From the website:** "Log in with Telegram" (official widget, HMAC verified) or "Log in with Discord" (OAuth2, `identify` scope).
- **Identities:** a user has one or more linked identities (`telegram`, `discord`). Linking a second one happens from /settings while logged in. One identity can belong to only one user.
- **Session:** a 30-day httpOnly cookie, backed by a `sessions` table so it can be revoked and "log out everywhere" works. The web app swaps it for a short-lived (1h) JWT that Convex verifies through its custom JWT auth.
- **Authorization:** every Convex query and mutation derives the user from the auth identity, never from arguments. Tests check that one user can't read another's data.

## M8 knowledge

1. **Your trades:** live through tools, always exact numbers.
2. **Your profile:** facts M8 learns and keeps, such as goals, strategy, recurring excuses and set rules. Stored as structured memory the user can view and edit in /settings.
3. **Your journal history:** searchable with vector search, so M8 can say "you said the same thing on Sept 12."
4. **The market:** one shared snapshot per chain each morning (majors, trench temperature, standout coins by name as context), prices of coins the user holds, and facts on any coin they ask about.
5. **Doctrine:** the coaching playbook. See below.

## M8 doctrine

M8's coaching rules live in `convex/m8/doctrine.md` (versioned) with an eval set of tricky conversations, such as a user asking for a call, a user on tilt, a user in distress, and a disputed tag.
The evals are scored before every doctrine or prompt change.
The doctrine is being written together before the build; the working draft starts from: no coin calls, process over outcome, evidence or silence, one thing at a time, ask before assuming, your rules are your promises, tilt protocol, harm line.

## Decisions from the mockups

- Every M8 suggestion ends in one-tap buttons (rules mostly get created from chat).
- Every proactive message type has a mute option; weekend check-ins are a separate toggle.
- Rule alerts ask rather than order, and accept "It's planned" with a reason.
- M8 makes no coin calls. Asked about a coin, it gives facts with no verdict (age, liquidity, holder concentration) and links them to the user's own record. The morning brief can name standout coins as market context, never as a pick.
- Sunday recap is a shareable branded card (growth loop).
- Onboarding ends with a real 30-day insight before the trial clock matters.
- Settings: Appearance (Dark / Light / System + accent swatches), wallet labels, "What M8 remembers" with Forget, "Tell M8 something", data export, payment history.
- Journal entries are written in the user's voice, first person, from their reply (text or voice). M8's take is separate, in M8's chosen voice, and is where cross-day patterns live. Trade notes are also first person. Both are editable by hand or through chat (with Undo).
- Repeat mistakes are called out twice:
  - Live, mid-session, at most one live callout per session, citing the past instance with receipts ("same as Sep 18: $PEPU, 2 min after a loss, 2.5x size, -$188"), with "It's planned" / "Good catch" buttons.
  - In the post-session nudge, quoting the user's own past words when vector search finds them ("on the 24th you wrote 'never again'").
  - On the journal, a "Same as Sep 18" link sits under the trade, and M8's take links to all receipts.
  - Repeats come from code (pattern detectors over positions); matching past words comes from vector search over journal entries. No callout without a past entry to point to.
- Sharing a day:
  - A share sheet with Image (branded card) or Text (the full entry, ready to paste on X or into a Telegram channel, with a 280-character counter). No public links or export in v1.
  - Money defaults to % only, with a per-share toggle to $ amounts. Wallet addresses are never included. Toggles for trade notes and M8's lesson.
- Stats: KPIs are net PnL, win rate, avg win / loss, max drawdown and profit factor. Daily calendar shows $ and trade count per day and links to the journal. Hour map (weekday x hour, avg per trade) replaces time-of-day buckets. Hold time and entry size bands (median return; size relative to the user's normal). Discipline section: tilt and revenge with receipts, then a full-width rules card with adherence %. No Edge/Leak badges: M8's one-liner on each card already says it.
- Stats skipped on purpose: composite scores (radar), PnL goals (outcome over process), session rings, long/short, journal streaks, return histograms.
- Corrections in chat ("that one wasn't planned") update tags and stats live, with Undo.
- Landing: parked until Phase 9. B2 (chat-first) and B3 (Poke-style editorial on night paper) are on the canvas. No invented testimonials or user counts.
- Discord (shortly after launch) mirrors Telegram, with the same story and numbers, but uses Discord's richer UI:
  - "Start on Discord" opens the Add App screen. "Add to My Apps" is the recommended path, with "or join the TrenchM8 server" as the fallback. Then M8 says hi first in the DM.
  - Journal summaries, morning briefs and the 30-day insight are embeds with the user's accent as the stripe.
  - Buttons replace Telegram's inline keyboards, and the voice picker is a select menu with sample lines.
  - Slash commands: `/start`, `/ask`, `/voice`. `/ask` also works in any server. Settings confirmations are ephemeral ("Only you can see this").
  - Charts and recap cards are the same images M8 sends on Telegram.
- Mockups: [design/mockups/](../design/mockups/), published at https://claude.ai/artifact/QmewGj69mk6Qr8uLsYED2V

## Open questions

Tracked in [decisions/README.md](decisions/README.md), each with the phase that has to settle it.
