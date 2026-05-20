# Semis + Software: Peer Benchmarking & Investment Scenarios — NVDA focus

**Peer set:** NVDA, AMD, MRVL, QCOM, AVGO (silicon) + PANW, NOW, ORCL (infrastructure software)
**As of:** May 2026 | **Period:** Most recent FY / TTM, flagged per row
**Format:** 9-slide markdown draft (per `plugins/agent-plugins/market-researcher/skills/competitive-analysis/SKILL.md`)
**Companion to:** `analysis/avgo-competitive-analysis.md` (same peer set, AVGO scenarios)

> **Draft note — sources required.** Figures below reflect publicly-reported FY24/FY25 results and consensus framing. Every value must be re-verified against 10-Ks, 10-Qs, and earnings releases before this is shared externally. Citations are stubbed as `[Company 10-K FYxx]` where final source links should be inserted.

---

## Slide 1 — Scope: eight peers across silicon and infrastructure software

- **Purpose.** Side-by-side benchmarking, with NVDA scenarios called out in Slide 9.
- **Coverage.** Five silicon names (NVDA, AMD, MRVL, QCOM, AVGO) and three infrastructure-software names (PANW, NOW, ORCL).
- **Why this set.** The semis cohort brackets NVDA's silicon competition — direct (AMD), custom-ASIC threat (AVGO, MRVL), and adjacent capex sinks (QCOM). The software cohort frames where the next leg of NVDA's stack (CUDA, NIM, Enterprise AI software) is competing for budget — against ORCL/OCI, NOW agents, and PANW AI security.
- **Period.** Most recent reported FY for each (fiscal year-ends differ — flagged).

Footer: "All figures in USD. Fiscal year-ends: NVDA Jan, AMD Dec, MRVL Jan, QCOM Sep, AVGO Oct, PANW Jul, NOW Dec, ORCL May."

---

## Slide 2 — Market context: AI accelerator TAM is NVDA's home field

| Market | 2024 size | Growth (CAGR) | NVDA exposure |
|---|---|---|---|
| Data-center AI accelerators | ~$125B [E] | 35-45% through 2027 [E] | ~85-90% share of merchant accelerators [E] |
| Networking silicon (custom ASIC + merchant) | ~$25-30B [E] | 20-25% [E] | Mellanox (InfiniBand + Spectrum-X Ethernet); contested by AVGO/MRVL |
| AI inference at the edge | ~$15-25B [E] | 30%+ [E] | Jetson, Drive; contested by QCOM/AMD |
| Enterprise AI software (CUDA stack, NIM, NeMo) | Emerging | n/m | Adjacent to ORCL/NOW/PANW |
| Gaming GPU | ~$15B | Low-to-mid single digit | Dominant share, ex-China |
| Auto / robotics compute | ~$10B [E] | 20%+ [E] | Drive platform; QCOM is primary competitor |

**Takeaway insight (slide title).** "NVDA's TAM map: ~$125B accelerator pool growing 35%+ is the gravity well; everything else is optionality or defense."

---

## Slide 3 — Industry economics: NVDA monetizes both silicon AND a software stack

**Value-chain framing:**

- **Fabless silicon** — gross margins 45-75% depending on mix. NVDA at ~75% is the high-water mark, reflecting compute-tier pricing and CUDA value-capture above the hardware.
- **Infrastructure software** — gross margins 70-85%. FCF margin 30-40% at scale.
- **NVDA's unusual position.** The only silicon peer with a proprietary software layer (CUDA + cuDNN + TensorRT + NIM + Omniverse) that customers price as part of the platform. That software layer doesn't show up cleanly in segment reporting but is the principal reason gross margin sits ~10-20pp above silicon peers.
- **AVGO's hybrid is the closest analog** — but AVGO's software (VMware) is unrelated to its silicon. NVDA's software is *inseparable* from its silicon.

**Takeaway insight (slide title).** "NVDA captures software-tier economics on a silicon P&L — the CUDA stack is the unrecognized SaaS layer driving 75% GM."

---

## Slide 4 — Silicon peer profiles (single comparison table)

| Company | FY | Revenue | YoY | Non-GAAP GM | Non-GAAP Op Margin | FCF Margin | Mkt Cap [E] | Key franchise |
|---|---|---:|---:|---:|---:|---:|---:|---|
| **NVDA** | FY25 (Jan-end) | ~$130.5B | +114% | ~75% | ~62% | ~50% | ~$3.0T | Data-center GPU + CUDA |
| AVGO | FY24 (Oct-end) | ~$51.6B | +44% (incl. VMware) | ~77% | ~62% | ~40% | ~$1.0T+ | Custom AI ASIC + networking + VMware |
| QCOM | FY24 (Sep-end) | ~$39.0B | +9% | ~56% | ~28% | ~22% | ~$190B | Handset SoC + auto + IoT |
| AMD | FY24 (Dec-end) | ~$25.8B | +14% | ~53% | ~22% | ~10% | ~$200B | DC CPU (EPYC) + DC GPU (MI300) |
| MRVL | FY25 (Jan-end) | ~$5.8B | +5% | ~62% | ~30% | ~25% | ~$80B | Custom ASIC + optical DSP |

**Source stub.** Each company's 10-K + most recent earnings release. All non-GAAP figures as reported by management. `[E]` market cap = approximate, point-in-time.

**Takeaway insight (slide title).** "NVDA's revenue scale is 2.5x AVGO; growth rate is 2.6x AVGO; both metrics widening vs. the rest of the silicon cohort."

---

## Slide 5 — Infrastructure-software peer profiles (single comparison table)

| Company | FY | Revenue | YoY | Non-GAAP GM | Non-GAAP Op Margin | FCF Margin | Mkt Cap [E] | Why it matters to NVDA |
|---|---|---:|---:|---:|---:|---:|---:|---|
| ORCL | FY25 (May-end) | ~$57B | +9% | ~80% | ~45% | ~25% | ~$450B | OCI is a top-3 NVDA GPU customer; potential GPU competition via OCI's own infra |
| NOW | FY24 (Dec-end) | ~$11.0B | +22% | ~83% | ~30% | ~31% | ~$200B | AI agent platform — competes with NVDA for the enterprise AI app budget |
| PANW | FY24 (Jul-end) | ~$8.0B | +16% | ~78% | ~28% | ~38% | ~$130B | AI security workloads run on NVDA — customer, not competitor |

**Source stub.** Each company's 10-K + segment disclosures.

**Takeaway insight (slide title).** "Software peers are mostly NVDA customers; the structural question is whether NVDA's enterprise AI software stack eventually competes with NOW/ORCL for the same enterprise dollar."

---

## Slide 6 — Positioning: 2×2 — Growth (YoY rev) × Profitability (FCF margin)

**Axes.**
- **X — YoY revenue growth (FY most recent).** Range: 0% to +115%.
- **Y — FCF margin (FY most recent).** Range: 10% to 55%.

**Plotted (X, Y):**

| Company | X — YoY rev | Y — FCF margin | Quadrant |
|---|---:|---:|---|
| **NVDA** | **+114%** | **~50%** | **Top-right (alone on the frontier)** |
| AVGO | +44% | ~40% | Top-right (only company within shouting distance) |
| NOW | +22% | ~31% | Upper-mid |
| PANW | +16% | ~38% | Upper-mid |
| AMD | +14% | ~10% | Lower-mid |
| QCOM | +9% | ~22% | Lower-mid |
| ORCL | +9% | ~25% | Lower-mid |
| MRVL | +5% | ~25% | Lower-left |

**Build note (for slide construction).** Real chart object (XY scatter), labels on each bubble, axis titles set explicitly, no overlapping labels. Bubble size = market cap (optional third dimension). NVDA dot should be visually isolated on the right edge of the plot — that's the insight.

**Takeaway insight (slide title).** "NVDA is alone in the top-right at 114% growth and 50% FCF margin — no other peer combines both."

---

## Slide 7 — Comparative scorecard (●●●/●●○/●○○ across 5 dimensions)

Ratings reflect rank within this 8-peer set, not absolute.

| Dimension | **NVDA** | AVGO | ORCL | QCOM | AMD | NOW | PANW | MRVL |
|---|---|---|---|---|---|---|---|---|
| **Scale** (Mkt cap) | ●●● $3.0T | ●●● $1.0T+ | ●●○ $450B | ●●○ $190B | ●●○ $200B | ●●○ $200B | ●○○ $130B | ●○○ $80B |
| **Growth** (YoY rev) | ●●● +114% | ●●● +44% | ●○○ +9% | ●○○ +9% | ●○○ +14% | ●●○ +22% | ●●○ +16% | ●○○ +5% |
| **Margins** (FCF) | ●●● 50% | ●●● 40% | ●●○ 25% | ●●○ 22% | ●○○ 10% | ●●○ 31% | ●●● 38% | ●●○ 25% |
| **Moat** (qual) | ●●● CUDA + DC lock-in | ●●● Custom ASIC + VMware switching cost | ●●○ DB switching cost; OCI emerging | ●●○ Modem IP + Apple risk | ●○○ Open ecosystem, catching up | ●●● Workflow embed | ●●○ Platform consolidation | ●○○ Concentrated customers |
| **Capital return** (buybacks + div) | ●●○ Buybacks expanding | ●●● Dividend + buyback | ●●○ Steady buyback + div | ●●● Heavy buyback + div | ●○○ Limited | ●○○ None | ●○○ None | ●○○ Limited |

**Takeaway insight (slide title).** "NVDA scores ●●● on Scale, Growth, Margins, and Moat — the only peer with four ●●● columns. Capital return is the single ●●○ to watch."

---

## Slide 8 — Moat assessment + structural vulnerabilities

| Company | Network effects | Switching costs | Scale economies | Intangibles | Durable advantages | Structural vulnerabilities |
|---|---|---|---|---|---|---|
| **NVDA** | **Strong (CUDA dev ecosystem — millions of developers)** | **Strong (CUDA lock-in, software stack, model checkpoints)** | **Strong (TSMC priority access, HBM allocation)** | **Strong (CUDA IP, brand, Mellanox networking IP)** | **DC GPU dominance + CUDA moat + full-stack (compute + networking + software)** | **Custom ASIC erosion at hyperscalers (AVGO, MRVL); China export controls; cyclical hyperscaler capex; AMD ROCm closing the software gap (slowly)** |
| AVGO | Moderate (VMware ecosystem) | Strong (VMware contractual + ASIC design wins) | Strong (fab capacity, vertical scale) | Strong (IP portfolio, M&A engine) | Custom ASIC franchise + VMware recurring | Customer concentration in AI ASIC (~2-3 hyperscalers); VMware churn risk |
| ORCL | Weak | Strong (DB migration cost) | Moderate (OCI scaling) | Strong (DB IP, install base) | DB + cloud DB lock-in; OCI AI tailwind | OCI capex burden; legacy apps decline |
| QCOM | Weak | Moderate (modem IP licensing) | Strong (modem scale) | Strong (5G/6G patents) | Modem IP, Apple revenue (declining) | Apple in-house modem; China handset cycle |
| AMD | Weak | Weak (open standards) | Moderate (TSMC dependency) | Moderate (CPU IP) | EPYC share gains in DC CPU | GPU gap vs NVDA; CUDA absence |
| NOW | Moderate (admin/dev community) | Strong (workflow embed) | Moderate | Strong (platform extensibility) | Workflow stickiness + AI agent layer | Federal exposure; AI cannibalization of seats |
| PANW | Weak | Strong (platform consolidation) | Moderate | Strong (security IP) | "Platformization" cross-sell | Decel risk in core firewall; competitive crowd |
| MRVL | Weak | Moderate (custom-ASIC design lock-in) | Weak (sub-scale vs AVGO) | Moderate | Optical DSP leadership; custom ASIC #2 | 2-3 customer concentration; AVGO competition |

**Takeaway insight (slide title).** "NVDA is the only peer rated Strong on all four moat dimensions; the principal vulnerability is hyperscaler custom-ASIC substitution at the margin, not a frontal compute attack."

---

## Slide 9 — Investment scenarios: NVDA bull/base/bear + relative peer ranking

### 9a — NVDA scenarios

| Scenario | Probability | Key drivers | Quantified signposts (12-18 mo) |
|---|---:|---|---|
| **Bull** | 30% | Blackwell + Rubin ramps without yield issues; sovereign AI demand >$30B contribution [E]; CUDA moat holds against ROCm and custom ASIC; gross margin stays >75% | DC quarterly revenue >$45B exit FY26; non-GAAP GM holds 75%+; networking attach rate >70% on new GPU deployments; <10% revenue contribution from custom-ASIC substitution at top-3 customers |
| **Base** | 55% | Blackwell ramps in line with capex; custom ASIC takes 15-25% of hyperscaler accelerator spend [E]; GM compresses modestly to 72-74% as ASIC mix-shifts the comp set | DC quarterly revenue $35-40B exit FY26; non-GAAP GM 72-74%; sovereign AI contributes $15-20B annually [E]; AMD MI series stays <8% share |
| **Bear** | 15% | Hyperscaler capex digestion in 2H FY26; custom ASIC accelerates to >35% of hyperscaler accel spend; export controls tighten further; GM falls to <70% | DC quarterly revenue decelerates QoQ for 2+ quarters; non-GAAP GM <70%; one top-4 customer signals reduced merchant GPU mix; China DC revenue <$5B FY26 |

Signposts are deck-defining: every scenario must be **falsifiable within 12-18 months** with a public data point.

### 9b — Relative pick order across the 8 peers (NVDA-anchored view)

| Rank | Company | Thesis in one line |
|---|---|---|
| 1 | **NVDA** | Frontier of growth + margin with a CUDA moat that is widening, not narrowing; base case still rewards holders at current multiple |
| 2 | AVGO | Best hedge against NVDA — owns the custom-ASIC counter-thesis with VMware as the cushion |
| 3 | NOW | Cleanest software compounder; orthogonal to silicon cycle; AI agent optionality |
| 4 | PANW | Highest FCF margin in the software peer set; consolidation tailwind |
| 5 | ORCL | OCI is NVDA's friend today, potentially its adjacent competitor tomorrow; cheaper multiple |
| 6 | MRVL | Best leveraged optical/DSP play; second mover on custom ASIC behind AVGO |
| 7 | QCOM | Cheapest semis name; Apple modem loss largely priced; limited AI accelerator exposure |
| 8 | AMD | DC CPU share story is real; GPU vs NVDA is the elephant — ROCm progress is slower than the narrative |

**Takeaway insight (slide title).** "Base case ranks NVDA #1 across all 8 peers; bear case still places NVDA top-3 because the alternatives (AVGO, NOW) inherit different — not lesser — risk profiles."

---

## Appendix — quality checklist (per skill)

**Prompt fidelity**
- [x] All 8 peers represented on every comparison slide
- [x] 2×2 matrix (not radar) — consistent with companion AVGO deck
- [x] Markdown draft (not .pptx) — consistent with companion AVGO deck
- [x] NVDA scenarios + peer ranking on Slide 9

**Data consistency**
- [ ] **Pending verification.** Every figure marked `[E]` or `~` requires source replacement against the most recent 10-K / 10-Q / earnings release before external use
- [ ] Same metric definitions across all 8 peers (non-GAAP basis where shown)
- [ ] All silicon/software peer data must match the companion AVGO file (numbers identical except where NVDA framing changes the narrative around them)
- [ ] Fiscal year-end mismatch flagged in Slide 1 footer

**Synthesis**
- [x] Moat assessment per peer (Slide 8) — NVDA row expanded
- [x] Durable advantages + structural vulnerabilities (Slide 8)
- [x] Probability-weighted scenarios with falsifiable signposts (Slide 9)

**Next steps to convert to a deck**
1. Replace every `[E]` and `~` with sourced values from 10-Ks / earnings releases
2. Build Slide 6 as a real XY scatter chart object (python-pptx or PowerPoint), bubble size = market cap, NVDA visually isolated on right edge
3. Convert Slides 4, 5, 7, 8, 9 tables into formatted PowerPoint tables (14pt body, bold gray header, right-aligned numerics)
4. Run visual verification pass for overflow, overlap, and citation completeness
