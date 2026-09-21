# Week 5 — What a rate rise costs you

**MBA03 Research & Quantitative Business Methods · Thu 22 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: bond pricing, duration and convexity (Renshaw ch. 10–13). Plus consolidation and a **mock of the final exam's calculus question**.

Last session of my half. It closes the loop deliberately: a bond is last week's arithmetic, duration is week 2's derivative, convexity is week 3's second derivative.

## Learning objectives

By the end of the session the students can:

1. **Price** a plain coupon bond and say, without arithmetic, whether it trades at a premium or a discount — resit's MCQ block.
2. **Compute** Macaulay and modified duration from a table of weights, and use modified duration to estimate a price change — resit's MCQ block.
3. **State** how maturity, coupon and yield move duration, and why — resit's MCQ block.
4. **Add** the convexity term, say which way duration alone errs, and explain in plain words what convexity buys the holder.
5. **Sit** the five-item calculus question under exam conditions and mark it.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:12 | HW4 walkthrough | Paper | The memo. Ask whether the Board member would accept it. |
| 10:12–10:40 | **A. Pricing a bond** | Slides → paper | Annuity plus lump sum. Premium, par, discount. |
| 10:40–11:20 | **B. Duration** | Slides + figure + clip → paper | The slope. Two durations. Three rules. |
| 11:20–11:35 | break | — | Outside the room. |
| 11:35–12:05 | **C. Convexity** | Slides + clip → notebook → paper | The gap the line misses. The reserve, answered. |
| 12:05–12:45 | **D. Mock exam** | Paper, exam conditions | Forty minutes, `mock_exam.md`, no notes. |
| 12:45–13:00 | Marking together, and handover | Paper | Mark it, then what happens next. |

## Script

### A. Pricing a bond (28')

**Open with the Board's question**, and promise the answer by 12:05: the firm holds €1M in bonds, rates may rise a point, should it worry?

**A bond is a promise with dates on it.** An annuity of coupons plus a lump sum at the end — both priced last week. Nothing new. Price the 5-year 4% at a 6% yield: `16.85 + 74.73 = €91.58`.

**The bet, answered without arithmetic:** why is it below 100? Because it pays 4% on its face while the market wants 6%, so the only way to deliver 6% is to sell it cheaper. Get that sentence from a student, not from yourself.

Then the table: coupon > yield premium, = par, < discount. And the rule with no exceptions: **price and yield move in opposite directions.**

→ **D1, D2, D3** on paper, 12 minutes. Annuity part and redemption part shown separately, always.

### B. Duration (40')

**Show the price–yield figure first.** The thing to notice is that it is a **curve**. Everything in this block and the next follows from that one fact.

**Clip — `w05_duration`.** The tangent at par, `dP/dy = −772`, `D_mod = 7.72`. Say it as the Board hears it: *a one-point rise costs about 7.7% of value.*

**Two durations, and keep them apart.** Macaulay is the average time to being repaid, in **years**. Modified is Macaulay divided by `(1+y)`, and it is a **sensitivity in % per %**. Students conflate them; the units are the way to keep them straight.

Build the weights table on the board for the 5-year 4% bond. **The weights must sum to 1** — say that if they do not, stop before computing anything. Macaulay 4.61 on a five-year bond: ask why it is under five before explaining. The coupons pull the average forward.

**Three rules**, derived from that sentence rather than memorised: longer maturity raises duration; a bigger coupon lowers it; a higher yield lowers it. A zero's duration is exactly its maturity, because there is nothing to pull forward.

→ **D5, D6** on paper, 15 minutes.

### C. Convexity (30')

**The bet:** duration says €92.28, the truth is €92.64. Is the straight line wrong in the holder's favour, or against?

**Clip — `w05_convexity`.** The gap opening as the yield moves, always the same way: the curve lies above the tangent on both sides. So duration alone **overstates the loss and understates the gain**.

The second term, and the two things that get dropped under pressure: the **half** and the **square**.

| | |
|---|---|
| duration only | 92.28 |
| + convexity | 92.66 |
| the truth | 92.64 |

Thirty-six cents out becomes two cents out. Be honest about the two cents: they belong to the next term, and nobody on a trading floor cares.

**The statement slide:** between two bonds of the same duration, the more convex is worth more — more upside, less downside, and you usually pay for it.

**Then answer the morning's question** with the portfolio: `D = 4.23`, `ΔV ≈ −€42,280`. Give them the Board sentence verbatim and ask what they would cut from it.

→ **D8, D11** on paper, 15 minutes.

### D. Mock exam (40' + marking)

Exam conditions, meant literally: no notes, calculator only, phones away, forty minutes on the clock. `mock_exam.md`.

Then **mark it together**, item by item, and make the marking scheme explicit: marks are for method. A correct answer with no working scores badly; a wrong answer with sound working scores well. Have them sort their lost marks into **method** and **execution** — the two piles need different remedies, and the distinction is the most useful thing they take from the exercise.

### Handover (last 5')

Say plainly what happens next:
- Homework 5 due Wednesday 28 October, lighter on purpose.
- Reading week has one optional online office hour. **Bring a draft.**
- Midterm due Sunday 1 November, 23:59, Turnitin. Presentations the week of 2 November.
- Weeks 6–10 with Vincenzo Nardelli, online: probability, distributions, statistics.
- I mark the midterm and remain their reference for it.

## Key concepts (one line each)

- A bond is an **annuity plus a lump sum**; price and yield move in opposite directions.
- Coupon above yield → premium; equal → par; below → discount.
- **Macaulay duration** is the average time to repayment, in years; **modified** is the sensitivity, in % per %.
- Longer maturity raises duration; a larger coupon lowers it; a higher yield lowers it. A zero's duration is its maturity.
- **Convexity** is the curvature duration misses, and it always favours the holder.
- A portfolio's duration is the **value-weighted average** of its parts.

## Tutor's notes

- Protect the forty minutes for the mock. If block C runs long, cut D8 and go straight to D11 — the mock is the only rehearsal they get of the exam's timing, which is what most of them will actually fail on.
- The weights-sum-to-one check saves more marks than any other single instruction this week.
- Keep Macaulay and modified apart in every sentence you say. Sloppiness here is contagious.
- Marking together is not optional: seeing the scheme applied to their own paper is where the "method, not answer" message finally lands.
- Do not end on the exam. End on the handover, with the midterm timetable on the board.
