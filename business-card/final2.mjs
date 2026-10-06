import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const meta = JSON.parse(fs.readFileSync('final/meta.json'));
const W = 3.75, H = 2.25, css = `@page{size:${W}in ${H}in;margin:0}html,body{margin:0}svg{display:block;page-break-after:always}`;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
for (const d of meta) {
  await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${d.front}${d.back}`);
  await p.pdf({ path: `final/${d.key}.pdf`, width: W+'in', height: H+'in', printBackground: true });
}
await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${meta.map(d=>d.front+d.back).join('')}`);
await p.pdf({ path: 'final/ALL-5-patterns-print.pdf', width: W+'in', height: H+'in', printBackground: true });
const sp = await b.newPage({ viewport: { width: 1296, height: 800 }, deviceScaleFactor: 1.5 });
const rows = meta.map(d => `<div class=r><div class=l>${d.key}</div><div class=c>${d.front_p}</div><div class=c>${d.back_p}</div></div>`).join('');
await sp.setContent(`<!doctype html><meta charset=utf-8><style>body{margin:0;padding:28px 32px;background:#dfe3e9;font-family:Inter;width:1296px}
.r{display:flex;align-items:center;gap:24px;margin-bottom:22px}.l{width:96px;font-weight:700;font-size:14px;color:#3a4452}
.c{width:560px;height:320px;border-radius:22px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.22)}.c svg{width:560px;height:320px;display:block}</style>${rows}`);
await sp.screenshot({ path: 'final/sheet-5-patterns.png', fullPage: true });
await b.close();
