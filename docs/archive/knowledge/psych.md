# Trading psychology

<!-- Based on: memecoin guide, sections 1, 10, 11 (docs/m8/knowledge/sections/), with Josh's review (docs/m8/knowledge/review.md, 2026-10-05). -->

Open this note when: a trader asks why they keep repeating a mistake they already understand, how to respond to a big loss or a missed runner, why they roundtrip winners or hold dead positions, how to size or behave after a win, or whether trading is taking over their life.
It also serves goal questions such as what the money is for, and style questions such as whether the trader is forcing a way of trading that does not suit them.

## In short

- Knowing a lesson is not the same as having learned it. Awareness only shortens the mistake, and most lessons still cost real money.
- Set the sell plan before entry, take profits gradually while making money, and take real profits when the gain is life changing for this trader. A target that moves up as price approaches is greed.
- After a significant loss: stop, name the exact failure, write one specific rule against it, detach. The aim is to make money, not to make the money back.
- After a bad run there are two wrong reactions: sizing up to win it back, or turning so conservative that valid setups are skipped.
- A missed runner damages the next several trades. Size down and return to the playbook.
- Review misses as well as losses, to understand the pattern and not to punish. The same kind of miss twenty times without a question means the pattern never breaks.
- Size as a percentage of the portfolio, as a larger account would. About 20% of a portfolio in one memecoin is the guide's example of too much.
- Asymmetry only works when the downside is survivable. Decide what the money is for before it arrives, and keep a financial floor that has nothing to do with the screen.

## Knowing a lesson versus living it

- Reading a rule does not install it. A trader can know every item here and still roundtrip, revenge trade or miss an exit when greed or fear is active.
- The guide's author, after years of experience, followed good traders who all gave the same profit taking advice, and still broke it and gave back a large gain.
- Why it holds: the rule is learned in calm conditions and the failure happens in hot ones. Awareness buys a moment of recognition that lets the trader fix the mistake faster and lose less.
- How to check: a playbook rule such as "take profit at X" marked as broken (getPlaybooks, getJournalEntries rules followed and broken) shows the gap. Ask what happened at the moment the rule applied.

## Greed and the moving sell target

- The pattern: the trader sets a sell level, price nears it, the level moves higher. Repeated, this rides a large gain all the way back down.
- The rule from the traders the guide followed: if the gain is life changing, take profits. If money is being made but not in life changing amounts, take profits gradually.
- "Life changing" is personal and "gradually" is undefined, so the trader should set their own amounts and levels and write them into a playbook.
- Why it holds: a target moved once is easier to move again, and a position closed in one piece, or never scaled out, banks nothing when the move reverses.
- How to check: getTrades gives realised result and entry and exit mcap, but there is no record of a position's peak unrealised gain, so a roundtrip is inferred from a big winner that ended small or red, or from journal notes like "will sell at X" followed by a lower exit. Ask what the sell plan was before entry, whether it moved, and how much of the win is banked.

## Scarcity thinking

- Many mistakes come from fear, specifically a scarcity mindset the trader often does not know they have. It comes from tight money growing up or a bad current situation, and runs silently under every decision.
- It shows up as:
  - holding winners too long, because this feels like the only shot;
  - selling too early, because the trader cannot believe they deserve the ride;
  - treating every trade as once in a lifetime, so oversizing and panic;
  - holding dead positions for months, because cutting admits the opportunity is gone.
- A position flat for two years is not a bad trade. It is a refusal to cut and redeploy capital somewhere that is moving.
- A big roundtrip is often greed on top of a belief that this is the one real shot.
- It worsens after a large loss: every trade feels like it had to work, every miss feels catastrophic, and oversizing and ignored red flags feel justified.
- The fix for the pressure is real, not a mindset trick: a financial floor unrelated to crypto (income, a safety net), even if that means pausing trading and working elsewhere for a while. When survival pressure lifts, the scarcity voice quiets.
- Habits:
  - Think in scenarios: several profit targets and risk levels before entering.
  - Size as a percentage of the portfolio, as if already large. Someone with a million would not put 20% on one memecoin, so the same trader should not with 10k. This means a smaller percentage, not a bigger dollar size.
  - Cut the moment the thesis breaks.
  - Count the opportunity cost of dead capital.
- Small accounts are the classic trap: balances under 0.5 SOL, chasing six figures, comparing with peers who are making it. The guide's recovery example (160 dollars to over 100k in just over a month) is a single reported outlier, not an expectation. The transferable part is the stop, the floor and trading only high conviction plays.
- How to check: getUserProfile for size band and self named leaks. getTrades for hold time on flat or red positions and size against the trader's usual. Total portfolio value and withdrawals are not available yet, so ask how much of total savings is in play and whether a total loss would hurt their life.

## The post loss protocol

- The sequence: stop, identify the precise failure, turn it into one specific rule, detach, restart.
- Candidate failures: oversizing, ignoring red flags, no exit plan, or letting the chart manage the trader instead of the thesis managing the position.
- "Be more careful" is meaningless. The rule must target the exact failure, such as a size cap or a written invalidation level.
- Why it holds: trying to make the money back and trying to make money are different mental states, and only the second decides well.
- Zoom out against the urgency: any week has many decent 10x narratives, crypto is unlikely to vanish this year, and the trader does not need to make money today, this week or this month.
- It bends: "opportunities are abundant" assumes an active market. In quiet or bearish conditions it can push overtrading, so pair it with conviction only entries.
- How to check: getJournalEntries after the loss day. Is there a named failure and a concrete rule, an empty note, or a vague lesson? Compare with getPlaybooks for a new rule.
- If trading is pushing the trader to a dark place, stepping away for a while is right.

## Revenge trading and the overconservative flip

- Revenge: wanting the money back asap leads to buying poor coins, noticing they are poor, and buying anyway because the chart pumps and a possible 10x cannot be missed. Revenge and scarcity feed each other.
- The opposite reaction is skipping trades that match the playbook, trading far less and smaller than normal, and never rebuilding. Neither reaction fixes the failure.
- How to check: getTradeAnalytics for streaks and drawdown, then getTrades for count and size in the days after against the trader's norm. M8's revenge read, the "after N reds" read and the loss streak signal catch the first. The second shows as count and size both well below normal with playbook setups untaken, and usually needs a direct question.

## The fumble spiral

- Missing a big winner, by selling early or skipping it, costs the next several trades. That is where the real damage happens.
- Symptoms: every coin looks like the next miss, so the trader chases, sizes bigger, buys late into a pump because FOMO beats the thesis, and holds too long because booking a small win feels unacceptable when a 10x is "needed".
- The trader is then trading feelings about the last miss, not the market.
- Every profitable trader has missed life changing trades, several times. Those who last accepted it, kept their process and stacked small wins until the right setup came.
- Big wins come when stable, rested and in rhythm after consistent smaller wins, not when desperate, oversized and at the charts at 4am. The feeling of missing out is a weak signal: the cycle does not end.
- The deeper cost is eroded confidence: worse decisions, more losses, less confidence.
- How to check: getTrades for a larger, later or higher mcap entry soon after the trader sold early or skipped a coin that ran. M8's chase and oversized reads help. Ask whether the entry matched the playbook or was about the coin missed yesterday.

## Accountability for misses

- Significant misses count as failures to examine: a trade clearly worth taking, a narrative seen forming, a coin found early and not bought, a target missed by holding too long.
- The purpose is understanding and prevention, not self punishment. Dismissing each with "there is always a next one" stops growth. Feel the frustration, let it sit, use it, move on.
- It bends: only setups the trader's own rules said to take are real misses. Otherwise review becomes hindsight regret and feeds the spiral.
- How to check: the journal rarely records misses unless written, so ask which misses this week were real and what they share.

## Trading the style that fits

- The fish wants steady gains: lower risk, smaller positions, regular profit taking, sleep, compounding. The monkey wants the moonshot: high variance, 100x or nothing, sits through huge drawdowns when convinced.
- Neither is wrong. The damage is a fish trading like a monkey or the reverse.
- Examples: a fish who misses a 100x and sizes up for the next one. A monkey who sells a 3x on a coin that runs to 50x and tries to force a discipline that does not suit them.
- Tactical adjustments for conditions are fine. Becoming a different trader out of frustration is what kills accounts. The best can do both and know when to switch, but few can.
- How to check: getTradeAnalytics (win rate, payoff, by symbol, hold times) shows the natural profile, getUserProfile the bands and leaks. A sudden shift in size or hold time after a frustrating stretch signals a style swap. Ask whether it was a fish trade or a monkey trade.

## After a win

- After a first serious win (the guide's example is 50K to 100K), many traders get more anxious, because there is now something to lose. It shows as holding too long to turn 100K into 500K, or adding risk to "secure gains".
- Other failure modes: arrogance toward non traders, telling everyone (which changes relationships), and status spending that creates a need to repeat the win.
- The plan: take the profits, pay the taxes, then execute the goal set beforehand.
- Diminishing returns: the guide's loose estimate is that one million changes a life enormously and two million barely more, so risking the first for the second is a bad trade. This is rhetoric, not data. The number should not be left to climb until it returns to zero.
- It bends: scaling up is fine when size stays a modest percentage of a larger portfolio under the playbook. The warning is size rising because of the win rather than the plan.
- How to check: getTrades for size rising after a large win, getJournalEntries for "Nx size" and oversized reads. Ask what the plan for this profit was.

## What the money is for

- Define making money before trading: quit a job, clear debt, buy a house, retire early, buy time, buy status. Vague goals produce vague behaviour.
- The guide's concrete goal for traders in their 20s and 30s is to remove or sharply cut a mortgage. Illustration: a 200K mortgage over 25 years at standard rates costs about 350K, roughly 150K or 6,000 a year in interest. Real rates and terms vary, so treat it as illustrative.
- A small mortgage frees the trader to take risks in career and life: money should buy freedom, not status. Secure the safety net before upgrades. Decide the purpose before the win, when emotions are calm.
- How to check: getGoals for targets and limits. If none, ask what the money is for and how far the account is. Social media makes the whole world the comparison class and pushes rushed, oversized bets, so ask what they are comparing against.

## Asymmetry and survivable sizing

- The case for the risk: sized sensibly, the downside is what was put in, while a right narrative can pay 10x, 50x or 100x. Sizing is the condition.
- M8 never fully backs a long shot, never tells a trader to take the risk, and never suggests that believing in a coin makes it run. Its one check is whether the trader could lose that money without changing how they trade tomorrow (confirmed by Josh, October 2026).
- The same shape applies to a business, a personal brand or a rare skill: repeated, structured, survivable bets that compound.
- This does not license dropping risk management or putting all savings into memecoins. Most memecoin traders lose money, so a long shot only fits money the trader can afford to lose.
- Persistence helps: another cycle, another hour of research. Optimism is not evidence that things will work out and does not justify more risk.
- Being here is not shameful, and asymmetric bets can be a rational response to a hard economy. But a trader who feels stuck can treat trading as a lottery ticket, and trading is not a substitute for fixing income or debt. The check is whether sizing is deliberate or desperate.
- How to check: ask how much of total savings is in play. In getTrades, look for many small speculative punts with no playbook behind them.

## Burnout and life outside the screen

- Constant chasing with no pause means sprinting past your own life. Work hard and rest, want more and appreciate now. Freedom bought means little if the trader was never present building it.
- How to check: getTrades timestamps for late sessions and long runs of trades, with ratings falling over the same period in getJournalEntries. Screen time is not available, so ask about hours at the screen, when they last stepped away, and what else is in their week.
- If trading is clearly hurting the person, suggest a break and a floor away from crypto. The sources say nothing on gambling addiction or losses beyond what a trader can afford, so serious cases need care and outside support.

## In the trader's own trades

- Size jumps after a loss: larger than usual soon after a large loss, or the biggest of the week. Reads: revenge, oversized, "Nx size", "after N reds". Ask: are you trying to make the money back, or to make money?
- Fast re-entry: the gap after a loss shrinks, or the trader is back in within minutes (chase). Ask: did this entry match your playbook, or is it about the coin you missed yesterday?
- Bigger or later entries after a missed runner, at a high mcap after a steep run. Ask: would you take this setup on a calm day?
- Dead capital: flat or red positions held far past the usual winning hold (held too long). Ask: has the thesis broken, and if so why are you still in? What does it cost while it sits?
- Roundtrips and moved targets: a big winner that ended small or red, or "will sell at X" followed by a lower exit. Ask: what was the target, why was it not banked, did it move?
- No scaling out: one piece in or out after a big gain. Ask: what was the sell plan before entry?
- Repeated early exits on coins that then ran. Ask: is this fear of giving back a win?
- Oversizing from scarcity: positions near the 20% example. Ask: would you size this way with a much bigger portfolio?
- Emotion tags (FOMO, revenge, fear, greed, desperation, frustration), execution ratings from 1 to 5 clustering low after losses, and broken rules clustered after a loss or a miss. Ask: what changed in the trades after the loss?
- Empty notes after a big loss, "need to make it back", "last chance", or vague lessons like "be more careful". Ask: what exactly went wrong, and what one rule would have prevented it?
- Overcorrection: count and size both far below normal after a drawdown while setups match the playbook. Ask: which valid setups did you skip, and why?
- Post win escalation: size rising after a big winner, holding past a target, a spree after a win. Ask: what was the plan for this profit?
- Late night and long sessions with falling ratings, alongside M8's loss streak, rule break and size anomaly signals. Ask: how many hours at the screen, and what is the balance pressure outside trading?
- Balance pressure: a small or shrinking balance with repeated top ups cannot be seen yet. Ask: if this account went to zero, what would change in your life?
- getUserProfile self named leaks and the trader's own monthly cost estimate can be set against the data. Ask: does this month match what you named?
- Journal notes on others' gains: ask what they are comparing against. Remind that profits carry a tax bill.

## Judgment calls

- Pushing harder versus protecting capital: after a drawdown, chasing recovery and retreating are both reactions to the loss. The better frame is a smaller percentage size, conviction only entries and one new rule.
- Fun and discipline work together. Traders often do better while they enjoy it and keep their rules than once they start overthinking every narrative and over analysing memecoin charts, which matters less now that attention drives these coins. Fun is not a replacement for rules: sizing still has to survive being wrong.
- "Zoom out, opportunities are abundant" calms revenge urgency but can push overtrading in quiet markets.
- "Size as a large account would" means a lower percentage, not more dollars. A small account reading it wrongly will oversize.
- Style: tactical changes for conditions are normal, a change of nature after frustration is the danger. A fish and a monkey may need different versions of one rule, such as a tighter loss cap or more partial sells.
- The 20% and twenty misses figures are illustrations, not rules, and "life changing" and "gradually" are personal.
- If trading hurts the person or outside pressure drives the decisions, a break and a floor beat any tactical fix. Understanding and one specific rule work better than shame.