"""Week 2 clips — the derivative, seen before it is defined.

Render (from anim/):
    manim -qm src/week02_scenes.py SecantToTangent -o w02_secant.mp4
    manim -qm src/week02_scenes.py TangentSlides   -o w02_tangent.mp4
"""
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption, line_through, profit, profit_prime


def profit_axes():
    ax = Axes(x_range=[0, 300, 50], y_range=[-60000, 40000, 20000],
              x_length=10.5, y_length=5.2,
              axis_config={"include_numbers": True, "font_size": 22},
              y_axis_config={"decimal_number_config": {"num_decimal_places": 0, "group_with_commas": True}})
    # The x-axis sits at y = 0, in the middle of the frame, so its label cannot
    # live on the axis: it would land on top of the tick numbers.
    xl = Tex("bikes $q$", font_size=28).next_to(ax, DOWN, buff=0.15)
    yl = Tex(r"profit €", font_size=28).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
    return ax, xl, yl


class SecantToTangent(Scene):
    """Average rate of change over an interval becomes the slope at a point."""

    def construct(self):
        ax, xl, yl = profit_axes()
        ax.shift(DOWN * 0.35)
        curve = ax.plot(profit, x_range=[5, 295], color=NAVY, stroke_width=5)
        title = MathTex(r"\pi(q) = -4q^2 + 1200q - 60{,}000", font_size=34, color=NAVY).to_edge(UP, buff=0.3)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=1.6)
        self.play(Create(curve), run_time=1.2)

        a = 80
        A = Dot(ax.c2p(a, profit(a)), color=GOLD, radius=0.09)
        self.play(FadeIn(A), run_time=0.4)

        h = ValueTracker(150)
        secant = always_redraw(lambda: line_through(
            ax, a, profit(a),
            (profit(a + h.get_value()) - profit(a)) / h.get_value(),
            110, color=RED, stroke_width=4))
        B = always_redraw(lambda: Dot(ax.c2p(a + h.get_value(), profit(a + h.get_value())), color=RED, radius=0.08))
        slope_txt = always_redraw(lambda: MathTex(
            r"\frac{\Delta \pi}{\Delta q} = " +
            f"{(profit(a + h.get_value()) - profit(a)) / h.get_value():,.0f}",
            font_size=34, color=RED).to_corner(UR, buff=0.5))
        self.add(secant, B, slope_txt)
        self.wait(0.8)
        self.play(h.animate.set_value(1), run_time=5, rate_func=smooth)
        self.wait(0.4)

        exact = MathTex(r"\pi'(80) = 560", font_size=36, color=GOLD).to_corner(UL, buff=0.5)
        self.play(Write(exact), run_time=0.8)
        self.play(Write(caption(r"Two points become one. The average becomes the slope \emph{at} a point.")), run_time=1.4)
        self.wait(0.8)


class TangentSlides(Scene):
    """The tangent walks the curve; its slope is positive, then zero, then negative."""

    def construct(self):
        ax, xl, yl = profit_axes()
        ax.shift(DOWN * 0.35)
        curve = ax.plot(profit, x_range=[5, 295], color=NAVY, stroke_width=5)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Create(curve), run_time=1.6)

        q = ValueTracker(40)
        tangent = always_redraw(lambda: line_through(
            ax, q.get_value(), profit(q.get_value()), profit_prime(q.get_value()),
            70, color=RED, stroke_width=5))
        dot = always_redraw(lambda: Dot(ax.c2p(q.get_value(), profit(q.get_value())), color=RED, radius=0.09))
        readout = always_redraw(lambda: MathTex(
            r"\pi'(q) = " + f"{profit_prime(q.get_value()):,.0f}",
            font_size=38,
            color=GREEN if profit_prime(q.get_value()) > 20 else (GOLD if abs(profit_prime(q.get_value())) <= 20 else RED),
        ).to_corner(UR, buff=0.5))
        meaning = always_redraw(lambda: Tex(
            "one more bike helps" if profit_prime(q.get_value()) > 20
            else ("one more bike hurts" if profit_prime(q.get_value()) < -20 else "one more bike changes nothing"),
            font_size=30, color=WHITE).next_to(readout, DOWN, aligned_edge=RIGHT, buff=0.25))
        self.add(tangent, dot, readout, meaning)
        self.wait(0.6)
        self.play(q.animate.set_value(150), run_time=3.2, rate_func=linear)
        flat = DashedLine(ax.c2p(60, profit(150)), ax.c2p(240, profit(150)), color=GOLD, stroke_width=3)
        self.play(Create(flat), run_time=0.7)
        self.wait(0.7)
        self.play(q.animate.set_value(260), run_time=3.0, rate_func=linear)
        self.play(Write(caption(r"The top of the hill is where the tangent is flat: $\pi'(q) = 0$.")), run_time=1.4)
        self.wait(0.7)


class AverageCostFalls(Scene):
    """Average cost is the variable cost plus the fixed cost shared out.
    Slide the quantity and watch the sharing do all the work."""

    def construct(self):
        FIXED, VAR = 60_000, 400
        ac = lambda q: FIXED / q + VAR

        ax = Axes(x_range=[0, 320, 50], y_range=[0, 2600, 500], x_length=9.0, y_length=4.6,
                  axis_config={"include_numbers": True, "font_size": 22}).shift(DOWN * 0.25 + LEFT * 0.8)
        xl = Tex("bikes per month $q$", font_size=26).next_to(ax, DOWN, buff=0.15)
        yl = Tex(r"average cost €/bike", font_size=26).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
        title = MathTex(r"AC(q) = \frac{60{,}000 + 400q}{q} = \underbrace{\frac{60{,}000}{q}}_{\text{shared out}} + \underbrace{400}_{\text{per bike}}",
                        font_size=30, color=NAVY).to_edge(UP, buff=0.25)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=2.2)

        curve = ax.plot(ac, x_range=[24, 318], color=NAVY, stroke_width=5)
        floor = DashedLine(ax.c2p(0, VAR), ax.c2p(320, VAR), color=RED, stroke_width=3)
        floor_lab = Tex(r"€400 — the variable cost, which never goes away", font_size=24, color=RED).next_to(ax.c2p(320, VAR), UP + LEFT, buff=0.15)
        self.play(Create(curve), run_time=1.4)
        self.play(Create(floor), FadeIn(floor_lab), run_time=1.0)

        q = ValueTracker(28)
        dot = always_redraw(lambda: Dot(ax.c2p(q.get_value(), ac(q.get_value())), color=GOLD, radius=0.09))
        share = always_redraw(lambda: Line(ax.c2p(q.get_value(), VAR), ax.c2p(q.get_value(), ac(q.get_value())),
                                           color=GOLD, stroke_width=7))
        readout = always_redraw(lambda: VGroup(
            MathTex(rf"q = {q.get_value():,.0f}", font_size=30, color=WHITE),
            MathTex(r"\text{fixed, per bike} = " + f"{FIXED / q.get_value():,.0f}", font_size=30, color=GOLD),
            MathTex(r"AC = " + f"{ac(q.get_value()):,.0f}", font_size=32, color=NAVY),
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.18).to_corner(UR, buff=0.4))
        self.add(dot, share, readout)
        self.wait(0.7)
        self.play(q.animate.set_value(300), run_time=5.0, rate_func=smooth)
        self.wait(0.5)
        self.play(Write(caption(r"The gold bar is the rent, split between the bikes. More bikes, thinner slice.")), run_time=1.5)
        self.wait(0.8)
