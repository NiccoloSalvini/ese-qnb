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

**D2b (core — asymptotes, in the resit's own form).** `f(x) = x² − 3x + 7 ln(x + 3)`.
(a) State the domain as an interval.
(b) Evaluate `lim (x→−3⁺) f(x)` and say what it tells you about the graph.
(c) Evaluate `lim (x→+∞) f(x)`.
(d) Sketch the shape, marking the asymptote.

**D3 (stretch).** `f(q) = q³ − 12q² + 36q` on `[0, 10]`.
(a) Stationary points and their nature. (b) Inflection point. (c) Sketch.

**D3b (core — step 6 on its own).** `f(q) = q³ − 6q² + 9q + 4`, for `q ≥ 0`.
(a) Compute `f''(q)` and solve `f''(q) = 0`.
(b) Give the sign of `f''` on each side of that point and name the intervals: convex where, concave where.
(c) The inflection point, with both coordinates.
(d) The stationary points, and the nature of each one — using `f''`, not a sketch.
(e) One sentence a report would use for step 6.

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

## D. When the world moves the curve: tariffs

*Added on 22 October, not covered in class: self-study for the midterm, with the addendum at the end of the week-3 slides.*

**D11 (core — the brief's tariff question, different numbers).** A firm has `R(q) = 60 ln(q + 1)` and `C(q) = 0.25q² + 5q + 30`, € thousand, `q ≥ 0`. Of the €5k that one more unit costs, €4k is a component imported from outside the EU. The EU imposes a **20% tariff** on it.
(a) Say which term of `C` the tariff moves, which it leaves alone, and why. Write the new cost `C_t(q)`.
(b) Find the profit-maximising output before and after the tariff. Confirm each is a maximum with `π''`.
(c) Profit at each optimum, and the change in euro and in percent.
(d) Check (c) in your head: tariff per unit × output. Why is the exact loss a little smaller?
(e) One sentence for the Board.

**D12 (core — a zero by bisection).** For the firm of D11 *with* the tariff, `π_t(q) = 60 ln(q + 1) − 0.25q² − 5.8q − 30`.
(a) Show that `π_t` changes sign between `q = 0.75` and `q = 0.8`, and between `q = 14` and `q = 14.5`.
(b) Halve each interval until you can state both break-even outputs to one decimal place.
(c) Before the tariff the break-evens were `0.76` and `15.57`. What happened to the profitable window?

**D13 (optional — the small-nation model).** A small open economy: demand `Q_d = 120 − 2p`, domestic supply `Q_s = 3p − 30` (`Q` in thousand units, `p` in €). The world price is €20.
(a) Price and quantity with no trade (autarky).
(b) Under free trade: quantity bought, made at home, imported.
(c) A tariff of €5 a unit. The same three quantities.
(d) Compute, as integrals or as areas: the loss of consumer surplus, the gain of domestic producers, the tariff revenue, and the two triangles — the protective and the consumption effect. Check that they add up.
(e) What is the deadweight loss, and what does it mean in one sentence?

**D14 (stretch — writing).** In 150–200 words for a Board, explain why a tariff hurts a small open economy *more* than the triangles of D13 suggest. Find the channels yourself, and support each with a source you have actually read.

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

**D2b.**
(a) `ln(x + 3)` needs `x + 3 > 0`, so the domain is **`(−3, +∞)`** — open, because `ln 0` is undefined.
(b) As `x → −3⁺`, `ln(x+3) → −∞`, and `x² − 3x → 18`, so `f(x) → **−∞**`. The line **`x = −3` is a vertical asymptote**: the curve plunges down it.
(c) As `x → +∞` the `x²` term dominates everything, so `f(x) → **+∞**`.
(d) `f'(x) = 2x − 3 + 7/(x + 3) = (2x − 1)(x + 2)/(x + 3)`, zero at `x = −2` and `x = ½`. So the curve comes up from `−∞` along `x = −3`, reaches a **local maximum** at `(−2, 10)`, dips to a **local minimum** at `(½, ≈ 7.52)`, then rises to `+∞`. Two turns, not one. Draw the asymptote as a dashed vertical line: the marker looks for it.

**D3.**
(a) `f'(q) = 3q² − 24q + 36 = 3(q² − 8q + 12) = 3(q − 2)(q − 6)` → `q = 2, 6`.
  `f''(q) = 6q − 24`: `f''(2) = −12 < 0` → **maximum**, `f(2) = 8 − 48 + 72 = 32`.
  `f''(6) = 12 > 0` → **minimum**, `f(6) = 216 − 432 + 216 = 0`.
(b) `f'' = 0` at **`q = 4`**, `f(4) = 64 − 192 + 144 = 16`; the curvature changes sign there, so it is an inflection.
(c) Rises to `(2, 32)`, falls to `(6, 0)`, rises again; at `q = 10`, `f = 1000 − 1200 + 360 = 160`.

**D3b.**
(a) `f'(q) = 3q² − 12q + 9`, `f''(q) = 6q − 12`. `f'' = 0` at **`q = 2`**.
(b) `f''(1) = −6 < 0`: **concave on `[0, 2)`**. `f''(3) = 6 > 0`: **convex on `(2, ∞)`**. The sign changes, so `q = 2` is a genuine inflection and not just a zero.
(c) `f(2) = 8 − 24 + 18 + 4 = 6`: **inflection at `(2, 6)`**. Both coordinates, or the point is not located.
(d) `f'(q) = 3(q − 1)(q − 3) = 0` → `q = 1, 3`. `f''(1) = −6 < 0` → **maximum**, `f(1) = 8`. `f''(3) = 6 > 0` → **minimum**, `f(3) = 4`. Max at 1, inflection at 2, min at 3: the inflection sits *between* the turning points, where the fall is steepest.
(e) "The curve is concave up to `q = 2` and convex beyond it, with an inflection at `(2, 6)`: the decline that begins at the maximum is steepest there, and slows afterwards until the minimum at `q = 3`."

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

**D11.**
(a) The tariff raises what the firm **pays per unit for the component**: `4 × 0.20 = €0.8k` more per unit. That is the linear term, `5q → 5.8q`. The quadratic term `0.25q²` is the plant's internal cost of running harder (overtime, congestion), not a purchase: untouched. The fixed cost `30` does not depend on output: untouched. **`C_t(q) = 0.25q² + 5.8q + 30`.** Revenue unchanged, assuming the firm cannot raise its price.
(b) Before: `π'(q) = 60/(q + 1) − 0.5q − 5 = 0` → `60 = (0.5q + 5)(q + 1) = 0.5q² + 5.5q + 5` → `q² + 11q − 110 = 0`. `Δ = 121 + 440 = 561`, `√Δ ≈ 23.685`, **`q* = (−11 + 23.685)/2 ≈ 6.34`** (the negative root is outside the domain).
After: `60 = (0.5q + 5.8)(q + 1) = 0.5q² + 6.3q + 5.8` → `q² + 12.6q − 108.4 = 0`. `Δ = 158.76 + 433.6 = 592.36`, `√Δ ≈ 24.339`, **`q_t* = (−12.6 + 24.339)/2 ≈ 5.87`**.
Both: `π''(q) = −60/(q + 1)² − 0.5 < 0` for every `q ≥ 0`, so each is a **maximum** (≈ −1.61 and −1.77).
(c) `π(6.34) = 60 ln 7.34 − 0.25(6.34)² − 5(6.34) − 30 ≈ **47.85**`; `π_t(5.87) ≈ **42.97**`. Change **−€4.88k, −10.2%**.
(d) `0.8 × 6.34 ≈ 5.07`. The exact loss is smaller because the firm cuts output by half a unit and stops paying the tariff on what it no longer makes.
(e) "The tariff costs us about €4.9k a month, a tenth of our profit; we should produce about 5.9 units instead of 6.3."

**D12.**
(a) `π_t(0.75) ≈ −0.91`, `π_t(0.8) ≈ +0.47`; `π_t(14) ≈ +2.28`, `π_t(14.5) ≈ −2.21`. Each pair has opposite signs, so `π_t` crosses zero inside each interval (it is continuous there).
(b) Lower: `π_t(0.775) ≈ −0.22` → between 0.775 and 0.8; `π_t(0.7875) ≈ +0.13` → between 0.775 and 0.7875. Every number in there rounds to **`q ≈ 0.8`** (exact 0.783). Upper: `π_t(14.25) ≈ +0.06` → between 14.25 and 14.5; `π_t(14.3) ≈ −0.39` → between 14.25 and 14.3: **`q ≈ 14.3`** (exact 14.257).
(c) From `[0.76, 15.57]` to `[0.78, 14.26]`: the window shrinks, mostly at the top. At high output the tariff is paid on many units, so the firm stops covering its costs much sooner.

**D13.**
(a) `120 − 2p = 3p − 30` → `p = 30`, `Q = 60`.
(b) At `p = 20`: bought `Q_d = 80`, made at home `Q_s = 30`, imported **50**.
(c) At `p = 25`: bought `70`, made at home `45`, imported **25**.
(d) `ΔCS = ∫₂₀²⁵ (120 − 2p) dp = [120p − p²]₂₀²⁵ = 2375 − 2000 = **375**`.
`ΔPS = ∫₂₀²⁵ (3p − 30) dp = [1.5p² − 30p]₂₀²⁵ = 187.5 − 0 = **187.5**`.
Revenue `= 5 × 25 = **125**`.
Protective effect `= ½ × 5 × (45 − 30) = **37.5**`; consumption effect `= ½ × 5 × (80 − 70) = **25**`.
Check: `187.5 + 125 + 37.5 + 25 = 375` ✔ (all in € thousand).
(e) Deadweight loss `= 37.5 + 25 = **62.5**`: the part of the consumers' loss that nobody gains — production done at home at more than the world price, and purchases that no longer happen.

**D14.** No model answer, on purpose: finding and judging the sources is the exercise. Check your paragraph against the method: each channel named precisely, a recent and reliable source cited Harvard, the way it reaches a firm's costs or revenue, the direction, and what a Board should do. At least one channel should come back to the cost function of D11. Wikipedia is not a source.

</details>
