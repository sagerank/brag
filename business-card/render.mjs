import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import path from 'path';
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const W = 3.75, H = 2.25;
for (const n of ['front', 'back']) {
  const p = await b.newPage({ viewport: { width: Math.round(W*96), height: Math.round(H*96) }, deviceScaleFactor: 12.5 });
  await p.goto('file://' + path.resolve(n + '.html'));
  await p.screenshot({ path: n + '-print-bleed.png' });
  await p.pdf({ path: n + '-print-bleed.pdf', width: W+'in', height: H+'in', printBackground: true });
  await p.close();
}
const p = await b.newPage();
await p.goto('file://' + path.resolve('both.html'));
await p.pdf({ path: 'sagerank-business-card-print.pdf', width: W+'in', height: H+'in', printBackground: true });
await b.close();
