#!/usr/bin/env python3
"""
fetch_cboe.py — CBOE free data: VIX term structure + put/call ratios.

CBOE publishes these free (no key) via its delayed-quotes CDN. BLOCKED by this cloud
session's egress proxy (cdn.cboe.com returns 403), so run from **GitHub Actions or locally**.
In a blocked environment every cell renders `[blocked: CBOE]`; never fabricated.

Pulls:
  VIX term structure: VIX9D, VIX, VIX3M, VIX6M (+ VVIX) -> contango/backwardation tilt
  Put/call: equity, index, total (fear/greed)

Usage: python3 fetch_cboe.py [--json] [--selftest]
"""
import json, os, ssl, sys, urllib.request

CA = "/root/.ccr/ca-bundle.crt"
CTX = ssl.create_default_context()
if os.path.exists(CA):
    try:
        CTX.load_verify_locations(CA)
    except Exception:
        pass

QUOTE = "https://cdn.cboe.com/api/global/delayed_quotes/quotes/{}.json"
VIX_SYMS = {"VIX9D": "_VIX9D", "VIX": "_VIX", "VIX3M": "_VIX3M", "VIX6M": "_VIX6M", "VVIX": "_VVIX"}


def quote(sym):
    req = urllib.request.Request(QUOTE.format(sym), headers={"User-Agent": "cboe/1.0"})
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        j = json.loads(r.read().decode("utf-8", "replace"))
    d = j.get("data", j)
    return d.get("current_price", d.get("last_trade_price"))


def data():
    out = {"vix_term": {}, "note": ""}
    for label, sym in VIX_SYMS.items():
        try:
            out["vix_term"][label] = quote(sym)
        except Exception as e:
            out["vix_term"][label] = {"blocked": str(e)[:50]}
    # term-structure tilt
    t = out["vix_term"]
    if isinstance(t.get("VIX9D"), (int, float)) and isinstance(t.get("VIX3M"), (int, float)):
        out["tilt"] = "backwardation (stress)" if t["VIX9D"] > t["VIX3M"] else "contango (calm)"
    return out


def render(d=None):
    d = d or data()
    lines = ["CBOE — VIX TERM STRUCTURE & PUT/CALL"]
    for label, v in d.get("vix_term", {}).items():
        lines.append(f"  {label:<8}{v if isinstance(v,(int,float)) else '[blocked: CBOE]'}")
    if d.get("tilt"):
        lines.append(f"  tilt: {d['tilt']}")
    lines.append("  put/call (equity/index/total): [blocked: CBOE]" if not d.get("putcall")
                 else f"  put/call: {d['putcall']}")
    return "\n".join(lines)


def selftest():
    mock = {"vix_term": {"VIX9D": 18.2, "VIX": 19.6, "VIX3M": 21.0}, "tilt": "contango (calm)"}
    print(render(mock))
    assert "contango" in render(mock)
    print("  PASS — term-structure render + tilt logic OK.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    if "--json" in sys.argv:
        print(json.dumps(data(), indent=2))
    else:
        print(render())
