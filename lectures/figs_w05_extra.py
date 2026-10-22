"""Week-5 extra figures. Run: python3 lectures/figs_w05_extra.py  (writes lectures/img/w05_*.svg).

Kept apart from figs.py on purpose; same palette and rcParams.
- w05_old_new_bond: why an old bond is worth less once rates rise (three panels).
- w05_timeline: a bond's cash flows on a time line, each brought back to today.
- w05_tangent: the tangent's triangle, one point of yield and €7.72 of price.
- w05_study_profit / w05_study_cr: the cargo-bike study, midterm format.
Cargo bike, q = tens of bikes a month, € thousand: C = q³ − 9q² + 30q + 20, R = 45q − 3q², π = R − C.
"""
import numpy as np, matplotlib, logging
logging.getLogger("matplotlib.font_manager").setLevel(logging.ERROR)
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from pathlib import Path

RED, GOLD, INK, MUTED, GREEN = "#AF1F25", "#a8955a", "#363636", "#7a7f85", "#1E8449"
plt.rcParams.update({"font.family": ["Source Sans 3", "Source Sans Pro", "Helvetica", "Arial"], "font.size": 13,
                     "axes.edgecolor": MUTED, "axes.labelcolor": INK, "xtick.color": INK, "ytick.color": INK,
                     "axes.spines.top": False, "axes.spines.right": False, "svg.fonttype": "none"})
OUT = Path(__file__).parent / "img"; OUT.mkdir(exist_ok=True)

def save(fig, name):
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", transparent=True); plt.close(fig)

def price(cpn, y, n=5, face=100):
    return sum(cpn / (1 + y) ** t for t in range(1, n + 1)) + face / (1 + y) ** n

# w05_old_new_bond — yesterday, today, and what your old bond fetches
fig, ax = plt.subplots(figsize=(11, 3.9)); ax.axis("off"); ax.set_xlim(0, 33); ax.set_ylim(0, 12)
panels = [
    (0.3, "YESTERDAY · rates 4%", "Your bond", "pays €4 a year for 5 years\n+ €100 at the end", "price €100", INK),
    (11.6, "TODAY · rates rise to 6%", "A new bond comes out", "pays €6 a year for 5 years\n+ €100 at the end", "price €100", GREEN),
    (22.9, "TODAY · you want to sell", "Your old bond", "still pays only €4 a year\n+ €100 at the end", f"price €{price(4, .06):.2f}", RED),
]
for x, head, title, body, tag, col in panels:
    ax.add_patch(FancyBboxPatch((x, 0.6), 9.8, 10.2, boxstyle="round,pad=0.1,rounding_size=0.6",
                                fc="white", ec=col, lw=2.5))
    ax.text(x + 4.9, 9.7, head, ha="center", fontsize=11, color=MUTED, fontweight="bold")
    ax.text(x + 4.9, 8.1, title, ha="center", fontsize=16, color=col, fontweight="bold")
    ax.text(x + 4.9, 5.3, body, ha="center", fontsize=13, color=INK, linespacing=1.5)
    ax.add_patch(FancyBboxPatch((x + 1.9, 1.4), 6.0, 1.9, boxstyle="round,pad=0.1,rounding_size=0.4",
                                fc=col, ec=col))
    ax.text(x + 4.9, 2.35, tag, ha="center", va="center", fontsize=16, color="white", fontweight="bold")
for x0 in (10.3, 21.6):
    ax.add_patch(FancyArrowPatch((x0, 5.7), (x0 + 1.2, 5.7), arrowstyle="-|>", mutation_scale=22, color=MUTED, lw=2))
ax.text(28.1, -0.4, "nobody pays €100 for €4 when €6 is on sale:\nthe price drops until it also earns 6%",
        ha="center", va="top", fontsize=12, color=RED, style="italic")
save(fig, "w05_old_new_bond")

# w05_timeline — five coupons and one face value, each brought back to today at 6%
fig, ax = plt.subplots(figsize=(10, 4.4)); ax.axis("off"); ax.set_xlim(-1.3, 5.8); ax.set_ylim(-3.4, 4.2)
ax.plot([0, 5.4], [0, 0], color=INK, lw=2)
for t in range(6):
    ax.plot([t, t], [-.12, .12], color=INK, lw=2)
    ax.text(t, -.45, "oggi" if t == 0 else f"anno {t}", ha="center", fontsize=11, color=INK)
for t in range(1, 6):
    ax.add_patch(FancyArrowPatch((t, 0.2), (t, 1.2), arrowstyle="-|>", mutation_scale=14, color=GOLD, lw=2))
    ax.text(t, 1.35, "€4", ha="center", fontsize=13, color=GOLD, fontweight="bold")
    ax.add_patch(FancyArrowPatch((t - .05, 1.75), (0.15, 0.25 + 0.32 * t), connectionstyle="arc3,rad=0.25",
                                 arrowstyle="-|>", mutation_scale=10, color=GOLD, lw=1, alpha=.7))
ax.add_patch(FancyArrowPatch((5, 1.9), (5, 3.2), arrowstyle="-|>", mutation_scale=14, color=RED, lw=2.5))
ax.text(5, 3.35, "€100", ha="center", fontsize=14, color=RED, fontweight="bold")
ax.add_patch(FancyArrowPatch((4.85, 3.5), (-0.05, 3.1), connectionstyle="arc3,rad=0.12",
                             arrowstyle="-|>", mutation_scale=14, color=RED, lw=1.6))
ax.text(-1.25, 2.95, "€74.73", fontsize=14, color=RED, fontweight="bold")
ax.text(-1.25, 1.0, "€16.85", fontsize=14, color=GOLD, fontweight="bold")
ax.text(2.6, -1.35, "oro: la STESSA cifra (€4) ogni anno  →  un'annualità:  4 × 4.212364 = €16.85",
        ha="center", fontsize=12, color=GOLD)
ax.text(2.6, -2.0, "rosso: UNA cifra (€100), UNA data  →  un solo sconto:  100 / 1.06⁵ = €74.73",
        ha="center", fontsize=12, color=RED)
ax.text(2.6, -2.8, "prezzo di oggi = 16.85 + 74.73 = €91.58", ha="center", fontsize=14, color=INK, fontweight="bold")
save(fig, "w05_timeline")

# w05_tangent — the triangle under the tangent: one point right, 7.72 down
def bond10(y): return sum(5 / (1 + y) ** t for t in range(1, 11)) + 100 / (1 + y) ** 10
slope = (bond10(.05 + 1e-6) - bond10(.05 - 1e-6)) / 2e-6          # about −772
fig, ax = plt.subplots(figsize=(7.4, 4.3))
ys = np.linspace(3.5, 7.5, 200)
ax.plot(ys, [bond10(v / 100) for v in ys], color=INK, lw=2.5, label="prezzo vero (curva)")
ax.plot(ys, 100 + slope * (ys / 100 - .05), color=RED, lw=2, ls="--", label="tangente in 5% (duration)")
ax.plot([5, 6], [100, 100], color=GOLD, lw=2.5); ax.plot([6, 6], [100, 100 + slope * .01], color=GOLD, lw=2.5)
ax.text(5.5, 101.2, "+1 punto di rendimento", ha="center", fontsize=11, color=GOLD, fontweight="bold")
ax.text(6.1, 96.6, "−€7.72", fontsize=11, color=RED, fontweight="bold")
ax.plot(6, bond10(.06), "o", color=INK, ms=6); ax.annotate("vero €92.64", (6, bond10(.06)), (6.5, 99), fontsize=11, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED))
ax.plot(6, 100 + slope * .01, "o", color=RED, ms=6); ax.annotate("retta €92.28", (6, 100 + slope * .01), (6.3, 86.5), fontsize=11, color=RED, arrowprops=dict(arrowstyle="-", color=RED))
ax.plot(5, 100, "o", color=GOLD, ms=9)
ax.set_xlim(4, 7.5); ax.set_ylim(84, 110)
ax.set_xlabel("rendimento y, %"); ax.set_ylabel("prezzo €"); ax.legend(frameon=False, loc="upper right")
save(fig, "w05_tangent")

# The cargo-bike study, in € thousand, q = tens of bikes a month
def C(q): return q**3 - 9*q**2 + 30*q + 20
def R(q): return 45*q - 3*q**2
def P(q): return R(q) - C(q)
Q2 = (5 + np.sqrt(105)) / 2                                         # second break-even, 7.62
q = np.linspace(0, 10, 400)
fig, ax = plt.subplots(figsize=(7.6, 4.4))
ax.axhline(0, color=MUTED, lw=1)
ax.fill_between(q, P(q), 0, where=(q > 1) & (q < Q2), color=GREEN, alpha=.12)
ax.plot(q, P(q), color=INK, lw=2.8, label="π(q) = −q³ + 6q² + 15q − 20")
pts = [(0, P(0), "π(0) = −20\n(fixed cost)", (0.15, -75)), (1, 0, "break-even q = 1", (1.2, -25)),
       (2, P(2), "inflection (2, 26)", (2.3, 8)), (5, P(5), "MAXIMUM (5, 80)", (5.3, 84)),
       (Q2, 0, "break-even q ≈ 7.62", (7.75, 10))]
for x, yv, lab, pos in pts:
    ax.plot(x, yv, "o", color=RED if "MAX" in lab else GOLD, ms=8)
    ax.annotate(lab, (x, yv), pos, fontsize=11, color=RED if "MAX" in lab else INK,
                fontweight="bold" if "MAX" in lab else "normal")
ax.text(4.4, 40, "profit", color=GREEN, fontsize=12, fontweight="bold", ha="center")
ax.set_xlabel("q, tens of cargo bikes a month"); ax.set_ylabel("€ thousand a month")
ax.set_xlim(0, 10); ax.set_ylim(-120, 105); ax.legend(frameon=False, loc="lower left")
save(fig, "w05_study_profit")

fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 3.8))
qc = np.linspace(0, 8, 300)
a1.plot(qc, C(qc), color=RED, lw=2.6); a1.plot(0, 20, "o", color=GOLD, ms=7); a1.plot(3, C(3), "o", color=GOLD, ms=7)
a1.annotate("C(0) = 20, fixed cost", (0, 20), (0.4, 95), fontsize=11, arrowprops=dict(arrowstyle="-", color=MUTED))
a1.annotate("inflection (3, 56):\nconcave, then convex", (3, C(3)), (3.4, 25), fontsize=11, arrowprops=dict(arrowstyle="-", color=MUTED))
a1.set_title("C(q) = q³ − 9q² + 30q + 20", fontsize=13, color=RED); a1.set_xlabel("q"); a1.set_ylabel("€ thousand")
a1.set_ylim(0, 230)
qr = np.linspace(0, 15, 300)
a2.plot(qr, R(qr), color=INK, lw=2.6); a2.plot(7.5, R(7.5), "o", color=RED, ms=8)
a2.plot([0, 15], [0, 0], "o", color=GOLD, ms=7)
a2.annotate("max (7.5, 168.75)", (7.5, R(7.5)), (8.3, 178), fontsize=11, color=RED, fontweight="bold")
a2.set_title("R(q) = 45q − 3q²", fontsize=13, color=INK); a2.set_xlabel("q"); a2.set_ylim(0, 200)
save(fig, "w05_study_cr")
print("week-5 extra figures written")
