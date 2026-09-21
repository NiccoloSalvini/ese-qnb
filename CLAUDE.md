# CLAUDE.md — Research & Quantitative Business Methods, weeks 1–5 (ESE Florence)

Course repository *and* course website for the first half (weeks 1–5, Niccolò
Salvini) of *MBA03 Research & Quantitative Business Methods*, ESE MBA, Florence,
Term 1 A.Y. 2026–2027. Module leader Arianna Ziliotto; Vincenzo Nardelli teaches
weeks 6–10 online after Reading Week. Thursdays 10:00–13:00, 24 Sep → 22 Oct 2026.

Live site: <https://niccolosalvini.github.io/ese-qnb/> · Repo: `NiccoloSalvini/ese-qnb` (public)

Sibling of `~/dev/ese-ai` (same site skeleton, same brand, same deploy). Read that
repo's `CLAUDE.md` for the Quarto/GitHub Pages gotchas; they all apply here.

## Confidentiality — read before writing anything

The repo is **public**. ESE official documents (syllabus PDF, midterm guidelines,
exam and resit papers with model answers) live in
`~/Downloads/ese-qnb-material/` and are **never** copied here: no exam item, no
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
  slides/weekNN.tex   beamer (metropolis) PDF deck, kept for printing; the PDF is committed and linked as "pdf"
  slides/weekNN.pdf   compiled deck (resource) — TinyTeX needs metropolis + pgfplots (tlmgr install)
  session.ipynb       Colab notebook driven from the projector (plotly sliders, sympy checks); rendered read-only
  build_notebook.py   regenerates session.ipynb — not rendered
  drills.md           in-class exercises, exam format, worked solutions in a <details> block — rendered
  homework.md         drill set + memo to the Board — rendered
  diagnostic.md       (week 1) anonymous placement test — NOT rendered (would defeat its purpose)
anim/src/             manim scenes; anim/out/*.mp4 committed and linked as clips; anim/frames/ used by the beamer deck
lectures/NN-slug.qmd  THE deck shown in class: revealjs with the ESE theme (lectures/ese.scss), clips embedded
                      as <video poster=...> from lectures/media/, figures as SVG from lectures/figs.py (matplotlib)
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
"Bet" = `callout-important`, "Board sentence" = `callout-tip`; math is KaTeX.
Figures are SVGs written by `lectures/figs.py` (matplotlib, brand colours, `svg.fonttype: none`
so the page's webfont renders the labels). Copy the mp4 and a poster PNG into
`lectures/media/`. The beamer `.tex` stays as the printable PDF; keep the two in step or drop the PDF.

Reveal font gotcha (as in ese-ai): `ese.scss` re-sets `--r-main-font` in the rules
section with quoted names, because Quarto interpolates the SCSS variable unquoted
and `Source Sans 3` unquoted is invalid CSS.

## Weekly loop

Thursday lesson → Friday: drill solutions and homework online (`make deploy`)
→ Wednesday 23:59 homework due on Moodle → next Thursday first 15' walkthrough.

## Moodle

Site: <https://esestudents.com> (**no `www`** — the other host answers
`requirecorrectaccess`). Moodle 4.5.10. This course is **id 2546**
(`MBA003_262701_FL`); the AI course is 2531.

Access is through `mcp-moodle-teacher` (own server,
<https://github.com/NiccoloSalvini/mcp-moodle-teacher>), wired in `.mcp.json`.
It reads enrolments, submissions, what is missing and the gradebook, and writes
a grade with feedback or a news-forum announcement. The published `moodle-mcp`
packages are student-side and were dropped.

Token: `.env` (gitignored, mode 600), obtained with
`MOODLE_SITE=https://esestudents.com bash ~/dev/mcp-moodle-teacher/scripts/get-moodle-token.sh`.
Export it before launching Claude Code: `set -a; . .env; set +a`. *Preferences >
Security keys* is empty for this account — the lecturer role lacks
`moodle/webservice:createtoken`, which is why the script exists.

**Materials cannot be uploaded through the API**: Moodle core has no web service
that creates a module. The course page carries links to this site instead.
