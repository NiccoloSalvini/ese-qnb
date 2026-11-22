"""Static SVG figures for the week-9 deck (read the output, then read the calendar; Arno Bikes).
Run: python3.11 lectures/figs_w09.py   (writes lectures/img/w09_*.svg from lectures/data/w09_*.csv).
Every number drawn here is asserted in lectures/check_w09.py."""
import csv, numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

RED, GOLD, INK, MUTED, GREEN, BLUE = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449", "#2471A3"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
HERE = Path(__file__).parent; OUT = HERE / "img"; DATA = HERE / "data"

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

def read(name):
    with open(DATA / name) as f: return list(csv.DictReader(f))

# 1 — 24 shop-months, ads against bikes, one pooled line (the shops are told apart only in block B)
rows = read("w09_shops.csv")
ads = np.array([float(r["ads_k"]) for r in rows]); y = np.array([float(r["bikes"]) for r in rows])
b, a = np.polyfit(ads, y, 1)
fig, ax = plt.subplots(figsize=(6.4, 4.4))
xx = np.linspace(1.5, 10.5, 2)
ax.plot(xx, a + b * xx, color=RED, lw=2, label=f"bikes = {a:.2f} + {b:.2f} × ads")
ax.scatter(ads, y, s=46, color=MUTED, zorder=3)
ax.set_xlabel("ads in the month (€ thousand)"); ax.set_ylabel("bikes sold in the month")
ax.legend(frameon=False, loc="upper left", fontsize=12); save(fig, "w09_shops_scatter")

# 2 — twelve quarters with the least-squares trend
q = np.array([float(r["bikes"]) for r in read("w09_quarters.csv")]); t = np.arange(1, 13)
bt, at = np.polyfit(t, q, 1)
fig, ax = plt.subplots(figsize=(6.8, 4.2))
ax.plot(t, q, "-o", color=BLUE, lw=2, ms=6, label="bikes sold")
ax.plot(np.r_[0.5, 12.5], at + bt * np.r_[0.5, 12.5], color=RED, lw=1.8, ls="--", label=f"trend {at:.1f} + {bt:.1f} t")
for i, v in enumerate(q, 1):
    if i % 4 == 3: ax.annotate("summer", (i, v), (i - .6, v + 18), fontsize=11, color=MUTED)
ax.set_xticks(t, [f"Q{(i - 1) % 4 + 1}\n'{24 + (i - 1) // 4}" for i in t], fontsize=10)
ax.set_ylabel("bikes sold in the quarter"); ax.set_ylim(260, 620)
ax.legend(frameon=False, loc="upper left", fontsize=12); save(fig, "w09_quarters")

# 3 — 36 months of web orders around 100
o = np.array([float(r["orders"]) for r in read("w09_orders.csv")]); m = np.arange(1, 37)
fig, ax = plt.subplots(figsize=(7.2, 4.0))
ax.axhline(99.5, color=MUTED, lw=1, ls="--"); ax.text(36.6, 99.5, "≈ 100", va="center", color=MUTED, fontsize=11)
ax.plot(m, o, "-o", color=BLUE, lw=1.6, ms=4)
ax.plot([36], [o[-1]], "o", color=RED, ms=9); ax.annotate("last month: 110", (36, 110), (27.5, 112.5), color=RED, fontsize=12)
ax.set_xlabel("month"); ax.set_ylabel("web orders"); ax.set_ylim(80, 116); save(fig, "w09_orders")


# 4 — the trend alone leaves a pattern: residuals of the straight trend, quarter by quarter
res = q - (at + bt * t)
fig, ax = plt.subplots(figsize=(7.4, 3.8))
cols = [BLUE, GOLD, RED, MUTED]
ax.bar(t, res, color=[cols[(i - 1) % 4] for i in t], width=.7)
ax.axhline(0, color=INK, lw=1)
for i, v in zip(t, res):
    ax.text(i, v + (5 if v > 0 else -13), f"{v:+.0f}", ha="center", fontsize=10, color=INK)
ax.set_xticks(t, [f"Q{(i - 1) % 4 + 1}\n'{24 + (i - 1) // 4}" for i in t], fontsize=10)
ax.set_ylabel("sales minus the trend"); ax.set_ylim(-95, 140)
ax.text(.6, 126, "every summer above, every winter below: the error repeats", fontsize=12, color=RED)
save(fig, "w09_trend_residuals")

# 5 — web orders: this month's gap against last month's (r = .59), before the fix
gap = o - o.mean()
fig, ax = plt.subplots(figsize=(5.2, 4.2))
ax.scatter(gap[:-1], gap[1:], s=36, color=BLUE)
bb, aa = np.polyfit(gap[:-1], gap[1:], 1); xx = np.linspace(gap.min(), gap.max(), 2)
ax.plot(xx, aa + bb * xx, color=RED, lw=1.8)
ax.axhline(0, color=MUTED, lw=.8); ax.axvline(0, color=MUTED, lw=.8)
ax.set_xlabel("last month's gap from the average"); ax.set_ylabel("this month's gap")
ax.text(.03, .93, f"r = {np.corrcoef(gap[:-1], gap[1:])[0, 1]:.2f}", transform=ax.transAxes, color=RED, fontsize=13)
save(fig, "w09_orders_lag")

print("ok", sorted(p.name for p in OUT.glob("w09_*.svg")))
