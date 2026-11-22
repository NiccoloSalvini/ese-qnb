"""Every number of week 9 (deck, drills, homework), recomputed. Run: python3.11 lectures/check_w09.py
Outputs are refitted from lectures/data/w09_*.csv with statsmodels; then each printed figure is looked for,
as written, in the file it belongs to."""
import sys, re, csv
from math import sqrt
from pathlib import Path
import numpy as np, statsmodels.api as sm
from scipy.stats import norm, t as tdist

ROOT = Path(__file__).resolve().parent.parent; DATA = ROOT / "lectures/data"
DECK = (ROOT / "lectures/09-multiple-regression-time-series.qmd").read_text()
DRILLS = (ROOT / "week-09/drills.md").read_text()
HW = (ROOT / "week-09/homework.md").read_text()
fails, n = [], 0

def ok(label, got, want, tol=5e-3):
    global n; n += 1
    if abs(got - want) > tol: fails.append(f"{label}: got {got:.6f}, want {want}")

def plain(t):
    t = t.replace("{,}", ",").replace("\\mathbf{", "").replace("\\textbf{", "").replace("\\text{", "")
    return re.sub(r"[*$}{]", "", t)

def says(label, text, *bits):
    global n
    text = plain(text)
    for b in bits:
        n += 1
        if plain(b) not in text: fails.append(f"{label}: '{b}' not found")

def read(name):
    with open(DATA / name) as f: return list(csv.DictReader(f))

T = lambda z: norm.cdf(round(z, 2))

# ---------- Homework 8 review: H4 and the memo ----------
z = (17 / 250 - .1) / sqrt(.09 / 250); ok("H4 se", sqrt(.09 / 250), .0190, 5e-4); ok("H4 z", round(z, 2), -1.69, 1e-9); ok("H4 p", 2 * T(z), .091, 5e-4)
z = (34 / 500 - .1) / sqrt(.09 / 500); ok("H4c se", sqrt(.09 / 500), .0134, 5e-4); ok("H4c z", round(z, 2), -2.39, 1e-9); ok("H4c p", 2 * T(z), .017, 5e-4)
z = (.09 - .12) / sqrt(.12 * .88 / 500); ok("memo z", z, -2.06); ok("memo p", 2 * T(z), .039, 5e-4)
ok("memo expected", 60, .12 * 500, 1e-9); ok("memo sd", sqrt(500 * .12 * .88), 7.27)
says("deck HW8", DECK, "**−1.69**", "**.091**", "**−2.39**", "**.017**", ".01453", "-2.06", ".0197", "= .039")

# ---------- block A: the line by hand ----------
x = np.array([0, 5, 10, 15, 20.]); y = np.array([80, 84, 89, 90, 97.])
b = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum(); a = y.mean() - b * x.mean()
sst = ((y - y.mean()) ** 2).sum(); sse = ((y - a - b * x) ** 2).sum()
ok("A b", b, .8, 1e-9); ok("A a", a, 80, 1e-9); ok("A SST", sst, 166, 1e-9); ok("A SSE", sse, 6, 1e-9)
ok("A R2", 1 - sse / sst, .964, 5e-4); ok("A r", sqrt(1 - sse / sst), .982, 5e-4); ok("A 12", a + 12 * b, 89.6, 1e-9)
says("deck A line", DECK, "**200**", "**250**", "**0.8**", "**80**", "**166**", "**.964**", "**.982**", "**89.6 km**", "72 km")

# ---------- block A: the output, refitted ----------
d = read("w09_sales_demos.csv")
ads = np.array([float(r["ads_k"]) for r in d]); hrs = np.array([float(r["demo_hours"]) for r in d]); bikes = np.array([float(r["bikes"]) for r in d])
m1 = sm.OLS(bikes, sm.add_constant(ads)).fit(); ci = m1.conf_int()
ok("out const", m1.params[0], 12.74); ok("out const se", m1.bse[0], 3.29); ok("out const t", m1.tvalues[0], 3.87)
ok("out slope", m1.params[1], 5.53); ok("out se", m1.bse[1], .53); ok("out t", m1.tvalues[1], 10.38)
ok("out ci lo", ci[1][0], 4.42); ok("out ci hi", ci[1][1], 6.63); ok("out c ci", ci[0][0], 5.92); ok("out c ci hi", ci[0][1], 19.55)
ok("out R2", m1.rsquared, .830, 5e-4)
ok("beta month", .2 + 1.3 * -4, -5.0, 1e-9)
says("deck sectors", DECK, "0.2\\% + 1.3", "**1.3%**", "-5.0\\%", "R^2 = .45")
says("deck A output", DECK, "12.74", "3.29", "3.87", "5.92 to 19.55", "**5.53**", "**0.53**", "**10.38**", "**4.42 to 6.63**", "R^2 = .830")

# ---------- block B: two predictors, refitted ----------
m2 = sm.OLS(bikes, sm.add_constant(np.c_[ads, hrs])).fit()
ok("B const", m2.params[0], 13.95); ok("B ads", m2.params[1], 2.94); ok("B hrs", m2.params[2], 1.16)
ok("B se c", m2.bse[0], .99); ok("B se ads", m2.bse[1], .24); ok("B se hrs", m2.bse[2], .08)
ok("B R2", m2.rsquared, .985, 5e-4); ok("B adj", m2.rsquared_adj, .984, 5e-4)
f = lambda A, H: 13.95 + 2.94 * A + 1.16 * H
ok("plan A", f(5, 10), 40.25, 1e-9); ok("plan B", f(6, 10), 43.19, 1e-9); ok("plan C", f(6, 15), 48.99, 1e-9); ok("5 hours", 5 * 1.16, 5.80, 1e-9)
g = lambda T_, L: 82 + .7 * T_ - .4 * L
ok("ride A", g(10, 5), 87, 1e-9); ok("ride B", g(20, 25), 86, 1e-9)
ok("disc 5", 22.1 + 2.8 * 4 + 1.1 * 5, 38.8, 1e-9); ok("disc 7", 22.1 + 2.8 * 4 + 1.1 * 7, 41.0, 1e-9); ok("disc ci", 1.1 - 2 * .9, -.7, 1e-9); ok("disc p", 2 * tdist.sf(1.1 / .9, 33), .23); ok("ads p", 2 * tdist.sf(2.8 / .6, 33), 0, 1e-3)
says("deck B", DECK, "13.95", "2.94", "1.16", "0.99", "0.24", "0.08", ".985", ".984", "40.25", "43.19", "48.99", "5.80",
     "87 km", "86 km", "**38.8 to 41.0**", "**2.2 bikes**", "**−0.7 to 2.9**", "**.23 > .05**")

# ---------- block C: trend and season, refitted ----------
q = np.array([float(r["bikes"]) for r in read("w09_quarters.csv")]); tt = np.arange(1, 13)
bt, at = np.polyfit(tt, q, 1); ok("C a", at, 354.8, .05); ok("C b", bt, 10.9, .05)
gap = q - (at + bt * tt)
for k, want in enumerate((-67.0, 39.1, 90.5, -62.7)): ok(f"C Q{k + 1}", gap[k::4].mean(), want, .05)
ok("C trend 13", 354.8 + 10.9 * 13, 496.5, 1e-9); ok("C Q1 fc", 354.8 + 141.7 - 67.0, 429.5, 1e-9)
says("deck C", DECK, "354.8 + 10.9", "−67.0", "+39.1", "+90.5", "−62.7", "**429.5**", "**430 bikes**", "about 497")

# ---------- drills ----------
ok("D1 t", 4.2 / 1.5, 2.80, 1e-9); ok("D1 p", 2 * tdist.sf(2.8, 18), .012, 5e-4); ok("D1 c p", 2 * tdist.sf(18.4 / 6.2, 18), .008, 5e-4)
ok("D1 ci lo", 4.2 - 2 * 1.5, 1.2, 1e-9); ok("D1 ci hi", 4.2 + 2 * 1.5, 7.2, 1e-9)
ok("D2 p disc", 2 * tdist.sf(1.1 / .9, 33), .23); ok("D2 p ads", 2 * tdist.sf(2.8 / .6, 33), 0, 1e-3); ok("D2 p c", 2 * tdist.sf(22.1 / 3, 33), 0, 1e-3)
ok("D2 diff", 2 * 1.1, 2.2, 1e-9); ok("D2 5", 22.1 + 11.2 + 5.5, 38.8, 1e-9); ok("D2 7", 22.1 + 11.2 + 7.7, 41.0, 1e-9)
ok("D4 f1", 24 + .7 * 90, 87, 1e-9); ok("D4 mu", 24 / .3, 80, 1e-9)
m = np.array([80, 86, 83, 90, 88, 95])
ok("opt naive", np.abs(m[3:] - m[2:-1]).mean(), 5.33); ok("opt MA", np.mean([abs(m[i] - m[i - 3:i].mean()) for i in range(3, 6)]), 5.56)
says("drills", DRILLS, "1.2 to 7.2", "**30%**", "**2.2 more bikes**", "38.8 against 41.0", "−0.7 to 2.9", "**87**", "**80**", "**5.33**", "**5.56**", "**95**", "**91**")

# ---------- homework (the numbers students must reach) ----------
ok("H1 p c", 2 * tdist.sf(40 / 12, 22), .003, 5e-4); ok("H1 pred", 40 + .85 * 300, 295, 1e-9)
r = lambda km, s: .90 + .012 * km + .35 * s
ok("H2 4 stops", r(200, 4), 4.7, 1e-9); ok("H2 stop min", .35 * 60, 21, 1e-9)
ok("H3 Q1", 120 + 4 * 13 - 25, 147, 1e-9); ok("H3 Q2", 120 + 4 * 14 + 10, 186, 1e-9)
ok("H4 f1", 30 + .5 * 80, 70, 1e-9); ok("H4 mu", 30 / .5, 60, 1e-9)
says("homework", HW, "40.0", "0.85", "0.10", "0.90+0.012", "120 + 4t", "$-25$", "$+10$")

# ---------- Homework 8 review, H1–H3 and H5 ----------
from scipy.stats import binom
sd = sqrt(400 * .04 * .96); ok("H1 sd", sd, 3.919, 5e-4); ok("H1 p", 1 - T(3.5 / sd), .187, 5e-4)
sd3 = sqrt(400 * .03 * .97); ok("H1c sd", sd3, 3.412, 5e-4); ok("H1c p", 1 - T(7.5 / sd3), .014, 5e-4); ok("H1c exact", 1 - binom.cdf(19, 400, .03), .020, 5e-4)
ok("H2 95", 1.645 * 4500, 7402.5, 1e-9); ok("H2 99", 2.33 * 4500, 10485, 1e-9); ok("H3 n", (1.96 * 21 / 2.5) ** 2, 271.06)
xd = np.array([0, 2, 4, 6, 8.]); yd = np.array([40, 43, 49, 50, 58.])
bd = ((xd - 4) * (yd - 48)).sum() / ((xd - 4) ** 2).sum(); ad = 48 - bd * 4
ok("H5 b", bd, 2.15, 1e-9); ok("H5 a", ad, 39.4, 1e-9); ok("H5 R2", 1 - ((yd - ad - bd * xd) ** 2).sum() / ((yd - 48) ** 2).sum(), .953, 5e-4)
says("deck HW8 more", DECK, "**3.919**", "**.187**", "**.014**", "**€7,402.50**", "**€10,485**", "**272 customers**", "**2.15**", "**39.4**", "**.953**", "**.976**", "**50.15**")

# ---------- assumptions and the violation over time ----------
res = y - (80 + .8 * x); ok("resid", float(np.abs(res - np.array([0, 0, 1, -2, 1])).sum()), 0, 1e-9)
rq = q - (at + bt * tt)
ok("summer resid min", min(rq[2::4]), 83.2, .05); ok("winter resid max", max(rq[0::4]), -63.7, .05)
o = np.array([float(r_["orders"]) for r_ in read("w09_orders.csv")]); gp = o - o.mean()
ok("orders lag r", np.corrcoef(gp[:-1], gp[1:])[0, 1], .59)
ar = sm.OLS(o[1:], sm.add_constant(o[:-1])).fit(); ok("after AR r", np.corrcoef(ar.resid[:-1], ar.resid[1:])[0, 1], -.04)
ok("AR c", ar.params[0], 39.8, .05); ok("AR phi", ar.params[1], .60, .005); ok("AR se c", ar.bse[0], 14.6, .05); ok("AR se phi", ar.bse[1], .15, .005); ok("AR p c", ar.pvalues[0], .010, 5e-4)
f1 = 39.8 + .6 * 110; ok("AR f1", f1, 105.8, 1e-9); ok("AR f2", 39.8 + .6 * f1, 103.3, .05); ok("AR mu", 39.8 / .4, 99.5, 1e-9)
says("deck assumptions/time", DECK, "+90", "−65", "r = .59", "r = -.04", "**0.60**", "**105.8**", "103.3", "**99.5**", "14.6", ".010")

if fails:
    print("\n".join(fails)); print(f"{len(fails)} of {n} checks FAILED"); sys.exit(1)
print(f"{n}/{n} checks passed")
