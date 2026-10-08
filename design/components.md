# Component inventory

Every UI component and pattern in `design/mockups`, in Storybook build order: primitives first, then product components, then page patterns.
Each entry lists its variants, the states it needs stories for, the boards that use it and the tokens it reads.
Token names are shortened: `surface-2` means `color.<theme>.surface-2`, `accent.base` means `color.accent.<name>.base`.

**State key:**
- D default, H hover, P pressed, F focus-visible, X disabled, L loading, E empty, R error.
- Sel means selected/current, Exp means expanded/open.

Every interactive component also gets a light-theme story and a reduced-motion story.

---

## 1. Foundations (Storybook "Tokens" pages, not components)

- **Color:**
  - Swatches for both themes, the 7 accents with `on` and `ink`, and the data palettes.
  - A contrast matrix for text on bg, surface and surface-2.
- **Type:** every `typography.*` style, tabular-number demo.
- **Space, radius, shadow, z-index:** visual scales.
- **Motion:** a live demo of each `motion.duration` with its easing, plus the reduced-motion swap.
- **Icons:** the line icon set at each `size.icon.*` with both strokes.
- **M8 glyph:** sm, md and lg on every accent; the rounded-square form (app, images) vs the circle avatar (Telegram, Discord).

## 2. Primitives

### Button
- **Variants:**
  - `primary`: accent.base fill, accent.on text.
  - `secondary`: surface-2 fill, text.
  - `ghost`: transparent, text-2.
  - `danger`: danger fill, on-status text.
  - `danger-ghost`: danger text.
  - `brand`: Telegram or Discord mark, used on the landing CTAs and the linked-app connect buttons.
- **Sizes:** `xs` 32, `sm` 36, `md` 40, `lg` 44, `xl` 48, `2xl` 56; full-width on mobile sheets and the landing.
- **Icon:** leading icon, trailing icon (external link), icon-only (see Icon button).
- **States:** D H P F X L.
  - Loading keeps the width, shows a spinner and swaps the label to the action in progress ("Checking wallet…").
  - The button locks against double presses while loading.
- **Boards:** all web boards.
- **Tokens:** `radius.pill`, `size.control.*`, `typography.body-sm` / `ui` / `label`, `motion.scale.press`, `motion.brightness.press-hover`, `duration.press`.

### Icon button
- **Variants:** `ghost` (header actions), `soft` (surface-2 circle), `on-inverse` (inside toasts).
- **Sizes:** 32, 36, 44 (default; 44 is the minimum on mobile).
- **States:** D H P F X, plus Sel for toggles like Expand / Collapse.
  - A tooltip is required (every icon-only control).
- **Boards:** M8Chat (back, history, expand, collapse, close), M8History, Modal (close, month arrows), Desktop (prev/next day), Main (calendar), JournalShare (close).
- **Tokens:** `radius.full`, `text-2`, `row-hover`.

### Link
- **Variants:**
  - Inline text link.
  - Receipts link: red "3rd chase" and "Same as Sep 18". These are links styled for meaning, not color for money, so they use `danger` / `text` and never `loss`.
  - External link with an icon.
- **States:** D H F.
- **Boards:** Main, Desktop, Modal, Stats, Landing.
- **Tokens:** `motion.brightness.link-hover`, `accent.ink` on light.

### Text field, Textarea, Search field
- **Variants:**
  - Single-line input (48).
  - Search with a leading icon (44, pill): M8History.
  - Textarea with a character counter: editEntry in Modal, the 280 counter in JournalShare text mode.
  - Composer: see M8 composer.
- **States:**
  - D H F X R.
  - Validating (inline spinner).
  - Valid (check).
  - Error: a shake (`tm-shake`) plus a message, e.g. the wallet address in Settings.
  - Over limit (counter turns `danger`).
- **Boards:** Settings (wallet add, Tell M8), Modal (rule value, editEntry, deleteAccount typed confirm), M8History, M8Chat, StatesBoard.
- **Tokens:** `surface`, `line`, accent focus border, `radius.md` or `pill`, `size.control.lg` / `xl`.

### Switch
- **One size:** 52x32 (`size.control.switch-*`).
- **States:** D (off, `control.track-off`), On (accent.base), H F X, plus Saving / Saved via the Field status.
- **Boards:** Settings (message toggles), JournalShare (show $ amounts, notes, lesson), Modal.
- **Tokens:** `shadow.1` on the knob, `duration.hover`.

### Segmented control (tabs-as-pills)
- **Variants:**
  - 2, 3 or 4 options.
  - Inside the glass bar (`glass.nav`) or on surface.
  - With icons: the Telegram / Discord toggle.
- **States:** D H P F Sel.
- **Rule:** the selected option is an `accent.base` fill with `accent.on` text, everywhere, including the Telegram / Discord toggle and the JournalShare toggles.
- **Boards:**
  - Stats (7D/30D/90D/All, `role=radiogroup`).
  - Settings (Theme: Dark/Light/System).
  - JournalShare (Image/Text, %/$).
  - Landing (Telegram/Discord hero toggle).
  - Desktop top bar tabs.
- **Tokens:** `radius.pill`, `surface-2` track, `size.control.sm`.
  - Selected fill is `accent.base` with `accent.on` text.
  - Stats, Settings and the week strip already do this; JournalShare and the Landing toggle use an inverted `text` fill instead and should switch.

### Radio card / option row
- **Variants:** plan picker (30 / 90 days), voice picker (Trench friend / Calm coach / Blunt degen with a sample line), rule type, export format.
- **States:** D H P F Sel X.
- **Boards:** Settings, Modal (rule, export, checkout).
- **Tokens:** `radius.md` / `lg`, Sel ring `accent.base`, `surface-2`.

### Checkbox
- **States:** D H F, checked, X.
- **Boards:** Modal (tags in trade detail, `role=checkbox`).

### Accent swatch picker
- 7 swatches with the name as the tooltip.
- **States:** D H F Sel.
- **Boards:** Settings (Appearance).
- **Tokens:** `color.accent.*.base`, `radius.full`, a Sel ring offset by `bg`.

### Select / dropdown (listbox)
- **Variants:** timezone, morning brief time.
- **States:** D H F Exp, option H / Sel.
- **Boards:** Settings (`role=listbox`).
- **Tokens:** `popover`, `shadow.3`, `zIndex.popover`.

### Menu / popover
- **Variants:** the chain filter (menuitemcheckbox + "All chains" menuitemradio) with chain dots.
- **States:** Exp, item H / F / checked.
- **Boards:** Stats.
- **Tokens:** `popover`, `shadow.3`, `data.chain.*`.

### Tooltip
- **Placement:** top (default), bottom, left, right; wrapped up to 240px.
- **Behavior:** shown on desktop hover and keyboard focus after a 350ms delay; never on touch.
- **Boards:** every web board (Stats has 22, Modal 18, Desktop 16).
- **Tokens:** `inverse.bg` / `fg`, `radius.sm`, `shadow.2`, `typography.caption`, `zIndex.tooltip`, `motion.duration.tooltip-delay`.

### Chip / Tag
- **Variants:**
  - `stat` chip (journal stat row: "6 planned trades").
  - Behavior `tag` on trades:
    - Neutral (Plan, Lucky): surface-2 fill with text-2.
    - Mistake (FOMO, Revenge, Late entry): loss-soft fill with text.
  - `rule` chip: shows a created rule, with a pop on create.
  - `context` chip in the M8 composer, removable.
  - `chain` chip (SOL / BASE with a dot).
  - `badge` (NEW, PRO, "Recommended").
- **States:** D, H/P when clickable, F, removable X.
- **Boards:** Main, Desktop, Modal, Stats, M8Chat, Settings, Landing.
- **Tokens:** `radius.pill`, `typography.label` / `micro`, `gain-soft` / `loss-soft`, `surface-2`.

### Avatar
- **Variants:** coin avatar (`data.avatar.1-8`, initials in accent.on), M8 glyph avatar, user initial, linked-app tile (`brand.*`).
- **Sizes:** 28, 32, 36, 40.
- **Boards:** Main, Desktop, Modal, M8Chat, Settings, Landing.

### Spinner and progress
- **Variants:**
  - Inline spinner (14-16px, in buttons and fields).
  - Large spinner (40px, checkout waiting).
  - Linear progress bar (wallet import, export, `role=progressbar`).
  - Usage meter (the "M8 today" mini bar).
- **States:** indeterminate, determinate with a count ("Importing 214 of 640 trades").
- **Boards:** Settings, Modal, StatesBoard, Desktop (usage meter).
- **Tokens:** spinner arc `accent.base` (dark) / `accent.ink` (light); the track is the fill's `on` color at 30%; `duration.spin`.

### Skeleton
- **Variants:** line, block, circle, chart; a full page skeleton for the Journal (mobile and desktop).
- **Boards:** Skeleton, StatesBoard, ProtoMobile, ProtoDesktop.
- **Tokens:** `skeleton.base` / `shine`, `radius.xs`, `duration.loop`; no shimmer under reduced motion.

### Status dot / Sync pill
- **Variants:** Live (gain dot with pulse), Syncing (accent spinner), Delayed (warn), Paused (text-3).
- **Boards:** StatesBoard only. It's missing from Main and Desktop, where the plan puts it next to the date.
- **Tokens:** `pulse`, `warn`, `text-3`, `duration.pulse`.

### Divider / separator
- **Variants:** hairline, a labeled separator ("Today · After-lunch losses" in M8Chat).
- **Tokens:** `line`, `typography.caption`.

## 3. Overlays and feedback

### Toast
- **Kinds:** success, info, error (with Retry), limit (daily M8 cap), and any kind with Undo.
- **Behavior:**
  - One at a time.
  - Bottom placement: above the tab bar on mobile, centered on desktop, beside the M8 drawer when it's open.
  - Shown for 3s, or 5s with Undo.
- **States:** entering, idle, Undo pressed (then the info toast "X is back to Y"), exiting.
- **Boards:** ProtoMobile, ProtoDesktop, StatesBoard.
- **Tokens:**
  - `inverse.*`, `radius.lg`, `shadow.3`, `size.control.xs` for Undo, `zIndex.toast`.
  - `duration.toast` and `toast-life` / `toast-life-undo`.
  - The icon disc uses the opposite theme's status color.

### Sheet (mobile) and Dialog (desktop)
- One `Modal` component with `layout=sheet|dialog`.
- **Kinds:**
  - trade, editEntry, receipts, calendar, rule.
  - confirm, deleteAccount, export, checkout, connect.
  - share (JournalShare).
- **Sizes:** dialog widths come from `size.modal.*`; sheet max height is 780.
- **Behavior:** a scrolling body with a sticky header and footer.
- **States:** opening, idle, busy (footer button loading), success (check pop), error, closing.
  - Esc and tapping the scrim close it.
  - Focus is trapped and returns to the trigger.
- **Boards:** Modal, ModalBoard, JournalShare, ProtoMobile, ProtoDesktop.
- **Tokens:** `surface`, `radius.2xl`, `shadow.4`, `scrim`, `zIndex.scrim` / `modal`, `motion.duration.ui` (sheet), `exit` (dialog in).

### Drawer
- The M8 drawer on desktop (440 wide), from the right.
- **Boards:** M8Drawer, ProtoDesktop.
- **Tokens:** `size.layout.drawer`, `shadow.drawer`, `scrim`, `motion.distance.drawer`.

### Confirm (destructive)
- **Variants:**
  - Simple confirm, e.g. "Stop tracking Main?" (remove wallet, log out everywhere).
  - Typed confirm: delete account needs the word "delete".
- **Boards:** Modal, StatesBoard.
- **Tokens:** `danger`, `on-status`.

### Success moment
- **Variants:** rule created (check pop + rule chip), rule kept (quiet pulse), payment confirmed (check pop + staggered lines).
- **Boards:** StatesBoard, Modal (checkout, connect), Settings.
- **Tokens:** `motion.duration.enter`, `stagger`; `tm-pop`; never confetti, never on PnL.

### Edge-state banner and empty state
- **Variants:**
  - Backfill in progress.
  - Rest day (no trades).
  - Trial ends tomorrow (top banner).
  - Plan ended (read-only).
  - Offline (top banner).
  - M8 daily limit.
  - Search no results (M8History).
  - Filter shows nothing (Stats).
- **Structure:** an icon, what's happening, what still works, and at most one action.
- **Boards:** StatesBoard, Main, Desktop, Stats, M8History.
- **Tokens:** `warn` for the trial and limit states, `danger` for offline, `text-3` for paused.

### Field status (autosave)
- "Saving…" then "Saved" beside a setting.
- **Boards:** Settings, StatesBoard.
- **Tokens:** `typography.caption`, `text-2`, `aria-live=polite`.

## 4. Product components

### Hero PnL
- The big number at the top of the journal day, with a count-up on first view and the day subtitle ("8 trades · 4W 4L").
- **Variants:** gain, loss, flat, rest day.
- **Sizes:** `hero-mobile` 52 / `hero` 56.
- **Boards:** Main, Desktop, StatesBoard.
- **Tokens:** `gain` / `loss`, `typography.hero*`, `motion.duration.draw`.

### Equity curve (mini line chart)
- Intraday cumulative PnL with a draw-in.
- **Variants:** gain or loss end, with a zero baseline.
- **Boards:** Main, Desktop, Skeleton.
- **Tokens:** `gain` / `loss` stroke, `line` baseline, `motion.duration.draw`.

### Week strip
- Mon-Sun days around the selected day, each with a PnL dot or amount.
- **States:** day D H P F Sel, today, rest day, future (X).
- **Boards:** Main, Desktop.
- **Tokens:** `radius.pill`, Sel = `accent.base` fill with `accent.on` text and dot, `gain` / `loss` dots, rest = `line` dot.

### Day navigation
- Prev/next arrows (desktop), the calendar button that opens the calendar sheet (mobile).
- **Boards:** Main, Desktop, Modal (calendar kind).

### Trade row
- Coin avatar, ticker, chain, time, hold time, size, PnL, tag chip, optional note, and the "Same as Sep 18" receipts link.
- **States:** D H P F, new (slides in with `tm-flash`), with note, repeat mistake.
- **Boards:** Main, Desktop, Modal (receipts lists).
- **Tokens:** `row-hover` / `row-press`, `radius.md`, `typography.body-sm` / `label`, `gain` / `loss`, `data.avatar.*`.

### Session group
- Trades grouped as "Morning · +$609" with a header.
- **Boards:** Main, Desktop.

### Stat chip row
- 3 chips on mobile, 4 on desktop, under the hero.
- **Boards:** Main, Desktop.

### Journal entry card ("My journal")
- First person, written by M8 from the reply.
- **Actions:** Edit (opens editEntry), Share, Ask M8.
- **States:** D, edited (with Undo), rest day, empty (reply still pending).
- **Boards:** Main, Desktop.
- **Tokens:** `typography.body` / `body-lg`, `size.layout.prose-max`.

### M8's take card
- M8's voice; cross-day patterns; receipts links and "Make it a rule".
- **Boards:** Main, Desktop.

### Conversation excerpt
- The nudge, the user's (voice) reply and M8's follow-up, shown on the journal day.
- **Boards:** Main, Desktop.
- **Tokens:** see M8 message and bubble.

### KPI card
- Net PnL, win rate, avg win / loss, max drawdown, profit factor.
- Each has a tooltip and an M8 one-liner.
- **States:** D H F, empty filter.
- **Boards:** Stats.
- **Tokens:** `typography.title-1` value, `caption` label, `radius.2xl`.

### Calendar heatmap
- Day cells showing $ and trade count, tinted by PnL.
- Tapping a cell opens that journal day.
- **Variants:** desktop (amount + count) and mobile (amount only); month or 4-week paging.
- **States:** cell D H F, rest, future, today.
- **Boards:** Stats, Modal (calendar kind).
- **Tokens:** gain/loss alpha ramp, `radius.xs`, `space.hairline` / 2-4 gaps.

### Hour map
- Weekday x hour grid of average PnL per trade, with a tooltip per cell.
- **Boards:** Stats.
- **Tokens:** gain/loss alpha ramp, `radius.xs`.

### Bar breakdowns
- Hold time bands and entry size bands (median return; size relative to the user's normal), "Where your edge is" bars, and M8's time-of-day bars in chat.
- **Boards:** Stats, M8Chat.
- **Tokens:** `gain` / `loss`, `surface-2` track, `radius.pill`.

### Discipline card
- Tilt and revenge counts with receipts (opens the receipts modal).
- **Boards:** Stats.

### Rules card
- Each rule with its adherence %, Edit, and "+ Add a rule".
- **States:** D, kept (pulse), broken, new (ring).
- **Boards:** Stats, Settings.

### Wallet row
- Label, address, chain, trade count, Remove.
- **States:** D H, importing (progress with a count), new (ring), validation error, limit reached (5).
- **Boards:** Settings.

### Plan card
- Days left (`number-lg`), progress ring/bar, plan picker, Pay in USDC, payment history.
- **States:** trial, active, ending soon, expired.
- **Boards:** Settings, Modal (checkout).

### Memory list ("What M8 remembers")
- Facts with Forget (Undo toast), plus "Tell M8 something".
- **Boards:** Settings.

### Linked apps
- Telegram and Discord tiles, primary-channel picker, Connect.
- **States:** connected, primary, waiting (spinner), connected success.
- **Boards:** Settings, Modal (connect).

### Usage meter ("M8 today")
- A percentage bar with a tooltip; resets at midnight.
- **States:** normal, near limit, at limit (warn).
- **Boards:** Desktop top bar, Settings, StatesBoard.

### M8 message and chat bubble
- **M8 message:** M8 glyph, channel label ("via Telegram"), text (`body`), and optional inline content:
  - A chart.
  - A journal edit card with Undo.
  - Receipts.
  - Buttons (one-tap suggestions).
- **User bubble:** text or a voice note (waveform, duration, transcript).
- **States:** sending, sent, thinking (typing dots + tool step "Reading your 142 trades…"), streaming, error with Retry.
- **Boards:** M8Chat, Main and Desktop (excerpt), Landing (hero mock).
- **Tokens:** `radius.lg` + `xs` tail, `surface-2`, `typography.body` / `body-sm`.
- Rule: only the user gets a bubble (`surface-2`, `lg` with an `xs` tail corner on the right). M8 writes full-width plain text, which leaves room for charts, cards and receipts. The Main and Desktop excerpts and the Landing hero mock follow the same rule.

### M8 composer
- Text input, context chip (removable, with Undo), send, voice record (waveform, cancel, stop), and "New topic".
- **States:** D F, typing, recording, sending, at daily limit (X with a reason).
- **Boards:** M8Chat.
- **Tokens:** `radius.pill`, `danger` for the recording dot (not `loss`), `tm-wave`.

### Suggested questions
- Three starter questions built from page data, shown on a fresh open.
- **Boards:** M8Chat (fresh), M8ChatFresh.

### Conversation list item
- Title, when, preview, meta (channel, edits).
- **States:** D H P F Sel (current, `background-image` fill).
- **Boards:** M8History.

### Share card (image)
- The branded day card M8 renders: PnL in % by default (toggle for $), trade notes, M8's lesson. Wallet addresses are never shown.
- **Variants:** image or text mode, % or $, notes on/off, lesson on/off.
- **Boards:** JournalShare, JournalShareText.
- **Tokens:** always dark theme (`color.dark.*`) plus the user's accent.

### Rendered images (sent by M8 in Telegram and Discord)
- **Variants:** week chart (Ask), Sunday recap card, 30-day insight.
- These render server-side from the same tokens, always dark, with the user's accent.
- The Discord embed stripe is `accent.base`.
- **Boards:** TgAsk, TgRecap, DcAsk, DcRecap, DcOnboarding, DcNudge, DcMorning.

## 5. Navigation and page patterns

### Mobile tab bar
- Journal · Stats · M8 · Settings: a floating pill bar, 56px items, the active item filled with the accent.
- It hides while M8 is full screen.
- **Boards:** Main, Stats, Settings, ProtoMobile.

### Desktop top bar
- Logo, the Journal · Stats · Settings tabs, the "M8 today" meter and "Talk to M8".
- Flat at the top; becomes the floating glass bar (1400 max, `radius.lg`, `glass.*`, `blur.glass`, `shadow.3`) once scrolled.
- The bar itself never animates on tab switch.
- **Boards:** Desktop, Stats, Settings, ProtoDesktop.

### Page shells
- **Journal day:**
  - Mobile: a single column.
  - Desktop: the center column (min 560) plus a pinned M8 panel (380, sticky at 92).
- **Stats:** a wrapping card grid (`auto-fit, minmax(320px, 1fr)`).
- **Settings:** sections in wrapping 2-column cards (`flex 1 1 380px`).
- **M8:**
  - Mobile: full screen.
  - Desktop: drawer (440), or expanded with the history column (320).
- **Boards:** Main, Desktop, Stats, Settings, M8Chat, M8Drawer, M8Expanded, M8History.

### First-visit load
- The skeleton in the real layout, then fade-out, then the content fades up with a stagger, the hero counts up and the curve draws.
- **Boards:** Skeleton, ProtoMobile, ProtoDesktop, StatesBoard.

### Landing sections
- Nav, hero (headline, Telegram/Discord CTA pair, channel toggle, chat mock + journal card), problem, how it works (3 steps), "What M8 notices", rhythm, recap card, trust, pricing, FAQ (`details`), final CTA, footer.
- **Boards:** Landing, LandingMobile.
- **Tokens:** `typography.marketing-*`, `size.layout.landing-max`, `size.control.2xl`.
- The Telegram and Discord chat mocks use third-party chrome colors from the exempt file.
