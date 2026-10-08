# Token audit

Every value in the web mockups that sits off the scale in `tokens.json`, with where it's used and the token it should snap to.
Counts come from grepping `design/mockups/*.dc.html` on 2026-10-08.
Unless noted, they cover the 13 web boards: Main, Desktop, Stats, Settings, M8Chat, M8History, Modal, JournalShare, StatesBoard, Skeleton, ProtoMobile, ProtoDesktop and Landing.
Only the M8-rendered images in the Tg*/Dc* boards were checked.

The rule throughout: snap near-duplicates to an existing step instead of minting a token for every value.
New tokens were added only where a value carries a distinct meaning: data palettes, the switch track, skeleton and accent ink.

## Summary

Measured against the final `tokens.json`, so values that became new tokens (avatar, chain, skeleton, switch track) count as on-scale.

| Area | Distinct values | On the scale | Off the scale | Off-scale uses / all uses |
|---|---|---|---|---|
| Hex colors | 66 | 46 | 20 (16 are third-party chrome) | 25 / 715 |
| rgba colors | 45 | 16 | 29 | 84 / 196 |
| Font sizes | 24 | 15 | 9 | 44 / 749 |
| Line heights | 12 | 6 | 6 | 61 / 146 |
| Letter spacing (em) | 10 | 4 | 6 | 18 / 59 |
| Border radius (single value) | 26 | 7 | 19 | 268 / 736 |
| Spacing (padding, margin, gap) | 32 | 19 | 13 | 177 / 1366 |
| Control heights (not switches) | 13 | 6 | 7 | 18 / 197 |
| Icon sizes | 20 | 6 | 14 | 52 / 157 |
| Icon stroke widths | 9 | 2 | 7 | 68 / 133 |
| z-index | 9 | 8 | 1 | 2 / 31 |

Shadows and timings are listed value by value below instead of counted.

The most common radius values look off-scale, but most of them are half of a square's size (18px on a 36px button, 22px on 44px).
Those become `radius.full`, so the real component radii collapse to 7 steps.

## Top 10 findings

1. **The accent text color `#15140E` is hardcoded 142 times** across 11 boards.
   It's correct everywhere, but it should be `color.accent.<name>.on`.
   That way a future accent with dark text, or a light-theme change, is a one-line edit.
2. **Every board redefines the whole theme object.**
   14 copies of the dark and light palettes exist, plus per-board extras: `gainBg`, `gainRgb`, `tipBg`, `pop`, `offTrack`, `well`, `edge`, `glass`.
   They agree on the core 10 colors but drift on the extras (findings 6 and 7).
   Phase 1 replaces all of them with generated CSS variables.
3. **The focus ring ignores the accent and the theme.**
   `--tm-focus` is never set on any board, so it always falls back to Sky `#7CD4FF`.
   On the light theme that's 1.5:1 against `#F4F4F7`, which fails the 3:1 minimum for non-text contrast.
   Snap to `color.accent.<name>.base` on dark and `color.accent.<name>.ink` on light.
   `ink` is a new token, darkened to 4.5:1 or better.
4. **Accent as foreground fails on the light theme.**
   Typing dots (M8Chat x2) and spinner arcs (Modal x4, Settings x1) use `{{accent}}` on light surfaces.
   Sky reaches 1.65:1 on white, Citrus 1.44:1, Apricot 1.76:1.
   Snap to `accent.*.ink` on the light theme.
5. **The warning color is the Apricot accent.**
   `warn` (dark) is `#FFB547`, the same hex as the Apricot accent.
   Its 14 uses span Main, Desktop, Stats, Settings, M8Chat, Modal, JournalShare, StatesBoard, Landing and ModalBoard; 10 of those are accent swatch lists, and warn itself appears in Modal and StatesBoard.
   With Apricot picked, the "Delayed" sync pill, the trial banner and the daily-limit bar look like brand chrome.
   **Decided (2026-10-08):** keep all 7 accents and shift warn: dark `#FFE07A` (pale butter) on `warn-soft`, light `#A86400`; warn is never a solid fill.
6. **Gain and loss tints have four different alphas.**
   - Main and Desktop use 0.14 (dark) and 0.10 (light).
   - StatesBoard uses 0.12 for light gain.
   - Stats uses 0.16.
   - Modal uses 0.08, 0.22 and 0.30.
   Snap tags and chips to `gain-soft` / `loss-soft`.
   Heatmaps keep a computed alpha ramp, which is a data-viz rule in DESIGN.md, not a token.
7. **The popover background differs.**
   Stats uses `#1D2029` (one-off); Settings uses `#21242F` (surface-2).
   Snap both to `color.*.popover`.
8. **Chat bubbles have four different radii and paddings.**
   | Board | Radius | Tail | Padding |
   |---|---|---|---|
   | M8Chat | 22 | 6 | 11/15 |
   | Main | 20 | 6 | 12/14 |
   | Desktop | 18 | 6 | 10/13 |
   | Landing | 16 | 4 | 9/12 |
   Snap to `radius.lg` (20) with an `xs` (6) tail and `space.12 space.16` padding.
   Who gets a bubble also differs; see the inconsistencies section.
9. **Switches come in three sizes.**
   Settings is 52x32, Modal 46x28 and JournalShare 44x26.
   Snap to `size.control.switch-w/h` (52x32).
10. **Spacing has 177 off-scale values.**
    The 3 biggest buckets:
    - 22px (41): StatesBoard and Landing card padding. Snap to 24.
    - 3px (37): chip padding like `3px 8px` and tiny gaps. Snap to 4 (padding) or 2 (gaps).
    - 18px (36): button padding `0 18px` and gaps. Snap to 20 for padding, 16 for gaps.
    Mixed bubble paddings (11, 13, 15) snap to 12 and 16.

## Colors

### Hex values off the palette

| Value | Uses | Boards | Snap to |
|---|---|---|---|
| `#15140E` | 142 | 11 web boards | `accent.*.on` (on-scale value, hardcoded) |
| `#FFFFFF` | 43 | 13 | `light.surface`, `on-status` (light), `brand.on-brand` |
| `#8FD3FF` `#9EE6C1` `#C3A6FF` `#FFE08A` `#A5B4FC` `#FFB86B` `#FF9EC4` | 6 each | Main, Desktop, Modal | `data.avatar.1-7` (new) |
| `#F9A8A8` | 9 | Main, Desktop, Modal | `data.avatar.8` (new) |
| `#FFD3A8` | 1 | Modal ($BIRB avatar) | `data.avatar.6` |
| `#9B6BFF` `#B8E62E` `#3D7BFF` `#F0B90B` | 2 each | Stats | `data.chain.solana/robinhood/base/bnb` (new) |
| `#2AABEE` `#5865F2` | 5, 7 | Settings, Landing | `brand.telegram`, `brand.discord` |
| `#A86400` | 3 | Modal, StatesBoard | `light.warn` (on-scale, see finding 5) |
| `#1B1D27` `#272A36` `#EFF0F4` | 2 each | StatesBoard, Skeleton | `skeleton.base/shine` (new) |
| `#3A3E4C` `#C9CCD6` | 1 each | Settings (switch off) | `control.track-off` (new) |
| `#1D2029` | 1 | Stats (popover) | `dark.popover` = surface-2 |
| `#111219` `#EBECF1` | 1 each | M8History (column bg) | `bg`, with a `line` border to separate the column |
| `#585E70` | 1 | TgRecap, DcRecap image (zero-line tick) | `dark.text-3` |
| Telegram and Discord chrome: `#10161F` `#1C2733` `#2A4A6B` `#E9EEF3` `#8A98A8` `#C9D3DD` `#313338` `#2B2D31` `#3F4147` `#4E5058` `#80848E` `#949BA4` `#B5BAC1` `#DBDEE1` `#F2F3F5` `#F0B232` | 20 | Landing hero chat mocks | Exempt. These illustrate other apps' UI and live in one `third-party-chrome.ts` file with a lint exemption. |

### rgba values off the palette

| Value | Uses | Boards | Snap to |
|---|---|---|---|
| `rgba(5,6,9,0.55)` | 2 | ProtoDesktop (drawer), StatesBoard | `scrim` (0.6) |
| `rgba(124,212,255,.22)` (tm-flash default) | 14 | every helmet | Sky is hardcoded. Use the accent at 22% (`color-mix`) so the new-row flash follows the user's accent. |
| `rgba(255,107,107,0.5)` | 1 | M8Chat (recording dot pulse) | `danger` (recording isn't money) |
| `rgba(255,255,255,0.35)`, `rgba(21,20,14,0.25)` | 1 each | Modal, StatesBoard (spinner track on a filled button) | The fill's `on` color at 30% via `color-mix`. One rule, no new token. |
| Stats heat alphas `.16 .28 .75 .76` | 6 | Stats | Data-viz ramp from `gain` / `loss` (DESIGN.md) |
| Modal `lossRgb .08 .22 .30`, `gainRgb .30` | 4 | Modal (receipts, trade detail) | `loss-soft` for fills, `line` for borders |
| StatesBoard light `gainSoft .12`, Stats `.16` | 3 | StatesBoard, Stats | `gain-soft` / `loss-soft` |
| `rgba(255,255,255,0.09)` | 2 | Landing (Telegram inline buttons) | Exempt (third-party chrome) |
| Shadow alphas `.25 .4 .45 .5` | 7 | Modal, StatesBoard, Settings, Stats, ProtoDesktop | `shadow.*` levels |

## Typography

### Font sizes

| Size | Uses | Where | Snap to |
|---|---|---|---|
| 10px | 4 | Main, Desktop, JournalShare, Landing (w700-800 tags) | `micro` 11 |
| 10.5px | 1 | Modal | `micro` 11 |
| 17px | 16 | 13 w800 headers (Main, Desktop, Stats, Settings, Modal, M8Chat), 2 w500 Landing | `title-3` 18; the w500 ones go to `body` 16 |
| 19px | 1 | Landing hero subcopy | `title-3` size with body weight, or `body-lg` 18 |
| 20px | 13 | Section and card titles (Stats, Desktop, Main, Landing, Modal) | `title-2` 22 |
| 24px | 1 | Desktop rest-day title | `title-2` 22 |
| 26px | 5 | Stats KPI values | `title-1` 28 |
| 30px | 1 | Modal checkout amount | `number-lg` 32 |
| 34px | 2 | Settings plan days, Modal rule value | `number-lg` 32 |
| 48px | 1 | StatesBoard hero demo | `hero-mobile` 52 |

On the scale: 11, 12, 13, 14, 15, 16, 18, 22, 28, 32, 40, 52, 56, plus the marketing sizes (72/44 for h1, 44/30 for h2).
13px is fine; it's the second most used size (166).

### Line height, letter spacing, weight

- Line heights 1.02 (Landing h1) and 1.15 / 1.2 / 1.25 (Stats, Desktop, Modal: 9 uses) snap to `none` (1) and `tight` (1.1).
- 1.4 (11 uses) snaps to `normal` (1.45), and 1.5 (40 uses) to `relaxed` (1.55).
- Letter spacing -0.025em (8, Landing) and -0.035em (1, Landing h1) snap to `tighter` (-0.03em).
- .04em, .08em and .02em (6 uses on uppercase labels and badges) snap to `wide` (.06em) or `normal`.
- Weights are clean: only 500, 600, 700 and 800 are used.

## Radius

207 of the single-value radii are circles or fully round ends: the radius is exactly half the element's width or height (6px on 12px skeleton bars, 22px on 44px icon buttons).
All of those become `radius.full`, or `pill` for bars and buttons.
The rest are real component shapes:

| Value | Uses (non-circle) | Snap to |
|---|---|---|
| 2px, 3px, 4px, 5px, 7px | 29 | `xs` 6 |
| 6px | 4 | `xs` (on-scale) |
| 8px, 9px, 11px, 12px, 13px | 24 | `sm` 10 |
| 10px | 25 | `sm` (on-scale) |
| 14px | 19 | `md` 16 |
| 16px | 52 | `md` (on-scale) |
| 18px, 22px | 63 | `lg` 20 |
| 20px | 13 | `lg` (on-scale) |
| 24px | 49 | `xl` (on-scale) |
| 28px | 36 | `2xl` (on-scale) |
| 36px | 1 | `2xl` 28 (Landing) |
| 999px | 188 | `pill` |
| Bubble shapes `22 22 6 22`, `20 20 20 6`, `18 18 18 6`, `16 16 16 4` | 11 | `lg` with an `xs` tail corner |

## Spacing

Total: 1366 px values in padding, margin and gap; 177 are off the scale.

| Value | Uses | Main boards | Snap to |
|---|---|---|---|
| 22px | 41 | StatesBoard 23, Landing 14 | 24 |
| 3px | 37 | Main, Settings, Modal, Stats, ProtoMobile | 4 for padding, 2 for gaps |
| 18px | 36 | Desktop, Modal, StatesBoard, Landing, Settings | 20 for padding, 16 for gaps |
| 1px | 19 | Stats 10 (heatmap grid) | `space.hairline` (allowed) |
| 5px | 10 | Modal, Landing | 4 or 6 |
| 9px | 8 | Landing, Desktop | 8 or 10 |
| 11px, 15px | 11 | M8Chat bubbles | 12, 16 |
| 13px | 5 | Desktop bubbles | 14 |
| 7px | 3 | Modal, Landing | 6 or 8 |
| 52px, 44px, 30px, 26px | 7 | Main, Settings, Desktop, StatesBoard | 48 / 56, 40 / 48, 32, 24 |

## Shadows

| Value | Uses | Snap to |
|---|---|---|
| `0 1px 3px rgba(0,0,0,.25)` | 1 (Modal switch knob) | `shadow.1` |
| `0 8px 24px rgba(0,0,0,.28)` | 14 (tooltip, every helmet) | `shadow.2` |
| `0 12px 32px` glass (.35 dark, .10 light) | 3 | `shadow.3` |
| `0 16px 40px` (.35 toast, .45 popover dark, .16 light) | 6 | `shadow.3` |
| `0 20px 48px rgba(0,0,0,.45)` | 1 (Stats popover) | `shadow.3` |
| `0 24px 48px rgba(0,0,0,.4)` | 1 (StatesBoard) | `shadow.4` |
| `0 24px 64px rgba(0,0,0,.5)` | 2 (ProtoDesktop dialog) | `shadow.4` |
| `-24px 0 48px rgba(0,0,0,.35)` | 1 (drawer) | `shadow.drawer` |
| `0 -12px 24px {{bg}}` | 1 (ProtoMobile tab bar fade) | Not a shadow: a `bg` fade above the tab bar. Make it a gradient in the TabBar component. |

## Controls and icons

- **Button and input heights:**
  - 26px and 28px (4 uses, not switches) snap to `xs` 32.
  - 34px and 38px (9) snap to `sm` 36 or `md` 40.
  - 50px and 52px (6: Modal input, JournalShare and Settings buttons) snap to `xl` 48.
  - 64px (1: the Main voice button) snaps to `2xl` 56.
- **Icon sizes:**
  - 13 (6) to 14, 15 (4) to 16, 17 (3) to 18, 19 (1) to 20.
  - 22 (3) and 26 (9, the Telegram/Discord marks on the Landing CTAs) go to 24.
  - 28, 32, 34 and 36 are M8 glyphs and avatars: `size.glyph`.
- **Icon strokes:**
  - 2, 2.4 and 2.5 (34 uses) snap to `stroke` 2.2.
  - 2.8, 3 and 3.4 (14) snap to `stroke-bold` 2.6.
  - 1 (5) is chart gridlines, which are exempt.

## z-index and motion

- **z-index:** 31 (Settings, 2 uses) snaps to `popover` 30.
- **Durations:**
  - .18s (Settings switch) snaps to `hover` 150.
  - .2s (Stats chevron) and .24s (the skeleton's fade-out) snap to `exit` 220.
  - .22s dialog-in and the tm-out fade-out are `exit` 220; .28s drawer snaps to `ui` 300.
  - .5s and .6s bar fills snap to `load` 600.
  - 1.8s (Settings new-row ring) snaps to `pulse` 1600.
- **Easings:** clean. Only `cubic-bezier(.2,.8,.2,1)`, `ease`, `ease-in-out` and `linear` are used.
