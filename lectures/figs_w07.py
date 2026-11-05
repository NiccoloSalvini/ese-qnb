"""Static SVG figures for the week-7 deck (three shapes, and how to decide with them; Arno Bikes).
Run: python3.11 lectures/figs_w07.py  (writes lectures/img/w07_*.svg).
The bridge picture (w07_mean_vs_spread) and the two circles (w07_venn_two) now belong to lesson 6 and are not
rewritten here; their SVGs stay in img/. Every number drawn here is asserted in lectures/check_w07.py."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle
from pathlib import Path
from scipy.stats import norm, binom, skewnorm, laplace, uniform

RED, GOLD, INK, MUTED, GREEN, BLUE = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449", "#2471A3"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

def bare(ax):
    ax.set_yticks([]); ax.spines["left"].set_visible(False)

# 1 — binomial bars, n = 12 test rides, p = .25 (static fallback for the app)
n, p = 12, .25; k = np.arange(0, n + 1); f = binom.pmf(k, n, p)
fig, ax = plt.subplots(figsize=(8, 3.6))
ax.bar(k, f, color=[RED if i == 3 else GOLD for i in k], width=.7)
for i, v in zip(k, f):
    if v >= .01: ax.text(i, v + .006, f"{v:.3f}", ha="center", fontsize=11, color=INK)
ax.axvline(n * p, color=INK, lw=1, ls="--"); ax.text(n * p + .15, .30, "mean np = 3", color=INK)
ax.set_xticks(k); ax.set_xlabel("buyers among 12 test rides"); ax.set_ylim(0, .34); bare(ax); save(fig, "w07_binomial")

# 2 — the bell for battery range N(90, 8) with 68–95–99.7
mu, sg = 90, 8; x = np.linspace(mu - 4 * sg, mu + 4 * sg, 800); y = norm.pdf(x, mu, sg)
fig, ax = plt.subplots(figsize=(9, 3.8)); ax.plot(x, y, color=INK, lw=2.5)
for k_, c, a in ((3, GOLD, .18), (2, GOLD, .28), (1, RED, .35)):
    m = (x >= mu - k_ * sg) & (x <= mu + k_ * sg); ax.fill_between(x[m], y[m], 0, color=c, alpha=a)
for i, (lab, c) in enumerate((("68% · 82–98 km", RED), ("95% · 74–106 km", GOLD), ("99.7% · 66–114 km", GOLD))):
    ax.text(mu - 3.9 * sg, .050 - i * .007, lab, fontsize=13, color=c, fontweight="bold" if i == 0 else "normal")
ax.set_xticks([mu + i * sg for i in range(-3, 4)]); ax.set_xlabel("battery range (km)"); ax.set_ylim(0, .056); bare(ax)
save(fig, "w07_empirical_rule")

# 3 — the guarantee: the 5% left tail of N(90, 8) sits at 76.8 km
q = mu + norm.ppf(.05) * sg
fig, ax = plt.subplots(figsize=(9, 3.6)); ax.plot(x, y, color=INK, lw=2.5)
m = x <= q; ax.fill_between(x[m], y[m], 0, color=RED, alpha=.4)
m75 = x <= 75; ax.fill_between(x[m75], y[m75], 0, color=RED, alpha=.5)
ax.axvline(q, color=RED, lw=1.5); ax.text(q - .6, .03, f"5% below {q:.1f} km", ha="right", color=RED)
ax.text(75 - .6, .012, "3% below 75 km", ha="right", color=INK, fontsize=12)
ax.axvline(mu, color=INK, lw=1, ls="--"); ax.text(mu + .5, .048, "mean 90", color=INK)
ax.set_xticks([66, 76.8, 90, 106, 114]); ax.set_xticklabels(["66", "76.8", "90", "106", "114"])
ax.set_xlabel("battery range (km)"); ax.set_ylim(0, .056); bare(ax); save(fig, "w07_guarantee")

# 4 — skewness: battery range (symmetric) vs delivery time (right-skewed)
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

# 5 — kurtosis: three shapes, same mean and same spread, told in plain words
xk = np.linspace(-4, 4, 800)
fig, ax = plt.subplots(figsize=(9, 3.7))
ax.plot(xk, norm.pdf(xk), color=INK, lw=2.6, label="the bell: battery range (mesokurtic)")
ax.plot(xk, laplace.pdf(xk, 0, 1 / np.sqrt(2)), color=RED, lw=2.2, label="sharper peak, fatter tails: delivery delays (leptokurtic)")
ax.plot(xk, uniform.pdf(xk, -np.sqrt(3), 2 * np.sqrt(3)), color=GOLD, lw=2.2, label="flat top, no tails: a rota (platykurtic)")
ax.text(2.1, .36, "all three: same mean,\nsame standard deviation", color=MUTED, fontsize=11.5)
ax.set_xlabel("distance from the mean, in σ"); ax.set_ylim(0, 1.0); bare(ax)
ax.legend(frameon=False, fontsize=11, loc="upper left"); save(fig, "w07_kurtosis")

# 6 — the decision tree: Volta €180 certain vs Ampere €165 with a 5% fault that costs €90 to replace on the line
def box(ax, xy, w, h, text, fc="#faf9f6", ec=GOLD, tc=INK, fs=12, bold=False):
    x_, y_ = xy
    ax.add_patch(FancyBboxPatch((x_ - w / 2, y_ - h / 2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec=ec, lw=1.4))
    ax.text(x_, y_, text, ha="center", va="center", color=tc, fontsize=fs, fontweight="bold" if bold else "normal", linespacing=1.2)

def edge(ax, a, b, label=None, col=MUTED, dy=.22):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=12, color=col, lw=1.4, shrinkA=2, shrinkB=2))
    if label:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + dy, label, ha="center", va="bottom", color=col, fontsize=11, style="italic")

ev_a = .95 * 165 + .05 * 255; sd_a = np.sqrt(.95 * (165 - ev_a) ** 2 + .05 * (255 - ev_a) ** 2)
fig, ax = plt.subplots(figsize=(12, 5.2)); ax.set_xlim(0, 20); ax.set_ylim(0, 8); ax.axis("off")
ax.add_patch(FancyBboxPatch((1.0, 3.3), 2.6, 1.4, boxstyle="square,pad=0.02", fc=RED, ec=RED))
ax.text(2.3, 4.0, "Which supplier\ndo we sign?", ha="center", va="center", color="white", fontsize=12.5, fontweight="bold")
# Volta branch: no chance node, one certain payoff
edge(ax, (3.6, 4.4), (8.0, 6.3), "Volta · fixed price", INK, .3)
box(ax, (10.2, 6.3), 4.2, 1.1, "€180 a battery, certain", fs=12.5)
box(ax, (16.2, 6.3), 5.6, 1.3, "expected cost €180.00\nspread σ = €0", fc="#f2ebd9", fs=12, bold=True)
# Ampere branch: a chance node, two outcomes
edge(ax, (3.6, 3.6), (7.4, 1.9), "Ampere · €165, 5% faulty", INK, -.55)
ax.add_patch(Circle((8.0, 1.9), .42, fc=GOLD, ec=GOLD)); ax.text(8.0, 1.9, "?", ha="center", va="center", color="white", fontsize=14, fontweight="bold")
edge(ax, (8.4, 2.1), (10.2, 2.9), "good · .95", GREEN, .12)
edge(ax, (8.4, 1.7), (10.2, 0.9), "faulty · .05", RED, -.5)
box(ax, (12.1, 2.9), 3.6, .95, "€165", fs=12.5)
box(ax, (12.1, 0.9), 3.6, .95, "€165 + €90 = €255", fs=12.5)
box(ax, (16.9, 1.9), 5.6, 1.5, f"expected cost\n.95 × 165 + .05 × 255 = €{ev_a:.2f}\nspread σ = €{sd_a:.1f}", fc="#f2ebd9", fs=12, bold=True)
ax.text(10.0, 7.6, "chance nodes carry probabilities; end nodes carry payoffs; the expected value sits at the node", ha="center", color=MUTED, fontsize=11)
save(fig, "w07_decision_tree")

# 7 — the normal approximation: 250 orders, p = .06 late; the bars of the binomial, the bell over them, the ≥ 20 tail shaded
n, p = 250, .06; mu_n, sg_n = n * p, np.sqrt(n * p * (1 - p)); k = np.arange(0, 31); f = binom.pmf(k, n, p)
fig, ax = plt.subplots(figsize=(9.5, 3.9))
ax.bar(k, f, color=[RED if i >= 20 else GOLD for i in k], width=.8, alpha=.85)
xx = np.linspace(0, 30, 600); ax.plot(xx, norm.pdf(xx, mu_n, sg_n), color=INK, lw=2.5)
ax.axvline(19.5, color=RED, lw=1.2, ls="--"); ax.text(19.7, .085, "19.5: the bar for 20 starts here", color=RED, fontsize=11)
ax.text(22.5, .045, f"P(X ≥ 20) ≈ {1 - norm.cdf(19.5, mu_n, sg_n):.3f}\nexact binomial {1 - binom.cdf(19, n, p):.3f}", color=RED, fontsize=11.5)
ax.text(2, .085, f"250 orders, 6% late\nμ = np = {mu_n:.0f}, σ = √(np(1−p)) = {sg_n:.3f}", color=INK, fontsize=11.5)
ax.set_xticks(range(0, 31, 5)); ax.set_xlabel("late orders out of 250"); ax.set_ylim(0, .12); bare(ax); save(fig, "w07_normal_approx")

print("wrote", sorted(p_.name for p_ in OUT.glob("w07_*.svg")))
