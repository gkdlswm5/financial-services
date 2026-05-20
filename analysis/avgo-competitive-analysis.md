# Semis + Software: Peer Benchmarking & Investment Scenarios

**Peer set:** NVDA, AMD, MRVL, QCOM, AVGO (silicon) + PANW, NOW, ORCL (infrastructure software)
**As of:** May 2026 | **Period:** Most recent FY / TTM, flagged per row
**Format:** 9-slide markdown draft (per `plugins/agent-plugins/market-researcher/skills/competitive-analysis/SKILL.md`)

> **Draft note — sources required.** Figures below reflect publicly-reported FY24/FY25 results and consensus framing. Every value must be re-verified against 10-Ks, 10-Qs, and earnings releases before this is shared externally. Citations are stubbed as `[Company 10-K FYxx]` where final source links should be inserted.

---

## Slide 1 — Scope: eight peers across silicon and infrastructure software

- **Purpose.** Side-by-side benchmarking, no protagonist, with AVGO scenarios called out in Slide 9.
- **Coverage.** Five silicon names (NVDA, AMD, MRVL, QCOM, AVGO) and three infrastructure-software names (PANW, NOW, ORCL).
- **Why this set.** AVGO is the only true hybrid (silicon + software at scale post-VMware). The semis cohort isolates the silicon comp; the software cohort isolates the infra-software comp. The two halves bracket AVGO from both sides.
- **Period.** Most recent reported FY for each (fiscal year-ends differ — flagged).

Footer: "All figures in USD. Fiscal year-ends: NVDA Jan, AMD Dec, MRVL Jan, QCOM Sep, AVGO Oct, PANW Jul, NOW Dec, ORCL May."

---

## Slide 2 — Market context: AI infra demand is the gravity well

| Market | 2024 size | Growth (CAGR) | Source |
|---|---|---|---|
| Data-center AI accelerators | ~$125B [E] | 35-45% through 2027 [E] | Sell-side consensus; NVDA DC run-rate |
| Networking silicon (custom ASIC + merchant) | ~$25-30B [E] | 20-25% [E] | Industry reports |
| Mobile/handset SoC | ~$30B | Flat to +3% | QCOM 10-K FY24 |
| Cybersecurity platform | ~$200B addressable | 12-14% | PANW investor day FY24 |
| Enterprise workflow / digital ops | ~$220B addressable | 15-18% | NOW investor day 2024 |
| Database + apps + OCI | ~$600B addressable | OCI 50%+; apps 10-12% | ORCL FY25 commentary |

**Takeaway insight (slide title).** "AI accelerator + custom-ASIC TAMs are the only double-digit silicon pockets; software pockets are larger but slower."

---

## Slide 3 — Industry economics: where AVGO sits is structurally rare

**Value-chain framing:**

- **Fabless silicon** — gross margins 45-75% depending on mix (compute > networking > mobile baseband). FCF margin 25-50%. Capital-light but cyclical; tied to hyperscaler / handset capex.
- **Infrastructure software** — gross margins 70-85%. FCF margin 30-40% at scale. Sticky, recurring, expansion-driven.
- **AVGO uniquely spans both** post-VMware: ~58% silicon / ~42% software by FY24 revenue mix [E, confirm against AVGO 10-K FY24]. No other peer in the set has >20% of revenue in the opposite category.

**Takeaway insight (slide title).** "AVGO is the only peer with material revenue on both sides of the silicon/software margin curve."

---

## Slide 4 — Silicon peer profiles (single comparison table)

| Company | FY | Revenue | YoY | Non-GAAP GM | Non-GAAP Op Margin | FCF Margin | Mkt Cap [E] | Key franchise |
|---|---|---:|---:|---:|---:|---:|---:|---|
| NVDA | FY25 (Jan-end) | ~$130.5B | +114% | ~75% | ~62% | ~50% | ~$3.0T | Data-center GPU + CUDA |
| AVGO | FY24 (Oct-end) | ~$51.6B | +44% (incl. VMware) | ~77% | ~62% | ~40% | ~$1.0T+ | Custom AI ASIC + networking + VMware |
| QCOM | FY24 (Sep-end) | ~$39.0B | +9% | ~56% | ~28% | ~22% | ~$190B | Handset SoC + auto + IoT |
| AMD | FY24 (Dec-end) | ~$25.8B | +14% | ~53% | ~22% | ~10% | ~$200B | DC CPU (EPYC) + DC GPU (MI300) |
| MRVL | FY25 (Jan-end) | ~$5.8B | +5% | ~62% | ~30% | ~25% | ~$80B | Custom ASIC + optical DSP |

**Source stub.** Each company's 10-K + most recent earnings release. All non-GAAP figures as reported by management. `[E]` market cap = approximate, point-in-time.

**Takeaway insight (slide title).** "NVDA and AVGO are the only silicon peers with >60% non-GAAP op margin; the rest sit in the 20-30% band."

---

## Slide 5 — Infrastructure-software peer profiles (single comparison table)

| Company | FY | Revenue | YoY | Non-GAAP GM | Non-GAAP Op Margin | FCF Margin | Mkt Cap [E] | Key franchise |
|---|---|---:|---:|---:|---:|---:|---:|---|
| ORCL | FY25 (May-end) | ~$57B | +9% | ~80% | ~45% | ~25% | ~$450B | DB + apps + OCI (AI infra) |
| NOW | FY24 (Dec-end) | ~$11.0B | +22% | ~83% | ~30% | ~31% | ~$200B | Workflow / ITSM + AI agents |
| PANW | FY24 (Jul-end) | ~$8.0B | +16% | ~78% | ~28% | ~38% | ~$130B | Network + cloud + SecOps platforms |
| AVGO software segment | FY24 (Oct-end) | ~$21.8B [E] | n/m (VMware step-up) | ~88% (segment GM) | ~70% (segment op margin) | n/a separately | n/a separately | VMware + Symantec + CA |

**Source stub.** Each company's 10-K + segment disclosures. AVGO software figures from segment reporting in AVGO 10-K FY24.

**Takeaway insight (slide title).** "AVGO's software segment margin profile (~70% op margin) exceeds every standalone software peer in the set."

---

## Slide 6 — Positioning: 2×2 — Growth (YoY rev) × Profitability (FCF margin)

**Axes.**
- **X — YoY revenue growth (FY most recent).** Range: 0% to +115%.
- **Y — FCF margin (FY most recent).** Range: 10% to 55%.

**Plotted (X, Y):**

| Company | X — YoY rev | Y — FCF margin | Quadrant |
|---|---:|---:|---|
| NVDA | +114% | ~50% | Top-right (best) |
| AVGO | +44% | ~40% | Top-right |
| NOW | +22% | ~31% | Upper-mid |
| PANW | +16% | ~38% | Upper-mid |
| AMD | +14% | ~10% | Lower-mid |
| QCOM | +9% | ~22% | Lower-mid |
| ORCL | +9% | ~25% | Lower-mid |
| MRVL | +5% | ~25% | Lower-left |

**Build note (for slide construction).** Real chart object (XY scatter), labels on each bubble, axis titles set explicitly, no overlapping labels. Bubble size = market cap (optional third dimension).

**Takeaway insight (slide title).** "NVDA and AVGO occupy the top-right alone; the rest cluster in a sub-25% growth / 20-40% FCF margin band."

---

## Slide 7 — Comparative scorecard (●●●/●●○/●○○ across 5 dimensions)

Ratings reflect rank within this 8-peer set, not absolute. Values in cell show the actual data driving the rating.

| Dimension | NVDA | AVGO | ORCL | QCOM | AMD | NOW | PANW | MRVL |
|---|---|---|---|---|---|---|---|---|
| **Scale** (Mkt cap) | ●●● $3.0T | ●●● $1.0T+ | ●●○ $450B | ●●○ $190B | ●●○ $200B | ●●○ $200B | ●○○ $130B | ●○○ $80B |
| **Growth** (YoY rev) | ●●● +114% | ●●● +44% | ●○○ +9% | ●○○ +9% | ●○○ +14% | ●●○ +22% | ●●○ +16% | ●○○ +5% |
| **Margins** (FCF) | ●●● 50% | ●●● 40% | ●●○ 25% | ●●○ 22% | ●○○ 10% | ●●○ 31% | ●●● 38% | ●●○ 25% |
| **Moat** (qual) | ●●● CUDA + DC lock-in | ●●● Custom ASIC + VMware switching cost | ●●○ DB switching cost; OCI emerging | ●●○ Modem IP + Apple risk | ●○○ Open ecosystem, catching up | ●●● Workflow embed | ●●○ Platform consolidation | ●○○ Concentrated customers |
| **Capital return** (buybacks + div) | ●●○ Buybacks expanding | ●●● Dividend + buyback | ●●○ Steady buyback + div | ●●● Heavy buyback + div | ●○○ Limited | ●○○ None | ●○○ None | ●○○ Limited |

**Takeaway insight (slide title).** "NVDA, AVGO lead 3 of 5 dimensions; AVGO is the only peer rated ●●● on Capital return."

---

## Slide 8 — Moat assessment + structural vulnerabilities

| Company | Network effects | Switching costs | Scale economies | Intangibles | Durable advantages | Structural vulnerabilities |
|---|---|---|---|---|---|---|
| **NVDA** | Strong (CUDA dev ecosystem) | Strong (CUDA lock-in, software stack) | Strong (TSMC priority access) | Strong (CUDA IP, brand) | DC GPU monopoly + CUDA moat | Custom ASIC erosion (AVGO/MRVL); hyperscaler in-house silicon |
| **AVGO** | Moderate (VMware ecosystem) | Strong (VMware contractual + ASIC design wins) | Strong (fab capacity, vertical scale) | Strong (IP portfolio, M&A engine) | Custom ASIC franchise + VMware recurring | Customer concentration in AI ASIC (~2-3 hyperscalers); VMware churn risk |
| **ORCL** | Weak | Strong (DB migration cost) | Moderate (OCI scaling) | Strong (DB IP, install base) | DB + cloud DB lock-in; OCI AI tailwind | OCI capex burden; legacy apps decline |
| **QCOM** | Weak | Moderate (modem IP licensing) | Strong (modem scale) | Strong (5G/6G patents) | Modem IP, Apple revenue (declining) | Apple in-house modem; China handset cycle |
| **AMD** | Weak | Weak (open standards) | Moderate (TSMC dependency) | Moderate (CPU IP) | EPYC share gains in DC CPU | GPU gap vs NVDA; CUDA absence |
| **NOW** | Moderate (admin/dev community) | Strong (workflow embed) | Moderate | Strong (platform extensibility) | Workflow stickiness + AI agent layer | Federal exposure; AI cannibalization of seats |
| **PANW** | Weak | Strong (platform consolidation) | Moderate | Strong (security IP) | "Platformization" cross-sell | Decel risk in core firewall; competitive crowd |
| **MRVL** | Weak | Moderate (custom-ASIC design lock-in) | Weak (sub-scale vs AVGO) | Moderate | Optical DSP leadership; custom ASIC #2 | 2-3 customer concentration; AVGO competition |

**Takeaway insight (slide title).** "NVDA and AVGO both score Strong on 3 of 4 moat dimensions; AVGO's hyperscaler ASIC concentration is the principal structural risk."

---

## Slide 9 — Investment scenarios: AVGO bull/base/bear + relative peer ranking

### 9a — AVGO scenarios

| Scenario | Probability | Key drivers | Quantified signposts (12-18 mo) |
|---|---:|---|---|
| **Bull** | 35% | AI ASIC ramps to 3rd hyperscaler; VMware revenue retention >95%; AI revenue >$25B FY25 [E] | AI segment >$8B per quarter exit FY25; VMware ARR re-acceleration; non-GAAP op margin >65% |
| **Base** | 50% | AI ASIC stays with 2 hyperscalers; VMware churn in line with plan; AI revenue ~$18-22B FY25 [E] | AI segment $5-7B per quarter; non-GAAP op margin 60-62%; FCF margin holds ~40% |
| **Bear** | 15% | Hyperscaler insources ASIC; VMware churn accelerates; AI revenue <$15B FY25 | AI segment <$4B per quarter; VMware billings decline; non-GAAP op margin <58% |

Signposts are deck-defining: every scenario must be **falsifiable within 12-18 months** with a public data point.

### 9b — Relative pick order across the 8 peers

| Rank | Company | Thesis in one line |
|---|---|---|
| 1 | NVDA | Still the AI compute monopolist; CUDA moat intact; growth and margin both at the frontier |
| 2 | AVGO | Only peer with two ●●● columns + ●●● capital return; bull/base both reward holders |
| 3 | NOW | Cleanest software compounder with AI agent optionality; no semis cyclicality |
| 4 | PANW | Best margin profile in software peer set; platformization is working |
| 5 | ORCL | OCI optionality at a lower multiple; DB lock-in is real |
| 6 | QCOM | Cheapest semis name; Apple modem loss already in the print |
| 7 | AMD | DC CPU share story is real; GPU vs NVDA is the elephant in the room |
| 8 | MRVL | Best leveraged optical/DSP play but sub-scale vs AVGO in ASIC |

**Takeaway insight (slide title).** "Base case ranks AVGO #2 behind NVDA; bear case repositions it below NOW and PANW on moat resilience."

---

## Appendix — quality checklist (per skill)

**Prompt fidelity**
- [x] All 8 peers represented on every comparison slide
- [x] 2×2 matrix (not radar) per user selection
- [x] Markdown draft (not .pptx) per user selection
- [x] AVGO scenarios + peer ranking on Slide 9 per user selection

**Data consistency**
- [ ] **Pending verification.** Every figure marked `[E]` or `~` requires source replacement against the most recent 10-K / 10-Q / earnings release before external use
- [ ] Same metric definitions across all 8 peers (non-GAAP basis where shown)
- [ ] Fiscal year-end mismatch flagged in Slide 1 footer

**Synthesis**
- [x] Moat assessment per peer (Slide 8)
- [x] Durable advantages + structural vulnerabilities (Slide 8)
- [x] Probability-weighted scenarios with falsifiable signposts (Slide 9)

**Next steps to convert to a deck**
1. Replace every `[E]` and `~` with sourced values from 10-Ks / earnings releases
2. Build Slide 6 as a real XY scatter chart object (python-pptx or PowerPoint), bubble size = market cap
3. Convert Slides 4, 5, 7, 8, 9 tables into formatted PowerPoint tables (14pt body, bold gray header, right-aligned numerics)
4. Run visual verification pass for overflow, overlap, and citation completeness
