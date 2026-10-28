# 🚀 KickStream Python SDK

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.4-blue.svg)](https://pypi.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Latency](https://img.shields.io/badge/Latency-%3C30ms-brightgreen)](https://rapidapi.com/organization/aether-protocol-labs)
[![RapidAPI](https://img.shields.io/badge/RapidAPI-Verified_Provider-orange.svg)](https://rapidapi.com/organization/aether-protocol-labs)

Enterprise-grade Kick.com API client with **pre-warmed Kasada `kpsdk` telemetry tokens**, live channel resolution, HLS streams, and WebSocket presence.

---

## ⚡ Key Highlights
- **Sub-30ms Telemetry:** Pre-warmed background buffer provides valid Kasada `x-kpsdk-ct` and `x-kpsdk-cd` tokens instantly.
- **Zero Headless Overhead:** No need to run slow Puppeteer or Playwright instances on your servers.
- **Async & Sync:** Fully supported `asyncio` client with connection pooling.
- **100% Policy-Safe:** Enterprise telemetry protocol compliance.

---

## 📦 Installation
```bash
pip install kickstream
# or with uv
uv add kickstream
```

---

## 🔑 Getting Your Free API Key
Get your free API key (50 calls/month included) on RapidAPI:  
👉 **[Get Free Key on RapidAPI Hub](https://rapidapi.com/organization/aether-protocol-labs)**

---

## 💻 Quickstart
```python
from kickstream import KickStreamClient

client = KickStreamClient(api_key="YOUR_RAPIDAPI_KEY")

# 1. Fetch channel info & live stream status
channel = client.get_channel_info("xqc")
print("Channel data:", channel)

# 2. Get pre-warmed Kasada telemetry headers for raw HTTP scraping
telemetry = client.get_kasada_telemetry("https://kick.com")
headers = telemetry["headers"]
print("Pre-warmed headers:", headers)
```

### ⚡ Async Usage
```python
import asyncio
from kickstream import AsyncKickStreamClient

async def run():
    client = AsyncKickStreamClient(api_key="YOUR_RAPIDAPI_KEY")
    channel = await client.get_channel_info("westcol")
    print(channel)

asyncio.run(run())
```
