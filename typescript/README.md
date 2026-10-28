# ⚡ kickstream-sdk (TypeScript / Node.js)

[![npm version](https://img.shields.io/badge/npm-v1.0.4-red.svg)](https://npmjs.org/package/kickstream-sdk)
[![TypeScript](https://img.shields.io/badge/TypeScript-Ready-blue.svg)](https://www.typescriptlang.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-%3C30ms-brightgreen)](https://rapidapi.com/organization/aether-protocol-labs)

High-performance TypeScript & Node.js client for **Kick.com API & pre-warmed Kasada `kpsdk` telemetry**.

---

## 📦 Installation
```bash
npm install kickstream-sdk
# or
pnpm add kickstream-sdk
# or
bun add kickstream-sdk
```

---

## 🚀 Quick Usage
```typescript
import { KickStreamClient } from 'kickstream-sdk';

const client = new KickStreamClient('YOUR_RAPIDAPI_KEY');

async function main() {
  // 1. Channel Live Stream Status
  const info = await client.getChannelInfo('xqc');
  console.log('Channel Status:', info.is_live ? 'LIVE' : 'OFFLINE');

  // 2. Fetch Pre-Warmed Kasada Telemetry (<30ms)
  const telemetry = await client.getKasadaTelemetry('https://kick.com');
  console.log('Valid Kasada Headers:', telemetry.headers);
}

main().catch(console.error);
```
