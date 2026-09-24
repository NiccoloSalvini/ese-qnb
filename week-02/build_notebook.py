"""Build week-02/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf
from pathlib import Path

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-02_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 2 — The tool that finds the top of any hill
**European School of Economics · Thu 1 Oct 2026 · Tutor: Niccolò Salvini**

Running case: **Arno Bikes**. `C(q) = 60,000 + 400q`, `p(q) = 1600 − 4q`, so `π(q) = −4q² + 1200q − 60,000`.

This notebook is driven from the projector. Every picture here is followed by the same computation **by hand on paper** — that is what the exam asks for.
""")

code(r"""
import subprocess, sys
try:
    import plotly, sympy
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly", "sympy"])
import numpy as np, plotly.graph_objects as go, sympy as sp
q = sp.Symbol("q", real=True)
print("ready")
""")

md(r"""
## A. Domain — where a function means anything

The exam asks "state the domain" and wants an interval. Sympy agrees with you or it does not.
""")
code(r"""
for expr in (sp.sqrt(q - 20), sp.log(q - 5), 120/(q - 40)):
    print(f"{str(expr):<18} domain: {sp.calculus.util.continuous_domain(expr, q, sp.S.Reals)}")
""")

md(r"""
## B. Limits — near a point you cannot reach

Average cost at zero output is undefined. Near zero, and far out, it is not.
""")
code(r"""
AC = (60000 + 400*q)/q
print("as q -> 0+ :", sp.limit(AC, q, 0, "+"))
print("as q -> oo :", sp.limit(AC, q, sp.oo))
print()
print("(q^2-100)/(q-10) as q->10 :", sp.limit((q**2 - 100)/(q - 10), q, 10))
print("(q-1)^2/(q-q^2)  as q->1+ :", sp.limit((q - 1)**2/(q - q**2), q, 1, "+"))
""")

md(r"""
### 🔍 CHECK
The second one is `0/0`. Factor it by hand first, then compare. If your hand answer and sympy disagree, sympy is not the one that is wrong — but find out *where* you diverged before moving on.
""")

md(r"""
## C. The derivative — what does one more bike do?

Move the point along the curve and read the slope. The slope is the answer to the only question a manager asks about the next unit.
""")
code(r"""
profit = lambda x: -4*x**2 + 1200*x - 60000
prime  = lambda x: -8*x + 1200
qs = np.linspace(0, 300, 400)

frames, points = [], np.arange(20, 281, 10)
for q0 in points:
    xs = np.linspace(q0 - 60, q0 + 60, 2)
    frames.append(go.Frame(name=str(q0), data=[
        go.Scatter(x=qs, y=profit(qs), line=dict(color="#363636", width=3)),
        go.Scatter(x=xs, y=profit(q0) + prime(q0)*(xs - q0), line=dict(color="#AF1F25", width=3)),
        go.Scatter(x=[q0], y=[profit(q0)], mode="markers+text", marker=dict(size=12, color="#AF1F25"),
                   text=[f"π'({q0}) = {prime(q0):+,.0f}"], textposition="top center"),
    ]))

fig = go.Figure(data=frames[0].data, frames=frames)
fig.update_layout(
    template="simple_white", height=480, showlegend=False,
    xaxis_title="bikes per month  q", yaxis_title="profit €",
    xaxis_range=[0, 300], yaxis_range=[-70000, 45000],
    sliders=[dict(active=0, currentvalue=dict(prefix="q = "),
                  steps=[dict(method="animate", label=f.name,
                              args=[[f.name], dict(mode="immediate", frame=dict(duration=0, redraw=True))])
                         for f in frames])])
fig.show()
""")

md(r"""
**Watch the sign, not the number.** Positive: make more. Negative: make fewer. Zero: you are at the top.
""")

code(r"""
pi = -4*q**2 + 1200*q - 60000
print("π'(q) =", sp.diff(pi, q))
print("π'(80)  =", sp.diff(pi, q).subs(q, 80), " → one more bike adds about €560")
print("π'(200) =", sp.diff(pi, q).subs(q, 200), " → one more bike costs about €400")
print("π'(q) = 0 at q =", sp.solve(sp.diff(pi, q), q))
print("week 1's vertex -b/2a =", -1200/(2*-4))
""")

md(r"""
### Change one number and watch everything move

The price falls €4 for each extra bike. What if it fell €3? Or €6?
""")
code(r"""
for drop in (3, 4, 6):
    p = (1600 - drop*q)*q - (60000 + 400*q)
    qstar = sp.solve(sp.diff(p, q), q)[0]
    print(f"price drop €{drop}/bike → best quantity {float(qstar):6.1f}, profit €{float(p.subs(q, qstar)):>10,.0f}")
""")

md(r"""
## D. Running it backwards

Given the derivative, recover the function. The constant is not decoration.
""")
code(r"""
c = sp.Symbol("c")
F = sp.integrate(6*q**2 - 2*q, q)
k = sp.solve(sp.Eq((F + c).subs(q, 1), 4), c)[0]
print("f'(q) = 6q² − 2q, f(1) = 4  →  f(q) =", F + k)

MC = sp.Rational(8, 10)*q + 3
print("MC(q) = 0.8q + 3 with C(0) = 25  →  C(q) =", sp.integrate(MC, q) + 25)
print("...and the constant IS the fixed cost.")
""")

# ---------------------------------------------------------------------------
# Drills, solved in code — one markdown + one code cell per drill in drills.md
# ---------------------------------------------------------------------------
md(r"""
## Drills, solved in code

This section is an optional companion: the code is **not examined**, but it is a good way to check your work. Every drill from `drills.md` is solved here with sympy, step by step, the way you would solve it by hand. Do the drill on paper first, then run the cell and compare.
""")

md(r"""
**D1 (a)** State the domain of $f(q) = \sqrt{q - 20}$.
""")
code(r"""
from sympy import solve_univariate_inequality
# A square root needs a non-negative inside
domain = solve_univariate_inequality(q - 20 >= 0, q, relational=False)
print("Domain of sqrt(q - 20):", domain)
assert domain == sp.Interval(20, sp.oo)
""")

md(r"""
**D1 (b)** State the domain of $g(q) = \ln(q - 5)$.
""")
code(r"""
# A logarithm needs a strictly positive inside (ln 0 does not exist)
domain = solve_univariate_inequality(q - 5 > 0, q, relational=False)
print("Domain of ln(q - 5):", domain)
assert domain == sp.Interval.open(5, sp.oo)
""")

md(r"""
**D1 (c)** State the domain of $h(q) = \dfrac{120}{q - 40}$.
""")
code(r"""
# A fraction needs a denominator different from zero
domain = solve_univariate_inequality(sp.Ne(q - 40, 0), q, relational=False)
print("Domain of 120/(q - 40):", domain)
# For a quantity we also need q >= 0
print("For a quantity:", domain.intersect(sp.Interval(0, sp.oo)))
assert domain == sp.Union(sp.Interval.open(-sp.oo, 40), sp.Interval.open(40, sp.oo))
""")

md(r"""
**D2 (a)** Arno Bikes faces demand $p(q) = 1600 - 4q$. Write revenue $R(q)$ and simplify.
""")
code(r"""
price = 1600 - 4*q
R = sp.expand(price * q)          # revenue = price x quantity
print("R(q) =", R)
assert R == 1600*q - 4*q**2
""")

md(r"""
**D2 (b)** Write profit $\pi(q)$ using $C(q) = 60{,}000 + 400q$.
""")
code(r"""
C = 60000 + 400*q
pi_q = sp.expand(R - C)           # profit = revenue - cost
print("π(q) =", pi_q)
assert pi_q == -4*q**2 + 1200*q - 60000
""")

md(r"""
**D2 (c)** Evaluate $\pi(100)$ and $\pi(200)$. Which quantity is better, and by how much?
""")
code(r"""
p100 = int(pi_q.subs(q, 100))
p200 = int(pi_q.subs(q, 200))
print(f"π(100) = €{p100:,}   π(200) = €{p200:,}   difference = €{p200 - p100:,}")
print("They are equal: the parabola is symmetric about q = 150.")
assert p100 == 20000 and p200 == 20000
""")

md(r"""
**D3 (a)** A second firm has $R(q) = 30\ln(q + 1)$ (€ thousand). State the domain of $R$ for $q \ge 0$.
""")
code(r"""
# The log needs q + 1 > 0; then keep only quantities q >= 0
domain = solve_univariate_inequality(q + 1 > 0, q, relational=False)
domain_q = domain.intersect(sp.Interval(0, sp.oo))
print("Domain of 30 ln(q + 1):", domain, "  for a quantity:", domain_q)
assert domain_q == sp.Interval(0, sp.oo)
""")

md(r"""
**D3 (b)** With $C(q) = 0.4q^2 + 3q + 25$, compute $\pi(5)$ and $\pi(10)$ to two decimals.
""")
code(r"""
R2 = 30*sp.log(q + 1)
C2 = sp.Rational(4, 10)*q**2 + 3*q + 25
profit2 = R2 - C2
pi5 = round(float(profit2.subs(q, 5)), 2)
pi10 = round(float(profit2.subs(q, 10)), 2)
print(f"π(5) = €{pi5}k   π(10) = €{pi10}k  → past its best scale at 10")
assert pi5 == 3.75
assert pi10 == -23.06   # 30 ln 11 = 71.94, so 71.94 - 95 = -23.06
""")

md(r"""
**D4 (a)** Evaluate $\displaystyle\lim_{q\to 10} \frac{q^2 - 100}{q - 10}$, showing the factoring step.
""")
code(r"""
expr = (q**2 - 100)/(q - 10)
print("numerator factored:", sp.factor(q**2 - 100))
print("after cancelling:  ", sp.cancel(expr))
answer = sp.limit(expr, q, 10)
print("The limit as q → 10 is", answer)
assert answer == 20
""")

md(r"""
**D4 (b)** Evaluate $\displaystyle\lim_{q\to 3} \frac{q^2 - 5q + 6}{q - 3}$, showing the factoring step.
""")
code(r"""
expr = (q**2 - 5*q + 6)/(q - 3)
print("numerator factored:", sp.factor(q**2 - 5*q + 6))
print("after cancelling:  ", sp.cancel(expr))
answer = sp.limit(expr, q, 3)
print("The limit as q → 3 is", answer)
assert answer == 1
""")

md(r"""
**D5** Evaluate the one-sided limit $\displaystyle\lim_{q\to 1^+} \frac{(q - 1)^2}{q - q^2}$.
""")
code(r"""
expr = (q - 1)**2/(q - q**2)
print("denominator factored:", sp.factor(q - q**2))   # -q(q - 1)
print("after cancelling:    ", sp.cancel(expr))       # -(q - 1)/q
answer = sp.limit(expr, q, 1, dir="+")                # from above only
print("The limit as q → 1 from above is", answer)
assert answer == 0
""")

md(r"""
**D6 (a)** Evaluate $\displaystyle\lim_{q\to\infty} \frac{1200q - 4q^2}{q^2}$ and say what it means for the firm.
""")
code(r"""
expr = (1200*q - 4*q**2)/q**2
print("divided through by q²:", sp.expand(expr))    # 1200/q - 4
answer = sp.limit(expr, q, sp.oo)
print("The limit is", answer, "→ far out, the -4q² term dominates: deep loss.")
assert answer == -4
""")

md(r"""
**D6 (b)** Evaluate $\displaystyle\lim_{q\to\infty} \frac{60{,}000 + 400q}{q}$ — average cost per bike as the run gets long.
""")
code(r"""
AC = (60000 + 400*q)/q
print("split the fraction:", sp.expand(AC))          # 60000/q + 400
answer = sp.limit(AC, q, sp.oo)
print(f"Average cost settles at €{answer} per bike: fixed cost spreads to nothing.")
assert answer == 400
""")

md(r"""
**D7** Evaluate $\displaystyle\lim_{q\to -\infty} \frac{3q^3 - 2q + 1}{5q^3 + q^2}$.
""")
code(r"""
expr = (3*q**3 - 2*q + 1)/(5*q**3 + q**2)
# Divide top and bottom by q³: every other term goes to 0
answer = sp.limit(expr, q, -sp.oo)
print("The limit as q → -∞ is", answer, "(ratio of the leading coefficients)")
assert answer == sp.Rational(3, 5)
""")

md(r"""
**D8** Differentiate, term by term:
(a) $\pi(q) = -4q^2 + 1200q - 60{,}000$ (b) $C(q) = 0.4q^2 + 3q + 25$ (c) $R(q) = 30\ln(q + 1)$ (d) $f(q) = 5q^3 - 2q^2 + 7q - 1$
""")
code(r"""
d_a = sp.diff(-4*q**2 + 1200*q - 60000, q)
d_b = sp.diff(sp.Rational(4, 10)*q**2 + 3*q + 25, q)
d_c = sp.diff(30*sp.log(q + 1), q)
d_d = sp.diff(5*q**3 - 2*q**2 + 7*q - 1, q)
print("(a) π'(q) =", d_a, "  (b) C'(q) =", d_b)
print("(c) R'(q) =", d_c, "  (d) f'(q) =", d_d)
assert d_a == -8*q + 1200 and d_b == sp.Rational(8, 10)*q + 3
assert d_c == 30/(q + 1) and d_d == 15*q**2 - 4*q + 7
""")

md(r"""
**D8b** Differentiate, naming the inside each time:
(a) $\ln(q + 1)$ (b) $\ln(5q)$ (c) $(3q - 4)^5$ (d) $e^{0.08t}$ (e) $20\ln(2q + 7)$
""")
code(r"""
t = sp.Symbol("t", real=True)
d_a = sp.diff(sp.log(q + 1), q)                  # inside q + 1, times 1
d_b = sp.simplify(sp.diff(sp.log(5*q), q))       # inside 5q, times 5
d_c = sp.diff((3*q - 4)**5, q)                   # inside 3q - 4, times 3
d_d = sp.diff(sp.exp(0.08*t), t)                 # inside 0.08t, times 0.08
d_e = sp.diff(20*sp.log(2*q + 7), q)             # inside 2q + 7, times 2
print("(a)", d_a, " (b)", d_b, " (c)", d_c, " (d)", d_d, " (e)", d_e)
assert (d_a, d_b, d_c) == (1/(q + 1), 1/q, 15*(3*q - 4)**4)
assert d_d == 0.08*sp.exp(0.08*t) and d_e == 40/(2*q + 7)
""")

md(r"""
**D9 (a)** For $\pi(q) = -4q^2 + 1200q - 60{,}000$, compute $\pi'(80)$ and say what it means for a manager.
""")
code(r"""
marginal = sp.diff(-4*q**2 + 1200*q - 60000, q)   # -8q + 1200
m80 = marginal.subs(q, 80)
print(f"π'(80) = {m80}: at 80 bikes a month, one more bike adds about €{m80} to profit. Make more.")
assert m80 == 560
""")

md(r"""
**D9 (b)** Compute $\pi'(200)$ and say what it means.
""")
code(r"""
m200 = marginal.subs(q, 200)
print(f"π'(200) = {m200}: at 200 bikes, one more bike costs about €{-m200} of profit. Make fewer.")
assert m200 == -400
""")

md(r"""
**D9 (c)** Solve $\pi'(q) = 0$ and compare with the week-1 vertex $-b/2a$.
""")
code(r"""
q_best = sp.solve(sp.Eq(marginal, 0), q)[0]
vertex = sp.Rational(-1200, 2*(-4))                # -b / 2a from week 1
print(f"π'(q) = 0 at q = {q_best}; the week-1 vertex is q = {vertex}. Same point.")
assert q_best == 150 and vertex == 150
""")

md(r"""
**D10** Using the definition $f'(a) = \lim_{h\to 0} \frac{f(a+h) - f(a)}{h}$, show that the derivative of $f(q) = 3q^2$ at $q = a$ is $6a$.
""")
code(r"""
a, h = sp.symbols("a h", real=True)
f = lambda x: 3*x**2
quotient = (f(a + h) - f(a))/h
print("difference quotient, simplified:", sp.cancel(quotient))   # 6a + 3h
answer = sp.limit(quotient, h, 0)
print("Letting h → 0, f'(a) =", answer)
assert answer == 6*a
""")

md(r"""
**D11** Find $f(q)$ given $f'(q) = 6q^2 - 2q$ and $f(1) = 4$.
""")
code(r"""
c = sp.Symbol("c")
f = sp.integrate(6*q**2 - 2*q, q) + c          # antiderivative + constant
print("general solution: f(q) =", f)
c_value = sp.solve(sp.Eq(f.subs(q, 1), 4), c)[0]   # use f(1) = 4
f = f.subs(c, c_value)
print(f"f(1) = 4 gives c = {c_value}, so f(q) = {f}")
assert sp.expand(f - (2*q**3 - q**2 + 3)) == 0
""")

md(r"""
**D12** Find the total cost function given marginal cost $MC(q) = 0.8q + 3$ and fixed cost $C(0) = 25$.
""")
code(r"""
c = sp.Symbol("c")
C = sp.integrate(sp.Rational(8, 10)*q + 3, q) + c   # antiderivative + constant
c_value = sp.solve(sp.Eq(C.subs(q, 0), 25), c)[0]   # use C(0) = 25
C = C.subs(c, c_value)
print(f"C(0) = 25 gives c = {c_value}, so C(q) = {C}. The constant IS the fixed cost.")
assert sp.expand(C - (sp.Rational(4, 10)*q**2 + 3*q + 25)) == 0
""")

md(r"""
## Homework

`homework.md` — eight drills on paper plus a memo to the Board: **should the eighty-first bike be built?**
Due Wednesday 7 October, 23:59, on Moodle.
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).with_name("session.ipynb"))
print("wrote session.ipynb")
