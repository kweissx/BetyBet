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

# Session 3 (2026-10-01)
- Added a franchise evaluation checklist and a "no debt / emergency fund first" rule to
  `docs/extra-income-plan.md`. Still waiting on the interview answers and the franchise details.
- The franchise is **Almalibre Açaí vending machine** (Spain, 24,900 € + VAT). Reviewed: not
  recommended now. Full analysis in `docs/extra-income-plan.md`. Interview answers still pending.
- Almalibre (Leo, Responsable de Franquicias, WhatsApp) asks for name, DNI/NIE, email and address
  to send an NDA before sharing detailed numbers. Advice: signing an NDA is normal and doesn't commit
  to buying; read it first. Questions to send afterwards: `docs/almalibre-preguntas.md`.
- The user **has a NIE and a Spanish bank account** (worked in Spain 2019–2020, then moved back to
  Mexico). This helps with the Almalibre NDA and with matched betting in Spain (Betfair needs a NIE).
- Leo refuses to answer any question before the NDA. Advice: OK to give data and sign the NDA if the
  user wants (it doesn't commit to buying), but send the NDA to Claude to review first, and pay no
  deposit. Overall verdict on the franchise is still "not now".

# 2026-10-05: Almalibre NDA review (pages 1–5 seen, page 6 missing)
- No payment, no exclusivity, no non-compete, no commitment to buy (cl. 1.3–1.5). Spanish law, Valencia courts.
- Problems: penalty of **10,000 € per breach** without proving damage (cl. 8); very broad definition
  incl. the user's own notes/analysis (2.2 n); **no clause allowing disclosure to advisors** (3c), so
  sharing their numbers with Claude, a lawyer or an accountant could count as a breach; 5-year term;
  date written as 10/02/2026; address filled in as Barcelona (user now lives in Mexico).
- Advice: given 30,000 € > 20,000 USD budget and the "not now" verdict, signing a 10,000 € penalty to
  evaluate an unaffordable franchise isn't worth it. If the user continues anyway: ask for an advisors
  clause, a lower penalty limited to intentional breach, a corrected date, then sign.
