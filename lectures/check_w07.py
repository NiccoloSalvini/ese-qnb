"""Numerical check of every number in the week-7 deck, drills and homework (Arno Bikes). Run: python3.11 lectures/check_w07.py"""
from math import comb, perm, sqrt, exp, isclose
import numpy as np
from scipy.stats import norm, binom, poisson

def ok(name, got, want, tol=5e-3):
    assert isclose(got, want, abs_tol=tol), f"{name}: got {got:.5f}, want {want}"
    print(f"  ok  {name:<46} {got:.4f}")

print("deck — bridge")
ok("stock 110, sigma 5: share of months run out", 1 - norm.cdf(110, 100, 5), .023)
ok("stock 110, sigma 20: share of months run out", 1 - norm.cdf(110, 100, 20), .309)

print("deck — block A")
both = 120 + 90 - (200 - 40); assert both == 50
assert (120 - both, both, 90 - both, 40) == (70, 50, 40, 40) and 70 + 50 + 40 + 40 == 200
ok("P(both)", both / 200, .25); ok("addition law P(A or S)", 120/200 + 90/200 - both/200, .80)
ok("complement", 1 - .80, .20)
assert comb(8, 3) == 56 and perm(8, 3) == 336 and perm(8, 3) == comb(8, 3) * 6
print("  ok  C(8,3)=56, P(8,3)=336")

print("deck — block B")
V, A = 700, 300; fV, fA = int(.02 * V), int(.05 * A); assert (fV, fA) == (14, 15) and fV + fA == 29
assert (V - fV, A - fA, 1000 - 29) == (686, 285, 971)
ok("P(F|Volta)", fV / V, .02); ok("P(F|Ampere)", fA / A, .05)
ok("P(Volta|F)", fV / 29, .48, 1e-2); ok("P(Ampere|F)", fA / 29, .52, 1e-2)
ok("P(F)", 29 / 1000, .029); ok("if independent: Volta faulty", 700 * .029, 20.3, .05); ok("if independent: Ampere faulty", 300 * .029, 8.7, .05)
ok("Bayes P(Ampere|F)", .05 * .30 / (.02 * .70 + .05 * .30), .52, 1e-2); ok("Bayes numerator", .05 * .30, .015); ok("Bayes denominator", .02 * .70 + .05 * .30, .029)

print("deck — block C")
x = np.array([4, 7, 3, 6, 5]); assert x.sum() == 25 and x.mean() == 5
dev = x - 5; assert dev.sum() == 0 and (dev ** 2).sum() == 10
ok("s^2 five weeks", x.var(ddof=1), 2.5); ok("s five weeks", x.std(ddof=1), 1.58)
vals = np.array([3, 4, 5, 6, 7]); P = np.array([.15, .20, .30, .20, .15]); assert isclose(P.sum(), 1)
ok("E(x) returns", (vals * P).sum(), 5.0); ok("sigma^2 returns", ((vals - 5) ** 2 * P).sum(), 1.6); ok("sigma returns", sqrt(1.6), 1.26)
assert np.allclose(vals * P, [.45, .80, 1.50, 1.20, 1.05]) and np.allclose((vals - 5) ** 2 * P, [.60, .20, 0, .20, .60])
ok("binomial 12,.25: P(3)", binom.pmf(3, 12, .25), .258); assert comb(12, 3) == 220
ok("binomial: .25^3", .25 ** 3, .0156, 1e-4); ok("binomial: .75^9", .75 ** 9, .0751, 1e-4)
ok("binomial mean", 12 * .25, 3); ok("binomial sigma", sqrt(12 * .25 * .75), 1.5)
ok("binomial P(0)", binom.pmf(0, 12, .25), .032); ok("binomial P(>=1)", 1 - binom.pmf(0, 12, .25), .968)
ok("Poisson mu 1.5: P(0)", poisson.pmf(0, 1.5), .223); ok("Poisson mu 3: P(0)", poisson.pmf(0, 3), .050)
ok("Poisson mu 3: P(>=1)", 1 - poisson.pmf(0, 3), .950); ok("Poisson mu 3: P(2)", poisson.pmf(2, 3), .224); ok("e^-3", exp(-3), .0498, 1e-4)
ok("miss at least one call in half an hour", 1 - poisson.pmf(0, 1.5), .777)

print("deck — block D")
mu, sg = 90, 8
for k, lo, hi, share in ((1, 82, 98, .683), (2, 74, 106, .954), (3, 66, 114, .997)):
    assert (mu - k * sg, mu + k * sg) == (lo, hi); ok(f"within {k} sigma", norm.cdf(k) - norm.cdf(-k), share)
ok("two sigma below: one in forty", norm.cdf(-2), .025, 3e-3)
ok("z for 75 km", (75 - mu) / sg, -1.875, 1e-9); ok("P(X<75) table z=-1.88", norm.cdf(-1.88), .030); ok("P(X<75) exact", norm.cdf(75, mu, sg), .030)
ok("z for 5%", norm.ppf(.05), -1.645); ok("guarantee x for 5%", mu + norm.ppf(.05) * sg, 76.8, .05); ok("1.645*8", 1.645 * 8, 13.2, .05)
ok("print 76: share below", norm.cdf(76, mu, sg), .040); ok("z for 76", (76 - mu) / sg, -1.75, 1e-9)
for xp, share in ((85, .27), (80, .11), (76.8, .05), (75, .03)):
    ok(f"print {xp}: share below", norm.cdf(xp, mu, sg), share, 6e-3)
ok("one rider in twenty-five", 1 / 25, .040)

print("drills")
# D1
assert comb(6, 2) == 15 and perm(6, 2) == 30 and perm(6, 2) == comb(6, 2) * 2 and 6 * 5 == 30 and 30 // 2 == 15
# D2
assert (int(.6 * 500), int(.03 * 300), int(.4 * 500), int(.06 * 200)) == (300, 9, 200, 12) and (291, 188, 479, 21) == (300 - 9, 200 - 12, 500 - 21, 9 + 12)
ok("D2 P(faulty|Rotor)", 9 / 300, .03); ok("D2 P(Rotor|faulty)", 9 / 21, .429); ok("D2 P(faulty)", 21 / 500, .042)
ok("D2 product test", .60 * .042, .0252, 1e-4); ok("D2 joint", 9 / 500, .018)
ok("D2 Bayes P(Spin|faulty)", .06 * .40 / (.03 * .60 + .06 * .40), .571); ok("D2 Bayes via counts", 12 / 21, .571)
ok("D2 P(faulty|Spin)", 12 / 200, .06); ok("D2 Bayes numerator", .06 * .40, .024, 1e-6); ok("D2 Bayes denominator", .03 * .60 + .06 * .40, .042, 1e-6)
# D3
c = np.array([2, 5, 3, 6, 4, 4]); assert c.sum() == 24 and c.mean() == 4 and (c - 4).sum() == 0 and ((c - 4) ** 2).sum() == 10
ok("D3 s^2", c.var(ddof=1), 2.0); ok("D3 s", c.std(ddof=1), 1.41)
ok("D3 binom 10,.3 P(2)", binom.pmf(2, 10, .3), .233); assert comb(10, 2) == 45; ok("D3 .7^8", .7 ** 8, .05765, 1e-4)
ok("D3 binom P(0)", binom.pmf(0, 10, .3), .028); ok("D3 binom P(>=1)", 1 - binom.pmf(0, 10, .3), .972)
ok("D3 binom mean", 10 * .3, 3); ok("D3 binom sigma", sqrt(10 * .3 * .7), 1.45); ok("D3 .3^2", .3 ** 2, .09, 1e-9); assert isclose(10 * .3 * .7, 2.1)
ok("D3 Poisson 4: P(0)", poisson.pmf(0, 4), .018); ok("D3 Poisson 4: P(2)", poisson.pmf(2, 4), .147); ok("D3 e^-4", exp(-4), .01832, 1e-4)
ok("D3 Poisson 1: P(0)", poisson.pmf(0, 1), .368); ok("D3 Poisson 1: P(>=1)", 1 - poisson.pmf(0, 1), .632)
# D4
ok("D4 P(X>270)", 1 - norm.cdf(1.5), .067); ok("D4 table .9332", norm.cdf(1.5), .9332, 1e-4)
ok("D4 P(220<X<260)", norm.cdf(1) - norm.cdf(-1), .683); ok("D4 .8413-.1587", .8413 - .1587, .6826, 1e-4)
ok("D4 table .8413", norm.cdf(1), .8413, 1e-4); ok("D4 table .1587", norm.cdf(-1), .1587, 1e-4)
ok("D4 z for top 10%", norm.ppf(.9), 1.28); ok("D4 flag threshold", 240 + 1.28 * 20, 265.6, .05)
ok("D4 1.28*20", 1.28 * 20, 25.6, 1e-9); ok("D4 z for 270", (270 - 240) / 20, 1.5, 1e-9)
ok("D4 table .8997 at z=1.28", norm.cdf(1.28), .8997, 6e-5); ok("D4 table .9015 at z=1.29", norm.cdf(1.29), .9015, 6e-5)
ok("D3 45*.09*.05765", 45 * .09 * .05765, .233, 1e-3); ok("D3 16*.01832/2", 16 * .01832 / 2, .147, 1e-3); ok("D3 e^-1", exp(-1), .368)
ok("D2 three-column: Rotor share of all faulty", .60 * .03, .018, 1e-9); ok("D2 three-column: Spin share of all faulty", .40 * .06, .024, 1e-9)

print("homework")
# H1
assert 240 - 60 == 180 and 140 + 80 - 180 == 40 and (140 - 40, 80 - 40) == (100, 40) and 100 + 40 + 40 + 60 == 240
ok("H1 P(T or F)", 140/240 + 80/240 - 40/240, .75); ok("H1 P(neither)", 60 / 240, .25)
assert comb(9, 4) == 126 and perm(9, 4) == 3024
# H2
assert (300, 12, 100, 10, 22) == (int(.75 * 400), int(.04 * 300), int(.25 * 400), int(.10 * 100), 12 + 10)
ok("H2 P(late|Fast)", 12 / 300, .04); ok("H2 P(Fast|late)", 12 / 22, .545); ok("H2 P(late)", 22 / 400, .055)
ok("H2 Bayes P(Local|late)", .10 * .25 / (.04 * .75 + .10 * .25), .4545); ok("H2 via counts", 10 / 22, .4545)
# H3
v = np.array([2, 3, 4, 5, 6]); p = np.array([.05, .30, .35, .20, .10]); assert isclose(p.sum(), 1)
E = (v * p).sum(); assert np.allclose(v * p, [.10, .90, 1.40, 1.00, .60]); ok("H3 E(x)", E, 4.0)
assert np.allclose(v - E, [-2, -1, 0, 1, 2]) and np.allclose((v - E) ** 2 * p, [.20, .30, 0, .20, .40])
ok("H3 variance", ((v - E) ** 2 * p).sum(), 1.10, 1e-9); ok("H3 sigma", sqrt(1.10), 1.049)
assert comb(15, 3) == 455; ok("H3 .2^3", .2 ** 3, .008, 1e-9); ok("H3 .8^12", .8 ** 12, .0687, 1e-4); ok("H3 455*.008", 455 * .008, 3.64, 1e-9)
ok("H3 binom 15,.2 P(3)", binom.pmf(3, 15, .2), .250); ok("H3 by hand", 455 * .008 * .0687, .250, 1e-3)
ok("H3 binom P(0) = .8^15", binom.pmf(0, 15, .2), .035); ok("H3 .8^15", .8 ** 15, .0352, 1e-4); ok("H3 binom P(>=1)", 1 - binom.pmf(0, 15, .2), .965)
ok("H3 binom mean", 15 * .2, 3); ok("H3 np(1-p)", 15 * .2 * .8, 2.4, 1e-9); ok("H3 binom sigma", sqrt(15 * .2 * .8), 1.549)
# H4
assert isclose(3 * 20 / 60, 1) and 3 * 2 == 6
ok("H4 mu 1: P(0)", poisson.pmf(0, 1), .368); ok("H4 mu 1: P(>=2)", 1 - poisson.cdf(1, 1), .264); ok("H4 mu 6: P(6)", poisson.pmf(6, 6), .161)
ok("H4 mu 1: P(1)", poisson.pmf(1, 1), .368); ok("H4 e^-1", exp(-1), .3679, 1e-4); ok("H4 P(>=2) by hand", 1 - .368 - .368, .264, 1e-9)
ok("H4 e^-6", exp(-6), .00248, 1e-5); assert 6 ** 6 == 46656 and 720 == 6 * 5 * 4 * 3 * 2 * 1; ok("H4 46656*.00248", 46656 * .00248, 115.7, .05); ok("H4 P(6) by hand", 46656 * .00248 / 720, .161, 1e-3)
# H5
ok("H5 P(X>100)", 1 - norm.cdf(100, 90, 8), .106); ok("H5 P(80<X<100)", norm.cdf(100, 90, 8) - norm.cdf(80, 90, 8), .789)
ok("H5 z for 100 km", (100 - 90) / 8, 1.25, 1e-9); ok("H5 table z=1.25", norm.cdf(1.25), .8944, 1e-4); ok("H5 table z=-1.25", norm.cdf(-1.25), .1056, 1e-4)
ok("H5 10% guarantee", 90 + norm.ppf(.10) * 8, 79.75, .05); ok("H5 10% guarantee, table z=-1.28", 90 - 1.28 * 8, 79.76, 1e-9); ok("H5 1.28*8", 1.28 * 8, 10.24, 1e-9)
ok("H5 table .8997 at z=1.28", norm.cdf(1.28), .8997, 6e-5); ok("H5 table .9015 at z=1.29", norm.cdf(1.29), .9015, 6e-5)
ok("H5 table .1003 at z=-1.28", norm.cdf(-1.28), .1003, 6e-5); ok("H5 table .0985 at z=-1.29", norm.cdf(-1.29), .0985, 6e-5); ok("H5 z for 79 km", (79 - 90) / 8, -1.375, 1e-9)
ok("H5 print 79: share below", norm.cdf(79, 90, 8), .085, 1e-3); ok("H5 P(weight<20)", norm.cdf(20, 22, 1.5), .091); ok("H5 P(weight<20), table z=-1.33", norm.cdf(-1.33), .092, 1e-3)
ok("H5 z for 20 kg", (20 - 22) / 1.5, -1.333, 1e-3); ok("H5 table z=-1.33", norm.cdf(-1.33), .0918, 1e-4); ok("H5 z for 10%", norm.ppf(.10), -1.28)
ok("H5 memo: sigma 12, 5% guarantee", 90 + norm.ppf(.05) * 12, 70.3, .05); ok("H5 memo: 1.645*12", 1.645 * 12, 19.74, 1e-9)
for xp, share in ((85, .27), (80, .11), (78, .07), (76, .04), (75, .03)):
    ok(f"memo: print {xp}, sigma 8: share below", norm.cdf(xp, 90, 8), share, 6e-3)
for xp, share in ((80, .20), (76, .12), (75, .11)):
    ok(f"memo: print {xp}, sigma 12: share below", norm.cdf(xp, 90, 12), share, 6e-3)

print("all week-7 numbers check out")

# standard normal table excerpt on the "Steps 3 and 4" slide, and the backwards lookup
for z, v in [(-2.0,.0228),(-1.9,.0287),(-1.8,.0359),(-1.7,.0446),(-1.6,.0548),(-2.08,.0188),(-1.98,.0239),(-1.88,.0301),(-1.78,.0375),(-1.68,.0465),(-1.64,.0505),(-1.65,.0495),(-1.84,.0329),(-1.85,.0322)]:
    ok(f"table z={z}", norm.cdf(z), v, 6e-5)
ok("P(X>75)", 1 - norm.cdf((75-90)/8), .970, 1e-3)
print("table excerpt ok")
