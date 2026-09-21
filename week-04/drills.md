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

**D3 (core — resit form).** *Select the correct alternative and justify in one line.*
A bank quotes 6% nominal. Which is worth more to a depositor?
(i) compounded annually (ii) compounded monthly (iii) they are the same

## B. Effective annual rate

**D4 (core).** Compute the EAR for a 12% nominal rate compounded (a) semi-annually, (b) quarterly, (c) monthly, (d) continuously.

**D5 (core).** Bank A offers 7.8% compounded monthly. Bank B offers 8% compounded annually. Which do you borrow from, and why? Show the comparison you made.

**D6 (stretch).** A rate is quoted as 5% nominal compounded continuously. What annual compounding rate would leave a depositor equally well off?

## C. Discounting and present value

**D7 (core).** What is €10,000 receivable in 5 years worth today at 7%?

**D8 (core).** A supplier offers you two ways to pay for a €50,000 machine:
(i) €50,000 today; (ii) €18,000 at the end of each of the next three years.
Your cost of capital is 9%. Which do you choose? Show the present value of (ii).

**D9 (core — annuities and perpetuities).**
(a) An annuity pays €12,000 at the end of each year for 10 years. At 6%, what is it worth today?
(b) A perpetuity pays €12,000 at the end of every year for ever. At 6%, what is it worth today?
(c) Explain the gap between (a) and (b) in one sentence.

**D10 (stretch).** A perpetuity pays €5,000 next year and grows at 2% a year for ever. At 7%, what is it worth today?

## D. NPV

**D11 (core — the case).** For the assembly line above, at a cost of capital of 9%:
(a) Write the NPV as a sum.
(b) Compute each discounted flow and the NPV.
(c) Accept or reject, and say the sentence you would tell the Board.

**D11b (core — where the rate comes from).** Arno Bikes is financed 60% by equity and 40% by debt. Shareholders expect 12%; the bank charges 6%; the corporate tax rate is 25%.
(a) Compute the weighted average cost of capital.
(b) One line: why does the tax rate appear at all, and only on the debt side?
(c) If the firm took on more debt and the mix became 40/60, what would happen to the WACC and therefore to the NPV of the assembly line? No arithmetic needed.

**D12 (stretch).** Recompute the NPV at 16%. What does the change in sign tell you, and what is the name of the rate at which it happens?

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

**D8.** `PV(ii) = 18,000 × [1 − (1.09)⁻³]/0.09 = 18,000 × 2.531295 = **€45,563.31**`.
`45,563.31 < 50,000`, so **pay in instalments**: it costs about €4,437 less in today's money.

**D9.**
(a) `PV = 12,000 × [1 − (1.06)⁻¹⁰]/0.06 = 12,000 × 7.360087 = **€88,321.04**`.
(b) `PV = 12,000 / 0.06 = **€200,000.00**`.
(c) The perpetuity is worth more, but not infinitely more: the payments after year 10 are worth about €111,679 in total today, because discounting shrinks distant money towards nothing.

**D10.** Growing perpetuity: `PV = C₁/(r − g) = 5,000/(0.07 − 0.02) = **€100,000.00**`.

**D11.**
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

**D11b.**
(a) `WACC = 0.6(12%) + 0.4(6%)(1 − 0.25) = 7.2% + 1.8% = **9.0%**` — the 9% we were handed all along.
(b) Interest on debt is **deductible from taxable profit**, so a 6% loan costs the firm only `6%(1 − 0.25) = 4.5%` after tax. Dividends are not deductible, so no such factor appears on the equity side.
(c) More weight on the cheaper source → **WACC falls** → future cash flows are discounted less → **the NPV rises**. Worth saying out loud that this is not free: more debt raises the risk, and in time both `r_e` and `r_d` rise with it.

**D12.** At 16%: `−2,400 + 603.45 + 594.53 + 576.59 + 552.29 = **−€73.14k**`. Negative.
The NPV falls as the discount rate rises and **changes sign** between 9% and 16%; the rate where it is exactly zero is the **internal rate of return** (about 14.6% here). Above it the project destroys value.

</details>
