# Static preview of a .dc.html: runs renderVals once (after optional state), expands sc-if/sc-for/{{}} in the browser.
# <dc-import name="X" ...> renders X.dc.html from the same folder for real: kebab-case attributes become camelCase props
# ("{{expr}}" passes the raw value from the parent scope), X's renderVals runs, and its template is expanded inline at
# its hint-size (width fixed, height as a minimum). Nested imports recurse up to MAX_DEPTH. A failed import falls back
# to a hatched box, logs the error to the console and appends it to the title.
# usage: python3 build.py File.dc.html out.html [propsJSON|null] [stateJSON|null]   (ROOTW env fixes the root width)
import sys, json, re, os

src_path, out = sys.argv[1], sys.argv[2]
props = sys.argv[3] if len(sys.argv) > 3 else 'null'
state = sys.argv[4] if len(sys.argv) > 4 else 'null'
folder = os.path.dirname(os.path.abspath(src_path))
root_name = os.path.basename(src_path).replace('.dc.html', '')


def parse(path):
    s = open(path).read()
    helmet = s[s.index('<helmet>') + 8:s.index('</helmet>')]
    body = s[s.index('</helmet>') + 9:s.index('</x-dc>')]
    js = s.split('<script type="text/x-dc"')[1]
    js = js[js.index('>') + 1:js.index('</script>')]
    return helmet, body, js


# Collect the root plus every component it imports, transitively.
comps, queue = {}, [root_name]
while queue:
    n = queue.pop()
    if n in comps:
        continue
    p = os.path.join(folder, n + '.dc.html')
    if not os.path.exists(p):
        comps[n] = None
        continue
    comps[n] = parse(p)
    queue += re.findall(r'<dc-import[^>]*\bname="([A-Za-z0-9_]+)"', comps[n][1])

# Helmet: the root's helmet whole; imported helmets contribute each <style>/<link> once.
head_parts, seen = [], set()
for n in [root_name] + [k for k in comps if k != root_name]:
    if not comps[n]:
        continue
    for chunk in re.findall(r'<style[^>]*>.*?</style>|<link[^>]*>', comps[n][0], re.S):
        key = chunk.strip()
        if key not in seen:
            seen.add(key)
            head_parts.append(chunk)

templates = ''.join(
    '<template id="t-%s">%s</template>' % (n, c[1]) for n, c in comps.items() if c)
classes = ',\n'.join(
    '%s: (function(){\n%s\nreturn Component;\n})()' % (json.dumps(n), c[2]) for n, c in comps.items() if c)
rootw = 'width:' + os.environ['ROOTW'] + 'px' if os.environ.get('ROOTW') else ''

html = '''<!doctype html><html><head><meta charset="utf-8">''' + ''.join(head_parts) + '''</head><body>''' + templates + '''<div id="root" style="''' + rootw + '''"></div>
<script>
const ERRS = [];
window.onerror = (m, u, l) => { ERRS.push(m + ' @' + l); document.title = 'ERR ' + m + ' @' + l; };
class DCLogic { constructor(){ this.state = null; this.props = {}; } setState(p){ this.state = Object.assign({}, this.state || {}, p); } }
const COMPONENTS = {
''' + classes + '''
};
const MAX_DEPTH = 6;
const noop = () => {};
const get = (scope, expr) => { expr = expr.trim(); if (expr === 'true') return true; if (expr === 'false') return false; let v = scope; for (const k of expr.split('.')) { if (v == null) return undefined; v = v[k]; } return v; };
const sub = (scope, str) => str.replace(/\\{\\{([^}]+)\\}\\}/g, (m, e) => { const v = get(scope, e); return typeof v === 'function' ? '' : (v == null ? '' : String(v)); });
const camel = (s) => s.replace(/-([a-z0-9])/g, (m, c) => c.toUpperCase());
function instance(name, props, preset) {
  const C = COMPONENTS[name];
  if (!C) throw new Error('no component ' + name);
  const c = new C();
  c.props = Object.assign({ onNav: noop, onToast: noop, onModal: noop, onClose: noop }, props || {});
  if (preset) c.state = preset;
  return c.renderVals();
}
function expand(name, vals, parent, depth) {
  const t = document.getElementById('t-' + name);
  for (const ch of t.content.childNodes) walk(ch, vals, parent, depth);
}
function hatch(parent, w, h, label) {
  const d = document.createElement('div');
  d.style.cssText = 'width:' + w + ';height:' + h + ';background:repeating-linear-gradient(45deg,#333 0 10px,#444 10px 20px);color:#fff;font:12px sans-serif;padding:8px;box-sizing:border-box';
  d.textContent = label; parent.appendChild(d);
}
function walk(node, scope, parent, depth) {
  if (node.nodeType === 3) { parent.appendChild(document.createTextNode(sub(scope, node.textContent))); return; }
  if (node.nodeType !== 1) return;
  const tag = node.tagName.toLowerCase();
  if (tag === 'sc-if') { const v = get(scope, node.getAttribute('value').replace(/[{}]/g, '')); if (v) for (const ch of node.childNodes) walk(ch, scope, parent, depth); return; }
  if (tag === 'sc-for') { const list = get(scope, node.getAttribute('list').replace(/[{}]/g, '')) || []; const as = node.getAttribute('as'); for (const it of list) { const sc = Object.assign(Object.create(scope), { [as]: it }); for (const ch of node.childNodes) walk(ch, sc, parent, depth); } return; }
  if (tag === 'dc-import') {
    const name = node.getAttribute('name');
    const hs = (node.getAttribute('hint-size') || '100%,auto').split(',').map((x) => x.trim());
    try {
      if (depth >= MAX_DEPTH) throw new Error('max import depth');
      const props = {};
      for (const a of node.attributes) {
        if (a.name === 'name' || a.name.startsWith('hint-')) continue;
        const raw = a.value.match(/^\\{\\{([^}]+)\\}\\}$/);
        props[camel(a.name)] = raw ? get(scope, raw[1]) : sub(scope, a.value);
      }
      const vals = instance(name, props, null);
      const wrap = document.createElement('div');
      wrap.setAttribute('data-import', name);
      wrap.style.cssText = 'width:' + hs[0] + ';min-height:' + hs[1] + ';display:flex;flex-direction:column;flex-shrink:0';
      expand(name, vals, wrap, depth + 1);
      const first = wrap.firstElementChild;
      if (first && !first.style.flexGrow) first.style.flexGrow = '1';
      parent.appendChild(wrap);
    } catch (e) {
      ERRS.push('import ' + name + ': ' + e.message);
      console.error('import ' + name, e);
      hatch(parent, hs[0], hs[1] === 'auto' ? '200px' : hs[1], 'import ' + name + ' failed: ' + e.message);
    }
    return;
  }
  const el = document.createElementNS(node.namespaceURI, node.localName);
  for (const a of node.attributes) { if (/^on[A-Z]/.test(a.name) || a.name === 'ref') continue; if (a.name.startsWith('on') && a.value.includes('{{')) continue; el.setAttribute(a.name, sub(scope, a.value)); }
  const kids = tag === 'template' ? node.content.childNodes : node.childNodes;
  for (const ch of kids) walk(ch, scope, el, depth);
  parent.appendChild(el);
}
const rootEl = document.getElementById('root');
const vals = instance(''' + json.dumps(root_name) + ''', ''' + props + ''', ''' + state + ''');
expand(''' + json.dumps(root_name) + ''', vals, rootEl, 0);
document.title = 'H=' + rootEl.scrollHeight + (ERRS.length ? ' ERR ' + ERRS.join(' | ') : '');
</script></body></html>'''
open(out, 'w').write(html)
