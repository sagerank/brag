import { chromium } from '/opt/node-tools/node_modules/playwright/index.mjs';
import fs from 'fs';
const f = fs.readFileSync('final/PRINT-READY/svg/SageRank-card_front_trim.svg', 'utf8');
const k = fs.readFileSync('final/PRINT-READY/svg/SageRank-card_back_trim.svg', 'utf8');
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage({ viewport: { width: 1500, height: 560 }, deviceScaleFactor: 2 });
const card = s => `<div class=c>${s}</div>`;
await p.setContent(`<body style="margin:0;background:#e4e8ee;display:flex;gap:48px;align-items:center;justify-content:center;height:560px;font-family:Inter">
<style>.c{width:630px;height:360px;border-radius:26px;overflow:hidden;box-shadow:0 18px 40px rgba(10,18,32,.22),0 2px 6px rgba(10,18,32,.12)}.c svg{width:630px;height:360px;display:block}
.w{display:flex;flex-direction:column;gap:14px;align-items:center}.l{font-size:13px;letter-spacing:.14em;color:#586376;font-weight:700}</style>
<div class=w>${card(f)}<div class=l>FRONT</div></div><div class=w>${card(k)}<div class=l>BACK</div></div></body>`);
await p.screenshot({ path: 'final/SageRank-business-card_front-and-back.png' });
await b.close();
