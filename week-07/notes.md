# Week 7 — Three shapes, and how to decide with them

**MBA03 Research & Quantitative Business Methods · Mon 9 Nov 2026, 10:00–13:00, online (Google Meet) · Tutor: Vincenzo Nardelli**

Syllabus topic: the binomial, the Poisson, the normal (with skewness and kurtosis), expected value as a decision tool, the normal approximation of the binomial, and a first simulation. Online, like the rest of the second half; lesson 6 (last Thursday, in person) did sets, the probability rules, conditional probability and Bayes, mean and variance, and the random variable with its shares.

Running case for the whole morning, as in weeks 1–6: **Arno Bikes**, the e-bike assembler in Florence (fixed cost €60,000 a month, €400 a bike, list €1,000). The pivot of the session: Thursday gave an unknown number a mean and a spread; today gives it a **shape**, and a shape is something you can read a probability off and decide with. Everything in weeks 8–10 stands on today's bell and on the words "mean" and "standard deviation".

## Learning objectives

By the end of the session the students can:

1. **Name the model in words** (binomial: how many of these n; Poisson: how many in this interval), write μ = rate × interval first, and compute P(x), P(0), P(≥ 1), the mean and the standard deviation. Say when the three shapes turn into one another.
2. **Answer a normal question as an area** — sketch, shade, standardise, table, sentence — forwards (share below a threshold) and backwards (the threshold for a given share: the guarantee). Say what skewness and kurtosis are and when the bell is the wrong picture.
3. **Decide with a tree**: draw the square and the circles, put probabilities and payoffs on it, compute the expected value and the spread at a chance node, and weigh both in one sentence for the Board.
4. **Read a count as a measurement** when the trials are many: μ = np, σ = √(np(1−p)), check np and n(1−p) ≥ 5, the four steps with the half unit. Say what a Monte Carlo simulation does and why its histogram is the distribution.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:15 | Homework 6 at the board | Board | The three items and the memo of Homework 6, corrected together. Then the recap slide ("Last Thursday, in one minute"), where we are, today's question, how today runs. |
| 10:15–10:50 | **A. How many returns next week?** | Slides → app → clip → paper | 12 test rides, p = .25 (binomial, P(3) = .258, mean 3, σ 1.5) + app; helpline 3 an hour, half an hour μ = 1.5 (Poisson, P(0) = .223) + clip; binomial or Poisson in words; the "one family" clip and its table. **D1** (8'). |
| 10:50–11:15 | **B. What range do we promise?** (part 1) | Slides → clip → board | N(90, 8); the clip; 68–95–99.7; the four steps; below 75 km (z = −1.88, .030) with the table excerpt. |
| 11:15–11:30 | Break | — | Outside the room. |
| 11:30–11:50 | **B.** (part 2) | App → board → paper | The app; the guarantee backwards (5% → z = −1.645 → 76.8 km, print 76); skewness; kurtosis. **D2** (8'). |
| 11:50–12:15 | **C. Which supplier do we sign?** | Slides → board → paper | Volta €180 certain vs Ampere €165 with 5% faulty at €90: the tree; E = €169.50, σ = €19.6; volume (1,000 batteries: 50 faulty ± 7) vs a rush order of ten (P(≥ 2 faulty) = .086). **D3** (8'). |
| 12:15–12:35 | **D. How many late orders in 250?** | Slides → board → app → paper | 250 orders, p = .06: μ = 15, σ = 3.755; the bars and the bell; P(X ≥ 20) = .115 with the half unit (exact .118; .092 without); Monte Carlo in words + the simulate app. **D4** (6'). |
| 12:35–12:50 | **Take home, four answers, homework** | Slides | The four take-home lines. The four answers for the founder, read back as sentences. The formula page (six lines). Homework 7, due Sunday 15 November 23:59 on Moodle. |
| 12:50–13:00 | Buffer | — | Questions; "next Monday, online: how sure are we of that number?". |

No quiz this week. Paper time 30 minutes across four frames; if a frame runs over, stop it, show the solution and move on — the solutions are online on Tuesday.

## Script

### Homework 6 and the opening (15')

Homework 6 at the board: the three items, then two memos read aloud, one sentence of feedback each. Keep it to fifteen minutes; what is not reached goes online with the solutions.

The recap slide: four cards, read in one minute — "or" and "given", count the ways, a number with its shares, and the homework we just did. **Red line:** Thursday you learnt to count and to condition; today the counts get a shape, and the shape gives a decision. Where we are (the one red line about assessments — say it once and do not come back to it). Today's question: the three numbers she does not know, and the fourth she has not thought of. How today runs: bets are *typed in the chat*; ask everyone to open it now and type their name as a test.

### A. How many returns next week? (35')

**Twelve test rides** (8'). Bet: most likely number of buyers, and the chance of exactly 3. Binomial in words first (fixed n, yes/no, same p, alone). P(3) = 220 × .0156 × .0751 = .258; mean np = 3; σ = 1.5. Nobody buys .032, at least one .968. **App** (`apps/w07_binomial.html`): push n to 40 — the bars become a bell (a promise for blocks B and D); drop p to .05 and watch the shape lean.

**The helpline** (7'). Bet: 3 calls an hour, she steps out for half an hour — chance nobody calls? Most write 5% (e⁻³) or "small". Write μ = 3 × ½ = 1.5 **before** any number; P(0) = e^{−1.5} = .223. Then the hour: P(0) = .050, P(≥ 1) = .950, P(2) = .224. **Red line:** without rescaling you say 5%; it is 22%, four times out. μ first, always. **Clip** (`media/w07_poisson.mp4`): calls arrive at random, the hourly counts pile into the Poisson shape.

**Binomial or Poisson** (3'). The two columns in words; make them say which one before any formula, every time. **Board sentence:** three sales expected from twelve rides, nobody buying is a one-in-thirty Saturday; leave the helpline for half an hour and you miss at least one call three times in four.

**One family** (4'). **Clip** (`media/w07_family.mp4`): bars that thin out into the Poisson, bars that smooth into a bell. Then the table in words: binomial → Poisson when trials are many and each is rare; binomial → normal when trials are many and p is not tiny; Poisson → normal at a high rate. Say that the third shape is block B, and that block D will use it on the 250 orders.

→ **D1** on paper, 8 minutes. Name the model; write μ. The slip to catch: e⁻⁴ used for the coffee break.

### B. What range do we promise? (part 1, 25'; part 2, 20')

**The bet** (3'): 200 bikes measured, mean 90 km, SD 8 km; print 75 km — what share see less? Then the normal in words (continuous, bell, symmetric, μ and σ, mean = median = mode, skewness zero, probability is an area). **Clip** (`media/w07_normal.mp4`): the ranges pile into the bell; the area left of a threshold fills.

**68–95–99.7** (4'). 82–98, 74–106, 66–114. A bike at 74 km is two σ below: one in forty. **Red line:** the same three numbers for every bell — that is why we measure in σ, not in km.

**The four steps and 75 km** (10'). Sketch, standardise, table, sentence — say the four words and make them write them. z = (75 − 90)/8 = −1.875 ≈ −1.88; the table gives the area to the **left**: .030. Three riders in a hundred. Show the table excerpt and how the row and column split z. The share above is 1 − .030.

*Break at 11:15, back at 11:30.*

**The app** (3') (`apps/w07_normal.html`): double σ to 16 and watch the tail grow; then the toggle, "find the threshold for a given share".

**The guarantee** (7'). The Board accepts 5%. Backwards: z = −1.645, x = 90 − 13.2 = 76.8 km. Print 76 (a promise rounds down): share below is .040. The small table: 85 km 27%, 80 km 11%, 76.8 km 5%, 75 km 3%. **Board sentence:** print 76 km; about one rider in twenty-five will see less, and every km on the box adds one or two complaints in a hundred. Ask who bet within 2 km at the start.

**Skewness and kurtosis** (4'). Battery range symmetric, skewness zero; delivery times with a long right tail, mean above median, positive skewness. Then the second question: same mean, same σ, where do the tails sit? The bell; a sharp peak with fat tails (delivery delays: a "three σ" day is far more common than one in three hundred); a flat top with no tails (a rota). **Red line:** fat tails mean the rare bad day is not as rare as the bell says. Two slides, in words; no formula for either.

→ **D2** on paper, 8 minutes. The sketch first; (c) ends in kg.

### C. Which supplier do we sign? (25')

**The offers** (3'). Volta €180 fixed, faults replaced by Volta. Ampere €165, 5% faulty, €90 to swap on the line. Bet: which, and the saving per battery? Most write Ampere and €15. Point: Volta is a number, Ampere is a distribution — Thursday's two-row table with euros in it.

**The tree** (5'). Show the figure and read it left to right: a square where we choose, a circle where chance chooses, payoffs at the ends, the expected value written at the node. Draw it on the board as you read.

**Expected value and spread** (8'). E = .95 × 165 + .05 × 255 = 156.75 + 12.75 = €169.50: €10.50 cheaper than Volta, €10,500 a month on a thousand. Then σ² = .95 × 4.5² + .05 × 85.5² = 19.24 + 365.51 = 384.75, σ = €19.6, against Volta's zero. **Red line:** the expected value is the price you pay on average; the spread is the surprise you pay sometimes.

**Volume** (5'). On a thousand batteries the faulty count is binomial: 50 ± 6.9, the bill €169,500 ± €620 — the saving is never at risk. On a rush order of ten, two faulty (P = .086, one order in twelve) wipe out the €150 saving. **Board sentence:** sign Ampere for volume, keep Volta for rush orders. **Red line:** expected value decides when the decision repeats; spread decides when it does not.

→ **D3** on paper, 8 minutes. Profit at the end nodes, not sales; the deviations table for σ.

### D. How many late orders in 250? (20')

**The question** (4'). 250 orders, p = .06, a penalty at 20 or more. Bet: how likely is a penalty month? Binomial, but the four steps would need 231 terms. The mean and spread we have: μ = 15, σ = √14.1 = 3.755. The clip said the bars become a bell: np = 15 and n(1−p) = 235, both at least 5.

**The figure** (2'). The exact bars, the bell over them, the ≥ 20 tail shaded; the bar for 20 starts at 19.5.

**The four steps on a count** (6'). z = (19.5 − 15)/3.755 = 1.20; area left .8849; P(X ≥ 20) = .115, about one month in nine. One muted line: without the half unit z = 1.33 and .092, a tenth too small; the exact binomial is .118. Do not dwell on the correction: "use it, move on". **Board sentence:** expect 15 late, give or take four; a penalty month about once in nine; at 4% late it is rarer than one in fifty.

**Monte Carlo** (5'). Play one Saturday: twelve coin flips, count the buyers. Play a thousand: the counts pile into bars; about 258 Saturdays with three buyers, about 32 with none. Same for the 250 orders: about 118 months in a thousand with twenty or more. **App** (`apps/w07_simulate.html`): 10 Saturdays, then 1,000; then n = 250, p = .06. **Red line:** the histogram of the simulation *is* the binomial; the formula is the shortcut, the simulation is the thing itself. No formula on this slide.

→ **D4** on paper, 6 minutes. The check np ≥ 5 before the bell; the half unit.

### Take home, four answers, homework (15')

The take-home slide: four lines, one per block, read aloud; the red line is the day's sentence (three shapes, one table, two numbers per decision). Then the four answers for the founder: ask the room to say each one before showing it. The formula page: six lines, each tied to a number from the morning. Homework 7 (five drills + the memo on the range to print, due Sunday 15 November 23:59 on Moodle, corrected together next Monday), and the one mention of the book: "if you want more, Anderson et al., the probability chapters — not required".

### Buffer (10')

Questions. Close on the Board's number, not on a formula. Last sentence: "A sample of 200 bikes gave 90 km. The true average is not 90. Next Monday, online: how far off can it be?"

## Cut order if late

The buffer goes first. Then:

1. **Monte Carlo** in block D: keep the one sentence ("the histogram of the simulation is the binomial") and skip the app; students run it at home.
2. **Kurtosis** in block B: one sentence on the skewness slide instead of its own.
3. **The volume slide** in block C: keep the Board sentence, skip the rush-order arithmetic.
4. Trim each remaining paper frame by one minute before cutting any teaching.

**Never cut:** "μ first" (A), the four steps and the guarantee backwards (B), the expected value *and* the spread at the chance node (C), the half unit and the check np ≥ 5 (D).

## Board, slide, screen — what goes where

Online: the shared deck is the board, the chat is the slip. Share the browser tab, not the whole screen; the clips are muted.

**On the board, always.** Every substitution line of a formula, the decision tree drawn while the figure is on screen, the deviations table for σ, every z with its sketch.

**On the slide.** The pictures (binomial bars, the bell with 68–95–99.7, the guarantee, skewness, kurtosis, the tree, the bars under the bell), the bets, the hubs, the Board sentences, the formula page.

**On screen.** Only when a parameter moves: the binomial app (n and p), the normal app (μ, σ, threshold, and the inverse toggle), the simulate app (n, p, number of runs), and the three clips. Full-screen them; never show code.

## Tutor's notes

- **What needs the projector:** the deck (`lectures/07-probability.qmd`), the three apps and the three clips (`lectures/apps/`, `lectures/media/`). Everything else is board and paper; if the projector fails, the session survives.
- **Bets on paper.** Hand out slips at 10:12; collect nothing, but ask for a show of hands after each answer ("who was within…?"). The surprises that teach: no call in half an hour is 22% not 5%; the guarantee is 76 not 80; Ampere's €15 saving is €10.50; a penalty month is one in nine, not "rare".
- **The table reads from the left.** Draw the shaded sketch before every table reading, including the easy ones; the wrong tail is the most expensive slip of the week.
- **The half unit.** If someone asks why 19.5: a bar for a whole number spans half a unit each side, and the bell has no bars. One sentence; do not derive.
- **Expected value is not a forecast.** If someone says "so Ampere costs €169.50": no battery ever costs €169.50; it costs €165 or €255. The expected value is the average over many. The spread is how far a single one can be from it.
- **Rounding.** z = −1.875 read as −1.88 gives .0301; the exact value is .0304. z = 1.198 read as 1.20 gives .1151; the exact binomial is .1179. Both accepted; say so once.
- **Language.** They will hear "expected value", "standard deviation", "standardise", "skewness", "kurtosis", "chance node", "continuity correction", "simulation". Write each on the board the first time.
