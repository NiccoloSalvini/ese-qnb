# CLAUDE.md — Research & Quantitative Business Methods (ESE Florence)

Course repository *and* course website of *MBA03 Research & Quantitative Business
Methods*, ESE MBA, Florence, Term 1 A.Y. 2026–2027. Module leader Arianna Ziliotto.
Weeks 1–5 Niccolò Salvini, in person, Thursdays 10:00–13:00, 24 Sep → 22 Oct 2026;
weeks 6–10 Vincenzo Nardelli: week 6 Thu 5 Nov in person in Florence, then weeks 7–10
online, Mondays 10:00–13:00, 9 → 30 Nov 2026.

Live site: <https://niccolosalvini.github.io/ese-qnb/> · Repo: `NiccoloSalvini/ese-qnb` (public)

How a session is designed and what a session pack contains: the project skill
`.claude/skills/ese-qnb-method/`. Both halves follow it.

Sibling of `~/dev/ese-ai` (same site skeleton, same brand, same deploy). Read that
repo's `CLAUDE.md` for the Quarto/GitHub Pages gotchas; they all apply here.

## Confidentiality — read before writing anything

The repo is **public**. ESE official documents (syllabus PDF, midterm guidelines,
exam and resit papers with model answers) live outside the repo, in each lecturer's
own folder (Niccolò's: `~/Downloads/ese-qnb-material/`), and are **never** copied here: no exam item, no
model answer, no midterm case function. Drills and homework use the same *form*
with different functions and numbers. `syllabus/` is gitignored as a guard.
Grading material, feedback and the handover to the colleague stay private.

## Commands

```bash
make preview   # quarto preview
make build     # quarto render -> _site/
make deploy    # render locally, then quarto publish gh-pages
make clean
```

No CI. Rendered here, `_site/` pushed to the `gh-pages` branch.

## Layout

```
week-NN/
  notes.md            tutor-only plan and script — NOT rendered
  slides/weekNN.tex   (week 1 only) beamer (metropolis) PDF deck, kept for printing; new weeks have no beamer deck
  slides/weekNN.pdf   (week 1 only) compiled deck (resource) — TinyTeX needs metropolis + pgfplots (tlmgr install)
  session.ipynb       Colab notebook: projector demos (plotly sliders), then "Drills, solved in code" — every drill
                      of drills.md solved in Python with an assert on the published answer. Optional companion for
                      students, linked as "code ↗" on the schedule; not examined
  build_notebook.py   regenerates session.ipynb next to itself — needs a Python with nbformat, then
                      `jupyter nbconvert --to notebook --execute --inplace week-NN/session.ipynb`; not rendered
  drills.md           in-class exercises, exam format, worked solutions in a <details> block — rendered
  homework.md         drill set + memo to the Board — rendered
  diagnostic.md       (week 1) anonymous placement test — NOT rendered (would defeat its purpose)
anim/src/weekNN_scenes.py  manim scenes, two per week, 10-12s each; common.py holds the palette and the
                      Arno Bikes functions. `bash anim/render.sh [weekNN]` renders at 720p30, copies the
                      mp4 into anim/out/ and a poster frame into anim/frames/. Needs the manim venv at
                      ~/.venvs/sbd-animations. Clips and posters are then copied into lectures/media/.
midterm/briefing.md   how to read the brief and write the report — method only, none of the brief's content
lectures/NN-slug.qmd  THE deck shown in class: revealjs with the ESE theme (lectures/ese.scss), clips embedded
                      as <video poster=...> from lectures/media/, figures as SVG from lectures/figs.py (matplotlib)
                      (plus lectures/figs_w04_gordon.py and figs_w05_immunisation.py for the beyond-the-syllabus blocks)
lectures/_metadata.yml every visual option of the revealjs decks; a lecture file sets title, subtitle, author, content
index.qmd             schedule table = home page; assessment scheme; readings
setup.qmd             "How to work": what to bring, homework hand-in, notebooks, exam-style writing
styles.scss, _fonts.html, images/   copied from ese-ai (ESE brand: red #AF1F25, gold #CDBA80, Source Sans 3)
```

`_quarto.yml` lists rendered files explicitly. Add a week by dropping the folder
in and replacing the `—` cells in the week's row of `index.qmd`.

## Decks: revealjs first, beamer for the PDF

The deck the students see is `lectures/NN-slug.qmd` (revealjs), same convention
as `sbd_26_27/lectures/`: section slides
`## [Block A]{.section-kicker} Title {.section-slide background-color="#AF1F25"}`;
LAB frames `## Title {.lab background-color="#2471A3"}` with `[LAB · session.ipynb § A]{.kicker}`;
PAPER frames `## D1, D2 {.paper background-color="#eceff0"}`;
clip frames `## Title {.clip background-color="#000000"}` with a raw `<video class="clipvideo" controls poster="media/x_poster.png">`
(the `{{< video >}}` shortcode gives a black box with a tiny play button on a black manim clip);
a one-line slide is `## Text {.statement}`;
"Bet" = `callout-important`, "Board sentence" = `callout-tip`; math is KaTeX.
Figures are SVGs written by `lectures/figs.py` (matplotlib, brand colours, `svg.fonttype: none`
so the page's webfont renders the labels). Copy the mp4 and a poster PNG into
`lectures/media/`. The beamer `.tex` stays as the printable PDF; keep the two in step or drop the PDF.

Reveal font gotcha (as in ese-ai): `ese.scss` re-sets `--r-main-font` in the rules
section with quoted names, because Quarto interpolates the SCSS variable unquoted
and `Source Sans 3` unquoted is invalid CSS.

## Two traps in the clips, both cost a re-render

`ax.plot(self.method, ...)` fails with `cannot pickle '_thread.lock'`: manim caches the plotted
function and pickling a bound method drags the Scene, locks included. Plotted functions must be
module level. And `get_riemann_rectangles` defaults to **left** endpoints — compute the displayed
approximation the same way, or the drawing and the number disagree. (The midpoint rule is exact for
a straight line, which shows no convergence at all.)

## Every number is verified before it ships

Drills, homework and the mock have worked solutions, and every one was checked with sympy before
being committed: derivatives, limits, integrals, bond prices, durations, NPV and IRR. Three of my own
slips were caught that way. When you change a number in a drill, re-run the check — the notebooks'
final cell does exactly this for the week's drills, on purpose.

## Weeks 6–10 (Vincenzo's half)

Same deck conventions and Niccolò's skeleton (four questions from the founder, bet → picture →
one formula → Board sentence), manim clips in anim/src/week07_*.py (venv ~/.venvs/ese-manim; the
Homebrew ffmpeg on this Mac is broken, render.sh makes posters with PyAV) and interactive apps in
lectures/apps/w07_*.html. Weeks 6 and 7 have a session.ipynb like weeks 1–5. The exam allows a calculator,
the standard normal table (or `NORM.S.DIST`) and paper, so the decks show formula, substitution,
number, one-sentence business reading; no textbook page references, no exam coaching.
lectures/figs_w07.py writes the week's SVGs; lectures/check_w07.py asserts every number in deck,
drills and homework (scipy.stats): run both with python3.11 before committing. The source handouts
live outside the repo in ~/Desktop/ese/dispense/.

## Weekly loop

Session → next day: deck, drill solutions and homework online (`make deploy`)
→ next session, first 15–20' on the homework at the board. Homework is on paper and
formative: nothing is handed in or graded.

## Moodle

Site: <https://esestudents.com> (**no `www`** — the other host answers
`requirecorrectaccess`). Moodle 4.5.10. This course is **id 2546**
(`MBA003_262701_FL`); the AI course is 2531.

Access is through `mcp-moodle-teacher` (own server,
<https://github.com/NiccoloSalvini/mcp-moodle-teacher>), wired in `.mcp.json`.
It reads enrolments, submissions, what is missing and the gradebook, and writes
a grade with feedback or a news-forum announcement. The published `moodle-mcp`
packages are student-side and were dropped.

Token: each lecturer's own, in this repo's `.env` (gitignored, mode 600; copy
`.env.template`). The server repo is private: once invited, clone it with
`gh repo clone NiccoloSalvini/mcp-moodle-teacher ~/dev/mcp-moodle-teacher`, then run
`MOODLE_SITE=https://esestudents.com bash ~/dev/mcp-moodle-teacher/scripts/get-moodle-token.sh`.
The script writes the token into the server repo's own `.env`: copy the
`MOODLE_TOKEN=` line into this repo's `.env`.
Export it before launching Claude Code: `set -a; . .env; set +a`. *Preferences >
Security keys* is empty for lecturer accounts — the role lacks
`moodle/webservice:createtoken`, which is why the script exists.

**Materials cannot be uploaded through the API**: Moodle core has no web service
that creates a module. The course page carries links to this site instead.
