"""Week 4 clips — where e comes from, and what an IRR is.

Render (from anim/):
    manim -qm src/week04_scenes.py CompoundingToE -o w04_compounding.mp4
    manim -qm src/week04_scenes.py NpvCrossesZero -o w04_npv.mp4
"""
import numpy as np
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption

RATE = 0.12
PRINCIPAL = 1000


class CompoundingToE(Scene):
    """€1,000 at 12% for one year, compounded n times. The gain stops growing."""

    def construct(self):
        title = MathTex(r"1000\left(1 + \frac{0.12}{n}\right)^{n}", font_size=40, color=NAVY).to_edge(UP, buff=0.35)
        self.play(Write(title), run_time=1.0)

        rows = [("once a year", 1), ("every 6 months", 2), ("every quarter", 4),
                ("every month", 12), ("every week", 52), ("every day", 365)]
        table = VGroup()
        for label, n in rows:
            value = PRINCIPAL * (1 + RATE / n) ** n
            table.add(VGroup(
                Tex(label, font_size=30, color=GREY),
                MathTex(rf"n = {n}", font_size=30, color=GREY),
                MathTex(rf"\text{{€}}{value:,.2f}", font_size=32, color=NAVY),
            ).arrange(RIGHT, buff=0.7))
        for row in table:
            row[0].align_to(table[0][0], LEFT)
            row[2].align_to(table[0][2], LEFT)
        table.arrange(DOWN, aligned_edge=LEFT, buff=0.34).next_to(title, DOWN, buff=0.55).shift(LEFT * 1.1)

        for row in table:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.75)

        limit_value = PRINCIPAL * np.exp(RATE)
        brace = Brace(VGroup(*[r[2] for r in table]), RIGHT, color=GOLD)
        limit = VGroup(
            MathTex(r"n \to \infty", font_size=34, color=GOLD),
            MathTex(rf"1000\,e^{{0.12}} = {limit_value:,.2f}", font_size=34, color=GOLD),
        ).arrange(DOWN, buff=0.2).next_to(brace, RIGHT, buff=0.3)
        self.play(GrowFromCenter(brace), Write(limit), run_time=1.6)
        self.wait(0.6)
        self.play(Write(caption(r"Compound more often and the gain stops growing. The ceiling is $e$.")), run_time=1.4)
        self.wait(0.7)


# €k: one outlay, then four years of cash. Module level, not a method: manim
# caches the plotted function, and pickling a bound method drags the whole Scene
# (locks included) along with it.
FLOWS = [-2400, 700, 800, 900, 1000]


def npv(r):
    return sum(cf / (1 + r) ** t for t, cf in enumerate(FLOWS))


def irr(lo=0.0, hi=0.5):
    for _ in range(80):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if npv(mid) > 0 else (lo, mid)
    return (lo + hi) / 2


class NpvCrossesZero(Scene):
    """A project's NPV falls as the discount rate rises; the crossing is the IRR."""

    def construct(self):
        ax = Axes(x_range=[0, 0.30, 0.05], y_range=[-500, 1200, 500], x_length=9.0, y_length=4.8,
                  axis_config={"include_numbers": True, "font_size": 22},
                  x_axis_config={"decimal_number_config": {"num_decimal_places": 2}}).shift(DOWN * 0.35)
        xl = Tex("discount rate $r$", font_size=28).next_to(ax, DOWN, buff=0.15)
        yl = Tex(r"NPV (€k)", font_size=28).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
        flows = MathTex(r"-2400,\; 700,\; 800,\; 900,\; 1000", font_size=32, color=GREY).to_edge(UP, buff=0.3)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(flows), run_time=1.6)

        curve = ax.plot(npv, x_range=[0.001, 0.30], color=NAVY, stroke_width=5)
        self.play(Create(curve), run_time=1.4)

        r = ValueTracker(0.02)
        dot = always_redraw(lambda: Dot(ax.c2p(r.get_value(), npv(r.get_value())),
                                        color=GREEN if npv(r.get_value()) > 0 else RED, radius=0.09))
        drop = always_redraw(lambda: DashedLine(ax.c2p(r.get_value(), 0),
                                                ax.c2p(r.get_value(), npv(r.get_value())),
                                                color=GREY, stroke_width=2))
        readout = always_redraw(lambda: VGroup(
            MathTex(rf"r = {r.get_value():.0%}".replace("%", r"\%"), font_size=34, color=GOLD),
            MathTex(rf"\text{{NPV}} = {npv(r.get_value()):,.0f}", font_size=34,
                    color=GREEN if npv(r.get_value()) > 0 else RED),
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.18).to_corner(UR, buff=0.45))
        self.add(dot, drop, readout)
        self.wait(0.5)

        rate = irr()
        self.play(r.animate.set_value(rate), run_time=3.0, rate_func=linear)
        mark = MathTex(rf"\text{{IRR}} = {rate:.1%}".replace("%", r"\%"), font_size=36, color=GOLD).next_to(ax.c2p(rate, 0), UP + RIGHT, buff=0.25)
        self.play(Write(mark), run_time=0.9)
        self.play(r.animate.set_value(0.27), run_time=2.0, rate_func=linear)
        self.play(Write(caption(r"Accept while NPV is positive. The rate where it crosses zero is the IRR.")), run_time=1.4)
        self.wait(0.6)
