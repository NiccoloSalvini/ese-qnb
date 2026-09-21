"""Static SVG figures for the week-1 deck. Run: python3 lectures/figs.py  (writes lectures/img/*.svg)."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

RED, GOLD, INK, MUTED, GREEN = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

def k(x, _): return f"{int(x/1000)}k" if x else "0"

# 1 — two lines and a crossing
q = np.linspace(0, 250, 2)
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(q, 60000 + 400*q, color=RED, lw=3, label="C(q) = 60,000 + 400q")
ax.plot(q, 1000*q, color=INK, lw=3, label="R(q) = 1,000q")
ax.plot(100, 100000, "o", color=GOLD, ms=9); ax.annotate("break-even  q* = 100", (100, 100000), (108, 92000), color=INK)
ax.set_xlabel("bikes per month  q"); ax.set_ylabel("€ per month"); ax.set_xlim(0, 250); ax.set_ylim(0, 250000)
ax.yaxis.set_major_formatter(k); ax.legend(frameon=False, loc="upper left"); save(fig, "w01_breakeven")

# 2 — parallel shift
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.plot(q, 60000 + 400*q, color=RED, lw=3, label="C(q)")
ax.plot(q, 72000 + 400*q, color=RED, lw=3, ls="--", label="C(q) after the shock")
ax.plot(q, 1000*q, color=INK, lw=3, label="R(q)")
ax.plot([100, 120], [100000, 120000], "o", color=GOLD, ms=9)
ax.set_xticks([100, 120]); ax.set_yticks([60000, 72000, 100000, 120000]); ax.yaxis.set_major_formatter(k)
ax.set_xlabel("q"); ax.set_ylabel("€"); ax.set_xlim(0, 250); ax.set_ylim(0, 250000); ax.legend(frameon=False, loc="upper left"); save(fig, "w01_shift")

# 3 — market picture (Q on x, p on y)
p = np.linspace(0, 600, 2)
fig, ax = plt.subplots(figsize=(4.2, 3.4))
ax.plot(1200 - 2*p, p, color=INK, lw=3, label="demand"); ax.plot(-300 + 3*p, p, color=RED, lw=3, label="supply")
ax.plot(600, 300, "o", color=GOLD, ms=9); ax.annotate("(600, 300)", (600, 300), (640, 250), color=INK)
ax.set_xlim(0, 1300); ax.set_ylim(0, 600); ax.set_xlabel("Q"); ax.set_ylabel("p"); ax.set_xticks([]); ax.set_yticks([]); ax.legend(frameon=False); save(fig, "w01_market")

# 4 — profit parabola with roots, vertex, sign line
q = np.linspace(0, 300, 300); pi = -4*q**2 + 1200*q - 60000
fig, (ax, sl) = plt.subplots(2, 1, figsize=(6.4, 4.8), height_ratios=[5, 1], sharex=True)
ax.plot(q, pi, color=GREEN, lw=3); ax.axhline(0, color=INK, lw=1)
ax.fill_between(q, pi, 0, where=pi > 0, color=GREEN, alpha=.12)
ax.plot([63.4, 236.6], [0, 0], "o", color=RED, ms=9); ax.plot(150, 30000, "o", color=GREEN, ms=9)
ax.set_ylim(-70000, 40000); ax.set_yticks([-60000, 0, 30000]); ax.yaxis.set_major_formatter(k); ax.set_ylabel("π(q)")
sl.axhline(0, color=INK, lw=1.5); sl.set_ylim(-1, 1); sl.set_yticks([]); sl.spines["left"].set_visible(False)
for x in (63.4, 236.6): sl.plot([x, x], [-.3, .3], color=INK, lw=1.5)
for x, s, c in ((30, "−", RED), (150, "+", GREEN), (270, "−", RED)): sl.text(x, .35, s, color=c, ha="center", fontsize=16, fontweight="bold")
sl.set_xticks([63.4, 150, 236.6]); sl.set_xlabel("q  —  the sign line"); ax.set_xlim(0, 300); save(fig, "w01_parabola_sign")

# 5 — tolerance band on the number line
fig, ax = plt.subplots(figsize=(7, 1.6))
ax.axhline(0, color=INK, lw=1.5); ax.plot([485, 515], [0, 0], color=GREEN, lw=9, solid_capstyle="butt")
for x in (485, 500, 515): ax.plot([x, x], [-.25, .25], color=INK, lw=1.5); ax.text(x, -.55, str(x), ha="center")
ax.plot(483, 0, "x", color=RED, ms=14, mew=3); ax.text(483, .45, "483", color=RED, ha="center")
ax.set_xlim(468, 532); ax.set_ylim(-1, 1); ax.axis("off"); save(fig, "w01_tolerance")
print("ok", sorted(p.name for p in OUT.glob("*.svg")))


# ---------------------------------------------------------------- weeks 2–5

def profit(q): return -4 * q**2 + 1200 * q - 60000


# w02 — the derivative as a slope you can read off
fig, ax = plt.subplots(figsize=(6.6, 4.0))
qs = np.linspace(0, 300, 400)
ax.plot(qs, profit(qs), color=INK, lw=2.5)
ax.axhline(0, color=MUTED, lw=1)
for q0, col in ((80, GREEN), (150, GOLD), (220, RED)):
    s = -8 * q0 + 1200
    xs = np.linspace(q0 - 55, q0 + 55, 2)
    ax.plot(xs, profit(q0) + s * (xs - q0), color=col, lw=2.5)
    ax.plot(q0, profit(q0), "o", color=col, ms=8)
    label = f"π'({q0}) = {s:+,.0f}" if s else f"π'({q0}) = 0  ← the top"
    ax.annotate(label, (q0, profit(q0)), (q0 - 34, profit(q0) - 24000),
                color=col, fontsize=11, fontweight="bold")
ax.set_xlabel("bikes per month  q"); ax.set_ylabel("profit €"); ax.yaxis.set_major_formatter(k)
ax.set_xlim(0, 300); ax.set_ylim(-70000, 45000); save(fig, "w02_three_tangents")

# w03 — average cost meets marginal cost at the bottom
fig, ax = plt.subplots(figsize=(6.4, 4.0))
qs = np.linspace(1.5, 18, 400)
ac = 0.4 * qs + 3 + 25 / qs
mc = 0.8 * qs + 3
ax.plot(qs, ac, color=INK, lw=2.5, label="average cost  C(q)/q")
ax.plot(qs, mc, color=RED, lw=2.5, label="marginal cost  C'(q)")
qstar = np.sqrt(62.5)
ax.plot(qstar, 0.4 * qstar + 3 + 25 / qstar, "o", color=GOLD, ms=9)
ax.annotate("they cross exactly\nat the minimum", (qstar, 0.4 * qstar + 3 + 25 / qstar),
            (qstar + 2.2, 7.5), color=GOLD, fontsize=11, fontweight="bold")
ax.set_xlabel("q"); ax.set_ylabel("€ thousand per unit"); ax.set_ylim(0, 20)
ax.legend(frameon=False, loc="upper center"); save(fig, "w03_ac_mc")

# w04 — the discount factor, and why distant money is cheap
fig, ax = plt.subplots(figsize=(6.6, 3.8))
years = np.arange(0, 21)
for r, col, lab in ((0.03, GOLD, "3%"), (0.09, INK, "9%"), (0.16, RED, "16%")):
    ax.plot(years, 1 / (1 + r) ** years, color=col, lw=2.5, label=lab)
ax.set_xlabel("years away"); ax.set_ylabel("worth of €1 today")
ax.set_ylim(0, 1.02); ax.legend(frameon=False, title="discount rate")
save(fig, "w04_discount_factor")

# w05 — price against yield, with the tangent duration draws
FACE, CPN, N, Y0 = 100.0, 0.05, 10, 0.05
def bond(y): return sum(CPN * FACE / (1 + y) ** t for t in range(1, N + 1)) + FACE / (1 + y) ** N
fig, ax = plt.subplots(figsize=(6.6, 4.0))
ys = np.linspace(0.01, 0.10, 300)
ax.plot(ys * 100, [bond(v) for v in ys], color=INK, lw=2.5, label="the bond")
slope = (bond(Y0 + 1e-6) - bond(Y0 - 1e-6)) / 2e-6
ax.plot(ys * 100, bond(Y0) + slope * (ys - Y0), color=RED, lw=2, ls="--", label="what duration predicts")
ax.fill_between(ys * 100, bond(Y0) + slope * (ys - Y0), [bond(v) for v in ys], color=GOLD, alpha=.25,
                label="the gap: convexity")
ax.plot(Y0 * 100, bond(Y0), "o", color=GOLD, ms=9)
ax.set_xlabel("yield  %"); ax.set_ylabel("price €"); ax.legend(frameon=False, loc="upper right")
save(fig, "w05_price_yield")
print("weeks 2-5 figures written")


# w03 — the staircase: every bike has its own price tag, and the total is the pile of them
fig, ax = plt.subplots(figsize=(7.0, 3.9))
bikes = np.arange(1, 21)
each = 0.8 * (bikes - 0.5) + 3          # the cost of the n-th bike
bars = ax.bar(bikes, each, width=0.86, color=GOLD, edgecolor="white", linewidth=1.1)
for n in (1, 10, 20):
    ax.annotate(f"bike {n}\n€{each[n-1]:.2f}", (n, each[n-1]), (n, each[n-1] + 3.4),
                ha="center", fontsize=10, color=INK, fontweight="bold",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1))
ax.plot(bikes, each, color=RED, lw=2.5, label="MC(q) = 0.8q + 3")
ax.set_xlabel("which bike"); ax.set_ylabel("what that one bike costs, €")
ax.set_xticks([1, 5, 10, 15, 20]); ax.set_ylim(0, 26)
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0, 0.88))
ax.text(10.5, 24.2, "add the twenty bars together  →  €220", ha="center", fontsize=12.5,
        color=RED, fontweight="bold")
save(fig, "w03_staircase")

# w04 — the same euro, two ways, year by year
fig, ax = plt.subplots(figsize=(7.0, 3.9))
yrs = np.arange(0, 11)
simple = 8000 * (1 + 0.06 * yrs)
comp = 8000 * 1.06 ** yrs
ax.plot(yrs, simple, color=MUTED, lw=3, marker="o", ms=5, label="simple — €480 every year")
ax.plot(yrs, comp, color=RED, lw=3, marker="o", ms=5, label="compound — 6% of whatever is there")
ax.fill_between(yrs, simple, comp, color=GOLD, alpha=.3)
for y in (3, 10):
    ax.annotate(f"+€{comp[y]-simple[y]:,.0f}", (y, comp[y]), (y - 1.6, comp[y] + 500),
                fontsize=11, color=GOLD, fontweight="bold")
ax.set_xlabel("years"); ax.set_ylabel("€"); ax.yaxis.set_major_formatter(k)
ax.set_xticks(yrs); ax.legend(frameon=False, loc="upper left")
save(fig, "w04_two_ways")
print("staircase and two-ways written")
