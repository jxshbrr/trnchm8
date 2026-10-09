// Logic check for .dc.html boards: runs renderVals for every theme/layout combo
// and asserts each {{ref}} in the markup resolves to something.
// Usage: node tools/check.js Main Desktop ...   (names without .dc.html; default: every board)
const fs = require('fs');
const path = require('path');

const DIR = path.join(__dirname, '..');
global.DCLogic = class {
  constructor() { this.state = null; this.props = {}; }
  setState(p) { this.state = Object.assign({}, this.state || {}, typeof p === 'function' ? p(this.state || {}) : p); }
};

const names = process.argv.slice(2).length
  ? process.argv.slice(2)
  : fs.readdirSync(DIR).filter((f) => f.endsWith('.dc.html')).map((f) => f.replace('.dc.html', ''));

const get = (o, p) => p.split('.').reduce((a, k) => (a == null ? undefined : a[k]), o);
let failed = 0;

for (const name of names) {
  const src = fs.readFileSync(path.join(DIR, name + '.dc.html'), 'utf8');
  const [body] = src.split('<script type="text/x-dc"');
  const js = src.split(/<script type="text\/x-dc"[^>]*>/)[1].split('</script>')[0];
  const propsDef = JSON.parse((src.match(/data-props='([^']*)'/) || [, '{}'])[1]);
  const C = new Function(js + '\nreturn Component;')();

  const aliases = new Set([...body.matchAll(/\bas="(\w+)"/g)].map((m) => m[1]));
  const refs = [...new Set([...body.matchAll(/\{\{\s*([A-Za-z_$][\w$.]*)\s*\}\}/g)].map((m) => m[1]))]
    .filter((r) => !aliases.has(r.split('.')[0]) && r !== 'true' && r !== 'false');

  // Every enum prop with "theme" or "layout" in its name gets each option tried.
  const combos = [{}];
  for (const [k, d] of Object.entries(propsDef)) {
    if (!d || d.editor !== 'enum' || !/theme|layout/i.test(k)) continue;
    const next = [];
    for (const c of combos) for (const o of d.options) next.push(Object.assign({}, c, { [k]: o }));
    combos.splice(0, combos.length, ...next);
  }
  if (!propsDef.theme) for (const c of [...combos]) combos.push(Object.assign({}, c, { theme: 'light' }));

  for (const props of combos) {
    const label = name + ' ' + JSON.stringify(props);
    try {
      const c = new C();
      c.props = Object.assign({ onNav() {}, onToast() {}, onModal() {}, onClose() {} }, props);
      const v = c.renderVals();
      const miss = refs.filter((r) => get(v, r) === undefined);
      if (miss.length) { failed++; console.log('FAIL', label, 'undefined:', miss.join(', ')); }
      else console.log('ok  ', label, refs.length + ' refs');
    } catch (e) {
      failed++;
      console.log('FAIL', label, e.message);
    }
  }
}
process.exit(failed ? 1 : 0);
