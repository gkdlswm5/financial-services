"""
Build QNT-Competitive-Analysis.html — tablet-friendly single-file HTML view
of the Quantinuum (QNT) analysis. Charts embedded as base64 PNG.
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
CHARTS = HERE / "charts"
OUT = HERE / "QNT-Competitive-Analysis.html"


def b64png(path):
    return base64.b64encode(Path(path).read_bytes()).decode("ascii")


revenue_b64 = b64png(CHARTS / "revenue_ramp.png")
ff_b64 = b64png(CHARTS / "football_field.png")
modality_b64 = b64png(CHARTS / "modality_2x2.png")
tam_b64 = b64png(CHARTS / "tam.png")
riken_b64 = b64png(CHARTS / "riken_cliff.png")


HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Quantinuum (QNT) — Competitive Analysis & Dual-DCF</title>
<style>
  :root {{
    --navy:#17365D; --mid:#4472C4; --light:#D9E1F2;
    --grey:#595959; --bg:#FAFAFA; --red:#C0392B; --green:#2E8640;
    --orange:#ED7D31;
  }}
  * {{ box-sizing:border-box; }}
  body {{
    font-family: "Times New Roman", Georgia, serif;
    margin:0; padding:0; background:var(--bg);
    color:var(--navy); line-height:1.5;
  }}
  header {{
    background:var(--navy); color:white; padding:24px 32px;
    border-bottom: 4px solid var(--mid);
  }}
  header h1 {{ margin:0; font-size:32px; font-weight:bold; }}
  header .subt {{ margin-top:6px; font-size:14px; color:var(--light); }}
  nav {{
    position:sticky; top:0; background:white; border-bottom:1px solid #ddd;
    padding:10px 32px; z-index:10; font-size:12px;
  }}
  nav a {{ color:var(--navy); text-decoration:none; margin-right:14px;
          padding:4px 8px; border-radius:3px; }}
  nav a:hover {{ background:var(--light); }}
  main {{ max-width:1080px; margin:0 auto; padding:24px 32px; }}
  section {{
    background:white; padding:24px 28px; margin-bottom:20px;
    border-left: 4px solid var(--navy);
    border-radius: 3px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04);
  }}
  section h2 {{
    margin-top:0; color:var(--navy); font-size:22px;
    border-bottom: 2px solid var(--light); padding-bottom:8px;
  }}
  section h3 {{ color:var(--navy); font-size:16px; margin-top:18px; }}
  .callout {{
    background:var(--light); padding:14px 18px; border-radius:3px;
    font-size:15px; margin:12px 0;
  }}
  .callout.warn {{ background:#fce4e4; border-left:3px solid var(--red); }}
  .callout.ok {{ background:#e2efda; border-left:3px solid var(--green); }}
  .callout.note {{ background:#fff3cd; border-left:3px solid var(--orange); }}
  table {{
    width:100%; border-collapse:collapse; margin:14px 0;
    font-size:13px;
  }}
  th, td {{
    text-align:left; padding:8px 10px; border-bottom:1px solid #ddd;
  }}
  th {{ background:var(--navy); color:white; font-weight:bold; }}
  tr:nth-child(even) td {{ background:#f5f5f5; }}
  .num {{ text-align:right; font-variant-numeric:tabular-nums; }}
  .red {{ color:var(--red); font-weight:bold; }}
  .green {{ color:var(--green); font-weight:bold; }}
  .orange {{ color:var(--orange); font-weight:bold; }}
  img.chart {{
    max-width:100%; height:auto; display:block; margin:14px auto;
    border:1px solid #ddd;
  }}
  .two-col {{ display:grid; grid-template-columns:1fr 1fr; gap:18px; }}
  .badge {{
    display:inline-block; padding:2px 8px; background:var(--mid);
    color:white; border-radius:3px; font-size:11px; margin-right:6px;
  }}
  footer {{
    text-align:center; color:var(--grey); padding:24px;
    font-size:11px; border-top:1px solid #ddd; background:white;
  }}
  @media (max-width: 740px) {{
    main {{ padding:14px 12px; }}
    section {{ padding:14px 16px; }}
    nav {{ padding:8px 14px; font-size:11px; overflow-x:auto;
           white-space:nowrap; }}
    .two-col {{ grid-template-columns:1fr; }}
    header {{ padding:18px 16px; }}
    header h1 {{ font-size:22px; }}
  }}
</style>
</head>
<body>
<header>
  <h1>Quantinuum Inc. (NASDAQ: QNT)</h1>
  <div class="subt">Competitive analysis, peer comps, dual-DCF valuation — June 4, 2026</div>
  <div class="subt">Priced $60 (above $53-55 range), trading $68, $1.68B raised, ~20x oversubscribed</div>
</header>

<nav>
  <a href="#exec">1. Executive summary</a>
  <a href="#ipo">2. IPO event</a>
  <a href="#profile">3. Company profile</a>
  <a href="#tam">4. TAM</a>
  <a href="#peers">5. Peer set</a>
  <a href="#tech">6. Tech scoreboard</a>
  <a href="#riken">7. RIKEN cliff</a>
  <a href="#rev">8. Revenue build</a>
  <a href="#ff">9. Football field</a>
  <a href="#dcf">10. Dual DCF</a>
  <a href="#scenarios">11. Bull/base/bear</a>
  <a href="#decision">12. Decision + HON</a>
</nav>

<main>

<section id="exec">
<h2>1. Executive summary</h2>
<div class="callout">
  <strong>$68 ≈ 2.75× our traditional DCF and ≈ 2.34× the FY35 revenue we model in base case.</strong>
  Stock prices a <strong>15.4% share of the 2035 quantum-computing TAM</strong>. Achievable, but the bar is high.
</div>

<div class="two-col">
  <div>
    <h3>Framework 1 — Traditional DCF (intrinsic)</h3>
    <table>
      <tr><th>Line</th><th class="num">Value</th></tr>
      <tr><td>WACC</td><td class="num">15.85%</td></tr>
      <tr><td>Terminal growth</td><td class="num">4.0%</td></tr>
      <tr><td>Sum PV(FCF) FY26E-FY35E</td><td class="num">$1,372M</td></tr>
      <tr><td>Terminal value</td><td class="num">$11,472M</td></tr>
      <tr><td>PV of terminal value</td><td class="num">$2,835M</td></tr>
      <tr><td>Enterprise value</td><td class="num">$4,207M</td></tr>
      <tr><td>+ Cash post-IPO</td><td class="num">$2,080M</td></tr>
      <tr><td>Equity value</td><td class="num">$6,287M</td></tr>
      <tr><td>Implied price / share</td><td class="num red">$24.76</td></tr>
      <tr><td>Current price</td><td class="num">$68.00</td></tr>
      <tr><td><strong>Premium to intrinsic</strong></td><td class="num red"><strong>+175%</strong></td></tr>
    </table>
  </div>
  <div>
    <h3>Framework 2 — Reverse-engineered to $68</h3>
    <table>
      <tr><th>Line</th><th class="num">Value</th></tr>
      <tr><td>Market cap (FD)</td><td class="num">$17,265M</td></tr>
      <tr><td>− Cash</td><td class="num">$2,080M</td></tr>
      <tr><td>= EV (today)</td><td class="num">$15,185M</td></tr>
      <tr><td>Assumed mature EV/Rev (FY35)</td><td class="num">8.0×</td></tr>
      <tr><td>Discount factor (9.5 yrs)</td><td class="num">4.16×</td></tr>
      <tr><td>Implied FY35E revenue</td><td class="num orange">$7,680M</td></tr>
      <tr><td>Model FY35E revenue</td><td class="num">$3,280M</td></tr>
      <tr><td>Gap (implied / model)</td><td class="num orange">+134%</td></tr>
      <tr><td>Implied 2035 QC TAM share</td><td class="num">15.4%</td></tr>
      <tr><td><strong>Required 10-yr CAGR</strong></td><td class="num orange"><strong>~75%</strong></td></tr>
    </table>
  </div>
</div>

<div class="callout note">
  <strong>Decision call:</strong> HOLD with downside skew at $68.
  Buy zone &lt;$45 (peer-median footing).
  First major catalyst is the Q2'26 print (Aug 2026) — RIKEN-cliff visibility, Helios ramp narrative.
</div>
</section>

<section id="ipo">
<h2>2. The IPO event — June 3, 2026</h2>
<div class="two-col">
  <div>
    <h3>Mechanics</h3>
    <table>
      <tr><td>Initial range (filed)</td><td class="num">$45–50</td></tr>
      <tr><td>Revised range (May 26)</td><td class="num">$53–55</td></tr>
      <tr><td>Final priced (Jun 3)</td><td class="num green">$60.00 — above range</td></tr>
      <tr><td>Shares offered</td><td class="num">28,000,000 (upsized from 21M)</td></tr>
      <tr><td>Gross proceeds</td><td class="num">$1.68B</td></tr>
      <tr><td>Underwriters</td><td>JPM, MS, Jefferies, Evercore</td></tr>
      <tr><td>Oversubscription</td><td class="num green">~20× reported</td></tr>
      <tr><td>Day-1 open</td><td class="num green">$68.00 (+13.3%)</td></tr>
      <tr><td>Post-money mkt cap (FD)</td><td class="num">~$15.6B</td></tr>
      <tr><td>Public float</td><td class="num red">~8.3% (very thin)</td></tr>
    </table>
  </div>
  <div>
    <h3>Cap table post-IPO (voting)</h3>
    <ul>
      <li><strong>Honeywell:</strong> ~48.1% voting power
        <br>+ Transaction Committee veto on M&amp;A &gt; $10M
        <br>+ Operating supplier ("H2 powered by Honeywell")
      </li>
      <li><strong>Cambridge Quantum Holdings:</strong> ~32.5% voting
        <br>Aggregates founder Ilyas Khan (~23%), IBM, JSR
      </li>
      <li><strong>Combined insiders:</strong> ~82% voting power</li>
      <li><strong>Public float:</strong> ~8.3% economic, similar voting</li>
    </ul>
    <div class="callout warn">
      <strong>Risk flag:</strong> 8.3% float makes QNT susceptible to high volatility
      and potential short-squeeze-style moves. Add gradually if accumulating.
    </div>
  </div>
</div>
</section>

<section id="profile">
<h2>3. Company profile + Honeywell parent angle</h2>
<div class="two-col">
  <div>
    <h3>Quantinuum Inc.</h3>
    <ul>
      <li>CEO: Ilyas Khan (ex-Cambridge Quantum founder)</li>
      <li>HQ: Cambridge UK + Broomfield CO</li>
      <li>Modality: trapped-ion (QCCD architecture)</li>
      <li>System generations: H1 → H2 → <strong>Helios</strong> → Sol → Apollo</li>
    </ul>
    <h3>Funding history</h3>
    <table>
      <tr><th>Date</th><th>Round</th><th class="num">Valuation</th></tr>
      <tr><td>Nov '21</td><td>HON-CQ merger</td><td class="num">~$3B</td></tr>
      <tr><td>Jan '24</td><td>$300M (JPMC)</td><td class="num">$5B pre</td></tr>
      <tr><td>Sep '25</td><td>$600M (NVIDIA+)</td><td class="num">$10B pre</td></tr>
      <tr><td>Jun '26</td><td>IPO at $60</td><td class="num">~$15.6B post</td></tr>
    </table>
    <h3>Financials (S-1)</h3>
    <table>
      <tr><th></th><th class="num">FY24</th><th class="num">FY25</th><th class="num">Q1'26</th></tr>
      <tr><td>Revenue</td><td class="num">$23.0M</td><td class="num">$30.9M</td><td class="num">$5.2M</td></tr>
      <tr><td>Net loss</td><td class="num red">($144M)</td><td class="num red">($193M)</td><td class="num red">($137M)</td></tr>
    </table>
  </div>
  <div>
    <h3>Honeywell parent angle (NYSE: HON)</h3>
    <ul>
      <li><strong>Pre-IPO ownership:</strong> ~54%</li>
      <li><strong>Post-IPO voting power:</strong> ~48.1%</li>
      <li><strong>QNT stake at $68:</strong> ~$7.5B (~122M shares × $68)</li>
      <li><strong>HON market cap:</strong> ~$138B</li>
      <li><strong>QNT % of HON value:</strong> ~5.4%</li>
    </ul>
    <h3>HON SOTP build</h3>
    <table>
      <tr><th>Segment</th><th class="num">FY25 rev</th><th class="num">EV</th></tr>
      <tr><td>Aerospace Tech</td><td class="num">$15.8B</td><td class="num">~$80B</td></tr>
      <tr><td>Industrial Auto</td><td class="num">$9.2B</td><td class="num">~$35B</td></tr>
      <tr><td>Building Auto</td><td class="num">$6.1B</td><td class="num">~$22B</td></tr>
      <tr><td>Energy &amp; Sustain.</td><td class="num">$7.4B</td><td class="num">~$18B</td></tr>
      <tr><td>QNT stake (48%)</td><td class="num">—</td><td class="num green">~$7.5B</td></tr>
      <tr><td>Net cash / other</td><td class="num">—</td><td class="num">$(15B)</td></tr>
      <tr><td><strong>Total EV</strong></td><td class="num">—</td><td class="num"><strong>~$147B</strong></td></tr>
      <tr><td><strong>Implied HON share</strong></td><td class="num">—</td><td class="num green"><strong>~$226</strong></td></tr>
      <tr><td>Current HON price</td><td class="num">—</td><td class="num">~$213 [E]</td></tr>
    </table>
    <div class="callout ok">
      QNT IPO adds ~$5/share to HON SOTP (~2.4%).
      Modest positive catalyst for HON shareholders, not transformative.
    </div>
  </div>
</div>
</section>

<section id="tam">
<h2>4. Quantum computing TAM</h2>
<img class="chart" src="data:image/png;base64,{tam_b64}" alt="TAM chart">
<div class="two-col">
  <div>
    <h3>McKinsey QTM 2026 (May 2026 update)</h3>
    <ul>
      <li>Global quantum tech market: <strong>$60-100B by 2035</strong></li>
      <li>Quantum computing specifically: <strong>$43-71B by 2035</strong></li>
      <li>Total downstream economic value: ~$2.7T by 2035</li>
      <li>QC market: $1-1.5B (2025) → $4-5B (2028) → step-function 2030+</li>
    </ul>
  </div>
  <div>
    <h3>BCG (Jul 2024)</h3>
    <ul>
      <li>Total economic value: <strong>$450-850B by 2040</strong></li>
      <li>Sustaining HW + SW vendor market: <strong>$90-170B by 2040</strong></li>
      <li>Split ~50/50 hardware/software in BCG framing [E]</li>
    </ul>
    <div class="callout note">
      For our reverse-engineered DCF we use <strong>$50B</strong> (McKinsey midpoint, 2035).
      The wider risk is mistaking "value created" ($2.7T downstream) for "value captured" (vendor margin).
    </div>
  </div>
</div>
</section>

<section id="peers">
<h2>5. Peer set & multiples</h2>
<table>
  <tr><th>Ticker</th><th>Modality</th><th class="num">Mkt cap</th><th class="num">EV</th><th class="num">FY25 rev</th><th class="num">Q1'26 YoY</th><th class="num">EV/FY25</th><th class="num">EV/TTM</th></tr>
  <tr><td><strong>QNT</strong></td><td>Trapped-ion</td><td class="num">$17.3B</td><td class="num">$15.2B</td><td class="num">$30.9M</td><td class="num">—</td><td class="num"><strong>~491×</strong></td><td class="num"><strong>~466×</strong></td></tr>
  <tr><td>IONQ</td><td>Trapped-ion</td><td class="num">$25.5B</td><td class="num">$22.4B</td><td class="num">$130.0M</td><td class="num green">+755%</td><td class="num">~172×</td><td class="num">~120×</td></tr>
  <tr><td>RGTI</td><td>Superconducting</td><td class="num">$7.8B</td><td class="num">$7.3B</td><td class="num">$7.1M</td><td class="num green">+199%</td><td class="num">~1,023×</td><td class="num">~726×</td></tr>
  <tr><td>QBTS</td><td>Annealing</td><td class="num">$10.0B</td><td class="num">$9.4B</td><td class="num">$24.6M</td><td class="num red">−81%</td><td class="num">~383×</td><td class="num">~754×</td></tr>
  <tr><td>HON (memo)</td><td>Conglomerate</td><td class="num">$138B</td><td class="num">$149B</td><td class="num">$38,500M</td><td class="num">+4%</td><td class="num">~3.9×</td><td class="num">~3.9×</td></tr>
</table>

<img class="chart" src="data:image/png;base64,{modality_b64}" alt="Modality 2x2">

<div class="callout">
<ul>
  <li>IONQ is the direct comp (trapped-ion, similar TAM) — but has 6× QNT's revenue base and 7.5× the YoY growth rate.</li>
  <li>QNT trades at <strong>+28% premium</strong> to peer median on FY25, but at <strong>−36% discount</strong> on TTM.</li>
  <li>The "QNT is rich vs peers" narrative is wrong overall — it's only true vs IONQ specifically.</li>
</ul>
</div>
</section>

<section id="tech">
<h2>6. Technology scoreboard</h2>
<table>
<tr><th></th><th>QNT (Helios)</th><th>IONQ (Tempo)</th><th>RGTI (Cepheus)</th><th>IBM (QS2)</th><th>Google (Willow)</th></tr>
<tr><td>Modality</td><td>Trapped-ion</td><td>Trapped-ion</td><td>Superconducting</td><td>Superconducting</td><td>Superconducting</td></tr>
<tr><td>Physical qubits</td><td>98</td><td>64+ AQ</td><td>108</td><td>1,121 (Condor)</td><td>105 (Willow)</td></tr>
<tr><td>2Q gate fidelity</td><td class="green">99.921%</td><td>99.99% (lab)</td><td>99.1%</td><td>~99.5%</td><td class="green">99.4%</td></tr>
<tr><td>Connectivity</td><td class="green">All-to-all</td><td>All-to-all</td><td>Limited</td><td>Heavy hex</td><td>2D grid</td></tr>
<tr><td>Quantum Volume</td><td class="green">2^25 (33M)</td><td>n/d</td><td>n/d</td><td>1024+</td><td>n/d</td></tr>
<tr><td>Logical qubits demoed</td><td class="green">12 (w/ MSFT)</td><td>0 (lab)</td><td>1</td><td>1</td><td class="green">Below threshold</td></tr>
<tr><td>FTQC target year</td><td>2029 (Apollo)</td><td>2028 functional</td><td>Unclear</td><td>Beyond 2030</td><td>Beyond 2030</td></tr>
<tr><td>Latest system launch</td><td>Helios (Nov '25)</td><td>Forte/Tempo ('26)</td><td>Cepheus-108Q (Apr '26)</td><td>Quantum System 2</td><td>Research only</td></tr>
</table>
<div class="callout ok">
  QNT's edge is logical qubits demoed (12 with Microsoft) — closest to commercial fault-tolerance.
  QNT roadmap to Apollo (2029) is the most aggressive timeline to fault-tolerant universal QC of any public pure-play.
</div>
</section>

<section id="riken">
<h2>7. RIKEN concentration cliff</h2>
<img class="chart" src="data:image/png;base64,{riken_b64}" alt="RIKEN concentration">
<div class="two-col">
  <div>
    <h3>What happened</h3>
    <ul>
      <li>RIKEN bought a QNT on-prem system — lumpy hardware delivery + ongoing maintenance</li>
      <li>Q1'26: install complete, dropped to 7% of revenue</li>
      <li>Helios was designed to fill the gap; launched Nov 2025; launch customers ramping in 2H'26</li>
    </ul>
  </div>
  <div>
    <h3>Risk vs mitigant</h3>
    <ul>
      <li><strong>Risk:</strong> Q2/Q3 '26 prints could show revenue decline YoY before Helios ramp — market may react harshly to QNT's first quarter as a public company.</li>
      <li><strong>Mitigants:</strong> Quantum Origin SaaS (recurring), Helios cloud/on-prem expanding, $100M CHIPS Act LOI (govt).</li>
    </ul>
  </div>
</div>
</section>

<section id="rev">
<h2>8. Revenue build — 4 streams</h2>
<img class="chart" src="data:image/png;base64,{revenue_b64}" alt="Revenue ramp">
<table>
<tr><th>FY (E)</th><th class="num">RIKEN</th><th class="num">Helios</th><th class="num">SaaS</th><th class="num">Govt</th><th class="num">Total</th></tr>
<tr><td>FY26E</td><td class="num">4</td><td class="num">22</td><td class="num">8</td><td class="num">6</td><td class="num"><strong>40</strong></td></tr>
<tr><td>FY27E</td><td class="num">2</td><td class="num">75</td><td class="num">16</td><td class="num">12</td><td class="num"><strong>105</strong></td></tr>
<tr><td>FY28E</td><td class="num">1</td><td class="num">180</td><td class="num">32</td><td class="num">20</td><td class="num"><strong>233</strong></td></tr>
<tr><td>FY29E</td><td class="num">1</td><td class="num">350</td><td class="num">60</td><td class="num">30</td><td class="num"><strong>441</strong></td></tr>
<tr><td>FY30E</td><td class="num">0</td><td class="num">580</td><td class="num">100</td><td class="num">45</td><td class="num"><strong>725</strong></td></tr>
<tr><td>FY35E</td><td class="num">0</td><td class="num">2,480</td><td class="num">600</td><td class="num">200</td><td class="num green"><strong>3,280</strong></td></tr>
</table>
<div class="callout">
  Implied 2035 QC market share at base case: ~6.6% of $50B McKinsey midpoint TAM.
  10-yr CAGR (FY25 → FY35): ~60%.
</div>
</section>

<section id="ff">
<h2>9. Football field — implied valuation</h2>
<img class="chart" src="data:image/png;base64,{ff_b64}" alt="Football field">
<div class="two-col">
  <div>
    <h3>Methodology ranges</h3>
    <ul>
      <li><strong>Traditional DCF:</strong> $18-38 (mid $25) — honest intrinsic</li>
      <li><strong>IONQ-anchored:</strong> $45-55 (applies IONQ ~172× FY25)</li>
      <li><strong>Peer median:</strong> $50-62</li>
      <li><strong>Reverse-engineered:</strong> $55-85 ($50B TAM + 12% share)</li>
      <li><strong>Bull case:</strong> $75-135 (McKinsey high + Apollo execution)</li>
      <li><strong>QBTS-anchored:</strong> $110-165 (distorted by tiny denominator)</li>
    </ul>
  </div>
  <div>
    <h3>Read</h3>
    <ul>
      <li>$68 trades <strong>below peer median</strong> (~$56) — peer story isn't expensive</li>
      <li>$68 trades <strong>well above intrinsic DCF</strong> ($25) — optionality story IS rich</li>
      <li>The gap between $25 (intrinsic) and $68 (price) IS the option premium for Apollo (FTQC)</li>
      <li>If Apollo slips by 12+ months, the gap collapses fast</li>
    </ul>
  </div>
</div>
</section>

<section id="scenarios">
<h2>11. Bull / Base / Bear scenarios</h2>
<table>
<tr><th></th><th>Bull ($110+)</th><th>Base ($60-75)</th><th>Bear ($25-45)</th></tr>
<tr><td>FY30E revenue</td><td class="num green">$1.0B+</td><td class="num">$725M</td><td class="num red">$300-450M</td></tr>
<tr><td>FY35E revenue</td><td class="num green">$5.5B+</td><td class="num">$3.3B</td><td class="num red">$1.5-2.0B</td></tr>
<tr><td>2035 QC market share</td><td class="num green">~11%</td><td class="num">~6.6%</td><td class="num red">~3-4%</td></tr>
<tr><td>FCF crossover year</td><td class="green">2028</td><td>2029</td><td class="red">2031+</td></tr>
<tr><td>Helios ramp</td><td class="green">Beats launch guidance</td><td>Meets guidance</td><td class="red">Slips 6-12 mo</td></tr>
<tr><td>Sol (2027)</td><td class="green">On time, 192q full</td><td>On time mostly</td><td class="red">Slips to 2028</td></tr>
<tr><td>Apollo (2029) FTQC</td><td class="green">On time, demoed</td><td>Slips ~6 mo</td><td class="red">Slips &gt;12 mo</td></tr>
<tr><td>Macro</td><td>Rate cuts; ERP↓</td><td>Stable rates</td><td class="red">Recession</td></tr>
<tr><td>HON sells down</td><td>Orderly secondary</td><td>Held through 2027</td><td class="red">Forced sale overhang</td></tr>
</table>
</section>

<section id="decision">
<h2>12. Decision + Honeywell SOTP</h2>
<div class="two-col">
  <div>
    <h3>QNT decision matrix</h3>
    <table>
      <tr><th class="num">Price</th><th>Read</th><th>Action</th></tr>
      <tr><td class="num">$25-35</td><td>Trades to intrinsic DCF</td><td class="green"><strong>BUY</strong></td></tr>
      <tr><td class="num">$35-50</td><td>Below peer median</td><td class="green"><strong>BUY ↓</strong></td></tr>
      <tr><td class="num">$50-65</td><td>Peer-median footing</td><td class="green"><strong>BUY ↓</strong></td></tr>
      <tr><td class="num">$65-80</td><td class="orange"><strong>CURRENT — optionality priced</strong></td><td class="orange"><strong>HOLD</strong></td></tr>
      <tr><td class="num">$80-100</td><td>Premium vs peers + DCF</td><td class="red"><strong>TRIM</strong></td></tr>
      <tr><td class="num">&gt;$100</td><td>Bull case priced in</td><td class="red"><strong>SELL</strong></td></tr>
    </table>
    <h3>Catalysts (next 12 months)</h3>
    <ol>
      <li>Q2'26 print (Aug 2026) — first as public co.; RIKEN cliff + Helios ramp narrative</li>
      <li>Sol roadmap update (timing TBC)</li>
      <li>Honeywell secondary (likely 6-12 mo) — lockup expiry creates overhang</li>
      <li>CHIPS Act $100M LOI conversion</li>
      <li>Hyperscaler distribution deal expansions</li>
    </ol>
  </div>
  <div>
    <h3>Honeywell SOTP read</h3>
    <ul>
      <li>QNT IPO adds ~$5/share to HON SOTP (~2.4%)</li>
      <li>Real upside if HON markets a clean SOTP story to investors</li>
      <li>Industrial-conglomerate discount could compress</li>
      <li><strong>Verdict for HON shareholders:</strong> modest positive, not transformative</li>
    </ul>
    <div class="callout">
      <strong>Cross-trade idea:</strong> If you want quantum optionality but
      are price-sensitive at $68, owning HON gives indirect QNT exposure plus
      stable cashflow and dividend — at a far lower multiple than QNT direct.
    </div>
  </div>
</div>
</section>

</main>

<footer>
Quantinuum (NASDAQ: QNT) — Competitive Analysis, Comps & Dual-DCF Valuation<br>
Generated June 4, 2026 using the financial-analysis skills pipeline<br>
Decision-framing only — not investment advice. [E] = estimate.<br>
Refresh after Q2'26 print (Aug 2026) and any Sol roadmap update.
</footer>

</body>
</html>
"""

OUT.write_text(HTML, encoding="utf-8")
print(f"Wrote {OUT} ({len(HTML)/1024:.1f} KB)")
