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
