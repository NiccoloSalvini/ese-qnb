#!/usr/bin/env bash
# Render every clip at 720p30, copy the mp4 into out/ and a poster frame into frames/.
#   bash render.sh            all weeks
#   bash render.sh week02     one week
set -euo pipefail
cd "$(dirname "$0")"
MANIM="${MANIM:-$HOME/.venvs/sbd-animations/bin/manim}"
MEDIA=/Users/niccolo/.cache/ese-qnb-manim/videos

render () {  # render <module> <Scene> <output-name>
  PYTHONPATH=src "$MANIM" -qm --disable_caching "src/$1.py" "$2" -o "$3.mp4" >/dev/null 2>&1
  cp "$MEDIA/$1/720p30/$3.mp4" "out/$3.mp4"
  # poster: three quarters in, when the picture is finished rather than half-drawn
  dur=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "out/$3.mp4")
  ffmpeg -v error -y -ss "$(echo "$dur * 0.78" | bc -l)" -i "out/$3.mp4" -frames:v 1 "frames/$3.png"
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
echo "done"
