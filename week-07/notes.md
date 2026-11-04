# Week 7 — The founder does not know the numbers

**MBA03 Research & Quantitative Business Methods · Mon 9 Nov 2026, 10:00–13:00, in person, Florence · Tutor: Vincenzo Nardelli**

Syllabus topic: sets and Venn diagrams, the rules of probability, conditional probability and Bayes, random variables with mean and variance, the binomial, the Poisson, the normal (with skewness in one slide). The only in-person session of the second half; weeks 8–10 are online.

Running case for the whole morning, as in weeks 1–5: **Arno Bikes**, the e-bike assembler in Florence (fixed cost €60,000 a month, €400 a bike, list €1,000). The pivot of the session: in weeks 1–5 every number was given; from today the founder does not know the numbers, and a number she does not know is a number with a spread. Everything in weeks 8–10 stands on today's normal and on the words "mean" and "standard deviation".

## Learning objectives

By the end of the session the students can:

1. **Define in one sentence** set, subset, universal set, complement, intersection and union, **count "both"** from two circles, and turn the count identity into the addition law by dividing by N. Tell combinations from permutations with one question ("does swapping change the outcome?").
2. **Read a two-way table both ways** (P(A | B) and P(B | A)), **test independence** by comparing a row share with the overall share, and **update** a prior with Bayes' theorem written as the column of the table.
3. **Compute by hand** the mean and variance of a short list, then the expected value and standard deviation of a discrete random variable with the shares as weights.
4. **Name the model in words** (binomial: how many of these n; Poisson: how many in this interval), write μ = rate × interval first, and compute P(x), P(0), P(≥ 1).
5. **Answer a normal question as an area** — sketch, shade, standardise, table, sentence — forwards (share below a threshold) and backwards (the threshold for a given share: the guarantee). Say what skewness is and when the bell is the wrong picture.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:10 | Welcome, the bridge | Slides | Who I am. Weeks 1–5 every number known; weeks 7–10 the same firm, numbers unknown. Planning on the mean and running out (the picture: same mean, two spreads). Where the four weeks go; how today runs; the case. |
| 10:10–10:40 | **A. How many of our customers do both?** | Slides → board → paper | Six words with Arno Bikes next to each; 200 customers, two circles, 50 both; divide by N: probability as a long-run share, the addition law; 3 of 8 staff: combinations (what ( ) and ! mean, cancel before you multiply: 56) then permutations (336, six times more). **D1** (3', two numbers) and the answer slide. |
| 10:40–11:10 | **B. Which supplier sent the faulty batteries?** | Slides → board → paper | Two-way table 1,000 batteries, Volta/Ampere; conditional both ways (.02 and .05 by row; .48 and .52 by column); independence as "the row does not change the share"; Bayes as the column in one line. **D2** (8'). |
| 11:10–11:25 | Break | — | Outside the room. |
| 11:25–12:00 | **C. How many returns next week?** | Slides → board → app → clip → paper | Five weeks of returns by hand (mean 5, s 1.58); the random variable with shares (E 5.0, σ 1.26); 12 test rides, p = .25 (binomial, P(3) = .258, mean 3) + app; helpline 3 an hour, half an hour μ = 1.5 (Poisson, P(0) = .223) + clip; binomial or Poisson in words. **D3** (8'). |
| 12:00–12:35 | **D. What range do we promise?** | Slides → clip → board → app → paper | N(90, 8); the clip; 68–95–99.7; below 75 km (z = −1.88, .030); the app; the guarantee backwards (5% → z = −1.645 → 76.8 km, print 76); skewness in one slide. **D4** (8'). |
| 12:35–12:50 | **Take home, four answers, homework** | Slides | The four take-home lines, one per block. The four answers for the founder, read back as sentences. The formula page. Homework 7, due Sunday 15 November 23:59 on Moodle. |
| 12:50–13:00 | Buffer | — | Questions; "next Monday, remotely: how sure are we of that number?". |

No quiz this week. Paper time 31 minutes across four frames; if a frame runs over, stop it, show the solution and move on — the solutions are online on Friday.

## Script

### The bridge (10')

Who I am, one minute. Then the table of the Arno Bikes numbers they used in weeks 1–5 — fixed cost, €400, €1,000, break-even 100, 9% cost of capital, the 4% bond — and the sentence: "every one of these was given; you solved for the rest." Click: the same firm, and four things the founder does not know. **Red line:** a number she does not know is a number with a spread.

**Planning on the average.** Demand averages 100 a month; she stocks 110 and thinks she is safe. Show the picture: same mean, σ = 5 runs out in 2% of months, σ = 20 in one month in three. "The mean was never the problem. The spread is. For the spread we need the variance — and the rest of today." Do not define variance yet; the picture is the promise.

Where the four weeks go (the one red line about assessments — say it once and do not come back to it), how today runs (bets are *written*: hand out the slips now), the case table.

### A. How many of our customers do both? (30')

**Six words** (3'). Read the table aloud once, left to right. Insist on "the set of customers that…" as the shape of a definition. Say once: a symbol alone is not a definition.

**The bet** (1'): 120 accessories, 90 service plan, 40 neither, out of 200 — "how many both? more or fewer than 30?". Most write 30 or a number near 120 + 90 − 200 = 10. Write on the board: at least one = 200 − 40 = 160; 120 + 90 = 210 counts "both" twice; 210 − 160 = **50**. Then the four regions, 70 / 50 / 40 / 40, check 200.

**Divide by N** (4'). Probability is a long-run share: 50/200 = .25. The same identity divided by 200 is the addition law, .60 + .45 − .25 = .80. Shares never negative, add to 1; the complement is the "neither" row. **Board sentence:** eighty per cent buy at least one extra, a quarter buy both; "or" adds, then takes the overlap out once.

**Three of eight** (4'). Bet: more or fewer than 100 teams? 56. Then the named roles: 336 = 56 × 3!. The one question that decides: does swapping two people change the outcome?

→ **D1** on paper, 3 minutes, two numbers: 2 of 6 mechanics, pairs then lead/assistant. Collect a few answers aloud, then the answer slide. The one slip to catch: 30 for the pairs.

### B. Which supplier sent the faulty batteries? (30')

**The bet** (2'): Volta 700 at 2%, Ampere 300 at 5%; a faulty battery with no label — which supplier, and a share? Most write Volta (they send most). Build the table on the board from the four facts: 14 and 15 faulty, 29 in all.

**Both ways** (8'). By row: 14/700 = .02 and 15/300 = .05 — the defect rates we started from. By column: 14/29 = .48 and 15/29 = .52. Most batteries come from Volta; most faulty ones from Ampere — just. **Red line:** same cell on top, different total underneath, different question. Make them say which total before dividing, every time.

**Independence** (5'). Overall share .029; knowing the row changes it (.02, .05): dependent. Show the table independence would have produced (2.9% in each row). Test, then say the word.

**Bayes** (8'). Write it in one line with the shares: (.05 × .30) / (.02 × .70 + .05 × .30) = .015/.029 = .52. Numerator = the Ampere-faulty cell; denominator = the faulty column. "Bayes is the two-way table with shares instead of counts." Before: .30. After: .52. The base rate survives the evidence. **Board sentence:** slightly more likely Ampere, 52 to 48; audit Ampere's line, do not switch supplier on one battery.

→ **D2** on paper, 8 minutes. Counts first, then shares; the test before the word "independent".

### Break (15') — back at 11:25.

### C. How many returns next week? (35')

**Five weeks by hand** (6'). 4, 7, 3, 6, 5. Mean 25/5 = 5. Deviations sum to zero (the check). Squares sum 10; divide by n − 1 = 4: s² = 2.5, s = 1.58. Say why n − 1 in one sentence (the mean was estimated from the same five numbers) and move on; week 8 uses it.

**The random variable** (5'). Twenty weeks of history turned into shares: 3 .15, 4 .20, 5 .30, 6 .20, 7 .15. "Next week's number, before we see it, with a share attached to each value." Same two formulas with the shares as weights: E = 5.0, σ² = 1.6, σ = 1.26. **Red line:** mean and variance are the same two formulas twice — once with 1/n, once with the shares.

**Twelve test rides** (7'). Bet: most likely number of buyers, and the chance of exactly 3. Binomial in words first (fixed n, yes/no, same p, alone). P(3) = 220 × .0156 × .0751 = .258; mean np = 3; σ = 1.5. Nobody buys .032, at least one .968. **App** (`apps/w07_binomial.html`): push n to 40 — the bars become a bell (a promise for block D); drop p to .05 and watch the shape lean.

**The helpline** (7'). Bet: 3 calls an hour, she steps out for half an hour — chance nobody calls? Most write 5% (e⁻³) or "small". Write μ = 3 × ½ = 1.5 **before** any number; P(0) = e^{−1.5} = .223. Then the hour: P(0) = .050, P(≥ 1) = .950, P(2) = .224. **Red line:** without rescaling you say 5%; it is 22%, four times out. μ first, always. **Clip** (`media/w07_poisson.mp4`): calls arrive at random, the hourly counts pile into the Poisson shape.

**Binomial or Poisson** (3'). The two columns in words; make them say which one before any formula, every time. **Board sentence:** three sales expected from twelve rides, nobody buying is a one-in-thirty Saturday; leave the helpline for half an hour and you miss at least one call three times in four.

→ **D3** on paper, 8 minutes. Deviations sum to zero before squaring; name the model; write μ.

### D. What range do we promise? (35')

**The bet** (3'): 200 bikes measured, mean 90 km, SD 8 km; print 75 km — what share see less? Then the normal in words (continuous, bell, symmetric, μ and σ, mean = median = mode, skewness zero, probability is an area). **Clip** (`media/w07_normal.mp4`): the ranges pile into the bell; the area left of a threshold fills.

**68–95–99.7** (4'). 82–98, 74–106, 66–114. A bike at 74 km is two σ below: one in forty. **Red line:** the same three numbers for every bell — that is why we measure in σ, not in km.

**Below 75 km** (7'). z = (75 − 90)/8 = −1.875 ≈ −1.88; the table gives the area to the **left**: .030. Three riders in a hundred. Sketch, shade, standardise, table, sentence — say the five words and make them write them. **App** (`apps/w07_normal.html`): double σ to 16 and watch the tail grow; then the toggle, "find the threshold for a given share".

**The guarantee** (8'). The Board accepts 5%. Backwards: z = −1.645, x = 90 − 13.2 = 76.8 km. Print 76 (a promise rounds down): share below is .040. The small table: 85 km 27%, 80 km 11%, 76.8 km 5%, 75 km 3%. **Board sentence:** print 76 km; about one rider in twenty-five will see less, and every km on the box adds one or two complaints in a hundred. Ask who bet within 2 km at the start.

**Skewness** (3'). Battery range symmetric, skewness zero; delivery times with a long right tail, mean above median, positive skewness. **Red line:** before the table, ask whether the data are a bell.

→ **D4** on paper, 8 minutes. The sketch first; (c) ends in minutes.

### Take home, four answers, homework (15')

The take-home slide: four lines, one per block, read aloud; the red line is the day's sentence (the mean was never the problem, the spread is). Then the four answers for the founder: ask the room to say each one before showing it. The formula page: ten lines, each tied to a number from the morning. Homework 7 (five drills + the memo on the range to print, due Sunday 15 November 23:59 on Moodle, corrected together next Monday), and the one mention of the book: "if you want more, Anderson et al., the probability chapters — not required". 

### Buffer (10')

Questions. Close on the Board's number, not on a formula. Last sentence: "A sample of 200 bikes gave 90 km. The true average is not 90. Next Monday, remotely: how far off can it be?"

## Cut order if late

The buffer goes first. Then:

1. **Skewness** in block D: one sentence on the take-home slide instead of the slide.
2. **The independence table** in block B: keep the comparison .02 / .05 / .029, skip the "if independent" table.
3. **Permutations** in block A: keep combinations and the 8-choose-3 bet.
4. Trim each remaining paper frame by one minute before cutting any teaching.

**Never cut:** the two-circle count and "divide by N" (A), the table read both ways (B), the five-row table by hand and "μ first" (C), the guarantee backwards (D).

## Board, slide, screen — what goes where

Two or three students in the room; the board is the table we work at.

**On the board, always.** The two-circle count (160, 210, 50), the two-way table built from the four facts, every division with its total named, the five-row table with the deviations, every substitution line of a formula. The students write what they watch being written.

**On the slide.** The six-words table, the pictures (mean vs spread, Venn, binomial bars, the bell, the guarantee, skewness), the bets, the hubs, the Board sentences, the formula page.

**On screen.** Only when a parameter moves: the binomial app (n and p), the normal app (μ, σ, threshold, and the inverse toggle), and the two clips. Full-screen them; never show code.

## Tutor's notes

- **What needs the projector:** the deck (`lectures/07-probability.qmd`), the two apps and the two clips (`lectures/apps/`, `lectures/media/`). Everything else is board and paper; if the projector fails, the session survives.
- **Bets on paper.** Hand out slips at 10:08; collect nothing, but ask for a show of hands after each answer ("who was within…?"). The surprises that teach: "both" is 50 not 30; the faulty battery is Ampere's by a hair; no call in half an hour is 22% not 5%.
- **The table reads from the left.** Draw the shaded sketch before every table reading, including the easy ones; the wrong tail is the most expensive slip of the week.
- **Keep "mutually exclusive" and "independent" apart** if the question comes: if A rules out B, knowing A changes P(B) to zero — the opposite of independent.
- **n − 1.** One sentence, no more. If someone asks "why not n", say "because the mean came from the same numbers; week 8 makes it matter" and move on.
- **Rounding.** z = −1.875 read as −1.88 gives .0301; the exact value is .0304. Both accepted; say so once.
- **Language.** They will hear "complement", "conditional", "independent", "expected value", "standard deviation", "standardise", "skewness". Write each on the board the first time.
