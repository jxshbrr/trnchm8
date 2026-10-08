# 0017 - Launch scope

Status: decided
Date: 2026-10-08

## Question

The spec said "Scope: full pitch".
What actually ships at launch, so the first build proves the loop without the surface that sank the first version?

## Options considered

- Everything in the spec and mockups at once.
- The bare loop only (Telegram, Solana, nudge, journal, recap).
- The loop plus the pieces that make it worth paying for, with the rest cut or moved after launch.

## Decision

**Channels**

- Telegram at launch; Discord shortly after, from the flow already designed.
- M8 lives only in the chat apps. The web has no M8 chat: it is the journal, stats and settings.

**Chains**

- All 4 at launch: Solana, Base, BNB Chain, Robinhood Chain. Phase 0 has to prove data coverage on each.

**Proactive messages** (all at launch, inside the doctrine's budget of 6 a day)

| Message | Has to be proven in Phase 0 |
|---|---|
| First-day insight (last 30 days) | Backfill speed and coverage on all 4 chains |
| Post-session nudge | Trades seen within about 1-2 minutes, at a cost that works at 30 wallets |
| Live check-in (tilt or repeat mistake, one per session) | Same as the nudge |
| Rule alerts (once per rule per day) | Same as the nudge |
| Morning brief | A source for the trench numbers below on each chain |
| Sunday recap and its card | Nothing new; just built |
| Account messages (trial, expiry, transfer and cost-basis questions) | Nothing new |

**Market data**

- One shared snapshot per chain, built once each morning and read by every user's brief, so cost doesn't grow with users.
- Majors: SOL, ETH and BNB overnight change.
- Trench temperature per chain, tying the majors to the trenches: DEX volume vs yesterday, launches and graduations, and how high the standout new coins got.
- Named coins (top runners, big rugs) appear in the brief as market context, with no verdict and no "worth a look".
- Prices of coins the user holds, and facts on any coin they ask about.

**Tags and alerts**

- 4 tags, merged from 6: Chase (bought into a pump, or bought back higher right after selling), Revenge (new entry right after a loss), Oversized (well above your normal size, including right after a win), Held too long (a loser held far past your usual winning hold). Plus Planned when the user disputes a tag.
- Tilt and repeat mistake ("same as Sep 18") are live alerts, not tags.
- Chase's "bought into a pump" half needs price data from just before the buy; until Phase 0 proves it, Chase uses the user's own fills only.

**Stats at launch**

- Everything in the mockups: net PnL, win rate, avg win and loss, max drawdown, profit factor, daily calendar, hour map, PnL by coin age at entry, hold time of winners vs losers, entry size bands, discipline (tilt and revenge with receipts, rule adherence).
- Later: PnL by source and the other detectors listed in the architecture as later.

**Rules** (all 5 at launch)

- Daily loss limit.
- Max trades per day.
- Max position size, counted across all the user's wallets so splitting a buy doesn't get around it.
- No new entries after a time (the action for the hour map and late-night pattern).
- Cooldown after a big loss.
  A big loss is one worse than 9 out of 10 of the user's past losses, measured in money (USD across chains, shown in the user's unit).
  Until there are about 20 losses, the line is half a normal buy.
  Users can switch to a fixed amount in Settings.

**Look**

- Unchanged: 7 accents, dark and light themes.

**AI**

- Alerts and reminders start as written text in all 3 voices, with numbers filled in by code.
- During development we test written text against live AI for each message type and keep AI where it is worth the cost.
- Model routing and providers (not only Anthropic) are chosen during the build against the eval set; frontier models only where writing or reasoning needs them, and always near the harm line.
- How plans differ on AI is decided with the plan numbers.

**Plans**

- Base and Pro ([0013](0013-plans-base-pro.md)) stay provisional until Phase 0 measures the cost of syncing wallets.

**Not a promise**

- Privacy is handled carefully (addresses only, never in shares or cards, deletable) but it is not a selling point or a guarantee.

**Parked**

- The landing page, until Phase 9.
- Charts in chat, until after launch.

## Why

- The first version failed by being complicated before anyone used the loop.
- Each cut removes a whole surface (Discord at launch, web M8 chat, charts) rather than weakening the loop itself.
- The pieces kept (all 4 chains, all proactive messages, rules, the mocked stats, accents and themes) are what the user judged necessary to be worth paying for.

## Consequences

- Supersedes the "Scope: full pitch", channels and in-app M8 chat rows of the spec, and parts of [0014](0014-m8-model-routing-and-caching.md) (routing becomes provisional).
- The doctrine's coin talk rule changes to allow named coins as market context in the brief.
- Mockups that show the web M8 chat, FOMO as a tag, the old cooldown wording or a Discord-first flow are out of date; they get a follow-up pass.
- Phase 0 adds tracks for trench data, pre-buy price data and Robinhood Chain coverage.
