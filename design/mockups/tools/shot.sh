#!/bin/bash
# Static preview of a .dc.html (no runtime: renderVals once, sc-if/sc-for/{{}} expanded, dc-import rendered inline from its own file).
# usage: [ROOTW=390] shot.sh File.dc.html outname width height [propsJSON|null] [stateJSON|null]
# ROOTW fixes the root width (use for 390 mobile; Chrome headless can't go below ~500 wide). Prints H=<content height>.
cd "$(dirname "$0")"
P=..  # design/mockups
python3 build.py "$P/$1" "$2.html" "${5:-null}" "${6:-null}"
CH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
W=$3; [ -n "$ROOTW" ] && [ "$W" -lt 520 ] && W=520
"$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=3000 --window-size=$W,$4 --dump-dom "file://$PWD/$2.html" 2>/dev/null | grep -o '<title>[^<]*'
"$CH" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --virtual-time-budget=3000 --window-size=$W,$4 --screenshot="$PWD/$2.png" "file://$PWD/$2.html" 2>/dev/null >/dev/null
echo "$PWD/$2.png"
