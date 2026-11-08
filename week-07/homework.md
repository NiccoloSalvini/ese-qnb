# Homework 7 — due Sunday 15 November, 23:59 on Moodle

**Two parts.** Part 1 is done on paper (photograph or scan it); Part 2 is a short typed text. Upload both to Moodle as one PDF. Expect about two hours. We go through it together at the start of next Monday's session — bring what you tried, even where you got stuck: the mistakes are the useful part.

Allowed, as in class: a calculator, the standard normal table or `NORM.S.DIST`, paper. Show all work: formula, substitution, number, one sentence. A bare number is not an answer.

## Part 1 — Drill set (paper, show all work)

**H1 — a number with its shares** *(Homework 6's H3, moved here: it needs today's block A)*.

(a) Walk-in visitors on the last six days: 12, 9, 15, 10, 14, 12. Compute the mean, the sample variance and the standard deviation by hand, in a table with the deviations and their squares.
(b) Test-ride bookings a day, from last year's data:

| bookings a day $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| $P(x)$ | .10 | .25 | .30 | .25 | .10 |

Check that the shares add to 1, then compute $E(x)$, $\sigma^{2}$ and $\sigma$ in a table with the columns $x$, $P(x)$, $x\,P(x)$, $x - \mu$, $(x - \mu)^{2}\,P(x)$. Write one sentence for the founder with a "give or take".

**H2 — the binomial.** Arno Bikes sends 20 financing quotes a week; one quote in five turns into a sale, each independently.

(a) Name the model and say in one line why it fits.
(b) Find the probability of exactly 4 sales. Write the four steps: the ways, $p^{x}$, $(1-p)^{n-x}$, multiply.
(c) Find the probability of no sale and of at least one sale.
(d) Find the mean and the standard deviation of the number of sales, and write one sentence for the founder.

**H3 — the Poisson.** Bikes come back under warranty at random, 5 a week on average (five working days).

(a) In one working day: write $\mu$ first, then find the probability of no return, of exactly one, and of at least two.
(b) In two weeks: write $\mu$ first, then find the probability of exactly 10 returns.
(c) In one sentence: what makes this a Poisson count and not a binomial one?

**H4 — the normal, and a guarantee.** A full charge of an Arno battery takes 240 minutes on average, standard deviation 20 minutes, bell-shaped: $X \sim N(240,\,20)$. For each part: sketch and shade, standardise, table, one sentence.

(a) What share of charges take more than 270 minutes?
(b) What share take between 220 and 260 minutes? Which rule of thumb gives the same answer without a table?
(c) The 10% slowest charges are flagged for a battery check. From how many minutes is a charge flagged? End in minutes, not in $z$.
(d) Marketing wants to print "fully charged in X minutes" and the Board accepts that 5% of charges take longer. What do we print?

**H5 — a decision with chance in it.** Deliveries can go with one of two couriers. **Fast** charges a flat **€40** per delivery and is never late. **Local** charges **€30** but is late 10% of the time, and a late delivery costs Arno Bikes **€60** in compensation to the customer.

(a) Draw the decision tree: the square, a circle for Local's chance node, the probabilities, the cost at each end node.
(b) Find the expected cost of a Local delivery, and the saving per delivery against Fast.
(c) Find the standard deviation of the cost of a Local delivery.
(d) Arno Bikes makes 400 deliveries a month. Expected monthly saving with Local? Then, in two sentences for the Board: which courier for the monthly volume, which for a single delivery to the firm's most important customer, and why the answer can differ.

**H6 — the normal approximation.** Arno Bikes sold 200 bikes last quarter; one bike in ten comes back under warranty within the year, independently.

(a) Name the exact model and give the mean and standard deviation of the number of returns.
(b) Check that the bell may be used. Then find the probability of 25 or more returns, with the four steps and the half unit.
(c) Find the probability of 14 or fewer returns.
(d) One sentence for the founder, with both numbers.

## Part 2 — Memo to the Board (150–250 words, typed)

You are the product manager of Arno Bikes. Engineering measured 200 bikes on the same loop: range 90 km on average, standard deviation 8 km, bell-shaped. Marketing wants one number on the box. Write a memo to the Board answering one question: **what range do we print, and why?**

Rules: numbers and their meaning, no formulas in the text (one small table in an appendix if you want). Give the Board the share of riders who will see less than the printed figure for at least two candidate numbers, say which one you recommend and what it costs in complaints, and say in one line what would change if the spread were 12 km instead of 8.

It will be read for clarity and for whether the numbers are right, not for length.

## Self-check before submitting

- The deviations sum to zero before you square them; the variance of the list divides by $n - 1$, the variance of the random variable uses the shares.
- Every count model is named before the formula, and $\mu$ is written as rate × interval before any Poisson number.
- Every normal question has a sketch with the area shaded, and the last line is a sentence in minutes, bikes or euros — not a $z$.
- Every decision has two numbers next to it: the expected value and the spread, and the sentence says what each one means.
- The normal approximation starts with $np$ and $\sqrt{np(1-p)}$, checks both are at least 5, and uses the half unit.
- The memo has no formulas and ends with one recommendation.
