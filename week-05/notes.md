# Week 5 — What a rate rise costs you

**MBA03 Research & Quantitative Business Methods · Thu 22 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: bond pricing, duration and convexity (Renshaw ch. 10–13). Plus consolidation and a **mock of the final exam's calculus question**. Beyond the syllabus, ten minutes: **immunisation** — duration used to make a payment safe; paid for by shortening the mock from 40' to 30'.

Last session of my half. It closes the loop deliberately: a bond is last week's arithmetic, duration is week 2's derivative, convexity is week 3's second derivative.

## Learning objectives

By the end of the session the students can:

1. **Price** a plain coupon bond and say, without arithmetic, whether it trades at a premium or a discount — resit's MCQ block.
2. **Compute** Macaulay and modified duration from a table of weights, and use modified duration to estimate a price change — resit's MCQ block.
3. **State** how maturity, coupon and yield move duration, and why — resit's MCQ block.
4. **Add** the convexity term, say which way duration alone errs, and explain in plain words what convexity buys the holder.
5. **Match** a portfolio's duration to the date of a payment (two zeros, one weight) and check the value at the horizon after a rate move — beyond the syllabus, not examined.
6. **Sit** the five-item calculus question under exam conditions and mark it.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:12 | HW4 walkthrough | Paper | The memo. Ask whether the Board member would accept it. |
| 10:12–10:40 | **A. Pricing a bond** | Slides → paper | Annuity plus lump sum. Premium, par, discount. |
| 10:40–11:20 | **B. Duration** | Slides + figure + clip → paper | The slope. Two durations. Three rules. |
| 11:20–11:35 | break | — | Outside the room. |
| 11:35–12:15 | **C. Convexity, then immunisation** | Slides + clip → notebook → paper | The gap the line misses. The reserve, answered. Then: can we stop worrying? |
| 12:15–12:45 | **D. Mock exam** | Paper, exam conditions | Thirty minutes, `mock_exam.md`, no notes. |
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

### C. Convexity, then immunisation (30' + 10')

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

**Immunisation (10', beyond the syllabus — say so).** The reserve answer measured the risk; now remove it. New setup: Arno Bikes owes **€1M in exactly 4 years** for the building and puts the money aside today in zeros at 5%. **The bet:** short bonds, long bonds, or a mix?

Two forces when rates rise: **prices fall** (bad — whatever is still held at year 4 is worth less) and **coupons reinvest at more** (good — whatever comes back early earns the new rate). Short bonds: reinvestment wins; long bonds: the price fall wins. When the portfolio's duration equals the date of the payment, the two offset to first order.

On the board: `PV = 1,000,000/1.05⁴ = €822,702.47`; `2w + 6(1 − w) = 4 → w = ½`; €411,351.24 in each; faces €453,514.74 (year 2) and €551,250.00 (year 6). Then the check at 6%: `453,514.74 × 1.06² + 551,250/1.06² = 509,569.16 + 490,610.54 = €1,000,179.70`. At 4%: €1,000,183.16. **Slightly above either way** — ask why before saying "convexity". The figure shows the two unmatched portfolios tilting opposite ways — about €19k off at 6%, €38k at 3% or 7%; the matched one is flat.

Board sentence, then the condition that makes it honest: durations drift apart as time passes, so the match is **reset every year**.

→ **D12** on paper, 5 minutes; D13–D14 for home if the clock says so. If block C is late, show the four slides and skip D12 — never eat into the mock.

### D. Mock exam (30' + marking)

Exam conditions, meant literally: no notes, calculator only, phones away, thirty minutes on the clock — six an item. All five items stay: none needs more than a few lines of working. `mock_exam.md`.

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
- **Immunisation**: hold a portfolio whose (Macaulay) duration equals the date of a payment and a one-off rate move leaves the payment covered — price and reinvestment effects cancel, convexity leaves a small surplus. Rebalance as time passes.

## Board, slide, screen — what goes where

**On the board.** The weights table for the duration calculation, column by column, with them
reading out each present value. The weights must sum to 1 — write that check on the board and
leave it. Then the convexity correction, term by term.

**On the slide.** The price–yield figure, both clips, the three duration rules, the
premium/par/discount table, the immunisation figure (value at year 4 against the new yield).

**On screen.** Optional this week; the clips carry the intuition. If you open the notebook at
all, it is for the table of actual-versus-estimate at several yield moves, or for the immunisation
slider (§ E): drag the weight in the long bond and watch the horizon line flatten at ½.

Then close everything for the mock. Thirty minutes, exam conditions, meant literally — it is
the only rehearsal they get of the exam's *timing*, which is what most candidates actually fail
on. Mark it together afterwards, out loud, so they see the scheme applied to their own paper.

## Tutor's notes

- Protect the thirty minutes for the mock. If block C runs long, cut D8 and go straight to D11, and run immunisation as slides only (D12 to home) — the mock is the only rehearsal they get of the exam's timing, which is what most of them will actually fail on.
- The weights-sum-to-one check saves more marks than any other single instruction this week.
- Keep Macaulay and modified apart in every sentence you say. Sloppiness here is contagious.
- Marking together is not optional: seeing the scheme applied to their own paper is where the "method, not answer" message finally lands.
- Do not end on the exam. End on the handover, with the midterm timetable on the board.
