# Homework 7 — due Sunday 15 November, 23:59 on Moodle

**Two parts.** Part 1 is done on paper (photograph or scan it); Part 2 is a short typed text. Upload both to Moodle as one PDF. Expect about two hours. We go through it together at the start of next Monday's session — bring what you tried, even where you got stuck: the mistakes are the useful part.

Allowed, as in class: a calculator, the standard normal table or `NORM.S.DIST`, paper. Show all work: formula, substitution, number, one sentence. A bare number is not an answer.

## Part 1 — Drill set (paper, show all work)

**H1 — sets and counting.** Last month 240 people visited the Arno Bikes showroom. 140 took a test ride ($T$), 80 asked for a financing quote ($F$), 60 did neither.

(a) Define in one full sentence each: *universal set*, *subset*, *union of two sets*. Use the visitors as the example.
(b) How many visitors did both? Draw the two circles and fill in all four regions.
(c) A visitor is picked at random. Find $P(T \cup F)$ with the addition law, and $P(\text{neither})$ as a complement.
(d) The window display has room for 4 of the 9 models. How many different displays? If the 4 are lined up left to right and the order is part of the display, how many?

**H2 — conditional probability and Bayes.** Bikes are shipped by two couriers. **Fast** carries 75% of deliveries and is late 4% of the time; **Local** carries 25% and is late 10% of the time. Last month there were 400 deliveries.

(a) Build the two-way table of counts (courier × on time/late).
(b) Find $P(\text{late} \mid \text{Fast})$ and $P(\text{Fast} \mid \text{late})$, and say in one sentence what each one answers.
(c) Are courier and lateness independent? Compare the rows before you say the word.
(d) A customer complains about a late delivery; the paperwork is lost. Use Bayes, written out, to find the probability it was Local. Compare with Local's share of deliveries.

**H3 — a random variable and the binomial.**

(a) Daily demand for the cargo model, from last year's data:

| bikes a day $x$ | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|
| $P(x)$ | .05 | .30 | .35 | .20 | .10 |

Check that the shares add to 1, then compute $E(x)$, $\sigma^{2}$ and $\sigma$ in a table with the columns $x$, $P(x)$, $x\,P(x)$, $x - \mu$, $(x - \mu)^{2}\,P(x)$. Write one sentence for the founder.
(b) Arno Bikes sends 15 financing quotes a week; one quote in five turns into a sale, each independently. Name the model and say why. Find the probability of exactly 3 sales, the probability of at least one sale, and the mean and standard deviation of the number of sales.

**H4 — the Poisson.** The helpline receives 3 calls an hour on average, at random.

(a) In a 20-minute coffee break: write $\mu$ first, then find the probability of no call, of exactly one call, and of at least two calls.
(b) In a two-hour window: write $\mu$ first, then find the probability of exactly 6 calls.
(c) In one sentence: what makes this a Poisson count and not a binomial one?

**H5 — the normal, mixed.** Battery range is $N(90 \text{ km},\, 8 \text{ km})$; bike weight is $N(22 \text{ kg},\, 1.5 \text{ kg})$. For each part: sketch and shade, standardise, table, one sentence.

(a) What share of bikes have a range above 100 km?
(b) What share have a range between 80 and 100 km?
(c) The Board accepts 10% of riders seeing less than the printed range. What range should be printed? End in km, not in $z$.
(d) A customer wants a bike under 20 kg. What share of bikes qualify?

## Part 2 — Memo to the Board (150–250 words, typed)

You are the product manager of Arno Bikes. Engineering measured 200 bikes on the same loop: range 90 km on average, standard deviation 8 km, bell-shaped. Marketing wants one number on the box. Write a memo to the Board answering one question: **what range do we print, and why?**

Rules: numbers and their meaning, no formulas in the text (one small table in an appendix if you want). Give the Board the share of riders who will see less than the printed figure for at least two candidate numbers, say which one you recommend and what it costs in complaints, and say in one line what would change if the spread were 12 km instead of 8.

It will be read for clarity and for whether the numbers are right, not for length.

## Self-check before submitting

- Every definition is a full sentence that starts "the set of…", with an Arno Bikes example.
- Every "given" has its denominator named: a row total or a column total, and you said which.
- Every count model is named before the formula, and $\mu$ is written as rate × interval before any Poisson number.
- Every normal question has a sketch with the area shaded, and the last line is a sentence in km, kg or minutes — not a $z$.
- The memo has no formulas and ends with one recommendation.
