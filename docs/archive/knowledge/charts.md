# Reading memecoin charts

<!-- Based on: memecoin guide, sections 07 (docs/m8/knowledge/sections/), with two lines from section 02 and Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks whether a chart looks good to buy, whether a setup is broken, where to enter or exit, which timeframe to use, how to draw levels or Fibonacci retracements, or whether to panic out of a position after a scare.
It also serves questions like "is this the bottom?", "did my level fail?" and "why does my line not hold?".

## In short

- A chart answers one question: is price going up, going down or going nowhere. Uptrend is likely a good buy, sideways is probably not, downtrend is likely not, and a turn from down to up is maybe.
- Trend is market structure: higher highs and higher lows is an uptrend, lower highs and lower lows is a downtrend. Indicators beyond that add little.
- A break of structure is the key signal: in an uptrend, price falling below the most recent higher low. In a downtrend, price rising above the most recent lower high.
- Be a little late on purpose. Buy after a confirmed uptrend, ideally at the retest of broken resistance, not at a hoped for bottom. Do not be crazy late either.
- Lines and zones need history, for example a level tested three times in four days. A coin with a few hours of data has nothing to draw on.
- Fibonacci pullback zone: 0.5, 0.618 (golden zone) and 0.786, drawn only on a finished, clean directional swing. Fibs are a timing aid on coins with a few days of history, never on a coin under a day old.
- Set invalidation before buying. A close below 0.786, or a break of the higher low that made the swing, means the idea is wrong. On memecoins one candle is not enough, so watch the reaction.
- Confluence: one signal is a possible reaction, two is a tradable area, three or more is a high confidence setup.

## Trend direction and the starting rule

- The rule of thumb: uptrend is likely a good buy, sideways is probably not, downtrend is likely not, and down to up is maybe a good buy.
- Why it holds: structure shows whether buyers or sellers are winning without needing indicators.
- Chart reading is not looking for confirmation. Opening a chart, drawing lines everywhere and stacking around ten indicators to justify a trade already decided is rationalising, not reading.
- Where it bends: the down to up turn is the author's preference, and fresh memecoins rarely give a clean higher low and retest.
- How to check: M8 has no candle data. The trader can attach a screenshot and M8 records its read with recordChartAnalysis. Otherwise the trader checks the structure on their own charting tool. getTokenDetail gives mcap vs all time high, which shows how far the coin sits from its peak.

## Choosing a timeframe by asset and coin age

- Match the timeframe to the asset and the plan. A multi year hold of a commodity like gold belongs on a very high timeframe such as weekly, where a 15% one day crash that recovers by afternoon is noise.
- At the other extreme, a freshly launched memecoin is watched on a 1 second or 2 second chart to see what is happening live. At that age there is nothing to draw.
- Higher timeframes carry more weight: a 0.618 tap on the daily or weekly implies serious money, the same tap on 1 minute may be noise. Analyse high, sharpen entry low.
- How to check: getTokenDetail returns age in minutes and getTokenLifecycle gives bonding stage and migration time. Token age at entry is stored per trade but not yet surfaced in tools.

## When lines and zones become meaningful

- Price has memory: a level where buyers stepped in or sellers pushed back before may do so again.
- A line needs history. On a coin with only a few hours of data, even a 30 minute old one, a line is a guess. A level tested three times in four days is meaningful.
- After a few days, patterns appear: where early buyers took profit and where dip buyers came in.
- Anchor zones, lines and fibs to candle bodies, not wicks. Low liquidity means one buyer, for example a roughly 2K dollar buy on a low cap at a resistance zone, can spike a wick that reflects one person, not the market. A cluster of body closes is more credible than a single spike. This differs from the usual wick to wick advice in traditional markets.
- Wicks are the extreme high and low of the period. The body runs from open to close.
- How to check: the trader looks for several separate reactions at the level. getTokenDetail liquidity and age show how much weight one wick deserves.

## Market structure and its breaks

- Uptrend: each pullback ends higher than the last and each push goes higher than the last.
- Downtrend: each push up is rejected lower and each drop goes deeper. Do not buy it.
- Break of structure down: in an uptrend, price falls below the most recent higher low. That level was supposed to attract buyers and did not. It is a bearish signal to add to trade management, meaning tighten or exit.
- Break of structure up: in a downtrend, price rises above the most recent lower high. Sellers were supposed to reject it and did not. The pattern of lower highs has ended and the chart becomes interesting to buy.
- The guide treats the break of the high and low pattern as the single most important idea: when it breaks, something is changing.
- Past example, PayPal monthly: after a 2021 peak, price fell below the higher low from about 6 months earlier, and lower lows and highs followed. A thesis left unchanged after that break missed what the chart said.
- Past example, Coinbase weekly: after a downtrend, price printed its lowest low, a base, then broke above the lower high. The entry marked was the retest of the old resistance as new support after the first higher high, not the bottom.
- Past example, Bitcoin weekly: in early 2023 BTC sat around 15K to 20K in lower highs and lows. It broke above the previous lower high around 25K (another line near 31K) and ran to about 125K. The flip around 25K to 30K was the buy, even weeks later. At the top, lower highs and a break below a higher low around 85K to 90K was the exit.
- How to check: the trader marks the latest higher low or lower high on their chart. A screenshot can go through recordChartAnalysis.

## Being a little late, bottoms and panic

- Buying after a confirmed uptrend is far better than buying early hoping a downtrend ends.
- Lesson one: do not try to catch the bottom. In a confirmed downtrend with no sign of strength, cut the loss and find something else. Repeatedly calling the bottom while the chart prints lower lows is the error.
- Lesson two: zoom out when panic starts. If structure just turned bullish and the trader fears they bought the top, move to a higher timeframe. Many 15 minute scares look like nothing on the weekly because the trader was looking too closely.
- Thesis and narrative research are the edge. If the fundamentals back the chart, the trade is likely good.
- Lesson three: late is fine, crazy late is not. Judge it by how high coins can go in current conditions, how comparable coins in the same narrative moved, and on chain reading such as a top holder with about 2% of supply on large profit who may have a sell order. If unsure, wait. Opportunities are abundant.
- How to check: getTokenDetail gives mcap vs all time high, volume acceleration and top 10 holder percent. Single top holder share is not available, so the trader checks the holder list on an explorer. getMarketSentiment gives Fear and Greed.

## Fibonacci retracements on memecoins

- Fibs add precision on top of structure, feeding a wider bundle of information.
- Why price reacts: enough traders expect it, so it becomes self fulfilling.
- Trends move in waves: push, pause, pullback, continue. A shallow retracement means a strong trend, a deep one a weakening trend.
- The levels that matter are 0.5, 0.618 and 0.786. Most others are ignored. 0.5 is where strong trends retrace to and the minimum pullback to count as a new bottom. 0.618 is the golden zone and the most respected. 0.786 is the last chance: the deepest acceptable pullback before the setup is probably wrong.
- Drawing steps for an uptrend: after a new high, draw from the last swing low (the 1 line) to the new swing high (the 0 line). Wait for a pullback into the 0.5 to 0.786 zone. If price bounces off a level in the zone, that bounce point is the new bottom to anchor the next fib from. Then wait for the next new high to set the 0 line and wait again for a retracement into the zone. Entry is through a retracement with higher highs and higher lows intact. For downtrends, flip the tool.
- Draw only on clean directional moves. Never draw inside a sideways range, since no impulse means no meaningful retracement.
- Draw only after the swing is finished, with both top and bottom set and reacted to. Unfinished moves give false levels.
- Where it bends: the levels are conventions, not verified rules. Treat 0.5 to 0.786 as a rough band, especially on thin coins where levels get blown through.
- Settled (Josh, October 2026): fibs are only a timing aid, on coins with a few days of price history. On a coin under a day old they mean nothing, and attention matters more than any level.
- How to check: M8 cannot draw them. The trader attaches a screenshot for recordChartAnalysis.

## Confluence

- One signal is a possible reaction, two is a tradable area, three or more is a high confidence setup.
- Signals that stack with a fib level: previous support or resistance at the same price, a trendline through the same zone, a round number such as 0.01 or 1.00 dollars, and high volume areas.
- Past example: a coin makes a new high, pulls back and hits the 0.618 at exactly the price of its previous all time high, which now acts as support. That is two signals in one place and worth attention.
- How to check: the trader counts independent signals on their chart. getTokenDetail mcap vs all time high locates a previous high.

## Invalidation, overshoots and flips

- Invalidation is the point where the trade no longer makes sense. In a bullish fib setup, a close below 0.786 means the idea is probably wrong. If the higher low that created the swing breaks, the uptrend structure drawn on is gone. The guide says most traders fail with fibs not by drawing wrong but by refusing to accept the setup died.
- Set the level before buying, so the trader knows exactly when they are wrong.
- Memecoin exception: they overshoot levels constantly through wicks and liquidity grabs before reversing. One candle closing below a level is not enough, so watch how price reacts. Price can be a rollercoaster while fundamentals are not, so keep updating the thesis from live information.
- The classic sign a level has fully flipped: price breaks below, returns to test it from underneath and is rejected back down. Support became resistance, the setup is over and the chart turned bearish.
- How to check: getTrades shows entry and exit price and mcap, so the trader can compare an exit to the level they named. getPlaybooks shows whether the strategy states an invalidation rule.

## Why TA behaves differently on memecoins, and the thesis first

- Memecoins run on attention, so heavy technical analysis on a memecoin chart adds little now. Overthinking the chart tends to hurt more than help.
- The chart's job on a memecoin is to read structure and time the entry and exit around a thesis built on attention, not to predict the coin.
- Botted and honeypot patterns belong in the Token safety note: near identical candles suggest bots, and an up only chart on low volume with few holders is the honeypot lure.
- The process: build the thesis first from the narrative, the dev, on chain data and the community. Then use the chart to find the entry. The chart confirms or challenges the thesis and does not replace it.
- How to check: getTokenDetail gives creator address with prior launch count and rug signal names, holder count and buy and sell counts. The trader checks X and Telegram, bundle clustering and fresh wallet funding themselves, since M8 has none of that data yet.

## In the trader's own trades

- Buying a coin that keeps printing lower highs and lower lows because it looks cheap. In getTrades this shows as repeated entries on one symbol with entry mcap falling each time, or large drops from entry mcap to exit mcap. The question: what higher low or lower high break made you think structure changed?
- Holding a loser after structure broke with the thesis never updated: the held too long read in getJournalEntries. The question: what new information justifies holding, or is it hope?
- Panic selling on a 1 or 15 minute candle just after a good entry: a very short hold and fear in the journal emotions. The question: what does the higher timeframe show?
- Chasing a pump after it ran. The chase read in getJournalEntries and an entry mcap near the all time high fit this. The question: after a retracement or at the top?
- Entering with no stated invalidation, then ignoring the stop. Check rules broken in getJournalEntries and getPlaybooks. The question: where would this idea have been wrong before you bought?
- Drawing lines on a coin that is minutes or hours old. Token age at entry is stored per trade but not yet surfaced, so the trader checks it themselves. The question: what history does that level have?
- Treating a single wick as support on a low liquidity coin. The question: was that wick one large order?
- Trading the chart alone with no thesis. Journal notes with no narrative, dev or community reasoning show it. The question: what is the picture, and does the chart confirm or challenge it?
- A playbook can carry two rules: entered with structure, and had invalidation, tracked through rules followed or broken.

## Judgment calls

- Rules of thumb, not edges: the starting buy and skip rule, the fib band and "a little late". The guide gives no number for how late is too late.
- Waiting for a confirmed retest pulls against fast memecoins, where a retest may never come. A fresh coin often has no clean structure, so the trader decides whether to pass or trade on thesis.
- Overshoot tolerance pulls against invalidation discipline. One candle is not enough, but a failed retest from underneath settles it.
- Higher timeframes carry more weight, but a coin hours old has no higher timeframe. Lines then wait for days of history.
- Thin liquidity gives misleading wicks, while mature coins give cleaner swings. Stock and Bitcoin weekly examples teach structure but do not transfer directly to a launch.