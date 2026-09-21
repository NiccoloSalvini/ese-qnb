# MBA03 Research & Quantitative Business Methods — weeks 1–5

European School of Economics, Florence · Term 1 AY 2026/27 · Tutor for weeks 1–5: Niccolò Salvini · Module leader: Arianna Ziliotto

Five Thursday sessions (24 Sep → 22 Oct 2026) covering the revision of algebra, calculus and financial mathematics that the midterm report and the final exam are built on. Each session is half slides, half laboratory: the deck sets the question and the technique, the Colab notebook shows it move, paper drills make it stick.

## Layout

```
week-01/ … week-05/     one folder per session
  notes.md              tutor's plan and script (timings, questions, bets, closing sentences)
  slides/weekNN.tex     beamer deck (metropolis); LAB frames cue the notebook, PAPER frames cue the drills
  slides/weekNN.pdf     compiled deck
  session.ipynb         Colab notebook driven from the projector (plotly sliders, LaTeX cells, sympy checks)
  build_notebook.py     regenerates session.ipynb (python build_notebook.py)
  drills.md             in-class exercises in exam format with worked solutions
  homework.md           weekly homework: drill set + memo to the Board
  diagnostic.md         (week 1) 20-minute anonymous placement test with key
anim/
  src/weekNN_scenes.py  manim scenes for the week's clips
  out/*.mp4             rendered clips (720p) played in class
  frames/*.png          key frames embedded in the slides as stepped overlays
midterm/                briefing (week 2), grading grid, handover to the second half
```

## Weekly cycle

Thursday 10:00–13:00 lesson → Friday: drill solutions and homework on Moodle → Wednesday 23:59 homework due → next Thursday, first 15 minutes are the walkthrough.

## Building

- Slides: `cd week-NN/slides && latexmk -pdf weekNN.tex` (TeX Live with beamer, metropolis, pgfplots). The ▶ link on each clip frame opens the mp4 in `anim/out/`.
- Clips: from `anim/`, `manim -qh src/week01_scenes.py RevenueRectangle -o w01_parabola.mp4` (needs a LaTeX install with `dvisvgm`); then `cp media/videos/**/1080p60/*.mp4 out/`.
- Notebook: open `session.ipynb` in Colab; the setup cell installs nothing Colab does not already have.

Official ESE documents (syllabus, assessment briefs, exam papers) are not in this repository.
