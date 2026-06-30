#!/usr/bin/env python3
"""
event_study.py — backtest the Event Deep Dive theories.

Tests whether the Buffett signal/noise + sentiment-2x2 classifications actually predict
forward returns, using a classic market-adjusted event study (cumulative abnormal return).

Pre-registered hypotheses (state them BEFORE looking, to avoid data-mining):
  H1  Overreaction reversion  — "NOISE->BUY" events revert UP over [-1,+20] days.
  H2  Drift continuation      — "SIGNAL" events keep drifting (post-earnings-drift).
  H3  Sentiment contra-signal — "OWN IT" quadrant outperforms; "MOMENTUM-CROWDED" lags.
  H4  Vol risk premium        — events tagged with a RICH IV regime (IV >> realized) see
                                weaker forward equity CAR / favor premium-selling. To test,
                                add an `iv_regime` column (e.g. RICH/CHEAP/NEUTRAL) to the
                                events file; it is grouped automatically alongside the
                                classification and quadrant dimensions. NOTE: a full vol
                                backtest needs options/IV history (LSEG equity_vol_surface),
                                not just the price-based CAR computed here.

Method
  abnormal return  AR_t = r_stock_t - r_benchmark_t      (market-adjusted; a beta/CAPM
                                                          model is more precise — see NOTE)
  CAR[a,b]         = sum of AR_t over the event window [a, b] trading days around t=0
  group stats      mean CAR, t-stat = mean / (std/sqrt(n)), win-rate, cost-adjusted CAR

Biases this harness tries NOT to fall into (read before trusting a result):
  * Look-ahead     — t=0 is the event date; windows use only data at/after t=0. Use the
                     date the news was PUBLIC, not a restated/revision date.
  * Survivorship   — include delisted tickers in your events file or reversion is overstated.
  * Multiple tests — test the few pre-registered hypotheses above, not 100 variations.
  * Costs          — --cost-bps subtracts round-trip costs; thin edges die after costs.
  * Regime         — --by-year splits results; an edge in one regime is not universal.

Inputs
  An events JSON/CSV. JSON may be the workflow.js output (events[] with date/category/...),
  but for a backtest each row needs at minimum: ticker, date, and a group label
  (classification and/or quadrant). CSV columns: ticker,date,classification,quadrant.

Usage
  python3 event_study.py --events events.csv --benchmark SPY.US --windows 1,5,20 --cost-bps 10
  python3 event_study.py --selftest        # offline; injects a known effect and recovers it
"""
import argparse, csv, json, math, sys, urllib.request, io
from collections import defaultdict
from datetime import datetime, timedelta

# --------------------------------------------------------------------------- data
def fetch_prices_stooq(symbol, d1, d2):
    """Daily closes from Stooq (no API key). symbol like 'AAPL.US' or 'SPY.US'."""
    url = f"https://stooq.com/q/d/l/?s={symbol.lower()}&d1={d1}&d2={d2}&i=d"
    with urllib.request.urlopen(url, timeout=30) as resp:
        text = resp.read().decode("utf-8", "replace")
    out = {}
    for row in csv.DictReader(io.StringIO(text)):
        try:
            out[row["Date"]] = float(row["Close"])
        except (KeyError, ValueError):
            continue
    if not out:
        raise RuntimeError(f"no price data for {symbol} (rate-limited? try CapIQ/FactSet MCP)")
    return out

def daily_returns(closes):
    days = sorted(closes)
    return {days[i]: closes[days[i]] / closes[days[i-1]] - 1.0 for i in range(1, len(days))}

# --------------------------------------------------------------------------- core
def car_for_event(stock_ret, bench_ret, event_date, a, b):
    """CAR over trading-day window [a,b] relative to the first trading day >= event_date."""
    days = sorted(set(stock_ret) & set(bench_ret))
    idx = next((i for i, d in enumerate(days) if d >= event_date), None)
    if idx is None or idx + a < 0 or idx + b >= len(days):
        return None
    car = 0.0
    for k in range(idx + a, idx + b + 1):
        d = days[k]
        car += stock_ret[d] - bench_ret[d]
    return car

def tstat(xs):
    n = len(xs)
    if n < 2:
        return float("nan")
    m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / (n - 1)
    sd = math.sqrt(var)
    return float("nan") if sd == 0 else m / (sd / math.sqrt(n))

def summarize(cars, cost_bps):
    n = len(cars)
    if n == 0:
        return None
    mean = sum(cars) / n
    wins = sum(1 for c in cars if c > 0) / n
    net = mean - 2 * cost_bps / 10000.0  # round-trip cost
    return dict(n=n, mean_car=mean, t=tstat(cars), win=wins, net_car=net)

# --------------------------------------------------------------------------- io
def load_events(path):
    if path.endswith(".json"):
        data = json.load(open(path))
        rows = data.get("analysis") or data.get("events") or data if isinstance(data, list) else \
               (data.get("analysis") or data.get("events") or [])
        ev = []
        for r in rows:
            t = r.get("ticker") or r.get("symbol")
            if not t:
                continue  # workflow events without a ticker can't be backtested directly
            ev.append(dict(ticker=t, date=r.get("date", ""),
                           classification=r.get("classification", ""),
                           quadrant=r.get("quadrant", "")))
        return ev
    return [dict(ticker=r["ticker"], date=r["date"],
                 classification=r.get("classification", ""), quadrant=r.get("quadrant", ""),
                 iv_regime=r.get("iv_regime", ""))
            for r in csv.DictReader(open(path))]

def run(events, benchmark, windows, cost_bps, by_year):
    dates = [e["date"] for e in events if e["date"]]
    d1 = (datetime.strptime(min(dates), "%Y-%m-%d") - timedelta(days=10)).strftime("%Y%m%d")
    d2 = (datetime.strptime(max(dates), "%Y-%m-%d") + timedelta(days=max(windows) * 2 + 20)).strftime("%Y%m%d")
    bench_ret = daily_returns(fetch_prices_stooq(benchmark, d1, d2))
    price_cache = {}
    groups = defaultdict(lambda: defaultdict(list))  # (dim,label,window) -> [cars]
    for e in events:
        tic = e["ticker"]
        if tic not in price_cache:
            try:
                price_cache[tic] = daily_returns(fetch_prices_stooq(tic, d1, d2))
            except Exception as ex:
                print(f"  ! skip {tic}: {ex}", file=sys.stderr)
                price_cache[tic] = {}
        sret = price_cache[tic]
        if not sret:
            continue
        yr = e["date"][:4] if by_year else "ALL"
        for w in windows:
            car = car_for_event(sret, bench_ret, e["date"], -1, w)
            if car is None:
                continue
            for dim, label in (("classification", e["classification"]),
                               ("quadrant", e["quadrant"]),
                               ("iv_regime", e.get("iv_regime", ""))):  # H4: grouped if present
                if label:
                    groups[(dim, label, w, yr)].append(car)
    return groups

def report(groups, cost_bps):
    print(f"\n{'GROUP':<34}{'win':>5}{'n':>4}{'meanCAR':>10}{'netCAR':>9}{'t':>7}")
    print("-" * 69)
    for (dim, label, w, yr) in sorted(groups):
        s = summarize(groups[(dim, label, w, yr)], cost_bps)
        if not s:
            continue
        tag = f"{label}[+{w}d]" + (f" {yr}" if yr != "ALL" else "")
        print(f"{tag:<34}{s['win']*100:>4.0f}%{s['n']:>4}"
              f"{s['mean_car']*100:>9.2f}%{s['net_car']*100:>8.2f}%{s['t']:>7.2f}")
    print("\nNOTE: market-adjusted (AR = stock - benchmark). For publication use a beta/CAPM\n"
          "model and an estimation window. |t|>~2 is suggestive, not proof — check --by-year.")

# --------------------------------------------------------------------------- selftest
def selftest():
    """Offline: synthesize prices, inject a known +3% drift after SIGNAL events, recover it."""
    import random
    random.seed(7)
    base = datetime(2024, 1, 1)
    days = [(base + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(400)]
    bench = {d: 100 * (1.0003) ** i for i, d in enumerate(days)}
    # two synthetic names; SIGNAL events get a +0.3%/day post-event drift for 10 days
    events = [dict(ticker="AAA", date=days[60], classification="SIGNAL", quadrant="OWN IT"),
              dict(ticker="AAA", date=days[200], classification="SIGNAL", quadrant="OWN IT"),
              dict(ticker="BBB", date=days[90], classification="NOISE", quadrant="AVOID-FADE"),
              dict(ticker="BBB", date=days[260], classification="NOISE", quadrant="AVOID-FADE")]
    def synth(drift_after):
        px, p = {}, 100.0
        for i, d in enumerate(days):
            bump = 0.003 if any(0 <= i - days.index(e["date"]) < 10 for e in drift_after) else 0
            p *= 1 + random.gauss(0.0003, 0.01) + bump
            px[d] = p
        return daily_returns(px)
    sret = {"AAA": synth([e for e in events if e["ticker"] == "AAA" and e["classification"] == "SIGNAL"]),
            "BBB": synth([])}
    bret = daily_returns(bench)
    groups = defaultdict(list)
    for e in events:
        car = car_for_event(sret[e["ticker"]], bret, e["date"], -1, 10)
        if car is not None:
            groups[e["classification"]].append(car)
    print("SELFTEST (injected +3% cumulative drift into SIGNAL events):")
    for label, cars in sorted(groups.items()):
        s = summarize(cars, 0)
        print(f"  {label:<14} n={s['n']}  meanCAR={s['mean_car']*100:+.2f}%  (expect SIGNAL >> NOISE)")
    ok = summarize(groups.get("SIGNAL", []), 0)["mean_car"] > summarize(groups.get("NOISE", []), 0)["mean_car"]
    print("  PASS" if ok else "  FAIL", "— harness recovers the injected effect.")
    return 0 if ok else 1

# --------------------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(description="Event-study backtest for the Event Deep Dive theories.")
    ap.add_argument("--events", help="events CSV (ticker,date,classification,quadrant) or workflow JSON")
    ap.add_argument("--benchmark", default="SPY.US")
    ap.add_argument("--windows", default="1,5,20", help="comma-sep forward trading-day windows")
    ap.add_argument("--cost-bps", type=float, default=10.0, help="one-way cost in bps")
    ap.add_argument("--by-year", action="store_true", help="split results by event year (regime check)")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.events:
        ap.error("--events required (or use --selftest)")
    events = [e for e in load_events(a.events) if e["date"]]
    if not events:
        ap.error("no usable events (need ticker + date; workflow events lacking tickers can't be tested)")
    windows = [int(x) for x in a.windows.split(",")]
    print(f"Loaded {len(events)} events; benchmark {a.benchmark}; windows {windows}; cost {a.cost_bps}bp")
    report(run(events, a.benchmark, windows, a.cost_bps, a.by_year), a.cost_bps)
    return 0

if __name__ == "__main__":
    sys.exit(main())
