"""Every number of week 8 (deck, drills, homework), recomputed. Run: python3.11 lectures/check_w08.py
Then each printed figure is looked for, as written, in the file it belongs to, so the text cannot drift."""
import sys
from math import sqrt, comb
from pathlib import Path
from scipy.stats import norm, binom

ROOT = Path(__file__).resolve().parent.parent
DECK = (ROOT / "lectures/08-inference-and-regression.qmd").read_text()
DRILLS = (ROOT / "week-08/drills.md").read_text()
HW = (ROOT / "week-08/homework.md").read_text()
fails, n = [], 0

def ok(label, got, want, tol=5e-4):
    global n; n += 1
    if abs(got - want) > tol: fails.append(f"{label}: got {got:.6f}, want {want}")

import re
def plain(t):  # drop markdown and KaTeX formatting, so "**.218**", "\\textbf{.218}" and ".218" all match
    t = t.replace("{,}", ",").replace("\\mathbf{", "").replace("\\textbf{", "").replace("\\text{", "")
    return re.sub(r"[*$}{]", "", t)

def says(label, text, *bits):
    global n
    text = plain(text)
    for b in bits:
        n += 1
        if plain(b) not in text: fails.append(f"{label}: '{b}' not found")

T = lambda z: norm.cdf(round(z, 2))           # the table: z to two decimals

def line(x, y):
    xb, yb = sum(x) / len(x), sum(y) / len(y)
    sxy = sum((a - xb) * (b - yb) for a, b in zip(x, y)); sxx = sum((a - xb) ** 2 for a in x)
    b = sxy / sxx; a = yb - b * xb
    sst = sum((v - yb) ** 2 for v in y); sse = sum((v - a - b * u) ** 2 for u, v in zip(x, y))
    return xb, yb, sxy, sxx, a, b, sst, sse, 1 - sse / sst

# ---------- deck: Homework 7 review ----------
w = [12, 9, 15, 10, 14, 12]; m = sum(w) / 6; s2 = sum((v - m) ** 2 for v in w) / 5
ok("H7 H1a mean", m, 12); ok("H7 H1a s2", s2, 5.2); ok("H7 H1a s", sqrt(s2), 2.28, 5e-3)
xs, ps = [1, 2, 3, 4, 5], [.1, .25, .3, .25, .1]
E = sum(a * b for a, b in zip(xs, ps)); V = sum((a - E) ** 2 * b for a, b in zip(xs, ps))
ok("H7 H1b E", E, 3); ok("H7 H1b var", V, 1.3); ok("H7 H1b sd", sqrt(V), 1.14, 5e-3)
ok("H7 H2 C", comb(20, 4), 4845); ok("H7 H2 P4", binom.pmf(4, 20, .2), .218)
ok("H7 H2 P0", .8 ** 20, .012); ok("H7 H2 sd", sqrt(3.2), 1.79, 5e-3)
ok("H7 H3 P0", norm.cdf(0) * 0 + 2.718281828 ** -1, .368)
ok("H7 H3 P>=2", 1 - 2 * 2.718281828 ** -1, .264); ok("H7 H3 P2 two days", 2 * 2.718281828 ** -2, .271)
ok("H7 H4a", 1 - T(1.5), .067); ok("H7 H4b", T(1) - T(-1), .683)
ok("H7 H4c", 240 + 1.645 * 20, 272.9, 1e-9)
ok("H7 VaR", 1.645 * 2000, 3290, 1e-9)
ok("H7 H5 E", .9 * 30 + .1 * 90, 36, 1e-9)
ok("H7 H5 var", .9 * 36 + .1 * 54 ** 2, 324, 1e-9); ok("H7 H5 sd", 18, sqrt(324), 1e-9)
for x_, a8, a12 in ((85, .27, .34), (80, .11, .20), (76, .04, .12), (75, .03, .11)):
    ok(f"memo {x_} s8", norm.cdf((x_ - 90) / 8), a8, 6e-3); ok(f"memo {x_} s12", norm.cdf((x_ - 90) / 12), a12, 6e-3)
ok("memo s12 5%", 90 - 1.645 * 12, 70.26, 1e-9)
says("deck HW7", DECK, "4,845", "**.218**", "**.012**", "**.988**", "**1.79**", "**.264**", "**.271**",
     "**.067**", "**.683**", "272.9", "−€3,290", "**€36**", "**€18**", "€1,600", "**70 km**")

# ---------- deck: block A ----------
sd = sqrt(250 * .06 * .94); z = (19.5 - 15) / sd
ok("A sd", sd, 3.755); ok("A z", z, 1.198); ok("A table", 1 - T(z), .115)
ok("A exact", 1 - binom.cdf(19, 250, .06), .118)
for k, se in ((1, 8), (16, 2), (64, 1), (256, .5)): ok(f"A SE n={k}", 8 / sqrt(k), se, 1e-12)
ok("A one bike >94", 1 - T(.5), .31, 5e-3); ok("A avg16 >94", 1 - T(2), .023)
says("deck A", DECK, "**3.755**", "**1.20**", "**.115**", "**118** of the thousand", "**2 km**", "share .31", "**.023**")

# ---------- deck: block B ----------
ok("B 95 lo", 88.5 - 1.96, 86.54); ok("B 95 hi", 88.5 + 1.96, 90.46)
ok("B 90 lo", 88.5 - 1.645, 86.855); ok("B 90 hi", 88.5 + 1.645, 90.145)
ok("B 99 lo", 88.5 - 2.576, 85.924); ok("B 99 hi", 88.5 + 2.576, 91.076)
ok("B wrong sqrt", 88.5 - 1.96 * 8, 72.82); ok("B wrong n", 88.5 - 1.96 * 8 / 64, 88.255)
ok("B n for 1", (1.96 * 8 / 1) ** 2, 245.86, 5e-3); ok("B n for .5", (1.96 * 8 / .5) ** 2, 983.45, 5e-3)
says("deck B", DECK, "**86.54 to 90.46 km**", "**86.86 to 90.15**", "85.92 to 91.08", "72.82 to 104.18",
     "88.26 to 88.75", "**246 bikes**", "**984**")

# ---------- deck: block C ----------
se = sqrt(.08 * .92 / 400); z = (22 / 400 - .08) / se
ok("C se", se, .01356, 5e-6); ok("C z", z, -1.84, 5e-3); ok("C p", 2 * T(z), .066, 1e-3)
se8 = sqrt(.08 * .92 / 800); z8 = (44 / 800 - .08) / se8
ok("C se800", se8, .00959, 5e-6); ok("C z800", z8, -2.61, 5e-3); ok("C p800", 2 * T(z8), .009, 1e-3)
ok("C mean z", (88.5 - 90) / 1, -1.5); ok("C mean p", 2 * T(-1.5), .134, 1e-3)
says("deck C", DECK, "$\\mathbf{-1.84}$", "$\\mathbf{.066}$", "-2.61", "**.009**", "**.134**")

# ---------- deck: block D ----------
xb, yb, sxy, sxx, a, b, sst, sse, r2 = line([0, 5, 10, 15, 20], [80, 84, 89, 90, 97])
ok("D xbar", xb, 10); ok("D ybar", yb, 88); ok("D sxy", sxy, 200); ok("D sxx", sxx, 250)
ok("D b", b, .8); ok("D a", a, 80); ok("D SST", sst, 166); ok("D SSE", sse, 6)
ok("D R2", r2, .964); ok("D r", sqrt(r2), .982); ok("D at 12", a + b * 12, 89.6); ok("D at -10", a - 10 * b, 72)
# block D (the line) moved to week 9: its numbers are asserted in check_w09.py

# ---------- drills ----------
sd = sqrt(300 * .05 * .95); z = 4.5 / sd
ok("D1 sd", sd, 3.775); ok("D1 z", z, 1.192); ok("D1 p", 1 - T(z), .117); ok("D1 exact", 1 - binom.cdf(19, 300, .05), .119)
ok("D1c", 1 - T(2), .023)
ok("D2 90", 1.645 * 3, 4.935); ok("D2 lo90", 84 - 4.935, 79.065); ok("D2 hi90", 84 + 4.935, 88.935)
ok("D2 95", 1.96 * 3, 5.88); ok("D2 iii", 84 - 1.96 * 18, 48.72); ok("D2 iv", 84 - 1.96 * 18 / 36, 83.02)
ok("D2 n", (1.96 * 18 / 2) ** 2, 311.17, 5e-3)
ok("D3 se", sqrt(.25 * .75 / 300), .025); ok("D3 z", (.3 - .25) / .025, 2); ok("D3 p", 2 * (1 - T(2)), .046, 1e-3)
xb, yb, sxy, sxx, a, b, sst, sse, r2 = line([1, 2, 3, 4, 5], [30, 34, 41, 42, 48])
ok("D4 sxy", sxy, 44); ok("D4 sxx", sxx, 10); ok("D4 b", b, 4.4); ok("D4 a", a, 25.8)
ok("D4 SST", sst, 200); ok("D4 SSE", sse, 6.4); ok("D4 R2", r2, .968); ok("D4 r", sqrt(r2), .984); ok("D4 pred", a + 3.5 * b, 41.2)
says("drills", DRILLS, "**3.775**", "**.117**", ".119", "**.023**", "**€79.07 to €88.94**", "**€78.12 to €89.88**",
     "€48.72 to €119.28", "€83.02 to €84.98", "**312 customers**", "$\\mathbf{.046}$", "**4.4**", "**25.8**",
     "**.968**", "**.984**", "**41.2**")

# ---------- homework (the numbers students must reach; they are in the drills_notes key) ----------
sd = sqrt(400 * .04 * .96); z = 3.5 / sd; ok("H1 sd", sd, 3.919); ok("H1 p", 1 - T(z), .187)
sd3 = sqrt(400 * .03 * .97); z3 = 7.5 / sd3; ok("H1c sd", sd3, 3.412); ok("H1c p", 1 - T(z3), .0139, 1e-4)
ok("H2 se16", 20 / 4, 5); ok("H2 se64", 20 / 8, 2.5); ok("H2 n", 20 ** 2, 400)
ok("H2 VaR95", 1.645 * 4500, 7402.5, 1e-9); ok("H2 VaR99", 2.33 * 4500, 10485, 1e-9)
ok("H3 lo90", 126 - 1.645 * 3, 121.065); ok("H3 hi90", 126 + 1.645 * 3, 130.935)
ok("H3 lo95", 126 - 5.88, 120.12); ok("H3 ii", 126 - 1.96 * 21, 84.84); ok("H3 iv", 126 - 1.96 * 21 / 49, 125.16)
ok("H3 n", (1.96 * 21 / 2.5) ** 2, 271.06, 5e-3)
se = sqrt(.1 * .9 / 250); z = (17 / 250 - .1) / se; ok("H4 z", round(z, 2), -1.69, 1e-9); ok("H4 p", 2 * T(z), .091, 1e-3)
se = sqrt(.1 * .9 / 500); z = (34 / 500 - .1) / se; ok("H4c z", round(z, 2), -2.39, 1e-9); ok("H4c p", 2 * T(z), .017, 1e-3)
xb, yb, sxy, sxx, a, b, sst, sse, r2 = line([0, 2, 4, 6, 8], [40, 43, 49, 50, 58])
ok("H5 b", b, 2.15); ok("H5 a", a, 39.4); ok("H5 SST", sst, 194); ok("H5 SSE", sse, 9.1)
ok("H5 R2", r2, .953); ok("H5 r", sqrt(r2), .976); ok("H5 pred", a + 5 * b, 50.15)
se = sqrt(.12 * .88 / 500); z = (45 / 500 - .12) / se; ok("memo z", round(z, 2), -2.06, 1e-9); ok("memo p", 2 * T(z), .039, 1e-3)
says("homework", HW, "€121.07 to €130.94", "€84.84 to €167.16", "€120.12 to €131.88", "€125.16 to €126.84",
     "194", "9.1", "**17 of 250**", "**34 of 500**", "**45**")

if fails:
    print("\n".join(fails)); print(f"{len(fails)} of {n} checks FAILED"); sys.exit(1)
print(f"{n}/{n} checks passed")
