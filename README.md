# BetyBet

A test of whether disciplined, research-based betting can bring in a small extra income, with **paper
trading (no real money) first**, measured honestly.

## The plan

| Phase | When | Money at risk | Goal |
|---|---|---|---|
| 1. Paper trading | Weeks 1–8 | 0 | Claude logs up to 4 picks each weekday at about 5pm (CDMX). We measure ROI and closing-line value (CLV) |
| 1b. Matched betting (optional, in parallel) | While you're in Spain | About €50–150, mostly recovered | Low-risk profit from bookmaker offers. See [docs/matched-betting.md](docs/matched-betting.md) |
| 2. Small real test | Only if Phase 1 passes the graduation rules | 1,000 MXN | Confirm the paper results with real bets |
| 3. Scale or stop | After about 150 real bets | Up to 2,000 MXN | Decide based on the numbers, not on feelings |

Realistic expectations: a *good* bettor makes 2–5% of the total amount staked. With 50 MXN stakes and
about 15 bets a week, that's around 15–40 MXN a week. **Betting at this size won't pay the bills.**
This project is about finding out whether there's an edge at all. If there isn't, we'll know cheaply.

## Files

- `.claude/skills/daily-picks/SKILL.md`: the daily process (grade results, research, compare with odds, log)
- `ledger/ledger.csv`: every pick ever made, graded honestly
- `picks/YYYY-MM-DD.md`: each day's picks with the reasoning
- `scripts/stats.py`: `python3 scripts/stats.py` prints hit rate, ROI, CLV and drawdown

## Rules that never change

1. No parlays. Flat stakes. Never chase losses.
2. Only legal, licensed bookmakers (SEGOB in Mexico, DGOJ in Spain).
3. Stop for a week at -25% from the peak. Stop for good at -50%.
4. If after 150 picks the average CLV is 0% or lower, the model has no edge and we stop.
