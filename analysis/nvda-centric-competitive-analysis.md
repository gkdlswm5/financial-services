# NVDA: Competitive Landscape — Protagonist-Centric View

**Protagonist:** NVIDIA (NVDA)
**Competitor set (by posture):**
- *Direct compute:* AMD, INTC (Gaudi)
- *Custom-ASIC merchant:* AVGO, MRVL
- *Hyperscaler captive:* Google TPU, AWS Trainium / Inferentia, MSFT Maia
- *Adjacent / ecosystem:* AMD ROCm, open-source stacks (PyTorch-XLA, OpenAI Triton)

**As of:** May 2026 | **Period:** Most recent FY / TTM, flagged per row
**Format:** 10-slide markdown draft (per `plugins/agent-plugins/market-researcher/skills/competitive-analysis/SKILL.md`)
**Companion files:** `analysis/avgo-competitive-analysis.md`, `analysis/nvda-competitive-analysis.md` (side-by-side benchmark)

> **Draft note — sources required.** Figures reflect publicly-reported FY24/FY25 results and consensus framing. Hyperscaler captive figures are estimates [E] inferred from capex disclosures, foundry checks, and management commentary — they require explicit sourcing from each hyperscaler's investor materials and infrastructure blog posts before external use.

---

## Slide 1 — Scope: NVDA as protagonist, four competitive postures arrayed around it

- **Why this framing.** NVDA's competitors are not a single peer set. Direct merchant competition (AMD, INTC) is the most visible but smallest threat by run-rate. Custom-ASIC merchant (AVGO, MRVL) is the fastest-growing share-take vector. Hyperscaler captive silicon (TPU, Trainium, Maia) is the largest structural long-term threat. Each posture has different economics, different timeframes, and different countermeasures.
- **What's in / out.** Excluded from this deck: QCOM (edge-only, not contesting DC), gaming-only competitors (AMD Radeon, INTC Arc — folded into AMD/INTC silicon lines), and pure software peers (NOW, PANW, ORCL — those compete for the enterprise AI budget but not for NVDA's silicon dollar).
- **Period.** NVDA FY25 (Jan-end) as the anchor; competitor data on their respective fiscal years, flagged.

Footer: "All figures USD. FY-ends: NVDA Jan, AMD Dec, INTC Dec, AVGO Oct, MRVL Jan. Hyperscaler captive silicon revenue is internal-use only and does not appear on any external P&L — figures shown are independent estimates."

---

## Slide 2 — Market context: where the AI silicon dollars sit and how fast they're growing

| Pool | 2024 size | Growth (CAGR) | NVDA position |
|---|---|---|---|
| Merchant DC accelerators (NVDA + AMD + INTC) | ~$135B [E] | 35-45% through 2027 [E] | ~85-90% share [E] |
| Custom-ASIC merchant (AVGO + MRVL) | ~$15-20B [E] | 40-50% [E] | Indirect — share-take from merchant accelerators |
| Hyperscaler captive silicon | ~$15-25B [E] equivalent fab spend | 50%+ [E] | Direct substitution — comes off NVDA TAM |
| Networking silicon for AI clusters | ~$25-30B [E] | 20-25% [E] | ~50% via Mellanox (InfiniBand + Spectrum-X); AVGO contested in Ethernet |
| Enterprise AI software / CUDA value-capture | Emerging | n/m | Monetized as silicon GM uplift, not separate revenue |

**Takeaway insight (slide title).** "Merchant accelerators are the big pool today; custom ASIC and hyperscaler captive silicon are the two pools eating into NVDA's TAM share at the margin."

---

## Slide 3 — Industry economics: NVDA captures software-tier economics on a silicon P&L

- **Fabless silicon margin curve.** 45-75% gross margin depending on mix. NVDA sits at the top (~75%) reflecting compute-tier pricing + CUDA value-capture.
- **NVDA's "shadow software" stack.** CUDA, cuDNN, TensorRT, NIM, NeMo, Omniverse, Drive — all priced as part of the GPU platform. No separate software P&L; the entire stack shows up as gross margin uplift on hardware revenue.
- **Counterpart for competitors:**
  - **AMD ROCm** — open, free, catching up but multi-year gap. No GM premium to AMD.
  - **AVGO** — no parallel software stack at the silicon layer; VMware is unrelated to the AI ASIC business.
  - **Hyperscaler captives** — software stacks are tightly coupled to internal training pipelines (JAX/XLA on TPU, Neuron SDK on Trainium). Capture is internal cost-savings, not external margin.
- **Implication.** NVDA's GM advantage is the most durable single line item in the competitive picture. If GM holds 72%+, the franchise is intact even with share loss at the edges. If GM compresses to 65%, the CUDA value-capture thesis is breaking.

**Takeaway insight (slide title).** "NVDA's 75% gross margin is the moat as a number — track it as the single most important competitive KPI."

---

## Slide 4 — NVDA profile

| Metric | FY25 (Jan-end) | YoY |
|---|---:|---:|
| Revenue | ~$130.5B | +114% |
| Non-GAAP gross margin | ~75% | +200-300 bps |
| Non-GAAP operating margin | ~62% | +500 bps [E] |
| Non-GAAP EPS | ~$2.99 [E] | +130% [E] |
| FCF margin | ~50% | +500 bps [E] |
| Market cap | ~$3.0T | — |

**Segment breakdown (FY25 [E]):**

| Segment | Revenue | Rev YoY | Rev % | Op margin |
|---|---:|---:|---:|---:|
| Data Center | ~$115B | +140% | ~88% | High 60s% |
| Gaming | ~$11B | +9% | ~8% | Mid 30s% |
| Professional Visualization | ~$2B | +20% | ~2% | Mid 30s% |
| Automotive | ~$1.7B | +55% | ~1% | Low 20s% |
| OEM & Other | <$1B | n/m | <1% | n/m |
| **Total** | **~$130.5B** | **+114%** | **100%** | **~62%** |

**Source stub.** NVDA 10-K FY25 + quarterly press releases. Segment op margins are estimates based on management commentary; replace with disclosed values where available.

**Takeaway insight (slide title).** "Data Center is now 88% of revenue and effectively the entire company — competitive analysis is a DC-segment analysis with everything else as optionality."

---

## Slide 5 — Competitor mapping by posture

**Posture diagram (concentric — NVDA at center):**

```
                  HYPERSCALER CAPTIVE
              (Google TPU, AWS Trainium,
                     MSFT Maia)
                          |
        DIRECT COMPUTE — NVDA — CUSTOM-ASIC MERCHANT
        (AMD, INTC Gaudi)     |     (AVGO, MRVL)
                              |
                       ADJACENT / ECOSYSTEM
                    (ROCm, PyTorch-XLA, Triton)
```

| Posture | Companies | Threat vector | Time horizon | NVDA countermeasure |
|---|---|---|---|---|
| **Direct compute** | AMD MI series; INTC Gaudi | Frontal GPU competition at lower price | 0-2 years | Annual cadence (Blackwell → Rubin → Feynman); CUDA lock-in |
| **Custom-ASIC merchant** | AVGO (Google TPU partner, MSFT Maia partner); MRVL (AWS Trainium partner) | Hyperscaler design wins shift TAM from merchant GPU to merchant ASIC | 1-3 years | Networking attach (Spectrum-X), NVL72 system selling, software stack incumbency |
| **Hyperscaler captive** | Google TPU (v5p, v6e); AWS Trainium2; MSFT Maia 100 | Hyperscaler internal substitution at scale; lowest cost-per-token | 2-5 years | DGX Cloud, sovereign AI partnerships, multi-cloud GPU presence, CUDA ecosystem lock |
| **Adjacent / ecosystem** | AMD ROCm; OpenAI Triton; PyTorch-XLA | Erodes CUDA moat over time | 3-7 years | CUDA developer investment, NIM, enterprise software bundling |

**Takeaway insight (slide title).** "Threats stack by time horizon — AMD this year, custom ASIC next, hyperscaler captive after that, CUDA erosion eventually."

---

## Slide 6 — Direct compute deep-dives (AMD, INTC)

### AMD

| Metric | Value (FY24, Dec-end) |
|---|---:|
| Revenue | ~$25.8B |
| Growth | +14% YoY |
| Non-GAAP GM | ~53% |
| Non-GAAP Op Margin | ~22% |
| FCF Margin | ~10% |
| Market cap [E] | ~$200B |
| DC GPU revenue (MI series) | ~$5B FY24 [E]; targeting $7-9B FY25 [E] |
| Market share, DC accelerator | <8% [E] |

| Category | Assessment |
|---|---|
| Business | x86 CPU (EPYC server, Ryzen client), DC GPU (MI300/MI325/MI355), embedded (Xilinx FPGAs) |
| Strengths | EPYC share gains; open ROCm narrative; close TSMC relationship; price/performance pitch |
| Weaknesses | CUDA absence is the central problem; ROCm hardening and ecosystem still 2-3 years behind; GM 20pp below NVDA |
| Strategy | Bet on Instinct MI series + ROCm + hyperscaler design wins (MSFT confirmed; META reported); CPU + GPU bundling |

### INTC (Gaudi line)

| Metric | Value (FY24, Dec-end) |
|---|---:|
| Total revenue | ~$53B |
| Total YoY | -2% |
| DC GPU revenue (Gaudi 3) | <$500M [E]; below management's earlier $500M Gaudi 3 target |
| GAAP op margin (total) | Negative — restructuring |
| Market cap [E] | ~$100B |

| Category | Assessment |
|---|---|
| Business | x86 CPU (Xeon), foundry (IFS), DC GPU (Gaudi 3, Falcon Shores roadmap) |
| Strengths | Foundry optionality; sovereign AI angle in EU |
| Weaknesses | Gaudi missed its own revenue target; software stack weakest of the three direct competitors; balance sheet under pressure |
| Strategy | Falcon Shores (2025-2026) consolidates Gaudi + Ponte Vecchio; foundry-led recovery |

**Takeaway insight (slide title).** "AMD is the only direct competitor with a credible roadmap; INTC's Gaudi line is sub-scale and the Falcon Shores reset is still ahead."

---

## Slide 7 — Custom-ASIC merchant deep-dives (AVGO, MRVL)

### AVGO

| Metric | Value (FY24, Oct-end) |
|---|---:|
| Total revenue | ~$51.6B |
| Total YoY | +44% (incl. VMware) |
| Non-GAAP GM | ~77% |
| Non-GAAP Op Margin | ~62% |
| AI revenue (DC ASIC + networking) | ~$12.2B FY24; targeting ~$18-22B FY25 [E] |
| Hyperscaler ASIC customers | Google TPU partner; MSFT Maia partner; rumored 3rd hyperscaler |
| Market cap [E] | ~$1.0T+ |

| Category | Assessment |
|---|---|
| Business | Hyperscaler custom AI ASIC, networking silicon (Tomahawk, Jericho), broadband/wireless, VMware software stack |
| Strengths | Design partnership lock-in with top hyperscalers; networking franchise complementary to ASIC; massive FCF + capital return |
| Weaknesses | Customer concentration (~2-3 hyperscalers in AI ASIC); execution risk on third hyperscaler ramp; VMware churn risk |
| Strategy | Add hyperscaler customer #3; cross-sell Ethernet AI networking against NVDA InfiniBand/Spectrum-X |

### MRVL

| Metric | Value (FY25, Jan-end) |
|---|---:|
| Total revenue | ~$5.8B |
| Total YoY | +5% |
| Non-GAAP GM | ~62% |
| Non-GAAP Op Margin | ~30% |
| AI revenue | ~$1.5B FY25 [E]; targeting >$2.5B FY26 [E] |
| Hyperscaler ASIC customers | AWS Trainium2; reportedly designing for 1-2 additional hyperscalers |
| Market cap [E] | ~$80B |

| Category | Assessment |
|---|---|
| Business | Custom ASIC (Trainium partnership), optical DSP, switching silicon, storage controllers |
| Strengths | Optical/DSP leadership in 800G/1.6T; #2 in custom AI ASIC behind AVGO; new design wins in pipeline |
| Weaknesses | Sub-scale vs AVGO; concentrated customer base; storage/wired markets are stagnant ballast |
| Strategy | Win 2nd and 3rd hyperscaler ASIC programs; ride 800G/1.6T optical cycle |

**Takeaway insight (slide title).** "Custom ASIC contests the highest-volume hyperscaler workloads; AVGO + MRVL combined are taking 15-25% [E] of incremental hyperscaler accelerator spend."

---

## Slide 8 — Hyperscaler captive silicon (TPU, Trainium, Maia)

These don't show up as revenue on any external P&L. Sizing is inferred from capex disclosures, foundry checks (TSMC, Samsung), and management commentary.

| Captive program | Hyperscaler | Generation in production (2026) | Design partner | Capability vs H100/B200 [E] | Scale of internal deployment [E] | Notes |
|---|---|---|---|---|---|---|
| **TPU** | Google | v5p, v6e (Trillium) | In-house ASIC team (with Broadcom as design partner for some generations) | Competitive on training; superior $/token for Google's models | >2M chips deployed estimated; Gemini trained on TPU | Most mature captive program; sells to external customers via GCP at limited scale |
| **Trainium / Inferentia** | AWS | Trainium2 (production); Trainium3 (in design) | Annapurna Labs + Marvell partnership on some generations | Below H100 on training perf; competitive on $/token for inference | Targeting >100k Trainium2 by end-2026 [E] | Anthropic partnership is the lighthouse training workload |
| **Maia 100** | Microsoft | Maia 100 (production); Maia 200 (in design) | In-house + Broadcom partnership | Generation behind H100 on training; targeted for inference | Limited deployment; OpenAI workloads still primarily on NVDA | Still early — execution risk |

**Captivity dynamics.** Hyperscalers will not move 100% of workloads to captive silicon — software stack maturity, model portability, and external workload (sovereign AI, enterprise) keep merchant GPU demand intact for years. But for *internal* training/inference at scale, captive silicon takes the marginal workload because the cost-per-token math is dramatic at hyperscaler volume.

**TAM math (illustrative, all [E]).** If hyperscaler captives reach $40B/year equivalent fab spend by 2028 vs. ~$20B today, that's ~$20B of incremental TAM that NVDA does not capture. On a $250B+ DC accelerator TAM that's manageable; if captives reach $80B, it's a thesis-breaker.

**Takeaway insight (slide title).** "Captive silicon is the only competitor that scales with the customer's own capex — track hyperscaler infrastructure blog posts, not earnings calls."

---

## Slide 9 — Positioning + moat synthesis

### 9a — 2×2 positioning: Capability × Ecosystem depth

**X — Capability (training perf at scale, generation-current):** Low → Frontier
**Y — Ecosystem depth (developer + software + system stack):** Shallow → Deep

| Competitor | X | Y | Quadrant |
|---|---|---|---|
| **NVDA** | Frontier | Deep | **Top-right (alone)** |
| Google TPU | High | Medium-deep (JAX/XLA + internal) | Upper-mid |
| AMD MI series | Medium-high | Shallow (ROCm catching up) | Lower-right |
| AVGO custom ASIC | High (for design-partner workloads) | Shallow (hyperscaler-internal) | Lower-right |
| AWS Trainium | Medium | Medium (Neuron SDK + AWS integration) | Mid |
| MRVL custom ASIC | Medium-high (for design-partner workloads) | Shallow | Lower-mid |
| MSFT Maia | Medium | Shallow | Lower-left |
| INTC Gaudi | Medium-low | Shallow | Lower-left |

**Build note.** NVDA in the upper-right alone — that's the visual. Other dots cluster in the lower-right and mid quadrants.

### 9b — Moat scorecard (NVDA vs each posture)

| Moat | NVDA | Direct compute (AMD/INTC) | Custom-ASIC (AVGO/MRVL) | Hyperscaler captive |
|---|---|---|---|---|
| **Network effects** | Strong (CUDA developers, model checkpoints, training recipes) | Weak (ROCm small, fragmented) | None (workload-specific) | Internal-only |
| **Switching costs** | Strong (code rewrites, validation, performance regressions) | Weak | Strong (for the design-partner hyperscaler) | Strong (internally) |
| **Scale economies** | Strong (TSMC priority, HBM allocation, system-level integration) | Moderate | Moderate (project-by-project) | Strong (paid for by parent capex) |
| **Intangibles** | Strong (CUDA IP, brand, Mellanox networking IP, system designs) | Moderate | Moderate (design IP) | Internal IP |

**Durable advantages.** Full-stack (compute + networking + software + system); CUDA dev ecosystem; annual cadence faster than competitors can ship.

**Structural vulnerabilities.** (1) Hyperscaler concentration — top 4 customers are ~50%+ of DC revenue [E]; (2) China export controls; (3) Custom-ASIC substitution at the margin for high-volume hyperscaler workloads.

**Takeaway insight (slide title).** "NVDA wins on all four moat dimensions; the real risk is hyperscaler concentration, not competitive displacement."

---

## Slide 10 — Investment scenarios + per-tier signposts

### 10a — NVDA bull/base/bear

| Scenario | Probability | Key drivers | Quantified signposts (12-18 mo) |
|---|---:|---|---|
| **Bull** | 30% | Blackwell + Rubin ramp clean; sovereign AI contributes >$30B [E]; CUDA moat holds; non-GAAP GM stays >75% | DC quarterly revenue >$45B exit FY26; non-GAAP GM 75%+; networking attach >70%; AMD MI share <8%; custom ASIC <20% of hyperscaler accel spend |
| **Base** | 55% | Blackwell ramps in line; custom ASIC takes 15-25% of hyperscaler accel spend [E]; GM modest compress to 72-74% | DC quarterly revenue $35-40B exit FY26; non-GAAP GM 72-74%; sovereign AI $15-20B FY26 [E]; one hyperscaler increases captive mix but stays >50% NVDA |
| **Bear** | 15% | Hyperscaler capex digestion 2H FY26; custom ASIC accelerates >35% of hyperscaler accel spend; export controls tighten; GM <70% | DC quarterly revenue decelerates QoQ 2+ quarters; non-GAAP GM <70%; top-4 customer signals reduced merchant GPU mix; China DC <$5B FY26 |

### 10b — Per-competitor-tier signposts to watch

| Tier | Watch for | What it means |
|---|---|---|
| **Direct compute** | AMD MI355/MI400 design wins disclosed at MSFT, META, OpenAI; ROCm 7+ parity benchmarks vs CUDA | AMD share creeping past 10% would shift the narrative; ROCm parity is the bigger long-term signal |
| **Custom-ASIC merchant** | AVGO disclosing a 3rd hyperscaler customer; MRVL winning a 2nd large hyperscaler ASIC program; AVGO/MRVL networking attach rates | Each new design win is incremental TAM permanently shifting from merchant GPU |
| **Hyperscaler captive** | Google TPU v6/v7 deployment scale; AWS Trainium3 specs and Anthropic commitments; MSFT Maia 200 production timeline; capex disclosures referencing internal silicon | The leading indicator is foundry/HBM allocation, not earnings calls |
| **Adjacent / ecosystem** | PyTorch-XLA adoption; OpenAI Triton spread; ROCm developer count | Slow-moving but binary — CUDA's moat depth changes if developer mindshare shifts |

**Takeaway insight (slide title).** "Base case ranks NVDA #1 across the cohort; the bear case is built from hyperscaler capex digestion + custom-ASIC acceleration, not from AMD."

---

## Appendix — quality checklist (per skill)

**Prompt fidelity**
- [x] NVDA-centric (protagonist) framing with competitors grouped by posture (per user selection)
- [x] 10-slide full primer (per user selection)
- [x] Peer set: silicon competitors + hyperscaler captives (per user selection)
- [x] Per-competitor deep-dive tables (Step 6 of skill) rather than side-by-side

**Data consistency**
- [ ] **Pending verification.** Every figure marked `[E]` or `~` requires sourcing. Hyperscaler captive sizing especially — these are inference estimates and must be replaced with capex / foundry / infrastructure-blog citations before external use
- [ ] Non-GAAP basis used consistently across all peers
- [ ] Numbers must agree with companion files (`avgo-competitive-analysis.md`, `nvda-competitive-analysis.md`) where the same metric appears

**Synthesis**
- [x] Moat scorecard with NVDA vs each posture (Slide 9b)
- [x] Durable advantages + structural vulnerabilities (Slide 9b)
- [x] Probability-weighted scenarios with falsifiable signposts (Slide 10a)
- [x] Per-tier signposts to watch (Slide 10b) — unique to the centric framing

**Next steps to convert to a deck**
1. Replace every `[E]` and `~` with sourced values
2. Build Slide 5 posture diagram as a centric/concentric shape diagram (not just text)
3. Build Slide 9a as a real XY scatter chart, NVDA visually isolated in upper-right
4. Convert competitor deep-dive blocks (Slides 6, 7) into formatted two-table layouts per competitor
5. Build Slide 8 captive-program comparison as a formatted table; add small inline charts where useful
6. Visual verification pass for overflow, overlap, citation completeness
