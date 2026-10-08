# 0014 - M8 model routing and prompt caching

Status: decided
Date: 2026-10-08
Replaces the "Default models" list in architecture.md.

Provisional: the routing, models and providers are chosen during the build against the eval set, written text is tested against live AI, and AI by plan is decided with the plan numbers ([0017](0017-launch-scope.md)).

## Question

How does M8 stay cheap enough for a $20 plan without getting worse?

## Options considered

- One frontier model for everything.
- A cascade of models picked per message, with prompt caching and batching.

## Decision

The cheapest thing that's still right handles each message.

| Tier | Handles | Model | Rough cost per turn |
|---|---|---|---|
| 0. Templates | Rule alerts, tilt check-in, loss limit, trial reminders, coin facts | No model; code templates written in all 3 voices | $0 |
| 1. Light | Intent triage, extraction (tags from replies), memory, naming and summarising conversations, short replies | Haiku 5.5 (`claude-haiku-5-5`, $0.10 / $0.50 per MTok up to 100K tokens) | ~$0.0015 |
| 2. Default | Nudges, journaling, normal chat | Sonnet 5.5 (`claude-sonnet-5-5`, $2 / $10 per MTok), effort `low` | ~$0.012 |
| 3. Deep | Sunday recap, deep pattern questions, questions that need several tools | Opus 5.5 (`claude-opus-5-5`, $4 / $20 per MTok), adaptive thinking | ~$0.05-0.10 |

Cost per turn assumes a ~10K-token prompt that is 75% cached and ~600 output tokens.

**Routing**
- Haiku triages every free-text message as light, default or deep.
- Anything near the harm line always goes to Sonnet or above, never Haiku.
- A conversation stays on one model unless it escalates, because caches are model-scoped.
- Before building the cascade, the Phase 0 spike runs the doctrine evals on Sonnet `low` and on Haiku, and measures cost and quality.

**Caching layout** (most stable first; a change only invalidates what comes after it)

```
[tools] [doctrine] [voice preset]                     shared by every user (3 variants), 1h TTL
[user profile + rules + memory]                       per user, 1h TTL
[conversation summary + recent turns + tool results]  automatic caching at the end
```

- 1h TTL because nudge replies land 5-60 minutes after the nudge, the range where it pays off (write 2x, read 0.1x).
- No timestamps, names or dates in the shared prefix. The current date goes in as a mid-conversation system message, which keeps the cache.
- Caches are per Anthropic workspace, so AI Gateway pins Anthropic direct with no Bedrock or Vertex fallback.
- Cache hits are checked in logs with `usage.cache_read_input_tokens`.

**Batch API (50% off)**
- Sunday recaps, nightly memory extraction, conversation summaries, and morning briefs started an hour early with fresh market data.

**Daily chat cap**
- The cap measures cost, not messages. The "M8 today" meter already shows a percentage, so a Haiku turn uses much less of it than a Sonnet turn.

## Why

- Most of M8's traffic is short and formulaic; a frontier model on every message would make heavy users unprofitable (50 Sonnet turns a day is ~$18 a month).
- Templates for alerts and coin facts are also safer: the doctrine can't drift there.
- Caching the large, stable prefix cuts most of the input cost.

## Consequences

- Rough AI cost: ~$2-4 a month for a typical active trader, ~$6-8 for a heavy one, against $16.67-20 revenue. The spike measures the real numbers.
- Every template needs a version in each voice, reviewed with the doctrine.
- The eval set runs per tier, so a routing change is tested like a prompt change.
