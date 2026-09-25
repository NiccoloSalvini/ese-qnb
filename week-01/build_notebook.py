"""Build week-01/session.ipynb with nbformat. Run from anywhere: python3 week-01/build_notebook.py"""
from pathlib import Path

import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-01_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 1 — Revision of mathematics, told as business decisions
**European School of Economics · Thu 24 Sep 2026 · Tutor: Niccolò Salvini**

Running case: **Arno Bikes**, e-bike assembler in Florence.
Fixed cost €60,000 / month · variable cost €400 / bike · list price €1,000.

This notebook is driven by the tutor. Every picture here is followed by the same computation **by hand on paper** — that is what the exam asks for.
""")

code(r"""
# Setup (Colab has plotly and sympy preinstalled; this is a no-op there)
import subprocess, sys
try:
    import plotly, sympy
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly", "sympy"])
import numpy as np
import plotly.graph_objects as go
import sympy as sp
np.set_printoptions(precision=3, suppress=True)
print("ready")
""")

# ---------------- A ----------------
md(r"""
## A. Launch or not? — break-even and equilibrium

**Question for the Board:** how many bikes a month before Arno Bikes stops losing money?

$$C(q) = 60{,}000 + 400\,q \qquad R(q) = 1{,}000\,q$$

Break-even is the quantity where the two lines cross: $R(q) = C(q)$.

*Business reading:* every bike contributes €600 (price minus variable cost); break-even is fixed cost ÷ contribution.
""")

code(r"""
FIXED, VC = 60_000, 400
q = np.linspace(0, 300, 301)

def breakeven_fig(prices=(700, 800, 900, 1000, 1200, 1400, 1600), fixed=FIXED):
    fig = go.Figure()
    frames = []
    for p in prices:
        be = fixed / (p - VC)
        frames.append(go.Frame(
            name=str(p),
            data=[go.Scatter(x=q, y=fixed + VC*q, name="Cost C(q)", line=dict(color="#c0392b", width=3)),
                  go.Scatter(x=q, y=p*q, name=f"Revenue R(q), p = €{p}", line=dict(color="#2471a3", width=3)),
                  go.Scatter(x=[be], y=[p*be], mode="markers+text", text=[f"break-even ≈ {be:.0f}"],
                             textposition="top left", marker=dict(size=12, color="black"), name="break-even")]))
    fig.add_traces(frames[3].data)
    fig.frames = frames
    fig.update_layout(
        title="Break-even: where revenue crosses cost",
        xaxis_title="bikes per month (q)", yaxis_title="€ per month", yaxis_range=[0, 300_000],
        sliders=[dict(active=3, currentvalue=dict(prefix="price €"),
                      steps=[dict(method="animate", label=f.name,
                                  args=[[f.name], dict(mode="immediate", frame=dict(duration=0, redraw=True))]) for f in frames])],
        template="plotly_white", height=480)
    return fig

breakeven_fig().show()
""")

md(r"""
**Bet before sliding:** what price makes break-even 50 bikes?

**Then:** the landlord raises the rent. Re-run the cell below and watch the cost line — same slope, higher intercept, crossing moves right. *This is exactly the mechanism behind the midterm's Q4 (a tariff shifts the cost schedule).*
""")

code(r"""
breakeven_fig(fixed=72_000).show()
""")

md(r"""
### Market equilibrium — two facts, two unknowns

$$Q_d = 1200 - 2p \qquad Q_s = -300 + 3p$$

Setting $Q_d = Q_s$: $\;1500 = 5p \Rightarrow p^* = 300,\; Q^* = 600$.

The algebra is the answer; the picture is the check.
""")

code(r"""
p = np.linspace(0, 600, 601)
Qd, Qs = 1200 - 2*p, -300 + 3*p
fig = go.Figure()
fig.add_scatter(x=Qd, y=p, name="Demand  Q = 1200 − 2p", line=dict(color="#2471a3", width=3))
fig.add_scatter(x=Qs, y=p, name="Supply  Q = −300 + 3p", line=dict(color="#c0392b", width=3))
fig.add_scatter(x=[600], y=[300], mode="markers+text", text=["(600, €300)"], textposition="middle right",
                marker=dict(size=12, color="black"), name="equilibrium")
fig.update_layout(title="Equilibrium (economists put price on the vertical axis)",
                  xaxis_title="bikes per month (Q)", yaxis_title="price (€)",
                  xaxis_range=[0, 1300], yaxis_range=[0, 600], template="plotly_white", height=450)
fig.show()
""")

# ---------------- B ----------------
md(r"""
## B. How many bikes? — quadratics

Price now responds to volume: $p(q) = 1600 - 4q$. Revenue is **price × quantity**, a rectangle whose sides pull in opposite directions:

$$R(q) = (1600 - 4q)\,q = 1600q - 4q^2$$

$$\pi(q) = R(q) - C(q) = -4q^2 + 1200q - 60{,}000$$

**Bet:** does selling more *always* bring more revenue?
""")

code(r"""
qq = np.linspace(0, 400, 401)
R = (1600 - 4*qq) * qq
fig = go.Figure()
frames = []
for q0 in range(0, 401, 25):
    p0 = 1600 - 4*q0
    frames.append(go.Frame(name=str(q0), data=[
        go.Scatter(x=qq, y=1600 - 4*qq, name="demand p(q)", line=dict(color="#7f8c8d", dash="dot"), yaxis="y2"),
        go.Scatter(x=[0, q0, q0, 0, 0], y=[0, 0, p0, p0, 0], fill="toself", fillcolor="rgba(36,113,163,0.25)",
                   line=dict(color="#2471a3"), name=f"rectangle p·q = {p0*q0:,.0f}", yaxis="y2"),
        go.Scatter(x=qq[qq <= q0], y=R[qq <= q0], name="revenue R(q)", line=dict(color="#2471a3", width=3)),
        go.Scatter(x=[q0], y=[p0*q0], mode="markers", marker=dict(size=10, color="black"), showlegend=False)]))
fig.add_traces(frames[6].data); fig.frames = frames
fig.update_layout(
    title="Revenue is the area of the rectangle price × quantity",
    xaxis_title="bikes (q)", yaxis=dict(title="revenue €", range=[0, 170_000]),
    yaxis2=dict(title="price €", overlaying="y", side="right", range=[0, 1700]),
    sliders=[dict(active=6, currentvalue=dict(prefix="q = "),
                  steps=[dict(method="animate", label=f.name,
                              args=[[f.name], dict(mode="immediate", frame=dict(duration=0, redraw=True))]) for f in frames])],
    template="plotly_white", height=500)
fig.show()
""")

md(r"""
### Where is profit zero? Where is it positive?

Divide by the common factor first: $\;q^2 - 300q + 15{,}000 = 0$

$$q = \frac{300 \pm \sqrt{300^2 - 4\cdot 15{,}000}}{2} = \frac{300 \pm \sqrt{30{,}000}}{2} \approx 63.4,\; 236.6$$

A downward parabola is **positive between its roots**: profitable for $63.4 < q < 236.6$.

**Bet before sliding:** at what fixed cost do the two break-evens merge into one?
""")

code(r"""
def profit_fig(fixed_values=(40_000, 50_000, 60_000, 70_000, 80_000, 90_000, 100_000)):
    qq = np.linspace(0, 320, 641)
    fig = go.Figure(); frames = []
    for F in fixed_values:
        pi = -4*qq**2 + 1200*qq - F
        disc = 300**2 - 4*(F/4)
        if disc > 0:
            r1, r2 = (300 - disc**0.5)/2, (300 + disc**0.5)/2
            label = f"roots {r1:.1f} and {r2:.1f} — profitable window"
        elif disc == 0:
            r1 = r2 = 150; label = "one root at 150 — single break-even"
        else:
            r1 = r2 = None; label = "no roots — no viable scale"
        data = [go.Scatter(x=qq, y=pi, name="profit π(q)", line=dict(color="#1e8449", width=3)),
                go.Scatter(x=qq, y=np.zeros_like(qq), name="zero", line=dict(color="black", width=1)),
                go.Scatter(x=[150], y=[-4*150**2 + 1200*150 - F], mode="markers+text", text=["vertex"],
                           textposition="top center", marker=dict(size=10, color="#1e8449"), name="vertex")]
        if r1 is not None:
            data.append(go.Scatter(x=[r1, r2], y=[0, 0], mode="markers", marker=dict(size=12, color="#c0392b"), name="roots"))
        frames.append(go.Frame(name=f"{F:,}", data=data, layout=go.Layout(title=f"Fixed cost €{F:,}: {label}")))
    fig.add_traces(frames[2].data); fig.frames = frames
    fig.update_layout(title=frames[2].layout.title, xaxis_title="bikes (q)", yaxis_title="profit €",
                      yaxis_range=[-60_000, 60_000],
                      sliders=[dict(active=2, currentvalue=dict(prefix="fixed cost €"),
                                    steps=[dict(method="animate", label=f.name,
                                                args=[[f.name], dict(mode="immediate", frame=dict(duration=0, redraw=True))]) for f in frames])],
                      template="plotly_white", height=480)
    return fig
profit_fig().show()
""")

md(r"""
Vertex: $q = -\dfrac{b}{2a} = 150$, $\pi(150) = 30{,}000$. Week 2 gives a tool that finds this point for **any** curve, not only parabolas.
""")

# ---------------- C ----------------
md(r"""
## C. How long to double? — exponentials and logarithms

Revenue €1.2M growing 12% a year: $\;R(t) = 1.2 \cdot 1.12^{\,t}$.

Linear growth adds the same **amount** each year; exponential growth adds the same **percentage**.

**Bet:** how many years to double?
""")

code(r"""
t = np.linspace(0, 12, 241)
lin = 1.2 + 0.144*t          # +12% of the *initial* revenue every year
expo = 1.2 * 1.12**t
t_double = np.log(2)/np.log(1.12)
fig = go.Figure()
fig.add_scatter(x=t, y=lin, name="linear: +€144k a year", line=dict(color="#7f8c8d", width=3))
fig.add_scatter(x=t, y=expo, name="exponential: ×1.12 a year", line=dict(color="#2471a3", width=3))
fig.add_hline(y=2.4, line=dict(color="black", dash="dash"), annotation_text="double (€2.4M)")
fig.add_scatter(x=[t_double], y=[2.4], mode="markers+text", text=[f"{t_double:.1f} yrs"], textposition="bottom right",
                marker=dict(size=12, color="black"), showlegend=False)
fig.update_layout(title="Same start, same first-year gain, different futures",
                  xaxis_title="years", yaxis_title="revenue (€M)", template="plotly_white", height=450)
fig.show()
print(f"ln 2 / ln 1.12 = {np.log(2):.4f} / {np.log(1.12):.4f} = {t_double:.2f} years")
""")

md(r"""
The unknown is in the exponent. No algebra so far reaches it — **that is what a logarithm is for**:

$$1.12^{\,t} = 2 \;\Longrightarrow\; t \ln 1.12 = \ln 2 \;\Longrightarrow\; t = \frac{\ln 2}{\ln 1.12} \approx 6.1$$

| rule | reading |
|---|---|
| $\ln(ab) = \ln a + \ln b$ | growth factors multiply → their logs add |
| $\ln(a/b) = \ln a - \ln b$ | a ratio of revenues becomes a difference |
| $\ln a^{k} = k \ln a$ | $k$ years of the same growth: the exponent comes down |
| $\log_b x = \ln x / \ln b$ | any base through the calculator's $\ln$ |

""")

code(r"""
# Growth-rate explorer: how sensitive is doubling time to g?
g = np.linspace(0.02, 0.30, 200)
fig = go.Figure()
fig.add_scatter(x=g*100, y=np.log(2)/np.log(1+g), name="ln 2 / ln(1+g)", line=dict(color="#2471a3", width=3))
fig.update_layout(title="Doubling time vs growth rate", xaxis_title="growth rate (% per year)",
                  yaxis_title="years to double", template="plotly_white", height=420)
fig.show()
""")

# ---------------- D ----------------
md(r"""
## D. Within tolerance — absolute value

Battery cells must be 500 Wh ± 15 Wh:

$$|c - 500| \le 15 \;\Longleftrightarrow\; 485 \le c \le 515 \;\Longleftrightarrow\; c \in [485, 515]$$

$|x-a|$ is the **distance** from $a$. "≤ b" is the closed interval; "> b" is the two tails.
""")

code(r"""
fig = go.Figure()
fig.add_scatter(x=[485, 515], y=[0, 0], mode="lines+markers", line=dict(color="#1e8449", width=8),
                marker=dict(size=14, symbol="line-ns-open"), name="|c − 500| ≤ 15")
fig.add_scatter(x=[500], y=[0], mode="markers+text", text=["500"], textposition="top center",
                marker=dict(size=10, color="black"), showlegend=False)
fig.add_scatter(x=[483], y=[0], mode="markers+text", text=["483 — rejected"], textposition="bottom center",
                marker=dict(size=12, color="#c0392b", symbol="x"), showlegend=False)
fig.update_layout(title="Tolerance band as an interval", xaxis_range=[470, 530], yaxis=dict(visible=False),
                  height=220, template="plotly_white", xaxis_title="Wh")
fig.show()
""")

# ---------------- drills, solved in code ----------------
md(r"""
## Drills, solved in code

This section is an optional companion: the code is **not examined**, the exam is on paper. Every drill in `drills.md` is solved here, one cell per question, with `sympy` doing the algebra you would do by hand. Do the drill on paper first, then run the cell and compare.
""")

code(r"""
# Symbols used in every drill below (real numbers, as on paper)
q, p, x, y, t, c = sp.symbols('q p x y t c', real=True)
print("symbols ready")
""")

# --- D1 ---
md(r"""
### D1 (a) — cost and revenue
Fixed costs €60,000 a month, variable cost €400 a bike, price €1,000. Write $C(q)$ and $R(q)$.
""")
code(r"""
C = 60000 + 400*q     # fixed part + variable part
R = 1000*q            # price x quantity
print("C(q) =", C, "   R(q) =", R)
assert C.subs(q, 0) == 60000 and R.subs(q, 1) == 1000
""")

md(r"""
### D1 (b) — break-even
Find the quantity where $R(q) = C(q)$.
""")
code(r"""
equation = sp.Eq(1000*q, 60000 + 400*q)
break_even = sp.solve(equation, q)[0]
contribution = 1000 - 400          # what each bike leaves after its own cost
print(f"Contribution per bike: €{contribution}")
print(f"Break-even: {break_even} bikes a month")
assert break_even == 100
""")

md(r"""
### D1 (c) — the rent goes up
Fixed costs become €72,000. New break-even? What happens to the cost line?
""")
code(r"""
new_break_even = sp.solve(sp.Eq(1000*q, 72000 + 400*q), q)[0]
shift = 72000 - 60000     # the intercept moves up, the slope (400) stays
print(f"New break-even: {new_break_even} bikes a month")
print(f"The cost line shifts up in parallel by €{shift:,}; the crossing moves right.")
assert new_break_even == 120
""")

# --- D2 ---
md(r"""
### D2 (a) — equilibrium
Demand $Q_d = 1200 - 2p$, supply $Q_s = -300 + 3p$. Find the equilibrium price and quantity.
""")
code(r"""
demand = 1200 - 2*p
supply = -300 + 3*p
p_star = sp.solve(sp.Eq(demand, supply), p)[0]
Q_star = demand.subs(p, p_star)
print(f"Equilibrium: price €{p_star}, quantity {Q_star} bikes a month")
assert p_star == 300 and Q_star == 600
""")

md(r"""
### D2 (b) — a €50 tax paid by sellers
Sellers now respond to $p - 50$. New supply and new equilibrium?
""")
code(r"""
supply_tax = sp.expand(-300 + 3*(p - 50))       # sellers keep p - 50
p_tax = sp.solve(sp.Eq(1200 - 2*p, supply_tax), p)[0]
Q_tax = (1200 - 2*p).subs(p, p_tax)
print("New supply: Q_s =", supply_tax)
print(f"New equilibrium: price €{p_tax}, quantity {Q_tax} bikes a month")
assert supply_tax == -450 + 3*p and p_tax == 330 and Q_tax == 540
""")

md(r"""
### D2 (c) — who pays the tax?
How much of the €50 is paid by buyers through a higher price?
""")
code(r"""
buyers_share = 330 - 300            # price after tax minus price before
sellers_keep = 330 - 50             # what sellers take home per bike
sellers_share = 300 - sellers_keep
print(f"Buyers pay €{buyers_share} of the €50 tax; sellers bear €{sellers_share}")
assert buyers_share == 30 and sellers_share == 20
""")

# --- D3 ---
md(r"""
### D3 — two models, two constraints
Model A takes 2 hours, model B 3 hours; 1,200 hours available; 500 bikes in total.
$$2x + 3y = 1200 \qquad x + y = 500$$
""")
code(r"""
hours = sp.Eq(2*x + 3*y, 1200)
total = sp.Eq(x + y, 500)
solution = sp.solve([hours, total], [x, y])
print(f"Plan: {solution[x]} of model A and {solution[y]} of model B")
assert solution[x] == 300 and solution[y] == 200
""")

# --- D3b ---
md(r"""
### D3b (a)
Solve $3q - 12 > 0$ and write the answer as an interval.
""")
code(r"""
answer = sp.solve_univariate_inequality(3*q - 12 > 0, q, relational=False)
print("q in", answer, "  i.e. (4, +oo)")
assert answer == sp.Interval.open(4, sp.oo)
""")

md(r"""
### D3b (b)
Solve $5 - 2q \ge 1$. *(Dividing by a negative number flips the sign.)*
""")
code(r"""
# -2q >= -4  ->  divide by -2 and FLIP the sign  ->  q <= 2
answer = sp.solve_univariate_inequality(5 - 2*q >= 1, q, relational=False)
print("q in", answer, "  i.e. (-oo, 2], or [0, 2] if q is a quantity")
assert answer == sp.Interval(-sp.oo, 2)
""")

md(r"""
### D3b (c)
Solve $400q + 60{,}000 \le 1{,}000q$.
""")
code(r"""
answer = sp.solve_univariate_inequality(400*q + 60000 <= 1000*q, q, relational=False)
print("q in", answer, "  i.e. [100, +oo)")
assert answer == sp.Interval(100, sp.oo)
""")

md(r"""
### D3b (d)
What does (c) say about Arno Bikes?
""")
code(r"""
# (c) is cost <= revenue: the break-even condition written as an inequality
lowest_safe_q = sp.Interval(100, sp.oo).inf
print(f"At {lowest_safe_q} bikes a month or more, Arno Bikes is not losing money.")
assert lowest_safe_q == 100
""")

# --- D4 ---
md(r"""
### D4 (a) — where profit is zero
$\pi(q) = -2q^2 + 600q - 40{,}000$. Find the quantities with zero profit.
""")
code(r"""
profit = -2*q**2 + 600*q - 40000
simpler = sp.expand(profit / -2)          # q^2 - 300q + 20000
discriminant = 300**2 - 4*20000
roots = sp.solve(sp.Eq(simpler, 0), q)
print("Divided by -2:", simpler, "   discriminant =", discriminant)
print(f"Profit is zero at q = {roots[0]} and q = {roots[1]} units")
assert discriminant == 10000 and roots == [100, 200]
""")

md(r"""
### D4 (b) — where the firm is profitable
For which quantities is $\pi(q) > 0$?
""")
code(r"""
profitable = sp.solve_univariate_inequality(profit > 0, q, relational=False)
# downward parabola (a = -2 < 0): positive between its roots
print("Profitable for q in", profitable, "  i.e. 100 < q < 200 units")
assert profitable == sp.Interval.open(100, 200)
""")

md(r"""
### D4 (c) — the vertex
Find the vertex of the parabola and interpret it.
""")
code(r"""
a_coef, b_coef = -2, 600
q_vertex = sp.Rational(-b_coef, 2*a_coef)     # -b / (2a)
max_profit = profit.subs(q, q_vertex)
print(f"Vertex: maximum profit €{int(max_profit):,} at {q_vertex} units")
assert q_vertex == 150 and max_profit == 5000
""")

# --- D5 ---
md(r"""
### D5 (a)
Solve $x^2 - 7x + 10 \le 0$.
""")
code(r"""
print("Factored:", sp.factor(x**2 - 7*x + 10))     # (x - 2)(x - 5)
answer = sp.solve_univariate_inequality(x**2 - 7*x + 10 <= 0, x, relational=False)
# upward parabola: <= 0 between its roots
print("x in", answer, "  i.e. [2, 5]")
assert answer == sp.Interval(2, 5)
""")

md(r"""
### D5 (b)
Solve $2x^2 + 3x - 2 > 0$.
""")
code(r"""
roots = sp.solve(2*x**2 + 3*x - 2, x)
print("Roots:", roots)
answer = sp.solve_univariate_inequality(2*x**2 + 3*x - 2 > 0, x, relational=False)
# upward parabola: > 0 outside its roots
print("x in", answer, "  i.e. x < -2 or x > 1/2")
assert answer == sp.Union(sp.Interval.open(-sp.oo, -2), sp.Interval.open(sp.Rational(1, 2), sp.oo))
""")

# --- D6 ---
md(r"""
### D6 — factor, cancel, check the sign
Simplify $\dfrac{(x-1)^2}{x - x^2}$, then evaluate at $x = 1.1$ and $x = 0.9$.
""")
code(r"""
print("Denominator factored:", sp.factor(x - x**2))        # -x(x - 1)
simplified = sp.cancel((x - 1)**2 / (x - x**2))            # valid for x != 0, 1
at_11 = float(simplified.subs(x, sp.Rational(11, 10)))
at_09 = float(simplified.subs(x, sp.Rational(9, 10)))
print("Simplified:", simplified)
print(f"At x = 1.1: {at_11:.3f}   At x = 0.9: {at_09:.3f}  -> the sign flips across x = 1")
assert sp.simplify(simplified - (-(x - 1)/x)) == 0
assert round(at_11, 3) == -0.091 and round(at_09, 3) == 0.111
""")

# --- D7 ---
md(r"""
### D7 (a) — simplify
$\ln(e^3)$, $\;\log_2 32$, $\;\ln\!\left(\dfrac{a^2 b}{c}\right)$
""")
code(r"""
a, b, cc = sp.symbols('a b c', positive=True)        # logs need positive numbers
first = sp.log(sp.exp(3))
second = sp.log(32, 2)                                # 2^5 = 32
third = sp.expand_log(sp.log(a**2 * b / cc))          # product, power and quotient rules
print("ln(e^3) =", first, "   log2(32) =", second)
print("ln(a^2 b / c) =", third)
assert first == 3 and second == 5
assert third == 2*sp.log(a) + sp.log(b) - sp.log(cc)
""")

md(r"""
### D7 (b) — solve for x
$3^x = 81$ and $10^x = 500$ (three decimals).
""")
code(r"""
x1 = sp.solve(sp.Eq(3**x, 81), x)[0]          # 81 = 3^4
x2 = sp.log(500, 10)                          # take log base 10 of both sides
x2_value = round(float(x2), 3)
print(f"3^x = 81   ->  x = {x1}")
print(f"10^x = 500 ->  x = {x2_value}")
assert x1 == 4 and x2_value == 2.699
""")

# --- D8 ---
md(r"""
### D8 (a) — revenue over time
€1.2M growing at 12% a year. Write revenue after $t$ years.
""")
code(r"""
revenue = sp.Rational(12, 10) * sp.Rational(112, 100)**t     # € millions
print("R(t) = 1.2 * 1.12**t   (€ millions, t in years)")
print(f"After 1 year: €{float(revenue.subs(t, 1)):.3f}M")
assert revenue.subs(t, 0) == sp.Rational(12, 10)
assert revenue.subs(t, 1) == sp.Rational(1344, 1000)
""")

md(r"""
### D8 (b) — years to double
Solve $1.12^t = 2$.
""")
code(r"""
# t * ln(1.12) = ln(2)
t_double = sp.log(2) / sp.log(sp.Rational(112, 100))
t_double_value = round(float(t_double), 1)
print(f"Doubling time: {t_double_value} years")
assert t_double_value == 6.1
""")

md(r"""
### D8 (c) — years to reach €3M
Solve $1.2 \cdot 1.12^t = 3$, i.e. $1.12^t = 2.5$.
""")
code(r"""
ratio = sp.Rational(3) / sp.Rational(12, 10)             # 2.5
t_3M = sp.log(ratio) / sp.log(sp.Rational(112, 100))
t_3M_value = round(float(t_3M), 1)
print(f"Revenue reaches €3M after {t_3M_value} years")
assert ratio == sp.Rational(5, 2) and t_3M_value == 8.1
""")

# --- D9 ---
md(r"""
### D9 (a)
Solve $5e^{0.03t} = 8$ for $t$.
""")
code(r"""
# divide by 5, then take ln of both sides: 0.03 t = ln(1.6)
t_solution = sp.solve(sp.Eq(5*sp.exp(sp.Rational(3, 100)*t), 8), t)[0]
t_value = round(float(t_solution), 1)
print(f"t = ln(1.6) / 0.03 = {t_value} years")
assert t_value == 15.7
""")

md(r"""
### D9 (b)
A competitor doubled revenue in 5 years. Implied constant annual growth rate?
""")
code(r"""
g = sp.symbols('g', positive=True)
g_solution = sp.solve(sp.Eq((1 + g)**5, 2), g)[0]      # 1 + g = 2^(1/5)
g_percent = round(float(g_solution) * 100, 1)
print(f"Implied growth: {g_percent}% a year")
assert g_percent == 14.9
""")

# --- D10 ---
md(r"""
### D10 (a) — tolerance
Cells must be 500 Wh ± 15 Wh. Absolute value, interval, and is 483 Wh acceptable?
""")
code(r"""
condition = sp.Abs(c - 500) <= 15
accepted = sp.solve_univariate_inequality(condition, c, relational=False)
ok_483 = accepted.contains(483)
print("|c - 500| <= 15  <=>  c in", accepted, "  i.e. [485, 515] Wh")
print("Is a 483 Wh cell acceptable?", "yes" if ok_483 else "no")
assert accepted == sp.Interval(485, 515) and ok_483 == False
""")

md(r"""
### D10 (b)
Solve $|x - 3| > 2$.
""")
code(r"""
answer = sp.solve_univariate_inequality(sp.Abs(x - 3) > 2, x, relational=False)
# distance from 3 bigger than 2: the two tails
print("x in", answer, "  i.e. x < 1 or x > 5")
assert answer == sp.Union(sp.Interval.open(-sp.oo, 1), sp.Interval.open(5, sp.oo))
""")

# --- D11 ---
md(r"""
### D11 (a)
Write $x \ge -3$ as an interval.
""")
code(r"""
answer = sp.solve_univariate_inequality(x >= -3, x, relational=False)
print("x >= -3  ->", answer, "  i.e. [-3, +oo)")
assert answer == sp.Interval(-3, sp.oo)
""")

md(r"""
### D11 (b)
Write $x > -3$ as an interval.
""")
code(r"""
answer = sp.solve_univariate_inequality(x > -3, x, relational=False)
print("x > -3  ->", answer, "  i.e. (-3, +oo)")
assert answer == sp.Interval.open(-3, sp.oo)
""")

md(r"""
### D11 (c)
Write $-3 < x \le 5$ as an interval.
""")
code(r"""
answer = sp.Interval.Lopen(-3, 5)     # open on the left, closed on the right
print("-3 < x <= 5  ->", answer, "  i.e. (-3, 5]")
assert answer.contains(5) and not answer.contains(-3)
""")

md(r"""
### D11 (d)
Domain of $f(x) = \sqrt{x + 3}$.
""")
code(r"""
# a square root needs a non-negative argument
domain = sp.solve_univariate_inequality(x + 3 >= 0, x, relational=False)
print("Domain of sqrt(x + 3):", domain, "  i.e. [-3, +oo)")
assert domain == sp.Interval(-3, sp.oo)
""")

md(r"""
### D11 (e)
Domain of $g(x) = \ln(x - 1)$.
""")
code(r"""
# a logarithm needs a strictly positive argument
domain = sp.solve_univariate_inequality(x - 1 > 0, x, relational=False)
print("Domain of ln(x - 1):", domain, "  i.e. (1, +oo)")
assert domain == sp.Interval.open(1, sp.oo)
""")

md(r"""
## Three take-home lines

Write yours on paper before leaving:

1. …
2. …
3. …
""")

nb.cells = cells
nbf.write(nb, Path(__file__).parent / "session.ipynb")
print("written session.ipynb with", len(cells), "cells")
