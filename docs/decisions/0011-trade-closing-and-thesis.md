# 0011 - When a trade closes, and when M8 asks why

Status: decided
Date: 2026-10-08

## Question

Memecoin traders take their initials at 2x and ride a moonbag for weeks, and often leave dust behind.
A trade defined as "first buy until flat" may never close, so it never reaches win rate, the journal or a nudge.
Waiting for the close also means the user has forgotten why they bought.

## Options considered

- Close when initials are out, and track the moonbag separately.
- Score every partial sell on its own.
- Close only when fully sold, with a small dust rule.

## Decision

- A trade closes when what's left is worth under $1.
- That one rule covers a full sell, leftover dust, and dead or rugged bags (worth about $0).
- Open positions are a plain list with their current value only.
- M8 asks the thesis ("why'd you get into $FROGZ?") in the post-session nudge after the buy, while the user still remembers.
- When the trade closes, M8 quotes that reason back ("closed $FROGZ, +3.2 SOL. you bought it for the AI agent meta. did that play out?").

## Why

- One rule instead of three (initials, dust, dead bags), which keeps the app simple.
- Axiom, GMGN and Fomo already show unrealized PnL well, so we don't rebuild it.
- Asking at entry gives a better journal than asking at the close, with no extra logic.

## Consequences

- Replaces the earlier "mark dead bags, then ask" idea.
- Win rate only counts closed trades, so a long-held moonbag shows up late, by design.
- Later sells of leftover dust in a closed trade add to that trade's PnL; a new buy starts a new trade.
- The thesis is stored on the trade and linked to the journal entry it came from.
