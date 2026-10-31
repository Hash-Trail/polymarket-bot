"""Recomputes the numbers quoted in the video from the CSV files in ../data."""
import csv
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"


def rows(name: str) -> list[dict]:
    with open(DATA / name, newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    by_result = {r["result"]: r for r in rows("by_result.csv")}
    staked = sum(float(r["staked_usd"]) for r in by_result.values())
    pnl = sum(float(r["pnl_usd"]) for r in by_result.values())
    fees = sum(float(r["fees_usd"]) for r in by_result.values())
    won, lost = int(by_result["Won"]["bets"]), int(by_result["Lost"]["bets"])

    price = rows("by_price.csv")
    avg_price = sum(float(r["avg_price_cents"]) * int(r["bets"]) for r in price) / sum(int(r["bets"]) for r in price)

    print(f"bets that reached a result:   {won + lost}")
    print(f"won:                          {won / (won + lost):.1%}")
    print(f"average price paid:           {avg_price:.1f}c")
    print(f"total staked:                 ${staked:,.2f}")
    print(f"result:                       ${pnl:,.2f} ({pnl / staked:+.2%} of staked)")
    print(f"fees:                         ${fees:,.2f} ({fees / staked:.2%} of staked)")
    for r in rows("monthly.csv"):
        print(f"month {r['month_bet_placed']}:                {float(r['pnl_pct_of_staked']):+.2f}%")
    weeks = rows("weekly.csv")
    up = sum(float(r["pnl_usd"]) > 0 for r in weeks)
    print(f"weeks up / down:              {up} / {len(weeks) - up}")


if __name__ == "__main__":
    main()
