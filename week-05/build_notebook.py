"""Build week-05/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-05_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 5 — What a rate rise costs you
**European School of Economics · Thu 22 Oct 2026 · Tutor: Niccolò Salvini**

Arno Bikes keeps **€1M in bonds**. The Board asks whether a one-point rise in rates should worry it. Two numbers answer that: duration and convexity.
""")

code(r"""
import subprocess, sys
try:
    import plotly
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly"])
import numpy as np, plotly.graph_objects as go

def price(coupon, years, y, face=100.0):
    return sum(coupon*face/(1 + y)**t for t in range(1, years + 1)) + face/(1 + y)**years

print("ready")
""")

md(r"""
## A. Price and yield move in opposite directions
""")
code(r"""
print(f"{'yield':>7} {'5y 4% coupon':>15}")
for y in (0.02, 0.03, 0.04, 0.05, 0.06, 0.08):
    p = price(0.04, 5, y)
    tag = "premium" if p > 100 else ("par" if abs(p - 100) < 1e-9 else "discount")
    print(f"{y:>7.0%} {p:>15.2f}   {tag}")
""")

md(r"""
## B. Duration — the weighted average time to being repaid
""")
code(r"""
def duration_table(coupon, years, y, face=100.0):
    P = price(coupon, years, y, face)
    print(f"P = {P:.2f}")
    print(f"{'t':>3} {'CF':>8} {'PV':>10} {'weight':>9} {'t·w':>9}")
    mac = 0.0
    for t in range(1, years + 1):
        cf = coupon*face + (face if t == years else 0)
        pv = cf/(1 + y)**t
        w = pv/P
        mac += t*w
        print(f"{t:>3} {cf:>8.2f} {pv:>10.2f} {w:>9.4f} {t*w:>9.4f}")
    print(f"{'':>3} {'':>8} {P:>10.2f} {1.0:>9.4f} {mac:>9.4f}")
    print(f"Macaulay duration = {mac:.4f} years")
    print(f"Modified duration = {mac/(1+y):.4f}  (% per 1% of yield)")
    return mac, mac/(1 + y)

duration_table(0.04, 5, 0.06)
""")

md(r"""
### 🔍 CHECK
The weights column must sum to 1. On paper, if it does not, stop: something is wrong *before* the duration is.
""")

code(r"""
print("What moves duration, other things equal:")
for lab, (c, n, y) in {
    "5y 4% coupon, y=6%": (0.04, 5, 0.06),
    "10y 4% coupon, y=6%": (0.04, 10, 0.06),
    "5y 8% coupon, y=6%": (0.08, 5, 0.06),
    "5y 4% coupon, y=10%": (0.04, 5, 0.10),
    "5y zero, y=6%": (0.0, 5, 0.06),
}.items():
    P = price(c, n, y)
    mac = sum(t*((c*100 + (100 if t == n else 0))/(1 + y)**t) for t in range(1, n + 1))/P
    print(f"  {lab:<22} Macaulay {mac:5.2f}")
print("\nLonger maturity raises it. A bigger coupon lowers it. A higher yield lowers it. A zero's duration is its maturity.")
""")

md(r"""
## C. Convexity — the gap the straight line misses
""")
code(r"""
P0, y0 = price(0.05, 10, 0.05), 0.05
h = 1e-6
slope = (price(0.05, 10, y0 + h) - price(0.05, 10, y0 - h))/(2*h)
dmod = -slope/P0
hh = 1e-4
conv = (price(0.05, 10, y0 + hh) - 2*P0 + price(0.05, 10, y0 - hh))/(hh*hh*P0)
print(f"10-year 5% bond at par: P = {P0:.2f}, modified duration = {dmod:.4f}, convexity = {conv:.2f}")

ys = np.linspace(0.01, 0.10, 300)
fig = go.Figure()
fig.add_scatter(x=ys*100, y=[price(0.05, 10, v) for v in ys], name="the bond",
                line=dict(color="#363636", width=3))
fig.add_scatter(x=ys*100, y=P0 + slope*(ys - y0), name="what duration predicts",
                line=dict(color="#AF1F25", width=2, dash="dash"))
fig.add_scatter(x=[y0*100], y=[P0], mode="markers", marker=dict(size=13, color="#CDBA80"), showlegend=False)
fig.update_layout(template="simple_white", height=460, xaxis_title="yield %", yaxis_title="price €")
fig.show()

for dy in (0.005, 0.01, 0.02, -0.02):
    actual = price(0.05, 10, y0 + dy)
    dur_only = P0*(1 - dmod*dy)
    both = P0*(1 - dmod*dy + 0.5*conv*dy**2)
    print(f"Δy = {dy:+.1%}  actual {actual:7.2f}   duration only {dur_only:7.2f}   + convexity {both:7.2f}")
""")

md(r"""
**Duration alone overstates the loss and understates the gain.** The curve is above the line on both sides.

## D. The reserve, answered
""")
code(r"""
holdings = [("10-year 5% at par", 400_000, 7.72), ("2-year", 600_000, 1.90)]
total = sum(v for _, v, _ in holdings)
dport = sum(v/total*d for _, v, d in holdings)
print(f"portfolio modified duration = {dport:.3f}")
for shift in (0.01, 0.005, -0.01):
    print(f"  yields {shift:+.1%}  →  {-dport*shift*total:>12,.0f} €")
""")

md(r"""
### The sentence for the Board
> "A one-point rise costs the reserve about €42,000, a little over 4%. The exposure sits almost entirely in the ten-year holding; shortening it would roughly halve the figure. Convexity means the true loss is slightly smaller than this."

## Homework and what comes next

`homework.md` — due Wednesday 28 October, lighter on purpose. **Reading week is for the midterm**, due Sunday 1 November on Turnitin.
""")

nb["cells"] = cells
nbf.write(nb, "session.ipynb")
print("wrote session.ipynb")
