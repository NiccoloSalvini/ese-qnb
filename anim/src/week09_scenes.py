"""Week 9 clips — dummies, moving averages, AR(1), decomposition.

Render (from anim/):
    manim -qm src/week09_scenes.py TwoParallelLines -o w09_dummy.mp4
    manim -qm src/week09_scenes.py MovingAverageSmooths -o w09_movavg.mp4
    manim -qm src/week09_scenes.py TodayRemembersYesterday -o w09_ar1.mp4
    manim -qm src/week09_scenes.py TrendSeasonNoise -o w09_decomp.mp4
"""
import numpy as np
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption

# ----------------------------------------------------------------------------
# Clip 1: monthly bike sales vs ad spend; out-of-town 20 + 3 ads, city 35 + 3 ads, noise sd 2.5.
# Seed 15: the dummy regression gives slope 3.02 and city coefficient 15.06.
# ----------------------------------------------------------------------------
_rng = np.random.default_rng(15)
ADS = np.r_[_rng.uniform(2, 10, 12), _rng.uniform(2, 10, 12)]
CITY = np.r_[np.zeros(12), np.ones(12)]
SALES = 20 + 3 * ADS + 15 * CITY + _rng.normal(0, 2.5, 24)
POOL_B, POOL_A = np.polyfit(ADS, SALES, 1)                                  # one line for everybody
D_A, D_B, D_CITY = np.linalg.lstsq(np.c_[np.ones(24), ADS, CITY], SALES, rcond=None)[0]
assert abs(D_B - 3) < 0.05 and abs(D_CITY - 15) < 0.1


class TwoParallelLines(Scene):
    """One grey line through the whole cloud splits into two parallel lines once the shops get a colour."""

    def construct(self):
        ax = Axes(x_range=[0, 12, 2], y_range=[10, 80, 10], x_length=8.2, y_length=5.0,
                  axis_config={"include_numbers": True, "font_size": 22}, tips=False) \
            .to_edge(LEFT, buff=1.0).shift(UP * 0.4)
        xl = Tex("ad spend (thousand euro)", font_size=24).next_to(ax.x_axis, DOWN, buff=0.5)
        yl = Tex("bikes sold per month", font_size=24).rotate(90 * DEGREES).next_to(ax.y_axis, LEFT, buff=0.5)
        dots = VGroup(*[Dot(ax.c2p(x, y), radius=0.07, color=GREY) for x, y in zip(ADS, SALES)])
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), LaggedStart(*[FadeIn(d, scale=0.5) for d in dots],
                                                                    lag_ratio=0.03), run_time=1.8)
        x1, x2 = 1.5, 10.5
        pooled = Line(ax.c2p(x1, POOL_A + POOL_B * x1), ax.c2p(x2, POOL_A + POOL_B * x2), color=WHITE, stroke_width=4)
        one_lab = Tex("one line for all shops", font_size=28, color=WHITE).to_corner(UR, buff=0.5)
        self.play(Create(pooled), FadeIn(one_lab), run_time=1.1)
        self.wait(0.9)

        # colour by group
        self.play(*[d.animate.set_color(GOLD if c else NAVY) for d, c in zip(dots, CITY)], run_time=1.0)
        legend = VGroup(Tex("city shops", font_size=28, color=GOLD),
                        Tex("out-of-town shops", font_size=28, color=NAVY)).arrange(DOWN, aligned_edge=RIGHT) \
            .to_corner(UR, buff=0.5)
        low = Line(ax.c2p(x1, D_A + D_B * x1), ax.c2p(x2, D_A + D_B * x2), color=NAVY, stroke_width=5)
        high = Line(ax.c2p(x1, D_A + D_CITY + D_B * x1), ax.c2p(x2, D_A + D_CITY + D_B * x2),
                    color=GOLD, stroke_width=5)
        self.play(ReplacementTransform(pooled, VGroup(low, high)), ReplacementTransform(one_lab, legend),
                  run_time=1.3)
        self.wait(0.4)

        xb = 11.0
        span = Line(ax.c2p(xb, D_A + D_B * xb), ax.c2p(xb, D_A + D_CITY + D_B * xb))
        brace = Brace(span, direction=RIGHT, color=WHITE)
        blab = VGroup(Tex("+15 bikes:", font_size=30, color=WHITE),
                      Tex("the city coefficient", font_size=26, color=WHITE)).arrange(DOWN, aligned_edge=LEFT) \
            .next_to(brace, RIGHT, buff=0.15)
        slope = Tex("both slopes: 3 bikes per thousand euro", font_size=24, color=GREY) \
            .next_to(legend, DOWN, buff=0.35).align_to(legend, RIGHT)
        self.play(GrowFromCenter(brace), Write(blab), FadeIn(slope), run_time=1.3)
        self.wait(0.8)
        self.play(Write(caption("A dummy moves the line up; the slope stays the same.")), run_time=1.3)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 2: monthly sales Jan-Dec; forecast for month t+1 = mean of months t-2..t.
# ----------------------------------------------------------------------------
MONTHLY = np.array([120, 132, 118, 141, 125, 138, 150, 131, 146, 158, 140, 155], dtype=float)
MONTH_LETTERS = "JFMAMJJASONDJ"
MA3 = {t + 1: MONTHLY[t - 3:t].mean() for t in range(3, 13)}               # month (1-based) -> forecast
assert abs(MA3[13] - 151) < 1e-9


class MovingAverageSmooths(Scene):
    """A three-month window slides along the jagged series; its averages trace a smooth red line, one month late."""

    def construct(self):
        ax = Axes(x_range=[0, 13.6, 1], y_range=[100, 170, 10], x_length=10.6, y_length=4.8,
                  axis_config={"include_numbers": False, "font_size": 22}, tips=False,
                  y_axis_config={"include_numbers": True}).shift(UP * 0.4 + RIGHT * 0.2)
        mlabs = VGroup(*[Tex(c, font_size=24, color=GREY if m <= 12 else RED).next_to(ax.c2p(m, 100), DOWN, buff=0.18)
                         for m, c in enumerate(MONTH_LETTERS, start=1)])
        yl = Tex("bikes sold", font_size=24).rotate(90 * DEGREES).next_to(ax.y_axis, LEFT, buff=0.5)
        pts = [ax.c2p(m, v) for m, v in enumerate(MONTHLY, start=1)]
        jag = VMobject(color=GREY, stroke_width=3).set_points_as_corners(pts)
        jdots = VGroup(*[Dot(p, radius=0.06, color=GREY) for p in pts])
        title = Tex("monthly sales", font_size=28, color=GREY).to_corner(UL, buff=0.4)
        self.play(Create(ax), FadeIn(mlabs), FadeIn(yl), FadeIn(title), Create(jag), FadeIn(jdots), run_time=1.8)
        self.wait(0.4)

        ux = ax.x_axis.unit_size
        h = ax.y_axis.unit_size * 70

        def window(t):
            return Rectangle(width=3 * ux, height=h, stroke_color=GOLD, stroke_width=2, fill_color=GOLD,
                             fill_opacity=0.15).move_to(ax.c2p(t - 1, 135))

        win = window(3)
        wlab = Tex("average of 3", font_size=24, color=GOLD).next_to(win, UP, buff=0.08)
        self.play(FadeIn(win), FadeIn(wlab), run_time=0.5)
        reds = VGroup()
        red_line = VMobject(color=RED, stroke_width=4)
        self.add(red_line)
        for t in range(3, 13):
            if t > 3:
                self.play(win.animate.move_to(ax.c2p(t - 1, 135)), wlab.animate.next_to(window(t), UP, buff=0.08),
                          run_time=0.3)
            src = VGroup(*[jdots[i].copy() for i in range(t - 3, t)])
            d = Dot(ax.c2p(t + 1, MA3[t + 1]), radius=0.08, color=RED)
            run = 0.6 if t == 3 else 0.32
            self.play(ReplacementTransform(src, d), run_time=run)
            reds.add(d)
            if len(reds) > 1:
                red_line.set_points_as_corners([r.get_center() for r in reds])
        self.add(reds)
        jan = Tex("next January: 151", font_size=30, color=RED).next_to(reds[-1], UP, buff=0.9).shift(LEFT * 0.6)
        arrow = Arrow(jan.get_bottom(), reds[-1].get_center(), buff=0.12, color=RED, stroke_width=3,
                      max_tip_length_to_length_ratio=0.2)
        self.play(FadeOut(win), FadeOut(wlab), run_time=0.3)
        self.play(Write(jan), GrowArrow(arrow), Flash(reds[-1], color=RED), run_time=0.9)
        self.wait(0.6)
        self.play(Write(caption("Average the last three: the noise cancels, but the line lags.")), run_time=1.3)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 3: AR(1) around 100, same shocks (sd 4, seed 0) and a +20 shock at month 10,
# phi = 0, 0.5, 0.9.
# ----------------------------------------------------------------------------
AR_T, AR_MEAN, SHOCK_MONTH = 30, 100.0, 10
SHOCKS = np.random.default_rng(0).normal(0, 4, AR_T)
SHOCKS[SHOCK_MONTH - 1] = 20.0
PHIS = (0.0, 0.5, 0.9)
AR_LABELS = (r"$\varphi = 0$: no memory", r"$\varphi = 0.5$", r"$\varphi = 0.9$: long memory")
AR_Y = (85, 130)


def ar_path(phi):
    """y_0 = 100, then y_t = 100 + phi (y_{t-1} - 100) + e_t for months 1..30."""
    y, out = AR_MEAN, [AR_MEAN]
    for e in SHOCKS:
        y = AR_MEAN + phi * (y - AR_MEAN) + e
        out.append(y)
    return np.array(out)


PATHS = [ar_path(p) for p in PHIS]
assert all(AR_Y[0] < p.min() and p.max() < AR_Y[1] for p in PATHS)


class TodayRemembersYesterday(Scene):
    """Three series fed the same news, with phi 0, 0.5, 0.9: the +20 shock fades fast, slower, slowest."""

    def construct(self):
        axes = VGroup()
        for i, y0 in enumerate((2.15, 0.25, -1.65)):
            axes.add(Axes(x_range=[0, AR_T, 5], y_range=[AR_Y[0], AR_Y[1], 15], x_length=10.6, y_length=1.6,
                          axis_config={"include_numbers": False, "font_size": 20, "include_ticks": True},
                          x_axis_config={"include_numbers": i == 2}, tips=False).move_to([0.5, y0, 0]))
        means = VGroup(*[DashedLine(a.c2p(0, AR_MEAN), a.c2p(AR_T, AR_MEAN), color=GREY, stroke_width=2,
                                    stroke_opacity=0.7) for a in axes])
        hund = VGroup(*[Tex("100", font_size=20, color=GREY).next_to(a.c2p(0, AR_MEAN), LEFT, buff=0.12) for a in axes])
        labs = VGroup(*[Tex(t, font_size=26, color=WHITE).next_to(a.c2p(AR_T, AR_Y[1]), DL, buff=0.0)
                        for a, t in zip(axes, AR_LABELS)])
        xl = Tex("month", font_size=22, color=GREY).next_to(axes[2].x_axis, RIGHT, buff=0.2).shift(DOWN * 0.3)
        a0, a2 = axes[0], axes[2]
        band = Rectangle(width=a0.x_axis.unit_size * 0.8, height=a0.c2p(0, AR_Y[1])[1] - a2.c2p(0, AR_Y[0])[1],
                         stroke_width=0, fill_color=GOLD, fill_opacity=0.18) \
            .move_to([a0.c2p(SHOCK_MONTH, 0)[0], (a0.c2p(0, AR_Y[1])[1] + a2.c2p(0, AR_Y[0])[1]) / 2, 0])
        blab = Tex("+20 shock, month 10", font_size=24, color=GOLD).next_to(band, UP, buff=0.05)
        self.play(Create(axes), Create(means), FadeIn(hund), FadeIn(labs), FadeIn(xl), run_time=1.4)

        t = ValueTracker(0.0)

        def drawn(a, path, color):
            def f():
                tv = t.get_value()
                k = int(tv)
                pts = [a.c2p(m, path[m]) for m in range(0, min(k, AR_T) + 1)]
                if k < AR_T and tv > k:
                    frac = tv - k
                    pts.append(a.c2p(tv, path[k] + frac * (path[k + 1] - path[k])))
                g = VGroup()
                if len(pts) > 1:
                    g.add(VMobject(color=color, stroke_width=3).set_points_as_corners(pts))
                g.add(*[Dot(a.c2p(m, path[m]), radius=0.035, color=color) for m in range(1, min(k, AR_T) + 1)])
                return g
            return always_redraw(f)

        lines = [drawn(a, p, c) for a, p, c in zip(axes, PATHS, (NAVY, NAVY, NAVY))]
        self.add(*lines)
        self.play(t.animate.set_value(SHOCK_MONTH - 0.5), run_time=2.2, rate_func=linear)
        self.play(FadeIn(band), FadeIn(blab), t.animate.set_value(SHOCK_MONTH + 0.5), run_time=0.8, rate_func=linear)
        self.play(t.animate.set_value(AR_T), run_time=4.0, rate_func=linear)

        # how fast the +20 dies out: 20 phi^k on top of 100
        fades = VGroup()
        for a, phi in zip(axes, PHIS):
            ks = np.arange(SHOCK_MONTH, AR_T + 1)
            pts = [a.c2p(k, AR_MEAN + 20 * phi ** (k - SHOCK_MONTH)) for k in ks]
            fades.add(VMobject(color=RED, stroke_width=4).set_points_smoothly(pts) if phi > 0 else
                      VMobject(color=RED, stroke_width=4).set_points_as_corners(pts))
        flab = Tex("red: what is left of the shock", font_size=24, color=RED).next_to(blab, RIGHT, buff=0.8)
        self.play(Create(fades), FadeIn(flab), run_time=1.3)
        self.wait(0.5)
        self.play(Write(caption(r"AR(1): this month = a share $\varphi$ of last month's gap, plus news.")),
                  run_time=1.3)
        self.wait(3.6)


# ----------------------------------------------------------------------------
# Clip 4: quarterly sales over three years = least-squares trend + quarterly pattern + noise.
# ----------------------------------------------------------------------------
QSALES = np.array([302, 418, 483, 337, 344, 457, 524, 378, 381, 503, 558, 423], dtype=float)
QT = np.arange(1, 13)
TREND_B, TREND_A = np.polyfit(QT, QSALES, 1)                        # 354.76 + 10.91 t
TREND = TREND_A + TREND_B * QT
GAPS = QSALES - TREND
SEASON = np.array([GAPS[q::4].mean() for q in range(4)])            # -67.0, 39.1, 90.5, -62.7
SEASON_T = np.tile(SEASON, 3)
NOISE = GAPS - SEASON_T                                             # all within +-7.3
assert np.allclose(TREND + SEASON_T + NOISE, QSALES)


def bars(ax, values, color, width=0.5):
    g = VGroup()
    for t, v in zip(QT, values):
        hgt = abs(v) * ax.y_axis.unit_size
        r = Rectangle(width=width * ax.x_axis.unit_size, height=max(hgt, 0.01), stroke_width=1, color=color,
                      fill_color=color, fill_opacity=0.7)
        r.move_to(ax.c2p(t, 0), aligned_edge=DOWN if v >= 0 else UP)
        g.add(r)
    return g


class TrendSeasonNoise(Scene):
    """The series splits into three rows: a straight trend, a repeating quarterly pattern, a little noise."""

    def construct(self):
        big = Axes(x_range=[0, 12.6, 1], y_range=[250, 600, 50], x_length=10.4, y_length=4.8,
                   axis_config={"include_numbers": False, "font_size": 20}, tips=False,
                   y_axis_config={"include_numbers": True, "numbers_to_include": [300, 400, 500, 600]}) \
            .shift(UP * 0.4 + RIGHT * 0.4)
        years = VGroup(*[Tex(f"year {i + 1}", font_size=22, color=GREY).next_to(big.c2p(2.5 + 4 * i, 250), DOWN, buff=0.2)
                         for i in range(3)])
        title = Tex("quarterly sales, three years", font_size=28, color=GREY).to_corner(UL, buff=0.4)
        pts = [big.c2p(t, v) for t, v in zip(QT, QSALES)]
        series = VGroup(VMobject(color=WHITE, stroke_width=3).set_points_as_corners(pts),
                        *[Dot(p, radius=0.06, color=WHITE) for p in pts])
        self.play(Create(big), FadeIn(years), FadeIn(title), Create(series), run_time=1.8)
        self.wait(0.6)

        # three rows
        x0 = 0.6
        r1 = Axes(x_range=[0, 12.6, 1], y_range=[250, 600, 350], x_length=10.4, y_length=1.5,
                  axis_config={"include_numbers": False}, tips=False).move_to([x0, 2.35, 0])
        r2 = Axes(x_range=[0, 12.6, 1], y_range=[-100, 100, 200], x_length=10.4, y_length=1.5,
                  axis_config={"include_numbers": False}, tips=False).move_to([x0, 0.35, 0])
        r3 = Axes(x_range=[0, 12.6, 1], y_range=[-100, 100, 200], x_length=10.4, y_length=1.5,
                  axis_config={"include_numbers": False}, tips=False).move_to([x0, -1.65, 0])
        pts1 = [r1.c2p(t, v) for t, v in zip(QT, QSALES)]
        series1 = VGroup(VMobject(color=GREY, stroke_width=2).set_points_as_corners(pts1),
                         *[Dot(p, radius=0.04, color=GREY) for p in pts1])
        lab = lambda s, c, r: Tex(s, font_size=28, color=c).next_to(r.c2p(0, r.y_range[1]), LEFT, buff=0.25) \
            .align_to(r.c2p(0, r.y_range[1]), UP)
        l1, l2, l3 = lab("trend", NAVY, r1), lab("season", GOLD, r2), lab("noise", RED, r3)
        self.play(ReplacementTransform(big, r1), ReplacementTransform(series, series1), FadeOut(years),
                  FadeOut(title), run_time=1.2)
        trend = Line(r1.c2p(0.6, TREND_A + TREND_B * 0.6), r1.c2p(12.4, TREND_A + TREND_B * 12.4),
                     color=NAVY, stroke_width=5)
        self.play(Create(trend), FadeIn(l1), run_time=0.9)

        gaps1 = VGroup(*[Line(r1.c2p(t, tr), r1.c2p(t, v), color=GOLD, stroke_width=3)
                         for t, tr, v in zip(QT, TREND, QSALES)])
        self.play(Create(gaps1), run_time=0.7)
        raw = bars(r2, GAPS, GOLD)
        self.play(Create(r2), TransformFromCopy(gaps1, raw), FadeIn(l2), run_time=1.1)
        season = bars(r2, SEASON_T, GOLD)
        qlab = Tex("average gap per quarter, repeating", font_size=22, color=GOLD) \
            .next_to(r2.c2p(12.6, 100), DL, buff=0.0)
        self.play(Transform(raw, season), FadeIn(qlab), run_time=1.0)
        noise = bars(r3, NOISE, RED)
        self.play(Create(r3), FadeIn(noise), FadeIn(l3), run_time=1.0)
        self.wait(0.6)
        self.play(Write(caption("Sales = trend + season + noise. Forecast the first two; the noise is what is left.",
                                size=28)), run_time=1.4)
        self.wait(3.6)
