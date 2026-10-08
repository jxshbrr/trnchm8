# 0015 - PnL unit

Status: decided
Date: 2026-10-08

## Question

Do memecoin traders count in SOL or USD?

## Options considered

- SOL on Solana, USD elsewhere.
- Native coin per chain, with a USD total.
- USD everywhere.

## Decision

- PnL is shown in each chain's native coin: SOL on Solana, ETH on Base, BNB on BNB Chain, and the native coin on Robinhood Chain.
- A USD total sits next to it, so a mixed day still adds up.
- The user can switch everything to USD in onboarding and in Settings.

## Why

- Solana traders think in SOL ("up 14 sol today"), and USD PnL is distorted when SOL itself moves.
- A USD total keeps multi-chain days readable.

## Consequences

- Cost basis is kept in both the native coin and USD at fill time.
- M8's messages, stats, charts and recap cards all respect the chosen unit.
- Rules with money amounts (loss limit, max position) are set in the user's unit.
