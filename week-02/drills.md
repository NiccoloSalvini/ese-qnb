# Week 2 — Drills

*Exam format. Show all work. Core items are for everyone; stretch items for whoever finishes early. Solutions at the end, worked the way an examiner wants to see them.*

## A. Reading a function

**D1 (core).** For each function, state the **domain** as an interval and say what the restriction means for the firm.
(a) `f(q) = √(q − 20)` — profit per bike above a minimum run.
(b) `g(q) = ln(q − 5)` — a log revenue that only starts once five units are sold.
(c) `h(q) = 120 / (q − 40)` — average fixed cost per bike above capacity 40.

**D2 (core).** Arno Bikes faces demand `p(q) = 1600 − 4q`.
(a) Write revenue `R(q)` and simplify.
(b) Write profit `π(q)` using `C(q) = 60,000 + 400q`.
(c) Evaluate `π(100)` and `π(200)`. Which quantity is better, and by how much?

**D3 (stretch).** A second firm has `R(q) = 30 ln(q + 1)` (€ thousand) and `C(q) = 0.4q² + 3q + 25`.
(a) State the domain of `R` for `q ≥ 0`.
(b) Compute `π(5)` and `π(10)` to two decimals.

## B. Limits

**D4 (core).** Evaluate, showing the factoring step:
(a) `lim (q→10) (q² − 100)/(q − 10)`
(b) `lim (q→3) (q² − 5q + 6)/(q − 3)`

**D5 (core — exam form).** Evaluate the one-sided limit `lim (q→1⁺) (q − 1)²/(q − q²)`.
*Hint: factor the denominator first. Note the sign of each factor as q approaches 1 from above.*

**D6 (core).** Evaluate the limits at infinity and say what each means for the firm:
(a) `lim (q→∞) (1200q − 4q²)/(q² )`
(b) `lim (q→∞) (60,000 + 400q)/q` — average cost per bike as the run gets long.

**D7 (stretch).** `lim (q→−∞) (3q³ − 2q + 1)/(5q³ + q²)`.

## C. The derivative

**D8 (core).** Differentiate, term by term:
(a) `π(q) = −4q² + 1200q − 60,000`
(b) `C(q) = 0.4q² + 3q + 25`
(c) `R(q) = 30 ln(q + 1)`
(d) `f(q) = 5q³ − 2q² + 7q − 1`

**D8b (core — one inside another).** Differentiate, naming the inside each time:
(a) `ln(q + 1)`   (b) `ln(5q)`   (c) `(3q − 4)⁵`   (d) `e^(0.08t)`   (e) `20 ln(2q + 7)`

**D9 (core — the point of the week).** For `π(q) = −4q² + 1200q − 60,000`:
(a) Compute `π'(80)` and say, in one sentence a manager would use, what it means.
(b) Compute `π'(200)` and do the same.
(c) Solve `π'(q) = 0`. Compare with the vertex you found in week 1.

**D10 (stretch).** Using the definition, `f'(a) = lim (h→0) [f(a+h) − f(a)]/h`, show that the derivative of `f(q) = 3q²` at `q = a` is `6a`.

## D. Reversing the derivative

**D11 (core — exam form).** Find `f(q)` given `f'(q) = 6q² − 2q` and `f(1) = 4`.

**D12 (core).** Find the total cost function given marginal cost `MC(q) = 0.8q + 3` and fixed cost `C(0) = 25`.

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**
(a) Need `q − 20 ≥ 0` → **`[20, +∞)`**. Below 20 bikes the formula has no meaning: the firm does not operate under a 20-bike run.
(b) Need `q − 5 > 0` (strict: `ln 0` is undefined) → **`(5, +∞)`**. Revenue only exists past the fifth unit.
(c) Need `q − 40 ≠ 0` → **`(−∞, 40) ∪ (40, +∞)`**; for a quantity, `[0, 40) ∪ (40, +∞)`. At exactly capacity the expression blows up — the model breaks there.

**D2.**
(a) `R(q) = (1600 − 4q)q = 1600q − 4q²`.
(b) `π(q) = 1600q − 4q² − 60,000 − 400q = −4q² + 1200q − 60,000`.
(c) `π(100) = −40,000 + 120,000 − 60,000 = €20,000`. `π(200) = −160,000 + 240,000 − 60,000 = €20,000`.
**Equal.** Two different quantities, the same profit — the parabola is symmetric about `q = 150`. Say this out loud: "more" is not the question, "where on the hill" is.

**D3.**
(a) `q + 1 > 0` → `q > −1`, so for a quantity the whole of **`[0, +∞)`**.
(b) `π(5) = 30 ln 6 − (0.4·25 + 15 + 25) = 53.75 − 50 = €3.75k`.
`π(10) = 30 ln 11 − (40 + 30 + 25) = 71.94 − 95 = −€23.06k`.
The second firm is past its best scale at 10.

**D4.**
(a) `(q² − 100)/(q − 10) = (q − 10)(q + 10)/(q − 10) = q + 10 → **20**`.
(b) `(q² − 5q + 6)/(q − 3) = (q − 3)(q − 2)/(q − 3) = q − 2 → **1**`.

**D5.** Factor: `(q − 1)² / (q(1 − q))`. Now `1 − q = −(q − 1)`, so the expression is
`(q − 1)² / (−q(q − 1)) = −(q − 1)/q`.
As `q → 1⁺`, `(q − 1) → 0⁺` and `q → 1`, so the value → `−0 = **0**`.
*The exam wants the factoring and the sign discussion written out, not just the answer.*

**D6.**
(a) Divide numerator and denominator by `q²`: `(1200/q − 4)/1 → **−4**`. Far out, profit falls like `−4q²`: the quadratic term dominates and the firm is deep in loss.
(b) `(60,000 + 400q)/q = 60,000/q + 400 → **400**`. Average cost per bike settles at the variable cost: fixed cost spreads to nothing. This is economies of scale in one line.

**D7.** Divide by `q³`: `(3 − 2/q² + 1/q³)/(5 + 1/q) → **3/5**`.

**D8.**
(a) `π'(q) = −8q + 1200`
(b) `C'(q) = 0.8q + 3`
(c) `R'(q) = 30/(q + 1)`
(d) `f'(q) = 15q² − 4q + 7`

**D8b.** Outside first, inside untouched, then times the inside's derivative.
(a) inside `q + 1`, derivative 1 → **`1/(q+1)`**. The multiplication by 1 is why this one looks free.
(b) inside `5q`, derivative 5 → `(1/5q)·5 = **1/q**`. (Also visible from `ln 5q = ln 5 + ln q`, and `ln 5` is a constant.)
(c) outside `(·)⁵`, inside `3q − 4`, derivative 3 → `5(3q−4)⁴·3 = **15(3q−4)⁴**`.
(d) inside `0.08t`, derivative 0.08 → **`0.08 e^(0.08t)`**.
(e) inside `2q + 7`, derivative 2 → `20 · (1/(2q+7)) · 2 = **40/(2q+7)**`.

**D9.**
(a) `π'(80) = −640 + 1200 = **+560**`. At 80 bikes a month, one more bike adds about €560 to profit. Make more.
(b) `π'(200) = −1600 + 1200 = **−400**`. At 200 bikes, one more bike *costs* about €400 of profit. Make fewer.
(c) `−8q + 1200 = 0` → **`q = 150`**, exactly the vertex `−b/2a` from week 1. The formula worked because the curve was a parabola; the derivative works whatever the curve.

**D10.**
`[3(a+h)² − 3a²]/h = [3a² + 6ah + 3h² − 3a²]/h = (6ah + 3h²)/h = 6a + 3h`.
As `h → 0` this → **`6a`**. Divide *before* letting `h` go: that is the whole trick.

**D11.** Antiderivative term by term: `f(q) = 2q³ − q² + c`.
Then `f(1) = 2 − 1 + c = 4` → `c = 3`, so **`f(q) = 2q³ − q² + 3`**.
*Never forget the constant: the initial condition is what pins it down, and the exam always gives you one.*

**D12.** `C(q) = 0.4q² + 3q + c`, and `C(0) = c = 25`, so **`C(q) = 0.4q² + 3q + 25`**.
The constant of integration *is* the fixed cost. That is not a coincidence; it is the economics.

</details>
