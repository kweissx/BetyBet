#!/usr/bin/env python3
"""Summarise ledger/ledger.csv: profit, ROI, hit rate, CLV and drawdown."""
import csv
import sys
from pathlib import Path

START_BANKROLL = 2000.0
LEDGER = Path(__file__).resolve().parent.parent / "ledger" / "ledger.csv"


def num(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def main(path=LEDGER):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    settled = [r for r in rows if r["result"].strip()]
    open_picks = len(rows) - len(settled)
    if not settled:
        print(f"No settled picks yet ({open_picks} open). Bankroll: {START_BANKROLL:.0f} MXN")
        return

    staked = sum(num(r["stake_mxn"]) or 0 for r in settled)
    pnl = sum(num(r["pnl_mxn"]) or 0 for r in settled)
    wins = sum(r["result"].strip().upper() in ("W", "HW") for r in settled)
    decided = sum(r["result"].strip().upper() != "P" for r in settled)
    clvs = [c for c in (num(r["clv_pct"]) for r in settled) if c is not None]

    bankroll = peak = START_BANKROLL
    max_dd = 0.0
    for r in settled:
        bankroll += num(r["pnl_mxn"]) or 0
        peak = max(peak, bankroll)
        max_dd = max(max_dd, (peak - bankroll) / peak)

    print(f"Settled picks: {len(settled)}  (open: {open_picks})")
    print(f"Hit rate:      {wins}/{decided} = {100 * wins / max(decided, 1):.1f}%")
    print(f"Staked:        {staked:.0f} MXN")
    print(f"Profit:        {pnl:+.0f} MXN")
    print(f"ROI:           {100 * pnl / staked:+.1f}%" if staked else "ROI: n/a")
    if clvs:
        beat = sum(c > 0 for c in clvs)
        print(f"Avg CLV:       {sum(clvs) / len(clvs):+.2f}%  (beat close {beat}/{len(clvs)})")
    print(f"Bankroll:      {bankroll:.0f} MXN  (start {START_BANKROLL:.0f}, max drawdown {100 * max_dd:.1f}%)")
    if len(settled) < 150:
        print(f"Progress to graduation review: {len(settled)}/150 settled picks")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else LEDGER)
