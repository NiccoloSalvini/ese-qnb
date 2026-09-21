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
    """The midterm asks for the same seven things, in this order, every time."""

    def construct(self):
        def f(q): return -4 * q ** 2 + 1200 * q - 60000
        ax = Axes(x_range=[0, 300, 50], y_range=[-60000, 40000, 20000], x_length=9.0, y_length=4.6,
                  axis_config={"include_numbers": True, "font_size": 20}).shift(DOWN * 0.4 + LEFT * 1.6)
        curve = ax.plot(f, x_range=[5, 295], color=NAVY, stroke_width=5)
        self.play(Create(ax), Create(curve), run_time=1.5)

        steps = VGroup(*[Tex(s, font_size=26) for s in (
            r"1. domain", r"2. zeros", r"3. sign", r"4. stationary point",
            r"5. maximum", r"6. shape", r"7. sketch")]
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).to_edge(RIGHT, buff=0.5)
        self.play(FadeIn(steps[0]), run_time=0.5)

        r1, r2 = 63.4, 236.6
        zeros = VGroup(Dot(ax.c2p(r1, 0), color=RED, radius=0.08), Dot(ax.c2p(r2, 0), color=RED, radius=0.08))
        self.play(FadeIn(steps[1]), FadeIn(zeros), run_time=1.0)

        band = ax.get_area(curve, x_range=[r1, r2], color=GREEN, opacity=0.25)
        self.play(FadeIn(steps[2]), FadeIn(band), run_time=1.1)

        top = Dot(ax.c2p(150, f(150)), color=GOLD, radius=0.1)
        flat = DashedLine(ax.c2p(80, f(150)), ax.c2p(220, f(150)), color=GOLD, stroke_width=3)
        self.play(FadeIn(steps[3]), FadeIn(top), Create(flat), run_time=1.2)

        note = MathTex(r"\pi'(q) = 0 \Rightarrow q = 150", font_size=30, color=GOLD).next_to(ax, UP, buff=0.15)
        self.play(FadeIn(steps[4]), Write(note), run_time=1.2)

        second = MathTex(r"\pi''(q) = -8 < 0 \;\Rightarrow\; \text{a maximum}", font_size=28, color=RED).next_to(note, DOWN, buff=0.12)
        self.play(FadeIn(steps[5]), Write(second), run_time=1.3)
        self.play(FadeIn(steps[6]), run_time=0.6)
        self.play(Write(caption(r"Seven steps, always the same order. The sketch is the last one, not the first.")), run_time=1.4)
        self.wait(0.6)
