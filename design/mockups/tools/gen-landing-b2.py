# Generates LandingB2.dc.html (refined chat-first landing, desktop + mobile) and its LandingB2Mobile wrapper.
# Usage: python3 tools/gen-landing-b2.py [desktopHeight] [mobileHeight]
import json, os, re, sys

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
H_DESK = int(sys.argv[1]) if len(sys.argv) > 1 else 5900
H_MOB = int(sys.argv[2]) if len(sys.argv) > 2 else 8460
ACCENTS = ["#7CD4FF", "#FFD23F", "#6495ED", "#B4A5FF", "#FF85C8", "#FF9152", "#FFB547"]


def R(s, **kw):
    """Fills [[name]] slots; leaves {{dc}} bindings alone."""
    for k, v in kw.items():
        s = s.replace('[[' + k + ']]', v)
    assert '[[' not in s, s[s.index('[['):][:60]
    return s


# ------------------------------------------------------------------ helmet
HELMET = open(D + 'tools/landing-helmet.html').read().replace('</style>\n</helmet>', '''/* Landing B2 */
.lp-clip [style*="position: sticky"]{position:relative!important;top:auto!important}
.lp-shot{box-shadow:0 30px 80px var(--lp-shadow, rgba(0,0,0,.45)), 0 0 0 1px var(--lp-edge, rgba(255,255,255,.06))}
@keyframes lp-word{from{opacity:0;filter:blur(14px);transform:translateY(10px)}to{opacity:1;filter:none;transform:none}}
.lp-word{display:inline-block;animation:lp-word .8s cubic-bezier(.2,.8,.2,1) both;animation-delay:var(--tm-d,0s)}
@keyframes lp-bub{from{opacity:0;transform:translateY(6px) scale(.7)}to{opacity:1;transform:none}}
.lp-bub{animation:lp-bub .42s cubic-bezier(.2,.9,.3,1.15) both;transform-origin:bottom left}
.lp-bub-r{animation:lp-bub .42s cubic-bezier(.2,.9,.3,1.15) both;transform-origin:bottom right}
@keyframes lp-chip{from{opacity:0;transform:translateY(8px) scale(.9)}to{opacity:1;transform:none}}
.lp-chip{animation:lp-chip .35s cubic-bezier(.2,.9,.3,1.15) both;animation-delay:var(--tm-d,0s);transition:transform .12s ease,filter .15s ease;cursor:pointer}
.lp-chip:hover{filter:brightness(1.18)}
.lp-chip:active{transform:scale(.96)}
.lp-chip:focus-visible{outline:2px solid var(--tm-focus,#7CD4FF);outline-offset:2px}
@keyframes lp-dot{0%,80%,100%{opacity:.35;transform:translateY(0)}40%{opacity:1;transform:translateY(-2px)}}
.lp-dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:currentColor;animation:lp-dot 1.1s ease-in-out infinite}
.lp-scroll{scrollbar-width:none}
.lp-scroll::-webkit-scrollbar{display:none}
@keyframes lp-rec{0%,100%{opacity:1}50%{opacity:.25}}
.lp-rec{animation:lp-rec 1s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){.lp-word,.lp-bub,.lp-bub-r,.lp-chip{animation:none}.lp-dot,.lp-rec{animation:none}}
</style>
</helmet>''')
assert '/* Landing B2 */' in HELMET


def extract_img(fname):
    s = open(D + fname).read()
    i = s.index('<div role="img"')
    depth = 0
    for m in re.finditer(r'<(/?)div\b', s[i:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            j = i + m.end()
            break
    return s[i:s.index('>', j) + 1]


RECAP = extract_img('TgRecap.dc.html')  # native width 330
DOTS3 = '<span class="lp-dot"></span><span class="lp-dot" style="animation-delay: .15s"></span><span class="lp-dot" style="animation-delay: .3s"></span>'


def recap(w):
    return f'<div style="width: {w}px; overflow: hidden"><div style="width: 330px; zoom: {round(w / 330, 4)}">{RECAP}</div></div>'


# ------------------------------------------------------------------ real boards (for the numbered rows)
BOARD = {'Desktop': (1440, 1840), 'Stats': (1440, 3100), 'Main': (390, 3020), 'TgNudge': (390, 1640), 'DcNudge': (390, 1072),
         'TgRepeat': (390, 1180), 'TgMorning': (390, 900)}
THEMED = {'Desktop', 'Stats', 'Main'}


def imp(name):
    w, h = BOARD[name]
    th = ' theme="{{theme}}"' if name in THEMED else ''
    lay = ' layout="desktop"' if name == 'Stats' else ''
    return f'<dc-import name="{name}"{th}{lay} accent="{{{{accent}}}}" hint-size="{w}px,{h}px"></dc-import>'


def clip(name, x, y, w, h, z, radius=24, bg='#0D0E13', shadow=True):
    bw, _ = BOARD[name]
    W, H = round(w * z), round(h * z)
    cls = 'lp-clip lp-shot' if shadow else 'lp-clip'
    return (f'<div class="{cls}" style="width: {W}px; height: {H}px; flex-shrink: 0; overflow: hidden; border-radius: {radius}px; background: {bg}">'
            f'<div style="zoom: {z}; width: {w}px; height: {h}px; overflow: hidden">'
            f'<div style="margin-left: -{x}px; margin-top: -{y}px; width: {bw}px">{imp(name)}</div></div></div>')


def cap(t):
    return f'<span style="font-size: 13px; font-weight: 700; color: {{{{c.text3}}}}">{t}</span>'


def captioned(inner, t):
    return f'<div style="display: flex; flex-direction: column; gap: 10px">{inner}{cap(t)}</div>'


# ------------------------------------------------------------------ icons
GLYPH = lambda s, r=12: (f'<svg width="{s}" height="{s}" viewBox="0 0 36 36" aria-hidden="true" style="flex-shrink: 0; display: block"><rect x="0" y="0" width="36" height="36" rx="{r}" fill="{{{{accent}}}}"></rect>'
                         '<rect x="11" y="12" width="4.5" height="9" rx="2.25" fill="#15140E"></rect><rect x="20.5" y="12" width="4.5" height="9" rx="2.25" fill="#15140E"></rect></svg>')
TG_ICON = lambda s=24: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true" style="flex-shrink: 0"><circle cx="12" cy="12" r="12" fill="#2AABEE"></circle><path d="M5.6 11.7l10.9-4.2c.5-.2 1 .1.8.9l-1.9 8.8c-.1.6-.5.8-1 .5l-2.8-2.1-1.4 1.3c-.2.2-.3.3-.6.3l.2-2.9 5.3-4.8c.2-.2 0-.3-.3-.1l-6.6 4.1-2.8-.9c-.6-.2-.6-.6.2-.9z" fill="#FFFFFF"></path></svg>'
DC_ICON = lambda s=24: f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true" style="flex-shrink: 0"><circle cx="12" cy="12" r="12" fill="#5865F2"></circle><path d="M16.9 8.1a9.6 9.6 0 0 0-2.4-.8l-.3.6a8.9 8.9 0 0 0-2.4-.1 8.9 8.9 0 0 0-1.4.1l-.3-.6a9.6 9.6 0 0 0-2.4.8C6.2 10.4 5.8 12.6 6 14.8a9.7 9.7 0 0 0 2.9 1.5l.6-1c-.3-.1-.7-.3-1-.5l.2-.2a6.9 6.9 0 0 0 6.6 0l.2.2c-.3.2-.7.4-1 .5l.6 1a9.6 9.6 0 0 0 2.9-1.5c.2-2.5-.4-4.7-2.1-6.7zM10 13.6c-.6 0-1-.5-1-1.1s.4-1.1 1-1.1 1 .5 1 1.1-.4 1.1-1 1.1zm4 0c-.6 0-1-.5-1-1.1s.4-1.1 1-1.1 1 .5 1 1.1-.4 1.1-1 1.1z" fill="#FFFFFF"></path></svg>'


def ico(paths, size=20, color='currentColor', sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'


I_EXT = '<path d="M7 17L17 7"></path><path d="M8 7h9v9"></path>'
I_MIC = '<rect x="9" y="3" width="6" height="11" rx="3"></rect><path d="M5 11a7 7 0 0 0 14 0"></path><path d="M12 18v3"></path>'
I_CHECK2 = '<path d="M2 12.5l4 4 8-9"></path><path d="M9.5 16.5l1 0 8-9"></path>'

# ------------------------------------------------------------------ phone shell
STATUS_ICONS = ('<svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1" fill="currentColor"></rect><rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="currentColor"></rect><rect x="10" y="3" width="3" height="9" rx="1" fill="currentColor"></rect><rect x="15" y="0" width="3" height="12" rx="1" fill="currentColor"></rect></svg>'
                '<svg width="16" height="12" viewBox="0 0 16 12" aria-hidden="true"><path d="M8 2.2c2.3 0 4.4.9 6 2.4l1.2-1.3A10.4 10.4 0 0 0 8 .4C5.2.4 2.7 1.5.8 3.3L2 4.6a8.6 8.6 0 0 1 6-2.4zm0 3.6c1.3 0 2.5.5 3.4 1.3l1.2-1.3A6.7 6.7 0 0 0 8 4c-1.8 0-3.4.7-4.6 1.8l1.2 1.3c.9-.8 2.1-1.3 3.4-1.3zm0 3.5c-.5 0-1 .2-1.3.5L8 11.2l1.3-1.4A1.9 1.9 0 0 0 8 9.3z" fill="currentColor"></path></svg>'
                '<svg width="27" height="13" viewBox="0 0 27 13" aria-hidden="true"><rect x="0.5" y="0.5" width="23" height="12" rx="3.8" fill="none" stroke="currentColor" stroke-opacity="0.4"></rect><rect x="2" y="2" width="18" height="9" rx="2.5" fill="currentColor"></rect><path d="M25 4.5v4c.8-.3 1.3-1.1 1.3-2s-.5-1.7-1.3-2z" fill="currentColor" fill-opacity="0.4"></path></svg>')


def status_bar(bg, fg):
    return f'''<div style="position: relative; height: 50px; flex-shrink: 0; display: flex; align-items: center; justify-content: space-between; padding: 6px 26px 0 34px; box-sizing: border-box; background: {bg}; color: {fg}">
          <span style="font-family: -apple-system, 'SF Pro Text', system-ui, sans-serif; font-size: 16px; font-weight: 600; letter-spacing: -0.01em">9:41</span>
          <span aria-hidden="true" style="position: absolute; left: 50%; top: 11px; width: 112px; height: 32px; margin-left: -56px; border-radius: 20px; background: #000000"></span>
          <span style="display: flex; align-items: center; gap: 6px">{STATUS_ICONS}</span>
        </div>'''


def home_bar(bg):
    return f'<div style="height: 26px; flex-shrink: 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 8px; box-sizing: border-box; background: {bg}"><span style="width: 128px; height: 5px; border-radius: 3px; background: #FFFFFF; opacity: 0.85"></span></div>'


def scroll(inner, pad):
    # column-reverse keeps the newest message pinned at the bottom (and scrollTop 0 is the bottom).
    return f'''<div ref="{{{{setScroll}}}}" class="lp-scroll" style="flex-grow: 1; min-height: 0; overflow-y: auto; -webkit-mask-image: linear-gradient(180deg, transparent 0, #000 36px); mask-image: linear-gradient(180deg, transparent 0, #000 36px); display: flex; flex-direction: column-reverse">
          <div style="display: flex; flex-direction: column; padding: {pad}">{inner}
          </div>
        </div>'''


# ------------------------------------------------------------------ Telegram chrome
TG_FONT = "-apple-system, BlinkMacSystemFont, 'SF Pro Text', Roboto, 'Helvetica Neue', sans-serif"
TG_IN = 'background: #1C2733; border-radius: 16px 16px 16px 4px'
TG_OUT = 'background: #2A4A6B; border-radius: 16px 16px 4px 16px'
TG_META = '<div style="font-size: 11px; color: #8A98A8; text-align: right; margin-top: 2px">[[t]]</div>'
TG_META_OUT = f'<div style="display: flex; justify-content: flex-end; align-items: center; gap: 3px; font-size: 11px; color: #A9C3DD; margin-top: 2px">[[t]]<span style="display: flex; color: #7FC1FF">{ico(I_CHECK2, 14, sw=1.8)}</span></div>'


def tg_in(body, t, w='max-width: 270px', top=6):
    return f'<div class="lp-bub" style="align-self: flex-start; {w}; margin-top: {top}px; padding: 7px 11px 5px 11px; {TG_IN}">{body}{R(TG_META, t=t)}</div>'


def tg_btns(*labels, cols=2, handlers=None):
    bs = ''
    for i, l in enumerate(labels):
        h = f' onClick="{{{{{handlers[i]}}}}}"' if handlers else ''
        bs += f'<button class="tm-press"{h} style="height: 38px; padding: 0 8px; border: none; border-radius: 10px; background: rgba(255,255,255,0.09); color: #E9EEF3; font-family: inherit; font-size: 14px; font-weight: 600; display: flex; align-items: center; justify-content: center; gap: 6px; cursor: pointer; white-space: nowrap">{l}</button>'
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 4px; margin-top: 4px">{bs}</div>'


def tg_group(body, t, btns='', top=6, w=270):
    return f'<div class="lp-bub" style="align-self: flex-start; width: {w}px; margin-top: {top}px; display: flex; flex-direction: column"><div style="padding: 7px 11px 5px 11px; {TG_IN}">{body}{R(TG_META, t=t)}</div>{btns}</div>'


def tg_out(body, t, top=6):
    return f'<div class="lp-bub-r" style="align-self: flex-end; max-width: 250px; margin-top: {top}px; padding: 7px 11px 5px 11px; {TG_OUT}">{body}{R(TG_META_OUT, t=t)}</div>'


WAVE = '<sc-for list="{{wave}}" as="b" hint-placeholder-count="30"><span style="width: 3px; flex-shrink: 0; border-radius: 2px; height: {{b.h}}; background: {{b.tg}}"></span></sc-for>'
WAVE_DC = '<sc-for list="{{wave}}" as="b" hint-placeholder-count="30"><span style="width: 3px; flex-shrink: 0; border-radius: 2px; height: {{b.h}}; background: {{b.dc}}"></span></sc-for>'

TG_VOICE = f'''<div class="lp-bub-r" style="align-self: flex-end; width: 236px; margin-top: 6px; padding: 7px 11px 5px 9px; {TG_OUT}; display: flex; flex-direction: column; gap: 2px">
              <div style="display: flex; align-items: center; gap: 9px">
                <span style="width: 38px; height: 38px; flex-shrink: 0; border-radius: 19px; background: #E9EEF3; color: #2A4A6B; display: flex; align-items: center; justify-content: center"><svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"></path></svg></span>
                <div aria-hidden="true" style="display: flex; align-items: center; gap: 2px; height: 26px; flex-grow: 1; min-width: 0; overflow: hidden">{WAVE}</div>
              </div>
              <div style="display: flex; justify-content: space-between; font-size: 11px; color: #A9C3DD"><span>0:07</span><span style="display: flex; align-items: center; gap: 3px">4:28 PM<span style="display: flex; color: #7FC1FF">{ico(I_CHECK2, 14, sw=1.8)}</span></span></div>
            </div>'''

TG_TYPING_IN = '<div class="lp-bub" style="align-self: flex-start; margin-top: 6px; height: 34px; padding: 0 14px; display: flex; align-items: center; gap: 4px; color: #8A98A8; background: #1C2733; border-radius: 16px 16px 16px 4px" aria-label="M8 is typing">' + DOTS3 + '</div>'

TG_JOURNAL = '''<span>Logged it. Here&#39;s your Wednesday:</span>
                <div style="display: flex; flex-direction: column; gap: 5px; margin-top: 6px; padding-left: 9px; border-left: 2px solid {{accent}}">
                  <span><b>Morning +$609.</b> 6 trades, sized small, took profit into strength.</span>
                  <span><b>$WIFHAT -$221.</b> FOMO: bought after a +180% candle.</span>
                  <span><b>$PEPU2 -$154.</b> Revenge: 4 min after closing $WIFHAT red, at 2x your normal size.</span>
                  <span style="color: #C9D3DD; font-style: italic">Your words: "they were pumping and I didn&#39;t want to miss out."</span>
                </div>'''

ANS_TG = {
    'week': tg_group(f'<div style="margin: -7px -11px 6px -11px; border-radius: 16px 16px 0 0; overflow: hidden">{recap(270)}</div><span>Your week: <b>up $816 on 31 trades</b>, best week this month. One change for next week: no new entries after 1 PM.</span>', '4:31 PM',
                     tg_btns('Share card', f'Full recap {ico(I_EXT, 13, sw=2.4)}')),
    'tilt': tg_in('<b>Heads up from today.</b> $PEPU2, 4 min after closing $WIFHAT red, at 2x your normal size: <b>-$154</b>.<br><br>Same move as Sep 18: $PEPU, 2 min after a loss, 2.5x size, -$188.', '4:31 PM')
            + tg_group('Want a 20 min cooldown after red trades? I&#39;ll ping you if you break it.', '4:31 PM', tg_btns('Set cooldown', 'Not now'), top=4),
    'calls': tg_in('<b>No calls, ever.</b> Ask about a coin and you get facts, not a verdict.<br><br>Not a call, just facts: $FROGZ is 41 min old, $86k liquidity, top 10 wallets hold 38%. Your best setup is coins under 1h old at normal size. Your call.', '4:31 PM'),
    'degen': tg_in('<span style="font-size: 13px; color: #8A98A8">Blunt degen voice · <span style="color: #7FC1FF">/voice</span> to switch</span><br>8 trades, +$234. morning was clean, then you gave back $375 on two coins after lunch. what happened, be honest', '4:31 PM'),
    'cta': tg_group('Want me to text you after your next session? Pick where:', '4:32 PM',
                    tg_btns(f'{TG_ICON(18)}Telegram', f'{DC_ICON(18)}Discord', handlers=['startTg', 'startDc']), top=4),
}


def tg_chip():
    return '''<button class="lp-chip" onClick="{{ch.pick}}" style="--tm-d: {{ch.d}}; height: 34px; padding: 0 13px; border: none; border-radius: 17px; background: #2A4A6B; color: #E9EEF3; font-family: inherit; font-size: 14px; font-weight: 500; box-shadow: 0 1px 0 rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.08); white-space: nowrap">{{ch.label}}</button>'''


def thread(kind):
    """The shared conversation, rendered in Telegram or Discord chrome."""
    if kind == 'tg':
        head = '''<span style="align-self: center; font-size: 12px; font-weight: 600; padding: 3px 10px; border-radius: 999px; background: rgba(255,255,255,0.08); color: #C9D3DD">Wednesday, October 7</span>
            <span style="align-self: center; margin-top: 6px; font-size: 12px; color: #8A98A8; text-align: center; padding: 0 20px">Last trade closed 2:20 PM. No activity for 2h, so M8 checks in.</span>'''
        nudge = tg_in('8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?', '4:22 PM', top=8)
        voice = TG_VOICE
        logged = tg_group(TG_JOURNAL, '4:28 PM', tg_btns(f'Open today&#39;s journal {ico(I_EXT, 13, sw=2.4)}', cols=1), w=282)
        you = '<div class="lp-bub-r" style="align-self: flex-end; max-width: 250px; margin-top: 8px; padding: 7px 11px 5px 11px; ' + TG_OUT + '">{{a.label}}' + R(TG_META_OUT, t='4:31 PM') + '</div>'
        ans = ANS_TG
        typing_in = TG_TYPING_IN
        chip = tg_chip()
        hint = ''
    else:
        head = DC_DIVIDER + DC_NOTE
        nudge = dc_group('m8', '4:22 PM', '8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?', top=10)
        voice = dc_group('you', '4:28 PM', DC_VOICE, cls='lp-bub')
        logged = dc_group('m8', '4:28 PM', 'Logged it. Here&#39;s your Wednesday:' + DC_JOURNAL + dc_row(dc_btn('Open today&#39;s journal', link=True)))
        you = dc_group('you', '4:31 PM', '{{a.label}}')
        ans = ANS_DC
        typing_in = ''
        chip = dc_chip()
        hint = ''
    answers = '\n'.join(f'<sc-if value="{{{{a.{k}}}}}" hint-placeholder-val="{{{{ false }}}}">{v}</sc-if>' for k, v in ans.items())
    return f'''
            {head}
            <sc-if value="{{{{s1}}}}" hint-placeholder-val="{{{{ true }}}}">{nudge}</sc-if>
            <sc-if value="{{{{s3}}}}" hint-placeholder-val="{{{{ true }}}}">{voice}</sc-if>
            <sc-if value="{{{{s5}}}}" hint-placeholder-val="{{{{ true }}}}">{logged}</sc-if>
            <sc-for list="{{{{answers}}}}" as="a" hint-placeholder-count="0">
              <sc-if value="{{{{a.you}}}}" hint-placeholder-val="{{{{ false }}}}">{you}</sc-if>
              {answers}
            </sc-for>
            <sc-if value="{{{{typingM8}}}}" hint-placeholder-val="{{{{ false }}}}">{typing_in}</sc-if>
            <sc-if value="{{{{showChips}}}}" hint-placeholder-val="{{{{ true }}}}">
              {hint}
              <div style="display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 6px; margin-top: 14px; padding: 0 {'0' if kind == 'tg' else '16px'} 0 24px">
                <sc-for list="{{{{chips}}}}" as="ch" hint-placeholder-count="4">{chip}</sc-for>
              </div>
            </sc-if>'''


def tg_screen():
    header = '''<div style="display: flex; align-items: center; gap: 10px; height: 54px; padding: 0 12px 0 4px; box-sizing: border-box; flex-shrink: 0; background: #17202B">
          <span style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; color: #7FC1FF"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"></path></svg></span>
          <div style="display: flex; flex-direction: column; flex-grow: 1; min-width: 0; line-height: 1.25">
            <span style="font-size: 16px; font-weight: 600">M8</span>
            <span style="font-size: 13px; color: {{tgSub.c}}">{{tgSub.t}}</span>
          </div>
          ''' + GLYPH(38, 19) + '''
        </div>'''
    composer = '''<div style="display: flex; align-items: center; gap: 8px; padding: 7px 8px 6px 8px; flex-shrink: 0; background: #17202B">
          <span style="height: 34px; padding: 0 12px; border-radius: 17px; background: #2A4A6B; color: #E9EEF3; display: flex; align-items: center; font-size: 14px; font-weight: 600">Menu</span>
          <sc-if value="{{typingYou}}" hint-placeholder-val="{{ false }}"><span style="flex-grow: 1; height: 38px; border-radius: 19px; padding: 0 14px; background: #10161F; color: #E9EEF3; display: flex; align-items: center; gap: 8px; font-size: 15px"><span class="lp-rec" style="width: 8px; height: 8px; border-radius: 50%; background: #FF5C5C"></span>0:05<span style="margin-left: auto; color: #8A98A8; font-size: 14px">‹ Slide to cancel</span></span></sc-if>
          <sc-if value="{{notTypingYou}}" hint-placeholder-val="{{ true }}"><span style="flex-grow: 1; height: 38px; border-radius: 19px; padding: 0 14px; background: #10161F; color: #6E7C8B; display: flex; align-items: center; font-size: 15px">Message</span></sc-if>
          <span style="width: 38px; height: 38px; flex-shrink: 0; border-radius: 19px; display: flex; align-items: center; justify-content: center; background: {{tgMic.bg}}; color: {{tgMic.fg}}">''' + ico(I_MIC, 22) + '''</span>
        </div>'''
    return f'''<div style="height: 100%; display: flex; flex-direction: column; background: #10161F; color: #E9EEF3; font-family: {TG_FONT}; font-size: 15px; line-height: 1.38">
        {status_bar('#17202B', '#FFFFFF')}
        {header}
        {scroll(thread('tg'), '10px 8px 12px 8px')}
        {composer}
        {home_bar('#17202B')}
      </div>'''


# ------------------------------------------------------------------ Discord chrome
DC_FONT = "'gg sans', 'Noto Sans', Whitney, 'Helvetica Neue', system-ui, sans-serif"
DC_APP = '<span style="display: inline-flex; align-items: center; height: 15px; padding: 0 4px; border-radius: 4px; background: #5865F2; color: #FFFFFF; font-size: 10px; font-weight: 600; line-height: 15px; letter-spacing: 0.02em; flex-shrink: 0">APP</span>'
DC_DIVIDER = '''<div style="display: flex; align-items: center; gap: 8px; margin: 4px 16px 0 16px">
              <div style="flex-grow: 1; height: 1px; background: #3F4147"></div><span style="font-size: 12px; font-weight: 600; color: #949BA4">October 7, 2026</span><div style="flex-grow: 1; height: 1px; background: #3F4147"></div>
            </div>'''
DC_NOTE = '<span style="align-self: center; margin-top: 8px; padding: 0 24px; font-size: 12px; font-style: italic; color: #949BA4; text-align: center">Last trade closed 2:20 PM. No activity for 2h, so M8 checks in.</span>'
YOU_AV = '<svg width="40" height="40" viewBox="0 0 40 40" aria-hidden="true" style="flex-shrink: 0; display: block"><circle cx="20" cy="20" r="20" fill="#F0B232"></circle><text x="20" y="26" text-anchor="middle" font-family="gg sans, Noto Sans, sans-serif" font-size="17" font-weight="700" fill="#15140E">Y</text></svg>'


def dc_group(who, t, body, top=14, cls='lp-bub'):
    av = GLYPH(40, 20) if who == 'm8' else YOU_AV
    name = 'M8' if who == 'm8' else 'you'
    badge = DC_APP if who == 'm8' else ''
    return f'''<div class="{cls}" style="display: flex; gap: 12px; margin-top: {top}px; padding: 2px 16px">
              {av}
              <div style="display: flex; flex-direction: column; min-width: 0; flex-grow: 1">
                <div style="display: flex; align-items: center; gap: 6px; height: 22px"><span style="font-size: 16px; font-weight: 600; color: #F2F3F5">{name}</span>{badge}<span style="font-size: 12px; color: #949BA4; margin-left: 2px">Today at {t}</span></div>
                <div style="font-size: 15px; line-height: 1.375; color: #DBDEE1; overflow-wrap: anywhere">{body}</div>
              </div>
            </div>'''


def dc_follow(body, top=6):
    return f'<div class="lp-bub" style="margin-top: {top}px; padding: 2px 16px 2px 68px; font-size: 15px; line-height: 1.375; color: #DBDEE1; overflow-wrap: anywhere">{body}</div>'


BTN_BG = {'primary': '#5865F2', 'secondary': '#4E5058'}


def dc_btn(label, kind='secondary', link=False, handler=None):
    ext = f'<span style="display: flex; opacity: 0.85">{ico(I_EXT, 13, sw=2.4)}</span>' if link else ''
    h = f' onClick="{{{{{handler}}}}}"' if handler else ''
    return f'<button class="tm-press"{h} style="height: 34px; padding: 0 12px; border: none; border-radius: 8px; background: {BTN_BG[kind]}; color: #FFFFFF; font-family: inherit; font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; white-space: nowrap; cursor: pointer">{label}{ext}</button>'


def dc_row(*bs):
    return f'<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 8px">{"".join(bs)}</div>'


def dc_embed(inner, color='{{accent}}'):
    return f'<div style="display: flex; margin-top: 6px; border-radius: 4px; overflow: hidden; background: #2B2D31; border: 1px solid #26272B"><div style="width: 4px; flex-shrink: 0; background: {color}"></div><div style="display: flex; flex-direction: column; gap: 6px; padding: 9px 12px 12px 11px; min-width: 0; flex-grow: 1">{inner}</div></div>'


def e_title(t):
    return f'<span style="font-size: 15px; font-weight: 700; line-height: 1.3; color: #F2F3F5">{t}</span>'


def e_desc(t):
    return f'<div style="font-size: 13.5px; line-height: 1.375; color: #DBDEE1">{t}</div>'


def e_fields(fields, cols=3):
    cells = ''.join(f'<div style="display: flex; flex-direction: column; gap: 1px; min-width: 0"><span style="font-size: 13px; font-weight: 700; color: #F2F3F5">{n}</span><span style="font-size: 13.5px; line-height: 1.375; color: #DBDEE1">{v}</span></div>' for n, v in fields)
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 6px 10px">{cells}</div>'


E_FOOT = f'<div style="display: flex; align-items: center; gap: 6px; margin-top: 2px; font-size: 12px; font-weight: 500; color: #949BA4">{GLYPH(18, 9)}<span>TrenchM8 · journaled by M8</span></div>'

DC_VOICE = f'''<div style="display: flex; align-items: center; gap: 9px; width: 240px; max-width: 100%; box-sizing: border-box; margin-top: 4px; padding: 7px 11px 7px 7px; border-radius: 22px; background: #2B2D31; border: 1px solid #26272B">
                  <span style="width: 30px; height: 30px; flex-shrink: 0; border-radius: 15px; background: #5865F2; display: flex; align-items: center; justify-content: center"><svg width="11" height="13" viewBox="0 0 12 14" aria-hidden="true"><path d="M1 1.5v11a1 1 0 0 0 1.5.86l9-5.5a1 1 0 0 0 0-1.72l-9-5.5A1 1 0 0 0 1 1.5z" fill="#FFFFFF"></path></svg></span>
                  <div aria-hidden="true" style="display: flex; align-items: center; gap: 2px; height: 26px; flex-grow: 1; min-width: 0; overflow: hidden">{WAVE_DC}</div>
                  <span style="flex-shrink: 0; font-size: 12px; font-weight: 500; color: #DBDEE1">0:07</span>
                </div>'''

DC_JOURNAL = dc_embed(e_title('Today&#39;s journal') +
                      e_desc('<b>Morning +$609.</b> 6 trades, sized small, took profit into strength.') +
                      e_desc('<b>$WIFHAT -$221.</b> FOMO: bought after a +180% candle.') +
                      e_desc('<b>$PEPU2 -$154.</b> Revenge: 4 min after closing $WIFHAT red, at 2x your normal size.') +
                      e_desc('<i>"they were pumping and I didn&#39;t want to miss out."</i>') + E_FOOT)

ANS_DC = {
    'week': dc_group('m8', '4:31 PM', 'Your week: <b>up $816 on 31 trades</b>, best week this month.'
                     f'<div style="width: 262px; margin-top: 6px; border-radius: 8px; overflow: hidden">{recap(262)}</div>'
                     + dc_row(dc_btn('Share card'), dc_btn('Full recap', link=True))),
    'tilt': dc_group('m8', '4:31 PM', 'Heads up from today:' + dc_embed(
        e_title('Same move as Sep 18') +
        e_fields([('Today', '$PEPU2, 4 min after closing $WIFHAT red, 2x your normal size: <span style="color: #FF6B6B">-$154</span>'),
                  ('Sep 18', '$PEPU, 2 min after a loss, 2.5x size: <span style="color: #FF6B6B">-$188</span>')], cols=1) + E_FOOT, color='#F23F43'))
            + dc_follow('Want a 20 min cooldown after red trades? I&#39;ll ping you if you break it.' + dc_row(dc_btn('Set 20 min cooldown', 'primary'), dc_btn('Not now'))),
    'calls': dc_group('m8', '4:31 PM', '<b>No calls, ever.</b> Ask about a coin and you get facts, not a verdict:' + dc_embed(
        e_title('$FROGZ · not a call') + e_fields([('Age', '41 min'), ('Liquidity', '$86k'), ('Top 10 hold', '38%')]) +
        e_desc('Your best setup is coins under 1h old at normal size. Your call.') + E_FOOT)),
    'degen': dc_group('m8', '4:31 PM', '<div style="font-size: 12.5px; color: #949BA4; margin-bottom: 2px">Blunt degen voice · switch with <span style="padding: 0 2px; border-radius: 3px; background: rgba(88,101,242,0.3); color: #C9CDFB; font-weight: 500">/voice</span></div>8 trades, +$234. morning was clean, then you gave back $375 on two coins after lunch. what happened, be honest'),
    'cta': dc_follow('Want me to text you after your next session? Pick where:' + dc_row(dc_btn(f'{DC_ICON(16)}Discord', 'primary', handler='startDc'), dc_btn(f'{TG_ICON(16)}Telegram', handler='startTg'))),
}


def dc_chip():
    return '''<button class="lp-chip" onClick="{{ch.pick}}" style="--tm-d: {{ch.d}}; height: 34px; padding: 0 13px; border: none; border-radius: 8px; background: #4E5058; color: #FFFFFF; font-family: inherit; font-size: 14px; font-weight: 600; box-shadow: 0 2px 0 rgba(0,0,0,0.28), inset 0 1px 0 rgba(255,255,255,0.06); white-space: nowrap">{{ch.label}}</button>'''


def dc_screen():
    header = f'''<div style="display: flex; align-items: center; gap: 8px; height: 52px; padding: 0 8px 0 4px; box-sizing: border-box; flex-shrink: 0; background: #313338; border-bottom: 1px solid #1F2023">
          <span style="width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; color: #B5BAC1">{ico('<path d="M19 12H5"></path><path d="M12 19l-7-7 7-7"></path>', 22)}</span>
          <div style="position: relative; width: 30px; height: 30px; flex-shrink: 0">{GLYPH(30, 15)}<span style="position: absolute; right: -3px; bottom: -3px; width: 9px; height: 9px; border-radius: 50%; background: #23A55A; border: 3px solid #313338"></span></div>
          <div style="display: flex; align-items: center; gap: 6px; flex-grow: 1; min-width: 0; padding-left: 4px"><span style="font-size: 17px; font-weight: 700; color: #F2F3F5">M8</span>{DC_APP}</div>
          <span style="width: 38px; height: 38px; display: flex; align-items: center; justify-content: center; color: #B5BAC1">{ico('<circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.35-4.35"></path>', 20)}</span>
        </div>'''
    composer = f'''<div style="display: flex; flex-direction: column; flex-shrink: 0; background: #313338">
          <sc-if value="{{{{typingM8}}}}" hint-placeholder-val="{{{{ false }}}}"><div style="display: flex; align-items: center; gap: 8px; padding: 0 16px 4px 16px; font-size: 13px; color: #DBDEE1"><span style="display: flex; gap: 3px; color: #DBDEE1; zoom: 0.85">{DOTS3}</span><span><b style="color: #F2F3F5">M8</b> is typing…</span></div></sc-if>
          <div style="display: flex; align-items: center; gap: 8px; padding: 6px 12px 6px 12px">
            <span style="width: 38px; height: 38px; flex-shrink: 0; border-radius: 19px; background: #383A40; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico('<path d="M12 5v14"></path><path d="M5 12h14"></path>', 22, sw=2.4)}</span>
            <sc-if value="{{{{typingYou}}}}" hint-placeholder-val="{{{{ false }}}}">
              <div style="flex-grow: 1; min-width: 0; height: 38px; box-sizing: border-box; padding: 0 14px; border-radius: 19px; background: #383A40; display: flex; align-items: center; gap: 8px; font-size: 15px; color: #DBDEE1"><span class="lp-rec" style="width: 8px; height: 8px; border-radius: 50%; background: #F23F43"></span>Recording… <span style="margin-left: auto; color: #949BA4">0:05</span></div>
            </sc-if>
            <sc-if value="{{{{notTypingYou}}}}" hint-placeholder-val="{{{{ true }}}}">
              <div style="flex-grow: 1; min-width: 0; height: 38px; box-sizing: border-box; padding: 0 14px; border-radius: 19px; background: #383A40; display: flex; align-items: center; font-size: 15px; color: #949BA4">Message @M8</div>
            </sc-if>
            <span style="width: 38px; height: 38px; flex-shrink: 0; border-radius: 19px; background: {{{{dcMic}}}}; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico(I_MIC, 20)}</span>
          </div>
        </div>'''
    return f'''<div style="height: 100%; display: flex; flex-direction: column; background: #313338; color: #DBDEE1; font-family: {DC_FONT}; font-size: 15px; line-height: 1.375">
        {status_bar('#313338', '#FFFFFF')}
        {header}
        {scroll(thread('dc'), '10px 0 12px 0')}
        {composer}
        {home_bar('#313338')}
      </div>'''


def phone():
    return f'''<div style="zoom: {{{{ph.zoom}}}}; position: relative; width: 360px; height: 800px; flex-shrink: 0; border-radius: 52px; overflow: hidden; background: #000000; box-shadow: 0 0 0 11px #0D0D10, 0 0 0 13px #4A4A52, 0 0 0 13.5px rgba(255,255,255,0.08), 0 24px 48px {{{{ph.s1}}}}, 0 64px 128px {{{{ph.s2}}}}" role="img" aria-label="M8 texting you on {{{{chanName}}}}">
      <sc-if value="{{{{isTg}}}}" hint-placeholder-val="{{{{ true }}}}">{tg_screen()}</sc-if>
      <sc-if value="{{{{isDc}}}}" hint-placeholder-val="{{{{ false }}}}">{dc_screen()}</sc-if>
    </div>'''


def toggle():
    seg = lambda key, label, icon: f'''<button class="tm-press" role="tab" aria-selected="{{{{chan.{key}On}}}}" onClick="{{{{chan.{key}}}}}" style="height: 38px; padding: 0 16px; border: none; border-radius: 999px; background: {{{{chan.{key}Bg}}}}; color: {{{{chan.{key}Fg}}}}; display: flex; align-items: center; justify-content: center; gap: 8px; font-family: inherit; font-size: 14px; font-weight: 800; cursor: pointer">{icon}{label}</button>'''
    return f'''<div role="tablist" aria-label="Where M8 texts you" style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2px; padding: 4px; border-radius: 999px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}">
        {seg('tg', 'Telegram', TG_ICON(18))}
        {seg('dc', 'Discord', DC_ICON(18))}
      </div>'''


# ------------------------------------------------------------------ atmosphere ("night chart glow")
CURVE = 'M-20 640 C 120 610, 200 560, 300 520 S 470 430, 560 440 S 700 360, 800 300 S 980 250, 1060 300 S 1200 420, 1300 470 S 1420 520, 1480 540'


def atmosphere():
    return f'''<div aria-hidden="true" style="position: absolute; inset: 0; overflow: hidden; pointer-events: none">
      <div style="position: absolute; left: {{{{atm.hazeX}}}}; top: {{{{atm.hazeY}}}}; width: {{{{atm.hazeW}}}}; height: {{{{atm.hazeW}}}}; border-radius: 50%; background: radial-gradient(closest-side, {{{{atm.haze}}}}, {{{{atm.hazeEdge}}}}); filter: blur(30px)"></div>
      <svg width="1440" height="900" viewBox="0 0 1440 900" style="position: absolute; left: {{{{atm.lineX}}}}; top: 0; opacity: {{{{atm.lineOp}}}}; -webkit-mask-image: {{{{atm.mask}}}}; mask-image: {{{{atm.mask}}}}">
        <path d="{CURVE}" fill="none" stroke="{{{{accent}}}}" stroke-width="18" stroke-linecap="round" style="filter: blur(22px)"></path>
        <path d="{CURVE}" fill="none" stroke="{{{{accent}}}}" stroke-width="1.5" stroke-linecap="round" stroke-opacity="0.55"></path>
      </svg>
      <svg width="100%" height="100%" style="position: absolute; inset: 0; opacity: {{{{atm.grain}}}}; mix-blend-mode: {{{{atm.blend}}}}"><filter id="lp-grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"></feTurbulence><feColorMatrix type="saturate" values="0"></feColorMatrix></filter><rect width="100%" height="100%" filter="url(#lp-grain)"></rect></svg>
      <div style="position: absolute; inset: 0; background: radial-gradient(120% 90% at 62% 38%, {{{{atm.clear}}}} 45%, {{{{c.bg}}}} 100%)"></div>
      <div style="position: absolute; left: 0; right: 0; bottom: 0; height: 160px; background: linear-gradient({{{{atm.clear}}}}, {{{{c.bg}}}})"></div>
    </div>'''


# ------------------------------------------------------------------ page pieces
BTN = 'height: 56px; padding: 0 24px 0 16px; box-sizing: border-box; border-radius: 999px; display: flex; align-items: center; justify-content: center; gap: 10px; font-size: 16px; font-weight: 800; text-decoration: none; white-space: nowrap; width: {{cta.w}}'


def ctas(price=True, center=False):
    p = '<span style="font-size: 14px; font-weight: 600; color: {{c.text3}}">Free for 7 days. Then $20 / 30 days in USDC.</span>' if price else ''
    return f'''<div style="display: flex; flex-direction: column; align-items: {{{{cta.{'calign' if center else 'align'}}}}}; gap: 14px; width: {{{{cta.wrapW}}}}">
        <div style="display: flex; flex-direction: {{{{cta.dir}}}}; gap: 10px; width: {{{{cta.wrapW}}}}">
          <a class="tm-press" href="https://t.me/" onClick="{{{{startTg}}}}" data-tip="Opens M8 in Telegram" data-tip-pos="bottom" style="{BTN}; background: {{{{accent}}}}; color: #15140E">{TG_ICON()}Start on Telegram</a>
          <a class="tm-press" href="https://discord.com/" onClick="{{{{startDc}}}}" data-tip="Adds the M8 app on Discord" data-tip-pos="bottom" style="{BTN}; background: {{{{c.surface}}}}; color: {{{{c.text}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}">{DC_ICON()}Start on Discord</a>
        </div>
        {p}
      </div>'''


def nav():
    link = 'min-height: 44px; padding: 0 14px; display: flex; align-items: center; font-size: 14px; font-weight: 700; color: {{c.text2}}; text-decoration: none'
    return f'''<div style="position: sticky; top: 0; z-index: 60; width: 100%; box-sizing: border-box; display: flex; justify-content: center; padding: {{{{nav.pad}}}}">
    <div ref="{{{{setSentinel}}}}" aria-hidden="true" style="position: absolute; top: 0; left: 0; width: 1px; height: 1px"></div>
    <header style="width: {{{{nav.w}}}}; max-width: 100%; height: {{{{nav.h}}}}; box-sizing: border-box; padding: 0 {{{{nav.inPad}}}}; display: flex; align-items: center; justify-content: space-between; border-radius: {{{{nav.r}}}}; background: {{{{nav.bg}}}}; box-shadow: {{{{nav.shadow}}}}; backdrop-filter: {{{{nav.blur}}}}; -webkit-backdrop-filter: {{{{nav.blur}}}}; transition: background-color .25s ease, box-shadow .25s ease">
      <a class="tm-hover" href="#top" style="display: flex; align-items: center; gap: 10px; color: {{{{c.text}}}}; text-decoration: none">{GLYPH(32)}<span style="font-size: 18px; font-weight: 800; letter-spacing: -0.01em">TrenchM8</span></a>
      <nav aria-label="Main" style="display: flex; align-items: center; gap: 2px">
        <sc-if value="{{{{desktop}}}}" hint-placeholder-val="{{{{ true }}}}">
          <a class="tm-hover" href="#how" style="{link}">How it works</a>
          <a class="tm-hover" href="#pricing" style="{link}">Pricing</a>
          <a class="tm-hover" href="#login" style="{link}">Log in</a>
        </sc-if>
        <a class="tm-press" href="#top" onClick="{{{{startTop}}}}" style="margin-left: 8px; height: 40px; padding: 0 18px; border-radius: 999px; display: flex; align-items: center; font-size: 14px; font-weight: 800; color: #15140E; background: {{{{accent}}}}; text-decoration: none">Start free</a>
      </nav>
    </header>
  </div>'''


WORDS = [('M8', 0), ('texts', 1), ('you.', 2), ('<br>', None), ('You', 3), ('reply.', 4), ('<br>', None), ('Journal', 5), ('done.', 6)]


def h1():
    out = []
    for w, i in WORDS:
        if i is None:
            out.append('<br>')
        else:
            out.append(f'<span class="lp-word" style="--tm-d: {0.08 + i * 0.11:.2f}s">{w}</span>')
    return ' '.join(out).replace(' <br> ', '<br>')


def hero():
    return f'''  <section id="top" style="position: relative; width: 100%; display: flex; justify-content: center; padding: {{{{hero.pad}}}}; box-sizing: border-box">
    {atmosphere()}
    <div style="position: relative; width: 1200px; max-width: 100%; display: flex; flex-direction: {{{{hero.dir}}}}; align-items: center; justify-content: space-between; gap: {{{{hero.gap}}}}">
      <div style="display: flex; flex-direction: column; gap: 26px; max-width: 600px; width: {{{{hero.textW}}}}">
        <span class="tm-in" style="align-self: flex-start; padding: 7px 12px; border-radius: 16px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}; font-size: 13px; font-weight: 700; color: {{{{c.text2}}}}">{{{{eyebrow}}}}</span>
        <h1 style="margin: 0; font-size: {{{{hero.h1}}}}; line-height: 0.98; font-weight: 800; letter-spacing: -0.045em">{h1()}</h1>
        <p class="tm-fade" style="--tm-d: .7s; margin: 0; max-width: 540px; font-size: {{{{hero.sub}}}}; line-height: 1.5; font-weight: 500; color: {{{{c.text2}}}}">M8 watches your wallets. About 2 hours after your last trade, it texts you on Telegram or Discord. Reply by text or voice, and your trading journal writes itself.</p>
        <div class="tm-fade" style="--tm-d: .85s">{ctas()}</div>
      </div>
      <div style="display: flex; flex-direction: column; align-items: center; gap: 30px; flex-shrink: 0; padding: 14px">
        {toggle()}
        {phone()}
      </div>
    </div>
  </section>'''


def marker(n):
    return f'<span style="font-size: 15px; font-weight: 700; color: {{{{c.text3}}}}; font-variant-numeric: tabular-nums">({n})</span>'


def facts(*items):
    li = ''.join(f'<span style="padding: 6px 11px; border-radius: 999px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}; font-size: 13px; font-weight: 700; color: {{{{c.text2}}}}">{t}</span>' for t in items)
    return f'<div style="display: flex; flex-wrap: wrap; gap: 8px">{li}</div>'


ROWS = {
    1: ('It texts you after you trade.',
        'Paste a wallet once. M8 tracks every trade on Solana, Base, BNB and Robinhood Chain. About 2 hours after your last trade, it texts you on Telegram or Discord. Reply however you like, a few words or a voice note.',
        facts('Read-only, nothing to sign', 'Up to 5 wallets', 'Text or voice')),
    2: ('Your journal writes itself.',
        'Your reply becomes the day&#39;s entry, in your own words. M8 adds its take, tags every trade and keeps the receipts. Change anything by hand, or just tell M8.',
        facts('In your words', 'M8&#39;s take, separate', 'Edit with Undo')),
    3: ('It catches your patterns.',
        'Once, while you&#39;re still in it: same move as Sep 18, 2 min after a loss. And over weeks, where your edge is and where it leaks: +$2,910 on coins under 1 hour old, -$1,626 on everything older.',
        facts('One live check-in per session', 'Always with receipts', 'Never a call')),
    4: ('Mornings and Sundays.',
        'A morning brief with what moved overnight on your chains and the one thing to remember from yesterday. On Sunday, your week on a card worth sharing.',
        facts('8 AM your time', 'Mute anytime', 'Shareable recap card')),
}


def row_text(n, w):
    h, p, f = ROWS[n]
    return f'''<div style="display: flex; flex-direction: column; gap: 18px; width: {w}">
        {marker(n)}
        <h2 style="margin: 0; font-size: {{{{row.h2}}}}; line-height: 1.04; font-weight: 800; letter-spacing: -0.035em">{h}</h2>
        <p style="margin: 0; font-size: {{{{row.p}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">{p}</p>
        {f}
      </div>'''


def visuals(mobile):
    if not mobile:
        v1 = f'<div style="display: flex; gap: 20px; align-items: flex-start">{captioned(clip("TgNudge", 0, 57, 390, 266, 0.95), "Telegram")}{captioned(clip("DcNudge", 0, 44, 390, 266, 0.95, bg="#313338"), "Discord")}</div>'
        v2 = clip('Desktop', 4, 76, 1432, 824, 0.838, radius=24)
        v3 = f'<div style="display: flex; gap: 20px; align-items: flex-start">{captioned(clip("TgRepeat", 0, 100, 390, 318, 0.95), "Live, mid-session")}{captioned(clip("Stats", 24, 1071, 453, 327, 0.81, bg="{{c.bg}}"), "Over weeks, on the web")}</div>'
        v4 = f'<div style="display: flex; gap: 20px; align-items: flex-start">{captioned(clip("TgMorning", 0, 64, 390, 660, 0.9), "8:00 AM")}{captioned(f"<div class=\"lp-shot\" style=\"border-radius: 20px; overflow: hidden\">{recap(370)}</div>", "Sunday, 6:00 PM")}</div>'
    else:
        v1 = f'<div style="display: flex; flex-direction: column; gap: 20px">{captioned(clip("TgNudge", 0, 57, 390, 266, 0.918), "Telegram")}{captioned(clip("DcNudge", 0, 44, 390, 266, 0.918, bg="#313338"), "Discord")}</div>'
        v2 = clip('Main', 0, 0, 390, 916, 0.918, radius=24)
        v3 = f'<div style="display: flex; flex-direction: column; gap: 20px">{captioned(clip("TgRepeat", 0, 100, 390, 318, 0.918), "Live, mid-session")}{captioned(clip("Stats", 24, 1071, 453, 327, 0.79, bg="{{c.bg}}"), "Over weeks, on the web")}</div>'
        v4 = f'<div style="display: flex; flex-direction: column; gap: 20px">{captioned(clip("TgMorning", 0, 64, 390, 660, 0.918), "8:00 AM")}{captioned(f"<div class=\"lp-shot\" style=\"border-radius: 20px; overflow: hidden\">{recap(358)}</div>", "Sunday, 6:00 PM")}</div>'
    return v1, v2, v3, v4


def rows():
    d1, d2, d3, d4 = visuals(False)
    m1, m2, m3, m4 = visuals(True)
    line = 'border-top: 1px solid {{c.line}}'
    desk = f'''<sc-if value="{{{{desktop}}}}" hint-placeholder-val="{{{{ true }}}}">
    <div style="width: 1200px; display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: 96px 0; {line}">{row_text(1, '400px')}{d1}</div>
    <div style="width: 1200px; display: flex; flex-direction: column; gap: 48px; padding: 96px 0; {line}">
      <div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px">
        <div style="display: flex; flex-direction: column; gap: 18px; width: 560px">{marker(2)}<h2 style="margin: 0; font-size: {{{{row.h2}}}}; line-height: 1.04; font-weight: 800; letter-spacing: -0.035em">{ROWS[2][0]}</h2></div>
        <div style="display: flex; flex-direction: column; gap: 18px; width: 520px"><p style="margin: 0; font-size: {{{{row.p}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">{ROWS[2][1]}</p>{ROWS[2][2]}</div>
      </div>
      {d2}
    </div>
    <div style="width: 1200px; display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: 96px 0; {line}">{d3}{row_text(3, '400px')}</div>
    <div style="width: 1200px; display: flex; align-items: center; justify-content: space-between; gap: 40px; padding: 96px 0; {line}">{row_text(4, '400px')}{d4}</div>
    </sc-if>'''
    mob = f'''<sc-if value="{{{{mobile}}}}" hint-placeholder-val="{{{{ false }}}}">
    <div style="width: 100%; display: flex; flex-direction: column; gap: 28px; padding: 64px 0; {line}">{row_text(1, '100%')}{m1}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 28px; padding: 64px 0; {line}">{row_text(2, '100%')}{m2}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 28px; padding: 64px 0; {line}">{row_text(3, '100%')}{m3}</div>
    <div style="width: 100%; display: flex; flex-direction: column; gap: 28px; padding: 64px 0; {line}">{row_text(4, '100%')}{m4}</div>
    </sc-if>'''
    return f'''  <section id="how" style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{{{sec.pad}}}}; display: flex; flex-direction: column; align-items: center">
    {desk}
    {mob}
  </section>'''


def founder():
    return f'''  <section style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{{{founder.pad}}}}; display: flex; justify-content: center">
    <figure style="margin: 0; width: 760px; max-width: 100%; box-sizing: border-box; padding: {{{{founder.inPad}}}}; border-radius: 28px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}; display: flex; flex-direction: column; gap: 22px">
      <div style="display: flex; align-items: center; justify-content: space-between; gap: 12px">
        <span style="font-size: 13px; font-weight: 800; color: {{{{c.text3}}}}">A note from the founder</span>
        <span style="padding: 4px 10px; border-radius: 999px; border: 1px dashed {{{{c.text3}}}}; font-size: 12px; font-weight: 700; color: {{{{c.text3}}}}">Draft: Josh to rewrite</span>
      </div>
      <blockquote style="margin: 0; display: flex; flex-direction: column; gap: 16px; font-size: {{{{founder.size}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text}}}}">
        <p style="margin: 0">Every trader knows a journal would help. Almost nobody keeps one, because writing it up after a long session is the last thing anyone feels like doing.</p>
        <p style="margin: 0">So M8 does the writing. It watches the wallets, texts once the session is over, and turns a quick reply into the journal you meant to keep. It won&#39;t tell you what to buy. It just makes sure you remember what you did, and why.</p>
      </blockquote>
      <figcaption style="display: flex; align-items: center; gap: 12px">{GLYPH(36, 18)}<span style="display: flex; flex-direction: column"><span style="font-size: 15px; font-weight: 800">Josh, founder</span><span style="font-size: 13px; font-weight: 600; color: {{{{c.text3}}}}">TrenchM8</span></span></figcaption>
    </figure>
  </section>'''


def pricing():
    plan = lambda price, per, note, hi: f'''<div style="flex: 1 1 0; min-width: 0; padding: 22px 22px 20px 22px; border-radius: 22px; background: {{{{c.bg}}}}; box-shadow: inset 0 0 0 {('2px {{accent}}' if hi else '1px {{c.line}}')}; display: flex; flex-direction: column; gap: 6px">
          <span style="font-size: 34px; font-weight: 800; letter-spacing: -0.03em">{price}<span style="font-size: 16px; font-weight: 700; color: {{{{c.text3}}}}; letter-spacing: 0"> / {per}</span></span>
          <span style="font-size: 14px; font-weight: 600; color: {{{{c.text2}}}}">{note}</span>
        </div>'''
    return f'''  <section id="pricing" style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{{{price.pad}}}}; display: flex; justify-content: center">
    <div style="width: 760px; max-width: 100%; display: flex; flex-direction: column; gap: 24px">
      <div style="display: flex; flex-direction: column; gap: 12px">
        <h2 style="margin: 0; font-size: {{{{row.h2}}}}; line-height: 1.04; font-weight: 800; letter-spacing: -0.035em">One price. All in.</h2>
        <p style="margin: 0; font-size: {{{{row.p}}}}; line-height: 1.55; font-weight: 500; color: {{{{c.text2}}}}">7 days free, no card. Then pay in USDC on Solana. No auto-renew: M8 reminds you 3 days before it runs out.</p>
      </div>
      <div style="padding: 8px; border-radius: 30px; background: {{{{c.surface}}}}; box-shadow: inset 0 0 0 1px {{{{c.line}}}}; display: flex; flex-direction: {{{{price.dir}}}}; gap: 8px">
        {plan('$0', '7 days', 'The full trial. Starts when you add a wallet.', False)}
        {plan('$20', '30 days', 'Everything, for a month.', True)}
        {plan('$50', '90 days', 'Everything, for three months. Saves $10.', False)}
      </div>
    </div>
  </section>'''


def closing():
    return f'''  <section style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{{{close.pad}}}}; display: flex; flex-direction: column; align-items: {{{{close.align}}}}; gap: 28px; text-align: {{{{close.textAlign}}}}">
    <h2 style="margin: 0; font-size: {{{{close.h2}}}}; line-height: 1.0; font-weight: 800; letter-spacing: -0.045em">Your journal<span style="display: {{{{close.brM}}}}"><br></span> starts<span style="display: {{{{close.br}}}}"><br></span> with<span style="display: {{{{close.brM}}}}"><br></span> one text.</h2>
    {ctas(center=True)}
  </section>'''


def footer():
    return '''  <footer style="width: 1200px; max-width: 100%; box-sizing: border-box; padding: {{foot.pad}}; display: flex; flex-direction: {{foot.dir}}; align-items: {{foot.align}}; justify-content: space-between; gap: 16px; font-size: 13px; font-weight: 600; color: {{c.text3}}; border-top: 1px solid {{c.line}}">
    <span>Not financial advice. M8 never makes calls.</span>
    <div style="display: flex; gap: 20px"><a class="tm-hover" href="#terms" style="color: {{c.text3}}; text-decoration: none">Terms</a><a class="tm-hover" href="#privacy" style="color: {{c.text3}}; text-decoration: none">Privacy</a></div>
  </footer>'''


SCRIPT = r'''class Component extends DCLogic {
  componentDidMount() {
    this._timers = [];
    const reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (!(this.state && this.state.step != null)) {
      if (reduce) this.setState({ step: 6 });
      else {
        // The opening conversation, about 6s: nudge, your voice note, M8 logs it, then reply chips.
        this.later(350, () => this.setState({ step: 1 }));
        this.later(1450, () => this.setState({ typingYou: true }));
        this.later(2650, () => this.setState({ step: 3, typingYou: false }));
        this.later(3250, () => this.setState({ typingM8: true }));
        this.later(4550, () => this.setState({ step: 5, typingM8: false }));
        this.later(5350, () => this.setState({ step: 6 }));
      }
    }
    this._onScroll = () => { const g = (window.scrollY || 0) > 24; if (g !== !!(this.state || {}).navGlass) this.setState({ navGlass: g }); };
    window.addEventListener('scroll', this._onScroll, { passive: true });
  }
  componentWillUnmount() {
    (this._timers || []).forEach(clearTimeout);
    if (this._onScroll) window.removeEventListener('scroll', this._onScroll);
    if (this._io) this._io.disconnect();
  }
  componentDidUpdate(prev, prevState) {
    // Keep the newest message in view (the thread is column-reverse, so the bottom is scrollTop 0).
    const a = prevState || {}, b = this.state || {};
    if (this._scroll && (a.step !== b.step || (a.log || []).length !== (b.log || []).length || a.typingM8 !== b.typingM8 || a.typingYou !== b.typingYou || a.chan !== b.chan)) {
      this._scroll.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }
  later(ms, fn) { this._timers = this._timers || []; this._timers.push(setTimeout(fn, ms)); }
  renderVals() {
    const st = this.state || {};
    const theme = this.props.theme ?? 'dark';
    const layout = this.props.layout ?? 'desktop';
    const desktop = layout !== 'mobile';
    const accent = this.props.accent ?? '#7CD4FF';
    const themes = {
      dark: { bg: '#0D0E13', surface: '#171922', surface2: '#21242F', line: '#2C303D', text: '#F3F4F7', text2: '#A9AEBE', text3: '#858B9E', tipBg: '#F3F4F7', tipFg: '#12131A', shadow: 'rgba(0,0,0,0.5)', edge: 'rgba(255,255,255,0.06)', glass: 'rgba(33,36,47,0.8)', glassLine: 'rgba(255,255,255,0.08)' },
      light: { bg: '#F4F4F7', surface: '#FFFFFF', surface2: '#EEEFF3', line: '#E3E5EB', text: '#12131A', text2: '#4F5566', text3: '#666C7E', tipBg: '#12131A', tipFg: '#F3F4F7', shadow: 'rgba(18,19,26,0.18)', edge: 'rgba(18,19,26,0.08)', glass: 'rgba(238,239,243,0.8)', glassLine: 'rgba(18,19,26,0.08)' }
    };
    const c = themes[theme] || themes.dark;
    const dark = theme !== 'light';
    const rgba = (hex, a) => { const h = hex.replace('#', ''); const n = parseInt(h.length === 3 ? h.split('').map((x) => x + x).join('') : h, 16); return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')'; };
    const stop = (e) => { if (e && e.preventDefault) e.preventDefault(); };

    // Channel toggle: same conversation, Telegram or Discord chrome.
    const chanKey = st.chan || 'tg';
    const seg = (on) => (on ? { bg: accent, fg: '#15140E' } : { bg: 'transparent', fg: c.text2 });
    const chan = {
      tgOn: String(chanKey === 'tg'), dcOn: String(chanKey === 'dc'),
      tgBg: seg(chanKey === 'tg').bg, tgFg: seg(chanKey === 'tg').fg, dcBg: seg(chanKey === 'dc').bg, dcFg: seg(chanKey === 'dc').fg,
      tg: () => this.setState({ chan: 'tg' }), dc: () => this.setState({ chan: 'dc' })
    };

    // Conversation state. step: 0 empty, 1 nudge, 3 voice note, 5 logged + journal, 6 chips.
    const step = st.step || 0;
    const log = st.log || [];
    const LABELS = { week: 'show me my week', tilt: 'did i tilt today?', calls: 'is this a call group?', degen: 'talk like a degen' };
    const asked = log.filter((x) => x.indexOf('you:') === 0).map((x) => x.slice(4));
    const answered = log.filter((x) => LABELS[x]).length;
    const pick = (id) => () => {
      const s = this.state || {};
      if (s.pending || (s.log || []).indexOf('you:' + id) >= 0) return;
      this.setState({ log: (s.log || []).concat(['you:' + id]), pending: id });
      this.later(500, () => this.setState({ typingM8: true }));
      this.later(1600, () => {
        const s2 = this.state || {};
        const next = (s2.log || []).concat([id]);
        const done = next.filter((x) => LABELS[x]).length;
        const offer = done >= 2 && next.indexOf('cta') < 0;
        this.setState({ log: next, typingM8: offer, pending: offer ? id : null });
        if (offer) this.later(1300, () => this.setState({ log: (this.state.log || []).concat(['cta']), typingM8: false, pending: null }));
      });
    };
    const answers = log.map((x) => {
      const you = x.indexOf('you:') === 0;
      return { you, label: you ? LABELS[x.slice(4)] : '', week: x === 'week', tilt: x === 'tilt', calls: x === 'calls', degen: x === 'degen', cta: x === 'cta' };
    });
    const chips = Object.keys(LABELS).filter((k) => asked.indexOf(k) < 0).map((k, i) => ({ id: k, label: LABELS[k], pick: pick(k), d: (0.05 + i * 0.1).toFixed(2) + 's' }));
    const typingM8 = !!st.typingM8;
    const typingYou = !!st.typingYou;
    const heights = [6, 10, 16, 22, 14, 20, 26, 18, 10, 16, 24, 28, 20, 12, 18, 24, 14, 8, 12, 20, 16, 10, 14, 8, 10, 6, 8, 5, 6, 4];
    const wave = heights.map((h, i) => ({ h: h + 'px', tg: i < 11 ? '#E9EEF3' : 'rgba(233,238,243,0.38)', dc: i < 11 ? '#F2F3F5' : 'rgba(242,243,245,0.32)' }));

    const glass = !!st.navGlass;
    return {
      theme, accent, c, desktop, mobile: !desktop, chan, isTg: chanKey === 'tg', isDc: chanKey === 'dc', chanName: chanKey === 'tg' ? 'Telegram' : 'Discord',
      s1: step >= 1, s3: step >= 3, s5: step >= 5, answers, chips, showChips: step >= 6 && !st.pending && chips.length > 0,
      typingM8, typingYou, notTypingYou: !typingYou, wave,
      tgSub: typingM8 ? { t: 'typing…', c: '#7FC1FF' } : { t: 'bot', c: '#8A98A8' },
      dcMic: typingYou ? '#F23F43' : '#383A40',
      tgMic: typingYou ? { bg: '#3A8EE6', fg: '#FFFFFF' } : { bg: 'transparent', fg: '#8A98A8' },
      startTg: stop, startDc: stop, startTop: stop,
      eyebrow: desktop ? 'For memecoin traders on Solana, Base, BNB and Robinhood Chain' : 'Solana · Base · BNB · Robinhood Chain',
      setScroll: (el) => { this._scroll = el; },
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
        ? { pad: '56px 0 96px 0', dir: 'row', gap: '48px', textW: '600px', h1: '84px', sub: '20px' }
        : { pad: '28px 16px 64px 16px', dir: 'column', gap: '40px', textW: '100%', h1: '52px', sub: '17px' },
      ph: { zoom: desktop ? 1 : 0.88, s1: dark ? 'rgba(0,0,0,0.42)' : 'rgba(18,19,26,0.18)', s2: dark ? 'rgba(0,0,0,0.5)' : 'rgba(18,19,26,0.16)' },
      atm: {
        haze: rgba(accent, dark ? 0.26 : 0.30), hazeEdge: rgba(accent, 0),
        hazeX: desktop ? '760px' : '-90px', hazeY: desktop ? '20px' : '520px', hazeW: desktop ? '680px' : '560px',
        lineX: desktop ? '0px' : '-520px', lineOp: dark ? '0.9' : '0.7',
        mask: desktop ? 'linear-gradient(90deg, transparent 38%, #000 62%)' : 'linear-gradient(180deg, transparent 30%, #000 60%)',
        grain: dark ? '0.07' : '0.05', blend: dark ? 'overlay' : 'multiply', clear: rgba(dark ? '#0D0E13' : '#F4F4F7', 0)
      },
      cta: desktop ? { dir: 'row', w: 'auto', wrapW: 'auto', align: 'flex-start', calign: 'center' } : { dir: 'column', w: '100%', wrapW: '100%', align: 'stretch', calign: 'stretch' },
      row: { h2: desktop ? '48px' : '34px', p: desktop ? '18px' : '16px' },
      sec: { pad: desktop ? '0' : '0 16px' },
      founder: { pad: desktop ? '96px 0' : '64px 16px', inPad: desktop ? '40px 44px' : '24px 22px', size: desktop ? '20px' : '17px' },
      price: { pad: desktop ? '96px 0' : '48px 16px', dir: desktop ? 'row' : 'column' },
      close: desktop ? { pad: '120px 0 128px 0', align: 'center', textAlign: 'center', h2: '84px', br: 'inline', brM: 'none' } : { pad: '72px 16px 80px 16px', align: 'stretch', textAlign: 'left', h2: '48px', br: 'none', brM: 'inline' },
      foot: desktop ? { pad: '32px 0 48px 0', dir: 'row', align: 'center' } : { pad: '28px 16px 40px 16px', dir: 'column', align: 'flex-start' }
    };
  }
}'''


def build():
    props = {"layout": {"editor": "enum", "options": ["desktop", "mobile"], "default": "desktop", "section": "Look"},
             "theme": {"editor": "enum", "options": ["dark", "light"], "default": "dark", "section": "Look"},
             "accent": {"editor": "color", "default": "#7CD4FF", "options": ACCENTS, "section": "Look"},
             "$preview": {"width": 1440, "height": H_DESK}}
    body = '\n'.join([nav(), hero(), rows(), founder(), pricing(), closing(), footer()])
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>TrenchM8 - landing v2, B2: chat-first, refined</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
{HELMET}
<div style="--tm-tip-bg: {{{{c.tipBg}}}}; --tm-tip-fg: {{{{c.tipFg}}}}; --tm-focus: {{{{accent}}}}; --lp-shadow: {{{{c.shadow}}}}; --lp-edge: {{{{c.edge}}}}; width: 100%; box-sizing: border-box; background: {{{{c.bg}}}}; color: {{{{c.text}}}}; font-family: Manrope, system-ui, sans-serif; font-variant-numeric: tabular-nums; -webkit-font-smoothing: antialiased; display: flex; flex-direction: column; align-items: center; overflow: clip">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(props, separators=(",", ":"))}'>
{SCRIPT}
</script>
</body>
</html>
'''
    open(D + 'LandingB2.dc.html', 'w').write(html)
    mob = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>TrenchM8 - landing v2, B2 (mobile)</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width: 390px; min-height: {H_MOB}px; background: {{{{bg}}}}">
  <dc-import name="LandingB2" layout="mobile" theme="{{{{theme}}}}" accent="{{{{accent}}}}" hint-size="390px,{H_MOB}px"></dc-import>
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
    open(D + 'LandingB2Mobile.dc.html', 'w').write(mob)


if __name__ == '__main__':
    build()
    print('ok')
