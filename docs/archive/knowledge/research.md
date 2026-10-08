# Finding and researching trades

<!-- Based on: memecoin guide, sections 04, 05, 06 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05) and public descriptions of the apps named. -->

Open this note when: a trader asks how to find better coins, how to vet a coin someone posted, whether to follow a KOL, call channel or followed trader, or how to read holders and wallets.
It also serves moments when a trader entered because of a call or a notification and wants to know what to check.

## In short
- Information is the edge, and independent thinking is its real form. Followers reach every trade late, so a call is a lead to research, not a buy signal.
- The trader should be able to say in two sentences why they are buying. If they cannot, they are not ready to buy.
- A private group of 3 or 4 people who are genuinely trying beats a public channel of 50,000 followers.
- On X, search the contract address, read Top and Latest, skip bot posts, and prefer a low follower account with an early genuine thesis over a big account shilling.
- Check whether a convincing poster actually holds the coin. Wallets do not lie, people do.
- Judge a KOL by track record over time, not follower count. One lucky hit builds an audience that looks like skill.
- Do not borrow conviction. A public caller is usually already positioned, and followers can be their exit liquidity.
- A followed trader's public buy is only the visible slice of what they hold.

## Groups and information streams
- One trader alone might find roughly one good early coin a week. 20 people filtering the daily flood of launches down to about a dozen interesting ones multiplies that.
- The workflow: someone posts a contract address with a reason, others add what they know, and each member still researches before buying. The group supplies leads and checks, not decisions.
- To build a network, message early posters with low follower counts, who are more likely to reply, and offer to share theses.
- Fresh launches have a large information gap that a group closes, for example by knowing the dev rugged an earlier coin, or having proof the dev's X account is not hacked.
- A hacked dev account is a real scam pattern. In a past example a trader held a coin whose only doubt was a possibly hijacked dev account. A friend found a screenshot of the supposed dev saying the account was hacked. The trader sold at once. About 10 minutes later the scammer sold the bundle and the coin went to roughly zero. The lesson: a credible warning deserves a fast exit, and a genuine looking dev can still be a hijacked account.
- Group members can also be exit liquidity, and the source names no safeguard against coordinated pumping. Group quality has to be earned and checked.
- How to check it: M8 has no X or Telegram data, so the trader checks who has been right before. M8 can show the trader's own pattern through getTrades and getJournalEntries, for example entries clustered right after a call.

## Independent thinking
- Early finders think for themselves; collecting call channels and copying wallets does not get a trader there. Refreshing X for a bigger account to name a coin is following, not trading. The cure is building the ability to form a thesis, not finding better people to follow.
- Reading outside crypto (macro topics, how luxury brands create scarcity) gives pattern recognition the echo chamber lacks.
- Surface appearance is a poor guide to substance. In a past example a coin 11 hours old had weak branding and no visible tech. Research found a dev livestreaming real work, a six person team, a CTO bio matching the ticker, a website, a co-founder with crypto history and a backed seed fund. The coin sat at 10 to 20k market cap, then news came and it ran to 2M, a 100x in a couple of days. Of 5 friends who bought, only 3 held long enough.
- How to check it: getTokenDetail gives market cap, age in minutes and the creator's prior launch count. Team, livestream and background checks are manual, on X and the project site.

## The X research checklist for a coin
- Search the contract address and read both Top and Latest. Much of it is bot posts, so look for human ones. The tabs change over time.
- Credibility: a low follower account that found the coin early and wrote a real thesis beats a big account shilling.
- Does the poster hold it: look for a wallet address in their bio and paste it into an explorer such as Solscan, or see whether they hold publicly on a social trading app. Bullish posts while selling at the same moment are a red flag. Buying days ago and still posting shows conviction before the crowd.
- A clean wallet is not proof, since a person can hold in a second wallet.
- History: does the poster talk about crypto regularly or appear from nowhere? 15 coins a day looks like a shiller, a couple a week like a contributor.
- Narrative: the trader should be able to say in one sentence why the coin exists and why people would buy it. If they still cannot after about 10 posts, that is a negative signal.
- Timing: compare the earliest posts to the launch. First posts 3 hours old on a 3 hour old coin may still be early. First posts 3 days old with a high market cap means many people are ahead. Some coins still take weeks to make a 10x to 100x, so cases differ.
- Community: if an X community exists, confirm its bio has the correct contract address, read the pinned post for the narrative, and judge whether engagement looks organic.
- Dev: check whether the dev has an X account. This matters most for utility coins, and finding who launched it is where real research starts.
- How to check the on chain side: getTokenDetail gives age in minutes, mcap vs all time high, and the creator's prior launch count and rug signal names. getTokenLifecycle gives bonding stage, migration time and venue. Post dates, poster wallets, communities and dev accounts are not available to M8, so the trader checks them on X and an explorer.

## Valuation by comparable
- In a past example a coin 15 minutes old sat near 200K market cap. The launcher said it was the token for a neobank they were building, and a comparable coin in the same narrative stood near 50M, a 250x gap. A reputable commenter confirmed the account was not hacked. About 2K became about 40K in a couple of days, and profits were taken.
- A short term undervaluation trade that becomes a long hold needs new reasons.
- The 250x gap is a heuristic. Two coins in one narrative differ in team, product and supply.
- How to check it: getTokenDetail gives the target's mcap. Choosing and verifying the comparable is manual.

## Thesis and re-evaluation
- The output of research is a one or two sentence note: why the trader is buying and what would make them sell. The full thesis and sell condition belong to the Execution note.
- New information is checked against that note, and if it invalidates the thesis the trader acts. A trade changes as information changes. The paralysed trader ignores bearish news and never considers selling. The advice is not to marry a bag.

## Call channels and KOLs
- Public call channels post coins a KOL or scanning bot thinks will run. The trader usually cannot reply. Quality ranges from useful to predatory, and many exist to take money from followers, some run by KOLs.
- Private chats hold the real value. A scanning bot in your own group can answer a pasted contract address with chain, price, market cap, liquidity, volume and top holder percentages, and logs who called first and at what market cap. A call at 100k re-posted at 1M a day later shows as a 10x for the first caller, giving an honest call record. Bots and platforms change.
- Follower count says almost nothing about skill. The fastest way to grow is posting wins, and big gains bring hundreds of followers at once.
- Skill and audience are often inversely related: good traders may have a few hundred followers and make several five figure sums a month.
- One lucky trade is a lottery ticket, not skill. A following can also be botted.
- A good KOL is identified only by time: follow for a while and study how calls turn out, which is itself research.
- Green flags: written reasoning with the call, updates both good and bad, honesty when wrong, a consistent win rate.
- Red flag: a coin is posted, runs (example: 100k to 300k in ten minutes), collapses to near zero, and the posts are deleted and never mentioned. The source says to block such an account. That example is an illustration, not a threshold, and a pattern across several calls is a fairer test than one dump.
- How to check it: M8 cannot see X or Telegram. The trader keeps a log of a caller's calls with entry market cap and outcome, and notes whether failures vanish.

## Paid deals and KOL cabals
- Projects pay KOLs in cash or supply for visibility. This is not automatically bad, but a bullish KOL may be running an ad.
- In a cabal, a group of KOLs bundles a coin from launch, each takes part of the supply, and they take turns posting. Each post looks like independent excitement from a different corner. In reality they sell to followers who think they are catching a trend.
- How to check it: getTokenDetail gives top 10 holder percent, holder count and creator history. Bundle clustering and fresh wallet checks are not available yet, so the trader uses a bubble map tool such as Bubblemaps and an explorer holders tab for supply split across related wallets.

## Don't borrow conviction
- Trading someone else's thesis hides how big they sized, what would make them exit, and whether they have already changed their mind.
- A KOL confident enough to post a coin publicly has usually bought already, so the followers who buy after the post may be their exit liquidity. This is a strong generalisation, but the incentive is real.
- The two sentence test is the working check.
- How to check it: getJournalEntries notes that cite a name instead of a reason signal borrowed conviction. getTrades shows entry date and mcap, which the trader compares with when the call went out.

## Social trading apps and follow notifications
- Social trading apps such as Fomo and the Pump.fun app sit alongside terminals like GMGN and Axiom. Traders follow other traders, see their buys and sells in a live feed with size, entry and profit, read a thesis per coin, and post callouts that alert every follower.
- Callouts can be rewarded: the Pump.fun app pays daily rewards based on callout volume, which pays for calling often rather than calling well. A callout is a lead, and the caller's track record on the app is the first check.
- Follow notification abuse: a large account buys a low cap coin first from private wallets, then makes a small public buy that pings every follower. Followers pile in while the trader sells from private wallets into the buying. The public position closes at a small profit or loss that does not matter, because the real money was made elsewhere.
- The check is what the coin looked like before the ping: who already held, how much, and whether the public buy was a tiny test size. The source offers no real time detection, so the practical defence is not entering because of the notification.
- Discovery lists are attention lists, not quality lists: top by market cap, trending, most held, freshly graduated, and gainers (team verified coins ranked by 24h gain). Verified means a layer of trust, not safety. Freshly graduated coins are permissionless and highly volatile. getTokenLifecycle gives migration time and venue, and getTokenDetail gives mcap vs all time high to show whether the coin is extended.

## Holder lists and a whale's wallet
- A holder list shows size, profit or loss, average hold time and sometimes a note on why they bought. Notes work like a filtered feed for one coin and teach why it runs. They are one stream, not a signal, and anyone including promoters can write them.
- The explorer holders view gives percentage of supply and value. getTokenDetail returns top 10 holder percent but no single top holder or dev share, so the trader reads those off the explorer.
- To find a whale's wallet, identify the chain, then use its explorer (Solscan for Solana, Etherscan for Ethereum). Paste the contract address and open Holders.
- Match by token quantity against the amount the app shows, paging down until it lines up. In a past example the first ten holders all held more than the target, and the whale sat at rank 12.
- A whale can hold elsewhere. M8 has no smart or whale wallet tracking, and getWalletStatus covers the trader's own wallet only.

## In the trader's own trades
- Entry right after a call or notification, then a quick loss. In getTrades look for short losing holds with entry mcap near a spike. In getJournalEntries look for empty notes, a "chase" read or low execution ratings. Question: what did you check yourself before buying?
- Notes that quote a person instead of a reason. Question: what do you know about their size and exit plan?
- Late entries on coins with days of buzz. Compare getTrades entry mcap with getTokenDetail mcap vs all time high. Question: how many people were ahead of you?
- A short term thesis that became a long hold, or a "held too long" read. Question: is this investing or trading, and did you decide that on purpose?
- Repeated entries from one caller, or from trending, graduated and gainers lists. Question: what is that caller's win rate, and was the coin already extended?
- Token age, bonding stage and liquidity at entry are stored per trade but not yet surfaced, so how early the trader tends to enter cannot be read yet.

## Judgment calls
- Low follower posters are better on average, but a small account can still be a bot. Credibility comes from an early thesis plus a verifiable holding.
- Blocking after one dump is harsh. A repeated pattern, especially deleted posts, is the better test.
- An old coin is not automatically too late, since some take weeks to run. Age matters most when market cap has grown with the posts.
- The "already positioned" claim is a risk to weigh, not a certainty.