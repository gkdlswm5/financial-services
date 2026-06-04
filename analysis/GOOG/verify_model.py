"""Independent recompute of GOOG base-case DCF."""
YR = ["FY26", "FY27", "FY28", "FY29", "FY30"]
serv = [393100, 432400, 471300, 509000, 545600]
cloud = [92000, 132000, 178000, 222000, 266000]
other = [1800, 2100, 2500, 3000, 3600]
serv_m = [0.45] * 5
cloud_m = [0.30, 0.32, 0.34, 0.35, 0.36]
other_m = [-3.5, -2.5, -1.5, -1.0, -0.5]
corp = [9000, 10000, 11000, 12000, 13000]
da = [38000, 58000, 76000, 90000, 100000]
capex = [185000, 200000, 180000, 160000, 150000]
tax = [0.18, 0.20, 0.21, 0.21, 0.21]
nwc_p = [0.05] * 5
rev_fy25 = 342700 + 58700 + 1537

rev = [s + c + o for s, c, o in zip(serv, cloud, other)]
ebit = [s * sm + c * cm + o * om - cp for s, sm, c, cm, o, om, cp in zip(serv, serv_m, cloud, cloud_m, other, other_m, corp)]
nopat = [e * (1 - t) for e, t in zip(ebit, tax)]
prev = [rev_fy25] + rev[:-1]
dnwc = [(r - p) * n for r, p, n in zip(rev, prev, nwc_p)]
ufcf = [n + d - c - w for n, d, c, w in zip(nopat, da, capex, dnwc)]

rf, erp, beta, kd, t_w = 0.043, 0.050, 1.0, 0.045, 0.18
price, sh, debt, cash = 357.73, 12120, 46500, 126800
coe = rf + beta * erp
katd = kd * (1 - t_w)
mve = price * sh
netcash = cash - debt
we = mve / (mve + debt); wd = debt / (mve + debt)
wacc = we * coe + wd * katd
g = 0.030
df = [1 / (1 + wacc) ** (i + 1) for i in range(5)]
pv = [f * d for f, d in zip(ufcf, df)]
pv_expl = sum(pv)
tv = ufcf[-1] * (1 + g) / (wacc - g)
pv_tv = tv * df[-1]
ev = pv_expl + pv_tv
equity = ev + netcash
per_share = equity / sh

print("REVENUE ($M):", [round(x) for x in rev])
print("  growth %:", ["n/a" if i == 0 else f"{rev[i]/rev[i-1]-1:.1%}" for i in range(5)])
print("EBIT ($M):", [round(x) for x in ebit])
print("Unlev FCF ($M):", [round(x) for x in ufcf])
print(f"\nCost of equity: {coe:.2%}  After-tax Kd: {katd:.2%}  Eq weight: {we:.1%}")
print(f"WACC: {wacc:.2%}  (target ~9.0% for sensitivity center)")
print(f"Net cash: ${netcash:,}M")
print(f"\nPV explicit FCF: ${pv_expl:,.0f}M")
print(f"Terminal value:  ${tv:,.0f}M (g={g:.1%})")
print(f"PV of TV:        ${pv_tv:,.0f}M ({pv_tv/ev:.0%} of EV)")
print(f"Enterprise val:  ${ev:,.0f}M")
print(f"Equity value:    ${equity:,.0f}M")
print(f"IMPLIED/SHARE:   ${per_share:,.2f}")
print(f"Current price:   ${price:,.2f}")
print(f"Upside/(down):   {per_share/price-1:+.1%}")
print()
g_axis = [0.020, 0.025, 0.030, 0.035, 0.040]
w_axis = [0.080, 0.085, 0.090, 0.095, 0.100]
print("SENSITIVITY ($/share):")
print("WACC\\g  " + "".join(f"{gg:>8.1%}" for gg in g_axis))
for w in w_axis:
    dfw = [1 / (1 + w) ** (i + 1) for i in range(5)]
    row = []
    for gg in g_axis:
        pvx = sum(f * d for f, d in zip(ufcf, dfw))
        tvv = ufcf[-1] * (1 + gg) / (w - gg)
        evv = pvx + tvv * dfw[-1]
        row.append((evv + netcash) / sh)
    mark = "*" if abs(w - 0.090) < 1e-9 else " "
    print(f"{w:>5.1%}{mark} " + "".join(f"{v:>8.0f}" for v in row))
