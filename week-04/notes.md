# Week 4 — Money has a date on it

**MBA03 Research & Quantitative Business Methods · Thu 15 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: simple and compound interest, compounding vs discounting, EAR, annuities and perpetuities, NPV (Renshaw ch. 10–13). *Beyond the syllabus:* the growing perpetuity (Gordon), as "what is Arno Bikes worth?".

A change of subject, not of method: from here the mathematics is arithmetic done carefully, and the discipline is that **every euro carries a date**.

## Learning objectives

By the end of the session the students can:

1. **Compute** a final amount under simple, periodic and continuous compounding, and say what each adds — resit's MCQ block.
2. **Convert** any nominal rate to an EAR and use it to compare two offers that look different — resit's MCQ block, and the single most useful skill of the module.
3. **Discount** a single sum, an annuity and a perpetuity, and explain why distant money is cheap — the machinery under every question that follows.
   Then **value a firm** as a growing perpetuity, `CF₁/(r − g)`, and say why the gap `r − g` is where the risk sits — beyond the syllabus, but it is the Board's favourite question.
4. **Lay out and compute an NPV**, state a decision from it, and say what IRR is and is not — the exam's financial-mathematics item and the register the midterm wants.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:15 | HW3 walkthrough | Paper | The Board report, read aloud by its author. Ask the room what they would cut. |
| 10:15–10:50 | **A. Interest and compounding** | Slides + clip → paper | Simple vs compound. More often is more. Where `e` comes from. |
| 10:50–11:10 | **B. The effective rate** | Slides → paper | EAR and the two-bank trap, on one slide. |
| 11:10–11:25 | break | — | Outside the room. |
| 11:25–12:10 | **C. Discounting** | Slides + figure → notebook → paper | PV, annuity, perpetuity. Why the rate matters more than the forecast. What is Arno Bikes worth (Gordon). |
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

### B. The effective rate (20')

**The line to leave on the board:** *a nominal rate is not a price until you know how often it compounds.*

One slide now: the table and the trap side by side. The table for 12% nominal: 12.36, 12.55, 12.68, 12.75 — read it, do not dwell. Then the trap, as a bet with hands up: **Bank A 7.8% monthly, Bank B 8% annually — which do you borrow from?** Almost everyone says A. A is 8.085%; B is 8.000%. The lower headline rate is the dearer loan.

Let that sit. It is the most directly useful thing in the module and it takes ninety seconds.

→ **D4, D5** on paper, 10 minutes. Insist that `m` is written down before any arithmetic.

### C. Discounting (45')

**Compounding runs the clock forward; discounting runs it back.** Same formula, read the other way. `10,000/(1.07)⁵ = €7,129.86`.

Show the discount-factor figure. At 3%, a euro in twenty years is worth 55 cents; at 16%, five cents. **Two analysts can agree on every cash flow and disagree entirely, because they disagreed about one number at the front.** Say that sentence slowly; it is the honest limitation of the whole method.

**Annuity and perpetuity**, as shortcuts, not as new theory. €12,000 a year for ten years at 6% is €88,321; for ever it is €200,000. Ask before revealing: "For ever, versus ten years — how many times more?" They guess large. It is 2.3 times. Everything after year ten is worth €111,679, because discounting shrinks distant money to nothing.

**What is Arno Bikes worth?** (10', beyond the syllabus.) A buyer asks for a price: €300k of free cash flow next year, growing 3% for ever, 9% cost of capital. Anchor first — with no growth it is the perpetuity just shown, €3.33M — then take the bet: *with 3% growth, how much?* Write the guesses up.

`300/(0.09 − 0.03) = €5M`. One line of intuition, no derivation: each year's PV is the previous one times 1.03/1.09, so the table is a geometric series and this is its sum; with `g = 0` it is `C/r` again. The first five years are only €1.23M of the €5M — the value of a firm lives in the far future.

Figure: 2% → €4.29M, 3% → €5M, 4% → €6M. **One point of growth is worth a million.** As `g → r` the value explodes — call it by name, a limit from week 2 — and the formula needs `g < r`. Close on the Board sentence: the gap `r − g` is a few points wide, and every point of doubt in it is a million on the price.

Notebook (optional, 2'): the slider over `g`, and watch the curve run up the asymptote.

→ **D8–D11** on paper, 15 minutes. D10 is the formula; D11 is the same question in Board form, and it ends with a sentence.

### D. NPV (35')

Back to the case. Lay the table out on the board **with a row for year 0 and a factor of 1** — the omitted year-0 row is the most common exam error in this topic.

NPV = +€318.94k. Return to the hands-up count from 10:15. The million becomes €319,000: still positive, still worth doing, **a third of what it looked like**. Adding flows from different years is the one thing this subject forbids.

**Clip — `w04_npv`.** The curve crossing zero. Then name it: IRR = 14.56%.

**What IRR is and is not.** It is the project's own break-even cost of money and a margin of safety — 9% against 14.6% is comfortable. It is not a ranking rule: compare two projects on IRR and you can pick the smaller one.

Notebook: slide the rate, watch the sign. Then the 🔍 CHECK — delay the first €700k by a year and predict whether IRR rises or falls *before* running it.

→ **D13, D14** on paper, 12 minutes.

### Board pitch (10')

A Board member has just said the line returns a million. Politely, with numbers and no formulas: why the flows cannot be added, what it is worth today, at what cost of capital the answer flips. This is the homework memo, rehearsed aloud.

## Key concepts (one line each)

- **Simple** interest pays on the principal; **compound** pays on the interest too.
- More frequent compounding always helps, and always by less; the ceiling is `e^i`.
- A nominal rate is not a price until you know `m`. **Compare on EAR.**
- Discounting is compounding read backwards. Distant money is cheap, and the rate decides how cheap.
- **Annuity** `C[1−(1+r)^−n]/r`; **perpetuity** `C/r`; **growing perpetuity** `CF₁/(r − g)`, only if `g < r`.
- A firm's value is next year's cash flow over `r − g`: a small denominator, so every doubt about growth is a large doubt about the price.
- Money with different dates **cannot be added**. Discount first, then add.
- **Accept when NPV > 0 at your own cost of capital.** IRR is where it crosses zero, and it is a margin of safety, not a ranking rule.

## Board, slide, screen — what goes where

**On the board.** The NPV table, built row by row with them reading out the factors — not
revealed finished. The EAR comparison of the two banks. The WACC calculation. Arithmetic
watched being done is arithmetic they can reproduce.

**On the slide.** The compounding table, the discount-factor figure, both clips, the annuity
and perpetuity formulas, the Gordon value-vs-growth figure.

**On screen.** Once: slide the discount rate and watch NPV cross zero. Then the check —
delay the first €700k by a year and have them predict which way IRR moves *before* running it.

This is the first session where the calculator matters. Check before block A ends that both
of them can do `(1.02)^16` and `e^0.12` on the machine they will bring to the exam. Someone
will not be able to, and 10:40 is a far better time to find out than the exam hall.

## Tutor's notes

- The two bets — the million, and the two banks — carry this session. Take the hands-up count both times and write it on the board; coming back to a number they committed to is what makes it stick.
- Calculators: this is the first session where they matter. Check everyone can do `(1.02)^16` and `e^0.12` before block A ends. Someone will not be able to, and it is better found at 10:40 than in the exam.
- The year-0 row and the factor of 1 are worth one minute of explicit attention.
- If ahead: D6 (continuous equivalent) and D12 (the growth the market is pricing in). If behind: drop D12 and D11 (c), keep D13 whole.
- Gordon is beyond the syllabus and not examined as such. If C runs long, cut the notebook slider, never the figure: "one point of growth is worth a million" is the line they will remember.
- Do not teach IRR before NPV, and do not let anyone leave preferring it. The syllabus lists NPV; IRR is here because the picture makes it free.
