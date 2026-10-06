import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const m = JSON.parse(fs.readFileSync('final/backs/meta.json'));
const W = 3.75, H = 2.25, css = `@page{size:${W}in ${H}in;margin:0}html,body{margin:0}svg{display:block;page-break-after:always}`;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
for (const d of m.items) {
  await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${d.front}${d.back}`);
  await p.pdf({ path: `final/backs/card-${d.key}.pdf`, width: W+'in', height: H+'in', printBackground: true });
}
const sp = await b.newPage({ viewport: { width: 1296, height: 800 }, deviceScaleFactor: 1.5 });
const cell = (svg, label) => `<div class=w><div class=l>${label}</div><div class=c>${svg}</div></div>`;
await sp.setContent(`<!doctype html><meta charset=utf-8><style>body{margin:0;padding:28px 32px;background:#dfe3e9;font-family:Inter;width:1296px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:22px 24px}.l{font-weight:700;font-size:14px;color:#3a4452;margin-bottom:8px}
.c{width:600px;height:343px;border-radius:24px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.22)}.c svg{width:600px;height:343px;display:block}</style>
<div class=g>${cell(m.front_p,'FRONT (confirmed, same for all)')}<div></div>${m.items.map(d=>cell(d.back_p,'BACK '+d.key)).join('')}</div>`);
await sp.screenshot({ path: 'final/backs/sheet-5-back-variations.png', fullPage: true });
await b.close();
