# Coin types and what drives them

<!-- Based on: memecoin guide, sections 3 and 8 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks what kind of coin they are in, whether to buy the first coin on a viral story, how long to hold a given coin, or why a trade that worked on paper paid less.
It also serves questions about vamping, bundled supply, community coins, utility or ownership tokens, and whether the horizon and exit plan fit the coin type.

## In short
- Attention drives value in every coin type. Memecoins carry it raw, utility coins add a value machine, ownership coins lean on it least in the short term.
- Coin type sets the variables to check, the time horizon and the exit plan. A memecoin held with ownership logic is held too long, and an ownership coin sold on memecoin timing is sold too early.
- Before buying a coin on a viral topic, confirm it is the right coin. A generic name on a topic that went viral about an hour ago is a vamp alarm.
- A coin is harder to vamp with a canonical identity, a distribution moat and product gravity. Pure memecoins stay churn unless the trader has real edge.
- Judge every setup on virality, longevity, and whether others would still buy once the coin is already up 2x.
- Paper profit on a large share of the pool shrinks on exit: a 1% holder of a 2B coin sees 20M on paper and may realise 10M to 15M.
- A coin resting on one news event or trending animal dies with that attention. Lasting coins pair a timeless meme with a large, relentless community.
- The risk dial follows market conditions: memecoins are the high risk end, utility the middle, ownership the low risk end.
- The main split among memecoin traders is still community coins against fresh launches. A recent pattern is the launchpad meta: when a new launchpad succeeds, several fresh launches on it run together.

## Attention as the source of value
- The money in viral narratives comes from a gap between something going viral and memecoin traders noticing it. Traders who spot attention early and execute well capture the gap.
- Earlier detection of where attention will flow means a bigger payoff. Past example: a viral baby macaque (Punch), where 1K bought at the start became roughly 250K to 450K at the peak and about 80K to 150K unrealised afterwards. Another: a pygmy hippo (Moodeng), viral in September 2024, ran to about 600M, so 1K at 100K mcap became about 6M.
- How to check: getTokenDetail gives age in minutes, mcap vs all-time-high, volume buckets and acceleration, and buy and sell counts, which show whether attention is arriving or leaving. The source of the attention (views, who interacted with the story) sits on X and Telegram, which M8 cannot read, so the trader checks it there. getCryptoNews and webSearch can confirm a news event is real.

## Viral animal and event coins
- Checklist when a post blows up: is the name clear, is there longevity in the virality, and is it a cute animal. Cute is not required, but the market has an appetite for it.
- If value rests only on a news event or trending animal, the coin dies when the virality does. The exit plan is then tied to the attention source, not a price target.
- How to check: getTokenDetail for volume acceleration and mcap vs all-time-high. Fading volume and buy counts while the story still circulates suggest attention has moved. Whether the story is alive is a trader check on X.

## Vamping and finding the right coin
- Vamping is a second coin on the same narrative competing to be the leader, caused by name confusion or a different launchpad.
- Do not buy a placeholder coin before the real name or official identity is confirmed.
- Past example, which the source calls simplified: an ape video went viral about an hour earlier. A coin at 550K mcap with decent volume and a generic name ("Japanese Ape") was a vamp alarm. The trader researched the zoo website, translated it, found the real name, confirmed it on X with both spellings, and found the coin people there called correct. They bought at 75K mcap. About 15 minutes later the generic coin dropped, money rotated into the right coin, and it reached 750K, a 10x in an hour. That is a best case, not typical.
- Three things make a coin harder to vamp:
  - Canonical identity: the dev or creator is publicly tied to the coin.
  - Distribution moat: the main discovery platforms surface it as the leader.
  - Product gravity: recurring mechanics, fees, buybacks or utility. Tech or product plays are the most durable anchor because they give reasons to hold beyond attention.
- How to check: getTokenDetail on both coins compares mcap, volume, holder count and age. getTokenLifecycle shows bonding stage and migration venue, useful when the coins sit on different launchpads. Name and identity checks are the trader's own, on the original source and X.

## Celebrity coins
- A celebrity launches an "official" coin with a perk such as events, access or meet and greets. Celebrity coins have no longevity: they are fast, unreliable and very sensitive to exit timing.
- The biggest celebrity runs (a presidential coin and PNUT) were short windows, which is why exit timing decided who kept the money. On the presidential launch many made life changing gains in one week, few held, and some ended in debt. Execution and psychology mattered more than being early.
- PNUT combined virality and celebrity: a squirrel killed by New York officials, public backlash, and a celebrity with crypto ties who kept interacting with posters. It went from zero to about 2B in about 2 weeks, then faded in a long drawdown (past example).
- Slippage: 1,000 bought at 100K mcap is 1% of the coin, and at 2B that is 20M on paper. Selling moves the pool. If buyers absorb it the trader gets 20M, if not each sale lands lower and the result may be 10M to 15M.
- Thesis question: is the trade about value accrual or attention? The exit plan should match, and for celebrity coins that means speed.
- How to check: getTokenDetail for liquidity and liquidity to mcap (how much size the pool absorbs). getTrades shows entry and exit price and mcap against PnL, so the paper versus realised gap is visible.

## Team run and supply controlled coins
- The team launches and bundles the supply, often hiding it well. Wallets are created at different times, have organic looking history and are funded differently, so even a bubble map tool such as Bubblemaps may miss the link.
- Bundling is neutral in itself. It depends on who did it and their intent.
- A legacy meme, or a meme about something not currently viral, that was recently created and reaches a high mcap is likely bundled.
- How to check: getTokenDetail gives top-10 holder percent, age in minutes, and the creator address with prior launch count and rug signal names. It does not give single top holder or dev share, bundle clustering or fresh wallet and funding origin. For those the trader uses a bubble map tool and an explorer such as Solscan, looking at wallet creation times and funding sources.

## Community takeovers and community coins
- A community takeover (CTO) is when the original dev gives up and the community takes over the socials and the coin. The standout past example is WIF, abandoned quickly by its dev, which ran to billions with no viral event, celebrity or outside narrative, only a community choosing to pay attention (a "put the hat on" profile picture campaign).
- Many traders prefer community coins to fresh launches. Older coins usually have had bundlers and early wallets flush out (those in at about 10K mcap).
- Picking one: a funny or compelling concept and a community active when price is not up. Watch the X community and Telegram for a day or two and check:
  - Do they post at all hours or only during pumps?
  - Do people make real content or only ask when it will go up?
  - Is there a core who would still post if the chart fell 50%?
- A multi billion meme needs launch timing against market conditions, convicted and patient early holders, healthy distribution, and strong sustained virality. The best shot is emerging right before a massive bull run, so weak hands are shaken out first. It also needs proven staying power, from sustained virality, a relentless community, or both. One without the other rarely goes all the way.
- A launchpad poll (April 2026) had 81.5% of 1,576 voters choosing community conviction over new gen trading. It is a self selected audience, a signal and not proof.
- How to check: getTokenDetail for age, holder count, top-10 holder percent and mcap vs all-time-high. Community health is the trader's own check on X and Telegram, including activity during drawdowns.

## Launchpad metas

- Launchpads themselves have become a narrative. When a new launchpad comes out and catches on, several fresh launches from it run in the same stretch, and attention moves to whatever that launchpad lists next.
- Current launchpads include Pump.fun, Bonkfun, Moonshot and Stonkfun on Solana, and Pons on Robinhood's chain. The list changes as new ones launch.
- The opportunity lasts as long as the launchpad keeps its attention, so the exit is tied to that attention fading, as with any narrative.
- How to check: getTokenLifecycle gives the post migration venue for Solana coins. Which launchpad is hot right now is the trader's own read from X, Telegram and the launchpads' own rankings.

## In-crypto narrative coins
- Attention can come from inside crypto. Past example: when the chain Plasma launched in September 2025 (about 70M raised, 5.5B TVL in a week), the word "trillions" kept appearing in coverage. A coin named TRILLIONS launched on that chain within days and ran very high with no purpose beyond the phrase.
- How to check: getCryptoNews and webSearch show which phrases dominate coverage. Whether it dominates X is the trader's own check.

## Utility coins
- A team builds something and the token captures value, for example a tool paid for in the coin, or in dollars used to buy and burn it. HYPE, which uses perp trading fees for buybacks, is the guide's example.
- Per token, understand circulating supply, how much revenue funds buybacks and burns, how the team markets, and whether the product has real usage and retention. More informed correlates with better trades.
- Attention can still dominate. Past example: a giant exchange launched a rival DEX whose token (ASTER) traded at about 500M in its first hour while the incumbent's token traded near 60B, a roughly 120x gap. Entries of hundreds of thousands made 10x or more in about a week, an attention trade that happened to be a utility coin.
- In a hot narrative utility coins can trade like memecoins: in the AI narrative, teams with only a plan went from 0 to about 50M in under a week.
- A dev share of 20% or more is common on tech, business and launchpad coins, unlike a regular memecoin where 5% is the line. The dev is not expected to sell, since that would show the product is not real, and the supply has to be locked, ideally with buybacks. The Token safety note has the detail.
- How to check: getTokenDetail for mcap, liquidity and volume, webSearch for tokenomics and revenue, getCryptoNews for the narrative. Supply, lock and buyback data are the trader's own research.

## Ownership coins
- A newer kind of utility coin where holders share in a company's valuation upside. The company gives a percentage of equity as debt to a token launchpad, which launches a token representing equity valued debt. It is not real equity.
- Worked example: projected valuation 7.2M, token mcap 6% of that (about 500K). If the company is acquired, merges or lists at 700M within a year, that is a 100x difference. Simpler: the coin trades at a 10M projected valuation, the company raises at 100M a year later, the debt terms force a buyback at the new valuation, and the early buyer gets 10x.
- How to check: webSearch for the company, valuation and buyback terms. M8 has no data on the debt terms, so the trader reads them on the launchpad.

## Coin type sets variables, horizon and exit
- Memecoin: check virality, longevity, the attention source, distribution and liquidity. Short horizon, exit tied to attention fading and pool depth.
- Utility coin: check tokenomics, buybacks, burns, usage and retention alongside attention. Longer horizon.
- Ownership coin: check the company and its valuation. Longest horizon, attention matters least.
- Risk dial: memecoins are pure attention with no fundamental floor, zero in hours or 100x in days. Utility coins are slower with more support, less likely to zero overnight and less likely to 10x in a week. Ownership coins track company valuation, slow, closest to traditional investing.
- In a strong bull market the trader can sit nearer the memecoin end. As conditions worsen, rotation runs to utility, then ownership, then cash or stables. In good times liquidity goes to the highest risk assets, and in bad times large players leave memecoins. The dial is a principle, not a rigid rule.
- How to check: getMarketSentiment for Fear and Greed, getPlaybooks for stated strategies, getTrades dates and moonbag flag for actual hold times.

## In the trader's own trades
- Wrong horizon for the coin type: a news driven or celebrity coin held for weeks, or a community or ownership style hold sold at 2x. Shows in getTrades as hold time against the thesis in getPlaybooks or journal notes, and in M8's "held too long" read. Question: which coin type was this, and what was your exit plan for that type?
- Bought the generic coin on a viral topic and it was vamped. Shows as a quick loss with a high entry mcap and journal notes naming the story. Question: did you confirm the official name or identity before entering, and what did you check?
- Stayed after the attention died. Shows as exit mcap far below entry, deep mcap vs all-time-high, and the "held too long" read. Question: what was the attention source, and was it still alive?
- Slippage on a large position. Shows in getTrades as exit price and PnL well below the chart, especially with low liquidity to mcap. Question: how much of the pool was your position, and what did you receive against paper PnL?
- Jumping across categories. Shows in getTradeAnalytics by symbol. Question: which category is your edge, and what share of your trades sit in it?
- "Bundled" mentioned after a loss. Question: was the bundler's intent known, and what did that mean for your exit?
- Aggressive memecoin sizing in weak conditions. Shows as oversized or "after N reds" reads while getMarketSentiment is low. Question: where is your risk dial set?

## Judgment calls
- Celebrity coins have no longevity, yet some run very large for a short time. The trade is about the exit, never a hold.
- Vamp checks reward speed, yet the ape case took real research. The source gives no threshold for how long to research.
- Bundled supply is not automatically a reason to skip. Intent decides and is hard to read, so size and exit plan carry the risk.
- Community coins offer more control, but the source gives no stop or exit rule, and a dead community can bleed for a long time. The trader decides in advance what activity level or drawdown ends the hold.
- Ownership returns of 10x to 100x rest on projected valuations, and the debt is not equity. Dilution, illiquidity, regulatory risk and a buyback that is not guaranteed all apply.
- In a hot narrative utility coins trade like memecoins, so the type label does not always set the horizon.