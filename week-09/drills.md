# Week 9 — Drills

*One drill per block, on paper, during the session. Today is reading, not computing: every number you need is in the output; the marks are in the sentences. For each coefficient say its units, its sign, and what is held fixed. The case is Arno Bikes throughout. Solutions at the end.*

## A. Reading a regression output

**D1 (8 minutes).** For 20 months, the bikes sold by the out-of-town shop were regressed on the number of test-ride Saturdays it held in the month. The output:

| | coefficient | std. error | $t$ | p-value |
|---|---:|---:|---:|---:|
| intercept | 18.4 | 6.2 | 2.97 | .008 |
| test-ride Saturdays | 4.2 | 1.5 | 2.80 | .012 |

$n = 20$ · $R^{2} = .30$

(a) Interpret the slope in one sentence, with its units.
(b) Which hypothesis does the p-value .012 test? What do you conclude at the 5% level, in words?
(c) The approximate 95% interval for the slope is 1.2 to 7.2 bikes. What does it tell the founder that the coefficient alone does not?
(d) What does $R^{2} = .30$ say? Name one thing, other than test rides, that could explain the rest.

## B. Held fixed

**D2 (8 minutes).** 36 shop-months. Bikes sold regressed on ad spend $A$ (€ thousand) and the price discount $D$ (percentage points):

| | coefficient | std. error | p-value |
|---|---:|---:|---:|
| intercept | 22.1 | 3.0 | < .001 |
| ads (€ thousand) | 2.8 | 0.6 | < .001 |
| discount (points) | 1.1 | 0.9 | .23 |

(a) Interpret both slopes, each in a sentence that says what is held fixed.
(b) The discount's p-value is .23. What does it mean, and what does it **not** mean?
(c) A colleague regresses sales on the discount **alone** and finds a slope of 2.5 with p = .01. Give one reason why the discount looks stronger on its own.
(d) At €4,000 of ads, how much more does a 7% discount sell than a 5% one, according to the model?

## C. The assumptions

**D3 (6 minutes).** Four regressions, four residual plots, described in words. For each: which assumption (L, I, N, E) — or which problem — is at stake, what it costs, and what you would do.

(a) Residuals of delivery time against distance: positive for short and long routes, negative in the middle.
(b) Residuals of monthly sales against ad spend: small when ads are low, very large when ads are high.
(c) Residuals of weekly orders, in time order: ten weeks above zero, then eight below, then nine above.
(d) Residuals of repair cost against bike age: no pattern, except one bike with a residual of +900 € when all the others are within ±100 €.

## D. Time

**D4 (8 minutes).**

(a) A straight trend is fitted to quarterly helmet sales. Its residuals are about +20 in every fourth quarter and about −10 in every first quarter, year after year. Which assumption is broken? What do you add to the model?
(b) Test-ride bookings, regressed on last month's bookings: $\hat{y}_t = 24 + 0.7\,y_{t-1}$, with p < .001 for 0.7. Interpret 0.7 in one sentence.
(c) Last month there were 90 bookings. Forecast next month, and say where the series settles in the long run.
(d) Would you trust the p-value of a regression of monthly sales on ad spend, fitted on five years of months, without looking at the residuals in time order? Why?

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) Each extra test-ride Saturday goes with about **4 more bikes** sold in the month.

(b) $H_0$: the slope is zero — test-ride Saturdays have no linear relation with sales. p = .012 < .05: reject. A relation this strong would rarely appear by luck if there were none.

(c) The effect is positive, but known only roughly: anywhere from **about 1 to about 7 bikes** per Saturday. Budgeting on exactly 4.2 would be over-precise.

(d) Test-ride Saturdays explain **30%** of the month-to-month differences in sales; 70% comes from other things — ad spend, the weather, the season, the price, the competition.

**D2.**

(a) **Ads**: at the same discount, €1,000 more ads goes with about 2.8 more bikes. **Discount**: at the same ad spend, one more point of discount goes with about 1.1 more bikes.

(b) With these 36 months we cannot tell the discount's effect from zero, once ads are held fixed: a slope this far from zero would turn up by luck 23 times in 100. It does **not** mean the discount does nothing: the effect may be small, or the data too few to see it (its interval runs from about −0.7 to 2.9).

(c) Months with deep discounts are probably months with more ads too. On its own, the discount takes the credit for the ads that came with it; with ads held fixed, that credit goes back to ads. (The same as 5.53 against 2.94 in class.)

(d) Two more points × 1.1 = **2.2 more bikes** (38.8 against 41.0) — but with p = .23, even the direction is uncertain.

**D3.**

(a) **L, linearity.** The relation bends: the line is wrong at both ends. Add distance squared, or a log.
(b) **E, equal spread** (a fan). The slope can still be right on average, but the standard errors and p-values are off. Take the log of sales, or use robust standard errors.
(c) **I, independence.** Long streaks mean one week's error tells you the next: the standard errors are too small and the p-values too optimistic. Model the time: a trend, a season, or last week's orders.
(d) **An outlier**, not a broken assumption as such: one bike can pull the whole line. Check that row (a typo? a special repair?) and report the line with and without it.

**D4.**

(a) **I, independence**: the error repeats with the calendar, so one quarter's error predicts next year's. Add the season — a gap for each quarter (here the fourth quarter about +20 and the first about −10).

(b) This month keeps **70%** of last month's gap from the average: a strong month is followed by a strong month, and the memory fades slowly.

(c) $24 + 0.7 \times 90 = \mathbf{87}$ bookings next month. In the long run it settles at $24 / (1 - 0.7) = \mathbf{80}$.

(d) No. Months follow one another: if the errors come in streaks, the standard errors are too small and the p-value too optimistic. Plot the residuals in time order first.

</details>

## Optional practice: the moving average

<details>
<summary>Naive forecast against a 3-month average, with the worked solution</summary>

Monthly sales of the cargo model: 80, 86, 83, 90, 88, 95.

(a) Forecast months 4, 5 and 6 with the naive method (next month = this month) and with the 3-month moving average, and compute the mean absolute error (MAE) of each. Which method wins here, and why?
(b) Forecast month 7 with both methods.

**Solution.**

| month | sold | naive | error | 3-month average | error |
|---|---:|---:|---:|---:|---:|
| 4 | 90 | 83 | 7 | 83.0 | 7.0 |
| 5 | 88 | 90 | 2 | 86.3 | 1.7 |
| 6 | 95 | 88 | 7 | 87.0 | 8.0 |
| | | | MAE **5.33** | | MAE **5.56** |

The **naive** method wins, just: sales are climbing, and the average of the last three lags behind a rising series.
Month 7: naive **95**; moving average $(90 + 88 + 95)/3 = \mathbf{91}$.

</details>
