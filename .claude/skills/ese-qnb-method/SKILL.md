---
name: ese-qnb-method
description: "How sessions of MBA03 Research & Quantitative Business Methods (ESE Florence, T1 AY26/27) are designed and built in this repo, for both halves: weeks 1–5 (Niccolò Salvini) and weeks 6–10 (Vincenzo Nardelli). Use it for any request to prepare a session or a piece of one: the revealjs deck, notes, drills, homework, Colab notebook, manim clip, SVG figures, a mock or revision set, the week's row on the site, or publishing it. Use it even when the request only says \"week 7\", \"Thursday's slides\", \"a drill on the binomial\", \"check these numbers\" or \"put it online\"."
---

# How this course is taught and built

`CLAUDE.md` at the repo root is the reference for layout, commands and the Quarto, revealjs and manim gotchas. Read it first. This skill is the method on top of it: what a session is for, what a session pack contains, and the rules that keep a public repo safe. It holds for both halves of the module, so that weeks 6–10 look and work like weeks 1–5.

## The course, in brief

- ESE MBA, Florence. Term 1, A.Y. 2026–2027, 30 contact hours. Module leader **Arianna Ziliotto**: she owns the syllabus and wrote the assessments.
- Weeks 1–5: **Niccolò Salvini**, in person, Thursdays 10:00–13:00 (24 Sep → 22 Oct). Algebra revision, calculus, financial mathematics. He marks the midterm.
- Weeks 6–10: **Vincenzo Nardelli**, online, Thursdays 10:00–13:00, from 5 November to mid-December. Probability and distributions, then econometrics and time series. The topics per week are in the schedule table in `index.qmd`.
- Students: a small group of MBA students in Florence, in the room for weeks 1–5 and online for weeks 6–10. Their quantitative background is mixed and largely unknown. They do not write code. A formula-first approach was disliked the year before.
- Assessment (public, in `index.qmd`): midterm 25% (a research paper on a business case built on a cost, a revenue and a profit function, plus an oral in week 6); final exam 75% (three hours, five equal questions, all work shown, non-programmable calculator, no notes). One question of the final is pure calculus (weeks 2–3); the others come from the second half. The resit covers the whole module. In-class quizzes fall in weeks 3, 7 and 10.

What is fixed is the content: the syllabus and the exam papers. What is free is the delivery. This skill is about the delivery.

## Confidentiality: the repo is public

The ESE documents (syllabus PDF, midterm guidelines, final and resit papers with model answers) live **outside** the repo, in each lecturer's own folder. Niccolò's is `~/Downloads/ese-qnb-material/`. If you do not know where the current lecturer keeps theirs, ask; do not guess.

- Read those documents before writing anything that touches assessment, so that each drill rehearses the right *form* of exam item. If they are not at hand yet, do not stop: work from the forms already public in the repo (`index.qmd`, the existing drills and mocks), mark every mapping to an exam item **TBC** in `notes.md`, and ask.
- Never copy into the repo an exam item, a model answer, the midterm case and its functions, or the lecturer's marking grid. Name an exam item by its form, as the repo already does ("the final's calculus question", "the resit's multiple-choice block"), and say no more about what it asks than `index.qmd` says. Drills, homework and mocks use the same form with **different functions and numbers**. If a sentence would let a student reconstruct the paper, it does not ship.
- Students' names, marks, feedback and submissions never go in the repo. Midterm marking lives in `midterm/marking/`, quiz items and their key in `week-NN/quiz.md`, tutor scripts in `week-*/talk.md` and `week-*/copione-*`: all of them are gitignored. `notes.md` holds only the quiz's slot and what it covers. Keep it that way, and check `git status` before committing.
- `syllabus/` is gitignored as a guard. Do not create an ESE document anywhere else in the tree.

## How a session is built

These choices came from what did not work the year before, and they are why the students follow.

- **Backward design from the two assessments.** Every technique is there because a specific exam item or midterm question needs it, and the students are told which one. In `notes.md`, each learning objective names the item it serves.
- **The direction of the arrow: decision → picture → technique → decision.** Each block opens with a business decision (how much to produce, whether to accept a project, what a rate rise does to a bond, whether a defect rate is acceptable). It is explored on screen with a clip or a slider. The technique is then done by hand, in exam format, and the block closes with a one-sentence "Board sentence" a manager would say.
- **Half slides, half laboratory.** The deck is the spine and follows one thread. At fixed points it hands over to the notebook (LAB slides) and to paper (PAPER slides). One idea per slide, the picture before the formula, no bullet dumps. The decks of weeks 1–5 run 40–50 slides counting section and hub slides: treat that as a ceiling, not a target.
- **Mathematics present, and presented well.** Formulas are written properly, named, and given a business reading underneath. Derive only when the derivation builds intuition (marginal = derivative, accumulation = integral, a probability as an area). Everything else is a rule, applied and drilled.
- **The time of a three-hour session:** the first 15–20 minutes on the previous homework at the board; about 40 minutes of decision and intuition (slides, clip, notebook); about 80 minutes of guided hand computation on exam-format drills; a short Board pitch by one student; about 10 minutes for the homework briefing and three take-home lines. A real break in the middle. When a week has no homework to correct, or has a quiz, the orals or the midterm feedback, the split cannot hold as it is: say in `notes.md`, block by block, what gives. Weeks 6–10 are online: keep the structure, but agree with the lecturer how the paper blocks run remotely, on the first pack of weeks 6–10. Do not decide it for them.
- **Animations are for intuition, never a video lecture.** Manim clips of 10–12 seconds, at most two or three per week, each with a one-sentence caption and followed by the slider version, where the lecturer moves a parameter live.
- **Mixed backgrounds** are handled with two tracks of drills: a core set everyone does and a stretch set for whoever is ahead. Never slow the course down to the weakest item; add office-hour material instead.
- **Firms, not abstract functions.** The running case is **Arno Bikes**, an e-bike assembler in Florence (fixed cost €60,000/month, variable cost €400/bike, demand p = 1600 − 4q). Its shared functions are in `anim/src/common.py`. Reuse it wherever it fits, including in the second half (defect rates, demand uncertainty, sales against advertising), so that the students always meet a familiar firm. When the second half needs a new shared value (a demand spread, a defect rate), add it to `common.py` with a comment, so that both halves use the same firm.
- **Homework is on paper and formative.** Nothing is handed in or graded: it is corrected together at the start of the next session. A homework with no session after it goes by email. The only deliverables are the assessments, on Turnitin.

## The session pack for week N

These are the files of a full session. Write the ones that were asked for, and list the rest as next steps instead of writing them unasked. Copy the shape of an existing week rather than inventing a new one; `week-05/` and `lectures/05-bonds-and-risk.qmd` are the most mature.

1. **`week-NN/notes.md`**: the lecturer's plan, not rendered, in English like every other material. Three to six learning objectives, verb-first, each mapped to the exam item or midterm question it serves; a timing table (time, block, support, content); a script per block (the opening question with a bet in it, the picture and what students should notice before anyone speaks, the technique in one formula, the drill numbers to do live, the Board sentence); what to cut if behind. A slide-by-slide `talk.md` is optional and stays local.
2. **`lectures/NN-slug.qmd`**: the deck shown in class, in revealjs. Every visual option is in `lectures/_metadata.yml`; a lecture file sets only title, subtitle (`Week n · date · time`), author, institute and content. The slide types (section, LAB, PAPER, clip, statement, Bet, Board sentence) are listed in `CLAUDE.md`; the week-5 deck also shows the hub slides, recap blocks and small classes (`.kicker`, `.muted`). Use the classes already in `lectures/ese.scss` and add no new ones. Math is KaTeX. Render the deck and look at it before calling it done.
3. **Figures**: `lectures/figs_wNN_<topic>.py`, one or more per week, matplotlib with the brand palette and `svg.fonttype: none`, writing SVGs into `lectures/img/`. Each script stands on its own; `figs.py` is the week-1 original.
4. **Clips**: scenes in `anim/src/weekNN_scenes.py` (the palette and the Arno Bikes functions are in `common.py`), the week added to `anim/render.sh`, then the mp4 and its poster frame copied into `lectures/media/`. Read the two traps in `CLAUDE.md` before writing a scene; each costs a re-render.
5. **`week-NN/session.ipynb`**, generated by `week-NN/build_notebook.py` (nbformat): the projector demos with plotly sliders first, then "Drills, solved in code", one cell per drill part with an `assert` on the answer published in `drills.md`. Execute it with nbconvert before delivering. It is optional for students and not examined.
6. **`week-NN/drills.md`**: ten to eighteen items, core and stretch, in exam wording, labelled D1, D2… by block. Calculus and financial mathematics: "Evaluate…", "Determine…", "Study the function…", "Select the correct alternative and justify in one line…". Probability and statistics: "Find the probability that…", "Determine the expected value and the standard deviation…", "State H₀ and H₁ and test at the 5% level…", "Construct a 95% confidence interval for…". Worked solutions go in a `<details>` block, written the way an examiner wants to see them: method first, number second.
7. **`week-NN/homework.md`**: five to eight drill items (two to three hours), one "memo to the Board" of 150–250 words applying the week's technique to a stated firm, a self-check list, and a line on what it prepares for.
8. **The site**: add any new rendered file to the explicit list in `_quarto.yml`, replace the `—` cells in the week's row of `index.qmd`, run `make build`, look at the pages, then `make deploy`.

## Every number is checked before it ships

Every worked solution is verified in code before it is committed: sympy for calculus and financial mathematics, scipy.stats or an exact computation for probabilities, tables and test statistics. The notebook's assert cells are that check, kept on purpose; until the week has a notebook, put the same checks in a script and run it. The strongest check also confirms that each rounded figure, exactly as printed, appears in `drills.md`, so that the published text cannot drift from the computation. When a number in a drill changes, re-run the check. A slip found by a student costs more trust than the ten minutes the check takes.

Round only at the end, and say in the solution how many decimals the answer is given to. Probabilities read from a table are the exception: round z to two decimals as the table does, give the table's value, and add the software's value in brackets when the fourth decimal differs. Use the table the exam provides; if you do not know which, ask.

## Weekly loop

Session → by the next day, deck, drill solutions and homework on the site (`make deploy`) → next session, the first 15–20 minutes go through the homework at the board.

Moodle (course id 2546) mirrors the site with links. Materials cannot be uploaded through the API, and the setup for the `mcp-moodle-teacher` server is in `CLAUDE.md`. Each lecturer uses their own token in their own `.env`. Announcements and grades are visible to students the moment they are written, so show the text to the lecturer and get a yes first.

## Who owns what

Niccolò owns weeks 1–5, the midterm briefing, and the midterm marking and its feedback. Vincenzo owns weeks 6–10 and the final exam's questions on them. Shared files (`index.qmd`, `setup.qmd`, `_quarto.yml`, `README.md`, `CLAUDE.md`, the theme) belong to both: change only what the current task needs. Do not edit the other half's weeks without asking.

## Style

- Materials are in English: plain, technically precise, the register of an MBA without buzzwords, never talking down. Talk to the lecturer in their own language.
- In the script, the lecturer asks a question with a bet inside, shows the picture, then gives the technique. The explanation follows the students' attempt.
- Commit messages are one plain sentence on what changed and why, as in `git log`. Commit only what the task produced.
