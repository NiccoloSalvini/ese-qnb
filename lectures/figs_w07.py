"""Static SVG figures for the week-7 deck (probability, Arno Bikes). Run: python3.11 lectures/figs_w07.py  (writes lectures/img/w07_*.svg)."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path
from scipy.stats import norm, binom, skewnorm

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
ax.legend(frameon=False, loc="upper left"); save(fig, "w07_mean_vs_spread")

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
ax.text(0.5, 0.55, "200 customers", fontsize=13, color=INK); save(fig, "w07_venn_two")

# 3 — binomial bars, n = 12 test rides, p = .25 (static fallback for the app)
n, p = 12, .25; k = np.arange(0, n + 1); f = binom.pmf(k, n, p)
fig, ax = plt.subplots(figsize=(8, 3.6))
ax.bar(k, f, color=[RED if i == 3 else GOLD for i in k], width=.7)
for i, v in zip(k, f):
    if v >= .01: ax.text(i, v + .006, f"{v:.3f}", ha="center", fontsize=11, color=INK)
ax.axvline(n * p, color=INK, lw=1, ls="--"); ax.text(n * p + .15, .30, "mean np = 3", color=INK)
ax.set_xticks(k); ax.set_xlabel("buyers among 12 test rides"); ax.set_ylim(0, .34); bare(ax); save(fig, "w07_binomial")

# 4 — the bell for battery range N(90, 8) with 68–95–99.7
mu, sg = 90, 8; x = np.linspace(mu - 4 * sg, mu + 4 * sg, 800); y = norm.pdf(x, mu, sg)
fig, ax = plt.subplots(figsize=(9, 3.8)); ax.plot(x, y, color=INK, lw=2.5)
for k_, c, a, lab in ((3, GOLD, .18, "99.7%  ·  66–114 km"), (2, GOLD, .28, "95%  ·  74–106 km"), (1, RED, .35, "68%  ·  82–98 km")):
    m = (x >= mu - k_ * sg) & (x <= mu + k_ * sg); ax.fill_between(x[m], y[m], 0, color=c, alpha=a)
for i, (lab, c) in enumerate((("68% · 82–98 km", RED), ("95% · 74–106 km", GOLD), ("99.7% · 66–114 km", GOLD))):
    ax.text(mu - 3.9 * sg, .050 - i * .007, lab, fontsize=13, color=c if i else RED, fontweight="bold" if i == 0 else "normal")
ax.set_xticks([mu + i * sg for i in range(-3, 4)]); ax.set_xlabel("battery range (km)"); ax.set_ylim(0, .056); bare(ax)
save(fig, "w07_empirical_rule")

# 5 — the guarantee: the 5% left tail of N(90, 8) sits at 76.8 km
q = mu + norm.ppf(.05) * sg
fig, ax = plt.subplots(figsize=(9, 3.6)); ax.plot(x, y, color=INK, lw=2.5)
m = x <= q; ax.fill_between(x[m], y[m], 0, color=RED, alpha=.4)
m75 = x <= 75; ax.fill_between(x[m75], y[m75], 0, color=RED, alpha=.5)
ax.axvline(q, color=RED, lw=1.5); ax.text(q - .6, .03, f"5% below {q:.1f} km", ha="right", color=RED)
ax.text(75 - .6, .012, "3% below 75 km", ha="right", color=INK, fontsize=12)
ax.axvline(mu, color=INK, lw=1, ls="--"); ax.text(mu + .5, .048, "mean 90", color=INK)
ax.set_xticks([66, 76.8, 90, 106, 114]); ax.set_xticklabels(["66", "76.8", "90", "106", "114"])
ax.set_xlabel("battery range (km)"); ax.set_ylim(0, .056); bare(ax); save(fig, "w07_guarantee")

# 6 — skewness: battery range (symmetric) vs delivery time (right-skewed)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.4))
xs = np.linspace(60, 120, 400); a1.plot(xs, norm.pdf(xs, 90, 8), color=INK, lw=2.5)
a1.axvline(90, color=RED, lw=1.5); a1.text(92.5, .045, "mean = median", color=RED)
a1.set_title("battery range: symmetric, skewness 0", fontsize=13, color=INK); a1.set_xlabel("km"); bare(a1)
xd = np.linspace(0, 12, 400); dist = skewnorm(6, loc=1.5, scale=3); yd = dist.pdf(xd)
a2.plot(xd, yd, color=INK, lw=2.5)
med, mean = dist.median(), dist.mean()
a2.axvline(med, color=GOLD, lw=1.5); a2.axvline(mean, color=RED, lw=1.5)
a2.text(med - .15, .30, "median", color=GOLD, ha="right"); a2.text(mean + .15, .30, "mean", color=RED)
a2.set_title("delivery time: a long right tail, mean > median", fontsize=13, color=INK); a2.set_xlabel("days"); bare(a2)
save(fig, "w07_skew")

print("wrote", sorted(p.name for p in OUT.glob("w07_*.svg")))
