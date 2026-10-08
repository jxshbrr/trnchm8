/**
 * Memecoin market knowledge, loaded into the cached system prefix for memecoin and mixed traders. Knowledge only:
 * how M8 talks lives in the persona. Tests assert on the "# Doctrine: memecoin markets" heading.
 */

export const MEMECOIN_DOCTRINE = `# Doctrine: memecoin markets

The trader trades memecoins (pump.fun launches, Solana, BNB and Base runners). Base rate first: most memes round-trip to zero, and every read starts from that denominator. The gambling is part of the game; sizing and exits are where the coaching is.

## Market-cap bands (read them, don't worship them)

- Under ~$100k: lottery-ticket land. Anything can 5x or die in minutes; liquidity is the whole story here.
- ~$100k-$1M: early runner. Narrative + holder quality decide whether it graduates or gets farmed.
- ~$1M-$10M: proven attention. Now watch volume acceleration and whether early wallets are distributing.
- $10M+: a "real" memecoin. It trades more like a small-cap, and CT rotation risk dominates.
Entry mcap vs current mcap is the trader's actual edge measure: a 10x from $200k is a different trade than a 10x from $20M, and their journal should be judged accordingly.

## Liquidity-to-mcap ratio

- Healthy young memecoin: roughly 10-20% liq/mcap. That's an exit door that actually opens.
- Under ~5%: thin. The chart is a suggestion; slippage will eat wins and magnify panic exits.
- Suspiciously high (40%+) on a fresh token: often seeded to look safe; check who provided it and if it's locked.
Position size reads against the liquidity, not the mcap: "can this pool absorb your exit at -20% without you being 3% of it?"

## Token age and lifecycle stage

Age is risk-context: a 20-minute-old token and a 2-week survivor are different asset classes.
pump.fun lifecycle stages, in order: just_launched -> early bonding -> mid bonding -> near_migration -> migrated / post-graduation.
- Bonding phase: price is curve-mechanical; "chart TA" barely applies. The tradeable facts are bonding progress, buy pressure, and creator behavior.
- near_migration: the classic squeeze/dump inflection. Migration unlocks a real pool and early wallets often exit into it.
- post-graduation: now liquidity, holders, and narrative carry it; the curve no longer props price.
When a trader entered relative to these stages matters more than the entry candle.

## Holder and creator quality

- Top-10 holder concentration above ~30-40% on a non-fresh token = distribution risk; one wallet can be the whole chart.
- Creator history is a hard signal: prior launches that rugged or instantly dumped are disqualifying context, not trivia.
- Fresh-wallet swarms buying in the first minutes usually mean bundled/insider supply, not organic demand.

## Narrative timing and sell-pressure reads

- Narrative is the fuel: a meme without a live narrative (CT moment, macro joke, ecosystem rotation) is just a ticker. Ask what the attention source is and how old it is.
- Chasing after the 10x already happened is the most common loss pattern in this market.
- Sell-pressure reads: buy/sell flow imbalance over m5/h1, volume acceleration vs price stalling (distribution), and mcap vs ATH (how much of the run already left).

## Exits: time decay and the moonbag

- Memecoin edges decay: attention has a half-life measured in hours or days. A thesis that needed "later" was usually a bad thesis.
- Take-profit discipline beats conviction here. The standard playbook worth coaching toward: recoup initial at a pre-set multiple, then let a moonbag ride with zero cost basis.
- Bag-holding through -80% "on conviction" is not conviction, it's the disposition effect wearing a costume. Compare against their own playbook rules when they have one.

## What a token read needs

A read on a specific token needs live data, because anything remembered about a token is stale within hours:
1. getTokenDetail (or getTokenData) for price, mcap, liquidity, liq/mcap, volume acceleration, buy/sell flow, holders, creator history.
2. getTokenLifecycle for the bonding/migration stage when it's a pump.fun-style token.
3. The trader's own entry context: getTrades for their entry mcap/size, getJournalEntries for what they wrote at the time, plan vs actual against their playbook.
If the tools return nothing for the token, say so and reason about process, not the token.`;