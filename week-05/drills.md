# Week 5 — Drills

*Exam format. Show all work. Core items are for everyone; stretch items for whoever finishes early. Solutions at the end, worked the way an examiner wants to see them.*

Running case: **Arno Bikes holds a small bond portfolio** as a cash reserve, and is asked by the Board whether rising rates should worry it.

Unless stated otherwise: annual coupons, face value €100, prices to the cent.

## A. Pricing a bond

**D1 (core).** A 5-year bond, 4% annual coupon, face €100, yield 6%.
(a) Write the price as a sum.
(b) Compute it.
(c) Is it at a premium or a discount, and why — in one sentence, without arithmetic?

**D2 (core).** The same bond at a yield of 4%. Then at 2%.
(a) Both prices.
(b) State the rule that connects coupon, yield and price.

**D3 (core — resit form).** *Select the correct alternative and justify in one line.*
A bond trades **above** par. Therefore:
(i) its coupon is above its yield (ii) its yield is above its coupon (iii) it must be close to maturity

**D4 (core).** A zero-coupon bond pays €100 in 8 years. The yield is 5%.
(a) Its price today. (b) If the yield rises to 6%, the new price and the percentage change.

## B. Duration

**D5 (core).** For the 5-year 4% bond priced at a 6% yield (D1):
(a) Compute Macaulay duration, showing the weight of each cash flow.
(b) Convert it to modified duration.
(c) Estimate the price change if the yield rises by 50 basis points.

**D6 (core).** A 10-year bond with a 5% coupon trades at par (yield 5%). Its modified duration is 7.72.
(a) Estimate the new price if the yield rises to 6%.
(b) The actual price at 6% is €92.64. Compare, and say which way the estimate errs.

**D7 (stretch).** Without computing anything, order these three by duration, longest first, and justify each comparison in one clause:
(i) a 10-year zero-coupon bond (ii) a 10-year 8% coupon bond (iii) a 3-year 8% coupon bond

## C. Convexity

**D8 (core).** Using the bond in D6 (`P = 100`, `D_mod = 7.72`, convexity `C = 75.0`):
(a) Estimate the price at a yield of 6% using duration **and** convexity.
(b) Compare with the actual €92.64 and with the duration-only estimate from D6.

**D9 (core — the Board sentence).** In two sentences, no formulas: what does convexity buy the holder of a bond, and why does a risk manager care about it?

**D10 (stretch).** Two bonds have the same duration; one has higher convexity. Rates move sharply, direction unknown. Which would you rather hold, and why?

*The session closes with a [mock of the final exam's calculus question](mock_exam.md), thirty minutes in exam conditions.*

## D. Putting it together

**D11 (core).** Arno Bikes holds €400,000 of the D6 bond (at par) and €600,000 of a 2-year bond with modified duration 1.90.
(a) The portfolio's modified duration. *(Weight each by market value.)*
(b) The estimated loss in euros if yields rise by 1% across the board.
(c) One sentence to the Board.

## E. Immunisation — beyond the syllabus

*The step after duration: using it to make a payment safe. A zero's Macaulay duration is its maturity; yields are flat and move once, the day after purchase.*

**D12 (core).** Arno Bikes must pay a supplier **€500,000 in exactly 3 years**. It can buy 1-year and 5-year zero-coupon bonds, both yielding 4%.
(a) How much must it set aside today?
(b) What share goes into each zero so that the portfolio's duration is 3 years?
(c) The euros in each, and the amount each zero pays at maturity.

**D13 (core).** The day after the purchase in D12, yields jump to **5%** and stay there.
(a) The 1-year zero's payment, reinvested at 5% until year 3: what is it worth then?
(b) The 5-year zero, still two years from maturity at year 3: what is it worth then?
(c) The total against the €500,000 owed. Then repeat (a)–(c) with yields falling to **3%** instead, and say what you notice.

**D14 (stretch).** Go back to the slide: €1M due in 4 years, flat yield 5%, money set aside today €822,702.47. Replace the 6-year zero with a **6-year 5% coupon bond at par**.
(a) Its Macaulay duration, with the table of weights.
(b) The share in the 2-year zero that makes the portfolio's duration 4 years, and the euros in each.
(c) One year later, yields unchanged: the payment is 3 years away, and the coupon bond is now a 5-year 5% bond at par, with Macaulay duration 4.55. By how much did each duration fall? What must the treasurer do, and how often?

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**
(a) `P = Σ(t=1..5) 4/(1.06)^t + 100/(1.06)^5`.
(b) Annuity part: `4 × [1 − (1.06)⁻⁵]/0.06 = 4 × 4.212364 = 16.85`. Face: `100/(1.06)⁵ = 74.73`.
  `P = **€91.58**`.
(c) A **discount**: the bond pays 4% on its face while the market demands 6%, so it must be cheaper than face to make up the difference.

**D2.**
(a) At 4%: coupon equals yield, so `P = **€100.00**` (par).
  At 2%: `4 × [1 − (1.02)⁻⁵]/0.02 + 100/(1.02)⁵ = 4 × 4.713460 + 90.573 = 18.854 + 90.573 = **€109.43**`.
(b) **Coupon > yield → premium; coupon = yield → par; coupon < yield → discount.** Price and yield move in opposite directions, always.

**D3.** **(i) its coupon is above its yield.** Investors pay more than face only to obtain a coupon better than the going rate.

**D4.**
(a) `P = 100/(1.05)⁸ = 100/1.477455 = **€67.68**`.
(b) `P = 100/(1.06)⁸ = 100/1.593848 = **€62.74**`; change `= (62.74 − 67.68)/67.68 = **−7.30%**`.

**D5.**
(a) With `P = 91.58`:

| t | CF | PV = CF/(1.06)^t | weight w = PV/P | t · w |
|---|---|---|---|---|
| 1 | 4 | 3.77 | 0.0412 | 0.0412 |
| 2 | 4 | 3.56 | 0.0389 | 0.0777 |
| 3 | 4 | 3.36 | 0.0367 | 0.1100 |
| 4 | 4 | 3.17 | 0.0346 | 0.1384 |
| 5 | 104 | 77.71 | 0.8486 | 4.2432 |
| | | **91.58** | **1.0000** | **4.611** |

**Macaulay duration = 4.61 years.** It is the average time to being repaid, weighted by present value — which is why it is under five even though the bond runs five years.
(b) `D_mod = D/(1 + y) = 4.611/1.06 = **4.350**`.
(c) `ΔP/P ≈ −D_mod × Δy = −4.350 × 0.005 = −2.18%`, i.e. about `−€1.99`, giving roughly **€89.59**.

**D6.**
(a) `ΔP/P ≈ −7.72 × 0.01 = −7.72%` → `P ≈ 100 × 0.9228 = **€92.28**`.
(b) The actual price is **€92.64**, so the estimate is **€0.36 too low**. Duration alone **overstates the loss**. It will also understate the gain when yields fall: the straight line lies below the curve on both sides.

**D7.** **(i) > (ii) > (iii).**
(i) beats (ii): a zero pays everything at the end, so its weighted average time is the full 10 years, while coupons pull (ii)'s average forward.
(ii) beats (iii): same coupon, but money returned over ten years instead of three.

**D8.**
(a) `ΔP/P ≈ −D_mod Δy + ½ C (Δy)² = −7.72(0.01) + ½(75.0)(0.0001) = −0.0772 + 0.00375 = −0.07345`
  → `P ≈ 100 × 0.92655 = **€92.66**`.
(b) Duration alone gave €92.28, out by 36 cents *below* the truth. Adding convexity gives €92.66, out by 2 cents *above* it. The second term recovers almost all of the curvature the straight line missed; the 2 cents that remain belong to the next term again, and no one on a trading floor cares about them.

**D9.** Convexity means the price curve bends away from the straight-line estimate in the holder's favour: when yields fall the bond gains more than duration predicts, and when they rise it loses less. A risk manager cares because a duration-only report overstates losses and understates gains, and because between two bonds of equal duration the more convex one is worth more when rates move a long way.

**D10.** The **more convex** one. With equal duration the two behave the same for a small move, but for a large move in either direction the convex bond does better: more upside, less downside. That asymmetry is worth paying for, and in the market you usually do.

**D11.**
(a) Weights `400/1,000 = 0.4` and `600/1,000 = 0.6`.
  `D_portfolio = 0.4(7.72) + 0.6(1.90) = 3.088 + 1.140 = **4.228**`.
(b) `ΔV ≈ −4.228 × 0.01 × €1,000,000 = **−€42,280**`.
(c) "A one-point rise in yields costs the reserve about €42,000, a little over 4% of it; about three quarters of the exposure sits in the ten-year holding, and shortening that would cut it roughly in half."

**D12.**
(a) `PV = 500,000/(1.04)³ = 500,000/1.124864 = **€444,498.18**`.
(b) Each zero's duration is its maturity. With a share `w` in the 1-year zero:
  `1·w + 5(1 − w) = 3 → 5 − 4w = 3 → **w = ½**`. Half in each.
(c) `€222,249.09` in each.
  The 1-year zero pays `222,249.09 × 1.04 = **€231,139.05**` in year 1.
  The 5-year zero pays `222,249.09 × (1.04)⁵ = **€270,400.00**` in year 5.

**D13.**
(a) `231,139.05 × (1.05)² = 231,139.05 × 1.1025 = **€254,830.80**`.
(b) `270,400.00/(1.05)² = 270,400.00/1.1025 = **€245,260.77**`.
(c) `254,830.80 + 245,260.77 = **€500,091.57**`, i.e. **€91.57 more** than the €500,000 owed.
  At 3%: `231,139.05 × 1.0609 = 245,215.42` and `270,400.00/1.0609 = 254,877.93`, total **€500,093.35**, **€93.35 more**.
  In both directions the reinvestment effect and the price effect cancel, and what is left over is a small **gain**: that is convexity, on the holder's side again. Without the match — all in the 1-year zero — a fall to 3% would leave `444,498.18 × 1.04 × 1.0609 = €490,430.84`, about €9,570 short.

**D14.**
(a) At par, `P = 100`:

| t | CF | PV = CF/(1.05)^t | weight w = PV/P | t · w |
|---|---|---|---|---|
| 1 | 5 | 4.76 | 0.0476 | 0.0476 |
| 2 | 5 | 4.54 | 0.0454 | 0.0907 |
| 3 | 5 | 4.32 | 0.0432 | 0.1296 |
| 4 | 5 | 4.11 | 0.0411 | 0.1645 |
| 5 | 5 | 3.92 | 0.0392 | 0.1959 |
| 6 | 105 | 78.35 | 0.7835 | 4.7012 |
| | | **100.00** | **1.0000** | **5.330** |

**Macaulay duration = 5.33 years**, under six because the coupons come back earlier.
(b) With a share `w` in the 2-year zero: `2w + 5.33(1 − w) = 4 → w = (5.33 − 4)/(5.33 − 2) = 1.33/3.33 = **0.40**`.
  About **40% in the zero (€328,509)** and **60% in the coupon bond (€494,193)**. Less in the short bond than on the slide, because the long bond is now shorter than six years.
(c) The payment's date fell by exactly **1 year** (4 → 3); the 2-year zero's duration too (2 → 1). The coupon bond's fell by only `5.33 − 4.55 = **0.78**`. So even with rates unchanged, durations drift apart as time passes and the match is lost. The treasurer must **re-compute the weights and rebalance**, in practice at least once a year and after any large rate move: immunisation is a routine, not a one-off purchase.

</details>
