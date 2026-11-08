"""Build week-07/session.ipynb with nbformat. Run: python3.11 week-07/build_notebook.py
then: python3.11 -m nbconvert --to notebook --execute --inplace week-07/session.ipynb"""
from pathlib import Path
import nbformat as nbf

nb = nbf.v4.new_notebook()
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nb.metadata["colab"] = {"name": "week-07_session.ipynb"}
cells = []
md = lambda s: cells.append(nbf.v4.new_markdown_cell(s.strip()))
code = lambda s: cells.append(nbf.v4.new_code_cell(s.strip()))

md(r"""
# MBA03 · Week 7 — Three shapes, and how to decide with them
**European School of Economics · Mon 9 Nov 2026 · online · Tutor: Vincenzo Nardelli**

Today each unknown number at **Arno Bikes** first gets a mean and a spread (block A, the part of Thursday we did not reach), then a **shape** — and a shape is something you can read a probability off. Three shapes cover almost every number a firm does not know: a count out of $n$ (binomial), a count at a rate (Poisson), a measurement (the normal). The founder's four questions: how many returns next week; how many of Saturday's riders buy; what range to print on the box; which battery supplier to sign.

This notebook is driven by the tutor. Every picture is followed by the same computation **by hand on paper**: formula, substitution, number, one sentence for the Board. The code is optional and not examined.
""")

code(r"""
# Setup (Colab has plotly, numpy, pandas and scipy preinstalled; this is a no-op there)
import subprocess, sys
try:
    import plotly
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "plotly"])
import math
import numpy as np, pandas as pd
from scipy import stats
import plotly.graph_objects as go

RED, GOLD, GREY, INK = "#AF1F25", "#CDBA80", "#7a7f85", "#363636"
print("ready")
""")

# ---------------- A ----------------
md(r"""
## A. How many returns next week? — mean and variance, the language of distributions

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

# ---------------- B ----------------
md(r"""
## B. How many of Saturday's riders buy? — binomial, Poisson, one family

Saturday: **12** test rides. From the CRM, one rider in four buys ($p = .25$), and each decides alone. A fixed number of yes/no trials, the same $p$ each time, independent: the **binomial**.

$$P(x) = \binom{n}{x}\, p^{x}\, (1-p)^{n-x} \qquad E(x) = np \qquad \sigma = \sqrt{np(1-p)}$$

*Business reading:* $\binom{n}{x}$ counts the ways to pick **which** $x$ of the $n$ riders buy; $p^{x}$ says those $x$ all buy; $(1-p)^{n-x}$ says the others all do not. Four steps, every binomial question. "At least one" is always $1 -$ "none".

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
print(f"nobody buys   P(0) = C(12,0) × .25^0 × .75^12 = {1-p}^{n} = {P0:.3f}")
print(f"at least one  1 − P(0) = 1 − {P0:.3f} = {1 - P0:.3f}")
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
print("Small n: count the ways. Large n: the bars smooth into a bell — block D uses that. Tiny p with many trials: a Poisson.")
""")

md(r"""
### Poisson: the helpline, three calls an hour
Calls arrive at random, **3 an hour**. The one person answering steps out for **half an hour**. A count in an interval, constant rate, no ceiling: the **Poisson**. Write $\mu$ = rate × interval **before** any number.

$$P(x) = \frac{\mu^{x} e^{-\mu}}{x!}$$

Then **drag the slider** on $\mu$: mean and variance of a Poisson are both $\mu$, so a high rate gives a wide, bell-shaped pile.
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

print("The half hour she is away — rescale first:"); mu_half, P0_half = poisson_steps(3, 0.5)
print("\nA full hour:"); mu_h, P0_h = poisson_steps(3, 1)
print(f"\nWithout the rescaling you would say {P0_h:.0%} for the half hour. It is {P0_half:.0%}: four times out. μ first, always.")
print(f"Reading: leaving the helpline for half an hour, we miss at least one call {1 - P0_half:.0%} of the time — three times out of four.")
""")

code(r"""
mus = np.round(np.arange(0.5, 10.01, 0.5), 1)
xs = np.arange(0, 21)
fig = go.Figure()
for m in mus:
    fig.add_bar(x=xs, y=stats.poisson.pmf(xs, m), marker_color=RED, visible=bool(m == 1.5), name=f"μ={m}", showlegend=False)
steps = [dict(method="update", label=f"{m:g}", args=[{"visible": [j == i for j in range(len(mus))]},
         {"title": f"μ = {m:g} expected calls → P(0) = {math.exp(-m):.3f}, P(≥1) = {1 - math.exp(-m):.3f}"}]) for i, m in enumerate(mus)]
fig.update_layout(template="simple_white", height=460, title="μ = 1.5 expected calls → P(0) = 0.223, P(≥1) = 0.777",
                  xaxis_title="calls in the interval", yaxis_title="probability",
                  sliders=[dict(active=int(np.where(mus == 1.5)[0][0]), steps=steps, currentvalue=dict(prefix="μ = rate × interval: "))])
fig.show()
print("Half an hour is μ = 1.5, a full hour μ = 3. Push μ to 10 and look: with a high rate the Poisson is a bell too.")
""")

md(r"""
### 🔍 CHECK
Say which model **in words** before any formula: *how many of these $n$?* is binomial, you are given $n$ and $p$; *how many in this interval?* is Poisson, you are given a rate and $\mu$ comes first. $P(0) + P(\geq 1) = 1$. If your $P(x)$ is above 1 or your mean is outside $0..n$, a step is wrong.
""")

# ---------------- C ----------------
md(r"""
## C. What range do we promise? — the normal, skewness and kurtosis

Engineering measured 200 bikes on the same loop: **90 km on average, standard deviation 8 km**, bell-shaped. $X \sim N(90, 8)$. Marketing wants to print **75 km**.

$$z = \frac{x - \mu}{\sigma}$$

Four steps, every time: **sketch and shade → standardise → table → sentence.** The table gives the area to the **left** of $z$; one table serves every bell, because step 2 turns every bell into the same one. Backwards, for a guarantee: area $\to z \to x = \mu + z\sigma$, and the answer ends in km.

Below the steps, **three sliders, one at a time** from the baseline $N(90, 8)$, threshold 75: the mean $\mu$, the spread $\sigma$, and the threshold printed on the box. The shaded tail is the share of riders who see less than promised.
""")
code(r"""
def table_left(z):
    # what the printed standard normal table shows: z to two decimals, area to the left to four
    return round(stats.norm.cdf(round(z, 2)), 4)

def normal_steps(x, mu, sigma, tail="below"):
    z = (x - mu) / sigma
    z2 = round(z, 2)                                       # the table has two decimals
    left = table_left(z)
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
print(f"   undo the standardisation: x = μ + zσ = 90 + ({z05}) × 8 = 90 − {abs(z05)*8:.1f} = {x05:.1f} km")
print(f"   Print 76 km, a promise rounds down: the share below it is P(z < {(76-90)/8:.2f}) = {table_left((76-90)/8):.3f}.")
print("   Sentence: print 76 km; about one rider in twenty-five will see less, and every km added to the box adds one or two complaints in a hundred.")
""")

code(r"""
mus_ = list(range(80, 101, 2)); sigmas_ = list(range(4, 17, 2)); thr_ = list(range(70, 91, 1))
grid = np.linspace(50, 130, 400)

def bell(mu, sigma, thr, visible):
    pdf = stats.norm.pdf(grid, mu, sigma); tail = grid <= thr
    return [go.Scatter(x=grid, y=pdf, mode="lines", line=dict(color=INK, width=3), visible=visible, showlegend=False),
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
print(f"{'print':>8} {'share who see less':>20}")
for t in (85, 80, 76.8, 75):
    print(f"{t:>8} {stats.norm.cdf(t, 90, 8):>20.0%}")
print("\nDouble σ to 16 and the 75-km tail grows from 3% to 17%: the spread, not the mean, is what a guarantee pays for.")
""")

code(r"""
mu, sigma = 90, 8
print("The empirical rule — the same three numbers for every bell, which is why we measure distance in σ and not in km\n")
print(f"{'within':>8} {'km range':>12} {'share, exact':>13} {'rule of thumb':>14}")
for k, rule in zip((1, 2, 3), ("68%", "95%", "99.7%")):
    share = stats.norm.cdf(k) - stats.norm.cdf(-k)
    print(f"{k:>7}σ {f'{mu - k*sigma} to {mu + k*sigma}':>12} {share:>13.3f} {rule:>14}")
print(f"\nA bike at 74 km is two σ below the mean: P(z < −2) = {stats.norm.cdf(-2):.3f}, about one in forty.")
print(f"Beyond three σ either side, under the bell: {2*stats.norm.cdf(-3):.4f}, about one in three hundred — remember this number for kurtosis.")
""")

md(r"""
### Skewness and kurtosis: when the bell is the wrong picture
Battery range is symmetric: mean and median coincide, **skewness zero**. Delivery time is not — most parcels take two days, a few take ten: a long right tail pulls the mean above the median, **positive skewness**. And **kurtosis** asks how much of the curve sits in the tails: with the *same* mean and σ, a fat-tailed shape has a "three σ" day far more often than one in three hundred.

Below, three simulated samples of 5,000 with the same mean and σ: a bell, a right-skewed lognormal, a fat-tailed $t$. Before you use the table, ask whether the data are a bell.
""")
code(r"""
rng = np.random.default_rng(16)
N_ = 5000
def rescale(x, mu=90, sd=8):                       # same mean and σ for all three, so only the shape differs
    return mu + (x - x.mean()) / x.std() * sd
bell_s   = rescale(rng.normal(size=N_))                 # symmetric: battery range
skewed_s = rescale(rng.lognormal(0, .7, size=N_))       # right-skewed: delivery time, rescaled
fat_s    = rescale(rng.standard_t(3, size=N_))          # fat tails: delivery delays, rescaled

fig = go.Figure()
for name, x, col in (("bell (battery range)", bell_s, GREY), ("right-skewed (lognormal)", skewed_s, RED), ("fat-tailed (t, 3 d.f.)", fat_s, GOLD)):
    fig.add_histogram(x=x, xbins=dict(start=50, end=130, size=1), name=name, marker_color=col, opacity=.6)
fig.update_layout(template="simple_white", height=440, barmode="overlay", title="Three shapes, the same mean 90 and the same σ 8",
                  xaxis_title="value", yaxis_title="count of 5,000", xaxis_range=[50, 130], legend=dict(x=.62, y=.95))
fig.show()

print(f"{'sample':<26} {'mean':>6} {'median':>7} {'skewness':>9} {'kurtosis':>9} {'beyond 3σ':>10}   in plain words")
for name, x in (("bell", bell_s), ("right-skewed lognormal", skewed_s), ("fat-tailed t", fat_s)):
    sk, ku = stats.skew(x), stats.kurtosis(x)         # scipy's kurtosis is excess kurtosis: 0 for the bell
    far = np.mean(np.abs(x - 90) > 24)
    words = ("mean ≈ median, tails like the bell: the table applies" if abs(sk) < .2 and abs(ku) < .5 else
             "mean > median: leans right, a z from the mean gives the wrong areas" if sk > .5 else
             "symmetric but fat tails: the rare bad day is not as rare as the bell says")
    print(f"{name:<26} {x.mean():>6.1f} {np.median(x):>7.1f} {sk:>+9.2f} {ku:>+9.2f} {far:>10.4f}   {words}")
print("\nSkewness: zero for a bell, positive when the long tail is on the right. Kurtosis (excess): zero for a bell, positive for fat tails.")
print("Under the bell, 'beyond three σ' is about .003; the fat-tailed sample has several times that with the same σ.")
""")

md(r"""
### 🔍 CHECK
The table only gives "to the left". Everything else is $1 -$ or a difference of two lookups; the sketch tells you which. Forwards: $x \to z \to$ area. Backwards: area $\to z \to x$, and the answer ends in km, not in $z$. And before any of it: mean above median says the data lean; fat tails say the bell under-counts the surprises.
""")

# ---------------- D ----------------
md(r"""
## D. Which supplier do we sign? — expected value to decide

Arno Bikes buys **1,000 batteries a month**. **Volta**: €180 a battery, faulty ones replaced by Volta — a **certain** number. **Ampere**: €165 a battery, but **5%** arrive faulty and a faulty battery costs us **€90** to swap on the line — a **random variable**, Thursday's table with two rows.

$$E(x) = \sum x\,P(x) \qquad \sigma^{2} = \sum (x - \mu)^{2}\,P(x)$$

*Business reading:* a cheaper price with a catch is not a price; it is a distribution, and you compare distributions by their mean — and then by their spread. The decision tree: a **square** where we choose, a **circle** where chance chooses; the number at a node is the expected value of everything to its right.
""")
code(r"""
def rv_table(values, shares, unit="€"):
    v, P = np.array(values, dtype=float), np.array(shares, dtype=float)
    assert abs(P.sum() - 1) < 1e-9, "shares must add to 1"
    mu = (v * P).sum()
    t = pd.DataFrame({"x": v, "P(x)": P, "x·P(x)": v * P, "x − μ": v - mu, "(x − μ)²": (v - mu) ** 2,
                      "(x − μ)²·P(x)": (v - mu) ** 2 * P})
    t.loc["sum"] = ["", P.sum(), mu, "", "", ((v - mu) ** 2 * P).sum()]
    print(t.to_string(index=False))
    var = ((v - mu) ** 2 * P).sum()
    print(f"\nE(x) = {' + '.join(f'{b:.2f} × {a:g}' for a, b in zip(v, P))} = {' + '.join(f'{a*b:.2f}' for a, b in zip(v, P))} = {unit}{mu:.2f}")
    print(f"σ² = {var:.2f},  σ = √{var:.2f} = {unit}{math.sqrt(var):.1f}")
    return mu, var

print("Ampere, cost per battery — the chance node:\n")
E_amp, V_amp = rv_table([165, 165 + 90], [.95, .05])
sd_amp = math.sqrt(V_amp)
print(f"\nOn average Ampere costs €{E_amp:.2f} a battery: the €165 price plus €{.05*90:.2f} for the faulty ones.")
print(f"Against Volta's €180: €{180 - E_amp:.2f} cheaper a battery, €{1000*(180 - E_amp):,.0f} a month.\n")

tree = pd.DataFrame({"Volta": ["€180.00", "€0", "€180"], "Ampere": [f"€{E_amp:.2f}", f"€{sd_amp:.1f}", "€255"]},
                    index=["expected cost", "spread σ", "worst battery"])
print(tree.to_string())
print("\nExpected value picks Ampere. Spread picks Volta. A decision has two numbers, and the Board must hear both.")
""")

code(r"""
# When does the spread matter? Volume.
n_m, p_f = 1000, .05
mu_f, sd_f = n_m * p_f, math.sqrt(n_m * p_f * (1 - p_f))
print(f"A thousand batteries a month — the faulty count is binomial, n = {n_m}, p = {p_f}:")
print(f"  np = {mu_f:.0f} faulty,  σ = √({n_m} × {p_f} × {1-p_f}) = {sd_f:.1f}")
bill, bill_sd = 165 * n_m + 90 * mu_f, 90 * sd_f
print(f"  monthly bill = €165 × {n_m:,} + €90 × {mu_f:.0f} = €{bill:,.0f}, give or take €{bill_sd:,.0f}. The €{1000*(180-E_amp):,.0f} saving is never at risk.\n")

n_r = 10
saving_r = n_r * (180 - 165)
P0_r, P1_r = stats.binom.pmf(0, n_r, p_f), stats.binom.pmf(1, n_r, p_f)
P2plus = 1 - P0_r - P1_r
print(f"A rush order of ten — same p, n = {n_r}: the saving on ten batteries is €{saving_r}; two faulty cost €{2*90} and wipe it out.")
print(f"  P(X ≥ 2) = 1 − P(0) − P(1) = 1 − {P0_r:.3f} − {P1_r:.3f} = {P2plus:.3f}   — one rush order in {round(1/P2plus)}.")
print("\nBoard sentence: sign Ampere for the volume contract, €10.50 a battery cheaper on average and the faults average out to about fifty,")
print("give or take seven. Keep Volta for rush orders of a few units, where one faulty battery in a box of ten is a problem the saving cannot pay for.")
print("Expected value decides when the decision repeats. Spread decides when it does not.")
""")

code(r"""
# Drag Ampere's defect rate: when does the expected value flip back to Volta?
rates = np.round(np.arange(0.00, 0.3001, 0.01), 2)
def ev_amp(r, price=165, swap=90):
    return price + r * swap
flip = (180 - 165) / 90                      # the rate at which 165 + r × 90 = 180
fig = go.Figure()
for r in rates:
    e = ev_amp(r); sd = math.sqrt((1 - r) * (165 - e) ** 2 + r * (255 - e) ** 2)
    fig.add_bar(x=["Volta", "Ampere"], y=[180, e], marker_color=[GREY, RED if e < 180 else INK], visible=bool(abs(r - .05) < 1e-9),
                text=["€180.00", f"€{e:.2f} ± {sd:.1f}"], textposition="outside", showlegend=False, name=f"{r:.0%}")
fig.add_hline(y=180, line=dict(color=GOLD, dash="dot"), annotation_text="Volta, certain €180")
steps = [dict(method="update", label=f"{r:.0%}",
              args=[{"visible": [j == i for j in range(len(rates))]},
                    {"title": f"Ampere defect rate {r:.0%} → expected cost €{ev_amp(r):.2f} a battery  ({'Ampere cheaper' if ev_amp(r) < 180 else 'Volta cheaper' if ev_amp(r) > 180 else 'a tie'})"}])
         for i, r in enumerate(rates)]
fig.update_layout(template="simple_white", height=460, yaxis_range=[150, 215], yaxis_title="expected cost per battery, €",
                  title="Ampere defect rate 5% → expected cost €169.50 a battery  (Ampere cheaper)",
                  sliders=[dict(active=int(np.argmin(abs(rates - .05))), steps=steps, currentvalue=dict(prefix="Ampere's defect rate: "))])
fig.show()
print(f"{'defect rate':>12} {'E(Ampere)':>10} {'vs Volta':>10}")
for r in (.00, .05, .10, flip, .20):
    print(f"{r:>12.1%} {ev_amp(r):>10.2f} {ev_amp(r) - 180:>+10.2f}")
print(f"\nThe expected value flips at a defect rate of 15/90 = {flip:.1%}: above that, the €15 discount no longer pays for the swaps.")
""")

md(r"""
### 🔍 CHECK
Shares at the chance node add to 1; the worst end node is the price plus the full cost of the catch. The expected value is the price you pay on average; the spread is the surprise you pay sometimes. A repeated decision follows the mean; a one-off weighs the spread. If your $E(x)$ is below the best end node or above the worst, the weights are wrong.
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
**D1.** (a) Warranty returns in the last five weeks: 3, 8, 5, 6, 8 — mean, sample variance and standard deviation by hand, in a table. (b) Orders for the cargo model per day, $x = 0..4$ with shares .10, .20, .40, .20, .10: check the shares, then $E(x)$, $\sigma^{2}$, $\sigma$ in a table, and one sentence with a "give or take".
""")
code(r"""
# D1 (a)
xbar3, s2_3 = spread_table([3, 8, 5, 6, 8])
close(xbar3, 6); close(s2_3, 4.5); close(math.sqrt(s2_3), 2.12, 5e-3)   # drills.md rounds to two decimals
close(sum((np.array([3, 8, 5, 6, 8]) - 6) ** 2), 18)
print(f"\nAbout {xbar3:g} returns a week, give or take {math.sqrt(s2_3):.0f}.")
""")

code(r"""
# D1 (b)
v3, p3 = [0, 1, 2, 3, 4], [.10, .20, .40, .20, .10]
print(f"shares add to {sum(p3):.2f}\n")
mu3, var3 = rv_table(v3, p3, unit="")
close(mu3, 2.0); close(var3, 1.20); close(math.sqrt(var3), 1.10, 5e-3)
assert np.allclose(np.array(v3) * p3, [0, .20, .80, .60, .40]) and np.allclose((np.array(v3) - 2) ** 2 * p3, [.40, .20, 0, .20, .40])
print("\nExpect two cargo orders a day, give or take one; a day with none happens one day in ten, a day with four as well.")
""")

# ---- D2 -------------------------------------------------------------------
md(r"""
**D2.** (a) Saturday brings 10 test rides; three riders in ten buy, each deciding alone. Name the model; find $P(2)$, $P(0)$, $P(\geq 1)$, the mean and the standard deviation. (b) Web-shop orders arrive at random, 4 an hour: name the model, find $P(0)$ in an hour; then, for a 15-minute coffee break, $\mu$ first, $P(0)$ and $P(\geq 1)$.
""")
code(r"""
# D2 (a)
n, p = 10, .3
print("(a) Binomial: a fixed number of trials (10), each yes or no, the same p = .3 every time, each rider alone.\n")
P2 = binomial_steps(n, 2, p)
P0 = (1 - p) ** n
print(f"\nP(0) = .7^10 = {P0:.3f}     P(≥1) = 1 − {P0:.3f} = {1 - P0:.3f}")
print(f"np = 10 × .3 = {n*p:g} buyers     σ = √(10 × .3 × .7) = √{n*p*(1-p):.1f} = {math.sqrt(n*p*(1-p)):.2f}")
close(math.comb(10, 2), 45); close(.3 ** 2, .09, 1e-9); close(.7 ** 8, .05765, 1e-4); close(45 * .09 * .05765, .233); close(P2, .233)
close(P0, .028); close(1 - P0, .972); close(n * p, 3); close(n * p * (1 - p), 2.1, 1e-9); close(math.sqrt(n * p * (1 - p)), 1.45)
print("Expect three buyers, give or take one and a half; a Saturday with no sale happens about three times in a hundred.\n")

# D2 (b)
print("(b) Poisson: orders arrive at random over time, at a constant rate, with no ceiling on the count.\n")
print("One hour:"); mu4, P0_4 = poisson_steps(4, 1)
print("\nA 15-minute break — a quarter of an hour, so μ first:"); mu1, P0_1 = poisson_steps(4, 0.25)
close(math.exp(-4), .01832, 1e-4); close(P0_4, .018)
close(mu1, 1, 1e-9); close(P0_1, .368); close(1 - P0_1, .632)
print("\nA silent hour is rare, two in a hundred; a silent coffee break happens more than once in three.")
""")

# ---- D3 -------------------------------------------------------------------
md(r"""
**D3.** Bike weight off the line: $X \sim N(22,\,1.5)$ kg. (a) Share under 20 kg. (b) The heaviest 5% are sent back for a check: from what weight? End in kg. (c) Delivery times: mean 3.1 days, median 2.4 — what shape, and why is the table the wrong tool?
""")
code(r"""
mu, sigma = 22, 1.5
print("(a) shade the left tail below 20 kg"); z_a, below20 = normal_steps(20, mu, sigma)
close(z_a, -1.333); close(table_left(z_a), .0918, 1e-4); close(below20, .092)
print("    About nine bikes in a hundred come in under 20 kg; the customer will wait, or pay for the light frame.\n")

print("(b) backwards: the heaviest 5% is the right tail, so 95% of the area is to the left of the threshold")
print(f"    find .9500 inside the table: z = 1.64 gives {table_left(1.64):.4f}, z = 1.65 gives {table_left(1.65):.4f} → z = 1.645   (Excel: =NORM.S.INV(0.95) = {stats.norm.ppf(.95):.3f})")
z_c = 1.645; x_c = mu + z_c * sigma
print(f"    undo the standardisation: x = μ + zσ = 22 + 1.645 × 1.5 = 22 + {z_c*sigma:.2f} = {x_c:.1f} kg")
close(table_left(1.64), .9495, 1e-4); close(table_left(1.65), .9505, 1e-4); close(stats.norm.ppf(.95), 1.645); close(z_c * sigma, 2.47, 5e-3); close(x_c, 24.5, .05)
print("    A bike over about 24.5 kg goes back for a check.\n")

print("(c) delivery times: mean 3.1 days, median 2.4 days")
mean_d, median_d = 3.1, 2.4
assert mean_d > median_d
print(f"    mean − median = {mean_d - median_d:+.1f} days: a long right tail, POSITIVE skewness — most parcels in two or three days, a few much later.")
print("    The normal is symmetric (mean = median), so a z from a mean of 3.1 would give the wrong areas: the table only answers questions about bells.")
""")

# ---- D4 -------------------------------------------------------------------
md(r"""
**D4.** €2,000 for one promotion in December; each extra bike earns the €600 margin (list €1,000, variable cost €400). **Test-ride Saturday**, cost €2,000: extra sales 6 / 10 / 14 bikes with probability .3 / .5 / .2. **Online ads**, cost €1,000: extra sales 4 / 6 bikes with probability .5 / .5. (a) The tree with the **profit** at each end node. (b) Expected profit of each. (c) Standard deviation of the ads (the Saturday's, €1,680, is given). (d) Two sentences for the Board.
""")
code(r"""
margin = 1000 - 400; close(margin, 600)
sat_x = [b * margin - 2000 for b in (6, 10, 14)]; sat_p = [.3, .5, .2]
ads_x = [b * margin - 1000 for b in (4, 6)];      ads_p = [.5, .5]
print("(a) end-node profits, margin €600 a bike minus the cost of the option")
print("    Saturday (cost €2,000): " + "; ".join(f"{b} × 600 − 2,000 = {x:,}" for b, x in zip((6, 10, 14), sat_x)))
print("    Ads (cost €1,000):      " + "; ".join(f"{b} × 600 − 1,000 = {x:,}" for b, x in zip((4, 6), ads_x)))
assert sat_x == [1600, 4000, 6400] and ads_x == [1400, 2600]
print("    The tree: a square 'which promotion?', two branches; on each a circle with branches .3 / .5 / .2 and .5 / .5, the profits at the ends.\n")

print("(b) Test-ride Saturday (its σ, €1,680, is given in the drill):"); E_sat, V_sat = rv_table(sat_x, sat_p)
print("\n(b), (c) Online ads:"); E_ads, V_ads = rv_table(ads_x, ads_p)
print(f"\n    σ(Saturday) / σ(ads) = {math.sqrt(V_sat):,.0f} / {math.sqrt(V_ads):,.0f} = {math.sqrt(V_sat)/math.sqrt(V_ads):.1f}: the Saturday is the riskier option, by far.")
assert np.allclose(np.array(sat_x) * sat_p, [480, 2000, 1280]) and np.allclose(np.array(ads_x) * ads_p, [700, 1300])
assert np.allclose(np.array(sat_x) - E_sat, [-2160, 240, 2640]) and np.allclose((np.array(sat_x) - E_sat) ** 2 * sat_p, [1399680, 28800, 1393920])
close(E_sat, 3760, 1e-6); close(E_ads, 2000, 1e-6); close(E_sat - E_ads, 1760, 1e-6)
close(V_sat, 2822400, 1e-6); close(math.sqrt(V_sat), 1680, 1e-6); close(V_ads, 360000, 1e-6); close(math.sqrt(V_ads), 600, 1e-6)
close(1680 / 600, 2.8, 1e-9); assert min(sat_x) == 1600 < E_ads

print(f"\n(d) The test-ride Saturday earns €{E_sat:,.0f} on average against €{E_ads:,.0f} for the ads, €{E_sat - E_ads:,.0f} more; its worst case, €{min(sat_x):,},")
print(f"    still beats the ads' average. Its spread is nearly three times larger (€{math.sqrt(V_sat):,.0f} against €{math.sqrt(V_ads):,.0f}): the Saturday can end anywhere")
print("    between €1,600 and €6,400, the ads between €1,400 and €2,600. Expected value picks the Saturday; the spread says the result will be a")
print("    surprise either way — and since even the bad Saturday beats the ads, the Board can take the Saturday without fear.")
""")

md(r"""
## Homework 7 and what comes next

`homework.md` — due **Sunday 15 November, 23:59 on Moodle**: five exercises on paper (H1 a list and a random variable, moved from Homework 6; H2 a binomial on financing quotes, H3 a Poisson rescaled twice, H4 the normal forwards and backwards, H5 two couriers in a decision tree) and a 150–250-word memo to the Board on the range to print. We go through it together at the start of next Monday's session.

Next **Monday 16 November, online**: *how sure are we of that number?* 200 bikes gave 90 km; the true average is not 90. Week 8 says how far off it can be.
""")

code(r"""
# Every number in drills.md, re-checked here. Change a number in a drill and this cell tells you what else moves.
checks = [
    ("D1 mean", np.mean([3, 8, 5, 6, 8]), 6), ("D1 sum of squares", np.sum((np.array([3, 8, 5, 6, 8]) - 6) ** 2), 18),
    ("D1 s²", np.var([3, 8, 5, 6, 8], ddof=1), 4.5), ("D1 s", np.std([3, 8, 5, 6, 8], ddof=1), 2.12),
    ("D1 E(x)", np.dot([0, 1, 2, 3, 4], [.10, .20, .40, .20, .10]), 2.0),
    ("D1 σ²", np.dot((np.array([0, 1, 2, 3, 4]) - 2) ** 2, [.10, .20, .40, .20, .10]), 1.20), ("D1 σ", math.sqrt(1.20), 1.10),
    ("D2 C(10,2)", math.comb(10, 2), 45), ("D2 binomial P(2)", stats.binom.pmf(2, 10, .3), .233), ("D2 binomial P(0)", stats.binom.pmf(0, 10, .3), .028),
    ("D2 binomial P(≥1)", 1 - stats.binom.pmf(0, 10, .3), .972), ("D2 binomial mean", 10 * .3, 3), ("D2 binomial σ", math.sqrt(10 * .3 * .7), 1.45),
    ("D2 Poisson μ=4 P(0)", stats.poisson.pmf(0, 4), .018),
    ("D2 Poisson μ for 15 min", 4 * .25, 1), ("D2 Poisson μ=1 P(0)", stats.poisson.pmf(0, 1), .368), ("D2 Poisson μ=1 P(≥1)", 1 - stats.poisson.pmf(0, 1), .632),
    ("D3 z for 20 kg", (20 - 22) / 1.5, -1.33), ("D3 P(X < 20)", stats.norm.cdf(20, 22, 1.5), .092),
    
    ("D3 z for the top 5%", stats.norm.ppf(.95), 1.645), ("D3 heaviest 5% threshold, kg", 22 + 1.645 * 1.5, 24.5),
    ("D4 margin", 1000 - 400, 600), ("D4 E(Saturday)", np.dot([1600, 4000, 6400], [.3, .5, .2]), 3760), ("D4 E(ads)", np.dot([1400, 2600], [.5, .5]), 2000),
    ("D4 difference", 3760 - 2000, 1760), ("D4 var(Saturday)", np.dot((np.array([1600, 4000, 6400]) - 3760) ** 2, [.3, .5, .2]), 2822400),
    ("D4 σ(Saturday)", math.sqrt(2822400), 1680), ("D4 var(ads)", np.dot((np.array([1400, 2600]) - 2000) ** 2, [.5, .5]), 360000), ("D4 σ(ads)", math.sqrt(360000), 600),
]
for name, got, want in checks:
    close(got, want, 5e-3 if abs(want) < 20 else 0.05)   # three decimals for shares and z, two for the rest
    print(f"  ok  {name:<32} {got:14.4f}   drills.md: {want}")
print(f"\n{len(checks)} numbers in drills.md, re-checked here: all agree.")
""")

nb["cells"] = cells
nbf.write(nb, Path(__file__).with_name("session.ipynb"))
print("wrote session.ipynb with", len(cells), "cells")
