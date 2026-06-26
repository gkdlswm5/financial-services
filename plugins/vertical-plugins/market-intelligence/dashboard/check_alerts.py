#!/usr/bin/env python3
"""
check_alerts.py — threshold rules over the combined market dashboard data.

Pure function `evaluate(data) -> [alerts]` so it's importable by build_dashboard.py and
runnable standalone (--selftest). Rules are intentionally conservative and institutional:
yield-curve inversion, vol spikes, credit-spread stress, and big single-name moves.

An alert = {"level": "critical|warning|info", "msg": "..."}.
"""
import json, sys


def _num(x):
    return x if isinstance(x, (int, float)) else None


def evaluate(d):
    alerts = []
    sp = d.get("spreads", {})
    s3m10 = _num(sp.get("3m10y"))
    s2_10 = _num(sp.get("2s10s"))
    if s3m10 is not None and s3m10 < 0:
        alerts.append({"level": "critical", "msg": f"Yield curve INVERTED (3m10y {s3m10:+.2f}) — recession watch"})
    if s2_10 is not None and s2_10 < 0:
        alerts.append({"level": "warning", "msg": f"2s10s inverted ({s2_10:+.2f})"})

    vix = _num(d.get("vix"))
    if vix is not None:
        if vix >= 35:
            alerts.append({"level": "critical", "msg": f"VIX spiking ({vix:.1f}) — acute stress"})
        elif vix >= 25:
            alerts.append({"level": "warning", "msg": f"VIX elevated ({vix:.1f})"})

    hy = (d.get("fred", {}) or {}).get("HY OAS (credit)", {})
    hy = _num(hy.get("value")) if isinstance(hy, dict) else None
    if hy is not None and hy >= 5.0:
        alerts.append({"level": "warning", "msg": f"Credit stress: HY OAS {hy:.2f}% (>500bp)"})

    for m in (d.get("movers", {}) or {}).get("biggest-losers", [])[:3]:
        pct = _num(m.get("changesPercentage", m.get("changePercentage")))
        if pct is not None and pct <= -20:
            alerts.append({"level": "info", "msg": f"Big drop: {m.get('symbol')} {pct:.1f}%"})

    # surprise on a high-impact event that already printed
    for ev in (d.get("calendar", []) or []):
        if ev.get("impact") == "High" and ev.get("actual") not in (None, "") and ev.get("estimate") not in (None, ""):
            try:
                a, e = float(ev["actual"]), float(ev["estimate"])
                if e != 0 and abs(a - e) / abs(e) > 0.15:
                    alerts.append({"level": "info", "msg": f"Surprise: {ev.get('event','')[:40]} actual {a} vs est {e}"})
            except (ValueError, TypeError):
                pass
    return alerts


def selftest():
    data = {"spreads": {"3m10y": -0.20, "2s10s": 0.10}, "vix": 27.5,
            "fred": {"HY OAS (credit)": {"value": 5.4}},
            "movers": {"biggest-losers": [{"symbol": "XYZ", "changesPercentage": -24.0}]},
            "calendar": []}
    alerts = evaluate(data)
    for a in alerts:
        print(f"  [{a['level']}] {a['msg']}")
    levels = {a["level"] for a in alerts}
    assert "critical" in levels and "warning" in levels and "info" in levels
    assert len(alerts) == 4
    print("  PASS — curve/vix/credit/mover rules all fired.")
    return 0


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(selftest())
    print(json.dumps(evaluate(json.load(sys.stdin)), indent=2))
