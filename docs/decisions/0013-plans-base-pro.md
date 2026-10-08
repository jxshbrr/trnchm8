# 0013 - Plans: Base and Pro

Status: decided
Date: 2026-10-08
Supersedes the locked "5 wallets per user" and single-price decisions in spec.md.

Provisional: revisited after Phase 0 measures the cost of syncing wallets ([0017](0017-launch-scope.md)).

## Question

5 wallets is plenty for newer traders but useless for advanced traders with 10-30+ wallets.
How do we price both without a complicated plan grid?

## Options considered

- Base + Pro.
- Base + Pro + Whale (100 wallets).
- One plan plus wallet packs.
- One generous plan with 30 wallets.

## Decision

| | Base | Pro |
|---|---|---|
| Trading wallets | 5 | 30 |
| Everything else | same | same |
| 30 days | $20 | $50 |
| 90 days | $50 | $125 |

- The only difference between plans is the wallet count.
- The trial is 7 days, capped at 5 wallets. Adding a 6th wallet offers Pro on the spot.
- An EVM address still counts once across Base, BNB and Robinhood Chain.

## Why

- Two plans keep a $20 entry for newer traders and let advanced traders, who get the most value, pay more.
- No feature differences means nothing to compare or explain.
- Capping the trial at 5 avoids a downgrade step where users choose which wallets to drop.

## Consequences

- Assumption: extra wallets are cheap for us, because a provider pushes wallet activity to us instead of us polling every wallet.
  The Phase 0 data spike (0001) measures the real cost per wallet at 30 wallets per user.
  If it's wrong, Pro's price changes, not the structure.
- No Whale tier or wallet packs until real users ask for them.
- Billing (Phase 8) stores the plan alongside `paid_until`; upgrading mid-period is settled in the Phase 8 plan.
