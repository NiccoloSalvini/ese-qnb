# Reading week — The full mock: everything from weeks 1–5

**For the reading week, at home. About three hours in all; do it in two sittings if you prefer. Exam conditions: no notes, non-programmable calculator only, all work shown.**

This is not a real paper. It covers what weeks 1–5 prepare you for: the final exam's calculus question (two complete sets of it), a full study of a function in the resit's form, a midterm-style study of a firm with a tariff, the financial mathematics in multiple choice with a one-line justification, and the welfare cost of protection. Every function and number is new. Solutions are folded at the bottom of each part; mark yourself honestly, one part at a time.

| part | what | time | serves |
|---|---|---|---|
| A | the final's calculus question, twice: five items each | 2 × 30' | final exam, the calculus question |
| B | a full study of a function, with asymptotes | 30' | resit; midterm Q2–Q3 |
| C | a firm, a tariff, a Board | 45' | midterm Q2–Q4 |
| D | financial mathematics, ten multiple-choice items | 30' | resit; weeks 4–5 |
| E | a tariff on a small open economy | 15' | midterm Q5 |

Marks are for method. A correct answer with no working scores badly; a wrong answer with sound working scores well.

---

## A. The calculus question, twice

Each set is five items, 20% each, thirty minutes.

### Set 1

**A1.** Evaluate, splitting the fraction first: $\displaystyle\int \frac{6x^{2} - 4x + 3}{x}\,dx$

**A2.** Find `f(x)` given $f'(x) = 9x^{2} - 8x + 2$ and $f(-1) = 4$.

**A3.** Evaluate, factoring and commenting on the sign of each factor: $\displaystyle\lim_{x \to 2^{+}} \frac{x^{2} - 5x + 6}{x^{2} - 2x}$

**A4.** Evaluate $\displaystyle\lim_{x \to -\infty} \frac{5x^{2} - 3x}{2x^{2} + x - 1}$

**A5.** Evaluate, leaving the answer in terms of `ln`: $\displaystyle\int_{2}^{4} \left(\frac{3}{x} + \frac{2x}{x^{2} - 3}\right) dx$

### Set 2

**A6.** Evaluate $\displaystyle\int \frac{2x^{3} + 5x - 4}{x^{2}}\,dx$

**A7.** Find `f(x)` given $f'(x) = 4x^{3} - 6x^{2} + 1$ and $f(2) = 7$.

**A8.** Evaluate $\displaystyle\lim_{x \to 3^{-}} \frac{x^{2} - 9}{x^{2} - 6x + 9}$

**A9.** Evaluate $\displaystyle\lim_{x \to -\infty} \frac{3x^{3} + 2x}{x^{2} - 4}$

**A10.** Evaluate $\displaystyle\int_{0}^{1} \left(\frac{2}{x + 1} + \frac{4x}{x^{2} + 1}\right) dx$

<details>
<summary><strong>Solutions to part A</strong></summary>

**A1.** Split: $6x - 4 + \dfrac{3}{x}$. Integrate term by term: **$3x^{2} - 4x + 3\ln|x| + c$**.

**A2.** $f(x) = 3x^{3} - 4x^{2} + 2x + c$. Then $f(-1) = -3 - 4 - 2 + c = -9 + c = 4$, so $c = 13$: **$f(x) = 3x^{3} - 4x^{2} + 2x + 13$**. *Every sign of $(-1)^{n}$ written out: odd powers stay negative.*

**A3.** Substituting gives $0/0$: factor. $\dfrac{(x-2)(x-3)}{x(x-2)} = \dfrac{x-3}{x}$ for $x \neq 2$. As $x \to 2^{+}$, $x - 3 \to -1$ and $x \to 2$: the limit is **$-\tfrac{1}{2}$**. The one-sided approach does not change the answer here, because the factor that vanished has cancelled.

**A4.** Divide by $x^{2}$: $\dfrac{5 - 3/x}{2 + 1/x - 1/x^{2}} \to$ **$\tfrac{5}{2}$**. Same degree top and bottom: the ratio of the leading coefficients.

**A5.** $\int \frac{3}{x}dx = 3\ln|x|$; the second term has the derivative of its denominator on top: $\int \frac{2x}{x^{2}-3}dx = \ln|x^{2} - 3|$.
$\big[3\ln x + \ln(x^{2} - 3)\big]_{2}^{4} = (3\ln 4 + \ln 13) - (3\ln 2 + \ln 1) = 3\ln 2 + \ln 13 =$ **$\ln 104 \approx 4.644$**.

**A6.** Split: $2x + \dfrac{5}{x} - \dfrac{4}{x^{2}} = 2x + 5x^{-1} - 4x^{-2}$. Integrate: **$x^{2} + 5\ln|x| + \dfrac{4}{x} + c$** (since $\int -4x^{-2}dx = 4x^{-1}$).

**A7.** $f(x) = x^{4} - 2x^{3} + x + c$; $f(2) = 16 - 16 + 2 + c = 7$, so $c = 5$: **$f(x) = x^{4} - 2x^{3} + x + 5$**.

**A8.** $\dfrac{(x-3)(x+3)}{(x-3)^{2}} = \dfrac{x+3}{x-3}$. As $x \to 3^{-}$: the top $\to 6 > 0$, the bottom $\to 0$ through **negative** values. Positive over a vanishing negative: **$-\infty$**. *A vertical asymptote at $x = 3$; from the right the limit is $+\infty$.*

**A9.** The top has the higher degree. Divide by $x^{2}$: $\dfrac{3x + 2/x}{1 - 4/x^{2}} \approx 3x \to$ **$-\infty$** as $x \to -\infty$.

**A10.** $\big[2\ln(x+1) + 2\ln(x^{2}+1)\big]_{0}^{1} = 2\ln 2 + 2\ln 2 - 0 =$ **$4\ln 2 = \ln 16 \approx 2.773$**. *Check the second term: the derivative of $x^{2} + 1$ is $2x$, and the top is $4x = 2 \cdot 2x$, so the integral is $2\ln(x^{2}+1)$.*

</details>

---

## B. A full study of a function

Study $\displaystyle f(x) = \frac{x^{2} + 3}{x - 1}$ completely:

(a) domain; (b) limits at the edges of the domain, and the asymptotes — vertical, horizontal or slant; (c) intersections with the axes and the sign; (d) stationary points and their nature, by the second derivative; (e) convexity and inflection; (f) range; (g) a sketch with everything above marked.

<details>
<summary><strong>Solution to part B</strong></summary>

**(a) Domain.** The denominator vanishes at $x = 1$: **$(-\infty, 1) \cup (1, +\infty)$**.

**(b) Limits and asymptotes.**
At the break: the top $\to 4$; the bottom $\to 0^{-}$ from the left, $0^{+}$ from the right. So $\lim_{x\to1^{-}} f = -\infty$, $\lim_{x\to1^{+}} f = +\infty$: **vertical asymptote $x = 1$**.
At infinity: $f \to \pm\infty$, so no horizontal asymptote. Slant: $m = \lim \frac{f(x)}{x} = \lim \frac{x^{2}+3}{x^{2}-x} = 1$; $b = \lim (f(x) - x) = \lim \frac{x^{2} + 3 - x^{2} + x}{x - 1} = \lim \frac{x+3}{x-1} = 1$. **Slant asymptote $y = x + 1$**, at both ends.

**(c) Axes and sign.** $f(0) = -3$: the curve crosses the y-axis at $(0, -3)$. $x^{2} + 3 > 0$ always, so **no zeros**. The sign is the sign of $x - 1$: **negative for $x < 1$, positive for $x > 1$**.

**(d) Stationary points.** $f'(x) = \dfrac{2x(x-1) - (x^{2}+3)}{(x-1)^{2}} = \dfrac{x^{2} - 2x - 3}{(x-1)^{2}} = \dfrac{(x-3)(x+1)}{(x-1)^{2}}$, zero at $x = -1$ and $x = 3$.
$f''(x) = \dfrac{8}{(x-1)^{3}}$. $f''(-1) = -1 < 0$: **local maximum $(-1, -2)$**. $f''(3) = 1 > 0$: **local minimum $(3, 6)$**.

**(e) Convexity.** $f'' < 0$ for $x < 1$: **concave**; $f'' > 0$ for $x > 1$: **convex**. The sign changes only at $x = 1$, which is outside the domain: **no inflection point**.

**(f) Range.** On the left branch the function climbs from $-\infty$ to the maximum $-2$ and falls back to $-\infty$; on the right branch it falls from $+\infty$ to the minimum $6$ and rises again. **Range $(-\infty, -2] \cup [6, +\infty)$**: no value between $-2$ and $6$ is ever taken.

**(g) Sketch.** Two branches, both hugging $y = x + 1$ far out and the line $x = 1$ near the break; the left one a dome through $(0, -3)$ with its top at $(-1, -2)$, the right one a bowl with its bottom at $(3, 6)$. Mark both asymptotes as dashed lines.

</details>

---

## C. A firm, a tariff, a Board

A firm assembles a component for e-bikes. In € thousand a month, with `q` in hundreds of units:

$$R(q) = 48\ln(q + 1) \qquad C(q) = 0.3q^{2} + 6q + 20$$

1. Study `C` and `R`: domain (algebraically and economically), limits, intersections with the axes, sign, maxima and minima, convexity and inflection, range. Sketch both on one diagram.
2. Derive `π(q)` and study it the same way. Find the best output and the profit there. The break-even outputs cannot be found with algebra: find them by bisection to one decimal place. Sketch.
3. Of the €6k that one more unit costs, €5k is a part imported from outside the EU. The EU sets a **30% tariff** on it. Rewrite the cost function, say which terms move and which do not, and find the new best output, the new profit and the new break-evens.
4. Three sentences for the Board.

<details>
<summary><strong>Solution to part C</strong></summary>

**1. Cost.** Domain: algebraically $(-\infty, +\infty)$, economically **$[0, +\infty)$**. $C(0) = 20$, the **fixed cost**. $\Delta = 36 - 24 = 12 > 0$: the parabola does have two zeros, at $q = (-6 \pm \sqrt{12})/0.6 \approx -4.23$ and $-15.77$, **both outside the economic domain** — on $[0, +\infty)$ cost is always positive. The vertex at $q = -10$ is outside too. $C'(q) = 0.6q + 6 > 0$ on the domain: increasing, no max or min; $C'' = 0.6 > 0$: **convex**, no inflection. $\lim_{q\to\infty} C = +\infty$, and $C/q \to \infty$: **no slant asymptote**. Range **$[20, +\infty)$**.

**Revenue.** Domain: algebraically $q > -1$, $(-1, +\infty)$; economically **$[0, +\infty)$**. $R(0) = 0$: through the origin, its only zero. Positive for $q > 0$. $R'(q) = \dfrac{48}{q+1} > 0$: increasing, no max or min. $R''(q) = -\dfrac{48}{(q+1)^{2}} < 0$: **concave** — diminishing returns. $R \to +\infty$ but $R/q \to 0$: no horizontal, no slant asymptote. Range **$[0, +\infty)$**.

**2. Profit.** $\pi(q) = 48\ln(q+1) - 0.3q^{2} - 6q - 20$ on $[0, +\infty)$. $\pi(0) = -20$: at zero output the firm loses its fixed cost. $\lim_{q\to\infty}\pi = -\infty$ (the square beats the log).
$\pi'(q) = \dfrac{48}{q+1} - 0.6q - 6 = 0$. Multiply by $10(q+1)$: $480 = (6q + 60)(q + 1)$, i.e. $q^{2} + 11q - 70 = 0$. $\Delta = 121 + 280 = 401$, $\sqrt{401} \approx 20.025$, **$q^{*} = (-11 + 20.025)/2 \approx 4.51$** (450 units). $\pi''(q) = -\dfrac{48}{(q+1)^{2}} - 0.6 < 0$ everywhere: a **maximum**, and **concave throughout, no inflection**. $\pi(4.51) \approx$ **28.75**. Range $(-\infty, 28.75]$.
Break-evens by bisection. Lower: $\pi(0.6) \approx -1.15$, $\pi(0.7) \approx +1.12$; $\pi(0.65) \approx +0.01$ → between 0.6 and 0.65; $\pi(0.625) \approx -0.56$ → between 0.625 and 0.65: **$q \approx 0.6$** to one decimal (exact 0.650, so 0.65 is right on the edge — write "about 0.65"). Upper: $\pi(10) \approx 5.10$, $\pi(11) \approx -3.02$; $\pi(10.5) \approx 1.16$; $\pi(10.75) \approx -0.90$; $\pi(10.625) \approx 0.13$ → between 10.625 and 10.75: **$q \approx 10.6$** (exact 10.64). Profitable between about 65 and 1,064 units.
*Sketch:* starts at $(0, -20)$, crosses at 0.65, peaks at $(4.51, 28.75)$, crosses again at 10.64, falls away.

**3. The tariff.** $0.30 \times 5 = 1.5$ more per unit. Only the **linear term** moves: $C_{t}(q) = 0.3q^{2} + 7.5q + 20$. The quadratic term is the plant's internal cost of running harder, the fixed cost does not depend on output, and revenue stays put on the assumption that the firm cannot raise its price.
$\pi_{t}'(q) = \dfrac{48}{q+1} - 0.6q - 7.5 = 0$ → $480 = (6q + 75)(q + 1)$ → $2q^{2} + 27q - 135 = 0$. $\Delta = 729 + 1080 = 1809$, $\sqrt{1809} \approx 42.53$, **$q_{t}^{*} = (-27 + 42.53)/4 \approx 3.88$**; $\pi_{t}'' < 0$, a maximum. $\pi_{t}(3.88) \approx$ **22.47**: **−6.28, or −22%**. Quick check: $1.5 \times 4.51 \approx 6.8$; the exact loss is smaller because output falls.
Break-evens: $\pi_{t}(0.6) \approx -2.05$, $\pi_{t}(0.7) \approx +0.07$; $\pi_{t}(0.65) \approx -0.96$ → between 0.65 and 0.7, **$q \approx 0.7$** (exact 0.696). Upper: $\pi_{t}(8.5) \approx 2.64$, $\pi_{t}(8.75) \approx 0.72$, $\pi_{t}(8.875) \approx -0.27$, $\pi_{t}(8.8125) \approx 0.22$, $\pi_{t}(8.84) \approx -0.02$ → **$q \approx 8.8$** (exact 8.84). The window shrinks from $[0.65, 10.64]$ to $[0.70, 8.84]$, mostly at the top.

**4. For the Board.** "The best output is about 450 units a month, for a profit of about €28,750. A 30% tariff on the imported part would cut that to about 390 units and €22,470 — a fifth of our profit — and we would stop covering costs above 880 units instead of 1,060. Every extra unit we import now carries the tariff, so the case for a second supplier inside the EU is worth costing."

</details>

---

## D. Financial mathematics — select and justify

For each item, choose one option and justify it in one line, with the computation.

**D1.** €5,000 is invested for 3 years at 4% a year. Simple interest gives (i) €5,600 and compound €5,624.32; (ii) both €5,600; (iii) simple €5,624.32 and compound €5,600; (iv) both €5,624.32.

**D2.** A loan charges 6% a year compounded monthly. Its effective annual rate is (i) 6.00%; (ii) 6.17%; (iii) 6.50%; (iv) 72%.

**D3.** The present value of €10,000 due in 5 years at 7% is closest to (i) €6,500; (ii) €7,130; (iii) €9,300; (iv) €14,026.

**D4.** €2,000 at the end of each year for 8 years, at 5%, is worth today closest to (i) €16,000; (ii) €12,926; (iii) €10,830; (iv) €19,099.

**D5.** A perpetuity of €600 a year at 4% is worth (i) €24,000; (ii) €2,400; (iii) €15,000; (iv) nothing: it never ends.

**D6.** A 10-year bond with face €1,000 pays a 5% annual coupon. The market yield is 6%. It trades (i) at par; (ii) at a premium; (iii) at a discount; (iv) cannot be said without the price.

**D7.** A zero-coupon bond pays €1,000 in 4 years; the yield is 5%. Its price is closest to (i) €800; (ii) €823; (iii) €952; (iv) €1,000.

**D8.** A bond has modified duration 6.2. The yield rises by 50 basis points. The price changes by about (i) −0.31%; (ii) −3.1%; (iii) −6.2%; (iv) +3.1%.

**D9.** A project costs €1,000 today and returns €400 at the end of each of the next 3 years. At 8% its NPV is about (i) €200, accept; (ii) €31, accept; (iii) −€31, reject; (iv) €0, indifferent.

**D10.** Positive convexity means that, compared with the duration estimate, the true price is (i) higher whether yields rise or fall; (ii) lower whether yields rise or fall; (iii) higher only when yields fall; (iv) the same.

<details>
<summary><strong>Solutions to part D</strong></summary>

| | answer | one line |
|---|---|---|
| D1 | **(i)** | simple $5000(1 + 0.04 \times 3) = 5{,}600$; compound $5000 \times 1.04^{3} = 5{,}624.32$ — interest on interest |
| D2 | **(ii)** | $(1 + 0.06/12)^{12} - 1 = 1.005^{12} - 1 = 6.168\%$ |
| D3 | **(ii)** | $10{,}000 / 1.07^{5} = 7{,}129.86$ |
| D4 | **(ii)** | $2000 \times \dfrac{1 - 1.05^{-8}}{0.05} = 2000 \times 6.4632 = 12{,}926.43$ |
| D5 | **(iii)** | $C/r = 600 / 0.04 = 15{,}000$: an infinite stream, a finite price, because far payments are worth almost nothing today |
| D6 | **(iii)** | coupon rate below the yield → price below par (it is €926.40) |
| D7 | **(ii)** | $1000 / 1.05^{4} = 822.70$ |
| D8 | **(ii)** | $\Delta P/P \approx -D_{mod}\,\Delta y = -6.2 \times 0.005 = -3.1\%$ |
| D9 | **(ii)** | $-1000 + 400\left(\tfrac{1}{1.08} + \tfrac{1}{1.08^{2}} + \tfrac{1}{1.08^{3}}\right) = -1000 + 400 \times 2.5771 = 30.84 > 0$ |
| D10 | **(i)** | the price–yield curve lies above its tangent on both sides: the duration line understates every price |

</details>

---

## E. A tariff on a small open economy

Demand `Q_d = 90 − p`, domestic supply `Q_s = 2p − 30` (`Q` in thousand units, `p` in €). The world price is €25, and the country is too small to move it.

(a) Price and quantity in autarky.
(b) Free trade: bought, made at home, imported.
(c) A tariff of €5 a unit: the same three quantities.
(d) The consumers' loss as an integral; the producers' gain as an integral; the tariff revenue; the protective and consumption effects. Show that they add up.
(e) Two sentences: who gains, who loses, and what is lost by everyone.

<details>
<summary><strong>Solution to part E</strong></summary>

(a) $90 - p = 2p - 30$ → **$p = 40$, $Q = 50$**.
(b) At $p = 25$: bought **65**, made at home **20**, imported **45**.
(c) At $p = 30$: bought **60**, made at home **30**, imported **30**.
(d) $\Delta CS = \int_{25}^{30} (90 - p)\,dp = \big[90p - \tfrac{p^{2}}{2}\big]_{25}^{30} = 2250 - 1937.5 =$ **312.5**.
$\Delta PS = \int_{25}^{30} (2p - 30)\,dp = \big[p^{2} - 30p\big]_{25}^{30} = 0 - (-125) =$ **125**.
Revenue $= 5 \times 30 =$ **150**. Protective effect $= \tfrac12 \times 5 \times (30 - 20) =$ **25**; consumption effect $= \tfrac12 \times 5 \times (65 - 60) =$ **12.5**.
Check: $125 + 150 + 25 + 12.5 = 312.5$ ✔ (€ thousand).
(e) Domestic producers gain €125k and the treasury €150k, both paid by consumers, who lose €312.5k. The remaining €37.5k — production at home that costs more than imports, and purchases that no longer happen — is lost to everyone: the deadweight cost of protection.

</details>

---

## After you have marked it

- **Part A below 70%?** Redo the week-2 and week-3 drills of the item type you missed, then the week-5 mock. These five item types are the whole of the final's calculus question.
- **Part B or C incomplete?** Check against the seven steps: domain, limits, range, sign, max and min, convexity, sketch. A missing step is a missing mark, however good the rest is.
- **Part D below 7/10?** The week-4 revision set covers every item type here.
- **Part C and E** are your midterm with different numbers. If they went well, your midterm is mostly written; if not, bring them to the office hour.
