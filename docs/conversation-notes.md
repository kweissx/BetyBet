# Conversation notes (session 1: 2026-10-01)

A summary of the first chat, so any future chat can continue from here.
Original session: https://claude.ai/code/session_0182tg54wodazSoc7kCyRcM5

## About the user
- Lives about 8 months a year in Mexico City and the rest in Spain, for work. **Tax residency: Mexico.**
- Money is tight, and the user may lose their job soon. They want extra income from several sources,
  with no rush.
- Has never bet. Doesn't follow any sport. Finds betting boring and sees it only as a possible extra income.
- Test budget: **2,000 MXN** they can afford to lose. Has no bookmaker accounts yet.
- Has 15–30 minutes a day.
- Has committed to following the advice, and to getting help if betting ever starts to feel like a need.
- Was motivated by friends who say they make money betting (likely survivorship bias).

## What was decided
1. No "secure bets" exist. Netting €50 a day on €100 staked isn't realistic. Professional bettors
   aim for 2–5% of the total amount staked.
2. **Phase 1, paper trading (from 2026-10-01):** a routine named "BetyBet daily picks"
   (trigger `trig_01PYocrMAzYGQHe6SR4mt7Ps`) runs Monday–Friday at 16:54 Mexico City time. It follows
   `.claude/skills/daily-picks/SKILL.md`, logs to `ledger/ledger.csv` and writes `picks/YYYY-MM-DD.md`.
   It runs on branch `claude/zealous-fermat-m3km7k`.
3. Graduation review after **150 settled picks**: real money (1,000 MXN, 25 MXN per bet) only if the
   average CLV is above +1%. Stop if the CLV is 0% or lower.
4. **Matched betting** (`docs/matched-betting.md`) is the low-risk track. It works best in Spain
   (Betfair Exchange, needs a NIE, and accounts must be verified for about 1 month before promos).
5. The user wants an **extra-income plan** and an **evaluation of a franchise** they saw. Started in
   session 2. See `docs/extra-income-plan.md`.
6. **GBM investing** (session 3, 2026-10-01): the user wants help growing their GBM account. Plan and
   current market context in `docs/investing-plan.md`. Waiting for balance, holdings and expenses.
