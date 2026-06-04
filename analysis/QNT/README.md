# Quantinuum Inc. (NASDAQ: QNT) — Competitive Analysis, Comps & Dual-DCF Valuation

Pre-IPO / IPO-day investment workup for Quantinuum (NASDAQ: QNT), produced
using the financial-analysis skill stack from `plugins/vertical-plugins/financial-analysis/skills/`:
`deep-research` · `competitive-analysis` · `comps-analysis` · `3-statement-model` ·
`dcf-model` · `audit-xls` · `ib-check-deck`.

QNT priced its IPO on **June 3, 2026 at $60/share** (above the $53-55 filed range,
upsized to 28M shares, ~20× oversubscribed, $1.68B gross). First trade June 4
opened at **$68.00**. This analysis is anchored on the $68 trading price.

## Files

| File | Built by | What it is |
|---|---|---|
| **`QNT-Model.xlsx`** | `build_model.py` | Integrated 3-statement model + **dual DCF**: Drivers · Income Statement · Balance Sheet · Cash Flow · DCF (traditional intrinsic + reverse-engineered at $68) · Sensitivity (5×5 WACC×g) · Notes. 12-year horizon (FY24A → FY35E) reflecting pre-profit / pre-FTQC optionality. |
| **`QNT-Comps-Analysis.xlsx`** | `build_comps.py` | Peer comps: Inputs · Operating Metrics · Valuation · Tech & Growth · Notes. 3 public quantum pure-plays (IONQ, RGTI, QBTS) + HON memo column for parent attribution. |
| **`QNT-Competitive-Analysis.pptx`** | `build_deck.py` | 16-slide deck: thesis → IPO event → profile + HON parent → TAM → modality 2×2 → peer set → IONQ deep-dive → RGTI/QBTS → tech scoreboard → RIKEN cliff → revenue build → football field → dual DCF → bull/base/bear → decision + HON SOTP |
| **`QNT-Competitive-Analysis.html`** | `build_html_view.py` | Tablet-friendly single-file view of all 12 sections (charts embedded base64). |
| `verify_model.py` | — | Independent Python recomputation of the dual DCF (cross-check). |
| `build_*.py` | — | Reproducible build scripts. Edit `INPUTS` / `Drivers` and re-run. |
| `charts/` | matplotlib | Revenue ramp · football field · modality 2×2 · TAM · RIKEN cliff. |

## Peer set

| Role | Ticker | Modality |
|---|---|---|
| Target | QNT | Trapped-ion (Helios) |
| Direct technology comp | IONQ | Trapped-ion (Forte/Tempo) |
| Superconducting | RGTI | Superconducting (Cepheus-108Q) |
| Specialty | QBTS | Quantum annealing (Advantage2) |
| Parent (memo) | HON | Multi-industrial conglomerate (~48% post-IPO voting) |

Comps statistics computed over the 3 public quantum pure-plays.
HON is a memo column — included for SOTP attribution analysis, not as a valuation comp.

## Headline finding

> **At $68, QNT priced full optionality.** Our traditional DCF — 15.85% WACC,
> 12-year horizon, FCF crossover in FY2029E (the Apollo year) — yields **~$25/share**
> (current at +175% premium). Our reverse-engineered DCF says **$68 requires FY35E
> revenue of $7.7B**, which is **134% above our base-case $3.3B** and implies a
> **15.4% share of McKinsey's $50B 2035 QC TAM** — requiring a ~75% 10-yr revenue CAGR.

That's not impossible — Apollo (the 2029 fault-tolerant universal QC target) could justify it.
But the asymmetry skews DOWN at $68. **Decision call: HOLD with downside skew.** Buy zone <$45.

## Dual DCF (base case)

**Framework 1 — Traditional DCF:**

| Line | Value |
|---|---|
| WACC | 15.85% |
| Terminal growth | 4.0% |
| Sum PV(FCF) FY26E-FY35E | $1,372M |
| PV of terminal value | $2,835M |
| Enterprise value | $4,207M |
| Equity value | $6,287M |
| **Implied price** | **$24.76** |
| Current price | $68.00 |
| **Premium to intrinsic** | **+175%** |

**Framework 2 — Reverse-engineered to $68:**

| Line | Value |
|---|---|
| EV today | $15,185M |
| Assumed FY35 EV/Rev (mature) | 8.0× |
| **Implied FY35E revenue** | **$7,680M** |
| Model FY35E revenue | $3,280M |
| **Gap** | **+134%** |
| Implied 2035 QC TAM share | 15.4% |
| Required 10-yr CAGR | ~75% |

## Honeywell parent angle

- HON owns ~48.1% post-IPO voting power; ~$7.5B stake at $68/share
- HON market cap ~$138B → QNT = **~5.4% of HON value**
- Modest catalyst for HON shareholders; **not transformative**
- HON SOTP build adds ~$5/share (~2.4%) to HON NAV
- **Cross-trade idea:** for investors who want quantum optionality but
  are price-sensitive at $68, HON offers indirect QNT exposure at a
  much lower multiple plus stable cash flow + dividend.

## Data sources & gaps

**Used** (via `deep-research`, ~June 2026): SEC EDGAR S-1/A; IONQ/RGTI/QBTS
10-Q filings; company press releases (Quantinuum, Honeywell); CNBC, Bloomberg,
Reuters, MIT Tech Review, HPCwire, Quantum Insider; McKinsey QTM 2026 and BCG
quantum reports for TAM; Wikipedia for funding history.

**Not used / caveats:**
- **MCP terminal connectors** (CapIQ/FactSet/Daloopa) were not configured;
  public sources substituted and flagged `[E]` in cell comments.
- **IBM ownership %** in QNT not corroborated in S-1 summaries reviewed
  (premise had ~6% — only Cambridge Quantum Holdings 32.5% aggregate is documented).
- **Gross margin** not broken out in S-1 — modeled by analogy to IONQ/RGTI.
- **Stock-based comp share of R&D** estimated from public quantum peers (~50% early).
- **Pre-money valuations** for prior funding rounds confirmed; round dates
  may shift by a quarter in some secondary sources.

## QA performed

- **`audit-xls` (model scope):** 0 broken cross-sheet links; BS balances;
  dual-DCF center cell of sensitivity = base case ($24.76); `verify_model.py`
  independently recomputes the same $24.76 intrinsic.
- **`ib-check-deck`:** number-consistency check — repeated QNT metrics tie
  out across slides; no genuine conflicts. All slide titles fit without overflow.

## Refresh checklist (post-IPO Q2'26 print)

1. Update DCF anchor: current trading price cell on DCF sheet
2. If Helios ramp guidance changes, refresh Helios revenue track in Drivers
3. If management commits to a profitability date, tighten WACC / beta
4. Refresh peer Q2 2026 data (IONQ, RGTI, QBTS) for live comps
5. If Honeywell secondaries get announced, model the lockup/overhang impact

## Reproducing / refreshing

```bash
cd analysis/QNT
pip install openpyxl python-pptx matplotlib
python3 build_model.py        # → QNT-Model.xlsx
python3 verify_model.py       # prints the base-case dual DCF cross-check
python3 build_comps.py        # → QNT-Comps-Analysis.xlsx
python3 build_deck.py         # → QNT-Competitive-Analysis.pptx + charts/
python3 build_html_view.py    # → QNT-Competitive-Analysis.html
```

## Caveats

- Research and decision-framing only — **not investment advice**.
- Cross-check valuation against a primary terminal before any binding decision.
- The traditional DCF on a pre-profit / pre-FTQC name is *honest but not informative
  in isolation* — that's why we run the dual framework.
- 8.3% public float makes QNT susceptible to high volatility and squeeze-style
  moves; size positions accordingly and accumulate gradually.
- `[E]` estimates are marked in Excel cell comments; review before use.
