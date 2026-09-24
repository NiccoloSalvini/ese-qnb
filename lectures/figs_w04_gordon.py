"""Week-4 Gordon figure: what Arno Bikes is worth as the growth rate moves.
Run: python3 lectures/figs_w04_gordon.py  (writes lectures/img/w04_gordon.svg).
Same palette and rcParams as lectures/figs.py, copied so the two scripts stay independent."""
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

CF1, R = 300.0, 0.09                      # € thousand next year, cost of capital
def value(g): return CF1 / (R - g)        # € thousand

fig, ax = plt.subplots(figsize=(7.2, 3.9))
g = np.linspace(0, 0.075, 300)
ax.plot(g * 100, value(g) / 1000, color=INK, lw=2.8)
ax.axvline(R * 100, color=RED, lw=1.8, ls="--")
ax.text(R * 100 - 0.15, 19.2, "g = r = 9%\nthe formula breaks", color=RED, ha="right", va="top", fontsize=11.5)
for gg, dx, dy in ((0.02, 0.6, -2.6), (0.03, -0.4, 2.4), (0.04, 0.5, -0.9)):
    v = value(gg) / 1000
    ax.plot(gg * 100, v, "o", color=GOLD if gg != 0.03 else RED, ms=9, zorder=3)
    ax.annotate(f"g = {gg:.0%}:  €{v:.2f}M".replace(".00M", "M"), (gg * 100, v), (gg * 100 + dx, v + dy),
                fontsize=11.5, color=INK, fontweight="bold", ha="right" if dx < 0 else "left", va="center",
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=1, shrinkA=2, shrinkB=6))
ax.text(0.15, value(0) / 1000 - 1.6, "no growth: €3.33M", color=MUTED, fontsize=11)
ax.set_xlim(0, 10); ax.set_ylim(0, 20.5)
ax.set_xticks(range(0, 11)); ax.set_xlabel("growth for ever, g  %")
ax.set_ylabel("value today, € million")
fig.savefig(OUT / "w04_gordon.svg", bbox_inches="tight", transparent=True); plt.close(fig)
print("w04_gordon written")
