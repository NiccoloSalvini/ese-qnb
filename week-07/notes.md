# Week 7 — Three shapes, and how to decide with them

**MBA03 Research & Quantitative Business Methods · Mon 9 Nov 2026, 10:00–13:00, online (Google Meet) · Tutor: Vincenzo Nardelli**

Syllabus topic: the mean and variance of a list and of a random variable (block C of lesson 6, not reached on Thursday), the binomial, the Poisson, the normal (with skewness and kurtosis), and expected value as a decision tool. The normal approximation of the binomial and the first simulation (originally block E) move to week 8, where they open the sampling distribution. Online, like the rest of the second half; lesson 6 (last Thursday, in person) did blocks A and B only: sets and counting, the two-way table, conditional probability and Bayes. Its block C (mean, variance, the random variable, the word "distribution") opens today as block A, before the three shapes.

Running case for the whole morning, as in weeks 1–6: **Arno Bikes**, the e-bike assembler in Florence (fixed cost €60,000 a month, €400 a bike, list €1,000). The pivot of the session: first an unknown number gets a mean and a spread (block A); then it gets a **shape**, and a shape is something you can read a probability off and decide with. Everything in weeks 8–10 stands on today's bell and on the words "mean" and "standard deviation".

## Learning objectives

By the end of the session the students can:

0. **Summarise a list and a random variable**: mean, variance with n − 1, standard deviation by hand in a table; E(x) and σ with the shares as weights; say that the table of shares, drawn, is the distribution.
1. **Name the model in words** (binomial: how many of these n; Poisson: how many in this interval), write μ = rate × interval first, and compute P(x), P(0), P(≥ 1), the mean and the standard deviation. Say when the three shapes turn into one another.
2. **Answer a normal question as an area** — sketch, shade, standardise, table, sentence — forwards (share below a threshold) and backwards (the threshold for a given share: the guarantee). Say what skewness and kurtosis are and when the bell is the wrong picture.
3. **Decide with a tree**: draw the square and the circles, put probabilities and payoffs on it, compute the expected value and the spread at a chance node, and weigh both in one sentence for the Board.

## Session plan

| Time / length | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:20 | Homework 6, step by step | Slides | The recap slide in one minute, then H1 (definitions, Venn: both 35; P(H ∪ L) .833, neither .167; 120 displays, 720 arrangements), H2 (table; .03 and .411; rows .03/.08 against .0475: dependent; Bayes .589) and the model memo, every step revealed in turn. H3 moved to Homework 7. Then where we are, today's question, how today runs. |
| 10:20–10:50 | **A. How many returns next week? — the language of distributions** | Slides → clip → chat | Lesson 6's block C: five weeks of returns by hand (mean 5, s 1.58); the spread clip; the random variable with shares (E 5.0, σ 1.26); the bars as the distribution; five words; the bridge to three shapes. **D1** at home (the paper time goes to the later drills). |
| 35' | **B. How many of Saturday's riders buy?** | Slides → app → clip → paper | 12 test rides, p = .25 (binomial, P(3) = .258, mean 3, σ 1.5) + app; helpline 3 an hour, half an hour μ = 1.5 (Poisson, P(0) = .223) + clip; binomial or Poisson in words; the "one family" clip and its table. **D2** (8'). |
| 25' | **C. What range do we promise?** (part 1) | Slides → clip → board | N(90, 8); the clip; 68–95–99.7; the four steps; below 75 km (z = −1.88, .030) with the table excerpt. |
| 15' | Break | — | Outside the room. |
| 20' | **C.** (part 2) | App → board → paper | The app; the guarantee backwards (5% → z = −1.645 → 76.8 km, print 76); skewness; kurtosis. **D3** (8'). |
| 25' | **D. Which supplier do we sign?** | Slides → board → paper | Volta €180 certain vs Ampere €165 with 5% faulty at €90: the tree; E = €169.50, σ = €19.6; volume (1,000 batteries: 50 faulty ± 7) vs a rush order of ten (P(≥ 2 faulty) = .086). **D4** (8'). |
| 15' | **Take home, four answers, homework** | Slides | The four take-home lines. The four answers for the founder, read back as sentences. The formula page (six lines). Homework 7, due Sunday 15 November 23:59 on Moodle. |
| 10' | Buffer | — | Questions; "next Monday, online: how sure are we of that number?". |

No quiz this week. Paper time 24 minutes across three frames (D2–D4; D1 at home); if a frame runs over, stop it, show the solution and move on — the solutions are online on Tuesday.

From block B on, each row keeps its content, order and length (in minutes); the clock is the lecturer's call. With block A and the longer homework review in front, the morning runs about 50 minutes over 13:00 if nothing is trimmed: see the cut order.

## Script

### Homework 6, step by step, and the opening (20')

The recap slide first, one minute: blocks A and B of Thursday as two cards, block C "not reached, opens today", and Homework 6 "now". Then the seven solution slides, one click per step; say the step before clicking it.

**H1 (a), (b).** Three definitions as sentences that start "the set of"; then "at least one" = 180 − 30 = 150, 110 + 75 = 185 counts both twice, both = 35, the four regions 75 / 35 / 40 / 30 with the check 180. **H1 (c).** P(H ∪ L) = .611 + .417 − .194 = .833; P(neither) = .167, checked as 30/180. The slip to name: 110 + 75 − 180 = 5. **H1 (d).** The one question (does swapping two models change the display?); 120 with the 7! cancelled; 720 = 120 × 3!.

**H2 (a).** Shares in, counts out: 1,300 / 39, 700 / 56, totals 95 and 1,905. **H2 (b), (c).** Same cell, two totals: .03 (the row) and .411 (the column). Rows .03 and .08 against .0475: dependent. **H2 (d).** Three columns, then P(F) = .0475 on its own line, then the formula: .589. **Red line:** .35 before the evidence, .59 after. **The memo.** Read the model answer aloud; then the four things we look for. Ask in the chat who answered "Celle because they send more".

H3 (mean, variance, random variable) was not doable without block C: say it moves to Homework 7 as H1. Then where we are, today's question (four unknown numbers and a fifth), how today runs.

### A. How many returns next week? — the language of distributions (30', lesson 6's block C)

**Five weeks by hand** (8'). 4, 7, 3, 6, 5. Mean 25/5 = 5. Deviations sum to zero (the check). Squares sum 10; divide by n − 1 = 4: s² = 2.5, s = 1.58. Say why n − 1 in one sentence (the mean was estimated from the same five numbers; only four deviations are free) and move on; week 8 uses it.

**The clip** (`media/w06_spread.mp4`, 3'): the five distances cancel, the squares do not.

**The random variable** (8'). Twenty weeks of history turned into shares: 3 .15, 4 .20, 5 .30, 6 .20, 7 .15. "Next week's number, before we see it, with a share attached to each value." E = 5.0 line by line. Then the variance table: σ² = 1.6, σ = 1.26. **Red line:** mean and variance are the same two formulas twice — once with 1/n, once with the shares.

**The distribution** (8'). Show the bars: the table drawn. "That picture is the distribution." Two numbers summarise it: where it sits, how wide it is. Ask the picture, not the mean: seven returns is the top of the table, not a crisis; eight has not happened in twenty weeks. **Board sentence:** plan the workshop for five returns a week, give or take one or two; seven is a normal bad week, eight would be news.

**Five words** (6'). Random variable, distribution, expected value, standard deviation, parameter — each with the Arno Bikes number next to it. **Red line:** our shares came from twenty weeks of history; from block B on they come from a formula instead, and the words stay the same.

**The bridge to the three shapes** (2'). Three shapes, one line each, no formulas: binomial (how many of these n), Poisson (how many in this interval), the normal (the bell). Then straight into block B.


### B. How many of Saturday's riders buy? (35')

**Twelve test rides** (8'). Bet: most likely number of buyers, and the chance of exactly 3. Binomial in words first (fixed n, yes/no, same p, alone). P(3) = 220 × .0156 × .0751 = .258; mean np = 3; σ = 1.5. Nobody buys .032, at least one .968. **App** (`apps/w07_binomial.html`): push n to 40 — the bars become a bell (a promise for blocks B and D); drop p to .05 and watch the shape lean.

**The helpline** (7'). Bet: 3 calls an hour, she steps out for half an hour — chance nobody calls? Most write 5% (e⁻³) or "small". Write μ = 3 × ½ = 1.5 **before** any number; P(0) = e^{−1.5} = .223. Then the hour: P(0) = .050, P(≥ 1) = .950, P(2) = .224. **Red line:** without rescaling you say 5%; it is 22%, four times out. μ first, always. **Clip** (`media/w07_poisson.mp4`): calls arrive at random, the hourly counts pile into the Poisson shape.

**Binomial or Poisson** (3'). The two columns in words; make them say which one before any formula, every time. **Board sentence:** three sales expected from twelve rides, nobody buying is a one-in-thirty Saturday; leave the helpline for half an hour and you miss at least one call three times in four.

**One family** (4'). **Clip** (`media/w07_family.mp4`): bars that thin out into the Poisson, bars that smooth into a bell. Then the table in words: binomial → Poisson when trials are many and each is rare; binomial → normal when trials are many and p is not tiny; Poisson → normal at a high rate. Say that the third shape is block B, and that block D will use it on the 250 orders.

→ **D2** on paper, 8 minutes. Name the model; write μ. The slip to catch: e⁻⁴ used for the coffee break.

### C. What range do we promise? (part 1, 25'; part 2, 20')

**The bet** (3'): 200 bikes measured, mean 90 km, SD 8 km; print 75 km — what share see less? Then the normal in words (continuous, bell, symmetric, μ and σ, mean = median = mode, skewness zero, probability is an area). **Clip** (`media/w07_normal.mp4`): the ranges pile into the bell; the area left of a threshold fills.

**68–95–99.7** (4'). 82–98, 74–106, 66–114. A bike at 74 km is two σ below: one in forty. **Red line:** the same three numbers for every bell — that is why we measure in σ, not in km.

**The four steps and 75 km** (10'). Sketch, standardise, table, sentence — say the four words and make them write them. z = (75 − 90)/8 = −1.875 ≈ −1.88; the table gives the area to the **left**: .030. Three riders in a hundred. Show the table excerpt and how the row and column split z. The share above is 1 − .030.

*Break at 11:15, back at 11:30.*

**The app** (3') (`apps/w07_normal.html`): double σ to 16 and watch the tail grow; then the toggle, "find the threshold for a given share".

**The guarantee** (7'). The Board accepts 5%. Backwards: z = −1.645, x = 90 − 13.2 = 76.8 km. Print 76 (a promise rounds down): share below is .040. The small table: 85 km 27%, 80 km 11%, 76.8 km 5%, 75 km 3%. **Board sentence:** print 76 km; about one rider in twenty-five will see less, and every km on the box adds one or two complaints in a hundred. Ask who bet within 2 km at the start.

**Skewness and kurtosis** (4'). Battery range symmetric, skewness zero; delivery times with a long right tail, mean above median, positive skewness. Then the second question: same mean, same σ, where do the tails sit? The bell; a sharp peak with fat tails (delivery delays: a "three σ" day is far more common than one in three hundred); a flat top with no tails (a rota). **Red line:** fat tails mean the rare bad day is not as rare as the bell says. Two slides, in words; no formula for either.

Before D3, click the last fragment of the guarantee slide: "the other tail", z = +1.645, a time rounds up — D3(b) and H4(c) need it. → **D3** on paper, 8 minutes. The sketch first; (b) ends in kg.

### D. Which supplier do we sign? (25')

**The offers** (3'). Volta €180 fixed, faults replaced by Volta. Ampere €165, 5% faulty, €90 to swap on the line. Bet: which, and the saving per battery? Most write Ampere and €15. Point: Volta is a number, Ampere is a distribution — block A's two-row table with euros in it.

**The tree** (5'). Show the figure and read it left to right: a square where we choose, a circle where chance chooses, payoffs at the ends, the expected value written at the node. Draw it on the board as you read.

**Expected value and spread** (8'). E = .95 × 165 + .05 × 255 = 156.75 + 12.75 = €169.50: €10.50 cheaper than Volta, €10,500 a month on a thousand. Then σ² = .95 × 4.5² + .05 × 85.5² = 19.24 + 365.51 = 384.75, σ = €19.6, against Volta's zero. **Red line:** the expected value is the price you pay on average; the spread is the surprise you pay sometimes.

**Volume** (5'). On a thousand batteries the faulty count is binomial: 50 ± 6.9, the bill €169,500 ± €620 — the saving is never at risk. On a rush order of ten, two faulty (P = .086, one order in twelve) wipe out the €150 saving. **Board sentence:** sign Ampere for volume, keep Volta for rush orders. **Red line:** expected value decides when the decision repeats; spread decides when it does not.

→ **D4** on paper, 8 minutes. Profit at the end nodes, not sales; σ by hand for the ads only (the Saturday's €1,680 is given).

### Take home, four answers, homework (15')

The take-home slide: four lines, one per block, read aloud; the red line is the day's sentence (three shapes, one table, two numbers per decision). Then the four answers for the founder: ask the room to say each one before showing it. The formula page: six lines, each tied to a number from the morning. Homework 7 (five exercises, H1 being Homework 6's H3, + the memo on the range to print, due Sunday 15 November 23:59 on Moodle, corrected together next Monday), and the one mention of the book: "if you want more, Anderson et al., the probability chapters — not required".

### Buffer (10')

Questions. Close on the Board's number, not on a formula. Last sentence: "A sample of 200 bikes gave 90 km. The true average is not 90. Next Monday, online: how far off can it be?"

## Cut order if late

The buffer goes first. Then:

1. **Kurtosis** in block C: one sentence on the skewness slide instead of its own.
2. **The volume slide** in block D: keep the Board sentence, skip the rush-order arithmetic.
3. Trim each remaining paper frame by one minute before cutting any teaching.

**Never cut:** "μ first" (B), the four steps and the guarantee backwards (C), the expected value *and* the spread at the chance node (D); in block A, the five-row table by hand and the random variable with its shares.

## Board, slide, screen — what goes where

Online: the shared deck is the board, the chat is the slip. Share the browser tab, not the whole screen; the clips are muted.

**On the board, always.** Every substitution line of a formula, the decision tree drawn while the figure is on screen, the deviations table for σ, every z with its sketch.

**On the slide.** The pictures (binomial bars, the bell with 68–95–99.7, the guarantee, skewness, kurtosis, the tree, the bars under the bell), the bets, the hubs, the Board sentences, the formula page.

**On screen.** Only when a parameter moves: the binomial app (n and p), the normal app (μ, σ, threshold, and the inverse toggle), and the three clips. Full-screen them; never show code.

## Tutor's notes

- **What needs the projector:** the deck (`lectures/07-probability.qmd`), the two apps (binomial, normal) and the three clips (`lectures/apps/`, `lectures/media/`). Everything else is board and paper; if the projector fails, the session survives.
- **Bets on paper.** Hand out slips at 10:12; collect nothing, but ask for a show of hands after each answer ("who was within…?"). The surprises that teach: no call in half an hour is 22% not 5%; the guarantee is 76 not 80; Ampere's €15 saving is €10.50; a penalty month is one in nine, not "rare".
- **The table reads from the left.** Draw the shaded sketch before every table reading, including the easy ones; the wrong tail is the most expensive slip of the week.
- **Expected value is not a forecast.** If someone says "so Ampere costs €169.50": no battery ever costs €169.50; it costs €165 or €255. The expected value is the average over many. The spread is how far a single one can be from it.
- **Rounding.** z = −1.875 read as −1.88 gives .0301; the exact value is .0304. z = 1.198 read as 1.20 gives .1151; the exact binomial is .1179. Both accepted; say so once.
- **Language.** They will hear "expected value", "standard deviation", "standardise", "skewness", "kurtosis", "chance node". Write each on the board the first time.
