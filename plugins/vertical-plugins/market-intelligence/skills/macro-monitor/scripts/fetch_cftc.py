#!/usr/bin/env python3
"""
fetch_cftc.py — CFTC Commitment-of-Traders positioning (FMP, allowlisted).

Institutions watch COT to see how speculators are positioned (crowded longs/shorts =
contrarian signal). Pulls FMP's COT analysis and filters to the headline contracts.

Auth: FMP_API_KEY from env (never printed). Usage: python3 fetch_cftc.py [--json]
"""
import json, os, ssl, sys, urllib.parse, urllib.request

BASE = "https://financialmodelingprep.com/stable"
_CA = "/root/.ccr/ca-bundle.crt"
_CTX = ssl.create_default_context()
if os.path.exists(_CA):
    try:
        _CTX.load_verify_locations(_CA)
    except Exception:
        pass

WATCH = ["S&P 500", "Nasdaq", "Gold", "Silver", "Crude Oil", "US Dollar",
         "10 Year", "2 Year", "VIX"]


def fmp(path, **params):
    key = os.environ.get("FMP_API_KEY")
    if not key:
        sys.exit("ERROR: FMP_API_KEY not set.")
    params["apikey"] = key
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "cftc/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=_CTX) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def data():
    rows = fmp("commitment-of-traders-analysis")
    rows = rows if isinstance(rows, list) else []
    seen, out = set(), []
    for r in rows:
        name = r.get("name", "")
        if any(w.lower() in name.lower() for w in WATCH) and name not in seen:
            seen.add(name)
            out.append({"name": name, "situation": r.get("marketSituation"),
                        "net": r.get("netPostion", r.get("netPosition")),
                        "prevNet": r.get("previousNetPosition"), "date": r.get("date", "")[:10]})
    return out


def render():
    rows = data()
    out = ["CFTC POSITIONING (COT — speculators; crowded = contrarian)",
           f"  {'contract':<22}{'situation':<12}{'net':>12}{'prev':>12}"]
    for r in rows:
        out.append(f"  {str(r['name'])[:21]:<22}{str(r['situation']):<12}"
                   f"{str(r['net']):>12}{str(r['prevNet']):>12}")
    if len(out) == 2:
        out.append("  (no watched contracts returned)")
    return "\n".join(out)


if __name__ == "__main__":
    if "--json" in sys.argv:
        print(json.dumps(data(), indent=2))
    else:
        print(render())
