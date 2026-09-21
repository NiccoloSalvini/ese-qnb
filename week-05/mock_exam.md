# Week 5 — Mock of the final exam's calculus question

**Forty minutes. Exam conditions: no notes, non-programmable calculator only, all work shown.**

This is not the real paper. It is the same five item types, with different functions and numbers, in the same proportions: five items, 20% each. Marks are for method — a correct answer with no working scores badly, and a wrong answer with sound working scores well.

---

**Q1 (20%).** Evaluate the indefinite integral, splitting the fraction term by term first:

$$\int \frac{2q^{5} - 5q^{3} + 3}{q^{2}}\,dq$$

**Q2 (20%).** Find `f(q)` given

$$f'(q) = 9q^{2} - 6q + 4 \qquad\text{and}\qquad f(1) = 8$$

**Q3 (20%).** Evaluate the one-sided limit, showing the factoring and commenting on the sign of each factor:

$$\lim_{q \to 3^{+}} \frac{(q-3)^{2}}{3q - q^{2}}$$

**Q4 (20%).** Evaluate:

$$\lim_{q \to -\infty} \frac{4q^{3} - 5q + 2}{7q^{3} + q^{2}}$$

**Q5 (20%).** Evaluate the definite integral, leaving the answer in terms of `ln`:

$$\int_{2}^{6} \left(\frac{8}{q} + 3q\right) dq$$

---

<details>
<summary><strong>Solutions — do not open before the forty minutes are up</strong></summary>

**Q1.** Divide term by term: `(2q⁵ − 5q³ + 3)/q² = 2q³ − 5q + 3q⁻²`.

$$\int = \frac{q^{4}}{2} - \frac{5q^{2}}{2} - \frac{3}{q} + c$$

*Common loss of marks: integrating before splitting, and forgetting `+ c`.*

**Q2.** `f(q) = 3q³ − 3q² + 4q + c`. Then `f(1) = 3 − 3 + 4 + c = 8`, so `c = 4`.

$$f(q) = 3q^{3} - 3q^{2} + 4q + 4$$

*Common loss of marks: leaving `c` unresolved when an initial condition is given.*

**Q3.** Factor the denominator: `3q − q² = q(3 − q) = −q(q − 3)`.

$$\frac{(q-3)^{2}}{-q(q-3)} = -\frac{q-3}{q}$$

As `q → 3⁺`: `(q − 3) → 0⁺` and `q → 3`, so the expression → `−0 = 0`.

$$\lim_{q \to 3^{+}} = 0$$

*Marks are for the factoring and the sign discussion, not the zero.*

**Q4.** Divide numerator and denominator by `q³`:

$$\frac{4 - 5/q^{2} + 2/q^{3}}{7 + 1/q} \longrightarrow \frac{4}{7}$$

*The sign of the infinity does not matter here: both cubes dominate and the ratio of leading coefficients survives.*

**Q5.**

$$\int_{2}^{6}\left(\frac{8}{q} + 3q\right)dq = \Big[8\ln q + \tfrac{3}{2}q^{2}\Big]_{2}^{6} = (8\ln 6 + 54) - (8\ln 2 + 6)$$

$$= 8(\ln 6 - \ln 2) + 48 = 8\ln 3 + 48 \approx 56.79$$

*Using `ln(6) − ln(2) = ln 3` is worth stating: the exam likes the log rules used, not just the calculator.*

</details>

## After you have marked it

Count the marks you lost, and sort them into two piles:

- **method** — you did not know what to do;
- **execution** — you knew, and slipped.

The first pile is what the remaining weeks and the resit revision are for. The second is answered by writing more steps down, not by working faster.
