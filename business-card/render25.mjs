import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const meta = JSON.parse(fs.readFileSync('designs/meta.json'));
const W = 3.75, H = 2.25;
const css = `@page{size:${W}in ${H}in;margin:0}html,body{margin:0}svg{display:block;page-break-after:always}`;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
for (const d of meta) {
  await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${d.front}${d.back}`);
  await p.pdf({ path: `designs/${d.key}.pdf`, width: W+'in', height: H+'in', printBackground: true });
}
await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${meta.map(d=>d.front+d.back).join('')}`);
await p.pdf({ path: 'designs/ALL-25-designs-print.pdf', width: W+'in', height: H+'in', printBackground: true });
// contact sheets (trim-size previews with rounded corners)
const concepts = [...new Set(meta.map(d => d.concept))];
const sp = await b.newPage({ viewport: { width: 1360, height: 800 }, deviceScaleFactor: 1.5 });
for (const c of concepts) {
  const rows = meta.filter(d => d.concept === c).map(d => `<div class=r><div class=l>${d.variant}</div><div class=c>${d.front_p}</div><div class=c>${d.back_p}</div></div>`).join('');
  await sp.setContent(`<!doctype html><meta charset=utf-8><style>body{margin:0;padding:28px 32px;background:#dfe3e9;font-family:Inter;width:1296px}
  h1{margin:0 0 18px;font-size:26px;color:#0B0F17}.r{display:flex;align-items:center;gap:24px;margin-bottom:22px}.l{width:96px;font-weight:700;font-size:15px;color:#3a4452}
  .c{width:560px;height:320px;border-radius:22px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.22)}.c svg{width:560px;height:320px;display:block}</style><h1>${c}</h1>${rows}`);
  await sp.screenshot({ path: `designs/sheet-${c}.png`, fullPage: true });
}
await b.close();
