"""
Tablet-friendly single-file HTML view of the AVGO deck (20 sections), charts
embedded as base64. Mirrors analysis/MP and analysis/WMT HTML views.
Run after build_deck.py (needs charts/ai_ramp.png, positioning.png, football.png).
"""
import base64
from pathlib import Path
HERE = Path(__file__).parent


def b64(p):
    return base64.b64encode((HERE / "charts" / p).read_bytes()).decode("ascii")


ai = b64("ai_ramp.png"); pos = b64("positioning.png"); fb = b64("football.png")

HTML = f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=5"/>
<title>Broadcom (AVGO) — Competitive Analysis & Valuation</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
  :root {{ --navy:#17365D; --red:#CC0000; --ink:#1f2937; --ink2:#6b7280; --bg:#f8fafc; --card:#fff; --border:#e5e7eb; --good:#2E7D32; --bad:#C0392B; --warn:#d97706; }}
  html,body {{ background:var(--bg); color:var(--ink); font-family:ui-serif,Georgia,'Times New Roman',serif; }}
  .card {{ background:var(--card); border:1px solid var(--border); border-radius:12px; box-shadow:0 1px 3px rgba(0,0,0,.04); }}
  .slide-num {{ font-family:ui-sans-serif,system-ui,sans-serif; font-size:.7rem; letter-spacing:.1em; text-transform:uppercase; color:var(--red); font-weight:600; }}
  h2.slide-title {{ font-size:1.3rem; line-height:1.3; color:var(--navy); font-weight:700; margin-top:.25rem; }}
  .pill {{ display:inline-block; padding:2px 10px; border-radius:999px; font-size:.72rem; font-family:ui-sans-serif,system-ui,sans-serif; font-weight:600; }}
  .pill-good {{ background:#dcfce7; color:#166534; }} .pill-warn {{ background:#fef3c7; color:#92400e; }}
  .pill-bad {{ background:#fee2e2; color:#991b1b; }} .pill-navy {{ background:#dbeafe; color:#1e40af; }}
  .pill-red {{ background:#fee2e2; color:#991b1b; }}
  table {{ width:100%; border-collapse:collapse; font-size:.85rem; }}
  th {{ background:var(--navy); color:#fff; padding:8px 10px; text-align:left; font-family:ui-sans-serif,system-ui,sans-serif; font-size:.8rem; }}
  td {{ padding:8px 10px; border-bottom:1px solid var(--border); vertical-align:top; }}
  tr:nth-child(even) td {{ background:#f9fafb; }}
  .num {{ text-align:right; font-variant-numeric:tabular-nums; }}
  ul.dot {{ list-style:none; padding:0; }} ul.dot li {{ position:relative; padding-left:1.1em; margin:.4em 0; line-height:1.55; }}
  ul.dot li::before {{ content:"\\2022"; color:var(--red); position:absolute; left:0; font-weight:700; }}
  .source {{ font-size:.72rem; color:var(--ink2); font-style:italic; margin-top:1rem; padding-top:.5rem; border-top:1px solid var(--border); }}
  .toc a {{ display:block; padding:6px 0; color:var(--ink); border-bottom:1px solid #f1f5f9; font-size:.85rem; }}
  .toc a:hover {{ color:var(--red); }} .toc-num {{ color:var(--red); font-family:ui-sans-serif,system-ui,sans-serif; font-weight:600; margin-right:8px; font-size:.75rem; }}
  details summary {{ cursor:pointer; padding:8px 12px; background:#f1f5f9; border-radius:8px; font-weight:600; font-family:ui-sans-serif,system-ui,sans-serif; }}
  .tier-bar {{ width:4px; border-radius:4px; }}
  @media (min-width:1024px) {{ .l2 {{ display:grid; grid-template-columns:1.4fr 1fr; gap:1.5rem; }} .l3 {{ display:grid; grid-template-columns:1fr 1fr 1fr; gap:1rem; }} }}
</style></head><body class="antialiased">

<header class="bg-[var(--navy)] text-white"><div class="max-w-3xl mx-auto px-5 py-6">
  <div class="text-xs uppercase tracking-widest" style="color:var(--red);">NASDAQ: AVGO &middot; Investment Decision Frame</div>
  <h1 class="text-3xl font-bold mt-2">Broadcom Inc.</h1>
  <div class="text-base mt-1 opacity-90">Competitive Landscape, Comps &amp; DCF Valuation</div>
  <div class="text-xs mt-3 opacity-70">As of June 2026 &middot; 20 sections</div>
</div></header>

<nav class="max-w-3xl mx-auto px-5 py-5"><details><summary>Jump to section</summary>
<div class="toc mt-3 px-2">
{''.join(f'<a href="#s{i}"><span class="toc-num">{i:02d}</span>{t}</a>' for i, t in [
 (1,"Cover"),(2,"Thesis"),(3,"The question"),(4,"Market — AI capex"),(5,"Segment split"),(6,"AVGO profile"),
 (7,"GPU vs custom ASIC"),(8,"AVGO moats"),(9,"Peer set"),(10,"Positioning 2×2"),(11,"NVIDIA deep dive"),
 (12,"AMD + Marvell"),(13,"Qualcomm + TI"),(14,"VMware vs Oracle"),(15,"Scoreboard"),(16,"Valuation — football field"),
 (17,"Valuation — DCF + sensitivity"),(18,"Synthesis & moats"),(19,"Bull/base/bear"),(20,"Decision & sources")])}
</div></details></nav>

<main class="max-w-3xl mx-auto px-5 pb-16 space-y-5">

<section id="s2" class="card p-5">
  <div class="slide-num">02 &middot; Thesis</div>
  <h2 class="slide-title">Q2 print confirms the franchise — but at ~$482, even after the move, the price still embeds bull AI</h2>
  <div class="mt-4 space-y-4 text-sm">
    <div><span class="pill pill-navy">1. The franchise</span><p class="mt-2">#1 custom AI-silicon design house (~70% share) + leading AI networking. Q2 FY26: revenue $22.2B (+48%), AI revenue $10.8B (+143%), adj. EBITDA $15.2B (69%), FCF $10.3B (46%). Q3 guide $29.4B (+84%). $73B AI backlog; 6 hyperscaler customers.</p></div>
    <div><span class="pill pill-red">2. The FCF engine</span><p class="mt-2">VMware made Infrastructure Software a ~$27B/yr, ~78%-operating-margin annuity. Consolidated TTM FCF ~$33B+ (~44% margin) post Q2's $10.3B. Net debt down to ~$49B from a ~$74B post-VMware peak; dividend +10%.</p></div>
    <div><span class="pill pill-warn">3. The valuation problem</span><p class="mt-2">Hock Tan REITERATED — did NOT raise — the FY27 "AI $100B+" guide despite the Q2 beat. Base-case DCF (haircut ~15% to $85B FY27 AI) ~$264/share. ENTIRE WACC×g grid ($200–$311) below the ~$482 price; bull corner ~$395.</p></div>
    <div><span class="pill pill-good">4. The read</span><p class="mt-2">Q2 beat closed some of the gap (stock +4.7% on the print) — but the structural finding holds: to justify $482 you still need full mgmt FY27 AI delivered AND a low discount rate. Long on pullbacks / pair vs MRVL; trim into strength.</p></div>
  </div>
  <div class="source">AVGO Q1 FY26 IR; AVGO-Model.xlsx (DCF); The Information (May 2026, OpenAI financing). Research, not investment advice.</div>
</section>

<section id="s3" class="card p-5">
  <div class="slide-num">03 &middot; The question</div>
  <h2 class="slide-title">The question this analysis answers</h2>
  <blockquote class="mt-4 pl-4 border-l-4 border-[var(--red)] text-base italic" style="color:var(--navy);">
    "Broadcom Q2 FY26 (June 3) printed +48% revenue, AI +143%, with Q3 guided +84% — but the stock is at ~$482 (~$2.3T, ~29x fwd). How much of the AI bull case is already in the price post-print, and what has to be true to justify owning it here?"</blockquote>
  <ol class="mt-4 space-y-1 pl-5 list-decimal text-sm">
    <li><b>Market</b> — is the hyperscaler AI-capex cycle still supportive?</li>
    <li><b>Competitive</b> — how durable is AVGO's custom-ASIC + networking position vs NVDA, AMD, MRVL?</li>
    <li><b>Financial (comps)</b> — how does AVGO screen vs the semis cohort + ORCL anchor?</li>
    <li><b>Intrinsic (DCF)</b> — what is AVGO worth on a base case, and what does $482 imply?</li>
    <li><b>Decision</b> — bull/base/bear and the cleanest way to express a view.</li>
  </ol>
</section>

<section id="s4" class="card p-5">
  <div class="slide-num">04 &middot; Market — AI capex</div>
  <h2 class="slide-title">Hyperscaler AI capex ~$630–725B in 2026, topping $1T by 2027 — and the mix is shifting to custom silicon</h2>
  <table class="mt-4"><thead><tr><th>Driver</th><th>Data point</th></tr></thead><tbody>
    <tr><td>Big-4 capex 2025A</td><td>~$388–410B (record)</td></tr>
    <tr><td>Big-4 capex 2026E</td><td>~$630–725B (+62–77%)</td></tr>
    <tr><td>Total compute capex 2026E</td><td>~$1.04T (first trillion-$ year)</td></tr>
    <tr><td>AI accelerator TAM</td><td>~$200B → $500B+ late-decade</td></tr>
    <tr><td>Custom ASIC growth 2026E</td><td>~+45% units vs ~+16% GPU</td></tr>
    <tr><td>AVGO + MRVL custom-ASIC share</td><td>~95% of co-design market</td></tr>
  </tbody></table>
  <div class="mt-4 text-sm"><div class="font-semibold" style="color:var(--red);">The catch</div>
  <ul class="dot mt-2"><li>Capex growing ~46% faster than revenue — wider than the 2001 telecom-bust divergence (Allianz).</li>
  <li>~$400B/yr implied AI depreciation &gt; Big-4's combined profits.</li>
  <li>Power is the binding constraint: ~40% of AI DCs power-limited by 2027 (Gartner).</li>
  <li>Digestion risk into 2027–28 is the key macro swing factor for AVGO.</li></ul></div>
  <div class="source">CNBC, Tom's Hardware, Goldman, Dell'Oro, Allianz, Gartner (2026). Third-party estimates; ranges where sources diverge.</div>
</section>

<section id="s5" class="card p-5">
  <div class="slide-num">05 &middot; Segment split</div>
  <h2 class="slide-title">Two businesses: a ~60% AI-led semis engine and a ~40% software FCF annuity</h2>
  <table class="mt-4"><thead><tr><th>Segment (Q1 FY26)</th><th class="num">Revenue</th><th class="num">Growth</th><th class="num">Op margin</th></tr></thead><tbody>
    <tr><td>Semiconductor Solutions</td><td class="num">$12.5B</td><td class="num" style="color:var(--good);">+52%</td><td class="num">high</td></tr>
    <tr><td>&nbsp;&nbsp;of which AI semis</td><td class="num">$8.4B</td><td class="num" style="color:var(--good);">+106%</td><td class="num">—</td></tr>
    <tr><td>&nbsp;&nbsp;of which non-AI semis</td><td class="num">$4.1B</td><td class="num">~flat</td><td class="num">—</td></tr>
    <tr><td>Infrastructure Software (VMware)</td><td class="num">$6.8B</td><td class="num">+1%</td><td class="num">78%</td></tr>
    <tr><td><b>Total</b></td><td class="num"><b>$19.3B</b></td><td class="num" style="color:var(--good);"><b>+29%</b></td><td class="num"><b>66% NG</b></td></tr>
  </tbody></table>
  <ul class="dot mt-3 text-sm">
    <li>The semis engine re-rates the stock — AI +106%, $73B backlog, "$100B+ AI in FY27" line of sight.</li>
    <li>The software annuity (78% op margin, ~$27B/yr) de-risks it — recurring cash funding debt paydown + buybacks.</li>
    <li>This bifurcation is why the comps need a software anchor (ORCL) alongside the semis cohort.</li>
    <li><b>Caveat:</b> AVGO reports ONE Semiconductor segment; the AI / non-AI split is mgmt commentary, partly estimated.</li>
  </ul>
  <div class="source">Broadcom Q1 FY26 earnings release (Mar 2026).</div>
</section>

<section id="s6" class="card p-5">
  <div class="slide-num">06 &middot; AVGO profile</div>
  <h2 class="slide-title">AI inflection with a fortress FCF profile and a de-levering balance sheet</h2>
  <div class="l2 mt-4">
    <table><thead><tr><th>Metric</th><th class="num">Value</th></tr></thead><tbody>
      <tr><td>Q2 FY26 revenue</td><td class="num">$22.2B (+48%)</td></tr>
      <tr><td>Q1 FY26 AI revenue</td><td class="num">$8.4B (+106%)</td></tr>
      <tr><td>Q2 FY26 guide (total / AI)</td><td class="num">$22.0B / $10.7B</td></tr>
      <tr><td>FY26 revenue consensus [E]</td><td class="num">~$94.7B</td></tr>
      <tr><td>Adj. EBITDA margin</td><td class="num">68%</td></tr>
      <tr><td>TTM FCF [E]</td><td class="num">~$33B+ (~42%)</td></tr>
      <tr><td>Net debt [E]</td><td class="num">~$51.9B</td></tr>
      <tr><td>Market cap / EV [E]</td><td class="num">~$2.18T / ~$2.23T</td></tr>
      <tr><td>P/E TTM / fwd</td><td class="num">~80x / ~31x</td></tr>
    </tbody></table>
    <div class="mt-4 lg:mt-0"><img src="data:image/png;base64,{ai}" class="rounded-lg border border-[var(--border)] w-full"/>
    <p class="text-xs mt-2" style="color:var(--ink2);">AI revenue ramp: red = base case; navy marker = mgmt's $100B+ FY27 line-of-sight we haircut ~24%.</p></div>
  </div>
  <div class="source">AVGO Q1 FY26 8-K/IR; StockAnalysis.com (~June 1 2026); AVGO-Model.xlsx.</div>
</section>

<section id="s7" class="card p-5">
  <div class="slide-num">07 &middot; GPU vs custom ASIC</div>
  <h2 class="slide-title">Merchant GPU vs custom ASIC — the structural share shift is the heart of the bull case</h2>
  <table class="mt-4"><thead><tr><th>Dimension</th><th>Merchant GPU</th><th>Custom ASIC / XPU</th></tr></thead><tbody>
    <tr><td>2026E unit growth</td><td>~+16%</td><td>~+45% (≈3x)</td></tr>
    <tr><td>Share today</td><td>~70% (NVDA), eroding</td><td>~15–25%, → ~50% by 2027</td></tr>
    <tr><td>Economics</td><td>High merchant margin</td><td>Sticky multi-gen design lock-in</td></tr>
    <tr><td>AVGO position</td><td>n/a</td><td>~70% of design market</td></tr>
  </tbody></table>
  <ul class="dot mt-3 text-sm">
    <li><b>Bull:</b> hyperscalers internalize inference on custom silicon → ASIC pool grows ~3x faster; AVGO+MRVL own ~95% of design.</li>
    <li><b>Bear:</b> AI revenue leans on a few programs; Google multi-sourcing (MediaTek/Marvell) dilutes content; an OpenAI slip is a large hole.</li>
    <li><b>Networking leg:</b> Tomahawk 6 (102.4 Tb/s) + Jericho4 — open Ethernet now past InfiniBand in AI back-end share (Dell'Oro).</li>
  </ul>
  <div class="source">Goldman Sachs, Dell'Oro, Tom's Hardware, The Next Platform (2026). Mix figures estimated.</div>
</section>

<section id="s8" class="card p-5">
  <div class="slide-num">08 &middot; Moats</div>
  <h2 class="slide-title">Custom-silicon switching costs + IP + a $73B backlog + VMware lock-in</h2>
  <table class="mt-4"><thead><tr><th>Layer</th><th>Detail / KPI</th></tr></thead><tbody>
    <tr><td>Design lock-in</td><td>Multi-year hyperscaler co-design; switching = full chip re-spin. ~70% design share.</td></tr>
    <tr><td>Backlog visibility</td><td>~$73B AI backlog; "$100B+ AI revenue FY27" across 6 customers</td></tr>
    <tr><td>Anchor customers</td><td>Google (TPU), Meta (MTIA), ByteDance; + Anthropic (~$21B), OpenAI (~10GW), Apple ("Baltra")</td></tr>
    <tr><td>AI networking</td><td>Tomahawk 6 / Ultra + Jericho4 — open Ethernet vs NVIDIA NVLink/InfiniBand</td></tr>
    <tr><td>IP &amp; SerDes</td><td>200G+ SerDes, analog/optical (CPO) portfolio</td></tr>
    <tr><td>VMware annuity</td><td>~$27B/yr, ~78% op margin, recurring; funds capital return</td></tr>
    <tr><td>Capital discipline</td><td>Hock Tan playbook: acquire → raise margins → de-lever → grow dividend; ~$33B+ TTM FCF</td></tr>
  </tbody></table>
  <div class="source">Broadcom IR & earnings; CNBC (Anthropic, Dec 2025); product releases. Some customer details reported/rumored.</div>
</section>

<section id="s9" class="card p-5">
  <div class="slide-num">09 &middot; Peer set</div>
  <h2 class="slide-title">Semis cohort for the ~60%, an infrastructure-software anchor for the ~40%</h2>
  <div class="mt-4 space-y-3">
  {''.join(f'<div class="flex gap-3"><div class="tier-bar" style="background:{c};"></div><div class="flex-1"><div class="font-semibold" style="color:{c};">{t}</div><ul class="dot mt-1 text-sm">{"".join(f"<li>{i}</li>" for i in items)}</ul></div></div>'
    for t, items, c in [
      ("Closest competitor — custom silicon", ["Marvell (MRVL) — #2 custom-ASIC; Amazon Trainium, Microsoft Maia", "Cleanest read-through to AVGO's AI ASIC franchise"], "#CC0000"),
      ("Merchant-GPU benchmarks", ["NVIDIA (NVDA) — accelerator leader; the anchor multiple", "AMD (AMD) — #2 data-center GPU"], "#17365D"),
      ("Mature-semi capital-return refs", ["Qualcomm (QCOM) — value multiple, low AI-accelerator exposure", "Texas Instruments (TXN) — analog quality/dividend ref"], "#7F8C8D"),
      ("Software anchor (VMware ~40%)", ["Oracle (ORCL) — infra software, now AI-capex-driven", "Memo; excluded from semis stats"], "#2E7D32"),
    ])}
  </div>
  <div class="source">Stats computed over the 5 semis peers; ORCL is a software-anchor memo (you don't median a software multiple into a semis set).</div>
</section>

<section id="s10" class="card p-5">
  <div class="slide-num">10 &middot; Positioning</div>
  <h2 class="slide-title">NVDA scaled-and-fast; AVGO the scaled compounder; MRVL the high-beta proxy</h2>
  <img src="data:image/png;base64,{pos}" class="mt-4 rounded-lg border border-[var(--border)] w-full"/>
  <ul class="dot mt-3 text-sm">
    <li>NVIDIA: uniquely scaled AND +85% — vast profitability justifies a "low" P/E.</li>
    <li>AVGO: $68B at +29% with the best margin/FCF profile — a scaled compounder.</li>
    <li>Marvell: small but +28% and re-rating — high-beta way to play the ASIC theme.</li>
    <li>QCOM/TXN scaled but mature; Oracle the +22% software anchor.</li>
  </ul>
  <div class="source">Bubble = market cap; growth = MRQ YoY. Source: AVGO-Comps-Analysis.xlsx.</div>
</section>

<section id="s11" class="card p-5">
  <div class="slide-num">11 &middot; NVIDIA deep dive</div>
  <h2 class="slide-title">NVIDIA — the benchmark; scaled, hyper-profitable, (optically) not expensive</h2>
  <div class="l2 mt-4">
    <table><thead><tr><th>Metric</th><th class="num">Value</th></tr></thead><tbody>
      <tr><td>Market cap</td><td class="num">~$5.46T</td></tr><tr><td>TTM revenue</td><td class="num">~$253.5B</td></tr>
      <tr><td>MRQ growth</td><td class="num">+85%</td></tr><tr><td>Gross margin</td><td class="num">74.9%</td></tr>
      <tr><td>TTM EBITDA / margin</td><td class="num">~$174B / ~69%</td></tr><tr><td>Net income (TTM)</td><td class="num">~$160B</td></tr>
      <tr><td>P/E TTM / fwd</td><td class="num">~34x / ~26x</td></tr><tr><td>EV/EBITDA / EV/Rev</td><td class="num">~31x / ~21x</td></tr>
    </tbody></table>
    <div class="mt-4 lg:mt-0 text-sm">
      <div class="font-semibold" style="color:var(--navy);">Strengths</div>
      <ul class="dot mt-1"><li>~70%+ accelerator share</li><li>Profitability funds the R&D lead</li><li>Full-stack incl. CUDA moat</li></ul>
      <div class="font-semibold mt-2" style="color:var(--navy);">Weaknesses</div>
      <ul class="dot mt-1"><li>Custom-ASIC share shift is the structural threat</li><li>Customer concentration</li><li>China/export risk</li></ul>
      <div class="font-semibold mt-2" style="color:var(--navy);">Read-through to AVGO</div>
      <ul class="dot mt-1"><li>NVDA's "low" P/E caps what the market pays for AI compute — yet AVGO trades richer on fwd P/E despite slower growth.</li></ul>
    </div>
  </div>
  <div class="source">NVIDIA Q1 FY27 newsroom; Macrotrends; GuruFocus (~June 2026).</div>
</section>

<section id="s12" class="card p-5">
  <div class="slide-num">12 &middot; AMD + Marvell</div>
  <h2 class="slide-title">AMD (#2 GPU) and Marvell (closest custom-silicon comp)</h2>
  <div class="l2 mt-4 text-sm">
    <div><div class="font-semibold" style="color:var(--red);">AMD (AMD)</div>
    <ul class="dot mt-2"><li>Mkt cap ~$839B; TTM rev $37.5B (+38%)</li><li>Gross margin ~53%; NI ~$5.0B [E] GAAP</li><li>P/E TTM ~150–167x / fwd ~33x; EV/Rev ~22x</li><li><b>Read:</b> #2 merchant GPU; use EV/Rev + forward, not GAAP TTM</li></ul></div>
    <div class="mt-4 lg:mt-0"><div class="font-semibold" style="color:var(--red);">Marvell (MRVL)</div>
    <ul class="dot mt-2"><li>Mkt cap ~$192B (+51% on NVDA endorsement)</li><li>TTM rev ~$8.6B [E] (+28%); GM 52% GAAP</li><li>NI ~$0.3B GAAP [E] (amort-depressed); fwd P/E ~48x</li><li><b>Read:</b> closest AVGO ASIC comp; smaller, higher-beta</li></ul></div>
  </div>
  <div class="source">AMD Q1 2026 8-K; Marvell Q1 FY27 IR; StockAnalysis.com (~June 2026).</div>
</section>

<section id="s13" class="card p-5">
  <div class="slide-num">13 &middot; Qualcomm + TI</div>
  <h2 class="slide-title">Qualcomm &amp; Texas Instruments — mature-semi valuation anchors</h2>
  <div class="l2 mt-4 text-sm">
    <div><div class="font-semibold" style="color:#7F8C8D;">Qualcomm (QCOM)</div>
    <ul class="dot mt-2"><li>Mkt cap ~$215B; TTM rev ~$44.5B</li><li>MRQ ~-3%; EBITDA ~$14B (~31%)</li><li>P/E TTM ~20x / fwd ~14x (cheapest)</li><li><b>Read:</b> value/mature; limited AI-accelerator exposure</li></ul></div>
    <div class="mt-4 lg:mt-0"><div class="font-semibold" style="color:#7F8C8D;">Texas Instruments (TXN)</div>
    <ul class="dot mt-2"><li>Mkt cap ~$287B; TTM rev ~$18.4B</li><li>MRQ +19%; EBITDA ~$8.8B (~48%)</li><li>P/E TTM ~50x / fwd ~30x (trough earnings)</li><li><b>Read:</b> quality/dividend ref; capex-cycle trough multiples</li></ul></div>
  </div>
  <div class="source">Qualcomm Q2 FY26; TI Q1 2026; Macrotrends (~May–June 2026). QCOM TTM NI ex one-time tax benefit.</div>
</section>

<section id="s14" class="card p-5">
  <div class="slide-num">14 &middot; VMware vs Oracle</div>
  <h2 class="slide-title">The software side: VMware (within AVGO) vs Oracle — the ~40% the semis comps miss</h2>
  <table class="mt-4"><thead><tr><th>Dimension</th><th>AVGO Software (VMware)</th><th>Oracle (anchor)</th></tr></thead><tbody>
    <tr><td>Revenue</td><td>~$27B/yr</td><td>~$64.1B TTM (+22%)</td></tr>
    <tr><td>Profitability</td><td>~78% op margin</td><td>~48% EBITDA margin</td></tr>
    <tr><td>Growth</td><td>~+1% (margin story)</td><td>+22% (OCI +84%) AI-capex story</td></tr>
    <tr><td>Balance sheet</td><td>funded within AVGO; de-levering</td><td>~$96B net debt, rising</td></tr>
    <tr><td>Multiple lens</td><td>annuity / FCF</td><td>EV/Rev ~12x (growth premium)</td></tr>
  </tbody></table>
  <ul class="dot mt-3 text-sm">
    <li>ORCL is the best large-cap anchor but imperfect — now an AI-datacenter capex story, whereas VMware is a low-growth ~78%-margin annuity.</li>
    <li>Value VMware as an FCF annuity, not on ORCL's growth multiple; it's the low-volatility ballast under the AI option.</li>
  </ul>
  <div class="source">Broadcom Q1 FY26 (software); Oracle Q3 FY26; Futurum; Macrotrends.</div>
</section>

<section id="s15" class="card p-5">
  <div class="slide-num">15 &middot; Scoreboard</div>
  <h2 class="slide-title">AVGO leads on margin/FCF quality; NVDA on growth; AVGO richest on forward P/E</h2>
  <div class="overflow-x-auto"><table class="mt-4" style="min-width:720px;">
    <thead><tr><th>Dimension</th><th>AVGO</th><th>NVDA</th><th>AMD</th><th>MRVL</th><th>QCOM</th><th>TXN</th></tr></thead><tbody>
    <tr><td>Revenue scale</td><td>●●○ $68B</td><td>●●● $254B</td><td>●○○ $37B</td><td>●○○ $9B</td><td>●●○ $44B</td><td>●○○ $18B</td></tr>
    <tr><td>Growth (MRQ)</td><td>●●○ +29%</td><td>●●● +85%</td><td>●●○ +38%</td><td>●●○ +28%</td><td>●○○ -3%</td><td>●○○ +19%</td></tr>
    <tr><td>AI exposure</td><td>●●● ASIC+net</td><td>●●● GPU</td><td>●●○ #2 GPU</td><td>●●● ASIC#2</td><td>●○○ edge</td><td>●○○ content</td></tr>
    <tr><td>Margin / FCF</td><td>●●● 68%</td><td>●●● 69%</td><td>●○○ 22%</td><td>●●○ ~31%</td><td>●●○ 31%</td><td>●●● 48%</td></tr>
    <tr><td>Balance sheet</td><td>●●○ $52B nd</td><td>●●● net cash</td><td>●●● net cash</td><td>●●○ $1.4B</td><td>●●○ $5.5B</td><td>●●○ $8B</td></tr>
    <tr><td>Value (fwd P/E)</td><td>●○○ ~31x</td><td>●●○ ~26x</td><td>●○○ ~33x</td><td>●○○ ~48x</td><td>●●● ~14x</td><td>●●○ ~30x</td></tr>
  </tbody></table></div>
  <div class="source">● stronger / ○ weaker (higher fwd P/E = weaker value). Calibrated to AVGO-Comps-Analysis.xlsx.</div>
</section>

<section id="s16" class="card p-5">
  <div class="slide-num">16 &middot; Valuation — football field</div>
  <h2 class="slide-title">Every method puts fair value at or below the $482 market price</h2>
  <img src="data:image/png;base64,{fb}" class="mt-4 rounded-lg border border-[var(--border)] w-full"/>
  <ul class="dot mt-3 text-sm">
    <li>DCF base ($264) and the full WACC×g grid ($200–311) sit well below $482.</li>
    <li>Comps (semis-median EV/EBITDA & fwd P/E) imply ~$300–480 — AVGO already trades at/above the cohort.</li>
    <li>Only the DCF bull case (mgmt FY27 AI fully delivered) reaches the $482 zone.</li>
    <li><b>Conclusion:</b> even after Q2 +48% & Q3 guide +84%, the market still prices the bull case as the base case.</li>
  </ul>
  <div class="source">Combines DCF (AVGO-Model.xlsx) and comps (AVGO-Comps-Analysis.xlsx). Ranges illustrative of method spread.</div>
</section>

<section id="s17" class="card p-5">
  <div class="slide-num">17 &middot; Valuation — DCF + sensitivity</div>
  <h2 class="slide-title">Base-case DCF $264/share; the entire WACC × growth grid is below $482</h2>
  <div class="l2 mt-4">
    <table><thead><tr><th>DCF bridge (base)</th><th class="num">$M / $</th></tr></thead><tbody>
      <tr><td>PV of explicit FCF (FY26–30)</td><td class="num">253,310</td></tr>
      <tr><td>PV of explicit FCF (FY26–30)</td><td class="num">269,084</td></tr>
      <tr><td>PV of terminal value</td><td class="num">1,030,519</td></tr>
      <tr><td>Enterprise value</td><td class="num">1,299,603</td></tr>
      <tr><td>(–) Net debt</td><td class="num">(49,000)</td></tr>
      <tr><td>Equity value</td><td class="num">1,162,812</td></tr>
      <tr><td>÷ Diluted shares (M)</td><td class="num">4,730</td></tr>
      <tr><td><b>Implied value / share</b></td><td class="num"><b>$264.40</b></td></tr>
      <tr><td>Current price</td><td class="num">$481.62</td></tr>
      <tr><td>Upside / (downside)</td><td class="num" style="color:var(--bad);">(45.1%)</td></tr>
    </tbody></table>
    <div class="mt-4 lg:mt-0">
      <div class="font-semibold text-sm" style="color:var(--navy);">Sensitivity — implied $/share (WACC × terminal g)</div>
      <table class="mt-2"><thead><tr><th>WACC↓ / g→</th><th class="num">2.5%</th><th class="num">3.0%</th><th class="num">3.5%</th><th class="num">4.0%</th><th class="num">4.5%</th></tr></thead><tbody>
        <tr><td>8.5%</td><td class="num">275</td><td class="num">296</td><td class="num">323</td><td class="num">355</td><td class="num">395</td></tr>
        <tr><td>9.0%</td><td class="num">252</td><td class="num">270</td><td class="num">291</td><td class="num">317</td><td class="num">348</td></tr>
        <tr><td><b>9.5% (base)</b></td><td class="num">232</td><td class="num">247</td><td class="num" style="background:#BDD7EE;font-weight:700;">265</td><td class="num">286</td><td class="num">311</td></tr>
        <tr><td>10.0%</td><td class="num">215</td><td class="num">228</td><td class="num">243</td><td class="num">260</td><td class="num">281</td></tr>
        <tr><td>10.5%</td><td class="num">200</td><td class="num">211</td><td class="num">224</td><td class="num">239</td><td class="num">256</td></tr>
      </tbody></table>
      <ul class="dot mt-2 text-sm"><li>Terminal value ~79% of EV — very sensitive to WACC/g.</li><li>Even the best corner (8.5%/4.5%) = $395 on base FCF; reaching $482 needs FCF above base (mgmt FY27 AI delivered).</li></ul>
    </div>
  </div>
  <div class="source">AVGO-Model.xlsx (validated, 0 formula errors). Base haircuts mgmt FY27 AI guidance ~24% for execution / OpenAI-financing risk.</div>
</section>

<section id="s18" class="card p-5">
  <div class="slide-num">18 &middot; Synthesis &amp; moats</div>
  <h2 class="slide-title">Moat: design lock-in + IP + FCF · Risk: concentration + valuation</h2>
  <div class="overflow-x-auto"><table class="mt-4" style="min-width:640px;">
    <thead><tr><th>Moat type</th><th>AVGO</th><th>NVDA</th><th>MRVL</th><th>Reading</th></tr></thead><tbody>
    <tr><td>Switching costs</td><td><b>Strong</b></td><td>Strong</td><td>Mod</td><td>Chip re-spin + VMware lock-in are sticky</td></tr>
    <tr><td>Intangibles (IP)</td><td><b>Strong</b></td><td>Strong</td><td>Mod</td><td>SerDes/optical/analog; CUDA is NVDA's equivalent</td></tr>
    <tr><td>Scale economies</td><td><b>Strong</b></td><td>Strong</td><td>Weak</td><td>AVGO + NVDA dominate R&D/supply scale</td></tr>
    <tr><td>Network effects</td><td>Weak</td><td><b>Strong</b></td><td>Weak</td><td>CUDA ecosystem is the real network effect</td></tr>
    <tr><td>Capital discipline</td><td><b>Strong</b></td><td>Mod</td><td>Mod</td><td>Hock Tan FCF + de-levering playbook</td></tr>
  </tbody></table></div>
  <div class="mt-3 text-sm">
    <p><b>Durable advantages:</b> ~70% custom-ASIC design share with multi-gen lock-in; leading open-Ethernet AI networking; ~$27B/yr ~78%-margin VMware annuity funding capital return.</p>
    <p class="mt-1"><b>Vulnerabilities:</b> AI revenue concentrated in a few hyperscaler programs (OpenAI financing snag live); Google multi-sourcing dilutes content; valuation leaves no margin of safety — $482 already prices the bull ramp.</p>
  </div>
</section>

<section id="s19" class="card p-5">
  <div class="slide-num">19 &middot; Bull / base / bear</div>
  <h2 class="slide-title">Anchored to the DCF: the market price embeds the bull case</h2>
  <table class="mt-4"><thead><tr><th>Scenario</th><th class="num">Prob.</th><th>Key drivers</th><th>DCF value</th></tr></thead><tbody>
    <tr><td><span class="pill pill-good">Bull</span></td><td class="num">30%</td><td>Mgmt $100B+ FY27 AI delivered & sustained; OpenAI funded; WACC ~8.5%, g ~4.5%</td><td>~$480–540 — justifies/exceeds $482</td></tr>
    <tr><td><span class="pill pill-navy">Base</span></td><td class="num">45%</td><td>AI FY27 ~$85B (guidance haircut ~15%, post-Q2); software steady; WACC 9.5%, g 3.5%</td><td>~$264 — ~45% below price</td></tr>
    <tr><td><span class="pill pill-bad">Bear</span></td><td class="num">25%</td><td>AI digestion 2027–28; OpenAI stalls; Google re-sourcing; WACC ~10.5%, g ~2.5%</td><td>~$200–225</td></tr>
  </tbody></table>
  <div class="mt-3 text-sm"><div class="font-semibold" style="color:var(--navy);">Signposts</div>
  <ol class="mt-1 pl-5 list-decimal"><li>OpenAI $18B financing structure resolved or not</li><li>Q2/Q3 FY26 AI revenue vs the $10.7B→ramp guide</li><li>Hyperscaler 2027 capex guidance (acceleration vs digestion)</li><li>Any Google/Meta program re-sourcing</li></ol></div>
  <div class="source">Probabilities are author's judgment, not consensus. DCF values from AVGO-Model.xlsx sensitivity + bull-FCF overlay.</div>
</section>

<section id="s20" class="card p-5">
  <div class="slide-num">20 &middot; Decision &amp; sources</div>
  <h2 class="slide-title">Decision frame &amp; sources</h2>
  <div class="mt-4 space-y-3 text-sm">
    <div><span class="pill pill-navy">Own quality, wait for a pullback</span><p class="mt-1">No margin of safety at $482. Accumulate toward the base-case zone (high-$200s–low-$300s) or on AI-digestion scares.</p></div>
    <div><span class="pill pill-red">Pair: long AVGO / short a richer AI name</span><p class="mt-1">Express the quality view while hedging the AI-multiple on relative valuation.</p></div>
    <div><span class="pill pill-warn">Play the theme via MRVL</span><p class="mt-1">Same custom-ASIC thesis with more torque (and risk); smaller, re-rating name.</p></div>
    <div><span class="pill pill-bad">Trim / avoid here</span><p class="mt-1">If you expect 2027–28 AI digestion + OpenAI-financing risk, the price already discounts the bull case.</p></div>
  </div>
  <div class="source">AVGO Q1 FY26 & FY23–25 SEC filings/IR; peer 10-Q/IR; StockAnalysis/GuruFocus/Macrotrends (~June 2026); CNBC, The Information, Goldman, Dell'Oro, Allianz. MCP terminals NOT configured — public sources, [E] flags in workbooks. AI/non-AI split partly estimated. Research only — NOT investment advice.</div>
</section>

</main>
<footer class="bg-[var(--navy)] text-white py-6 mt-8"><div class="max-w-3xl mx-auto px-5 text-xs opacity-80 flex justify-between flex-wrap gap-2">
  <span>Broadcom (AVGO) competitive analysis &amp; valuation · June 2026 · sourced public data</span>
  <span>Research only — not investment advice</span>
</div></footer>
</body></html>"""

OUT = HERE / "AVGO-Competitive-Analysis.html"
OUT.write_text(HTML, encoding="utf-8")
print(f"Wrote {OUT} ({len(HTML):,} bytes)")
