#!/usr/bin/env python3
"""
build_dashboard.py — assemble the hosted Market Intelligence dashboard.

Orchestrates the per-skill adapters (FMP movers/vol, macro curve/calendar/indicators, CFTC
positioning, FRED credit/leading, CBOE vol term structure), evaluates threshold alerts, and
writes a self-contained static page to dist/ for GitHub Pages.

Designed to run from GitHub Actions or locally — NOT this restricted cloud sandbox, where
FRED/CBOE are egress-blocked (they degrade gracefully to [blocked] cells). FMP requires
FMP_API_KEY in the environment.

Every source is wrapped in try/except so one failure never sinks the build. Outputs:
  dist/index.html   — the dashboard
  dist/data.json    — the raw combined data (+ alerts)

Usage: python3 build_dashboard.py [--out dist]
"""
import argparse, html, importlib.util, json, os, sys
from datetime import datetime, timedelta, timezone

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "skills"))


def load(modname, relpath):
    path = os.path.join(ROOT, relpath)
    spec = importlib.util.spec_from_file_location(modname, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def safe(fn, default=None):
    try:
        return fn()
    except Exception as e:
        return {"error": str(e)[:80]} if default is None else default


def collect():
    fmp_mod = load("fetch_fmp", "vol-pulse/scripts/fetch_fmp.py")
    macro = load("fetch_macro", "macro-monitor/scripts/fetch_macro.py")
    cftc = load("fetch_cftc", "macro-monitor/scripts/fetch_cftc.py")
    fred = load("fetch_fred", "macro-monitor/scripts/fetch_fred.py")
    cboe = load("fetch_cboe", "vol-pulse/scripts/fetch_cboe.py")

    t = safe(macro.treasury, {})
    spreads = {}
    if isinstance(t, dict) and "year10" in t:
        spreads = {"2s10s": round(t["year10"] - t.get("year2", 0), 2),
                   "3m10y": round(t["year10"] - t.get("month3", 0), 2)}
    today = datetime.now(timezone.utc).date()
    cal = safe(lambda: macro.fmp("economic-calendar", **{"from": today.isoformat(),
               "to": (today + timedelta(days=7)).isoformat()}), [])
    cal = [r for r in cal if isinstance(r, dict) and r.get("country") == "US"
           and r.get("impact") in ("High", "Medium")][:12] if isinstance(cal, list) else []
    vix = safe(lambda: fmp_mod.fmp("quote", symbol="^VIX")[0].get("price"))
    return {
        "asof": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "treasury": t, "spreads": spreads, "calendar": cal,
        "movers": {k: safe(lambda k=k: fmp_mod.movers(k), []) for k in
                   ("most-actives", "biggest-gainers", "biggest-losers")},
        "vix": vix,
        "cftc": safe(cftc.data, []),
        "fred": safe(fred.data, {}),
        "cboe": safe(cboe.data, {}),
    }


def _row(cells):
    return "<tr>" + "".join(f"<td>{html.escape(str(c))}</td>" for c in cells) + "</tr>"


def render_html(d, alerts):
    badge = {"critical": "#c0392b", "warning": "#e67e22", "info": "#2980b9"}
    abanner = "".join(
        f'<div class="alert" style="border-left:5px solid {badge[a["level"]]}">'
        f'<b>{a["level"].upper()}</b> — {html.escape(a["msg"])}</div>' for a in alerts
    ) or '<div class="alert ok">No alerts — thresholds nominal.</div>'

    t = d.get("treasury", {})
    curve = _row([f"{k.upper()} {t.get(v)}" for k, v in
                  [("1M", "month1"), ("3M", "month3"), ("2Y", "year2"), ("10Y", "year10"), ("30Y", "year30")]
                  if isinstance(t.get(v), (int, float))]) if t else ""
    sp = d.get("spreads", {})
    cal = "".join(_row([e.get("date", "")[:16], e.get("event", "")[:40],
                        e.get("estimate", ""), e.get("previous", "")]) for e in d.get("calendar", []))
    losers = "".join(_row([m.get("symbol", ""), m.get("price", ""),
                          m.get("changesPercentage", m.get("changePercentage", ""))])
                     for m in d.get("movers", {}).get("biggest-losers", [])[:5])
    gainers = "".join(_row([m.get("symbol", ""), m.get("price", ""),
                           m.get("changesPercentage", m.get("changePercentage", ""))])
                      for m in d.get("movers", {}).get("biggest-gainers", [])[:5])
    cftc = "".join(_row([c.get("name", "")[:24], c.get("situation", ""), c.get("net", "")])
                   for c in (d.get("cftc", []) or [])[:8])
    fred = "".join(_row([k, (v.get("value") if isinstance(v, dict) and "value" in v else "[blocked: FRED]")])
                   for k, v in (d.get("fred", {}) or {}).items())
    cb = (d.get("cboe", {}) or {}).get("vix_term", {})
    cboe_rows = "".join(_row([k, v]) for k, v in cb.items() if isinstance(v, (int, float)))
    cboe_tilt = (d.get("cboe", {}) or {}).get("tilt", "")

    return f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Market Intelligence Dashboard</title>
<style>
 body{{font:14px/1.5 -apple-system,Segoe UI,Roboto,sans-serif;margin:0;background:#0f1115;color:#e6e6e6}}
 header{{padding:16px 24px;background:#161922;border-bottom:1px solid #262b36}}
 h1{{font-size:18px;margin:0}} .as-of{{color:#8a93a3;font-size:12px}}
 main{{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;padding:24px;max-width:1200px}}
 .card{{background:#161922;border:1px solid #262b36;border-radius:10px;padding:16px}}
 .card h2{{font-size:13px;text-transform:uppercase;letter-spacing:.05em;color:#9aa4b2;margin:0 0 10px}}
 table{{width:100%;border-collapse:collapse}} td{{padding:4px 6px;border-bottom:1px solid #20242e}}
 .alert{{background:#1b1f29;margin:6px 24px;padding:10px 14px;border-radius:6px}}
 .alert.ok{{border-left:5px solid #27ae60;color:#9aa4b2}}
 .spread{{font-size:20px;font-weight:600}} .blocked{{color:#7a8595;font-style:italic}}
</style></head><body>
<header><h1>📊 Market Intelligence Dashboard</h1><div class="as-of">as of {html.escape(d.get('asof',''))} · auto-generated</div></header>
{abanner}
<main>
 <div class="card"><h2>Treasury Curve</h2><table>{curve}</table>
   <p class="spread">2s10s {sp.get('2s10s','?')} · 3m10y {sp.get('3m10y','?')}</p></div>
 <div class="card"><h2>VIX</h2><p class="spread">{d.get('vix','[n/a]')}</p>
   {f'<table>{cboe_rows}</table><p class="as-of">term structure: {html.escape(cboe_tilt)}</p>' if cboe_rows
     else '<p class="blocked">VIX term structure / put-call via CBOE — [blocked here; fills on local/Actions run]</p>'}</div>
 <div class="card"><h2>Big Macro Events (7d)</h2><table>{cal or _row(['(none)'])}</table></div>
 <div class="card"><h2>Top Gainers</h2><table>{gainers}</table></div>
 <div class="card"><h2>Top Losers</h2><table>{losers}</table></div>
 <div class="card"><h2>CFTC Positioning</h2><table>{cftc or _row(['(n/a)'])}</table></div>
 <div class="card"><h2>Credit / Leading (FRED)</h2><table>{fred or _row(['[blocked: FRED]'])}</table></div>
</main></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="dist")
    a = ap.parse_args()
    data = collect()
    sys.path.insert(0, os.path.dirname(__file__))
    import check_alerts
    alerts = check_alerts.evaluate(data)
    data["alerts"] = alerts
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "data.json"), "w") as f:
        json.dump(data, f, indent=2, default=str)
    with open(os.path.join(a.out, "index.html"), "w") as f:
        f.write(render_html(data, alerts))
    print(f"Wrote {a.out}/index.html and data.json · {len(alerts)} alert(s)")
    for al in alerts:
        print(f"  [{al['level']}] {al['msg']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
