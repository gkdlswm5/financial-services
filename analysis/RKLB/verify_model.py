"""Independent recompute of RKLB base-case DCF."""
YR = ["FY27", "FY28", "FY29", "FY30", "FY31"]
launch = [550, 1100, 1700, 2300, 2900]
space = [825, 1080, 1380, 1700, 2050]
opm = [-0.05, 0.05, 0.10, 0.13, 0.15]
da = [85, 120, 150, 175, 195]
capex = [220, 200, 170, 150, 140]
tax = [0, 0.10, 0.15, 0.21, 0.21]
rev_fy26 = 260 + 610

rev = [l + s for l, s in zip(launch, space)]
ebit = [o * r for o, r in zip(opm, rev)]
taxes = [max(e, 0) * t for e, t in zip(ebit, tax)]
nopat = [e - t for e, t in zip(ebit, taxes)]
ufcf = [n + d - c for n, d, c in zip(nopat, da, capex)]

rf, erp, beta, kd, t_w = 0.043, 0.050, 1.8, 0.060, 0.21
price, sh, debt, cash = 123.32, 608, 38, 1480
coe = rf + beta * erp
katd = kd * (1 - t_w)
mve = price * sh
netcash = cash - debt
we = mve / (mve + debt); wd = debt / (mve + debt)
wacc = we * coe + wd * katd
g = 0.035
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
print(f"\nCost of equity: {coe:.2%}  After-tax Kd: {katd:.2%}  Eq weight: {we:.2%}")
print(f"WACC: {wacc:.2%}  (target ~13.0% for sensitivity center)")
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
g_axis = [0.025, 0.030, 0.035, 0.040, 0.045]
w_axis = [0.110, 0.120, 0.130, 0.140, 0.150]
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
    mark = "*" if abs(w - 0.130) < 1e-9 else " "
    print(f"{w:>5.1%}{mark} " + "".join(f"{v:>8.0f}" for v in row))
