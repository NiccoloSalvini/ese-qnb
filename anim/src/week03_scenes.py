"""Week 3 clips — accumulation, and the seven-point study of a function.

Render (from anim/):
    manim -qm src/week03_scenes.py RiemannFills  -o w03_riemann.mp4
    manim -qm src/week03_scenes.py StudyAFunction -o w03_study.mp4
"""
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption

# A different firm from the midterm's, same shape: a quadratic cost, a log revenue.
def marginal_cost(q): return 0.8 * q + 3          # MC(q), €/bike
def total_cost(q): return 0.4 * q ** 2 + 3 * q    # its integral, from 0


class RiemannFills(Scene):
    """Total cost is the area under marginal cost. Thinner slices, truer area."""

    def construct(self):
        ax = Axes(x_range=[0, 22, 5], y_range=[0, 22, 5], x_length=9.4, y_length=5.0,
                  axis_config={"include_numbers": True, "font_size": 24}).shift(DOWN * 0.3)
        xl = Tex("bikes $q$", font_size=28).next_to(ax, DOWN, buff=0.15)
        yl = Tex(r"marginal cost €/bike", font_size=26).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
        mc = ax.plot(marginal_cost, x_range=[0, 20], color=NAVY, stroke_width=5)
        label = MathTex(r"MC(q) = 0.8q + 3", font_size=34, color=NAVY).to_edge(UP, buff=0.3)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Create(mc), Write(label), run_time=1.8)

        exact = total_cost(20)
        readout = Text("", font_size=1)
        for n, t in ((4, 1.3), (8, 1.2), (20, 1.2), (60, 1.2)):
            # Left endpoints, in the drawing and in the number. The midpoint rule is
            # exact for a straight line, which would show no convergence at all.
            rects = ax.get_riemann_rectangles(mc, x_range=[0, 20], dx=20 / n,
                                              input_sample_type="left",
                                              color=(GOLD, RED), fill_opacity=0.55, stroke_width=0.6)
            approx = sum(marginal_cost(i * 20 / n) * 20 / n for i in range(n))
            new = VGroup(
                MathTex(rf"n = {n}", font_size=34, color=GOLD),
                MathTex(rf"\text{{area}} \approx {approx:,.0f}", font_size=34, color=GOLD),
            ).arrange(DOWN, aligned_edge=RIGHT, buff=0.2).to_corner(UR, buff=0.5)
            if n == 4:
                self.play(FadeIn(rects), FadeIn(new), run_time=t)
                bars, readout = rects, new
            else:
                self.play(Transform(bars, rects), Transform(readout, new), run_time=t)
        self.wait(0.5)
        truth = MathTex(rf"\int_0^{{20}} MC(q)\,dq = {exact:,.0f}", font_size=36, color=GREEN).to_corner(UL, buff=0.5)
        self.play(Write(truth), run_time=1.0)
        self.play(Write(caption(r"Adding up marginal cost gives total cost. That sum is the integral.")), run_time=1.4)
        self.wait(0.7)


class StudyAFunction(Scene):
    """The midterm asks for the same seven things in the same order. Each step lights up
    with the thing it names, so it is never in doubt which word belongs to which mark."""

    def construct(self):
        def f(q): return -4 * q ** 2 + 1200 * q - 60000
        ax = Axes(x_range=[0, 300, 50], y_range=[-60000, 40000, 20000], x_length=8.2, y_length=4.4,
                  axis_config={"include_numbers": True, "font_size": 19}).shift(DOWN * 0.3 + LEFT * 1.9)
        curve = ax.plot(f, x_range=[5, 295], color=NAVY, stroke_width=5)
        self.play(Create(ax), Create(curve), run_time=1.4)

        words = ["domain", "limits", "range", "sign", "maximum", "convexity", "sketch"]
        steps = VGroup(*[Tex(f"{i+1}. {w}", font_size=25, color=GREY) for i, w in enumerate(words)]) \
            .arrange(DOWN, aligned_edge=LEFT, buff=0.26).to_edge(RIGHT, buff=0.7)
        self.play(FadeIn(steps), run_time=0.8)

        def light(i, *mobs, t=1.15):
            """Turn one step gold while its own object appears on the curve."""
            self.play(steps[i].animate.set_color(GOLD).scale(1.12), *mobs, run_time=t)

        r1, r2 = 63.4, 236.6
        # 1 domain: the stretch of axis where the function lives
        dom = Line(ax.c2p(0, 0), ax.c2p(295, 0), color=GOLD, stroke_width=8)
        light(0, Create(dom))
        self.play(FadeOut(dom), steps[0].animate.set_color(GREY).scale(1 / 1.12), run_time=0.5)

        # 2 limits: where it goes at the far end
        arrow = Arrow(ax.c2p(270, -20000), ax.c2p(295, -52000), color=GOLD, buff=0, stroke_width=5)
        lim = MathTex(r"\to -\infty", font_size=28, color=GOLD).next_to(arrow, RIGHT, buff=0.1)
        light(1, GrowArrow(arrow), FadeIn(lim))

        # 3 range: the values it actually takes, on the vertical axis
        rng = Line(ax.c2p(0, -60000), ax.c2p(0, 30000), color=GOLD, stroke_width=8)
        light(2, Create(rng))

        # 4 sign: positive between the zeros
        zeros = VGroup(Dot(ax.c2p(r1, 0), color=RED, radius=0.09), Dot(ax.c2p(r2, 0), color=RED, radius=0.09))
        band = ax.get_area(curve, x_range=[r1, r2], color=GREEN, opacity=0.3)
        light(3, FadeIn(zeros), FadeIn(band), t=1.3)

        # 5 maximum: the flat tangent at the top
        top = Dot(ax.c2p(150, f(150)), color=GOLD, radius=0.11)
        flat = DashedLine(ax.c2p(85, f(150)), ax.c2p(215, f(150)), color=GOLD, stroke_width=4)
        note = MathTex(r"\pi'(q) = 0 \Rightarrow q = 150", font_size=26, color=GOLD).next_to(flat, UP, buff=0.18)
        light(4, FadeIn(top), Create(flat), Write(note), t=1.4)

        # 6 convexity: which way it bends
        second = MathTex(r"\pi''= -8 < 0 \;\Rightarrow\; \text{concave everywhere}", font_size=26, color=RED) \
            .to_corner(UL, buff=0.45)
        light(5, Write(second), t=1.2)

        # 7 sketch: everything that is now on the screen
        light(6, Indicate(curve, color=NAVY, scale_factor=1.03), t=1.0)
        self.play(Write(caption(r"Seven words, seven marks. The sketch is the last one, not the first.")), run_time=1.4)
        self.wait(0.8)
