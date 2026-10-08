# Reading market conditions

<!-- Based on: memecoin guide, sections 08 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks whether the market is hot or cold, bull or bear, how much to trade or size right now, or whether to trade more to make back losses in a quiet stretch.
It also serves reviews of a losing week or month where the question is whether the trader or the market was the cause.

## In short

- Size and activity follow conditions. Most losses come from trading the same way in every regime.
- Two indicators matter most: price action of the majors (BTC, ETH, SOL) and on chain activity in the trenches.
- Where the activity sits matters too: a new launchpad that catches on can carry a run of fresh launches even when the wider market is mixed.
- Fresh launches regularly reaching 5M to 10M or more is a hot read. Launches topping near 500K and dying is a cold read.
- Good conditions call for high risk mode: more capital, more screen time, aggressive early entries. Bad conditions call for low risk mode: less capital, fewer trades, lower risk setups, more time away.
- In bad conditions the one job is protecting capital until good conditions return.
- Trading more or bigger to make up for a dead market backfires. Bad conditions punish effort, they do not reward it.
- Do not try to call the exact top or bottom. Read the surroundings, adjust behaviour, and do not fight the turn from bull to bear.
- Cold weeks happen inside bull markets too. In a cold week, slow down and do not push harder.

## The two main indicators

- Majors: BTC, ETH and SOL price action is one of the two most reliable indicators of the regime.
- On chain conditions: how active the trenches are, meaning coins launching, running and dying every day.
- How to check the majors: getTokenData on BTC, ETH or SOL gives price and 24h change. getMarketSentiment gives the crypto Fear and Greed index. getCryptoNews gives recent headlines.
- M8 has no candle data, so a sustained downtrend or new highs need to be confirmed by the trader on a chart.
- M8 has no market wide memecoin launch or graduation statistics and no on chain volume across the trenches. The trader should check a launchpad leaderboard or an on chain dashboard themselves.

## Questions to ask regularly

- How high are coins reaching in market cap? Do fresh launches regularly hit 5M or 10M or more, or do they top at 500K and die?
- How active are the trader's group chats and X feed? Is there excitement or quiet?
- What does on chain volume look like?
- Are people outside crypto talking about it? Are friends who ignore crypto asking about Bitcoin again?
- The answers set a risk level. The guide gives no numeric cutoff for switching modes, so these are judgement signals.
- Josh confirmed the 5M, 10M and 500K benchmarks still hold in October 2026. Comparing this week with a month ago adds the trend on top of the level.

## Bull and bear signals

- Bull signals: Bitcoin making new highs or holding well above prior cycle levels. Total crypto market cap expanding. Solana memecoin volume consistently high. Active Telegram groups surfacing several runners a week. Fresh launches regularly breaking out past 10M. Outsiders asking about crypto again.
- Bear signals: Bitcoin in a sustained downtrend. Memecoin volume drying up. Quiet groups. Coins topping near 500K where they used to top near 5M. The same capital rotating among the same few coins with nothing new breaking through. People publicly leaving the space and declaring crypto dead.
- The switch is rarely obvious in the moment. It happens gradually, then suddenly.
- The trader who stays stubborn after the evidence points to lower risk pays for it. Fighting the turn is a named mistake in the guide, and it cost its author heavily.

## High risk mode and low risk mode

- High risk mode (good conditions): more capital deployed, more screen time, higher risk setups, aggressive early entries.
- Low risk mode (bad conditions): less money deployed, fewer trades, lower risk setups, more time away from crypto.
- The source covers memecoins only: it says nothing about perps, leverage or shorting in bad conditions.

## The risk dial

- Memecoins are the high risk end: pure attention, no fundamental floor, can go to zero in hours or 100x in days.
- Utility coins sit in the middle: usually slower, more fundamental support, less likely to go to zero overnight and less likely to 10x in a week.
- Ownership coins are the low risk end: tied to company valuations, slow, closest to traditional investing.
- In a strong bull market, sit nearer the memecoin end. As conditions worsen, rotate to utility, then ownership, then out of crypto into cash or stables.
- Most traders never turn the dial. They stay in memecoins through bear markets and keep losing because the instrument does not fit the conditions.
- It is a principle, not a rigid rule. In a hot narrative, utility coins can trade like memecoins. Past example: in an AI narrative, teams with only a plan and nothing delivered went from 0 to about 50M in under a week.
- Capital flow follows conditions. In good times liquidity and attention go to the highest risk assets. In bad times large players move to safer assets and quit memecoins or hold only a little. The guide's advice is to move with that flow.

## The cost of forcing trades

- When coins are not running, most traders trade more and bigger to compensate. That is backwards.
- Survivors across cycles do less when the market gives less. They stay quiet, protect capital, and stay sharp and rested to catch the next opening.
- The alternative is burnout and a drawdown of around 60% from forcing a dead market.
- How to check: getTradeAnalytics by week and by month shows trade count, size and PnL over time. Compare these with how coins were performing in the same weeks.

## Cycles within cycles

- Even in a bull market there are cold weeks and hot weeks.
- Signs of a cold week: the trader's group was finding runners and suddenly volume dries up, market caps top lower than usual, and nothing holds its gains.
- The response is to slow down.
- Pushing harder is the instinct working against the trader. Traders then blame themselves for not finding good trades, when the market is simply not in a giving mode.
- How to check: getTokenDetail on recent coins shows mcap vs all time high. If recent runners all sit far below their highs and top lower than a month ago, the week is cold.

## The widening skill gap

- The game is structurally harder than before. Past example: years ago a trader could buy a coin tied to big news 20 minutes late at about 10K cap, see liquidity locked, and profit.
- Today experienced traders with pattern recognition, multiwallet operations and sniper bots can buy about 10% of a coin at 4K cap within 5 seconds of the news. The 4K, 10% and 5 seconds figures are illustrative, not measured.
- Beating that is not impossible, but the edge built through understanding matters more than ever. The gap between informed and uninformed traders has never been wider.

## In the trader's own trades

- Forcing a dead market. Shows as trade count and size rising in weeks when coins were not running, with PnL falling. Check getTradeAnalytics by week for count, size and drawdown, and getTrades for entry mcap. Question: what changed in the market that week, and what changed in you?
- Size not turned down. Shows as the M8 trade reads "Nx size" or oversized in getJournalEntries during a cold stretch, or larger size and leverage in getTrades. Question: did you reduce size or take time off when conditions turned, or hold the same style?
- Revenge and chase in a cold market. Revenge reads (back into the same coin after a loss at same or bigger size), chase reads (back in within minutes of closing) and "after N reds" clustering in cold weeks suggest the trader is pushing to recover. Question: were these entries planned, or were they about the previous loss?
- Same bull setups in a bear regime. Aggressive early entries and low entry mcap trades that kept going after launches stopped running. Check entry mcap and exit mcap in getTrades, plus the playbook in getPlaybooks. Question: which of your setups has the market stopped paying for?
- Stubbornness through a regime change. Rule breaks in the journal (rules followed and broken) that cluster after conditions worsened. Question: when did your rule breaks start, and what was the market doing then?
- Self-blame in cold weeks. Journal notes and daily recaps blaming skill for not finding trades when volume had dried up. Question: after a losing week, did you check whether the market was giving?
- Racing bots on news coins. Shows as quick losses on coins bought right after a news event, where faster wallets bought far lower in the first seconds. Question: can you realistically compete with bots and multiwallet traders for that entry?
- No time off. A long run of trading days with no gap through a cold stretch, shown by getTradeAnalytics by week. Question: when did you last take a day away from the screen?
- The regime itself is not labelled in the trader's data. Matching weeks to conditions needs the trader's own account of what the market was doing, or the majors via getTokenData and getMarketSentiment for the current week.

## Judgment calls

- The thresholds (5M, 10M, 500K) are rules of thumb, confirmed current in October 2026. There is no numeric rule for switching modes, so these are judgement signals, not cutoffs.
- Leading signals (launch ceiling, volume, nothing holding gains) pull against lagging ones (group quiet, people leaving). The lagging ones confirm, the leading ones warn.
- Not calling tops and bottoms pulls against not fighting the turn. The resolution is to adjust gradually as signals stack up rather than all at once on a single read.
- The risk dial is a principle: narratives can make utility coins behave like memecoins, and a trader may reasonably stay in memecoins by trading smaller and less often.