"""Build week-06/session.ipynb with nbformat. Run: python3.11 week-06/build_notebook.py
then: python3.11 -m nbconvert --to notebook --execute --inplace week-06/session.ipynb"""
from pathlib import Path
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-06_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 6 — The founder does not know the numbers
**European School of Economics · Thu 5 Nov 2026 · online · Tutor: Vincenzo Nardelli**

In weeks 1–5 every number at **Arno Bikes** was given: a fixed cost, a list price, a coupon. This quarter the founder asks three questions she cannot answer with a given number — how many customers do both, which supplier sent the faulty battery, how many returns next week. Each answer comes with a spread.

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
import plotly.graph_objects as go

RED, GOLD, GREY = "#AF1F25", "#CDBA80", "#7a7f85"
print("ready")
""")

# ---------------- A ----------------
md(r"""
## A. How many of our customers do both? — sets and counting

The CRM says: of **200** customers, **120** bought accessories, **90** a service plan, **40** neither. The founder wants to upsell the ones who bought **both**.

$$n(A \cup S) = n(A) + n(S) - n(A \cap S)$$

*Business reading:* "or" adds the two counts, then takes the overlap out once — otherwise the "both" customers are counted twice. Divide every count by 200 and the same identity is the **addition law**.

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
print("Eighty per cent of our customers buy at least one extra; a quarter buy both.")
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
print("The faulty battery is slightly more likely from Ampere, 52 to 48. Audit Ampere's line, but do not switch supplier on one battery.")
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
## C. How many returns next week? — mean and variance, the language of distributions

Five weeks of warranty returns: **4, 7, 3, 6, 5**.

$$\bar{x} = \frac{\sum x}{n} \qquad s^{2} = \frac{\sum (x - \bar{x})^{2}}{n-1}$$

*Business reading:* the mean is the total, shared equally. The variance is the average squared distance from it — divided by $n-1$ because the deviations always sum to zero, so only $n-1$ of them are free.

Then the **random variable**: next week's returns, with a share attached to each value — twenty weeks of history turned into shares. Same two formulas, with the shares as weights instead of $1/n$: $E(x) = \sum x\,P(x)$ and $\sigma^{2} = \sum (x - \mu)^{2}\,P(x)$. The table of shares, drawn, **is** the distribution.
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

code(r"""
vals, P = [3, 4, 5, 6, 7], [.15, .20, .30, .20, .15]
sd = math.sqrt(var_rv)
fig = go.Figure(go.Bar(x=vals, y=P, marker_color=RED, text=[f"{p:.2f}" for p in P], textposition="outside",
                       name="share of weeks", showlegend=False))
fig.add_vline(x=mu_rv, line=dict(color=GOLD, width=3, dash="dash"), annotation_text=f"E(x) = {mu_rv:.0f}", annotation_position="top")
fig.add_shape(type="line", x0=mu_rv - sd, x1=mu_rv + sd, y0=.33, y1=.33, line=dict(color=GREY, width=2))
fig.add_annotation(x=mu_rv, y=.345, text=f"± σ = {sd:.2f}", showarrow=False, font=dict(color=GREY))
fig.update_layout(template="simple_white", height=420, title="Next week's returns: the table of shares, drawn — that picture IS the distribution",
                  xaxis_title="returns next week, x", yaxis_title="share P(x)", yaxis_range=[0, .4], xaxis=dict(tickmode="array", tickvals=vals))
fig.show()
print("Where it sits: E(x) = 5. How wide: σ = 1.26. Seven is the top of the table, a normal bad week; eight has not happened in twenty weeks.")
print("Plan the workshop for five returns a week, give or take one or two.")
""")

md(r"""
### 🔍 CHECK
Deviations sum to zero; shares sum to one. Two formulas, used twice: once with $1/n$ as the weight (the five weeks), once with the shares (the random variable). If your $E(x)$ is outside the range of the values, the weights are wrong.
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

print("helpers ready")
""")

# ---- D1 -------------------------------------------------------------------
md(r"""
**D1.** Last Saturday **150** people visited the showroom: **95** took a test ride ($T$), **70** asked about financing ($F$), **25** did neither. (a) How many did both? The four regions. (b) $P(T \cup F)$ with the addition law and $P(T \cap F)$. (c) 2 of 7 sales staff for the Saturday shift: how many pairs? If one opens and the other closes, how many assignments?
""")
code(r"""
print("(a)"); both1 = venn_count(150, 95, 70, 25, A="test ride", B="financing")
close(both1, 40); close(95 - both1, 55); close(70 - both1, 30)

pT, pF, pTF = 95 / 150, 70 / 150, both1 / 150
print(f"\n(b) P(T or F) = {pT:.3f} + {pF:.3f} − {pTF:.3f} = {pT + pF - pTF:.3f};  as a count, 125 / 150 = {125/150:.3f}")
print(f"    P(T and F) = 40 / 150 = {pTF:.3f}")
close(pT, .633); close(pF, .467); close(pTF, .267); close(pT + pF - pTF, .833)
print("    Five visitors in six did at least one of the two; about one in four did both.")

pairs, assignments = math.comb(7, 2), math.perm(7, 2)
print(f"\n(c) C(7,2) = 7·6 / 2 = {pairs} pairs;  P(7,2) = 7·6 = {assignments} assignments")
print(f"    each pair takes the two roles in 2! = {math.factorial(2)} ways: {pairs} × 2 = {pairs * 2}. The 2! underneath in the combinations removes exactly those orderings.")
close(pairs, 21); close(assignments, 42); close(assignments / pairs, 2)
""")

# ---- D2 -------------------------------------------------------------------
md(r"""
**D2.** Chargers from two suppliers: **Ohm** sends 60%, 4% faulty; **Watt** sends 40%, 1% faulty. Last month, 500 chargers. (a) The two-way table. (b) $P(\text{faulty} \mid \text{Ohm})$ and $P(\text{Ohm} \mid \text{faulty})$. (c) Independent? (d) Bayes for $P(\text{Ohm} \mid \text{faulty})$; compare with this morning's battery case.
""")
code(r"""
N = 500
counts = [round(.60 * N), round(.40 * N)]                                  # 300 Ohm, 200 Watt
print("(a) " + "; ".join(f"{s}: {c} chargers, {round(c*r)} faulty, {c - round(c*r)} good" for s, c, r in zip(["Ohm", "Watt"], counts, [.04, .01])))
d2 = two_way(["Ohm", "Watt"], counts, [.04, .01])
print(d2.to_string())
assert d2.loc["Ohm"].tolist() == [288, 12, 300] and d2.loc["Watt"].tolist() == [198, 2, 200] and d2.loc["total"].tolist() == [486, 14, 500]

p_f_ohm = d2.loc["Ohm", "faulty"] / d2.loc["Ohm", "total"]                 # the row
p_ohm_f = d2.loc["Ohm", "faulty"] / d2.loc["total", "faulty"]              # the column
print(f"\n(b) P(faulty | Ohm) = 12 / 300 = {p_f_ohm:.3f}   — Ohm's row: how good is Ohm")
print(f"    P(Ohm | faulty) = 12 / 14  = {p_ohm_f:.3f}   — the faulty column: who sent this faulty one")
close(p_f_ohm, .04); close(p_ohm_f, .857)

p_f_watt = d2.loc["Watt", "faulty"] / d2.loc["Watt", "total"]; p_f = d2.loc["total", "faulty"] / N
print(f"\n(c) rows: Ohm {p_f_ohm:.3f}, Watt {p_f_watt:.3f}; total {p_f:.3f} → the rows differ: DEPENDENT")
close(p_f_watt, .01); close(p_f, .028)

bt2 = bayes_table(["Ohm", "Watt"], [.60, .40], [.04, .01])
print("\n(d)"); print(bt2.round(3).to_string())
p_ohm_bayes = .04 * .60 / (.04 * .60 + .01 * .40)
print(f"    P(Ohm | faulty) = .04 × .60 / (.04 × .60 + .01 × .40) = .024 / .028 = {p_ohm_bayes:.3f};  via counts 12/14 = {12/14:.3f}")
close(.60 * .04, .024, 1e-9); close(.40 * .01, .004, 1e-9); close(.04 * .60 + .01 * .40, .028, 1e-9)
close(p_ohm_bayes, .857); close(.004 / .028, .143)
print("\nOhm sends 60% of the chargers and is behind 86% of the faulty ones. This morning the big supplier had the LOWER rate and the")
print("evidence pulled towards the small one; here the big supplier also has the higher rate, so both effects push the same way.")
""")

# ---- D3 -------------------------------------------------------------------
md(r"""
**D3.** (a) Warranty returns in the last five weeks: 3, 8, 5, 6, 8 — mean, sample variance and standard deviation by hand, in a table. (b) Orders for the cargo model per day, $x = 0..4$ with shares .10, .20, .40, .20, .10: check the shares, then $E(x)$, $\sigma^{2}$, $\sigma$ in a table, and one sentence with a "give or take".
""")
code(r"""
# D3 (a)
xbar3, s2_3 = spread_table([3, 8, 5, 6, 8])
close(xbar3, 6); close(s2_3, 4.5); close(math.sqrt(s2_3), 2.12, 5e-3)   # drills.md rounds to two decimals
close(sum((np.array([3, 8, 5, 6, 8]) - 6) ** 2), 18)
print(f"\nAbout {xbar3:g} returns a week, give or take {math.sqrt(s2_3):.0f}.")
""")

code(r"""
# D3 (b)
v3, p3 = [0, 1, 2, 3, 4], [.10, .20, .40, .20, .10]
print(f"shares add to {sum(p3):.2f}\n")
mu3, var3 = rv_table(v3, p3)
close(mu3, 2.0); close(var3, 1.20); close(math.sqrt(var3), 1.10, 5e-3)
assert np.allclose(np.array(v3) * p3, [0, .20, .80, .60, .40]) and np.allclose((np.array(v3) - 2) ** 2 * p3, [.40, .20, 0, .20, .40])
print("\nExpect two cargo orders a day, give or take one; a day with none happens one day in ten, a day with four as well.")
""")

md(r"""
## Homework 6 and what comes next

`homework.md` — due **Sunday 8 November, 23:59 on Moodle**: three short exercises on paper and a 100–150-word memo to the founder on the faulty battery. Short on purpose: we meet again on Monday. We go through it together at the start of Monday's session.

Next **Monday 9 November, in person in Florence**: three shapes — binomial, Poisson, the normal — and how to decide with them. Three ready-made tables of shares; same five words, same $E(x)$ and $\sigma$.
""")

code(r"""
# Every number in drills.md, re-checked here. Change a number in a drill and this cell tells you what else moves.
checks = [
    ("D1 both", 95 + 70 - (150 - 25), 40), ("D1 test ride only", 95 - 40, 55), ("D1 financing only", 70 - 40, 30),
    ("D1 P(T)", 95 / 150, .633), ("D1 P(F)", 70 / 150, .467), ("D1 P(T and F)", 40 / 150, .267), ("D1 P(T or F)", 125 / 150, .833),
    ("D1 pairs C(7,2)", math.comb(7, 2), 21), ("D1 assignments P(7,2)", math.perm(7, 2), 42),
    ("D2 Ohm faulty", round(.04 * 300), 12), ("D2 Watt faulty", round(.01 * 200), 2), ("D2 total faulty", 12 + 2, 14),
    ("D2 P(faulty | Ohm)", 12 / 300, .04), ("D2 P(Ohm | faulty)", 12 / 14, .857), ("D2 P(faulty | Watt)", 2 / 200, .01),
    ("D2 P(faulty)", 14 / 500, .028), ("D2 Bayes P(Ohm | faulty)", .04 * .60 / (.04 * .60 + .01 * .40), .857),
    ("D2 Bayes P(Watt | faulty)", .004 / .028, .143),
    ("D3 mean", np.mean([3, 8, 5, 6, 8]), 6), ("D3 sum of squares", np.sum((np.array([3, 8, 5, 6, 8]) - 6) ** 2), 18),
    ("D3 s²", np.var([3, 8, 5, 6, 8], ddof=1), 4.5), ("D3 s", np.std([3, 8, 5, 6, 8], ddof=1), 2.12),
    ("D3 E(x)", np.dot([0, 1, 2, 3, 4], [.10, .20, .40, .20, .10]), 2.0),
    ("D3 σ²", np.dot((np.array([0, 1, 2, 3, 4]) - 2) ** 2, [.10, .20, .40, .20, .10]), 1.20), ("D3 σ", math.sqrt(1.20), 1.10),
]
for name, got, want in checks:
    close(got, want, 5e-3 if want < 20 else 0.05)   # three decimals for shares, two for the rest
    print(f"  ok  {name:<28} {got:9.4f}   drills.md: {want}")
print(f"\n{len(checks)} numbers in drills.md, re-checked here: all agree.")
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).with_name("session.ipynb"))
print("wrote session.ipynb with", len(cells), "cells")
