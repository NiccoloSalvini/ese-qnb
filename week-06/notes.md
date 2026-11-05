# Week 6 — The founder does not know the numbers

**MBA03 Research & Quantitative Business Methods · Thu 5 Nov 2026, 10:00–13:00, in person, Florence · Tutor: Vincenzo Nardelli**

Syllabus topic: sets and Venn diagrams, the rules of probability, counting, conditional probability and Bayes, mean and variance of a list, random variables with expected value and standard deviation, and the word "distribution". The three named shapes (binomial, Poisson, normal) and deciding with them are Monday's session (week 7, online).

Running case for the whole morning, as in weeks 1–5: **Arno Bikes**, the e-bike assembler in Florence (fixed cost €60,000 a month, €400 a bike, list €1,000). The pivot of the session: in weeks 1–5 every number was given; from today the founder does not know the numbers, and a number she does not know is a number with a spread. Everything in weeks 7–10 stands on today's words "mean", "standard deviation" and "distribution".

In-person format: bets are written on a slip (not said aloud); no drill frames in the deck — the three drills are online with solutions, to be done on paper tonight; the two clips are played full-screen from the deck.

## Learning objectives

By the end of the session the students can:

1. **Define in one sentence** set, subset, universal set, complement, intersection and union, **count "both"** from two circles, and turn the count identity into the addition law by dividing by N. Tell combinations from permutations with one question ("does swapping change the outcome?").
2. **Read a two-way table both ways** (P(A | B) and P(B | A)), **test independence** by comparing a row share with the overall share, and **update** a prior with Bayes' theorem written as the column of the table.
3. **Compute by hand** the mean and variance of a short list (n − 1), then the expected value and standard deviation of a discrete random variable with the shares as weights.
4. **Use the five words** random variable, distribution, expected value, standard deviation, parameter about an Arno Bikes number, and read a bar picture of shares as "where it sits, how wide it is".

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:10 | Welcome, the bridge | Slides | Who I am. Weeks 1–5 every number known; weeks 6–10 the same firm, numbers unknown. Planning on the mean and running out (the picture: same mean, two spreads). Where the weeks go (6–10); how today runs; the case. |
| 10:10–10:45 | **A. How many of our customers do both?** | Slides → slips → clip | Six words with Arno Bikes next to each; 200 customers, two circles, 50 both; divide by N: probability as a long-run share, the addition law; the choices clip; 3 of 8 staff: combinations (what ( ) and ! mean, cancel before you multiply: 56) then permutations (336, six times more). |
| 10:45–11:15 | **B. Which supplier sent the faulty batteries?** | Slides → slips | Two-way table 1,000 batteries, Volta/Ampere; conditional both ways (.02 and .05 by row; .48 and .52 by column); independence as "the row does not change the share"; Bayes as the column in one line. |
| 11:15–11:30 | Break | — | Cameras off. Back at 11:30. |
| 11:30–12:20 | **C. How many returns next week? — the language of distributions** | Slides → clip → slips | Five weeks of returns by hand (mean 5, s 1.58); the spread clip; the random variable with shares (E 5.0, σ 1.26); the bars as the distribution; five words; the bridge to Monday's three shapes. |
| 12:20–12:40 | **Take home, three answers, homework** | Slides | The three take-home lines. The three answers for the founder, read back as sentences. The formula page (six lines). Homework 6, due Sunday 8 November 23:59 on Moodle. |
| 12:40–13:00 | Buffer | — | Questions; "Monday, online: three shapes, and how to decide with them". |

No quiz this week. No drill frames: the three drills (D1–D3) are published with solutions tonight; the first 15 minutes on Monday go to the homework, not to the drills.

## Script

### The bridge (10')

Who I am, one minute. Then the table of the Arno Bikes numbers they used in weeks 1–5 — fixed cost, €400, €1,000, break-even 100, 9% cost of capital, the 4% bond — and the sentence: "every one of these was given; you solved for the rest." Click: the same firm, and four things the founder does not know. **Red line:** a number she does not know is a number with a spread.

**Planning on the average.** Demand averages 100 a month; she stocks 110 and thinks she is safe. Show the picture: same mean, σ = 5 runs out in 2% of months, σ = 20 in one month in three. "The mean was never the problem. The spread is. For the spread we need the variance — and the rest of today." Do not define variance yet; the picture is the promise.

Where the weeks go (the one red line about assessments — say it once and do not come back to it), how today runs (bets are *written on the slip*: hand the slips out now), the case table.

### A. How many of our customers do both? (35')

**Six words** (4'). Read the table aloud once, left to right. Insist on "the set of customers that…" as the shape of a definition. Say once: a symbol alone is not a definition.

**The bet** (2'): 120 accessories, 90 service plan, 40 neither, out of 200 — "how many both? more or fewer than 30? type it". Most type 30 or a number near 120 + 90 − 200 = 10. Reveal: at least one = 200 − 40 = 160; 120 + 90 = 210 counts "both" twice; 210 − 160 = **50**. Then the four regions, 70 / 50 / 40 / 40, check 200.

**Divide by N** (6'). Probability is a long-run share: 50/200 = .25. The same identity divided by 200 is the addition law, .60 + .45 − .25 = .80. Shares never negative, add to 1; the complement is the "neither" row. **Board sentence:** eighty per cent buy at least one extra, a quarter buy both; "or" adds, then takes the overlap out once.

**The clip** (`media/w06_choices.mp4`, 2'): three of eight picked one at a time; the orderings that collapse into one team.

**Three of eight** (8'). Bet: more or fewer than 100 teams? 56. Then the named roles: 336 = 56 × 3!. The one question that decides: does swapping two people change the outcome?

### B. Which supplier sent the faulty batteries? (30')

**The bet** (2'): Volta 700 at 2%, Ampere 300 at 5%; a faulty battery with no label — which supplier, and a share? Type both. Most type Volta (they send most). Build the table step by step from the three facts: 14 and 15 faulty, 29 in all.

**Both ways** (8'). By row: 14/700 = .02 and 15/300 = .05 — the defect rates we started from. By column: 14/29 = .48 and 15/29 = .52. Most batteries come from Volta; most faulty ones from Ampere — just. **Red line:** same cell on top, different total underneath, different question. Make them type which total before dividing, every time.

**Independence** (5'). Overall share .029; knowing the row changes it (.02, .05): dependent. Say what the table would look like if independent (2.9% in each row). Test, then say the word.

**Bayes** (10'). Write it in one line with the shares: (.05 × .30) / (.02 × .70 + .05 × .30) = .015/.029 = .52. Numerator = the Ampere-faulty cell; denominator = the faulty column. "Bayes is the two-way table with shares instead of counts." Before: .30. After: .52. The base rate survives the evidence. **Board sentence:** slightly more likely Ampere, 52 to 48; audit Ampere's line, do not switch supplier on one battery.

### Break (15') — back at 11:30.

### C. How many returns next week? — the language of distributions (50')

**Five weeks by hand** (8'). 4, 7, 3, 6, 5. Mean 25/5 = 5. Deviations sum to zero (the check). Squares sum 10; divide by n − 1 = 4: s² = 2.5, s = 1.58. Say why n − 1 in one sentence (the mean was estimated from the same five numbers; only four deviations are free) and move on; week 8 uses it.

**The clip** (`media/w06_spread.mp4`, 3'): the five distances cancel, the squares do not.

**The random variable** (8'). Twenty weeks of history turned into shares: 3 .15, 4 .20, 5 .30, 6 .20, 7 .15. "Next week's number, before we see it, with a share attached to each value." E = 5.0 line by line. Then the variance table: σ² = 1.6, σ = 1.26. **Red line:** mean and variance are the same two formulas twice — once with 1/n, once with the shares.

**The distribution** (8'). Show the bars: the table drawn. "That picture is the distribution." Two numbers summarise it: where it sits, how wide it is. Ask the picture, not the mean: seven returns is the top of the table, not a crisis; eight has not happened in twenty weeks. **Board sentence:** plan the workshop for five returns a week, give or take one or two; seven is a normal bad week, eight would be news.

**Five words** (6'). Random variable, distribution, expected value, standard deviation, parameter — each with the Arno Bikes number next to it. **Red line:** our shares came from twenty weeks of history; on Monday they come from a formula instead, and the words stay the same.

**The bridge to Monday** (3'). Three shapes, one line each, no formulas: binomial (how many of these n), Poisson (how many in this interval), the normal (the bell). Then: how to decide with them. Stop there.

### Take home, three answers, homework (20')

The take-home slide: three lines, one per block, read aloud; the red line is the day's sentence (the mean was never the problem, the spread is). Then the three answers for the founder: ask them to write each one down before showing it. The formula page: six lines, each tied to a number from the morning. Homework 6 (three drills + the 100–150-word memo on the faulty battery, due Sunday 8 November 23:59 on Moodle, corrected together on Monday). Tell them the three drills with solutions are online tonight.

### Buffer (20')

Questions. Close on the founder's sentences, not on a formula. Last sentence: "Monday, online: three shapes — binomial, Poisson, the normal — and how to decide with them. Bring a calculator."

## Cut order if late

The buffer goes first. Then:

1. **The five-words slide** in block C: say the five words over the bars slide instead.
2. **The independence slide** in block B: keep the comparison .02 / .05 / .029 in one sentence on the column slide.
3. **Permutations** in block A: keep combinations and the 8-choose-3 bet; 336 moves to the drills.

**Never cut:** the two-circle count and "divide by N" (A), the table read both ways and Bayes as the column (B), the five-row table by hand and the random variable with its shares (C), the bridge slide to Monday.

## Board, slip, screen — what goes where

**On the slip, always.** Every bet (a number or a name) before the reveal; "which total?" before every division; the three answers for the founder before they are shown. Collect a few and read them aloud, by name.

**On the board.** Every substitution line of a formula, written while the slide shows it; the two circles; the five deviations and their squares.

**On the slide.** The six-words table, the pictures (mean vs spread, Venn, the bars), the two-way table built step by step, the five-row table with the deviations, every substitution line of a formula, the Board sentences, the formula page.

**On screen.** The three clips (`media/w06_choices.mp4`, `media/w06_bayes.mp4`, `media/w06_spread.mp4`), full-screen from the deck. No apps this week. The Bayes clip comes right after the "belief, evidence, new belief" slide and before the three-column table: let it run to the end before the formula.

## Tutor's notes

- **What needs the projector:** the deck (`lectures/06-the-founder-does-not-know.qmd`) and its three clips (muted). Slips of paper for the bets.
- **Bets on the slip.** Ask for them explicitly and wait ten seconds. The surprises that teach: "both" is 50 not 30; the faulty battery is Ampere's by a hair; the variance divides by 4, not 5.
- **The reveal pace.** Every long slide is in fragments: one click per step, and say the step before clicking it. The fragment is the slide's board; the real board is for the substitution lines.
- **Keep "mutually exclusive" and "independent" apart** if the question comes: if A rules out B, knowing A changes P(B) to zero — the opposite of independent.
- **n − 1.** One sentence, no more. If someone asks "why not n", say "because the mean came from the same numbers; week 8 makes it matter" and move on.
- **Do not start the three shapes.** If asked "is this the binomial?", answer "Monday" — the bridge slide has one line per shape, and that is all today needs.
- **Language.** They will hear "complement", "conditional", "independent", "expected value", "standard deviation", "distribution", "parameter". Write each one on the board the first time it is said.
