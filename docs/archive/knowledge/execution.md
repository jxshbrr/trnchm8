# Trade execution

<!-- Based on: memecoin guide, sections 9 and 13 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks why they keep losing despite finding decent coins, how big a position should be, whether to hold or sell something they already own, whether an entry is FOMO, how to take profit, when to cut a loser, or how a newer trader should start.
It also serves any review of the trader's stored trades for sizing, chasing, roundtrips and missing exits.

## In short

- Most traders lose on execution, not on coin picking. Entry, size, profit taking and loss cutting matter more than finding the coin, and managing the trade matters more than the entry.
- Before a buy, know why you are buying and what would make you sell. Write it down. If the reason cannot be put into words, there was none.
- Size by share of portfolio and by conviction. The test is: if this goes to zero, can I still trade normally tomorrow? If not, it is too big.
- A trade near 5 times the trader's normal size is the typical blow-up pattern, usually driven by overconfidence.
- Spreading small amounts across about 20 coins is a common and costly habit. Only hold coins you have researched and can follow.
- Chase test: if I had never seen this chart, would I buy right now? If the honest answer is no, it is FOMO.
- Take profit in portions on the way up, with the plan made before the buy. Roundtrips from 5X or 10X back to breakeven catch experienced traders as often as beginners.
- A 40% drop with no new information to explain it is a stop signal. Respecting it is the skill that keeps the trader in the game.
- Newer traders: risk only an amount that can be lost entirely, treat early deposits as tuition, paper trade first, and withdraw part (not all) of the first big win.

## The thesis: why you buy and what makes you sell

- The rule: before any buy, the trader states why they are buying and what would make them sell. Most people need to write it down. Only a few can hold it in their head.
- Why it holds: many traders cannot name a reason once asked, which means there was none. Writing it also tests the real information edge, because vague bullishness collapses in words.
- The thesis is the anchor for every later decision. When price drops, news lands or the group panics, the only question is whether the original thesis is still intact. If yes, hold. If no, act.
- How to check: getPlaybooks shows whether the trader has written entry, sizing and exit rules. getJournalEntries shows notes, tags, rules followed and rules broken on the trade. A trade with no note, no rules followed and no exit condition was entered without a thesis. M8 has no required thesis field, so the trader may need to say the thesis out loud.

## Information edge, and how the thesis ages

- The best trades tend to come from an information edge: knowing something very few others know yet. The guide's example: researching a new coin's dev (old posts, who followed the dev, a rumoured credible group) before anyone posted about it, sizing up, and being up a couple of X when legitimacy showed on the chart.
- The edge is time sensitive. It exists only until the information is public and priced in.
- Day one and day seven are different decisions:
  - Day one questions: is the dev legit, is the narrative fresh, am I early?
  - Day seven questions: is the team building, when does the product launch, is the community growing?
- By day seven the information edge trade has played out. A launch thesis has an expiry date, so the trader keeps re evaluating and does not marry the bag.
- Holding for the launch thesis and holding because you like the project's future at today's price are different decisions. Know which one it is.
- How to check: getTokenDetail gives age in minutes, mcap versus all time high, holder count, top 10 holder percent, creator address with prior launch count and rug signal names. getTokenLifecycle gives bonding stage and migration. These cover the day one questions only partly. Dev legitimacy beyond prior launches, who follows the dev, and social signals are not in M8's data, so the trader should check X and Telegram themselves and report what they found.

## The hold test: would I buy this now, and how much

- The rule: the most important trade management question is whether the trader would buy this coin if they found it only now, and how much they would buy.
- The gap between what they would buy now at today's price and what they currently hold is the amount to sell. If there is no gap, they are effectively making a brand new trade.
- The same test works on winners. If I did not own this coin and saw it at this price, would I buy? If no, sell something, though not necessarily everything.
- When it bends: the rule ignores fees, slippage and tax, and on illiquid memecoins the exit itself can cost real money, so the gap is a guide to direction and rough amount, not an exact figure.
- How to check: getTokenData for the quote, getTokenDetail for liquidity, liquidity to mcap, volume and buy and sell counts, getTrades for the held size. The answer belongs to the trader, so ask what they would buy now.

## Position sizing

- The rule: think in percentages of the portfolio, not absolute amounts. The guide's example is 20% of a portfolio in one memecoin at a 50K market cap against 2%, which are very different decisions.
- Sizing is where beginners go wrong most. Too big on a bad coin wipes them out. Too small on a good coin means the win does not move the portfolio.
- The simple rule: size so a win feels like a win and a loss does not hurt enough to affect the next decision. Emotional damage from a loss is as real as financial damage, and a loss that triggers revenge trading costs the trader twice.
- The pre trade test: if this goes to zero, can I still trade normally tomorrow? If not, the size is too big.
- Scale with conviction on top of the portfolio rule.
  - Very bullish, non public information that almost nobody has: size a lot.
  - Public information where the only edge is that the coin launched about 5 hours ago while the American session sleeps: size less.
- Sizing discipline has to grow with the portfolio. Blow ups come from sizing and management, not bad picks, typically a bad trade at about 5 times normal size because of overconfidence. Confidence is not an edge. It is a liability if it makes the trader oversize.
- No fixed cap is given. The example rule is a personal cap such as "never above X% of the portfolio on a memecoin under 500K market cap", where X is the trader's own number, best chosen from their own history.
- How to check: getTrades gives size and entry mcap per trade, and getTradeAnalytics shows payoff and drawdown. The total portfolio value is not available to M8, so the share of portfolio is known only if the trader says it. getUserProfile has the size band. getGoals may hold a daily loss limit. Ask the trader for the portfolio value and what they would be left with if the position went to zero.

## Spreading across too many coins

- The rule: small amounts across about 20 coins out of fear of missing something is one of the most common and costly habits.
- Why it holds: the trader cannot follow every coin daily, and with too many positions the winners are too small to matter while the losers still add up. Concentrated conviction beats spreading thin. Only buy coins you have researched and can keep following.
- How to check: count overlapping positions from entry and exit dates in getTrades. getTradeAnalytics by symbol shows how thin the book is. Ask whether the trader can name the thesis for each open coin.

## FOMO entries and the chase test

- The rule: the worst time to buy is when the urgency comes mainly from price action. Green candle after green candle, an excited group and fear of missing out are not reasons.
- The chase test: if I had never seen this chart, would I buy right now? If the honest answer is no, it is FOMO.
- Fix: define the entry, size and price before the excitement starts, then monitor whether the thesis is intact, not every candle, because a one minute candle presents noise as meaning.
- Why it holds: late entries into already pumped coins are among the most reliable ways to lose money, because the sellers into your buy were earlier and know it.
- When it bends: being late is not always wrong. Some coins take weeks to finish their move, and a researched late entry into a strong narrative can work. The difference is a deliberate decision on thesis versus an emotion driven chase.
- How to check: getTokenDetail for mcap versus all time high, volume acceleration, buy and sell counts and age in minutes. getTrades gives entry mcap and the journaled flag. M8's chase read in getJournalEntries marks a re entry within minutes of closing. Candle data is not available, so momentum before entry needs the trader's own chart.

## Taking profits and the roundtrip trap

- The rule: scale out gradually on the way up, because the top cannot be timed. Sell a portion when making good money, another when euphoria creeps in, and let the rest run only if the thesis and price still make sense together.
- Why it holds: it locks in money, reduces risk and keeps upside exposure. Profit taking is the most important thing when sitting on a winner.
- The specific targets matter less than having a plan before the buy, not after the coin is already up 5X and greed has taken over.
- The roundtrip trap: at 5X the brain starts calculating what 10X would mean, at 10X it calculates 20X. Experienced traders get caught as often as beginners. A chart can go up the stairs and come down the elevator.
- If the trader is up a life changing amount, take profit now, not eventually, because the "just a little more" number keeps moving until it is too late. The guide gives no figure for this.
- How to check: getTrades has entry and exit mcap, PnL, result and the moonbag flag. There is no record of a position's peak unrealised gain, so a roundtrip can only be seen through journal notes or by comparing entry and exit mcap, for example a trader who mentions 5X or 10X and then closed near breakeven. A single lump exit at the end, with no partial sells, suggests no scaling plan, though partial exits depend on how the trades were stored.

## Stop signals and cutting losses

- The rule: have hard stop rules. A 40% drop with no new information to explain it may be the market telling the trader something they do not know yet. It is a rule of thumb for coins with no news, not a universal stop.
- Why it holds: respecting a stop feels like admitting you were wrong, and it is, which is the skill that keeps you in the game.
- Large losses are rarely bad luck. They are hidden process weaknesses: unchecked bundled supply, a thesis weaker than admitted, size too big for the real conviction, ignored red flags.
- Bearish information: do not hold the whole position when bearish news appears, even if unsure about it. Reduce and sell some.
- Two wrong reactions to a loss: sizing up to win it back fast, or quitting out of fear. The right one is to name the precise failure (oversizing, no exit plan, ignored red flags, emotional entry, not managing the trade on bearish information) and turn it into a concrete rule.
- The trader is trying to make money, not to make the money back. Those are different mental states and only one leads to good decisions.
- After a large drawdown, pressure to win it all back leads to entries with no edge and no thesis and can take an account to zero. Recovery comes from stopping, waiting, coming back small and buying only with real conviction.
- How to check: getTrades for the loss, entry versus exit mcap and the date. getTokenDetail for rug signal names and top 10 holder percent now. getCryptoNews and webSearch for bearish news the trader held through. Bundle clustering and single top holder or dev share are not available, so the trader should check bundles on a chain explorer or bundle checker and report back.

## Journaling and turning losses into rules

- Journal significant trades, especially losses: entry, reason, thesis, what happened, and what went right or wrong. Not every small trade, only those where something was learned or should have been.
- The same mistake three times without understanding why is paying tuition without attending class.
- How to check: getJournalEntries for notes, rules followed and broken, and tags. getPlaybooks for whether a rule already covers the mistake. A coach can offer to add the new rule to a playbook.

## Starting rules for newer traders

- Size as tuition: start with an amount that can be lost completely without affecting the trader's life. If losing it would cause stress, it is too much. The first weeks or months are for learning, not earning, and early deposits are spent on that.
- Paper trade first. Record the trade without making it: the coin, the entry price, the thesis and what would make the trader sell. Then manage it and follow the result.
- Paper trading forces a thesis before entry, shows how often instincts are right without cost, and builds the habit of documenting trades before real money is on the line.
- Public Telegram channels are information streams only, never buy signals. Use them to surface coins, then research. Some channels take undisclosed paid deals. Beginners who follow big call channels tend to lose because they lack the pattern recognition for when to enter, exit and ignore a call.
- Feed: follow people who post real research and show their reasoning, preferably low to medium follower accounts, and avoid accounts posting around 15 coins a day with price targets and no explanation. Three real traders in a private group are worth more than a public channel of 50,000. Writing one's own thinking out loud from day one builds the thesis habit.
- After the first big win, withdraw part of it (not all) to a bank account. Seeing real money land makes the win feel real, gives the trader something to protect and changes how they trade. Traders who leave everything compounding never feel what winning was, so the first loss hits harder. The guide gives no percentage, so the trader chooses theirs.
- One good trade does not make a good trader. Watch for size jumps or loosened rules right after a win.
- How to check: getUserProfile for experience and size band, getTrades for early sizes and the journaled flag. M8 has no paper trade mode, withdrawal record or entry source data, so the trader should say whether they paper traded, what they withdrew and where each coin came from.

## In the trader's own trades

- No thesis or exit condition. Shows as a trade in getTrades with journaled false, or a journal entry with no note, no rules followed and a low or missing rating. Question: what was the reason for this buy and what would have made you sell?
- Revenge sizing and re entry. Shows as M8's revenge read, "after N reds", or a larger size right after a big loss with quick entries and low ratings. Question: are you trying to make money or trying to make it back?
- Overconfidence oversizing. Shows as the oversized read or an "Nx size" tag near 5, especially after a win streak. Question: has confidence turned into size, and could you trade normally tomorrow if it went to zero?
- FOMO chase. Shows as the chase read, a high entry mcap relative to the all time high from getTokenDetail, a young coin bought late in its run, no notes and a low execution rating. Question: if you had never seen this chart, would you buy now?
- Spreading thin. Shows as many small trades with overlapping dates in getTrades. Question: can you follow each of these coins daily, and what is the thesis on each?
- Held too long. Shows as the held too long read, a loser held past the trader's usual winning hold, or a deep loss with no exit and no note about new information. Question: what new information justified holding through a 40% drop?
- Roundtrip and lump exits. Shows as journal notes mentioning a large multiple with a final exit near breakeven or a loss, or one lump sale with no partials. Question: was there a profit plan before entry, and did you scale out?
- Repeated mistakes. Shows as the same rule appearing among rules broken across three or more trades in getJournalEntries, with no matching rule in getPlaybooks. Question: is there a written rule for this yet?
- Newer trader patterns. Shows as large sizes from a beginner in getUserProfile, or size jumps right after a first big win. Question: is this money you could lose entirely, and did you withdraw any of the win?

## Judgment calls

- The 40% stop (confirmed by Josh), the 5X sizing flag, "about 20 coins" and the 5 hour launch example are rules of thumb and examples, not universal limits. The guide gives no recommended portfolio percentage, so a coach helps the trader choose their own from their history.
- Conviction and the zero test can pull against each other. The zero test sets the ceiling and conviction decides where under it.
- A coin can fail the "buy now" test while the thesis is intact, because price already reflects it. That points to trimming, not necessarily exiting.