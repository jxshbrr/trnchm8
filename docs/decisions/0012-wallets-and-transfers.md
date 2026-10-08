# 0012 - Trading wallets and transfers between them

Status: decided
Date: 2026-10-08

## Question

Advanced traders use 10-30+ wallets and move tokens between them.
How do we keep PnL right without building wallet roles, cluster detection or other machinery?

## Context from the trader interviews

- Traders spread across many wallets to hide how much supply they hold, to dodge copy-traders and wallet trackers, to bundle buys at launch, and to separate strategies.
- Supply moves by direct token transfers, through fund-and-split chains, through fresh burners funded from a CEX, and through bridges, swaps or mixers.
- CEX-funded burners break the funding trail on purpose, so automatic wallet linking can never be complete.
- Advanced traders will add their wallets if they're handled carefully: addresses only, never shown in shares or recap cards, deletable. This is care, not a marketed guarantee ([0017](0017-launch-scope.md)).

## Options considered

- Wallet roles (Trading, Sniper, Farm, Vault) with auto-detection.
- Per-trade detection of wash trades and bot snipes.
- Trading wallets only, declared by the user.

## Decision

- Users add the wallets they trade from. One wallet, one slot. No roles and no farm or sniper detection.
- We read spot swaps only: no perps, no LP, no staking.
- Transfers between tracked wallets are internal moves: cost basis follows the tokens (FIFO per user, chain and token across all wallets), and nothing is realized.
- Tokens sent to a wallet we don't track: the position stays open as "moved out", and M8 asks once:
  - **Mine, track it:** the wallet is added (uses a slot) and its sells count.
  - **Not mine:** closed at market value at the time of the transfer, counted as an exit, not a loss.
  - **Ignore:** stays "moved out" with no PnL.
- Tokens received from outside (airdrops, a friend, creator rewards, an untracked wallet) start at zero cost.
  M8 asks what they paid only when one gets sold for real money ("bought it elsewhere? what did you pay?").
- Devs who launch coins are normal traders: dev buys and sells are fills, and creator fees count as income.

## Why

- The first version of this product failed from complexity; one simple model beats clever detection.
- User-declared wallets work even when funding trails are broken on purpose.
- The untracked-transfer question catches the main trick advanced traders use, at the moment it happens.

## Consequences

- Farming or sniper wallets added by a user count in their stats; that's their choice.
- Wallet addresses are sensitive data: never in shares, recap cards, logs or third-party analytics.
- The data spike (0001) has to return token transfers as well as swaps.
