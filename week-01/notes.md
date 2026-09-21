# Week 1 — Revision of mathematics, told as business decisions

**MBA03 Research & Quantitative Business Methods · Thu 24 Sep 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: linear and quadratic equations, linear and quadratic inequalities, systems of equations, logarithms and exponentials, absolute values (Renshaw ch. 1, 3, 4, 5).

Running case for the whole session: **Arno Bikes**, a small e-bike assembler in Florence. Fixed monthly cost €60,000, variable cost €400 per bike, list price €1,000. Everything today is a question the founder actually has to answer.

## Learning objectives

By the end of the session the students can:

1. **Set up and solve** a linear equation and a 2×2 linear system from a verbal business situation (break-even; market equilibrium) — serves LO3/LO4 and the midterm's Q4 reasoning on cost shifts.
2. **Solve** a quadratic equation and a quadratic inequality by factoring or formula and **read the roots** as business quantities (loss/profit zones) — serves the midterm study of function (sign of the profit) and the factoring step inside the final exam's limits (`x − x² = x(1 − x)`).
3. **Manipulate** exponentials and logarithms (product, quotient, power rules; change of base) and **solve for time** in a growth problem — serves week 4 (continuous compounding, EAR) and the log integrals of final Q5.
4. **Read** an absolute-value condition as a tolerance band and solve `|x − a| ≤ b` — serves the resit's domain questions and general exam hygiene.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:10 | Welcome | Whiteboard | Who we are, how the first half works, what the exam looks like (show Q5 of the final for 60 seconds — no comment beyond "by 22 October you will do this on paper"). |
| 10:10–10:30 | **Diagnostic** | Paper | 10 anonymous items (`diagnostic.md`). Collected, not graded. Tutor skims during the break to calibrate blocks C and D. |
| 10:30–11:05 | **A. Launch or not?** | Slides → notebook → paper | Break-even as a linear equation. Market equilibrium as a 2×2 system. Three ways to solve a system (substitution, elimination, picture). |
| 11:05–11:40 | **B. How many bikes?** | Slides + clip → notebook → paper | Linear demand makes revenue a parabola. Profit zeros = quadratic equation. Profit > 0 = quadratic inequality. The vertex is a preview of week 2's maximum. |
| 11:40–11:55 | Break | — | Outside the room. Tutor reads the diagnostics. |
| 11:55–12:30 | **C. How long to double?** | Slides + clip → notebook → paper | Exponential growth; why we need logs; the three log rules and change of base; solving `1.12^t = 2`. Rule of 70 as a sanity check. |
| 12:30–12:45 | **D. Within tolerance** | Slides → paper | Absolute value as distance; `|x − a| ≤ b` as an interval; one inequality with `>`. |
| 12:45–12:55 | **Board pitch** | Student at the board | One student, 60 seconds, tells "the Board" the break-even, the profitable range and the doubling time. No formulas allowed in the pitch — only numbers and their meaning. |
| 12:55–13:00 | Close | Paper | Homework briefing; each student writes three take-home lines. |

## Script

### A. Launch or not? (linear equations and systems) — 35'

**Opening question (whiteboard):** "Arno Bikes pays €60,000 a month whether it sells one bike or a thousand, and €400 of parts per bike. It sells at €1,000. The founder asks: how many bikes a month before I stop losing money? Write your number before we compute anything."

Draw on the whiteboard two lines on a (q, €) plane: cost `C(q) = 60000 + 400q` and revenue `R(q) = 1000q`. Ask where they cross *before* drawing the crossing.

**Technique (one line):** break-even is `R(q) = C(q)` → `1000q = 60000 + 400q` → `600q = 60000` → **q = 100**. Slide "Two lines and a crossing".

Reading: €600 is the *contribution per bike*; break-even is fixed cost ÷ contribution. Say it once in words, once in symbols.

**Plotly (notebook §A):** slider on the price. Ask: "What price makes break-even 50 bikes?" They guess, the slider confirms (€1,600). Then: "What happens to the picture if the landlord raises the rent?" — the cost line shifts up parallel; break-even moves right. This *is* the midterm's Q4 (a tariff shifts the cost schedule): say so explicitly.

**Systems (whiteboard):** "Now the whole e-bike market in Tuscany. Buyers: `Q_d = 1200 − 2p`. Sellers: `Q_s = −300 + 3p`. What price clears the market?" Bet first. Then solve three ways, quickly: substitution (set `Q_d = Q_s` → `1500 = 5p` → **p = 300, Q = 600**), elimination (write both as `Q + 2p = 1200`, `Q − 3p = −300`, subtract), and the picture (slide "The whole market"). Point out that the picture is the check, the algebra is the answer the exam wants.

**Drills live:** D1, D2 (core), D3 (stretch) from `drills.md`. Students on paper, tutor circulates. 10 minutes.

**Closing sentence:** "One equation is one fact about the business. Two unknowns need two facts. The exam gives you the facts in words; your first job is always to write them as equations before touching a number."

### B. How many bikes? (quadratics) — 35'

**Opening question:** "The founder learns that at €1,000 she sells 150 bikes, and every €4 she cuts from the price sells one more bike: `p(q) = 1600 − 4q`. Revenue is now price × quantity. Is revenue a straight line? Bet: does selling more *always* bring more revenue?"

**Manim clip 1 (`anim/out/w01_parabola.mp4`, ~25 s):** the demand line `p(q)` and the rectangle `p·q` growing as q moves; the rectangle's area traced out becomes the revenue parabola. Caption: *"Revenue is the area of a rectangle whose sides pull in opposite directions."*

**Technique:** `R(q) = (1600 − 4q)q = 1600q − 4q²`. Profit `π(q) = R − C = −4q² + 1200q − 60000`. Slide "Revenue, cost, profit".

"Where is profit zero?" Solve `−4q² + 1200q − 60000 = 0`. First move: divide by −4 → `q² − 300q + 15000 = 0`. Formula: `q = (300 ± √(90000 − 60000))/2 = (300 ± √30000)/2 = (300 ± 173.2)/2` → **q ≈ 63.4 and q ≈ 236.6**. Say the discriminant out loud as "how far apart the two break-evens are".

**Inequality:** "For which q is she profitable?" A downward parabola is positive *between* its roots: **63.4 < q < 236.6**. Draw the sign line under the parabola (slide "The discriminant decides"). This exact sign line reappears in the midterm's "sign of the profit function".

**Plotly (notebook §B):** slider on fixed cost. Push fixed cost up: roots move together; at €90,000 they merge (discriminant zero — one break-even, touching); above, no roots — "there is no quantity that makes money". Ask them to predict the fixed cost at which the roots merge *before* sliding (answer: vertex value 30,000 above 60,000).

Vertex: `q = −b/(2a) = 150`, `π(150) = 30,000`. Do not derive; say "week 2 gives you a tool that finds this point for *any* curve, not just parabolas".

**Drills live:** D4, D5 (core), D6 (stretch: factor-and-cancel, the final-exam pattern). 10 minutes.

**Closing sentence:** "A quadratic has two roots, one root or none, and the discriminant tells you which before you compute anything. In business the three cases are: a profitable window, a single break-even, no viable scale."

### C. How long to double? (exponentials and logarithms) — 35'

**Opening question:** "Arno Bikes' revenue is €1.2M and grows 12% a year. Bet: how many years to double? Write it down."

**Manim clip 2 (`anim/out/w01_growth.mp4`, ~30 s):** linear growth (+€144k a year) versus compound growth (×1.12 a year) from the same start, the gap widening; a horizontal line at €2.4M and the two crossing times. Caption: *"Linear adds the same amount; exponential adds the same percentage."*

**Technique:** `1.2 · 1.12^t = 2.4` → `1.12^t = 2`. The unknown is in the exponent: no algebra we have so far reaches it. That is *what a logarithm is for*: `t = log₁.₁₂ 2 = ln 2 / ln 1.12 = 0.6931 / 0.1133 ≈ **6.1 years**`. Slide "The unknown is in the exponent".

Board: the three rules, each with a one-line reason and the business reading:
- `ln(ab) = ln a + ln b` — growth factors multiply, their logs add (two years of 12% then 8% → add the logs).
- `ln(a/b) = ln a − ln b` — a ratio of revenues becomes a difference.
- `ln(aᵏ) = k ln a` — k years of the same growth: the exponent comes down. This is the rule that solved the doubling problem.
- Change of base `log_b x = ln x / ln b`; `e ≈ 2.718` introduced as "the base your calculator and week 4 prefer" — nothing more today.

Rule of 70: `70 / 12 ≈ 5.8`. Show why it is close (`ln 2 ≈ 0.69`, `ln(1+g) ≈ g` for small g) in one line; it is their exam sanity check.

**Drills live:** D7, D8 (core), D9 (stretch: solve `5e^{0.03t} = 8`; preview of continuous compounding). 12 minutes.

**Closing sentence:** "Whenever the unknown is in the exponent, take logs of both sides. Whenever you see a log, remember it is a question: 'to what power?'"

### D. Within tolerance (absolute value) — 15'

**Opening question:** "Battery cells must be 500 Wh ± 15. A supplier ships a cell at 483 Wh. In or out?" Bet, then write it as `|c − 500| ≤ 15` ↔ `485 ≤ c ≤ 515`. Slide "Is this cell within spec?".

Two moves only: `|x − a| ≤ b` is the closed interval `[a − b, a + b]`; `|x − a| > b` is the two tails `x < a − b` or `x > a + b`. One drill each (D10, D11). Mention that the resit asks for domains written as intervals with round and square brackets — practise the notation now.

### Board pitch — 10'

One student stands up; the other is the Board. Sixty seconds, no formulas: break-even 100 bikes a month at the current price; profitable window between about 63 and 237 bikes once price responds to volume; revenue doubles in roughly six years at 12%. The Board asks one question. Tutor notes clarity for the trajectory record.

### Close — 5'

Homework briefing (see `homework.md`). Three take-home lines written on paper, photographed, posted on Moodle.

## Key concepts (one line each, for the students' notes)

- Break-even: revenue = cost; fixed cost ÷ contribution per unit.
- A system of two equations = two facts about the same unknowns; solve by substitution or elimination; the graph is the check.
- Quadratic `ax² + bx + c = 0`: divide by a common factor first; discriminant `b² − 4ac` decides two/one/no roots.
- Quadratic inequality: find the roots, draw the parabola's sign line, read the interval.
- Exponential growth: same *percentage* each period; `A · (1+g)^t`.
- Logarithm: the answer to "to what power?"; `ln(aᵏ) = k ln a` pulls the unknown down from the exponent.
- Rule of 70: doubling time ≈ 70 / growth rate in %.
- `|x − a| ≤ b` ↔ `a − b ≤ x ≤ a + b`.

## Board, slide, screen — what goes where

There are two students in the room. A deck built to broadcast to thirty is the wrong
instrument for two; the board is not a display, it is the table you work at together.

**On the board, always.** Every rearrangement. `1,000q = 60,000 + 400q` becomes
`600q = 60,000` becomes `q = 100` **in front of them, at the speed of thinking**. The
exam says *ALL WORK must be shown* and marks the method: students write what they have
watched being written. Show only finished algebra and they will write finished algebra
with no steps, and lose marks they had earned.

**On the slide.** The picture, the clip, the rules table, the bet, where-we-are, and the
Board sentence. Things a board does badly or slowly.

**On screen.** Only when a *parameter moves*: this week, the price slider and the fixed-cost
slider. That is the one thing neither board nor chalk can do. Full-screen the figure — never
scroll through code. They do not write Python in this course, they never will, and showing
them a cell they cannot read spends credibility for nothing.

The slide after a derivation is the **check**, not the teaching: do it on the board, then
click to the slide and let them see it agrees.

## Tutor's notes

- **What needs the projector:** the deck (`slides/week01.pdf`; LAB frames are the cue to switch to the notebook, PAPER frames to the drills), notebook §A and §B sliders, the two manim clips (▶ link on the black frames). Everything else is whiteboard and paper; if the projector fails, the session survives.
- **If behind:** cut D (absolute values) to five minutes — one example, one drill in the homework. Never cut block C: logs are the bridge to week 4 and to final Q5.
- **If the diagnostic is weak on algebra** (fewer than 5/10 on items 1–5): spend the first ten minutes of block B on the quadratic formula itself, skip the plotly discriminant exploration, move D6 to homework stretch.
- **If the diagnostic is strong:** do D3, D6, D9 live and start sketching the parabola with intercepts and vertex — it shortens week 2.
- **Energy:** the parabola clip and the growth clip are the two "look at this" moments; place them right after each opening question, not after the algebra.
- **Language:** the students will hear "contribution", "break-even", "equilibrium", "tolerance". Write each on the board the first time.
- **Record for grading:** keep the diagnostics (anonymous but you will recognise handwriting) and a two-line note per student on the Board pitch. They are the baseline for the trajectory judgement in the midterm.
