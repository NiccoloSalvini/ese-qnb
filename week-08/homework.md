# Homework 8 — due Sunday 22 November, 23:59 on Moodle

**Two parts.** Part 1 is done on paper (photograph or scan it); Part 2 is a short typed text. Upload both to Moodle as one PDF. Expect about two hours. We go through it together at the start of next Monday's session — bring what you tried, even where you got stuck: the mistakes are the useful part.

Allowed, as in class: a calculator, the standard normal table or `NORM.S.DIST`, paper. Show all work: formula, substitution, number, one sentence. A bare number is not an answer. Read $z$ to two decimals, as the table does.

## Part 1 — Drill set (paper, show all work)

**H1 — a big count read as a bell.** Arno Bikes ships 400 orders in December; each is late with probability .04, independently. The courier's penalty starts at 20 late orders.

(a) Check that the normal can be used, and find the mean and the standard deviation of the number of late orders.
(b) Find the probability of a penalty month. Use the half unit.
(c) A new courier promises a late rate of 3%. Find the probability of a penalty month with it, and write one sentence for the founder.

**H2 — the standard error, and the worst week.**

(a) A full charge takes 240 minutes on average, standard deviation 20. Find the standard error of the average of 16 charges and of 64 charges. How many charges do we need for a standard error of 1 minute?
(b) The cash fund's value changes every **week** by zero on average, standard deviation **€4,500**, bell-shaped. Find the maximum weekly loss at 95%, and at 99% ($z = 2.33$). Write one sentence for the founder for each.

**H3 — an interval, and how many to ask.** 49 customers, chosen at random, spent on average **€126** on servicing last year. From past years, σ = **€21**.

(a) Find the standard error.
(b) Construct the 90% and the 95% confidence intervals for the average spend of all customers.
(c) Select the correct 95% interval and say what went wrong in each of the others: (i) €121.07 to €130.94; (ii) €84.84 to €167.16; (iii) €120.12 to €131.88; (iv) €125.16 to €126.84.
(d) How many customers must we survey to know the average within **€2.50**, at 95%?

**H4 — a test on a proportion.** For years, 10% of online orders arrived with a damaged box. With new packaging, **17 of 250** orders arrived damaged.

(a) State $H_0$ and $H_1$ for a two-tailed test.
(b) Test at the 5% level in six steps, and write the p-value in words.
(c) Repeat the test assuming instead that **34 of 500** orders arrived damaged — the same share. What changes, and why?

**H5 — a line through five points.** Five months: price discount $x$ (%) and bikes sold $y$.

| $x$ | 0 | 2 | 4 | 6 | 8 |
|---|---:|---:|---:|---:|---:|
| $y$ | 40 | 43 | 49 | 50 | 58 |

(a) Find the least-squares line $\hat{y} = a + b\,x$ by hand, in a table.
(b) Interpret the slope in one sentence.
(c) The squared distances from $\bar{y}$ add to 194, those left by the line to 9.1. Find $R^{2}$ and $r$.
(d) Predict sales at a 5% discount. Would you use the line for a 25% discount? Why not?

## Part 2 — Memo to the Board (150–250 words, typed)

You run customer service at Arno Bikes. For years, **12%** of helpline calls ended in a formal complaint. Last month a new call script was introduced: of **500 calls**, **45** ended in a complaint.

Write a memo to the Board answering one question: **has the new script cut complaints?**

Rules: numbers and their meaning, no formulas in the text (one small table in an appendix if you want). Say what "nothing changed" would predict, how far the data are from it, the p-value in one sentence of plain words, your conclusion at the 5% level, and one recommendation for what to do next. It will be read for clarity and for whether the numbers are right, not for length.

## Self-check before submitting

- Every count read as a bell has its check ($np \ge 5$, $n(1-p) \ge 5$) and its half unit.
- Every standard error divides σ by $\sqrt{n}$, not by $n$, and every interval says 90% or 95% and uses the matching $z$.
- Every test writes $H_0$ and $H_1$ first, uses the standard error **under $H_0$**, doubles the tail for a two-tailed p-value, and ends in a sentence, not in "reject".
- The line has its table, its two sums, and a slope read in units of the business.
- The memo has no formulas and ends with one recommendation.
