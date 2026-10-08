# 0016 - M8 coaching knowledge

Status: decided
Date: 2026-10-08

## Question

Seven knowledge notes (about 27K tokens) and the old app's memecoin doctrine were added to `convex/m8/`.
Should M8 load them, and what in them is worth keeping?

## Options considered

- Load all of them into the cached prompt.
- Load them on demand through a knowledge tool.
- Distill what fits the doctrine into one short note, and move the rest into code and the archive.

## Decision

- One short note, [convex/m8/knowledge/coaching.md](../../convex/m8/knowledge/coaching.md), sits in the cached prompt after the doctrine.
  It is written as questions M8 asks, with no thresholds, no past-win stories and only TrenchM8 tools.
- The "in the trader's own trades" ideas become pattern detectors in code (architecture, Rules, patterns, stats).
- The token safety checks become `get_token_facts` fields, shown as facts with no verdict, and are snapshotted at entry on each trade.
- Rules of thumb (top holder about 3.5%, dev share 5% or less, volume at least 80% of market cap) are never applied to a coin the user is looking at.
  They are defaults in code, used only in reviews of the user's own closed trades ("7 of your 9 losers had a top holder above 5%").
- The originals move to [docs/archive/knowledge/](../archive/knowledge/), out of the prompt.

## Why

- The notes call 14 tools TrenchM8 doesn't have and assume data it doesn't collect (ratings, emotion tags, playbooks, portfolio value).
- Much of the advice is a buy, sell or hold call or a coin verdict ("a 40% drop is a stop signal", "avoid it", "uptrend is likely a good buy"), which the doctrine rules out.
- Numbers in prose break "numbers come from code", and past-win figures go stale and read as hype.
- 27K tokens in the shared prefix would add roughly $0.005 to every Sonnet turn and dilute the doctrine.
- The psychology and execution coaching (post-loss protocol, chase test, zero test, thesis, moving targets, fumble spiral, cold markets) is exactly M8's job and is kept.

## Consequences

- Phase 3 loads `coaching.md` with the doctrine and covers it in the eval set.
- Phase 5 builds the new detectors; the data spike (0001) checks which safety facts the API returns (top holder, dev share, authorities, LP status).
- The cited source guide and `review.md` are not in the repo; we are allowed to use the content (confirmed 2026-10-08).
