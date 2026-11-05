# Homework 6 — due Sunday 8 November, 23:59 on Moodle

**Two parts.** Part 1 is done on paper (photograph or scan it); Part 2 is a short typed text. Upload both to Moodle as one PDF. It is short on purpose — we meet again on Monday morning — and should take about an hour. We go through it together at the start of Monday's session; bring what you tried, even where you got stuck.

Allowed: a calculator and paper. Show all work: formula, substitution, number, one sentence. A bare number is not an answer.

## Part 1 — Drill set (paper, show all work)

**H1 — sets, Venn, counting.** In October 180 customers bought from Arno Bikes. 110 bought a helmet ($H$), 75 bought a lock ($L$), 30 bought neither.

(a) Define in one full sentence each: *universal set*, *complement*, *intersection*. Use the customers as the example.
(b) How many bought both? Draw the two circles and fill in all four regions; check that they add to 180.
(c) A customer is picked at random. Find $P(H \cup L)$ with the addition law, and $P(\text{neither})$ as a complement.
(d) The window display has room for 3 of the 10 models. How many different displays? If the 3 are lined up left to right and the order is part of the display, how many? One line: which question decides between the two numbers?

**H2 — two-way table and Bayes.** Batteries come from two suppliers. **Celle** sends 65% of them and 3% of Celle's batteries are faulty; **Ionix** sends 35% and 8% of Ionix's are faulty. Last quarter Arno Bikes received 2,000 batteries.

(a) Build the two-way table of counts (supplier × good/faulty).
(b) Find $P(\text{faulty} \mid \text{Celle})$ and $P(\text{Celle} \mid \text{faulty})$, and say in one sentence what each one answers.
(c) Are supplier and fault independent? Compare the rows before you say the word.
(d) A faulty battery is on the bench, label gone. Use Bayes, written out, to find the probability it came from Ionix. Compare with Ionix's share of deliveries.

**H3 — a random variable.**

(a) Walk-in visitors on the last six days: 12, 9, 15, 10, 14, 12. Compute the mean, the sample variance and the standard deviation by hand, in a table with the deviations and their squares.
(b) Test-ride bookings a day, from last year's data:

| bookings a day $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| $P(x)$ | .10 | .25 | .30 | .25 | .10 |

Check that the shares add to 1, then compute $E(x)$, $\sigma^{2}$ and $\sigma$ in a table with the columns $x$, $P(x)$, $x\,P(x)$, $x - \mu$, $(x - \mu)^{2}\,P(x)$. Write one sentence for the founder with a "give or take".

## Part 2 — Memo to the founder (100–150 words, typed)

You run quality at Arno Bikes. Using your H2 table, write a short memo to the founder answering one question: **which supplier is the faulty battery most likely from, and what do we do about it?**

Rules: numbers and their meaning, no formulas in the text. Give the founder the share for each supplier, say in one line why the smaller supplier can still be the likelier culprit, and end with one recommendation — audit, renegotiate, switch, or wait for more batteries — and the reason in one sentence.

It will be read for clarity and for whether the numbers are right, not for length.

## Self-check before submitting

- Every definition is a full sentence that starts "the set of…", with an Arno Bikes example.
- The four regions of the Venn diagram add to the total, and "both" was found from "at least one", not guessed.
- Every "given" has its denominator named: a row total or a column total, and you said which.
- The deviations sum to zero before you square them; the variance of the list divides by $n - 1$, the variance of the random variable uses the shares.
- The memo has no formulas and ends with one recommendation.
