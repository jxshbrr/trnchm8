# TrenchM8 design rules

These are the rules every UI change follows, for people and for agents.
`tokens.json` holds the values, `components.md` lists the components, and `mockups/` is the visual reference.
If a change needs something these rules don't cover, change the rules (and the tokens) first, then build.

## 1. Principles

- A consumer app, not a terminal: calm, friendly, confident (Fomo + Phantom).
- Dark first, light fully supported. Both themes are complete token sets, never an afterthought.
- One hero number per journal screen, and numbers always in tabular figures.
- Every action answers within 100ms. Anything slower shows a skeleton, a named step or progress.
- Celebrate process, never PnL. No confetti, no "great day" for a green day.
- Undo instead of confirm for anything reversible. Dialogs only for what Undo can't fix.
- Each screen offers at most one primary action.

## 2. Tokens

- `design/tokens.json` (W3C DTCG) is the single source of truth.
  Code never contains a raw color, pixel size, radius, shadow, duration, easing or z-index.
- Use semantic tokens (`bg`, `surface`, `text-2`, `gain`, `danger`), never theme-specific ones (`color.dark.bg`) in components.
- Use only the scale steps: `space.*`, `radius.*`, `typography.*`, `size.control.*`, `size.icon.*`, `zIndex.*`, `motion.*`.
  If a value doesn't fit, pick the nearest step.
  If it truly can't, add a token in a PR that says why.
- `space.hairline` (1px) is for heatmap grid gaps and dividers only.
- Circles use `radius.full`. Bars and buttons use `radius.pill`. Never write half the size in pixels.
- **Data colors** (`data.avatar.*`, `data.chain.*`) are for data marks only, never UI chrome.
- **Brand colors** (`brand.*`) are for Telegram and Discord marks only.
- **Exempt:** the Telegram and Discord chat mocks on the landing page, which illustrate other apps.
  They live in one `third-party-chrome.ts` file, the only file besides the generated tokens that the lint rules exempt.

## 3. Theming

- The theme is `data-theme="dark|light"` on `<html>` ("System" follows `prefers-color-scheme`).
- The accent is `data-accent="sky|citrus|cornflower|lilac|bubblegum|tangerine|apricot"`; the default is `sky`.
- Users pick from the 7 accents only. No custom hex, so contrast stays safe and no accent collides with PnL green or red.
- **Accent roles:**
  - `accent.base`: primary buttons, the selected tab or segment, the active week day, the M8 glyph, the usage meter, chart highlights.
  - `accent.on`: text and icons on an `accent.base` fill (all accents reach 6.2:1 or better).
  - `accent.ink`:
    - On the light theme: accent as foreground (focus ring, links, spinner arcs, typing dots, the selected card or option border, the usage meter fill), because `base` is too pale there.
    - Small accent fills that carry `accent.on` text (buttons, selected chips, the M8 glyph) keep `base` on both themes.
    - On the dark theme, `base` works as foreground.
- **Inverse surfaces** (toasts, tooltips) use `inverse.*`.
  Status icons inside them use the opposite theme's status color.
- **Images M8 sends** (charts, recap cards, the share card, the 30-day insight):
  - Always render in the dark theme with the user's accent, whatever the app theme.
  - The Discord embed stripe is `accent.base`.

## 4. Layout and navigation

- **Design frames:** 390 (mobile) and 1440 (desktop).
- **Breakpoints:**
  - `md` (768): sheets become dialogs, one column becomes two.
  - `lg` (1024): the bottom tab bar becomes the top bar.
- **Mobile:**
  - A 16px side gutter.
  - A floating pill tab bar: Journal · Stats · Settings, icon over label, 56px items, active item filled with the accent.
  - There is no M8 chat on the web; M8 lives in the chat app ([0017](../docs/decisions/0017-launch-scope.md)).
- **Desktop top bar:**
  - Logo, then the Journal · Stats · Settings tabs, then an "Open M8 in Telegram" link on the right.
  - Flat at the top of the page; once scrolled, a floating glass bar (`glass.*`, `blur.glass`, `radius.lg`, `shadow.3`, max 1400).
  - The nav never animates on tab switch.
- **No sidebar.** The journal picks days from the week strip under the date (and a calendar sheet on mobile).
- **Page widths:**
  - App pages max 1440 with 24px padding; the landing max is 1200.
  - Journal day: center column (min 560) plus the pinned M8 panel (380, sticky under the bar).
- Cards wrap with flex or `auto-fit` grids; nothing scrolls sideways at 390.

## 5. Type

- Manrope for all UI, weights 500, 600, 700 and 800.
  800 is for headings, numbers, buttons and nav; 500 for long text.
- Instrument Serif (`font.family.display`, weight 400, roman and italic) is for display headlines only: the landing page and recap or share card titles.
  Italic marks the promise in a headline ("texts you *after every session.*"). Never use it in app UI, numbers or buttons.
- Every root sets `font-variant-numeric: tabular-nums`.
- Use the 18 `typography.*` styles; don't set font-size, line-height or letter-spacing by hand.
- **Hero numbers** use `hero` (56) on desktop and `hero-mobile` (52) on mobile, one per screen.
- Never go below 11px (`micro`). `micro` is for UPPERCASE overlines with `wide` tracking.
- `marketing-*` styles are for the landing page only.
- Journal text is capped at 72ch.

## 6. Color

- **Money uses gain and loss only.** `gain` / `loss` (and their `-soft` tints) are only for PnL, money amounts and data derived from them (heatmaps, curves).
  - Errors, destructive actions, the recording dot and offline banners use `danger`, even though it has the same value today.
  - FOMO and Revenge tags use `loss-soft` because they mark money-losing behavior on a trade.
- **Warn** (`warn`) is for degraded but working states: delayed sync, trial ending, daily limit.
  - It is always text or an icon on `warn-soft`, with a label, never a solid fill, so it can't be mistaken for a warm accent (Citrus, Apricot, Tangerine).
- **Text hierarchy:**
  - `text` for primary.
  - `text-2` for secondary.
  - `text-3` for meta only, and never for anything the user must read to act.
- **Heatmaps and hour maps** tint with gain/loss at an alpha that scales with the absolute value: from 0.16 at the smallest to 0.76 at the largest.
  Text on tinted cells stays `text`.
- **Contrast targets:**
  - Body text 4.5:1, large text (24px+, or 18.66px+ bold) and UI parts 3:1.
  - Check both themes and all 7 accents in Storybook before merging.

## 7. Motion

Durations and easings come from `motion.*`; never write timings by hand.

| What | Duration | Easing | Detail |
|---|---|---|---|
| Press | `press` 120ms | standard | Scale to 0.97 |
| Hover | `hover` 150ms | standard | Brighten only (1.12 buttons, 1.18 links, 1.07 cards), never move |
| Toast in | `toast` 250ms | out | 12px rise, from 0.98 scale |
| Dialog in, anything leaving | `exit` 220ms | out | 8px rise |
| Sheets, drawers, chips, the top bar | `ui` 300ms | out | Sheet 24px, drawer 32px |
| New content, new trade rows | `enter` 350ms | out | 8px rise, then a 1.6s `tm-flash` highlight in the accent |
| Load-in, once per visit | `load` 600ms + `draw` 900ms | out | Cards fade up with an 80ms stagger, the hero counts up, the equity line draws |

- **Tab switches** are instant.
- **Loops:**
  - Shimmer and typing dots: `loop` 1200ms.
  - Spinner: `spin` 800ms.
  - Live dot and rule kept: `pulse` 1600ms.
- **Reduced motion:** everything becomes a 200ms fade.
  No count-up, line draw, shimmer, press scale, pulse, shake or waveform.

## 8. Loading and progress

- **First visit only:** a skeleton in the page's real layout (`skeleton.*`). Cached pages show instantly.
- **Buttons:**
  - Keep their width, show a spinner and say what they're doing ("Checking wallet…").
  - Lock against double presses.
  - Use `aria-disabled` with a guard, so focus stays.
- **M8 thinking:** show the running tool ("Reading your 142 trades…"), then stream the answer.
- **Wallet backfill:** show real counts and a step name, and say M8 will message you when it's done.
- **Sync indicator** next to the date: Live, Syncing, Delayed, Paused.
- **New trades** slide in at the top with a short highlight; numbers update in place.
- **Settings save themselves:** "Saving…" then "Saved" beside the field, announced with `aria-live="polite"`.

## 9. Toasts and Undo

- **Position:** bottom; above the tab bar on mobile, centered on desktop, beside the M8 drawer when it's open.
- **Behavior:**
  - One at a time, on `inverse.*` with `radius.lg` and `shadow.3`, in a `role="status"` region.
  - Shown for 3s, or 5s when carrying Undo.
- **Kinds:** success, info, error with Retry, and daily limit.
- **Undo** replaces confirm dialogs for rules, tags, journal edits and forgetting a memory.
  After an Undo, an info toast says what changed back.

## 10. Tooltips

- **Required on:**
  - Every icon-only control.
  - Every number that needs explaining: KPIs, chips, hour map cells, calendar days, the usage meter.
- **When they show:** on desktop hover and keyboard focus, after `tooltip-delay` (350ms); never on touch (`@media (hover: none)`).
- **Content:** a sentence, not a label repeat. Wrap at 240px for long text.
- **Styling:** `inverse.*`, `radius.sm`, `shadow.2`, `typography.caption`, `zIndex.tooltip`.

## 11. Modals, sheets and dialogs

- **One component:** a bottom sheet on mobile (max 780 tall), a centered dialog on desktop (width from `size.modal.*`, max 86vh).
  The body scrolls; the header and footer stay.
- **Closing and focus:**
  - Esc, the close button and tapping the scrim close the top layer.
  - Focus is trapped and returns to the trigger.
- **One modal at a time.** Order of layers: scrim, then modal, then toast, then takeover, then tooltip.
- **Used for:** trade detail, editing an entry, pattern receipts, the day calendar, the rule editor, checkout, linking an app, export, sharing a day, and confirms.
  Everything else happens in place with Undo.
- **Destructive actions:**
  - Removing a wallet asks first.
  - Deleting the account needs the word "delete" typed.
- **Keyboard (desktop):** Esc closes the top layer; M opens M8.

## 12. Empty and edge states

- **Covered states:**
  - Backfill in progress.
  - A day with no trades.
  - Trial ending.
  - Plan ended (read-only).
  - Offline.
  - M8 daily limit.
  - No search results.
  - A filter with nothing to show.
- **Structure:** each says what's going on, what still works, and offers at most one action.
- **Expired plan:** journal and stats stay readable forever; tracking and M8 show as paused, not broken.

## 13. Accessibility

- **Focus:** every interactive element shows a 2px focus ring (`accent.base` dark, `accent.ink` light) with a 2px offset on `:focus-visible`.
- **Touch targets:** at least 44x44 on mobile. 32-40px controls are for desktop, or for compact controls inside a 44px row.
- **Semantics:**
  - Real elements: `button`, `a`, `input`.
  - Roles where needed: `switch`, `radiogroup`, `tablist`, `menu`, `listbox`, `progressbar`, `dialog`.
  - Selected state via `aria-pressed`, `aria-checked`, `aria-selected` or `aria-current`.
- **Charts and maps** have a text alternative (`role="img"` + `aria-label` with the numbers).
- **Live changes** (toasts, saves, sync status, M8 streaming) are announced politely.
- **Color** is never the only signal: gain and loss also carry a + or - sign, and tags carry words.
- Respect `prefers-reduced-motion` (section 7).

## 14. Copy voice for UI text

- **Plain and short, second person:** "Your trial ends tomorrow", not "Trial expiration notice".
- **Specific numbers over adjectives:** "-$375 after lunch", "8 trades · 4W 4L".
- **Sentence case everywhere**, including buttons ("Make it a rule"). No exclamation marks.
- **Name the outcome:**
  - Buttons say the action ("Pay $50 in USDC", "Remove wallet"); avoid "Submit" and "OK".
  - Loading says what's happening ("Checking wallet…").
- **Errors** say what happened, that data is safe, and what happens next ("Couldn't reach Solana data. Retrying in 30s.").
- **Naming:** M8 is "M8", never "the AI" or "the bot". The journal is "your journal".
- **No em dashes;** use "-", ":" or a new sentence. Money is "$1,284" and "-$154" (sign before the dollar sign); percentages are "52%".
- **M8's own messages** follow the doctrine and the chosen voice (Trench friend, Calm coach, Blunt degen).
  UI chrome stays neutral in every voice.

## 15. Code setup (Phase 1)

- **Token pipeline:** `design/tokens.json` is built (Style Dictionary or a small script, run in `prebuild` and CI) into:
  - `tokens.css`:
    - CSS custom properties.
    - `:root[data-theme=dark]` and `[data-theme=light]` blocks for `color.*`.
    - `[data-accent=*]` blocks setting `--accent`, `--accent-on`, `--accent-ink`.
    - The motion keyframes and `tm-*` utility classes from the mockups' `motion.css`, rewritten to use the variables.
  - A Tailwind v4 `@theme` block mapping the variables to utilities:
    - `bg-surface`, `text-text-2`, `text-gain`, `rounded-lg`, `p-16`, `shadow-3`, `duration-ui`, `ease-out`, and so on.
    - The default Tailwind palette and spacing are cleared, so only token utilities exist.
  - `tokens.ts`: a typed export of resolved values for the server-side image renderer (satori/resvg for chart PNGs and recap cards) and for charts that need numbers.
- **Components:**
  - shadcn/ui primitives (Button, Dialog/Sheet, Tooltip, Switch, RadioGroup, Select, DropdownMenu, Toast via Sonner, Tabs), restyled only through tokens.
  - TrenchM8 components (`components.md`, section 4) built on top.
- **Storybook is the catalog:**
  - One story per variant and state in `components.md`.
  - A theme and accent toolbar, and a reduced-motion toggle.
  - Playwright takes screenshots of every story in dark and light (and a sample of accents) on each PR.
  - Any visual diff needs approval.
- **Lint guardrails** (fail CI):
  - No hex, rgb(a) or hsl colors in components or CSS outside the generated token files and `third-party-chrome.ts`.
  - No Tailwind arbitrary values (`p-[13px]`, `bg-[#...]`, `rounded-[18px]`).
  - No inline `style` with literal colors or sizes.
  - No `z-index` numbers outside the tokens.
- **Agent skill:** `.claude/skills/trenchm8-ui/SKILL.md` tells agents to:
  - Read this file and `components.md` before any UI work.
  - Reuse components before creating new ones.
  - Add a story for every new component or state.
  - Run the Storybook screenshot check before claiming done.
  - `CLAUDE.md` points to the skill.
- **Mockups stay the reference:** when the mockups and the code disagree, fix one of them in the same PR so they don't drift.
