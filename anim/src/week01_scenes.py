"""Week 1 manim clips.

Render (from anim/):
    manim -qm src/week01_scenes.py RevenueRectangle   -o w01_parabola.mp4
    manim -qm src/week01_scenes.py LinearVsExponential -o w01_growth.mp4
Outputs land in anim/media/videos/...; copy the mp4s to anim/out/.
Use -ql for a quick preview, -qh for the projector.
"""
from manim import *

NAVY, RED, GREY = "#2471a3", "#c0392b", "#7f8c8d"


class RevenueRectangle(Scene):
    """Demand line p(q) = 1600 − 4q; the rectangle p·q sweeps out the revenue parabola."""

    def construct(self):
        ax = Axes(x_range=[0, 420, 100], y_range=[0, 1800, 400], x_length=6.2, y_length=4.2,
                  axis_config={"include_numbers": True, "font_size": 24}).to_edge(LEFT, buff=0.6)
        xl = ax.get_x_axis_label(Tex("bikes $q$", font_size=28), edge=DOWN, direction=DOWN)
        yl = ax.get_y_axis_label(Tex("price €", font_size=28).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.4)

        ax2 = Axes(x_range=[0, 420, 100], y_range=[0, 180000, 40000], x_length=6.2, y_length=4.2,
                   axis_config={"include_numbers": True, "font_size": 24}).to_edge(RIGHT, buff=0.6)
        xl2 = ax2.get_x_axis_label(Tex("bikes $q$", font_size=28), edge=DOWN, direction=DOWN)
        yl2 = ax2.get_y_axis_label(Tex("revenue €", font_size=28).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.4)

        demand = ax.plot(lambda q: 1600 - 4 * q, x_range=[0, 400], color=GREY)
        dlabel = MathTex(r"p(q) = 1600 - 4q", font_size=32, color=GREY).next_to(ax, UP)
        rlabel = MathTex(r"R(q) = p(q)\cdot q", font_size=32, color=NAVY).next_to(ax2, UP)

        self.play(Create(ax), Create(ax2), Write(xl), Write(yl), Write(xl2), Write(yl2))
        self.play(Create(demand), Write(dlabel), Write(rlabel))

        q = ValueTracker(20)
        rect = always_redraw(lambda: Polygon(
            ax.c2p(0, 0), ax.c2p(q.get_value(), 0),
            ax.c2p(q.get_value(), 1600 - 4 * q.get_value()), ax.c2p(0, 1600 - 4 * q.get_value()),
            color=NAVY, fill_color=NAVY, fill_opacity=0.3))
        dot = always_redraw(lambda: Dot(ax2.c2p(q.get_value(), (1600 - 4 * q.get_value()) * q.get_value()), color=NAVY))
        trace = TracedPath(dot.get_center, stroke_color=NAVY, stroke_width=4)
        area_txt = always_redraw(lambda: Tex(
            f"area = {(1600 - 4 * q.get_value()) * q.get_value():,.0f}", font_size=28, color=NAVY
        ).next_to(rect, UP, buff=0.1))

        self.add(rect, dot, trace, area_txt)
        self.play(q.animate.set_value(200), run_time=5, rate_func=linear)
        self.wait(0.6)
        peak = Tex("wider, but shorter", font_size=26, color=RED).next_to(ax2.c2p(200, 160000), UP)
        self.play(FadeIn(peak))
        self.play(q.animate.set_value(400), run_time=5, rate_func=linear)
        self.wait(0.5)
        caption = Tex("Revenue is the area of a rectangle whose sides pull in opposite directions.",
                      font_size=30).to_edge(DOWN, buff=0.3)
        self.play(Write(caption))
        self.wait(2)


class LinearVsExponential(Scene):
    """Same start (€1.2M), same first-year gain; linear adds €144k a year, exponential multiplies by 1.12."""

    def construct(self):
        ax = Axes(x_range=[0, 12, 2], y_range=[0, 5, 1], x_length=9, y_length=5,
                  axis_config={"include_numbers": True, "font_size": 26}).shift(DOWN * 0.3)
        xl = ax.get_x_axis_label(Tex("years", font_size=28), edge=DOWN, direction=DOWN)
        yl = ax.get_y_axis_label(Tex("revenue (€M)", font_size=28).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.4)
        self.play(Create(ax), Write(xl), Write(yl))

        t = ValueTracker(0)
        lin = always_redraw(lambda: ax.plot(lambda x: 1.2 + 0.144 * x, x_range=[0, max(t.get_value(), 1e-3)], color=GREY, stroke_width=5))
        exp = always_redraw(lambda: ax.plot(lambda x: 1.2 * 1.12 ** x, x_range=[0, max(t.get_value(), 1e-3)], color=NAVY, stroke_width=5))
        l1 = Tex("linear: +€144k every year", font_size=28, color=GREY).to_corner(UL, buff=0.5)
        l2 = Tex(r"exponential: $\times 1.12$ every year", font_size=28, color=NAVY).next_to(l1, DOWN, aligned_edge=LEFT)
        self.play(Write(l1), Write(l2))
        self.add(lin, exp)

        double = DashedLine(ax.c2p(0, 2.4), ax.c2p(12, 2.4), color=WHITE)
        dlab = Tex("double: €2.4M", font_size=26).next_to(double, UP, aligned_edge=LEFT)
        self.play(Create(double), Write(dlab))

        self.play(t.animate.set_value(12), run_time=6, rate_func=linear)

        t_exp = np.log(2) / np.log(1.12)
        t_lin = 1.2 / 0.144
        d1 = Dot(ax.c2p(t_exp, 2.4), color=NAVY)
        d2 = Dot(ax.c2p(t_lin, 2.4), color=GREY)
        n1 = MathTex(r"t = \tfrac{\ln 2}{\ln 1.12} \approx 6.1", font_size=32, color=NAVY).next_to(d1, UP + LEFT, buff=0.3)
        n2 = MathTex(r"t = \tfrac{1.2}{0.144} \approx 8.3", font_size=32, color=GREY).next_to(d2, DOWN + RIGHT, buff=0.3)
        self.play(FadeIn(d1), Write(n1))
        self.play(FadeIn(d2), Write(n2))
        gap = Tex("Linear adds the same amount; exponential adds the same percentage.",
                  font_size=30).to_edge(DOWN, buff=0.2)
        self.play(Write(gap))
        self.wait(2)
