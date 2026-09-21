# Week 4 — Money has a date on it

**MBA03 Research & Quantitative Business Methods · Thu 15 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: simple and compound interest, compounding vs discounting, EAR, annuities and perpetuities, NPV (Renshaw ch. 10–13).

A change of subject, not of method: from here the mathematics is arithmetic done carefully, and the discipline is that **every euro carries a date**.

## Learning objectives

By the end of the session the students can:

1. **Compute** a final amount under simple, periodic and continuous compounding, and say what each adds — resit's MCQ block.
2. **Convert** any nominal rate to an EAR and use it to compare two offers that look different — resit's MCQ block, and the single most useful skill of the module.
3. **Discount** a single sum, an annuity and a perpetuity, and explain why distant money is cheap — the machinery under every question that follows.
4. **Lay out and compute an NPV**, state a decision from it, and say what IRR is and is not — the exam's financial-mathematics item and the register the midterm wants.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:15 | HW3 walkthrough | Paper | The Board report, read aloud by its author. Ask the room what they would cut. |
| 10:15–10:50 | **A. Interest and compounding** | Slides + clip → paper | Simple vs compound. More often is more. Where `e` comes from. |
| 10:50–11:20 | **B. The effective rate** | Slides → paper | EAR. The two-bank trap. |
| 11:20–11:35 | break | — | Outside the room. |
| 11:35–12:10 | **C. Discounting** | Slides + figure → notebook | PV, annuity, perpetuity. Why the rate matters more than the forecast. |
| 12:10–12:45 | **D. NPV** | Slides + clip → notebook → paper | The assembly line, decided. IRR. |
| 12:45–12:55 | Board pitch | Student at the board | Correct the Board member who added the flows. |
| 12:55–13:00 | Close | — | Homework brief. |

## Script

### A. Interest and compounding (35')

**Open with the case and the bet.** The assembly line: €2.4M out, €3.4M back over four years. "A million of profit — obviously we do it. Yes or no?" Take a show of hands and write the count on the board. Come back to it at 12:30.

**Simple vs compound.** €8,000 at 6% for three years: €9,440 vs €9,528.13. €88 over three years, and say the honest thing — over thirty years it is not €88. Simple interest is in the syllabus so they can *name* what compounding adds, not because anyone uses it.

**More often is more.** `A = P(1 + i/m)^(mt)`, and `m` is the number that matters. The bet: "€1,000 at 12%, compounded every single day instead of once. How much more than €1,120?" They over-guess, usually by a lot.

**Clip — `w04_compounding`.** 1,120 · 1,123.60 · 1,125.51 · 1,126.83 · 1,127.34 → 1,127.50. Seven euros from yearly to daily; three cents from daily to infinitely often.

Then `e`, and say why it belongs here: in week 1 it was "the base your calculator uses", and now it is the **ceiling on compounding**. That is the whole of continuous compounding, and the derivation is not needed.

### B. The effective rate (30')

**The line to leave on the board:** *a nominal rate is not a price until you know how often it compounds.*

The table for 12% nominal: 12.36, 12.55, 12.68, 12.75. Then the trap, as a bet with hands up: **Bank A 7.8% monthly, Bank B 8% annually — which do you borrow from?** Almost everyone says A. A is 8.085%; B is 8.000%. The lower headline rate is the dearer loan.

Let that sit. It is the most directly useful thing in the module and it takes ninety seconds.

→ **D4, D5** on paper, 12 minutes. Insist that `m` is written down before any arithmetic.

### C. Discounting (35')

**Compounding runs the clock forward; discounting runs it back.** Same formula, read the other way. `10,000/(1.07)⁵ = €7,129.86`.

Show the discount-factor figure. At 3%, a euro in twenty years is worth 55 cents; at 16%, five cents. **Two analysts can agree on every cash flow and disagree entirely, because they disagreed about one number at the front.** Say that sentence slowly; it is the honest limitation of the whole method.

**Annuity and perpetuity**, as shortcuts, not as new theory. €12,000 a year for ten years at 6% is €88,321; for ever it is €200,000. Ask before revealing: "For ever, versus ten years — how many times more?" They guess large. It is 2.3 times. Everything after year ten is worth €111,679, because discounting shrinks distant money to nothing.

→ **D8, D9** on paper, 12 minutes.

### D. NPV (35')

Back to the case. Lay the table out on the board **with a row for year 0 and a factor of 1** — the omitted year-0 row is the most common exam error in this topic.

NPV = +€318.94k. Return to the hands-up count from 10:15. The million becomes €319,000: still positive, still worth doing, **a third of what it looked like**. Adding flows from different years is the one thing this subject forbids.

**Clip — `w04_npv`.** The curve crossing zero. Then name it: IRR = 14.56%.

**What IRR is and is not.** It is the project's own break-even cost of money and a margin of safety — 9% against 14.6% is comfortable. It is not a ranking rule: compare two projects on IRR and you can pick the smaller one.

Notebook: slide the rate, watch the sign. Then the 🔍 CHECK — delay the first €700k by a year and predict whether IRR rises or falls *before* running it.

→ **D11, D12** on paper, 12 minutes.

### Board pitch (10')

A Board member has just said the line returns a million. Politely, with numbers and no formulas: why the flows cannot be added, what it is worth today, at what cost of capital the answer flips. This is the homework memo, rehearsed aloud.

## Key concepts (one line each)

- **Simple** interest pays on the principal; **compound** pays on the interest too.
- More frequent compounding always helps, and always by less; the ceiling is `e^i`.
- A nominal rate is not a price until you know `m`. **Compare on EAR.**
- Discounting is compounding read backwards. Distant money is cheap, and the rate decides how cheap.
- **Annuity** `C[1−(1+r)^−n]/r`; **perpetuity** `C/r`.
- Money with different dates **cannot be added**. Discount first, then add.
- **Accept when NPV > 0 at your own cost of capital.** IRR is where it crosses zero, and it is a margin of safety, not a ranking rule.

## Tutor's notes

- The two bets — the million, and the two banks — carry this session. Take the hands-up count both times and write it on the board; coming back to a number they committed to is what makes it stick.
- Calculators: this is the first session where they matter. Check everyone can do `(1.02)^16` and `e^0.12` before block A ends. Someone will not be able to, and it is better found at 10:40 than in the exam.
- The year-0 row and the factor of 1 are worth one minute of explicit attention.
- If ahead: D6 (continuous equivalent) and D10 (growing perpetuity). If behind: drop D10, keep D11 whole.
- Do not teach IRR before NPV, and do not let anyone leave preferring it. The syllabus lists NPV; IRR is here because the picture makes it free.
