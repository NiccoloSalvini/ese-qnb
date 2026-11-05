# Week 7 — Drills

*One drill per block, on paper, in class. Show all work: formula, substitution, number, one sentence for the founder. The case is Arno Bikes throughout; the numbers are new. Solutions at the end.*

## A. Binomial and Poisson

**D1 (8 minutes).**

(a) Saturday brings 10 test rides; from the CRM, three riders in ten buy, each deciding alone. Name the model and say why. Find the probability that exactly 2 buy, that nobody buys, that at least one buys, and the mean and standard deviation of the number of buyers.
(b) Orders on the web shop arrive at random, 4 an hour on average. Name the model and say why. Find the probability of no order in an hour and of exactly 2 orders in an hour. Then, for a 15-minute coffee break: write $\mu$ first, then the probability of no order and of at least one.

## B. The normal, forwards and backwards

**D2 (8 minutes).** The weight of an Arno bike off the line is bell-shaped: mean 22 kg, standard deviation 1.5 kg, $X \sim N(22,\,1.5)$. For each part: sketch and shade, standardise, table, one sentence.

(a) A customer wants a bike under 20 kg. What share of bikes qualify?
(b) What share of bikes weigh between 21 and 24 kg?
(c) The heaviest 5% of bikes are sent back for a check. From what weight is a bike sent back? End in kg, not in $z$.
(d) Delivery times to customers have a mean of 3.1 days and a median of 2.4 days. In one sentence: what shape is that, and why is the table the wrong tool for it?

## C. Expected value to decide

**D3 (8 minutes).** The founder has €2,000 for one promotion in December and two options. Each extra bike sold earns the usual margin of €600 (list €1,000, variable cost €400).

- **Test-ride Saturday**, cost €2,000: extra sales of 6 bikes with probability .3, 10 bikes with probability .5, 14 bikes with probability .2.
- **Online ads**, cost €1,000: extra sales of 4 bikes with probability .5, 6 bikes with probability .5.

(a) Draw the decision tree: a square for the choice, a circle for each chance node, the probabilities on the branches, the **profit** (margin minus cost) at each end node.
(b) Find the expected profit of each option.
(c) Find the standard deviation of the profit of each option.
(d) In two sentences for the Board: which option, and what the other number says.

## D. The normal approximation

**D4 (6 minutes).** Arno Bikes ships 300 orders this month; each ships late with probability .05, independently. The logistics partner charges a penalty when 20 or more orders are late.

(a) Name the exact model, and say in one line why you will not compute it by hand.
(b) Find the mean and the standard deviation of the number of late orders.
(c) Check that the bell may be used, then find the probability of a penalty month with the four steps and the half unit.
(d) One sentence for the founder.

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) **Binomial**: a fixed number of trials ($n = 10$), each yes or no, the same $p = .3$ every time, each rider alone.

$$P(2) = \binom{10}{2}\, .3^{2}\, .7^{8} = 45 \times .09 \times .05765 = \mathbf{.233}$$

$$P(0) = .7^{10} = \mathbf{.028} \qquad P(\ge 1) = 1 - P(0) = 1 - .028 = \mathbf{.972}$$

$$np = 10 \times .3 = \mathbf{3} \text{ buyers} \qquad \sigma = \sqrt{np(1-p)} = \sqrt{10 \times .3 \times .7} = \sqrt{2.1} = \mathbf{1.45}$$

Expect three buyers, give or take one and a half; a Saturday with no sale happens about three times in a hundred.

(b) **Poisson**: orders arrive at random over time, at a constant rate, with no ceiling on the count. One hour, $\mu = 4$:

$$P(0) = \frac{4^{0} e^{-4}}{0!} = e^{-4} = \mathbf{.018} \qquad P(2) = \frac{4^{2} e^{-4}}{2!} = \frac{16 \times .01832}{2} = \mathbf{.147}$$

Fifteen minutes is a quarter of an hour, so $\mu$ first:

$$\mu = 4 \times \tfrac{1}{4} = 1 \qquad P(0) = e^{-1} = \mathbf{.368} \qquad P(\ge 1) = 1 - .368 = \mathbf{.632}$$

A silent hour is rare, two in a hundred; a silent coffee break happens more than once in three.

**D2.**

(a) Shade the left tail below 20 kg.

$$z = \frac{x - \mu}{\sigma} = \frac{20 - 22}{1.5} = \frac{-2}{1.5} = -1.33 \qquad \text{table, area to the left: } P(z < -1.33) = .0918$$

$$P(X < 20) = \mathbf{.092}$$

About nine bikes in a hundred come in under 20 kg; the customer will wait, or pay for the light frame.

(b) Shade between 21 and 24.

$$z = \frac{21 - 22}{1.5} = -0.67 \qquad z = \frac{24 - 22}{1.5} = 1.33$$

Two lookups, area to the left of each, and a difference:

$$P(-0.67 < z < 1.33) = P(z < 1.33) - P(z < -0.67) = .9082 - .2514 = \mathbf{.657}$$

Two bikes in three weigh between 21 and 24 kg.

(c) Backwards: the area is given, $x$ is wanted. The heaviest 5% is the right tail, so 95% of the area is to the left of the threshold. Find .9500 *inside* the table: between $z = 1.64$ (.9495) and $z = 1.65$ (.9505), so $z = 1.645$ (Excel: `=NORM.S.INV(0.95)`). Undo the standardisation:

$$x = \mu + z\,\sigma = 22 + 1.645 \times 1.5 = 22 + 2.47 = \mathbf{24.5 \text{ kg}}$$

A bike over about 24.5 kg goes back for a check.

(d) Mean well above median: a long right tail, **positive skewness** — most parcels in two or three days, a few much later. The normal is symmetric (mean = median), so a $z$ from a mean of 3.1 would give the wrong areas: the table only answers questions about bells.

**D3.**

(a) End-node profits, margin €600 a bike minus the cost of the option.

Test-ride Saturday (cost €2,000): $6 \times 600 - 2{,}000 = 1{,}600$; $10 \times 600 - 2{,}000 = 4{,}000$; $14 \times 600 - 2{,}000 = 6{,}400$.
Online ads (cost €1,000): $4 \times 600 - 1{,}000 = 1{,}400$; $6 \times 600 - 1{,}000 = 2{,}600$.

The tree: a square "which promotion?", two branches; on each a circle with its branches labelled .3 / .5 / .2 and .5 / .5, the profits at the ends.

(b) Expected profit, $E(x) = \sum x\,P(x)$:

$$E(\text{Saturday}) = .3 \times 1{,}600 + .5 \times 4{,}000 + .2 \times 6{,}400 = 480 + 2{,}000 + 1{,}280 = \mathbf{€3{,}760}$$

$$E(\text{ads}) = .5 \times 1{,}400 + .5 \times 2{,}600 = 700 + 1{,}300 = \mathbf{€2{,}000}$$

(c) Spread, $\sigma^{2} = \sum (x - \mu)^{2} P(x)$:

| Saturday | $x$ | $P(x)$ | $x - \mu$ | $(x-\mu)^{2} P(x)$ |
|---|---:|---:|---:|---:|
| | 1,600 | .3 | −2,160 | 1,399,680 |
| | 4,000 | .5 | 240 | 28,800 |
| | 6,400 | .2 | 2,640 | 1,393,920 |
| | | | **sum** | **2,822,400** |

$$\sigma_{\text{Saturday}} = \sqrt{2{,}822{,}400} = \mathbf{€1{,}680}$$

Ads: deviations $\pm 600$, each with share .5: $\sigma^{2} = .5 \times 600^{2} + .5 \times 600^{2} = 360{,}000$, so $\sigma_{\text{ads}} = \mathbf{€600}$.

(d) The test-ride Saturday earns €3,760 on average against €2,000 for the ads, €1,760 more; its worst case, €1,600, still beats the ads' average. Its spread is nearly three times larger (€1,680 against €600): the Saturday can end anywhere between €1,600 and €6,400, the ads between €1,400 and €2,600. Expected value picks the Saturday; the spread says the result will be a surprise either way — and since even the bad Saturday beats the ads, the Board can take the Saturday without fear.

**D4.**

(a) **Binomial**, $n = 300$, $p = .05$: a fixed number of orders, each late or not, the same $p$, independent. "20 or more" means summing $P(20) + P(21) + \dots + P(300)$, each with $\binom{300}{x}$ and $.95^{300 - x}$: not by hand.

(b)

$$\mu = np = 300 \times .05 = \mathbf{15} \qquad \sigma = \sqrt{np(1-p)} = \sqrt{300 \times .05 \times .95} = \sqrt{14.25} = \mathbf{3.775}$$

(c) $np = 15 \ge 5$ and $n(1-p) = 285 \ge 5$: the bell may be used. Sketch the bell at 15; the bar for 20 starts at 19.5, shade from there to the right.

$$z = \frac{19.5 - 15}{3.775} = \frac{4.5}{3.775} = 1.19 \qquad \text{table: } P(z < 1.19) = .8830$$

$$P(X \ge 20) = 1 - .8830 = \mathbf{.117}$$

(The exact binomial gives .119. Without the half unit, $z = 5/3.775 = 1.32$ and the area is .093 — a fifth too small.)

(d) Expect 15 late orders, give or take four; a penalty month comes about once in eight or nine months.

</details>
