"""Build week-04/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf

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
import numpy as np, plotly.graph_objects as go
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

## Homework

`homework.md` — eight drills plus a memo correcting the Board member who added the flows up.
Due Wednesday 21 October, 23:59.
""")

nb["cells"] = cells
nbf.write(nb, "session.ipynb")
print("wrote session.ipynb")
