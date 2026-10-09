# Mockups

The design canvas boards (`.dc.html`) for every screen, both bots and the landing page.
They mirror the published canvas: https://claude.ai/artifact/QmewGj69mk6Qr8uLsYED2V

- `canvas.json` holds the board layout and notes.
- `Proto*.dc.html` are the clickable prototypes; `StatesBoard` and `ModalBoard` are live references for states, motion and modals.
- `Dc*.dc.html` (Discord) are generated: edit `tools/build-dc.py`, then run `python3 tools/build-dc.py`.
- `tools/shot.sh` renders a static preview with headless Chrome: `ROOTW=390 tools/shot.sh Main.dc.html main 390 3000`.

When a board changes on the canvas, copy it back here in the same change.
