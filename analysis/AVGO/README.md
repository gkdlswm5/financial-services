# Broadcom Inc. (AVGO) — Competitive Analysis, Comps & DCF Valuation

Full institutional-style investment workup for Broadcom (NASDAQ: AVGO),
produced using **seven** skills from `plugins/vertical-plugins/financial-analysis/skills/`:
`deep-research` · `competitive-analysis` · `comps-analysis` · `3-statement-model` ·
`dcf-model` · `audit-xls` · `ib-check-deck`.

This is the deepest of the three example workups in `analysis/` — MP and WMT are
landscape + comps; AVGO adds an integrated 3-statement model, a DCF, and a QA pass.

## Files

| File | Built by | What it is |
|---|---|---|
| **`AVGO-Competitive-Analysis.pptx`** | `build_deck.py` | 20-slide deck: thesis → market → segment split → profile → moats → peer set → 2×2 → peer deep dives → VMware/ORCL → scoreboard → **comps football field** → **DCF + sensitivity** → synthesis → bull/base/bear → decision |
| **`AVGO-Model.xlsx`** | `build_model.py` | Integrated **3-statement model + DCF**: Drivers · Income Statement · Balance Sheet · Cash Flow · DCF (5×5 WACC×g sensitivity) · Notes. 267 live formulas, validated 0 errors. |
| **`AVGO-Comps-Analysis.xlsx`** | `build_comps.py` | Peer comps: Inputs · Operating Metrics · Valuation · Growth & AI Exposure · Notes. Stats over the 5 semis peers; ORCL as software-anchor memo. |
| **`AVGO-Competitive-Analysis.html`** | `build_html_view.py` | Tablet-friendly single-file view of all 20 sections (charts embedded base64). |
| `verify_model.py` | — | Independent Python recomputation of the model (cross-check; LibreOffice recalc unavailable in sandbox). |
| `build_*.py` | — | Reproducible build scripts. Edit `INPUTS` / `Drivers` and re-run. |
| `charts/` | matplotlib | AI-revenue ramp, positioning 2×2, valuation football field. |

## Peer set (second framing: semis cohort + software anchor)

| Role | Ticker |
|---|---|
| Target | AVGO |
| Closest competitor (custom silicon) | MRVL |
| Merchant-GPU benchmarks | NVDA, AMD |
| Mature-semi capital-return refs | QCOM, TXN |
| Software anchor for VMware ~40% (memo) | ORCL |

Comps statistics are computed over the **5 semis peers only** (NVDA, AMD, MRVL,
QCOM, TXN). AVGO is the target; ORCL is a memo row (you don't median a software
multiple into a semis set).

## Headline finding

> **At ~$460 the market prices the bull AI ramp.** Our base-case DCF — which
> *haircuts* management's "line of sight to $100B+ AI revenue in FY2027" by ~24%
> (to ~$76B) for execution / OpenAI-financing risk — yields **~$246/share**. The
> **entire** WACC×terminal-growth sensitivity grid ($185–$289) sits below the
> market price; even the most generous corner (WACC 8.5% / g 4.5%) is ~$367 on
> base FCF. To justify $460 you need management's full AI guidance delivered
> *and* a low discount rate (the bull case ≈ $470–520).

High-quality compounder; no margin of safety at the current price.

## Model key assumptions (base case)

- Revenue built by segment: AI semis $48B→$131B (FY26E→FY30E), non-AI semis, software.
- GAAP operating margin 44%→51% (VMware intangible amortization rolling off); D&A 12%→6% of revenue.
- WACC **9.50%** (rf 4.3%, ERP 5.0%, beta 1.07, ~97% equity weight); terminal growth 3.5%.
- Capex ~2.5% of revenue (fabless); cash tax ~14–15%.
- **Yellow flag (disclosed):** terminal value is ~79% of enterprise value — valuation is highly WACC/g-sensitive.

## QA performed

- **`audit-xls`** (model scope): 0 broken cross-sheet links, BS balances, unlevered FCF excludes interest, TV discounted, sensitivity center cell = base case ($246). `validate_dcf.py`: PASS, 0 formula errors over 267 formulas.
- **`ib-check-deck`**: number-consistency check — repeated AVGO metrics tie out across slides; no genuine conflicts (the script's category-bucket flags are cross-metric false positives). All slide titles fit without overflow.

## Data sources & gaps

**Used** (via `deep-research`, ~June 2026): AVGO Q1 FY26 8-K/IR and FY2023–25 SEC
filings; latest 10-Q/IR for NVDA, AMD, MRVL, QCOM, TXN, ORCL; StockAnalysis.com,
GuruFocus, Macrotrends, companiesmarketcap for market data; CNBC, The Information,
Goldman Sachs, Dell'Oro, Allianz, Gartner for AI-capex and customer detail.

**Not used / caveats:**
- **MCP terminal connectors** (CapIQ/FactSet/Daloopa) were not configured in this
  environment; public sources substituted and flagged `[E]` in cell comments.
- **AI vs non-AI semiconductor split** is partly estimated — AVGO reports a single
  Semiconductor segment.
- **Walmart Connect-style disclosure gap:** several customer figures (Anthropic ~$21B,
  OpenAI ~10GW, Apple "Baltra") are reported/rumored, not all company-confirmed.
- **Market caps were volatile May–June 2026** (ORCL ranged ~$550B–$718B); a single
  valuation date (~June 1, 2026) was used — re-pull on one date before finalizing.

## Reproducing / refreshing

```bash
cd analysis/AVGO
pip install openpyxl python-pptx matplotlib
python3 build_model.py        # → AVGO-Model.xlsx
python3 verify_model.py       # prints the base-case DCF cross-check
python3 build_comps.py        # → AVGO-Comps-Analysis.xlsx
python3 build_deck.py         # → AVGO-Competitive-Analysis.pptx + charts/
python3 build_html_view.py    # → AVGO-Competitive-Analysis.html
```

## Caveats

- Research and decision-framing only — **not investment advice**.
- Cross-check valuation against a primary terminal before any binding decision.
- The DCF is GAAP-based (conservative); AVGO's non-GAAP operating margin (~66%)
  and adjusted EBITDA margin (~68%) are materially higher.
- `[E]` estimates are marked in Excel cell comments; review before use.
