"""Week 7 clip — mean and spread: the distances cancel, their squares do not.

Render (from anim/):
    manim -qm src/week07_spread.py MeanAndSpread -o w07_spread.mp4
"""
import math

from manim import *
from common import NAVY, RED, GREY, GOLD, caption

RETURNS = [4, 7, 3, 6, 5]                      # five weeks at Arno Bikes
MEAN = sum(RETURNS) / len(RETURNS)             # 5
DEV = [r - MEAN for r in RETURNS]              # -1, +2, -2, +1, 0
SQ = [d * d for d in DEV]                      # 1, 4, 4, 1, 0
SS = sum(SQ)                                   # 10
VAR = SS / (len(RETURNS) - 1)                  # 2.5
SD = math.sqrt(VAR)                            # 1.58


def signed(d):
    d = int(d)
    return "$0$" if d == 0 else (f"$+{d}$" if d > 0 else f"${d}$")


class MeanAndSpread(Scene):
    """Bars, the mean line, signed distances that sum to zero, squares that do not, and the ±s band."""

    def construct(self):
        ax = Axes(x_range=[0, 6, 1], y_range=[0, 8, 2], x_length=6.2, y_length=4.0,
                  axis_config={"include_numbers": False, "font_size": 22},
                  x_axis_config={"include_numbers": True, "numbers_to_include": [1, 2, 3, 4, 5]},
                  y_axis_config={"include_numbers": True}).move_to(LEFT * 3.3 + DOWN * 0.15)
        ux, uy = ax.x_axis.unit_size, ax.y_axis.unit_size
        xl = Tex("week", font_size=24).next_to(ax.x_axis, DOWN, buff=0.35)
        yl = Tex(r"return (\%)", font_size=24).rotate(90 * DEGREES).next_to(ax.y_axis, LEFT, buff=0.3)
        title = Tex("Arno Bikes, five weekly returns: 4, 7, 3, 6, 5", font_size=30, color=NAVY).to_edge(UP, buff=0.3)

        # (1) five NAVY bars rise
        bars = VGroup(*[Rectangle(width=ux * 0.6, height=uy * r, color=NAVY, fill_color=NAVY, fill_opacity=0.6,
                                  stroke_width=2).move_to(ax.c2p(k + 1, 0), aligned_edge=DOWN)
                        for k, r in enumerate(RETURNS)])
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=1.0)
        self.wait(1.2)
        self.play(LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.12), run_time=1.1)

        # (2) the GOLD mean line slides up from 0 and settles at 5
        m = ValueTracker(0.0)
        mline = always_redraw(lambda: Line(ax.c2p(0, m.get_value()), ax.c2p(6, m.get_value()),
                                           color=GOLD, stroke_width=5))
        self.add(mline)
        self.play(m.animate.set_value(MEAN), run_time=1.1, rate_func=smooth)
        mean_line = Line(ax.c2p(0, MEAN), ax.c2p(6, MEAN), color=GOLD, stroke_width=5)
        mlab = Tex("mean = 25 / 5 = 5", font_size=24, color=GOLD).next_to(mean_line.get_end(), RIGHT, buff=0.1)
        self.remove(mline)
        self.add(mean_line)
        self.play(Write(mlab), run_time=0.6)
        self.wait(1.2)

        # (3) arrows from bar tops to the mean line, signed distances
        arrows, dlabels = VGroup(), VGroup()
        for k, (r, d) in enumerate(zip(RETURNS, DEV)):
            x = k + 1
            if d == 0:
                a = Dot(ax.c2p(x, MEAN), radius=0.07, color=RED)
            else:
                a = Arrow(ax.c2p(x, r), ax.c2p(x, MEAN), buff=0, color=RED, stroke_width=4,
                          max_tip_length_to_length_ratio=0.3)
            arrows.add(a)
            dlabels.add(Tex(signed(d), font_size=26, color=RED).next_to(a, RIGHT, buff=0.05))
        self.play(LaggedStart(*[GrowArrow(a) if isinstance(a, Arrow) else FadeIn(a) for a in arrows], lag_ratio=0.1),
                  FadeIn(dlabels), run_time=1.0)
        self.wait(0.4)

        rx = 4.0                                   # the right-hand column
        sum1 = Tex("$-1$", r"$\;+\,2$", r"$\;-\,2$", r"$\;+\,1$", r"$\;+\,0$", r"$\;=\;0$", font_size=34).move_to([rx, 2.3, 0])
        self.play(*[ReplacementTransform(dlabels[i], sum1[i]) for i in range(5)], run_time=1.1)
        cancel = Tex("the distances cancel", font_size=26, color=GREY).next_to(sum1, DOWN, buff=0.2)
        self.play(Write(sum1[5]), FadeIn(cancel), run_time=0.6)
        self.wait(1.2)

        # (4) the arrows become squares of side = distance, area labels
        squares, slabels = VGroup(), VGroup()
        for k, (r, d) in enumerate(zip(RETURNS, DEV)):
            x = k + 1
            side = max(abs(d) * uy, 0.04)
            lo, hi = min(r, MEAN), max(r, MEAN)
            sq = Square(side_length=side, color=RED, fill_color=RED, fill_opacity=0.35, stroke_width=2.5)
            sq.move_to(ax.c2p(x, (lo + hi) / 2))
            squares.add(sq)
            slabels.add(Tex(f"${int(d * d)}$", font_size=26, color=RED).move_to(sq.get_center())
                        if d != 0 else Tex("$0$", font_size=26, color=RED).next_to(sq, RIGHT, buff=0.05))
        self.play(*[ReplacementTransform(arrows[i], squares[i]) for i in range(5)], run_time=1.1)
        self.play(FadeIn(slabels), run_time=0.4)
        self.wait(0.3)
        sum2 = Tex("$1$", r"$\;+\,4$", r"$\;+\,4$", r"$\;+\,1$", r"$\;+\,0$", r"$\;=\;10$", font_size=34).move_to([rx, 1.1, 0])
        self.play(*[ReplacementTransform(slabels[i].copy(), sum2[i]) for i in range(5)], run_time=1.1)
        self.play(Write(sum2[5]), run_time=0.4)
        self.wait(0.6)

        # (5) divide by n - 1, take the root, shade the band
        divide = Tex(r"$\div\,(5-1) = 2.5$", font_size=34).next_to(sum2, DOWN, buff=0.35).align_to(sum2, RIGHT)
        sd = Tex(r"$s = \sqrt{2.5} = 1.58$", font_size=36, color=RED).next_to(divide, DOWN, buff=0.35).align_to(sum2, RIGHT)
        self.play(Write(divide), run_time=0.7)
        self.wait(0.3)
        self.play(Write(sd), run_time=0.7)
        self.wait(0.3)
        band = Rectangle(width=ux * 6, height=uy * 2 * SD, color=RED, fill_color=RED, fill_opacity=0.25,
                         stroke_width=0).move_to(ax.c2p(3, MEAN))
        self.play(FadeIn(band), run_time=0.9)
        self.play(Write(caption(r"The distances cancel; their squares do not.\\ "
                                r"Divide by $n-1$: the last distance is never free.", size=28)), run_time=1.6)
        self.wait(2.5)
