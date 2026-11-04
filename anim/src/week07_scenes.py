"""Week 7 clips — randomness one by one, a shape all together.

Render (from anim/):
    manim -qm src/week07_scenes.py PoissonArrivals -o w07_poisson.mp4
    manim -qm src/week07_scenes.py NormalAreaFills -o w07_normal.mp4
"""
import math

import numpy as np
from manim import *
from common import NAVY, RED, GREY, GOLD, GREEN, caption

# ----------------------------------------------------------------------------
# Clip 1: calls to the Arno Bikes helpline, 09:00–18:00, rate 3 per hour.
# ----------------------------------------------------------------------------
HOURS, RATE = 9, 3
_rng = np.random.default_rng(26)
CALLS = np.sort(_rng.uniform(0, HOURS, _rng.poisson(RATE * HOURS)))   # 27 calls
PER_HOUR = np.bincount(CALLS.astype(int), minlength=HOURS)             # [1 4 3 2 5 2 3 2 5], mean 3.0
BINS = 7                                                               # 0,1,...,5,6+


def hist_counts(hours_done):
    """How many of the finished hours had 0, 1, ..., 6+ calls."""
    done = PER_HOUR[:hours_done]
    return np.bincount(np.minimum(done, BINS - 1), minlength=BINS)


class PoissonArrivals(Scene):
    """Dots land at random on a day's timeline; the per-hour counts pile into the Poisson shape."""

    def construct(self):
        # timeline, left
        tl = NumberLine(x_range=[0, HOURS, 1], length=6.4, include_numbers=False, color=GREY,
                        stroke_width=3, tick_size=0.08).move_to(LEFT * 3.2 + DOWN * 0.1)
        hour_labels = VGroup(*[Tex(f"{9 + h:02d}", font_size=20, color=GREY).next_to(tl.n2p(h), DOWN, buff=0.15)
                               for h in range(0, HOURS + 1, 3)])
        tl_title = Tex("helpline calls, one working day", font_size=28, color=NAVY).next_to(tl, UP, buff=1.0)

        # histogram, right
        ax = Axes(x_range=[-0.5, 6.5, 1], y_range=[0, 4, 1], x_length=4.6, y_length=3.0,
                  axis_config={"include_numbers": False, "font_size": 22},
                  y_axis_config={"include_numbers": True}).move_to(RIGHT * 3.6 + DOWN * 0.1)
        bin_labels = VGroup(*[Tex(str(k) if k < BINS - 1 else "6+", font_size=22).next_to(ax.c2p(k, 0), DOWN, buff=0.15)
                              for k in range(BINS)])
        xl = Tex("calls in the hour", font_size=24).next_to(bin_labels, DOWN, buff=0.15)
        yl = Tex("hours", font_size=24).rotate(90 * DEGREES).next_to(ax.y_axis, LEFT, buff=0.3)

        self.play(Create(tl), FadeIn(hour_labels), Write(tl_title), Create(ax), FadeIn(bin_labels),
                  FadeIn(xl), FadeIn(yl), run_time=2.4)
        self.wait(1.2)

        # the clock sweeps the day; dots and bars follow it
        t = ValueTracker(0.0)
        sweep = always_redraw(lambda: Line(tl.n2p(t.get_value()) + UP * 0.45, tl.n2p(t.get_value()) + DOWN * 0.45,
                                           color=GOLD, stroke_width=3))
        dots = always_redraw(lambda: VGroup(*[Dot(tl.n2p(c) + UP * 0.22, radius=0.07, color=NAVY)
                                              for c in CALLS if c <= t.get_value()]))
        clock = always_redraw(lambda: Tex(f"{9 + int(t.get_value()):02d}:{int((t.get_value() % 1) * 60):02d}",
                                          font_size=30, color=GOLD).next_to(tl, UP, buff=0.5))
        so_far = always_redraw(lambda: Tex(f"{int((CALLS <= t.get_value()).sum())} calls",
                                           font_size=26, color=NAVY).next_to(clock, RIGHT, buff=0.6))

        def bars():
            counts = hist_counts(int(t.get_value()))
            g = VGroup()
            for k, n in enumerate(counts):
                if n == 0:
                    continue
                g.add(Rectangle(width=ax.x_axis.unit_size * 0.8, height=ax.y_axis.unit_size * n,
                                color=NAVY, fill_color=NAVY, fill_opacity=0.6, stroke_width=2)
                      .move_to(ax.c2p(k, 0), aligned_edge=DOWN))
            return g

        hist = always_redraw(bars)
        self.add(sweep, dots, clock, so_far, hist)
        self.play(t.animate.set_value(HOURS), run_time=9.5, rate_func=linear)
        self.wait(0.6)

        # settle: the sweep goes, the mean marker comes
        mean = PER_HOUR.mean()
        marker = DashedLine(ax.c2p(mean, 0), ax.c2p(mean, 4), color=RED, stroke_width=4)
        mlab = Tex(f"mean {mean:.0f}", font_size=28, color=RED).next_to(marker, UP, buff=0.1)
        self.play(FadeOut(sweep), Create(marker), Write(mlab), run_time=1.6)
        self.wait(1.2)
        self.play(Write(caption("Calls per hour: random one by one, a shape all together. Mean 3.")), run_time=1.8)
        self.wait(2.6)


# ----------------------------------------------------------------------------
# Clip 2: 200 battery ranges, N(90, 8); the share below the printed 75 km.
# ----------------------------------------------------------------------------
MU, SIGMA, N_BIKES, THRESHOLD = 90.0, 8.0, 200, 75.0
X_LO, X_HI, BIN_W = 60, 120, 2
RANGES = np.random.default_rng(15).normal(MU, SIGMA, N_BIKES)   # mean 90.4, sd 8.1, all within 60–120
EDGES = np.arange(X_LO, X_HI + BIN_W, BIN_W)


def bell(x):
    """Normal density scaled to the histogram: expected count in a bin of width BIN_W at x."""
    return N_BIKES * BIN_W * math.exp(-0.5 * ((x - MU) / SIGMA) ** 2) / (SIGMA * math.sqrt(2 * math.pi))


def share_below(x):
    return 0.5 * (1 + math.erf((x - MU) / (SIGMA * math.sqrt(2))))


class NormalAreaFills(Scene):
    """Ranges drop one by one into bins; the bell fits the pile; the left tail fills to 3.0%."""

    def construct(self):
        ax = Axes(x_range=[X_LO, X_HI, 10], y_range=[0, 24, 6], x_length=9.6, y_length=4.2,
                  axis_config={"include_numbers": True, "font_size": 22}).shift(UP * 0.25)
        xl = Tex("range on one charge (km)", font_size=28).next_to(ax, DOWN, buff=0.15)
        yl = Tex("bikes", font_size=28).rotate(90 * DEGREES).next_to(ax, LEFT, buff=0.15)
        title = Tex(r"200 bikes, battery range $N(90,\,8)$", font_size=32, color=NAVY).to_edge(UP, buff=0.3)
        self.play(Create(ax), FadeIn(xl), FadeIn(yl), Write(title), run_time=2.0)
        self.wait(1.2)

        n = ValueTracker(0)
        unit_x, unit_y = ax.x_axis.unit_size, ax.y_axis.unit_size

        def bars():
            k = int(n.get_value())
            counts, _ = np.histogram(RANGES[:k], EDGES)
            g = VGroup()
            for i, c in enumerate(counts):
                if c == 0:
                    continue
                g.add(Rectangle(width=unit_x * BIN_W, height=unit_y * c, color=NAVY, fill_color=NAVY,
                                fill_opacity=0.55, stroke_width=1.5).move_to(ax.c2p(EDGES[i], 0), aligned_edge=DL))
            return g

        def falling():
            k = int(n.get_value())
            if k >= N_BIKES:
                return VGroup()
            x = RANGES[k]
            i = min(int((x - X_LO) // BIN_W), len(EDGES) - 2)
            c = np.histogram(RANGES[:k], EDGES)[0][i]
            return Dot(ax.c2p(EDGES[i] + BIN_W / 2, c + 1.0), radius=0.06, color=GOLD)

        counter = always_redraw(lambda: Tex(f"{int(n.get_value())} bikes", font_size=28, color=GREY).to_corner(UR, buff=0.45))
        hist = always_redraw(bars)
        drop = always_redraw(falling)
        self.add(hist, drop, counter)
        self.play(n.animate.set_value(N_BIKES), run_time=5.0, rate_func=linear)
        self.remove(drop)
        self.wait(0.4)

        curve = ax.plot(bell, x_range=[X_LO, X_HI], color=GOLD, stroke_width=5)
        self.play(Create(curve), run_time=1.6)
        self.wait(0.4)

        line = DashedLine(ax.c2p(THRESHOLD, 0), ax.c2p(THRESHOLD, 22), color=RED, stroke_width=4)
        llab = Tex("printed: 75 km", font_size=26, color=RED).next_to(line, UP, buff=0.1)
        self.play(Create(line), Write(llab), run_time=1.2)
        self.wait(1.2)

        xr = ValueTracker(X_LO + 0.5)
        area = always_redraw(lambda: ax.get_area(curve, x_range=[X_LO, xr.get_value()], color=RED, opacity=0.75))
        share = always_redraw(lambda: Tex(f"P(range $<$ 75) = {100 * share_below(xr.get_value()):.1f}\\%",
                                          font_size=32, color=RED).to_corner(UR, buff=0.45))
        self.play(FadeOut(counter), run_time=0.3)
        self.add(area, share)
        self.play(xr.animate.set_value(THRESHOLD), run_time=2.2, rate_func=linear)
        self.wait(1.2)
        self.play(Write(caption("Printed range 75 km: three bikes in a hundred fall short.")), run_time=1.6)
        self.wait(2.5)


# ----------------------------------------------------------------------------
# Clip 3: Arno Bikes sends 3 of its 8 staff to the Milan fair. Ordered picks
# (8 x 7 x 6 = 336) collapse to teams (336 / 3! = 56).
# ----------------------------------------------------------------------------
STAFF = "ABCDEFGH"
ORDERINGS = ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]


def fan(parent, children, label_size=20, radius=0.07):
    """Dots for the children, labels under them, GREY lines from the parent dot."""
    dots = VGroup(*[Dot(pos, radius=radius, color=NAVY) for pos, _ in children])
    labels = VGroup(*[Tex(name, font_size=label_size, color=NAVY).next_to(pos, DOWN, buff=0.08)
                      for pos, name in children])
    lines = VGroup(*[Line(parent.get_center(), pos, color=GREY, stroke_width=1.5) for pos, _ in children])
    return dots, labels, lines


class ChoicesTree(Scene):
    """A tree of ordered picks on the left; on the right six orderings merge into one team."""

    def construct(self):
        cx = -3.5                                                # the tree's axis
        root = Dot([cx, 2.3, 0], radius=0.1, color=NAVY)
        root_lab = Tex("3 of 8 to the Milan fair", font_size=26, color=NAVY).next_to(root, UP, buff=0.15)

        lvl1 = [([cx + (i - 3.5) * 0.8, 1.1, 0], s) for i, s in enumerate(STAFF)]
        lvl2 = [([cx + (i - 3.0) * 0.7, -0.2, 0], s) for i, s in enumerate(STAFF[1:])]   # after A
        lvl3 = [([cx + (i - 2.5) * 0.6, -1.5, 0], s) for i, s in enumerate(STAFF[2:])]   # after A, B
        d1, l1, e1 = fan(root, lvl1)
        d2, l2, e2 = fan(d1[0], lvl2)
        d3, l3, e3 = fan(d2[0], lvl3, label_size=18, radius=0.06)

        counter = Tex("8", font_size=36, color=GOLD).to_edge(UP, buff=0.3)
        self.play(FadeIn(root), Write(root_lab), run_time=1.0)
        self.wait(1.2)
        self.play(Create(e1), FadeIn(d1), FadeIn(l1), Write(counter), run_time=1.5)
        self.wait(0.7)
        c2 = Tex(r"8 $\times$ 7", font_size=36, color=GOLD).to_edge(UP, buff=0.3)
        self.play(Create(e2), FadeIn(d2), FadeIn(l2), ReplacementTransform(counter, c2), run_time=1.5)
        self.wait(0.7)
        c3 = Tex(r"8 $\times$ 7 $\times$ 6 = 336 ordered picks", font_size=36, color=GOLD).to_edge(UP, buff=0.3)
        self.play(Create(e3), FadeIn(d3), FadeIn(l3), ReplacementTransform(c2, c3), run_time=1.5)
        self.wait(1.2)

        # right: the six orderings of the same three people
        rx = 3.6
        boxes = VGroup()
        for i, s in enumerate(ORDERINGS):
            pos = [rx + (i % 3 - 1) * 1.4, 1.3 - (i // 3) * 0.8, 0]
            box = RoundedRectangle(width=1.15, height=0.55, corner_radius=0.1, color=NAVY, stroke_width=2)
            boxes.add(VGroup(box, Tex(s, font_size=28, color=NAVY)).move_to(pos))
        head = Tex("the same three people, six orders", font_size=26, color=GREY).next_to(boxes, UP, buff=0.3)
        self.play(FadeIn(head), LaggedStart(*[FadeIn(b, shift=DOWN * 0.2) for b in boxes], lag_ratio=0.12),
                  run_time=1.8)
        self.wait(1.0)

        team_box = RoundedRectangle(width=3.6, height=0.7, corner_radius=0.12, color=RED, fill_color=RED,
                                    fill_opacity=0.15, stroke_width=3)
        team = VGroup(team_box, Tex(r"one team $\{A, B, C\}$", font_size=30, color=RED)).move_to([rx, -0.6, 0])
        divide = Tex(r"$\div\, 3! = 6$", font_size=32, color=GOLD).next_to(team, DOWN, buff=0.3)
        self.play(*[b.animate.move_to(team.get_center()).scale(0.3).set_opacity(0) for b in boxes],
                  FadeIn(team), run_time=1.5)
        self.remove(boxes)
        self.wait(0.4)
        self.play(Write(divide), run_time=0.9)
        self.wait(0.5)
        c4 = Tex(r"336 $\div$ 6 = 56 teams", font_size=36, color=GOLD).to_edge(UP, buff=0.3)
        self.play(ReplacementTransform(c3, c4), run_time=1.0)
        self.wait(0.8)
        self.play(Write(caption("Order matters: 336 permutations. Order does not: 56 combinations.")), run_time=1.5)
        self.wait(2.5)


# ----------------------------------------------------------------------------
# Clip 4: one family. Binomial(12, .25) -> Poisson(3) as n grows with np fixed;
# Binomial(n, .25) -> the bell as n grows with p fixed.
# ----------------------------------------------------------------------------
from scipy.special import gammaln   # noqa: E402

N0, P0, LAM = 12, 0.25, 3.0
N_POIS, N_BELL = 200, 400
P_POIS = LAM / N_POIS                       # .015


def binom_pmf(ks, n, p):
    """Binomial pmf for real-valued n (gamma functions), so the bars move smoothly between frames."""
    ks = np.asarray(ks, dtype=float)
    out = np.zeros_like(ks)
    ok = ks <= n
    k = ks[ok]
    out[ok] = np.exp(gammaln(n + 1) - gammaln(k + 1) - gammaln(n - k + 1)
                     + k * math.log(p) + (n - k) * math.log(1 - p))
    return out


def poisson_pmf(ks, lam):
    ks = np.asarray(ks, dtype=float)
    return np.exp(-lam + ks * math.log(lam) - gammaln(ks + 1))


def x_max(n, p):
    """Right end of the x-axis: enough room for mean + 4 sd, never less than 12 (and a bit, so "12" is drawn)."""
    m, s = n * p, math.sqrt(n * p * (1 - p))
    return max(12.6, m + 4 * s + 1)


def nice_step(xmax):
    for step in (1, 2, 5, 10, 20, 25, 50):
        if xmax / step <= 13:
            return step
    return 100


def make_axes(xmax, ymax):
    return Axes(x_range=[0, xmax, nice_step(xmax)], y_range=[0, ymax, ymax], x_length=10.0, y_length=4.0,
                axis_config={"include_numbers": False, "font_size": 22, "include_ticks": True},
                x_axis_config={"include_numbers": True},
                y_axis_config={"include_ticks": False}).shift(UP * 0.1)


def bell_height(x):
    """Normal density matching Binomial(N_BELL, P0): the height of a bar of width 1 at x."""
    m, s = N_BELL * P0, math.sqrt(N_BELL * P0 * (1 - P0))
    return math.exp(-0.5 * ((x - m) / s) ** 2) / (s * math.sqrt(2 * math.pi))


class OneFamily(Scene):
    """Binomial bars morph into the Poisson shape, then rewind and spread into the bell."""

    def construct(self):
        n = ValueTracker(N0)
        p = ValueTracker(P0)

        def state():
            nv, pv = n.get_value(), p.get_value()
            xm = x_max(nv, pv)
            ks = np.arange(0, int(xm) + 1)
            pm = binom_pmf(ks, nv, pv)
            return nv, pv, xm, ks, pm, 1.18 * pm.max()

        def axes():
            _, _, xm, _, _, ym = state()
            return make_axes(xm, ym)

        def bars():
            nv, pv, xm, ks, pm, ym = state()
            ax = make_axes(xm, ym)
            ux, uy = ax.x_axis.unit_size, ax.y_axis.unit_size
            w = max(ux * 0.85, 0.02)
            g = VGroup()
            for k, q in zip(ks, pm):
                if q < 2e-4:
                    continue
                g.add(Rectangle(width=w, height=uy * q, color=NAVY, fill_color=NAVY, fill_opacity=0.6,
                                stroke_width=1 if ux > 0.12 else 0).move_to(ax.c2p(k, 0), aligned_edge=DOWN))
            return g

        ax = always_redraw(axes)
        hist = always_redraw(bars)
        # "n = 12, p = 0.250": the digits are an Integer and a DecimalNumber laid over invisible
        # placeholders in one Tex, so the label keeps its shape while n grows from 2 to 3 digits
        frame = Tex(r"$n =\,$", "$000$", r", $p =\,$", "$0.000$", font_size=32, color=NAVY).to_corner(UL, buff=0.4)
        frame[1].set_opacity(0)
        frame[3].set_opacity(0)
        n_num = Integer(N0, font_size=32, color=NAVY)
        p_num = DecimalNumber(P0, num_decimal_places=3, font_size=32, color=NAVY)
        n_num.add_updater(lambda m: m.set_value(int(round(n.get_value()))).move_to(frame[1], aligned_edge=LEFT))
        p_num.add_updater(lambda m: m.set_value(p.get_value()).move_to(frame[3], aligned_edge=LEFT))
        n_lab = VGroup(frame, n_num, p_num)
        xl = Tex("successes out of $n$ trials", font_size=26).to_edge(DOWN, buff=0.95)
        title = Tex("Binomial", font_size=32, color=GREY).to_corner(UR, buff=0.4)

        self.play(Create(ax), FadeIn(hist), FadeIn(n_lab), FadeIn(xl), Write(title), run_time=1.4)
        self.add(ax, hist)
        self.wait(1.0)

        # phase 1: n up, p down, np = 3 throughout
        self.play(n.animate.set_value(N_POIS), p.animate.set_value(P_POIS), run_time=4.0, rate_func=smooth)
        _, _, xm, _, _, ym = state()
        ax1 = make_axes(xm, ym)
        ks = np.arange(0, 13)
        pois = VGroup(*[Dot(ax1.c2p(k, q), radius=0.09, color=GOLD) for k, q in zip(ks, poisson_pmf(ks, LAM))])
        pois_lab = Tex("Poisson, mean 3", font_size=32, color=GOLD).to_corner(UR, buff=0.4)
        self.play(FadeOut(title), FadeIn(pois_lab), LaggedStart(*[FadeIn(d, scale=0.5) for d in pois], lag_ratio=0.05),
                  run_time=1.4)
        self.wait(1.2)

        # rewind, then phase 2: p fixed at .25, n up to 400
        self.play(FadeOut(pois), FadeOut(pois_lab), n.animate.set_value(N0), p.animate.set_value(P0), run_time=1.0)
        self.wait(0.3)
        self.play(n.animate.set_value(N_BELL), run_time=4.0, rate_func=smooth)
        _, _, xm, _, _, ym = state()
        ax2 = make_axes(xm, ym)
        m, s = N_BELL * P0, math.sqrt(N_BELL * P0 * (1 - P0))
        bell_curve = ax2.plot(bell_height, x_range=[max(0, m - 4 * s), min(xm, m + 4 * s)], color=RED, stroke_width=5)
        bell_lab = Tex("Normal", font_size=32, color=RED).to_corner(UR, buff=0.4)
        self.play(Create(bell_curve), FadeIn(bell_lab), run_time=1.0)
        self.wait(1.0)
        self.play(Write(caption("Many trials, each rare: Poisson. Many trials, $p$ not tiny: the bell.")), run_time=1.8)
        self.wait(2.5)
