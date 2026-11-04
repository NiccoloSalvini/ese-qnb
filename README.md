# MBA03 Research & Quantitative Business Methods — weeks 1–5

European School of Economics, Florence · Term 1 AY 2026/27 · Weeks 1–5: Niccolò Salvini · weeks 6–10: Vincenzo Nardelli · Module leader: Arianna Ziliotto

Course site: <https://niccolosalvini.github.io/ese-qnb/>, built from this repository with Quarto.

Five Thursday sessions (24 Sep → 22 Oct 2026) covering the revision of algebra, calculus and financial mathematics that the midterm report and the final exam are built on. Each session is half slides, half laboratory: the deck sets the question and the technique, the Colab notebook shows it move, paper drills make it stick. One running case throughout: Arno Bikes, an e-bike assembler in Florence.

## Layout

```
index.qmd               home page: schedule, assessment scheme, readings
setup.qmd               "How to work": what to bring, homework, notebooks, exam-style writing
_quarto.yml             site config; every rendered file is listed explicitly
styles.scss, _fonts.html, images/   ESE brand (red #AF1F25, gold #CDBA80, Source Sans 3)
week-01/ … week-05/     one folder per session
  notes.md              tutor's plan (not rendered)
  drills.md             in-class exercises in exam format, worked solutions folded at the bottom
  homework.md           drill set + memo to the Board, corrected together at the next session
  session.ipynb         Colab notebook: projector demos (plotly sliders), then every drill solved in Python
                        with an assert on the published answer; linked as "code ↗", optional, not examined
  build_notebook.py     regenerates session.ipynb
  diagnostic.md         (week 1) 20-minute anonymous placement test with key (not rendered)
  slides/               (week 1) beamer deck (metropolis) and its PDF, the printable version
  revision.md           (week 4) revision set on weeks 1–4, for the reading week
  mock_exam.md          (week 5) mock of the final exam's calculus question
reading-week/
  mock_exam.md          the full mock: weeks 1–5 in one sitting
midterm/
  briefing.md           how to read the brief and write the report (week 2) — method only
  oral.md               how to prepare the oral
lectures/
  NN-slug.qmd           the deck shown in class: Quarto revealjs, ESE theme, clips embedded
  _metadata.yml, ese.scss   every visual option of the decks
  figs.py, figs_wNN_*.py    matplotlib scripts writing the SVG figures in img/
  apps/function-lab.html    interactive function plot, embedded in the week-1 deck
  media/                clips (mp4) and their poster frames, copied from anim/
anim/
  src/weekNN_scenes.py  manim scenes for the week's clips; common.py holds the palette and the Arno Bikes functions
  render.sh             renders the clips into out/ and a poster frame of each into frames/
Makefile                preview, build, deploy
```

## Weekly cycle

Thursday 10:00–13:00 lesson → by Friday: deck, drill solutions and homework on the site → next Thursday, the first 15–20 minutes go through the homework at the board. Homework is done on paper and is formative: nothing is handed in or graded. Homework 5, with no session after it, went by email. The midterm paper is the only deliverable of weeks 1–5, on Turnitin.

## Building

- Site: `make preview` while editing; `make build` renders to `_site/`; `make deploy` renders locally and publishes `_site/` to the `gh-pages` branch. There is no CI. Execution is off, so notebooks are shown with the outputs they were saved with.
- Notebooks: `python3 week-NN/build_notebook.py` (needs `nbformat`), then `jupyter nbconvert --to notebook --execute --inplace week-NN/session.ipynb`. The final cells re-check every drill's published answer.
- Clips: `bash anim/render.sh [weekNN]` (manim and ffmpeg; set `MANIM=` to point at your manim) renders at 720p30. Copy the mp4 and the frame into `lectures/media/`, the frame as `<clip>_poster.png`.
- Figures: `python3 lectures/figs.py`, and each `figs_wNN_*.py`, writes its SVGs into `lectures/img/`.
- Week-1 PDF: `cd week-01/slides && latexmk -pdf week01.tex` (TeX Live with beamer, metropolis, pgfplots).

Every worked solution is checked with sympy before it is published.

Official ESE documents (syllabus, assessment briefs, exam papers) and grading are not in this repository. Drills and mocks use the exam's form with different functions and numbers.
