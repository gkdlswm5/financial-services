"""Independent recompute of WMT base-case DCF — mirrors workbook formulas."""
YR = ["FY27", "FY28", "FY29", "FY30", "FY31"]
us = [509000, 535000, 562000, 590000, 619000]
intl = [131000, 141000, 152000, 163000, 175000]
sams = [100000, 106000, 112000, 119000, 126000]
opm = [0.047, 0.049, 0.051, 0.052, 0.053]
da_p = [0.018] * 5
cap_p = [0.027, 0.026, 0.025, 0.024, 0.024]
tax = [0.245] * 5
nwc_p = [0.00] * 5
rev_fy26 = 485000 + 122000 + 95000  # 702000

rev = [a + b + c for a, b, c in zip(us, intl, sams)]
ebit = [o * r for o, r in zip(opm, rev)]
nopat = [e * (1 - t) for e, t in zip(ebit, tax)]
da = [d * r for d, r in zip(da_p, rev)]
capex = [c * r for c, r in zip(cap_p, rev)]
prev = [rev_fy26] + rev[:-1]
dnwc = [(r - p) * n for r, p, n in zip(rev, prev, nwc_p)]
ufcf = [n + d - c - w for n, d, c, w in zip(nopat, da, capex, dnwc)]

rf, erp, beta, kd, t_w = 0.043, 0.050, 0.60, 0.045, 0.245
price, sh, debt, cash = 95.50, 8050, 60000, 11000
coe = rf + beta * erp
katd = kd * (1 - t_w)
mve = price * sh
netdebt = debt - cash
we = mve / (mve + debt); wd = debt / (mve + debt)
wacc = we * coe + wd * katd
g = 0.025
df = [1 / (1 + wacc) ** (i + 1) for i in range(5)]
pv = [f * d for f, d in zip(ufcf, df)]
pv_expl = sum(pv)
tv = ufcf[-1] * (1 + g) / (wacc - g)
pv_tv = tv * df[-1]
ev = pv_expl + pv_tv
equity = ev - netdebt
per_share = equity / sh

print("REVENUE ($M):", [round(x) for x in rev])
print("  growth %:", ["n/a" if i == 0 else f"{rev[i]/rev[i-1]-1:.1%}" for i in range(5)])
print("EBIT ($M):", [round(x) for x in ebit])
print("EBITDA ($M):", [round(e + d) for e, d in zip(ebit, da)])
print("Unlev FCF ($M):", [round(x) for x in ufcf])
print(f"\nCost of equity: {coe:.2%}  After-tax Kd: {katd:.2%}  Eq weight: {we:.1%}")
print(f"WACC: {wacc:.2%}  (target ~7.0% for sensitivity center)")
print(f"Net debt: ${netdebt:,}M")
print(f"\nPV explicit FCF: ${pv_expl:,.0f}M")
print(f"Terminal value:  ${tv:,.0f}M (g={g:.1%})")
print(f"PV of TV:        ${pv_tv:,.0f}M ({pv_tv/ev:.0%} of EV)")
print(f"Enterprise val:  ${ev:,.0f}M")
print(f"Equity value:    ${equity:,.0f}M")
print(f"IMPLIED/SHARE:   ${per_share:,.2f}")
print(f"Current price:   ${price:,.2f}")
print(f"Upside/(down):   {per_share/price-1:+.1%}")
print()
g_axis = [0.015, 0.020, 0.025, 0.030, 0.035]
w_axis = [0.060, 0.065, 0.070, 0.075, 0.080]
print("SENSITIVITY ($/share):")
print("WACC\\g  " + "".join(f"{gg:>8.1%}" for gg in g_axis))
for w in w_axis:
    dfw = [1 / (1 + w) ** (i + 1) for i in range(5)]
    row = []
    for gg in g_axis:
        pvx = sum(f * d for f, d in zip(ufcf, dfw))
        tvv = ufcf[-1] * (1 + gg) / (w - gg)
        evv = pvx + tvv * dfw[-1]
        row.append((evv - netdebt) / sh)
    mark = "*" if abs(w - 0.070) < 1e-9 else " "
    print(f"{w:>5.1%}{mark} " + "".join(f"{v:>8.0f}" for v in row))
