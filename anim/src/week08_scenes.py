"""Week 8 clips — from one sample to many: standard error, intervals, p-values, least squares.

Render (from anim/):
    manim -qm src/week08_scenes.py ManySamplesOneBell -o w08_samples.mp4
    manim -qm src/week08_scenes.py IntervalsThatMiss -o w08_intervals.mp4
    manim -qm src/week08_scenes.py PValueIsATail -o w08_pvalue.mp4
    manim -qm src/week08_scenes.py LeastSquaresLiterally -o w08_leastsq.mp4
"""
import math

import numpy as np
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption

# ----------------------------------------------------------------------------
# Clip 1: one bike N(90, 8); the average of 16 bikes N(90, 2). 300 samples.
# ----------------------------------------------------------------------------
MU, SIGMA, N_PER, N_SAMPLES, N_SLOW = 90.0, 8.0, 16, 300, 6
SE = SIGMA / math.sqrt(N_PER)                                         # 2
SX_LO, SX_HI, SBIN = 66, 114, 1
SAMPLES = np.random.default_rng(8).normal(MU, SIGMA, (N_SAMPLES, N_PER))
MEANS = SAMPLES.mean(axis=1)                                          # sd of the 300 means: 1.98
S_EDGES = np.arange(SX_LO, SX_HI + SBIN, SBIN)
S_YMAX = 70                                                           # tallest bin 56, red bell peak 59.8


def wide_bell(x):
    """One bike, N(90, 8), scaled to the histogram of 300 means in 1-km bins (same total area)."""
    return N_SAMPLES * SBIN * math.exp(-0.5 * ((x - MU) / SIGMA) ** 2) / (SIGMA * math.sqrt(2 * math.pi))


def narrow_bell(x):
    """The average of 16, N(90, 2), on the same scale."""
    return N_SAMPLES * SBIN * math.exp(-0.5 * ((x - MU) / SE) ** 2) / (SE * math.sqrt(2 * math.pi))


class ManySamplesOneBell(Scene):
    """Samples of 16 flash on the axis; their averages pile into a narrow bell."""

    def construct(self):
        ax = Axes(x_range=[SX_LO, SX_HI, 6], y_range=[0, S_YMAX, 20], x_length=10.6, y_length=4.4,
                  axis_config={"include_numbers": True, "font_size": 22}).shift(UP * 0.35)
        xl = Tex("range on one charge (km)", font_size=26).next_to(ax, DOWN, buff=0.12)
        yl = Tex("samples", font_size=26).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.12)
        title = Tex(r"One bike: battery range $N(90,\,8)$", font_size=32, color=NAVY).to_corner(UL, buff=0.35)
        wide = ax.plot(wide_bell, x_range=[SX_LO, SX_HI], color=GREY, stroke_width=3, stroke_opacity=0.7)
        wide_lab = Tex("one bike", font_size=24, color=GREY).next_to(ax.c2p(103, wide_bell(103)), UR, buff=0.08)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=1.2)
        self.play(Create(wide), FadeIn(wide_lab), run_time=0.8)

        n = ValueTracker(0)
        ux, uy = ax.x_axis.unit_size, ax.y_axis.unit_size

        def bars():
            counts, _ = np.histogram(MEANS[:int(n.get_value())], S_EDGES)
            g = VGroup()
            for i, c in enumerate(counts):
                if c:
                    g.add(Rectangle(width=ux * SBIN, height=uy * c, color=NAVY, fill_color=NAVY,
                                    fill_opacity=0.6, stroke_width=1).move_to(ax.c2p(S_EDGES[i], 0), aligned_edge=DL))
            return g

        def sample_dots(i):
            return VGroup(*[Dot(ax.c2p(x, 0), radius=0.055, color=WHITE) for x in SAMPLES[i] if SX_LO <= x <= SX_HI])

        counter = always_redraw(lambda: Tex(f"samples of 16 bikes: {int(n.get_value())}", font_size=28, color=GREY)
                                .to_corner(UR, buff=0.4))
        hist = always_redraw(bars)
        self.add(hist, counter)

        # the first six, one at a time
        for i in range(N_SLOW):
            dots = sample_dots(i)
            m = MEANS[i]
            mark = Triangle(color=GOLD, fill_color=GOLD, fill_opacity=1).scale(0.09).rotate(PI) \
                .next_to(ax.c2p(m, 0), UP, buff=0.02)
            j = int((m - SX_LO) // SBIN)
            below = int(((MEANS[:i] >= S_EDGES[j]) & (MEANS[:i] < S_EDGES[j + 1])).sum())
            block = Rectangle(width=ux * SBIN, height=uy, color=GOLD, fill_color=GOLD, fill_opacity=0.9,
                              stroke_width=1).move_to(ax.c2p(m, 0) + UP * 0.5)
            slow = 0.85 if i < 2 else 0.5
            extra = [Tex("average", font_size=22, color=GOLD).next_to(mark, UP, buff=0.55)] if i == 0 else []
            self.play(LaggedStart(*[FadeIn(d, scale=0.4) for d in dots], lag_ratio=0.04), run_time=0.45 * slow)
            self.play(FadeIn(mark), FadeIn(block), *[FadeIn(e) for e in extra], run_time=0.25 * slow)
            self.play(block.animate.move_to(ax.c2p(S_EDGES[j], below), aligned_edge=DL), FadeOut(dots),
                      run_time=0.4 * slow)
            n.set_value(i + 1)
            self.remove(block)
            self.play(FadeOut(mark), *[FadeOut(e) for e in extra], run_time=0.1)

        # then the rest, fast
        flash = always_redraw(lambda: sample_dots(min(int(n.get_value()), N_SAMPLES - 1)))
        self.add(flash)
        self.play(n.animate.set_value(N_SAMPLES), run_time=2.6, rate_func=linear)
        self.remove(flash)

        narrow = ax.plot(narrow_bell, x_range=[MU - 4 * SE, MU + 4 * SE], color=RED, stroke_width=5)
        narrow_lab = Tex("average of 16", font_size=24, color=RED).next_to(ax.c2p(92.5, 52), RIGHT, buff=0.1)
        se = Tex(r"standard error = $8/\sqrt{16} = 2$", font_size=30, color=RED) \
            .next_to(ax.c2p(96, 38), RIGHT, buff=0.2)
        self.play(Create(narrow), FadeIn(narrow_lab), FadeIn(se), run_time=1.4)
        self.play(Write(caption("One bike: give or take 8 km. The average of 16: give or take 2 km.")), run_time=1.2)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 2: twenty 95% intervals, xbar +- 1.96 with standard error 8/sqrt(64) = 1.
# Seed 275: exactly one of the twenty misses 90 (the 12th, xbar = 93.34).
# ----------------------------------------------------------------------------
N_INT, IV_SE, Z95 = 20, 1.0, 1.96
XBARS = np.random.default_rng(275).normal(MU, IV_SE, N_INT)
CAUGHT = np.abs(XBARS - MU) <= Z95 * IV_SE                             # 19 True, one False


class IntervalsThatMiss(Scene):
    """Twenty intervals stack up; nineteen cross the true mean, one misses and turns red."""

    def construct(self):
        nl = NumberLine(x_range=[84, 96, 1], length=10.0, include_numbers=True, font_size=22, color=GREY,
                        numbers_to_exclude=[]).move_to(DOWN * 2.7)
        xl = Tex("km", font_size=24, color=GREY).next_to(nl, RIGHT, buff=0.2)
        top, step = 2.55, 0.245
        truth = DashedLine(nl.n2p(MU) + UP * 0.1, nl.n2p(MU) + UP * (2.7 + top + 0.25), color=GOLD, stroke_width=3)
        truth_lab = Tex("true mean 90", font_size=26, color=GOLD).next_to(truth, UP, buff=0.08)
        title = Tex(r"20 samples of 64 bikes: $\bar x \pm 1.96$", font_size=28, color=NAVY).to_corner(UL, buff=0.35)
        self.play(Create(nl), FadeIn(xl), Create(truth), FadeIn(truth_lab), Write(title), run_time=1.5)

        k, shown = ValueTracker(0), ValueTracker(0)
        counter = always_redraw(lambda: Tex(f"caught 90: {int(k.get_value())} of {int(shown.get_value())}",
                                            font_size=30, color=WHITE).to_corner(UR, buff=0.35))
        self.add(counter)

        miss = None
        for i, xb in enumerate(XBARS):
            y = top - i * step
            lo, hi = nl.n2p(xb - Z95 * IV_SE), nl.n2p(xb + Z95 * IV_SE)
            seg = Line([lo[0], y, 0], [hi[0], y, 0], color=NAVY, stroke_width=5)
            dot = Dot([nl.n2p(xb)[0], y, 0], radius=0.05, color=WHITE)
            iv = VGroup(seg, dot)
            self.play(Create(seg), FadeIn(dot), run_time=0.3)
            shown.set_value(i + 1)
            if CAUGHT[i]:
                k.increment_value(1)
            else:
                miss = iv
                self.play(seg.animate.set_color(RED), dot.animate.set_color(RED), run_time=0.4)
        self.wait(0.6)
        self.play(Indicate(miss, color=RED, scale_factor=1.15), run_time=1.0)
        self.wait(0.4)
        self.play(Write(caption("95\\% is about the method: about 19 intervals in 20 catch the truth.")), run_time=1.5)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 3: returns test. H0: 8% returned. 400 bikes, 22 returned (5.5%): z = -1.84,
# p = .066. 800 bikes, 44 returned (5.5%): z = -2.61, p = .009.
# ----------------------------------------------------------------------------
P0_RET = 0.08


def z_stat(returned, n):
    return (returned / n - P0_RET) / math.sqrt(P0_RET * (1 - P0_RET) / n)


def std_normal(z):
    return math.exp(-0.5 * z * z) / math.sqrt(2 * math.pi)


class PValueIsATail(Scene):
    """The observed z drops onto the null bell; the two tails beyond it are the p-value."""

    def construct(self):
        ax = Axes(x_range=[-4, 4, 1], y_range=[0, 0.45, 0.1], x_length=10.0, y_length=4.0,
                  axis_config={"include_numbers": False, "font_size": 22},
                  x_axis_config={"include_numbers": True},
                  tips=False).shift(DOWN * 0.15)
        ax.y_axis.set_opacity(0)
        zero = MathTex("0", font_size=22).next_to(ax.c2p(0, 0), DOWN, buff=0.2)
        curve = ax.plot(std_normal, x_range=[-4, 4], color=WHITE, stroke_width=4)
        h0 = Tex(r"if nothing changed ($H_0$: 8\% returned)", font_size=28, color=GREY) \
            .next_to(ax.c2p(0, std_normal(0)), UP, buff=0.15)
        cuts = VGroup(*[DashedLine(ax.c2p(c, 0), ax.c2p(c, 0.3), color=GREY, stroke_width=2, stroke_opacity=0.7)
                        for c in (-1.96, 1.96)])
        cut_lab = Tex(r"$\pm 1.96$: 5\% outside", font_size=22, color=GREY).next_to(cuts[1], UR, buff=0.05)
        xl = Tex("$z$", font_size=28, color=GREY).next_to(ax.x_axis, RIGHT, buff=0.15)
        self.play(Create(ax), Create(curve), FadeIn(h0), FadeIn(xl), FadeIn(zero), run_time=1.6)
        self.play(Create(cuts), FadeIn(cut_lab), run_time=0.8)

        def stage(returned, n, z_shown, p_text, verdict, color):
            z = round(z_stat(returned, n), 2)
            assert abs(z - z_shown) < 0.005
            head = Tex(f"{n} bikes, {returned} returned: 5.5\\%", font_size=30, color=color).to_corner(UL, buff=0.35)
            marker = VGroup(Line(ax.c2p(z, 0), ax.c2p(z, 0.33), color=color, stroke_width=5),
                            Dot(ax.c2p(z, 0), radius=0.08, color=color))
            zlab = MathTex(f"z = {z_shown:.2f}", font_size=30, color=color).next_to(ax.c2p(z, 0.33), UP, buff=0.1) \
                .align_to(marker, RIGHT)
            tails = VGroup(ax.get_area(curve, x_range=[-4, -abs(z)], color=color, opacity=0.85),
                           ax.get_area(curve, x_range=[abs(z), 4], color=color, opacity=0.85))
            plab = Tex(p_text, font_size=34, color=color).to_corner(UR, buff=0.35)
            vlab = Tex(verdict, font_size=28, color=color).next_to(plab, DOWN, buff=0.15).align_to(plab, RIGHT)
            return head, marker, zlab, tails, plab, vlab

        h1, m1, z1, t1, p1, v1 = stage(22, 400, -1.84, "p-value = .066", "inside the cut-offs: not enough evidence", GOLD)
        self.play(FadeIn(h1), FadeIn(m1, shift=DOWN * 1.5), FadeIn(z1, shift=DOWN * 1.5), run_time=1.0)
        self.play(FadeIn(t1), run_time=0.8)
        self.play(Write(p1), FadeIn(v1), run_time=0.9)
        self.wait(1.6)

        h2, m2, z2, t2, p2, v2 = stage(44, 800, -2.61, "p-value = .009", r"outside: reject $H_0$", RED)
        self.play(ReplacementTransform(h1, h2), ReplacementTransform(m1, m2), ReplacementTransform(z1, z2),
                  ReplacementTransform(t1, t2), ReplacementTransform(p1, p2), ReplacementTransform(v1, v2),
                  run_time=1.6)
        self.wait(1.4)
        self.play(Write(caption("The p-value is the tail beyond what we saw, on both sides.")), run_time=1.5)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 4: five (temperature, range) points. Through the centre (10, 88), sum of
# squared residuals at slope b is 166 - 400 b + 250 b^2: 166 at b = 0, minimum 6 at b = 0.8.
# ----------------------------------------------------------------------------
B_PEAK = 1.25    # the steepest line that still fits the 75-100 km box: 75.5 at 0 C, 100.5 at 20 C
TEMPS = np.array([0, 5, 10, 15, 20], dtype=float)
RANGES_KM = np.array([80, 84, 89, 90, 97], dtype=float)
XC, YC = TEMPS.mean(), RANGES_KM.mean()                               # (10, 88)
LX_LO, LX_HI, LY_LO, LY_HI = 0, 25, 75, 100


def fitted(x, b):
    return YC + b * (x - XC)


def residual(x, y, b):
    """Observed minus the line through the centre with slope b."""
    return y - fitted(x, b)


def sum_squares(b):
    return float(sum(residual(x, y, b) ** 2 for x, y in zip(TEMPS, RANGES_KM)))


def clipped_ends(b):
    """End points of the line inside the plotting box 0-25 x 75-100."""
    xs = [LX_LO, LX_HI]
    if b > 1e-9:
        xs = [max(LX_LO, XC + (LY_LO - YC) / b), min(LX_HI, XC + (LY_HI - YC) / b)]
    return xs[0], xs[1]


assert abs(sum_squares(0) - 166) < 1e-9 and abs(sum_squares(0.8) - 6) < 1e-9


class LeastSquaresLiterally(Scene):
    """A line pivots about the centre; each residual carries its square; the total is smallest at 0.8."""

    def construct(self):
        ax = Axes(x_range=[LX_LO, LX_HI, 5], y_range=[LY_LO, LY_HI, 5], x_length=6.8, y_length=5.0,
                  axis_config={"include_numbers": True, "font_size": 22}, tips=False) \
            .to_edge(LEFT, buff=1.0).shift(UP * 0.45)
        zero = MathTex("0", font_size=22).next_to(ax.c2p(0, LY_LO), DOWN, buff=0.2)
        xl = Tex(r"temperature ($^\circ$C)", font_size=24).next_to(ax.x_axis, DOWN, buff=0.5)
        yl = Tex("range (km)", font_size=24).rotate(90 * DEGREES).next_to(ax.y_axis, LEFT, buff=0.45)
        pts = VGroup(*[Dot(ax.c2p(x, y), radius=0.08, color=WHITE) for x, y in zip(TEMPS, RANGES_KM)])
        self.play(Create(ax), FadeIn(zero), FadeIn(xl), FadeIn(yl), LaggedStart(*[FadeIn(p, scale=0.5) for p in pts],
                                                                    lag_ratio=0.15), run_time=1.6)

        b = ValueTracker(0.0)
        ux, uy = ax.x_axis.unit_size, ax.y_axis.unit_size

        def line():
            x1, x2 = clipped_ends(b.get_value())
            return Line(ax.c2p(x1, fitted(x1, b.get_value())), ax.c2p(x2, fitted(x2, b.get_value())),
                        color=GOLD, stroke_width=4)

        def squares():
            g = VGroup()
            for x, y in zip(TEMPS, RANGES_KM):
                r = residual(x, y, b.get_value())
                side = abs(r) * uy                                  # a true square on screen
                if side < 1e-3:
                    continue
                p_line = ax.c2p(x, fitted(x, b.get_value()))
                p_obs = ax.c2p(x, y)
                sq = Square(side_length=side, color=RED, fill_color=RED, fill_opacity=0.25, stroke_width=1.5)
                toward = RIGHT if x <= XC else LEFT                 # keep the squares inside the box
                sq.move_to((p_line + p_obs) / 2 + toward * side / 2)
                g.add(sq, Line(p_line, p_obs, color=RED, stroke_width=3))
            return g

        centre = Dot(ax.c2p(XC, YC), radius=0.06, color=GOLD)
        ln = always_redraw(line)
        sqs = always_redraw(squares)
        panel_x = 3.9
        b_lab = always_redraw(lambda: MathTex(f"b = {b.get_value():.2f}", font_size=36, color=GOLD)
                              .move_to([panel_x, 1.6, 0]))
        ss_lab = always_redraw(lambda: Tex(f"sum of squares = {sum_squares(b.get_value()):.0f}",
                                           font_size=34, color=RED).move_to([panel_x, 0.8, 0]))
        self.play(FadeIn(centre), Create(ln), FadeIn(sqs), FadeIn(b_lab), FadeIn(ss_lab), run_time=1.0)
        self.add(sqs, ln, centre)
        self.wait(0.6)
        self.play(b.animate.set_value(B_PEAK), run_time=3.0, rate_func=smooth)
        self.play(b.animate.set_value(0.8), run_time=2.4, rate_func=smooth)
        self.wait(0.4)

        eq = Tex(r"range = 80 + 0.8 $\times$ temperature", font_size=32, color=GOLD).move_to([panel_x, -0.3, 0])
        best = Tex("smallest total: 6", font_size=32, color=RED).move_to([panel_x, -1.0, 0])
        self.play(Write(eq), run_time=1.0)
        self.play(FadeIn(best), run_time=0.6)
        self.play(Write(caption("Least squares: the line that makes the squares smallest.")), run_time=1.4)
        self.wait(3.6)
