"""Static SVG figures for the week-6 deck (sets, conditional probability, the language of distributions — Arno Bikes).
Run: python3.11 lectures/figs_w06.py  (writes lectures/img/w06_*.svg)."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path
from scipy.stats import norm

RED, GOLD, INK, MUTED, GREEN, BLUE = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449", "#2471A3"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

def bare(ax):
    ax.set_yticks([]); ax.spines["left"].set_visible(False)

# 1 — the bridge: same mean (100 bikes a month), two spreads; stock set at 110
x = np.linspace(40, 160, 600)
fig, ax = plt.subplots(figsize=(9, 3.8))
for s, c, lab in ((5, GREEN, "σ = 5 bikes"), (20, RED, "σ = 20 bikes")):
    y = norm.pdf(x, 100, s); ax.plot(x, y, color=c, lw=2.5, label=lab)
    m = x >= 110; ax.fill_between(x[m], y[m], 0, color=c, alpha=.25)
ax.axvline(100, color=INK, lw=1, ls="--"); ax.axvline(110, color=INK, lw=1.5)
ax.text(100, .083, "mean 100", ha="center", color=INK); ax.text(111, .06, "stock 110", color=INK)
ax.text(128, .006, "31% of months\nrun out", color=RED, fontsize=12)
ax.text(113, .022, "2%", color=GREEN, fontsize=12)
ax.set_xlabel("bikes demanded in a month"); ax.set_xlim(40, 160); ax.set_ylim(0, .09); bare(ax)
ax.legend(frameon=False, loc="upper left"); save(fig, "w06_mean_vs_spread")

# 2 — two circles: 200 customers, 120 accessories, 90 service plan, 40 neither → 50 both
fig, ax = plt.subplots(figsize=(7.5, 4.4)); ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.set_aspect("equal"); ax.axis("off")
ax.add_patch(plt.Rectangle((0.3, 0.3), 9.4, 5.4, fill=False, ec=INK, lw=1.5))
ax.add_patch(Circle((3.9, 3), 2.2, fc=RED, alpha=.18, ec=RED, lw=2))
ax.add_patch(Circle((6.3, 3), 2.2, fc=GOLD, alpha=.25, ec=GOLD, lw=2))
ax.text(2.9, 3, "70", ha="center", va="center", fontsize=22, color=INK)
ax.text(5.1, 3, "50", ha="center", va="center", fontsize=22, color=INK, fontweight="bold")
ax.text(7.3, 3, "40", ha="center", va="center", fontsize=22, color=INK)
ax.text(8.9, 0.8, "40 neither", ha="right", fontsize=14, color=MUTED)
ax.text(2.6, 5.45, "accessories · 120", ha="center", fontsize=14, color=RED)
ax.text(7.6, 5.45, "service plan · 90", ha="center", fontsize=14, color=GOLD)
ax.text(0.5, 0.55, "200 customers", fontsize=13, color=INK); save(fig, "w06_venn_two")

# 3 — the distribution of next week's returns: the shares table drawn as bars, mean 5, σ 1.26
vals = np.array([3, 4, 5, 6, 7]); P = np.array([.15, .20, .30, .20, .15])
mu = float((vals * P).sum()); sg = float(np.sqrt(((vals - mu) ** 2 * P).sum()))
fig, ax = plt.subplots(figsize=(8, 3.6))
ax.bar(vals, P, color=[RED if v == 5 else GOLD for v in vals], width=.7)
for v, p in zip(vals, P): ax.text(v, p + .008, f"{p:.2f}", ha="center", fontsize=12, color=INK)
ax.plot([mu, mu], [.325, .375], color=INK, lw=1, ls="--"); ax.text(mu + .08, .352, f"E(x) = {mu:.0f}", color=INK)
ax.annotate("", xy=(mu - sg, .04), xytext=(mu + sg, .04), arrowprops=dict(arrowstyle="<->", color=INK, lw=1.3))
ax.text(mu, .04, f"σ = {sg:.2f}", ha="center", va="center", color=INK, fontsize=12, bbox=dict(fc="white", ec="none", pad=2))
ax.set_xticks(vals); ax.set_xlabel("returns next week"); ax.set_ylim(0, .38); bare(ax); save(fig, "w06_returns_dist")

print("wrote", sorted(p.name for p in OUT.glob("w06_*.svg")))
