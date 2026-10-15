# Week 4 — Drills

*Exam format. Show all work. Core items are for everyone; stretch items for whoever finishes early. Solutions at the end, worked the way an examiner wants to see them.*

Running case for weeks 4–5: **Arno Bikes is considering a new assembly line.** It costs €2.4M now and is expected to return €700k, €800k, €900k and €1,000k at the end of each of the next four years. The firm can borrow at 9%.

Round money to the cent, rates to two decimals in a percentage.

## A. Simple and compound interest

**D1 (core).** €8,000 is invested for 3 years at 6% a year.
(a) Simple interest: the final amount.
(b) Compounded annually: the final amount.
(c) The difference, and one sentence on where it comes from.

**D2 (core).** €5,000 for 4 years at 8% nominal, compounded quarterly.
(a) The final amount. (b) The interest earned.

**D2b (core — the rate moves).** €10,000 for eight years at 5%, compounded annually.
(a) The final amount.
(b) Recompute at 4% and at 6%. In euros, what is one point of interest worth over eight years? And over twenty?
(c) One sentence: why is the answer to (b) so much larger at twenty years than at eight?

**D3 (core — resit form).** *Select the correct alternative and justify in one line.*
A bank quotes 6% nominal. Which is worth more to a depositor?
(i) compounded annually (ii) compounded monthly (iii) they are the same

## B. Effective annual rate

**D4 (core).** Compute the EAR for a 12% nominal rate compounded (a) semi-annually, (b) quarterly, (c) monthly, (d) continuously.

**D5 (core).** Bank A offers 7.8% compounded monthly. Bank B offers 8% compounded annually. Which do you borrow from, and why? Show the comparison you made.

**D6 (stretch).** A rate is quoted as 5% nominal compounded continuously. What annual compounding rate would leave a depositor equally well off?

## C. Discounting, present value and growth

**D7 (core).** What is €10,000 receivable in 5 years worth today at 7%?

**D8 (core).** A supplier offers you two ways to pay for a €50,000 machine:
(i) €50,000 today; (ii) €18,000 at the end of each of the next three years.
Your cost of capital is 9%. Which do you choose? Show the present value of (ii).

**D9 (core — annuities and perpetuities).**
(a) An annuity pays €12,000 at the end of each year for 10 years. At 6%, what is it worth today?
(b) A perpetuity pays €12,000 at the end of every year for ever. At 6%, what is it worth today?
(c) Explain the gap between (a) and (b) in one sentence.

**D10 (core — growing perpetuity).** A perpetuity pays €5,000 next year and grows at 2% a year for ever. At 7%, what is it worth today?

**D11 (core — Board form).** Three years on, the Board asks again: *what is Arno Bikes worth?* The new forecast is a free cash flow of €350k next year, growing 4% a year for ever; the cost of capital is still 9%.
(a) The value of the firm today.
(b) By how much does the value change if growth is one point lower, 3% instead of 4%? In euros and in per cent.
(c) One sentence for the Board.

**D12 (stretch — what the market assumes).** A listed rival is valued by the market at €12M. Next year's free cash flow is €600k and its cost of capital is 9%.
(a) What growth rate for ever is the market pricing in?
(b) One line: is that believable for a mature firm, and what would you check?

## D. NPV

**D13 (core — the case).** For the assembly line above, at a cost of capital of 9%:
(a) Write the NPV as a sum.
(b) Compute each discounted flow and the NPV.
(c) Accept or reject, and say the sentence you would tell the Board.

**D13b (core — where the rate comes from).** Arno Bikes is financed 60% by equity and 40% by debt. Shareholders expect 12%; the bank charges 6%; the corporate tax rate is 25%.
(a) Compute the weighted average cost of capital.
(b) One line: why does the tax rate appear at all, and only on the debt side?
(c) If the firm took on more debt and the mix became 40/60, what would happen to the WACC and therefore to the NPV of the assembly line? No arithmetic needed.

**D14 (stretch).** Recompute the NPV at 16%. What does the change in sign tell you, and what is the name of the rate at which it happens?

## E. Challenge — the seven steps, on money

*Use the function-study procedure of week 3. Nothing here is new; the point is to see that these curves are functions like any other.*

**D15 (challenge).** `A(t) = 10,000 × 1.05^t`, for `t ≥ 0`.
(a) Domain, `A(0)`, and the limit as `t → ∞`.
(b) `A'(t)`. Its sign, and what it says. *(Hint: `d/dt aᵗ = aᵗ ln a`.)*
(c) `A''(t)`. Convex or concave? Is there an inflection?
(d) Compare with simple interest `S(t) = 10,000(1 + 0.05t)`: what is `S''`? Sketch both on the same axes, `t` from 0 to 30, marking `t = 0` and `t ≈ 14.2` where `A = 20,000`.

**D16 (challenge — the NPV curve as a function).** For the assembly line, `NPV(r) = −2,400 + 700/(1+r) + 800/(1+r)² + 900/(1+r)³ + 1,000/(1+r)⁴`, for `r ≥ 0`.
(a) `NPV(0)`. What does that number mean, and who said it this morning?
(b) The limit as `r → ∞`, and what it means. Is there a horizontal asymptote?
(c) Without computing it, say why `NPV'(r) < 0` for every `r`. *(Each term `CF/(1+r)ᵗ` has derivative `−t·CF/(1+r)^(t+1)`.)*
(d) Sign of `NPV(r)`: you know `NPV(0.09) = 318.94` and `NPV(0.16) = −73.14`. Where is the zero, roughly, and what is it called?
(e) Sketch: `NPV` against `r`, with the intercept, the zero and the asymptote. Then one sentence for the Board on what the sketch says about risk.

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**
(a) Simple: `8000(1 + 0.06 × 3) = 8000 × 1.18 = **€9,440.00**`.
(b) Compound: `8000(1.06)³ = 8000 × 1.191016 = **€9,528.13**`.
(c) Difference **€88.13**. Simple interest pays on the original €8,000 only; compounding pays interest on the interest already earned.

**D2.**
(a) `5000(1 + 0.08/4)^(4×4) = 5000(1.02)^16 = 5000 × 1.372786 = **€6,863.93**`.
(b) Interest `= **€1,863.93**`.

**D2b.**
(a) `10,000 × 1.05⁸ = 10,000 × 1.477455 = **€14,774.55**`.
(b) At 4%: `10,000 × 1.04⁸ = **€13,685.69**`; at 6%: `10,000 × 1.06⁸ = **€15,938.48**`. One point is worth about **€1,100** over eight years. Over twenty: 4% → €21,911.23, 5% → €26,532.98, 6% → €32,071.35: about **€4,600 to €5,500**.
(c) The rate sits in the base of a power with exponent `t`: a point of rate is multiplied by itself twenty times instead of eight. Small differences in the rate become large differences in the amount, and the longer the horizon the larger.

**D3.** **(ii) compounded monthly.** More frequent compounding earns interest on interest sooner, so the effective rate is higher: `(1 + 0.06/12)^12 − 1 = 6.17% > 6%`.

**D4.** `EAR = (1 + i/m)^m − 1`, and `e^i − 1` in the limit.
(a) `(1.06)² − 1 = **12.36%**`
(b) `(1.03)⁴ − 1 = **12.55%**`
(c) `(1.01)^12 − 1 = **12.68%**`
(d) `e^0.12 − 1 = **12.75%**`
The gaps shrink: that ceiling is where `e` comes from.

**D5.** Compare like with like, on EAR.
Bank A: `(1 + 0.078/12)^12 − 1 = (1.0065)^12 − 1 = 0.080850 = **8.085%**`.
Bank B: **8.00%**.
**Borrow from B.** A's lower quoted rate hides more frequent compounding, and once both are put on the same basis A is the dearer of the two. The nominal rate is not the price.

**D6.** `e^0.05 − 1 = **5.13%**`.

**D7.** `PV = 10,000 / (1.07)⁵ = 10,000 / 1.402552 = **€7,129.86**`.

**D8.** `PV(ii) = 18,000 × [1 − (1.09)⁻³]/0.09 = 18,000 × 2.5312955 = **€45,563.30**`.
`45,563.30 < 50,000`, so **pay in instalments**: it costs about €4,437 less in today's money.

**D9.**
(a) `PV = 12,000 × [1 − (1.06)⁻¹⁰]/0.06 = 12,000 × 7.360087 = **€88,321.04**`.
(b) `PV = 12,000 / 0.06 = **€200,000.00**`.
(c) The perpetuity is worth more, but not infinitely more: the payments after year 10 are worth about €111,679 in total today, because discounting shrinks distant money towards nothing.

**D10.** Growing perpetuity: `PV = C₁/(r − g) = 5,000/(0.07 − 0.02) = 5,000/0.05 = **€100,000.00**`.
With no growth the same €5,000 would be worth `5,000/0.07 = €71,428.57`: two points of growth cut the denominator from 7% to 5% and add 40% to the value.

**D11.**
(a) `V = CF₁/(r − g) = 350/(0.09 − 0.04) = 350/0.05 = **€7,000.00k**`, i.e. €7M.
(b) At 3%: `350/(0.09 − 0.03) = 350/0.06 = **€5,833.33k**`. The value falls by **€1,166.67k**, **−16.67%**. One point of growth moved the price by a sixth, because it made the denominator a fifth larger, from 5% to 6%, and `1/1.2 = 0.8333`.
(c) "On our forecast Arno Bikes is worth about €7M; if growth is one point lower it is worth €5.8M, so the price we accept should rest on the growth we can defend, not on the one we hope for."

**D12.**
(a) `P = CF₁/(r − g)` ⇒ `g = r − CF₁/P = 0.09 − 600/12,000 = 0.09 − 0.05 = **4.00%**`.
(b) 4% a year for ever is at the top of what a mature firm can sustain — roughly the economy's long-run nominal growth. Check whether recent cash-flow growth supports it, and remember the market price also embeds its own `r`: a lower `r` would need less growth to justify €12M.

**D13.**
(a) `NPV = −2,400 + 700/(1.09) + 800/(1.09)² + 900/(1.09)³ + 1,000/(1.09)⁴` (€ thousand).
(b)

| Year | Flow (€k) | Factor | Present value (€k) |
|---|---|---|---|
| 0 | −2,400 | 1.000000 | −2,400.00 |
| 1 | 700 | 0.917431 | 642.20 |
| 2 | 800 | 0.841680 | 673.34 |
| 3 | 900 | 0.772183 | 694.97 |
| 4 | 1,000 | 0.708425 | 708.43 |
| | | **NPV** | **+318.94** |

(c) **Accept.** "At our 9% cost of capital the line adds about €319,000 of value in today's money; the cash it returns covers the outlay by the end of year three."

**D13b.**
(a) `WACC = 0.6(12%) + 0.4(6%)(1 − 0.25) = 7.2% + 1.8% = **9.0%**` — the 9% we were handed all along.
(b) Interest on debt is **deductible from taxable profit**, so a 6% loan costs the firm only `6%(1 − 0.25) = 4.5%` after tax. Dividends are not deductible, so no such factor appears on the equity side.
(c) More weight on the cheaper source → **WACC falls** → future cash flows are discounted less → **the NPV rises**. Worth saying out loud that this is not free: more debt raises the risk, and in time both `r_e` and `r_d` rise with it.

**D14.** At 16%: `−2,400 + 603.45 + 594.53 + 576.59 + 552.29 = **−€73.14k**`. Negative.
The NPV falls as the discount rate rises and **changes sign** between 9% and 16%; the rate where it is exactly zero is the **internal rate of return** (about 14.6% here). Above it the project destroys value.

**D15.**
(a) Domain `[0, ∞)`. `A(0) = 10,000` — the principal. `lim (t→∞) A(t) = +∞`: there is no ceiling.
(b) `A'(t) = 10,000 × 1.05^t × ln 1.05 = A(t) × 0.04879 > 0` for every `t`: **always increasing**, and the increase is proportional to the amount already there — that *is* compounding.
(c) `A''(t) = A(t) × (ln 1.05)² > 0`: **convex throughout, no inflection**. The curve bends upward for ever: growth that keeps accelerating.
(d) `S''(t) = 0`: a straight line. Both start at 10,000 with almost the same slope (`S' = 500`, `A'(0) = 487.9`); then `A` pulls away. `A = 20,000` when `1.05^t = 2`, `t = ln 2 / ln 1.05 ≈ 14.2` years; at that point `S = 17,100`. At `t = 30`: `A = 43,219`, `S = 25,000`.

**D16.**
(a) `NPV(0) = −2,400 + 700 + 800 + 900 + 1,000 = **+1,000**`: the "million of profit" — it is what you get by adding the flows with no discounting at all, i.e. at a zero cost of money. The Board member was computing NPV at `r = 0`.
(b) `lim (r→∞) NPV(r) = **−2,400**`: every future flow is discounted to nothing and only the outlay remains. **`y = −2,400` is a horizontal asymptote.**
(c) Each term `CF/(1+r)ᵗ` falls as `r` rises (its derivative `−t·CF/(1+r)^(t+1)` is negative, since `CF > 0`); the constant `−2,400` differentiates to zero. A sum of negatives is negative: **`NPV` is decreasing for every `r`**, so it crosses zero exactly once.
(d) `NPV` is positive at 9% and negative at 16%, so the zero lies between; it is at **`r ≈ 14.6%`**, the **internal rate of return**. Sign: `NPV > 0` for `r < 14.6%`, `NPV < 0` above.
(e) A falling, convex curve from `(0, 1,000)` through `(0.09, 318.94)` and `(0.146, 0)`, flattening towards `−2,400`. Board sentence: "The project stays worth doing for any cost of money up to 14.6%; our 9% leaves about five and a half points of room, and the curve is steepest exactly where we are, so each point of rate costs us roughly €80k of value."
</details>
