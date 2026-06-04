# Alphabet Inc. (GOOG/GOOGL) — Competitive Analysis, Comps & DCF Valuation

Full 7-skill institutional workup. Same shape as `analysis/AVGO/`.
Skills: `deep-research` · `competitive-analysis` · `comps-analysis` ·
`3-statement-model` · `dcf-model` · `audit-xls` · `ib-check-deck`.

**Headline finding:** base-case DCF **$213.45/share** vs **$357.73** market = **−40%**.
The FY26 capex spike ($92B → $185B) crushes Year-1 unlevered FCF to ~$4B; valuation
normalizes by FY28–30. Even the bull WACC/g corner ($334) sits below the current
price; only the *bull* assumption set (Cloud margin >36% by FY28 + faster capex
taper) reaches the $358 zone. Comps say ~$260–380. Net: the market is pricing
successful capex payback; cheap on fwd P/E (~24x) but expensive on intrinsic.

## Files

| File | Built by | What it is |
|---|---|---|
| **`GOOG-Competitive-Analysis.pptx`** | `build_deck.py` | 18-slide deck: thesis → capex chart → segment split → moats → peer set → 2×2 → META + MSFT/AMZN deep dives → scoreboard → valuation football field → DCF + sensitivity → bull/base/bear → decision frame → sources |
| **`GOOG-Model.xlsx`** | `build_model.py` | Integrated **3-statement model + DCF**: Drivers (Services/Cloud/Other Bets + Cloud margin trajectory) · IS · BS · CF · DCF (5×5 WACC×g sensitivity) · Notes. 267 live formulas, validated 0 errors. WACC 9.24%, terminal g 3.0%. |
| **`GOOG-Comps-Analysis.xlsx`** | `build_comps.py` | Peer comps: Inputs · Operating Metrics · Valuation · Notes. Stats over 4 mega-cap peers (META, MSFT, AMZN, NFLX); TTD + RDDT as ads-pure memo. |
| `verify_model.py` | — | Independent recompute of base-case DCF. |
| `charts/` | matplotlib | Capex cycle bar chart, scale × growth 2×2, valuation football field. |

## Peer set

| Role | Ticker |
|---|---|
| Target | GOOG / GOOGL |
| Mega-cap cohort (stat set) | META, MSFT, AMZN, NFLX |
| Ads-pure (memo) | TTD, RDDT |

## Model key assumptions (base case)

- **Revenue**: Services +13–15%/yr (Search + YouTube + Subscriptions); Cloud $58.7B (FY25) → $266B (FY30) — +57% in FY26 tapering; Other Bets stable.
- **Cloud margin**: 24% (FY25) → 30% (FY26E) → 36% (FY30E). Q1 26 actual was 32.9%.
- **Capex**: $92B (FY25) → $185B (FY26 guide midpoint) → tapers to $150B by FY30.
- **D&A**: ramps with 2–3-year lag from capex; reaches ~$100B by FY30.
- **WACC 9.24%** (rf 4.3%, ERP 5.0%, beta 1.0, ~99% equity weight); **terminal g 3.0%**.
- **TV is ~86% of EV** — valuation is extremely WACC/g-sensitive.

## QA performed

- **`audit-xls`** (model scope): 267 formulas, 0 errors, balanced summary BS, unlevered FCF excludes interest, sensitivity center cell = base case ($213).
- **`ib-check-deck`**: 18 slides, all titles fit; metrics tie across slides.

## Data sources & gaps

- **Used** (~June 1–3, 2026 via `deep-research`): Alphabet Q1 CY26 8-K & 10-Q (Apr 2026), FY25 10-K (Feb 2026), FY23/FY24 10-Ks; June 2026 FWP (Berkshire pp + ATM); DOJ Sept 2025 remedies ruling; Anthropic-Google-Broadcom 3.5GW TPU deal (April 2026); Waymo $16B funding (Feb 2026); peer 10-Qs (META, MSFT, AMZN, NFLX, TTD, RDDT); StockAnalysis/Macrotrends/GuruFocus.
- **MCP terminals not configured** — public sources, `[E]`-flagged where derived.
- **Other Bets revenue** is largely Waymo; not broken out separately.
- **HTML view not built** for GOOG (deck + workbooks are the primary deliverables).

## Reproducing

```bash
cd analysis/GOOG
pip install openpyxl python-pptx matplotlib
python3 build_model.py
python3 verify_model.py
python3 build_comps.py
python3 build_deck.py
```

## Caveats

- Research and decision-framing only — **not investment advice**.
- The capex cycle assumption (peaks FY27, tapers FY28+) is the key risk to the model. If Anthropic + sovereign deals demand continued elevated capex, FCF normalization delays and base-case fair value falls further.
- DCF is GAAP-style; reported NI includes Anthropic mark-to-market gains that are not reflected in the model's operating assumptions.
