# Week 7 — Drills

*One drill per block, on paper, during the session. Show all work: formula, substitution, number, one sentence for the founder. The case is Arno Bikes throughout; the numbers are new. Solutions at the end.*

## A. Mean and variance, a random variable

**D1 (8 minutes).**

(a) Warranty returns in the last five weeks: 3, 8, 5, 6, 8. Compute the mean, the sample variance and the standard deviation by hand, in a table with the deviations and their squares. Check that the deviations sum to zero before you square.
(b) Orders for the cargo model, per day, from last year's data:

| orders a day $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| $P(x)$ | .10 | .20 | .40 | .20 | .10 |

Check that the shares add to 1, then compute $E(x)$, $\sigma^{2}$ and $\sigma$ in a table with the columns $x$, $P(x)$, $x\,P(x)$, $x - \mu$, $(x - \mu)^{2}\,P(x)$. Write one sentence for the founder, with a "give or take".

## B. Binomial and Poisson

**D2 (8 minutes).**

(a) Saturday brings 10 test rides; from the CRM, three riders in ten buy, each deciding alone. Name the model and say why. Find the probability that exactly 2 buy, that nobody buys, that at least one buys, and the mean and standard deviation of the number of buyers.
(b) Orders on the web shop arrive at random, 4 an hour on average. Name the model and say why. Find the probability of no order in an hour. Then, for a 15-minute coffee break: write $\mu$ first, then the probability of no order and of at least one.

## C. The normal, forwards and backwards

**D3 (8 minutes).** The weight of an Arno bike off the line is bell-shaped: mean 22 kg, standard deviation 1.5 kg, $X \sim N(22,\,1.5)$. For each part: sketch and shade, standardise, table, one sentence.

(a) A customer wants a bike under 20 kg. What share of bikes qualify?
(b) The heaviest 5% of bikes are sent back for a check. From what weight is a bike sent back? End in kg, not in $z$.
(c) Delivery times to customers have a mean of 3.1 days and a median of 2.4 days. In one sentence: what shape is that, and why is the table the wrong tool for it?

## D. Expected value to decide

**D4 (8 minutes).** The founder has €2,000 for one promotion in December and two options. Each extra bike sold earns the usual margin of €600 (list €1,000, variable cost €400).

- **Test-ride Saturday**, cost €2,000: extra sales of 6 bikes with probability .3, 10 bikes with probability .5, 14 bikes with probability .2.
- **Online ads**, cost €1,000: extra sales of 4 bikes with probability .5, 6 bikes with probability .5.

(a) Draw the decision tree: a square for the choice, a circle for each chance node, the probabilities on the branches, the **profit** (margin minus cost) at each end node.
(b) Find the expected profit of each option.
(c) Find the standard deviation of the profit of the online ads. The test-ride Saturday's is €1,680 (given: three branches with large numbers). Which option is the riskier, and by how much?
(d) In two sentences for the Board: which option, and what the other number says.

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) The table first; the deviations must sum to zero before you square.

| week | returns $x$ | $x - \bar{x}$ | $(x - \bar{x})^{2}$ |
|---|---:|---:|---:|
| 1 | 3 | −3 | 9 |
| 2 | 8 | 2 | 4 |
| 3 | 5 | −1 | 1 |
| 4 | 6 | 0 | 0 |
| 5 | 8 | 2 | 4 |
| **sum** | **30** | 0 | **18** |

$$\bar{x} = \frac{\sum x}{n} = \frac{30}{5} = \mathbf{6}$$

$$s^{2} = \frac{\sum (x - \bar{x})^{2}}{n - 1} = \frac{18}{4} = \mathbf{4.5} \qquad s = \sqrt{4.5} = \mathbf{2.12}$$

About 6 returns a week, give or take 2.

(b) The shares: $.10 + .20 + .40 + .20 + .10 = 1.00$.

| $x$ | $P(x)$ | $x\,P(x)$ | $x - \mu$ | $(x - \mu)^{2}\,P(x)$ |
|---:|---:|---:|---:|---:|
| 0 | .10 | 0 | −2 | 4 × .10 = .40 |
| 1 | .20 | .20 | −1 | 1 × .20 = .20 |
| 2 | .40 | .80 | 0 | 0 |
| 3 | .20 | .60 | 1 | 1 × .20 = .20 |
| 4 | .10 | .40 | 2 | 4 × .10 = .40 |
| **sum** | **1.00** | **2.00** | | **1.20** |

$$E(x) = \sum x\,P(x) = \mathbf{2.0 \text{ orders a day}}$$

$$\sigma^{2} = \sum (x - \mu)^{2}\,P(x) = \mathbf{1.20} \qquad \sigma = \sqrt{1.20} = \mathbf{1.10}$$

Expect two cargo orders a day, give or take one; a day with none happens one day in ten, a day with four as well.

**D2.**

(a) **Binomial**: a fixed number of trials ($n = 10$), each yes or no, the same $p = .3$ every time, each rider alone.

$$P(2) = \binom{10}{2}\, .3^{2}\, .7^{8} = 45 \times .09 \times .05765 = \mathbf{.233}$$

$$P(0) = .7^{10} = \mathbf{.028} \qquad P(\ge 1) = 1 - P(0) = 1 - .028 = \mathbf{.972}$$

$$np = 10 \times .3 = \mathbf{3} \text{ buyers} \qquad \sigma = \sqrt{np(1-p)} = \sqrt{10 \times .3 \times .7} = \sqrt{2.1} = \mathbf{1.45}$$

Expect three buyers, give or take one and a half; a Saturday with no sale happens about three times in a hundred.

(b) **Poisson**: orders arrive at random over time, at a constant rate, with no ceiling on the count. One hour, $\mu = 4$:

$$P(0) = \frac{4^{0} e^{-4}}{0!} = e^{-4} = \mathbf{.018}$$

Fifteen minutes is a quarter of an hour, so $\mu$ first:

$$\mu = 4 \times \tfrac{1}{4} = 1 \qquad P(0) = e^{-1} = \mathbf{.368} \qquad P(\ge 1) = 1 - .368 = \mathbf{.632}$$

A silent hour is rare, two in a hundred; a silent coffee break happens more than once in three.

**D3.**

(a) Shade the left tail below 20 kg.

$$z = \frac{x - \mu}{\sigma} = \frac{20 - 22}{1.5} = \frac{-2}{1.5} = -1.33 \qquad \text{table, area to the left: } P(z < -1.33) = .0918$$

$$P(X < 20) = \mathbf{.092}$$

About nine bikes in a hundred come in under 20 kg; the customer will wait, or pay for the light frame.

(b) Backwards: the area is given, $x$ is wanted. The heaviest 5% is the **right** tail (the slide showed the left one: same steps, the sign flips), so 95% of the area is to the left of the threshold. Find .9500 *inside* the table: between $z = 1.64$ (.9495) and $z = 1.65$ (.9505), so $z = 1.645$ (Excel: `=NORM.S.INV(0.95)`). Undo the standardisation:

$$x = \mu + z\,\sigma = 22 + 1.645 \times 1.5 = 22 + 2.47 = \mathbf{24.5 \text{ kg}}$$

A bike over about 24.5 kg goes back for a check.

(c) Mean well above median: a long right tail, **positive skewness** — most parcels in two or three days, a few much later. The normal is symmetric (mean = median), so a $z$ from a mean of 3.1 would give the wrong areas: the table only answers questions about bells.

**D4.**

(a) End-node profits, margin €600 a bike minus the cost of the option.

Test-ride Saturday (cost €2,000): $6 \times 600 - 2{,}000 = 1{,}600$; $10 \times 600 - 2{,}000 = 4{,}000$; $14 \times 600 - 2{,}000 = 6{,}400$.
Online ads (cost €1,000): $4 \times 600 - 1{,}000 = 1{,}400$; $6 \times 600 - 1{,}000 = 2{,}600$.

The tree: a square "which promotion?", two branches; on each a circle with its branches labelled .3 / .5 / .2 and .5 / .5, the profits at the ends.

(b) Expected profit, $E(x) = \sum x\,P(x)$:

$$E(\text{Saturday}) = .3 \times 1{,}600 + .5 \times 4{,}000 + .2 \times 6{,}400 = 480 + 2{,}000 + 1{,}280 = \mathbf{€3{,}760}$$

$$E(\text{ads}) = .5 \times 1{,}400 + .5 \times 2{,}600 = 700 + 1{,}300 = \mathbf{€2{,}000}$$

(c) Spread of the ads, $\sigma^{2} = \sum (x - \mu)^{2} P(x)$: deviations $\pm 600$, each with share .5.

$$\sigma^{2} = .5 \times 600^{2} + .5 \times 600^{2} = 360{,}000 \qquad \sigma_{\text{ads}} = \sqrt{360{,}000} = \mathbf{€600}$$

The Saturday's €1,680 is 2.8 times larger: the Saturday is the riskier option, by far. (For the curious, its table: deviations −2,160, 240, 2,640; weighted squares 1,399,680 + 28,800 + 1,393,920 = 2,822,400; and $\sqrt{2{,}822{,}400} = 1{,}680$.)

(d) The test-ride Saturday earns €3,760 on average against €2,000 for the ads, €1,760 more; its worst case, €1,600, still beats the ads' average. Its spread is nearly three times larger (€1,680 against €600): the Saturday can end anywhere between €1,600 and €6,400, the ads between €1,400 and €2,600. Expected value picks the Saturday; the spread says the result will be a surprise either way — and since even the bad Saturday beats the ads, the Board can take the Saturday without fear.

</details>
