"""Build week-02/session.ipynb with nbformat. Run: python build_notebook.py"""
import nbformat as nbf

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

md(r"""
### 🔍 CHECK — the drills, verified

Every answer in `drills.md` should survive this cell. If one does not, the drill is wrong and I want to know.
""")
code(r"""
checks = {
    "D8a  π'": (sp.diff(-4*q**2 + 1200*q - 60000, q), -8*q + 1200),
    "D8c  R'": (sp.diff(30*sp.log(q + 1), q), 30/(q + 1)),
    "D11  f ": (sp.integrate(6*q**2 - 2*q, q) + 3, 2*q**3 - q**2 + 3),
    "D12  C ": (sp.integrate(sp.Rational(8,10)*q + 3, q) + 25, sp.Rational(4,10)*q**2 + 3*q + 25),
}
for name, (got, want) in checks.items():
    print(f"{'ok  ' if sp.simplify(got - want) == 0 else 'MISMATCH'} {name}: {got}")
""")

md(r"""
## Homework

`homework.md` — eight drills on paper plus a memo to the Board: **should the eighty-first bike be built?**
Due Wednesday 7 October, 23:59, on Moodle.
""")

nb["cells"] = cells
nbf.write(nb, "session.ipynb")
print("wrote session.ipynb")
