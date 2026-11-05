"""Numerical check of every number in the week-6 deck, drills and homework (Arno Bikes). Run: python3.11 lectures/check_w06.py"""
from math import comb, perm, sqrt, isclose
import numpy as np
from scipy.stats import norm

def ok(name, got, want, tol=5e-3):
    assert isclose(got, want, abs_tol=tol), f"{name}: got {got:.5f}, want {want}"
    print(f"  ok  {name:<46} {got:.4f}")

print("deck — bridge")
ok("stock 110, sigma 5: share of months run out", 1 - norm.cdf(110, 100, 5), .023)
ok("stock 110, sigma 20: share of months run out", 1 - norm.cdf(110, 100, 20), .309)
assert 60000 / (1000 - 400) == 100  # break-even, weeks 1-5

print("deck — block A")
both = 120 + 90 - (200 - 40); assert both == 50
assert (120 - both, both, 90 - both, 40) == (70, 50, 40, 40) and 70 + 50 + 40 + 40 == 200
ok("P(both)", both / 200, .25); ok("P(A)", 120 / 200, .60); ok("P(S)", 90 / 200, .45)
ok("addition law P(A or S)", 120/200 + 90/200 - both/200, .80); ok("complement", 1 - .80, .20)
assert np.allclose(np.array([70, 50, 40, 40]) / 200, [.35, .25, .20, .20])
assert comb(8, 3) == 56 and perm(8, 3) == 336 and perm(8, 3) == comb(8, 3) * 6 and 8 * 7 * 6 == 336
from math import factorial; assert factorial(3) == 6 and factorial(8) == 40320 and 336 // 6 == 56
print("  ok  C(8,3)=56, P(8,3)=336, 3!=6, 8!=40320")

print("deck — block B")
V, A = 700, 300; fV, fA = int(.02 * V), int(.05 * A); assert (fV, fA) == (14, 15) and fV + fA == 29
assert (V - fV, A - fA, 1000 - 29) == (686, 285, 971)
ok("P(F|Volta)", fV / V, .02); ok("P(F|Ampere)", fA / A, .05)
ok("P(Volta|F)", fV / 29, .48, 1e-2); ok("P(Ampere|F)", fA / 29, .52, 1e-2)
ok("P(F)", 29 / 1000, .029)
ok("Bayes numerator", .05 * .30, .015, 1e-6); ok("Bayes Volta cell", .02 * .70, .014, 1e-6)
ok("Bayes denominator", .02 * .70 + .05 * .30, .029, 1e-6)
ok("Bayes P(Ampere|F)", .05 * .30 / (.02 * .70 + .05 * .30), .52, 1e-2); ok("Bayes P(Volta|F)", .014 / .029, .48, 1e-2)

print("deck — block C")
x = np.array([4, 7, 3, 6, 5]); assert x.sum() == 25 and x.mean() == 5
dev = x - 5; assert dev.sum() == 0 and list(dev) == [-1, 2, -2, 1, 0] and list(dev ** 2) == [1, 4, 4, 1, 0] and (dev ** 2).sum() == 10
ok("s^2 five weeks", x.var(ddof=1), 2.5); ok("s five weeks", x.std(ddof=1), 1.58)
vals = np.array([3, 4, 5, 6, 7]); P = np.array([.15, .20, .30, .20, .15]); assert isclose(P.sum(), 1)
assert np.allclose(P * 20, [3, 4, 6, 4, 3])  # twenty weeks of history
ok("E(x) returns", (vals * P).sum(), 5.0); ok("sigma^2 returns", ((vals - 5) ** 2 * P).sum(), 1.6); ok("sigma returns", sqrt(1.6), 1.26)
assert np.allclose(vals * P, [.45, .80, 1.50, 1.20, 1.05]) and np.allclose((vals - 5) ** 2 * P, [.60, .20, 0, .20, .60])
ok("over 50 weeks", 50 * 5.0, 250, 1e-9)
assert vals.max() == 7  # "eight or more has not happened in twenty weeks"

print("drills")
# D1
both1 = 95 + 70 - (150 - 25); assert both1 == 40 and (95 - 40, 40, 70 - 40, 25) == (55, 40, 30, 25) and 55 + 40 + 30 + 25 == 150
ok("D1 P(T)", 95 / 150, .633); ok("D1 P(F)", 70 / 150, .467); ok("D1 P(both)", 40 / 150, .267)
ok("D1 P(T or F)", 95/150 + 70/150 - 40/150, .833); ok("D1 at least one, as count", 125 / 150, .833)
assert comb(7, 2) == 21 and perm(7, 2) == 42 and 7 * 6 == 42 and 42 // 2 == 21 and perm(7, 2) == comb(7, 2) * 2
# D2
assert (int(.6 * 500), int(.4 * 500)) == (300, 200) and (round(.04 * 300), round(.01 * 200)) == (12, 2)
assert (300 - 12, 200 - 2, 12 + 2, 500 - 14) == (288, 198, 14, 486)
ok("D2 P(faulty|Ohm)", 12 / 300, .04); ok("D2 P(faulty|Watt)", 2 / 200, .01); ok("D2 P(faulty)", 14 / 500, .028)
ok("D2 P(Ohm|faulty)", 12 / 14, .857); ok("D2 P(Watt|faulty)", 2 / 14, .143)
ok("D2 Bayes numerator", .04 * .60, .024, 1e-6); ok("D2 Watt cell", .01 * .40, .004, 1e-6); ok("D2 denominator", .04 * .60 + .01 * .40, .028, 1e-6)
ok("D2 Bayes P(Ohm|faulty)", .04 * .60 / (.04 * .60 + .01 * .40), .857); ok("D2 Bayes P(Watt|faulty)", .004 / .028, .143)
# D3
c = np.array([3, 8, 5, 6, 8]); assert c.sum() == 30 and c.mean() == 6
dc = c - 6; assert list(dc) == [-3, 2, -1, 0, 2] and dc.sum() == 0 and list(dc ** 2) == [9, 4, 1, 0, 4] and (dc ** 2).sum() == 18
ok("D3 s^2", c.var(ddof=1), 4.5); ok("D3 s", c.std(ddof=1), 2.12)
v3 = np.array([0, 1, 2, 3, 4]); p3 = np.array([.10, .20, .40, .20, .10]); assert isclose(p3.sum(), 1)
assert np.allclose(v3 * p3, [0, .20, .80, .60, .40]); ok("D3 E(x)", (v3 * p3).sum(), 2.0)
assert np.allclose((v3 - 2) ** 2 * p3, [.40, .20, 0, .20, .40]); ok("D3 sigma^2", ((v3 - 2) ** 2 * p3).sum(), 1.20); ok("D3 sigma", sqrt(1.20), 1.10)

print("homework")
# H1
bothH = 110 + 75 - (180 - 30); assert bothH == 35 and (110 - 35, 35, 75 - 35, 30) == (75, 35, 40, 30) and 75 + 35 + 40 + 30 == 180
ok("H1 P(H or L)", 110/180 + 75/180 - 35/180, .833); ok("H1 P(H or L) as count", 150 / 180, .833); ok("H1 P(neither)", 30 / 180, .167)
ok("H1 P(H)", 110 / 180, .611); ok("H1 P(L)", 75 / 180, .417); ok("H1 P(both)", 35 / 180, .194)
assert comb(10, 3) == 120 and perm(10, 3) == 720 and perm(10, 3) == comb(10, 3) * 6
# H2
assert (int(.65 * 2000), int(.35 * 2000)) == (1300, 700) and (round(.03 * 1300), round(.08 * 700)) == (39, 56)
assert (1300 - 39, 700 - 56, 39 + 56, 2000 - 95) == (1261, 644, 95, 1905)
ok("H2 P(faulty|Celle)", 39 / 1300, .03); ok("H2 P(faulty|Ionix)", 56 / 700, .08); ok("H2 P(faulty)", 95 / 2000, .0475, 1e-6)
ok("H2 P(Celle|faulty)", 39 / 95, .411); ok("H2 P(Ionix|faulty)", 56 / 95, .589)
ok("H2 Bayes numerator", .08 * .35, .028, 1e-6); ok("H2 Celle cell", .03 * .65, .0195, 1e-6); ok("H2 denominator", .03 * .65 + .08 * .35, .0475, 1e-6)
ok("H2 Bayes P(Ionix|faulty)", .08 * .35 / (.03 * .65 + .08 * .35), .589)
# H3
w = np.array([12, 9, 15, 10, 14, 12]); assert w.sum() == 72 and w.mean() == 12
dw = w - 12; assert list(dw) == [0, -3, 3, -2, 2, 0] and dw.sum() == 0 and (dw ** 2).sum() == 26
ok("H3 s^2", w.var(ddof=1), 5.2); ok("H3 s", w.std(ddof=1), 2.28)
vH = np.array([1, 2, 3, 4, 5]); pH = np.array([.10, .25, .30, .25, .10]); assert isclose(pH.sum(), 1)
assert np.allclose(vH * pH, [.10, .50, .90, 1.00, .50]); ok("H3 E(x)", (vH * pH).sum(), 3.0)
assert np.allclose((vH - 3) ** 2 * pH, [.40, .25, 0, .25, .40]); ok("H3 sigma^2", ((vH - 3) ** 2 * pH).sum(), 1.30); ok("H3 sigma", sqrt(1.30), 1.14)

print("all week-6 numbers check out")
