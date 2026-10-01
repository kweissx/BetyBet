---
name: daily-picks
description: BetyBet daily paper-trading run. Grades yesterday's picks, then researches today's events and logs up to 4 value bets (singles only) with a fixed virtual stake. Use when asked for "today's picks", "daily picks", "run BetyBet", or when the 5pm weekday routine fires.
---

# BetyBet daily picks (paper trading)

The aim of this phase is to **measure** whether these picks beat the market, not to make money.
No real money is staked until the rules in "Graduation" are met. Be honest in every output: if
nothing has value today, log zero picks and say so. Zero picks is a valid, good result.

All times are **America/Mexico_City** unless the user says they're in Spain (then Europe/Madrid).
Currency is MXN. Virtual bankroll: **2,000 MXN**. One unit = **50 MXN** (2.5% of the bankroll).

## Step 1: Grade open picks (always do this first)

1. Open `ledger/ledger.csv` and find the rows with an empty `result`.
2. For each one, search the web for the final result and the **closing odds** (the last price before
   kickoff, from an odds-comparison site such as OddsPortal, or the same bookmaker if it's available).
3. Fill in the columns:
   - `result`: `W`, `L`, `P` (push/void) or `HW`/`HL` (half win/half loss on Asian lines).
     `SKIP` means the user's bookmaker (Caliente) offered less than the minimum odds, so it isn't counted
   - `pnl_mxn`: for W, `stake*(odds_taken-1)`. For L, `-stake`. For P, `0`. Halve it for HW/HL.
   - `closing_odds` and `clv_pct = (odds_taken / closing_odds - 1) * 100`
4. If the event hasn't finished or you can't confirm the result, leave it open and add a note.
   Never guess a result.

**If `picks/YYYY-MM-DD.md` already exists for today** (because of an earlier manual run), only do Step 1. Add
a "Later update" section to that file with the graded results and the stats output, and log no new picks.

**Data access:** odds-comparison and some sports sites (OddsPortal, ESPN, Betfred) are blocked by the network
proxy. Use WebSearch for results and odds, and say in the report that the prices are approximate. Record
each pick's **minimum acceptable odds** in `notes` (the price where the edge drops below 3%).

## Step 2: Find candidates

- Window: events that start between **18:00 today and 14:00 tomorrow** (CDMX time), so the user can place
  the bet after receiving the picks.
- Sports, in this order of preference: football (LaLiga, Premier League, Liga MX, Bundesliga, Serie A,
  Champions/Europa League), NBA, tennis (ATP/WTA main draw), MLB/NFL in season.
- Markets: match result (1X2), draw no bet, Asian handicap, totals (over/under), moneyline.
  **No parlays or accumulators, no player props, no live bets.**
- Odds range: **1.50 to 3.20**. Lower odds hide big losses. Higher odds produce too much noise for a
  small test.

## Step 3: Research each candidate (about 6–10 candidates)

For each candidate, write short notes on:
- confirmed or likely line-ups, injuries and suspensions
- recent form *with underlying numbers* (xG for football, net rating for NBA, serve/return stats for tennis)
- rest days, travel, fixture congestion, rotation risk (cup games, European weeks)
- motivation (title, relegation, dead rubber), and weather for outdoor sports

Then write **your own probability** for the selection **before** you look at the odds.

## Step 4: Compare with the market

1. Get the best available odds from bookmakers that are legal for the user: in Mexico, SEGOB-licensed
   books (Caliente, Codere, bet365, Betway, Strendus...). In Spain, DGOJ-licensed books.
   The user only has access to **Caliente** in Mexico (search works at caliente.mx without logging in). Mexican
   prices are often lower than European ones, so when a pick depends on a price that Caliente rarely matches
   (for example, European draws and underdogs), say so. Always give the minimum odds in **American format** too
   (e.g. 3.35 = +235, 1.90 = -111), because that's what the user sees.
2. Remove the bookmaker margin to get the fair market probability. For a market with outcomes i, the fair
   probability is `p_i = (1/odds_i) / sum(1/odds_j)`. Use a sharp reference (Pinnacle or exchange prices)
   when you can find one.
3. Edge = `my_prob * odds_taken - 1`.
4. **Only log a pick if the edge is at least 3%** and your probability is no more than 8 percentage
   points away from the fair market probability. A bigger gap almost always means you've missed
   information (an injury, a rotation, a line-up). Recheck it, or skip the pick.
5. Keep the **best 4 at most**, and no more than 2 from the same competition.

## Step 5: Log and report

1. Append one row per pick to `ledger/ledger.csv`. Stake is 50 MXN (1 unit). Leave `closing_odds`,
   `clv_pct`, `result` and `pnl_mxn` empty.
2. Write `picks/YYYY-MM-DD.md` with:
   - a table: event, kickoff (CDMX), market, selection, odds and book, my probability, fair probability,
     edge, stake
   - 2–3 lines of reasoning for each pick, including **the main way it loses**
   - the candidates you rejected, and why (one line each)
   - yesterday's graded results and the output of `python3 scripts/stats.py`
3. End with the reminder: *Paper trading: do not place real bets yet.*

## Graduation (from paper to real money)

Suggest real money (starting with **1,000 MXN, 1 unit = 25 MXN**) only when **all** of these are true:
- at least **150 settled picks**
- average CLV **above +1%** (this is the most reliable signal: it shows whether we beat the closing price)
- ROI is not below -5% (with 150 picks, ROI is still mostly luck. CLV matters more.)

If the average CLV is **0% or lower** after 150 picks, tell the user plainly that the model has no edge
and recommend stopping. Don't change the rules after the fact to make the numbers look better.

## Hard rules (also for real money later)

- Flat stakes. Never increase the stake after losses. Never "win it back".
- Never more than 4 picks a day, and never more than 10% of the bankroll at risk on one day.
- Stop for a week if the bankroll drops 25% from its peak. Stop completely if it reaches 50%.
- Only legal, licensed bookmakers. Never use money that's needed for living costs.
