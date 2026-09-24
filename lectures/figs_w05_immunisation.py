"""Week-5 immunisation figure. Run: python3 lectures/figs_w05_immunisation.py  (writes lectures/img/w05_immunisation.svg).

Kept apart from figs.py on purpose; same palette and rcParams.
Arno Bikes owes €1M in 4 years; flat yield 5%. Money set aside today = 1,000,000/1.05^4.
Yields jump once, the day after purchase, to y. Value at year 4 of each holding:
a 2-year zero's face reinvested for 2 years at y, a 6-year zero sold with 2 years left at y.
"""
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

L, Y0, H = 1_000_000, 0.05, 4
PV = L / (1 + Y0) ** H                                   # 822,702.47


def horizon_value(w_short, y):
    """Value at year 4 when a share w_short of PV sits in the 2-year zero, the rest in the 6-year zero."""
    face2 = w_short * PV * (1 + Y0) ** 2                  # paid at year 2, reinvested to year 4
    face6 = (1 - w_short) * PV * (1 + Y0) ** 6            # paid at year 6, sold at year 4
    return face2 * (1 + y) ** 2 + face6 / (1 + y) ** 2


assert abs(horizon_value(0.5, 0.06) - 1_000_179.70) < 0.01
assert abs(horizon_value(0.5, 0.04) - 1_000_183.15) < 0.01

ys = np.linspace(0.03, 0.07, 200)
fig, ax = plt.subplots(figsize=(6.4, 4.2))
ax.axhline(L, color=MUTED, lw=1, ls=":")
ax.text(3.08, L - 3500, "the €1M we owe", color=MUTED, fontsize=12, va="top")
ax.plot(ys * 100, [horizon_value(1.0, v) for v in ys], color=INK, lw=2.5, label="all in the 2-year zero")
ax.plot(ys * 100, [horizon_value(0.0, v) for v in ys], color=GOLD, lw=2.5, label="all in the 6-year zero")
ax.plot(ys * 100, [horizon_value(0.5, v) for v in ys], color=RED, lw=3.5, label="half and half: duration 4")
ax.plot(Y0 * 100, L, "o", color=RED, ms=8)
ax.set_xlabel("yield after the move  %"); ax.set_ylabel("value at year 4  €")
ax.set_xlim(3, 7); ax.set_ylim(955_000, 1_045_000)
ax.yaxis.set_major_formatter(lambda x, _: f"{x/1000:,.0f}k")
ax.legend(frameon=False, loc="upper center", fontsize=12)
fig.savefig(OUT / "w05_immunisation.svg", bbox_inches="tight", transparent=True); plt.close(fig)
print("wrote", OUT / "w05_immunisation.svg")
