"""Static SVG figures for the week-8 deck (how sure are we of that number; Arno Bikes).
Run: python3.11 lectures/figs_w08.py   (writes lectures/img/w08_*.svg).
The normal approximation picture is lesson 7's w07_normal_approx.svg, reused. Every number drawn here is
asserted in lectures/check_w08.py."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

RED, GOLD, INK, MUTED, GREEN, BLUE = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449", "#2471A3"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

# 1 — five test days: temperature against range, with the least-squares line 80 + 0.8x
x = np.array([0, 5, 10, 15, 20]); y = np.array([80, 84, 89, 90, 97])
b = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum(); a = y.mean() - b * x.mean()
assert (a, b) == (80, 0.8)
fig, ax = plt.subplots(figsize=(6.4, 4.2))
xx = np.linspace(-1, 21, 2)
ax.plot(xx, a + b * xx, color=RED, lw=2, label="range = 80 + 0.8 × temperature")
for xi, yi in zip(x, y):
    ax.plot([xi, xi], [yi, a + b * xi], color=MUTED, lw=1, ls=":")
ax.scatter(x, y, s=70, color=BLUE, zorder=3)
ax.scatter([x.mean()], [y.mean()], s=60, marker="x", color=INK, zorder=4)
ax.annotate("the centre (10, 88)", (10, 88), (11.2, 84.2), fontsize=11, color=INK,
            arrowprops=dict(arrowstyle="-", color=MUTED, lw=.8))
ax.set_xlabel("temperature (°C)"); ax.set_ylabel("range (km)")
ax.set_xlim(-1.5, 21.5); ax.set_ylim(76, 100); ax.set_xticks(x)
ax.legend(frameon=False, loc="upper left", fontsize=12); save(fig, "w08_scatter")

# 2 — four clouds and their r
rng = np.random.default_rng(8)
def cloud(r, n=60):
    z1, z2 = rng.standard_normal(n), rng.standard_normal(n)
    return z1, r * z1 + np.sqrt(1 - r ** 2) * z2
panels = [(.95, "r ≈ +0.95\nclose to a rising line"), (.5, "r ≈ +0.5\na loose rising cloud"),
          (0, "r ≈ 0\nno straight-line relation"), (-.8, "r ≈ −0.8\na falling line")]
fig, axs = plt.subplots(1, 5, figsize=(14, 3.1), gridspec_kw=dict(wspace=.25))
for ax, (r, lab) in zip(axs[:4], panels):
    u, v = cloud(r); ax.scatter(u, v, s=14, color=BLUE, alpha=.8)
    ax.set_title(lab, fontsize=12, color=INK); ax.set_xticks([]); ax.set_yticks([])
u = np.linspace(-2, 2, 60); v = u ** 2 + rng.normal(0, .25, 60)
axs[4].scatter(u, v, s=14, color=RED, alpha=.8)
axs[4].set_title(f"r ≈ {np.corrcoef(u, v)[0, 1]:+.1f}\nbut a clear curve", fontsize=12, color=RED)
axs[4].set_xticks([]); axs[4].set_yticks([])
save(fig, "w08_r_shapes")

print("ok", sorted(p.name for p in OUT.glob("w08_*.svg")))
