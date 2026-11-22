# Week 8 — How sure are we of that number?

**MBA03 Research & Quantitative Business Methods · Mon 16 Nov 2026, 10:00–13:00, online (Google Meet) · Tutor: Vincenzo Nardelli**

Syllabus topic (weeks 8–9 share one list: OLS regression and correlation, hypothesis testing, confidence intervals, time series, autoregressive models). The split is ours: **week 8 covers inference; week 9 begins with the least-squares line by hand, compares multiple regression models, then forecasts with trend and seasonality.** Announce it once.

Running case, as in weeks 1–7: **Arno Bikes**. The thread: last week a known shape gave a share of bikes; today the arrow turns round, from one sample back to an unknown number, with its standard error. Lesson 7's block E (a count read as a bell, the Monte Carlo) opens block A.

## Learning objectives

By the end of the session the students can:

1. **Read a big count as a bell** (check $np \ge 5$, the half unit) and **compute a standard error** $\sigma/\sqrt{n}$, saying what the CLT does and does not do — the final's normal items; the base of 2–3.
2. **Construct and choose** a confidence interval for a mean with σ known at 90% and 95%, name the three wrong roads, state the confidence sentence, and size a sample for a target margin — the final's interval item, in its multiple-choice form.
3. **Test** a proportion two-tailed at 5% in six steps, write the p-value in words, and link a test on a mean to the interval — the final's test item.
4. Also rehearsed in the Homework 7 review: **the maximum loss at 95%** (the guarantee backwards, in euros) — the final's portfolio item.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:20 | Homework 7, step by step | Slides | Recap, H1–H5 and the memo; the "same move, in euros" slide (maximum loss at 95%: €3,290). |
| 10:20–10:25 | Opening | Slides | Where we are, today's question, the hub. |
| 10:25–10:45 | **A. Will we pay the courier's penalty?** | Slides → app → clip | 250 orders at 6%: $N(15, 3.755)$, half unit, .115 (exact .118); Monte Carlo in one slide + app; one bike vs the average of 16 (SE 2) + clip; the SE table and the CLT in three lines. |
| 10:45–10:53 | **D1** | Paper | 300 orders at 5%; SE of 25 and 100 charges; the average above 248. |
| 10:53–11:20 | **B. How far off is our 90 km?** | Slides → clip → app | 64 bikes, 88.5 km, σ 8: SE 1, 95% 86.54–90.46, 90% 86.86–90.15; the four-option choice with three wrong roads; the clip; what 95% means; the app; 246 bikes for ±1 km. |
| 11:20–11:28 | **D2** | Paper | €84, σ 18, n 36: two intervals, the choice, 312 customers. |
| 11:28–11:43 | Break | — | Cameras off. |
| 11:43–12:12 | **C. Has dropping Ionix cut returns?** | Slides → clip | 8% before; 22 of 400 after: six steps, z −1.84, p .066, do not reject; the clip; 800 bikes, same 5.5%, z −2.61, p .009; Type I/II in words; the mean test (z −1.5, p .134) and the interval agree. |
| 12:12–12:20 | **D3** | Paper | One rider in four; 90 of 300 with the new script: z 2.00, p .046, reject — only just. |
| 12:20–12:50 | Guided practice and questions | Paper | Revisit D2 and D3. Ask each group to explain one interval or test result to the founder. |
| 12:50–13:00 | Take home, three answers, homework | Slides | Three answers; formula page; Homework 8 (due Sun 22 Nov). |

No quiz this week (the in-class quiz is in week 10).

## Script

### Homework 7 (20')

One click per step, say the step before clicking. **H1**: the deviations sum to zero; 26/5, not 26/6. **H2**: the four steps, 4,845. **H3**: μ = 1 a day before anything. **H4(c)**: the bad tail is on the right, 272.9 → print 275 (273 accepted); the slip is 207. Then the **euro slide**: same move, mean 0, σ €2,000, the worst 5% of days on the left: €3,290. Say it is the final's portfolio item in form, and that it is last week's guarantee with another unit. **H5**: €36, €18, €1,600. **Memo**: the table at σ 8 and 12; the best memos price the consistency (6 km on the box).

### A. Will we pay the courier's penalty? (20')

Bet: how often a penalty month. $np = 15$, $\sigma = 3.755$; "20 or more" starts at 19.5; $z = 1.20$, .115. Exact .118. **Monte Carlo** in one slide; app with `?n=250&p=0.06&k=20&label=orders`: run 1,000 months. **One bike vs sixteen**: bet on the SE; $8/\sqrt{16} = 2$; last fragment: an average of 16 above 94 km, $z = 2$, .023 against .31 for one bike (D1(c) needs it). **Clip** `w08_samples`. The SE table (four times the bikes, half the error) and the CLT in three lines: the data do not become a bell, their average does; σ vs SE; a big wrong sample is still wrong. Board sentence.

### B. How far off is our 90 km? (27')

Bet: a 95% range. SE = 1, ±1.96. 90 is inside: no evidence the batch is worse. The table with 90/95/99. **The choice** (the exam form): four options; ask the chat for the letter before clicking; name the three wrong roads. **Clip** `w08_intervals`: one interval in twenty misses. Right and wrong sentence for "95%". **App** `w08_intervals`: 100 draws at 95% and 90%; n 16. **Sample size**: 246, round up; 984 for ±0.5.

### C. Has dropping Ionix cut returns? (29')

Bet: "changed" or "luck". $H_0$ is the boring story. The six-step table, one row at a time; insist on the SE **under $H_0$** (with .08, not .055). p = .066: do not reject. **Clip** `w08_pvalue`. The p-value in words; then 800 bikes: same share, other verdict — data buy certainty. Type I and II in two lines. Last slide: the mean test and the interval are one calculation.

Do not show an interval for the proportion here: built with $\hat{p}$ it excludes .08 while the test (built with $p_0$) does not reject, and the two standard errors are a detour we do not need.

### Take home (10')

The three answers (ask the chat before each); formula page; Homework 8, due Sunday 22 November, 23:59. Last sentence: "Next Monday we fit a line to five test rides and read its slope in kilometres per degree."

## Cut order if late

1. The 99% row and the ±0.5 km line in block B; the Type I/II box in block C.

**Never cut:** the SE, the interval and the choice with the wrong roads (B), the six steps and the p-value in words (C), the euro slide in the homework review.

## Board, slide, screen

Online: the shared deck is the board, the chat is the slip. Bets go in the chat before the click. Drills: share `drills.md` (section by section) and a visible timer; the solution is said aloud from `drills_notes.pdf`.

## Tutor's notes

- **Table rounding.** $z$ to two decimals: 1.198 → 1.20 (.115; software .1151), −1.843 → −1.84 (.0329 per tail), −2.606 → −2.61. Accept the software values.
- **"95% sure the true mean is in this interval"** is tolerated in speech; insist on the version "19 intervals in 20" in writing.
- **"Do not reject" is not "accept".** Say it once with the 800-bike slide.
