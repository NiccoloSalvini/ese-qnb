#!/usr/bin/env bash
# Render every clip at 720p30, copy the mp4 into out/ and a poster frame into frames/.
#   bash render.sh            all weeks
#   bash render.sh week02     one week
set -euo pipefail
cd "$(dirname "$0")"
# Override on another machine: MANIM=~/.venvs/ese-manim/bin/manim MEDIA_DIR=~/.cache/ese-qnb-manim bash render.sh week07
MANIM="${MANIM:-$HOME/.venvs/sbd-animations/bin/manim}"
MEDIA_DIR="${MEDIA_DIR:-/Users/niccolo/.cache/ese-qnb-manim}"
MEDIA="$MEDIA_DIR/videos"
PY="$(dirname "$MANIM")/python"   # the venv's python: PyAV and Pillow come with manim

render () {  # render <module> <Scene> <output-name>
  PYTHONPATH=src "$MANIM" -qm --disable_caching --media_dir "$MEDIA_DIR" "src/$1.py" "$2" -o "$3.mp4" >/dev/null 2>&1
  cp "$MEDIA/$1/720p30/$3.mp4" "out/$3.mp4"
  # poster: three quarters in, when the picture is finished rather than half-drawn
  # (PyAV rather than ffmpeg/ffprobe, so a broken ffmpeg binary does not matter)
  dur=$("$PY" - "out/$3.mp4" "frames/$3.png" <<'PYEOF'
import sys, av
src, dst = sys.argv[1:]
with av.open(src) as c:
    s = c.streams.video[0]
    dur = c.duration / av.time_base
    at = dur * 0.78
    c.seek(int(at / av.time_base), backward=True, any_frame=False)
    for f in c.decode(s):
        if float(f.pts * s.time_base) >= at:
            f.to_image().save(dst); break
print(f"{dur:.2f}")
PYEOF
)
  printf '%-22s %5.1fs  %s\n' "$3" "$dur" "$(du -h "out/$3.mp4" | cut -f1)"
}

want="${1:-all}"
[ "$want" = all ] || [ "$want" = week02 ] && {
  render week02_scenes SecantToTangent w02_secant
  render week02_scenes TangentSlides   w02_tangent
  render week02_scenes AverageCostFalls w02_avgcost
}
[ "$want" = all ] || [ "$want" = week03 ] && {
  render week03_scenes RiemannFills   w03_riemann
  render week03_scenes StudyAFunction w03_study
}
[ "$want" = all ] || [ "$want" = week04 ] && {
  render week04_scenes CompoundingToE w04_compounding
  render week04_scenes NpvCrossesZero w04_npv
}
[ "$want" = all ] || [ "$want" = week05 ] && {
  render week05_scenes DurationIsTheTangent w05_duration
  render week05_scenes ConvexityIsTheGap    w05_convexity
}
[ "$want" = all ] || [ "$want" = week07 ] && {
  render week07_scenes PoissonArrivals w07_poisson
  render week07_scenes NormalAreaFills w07_normal
  render week07_scenes ChoicesTree     w06_choices
  render week07_scenes OneFamily       w07_family
  render week07_spread MeanAndSpread   w06_spread
}
echo "done"
