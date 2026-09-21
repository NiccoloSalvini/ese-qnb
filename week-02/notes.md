# Week 2 — The tool that finds the top of any hill

**MBA03 Research & Quantitative Business Methods · Thu 1 Oct 2026, 10:00–13:00 · Tutor: Niccolò Salvini**

Syllabus topic: functions and the Cartesian plane, limits, differentiation, integration (Renshaw ch. 6, 7, 8, 9, 18). **Plus the midterm guidelines briefing, which the syllabus places here and which must happen.**

## Learning objectives

By the end of the session the students can:

1. **State the domain** of a root, a log and a rational function as an interval, and say what the restriction means for a firm — serves the resit's domain questions and step 1 of the midterm's function study.
2. **Evaluate** a `0/0` limit by factoring, a one-sided limit, and a limit at infinity, and give the business reading of the last — serves two of the five items of the final's Q5.
3. **Differentiate** a polynomial, a log and a sum term by term, and **read** `f'(a)` as "what one more unit does" — serves the midterm's Q3 and the final's Q5.
4. **Recover** a function from its derivative with an initial condition, and recognise the constant of integration as fixed cost — serves the final's Q5 item 2.

## Session plan

| Time | Block | Support | Content |
|------|-------|---------|---------|
| 10:00–10:15 | HW1 walkthrough | Paper | One student takes us through one drill at the board. Not a performance: I want to see the working, including the wrong turn. |
| 10:15–10:50 | **Midterm briefing** | Slides + guidelines | The brief line by line, the seven required elements, the timetable back from 1 Nov. Questions now. |
| 10:50–11:15 | **A. What a function is, once you have to use one** | Slides → paper | Four functions, one firm. Domain as the first question. |
| 11:15–11:30 | break | — | Outside the room. |
| 11:30–12:00 | **B. Limits** | Slides → notebook → paper | Average cost at 0 and at ∞. The `0/0` that factors. |
| 12:00–12:40 | **C. The derivative** | Slides + 2 clips → notebook → paper | Secant to tangent. Read the slope. Last week's vertex, recovered. |
| 12:40–12:52 | **D. Running it backwards** | Slides → paper | Antiderivative, the constant, and why it is the rent. |
| 12:52–13:00 | Board pitch and close | Student at the board | Sixty seconds: should the 81st bike be built? |

## Script

### Midterm briefing (35')

Do this first, while everyone is fresh, and do not let it slide. The guidelines are on the student portal; read them **on screen, together**, rather than paraphrasing.

Cover, in this order:
1. **What is being asked.** A report to a Board, built on the study of a cost, a revenue and a profit function, plus qualitative sections. 1,500 words ±10%, plus an oral.
2. **The seven elements** a full function study must contain. Write them on the board; they reappear in week 3 and in every drill from here.
3. **The qualitative sections.** What "research" means here: a claim, a source, a Harvard reference. Two good sources beat eight bad ones.
4. **Format.** Cover, contents, executive summary, introduction, methodology, findings, analysis, conclusions. Arial 12, double spaced.
5. **The timetable**, backwards from Sunday 1 November: draft of the maths by 18 Oct, draft of the prose by 25 Oct, office hour in reading week, submit Saturday not Sunday.
6. **Failure modes**, named plainly: sketching without studying; studying without a sketch; no second derivative; the qualitative sections written as filler; submitting at 23:55.

Say once, clearly: **no late submission for postgraduate work.** A missed deadline is a resubmission capped at 50%.

### A. What a function is (25')

**Opening question:** "Four functions on the board. Which one is Arno Bikes' cost, and how do you know without being told?" Let them argue from the shape of the formula: a constant plus something per unit.

**Domain first.** `√(q−20)`, `ln(q−5)`, `120/(q−40)`. Each restriction is a sentence about the firm. The exam wants the interval with the right bracket; the log is the one that trips people, because it is strict.

**The bet:** `π(100)` vs `π(200)`. They will pick 200 — more bikes, more profit. Both are €20,000. The parabola is symmetric about 150. Let that land before explaining it.

→ **D1, D2** on paper, 10 minutes.

### B. Limits (30')

**Opening:** "Average cost at zero output. Compute it." They cannot; that is the point.

`AC(q) = (60,000 + 400q)/q`. Near zero it explodes; far out it settles at 400. Say the economics out loud: **fixed cost spread over a long run disappears, and average cost falls to the variable cost.** That is economies of scale in two limits, and it is worth more to them than the notation.

**The `0/0`.** `(q²−100)/(q−10)` at `q = 10`. Substitute first and you get `0/0`, which says nothing. Factor, cancel, *then* substitute. State the rule as an instruction, not a fact: **`0/0` means factor.**

Notebook: the sympy cell. Use it to confirm, never to discover.

→ **D4, D5, D6** on paper, 12 minutes. D5 is the exam's one-sided limit.

### C. The derivative (40')

**Opening question:** "You made 80 bikes last month. What does the eighty-first add? Write a number before we compute anything." Collect two or three guesses aloud.

**Clip 1 — `w02_secant`.** Play it once without commentary. Then ask what they saw before saying it: two points, a slope, the points coming together. Then the definition, once, on the board. Say plainly that they will use the definition twice in their lives and the rules every day.

**The rules table.** `qⁿ → nqⁿ⁻¹`, constants vanish, `ln q → 1/q`, sums term by term. That is the whole of what the exam needs.

**Clip 2 — `w02_tangent`.** The tangent walking the curve, slope positive then flat then negative. Pause it at the top. "What is true here that is true nowhere else?"

**The payoff, and say it as a payoff:** last week they found `q = 150` with `−b/2a`, which only works for parabolas. `π'(q) = −8q + 1200 = 0` gives the same 150 — and still works when revenue is a log. This is the moment the course justifies itself.

Notebook: slide the price drop from €4 to €3 to €6 and watch the optimum move from 150 to 200 to 100. Bet first.

→ **D8, D9** on paper, 12 minutes. Insist on the *sentence* in D9, not just the number.

### D. Running it backwards (12')

Given `f'`, find `f`. The constant is the whole lesson: every `2q³ − q² + c` has the same derivative, so one fact pins it down.

Then the economics: from `MC(q) = 0.8q + 3` and `C(0) = 25`, the constant of integration **is the fixed cost**. Not an analogy — the same number.

→ **D11, D12** on paper, 8 minutes.

### Board pitch (8')

One student, sixty seconds, no formulas: what the 81st bike adds, where the answer turns negative, and one thing they would check first. The last part is the one that separates a good midterm from a mechanical one.

## Key concepts (one line each, for the students' notes)

- The **domain** is the first question about any function, and the exam wants it as an interval.
- `0/0` is not an answer; it is an instruction to factor and cancel.
- A **limit at infinity** answers "what happens in the long run" — average cost falls to variable cost.
- The **derivative** is what one more unit does: positive, make more; negative, make fewer; zero, stop.
- `−b/2a` works for parabolas. `f'(q) = 0` works for everything.
- Reversing a derivative needs a **constant**, and in cost functions that constant is the fixed cost.

## Board, slide, screen — what goes where

**On the board.** The definition of the derivative, once, written out. The factoring of
every `0/0`. The whole of block D — the antiderivative and the constant. Anything where a
line becomes the next line.

**On the slide.** The four-functions table, the domain examples, the rules table, both
clips, the week-1-versus-week-2 comparison. The clip earns the slide: motion is the one
thing chalk cannot do.

**On screen.** Once, in block C: slide the price drop from €4 to €3 to €6 and watch the
optimum move from 150 to 200 to 100. Bet first, then slide. Then close it.

The bet is the highest-value thirty seconds of the session and it costs nothing: make them
commit to a number, out loud, before any arithmetic. With two students there is nowhere to
hide, which is the point.

## Tutor's notes

- **The briefing is not optional and not compressible.** If the clock is tight, cut block B's stretch items and let the notebook carry the limits — never the briefing.
- The `π(100) = π(200)` bet is the best twenty seconds of the session. Do not spoil it by explaining symmetry first.
- Clips are for intuition, not instruction. Play each once, ask what they saw, play again only if asked.
- If the room is ahead: D3, D7, D10 (the definition from first principles). If behind: drop D10 and the second notebook slider, keep D9 and D11 whatever happens — both are exam items.
- The projector is needed for both clips and the notebook slider. Check it before 10:00; the slider is the one thing that does not work from a PDF.
- Watch for the student who differentiates correctly and cannot say what the number means. That gap is what the midterm punishes, and it is fixable only by making them say the sentence out loud, every time.
