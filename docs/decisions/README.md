# Decision records

A short record for every decision that changes the spec or architecture, written before the docs are updated.
File name: `NNNN-short-title.md`.

```markdown
# NNNN - Title

Status: open | decided | superseded by NNNN
Date: YYYY-MM-DD

## Question
## Options considered
## Decision
## Why
## Consequences
```

## Open decisions

| # | Question | Settled by | Status |
|---|---|---|---|
| 0001 | Trade data API: Mobula or Zerion, plus push (Helius webhooks on Solana, address-activity webhooks on EVM) vs polling, cost per wallet at 30 wallets per user, and token transfers as well as swaps | Phase 0 spike | open |
| 0002 | Payment processor for USDC on Solana | Phase 0 spike | open |
| 0003 | Discord install path: user-installed app or joining the TrenchM8 server | Phase 10 spike | open |
| 0004 | Does the Chat SDK need a Redis state store on Vercel | Phase 0 spike | open |
| 0005 | Discord monetization policy: is linking to web checkout allowed | Phase 10 spike | open |
| 0006 | Token build: Style Dictionary or a small script, from `design/tokens.json` | Phase 1 plan | open |
| 0007 | M8 glyph design | Before Phase 1 | open |
| 0008 | Chat audio retention (proposal: transcribe, then delete the audio) | Phase 3 plan | open |
| 0009 | Product analytics tool and funnel events (start, wallet, first reply, paid) | Phase 1 plan | open |
| 0010 | Legal pages: Terms, Privacy, not financial advice | Phase 9 plan | open |

## Decided

| # | Decision |
|---|---|
| [0011](0011-trade-closing-and-thesis.md) | A trade closes when what's left is worth under $1; M8 asks the thesis after the buy and quotes it back at the close |
| [0012](0012-wallets-and-transfers.md) | Trading wallets only, one slot each; internal transfers keep cost basis; M8 asks once about tokens sent to an untracked wallet |
| [0013](0013-plans-base-pro.md) | Base (5 wallets, $20 / $50) and Pro (30 wallets, $50 / $125), identical otherwise |
| [0014](0014-m8-model-routing-and-caching.md) | M8 routes templates, Haiku 5.5, Sonnet 5.5 low and Opus 5.5 by task, with prompt caching and the Batch API |
| [0015](0015-pnl-unit.md) | PnL in each chain's native coin with a USD total, switchable to USD |
| [0016](0016-m8-knowledge.md) | M8 knowledge: one short coaching note in the prompt; patterns and coin safety checks in code; originals archived |
| [0017](0017-launch-scope.md) | Launch scope: Telegram first, all 4 chains, M8 only in the chat app, all proactive messages, 4 tags, 5 rules, trench data in the brief |

The decisions already locked are in the table at the top of [spec.md](../spec.md).
