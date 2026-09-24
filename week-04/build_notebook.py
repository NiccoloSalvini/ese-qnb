"""Build week-04/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf
from pathlib import Path

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-04_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 4 — Money has a date on it
**European School of Economics · Thu 15 Oct 2026 · Tutor: Niccolò Salvini**

The case: a new assembly line costs **€2.4M today** and returns **€700k, €800k, €900k, €1,000k** over four years. Arno Bikes borrows at **9%**.
""")

code(r"""
import subprocess, sys
try:
    import plotly
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly"])
import numpy as np, pandas as pd, plotly.graph_objects as go
from math import exp
print("ready")
""")

md(r"""
## A. Compounding, and its ceiling

€1,000 at 12% for one year, compounded `n` times a year.
""")
code(r"""
for label, n in [("once a year", 1), ("every 6 months", 2), ("every quarter", 4),
                 ("every month", 12), ("every week", 52), ("every day", 365),
                 ("every hour", 8760)]:
    print(f"{label:<16} n = {n:>5}   €{1000*(1 + 0.12/n)**n:,.4f}")
print(f"{'continuously':<16} n → ∞     €{1000*exp(0.12):,.4f}   ← the ceiling, and that is e")
""")

md(r"""
### 🔍 CHECK
The gap from yearly to daily is €7.47. The gap from daily to *infinitely often* is three cents. Say out loud what that means for a bank's marketing.
""")

md(r"""
## B. The effective annual rate — the only honest comparison
""")
code(r"""
def ear(nominal, m):
    return exp(nominal) - 1 if m is None else (1 + nominal/m)**m - 1

print("12% nominal:")
for lab, m in [("semi-annually", 2), ("quarterly", 4), ("monthly", 12), ("continuously", None)]:
    print(f"  compounded {lab:<14} EAR = {ear(0.12, m):.4%}")

print()
print("Bank A: 7.8% monthly  → EAR", f"{ear(0.078, 12):.4%}")
print("Bank B: 8.0% annually → EAR", f"{ear(0.08, 1):.4%}")
print("The lower headline rate is the dearer loan.")
""")

md(r"""
## C. Discounting — what distant money is worth
""")
code(r"""
years = np.arange(0, 21)
fig = go.Figure()
for r, col in ((0.03, "#CDBA80"), (0.09, "#363636"), (0.16, "#AF1F25")):
    fig.add_scatter(x=years, y=1/(1 + r)**years, name=f"{r:.0%}",
                    line=dict(color=col, width=3))
fig.update_layout(template="simple_white", height=420, xaxis_title="years away",
                  yaxis_title="worth of €1 today", legend_title="discount rate")
fig.show()
""")
code(r"""
annuity    = lambda c, r, n: c*(1 - (1 + r)**-n)/r
perpetuity = lambda c, r: c/r
print(f"€10,000 in 5 years at 7%        : €{10000/1.07**5:,.2f}")
print(f"€12,000 a year for 10 yrs at 6% : €{annuity(12000, 0.06, 10):,.2f}")
print(f"€12,000 a year for ever at 6%   : €{perpetuity(12000, 0.06):,.2f}")
print(f"  everything after year 10      : €{perpetuity(12000, 0.06) - annuity(12000, 0.06, 10):,.2f}")
""")

md(r"""
## D. NPV, and the rate that makes it zero

Move the discount rate. Watch the sign change.
""")
code(r"""
FLOWS = [-2400, 700, 800, 900, 1000]          # € thousand
npv = lambda r: sum(cf/(1 + r)**t for t, cf in enumerate(FLOWS))

print(f"{'year':>5} {'flow':>8} {'factor':>10} {'PV @9%':>10}")
for t, cf in enumerate(FLOWS):
    print(f"{t:>5} {cf:>8,} {1/1.09**t:>10.6f} {cf/1.09**t:>10.2f}")
print(f"{'':>5} {'':>8} {'NPV':>10} {npv(0.09):>10.2f}")
""")
code(r"""
rates = np.linspace(0.001, 0.30, 300)
lo, hi = 0.0, 0.5
for _ in range(80):
    mid = (lo + hi)/2
    lo, hi = (mid, hi) if npv(mid) > 0 else (lo, mid)
irr = (lo + hi)/2

fig = go.Figure(go.Scatter(x=rates*100, y=[npv(r) for r in rates],
                           line=dict(color="#363636", width=3), name="NPV"))
fig.add_hline(y=0, line=dict(color="#7a7f85", width=1))
fig.add_scatter(x=[9], y=[npv(0.09)], mode="markers+text", marker=dict(size=13, color="#1E8449"),
                text=[f"our 9%: +{npv(0.09):,.0f}k"], textposition="top right", showlegend=False)
fig.add_scatter(x=[irr*100], y=[0], mode="markers+text", marker=dict(size=13, color="#CDBA80"),
                text=[f"IRR = {irr:.2%}"], textposition="bottom right", showlegend=False)
fig.update_layout(template="simple_white", height=440, xaxis_title="discount rate %",
                  yaxis_title="NPV (€ thousand)")
fig.show()
print(f"IRR = {irr:.4%}    NPV at 16% = {npv(0.16):,.2f}k")
""")

md(r"""
### 🔍 CHECK
Delay the first €700k by one year (so the flows become `−2400, 0, 700, 800, 900, 1000`). Before running it: does the IRR rise or fall? Then change `FLOWS` above and find out.
""")

md(r"""
## Drills, solved in code

This section is an optional companion: the code is not examined, but it is a good way to check your work. Every drill from `drills.md` is solved here in plain Python, with the same numbers. Do the drill on paper first, then run the cell and compare.
""")

md(r"""
**D1 (a).** €8,000 is invested for 3 years at 6% a year. Simple interest: the final amount.

$$A = P(1 + r\,t)$$
""")
code(r"""
P = 8000     # principal, €
r = 0.06     # yearly rate
t = 3        # years

A_simple = P * (1 + r * t)    # interest only on the original €8,000
print(f"With simple interest the final amount is €{A_simple:,.2f}.")
assert abs(A_simple - 9440.00) < 0.01
""")

md(r"""
**D1 (b).** Same money, compounded annually: the final amount.

$$A = P(1 + r)^t$$
""")
code(r"""
P, r, t = 8000, 0.06, 3

A_compound = P * (1 + r) ** t    # interest also earns interest
print(f"Compounded annually the final amount is €{A_compound:,.2f}.")
assert abs(A_compound - 9528.13) < 0.01
""")

md(r"""
**D1 (c).** The difference, and one sentence on where it comes from.
""")
code(r"""
P, r, t = 8000, 0.06, 3
A_simple = P * (1 + r * t)
A_compound = P * (1 + r) ** t

difference = A_compound - A_simple
print(f"Compounding earns €{difference:,.2f} more: interest is paid on the interest already earned.")
assert abs(difference - 88.13) < 0.01
""")

md(r"""
**D2 (a).** €5,000 for 4 years at 8% nominal, compounded quarterly. The final amount.

$$A = P\left(1 + \frac{i}{m}\right)^{m t}$$
""")
code(r"""
P = 5000     # principal, €
i = 0.08     # nominal yearly rate
m = 4        # compounding periods per year (quarterly)
t = 4        # years

A = P * (1 + i / m) ** (m * t)    # 2% a quarter, 16 quarters
print(f"The final amount is €{A:,.2f}.")
assert abs(A - 6863.93) < 0.01
""")

md(r"""
**D2 (b).** The interest earned.
""")
code(r"""
P, i, m, t = 5000, 0.08, 4, 4
A = P * (1 + i / m) ** (m * t)

interest = A - P
print(f"The interest earned is €{interest:,.2f}.")
assert abs(interest - 1863.93) < 0.01
""")

md(r"""
**D3.** A bank quotes 6% nominal. Which is worth more to a depositor?
(i) compounded annually (ii) compounded monthly (iii) they are the same
""")
code(r"""
i = 0.06
ear_annual = (1 + i / 1) ** 1 - 1
ear_monthly = (1 + i / 12) ** 12 - 1

print(f"Annually: EAR = {ear_annual:.2%}.  Monthly: EAR = {ear_monthly:.2%}.")
print("Answer (ii): monthly compounding pays interest on interest sooner, so it is worth more.")
assert ear_monthly > ear_annual
assert abs(ear_monthly - 0.0617) < 0.00005
""")

md(r"""
**D4.** Compute the EAR for a 12% nominal rate compounded (a) semi-annually, (b) quarterly, (c) monthly.

$$\text{EAR} = \left(1 + \frac{i}{m}\right)^m - 1$$
""")
code(r"""
i = 0.12
ear_a = (1 + i / 2) ** 2 - 1      # (a) semi-annually
ear_b = (1 + i / 4) ** 4 - 1      # (b) quarterly
ear_c = (1 + i / 12) ** 12 - 1    # (c) monthly

print(f"(a) semi-annually: EAR = {ear_a:.2%}")
print(f"(b) quarterly:     EAR = {ear_b:.2%}")
print(f"(c) monthly:       EAR = {ear_c:.2%}")
assert abs(ear_a - 0.1236) < 0.00005 and abs(ear_b - 0.1255) < 0.00005
assert abs(ear_c - 0.1268) < 0.00005
""")

md(r"""
**D4 (d).** The same 12% compounded continuously.

$$\text{EAR} = e^{i} - 1$$
""")
code(r"""
i = 0.12
ear_d = exp(i) - 1    # the ceiling that (a), (b), (c) approach

print(f"(d) continuously:  EAR = {ear_d:.2%} — the gaps shrink towards this ceiling.")
assert abs(ear_d - 0.1275) < 0.00005
""")

md(r"""
**D5.** Bank A offers 7.8% compounded monthly. Bank B offers 8% compounded annually. Which do you borrow from, and why?
""")
code(r"""
ear_A = (1 + 0.078 / 12) ** 12 - 1    # put Bank A on an annual basis
ear_B = (1 + 0.08 / 1) ** 1 - 1       # Bank B is already annual

print(f"Bank A: EAR = {ear_A:.3%}.  Bank B: EAR = {ear_B:.3%}.")
print("Borrow from B: A's lower quoted rate hides more frequent compounding.")
assert abs(ear_A - 0.08085) < 0.000005
assert ear_B < ear_A
""")

md(r"""
**D6 (stretch).** 5% nominal compounded continuously. What annual compounding rate leaves a depositor equally well off?
""")
code(r"""
i = 0.05
equivalent_annual = exp(i) - 1    # one year of continuous growth, as a yearly rate

print(f"An annual rate of {equivalent_annual:.2%} is equivalent.")
assert abs(equivalent_annual - 0.0513) < 0.00005
""")

md(r"""
**D7.** What is €10,000 receivable in 5 years worth today at 7%?

$$PV = \frac{FV}{(1 + r)^n}$$
""")
code(r"""
FV = 10000   # € received in the future
r = 0.07
n = 5        # years away

PV = FV / (1 + r) ** n
print(f"€10,000 in 5 years is worth €{PV:,.2f} today.")
assert abs(PV - 7129.86) < 0.01
""")

md(r"""
**D8.** Pay for a €50,000 machine with (i) €50,000 today or (ii) €18,000 at the end of each of the next three years. Cost of capital 9%. Which do you choose?

$$PV_{\text{annuity}} = C \cdot \frac{1 - (1 + r)^{-n}}{r}$$
""")
code(r"""
C, r, n = 18000, 0.09, 3
price_today = 50000

factor = (1 - (1 + r) ** -n) / r     # annuity factor
PV_instalments = C * factor
print(f"Annuity factor {factor:.6f}; PV of the instalments = €{PV_instalments:,.2f}.")
print(f"Pay in instalments: about €{price_today - PV_instalments:,.0f} less in today's money.")
assert abs(PV_instalments - 45563.31) < 0.02
""")

md(r"""
**D9 (a).** An annuity pays €12,000 at the end of each year for 10 years. At 6%, what is it worth today?
""")
code(r"""
C, r, n = 12000, 0.06, 10

PV_annuity = C * (1 - (1 + r) ** -n) / r
print(f"The 10-year annuity is worth €{PV_annuity:,.2f} today.")
assert abs(PV_annuity - 88321.04) < 0.01
""")

md(r"""
**D9 (b).** A perpetuity pays €12,000 at the end of every year for ever. At 6%, what is it worth today?

$$PV = \frac{C}{r}$$
""")
code(r"""
C, r = 12000, 0.06

PV_perpetuity = C / r
print(f"The perpetuity is worth €{PV_perpetuity:,.2f} today.")
assert abs(PV_perpetuity - 200000.00) < 0.01
""")

md(r"""
**D9 (c).** Explain the gap between (a) and (b).
""")
code(r"""
C, r, n = 12000, 0.06, 10
PV_annuity = C * (1 - (1 + r) ** -n) / r
PV_perpetuity = C / r

gap = PV_perpetuity - PV_annuity    # value today of every payment after year 10
print(f"All the payments after year 10 are worth only €{gap:,.0f} today:")
print("discounting shrinks distant money towards nothing.")
assert abs(gap - 111679) < 1
""")

md(r"""
**D10 (stretch).** A perpetuity pays €5,000 next year and grows at 2% a year for ever. At 7%, what is it worth today?

$$PV = \frac{C_1}{r - g}$$
""")
code(r"""
C1 = 5000    # first payment, next year
r = 0.07     # discount rate
g = 0.02     # growth rate of the payment

PV = C1 / (r - g)
print(f"The growing perpetuity is worth €{PV:,.2f} today.")
assert abs(PV - 100000.00) < 0.01
""")

md(r"""
**D11 (a).** Arno Bikes' assembly line at a 9% cost of capital: write the NPV as a sum (€ thousand).

$$NPV = -2400 + \frac{700}{1.09} + \frac{800}{1.09^2} + \frac{900}{1.09^3} + \frac{1000}{1.09^4}$$
""")
code(r"""
flows = [-2400, 700, 800, 900, 1000]    # € thousand, years 0..4
r = 0.09

terms = [f"{cf}/(1.09)^{t}" for t, cf in enumerate(flows)]
print("NPV = " + " + ".join(terms))
""")

md(r"""
**D11 (b).** Compute each discounted flow and the NPV.
""")
code(r"""
flows = [-2400, 700, 800, 900, 1000]    # € thousand
r = 0.09

table = pd.DataFrame({"Year": range(len(flows)), "Flow (€k)": flows})
table["Factor"] = 1 / (1 + r) ** table["Year"]
table["Present value (€k)"] = table["Flow (€k)"] * table["Factor"]
print(table.round({"Factor": 6, "Present value (€k)": 2}).to_string(index=False))

NPV = table["Present value (€k)"].sum()
print(f"NPV = €{NPV:,.2f}k")
assert abs(NPV - 318.94) < 0.01
""")

md(r"""
**D11 (c).** Accept or reject, and say the sentence you would tell the Board.
""")
code(r"""
flows = [-2400, 700, 800, 900, 1000]
r = 0.09
NPV = sum(cf / (1 + r) ** t for t, cf in enumerate(flows))

decision = "Accept" if NPV > 0 else "Reject"
print(f"{decision}. At our 9% cost of capital the line adds about €{round(NPV)*1000:,.0f}")
print("of value in today's money.")
assert decision == "Accept"
""")

md(r"""
**D11b (a).** 60% equity, 40% debt. Shareholders expect 12%, the bank charges 6%, tax rate 25%. Compute the WACC.

$$\text{WACC} = w_e\,r_e + w_d\,r_d\,(1 - T)$$
""")
code(r"""
w_e, w_d = 0.60, 0.40    # weights of equity and debt
r_e, r_d = 0.12, 0.06    # cost of equity, cost of debt
T = 0.25                 # corporate tax rate

WACC = w_e * r_e + w_d * r_d * (1 - T)
print(f"WACC = {w_e*r_e:.1%} + {w_d*r_d*(1-T):.1%} = {WACC:.1%} — the 9% we were handed.")
assert abs(WACC - 0.09) < 1e-9
""")

md(r"""
**D11b (b).** Why does the tax rate appear at all, and only on the debt side?
""")
code(r"""
r_d, T = 0.06, 0.25

after_tax_debt = r_d * (1 - T)    # interest is deductible from taxable profit
print(f"Interest is tax-deductible, so a 6% loan really costs {after_tax_debt:.1%} after tax.")
print("Dividends are not deductible, so the equity side gets no (1 - T).")
assert abs(after_tax_debt - 0.045) < 1e-9
""")

md(r"""
**D11b (c).** If the mix became 40/60 (more debt), what happens to the WACC and to the NPV of the line?
""")
code(r"""
r_e, r_d, T = 0.12, 0.06, 0.25
flows = [-2400, 700, 800, 900, 1000]
npv = lambda r: sum(cf / (1 + r) ** t for t, cf in enumerate(flows))

WACC_new = 0.40 * r_e + 0.60 * r_d * (1 - T)    # more weight on the cheaper source
print(f"WACC falls from 9.0% to {WACC_new:.1%}; NPV rises from €{npv(0.09):,.2f}k to €{npv(WACC_new):,.2f}k.")
print("Not free: more debt means more risk, and in time r_e and r_d rise with it.")
assert WACC_new < 0.09 and npv(WACC_new) > npv(0.09)
""")

md(r"""
**D12 (stretch).** Recompute the NPV at 16%. What does the change in sign tell you, and what is the rate at which it happens?
""")
code(r"""
flows = [-2400, 700, 800, 900, 1000]    # € thousand
npv = lambda r: sum(cf / (1 + r) ** t for t, cf in enumerate(flows))
print(f"NPV at 16% = −€{-npv(0.16):,.2f}k: negative.")

lo, hi = 0.09, 0.16            # NPV > 0 at 9%, < 0 at 16%: the zero is in between
for _ in range(50):            # bisection: halve the interval, keep the sign change
    mid = (lo + hi) / 2
    lo, hi = (mid, hi) if npv(mid) > 0 else (lo, mid)
irr = (lo + hi) / 2
print(f"NPV = 0 at {irr:.1%}: the internal rate of return. Above it the project destroys value.")
assert abs(npv(0.16) - (-73.14)) < 0.01 and abs(irr - 0.146) < 0.0005
""")

md(r"""
## Homework

`homework.md` — eight drills plus a memo correcting the Board member who added the flows up.
Due Wednesday 21 October, 23:59.
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).parent / "session.ipynb")
print("wrote session.ipynb")
