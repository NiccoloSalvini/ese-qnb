# Week 8 — Drills

*One drill per block, on paper, during the session. Show all work: formula, substitution, number, one sentence for the founder. The case is Arno Bikes throughout; the numbers are new. Read $z$ to two decimals, as the table does. Solutions at the end.*

## A. A count read as a bell, the standard error

**D1 (8 minutes).**

(a) Next month Arno Bikes ships 300 orders; each is late with probability .05, independently. The courier charges a penalty in a month with 20 or more late orders. Check that the normal can be used, then find the probability of a penalty month. Use the half unit.
(b) One full charge takes 240 minutes on average, standard deviation 20 minutes. Find the standard error of the average of 25 charges, and of 100 charges.
(c) Find the probability that the average of 25 charges is above 248 minutes.

## B. The confidence interval

**D2 (8 minutes).** 36 customers, chosen at random, spent on average **€84** on accessories in the shop. From two years of receipts, σ = **€18**.

(a) Find the standard error.
(b) Construct the 90% and the 95% confidence interval for the average spend of all customers.
(c) Select the correct 95% interval and say in one line what went wrong in each of the others: (i) €78.12 to €89.88; (ii) €79.07 to €88.94; (iii) €48.72 to €119.28; (iv) €83.02 to €84.98.
(d) How many customers do we need to survey to know the average spend within **€2**, at 95%?

## C. The hypothesis test

**D3 (8 minutes).** Until now, one test rider in four bought a bike. With a new sales script, **90 of 300** test riders bought.

(a) State $H_0$ and $H_1$ for a two-tailed test.
(b) Test at the 5% level, in six steps: the standard error under $H_0$, $z$, the p-value, the decision.
(c) Write the p-value in one sentence of words, and one sentence for the Board.

## D. The least-squares line

**D4 (8 minutes).** Five months: ad spend $x$ (€ thousand) and bikes sold $y$.

| $x$ | 1 | 2 | 3 | 4 | 5 |
|---|---:|---:|---:|---:|---:|
| $y$ | 30 | 34 | 41 | 42 | 48 |

(a) Compute $\bar{x}$ and $\bar{y}$, then the slope $b$ and the intercept $a$ in a table with the columns $x - \bar{x}$, $y - \bar{y}$, their product, $(x - \bar{x})^{2}$.
(b) Interpret the slope in one sentence, in bikes and euros.
(c) Given that the squared distances from $\bar{y}$ add to 200 and those left by the line add to 6.4, compute $R^{2}$ and $r$.
(d) Predict sales for €3,500 of ads. Would you use the line for €12,000? Why not?

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) $np = 300 \times .05 = 15$ and $n(1-p) = 285$, both at least 5: the bell can be used.

$$\mu = np = \mathbf{15} \qquad \sigma = \sqrt{np(1-p)} = \sqrt{300 \times .05 \times .95} = \sqrt{14.25} = \mathbf{3.775}$$

"20 or more" starts at 19.5:

$$z = \frac{19.5 - 15}{3.775} = 1.192 \approx 1.19 \qquad P(X \ge 20) = 1 - .8830 = \mathbf{.117}$$

A penalty month comes about one month in nine (the exact binomial gives .119).

(b) $SE = \sigma / \sqrt{n}$:

$$SE_{25} = \frac{20}{\sqrt{25}} = \frac{20}{5} = \mathbf{4 \text{ minutes}} \qquad SE_{100} = \frac{20}{10} = \mathbf{2 \text{ minutes}}$$

Four times the charges, half the standard error.

(c) The average of 25 charges is a bell with mean 240 and standard error 4:

$$z = \frac{248 - 240}{4} = 2.00 \qquad P(\bar{x} > 248) = 1 - .9772 = \mathbf{.023}$$

One charge above 248 minutes is common ($z = 0.4$); an *average* of 25 above 248 happens about twice in a hundred.

**D2.**

(a) $SE = 18 / \sqrt{36} = 18 / 6 = \mathbf{€3}$.

(b) 90%, $z = 1.645$: $84 \pm 1.645 \times 3 = 84 \pm 4.94$, **€79.07 to €88.94**.
95%, $z = 1.96$: $84 \pm 1.96 \times 3 = 84 \pm 5.88$, **€78.12 to €89.88**.

(c) **(i)** is the 95% interval. (ii) is the 90% one ($z = 1.645$). (iii) uses $1.96 \times 18$: the σ of one customer, no $\sqrt{n}$. (iv) divides by $n = 36$ instead of $\sqrt{36}$.

(d) $n = (z\,\sigma / E)^{2} = (1.96 \times 18 / 2)^{2} = 17.64^{2} = 311.2$, so **312 customers** (always round up).

**D3.**

(a) $H_0$: $p = .25$ (the script changed nothing). $H_1$: $p \neq .25$.

(b) Level 5%, two tails: cut-offs $\pm 1.96$. The sample share is $\hat{p} = 90/300 = .30$.

$$SE = \sqrt{\frac{.25 \times .75}{300}} = \sqrt{.000625} = .025 \qquad z = \frac{.30 - .25}{.025} = \mathbf{2.00}$$

$$p\text{-value} = 2 \times P(z > 2.00) = 2 \times .0228 = \mathbf{.046}$$

$.046 < .05$: **reject $H_0$**.

(c) If the script had changed nothing, a share as far from 25% as ours, either way, would turn up less than 5 times in 100. For the Board: the new script lifted conversion from one rider in four to three in ten, and the rise is unlikely to be luck — though only just (p = .046): keep checking it for another month.

**D4.**

(a) $\bar{x} = 15/5 = 3$, $\bar{y} = 195/5 = 39$.

| $x - \bar{x}$ | $y - \bar{y}$ | product | $(x - \bar{x})^{2}$ |
|---:|---:|---:|---:|
| −2 | −9 | 18 | 4 |
| −1 | −5 | 5 | 1 |
| 0 | 2 | 0 | 0 |
| 1 | 3 | 3 | 1 |
| 2 | 9 | 18 | 4 |
| | | **44** | **10** |

$$b = \frac{44}{10} = \mathbf{4.4} \qquad a = \bar{y} - b\,\bar{x} = 39 - 4.4 \times 3 = \mathbf{25.8} \qquad \hat{y} = 25.8 + 4.4\,x$$

(b) Each extra €1,000 of ads goes with about 4.4 more bikes sold in the month.

(c) $R^{2} = 1 - 6.4/200 = \mathbf{.968}$; $r = +\sqrt{.968} = \mathbf{.984}$ (positive, like the slope). Ad spend explains about 97% of the month-to-month differences in sales.

(d) $\hat{y} = 25.8 + 4.4 \times 3.5 = 25.8 + 15.4 = \mathbf{41.2}$ bikes. Not for €12,000: we never spent more than €5,000, and nothing says the line keeps rising out there.

</details>
