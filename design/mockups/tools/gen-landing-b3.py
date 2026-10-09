# Generates LandingB3.dc.html (Poke-style editorial landing on night paper, desktop + mobile) and its LandingB3Mobile wrapper.
# Reuses the phone, Telegram chrome and board clips from gen-landing-b2.py.
# Usage: python3 tools/gen-landing-b3.py [desktopHeight] [mobileHeight]
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location('b2', os.path.join(HERE, 'gen-landing-b2.py'))
b2 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(b2)
D, ACCENTS, R = b2.D, b2.ACCENTS, b2.R
GLYPH, TG_ICON, DC_ICON, ico, I_EXT = b2.GLYPH, b2.TG_ICON, b2.DC_ICON, b2.ico, b2.I_EXT

H_DESK = int(sys.argv[1]) if len(sys.argv) > 1 else 5600
H_MOB = int(sys.argv[2]) if len(sys.argv) > 2 else 8000
SERIF = "'Instrument Serif', Georgia, 'Times New Roman', serif"
FONTS = 'https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap'

# ------------------------------------------------------------------ helmet
GRAIN = ("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='220' height='220'>"
         "<filter id='n'><feTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='2' stitchTiles='stitch'/>"
         "<feColorMatrix type='saturate' values='0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")
base = open(D + 'tools/landing-helmet.html').read()
base = base.replace('family=Manrope:wght@400;500;600;700;800&amp;display=swap', FONTS.split('css2?')[1])
assert 'Instrument+Serif' in base
HELMET = base.replace('</style>\n</helmet>', f'''/* Landing B3: night paper */
.lp-clip [style*="position: sticky"]{{position:relative!important;top:auto!important}}
.lp-shot{{box-shadow:0 24px 60px var(--lp-shadow, rgba(0,0,0,.4)), 0 0 0 1px var(--lp-edge, rgba(255,255,255,.06))}}
.lp-paper{{position:relative}}
.lp-paper::after{{content:"";position:absolute;inset:0;pointer-events:none;z-index:100;background-image:url("{GRAIN}");background-size:220px 220px;opacity:var(--lp-grain,.06);mix-blend-mode:var(--lp-blend,overlay)}}
@keyframes lp-word{{from{{opacity:0;filter:blur(12px);transform:translateY(8px)}}to{{opacity:1;filter:none;transform:none}}}}
.lp-word{{display:inline-block;animation:lp-word .9s cubic-bezier(.2,.8,.2,1) both;animation-delay:var(--tm-d,0s)}}
.lp-serif{{font-family:{SERIF};font-weight:400;font-variant-numeric:normal}}
@media (prefers-reduced-motion:reduce){{.lp-word{{animation:tm-fade .2s ease both}}}}
</style>
</helmet>''')
assert '/* Landing B3' in HELMET


# ------------------------------------------------------------------ hero phone (static, cut by the fold)
def hero_phone():
    head = '''<span style="align-self: center; font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 999px; background: rgba(255,255,255,0.08); color: #C9D3DD">Wednesday, October 7</span>
            <span style="align-self: center; margin-top: 6px; font-size: 12px; color: #8A98A8; text-align: center; padding: 0 20px">Last trade closed 2:20 PM. No activity for 2h, so M8 checks in.</span>'''
    nudge = b2.tg_in('8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?', '4:22 PM', top=8)
    logged = b2.tg_group(b2.TG_JOURNAL, '4:28 PM', b2.tg_btns(f'Open today&#39;s journal {ico(I_EXT, 13, sw=2.4)}', cols=1), w=282)
    header = '''<div style="display: flex; align-items: center; gap: 10px; height: 54px; padding: 0 12px 0 4px; box-sizing: border-box; flex-shrink: 0; background: #17202B">
          <span style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; color: #7FC1FF"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"></path></svg></span>
          <div style="display: flex; flex-direction: column; flex-grow: 1; min-width: 0; line-height: 1.25">
            <span style="font-size: 16px; font-weight: 600">M8</span>
            <span style="font-size: 13px; color: #8A98A8">bot</span>
          </div>
          ''' + GLYPH(38, 19) + '''
        </div>'''
    screen = f'''<div style="height: 100%; display: flex; flex-direction: column; background: #10161F; color: #E9EEF3; font-family: {b2.TG_FONT}; font-size: 15px; line-height: 1.38">
        {b2.status_bar('#17202B', '#FFFFFF')}
        {header}
        <div style="display: flex; flex-direction: column; padding: 12px 8px 12px 8px">{head}{nudge}{b2.TG_VOICE}{logged}</div>
      </div>'''
    # The crop box leaves room for the bezel rings on the sides and top; the bottom is cut flat by the section's hairline.
    return f'''<div style="width: {{{{ph.cropW}}}}; height: {{{{ph.cropH}}}}; overflow: hidden; display: flex; justify-content: center; padding-top: 14px; box-sizing: border-box; flex-shrink: 0">
      <div style="zoom: {{{{ph.zoom}}}}; position: relative; width: 360px; height: 800px; flex-shrink: 0; border-radius: 52px; overflow: hidden; background: #000000; box-shadow: 0 0 0 11px #0D0D10, 0 0 0 13px #4A4A52, 0 0 0 13.5px rgba(255,255,255,0.08), 0 30px 80px {{{{ph.s1}}}}" role="img" aria-label="M8 texting you on Telegram after a session">
        {screen}
      </div>
    </div>'''


# ------------------------------------------------------------------ page pieces
BTN = b2.BTN


def ctas(center=True):
    return f'''<div style="display: flex; flex-direction: column; align-items: {{{{cta.{'calign' if center else 'align'}}}}}; gap: 14px; width: {{{{cta.wrapW}}}}">
        <div style="display: flex; flex-direction: {{{{cta.dir}}}}; gap: 10px; width: {{{{cta.wrapW}}}}">
          <a class="tm-press" href="https://t.me/" onClick="{{{{startTg}}}}" data-tip="Opens M8 in Telegram" data-tip-pos="bottom" style="{BTN}; background: {{{{accent}}}}; color: #15140E">{TG_ICON()}Start on Telegram</a>
          <a class="tm-press" href="https://discord.com/" onClick="{{{{startDc}}}}" data-tip="Adds the M8 app on Discord" data-tip-pos="bottom" style="{BTN}; background: {{{{c.surface}}}}; color: {{{{c.text}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}">{DC_ICON()}Start on Discord</a>
        </div>
        <span style="font-size: 14px; font-weight: 600; color: {{{{c.text3}}}}">Free for 7 days. Then from $20 / 30 days in USDC.</span>
      </div>'''


def nav():
    link = 'min-height: 44px; padding: 0 14px; display: flex; align-items: center; font-size: 14px; font-weight: 700; color: {{c.text2}}; text-decoration: none'
    return f'''<div style="position: sticky; top: 0; z-index: 60; width: 100%; box-sizing: border-box; display: flex; justify-content: center; padding: {{{{nav.pad}}}}">
    <div ref="{{{{setSentinel}}}}" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 1px; height: 1px"></div>
    <header style="width: {{{{nav.w}}}}; max-width: 100%; height: {{{{nav.h}}}}; box-sizing: border-box; padding: 0 {{{{nav.inPad}}}}; display: flex; align-items: center; justify-content: space-between; border-radius: {{{{nav.r}}}}; background: {{{{nav.bg}}}}; box-shadow: {{{{nav.shadow}}}}; backdrop-filter: {{{{nav.blur}}}}; -webkit-backdrop-filter: {{{{nav.blur}}}}; transition: background-color .25s ease, box-shadow .25s ease">
      <a class="tm-hover" href="#top" style="display: flex; align-items: center; gap: 10px; color: {{{{c.text}}}}; text-decoration: none">{GLYPH(30, 10)}<span style="font-size: 18px; font-weight: 800; letter-spacing: -0.01em">TrenchM8</span></a>
      <nav aria-label="Main" style="display: flex; align-items: center; gap: 2px">
        <sc-if value="{{{{desktop}}}}" hint-placeholder-val="{{{{ true }}}}">
          <a class="tm-hover" href="#how" style="{link}">How it works</a>
          <a class="tm-hover" href="#pricing" style="{link}">Pricing</a>
          <a class="tm-hover" href="#login" style="{link}">Log in</a>
        </sc-if>
        <a class="tm-press" href="#top" onClick="{{{{startTop}}}}" style="margin-left: 8px; height: 40px; padding: 0 18px; border-radius: 999px; display: flex; align-items: center; font-size: 14px; font-weight: 800; color: {{{{c.bg}}}}; background: {{{{c.text}}}}; text-decoration: none">Start free</a>
      </nav>
    </header>
  </div>'''


# Headline words: (text, italic). The italic half is the promise.
WORDS = [('Your', 0), ('trading', 0), ('mate', 0), ('texts', 0), ('you', 0), ('|', 0), ('after', 1), ('every', 1), ('session.', 1)]


def h1():
    out, i = [], 0
    for w, it in WORDS:
        if w == '|':
            out.append('<span style="display: {{hero.br}}"><br></span>')
            continue
        st = ' font-style: italic;' if it else ''
        out.append(f'<span class="lp-word" style="--tm-d: {0.06 + i * 0.09:.2f}s;{st}">{w}</span>')
        i += 1
    return ' '.join(out)


def hero():
    return f'''  <section id="top" style="position: relative; width: 100%; display: flex; flex-direction: column; align-items: center; padding: {{{{hero.pad}}}}; box-sizing: border-box">
    <div style="display: flex; flex-direction: column; align-items: center; gap: {{{{hero.gap}}}}; width: 980px; max-width: 100%; text-align: center">
      <span class="tm-fade" style="font-size: 13px; font-weight: 700; color: {{{{c.text3}}}}">{{{{eyebrow}}}}</span>
      <h1 class="lp-serif" style="margin: 0; font-size: {{{{hero.h1}}}}; line-height: 0.98; letter-spacing: -0.02em">{h1()}</h1>
      <p class="tm-fade" style="--tm-d: .7s; margin: 0; max-width: 560px; font-size: {{{{hero.sub}}}}; line-height: 1.5; font-weight: 500; color: {{{{c.text2}}}}">M8 watches your wallets. About 2 hours after your last trade, it texts you on Telegram or Discord. Reply by text or voice, and your journal writes itself.</p>
      <div class="tm-fade" style="--tm-d: .85s; width: {{{{cta.wrapW}}}}; display: flex; justify-content: center; margin-top: 6px">{ctas()}</div>
    </div>
    <div class="tm-fade" style="--tm-d: 1s; margin-top: {{{{hero.phoneTop}}}}">{hero_phone()}</div>
  </section>'''


def marker(n):
    return f'<span style="font-size: 14px; font-weight: 700; color: {{{{c.text3}}}}; font-variant-numeric: tabular-nums">({n})</span>'


def facts(*items):
    return f'<div style="display: flex; flex-wrap: wrap; align-items: center; gap: 6px 22px; font-size: 14px; font-weight: 700; color: {{{{c.text3}}}}">{"".join(f"<span>{t}</span>" for t in items)}</div>'


def h2(t, size='{{row.h2}}'):
    return f'<h2 class="lp-serif" style="margin: 0; font-size: {size}; line-height: 1.0; letter-spacing: -0.02em">{t}</h2>'


def para(t, w='auto'):
    return f'<p style="margin: 0; max-width: {w}; font-size: {{{{row.p}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">{t}</p>'


ROWS = {
    1: ('It texts you <i>after</i> you trade.',
        'Paste a wallet once. M8 tracks every trade on Solana, Base, BNB and Robinhood Chain. About 2 hours after your last trade, it texts you on Telegram or Discord. Reply however you like, a few words or a voice note.',
        facts('Read-only, nothing to sign', '5 wallets, or 30 on Pro', 'Text or voice')),
    2: ('Your journal <i>writes itself.</i>',
        'Your reply becomes the day&#39;s entry, in your own words. M8 adds its take, tags every trade and keeps the receipts. Change anything by hand, or just tell M8.',
        facts('In your words', 'M8&#39;s take, separate', 'Edit with Undo')),
    3: ('It <i>catches</i> your patterns.',
        'Once, while you&#39;re still in it: same move as Sep 18, 2 min after a loss. And over weeks, where your edge is and where it leaks: +$2,910 on coins under 1 hour old, -$1,626 on everything older.',
        facts('One live check-in per session', 'Always with receipts', 'Never a call')),
}


def row_text(n, w):
    t, p, f = ROWS[n]
    return f'''<div style="display: flex; flex-direction: column; gap: 20px; width: {w}">
        {marker(n)}
        {h2(t)}
        {para(p)}
        {f}
      </div>'''


# ------------------------------------------------------------------ (4) a day with M8: notifications
def app_icon(kind, s=38):
    bg = '#2AABEE' if kind == 'tg' else '#5865F2'
    inner = TG_ICON(s) if kind == 'tg' else DC_ICON(s)
    # Squircle app icon: the round logo scaled up inside a rounded square of the same colour.
    return f'<span style="width: {s}px; height: {s}px; flex-shrink: 0; border-radius: {round(s * 0.24)}px; background: {bg}; overflow: hidden; display: flex; align-items: center; justify-content: center"><span style="display: flex; transform: scale(1.32)">{inner}</span></span>'


DAY = [
    ('8:00 AM', 'Morning brief', 'tg', 'Morning. SOL is up 4% overnight and Base launches are busy. One thing from yesterday: no new entries after 1 PM.'),
    ('1:12 PM', 'Rule alert', 'tg', 'Your rule: no new entries after 1 PM. You just bought $WIFHAT. Planned?'),
    ('1:31 PM', 'Live check-in', 'dc', 'Same move as Sep 18: $PEPU2, 4 min after a red trade, at 2x your normal size. Planned?'),
    ('4:22 PM', 'After the session', 'tg', '8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?'),
    ('4:28 PM', 'Journal', 'tg', 'Logged it. Morning +$609, $WIFHAT -$221 (FOMO), $PEPU2 -$154 (revenge). Your words are in.'),
    ('Sunday, 6:00 PM', 'Sunday recap', 'dc', 'Your week: up $816 on 31 trades, best week this month. Your recap card is ready.'),
]


def notif(t, label, kind, body):
    app = 'Telegram' if kind == 'tg' else 'Discord'
    return f'''<div style="display: flex; flex-direction: column; gap: 10px; min-width: 0">
          <span style="font-size: 13px; font-weight: 700; color: {{{{c.text3}}}}">{t} · {label}</span>
          <div style="flex-grow: 1; display: flex; gap: 12px; padding: 14px 16px 15px 14px; border-radius: 24px; background: {{{{c.notif}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}" aria-label="{app} notification from M8, {t}">
            {app_icon(kind)}
            <div style="display: flex; flex-direction: column; gap: 2px; min-width: 0; flex-grow: 1">
              <div style="display: flex; align-items: baseline; justify-content: space-between; gap: 8px"><span style="font-size: 15px; font-weight: 800">M8</span><span style="font-size: 12px; font-weight: 600; color: {{{{c.text3}}}}">{app}</span></div>
              <span style="font-size: 15px; line-height: 1.4; font-weight: 500; color: {{{{c.text2}}}}">{body}</span>
            </div>
          </div>
        </div>'''


def day():
    cards = ''.join(notif(*d) for d in DAY)
    return f'''<div style="width: 100%; display: flex; flex-direction: column; gap: {{{{day.gap}}}}; padding: {{{{row.pad}}}}; border-top: 1px solid {{{{c.line}}}}">
      <div style="display: flex; flex-direction: {{{{day.headDir}}}}; align-items: {{{{day.headAlign}}}}; justify-content: space-between; gap: 20px">
        <div style="display: flex; flex-direction: column; gap: 20px; width: {{{{day.titleW}}}}">{marker(4)}{h2('A day <i>with</i> M8.')}</div>
        <div style="display: flex; flex-direction: column; gap: 20px; width: {{{{day.textW}}}}">{para('Mornings, live check-ins, the nudge after a session, and your week on Sunday. Never more than 6 messages a day, and you can mute any of them.')}{facts('8 AM your time', 'Mute anytime', 'Shareable recap card')}</div>
      </div>
      <div style="display: grid; grid-template-columns: {{{{day.cols}}}}; gap: 28px 20px">{cards}</div>
    </div>'''


def visuals(mobile):
    clip, captioned = b2.clip, b2.captioned
    if not mobile:
        v1 = f'<div style="display: flex; gap: 20px; align-items: flex-start">{captioned(clip("TgNudge", 0, 57, 390, 266, 0.95), "Telegram")}{captioned(clip("DcNudge", 0, 44, 390, 266, 0.95, bg="#313338"), "Discord")}</div>'
        v2 = clip('Desktop', 4, 76, 1432, 824, 0.838, radius=24)
        v3 = f'<div style="display: flex; gap: 20px; align-items: flex-start">{captioned(clip("TgRepeat", 0, 100, 390, 318, 0.95), "Live, mid-session")}{captioned(clip("Stats", 24, 1071, 453, 327, 0.81, bg="{{c.bg}}"), "Over weeks, on the web")}</div>'
    else:
        v1 = f'<div style="display: flex; flex-direction: column; gap: 20px">{captioned(clip("TgNudge", 0, 57, 390, 266, 0.918), "Telegram")}{captioned(clip("DcNudge", 0, 44, 390, 266, 0.918, bg="#313338"), "Discord")}</div>'
        v2 = clip('Main', 0, 0, 390, 916, 0.918, radius=24)
        v3 = f'<div style="display: flex; flex-direction: column; gap: 20px">{captioned(clip("TgRepeat", 0, 100, 390, 318, 0.918), "Live, mid-session")}{captioned(clip("Stats", 24, 1071, 453, 327, 0.79, bg="{{c.bg}}"), "Over weeks, on the web")}</div>'
    return v1, v2, v3


def rows():
    d1, d2, d3 = visuals(False)
    m1, m2, m3 = visuals(True)
    line = 'border-top: 1px solid {{c.line}}'
    desk = f'''<sc-if value="{{{{desktop}}}}" hint-placeholder-val="{{{{ true }}}}">
    <div style="width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: {{{{row.pad}}}}; {line}">{row_text(1, '420px')}{d1}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 48px; padding: {{{{row.pad}}}}; {line}">
      <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
        <div style="display: flex; flex-direction: column; gap: 20px; width: 560px">{marker(2)}{h2(ROWS[2][0])}</div>
        <div style="display: flex; flex-direction: column; gap: 20px; width: 500px">{para(ROWS[2][1])}{ROWS[2][2]}</div>
      </div>
      {d2}
    </div>
    <div style="width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: {{{{row.pad}}}}; {line}">{d3}{row_text(3, '420px')}</div>
    </sc-if>'''
    mob = f'''<sc-if value="{{{{mobile}}}}" hint-placeholder-val="{{{{ false }}}}">
    <div style="width: 100%; display: flex; flex-direction: column; gap: 32px; padding: {{{{row.pad}}}}; {line}">{row_text(1, '100%')}{m1}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 32px; padding: {{{{row.pad}}}}; {line}">{row_text(2, '100%')}{m2}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 32px; padding: {{{{row.pad}}}}; {line}">{row_text(3, '100%')}{m3}</div>
    </sc-if>'''
    return f'''  <section id="how" style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{{{sec.pad}}}}; display: flex; flex-direction: column; align-items: center">
    {desk}
    {mob}
    {day()}
  </section>'''


def pricing():
    def plan(name, price, alt, wallets, who):
        return f'''<div style="flex: 1 1 0; min-width: 0; padding: {{{{price.cardPad}}}}; border-radius: 28px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}; display: flex; flex-direction: column; gap: 6px">
          <span style="font-size: 15px; font-weight: 800; color: {{{{c.text2}}}}">{name}</span>
          <span style="display: flex; align-items: baseline; gap: 8px; margin-top: 6px"><span class="lp-serif" style="font-size: 64px; line-height: 1; letter-spacing: -0.02em">{price}</span><span style="font-size: 16px; font-weight: 700; color: {{{{c.text3}}}}">/ 30 days</span></span>
          <span style="font-size: 14px; font-weight: 600; color: {{{{c.text3}}}}">{alt}</span>
          <div style="height: 1px; margin: 16px 0 12px 0; background: {{{{c.line}}}}"></div>
          <span style="font-size: 17px; font-weight: 800">{wallets}</span>
          <span style="font-size: 15px; font-weight: 500; color: {{{{c.text2}}}}">{who}</span>
        </div>'''
    return f'''  <section id="pricing" style="width: {{{{sec.w}}}}; max-width: 100%; box-sizing: border-box; padding: {{{{price.pad}}}}; display: flex; flex-direction: column; gap: 40px; border-top: 1px solid {{{{c.line}}}}">
    <div style="display: flex; flex-direction: {{{{day.headDir}}}}; align-items: {{{{day.headAlign}}}}; justify-content: space-between; gap: 20px">
      <div style="display: flex; flex-direction: column; gap: 20px; width: {{{{day.titleW}}}}">{marker(5)}{h2('Two plans. <i>Same</i> M8.')}</div>
      <div style="width: {{{{day.textW}}}}">{para('Both get everything: nudges, the journal, patterns, briefs, recaps and ask-anything. The only difference is how many wallets you trade from.')}</div>
    </div>
    <div style="display: flex; flex-direction: {{{{price.dir}}}}; gap: 16px">
      {plan('Base', '$20', 'or $50 for 90 days', '5 trading wallets', 'For most traders.')}
      {plan('Pro', '$50', 'or $125 for 90 days', '30 trading wallets', 'For traders who split across many wallets.')}
    </div>
    <span style="font-size: 14px; font-weight: 600; line-height: 1.5; color: {{{{c.text3}}}}">7 days free, no card. Pay in USDC on Solana. No auto-renew: M8 reminds you 3 days before it runs out.</span>
  </section>'''


def founder():
    return f'''  <section style="width: {{{{sec.w}}}}; max-width: 100%; box-sizing: border-box; padding: {{{{founder.pad}}}}; display: flex; justify-content: center; border-top: 1px solid {{{{c.line}}}}">
    <figure style="margin: 0; width: 820px; max-width: 100%; display: flex; flex-direction: column; align-items: {{{{founder.align}}}}; gap: 28px; text-align: {{{{founder.textAlign}}}}">
      <span style="padding: 4px 10px; border-radius: 999px; border: 1px dashed {{{{c.text3}}}}; font-size: 12px; font-weight: 700; color: {{{{c.text3}}}}">Draft: Josh to rewrite</span>
      <blockquote class="lp-serif" style="margin: 0; font-size: {{{{founder.size}}}}; line-height: 1.12; letter-spacing: -0.01em">&#8220;Every trader knows a journal would help.<span style="display: {{founder.br}}"><br></span> Almost nobody keeps one.<span style="display: {{founder.br}}"><br></span> <i>So M8 does the writing.</i>&#8221;</blockquote>
      <p style="margin: 0; max-width: 600px; font-size: {{{{row.p}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">It watches the wallets, texts once the session is over, and turns a quick reply into the journal you meant to keep. It won&#39;t tell you what to buy. It just makes sure you remember what you did, and why.</p>
      <figcaption style="display: flex; align-items: center; gap: 12px; text-align: left">{GLYPH(36, 12)}<span style="display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 800">Josh, founder</span><span style="font-size: 13px; font-weight: 600; color: {{{{c.text3}}}}">TrenchM8</span></span></figcaption>
    </figure>
  </section>'''


def closing():
    return f'''  <section style="width: {{{{sec.w}}}}; max-width: 100%; box-sizing: border-box; padding: {{{{close.pad}}}}; display: flex; flex-direction: column; align-items: center; gap: 36px; text-align: center; border-top: 1px solid {{{{c.line}}}}">
    <h2 class="lp-serif" style="margin: 0; font-size: {{{{close.h2}}}}; line-height: 0.98; letter-spacing: -0.02em">Your journal starts<span style="display: {{{{close.br}}}}"><br></span> <i>with one text.</i></h2>
    {ctas()}
  </section>'''


def footer():
    return '''  <footer style="width: {{sec.w}}; max-width: 100%; box-sizing: border-box; padding: {{foot.pad}}; display: flex; flex-direction: {{foot.dir}}; align-items: {{foot.align}}; justify-content: space-between; gap: 16px; font-size: 13px; font-weight: 600; color: {{c.text3}}; border-top: 1px solid {{c.line}}">
    <span>Not financial advice. M8 never makes calls.</span>
    <div style="display: flex; gap: 20px"><a class="tm-hover" href="#terms" style="color: {{c.text3}}; text-decoration: none">Terms</a><a class="tm-hover" href="#privacy" style="color: {{c.text3}}; text-decoration: none">Privacy</a></div>
  </footer>'''


SCRIPT = r'''class Component extends DCLogic {
  componentWillUnmount() { if (this._io) this._io.disconnect(); }
  renderVals() {
    const st = this.state || {};
    const theme = this.props.theme ?? 'dark';
    const layout = this.props.layout ?? 'desktop';
    const desktop = layout !== 'mobile';
    const accent = this.props.accent ?? '#7CD4FF';
    const themes = {
      dark: { bg: '#0D0E13', surface: '#171922', line: '#2C303D', text: '#F3F4F7', text2: '#A9AEBE', text3: '#858B9E', notif: 'rgba(33,36,47,0.72)', tipBg: '#F3F4F7', tipFg: '#12131A', shadow: 'rgba(0,0,0,0.5)', edge: 'rgba(255,255,255,0.06)', glass: 'rgba(23,25,34,0.78)', glassLine: 'rgba(255,255,255,0.08)', grain: '0.07', blend: 'overlay' },
      light: { bg: '#F4F4F7', surface: '#FFFFFF', line: '#E3E5EB', text: '#12131A', text2: '#4F5566', text3: '#666C7E', notif: '#FFFFFF', tipBg: '#12131A', tipFg: '#F3F4F7', shadow: 'rgba(18,19,26,0.16)', edge: 'rgba(18,19,26,0.08)', glass: 'rgba(255,255,255,0.8)', glassLine: 'rgba(18,19,26,0.08)', grain: '0.05', blend: 'multiply' }
    };
    const c = themes[theme] || themes.dark;
    const dark = theme !== 'light';
    const stop = (e) => { if (e && e.preventDefault) e.preventDefault(); };
    const heights = [6, 10, 16, 22, 14, 20, 26, 18, 10, 16, 24, 28, 20, 12, 18, 24, 14, 8, 12, 20, 16, 10, 14, 8, 10, 6, 8, 5, 6, 4];
    const wave = heights.map((h, i) => ({ h: h + 'px', tg: i < 11 ? '#E9EEF3' : 'rgba(233,238,243,0.38)' }));
    const glass = !!st.navGlass;
    return {
      theme, accent, c, desktop, mobile: !desktop, wave,
      startTg: stop, startDc: stop, startTop: stop,
      eyebrow: desktop ? 'For memecoin traders on Solana, Base, BNB and Robinhood Chain' : 'Solana · Base · BNB · Robinhood Chain',
      setSentinel: (el) => {
        if (this._io) { this._io.disconnect(); this._io = null; }
        if (el && window.IntersectionObserver) {
          this._io = new IntersectionObserver((es) => { const g = !es[0].isIntersecting; if (g !== !!(this.state || {}).navGlass) this.setState({ navGlass: g }); });
          this._io.observe(el);
        }
      },
      nav: glass
        ? { pad: desktop ? '12px 20px 0 20px' : '8px 12px 0 12px', w: desktop ? '1240px' : '100%', h: desktop ? '64px' : '56px', inPad: desktop ? '12px 0 20px' : '8px 0 14px', r: '20px', bg: c.glass, shadow: '0 16px 40px ' + (dark ? 'rgba(0,0,0,0.35)' : 'rgba(18,19,26,0.16)') + ', inset 0 0 0 1px ' + c.glassLine, blur: 'blur(18px) saturate(140%)' }
        : { pad: desktop ? '12px 20px 0 20px' : '8px 12px 0 12px', w: desktop ? '1240px' : '100%', h: desktop ? '64px' : '56px', inPad: desktop ? '20px' : '4px', r: '20px', bg: 'transparent', shadow: 'none', blur: 'none' },
      hero: desktop
        ? { pad: '72px 0 0 0', gap: '24px', h1: '92px', sub: '20px', br: 'inline', phoneTop: '64px' }
        : { pad: '40px 16px 0 16px', gap: '20px', h1: '54px', sub: '17px', br: 'none', phoneTop: '48px' },
      ph: desktop ? { zoom: 1, cropW: '400px', cropH: '470px', s1: dark ? 'rgba(0,0,0,0.5)' : 'rgba(18,19,26,0.18)' } : { zoom: 0.88, cropW: '358px', cropH: '420px', s1: dark ? 'rgba(0,0,0,0.5)' : 'rgba(18,19,26,0.18)' },
      cta: desktop ? { dir: 'row', w: 'auto', wrapW: 'auto', align: 'flex-start', calign: 'center' } : { dir: 'column', w: '100%', wrapW: '100%', align: 'stretch', calign: 'center' },
      row: { h2: desktop ? '64px' : '42px', p: desktop ? '18px' : '16px', pad: desktop ? '112px 0' : '64px 0' },
      day: desktop
        ? { gap: '56px', headDir: 'row', headAlign: 'flex-end', titleW: '560px', textW: '500px', cols: 'repeat(3, minmax(0, 1fr))' }
        : { gap: '32px', headDir: 'column', headAlign: 'stretch', titleW: '100%', textW: '100%', cols: 'minmax(0, 1fr)' },
      sec: { pad: desktop ? '0' : '0 16px', w: desktop ? '1200px' : 'calc(100% - 32px)' },
      price: { pad: desktop ? '112px 0' : '64px 0', dir: desktop ? 'row' : 'column', cardPad: desktop ? '28px 28px 26px 28px' : '22px 22px 20px 22px' },
      founder: desktop ? { pad: '112px 0', size: '56px', align: 'center', textAlign: 'center', br: 'inline' } : { pad: '64px 0', size: '36px', align: 'flex-start', textAlign: 'left', br: 'none' },
      close: desktop ? { pad: '128px 0 136px 0', h2: '104px', br: 'inline' } : { pad: '80px 0 88px 0', h2: '56px', br: 'none' },
      foot: desktop ? { pad: '32px 0 48px 0', dir: 'row', align: 'center' } : { pad: '28px 0 40px 0', dir: 'column', align: 'flex-start' }
    };
  }
}'''


def build():
    props = {"layout": {"editor": "enum", "options": ["desktop", "mobile"], "default": "desktop", "section": "Look"},
             "theme": {"editor": "enum", "options": ["dark", "light"], "default": "dark", "section": "Look"},
             "accent": {"editor": "color", "default": "#7CD4FF", "options": ACCENTS, "section": "Look"},
             "$preview": {"width": 1440, "height": H_DESK}}
    body = '\n'.join([nav(), hero(), rows(), pricing(), founder(), closing(), footer()])
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>TrenchM8 - landing v2, B3: editorial, night paper</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div class="lp-paper" style="--tm-tip-bg: {{{{c.tipBg}}}}; --tm-tip-fg: {{{{c.tipFg}}}}; --tm-focus: {{{{accent}}}}; --lp-shadow: {{{{c.shadow}}}}; --lp-edge: {{{{c.edge}}}}; --lp-grain: {{{{c.grain}}}}; --lp-blend: {{{{c.blend}}}}; width: 100%; box-sizing: border-box; background: {{{{c.bg}}}}; color: {{{{c.text}}}}; font-family: Manrope, system-ui, sans-serif; font-variant-numeric: tabular-nums; -webkit-font-smoothing: antialiased; display: flex; flex-direction: column; align-items: center; overflow: clip">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, separators=(",", ":"))}'>
{SCRIPT}
</script>
</body>
</html>
'''
    open(D + 'LandingB3.dc.html', 'w').write(html)
    mob = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>TrenchM8 - landing v2, B3 (mobile)</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link href="{FONTS}" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width: 390px; min-height: {H_MOB}px; background: {{{{bg}}}}">
  <dc-import name="LandingB3" layout="mobile" theme="{{{{theme}}}}" accent="{{{{accent}}}}" hint-size="390px,{H_MOB}px"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps({"theme": props["theme"], "accent": props["accent"], "$preview": {"width": 390, "height": H_MOB}}, separators=(",", ":"))}'>
class Component extends DCLogic {{
  renderVals() {{
    const theme = this.props.theme ?? 'dark';
    return {{ theme, accent: this.props.accent ?? '#7CD4FF', bg: theme === 'light' ? '#F4F4F7' : '#0D0E13' }};
  }}
}}
</script>
</body>
</html>
'''
    open(D + 'LandingB3Mobile.dc.html', 'w').write(mob)


if __name__ == '__main__':
    build()
    print('ok')
