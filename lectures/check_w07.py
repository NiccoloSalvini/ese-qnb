"""Numerical check of every number in the week-7 deck, drills and homework (three shapes, and how to decide with them; Arno Bikes).
Run: python3.11 lectures/check_w07.py"""
from math import comb, sqrt, exp, isclose
import numpy as np
from scipy.stats import norm, binom, poisson

def ok(name, got, want, tol=5e-3):
    assert isclose(got, want, abs_tol=tol), f"{name}: got {got:.5f}, want {want}"
    print(f"  ok  {name:<52} {got:.4f}")

print("deck — recap of lesson 6")
x = np.array([4, 7, 3, 6, 5]); assert x.mean() == 5; ok("five weeks: s", x.std(ddof=1), 1.58)

print("deck — block A: binomial, Poisson")
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

print("deck — block B: the normal")
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

print("deck — block C: the decision tree")
ev = .95 * 165 + .05 * 255; ok("Ampere expected cost", ev, 169.50, 1e-9); ok(".95*165", .95 * 165, 156.75, 1e-9); ok(".05*255", .05 * 255, 12.75, 1e-9)
assert 165 + 90 == 255; ok("extra per battery from faults", .05 * 90, 4.50, 1e-9); ok("saving per battery", 180 - ev, 10.50, 1e-9); ok("saving per month", 1000 * (180 - ev), 10500, 1e-6)
var = .95 * (165 - ev) ** 2 + .05 * (255 - ev) ** 2; ok(".95*4.5^2", .95 * 4.5 ** 2, 19.24, 5e-3); ok(".05*85.5^2", .05 * 85.5 ** 2, 365.51, 5e-3)
ok("Ampere variance", var, 384.75, 1e-9); ok("Ampere sigma", sqrt(var), 19.6, .05)
ok("1000 batteries: faulty mean", 1000 * .05, 50, 1e-9); ok("1000 batteries: faulty sigma", sqrt(1000 * .05 * .95), 6.9, .05)
ok("monthly bill", 165000 + 90 * 50, 169500, 1e-6); ok("monthly bill sigma", 90 * sqrt(1000 * .05 * .95), 620, 1)
ok("rush order of ten: saving", 10 * 15, 150, 1e-9); ok("two faulty cost", 2 * 90, 180, 1e-9)
ok("rush order: P(0)", binom.pmf(0, 10, .05), .599); ok("rush order: P(1)", binom.pmf(1, 10, .05), .315); ok("rush order: P(>=2)", 1 - binom.cdf(1, 10, .05), .086)
ok("one rush order in twelve", 1 / 12, .086, 3e-3)

print("deck — block D: the normal approximation and Monte Carlo")
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
ok("D1 binom 10,.3 P(2)", binom.pmf(2, 10, .3), .233); assert comb(10, 2) == 45; ok("D1 .7^8", .7 ** 8, .05765, 1e-4); ok("D1 .3^2", .3 ** 2, .09, 1e-9)
ok("D1 45*.09*.05765", 45 * .09 * .05765, .233, 1e-3); ok("D1 binom P(0)", binom.pmf(0, 10, .3), .028); ok("D1 binom P(>=1)", 1 - binom.pmf(0, 10, .3), .972)
ok("D1 binom mean", 10 * .3, 3); assert isclose(10 * .3 * .7, 2.1); ok("D1 binom sigma", sqrt(2.1), 1.45)
ok("D1 Poisson 4: P(0)", poisson.pmf(0, 4), .018); ok("D1 Poisson 4: P(2)", poisson.pmf(2, 4), .147); ok("D1 e^-4", exp(-4), .01832, 1e-4); ok("D1 16*.01832/2", 16 * .01832 / 2, .147, 1e-3)
assert isclose(4 * .25, 1); ok("D1 Poisson 1: P(0)", poisson.pmf(0, 1), .368); ok("D1 Poisson 1: P(>=1)", 1 - poisson.pmf(0, 1), .632); ok("D1 e^-1", exp(-1), .368)
# D2
ok("D2 z for 20 kg", (20 - 22) / 1.5, -1.333, 1e-3); ok("D2 table z=-1.33", norm.cdf(-1.33), .0918, 6e-5); ok("D2 P(X<20)", norm.cdf(20, 22, 1.5), .092, 1e-3)
ok("D2 z for 21", (21 - 22) / 1.5, -0.667, 1e-3); ok("D2 z for 24", (24 - 22) / 1.5, 1.333, 1e-3)
ok("D2 table z=1.33", norm.cdf(1.33), .9082, 6e-5); ok("D2 table z=-0.67", norm.cdf(-0.67), .2514, 6e-5); ok("D2 .9082-.2514", .9082 - .2514, .657, 1e-3)
ok("D2 P(21<X<24) exact", norm.cdf(24, 22, 1.5) - norm.cdf(21, 22, 1.5), .656, 1e-3)
ok("D2 table z=1.64", norm.cdf(1.64), .9495, 6e-5); ok("D2 table z=1.65", norm.cdf(1.65), .9505, 6e-5); ok("D2 z for 95%", norm.ppf(.95), 1.645)
ok("D2 1.645*1.5", 1.645 * 1.5, 2.47, 5e-3); ok("D2 heaviest 5% threshold", 22 + 1.645 * 1.5, 24.5, .05)
# D3
assert 1000 - 400 == 600
sat_x = np.array([6 * 600 - 2000, 10 * 600 - 2000, 14 * 600 - 2000]); sat_p = np.array([.3, .5, .2]); assert list(sat_x) == [1600, 4000, 6400] and isclose(sat_p.sum(), 1)
ads_x = np.array([4 * 600 - 1000, 6 * 600 - 1000]); ads_p = np.array([.5, .5]); assert list(ads_x) == [1400, 2600]
E_sat = (sat_x * sat_p).sum(); E_ads = (ads_x * ads_p).sum()
assert np.allclose(sat_x * sat_p, [480, 2000, 1280]) and np.allclose(ads_x * ads_p, [700, 1300])
ok("D3 E(Saturday)", E_sat, 3760, 1e-6); ok("D3 E(ads)", E_ads, 2000, 1e-6); ok("D3 difference", E_sat - E_ads, 1760, 1e-6)
assert np.allclose(sat_x - E_sat, [-2160, 240, 2640]) and np.allclose((sat_x - E_sat) ** 2 * sat_p, [1399680, 28800, 1393920])
V_sat = ((sat_x - E_sat) ** 2 * sat_p).sum(); ok("D3 var(Saturday)", V_sat, 2822400, 1e-6); ok("D3 sigma(Saturday)", sqrt(V_sat), 1680, 1e-6)
V_ads = ((ads_x - E_ads) ** 2 * ads_p).sum(); ok("D3 var(ads)", V_ads, 360000, 1e-6); ok("D3 sigma(ads)", sqrt(V_ads), 600, 1e-6)
ok("D3 spread ratio nearly three", 1680 / 600, 2.8, 1e-9); assert sat_x.min() == 1600 < E_ads
# D4
n4, p4 = 300, .05; mu4, sg4 = n4 * p4, sqrt(n4 * p4 * (1 - p4))
ok("D4 mu", mu4, 15, 1e-9); ok("D4 np(1-p)", n4 * p4 * (1 - p4), 14.25, 1e-9); ok("D4 sigma", sg4, 3.775, 5e-4); assert n4 * (1 - p4) == 285
ok("D4 z with the half unit", (19.5 - mu4) / sg4, 1.19, 3e-3); ok("D4 table z=1.19", norm.cdf(1.19), .8830, 6e-5); ok("D4 P(X>=20) approx", 1 - .8830, .117, 1e-9)
ok("D4 exact binomial", 1 - binom.cdf(19, n4, p4), .119, 1e-3); ok("D4 z without", (20 - mu4) / sg4, 1.32, 5e-3); ok("D4 P without", 1 - norm.cdf(1.32), .093, 1e-3)
ok("D4 once in eight or nine months", 1 / .117, 8.5, .5)

print("homework")
# H1
assert comb(20, 4) == 4845; ok("H1 .2^4", .2 ** 4, .0016, 1e-9); ok("H1 .8^16", .8 ** 16, .0281, 1e-4)
ok("H1 binom 20,.2 P(4)", binom.pmf(4, 20, .2), .218); ok("H1 by hand", 4845 * .0016 * .0281, .218, 2e-3)
ok("H1 P(0) = .8^20", binom.pmf(0, 20, .2), .0115, 1e-4); ok("H1 P(>=1)", 1 - binom.pmf(0, 20, .2), .988, 1e-3)
ok("H1 mean", 20 * .2, 4); ok("H1 np(1-p)", 20 * .2 * .8, 3.2, 1e-9); ok("H1 sigma", sqrt(3.2), 1.79)
# H2
assert isclose(5 / 5, 1) and 5 * 2 == 10
ok("H2 mu 1: P(0)", poisson.pmf(0, 1), .368); ok("H2 mu 1: P(1)", poisson.pmf(1, 1), .368); ok("H2 mu 1: P(>=2)", 1 - poisson.cdf(1, 1), .264); ok("H2 by hand", 1 - .368 - .368, .264, 1e-9)
ok("H2 mu 10: P(10)", poisson.pmf(10, 10), .125); ok("H2 e^-10", exp(-10), 4.54e-5, 1e-7)
# H3
ok("H3 z for 270", (270 - 240) / 20, 1.5, 1e-9); ok("H3 table z=1.5", norm.cdf(1.5), .9332, 6e-5); ok("H3 P(X>270)", 1 - norm.cdf(1.5), .067)
ok("H3 table z=1", norm.cdf(1), .8413, 6e-5); ok("H3 table z=-1", norm.cdf(-1), .1587, 6e-5); ok("H3 P(220<X<260)", norm.cdf(1) - norm.cdf(-1), .683)
ok("H3 z for top 10%", norm.ppf(.9), 1.28); ok("H3 table z=1.28", norm.cdf(1.28), .8997, 6e-5); ok("H3 table z=1.29", norm.cdf(1.29), .9015, 6e-5)
ok("H3 flag threshold", 240 + 1.28 * 20, 265.6, 1e-9); ok("H3 1.28*20", 1.28 * 20, 25.6, 1e-9)
ok("H3 guarantee: z for 95%", norm.ppf(.95), 1.645); ok("H3 1.645*20", 1.645 * 20, 32.9, 1e-9); ok("H3 print minutes", 240 + 1.645 * 20, 272.9, 1e-9)
# H4
ev4 = .9 * 30 + .1 * 90; assert 30 + 60 == 90; ok("H4 Local expected cost", ev4, 36, 1e-9); ok("H4 saving per delivery", 40 - ev4, 4, 1e-9)
var4 = .9 * (30 - ev4) ** 2 + .1 * (90 - ev4) ** 2; ok("H4 Local variance", var4, 324, 1e-9); ok("H4 Local sigma", sqrt(var4), 18, 1e-9)
ok("H4 monthly saving on 400", 400 * (40 - ev4), 1600, 1e-6); ok("H4 late in 400: mean", 400 * .1, 40, 1e-9); ok("H4 late in 400: sigma", sqrt(400 * .1 * .9), 6, 1e-9)
ok("H4 Local monthly bill", 400 * 30 + 60 * 40, 14400, 1e-6); ok("H4 Fast monthly bill", 400 * 40, 16000, 1e-6)
# H5
n5, p5 = 200, .10; mu5, sg5 = n5 * p5, sqrt(n5 * p5 * (1 - p5))
ok("H5 mu", mu5, 20, 1e-9); ok("H5 np(1-p)", n5 * p5 * (1 - p5), 18, 1e-9); ok("H5 sigma", sg5, 4.243, 5e-4); assert mu5 >= 5 and n5 * (1 - p5) == 180
ok("H5 z for 24.5", (24.5 - mu5) / sg5, 1.06, 2e-3); ok("H5 table z=1.06", norm.cdf(1.06), .8554, 6e-5); ok("H5 P(X>=25)", 1 - .8554, .145, 1e-3); ok("H5 exact", 1 - binom.cdf(24, n5, p5), .145, 1e-3)
ok("H5 z for 14.5", (14.5 - mu5) / sg5, -1.30, 4e-3); ok("H5 table z=-1.30", norm.cdf(-1.30), .0968, 6e-5); ok("H5 P(X<=14)", norm.cdf(-1.30), .097, 1e-3); ok("H5 exact P(X<=14)", binom.cdf(14, n5, p5), .093, 1e-3)
# memo
ok("memo: sigma 12, 5% guarantee", 90 + norm.ppf(.05) * 12, 70.3, .05)
for xp, share in ((85, .27), (80, .11), (78, .07), (76, .04), (75, .03)):
    ok(f"memo: print {xp}, sigma 8: share below", norm.cdf(xp, 90, 8), share, 6e-3)
for xp, share in ((80, .20), (76, .12), (75, .11)):
    ok(f"memo: print {xp}, sigma 12: share below", norm.cdf(xp, 90, 12), share, 6e-3)

print("all week-7 numbers check out")
