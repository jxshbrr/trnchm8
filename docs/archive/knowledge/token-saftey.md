# Token safety

<!-- Based on: memecoin guide, sections 2 and 12 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks whether a coin is safe, bundled, a honeypot or a rug, or asks what to check before buying a new coin.
It also serves questions about slippage and thin pools, mint, freeze and LP checks, holder and volume numbers, suspicious charts, and fake dev posts or call channels.

## In short

- Among traders, the top holder (ignoring the liquidity pool row) should own no more than about 3.5% of supply, with some grace up to about 4 to 4.5%.
- The dev is judged separately. On a regular memecoin the dev should hold no more than 5%. On a tech, business or launchpad coin a dev share of 20% or more is common, and then it has to be locked, ideally with buybacks.
- Many traders now spread one position across several wallets, so a clean holder list can hide a controller with far more than 3.5%. Cluster checks and wallet tracking close that gap.
- Volume above market cap is the healthy target for a young coin. Volume under 80% of market cap is the floor: below it the coin is almost certainly a bundle.
- Avoid a coin with multiple fresh wallets among its holders, or one where most holders carry the bundler icon.
- More than 3 to 5 holders funded from the same source at about the same time is a bad sign.
- Liquidity must be locked or burned, and mint authority must be disabled. Freeze authority should be disabled too.
- A coin that rises almost without pullbacks, on low volume, with few holders, is a honeypot or coordinated pump until proven otherwise.
- A 15K market cap coin on Solana should have paid more than 0.5 SOL in fees (on Robinhood's chain, about 0.02 ETH by 15K to 20K). A tiny figure means fake or thin activity.
- Check the contract address across several channels, even when it comes from a trusted account, because accounts get hacked.

## Pool mechanics and slippage

- A trade is a swap against a pool, not against another person. The pool holds the memecoin and SOL, and price is the ratio between them.
- Worked example: a pool of 1 SOL and 100 tokens prices a token at 0.01 SOL. A 0.1 SOL buy takes out about 10 tokens, leaves 1.1 SOL against 90 tokens, and lifts the price about 22%.
- Why it holds: every slice of an order moves the price, so the average fill is worse than the first sliver. That climb across one order is slippage.
- A deep pool barely moves on a buy. A pool with only 1 SOL roughly doubles in price on a 1 SOL buy, fees aside.
- External slippage is separate. Other traders' orders land in the same block ahead of yours, so the fill is worse than the price seen at the click.
- If two buyers ahead of you pushed the price 2%, the trader gets about 2% slippage. Sells work the same way.
- More volume and more traders on a coin raise the chance of bad slippage.
- When it applies: slippage is normal on small, high volume coins and hurts most on low cap coins with shallow pools. Large established memecoins have very deep pools.
- Market cap is circulating supply times price. The creator picks total supply arbitrarily, so supply alone says nothing about value.
- How to check: getTokenDetail gives mcap, liquidity and liquidity to mcap, which together show how much a given buy will move price. getTokenData gives the quick quote. The trader's own slippage can be compared by reading entry price in getTrades against the price they saw at the click.
- Not yet available: slippage taken per fill. Liquidity at entry is stored per trade but not surfaced in tools.

## Rug mechanics: LP lock, mint and freeze authority

- The liquidity pool has to be locked, meaning the creator burned the keys that would let them withdraw the SOL. If it is not, the creator can pull all the SOL and the coin is worthless.
- Mint authority has to be disabled. If it is enabled, the creator can create new tokens from nothing and sell them into the pool until the SOL is drained.
- Freeze authority should be disabled. Left on, it is listed as a honeypot red flag, because the creator can stop wallets from selling.
- When it applies: coins launched on the main launchpads (Pump.fun, Bonkfun, Moonshot and Stonkfun on Solana, Pons on Robinhood's chain, and others) get these protections handled automatically. Coins launched by hand or elsewhere need the trader to check LP lock percentage and mint authority themselves.
- A healthy checker page in the guide showed the main pool 99.59% locked and mint authority disabled.
- How to check: getTokenDetail returns the creator address with prior launch count and rug signal names, which covers part of this. The trader should confirm LP lock, mint and freeze status on a token checker such as Rugcheck, because M8 does not report each of them directly.

## Launchpad stage and bonding curve

- A new coin trades first on the launchpad's bonding curve. When enough SOL has been swapped in and the coin hits a set market cap, it graduates to open trading on the wider chain.
- A launchpad page shows progress as a percentage. In the example, a coin at 90% needed roughly 10% more SOL in the pool to graduate.
- Why it matters: the launchpad handles LP and authority protections, so the stage shows which checks are already done.
- How to check: getTokenLifecycle returns bonding curve stage and percent, plus migration time and venue. Bonding stage at entry is stored on each trade but not yet surfaced in getTrades.

## Holder concentration and the top holder rule

- Among traders, the top holder should not own more than about 3.5% of supply when trenching. It is an unwritten rule of thumb with some grace: a holder at 4 to 4.5% is not an automatic pass.
- The liquidity pool nearly always sits at the top of the holder list and is not a trader, so it is ignored.
- Why it holds: if one wallet dumps, the pool equation drags the chart down hard, and unless the trader entered at a low market cap it will often put them in the red.
- Extreme example: two wallets at 62.79% and 35.47% of supply is an obvious bundle.
- When it bends: many traders now trade from several wallets at once, so one person can control well over 3.5% while every wallet sits under the line. The holder list does not show who controls each wallet, so the rule only works paired with the cluster and funding checks below and with tracking known wallets.
- How to check: M8 has top 10 holder percent in getTokenDetail, and holder count. It does not have the single top holder or dev share, so the trader should open the Holders tab on a chart site or terminal and read the top rows themselves.

## Dev share

- The dev's share is judged separately from traders, and the right number depends on the kind of coin.
- Regular memecoin: the dev should hold no more than 5%. On these coins the dev most often sells the dev wallet before migration, so a large dev share is supply waiting to hit the chart.
- Tech coin, business coin or launchpad coin: a dev share of 20% or more is common. Here the dev is not expected to sell, because selling would show the tech is not real. The supply has to be locked, ideally with buybacks.
- So a 20% dev share is a red flag on a regular memecoin and can be normal on a real tech or business coin, provided it is locked.
- How to check: getTokenDetail gives the creator address with prior launch count and rug signal names, but not the dev's share or whether it is locked. The trader reads the dev share from the holder list and confirms any lock on a token checker or the project's own announcement.

## Bundles: what they are and how to detect them

- Bundling means one person or entity holds supply across many wallets so it looks widely distributed.
- It is sometimes benign. Teams hold supply for operations, influencer hand outs, exchange listings or a market maker, which is an entity that trades with a lot of money to steer the chart. Held supply can create a supply deficit that lets price rise more easily.
- With bad intent it is one of the most common scams. A trend appears, copy tokens are launched fast, often by automation, and a bundler uses a multi wallet tool to buy a large share the moment liquidity is added.
- Later buyers enter above the bundler, who effectively sets the floor and is never at a loss while buying continues. The bundler can dump everything at once, or farm the chart by selling slowly while the token stays active.

### Bubble map

- A bubble map tool such as Bubblemaps shows top holders as bubbles sized by amount held. Linked wallets (same creation time, same funding source such as a centralised exchange, transfers between each other) form a cluster.
- A heavily bundled coin shows one big dense clump of overlapping yellow bubbles, which the guide estimates at roughly 50 to 80% of supply held by one trader.
- A healthy coin shows mostly small grey unlinked bubbles with only tiny clusters.
- It is slow on fast, high volume tokens, so the quicker checks come first.

### Fresh wallets and bundler icons

- Terminals tag holders from wallet activity. A fresh wallet icon (a green leaf) means the wallet is brand new. It is a big red flag, especially on coins just launched in the new pairs feed. The safe rule is to avoid any coin with multiple fresh wallets among holders.
- The bundler icon (red, three linked circles) is not decisive alone, since legitimate coins often have some. The rule is to avoid coins where the majority of holders carry it.
- Not in M8. The trader checks the holder list in a terminal.

### Funding origin

- Look at where each holder wallet got its money and when. In the guide's example, holders were funded 17 to 21 hours earlier from exchanges.
- More than 3 to 5 such wallets among holders is a bad sign. Both the source and the timing matter.
- Not available in M8. The trader checks it in the holder panel of their terminal or on a chain explorer.

### Is a cluster selling

- In a bubble map, click the cluster, copy a wallet, open it on a chain explorer such as Solscan, go to Balance Changes and filter by the coin's contract address.
- In the guide's example, the cluster's main wallet, also the launchpad creator at about 5% of supply, had only received tokens and had not sold.

### Dev buys and creator history

- Any significant dev buy (a DB marker on the chart) is a reason to ignore the coin or be very careful. A dev sell (DS marker) swings market cap heavily.
- How to check: getTokenDetail shows the creator address with prior launch count and rug signal names. The dev's share of supply is not available, so the trader reads it from the holder list.

## Volume, market cap and fees

- Volume should normally be higher than market cap, and the younger the coin the bigger the gap should be. Volume above market cap is the healthy target.
- The floor is volume at 80% of market cap. Below that, a young coin is almost certainly a bundle.
- Example: market cap $15.6K with volume $7K is about 45%, well under the floor. Avoid it.
- When it bends: some real coins fall short of the target, which is why the target is volume above market cap and the floor is the 80% line. The guide's own caveat is that heavily traded new pairs often show volume above market cap on day one, so a pass on this check is weak evidence alone, while a fail is strong.
- Fees paid: real trading generates fees. A 15K market cap coin should have paid more than 0.5 SOL in fees, and the example coin showed only 0.061 SOL. That is a sign of fake or thin activity. On Robinhood's chain the line is about 0.02 ETH by 15K to 20K market cap.
- How to check: getTokenData and getTokenDetail give mcap and 24h volume, with volume buckets and acceleration, and buy and sell counts. Compute volume divided by market cap from them. Fees paid is not available, so the trader reads it on a chart site or terminal.

## Chart patterns that signal bots or control

- Candles of near identical size, one after another, mean bots. Real supply and demand does not look like that.
- One large instant candle plus bot buys is a variation.
- Only huge candles are arguably the most obvious sign of a bundle: one party controls most of the supply and buys or dumps within a second.
- The staircase pattern is repeated small up steps with brief red pauses, building at a near constant pace. It is seen most commonly in honeypots.
- M8 has no candle data, so the trader reads the chart. getTokenDetail volume buckets and acceleration are a rough substitute.

## Honeypots

- A honeypot lures buyers with a beautiful, almost up only chart, then traps them. The causes are LP not locked, mint or freeze authority not disabled, or supply massively bundled.
- Fast rule: a coin going up almost without pullbacks on low volume with few holders carries three red flags together. Treat it as a coordinated pump or honeypot and avoid it, however good the chart looks.
- The sell side is the trap. With freeze authority on, the trader buys and then cannot sell.
- How to check: getTokenDetail for holder count, volume and buy and sell counts, and the creator signals. A chart read and the authority check on a token checker complete the picture.

## Fake dev posts and call channels

- A hacked X account of a trusted dev or influencer can post a contract address or link. The guide gives a real case of it. Verify any contract address across several channels, even from trusted accounts.
- A coin's X community can hold a post under the pinned one reading "dev live active" that looks popular thanks to bot comments (231 in the example). It links to a clone of a big launchpad site, and logging in or connecting a wallet empties it. Lookalike domains differ by one subtle character, so the URL has to be checked.
- Searching a contract address on X, Latest tab, often returns many near identical bot posts with a multiplier ("called at 11K, now 14x") and a Telegram call channel link.
- Those channels give no reason for the call and only show multiples. A bot scans every new coin and posts only the calls that already did well, so the track record is manufactured.
- A friendly stranger sharing alpha on a coin on a chain the trader does not normally use, after days of rapport, is setting up a honeypot. After the buy the trader cannot sell and the chats are deleted.

## Narrative and visibility

- A coin that shoots up at launch and never returns to the start level is either real demand or a team buying supply upward. Team control is not inherently bad.
- Creator videos calling a coin undervalued are content aimed at newcomers, and narrative spin can become self fulfilling.
- Screener rankings blend age, volume and market cap, and yellow lightning bolts mark paid boosts, so visibility can be bought.
- Good traders weigh many variables: bundling percent, dev wallet, narrative, liquidity, market conditions, holder count and chart structure. The outcome is a buy sized by conviction, a pass, or an exit as information changes.

## In the trader's own trades

- Losses within seconds or minutes of entry on very young coins.
  - Where it shows: getTrades result and dates, with token age at entry and bonding stage at entry stored but not yet surfaced. Entry mcap in getTrades also shows how early the entry was.
  - Question: what did the top holder share and bundling look like before the buy?
- Buying low market cap coins that went up in a straight line on thin volume.
  - Where it shows: getTrades entry mcap against getTokenDetail for the symbol. The journal notes may mention smooth charts.
  - Question: what were volume and the holder list at entry, and was lack of pullbacks read as strength?
- Rug like exits, where price went to near zero.
  - Where it shows: getTrades PnL and result with exit mcap near zero, and rug signal names in getTokenDetail for the creator.
  - Question: were LP lock, mint and freeze authority checked, especially for a coin not launched on a main launchpad?
- Oversized or illiquid entries.
  - Where it shows: getTrades size against liquidity at entry (stored, not surfaced), and "Nx size" or oversized reads in getJournalEntries.
  - Question: how much slippage was accepted, and was size matched to pool depth?
- Buys that came from a call channel, a DM tip or a link in a comment.
  - Where it shows: journal notes and trade tags in getJournalEntries.
  - Question: who told the trader, and was the contract address verified through more than one channel?
- Buying a coin they later could not sell.
  - Where it shows: journal notes, and a trade still open long after the coin died.
  - Question: how did it reach the trader, and what was checked first?
- Entries near graduation or on boosted rankings.
  - Where it shows: getTokenLifecycle for stage and percent, and journal notes.
  - Question: what was the curve percent, and who paid for the visibility?
- Playbook rules that exist but are not followed.
  - Where it shows: getPlaybooks for rules like top holder under 3.5% or volume above market cap, and rules followed and broken in getJournalEntries, especially on losing trades.
  - Question: is the safety check in the playbook at all, and was it broken on the losers?

## Judgment calls

- The numbers are rules of thumb, not tested statistics. Josh confirmed the 3.5% top holder line, the 5% dev line, the 80% volume floor, the 0.5 SOL fee figure and the funding and fresh wallet rules as current in October 2026.
- The top holder rule and the bundle rules can disagree. A coin can pass 3.5% because supply is split across many wallets, while funding origin or the bubble map shows one controller. A pass on one check does not clear the others.
- Volume above market cap is common on any heavily traded new pair, so it is weak as proof of health. A fail is a much stronger signal than a pass.
- Bubble maps and explorer tracing are slow on fast tokens, so the quick checks come first.
- Coin type changes the picture. Coins launched on a main launchpad have LP and authorities handled, so effort goes to bundles. Coins launched elsewhere need the authority checks first.
- Team control is not inherently bad. A clustered holder can be a market maker or a team holding supply for good reasons, so the signal is behaviour such as selling, not clustering alone.
- When the checks M8 cannot run are the ones that matter, the honest answer is to name what the trader has to look at themselves: single top holder and dev share, bubble map, fresh wallets, funding origin, fees paid, candles, and social data.