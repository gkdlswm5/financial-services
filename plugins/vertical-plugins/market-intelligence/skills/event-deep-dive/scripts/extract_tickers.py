#!/usr/bin/env python3
"""
extract_tickers.py — turn an Event Deep Dive workflow result into a backtestable events file.

The workflow (workflow.js) emits events[] (with dates) and analysis[] (with classification +
quadrant) keyed by headline, but no ticker column. This script extracts likely tickers from
the headlines/summaries (via a name->ticker map plus an explicit-ticker regex), joins the
date from events[] and the classification/quadrant from analysis[], and writes a CSV that
event_study.py consumes directly.

Honest limits:
  * Only company/micro events carry a ticker — macro events (rates, oil, FX) are dropped.
  * Name->ticker mapping is best-effort; review the output before trusting a backtest.
  * One headline can mention several names (e.g. "AMD/Intel led lower") -> multiple rows.

Usage
  python3 extract_tickers.py --in result.json --out events.csv
  python3 extract_tickers.py --selftest
"""
import argparse, csv, json, re, sys

# Common names that show up in macro/sector event headlines -> primary US listing.
NAME_TO_TICKER = {
    "nvidia": "NVDA", "broadcom": "AVGO", "amd": "AMD", "intel": "INTC", "micron": "MU",
    "tsmc": "TSM", "taiwan semiconductor": "TSM", "asml": "ASML", "microsoft": "MSFT",
    "meta": "META", "alphabet": "GOOGL", "google": "GOOGL", "amazon": "AMZN", "apple": "AAPL",
    "exxonmobil": "XOM", "exxon": "XOM", "chevron": "CVX", "hess": "HES", "occidental": "OXY",
    "jpmorgan": "JPM", "jp morgan": "JPM", "goldman sachs": "GS", "goldman": "GS",
    "morgan stanley": "MS", "wells fargo": "WFC", "citigroup": "C", "citi": "C",
    "bank of america": "BAC",
}
# Explicit ticker like "(NVDA)" or "$NVDA" or "NVDA" near a verb; conservative to avoid noise.
TICKER_RE = re.compile(r"\(([A-Z]{1,5})\)|\$([A-Z]{1,5})\b")
# ETFs / index proxies we DO want to keep if they appear.
KNOWN_TICKERS = set(NAME_TO_TICKER.values()) | {"SPY", "QQQ", "IWM", "XLF", "XLE", "SMH", "GLD", "SLV"}


def tickers_in(text):
    found = []
    for m in TICKER_RE.finditer(text or ""):
        t = m.group(1) or m.group(2)
        if t in KNOWN_TICKERS:
            found.append(t)
    low = (text or "").lower()
    for name, tic in NAME_TO_TICKER.items():
        if name in low:
            found.append(tic)
    # de-dupe, preserve order
    seen, out = set(), []
    for t in found:
        if t not in seen:
            seen.add(t)
            out.append(t)
    return out


def extract(result):
    events = result.get("events", []) or []
    analysis = result.get("analysis", []) or []
    date_by_headline = {e.get("headline", ""): e.get("date", "") for e in events if e.get("date")}
    rows, seen = [], set()
    # Prefer analysis[] (has classification+quadrant); fall back to events[] text for tickers.
    src = analysis if analysis else events
    for item in src:
        hl = item.get("headline", "")
        date = date_by_headline.get(hl, item.get("date", ""))
        text = hl + " " + (item.get("summary", "") or "")
        for tic in tickers_in(text):
            key = (tic, date)
            if not date or key in seen:
                continue
            seen.add(key)
            rows.append(dict(
                ticker=f"{tic}.US", date=date,
                classification=item.get("classification", ""),
                quadrant=item.get("quadrant", ""),
                headline=hl[:80],
            ))
    return rows


def write_csv(rows, path):
    cols = ["ticker", "date", "classification", "quadrant", "headline"]
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)


def selftest():
    sample = {
        "events": [
            {"headline": "Nvidia posts record Q1 results", "date": "2026-05-20"},
            {"headline": "Broadcom's cautious AI outlook triggers selloff, dragging AMD/Intel", "date": "2026-06-04"},
            {"headline": "Fed holds rates at 3.50-3.75%", "date": "2026-06-17"},
        ],
        "analysis": [
            {"headline": "Nvidia posts record Q1 results", "classification": "SIGNAL", "quadrant": "AVOID-FADE",
             "summary": "Nvidia (NVDA) beat."},
            {"headline": "Broadcom's cautious AI outlook triggers selloff, dragging AMD/Intel",
             "classification": "NOISE->BUY", "quadrant": "OWN IT", "summary": "Broadcom and AMD fell."},
            {"headline": "Fed holds rates at 3.50-3.75%", "classification": "NOISE", "quadrant": "OWN IT",
             "summary": "Macro only, no ticker."},
        ],
    }
    rows = extract(sample)
    tickers = sorted({r["ticker"] for r in rows})
    print("SELFTEST extracted:", tickers)
    ok = tickers == ["AMD.US", "AVGO.US", "INTC.US", "NVDA.US"]
    print("  PASS" if ok else f"  FAIL (got {tickers})", "— macro-only event correctly dropped.")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Extract a backtestable events CSV from a workflow result.")
    ap.add_argument("--in", dest="inp", help="workflow result JSON")
    ap.add_argument("--out", default="events.csv")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.inp:
        ap.error("--in required (or --selftest)")
    result = json.load(open(a.inp))
    result = result.get("result", result)  # tolerate the task-output wrapper
    rows = extract(result)
    write_csv(rows, a.out)
    print(f"Wrote {len(rows)} ticker-events to {a.out} "
          f"({len({r['ticker'] for r in rows})} unique names). Review before backtesting.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
