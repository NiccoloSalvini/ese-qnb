"""Build week-05/session.ipynb with nbformat. Run: python build_notebook.py"""
from pathlib import Path
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
import numpy as np, pandas as pd, plotly.graph_objects as go

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
> "A one-point rise costs the reserve about €42,000, a little over 4%. About three quarters of the exposure sits in the ten-year holding; shortening it would roughly halve the figure. Convexity means the true loss is slightly smaller than this."
""")

# ---------------------------------------------------------------------------
# Drills, solved in code — one markdown + one code cell per drill part.
# Numbers match drills.md; every cell asserts against the worked solution.
# ---------------------------------------------------------------------------
md(r"""
## Drills, solved in code

This section is an optional companion: the code is not examined, but reading it is recommended. Every drill in `drills.md` is solved here in Python, one cell per question. Do the drill on paper first, then run the cell and compare your numbers with the output.
""")
code(r"""
# Two helpers used below. `close` checks our result against drills.md.
def close(value, expected, tol=0.01):
    assert abs(value - expected) <= tol, f"got {value}, drills.md says {expected}"

def cash_flow_table(coupon, years, y, face=100.0):
    # One row per year: time, cash flow, discount factor, present value, t × PV
    t = np.arange(1, years + 1)
    cf = np.full(years, coupon * face)
    cf[-1] += face                        # the face value comes back at maturity
    df = 1 / (1 + y) ** t                 # discount factor
    table = pd.DataFrame({"t": t, "CF": cf, "discount factor": df, "PV": cf * df})
    table["t·PV"] = table["t"] * table["PV"]
    return table

print("helpers ready")
""")

# ---- D1 -------------------------------------------------------------------
md(r"""
**D1 (a).** A 5-year bond, 4% annual coupon, face €100, yield 6%. Write the price as a sum.

$$P = \sum_{t=1}^{5} \frac{4}{(1.06)^t} + \frac{100}{(1.06)^5}$$
""")
code(r"""
coupon, face, y, years = 0.04, 100, 0.06, 5
# Each term of the sum is one cash flow divided by (1 + y)^t
terms = [coupon * face / (1 + y) ** t for t in range(1, years + 1)]
terms.append(face / (1 + y) ** years)     # the face value, repaid in year 5
for i, pv in enumerate(terms, start=1):
    label = f"coupon year {i}" if i <= years else "face value, year 5"
    print(f"{label:<20} {pv:6.2f}")
print(f"The price is the sum of these {len(terms)} present values.")
""")

md(r"""
**D1 (b).** Compute the price.

$$P = 4 \times \frac{1-(1.06)^{-5}}{0.06} + \frac{100}{(1.06)^5}$$
""")
code(r"""
coupon, face, y, years = 0.04, 100, 0.06, 5
annuity_factor = (1 - (1 + y) ** -years) / y        # 4.212364
coupons_pv = coupon * face * annuity_factor         # 16.85
face_pv = face / (1 + y) ** years                   # 74.73
P_d1 = coupons_pv + face_pv
print(f"annuity factor {annuity_factor:.6f}, coupons {coupons_pv:.2f}, face {face_pv:.2f}")
close(annuity_factor, 4.212364, 1e-6); close(coupons_pv, 16.85); close(face_pv, 74.73)
close(P_d1, 91.58)
print(f"The bond's price is €{P_d1:.2f}.")
""")

md(r"""
**D1 (c).** Is it at a premium or a discount, and why?
""")
code(r"""
coupon, y = 0.04, 0.06
status = "premium" if coupon > y else ("par" if coupon == y else "discount")
assert status == "discount" and P_d1 < 100
print(f"A {status}: the bond pays {coupon:.0%} on its face while the market demands {y:.0%}, "
      f"so it must sell below €100 (here €{P_d1:.2f}) to make up the difference.")
""")

# ---- D2 -------------------------------------------------------------------
md(r"""
**D2 (a).** The same bond (5 years, 4% coupon) at a yield of 4%, then at 2%. Both prices.
""")
code(r"""
coupon, face, years = 0.04, 100, 5
for y, expected in [(0.04, 100.00), (0.02, 109.43)]:
    annuity_factor = (1 - (1 + y) ** -years) / y
    coupons_pv = coupon * face * annuity_factor
    face_pv = face / (1 + y) ** years
    P = coupons_pv + face_pv
    print(f"yield {y:.0%}: {coupon*face:.0f} × {annuity_factor:.6f} + {face_pv:.2f} = €{P:.2f}")
    close(P, expected)
print(f"At 4% the bond is at par (€100.00); at 2% it costs €{P:.2f}.")
""")

md(r"""
**D2 (b).** State the rule that connects coupon, yield and price.
""")
code(r"""
coupon = 0.04
rows = []
for y in (0.02, 0.04, 0.06):
    P = price(coupon, 5, y)
    status = "premium" if P > 100 + 1e-9 else ("par" if abs(P - 100) < 1e-9 else "discount")
    rows.append({"coupon": coupon, "yield": y, "price": round(P, 2), "status": status})
print(pd.DataFrame(rows).to_string(index=False))
assert [r["status"] for r in rows] == ["premium", "par", "discount"]
print("Rule: coupon > yield → premium; coupon = yield → par; coupon < yield → discount. "
      "Price and yield always move in opposite directions.")
""")

# ---- D3 -------------------------------------------------------------------
md(r"""
**D3 (resit form).** A bond trades **above** par. Therefore: (i) its coupon is above its yield (ii) its yield is above its coupon (iii) it must be close to maturity.
""")
code(r"""
# Check each alternative on a 4% coupon bond at a few yields and maturities
premium_cases = [(y, n) for y in (0.02, 0.04, 0.06) for n in (2, 10, 30)
                 if price(0.04, n, y) > 100 + 1e-9]
print("Above par only when (yield, years) =", premium_cases)
assert all(y < 0.04 for y, _ in premium_cases)          # (i) always holds
assert any(n == 30 for _, n in premium_cases)           # (iii) fails: 30 years out, still a premium
print("Answer (i): its coupon is above its yield — investors pay more than face "
      "only to obtain a coupon better than the going rate.")
""")

# ---- D4 -------------------------------------------------------------------
md(r"""
**D4 (a).** A zero-coupon bond pays €100 in 8 years. The yield is 5%. Its price today.

$$P = \frac{100}{(1.05)^8}$$
""")
code(r"""
face, years, y = 100, 8, 0.05
growth = (1 + y) ** years             # 1.477455
P_zero_5 = face / growth
close(growth, 1.477455, 1e-6); close(P_zero_5, 67.68)
print(f"(1.05)^8 = {growth:.6f}, so the price is €{P_zero_5:.2f}.")
""")

md(r"""
**D4 (b).** If the yield rises to 6%, the new price and the percentage change.
""")
code(r"""
face, years, y_new = 100, 8, 0.06
growth = (1 + y_new) ** years         # 1.593848
P_zero_6 = face / growth
pct_change = (round(P_zero_6, 2) - round(P_zero_5, 2)) / round(P_zero_5, 2)
close(growth, 1.593848, 1e-6); close(P_zero_6, 62.74); close(pct_change, -0.0730, 1e-4)
print(f"New price €{P_zero_6:.2f}; change ({P_zero_6:.2f} − {P_zero_5:.2f})/{P_zero_5:.2f} = {pct_change:.2%}.")
""")

# ---- D5 -------------------------------------------------------------------
md(r"""
**D5 (a).** For the 5-year 4% bond priced at a 6% yield (D1): compute Macaulay duration, showing the weight of each cash flow.

$$D = \sum_t t \cdot w_t, \qquad w_t = \frac{PV_t}{P}$$
""")
code(r"""
table = cash_flow_table(0.04, 5, 0.06)
P = table["PV"].sum()
table["weight"] = table["PV"] / P
table["t·w"] = table["t"] * table["weight"]
print(table.round(4).to_string(index=False))
print(f"sum of PV = {P:.2f}, sum of weights = {table['weight'].sum():.4f}")
D_mac = table["t·w"].sum()              # same as table["t·PV"].sum() / P
close(table["weight"].sum(), 1.0, 1e-9); close(D_mac, 4.611, 0.001)
print(f"Macaulay duration = {D_mac:.2f} years: the PV-weighted average time to being repaid, "
      "under five because the coupons come back earlier.")
""")

md(r"""
**D5 (b).** Convert it to modified duration.

$$D_{mod} = \frac{D}{1+y}$$
""")
code(r"""
y = 0.06
D_mod = D_mac / (1 + y)
close(D_mod, 4.350, 0.001)
print(f"Modified duration = {D_mac:.4f} / {1 + y} = {D_mod:.3f} (drills.md: 4.611/1.06 = 4.350).")
""")

md(r"""
**D5 (c).** Estimate the price change if the yield rises by 50 basis points.

$$\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y$$
""")
code(r"""
dy = 0.005                              # 50 basis points
pct = -D_mod * dy                       # −2.17%
dP = round(pct * P_d1, 2)               # rounded to the cent, as on paper: −1.99
P_new = round(P_d1, 2) + dP
close(pct, -0.02175, 1e-4); close(dP, -1.99); close(P_new, 89.59)
print(f"ΔP/P ≈ −{D_mod:.3f} × {dy} = {pct:.2%}, i.e. about −€{-dP:.2f}, "
      f"giving roughly €{P_new:.2f}.")
""")

# ---- D6 -------------------------------------------------------------------
md(r"""
**D6 (a).** A 10-year bond with a 5% coupon trades at par (yield 5%). Its modified duration is 7.72. Estimate the new price if the yield rises to 6%.
""")
code(r"""
P0, D_mod_10, dy = 100, 7.72, 0.01
# Check the given 7.72 from the cash flows (Macaulay / (1 + y))
table = cash_flow_table(0.05, 10, 0.05)
print(table.round(4).to_string(index=False))
close(table["t·PV"].sum() / table["PV"].sum() / 1.05, 7.72, 0.005)
P_dur_only = P0 * (1 - D_mod_10 * dy)
close(P_dur_only, 92.28)
print(f"ΔP/P ≈ −{D_mod_10} × {dy} = {-D_mod_10*dy:.2%}, so P ≈ €{P_dur_only:.2f}.")
""")

md(r"""
**D6 (b).** The actual price at 6% is €92.64. Compare, and say which way the estimate errs.
""")
code(r"""
P_actual = price(0.05, 10, 0.06)        # recompute the "actual" price ourselves
close(P_actual, 92.64)
gap = P_actual - P_dur_only
close(gap, 0.36)
print(f"Actual €{P_actual:.2f} vs estimate €{P_dur_only:.2f}: the estimate is €{gap:.2f} too low. "
      "Duration alone overstates the loss (and understates the gain when yields fall).")
""")

# ---- D7 -------------------------------------------------------------------
md(r"""
**D7 (stretch).** Order by duration, longest first: (i) a 10-year zero-coupon bond (ii) a 10-year 8% coupon bond (iii) a 3-year 8% coupon bond.
""")
code(r"""
# The drill gives no yield: any yield gives the same order; we try three.
bonds = {"(i) 10y zero": (0.0, 10), "(ii) 10y 8%": (0.08, 10), "(iii) 3y 8%": (0.08, 3)}
for y in (0.03, 0.05, 0.08):
    mac = {}
    for name, (c, n) in bonds.items():
        t = cash_flow_table(c, n, y)
        mac[name] = t["t·PV"].sum() / t["PV"].sum()
    print(f"y = {y:.0%}: " + ", ".join(f"{k} {v:.2f}" for k, v in mac.items()))
    assert mac["(i) 10y zero"] > mac["(ii) 10y 8%"] > mac["(iii) 3y 8%"]
print("Order (i) > (ii) > (iii): a zero's duration is its full maturity, coupons pull "
      "(ii)'s average forward, and (iii) returns the money in three years instead of ten.")
""")

# ---- D8 -------------------------------------------------------------------
md(r"""
**D8 (a).** Using the D6 bond ($P = 100$, $D_{mod} = 7.72$, convexity $C = 75.0$), estimate the price at a yield of 6% using duration **and** convexity.

$$\frac{\Delta P}{P} \approx -D_{mod}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^2$$
""")
code(r"""
P0, D_mod_10, C, dy = 100, 7.72, 75.0, 0.01
duration_term = -D_mod_10 * dy          # −0.0772
convexity_term = 0.5 * C * dy ** 2      # +0.00375
pct = duration_term + convexity_term    # −0.07345
P_dur_conv = P0 * (1 + pct)
close(pct, -0.07345, 1e-9); close(P_dur_conv, 92.66)
print(f"ΔP/P ≈ {duration_term:.4f} + {convexity_term:.5f} = {pct:.5f}, so P ≈ €{P_dur_conv:.2f}.")
""")

md(r"""
**D8 (b).** Compare with the actual €92.64 and with the duration-only estimate from D6.
""")
code(r"""
err_dur = P_dur_only - P_actual         # about −0.36: below the truth
err_both = P_dur_conv - P_actual        # about +0.02: above the truth
close(err_dur, -0.36); close(err_both, 0.02)
print(pd.DataFrame({"estimate": ["duration only", "duration + convexity", "actual"],
                    "price €": [round(P_dur_only, 2), round(P_dur_conv, 2), round(P_actual, 2)]}
                   ).to_string(index=False))
print(f"Duration alone is €{abs(err_dur):.2f} below the truth; adding convexity leaves it only "
      f"€{err_both:.2f} above. The second term recovers almost all the curvature.")
""")

# ---- D9 -------------------------------------------------------------------
md(r"""
**D9 (the Board sentence).** In two sentences, no formulas: what does convexity buy the holder of a bond, and why does a risk manager care about it?
""")
code(r"""
# Show it on the D6 bond: yields up 1% and down 1%
for dy in (+0.01, -0.01):
    actual = price(0.05, 10, 0.05 + dy)
    straight_line = 100 * (1 - 7.72 * dy)
    print(f"yield {dy:+.0%}: actual €{actual:.2f}, duration line €{straight_line:.2f}, "
          f"holder better off by €{actual - straight_line:.2f}")
    assert actual > straight_line       # the curve beats the line on both sides
print("Convexity bends the price curve in the holder's favour: gains are bigger and losses "
      "smaller than duration predicts. A risk manager cares because a duration-only report "
      "overstates losses, and between equal durations the more convex bond is worth more.")
""")

# ---- D10 ------------------------------------------------------------------
md(r"""
**D10 (stretch).** Two bonds have the same duration; one has higher convexity. Rates move sharply, direction unknown. Which would you rather hold, and why?
""")
code(r"""
D_mod, C_low, C_high = 7.72, 40.0, 75.0     # same duration, different convexity
for dy in (-0.02, +0.02):                   # a sharp move either way
    low = 100 * (1 - D_mod * dy + 0.5 * C_low * dy ** 2)
    high = 100 * (1 - D_mod * dy + 0.5 * C_high * dy ** 2)
    print(f"yield {dy:+.0%}: less convex €{low:.2f}, more convex €{high:.2f}")
    assert high > low                       # the convex bond wins in both directions
print("The more convex one: same behaviour for small moves, but for a large move either way "
      "it gains more and loses less. That asymmetry is worth paying for.")
""")

# ---- D11 ------------------------------------------------------------------
md(r"""
**D11 (a).** Arno Bikes holds €400,000 of the D6 bond (at par) and €600,000 of a 2-year bond with modified duration 1.90. The portfolio's modified duration, weighting by market value.
""")
code(r"""
holdings = pd.DataFrame({"bond": ["10-year 5% (D6)", "2-year"],
                         "market value €": [400_000, 600_000],
                         "modified duration": [7.72, 1.90]})
V = holdings["market value €"].sum()
holdings["weight"] = holdings["market value €"] / V
holdings["weight × D_mod"] = holdings["weight"] * holdings["modified duration"]
print(holdings.to_string(index=False))
D_port = holdings["weight × D_mod"].sum()
close(D_port, 4.228, 1e-9)
print(f"Portfolio modified duration = 0.4(7.72) + 0.6(1.90) = {D_port:.3f}.")
""")

md(r"""
**D11 (b).** The estimated loss in euros if yields rise by 1% across the board.
""")
code(r"""
dy = 0.01
loss = -D_port * dy * V
close(loss, -42_280, 0.5)
print(f"ΔV ≈ −{D_port:.3f} × {dy} × €{V:,.0f} = −€{-loss:,.0f}.")
""")

md(r"""
**D11 (c).** One sentence to the Board.
""")
code(r"""
share = -loss / V
ten_year_part = 0.4 * 7.72 * dy * V         # the part of the loss from the ten-year bond
print(f"Loss {share:.1%} of the reserve; €{ten_year_part:,.0f} of it comes from the ten-year holding.")
assert 0.04 < share < 0.045 and ten_year_part / -loss > 0.7
print('"A one-point rise in yields costs the reserve about €42,000, a little over 4% of it; '
      'about three quarters of the exposure sits in the ten-year holding, and shortening that would '
      'cut it roughly in half."')
""")

md(r"""
## Homework and what comes next

`homework.md` — due Wednesday 28 October, lighter on purpose. **Reading week is for the midterm**, due Sunday 1 November on Turnitin.
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).with_name("session.ipynb"))
print("wrote session.ipynb")
