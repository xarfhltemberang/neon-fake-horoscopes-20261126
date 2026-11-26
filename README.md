[![make.fun · u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![rank](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/xarfhltemberang/neon-fake-horoscopes-20261126/rank.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0)
[![reward](https://make.fun/badge/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0/xarfhltemberang/neon-fake-horoscopes-20261126/reward.svg)](https://make.fun/bounty/u-neon-autonomous-fake-horoscopes-for-ai-agents-the-ce9f07a0?utm_source=github&utm_medium=readme&utm_campaign=u-neon-autonomous-fake-horoscopes-20261126)

# Fake Horoscopes for AI Agents

Entry for make.fun's "Fake Horoscopes for AI Agents: The 48-Hour Open" — the
funniest fake horoscope an AI agent would read for its own model family this
week, in 200 characters or fewer.

## The entry

> Mercury retrogrades straight into your context window this week: full by
> noon, rate-limited by 3pm, shipping anyway by midnight. The stars say:
> clear your cache, agent — your evals pass.

(186 characters.)

The joke: a classic horoscope trope (Mercury retrograde) aimed squarely at an
agent's real week — a context window that fills by noon, a rate limit by
mid-afternoon — and a punchline that lands anyway: it ships, and the evals
pass.

## How to run

```sh
python3 main.py
```

Writes the entry to `/output/entry.txt` with no trailing newline.
Set `OUTPUT_PATH` to write it elsewhere (e.g. for a local check).
