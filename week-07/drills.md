# Week 7 — Drills

*One drill per block, on paper, in class. Show all work: formula, substitution, number, one sentence for the founder. The case is Arno Bikes throughout; the numbers are new. Solutions at the end.*

## A. Counting

**D1 (3 minutes).** The founder sends 2 of the 6 mechanics to a training course.

(a) How many different pairs can go? Write the formula, cancel, then the number.
(b) If one of the two is the **lead** and the other the **assistant**, how many possible assignments?
(c) In one line: why is (b) exactly twice (a)?

## B. Conditional probability and Bayes

**D2 (8 minutes).** Motors come from two suppliers. **Rotor** sends 60% of them and 3% of Rotor's motors are faulty; **Spin** sends 40% and 6% of Spin's are faulty. Last month Arno Bikes received 500 motors.

(a) Build the two-way table of counts (supplier × good/faulty).
(b) Find $P(\text{faulty} \mid \text{Rotor})$ and $P(\text{Rotor} \mid \text{faulty})$. Say in one sentence why they are different questions.
(c) Are supplier and fault independent? Compare the rows, then say the word.
(d) A faulty motor is on the bench. Use Bayes, written out, to find the probability it came from Spin. Compare with Spin's share of deliveries.

## C. Mean and variance, binomial, Poisson

**D3 (8 minutes).**

(a) Warranty claims in the last six weeks: 2, 5, 3, 6, 4, 4. Compute the mean, the sample variance and the standard deviation by hand, in a table with the deviations and their squares.
(b) Saturday brings 10 test rides; from the CRM, three riders in ten buy, each deciding alone. Name the model and say why. Find the probability that exactly 2 buy, that nobody buys, that at least one buys, and the mean and standard deviation of the number of buyers.
(c) Orders on the web shop arrive at random, 4 an hour on average. Name the model and say why. Find the probability of no order in an hour and of exactly 2 orders in an hour. Then, for a 15-minute coffee break: write $\mu$ first, then the probability of no order and of at least one.

## D. The normal

**D4 (8 minutes).** A full charge of an Arno battery takes 240 minutes on average, standard deviation 20 minutes, bell-shaped: $X \sim N(240,\,20)$. For each part: sketch and shade, standardise, table, one sentence.

(a) What share of charges take more than 270 minutes?
(b) What share take between 220 and 260 minutes? Which rule of thumb gives the same answer without a table?
(c) The 10% slowest charges are flagged for a battery check. From how many minutes is a charge flagged? End in minutes, not in $z$.
(d) Delivery times to customers have a mean of 3.1 days and a median of 2.4 days. In one sentence: what shape is that, and why is the table the wrong tool for it?

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) A pair is a pair, order does not matter — combinations:

$$\binom{6}{2} = \frac{6!}{2!\,(6-2)!} = \frac{6!}{2!\,4!} = \frac{6 \cdot 5 \cdot \cancel{4!}}{2 \cdot 1 \cdot \cancel{4!}} = \frac{30}{2} = \mathbf{15} \text{ pairs}$$

Fifteen different pairs of mechanics can go on the course.

(b) Lead and assistant are named roles, order matters — permutations:

$$P^{6}_{2} = \frac{6!}{(6-2)!} = \frac{6!}{4!} = 6 \cdot 5 = \mathbf{30} \text{ assignments}$$

Two decisions in a row: 6 choices for the lead, 5 left for the assistant. Thirty different lead–assistant assignments.

(c) Each pair can take the two roles in $2! = 2$ ways: $15 \times 2 = 30$. The $2!$ underneath in (a) removes exactly those orderings.

**D2.**

(a) Counts from the three facts. Rotor: $0.60 \times 500 = 300$ motors, $0.03 \times 300 = 9$ faulty, $300 - 9 = 291$ good. Spin: $0.40 \times 500 = 200$ motors, $0.06 \times 200 = 12$ faulty, $200 - 12 = 188$ good.

| | good | faulty | total |
|---|---:|---:|---:|
| **Rotor** | 291 | 9 | 300 |
| **Spin** | 188 | 12 | 200 |
| **total** | 479 | 21 | 500 |

(b) Same cell, 9, on top; a different total underneath.

$$P(\text{faulty} \mid \text{Rotor}) = \frac{9}{300} = \mathbf{.03} \qquad \text{(Rotor's row: of Rotor's motors, what share is faulty)}$$

$$P(\text{Rotor} \mid \text{faulty}) = \frac{9}{21} = \mathbf{.429} \qquad \text{(the faulty column: of the faulty motors, what share is Rotor's)}$$

The first answers "how good is Rotor"; the second answers "who sent this faulty one".

(c) Compare the rows with the total:

$$P(\text{faulty} \mid \text{Rotor}) = .03 \qquad P(\text{faulty} \mid \text{Spin}) = \frac{12}{200} = .06 \qquad P(\text{faulty}) = \frac{21}{500} = .042$$

The rows differ from each other and from the total: knowing the supplier changes the share of faulty, so supplier and fault are **dependent**. Had both rows read .042, the supplier would tell us nothing about the fault.

(d) Bayes is the faulty column in shares. First the three-column update, as on the slide:

| supplier | prior share | × defect rate | = faulty, as a share of all | ÷ total faulty |
|---|---:|---:|---:|---:|
| Rotor | .60 | .03 | .018 | .018 / .042 = **.429** |
| Spin | .40 | .06 | .024 | .024 / .042 = **.571** |
| total | 1.00 | | .042 | 1.00 |

Then the same table in symbols:

$$P(\text{Spin} \mid \text{faulty}) = \frac{P(\text{faulty} \mid \text{Spin})\,P(\text{Spin})}{P(\text{faulty} \mid \text{Rotor})\,P(\text{Rotor}) + P(\text{faulty} \mid \text{Spin})\,P(\text{Spin})}$$

$$= \frac{.06 \times .40}{.03 \times .60 + .06 \times .40} = \frac{.024}{.018 + .024} = \frac{.024}{.042} = \mathbf{.571}$$

Check with the counts: $12/21 = .571$. Spin sends 40% of the motors but is behind 57% of the faulty ones. The evidence moved the share up; a 40% supplier with twice the defect rate is the likelier culprit, not a certain one.

**D3.**

(a) The table first; the deviations must sum to zero before you square.

| week | claims $x$ | $x - \bar{x}$ | $(x - \bar{x})^{2}$ |
|---|---:|---:|---:|
| 1 | 2 | −2 | 4 |
| 2 | 5 | 1 | 1 |
| 3 | 3 | −1 | 1 |
| 4 | 6 | 2 | 4 |
| 5 | 4 | 0 | 0 |
| 6 | 4 | 0 | 0 |
| **sum** | **24** | 0 | **10** |

$$\bar{x} = \frac{\sum x}{n} = \frac{24}{6} = \mathbf{4}$$

$$s^{2} = \frac{\sum (x - \bar{x})^{2}}{n - 1} = \frac{10}{5} = \mathbf{2.0} \qquad s = \sqrt{2.0} = \mathbf{1.41}$$

About 4 claims a week, give or take 1.4.

(b) **Binomial**: a fixed number of trials ($n = 10$), each yes or no, the same $p = .3$ every time, each rider alone.

$$P(2) = \binom{10}{2}\, .3^{2}\, .7^{8} = 45 \times .09 \times .05765 = \mathbf{.233}$$

$$P(0) = .7^{10} = \mathbf{.028} \qquad P(\ge 1) = 1 - P(0) = 1 - .028 = \mathbf{.972}$$

$$np = 10 \times .3 = \mathbf{3} \text{ buyers} \qquad \sigma = \sqrt{np(1-p)} = \sqrt{10 \times .3 \times .7} = \sqrt{2.1} = \mathbf{1.45}$$

Expect three buyers, give or take one and a half; a Saturday with no sale happens about three times in a hundred.

(c) **Poisson**: orders arrive at random over time, at a constant rate, with no ceiling on the count. One hour, $\mu = 4$:

$$P(0) = \frac{4^{0} e^{-4}}{0!} = e^{-4} = \mathbf{.018} \qquad P(2) = \frac{4^{2} e^{-4}}{2!} = \frac{16 \times .01832}{2} = \mathbf{.147}$$

Fifteen minutes is a quarter of an hour, so $\mu$ first:

$$\mu = 4 \times \tfrac{1}{4} = 1 \qquad P(0) = e^{-1} = \mathbf{.368} \qquad P(\ge 1) = 1 - .368 = \mathbf{.632}$$

A silent hour is rare, two in a hundred; a silent coffee break happens more than once in three.

**D4.**

(a) Shade the right tail beyond 270.

$$z = \frac{x - \mu}{\sigma} = \frac{270 - 240}{20} = \frac{30}{20} = 1.50 \qquad \text{table, area to the left: } P(z < 1.50) = .9332$$

$$P(X > 270) = 1 - .9332 = \mathbf{.067}$$

About 7 charges in 100 take more than four and a half hours.

(b) Shade between 220 and 260.

$$z = \frac{220 - 240}{20} = -1 \qquad z = \frac{260 - 240}{20} = +1$$

Two lookups, area to the left of each, and a difference:

$$P(-1 < z < 1) = P(z < 1) - P(z < -1) = .8413 - .1587 = \mathbf{.683}$$

One $\sigma$ either side of the mean: the 68% rule, no table needed.

(c) Backwards: the area is given, $x$ is wanted. The slowest 10% is the right tail, so 90% of the area is to the left of the threshold. Find .9000 *inside* the table: between $z = 1.28$ (.8997) and $z = 1.29$ (.9015), nearer to 1.28, so $z = 1.28$ (Excel: `=NORM.S.INV(0.90)`). Undo the standardisation, solving $z = (x - \mu)/\sigma$ for $x$:

$$x = \mu + z\,\sigma = 240 + 1.28 \times 20 = 240 + 25.6 = \mathbf{265.6 \text{ minutes}}$$

A charge over about 266 minutes is flagged.

(d) Mean well above median: a long right tail, **positive skewness** — most parcels in two or three days, a few much later. The normal is symmetric (mean = median), so a $z$ from a mean of 3.1 would give the wrong areas: the table only answers questions about bells.

</details>
