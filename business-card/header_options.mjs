import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const m = JSON.parse(fs.readFileSync('final/header-options/meta.json'));
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1360, height: 800 }, deviceScaleFactor: 1.5 });
const cell = d => `<div><div class=l>${d.key}</div><div class=c>${d.back_p}</div></div>`;
await p.setContent(`<!doctype html><meta charset=utf-8><style>body{margin:0;padding:28px 32px;background:#dfe3e9;font-family:Inter;width:1296px}
.g{display:grid;grid-template-columns:1fr 1fr;gap:26px 28px}.l{font-weight:700;font-size:15px;color:#2a3342;margin-bottom:9px}
.c{width:620px;height:354px;border-radius:24px;overflow:hidden;box-shadow:0 8px 22px rgba(10,18,32,.22)}.c svg{width:620px;height:354px;display:block}</style>
<div class=g>${m.map(cell).join('')}</div>`);
await p.screenshot({ path: 'final/header-options/name-title-options.png', fullPage: true });
await b.close();
