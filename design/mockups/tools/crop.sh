#!/bin/bash
# usage: crop.sh img.png outprefix width chunkHeight totalHeight  -> outprefix-N.png chunks (no PIL needed)
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
I=$1; O=$2; W=$3; C=$4; T=$5; n=0; y=0
while [ $y -lt $T ]; do
  echo "<html><body style=\"margin:0;overflow:hidden\"><img src=\"$I\" style=\"display:block;margin-top:-${y}px\"></body></html>" > "$O-c.html"
  "$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=$W,$C --screenshot="$PWD/$O-$n.png" "file://$PWD/$O-c.html" 2>/dev/null >/dev/null
  n=$((n+1)); y=$((y+C))
done
echo $n chunks
