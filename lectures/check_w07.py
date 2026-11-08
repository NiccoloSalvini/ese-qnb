"""Numerical check of every number in the week-7 deck, drills and homework (three shapes, and how to decide with them; Arno Bikes).
Run: python3.11 lectures/check_w07.py"""
from math import comb, perm, sqrt, exp, isclose
import numpy as np
from scipy.stats import norm, binom, poisson

def ok(name, got, want, tol=5e-3):
    assert isclose(got, want, abs_tol=tol), f"{name}: got {got:.5f}, want {want}"
    print(f"  ok  {name:<52} {got:.4f}")

print("deck — Homework 6 corrected: H1, H2")
bothH = 110 + 75 - (180 - 30); assert bothH == 35 and (110 - 35, 35, 75 - 35, 30) == (75, 35, 40, 30) and 75 + 35 + 40 + 30 == 180
ok("HW6 H1 P(H or L)", 110/180 + 75/180 - 35/180, .833); ok("HW6 H1 P(H or L) as count", 150 / 180, .833); ok("HW6 H1 P(neither)", 30 / 180, .167)
ok("HW6 H1 P(H)", 110 / 180, .611); ok("HW6 H1 P(L)", 75 / 180, .417); ok("HW6 H1 P(both)", 35 / 180, .194)
assert comb(10, 3) == 120 and perm(10, 3) == 720 and perm(10, 3) == comb(10, 3) * 6
assert (int(.65 * 2000), int(.35 * 2000)) == (1300, 700) and (round(.03 * 1300), round(.08 * 700)) == (39, 56)
assert (1300 - 39, 700 - 56, 39 + 56, 2000 - 95) == (1261, 644, 95, 1905)
ok("HW6 H2 P(faulty|Celle)", 39 / 1300, .03); ok("HW6 H2 P(faulty|Ionix)", 56 / 700, .08); ok("HW6 H2 P(faulty)", 95 / 2000, .0475, 1e-6)
ok("HW6 H2 P(Celle|faulty)", 39 / 95, .411); ok("HW6 H2 P(Ionix|faulty)", 56 / 95, .589)
ok("HW6 H2 Bayes numerator", .08 * .35, .028, 1e-6); ok("HW6 H2 Celle cell", .03 * .65, .0195, 1e-6); ok("HW6 H2 denominator", .03 * .65 + .08 * .35, .0475, 1e-6)
ok("HW6 H2 Bayes P(Ionix|faulty)", .08 * .35 / (.03 * .65 + .08 * .35), .589)

print("deck — block A: mean, variance, a random variable (moved from lesson 6)")
x = np.array([4, 7, 3, 6, 5]); assert x.sum() == 25 and x.mean() == 5
dev = x - 5; assert dev.sum() == 0 and list(dev) == [-1, 2, -2, 1, 0] and list(dev ** 2) == [1, 4, 4, 1, 0] and (dev ** 2).sum() == 10
ok("s^2 five weeks", x.var(ddof=1), 2.5); ok("s five weeks", x.std(ddof=1), 1.58)
vals = np.array([3, 4, 5, 6, 7]); P = np.array([.15, .20, .30, .20, .15]); assert isclose(P.sum(), 1)
assert np.allclose(P * 20, [3, 4, 6, 4, 3])  # twenty weeks of history
ok("E(x) returns", (vals * P).sum(), 5.0); ok("sigma^2 returns", ((vals - 5) ** 2 * P).sum(), 1.6); ok("sigma returns", sqrt(1.6), 1.26)
assert np.allclose(vals * P, [.45, .80, 1.50, 1.20, 1.05]) and np.allclose((vals - 5) ** 2 * P, [.60, .20, 0, .20, .60])
ok("over 50 weeks", 50 * 5.0, 250, 1e-9)
assert vals.max() == 7  # "eight or more has not happened in twenty weeks"

print("deck — block B: binomial, Poisson")
ok("binomial 12,.25: P(3)", binom.pmf(3, 12, .25), .258); assert comb(12, 3) == 220 and 12 * 11 * 10 == 1320
ok("binomial: .25^3", .25 ** 3, .015625, 1e-9); ok("binomial: .75^9", .75 ** 9, .0751, 1e-4)
ok("binomial by hand", 220 * .015625 * .0751, .258, 1e-3)
ok("binomial mean", 12 * .25, 3); ok("binomial sigma", sqrt(12 * .25 * .75), 1.5); assert isclose(12 * .25 * .75, 2.25)
ok("binomial P(0)", binom.pmf(0, 12, .25), .032); ok("binomial P(>=1)", 1 - binom.pmf(0, 12, .25), .968)
ok("one-in-thirty Saturday", 1 / 30, .032, 2e-3)
ok("Poisson mu 1.5: P(0)", poisson.pmf(0, 1.5), .223); assert isclose(3 * .5, 1.5)
ok("Poisson mu 3: P(0)", poisson.pmf(0, 3), .050); ok("Poisson mu 3: P(>=1)", 1 - poisson.pmf(0, 3), .950)
ok("Poisson mu 3: P(2)", poisson.pmf(2, 3), .224); ok("e^-3", exp(-3), .0498, 1e-4); ok("9*.0498/2", 9 * .0498 / 2, .224, 1e-3)
ok("miss at least one call in half an hour", 1 - poisson.pmf(0, 1.5), .777); ok("four times out: .223/.050", .223 / .050, 4.5, .6)

print("deck — block C: the normal")
mu, sg = 90, 8
for k, lo, hi, share in ((1, 82, 98, .683), (2, 74, 106, .954), (3, 66, 114, .997)):
    assert (mu - k * sg, mu + k * sg) == (lo, hi); ok(f"within {k} sigma", norm.cdf(k) - norm.cdf(-k), share)
ok("two sigma below: one in forty", norm.cdf(-2), .025, 3e-3)
ok("z for 75 km", (75 - mu) / sg, -1.875, 1e-9); ok("P(X<75) table z=-1.88", norm.cdf(-1.88), .030); ok("P(X<75) exact", norm.cdf(75, mu, sg), .030)
ok("P(X>75)", 1 - norm.cdf(-1.88), .970, 1e-3)
for z, v in [(-2.0, .0228), (-1.9, .0287), (-1.8, .0359), (-1.7, .0446), (-1.6, .0548), (-2.04, .0207), (-1.94, .0262), (-1.84, .0329), (-1.74, .0409), (-1.64, .0505),
             (-2.05, .0202), (-1.95, .0256), (-1.85, .0322), (-1.75, .0401), (-1.65, .0495), (-2.08, .0188), (-1.98, .0239), (-1.88, .0301), (-1.78, .0375), (-1.68, .0465)]:
    ok(f"table excerpt z={z}", norm.cdf(z), v, 6e-5)
ok("z for 5%", norm.ppf(.05), -1.645); ok("guarantee x for 5%", mu + norm.ppf(.05) * sg, 76.8, .05); ok("1.645*8", 1.645 * 8, 13.2, .05)
ok("print 76: share below", norm.cdf(76, mu, sg), .040); ok("z for 76", (76 - mu) / sg, -1.75, 1e-9); ok("one rider in twenty-five", 1 / 25, .040)
for xp, share in ((85, .27), (80, .11), (76.8, .05), (75, .03)):
    ok(f"print {xp}: share below", norm.cdf(xp, mu, sg), share, 6e-3)
ok("kurtosis: three sigma under the bell, one in three hundred", 2 * norm.cdf(-3), 1 / 300, 1e-3)

print("deck — block D: the decision tree")
ev = .95 * 165 + .05 * 255; ok("Ampere expected cost", ev, 169.50, 1e-9); ok(".95*165", .95 * 165, 156.75, 1e-9); ok(".05*255", .05 * 255, 12.75, 1e-9)
assert 165 + 90 == 255; ok("extra per battery from faults", .05 * 90, 4.50, 1e-9); ok("saving per battery", 180 - ev, 10.50, 1e-9); ok("saving per month", 1000 * (180 - ev), 10500, 1e-6)
var = .95 * (165 - ev) ** 2 + .05 * (255 - ev) ** 2; ok(".95*4.5^2", .95 * 4.5 ** 2, 19.24, 5e-3); ok(".05*85.5^2", .05 * 85.5 ** 2, 365.51, 5e-3)
ok("Ampere variance", var, 384.75, 1e-9); ok("Ampere sigma", sqrt(var), 19.6, .05)
ok("1000 batteries: faulty mean", 1000 * .05, 50, 1e-9); ok("1000 batteries: faulty sigma", sqrt(1000 * .05 * .95), 6.9, .05)
ok("monthly bill", 165000 + 90 * 50, 169500, 1e-6); ok("monthly bill sigma", 90 * sqrt(1000 * .05 * .95), 620, 1)
ok("rush order of ten: saving", 10 * 15, 150, 1e-9); ok("two faulty cost", 2 * 90, 180, 1e-9)
ok("rush order: P(0)", binom.pmf(0, 10, .05), .599); ok("rush order: P(1)", binom.pmf(1, 10, .05), .315); ok("rush order: P(>=2)", 1 - binom.cdf(1, 10, .05), .086)
ok("one rush order in twelve", 1 / 12, .086, 3e-3)

print("deck — block E: the normal approximation and Monte Carlo")
n, p = 250, .06; mu_n, sg_n = n * p, sqrt(n * p * (1 - p))
ok("mu = np", mu_n, 15, 1e-9); ok("np(1-p)", n * p * (1 - p), 14.1, 1e-9); ok("sigma", sg_n, 3.755, 5e-4); assert mu_n >= 5 and n * (1 - p) == 235 >= 5
ok("z with the half unit", (19.5 - mu_n) / sg_n, 1.198, 1e-3); ok("table z=1.20", norm.cdf(1.20), .8849, 6e-5); ok("P(X>=20) approx", 1 - norm.cdf(1.20), .115, 1e-3)
ok("P(X>=20) exact binomial", 1 - binom.cdf(19, n, p), .118, 1e-3); ok("about one month in nine", 1 / 9, .115, 5e-3)
ok("z without the half unit", (20 - mu_n) / sg_n, 1.33, 2e-3); ok("P without the half unit", 1 - norm.cdf(1.33), .092, 1e-3)
ok("give or take four", sg_n, 4, .3)
ok("at 4% late: P(X>=20)", 1 - binom.cdf(19, 250, .04), .003, 2e-3); assert 1 - binom.cdf(19, 250, .04) < 1 / 50
ok("Monte Carlo: Saturdays with 3 buyers in 1,000", 1000 * binom.pmf(3, 12, .25), 258, .5); ok("Monte Carlo: Saturdays with none", 1000 * binom.pmf(0, 12, .25), 32, .5)
ok("Monte Carlo: months with >=20 late in 1,000", 1000 * (1 - binom.cdf(19, 250, .06)), 118, .5)

print("drills")
# D1
c = np.array([3, 8, 5, 6, 8]); assert c.sum() == 30 and c.mean() == 6
dc = c - 6; assert list(dc) == [-3, 2, -1, 0, 2] and dc.sum() == 0 and list(dc ** 2) == [9, 4, 1, 0, 4] and (dc ** 2).sum() == 18
ok("D1 s^2", c.var(ddof=1), 4.5); ok("D1 s", c.std(ddof=1), 2.12)
v3 = np.array([0, 1, 2, 3, 4]); p3 = np.array([.10, .20, .40, .20, .10]); assert isclose(p3.sum(), 1)
assert np.allclose(v3 * p3, [0, .20, .80, .60, .40]); ok("D1 E(x)", (v3 * p3).sum(), 2.0)
assert np.allclose((v3 - 2) ** 2 * p3, [.40, .20, 0, .20, .40]); ok("D1 sigma^2", ((v3 - 2) ** 2 * p3).sum(), 1.20); ok("D1 sigma", sqrt(1.20), 1.10)

# D2
ok("D2 binom 10,.3 P(2)", binom.pmf(2, 10, .3), .233); assert comb(10, 2) == 45; ok("D2 .7^8", .7 ** 8, .05765, 1e-4); ok("D2 .3^2", .3 ** 2, .09, 1e-9)
ok("D2 45*.09*.05765", 45 * .09 * .05765, .233, 1e-3); ok("D2 binom P(0)", binom.pmf(0, 10, .3), .028); ok("D2 binom P(>=1)", 1 - binom.pmf(0, 10, .3), .972)
ok("D2 binom mean", 10 * .3, 3); assert isclose(10 * .3 * .7, 2.1); ok("D2 binom sigma", sqrt(2.1), 1.45)
ok("D2 Poisson 4: P(0)", poisson.pmf(0, 4), .018); ok("D2 Poisson 4: P(2)", poisson.pmf(2, 4), .147); ok("D2 e^-4", exp(-4), .01832, 1e-4); ok("D2 16*.01832/2", 16 * .01832 / 2, .147, 1e-3)
assert isclose(4 * .25, 1); ok("D2 Poisson 1: P(0)", poisson.pmf(0, 1), .368); ok("D2 Poisson 1: P(>=1)", 1 - poisson.pmf(0, 1), .632); ok("D2 e^-1", exp(-1), .368)
# D3
ok("D3 z for 20 kg", (20 - 22) / 1.5, -1.333, 1e-3); ok("D3 table z=-1.33", norm.cdf(-1.33), .0918, 6e-5); ok("D3 P(X<20)", norm.cdf(20, 22, 1.5), .092, 1e-3)
ok("D3 z for 21", (21 - 22) / 1.5, -0.667, 1e-3); ok("D3 z for 24", (24 - 22) / 1.5, 1.333, 1e-3)
ok("D3 table z=1.33", norm.cdf(1.33), .9082, 6e-5); ok("D3 table z=-0.67", norm.cdf(-0.67), .2514, 6e-5); ok("D3 .9082-.2514", .9082 - .2514, .657, 1e-3)
ok("D3 P(21<X<24) exact", norm.cdf(24, 22, 1.5) - norm.cdf(21, 22, 1.5), .656, 1e-3)
ok("D3 table z=1.64", norm.cdf(1.64), .9495, 6e-5); ok("D3 table z=1.65", norm.cdf(1.65), .9505, 6e-5); ok("D3 z for 95%", norm.ppf(.95), 1.645)
ok("D3 1.645*1.5", 1.645 * 1.5, 2.47, 5e-3); ok("D3 heaviest 5% threshold", 22 + 1.645 * 1.5, 24.5, .05)
# D4
assert 1000 - 400 == 600
sat_x = np.array([6 * 600 - 2000, 10 * 600 - 2000, 14 * 600 - 2000]); sat_p = np.array([.3, .5, .2]); assert list(sat_x) == [1600, 4000, 6400] and isclose(sat_p.sum(), 1)
ads_x = np.array([4 * 600 - 1000, 6 * 600 - 1000]); ads_p = np.array([.5, .5]); assert list(ads_x) == [1400, 2600]
E_sat = (sat_x * sat_p).sum(); E_ads = (ads_x * ads_p).sum()
assert np.allclose(sat_x * sat_p, [480, 2000, 1280]) and np.allclose(ads_x * ads_p, [700, 1300])
ok("D4 E(Saturday)", E_sat, 3760, 1e-6); ok("D4 E(ads)", E_ads, 2000, 1e-6); ok("D4 difference", E_sat - E_ads, 1760, 1e-6)
assert np.allclose(sat_x - E_sat, [-2160, 240, 2640]) and np.allclose((sat_x - E_sat) ** 2 * sat_p, [1399680, 28800, 1393920])
V_sat = ((sat_x - E_sat) ** 2 * sat_p).sum(); ok("D4 var(Saturday)", V_sat, 2822400, 1e-6); ok("D4 sigma(Saturday)", sqrt(V_sat), 1680, 1e-6)
V_ads = ((ads_x - E_ads) ** 2 * ads_p).sum(); ok("D4 var(ads)", V_ads, 360000, 1e-6); ok("D4 sigma(ads)", sqrt(V_ads), 600, 1e-6)
ok("D4 spread ratio nearly three", 1680 / 600, 2.8, 1e-9); assert sat_x.min() == 1600 < E_ads
# D5
n4, p4 = 300, .05; mu4, sg4 = n4 * p4, sqrt(n4 * p4 * (1 - p4))
ok("D5 mu", mu4, 15, 1e-9); ok("D5 np(1-p)", n4 * p4 * (1 - p4), 14.25, 1e-9); ok("D5 sigma", sg4, 3.775, 5e-4); assert n4 * (1 - p4) == 285
ok("D5 z with the half unit", (19.5 - mu4) / sg4, 1.19, 3e-3); ok("D5 table z=1.19", norm.cdf(1.19), .8830, 6e-5); ok("D5 P(X>=20) approx", 1 - .8830, .117, 1e-9)
ok("D5 exact binomial", 1 - binom.cdf(19, n4, p4), .119, 1e-3); ok("D5 z without", (20 - mu4) / sg4, 1.32, 5e-3); ok("D5 P without", 1 - norm.cdf(1.32), .093, 1e-3)
ok("D5 once in eight or nine months", 1 / .117, 8.5, .5)

print("homework")
# H1
w = np.array([12, 9, 15, 10, 14, 12]); assert w.sum() == 72 and w.mean() == 12
dw = w - 12; assert list(dw) == [0, -3, 3, -2, 2, 0] and dw.sum() == 0 and (dw ** 2).sum() == 26
ok("H1 s^2", w.var(ddof=1), 5.2); ok("H1 s", w.std(ddof=1), 2.28)
vH = np.array([1, 2, 3, 4, 5]); pH = np.array([.10, .25, .30, .25, .10]); assert isclose(pH.sum(), 1)
assert np.allclose(vH * pH, [.10, .50, .90, 1.00, .50]); ok("H1 E(x)", (vH * pH).sum(), 3.0)
assert np.allclose((vH - 3) ** 2 * pH, [.40, .25, 0, .25, .40]); ok("H1 sigma^2", ((vH - 3) ** 2 * pH).sum(), 1.30); ok("H1 sigma", sqrt(1.30), 1.14)

# H2
assert comb(20, 4) == 4845; ok("H2 .2^4", .2 ** 4, .0016, 1e-9); ok("H2 .8^16", .8 ** 16, .0281, 1e-4)
ok("H2 binom 20,.2 P(4)", binom.pmf(4, 20, .2), .218); ok("H2 by hand", 4845 * .0016 * .0281, .218, 2e-3)
ok("H2 P(0) = .8^20", binom.pmf(0, 20, .2), .0115, 1e-4); ok("H2 P(>=1)", 1 - binom.pmf(0, 20, .2), .988, 1e-3)
ok("H2 mean", 20 * .2, 4); ok("H2 np(1-p)", 20 * .2 * .8, 3.2, 1e-9); ok("H2 sigma", sqrt(3.2), 1.79)
# H3
assert isclose(5 / 5, 1) and 5 * 2 == 10
ok("H3 mu 1: P(0)", poisson.pmf(0, 1), .368); ok("H3 mu 1: P(1)", poisson.pmf(1, 1), .368); ok("H3 mu 1: P(>=2)", 1 - poisson.cdf(1, 1), .264); ok("H3 by hand", 1 - .368 - .368, .264, 1e-9)
ok("H3 mu 10: P(10)", poisson.pmf(10, 10), .125); ok("H3 e^-10", exp(-10), 4.54e-5, 1e-7)
# H4
ok("H4 z for 270", (270 - 240) / 20, 1.5, 1e-9); ok("H4 table z=1.5", norm.cdf(1.5), .9332, 6e-5); ok("H4 P(X>270)", 1 - norm.cdf(1.5), .067)
ok("H4 table z=1", norm.cdf(1), .8413, 6e-5); ok("H4 table z=-1", norm.cdf(-1), .1587, 6e-5); ok("H4 P(220<X<260)", norm.cdf(1) - norm.cdf(-1), .683)
ok("H4 z for top 10%", norm.ppf(.9), 1.28); ok("H4 table z=1.28", norm.cdf(1.28), .8997, 6e-5); ok("H4 table z=1.29", norm.cdf(1.29), .9015, 6e-5)
ok("H4 flag threshold", 240 + 1.28 * 20, 265.6, 1e-9); ok("H4 1.28*20", 1.28 * 20, 25.6, 1e-9)
ok("H4 guarantee: z for 95%", norm.ppf(.95), 1.645); ok("H4 1.645*20", 1.645 * 20, 32.9, 1e-9); ok("H4 print minutes", 240 + 1.645 * 20, 272.9, 1e-9)
# H5
ev4 = .9 * 30 + .1 * 90; assert 30 + 60 == 90; ok("H5 Local expected cost", ev4, 36, 1e-9); ok("H5 saving per delivery", 40 - ev4, 4, 1e-9)
var4 = .9 * (30 - ev4) ** 2 + .1 * (90 - ev4) ** 2; ok("H5 Local variance", var4, 324, 1e-9); ok("H5 Local sigma", sqrt(var4), 18, 1e-9)
ok("H5 monthly saving on 400", 400 * (40 - ev4), 1600, 1e-6); ok("H5 late in 400: mean", 400 * .1, 40, 1e-9); ok("H5 late in 400: sigma", sqrt(400 * .1 * .9), 6, 1e-9)
ok("H5 Local monthly bill", 400 * 30 + 60 * 40, 14400, 1e-6); ok("H5 Fast monthly bill", 400 * 40, 16000, 1e-6)
# H6
n5, p5 = 200, .10; mu5, sg5 = n5 * p5, sqrt(n5 * p5 * (1 - p5))
ok("H6 mu", mu5, 20, 1e-9); ok("H6 np(1-p)", n5 * p5 * (1 - p5), 18, 1e-9); ok("H6 sigma", sg5, 4.243, 5e-4); assert mu5 >= 5 and n5 * (1 - p5) == 180
ok("H6 z for 24.5", (24.5 - mu5) / sg5, 1.06, 2e-3); ok("H6 table z=1.06", norm.cdf(1.06), .8554, 6e-5); ok("H6 P(X>=25)", 1 - .8554, .145, 1e-3); ok("H6 exact", 1 - binom.cdf(24, n5, p5), .145, 1e-3)
ok("H6 z for 14.5", (14.5 - mu5) / sg5, -1.30, 4e-3); ok("H6 table z=-1.30", norm.cdf(-1.30), .0968, 6e-5); ok("H6 P(X<=14)", norm.cdf(-1.30), .097, 1e-3); ok("H6 exact P(X<=14)", binom.cdf(14, n5, p5), .093, 1e-3)
# memo
ok("memo: sigma 12, 5% guarantee", 90 + norm.ppf(.05) * 12, 70.3, .05)
for xp, share in ((85, .27), (80, .11), (78, .07), (76, .04), (75, .03)):
    ok(f"memo: print {xp}, sigma 8: share below", norm.cdf(xp, 90, 8), share, 6e-3)
for xp, share in ((80, .20), (76, .12), (75, .11)):
    ok(f"memo: print {xp}, sigma 12: share below", norm.cdf(xp, 90, 12), share, 6e-3)

print("all week-7 numbers check out")
