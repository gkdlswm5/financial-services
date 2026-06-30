# Market Intelligence Dashboard (hosted)

A static, auto-refreshed dashboard published to **GitHub Pages** by
`.github/workflows/market-dashboard.yml`. This is the "Level 2" hosting path: on-demand
skills render in your Claude session; this gives you an always-available page you can
bookmark, regenerated on a schedule.

## Why host it in Actions (not the Claude sandbox)

The Claude cloud session's egress policy **blocks FRED and CBOE** (403 at the proxy). A
GitHub-hosted runner has open internet, so running the same adapters here **also unblocks**
credit spreads, leading indicators, and the VIX term structure — cells that show
`[blocked]` in-session populate on the hosted page.

## One-time setup (manual — needs repo admin)

1. **Add the FMP key as a secret:**
   Settings → Secrets and variables → Actions → New repository secret →
   name `FMP_API_KEY`, value = your FMP premium key.
2. **Enable Pages from Actions:**
   Settings → Pages → Build and deployment → Source → **GitHub Actions**.
3. (Optional) create a `market-alert` label so the alert issues are tagged.

After that the workflow runs weekdays at 13:00 UTC (and on manual *Run workflow*), and the
dashboard is published at `https://<you>.github.io/<repo>/`.

## What it shows

Treasury curve + 2s10s/3m10y spreads · VIX · big macro events (7d) · top gainers/losers ·
CFTC positioning · credit & leading indicators (FRED). An **alert banner** surfaces
threshold breaches (curve inversion, VIX spike, credit stress, big drops); **critical**
alerts also open a GitHub issue.

## Pieces

| File | Role |
|---|---|
| `build_dashboard.py` | Orchestrates the adapters → `dist/index.html` + `dist/data.json` |
| `check_alerts.py` | Threshold rules (importable + `--selftest`) |
| `../skills/*/scripts/fetch_*.py` | The per-source adapters (FMP, macro, CFTC, FRED, CBOE) |

## Run it locally

```bash
export FMP_API_KEY=...   # from your .env
python3 plugins/vertical-plugins/stonks/dashboard/build_dashboard.py --out dist
open dist/index.html
```

Locally, FRED/CBOE are reachable too — so a local run is fully populated, same as Actions.
