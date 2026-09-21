# Week 3 — Studying a function, and adding one up

**MBA03 Research & Quantitative Business Methods · Thu 8 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: function study, optimisation, integration (Renshaw ch. 6–9, 18). **In-class quiz, per the syllabus.**

This is the midterm's mathematical content, entire. Say so at the start.

## Learning objectives

By the end of the session the students can:

1. **Carry out** the seven-step study of a function and produce a labelled sketch — this *is* the midterm's central question.
2. **Locate and classify** a stationary point using `f'` and the sign of `f''`, and state the classification in words — midterm Q2 and Q3.
3. **Solve** an optimisation problem where revenue is a log and cost a quadratic, and read `π'(q) = 0` as `MR = MC` — midterm Q3, resit's function study.
4. **Integrate** a fraction term by term and a definite integral producing a log, and explain why the integral of the marginal is the change in the total — two of the five items of the final's Q5.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:15 | HW2 walkthrough | Paper | One student at the board. Ask for the memo's sentence, not just the drill. |
| 10:15–10:50 | **A. The study, done properly** | Slides + clip → paper | Seven steps, in order, on a function they know. |
| 10:50–11:05 | break | — | Outside the room. |
| 11:05–11:45 | **B. Optimisation** | Slides + figure → notebook → paper | AC meets MC. `MR = MC`. The log-revenue firm. |
| 11:45–12:20 | **C. Integration** | Slides + clip → notebook → paper | Riemann sums. Two rules. The marginal-to-total sentence. |
| 12:20–12:40 | **Quiz** | Paper | 20 minutes, five items, weeks 1–3. |
| 12:40–12:52 | Board pitch | Student at the board | How much, how much profit, how much room for error. |
| 12:52–13:00 | Close | Paper | Homework brief: the midterm dry run. |

## Script

### A. The study, done properly (35')

**Open with the frame, not with mathematics:** "Everything the midterm asks you to do mathematically, you will do in the next thirty-five minutes. The rest is writing."

Put the **seven steps on the board and leave them there all morning**: domain, zeros, sign, stationary, nature, shape, sketch. Number them. Every drill from here refers to them by number.

**Clip — `w03_study`.** Play once. It shows the steps landing on `π(q)` in the exam's order. Then do it on the board with them talking, not you.

The two places marks are lost, named now:
- **Sketching first.** The sketch is step 7. A sketch drawn before the study is a guess with a ruler.
- **"Maximum" with no second derivative.** `f'` finds candidates; only `f''` says which kind. Writing "maximum" because the picture looks like a hill earns nothing.

Say the rule for `f''` in physical terms: **positive holds water, negative spills it.** Inflection is where the bending changes — in business, where growth stops accelerating.

→ **D1** on paper, 15 minutes. This is the midterm's Q2 with different numbers. Circulate and read what they write, not what they get.

### B. Optimisation (40')

**Opening bet:** show the AC/MC figure. "Marginal cost crosses average cost. Left of the minimum, at it, or right of it?" Most say "left". It is exactly at it.

Then show why, in words before algebra: **while the next unit costs less than the average, it drags the average down.** The average stops falling precisely when the next unit costs what the average costs. Then the arithmetic: `q ≈ 7.91`, `AC = MC = 9.32`.

**The rule that runs every firm.** `π'(q) = 0` is `R'(q) = C'(q)`. Write both forms side by side. Ask them to say it in English before you do.

The log-revenue firm: `30/(q+1) = 0.8q + 3` clears to `4q² + 19q − 135 = 0`, `q ≈ 3.90`. Walk the clearing step slowly — multiplying through by `(q+1)` is where the arithmetic goes wrong under exam pressure.

Notebook: raise the log coefficient 20 → 30 → 40 → 60 and watch the optimum move. **One of those rows has a positive optimum and a negative profit** (the 20 row: `q* = 2.81`, `π = −9.84k`). Stop there and ask what a manager does. The answer — the best you can do is still a loss, so the question becomes whether to operate at all — is worth more than the calculus.

Second slider: raise fixed cost 25 → 60. The optimum does not move. Ask why before explaining: a constant differentiates to zero, so fixed cost changes *how much* you make, never *how many*. This is a midterm-grade insight and a tariff question in disguise.

→ **D4, D5** on paper, 12 minutes.

### C. Integration (35')

**Opening question:** "The tenth bike costs €11, the eleventh €11.80. What do the first twenty cost together?" Let them propose adding them up. That is exactly right, and it is the integral.

**Clip — `w03_riemann`.** 180, 200, 212, 217 → 220. Thinner slices, truer area. Play once, then ask what the number is converging *to* and why it never quite arrives on screen.

**Two rules only:** the power rule and `1/q → ln|q|`. Then the exam's shape: the integral always arrives as a fraction, so **divide term by term first**; after that every piece is a power or a log. Drill this as a reflex, because under pressure people try to integrate the fraction whole.

**The sentence of the block:** `∫₁₀₀¹⁵⁰ π'(q) dq = π(150) − π(100) = €10,000`. Show both sides. *The integral of the marginal is the change in the total.* Write it on the board and leave it.

→ **D7, D8, D9** on paper, 15 minutes. D7 and D8 are exam items verbatim in form.

### Quiz (20')

Five items, one from each of: domain, limit, derivative-with-reading, stationary point with nature, integral. Announced in advance, not a trap. Collect, mark tonight, return next week with one line of feedback each.

Its purpose is diagnostic: it tells me who can compute and cannot interpret, which is the failure mode the midterm punishes.

### Board pitch (12')

The log-revenue firm. How much to produce, how much it makes, **and how much room for error**. The third question is the one that distinguishes a report from a calculation, and the midterm rewards it.

## Key concepts (one line each)

- The study has **seven steps in a fixed order**, and the sketch is the last one.
- `f'` finds the candidates; the **sign of `f''`** says maximum or minimum.
- `f'' > 0` convex, holds water; `f'' < 0` concave, spills it; sign change is an **inflection**.
- **Average cost is lowest where marginal cost crosses it** — not a coincidence, a definition.
- **Produce until marginal revenue equals marginal cost.**
- Fixed cost changes how much you earn, never how many you make.
- **The integral of the marginal is the change in the total.**

## Tutor's notes

- This session is full. The quiz is in the syllabus and cannot move; if the clock slips, shorten block C's drills, never the seven-step board work in block A.
- The negative-profit row in the notebook is the best teaching moment of the week. Do not rush past it to the next slider.
- Expect resistance to "sketch last". The habit of drawing first is strong and it costs marks. Say it three times.
- If the room is ahead: D3 (cubic with an inflection) and D6 (the box). If behind: D6 and D10 go, D1 and D7 stay.
- Mark the quiz the same evening while you can still remember who hesitated where. The pattern matters more than the score.
