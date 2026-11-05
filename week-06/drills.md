# Week 6 — Drills

*One drill per block. There is no drill time in today's session, so these are for tonight, on paper, before Monday: show all work — formula, substitution, number, one sentence for the founder. The case is Arno Bikes throughout; the numbers are new. Solutions at the end; check yourself before you look.*

## A. Sets and counting

**D1 (5 minutes).** Last Saturday 150 people visited the Arno Bikes showroom. 95 took a test ride ($T$), 70 asked about financing ($F$), 25 did neither.

(a) How many visitors did both? Draw the two circles and fill in all four regions; check that they add to 150.
(b) A visitor is picked at random. Find $P(T \cup F)$ with the addition law and $P(T \cap F)$ as a share.
(c) The founder picks 2 of her 7 sales staff for the Saturday shift. How many different pairs? If one **opens** and the other **closes**, how many assignments? In one line: why is the second number exactly twice the first?

## B. Conditional probability and Bayes

**D2 (8 minutes).** Chargers come from two suppliers. **Ohm** sends 60% of them and 4% of Ohm's chargers are faulty; **Watt** sends 40% and 1% of Watt's are faulty. Last month Arno Bikes received 500 chargers.

(a) Build the two-way table of counts (supplier × good/faulty).
(b) Find $P(\text{faulty} \mid \text{Ohm})$ and $P(\text{Ohm} \mid \text{faulty})$. Say in one sentence why they are different questions.
(c) Are supplier and fault independent? Compare the rows, then say the word.
(d) A faulty charger is on the bench. Use Bayes, written out, to find the probability it came from Ohm. Compare with Ohm's share of deliveries, and with the battery case of this morning: what is different here?

## C. Mean and variance, a random variable

**D3 (8 minutes).**

(a) Warranty returns in the last five weeks: 3, 8, 5, 6, 8. Compute the mean, the sample variance and the standard deviation by hand, in a table with the deviations and their squares. Check that the deviations sum to zero before you square.
(b) Orders for the cargo model, per day, from last year's data:

| orders a day $x$ | 0 | 1 | 2 | 3 | 4 |
|---|---:|---:|---:|---:|---:|
| $P(x)$ | .10 | .20 | .40 | .20 | .10 |

Check that the shares add to 1, then compute $E(x)$, $\sigma^{2}$ and $\sigma$ in a table with the columns $x$, $P(x)$, $x\,P(x)$, $x - \mu$, $(x - \mu)^{2}\,P(x)$. Write one sentence for the founder, with a "give or take".

---

<details>
<summary><strong>Solutions</strong></summary>

**D1.**

(a) At least one: $150 - 25 = 125$. Then $95 + 70 = 165$ counts "both" twice:

$$n(T \cup F) = n(T) + n(F) - n(T \cap F) \;\Rightarrow\; 125 = 95 + 70 - \text{both} \;\Rightarrow\; \text{both} = \mathbf{40}$$

The four regions: test ride only $95 - 40 = 55$, both $40$, financing only $70 - 40 = 30$, neither $25$. Check: $55 + 40 + 30 + 25 = 150$.

(b) Divide every count by 150:

$$P(T \cup F) = P(T) + P(F) - P(T \cap F) = \frac{95}{150} + \frac{70}{150} - \frac{40}{150} = .633 + .467 - .267 = \mathbf{.833}$$

$$P(T \cap F) = \frac{40}{150} = \mathbf{.267}$$

Five visitors in six did at least one of the two; about one in four did both.

(c) A pair is a pair, order does not matter — combinations:

$$\binom{7}{2} = \frac{7!}{2!\,(7-2)!} = \frac{7 \cdot 6 \cdot \cancel{5!}}{2 \cdot 1 \cdot \cancel{5!}} = \frac{42}{2} = \mathbf{21} \text{ pairs}$$

Opening and closing are named roles, order matters — permutations:

$$P^{7}_{2} = \frac{7!}{(7-2)!} = 7 \cdot 6 = \mathbf{42} \text{ assignments}$$

Each pair can take the two roles in $2! = 2$ ways: $21 \times 2 = 42$. The $2!$ underneath in the combinations removes exactly those orderings.

**D2.**

(a) Counts from the three facts. Ohm: $0.60 \times 500 = 300$ chargers, $0.04 \times 300 = 12$ faulty, $300 - 12 = 288$ good. Watt: $0.40 \times 500 = 200$ chargers, $0.01 \times 200 = 2$ faulty, $200 - 2 = 198$ good.

| | good | faulty | total |
|---|---:|---:|---:|
| **Ohm** | 288 | 12 | 300 |
| **Watt** | 198 | 2 | 200 |
| **total** | 486 | 14 | 500 |

(b) Same cell, 12, on top; a different total underneath.

$$P(\text{faulty} \mid \text{Ohm}) = \frac{12}{300} = \mathbf{.04} \qquad \text{(Ohm's row: of Ohm's chargers, what share is faulty)}$$

$$P(\text{Ohm} \mid \text{faulty}) = \frac{12}{14} = \mathbf{.857} \qquad \text{(the faulty column: of the faulty chargers, what share is Ohm's)}$$

The first answers "how good is Ohm"; the second answers "who sent this faulty one".

(c) Compare the rows with the total:

$$P(\text{faulty} \mid \text{Ohm}) = .04 \qquad P(\text{faulty} \mid \text{Watt}) = \frac{2}{200} = .01 \qquad P(\text{faulty}) = \frac{14}{500} = .028$$

The rows differ from each other and from the total: knowing the supplier changes the share of faulty, so supplier and fault are **dependent**. Had both rows read .028, the supplier would tell us nothing about the fault.

(d) Bayes is the faulty column in shares. First the three-column update, as on the slide:

| supplier | prior share | × defect rate | = faulty, as a share of all | ÷ total faulty |
|---|---:|---:|---:|---:|
| Ohm | .60 | .04 | .024 | .024 / .028 = **.857** |
| Watt | .40 | .01 | .004 | .004 / .028 = **.143** |
| total | 1.00 | | .028 | 1.00 |

Then the same table in symbols:

$$P(\text{Ohm} \mid \text{faulty}) = \frac{P(\text{faulty} \mid \text{Ohm})\,P(\text{Ohm})}{P(\text{faulty} \mid \text{Ohm})\,P(\text{Ohm}) + P(\text{faulty} \mid \text{Watt})\,P(\text{Watt})} = \frac{.04 \times .60}{.04 \times .60 + .01 \times .40} = \frac{.024}{.028} = \mathbf{.857}$$

Check with the counts: $12/14 = .857$. Ohm sends 60% of the chargers and is behind 86% of the faulty ones. This morning the big supplier (Volta) had the *lower* defect rate, and the evidence pulled the answer towards the small one; here the big supplier also has the higher rate, so the two effects push the same way and the answer is close to certain. Same formula, opposite story: the volume and the rate must both be read.

**D3.**

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

</details>
