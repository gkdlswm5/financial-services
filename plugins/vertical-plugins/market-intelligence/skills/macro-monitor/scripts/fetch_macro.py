#!/usr/bin/env python3
"""
fetch_macro.py — the FMP macro/bonds/events layer for the macro-monitor dashboard.

Renders what FMP (allowlisted) can serve:
  * Treasury yield curve (1mo..30yr) + key spreads (2s10s, 3m10y) + inversion flags
  * Economic-events calendar (high/medium-impact US releases, with estimate vs actual)
  * Key economic / leading indicators (GDP, CPI, unemployment, fed funds, ...)

Cells that need policy-blocked sources are printed honestly:
  * Credit spreads (HY OAS), Conference Board LEI, jobless-claims series -> FRED  [blocked]
  * VIX term structure / put-call                                       -> CBOE  [blocked]
  (Both 403 at this environment's egress proxy. Allowlist those hosts in the environment's
  network policy, or run this adapter locally, to fill them.)

Auth: reads FMP_API_KEY from the environment (never printed). Uses FMP /stable/ endpoints.

Usage
  python3 fetch_macro.py                  # full macro dashboard
  python3 fetch_macro.py --calendar-days 7
  python3 fetch_macro.py --json
"""
import argparse, json, os, ssl, sys, urllib.parse, urllib.request
from datetime import datetime, timedelta

BASE = "https://financialmodelingprep.com/stable"
_CA = "/root/.ccr/ca-bundle.crt"
_CTX = ssl.create_default_context()
if os.path.exists(_CA):
    try:
        _CTX.load_verify_locations(_CA)
    except Exception:
        pass


def fmp(path, **params):
    key = os.environ.get("FMP_API_KEY")
    if not key:
        sys.exit("ERROR: FMP_API_KEY not set.")
    params["apikey"] = key
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "macro-monitor/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=_CTX) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def treasury():
    rows = fmp("treasury-rates")
    return rows[0] if isinstance(rows, list) and rows else {}


def curve_panel(t):
    if not t:
        return ["TREASURY CURVE: unavailable"]
    tenors = [("1M", "month1"), ("3M", "month3"), ("6M", "month6"), ("1Y", "year1"),
              ("2Y", "year2"), ("5Y", "year5"), ("10Y", "year10"), ("30Y", "year30")]
    line = "  ".join(f"{lbl} {t.get(k):.2f}" for lbl, k in tenors if isinstance(t.get(k), (int, float)))
    s2_10 = (t.get("year10", 0) - t.get("year2", 0))
    s3m10 = (t.get("year10", 0) - t.get("month3", 0))
    def tag(s):
        return "INVERTED (recession signal)" if s < 0 else ("flat" if s < 0.2 else "normal/steep")
    return [f"TREASURY CURVE  (as of {t.get('date','?')})", "  " + line,
            f"  2s10s: {s2_10:+.2f}  [{tag(s2_10)}]    3m10y: {s3m10:+.2f}  [{tag(s3m10)}]"]


def calendar_panel(days, min_impact=("High", "Medium")):
    today = datetime.utcnow().date()
    rows = fmp("economic-calendar",
               **{"from": today.isoformat(), "to": (today + timedelta(days=days)).isoformat()})
    us = [r for r in rows if r.get("country") == "US" and r.get("impact") in min_impact]
    us.sort(key=lambda r: r.get("date", ""))
    out = [f"BIG MACRO EVENTS — next {days}d (US, high/med impact)",
           f"  {'when':<17}{'event':<34}{'est':>8}{'prev':>8}"]
    for r in us[:14]:
        out.append(f"  {r.get('date','')[:16]:<17}{str(r.get('event',''))[:33]:<34}"
                   f"{str(r.get('estimate','')):>8}{str(r.get('previous','')):>8}")
    if len(out) == 2:
        out.append("  (no high/medium-impact US events in window)")
    return out


INDICATORS = [("GDP", "GDP"), ("Real GDP", "realGDP"), ("CPI", "CPI"),
              ("Unemployment %", "unemploymentRate"), ("Fed Funds %", "federalFunds"),
              ("Retail Sales", "retailSales"), ("Consumer Sentiment", "consumerSentiment")]


def indicators_panel():
    out = ["KEY INDICATORS (latest)"]
    for label, name in INDICATORS:
        try:
            rows = fmp("economic-indicators", name=name)
            if isinstance(rows, list) and rows:
                latest = sorted(rows, key=lambda x: x.get("date", ""))[-1]
                out.append(f"  {label:<20}{latest.get('value'):>12}   ({latest.get('date','')})")
        except Exception:
            out.append(f"  {label:<20}{'[n/a]':>12}")
    return out


def render(days):
    asof = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    out = [f"MACRO MONITOR — {asof}  (FMP live)", "=" * 64, ""]
    out += curve_panel(treasury()) + [""]
    out += calendar_panel(days) + [""]
    out += indicators_panel() + [""]
    out += ["BLOCKED in this environment (egress policy 403 — allowlist or run local):",
            "  Credit spreads (HY OAS), Conf. Board LEI, jobless claims  -> FRED  [blocked]",
            "  VIX term structure / put-call ratio                       -> CBOE  [blocked]", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--calendar-days", type=int, default=7)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.json:
        today = datetime.utcnow().date()
        print(json.dumps({
            "asof": datetime.utcnow().isoformat() + "Z",
            "treasury": treasury(),
            "calendar": fmp("economic-calendar", **{"from": today.isoformat(),
                            "to": (today + timedelta(days=a.calendar_days)).isoformat()}),
        }, indent=2)[:4000])
    else:
        print(render(a.calendar_days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
