"""Shared palette and helpers for the ESE QnB clips.

Every clip is 10–12 seconds: long enough to see the idea move, short enough to
play twice in a session without losing the room.
"""
from manim import *

NAVY, RED, GREY, GOLD, GREEN = "#2471a3", "#c0392b", "#7f8c8d", "#cdba80", "#1e8449"

# Arno Bikes, the running case, in every formula the students have already met.
FIXED, VARIABLE = 60_000, 400
def cost(q): return FIXED + VARIABLE * q
def price(q): return 1600 - 4 * q
def revenue(q): return price(q) * q
def profit(q): return revenue(q) - cost(q)          # -4q^2 + 1200q - 60000
def profit_prime(q): return -8 * q + 1200            # zero at q = 150


def line_through(ax, x0, y0, slope, half_width, **kwargs):
    """A straight line of a given slope through (x0, y0), in axis coordinates."""
    x1, x2 = x0 - half_width, x0 + half_width
    return Line(ax.c2p(x1, y0 + slope * (x1 - x0)),
                ax.c2p(x2, y0 + slope * (x2 - x0)), **kwargs)


def caption(text, size=30):
    return Tex(text, font_size=size).to_edge(DOWN, buff=0.25)
