# Week 3 — Drills

*Exam format. Show all work. Core items are for everyone; stretch items for whoever finishes early. Solutions at the end, worked the way an examiner wants to see them.*

The seven-point study, in the order the midterm expects it:
**domain → zeros → sign → stationary points → nature (max/min) → shape (convexity, inflection) → sketch.**

## A. The full study of a function

**D1 (core — the midterm rehearsal).** Study `π(q) = −4q² + 1200q − 60,000` completely and sketch it.
Give: domain, zeros, sign line, `π'` and the stationary point, `π''` and its nature, behaviour as `q → ∞`, and a labelled sketch.

**D2 (core).** A cost function: `C(q) = 0.4q² + 3q + 25` (€ thousand), for `q ≥ 0`.
(a) Domain, and `C(0)`. What is `C(0)` called?
(b) Average cost `AC(q) = C(q)/q`. Find its domain and `lim (q→0⁺) AC(q)` and `lim (q→∞) AC(q)`.
(c) Minimise `AC(q)`. At that quantity, compute `AC` and `C'(q)` and comment on what you notice.

**D3 (stretch).** `f(q) = q³ − 12q² + 36q` on `[0, 10]`.
(a) Stationary points and their nature. (b) Inflection point. (c) Sketch.

## B. Optimisation, and what it is for

**D4 (core).** A second firm: `R(q) = 30 ln(q + 1)`, `C(q) = 0.4q² + 3q + 25`, both in € thousand, `q ≥ 0`.
(a) Write `π(q)`.
(b) Write `π'(q)`.
(c) Solve `π'(q) = 0`. Leave it as an equation in `q` first, then solve the quadratic it becomes.
(d) Confirm with `π''` that it is a maximum.
(e) Is the firm profitable at that quantity? Answer with a number.

**D5 (core — the managerial reading).** For the firm in D4, `R'(q)` is marginal revenue and `C'(q)` is marginal cost.
(a) Write the condition `π'(q) = 0` as `R'(q) = C'(q)`, in words.
(b) At `q = 2` compute both. Which is larger, and what should the firm do?

**D6 (stretch).** A box with a square base and no lid must hold 32 m³. Minimise the material used. *(Surface `S = x² + 4xh`, volume `x²h = 32`.)*

## C. Integration

**D7 (core — exam form).** Evaluate, splitting term by term:
(a) `∫ (q⁵ − 3q³ + 2)/q² dq`
(b) `∫ (4q³ − 6q + 5) dq`
(c) `∫ (2/q + 3√q) dq`

**D8 (core — exam form).** Find `f(q)` given `f'(q) = 12q² − 6q + 1` and `f(2) = 20`.

**D8b (core — exam form, and the one that catches people).** Find `f(x)` given `f'(x) = 12x² − 4x` and **`f(−3) = 17`**. Watch every sign.

**D8c (core — the third rule).** Evaluate, by asking first whether the top is the derivative of the bottom:
(a) `∫ 1/(q − 4) dq`   (b) `∫ q/(q² + 5) dq`   (c) `∫ (2q + 3)/(q² + 3q − 1) dq`   (d) `∫ 5/(2q + 1) dq`

**D9 (core).** Evaluate the definite integrals and say what each measures:
(a) `∫₀²⁰ (0.8q + 3) dq` where `0.8q + 3` is marginal cost.
(b) `∫₁⁴ (6/q) dq`. Leave the answer in terms of `ln`.

**D9b (core — exam form).** Evaluate `∫₀^(1/2) [ 1/(x − 1) + x/(x² − 1) ] dx`, leaving the answer in terms of `ln`. Both terms are logs; neither is `1/x`.

**D10 (stretch).** Marginal profit is `π'(q) = 1200 − 8q`. The firm currently makes 100 bikes.
(a) By how much does profit change if output rises from 100 to 150? Compute it as a definite integral.
(b) Check your answer against `π(150) − π(100)` using `π(q) = −4q² + 1200q − 60,000`.

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**
- **Domain.** A polynomial: all of `ℝ`. For a quantity, `[0, +∞)`.
- **Zeros.** `−4q² + 1200q − 60,000 = 0`; divide by `−4`: `q² − 300q + 15,000 = 0`.
  `Δ = 90,000 − 60,000 = 30,000`, `√Δ ≈ 173.2`. `q = (300 ± 173.2)/2` → **`q ≈ 63.4` and `q ≈ 236.6`**.
- **Sign.** `a = −4 < 0`, so positive between the roots: `π > 0` on `(63.4, 236.6)`, negative outside.
- **Stationary point.** `π'(q) = −8q + 1200 = 0` → **`q = 150`**.
- **Nature.** `π''(q) = −8 < 0` for every `q`, so the stationary point is a **maximum**; the curve is concave everywhere. `π(150) = −90,000 + 180,000 − 60,000 = **€30,000**`.
- **Behaviour.** `lim (q→∞) π(q) = −∞`: the `−4q²` term wins. There is no "sell more forever".
- **Sketch.** Downward parabola, crossing the axis at 63.4 and 236.6, peak `(150, 30,000)`, intercept `π(0) = −60,000`. Label all four.

**D2.**
(a) `[0, +∞)`; `C(0) = 25`. That is **fixed cost**: what the firm pays having produced nothing.
(b) `AC(q) = 0.4q + 3 + 25/q`, domain `(0, +∞)` — zero output has no average.
  `lim (q→0⁺) AC = +∞` (fixed cost spread over almost nothing).
  `lim (q→∞) AC = +∞` (the `0.4q` term takes over). So `AC` falls, then rises: it has a minimum.
(c) `AC'(q) = 0.4 − 25/q² = 0` → `q² = 62.5` → **`q ≈ 7.91`**.
  `AC(7.91) = 3.16 + 3 + 3.16 = **9.32**`; `C'(7.91) = 0.8(7.91) + 3 = **9.32**`.
  **They are equal.** Average cost is at its lowest exactly where marginal cost crosses it. Worth stating out loud: it is not a coincidence, it is what "average" means.

**D3.**
(a) `f'(q) = 3q² − 24q + 36 = 3(q² − 8q + 12) = 3(q − 2)(q − 6)` → `q = 2, 6`.
  `f''(q) = 6q − 24`: `f''(2) = −12 < 0` → **maximum**, `f(2) = 8 − 48 + 72 = 32`.
  `f''(6) = 12 > 0` → **minimum**, `f(6) = 216 − 432 + 216 = 0`.
(b) `f'' = 0` at **`q = 4`**, `f(4) = 64 − 192 + 144 = 16`; the curvature changes sign there, so it is an inflection.
(c) Rises to `(2, 32)`, falls to `(6, 0)`, rises again; at `q = 10`, `f = 1000 − 1200 + 360 = 160`.

**D4.**
(a) `π(q) = 30 ln(q + 1) − 0.4q² − 3q − 25`.
(b) `π'(q) = 30/(q + 1) − 0.8q − 3`.
(c) `30/(q + 1) = 0.8q + 3`. Multiply by `(q + 1)`:
  `30 = (0.8q + 3)(q + 1) = 0.8q² + 3.8q + 3` → `0.8q² + 3.8q − 27 = 0`.
  Multiply by 5: `4q² + 19q − 135 = 0`. `Δ = 361 + 2160 = 2521`, `√Δ ≈ 50.21`.
  `q = (−19 ± 50.21)/8` → **`q ≈ 3.90`** (the negative root is discarded: a quantity).
(d) `π''(q) = −30/(q + 1)² − 0.8 < 0` everywhere → **maximum**.
(e) `π(3.90) = 30 ln(4.90) − 0.4(15.21) − 3(3.90) − 25 = 47.68 − 6.08 − 11.70 − 25 = **€4.89k**`. Profitable, but only just — the window is narrow, which is the point.

**D5.**
(a) `π' = R' − C' = 0` means `R'(q) = C'(q)`: **produce up to the point where the revenue from one more unit equals what that unit costs.**
(b) `R'(2) = 30/3 = **10**`; `C'(2) = 0.8(2) + 3 = **4.6**`. Marginal revenue is larger, so each extra unit still adds `10 − 4.6 = 5.4` — **produce more**, up to `q ≈ 3.90`.

**D6.** `h = 32/x²`, so `S = x² + 4x(32/x²) = x² + 128/x`.
`S' = 2x − 128/x² = 0` → `x³ = 64` → **`x = 4`**, `h = 2`. `S'' = 2 + 256/x³ > 0` → minimum. `S = 16 + 32 = **48 m²**`.

**D7.**
(a) Split first: `(q⁵ − 3q³ + 2)/q² = q³ − 3q + 2q⁻²`.
  `∫ = q⁴/4 − 3q²/2 − 2/q + c`.
(b) `q⁴ − 3q² + 5q + c`.
(c) `∫ 2/q dq = 2 ln|q|`; `∫ 3q^{1/2} dq = 3 · (2/3) q^{3/2} = 2q^{3/2}`. Total: `2 ln|q| + 2q^{3/2} + c`.
*The exam's integral is always this shape: divide term by term first, then each term is a power or a log.*

**D8.** `f(q) = 4q³ − 3q² + q + c`. `f(2) = 32 − 12 + 2 + c = 20` → `c = −2`.
**`f(q) = 4q³ − 3q² + q − 2`**.

**D8b.** `f(x) = 4x³ − 2x² + c`. Now substitute carefully:
`f(−3) = 4(−27) − 2(9) + c = −108 − 18 + c = −126 + c = 17` → `c = 143`.
**`f(x) = 4x³ − 2x² + 143`**.
*The trap is `(−3)³ = −27` and `(−3)² = +9`. Two signs, two marks.*

**D8c.** Ask each time: is the top the derivative of the bottom?
(a) bottom differentiates to 1 → **`ln|q − 4| + c`**.
(b) bottom differentiates to `2q`, top is `q`, so a factor `½` is missing → **`½ ln(q² + 5) + c`**. (No modulus needed: `q² + 5 > 0` always.)
(c) bottom differentiates to `2q + 3`, which is exactly the top → **`ln|q² + 3q − 1| + c`**.
(d) bottom differentiates to 2, top is 5, so `5/2` comes out → **`(5/2) ln|2q + 1| + c`**.

**D9.**
(a) `[0.4q² + 3q]₀²⁰ = 160 + 60 = **220**`. Total variable cost of the first 20 bikes: adding up marginal cost gives total cost.
(b) `[6 ln q]₁⁴ = 6 ln 4 − 6 ln 1 = **6 ln 4 ≈ 8.32**`.

**D9b.** Each term is a log.
`∫ 1/(x−1) dx = ln|x−1|`; `∫ x/(x²−1) dx = ½ ln|x²−1|`.
So the antiderivative is `ln|x−1| + ½ ln|x²−1|`, and

`at ½ :  ln(½) + ½ ln(¾) = −0.6931 + ½(−0.2877) = −0.8370`
`at 0 :  ln 1 + ½ ln 1 = 0`

**`= −0.8370`**, or exactly `ln(½) + ½ ln(¾)`.
*Note the modulus: between 0 and ½ both `x − 1` and `x² − 1` are negative, and without the absolute value the logs are undefined. The exam's model answer expects it.*

**D10.**
(a) `∫₁₀₀¹⁵⁰ (1200 − 8q) dq = [1200q − 4q²]₁₀₀¹⁵⁰ = (180,000 − 90,000) − (120,000 − 40,000) = 90,000 − 80,000 = **€10,000**`.
(b) `π(150) = 30,000`; `π(100) = −40,000 + 120,000 − 60,000 = 20,000`. Difference `= **€10,000**`. ✔
The integral of the marginal is the change in the total. That sentence is the whole of integration.

</details>
