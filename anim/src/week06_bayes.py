"""Week 6 clip — Bayes as the faulty column: 1,000 batteries, the good ones vanish, the shares turn.

Render (from anim/):
    manim -qm src/week06_bayes.py BayesColumn -o w06_bayes.mp4
"""
from manim import *
from common import NAVY, RED, GREY, GOLD, caption

N_VOLTA, N_AMPERE = 700, 300          # the founder's prior: 70 / 30
F_VOLTA, F_AMPERE = 14, 15            # 2% of 700, 5% of 300
W = 9.0                               # width of the 1,000-battery bar, in scene units


def bar(n, color, x_left, y, h=1.1, fill=0.85):
    w = W * n / 1000
    r = Rectangle(width=w, height=h, color=color, fill_color=color, fill_opacity=fill, stroke_width=2)
    return r.move_to([x_left + w / 2, y, 0])


class BayesColumn(Scene):
    """Prior as a 70/30 bar; the faulty slices appear; the good batteries fade; the two slices become 48/52."""

    def construct(self):
        x0 = -W / 2
        y_bar = 0.9
        title = Tex("1{,}000 batteries received this quarter", font_size=30, color=NAVY).to_edge(UP, buff=0.4)
        volta = bar(N_VOLTA, NAVY, x0, y_bar)
        ampere = bar(N_AMPERE, GOLD, x0 + W * N_VOLTA / 1000, y_bar)
        lab_v = Tex("Volta  700", font_size=30, color=WHITE).move_to(volta)
        lab_a = Tex("Ampere  300", font_size=30, color=WHITE).move_to(ampere)
        prior = Tex(r"the founder's prior: ``probably Volta, they send 70\%''", font_size=28, color=GREY)
        prior.next_to(volta, DOWN, buff=0.35).align_to(volta, LEFT)

        self.play(Write(title), run_time=1.0)
        self.play(GrowFromEdge(volta, LEFT), FadeIn(lab_v), run_time=1.2)
        self.play(GrowFromEdge(ampere, LEFT), FadeIn(lab_a), run_time=0.8)
        self.play(Write(prior), run_time=1.2)
        self.wait(1.2)

        # the faulty slices: 2% of Volta, 5% of Ampere, drawn at the right end of each bar
        def slice_of(parent, n, n_tot):
            w = parent.width * n / n_tot
            s = Rectangle(width=w, height=parent.height, color=RED, fill_color=RED, fill_opacity=1, stroke_width=0)
            return s.align_to(parent, RIGHT).align_to(parent, UP)

        fv, fa = slice_of(volta, F_VOLTA, N_VOLTA), slice_of(ampere, F_AMPERE, N_AMPERE)
        tv = Tex(r"2\% faulty = 14", font_size=26, color=RED).next_to(fv, UP, buff=0.15)
        ta = Tex(r"5\% faulty = 15", font_size=26, color=RED).next_to(fa, UP, buff=0.15)
        self.play(FadeIn(fv), Write(tv), run_time=1.0)
        self.play(FadeIn(fa), Write(ta), run_time=1.0)
        self.wait(1.3)

        # the evidence: the battery on the bench is faulty. The good ones no longer matter.
        evidence = Tex(r"the evidence: the battery on the bench is \textbf{faulty}", font_size=28, color=RED)
        evidence.next_to(prior, DOWN, buff=0.3).align_to(prior, LEFT)
        self.play(Write(evidence), run_time=1.2)
        self.wait(0.6)
        self.play(volta.animate.set_opacity(0.12), ampere.animate.set_opacity(0.12),
                  lab_v.animate.set_opacity(0.15), lab_a.animate.set_opacity(0.15), run_time=1.2)
        self.wait(0.8)

        # only the faulty column counts: the two slices come together and grow to one bar of 29
        y2 = -1.9
        total_w = 7.0
        new_v = Rectangle(width=total_w * F_VOLTA / 29, height=1.0, color=NAVY, fill_color=NAVY, fill_opacity=0.9, stroke_width=2)
        new_a = Rectangle(width=total_w * F_AMPERE / 29, height=1.0, color=GOLD, fill_color=GOLD, fill_opacity=0.9, stroke_width=2)
        new_v.move_to([-total_w / 2 + new_v.width / 2, y2, 0])
        new_a.next_to(new_v, RIGHT, buff=0)
        col_title = Tex("the 29 faulty batteries, by supplier", font_size=28, color=RED).next_to(new_v, UP, buff=0.25).set_x(0)
        self.play(FadeOut(evidence), FadeOut(prior), FadeOut(tv), FadeOut(ta), run_time=0.5)
        self.play(ReplacementTransform(fv, new_v), ReplacementTransform(fa, new_a), FadeIn(col_title), run_time=1.8)
        sv = Tex(r"Volta  14/29 = .48", font_size=30, color=WHITE).move_to(new_v)
        sa = Tex(r"Ampere  15/29 = .52", font_size=30, color=WHITE).move_to(new_a)
        self.play(FadeIn(sv), FadeIn(sa), run_time=0.8)
        self.wait(1.0)

        arrow = Tex(r"prior $.70 / .30 \;\longrightarrow\;$ after the evidence $.48 / .52$", font_size=32, color=GOLD)
        arrow.next_to(new_v, DOWN, buff=0.35).set_x(0)
        self.play(Write(arrow), run_time=1.3)
        self.wait(0.8)
        self.play(Write(caption("Bayes is the faulty column, read in shares: the evidence moved Ampere from .30 to .52.")), run_time=1.5)
        self.wait(2.5)
