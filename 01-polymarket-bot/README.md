# Case 01 — My Polymarket bot won 93% of its bets and still lost money

A bot bought outcome shares on Polymarket at 90–95¢ ("prediction market bonds") with real money,
from **March 19 to June 10, 2026**, with a bank of about $100 and bets of about $2.

Recompute everything below:

```
python3 scripts/recompute.py
```

## The numbers from the video

| Claim | Value | File |
|---|---|---|
| Bets that reached a result (won or lost) | 807 | `data/by_result.csv` |
| Average price paid | 93.0¢ | `data/by_price.csv` |
| Won | 93.3% | `data/by_result.csv` |
| Total staked over the period | $1,520.96 | `data/by_result.csv` |
| Result | −$12.62, **−0.83%** of everything staked | `data/by_result.csv` |
| Fees | $6.51, 0.43% of staked | `data/by_result.csv` |
| Result by month (bet placed): Mar / Apr / May / Jun | +1.60% / +3.20% / −3.73% / −5.45% | `data/monthly.csv` |
| Weeks up / down (by week a bet was resolved) | 10 / 7 | `data/weekly.csv` |

"Before fees +0.3%, fees 0.4%" in the video refers to won + lost bets only; the rest of the loss comes
from emergency sales (`StoppedOut`) and cancelled markets (`Void`).

## Data

All files come from the bot's own database (table of real bets, dry-run bets excluded), exported on Oct 31, 2026.

- `by_result.csv` — totals by outcome: `Won`, `Lost`, `StoppedOut` (sold early by a stop-loss), `Void` (market cancelled).
- `by_price.csv` — won / lost bets grouped by the price paid.
- `time_to_close.csv` — won / lost bets grouped by how long before the market's scheduled end the bet was placed.
- `monthly.csv` — result by the month a bet was placed, as in the video's monthly chart.
- `weekly.csv` — result by the week a bet was resolved, as in the video's weekly chart.

Individual bets are not published: a single trade (market + minute + price) is enough to find the bot's wallet on chain.

## The backtest

The plan came from a backtest on public Polymarket data: every position of leaderboard traders bought at
90–95¢, **118,872 positions**. As shown in the video:

| Bought at | Won | Per bet |
|---|---|---|
| 90–92¢ | 97.0% | +6.7% |
| 92–95¢ | 97.9% | +4.8% |

Two holes explained in the video:

1. **Average price per position.** The data stores one average price per position, which mixes risky buys
   with near-certain buys made after the outcome was already clear. Counting individual trades instead,
   top traders won about **95% at 93¢**, not 97%.
2. **Missing losses.** Losing positions with a $0 payout that were never claimed don't show up as closed
   positions — over 1,600 of them were missing from the backtest.

The raw backtest data (other traders' wallets and positions) is not republished here.
It comes from Polymarket's public data API (`/positions`, `/closed-positions`, `/trades`).

## Not financial advice

This is a record of one experiment and its result.
