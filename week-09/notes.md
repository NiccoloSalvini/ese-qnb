# Week 9 — Read the output, then read the calendar

**Monday 23 November 2026, 10:00–13:00, online · Vincenzo Nardelli**

Students fit one simple line by hand (the line was not reached in week 8), see where the same line is used across business, explain how a coefficient changes when a predictor is held fixed, check the four assumptions of the linear model (LINE) on the residuals, and see the I of LINE break over time — then fix it with the season and with last month (AR(1)), the autoregressive model the syllabus names.

| Time | Activity | Teaching prompt |
|---|---|---|
| 10:00–10:25 | Homework 8, H1–H4 and memo | H1: the half unit, .187 vs .014. H2: 1.645, not 1.96, for a one-sided loss. H3: the three wrong roads. H4: the damage rate stays at 6.8% — why does the p-value fall from .091 to .017? Memo: one student puts the complaint result into words. |
| 10:25–10:50 | A · Temperature and range | Elicit a guess in km per degree. The table by hand, the clip, $R^2$; then the model behind the line (ε, residuals 0, 0, +1, −2, +1) and LINE in one table; move the 20 °C point in the app. |
| 10:50–10:58 | Homework 8, H5 | The same table on their data: 86/40 = 2.15, 39.4; $R^2$ .953. Ask who could not do it last week: now they can. |
| 10:58–11:06 | The same line, everywhere | Departments table (ask the chat which row is closest to their job), the beta of a stock (a −4% market month gives −5.0%), other sectors. Read, don't compute. |
| 11:06–11:20 | Read the sales output · D1 | One sentence with a coefficient, one with its interval. Ask what other activities vary with advertising. |
| 11:20–11:35 | Break | — |
| 11:35–12:00 | B · Held fixed · D2 | Plans A, B, C; 5.53 vs 2.94; the held-fixed app (move the hours); the loaded rides (+7 −8 = −1 km); the discount with its p-value .23; D2. |
| 12:00–12:17 | C · When the assumptions break · D3 | Back to LINE from block A: what breaks and what we do; the residual-check app, five cases; D3 (four residual plots in words). |
| 12:17–12:52 | D · Time · D4 | The straight trend leaves a pattern (summer +90, winter −65); web orders remember last month (r = .59); the time-errors app; the two fixes; quarterly trend + season (Q1 = 429.5); AR(1) on web orders (105.8, 103.3, 99.5) and the clip; D4. |
| 12:52–13:00 | Debrief and Homework 9 | A sentence naming a slope, its units and what stays fixed. Assign H1–H4 and the production memo. |

Data: lectures/data/w09_sales_demos.csv (ads and test-ride hours), w09_quarters.csv, w09_orders.csv. Every number on the slides is refitted in lectures/check_w09.py.

**If time runs short:** the "other sectors" slide; the loaded rides; the AR(1) clip (keep its output and the forecasts). **Never cut:** the line by hand, 5.53 vs 2.94, LINE, the violation and its two fixes.

The optional time-series drills (moving average, AR(1)) give students extra practice at home.
