# Week 5 — Mock of the final exam's calculus question

**Forty minutes. Exam conditions: no notes, non-programmable calculator only, all work shown.**

This is not the real paper. It is the same five item types, with different functions and numbers, in the same proportions: five items, 20% each. Marks are for method — a correct answer with no working scores badly, and a wrong answer with sound working scores well.

---

**Q1 (20%).** Evaluate the indefinite integral, splitting the fraction term by term first:

$$\int \frac{2q^{5} - 5q^{3} + 3}{q^{2}}\,dq$$

**Q2 (20%).** Find `f(x)` given

$$f'(x) = 9x^{2} - 6x + 4 \qquad\text{and}\qquad f(-2) = 11$$

**Q3 (20%).** Evaluate the one-sided limit, showing the factoring and commenting on the sign of each factor:

$$\lim_{q \to 3^{+}} \frac{(q-3)^{2}}{3q - q^{2}}$$

**Q4 (20%).** Evaluate:

$$\lim_{q \to -\infty} \frac{4q^{3} - 5q + 2}{7q^{3} + q^{2}}$$

**Q5 (20%).** Evaluate the definite integral, leaving the answer in terms of `ln`:

$$\int_{0}^{\frac{1}{3}} \left(\frac{1}{x-1} + \frac{x}{x^{2}-1}\right) dx$$

---

<details>
<summary><strong>Solutions — do not open before the forty minutes are up</strong></summary>

**Q1.** Divide term by term: `(2q⁵ − 5q³ + 3)/q² = 2q³ − 5q + 3q⁻²`.

$$\int = \frac{q^{4}}{2} - \frac{5q^{2}}{2} - \frac{3}{q} + c$$

*Common loss of marks: integrating before splitting, and forgetting `+ c`.*

**Q2.** `f(x) = 3x³ − 3x² + 4x + c`. Substitute carefully:
`f(−2) = 3(−8) − 3(4) + 4(−2) + c = −24 − 12 − 8 + c = −44 + c = 11`, so `c = 55`.

$$f(x) = 3x^{3} - 3x^{2} + 4x + 55$$

*Two common losses: leaving `c` unresolved, and the signs of `(−2)³ = −8` against `(−2)² = +4`. The real paper puts its initial condition at a negative value for exactly this reason.*

**Q3.** Factor the denominator: `3q − q² = q(3 − q) = −q(q − 3)`.

$$\frac{(q-3)^{2}}{-q(q-3)} = -\frac{q-3}{q}$$

As `q → 3⁺`: `(q − 3) → 0⁺` and `q → 3`, so the expression → `−0 = 0`.

$$\lim_{q \to 3^{+}} = 0$$

*Marks are for the factoring and the sign discussion, not the zero.*

**Q4.** Divide numerator and denominator by `q³`:

$$\frac{4 - 5/q^{2} + 2/q^{3}}{7 + 1/q} \longrightarrow \frac{4}{7}$$

*The sign of the infinity does not matter here: both cubes dominate and the ratio of leading coefficients survives.*

**Q5.** Neither term is `1/x`. Ask of each: is the top the derivative of the bottom?

- `1/(x−1)`: the bottom differentiates to 1 → `ln|x − 1|`.
- `x/(x²−1)`: the bottom differentiates to `2x`, the top is `x`, so a `½` is missing → `½ ln|x² − 1|`.

$$\Big[\ln|x-1| + \tfrac{1}{2}\ln|x^{2}-1|\Big]_{0}^{1/3}
= \left(\ln\tfrac{2}{3} + \tfrac{1}{2}\ln\tfrac{8}{9}\right) - 0 \approx -0.4644$$

*The modulus is not decoration: on `[0, ⅓]` both `x − 1` and `x² − 1` are negative, and the logs are undefined without it. Marks are lost here every year.*

</details>

## After you have marked it

Count the marks you lost, and sort them into two piles:

- **method** — you did not know what to do;
- **execution** — you knew, and slipped.

The first pile is what the remaining weeks and the resit revision are for. The second is answered by writing more steps down, not by working faster.
