#!/usr/bin/env python3
"""
fetch_fmp.py — the FMP (cloud) data layer for the vol-pulse dashboard.

Pulls what FMP can actually serve — top movers, realized vol, spot VIX — and renders the
FMP tier of the VOL & FLOW PULSE. Cells FMP cannot serve are printed honestly:
  * IV rank / skew / term structure / option volume  -> [needs IBKR]  (local gateway)
  * VIX9D / VVIX / VIX3M                              -> [needs source] (CBOE-free or IBKR)
  * put/call ratio                                    -> [needs source] (CBOE-free daily file)

Auth: reads FMP_API_KEY from the environment (already set in cloud sessions; locally put it
in a gitignored .env and `export`/source it). The key is never printed.

Uses FMP's current /stable/ API (the old /api/v3/ paths are deprecated and 403).

Usage
  python3 fetch_fmp.py                       # full dashboard
  python3 fetch_fmp.py --indexes SPY QQQ IWM # RV proxies for SPX/NDX/RUT
  python3 fetch_fmp.py --json                # raw JSON instead of the rendered panel
"""
import argparse, json, math, os, ssl, sys, urllib.parse, urllib.request
from datetime import datetime

BASE = "https://financialmodelingprep.com/stable"

# In cloud sessions an intercepting proxy is used; trust its CA if present. Harmless locally.
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
        sys.exit("ERROR: FMP_API_KEY not set (cloud: env settings; local: .env then export).")
    params["apikey"] = key
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "vol-pulse/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=_CTX) as r:
        data = json.loads(r.read().decode("utf-8", "replace"))
    if isinstance(data, dict) and ("Error Message" in data or "Premium Query Parameter" in str(data)):
        raise RuntimeError(str(data)[:160])
    return data


def realized_vol(closes, window):
    """Annualized close-to-close realized vol over the last `window` returns."""
    if len(closes) < window + 1:
        return None
    rets = [math.log(closes[i] / closes[i - 1]) for i in range(1, len(closes))][-window:]
    m = sum(rets) / len(rets)
    var = sum((x - m) ** 2 for x in rets) / (len(rets) - 1)
    return math.sqrt(var) * math.sqrt(252) * 100  # %, annualized


def get_rv(symbol):
    rows = fmp("historical-price-eod/full", symbol=symbol)
    rows = rows if isinstance(rows, list) else rows.get("historical", [])
    closes = [r["close"] for r in sorted(rows, key=lambda x: x["date"])][-120:]
    return {w: realized_vol(closes, w) for w in (20, 60, 90)}


def movers(kind, n=5):
    rows = fmp(kind)
    return rows[:n] if isinstance(rows, list) else []


def fnum(v, suf="", w=8):
    return f"{v:>{w}.2f}{suf}" if isinstance(v, (int, float)) else f"{'[needs IBKR]':>{w}}"


def render(indexes):
    asof = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    out = [f"VOL & FLOW PULSE — {asof}  (FMP live tier)", "=" * 60, "",
           "REALIZED VOL (annualized, FMP EOD)   |  IV-derived = [needs IBKR]",
           f"{'idx':<6}{'RV20':>9}{'RV60':>9}{'RV90':>9}   IVrank/skew/term"]
    for sym in indexes:
        try:
            rv = get_rv(sym)
            out.append(f"{sym:<6}{fnum(rv[20],'%',8)} {fnum(rv[60],'%',8)} {fnum(rv[90],'%',8)}"
                       f"   [needs IBKR]")
        except Exception as e:
            out.append(f"{sym:<6}  error: {str(e)[:40]}")
    # Spot VIX
    try:
        vix = fmp("quote", symbol="^VIX")[0]
        out += ["", f"VIX spot: {vix['price']:.2f} ({vix.get('changePercentage',0):+.2f}%)"
                    f"   |  VIX9D/VVIX/VIX3M: [needs source: CBOE-free or IBKR]"]
    except Exception as e:
        out += ["", f"VIX: error {str(e)[:50]}"]
    # Movers
    for kind, label in (("most-actives", "MOST ACTIVE"), ("biggest-gainers", "TOP GAINERS"),
                        ("biggest-losers", "TOP LOSERS")):
        out += ["", f"{label}", f"{'sym':<8}{'price':>10}{'chg%':>9}"]
        for m in movers(kind):
            pct = m.get("changesPercentage", m.get("changePercentage"))
            out.append(f"{m.get('symbol',''):<8}{fnum(m.get('price'),'',10)}{fnum(pct,'%',8)}")
    out += ["", "PUT/CALL ratio: [needs source: CBOE-free daily file]",
            "Option volume / OI / Greeks: [needs IBKR — local gateway]", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--indexes", nargs="+", default=["SPY", "QQQ", "IWM"],
                    help="ETF proxies for SPX/NDX/RUT realized vol")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.json:
        data = {"asof": datetime.utcnow().isoformat() + "Z",
                "rv": {s: get_rv(s) for s in a.indexes},
                "vix": fmp("quote", symbol="^VIX")[0],
                "movers": {k: movers(k) for k in ("most-actives", "biggest-gainers", "biggest-losers")}}
        print(json.dumps(data, indent=2))
    else:
        print(render(a.indexes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
