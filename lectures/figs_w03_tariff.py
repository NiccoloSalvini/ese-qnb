"""Week-3 tariff figures: a tariff on an imported part, first for the firm, then for the country.
Run: python3 lectures/figs_w03_tariff.py  (writes lectures/img/w03_tariff_profit.svg and w03_small_nation.svg).
Same palette and rcParams as lectures/figs.py, copied so the two scripts stay independent."""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

RED, GOLD, INK, MUTED, GREEN, NAVY = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449", "#2471A3"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

# the firm: R = 30 ln(q+1), C = 0.4q² + bq + 25; the tariff lifts b from 3 to 3.5 (€ thousand)
def profit(q, b): return 30 * np.log(q + 1) - 0.4 * q**2 - b * q - 25
q = np.linspace(0, 8, 400)
fig, ax = plt.subplots(figsize=(7.0, 4.0))
ax.axhline(0, color=MUTED, lw=1)
ax.plot(q, profit(q, 3.0), color=INK, lw=2.8, label="before:  C = 0.4q² + 3q + 25")
ax.plot(q, profit(q, 3.5), color=RED, lw=2.8, ls="--", label="with the tariff:  C = 0.4q² + 3.5q + 25")
for qs, b, col, xy in ((3.901, 3.0, INK, (4.3, 5.6)), (3.664, 3.5, RED, (0.3, 3.4))):
    ax.plot(qs, profit(qs, b), "o", color=col, ms=8)
    ax.annotate(f"q* = {qs:.2f},  π = {profit(qs, b):.2f}", (qs, profit(qs, b)), xy, color=col, fontsize=11.5)
for z, col in ((1.935, INK), (6.264, INK), (2.139, RED), (5.440, RED)):
    ax.plot(z, 0, "o", color=col, ms=6, mfc="white", mew=2)
ax.set_xlim(0, 8); ax.set_ylim(-12, 7.5); ax.set_xlabel("output q"); ax.set_ylabel("profit, € thousand")
ax.legend(frameon=False, loc="lower center", fontsize=11.5)
save(fig, "w03_tariff_profit")

# the country: Qd = 100 − p, Qs = p − 20; world price 40, tariff 10 (Q in thousands, p in €)
Q = np.linspace(0, 100, 201)
fig, ax = plt.subplots(figsize=(7.0, 4.6))
ax.plot(Q, 100 - Q, color=INK, lw=2.6); ax.text(88, 8, "demand", color=INK)
ax.plot(Q[Q <= 80], 20 + Q[Q <= 80], color=NAVY, lw=2.6); ax.text(52, 86, "domestic\nsupply", color=NAVY)
ax.axhline(40, color=MUTED, lw=1.6); ax.text(99, 41.5, "world price 40", ha="right", va="bottom", color=MUTED, fontsize=11)
ax.axhline(50, color=RED, lw=1.6, ls="--"); ax.text(99, 51.5, "with the tariff 50", ha="right", va="bottom", color=RED, fontsize=11)
ax.fill([0, 20, 30, 0], [40, 40, 50, 50], color=GOLD, alpha=.55, lw=0)                # to domestic producers
ax.fill([20, 30, 30], [40, 40, 50], color=GREEN, alpha=.55, lw=0)                      # protective effect
ax.fill([30, 50, 50, 30], [40, 40, 50, 50], color=NAVY, alpha=.45, lw=0)               # government revenue
ax.fill([50, 50, 60], [40, 50, 40], color=RED, alpha=.55, lw=0)                        # consumption effect
ax.plot(40, 60, "o", color=INK, ms=7); ax.annotate("autarky (40, 60)", (40, 60), (44, 64), fontsize=11)
for x in (20, 30, 50, 60): ax.plot([x, x], [0, 40 if x in (20, 60) else 50], color=MUTED, lw=.8, ls=":")
ax.set_xticks([20, 30, 50, 60]); ax.set_yticks([20, 40, 50, 60, 100])
ax.set_xlim(0, 100); ax.set_ylim(0, 105); ax.set_xlabel("quantity Q, thousand"); ax.set_ylabel("price p, €")
from matplotlib.patches import Patch
ax.legend(handles=[Patch(color=GOLD, alpha=.55, label="to producers  250"),
                   Patch(color=GREEN, alpha=.55, label="protective effect  50"),
                   Patch(color=NAVY, alpha=.45, label="tariff revenue  200"),
                   Patch(color=RED, alpha=.55, label="consumption effect  50")],
          frameon=False, loc="upper left", bbox_to_anchor=(1.0, 1.0), fontsize=11, title="lost by consumers: 550", title_fontsize=11.5)
save(fig, "w03_small_nation")
print("tariff profit and small-nation figures written")
