"""Build week-03/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-03_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 3 — Studying a function, and adding one up
**European School of Economics · Thu 8 Oct 2026 · Tutor: Niccolò Salvini**

Today is the mathematical content of the midterm: the seven-step study, optimisation, and integration.
""")

code(r"""
import subprocess, sys
try:
    import plotly, sympy
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly", "sympy"])
import numpy as np, plotly.graph_objects as go, sympy as sp
q = sp.Symbol("q", positive=True)
print("ready")
""")

md(r"""
## A. The seven steps, done by machine so you can check yourself

Do it on paper first. This cell is the answer key, not the method.
""")
code(r"""
def study(f, name="f"):
    fp, fpp = sp.diff(f, q), sp.diff(f, q, 2)
    print(f"{name}(q) = {f}")
    print("  1 domain     :", sp.calculus.util.continuous_domain(f, q, sp.Interval(0, sp.oo)))
    print("  2 zeros      :", [round(float(r), 3) for r in sp.solve(f, q) if r.is_real])
    print(f"  3 f'         : {fp}")
    stat = sp.solve(fp, q)
    print("  4 stationary :", stat)
    for s in stat:
        kind = "maximum" if fpp.subs(q, s) < 0 else ("minimum" if fpp.subs(q, s) > 0 else "unclear")
        print(f"  5 at q={float(s):.3f}: f''={float(fpp.subs(q, s)):.3f} → {kind}, f={float(f.subs(q, s)):,.2f}")
    print("  6 f''        :", fpp, "  inflection at:", sp.solve(fpp, q))
    print("  7 as q→∞     :", sp.limit(f, q, sp.oo))

study(-4*q**2 + 1200*q - 60000, "π")
""")

md(r"""
## B. Average cost meets marginal cost

Where does the average stop falling? Move the slider and watch the two curves.
""")
code(r"""
C  = lambda x: 0.4*x**2 + 3*x + 25
AC = lambda x: C(x)/x
MC = lambda x: 0.8*x + 3
xs = np.linspace(1.5, 18, 300)

fig = go.Figure([
    go.Scatter(x=xs, y=AC(xs), name="average cost C(q)/q", line=dict(color="#363636", width=3)),
    go.Scatter(x=xs, y=MC(xs), name="marginal cost C'(q)", line=dict(color="#AF1F25", width=3)),
])
qstar = float(np.sqrt(62.5))
fig.add_scatter(x=[qstar], y=[AC(qstar)], mode="markers+text", marker=dict(size=13, color="#CDBA80"),
                text=[f"q* = {qstar:.2f}"], textposition="top right", showlegend=False)
fig.update_layout(template="simple_white", height=460, xaxis_title="q",
                  yaxis_title="€ thousand per unit", yaxis_range=[0, 20])
fig.show()
""")
code(r"""
Cs = sp.Rational(4,10)*q**2 + 3*q + 25
ACs = sp.simplify(Cs/q)
qm = [s for s in sp.solve(sp.diff(ACs, q), q) if s.is_real and s > 0][0]
print(f"AC is lowest at q = {float(qm):.4f}")
print(f"  AC there = {float(ACs.subs(q, qm)):.4f}")
print(f"  MC there = {float(sp.diff(Cs, q).subs(q, qm)):.4f}   ← equal, and not by accident")
""")

md(r"""
## C. Optimisation — marginal revenue equals marginal cost

A firm with log revenue. Change the 30 and watch the optimum move.
""")
code(r"""
for a in (20, 30, 40, 60):
    pi = a*sp.log(q + 1) - Cs
    root = [r for r in sp.solve(sp.Eq(sp.diff(pi, q), 0), q) if r.is_real and r > 0]
    if root:
        qs_ = float(root[0])
        print(f"R = {a} ln(q+1):  q* = {qs_:6.3f},  π(q*) = {float(pi.subs(q, root[0])):>8,.2f}k")
""")

md(r"""
### 🔍 CHECK
One of those rows has a positive optimum and a **negative** profit. Find it, and say what a manager should do in that case. Maximising profit and making a profit are not the same thing.
""")

md(r"""
## D. Integration — thinner slices, truer area

`MC(q) = 0.8q + 3`. What do the first twenty bikes cost in total?
""")
code(r"""
mc = lambda x: 0.8*x + 3
exact = 0.4*20**2 + 3*20
for n in (4, 8, 20, 60, 500):
    dx = 20/n
    left = sum(mc(i*dx)*dx for i in range(n))
    print(f"n = {n:>3}  left-endpoint sum = {left:7.2f}   (exact {exact})")
""")
code(r"""
print("∫ (q⁵ − 3q³ + 2)/q² dq =", sp.integrate((q**5 - 3*q**3 + 2)/q**2, q), "+ c")
print("∫₀²⁰ (0.8q + 3) dq     =", sp.integrate(sp.Rational(8,10)*q + 3, (q, 0, 20)))
print()
pi = -4*q**2 + 1200*q - 60000
print("∫₁₀₀¹⁵⁰ π'(q) dq =", sp.integrate(sp.diff(pi, q), (q, 100, 150)))
print("π(150) − π(100)  =", pi.subs(q, 150) - pi.subs(q, 100), " ← the same number")
""")

md(r"""
**The integral of the marginal is the change in the total.** That sentence is the whole of integration.

## Homework

`homework.md` — seven drills plus a **400–500 word Board report**: a dry run of the midterm, sketch included.
Due Wednesday 14 October, 23:59.
""")

nb["cells"] = cells
nbf.write(nb, "session.ipynb")
print("wrote session.ipynb")
