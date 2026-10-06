import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const keys = ['01-diagonal_A-light','02-slant-panel_A-light','02-slant-panel_D-mist'];
const meta = JSON.parse(fs.readFileSync('designs/meta.json'));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 360, height: 216 }, deviceScaleFactor: 400/96 });
for (const k of keys) {
  const d = meta.find(x => x.key === k);
  fs.copyFileSync(`designs/${k}.pdf`, `final/${k}.pdf`);
  for (const side of ['front','back']) {
    await p.setContent(`<style>html,body{margin:0}svg{display:block}</style>${d[side]}`);
    await p.screenshot({ path: `final/${k}_${side}_400dpi-with-bleed.png` });
  }
  // rounded-corner trim preview, both sides on one image
  const pv = await b.newPage({ viewport: { width: 1200, height: 420 }, deviceScaleFactor: 2 });
  await pv.setContent(`<body style="margin:0;background:#dfe3e9;display:flex;gap:30px;align-items:center;justify-content:center;height:420px">
   ${['front_p','back_p'].map(s=>`<div style="width:540px;height:309px;border-radius:20px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.25)"><div style="width:540px;height:309px" class=s>${d[s]}</div></div>`).join('')}
   <style>.s svg{width:540px;height:309px;display:block}</style></body>`);
  await pv.screenshot({ path: `final/${k}_preview.png` });
  await pv.close();
}
await b.close();
