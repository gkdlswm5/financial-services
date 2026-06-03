"""
Independent recomputation of AVGO-Model.xlsx base case — mirrors the workbook
formulas in pure Python so the model's outputs can be verified and the headline
numbers reused in the deck/README. The workbook (validated, 0 formula errors)
remains the source of truth; this is a cross-check (LibreOffice headless recalc
is unavailable in this sandbox).
"""
YR = ["FY26", "FY27", "FY28", "FY29", "FY30"]
ai   = [48000, 76000, 98000, 116000, 131000]
nai  = [17500, 18500, 19500, 20500, 21500]
sw   = [28000, 30000, 32000, 34000, 36000]
opm  = [0.44, 0.47, 0.49, 0.50, 0.51]
da_p = [0.12, 0.10, 0.08, 0.07, 0.06]
cap_p= [0.025]*5
tax  = [0.14, 0.14, 0.14, 0.15, 0.15]
nwc_p= [0.03]*5
rev_fy25 = 63887

rev = [a+b+c for a, b, c in zip(ai, nai, sw)]
ebit = [o*r for o, r in zip(opm, rev)]
nopat = [e*(1-t) for e, t in zip(ebit, tax)]
da = [d*r for d, r in zip(da_p, rev)]
capex = [c*r for c, r in zip(cap_p, rev)]
prev = [rev_fy25] + rev[:-1]
dnwc = [(r-p)*n for r, p, n in zip(rev, prev, nwc_p)]
ufcf = [n+d-c-w for n, d, c, w in zip(nopat, da, capex, dnwc)]

# WACC
rf, erp, beta, kd, t_w = 0.043, 0.050, 1.072, 0.050, 0.14
price, sh, debt, cash = 460.00, 4730, 66057, 14200
coe = rf + beta*erp
katd = kd*(1-t_w)
mve = price*sh
netdebt = debt-cash
we = mve/(mve+debt); wd = debt/(mve+debt)
wacc = we*coe + wd*katd

g = 0.035
df = [1/(1+wacc)**(i+1) for i in range(5)]
pv = [f*d for f, d in zip(ufcf, df)]
pv_expl = sum(pv)
tv = ufcf[-1]*(1+g)/(wacc-g)
pv_tv = tv*df[-1]
ev = pv_expl + pv_tv
equity = ev - netdebt
per_share = equity/sh

print("REVENUE ($M):", [round(x) for x in rev])
print("  growth %   :", ["n/a"] + [f"{rev[i]/rev[i-1]-1:.1%}" for i in range(1, 5)])
print("  AI mix %   :", [f"{a/r:.0%}" for a, r in zip(ai, rev)])
print("EBIT ($M)    :", [round(x) for x in ebit])
print("D&A ($M)     :", [round(x) for x in da])
print("EBITDA ($M)  :", [round(e+d) for e, d in zip(ebit, da)])
print("Unlev FCF($M):", [round(x) for x in ufcf])
print("uFCF margin  :", [f"{u/r:.0%}" for u, r in zip(ufcf, rev)])
print()
print(f"Cost of equity : {coe:.2%}")
print(f"After-tax Kd   : {katd:.2%}")
print(f"Equity weight  : {we:.1%}  Debt weight: {wd:.1%}")
print(f"WACC           : {wacc:.2%}   (target 9.50% for sensitivity center)")
print(f"Net debt ($M)  : {netdebt:,}")
print()
print(f"PV explicit FCF: ${pv_expl:,.0f}M")
print(f"Terminal value : ${tv:,.0f}M  (Gordon, g={g:.1%})")
print(f"PV of TV       : ${pv_tv:,.0f}M   ({pv_tv/ev:.0%} of EV)")
print(f"Enterprise val : ${ev:,.0f}M")
print(f"Equity value   : ${equity:,.0f}M")
print(f"IMPLIED / SHARE: ${per_share:,.2f}")
print(f"Current price  : ${price:,.2f}")
print(f"Upside/(down)  : {per_share/price-1:+.1%}")
print()
# 5x5 sensitivity (WACC rows x g cols), implied per share
g_axis = [0.025, 0.030, 0.035, 0.040, 0.045]
w_axis = [0.085, 0.090, 0.095, 0.100, 0.105]
print("SENSITIVITY — implied $/share   (rows=WACC, cols=terminal g)")
print("WACC\\g  " + "".join(f"{gg:>8.1%}" for gg in g_axis))
for w in w_axis:
    dfw = [1/(1+w)**(i+1) for i in range(5)]
    row = []
    for gg in g_axis:
        pvx = sum(f*d for f, d in zip(ufcf, dfw))
        tvv = ufcf[-1]*(1+gg)/(w-gg)
        evv = pvx + tvv*dfw[-1]
        row.append((evv-netdebt)/sh)
    mark = "*" if abs(w-0.095) < 1e-9 else " "
    print(f"{w:>5.1%}{mark} " + "".join(f"{v:>8.0f}" for v in row))
print("* base-case WACC row; center cell (9.5%/3.5%) should equal implied $/share above")
