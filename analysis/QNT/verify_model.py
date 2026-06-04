"""Quick sanity check: recompute base-case dual DCF in pure Python, no openpyxl recalc."""

# --- Drivers (must match build_model.py exactly) ---
years = ["FY24A", "FY25A", "FY26E", "FY27E", "FY28E", "FY29E",
         "FY30E", "FY31E", "FY32E", "FY33E", "FY34E", "FY35E"]

riken  = [14.5, 18.5,  4.0,  2.0,  1.0,  0.5,    0.0,    0.0,    0.0,    0.0,    0.0,    0.0]
helios = [ 4.0,  5.0, 22.0, 75.0,180.0,350.0, 580.0, 850.0,1180.0,1550.0,1980.0,2480.0]
saas   = [ 2.5,  4.0,  8.0, 16.0, 32.0, 60.0, 100.0, 160.0, 240.0, 340.0, 460.0, 600.0]
gov    = [ 2.0,  3.4,  6.0, 12.0, 20.0, 30.0,  45.0,  65.0,  90.0, 120.0, 160.0, 200.0]
gm_pct = [0.30,0.32,0.38,0.45,0.52,0.58,0.62,0.65,0.67,0.68,0.69,0.70]
rd_pct = [4.50,5.40,2.80,1.20,0.55,0.32,0.22,0.16,0.13,0.11,0.10,0.09]
sga_pct= [1.50,1.80,1.10,0.55,0.30,0.20,0.16,0.14,0.12,0.11,0.10,0.10]
sbc_pct= [0.55,0.50,0.45,0.40,0.35,0.30,0.27,0.25,0.22,0.20,0.18,0.16]
capex_pct=[0.80,0.65,0.40,0.25,0.18,0.14,0.12,0.10,0.09,0.08,0.08,0.07]
da_pct = [0.50,0.40,0.28,0.20,0.15,0.12,0.10,0.08,0.07,0.06,0.06,0.05]
int_inc= [25,28,80,75,65,55,45,35,25,15,10,5]
shares = [200,226,253.9,263,273,283,293,303,313,323,333,343]

rf, erp, beta = 0.043, 0.055, 2.10
wacc = rf + beta * erp
g    = 0.040
cash_post_ipo = 2080.0

# --- Compute ---
rev   = [r+h+s+g_ for r,h,s,g_ in zip(riken,helios,saas,gov)]
gp    = [r*gm for r,gm in zip(rev,gm_pct)]
rd    = [r*p  for r,p  in zip(rev,rd_pct)]
sga   = [r*p  for r,p  in zip(rev,sga_pct)]
op    = [gp[i]-rd[i]-sga[i] for i in range(len(rev))]
ni    = [op[i]+int_inc[i] - max(0, op[i]+int_inc[i])*0.21 for i in range(len(rev))]
sbc   = [rd[i]*sbc_pct[i] for i in range(len(rev))]
da    = [rev[i]*da_pct[i] for i in range(len(rev))]
ocf   = [ni[i]+sbc[i]+da[i] for i in range(len(rev))]
capex = [-rev[i]*capex_pct[i] for i in range(len(rev))]
fcf   = [ocf[i]+capex[i] for i in range(len(rev))]

# DCF
disc_per = [0,0,0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5]
df = [1/(1+wacc)**dp for dp in disc_per]
pv = [fcf[i]*df[i] for i in range(len(rev))]
pv_explicit = sum(pv[2:])  # FY26E onward
tv = fcf[-1]*(1+g)/(wacc-g)
pv_tv = tv * df[-1]
ev = pv_explicit + pv_tv
eqv = ev + cash_post_ipo
implied_price = eqv / shares[2]  # use FY26E share count

# Reverse-engineered
curr = 68.00
mc = curr * shares[2]
ev_today = mc - cash_post_ipo
mature_mult = 8.0
impl_rev_35 = ev_today * (1+wacc)**9.5 / mature_mult
gap = impl_rev_35 / rev[-1] - 1
share_of_tam = impl_rev_35 / 50000

print(f"\n{'='*68}")
print(f"QNT MODEL VERIFICATION — base case")
print(f"{'='*68}\n")
print(f"WACC                        : {wacc:.2%}")
print(f"Terminal growth             : {g:.2%}\n")
print(f"Revenue path:")
for i,y in enumerate(years):
    print(f"  {y}: ${rev[i]:>8,.1f}M   op ${op[i]:>9,.1f}M   fcf ${fcf[i]:>9,.1f}M")
print(f"\nFRAMEWORK 1 — Traditional DCF")
print(f"  Sum PV(FCF) FY26E-FY35E  : ${pv_explicit:>9,.0f}M")
print(f"  Terminal value           : ${tv:>9,.0f}M")
print(f"  PV of TV                 : ${pv_tv:>9,.0f}M")
print(f"  Enterprise value         : ${ev:>9,.0f}M")
print(f"  + Cash post-IPO          : ${cash_post_ipo:>9,.0f}M")
print(f"  Equity value             : ${eqv:>9,.0f}M")
print(f"  Implied price/share      : ${implied_price:>9,.2f}")
print(f"  Current trading price    : ${curr:>9,.2f}")
print(f"  Premium to intrinsic     : {curr/implied_price-1:>9.0%}")
print(f"\nFRAMEWORK 2 — Reverse-engineered to clear $68")
print(f"  Current FD market cap    : ${mc:>9,.0f}M")
print(f"  Current EV (ex-cash)     : ${ev_today:>9,.0f}M")
print(f"  Assumed mature multiple  : {mature_mult:>9.1f}x EV/Rev")
print(f"  Implied FY2035 revenue   : ${impl_rev_35:>9,.0f}M")
print(f"  Model FY2035 revenue     : ${rev[-1]:>9,.0f}M")
print(f"  Gap (impl vs model)      : {gap:>9.0%}")
print(f"  Implied 2035 QC TAM share: {share_of_tam:>9.1%} of $50B")
print(f"\n{'='*68}")
