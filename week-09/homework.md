# Homework 9 — due Sunday 29 November, 23:59 on Moodle

**Two parts.** Part 1 is done on paper (photograph or scan it); Part 2 is a short typed text. Upload both to Moodle as one PDF. Expect about an hour and a half. We go through it together at the start of next Monday's session, the review.

Today's rule holds: every number you need is in the output or in the exercise. The marks are in the sentences. A bare number is not an answer.

## Part 1 — Drill set (paper, show all work)

**H1 — one output, four sentences.** For 24 months, the hours worked in the Arno Bikes workshop were regressed on the number of bikes sold in the month.

| | coefficient | std. error | $t$ | p-value |
|---|---:|---:|---:|---:|
| intercept | 40.0 | 12.0 | 3.33 | .003 |
| bikes sold | 0.85 | 0.10 | 8.50 | < .001 |

$n = 24$ · $R^{2} = .77$

(a) Interpret the slope in one sentence, in hours and bikes. Does the intercept (40 hours in a month with no bike sold) mean something? Why?
(b) State the hypothesis the slope's p-value tests, and your conclusion at 5%, in words.
(c) Give an approximate 95% interval for the slope (± 2 standard errors) and say what it adds to the coefficient.
(d) Read $R^{2}$. Predict the workshop hours for a month with 300 bikes sold.

**H2 — planning delivery runs.** Dispatch uses the model $\widehat{\text{hours}}=0.90+0.012\,\text{km}+0.35\,\text{stops}$.

(a) Interpret both slopes, each with what is held fixed. How many minutes does one more stop add?
(b) Predict the duration of a 200 km run with four stops.
(c) Longer routes tend to include more stops. Explain why dropping stops from the regression would increase the estimated slope for distance.
(d) The manager concludes: "Each stop **causes** 21 extra minutes, so cutting two stops saves 42 minutes." What would you check before agreeing?

**H3 — trend and seasonal gaps.** Quarterly accessory sales have the trend $120 + 4t$ ($t = 1$ in the first quarter of the first year). The seasonal gaps are Q1 $-25$, Q2 $+10$, Q3 $+30$, Q4 $-15$. Forecast the first two quarters of the fourth year and explain why the forecasts differ.

**H4 — can we trust it?** Answer each in two or three sentences.

(a) A regression of monthly bike sales on ad spend, over 48 months, has $R^2 = .80$ and a slope with p < .001. Its residuals, in time order, stay above zero for most of the summer months and below zero for most of the winter months. Which assumption is broken? What does it cost, and what would you add to the model?
(b) Web orders follow $\hat{y}_t = 30 + 0.5\,y_{t-1}$. Last month: 80 orders. Forecast next month, and say where the series settles. Why does a forecast from this model not jump to 80 again?
(c) A colleague says: "$R^2$ is high, so the assumptions do not matter." Answer in two sentences.

## Part 2 — Memo to the production manager (150–250 words, typed)

You are the planner of Arno Bikes. Use the accessory series of H3: the trend $120 + 4t$ and its seasonal gaps.

Write a memo to the production manager answering one question: **how many accessory kits should we plan for each of the next two quarters, and how sure are we?**

Rules: numbers and their meaning, no formulas in the text. Give the two forecasts, say in one line where they come from (a growing trend, a seasonal shape), and say in one line what could make them wrong — a change the past cannot see. It will be read for clarity and for whether the numbers are right, not for length.

## Self-check before submitting

- Every coefficient is read in the units of the business, and in a multiple regression "with the others held fixed".
- Every p-value is linked to its hypothesis ("the slope is zero") and to a decision at 5%.
- Each forecast shows the quarter index, trend and seasonal adjustment.
- Every assumption you name comes with what it costs and what you would do.
- The memo has no formulas and ends with one recommendation.
