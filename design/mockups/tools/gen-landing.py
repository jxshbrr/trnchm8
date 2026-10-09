# Generates LandingA/B/C.dc.html (Landing v2 directions) into design/mockups/.
import json, os, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
HELMET = open(os.path.join(os.path.dirname(__file__), 'landing-helmet.html')).read()
HELMET = HELMET.replace('</style>\n</helmet>', '''/* Landing v2 */
.lp-clip [style*="position: sticky"]{position:relative!important;top:auto!important}
.lp-shot{box-shadow:0 30px 80px var(--lp-shadow, rgba(0,0,0,.45)), 0 0 0 1px var(--lp-edge, rgba(255,255,255,.06))}
</style>
</helmet>''')
assert '/* Landing v2 */' in HELMET
ACCENTS = ["#7CD4FF", "#FFD23F", "#6495ED", "#B4A5FF", "#FF85C8", "#FF9152", "#FFB547"]

# Board sizes (hint sizes) for the imports.
BOARD = {
    'Main': (390, 3020), 'Desktop': (1440, 1820), 'Stats': (1440, 3100), 'Modal': (520, 900),
    'TgNudge': (390, 1640), 'TgRepeat': (390, 1180), 'TgRecap': (390, 1240), 'TgRuleAlert': (390, 1060),
    'TgMorning': (390, 900), 'TgAsk': (390, 1060), 'DcNudge': (390, 1053), 'DcRepeat': (390, 1052),
}
THEMED = {'Main', 'Desktop', 'Stats', 'Modal'}


def imp(name, extra=''):
    w, h = BOARD[name]
    th = ' theme="{{theme}}"' if name in THEMED else ''
    lay = ' layout="desktop"' if name == 'Stats' else ''
    return f'<dc-import name="{name}"{th}{lay} accent="{{{{accent}}}}"{extra} hint-size="{w}px,{h}px"></dc-import>'


def clip(name, x, y, w, h, z, radius=24, extra='', shadow=True, bg='#0D0E13'):
    """Shows the region (x, y, w, h) of a board, scaled by z, in a rounded frame."""
    bw, _ = BOARD[name]
    W, H = round(w * z), round(h * z)
    cls = ' class="lp-clip lp-shot"' if shadow else ' class="lp-clip"'
    return (f'<div{cls} style="width: {W}px; height: {H}px; flex-shrink: 0; overflow: hidden; border-radius: {radius}px; background: {bg}">'
            f'<div style="zoom: {z}; width: {w}px; height: {h}px; overflow: hidden">'
            f'<div style="margin-left: -{x}px; margin-top: -{y}px; width: {bw}px">{imp(name, extra)}</div></div></div>')


def phone(name, y, h, z, x=0, w=390):
    """A board region in a phone bezel."""
    inner = clip(name, x, y, w, h, z, radius=34, shadow=False)
    return (f'<div class="lp-shot" style="flex-shrink: 0; padding: 9px; border-radius: 43px; background: #08090C; '
            f'box-shadow: inset 0 0 0 1px rgba(255,255,255,0.09)">{inner}</div>')


GLYPH = lambda s, r=None: (f'<svg width="{s}" height="{s}" viewBox="0 0 36 36" aria-hidden="true" style="flex-shrink: 0"><rect x="0" y="0" width="36" height="36" rx="{r if r is not None else 12}" fill="{{{{accent}}}}"></rect>'
                           '<rect x="11" y="12" width="4.5" height="9" rx="2.25" fill="{{onAccent}}"></rect><rect x="20.5" y="12" width="4.5" height="9" rx="2.25" fill="{{onAccent}}"></rect></svg>')
TG = '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" style="flex-shrink: 0"><circle cx="12" cy="12" r="12" fill="#2AABEE"></circle><path d="M5.6 11.7l10.9-4.2c.5-.2 1 .1.8.9l-1.9 8.8c-.1.6-.5.8-1 .5l-2.8-2.1-1.4 1.3c-.2.2-.3.3-.6.3l.2-2.9 5.3-4.8c.2-.2 0-.3-.3-.1l-6.6 4.1-2.8-.9c-.6-.2-.6-.6.2-.9z" fill="#FFFFFF"></path></svg>'
DC = '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" style="flex-shrink: 0"><circle cx="12" cy="12" r="12" fill="#5865F2"></circle><path d="M16.9 8.1a9.6 9.6 0 0 0-2.4-.8l-.3.6a8.9 8.9 0 0 0-2.4-.1 8.9 8.9 0 0 0-1.4.1l-.3-.6a9.6 9.6 0 0 0-2.4.8C6.2 10.4 5.8 12.6 6 14.8a9.7 9.7 0 0 0 2.9 1.5l.6-1c-.3-.1-.7-.3-1-.5l.2-.2a6.9 6.9 0 0 0 6.6 0l.2.2c-.3.2-.7.4-1 .5l.6 1a9.6 9.6 0 0 0 2.9-1.5c.2-2.5-.4-4.7-2.1-6.7zM10 13.6c-.6 0-1-.5-1-1.1s.4-1.1 1-1.1 1 .5 1 1.1-.4 1.1-1 1.1zm4 0c-.6 0-1-.5-1-1.1s.4-1.1 1-1.1 1 .5 1 1.1-.4 1.1-1 1.1z" fill="#FFFFFF"></path></svg>'


def ctas(price=True, align='flex-start'):
    btn = 'height: 56px; padding: 0 24px 0 16px; box-sizing: border-box; border-radius: 999px; display: flex; align-items: center; gap: 10px; font-size: 16px; font-weight: 800; text-decoration: none; white-space: nowrap'
    p = '<span style="font-size: 14px; font-weight: 600; color: {{c.text3}}">Free for 7 days. Then $20 / 30 days in USDC.</span>' if price else ''
    return f'''<div style="display: flex; flex-direction: column; align-items: {align}; gap: 14px">
        <div style="display: flex; gap: 10px">
          <a class="tm-press" href="https://t.me/" onClick="{{{{startTg}}}}" data-tip="Opens M8 in Telegram" data-tip-pos="bottom" style="{btn}; background: {{{{accent}}}}; color: {{{{onAccent}}}}">{TG}Start on Telegram</a>
          <a class="tm-press" href="https://discord.com/" onClick="{{{{startDc}}}}" data-tip="Adds the M8 app on Discord" data-tip-pos="bottom" style="{btn}; background: {{{{c.surface}}}}; color: {{{{c.text}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}">{DC}Start on Discord</a>
        </div>
        {p}
      </div>'''


def nav():
    link = 'min-height: 44px; padding: 0 14px; display: flex; align-items: center; font-size: 14px; font-weight: 700; color: {{c.text2}}; text-decoration: none'
    return f'''<header style="width: 1200px; max-width: 100%; height: 72px; display: flex; align-items: center; justify-content: space-between">
    <a class="tm-hover" href="#top" style="display: flex; align-items: center; gap: 10px; color: {{{{c.text}}}}; text-decoration: none">{GLYPH(32)}<span style="font-size: 18px; font-weight: 800; letter-spacing: -0.01em">TrenchM8</span></a>
    <nav aria-label="Main" style="display: flex; align-items: center; gap: 2px">
      <a class="tm-hover" href="#how" style="{link}">How it works</a>
      <a class="tm-hover" href="#pricing" style="{link}">Pricing</a>
      <a class="tm-hover" href="#faq" style="{link}">FAQ</a>
      <a class="tm-press" href="#login" style="margin-left: 10px; height: 40px; padding: 0 16px; border-radius: 999px; display: flex; align-items: center; font-size: 14px; font-weight: 800; color: {{{{c.text}}}}; text-decoration: none; box-shadow: inset 0 0 0 1px {{{{c.line}}}}">Log in</a>
    </nav>
  </header>'''


def footer():
    return '''<footer style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: 32px 0 48px 0; display: flex; align-items: center; justify-content: space-between; gap: 24px; font-size: 13px; font-weight: 600; color: {{c.text3}}; border-top: 1px solid {{c.line}}">
    <span>Not financial advice. M8 never makes calls.</span>
    <div style="display: flex; gap: 20px"><a class="tm-hover" href="#terms" style="color: {{c.text3}}; text-decoration: none">Terms</a><a class="tm-hover" href="#privacy" style="color: {{c.text3}}; text-decoration: none">Privacy</a></div>
  </footer>'''


SCRIPT = '''class Component extends DCLogic {
  renderVals() {
    const theme = this.props.theme ?? 'dark';
    const accent = this.props.accent ?? '#7CD4FF';
    const themes = {
      dark: { bg: '#0D0E13', surface: '#171922', surface2: '#21242F', line: '#2C303D', text: '#F3F4F7', text2: '#A9AEBE', text3: '#858B9E', gain: '#3FD98E', loss: '#FF6B6B', lossSoft: 'rgba(255,107,107,0.14)', gainSoft: 'rgba(63,217,142,0.12)', tipBg: '#F3F4F7', tipFg: '#12131A', shadow: 'rgba(0,0,0,0.5)', edge: 'rgba(255,255,255,0.06)' },
      light: { bg: '#F4F4F7', surface: '#FFFFFF', surface2: '#EEEFF3', line: '#E3E5EB', text: '#12131A', text2: '#4F5566', text3: '#666C7E', gain: '#0B8A51', loss: '#D23434', lossSoft: 'rgba(210,52,52,0.10)', gainSoft: 'rgba(11,138,81,0.10)', tipBg: '#12131A', tipFg: '#F3F4F7', shadow: 'rgba(18,19,26,0.18)', edge: 'rgba(18,19,26,0.08)' }
    };
    const c = themes[theme] || themes.dark;
    // The mock stays in place; in production these open Telegram and Discord.
    const stop = (e) => { if (e && e.preventDefault) e.preventDefault(); };
    return Object.assign({ theme, accent, c, onAccent: '#15140E', startTg: stop, startDc: stop }, EXTRA);
  }
}'''


def page(name, title, height, body, extra='{}'):
    props = {"theme": {"editor": "enum", "options": ["dark", "light"], "default": "dark", "section": "Look"},
             "accent": {"editor": "color", "default": "#7CD4FF", "options": ACCENTS, "section": "Look"},
             "$preview": {"width": 1440, "height": height}}
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="--tm-tip-bg: {{{{c.tipBg}}}}; --tm-tip-fg: {{{{c.tipFg}}}}; --tm-focus: {{{{accent}}}}; --lp-shadow: {{{{c.shadow}}}}; --lp-edge: {{{{c.edge}}}}; width: 100%; box-sizing: border-box; background: {{{{c.bg}}}}; color: {{{{c.text}}}}; font-family: Manrope, system-ui, sans-serif; font-variant-numeric: tabular-nums; -webkit-font-smoothing: antialiased; display: flex; flex-direction: column; align-items: center; overflow: hidden">
  {nav()}
{body}
  {footer()}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, separators=(",", ":"))}'>
{SCRIPT.replace("EXTRA", extra)}
</script>
</body>
</html>
'''
    open(OUT + name + '.dc.html', 'w').write(html)


H2 = 'margin: 0; font-size: 48px; line-height: 1.06; font-weight: 800; letter-spacing: -0.035em'
P = 'margin: 0; font-size: 18px; line-height: 1.55; font-weight: 500; color: {{c.text2}}'

# ---------------------------------------------------------------- A: the loop, live
def step(time, title, body, ui, ui_align='flex-start'):
    return f'''    <div style="display: grid; grid-template-columns: 300px minmax(0, 1fr); gap: 56px">
      <div style="display: flex; flex-direction: column; gap: 10px; padding: 6px 0 0 28px; border-left: 2px solid {{{{c.line}}}}">
        <span style="font-size: 15px; font-weight: 800; color: {{{{accent}}}}">{time}</span>
        <span style="font-size: 26px; line-height: 1.15; font-weight: 800; letter-spacing: -0.02em">{title}</span>
        <span style="font-size: 16px; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">{body}</span>
      </div>
      <div style="display: flex; gap: 24px; align-items: flex-start; justify-content: {ui_align}">{ui}</div>
    </div>'''


def landing_a():
    hero = f'''  <section id="top" style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: minmax(0, 1fr) 470px; gap: 40px; align-items: center; padding: 40px 0 72px 0">
    <div class="tm-in" style="display: flex; flex-direction: column; gap: 28px">
      <h1 style="margin: 0; font-size: 64px; line-height: 1.02; font-weight: 800; letter-spacing: -0.045em">You trade.<br>M8 writes the journal.</h1>
      <p style="{P}; font-size: 20px; max-width: 540px">M8 watches your wallets, texts you two hours after your last trade, and turns your reply into your journal.</p>
      {ctas()}
    </div>
    <div style="position: relative; height: 660px">
      <div style="position: absolute; right: 0; top: 0">{phone('TgNudge', 0, 760, 0.78)}</div>
      <div style="position: absolute; left: 0; bottom: 0">{clip('Main', 12, 548, 366, 350, 0.95, radius=26)}</div>
    </div>
  </section>'''
    steps = '\n'.join([
        step('9:02 AM', 'You trade like normal.', 'Any bot, any DEX. Paste a wallet once: Solana, Base, BNB or Robinhood Chain. Read-only, nothing to sign.',
             clip('Desktop', 24, 905, 990, 910, 0.8, radius=22)),
        step('1:58 PM', 'M8 spots a repeat, live.', 'Same move as Sep 18, with the receipts. One heads-up per session, then it stays out of your way.',
             clip('TgRepeat', 0, 64, 390, 356, 1.1, radius=24) + clip('Modal', 0, 0, 520, 500, 0.86, radius=24, extra=' layout="dialog" modal="{{chase}}" max-h="900px"', bg='transparent')),
        step('4:22 PM', 'Two hours after your last trade, M8 texts.', 'On Telegram or Discord. Reply the way you would text a friend. Voice notes work.',
             '<div style="display: flex; flex-direction: column; gap: 10px">' + clip('TgNudge', 0, 64, 390, 268, 1.1) + '<span style="font-size: 13px; font-weight: 700; color: {{c.text3}}">Telegram</span></div>'
             + '<div style="display: flex; flex-direction: column; gap: 10px">' + clip('DcNudge', 0, 56, 390, 268, 1.1, bg='#313338') + '<span style="font-size: 13px; font-weight: 700; color: {{c.text3}}">Discord</span></div>'),
        step('4:31 PM', 'Your journal, in your words.', 'Written from a 7 second voice note. Every trade tagged, plus M8&#39;s take on the pattern.',
             clip('Desktop', 0, 0, 1440, 900, 0.6, radius=22)),
        step('Sunday, 6 PM', 'The week, in one card.', 'Biggest mistake, what worked, one change for next week. Share it, or make the change a rule.',
             clip('TgRecap', 10, 108, 330, 404, 1.3, radius=24)),
    ])
    timeline = f'''  <section id="how" style="width: 1200px; max-width: 100%; display: flex; flex-direction: column; gap: 72px; padding: 96px 0 40px 0">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 760px">
      <h2 style="{H2}">One Wednesday, start to finish.</h2>
      <p style="{P}">A sample day, Oct 7. Every screen below is the product.</p>
    </div>
{steps}
  </section>'''
    edge = f'''  <section style="width: 1200px; max-width: 100%; display: flex; flex-direction: column; gap: 36px; padding: 120px 0 40px 0">
    <div style="display: flex; flex-direction: column; gap: 14px; max-width: 760px">
      <h2 style="{H2}">Your edge, and your leak.</h2>
      <p style="{P}">M8 reads every trade and tells you where you make money and where it goes. Each claim links to the trades behind it.</p>
    </div>
    {clip('Stats', 0, 1006, 1440, 394, 0.833, radius=24)}
  </section>'''
    price = f'''  <section id="pricing" style="width: 1200px; max-width: 100%; padding: 120px 0 96px 0">
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 440px; gap: 64px; align-items: center; padding: 56px; border-radius: 32px; background: {{{{c.surface}}}}">
      <div style="display: flex; flex-direction: column; gap: 22px">
        <h2 style="{H2}">Free for 7 days.</h2>
        <p style="{P}; max-width: 520px">Everything on: tracking, check-ins, your journal, stats and rule alerts. Then pay in USDC on Solana. No auto-renew; M8 reminds you before it ends.</p>
        {ctas(price=False)}
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px">
        <div style="padding: 24px; border-radius: 24px; background: {{{{c.surface2}}}}; display: flex; flex-direction: column; gap: 6px">
          <span style="font-size: 40px; font-weight: 800; letter-spacing: -0.03em">$20</span>
          <span style="font-size: 15px; font-weight: 700; color: {{{{c.text2}}}}">30 days</span>
        </div>
        <div style="padding: 24px; border-radius: 24px; background: {{{{c.surface2}}}}; box-shadow: inset 0 0 0 2px {{{{accent}}}}; display: flex; flex-direction: column; gap: 6px">
          <span style="font-size: 40px; font-weight: 800; letter-spacing: -0.03em">$50</span>
          <span style="font-size: 15px; font-weight: 700; color: {{{{c.text2}}}}">90 days, about $16.67 a month</span>
        </div>
      </div>
    </div>
  </section>'''
    page('LandingA', 'TrenchM8 - landing v2, A: the loop, live', 5000, '\n'.join([hero, timeline, edge, price]),
         extra="{ chase: { kind: 'receipts', pattern: 'chase' } }")


# ---------------------------------------------------------------- B: chat-first
def m8(text, size=22, extra=''):
    return f'''    <div style="display: flex; gap: 16px; align-items: flex-start; width: 760px">
      {GLYPH(40, 20)}
      <div style="flex-grow: 1; min-width: 0; display: flex; flex-direction: column; gap: 14px; padding-top: 6px">
        <span style="font-size: {size}px; line-height: 1.45; font-weight: 600">{text}</span>{extra}
      </div>
    </div>'''


def you(text):
    return f'''    <div style="width: 1200px; display: flex; justify-content: flex-end">
      <span style="max-width: 460px; padding: 14px 20px; border-radius: 24px 24px 6px 24px; background: {{{{c.surface2}}}}; font-size: 20px; line-height: 1.4; font-weight: 600">{text}</span>
    </div>'''


def divider(t):
    return f'''    <div style="width: 1200px; display: flex; justify-content: center"><span style="padding: 6px 14px; border-radius: 999px; background: {{{{c.surface}}}}; font-size: 13px; font-weight: 700; color: {{{{c.text3}}}}">{t}</span></div>'''


def breakout(inner, gap=24, align='flex-start'):
    return f'''    <div style="width: 1200px; display: flex; gap: {gap}px; align-items: {align}; padding-left: 56px; box-sizing: border-box">{inner}</div>'''


def landing_b():
    bars = ''.join(f'<span style="width: 3px; height: {h}px; border-radius: 2px; background: {{{{c.text2}}}}"></span>' for h in [8, 14, 22, 12, 26, 18, 30, 20, 12, 24, 16, 28, 14, 8, 18, 24, 12, 20, 10, 16, 8, 12, 6, 10])
    voice = f'''    <div style="width: 1200px; display: flex; flex-direction: column; align-items: flex-end; gap: 8px">
      <div style="display: flex; align-items: center; gap: 14px; padding: 12px 20px 12px 12px; border-radius: 24px 24px 6px 24px; background: {{{{c.surface2}}}}">
        <span style="width: 40px; height: 40px; border-radius: 20px; background: {{{{accent}}}}; display: flex; align-items: center; justify-content: center"><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4l13 8-13 8z" fill="{{{{onAccent}}}}"></path></svg></span>
        <span style="display: flex; align-items: center; gap: 3px">{bars}</span>
        <span style="font-size: 15px; font-weight: 700; color: {{{{c.text2}}}}">0:07</span>
      </div>
      <span style="max-width: 460px; font-size: 15px; line-height: 1.5; font-weight: 500; font-style: italic; color: {{{{c.text3}}}}; text-align: right">"i chased them, they were pumping and i didn't want to miss out"</span>
    </div>'''
    cap = lambda t: f'<span style="font-size: 13px; font-weight: 700; color: {{{{c.text3}}}}">{t}</span>'
    col = lambda inner, t: f'<div style="display: flex; flex-direction: column; justify-content: space-between; gap: 10px">{inner}{cap(t)}</div>'
    hero = f'''  <section id="top" style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: minmax(0, 1fr) 360px; gap: 64px; align-items: center; padding: 40px 0 64px 0">
    <div class="tm-in" style="display: flex; flex-direction: column; gap: 28px">
      <div style="display: flex; align-items: center; gap: 12px">{GLYPH(48, 24)}<span style="font-size: 16px; font-weight: 800">M8</span><span style="font-size: 14px; font-weight: 600; color: {{{{c.text3}}}}">now</span></div>
      <h1 style="margin: 0; font-size: 72px; line-height: 1.0; font-weight: 800; letter-spacing: -0.045em">gm. I'm M8,<br>your trading journal.</h1>
      <p style="{P}; font-size: 22px; color: {{{{c.text}}}}; max-width: 620px">I watch your wallets. Two hours after you stop trading, I text you. You reply, I write it up.</p>
      {ctas()}
    </div>
    {phone('Main', 0, 760, 0.86)}
  </section>'''
    thread = '\n'.join([
        divider('Wednesday, Oct 7'),
        you('ok how does it work'),
        m8('You trade like normal. When you go quiet for 2 hours, I text you on Telegram or Discord. Same message, your pick:'),
        breakout(col(clip('TgNudge', 0, 64, 390, 186, 1.36), 'Telegram') + col(clip('DcNudge', 0, 52, 390, 186, 1.36, bg='#313338'), 'Discord'), align='stretch'),
        voice,
        m8('Done. Here&#39;s your Wednesday, written from that voice note:'),
        breakout(clip('Desktop', 0, 0, 1440, 900, 0.76, radius=22)),
        you('be honest, do i have an edge'),
        m8('Yes. Coins under 1 hour old made you +$2,910 this month. Everything older cost you $1,626. Receipts:'),
        breakout(clip('Stats', 0, 1006, 1440, 394, 0.76, radius=22)),
        you('what if i&#39;m about to do something dumb'),
        m8('I say so once, while you&#39;re still in it. Like Wednesday at 1:58 PM:'),
        breakout(clip('TgRepeat', 0, 64, 390, 356, 1.1) + clip('Modal', 0, 0, 520, 500, 0.86, extra=' layout="dialog" modal="{{chase}}" max-h="900px"', bg='transparent')),
        you('is this a signal group'),
        m8('No. I don&#39;t make calls. Ask me about a coin and you get facts, not a verdict. I&#39;m here for how you trade.'),
        you('how much'),
        m8('7 days free with everything on. Then $20 for 30 days, or $50 for 90, in USDC on Solana. No auto-renew. I&#39;ll remind you.', extra='\n        ' + ctas(price=False)),
    ])
    body = f'''{hero}
  <section id="how" style="width: 1200px; max-width: 100%; display: flex; flex-direction: column; gap: 40px; padding: 72px 0 120px 0">
{thread}
  </section>'''
    page('LandingB', 'TrenchM8 - landing v2, B: chat-first', 6000, body, extra="{ chase: { kind: 'receipts', pattern: 'chase' } }")


# ---------------------------------------------------------------- C: a trader's week
def landing_c():
    days = [('Mon', '5', '+$412', 'gain', '6 trades', 'Fresh launches before 11. Sold into strength.'),
            ('Tue', '6', '-$88', 'loss', '3 trades', 'Quiet one. All 3 planned.'),
            ('Wed', '7', '+$234', 'gain', '8 trades', 'Great morning, then two chases after lunch.'),
            ('Thu', '8', '+$318', 'gain', '5 trades', 'No new entries after 1 PM. Kept it.'),
            ('Fri', '9', '-$156', 'loss', '5 trades', 'Hit the $150 limit and stopped.'),
            ('Sat', '10', '+$96', 'gain', '4 trades', 'Small and clean.'),
            ('Sun', '11', 'Recap', 'text', 'Rest day', 'Up $816 on the week.')]
    cells = '\n'.join(f'''      <a class="tm-lift" href="#{d.lower()}" style="padding: 18px 16px; border-radius: 22px; background: {{{{c.surface}}}}; color: {{{{c.text}}}}; text-decoration: none; display: flex; flex-direction: column; gap: 10px{'; box-shadow: inset 0 0 0 2px {{accent}}' if d in ('Wed',) else ''}">
        <span style="display: flex; justify-content: space-between; font-size: 13px; font-weight: 800; color: {{{{c.text3}}}}"><span>{d} {n}</span><span>{t}</span></span>
        <span style="font-size: 28px; font-weight: 800; letter-spacing: -0.03em; color: {{{{c.{k}}}}}">{v}</span>
        <span style="font-size: 14px; line-height: 1.45; font-weight: 600; color: {{{{c.text2}}}}">{s}</span>
      </a>''' for d, n, v, k, t, s in days)
    hero = f'''  <section id="top" style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: minmax(0, 1fr) 470px; gap: 48px; align-items: center; padding: 40px 0 56px 0">
    <div class="tm-in" style="display: flex; flex-direction: column; gap: 28px">
      <h1 style="margin: 0; font-size: 72px; line-height: 1.0; font-weight: 800; letter-spacing: -0.045em">A week in<br>the trenches.</h1>
      <p style="{P}; font-size: 20px; max-width: 560px">You trade. M8 texts you after, you reply, and it writes the journal. Here is one sample week.</p>
      {ctas()}
    </div>
    <div style="display: flex; justify-content: flex-end">{clip('TgRecap', 10, 108, 330, 404, 1.3, radius=26)}</div>
  </section>
  <section style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 10px; padding-bottom: 40px">
{cells}
  </section>'''
    wed = f'''  <section id="wed" style="width: 1200px; max-width: 100%; display: flex; flex-direction: column; gap: 40px; padding: 120px 0 0 0">
    <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
      <div style="display: flex; flex-direction: column; gap: 6px">
        <span style="font-size: 18px; font-weight: 800; color: {{{{c.text3}}}}">Wednesday, Oct 7</span>
        <h2 style="margin: 0; font-size: 120px; line-height: 0.92; font-weight: 800; letter-spacing: -0.055em; color: {{{{c.gain}}}}">+$234</h2>
      </div>
      <p style="{P}; max-width: 420px; padding-bottom: 10px">8 trades. A great morning, then $375 handed back on two coins after lunch. M8 texted at 4:22 PM.</p>
    </div>
    {clip('Desktop', 0, 0, 1440, 900, 0.833, radius=24)}
    <div style="display: grid; grid-template-columns: minmax(0, 1fr) 430px; gap: 64px; align-items: center; padding-top: 24px">
      <div style="display: flex; flex-direction: column; gap: 20px">
        <span style="font-size: 44px; line-height: 1.15; font-weight: 800; letter-spacing: -0.03em">"Still green, but it was a $647 day before the chase."</span>
        <span style="font-size: 16px; font-weight: 600; color: {{{{c.text3}}}}">Your journal, written by M8 from a 7 second voice note.</span>
      </div>
      {clip('TgNudge', 0, 64, 390, 268, 1.1)}
    </div>
  </section>'''
    thu = f'''  <section id="thu" style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: 420px minmax(0, 1fr); gap: 96px; align-items: center; padding: 160px 0 0 0">
    {phone('TgMorning', 0, 740, 1.0)}
    <div style="display: flex; flex-direction: column; gap: 24px">
      <span style="font-size: 18px; font-weight: 800; color: {{{{c.text3}}}}">Thursday, 8:00 AM</span>
      <h2 style="{H2}; font-size: 56px">gm. Yesterday, in one line.</h2>
      <p style="{P}; max-width: 520px">The morning brief: what moved overnight on your chains, and the one thing to remember from yesterday. You replied "no trades after 1 today". M8 asked if that should be a rule.</p>
      <div style="display: flex; align-items: baseline; gap: 14px; padding-top: 8px">
        <span style="font-size: 56px; font-weight: 800; letter-spacing: -0.04em; color: {{{{c.gain}}}}">+$318</span>
        <span style="font-size: 16px; font-weight: 700; color: {{{{c.text2}}}}">and nothing after 1 PM.</span>
      </div>
    </div>
  </section>'''
    fri = f'''  <section id="fri" style="width: 1200px; max-width: 100%; display: grid; grid-template-columns: minmax(0, 1fr) 470px; gap: 72px; align-items: center; padding: 160px 0 0 0">
    <div style="display: flex; flex-direction: column; gap: 24px">
      <span style="font-size: 18px; font-weight: 800; color: {{{{c.text3}}}}">Friday, 2:41 PM</span>
      <h2 style="margin: 0; font-size: 120px; line-height: 0.92; font-weight: 800; letter-spacing: -0.055em; color: {{{{c.loss}}}}">-$156</h2>
      <h3 style="margin: 0; font-size: 34px; line-height: 1.15; font-weight: 800; letter-spacing: -0.02em; max-width: 560px">A red day that still counts as a good one.</h3>
      <p style="{P}; max-width: 540px">You set a $150 daily stop. You hit it and logged off. M8 calls that a rule kept, and it shows up in your week.</p>
    </div>
    {clip('TgRuleAlert', 0, 608, 390, 300, 1.2, radius=24)}
  </section>'''
    close = f'''  <section id="pricing" style="width: 1200px; max-width: 100%; display: flex; flex-direction: column; gap: 32px; padding: 180px 0 120px 0">
    <h2 style="margin: 0; font-size: 76px; line-height: 1.0; font-weight: 800; letter-spacing: -0.05em">Your week, written for you.</h2>
    <p style="{P}; font-size: 20px; max-width: 640px">7 days free with everything on. Then $20 for 30 days, or $50 for 90, in USDC on Solana. No auto-renew.</p>
    {ctas(price=False)}
  </section>'''
    page('LandingC', 'TrenchM8 - landing v2, C: a trader&#39;s week', 5200, '\n'.join([hero, wed, thu, fri, close]))


landing_a(); landing_b(); landing_c()
print('ok')
