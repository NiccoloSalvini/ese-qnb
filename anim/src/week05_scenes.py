"""Week 5 clips — duration is the tangent, convexity is the gap it misses.

Render (from anim/):
    manim -qm src/week05_scenes.py DurationIsTheTangent -o w05_duration.mp4
    manim -qm src/week05_scenes.py ConvexityIsTheGap    -o w05_convexity.mp4
"""
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption, line_through

FACE, COUPON, YEARS, Y0 = 100.0, 0.05, 10, 0.05


def price(y):
    """Plain annual-coupon bond: coupons discounted, plus the face value."""
    return sum(COUPON * FACE / (1 + y) ** t for t in range(1, YEARS + 1)) + FACE / (1 + y) ** YEARS


def dprice(y, h=1e-5):
    return (price(y + h) - price(y - h)) / (2 * h)


def bond_axes():
    ax = Axes(x_range=[0.01, 0.11, 0.02], y_range=[60, 160, 20], x_length=9.2, y_length=4.4,
              axis_config={"include_numbers": True, "font_size": 22},
              x_axis_config={"decimal_number_config": {"num_decimal_places": 2}}).shift(UP * 0.1)
    xl = Tex("yield $y$", font_size=28).next_to(ax, DOWN, buff=0.15)
    yl = Tex("price €", font_size=28).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
    return ax, xl, yl


class DurationIsTheTangent(Scene):
    """Modified duration is a slope: the straight-line guess at how the price moves."""

    def construct(self):
        ax, xl, yl = bond_axes()
        curve = ax.plot(price, x_range=[0.011, 0.109], color=NAVY, stroke_width=5)
        title = Tex(r"10-year bond, 5\% coupon, priced at par", font_size=32, color=NAVY).to_edge(UP, buff=0.3)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=1.6)
        self.play(Create(curve), run_time=1.3)

        p0, slope = price(Y0), dprice(Y0)
        at_par = Dot(ax.c2p(Y0, p0), color=GOLD, radius=0.1)
        self.play(FadeIn(at_par), run_time=0.5)

        tangent = line_through(ax, Y0, p0, slope, 0.045, color=RED, stroke_width=4)
        modified = -slope / p0
        readout = VGroup(
            MathTex(r"\frac{dP}{dy} = " + f"{slope:,.0f}", font_size=32, color=RED),
            MathTex(r"D_{\text{mod}} = -\frac{1}{P}\frac{dP}{dy} = " + f"{modified:.2f}", font_size=32, color=GOLD),
        ).arrange(DOWN, aligned_edge=RIGHT, buff=0.2).to_corner(UR, buff=0.45)
        self.play(Create(tangent), Write(readout), run_time=1.8)
        self.wait(0.5)

        rule = MathTex(r"+1\% \text{ in } y \;\Rightarrow\; " + f"{-modified:.1f}" + r"\% \text{ in price}",
                       font_size=32, color=WHITE).next_to(readout, DOWN, aligned_edge=RIGHT, buff=0.3)
        self.play(Write(rule), run_time=1.2)
        self.play(Write(caption(r"Duration is the slope of this curve, written as a percentage.")), run_time=1.4)
        self.wait(0.8)


class ConvexityIsTheGap(Scene):
    """The straight-line guess is wrong, and wrong in the holder's favour."""

    def construct(self):
        ax, xl, yl = bond_axes()
        curve = ax.plot(price, x_range=[0.011, 0.109], color=NAVY, stroke_width=5)
        p0, slope = price(Y0), dprice(Y0)
        tangent = line_through(ax, Y0, p0, slope, 0.045, color=RED, stroke_width=4)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Create(curve), Create(tangent), run_time=2.0)

        y = ValueTracker(Y0 + 0.004)
        on_curve = always_redraw(lambda: Dot(ax.c2p(y.get_value(), price(y.get_value())), color=NAVY, radius=0.08))
        on_line = always_redraw(lambda: Dot(ax.c2p(y.get_value(), p0 + slope * (y.get_value() - Y0)), color=RED, radius=0.08))
        gap = always_redraw(lambda: Line(
            ax.c2p(y.get_value(), p0 + slope * (y.get_value() - Y0)),
            ax.c2p(y.get_value(), price(y.get_value())), color=GOLD, stroke_width=6))
        readout = always_redraw(lambda: MathTex(
            r"\text{curve} - \text{tangent} = " + f"{price(y.get_value()) - (p0 + slope * (y.get_value() - Y0)):.2f}",
            font_size=34, color=GOLD).to_corner(UR, buff=0.45))
        self.add(on_curve, on_line, gap, readout)
        self.wait(0.6)
        self.play(y.animate.set_value(0.10), run_time=2.6, rate_func=linear)
        self.wait(0.4)
        self.play(y.animate.set_value(0.015), run_time=3.2, rate_func=linear)
        self.wait(0.4)
        note = Tex(r"the curve is always \emph{above} the tangent", font_size=30, color=GOLD).to_corner(UL, buff=0.4)
        self.play(Write(note), run_time=1.0)
        self.play(Write(caption(r"Convexity is that gap: duration alone understates the gain and overstates the loss.")), run_time=1.5)
        self.wait(0.6)
