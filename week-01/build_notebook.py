"""Build week-01/session.ipynb with nbformat. Run: python build_notebook.py"""
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
print(f"ln 2 / ln 1.12 = {np.log(2):.4f} / {np.log(1.12):.4f} = {t_double:.2f} years   (rule of 70: {70/12:.1f})")
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

Rule of 70: $t_{double} \approx 70/g_{\%}$, because $\ln 2 \approx 0.69$ and $\ln(1+g) \approx g$ for small $g$.
""")

code(r"""
# Growth-rate explorer: how sensitive is doubling time to g?
g = np.linspace(0.02, 0.30, 200)
fig = go.Figure()
fig.add_scatter(x=g*100, y=np.log(2)/np.log(1+g), name="exact  ln2 / ln(1+g)", line=dict(color="#2471a3", width=3))
fig.add_scatter(x=g*100, y=70/(g*100), name="rule of 70", line=dict(color="#c0392b", dash="dash", width=2))
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

# ---------------- checks ----------------
md(r"""
## Tutor's safety net — sympy checks of every drill answer

*(Collapsed in class. Run if a student's answer disagrees with yours.)*
""")

code(r"""
x, q, p, t = sp.symbols('x q p t', real=True)
checks = {
 "D1b break-even": sp.solve(sp.Eq(1000*q, 60000 + 400*q), q),
 "D1c new break-even": sp.solve(sp.Eq(1000*q, 72000 + 400*q), q),
 "D2a equilibrium": sp.solve([sp.Eq(1200 - 2*p, -300 + 3*p)], p),
 "D2b with tax": sp.solve(sp.Eq(1200 - 2*p, -450 + 3*p), p),
 "D3 models": sp.solve([sp.Eq(2*x + 3*q, 1200), sp.Eq(x + q, 500)], [x, q]),
 "D4a roots": [sp.N(r, 4) for r in sp.solve(-2*q**2 + 600*q - 40000, q)],
 "D4c vertex": (150, -2*150**2 + 600*150 - 40000),
 "D5a": sp.solve_univariate_inequality(x**2 - 7*x + 10 <= 0, x),
 "D5b": sp.solve_univariate_inequality(2*x**2 + 3*x - 2 > 0, x),
 "D6 simplify": sp.simplify((x-1)**2 / (x - x**2)),
 "D7b 10^x=500": sp.N(sp.log(500, 10), 4),
 "D8b doubling": sp.N(sp.log(2)/sp.log(sp.Rational(112, 100)), 4),
 "D8c to 3M": sp.N(sp.log(sp.Rational(5, 2))/sp.log(sp.Rational(112, 100)), 4),
 "D9a": sp.N(sp.solve(sp.Eq(5*sp.exp(sp.Rational(3, 100)*t), 8), t)[0], 4),
 "D9b growth": sp.N(2**sp.Rational(1, 5) - 1, 4),
 "D10b": sp.solve_univariate_inequality(sp.Abs(x - 3) > 2, x),
 "Arno roots": [sp.N(r, 4) for r in sp.solve(-4*q**2 + 1200*q - 60000, q)],
}
for k, v in checks.items():
    print(f"{k:22s} → {v}")
""")

md(r"""
## Three take-home lines

Write yours on paper before leaving:

1. …
2. …
3. …
""")

nb.cells = cells
nbf.write(nb, "session.ipynb")
print("written session.ipynb with", len(cells), "cells")
