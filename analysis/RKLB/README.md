# Rocket Lab USA (RKLB) — Competitive Analysis, Comps & DCF Valuation

Full 7-skill institutional workup, **small-cap-growth adaptation** per user
scope. Same shape as `analysis/AVGO/` and `analysis/GOOG/`, with EV/Revenue
emphasized over EBITDA-based multiples (cohort is largely pre-profit).
Skills: `deep-research` · `competitive-analysis` · `comps-analysis` ·
`3-statement-model` · `dcf-model` · `audit-xls` · `ib-check-deck`.

**Headline finding (stark):** base-case DCF **$9.35/share** vs **$123.32**
market = **−92%**. Even the most generous DCF corner (WACC 11% / g 4.5%) = $14.
This is not a quirky result — analyst consensus PT is **$103.91 (16% below
spot)**, and the only valuation lens that gets close to the current price is
the SpaceX-comp EV/Revenue benchmark (~$104). At $123 you're paying for
SpaceX-lite terminal-state execution (~10%+ growth through 2040+).

## Files

| File | Built by | What it is |
|---|---|---|
| **`RKLB-Competitive-Analysis.pptx`** | `build_deck.py` | 14-slide deck: thesis → market → profile → Neutron ramp chart → EV/Rev chart → peer deep dive → valuation football field → DCF + sensitivity → bull/base/bear → decision frame → risks → sources |
| **`RKLB-Model.xlsx`** | `build_model.py` | Integrated **3-statement model + DCF**: Drivers (Launch + Space Systems + capacity build) · IS · BS · CF · DCF (5×5 WACC×g sensitivity with wider 11-15% bands) · Notes. 225 live formulas, validated 0 errors. |
| **`RKLB-Comps-Analysis.xlsx`** | `build_comps.py` | Peer comps: Inputs · Valuation (EV/Rev focus) · Capacity · Notes. ASTS, PL, IRDM, RDW + LMT (old-space anchor) + SpaceX (private memo). |
| `verify_model.py` | — | Independent recompute of base-case DCF. |
| `charts/` | matplotlib | Neutron launch cadence ramp; EV/Revenue peer comparison. |

## Peer set

| Role | Ticker / Name |
|---|---|
| Target | RKLB |
| Public pure-play space peers | ASTS (direct-to-cell), PL (Earth obs), IRDM (mature satcom), RDW (space infra) |
| Old-space anchor (memo) | LMT (Space segment) |
| Private benchmark (memo) | SpaceX (S-1 filed April 2026; ~$1.75T IPO target) |

## Model key assumptions (base case)

- **Revenue**: $602M (FY25 actual) → $870M (FY26E) → $1.65B (FY27E, first Neutron commercial year) → $4.95B (FY31E)
- **Neutron cadence**: Q4 2026 NET first launch (expendable); 5 in FY27 → 18-20/yr at mature cadence by FY30+
- **Op margin**: -38% (FY25) → -20% (FY26) → -5% (FY27) → +5% (FY28, first profitable year) → +15% (FY31)
- **WACC 13.30%** (rf 4.3%, ERP 5.0%, beta 1.8, ~100% equity weight); **terminal g 3.5%** (space secular tailwind)
- **TV is ~86% of EV** — model is structurally bearish for story stocks; the gap to market is the SpaceX-lite optionality beyond FY31

## QA performed

- **`audit-xls`** (model scope): 225 formulas, 0 errors. Sensitivity grid wider (WACC 11-15%) than mega-caps to reflect small-cap risk.
- **`ib-check-deck`**: 14 slides, all titles fit. Metrics tie across slides.

## Data sources & gaps

- **Used** (~June 1-3, 2026 via `deep-research`): RKLB Q1 CY26 10-Q (May 7, 2026), FY25 10-K (Feb 2026), IR press releases (Mynaric close April 14, 2026; mystery-customer 8-launch deal May 7, 2026); Spaceflight Now / SpaceNews coverage of Neutron timeline; peer Q1 26 8-Ks (ASTS, PL, IRDM, RDW); SpaceX S-1 (April 2026) + Bloomberg/Reuters; LMT Space segment FY25 results.
- **MCP terminals NOT configured** — all data from public sources, `[E]`-flagged where derived.
- **Neutron pricing / cadence are management commentary**, not contracts — heavily execution-dependent.
- **Mynaric NOT MDA Space** — confusing similar names; the 2026 acquisition was Mynaric (laser optical comms).
- **HTML view not built** for RKLB (deck + workbooks are the primary deliverables).

## Reproducing

```bash
cd analysis/RKLB
pip install openpyxl python-pptx matplotlib
python3 build_model.py
python3 verify_model.py
python3 build_comps.py
python3 build_deck.py
```

## Caveats

- Research and decision-framing only — **not investment advice**.
- RKLB is a high-volatility small-cap; intraday price moves of 5-15% are common; refresh price before using.
- The DCF result ($9 vs $123) looks extreme but is corroborated by the Street (consensus PT $104).
- The only valuation framework that justifies $123 is SpaceX-comp EV/Revenue — and SpaceX itself is private and unproven as a public-market multiple.
