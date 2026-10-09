# Generates the Discord flow boards (Dc*.dc.html) from shared Discord mobile-dark chrome.
# Usage: python3 build-dc.py [Name=height ...]  (run from anywhere; writes into design/mockups/)
import re, sys, json, os

P = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..') + '/'
ACC = '{{accent}}'
FONT = "'gg sans', 'Noto Sans', Whitney, 'Helvetica Neue', system-ui, sans-serif"
HEIGHTS = {'DcInstall': 1500, 'DcOnboarding': 1900, 'DcNudge': 1500, 'DcRuleAlert': 1200, 'DcMorning': 1000, 'DcAsk': 1300, 'DcRecap': 1300, 'DcRepeat': 1200}
for a in sys.argv[1:]:
    k, v = a.split('='); HEIGHTS[k] = int(v)

ACCENTS = ["#7CD4FF", "#FFD23F", "#6495ED", "#B4A5FF", "#FF85C8", "#FF9152", "#FFB547"]

# ---------- extract the M8-rendered images from the Tg boards so both platforms stay in sync
def extract_img(fname):
    s = open(P + fname).read()
    i = s.index('<div role="img"')
    depth, j = 0, i
    for m in re.finditer(r'<(/?)div\b', s[i:]):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            j = i + m.end(); break
    return s[i:s.index('>', j) + 1]

# ---------- icons
def ico(paths, size=20, color='currentColor', sw=2):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths}</svg>'

I_BACK = '<path d="M19 12H5"></path><path d="M12 19l-7-7 7-7"></path>'
I_PHONE = '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>'
I_SEARCH = '<circle cx="11" cy="11" r="7"></circle><path d="M21 21l-4.35-4.35"></path>'
I_PLUS = '<path d="M12 5v14"></path><path d="M5 12h14"></path>'
I_SMILE = '<circle cx="12" cy="12" r="10"></circle><path d="M8 14s1.5 2 4 2 4-2 4-2"></path><path d="M9 9h.01"></path><path d="M15 9h.01"></path>'
I_GIFT = '<rect x="3" y="8" width="18" height="4" rx="1"></rect><path d="M12 8v13"></path><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"></path><path d="M7.5 8a2.5 2.5 0 0 1 0-5C9 3 12 8 12 8s3-5 4.5-5a2.5 2.5 0 0 1 0 5"></path>'
I_MIC = '<rect x="9" y="2" width="6" height="12" rx="3"></rect><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><path d="M12 19v3"></path>'
I_EXT = '<path d="M15 3h6v6"></path><path d="M10 14L21 3"></path><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>'
I_EYE = '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"></path><circle cx="12" cy="12" r="3"></circle>'
I_DOWN = '<path d="M6 9l6 6 6-6"></path>'
I_UP = '<path d="M18 15l-6-6-6 6"></path>'
I_RIGHT = '<path d="M9 18l6-6-6-6"></path>'
I_CHECK = '<path d="M20 6L9 17l-5-5"></path>'
I_X = '<path d="M18 6L6 18"></path><path d="M6 6l12 12"></path>'
I_USER = '<circle cx="12" cy="8" r="4"></circle><path d="M4 21a8 8 0 0 1 16 0"></path>'
I_SERVER = '<rect x="3" y="4" width="18" height="16" rx="4"></rect><path d="M8 10h8"></path><path d="M8 14h5"></path>'
I_SLASH = '<path d="M15 4L9 20"></path>'
I_LOCK = '<rect x="4" y="11" width="16" height="10" rx="2"></rect><path d="M8 11V7a4 4 0 0 1 8 0v4"></path>'

DISCORD_LOGO = 'M20.317 4.3698a19.7913 19.7913 0 00-4.8851-1.5152.0741.0741 0 00-.0785.0371c-.211.3753-.4447.8648-.6083 1.2495-1.8447-.2762-3.68-.2762-5.4868 0-.1636-.3933-.4058-.8742-.6177-1.2495a.077.077 0 00-.0785-.037 19.7363 19.7363 0 00-4.8852 1.515.0699.0699 0 00-.0321.0277C.5334 9.0458-.319 13.5799.0992 18.0578a.0824.0824 0 00.0312.0561c2.0528 1.5076 4.0413 2.4228 5.9929 3.0294a.0777.0777 0 00.0842-.0276c.4616-.6304.8731-1.2952 1.226-1.9942a.076.076 0 00-.0416-.1057c-.6528-.2476-1.2743-.5495-1.8722-.8923a.077.077 0 01-.0076-.1277c.1258-.0943.2517-.1923.3718-.2914a.0743.0743 0 01.0776-.0105c3.9278 1.7933 8.18 1.7933 12.0614 0a.0739.0739 0 01.0785.0095c.1202.099.246.1981.3728.2924a.077.077 0 01-.0066.1276 12.2986 12.2986 0 01-1.873.8914.0766.0766 0 00-.0407.1067c.3604.698.7719 1.3628 1.225 1.9932a.076.076 0 00.0842.0286c1.961-.6067 3.9495-1.5219 6.0023-3.0294a.077.077 0 00.0313-.0552c.5004-5.177-.8382-9.6739-3.5485-13.6604a.061.061 0 00-.0312-.0286zM8.02 15.3312c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9555-2.4189 2.157-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.9555 2.4189-2.1569 2.4189zm7.9748 0c-1.1825 0-2.1569-1.0857-2.1569-2.419 0-1.3332.9554-2.4189 2.1569-2.4189 1.2108 0 2.1757 1.0952 2.1568 2.419 0 1.3332-.946 2.4189-2.1568 2.4189Z'

# ---------- avatars
def m8_av(size=40, rx=18):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 36 36" aria-hidden="true" style="flex-shrink: 0; display: block"><rect x="0" y="0" width="36" height="36" rx="{rx}" fill="{ACC}"></rect><rect x="11" y="12" width="4.5" height="9" rx="2.25" fill="#15140E"></rect><rect x="20.5" y="12" width="4.5" height="9" rx="2.25" fill="#15140E"></rect></svg>'

def josh_av(size=40):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 40 40" aria-hidden="true" style="flex-shrink: 0; display: block"><circle cx="20" cy="20" r="20" fill="#5865F2"></circle><path transform="translate(9.5 10) scale(0.875)" fill="#FFFFFF" fill-rule="evenodd" d="{DISCORD_LOGO}"></path></svg>'

APP = '<span style="display: inline-flex; align-items: center; height: 15px; padding: 0 4px; border-radius: 4px; background: #5865F2; color: #FFFFFF; font-size: 10px; font-weight: 600; line-height: 15px; letter-spacing: 0.02em; flex-shrink: 0">APP</span>'

# ---------- inline markdown
def code(t):
    return f'<code style="font-family: Consolas, \'Andale Mono WT\', Menlo, monospace; font-size: 0.85em; padding: 1px 4px; border-radius: 4px; background: #2B2D31; border: 1px solid #1E1F22; color: #DBDEE1; white-space: nowrap">{t}</code>'

def cmd(name):  # slash-command mention (</voice:id>)
    return f'<span style="padding: 0 2px; border-radius: 3px; background: rgba(88,101,242,0.3); color: #C9CDFB; font-weight: 500">/{name}</span>'

def quote(inner):
    return f'<div style="display: flex; gap: 0; margin: 2px 0"><div style="width: 4px; flex-shrink: 0; border-radius: 4px; background: #4E5058"></div><div style="padding: 0 8px 0 12px; min-width: 0">{inner}</div></div>'

def sub(t):  # Discord "-#" subtext
    return f'<div style="font-size: 13px; line-height: 1.3; color: #949BA4; margin-top: 2px">{t}</div>'

# ---------- chrome
def header():
    return f'''
  <div style="display: flex; align-items: center; gap: 8px; height: 56px; padding: 0 8px 0 4px; box-sizing: border-box; background: #313338; border-bottom: 1px solid #1F2023; flex-shrink: 0">
    <button class="dc-icon" aria-label="Back" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: transparent; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico(I_BACK, 22)}</button>
    <div style="position: relative; width: 32px; height: 32px; flex-shrink: 0">
      {m8_av(32)}
      <span style="position: absolute; right: -3px; bottom: -3px; width: 10px; height: 10px; border-radius: 50%; background: #23A55A; border: 3px solid #313338"></span>
    </div>
    <div style="display: flex; align-items: center; gap: 6px; flex-grow: 1; min-width: 0; padding-left: 4px">
      <span style="font-size: 17px; font-weight: 700; color: #F2F3F5">M8</span>
      {APP}
      <span style="display: flex; color: #80848E">{ico(I_RIGHT, 16, sw=2.4)}</span>
    </div>
    <button class="dc-icon" aria-label="Start voice call" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: transparent; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico(I_PHONE, 20)}</button>
    <button class="dc-icon" aria-label="Search" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: transparent; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico(I_SEARCH, 20)}</button>
  </div>'''

def composer(inner=None, typing=False):
    pill = inner or '<span style="flex-grow: 1; font-size: 16px; color: #949BA4">Message @M8</span>'
    t = ''
    if typing:
        dot = '<span class="dc-dot" style="width: 6px; height: 6px; border-radius: 50%; background: #DBDEE1"></span>'
        t = f'<div style="display: flex; align-items: center; gap: 8px; padding: 0 16px 6px 16px; font-size: 13px; color: #DBDEE1"><span style="display: flex; gap: 3px">{dot}{dot}{dot}</span><span><b style="color: #F2F3F5">M8</b> is typing…</span></div>'
    return f'''
  <div style="margin-top: auto; display: flex; flex-direction: column; flex-shrink: 0">{t}
    <div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px 14px 12px">
      <button class="dc-icon" aria-label="Attach" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: #383A40; color: #B5BAC1; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ico(I_PLUS, 22, sw=2.4)}</button>
      <div style="flex-grow: 1; min-width: 0; height: 40px; box-sizing: border-box; padding: 0 12px 0 16px; border-radius: 20px; background: #383A40; display: flex; align-items: center; gap: 10px">
        {pill}
        <span style="display: flex; color: #B5BAC1">{ico(I_GIFT, 20)}</span>
        <span style="display: flex; color: #B5BAC1">{ico(I_SMILE, 20)}</span>
      </div>
      <button class="dc-icon" aria-label="Record voice message" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: #383A40; color: #B5BAC1; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ico(I_MIC, 20)}</button>
    </div>
  </div>'''

def divider(label, top=16):
    return f'''
    <div style="display: flex; align-items: center; gap: 8px; margin: {top}px 16px 0 16px">
      <div style="flex-grow: 1; height: 1px; background: #3F4147"></div>
      <span style="font-size: 12px; font-weight: 600; color: #949BA4">{label}</span>
      <div style="flex-grow: 1; height: 1px; background: #3F4147"></div>
    </div>'''

def note(text, top=12):  # board annotation, not Discord UI (same role as the Tg boards' grey lines)
    return f'\n    <span style="align-self: center; margin-top: {top}px; padding: 0 24px; font-size: 12px; font-style: italic; color: #949BA4; text-align: center">{text}</span>'

def used(command):
    return f'''
    <div style="position: relative; display: flex; align-items: center; gap: 4px; margin-top: 16px; padding: 0 16px 0 72px; height: 20px; font-size: 14px; color: #949BA4; white-space: nowrap">
      <span style="position: absolute; left: 35px; top: 10px; width: 30px; height: 10px; box-sizing: border-box; border-left: 2px solid #4E5058; border-top: 2px solid #4E5058; border-top-left-radius: 6px"></span>
      {josh_av(16)}
      <span style="color: #F2F3F5; font-weight: 500; margin-left: 2px">josh</span>
      <span>used</span>
      <span style="color: #00A8FC">/{command}</span>
    </div>'''

def group(who, time, body, top=16):
    av = m8_av(40) if who == 'm8' else josh_av(40)
    name = 'M8' if who == 'm8' else 'josh'
    badge = APP if who == 'm8' else ''
    return f'''
    <div style="display: flex; gap: 12px; margin-top: {top}px; padding: 2px 16px">
      {av}
      <div style="display: flex; flex-direction: column; min-width: 0; flex-grow: 1">
        <div style="display: flex; align-items: center; gap: 6px; height: 22px">
          <span style="font-size: 16px; font-weight: 600; color: #F2F3F5">{name}</span>
          {badge}
          <span style="font-size: 12px; color: #949BA4; margin-left: 2px">Today at {time}</span>
        </div>
        <div style="font-size: 16px; line-height: 1.375; color: #DBDEE1; overflow-wrap: anywhere">{body}</div>
      </div>
    </div>'''

def follow(body, top=4):
    return f'\n    <div style="margin-top: {top}px; padding: 2px 16px 2px 68px; font-size: 16px; line-height: 1.375; color: #DBDEE1; overflow-wrap: anywhere">{body}</div>'

BTN_BG = {'primary': '#5865F2', 'secondary': '#4E5058', 'success': '#248046', 'danger': '#DA373C'}
def btn(label, kind='secondary', link=False, grow=False):
    ext = f'<span style="display: flex; opacity: 0.85">{ico(I_EXT, 14, sw=2.4)}</span>' if link else ''
    g = ' flex-grow: 1; justify-content: center;' if grow else ''
    return f'<button class="dc-btn" style="height: 36px; padding: 0 14px; border: none; border-radius: 8px; background: {BTN_BG[kind]}; color: #FFFFFF; font-size: 14px; font-weight: 600; display: inline-flex; align-items: center; gap: 6px; white-space: nowrap;{g}">{label}{ext}</button>'

def row(*bs, top=8):
    return f'<div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: {top}px">{"".join(bs)}</div>'

def embed(inner, color=ACC, top=6):
    return f'<div style="display: flex; margin-top: {top}px; border-radius: 4px; overflow: hidden; background: #2B2D31; border: 1px solid #26272B"><div style="width: 4px; flex-shrink: 0; background: {color}"></div><div style="display: flex; flex-direction: column; gap: 8px; padding: 10px 14px 14px 12px; min-width: 0; flex-grow: 1">{inner}</div></div>'

def e_title(t):
    return f'<span style="font-size: 16px; font-weight: 700; line-height: 1.3; color: #F2F3F5">{t}</span>'

def e_desc(t):
    return f'<div style="font-size: 14px; line-height: 1.375; color: #DBDEE1">{t}</div>'

def e_fields(fields, cols=3):
    cells = ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px; min-width: 0"><span style="font-size: 14px; font-weight: 700; color: #F2F3F5">{n}</span><span style="font-size: 14px; line-height: 1.375; color: {c}">{v}</span></div>' for n, v, c in fields)
    return f'<div style="display: grid; grid-template-columns: repeat({cols}, minmax(0, 1fr)); gap: 8px 12px">{cells}</div>'

def e_footer():
    return f'<div style="display: flex; align-items: center; gap: 8px; margin-top: 2px; font-size: 12px; font-weight: 500; color: #949BA4">{m8_av(20, 10)}<span>TrenchM8 · journaled by M8</span></div>'

def attach(img, w=300, top=6, zoom=None):  # zoom: render the image at its native width, scaled like Discord scales a PNG
    inner = f'<div style="width: {round(w / zoom)}px; zoom: {zoom}">{img}</div>' if zoom else img
    return f'<div style="width: {w}px; max-width: 100%; margin-top: {top}px; border-radius: 8px; overflow: hidden">{inner}</div>'

def ephemeral(body):
    return f'''{body}<div style="display: flex; align-items: center; gap: 4px; margin-top: 4px; font-size: 12px; color: #949BA4">{ico(I_EYE, 14)}<span>Only you can see this ·</span><span style="color: #00A8FC">Dismiss message</span></div>'''

def voice_pill(lst='wave', dur='0:07'):
    return f'''<div style="display: flex; align-items: center; gap: 10px; width: 280px; max-width: 100%; box-sizing: border-box; margin-top: 4px; padding: 8px 12px 8px 8px; border-radius: 24px; background: #2B2D31; border: 1px solid #26272B">
          <button class="dc-btn" aria-label="Play voice message" style="width: 32px; height: 32px; padding: 0; border: none; border-radius: 16px; background: #5865F2; display: flex; align-items: center; justify-content: center; flex-shrink: 0"><svg width="12" height="14" viewBox="0 0 12 14" aria-hidden="true"><path d="M1 1.5v11a1 1 0 0 0 1.5.86l9-5.5a1 1 0 0 0 0-1.72l-9-5.5A1 1 0 0 0 1 1.5z" fill="#FFFFFF"></path></svg></button>
          <div style="display: flex; align-items: center; gap: 2px; height: 28px; flex-grow: 1; min-width: 0; overflow: hidden">
            <sc-for list="{{{{{lst}}}}}" as="w" hint-placeholder-count="34"><span style="width: 3px; flex-shrink: 0; border-radius: 2px; height: {{{{w.h}}}}; background: {{{{w.c}}}}"></span></sc-for>
          </div>
          <span style="flex-shrink: 0; white-space: nowrap; font-size: 12px; font-weight: 500; color: #DBDEE1; font-variant-numeric: tabular-nums">{dur}</span>
        </div>'''

# ---------- file shell
HELMET = '''<helmet>
<style>
body{margin:0}
a{color:#00A8FC;text-decoration:none}a:hover{text-decoration:underline}
button{font-family:inherit;cursor:pointer}
.dc-btn{transition:filter .15s ease,transform .1s ease}
.dc-btn:hover{filter:brightness(.88)}
.dc-btn:active{transform:scale(.97)}
.dc-icon:hover{background:#3F4147 !important;color:#DBDEE1 !important}
.dc-dot{animation:dc-dot 1.2s infinite ease-in-out}
.dc-dot:nth-child(2){animation-delay:.15s}.dc-dot:nth-child(3){animation-delay:.3s}
@keyframes dc-dot{0%,60%,100%{opacity:.35;transform:translateY(0)}30%{opacity:1;transform:translateY(-2px)}}
@media (prefers-reduced-motion: reduce){.dc-dot{animation:none}.dc-btn{transition:none}}
</style>
</helmet>'''

def props_json(h, extra=None):
    d = {'accent': {'editor': 'color', 'default': '#7CD4FF', 'options': ACCENTS}}
    if extra: d.update(extra)
    d['$preview'] = {'width': 390, 'height': h}
    return json.dumps(d, separators=(',', ':'))

DEFAULT_JS = '''class Component extends DCLogic {
  renderVals() {
    return { accent: this.props.accent ?? '#7CD4FF' };
  }
}'''

def write(name, title, body, js=DEFAULT_JS, extra_props=None, root_bg='#313338'):
    h = HEIGHTS[name]
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
<div style="width: 390px; min-height: {h}px; box-sizing: border-box; display: flex; flex-direction: column; background: {root_bg}; color: #DBDEE1; font-family: {FONT}; font-size: 16px; line-height: 1.375; -webkit-font-smoothing: antialiased">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{props_json(h, extra_props)}'>
{js}
</script>
</body>
</html>
'''
    assert '—' not in html, name + ' has an em dash'
    open(P + name + '.dc.html', 'w').write(html)

WAVE_JS = '''    const heights = [8, 14, 22, 12, 18, 26, 20, 10, 16, 24, 28, 18, 12, 20, 26, 14, 8, 12, 22, 18, 10, 16, 24, 20, 12, 8, 14, 18, 10, 6, 10, 8, 6, 4];
    const wave = heights.map((h, i) => ({ h: h + 'px', c: i < 12 ? '#F2F3F5' : 'rgba(242,243,245,0.32)' }));'''

def msgs(*parts, pb=16):
    return f'\n  <div style="display: flex; flex-direction: column; padding: 4px 0 {pb}px 0">' + ''.join(parts) + '\n  </div>'

# =====================================================================================
# DcInstall
def install():
    perm = lambda t: f'<div style="display: flex; align-items: center; gap: 12px; padding: 10px 0"><span style="width: 24px; height: 24px; border-radius: 12px; background: #23A55A; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ico(I_CHECK, 14, sw=3)}</span><span style="font-size: 15px; color: #DBDEE1">{t}</span></div>'
    def choice(icon, title, desc, sel, tag=''):
        border = '#5865F2' if sel else '#3F4147'
        radio = ('<span style="width: 20px; height: 20px; box-sizing: border-box; border-radius: 10px; border: 6px solid #5865F2; background: #FFFFFF; flex-shrink: 0"></span>' if sel
                 else '<span style="width: 20px; height: 20px; box-sizing: border-box; border-radius: 10px; border: 2px solid #80848E; flex-shrink: 0"></span>')
        return f'''
        <button class="dc-btn" style="display: flex; align-items: center; gap: 12px; width: 100%; padding: 12px 14px; box-sizing: border-box; border-radius: 8px; border: 2px solid {border}; background: #2B2D31; color: #DBDEE1; text-align: left">
          <span style="width: 40px; height: 40px; border-radius: 20px; background: #383A40; color: #DBDEE1; display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ico(icon, 20)}</span>
          <span style="display: flex; flex-direction: column; gap: 2px; flex-grow: 1; min-width: 0">
            {tag}<span style="font-size: 16px; font-weight: 700; color: #F2F3F5">{title}</span>
            <span style="font-size: 13px; line-height: 1.3; color: #B5BAC1">{desc}</span>
          </span>
          {radio}
        </button>'''
    rec = '<span style="align-self: flex-start; margin-bottom: 2px; height: 18px; padding: 0 6px; border-radius: 9px; background: #248046; color: #FFFFFF; font-size: 11px; font-weight: 700; line-height: 18px">Recommended</span>'
    dots = '<span style="display: flex; gap: 5px">' + '<span style="width: 6px; height: 6px; border-radius: 3px; background: #4E5058"></span>' * 3 + '</span>'
    body = f'''
  <span style="align-self: center; margin-top: 14px; padding: 0 32px; font-size: 12px; font-style: italic; color: #949BA4; text-align: center">From the landing page, "Start on Discord" opens Discord's Add App screen.</span>

  <div style="display: flex; flex-direction: column; margin: 12px 12px 0 12px; border-radius: 16px; overflow: hidden; background: #313338; border: 1px solid #3F4147">
    <div style="display: flex; align-items: center; height: 52px; padding: 0 8px; border-bottom: 1px solid #1F2023">
      <button class="dc-icon" aria-label="Close" style="width: 40px; height: 40px; padding: 0; border: none; border-radius: 20px; background: transparent; color: #B5BAC1; display: flex; align-items: center; justify-content: center">{ico(I_X, 22)}</button>
      <span style="flex-grow: 1; text-align: center; font-size: 16px; font-weight: 700; color: #F2F3F5; margin-right: 40px">Add App</span>
    </div>

    <div style="display: flex; flex-direction: column; align-items: center; padding: 22px 18px 0 18px">
      <div style="display: flex; align-items: center; gap: 14px">{m8_av(72)}{dots}{josh_av(72)}</div>
      <div style="display: flex; align-items: center; gap: 6px; margin-top: 16px"><span style="font-size: 24px; font-weight: 800; color: #F2F3F5">TrenchM8</span>{APP}</div>
      <span style="margin-top: 4px; font-size: 15px; color: #B5BAC1; text-align: center">wants to access your Discord account</span>
      <span style="margin-top: 10px; font-size: 13px; color: #949BA4">Signed in as <b style="color: #DBDEE1">josh</b> · <a href="#">Not you?</a></span>
    </div>

    <div style="display: flex; flex-direction: column; gap: 8px; padding: 20px 16px 0 16px">
      <span style="font-size: 12px; font-weight: 700; letter-spacing: 0.02em; color: #B5BAC1">ADD TRENCHM8 TO</span>{choice(I_USER, 'Add to My Apps', 'Use M8 in your DMs and across every server.', True, rec)}{choice(I_SERVER, 'Add to Server', 'Add M8 to a server you manage.', False)}
    </div>

    <div style="display: flex; flex-direction: column; padding: 20px 16px 0 16px">
      <span style="font-size: 12px; font-weight: 700; letter-spacing: 0.02em; color: #B5BAC1">THIS WILL ALLOW TRENCHM8 TO</span>
      {perm('Use application commands')}
      <div style="height: 1px; background: #3F4147"></div>
      {perm('Send you direct messages')}
    </div>

    <div style="display: flex; align-items: flex-start; gap: 8px; margin: 10px 16px 0 16px; font-size: 12px; line-height: 1.4; color: #949BA4">
      <span style="display: flex; flex-shrink: 0; margin-top: 1px">{ico(I_LOCK, 14)}</span>
      <span>TrenchM8's <a href="#">privacy policy</a> and <a href="#">terms of service</a> apply. It can't read your other DMs or see your wallet keys.</span>
    </div>

    <div style="display: flex; gap: 10px; padding: 18px 16px 12px 16px">
      {btn('Cancel', 'secondary', grow=True).replace('height: 36px', 'height: 44px')}
      {btn('Authorize', 'primary', grow=True).replace('height: 36px', 'height: 44px')}
    </div>
    <a href="#" style="align-self: center; padding-bottom: 18px; font-size: 13px; font-weight: 500">or join the TrenchM8 server</a>
  </div>

  <span style="align-self: center; margin-top: 18px; padding: 0 32px; font-size: 12px; font-style: italic; color: #949BA4; text-align: center">After Authorize, Discord opens the M8 DM and M8 says hi.</span>

  <div style="display: flex; flex-direction: column; margin: 12px 12px 0 12px; border-radius: 16px; overflow: hidden; border: 1px solid #3F4147; background: #313338">
    {header()}
    <div style="display: flex; flex-direction: column; padding: 20px 16px 8px 16px">
      {m8_av(80)}
      <div style="display: flex; align-items: center; gap: 8px; margin-top: 12px"><span style="font-size: 26px; font-weight: 800; color: #F2F3F5">M8</span>{APP}</div>
      <span style="font-size: 15px; color: #DBDEE1; margin-top: 2px">trenchm8</span>
      <span style="font-size: 15px; color: #B5BAC1; margin-top: 10px">This is the beginning of your direct message history with <b style="color: #DBDEE1">M8</b>.</span>
      <div style="display: flex; gap: 8px; margin-top: 12px">{btn('Profile', 'secondary')}{btn('Block', 'secondary')}</div>
    </div>
    {divider('October 7, 2026', 12)}
    <div style="height: 28px"></div>
    {composer(typing=True)}
  </div>

  <div style="display: flex; flex-direction: column; gap: 4px; margin: 16px 12px 16px 12px; padding: 12px 14px; border-radius: 12px; border: 1px dashed #4E5058; font-size: 13px; line-height: 1.4; color: #B5BAC1">
    <span style="font-size: 11px; font-weight: 700; letter-spacing: 0.06em; color: #949BA4">BOARD NOTE</span>
    <span>The Phase 0 spike decides <b style="color: #F2F3F5">user-installed app</b> vs <b style="color: #F2F3F5">server join</b>, whichever reliably allows proactive DMs. If it's the server, "Add to My Apps" drops and the fallback link becomes the main path.</span>
  </div>'''
    write('DcInstall', 'M8 on Discord - install', body, root_bg='#1E1F22')

# =====================================================================================
def onboarding():
    def opt(label, sample, sel):
        bg = 'background: #404249;' if sel else ''
        mark = f'<span style="display: flex; color: #5865F2">{ico(I_CHECK, 18, sw=2.6)}</span>' if sel else '<span style="width: 18px"></span>'
        return f'<div style="display: flex; align-items: center; gap: 10px; padding: 8px 12px; {bg}"><div style="display: flex; flex-direction: column; flex-grow: 1; min-width: 0"><span style="font-size: 15px; font-weight: 500; color: #F2F3F5">{label}</span><span style="font-size: 13px; line-height: 1.3; color: #B5BAC1">{sample}</span></div>{mark}</div>'
    select = f'''<div style="margin-top: 8px; display: flex; flex-direction: column; border-radius: 8px; overflow: hidden; border: 1px solid #1E1F22">
          <div style="display: flex; align-items: center; height: 40px; padding: 0 10px 0 12px; background: #1E1F22; border-bottom: 1px solid #3F4147"><span style="flex-grow: 1; font-size: 15px; color: #949BA4">Pick a voice</span><span style="display: flex; color: #DBDEE1">{ico(I_UP, 20)}</span></div>
          <div style="display: flex; flex-direction: column; padding: 4px 0; background: #2B2D31">{opt('Trench friend', 'you chased those two after lunch. what happened?', True)}{opt('Calm coach', 'Two trades after lunch lost $375. What was going on there?', False)}{opt('Blunt degen', '-$375 after lunch. explain yourself.', False)}</div>
        </div>'''
    green = '#23A55A'
    body = header() + msgs(
        divider('October 7, 2026'),
        used('start'),
        group('m8', '9:41 AM', "<b>gm. I'm M8.</b><br>I watch your wallets, text you after you trade, and turn your replies into a trading journal. You never write a thing.<br><br>First: paste a wallet you trade from. Solana, Base, BNB or Robinhood Chain." + sub("Read-only. I'll never ask you to sign anything or connect."), top=4),
        group('josh', '9:42 AM', '7xKpQ2vNfL8dRj4tYc1Hs9aEwBmZ63fQa'),
        group('m8', '9:42 AM', f"Solana wallet {code('7xKp…3fQa')} added. Pulling your last 30 days of trades now, about a minute." + row(btn('Add another'), btn("That's all", 'primary'))),
        note('You tapped "That\'s all"', 10),
        follow('<b>Pick my voice.</b> Same facts, different delivery:' + select, 10),
        note('You picked "Trench friend". The reply is ephemeral.', 10),
        follow(ephemeral(f'Trench friend it is. Switch anytime with {cmd("voice")}.'), 10),
        follow("Last thing: looks like you're on <b>New York time (ET)</b>. Right?" + row(btn('Yep', 'primary'), btn('Change')), 10),
        note('You tapped "Yep"', 10),
        group('m8', '9:44 AM', embed(
            e_title('Your last 30 days') +
            e_fields([('Trades', '142', '#DBDEE1'), ('PnL', 'up $1,284', '#3FD98E'), ('Win rate', '48%', '#DBDEE1')]) +
            e_desc("One thing jumped out: you're <b>up $2,910 on coins under 1 hour old</b>, and <b>down $1,626 on everything older</b>. Fresh launches are your edge. Old coins are where it leaks.") +
            e_footer(), green, top=2), top=10),
        follow("I'll text you about 2h after your next session. Your 7-day trial starts now, everything unlocked." + row(btn('Open my journal', link=True))),
    ) + composer()
    write('DcOnboarding', 'M8 on Discord - onboarding', body)

# =====================================================================================
def nudge():
    journal = embed(
        e_title("Today's journal") +
        e_desc('<b>Morning +$609.</b> 6 trades, sized small, took profit into strength.') +
        e_desc('<b>$WIFHAT -$221.</b> FOMO: bought after a +180% candle, at 2x your morning size.') +
        e_desc('<b>$PEPU2 -$154.</b> Revenge: entered 4 min after closing $WIFHAT red, at 2x your normal size.') +
        e_desc('Your words:' + quote('<i>they were pumping and I didn\'t want to miss out.</i>')) +
        e_footer())
    body = header() + msgs(
        divider('October 7, 2026'),
        note('Last trade closed 2:20 PM. No activity for 2h, so M8 checks in.', 10),
        group('m8', '4:22 PM', '{{v.nudge}}', top=12),
        group('josh', '4:28 PM', voice_pill()),
        group('m8', '4:28 PM', '{{v.logged}}' + journal + row(btn("Open today's journal", link=True))),
        follow('{{v.suggest}}' + row(btn('Set 20 min cooldown', 'primary'), btn('Not now')), 10),
        note('You tapped "Set 20 min cooldown"', 10),
        follow('{{v.done}}', 10),
    ) + composer()
    js = '''class Component extends DCLogic {
  renderVals() {
    const accent = this.props.accent ?? '#7CD4FF';
    const voice = this.props.voice ?? 'friend';
    const voices = {
      friend: {
        nudge: '8 trades today, up $234. Your morning was great, but you lost $375 on two coins after lunch. What happened there?',
        logged: 'Got it. Here’s what went in your journal:',
        suggest: 'Real talk: that’s the 3rd time this week you chased right after a red trade. Want a 20 min cooldown after losses? I’ll ping you if you break it.',
        done: 'Done. 20 min cooldown after any red trade. Go touch some grass, see you tomorrow.'
      },
      coach: {
        nudge: '8 trades today, up $234 overall. A strong morning, then two trades after lunch lost $375. What was going on there?',
        logged: 'Thank you. Here’s what I added to your journal:',
        suggest: 'This is the third time this week a losing trade was followed by a chase. Would a 20-minute cooldown after losses help? I can alert you if it’s broken.',
        done: 'Set: a 20-minute cooldown after any losing trade. Rest well, talk tomorrow.'
      },
      degen: {
        nudge: '8 trades, +$234. Morning: chef. After lunch: -$375 on two coins. Explain yourself.',
        logged: 'Noted. Your crimes, for the record:',
        suggest: '3rd revenge chase this week, ser. Want a 20 min timeout after red trades? I will snitch if you break it.',
        done: 'Locked. 20 min timeout after every red trade. Log off.'
      }
    };
''' + WAVE_JS + '''
    return { accent, v: voices[voice] || voices.friend, wave };
  }
}'''
    write('DcNudge', 'M8 on Discord - evening nudge', body, js, {'voice': {'editor': 'enum', 'options': ['friend', 'coach', 'degen'], 'default': 'friend'}})

# =====================================================================================
def rule():
    body = header() + msgs(
        divider('October 9, 2026'),
        note('Mid-session. M8 saw the buy on its next wallet poll, about a minute later.', 10),
        group('m8', '1:12 PM', "<b>Cooldown check.</b> You bought <b>$FROGZ</b> 3 min after closing <b>$SNEK</b> red (-$64). Your rule is 20 min after a red trade.<br><br>Not telling you what to do with it. Just making sure this one's on purpose." + row(btn("It's planned"), btn('My bad, pausing', 'primary')), top=12),
        note('You tapped "It\'s planned"', 10),
        follow("Cool. What's the setup?", 10),
        group('josh', '1:13 PM', 'fresh launch, dev burned LP, half my normal size'),
        group('m8', '1:13 PM', "Logged as planned, with your reasons. We'll see how it played out tonight."),
        note('Later that afternoon', 18),
        group('m8', '2:41 PM', "<b>Daily loss limit hit.</b> You're down <b>$156</b> today. The stop you set is $150.<br><br>That's the day. Everything after this is just a donation to the trenches." + row(btn('Done for today', 'primary'), btn('Show me today')), top=12),
        note('You tapped "Done for today"', 10),
        follow('Respect. That\'s a rule kept, and it\'ll show up in your week. I\'ll check in tonight.', 10),
    ) + composer()
    write('DcRuleAlert', 'M8 on Discord - live rule alert', body)

# =====================================================================================
def morning():
    def field(name, val):
        return f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="font-size: 14px; font-weight: 700; color: #F2F3F5">{name}</span><div style="font-size: 14px; line-height: 1.375; color: #DBDEE1">{val}</div></div>'
    li = lambda t: f'<div style="display: flex; gap: 8px"><span style="color: #949BA4">•</span><span>{t}</span></div>'
    brief = embed(
        field('Overnight in the trenches',
              li('<b>Solana:</b> pump.fun launches down 18% vs yesterday. Fewer coins, same volume.') +
              li('<b>Robinhood Chain:</b> busiest night this month. 3 of the top 10 new pairs launched there.') +
              li('<b>Base, BNB:</b> quiet. One big rug on BNB ($PANDAX, -94% in 6 min).')) +
        field('From yesterday', 'You were up $647 before lunch and gave $375 back chasing. Your new cooldown is live today: <b>20 min after any red trade.</b>') +
        field('Worth knowing', "This month you're <b>+$2,140 between 9 and 11 AM</b> and <b>-$860 after 1 PM</b>.") +
        e_footer())
    body = header() + msgs(
        divider('October 8, 2026'),
        group('m8', '8:00 AM', "<b>gm. Here's your Thursday.</b>" + brief + row(btn('Yesterday', link=True), btn('Mute mornings')), top=12),
        group('josh', '8:06 AM', 'ty m8. no trades after 1 today'),
        group('m8', '8:06 AM', 'Want that as a rule for today, or every day?' + row(btn('Just today'), btn('Every day', 'primary'))),
    ) + composer()
    write('DcMorning', 'M8 on Discord - morning brief', body)

# =====================================================================================
def ask():
    chart = extract_img('TgAsk.dc.html')
    caption = "<b>+$720 this week</b> across 27 trades, 52% win rate.<br><br>Best day Monday (+$412). Worst was today (-$156), but you hit your loss limit and stopped. This month, on days you kept going past -$150, you lost another $210 on average. Today you didn't.<br><br>Cooldown: kept 2 of 3 times, and the one you broke you called planned."
    auto = f'''
  <div style="display: flex; flex-direction: column; margin: 0 12px; border-radius: 8px; overflow: hidden; background: #2B2D31; border: 1px solid #1E1F22">
    <div style="display: flex; align-items: center; gap: 8px; padding: 8px 12px; font-size: 12px; font-weight: 700; letter-spacing: 0.02em; color: #B5BAC1; border-bottom: 1px solid #3F4147">{m8_av(16, 8)}<span>TRENCHM8</span></div>
    <div style="display: flex; align-items: center; gap: 12px; padding: 10px 12px; background: #404249">
      {m8_av(32)}
      <div style="display: flex; flex-direction: column; flex-grow: 1; min-width: 0">
        <span style="font-size: 15px; color: #F2F3F5"><b>/ask</b> <span style="color: #B5BAC1">question</span></span>
        <span style="font-size: 13px; color: #B5BAC1; white-space: nowrap; overflow: hidden; text-overflow: ellipsis">Ask M8 anything about your trading</span>
      </div>
      <span style="font-size: 12px; color: #949BA4">TrenchM8</span>
    </div>
    <div style="display: flex; align-items: center; gap: 12px; padding: 10px 12px">
      {m8_av(32)}
      <div style="display: flex; flex-direction: column; flex-grow: 1; min-width: 0">
        <span style="font-size: 15px; color: #F2F3F5"><b>/voice</b> <span style="color: #B5BAC1">voice</span></span>
        <span style="font-size: 13px; color: #B5BAC1">Switch how M8 talks to you</span>
      </div>
      <span style="font-size: 12px; color: #949BA4">TrenchM8</span>
    </div>
  </div>'''
    pill = '<span style="flex-grow: 1; min-width: 0; display: flex; align-items: center; gap: 6px; font-size: 16px; color: #F2F3F5; white-space: nowrap; overflow: hidden"><b>/ask</b><span style="height: 24px; padding: 0 6px; border-radius: 4px; background: #1E1F22; color: #DBDEE1; font-size: 14px; line-height: 24px">question:</span><span style="width: 2px; height: 18px; background: #F2F3F5"></span></span>'
    body = header() + msgs(
        divider('October 9, 2026'),
        used('ask'),
        group('m8', '7:40 PM', quote('<span style="color: #DBDEE1">how did i do this week?</span>') + '<div style="margin-top: 6px">' + caption + '</div>' + attach(chart) + row(btn('Full stats', link=True), btn('vs last week')), top=4),
        group('josh', '7:42 PM', 'is $FROGZ gonna run again tomorrow?'),
        group('m8', '7:42 PM', 'Not a call, just facts: $FROGZ is 7h old, $214k liquidity, top 10 wallets hold 31%.<br><br>Your best setup is coins under 1h old at normal size: your planned entries there are +$1,980 this month. Your call.'),
        note('/ask works in the DM and in any server. In the DM you can also just type.', 18),
        pb=10) + auto + composer(pill)
    write('DcAsk', 'M8 on Discord - ask', body)

# =====================================================================================
def recap():
    card = extract_img('TgRecap.dc.html')
    caption = "<b>Your week.</b> Up $816 on 31 trades, best week this month.<br><br><b>Biggest mistake:</b> chasing right after a red trade. 3 times, -$512 combined. Without those you'd be up $1,328.<br><br><b>What worked:</b> fresh launches before 11 AM (+$1,140), and stopping at your limit on Friday.<br><br><b>One change:</b> your after-1 PM trades lost $430 this week. No new entries after 1 PM. Make it a rule?"
    body = header() + msgs(
        divider('October 11, 2026'),
        group('m8', '6:00 PM', caption + attach(card, 306, 8, 0.9) + row(btn('Make it a rule', 'primary'), btn('Not this week')) + row(btn('Share card'), btn('Full recap', link=True)), top=12),
    ) + composer()
    write('DcRecap', 'M8 on Discord - weekly recap', body)

# =====================================================================================
def repeat():
    body = header() + msgs(
        divider('October 7, 2026'),
        group('m8', '1:58 PM', "<b>Heads up.</b> You just bought <b>$PEPU2</b> 4 min after closing <b>$WIFHAT</b> red, at 2x your normal size.<br><br>Same move as Sep 18: $PEPU, 2 min after a loss, 2.5x size, -$188. Planned?" + row(btn("It's planned"), btn('Good catch', 'primary')), top=12),
        note('You tapped "Good catch"', 10),
        follow("Noted. I'll stay quiet for the rest of this session. We'll look at it tonight.", 10),
        note('2 hours after your last trade', 18),
        group('m8', '4:22 PM', "8 trades today, up $234. Great morning. After lunch, $WIFHAT and $PEPU2 cost $375.<br><br>$PEPU2 was the same re-entry as Sep 18 and Sep 24. On the 24th you wrote <i>\"never again after a red one\"</i>. What happened today?", top=12),
        group('josh', '4:23 PM', voice_pill() + '<div style="margin-top: 6px; font-size: 13px; font-style: italic; color: #949BA4">"i chased them, they were pumping and i didn\'t want to miss out"</div>'),
        group('m8', '4:23 PM', "Written up in your words. That's 3 times now, all after 1 PM.<br><br>Want a 20 min cooldown after red trades? I'll ping you if you break it." + row(btn('Make it a rule', 'primary'), btn('See journal', link=True))),
    ) + composer()
    js = '''class Component extends DCLogic {
  renderVals() {
    const accent = this.props.accent ?? '#7CD4FF';
''' + WAVE_JS + '''
    return { accent, wave };
  }
}'''
    write('DcRepeat', 'M8 on Discord - repeat pattern', body, js)

for f in (install, onboarding, nudge, rule, morning, ask, recap, repeat):
    f()
print('ok')
