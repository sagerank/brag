import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const d = JSON.parse(fs.readFileSync('final/combo/meta.json'));
const W = 3.75, H = 2.25, css = `@page{size:${W}in ${H}in;margin:0}html,body{margin:0}svg{display:block;page-break-after:always}`;
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 360, height: 216 }, deviceScaleFactor: 400/96 });
await p.setContent(`<!doctype html><meta charset=utf-8><style>${css}</style>${d.front}${d.back}`);
await p.pdf({ path: 'final/combo/SageRank-business-card-FINAL.pdf', width: W+'in', height: H+'in', printBackground: true });
for (const s of ['front','back']) { await p.setContent(`<style>html,body{margin:0}svg{display:block}</style>${d[s]}`); await p.screenshot({ path: `final/combo/${s}_400dpi-with-bleed.png` }); }
const pv = await b.newPage({ viewport: { width: 1200, height: 420 }, deviceScaleFactor: 2 });
await pv.setContent(`<body style="margin:0;background:#dfe3e9;display:flex;gap:30px;align-items:center;justify-content:center;height:420px"><style>.s svg{width:540px;height:309px;display:block}.c{width:540px;height:309px;border-radius:20px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.25)}</style>
<div class=c><div class=s>${d.front_p}</div></div><div class=c><div class=s>${d.back_p}</div></div></body>`);
await pv.screenshot({ path: 'final/combo/preview.png' });
await b.close();
