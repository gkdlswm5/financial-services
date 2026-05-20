# Sector Idea Generation — May 2026

**Frame:** Adapted `idea-generation` skill — top-down sector ranking rather than single-stock screen.
**Defaults applied (override if wrong):**
- Direction: long-only
- Market cap: all caps (sector-level)
- Geography: US (S&P 500 GICS sectors)
- Style: quality + growth bias, valuation-aware
- Theme: none constrained — let the screen surface it

**As of:** May 2026
**Source stub:** Every figure marked `[E]` requires sourcing against FactSet/Bloomberg/sell-side consensus before external use.

---

## Step 1 — Screening framework

Sectors ranked across five dimensions, each scored 1-5 (5 = best):

| Dimension | What it measures | Why it matters |
|---|---|---|
| **Earnings revisions** | Trailing 3-mo upward EPS revisions ratio | Most reliable single predictor of sector outperformance |
| **Valuation vs. own history** | Forward P/E vs. 10-yr median | Catches sectors at attractive entry points |
| **Secular driver strength** | Qualitative — how durable the multi-year tailwind | Separates cyclical bounces from structural rerates |
| **Forward growth** | Consensus FY1 + FY2 EPS growth | The "what you're getting" |
| **Crowding / positioning** | Investor positioning vs. history; sell-side ratings; flows | Avoids consensus-long traps |

Composite score = simple average; ties broken by Secular driver strength.

---

## Step 2 — Sector scorecard (11 GICS sectors)

| Sector | Earnings revisions | Valuation vs. history | Secular driver | Forward growth | Crowding (lower = better) | **Composite** | Verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| **Utilities (power-gen tilt)** | 5 | 3 | 5 (AI power demand) | 4 | 4 | **4.2** | **#1 — buy** |
| **Industrials** | 4 | 3 | 5 (reshoring + defense + infra) | 4 | 4 | **4.0** | **#2 — buy** |
| **Financials** | 4 | 4 | 3 (capital markets recovery) | 4 | 4 | **3.8** | **#3 — buy** |
| **Health Care** | 3 | 5 (cheapest sector) | 4 (GLP-1 next gen + biotech recovery) | 3 | 5 | **4.0** | **#2 tie — buy** |
| **Communication Services** | 4 | 3 | 4 (AI monetization at META, GOOGL) | 4 | 2 | 3.4 | Hold |
| **Information Technology** | 3 | 1 (priciest sector) | 5 (AI infra) | 4 | 1 (most crowded) | 2.8 | Hold / trim |
| **Consumer Discretionary** | 3 | 3 | 3 (mixed) | 3 | 3 | 3.0 | Hold |
| **Energy** | 3 | 4 | 3 (AI power demand for gas + nuclear; offset by EV trend) | 3 | 4 | 3.4 | Hold |
| **Materials** | 2 | 3 | 3 (copper for electrification; offset by China) | 3 | 4 | 3.0 | Hold |
| **Consumer Staples** | 2 | 3 | 1 (no driver) | 2 | 3 | 2.2 | Underweight |
| **Real Estate** | 3 | 4 | 2 (rate relief offset by office) | 2 | 5 | 3.2 | Hold |

**Composite top 3:**
1. **Utilities** — 4.2
2. **Industrials** — 4.0 (tied with Health Care)
3. **Health Care** — 4.0

---

## Step 3 — Thematic sweep behind the top 3

### #1 — Utilities (power-gen tilt)

**Thesis.** AI data center power demand is the most underwritten structural change in the US power market in 40 years. Hyperscaler capex is now a meaningful driver of utility load growth — Dominion, Constellation, Vistra, NextEra are seeing 5-10% data-center-driven load growth in their service territories vs. historical 0-1% baseline.

**Value chain.**
- **Regulated utilities with data-center load growth** — Dominion (D), Duke (DUK), Southern (SO), American Electric Power (AEP)
- **Independent power producers / merchant generators** — Constellation (CEG, nuclear), Vistra (VST, nuclear + gas), Talen (TLN, nuclear)
- **Natural gas pipelines / midstream** — Williams (WMB), Kinder Morgan (KMI)
- **Nuclear-direct plays** — CEG, VST, TLN; uranium miners (CCJ)
- **Power equipment** — GE Vernova (GEV), Eaton (ETN), Quanta Services (PWR)

**What the market is missing.** Re-rating has happened in the merchant generators (CEG, VST up 200%+ in 12 months) but the regulated utilities trade at modest premiums to history despite a fundamentally changed growth profile. The arbitrage is in regulated names with constructive regulatory bodies (D, DUK, AEP) where data-center contracts are getting approved.

**Pure-play vs. diversified.** CEG and VST are the cleanest pure plays; D and AEP are the regulated-utility leveraged plays; GEV is the picks-and-shovels.

**Already priced in?** Merchant generators yes; regulated utilities partially; power equipment varies.

### #2 — Industrials

**Thesis.** Three durable tailwinds simultaneously: (1) reshoring + onshoring capex, (2) defense budget expansion globally, (3) infrastructure spending tail from CHIPS + IRA + IIJA.

**Value chain.**
- **Defense primes** — LMT, RTX, NOC, GD
- **Aerospace** — BA (recovery), GE (engines), TDG
- **Electrical equipment / automation** — ETN, ROK, EMR, PWR
- **Multi-industrials** — HON, ITW, PH
- **Engineering & construction** — FLR, J, PWR

**What the market is missing.** Aerospace + defense margin recovery (BA turnaround, GE engines, defense backlog conversion) is being underwritten too cautiously. Electrical equipment is benefiting from both reshoring and AI power buildout — double-counted tailwind.

### #3 — Health Care

**Thesis.** Sector trades at the cheapest valuation vs. broader market since 2009 [E]. Three sub-stories:
1. **GLP-1 next generation** — oral GLP-1, dual-agonists, triple-agonists from LLY, NVO, AMGN, VKTX
2. **Biotech recovery** — XBI was beaten down in 2022-2024; rate cuts + return of M&A
3. **MedTech recovery** — procedure volume strength, ISRG, BSX, MDT

**Value chain.**
- **Pharma** — LLY, NVO, MRK, JNJ
- **Biotech large-cap** — VRTX, REGN, AMGN
- **Biotech small/mid** — VKTX, MDGL, IONS, RNA
- **MedTech** — ISRG, BSX, DXCM
- **Health insurers** — UNH (cheaper post-DOJ overhang), ELV
- **CRO / services** — IQV, ICLR

**What the market is missing.** The biotech XBI rally is early; large-cap pharma trades cheaply due to LOE concerns that may be over-priced given pipeline depth. UNH at trough multiple if DOJ investigation resolves benignly.

---

## Step 4 — Per-sector idea presentation

### Utilities — top 3 names to research first

**Constellation Energy (CEG) — LONG**

| Metric | Value [E] |
|---|---|
| Market cap | ~$80B |
| EV/EBITDA NTM | ~16x |
| P/E NTM | ~30x |
| Revenue growth FY25 | +10% [E] |
| EBITDA margin | ~30% |
| FCF yield | ~3% |

**Thesis.**
- Largest US nuclear fleet — 22 GW of carbon-free baseload
- AI hyperscaler PPA structure (Microsoft Three Mile Island restart at premium pricing) sets a new pricing precedent
- Nuclear PTC under IRA creates floor pricing for legacy plants
- Capacity prices in PJM have re-rated dramatically (>9x in last auction)

**Key risks.** Multiple is now demanding; further re-rating requires continued AI demand validation. Outage risk on a single large unit can hit a quarter.

**Suggested next steps.** Full model build; PJM capacity auction tracker; hyperscaler PPA pipeline diligence.

**Dominion Energy (D) — LONG**

| Metric | Value [E] |
|---|---|
| Market cap | ~$50B |
| EV/EBITDA NTM | ~13x |
| P/E NTM | ~18x |
| EPS growth FY25 | +6-8% [E] |
| Dividend yield | ~5% |

**Thesis.**
- Virginia data-center alley — largest concentration of hyperscaler data centers in the world (Loudoun County)
- Load growth forecast revised to ~5%+ from historical ~1% — multi-year regulated capex expansion
- Constructive Virginia State Corporation Commission

**Key risks.** Regulatory lag; capex execution; rate-case outcomes.

**GE Vernova (GEV) — LONG**

| Metric | Value [E] |
|---|---|
| Market cap | ~$80B |
| EV/EBITDA NTM | ~22x |
| Revenue growth FY25 | +8-10% [E] |
| FCF inflection | Significant FCF acceleration FY26-27 |

**Thesis.**
- Gas turbine backlog at all-time highs; pricing power
- Grid equipment (transformers, switchgear) backlogs >2 years
- Wind margins improving as Vineyard losses anniversary

**Key risks.** Wind segment still margin-dilutive; nuclear / SMR ramp slower than backlog suggests.

---

### Industrials — top 3 names to research first

**Eaton (ETN) — LONG.** Double tailwind (reshoring + AI power buildout); electrical equipment backlog growing; FY25 EPS growth ~13% [E].

**GE Aerospace (GE) — LONG.** Commercial engines aftermarket dominance; LEAP installed base ramp drives margin and cash; defense optionality.

**Quanta Services (PWR) — LONG.** Grid construction + renewables build; multi-year backlog; insulated from cyclicality by regulated-utility customer base.

---

### Health Care — top 3 names to research first

**Eli Lilly (LLY) — LONG.** GLP-1 leadership + oral GLP-1 (orforglipron) pipeline + Alzheimer's (donanemab) optionality. Premium multiple but justified given pipeline.

**Vertex Pharmaceuticals (VRTX) — LONG.** Diversification beyond CF — Vanzacaftor; suzetrigine (non-opioid pain); inaxaplin (kidney). Cheapest large-cap biotech relative to pipeline.

**Boston Scientific (BSX) — LONG.** WATCHMAN + Farapulse driving procedure volume; cleanest large-cap MedTech growth story; mid-teens EPS growth at premium-but-defensible multiple.

---

## Step 5 — Prioritized research order

| Priority | Sector | Top idea | Why first |
|---|---|---|---|
| 1 | **Utilities (power-gen)** | CEG / D / GEV | Highest composite score; clearest secular thesis; do sector-overview first |
| 2 | **Industrials** | ETN / GE / PWR | Diversified tailwinds; less crowded than utilities |
| 3 | **Health Care** | LLY / VRTX / BSX | Cheapest sector; multiple sub-stories with different cycle timing |

**Next action.** Run `sector-overview` on **Utilities** (the #1 ranked sector). See `analysis/utilities-sector-overview.md`.

---

## Important notes (per skill)

- Screens surface candidates, not conclusions — every name above needs full fundamental work before sizing
- The Utilities re-rating in merchant names has happened — incremental alpha is in regulated names and picks-and-shovels (GEV, ETN, PWR)
- Avoid crowding traps in semis/IT — that sector scored 2.8 here despite great fundamentals because it's the most crowded long in the market
- Contrarian idea (Health Care) needs catalyst — biotech XBI uptrend + biotech M&A pickup are the visible catalysts
- Source every `[E]` from FactSet / Bloomberg / sell-side consensus before this leaves the room
