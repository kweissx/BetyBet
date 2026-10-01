# Matched betting: the low-risk track

Matched betting turns bookmaker promotions (free bets, refunds, boosted odds) into a mostly predictable
profit. You don't need to know anything about sports. It's maths and careful clicking.

## How it works (one example)

1. The bookmaker says: "Bet €10, get a €10 free bet".
2. **Qualifying bet:** you back Team A at the bookmaker for €10 at odds of 2.10.
3. At the same time you **lay** Team A (bet *against* it) on a betting exchange at odds of about 2.14.
   A matched-betting calculator tells you the exact lay stake.
4. Whatever happens, you lose about €0.30–0.50, and you now have the €10 free bet.
5. **Free bet:** repeat the process at higher odds (about 4–6). You keep roughly 70–80% of the free bet
   as real cash, so about €7–8 here.

Net result: roughly **+€7** with no dependence on who wins. Mistakes (a wrong stake, a lay bet that
didn't get matched, the wrong market) are the main risk. That's why you start with small offers.

## Where it works for you

| | Spain (while you're there) | Mexico |
|---|---|---|
| Exchange for laying | Betfair Exchange (betfair.es), legal, about 2% commission | Betfair's exchange status in Mexico is unclear. Check before relying on it |
| Promotions | Welcome bonuses have been restricted since 2020, and new accounts must be verified for about 1 month before getting promos. Ongoing free-bet offers still exist | Welcome bonuses are common (Caliente, Codere, bet365, Betway, Strendus...) |
| Requirement | DNI/NIE and a Spanish bank account | INE/RFC and a Mexican bank account |
| Verdict | **The best place to start**, if you have a NIE | Possible with "bookmaker vs bookmaker" coverage (dutching), but less efficient. Ask me to calculate each offer |

Rules in both countries change often. Confirm each offer's terms (minimum odds, expiry date, whether the
stake is returned) **before** placing the first bet.

## Getting started (Spain)

1. Open a Betfair.es account (it has both the sportsbook and the exchange) and complete DNI/NIE verification.
2. Open 2–3 other DGOJ-licensed bookmakers and verify them, so the 1-month waiting period runs in parallel.
3. Deposit only what the offers need (about €50–150 in total, spread across accounts).
4. For each offer, paste its terms into a chat with Claude: "calculate the back/lay stakes for this offer".
   Claude will give you the exact stakes and the expected profit. Double-check them in a free online
   matched-betting calculator.
5. Record every offer in `ledger/matched.csv` (Claude can create it for you).

## Look around corners

- **Taxes:** your tax residency is Mexico, so profit from either country is reportable there.
  Mexican bookmakers usually withhold tax on winnings, and Spain may tax gambling profit separately.
  Ask an accountant once profits become regular.
- **Gubbing:** bookmakers restrict accounts that only take offers. Placing occasional normal small bets
  helps, but expect it to happen. Matched betting brings in a **limited amount of money**
  (often a few hundred euros in total), not a permanent salary.
- **Never** use someone else's account or ID. It's fraud and the bookmaker will confiscate the balance.
- Keep the exchange balance high enough to cover your **lay liability** (this is the number people forget).
