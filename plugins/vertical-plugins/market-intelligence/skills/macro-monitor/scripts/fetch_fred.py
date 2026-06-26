#!/usr/bin/env python3
"""
fetch_fred.py — FRED macro series (credit spreads, leading indicators, curve).

FRED is the free gold-standard for macro/bond/leading-indicator data — NO API key needed
(uses the public fredgraph.csv export). It is BLOCKED by this cloud session's egress proxy
(fred.stlouisfed.org returns 403), so this adapter is meant to run from **GitHub Actions or
locally**, where FRED is reachable. In a blocked environment every series renders
`[blocked: FRED]`; the adapter never fabricates.

Series:
  DGS10/DGS2 (10y/2y UST) · T10Y2Y/T10Y3M (curve spreads) · BAMLH0A0HYM2 (HY OAS credit
  spread) · BAMLC0A0CM (IG OAS) · USSLIND (Conf. Board-style leading index) · ICSA (initial
  jobless claims) · NFCI (Chicago Fed financial conditions)

Usage: python3 fetch_fred.py [--json] [--selftest]
"""
import csv, io, json, os, ssl, sys, urllib.request

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context()
if os.path.exists(CA):
    try:
        CTX.load_verify_locations(CA)
    except Exception:
        pass

SERIES = {
    "10y UST": "DGS10", "2y UST": "DGS2", "2s10s": "T10Y2Y", "3m10y": "T10Y3M",
    "HY OAS (credit)": "BAMLH0A0HYM2", "IG OAS (credit)": "BAMLC0A0CM",
    "Leading Index": "USSLIND", "Jobless Claims": "ICSA", "Fin. Conditions (NFCI)": "NFCI",
}


def latest(series_id):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "fred/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        text = r.read().decode("utf-8", "replace")
    rows = [row for row in csv.reader(io.StringIO(text))][1:]
    vals = [(d, v) for d, v in rows if v not in (".", "")]
    if not vals:
        return None
    d, v = vals[-1]
    return {"value": float(v), "date": d}


def data():
    out = {}
    for label, sid in SERIES.items():
        try:
            out[label] = latest(sid)
        except Exception as e:
            out[label] = {"blocked": str(e)[:60]}
    return out


def render(d=None):
    d = d or data()
    lines = ["FRED MACRO SERIES (credit / leading indicators / curve)"]
    for label, v in d.items():
        if v and "value" in v:
            lines.append(f"  {label:<24}{v['value']:>10.2f}   ({v['date']})")
        else:
            lines.append(f"  {label:<24}{'[blocked: FRED]':>16}")
    return "\n".join(lines)


def selftest():
    mock = {"HY OAS (credit)": {"value": 3.21, "date": "2026-06-25"},
            "2s10s": {"value": 0.31, "date": "2026-06-25"},
            "Jobless Claims": {"blocked": "egress 403"}}
    print(render(mock))
    assert "3.21" in render(mock) and "[blocked: FRED]" in render(mock)
    print("  PASS — renders live values and blocked cells correctly.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--json" in sys.argv:
        print(json.dumps(data(), indent=2))
    else:
        print(render())
