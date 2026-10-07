import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs'; import path from 'path';
const R = 'final/PRINT-READY'; fs.mkdirSync(`${R}/png`, { recursive: true }); fs.mkdirSync(`${R}/pdf`, { recursive: true });
const meta = JSON.parse(fs.readFileSync('final/FINAL/meta.json'));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const DPI = 600, k = DPI/96;
const sizes = { bleed: [3.75, 2.25], trim: [3.5, 2] };
for (const side of ['front','back']) for (const tag of ['bleed','trim']) {
  const [w, h] = sizes[tag];
  const p = await b.newPage({ viewport: { width: Math.round(w*96), height: Math.round(h*96) }, deviceScaleFactor: k });
  await p.goto('file://' + path.resolve(`${R}/svg/SageRank-card_${side}_${tag}.svg`));
  await p.screenshot({ path: `${R}/png/SageRank-card_${side}_${tag}_${DPI}dpi.png` });
  if (tag === 'bleed') await p.pdf({ path: `${R}/pdf/_${side}.pdf`, width: w+'in', height: h+'in', printBackground: true });
  await p.close();
}
// reference render of the ORIGINAL (live-text) design for an outline-fidelity check
const rp = await b.newPage({ viewport: { width: 360, height: 216 }, deviceScaleFactor: k });
for (const side of ['front','back']) { await rp.setContent(`<style>html,body{margin:0}svg{display:block}</style>${meta[side]}`); await rp.screenshot({ path: `final/PRINT-READY/_ref_${side}.png` }); }
await b.close();
