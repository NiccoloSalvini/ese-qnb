"""Build week-07/session.ipynb with nbformat. Run: python3.11 week-07/build_notebook.py
then: python3.11 -m jupyter nbconvert --to notebook --execute --inplace week-07/session.ipynb"""
from pathlib import Path
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-07_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 7 — The founder does not know the numbers
**European School of Economics · Mon 9 Nov 2026 · Tutor: Vincenzo Nardelli**

In weeks 1–5 every number at **Arno Bikes** was given: a fixed cost, a list price, a coupon. This quarter the founder asks four questions she cannot answer with a given number — how many customers do both, which supplier sent the faulty battery, how many returns next week, what range to print on the box. Each answer comes with a spread.

This notebook is driven by the tutor. Every picture is followed by the same computation **by hand on paper**: formula, substitution, number, one sentence for the Board. The code is optional and not examined.
""")

code(r"""
# Setup (Colab has plotly preinstalled; this is a no-op there)
import subprocess, sys
try:
    import plotly
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly"])
import math
import numpy as np, pandas as pd
from scipy import stats
import plotly.graph_objects as go

RED, GOLD, GREY = "#AF1F25", "#CDBA80", "#7a7f85"
print("ready")
""")

# ---------------- A ----------------
md(r"""
## A. How many of our customers do both? — sets and counting

The CRM says: of **200** customers, **120** bought accessories, **90** a service plan, **40** neither. The founder wants to upsell the ones who bought **both**.

$$n(A \cup S) = n(A) + n(S) - n(A \cap S)$$

*Business reading:* "or" adds the two counts, then takes the overlap out once — otherwise the "both" customers are counted twice.

Then counting: eight people work at Arno Bikes, three go to the Milan trade fair. **Does swapping two people change the outcome?** No → combinations. Yes (named roles) → permutations.
""")

code(r"""
def venn_count(N, nA, nB, neither, A="accessories", B="service plan"):
    # Four regions of a two-circle Venn diagram, from the four facts we usually have
    at_least_one = N - neither
    both = nA + nB - at_least_one          # the addition law, solved for the overlap
    only_A, only_B = nA - both, nB - both
    rows = [(f"{A} only", only_A), ("both", both), (f"{B} only", only_B), ("neither", neither)]
    print(f"at least one = {N} − {neither} = {at_least_one}")
    print(f"both = {nA} + {nB} − {at_least_one} = {both}\n")
    print(f"{'region':<20} {'count':>6} {'share':>7}")
    for name, n in rows:
        print(f"{name:<20} {n:>6} {n/N:>7.2f}")
    print(f"{'total':<20} {sum(n for _, n in rows):>6} {sum(n for _, n in rows)/N:>7.2f}")
    assert sum(n for _, n in rows) == N
    return both

both = venn_count(200, 120, 90, 40)
P_union = 120/200 + 90/200 - both/200
print(f"\nP(A or S) = .60 + .45 − {both/200:.2f} = {P_union:.2f};  complement = {1 - P_union:.2f}")
""")

code(r"""
n, k = 8, 3
teams = math.comb(n, k)                   # order does not matter
roles = math.perm(n, k)                   # stand lead, demo rider, sales
print(pd.DataFrame({
    "question": ["teams of 3 (combinations)", "3 named roles (permutations)", "ratio"],
    "formula": ["8! / (3!·5!) = 8·7·6 / 6", "8! / 5! = 8·7·6", "3! = 6"],
    "result": [teams, roles, roles // teams]}).to_string(index=False))
assert roles == teams * math.factorial(k)
print(f"\nEach team of {k} can be arranged in {k}! = {math.factorial(k)} ways: {teams} × {math.factorial(k)} = {roles}.")
""")

code(r"""
ks = list(range(0, 9))
fig = go.Figure(go.Bar(x=ks, y=[math.comb(8, j) for j in ks], marker_color=[RED if j == 3 else GREY for j in ks],
                       text=[math.comb(8, j) for j in ks], textposition="outside"))
fig.update_layout(template="simple_white", height=420, title="How many groups of k can you pick from 8 people?",
                  xaxis_title="k, size of the group", yaxis_title="C(8, k)", yaxis_range=[0, 80])
fig.show()
print("Symmetric: choosing the 3 who go is the same as choosing the 5 who stay. C(8,3) = C(8,5) =", math.comb(8, 5))
""")

md(r"""
### 🔍 CHECK
The four regions must add back to **200**, and the shares to **1.00**. On paper, if they do not, stop before you compute any probability. For counting, ask the one question first: *does order matter?*
""")

# ---------------- B ----------------
md(r"""
## B. Which supplier sent the faulty battery? — the two-way table and Bayes

Last month: **1,000** batteries. **Volta** sent **700** at a **2%** defect rate; **Ampere** sent **300** at **5%**. A faulty battery is on the bench, label gone.

$$P(A \mid B) = \frac{\text{number in both } A \text{ and } B}{\text{number in } B}$$

*Business reading:* "given B" means look only at B's row (or column) and divide by **its** total. Same cell on top, different total underneath, different question.

Then the independence check: supplier and fault are **independent** if every row shows the same share of faulty as the total. Under independence the cells would be *row total × column share*.
""")
code(r"""
def two_way(suppliers, counts, rates, bad="faulty", good="good"):
    # Build the table of counts from the three facts: who sent how many, at what defect rate
    faulty = [round(c * r) for c, r in zip(counts, rates)]
    tab = pd.DataFrame({good: [c - f for c, f in zip(counts, faulty)], bad: faulty}, index=suppliers)
    tab["total"] = tab[good] + tab[bad]
    tab.loc["total"] = tab.sum()
    return tab

for s, c, r in zip(["Volta", "Ampere"], [700, 300], [.02, .05]):
    print(f"{s}: {c} × {r:.0%} = {round(c*r)} faulty, {c} − {round(c*r)} = {c - round(c*r)} good")
tab = two_way(["Volta", "Ampere"], [700, 300], [.02, .05])
print("\n", tab.to_string(), sep="")

print("\nThe ROW — given the supplier, how often faulty?")
for s in ["Volta", "Ampere"]:
    print(f"  P(faulty | {s:<6}) = {tab.loc[s, 'faulty']:>2} / {tab.loc[s, 'total']:>4} = {tab.loc[s, 'faulty']/tab.loc[s, 'total']:.3f}")
print("  (the defect rates we started from: the table is built right)")
print("\nThe COLUMN — given faulty, which supplier?")
for s in ["Volta", "Ampere"]:
    print(f"  P({s:<6} | faulty) = {tab.loc[s, 'faulty']:>2} / {tab.loc['total', 'faulty']:>4} = {tab.loc[s, 'faulty']/tab.loc['total', 'faulty']:.2f}")
print(f"\nOverall P(faulty) = 29 / 1,000 = {tab.loc['total', 'faulty']/tab.loc['total', 'total']:.3f}")
""")

code(r"""
p_faulty = tab.loc["total", "faulty"] / tab.loc["total", "total"]
expected = pd.DataFrame({
    "good":   [tab.loc[s, "total"] * (1 - p_faulty) for s in ["Volta", "Ampere"]],
    "faulty": [tab.loc[s, "total"] * p_faulty for s in ["Volta", "Ampere"]]}, index=["Volta", "Ampere"])
print("Observed share faulty by row:", {s: round(tab.loc[s, "faulty"] / tab.loc[s, "total"], 3) for s in ["Volta", "Ampere"]},
      f" overall {p_faulty:.3f}")
print("\nIf supplier told us nothing about the fault, the table would read:")
print(expected.round(1).to_string())
print("\nObserved faulty: Volta 14 vs 20.3 expected, Ampere 15 vs 8.7 expected.")
print("The rows differ from the total: supplier and fault are DEPENDENT. Say the comparison, then the word.")
""")

md(r"""
### Bayes: the faulty column, with shares instead of counts
The founder's prior: "probably Volta, they send 70%". One faulty battery is the evidence.

$$P(\text{Ampere} \mid F) = \frac{P(F \mid \text{Ampere})\,P(\text{Ampere})}{P(F)}$$

Then **drag the slider:** Ampere's defect rate, from 1% to 10%. Volta stays at 2% with 70% of deliveries. When does Ampere become the clear suspect?
""")
code(r"""
def bayes_table(suppliers, prior, rate):
    joint = [p * r for p, r in zip(prior, rate)]           # share of ALL batteries that are faulty from each
    total = sum(joint)
    t = pd.DataFrame({"prior share": prior, "× defect rate": rate, "= faulty, share of all": joint,
                      "÷ total faulty": [j / total for j in joint]}, index=suppliers)
    t.loc["total"] = [sum(prior), np.nan, total, 1.0]
    return t

bt = bayes_table(["Volta", "Ampere"], [.70, .30], [.02, .05])
print(bt.round(3).to_string())
print(f"\nP(Ampere | F) = .05 × .30 / (.02 × .70 + .05 × .30) = .015 / .029 = {bt.loc['Ampere', '÷ total faulty']:.2f}")
print("Before the evidence Ampere was .30; after, .52. A 30% supplier at twice the defect rate is only a coin-flip suspect.")
""")

code(r"""
rates = np.round(np.arange(0.01, 0.1001, 0.005), 3)
def posterior(rA, rV=.02, pV=.70):
    jV, jA = pV * rV, (1 - pV) * rA
    return jV / (jV + jA), jA / (jV + jA)

fig = go.Figure()
for r in rates:
    pV, pA = posterior(r)
    fig.add_bar(x=["Volta", "Ampere"], y=[pV, pA], marker_color=[GREY, RED], visible=bool(abs(r - .05) < 1e-9),
                text=[f"{pV:.2f}", f"{pA:.2f}"], textposition="outside", name=f"{r:.1%}")
fig.add_hline(y=.30, line=dict(color=GOLD, dash="dot"), annotation_text="Ampere's prior share .30")
steps = [dict(method="update", label=f"{r:.1%}",
              args=[{"visible": [j == i for j in range(len(rates))]},
                    {"title": f"Ampere defect rate {r:.1%} → P(Ampere | faulty) = {posterior(r)[1]:.2f}"}])
         for i, r in enumerate(rates)]
fig.update_layout(template="simple_white", height=460, showlegend=False, yaxis_range=[0, 1],
                  title="Ampere defect rate 5.0% → P(Ampere | faulty) = 0.52", yaxis_title="P(supplier | faulty)",
                  sliders=[dict(active=int(np.argmin(abs(rates - .05))), steps=steps,
                                currentvalue=dict(prefix="Ampere's defect rate: "))])
fig.show()
print(f"{'Ampere rate':>12} {'P(Ampere | faulty)':>20}")
for r in (.01, .02, .05, .08, .10):
    print(f"{r:>12.0%} {posterior(r)[1]:>20.2f}")
""")

md(r"""
### 🔍 CHECK
At 2% both rows read the same and the posterior equals the prior (.30): the supplier tells you nothing. The row check — $14/700 = .02$ — must return the defect rate you were given. If it does not, the table is wrong, not the question.
""")

# ---------------- C ----------------
md(r"""
## C. How many returns next week? — mean and variance, binomial, Poisson

Five weeks of warranty returns: **4, 7, 3, 6, 5**.

$$\bar{x} = \frac{\sum x}{n} \qquad s^{2} = \frac{\sum (x - \bar{x})^{2}}{n-1}$$

*Business reading:* the mean is the total, shared equally. The variance is the average squared distance from it — divided by $n-1$ because the deviations always sum to zero, so only $n-1$ of them are free.

Then the **random variable**: next week's returns, with a share attached to each value — twenty weeks of history turned into shares. Same two formulas, with the shares as weights instead of $1/n$: $E(x) = \sum x\,P(x)$ and $\sigma^{2} = \sum (x - \mu)^{2}\,P(x)$.
""")
code(r"""
def spread_table(x, label="returns"):
    x = np.array(x, dtype=float); n = len(x); xbar = x.sum() / n
    t = pd.DataFrame({"week": range(1, n + 1), label: x, "x − x̄": x - xbar, "(x − x̄)²": (x - xbar) ** 2})
    t.loc["sum"] = ["", x.sum(), (x - xbar).sum(), ((x - xbar) ** 2).sum()]
    print(t.to_string(index=False))
    ss = ((x - xbar) ** 2).sum()
    print(f"\nmean   x̄  = {x.sum():.0f} / {n} = {xbar:g}")
    print(f"variance s² = {ss:.0f} / ({n} − 1) = {ss:.0f} / {n-1} = {ss/(n-1):g}")
    print(f"st. dev. s  = √{ss/(n-1):g} = {math.sqrt(ss/(n-1)):.2f}")
    return xbar, ss / (n - 1)

xbar, s2 = spread_table([4, 7, 3, 6, 5])
print(f"\nReading: a typical week is {xbar:g} returns, give or take about {math.sqrt(s2):.1f}. The deviations sum to zero: a check, not a result.")
""")

code(r"""
def rv_table(values, shares):
    v, P = np.array(values, dtype=float), np.array(shares, dtype=float)
    assert abs(P.sum() - 1) < 1e-9, "shares must add to 1"
    mu = (v * P).sum()
    t = pd.DataFrame({"x": v, "P(x)": P, "x·P(x)": v * P, "x − μ": v - mu, "(x − μ)²": (v - mu) ** 2,
                      "(x − μ)²·P(x)": (v - mu) ** 2 * P})
    t.loc["sum"] = ["", P.sum(), mu, "", "", ((v - mu) ** 2 * P).sum()]
    print(t.to_string(index=False))
    var = ((v - mu) ** 2 * P).sum()
    print(f"\nE(x) = {' + '.join(f'{a:g}({b:.2f})' for a, b in zip(v, P))} = {mu:.1f}")
    print(f"σ² = {var:.2f},  σ = √{var:.2f} = {math.sqrt(var):.2f}")
    return mu, var

mu_rv, var_rv = rv_table([3, 4, 5, 6, 7], [.15, .20, .30, .20, .15])
print(f"\nReading: expect {mu_rv:.0f} returns a week, give or take about {math.sqrt(var_rv):.1f}. No single week has exactly 5.0; over 50 weeks, about 250.")
""")

md(r"""
### Binomial: twelve test rides, how many buy?
Saturday: **12** test rides, one rider in four buys ($p = .25$), each decides alone. A fixed number of yes/no trials, same $p$, independent.

$$P(x) = \binom{n}{x}\, p^{x}\, (1-p)^{n-x}$$

Below the four steps, **two sliders, one at a time:** the number of test rides $n$ (with $p = .25$) and the share who buy $p$ (with $n = 12$). Push $n$ to 40 and watch the bars become a bell; drop $p$ to .05 and see where the peak goes.
""")
code(r"""
def binomial_steps(n, x, p):
    ways = math.comb(n, x); yes = p ** x; no = (1 - p) ** (n - x)
    print(f"1. the ways to pick which {x} of the {n} buy:   C({n},{x}) = {ways}")
    print(f"2. those {x} buy:                              {p}^{x} = {yes:.6f}")
    print(f"3. the other {n-x} do not:                      {1-p}^{n-x} = {no:.4f}")
    print(f"4. multiply:                                 {ways} × {yes:.6f} × {no:.4f} = {ways*yes*no:.3f}")
    return ways * yes * no

n, p = 12, .25
P3 = binomial_steps(n, 3, p)
print(f"\nscipy agrees: binom.pmf(3, 12, .25) = {stats.binom.pmf(3, n, p):.3f}")
print(f"\nmean          np = {n} × {p} = {n*p:g} buyers")
print(f"st. dev.  √np(1−p) = √({n} × {p} × {1-p}) = √{n*p*(1-p):g} = {math.sqrt(n*p*(1-p)):g}")
P0 = (1 - p) ** n
print(f"nobody buys   P(0) = {1-p}^{n} = {P0:.3f}")
print(f"at least one  1 − P(0) = {1 - P0:.3f}")
print("\nReading: one Saturday in four ends with exactly three buyers; nobody buying is a one-in-thirty Saturday.")
""")

code(r"""
ns = list(range(4, 41, 2)); ps = np.round(np.arange(0.05, 0.96, 0.05), 2)

def pmf_bars(n, p, visible):
    xs = np.arange(0, n + 1); ys = stats.binom.pmf(xs, n, p)
    return [go.Bar(x=xs, y=ys, marker_color=RED, visible=visible, name=f"n={n}, p={p}", showlegend=False),
            go.Scatter(x=[n * p, n * p], y=[0, ys.max() * 1.08], mode="lines", visible=visible, showlegend=False,
                       line=dict(color=GOLD, width=3, dash="dash"), name=f"mean {n*p:.1f}")]

fig = go.Figure()
for n_ in ns:
    fig.add_traces(pmf_bars(n_, .25, n_ == 12))
for p_ in ps:
    fig.add_traces(pmf_bars(12, p_, False))
T = 2 * (len(ns) + len(ps))
def vis(idx):                       # show the pair of traces number idx, hide all others
    v = [False] * T; v[2*idx] = v[2*idx + 1] = True; return v
steps_n = [dict(method="update", label=str(n_), args=[{"visible": vis(i)},
           {"title": f"n = {n_} test rides, p = .25 → mean np = {n_*.25:.1f}, σ = {math.sqrt(n_*.25*.75):.2f}"}]) for i, n_ in enumerate(ns)]
steps_p = [dict(method="update", label=f"{p_:.2f}", args=[{"visible": vis(len(ns) + i)},
           {"title": f"n = 12 test rides, p = {p_:.2f} → mean np = {12*p_:.1f}, σ = {math.sqrt(12*p_*(1-p_)):.2f}"}]) for i, p_ in enumerate(ps)]
fig.update_layout(template="simple_white", height=520, title="n = 12 test rides, p = .25 → mean np = 3.0, σ = 1.50",
                  xaxis_title="number of buyers", yaxis_title="probability", xaxis_range=[-0.5, 40.5],
                  sliders=[dict(active=ns.index(12), steps=steps_n, currentvalue=dict(prefix="n (p = .25): "), y=-0.05),
                           dict(active=int(np.argmin(abs(ps - .25))), steps=steps_p, currentvalue=dict(prefix="p (n = 12): "), y=-0.35)],
                  margin=dict(b=200))
fig.show()
""")

md(r"""
### Poisson: the helpline, three calls an hour
Calls arrive at random, **3 an hour**. The one person answering steps out for **half an hour**. A count in an interval, constant rate, no ceiling. Write $\mu$ = rate × interval **before** any number.

$$P(x) = \frac{\mu^{x} e^{-\mu}}{x!}$$
""")
code(r"""
def poisson_steps(rate, hours):
    mu = rate * hours
    print(f"μ = {rate} an hour × {hours:g} hour(s) = {mu:g}")
    P0 = math.exp(-mu)
    print(f"  P(0)  = {mu:g}^0 e^−{mu:g} / 0! = e^−{mu:g} = {P0:.3f}")
    print(f"  P(≥1) = 1 − {P0:.3f} = {1 - P0:.3f}")
    print(f"  P(2)  = {mu:g}² e^−{mu:g} / 2! = {mu**2:g} × {P0:.4f} / 2 = {stats.poisson.pmf(2, mu):.3f}")
    return mu, P0

print("A full hour:"); mu_h, P0_h = poisson_steps(3, 1)
print("\nThe half hour she is away — rescale first:"); mu_half, P0_half = poisson_steps(3, 0.5)
print(f"\nWithout the rescaling you would say {P0_h:.0%} for the half hour. It is {P0_half:.0%}: four times out. μ first, always.")
print(f"Reading: leaving the helpline for half an hour, we miss at least one call {1 - P0_half:.0%} of the time — three times out of four.")
""")

code(r"""
mus = np.round(np.arange(0.5, 10.01, 0.5), 1)
xs = np.arange(0, 21)
fig = go.Figure()
for m in mus:
    fig.add_bar(x=xs, y=stats.poisson.pmf(xs, m), marker_color=RED, visible=bool(m == 3.0), name=f"μ={m}", showlegend=False)
steps = [dict(method="update", label=f"{m:g}", args=[{"visible": [j == i for j in range(len(mus))]},
         {"title": f"μ = {m:g} expected calls → P(0) = {math.exp(-m):.3f}, P(≥1) = {1 - math.exp(-m):.3f}"}]) for i, m in enumerate(mus)]
fig.update_layout(template="simple_white", height=460, title="μ = 3 expected calls → P(0) = 0.050, P(≥1) = 0.950",
                  xaxis_title="calls in the interval", yaxis_title="probability",
                  sliders=[dict(active=int(np.where(mus == 3.0)[0][0]), steps=steps, currentvalue=dict(prefix="μ = rate × interval: "))])
fig.show()
print("Mean and variance of a Poisson are both μ: a high rate gives a wide, bell-shaped pile. Push μ to 10 and look.")
""")

md(r"""
### 🔍 CHECK
Deviations sum to zero; shares sum to one; $P(0) + P(\geq 1) = 1$. Before any formula, say which model in words: *how many of these $n$?* is binomial; *how many in this interval?* is Poisson, and $\mu$ comes first.
""")

# ---------------- D ----------------
md(r"""
## D. What range do we promise? — the normal

Engineering measured 200 bikes on the same loop: **90 km on average, standard deviation 8 km**, bell-shaped. $X \sim N(90, 8)$. Marketing wants to print **75 km**.

$$z = \frac{x - \mu}{\sigma}$$

Four steps, every time: **sketch and shade → standardise → table → sentence.** The table gives the area to the **left** of $z$.

Below the steps, **three sliders, one at a time** from the baseline $N(90, 8)$, threshold 75: the mean $\mu$, the spread $\sigma$, and the threshold printed on the box. The shaded tail is the share of riders who see less than promised. Then the empirical rule — one σ, two σ, three σ: the same three numbers for every bell, which is why we measure distance in σ and not in km.
""")
code(r"""
def normal_steps(x, mu, sigma, tail="below"):
    z = (x - mu) / sigma
    z2 = round(z, 2)                                       # the table has two decimals
    left = round(stats.norm.cdf(z2), 4)                    # what the printed table shows
    print(f"1. sketch: the bell centred at {mu}, shade the area {tail} {x}")
    print(f"2. standardise: z = ({x} − {mu}) / {sigma} = {x - mu} / {sigma} = {z:.3f} ≈ {z2:.2f}")
    print(f"3. table, area to the left of {z2:.2f}: {left:.4f}   (Excel: =NORM.S.DIST({z2:.2f}, TRUE))")
    area = left if tail == "below" else 1 - left
    if tail == "above":
        print(f"   the whole area is 1, so P(X > {x}) = 1 − {left:.4f} = {area:.3f}")
    print(f"4. P(X {'<' if tail == 'below' else '>'} {x}) = {area:.3f}")
    return z, area

print("Print 75 km: what share of riders see less?"); z75, below75 = normal_steps(75, 90, 8)
print(f"   Sentence: print 75 km and about {round(below75*100):.0f} riders in a hundred will see less than the box promised.\n")
print("And the share above 75 km:"); _, above75 = normal_steps(75, 90, 8, tail="above")

print("\nBackwards — the Board accepts 5% below the box. What do we print?")
z05 = -1.645                                                # .05 sits between z = −1.64 (.0505) and −1.65 (.0495)
x05 = 90 + z05 * 8
print(f"   table, backwards: area .05 → z = {z05}   (Excel: =NORM.S.INV(0.05) = {stats.norm.ppf(.05):.3f})")
print(f"   undo the standardisation: x = μ + zσ = 90 + ({z05}) × 8 = 90 − {abs(z05)*8:.2f} = {x05:.2f} km")
print(f"   Print 76 km, a promise rounds down: the share below it is P(z < {(76-90)/8:.2f}) = {stats.norm.cdf(76, 90, 8):.3f}.")
print("   Sentence: print 76 km; about one rider in twenty-five will see less, and every km added to the box adds one or two complaints in a hundred.")
""")

code(r"""
mus_ = list(range(80, 101, 2)); sigmas_ = list(range(4, 17, 2)); thr_ = list(range(70, 91, 1))
grid = np.linspace(50, 130, 400)

def bell(mu, sigma, thr, visible):
    pdf = stats.norm.pdf(grid, mu, sigma); tail = grid <= thr
    return [go.Scatter(x=grid, y=pdf, mode="lines", line=dict(color="#363636", width=3), visible=visible, showlegend=False),
            go.Scatter(x=grid[tail], y=pdf[tail], fill="tozeroy", mode="lines", line=dict(color=RED, width=0),
                       fillcolor="rgba(175,31,37,.45)", visible=visible, showlegend=False)]
settings = [(m, 8, 75) for m in mus_] + [(90, s, 75) for s in sigmas_] + [(90, 8, t) for t in thr_]
fig = go.Figure()
for (m, s, t) in settings:
    fig.add_traces(bell(m, s, t, (m, s, t) == (90, 8, 75)))
T = 2 * len(settings)
def vis(idx):
    v = [False] * T; v[2*idx] = v[2*idx + 1] = True; return v
def title(m, s, t):
    return f"N({m}, {s}), box says {t} km → z = {(t-m)/s:.2f}, share below = {stats.norm.cdf(t, m, s):.3f}"
mk = lambda i, lab: dict(method="update", label=lab, args=[{"visible": vis(i)}, {"title": title(*settings[i])}])
off = 0; steps_mu = [mk(off + i, str(m)) for i, m in enumerate(mus_)]
off += len(mus_); steps_sg = [mk(off + i, str(s)) for i, s in enumerate(sigmas_)]
off += len(sigmas_); steps_th = [mk(off + i, str(t)) for i, t in enumerate(thr_)]
fig.update_layout(template="simple_white", height=600, title=title(90, 8, 75), xaxis_title="range, km", yaxis_title="density",
                  yaxis_range=[0, 0.105], margin=dict(b=260),
                  sliders=[dict(active=mus_.index(90), steps=steps_mu, currentvalue=dict(prefix="μ (σ = 8, box 75): "), y=-0.04),
                           dict(active=sigmas_.index(8), steps=steps_sg, currentvalue=dict(prefix="σ (μ = 90, box 75): "), y=-0.30),
                           dict(active=thr_.index(75), steps=steps_th, currentvalue=dict(prefix="box says, km (μ = 90, σ = 8): "), y=-0.56)])
fig.show()
print(f"{'print':>6} {'share who see less':>20}")
for t in (85, 80, 76.8, 75):
    print(f"{t:>6} {stats.norm.cdf(t, 90, 8):>20.0%}")
""")

code(r"""
mu, sigma = 90, 8
print(f"{'within':>8} {'km range':>12} {'share, exact':>13} {'rule of thumb':>14}")
for k, rule in zip((1, 2, 3), ("68%", "95%", "99.7%")):
    share = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"{k:>7}σ {f'{mu - k*sigma} to {mu + k*sigma}':>12} {share:>13.3f} {rule:>14}")
print(f"\nA bike at 74 km is two σ below the mean: {stats.norm.cdf(-2):.3f}, about one in forty.")
""")

md(r"""
### Skewness: when the bell is the wrong picture
Battery range is symmetric: mean and median coincide. Delivery time is not — most parcels take two days, a few take ten. A long right tail pulls the mean above the median. Before you use the table, ask whether the data are a bell.
""")
code(r"""
rng = np.random.default_rng(7)
ranges = rng.normal(90, 8, 5000)                                  # symmetric: battery range
delivery = rng.lognormal(mean=np.log(2.4), sigma=0.716, size=5000) # right-skewed: delivery days, median 2.4

fig = go.Figure()
fig.add_histogram(x=ranges, nbinsx=60, name="battery range, km", marker_color=GREY, opacity=.8)
fig.add_histogram(x=delivery * 10 + 50, nbinsx=60, name="delivery time (days, rescaled to share the axis)", marker_color=RED, opacity=.7)
fig.update_layout(template="simple_white", height=420, barmode="overlay", title="A bell and a long right tail",
                  xaxis_title="", yaxis_title="count of 5,000", legend=dict(x=.55, y=.95))
fig.show()

for name, x, unit in (("battery range", ranges, "km"), ("delivery time", delivery, "days")):
    skew = stats.skew(x)
    print(f"{name:<14} mean {np.mean(x):6.2f} {unit:<4} median {np.median(x):6.2f} {unit:<4} skewness {skew:+.2f}"
          f"  → {'mean ≈ median: symmetric, the table applies' if abs(skew) < .2 else 'mean > median: positive skew, the table does not apply'}")
""")

md(r"""
### 🔍 CHECK
The table only gives "to the left". Everything else is $1 -$ or a difference of two lookups; the sketch tells you which. Forwards: $x \to z \to$ area. Backwards: area $\to z \to x$, and the answer ends in km, not in $z$.
""")

# ---------------------------------------------------------------------------
# Drills, solved in code — every published number asserted against drills.md
# ---------------------------------------------------------------------------
md(r"""
## Drills, solved in code

This section is an optional companion: the code is not examined, but reading it is recommended. Every drill in `drills.md` is solved here in Python. Do the drill on paper first, then run the cell and compare your numbers with the output.
""")
code(r"""
# `close` checks our result against the number printed in drills.md
def close(value, expected, tol=1e-3):
    assert abs(value - expected) <= tol, f"got {value}, drills.md says {expected}"

def table_left(z):
    # what the printed standard normal table shows: z to two decimals, area to the left to four
    return round(stats.norm.cdf(round(z, 2)), 4)

print("helpers ready")
""")

# ---- D1 -------------------------------------------------------------------
md(r"""
**D1.** The founder sends 2 of the 6 mechanics to a training course. (a) How many different pairs? (b) With a **lead** and an **assistant**, how many assignments? (c) Why is (b) exactly twice (a)?
""")
code(r"""
n, k = 6, 2
pairs = math.comb(n, k)                       # (a) a pair is a pair: order does not matter
assignments = math.perm(n, k)                 # (b) named roles: order matters
print(f"(a) C(6,2) = 6! / (2!·4!) = 6·5 / 2 = {6*5} / 2 = {pairs} pairs")
print(f"(b) P(6,2) = 6! / 4! = 6·5 = {assignments} assignments: 6 choices for the lead, 5 left for the assistant")
print(f"(c) each pair takes the two roles in 2! = {math.factorial(k)} ways: {pairs} × {math.factorial(k)} = {pairs * math.factorial(k)}")
close(pairs, 15); close(assignments, 30); close(assignments / pairs, 2)
print("\nFifteen different pairs can go; thirty different lead–assistant assignments. The 2! underneath in (a) removes exactly those orderings.")
""")

# ---- D2 -------------------------------------------------------------------
md(r"""
**D2.** Motors from two suppliers: **Rotor** sends 60%, 3% faulty; **Spin** sends 40%, 6% faulty. Last month, 500 motors. (a) The two-way table. (b) $P(\text{faulty} \mid \text{Rotor})$ and $P(\text{Rotor} \mid \text{faulty})$. (c) Independent? (d) Bayes for $P(\text{Spin} \mid \text{faulty})$.
""")
code(r"""
N = 500
counts = [round(.60 * N), round(.40 * N)]                                  # 300 Rotor, 200 Spin
print("(a) " + "; ".join(f"{s}: {c} motors, {round(c*r)} faulty, {c - round(c*r)} good" for s, c, r in zip(["Rotor", "Spin"], counts, [.03, .06])))
d2 = two_way(["Rotor", "Spin"], counts, [.03, .06])
print(d2.to_string())
assert d2.loc["Rotor"].tolist() == [291, 9, 300] and d2.loc["Spin"].tolist() == [188, 12, 200] and d2.loc["total"].tolist() == [479, 21, 500]

p_f_rotor = d2.loc["Rotor", "faulty"] / d2.loc["Rotor", "total"]           # the row
p_rotor_f = d2.loc["Rotor", "faulty"] / d2.loc["total", "faulty"]           # the column
print(f"\n(b) P(faulty | Rotor) = 9 / 300 = {p_f_rotor:.3f}   — Rotor's row: how good is Rotor")
print(f"    P(Rotor | faulty) = 9 / 21  = {p_rotor_f:.3f}   — the faulty column: who sent this faulty one")
close(p_f_rotor, .03); close(p_rotor_f, .429)

p_f_spin = d2.loc["Spin", "faulty"] / d2.loc["Spin", "total"]; p_f = d2.loc["total", "faulty"] / N
print(f"\n(c) rows: Rotor {p_f_rotor:.3f}, Spin {p_f_spin:.3f}; total {p_f:.3f} → the rows differ: DEPENDENT")
close(p_f_spin, .06); close(p_f, .042)

bt2 = bayes_table(["Rotor", "Spin"], [.60, .40], [.03, .06])
print("\n(d)"); print(bt2.round(3).to_string())
p_spin_f = .06 * .40 / (.03 * .60 + .06 * .40)
print(f"    P(Spin | faulty) = .06 × .40 / (.03 × .60 + .06 × .40) = .024 / .042 = {p_spin_f:.3f};  via counts 12/21 = {12/21:.3f}")
close(.60 * .03, .018, 1e-9); close(.40 * .06, .024, 1e-9); close(p_spin_f, .571); close(12 / 21, .571)
print("\nSpin sends 40% of the motors but is behind 57% of the faulty ones: the likelier culprit, not a certain one.")
""")

# ---- D3 -------------------------------------------------------------------
md(r"""
**D3.** (a) Warranty claims in the last six weeks: 2, 5, 3, 6, 4, 4 — mean, sample variance and standard deviation by hand, in a table. (b) Saturday brings 10 test rides; three riders in ten buy, each deciding alone: name the model, find $P(2)$, $P(0)$, $P(\geq 1)$, the mean and the standard deviation. (c) Web-shop orders arrive at random, 4 an hour: name the model, find $P(0)$ and $P(2)$ in an hour; then, for a 15-minute coffee break, $\mu$ first, $P(0)$ and $P(\geq 1)$.
""")
code(r"""
xbar3, s2_3 = spread_table([2, 5, 3, 6, 4, 4], label="claims")
close(xbar3, 4); close(s2_3, 2.0); close(math.sqrt(s2_3), 1.41, 5e-3)   # drills.md rounds to two decimals
print(f"\nAbout {xbar3:g} claims a week, give or take {math.sqrt(s2_3):.1f}.")
""")

code(r"""
# D3 (b)
n, p = 10, .3
print("Binomial: a fixed number of trials (10), each yes or no, the same p = .3 every time, each rider alone.\n")
P2 = binomial_steps(n, 2, p)
P0 = (1 - p) ** n
print(f"\nP(0) = .7^10 = {P0:.3f}     P(≥1) = 1 − {P0:.3f} = {1 - P0:.3f}")
print(f"np = 10 × .3 = {n*p:g} buyers     σ = √(10 × .3 × .7) = √{n*p*(1-p):.1f} = {math.sqrt(n*p*(1-p)):.2f}")
close(math.comb(10, 2), 45); close(.7 ** 8, .05765, 1e-4); close(P2, .233)
close(P0, .028); close(1 - P0, .972); close(n * p, 3); close(math.sqrt(n * p * (1 - p)), 1.45)
print("\nExpect three buyers, give or take one and a half; a Saturday with no sale happens about three times in a hundred.")
""")

code(r"""
# D3 (c)
print("Poisson: orders arrive at random over time, at a constant rate, with no ceiling on the count.\n")
print("One hour:"); mu4, P0_4 = poisson_steps(4, 1)
print("\nA 15-minute break — a quarter of an hour, so μ first:"); mu1, P0_1 = poisson_steps(4, 0.25)
close(P0_4, .018); close(stats.poisson.pmf(2, 4), .147); close(math.exp(-4), .01832, 1e-4)
close(mu1, 1); close(P0_1, .368); close(1 - P0_1, .632)
print("\nA silent hour is rare, two in a hundred; a silent coffee break happens more than once in three.")
""")

# ---- D4 -------------------------------------------------------------------
md(r"""
**D4.** A full charge takes 240 minutes on average, standard deviation 20, bell-shaped: $X \sim N(240, 20)$. (a) Share over 270 minutes. (b) Share between 220 and 260, and the rule of thumb that gives it. (c) The slowest 10% are flagged: from how many minutes? (d) Delivery times: mean 3.1 days, median 2.4 — what shape, and why is the table the wrong tool?
""")
code(r"""
mu, sigma = 240, 20
print("(a) shade the right tail beyond 270"); z_a, above270 = normal_steps(270, mu, sigma, tail="above")
close(z_a, 1.5, 1e-9); close(table_left(z_a), .9332, 1e-4); close(above270, .067)
print("    About 7 charges in 100 take more than four and a half hours.\n")

print("(b) shade between 220 and 260: two lookups, area to the left of each, and a difference")
z_lo, z_hi = (220 - mu) / sigma, (260 - mu) / sigma
between = table_left(z_hi) - table_left(z_lo)
print(f"    z = {z_lo:+.0f} and z = {z_hi:+.0f}:  P(−1 < z < 1) = {table_left(z_hi):.4f} − {table_left(z_lo):.4f} = {between:.3f}")
close(table_left(z_hi), .8413, 1e-4); close(table_left(z_lo), .1587, 1e-4); close(between, .683)
print("    One σ either side of the mean: the 68% rule, no table needed.\n")

print("(c) backwards: the slowest 10% is the right tail, so 90% of the area is to the left of the threshold")
print(f"    find .9000 inside the table: z = 1.28 gives {table_left(1.28):.4f}, z = 1.29 gives {table_left(1.29):.4f} → nearer 1.28   (Excel: =NORM.S.INV(0.90) = {stats.norm.ppf(.9):.3f})")
z_c = 1.28
x_c = mu + z_c * sigma
print(f"    undo the standardisation: x = μ + zσ = 240 + 1.28 × 20 = 240 + {z_c*sigma:.1f} = {x_c:.1f} minutes")
close(table_left(1.28), .8997, 1e-4); close(table_left(1.29), .9015, 1e-4); close(stats.norm.ppf(.9), 1.28, 5e-3); close(x_c, 265.6)
print("    A charge over about 266 minutes is flagged.\n")

print("(d) delivery times: mean 3.1 days, median 2.4 days")
mean_d, median_d = 3.1, 2.4
assert mean_d > median_d
print(f"    mean − median = {mean_d - median_d:+.1f} days: a long right tail, POSITIVE skewness — most parcels in two or three days, a few much later.")
print("    The normal is symmetric (mean = median), so a z from a mean of 3.1 would give the wrong areas: the table only answers questions about bells.")
""")

md(r"""
## Homework 7 and what comes next

`homework.md` — due **Sunday 15 November, 23:59 on Moodle**: five exercises on paper and a 150–250-word memo to the Board on the range to print. We go through it together at the start of next Monday's session.

Next Monday, online: *how sure are we of that number?* 200 bikes gave 90 km; the true average is not 90. Week 8 says how far off it can be.
""")

code(r"""
# Every number in drills.md, re-checked here. Change a number in a drill and this cell tells you what else moves.
checks = [
    ("D1 pairs C(6,2)", math.comb(6, 2), 15), ("D1 assignments P(6,2)", math.perm(6, 2), 30),
    ("D2 Rotor faulty", round(.03 * 300), 9), ("D2 Spin faulty", round(.06 * 200), 12), ("D2 total faulty", 9 + 12, 21),
    ("D2 P(faulty | Rotor)", 9 / 300, .03), ("D2 P(Rotor | faulty)", 9 / 21, .429), ("D2 P(faulty | Spin)", 12 / 200, .06),
    ("D2 P(faulty)", 21 / 500, .042), ("D2 Bayes P(Spin | faulty)", .06 * .40 / (.03 * .60 + .06 * .40), .571),
    ("D3 mean", np.mean([2, 5, 3, 6, 4, 4]), 4), ("D3 s²", np.var([2, 5, 3, 6, 4, 4], ddof=1), 2.0), ("D3 s", np.std([2, 5, 3, 6, 4, 4], ddof=1), 1.41),
    ("D3 binomial P(2)", stats.binom.pmf(2, 10, .3), .233), ("D3 binomial P(0)", stats.binom.pmf(0, 10, .3), .028),
    ("D3 binomial P(≥1)", 1 - stats.binom.pmf(0, 10, .3), .972), ("D3 binomial mean", 10 * .3, 3), ("D3 binomial σ", math.sqrt(10 * .3 * .7), 1.45),
    ("D3 Poisson μ=4 P(0)", stats.poisson.pmf(0, 4), .018), ("D3 Poisson μ=4 P(2)", stats.poisson.pmf(2, 4), .147),
    ("D3 Poisson μ=1 P(0)", stats.poisson.pmf(0, 1), .368), ("D3 Poisson μ=1 P(≥1)", 1 - stats.poisson.pmf(0, 1), .632),
    ("D4 P(X > 270)", 1 - stats.norm.cdf(270, 240, 20), .067), ("D4 P(220 < X < 260)", stats.norm.cdf(260, 240, 20) - stats.norm.cdf(220, 240, 20), .683),
    ("D4 flag threshold, minutes", 240 + 1.28 * 20, 265.6),
]
for name, got, want in checks:
    close(got, want, 5e-3 if want < 20 else 0.05)   # three decimals for shares, two for the rest
    print(f"  ok  {name:<32} {got:9.4f}   drills.md: {want}")
print(f"\n{len(checks)} numbers in drills.md, re-checked here: all agree.")
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).with_name("session.ipynb"))
print("wrote session.ipynb with", len(cells), "cells")
